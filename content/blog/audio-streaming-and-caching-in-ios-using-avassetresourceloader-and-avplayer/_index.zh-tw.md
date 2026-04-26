---
title: "使用 AVAssetResourceLoader 實現 iOS 音訊串流播放"
date: 2015-06-20
description: "學習如何使用 AVAssetResourceLoaderDelegate 和 AVPlayer，透過自訂 URL 方案和磁碟快取在 iOS 中實現音訊串流傳輸與快取。"
keywords: ["iOS 音訊串流", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer 教學", "AVFoundation 音訊", "AVAssetResourceLoadingRequest", "iOS 自訂音訊播放器", "iOS 雲端音訊串流", "iOS 音訊快取", "Swift AVPlayer 自訂方案"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**TL;DR：** 使用帶有自訂 URL 方案的 `AVAssetResourceLoaderDelegate` 來攔截 AVPlayer 的資源載入。這讓你可以為雲端服務新增自訂授權標頭、將音訊快取到磁碟，並控制串流行為——無需編寫本地 HTTP 代理。完整原始碼託管於 [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader)。

---

## 為什麼 AVPlayer 需要自訂資源載入器

`AVPlayer` 可以播放本地檔案和遠端 URL 的音訊。對於大多數雲端服務（Dropbox、Google Drive、Box），你可以傳入直接下載連結，播放即可開箱即用。

然而，像 **Yandex.Disk** 和 **WebDAV** 這類服務在 GET 請求中需要自訂授權標頭。`AVPlayer` 沒有內建方式來注入這些標頭。

解決方案：使用 `AVURLAsset` 的 `resourceLoader` 屬性。該 API 攔截資源載入請求，如同本地 HTTP 代理，但沒有複雜的實作難度。

### 運作原理

當 AVPlayer 無法識別 URL 方案時，會使用 `resourceLoader`。透過將 `https://` 替換為自訂方案（如 `customscheme://`），你可以強制 AVPlayer 將所有載入委派給你的應用程式。

你需要實作兩個 `AVAssetResourceLoaderDelegate` 方法：

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- 當 AVPlayer 需要資料時呼叫。儲存 `AVAssetResourceLoadingRequest` 並啟動資料載入操作。
2. **`resourceLoader:didCancelLoadingRequest:`** -- 當請求被取消或被替代時呼叫。

## 如何建立自訂 AVPlayer

使用自訂 URL 方案設定 AVPlayer：

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

此程式碼：
- 定義帶有自訂方案的 URL
- 在主佇列上建立帶有委派的 `AVURLAsset`
- 從資源建構 `AVPlayerItem`
- 初始化 `AVPlayer`

## 實作資源載入器委派

建立名為 `LSFilePlayerResourceLoader` 的類別來處理從伺服器擷取資料並將其傳回 `AVURLAsset`。將載入器實例儲存在以資源 URL 為鍵的字典中。

```objc
- (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest *)loadingRequest {
    NSURL *resourceURL = [loadingRequest.request URL];
    if ([resourceURL.scheme isEqualToString:@"customscheme"]) {
        LSFilePlayerResourceLoader *loader = 
        [self resourceLoaderForRequest:loadingRequest];
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

這些方法檢查 URL 方案，建立或取得載入器，並將請求新增至載入器佇列。無法識別的方案回傳 `NO`。

## LSFilePlayerResourceLoader 介面

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

## 資料載入：兩步驟流程

當載入請求進入佇列時，兩個操作依序執行：

- **contentInfoOperation** -- 查詢內容長度、MIME 類型和位元組範圍支援
- **dataOperation** -- 從 `requestedOffset` 開始擷取檔案資料

## 磁碟快取策略

下載的資料被寫入磁碟上的暫存檔案。後續對相同內容的請求從此快取提供，避免多餘的網路呼叫。此方法：

- 減少頻寬使用
- 實現幾乎即時的重播
- 支援在快取範圍內的快進操作

## 處理待處理請求

`processPendingRequests` 方法用中繼資料填充每個請求的 `contentInformationRequest`，並傳遞快取的位元組範圍。已完成的請求從佇列中移除。

## 原始碼與後續步驟

本教學提供了實作 `AVAssetResourceLoaderDelegate` 進行帶自訂授權標頭的雲端音訊串流的高層次概述。完整原始碼可在 [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader) 取得。

此方法為 [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) 的音訊串流引擎提供支援，該應用程式可在 iOS 和 macOS 上從 Dropbox、Google Drive、OneDrive、Yandex.Disk 及其他雲端服務串流播放音樂。

## 常見問題

{{% details title="何時應該使用 AVAssetResourceLoaderDelegate 而不是直接 URL？" closed="true" %}}
當雲端服務需要自訂授權標頭、需要對串流音訊進行磁碟快取，或希望精細控制資料載入和緩衝方式時，請使用它。
{{% /details %}}

{{% details title="這種方法適用於 Swift 嗎？" closed="true" %}}
是的。`AVAssetResourceLoaderDelegate` 協定在 Swift 中的運作方式完全相同。這裡的 Objective-C 範例可以直接轉換。
{{% /details %}}

{{% details title="這可以用於視訊串流嗎？" closed="true" %}}
可以。`AVAssetResourceLoaderDelegate` 適用於 AVPlayer 支援的任何媒體類型，包括視訊。同樣的自訂方案方法同樣適用。
{{% /details %}}

{{% details title="這是否支援背景音訊播放？" closed="true" %}}
是的，只要你在應用程式的功能中啟用了「Audio, AirPlay, and Picture in Picture」背景模式，並正確設定了 `AVAudioSession`。
{{% /details %}}
