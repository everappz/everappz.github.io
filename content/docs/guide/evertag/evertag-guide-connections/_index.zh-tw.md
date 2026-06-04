---
title: "連接"
date: 2020-02-01
description: "了解如何將雲端儲存、NAS 和電腦連接到 Evertag。直接從雲端儲存、個人 NAS 或 Mac/PC 存取和編輯音訊檔案。"
keywords: [
  "Evertag 雲端設定", "連接 iCloud 到 Evertag", "iOS SMB 檔案存取",
  "WebDAV 音訊標籤編輯器", "NAS 元資料編輯", "Wi-Fi Drive Evertag",
  "傳輸音訊檔案到 iPhone", "Evertag iTunes File Sharing", "從雲端編輯 FLAC 標籤"
]
tags: ["指南", "evertag", "連接"]
readingTime: 11
---


在此畫面上，您可以連接各種包含音訊檔案的來源。您可以整合 Google Drive、Dropbox、OneDrive、iCloud 等熱門雲端服務，以及連接您的 Mac 或 PC。此外，您還可以選擇編輯存放在 Apple Time Capsule、WD Cloud Home 或任何支援 SMB 或 WebDAV 的 NAS 上的音訊檔案。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Connections Screen" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## 快速存取

在連接畫面頂部，您會找到一個**快速存取**列表。任何加入最愛的雲端資料夾——即使嵌套在多層目錄中——都會顯示在這裡，讓您無需每次都瀏覽父資料夾即可直接跳轉。

## 連接到雲端儲存

- 開啟「連接」標籤頁  
- 從選單中選擇「連接到雲端儲存」  
- 從清單中選擇雲端儲存服務  
- 輸入您的憑據，然後點選「完成」。

如果遇到任何問題，請檢查您的網際網路連線和登入名稱/密碼。  
在應用程式的進階版本中，您可以新增無限數量的服務。

## 支援的雲端儲存服務

目前，應用程式支援最流行的雲端儲存服務：iCloud Drive、Google Drive、Dropbox、OneDrive、Box、MEGA、Yandex.Disk、pCloud、Synology Drive、MediaFire、WD My Cloud Home、InfiniCLOUD (TeraCLOUD)、HiDrive、OpenDrive、MyDrive、Put.io、Cloud Mail.ru、百度網盤，以及任何 SMB 或 WebDAV 伺服器。

## 安全性與隱私

我們僅使用官方 SDK 和安全連線與已連接的雲端服務互動。您的登入名稱和密碼對應用程式不可存取。應用程式向雲端服務發出的所有請求都經過加密。

當您輸入登入名稱和密碼時，應用程式會顯示雲端服務提供商提供的官方授權頁面，整個授權過程在應用程式外部進行。授權成功後，雲端服務提供商將授權權杖傳送給應用程式，該權杖用於進行 API 呼叫。

授權權杖是允許第三方應用程式與雲端儲存互動的數位金鑰。授權權杖儲存在裝置上名為 Keychain 的安全系統儲存中。您可以將檔案從已連接的雲端服務下載到裝置，這些檔案將存放在應用程式的「文件」目錄中。您可以隨時使用內建檔案管理器刪除這些檔案。

應用程式不會共享來自已連接雲端帳戶的任何資訊。您可以隨時透過在網頁瀏覽器中開啟帳戶設定頁面來撤銷對雲端帳戶的存取權限。

## 撤銷授權權杖

在網頁瀏覽器中登入您的帳戶並前往設定頁面。在那裡，您可以找到所有連接到您雲端帳戶的第三方應用程式，並在不想繼續使用時刪除其中任何一個。詳細說明可在[此處](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)找到。

您也可以在應用程式中斷開已連接的雲端帳戶，授權權杖也將從您的裝置中刪除。如果您從裝置中刪除應用程式，所有已下載的資料和存取權杖也將被刪除。

## 斷開雲端儲存或變更設定

- 在應用程式介面中找到您要管理的雲端儲存。  
- 點選服務標題旁邊的「...」按鈕以存取更多選項。  
  - **重新命名**：更改雲端服務在清單中顯示的名稱。  
  - **設定**：修改雲端服務的設定或驗證資料。如果授權權杖已過期，有時可能需要重新授權已連接的雲端服務。  
  - **斷開連接**：完全切斷應用程式與雲端服務之間的連線。請注意，選擇此選項將從應用程式的音樂庫中刪除與此雲端服務關聯的所有歌曲，但它們仍將保留在伺服器上。

## 連接到電腦或 NAS

您還可以使用 SMB、DLNA 或 WebDAV 通訊協定連接您的電腦、個人 NAS 或其他網路裝置。

## 透過 SMB 連接到電腦

- 點選「連接到雲端儲存」→ SMB。  
- 在 URL 欄位中輸入電腦 IP 位址和共享資料夾名稱，格式為 smb://computer-ip-address/shared-folder-name  
- 選擇通訊協定版本：Auto、SMB1、SMB2  
- 輸入登入名稱和密碼（如果需要）  
- 點選「完成」。

如果連線成功，您將在「雲端儲存」部分看到已連接的儲存。  
有關如何使用 SMB 連接 Mac 或 PC 的完整教學，請訪問[此處](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)。

## 透過 WebDAV 連接到 NAS

所有步驟相同，只是 URL 欄位不同。  
URL 應採用 http://server-name 格式，如果伺服器支援 SSL，則使用 https://server-name。  
有關如何使用 WebDAV 通訊協定連接 NAS 的完整教學，請訪問[此處](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)。

## 可用設備

此部分顯示您本地網路中所有可透過應用程式連接的裝置。  
要與裝置建立連線，請按照以下步驟操作：

- 開啟應用程式並前往「可用設備」部分。  
- 從清單中點選您要連接的裝置。  
- 如果需要，輸入您的登入詳細資訊以完成連線。

## Wi-Fi Drive

Wi-Fi Drive 是一種便捷技術，可透過桌面瀏覽器將檔案從電腦無線傳輸到 iOS 裝置。  
要有效使用此功能，請確保您的裝置和電腦連接到同一 Wi-Fi 網路。  
以下是使用 Wi-Fi Drive 的逐步指南。

## 啟用 Wi-Fi Drive

- 開啟應用程式並前往「連接」標籤頁。  
- 選擇「透過 Wi-Fi 連接」以存取 Wi-Fi Drive 主畫面。  
- 點選「啟動 Wi-Fi Drive」以啟用 Wi-Fi Drive。

## 在電腦上存取 Wi-Fi Drive

- 在電腦（桌上型或筆記型電腦）上，開啟網頁瀏覽器（Chrome、Firefox 或 Safari）。  
- 在瀏覽器的網址列中，輸入應用程式提供的 URL。

## 無線傳輸檔案

當對應您 iOS 裝置的網頁在瀏覽器中開啟後，您可以輕鬆地將檔案從電腦拖放到網頁上。  
您拖放的檔案將開始傳輸到您的 iOS 裝置，並可在應用程式內存取。

有關如何使用 Wi-Fi Drive 無線傳輸檔案的詳細說明，請訪問[此處](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)。

## iTunes File Sharing

iTunes File Sharing 是另一種技術，允許您使用 Mac 上的 Finder 應用程式和 Lightning 數據線從電腦向裝置傳輸檔案。  
- 只需使用數據線將裝置連接到電腦，然後在 Mac 上執行 Finder 應用程式。  
- 開啟「位置」→「您的已連接裝置」→「檔案」→ 找到目前應用程式。  
- 點選應用程式圖示查看所有共享資料夾。  
- 使用拖放方式將檔案從電腦複製到裝置上的共享資料夾。

有關如何使用 iTunes File Sharing 的詳細說明，請訪問[此處](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/)。

## 連接 USB 隨身碟

如果您有 SD 卡或 USB 隨身碟，可以在 iPhone/iPad 上使用 Lightning 或 USB-C 讀卡機連接，或直接插入 Mac。應用程式目前支援 Apple 認證的讀卡機。我們有關於如何將 USB 隨身碟連接到 iPhone 或 iPad 並管理其中檔案的詳細說明，請訪問[此處](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it)。已連接的磁碟機將顯示在連接畫面的**連接的配件**部分。

## 檔案管理器

連接雲端儲存服務後，點選其圖示查看所有可用檔案和資料夾。您可以使用內建檔案管理器處理這些檔案——下載、重新命名、移動等。開始下載時，檔案將出現在傳輸佇列中。要查看傳輸佇列，請前往「本機檔案」標籤頁，點選左上角的旋轉箭頭圖示。所有已下載的檔案和資料夾均可在「本機檔案」部分存取。

## 頂部工具列

頂部工具列位於導覽列下方，提供幾個便捷操作的快速存取。您可以透過向下滑動手勢顯示或隱藏此工具列。可用操作：

- **搜尋**：在目前目錄中執行快速搜尋，輕鬆找到特定檔案或資料夾。  

## 資料夾選項

當您在應用程式中開啟資料夾時，點選畫面右上角的「...」按鈕即可找到一組便捷操作。  
可用操作：

- **選擇**：啟動檔案選擇模式，在資料夾中選擇一個或多個檔案。  
- **新增資料夾**：在目前資料夾中建立新資料夾以整理檔案。  
- **上傳檔案**：將裝置中的檔案上傳到線上資料夾。  
- **搜尋**：在目前資料夾中搜尋特定檔案。  
- **排序**：按名稱、大小或編輯日期對資料夾中的檔案進行排序。  
- **格狀/清單檢視**：在表格檢視和縮圖檢視之間切換。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloud Folder Sort" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## 編輯線上檔案

當需要管理雲端儲存中的多個檔案時，可以使用選擇模式來簡化操作。步驟如下：

- **啟動選擇模式**：開啟應用程式並導覽到包含雲端儲存的部分。點選右上角的「...」按鈕，選擇「選擇」選單項目以啟動選擇模式。  
- **選擇檔案**：每個檔案或資料夾旁邊會出現核取方塊。點選旁邊的核取方塊選擇一個或多個檔案或資料夾。  
- **執行各種操作**：選擇檔案或資料夾後，您將可以存取針對您需求量身定制的多種操作。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Select" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## 檔案操作

在檔案標題附近，您會看到省略符號「...」（三個點）——這是操作選單。  
點選它可顯示可用操作清單：

- **編輯音訊標籤**：存取內建標籤編輯器，修改所選檔案的音訊標籤。檔案將臨時下載到暫存目錄，確認變更後上傳回儲存。  
- **新增到最愛項目**：將檔案新增到最愛檔案清單以便快速存取。  
- **下載**：將檔案或資料夾下載到裝置以供離線使用。  
- **重新命名**：直接在遠端儲存上重新命名檔案。  
- **移動**：將檔案移動到雲端儲存中的其他資料夾。  
- **開啟方式**：將檔案匯出到其他相容應用程式。檔案將下載到裝置，然後顯示分享對話框。  
- **刪除**：此操作會從雲端儲存中永久刪除檔案。**此刪除操作無法復原**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Options" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

如果操作清單超出畫面可用空間，只需在操作選單中向下捲動即可存取更多選項。

## 資料夾操作

對於雲端儲存中的每個資料夾，您都有多種可用操作。只需點選資料夾標題旁邊的省略圖示「...」。如果看不到所有操作，請向下捲動以顯示更多選項。可用操作：

- **新增到最愛項目**：將資料夾新增到最愛清單以便快速存取。  
- **下載**：將資料夾的所有內容下載到裝置以供離線存取。  
- **重新命名**：直接在遠端儲存上重新命名資料夾。  
- **移動**：將資料夾移動到雲端儲存中的其他位置。  
- **刪除**：此操作會從雲端儲存中永久刪除資料夾及其內容。**此操作無法復原**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Folder Options" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
