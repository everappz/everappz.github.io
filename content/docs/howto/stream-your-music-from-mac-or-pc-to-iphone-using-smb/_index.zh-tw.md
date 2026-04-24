---
title: "使用SMB從Mac或PC串流音樂到iPhone"
description: "了解如何使用Evermusic和SMB協議從Mac或Windows PC向iPhone或iPad串流您的音樂收藏。一個簡單的逐步指南，無需同步即可連接和享受音訊。"
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["從Mac串流音樂到iPhone", "SMB音訊串流iOS", "Evermusic SMB設定", "連接PC音樂iPhone", "Mac音樂分享iOS", "SMB Windows檔案串流", "Evermusic PC資料夾存取"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**簡要說明：** 使用Evermusic應用程式透過SMB在本地網路上從Mac或Windows PC向iPhone或iPad串流音樂。無需同步，無需複製——只需在電腦上啟用檔案共享，在應用程式中連接並播放。設定不到5分鐘。

您是否淹沒在MAC或PC上的音樂海洋中，想要在iPhone或iPad上輕鬆享受它們？Evermusic就是您的最佳選擇。使用Evermusic，透過SMB協議連接您的電腦並串流您喜愛的音樂非常簡單，無需擔心佔用額外的裝置空間或處理同步問題。以下是入門的逐步指南：

## 第1步：在電腦上啟用SMB協議

![Evermusic - SMB支援 - Mac共享畫面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### 如果您使用MAC

- 開啟系統偏好設定 -> 共享。
- 啟用檔案共享服務。
- 在「共享資料夾」部分，新增您的音樂資料夾，選擇使用者並設定權限等級（讀寫或唯讀）。
- 為方便起見，您可以為音樂資料夾選擇「所有人：唯讀」，使其在Evermusic中輕鬆存取。
- 別忘記記住您電腦的URL（smb://192.168.xx.xx）以用於下一步。

![Evermusic - SMB支援 - 檔案共享畫面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- 點擊「選項」並啟用「使用SMB共享檔案和資料夾」。
- 為可用帳號啟用「Windows檔案共享」。

![Evermusic - SMB支援 - 共享檔案和資料夾畫面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### 如果您使用Windows PC

![Evermusic - SMB支援 - 在Windows上共享檔案](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- 右鍵點擊您的音樂資料夾。
- 選擇「內容」。
- 開啟「共享」索引標籤。
- 點擊「共享...」
- 選擇要共享的人員並設定他們的權限等級。
- 與MAC一樣，您可以為所選音樂資料夾選擇「所有人：讀取」。
- 點擊「完成」儲存設定。

![Evermusic - SMB支援 - Windows上的共享資料夾](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## 第2步：自動新增您的電腦

- 現在，開啟Evermusic並前往「連接」索引標籤（如果您使用舊版應用程式，則為「網路」）。
- 如果您在「可用設備」（如果您使用舊版應用程式，則為「可用共享」）部分看到您的電腦，並且在上一步中選擇了「所有人：唯讀」，只需點擊您的電腦，它將自動連接。
- 如果沒有發生，您可以手動新增電腦。

![Evermusic - SMB支援 - 連接帳號畫面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## 第3步：手動新增您的電腦

- 點擊「連接雲端服務」（如果您使用舊版應用程式，則為「新增帳號」）
- 在下一個畫面上從可用伺服器清單中選擇「SMB」。
- 在「SMB」設定畫面上：
  - 輸入帶有共享資料夾路徑的伺服器URL。您可以輸入伺服器名稱或伺服器IP。例如：
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - 輸入您的登入名稱和密碼，或者如果您在上一步中選擇了「所有人：唯讀」，則將這些欄位留空。
  - 「WORKGROUP」欄位是選填的，如果您有Active Directory網域則應使用。

![Evermusic - SMB支援 - 輸入憑證畫面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

連接SMB帳號後，它將出現在「雲端服務」（「帳號」）部分。點擊開啟已連接的帳號，導航到音樂資料夾，然後點擊任何音訊檔案以啟動播放器。

![Evermusic - SMB支援 - 開啟已連接資料夾畫面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

使用Evermusic在iPhone或iPad上無縫享受您的音樂收藏。

![Evermusic - SMB支援 - 音訊播放器畫面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## 第4步：SMB2解決方案

如果您在瀏覽資料夾或播放包含特殊字元（如ü、ö、é）的檔案時遇到問題，這可能與SMB2協議有關。我們正在積極解決這個問題。

作為臨時解決方案，請嘗試在伺服器和應用程式設定中啟用SMB 1。或者，您可以使用系統檔案開啟選單連接到SMB伺服器。方法如下：

1. 導航到「本機檔案」。
2. 向下捲動到「此裝置上的檔案」部分，然後點擊「開啟檔案...」或「開啟資料夾...」
3. 找到您的伺服器並選擇所需的檔案或資料夾。
4. 點擊「開啟」確認選擇。

## 第5步：WebDAV解決方案

此外，如果支援，您可以嘗試使用WebDAV或DLNA協議連接到NAS。

按照這些步驟，您可以繞過與檔案名稱中特殊字元相關的問題，繼續享受您的媒體檔案。

附註：您還可以使用iTunes檔案共享將音訊檔案從MAC/PC傳輸到iPhone，並播放本機音訊檔案。在我們的指南中了解有關此功能的更多資訊：[如何在iPhone上播放iTunes檔案](/docs/howto/how-to-play-local-itunes-files-on-my-iphone)。

## 常見問題

{{% details title="我可以不用iTunes從PC串流音樂到iPhone嗎？" closed="true" %}}
可以。Evermusic透過本地Wi-Fi網路上的SMB連接到您的PC。不需要iTunes。只需在PC上啟用檔案共享並在應用程式中連接。
{{% /details %}}

{{% details title="SMB串流使用行動數據嗎？" closed="true" %}}
不。SMB透過本地Wi-Fi網路運作。不需要網際網路連接或行動數據。
{{% /details %}}

{{% details title="Evermusic透過SMB支援哪些音訊格式？" closed="true" %}}
Evermusic支援MP3、FLAC、AAC、WAV、AIFF、OGG、WMA、ALAC和其他常見音訊格式。檔案直接從SMB共享播放。
{{% /details %}}

{{% details title="我可以從NAS串流音樂到iPhone嗎？" closed="true" %}}
可以。如果您的NAS支援SMB（大多數支援，包括Synology、QNAP和WD My Cloud），您可以使用本指南中的相同步驟進行連接。
{{% /details %}}

{{% details title="串流時需要保持電腦開機嗎？" closed="true" %}}
是的。由於Evermusic直接從電腦串流檔案，電腦必須開機並連接到與iPhone相同的網路。
{{% /details %}}

{{% details title="SMB串流有檔案大小限制嗎？" closed="true" %}}
沒有。Evermusic透過SMB串流任何大小的檔案。大型無損檔案（FLAC、WAV）可以正常運作。
{{% /details %}}
