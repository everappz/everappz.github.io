---
title: "使用SMB協議將檔案從電腦傳輸到iPhone"
description: "了解如何使用Evermusic和SMB協議將大型檔案從Mac或Windows PC傳輸並存取到iPhone或iPad。無縫串流和檔案管理的逐步指南。"
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["傳輸檔案到iPhone SMB", "在iPhone上串流PC音樂", "Mac連接iPhone SMB", "Evermusic SMB設定", "存取電腦檔案iPhone", "Windows音樂共享iOS", "SMB檔案傳輸Evermusic"]
---

{{< author-byline >}}


**摘要：** 在iPhone或iPad上使用Evermusic，透過SMB在本地網路上存取儲存在Mac或Windows PC上的檔案。無需傳輸線、無需iTunes、無需上傳到雲端。在電腦上啟用檔案共享，在應用程式中連接，即可無線瀏覽或播放檔案。

您的MAC或PC上是否有大量檔案，想要從iPhone或iPad輕鬆存取？我們的應用程式提供了簡單的解決方案。

按照以下步驟，使用SMB協議在電腦和iOS裝置之間實現無縫存取：

## 步驟1：在電腦上啟用SMB協議

**對於MAC：**

1. 在MAC上開啟「系統偏好設定」。
2. 點選「共享」。
3. 啟用「檔案共享」服務。
4. 將音樂資料夾新增到「共享資料夾」區段。新增使用者並選擇權限等級（讀寫或唯讀）。您可以為新增的音樂資料夾選擇「所有人：唯讀」。

   ![Mac設定畫面](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. 記住電腦URL（smb://192.168.xx.xx），因為您將在下一步中使用它。
6. 點選「選項」並啟用「使用SMB共享檔案和資料夾」。

   ![Mac檔案共享畫面](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. 為可用帳戶啟用「Windows檔案共享」。

   ![Mac SMB共享畫面](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**對於Windows PC：**

1. 右鍵點選音樂資料夾。
2. 選擇「內容」。
3. 導覽到「共用」索引標籤。
4. 點選「共用...」
5. 選擇要與之共享資料夾的人員並指定權限等級。您可以為選擇的音樂資料夾選擇「所有人：讀取」。

   ![Windows SMB共享畫面](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. 點選「完成」。
7. 在「檔案共享」視窗中點選「完成」，並記住資料夾路徑。

   ![Windows SMB共享資料夾](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## 步驟2：連接iOS裝置

1. 在iPhone或iPad上開啟應用程式。
2. 前往「連接」索引標籤。

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic連接畫面"
  caption="Evermusic連接畫面"
  width="400"
>}}

*如果您的電腦出現在「可用設備」區段：*

如果您的電腦在「可用設備」區段可見，且您在上一步中選擇了「所有人：唯讀」，只需點按您的電腦即可自動連接。

*如果您的電腦沒有自動出現：*

1. 點按「連接雲端服務」。
2. 在「連接雲端服務」畫面中選擇「SMB」。

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic連接雲端服務畫面"
  caption="Evermusic連接雲端服務畫面"
  width="400"
>}}

3. 在「SMB連接」畫面中，輸入伺服器URL和共享資料夾路徑。您可以使用伺服器名稱或伺服器IP：

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. 輸入您的使用者名稱和密碼，或者如果您在上一步中選擇了「所有人：唯讀」，則將這些欄位留空。
5. 「WORKGROUP」欄位是選填的，如果您有Active Directory Domain則應使用。

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMB連接器畫面"
  caption="Evermusic SMB連接器畫面"
  width="400"
>}}

6. 使用SMB協議連接電腦後，它將出現在「連接」畫面的「雲端服務」區段。
7. 開啟已連接的服務並導覽到所需資料夾。

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="在Evermusic中開啟的SMB資料夾"
  caption="在Evermusic中開啟的SMB資料夾"
  width="400"
>}}

8. 您可以使用內建檔案管理器根據需要編輯檔案。

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic檔案管理器"
  caption="Evermusic檔案管理器"
  width="400"
>}}

## 步驟3：包含特殊字元的SMB2資料夾解決方案

使用SMB2協議時，有時可能會遇到包含特殊字元的資料夾問題。以下是解決此問題的步驟：

1. **啟用SMB 1：**  
   • 作為臨時解決方案，嘗試在伺服器和應用程式設定中啟用SMB 1。這可以幫助繞過與資料夾名稱中特殊字元相關的問題。

2. **使用系統檔案開啟選單：**  
   • 導覽到「本機檔案」。  
   • 向下捲動到「此裝置上的檔案」區段。  
   • 點按「開啟檔案...」或「開啟資料夾...」。  
   • 找到您的伺服器並選擇所需的檔案或資料夾。  
   • 點按「開啟」確認您的選擇。

3. **替代協議：**  
   • 如果問題持續存在，請考慮使用WebDAV或DLNA協議連接到NAS（如果您的NAS支援這些選項）。這些協議可能更好地處理特殊字元。

按照這些步驟，您可以減輕使用SMB2協議時資料夾名稱中特殊字元的問題。

## 結論

透過這些步驟，您可以使用我們的應用程式輕鬆地從MAC或PC在iPhone或iPad上存取大量檔案。

## 常見問題

{{% details title="我可以不用iTunes從iPhone存取PC上的檔案嗎？" closed="true" %}}
可以。Evermusic透過本地Wi-Fi網路上的SMB連接到您的電腦。不需要iTunes或Finder同步。在PC上啟用檔案共享，直接從應用程式連接即可。
{{% /details %}}

{{% details title="SMB檔案存取可以透過網際網路運作嗎？" closed="true" %}}
不可以。SMB是本地網路協議。您的iPhone和電腦必須在同一個Wi-Fi網路上。要遠端存取，請將檔案上傳到Google Drive或Dropbox等雲端服務，然後在Evermusic中連接。
{{% /details %}}

{{% details title="我可以透過SMB存取哪些檔案類型？" closed="true" %}}
Evermusic支援MP3、FLAC、AAC、WAV、AIFF、OGG、WMA、ALAC和其他音訊格式。您還可以使用內建檔案管理器瀏覽和管理非音訊檔案。
{{% /details %}}

{{% details title="我可以使用SMB將檔案從NAS傳輸到iPhone嗎？" closed="true" %}}
可以。大多數NAS裝置（Synology、QNAP、WD My Cloud等）都支援SMB。使用本指南中的相同步驟連接到您的NAS。
{{% /details %}}

{{% details title="我需要將檔案複製到iPhone才能播放嗎？" closed="true" %}}
不需要。Evermusic透過網路直接從您的電腦或NAS串流檔案。除非您選擇下載檔案進行離線播放，否則檔案不會複製到iPhone。
{{% /details %}}

{{% details title="SMB檔案共享安全嗎？" closed="true" %}}
SMB檔案共享僅在本地網路上運作。其他網路上的裝置無法存取您的共享資料夾。為了額外安全，請使用使用者名稱和密碼而不是匿名（所有人）存取。
{{% /details %}}
