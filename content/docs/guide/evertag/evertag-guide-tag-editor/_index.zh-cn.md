---
title: "标签编辑器"
date: 2020-02-01
description: "了解如何使用 Evertag 标签编辑器更新音乐元数据、编辑专辑封面、批量编辑多个文件以及管理来自 MusicBrainz 的标签。非常适合在 iOS 和 Mac 上整理音乐库。"
keywords: [
  "Evertag 标签编辑器", "音频元数据编辑器", "音乐标签编辑器",
  "iPhone 编辑音频标签", "专辑封面编辑器", "批量编辑音频标签",
  "MusicBrainz 元数据", "音乐整理应用", "Evertag 指南", "ID3 标签编辑器"
]
tags: ["指南", "evertag", "标签编辑器"]
readingTime: 5
---


**标签编辑器**是 Evertag 应用的主屏幕，您可以在此查看和编辑音频文件元数据。通过点击**本地文件**部分中的文件或从任何已连接的**云存储**账户打开此屏幕。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag Editor Screen" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## 编辑模式

Evertag 提供两种编辑模式：

- **单文件模式**  
  - 通过在封面轮播上向左或向右滑动在文件之间导航。  

- **批量模式**  
  - 同时编辑多个文件并应用共享元数据。  
  - 要激活，向下滚动并点击**同时编辑文件**。

## 单文件模式

默认情况下，应用以单文件模式打开标签编辑器，仅启用主要编辑选项。在此模式下，您可以编辑最常见的元数据字段，例如：

**曲目标题、副标题、专辑艺术家、专辑、艺术家、作曲家、表演者、流派、评论、每分钟节拍数、播客、合辑、碟号、曲目号、曲目总数、评分、年份**

要访问所有可用标签，向下滚动到屏幕底部并点击**显示扩展标签**选项。这将把编辑器切换到扩展模式，允许您编辑超过 **120 个元数据字段**，包括 **MusicBrainz 标签**、**歌词**、**内容分级**、replay-gain 值、排序顺序、播客元数据等。使用**设置 → 音频标签编辑器 → 主屏幕按钮**永久切换显示扩展标签。

{{< cards cols="1">}}
{{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## 批量模式

您可以通过两种方式进入批量编辑：

1. **从文件管理器**  
   - 点击右上角的**更多操作** (•••)。  
   - 点击**选择**，选择多个文件，然后点击**编辑音频标签**。

2. **从标签编辑器**  
   - 打开任何文件，向下滚动，点击**同时编辑文件**以加载同一文件夹中的所有文件。

{{< cards cols="1">}}
{{< card title="" subtitle="Batch Editing Mode" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

编辑后，点击**保存**以应用更改。

## 编辑歌词

扩展编辑器提供**歌词**字段。点击它可打开歌词列表——每个歌词条目都有自己的语言和描述，因此一首曲目可以存储多个翻译版本。

您无需从头输入歌词。编辑器包含一键搜索快捷方式，链接到网络上最流行的歌词数据库，预填当前曲目的艺术家和标题：

- **Lrclib** — **带时间戳 (LRC 格式) 歌词**的首选公共数据库。当您需要在支持它的播放器中逐行滚动的同步歌词时使用。
- **Genius** — 包含注释和准确纯文本歌词的大型目录。
- **Lyricsify** — 包含普通和带时间戳歌词的社区驱动数据库。
- **Google** — 当专用数据库没有匹配项时作为通用网络搜索后备。

每个快捷方式只在相应服务从您的设备可访问时显示。点击一个服务，复制您想要的歌词（或 LRC 时间戳），返回 Evertag，将其粘贴到文本字段中——然后点击**保存**将歌词写回音频文件的标签。

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Pages" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

从选择器中选择语言：

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Language Selector" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

然后粘贴或输入歌词文本。Evertag 支持纯文本和带时间戳（同步）歌词——占位符显示 LRC 格式的示例，这正是 Lrclib 和 Lyricsify 为同步结果返回的内容。

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Text Editor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## 设置评分和内容分级

扩展编辑器提供星级**评分**控件以及**内容分级**分段控件。

### 星级评分

使用**评分**字段为曲目打一到五星的个人评分。该值写入文件的标准评分标签（ID3 的 POPM、MP4 的 `rate`、Vorbis/APE 的 `RATING` 等），因此其他读取此标签的应用——包括 Music 应用、Plex、Roon 和大多数桌面标签编辑器——会立即获取您的评分。

{{< cards cols="1">}}
  {{< card title="" subtitle="Rating" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### 内容分级

**内容分级**使用 iTunes Store 和大多数音乐平台使用的家长咨询标准中的值之一标记曲目内容：

- **无冒犯** — 没有家长咨询信息的曲目的默认值。文件被视为适合所有听众，不会在尊重该标签的播放器中显示任何咨询标签。
- **明确** — 曲目包含明确的语言或内容。尊重家长控制的播放器（Music 应用、Apple TV 应用、Spotify 导出、Plex 等）将在标题旁显示 **E** 标志。
- **干净** — 明确曲目的审查或编辑版本。播放器显示 **C** 标志，让听众区分干净编辑版本和原始明确母带。

以下情况需要设置或修复此字段：

- 文件有错误标签（例如被错误标记为明确的干净电台编辑版，或反之）。
- 曲目被翻录或下载时没有标签，现在显示为无冒犯，即使包含明确内容。
- 您正在为提交或分享准备专辑，需要每首曲目携带一致的元数据。
- 您希望 CarPlay、锁屏、Apple Music 风格播放器或 DJ 软件在曲目标题旁显示正确的 **E** / **C** 标志。

该值存储在文件格式的标准内容分级字段中（MP4 的 `rtng`、ID3 的 `TXXX:ITUNESADVISORY`、Vorbis 的 `ITUNESADVISORY`），因此任何读取家长咨询元数据的播放器都会看到您的更新。

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Advisory Rating" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## 编辑专辑封面

要更改专辑封面：

1. 点击封面轮播中的**相机图标**。  
2. 选择图像位置：本地文件、云端、下载或照片库。  
3. 选择要应用为封面艺术的图像。

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## 标签编辑器中的更多操作

额外的编辑选项通过封面视图下方的工具栏提供。

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### 自动搜索音频标签

此操作激活智能标签搜索引擎，根据现有信息为您的音频文件查找并填充完整的元数据。  
应用使用 MusicBrainz 数据库——最全面的标签数据库之一——拥有超过 **5000 万**首曲目。

### 搜索专辑封面

使用元数据在网络上搜索正确的专辑封面。  

{{< cards cols="1">}}
  {{< card title="" subtitle="Search Album Cover" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

找到后，使用系统上下文菜单将图像保存到您的**照片**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Add Image to Photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

之后，返回标签编辑器，点击相机图标，转到**照片库**，选择保存的图像。应用程序将其设置为您音频文件的封面。

您可以在应用设置中调整封面图像的缩放方式。

### 保存专辑封面

此操作将当前专辑封面保存到**文档**文件夹，以便您以后重复使用。

### 规范化编码

此操作将规范化音频文件元数据中所有标签的文本编码。如果您从 Windows PC 切换过来，文件可能使用不同的编码，在 Mac 上显示为不可读或乱码字符，此功能特别有用。

### 手动搜索标签

使用 MusicBrainz 数据库手动搜索专辑元数据。  

- 选择专辑  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- 选择正确的歌曲  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Song" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- 选择要应用哪些标签  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Audio Tags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

点击**完成**将选定的元数据应用到您的曲目。

### 删除音频标签

清除文件的所有元数据字段。从头开始时很有用。点击**保存**确认。

## 标签编辑器设置

导航到**设置 → 音频标签编辑器**以自定义行为。

### 专辑封面缩放

选择将专辑封面保存到音频文件时应如何缩放。您可以禁用缩放以保留原始图像大小，但请注意某些播放器可能不支持大型封面文件。「原始大小」选项是 Premium 个性化功能的一部分。

### 标签保存选项

- **ID3v2.4** — 启用时，应用尽可能以 ID3v2.4 格式保存标签。如果音频标签在较旧的播放器或设备上无法正确显示，请禁用以回退到更广泛支持的 ID3v2.3。
- **重复标签** — 启用时，通用元数据字段被复制到文件的两个标签部分。这提高了与旧版音频播放器的兼容性，但在大多数情况下不需要。

### 云文件元数据更新选项

您可以控制应用如何更新存储在云服务中的音频文件元数据：

- **显示确认消息**  
  在将元数据更改应用到云文件之前询问。

- **自动更新文件元数据**  
  编辑后自动将元数据更改保存到云文件。

- **不更新文件元数据**  
  跳过更新云文件——更改仅在本地应用。

### 编辑在线文件

选择编辑后云文件的本地下载副本会发生什么：

- **始终删除下载的文件**  
  保存更改后删除本地副本。

- **不删除下载的文件**  
  编辑后将下载的文件保留在设备上。

### 主屏幕按钮

自定义哪些操作出现在标签编辑器主屏幕上（自动搜索音频标签、手动搜索音频标签、搜索专辑封面、保存专辑封面、规范化编码、删除音频标签）。您还可以切换**显示扩展标签**和**同时编辑文件**，使编辑器始终以您偏好的模式打开。
