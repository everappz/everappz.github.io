---
title: "標籤編輯器"
date: 2020-02-01
description: "了解如何使用 Evertag 標籤編輯器更新音樂元資料、編輯專輯封面、批次編輯多個檔案以及管理來自 MusicBrainz 的標籤。非常適合在 iOS 和 Mac 上整理音樂庫。"
keywords: [
  "Evertag 標籤編輯器", "音訊元資料編輯器", "音樂標籤編輯器",
  "iPhone 編輯音訊標籤", "專輯封面編輯器", "批次編輯音訊標籤",
  "MusicBrainz 元資料", "音樂整理應用程式", "Evertag 指南", "ID3 標籤編輯器"
]
tags: ["指南", "evertag", "標籤編輯器"]
readingTime: 5
---


**標籤編輯器**是 Evertag 應用程式的主畫面，您可以在此查看和編輯音訊檔案元資料。透過點選**本機檔案**部分中的檔案或從任何已連接的**雲端儲存**帳戶開啟此畫面。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag Editor Screen" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## 編輯模式

Evertag 提供兩種編輯模式：

- **單檔案模式**  
  - 透過在封面輪播上向左或向右滑動在檔案之間導航。  

- **批次模式**  
  - 同時編輯多個檔案並套用共享元資料。  
  - 要啟動，向下捲動並點選**同時編輯檔案**。

## 單檔案模式

預設情況下，應用程式以單檔案模式開啟標籤編輯器，僅啟用主要編輯選項。在此模式下，您可以編輯最常見的元資料欄位，例如：

**曲目標題、副標題、專輯藝術家、專輯、藝術家、作曲家、表演者、流派、評論、每分鐘節拍數、播客、合輯、碟號、曲目號、曲目總數、評分、年份**

要存取所有可用標籤，向下捲動到畫面底部並點選**顯示擴展標籤**選項。這將把編輯器切換到擴展模式，允許您編輯超過 **120 個元資料欄位**，包括 **MusicBrainz 標籤**、**歌詞**、**內容分級**、replay-gain 值、排序順序、播客元資料等。使用**設定 → 音訊標籤編輯器 → 主畫面按鈕**永久切換顯示擴展標籤。

{{< cards cols="1">}}
{{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## 批次模式

您可以透過兩種方式進入批次編輯：

1. **從檔案管理器**  
   - 點選右上角的**更多操作** (•••)。  
   - 點選**選擇**，選擇多個檔案，然後點選**編輯音訊標籤**。

2. **從標籤編輯器**  
   - 開啟任何檔案，向下捲動，點選**同時編輯檔案**以載入同一資料夾中的所有檔案。

{{< cards cols="1">}}
{{< card title="" subtitle="Batch Editing Mode" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

編輯後，點選**儲存**以套用變更。

## 編輯歌詞

擴展編輯器提供**歌詞**欄位。點選它可開啟歌詞列表——每個歌詞條目都有自己的語言和描述，因此一首曲目可以儲存多個翻譯版本。

您無需從頭輸入歌詞。編輯器包含一鍵搜尋捷徑，連結到網路上最流行的歌詞資料庫，預填當前曲目的藝術家和標題：

- **Lrclib** — **帶時間戳 (LRC 格式) 歌詞**的首選公共資料庫。當您需要在支援它的播放器中逐行捲動的同步歌詞時使用。
- **Genius** — 包含注釋和準確純文字歌詞的大型目錄。
- **Lyricsify** — 包含普通和帶時間戳歌詞的社群驅動資料庫。
- **Google** — 當專用資料庫沒有匹配項時作為通用網路搜尋後備。

每個捷徑只在相應服務從您的裝置可存取時顯示。點選一個服務，複製您想要的歌詞（或 LRC 時間戳），返回 Evertag，將其貼上到文字欄位中——然後點選**儲存**將歌詞寫回音訊檔案的標籤。

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Pages" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

從選擇器中選擇語言：

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Language Selector" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

然後貼上或輸入歌詞文字。Evertag 支援純文字和帶時間戳（同步）歌詞——預留位置顯示 LRC 格式的範例，這正是 Lrclib 和 Lyricsify 為同步結果返回的內容。

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Text Editor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## 設定評分和內容分級

擴展編輯器提供星級**評分**控制項以及**內容分級**分段控制項。

### 星級評分

使用**評分**欄位為曲目打一到五星的個人評分。該值寫入檔案的標準評分標籤（ID3 的 POPM、MP4 的 `rate`、Vorbis/APE 的 `RATING` 等），因此其他讀取此標籤的應用程式——包括 Music 應用程式、Plex、Roon 和大多數桌面標籤編輯器——會立即獲取您的評分。

{{< cards cols="1">}}
  {{< card title="" subtitle="Rating" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### 內容分級

**內容分級**使用 iTunes Store 和大多數音樂平台使用的家長諮詢標準中的值之一標記曲目內容：

- **無冒犯** — 沒有家長諮詢資訊的曲目的預設值。檔案被視為適合所有聽眾，不會在尊重該標籤的播放器中顯示任何諮詢標籤。
- **明確** — 曲目包含明確的語言或內容。尊重家長控制的播放器（Music 應用程式、Apple TV 應用程式、Spotify 匯出、Plex 等）將在標題旁顯示 **E** 標誌。
- **乾淨** — 明確曲目的審查或編輯版本。播放器顯示 **C** 標誌，讓聽眾區分乾淨編輯版本和原始明確母帶。

以下情況需要設定或修復此欄位：

- 檔案有錯誤標籤（例如被錯誤標記為明確的乾淨電台編輯版，或反之）。
- 曲目被翻錄或下載時沒有標籤，現在顯示為無冒犯，即使包含明確內容。
- 您正在為提交或分享準備專輯，需要每首曲目攜帶一致的元資料。
- 您希望 CarPlay、鎖定畫面、Apple Music 風格播放器或 DJ 軟體在曲目標題旁顯示正確的 **E** / **C** 標誌。

該值儲存在檔案格式的標準內容分級欄位中（MP4 的 `rtng`、ID3 的 `TXXX:ITUNESADVISORY`、Vorbis 的 `ITUNESADVISORY`），因此任何讀取家長諮詢元資料的播放器都會看到您的更新。

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Advisory Rating" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## 編輯專輯封面

要變更專輯封面：

1. 點選封面輪播中的**相機圖示**。  
2. 選擇圖像位置：本機檔案、雲端、下載或照片庫。  
3. 選擇要套用為封面藝術的圖像。

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## 標籤編輯器中的更多操作

額外的編輯選項透過封面視圖下方的工具列提供。

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### 自動搜尋音訊標籤

此操作啟動智慧標籤搜尋引擎，根據現有資訊為您的音訊檔案尋找並填入完整的元資料。  
應用程式使用 MusicBrainz 資料庫——最全面的標籤資料庫之一——擁有超過 **5000 萬**首曲目。

### 搜尋專輯封面

使用元資料在網路上搜尋正確的專輯封面。  

{{< cards cols="1">}}
  {{< card title="" subtitle="Search Album Cover" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

找到後，使用系統右鍵選單將圖像儲存到您的**照片**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Add Image to Photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

之後，返回標籤編輯器，點選相機圖示，前往**照片庫**，選擇已儲存的圖像。應用程式將其設定為您音訊檔案的封面。

您可以在應用程式設定中調整封面圖像的縮放方式。

### 儲存專輯封面

此操作將目前專輯封面儲存到**文件**資料夾，以便您以後重複使用。

### 規範化編碼

此操作將規範化音訊檔案元資料中所有標籤的文字編碼。如果您從 Windows PC 切換過來，檔案可能使用不同的編碼，在 Mac 上顯示為不可讀或亂碼字元，此功能特別有用。

### 手動搜尋標籤

使用 MusicBrainz 資料庫手動搜尋專輯元資料。  

- 選擇專輯  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- 選擇正確的歌曲  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Song" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- 選擇要套用哪些標籤  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Audio Tags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

點選**完成**將選定的元資料套用到您的曲目。

### 刪除音訊標籤

清除檔案的所有元資料欄位。從頭開始時很有用。點選**儲存**確認。

## 標籤編輯器設定

導覽至**設定 → 音訊標籤編輯器**以自訂行為。

### 專輯封面縮放

選擇將專輯封面儲存到音訊檔案時應如何縮放。您可以停用縮放以保留原始圖像大小，但請注意某些播放器可能不支援大型封面檔案。「原始大小」選項是 Premium 個人化功能的一部分。

### 標籤儲存選項

- **ID3v2.4** — 啟用時，應用程式盡可能以 ID3v2.4 格式儲存標籤。如果音訊標籤在較舊的播放器或裝置上無法正確顯示，請停用以退回到更廣泛支援的 ID3v2.3。
- **重複標籤** — 啟用時，通用元資料欄位被複製到檔案的兩個標籤部分。這提高了與舊版音訊播放器的相容性，但在大多數情況下不需要。

### 雲端檔案元資料更新選項

您可以控制應用程式如何更新存放在雲端服務中的音訊檔案元資料：

- **顯示確認訊息**  
  在將元資料變更套用到雲端檔案之前詢問。

- **自動更新檔案元資料**  
  編輯後自動將元資料變更儲存到雲端檔案。

- **不更新檔案元資料**  
  跳過更新雲端檔案——變更僅在本機套用。

### 編輯線上檔案

選擇編輯後雲端檔案的本機下載副本會發生什麼：

- **始終刪除已下載的檔案**  
  儲存變更後刪除本機副本。

- **不刪除已下載的檔案**  
  編輯後將已下載的檔案保留在裝置上。

### 主畫面按鈕

自訂哪些操作出現在標籤編輯器主畫面上（自動搜尋音訊標籤、手動搜尋音訊標籤、搜尋專輯封面、儲存專輯封面、規範化編碼、刪除音訊標籤）。您還可以切換**顯示擴展標籤**和**同時編輯檔案**，使編輯器始終以您偏好的模式開啟。
