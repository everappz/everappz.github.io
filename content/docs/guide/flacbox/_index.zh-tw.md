---
date: 2020-01-01
title: 'Flacbox'
description: '了解如何使用 Flacbox——這款支援 FLAC、DSD、ALAC 和 FFmpeg 的高解析度雲端音樂播放器，適用於 iPhone、iPad 和 Mac。連接 iCloud Drive、Google Drive、Dropbox、OneDrive、MEGA、Box、pCloud、Synology、QNAP、NAS、WebDAV、SMB 和 DLNA。串流和下載高解析度音訊、編輯後設資料、收聽有聲書、向 Last.fm 回報播放紀錄、使用 Apple CarPlay 和主畫面小工具，以及自訂 10 段等化器。'
keywords: [
  "Flacbox 使用指南", "Flacbox 如何使用", "iPhone 高解析度音樂播放器", "iPhone FLAC 播放器",
  "iOS DSD 播放器", "Mac ALAC 播放器", "無損音樂應用程式", "iPhone 雲端音樂播放器",
  "Mac 離線 FLAC 播放器", "音樂庫管理器", "音訊標籤編輯器",
  "CarPlay FLAC 播放器", "Chromecast 音訊應用程式", "AirPlay 2 音樂",
  "Flacbox 小工具", "Flacbox CarPlay", "iOS FFmpeg 音樂播放器",
  "iPhone 有聲書播放器", "iOS 音訊書籤", "音樂變調應用程式",
  "音訊輸出取樣率", "iPhone 外接 DAC", "Mac USB DAC",
  "Synology 音樂應用程式", "QNAP 音樂應用程式", "iPhone NAS 音樂播放器",
  "WebDAV 音樂播放器", "SMB 音樂串流", "DLNA 音樂播放器",
  "iCloud Drive 音樂", "Google Drive FLAC", "Dropbox FLAC 播放器",
  "Wi-Fi Drive 音樂傳輸", "M3U 播放清單匯入", "Last.fm 回報播放紀錄"
]
tags: ["flacbox", "指南", "高解析度", "FLAC", "FFmpeg", "雲端", "CarPlay", "小工具"]
---


### 歡迎使用 Flacbox 指南

Flacbox 是一款適用於 iPhone、iPad 和 Mac 的高解析度音樂播放器，可讓您將喜愛的雲端儲存空間、NAS 和媒體伺服器變成專屬的個人串流服務。

Flacbox 可連接極為豐富的音源，一切盡在一款應用程式中：

- **個人雲端儲存：** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **自架伺服器：** Plex · Jellyfin · Emby · Subsonic（及所有 Subsonic 相容伺服器——Airsonic、Funkwhale、Gonic、Logitech Media Server、Ampache）· Navidrome · Nextcloud（以及透過共享 API 的 ownCloud）· Synology Drive · QNAP.
- **NAS 和檔案共享協定：** SMB（SMB1、SMB2、Auto）· WebDAV（HTTP / HTTPS）· FTP / FTPS · SFTP（密碼或公鑰認證）· NFS · DLNA / UPnP（播放和下載）。相容 Apple Time Capsule、Synology、QNAP、WD My Cloud 以及任何 Linux Samba / NFS / SSH 主機或 Mac / Windows PC 上的共享資料夾。
- **S3 相容物件儲存：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 及任何其他 S3-API 端點。
- **區域網路探索：**「可用設備」區域自動列出 Wi-Fi 上的所有 Bonjour / mDNS 服務——Plex、Jellyfin、Emby、Synology、QNAP、附有外接硬碟的 AirPort 路由器、Time Capsule——無需輸入 IP 位址，輕點即可連接。

大多數音樂應用程式僅使用 Apple 內建音訊引擎，而 Flacbox 在系統編解碼器的基礎上還整合了 **FFmpeg**，可播放 iOS 預設不支援的格式——WMA、OGG、OPUS、APE、DSD、DSF、DFF、TTA、MPC、WV，以及常見的 MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC。結合可設定的音訊輸出取樣率（44.1 / 48 / 64 / 88.2 / 96 kHz）、多聲道輸出、IO 緩衝調整和音調校正，Flacbox 為發燒友提供了大多數消費類音樂應用程式所沒有的精細控制。

### 享受流暢的串流和離線播放

Flacbox 具備智慧緩衝，確保串流播放流暢，同時內建下載管理器，讓您可將整個播放清單、藝術家、專輯、資料夾或單曲下載到裝置以供離線使用。

### 自動整理的音樂庫

匯入音軌時，Flacbox 會掃描其後設資料並整理成清晰的音樂庫——按歌曲、未播放歌曲、專輯、專輯藝術家、藝術家、類型和作曲家分組。

### 修復後設資料並為音樂打標籤

內建 ID3 標籤編輯器可修復損壞的標籤——手動或透過自動 MusicBrainz 查詢。還可以規範化字元編碼、搜尋缺失的專輯封面，並自動將變更寫回雲端的原始檔案。

### 輕鬆從 Mac、PC 或 NAS 傳輸

透過以下工具在電腦與 iPhone 或 iPad 之間移動音樂：SMB、WebDAV、DLNA、Wi-Fi Drive（在任意桌面瀏覽器中拖放）、透過 Lightning 或 USB-C 連接線進行 iTunes / Finder 檔案共享、USB 隨身碟或 iXpand 隨身碟。

### 透過等化器自訂音效

Flacbox 內建 10 段等化器，提供 iPod 風格的預設（Acoustic、Bass Booster、Classical、Dance、Rock、Pop、Jazz 等）、前置放大器和儲存自訂預設的功能。

### 專為有聲書設計

Flacbox 是出色的有聲書播放器——每首曲目支援多個書籤、精細的播放速度調整（0.02× 至 3.00×）、從停止處精確恢復播放、可自訂跳過時間按鈕以及漸出睡眠計時器。完整支援 M4B 章節標記和長檔案。

### 隨時隨地串流——包括車內和主畫面

透過 AirPlay 2 向 Apple TV / HomePod 串流，傳送到 Google Chromecast 和支援 Cast 的電視，並透過 Apple CarPlay 在路上享受音樂。

### 隱私與安全

Flacbox 僅使用每家雲端供應商的官方 SDK 和 OAuth 登入——您的密碼永遠不會傳送至應用程式。存取權杖加密儲存在 iOS Keychain 中，所有傳輸均受 TLS 保護。

### Flacbox 入門

本指南將帶您了解 Flacbox 在 iPhone、iPad 和 Mac 上的每個功能——從連接雲端服務、整理音樂庫、傳輸檔案和管理播放清單，到微調等化器和設定音訊引擎。

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="導覽" subtitle="iPhone 的標籤列，iPad 和 Mac 的左側選單，迷你播放器，小工具，CarPlay。" >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="連接" subtitle="iCloud、Google Drive、Dropbox、OneDrive、NAS、WebDAV、SMB、DLNA。" >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="音樂庫" subtitle="歌曲、專輯、藝術家、類型、作曲家——同步、搜尋、編輯後設資料。" >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="播放清單" subtitle="建立、匯入 M3U / M3U8 / CUE，重新排序，並匯出為 M3U / CSV / TXT。" >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="本機檔案" subtitle="離線音樂、USB 磁碟機、Wi-Fi Drive、檔案管理器、離線資料夾。" >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="音訊播放器" subtitle="高解析度輸出、等化器、音調、書籤、AirPlay、Chromecast、速度、睡眠計時器。" >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="設定" subtitle="音訊引擎、音樂庫、檔案管理器、CarPlay、小工具、個人化、語言、備份。" >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="常見問題" subtitle="查找有關 Flacbox 的 50 個最常見問題的解答。" >}}

{{< /cards >}}
