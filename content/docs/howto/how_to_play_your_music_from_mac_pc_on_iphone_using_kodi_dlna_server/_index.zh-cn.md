---
title: "如何使用 Kodi DLNA 服务器在 iPhone 上播放 Mac / PC / Linux / NAS 中的音乐"
date: 2025-07-25
description: "使用 Kodi DLNA 和 Evermusic 应用通过 Wi-Fi 将电脑或 NAS 中的音乐流式传输到 iPhone。"
keywords: ["kodi dlna 服务器", "将音乐流式传输到 iphone", "从 nas 播放音乐", "evermusic dlna", "mac 到 iphone 音乐", "windows 到 iphone 音乐", "kodi dlna iphone", "dlna 音频流"]
tags: ["dlna", "kodi", "evermusic", "iphone", "音乐流式传输", "mac", "nas", "linux", "本地网络"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** 在 Mac、PC、Linux 或 NAS 上安装 Kodi，启用 DLNA/UPnP 服务器，使用免费的 Evermusic 或 Flacbox 应用通过 Wi-Fi 将整个音乐库流式传输到 iPhone 或 iPad。无需订阅。

## 简介

如果您有 **Mac、Windows PC、Linux 电脑或 NAS 设备**，您可以使用 [Kodi](https://kodi.tv/)（一个免费的开源媒体平台）轻松将其转变为家中的**个人音乐服务器**。借助 Kodi 内置的 **DLNA/UPnP 服务器**，您可以将整个音乐库流式传输到任何兼容 DLNA 的客户端——包括您的 iPhone 或 iPad。

在本指南中，我们将逐步向您展示如何：

- 在 Mac 或 PC 上安装 Kodi
- 设置音乐文件夹以进行共享
- 启用 DLNA 音乐服务器
- 使用 **Evermusic** 或 **Flacbox** iOS 应用访问音乐

此设置 100% 免费——无需订阅，只需通过 Wi-Fi 网络流式传输您自己的音乐。无论您是想整理大量 MP3 收藏、通过 Wi-Fi 收听 FLAC，还是只想在不通过 iTunes 同步的情况下享受本地音乐，此设置都非常适合您。

## 在 Mac / PC / Linux / NAS 上下载并安装 Kodi

首先，访问 Kodi 官方网站：

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi 主页" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

点击**下载**并向下滚动找到适合您电脑的版本。
选择您的操作系统。在此示例中，我们将使用 **macOS**。

{{< cards cols="1">}}
{{< card subtitle="Kodi 下载页面" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

如果您有 Intel Mac，请点击 **Intel (x86/64)**，或者为 M1、M2、M3 Mac 点击 **Apple Silicon** 开始下载。

{{< cards cols="1">}}
{{< card subtitle="选择 macOS 安装程序" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

请稍等，安装程序正在下载。

{{< cards cols="1">}}
{{< card subtitle="Kodi 已下载" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

下载后，在**下载**文件夹中找到 `.dmg` 文件。

{{< cards cols="1">}}
{{< card subtitle="安装 Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

双击下载的文件以启动安装程序。
将 Kodi 拖到**应用程序**文件夹中进行安装。

{{< cards cols="1">}}
{{< card title="" subtitle="将 Kodi 拖到应用程序中安装" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

启动 Kodi。您可能需要在**系统偏好设置 → 安全性与隐私 → 仍然打开**中允许它。

{{< cards cols="1">}}
{{< card subtitle="Kodi 主屏幕" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## 将音乐添加到 Kodi 媒体库

从主屏幕点击**齿轮图标**（设置）。

{{< cards cols="1">}}
{{< card subtitle="Kodi 设置" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

导航到**媒体设置 → 媒体库**。启用视频库和音乐库的**启动时更新媒体库**以进行自动索引。

{{< cards cols="1">}}
{{< card subtitle="媒体库设置" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

然后转到**音乐**部分并点击**添加音乐**。

{{< cards cols="1">}}
{{< card subtitle="添加音乐文件夹" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

浏览并选择存储音乐的文件夹。

{{< cards cols="1">}}
{{< card subtitle="选择音乐源" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

将音乐源添加到 Kodi。

{{< cards cols="1">}}
{{< card subtitle="添加音乐源" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

确认并让 Kodi 扫描您的音乐库。

{{< cards cols="1">}}
{{< card subtitle="确认音乐源" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

请稍等，媒体库正在扫描和完全构建。

{{< cards cols="1">}}
{{< card subtitle="正在扫描音乐库" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## 启用 Kodi 的 DLNA 服务器

转到**设置 → 服务 → UPnP/DLNA**。

启用选项：**共享我的媒体库**。

Kodi 现在作为 DLNA 服务器在您的本地 Wi-Fi 网络上运行。

{{< cards cols="1">}}
{{< card subtitle="在 Kodi 中启用 DLNA" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## 打开 Kodi 媒体库

右键单击关闭设置窗口并打开 Kodi 主媒体库。

{{< cards cols="1">}}
{{< card title="" subtitle="右键单击访问 Kodi 媒体库" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## 下载 iOS 音乐流媒体应用

获取一个免费的 iOS DLNA 客户端应用，让您从各种云存储服务和 DLNA 服务器流式传输音乐。

- 如果您的收藏主要是 MP3 和其他标准音频格式，请使用 **Evermusic**。
- 如果您有 FLAC、ALAC 或 DSD 等格式的高分辨率音乐库，请选择 **Flacbox**。

两个应用都可在 **iOS** 和 **macOS** 上使用，且免费。

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="下载 Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="下载 Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## 添加 DLNA 源

下载 iOS 应用后，打开**所有连接**部分。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 应用主侧栏" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

向下滚动并点击**本地网络 - 可用设备**以发现 DLNA 服务器。
在此部分中，您将看到本地网络上所有可用的设备。您的 **Kodi DLNA 服务器**应该出现在这里。点击 Kodi 服务器进行连接。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 中的可用 DLNA 设备" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic 将显示通过 Kodi 共享的媒体库文件夹。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 中的 Kodi 音乐库" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

导航到**歌曲**文件夹以查看 DLNA 服务器上所有可用的音频文件。

{{< cards cols="1">}}
{{< card title="" subtitle="来自远程文件夹的歌曲" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

点击任何音频文件即可立即开始流式播放。

{{< cards cols="1">}}
{{< card title="" subtitle="在 Evermusic 中播放 MP3 文件" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

返回**连接**部分。添加的 DLNA 服务器现在将显示在这里。随时点击其图标重新连接。

您还可以在这里启用 **Last.fm 记录**。播放统计数据将保存到您的 Last.fm 账户中。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 中的连接" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## 构建音乐库

**Evermusic** 和 **Flacbox** 都允许您将音乐添加到媒体库，并按**元数据标签**（如艺术家、专辑、流派和作曲家）进行组织。

首先，打开**音乐库**部分。向下滚动到**工具和偏好设置**，然后点击**添加音乐**。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 音乐库" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

选择音乐源——在此选择**连接**。

{{< cards cols="1">}}
{{< card title="" subtitle="在 Evermusic 中添加新音乐" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

在连接中找到 **Kodi DLNA 服务器**并点击查看文件夹和文件。

{{< cards cols="1">}}
{{< card title="" subtitle="选择 DLNA 服务器导入音乐" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

选择要添加的文件夹或文件，然后点击**完成**。

{{< cards cols="1">}}
{{< card title="" subtitle="选择要添加的音乐文件夹" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

应用将扫描您选择的文件，并使用元数据将其组织到艺术家、专辑、流派和作曲家等部分。

{{< cards cols="1">}}
{{< card title="" subtitle="带分类的音乐库" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## 创建播放列表

您还可以创建自己的播放列表。

首先，打开**播放列表**标签页。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 中的播放列表标签页" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

点击**加号 (+)** 按钮并选择**新建播放列表**。

{{< cards cols="1">}}
{{< card title="" subtitle="创建新播放列表" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

输入播放列表名称并点击**保存**。

{{< cards cols="1">}}
{{< card title="" subtitle="输入播放列表名称" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

接下来，选择添加歌曲的来源——这里我们选择**媒体库**。

{{< cards cols="1">}}
{{< card title="" subtitle="向新播放列表添加歌曲" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

选择想要的歌曲并点击**完成**添加。

{{< cards cols="1">}}
{{< card title="" subtitle="从媒体库添加音乐到播放列表" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

选定的曲目现在将出现在创建的播放列表中。

{{< cards cols="1">}}
{{< card title="" subtitle="创建的播放列表显示在列表中" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

默认情况下，歌曲可用于流式播放。要离线收听，请启用**离线模式**——应用将下载所有播放列表曲目。

{{< cards cols="1">}}
{{< card title="" subtitle="播放列表已启用离线模式" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

点击**更多操作**按钮探索其他选项。您可以：

- 归档播放列表
- 更改专辑封面
- 重新排列曲目
- 以及更多实用功能

{{< cards cols="1">}}
{{< card title="" subtitle="更多播放列表操作可用" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## 总结

使用 **Evermusic** 和 **Flacbox**，将您的 iPhone、iPad 或 Mac 变成强大的 DLNA 音乐播放器非常简单。

- 直接从您的 **Kodi DLNA 服务器**流式传输 MP3 或高分辨率 FLAC
- 构建按元数据分组的个人音乐库（专辑、流派、作曲家）
- 创建和管理**自定义播放列表**
- 启用**离线模式**以便随时随地收听
- 连接到**多个云服务**和**本地网络设备**
- 使用 **Last.fm 集成**跟踪您的收听习惯

无论您是发烧友还是普通听众，Evermusic 和 Flacbox 都能为您提供无缝音乐流媒体和组织所需的一切。

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="下载 Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="下载 Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

立即开始构建您的个人音乐体验。

## 常见问题

{{% details title="Kodi 作为 DLNA 服务器是免费的吗？" closed="true" %}}
是的。Kodi 完全免费且开源。可在 macOS、Windows、Linux 和许多 NAS 设备上运行。
{{% /details %}}

{{% details title="Evermusic 和 Flacbox 是否支持通过 DLNA 流式传输 FLAC？" closed="true" %}}
是的。Flacbox 针对 FLAC、ALAC 和 DSD 等高分辨率格式进行了优化。Evermusic 也支持 FLAC 播放以及 MP3 和其他标准格式。
{{% /details %}}

{{% details title="从 Kodi 流式传输后可以离线收听吗？" closed="true" %}}
可以。在任何播放列表上启用离线模式，应用将把所有曲目下载到您的设备上。
{{% /details %}}

{{% details title="使用 DLNA 需要高级订阅吗？" closed="true" %}}
免费版本支持最多 3 个云或网络连接。高级版取消此限制。
{{% /details %}}

{{% details title="我的 iPhone 需要与 Kodi 在同一个 Wi-Fi 网络上吗？" closed="true" %}}
是的。DLNA 流式传输通过您的本地网络工作。Kodi 服务器和 iOS 设备都必须连接到同一个 Wi-Fi 网络。
{{% /details %}}

{{% details title="我可以用 NAS 代替 Mac 或 PC 使用此设置吗？" closed="true" %}}
可以。许多 NAS 设备（Synology、QNAP 等）支持 Kodi 或有自己内置的 DLNA 服务器。Evermusic 和 Flacbox 可以连接到任何标准 DLNA/UPnP 服务器。
{{% /details %}}
