---
title: "AVAssetResourceLoaderを使ったiOSオーディオストリーミング"
date: 2015-06-20
description: "カスタムURLスキームとディスクキャッシュを使用して、AVAssetResourceLoaderDelegateとAVPlayerでiOSのオーディオをストリーミングおよびキャッシュする方法を学びます。"
keywords: ["iOSオーディオストリーミング", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayerチュートリアル", "AVFoundationオーディオ", "AVAssetResourceLoadingRequest", "カスタムオーディオプレーヤーiOS", "クラウドオーディオストリーミングiOS", "オーディオキャッシュiOS", "Swift AVPlayerカスタムスキーム"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
draft: false
aliases:
  - /post/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
  - /amp/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
  - /single-post/Audio-Streaming-and-Caching-in-iOS-using-AVAssetResourceLoader-and-AVPlayer/
  - /index.php/2015/02/10/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**TL;DR:** カスタムURLスキームと組み合わせた`AVAssetResourceLoaderDelegate`を使用して、AVPlayerのリソース読み込みをインターセプトします。これにより、クラウドサービスへのカスタム認証ヘッダーの追加、オーディオのディスクへのキャッシュ、ストリーミング動作の制御が可能になります -- ローカルHTTPプロキシを書かずに済みます。完全なソースコードは[GitHub](http://github.com/leshkoapps/AVAssetResourceLoader)で公開されています。

---

## なぜAVPlayerにカスタムリソースローダーが必要なのか

`AVPlayer`はローカルファイルとリモートURLからオーディオを再生します。ほとんどのクラウドサービス（Dropbox、Google Drive、Box）では、直接ダウンロードURLを渡すだけで再生がすぐに動作します。

しかし、**Yandex.Disk**や**WebDAV**などの一部のサービスは、GETリクエストにカスタム認証ヘッダーを必要とします。`AVPlayer`にはこれらのヘッダーを注入する組み込みの方法がありません。

解決策: `AVURLAsset`の`resourceLoader`プロパティを使用します。このAPIはリソース読み込みリクエストをインターセプトし、複雑さなしにローカルHTTPプロキシのように機能します。

### 仕組み

`AVPlayer`はURLスキームを認識しない場合に`resourceLoader`を使用します。`https://`をカスタムスキーム（例: `customscheme://`）に置き換えることで、AVPlayerがすべての読み込みをアプリに委任するよう強制できます。

2つの`AVAssetResourceLoaderDelegate`メソッドを実装する必要があります:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- AVPlayerがデータを必要とするときに呼び出されます。`AVAssetResourceLoadingRequest`を保存し、データ読み込み操作を開始します。
2. **`resourceLoader:didCancelLoadingRequest:`** -- リクエストがキャンセルまたは上書きされたときに呼び出されます。

## カスタムAVPlayerの作成方法

カスタムURLスキームでAVPlayerをセットアップします:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

このコードは:
- カスタムスキームでURLを定義します
- メインキューにデリゲートを持つ`AVURLAsset`を作成します
- アセットから`AVPlayerItem`を構築します
- `AVPlayer`を初期化します

## リソースローダーデリゲートの実装

サーバーからのデータ取得を処理し、`AVURLAsset`に返すための`LSFilePlayerResourceLoader`というクラスを作成します。リソースURLをキーとしてローダーインスタンスをディクショナリに保存します。

```objc
- (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest *)loadingRequest {
    NSURL *resourceURL = [loadingRequest.request URL];
    if ([resourceURL.scheme isEqualToString:@"customscheme"]) {
        LSFilePlayerResourceLoader *loader = [self resourceLoaderForRequest:loadingRequest];
        if (!loader) {
            loader = [[LSFilePlayerResourceLoader alloc] initWithResourceURL:resourceURL session:self.session];
            loader.delegate = self;
            [self.resourceLoaders setObject:loader forKey:[self keyForResourceLoaderWithURL:resourceURL]];
        }
        [loader addRequest:loadingRequest];
        return YES;
    }
    return NO;
}

- (void)resourceLoader:(AVAssetResourceLoader *)resourceLoader didCancelLoadingRequest:(AVAssetResourceLoadingRequest *)loadingRequest {
    LSFilePlayerResourceLoader *loader = [self resourceLoaderForRequest:loadingRequest];
    [loader removeRequest:loadingRequest];
}
```

これらのメソッドはURLスキームを確認し、ローダーを作成または取得し、リクエストをローダーのキューに追加します。未知のスキームは`NO`を返します。

## LSFilePlayerResourceLoaderインターフェース

```objc
@interface LSFilePlayerResourceLoader : NSObject
@property (nonatomic, readonly, strong) NSURL *resourceURL;
@property (nonatomic, readonly) NSArray *requests;
@property (nonatomic, readonly, strong) YDSession *session;
@property (nonatomic, readonly, assign) BOOL isCancelled;
@property (nonatomic, weak) id<LSFilePlayerResourceLoaderDelegate> delegate;
- (instancetype)initWithResourceURL:(NSURL *)url session:(YDSession *)session;
- (void)addRequest:(AVAssetResourceLoadingRequest *)loadingRequest;
- (void)removeRequest:(AVAssetResourceLoadingRequest *)loadingRequest;
- (void)cancel;
@end

@protocol LSFilePlayerResourceLoaderDelegate <NSObject>
@optional
- (void)filePlayerResourceLoader:(LSFilePlayerResourceLoader *)resourceLoader didFailWithError:(NSError *)error;
- (void)filePlayerResourceLoader:(LSFilePlayerResourceLoader *)resourceLoader didLoadResource:(NSURL *)resourceURL;
@end
```

## データ読み込み: 2ステップのプロセス

読み込みリクエストがキューに入ると、2つの操作が順番に実行されます:

- **contentInfoOperation** -- コンテンツの長さ、MIMEタイプ、バイト範囲のサポートを照会します
- **dataOperation** -- `requestedOffset`から始まるファイルデータを取得します

## ディスクキャッシュ戦略

ダウンロードされたデータはディスク上の一時ファイルに書き込まれます。同じコンテンツへのその後のリクエストはこのキャッシュから提供され、冗長なネットワーク呼び出しを避けます。このアプローチは:

- 帯域幅の使用量を削減します
- ほぼ即時の再生を可能にします
- キャッシュされた範囲内のシーク操作をサポートします

## 保留中のリクエストの処理

`processPendingRequests`メソッドは各リクエストの`contentInformationRequest`にメタデータを入力し、キャッシュされたバイト範囲を配信します。完了したリクエストはキューから削除されます。

## ソースコードと次のステップ

このチュートリアルでは、カスタム認証ヘッダーを使用したクラウドオーディオストリーミングのための`AVAssetResourceLoaderDelegate`実装の概要を説明しました。完全なソースコードは[GitHub](http://github.com/leshkoapps/AVAssetResourceLoader)で公開されています。

このアプローチは、iOSおよびmacOSでDropbox、Google Drive、OneDrive、Yandex.Diskなどのクラウドサービスから音楽をストリーミングする[Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198)のオーディオストリーミングエンジンを動かしています。

## よくある質問

{{% details title="直接URLの代わりにAVAssetResourceLoaderDelegateを使うのはいつですか？" closed="true" %}}
クラウドサービスがカスタム認証ヘッダーを必要とする場合、ストリーミングされたオーディオのディスクキャッシュが必要な場合、またはデータの読み込みとバッファリングの方法を細かく制御したい場合に使用します。
{{% /details %}}

{{% details title="このアプローチはSwiftでも動作しますか？" closed="true" %}}
はい。`AVAssetResourceLoaderDelegate`プロトコルはSwiftでも同じように動作します。ここにあるObjective-Cの例はそのまま翻訳できます。
{{% /details %}}

{{% details title="ビデオストリーミングにも使えますか？" closed="true" %}}
はい。`AVAssetResourceLoaderDelegate`はビデオを含むAVPlayerがサポートするあらゆるメディアタイプで動作します。同じカスタムスキームアプローチが適用されます。
{{% /details %}}

{{% details title="バックグラウンドでのオーディオ再生はサポートされていますか？" closed="true" %}}
はい。アプリの機能で「Audio, AirPlay, and Picture in Picture」バックグラウンドモードを有効にし、`AVAudioSession`を正しく設定する限り、サポートされます。
{{% /details %}}
