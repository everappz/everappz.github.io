---
title: "如何從Evermusic、Flacbox、Evertag連接Bluesound VAULT的內部儲存"
date: 2022-03-10
description: "了解如何使用SMB協定從Evermusic、Flacbox和Evertag存取Bluesound VAULT的內部硬碟，以管理、編輯和播放音訊檔案。"
keywords: ["bluesound vault", "連接smb儲存", "evermusic smb", "flacbox vault", "evertag smb", "nas儲存音樂", "vault內部磁碟機"]
tags: ["evermusic", "連接", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**摘要：** 使用Evermusic、Flacbox或Evertag透過SMB連接到Bluesound VAULT的內部儲存。在BluOS應用程式中找到VAULT的IP位址，將其作為SMB連接輸入並使用訪客存取，然後開始播放或管理您的音樂檔案。

Bluesound VAULT擁有內部硬碟，可作為網路附加儲存（NAS）使用。存取VAULT的內部硬碟可以讓您從我們的應用程式Evermusic、Flacbox、Evertag中新增/刪除檔案、編輯中繼資料標籤。

**以下是存取VAULT內部硬碟的步驟：**

1. 在BluOS應用程式中，選擇**說明 > 診斷**。

2. 從**診斷**頁面取得VAULT的**IP位址**。此**IP位址**將在後續步驟中使用。

3. 開啟Evermusic、Flacbox或Evertag。

   ![Everappz應用程式](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. 開啟「連接」畫面，選擇「連接雲端服務」選單項目。

   ![Evermusic連接畫面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. 選擇「SMB」雲端服務。

   ![Evermusic連接雲端服務畫面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. 在「SMB設定畫面」中按以下格式輸入URL：

   ```
   SMB://<<VAULT-IP>>
   ```

   將`<<VAULT-IP>>`替換為步驟2中取得的**IP位址**。

   **注意：** 將登入和密碼欄位留空，因為VAULT儲存支援訪客（GUEST）模式。

   ![Evermusic SMB連接畫面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. 點擊「登入」按鈕儲存設定。

8. 開啟已連接的雲端儲存，瀏覽至包含音訊檔案的資料夾，點擊任意檔案啟動音訊播放器。

   ![Evermusic已開啟的SMB伺服器畫面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. 您還可以使用內建檔案管理員編輯檔案。

   ![Evermusic檔案管理員畫面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

透過這些簡單的步驟，您可以輕鬆存取Bluesound VAULT的內部硬碟，並使用Evermusic、Flacbox或Evertag控制您的音樂庫。

## 常見問題

{{% details title="連接Bluesound VAULT需要使用者名稱和密碼嗎？" closed="true" %}}
不需要。Bluesound VAULT支援透過SMB進行訪客（匿名）存取。設定連接時將登入和密碼欄位留空即可。
{{% /details %}}

{{% details title="我可以在Bluesound VAULT上編輯音樂標籤嗎？" closed="true" %}}
可以。使用Evertag，您可以編輯直接儲存在VAULT內部硬碟上的音訊檔案的中繼資料標籤（標題、藝術家、專輯等）。
{{% /details %}}

{{% details title="Bluesound VAULT支援哪些協定？" closed="true" %}}
Bluesound VAULT透過SMB（Server Message Block）公開其內部儲存。Evermusic、Flacbox和Evertag都支援SMB連接，使連接變得簡單。
{{% /details %}}

{{% details title="我可以在不將檔案複製到iPhone的情況下從VAULT串流音樂嗎？" closed="true" %}}
可以。透過SMB連接後，您可以直接從VAULT的內部磁碟機串流音訊檔案，無需將其複製到您的裝置。
{{% /details %}}
