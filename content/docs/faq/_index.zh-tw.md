---
date: '2025-06-12T17:00:00+00:00'
title: '常見問題解答'
description: '尋找關於 Evermusic、Flacbox、Evervideo 和 Evertag 的常見問題解答。探索雲端串流、檔案管理、播放選項、中繼資料編輯等功能。'
keywords: [
  "Evermusic 常見問題", "Flacbox 支援", "Evervideo 幫助", "Evertag 問題",
  "如何使用 Evermusic", "雲端音樂播放器故障排除", "離線播放指南",
  "音訊標籤編輯器支援", "視訊串流問題", "檔案傳輸教學"
]
tags: [
  "常見問題", "幫助", "支援", "evermusic", "flacbox", "evervideo", "evertag",
  "雲端設定", "播放問題", "檔案管理", "中繼資料編輯",
  "故障排除", "離線模式", "音樂播放器", "視訊播放器"
]
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## 學習如何使用我們的應用程式

正在尋找使用我們某款應用程式的答案或協助？您來對地方了。

我們的常見問題頁面將協助您連接雲端儲存、管理音樂和視訊檔案、設定離線播放、調整等化器設定、修復中繼資料等。

在下方瀏覽您的應用程式常見問題以開始，或查閱我們從使用者郵件收到的常見問題和解答。

## 選擇您的應用程式

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="播放 360° 視訊，從 iCloud 串流，帶字幕觀看，應用視訊等化器，用播放清單整理內容，下載視訊供離線觀看。"
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="具有離線模式、音訊等化器、交叉淡入淡出、無縫播放、播放清單管理、完整音樂庫和內建檔案管理器的雲端音樂播放器。"
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="適用於 iPhone 和 Mac 的高解析度音訊播放器。以 FLAC、ALAC、APE 和 DSD 等無損格式聆聽音樂。透過進階音訊設定精細調整輸出。"
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="具有批次編輯功能的智慧音樂標籤編輯器。修復遺失的中繼資料、專輯封面等。編輯 ID3、FLAC、APE 標籤——支援超過 120 個欄位。" 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## 常見問題和解答

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="為什麼我無法在舊版 iOS（15.8.4）上登入 pCloud？" closed="true" %}}
pCloud 的網頁登入頁面可能無法在 15.8.4 等舊版 iOS 上正常顯示，導致無法在雲端連線畫面中輸入電子郵件和密碼。<br><br>

作為解決方法，您可以使用 **WebDAV** 通訊協定，該協定受 pCloud 支援，並在所有 iOS 版本上穩定運作。

**WebDAV 設定：**<br>
- **美國伺服器：** `https://webdav.pcloud.com`  
- **歐洲伺服器：** `https://ewebdav.pcloud.com`  
- **使用者名稱：** 您的 pCloud 電子郵件地址  
- **密碼：** 您的 pCloud 帳戶密碼  

開啟應用程式 → 連線 → 連線到雲端儲存 → 選擇 **WebDAV** → 輸入您的憑證和伺服器 URL。

此方法可讓您連線到 pCloud 儲存空間，並在舊裝置上無障礙存取您的檔案。
{{% /details %}}

{{% details title="如何在 Mac (macOS) 上透過 AirPlay 播放音樂？" closed="true" %}}
macOS 版應用程式不像 iOS 那樣內建 AirPlay、Chromecast 或藍牙連線按鈕。<br><br>

要在 MacBook Pro 上使用 **AirPlay**，請按照以下步驟操作：

1. 前往螢幕**右上角**，開啟**控制中心**（時鐘旁邊）。  
2. 點按**聲音/音量**圖示。  
3. 在下一個畫面中，點按 **AirPlay** 查看所有可用 AirPlay 裝置的清單。  
4. 選擇所需裝置開始播放音樂。  

這將把所有系統音訊（包括來自 Evermusic 或 Flacbox 的音訊）路由到您選擇的 AirPlay 裝置。
{{% /details %}}

{{% details title="為什麼我在 iPhone 上購買的 Premium 沒有在 Mac 上啟動？" closed="true" %}}
終身購買和訂閱透過 **iCloud** 在 iOS 和 Mac 之間同步。<br><br>

要在 Mac 上啟動 Premium：<br>
- 確保兩台裝置上都安裝了最新版本的應用程式<br>
- 在兩台裝置上啟用 **iCloud**<br>
- 在 iOS 裝置上啟動應用程式，等待 1 分鐘讓購買資訊上傳<br>
- 在 Mac 上，使用**相同的 Apple ID** 從 App Store 安裝應用程式<br>
- 啟動應用程式並等待幾秒鐘讓資訊同步<br>
- 或者，在兩台裝置的應用程式設定中點按**恢復購買**<br><br>

您的 Premium 功能將自動在 Mac 上啟動。
{{% /details %}}

{{% details title="如何在裝置之間自動同步播放清單？" closed="true" %}}
目前播放清單**沒有自動同步**功能。<br><br>

您可以使用以下選項之一：<br>
- 從應用程式設定中**備份和還原** [如何在 Evermusic 裝置之間傳輸音樂庫：逐步指南](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **將播放清單匯出為 M3U**，然後在另一台裝置上匯入：<br>
  - [如何匯出播放清單](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [如何匯入播放清單](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **封存播放清單或專輯**並透過 ZIP 傳輸：<br>
  - [播放清單封存指南](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="您的應用程式安全嗎？我可以停用分析功能嗎？" closed="true" %}}
是的，您的隱私是我們的首要任務。<br><br>

- 所有資料——音樂檔案、設定、雲端登入——都儲存在您的裝置上<br>
- 登入憑證安全儲存在 **iOS 鑰匙圈**中<br>
- 我們只收集匿名崩潰和使用報告<br>
- 您可以在**應用程式設定 → 分析**中選擇退出<br><br>

更多資訊：<br>
- [隱私權政策](/legal/privacy-policy/)<br>
- [Apple 鑰匙圈安全性](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

如果使用個人化廣告，Google Mobile Ads 需要顯示同意設定。<br>
Premium 使用者看不到廣告，廣告 SDK 已完全停用。
{{% /details %}}

{{% details title="您的應用程式支援家人共享嗎？" closed="true" %}}
是的，支援家人共享。<br><br>

要共享應用程式內購買：<br>
- 確保購買已設定為與您的家庭群組共享<br>
- 在家庭成員的裝置上，前往**設定 > 購買 > 恢復購買**<br>
- 這將從 Apple 伺服器請求購買資料並在其裝置上啟動
{{% /details %}}

{{% details title="如何加快中繼資料和雲端同步速度？" closed="true" %}}
要提高同步速度，請啟用背景工作：<br><br>

- **設定 → 音樂庫 → 中繼資料讀取 → 在背景讀取中繼資料**<br>
- **設定 → 音樂庫 → 線上音樂同步 → 背景同步**<br><br>

此外，在 macOS 上，透過**設定 → 音樂庫**提高中繼資料讀取速度。<br>
如果播放器處於活動狀態（正在播放音訊），iOS 不會暫停應用程式，從而實現持續同步。
{{% /details %}}

{{% details title="如何取消訂閱？" closed="true" %}}
您可以按照 Apple 的官方說明取消訂閱：<br>
👉 [如何取消訂閱](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="如何連線並從 WD MyCloud EX2 Ultra 串流音訊？" closed="true" %}}

當您透過應用程式中的**連線 > 連線到雲端儲存 > My Cloud Home** 新增連線時，該功能官方設計支援 **WD MyCloud Home** 裝置。<br>
WD MyCloud EX2 Ultra 對應用程式使用受限存取。<br><br>

但是，如果您已成功連線到 **WD MyCloud EX2 Ultra**、**WD MyCloud Mirror** 或其他 **WD MyCloud** 儲存型號，您仍可透過以下解決方法使用它：<br><br>

1. 開啟**連線 → 連線到雲端儲存 → My Cloud Home**<br>
2. 使用內建檔案管理器建立資料夾<br>
3. 將音樂檔案上傳到此資料夾<br>
4. 這些檔案將儲存在僅應用程式可存取的「沙箱」中<br>
5. 您現在可以直接串流或下載它們<br><br>

⚠️ 只有透過應用程式建立的資料夾才能從 NAS 存取。
{{% /details %}}

{{% details title="如何連線到 Koofr.eu？" closed="true" %}}
您可以使用 **WebDAV** 連線 Koofr。<br><br>

- Koofr WebDAV 設定指南：[koofr.eu 部落格](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Evermusic/Flacbox WebDAV 指南：[如何使用 WebDAV 連線 NAS 儲存空間並在 iPhone 或 Mac 上聆聽音樂](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="應用程式的 URL scheme 是什麼？" closed="true" %}}
以下是支援的 scheme：<br><br>

**Evermusic**<br>
- iOS（藍色圖示）：`lsevermusic://`<br>
- macOS：`lsevermusicmac://`<br>
- iOS（紅色圖示）：`lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS：`lsflap://`<br>
- macOS：`lsflapmac://`<br><br>

**Evertag**<br>
- iOS：`lsevertag://`<br>
- macOS：`lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS：`lsevervideo://`<br>
- macOS：`lsevervideomac://`
{{% /details %}}

{{% details title="應用程式在背景時音樂停止播放——如何修復？" closed="true" %}}
如果應用程式在背景崩潰或暫停：<br>
- 前往**設定 > 音樂庫 > 線上音樂同步 > 背景同步 → 停用**<br>
- **設定 > 音樂庫 > 中繼資料讀取 > 在背景讀取中繼資料 → 停用**<br>
- **設定 > 檔案管理器 > 背景傳輸 → 停用**
{{% /details %}}

{{% details title="無縫播放無法運作——如何修復？" closed="true" %}}
無縫播放取決於 iOS 版本和音訊引擎。<br>
嘗試切換音訊引擎：<br>
- 前往**設定 → 音訊播放器 → 一般 → 音訊處理器**<br>
- 選擇 **Core Audio** 以獲得更好的無縫播放支援
{{% /details %}}

{{% details title="為什麼應用程式在清單中只顯示 100 個項目？" closed="true" %}}
應用程式使用分頁以提高效能。<br>
要停用它：<br>
- 前往**設定 → 個人化 → 內容載入限制 → 已停用**<br>
現在所有項目將一次性載入。
{{% /details %}}

{{% details title="為什麼中繼資料中有奇怪的字元？" closed="true" %}}
嘗試啟用中繼資料標準化：<br>
- **設定 → 音樂庫 → 中繼資料讀取 → 標準化中繼資料編碼**
{{% /details %}}

{{% details title="為什麼應用程式無法讀取含有特殊字元的資料夾名稱？" closed="true" %}}
這是 **SMB2 通訊協定**的已知問題。<br><br>

嘗試以下解決方案：<br>
- 在伺服器和應用程式設定中啟用 **SMB1**<br>
- 使用**系統檔案選取器**：<br>
  - 前往**本機檔案 > 此裝置上的檔案 > 開啟檔案...**<br>
  - 使用 Apple 的原生選單選取資料夾/檔案<br><br>

或者，如果您的 NAS 支援，可使用 **WebDAV** 或 **DLNA** 連線。
{{% /details %}}

{{% details title="如何在 iCloud 中上傳和管理音樂？" closed="true" %}}
– **如何將音樂上傳到 iCloud？**  <br>
在瀏覽器中前往 [https://www.icloud.com](https://www.icloud.com)，建立資料夾，然後直接從 Mac 或 PC 上傳音樂檔案。<br>

– **如何管理 iCloud 儲存空間？**  <br>
您有兩個選項：  <br>
1. 在瀏覽器中使用 [https://www.icloud.com](https://www.icloud.com) 整理、上傳或刪除檔案。<br>  
2. 在應用程式中，透過**連線 → 連線到雲端儲存 → iCloud Drive** 連線到 iCloud 後，使用內建檔案管理器直接在 iCloud 儲存空間中上傳、下載、重新命名資料夾或刪除檔案——無需儲存到裝置。<br>

⚠️ 刪除檔案時請小心。應用程式會永久刪除檔案（不會進入垃圾桶，無法還原）。<br>

在此深入了解：[如何從 iCloud Drive 在 iPhone 或 Mac 上串流音樂](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="如何將 10GB 音樂庫從 Windows 11 傳輸到 iPhone 進行離線播放？" closed="true" %}}

您有多種可靠的方式將音樂庫從 Windows 11 PC 移動到 iPhone，並在應用程式中離線使用。選擇最適合您的方法：

1. **使用傳輸線連線（推薦用於大型音樂庫）**  <br>
   在 Windows 11 上使用 **Apple Devices** 應用程式透過 USB 直接將檔案傳輸到 iPhone。  
   請按照 Apple 的指南操作：  
   https://support.apple.com/en-ph/120402 <br>

2. **透過 Wi-Fi Drive 無線傳輸**  <br>
   在應用程式中啟用 **WiFi Drive** 功能，並透過電腦上的瀏覽器上傳音樂。  
   逐步說明：  
   [如何不使用 iTunes 透過 WiFi-Drive 將音樂檔案從電腦傳輸到 iPhone](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **使用 DLNA 伺服器無線傳輸**  <br>
   在 Windows 電腦上開啟 DLNA 媒體伺服器，將音樂庫直接串流或傳輸到應用程式。  
   指南：  
   [如何在 Windows 10 上啟用 DLNA 媒體伺服器並在 iPhone 上播放音樂](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **使用 SMB 檔案共享無線傳輸**  <br>
   在 PC 上啟用 **SMB 檔案共享**，在應用程式中連線後按資料夾瀏覽、下載或傳輸檔案。  
   說明：  
   [使用 SMB 通訊協定將檔案從電腦傳輸到 iPhone](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ 傳輸大型音樂庫（10GB+）時，有線 USB 傳輸通常是最快且最穩定的選項。

{{% /details %}}

</div>
