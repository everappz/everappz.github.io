---
title: "如何在iPhone上播放FLAC(無損)音樂"
date: 2024-01-29
lastmod: 2026-09-26
description: "2026年如何使用Flacbox在iPhone和iPad上播放FLAC。Flacbox是一款高解析度播放器,支援120多種格式,輸出高達384 kHz,支援USB DAC、10段等化器、BASS音訊引擎、殘響和延遲等即時效果、DSP處理器以及帶500個預設的音樂視覺化工具。可從雲端或NAS串流播放,也可離線播放。"
keywords: ["如何在iphone上播放flac", "flac播放器iphone", "flac", "iphone", "無損", "高解析度音訊", "dsd播放器ios", "usb dac iphone", "384khz", "音樂", "flacbox", "串流播放", "離線", "等化器", "dsp", "音樂視覺化工具", "bass引擎"]
tags: ["音樂", "雲端", "播放器", "下載器", "等化器", "無損", "高解析度", "離線", "FLAC", "DSD", "DAC", "串流媒體", "視覺化工具", "DSP"]
readingTime: 8
---

{{< author-byline >}}


**摘要:** 要在iPhone上播放FLAC,你需要一款第三方播放器,因為Apple的Music應用程式不支援FLAC。安裝[Flacbox](/products/flacbox)(免費),然後透過Wi-Fi Drive或USB傳輸檔案,或者連接你的雲端儲存或NAS。你的FLAC音樂庫將以完整品質播放,透過USB DAC可達384 kHz和32-bit。Flacbox還能播放120多種格式,包括FLAC、DSD、ALAC、APE、WAV、OGG和OPUS,並加入了10段等化器、帶即時效果的專業BASS音訊引擎、DSP處理器以及全螢幕音樂視覺化工具。

[{{< figure src="/docs/howto/how-to-play-flac-music-on-iphone/Flacbox_Icon-App-1024x1024.webp" alt="Flacbox Icon - FLAC music player and downloader" width="160" >}}](/products/flacbox)

## 為什麼我的iPhone無法原生播放FLAC?

Apple有自己的無損格式,稱為ALAC(Apple Lossless),而Music應用程式是圍繞它建構的,而不是FLAC。自iOS 11起,Files應用程式可以預覽單個FLAC檔案,但它沒有音樂庫、播放列表、播放佇列、等化器,也沒有雲端串流播放。它是一個檔案檢視器,而不是音樂播放器。

因此你有兩個真正的選擇:

1. 使用播放器應用程式播放FLAC,讓你的檔案保持原樣。這是我們推薦的方案。
2. 將FLAC轉換為ALAC,這是從無損到無損的轉換,然後與Music應用程式同步。

如果你擁有一個真正的FLAC收藏,第一個選擇更好。你避免了重複的音樂庫,省去了轉換時間,而且你的資料夾和高解析度品質都保持不變。Flacbox正是為此而生。

## 選擇1:使用Flacbox播放FLAC

Flacbox是一款適用於iPhone、iPad和Mac的高解析度音樂播放器。它將你的雲端儲存、NAS或電腦變成你自己的私人音樂庫,無需轉換,也無需訂閱。

### 第1步。安裝Flacbox

Flacbox可免費下載,並可在iPhone、iPad和Mac上執行。

{{< app-details product="flacbox" >}}

### 第2步。匯入你的FLAC檔案

選擇對你來說最簡單的方式:

- **Wi-Fi Drive** — 打開連接,然後電腦,再選擇透過Wi-Fi連接,並從任意桌面瀏覽器拖入檔案。請參閱[Wi-Fi Drive指南](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)。
- **雲端儲存** — 連接iCloud Drive、Google Drive、Dropbox、OneDrive、Box、MEGA、pCloud、Proton Drive以及另外20種服務,然後直接從雲端串流播放。
- **NAS或電腦** — 透過SMB、WebDAV、DLNA、FTP、SFTP或NFS連接(Synology、QNAP、WD My Cloud、Time Capsule,或任意Samba共用)。完整列表見[連接指南](/docs/guide/flacbox/flacbox-guide-connections)。
- **USB隨身碟** — 插入SanDisk iXpand或任意外接讀卡機,並[直接從磁碟機播放](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it),無需匯入。
- **iTunes或Finder檔案共享** — 透過Lightning或USB-C線纜。

### 第3步。按下播放

你的曲目會出現在音樂庫中,標籤和封面圖直接從檔案本身讀取,並按專輯、演出者、類型和作曲者分組。每首曲目都會顯示其確切的編解碼器和解析度,例如FLAC、96 kHz、24-bit。

## 高解析度輸出、USB DAC與多聲道

Flacbox專為在意音質的人打造,而不僅僅是隨意播放:

- **取樣率** — 從8 kHz播放至384 kHz,多聲道輸出可從1到7聲道(最高5.1和ITU BS.775-1)。
- **USB DAC支援** — 任何高於48 kHz的內容都能透過USB DAC以其真實解析度播放。透過iPhone自身的輸出,iOS會像對待每個應用程式那樣對音訊重新取樣,因此DAC是獲得位元完美高解析度的方式。
- **可調輸出** — 在設定,然後音訊播放器中,設定取樣率、聲道數量和IO緩衝時長(約5 ms可實現低延遲高解析度)。
- **音調與速度** — 精細的音調校正,以及從0.02×到3.00×的播放速度。

## 播放120多種格式,不僅僅是FLAC

除了FLAC,Flacbox還捆綁了FFmpeg,因此它可以播放iOS無法自行開啟的格式。你無需事先轉換或整理混合的音樂庫:

- **無損與高解析度** — FLAC、ALAC、WAV、AIFF、APE、WV(WavPack)以及DSD(DSF和DFF,包括DSD64、DSD128和DSD256)。
- **有損** — MP3、AAC、M4A、OGG、OPUS、WMA、MPC等。
- **Tracker和MOD音樂** — 經典的MOD、XM、IT、S3M、MTM、UMX和MO3等chiptune與demoscene檔案,大多數播放器都無法開啟。

這樣總共超過120種格式,幾乎涵蓋了現代音樂收藏中的任何內容。

## 三種音訊引擎,包括BASS引擎

你可以在設定,然後音訊播放器,再到音訊編解碼器中選擇播放引擎:

- **System Codec + FFmpeg** — 最大程度的相容性和穩定性。
- **FFmpeg** — 強制使用FFmpeg路徑,可解鎖音調校正和自訂輸出取樣率。
- **BASS™引擎** — 在[Flacbox 7.6](/blog/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer)中加入的專業播放核心。它可解鎖即時音訊效果、DSP處理器、音樂視覺化工具、Tracker和MOD播放以及高品質重新取樣。它還增加了獨立的音調控制(±60 semitones)和速度控制(0.1× to 4×)。

## 10段等化器、低音增強與前級放大

Flacbox包含一個10段圖形等化器,帶有類似iPod的預設,如Acoustic、Bass Booster、Rock、Pop、Jazz、Classical和Dance。有一個前級放大器可在不削波的情況下提升安靜曲目的音量,你還可以儲存自己的預設。為入耳式監聽耳機、HomePod或車載音響進行調音。有關完整教學,請參閱[等化器指南](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox)。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox音訊播放器等化器" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## 即時音訊效果

當BASS引擎開啟時,你可以獲得十一種即時效果,可在音樂播放時疊加和調整。任何內容都不會被重新編碼,關閉某個效果會立即恢復原始聲音:

- **殘響** — 從小房間到大教堂。
- **延遲與多重回聲** — 從緊湊的slapback到悠長的氛圍餘韻。
- **交叉饋送** — 混合立體聲聲道,使耳機在硬聲像混音上聽起來更像真實的揚聲器。
- **壓縮器** — 均衡響亮和安靜的部分,非常適合車內或健身房。
- **Chorus、Flanger、Phaser、Auto-Wah、Distortion和Stereo Rotation** — 富有創意的調變與音色效果。

Flacbox還具備基於廣播級EBU R128響度標準的自動音量平衡功能。專輯和隨機播放列表會以穩定的音量播放,因此你不必總是去調整音量。它自帶Light、Standard、Strong和Night預設。

## 建構你自己的DSP處理器

除了效果之外,Flacbox還為你提供一個由你自己設定的即時14濾波器DSP處理器。你可以新增專業濾波器和參數EQ頻段、飽和度和bit crusher,以及像顫音、環形調變器和立體聲寬度這樣富有創意的處理器。它全部對你播放的任何內容即時執行,從本地FLAC到雲端串流,而且DSP設定甚至在CarPlay中也可用。

## 全螢幕音樂視覺化工具

Flacbox內建一個音樂視覺化工具,可隨著你的音樂節奏繪製流動、多彩的視覺效果。它使用著名的Milkdrop引擎(projectM),帶有500個預設,在iPhone、iPad和Mac上用OpenGL繪製。在播放器中點擊更多操作按鈕,然後選擇視覺化即可開啟。選擇一個預設,或使用Auto模式每30 秒切換一次並平滑交叉淡入淡出。有關逐步協助,請參閱關於[如何開啟音樂視覺化工具](/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac)的指南。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox音樂視覺化工具 (Milkdrop and projectM)" image="/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac/music-visualizer-starfield-sectors-preset.webp" >}}
{{< /cards >}}

## 雲端、NAS與離線播放

直接從30多種雲端服務串流播放,包括iCloud Drive、Google Drive、Dropbox、OneDrive、Box、MEGA、pCloud、Proton Drive和Internxt。你還可以連接自架伺服器,如Plex、Jellyfin、Emby、Subsonic和Navidrome,以及透過SMB、WebDAV、DLNA、FTP、SFTP或NFS連接任意NAS。

當你想隨身攜帶音樂時,內建的下載管理器可儲存整個播放列表、演出者、專輯或資料夾以供離線聆聽。離線模式隨後會在新曲目出現在雲端時自動同步它們。空間不足?一鍵清除快取即可繼續串流播放。

## 認真的聽眾想要的一切

- **有序的音樂庫** — 按歌曲、專輯、專輯演出者、演出者、類型和作曲者分組,配有可離線使用的快速搜尋。
- **ID3標籤編輯器** — 修復混亂的中繼資料和損壞的編碼(西里爾文、日文、中文),並將變更寫回檔案。
- **播放列表** — 建立、重新排序、匯入和匯出M3U、M3U8和CUE,並可離線使用。
- **Apple CarPlay** — 專用的車內螢幕,用於音樂庫、雲端、本地和離線音樂,並內建等化器。
- **AirPlay 2和Chromecast** — 投放到HomePods、Apple TV和支援Cast的揚聲器。
- **有聲書工具** — 多個書籤、可調速度、睡眠計時器,以及從上次停止處繼續。
- **小工具及更多** — 主畫面和鎖定畫面小工具、Last.fm記錄、定時歌詞和LRC,以及完整的VoiceOver無障礙功能。

Flacbox可免費下載。Premium會解除免費版對雲端帳戶、播放列表和離線資料夾的限制,並提供一次性終身購買或按月/按年訂閱,支援家人共享。

{{< app-details product="flacbox" >}}

## 選擇2:將FLAC轉換為ALAC以用於Music應用程式

如果你確實想讓你的擷取檔案進入Apple的Music應用程式,你可以轉換它們。FLAC到ALAC是從無損到無損,因此你不會損失任何品質:

1. 在你的電腦上,使用像Mac上的XLD或Windows上的foobar2000這樣的免費工具批次轉換。兩者都會保留你的標籤。
2. 將ALAC檔案新增到你的Music或iTunes音樂庫中。
3. 在Mac上用Finder或在Windows上用Apple Devices應用程式同步到iPhone。

代價是實實在在的。現在你保留了兩份音樂庫副本,每次中繼資料編輯都意味著又一次同步,而且Music應用程式的版面固定不變,沒有基於規則的播放列表,沒有等化器,沒有DSP,裝置上也沒有雲端或NAS串流播放。這就是為什麼大多數擁有認真FLAC收藏的人會選擇第一個選項。

## 常見問題

{{% details title="iPhone可以原生播放FLAC檔案嗎?" closed="true" %}}
僅在有限範圍內。自iOS 11起,Files應用程式可以預覽單個FLAC檔案,但沒有音樂庫、播放列表、播放佇列、等化器或雲端串流播放。要真正聆聽,請使用像Flacbox這樣的播放器應用程式。
{{% /details %}}

{{% details title="我可以在iPhone上播放24-bit或96kHz(或更高)的FLAC嗎?" closed="true" %}}
可以。Flacbox支援高達384 kHz的高解析度輸出。要以真實解析度播放高於48 kHz的內容,請連接外接USB DAC,因為iPhone的內建輸出會為每個應用程式重新取樣音訊。
{{% /details %}}

{{% details title="Flacbox會將FLAC轉換為其他格式嗎?" closed="true" %}}
不會。Flacbox以其原始無損品質播放FLAC,無需轉換。效果和DSP僅在播放期間即時套用,它們從不改變你的檔案。
{{% /details %}}

{{% details title="將FLAC轉換為ALAC會損失品質嗎?" closed="true" %}}
不會。FLAC和ALAC都是無損格式,因此轉換是位元完美的。你只是花費時間並放棄便利,因為你最終會有兩個需要維護的音樂庫,並且在編輯後必須重新同步。
{{% /details %}}

{{% details title="Flacbox支援哪些音訊格式?" closed="true" %}}
超過120種格式,包括FLAC、DSD(DSF和DFF)、ALAC、APE、WAV、AIFF、WV、OGG、OPUS、MP3、AAC、M4A、WMA,甚至還有MOD、XM、IT和S3M等Tracker和MOD音樂。
{{% /details %}}

{{% details title="Flacbox有等化器、效果和視覺化工具嗎?" closed="true" %}}
有。它有一個帶預設和前級放大器的10段等化器。它還有一個專業的BASS引擎,帶有十一種即時效果(殘響、延遲、多重回聲、交叉饋送、壓縮器、chorus、flanger、phaser、auto-wah、distortion和stereo rotation),外加EBU R128音量平衡、一個14濾波器DSP處理器,以及一個帶500個預設的全螢幕Milkdrop視覺化工具。
{{% /details %}}

{{% details title="我可以從我的NAS或雲端串流播放FLAC嗎?" closed="true" %}}
可以。Flacbox可連接到30多種雲端服務,並可透過SMB、WebDAV、DLNA、FTP、SFTP和NFS連接到NAS或電腦。你的整個音樂庫無需將檔案複製到iPhone即可使用,而且你可以隨時下載曲目以供離線播放。
{{% /details %}}

{{% details title="Flacbox真的免費嗎?" closed="true" %}}
Flacbox可免費下載,包含等化器、雲端串流播放和離線播放等核心功能。Premium會解除免費版對雲端帳戶、播放列表和離線資料夾的限制,並以一次性終身購買或按月/按年訂閱的形式提供,支援家人共享。
{{% /details %}}
