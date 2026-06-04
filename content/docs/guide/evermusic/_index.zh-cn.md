---
title: "Evermusic"
date: 2020-01-01
description: "Evermusic — 适用于 iPhone、iPad 和 Mac 的强大云端音乐播放器和音乐库管理器。从 Google Drive、Dropbox、iCloud、OneDrive、MEGA、Synology、pCloud、Plex、Jellyfin、Subsonic、Navidrome 或任何通过 SMB / WebDAV / FTP / SFTP 连接的 NAS 进行流媒体播放。编辑 ID3 和 FLAC 标签，按艺术家 / 专辑 / 流派整理，离线播放，使用 10 段均衡器、crossfade、gapless、空间音频、睡眠计时器、CarPlay、AirPlay 2、Google Cast、音频书签、Last.fm 音乐记录和锁屏小组件。"
keywords: [
  "Evermusic", "Evermusic Pro", "Evermusic iPhone", "Evermusic iPad", "Evermusic Mac",
  "云端音乐播放器", "iOS FLAC播放器", "DSD播放器", "iPhone高分辨率音频",
  "Google Drive播放音乐", "Dropbox播放音乐", "iCloud Drive播放音乐",
  "OneDrive播放音乐", "MEGA播放音乐", "Synology音乐播放器", "pCloud音乐播放器",
  "Plex音乐客户端", "Jellyfin音乐播放器", "Emby音乐客户端",
  "iPhone Subsonic客户端", "iPhone Navidrome客户端", "Nextcloud音乐播放器",
  "NAS音乐流媒体", "iPhone SMB音乐播放器", "WebDAV音频播放器",
  "iPhone FTP音乐播放器", "SFTP音乐播放器", "S3音乐播放器",
  "10段均衡器", "crossfade播放", "gapless播放", "空间音频",
  "有声书书签", "离线音乐应用", "iPhone音乐库", "ID3标签编辑器",
  "M3U播放列表导入", "CSV TXT播放列表导出", "Apple CarPlay音乐播放器",
  "AirPlay 2", "Google Cast Chromecast音乐", "Last.fm音乐记录", "锁屏小组件"
]
tags: ["evermusic", "指南"]
readingTime: 4
---


Evermusic 是一款强大的云端音乐播放器和音乐库管理器，可将您的 iPhone、iPad 或 Mac 变成功能完备的流媒体和离线音乐系统。它与您已有的云账户和 NAS 兼容，几乎可播放设备支持的所有音频格式，并在此基础上提供深度音频引擎（10 段均衡器、crossfade、gapless、空间音频、音调校正）。

提供两个版本：Evermusic（免费，含广告）和 Evermusic Pro（付费，无广告，完整功能集）。免费版中的终身、月度和年度 Premium 计划可解锁相同的功能集；两个版本通过 iCloud 和 Family Sharing 在 iOS 和 Mac 之间共享购买。

### 随时随地享受音乐

Evermusic 让您构建自己的云端音乐流媒体系统——就像 Spotify，但没有任何限制。连接任意来源组合，按需流媒体或下载曲目：

- **个人云账户：** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **自建服务器和媒体库：** Plex · Jellyfin · Emby · Subsonic（以及所有 Subsonic 兼容服务器——Airsonic、Funkwhale、Gonic、Logitech Media Server、Ampache）· Navidrome · Nextcloud（以及通过共享 API 的 Owncloud）· Synology Drive · QNAP.
- **NAS 和文件共享协议：** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP（SSH 文件传输协议，密码或公钥认证）· NFS · DLNA / UPnP（播放和下载）。支持 Apple Time Capsule、Synology、QNAP、WD My Cloud Home、Buffalo、任何 Linux Samba / NFS / SSH 主机，或 Mac 或 Windows PC 上的共享文件夹。
- **S3 兼容对象存储：** AWS S3 · Backblaze B2 · Wasabi · Cloudflare R2 · MinIO · DigitalOcean Spaces · Linode Object Storage · IBM Cloud Object Storage · 任何 S3-API 端点。
- **本地网络发现：**「可用设备」部分自动列出您 Wi-Fi 上通过 Bonjour / mDNS 广播的所有设备——Plex、Jellyfin、Emby 服务器、Synology、QNAP、带附加硬盘的 AirPort 路由器、Time Capsule——点击即可连接，无需输入 IP。
- **设备和外部来源：** iPod / Apple Music 媒体库（无 DRM 曲目）、系统 Files 应用中的文件（其他应用、外部 SSD、挂载的文件夹）、通过 Apple 认证读卡器和 iXpand Flash Drives 连接的 USB 闪存盘、Wi-Fi Drive（在桌面浏览器中拖放）、iTunes / Finder 文件共享（USB 数据线）。

一个应用支持 30 多种来源。音乐在云端后，您可以随时随地播放，每台设备上的媒体库相同。备份与恢复功能可将整个媒体库快照为单个文件，并在数秒内导入到另一台 iPhone、iPad 或 Mac 上。

### 流畅播放

Evermusic 使用智能预加载和可配置的播放缓存，即使在连接缓慢的情况下也能流畅播放歌曲。智能流媒体使用 AVAssetResourceLoader，播放立即开始，同时后台下载文件的其余部分。您也可以下载专辑、艺术家、播放列表或单首歌曲供离线收听——如果存储空间不足，只需删除缓存文件并继续从云端流媒体。

### 轻松整理音乐

将歌曲添加到 Evermusic 时，后台元数据读取器会解析每个文件并构建按歌曲、未播放歌曲、专辑、专辑艺术家、艺术家、流派和作曲家排序的干净音乐库。专辑有三个子视图：所有专辑、独家专辑和独唱专辑，避免合辑和不同艺术家同名专辑之间的混淆。

### 轻松修正歌曲信息

如果歌曲标题或专辑信息有误或缺失，不用担心。Evermusic 包含内置标签编辑器，让您在几秒内修复元数据。您可以更新标题、艺术家、专辑、专辑艺术家、年份、流派和专辑封面，还可以一键规范化损坏的编码（乱码显示的西里尔文或亚洲文字）。编辑器使用 MusicBrainz 自动查找缺失的标签和专辑封面。

### 简单文件传输

从计算机向 iPhone 或 iPad 发送音乐非常简单。Evermusic 支持 SMB、WebDAV、FTP / FTPS、SFTP、NFS、DLNA、Wi-Fi Drive（在浏览器中拖放）、iTunes / Finder 文件共享（USB 数据线）以及从任何已连接云账户直接下载。您还可以连接 Apple Time Capsule、WD My Cloud Home、Synology、QNAP、Buffalo 或任何其他公开上述标准协议的 NAS，而不占用设备存储空间。

### 强大的音效控制

Evermusic 包含完整的 10 段音频均衡器，带有 iPod 风格的预设（Acoustic、Bass Booster、Classical、Dance、Electronic、Flat、Hip-Hop、Jazz、Latin、Loudness、Lounge、Piano、Pop、R&B、Rock、Small Speakers、Spoken Word、Treble Booster、Vocal Booster）、用于安静曲目的前置放大器、可导出和导入的自定义预设，以及基于 RMS 的响度计算。添加 crossfade 播放（1–15 秒）、gapless 播放、空间音频、音调校正和 CoreAudio 输出高达 384 kHz 单声道或立体声，可以完全按照自己的喜好调整音效。

### 非常适合有声书

如果您收听有声书、播客或录制的讲座，Evermusic 是完美之选。您可以为每首曲目添加多个书签、自动从上次位置恢复、将播放速度从 0.02× 更改为 3×（带有精确滑块模式）、设置带有自定义间隔的睡眠计时器，并在同一屏幕上查看评论、嵌入式歌词和 LRC 文件。

### 随处可用

您不仅限于手机或平板电脑。Evermusic 还支持 Apple CarPlay（仅限 iOS，针对车载界面优化）、AirPlay 2（同时向多个扬声器流媒体）、Google Cast / Chromecast、锁屏小组件、正在播放控件、Last.fm 音乐记录（自动将播放数据发送到您的 Last.fm 账户以获取统计数据和推荐）和 Mac 键盘快捷键。无论您在家、在车里还是旅途中，音乐始终伴随您。

### Evermusic 入门

本指南将帮助您在 iPhone、iPad 或 Mac 上充分利用 Evermusic。了解如何从云端流媒体音乐、整理存储在自己存储上的媒体库、管理播放列表和离线文件夹、微调音频引擎以及收听有声书。Evermusic 让您在一个简单的应用中完全控制您的音乐收藏。<br><br>


{{< cards >}}
  {{< card icon="location-marker" title="导航" subtitle="了解如何在 iPhone 上使用标签栏或在 iPad 和 Mac 上使用左侧菜单导航 Evermusic。" link="/docs/guide/evermusic/evermusic-guide-navigation" >}}

  {{< card icon="cloud" title="连接" subtitle="连接您的云账户并使用内置文件管理器管理在线文件。" link="/docs/guide/evermusic/evermusic-guide-connections" >}}

  {{< card icon="collection" title="音乐库" subtitle="在音乐库中整理和浏览您的曲目、专辑和艺术家。" link="/docs/guide/evermusic/evermusic-guide-music-library" >}}

  {{< card icon="music-note" title="播放列表" subtitle="创建和整理播放列表以匹配您的心情或场合。" link="/docs/guide/evermusic/evermusic-guide-playlists" >}}

  {{< card icon="folder" title="本地文件" subtitle="通过本地文件部分访问和管理离线音乐。" link="/docs/guide/evermusic/evermusic-guide-local-files" >}}

  {{< card icon="play" title="音频播放器" subtitle="控制播放、队列和音频设置，如均衡器和睡眠计时器。" link="/docs/guide/evermusic/evermusic-guide-player" >}}

  {{< card icon="adjustments" title="设置" subtitle="自定义 Evermusic 的外观、功能和性能设置。" link="/docs/guide/evermusic/evermusic-guide-settings" >}}

  {{< card icon="question-mark-circle" title="FAQ" subtitle="在我们的 FAQ 部分找到常见问题的快速解答。" link="/docs/faq/evermusic" >}}
{{< /cards >}}
