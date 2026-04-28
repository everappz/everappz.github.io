---
title: "如何連接 Synology NAS 並在 iPhone 或 Mac 上聆聽音樂"
date: 2024-09-19
description: "了解如何使用原生 API 或 QuickConnect 連接您的 Synology NAS，並透過 Evermusic 和 Flacbox 在 iPhone 或 Mac 上串流高品質音樂。"
keywords: ["synology nas", "串流音樂", "quickconnect", "evermusic synology", "flacbox synology", "nas 音樂播放器", "iphone nas 音樂"]
tags: ["音樂", "串流", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**摘要：** 使用 Synology 的原生 API 將 Synology NAS 連接到 Evermusic 或 Flacbox —— 透過 IP 位址手動連接或透過 QuickConnect ID 自動連接。QuickConnect 讓您無需連接埠轉發即可遠端串流音樂。兩款應用程式都支援 FLAC、MP3、WAV 及其他高解析度格式。

如果您正在尋找一種無縫的方式來連接 Synology NAS 並在 iPhone 或 Mac 上享受音樂庫，Evermusic 和 Flacbox 應用程式是完美的解決方案。這些應用程式支援多種音訊格式，包括 FLAC、MP3 和 WAV，讓您可以輕鬆地從 Synology NAS 直接串流和聆聽高品質音樂。

在本指南中，我們將向您展示如何使用 Synology 的原生 API 和 QuickConnect 功能將 Synology NAS 連接到 Evermusic 或 Flacbox 應用程式。透過利用 Synology 的直接 API，您可以在家庭網路之外安全地存取音樂庫，無需 WebDAV、SMB、DLNA 等複雜配置。藉助 QuickConnect，您可以使用 iPhone 或 Mac 從任何地方串流和管理音樂。

## 步驟 1：設定共用資料夾權限（選用）

1. 開啟**控制台**並前往**共用資料夾**區段。

![共用資料夾](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. 選擇 **Music** 資料夾並點選**編輯**。

3. 在**權限**標籤中設定權限。如果您只需要聽音樂，請啟用唯讀的訪客存取；如果需要修改檔案，請啟用讀寫權限。儲存變更。

![權限](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## 步驟 2：尋找 Synology NAS IP 位址

1. 開啟**控制台**並前往**網路介面**標籤。

![網路介面](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. 或使用瀏覽器造訪 [find.synology.com](http://find.synology.com)。

![尋找 Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. 記下 Synology NAS 的 IP 位址（例如 192.168.18.137）。

## 步驟 3：尋找 Synology NAS 網路連接埠

您可以在此 [Synology 知識中心文章](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services)中找到 Synology 官方的 DSM 預設網路連接埠文件。

Synology DSM 使用以下預設連接埠：
- **HTTP（Web 存取）：** 連接埠 **5000**
- **HTTPS（安全 Web 存取）：** 連接埠 **5001**

這些是存取 DSM 介面的預設連接埠。

![網路連接埠](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## 步驟 4：啟用 QuickConnect ID 功能

Synology QuickConnect ID 是一個唯一識別碼，允許您透過網際網路遠端存取 Synology NAS，無需設定連接埠轉發等複雜的網路設定。QuickConnect 透過使用 Synology 的伺服器來建立 NAS 與您的裝置（如智慧型手機或電腦）之間的連線，從而簡化遠端存取。

**如何尋找或設定 QuickConnect ID：**

1. **登入 DSM。**
2. 前往**控制台 > 外部存取 > QuickConnect**。
3. **啟用 QuickConnect** 並建立或檢視您的唯一 QuickConnect ID。

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## 步驟 5：使用 Evermusic 或 Flacbox 在 iPhone/Mac 上連接 Synology NAS

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) 和 [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) 都是為 iOS 和 macOS 裝置設計的音樂播放器應用程式，各自提供獨特的功能來管理和享受您的音樂庫。

1. 開啟 Evermusic 或 Flacbox 應用程式並前往**連接**標籤。

![連接](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. 選擇**連接雲端服務**並選擇 **Synology Drive**。

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

您有兩種連線選項：使用伺服器 IP 位址和連接埠的**手動**連線，或透過 QuickConnect ID 的**自動**連線。

### 手動連線

對於手動方法，您需要在之前步驟中取得的直接 IP 位址和連接埠號。

1. 輸入在步驟 2 中取得的伺服器 URL，使用以下格式：通訊協定://IP位址:連接埠號
   - HTTP 使用**連接埠 5000**，HTTPS 連線使用**連接埠 5001**。

   例如：
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. 實際連接埠號可在設定的步驟 3 中確認。
3. 輸入 Synology NAS 的**使用者名稱**和**密碼**。
4. 點選**登入**以建立連線。

![手動連線](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### 自動連線

對於自動連線，您將使用步驟 4 中的 **QuickConnect ID**。無需手動輸入 Synology NAS 的 IP 位址和連接埠號，只需輸入 **QuickConnect ID**。應用程式將自動取得必要的連線資訊。

此方法允許您遠端存取 NAS，即使在家庭網路之外，也可以透過網際網路管理檔案，無需設定連接埠轉發或靜態 IP 位址。

![自動連線](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## 雙重身份驗證

從 DSM 4.2 開始，Synology 引入了**兩步驟驗證**以增強安全性。此功能需要由驗證應用程式產生的**一次性密碼 (OTP)** 代碼，作為一般登入憑證的補充。如果您已啟用兩步驟驗證，在輸入使用者名稱和密碼後，還需要輸入 OTP 才能登入 DSM 工作階段。

請注意，工作階段過期後，需要手動重新授權應用程式。要重新授權：

1. 前往應用程式中的**連接**標籤。
2. 點選伺服器名稱旁邊的**更多操作**按鈕。
3. 從選單中選擇**設定**以輸入新的驗證代碼並完成重新授權流程。

這確保即使您從不受信任的網路存取 NAS，您的資料也能保持安全。

## 步驟 6：瀏覽和播放音樂

1. 連線後，裝置將出現在**已連接裝置**清單中。

![已連接裝置](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. 導覽至 **Music** 資料夾，點選任意音訊檔案開始播放。

![播放音樂](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## 步驟 7：將已連接的雲端資料夾新增到音樂庫

1. 在應用程式中開啟**音樂庫**區段。
2. 選擇**新增音樂**並選擇**連接**。
3. 選擇已連接的 NAS 伺服器並選擇 **Music** 資料夾。點選**完成**。
4. 應用程式將掃描音樂資料夾並將支援的音訊檔案新增到音樂庫。中繼資料將被載入，您的曲目將按專輯、藝術家和類型分組。

## 結語

按照這些步驟，您可以輕鬆地在 Synology NAS 上設定連線，並使用 Evermusic 或 Flacbox 將整個音樂庫串流到 iPhone 或 Mac。無論是在家還是外出，都可以使用 QuickConnect 從任何地方無縫、高品質地存取您喜愛的曲目。充分利用這些應用程式提供的靈活性和便利性，輕鬆管理所有裝置上的音樂收藏。

透過 QuickConnect 的安全遠端存取和對多種音訊格式的支援，您永遠不會遠離音樂。現在，NAS 上儲存的檔案只需輕輕一點！

## FAQ

{{% details title="手動連線和 QuickConnect 有什麼區別？" closed="true" %}}
手動連線使用 NAS IP 位址和連接埠，在本地網路上運作。QuickConnect 使用 Synology 的中繼服務從網際網路上的任何地方建立連線，無需連接埠轉發。
{{% /details %}}

{{% details title="我可以在家庭網路之外從 Synology NAS 串流音樂嗎？" closed="true" %}}
可以。在 Synology NAS 上啟用 QuickConnect，並在 Evermusic 或 Flacbox 中使用 QuickConnect ID，即可從任何有網際網路連線的地方串流音樂。
{{% /details %}}

{{% details title="從 Synology NAS 串流時支援哪些音訊格式？" closed="true" %}}
Evermusic 和 Flacbox 支援 FLAC、MP3、AAC、WAV、ALAC、OGG、WMA、DSD 及許多其他格式。從 Synology NAS 串流時，所有支援的格式均可使用。
{{% /details %}}

{{% details title="連線需要雙重身份驗證嗎？" closed="true" %}}
不需要，2FA 是選用的。但是，如果您在 Synology DSM 上啟用了兩步驟驗證，應用程式將在登入時要求輸入一次性密碼。工作階段過期時需要重新授權。
{{% /details %}}

{{% details title="應該使用 Synology 原生 API、WebDAV 還是 SMB 來連線？" closed="true" %}}
帶有 QuickConnect 的 Synology 原生 API 是遠端存取的最佳選擇。對於本地網路使用，SMB 通常是最快的選項。WebDAV 在本地和遠端存取中都表現良好。Evermusic 和 Flacbox 支援所有三種通訊協定。
{{% /details %}}
