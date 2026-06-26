---
title: "Evervideo 1.7:全新 Plex、Jellyfin、雲端串流與播放手勢"
date: 2026-05-18
description: "Evervideo 1.7 新增 10 項以上的全新連線 — Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS — 以及全新的播放手勢(雙擊快轉/倒轉、長按 2 倍速),煥然一新的 Wi-Fi Drive 支援批次上傳,並為 iPhone、iPad 與 Mac 帶來 Liquid Glass 介面更新。"
keywords: ["Evervideo 1.7", "Evervideo 更新", "HD 影片播放器 iPhone", "Plex 影片播放器 iOS", "Jellyfin iPhone 影片", "Emby 影片播放器 iOS", "Subsonic 影片 iOS", "Navidrome 影片 iOS", "Internxt 影片串流", "Proton Drive 影片播放器", "QNAP 影片播放器 iPhone", "Nextcloud 影片播放器 iOS", "Amazon S3 影片串流", "SFTP 影片播放器 iPhone", "FTP 影片播放器 iOS", "NFS 影片串流 iPhone", "從 NAS 串流影片 iPhone", "MKV 播放器 iPhone", "影片播放器手勢 iOS", "雙擊快轉影片", "Wi-Fi Drive 影片傳輸 iPhone", "Liquid Glass 設計", "雲端影片播放器 iOS 2026", "從雲端串流電影 iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "播放手勢", "Liquid Glass", "新功能"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**重點:** [Evervideo 1.7](/products/evervideo) 是 iPhone、iPad 與 Mac 上 HD 影片播放器的一次重大更新。此版本新增了 10 項以上的雲端、NAS 與媒體伺服器連線 — **Internxt**、**Proton Drive**、**QNAP**、**Nextcloud**、**Amazon S3**,以及最受歡迎的媒體伺服器 **Plex**、**Subsonic**、**Navidrome**、**Jellyfin** 與 **Emby**,還有三種網路通訊協定:**FTP**、**SFTP** 與 **NFS**。全新的 **播放手勢** 讓你能雙擊向前或向後跳轉、長按以 2 倍速播放,以及單擊切換控制列 — 一切都不必離開全螢幕模式。Wi-Fi Drive 擁有煥然一新的介面、多選模式與更聰明的上傳佇列。整個應用程式都已為 Apple 全新的 **Liquid Glass** 設計進行調整。

---

## 大家好!

Evervideo 的一項重大更新到了。這是我們發佈過最大的版本之一:**10 項以上全新的雲端、伺服器與網路連線**、嶄新的 **播放手勢** 讓你在全螢幕中更快控制、煥然一新的 **Wi-Fi Drive**,以及為 iPhone、iPad 與 Mac 調校過的 **Liquid Glass** 介面。

[從 App Store 下載 Evervideo 1.7](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336),或從你目前的版本進行更新。Mac 使用者可以在 [此處取得桌面版](https://apps.apple.com/app/evervideo/id6743504109)。

## 10 項以上全新的雲端、NAS 與媒體伺服器連線

Evervideo 1.7 擴展了你所謂「影片資料庫」的範圍。若你的電影、影集或錄影檔放在你信任的雲端、家中的 NAS,或是自架的媒體伺服器上,Evervideo 現在都能直接從中串流 — 不必下載、不必轉檔、不必重新編碼。

### 重視隱私的雲端儲存:Internxt 與 Proton Drive

如果你重視端對端加密與零知識儲存,兩個最受推崇的隱私導向雲端如今已成為 Evervideo 的原生選項:

- **Internxt** — 來自西班牙的開源、後量子加密、符合 GDPR 的雲端服務。提供免費方案。
- **Proton Drive** — 由 Proton Mail 與 Proton VPN 團隊打造、總部位於瑞士的端對端加密儲存空間。提供免費方案,以及供更大資料庫使用的付費方案。

連線一次,你的影片即可透過加密通道串流 — Evervideo 永遠看不到你的明文資料,服務商伺服器也看不到。

### 自架儲存:QNAP、Nextcloud、Amazon S3

適合自行管理基礎架構的使用者:

- **QNAP** — 透過原生 API 連線至 QNAP NAS 裝置,以本機 Wi-Fi 或遠端存取進行快速且穩定的影片播放。無需重新編碼即可直接串流 4K MKV 檔案。
- **Nextcloud** — 連線到任何自架或代管的 Nextcloud 執行個體。如果你已基於隱私考量從 Google Drive 或 Dropbox 遷移,這會是絕佳選擇。
- **Amazon S3** — 將 Evervideo 指向任何 S3 儲存桶(或 Backblaze B2、Wasabi、MinIO、Cloudflare R2 等 S3 相容儲存),即可直接串流你的收藏。

### <a id="media-servers"></a>媒體伺服器:Plex、Subsonic、Navidrome、Jellyfin、Emby

這是給自架影片愛好者的大消息。Evervideo 1.7 讓你的 iPhone、iPad 或 Mac 成為最受歡迎的開源與 freemium 媒體伺服器的一流用戶端:

- **Plex** — Plex Media Server **免費** 下載與執行,可選 **Plex Pass** 訂閱以取得行動同步、硬體轉碼與直播電視等功能。Evervideo 同時支援免費與 Plex Pass 資料庫 — 串流你完整的電影與電視收藏。
- **Subsonic** — 最早的自架串流伺服器。官方 Subsonic 伺服器 **付費**(30 天試用後每月 1 美元),Evervideo 也使用 Subsonic API 與相容的影片伺服器對話。
- **Navidrome** — 現代、輕量、**完全免費且開源** 的伺服器。實作 Subsonic API。可在 Raspberry Pi、NAS 或任何 Linux 主機上執行。
- **Jellyfin** — **完全免費且開源** 的媒體伺服器(Emby 的社群分支)。處理電影、電視、音樂、書籍與家庭影片。沒有帳號、沒有遙測、沒有訂閱。是希望在不被商業條件綁住的情況下進行自架串流的使用者首選。
- **Emby** — **freemium** 媒體伺服器。核心伺服器免費;**Emby Premiere** 是一次性或年度購買,可解鎖行動 App、離線同步、Cinema Mode 等。Evervideo 同時連線到免費與 Premiere 資料庫。

無論你執行哪一種伺服器,Evervideo 都會串流你完整的資料庫 — 電影、影集、家庭影片與內嵌字幕軌 — 並支援影片等化器、360° 支援、子母畫面、AirPlay 與 Chromecast。

### 全新網路通訊協定:FTP、SFTP、NFS

對於擁有自訂伺服器、家庭實驗室或缺乏精緻行動 App 的通用 NAS 的使用者,Evervideo 1.7 新增了三項經典通訊協定:

- **SFTP(SSH File Transfer Protocol)** — 這是 **從自己的伺服器進行安全遠端影片串流** 的正確選擇。SFTP 在 SSH 之上執行,因此整個傳輸(身分驗證與影片資料)都會被加密。如果你擁有 VPS、專屬伺服器,或家中具備 SSH 存取權的 Linux 機器,可以把一個影片資料夾放上去,並透過公開網際網路串流,而無須暴露任何其他內容。支援密碼與金鑰驗證。
- **FTP** — 長期以來確立的檔案傳輸標準。若你的 **家用 NAS**(較舊的 Synology、ASUS、D-Link、TerraMaster 或一般機型)提供 FTP 伺服器但沒有原生 API 整合,會很實用。最適合在區域網路中使用。
- **NFS(Network File System)** — Linux 與大多數 NAS 裝置上事實上的分享通訊協定。NFS 分享在家庭實驗室與中小企業網路中很常見;Evervideo 現可掛載並以低負擔串流 4K 與 HD 影片。

> **提示:** 想透過開放網際網路串流時,SFTP 是最佳選擇。FTP 與 NFS 比較適合在區域網路內使用 — 除非以 VPN 包覆,否則別把它們暴露在公共網際網路。

## 全新播放手勢

在全螢幕觀看影片應該毫不費力。Evervideo 1.7 引入一組簡潔的點擊手勢,讓你不必顯示螢幕控制列也能掌控播放 — 非常適合看電影、聽課,或任何你想不被打擾的內容。

### 雙擊 — 向前或向後跳轉

雙擊螢幕 **右側** 可 **快轉** 一個可設定的秒數。雙擊 **左側** 可 **倒轉**。可在 **設定 → 播放 → 手勢跳轉間隔** 中修改時間(預設:10 秒) — 從 5 秒(精細定位)到 60 秒(略過片頭)。

這是 YouTube 與 Netflix 使用者一眼就能辨識的手勢,現在已原生內建於 Evervideo,可用於任何來源的任何影片。

### 長按 — 暫時 2 倍速

在螢幕任意位置按住即可 **暫時將播放速度加快至 2 倍**。放開即恢復一般速度。非常適合:

- 在不切換永久速度的情況下略過緩慢的場景。
- 快速掃過課程、教學或 podcast 找出相關段落。
- 在投入觀看完整版本之前先試看電影。

長按手勢不會更改你儲存的播放速度 — 一放開就回到原來的位置。

### 單擊 — 顯示 / 隱藏控制列

單擊螢幕可切換播放控制(播放、暫停、進度列、字幕、等化器)。點一次顯示,再點一次隱藏。結合雙擊與長按,你幾乎可以整部電影都待在乾淨的全螢幕模式中,同時又能在需要時拖動、暫停與快速掃看。

## Wi-Fi Drive:全新介面與更快的上傳

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) 是 Evervideo 內建的功能,用於 **從電腦無線傳輸影片到 iPhone 或 iPad — 不需要 iTunes、不需要傳輸線、不需要雲端帳號**。兩台裝置必須位於相同的 Wi-Fi 網路。你在 iOS App 上啟動伺服器後,選擇下列其一:

- 在任何桌面瀏覽器(Safari、Chrome、Firefox、Edge)中開啟網址,把影片檔拖進頁面,即可直接上傳至裝置;或
- 透過 **Mac Finder**(「連線到伺服器…」)或 **Windows 檔案總管**(對應網路磁碟機),用 WebDAV 把裝置掛載為網路共用。

這是把大量本機影片收藏移到手機或平板的最快方式,不需要任何第三方服務。請參閱 [此處的逐步教學](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/)。

在 Evervideo 1.7 中,Wi-Fi Drive 取得:

- **重新設計的使用者介面** — 更整潔、更易於一眼閱讀,並已對齊 Liquid Glass。
- **新的批次操作選擇模式** — 選取多個檔案或資料夾並批次處理(刪除、移動、複製)。
- **改進的檔案上傳佇列** — 更好的進度回饋與面對網路抖動的韌性,讓不穩定的 Wi-Fi 連線不再毀掉一次 30 GB 的傳輸。
- **整體傳輸效能更好** — 對大型資料庫可量測地更快上傳,尤其是 4K MKV 檔與電影合集。

## 其他改進

### Liquid Glass 設計更新

Evervideo 1.7 的介面已在整個 App 中為 Apple 新的 **Liquid Glass** 材質進行更新 — 半透明表面、更平滑的動畫,以及與 iOS 26、iPadOS 26 與 macOS 26 自然契合的細緻控制項。Now Playing、檔案瀏覽器與設定畫面都已重新調整,以符合新的系統美學。

### 更新的連線函式庫

我們刷新了 Evervideo 用來與 **WebDAV**、**SMB**、**DLNA**、**Dropbox**、**Google Drive**、**OneDrive**、**iCloud Drive**、**MEGA** 等服務對話的底層函式庫。結果是:邊界情況下的連線失敗更少、對較新版本伺服器的支援更好,以及在較慢或地理距離較遠的連線上串流影片時更高的可靠性。

### 播放錯誤修正

- 修正了在某些自架伺服器上,在大型 MKV 檔上拖動後串流會停頓的播放問題。
- 在播放中網路短暫斷線時有更佳的回復行為。
- 長片內容上的字幕同步更為平滑。

### 在地化修正

根據使用者直接回饋,於多種語言中修正翻譯。在較小的按鈕與較長的歐洲語言(德語、荷蘭語、法語)上,文字呈現更為合宜。

### 受你回饋啟發的小幅打磨

許多更小的改善源自 App Store 評論與寄到 support@everappz.com 的郵件。我們閱讀每一則訊息。

## 為什麼這次更新很重要

Evervideo 1.7 圍繞三個理念打造:

1. **你的影片,在你儲存的任何地方。** 不論你的資料庫在 iCloud Drive、Proton Drive 或 Internxt 這類重視隱私的雲端、Plex 或 Jellyfin 這類媒體伺服器、家中的 NAS,或是執行 Navidrome 的 Raspberry Pi — Evervideo 現在都能原生連線,並在所有位置提供一致的播放體驗。
2. **毫不費力的全螢幕影片。** 全新點擊手勢(雙擊、長按、單擊)帶來 YouTube 與 Netflix 等串流 App 已讓使用者習以為常的流暢操作,並套用到 *你自己* 的影片收藏。
3. **從電腦更快傳輸。** 煥然一新的 Wi-Fi Drive 加上批次選擇與更聰明的上傳佇列,讓把大型 4K 電影收藏移到 iPhone 或 iPad 真正變得快速 — 無線、無 iTunes、無壓縮。

## 取得 Evervideo 1.7

[**從 App Store 下載 Evervideo**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336),或在 App Store 內進行更新。[Mac 版](https://apps.apple.com/app/evervideo/id6743504109) 以通用 Mac App 形式單獨提供。Evervideo 為免費下載,並提供選用的應用程式內升級以取得進階功能。新的雲端連線、媒體伺服器支援、播放手勢、Wi-Fi Drive 改進與 Liquid Glass UI 都屬於基本更新。

如果你喜歡這個 App,請在 App Store 留下評分 — 這真的很有幫助。有回饋或遇到問題?請寫信給我們 **support@everappz.com**。我們會閱讀每一則訊息。

## 常見問題

{{% details title="Evervideo 1.7 有什麼新功能?" closed="true" %}}
Evervideo 1.7 引入對 10 項以上新連線的支援(Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS)、全新的播放手勢(雙擊快轉/倒轉、長按 2 倍速、單擊切換控制列)、重新設計的 Wi-Fi Drive(具備選擇模式與更聰明的上傳佇列)、Liquid Glass 設計更新、連線函式庫更新,以及大量錯誤修正。
{{% /details %}}

{{% details title="Evervideo 能搭配 Plex 使用嗎?" closed="true" %}}
可以。自 Evervideo 1.7 起,你可以連線到 Plex Media Server 並串流完整的影片資料庫 — 電影、電視劇與家庭影片。Plex Media Server 免費執行;Plex Pass 為可選項。Evervideo 同時支援免費與 Plex Pass 設定,包括直接播放 MKV、MP4、AVI、MOV 等格式而無需重新編碼。
{{% /details %}}

{{% details title="Evervideo 支援 Jellyfin 或 Navidrome 嗎?" closed="true" %}}
是的。Jellyfin 與 Navidrome 都在 Evervideo 1.7 中獲得完整支援。Jellyfin 是處理影片與音訊的免費開源媒體伺服器。Navidrome 是實作 Subsonic API 的免費開源伺服器。Evervideo 原生連線到兩者。
{{% /details %}}

{{% details title="Plex、Jellyfin、Emby、Navidrome 與 Subsonic 都是免費的嗎?" closed="true" %}}
- **Plex** — 伺服器免費;Plex Pass 是可選的付費升級。
- **Jellyfin** — 完全免費且開源。
- **Emby** — 伺服器免費;Emby Premiere 付費,可解鎖行動同步與離線功能。
- **Navidrome** — 完全免費且開源。
- **Subsonic** — 官方伺服器在 30 天試用後每月 1 美元,但其 API 開放,許多免費伺服器(包括 Navidrome)都已實作。
{{% /details %}}

{{% details title="我可以透過 SFTP、FTP 或 NFS 從家中的 NAS 串流嗎?" closed="true" %}}
可以。Evervideo 1.7 新增 SFTP、FTP 與 NFS 作為原生連線類型。SFTP 是透過公開網際網路從你自己的伺服器串流的建議選擇,因為所有流量都會透過 SSH 加密。FTP 與 NFS 最好在區域網路內使用,或在 VPN 後使用。
{{% /details %}}

{{% details title="如何用 SFTP 把 Evervideo 連到自訂伺服器?" closed="true" %}}
開啟 Evervideo,前往「連接」分頁,選擇 SFTP,然後輸入伺服器的主機名稱或 IP、連接埠(通常為 22)、使用者名稱,以及密碼或 SSH 私密金鑰。Evervideo 會瀏覽你的遠端資料夾,並以端對端加密直接串流影片檔。
{{% /details %}}

{{% details title="Evervideo 支援 Internxt 與 Proton Drive 嗎?" closed="true" %}}
支援。這兩種重視隱私的雲端服務從 Evervideo 1.7 起獲得支援。它們加入 MEGA 與應用程式中已有的其他重視隱私的服務。
{{% /details %}}

{{% details title="全新的播放手勢如何使用?" closed="true" %}}
在全螢幕影片播放中,**雙擊右側** 可快轉,**雙擊左側** 可倒轉一個可設定的間隔(預設 10 秒 — 可在「設定」中修改)。**長按** 螢幕任意位置可暫時加速至 2 倍;放開後恢復一般速度。**單擊** 螢幕任意位置可切換播放控制(顯示或隱藏)。
{{% /details %}}

{{% details title="我可以變更雙擊的跳轉間隔嗎?" closed="true" %}}
可以。前往 **設定 → 播放 → 手勢跳轉間隔**,選擇介於 5 與 60 秒之間的值。大多數使用者保持 10 或 15 秒。
{{% /details %}}

{{% details title="Evervideo 中的 Wi-Fi Drive 是什麼?" closed="true" %}}
Wi-Fi Drive 是 Evervideo 內建的無線檔案傳輸功能。它讓你能透過本機 Wi-Fi 網路從電腦上傳影片到 iPhone 或 iPad — 不需要 iTunes、不需要傳輸線、不需要雲端帳號。你可以使用任何桌面瀏覽器,或像 Mac Finder 或 Windows 檔案總管這類 WebDAV 用戶端。請參閱 [完整的 Wi-Fi Drive 指南](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/)。
{{% /details %}}

{{% details title="Evervideo 能從 Plex 或 Jellyfin 播放 MKV、AVI 與其他格式嗎?" closed="true" %}}
可以。Evervideo 播放幾乎所有影片格式 — MKV、AVI、MP4、MOV、FLV、WMV、WEBM、M4V、TS、3GP — 並直接從 Plex、Jellyfin、Emby 與其他媒體伺服器串流它們,多數轉碼器無需轉碼。這代表你的伺服器 CPU 負載更低、啟動時間更快。
{{% /details %}}

{{% details title="升級到 Evervideo 1.7 免費嗎?" closed="true" %}}
是的。Evervideo 為 App Store 中的免費下載,1.7 則是所有現有使用者的免費更新。新的雲端整合、媒體伺服器支援、播放手勢、Wi-Fi Drive 改進與 Liquid Glass UI 都屬於基本更新。
{{% /details %}}

{{% details title="Evervideo 1.7 支援哪些裝置?" closed="true" %}}
Evervideo 1.7 在 iPhone、iPad 與 Mac 上執行。AirPlay 與 Chromecast 讓你可以把播放投到更大的螢幕。iCloud Drive 同步可在不同裝置間維持資料庫與設定一致。
{{% /details %}}
