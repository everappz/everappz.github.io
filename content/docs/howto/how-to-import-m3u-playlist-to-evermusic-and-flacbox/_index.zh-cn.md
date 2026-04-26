---
title: "如何将M3U播放列表导入Evermusic和Flacbox"
date: 2024-01-31
description: "了解如何从云端、本地存储或设备将M3U、M3U8和CUE播放列表文件导入Evermusic和Flacbox。"
keywords: ["evermusic", "flacbox", "播放列表", "m3u", "m3u8", "cue", "导入", "音乐应用"]
tags: ["evermusic", "导入", "播放列表", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**摘要：** Evermusic和Flacbox支持从云存储、本地应用文件或您的设备导入M3U、M3U8和CUE播放列表文件。前往播放列表 > 更多 > 导入播放列表，选择来源，选择文件，应用将自动创建您的播放列表。

M3U，代表MP3 URL或Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator，是一种用于多媒体播放列表的计算机文件格式。其主要用途之一是创建指向互联网流的单条目播放列表文件。这些文件提供了对流媒体内容的便捷访问，通常用于下载、电子邮件和收听网络电台。

尽管M3U格式被广泛使用，但没有正式的规范；它已成为事实上的标准。M3U文件本质上是一个纯文本文件，指定一个或多个媒体文件的位置。根据编码方式，它以"m3u"或"m3u8"文件扩展名保存。文件中的每个条目指定一个媒体文件的位置，可以是绝对本地路径名、相对于M3U文件位置的本地路径名或URL。条目由换行符分隔，某些设备要求换行符表示为CR LF。

此外，M3U文件可以包含以"#"字符为前缀的注释。在扩展M3U中，"#"引入扩展M3U指令，这些指令可能支持以冒号":"结尾的参数。

在我们的应用Evermusic和Flacbox中，我们实现了M3U文件导入功能，消除了手动创建播放列表的需要。本指南将引导您从云存储、本地文件或设备上的文件直接将播放列表导入应用。

首先，导航到"播放列表"部分。然后，点击右上角的"更多"按钮。从出现的菜单中，选择"导入播放列表"选项。

![导入播放列表操作](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

在下一个屏幕上，选择文件位置。支持的选项包括：

- 已连接的云存储；
- 应用中的文件；
- 设备上的文件；

![选择文件位置](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

让我们选择已连接的云存储并打开包含播放列表文件的文件夹。支持的播放列表文件扩展名包括M3U、M3U8和CUE。选择播放列表文件并点击"完成"以确认您的选择。

![选择M3U文件](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

应用将解析播放列表文件并创建曲目列表。然后它将在存储中找到这些文件并编译最终的播放列表，该列表将被导入到音乐库中。确保您的M3U/CUE文件包含正确的媒体文件路径至关重要，并且文件应位于存储中的这些路径上。

![已导入的播放列表](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

应用同时支持相对路径和绝对文件URL。

例如：

使用相对路径的播放列表：

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

使用绝对URL的播放列表：

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

如果您导入的播放列表文件位于应用内（本地文件部分），则无需额外步骤。

但是，如果您想使用系统文件选择器导入位于设备上的播放列表，有一个重要事项需要注意。

由于安全策略，应用只能访问您使用系统文件选择器选择的文件。但是，播放列表文件可能包含指向设备上其他媒体文件的链接。要从设备导入播放列表，您必须选择一个包含播放列表文件和所有关联媒体文件的文件夹。在这种情况下，应用将扫描选定的文件夹，找到播放列表文件，构建曲目列表，并将其导入到音乐库中。

此外，您可以通过点击"更多操作"按钮并选择"从文件夹导入播放列表"来一次导入多个播放列表。应用将扫描文件夹内容，找到支持的播放列表文件并将其导入到库中。

## 常见问题

{{% details title="Evermusic和Flacbox支持哪些播放列表格式？" closed="true" %}}
两个应用都支持M3U、M3U8和CUE播放列表文件格式。这些涵盖了音乐播放器和媒体软件使用的最常见播放列表标准。
{{% /details %}}

{{% details title="我可以从云存储导入播放列表吗？" closed="true" %}}
可以。您可以从任何已连接的云存储服务导入播放列表文件，包括Google Drive、Dropbox、OneDrive和WebDAV服务器。
{{% /details %}}

{{% details title="为什么导入后有些曲目丢失了？" closed="true" %}}
播放列表文件必须包含指向您媒体文件的正确路径，并且这些文件必须存在于存储中指定的位置。请仔细检查M3U或CUE文件中的文件路径是否与实际文件位置匹配。
{{% /details %}}

{{% details title="我可以一次导入多个播放列表吗？" closed="true" %}}
可以。使用更多操作按钮并选择"从文件夹导入播放列表"。应用会扫描文件夹中所有支持的播放列表文件并一步导入。
{{% /details %}}

{{% details title="我需要手动创建播放列表吗？" closed="true" %}}
不需要。导入功能消除了手动创建播放列表的需要。只需将应用指向您现有的M3U、M3U8或CUE文件，它就会自动构建播放列表。
{{% /details %}}
