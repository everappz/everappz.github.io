---
title: "Evertag 4.2:全新雲端連線,標籤編輯器設定詳解"
date: 2026-05-09
description: "Evertag 4.2 新增對 Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP 與 NFS 的連線,刷新 Wi-Fi Drive 並讓介面對齊 Liquid Glass。本文也逐項說明標籤編輯器的所有設定 — 包含 ID3v2.4 與 ID3v2.3、專輯封面縮放、標籤複製、雲端上傳模式,以及為 Spotify 等串流服務準備檔案時要選擇的正確選項。"
keywords: ["Evertag 4.2", "Evertag 更新", "ID3 標籤編輯器 iPhone", "ID3v2.4 vs ID3v2.3", "FLAC 標籤編輯 iOS", "MP3 標籤編輯 iPhone", "專輯封面編輯 iOS", "Spotify 標籤編輯器", "Plex 標籤編輯器", "Apple Music 標籤編輯器", "Evertag 雲端標籤編輯器", "Internxt 標籤編輯器", "Proton Drive 標籤編輯器", "QNAP 標籤編輯器", "Nextcloud 標籤編輯器", "Amazon S3 標籤編輯器", "SFTP 標籤編輯器 iPhone", "FTP 音訊標籤編輯器", "NFS 標籤編輯器 iPhone", "Wi-Fi Drive 標籤編輯器", "ID3 標籤複製", "專輯封面縮放", "Liquid Glass 設計", "音訊中繼資料編輯器 iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "標籤編輯器", "ID3", "ID3v2.4", "ID3v2.3", "FLAC 標籤", "MP3 標籤", "專輯封面", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "新功能"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**重點:** [Evertag 4.2](/products/evertag) 是 iPhone、iPad 與 Mac 上音訊標籤編輯器的重大更新。我們處理了關鍵的標籤編輯錯誤,並新增 6 項以上的雲端與伺服器連線 — **Internxt**、**Proton Drive**、**QNAP**、**Nextcloud**、**Amazon S3**,以及 **FTP**、**SFTP** 和 **NFS** 通訊協定。Wi-Fi Drive 擁有煥然一新的介面、多選模式、更聰明的上傳佇列與更快的傳輸速度。整個應用程式都已對齊 **Liquid Glass** 設計。本文也深入說明 Evertag 的標籤編輯器設定 — 講清楚 **ID3v2.4 與 ID3v2.3**、**專輯封面縮放**、**標籤複製**、**雲端上傳模式**、**已下載檔案的刪除**,以及為 **Spotify**、**Apple Music**、**Plex**、**Jellyfin** 或其他串流服務準備音訊時應選哪一項。

---

## 大家好!

Evertag 的一項重大更新到了。我們處理了關鍵的標籤編輯錯誤,並新增 **6 項以上的雲端與伺服器連線**,讓管理音訊中繼資料比以往更輕鬆 — 不論你的曲庫放在重視隱私的雲端、自架的 NAS,或一般 FTP/SFTP/NFS 伺服器上。

[從 App Store 下載 Evertag 4.2](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611),或從你目前的版本進行更新。

## 擴大的雲端與伺服器支援

Evertag 現在原生連線到更廣泛的雲端與自架儲存選項。不論檔案放在哪裡,都能編輯 ID3、MP4、FLAC、OGG 與 APE 標籤。

### 重視隱私的雲端儲存:Internxt 與 Proton Drive

如果你重視端對端加密與零知識儲存,兩個最受推崇的隱私導向雲端如今已成為 Evertag 的原生選項:

- **Internxt** — 來自西班牙的開源、後量子加密、符合 GDPR 的雲端服務。提供免費方案。
- **Proton Drive** — 由 Proton Mail 與 Proton VPN 團隊打造、總部位於瑞士的端對端加密儲存空間。提供免費方案,以及供更大資料庫使用的付費方案。

你現在可以直接編輯這兩種服務上儲存的音訊檔案中繼資料 — 檔案在傳輸過程中保持加密,只有新標籤會被寫回。

### 自架解決方案:QNAP、Nextcloud、Amazon S3

適合自行管理基礎架構的使用者:

- **QNAP** — 透過原生 API 連線至 QNAP NAS 裝置。透過本機 Wi-Fi 或遠端存取編輯 QNAP 上檔案的標籤。
- **Nextcloud** — 連線到任何自架或代管的 Nextcloud 執行個體。
- **Amazon S3** — 將 Evertag 指向任何 S3 儲存桶(或 Backblaze B2、Wasabi、MinIO、Cloudflare R2 等 S3 相容儲存),即可就地編輯中繼資料。

### 全新的網路通訊協定:FTP、SFTP、NFS

對於使用自訂伺服器、家庭實驗室或缺乏精緻行動 App 的通用 NAS 的使用者,Evertag 4.2 新增了三種經典通訊協定:

- **SFTP(SSH 檔案傳輸協定)** — 這是 **從自己的伺服器進行安全遠端標籤編輯** 的正確選擇。SFTP 在 SSH 之上執行,因此整個傳輸(身分驗證與音訊資料)都會被加密。如果你擁有 VPS、專屬伺服器,或家中具備 SSH 存取權的 Linux 機器,可以編輯遠端檔案的標籤,而不必暴露任何其他內容。支援密碼及金鑰驗證。
- **FTP** — 長期以來確立的檔案傳輸標準。對於提供 FTP 但沒有原生 API 整合的較舊家用 NAS 很有用。
- **NFS(網路檔案系統)** — Linux 與大多數 NAS 裝置上事實上的分享通訊協定。在相同硬體上,NFS 的負擔比 SMB 更小。

> **提示:** 想透過開放網際網路進行遠端編輯時,SFTP 是最佳選擇。FTP 與 NFS 比較適合在區域網路內使用 — 除非以 VPN 包覆,否則別把它們暴露在網際網路。

## Wi-Fi Drive 升級

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) 是 Evertag 內建的功能,用於在電腦與 iPhone 或 iPad 之間無線傳輸音訊檔案 — 不需要 iTunes、傳輸線或雲端帳號。兩台裝置必須位於相同的 Wi-Fi 網路。

在 Evertag 4.2 中,Wi-Fi Drive 加入了:

- **煥然一新的現代介面** — 更整潔、更易於一目了然,並對齊 Liquid Glass。
- **多選模式** — 選取多個檔案或資料夾,執行批次操作。
- **更聰明的上傳佇列** — 進度回饋更清楚,更能承受網路波動。
- **整體速度與可靠性提升** — 大型資料庫的傳輸更快。

這是不依賴第三方服務,將一批音訊檔案從電腦搬到手機、編輯標籤後再送回的最快方式。

## 標籤編輯器設定:深入解說

這是大多數使用者從不閱讀的部分 — 但它決定了你的標籤是在所有 App 都能運作,還是只能在某些 App 中。開啟 Evertag,然後進入 **音訊標籤編輯器設定** 區。下面說明每個選項的實際作用,以及依目的應該選擇哪一項。

### 專輯封面縮放

當你將專輯封面儲存到音訊檔案時,Evertag 可以在嵌入前縮放影像。可用選項:

- **小** — 對檔案大小影響最小,影像品質較低。
- **中** — 對大多數使用者而言均衡的選擇。
- **大** — 高品質,適合大螢幕播放器與 CarPlay。
- **特大** — 非常高品質,檔案大小明顯增加。
- **原始(已停用)** — 以原始解析度嵌入。**完全不縮放。**

**為什麼這很重要:**

- **品質越高 = 檔案越大。** 一張 3,000 × 3,000 像素的封面每首歌可能多出數 MB。乘上整張專輯,磁碟用量很快累積。
- **某些播放器對非常大的嵌入影像處理得不好。** 較舊裝置、某些車用主機,以及一些舊版桌面播放器,在 ~1,500 px 以上的封面可能卡住或拒絕顯示。
- **對大多數雲端與串流流程**,**中** 或 **大** 是最佳折衷。只有當你需要封存品質,或為信任能正確處理的播放器準備檔案時才使用 **原始**。

> **原始** 尺寸選項屬於 Evertag 進階個人化升級的一部分。標準尺寸(小/中/大/特大)免費。

### 標籤儲存選項:ID3v2.4 vs ID3v2.3

這是相容性最重要的單一設定。ID3v2 是 MP3 檔案內使用的中繼資料格式。兩個被廣泛使用的版本之間有細微但重要的差異。

#### ID3v2.4

- 較新,支援 **UTF-8 文字編碼** — 能正確處理非拉丁文字(中文、俄文、日文、阿拉伯文、希伯來文等)。
- 更多框架類型(相對音量、等化器預設等)。
- **建議在支援它的現代播放器** 中使用。

#### ID3v2.3

- 較舊,但 **獲得最普遍支援** 的 ID3 版本。
- 不直接支援 UTF-8(對 Unicode 文字使用 UTF-16)。
- **當你需要與較舊播放器、車載音響和某些桌面 App 取得最大相容性時建議使用**。

#### 在 Evertag 中何時開啟 ID3v2.4

- 你使用 Evermusic、Plex、Jellyfin、Navidrome、foobar2000、VLC、Apple Music(目前版本)或現代 Android 播放器等 **現代音訊播放器**。 ✅ **開啟 ID3v2.4。**
- 你的資料庫包含 **非拉丁字元**(中文、韓文、日文、俄文、阿拉伯文、希臘文、希伯來文)。 ✅ **開啟 ID3v2.4** — UTF-8 處理這些字元更乾淨。

#### 在 Evertag 中何時關閉 ID3v2.4(改用 ID3v2.3)

- 你正為不讀取 v2.4 標籤的 **較舊車載音響或儀表板主機** 準備檔案。
- 編輯後在某些 App 看到 **亂碼或缺失的標籤** — 這強烈表示那裡不支援 v2.4。回到 v2.3。
- 你瞄準 **舊版桌面播放器** 或更舊的可攜式播放器(早期 iPod、2000–2010 年代的某些 MP3 播放器)。

> **經驗法則:** 如果你的標籤在所有地方都用 v2.4 顯示正確,就保持開啟。如果即使一個重要播放器顯示錯誤字元、空白或讀取失敗,關閉 v2.4 並重新儲存。

#### 標籤複製

啟用 **標籤複製** 後,Evertag 會將通用中繼資料欄位(標題、藝人、專輯等)同時寫入檔案的 **ID3v1 與 ID3v2 兩個區段**。這能改善與只讀取 ID3v1(檔案末端原本的 128 位元組標籤)的非常老舊播放器之間的相容性。

- **大多數使用者不需要此項。** 現代播放器優先讀取 ID3v2。
- **只在** 處理古董硬體或忽略 ID3v2 的特定軟體時才啟用。

### 更新線上檔案:Evertag 如何處理雲端編輯

當你在已連線雲端(Google Drive、Dropbox、OneDrive、iCloud、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、SFTP 等)上的檔案上編輯標籤時,Evertag 必須把修改後的檔案重新上傳。你來掌控如何處理:

- **顯示確認訊息** *(預設,建議)* — Evertag 在上傳前會詢問。最適合謹慎的使用者與共用資料庫。
- **自動更新檔案中繼資料** — 每次編輯後安靜地上傳。最適合連線穩定快速、且常常編輯的單人使用者。
- **不更新檔案中繼資料** — Evertag 只編輯本機副本。當你想要在不同步到雲端的情況下預覽標籤變更時很有用。

### 編輯線上檔案:本機檔案清理

要編輯遠端檔案,Evertag 會先把它下載到裝置。編輯後,你選擇本機副本要怎麼處理:

- **永遠刪除已下載檔案** — Evertag 在編輯後移除暫存檔案。如果你儲存空間吃緊或正在處理他人檔案,**建議**。
- **不刪除已下載檔案** — 將編輯後的檔案保留在裝置。當你既要離線副本,也要更新後的雲端副本時很有用。

### 主畫面上的按鈕

Evertag 的標籤編輯器主畫面可以顯示或隱藏個別操作的按鈕。只啟用你實際會使用的按鈕,讓介面保持聚焦:

- **自動搜尋音訊標籤** — 依檔案的音訊指紋線上找出缺少的中繼資料。
- **手動搜尋音訊標籤** — 自動搜尋失準時,以標題/藝人搜尋。
- **搜尋專輯封面** — 找到並嵌入高品質封面。
- **儲存專輯封面** — 將內嵌封面匯出至照片圖庫或檔案。
- **正規化編碼** — 修正由舊編碼造成的亂碼非拉丁文字(對使用舊版軟體擷取的西里爾、中、日文歌曲特別有用)。
- **刪除音訊標籤** — 從檔案清除所有標籤。在重新打標籤前很有用。

### 顯示延伸標籤

切換此項以顯示超出基本 標題/藝人/專輯/年份 的所有中繼資料欄位 — 包括 BPM、指揮、原始藝人、心情、版權、編碼器、留言、歌詞等。進階功能;一般使用者多半不需要。

### 同時編輯檔案

啟用後,Evertag 讓你 **跨多個選取檔案同時** 編輯中繼資料 — 一次操作就能為整張專輯設定相同的 album artist、年份或類型。整理大型雜亂資料庫的最快方式。

## 為 Spotify、Apple Music 與串流平台編輯標籤

常見問題:「我在 Evertag 編輯了標籤、上傳了檔案,但串流服務顯示的中繼資料是錯的。怎麼回事?」

簡短回答:**串流服務不一定會採用你的本機標籤。** Apple Music 與 Spotify 都有自己的內部資料庫 — 當它們辨識到一首歌曲時,會以自家中繼資料覆蓋顯示。但對於 **上傳的檔案**、本機檔案(Apple Music 的「資料庫」功能、Spotify Local Files),以及 **透過代理商上傳到串流平台** 的內容,你的標籤絕對重要。下面是各情境下 Evertag 的設定方式:

### 為 Apple Music 準備檔案(Cloud Music Library / iTunes Match)

- **ID3v2.4: 開** — Apple Music 正確處理 UTF-8。
- **專輯封面: 大** — Apple 的 App 會把大封面顯示得很好;原始尺寸過頭。
- **標籤複製: 關** — 不需要。
- 確認 **Album Artist** 已正確填入 — Apple Music 用它來分組。

### 為 Spotify Local Files 準備檔案

Spotify Local Files 只顯示標籤良好的檔案。Spotify 讀取的標籤有限。

- 大多數情況 **ID3v2.4: 開**。如果某首歌編輯後在 Spotify 中無法正確顯示,**試著以 ID3v2.4: 關 儲存**(亦即 ID3v2.3) — Spotify 的剖析器歷史上對 v2.4 較保守。
- **專輯封面: 中或大** — Spotify 反正會把封面縮小。
- 至少填入 **標題**、**藝人**、**專輯** 與 **曲目編號**。

### 為代理商上傳準備檔案(DistroKid、TuneCore、CD Baby 等)

如果你是把自己作品上傳到串流平台的藝人,代理商通常會讀取標籤,但也會在自己介面要求填寫中繼資料。無論哪種:

- **ID3v2.3** 通常是更安全的預設值 — 許多代理商管線多年前建置,偏好較舊的格式。
- 嵌入 **大** 尺寸封面(大多數代理商要求 ≥ 1,400 × 1,400 px 的封面 — 請查看其指南)。
- 不要倚賴延伸標籤 — 代理商只讀取核心欄位。

### 為 Plex、Jellyfin、Navidrome、Subsonic、Emby 準備檔案

這些自架媒體伺服器非常寬容。它們會乾淨地讀取 v2.3 與 v2.4,並能很好地處理 UTF-8。

- **ID3v2.4: 開** 即可。
- **專輯封面: 大** 或 **特大** — 這些伺服器會把封面送到行動用戶端與 CarPlay 螢幕,品質很重要。
- 強烈建議 **Album Artist** — 它是 Plex/Jellyfin 用來依藝人正確分組的依據。

### 為車載音響與較舊硬體準備檔案

- **ID3v2.4: 關**(改用 ID3v2.3) — 較舊主機通常不支援 v2.4。
- **專輯封面: 中** — 許多車用顯示器會在大型內嵌封面上卡住。
- **標籤複製: 開** — 較舊車載音響有時只讀 ID3v1 後備。

## 其他改進

### Liquid Glass 設計

Evertag 4.2 的整個應用程式介面已針對 Apple 全新的 **Liquid Glass** 材質進行更新 — 半透明表面、更滑順的動畫,以及自然融入 iOS、iPadOS 與 macOS 的精緻控制項。

### 更新的連線函式庫

我們更新了 Evertag 用以與 **WebDAV**、**SMB**、**DLNA**、**Dropbox**、**Google Drive**、**OneDrive** 等服務通訊的內部函式庫。換言之:邊緣情境下的連線失敗更少、對較新版伺服器的支援更好,在遠端檔案上編輯標籤時的可靠性也提升。

### 翻譯與在地化修正

依使用者直接回饋進行的多語系 UI 修正。多種語言中較小按鈕的文字貼合更佳。

### 受你回饋啟發的小幅打磨

依 App Store 評論與寄至 support@everappz.com 的回饋進行的多項細部改進。我們閱讀每一則訊息。

## 取得 Evertag 4.2

[**從 App Store 下載 Evertag**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) 或在 App Store 中更新。Evertag 為免費下載,並提供針對進階功能的可選 App 內升級。新的雲端連線、網路通訊協定、Wi-Fi Drive 改進與 Liquid Glass UI,皆屬於基礎更新。

如果你喜歡這款 App,請在 App Store 留下評分 — 這真的對我們很有幫助。如果你有回饋或遇到問題,請寄信到 **support@everappz.com**,我們會閱讀每一封訊息。

## 常見問題

{{% details title="Evertag 4.2 有什麼新功能?" closed="true" %}}
Evertag 4.2 新增了 6 項以上的雲端與伺服器連線(Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS)、具備多選與更聰明上傳佇列的全新 Wi-Fi Drive、Liquid Glass UI 更新、更新的連線函式庫、關鍵的標籤編輯錯誤修正,以及翻譯改進。
{{% /details %}}

{{% details title="在 Evertag 中該使用 ID3v2.4 還是 ID3v2.3?" closed="true" %}}
對現代播放器(Evermusic、Plex、Jellyfin、Apple Music、foobar2000、VLC、現代 Android App)以及包含非拉丁字元的資料庫,使用 **ID3v2.4** — UTF-8 支援表示中文、韓文、日文、俄文、阿拉伯文與希伯來文標籤更乾淨。如果標籤在某些 App 顯示不正確、面向較舊車載音響,或某條串流代理商管線拒絕 v2.4,使用 **ID3v2.3**。你隨時可以切換並重新儲存。
{{% /details %}}

{{% details title="為什麼編輯後我的標籤在 Spotify 顯示錯誤?" closed="true" %}}
Spotify 大多顯示自家目錄的中繼資料 — 你的本機標籤只用於「Local Files」或你以藝人身分上傳的內容。如果你為 Spotify Local Files 打標籤後未正確顯示,試著在 Evertag 中關閉 ID3v2.4 並儲存為 ID3v2.3 — Spotify 的剖析器歷來對 v2.4 較保守。
{{% /details %}}

{{% details title="Evertag 中該選哪個專輯封面尺寸?" closed="true" %}}
對大多數使用者:**大**。在手機、iPad、Mac 與現代車用顯示器上看起來都很好,且不會過度增加檔案大小。資料庫非常大、想節省磁碟時用 **中**。只有需要封存母帶或確實需要最高品質時才使用 **原始**(不縮放) — 但要留意有些較舊播放器處理超大內嵌封面會有困難。**原始** 屬於 Evertag 進階個人化升級的一部分。
{{% /details %}}

{{% details title="較大的專輯封面會讓我的檔案變大嗎?" closed="true" %}}
會。嵌入一張 3,000 × 3,000 px 的封面可為單一音訊檔案多出數 MB。在 1,000 首歌曲的資料庫中,加總可達 GB。如果儲存吃緊,使用 中 或 大;如果你從 NAS 串流、不在意大小,特大 或 原始 也可以。
{{% /details %}}

{{% details title="什麼是標籤複製,我應該啟用嗎?" closed="true" %}}
標籤複製會把核心中繼資料同時寫入檔案的 ID3v1(舊版 128 位元組)與 ID3v2(新版)兩個區段。只在面向非常老舊的播放器或讀取 ID3v1 的硬體時啟用。對所有現代裝置(智慧型手機、電腦、近期車載音響),關閉即可。
{{% /details %}}

{{% details title="Evertag 是直接在雲端檔案上編輯標籤嗎?" closed="true" %}}
是的。連線到你的雲端(Google Drive、Dropbox、OneDrive、iCloud Drive、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3 等)或透過 FTP/SFTP/NFS,然後開啟檔案,像本機檔案一樣編輯標籤。Evertag 會下載檔案、套用你的編輯,並把更新後的版本上傳回去。你可以在設定中選擇「永遠詢問」、「自動上傳」或「不上傳」模式。
{{% /details %}}

{{% details title="可以在 iPhone 上用 Evertag 編輯 FLAC 標籤嗎?" closed="true" %}}
可以。Evertag 支援 FLAC、MP3、M4A/MP4、AIFF、WAV、OGG、APE 與其他主要格式,並提供完整標籤讀寫支援,包含內嵌封面。
{{% /details %}}

{{% details title="如何透過 SFTP 在家用伺服器上安全地編輯標籤?" closed="true" %}}
開啟 Evertag,前往連線分頁,選擇 SFTP,然後輸入伺服器的主機名稱或 IP、連接埠(通常為 22)、使用者名稱,以及密碼或 SSH 私密金鑰。Evertag 會瀏覽你的遠端資料夾,並透過 SSH 上的端對端加密直接編輯標籤。
{{% /details %}}

{{% details title="可以一次編輯多個檔案的標籤嗎?" closed="true" %}}
可以。在設定中啟用 **同時編輯檔案**。選擇多個檔案,開啟標籤編輯器,你變更的任何欄位都會套用到所有所選檔案。是為整張專輯設定相同 album artist、年份或類型的最快方法。
{{% /details %}}

{{% details title="Evertag 4.2 的更新是免費的嗎?" closed="true" %}}
是的。Evertag 在 App Store 為免費下載,4.2 也是針對所有現有使用者的免費更新。新的雲端整合、Wi-Fi Drive 改進與 Liquid Glass UI 都包含在基礎更新內。
{{% /details %}}

{{% details title="Evertag 4.2 在哪些裝置上可用?" closed="true" %}}
Evertag 4.2 可在 iPhone、iPad 與 Mac 上執行。iCloud Drive 同步會讓你的標籤編輯器設定在不同裝置間保持一致。
{{% /details %}}
