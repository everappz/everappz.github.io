---
title: "連接"
date: 2020-02-01
description: "了解如何將雲端服務和 NAS 裝置連接到 Flacbox。從 iCloud Drive、Dropbox、Google Drive、OneDrive、MEGA、Box、pCloud、Synology Drive、Yandex Disk 等串流高解析度音樂。使用 SMB、WebDAV、DLNA、FTP / SFTP、Wi-Fi Drive、iTunes / Finder 檔案共享和 USB 隨身碟。"
keywords: [
  "Flacbox 雲端設定", "連接 Google Drive 到 Flacbox", "SMB 音樂串流",
  "WebDAV iOS 播放器", "DLNA 音樂應用程式", "NAS 音訊串流", "Wi-Fi Drive iPhone",
  "傳輸檔案到 iPhone", "Flacbox iTunes 檔案共享", "連接 NAS 到 iPhone",
  "Synology Drive 音樂應用程式", "QNAP 音樂應用程式", "Bluesound 音樂應用程式",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm 回報播放紀錄",
  "iXpand 隨身碟音樂", "USB DAC iPhone"
]
tags: ["指南", "flacbox", "連接", "雲端", "NAS"]
readingTime: 12
---


在此畫面上，您可以連接存放音樂的所有來源。您可以整合 Dropbox、Google Drive、iCloud Drive、OneDrive、MEGA、Box、pCloud、Yandex Disk、Synology Drive 等熱門雲端服務，以及透過標準協定連接 Mac、PC 或 NAS。無論您的音樂收藏存放在 Dropbox 等雲端服務，還是 Synology、QNAP、Buffalo、Apple Time Capsule、WD My Cloud Home 等個人 NAS 上，Flacbox 都能從單一畫面連接所有這些來源。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 連接畫面" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## 連接到雲端儲存空間

- 開啟**連接**標籤頁。
- 從選單中選擇**連接到雲端儲存空間**。
- 從清單中選擇雲端儲存服務。
- 在雲端服務提供商的官方授權頁面上輸入您的憑據，然後點擊**完成**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 新增雲端儲存服務" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

如果遇到問題，請檢查網路連線和登入名稱 / 密碼。在 Premium 版本中，您可以新增無限數量的服務；免費版本最多支援三個。

## 支援的雲端儲存服務、媒體伺服器和協定

Flacbox 支援極為豐富的音樂來源。以下所有內容都可透過一個**連接到雲端儲存空間**畫面存取。

**個人雲端儲存：** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**自架伺服器：** Plex · Jellyfin · Emby · Subsonic（及所有 Subsonic 相容伺服器——Airsonic、Funkwhale、Gonic、Logitech Media Server、Ampache）· Navidrome · Nextcloud（以及透過共享 API 的 ownCloud）· Synology Drive · QNAP.

**NAS 和檔案共享協定：** SMB（SMB1、SMB2、Auto）· WebDAV（HTTP / HTTPS）· FTP · FTPS · SFTP（SSH 檔案傳輸協定，密碼或公鑰認證）· NFS · DLNA / UPnP（播放和下載）。

**S3 相容物件儲存：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 及任何其他 S3-API 端點。

**區域網路探索：**「可用設備」區域自動列出 Wi-Fi 上的所有 Bonjour / mDNS 服務，無需輸入 IP 位址即可輕點連接。

每個連接都使用服務的**官方 SDK 或開放協定**，並在支援的情況下使用 OAuth 授權。您可以連接同一服務的多個帳戶，並在連接畫面中並排瀏覽它們。

## 安全與隱私

我們僅使用官方 SDK 和安全連線與已連接的雲端服務進行互動。您的登入名稱和密碼無法被應用程式存取——所有傳輸均經過 TLS 加密。

當您輸入登入名稱和密碼時，應用程式會顯示雲端服務提供商的官方授權頁面，整個授權過程在應用程式外部進行。雲端服務提供商在成功授權後向應用程式傳送 auth-token，該 token 用於進行 API 呼叫。

auth-token 是一種數位金鑰，允許第三方應用程式代表您與雲端儲存空間互動。token 存放在裝置上 Apple 的安全系統儲存空間（Keychain）中，靜態加密並由裝置密碼或生物特徵鎖保護。

應用程式不會將您已連接雲端帳戶中的任何資訊與 Everappz、廣告商或任何第三方共享。您可以隨時透過在網頁瀏覽器中開啟帳戶設定頁面來撤銷對您雲端帳戶的存取權限。

## 撤銷 Auth-Token

要撤銷 auth-token，請在網頁瀏覽器中登入您的雲端帳戶並導覽至安全性或已連接應用程式頁面。在那裡您可以找到連接到您雲端帳戶的每個第三方應用程式，並移除不再需要的任何應用。Google 帳戶的詳細說明請參閱[此處](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)。

您也可以在應用程式內斷開雲端帳戶——此時 auth-token 立即從您的裝置中刪除。如果您從裝置上解除安裝應用程式，所有已下載的資料和存取權杖都會自動隨之刪除。

## 斷開雲端儲存空間或變更設定

- **存取雲端儲存空間選項** — 在**連接**畫面中找到已連接的服務。
- **點擊服務標題旁的「...」按鈕**以開啟更多選項：
  - **重新命名** — 變更雲端服務在清單中的顯示名稱。
  - **設定** — 修改設定或身分驗證資料。有時您可能需要重新授權，如果授權 token 已過期。
  - **斷開連接** — 完全切斷應用程式與雲端服務之間的連線。這會從您的應用音樂庫中刪除與該服務關聯的所有歌曲，但它們在伺服器上保持不變。

## 連接到電腦或 NAS

您也可以使用 SMB、DLNA 或 WebDAV 協定連接電腦、個人 NAS 或其他網路裝置。這是將現有家庭音樂庫——無論存放在 Mac、Windows PC、Synology 還是 NAS 上——帶入 Flacbox 而無需複製任何內容的最簡便方式。

## 透過 SMB 連接到電腦

- 點擊**連接到雲端儲存空間 → SMB**。
- 在 URL 欄位中以 `smb://computer-ip-address/shared-folder-name` 格式輸入電腦 IP 位址和共享資料夾名稱。
- 選擇協定版本：**Auto**、**SMB1** 或 **SMB2**。
- 輸入登入名稱和密碼（如需要）。
- 點擊**完成**。

如果連線成功，您將在**雲端儲存空間**部分看到已連接的儲存空間。關於如何使用 SMB 連接 Mac 或 PC 的完整教學請參閱[此處](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)。

## 透過 WebDAV 連接到 NAS

所有步驟與 SMB 相同，除了 URL 欄位。URL 應為 `http://server-name` 或 `https://server-name`（如果伺服器支援 SSL）。WebDAV 可與 **Synology、QNAP、Nextcloud、ownCloud** 及許多其他伺服器搭配使用。

關於如何使用 WebDAV 連接 NAS 的完整教學請參閱[此處](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)。

## 透過 DLNA 連接到電腦或 NAS

您也可以使用 DLNA / UPnP 協定共享 Windows PC 或個人 NAS 上的音樂庫，如[此處](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)所述。DLNA 只允許播放或下載音樂，無法上傳檔案或在 DLNA 伺服器上建立新資料夾。

## 透過 FTP、FTPS 或 SFTP 連接到 NAS 或伺服器

Flacbox 還支援傳統的檔案傳輸協定。要透過 FTP 或 FTPS 連接伺服器，點擊**連接到雲端儲存空間 → FTP**，以 `ftp://server-name`（或加密連線為 `ftps://server-name`）格式輸入主機 URL，提供登入名稱和密碼，然後點擊**完成**。對於 **SFTP**，選擇 **SFTP** 並提供密碼或 SSH 金鑰對。

## 連接到 NFS 共享

Flacbox 支援 **NFS**（網路檔案系統）。在**連接到雲端儲存空間**選單中選擇 **NFS**，輸入伺服器位址和匯出路徑，然後點擊**完成**。

## 連接 Plex Media Server

Flacbox 可以直接連接 Plex Media Server 並按藝術家、專輯、類型和播放清單瀏覽您的音樂庫。點擊**連接到雲端儲存空間 → Plex**，用您的 Plex 帳戶登入，選擇一個伺服器——音樂庫將與您的雲端服務一起顯示。

## 連接 Jellyfin 或 Emby 伺服器

**Jellyfin**（開源）和 **Emby**（商業）媒體伺服器在 Flacbox 中均可原生使用。點擊**連接到雲端儲存空間 → Jellyfin** 或 **Emby**，輸入伺服器 URL 和憑據，音樂庫即可串流。

## 連接 Subsonic 或 Navidrome 伺服器

Flacbox 支援 Subsonic API，即可與 **Subsonic**、**Navidrome** 及每個其他 Subsonic 相容伺服器搭配使用。點擊**連接到雲端儲存空間 → Subsonic**，輸入伺服器 URL 和憑據。

## 連接到 S3 相容物件儲存空間

點擊**連接到雲端儲存空間 → S3 儲存空間**，然後輸入端點 URL、區域、存取金鑰、秘密金鑰和儲存貯體名稱。適用於 AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 及任何其他 S3-API 服務。

## 可用設備

此部分透過 Bonjour 探索顯示區域網路上您可以連接的每個裝置。

- 開啟應用程式並前往「連接」下的**可用設備**部分。
- 點擊您要連接的裝置。
- 如需要，輸入登入資訊以完成連線。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 區域網路上的可用設備" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive 是一種便捷技術，可透過任何桌面瀏覽器從電腦無線傳輸檔案到 iOS 裝置。請確保您的裝置和電腦連接到同一 Wi-Fi 網路。

### 啟用 Wi-Fi Drive

- 開啟應用程式並前往**連接**標籤頁。
- 選擇**透過 Wi-Fi 連接**以存取 Wi-Fi Drive 主畫面。
- （可選）為嵌入式 Web 伺服器設定使用者名稱和密碼以保護存取。
- 點擊**啟動 Wi-Fi Drive** 以啟用 Wi-Fi Drive。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### 在電腦上存取 Wi-Fi Drive

- 在電腦上開啟網頁瀏覽器（如 Chrome、Firefox 或 Safari）。
- 在網址列中輸入應用程式提供的 URL。

### 無線傳輸檔案

當與您 iOS 裝置對應的網頁在瀏覽器中開啟後，您可以輕鬆地從電腦將檔案拖放到網頁上。您拖放的檔案將開始傳輸到您的 iOS 裝置，並可在 Flacbox 內存取。

您也可以在 macOS 的 Finder 中直接掛載 Wi-Fi Drive（前往 → 連接至伺服器…）或在 Windows 的檔案總管中（對應網路磁碟機…）。

關於如何使用 Wi-Fi Drive 無線傳輸檔案的詳細說明請參閱[此處](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)。

## iTunes / Finder 檔案共享

iTunes 檔案共享（在 macOS Catalina 及更高版本上現為 Finder 檔案共享）是透過 Lightning 或 USB-C 連接線從電腦傳輸檔案到裝置的另一種方式。

- 使用連接線將裝置連接到電腦，並在 Mac 上執行 **Finder**（或在 Windows 上執行 **iTunes**）。
- 開啟**位置 → 您已連接的裝置 → 檔案**並找到 Flacbox 應用程式。
- 點擊應用程式圖示以查看所有共享資料夾。
- 透過拖放將檔案從電腦複製到裝置上的共享資料夾。

關於如何使用 Finder 檔案共享的詳細說明請參閱[此處](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/)。

## 連接 USB 隨身碟

如果您有 SD 卡或 USB 磁碟機，可以使用 Lightning to USB / SD 讀卡器或 USB-C 磁碟機（在 iPad 和 iPhone 15 / 16 / 17 / Pro 上）連接。應用程式支援 Apple 認證的讀卡器和 iXpand 隨身碟。

關於如何將 USB 隨身碟連接到 iPhone 的詳細說明請參閱[此處](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it)。

## 檔案管理器

連接雲端儲存服務後，點擊其圖示查看所有可用檔案和資料夾。您可以使用內建檔案管理器處理這些檔案——下載、重新命名、移動、上傳、刪除等。

## 頂部工具列

頂部工具列方便地位於導覽列下方，提供幾個常用操作。您可以透過向下輕掃手勢顯示或隱藏它。

- **搜尋** — 在當前目錄中執行快速搜尋。
- **繼續播放** — 如果在應用程式設定中啟用，將恢復音訊播放器佇列和當前資料夾的最後媒體位置。
- **播放全部** — 掃描當前資料夾及其子資料夾，然後將所有找到的音訊檔案新增到新的播放器佇列中。
- **隨機播放全部** — 與播放全部相似，但在新增到音訊播放器佇列之前隨機排列檔案。

## 資料夾選項

開啟資料夾時，點擊右上角的 **«...»** 按鈕可存取操作：

- **選擇** — 啟動檔案選擇模式。
- **新建資料夾** — 在當前資料夾中建立新資料夾。
- **啟用離線模式** — 為當前資料夾切換離線模式，自動監控資料夾變化。
- **上傳檔案** — 將裝置上的檔案上傳到線上資料夾。
- **搜尋** — 在當前資料夾中搜尋特定檔案。
- **排序** — 按名稱、大小、修改日期或後設資料排序檔案。
- **網格 / 清單視圖** — 在表格視圖和縮圖視圖之間切換。

## 編輯線上檔案

要管理雲端儲存空間中的多個檔案，使用**選擇模式**：

- **啟動選擇模式** — 點擊右上角的 **«...»** 按鈕並選擇**選擇**。
- **選擇檔案** — 每個檔案和資料夾旁邊出現核取方塊。
- **執行操作** — 選擇檔案後，可進行：播放下一首、稍後播放、新增到音樂庫、新增到播放清單、複製、上傳、移動、重新命名、刪除。

## 檔案操作

點擊檔案標題旁的 **«...»** 圖示以顯示操作選單：

- **播放下一首** — 將檔案插入播放器佇列頂部。
- **稍後播放** — 將檔案附加到播放器佇列底部。
- **新增到音樂庫** — 將檔案納入音樂庫。
- **新增到播放清單** — 將檔案新增到現有播放清單或建立新播放清單。
- **編輯音訊標籤** — 開啟內建標籤編輯器修改後設資料。
- **新增到最愛** — 將檔案新增到最愛項目以便快速存取。
- **下載** — 將檔案或資料夾下載到裝置以供離線使用。
- **重新命名** — 直接在遠端儲存空間上重新命名檔案。
- **移動** — 將檔案移動到雲端儲存空間中的其他資料夾。
- **以...開啟** — 將檔案匯出到另一個相容應用程式。
- **刪除** — 從雲端儲存空間中永久刪除檔案。**此操作無法復原。**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 已連接雲端儲存空間中檔案的更多操作" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

## 資料夾操作

對於雲端儲存空間中的每個資料夾，點擊資料夾標題旁的 **«...»** 圖示可存取多種操作：

- **播放全部** — 用所選資料夾中的所有內容替換當前播放器佇列。
- **播放下一首** — 將整個資料夾新增到播放器佇列頂部。
- **稍後播放** — 將資料夾內容附加到播放器佇列底部。
- **新增到音樂庫** — 將資料夾內容納入音樂庫。
- **新增到播放清單** — 將整個資料夾新增到播放清單。
- **新增到最愛** — 將資料夾新增到最愛項目。
- **啟用離線模式** — 持續監控資料夾並在檔案出現時自動下載。
- **下載** — 將資料夾所有內容下載到裝置以供離線存取。
- **重新命名** — 直接在遠端儲存空間上重新命名資料夾。
- **移動** — 將資料夾移動到雲端儲存空間中的其他位置。
- **封存 (ZIP)** — 將資料夾內容打包成單個 ZIP 檔案（Premium 功能）。
- **刪除** — 從雲端儲存空間中永久刪除資料夾及其內容。**此操作無法復原。**

## 快速存取

快速存取部分位於畫面頂部。它讓您快速存取已連接雲端服務中的最愛和最近開啟的檔案。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 線上連結和快速存取" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## 其他服務

此部分顯示增強使用體驗的額外功能。目前，應用程式支援 **Last.fm** 回報播放紀錄——連接後，您的播放統計資料會自動傳送到您的 Last.fm 帳戶。詳細設定說明請參閱[此處](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm 連接" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
