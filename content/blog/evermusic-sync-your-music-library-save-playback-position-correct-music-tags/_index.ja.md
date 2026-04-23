---
title: "Evermusic 2.3：自動同期、再生位置、タグ機能"
date: 2016-05-26
description: "Evermusic 2.3はクラウド音楽の自動同期、オーディオブックの再生位置保存、バックグラウンドメタデータ読み取り、ID3タグ修正機能を追加しました。"
keywords: ["Evermusic", "クラウド音楽プレーヤー", "音楽同期iOS", "再生位置を保存", "オーディオブック再生", "メタデータリーダー", "ID3タグ修正", "クラウドから音楽ストリーミング", "Dropbox用音楽アプリ", "Google Driveプレーヤー", "自動音楽ライブラリ同期", "オーディオブック位置保存iOS"]
tags: ["evermusic", "音楽", "再生", "マネージャー", "エディター", "同期", "位置", "id3タグ", "クラウド", "新機能"]
draft: false
aliases:
  - /post/evermusic-sync-your-music-library-save-playback-position-correct-music-tags/
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/evermusic-sync-your-music-library-save-playback-position-correct-music-tags/21260c_641f376e779e47d4927b43c210d3c87f~mv2.jpeg)

## Evermusic 2.3が音楽ライブラリにもたらすもの

**TL;DR:** Evermusic 2.3はクラウドフォルダの自動同期、再生位置の保存（オーディオブックに最適）、バックグラウンドでのメタデータ読み取り、ID3タグの自動修正を導入します。Dropbox、Google Drive、OneDrive、MEGA、WebDAV、SMBで動作します。

Evermusicは、Dropbox、Google Drive、OneDrive、MEGA、WebDAV、SMBサーバーからオーディオをストリーミングまたはダウンロードできるiOSおよびmacOS用のクラウド音楽プレーヤーです。バージョン2.3では、ユーザーが要望していた4つの機能が追加されました。まだEvermusicを試していない方は、[App Storeからダウンロード](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198)してください。

## 音楽ライブラリの自動同期

![](/blog/evermusic-sync-your-music-library-save-playback-position-correct-music-tags/21260c_7ae554f5982649758176de1c994b6b05~mv2.jpg)

手動でのフォルダスキャンはもう不要です。Evermusic 2.3は選択したクラウドフォルダを監視し、ファイルが変更されると音楽ライブラリを自動的に更新します。追跡したいフォルダを設定すれば、あとはアプリがバックグラウンドで処理します。

これにより：

- 新しいアップロードが手動更新なしでライブラリに表示されます
- 削除されたファイルは自動的にライブラリから削除されます
- アプリがフォアグラウンドでもバックグラウンドでも変更が同期されます

## オーディオブックとポッドキャストの再生位置を保存

![](/blog/evermusic-sync-your-music-library-save-playback-position-correct-music-tags/21260c_3baab435323443bcb788e5f6da0d39f3~mv2.jpg)

オーディオブックや講義を一時停止し、中断したところから正確に再開できます。有効にすると、Evermusicは各ファイルの再生位置を自動的に記憶します — 手動のブックマークは不要です。

最適な用途：

- オーディオブック
- 講義やコース
- ポッドキャスト
- 長時間の録音

アプリのオーディオ設定で有効にしてください。

## バックグラウンドでのメタデータ読み取り

![](/blog/evermusic-sync-your-music-library-save-playback-position-correct-music-tags/21260c_511ee81f8b094059a2c14f1cfc32a1cc~mv2.jpg)

大規模な音楽コレクションの場合、メタデータの読み取りがバックグラウンドで実行されるようになりました。閲覧中や再生中に、Evermusicがオーディオファイルをスキャンし、アーティスト、アルバム、ジャンル別に整理します。これにより、数千曲のコレクションでのライブラリ閲覧が大幅に高速化されます。

## ID3タグの自動修正

![](/blog/evermusic-sync-your-music-library-save-playback-position-correct-music-tags/21260c_2374803418e74c8680fd3420fc1fc35a~mv2.jpg)

Evermusicはオンラインデータベースを使用して、無効または不完全なID3タグを検出し修正します。乱雑な、欠落した、または不正確なメタデータを持つファイルが自動的にクリーンアップされ、手動編集なしでライブラリが整理された状態に保たれます。

---

[Evermusicをダウンロード](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198)して、今すぐこれらの機能をお試しください。

## よくある質問

{{% details title="Evermusicの自動同期はすべてのクラウドサービスで動作しますか？" closed="true" %}}
はい。自動同期はDropbox、Google Drive、OneDrive、MEGA、WebDAV、SMBで動作します。監視したいフォルダを選択すれば、Evermusicがライブラリを最新の状態に保ちます。
{{% /details %}}

{{% details title="Evermusicはオーディオブックの位置を保存できますか？" closed="true" %}}
はい。オーディオ設定で再生位置の保存を有効にしてください。Evermusicは各ファイルで停止した位置を記憶するので、手動のブックマークなしで再開できます。
{{% /details %}}

{{% details title="バックグラウンドでのメタデータ読み取りはどのように機能しますか？" closed="true" %}}
Evermusicは他の機能を使用中にバックグラウンドでID3タグとファイルメタデータを読み取ります。アーティスト、アルバム、ジャンル別にライブラリを自動的に整理します。
{{% /details %}}

{{% details title="Evermusicは壊れた音楽タグを修正してくれますか？" closed="true" %}}
はい。自動タグ修正機能がオンラインデータベースとファイルを照合し、無効な、不完全な、または欠落しているID3メタデータを修正します。
{{% /details %}}

{{% details title="Evermusicは無料でダウンロードできますか？" closed="true" %}}
Evermusicは無料でダウンロードでき、オプションのプレミアム機能はアプリ内課金で利用できます。
{{% /details %}}
