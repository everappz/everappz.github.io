---
title: "Evervideo 1.7:全新 Plex、Jellyfin、云端串流与播放手势"
date: 2026-05-18
description: "Evervideo 1.7 新增 10 项以上全新连接 — Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS — 以及全新的播放手势(双击快进/快退、长按 2 倍速),刷新的 Wi-Fi Drive 支持批量上传,并面向 iPhone、iPad 和 Mac 进行 Liquid Glass 界面更新。"
keywords: ["Evervideo 1.7", "Evervideo 更新", "HD 视频播放器 iPhone", "Plex 视频播放器 iOS", "Jellyfin iPhone 视频", "Emby 视频播放器 iOS", "Subsonic 视频 iOS", "Navidrome 视频 iOS", "Internxt 视频串流", "Proton Drive 视频播放器", "QNAP 视频播放器 iPhone", "Nextcloud 视频播放器 iOS", "Amazon S3 视频串流", "SFTP 视频播放器 iPhone", "FTP 视频播放器 iOS", "NFS 视频串流 iPhone", "从 NAS 串流视频 iPhone", "MKV 播放器 iPhone", "视频播放器手势 iOS", "双击快进视频", "Wi-Fi Drive 视频传输 iPhone", "Liquid Glass 设计", "云端视频播放器 iOS 2026", "从云端串流电影 iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "播放手势", "Liquid Glass", "新功能"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**简要:** [Evervideo 1.7](/products/evervideo) 是 iPhone、iPad 和 Mac 上 HD 视频播放器的一次重大更新。此版本新增了 10 项以上的云端、NAS 和媒体服务器连接 — **Internxt**、**Proton Drive**、**QNAP**、**Nextcloud**、**Amazon S3**,以及最受欢迎的媒体服务器 **Plex**、**Subsonic**、**Navidrome**、**Jellyfin** 和 **Emby**,还有三种网络协议:**FTP**、**SFTP** 和 **NFS**。全新的 **播放手势** 让你能双击向前或向后跳转、长按以 2 倍速播放,以及单击切换控制条 — 全部都在全屏模式下完成。Wi-Fi Drive 拥有焕然一新的界面、多选模式和更聪明的上传队列。整个应用都已为 Apple 全新的 **Liquid Glass** 设计进行了调整。

---

## 大家好!

Evervideo 的一项大型更新到了。这是我们发布过的最大版本之一:**10 项以上全新的云端、服务器和网络连接**,全新的 **播放手势** 让你在全屏中更快控制,焕然一新的 **Wi-Fi Drive**,以及面向 iPhone、iPad 和 Mac 调校过的 **Liquid Glass** 界面。

[在 App Store 下载 Evervideo 1.7](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) 或从现有版本进行更新。Mac 用户可在 [此处获取桌面版](https://apps.apple.com/app/evervideo/id6743504109)。

## 10 项以上全新的云端、NAS 和媒体服务器连接

Evervideo 1.7 扩展了你所谓「视频库」的概念。如果你的电影、剧集或录像保存在你信赖的云端、家中的 NAS 或自托管的媒体服务器上,Evervideo 现在可以直接从中串流 — 无需下载、无需转换、无需重新编码。

### 注重隐私的云端存储:Internxt 与 Proton Drive

如果你看重端到端加密和零知识存储,两个最受认可的隐私优先云端服务现在已被 Evervideo 原生支持:

- **Internxt** — 西班牙的开源、后量子加密、符合 GDPR 的云端服务。提供免费套餐。
- **Proton Drive** — 由 Proton Mail 与 Proton VPN 团队打造、总部位于瑞士的端到端加密存储。提供免费套餐,以及面向更大资料库的付费方案。

连接一次后,你的视频通过加密通道串流 — Evervideo 始终看不到你的明文数据,提供方的服务器也看不到。

### 自托管存储:QNAP、Nextcloud、Amazon S3

适合自行运维基础设施的用户:

- **QNAP** — 通过原生 API 连接 QNAP NAS 设备,通过本地 Wi-Fi 或远程访问进行快速可靠的视频播放。无需重新编码即可直接串流 4K MKV 文件。
- **Nextcloud** — 连接任意自托管或托管的 Nextcloud 实例。如果你已出于隐私考虑从 Google Drive 或 Dropbox 迁移过来,会非常合适。
- **Amazon S3** — 将 Evervideo 指向任意 S3 存储桶(或 Backblaze B2、Wasabi、MinIO、Cloudflare R2 等 S3 兼容存储)并直接串流你的合集。

### <a id="media-servers"></a>媒体服务器:Plex、Subsonic、Navidrome、Jellyfin、Emby

这是面向自托管视频爱好者的重磅消息。Evervideo 1.7 让你的 iPhone、iPad 或 Mac 成为最受欢迎的开源与 freemium 媒体服务器的一流客户端:

- **Plex** — Plex Media Server **免费** 下载和运行,可选 **Plex Pass** 订阅以获取移动同步、硬件转码和直播电视等功能。Evervideo 同时兼容免费版和 Plex Pass 库 — 串流你的全部电影和电视收藏。
- **Subsonic** — 最早的自托管流媒体服务器。官方 Subsonic 服务器 **收费**(30 天试用后每月 1 美元),Evervideo 也通过 Subsonic API 与兼容的视频服务器对话。
- **Navidrome** — 现代、轻量、**完全免费且开源** 的服务器。实现 Subsonic API。可在 Raspberry Pi、NAS 或任何 Linux 主机上运行。
- **Jellyfin** — **完全免费且开源** 的媒体服务器(Emby 的社区分支)。处理电影、电视、音乐、书籍和家庭视频。没有账户、没有遥测、没有订阅。是希望在没有商业附加条件下进行自托管串流的用户的首选。
- **Emby** — **freemium** 媒体服务器。核心服务器免费;**Emby Premiere** 是一次性或年度购买,可解锁移动应用、离线同步、Cinema Mode 等。Evervideo 同时连接免费版和 Premiere 库。

无论你运行的是哪种服务器,Evervideo 都会串流你的全部资料库 — 电影、剧集、家庭视频和内嵌字幕轨 — 同时支持视频均衡器、360° 支持、画中画、AirPlay 和 Chromecast。

### 全新网络协议:FTP、SFTP、NFS

对于使用自定义服务器、家庭实验室或没有精致移动应用的通用 NAS 的用户,Evervideo 1.7 新增了三种经典协议:

- **SFTP(SSH 文件传输协议)** — 这是 **从你自己的服务器进行安全远程视频串流** 的正确答案。SFTP 运行在 SSH 之上,因此整个传输(身份验证和视频数据)都被加密。如果你拥有 VPS、独立服务器或家中带 SSH 访问的 Linux 主机,可以把视频文件夹放上去,并通过公共互联网串流,而不会暴露其他任何东西。支持密码和密钥认证。
- **FTP** — 长期以来的文件传输标准。如果你的 **家用 NAS**(较老的 Synology、ASUS、D-Link、TerraMaster 或通用机型)暴露 FTP 但没有原生 API 集成,会很有用。最适合在本地网络中使用。
- **NFS(网络文件系统)** — Linux 和大多数 NAS 设备上事实标准的共享协议。NFS 共享在家庭实验室和小型企业网络中很常见;Evervideo 现可挂载并以低开销串流 4K 和 HD 视频。

> **提示:** SFTP 是适合通过开放互联网串流的协议。FTP 和 NFS 更适合本地网络使用 — 除非用 VPN 封装,否则不要将其暴露在公共互联网。

## 全新播放手势

在全屏中观看视频应当毫不费力。Evervideo 1.7 引入了一组简洁的点击手势,让你在不显示屏幕控制条的情况下控制播放 — 非常适合看电影、听讲座或任何你希望不被打扰的内容。

### 双击 — 向前或向后跳转

双击屏幕 **右侧** 可 **快进** 一个可配置的秒数。双击 **左侧** 可 **快退**。可在 **设置 → 播放 → 手势跳转间隔** 中修改时间(默认:10 秒) — 从 5 秒(用于精细定位)到 60 秒(用于跳过开场)。

这是 YouTube 和 Netflix 用户能立刻识别的手势,现在已原生集成在 Evervideo,适用于任何来源的任意视频。

### 长按 — 临时 2 倍速

按住屏幕任意位置即可 **临时将播放速度加快到 2 倍**。松开后恢复正常速度。非常适合:

- 在不切换永久速度的情况下跳过缓慢的场景。
- 快速扫过讲座、教程或播客以找到相关片段。
- 在投入观看完整版本之前先试听电影。

长按手势不会改变你保存的播放速度 — 一松开就回到原来的位置。

### 单击 — 显示 / 隐藏控制条

单击屏幕可以切换播放控制(播放、暂停、进度条、字幕、均衡器)。点一次显示,再点一次隐藏。结合双击和长按,你几乎可以整部电影都待在干净的全屏模式中,同时随时可以拖动、暂停和快速浏览。

## Wi-Fi Drive:全新 UI 和更快的上传

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) 是 Evervideo 内置的功能,用于 **将视频从电脑无线传输到 iPhone 或 iPad — 不需要 iTunes、不需要数据线、不需要云端账户**。两台设备需要在同一 Wi-Fi 网络中。你在 iOS 应用中启动服务器,然后:

- 在任意桌面浏览器(Safari、Chrome、Firefox、Edge)中打开 URL,将视频文件拖到页面上,即可直接上传到设备,或者
- 通过 **Mac Finder**(「连接服务器…」)或 **Windows File Explorer**(映射网络驱动器),使用 WebDAV 把设备挂载为网络共享。

这是把大量本地视频收藏移到手机或平板上的最快方式,无需任何第三方服务。请参阅 [此处的分步指南](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/)。

在 Evervideo 1.7 中,Wi-Fi Drive 获得:

- **重新设计的用户界面** — 更整洁、看一眼更易读,并为 Liquid Glass 进行了更新。
- **新的批量操作选择模式** — 选取多个文件或文件夹并进行批量操作(删除、移动、复制)。
- **改进的文件上传队列** — 更好的进度反馈,以及对网络波动的更强韧性,从此不稳定的 Wi-Fi 连接不再毁掉一次 30 GB 的传输。
- **整体传输性能更好** — 对大型资料库可见地更快上传,尤其是 4K MKV 文件和电影合集。

## 其他改进

### Liquid Glass 设计更新

Evervideo 1.7 的界面在整个应用中都为 Apple 全新的 **Liquid Glass** 材质进行了更新 — 半透明表面、更顺滑的动画,以及自然契合 iOS 26、iPadOS 26 和 macOS 26 的细致控件。Now Playing、文件浏览器以及设置界面都已重新调整,以匹配新的系统美学。

### 更新的连接库

我们刷新了 Evervideo 用于与 **WebDAV**、**SMB**、**DLNA**、**Dropbox**、**Google Drive**、**OneDrive**、**iCloud Drive**、**MEGA** 等服务对话的底层库。结果是:更少的边缘情况连接失败、对新版本服务器的更好支持,以及在较慢或地理位置较远的连接上串流视频时更高的可靠性。

### 播放 bug 修复

- 修复了部分自托管服务器上的播放问题,在大型 MKV 文件上拖动后串流会卡住。
- 在播放过程中网络短暂中断时有更好的恢复行为。
- 长篇内容上更平滑的字幕同步。

### 本地化修复

基于用户直接反馈在多种语言中进行了翻译修复。在较小的按钮和较长的欧洲语言(德语、荷兰语、法语)上文字适配更好。

### 受你反馈启发的更小优化

许多更小的改进基于 App Store 评价和发送到 support@everappz.com 的邮件。我们阅读每一条消息。

## 为什么这次更新很重要

Evervideo 1.7 围绕三个理念构建:

1. **你的视频,在你保存它的任何地方。** 无论你的资料库在 iCloud Drive、Proton Drive 或 Internxt 这样的隐私优先云端、Plex 或 Jellyfin 这样的媒体服务器、家中的 NAS,还是运行 Navidrome 的 Raspberry Pi — Evervideo 现在都能原生连接,并在所有位置提供一致的播放体验。
2. **毫不费力的全屏视频。** 全新点击手势(双击、长按、单击)带来 YouTube 和 Netflix 等流媒体应用让用户习以为常的流畅控制,应用到 *你自己* 的视频合集上。
3. **从电脑更快传输。** 焕然一新的 Wi-Fi Drive 配合批量选择和更聪明的上传队列,让把大型 4K 电影合集移到 iPhone 或 iPad 上真正变快 — 无线、无 iTunes、无压缩。

## 获取 Evervideo 1.7

[**在 App Store 下载 Evervideo**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) 或在 App Store 内进行更新。[Mac 版](https://apps.apple.com/app/evervideo/id6743504109) 单独作为通用 Mac 应用提供。Evervideo 免费下载,可选择购买应用内升级以获得高级功能。新的云端连接、媒体服务器支持、播放手势、Wi-Fi Drive 改进和 Liquid Glass UI 都包含在基础更新中。

如果你喜欢这款应用,请在 App Store 留下评分 — 这真的对我们很有帮助。有反馈或遇到问题?请发送邮件至 **support@everappz.com**。我们阅读每一条消息。

## 常见问题

{{% details title="Evervideo 1.7 有什么新功能?" closed="true" %}}
Evervideo 1.7 引入对 10 项以上新连接的支持(Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS)、新的播放手势(双击快进/快退、长按 2 倍速、单击切换控制条)、重新设计的 Wi-Fi Drive(带选择模式和更聪明的上传队列)、Liquid Glass 设计更新、连接库更新,以及大量 bug 修复。
{{% /details %}}

{{% details title="Evervideo 能搭配 Plex 使用吗?" closed="true" %}}
可以。从 Evervideo 1.7 开始,你可以连接到 Plex Media Server 并串流完整的视频库 — 电影、电视剧和家庭视频。Plex Media Server 免费运行;Plex Pass 为可选项。Evervideo 同时支持免费和 Plex Pass 设置,包括直接播放 MKV、MP4、AVI、MOV 等格式而无需重新编码。
{{% /details %}}

{{% details title="Evervideo 支持 Jellyfin 或 Navidrome 吗?" closed="true" %}}
是的。Jellyfin 和 Navidrome 都在 Evervideo 1.7 中获得完整支持。Jellyfin 是处理视频和音频的免费开源媒体服务器。Navidrome 是实现 Subsonic API 的免费开源服务器。Evervideo 原生连接到两者。
{{% /details %}}

{{% details title="Plex、Jellyfin、Emby、Navidrome 和 Subsonic 都是免费的吗?" closed="true" %}}
- **Plex** — 服务器免费;Plex Pass 是可选的付费升级。
- **Jellyfin** — 完全免费且开源。
- **Emby** — 服务器免费;Emby Premiere 付费,可解锁移动同步和离线功能。
- **Navidrome** — 完全免费且开源。
- **Subsonic** — 官方服务器在 30 天试用后每月 1 美元,但其 API 开放,许多免费服务器(包括 Navidrome)都已实现。
{{% /details %}}

{{% details title="我可以通过 SFTP、FTP 或 NFS 从家中的 NAS 串流吗?" closed="true" %}}
可以。Evervideo 1.7 新增 SFTP、FTP 和 NFS 作为原生连接类型。SFTP 是通过公共互联网从你自己的服务器进行串流的推荐选择,因为所有流量都通过 SSH 加密。FTP 和 NFS 最好在本地网络内使用或在 VPN 后使用。
{{% /details %}}

{{% details title="如何使用 SFTP 把 Evervideo 连接到自定义服务器?" closed="true" %}}
打开 Evervideo,前往「连接」标签,选择 SFTP,然后输入服务器的主机名或 IP、端口(通常是 22)、用户名,以及密码或 SSH 私钥。Evervideo 将浏览你的远程文件夹,并以端到端加密直接串流视频文件。
{{% /details %}}

{{% details title="Evervideo 支持 Internxt 和 Proton Drive 吗?" closed="true" %}}
支持。两个注重隐私的云端服务从 Evervideo 1.7 起得到支持。它们加入 MEGA 和应用中已有的其他注重隐私的服务。
{{% /details %}}

{{% details title="新的播放手势如何使用?" closed="true" %}}
在全屏视频播放中,**双击右侧** 可快进,**双击左侧** 可快退一个可配置的间隔(默认 10 秒 — 可在「设置」中修改)。**长按** 屏幕任意位置可临时加速到 2 倍;松开后恢复正常。**单击** 屏幕任意位置可切换播放控制(显示或隐藏)。
{{% /details %}}

{{% details title="我可以更改双击的跳转间隔吗?" closed="true" %}}
可以。前往 **设置 → 播放 → 手势跳转间隔**,选择 5 到 60 秒之间的值。大多数用户保持 10 或 15 秒。
{{% /details %}}

{{% details title="Evervideo 中的 Wi-Fi Drive 是什么?" closed="true" %}}
Wi-Fi Drive 是 Evervideo 内置的无线文件传输功能。它允许你通过本地 Wi-Fi 网络从电脑上传视频到 iPhone 或 iPad — 无需 iTunes、无需数据线、无需云端账户。你可以使用任意桌面浏览器或 WebDAV 客户端(如 Mac Finder 或 Windows File Explorer)。查看 [完整的 Wi-Fi Drive 指南](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/)。
{{% /details %}}

{{% details title="Evervideo 能从 Plex 或 Jellyfin 播放 MKV、AVI 等格式吗?" closed="true" %}}
可以。Evervideo 播放几乎所有视频格式 — MKV、AVI、MP4、MOV、FLV、WMV、WEBM、M4V、TS、3GP — 并直接从 Plex、Jellyfin、Emby 及其他媒体服务器串流它们,大多数编解码器无需转码。这意味着你的服务器 CPU 负载更低、启动时间更快。
{{% /details %}}

{{% details title="升级到 Evervideo 1.7 免费吗?" closed="true" %}}
是的。Evervideo 是 App Store 中的免费下载,1.7 是所有现有用户的免费更新。全新的云端集成、媒体服务器支持、播放手势、Wi-Fi Drive 改进和 Liquid Glass UI 都是基础更新的一部分。
{{% /details %}}

{{% details title="Evervideo 1.7 支持哪些设备?" closed="true" %}}
Evervideo 1.7 运行于 iPhone、iPad 和 Mac 上。AirPlay 和 Chromecast 让你能把播放投到更大的屏幕。iCloud Drive 同步保持你的资料库和设置在各设备间一致。
{{% /details %}}
