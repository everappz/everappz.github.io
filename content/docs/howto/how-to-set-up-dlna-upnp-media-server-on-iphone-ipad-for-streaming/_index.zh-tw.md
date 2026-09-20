---
title: "如何在 iPhone 和 iPad 上設定 DLNA/UPnP 媒體伺服器來串流"
description: "用 Everdisk 把你的 iPhone 或 iPad 變成 DLNA/UPnP 媒體伺服器，透過 Wi-Fi 把相片、影片和音樂串流到智慧電視、遊戲主機、VLC 或 Kodi。完整設定，並教你如何從 Samsung、LG、Sony 電視、Windows、Mac、Linux、Android 和另一支 iPhone 連上。"
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "媒體伺服器", "串流", "智慧電視", "iphone", "ipad", "wifi"]
keywords: ["iPhone DLNA 伺服器", "iPad UPnP 伺服器", "如何在 iPhone 設定 DLNA", "從 iPhone 串流到智慧電視", "iOS DLNA 媒體伺服器", "不用線材把影片串流到電視", "在電視上播放 iPhone 相片", "Samsung 電視 DLNA iPhone", "LG 電視 DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA 媒體伺服器", "iOS UPnP AV 媒體伺服器", "從 iPhone 把音樂串流到電視", "iPhone 媒體伺服器 App"]
readingTime: 9
---

{{< author-byline >}}

DLNA（也叫 UPnP AV）是大多數智慧電視背後那位默默工作的功臣。它是一種共通語言，讓電視或媒體播放器找到同一個 Wi-Fi 上的媒體庫並從中播放，電視上完全不必安裝任何東西。只要你的 iPhone 或 iPad 能扮演那個媒體庫，你的相片、影片和音樂就會自己出現在大螢幕上。

這份指南會教你如何用 [Everdisk](/products/everdisk) 把你的 iPhone 或 iPad 變成 DLNA/UPnP 媒體伺服器，以及如何從智慧電視、遊戲主機、VLC、Kodi、電腦、Android 手機，甚至第二支 iPhone 打開那個媒體庫。所有內容都透過你的本機 Wi-Fi 執行，不會上傳到任何地方。

## 你需要準備什麼

- 一支已安裝 [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) 的 iPhone 或 iPad。
- 一台和你的裝置在**同一個 Wi-Fi 網路**上的電視、播放器或電腦。
- 你想播放的相片、影片或音樂，並已經存在你的 iPhone 上（在「照片」App、「音樂」App，或 Everdisk 的「文件」資料夾裡）。

## 在 Everdisk 裡設定 DLNA 伺服器

### 步驟 1：選擇要分享什麼

打開 Everdisk，前往「共享」分頁。點一下「分享什麼」，挑選你的內容：

- 開啟「允許存取整個照片圖庫」來分享每一本相簿，或點一下「加入照片」來挑選幾張。
- 開啟「允許存取整個音樂資料庫」來分享你的歌曲，或點一下「加入歌曲」來挑選一部分。
- 用「加入檔案夾」和「加入檔案」加入任何資料夾或檔案。App 自己的「文件」資料夾預設就會分享。

在能開始分享之前，你至少要選取一個項目。

### 步驟 2：開啟「電視與媒體中心」（DLNA）

前往「設定」，接著「共享」，接著「連線」。確認「電視與媒體中心」是開啟的。它預設就是開啟的，並帶有 DLNA 標籤。這就是電視和播放器會去尋找的伺服器。

### 步驟 3：開始分享

回到「共享」分頁，點一下大大的「開始」按鈕。你的裝置現在就是你 Wi-Fi 上的媒體伺服器了。它會以易記的名稱出現在其他裝置上，也就是 App 裡顯示的裝置名稱（在你改名之前，可能是類似「Speedy-Hare」之類的名字）。

DLNA 串流永遠是開放的，所以電視上不需要輸入密碼。觀看時請讓 Everdisk 保持開在畫面上，因為 iOS 會暫停被完全推到背景的 App。

## 在智慧電視上播放

這是最常見的情況，通常只要大約三十秒。

1. 把電視接上和你 iPhone **同一個 Wi-Fi**。
2. 打開電視內建的媒體播放器。名稱因品牌而異：**Media Player**、**Gallery**、**SmartShare**（LG）、**AllShare** 或 **SmartThings**（Samsung）、**Content Share** 或 **SimplyShare**。
3. 找到媒體伺服器或來源的清單。你的裝置會以它的名稱出現在那裡。
4. 選取它，瀏覽進你的相片、影片或音樂，然後按播放。

預覽縮圖會自動顯示，所以你可以找到正確的假期相簿或電影，不必用猜的。

### 哪些電視可以用

大多數 **Samsung、LG、Sony BRAVIA、Panasonic（VIERA 韌體）、Philips 和 Hisense** 的電視都內建 DLNA，可以立刻使用。**PlayStation 和 Xbox 主機以及大多數 AV 擴大機**也可以。

有少數平台沒有內建：**Roku 電視、Amazon Fire TV、Vizio SmartCast，以及沒有廠商媒體 App 的原生 Google TV**。如果你的電視是這幾款，而且找不到你的裝置，通常就是這個原因。在那些電視上，請安裝像 VLC 或 Kodi 這類 DLNA 播放器 App，或改用[ WebDAV 設定指南](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/)透過網頁瀏覽器存取你的檔案。

有些品牌即使移除了官方的 DLNA 標誌，DLNA 其實還能用，所以如果看起來像是沒有這個功能，請找一找上面列出的那些媒體播放器名稱。

## 在 Windows、Mac 和 Linux 上用 VLC 或 Kodi 播放

VLC 和 Kodi 都是免費的，在每一種桌面系統上都能執行，而且很懂 DLNA。它們是在電腦上打開你 Everdisk 媒體庫最可靠的方式。

**VLC（Windows、Mac、Linux）：**

1. 打開 VLC。
2. 顯示播放清單（在 Windows 和 Linux 上按 **Ctrl+L**，在 Mac 上從「顯示方式」選單打開**播放清單**）。
3. 在側邊欄裡，於「本地網路」底下打開 **Universal Plug'n'Play**。
4. 你的裝置會出現在清單裡。點進去並挑選一個檔案。

**Kodi（Windows、Mac、Linux）：**

1. 前往**影片**、**音樂**或**圖片**，接著**檔案**，接著**加入來源**（或**瀏覽**）。
2. 選擇 **UPnP devices**。
3. 選取你的裝置並瀏覽你的媒體庫。

在 Windows 上，你也可以打開 **Windows Media Player**，在側邊欄展開 **Other Libraries**，你的裝置就會出現在那裡。

## 在 Android 上播放

Android 手機和平板沒有系統內建的 DLNA 瀏覽器，所以要用 App：

- **VLC for Android**：打開側邊選單，點一下 **Local Network**，你的裝置就會出現在 UPnP 伺服器底下。
- **BubbleUPnP** 或類似的 UPnP App：你的裝置會出現在伺服器清單裡，這類 App 還能把播放推送到電視。

## 在另一支 iPhone 或 iPad 上播放

兩台裝置，一個媒體庫。假設相片在你的 iPhone 上，而你想在 iPad 上觀看。

- 最簡單的做法是用第二台裝置上 Everdisk 自己的「裝置」分頁。它既是 DLNA 用戶端也是伺服器。在 iPad 上打開 Everdisk，前往「裝置」，你的 iPhone 就會出現在「可用裝置」底下。點一下它就能瀏覽和播放。
- 任何 iOS 上的 DLNA 播放器 App 也可以，例如 VLC 或某個 UPnP 瀏覽器。打開它的本地網路檢視，然後挑選你的 iPhone。

## 在遊戲主機上播放

- **PlayStation 5 和 4**：打開 **Media** App（媒體庫），你的裝置就會以可瀏覽的媒體伺服器出現。
- **Xbox**：使用支援 DLNA 的媒體播放器 App，然後從伺服器清單裡挑選你的裝置。

## 如果你的裝置沒有出現在清單裡

有些播放器讓你用位址手動加入媒體伺服器，而不用等它被自動探索到。在 Everdisk 的「共享」畫面上，DLNA 卡片會顯示一個以 `/device-desc.xml` 結尾的裝置描述位址。把那個位址輸入到播放器的加入伺服器欄位裡。

如果還是沒有出現，請檢查三件事：兩台裝置都在同一個 Wi-Fi 上（不是封鎖裝置對裝置流量的訪客網路）、Everdisk 有開著而且已開始分享，以及「設定」裡的「電視與媒體中心」是開啟的。

## 如果影片無法播放

DLNA 會把檔案原封不動地交給電視，而電視必須有能力解碼它。如果某段影片無法播放，通常是那台電視不支援它的格式。有兩種解法：

- 打開「設定」，接著「共享」，接著「影片」，然後把「品質」調低。Everdisk 就會在串流時把影片轉換成更相容的格式。（轉換是 Premium 功能。）
- 或是用 Everdisk 的瀏覽器連結在網頁瀏覽器裡打開同一個檔案，它對格式比較寬容。

## 大家實際上怎麼用

- **家庭電影之夜。** 用手機拍的影片，不用線材也不用 Apple TV，就能在客廳電視上播放。
- **在大螢幕上看假期相片。** 在電視上打開你的「照片」圖庫，和滿屋子的人一起滑過整趟旅程。
- **派對背景音樂。** 讓 DLNA 喇叭或 AV 擴大機對準你的「音樂」庫，讓它一直播下去。
- **在飯店電視上觀看**，只要兩台裝置都連上房間的 Wi-Fi，而電視有媒體播放器就行。

## 一些小提示

- 串流時讓 Everdisk 保持開著。如果你把手機鎖住很久，iOS 可能會暫停 App，播放就會停止。
- 長時間看電影時，把手機接上電源。
- 想要最快的串流，就把「設定」裡的「格式」和「品質」保持在「原始」，只有在某台特定電視處理某個檔案有困難時才調低。
- DLNA 只用於串流。電視那一端的任何人都無法更改或刪除你的檔案。若要雙向傳輸檔案，請改用 [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)、[WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) 或 [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) 伺服器。

## 常見問題

{{% details title="DLNA 和 UPnP 有什麼差別？" closed="true" %}}
它們關係非常密切。UPnP 是底層的網路標準，而 DLNA 是建立在它之上、供電視和播放器用來分享和播放相片、影片和音樂的媒體設定檔。在日常使用上，這兩個詞可以互換。當你在 Everdisk 裡開啟「電視與媒體中心」時，你的裝置就成為任何 DLNA 用戶端都能瀏覽的 DLNA/UPnP 媒體伺服器。
{{% /details %}}

{{% details title="我需要在電視上安裝任何東西嗎？" closed="true" %}}
不用。如果你的電視支援 DLNA，它已經有一個能在 Wi-Fi 上找到你裝置的媒體播放器。你只需要在存放內容的那支 iPhone 或 iPad 上安裝 Everdisk。如果你的電視不支援 DLNA，就在連接它的裝置上安裝像 VLC 或 Kodi 這樣的播放器。
{{% /details %}}

{{% details title="為什麼我的 iPhone 沒有出現在電視上？" closed="true" %}}
請檢查兩台裝置是否在同一個 Wi-Fi 網路上。訪客網路以及某些辦公室或飯店網路會阻止裝置彼此看見對方，這會讓 DLNA 無法運作。接著確認 Everdisk 有開著而且已開始分享，以及在「設定」、「共享」、「連線」裡「電視與媒體中心」是開啟的。如果電視還是找不到它，請用那個以 /device-desc.xml 結尾的裝置描述位址手動加入伺服器。
{{% /details %}}

{{% details title="DLNA 串流需要密碼嗎？" closed="true" %}}
不需要。DLNA 在開啟時，永遠對同一個 Wi-Fi 上的任何人開放，這就是為什麼電視那一端不用登入。在你信任的家庭網路上這沒問題。在你不信任的網路上，用完後就把「電視與媒體中心」關掉，或改用有加密的 SMB 伺服器。
{{% /details %}}

{{% details title="我可以串流到 Chromecast 或 Roku 嗎？" closed="true" %}}
Chromecast 和 Roku 開箱狀態下不會扮演 DLNA 播放器，所以它們不會直接找到你的裝置。變通做法是安裝一個能投放的 DLNA App，例如手機上的 VLC 或 BubbleUPnP，再從那裡把播放推送到 Chromecast 或 Roku。在大多數其他智慧電視上，DLNA 不用這些就能運作。
{{% /details %}}

{{% details title="影片播放時沒有聲音或無法打開，我該怎麼辦？" closed="true" %}}
那是電視無法解碼的格式。在 Everdisk 裡打開「設定」、「共享」、「影片」，把「品質」調低，讓 App 在串流時把影片轉換成更相容的格式。你也可以透過瀏覽器連結打開同一個檔案，它能處理更多格式。
{{% /details %}}

{{% details title="我可以只串流音樂，而不是影片嗎？" closed="true" %}}
可以。開啟「允許存取整個音樂資料庫」，或加入特定的歌曲，然後開始分享。你的歌曲就會出現在任何 DLNA 喇叭、AV 擴大機或電視上，並附有封面和曲目資訊。音樂永遠以原始品質分享。
{{% /details %}}

{{% details title="我觀看時 App 必須一直開著嗎？" closed="true" %}}
是的。你的 iPhone 是在扮演伺服器，而 iOS 會暫停被完全推到背景太久的 App。串流時請讓 Everdisk 保持開在畫面上，長時間播放時把手機接上電源。
{{% /details %}}

{{% details title="我要怎麼從一支 iPhone 串流到另一台 iPad？" closed="true" %}}
在 iPhone 上開始分享，然後在 iPad 上打開 Everdisk，前往「裝置」分頁。那支 iPhone 會以媒體伺服器的身分出現在「可用裝置」底下。點一下它就能瀏覽和播放。Everdisk 既是 DLNA 用戶端也是伺服器，所以你不需要另外的 App。
{{% /details %}}

{{% details title="Everdisk 是免費的嗎？" closed="true" %}}
是的，Everdisk 免費下載，而且內含 DLNA 媒體伺服器。選購的一次性 Premium 終身版會加入一些額外功能，例如給較舊電視的相片和影片轉換、自訂連接埠等等。你不用付費就能設定並使用 DLNA 串流。
{{% /details %}}

準備好試試看了嗎？[從 App Store 下載 Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)，幾分鐘內就把你的第一張專輯串流到電視上。有問題或建議嗎？寄信給我們：**support@everappz.com**。
