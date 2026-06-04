---
date: 2020-01-01
lastmod: 2026-06-01
title: "Evervideo"
description: "了解如何使用 Evervideo——适用于 iPhone、iPad 和 Mac 的全能云视频播放器。从 iCloud Drive、Google Drive、Dropbox、OneDrive、MEGA、Box、pCloud、Synology、QNAP、NAS、WebDAV、SMB、NFS、FTP / SFTP、DLNA 和 S3，以及 Plex、Jellyfin、Emby、Subsonic 和 Navidrome 播放和下载视频。支持画中画、主副字幕、音频和视频均衡器、RTSP IP 摄像头流、Chromecast、AirPlay 2、硬件 H.264 / HEVC 解码、Photos 与 Apple Music 资料库集成，以及常驻迷你播放器。"
keywords: [
  "Evervideo 使用指南", "Evervideo 怎么用", "云视频播放器 iPhone", "视频播放器 Mac",
  "MKV 播放器 iOS", "FFmpeg 视频播放器", "HEVC 视频播放器 iPhone",
  "iPhone 画中画视频", "iPad PiP 视频播放器",
  "RTSP 播放器 iPhone", "IP 摄像头查看器", "DLNA 视频播放器",
  "Plex 客户端 iPhone", "Jellyfin 客户端 iOS", "Emby 客户端 iPad",
  "iOS 字幕播放器", "SRT VTT ASS 字幕", "iPhone 辅助字幕",
  "iOS 视频均衡器", "视频播放器音频均衡器", "外置 DAC 视频",
  "从 Google Drive 播放视频", "从 Dropbox 播放视频",
  "从 OneDrive 播放视频", "从 iCloud Drive 播放视频",
  "从 MEGA 播放视频", "从 NAS 播放视频",
  "iPhone Chromecast 视频", "AirPlay 2 视频", "iCloud 视频播放器",
  "Photos 资料库视频播放器", "Apple Music 视频播放器",
  "Wi-Fi Drive 视频传输", "M3U 视频播放列表",
  "Evervideo Premium", "家庭共享视频应用"
]
tags: ["evervideo", "使用指南", "视频播放器", "PiP", "字幕", "RTSP", "云", "FFmpeg"]
---


### 欢迎使用 Evervideo 指南

Evervideo 是适用于 iPhone、iPad 和 Mac 的全功能云媒体播放器，可将任何云存储账户、NAS 或媒体服务器变成您的个人媒体库，无需重新上传任何内容，同时完全掌控您的文件。

基于定制 FFmpeg 播放引擎，配备硬件加速 H.264 和 HEVC 解码，Evervideo 几乎可以播放所有现代容器和编解码器——MP4、MKV、AVI、MOV、FLV、WMV、WebM、TS、M2TS 以及众多 FFmpeg 格式——以完整质量播放，并通过智能缓冲在 Wi-Fi 或蜂窝网络上实现流畅串流。画中画功能让视频始终显示在所有其他应用之上，常驻迷你播放器让您在浏览资料库时持续观看，而 Chromecast 和 AirPlay 2 只需一触即可将播放投射到电视、HomePod 或音响系统。

Evervideo 可连接到丰富的来源，全部来自一个应用：

- **个人云存储：** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **自托管媒体服务器：** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud（及通过共享 API 的 ownCloud）· Synology Drive · QNAP.
- **NAS 和文件共享协议：** SMB（SMB1、SMB2、自动）· WebDAV（HTTP / HTTPS）· FTP · FTPS · SFTP（密码或公钥认证）· NFS · DLNA · UPnP.
- **直播和 IP 摄像头流：** RTSP——将 Evervideo 指向任意 RTSP URL（`rtsp://camera-ip/stream`）即可直接播放。
- **S3 兼容对象存储：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 以及任何其他 S3 API 端点。
- **设备本地来源：** Photos 资料库（所有视频、短/中/长视频、屏幕录制及相册）、Music 应用资料库（专辑、流派、播放列表）、USB / SD 驱动器和本地文件。

### 一个播放器，支持所有格式和编解码器

大多数 iOS 应用止步于 MP4 / MOV 中的 H.264 / H.265，而 Evervideo 将 FFmpeg 与 Apple 系统编解码器捆绑在一起，让您可以播放系统无法识别的格式——MKV 容器、VP9、AV1、MPEG-2、OGG、Vorbis 等——并根据文件和设备自动在硬件 H.264 / HEVC 解码和软件解码之间切换。

您可以选择视频轨道（多流蓝光翻录）、音频轨道（评论轨道、备用配音）和字幕轨道。外部 SRT、VTT 和 ASS / SSA 字幕文件一键加载；得益于内置 libass，高级 ASS / SSA 样式可正确渲染。

### 智能字幕

- **字幕轨道选择**——非常适合语言学习。
- **外部字幕文件**（`.srt`、`.vtt`、`.ass`、`.ssa`）可从设备任意位置或云端加载。
- **libass** 提供完整风格化的 ASS / SSA 渲染。
- **每轨道和全局字体选择**，用于字幕。
- **音频轨道选择**——选择配音、评论或导演剪辑轨道。
- **视频轨道选择**，适用于多角度或多版本文件。

### 精调画面和声音

两个并排均衡器：音频均衡器用于调节低音和高音（支持自定义预设的导入/导出），视频均衡器用于调节亮度、对比度、饱和度和色调（同样支持导入/导出）。两个引擎还提供发烧友级别的控制：音频输出采样率、声道数量、IO 缓冲时长和混合模式——适合使用外置 DAC 和家庭影院接收器的用户。

### 投射、AirPlay 和画中画

- **画中画（PiP）：** 在使用其他应用时继续观看。
- **AirPlay 2：** 将视频投射到 Apple TV、HomePod 或任何支持 AirPlay 2 的音箱/电视。
- **Google Chromecast：** 直接投射到 Chromecast 或支持 Cast 的电视。
- **迷你播放器：** 常驻于每个屏幕顶部，让您在浏览资料库时不会丢失视频。

### 隐私与安全

Evervideo 使用每个云服务商的官方 SDK 和基于 OAuth 的登录，因此您的密码永远不会传到应用。访问令牌以加密形式存储在 iOS/macOS Keychain 中，每次传输均受 TLS 保护，从云账户撤销访问（或从设备删除 Evervideo）会立即删除所有内容。通过可选的 4 位数字密码保护您的资料库，增加额外的隐私层。

### Evervideo 入门

本指南将带您了解 Evervideo 在 iPhone、iPad 和 Mac 上的每个部分——从连接云服务、浏览资料库、下载和传输文件、管理播放列表，到精细调整媒体播放器、均衡器、字幕和画中画。使用下方卡片直接跳转到您需要的部分。<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="导航" subtitle="iPhone 上的标签栏，iPad 和 Mac 上的左侧菜单，常驻迷你媒体播放器。" >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="文件" subtitle="云、NAS、RTSP 流、本地文件、USB 驱动器和传输队列的统一标签页。" >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="媒体资料库" subtitle="按专辑、流派、最近使用、收藏夹浏览——以及 iOS Photos 资料库和 Apple Music 资料库。" >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="播放列表" subtitle="从云、本地、Photos 或 Music 资料库创建播放列表，导入 M3U / M3U8 / CUE。" >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="媒体播放器" subtitle="画中画、音频和视频轨道、字幕、音频和视频均衡器、AirPlay、Chromecast。" >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="设置" subtitle="音频引擎、视频解码器、字幕、资料库、文件管理器、小组件、个性化、语言、备份。" >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="常见问题" subtitle="查找有关 Evervideo 最常见问题的解答。" >}}

{{< /cards >}}
