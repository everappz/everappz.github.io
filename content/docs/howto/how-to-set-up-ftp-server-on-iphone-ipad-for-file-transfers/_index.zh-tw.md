---
title: "如何在 iPhone 和 iPad 上設定 FTP 伺服器來傳輸檔案"
description: "用 Everdisk 把你的 iPhone 或 iPad 變成 FTP 伺服器，透過 Wi-Fi 從 Mac、Windows PC、Linux、Android、像 FileZilla 這樣的 FTP App，或另一支 iPhone 傳輸檔案。完整設定、ftp 位址和連接埠、訪客存取，以及每一種裝置的逐步連線教學。"
date: 2026-09-19
tags: ["everdisk", "ftp", "檔案傳輸", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["iPhone FTP 伺服器", "iPad FTP 伺服器", "如何在 iPhone 設定 FTP", "iphone ftp 伺服器 app", "把 FileZilla 連接到 iPhone", "Cyberduck iPhone FTP", "透過 FTP 傳輸 iPhone 檔案", "ftp iphone 到電腦", "ftp iphone 到 iphone", "從 Windows 連接 iPhone FTP", "iphone ftp 位址連接埠", "匿名 ftp iphone", "從 iphone 分享檔案 ftp", "給相機和 nas 用的 iphone ftp"]
readingTime: 9
---

{{< author-byline >}}

FTP 是檔案傳輸界的老可靠。它已經存在了數十年，而這正是它如此好用的原因：幾乎任何能和伺服器溝通的東西都懂它。相機、智慧電視、路由器、網路磁碟、自動化工具和每一個桌面 FTP App 都會說 FTP。有了 [Everdisk](/products/everdisk)，你可以在 iPhone 或 iPad 上執行一個 FTP 伺服器，讓手機成為那些裝置和 App 可以連上並移動檔案的地方。

當其他選項不合適時就選 FTP，例如某台較舊的裝置，或某個只會透過 FTP 連接的 App。這份指南涵蓋設定，以及如何從 Mac、Windows、FTP App、Linux、Android 和第二支 iPhone 連上。

## 你需要準備什麼

- 一支已安裝 [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) 的 iPhone 或 iPad。
- 一台在**同一個 Wi-Fi 網路**上的電腦、App 或裝置。
- 你想分享的檔案，放在 Everdisk 的「文件」資料夾或你加入的資料夾裡。

## 在 Everdisk 裡設定 FTP 伺服器

### 步驟 1：選擇要分享什麼並設定存取權

打開 Everdisk，前往「共享」分頁，點一下「分享什麼」。「文件」資料夾預設就會分享。用「加入檔案夾」和「加入檔案」加入更多。

打開「設定」，接著「共享」，接著「存取權」。如果你想讓別人上傳、重新命名和刪除，就把「檔案編輯」開啟；想只允許下載就關閉。如果你想要登入，就設定「登入名稱」和「密碼」，或留空讓任何人都能以訪客身分連接。

### 步驟 2：開啟 FTP 伺服器

前往「設定」，接著「共享」，接著「連線」，然後開啟「其他應用程式和裝置」。那就是 FTP 伺服器（它帶有 FTP 標籤）。

### 步驟 3：開始分享並記下位址

回到「共享」分頁並點一下「開始」。「如何連線」這一區會顯示 FTP 位址。它看起來像這樣：

```
ftp://192.168.1.20:2121
```

冒號後面的數字是**連接埠**，預設是 **2121**。第一部分是你 iPhone 在 Wi-Fi 上的位址，所以你的會不一樣。裝置連著的時候，請讓 Everdisk 保持開在畫面上。

## 從 Mac 連接

1. 打開 **Finder**，選擇「前往」，接著「連接伺服器」（或按 **Command 加 K**）。
2. 輸入 Everdisk 裡顯示的 FTP 位址，例如 `ftp://192.168.1.20:2121`。
3. 點一下「連接」，然後選擇「訪客」或輸入你的「登入名稱」和「密碼」。

Finder 會掛載這個 FTP 共享，讓你可以瀏覽並把檔案複製到你的 Mac。請注意 Finder 是以唯讀方式打開 FTP。當你想從 Mac 上傳時，請用下面說明的 FTP App。

## 從 Windows 連接

1. 打開**檔案總管**，點一下頂端的位址列。
2. 輸入 Everdisk 裡的 FTP 位址，例如 `ftp://192.168.1.20:2121`，然後按 **Enter**。
3. 如果你有設定，就輸入你的「登入名稱」和「密碼」，或以訪客身分繼續。

共享的檔案會出現在視窗裡，你可以把它們複製到你的 PC。

## 用 FTP App 連接（FileZilla、Cyberduck）

若要上傳並完整掌控，FTP App 是最好的工具。**FileZilla** 和 **Cyberduck** 都是免費的，在 Windows、Mac 和 Linux 上都能執行。

1. 打開 App 並建立一個新連線。
2. 把 **Host** 設為你 iPhone 的 Wi-Fi 位址，**Port** 設為 **2121**。
3. 登入方面，輸入你的「登入名稱」和「密碼」，或如果你沒有設定就選擇 **Anonymous**。
4. 連接，然後雙向拖放檔案（上傳需要「檔案編輯」開啟）。

## 從 Linux 連接

1. 打開你的檔案管理程式，選擇「連接伺服器」或「其他位置」。
2. 輸入位址，例如 `ftp://192.168.1.20:2121`。
3. 以訪客身分或用你的登入資訊連接。

你也可以從終端機用任何 Linux FTP 用戶端，把它指向同樣的主機和連接埠 2121。

## 從 Android 連接

Android 沒有系統內建的 FTP 瀏覽器，所以要用一個 App：

1. 安裝像 **AndFTP**、**FTPCafe** 這樣的 FTP 用戶端，或像 **Solid Explorer** 這樣支援 FTP 的檔案管理程式。
2. 加入一個連線，填入主機、**連接埠 2121**，以及你的登入資訊或 Anonymous。
3. 瀏覽並傳輸。

## 從另一支 iPhone 或 iPad 連接

iOS 的「檔案」App 不含 FTP 用戶端，所以在第二台裝置上用以下其中一種：

- **Everdisk 自己的「裝置」分頁。** 打開 Everdisk，前往「裝置」，點一下「新增連線」，選擇「FTP」，然後輸入位址，例如 `ftp://192.168.1.20:2121`。這是最簡單的做法。
- **一個專用的 iOS FTP App**，使用同樣的主機、連接埠 2121 和登入資訊。

## 連接其他裝置：相機、電視、路由器和 NAS

這正是 FTP 大放異彩的地方。許多裝置都有內建的 FTP 用戶端，可以傳送或抓取檔案：

- **透過 FTP 上傳相片的相機**可以把它們直接送到你的 iPhone。
- **支援 FTP 的智慧電視、路由器、NAS 機盒和自動化工具**都能用同樣的方式連接。

把它們指向你 iPhone 的 Wi-Fi 位址、連接埠 **2121**，以及你的登入資訊（或 Anonymous），使用 Everdisk 裡顯示的位址。

## 唯讀還是可讀寫

「設定」、「共享」、「存取權」裡的「檔案編輯」開關會控制這一點。開啟時讓別人上傳、重新命名和刪除。關閉時表示他們只能下載。當你要把檔案交出去，而不想手機上的任何東西被更動時，就選擇唯讀。

## 大家實際上怎麼用

- **把 FileZilla 連接到你的 iPhone**，一次把一批檔案推送到手機上。
- **讓某個只會說 FTP 的老舊 App 或裝置**在其他方法都連不上時，能連到你的檔案。
- **接收來自相機的相片**，透過 FTP 上傳。
- **在 iPhone 和 iPad 之間移動檔案**，用接收端裝置上 Everdisk 的「裝置」分頁。

## 一些小提示

- 裝置連著的時候讓 Everdisk 保持開著，因為 iOS 過一陣子會暫停背景 App。
- 若要從 Mac 上傳，請用 FileZilla 或 Cyberduck 而不是 Finder，因為 Finder 是以唯讀方式打開 FTP。
- 想要最廣泛的相容性，就把登入留空，然後以 Anonymous 連接，大多數 FTP 用戶端都提供這個選項。
- FTP 不會加密它的流量。在你不信任的網路上，改用[有加密的 SMB 伺服器](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)。

## 常見問題

{{% details title="我 iPhone 的 FTP 位址和連接埠是什麼？" closed="true" %}}
在你開始分享後，Everdisk 會在「共享」畫面上顯示位址。它看起來像 ftp://192.168.1.20:2121。2121 是 Everdisk 用於 FTP 的連接埠，第一部分是你 iPhone 在 Wi-Fi 上的位址，所以你的會不一樣。
{{% /details %}}

{{% details title="我要怎麼把 FileZilla 或 Cyberduck 連接到我的 iPhone？" closed="true" %}}
打開 App 並建立一個新連線。把 Host 設為你 iPhone 的 Wi-Fi 位址，Port 設為 2121。輸入你的「登入名稱」和「密碼」，或如果你在 Everdisk 裡沒有設定就選擇 Anonymous。連接後，當「檔案編輯」開啟時你就能雙向拖放檔案。
{{% /details %}}

{{% details title="我可以從 Windows 連上我 iPhone 的 FTP 嗎？" closed="true" %}}
可以。打開檔案總管，點一下位址列，輸入 Everdisk 裡的 FTP 位址（例如 ftp://192.168.1.20:2121），然後按 Enter。如果你有設定就輸入你的登入資訊，或以訪客身分繼續。若要上傳並有更多掌控，請改用像 FileZilla 這樣的 FTP App。
{{% /details %}}

{{% details title="我需要 FTP 的登入嗎？" closed="true" %}}
不需要，登入是選用的。在「設定」、「共享」、「存取權」裡把「登入名稱」和「密碼」留空，然後以 Anonymous 連接，大多數 FTP 用戶端都提供這個選項。如果你想要連線先登入，就設定一組登入資訊。
{{% /details %}}

{{% details title="為什麼我在 FTP 上只能下載而不能上傳？" closed="true" %}}
有兩個常見原因。首先，「設定」、「共享」、「存取權」裡的「檔案編輯」開關必須開啟，才能允許上傳、重新命名和刪除。其次，Mac Finder 是以唯讀方式打開 FTP，所以當你想上傳時，請用像 FileZilla 或 Cyberduck 這樣的 FTP App。
{{% /details %}}

{{% details title="我可以在兩支 iPhone 之間用 FTP 嗎？" closed="true" %}}
可以。在第一支 iPhone 上開始 FTP 伺服器。在第二支上，打開 Everdisk，前往「裝置」分頁，點一下「新增連線」，選擇「FTP」，然後輸入第一支手機上顯示的位址。專用的 iOS FTP App 也可以，因為 iOS 的「檔案」App 不含 FTP 用戶端。
{{% /details %}}

{{% details title="FTP 安全嗎？" closed="true" %}}
純 FTP 不會加密它的流量，所以把它當成給你信任的網路（例如你家的 Wi-Fi）用的工具。在你無法掌控的網路上，改用開啟「要求 SMB 加密」的 SMB 伺服器，它會保護每一次傳輸。
{{% /details %}}

{{% details title="哪些裝置可以透過 FTP 連接？" closed="true" %}}
幾乎任何有 FTP 用戶端的東西都可以。這包括 Mac、Windows 和 Linux 電腦、像 FileZilla 和 Cyberduck 這樣的 FTP App、Android 檔案管理程式，以及相機、智慧電視、路由器、NAS 機盒和自動化工具等硬體。那種廣泛的觸及範圍正是選擇 FTP 的主要原因。
{{% /details %}}

{{% details title="我的 FTP 連線為什麼中斷了？" closed="true" %}}
你的 iPhone 是伺服器，而 iOS 會暫停在背景待太久的 App。裝置連著的時候，請讓 Everdisk 保持開在畫面上，並在長時間傳輸時接上電源。也要確認兩台裝置仍在同一個 Wi-Fi 上。
{{% /details %}}

{{% details title="Everdisk 是免費的嗎？" closed="true" %}}
是的，Everdisk 免費下載，而且內含 FTP 伺服器。選購的一次性 Premium 購買會加入一些額外功能，例如自訂連接埠以及相片和影片轉換。你不用付費就能設定 FTP 並傳輸檔案。
{{% /details %}}

準備好試試看了嗎？[從 App Store 下載 Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)，幾分鐘內就能連上你的第一個 FTP 用戶端。有問題或建議嗎？寄信給我們：**support@everappz.com**。
