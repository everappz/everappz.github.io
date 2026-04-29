---
title: 如何在 Evermusic 和 Flacbox 中將曲目合集匯出為 M3U、CSV 和 TXT
date: 2024-01-31
description: 了解如何將 Evermusic 和 Flacbox 中的最近使用的、最愛項目、播放清單和專輯匯出為 M3U、CSV 或 TXT 格式。非常適合 Last.fm 記錄和在其他裝置上播放。
keywords: ["evermusic 匯出", "flacbox 匯出", "匯出為 m3u", "匯出播放清單為 csv", "m3u txt csv 播放清單", "音樂匯出"]
tags: ["evermusic", "recents", "favorites", "export", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**摘要：** Evermusic 和 Flacbox 允許您將任何曲目合集（最近使用的、最愛項目、播放清單、專輯）匯出為 CSV、TXT 或 M3U 檔案。使用這些匯出檔案可以向 Last.fm 記錄播放歷史、備份音樂庫或在其他裝置上播放您的播放清單。

## 簡介

將應用程式中的最近使用的、最愛項目、專輯和播放清單匯出到外部檔案非常實用。您可以使用這些檔案在 [Last.fm](http://Last.fm) 等記錄服務上更新收聽歷史，或在外部裝置上收聽播放清單。使用 Evermusic 和 Flacbox，這個過程非常簡單。在這裡，我們將向您展示如何將最近使用的匯出為 CSV/TXT，以及將播放清單匯出為 M3U。不過，此功能適用於應用程式內的任何曲目合集。

## 選擇格式

要匯出最近使用的曲目，請開啟「音樂庫」區段，選擇「最近使用的」選單項目。

![音樂庫](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

在下一個畫面上，點擊右上角的「更多」按鈕，選擇「匯出歌曲清單」。

![匯出最近使用的](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

在「選擇檔案格式」畫面上，您有幾個選項 - CSV、TXT、M3U。

- CSV

這是逗號分隔值的縮寫，非常適合將資料整理成整齊的表格格式。在目標檔案中，您將找到藝術家名稱、專輯名稱、曲目名稱、時間戳記（您收聽曲目的時間）、專輯藝術家名稱和曲目時長等參數。您可以稍後使用該檔案在 [Last.fm](http://Last.fm) 等記錄服務上更新收聽歷史，如[此處](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/)所述。

- TXT

這是一個純文字檔案。簡單直觀，包含藝術家名稱、專輯名稱、曲目名稱和時長等參數。如果您只需要文字形式的曲目清單，這會很有用。

- M3U

此格式是建立播放清單的事實標準。它的優點在於您可以匯出歌曲清單，並在任何裝置上欣賞曲目，即使您沒有原始檔案（如果選擇了媒體檔案的絕對 URL 選項進行匯出）。在輸出檔案中，您將找到時長、藝術家名稱、曲目名稱和媒體檔案位置等參數。

## CSV 格式

現在，讓我們選擇 CSV，看看會得到什麼。只需選擇 CSV 並點擊「匯出」按鈕。

![選擇檔案格式](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

匯出完成後，您將看到一個包含兩個選項的提示。點擊「顯示檔案」將在您的文件目錄中顯示結果檔案。

![匯出完成](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

現在您可以傳送該檔案、在外部文字編輯器中開啟它，或用它在 [Last.fm](http://Last.fm) 上更新您的收聽進度。

![包含結果檔案的匯出資料夾](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

輸出 CSV 檔案將包含以下格式的欄位：

```
{藝術家名稱},{專輯名稱},{曲目名稱},{時間戳記 yyyy-MM-dd HH:mm:ss},{專輯藝術家名稱},{曲目時長 HH:mm:ss}
```

例如：

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![匯出的 csv 檔案](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT 格式

輸出 TXT 檔案將包含以下格式的欄位：

```
{序號}. {藝術家名稱} - {專輯名稱} - {曲目名稱} (時長 HH:mm:ss)
```

例如：

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![匯出的 txt 檔案](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U 格式

接下來，我們將指導您將播放清單匯出為 M3U 格式，這是播放清單檔案的事實標準。成功匯出播放清單的主要前提是播放清單中的所有檔案必須位於同一儲存位置，無論是 Google Drive 等雲端服務、本機檔案還是裝置上的檔案。要開始匯出過程，開啟任意播放清單，點擊右上角的「更多」按鈕，然後選擇「匯出歌曲清單」選單項目。

![播放清單畫面](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

在下一個畫面上，選擇「M3U」檔案格式，您將看到「媒體檔案位置類型」的兩個選項：

![選擇匯出檔案格式畫面](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. 如果選擇「相對路徑」，播放清單將以相對於播放清單檔案的媒體檔案位置建立。例如：

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   在這種情況下，匯出完成後請避免更改 M3U 檔案的位置，否則會破壞媒體檔案的路徑。要開始播放您的播放清單，只需點擊匯出的播放清單檔案，應用程式將自動在您的儲存空間中找到媒體檔案並開始播放。您甚至可以將播放清單匯出到儲存裝置，然後在新裝置上重新匯入。

2. 如果選擇「絕對 URL」，應用程式將為您的媒體檔案產生直接 URL。這允許您在任何裝置/應用程式上播放播放清單，而無需所有媒體檔案都與播放清單檔案位於同一儲存位置。此選項僅支援能夠產生直接檔案 URL 的雲端儲存服務。但請注意，在某些情況下，產生的 URL 可能有有限的有效期，一段時間後可能會過期。以下是支援的雲端服務清單：iCloud Drive、pCloud、PanBaidu、MyCloudHome、DLNA、MediaFire、OneDrive、Box、Dropbox、GoogleDrive、WebDav（訪客模式下）  

輸出的媒體檔案 URL 類似於：

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

選擇「媒體檔案位置類型」後，點擊「匯出」。應用程式將提示您選擇匯出 M3U 檔案的目標資料夾。點擊「完成」確認選擇。

![選擇資料夾](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

應用程式將產生 M3U 檔案並將其上傳/移動到目標資料夾。

![正在上傳 m3u 檔案](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

匯出完成後，將出現一個系統提示，提供「顯示檔案」選項。

![匯出完成提示](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

點擊此選項將在應用程式中顯示匯出的檔案。

![檔案清單中的匯出 m3u 檔案](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

如果在上一步中選擇了「相對路徑」作為「媒體檔案位置類型」，輸出檔案將採用以下格式：

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![相對路徑的 m3u 範例](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

對於「絕對 URL」選項，應用程式將產生以下格式的 M3U 檔案：

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![絕對檔案 URL 的 m3u 範例](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

您可以在任何支援 M3U 播放清單的裝置/應用程式上開啟該檔案。

![在外部應用程式中開啟的 m3u 播放清單](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## 總結

從 Evermusic 和 Flacbox 匯出曲目讓您完全掌控自己的音樂資料。無論是備份收聽歷史、向 Last.fm 記錄播放資料，還是在外部裝置上欣賞播放清單，M3U、CSV 和 TXT 這些匯出選項都是為靈活性和相容性量身定制的強大工具。充分利用這些功能，提升您在各平台間整理、分享和回顧音樂合集的體驗。

## 常見問題

{{% details title="Last.fm 記錄應該使用哪種匯出格式？" closed="true" %}}
使用 CSV。它包含 Last.fm-Scrubbler-WPF 等記錄工具所需的時間戳記和完整中繼資料。
{{% /details %}}

{{% details title="除了播放清單，我能匯出其他曲目合集嗎？" closed="true" %}}
可以。您可以使用相同的步驟匯出應用程式中的最近使用的、最愛項目、專輯、播放清單以及任何其他曲目合集。
{{% /details %}}

{{% details title="我的 M3U 播放清單能在其他裝置上使用嗎？" closed="true" %}}
如果您在匯出時選擇了絕對 URL 選項，M3U 檔案可以在任何支援 M3U 播放清單的裝置上播放。請注意，某些雲端 URL 可能會隨時間過期。
{{% /details %}}

{{% details title="匯出功能是免費的嗎？" closed="true" %}}
是的。將曲目合集匯出為 M3U、CSV 和 TXT 在 Evermusic 和 Flacbox 的免費版和進階版中均可使用。
{{% /details %}}

{{% details title="哪些雲端服務支援絕對 URL 匯出？" closed="true" %}}
絕對 URL 匯出支援 iCloud Drive、pCloud、PanBaidu、MyCloudHome、DLNA、MediaFire、OneDrive、Box、Dropbox、Google Drive 和 WebDAV（訪客模式）。
{{% /details %}}
