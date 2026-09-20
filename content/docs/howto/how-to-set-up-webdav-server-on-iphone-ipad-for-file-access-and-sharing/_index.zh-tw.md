---
title: "如何在 iPhone 和 iPad 上設定 WebDAV 伺服器來存取與分享檔案"
description: "用 Everdisk 把你的 iPhone 或 iPad 變成 WebDAV 伺服器，透過 Wi-Fi 在 Mac Finder、Windows 檔案總管、Linux、Android 或另一支 iPhone 上把它掛載成網路磁碟。完整設定、WebDAV 位址和連接埠，以及每一種裝置的逐步連線教學。"
date: 2026-09-19
tags: ["everdisk", "webdav", "網路磁碟", "檔案分享", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["iPhone WebDAV 伺服器", "iPad WebDAV 伺服器", "如何在 iPhone 設定 WebDAV", "把 iPhone 掛載成網路磁碟", "從 Mac Finder 連接 iPhone WebDAV", "WebDAV Windows 檔案總管 iPhone", "iphone 網路磁碟 Windows", "WebDAV Linux iPhone", "從電腦存取 iPhone 檔案", "iphone 到 iphone webdav", "從 iPhone 分享檔案 WebDAV", "把 iphone 對應成網路磁碟", "透過 webdav 傳輸 iphone 檔案", "iphone webdav 位址連接埠"]
readingTime: 9
---

{{< author-byline >}}

WebDAV 把一個資料夾變成網路磁碟，讓電腦能在它一般的檔案管理程式裡打開。它透過和你瀏覽器一樣的網頁協定執行，這就是為什麼它能跨 Mac、Windows 和 Linux 順暢運作，而不需要特殊驅動程式。有了 [Everdisk](/products/everdisk)，你可以在 iPhone 或 iPad 上執行一個 WebDAV 伺服器，讓手機以磁碟的形式出現，供你從幾乎任何電腦瀏覽、從中複製，以及複製檔案進去。

當有 Windows 在其中時，WebDAV 是最好的選擇，因為 Windows 檔案總管能乾淨俐落地連上它。這份指南涵蓋設定，以及如何從 Mac、Windows、Linux、Android 和第二支 iPhone 連上。

## 你需要準備什麼

- 一支已安裝 [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) 的 iPhone 或 iPad。
- 一台在**同一個 Wi-Fi 網路**上的電腦或另一台裝置。
- 你想分享的檔案，放在 Everdisk 的「文件」資料夾或你加入的資料夾裡。

## 在 Everdisk 裡設定 WebDAV 伺服器

### 步驟 1：選擇要分享什麼並設定存取權

打開 Everdisk，前往「共享」分頁，點一下「分享什麼」。「文件」資料夾預設就會分享。用「加入檔案夾」和「加入檔案」加入更多。

打開「設定」，接著「共享」，接著「存取權」。如果你想讓連接的電腦把檔案複製到你的手機上，並重新命名或刪除，就把「檔案編輯」開啟；想要唯讀磁碟就關閉。如果你想要登入，就在這裡設定「登入名稱」和「密碼」，或留空以允許訪客存取。

### 步驟 2：開啟 WebDAV 伺服器

前往「設定」，接著「共享」，接著「連線」，然後開啟「電腦」。那就是 WebDAV 伺服器（它帶有 WebDAV 標籤）。

### 步驟 3：開始分享並記下位址

回到「共享」分頁並點一下「開始」。「如何連線」這一區會顯示 WebDAV 位址。它看起來像這樣：

```
http://192.168.1.20:8080
```

冒號後面的數字是**連接埠**，預設是 **8080**。第一部分是你 iPhone 在 Wi-Fi 上的位址，所以你的會不一樣。裝置連著的時候，請讓 Everdisk 保持開在畫面上。

## 從 Mac 連接

1. 打開 **Finder**，選擇「前往」，接著「連接伺服器」（或按 **Command 加 K**）。
2. 輸入 Everdisk 裡顯示的 WebDAV 位址，例如 `http://192.168.1.20:8080`。
3. 點一下「連接」，然後選擇「訪客」或輸入你的「登入名稱」和「密碼」。

你的 iPhone 會在一個 Finder 視窗裡打開，表現得像一般資料夾。如果「檔案編輯」有開，就能雙向複製檔案。

## 從 Windows 連接

Windows 內建 WebDAV 用戶端，所以這在檔案總管裡就能運作。

1. 打開**檔案總管**，在側邊欄右鍵點一下**本機**，選擇**新增網路位置**（你也可以用**對應網路磁碟機**）。
2. 被詢問位址時，輸入 Everdisk 裡同樣的 WebDAV 位址，例如 `http://192.168.1.20:8080`，然後點**下一步**。
3. 如果你有設定，就輸入你的「登入名稱」和「密碼」。

之後裝置會以一個網路位置的形式出現在「本機」底下，你可以打開它並從中複製檔案。如果 Windows 第一次拒絕連接，請確認 **WebClient** 服務正在執行（在「開始」選單搜尋「服務」，找到 WebClient，把它設為啟動），然後再試一次。

## 從 Linux 連接

1. 打開你的檔案管理程式，選擇「連接伺服器」或「其他位置」。
2. 輸入帶有 WebDAV 前綴的位址，例如 `dav://192.168.1.20:8080`（只有在你設定了 TLS 時才用 `davs://`）。
3. 以訪客身分連接，或輸入你的登入資訊。

## 從 Android 連接

Android 沒有系統內建的 WebDAV 瀏覽器，所以要用一個支援它的檔案管理程式：

1. 安裝像 **Solid Explorer** 或 **CX File Explorer** 這樣的 App。
2. 加入一個新的 **WebDAV** 連線。
3. 輸入主機和**連接埠 8080**，選擇 `http` 協定，如果你有設定就加上你的登入資訊。

## 從另一支 iPhone 或 iPad 連接

iOS 的「檔案」App 不含 WebDAV 用戶端，所以用以下其中一種：

- **Everdisk 自己的「裝置」分頁。** 在第二台裝置上，打開 Everdisk，前往「裝置」，點一下「新增連線」，選擇「WebDAV」，然後輸入位址，例如 `http://192.168.1.20:8080`。這是最簡單的做法，不需要任何額外的東西。
- **一個 WebDAV App**，例如 Documents by Readdle，它可以用同樣的位址和登入資訊加入一個 WebDAV 連線。

## 比較想要一個快速連結而不是磁碟？

如果你只是想快速抓一個檔案，而完全不想掛載磁碟，就在「設定」、「共享」、「連線」裡開啟「瀏覽器」連線。Everdisk 就會給你一個網址，你可以在任何裝置的任何瀏覽器裡打開它，來瀏覽和下載你的檔案。這是把檔案交給 Windows PC、Chromebook 或朋友手機最快的方式。

## 唯讀還是可讀寫

「設定」、「共享」、「存取權」裡的「檔案編輯」開關決定這一點。開啟表示連接的電腦可以上傳、重新命名和刪除。關閉表示磁碟是唯讀的，所以別人可以檢視並複製你的檔案，但不能更改它們。

## 大家實際上怎麼用

- **從 Windows PC 把檔案複製到你的 iPhone 上**，把它對應成一個網路位置，再把檔案拖過去。
- **把相片和文件卸載到筆電上**，用你早就熟悉的檔案管理程式，不用線材也不用 iTunes。
- **就地編輯文件**，從你的 Mac 直接從手機打開它並存回去。
- **在 iPhone 和 iPad 之間移動一個資料夾**，用接收端裝置上 Everdisk 的「裝置」分頁。

## 一些小提示

- 裝置連著的時候讓 Everdisk 保持開著。把手機鎖住很久可能會暫停 App。
- 在 Windows 上，如果連線失敗，就啟動 WebClient 服務再重試那個位址。
- WebDAV 和 SMB 都會掛載成網路磁碟。有 Windows 時用 WebDAV，想要 Finder 速度和加密時用 [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)。
- 想要最快的傳輸，就把「設定」裡的相片和影片品質保持在「原始」。

## 常見問題

{{% details title="我 iPhone 的 WebDAV 位址和連接埠是什麼？" closed="true" %}}
在你開始分享後，Everdisk 會在「共享」畫面上顯示位址。它看起來像 http://192.168.1.20:8080。8080 是 Everdisk 用於 WebDAV 的連接埠，第一部分是你 iPhone 在 Wi-Fi 上的位址，所以你的會不一樣。
{{% /details %}}

{{% details title="我要怎麼從 Windows 連上我 iPhone 的 WebDAV？" closed="true" %}}
打開檔案總管，右鍵點一下本機，選擇新增網路位置或對應網路磁碟機。輸入 Everdisk 裡的 WebDAV 位址，例如 http://192.168.1.20:8080，然後如果你有設定就輸入你的登入資訊。如果 Windows 連不上，請確認 WebClient 服務正在執行（搜尋「服務」，找到 WebClient，啟動它），然後再試一次。
{{% /details %}}

{{% details title="我可以在兩支 iPhone 之間用 WebDAV 嗎？" closed="true" %}}
可以，但 iOS 的「檔案」App 沒有 WebDAV 用戶端，所以在第二台裝置上用 Everdisk。打開「裝置」分頁，點一下「新增連線」，選擇「WebDAV」，然後輸入第一支手機上顯示的位址。像 Documents by Readdle 這樣的 WebDAV App 也可以。
{{% /details %}}

{{% details title="WebDAV 需要密碼嗎？" closed="true" %}}
不需要，登入是選用的。在「設定」、「共享」、「存取權」裡把「登入名稱」和「密碼」留空以允許訪客存取，或設定它們讓連線先登入。
{{% /details %}}

{{% details title="別人可以透過 WebDAV 更改我的檔案嗎？" closed="true" %}}
只有在你允許時才行。「設定」、「共享」、「存取權」裡的「檔案編輯」開關會控制這一點。開啟時，連接的裝置可以上傳、重新命名和刪除。關閉時，磁碟是唯讀的，所以別人可以檢視並複製，但不能更改任何東西。
{{% /details %}}

{{% details title="WebDAV 還是 SMB，差別是什麼？" closed="true" %}}
兩者都會把你的 iPhone 掛載成網路磁碟。WebDAV 透過網頁協定執行，並能從 Windows 檔案總管乾淨地連上，這是它的主要強項。SMB 是 Mac、Linux 和 NAS 裝置上原生的檔案分享方式，在 Mac 上通常更快，而且是 Everdisk 裡唯一能加密傳輸的連線。Everdisk 可以同時執行兩者。
{{% /details %}}

{{% details title="我的 WebDAV 磁碟為什麼會斷線？" closed="true" %}}
你的 iPhone 是伺服器，而 iOS 會暫停在背景待太久的 App。裝置連著的時候，請讓 Everdisk 保持開在畫面上，並在長時間傳輸時接上電源。也要確認兩台裝置仍在同一個 Wi-Fi 上。
{{% /details %}}

{{% details title="我可以在沒有 Wi-Fi 的情況下透過 WebDAV 連接嗎？" closed="true" %}}
可以，只要你用線材把 iPhone 接上 Mac。Everdisk 就會顯示一個額外的傳輸線連接位址，連接的 Mac 可以在 Finder 裡打開它，即使完全沒有 Wi-Fi 也能運作。在傳輸線上，只有那台 Mac 能連到裝置。
{{% /details %}}

{{% details title="Everdisk 是免費的嗎？" closed="true" %}}
是的，Everdisk 免費下載，而且內含 WebDAV 伺服器。選購的一次性 Premium 購買會加入一些額外功能，例如自訂連接埠以及相片和影片轉換。你不用付費就能設定 WebDAV 並分享檔案。
{{% /details %}}

準備好試試看了嗎？[從 App Store 下載 Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)，幾分鐘內就把你的 iPhone 掛載成磁碟。有問題或建議嗎？寄信給我們：**support@everappz.com**。
