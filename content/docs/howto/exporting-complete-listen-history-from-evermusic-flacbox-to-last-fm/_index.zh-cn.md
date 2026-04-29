---
title: "从Evermusic和Flacbox导出完整收听历史到Last.fm"
date: 2024-01-30
description: "了解如何从Evermusic和Flacbox导出音乐历史记录，并使用CSV文件和Windows版Last.fm Scrubbler工具上传到Last.fm。"
keywords: ["evermusic", "flacbox", "lastfm", "音乐历史", "scrobbling", "导出曲目", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "最近使用", "lastfm", "导出", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**摘要：** 将您的收听历史从Evermusic或Flacbox导出为CSV文件，然后使用Windows上的免费工具Last.fm-Scrubbler-WPF上传到Last.fm。两个应用程序都原生支持自动scrobble功能。

**更新：** 自动scrobble功能现已推出！在此了解更多：[/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling是一种简单的方式，可以自动将您正在播放的歌曲的基本信息（如标题和艺术家）保存到在线服务中。之后，您可以查看自己的收听历史。

[Last.fm](https://www.last.fm/home)由名为Audioscrobbler的音乐推荐系统驱动，免费提供此服务。它通过记录您收听的曲目（无论是来自网络电台、您的电脑还是各种便携式音乐设备）来创建您音乐品味的详细档案。您可以稍后访问该网站，获取与您音乐品味匹配的新艺术家或专辑推荐。

您可以使用免费工具将收听历史从Evermusic和Flacbox应用上传到[Last.fm](http://Last.fm)，我们将向您介绍具体操作方法。

打开应用程序的「音乐库」部分，滚动到「快速访问」部分。点击「最近使用」菜单项。

![音乐库屏幕](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

在「最近使用」屏幕上，点击右上角的「更多」按钮以激活「更多操作」菜单。点击「导出歌曲列表」菜单项。

![最近使用屏幕](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

在「选择文件格式」屏幕上，您可以选择目标文件的格式。可用选项 - CSV、TXT、M3U。

![选择文件格式屏幕](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV：即逗号分隔值（Comma-Separated Values），非常适合将数据组织成整齐的表格格式。在目标文件中，您将找到艺术家名称、专辑名称、曲目名称、时间戳（您收听曲目的时间）、专辑艺术家名称和曲目时长等参数。

TXT：这是一个纯文本文件。简单直接，参数包括艺术家名称、专辑名称、曲目名称和时长。

M3U：这种格式是创建播放列表的首选。它很棒，因为您可以导出歌曲列表并在任何设备上欣赏您的曲目，即使您没有原始文件（前提是您选择媒体文件的绝对URL选项）。在输出文件中，您将找到时长、艺术家名称、曲目名称和媒体文件位置等参数。

对于我们的任务，选择CSV是正确的选择。我们将使用此文件配合免费软件Last.fm-Scrubbler-WPF将收听历史上传到[Last.fm](http://Last.fm)服务。只需选择CSV并点击「导出」按钮。

![导出完成屏幕](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

导出完成后，只需点击「显示文件」按钮，应用程序将在您的文档文件夹中显示创建的文件。然后，点击文件名旁边的「更多操作」按钮，从菜单中选择「打开方式」选项。下一步是将导出的文件复制到您的桌面电脑。您可以通过从「打开方式」菜单中选择AirDrop选项轻松完成此操作。

![导出文件的更多操作](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

接下来，我们将使用一个免费的开源[Last.FM](http://Last.FM)客户端，该客户端仅在Windows平台上可用。此客户端允许您使用我们刚刚导出的CSV文件高效地更新[Last.FM](http://Last.FM)上的收听历史。

如果您目前没有使用Windows电脑，不用担心。您可以通过在Mac上安装VirtualBox并使用官方Windows开发环境镜像文件来访问此客户端。

以下是您需要做的：

- 从以下链接安装VirtualBox：[下载VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- 从此链接下载并安装Windows开发环境：[Windows开发环境](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

在您的Windows电脑上（或带有Windows Development镜像的VirtualBox应用中）下载并安装[Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - GitHub上可用的免费开源软件。我们在1.28版本上进行了测试，您可以在此处下载：[https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Last.fm-Scrubbler-WPF下载页面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

在「Assets」部分点击[Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip)下载安装包。解压下载的文件并打开解压后的文件夹。

- 重要提示

此应用仍处于测试版。应用创建者没有进行大量测试。他们建议先尝试scrobble到测试账户，看看您想要scrobble的内容是否正确。特别是如果您一次scrobble大量曲目。请谨慎使用您的账户。

运行 Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

在应用程序的主屏幕上，只需点击左下角的「未登录」以激活「添加账户」屏幕。

![添加账户屏幕](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

输入您的登录凭据。

![输入登录凭据屏幕](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

点击「Login」按钮添加您的账户。

![点击Login按钮添加您的账户。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

打开「File Parse Scrobbler」选项卡，开始从Evermusic应用导入CSV文件。

![打开File Parse Scrobbler选项卡，开始从Evermusic应用导入CSV文件。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

选择「Parser: CSV」并点击「Settings」按钮。

在下一个屏幕上，您可以选择CSV文件中参数的顺序。

各个字段可以用引号括起来，如果字段包含任何设定的分隔符，则必须用引号括起来。例如：

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

因此保留所有默认设置，您唯一需要更改的是启用「Has Fields Enclosed In Quotes」字段中的复选框。

点击「Save & Close」应用更改。

![选择CSV文件中参数的顺序。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

文件解析scrobbling有两种模式。可以通过「Scrobbling Mode」下拉框更改。

普通模式：在此模式下，曲目将使用解析的scrobble时间戳进行scrobble。只有14天内的scrobble才能被scrobble。

导入模式：在此模式下，曲目将使用从「Finish Time」和每个曲目之间选定的时长计算出的时间戳进行scrobble。这允许即使解析的scrobble时间戳超过14天也能scrobble曲目。因此，CSV文件中的第一个（最上面的）曲目将使用「Finish Time」进行scrobble。

在「File:」字段中选择之前从Evermusic应用生成的CSV文件，然后点击「Parse」。在某些情况下，您可能会看到错误提示，说某些scrobble无法解析。如果您有一些缺少完整元数据（如艺术家名称）的曲目，这是正常的。

![某些scrobble无法解析](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

点击「Check All」按钮选择所有已解析的曲目。

![点击Check All按钮选择所有已解析的曲目。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

点击「Preview」按钮检查将要发送到服务器的所有更改。

![点击Preview按钮检查将要发送到服务器的所有更改。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

点击「Scrobble」按钮将所有更改上传到服务器。

![点击Scrobble按钮将所有更改上传到服务器。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

之前Last.fm-Scrubbler-WPF没有每日scrobble限制。现在已经改变了，因为一些人使用Scrubbler scrobble了太多曲目，导致Last.fm页面出现问题。目前scrobble限制为每天2800次。当您尝试scrobble超过此数量时，将收到错误消息。计划添加「scrobble队列」功能，这样如果您需要scrobble超过2800个曲目，它们将被添加到队列中，过一段时间后自动scrobble。您可以在用户选择视图中查看剩余的scrobble次数。

当所有记录成功上传到服务器后，您将在应用窗口底部看到确认消息：'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

现在您可以在[Last.fm](http://Last.fm)页面上打开您的个人资料并检查所有更改。

![您在Last.fm页面上的个人资料](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## 常见问题

{{% details title="我可以不导出CSV文件而自动scrobble吗？" closed="true" %}}
可以。Evermusic和Flacbox现在都支持自动Last.fm scrobble。请参阅指南：[如何Scrobble到Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)。
{{% /details %}}

{{% details title="如果我的CSV中有超过14天的曲目怎么办？" closed="true" %}}
在Last.fm-Scrubbler-WPF中使用导入模式。它从Finish Time重新计算时间戳，允许您不受原始日期限制地scrobble曲目。
{{% /details %}}

{{% details title="我没有Windows电脑。我还能使用Last.fm-Scrubbler吗？" closed="true" %}}
可以。在Mac上安装VirtualBox并从Microsoft下载免费的Windows开发环境镜像。在虚拟机中运行Last.fm-Scrubbler-WPF。
{{% /details %}}

{{% details title="为什么某些scrobble没有被解析？" closed="true" %}}
缺少必要元数据（如艺术家名称）的曲目无法被解析。这是正常的，不会影响文件中的其他曲目。
{{% /details %}}

{{% details title="有每日scrobble限制吗？" closed="true" %}}
有。Last.fm-Scrubbler-WPF允许每天最多2,800次scrobble。如果您需要scrobble更多，请将过程分散到多天进行。
{{% /details %}}
