---
title: "逐步指南：將 iCloud 資料庫匯入 Evermusic 和 Flacbox"
description: "了解如何在 Evermusic 和 Flacbox 中同步和串流 iCloud 音樂資料庫。本指南介紹了串流、元資料讀取和離線同步的最佳實踐。"
date: 2024-11-14
readingTime: 7
tags: ["音樂", "雲端", "串流", "同步", "icloud", "資料庫"]
keywords: ["匯入 iCloud 音樂 Evermusic", "Flacbox iCloud 同步", "Evermusic 從 iCloud 串流", "音樂資料庫 iOS 應用", "Flacbox 元資料讀取器", "iCloud 音樂串流 iPhone"]
---

{{< author-byline >}}


**摘要：** 您可以在 Evermusic 和 Flacbox 中串流 iCloud Drive 音樂資料庫，無需將檔案下載到裝置。在應用程式中連接 iCloud Drive，啟用線上音樂同步來建立資料庫，設定元資料讀取器按藝術家/專輯/類型整理，並可選擇啟用離線模式下載專輯以便在沒有網路的情況下聆聽。這些步驟也適用於 Google Drive、Dropbox、OneDrive 和其他支援的雲端服務。

如何將 iCloud 音樂資料庫與 Flacbox 和 Evermusic 同步以實現流暢播放。最近，我們的一位訂閱者就一個常見問題聯繫了 Everappz 支援團隊：

> "您好 Flacbox 支援團隊，我最近訂閱了 Flacbox 一年，但在正確同步 iCloud 中的音樂方面遇到了很大困難。我的 iCloud 中儲存了大約 60 張各種原聲專輯，我想將它們整合到應用程式中。然而，匯入 Flacbox 資料庫的過程似乎並不像我希望的那樣順暢。即使載入一張專輯到應用程式中也需要非常長的時間。昨天，我花了幾個小時嘗試不同的方法來高效匯入專輯，但沒有找到滿意的解決方案。我希望能獲得任何指導或逐步指南，了解如何匯入 iCloud 音樂（不在 iPhone 上本地儲存）而不會導致過長的載入時間。"

對於許多在 iCloud 中擁有大量音樂資料庫的使用者來說，將檔案整合到 Flacbox 和 Evermusic 中有時會面臨挑戰，特別是在同步速度和效率方面。如果您遇到了類似的問題，本指南將引導您了解簡化匯入流程、最小化載入時間和輕鬆享受音樂的最佳實踐。在本指南中，我們將使用 iCloud 儲存，但這些步驟也適用於應用程式支援的任何其他雲端服務。您將在本指南中看到 Mac 截圖，但在 iPhone 上，畫面和功能位置相同。

## 匯入您的 iCloud 資料庫

首先開啟 [iCloud.com](https://icloud.com) 並建立 Music 資料夾來整理您的資料庫。使用電腦操作更簡單，因為網站支援拖放。

![iCloud Music 資料夾](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_141e817570c34e6a8c528b65a99a5ba4~mv2.png)

等待所有檔案完全上傳到 iCloud 後再繼續。

![iCloud 上傳](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_6f9f363bd64e4ca58190541fcc1ed28e~mv2.png)

開啟應用程式並導覽至 **連接** 部分。點擊 **連接雲端服務** 並選擇 **iCloud Drive**。在下一個畫面上點擊 **選擇資料夾**。在左側面板中選擇 **iCloud Drive**，導覽至 Music 資料夾並點擊 **開啟**。

![連接部分](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_ccfbcec8308d4974b630bd1a0868dfd4~mv2.png)

雲端資料夾新增到應用程式後，將出現在 **連接** 部分。點擊已連接雲端資料夾中的任何檔案啟動音訊播放器——應用程式將串流檔案而不下載。

![音訊播放器](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_27d2d6ec37c648fdb7e84e82d52eb38b~mv2.png)

要將檔案新增到音樂資料庫，開啟 **音樂資料庫** 畫面。點擊 **更多操作** 按鈕並選擇 **設定**。重點關注 **線上音樂同步**。啟用此功能並點擊 **同步線上資料夾** 選擇資料夾。點擊 **完成** 確認。

![線上音樂同步](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_cc7a80af9d394d57979549b0a5b9c91d~mv2.png)

啟用 **背景同步** 後，應用程式即使在背景執行也會繼續掃描。點擊 **開始同步**。

## 元資料讀取

前往 **音樂資料庫設定** 並點擊 **元資料讀取**。

![元資料讀取](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_a74acfe948934fa48913bfcd8450b3ab~mv2.png)

**可用模式：** 停用、目前歌曲、音訊播放器佇列、音樂資料庫。

**重要**，元資料讀取器僅更新音樂資料庫中的元資料，不會變更雲端帳戶或本地儲存中的檔案。

**重新加載元數據** 操作將標記所有檔案為缺少元資料以觸發更新。

## 離線音樂同步

離線存取的兩個選項：

1. **下載** 操作下載整個資料夾內容。
2. **離線模式** ——應用程式定期檢查雲端資料夾並自動下載新檔案。

點擊 **更多操作** 並選擇 **啟用離線模式**。

![啟用離線模式](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_f77314386cab41349e0140311515f9f1~mv2.png)

下載的檔案出現在 **本地檔案 - 離線資料夾** 部分。在 **同步離線資料夾** 部分可以管理離線同步。

![同步離線資料夾](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_bb941f44ec994437a05fc3bcdd121c91~mv2.png)

**重要：** 建議定期啟動離線音樂同步以保持音樂資料庫更新。

今天就到這裡！希望本指南幫助您設定雲端伺服器和裝置之間的同步。

## 常見問題

{{% details title="我可以不下載檔案到 iPhone 就串流 iCloud 音樂嗎？" closed="true" %}}
可以。連接 iCloud Drive 並使用線上音樂同步後，應用程式建立到雲端檔案的連結並按需串流。除非您明確啟用離線模式，否則檔案不會被下載。
{{% /details %}}

{{% details title="為什麼 iCloud 音樂匯入很慢？" closed="true" %}}
匯入慢通常是因為透過行動連線讀取大型資料庫的元資料。啟用背景同步並考慮使用 Mac 版本。
{{% /details %}}

{{% details title="本指南適用於 iCloud 以外的雲端服務嗎？" closed="true" %}}
適用。相同步驟適用於 Google Drive、Dropbox、OneDrive、SMB、WebDAV 和所有其他支援的雲端服務。
{{% /details %}}

{{% details title="如何將音樂資料庫從 Mac 傳輸到 iPhone？" closed="true" %}}
使用應用程式設定中的資料備份/還原功能。先在 Mac 版本上同步和讀取元資料，建立備份，然後在 iOS 版本上還原。
{{% /details %}}

{{% details title="元資料讀取器會變更我的原始音訊檔案嗎？" closed="true" %}}
不會。元資料讀取器僅更新音樂資料庫中的顯示資訊。要編輯檔案標籤，請使用內建標籤編輯器。
{{% /details %}}

{{% details title="如何使專輯可離線使用？" closed="true" %}}
點擊雲端資料夾上的 **更多操作** 並選擇 **啟用離線模式**。應用程式下載所有檔案並自動保持與雲端版本同步。
{{% /details %}}
