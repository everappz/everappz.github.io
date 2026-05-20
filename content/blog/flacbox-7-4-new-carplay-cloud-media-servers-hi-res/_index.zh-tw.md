---
title: "Flacbox 7.4:重建 CarPlay,Plex、Jellyfin、Subsonic、SFTP 助力 Hi-Res 音訊"
date: 2026-05-20
description: "Flacbox 7.4 帶來從零開始重建的 CarPlay 體驗,新增 10+ 種播放無損音樂庫的新方式 — Plex、Subsonic、Navidrome、Jellyfin、Emby、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3,以及 FTP、SFTP 與 NFS。包含煥新的主畫面小工具、Liquid Glass 設計,以及更強的網路函式庫,支援在 iPhone 與 Mac 上播放 FLAC、DSD、ALAC 與 APE。"
keywords: ["Flacbox 7.4", "Flacbox 更新", "CarPlay hi-res 音訊播放器", "CarPlay FLAC 播放器 iPhone", "Plex hi-res 音樂 iPhone", "Plex 無損串流", "Jellyfin FLAC 播放器 iOS", "Emby 無損音樂 iOS", "Subsonic FLAC iPhone", "Navidrome 無損 iOS 用戶端", "Internxt FLAC 串流", "Proton Drive 無損音樂", "QNAP hi-res 音樂播放器", "Nextcloud FLAC 串流 iOS", "Amazon S3 無損音訊 iPhone", "SFTP FLAC 播放器 iPhone", "FTP hi-res 音訊 iOS", "NFS 無損串流 iPhone", "從 NAS 串流 DSD iPhone", "DSD 播放器 iPhone 2026", "ALAC 播放器 iOS", "無損音樂播放器 iPhone", "Liquid Glass 音訊應用程式", "hi-res 音訊播放器 iOS 2026"]
tags: ["Flacbox", "Flacbox 7.4", "CarPlay", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "主畫面小工具", "Liquid Glass", "Hi-Res Audio", "FLAC", "DSD", "ALAC", "新功能"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**重點:** [Flacbox 7.4](/products/flacbox) 是 iPhone 與 Mac 上 hi-res 音訊播放器的重大更新。CarPlay 已從零開始重建 — 快速排序、多種配色配置、全新「正在播放」畫面、一眼看到完整播放佇列,以及針對龐大資料庫的字母索引。本次更新新增了 10+ 種連結音樂的新方式 — 重視隱私的雲端 **Internxt** 與 **Proton Drive**、個人伺服器 **QNAP**、**Nextcloud** 和 **Amazon S3**、串流伺服器 **Plex**、**Subsonic**、**Navidrome**、**Jellyfin** 與 **Emby**,以及 **FTP**、**SFTP** 與 **NFS** 網路協定。介面已針對 Apple 全新的 **Liquid Glass** 材質進行調校,底層網路函式庫更強,主畫面小工具更新更可靠。

---

## 大家好!

Flacbox 的重大更新已經到來。我們從零開始重建了 CarPlay,並新增了十多種連線到你無損音樂資料庫的新方式 — 從重視隱私的雲端儲存,到熱門的自架媒體伺服器,以及經典的網路協定。

[從 App Store 下載 Flacbox 7.4](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) 或從你目前的版本進行更新。Mac 使用者可以從 [此處取得桌面版](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8)。

## CarPlay,從零開始重建

我們從零開始為 Flacbox 重新設計了 **Apple CarPlay**,讓在路上聆聽更安全、更輕鬆。每個細節 — 從如何尋找歌曲,到如何控制播放 — 都針對車內體驗進行了重新調校。

- **快速排序** — 在專輯、藝術家、播放清單與資料夾中,瞬間就能找到任意一首歌,無需無止盡捲動。
- **匹配車輛的配色配置** — 選擇與儀表板或車內燈光相搭配的主題,白天或夜晚皆宜。
- **全新「正在播放」畫面** — 更大的封面、更清晰的控制項,以及輕點即可使用的全新播放動作。
- **一眼看到完整播放佇列** — 不必離開目前畫面就能查看接下來要播放的內容。
- **針對大型資料庫的字母索引** — 輕點一下即可跳轉數萬首 FLAC、DSD、ALAC 與 APE 曲目。
- **載入更快,不再卡頓** — 開啟大型資料夾、雲端目錄或媒體伺服器資料庫時,感覺即時。

如果你在開車時串流無損音訊 — 從 Dropbox、Google Drive、OneDrive、iCloud Drive、[Plex](#media-servers)、[Jellyfin](#media-servers)、Subsonic 或任何其他來源 — 重建後的 CarPlay 體驗會讓整個流程感覺就像車內原生。

## 10+ 種連結音樂的新方式

Flacbox 7.4 擴大了「音樂資料庫」的定義。如果你的 hi-res 檔案位於你信任的雲端、家中的 NAS,或是自架的串流伺服器,Flacbox 現在可以直接從中串流播放 — 無需同步、無需匯出、無需格式轉換。

### 重視隱私的雲端:Internxt 與 Proton Drive

如果你重視端對端加密與零知識儲存,兩個最受推崇的隱私導向雲端如今已成為 Flacbox 的原生選項:

- **Internxt** — 來自西班牙的開源、後量子加密、符合 GDPR 的雲端服務。提供免費方案。
- **Proton Drive** — 由 Proton Mail 與 Proton VPN 團隊打造、總部位於瑞士的端對端加密儲存空間。提供免費方案,以及供更大資料庫使用的付費方案。

只要連線一次,你的 FLAC、DSD 或 ALAC 檔案就會走加密通道 — Flacbox 看不到你的明文資料,服務商伺服器同樣也看不到。

### 個人伺服器:QNAP、Nextcloud、Amazon S3

適合自行管理基礎架構的聽眾:

- **QNAP** — 透過原生 API 連線至 QNAP NAS 裝置,無論是本地 Wi-Fi 還是遠端存取,都能享有快速且穩定的播放。直接串流高位元率 FLAC 與 DSD,無需重新編碼。
- **Nextcloud** — 連線到任何自架或代管的 Nextcloud 執行個體。如果你出於隱私考量已從 Google Drive 或 Dropbox 移轉,這非常適合你。
- **Amazon S3** — 將 Flacbox 指向任何 S3 儲存桶(或 Backblaze B2、Wasabi、MinIO、Cloudflare R2 等 S3 相容儲存),即可直接串流你的收藏。

### <a id="media-servers"></a>串流伺服器:Plex、Subsonic、Navidrome、Jellyfin、Emby

對自架音樂愛好者來說,這是最重要的一項更新。Flacbox 7.4 把你的 iPhone 或 Mac 變成最受歡迎的開源與免費增值媒體伺服器的一流 hi-res 用戶端:

- **Plex** — Plex Media Server 可 **免費** 下載並執行。**Plex Pass** 為可選付費訂閱,可解鎖行動同步、硬體轉碼與其他附加功能。Flacbox 同時支援免費與 Plex Pass 資料庫。
- **Subsonic** — 自架音樂串流伺服器的鼻祖。官方 Subsonic 伺服器需 **付費**(30 天試用後每月 1 美元),Flacbox 也支援數十種採用 Subsonic API 的相容伺服器。
- **Navidrome** — 以 Go 撰寫的現代化、輕量級音樂伺服器,**完全免費且開源**。實作 Subsonic API。可在 Raspberry Pi、NAS 或任何 Linux 機器上執行。針對數十萬首以內的無損收藏資料庫,我們強力推薦。
- **Jellyfin** — **完全免費且開源** 的媒體伺服器(Emby 的社群分支)。可處理音樂、電影、電視與有聲書。沒有帳號、沒有遙測、沒有訂閱。
- **Emby** — **免費增值** 的媒體伺服器。核心伺服器免費;**Emby Premiere** 為一次性或年度付費,可解鎖行動 App、離線同步等。Flacbox 同時支援免費與 Premiere 資料庫。

無論你執行哪一種伺服器,Flacbox 都能串流你的整個收藏 — 包含專輯、藝術家、播放清單、類型與內嵌封面 — 並提供 bit-perfect 輸出至 USB DAC、10 段等化器、crossfade 與 gapless 播放、AirPlay、Chromecast 與重建後的 **CarPlay** 體驗。你的伺服器保留收聽紀錄;Flacbox 會予以尊重。

### 全新的傳輸方式:FTP、SFTP、NFS

對於使用自訂伺服器、家庭實驗室或缺乏精緻行動 App 的通用 NAS 的聽眾,Flacbox 7.4 新增了三種經典網路協定:

- **SFTP(SSH 檔案傳輸協定)** — 這是 **從自己的伺服器進行安全遠端串流** 的正確選擇。SFTP 在 SSH 之上執行,因此整個傳輸(身分驗證與音訊資料)都會被加密。如果你擁有 VPS、專屬伺服器,或家中具備 SSH 存取權的 Linux 機器,可以將 FLAC 或 DSD 資料夾放在那裡,透過公開網際網路串流,而不必暴露任何其他內容。支援密碼及金鑰驗證。
- **FTP** — 長期以來確立的檔案傳輸標準。如果你的 **家用 NAS**(較舊的 Synology、ASUS、D-Link、TerraMaster 或通用機殼)提供 FTP 伺服器但沒有原生 API 整合,這就很有用。建議在區域網路中使用。
- **NFS(網路檔案系統)** — Linux 與大多數 NAS 裝置上事實上的分享協定。NFS 共用在家庭實驗室與小型企業網路中相當常見;Flacbox 現在可以掛載並直接串流 bit-perfect 音訊。在相同硬體上,NFS 的負擔比 SMB 更小。

> **提示:** 想透過開放網際網路串流時,SFTP 是最佳選擇。FTP 與 NFS 比較適合在區域網路內使用 — 除非以 VPN 包覆,否則別把它們暴露在網際網路。

## 其他改進

### 與 Liquid Glass 相匹配的全新外觀

Flacbox 7.4 的整個應用程式介面已針對 Apple 全新的 **Liquid Glass** 材質進行更新 — 半透明表面、更滑順的動畫,以及自然融入 iOS 26 與 macOS 26 的精緻控制項。資料庫、正在播放、等化器與設定畫面皆已為新系統美學進行調校。

### 更強的網路函式庫

我們更新了 Flacbox 用以與 **WebDAV**、**SMB**、**DLNA**、**Dropbox**、**Google Drive**、**OneDrive**、**iCloud Drive**、**MEGA** 等服務通訊的內部函式庫。換言之:邊緣情境下的連線失敗更少、對較新版伺服器的支援更好,在較慢或地理位置較遠的連線上串流高位元率音訊時可靠性更高。

### 修復了某些伺服器上的播放問題

我們追查並修復了某些自架伺服器上的若干播放問題 — 包含大型 FLAC 與 DSD 檔案搜尋後的卡頓,以及檔案清單很長的資料庫上啟動時間慢的問題。串流從頭到尾會感覺更乾淨。

### 重新整理更佳的全新主畫面小工具

主畫面小工具 — 正在播放、播放佇列、最近播放 — 經過重新設計,採用更整潔的版面與更聰明的重新整理策略。它們與應用程式保持同步而不會額外耗電,而幾種新的小工具尺寸讓你能更好地控制一眼可見的資訊。

### 翻譯修正

根據使用者直接回饋,多種語言的多處小型本地化修正。文字在較小按鈕與較長的歐洲語言(德語、荷蘭語、法語、西班牙語)中更加合適。

### 受你訊息啟發的小幅打磨

根據 App Store 評論與寄至 support@everappz.com 的電子郵件的眾多小幅改進。我們閱讀每一條訊息。

## 這次更新為何重要

Flacbox 7.4 圍繞兩個想法打造:

1. **無論你把 hi-res 音樂放在哪裡,音樂都是你的。** 不管你的無損資料庫位於 iCloud Drive、Proton Drive 或 Internxt 等重視隱私的雲端、Plex 或 Jellyfin 等媒體伺服器、家中的 NAS,還是執行 Navidrome 的 Raspberry Pi — Flacbox 都以原生方式連線,提供處處一致的 bit-perfect 播放體驗。
2. **車內體驗更好。** CarPlay 是許多聽眾最常注視的螢幕,而重建後的體驗反映了這一點 — 更快、更安全,圍繞真實駕駛者如何接觸音樂而建構。

## 取得 Flacbox 7.4

[**從 App Store 下載 Flacbox**](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) 或在 App Store 中更新。[Mac 版本](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8) 作為通用 Mac 應用程式單獨提供。Flacbox 為免費下載,並提供針對進階功能的可選 App 內升級。重建的 CarPlay、所有全新的雲端與伺服器連線、煥新的主畫面小工具以及 Liquid Glass UI 皆屬於基礎更新。

如果這款 App 讓你的生活更美好,請在 App Store 留下評分 — 這真的對我們很有幫助。如有問題或回饋?請寄信到 **support@everappz.com**,我們會閱讀每一封訊息。

## 常見問題

{{% details title="Flacbox 7.4 有什麼新功能?" closed="true" %}}
Flacbox 7.4 帶來完全重建的 CarPlay 體驗、新增 10+ 種連線 — Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS。此次更新還帶來 Liquid Glass 設計煥新、更強的網路函式庫、智慧重新整理的重新設計主畫面小工具、某些伺服器上的播放修正、翻譯改進以及眾多小幅打磨。
{{% /details %}}

{{% details title="Flacbox 是否支援 Plex 的 FLAC 與無損音訊?" closed="true" %}}
是的。從 Flacbox 7.4 開始,你可以連線至 Plex Media Server,並串流整個 hi-res 資料庫 — FLAC、ALAC、WAV、AIFF、OGG、OPUS 與其他無損格式。Plex Media Server 可免費執行;Plex Pass 為可選。Flacbox 同時支援免費與 Plex Pass 設定。
{{% /details %}}

{{% details title="Flacbox 支援 Jellyfin 與 Navidrome 嗎?" closed="true" %}}
是的。Jellyfin 與 Navidrome 都在 Flacbox 7.4 中獲得完整支援。Jellyfin 是免費、開源的媒體伺服器;Navidrome 是實作 Subsonic API 的免費、開源音樂伺服器。Flacbox 以原生方式連線兩者,並以完整的中繼資料與封面串流你的無損資料庫。
{{% /details %}}

{{% details title="Plex、Jellyfin、Emby、Navidrome 與 Subsonic 是免費的嗎?" closed="true" %}}
- **Plex** — 伺服器免費;Plex Pass 為可選的付費升級。
- **Jellyfin** — 完全免費且開源。
- **Emby** — 伺服器免費;Emby Premiere 為付費,可解鎖行動同步與離線。
- **Navidrome** — 完全免費且開源。
- **Subsonic** — 官方伺服器在 30 天試用後每月 1 美元,但其 API 為開放,許多免費伺服器(包含 Navidrome)都實作了它。
{{% /details %}}

{{% details title="可以透過 SFTP、FTP 或 NFS 從家用 NAS 串流 FLAC 與 DSD 嗎?" closed="true" %}}
可以。Flacbox 7.4 將 SFTP、FTP 與 NFS 加入為原生連線型別。SFTP 是從自己的伺服器透過公開網際網路串流的建議選擇,因為所有流量都會透過 SSH 加密。FTP 與 NFS 較適合在區域網路或 VPN 內使用。
{{% /details %}}

{{% details title="如何使用 SFTP 將 Flacbox 連線至自訂伺服器?" closed="true" %}}
開啟 Flacbox,前往連線分頁,選擇 SFTP,然後輸入伺服器的主機名稱或 IP、連接埠(通常為 22)、使用者名稱,以及密碼或 SSH 私密金鑰。Flacbox 會瀏覽你的遠端資料夾,並以端對端加密直接串流音訊檔。
{{% /details %}}

{{% details title="Flacbox 支援 Internxt 與 Proton Drive 嗎?" closed="true" %}}
支援。兩款重視隱私的雲端皆從 Flacbox 7.4 起獲得支援。它們與 App 中已有的 MEGA 等重視隱私的服務並列。
{{% /details %}}

{{% details title="Flacbox 是否能播放來自 Plex、Jellyfin 或 NAS 的 DSD 檔案?" closed="true" %}}
是的。Flacbox 能播放從 Plex、Jellyfin、Emby、Subsonic 相容伺服器、QNAP、Nextcloud、Amazon S3 以及透過 SFTP、FTP 與 NFS 串流的 DSD64、DSD128 與 DSD256 檔案(DSF 與 DFF 容器)。在 iPhone、iPad 與 Mac 上支援 bit-perfect 輸出至 USB DAC。
{{% /details %}}

{{% details title="重新設計的 CarPlay 畫面如何運作?" closed="true" %}}
Flacbox 的 CarPlay 介面已重建,支援在專輯、藝術家、播放清單與資料夾中快速排序;多種與不同車內裝飾相匹配的配色配置;帶有新控制項的全新「正在播放」畫面;一眼可見的完整播放佇列;針對大型資料庫的字母索引;以及在大型資料夾與雲端目錄上的更快載入。
{{% /details %}}

{{% details title="Flacbox 7.4 是免費更新嗎?" closed="true" %}}
是的。Flacbox 在 App Store 為免費下載,7.4 是針對所有現有使用者的免費更新。重建的 CarPlay、所有全新的雲端與伺服器連線、煥新的主畫面小工具以及 Liquid Glass UI 皆屬於基礎更新。
{{% /details %}}

{{% details title="Flacbox 7.4 在哪些裝置上可用?" closed="true" %}}
Flacbox 7.4 可在 iPhone、iPad 與 Mac 上執行。CarPlay 支援需要相容 CarPlay 的車輛或售後主機。AirPlay 與 Chromecast 讓你能把播放投到更大的系統;USB DAC 支援 bit-perfect 無損輸出。
{{% /details %}}
