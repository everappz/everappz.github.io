---
title: 如何在 Evermusic 和 Flacbox 中将曲目合集导出为 M3U、CSV 和 TXT
date: 2024-01-31
description: 了解如何将 Evermusic 和 Flacbox 中的最近使用、收藏夹、播放列表和专辑导出为 M3U、CSV 或 TXT 格式。非常适合 Last.fm 记录和在其他设备上播放。
keywords: ["evermusic 导出", "flacbox 导出", "导出为 m3u", "导出播放列表为 csv", "m3u txt csv 播放列表", "音乐导出"]
tags: ["evermusic", "recents", "favorites", "export", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**摘要：** Evermusic 和 Flacbox 允许您将任何曲目合集（最近使用、收藏夹、播放列表、专辑）导出为 CSV、TXT 或 M3U 文件。使用这些导出文件可以向 Last.fm 记录播放历史、备份音乐库或在其他设备上播放您的播放列表。

## 简介

将应用中的最近使用、收藏夹、专辑和播放列表导出到外部文件非常实用。您可以使用这些文件在 [Last.fm](http://Last.fm) 等记录服务上更新收听历史，或在外部设备上收听播放列表。使用 Evermusic 和 Flacbox，这个过程非常简单。在这里，我们将向您展示如何将最近使用导出为 CSV/TXT，以及将播放列表导出为 M3U。不过，此功能适用于应用内的任何曲目合集。

## 选择格式

要导出最近使用的曲目，请打开「音乐库」部分，选择「最近使用」菜单项。

![音乐库](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

在下一个屏幕上，点击右上角的「更多」按钮，选择「导出歌曲列表」。

![导出最近使用](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

在「选择文件格式」屏幕上，您有几个选项 - CSV、TXT、M3U。

- CSV

这是逗号分隔值的缩写，非常适合将数据整理成整齐的表格格式。在目标文件中，您将找到艺术家名称、专辑名称、曲目名称、时间戳（您收听曲目的时间）、专辑艺术家名称和曲目时长等参数。您可以稍后使用该文件在 [Last.fm](http://Last.fm) 等记录服务上更新收听历史，如[此处](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/)所述。

- TXT

这是一个纯文本文件。简单直观，包含艺术家名称、专辑名称、曲目名称和时长等参数。如果您只需要文本形式的曲目列表，这会很有用。

- M3U

此格式是创建播放列表的事实标准。它的优点在于您可以导出歌曲列表，并在任何设备上欣赏曲目，即使您没有原始文件（如果选择了媒体文件的绝对 URL 选项进行导出）。在输出文件中，您将找到时长、艺术家名称、曲目名称和媒体文件位置等参数。

## CSV 格式

现在，让我们选择 CSV，看看会得到什么。只需选择 CSV 并点击「导出」按钮。

![选择文件格式](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

导出完成后，您将看到一个包含两个选项的提示。点击「显示文件」将在您的文档目录中显示结果文件。

![导出完成](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

现在您可以发送该文件、在外部文本编辑器中打开它，或用它在 [Last.fm](http://Last.fm) 上更新您的收听进度。

![包含结果文件的导出文件夹](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

输出 CSV 文件将包含以下格式的字段：

```
{艺术家名称},{专辑名称},{曲目名称},{时间戳 yyyy-MM-dd HH:mm:ss},{专辑艺术家名称},{曲目时长 HH:mm:ss}
```

例如：

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![导出的 csv 文件](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT 格式

输出 TXT 文件将包含以下格式的字段：

```
{序号}. {艺术家名称} - {专辑名称} - {曲目名称} (时长 HH:mm:ss)
```

例如：

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![导出的 txt 文件](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U 格式

接下来，我们将指导您将播放列表导出为 M3U 格式，这是播放列表文件的事实标准。成功导出播放列表的主要前提是播放列表中的所有文件必须位于同一存储位置，无论是 Google Drive 等云服务、本地文件还是设备上的文件。要开始导出过程，打开任意播放列表，点击右上角的「更多」按钮，然后选择「导出歌曲列表」菜单项。

![播放列表屏幕](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

在下一个屏幕上，选择「M3U」文件格式，您将看到「媒体文件位置类型」的两个选项：

![选择导出文件格式屏幕](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. 如果选择「相对路径」，播放列表将以相对于播放列表文件的媒体文件位置创建。例如：

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   在这种情况下，导出完成后请避免更改 M3U 文件的位置，否则会破坏媒体文件的路径。要开始播放您的播放列表，只需点击导出的播放列表文件，应用将自动在您的存储中找到媒体文件并开始播放。您甚至可以将播放列表导出到存储设备，然后在新设备上重新导入。

2. 如果选择「绝对 URL」，应用将为您的媒体文件生成直接 URL。这允许您在任何设备/应用上播放播放列表，而无需所有媒体文件都与播放列表文件位于同一存储位置。此选项仅支持能够生成直接文件 URL 的云存储服务。但请注意，在某些情况下，生成的 URL 可能有有限的有效期，一段时间后可能会过期。以下是支持的云服务列表：iCloud Drive、pCloud、PanBaidu、MyCloudHome、DLNA、MediaFire、OneDrive、Box、Dropbox、GoogleDrive、WebDav（访客模式下）  

输出的媒体文件 URL 类似于：

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

选择「媒体文件位置类型」后，点击「导出」。应用将提示您选择导出 M3U 文件的目标文件夹。点击「完成」确认选择。

![选择文件夹](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

应用将生成 M3U 文件并将其上传/移动到目标文件夹。

![正在上传 m3u 文件](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

导出完成后，将出现一个系统提示，提供「显示文件」选项。

![导出完成提示](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

点击此选项将在应用中显示导出的文件。

![文件列表中的导出 m3u 文件](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

如果在上一步中选择了「相对路径」作为「媒体文件位置类型」，输出文件将采用以下格式：

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![相对路径的 m3u 示例](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

对于「绝对 URL」选项，应用将生成以下格式的 M3U 文件：

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![绝对文件 URL 的 m3u 示例](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

您可以在任何支持 M3U 播放列表的设备/应用上打开该文件。

![在外部应用中打开的 m3u 播放列表](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## 总结

从 Evermusic 和 Flacbox 导出曲目让您完全掌控自己的音乐数据。无论是备份收听历史、向 Last.fm 记录播放数据，还是在外部设备上欣赏播放列表，M3U、CSV 和 TXT 这些导出选项都是为灵活性和兼容性量身定制的强大工具。充分利用这些功能，提升您在各平台间整理、分享和回顾音乐合集的体验。

## 常见问题

{{% details title="Last.fm 记录应该使用哪种导出格式？" closed="true" %}}
使用 CSV。它包含 Last.fm-Scrubbler-WPF 等记录工具所需的时间戳和完整元数据。
{{% /details %}}

{{% details title="除了播放列表，我能导出其他曲目合集吗？" closed="true" %}}
可以。您可以使用相同的步骤导出应用中的最近使用、收藏夹、专辑、播放列表以及任何其他曲目合集。
{{% /details %}}

{{% details title="我的 M3U 播放列表能在其他设备上使用吗？" closed="true" %}}
如果您在导出时选择了绝对 URL 选项，M3U 文件可以在任何支持 M3U 播放列表的设备上播放。请注意，某些云端 URL 可能会随时间过期。
{{% /details %}}

{{% details title="导出功能是免费的吗？" closed="true" %}}
是的。将曲目合集导出为 M3U、CSV 和 TXT 在 Evermusic 和 Flacbox 的免费版和高级版中均可使用。
{{% /details %}}

{{% details title="哪些云服务支持绝对 URL 导出？" closed="true" %}}
绝对 URL 导出支持 iCloud Drive、pCloud、PanBaidu、MyCloudHome、DLNA、MediaFire、OneDrive、Box、Dropbox、Google Drive 和 WebDAV（访客模式）。
{{% /details %}}
