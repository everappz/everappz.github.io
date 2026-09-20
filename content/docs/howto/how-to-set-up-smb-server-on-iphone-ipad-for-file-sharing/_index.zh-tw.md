---
title: "如何在 iPhone 和 iPad 上設定 SMB 伺服器來分享檔案"
description: "用 Everdisk 把你的 iPhone 或 iPad 變成 SMB 檔案伺服器，透過 Wi-Fi 從 Mac、另一支 iPhone、Linux 或 Android 像網路磁碟一樣打開它。完整設定、smb 位址和連接埠、選用的 SMB3 加密，以及每一種裝置的逐步連線教學。"
date: 2026-09-19
tags: ["everdisk", "smb", "檔案分享", "網路磁碟", "iphone", "ipad", "mac", "finder", "加密", "wifi"]
keywords: ["iPhone SMB 伺服器", "iPad SMB 伺服器", "如何在 iPhone 設定 SMB", "iPhone SMB 共享", "從 Mac Finder 連接 iPhone SMB", "iphone 到 iphone smb", "iOS 檔案 App 連接 SMB 伺服器", "從 iPhone 分享檔案 SMB", "iphone 網路磁碟 Finder", "iOS SMB3 加密", "iPhone Android smb 共享", "從 Linux 連接 SMB", "iphone 當網路磁碟", "透過 wifi 在 iphone 間分享檔案", "把 iphone 對應成網路磁碟"]
readingTime: 10
---

{{< author-byline >}}

SMB 是 macOS、Windows 和 Linux，以及幾乎每一台網路磁碟（NAS）內建的檔案分享方式。當你連上另一台電腦上的共享資料夾，而它在 Finder 或檔案總管裡像一般磁碟一樣打開時，那就是 SMB 在做的工作。有了 [Everdisk](/products/everdisk)，你可以在 iPhone 或 iPad 上放一個 SMB 共享，讓手機本身以網路磁碟的形式出現，供其他裝置瀏覽、從中複製，以及複製檔案進去。

當你想讓 iPhone 表現得像一個真正的磁碟，而不是一個網頁時，這就是該選的選項。它速度快，可以雙向拖放，而且它是 Everdisk 裡唯一能加密每一次傳輸的連線類型。這份指南涵蓋設定，以及如何從 Mac、另一支 iPhone 或 iPad、Linux、Android 和 Windows 連上。

## 你需要準備什麼

- 一支已安裝 [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) 的 iPhone 或 iPad。
- 另一台在**同一個 Wi-Fi 網路**上的裝置。
- 你想分享的檔案，放在 Everdisk 的「文件」資料夾或你加入的資料夾裡。

## 在 Everdisk 裡設定 SMB 伺服器

### 步驟 1：挑選要分享什麼，以及誰可以寫入

打開 Everdisk，前往「共享」分頁，點一下「分享什麼」。「文件」資料夾預設就會分享。用「加入檔案夾」和「加入檔案」加入更多，如果你也想提供照片或音樂庫，就把它們開啟。

決定其他裝置是只能讀取你的檔案，還是也能更改它們。打開「設定」，接著「共享」，接著「存取權」，然後設定「檔案編輯」。開啟時，連接的裝置可以把檔案複製到你的手機上，並重新命名或刪除。關閉時，這個共享就是唯讀的。

如果你想要登入，就在同一個「存取權」畫面上設定「登入名稱」和「密碼」。兩者都留空就會允許訪客存取。

### 步驟 2：開啟 SMB 伺服器

前往「設定」，接著「共享」，接著「連線」，然後開啟「電腦（進階）」。那就是 SMB 伺服器（它帶有 SMB 標籤）。

### 步驟 3：開始分享並記下位址

回到「共享」分頁並點一下「開始」。「如何連線」這一區現在會顯示 SMB 位址。它看起來像這樣：

```
smb://192.168.1.20:4455/Share
```

關於那個位址，有三件事要知道：

- 冒號後面的數字是**連接埠**。Everdisk 預設使用 **4455**。
- 共享的名稱是 **Share**。
- 第一部分是你 iPhone 在 Wi-Fi 上的位址，所以在你的網路上會不一樣。

裝置連著的時候請讓 Everdisk 保持開著，因為 iOS 會暫停在背景待太久的 App。

## 從 Mac 連接

這是最順的情況，因為 macOS 原生就會說 SMB。

最快的方式：打開 **Finder**，在側邊欄的「位置」或「網路」底下找。Everdisk 會在 Wi-Fi 上宣告自己，所以你的 iPhone 常常會自己出現在那裡。點它一下，然後點「連接身分」並選擇「訪客」，或輸入你的登入資訊。

手動連接：

1. 在 Finder 裡，選擇「前往」，接著「連接伺服器」（或按 **Command 加 K**）。
2. 輸入 Everdisk 裡顯示的 SMB 位址，例如 `smb://192.168.1.20:4455/Share`。
3. 點一下「連接」，然後挑選「訪客」或輸入你的「登入名稱」和「密碼」。

你的 iPhone 會在一個 Finder 視窗裡打開。像操作其他磁碟一樣拖放，就能把檔案複製進來或複製出去（前提是「檔案編輯」有開）。

## 從另一支 iPhone 或 iPad 連接

iOS 和 iPadOS 可以在內建的「檔案」App 裡打開 SMB 共享，讓手機對手機的傳輸乾淨又快速。

在第二台裝置上：

1. 打開「檔案」App。
2. 點一下「更多」按鈕（那三個點，在 iPhone 上位於右上角）並選擇「連接伺服器」。
3. 輸入 Everdisk 裡的 SMB 位址，例如 `smb://192.168.1.20:4455/Share`。
4. 選擇「訪客」，或選「註冊使用者」並輸入你的登入資訊。
5. 這個共享會出現在「檔案」的「位置」底下。瀏覽並雙向複製。

你也可以用第二台裝置上 Everdisk 自己的「裝置」分頁，它內含一個 SMB 用戶端。打開 Everdisk，前往「裝置」，點一下「新增連線」，選擇「SMB」，然後輸入位址。

## 從 Linux 連接

1. 打開你的檔案管理程式（GNOME 上的 Files/Nautilus、KDE 上的 Dolphin）。
2. 選擇「其他位置」或「連接伺服器」。
3. 輸入位址，例如 `smb://192.168.1.20:4455/Share`。
4. 以訪客身分連接，或輸入你的登入資訊。

從終端機你也可以執行 `smbclient //192.168.1.20/Share -p 4455`，並在被詢問時輸入你的登入資訊。

## 從 Android 連接

Android 沒有系統內建的 SMB 瀏覽器，所以要用一個支援 SMB 的檔案管理程式：

1. 安裝像 **CX File Explorer**、**Solid Explorer** 或 **X-plore File Manager** 這樣的 App。
2. 加入一個新的 **SMB** 或 **LAN** 連線。
3. 輸入主機（你 iPhone 的 Wi-Fi 位址），把**連接埠設為 4455**，共享名稱設為 **Share**。
4. 以訪客身分或用你的登入資訊連接，然後瀏覽和複製。

## 從 Windows 連接

Windows 可以讀取 SMB 共享，但有一個值得先知道的地方。內建的檔案總管只會透過標準連接埠與 SMB 溝通，而且不允許你在路徑裡輸入自訂連接埠，而 Everdisk 使用連接埠 4455。所以單純的「對應網路磁碟機」這條路通常連不上。

在 Windows 上你有兩個好選擇：

- 使用一個能設定自訂連接埠的檔案管理程式或 SMB 用戶端，把它指向你 iPhone 的位址，連接埠 **4455**，共享名稱 **Share**。
- 或改用 Everdisk 的其他伺服器從 Windows 連接。[WebDAV 設定](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/)和 [FTP 設定](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/)都能從 Windows 檔案總管順利運作，而瀏覽器連結在任何瀏覽器裡都行。

如果你確實想試試「對應網路磁碟機」：打開**檔案總管**，右鍵點一下**本機**，選擇**對應網路磁碟機**，然後輸入 Everdisk 裡顯示的主機和共享名稱。如果連不上，那就是上面說的連接埠限制，所以請改用 WebDAV 或 FTP。

## 為不信任的 Wi-Fi 開啟加密

SMB 是 Everdisk 裡唯一能加密每一次傳輸的連線，這在你無法完全掌控的 Wi-Fi 上很重要，例如咖啡店或辦公室網路。

1. 在「設定」、「共享」、「存取權」裡，設定「登入名稱」和「密碼」。加密的連線不能匿名，所以這一步是必要的。
2. 在「設定」、「共享」裡，開啟「要求 SMB 加密」。
3. 停止並重新開始分享，讓變更生效。

之後每一次 SMB 傳輸都會用 **SMB3 加密 (AES)** 保護。連接的裝置需要支援 SMB3，新型 Mac 上的 Finder 和 Windows 10 以上版本都支援。SMB 加密是一次性 Premium 購買的一部分。

## 唯讀還是可讀寫

「設定」、「共享」、「存取權」裡的「檔案編輯」開關會控制每一個伺服器（包括 SMB）的這項行為。開啟時，連接的裝置可以上傳、重新命名和刪除。關閉時，它們只能瀏覽並把檔案從你的手機複製出去。當你要把檔案交給某個你不希望更動任何東西的人時，就選擇唯讀。

## 大家實際上怎麼用

- **從 Mac 把一個大資料夾移到你的 iPhone 上**，只要把它拖進 Finder 視窗，比網頁上傳快。
- **把一天的相片和影片從你的手機拉到**筆電上，不用 iTunes 也不用線材。
- **在兩支 iPhone 之間傳檔案**，透過「檔案」App，兩端都不用第三個 App。
- **就地處理檔案**，直接從手機在你 Mac 上的某個 App 裡打開文件，再存回去。

## 一些小提示

- 裝置連著的時候讓 Everdisk 保持開著。把手機鎖住很久可能會暫停 App 並中斷連線。
- 如果 Mac 在 Finder 側邊欄裡看不到手機，就用「連接伺服器」搭配完整的 smb 位址手動連接。
- 想在大量傳輸時獲得最佳速度，就把「設定」裡的相片和影片品質保持在「原始」。
- 在不信任的網路上，開啟「要求 SMB 加密」，並在你工作時把其他伺服器關掉。

## 常見問題

{{% details title="我 iPhone 的 SMB 位址和連接埠是什麼？" closed="true" %}}
在你開始分享後，Everdisk 會在「共享」畫面上顯示位址。它看起來像 smb://192.168.1.20:4455/Share。4455 是 Everdisk 用於 SMB 的連接埠，Share 是共享資料夾的名稱。第一部分是你 iPhone 在 Wi-Fi 上的位址，所以你的會不一樣。
{{% /details %}}

{{% details title="我可以從 Windows 連上我 iPhone 的 SMB 共享嗎？" closed="true" %}}
Windows 檔案總管只會透過標準連接埠連接 SMB，而且不接受路徑裡的自訂連接埠，而 Everdisk 使用連接埠 4455。所以單純的「對應網路磁碟機」這條路通常連不上。請使用能設定自訂連接埠的檔案管理程式，或改用 WebDAV、FTP 或瀏覽器連結從 Windows 連接。那些方式從 Windows 都不會有連接埠問題。
{{% /details %}}

{{% details title="我要怎麼用 SMB 在兩支 iPhone 之間分享檔案？" closed="true" %}}
在第一支 iPhone 上用 Everdisk 開始 SMB 伺服器。在第二支 iPhone 上，打開「檔案」App，點一下「更多」按鈕，選擇「連接伺服器」，然後輸入 Everdisk 裡顯示的 smb 位址（例如 smb://192.168.1.20:4455/Share）。以訪客身分或用你的登入資訊連接，這個共享就會出現在「檔案」裡。你也可以用第二支手機上 Everdisk 自己的「裝置」分頁。
{{% /details %}}

{{% details title="我的 iPhone 會自動出現在 Mac 的 Finder 側邊欄嗎？" closed="true" %}}
通常會。Everdisk 會在你的 Wi-Fi 上宣告 SMB 共享，所以你的 iPhone 常常會出現在 Finder 側邊欄的「位置」或「網路」底下。點它一下並選擇「連接身分」，然後選「訪客」或你的登入資訊。如果它沒有出現，就用「前往」、「連接伺服器」搭配完整的 smb 位址手動連接。
{{% /details %}}

{{% details title="我需要密碼才能用 SMB 嗎？" closed="true" %}}
不需要，登入是選用的。在「設定」、「共享」、「存取權」裡把「登入名稱」和「密碼」留空，就會允許訪客存取。如果你想要連線先登入，就設定它們。只有在你開啟「要求 SMB 加密」時才需要登入名稱和密碼，因為加密的連線不能匿名。
{{% /details %}}

{{% details title="SMB 連線有加密嗎？" closed="true" %}}
可以有。SMB 是 Everdisk 裡唯一支援加密的連線。設定登入名稱和密碼，然後在「設定」、「共享」裡開啟「要求 SMB 加密」。之後每一次傳輸都會用 SMB3 (AES) 保護。另一台裝置需要支援 SMB3，新型 Mac 和 Windows 10 以上版本都支援。加密是 Premium 功能。
{{% /details %}}

{{% details title="別人可以透過 SMB 更改或刪除我的檔案嗎？" closed="true" %}}
只有在你允許時才行。「設定」、「共享」、「存取權」裡的「檔案編輯」開關會控制這一點。開啟時，連接的裝置可以上傳、重新命名和刪除。關閉時，這個共享就是唯讀的，別人可以瀏覽並把檔案從你的手機複製出去，但不能更改任何東西。
{{% /details %}}

{{% details title="我的 SMB 連線為什麼中斷了？" closed="true" %}}
你的 iPhone 是伺服器，而 iOS 會暫停在背景待太久的 App。裝置連著的時候，請讓 Everdisk 保持開在畫面上，並在長時間傳輸時把手機接上電源。也要確認兩台裝置仍在同一個 Wi-Fi 上。
{{% /details %}}

{{% details title="SMB、WebDAV 還是 FTP，我該用哪一個？" closed="true" %}}
當你想讓手機在 Mac、另一支 iPhone、Linux 或 NAS 上表現得像一個真正的網路磁碟，而且想要加密時，就用 SMB。當你想要一個也能從 Windows 順利運作的網路磁碟時，就用 WebDAV。想要和較舊裝置及 App 有最廣泛的相容性時，就用 FTP。Everdisk 可以同時執行全部三種，所以你不會被綁在其中一種上。
{{% /details %}}

{{% details title="Everdisk 是免費的嗎？" closed="true" %}}
是的，Everdisk 免費下載，而且內含 SMB 伺服器。選購的一次性 Premium 購買會加入 SMB 加密、自訂連接埠和其他幾項額外功能。你不用付費就能設定 SMB 並分享檔案。
{{% /details %}}

準備好試試看了嗎？[從 App Store 下載 Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)，大約一分鐘就能在 Finder 裡打開你的 iPhone。有問題或建議嗎？寄信給我們：**support@everappz.com**。
