---
title: "Evermusic"
date: 2020-01-01
description: "Evermusic — 適用於 iPhone、iPad 和 Mac 的強大雲端音樂播放器和音樂庫管理器。從 Google Drive、Dropbox、iCloud、OneDrive、MEGA、Synology、pCloud、Plex、Jellyfin、Subsonic、Navidrome 或任何通過 SMB / WebDAV / FTP / SFTP 連接的 NAS 進行串流播放。編輯 ID3 和 FLAC 標籤，按藝術家 / 專輯 / 類型整理，離線播放，使用 10 段均衡器、crossfade、gapless、空間音訊、睡眠計時器、CarPlay、AirPlay 2、Google Cast、音訊書籤、Last.fm 音樂記錄和鎖定畫面小工具。"
keywords: [
  "Evermusic", "Evermusic Pro", "Evermusic iPhone", "Evermusic iPad", "Evermusic Mac",
  "雲端音樂播放器", "iOS FLAC播放器", "DSD播放器", "iPhone高解析度音訊",
  "Google Drive播放音樂", "Dropbox播放音樂", "iCloud Drive播放音樂",
  "OneDrive播放音樂", "MEGA播放音樂", "Synology音樂播放器", "pCloud音樂播放器",
  "Plex音樂客戶端", "Jellyfin音樂播放器", "Emby音樂客戶端",
  "iPhone Subsonic客戶端", "iPhone Navidrome客戶端", "Nextcloud音樂播放器",
  "NAS音樂串流", "iPhone SMB音樂播放器", "WebDAV音訊播放器",
  "iPhone FTP音樂播放器", "SFTP音樂播放器", "S3音樂播放器",
  "10段均衡器", "crossfade播放", "gapless播放", "空間音訊",
  "有聲書書籤", "離線音樂應用程式", "iPhone音樂庫", "ID3標籤編輯器",
  "M3U播放清單匯入", "CSV TXT播放清單匯出", "Apple CarPlay音樂播放器",
  "AirPlay 2", "Google Cast Chromecast音樂", "Last.fm音樂記錄", "鎖定畫面小工具"
]
tags: ["evermusic", "指南"]
readingTime: 4
---


Evermusic 是一款強大的雲端音樂播放器和音樂庫管理器，可將您的 iPhone、iPad 或 Mac 變成功能完備的串流和離線音樂系統。它與您已有的雲端帳戶和 NAS 相容，幾乎可播放裝置支援的所有音訊格式，並在此基礎上提供深度音訊引擎（10 段均衡器、crossfade、gapless、空間音訊、音調校正）。

提供兩個版本：Evermusic（免費，含廣告）和 Evermusic Pro（付費，無廣告，完整功能集）。免費版中的終身、月度和年度 Premium 方案可解鎖相同的功能集；兩個版本通過 iCloud 和 Family Sharing 在 iOS 和 Mac 之間共享購買。

### 隨時隨地享受音樂

Evermusic 讓您建立自己的雲端音樂串流系統——就像 Spotify，但沒有任何限制。連接任意來源組合，按需串流或下載曲目：

- **個人雲端帳戶：** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **自建伺服器和媒體庫：** Plex · Jellyfin · Emby · Subsonic（以及所有 Subsonic 相容伺服器——Airsonic、Funkwhale、Gonic、Logitech Media Server、Ampache）· Navidrome · Nextcloud（以及通過共享 API 的 Owncloud）· Synology Drive · QNAP.
- **NAS 和檔案共享協議：** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP（SSH 檔案傳輸協議，密碼或公鑰認證）· NFS · DLNA / UPnP（播放和下載）。支援 Apple Time Capsule、Synology、QNAP、WD My Cloud Home、Buffalo、任何 Linux Samba / NFS / SSH 主機，或 Mac 或 Windows PC 上的共享資料夾。
- **S3 相容物件儲存：** AWS S3 · Backblaze B2 · Wasabi · Cloudflare R2 · MinIO · DigitalOcean Spaces · Linode Object Storage · IBM Cloud Object Storage · 任何 S3-API 端點。
- **區域網路探索：**「可用設備」部分自動列出您 Wi-Fi 上通過 Bonjour / mDNS 廣播的所有裝置——Plex、Jellyfin、Emby 伺服器、Synology、QNAP、帶附加硬碟的 AirPort 路由器、Time Capsule——點擊即可連接，無需輸入 IP。
- **裝置和外部來源：** iPod / Apple Music 媒體庫（無 DRM 曲目）、系統 Files 應用程式中的檔案（其他應用程式、外部 SSD、掛載的資料夾）、通過 Apple 認證讀卡器和 iXpand Flash Drives 連接的 USB 隨身碟、Wi-Fi Drive（在桌面瀏覽器中拖放）、iTunes / Finder 檔案共享（USB 傳輸線）。

一個應用程式支援 30 多種來源。音樂在雲端後，您可以隨時隨地播放，每台裝置上的媒體庫相同。備份與還原功能可將整個媒體庫快照為單個檔案，並在數秒內匯入到另一台 iPhone、iPad 或 Mac 上。

### 流暢播放

Evermusic 使用智慧預載和可配置的播放快取，即使在連接緩慢的情況下也能流暢播放歌曲。智慧串流使用 AVAssetResourceLoader，播放立即開始，同時後台下載檔案的其餘部分。您也可以下載專輯、藝術家、播放清單或單首歌曲供離線聆聽——如果儲存空間不足，只需刪除快取檔案並繼續從雲端串流。

### 輕鬆整理音樂

將歌曲加入 Evermusic 時，後台元數據讀取器會解析每個檔案並建立按歌曲、未播放歌曲、專輯、專輯藝術家、藝術家、類型和作曲家排序的整潔音樂庫。專輯有三個子視圖：所有專輯、獨家專輯和獨唱專輯，避免合輯和不同藝術家同名專輯之間的混淆。

### 輕鬆修正歌曲資訊

如果歌曲標題或專輯資訊有誤或缺失，不用擔心。Evermusic 包含內建標籤編輯器，讓您在幾秒內修復元數據。您可以更新標題、藝術家、專輯、專輯藝術家、年份、類型和專輯封面，還可以一鍵規範化損壞的編碼（亂碼顯示的西里爾文或亞洲文字）。編輯器使用 MusicBrainz 自動尋找缺失的標籤和專輯封面。

### 簡單檔案傳輸

從電腦向 iPhone 或 iPad 傳送音樂非常簡單。Evermusic 支援 SMB、WebDAV、FTP / FTPS、SFTP、NFS、DLNA、Wi-Fi Drive（在瀏覽器中拖放）、iTunes / Finder 檔案共享（USB 傳輸線）以及從任何已連接雲端帳戶直接下載。您還可以連接 Apple Time Capsule、WD My Cloud Home、Synology、QNAP、Buffalo 或任何其他公開上述標準協議的 NAS，而不佔用裝置儲存空間。

### 強大的音效控制

Evermusic 包含完整的 10 段音訊均衡器，帶有 iPod 風格的預設（Acoustic、Bass Booster、Classical、Dance、Electronic、Flat、Hip-Hop、Jazz、Latin、Loudness、Lounge、Piano、Pop、R&B、Rock、Small Speakers、Spoken Word、Treble Booster、Vocal Booster）、用於安靜曲目的前置放大器、可匯出和匯入的自訂預設，以及基於 RMS 的響度計算。加入 crossfade 播放（1–15 秒）、gapless 播放、空間音訊、音調校正和 CoreAudio 輸出高達 384 kHz 單聲道或立體聲，可以完全按照自己的喜好調整音效。

### 非常適合有聲書

如果您聆聽有聲書、播客或錄製的講座，Evermusic 是完美之選。您可以為每首曲目加入多個書籤、自動從上次位置恢復、將播放速度從 0.02× 更改為 3×（帶有精確滑桿模式）、設定帶有自訂間隔的睡眠計時器，並在同一螢幕上查看評論、嵌入式歌詞和 LRC 檔案。

### 隨處可用

您不僅限於手機或平板電腦。Evermusic 還支援 Apple CarPlay（僅限 iOS，針對車載介面優化）、AirPlay 2（同時向多個揚聲器串流）、Google Cast / Chromecast、鎖定畫面小工具、正在播放控制、Last.fm 音樂記錄（自動將播放數據發送到您的 Last.fm 帳戶以獲取統計數據和推薦）和 Mac 鍵盤快捷鍵。無論您在家、在車裡還是旅途中，音樂始終伴隨您。

### Evermusic 入門

本指南將幫助您在 iPhone、iPad 或 Mac 上充分利用 Evermusic。了解如何從雲端串流音樂、整理存儲在自己儲存空間上的媒體庫、管理播放清單和離線資料夾、微調音訊引擎以及聆聽有聲書。Evermusic 讓您在一個簡單的應用程式中完全控制您的音樂收藏。<br><br>


{{< cards >}}
  {{< card icon="location-marker" title="導航" subtitle="了解如何在 iPhone 上使用標籤列或在 iPad 和 Mac 上使用左側選單導航 Evermusic。" link="/docs/guide/evermusic/evermusic-guide-navigation" >}}

  {{< card icon="cloud" title="連接" subtitle="連接您的雲端帳戶並使用內建檔案管理器管理線上檔案。" link="/docs/guide/evermusic/evermusic-guide-connections" >}}

  {{< card icon="collection" title="音樂庫" subtitle="在音樂庫中整理和瀏覽您的曲目、專輯和藝術家。" link="/docs/guide/evermusic/evermusic-guide-music-library" >}}

  {{< card icon="music-note" title="播放清單" subtitle="建立和整理播放清單以符合您的心情或場合。" link="/docs/guide/evermusic/evermusic-guide-playlists" >}}

  {{< card icon="folder" title="本地檔案" subtitle="通過本地檔案部分存取和管理離線音樂。" link="/docs/guide/evermusic/evermusic-guide-local-files" >}}

  {{< card icon="play" title="音訊播放器" subtitle="控制播放、佇列和音訊設定，如均衡器和睡眠計時器。" link="/docs/guide/evermusic/evermusic-guide-player" >}}

  {{< card icon="adjustments" title="設定" subtitle="自訂 Evermusic 的外觀、功能和效能設定。" link="/docs/guide/evermusic/evermusic-guide-settings" >}}

  {{< card icon="question-mark-circle" title="FAQ" subtitle="在我們的 FAQ 部分找到常見問題的快速解答。" link="/docs/faq/evermusic" >}}
{{< /cards >}}
