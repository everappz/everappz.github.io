---
title: "Evermusic・FlacboxでトラックコレクションをM3U、CSV、TXTにエクスポートする方法"
date: 2024-01-31
description: "Evermusic・Flacboxで最近の項目、お気に入り、プレイリスト、アルバムをM3U、CSV、TXT形式にエクスポートする方法を学びましょう。Last.fmのスクロブルや他のデバイスでの再生に最適です。"
keywords: ["evermusic エクスポート", "flacbox エクスポート", "m3uにエクスポート", "プレイリストをcsvにエクスポート", "m3u txt csv プレイリスト", "音楽エクスポート"]
tags: ["evermusic", "最近の項目", "お気に入り", "エクスポート", "m3u", "プレイリスト", "csv", "txt", "アルバム"]
---

{{< author-byline >}}


**要約:** Evermusic・Flacboxでは、あらゆるトラックコレクション（最近の項目、お気に入り、プレイリスト、アルバム）をCSV、TXT、またはM3Uファイルにエクスポートできます。これらのエクスポートを使用して、Last.fmへのスクロブル、ライブラリのバックアップ、他のデバイスでのプレイリスト再生が可能です。

## はじめに

アプリから最近の項目、お気に入り、アルバム、プレイリストを外部ファイルにエクスポートすることは非常に便利です。これらのファイルを使用して、[Last.fm](http://Last.fm)などのスクロブルサービスでリスニング履歴を更新したり、外部デバイスでプレイリストを再生したりできます。Evermusic・Flacboxなら、このプロセスは簡単です。ここでは、最近の項目をCSV/TXTに、プレイリストをM3Uにエクスポートする方法をご紹介します。ただし、この機能はアプリ内のすべてのトラックコレクションで利用できます。

## フォーマットを選択

最近の項目をエクスポートするには、「ミュージックライブラリ」セクションを開き、「最近の項目」メニュー項目を選択します。

![ミュージックライブラリ](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

次の画面で、右上の「その他」ボタンをタップし、「曲リストをエクスポート」を選択します。

![最近の項目をエクスポート](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

「ファイル形式を選択」画面では、CSV、TXT、M3Uのオプションがあります。

- CSV

カンマ区切り値の略で、データをきれいな表形式に整理するのに最適です。出力ファイルには、アーティスト名、アルバム名、トラック名、タイムスタンプ（トラックを聴いた時間）、アルバムアーティスト名、トラック再生時間などのパラメータが含まれます。このファイルは、[こちら](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/)で説明されているように、[Last.fm](http://Last.fm)などのスクロブルサービスでリスニング履歴を更新するために使用できます。

- TXT

プレーンテキストファイルです。シンプルで分かりやすく、アーティスト名、アルバム名、トラック名、再生時間などのパラメータが含まれます。テキスト形式でトラックリストが必要な場合に便利です。

- M3U

この形式は、プレイリスト作成の標準フォーマットです。曲リストをエクスポートして、元のファイルがなくても（メディアファイルの絶対URLオプションを選択した場合）、あらゆるデバイスでトラックを楽しむことができます。出力ファイルには、再生時間、アーティスト名、トラック名、メディアファイルの場所などのパラメータが含まれます。

## CSV形式

では、CSVを選択して結果を確認しましょう。CSVを選んで「エクスポート」ボタンを押すだけです。

![ファイル形式を選択](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

エクスポートが完了すると、2つのオプションのあるアラートが表示されます。「ファイルを表示」をタップすると、ドキュメントディレクトリに生成されたファイルが表示されます。

![エクスポート完了](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

このファイルを送信したり、外部テキストエディタで開いたり、[Last.fm](http://Last.fm)でリスニング履歴を更新するために使用できます。

![エクスポート結果ファイルのフォルダ](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

出力CSVファイルには、以下の形式でフィールドが含まれます：

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

例：

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![エクスポートされたCSVファイル](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT形式

出力TXTファイルには、以下の形式でフィールドが含まれます：

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

例：

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![エクスポートされたTXTファイル](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U形式

次に、プレイリストをM3U形式にエクスポートする方法をご案内します。M3Uはプレイリストファイルの事実上の標準です。プレイリストのエクスポートを成功させるための主な前提条件は、プレイリスト内のすべてのファイルが同じストレージ上にあることです。これはGoogle Driveなどのクラウドサービス、ローカルファイル、またはデバイス上のファイルのいずれかです。エクスポートプロセスを開始するには、任意のプレイリストを開き、右上の「その他」ボタンをタップしてから、「曲リストをエクスポート」メニュー項目を選択します。

![プレイリスト画面](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

次の画面で「M3U」ファイル形式を選択すると、「メディアファイルの場所タイプ」の2つのオプションが表示されます：

![エクスポートファイル形式選択画面](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. 「相対パス」を選択すると、プレイリストファイルからの相対パスでメディアファイルの場所が記録されます。例：

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   この場合、エクスポート完了後にM3Uファイルの場所を変更しないでください。変更するとメディアファイルのパスが無効になります。プレイリストの再生を開始するには、エクスポートされたプレイリストファイルをタップするだけで、アプリが自動的にストレージ上のメディアファイルを見つけて再生を開始します。また、プレイリストをストレージにエクスポートしてから、新しいデバイスで再度インポートすることもできます。

2. 「絶対URL」を選択すると、アプリがメディアファイルのダイレクトURLを生成します。これにより、すべてのメディアファイルがプレイリストファイルと同じストレージにある必要なく、あらゆるデバイス・アプリケーションでプレイリストを再生できます。このオプションは、ダイレクトファイルURLを生成できるクラウドストレージでのみサポートされています。ただし、生成されたURLの有効期限が限られている場合があり、一定時間後に期限切れになることがあります。サポートされているクラウドサービスの一覧：iCloud Drive、pCloud、PanBaidu、MyCloudHome、DLNA、MediaFire、OneDrive、Box、Dropbox、GoogleDrive、WebDav（ゲストモードの場合）  

出力メディアファイルURLは以下のようになります：

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

「メディアファイルの場所タイプ」を選択したら、「エクスポート」をタップします。アプリがM3Uファイルのエクスポート先フォルダを選択するよう求めます。「完了」をタップして選択を確認します。

![フォルダを選択](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

アプリがM3Uファイルを生成し、エクスポート先フォルダにアップロード/移動します。

![M3Uファイルをアップロード中](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

エクスポートが完了すると、「ファイルを表示」オプションのあるシステムアラートが表示されます。

![エクスポート完了アラート](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

タップすると、アプリ内でエクスポートされたファイルが表示されます。

![ファイルリスト内のエクスポートされたM3Uファイル](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

前のステップで「メディアファイルの場所タイプ」として「相対パス」を選択した場合、出力ファイルは以下の形式になります：

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![相対パスのM3U例](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

「絶対URL」オプションの場合、アプリは以下の形式でM3Uファイルを生成します：

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![絶対ファイルURLのM3U例](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

M3Uプレイリストをサポートするあらゆるデバイス・アプリケーションでそのファイルを開くことができます。

![外部アプリで開いたM3Uプレイリスト](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## まとめ

Evermusic・Flacboxからトラックをエクスポートすることで、音楽データを完全にコントロールできます。リスニング履歴のバックアップ、Last.fmへのスクロブル、外部デバイスでのプレイリスト再生など、M3U、CSV、TXTのエクスポートオプションは、柔軟性と互換性のための強力なツールです。これらの機能を活用して、プラットフォームをまたいで音楽コレクションの整理、共有、再訪を充実させましょう。

## FAQ

{{% details title="Last.fmのスクロブルにはどのエクスポート形式を使用すべきですか？" closed="true" %}}
CSVを使用してください。Last.fm-Scrubbler-WPFなどのスクロブルツールに必要なタイムスタンプと完全なメタデータが含まれています。
{{% /details %}}

{{% details title="プレイリスト以外のトラックコレクションもエクスポートできますか？" closed="true" %}}
はい。同じ手順で、最近の項目、お気に入り、アルバム、プレイリスト、その他アプリ内のあらゆるトラックコレクションをエクスポートできます。
{{% /details %}}

{{% details title="M3Uプレイリストは他のデバイスで動作しますか？" closed="true" %}}
エクスポート時に絶対URLオプションを選択した場合、M3UファイルはM3Uプレイリストをサポートするあらゆるデバイスで再生できます。ただし、一部のクラウドURLは時間の経過とともに期限切れになる場合があります。
{{% /details %}}

{{% details title="エクスポート機能は無料ですか？" closed="true" %}}
はい。M3U、CSV、TXTへのトラックコレクションのエクスポートは、Evermusic・Flacboxの無料版とプレミアム版の両方で利用できます。
{{% /details %}}

{{% details title="絶対URLエクスポートをサポートしているクラウドサービスは？" closed="true" %}}
絶対URLエクスポートは、iCloud Drive、pCloud、PanBaidu、MyCloudHome、DLNA、MediaFire、OneDrive、Box、Dropbox、Google Drive、WebDAV（ゲストモード）でサポートされています。
{{% /details %}}
