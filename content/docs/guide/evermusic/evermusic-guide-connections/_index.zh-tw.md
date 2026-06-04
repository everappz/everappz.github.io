---
title: "連接"
date: 2020-01-01
description: "了解如何使用 Evermusic 連接雲端服務、電腦、NAS 設備並管理音樂檔案。Wi-Fi Drive、SMB、DLNA、WebDAV、iTunes 檔案共享等的分步指南。"
keywords: [
  "Evermusic", "雲端音樂播放器", "NAS 串流", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes 檔案共享",
  "連接雲端儲存", "iPhone 音樂傳輸", "iOS 檔案管理器"
]
tags: ["evermusic", "指南", "連接"]
readingTime: 11
---


在「連接」螢幕上，您可以連接所有保存音樂的來源——流行的雲端服務、自托管媒體伺服器、Mac 或 PC、個人 NAS、Apple Time Capsule、WD My Cloud Home，甚至 USB 隨身碟——並通過統一介面使用所有這些來源。「連接」也是您設定快速存取深層嵌套雲端資料夾以及為 Last.fm scrobbling 進行身份驗證的地方。

螢幕被分為清楚標記的部分：頂部的快速存取（您收藏的雲端資料夾）、雲端儲存（已新增的帳戶）、區域網路（Bonjour 發現的設備）、電腦（Wi-Fi Drive、iTunes 檔案共享、SMB）、外部配件（已連接的 USB 隨身碟）以及其他服務（Last.fm 等）。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic 連接螢幕" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## 連接雲端儲存

- 開啟「連接」標籤頁。
- 從選單中選擇「連接雲端儲存」。
- 從清單中選擇雲端儲存服務。
- 在提供商的官方授權頁面登入（Evermusic 從不查看您的密碼）。
- 點選「完成」。

{{< cards cols="1">}}
  {{< card title="" subtitle="連接雲端儲存提供商選擇器" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

如果遇到任何問題，請仔細檢查您的網路連接和登入憑據，並確保該服務的雙重認證配置正確。  
在應用程式的 Premium 版本中，您可以新增無限數量的服務。免費使用者一次只能連接一個雲端帳戶。

## 支援的雲端儲存服務

Evermusic 支援全系列流行的雲端和自托管服務。免費使用者獲得相同的提供商目錄，但有單帳戶限制；Premium 解鎖無限帳戶並取消大多數其他限制。

- **個人雲端帳戶：** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **自托管伺服器和媒體庫：** Plex · Jellyfin · Emby · Subsonic（以及所有 Subsonic 相容伺服器——Airsonic、Funkwhale、Gonic、Logitech Media Server、Ampache）· Navidrome · Nextcloud（以及通過共享 API 的 Owncloud）· Synology Drive · QNAP.
- **NAS 和檔案共享協議：** SMB (SMB1, SMB2, Auto)、WebDAV (HTTP / HTTPS)、FTP / FTPS、SFTP（密碼或公鑰認證）、NFS 和 DLNA（只讀——播放和下載）。
- **S3 相容物件儲存：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces、Linode Object Storage、IBM Cloud Object Storage 或任何 S3-API 端點。
- **區域網路探索：**「可用設備」部分自動列出您 Wi-Fi 上通過 Bonjour / mDNS 廣播的任何裝置——Plex、Jellyfin、Emby 伺服器、Synology、QNAP、WD My Cloud Home、Apple Time Capsule、帶附加硬碟的 AirPort 路由器等。

## 安全與隱私

我們僅使用官方 SDK 和安全連接與已連接的雲端服務互動。您的登入名稱和密碼對應用程式不可見。從應用程式到雲端服務的所有請求均已加密。

當您輸入登入名稱和密碼時，應用程式會顯示由雲端服務提供商提供的官方授權頁面，所有授權過程均在應用程式外部進行。雲端服務提供商在成功授權後向應用程式發送 auth token，該 token 用於進行 API 呼叫。

Auth token 是允許第三方應用程式與雲端儲存互動的數字密鑰。Auth token 存儲在您的裝置上名為 Keychain 的安全系統存儲中。您可以將檔案從已連接的雲端服務下載到裝置，這些檔案將存放在應用程式的「Documents」目錄中。您可以隨時使用內建檔案管理器刪除這些檔案。

應用程式不會共享已連接雲端帳戶中的任何資訊。您可以隨時通過在 Web 瀏覽器中開啟帳戶設定頁面來撤銷對雲端帳戶的存取權限。

## 撤銷 auth token

在 Web 瀏覽器中登入您的帳戶並導航到設定頁面。在那裡，您可以找到連接到您的雲端帳戶的所有第三方應用程式，並刪除任何您不再想使用的應用程式。詳細說明請參見[此處](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)。

您也可以在應用程式中斷開已連接的雲端帳戶，auth token 也將從您的裝置中刪除。如果您從裝置中刪除應用程式，所有已下載的資料和存取令牌也將被刪除。

## 斷開雲端儲存或更改配置

- 存取雲端儲存選項：首先，在應用程式介面中找到您想管理的雲端儲存。
- 點選「...」按鈕：服務標題旁邊，您會看到一個「...」按鈕。點選它以存取其他選項。
  - **重新命名**：如果您想更改雲端服務在清單中顯示的名稱，請選擇「重新命名」。
  - **設定**：要修改雲端服務的配置或認證資料，請選擇「設定」。有時，如果授權令牌已過期，您可能需要重新授權已連接的雲端服務。
  - **斷開連接**：如果您希望完全斷開應用程式與雲端服務的連接，請選擇「斷開連接」。請注意，選擇此選項將從應用程式的音樂庫中刪除與此雲端服務關聯的所有歌曲，但它們將保留在伺服器上。

{{< cards cols="1">}}
  {{< card title="" subtitle="已連接雲端儲存的更多操作選單" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## 連接電腦或 NAS

您也可以使用 SMB、DLNA 或 WebDAV 協議連接您的電腦、個人 NAS 或其他網路設備。

## 使用 SMB 連接電腦

- 點選「連接雲端儲存」→ SMB。
- 在 URL 欄位中輸入電腦 IP 位址和共享資料夾名稱，格式為 smb://computer-ip-address/shared-folder-name
- 選擇協議版本：Auto、SMB1、SMB2
- 輸入登入名稱和密碼（如果需要）
- 點選「完成」。

如果連接成功，您將在「雲端儲存」部分看到已連接的儲存。  
關於如何使用 SMB 連接 Mac 或 PC 的完整教學請參見[此處](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)。

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB 連接設定" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## 使用 WebDAV 連接 NAS

所有步驟相同，除了 URL 欄位。  
URL 應為 http://server-name 格式，如果伺服器支援 SSL 則為 https://server-name。
關於如何使用 WebDAV 協議連接 NAS 儲存的完整教學請參見[此處](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)。

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV 連接設定" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## 使用 DLNA 連接電腦或 NAS

您也可以使用 DLNA 協議共享位於 Windows PC 或個人 NAS 上的音樂庫，並在應用程式中存取該庫，如[此處](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)所述。DLNA 是一種流行且廣泛使用的協議，但它只允許您播放或下載音樂。您無法上傳檔案或在伺服器上建立新資料夾。

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA 連接設定" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## 可用設備

此部分顯示您區域網路中可以通過應用程式連接的所有設備。  
要與設備建立連接，請按照以下步驟操作：

- 開啟應用程式並進入「可用設備」部分。
- 從清單中點選您想連接的設備。
- 如有需要，輸入您的登入資訊以完成連接。

{{< cards cols="1">}}
  {{< card title="" subtitle="區域網路上的可用設備" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive 是一種便捷的技術，可通過桌面瀏覽器將檔案從電腦無線傳輸到 iOS 裝置。  
為了有效使用此功能，請確保您的裝置和電腦連接到同一 Wi-Fi 網路。  
以下是如何使用 Wi-Fi Drive 的分步指南。

## 啟用 Wi-Fi Drive

- 開啟應用程式並進入「連接」標籤頁。
- 選擇「通過 Wi-Fi 連接」以存取 Wi-Fi Drive 主螢幕。
- 點選「啟動 Wi-Fi Drive」以啟用 Wi-Fi Drive。

## 在您的電腦上存取 Wi-Fi Drive

- 在您的電腦（桌上型電腦或筆記型電腦）上，開啟 Web 瀏覽器（如 Chrome、Firefox 或 Safari）。
- 在瀏覽器的網址列中，輸入應用程式提供的 URL。

## 無線傳輸檔案

一旦 iOS 裝置對應的網頁在瀏覽器中開啟，您就可以輕鬆地將檔案從電腦拖放到網頁上。  
您拖放的檔案將開始傳輸到 iOS 裝置，並可在應用程式中存取。

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive 伺服器設定" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

關於如何使用 WiFi-Drive 無線傳輸檔案的詳細說明請參見[此處](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)。

## iTunes 檔案共享

iTunes 檔案共享是另一種技術，允許您使用 Mac 上的 Finder 應用程式和 lightning 傳輸線將檔案從電腦傳輸到裝置。  
- 只需使用傳輸線將裝置連接到電腦並在 Mac 上執行 Finder 應用程式。 
- 開啟「位置」→「已連接的裝置」→「檔案」→ 找到 Evermusic 應用程式。 
- 點選應用程式圖示查看所有共享資料夾。 
- 使用拖放將檔案從電腦複製到裝置上的共享資料夾。  

關於如何使用 iTunes 檔案共享的詳細說明請參見[此處](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/)。

{{< cards cols="1">}}
  {{< card title="" subtitle="Mac 上的 iTunes / Finder 檔案共享" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## 連接 USB 隨身碟

如果您有 SD 卡，可以使用 lightning 讀卡器連接它。應用程式目前支援 Apple 認證讀卡器和 iXpand Flash Drives。如果您有 iXpand Flash Drive - 將其插入 lightning 連接埠並開啟應用程式。您將看到「已連接外部裝置」訊息和裝置資訊。只需點選隨身碟圖示即可存取音樂資料夾，點選任何音訊檔案即可開始播放。關於如何將 USB 隨身碟連接到 iPhone 並聆聽音樂或管理其上檔案的詳細說明請參見[此處](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it)。

## 檔案管理器

連接雲端儲存服務後，點選其圖示查看所有可用檔案和資料夾。您可以使用內建檔案管理器處理這些檔案——下載、重新命名、移動等等。開始下載時，檔案將出現在傳輸佇列中。要查看傳輸佇列，前往「本地檔案」標籤頁並點選左上角的旋轉箭頭圖示。所有下載的檔案和資料夾都在「本地檔案」部分中可用。

## 頂部工具列

頂部工具列方便地位於導覽列下方，提供幾個實用操作以便於存取。您可以通過向下滑動手勢顯示或隱藏此工具列。以下是可用操作：

- **搜尋**：此選項允許您在當前目錄中執行快速搜尋，輕鬆找到特定檔案或資料夾。
- **繼續播放**：如果在應用程式設定中啟用，此功能將為當前資料夾恢復音訊播放器佇列和最後的媒體位置。
- **全部播放**：選擇此操作時，應用程式將掃描當前資料夾及其子資料夾，將所有找到的音訊檔案新增到新的播放器佇列中。
- **隨機播放**：類似於「全部播放」，但在將檔案新增到音訊播放器佇列之前對其進行隨機排序。

{{< cards cols="1">}}
  {{< card title="" subtitle="雲端資料夾內的頂部工具列" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## 資料夾選項

在應用程式中開啟資料夾時，您會發現一組方便的操作，可通過點選螢幕右上角的「...」按鈕存取。  
以下是這些操作的說明：

- **選擇**：啟用檔案選擇模式。此模式允許您選擇資料夾內的一個或多個檔案。
- **新建資料夾**：在當前資料夾內建立新資料夾。
- **啟用離線模式**：為當前資料夾開啟離線模式。離線模式不僅僅是簡單的下載；它主動監控資料夾的變化。如果您線上向資料夾新增新檔案，應用程式將自動將這些檔案下載到您的裝置。
- **上傳檔案**：將裝置中的檔案上傳到線上資料夾。
- **搜尋**：搜尋當前資料夾中的特定檔案。
- **排序**：按名稱、大小或編輯日期等條件對資料夾中的檔案進行排序。
- **網格/清單視圖**：在表格視圖和縮圖視圖兩種顯示模式之間切換。

{{< cards cols="1">}}
  {{< card title="" subtitle="當前資料夾的更多操作選單" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## 編輯線上檔案

當您需要在 Evermusic 中管理雲端儲存中的多個檔案時，可以使用選擇模式。請按照以下步驟操作：

- **啟用選擇模式**：開啟應用程式並導航到包含雲端儲存的部分。找到右上角的「...」（省略號）按鈕。點選它並選擇「選擇」選單項以啟用選擇模式。
- **選擇檔案**：您會注意到每個檔案或資料夾旁邊出現核取方塊。通過點選旁邊的核取方塊選擇一個或多個檔案或資料夾。
- **執行各種操作**：選擇要管理的檔案或資料夾後，您將可以存取多個操作。

{{< cards cols="1">}}
  {{< card title="" subtitle="線上檔案的選擇模式" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## 檔案操作

在檔案標題旁邊，您會注意到省略號符號「...」（三個點）——這是操作選單。  
點選它以查看可用操作清單：

- **下一首播放**：選擇此操作將所選檔案插入播放器佇列頂部，確保它在當前播放項目後立即播放。
- **稍後播放**：將檔案新增到播放器佇列底部。
- **新增到音樂庫**：將檔案整合到您的音樂庫中。
- **新增到播放清單**：使用此操作將檔案新增到現有播放清單或建立新播放清單。
- **編輯音訊標籤**：存取 Evermusic 的內建標籤編輯器，修改所選檔案的音訊標籤。
- **新增到最愛項目**：將檔案新增到您的最愛項目清單。
- **下載**：將檔案或資料夾下載到您的裝置供離線使用。
- **重新命名**：直接在遠端儲存上重新命名檔案。
- **移動**：將檔案移動到雲端儲存中的不同資料夾。
- **在其中開啟**：將檔案匯出到另一個相容應用程式。
- **刪除**：此操作會永久從雲端儲存中刪除檔案，此操作無法撤銷。

{{< cards cols="1">}}
  {{< card title="" subtitle="單個檔案的更多操作選單" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

如果操作清單超出可用螢幕空間，只需在操作選單中向下捲動以存取其他選項。

## 資料夾操作

對於雲端儲存中的每個資料夾，都有各種可用操作。要存取這些選項，只需點選資料夾標題旁邊的省略號圖示「...」。以下是可用操作：

- **全部播放**：將當前播放器佇列替換為所選資料夾中的所有項目。
- **下一首播放**：將整個資料夾新增到播放器佇列頂部。
- **稍後播放**：將資料夾內容追加到播放器佇列底部。
- **新增到音樂庫**：將資料夾內容無縫整合到您的音樂庫中。
- **新增到播放清單**：您可以將整個資料夾包含在播放清單中。
- **新增到最愛項目**：使用此操作將資料夾新增到您的最愛項目清單。
- **啟用離線模式**：通過為所選資料夾啟用離線模式，應用程式持續掃描變化並自動下載新檔案。
- **下載**：將資料夾的所有內容下載到裝置供離線存取。
- **重新命名**：直接在遠端儲存上重新命名資料夾。
- **移動**：將資料夾移動到雲端儲存中的不同位置。
- **刪除**：請謹慎使用此操作，因為它會永久從雲端儲存中刪除資料夾及其內容，此操作無法撤銷。


## 快速存取

快速存取部分位於螢幕頂部。它讓您快速存取已連接雲端服務中您收藏的和最近開啟的檔案。
每當您從雲端開啟檔案或資料夾時，它都會被新增到「最近使用的」清單中。要清除此清單，開啟「最近使用的」，點選「更多操作」按鈕，然後選擇「刪除清單」。您還可以將深層嵌套的資料夾標記為最愛項目，以便快速存取而無需瀏覽目錄結構。

## 其他服務

此部分顯示增強您體驗的額外功能。目前，應用程式支援 Last.fm scrobbling。連接後，您的播放統計資料會自動發送到您的 Last.fm 帳戶。您可以稍後存取您的 Last.fm 個人資料查看聆聽分析並獲取個性化音樂推薦。詳細設定說明請參見[此處](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)。
