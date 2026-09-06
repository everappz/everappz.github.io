---
title: "連接到伺服器"
date: 2026-08-20
description: "使用 Everdisk 的 Devices 分頁連接到網路上的其他伺服器。新增並瀏覽 DLNA、WebDAV、FTP 和 SFTP 伺服器與 NAS 硬碟，串流音訊和影片，下載檔案，並在允許的伺服器上建立、上傳、重新命名、移動或刪除。"
keywords: ["Everdisk Devices 分頁", "連接 NAS", "iPhone DLNA 用戶端", "iPhone WebDAV 用戶端", "iPhone FTP 用戶端", "iPhone SFTP 用戶端", "瀏覽網路伺服器", "從 NAS 串流", "從伺服器下載", "連接雲端 WebDAV"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk 不只是一台無線硬碟 - 它也是網路上其他裝置的用戶端。**Devices** 分頁讓你連接到 **DLNA**、**WebDAV**、**FTP** 和 **SFTP** 伺服器，包括 NAS 硬碟和媒體伺服器，然後瀏覽、串流和下載它們的檔案。

## Devices 畫面

Devices 分頁分為兩個部分：

- **Connections** - 你已經儲存的伺服器。
- **Available Devices** - Everdisk 在你的本地網路上自動找到的伺服器。

要連接 Everdisk 已找到的裝置，只要在 **Available Devices** 裡點一下它即可。要手動新增伺服器，點一下 **加號 (+)** 按鈕或 **New Connection**。

## 新增一個連線

點一下 **New Connection**，選擇你想存取的伺服器類型：

- **DLNA / UPnP** - 最適合媒體伺服器。從媒體庫、網路儲存硬碟以及支援 DLNA 的電視和電腦串流影片、音樂和相片。DLNA 為唯讀：你可以瀏覽、串流和下載，但無法上傳或變更檔案。
- **WebDAV** - 連接到支援 WebDAV 的檔案伺服器、網路儲存硬碟和雲端硬碟。在伺服器允許時可讀寫。
- **FTP** - 常見於路由器、網路儲存硬碟和網頁主機。預設連接埠是 21（安全 FTPS 為 990）；你可以在位址裡設定自訂連接埠，例如 `ftp://host:2121`。留空帳號和密碼即可進行匿名存取。
- **SFTP** - 透過 SSH 安全連接。預設連接埠是 22；若有需要，可在位址裡使用自訂連接埠，例如 `sftp://host:2222`。

> Everdisk 只連接這些本地網路和直接定址的通訊協定。它不會登入 Google Drive 或 Dropbox 這類雲端帳號。只有當該服務提供你能輸入的 **WebDAV** 位址時，雲端硬碟才可存取。

## 輸入位址並登入

在連線編輯器裡，填寫：

- **Title** - 這個連線的好記名稱。
- **URL / 位址** - 伺服器位址（每種類型都會顯示範例）。
- **Login** 和 **Password** - 若伺服器允許匿名存取，兩者都留空。

若你的 WebDAV 伺服器使用自我簽署憑證，你可以允許無效的憑證。如果安全伺服器的身分無法驗證，Everdisk 會先請你確認才信任它。

免費使用者最多可儲存 **10** 個連線。Premium 解除此限制。

## 瀏覽、串流與下載

連上之後，點一下伺服器即可開啟它：

- **瀏覽** 資料夾，以清單或格狀檢視，排序，並查看縮圖。DLNA 伺服器還會顯示音樂細節和封面。
- **串流** 音訊和影片。音訊會進入迷你播放器佇列；影片全螢幕播放。串流檔案時可以拖曳進度。
- 把檔案 **下載** 到你的裝置。一次選取多個進行批次下載。下載會出現在 **File Transfers** 裡，並存到你的 **Documents** 資料夾。
- 任何項目上的 **Info** 會顯示它的種類、大小、日期、路徑和媒體細節。

## 在伺服器上變更檔案

在允許寫入的伺服器上 - **WebDAV、FTP 和 SFTP** - 你還可以管理檔案：

- **New Folder**
- 從你的裝置 **Upload Files**
- **Rename**、**Move** 和 **Delete**（一次一個或多個項目）

**DLNA** 伺服器為唯讀，所以這些操作在那裡無法使用。

## 追蹤你的傳輸

下載和上傳會在背景執行，並顯示在 **File Transfers** 裡，你可以從 **Documents** 分頁左上角開啟它。你可以在那裡查看進度，並暫停、繼續、重試、取消或清除工作。你也可以在 [設定 → Network](/docs/guide/everdisk/everdisk-guide-settings) 裡調整傳輸（僅 Wi-Fi 或 Wi-Fi 加行動網路、同時執行幾個，以及是否在背景繼續）。

## 下一步

- [檔案與文件](/docs/guide/everdisk/everdisk-guide-files) - 管理你下載的一切。
- [相片、音樂與影片](/docs/guide/everdisk/everdisk-guide-media) - 播放你串流的內容。
- [設定](/docs/guide/everdisk/everdisk-guide-settings) - 連線上限和傳輸選項。
