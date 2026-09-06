---
title: "分享"
date: 2026-08-20
description: "了解 Everdisk 的分享如何運作：點一下 Start 把 iPhone 或 iPad 變成無線硬碟，選擇要分享的內容（檔案、資料夾、相片和音樂），執行四種伺服器（DLNA、HTTP、WebDAV、FTP），讀取連線位址，查看誰已連線，並透過 Wi-Fi 或 USB 傳輸線持續分享。"
keywords: ["Everdisk 分享", "iPhone 無線硬碟", "開始分享", "iPhone 分享檔案", "透過網路分享相片", "DLNA HTTP WebDAV FTP", "分享什麼", "如何連線", "保持 app 開啟", "透過 Wi-Fi 或 USB 傳輸線分享"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


**Sharing** 分頁是 Everdisk 的核心。你在這裡把 iPhone 或 iPad 變成無線硬碟，精確挑選想分享的內容，並取得其他裝置連線時要用的位址。這是你打開 app 後看到的第一個分頁。

## 開始與停止分享

分享畫面的正中央有一個大圓形按鈕。

- 點一下 **Start**，讓所有已啟用的伺服器同時上線。按鈕會顯示 **Starting...**，等分享上線後就變成 **Stop**。
- 點一下 **Stop**，讓一切重新離線。已連線的裝置會被中斷連線。

分享執行期間，你挑選的檔案、相片和音樂，會提供給同一網路上以下方四種方法之一連線的任何裝置。

> 分享只在 app 開啟時運作。請看本頁接近結尾的 **保持 app 開啟**，了解原因，以及如何讓大型傳輸持續進行。

## 選擇要分享的內容

開始前，先點一下 **What to Share** 標題，開啟三個群組。你可以任意組合分享，而且開始分享前至少要選一項。

**檔案與資料夾**

- 預設會分享 app 本身的 **Documents** 資料夾。你也可以選擇不分享它。
- 點一下 **Add Folder** 分享裝置上任何位置的資料夾，或點 **Add File** 分享個別檔案。
- 每個已分享的項目都有一個 **Info** 按鈕和一個 **Stop Sharing** 按鈕。

**相片與影片**

- 開啟 **Allow access to all Photos Library** 分享整個相片和影片圖庫，或
- 點一下 **Add Photos**，只挑選你想分享的相片和影片。

**音樂**

- 開啟 **Allow access to all Music Library** 分享整個音樂圖庫，或
- 點一下 **Add Tracks**，只分享選定的歌曲。
- 受保護（DRM）或僅儲存在雲端的曲目無法分享。

如果你什麼都沒選就試著開始，Everdisk 會顯示 **Nothing to Share** 提示。若你在分享執行期間變更了分享內容，請 **先 Stop 再重新 Start**，讓變更生效。

## 四種伺服器

Everdisk 會同時以四種方式分享同一批內容。每一種都是為不同類型的裝置設計的，都能在 **設定 → 分享 → 連接** 裡開啟或關閉。四種預設全部開啟。

- **TV & Media Center (DLNA)** - 適用於智慧型電視和媒體播放器。它們會自行找到你的裝置，並顯示你的相片、影片和音樂，還附帶預覽縮圖。
- **Browser (HTTP)** - 適用於任何手機、平板或電腦。對方在網頁瀏覽器裡開啟一個連結，就能瀏覽和下載你的檔案。不必安裝任何東西。
- **Computer (WebDAV)** - 適用於 Mac、Windows PC 或 Linux 電腦。你的裝置會像一般網路硬碟一樣出現，讓你雙向拖放檔案。
- **Other Apps & Devices (FTP)** - 適用於支援 FTP 的檔案 app 和進階使用者。

每種類型的逐步連線說明，請看 [連接你的裝置](/docs/guide/everdisk/everdisk-guide-connect)。

## 如何連線與連線位址

點下 Start 之後，**How to Connect** 區段會為每個運作中的伺服器顯示一張卡片，附上要在對方裝置上輸入的確切 **位址**。每個位址都很容易複製 - 點一下即可複製、用 **Share** 按鈕傳送，或點 **info (ⓘ)** 按鈕查看各通訊協定的詳細說明。

- DLNA 卡片會顯示一個以 `/device-desc.xml` 結尾的裝置描述位址，供需要它的播放器使用。
- 當你的裝置用傳輸線接上 Mac 時，會多出一個帶 **Cable Connection** 標記的位址，使用你裝置的 `.local` 名稱。

你也可以把位址開成 **QR code**，讓另一台裝置的相機直接跳轉過去。

## 誰已連線

**Who is Connected** 區段會即時列出目前連到你的裝置。若有你不認得的裝置，點一下它旁邊的更多操作按鈕，即可 **Block this device**。被封鎖的裝置在 [存取與隱私](/docs/guide/everdisk/everdisk-guide-access) 裡管理。

## 你的裝置名稱與頭像

每台裝置都有一個好記的名稱（例如「Speedy-Hare」）和一個彩色頭像。這是電視、電腦或其他 app 在網路上顯示你裝置時所用的名稱，方便辨識。你可以免費重新產生名稱和頭像，或用 Premium 設定自訂名稱、圖示或相片頭像。請看 [設定](/docs/guide/everdisk/everdisk-guide-settings)。

## 透過 Wi-Fi 或 USB 傳輸線分享

分享可以在兩種情況下運作：

- **透過 Wi-Fi** - 你的裝置和其他裝置在同一個 Wi-Fi 網路上。
- **透過 USB 傳輸線** - 你的裝置用傳輸線接到 **Mac**，即使完全沒有 Wi-Fi 也行。這比 Wi-Fi 更快，而且在飛機上、飯店裡或受限的網路上都能持續運作。

如果 Wi-Fi 和傳輸線都不可用，**Start** 按鈕會停用，並出現 **No Wi-Fi Connection** 提示。若分享期間連線中斷，Everdisk 會自動停止分享並通知你。點一下這些提示上的 info 按鈕，即可看到完整說明。

## 保持 app 開啟

由於你的 iPhone 或 iPad 正扮演伺服器的角色，**分享只在 Everdisk 於畫面上開啟時運作**。如果你關閉 app，或長時間鎖住裝置，系統可能會暫停 app，分享便會停止。

進行大型傳輸時：

- 讓 Everdisk 保持開啟並在前景。
- 把裝置接上電源。
- 傳輸期間，在 iOS 設定 app 裡把 **Auto-Lock** 設為 **Never**。

你可以開啟 **Notify before disconnecting**（在 設定 → 分享 裡），讓 Everdisk 在系統暫停 app 之前提醒你重新開啟。點一下 **保持 app 開啟** 橫幅上的 info 按鈕，可看到更多細節。

## 下一步

- [連接你的裝置](/docs/guide/everdisk/everdisk-guide-connect) - 連接電視、電腦、瀏覽器、手機或 USB 傳輸線。
- [存取與隱私](/docs/guide/everdisk/everdisk-guide-access) - 加上密碼並控制編輯權限。
- [設定](/docs/guide/everdisk/everdisk-guide-settings) - 開啟或關閉伺服器並調整品質。
