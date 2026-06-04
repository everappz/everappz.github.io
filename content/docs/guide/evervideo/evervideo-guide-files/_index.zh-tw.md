---
title: "檔案"
date: 2020-02-01
lastmod: 2026-06-01
description: "了解如何在 iPhone、iPad 和 Mac 上使用 Evervideo 的檔案標籤頁。在一個地方連接雲端服務、NAS 裝置、媒體伺服器和 RTSP 串流。管理離線視訊、傳輸佇列、下載、Wi-Fi Drive、iTunes / Finder 檔案共享和 USB 磁碟機。支援 iCloud Drive、Google Drive、Dropbox、OneDrive、MEGA、Box、pCloud、Synology、QNAP、Plex、Jellyfin、Emby、Subsonic、Navidrome、SMB、WebDAV、NFS、FTP / SFTP、DLNA 和 S3 相容儲存。"
keywords: [
  "Evervideo 檔案", "Evervideo 連接", "Evervideo 本機檔案",
  "雲端視訊設定 iPhone", "連接 Google Drive 視訊", "SMB 視訊串流",
  "iOS WebDAV 視訊播放器", "DLNA 視訊 iPhone", "NAS 視訊串流",
  "Wi-Fi Drive 視訊傳輸", "Evervideo iTunes 檔案共享", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo 離線模式視訊", "Evervideo 傳輸佇列",
  "Evervideo 檔案管理員", "Evervideo Documents 資料夾",
  "視訊播放器 Synology", "視訊播放器 QNAP",
  "視訊播放器 Apple Time Capsule", "USB DAC 視訊",
  "iXpand 視訊播放器", "S3 視訊播放器"
]
tags: ["使用指南", "evervideo", "檔案", "連接", "雲端", "NAS", "Plex", "RTSP"]
readingTime: 14
---

檔案標籤頁是 Evervideo 的多合一檔案管理員。與大多數視訊應用將雲端儲存和本機檔案分成不同標籤頁不同，Evervideo 將兩者合併到一個可捲動的畫面中，讓您可以從 Plex 伺服器切換到雲端資料夾再到 iPhone 的 Documents 資料夾，而無需在標籤頁之間切換。

檔案標籤頁分為清晰的幾個部分，按以下順序顯示在畫面上：

- **快速存取** — 您最近開啟的檔案和資料夾的最近使用的和最愛項目。
- **此應用程式中的檔案** — Evervideo 沙盒 Documents 資料夾中的內容。
- **此 iPhone / iPad / Mac 上的檔案** — 透過系統檔案選取器顯示的裝置其他位置的視訊。
- **雲端儲存** — 您已連線的每個雲端帳戶、NAS 和媒體伺服器。
- **可用設備** — 透過 Bonjour / mDNS 自動發現的本機網路上的伺服器和磁碟機。

檔案畫面右上角有一個傳輸按鈕（旋轉箭頭圖示）。點選它可開啟傳輸佇列，在這裡您可以監控所有來源的每次下載和上傳。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 已連線儲存中的檔案" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## 連線到雲端儲存

檔案標籤頁的雲端儲存部分是所有已連線帳戶、NAS、媒體伺服器和串流所在的地方——並排，在一個可捲動的清單中。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 檔案標籤頁中的雲端儲存部分" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- 開啟**檔案**標籤頁。
- 捲動到**雲端儲存**部分。
- 從選單中點選**連線到雲端儲存**。
- 從清單中選擇雲端儲存服務。
- 在雲端服務提供商提供的官方授權頁面上輸入您的憑據，然後點選**完成**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 連線雲端儲存服務" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

如果遇到問題，請檢查您的網路連線和登入 / 密碼。在應用程式的 Premium 版本中，您可以新增無限數量的服務；免費版本最多支援三個。

## 支援的雲端儲存服務、媒體伺服器和通訊協定

Evervideo 支援極其廣泛的視訊來源。以下所有內容都可透過單一的連線到雲端儲存流程存取。

**個人雲端儲存：** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**自行託管媒體伺服器：** Plex · Jellyfin · Emby · Subsonic（及每個 Subsonic 相容伺服器——Airsonic、Funkwhale、Gonic、Ampache）· Navidrome · Nextcloud（及透過共享 API 的 ownCloud）· Synology Drive · QNAP.

**NAS 和檔案共享通訊協定：** SMB（SMB1、SMB2、Auto）· WebDAV（HTTP / HTTPS）· FTP · FTPS · SFTP（SSH 檔案傳輸通訊協定，密碼或公鑰認證）· NFS · DLNA / UPnP（播放和下載）.

**直播和 IP 攝影機串流：** RTSP——將 Evervideo 指向任意 `rtsp://` URL，它就可以直接播放。非常適合安全攝影機、IPTV 串流、門鈴攝影機、嬰兒監視器和類似的直播來源。

**S3 相容物件儲存：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 以及任何其他 S3 API 端點。

**裝置本機資料庫：** Photos 資料庫（所有視訊、螢幕錄製、相簿）和 Music 應用程式資料庫（專輯、流派、播放清單）——兩者都顯示在媒體資料庫中，無需複製任何內容。

**區域網路探索：** 可用設備部分自動列出 Wi-Fi 網路上的每個 Bonjour / mDNS 服務——Plex、Jellyfin、Emby 伺服器、Synology、QNAP、帶附加磁碟機的 AirPort 路由器、Apple Time Capsule——讓您無需輸入 IP 位址即可點選連線。

每個連線都使用服務的官方 SDK 或開放通訊協定，在支援的情況下使用基於 OAuth 的授權。您可以連線同一服務的多個帳戶（例如兩個 Google Drive 帳戶，或同時使用 Plex 和 Jellyfin 伺服器），並在雲端儲存部分並排瀏覽它們。

## 安全和隱私

Evervideo 僅使用官方 SDK 和安全連線與已連線的雲端服務互動。您的登入名稱和密碼對應用程式不可存取——所有傳輸均採用 TLS 加密。

當您輸入登入名稱和密碼時，應用程式會顯示由雲端服務提供商提供的官方授權頁面，整個授權過程在應用程式外部進行。成功授權後，雲端服務提供商向應用程式傳送 auth-token，該 token 用於進行 API 呼叫。

Auth-token 是一個數位金鑰，允許第三方應用程式代表您與雲端儲存互動。該 token 儲存在您裝置上 Apple 的安全系統儲存（Keychain）中，靜態加密並受裝置密碼或生物辨識鎖保護。您可以將已連線雲端服務中的檔案下載到裝置；這些檔案放置在應用程式的 Documents 目錄中，可以隨時使用內建檔案管理員刪除。

應用程式不會將您已連線雲端帳戶的任何資訊與 Everappz、廣告商或任何第三方共享。您可以隨時透過在網路瀏覽器中開啟帳戶設定頁面來撤銷對雲端帳戶的存取權限。

## 撤銷 Auth-Token

要撤銷 auth-token，請在網路瀏覽器中登入您的雲端帳戶，然後導覽至安全性或已連線應用程式頁面。在那裡您可以找到連線到您雲端帳戶的每個第三方應用程式，並在不再想使用時刪除其中任何一個。Google 帳戶的詳細說明可在[這裡](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)找到。

您也可以在應用程式內斷開雲端帳戶——這樣做時，auth-token 會立即從您的裝置上刪除。如果您從裝置上移除應用程式，所有下載的資料和存取 token 都會隨之自動刪除。

## 斷開雲端儲存或變更設定

- **存取雲端儲存選項** — 在檔案標籤頁的**雲端儲存**部分找到已連線的服務。
- **點選「...」按鈕** 位於服務標題旁邊，開啟其他選項：
  - **重新命名** — 變更雲端服務在您清單中顯示的名稱。
  - **設定** — 修改設定或認證資料。有時如果授權 token 已過期，您可能需要重新授權已連線的雲端服務。
  - **斷開連接** — 完全切斷應用程式與雲端服務之間的連線。這會從您的媒體資料庫中刪除與該服務關聯的所有視訊，但在伺服器上保持完整不變。

## 連線到電腦或 NAS

您可以使用 SMB、WebDAV、FTP / FTPS、SFTP、NFS 或 DLNA 通訊協定連線您的電腦、個人 NAS 或其他網路裝置。這是將現有家庭媒體庫——無論它位於 Mac、Windows PC、Synology、QNAP、Apple Time Capsule 還是 WD My Cloud Home 上——引入 Evervideo 而無需複製任何內容的最簡單方式。

### 使用 SMB 連線到電腦

- 點選**連線到雲端儲存 → SMB**。
- 使用格式 `smb://computer-ip-address/shared-folder-name` 輸入電腦的 IP 位址和共享資料夾名稱。
- 選擇通訊協定版本：**Auto**、**SMB1** 或 **SMB2**。
- 輸入您的登入名稱和密碼（如需）。
- 點選**完成**。

如果連線成功，共享會出現在雲端儲存部分。關於如何使用 SMB 連線 Mac 或 PC 的完整教學可在[這裡](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)找到。

### 使用 WebDAV 連線到 NAS

所有步驟與 SMB 相同，除了 URL 欄位。如果伺服器支援 SSL，請使用 `http://server-name` 或 `https://server-name`。WebDAV 與 Synology、QNAP、Nextcloud、ownCloud、WD My Cloud Home 以及任何具有 WebDAV 端點的其他伺服器相容。

WebDAV 的完整教學可在[這裡](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)找到。

### 透過 DLNA / UPnP 連線

使用 DLNA / UPnP 通訊協定共享位於 Windows PC 或 NAS 上的媒體庫，並在 Evervideo 中存取，如[這裡](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)所述。DLNA 被廣泛支援，但它只允許您播放或下載視訊——您無法在 DLNA 伺服器上上傳檔案或建立新資料夾。

### 使用 FTP、FTPS 或 SFTP 連線

Evervideo 還支援傳統的檔案傳輸通訊協定。要透過 FTP 或 FTPS 連線伺服器，點選連線到雲端儲存 → FTP，以 `ftp://server-name` 形式輸入主機 URL（或 `ftps://server-name` 用於加密連線），提供登入名稱和密碼，然後點選完成。對於 SFTP（SSH 檔案傳輸通訊協定），選擇 SFTP 並提供密碼或 SSH 金鑰組。

### 連線到 NFS 共享

Evervideo 包含 NFS（網路檔案系統）支援——方便用於偏好透過 NFS 而非 SMB 公開視訊庫的 Linux 主機、BSD 伺服器和 NAS 裝置。在連線到雲端儲存選單中選擇 NFS，輸入伺服器位址和匯出路徑，然後點選完成。

## 連線 Plex Media Server

Evervideo 可以直接連線到 Plex Media Server 並瀏覽您的電影、電視節目和家庭視訊庫。點選連線到雲端儲存 → Plex，用您的 Plex 帳戶登入，選擇一個伺服器，庫就會出現在您的雲端服務旁邊。同一區域網路上的 Plex 伺服器也會在可用設備部分自動發現。

## 連線 Jellyfin 或 Emby 伺服器

Jellyfin（開源）和 Emby（商業）媒體伺服器都在 Evervideo 中原生工作。點選連線到雲端儲存 → Jellyfin 或 Emby，輸入您的伺服器 URL（通常是 `http://server-ip:8096`）和憑據，您的庫就可以開始串流了。

## 連線 Subsonic 或 Navidrome 伺服器

Evervideo 支援 Subsonic API，這意味著它與 Subsonic 本身、Navidrome 以及其他每個 Subsonic 相容伺服器相容——包括 Airsonic、Funkwhale、Gonic、Logitech Media Server (LMS) 和 Ampache。點選連線到雲端儲存 → Subsonic，輸入伺服器 URL 和憑據，庫就會出現在雲端儲存部分。

## 連線 RTSP 串流（IP 攝影機、直播 TV、IPTV）

Evervideo 具有原生 RTSP 支援，因此您可以將其指向任何 RTSP 來源——安全攝影機、門鈴攝影機、IPTV 提供商、嬰兒監視器、廣播來源——Evervideo 將即時提取和解碼串流。點選線上連結 → 新增連結，貼上完整 URL（`rtsp://camera-ip:port/stream-path`），如需提供登入名稱和密碼，然後點選完成。

## 連線到 S3 相容物件儲存

對於使用雲端物件儲存的自行託管使用者和進階使用者，Evervideo 包含一個 S3 相容連接器。點選連線到雲端儲存 → S3 儲存，然後輸入端點 URL、區域、存取金鑰、秘密金鑰和儲存桶名稱。這適用於 AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 以及任何其他 S3 API 端點。

## 可用設備

此部分顯示您本機網路上可以透過 Bonjour / mDNS 探索從 Evervideo 連線的每個裝置——Plex、Jellyfin、Emby 伺服器、Synology、QNAP、帶附加磁碟機的 AirPort 路由器、Apple Time Capsule 等。要建立連線：

- 在檔案標籤頁中捲動到可用設備部分。
- 點選您想連線的裝置。
- 如需，輸入登入詳細資訊以完成連線。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 本機網路上的可用設備" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive 讓您可以透過任何桌面瀏覽器、Finder 或 File Explorer 從電腦無線傳輸檔案到 iOS 裝置。您的裝置和電腦必須在同一 Wi-Fi 網路上。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### 啟用 Wi-Fi Drive

- 在檔案標籤頁中，捲動到雲端儲存 → 透過 Wi-Fi 連線，開啟 Wi-Fi Drive 主畫面。
- （選擇性）為嵌入式 Web 伺服器設定使用者名稱和密碼。
- 點選啟動 Wi-Fi Drive。

### 在電腦上存取 Wi-Fi Drive

- 在電腦上開啟 Web 瀏覽器（Chrome、Firefox、Safari 等）。
- 輸入應用程式顯示的 URL。
- 將檔案從電腦拖放到網頁上——它們將開始傳輸到您的 iOS 裝置。

您還可以直接在 macOS 的 **Finder** 中（前往 → 連線到伺服器…）或 Windows 的 File Explorer 中（對應網路磁碟機…）掛載 Wi-Fi Drive，將您的 iPhone 或 iPad 作為一般網路磁碟機使用。

詳細說明可在[這裡](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)找到。

## iTunes / Finder 檔案共享

iTunes 檔案共享（macOS Catalina 及更高版本中現為 Finder 檔案共享）允許您使用 Lightning 或 USB-C 資料線傳輸檔案。連線裝置，在 Mac 上開啟 Finder（或在 Windows 上開啟 iTunes），在應用程式清單中找到 Evervideo，並將檔案複製到其共享資料夾。

## 連接 USB 快閃磁碟機或 SD 卡

透過 Lightning-to-USB / USB-C 轉接器或讀卡機將 USB 磁碟機或 SD 卡插入 iPhone、iPad 或 Mac。開啟檔案 → 此 iPhone 上的檔案 → 開啟資料夾，導覽至磁碟機，選擇視訊檔案或資料夾。Evervideo 直接從磁碟機播放檔案，無需複製到內部儲存空間——非常適合非常大的 4K 資料庫。

## 在已連線儲存中瀏覽資料夾

點選任何已連線的雲端服務開啟其檔案瀏覽器。資料夾在可用時顯示視訊縮圖，點選視訊會立即開始播放，同時在背景中繼續串流檔案的其餘部分。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 在已連線儲存中瀏覽資料夾" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## 快速存取

快速存取部分位於檔案標籤頁的頂部。它提供對您最愛的和最近開啟的檔案和資料夾的快速存取——來自雲端服務和裝置儲存。每當您從雲端開啟檔案或資料夾時，它都會被新增到最近開啟清單中。您可以將深層巢狀的資料夾標記為最愛，以便快速存取而無需遍歷目錄結構。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 線上連結和快速存取" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## 此應用程式中的檔案

此部分顯示儲存在 Evervideo 沙盒 Documents 目錄中的檔案和資料夾——您從雲端下載的所有內容、透過 Wi-Fi Drive 傳輸的、透過 Finder 檔案共享複製的或從其他應用程式匯入的。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 應用程式中的檔案" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Documents 資料夾

Documents 資料夾是「此應用程式中的檔案」內所有內容的根目錄。您可以建立子資料夾、重新命名檔案、移動它們，以及按您喜歡的方式整理。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 本機檔案 — Documents 資料夾" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## 此 iPhone / iPad / Mac 上的檔案

此部分顯示位於您裝置上但在不同應用程式中的視訊。您可以使用系統檔案選取器將它們匯入 Evervideo：

- 點選開啟檔案… 選擇特定檔案。
- 點選開啟資料夾… 選擇整個資料夾。

您還可以使用連接資料夾來建立裝置上具有讀 / 寫存取權限的資料夾連結——非常適合在不複製任何內容的情況下處理 iCloud Drive 上的資料夾或附加的 USB 磁碟機。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 此裝置上的檔案" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## 特殊資料夾

在檔案標籤頁中，您會看到 Evervideo 自動建立和使用的幾個特殊資料夾：

- **下載** — 從雲端下載的每個檔案預設出現在這裡。在設定 → 檔案管理員 → 將下載的檔案儲存到中自訂。
- **播放器快取** — 媒體播放器快取。預設情況下，播放器下載即將播放的視訊以確保流暢播放。您可以在應用程式設定中停用快取或直接刪除此資料夾。
- **iCloud** — 此資料夾中的檔案會在連線到同一 iCloud 帳戶的所有裝置之間同步。
- **離線資料夾** — 當您將資料夾、播放清單、專輯或流派標記為可離線使用時，檔案會下載到此資料夾中。

## 頂部工具列

位於導覽列下方的頂部工具列提供多項操作，您可以透過向下滑動手勢顯示或隱藏：

- **搜尋** — 在目前資料夾或部分中執行搜尋。
- **繼續播放** — 如果在設定中啟用，恢復目前資料夾的播放器佇列和上次視訊位置。
- **播放全部** — 掃描目前資料夾及其子資料夾並將檔案新增到播放器佇列。
- **隨機播放** — 與播放全部類似，但在新增前隨機排序。

## 資料夾選項

開啟資料夾後，點選右上角的 **「...」** 按鈕查看以下操作：

- **選擇** — 啟動檔案選擇模式。
- **新建資料夾** — 在目前資料夾中建立新資料夾。
- **啟用離線模式** — 為目前資料夾開啟離線同步。在線上新增的新檔案會自動下載。
- **上傳檔案** — 將裝置中的檔案上傳到線上資料夾。
- **搜尋** — 在資料夾中搜尋。
- **排序** — 按名稱、大小、修改日期或元資料排序檔案。
- **格線 / 清單視圖** — 在表格視圖和縮圖視圖之間切換。縮圖視圖顯示大型視訊海報預覽。

## 選擇模式

點選右上角的 **「...」** 並選擇**選擇**進入選擇模式。每個檔案和資料夾旁邊會出現核取方塊。點選選擇一個或多個項目，然後執行批次操作：播放下一個、稍後播放、新增到媒體資料庫、新增到播放清單、複製、上傳、移動、重新命名或刪除。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 檔案管理員中的選擇模式" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

如果您希望將已連線的雲端儲存視為唯讀（防止意外刪除），請啟用設定 → 檔案管理員 → 編輯線上檔案 → 關閉，以從介面中隱藏所有破壞性操作。

## 檔案操作

點選檔案標題旁邊的 **「...」** 圖示可顯示其操作選單：

- **播放下一個** — 將檔案插入播放器佇列頂部。
- **稍後播放** — 將檔案附加到播放器佇列底部。
- **新增到媒體資料庫** — 將檔案納入媒體資料庫，按專輯和流派整理。
- **新增到播放清單** — 將檔案新增到現有播放清單或建立新播放清單。
- **編輯標籤** — 開啟內建標籤編輯器修改元資料。對於線上檔案，檔案會暫時下載、編輯，然後在您確認後重新上傳。
- **新增到最愛** — 將檔案新增到最愛項目清單以便快速存取。
- **下載** — 將檔案或資料夾下載到裝置以供離線使用。
- **重新命名** — 直接在遠端儲存上重新命名檔案。
- **移動** — 將檔案移動到雲端儲存中的不同資料夾。
- **新增到封存** — 將檔案打包成單個 ZIP 檔案（Premium 功能）。
- **以...開啟** — 透過系統分享頁將檔案匯出到其他相容應用程式。
- **刪除** — 永久刪除檔案。**此操作無法復原。**

## 資料夾操作

對於雲端儲存中的每個資料夾，透過點選資料夾標題旁邊的 **「...」** 圖示可以使用多項操作。

- **播放全部** — 用資料夾中的所有視訊取代目前播放器佇列。
- **播放下一個 / 稍後播放** — 將整個資料夾新增到佇列。
- **新增到媒體資料庫** — 將資料夾內容納入媒體資料庫。
- **新增到播放清單** — 將整個資料夾新增到播放清單。
- **新增到最愛** — 將資料夾新增到最愛。
- **啟用離線模式** — 除了簡單下載，這還會持續監控資料夾中的新檔案，並在它們出現在線上時自動下載。
- **下載** — 將資料夾的所有內容下載到裝置以供離線存取。
- **重新命名 / 移動** — 在遠端儲存上重新命名或移動資料夾。
- **新增到封存** — 將資料夾內容打包成 ZIP 檔案（Premium 功能）。
- **刪除** — 永久刪除資料夾及其內容。**此操作無法復原。**

## 傳輸佇列

檔案標籤頁右上角有一個**傳輸**按鈕（旋轉箭頭圖示）。點選它可開啟傳輸佇列——所有來源的每個活動下載和上傳的清單，附帶即時進度、速度和每個檔案的預計時間。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 檔案傳輸佇列" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

您可以暫停、恢復、重試失敗的傳輸、重新排列項目以優先處理特定下載，或逐個取消。您還可以在設定 → 檔案管理員中調整傳輸佇列速度（最大平行任務數）、網路類型（僅 Wi-Fi 或 Wi-Fi + 行動網路）和背景傳輸。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 檔案傳輸佇列上的操作" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## 離線模式和同步離線資料夾

離線模式是一項實用功能，讓您即使在沒有網路連線時也可以觀看喜愛的視訊。當您為任何資料夾、播放清單、專輯或流派啟用離線模式時，該集合中的所有檔案都會自動下載到裝置以供離線播放。它們顯示在離線資料夾部分。

當您向遠端伺服器新增新檔案時，它們也會自動下載——因此您的離線集合始終保持最新，無需您做任何操作。要手動重新同步，點選離線資料夾右上角的三個點，選擇同步。

您可以在設定 → 檔案管理員 → 同步離線資料夾 → 時間間隔中調整同步逾時。

詳細說明可在[這裡](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/)找到。

## 個人化

在設定 → 個人化中，您可以設定檔案標籤頁的顯示方式：

- **檔案畫面樣式** — 純選單（直接顯示資料夾清單）或分組選單（按類別分組內容——快速存取、特殊資料夾、雲端儲存等）。
