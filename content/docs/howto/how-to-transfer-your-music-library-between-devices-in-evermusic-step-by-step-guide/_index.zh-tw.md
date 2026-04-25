---
title: "如何在Evermusic中在裝置之間傳輸音樂庫：逐步指南"
description: "使用Wi-Fi Drive和備份工具，輕鬆將Evermusic音樂庫、播放列表、專輯封面和設定從一台iPhone、iPad或Mac傳輸到另一台。"
date: 2024-12-29
tags: ["音樂庫", "傳輸", "wifi", "備份", "webdav", "還原"]
keywords: ["傳輸音樂庫Evermusic", "備份和還原播放列表Evermusic", "Evermusic WiFi Drive", "在裝置之間同步Evermusic", "遷移Evermusic資料庫", "Evermusic檔案傳輸", "還原音訊播放器設定", "WebDAV音樂傳輸iOS"]
readingTime: 3
---

{{< author-byline >}}


**摘要：** 要將Evermusic庫傳輸到新裝置，請在來源裝置上建立備份，啟動Wi-Fi Drive，透過同一網路連接第二台裝置，下載備份和音樂檔案，然後從備份還原。整個過程大約需要10分鐘，視庫的大小而定。

在本指南中，我們將引導您完成將整個音樂庫（包括資料庫、專輯封面和設定）從一台裝置（iPhone或Mac）傳輸到另一台裝置的過程。雖然自動音樂庫和播放列表同步是計劃在未來推出的功能，但目前此過程必須手動完成。

## 步驟1：在第一台裝置上建立備份

1. **在第一台裝置上開啟應用程式**（擁有音樂庫、播放列表和已連接雲端服務的裝置）。
2. **導覽至設定**，選擇**備份和還原**選項。

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. 在**備份和還原**畫面，選擇要包含在備份檔案中的項目：
   - **資料庫**（包括音樂庫和播放列表）
   - **專輯封面**
   - **設定**

這些選項預設已啟用。

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. 點擊**備份應用程式資料**開始備份過程。

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. 備份完成後，將出現一條資訊提示。

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

點擊**顯示檔案**以在**文件**目錄中檢視備份檔案。備份檔案通常儲存在**Backup**資料夾中。

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## 步驟2：啟動Wi-Fi Drive伺服器

1. 在應用程式中進入**連接**部分。
2. 向下捲動到**透過Wi-Fi連接**並點擊。

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. 在下一個畫面，點擊**啟動Wi-Fi Drive**。

- 您可以選擇設定使用者名稱和密碼以增強安全性，但對於家庭網路來說這不是必需的。

4. 啟動後，您將看到可用的伺服器位址。這可以用於桌面瀏覽器或WebDAV應用程式，但在本指南中，我們將直接進入下一步。

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## 步驟3：將第二台裝置連接到第一台

1. 在第二台裝置上開啟應用程式（您要將庫傳輸到的裝置）。
2. 確保兩台裝置連接到同一Wi-Fi網路。
3. 在第二台裝置上，開啟**連接**標籤頁並選擇**可用設備**。

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. 您應該會看到一個名為**Evermusic**的WebDAV連接（我們在第一台裝置上啟動的伺服器）。點擊它進行連接。

5. 連接後，您將看到第一台裝置上的所有資料夾。

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## 步驟4：準備檔案傳輸

1. 在第二台裝置上，進入**設定 > 檔案管理員**並啟用**將下載的檔案儲存到 - 每次詢問**。

- 這確保您可以為每次下載選擇目標資料夾。

2. 返回**連接**標籤頁並導覽到已連接的WebDAV伺服器。

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## 步驟5：傳輸備份和音樂檔案

1. 開啟已連接WebDAV伺服器上的**Backup**資料夾。

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. 點擊備份檔案旁邊的**更多操作**按鈕（三個點）並選擇**下載**。

3. 在第二台裝置上建立一個**Backup**資料夾來儲存下載的檔案。點擊**完成**確認選擇。

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. 傳輸任何其他音樂檔案：
   - 檢查WebDAV伺服器上的**下載**資料夾或其他相關資料夾。

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- 使用**選擇**選項選擇檔案，然後點擊**更多操作 > 下載**。將它們儲存到第二台裝置上的相應資料夾中，以保持相同的目錄結構。

目標是將第一台裝置上的所有檔案傳輸到當前裝置，確保資料夾結構保持一致。這樣，音樂庫和播放列表中的連結將保持完好。請注意，儲存在第一台裝置應用程式文件目錄之外的本地檔案必須單獨傳輸。由於應用程式在Wi-Fi Drive模式下無法存取這些檔案，您需要使用系統檔案應用程式進行傳輸。

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## 步驟6：監控傳輸進度

1. 在第二台裝置上，進入**本地檔案**部分（或iPad/Mac上的**下載**標籤頁）。

2. 點擊左上角的**傳輸活動**按鈕來監控傳輸佇列。

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## 步驟7：從備份還原資料

1. 備份檔案和所有需要的音訊檔案下載到第二台裝置後，開啟**Backup**資料夾。

2. 點擊備份檔案，將出現確認訊息。

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **注意：** 還原將用備份資料替換當前所有音樂庫資料、播放列表、設定和專輯封面。

3. 點擊**還原**開始過程。

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. 還原完成後，提示將確認成功。

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

檢查**播放列表**或**音樂庫**部分以驗證還原。

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## 步驟8：重新索引音樂庫

1. 為獲得最佳效果，請重新索引您的庫以確保所有檔案都被成功偵測到。

2. 進入**設定 > 音樂庫 > 離線音樂同步**並選擇**開始掃描本地資料夾**。

按照這些步驟，您將成功將音樂庫、播放列表和設定傳輸到另一台裝置。如果遇到任何問題，請隨時聯繫支援團隊。

## 常見問題

{{% details title="我可以在沒有Wi-Fi的情況下傳輸Evermusic庫嗎？" closed="true" %}}
Wi-Fi Drive要求兩台裝置在同一Wi-Fi網路上。目前沒有藍牙或行動網路傳輸選項。您也可以使用AirDrop或檔案應用程式在裝置之間手動移動備份檔案和音樂資料夾。
{{% /details %}}

{{% details title="雲端服務連接會隨備份一起傳輸嗎？" closed="true" %}}
備份包括資料庫、播放列表、專輯封面和設定。出於安全原因，不包括雲端服務登入憑證。還原後，您需要在新裝置上重新連接雲端帳戶。
{{% /details %}}

{{% details title="第二台裝置上的現有庫會怎樣？" closed="true" %}}
還原備份將替換第二台裝置上所有現有的音樂庫資料、播放列表、設定和專輯封面。如果您想保留其資料，請先為第二台裝置建立單獨的備份。
{{% /details %}}

{{% details title="此過程在iPhone和Mac之間是否有效？" closed="true" %}}
是的。Evermusic支援在iPhone、iPad和Mac的任意組合之間進行Wi-Fi Drive傳輸。兩台裝置只需在同一Wi-Fi網路上即可。
{{% /details %}}

{{% details title="傳輸需要多長時間？" closed="true" %}}
傳輸時間取決於音樂庫的大小和Wi-Fi速度。幾個GB的典型庫透過標準家庭網路傳輸需要5-15分鐘。
{{% /details %}}
