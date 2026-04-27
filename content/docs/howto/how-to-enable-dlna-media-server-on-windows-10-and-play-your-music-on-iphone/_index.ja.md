---
title: "Windows 10でDLNAメディアサーバーを有効にしてiPhoneで音楽を再生する方法"
date: 2019-11-26
description: "Windows 10でDLNAサーバーを有効にし、Evermusicアプリを使ってiPhoneに音楽をストリーミング。ステップバイステップのセットアップガイド付き。"
keywords: ["evermusic", "dlna", "windows 10", "iphone 音楽ストリーミング", "メディアサーバー", "ローカルネットワーク", "upnp"]
tags: ["evermusic", "音楽", "クラウド", "iphone", "ストレージ", "ローカル", "nas", "windows", "wifi", "聴く", "ネットワーク", "リモート", "ホーム", "オンライン", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**要約：** Windows 10には内蔵DLNAサーバーがあります。ネットワークと共有の設定で有効にし、iPhoneの無料アプリ**Evermusic**を使ってWi-Fi経由で音楽ライブラリ全体をストリーミングできます。サードパーティのサーバーソフトウェアは不要です。

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA：表紙" caption="Windows 10とEvermusicを使用したiPhoneへのDLNA音楽ストリーミング" width="800" >}}

DLNA（Digital Living Network Alliance）は、ネットワーク上のDLNA対応デバイス間で音楽を含むさまざまなメディアコンテンツを簡単にストリーミングできる強力なツールです。良いニュースは、Windows 10および以前のバージョンにはDLNA機能が内蔵されており、サードパーティのメディアサーバーが不要なことです。ここでは、Windows 10でDLNAメディアサーバーを有効にして、iPhoneで音楽ストリーミングを楽しむ方法を紹介します。

## Windows 10でDLNAメディアサーバーを有効にする方法

1. 「スタート」ボタンをクリックします。  
2. 「設定」アイコンを選択します。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="サーバー設定" caption="Windows設定を開く" width="500" >}}

3. 「Windows設定」画面で、「ネットワークとインターネット」を選択します。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows設定" caption="ネットワークとインターネットを選択" width="500" >}}

4. 「ネットワーク」の下で、「ネットワークと共有センター」を選択します。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="共有センター" caption="ネットワークと共有センターを開く" width="500" >}}

5. 「ネットワークと共有センター」画面で、左メニューの「共有の詳細設定の変更」をクリックします。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="共有の詳細設定" caption="共有の詳細設定の変更" width="500" >}}

6. 「共有の詳細設定」画面で、「すべてのネットワーク」セクションまでスクロールし、矢印をクリックして展開します。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="探索を有効にする" caption="すべてのネットワーク設定を展開" width="500" >}}

7. 「メディアストリーミングを有効にする」をクリックしてDLNAサーバーを有効にします。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="サーバーを有効にする" caption="メディアストリーミングサーバーを有効にする" width="500" >}}

8. メディアライブラリに名前を付け、アクセスを許可するデバイスを選択します。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="メディアライブラリ名" caption="DLNAメディアライブラリに名前を付ける" width="500" >}}

9. 「OK」をクリックして確認します。これで、ミュージック、ピクチャ、ビデオなどの個人フォルダが、UPnP対応のストリーミングデバイスに表示されます。

## Windows 10でDLNAメディアサーバーを無効にする方法

1. 「スタート」をクリックし、検索フィールドに「services」と入力します。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windowsサービス" caption="Windowsサービスを開く" width="500" >}}

2. 「サービス」画面で、「Windows Media Player Network Sharing Service」を探してスクロールします。  
3. ダブルクリックし、「スタートアップの種類」を「手動」に設定します。  
4. 「停止」ボタンをクリックしてサービスを停止します。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="DLNAサービス停止" caption="DLNAネットワーク共有サービスを無効にする" width="500" >}}

## iPhoneでDLNAサーバーから音楽を再生する方法

1. App Storeから無料の**Evermusic**アプリをインストールします：  
   [Evermusicアプリ](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. 「接続」タブを開き、「ローカルネットワーク」セクションの「利用可能なデバイス」をタップします。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic接続" caption="Evermusic：接続画面" width="500" >}}

3. デバイスリストが読み込まれるまで数秒待ち、Windows Media Player DLNAサーバーをタップします（例：「MSEDGEWIN10: My Windows Library」）。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="利用可能なデバイス" caption="Evermusicで利用可能なDLNAサーバー" width="500" >}}

4. メディアサーバーで利用可能なフォルダのリストが表示されます。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusicフォルダ" caption="DLNAサーバーの共有フォルダを閲覧" width="500" >}}

5. オーディオファイルが含まれるフォルダを開きます。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="フォルダ内容" caption="共有DLNAフォルダの内容を表示" width="500" >}}

6. 任意のファイルをタップしてオーディオプレーヤーを起動します。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="オーディオプレーヤー" caption="EvermusicでDLNAからオーディオファイルを再生" width="500" >}}

7. オーディオ体験を向上させるには、画面下部の音量インジケーター付近の「イコライザー」アイコンをタップして、プリアンプ付きiPodスタイルイコライザーを有効にします。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="イコライザー" caption="内蔵イコライザーで再生品質を向上" width="500" >}}

## まとめ

Windows 10のDLNAメディアサーバーとiPhoneのEvermusicを使えば、コンピューターからモバイルデバイスへのシームレスな音楽ストリーミングを楽しめます。ストレージの制限にさよならを告げ、オンデマンドの音楽を楽しみましょう！

## よくある質問

{{% details title="Windows 10にサーバーソフトウェアをインストールする必要がありますか？" closed="true" %}}
いいえ。Windows 10には内蔵DLNAメディアサーバーが含まれています。ネットワークと共有センターの設定でメディアストリーミングを有効にするだけです。サードパーティソフトウェアは不要です。
{{% /details %}}

{{% details title="iPhoneは同じWi-Fiネットワークに接続する必要がありますか？" closed="true" %}}
はい。DLNAストリーミングはローカルネットワーク上で動作します。EvermusicがDLNAサーバーを検出するには、Windows 10 PCとiPhoneの両方が同じWi-Fiネットワークに接続されている必要があります。
{{% /details %}}

{{% details title="DLNA経由でどのオーディオフォーマットをストリーミングできますか？" closed="true" %}}
Windows DLNAサーバーは、フォーマットに関係なくミュージックフォルダのファイルを共有します。EvermusicはMP3、FLAC、AAC、WAV、OGG、AIFFなど多くのフォーマットに対応しているため、サーバーからほぼすべてのオーディオファイルを再生できます。
{{% /details %}}

{{% details title="Evermusicの代わりにFlacboxを使用できますか？" closed="true" %}}
はい。FlacboxもDLNA/UPnPの閲覧と再生に対応しています。どちらのアプリでもWindows DLNAサーバーから音楽を検出して再生できます。
{{% /details %}}

{{% details title="DLNAストリーミングはモバイルデータを使用しますか？" closed="true" %}}
いいえ。DLNAはローカルWi-Fiネットワーク上でのみ動作します。モバイルデータは一切使用しません。ただし、再生中は両方のデバイスが同じネットワークに接続されている必要があります。
{{% /details %}}
