---
title: "如何將M3U播放列表匯入Evermusic和Flacbox"
date: 2024-01-31
description: "了解如何從雲端、本機儲存或裝置將M3U、M3U8和CUE播放列表檔案匯入Evermusic和Flacbox。"
keywords: ["evermusic", "flacbox", "播放列表", "m3u", "m3u8", "cue", "匯入", "音樂應用程式"]
tags: ["evermusic", "匯入", "播放列表", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**摘要：** Evermusic和Flacbox支援從雲端儲存、本機應用程式檔案或您的裝置匯入M3U、M3U8和CUE播放列表檔案。前往播放列表 > 更多 > 匯入播放列表，選擇來源，選擇檔案，應用程式將自動建立您的播放列表。

M3U，代表MP3 URL或Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator，是一種用於多媒體播放列表的電腦檔案格式。其主要用途之一是建立指向網際網路串流的單一項目播放列表檔案。這些檔案提供了對串流內容的便捷存取，通常用於下載、電子郵件和收聽網路電台。

儘管M3U格式被廣泛使用，但沒有正式的規範；它已成為事實上的標準。M3U檔案本質上是一個純文字檔案，指定一個或多個媒體檔案的位置。根據編碼方式，它以「m3u」或「m3u8」副檔名儲存。檔案中的每個項目指定一個媒體檔案的位置，可以是絕對本機路徑名、相對於M3U檔案位置的本機路徑名或URL。項目由換行符分隔，某些裝置要求換行符表示為CR LF。

此外，M3U檔案可以包含以「#」字元為前綴的註解。在延伸M3U中，「#」引入延伸M3U指令，這些指令可能支援以冒號「:」結尾的參數。

在我們的應用程式Evermusic和Flacbox中，我們實現了M3U檔案匯入功能，消除了手動建立播放列表的需要。本指南將引導您從雲端儲存、本機檔案或裝置上的檔案直接將播放列表匯入應用程式。

首先，導覽至「播放列表」區段。然後，點擊右上角的「更多」按鈕。從出現的選單中，選擇「匯入播放列表」選項。

![匯入播放列表操作](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

在下一個畫面上，選擇檔案位置。支援的選項包括：

- 已連接的雲端儲存；
- 應用程式中的檔案；
- 裝置上的檔案；

![選擇檔案位置](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

讓我們選擇已連接的雲端儲存並開啟包含播放列表檔案的資料夾。支援的播放列表副檔名包括M3U、M3U8和CUE。選擇播放列表檔案並點擊「完成」以確認您的選擇。

![選擇M3U檔案](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

應用程式將解析播放列表檔案並建立曲目列表。然後它將在儲存中找到這些檔案並編譯最終的播放列表，該列表將被匯入到音樂資料庫中。確保您的M3U/CUE檔案包含正確的媒體檔案路徑至關重要，並且檔案應位於儲存中的這些路徑上。

![已匯入的播放列表](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

應用程式同時支援相對路徑和絕對檔案URL。

例如：

使用相對路徑的播放列表：

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

使用絕對URL的播放列表：

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

如果您匯入的播放列表檔案位於應用程式內（本機檔案區段），則無需額外步驟。

但是，如果您想使用系統檔案選擇器匯入位於裝置上的播放列表，有一個重要事項需要注意。

由於安全政策，應用程式只能存取您使用系統檔案選擇器選擇的檔案。但是，播放列表檔案可能包含指向裝置上其他媒體檔案的連結。要從裝置匯入播放列表，您必須選擇一個包含播放列表檔案和所有關聯媒體檔案的資料夾。在這種情況下，應用程式將掃描選定的資料夾，找到播放列表檔案，建立曲目列表，並將其匯入到音樂資料庫中。

此外，您可以透過點擊「更多操作」按鈕並選擇「從資料夾匯入播放列表」來一次匯入多個播放列表。應用程式將掃描資料夾內容，找到支援的播放列表檔案並將其匯入到資料庫中。

## 常見問題

{{% details title="Evermusic和Flacbox支援哪些播放列表格式？" closed="true" %}}
兩個應用程式都支援M3U、M3U8和CUE播放列表檔案格式。這些涵蓋了音樂播放器和媒體軟體使用的最常見播放列表標準。
{{% /details %}}

{{% details title="我可以從雲端儲存匯入播放列表嗎？" closed="true" %}}
可以。您可以從任何已連接的雲端儲存服務匯入播放列表檔案，包括Google Drive、Dropbox、OneDrive和WebDAV伺服器。
{{% /details %}}

{{% details title="為什麼匯入後有些曲目遺失了？" closed="true" %}}
播放列表檔案必須包含指向您媒體檔案的正確路徑，並且這些檔案必須存在於儲存中指定的位置。請仔細檢查M3U或CUE檔案中的檔案路徑是否與實際檔案位置相符。
{{% /details %}}

{{% details title="我可以一次匯入多個播放列表嗎？" closed="true" %}}
可以。使用更多操作按鈕並選擇「從資料夾匯入播放列表」。應用程式會掃描資料夾中所有支援的播放列表檔案並一步匯入。
{{% /details %}}

{{% details title="我需要手動建立播放列表嗎？" closed="true" %}}
不需要。匯入功能消除了手動建立播放列表的需要。只需將應用程式指向您現有的M3U、M3U8或CUE檔案，它就會自動建立播放列表。
{{% /details %}}
