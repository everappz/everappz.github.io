---
title: "連接你的裝置"
date: 2026-08-20
description: "連接到你的 Everdisk 無線硬碟的逐步說明：透過 DLNA 在智慧型電視上觀看、在任何網頁瀏覽器裡開啟你的檔案、透過 WebDAV 把裝置掛載成 Finder、Windows 或 Linux 的網路硬碟、透過 FTP 連接檔案 app，以及在沒有 Wi-Fi 時用 USB 傳輸線傳到 Mac。"
keywords: ["連接到 Everdisk", "DLNA 串流到電視", "在瀏覽器開啟檔案", "在 Finder 掛載網路硬碟", "WebDAV Windows Linux", "FTP 檔案 app", "USB 傳輸線傳到 Mac", "把 iPhone 連到電腦", "iPhone 網路硬碟"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


在 [分享](/docs/guide/everdisk/everdisk-guide-sharing) 畫面上點一下 **Start** 之後，其他裝置就能用四種不同方式連上你的檔案。挑選符合你想使用裝置的方法。無論哪一種，你需要的確切 **位址** 都會顯示在分享畫面的 **How to Connect** 區段裡。

> 兩台裝置必須在 **同一個 Wi-Fi 網路** 上 - 或者，若是 Mac，用 **USB 傳輸線** 連接（請看最後一節）。

## 在電視上觀看 (DLNA)

用這個方式在智慧型電視或媒體播放器上顯示相片、影片和音樂。

1. 在 **設定 → 分享 → 連接** 裡，確認 **TV & Media Center** 已開啟（預設是開啟的）。
2. 在分享畫面上，點一下 **Start**。
3. 在你的電視上，開啟內建的媒體播放器或媒體伺服器 app（它可能叫 Media Player、SmartShare、AllShare 或類似的名稱）。
4. 你的裝置會以它的名稱（例如「Speedy-Hare」）出現在媒體伺服器清單裡。選取它。
5. 瀏覽你分享的相片、影片和音樂並開始播放。預覽縮圖會自動出現。

注意事項：

- DLNA 無法設定密碼保護，所以只要開啟，同一 Wi-Fi 上的任何人都能存取這個連線。
- 如果影片在較舊的電視上無法播放，請在 **設定 → 分享 → 影片** 裡降低影片品質，讓 Everdisk 把它轉換成相容性更高的格式。

## 在網頁瀏覽器裡開啟 (HTTP)

用這個方式把檔案交給任何有網頁瀏覽器的人 - 完全不用安裝 app。

1. 在 **設定 → 分享 → 連接** 裡，確認 **Browser** 已開啟。
2. 點一下 **Start**。
3. 在分享畫面上，複製 **Browser** 位址（或顯示它的 QR code）。
4. 在另一支手機、平板或電腦上，開啟任何網頁瀏覽器（Safari、Chrome、Edge、Firefox）並輸入那個位址。
5. 頁面就會開啟，顯示你分享的檔案。

在瀏覽器裡，對方可以：

- 在 **清單** 和 **格狀** 檢視間切換，並依名稱、日期或大小排序。
- 看到相片、影片、PDF 和音樂封面的真實 **縮圖**。
- 開啟相片進入全螢幕 **圖庫**，支援滑動、雙指縮放和幻燈片播放。
- 在內建 **播放器** 裡播放音樂，附有佇列、隨機播放和重複播放。
- **下載** 任何檔案，或把整個資料夾（或數個選取的項目）當成一個 **Archive.zip** 下載。
- 把檔案 **上傳** 回你的裝置 - 前提是你開啟了 **Files Editing**（請看 [存取與隱私](/docs/guide/everdisk/everdisk-guide-access)）。

## 當成網路硬碟使用 (WebDAV)

用這個方式讓你的裝置在 Mac、Windows PC 或 Linux 電腦上像一般磁碟一樣出現，讓你雙向拖放檔案。

**在 Mac（Finder）上**

1. 在 **設定 → 分享 → 連接** 裡，確認 **Computer** 已開啟。
2. 點一下 **Start** 並記下 **Computer (WebDAV)** 位址。
3. 在 Finder 裡，選擇 **前往 → 連接伺服器**（或按 **⌘K**）。
4. 完全依照顯示的內容輸入 WebDAV 位址，然後按 **連接**。
5. 如果你設了帳號和密碼就輸入，否則以訪客身分連接。
6. 你的裝置會像其他網路硬碟一樣開啟。把檔案拖進拖出即可。

**在 Windows 上**

1. 開啟 **檔案總管**，右鍵點 **本機**，然後選 **新增網路位置**（或對應網路磁碟機）。
2. 輸入 Everdisk 裡顯示的 WebDAV 位址。
3. 如果你設了帳號和密碼就輸入。

**在 Linux 上**

1. 開啟你的檔案管理員並選擇 **連接伺服器**（或使用 `davs://` / `dav://`）。
2. 輸入 Everdisk 裡顯示的 WebDAV 位址。

連線是唯讀還是雙向，取決於 **Files Editing** 設定。開啟時，你可以把檔案複製到裝置上，並重新命名或刪除；關閉時，磁碟為唯讀。

## 連接檔案 app (FTP)

用這個方式連接支援 FTP 的檔案管理員和傳輸 app（例如電腦上的 FileZilla 或 Cyberduck）。

1. 在 **設定 → 分享 → 連接** 裡，確認 **Other Apps & Devices** 已開啟。
2. 點一下 **Start** 並記下 **FTP** 位址。
3. 在你的 FTP app 裡，用那個位址新增一個連線。
4. 如果你設了帳號和密碼就輸入，或留空以進行匿名存取。

## 透過 USB 傳輸線傳輸（Mac，不需 Wi-Fi）

當沒有 Wi-Fi，或你想要最快、最私密的傳輸時，就用這個方式。它只適用於 **Mac**。

1. 用一般的充電線把你的 iPhone 或 iPad 接到 Mac。
2. 若裝置上詢問，點一下 **信任這部電腦**。
3. 在 Everdisk 裡點一下 **Start**。會出現 **Fast Connection Available** 提示，分享畫面也會多出一個帶 **Cable Connection** 標記、以 `.local` 結尾的位址。
4. 在 Mac 上，開啟 Finder → **前往 → 連接伺服器**（**⌘K**），輸入那個 `.local` 位址（它對 Browser 和 Computer 兩種連線都有效）。
5. 你的裝置會透過傳輸線開啟 - 比 Wi-Fi 更快，而且資料完全不會經過路由器或網際網路。

注意事項：

- 使用 **`.local` 名稱**，而非 IP 位址（IP 位址只在 Wi-Fi 上有效），也絕不要用 `localhost`。
- 傳輸線路徑 **僅限 Mac**。Windows PC 和 Android 裝置必須使用 Wi-Fi。
- 你也可以透過標準的 iOS 檔案分享，在 Mac 上用 Finder，或在 Windows 上用 Apple Devices app（或 iTunes），把檔案拖進 Everdisk 資料夾。

## 下一步

- [存取與隱私](/docs/guide/everdisk/everdisk-guide-access) - 加上密碼、允許上傳、封鎖裝置。
- [相片、音樂與影片](/docs/guide/everdisk/everdisk-guide-media) - 分享整個圖庫並設定品質。
- [連接到伺服器](/docs/guide/everdisk/everdisk-guide-devices) - 從 Everdisk 存取其他裝置。
