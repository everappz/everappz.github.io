---
date: 2020-01-01
lastmod: 2026-06-01
title: "Evervideo"
description: "了解如何使用 Evervideo——適用於 iPhone、iPad 和 Mac 的全能雲端視訊播放器。從 iCloud Drive、Google Drive、Dropbox、OneDrive、MEGA、Box、pCloud、Synology、QNAP、NAS、WebDAV、SMB、NFS、FTP / SFTP、DLNA 和 S3，以及 Plex、Jellyfin、Emby、Subsonic 和 Navidrome 播放和下載視訊。支援子母畫面、主副字幕、音訊和視訊等化器、RTSP IP 攝影機串流、Chromecast、AirPlay 2、硬體 H.264 / HEVC 解碼、Photos 與 Apple Music 資料庫整合，以及常駐迷你播放器。"
keywords: [
  "Evervideo 使用指南", "Evervideo 怎麼用", "雲端視訊播放器 iPhone", "視訊播放器 Mac",
  "MKV 播放器 iOS", "FFmpeg 視訊播放器", "HEVC 視訊播放器 iPhone",
  "iPhone 子母畫面視訊", "iPad PiP 視訊播放器",
  "RTSP 播放器 iPhone", "IP 攝影機檢視器", "DLNA 視訊播放器",
  "Plex 用戶端 iPhone", "Jellyfin 用戶端 iOS", "Emby 用戶端 iPad",
  "iOS 字幕播放器", "SRT VTT ASS 字幕", "iPhone 輔助字幕",
  "iOS 視訊等化器", "視訊播放器音訊等化器", "外接 DAC 視訊",
  "從 Google Drive 播放視訊", "從 Dropbox 播放視訊",
  "從 OneDrive 播放視訊", "從 iCloud Drive 播放視訊",
  "從 MEGA 播放視訊", "從 NAS 播放視訊",
  "iPhone Chromecast 視訊", "AirPlay 2 視訊", "iCloud 視訊播放器",
  "Photos 資料庫視訊播放器", "Apple Music 視訊播放器",
  "Wi-Fi Drive 視訊傳輸", "M3U 視訊播放清單",
  "Evervideo Premium", "家庭共享視訊應用程式"
]
tags: ["evervideo", "使用指南", "視訊播放器", "PiP", "字幕", "RTSP", "雲端", "FFmpeg"]
---


### 歡迎使用 Evervideo 指南

Evervideo 是適用於 iPhone、iPad 和 Mac 的全功能雲端媒體播放器，可將任何雲端儲存帳戶、NAS 或媒體伺服器變成您的個人媒體庫，無需重新上傳任何內容，同時完全掌控您的檔案。

基於定製 FFmpeg 播放引擎，配備硬體加速 H.264 和 HEVC 解碼，Evervideo 幾乎可以播放所有現代容器和編解碼器——MP4、MKV、AVI、MOV、FLV、WMV、WebM、TS、M2TS 以及衆多 FFmpeg 格式——以完整品質播放，並透過智慧緩衝在 Wi-Fi 或行動網路上實現流暢串流。子母畫面功能讓視訊始終顯示在所有其他應用程式之上，常駐迷你播放器讓您在瀏覽資料庫時持續觀看，而 Chromecast 和 AirPlay 2 只需一觸即可將播放投影到電視、HomePod 或音響系統。

Evervideo 可連線至豐富的來源，全部來自一個應用程式：

- **個人雲端儲存：** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **自行託管媒體伺服器：** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud（及透過共享 API 的 ownCloud）· Synology Drive · QNAP.
- **NAS 和檔案共享通訊協定：** SMB（SMB1、SMB2、自動）· WebDAV（HTTP / HTTPS）· FTP · FTPS · SFTP（密碼或公鑰認證）· NFS · DLNA · UPnP.
- **直播和 IP 攝影機串流：** RTSP——將 Evervideo 指向任意 RTSP URL（`rtsp://camera-ip/stream`）即可直接播放。
- **S3 相容物件儲存：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 以及任何其他 S3 API 端點。
- **裝置本機來源：** Photos 資料庫（所有視訊、短/中/長視訊、螢幕錄製及相簿）、Music 應用程式資料庫（專輯、流派、播放清單）、USB / SD 磁碟機和本機檔案。

### 一個播放器，支援所有格式和編解碼器

大多數 iOS 應用程式止步於 MP4 / MOV 中的 H.264 / H.265，而 Evervideo 將 FFmpeg 與 Apple 系統編解碼器捆綁在一起，讓您可以播放系統無法識別的格式——MKV 容器、VP9、AV1、MPEG-2、OGG、Vorbis 等——並根據檔案和裝置自動在硬體 H.264 / HEVC 解碼和軟體解碼之間切換。

您可以選擇視訊軌道（多串流藍光轉錄）、音訊軌道（評論軌道、備用配音）和字幕軌道。外部 SRT、VTT 和 ASS / SSA 字幕檔案一鍵載入；得益於內建 libass，進階 ASS / SSA 樣式可正確渲染。

### 智慧字幕

- **字幕軌道選擇**——非常適合語言學習。
- **外部字幕檔案**（`.srt`、`.vtt`、`.ass`、`.ssa`）可從裝置任意位置或雲端載入。
- **libass** 提供完整風格化的 ASS / SSA 渲染。
- **每軌道和全域字型選擇**，用於字幕。
- **音訊軌道選擇**——選擇配音、評論或導演剪輯軌道。
- **視訊軌道選擇**，適用於多角度或多版本檔案。

### 精調畫面和聲音

兩個並排等化器：音訊等化器用於調節低音和高音（支援自訂預設的匯入/匯出），視訊等化器用於調節亮度、對比度、飽和度和色調（同樣支援匯入/匯出）。兩個引擎還提供發燒友級別的控制：音訊輸出取樣率、聲道數量、IO 緩衝時長和混合模式——適合使用外接 DAC 和家庭劇院接收器的用戶。

### 投影、AirPlay 和子母畫面

- **子母畫面（PiP）：** 在使用其他應用程式時繼續觀看。
- **AirPlay 2：** 將視訊投影到 Apple TV、HomePod 或任何支援 AirPlay 2 的音箱/電視。
- **Google Chromecast：** 直接投影到 Chromecast 或支援 Cast 的電視。
- **迷你播放器：** 常駐於每個畫面頂部，讓您在瀏覽資料庫時不會遺失視訊。

### 隱私與安全

Evervideo 使用每個雲端服務商的官方 SDK 和基於 OAuth 的登入，因此您的密碼永遠不會傳到應用程式。存取權杖以加密形式儲存在 iOS/macOS Keychain 中，每次傳輸均受 TLS 保護，從雲端帳戶撤銷存取（或從裝置刪除 Evervideo）會立即刪除所有內容。透過可選的 4 位數字密碼保護您的資料庫，增加額外的隱私層。

### Evervideo 入門

本指南將帶您了解 Evervideo 在 iPhone、iPad 和 Mac 上的每個部分——從連線雲端服務、瀏覽資料庫、下載和傳輸檔案、管理播放清單，到精細調整媒體播放器、等化器、字幕和子母畫面。使用下方卡片直接跳轉到您需要的部分。<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="導覽" subtitle="iPhone 上的標籤列，iPad 和 Mac 上的左側選單，常駐迷你媒體播放器。" >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="檔案" subtitle="雲端、NAS、RTSP 串流、本機檔案、USB 磁碟機和傳輸佇列的統一標籤頁。" >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="媒體資料庫" subtitle="按專輯、流派、最近使用的、最愛項目瀏覽——以及 iOS Photos 資料庫和 Apple Music 資料庫。" >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="播放清單" subtitle="從雲端、本機、Photos 或 Music 資料庫建立播放清單，匯入 M3U / M3U8 / CUE。" >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="媒體播放器" subtitle="子母畫面、音訊和視訊軌道、字幕、音訊和視訊等化器、AirPlay、Chromecast。" >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="設定" subtitle="音訊引擎、視訊解碼器、字幕、資料庫、檔案管理員、小工具、個人化、語言、備份。" >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="常見問題" subtitle="尋找有關 Evervideo 最常見問題的解答。" >}}

{{< /cards >}}
