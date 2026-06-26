---
title: "Evertag 4.2:新增云连接,标签编辑器设置详解"
date: 2026-05-09
description: "Evertag 4.2 新增对 Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP 和 NFS 的连接,刷新 Wi-Fi Drive 并将界面适配 Liquid Glass。本文还逐项讲解标签编辑器的所有设置 — 包括 ID3v2.4 与 ID3v2.3、专辑封面缩放、标签复制、云端上传模式,以及为 Spotify 等流媒体服务准备文件时应选择的正确选项。"
keywords: ["Evertag 4.2", "Evertag 更新", "ID3 标签编辑器 iPhone", "ID3v2.4 vs ID3v2.3", "FLAC 标签编辑 iOS", "MP3 标签编辑 iPhone", "专辑封面编辑 iOS", "Spotify 标签编辑器", "Plex 标签编辑器", "Apple Music 标签编辑器", "Evertag 云端标签编辑器", "Internxt 标签编辑器", "Proton Drive 标签编辑器", "QNAP 标签编辑器", "Nextcloud 标签编辑器", "Amazon S3 标签编辑器", "SFTP 标签编辑器 iPhone", "FTP 音频标签编辑器", "NFS 标签编辑器 iPhone", "Wi-Fi Drive 标签编辑器", "ID3 标签复制", "专辑封面缩放", "Liquid Glass 设计", "音频元数据编辑器 iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "标签编辑器", "ID3", "ID3v2.4", "ID3v2.3", "FLAC 标签", "MP3 标签", "专辑封面", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "新功能"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**简要:** [Evertag 4.2](/products/evertag) 是 iPhone、iPad 和 Mac 上音频标签编辑器的一次重大更新。我们解决了关键的标签编辑 bug,并新增 6 项以上的云端和服务器连接 — **Internxt**、**Proton Drive**、**QNAP**、**Nextcloud**、**Amazon S3**,以及 **FTP**、**SFTP** 和 **NFS** 协议。Wi-Fi Drive 拥有焕然一新的界面、多选模式、更聪明的上传队列和更快的传输速度。整个应用都已按 **Liquid Glass** 设计调校。本文还深入解读 Evertag 的标签编辑器设置 — 讲清 **ID3v2.4 与 ID3v2.3**、**专辑封面缩放**、**标签复制**、**云端上传模式**、**已下载文件删除**,以及在为 **Spotify**、**Apple Music**、**Plex**、**Jellyfin** 或其他流媒体服务准备音频时,究竟该选哪个选项。

---

## 大家好!

Evertag 的一项大型更新到了。我们解决了关键的标签编辑 bug,并新增 **6 项以上的云端和服务器连接**,让管理音频元数据比以往更轻松 — 无论你的曲库放在以隐私为先的云端、自托管的 NAS,还是通用的 FTP/SFTP/NFS 服务器上。

[在 App Store 下载 Evertag 4.2](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) 或从现有版本进行更新。

## 扩展的云与服务器支持

Evertag 现在原生连接更多云端和自托管存储选项。无论文件放在哪里,你都可以编辑 ID3、MP4、FLAC、OGG 和 APE 标签。

### 注重隐私的云端:Internxt 与 Proton Drive

如果你看重端到端加密和零知识存储,两个最受认可的隐私优先云端服务现在已被原生集成到 Evertag:

- **Internxt** — 西班牙的开源、后量子加密、符合 GDPR 的云端服务。提供免费套餐。
- **Proton Drive** — 由 Proton Mail 与 Proton VPN 团队打造、总部位于瑞士的端到端加密存储。提供免费套餐,以及面向更大音乐库的付费方案。

你现在可以直接在两个服务上保存的音频文件上编辑元数据 — 文件在传输中保持加密,只有新的标签会被写回。

### 自托管解决方案:QNAP、Nextcloud、Amazon S3

适合自行运维基础设施的用户:

- **QNAP** — 通过原生 API 连接 QNAP NAS 设备。可通过本地 Wi-Fi 或远程访问编辑 QNAP 上的文件标签。
- **Nextcloud** — 连接任意自托管或托管的 Nextcloud 实例。
- **Amazon S3** — 将 Evertag 指向任意 S3 桶(或 Backblaze B2、Wasabi、MinIO、Cloudflare R2 等 S3 兼容存储)并就地编辑元数据。

### 全新的网络协议:FTP、SFTP、NFS

对于使用自定义服务器、家庭实验室或没有精致移动应用的通用 NAS 的用户,Evertag 4.2 新增了三种经典协议:

- **SFTP(SSH 文件传输协议)** — 这是 **从你自己的服务器进行安全远程标签编辑** 的正确选择。SFTP 基于 SSH 运行,因此整个传输(身份验证和音频数据)都被加密。如果你拥有 VPS、独立服务器或家中带有 SSH 访问权限的 Linux 机器,可以编辑远程文件的标签,而不会暴露其他任何东西。支持密码和密钥认证。
- **FTP** — 长期以来确立的文件传输标准。对于暴露 FTP 但没有原生 API 集成的较老家用 NAS 很有用。
- **NFS(网络文件系统)** — Linux 和大多数 NAS 设备上的事实标准共享协议。在相同硬件上,NFS 的开销比 SMB 更小。

> **提示:** SFTP 是适合通过开放互联网进行远程编辑的协议。FTP 和 NFS 更适合本地网络使用 — 除非你将其封装在 VPN 中,否则不要将其暴露在公共互联网。

## Wi-Fi Drive 升级

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) 是 Evertag 内置的功能,用于在电脑与 iPhone 或 iPad 之间无线传输音频文件 — 无需 iTunes、无需数据线、无需云端账户。两台设备需要在同一个 Wi-Fi 网络中。

在 Evertag 4.2 中,Wi-Fi Drive 获得:

- **焕然一新的现代界面** — 更整洁、更易于一眼看清,并已适配 Liquid Glass。
- **多选模式** — 选择多个文件或文件夹并批量进行操作。
- **更聪明的上传队列** — 进度反馈更清晰,对网络波动的容忍度更高。
- **整体速度与可靠性提升** — 大型库的传输速度更快。

这是在不依赖第三方服务的前提下,将一批音频文件从电脑搬到手机、编辑标签后再发回的最快方式。

## 标签编辑器设置:深入解读

这是大多数用户从不阅读的部分 — 而它决定了你的标签是在所有应用中生效,还是只在部分应用中。打开 Evertag,然后进入 **音频标签编辑器设置** 部分。下面解释每个选项的实际作用,以及根据目标应该选哪一项。

### 专辑封面缩放

将专辑封面保存到音频文件时,Evertag 可以在嵌入前对图像进行缩放。可用选项:

- **小** — 对文件大小影响最小,图像质量较低。
- **中** — 对大多数用户而言均衡的选择。
- **大** — 高质量,适合大屏播放器和 CarPlay。
- **特大** — 非常高的质量,文件大小显著增加。
- **原始(已停用)** — 以原始分辨率嵌入封面。**完全不缩放。**

**为什么这很重要:**

- **质量越高 = 文件越大。** 一张 3,000 × 3,000 像素的封面可能为每首歌增加数 MB。乘上整张专辑,磁盘占用累积得很快。
- **某些播放器对超大嵌入图像处理不佳。** 老旧设备、某些车机、以及一些遗留的桌面播放器可能在 ~1,500 px 以上的封面卡住或拒绝显示。
- **对大多数云端和流媒体工作流**,**中** 或 **大** 是最佳点。仅在确实需要存档质量,或为信任能正确处理的播放器准备文件时才使用 **原始**。

> **原始** 尺寸选项属于 Evertag 高级个性化升级。标准尺寸(小/中/大/特大)免费。

### 标签保存选项:ID3v2.4 与 ID3v2.3

这是兼容性最重要的单一设置。ID3v2 是 MP3 文件中使用的元数据格式。两个广泛使用的版本之间存在细微但重要的差异。

#### ID3v2.4

- 更新,支持 **UTF-8 文本编码** — 可正确处理非拉丁文字(中文、俄文、日文、阿拉伯文、希伯来文等)。
- 更多的帧类型(相对音量、均衡器预设等)。
- **建议在支持它的现代播放器** 中使用。

#### ID3v2.3

- 更老,但 **得到普遍支持** 的 ID3 版本。
- 不直接支持 UTF-8(对 Unicode 文本使用 UTF-16)。
- **当你需要与较老的播放器、车载主机和某些桌面应用获得最大兼容性时建议使用**。

#### 何时在 Evertag 中开启 ID3v2.4

- 你使用 Evermusic、Plex、Jellyfin、Navidrome、foobar2000、VLC、Apple Music(当前版本)或现代 Android 播放器等 **现代音频播放器**。 ✅ **打开 ID3v2.4。**
- 你的库包含 **非拉丁字符**(中文、韩文、日文、俄文、阿拉伯文、希腊文、希伯来文)。 ✅ **打开 ID3v2.4** — UTF-8 处理这些字符更干净。

#### 何时在 Evertag 中关闭 ID3v2.4(改用 ID3v2.3)

- 你正为不读取 v2.4 标签的 **较旧车载音响或仪表盘单元** 准备文件。
- 编辑后某些应用中出现 **乱码或缺失的标签** — 这强烈说明那里不支持 v2.4。改回 v2.3。
- 你瞄准 **遗留的桌面播放器** 或更老的便携播放器(早期 iPod、2000 至 2010 年代的某些 MP3 播放器)。

> **经验法则:** 如果你的标签在所有地方都用 v2.4 显示正确,就保持开启。如果即使一个重要播放器显示错误字符、空白或读取失败,关闭 v2.4 并重新保存。

#### 标签复制

启用 **标签复制** 后,Evertag 会把通用元数据字段(标题、艺术家、专辑等)同时写入文件的 **ID3v1 和 ID3v2 两个区段**。这能改善与只读取 ID3v1(文件末尾原始的 128 字节标签)的非常老旧播放器之间的兼容性。

- **大多数用户不需要此项。** 现代播放器优先读取 ID3v2。
- **仅在** 你处理的是古董硬件或忽略 ID3v2 的特定软件时才启用。

### 更新在线文件:Evertag 如何处理云端编辑

当你编辑保存在已连接云端(Google Drive、Dropbox、OneDrive、iCloud、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、SFTP 等)上的文件标签时,Evertag 必须把修改后的文件上传回去。你来掌控如何处理:

- **显示确认消息** *(默认,推荐)* — Evertag 会在上传前询问。最适合谨慎的用户和共享库。
- **自动更新文件元数据** — 每次编辑后静默上传。最适合连接稳定快速、且经常编辑的单人用户。
- **不更新文件元数据** — Evertag 仅编辑本地副本。适合在不向云端提交的情况下预览标签变更。

### 编辑在线文件:本地文件清理

要编辑远程文件,Evertag 先把它下载到设备。编辑后,你选择本地副本如何处理:

- **始终删除已下载文件** — Evertag 在编辑后移除临时文件。如果你存储紧张或在处理别人的文件,**推荐**。
- **不删除已下载文件** — 在设备上保留已编辑文件。当你既想要离线副本,又想要更新过的云端副本时很有用。

### 主屏幕的按钮

Evertag 的标签编辑器主屏幕可以显示或隐藏单项操作的按钮。仅启用你真的会使用的按钮,以保持界面聚焦:

- **自动搜索音频标签** — 基于文件的音频指纹在线查找缺失的元数据。
- **手动搜索音频标签** — 当自动搜索失误时,按标题/艺术家进行搜索。
- **搜索专辑封面** — 查找并嵌入高质量封面。
- **保存专辑封面** — 将嵌入的封面导出到照片库或文件中。
- **规范化编码** — 修复由旧编码导致的乱码非拉丁文本(对用遗留软件抓轨的西里尔、中文、日文曲目特别有用)。
- **删除音频标签** — 从文件中清除所有标签。在重新打标签之前很有用。

### 显示扩展标签

启用此项可显示超出基本 标题/艺术家/专辑/年份 的全部元数据字段 — 包括 BPM、指挥、原唱、情绪、版权、编码器、注释、歌词等。高级用户功能;大多数普通用户不需要。

### 同时编辑文件

启用后,Evertag 让你 **跨多个所选文件同时** 编辑元数据 — 一次操作即可为整张专辑设置相同的 album artist、年份或类型。整理大型杂乱库的最快方式。

## 为 Spotify、Apple Music 和流媒体平台编辑标签

我们常被问:「我在 Evertag 里编辑了标签,把文件上传后,流媒体服务显示的元数据却是错的。怎么回事?」

简短答案:**流媒体服务并不总是采用你的本地标签。** Apple Music 和 Spotify 都有自己的内部数据库 — 当它们识别出一首曲目时,会用自家的元数据覆盖显示。但对于 **上传的文件**、本地文件(Apple Music 的「资料库」功能、Spotify Local Files)以及 **通过分销商上传到流媒体平台** 的内容,你的标签绝对重要。下面是各场景下 Evertag 的设置方式:

### 为 Apple Music 准备文件(Cloud Music Library / iTunes Match)

- **ID3v2.4: 开** — Apple Music 正确处理 UTF-8。
- **专辑封面: 大** — Apple 的应用能很好地呈现大封面;原始尺寸过头。
- **标签复制: 关** — 不需要。
- 确保 **Album Artist** 已正确填写 — Apple Music 会用它进行分组。

### 为 Spotify Local Files 准备文件

Spotify Local Files 只显示标签良好的文件。Spotify 读取的标签有限。

- 大多数情况下 **ID3v2.4: 开**。如果某曲目编辑后在 Spotify 中显示不正确,**尝试以 ID3v2.4: 关 保存**(即作为 ID3v2.3) — Spotify 的解析器对 v2.4 历来比较保守。
- **专辑封面: 中或大** — Spotify 会把封面缩小。
- 至少填写 **标题**、**艺术家**、**专辑** 和 **曲目编号**。

### 为分销商上传准备文件(DistroKid、TuneCore、CD Baby 等)

如果你是上传自己作品到流媒体平台的艺术家,你的分销商通常会读取标签,但也会在它的界面里要求填写元数据。无论哪种方式:

- **ID3v2.3** 通常是更安全的默认 — 许多分销商管线建于多年前,偏好旧格式。
- 嵌入 **大** 尺寸封面(大多数分销商要求 ≥ 1,400 × 1,400 px 的封面 — 请查看其指南)。
- 不要依赖扩展标签 — 分销商只读取核心字段。

### 为 Plex、Jellyfin、Navidrome、Subsonic、Emby 准备文件

这些自托管媒体服务器的容忍度很高。它们对 v2.3 和 v2.4 都能干净读取,并能很好地处理 UTF-8。

- **ID3v2.4: 开** 即可。
- **专辑封面: 大** 或 **特大** — 这些服务器会把封面送给移动客户端和 CarPlay 屏幕,质量很重要。
- 强烈建议 **Album Artist** — 这是 Plex/Jellyfin 用来按艺术家正确分组的字段。

### 为车载音响和较旧硬件准备文件

- **ID3v2.4: 关**(改用 ID3v2.3) — 较旧的主机往往不支持 v2.4。
- **专辑封面: 中** — 许多车载显示器在大尺寸嵌入封面上会卡顿。
- **标签复制: 开** — 较旧的车载音响有时只读取 ID3v1 备援。

## 其他改进

### Liquid Glass 设计

Evertag 4.2 的整个应用界面已针对 Apple 全新的 **Liquid Glass** 材质进行更新 — 半透明表面、更顺滑的动画,以及自然融入 iOS、iPadOS 和 macOS 的精致控件。

### 更新的连接库

我们刷新了 Evertag 用于与 **WebDAV**、**SMB**、**DLNA**、**Dropbox**、**Google Drive**、**OneDrive** 及其他服务通信的底层库。结果:边缘场景下连接失败更少,对较新版本服务器支持更好,远程文件标签编辑也更可靠。

### 翻译与本地化修正

基于用户直接反馈的多语种 UI 修正。多种语言中较小按钮的文本贴合更佳。

### 受你反馈启发的小打磨

基于 App Store 评论与 support@everappz.com 邮件的多项细节改进。我们阅读每一条消息。

## 获取 Evertag 4.2

[**在 App Store 下载 Evertag**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) 或在 App Store 中更新。Evertag 是免费下载的,部分高级功能可通过应用内升级解锁。新的云连接、网络协议、Wi-Fi Drive 改进和 Liquid Glass UI 都包含在基础更新中。

如果你喜欢这款应用,请在 App Store 留下评分 — 这真的对我们很有帮助。如果你有反馈或遇到问题,请发邮件到 **support@everappz.com**。我们阅读每一条消息。

## 常见问题

{{% details title="Evertag 4.2 有哪些新功能?" closed="true" %}}
Evertag 4.2 新增 6 项以上的云端和服务器连接(Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS),带多选和更聪明的上传队列的全新 Wi-Fi Drive、Liquid Glass UI 更新、更新的连接库、关键的标签编辑 bug 修复以及翻译改进。
{{% /details %}}

{{% details title="在 Evertag 中应使用 ID3v2.4 还是 ID3v2.3?" closed="true" %}}
对现代播放器(Evermusic、Plex、Jellyfin、Apple Music、foobar2000、VLC、现代 Android 应用)以及包含非拉丁字符的库,使用 **ID3v2.4** — UTF-8 支持意味着中文、韩文、日文、俄文、阿拉伯文和希伯来文标签更干净。如果你的标签在某些应用中显示错误、面向较旧的车载音响,或某条流媒体分销商管线拒绝 v2.4,使用 **ID3v2.3**。你随时可以切换并重新保存。
{{% /details %}}

{{% details title="为什么编辑后我的标签在 Spotify 显示错误?" closed="true" %}}
Spotify 大多显示其自家目录的元数据 — 你的本地标签仅用于「Local Files」或你作为艺术家上传的内容。如果你为 Spotify Local Files 打标签后未正确显示,尝试在 Evertag 中关闭 ID3v2.4 并保存为 ID3v2.3 — Spotify 的解析器对 v2.4 历来较保守。
{{% /details %}}

{{% details title="在 Evertag 中应选择什么尺寸的专辑封面?" closed="true" %}}
对大多数用户:**大**。在手机、iPad、Mac 和现代车载显示器上看起来都很棒,且不会过度增大文件。库非常大、想节省磁盘的话用 **中**。仅当需要存档级母带或确实需要最高质量时使用 **原始**(无缩放) — 但要注意一些较旧播放器对超大嵌入封面会有困难。**原始** 属于 Evertag 高级个性化升级的一部分。
{{% /details %}}

{{% details title="较大的专辑封面会让我的文件更大吗?" closed="true" %}}
会。嵌入一张 3,000 × 3,000 px 的封面可为单个音频文件增加几 MB。以 1,000 首曲目的库计算,总量可达 GB。如果存储紧张,使用 中 或 大;如果你从 NAS 流播放、不在意大小,特大 或 原始 也可以。
{{% /details %}}

{{% details title="什么是标签复制,我应该启用吗?" closed="true" %}}
标签复制把核心元数据同时写入文件的 ID3v1(传统 128 字节)和 ID3v2(现代)两个区段。仅当你面向非常老旧的播放器或读取 ID3v1 的硬件时启用。对所有现代场景(智能手机、电脑、近期车载音响),保持关闭即可。
{{% /details %}}

{{% details title="Evertag 是直接编辑云端文件中的标签吗?" closed="true" %}}
是。连接到你的云端(Google Drive、Dropbox、OneDrive、iCloud Drive、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3 等)或通过 FTP/SFTP/NFS,然后打开文件并像本地文件一样编辑标签。Evertag 会下载文件,应用你的修改,并把更新后的版本上传回去。你可以在设置中选择「始终询问」、「自动上传」或「不上传」模式。
{{% /details %}}

{{% details title="可以在 iPhone 上用 Evertag 编辑 FLAC 标签吗?" closed="true" %}}
可以。Evertag 支持 FLAC、MP3、M4A/MP4、AIFF、WAV、OGG、APE 及其他主要格式,并提供完整的标签读写支持,含嵌入封面。
{{% /details %}}

{{% details title="如何用 SFTP 安全地在我的家庭服务器上编辑标签?" closed="true" %}}
打开 Evertag,进入连接选项卡,选择 SFTP,然后输入服务器的主机名或 IP、端口(通常为 22)、用户名,以及密码或 SSH 私钥。Evertag 会浏览你的远程文件夹,并通过 SSH 上的端到端加密直接编辑标签。
{{% /details %}}

{{% details title="可以一次编辑多个文件的标签吗?" closed="true" %}}
可以。在设置中启用 **同时编辑文件**。选择多个文件,打开标签编辑器,你修改的任何字段都会应用到所有所选文件。这是为整张专辑设置相同的 album artist、年份或类型的最快方法。
{{% /details %}}

{{% details title="Evertag 4.2 是免费更新吗?" closed="true" %}}
是的。Evertag 在 App Store 上免费下载,4.2 也是面向所有现有用户的免费更新。新的云端集成、Wi-Fi Drive 改进和 Liquid Glass UI 都包含在基础更新中。
{{% /details %}}

{{% details title="Evertag 4.2 在哪些设备上可用?" closed="true" %}}
Evertag 4.2 在 iPhone、iPad 和 Mac 上运行。iCloud Drive 同步会让你的标签编辑器设置在不同设备间保持一致。
{{% /details %}}
