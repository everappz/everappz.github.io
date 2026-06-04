---
title: "文件"
date: 2020-02-01
lastmod: 2026-06-01
description: "了解如何在 iPhone、iPad 和 Mac 上使用 Evervideo 的文件标签页。在一个地方连接云服务、NAS 设备、媒体服务器和 RTSP 流。管理离线视频、传输队列、下载、Wi-Fi Drive、iTunes / Finder 文件共享和 USB 驱动器。支持 iCloud Drive、Google Drive、Dropbox、OneDrive、MEGA、Box、pCloud、Synology、QNAP、Plex、Jellyfin、Emby、Subsonic、Navidrome、SMB、WebDAV、NFS、FTP / SFTP、DLNA 和 S3 兼容存储。"
keywords: [
  "Evervideo 文件", "Evervideo 连接", "Evervideo 本地文件",
  "云视频设置 iPhone", "连接 Google Drive 视频", "SMB 视频流",
  "iOS WebDAV 视频播放器", "DLNA 视频 iPhone", "NAS 视频流",
  "Wi-Fi Drive 视频传输", "Evervideo iTunes 文件共享", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo 离线模式视频", "Evervideo 传输队列",
  "Evervideo 文件管理器", "Evervideo Documents 文件夹",
  "视频播放器 Synology", "视频播放器 QNAP",
  "视频播放器 Apple Time Capsule", "USB DAC 视频",
  "iXpand 视频播放器", "S3 视频播放器"
]
tags: ["使用指南", "evervideo", "文件", "连接", "云", "NAS", "Plex", "RTSP"]
readingTime: 14
---

文件标签页是 Evervideo 的多合一文件管理器。与大多数视频应用将云存储和本地文件分成不同标签页不同，Evervideo 将两者合并到一个可滚动的屏幕中，让您可以从 Plex 服务器切换到云文件夹再到 iPhone 的 Documents 文件夹，而无需在标签页之间切换。

文件标签页分为清晰的几个部分，按以下顺序显示在屏幕上：

- **快速访问** — 您最近打开的文件和文件夹的最近使用和收藏夹。
- **此应用中的文件** — Evervideo 沙盒 Documents 文件夹中的内容。
- **此 iPhone / iPad / Mac 上的文件** — 通过系统文件选取器显示的设备其他位置的视频。
- **云存储** — 您已连接的每个云账户、NAS 和媒体服务器。
- **可用设备** — 通过 Bonjour / mDNS 自动发现的本地网络上的服务器和驱动器。

文件屏幕右上角有一个传输按钮（旋转箭头图标）。点击它可打开传输队列，在这里您可以监控所有来源的每次下载和上传。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 已连接存储中的文件" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## 连接到云存储

文件标签页的云存储部分是所有已连接账户、NAS、媒体服务器和流所在的地方——并排，在一个可滚动的列表中。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 文件标签页中的云存储部分" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- 打开**文件**标签页。
- 滚动到**云存储**部分。
- 从菜单中点击**连接到云存储**。
- 从列表中选择云存储服务。
- 在云服务提供商提供的官方授权页面上输入您的凭据，然后点击**完成**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 连接云存储服务" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

如果遇到问题，请检查您的网络连接和登录 / 密码。在应用的 Premium 版本中，您可以添加无限数量的服务；免费版本最多支持三个。

## 支持的云存储服务、媒体服务器和协议

Evervideo 支持极其广泛的视频来源。以下所有内容都可通过单一的连接到云存储流程访问。

**个人云存储：** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**自托管媒体服务器：** Plex · Jellyfin · Emby · Subsonic（及每个 Subsonic 兼容服务器——Airsonic、Funkwhale、Gonic、Ampache）· Navidrome · Nextcloud（及通过共享 API 的 ownCloud）· Synology Drive · QNAP.

**NAS 和文件共享协议：** SMB（SMB1、SMB2、Auto）· WebDAV（HTTP / HTTPS）· FTP · FTPS · SFTP（SSH 文件传输协议，密码或公钥认证）· NFS · DLNA / UPnP（播放和下载）.

**直播和 IP 摄像头流：** RTSP——将 Evervideo 指向任意 `rtsp://` URL，它就可以直接播放。非常适合安全摄像头、IPTV 流、门铃摄像头、婴儿监视器和类似的直播来源。

**S3 兼容对象存储：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 以及任何其他 S3 API 端点。

**设备本地资料库：** Photos 资料库（所有视频、屏幕录制、相册）和 Music 应用资料库（专辑、流派、播放列表）——两者都显示在媒体资料库中，无需复制任何内容。

**局域网发现：** 可用设备部分自动列出 Wi-Fi 网络上的每个 Bonjour / mDNS 服务——Plex、Jellyfin、Emby 服务器、Synology、QNAP、带附加驱动器的 AirPort 路由器、Apple Time Capsule——让您无需输入 IP 地址即可点击连接。

每个连接都使用服务的官方 SDK 或开放协议，在支持的情况下使用基于 OAuth 的授权。您可以连接同一服务的多个账户（例如两个 Google Drive 账户，或同时使用 Plex 和 Jellyfin 服务器），并在云存储部分并排浏览它们。

## 安全和隐私

Evervideo 仅使用官方 SDK 和安全连接与已连接的云服务交互。您的登录名和密码对应用程序不可访问——所有传输均采用 TLS 加密。

当您输入登录名和密码时，应用程序会显示由云服务提供商提供的官方授权页面，整个授权过程在应用程序外部进行。成功授权后，云服务提供商向应用程序发送 auth-token，该 token 用于进行 API 调用。

Auth-token 是一个数字密钥，允许第三方应用程序代表您与云存储交互。该 token 存储在您设备上 Apple 的安全系统存储（Keychain）中，静态加密并受设备密码或生物识别锁保护。您可以将已连接云服务中的文件下载到设备；这些文件放置在应用的 Documents 目录中，可以随时使用内置文件管理器删除。

应用程序不会将您已连接云账户的任何信息与 Everappz、广告商或任何第三方共享。您可以随时通过在网络浏览器中打开账户设置页面来撤销对云账户的访问权限。

## 撤销 Auth-Token

要撤销 auth-token，请在网络浏览器中登录您的云账户，然后导航到安全或已连接应用页面。在那里您可以找到连接到您云账户的每个第三方应用，并在不再想使用时删除其中任何一个。Google 账户的详细说明可在[这里](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)找到。

您也可以在应用内断开云账户——这样做时，auth-token 会立即从您的设备上删除。如果您从设备上卸载应用，所有下载的数据和访问 token 都会随之自动删除。

## 断开云存储或更改配置

- **访问云存储选项** — 在文件标签页的**云存储**部分找到已连接的服务。
- **点击「...」按钮** 位于服务标题旁边，打开其他选项：
  - **重命名** — 更改云服务在您列表中显示的名称。
  - **设置** — 修改配置或认证数据。有时如果授权 token 已过期，您可能需要重新授权已连接的云服务。
  - **断开连接** — 完全切断应用与云服务之间的连接。这会从您的媒体资料库中删除与该服务关联的所有视频，但在服务器上保持完整不变。

## 连接到计算机或 NAS

您可以使用 SMB、WebDAV、FTP / FTPS、SFTP、NFS 或 DLNA 协议连接您的计算机、个人 NAS 或其他网络设备。这是将现有家庭媒体库——无论它位于 Mac、Windows PC、Synology、QNAP、Apple Time Capsule 还是 WD My Cloud Home 上——引入 Evervideo 而无需复制任何内容的最简单方式。

### 使用 SMB 连接到计算机

- 点击**连接到云存储 → SMB**。
- 使用格式 `smb://computer-ip-address/shared-folder-name` 输入计算机的 IP 地址和共享文件夹名称。
- 选择协议版本：**Auto**、**SMB1** 或 **SMB2**。
- 输入您的登录名和密码（如需）。
- 点击**完成**。

如果连接成功，共享会出现在云存储部分。关于如何使用 SMB 连接 Mac 或 PC 的完整教程可在[这里](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)找到。

### 使用 WebDAV 连接到 NAS

所有步骤与 SMB 相同，除了 URL 字段。如果服务器支持 SSL，请使用 `http://server-name` 或 `https://server-name`。WebDAV 与 Synology、QNAP、Nextcloud、ownCloud、WD My Cloud Home 以及任何具有 WebDAV 端点的其他服务器兼容。

WebDAV 的完整教程可在[这里](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)找到。

### 通过 DLNA / UPnP 连接

使用 DLNA / UPnP 协议共享位于 Windows PC 或 NAS 上的媒体库，并在 Evervideo 中访问，如[这里](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)所述。DLNA 被广泛支持，但它只允许您播放或下载视频——您无法在 DLNA 服务器上上传文件或创建新文件夹。

### 使用 FTP、FTPS 或 SFTP 连接

Evervideo 还支持经典的文件传输协议。要通过 FTP 或 FTPS 连接服务器，点击连接到云存储 → FTP，以 `ftp://server-name` 形式输入主机 URL（或 `ftps://server-name` 用于加密连接），提供登录名和密码，然后点击完成。对于 SFTP（SSH 文件传输协议），选择 SFTP 并提供密码或 SSH 密钥对。

### 连接到 NFS 共享

Evervideo 包含 NFS（网络文件系统）支持——方便用于偏好通过 NFS 而非 SMB 公开视频库的 Linux 主机、BSD 服务器和 NAS 设备。在连接到云存储菜单中选择 NFS，输入服务器地址和导出路径，然后点击完成。

## 连接 Plex Media Server

Evervideo 可以直接连接到 Plex Media Server 并浏览您的电影、电视节目和家庭视频库。点击连接到云存储 → Plex，用您的 Plex 账户登录，选择一个服务器，库就会出现在您的云服务旁边。同一局域网上的 Plex 服务器也会在可用设备部分自动发现。

## 连接 Jellyfin 或 Emby 服务器

Jellyfin（开源）和 Emby（商业）媒体服务器都在 Evervideo 中原生工作。点击连接到云存储 → Jellyfin 或 Emby，输入您的服务器 URL（通常是 `http://server-ip:8096`）和凭据，您的库就可以开始流媒体了。

## 连接 Subsonic 或 Navidrome 服务器

Evervideo 支持 Subsonic API，这意味着它与 Subsonic 本身、Navidrome 以及其他每个 Subsonic 兼容服务器兼容——包括 Airsonic、Funkwhale、Gonic、Logitech Media Server (LMS) 和 Ampache。点击连接到云存储 → Subsonic，输入服务器 URL 和凭据，库就会出现在云存储部分。

## 连接 RTSP 流（IP 摄像头、直播 TV、IPTV）

Evervideo 具有原生 RTSP 支持，因此您可以将其指向任何 RTSP 来源——安全摄像头、门铃摄像头、IPTV 提供商、婴儿监视器、广播源——Evervideo 将实时拉取和解码流。点击在线链接 → 添加链接，粘贴完整 URL（`rtsp://camera-ip:port/stream-path`），如需提供登录名和密码，然后点击完成。

## 连接到 S3 兼容对象存储

对于使用云对象存储的自托管用户和高级用户，Evervideo 包含一个 S3 兼容连接器。点击连接到云存储 → S3 存储，然后输入端点 URL、区域、访问密钥、秘密密钥和存储桶名称。这适用于 AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 以及任何其他 S3 API 端点。

## 可用设备

此部分显示您本地网络上可以通过 Bonjour / mDNS 发现从 Evervideo 连接的每个设备——Plex、Jellyfin、Emby 服务器、Synology、QNAP、带附加驱动器的 AirPort 路由器、Apple Time Capsule 等。要建立连接：

- 在文件标签页中滚动到可用设备部分。
- 点击您想连接的设备。
- 如需，输入登录详细信息以完成连接。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 本地网络上的可用设备" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive 让您可以通过任何桌面浏览器、Finder 或 File Explorer 从计算机无线传输文件到 iOS 设备。您的设备和计算机必须在同一 Wi-Fi 网络上。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### 启用 Wi-Fi Drive

- 在文件标签页中，滚动到云存储 → 通过 Wi-Fi 连接，打开 Wi-Fi Drive 主屏幕。
- （可选）为嵌入式 Web 服务器设置用户名和密码。
- 点击启动 Wi-Fi Drive。

### 在计算机上访问 Wi-Fi Drive

- 在计算机上打开 Web 浏览器（Chrome、Firefox、Safari 等）。
- 输入应用程序显示的 URL。
- 将文件从计算机拖放到网页上——它们将开始传输到您的 iOS 设备。

您还可以直接在 macOS 的 **Finder** 中（前往 → 连接到服务器…）或 Windows 的 File Explorer 中（映射网络驱动器…）挂载 Wi-Fi Drive，将您的 iPhone 或 iPad 作为常规网络驱动器使用。

详细说明可在[这里](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)找到。

## iTunes / Finder 文件共享

iTunes 文件共享（macOS Catalina 及更高版本中现为 Finder 文件共享）允许您使用 Lightning 或 USB-C 数据线传输文件。连接设备，在 Mac 上打开 Finder（或在 Windows 上打开 iTunes），在应用列表中找到 Evervideo，并将文件复制到其共享文件夹。

## 连接 USB 闪存驱动器或 SD 卡

通过 Lightning-to-USB / USB-C 适配器或读卡器将 USB 驱动器或 SD 卡插入 iPhone、iPad 或 Mac。打开文件 → 此 iPhone 上的文件 → 打开文件夹，导航到驱动器，选择视频文件或文件夹。Evervideo 直接从驱动器播放文件，无需复制到内部存储——非常适合非常大的 4K 库。

## 在已连接存储中浏览文件夹

点击任何已连接的云服务打开其文件浏览器。文件夹在可用时显示视频缩略图，点击视频会立即开始播放，同时在后台继续流式传输文件的其余部分。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 在已连接存储中浏览文件夹" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## 快速访问

快速访问部分位于文件标签页的顶部。它提供对您收藏的和最近打开的文件和文件夹的快速访问——来自云服务和设备存储。每当您从云端打开文件或文件夹时，它都会被添加到最近打开列表中。您可以将深层嵌套的文件夹标记为收藏夹，以便快速访问而无需遍历目录结构。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 在线链接和快速访问" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## 此应用中的文件

此部分显示存储在 Evervideo 沙盒 Documents 目录中的文件和文件夹——您从云端下载的所有内容、通过 Wi-Fi Drive 传输的、通过 Finder 文件共享复制的或从其他应用导入的。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 应用中的文件" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Documents 文件夹

Documents 文件夹是「此应用中的文件」内所有内容的根目录。您可以创建子文件夹、重命名文件、移动它们，以及按您喜欢的方式组织。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 本地文件 — Documents 文件夹" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## 此 iPhone / iPad / Mac 上的文件

此部分显示位于您设备上但在不同应用程序中的视频。您可以使用系统文件选取器将它们导入 Evervideo：

- 点击打开文件… 选择特定文件。
- 点击打开文件夹… 选择整个文件夹。

您还可以使用连接文件夹来创建设备上具有读 / 写访问权限的文件夹链接——非常适合在不复制任何内容的情况下处理 iCloud Drive 上的文件夹或附加的 USB 驱动器。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 此设备上的文件" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## 特殊文件夹

在文件标签页中，您会看到 Evervideo 自动创建和使用的几个特殊文件夹：

- **下载** — 从云端下载的每个文件默认出现在这里。在设置 → 文件管理器 → 将下载的文件保存到中自定义。
- **播放器缓存** — 媒体播放器缓存。默认情况下，播放器下载即将播放的视频以确保流畅播放。您可以在应用设置中禁用缓存或直接删除此文件夹。
- **iCloud** — 此文件夹中的文件会在连接到同一 iCloud 账户的所有设备之间同步。
- **离线文件夹** — 当您将文件夹、播放列表、专辑或流派标记为可离线使用时，文件会下载到此文件夹中。

## 顶部工具栏

位于导航栏下方的顶部工具栏提供多项操作，您可以通过向下滑动手势显示或隐藏：

- **搜索** — 在当前文件夹或部分中执行搜索。
- **继续播放** — 如果在设置中启用，恢复当前文件夹的播放器队列和上次视频位置。
- **播放全部** — 扫描当前文件夹及其子文件夹并将文件添加到播放器队列。
- **随机播放** — 与播放全部类似，但在添加前随机排序。

## 文件夹选项

打开文件夹后，点击右上角的 **「...」** 按钮查看以下操作：

- **选择** — 激活文件选择模式。
- **新建文件夹** — 在当前文件夹中创建新文件夹。
- **启用离线模式** — 为当前文件夹开启离线同步。在线添加的新文件会自动下载。
- **上传文件** — 将设备中的文件上传到在线文件夹。
- **搜索** — 在文件夹中搜索。
- **排序** — 按名称、大小、修改日期或元数据排序文件。
- **网格 / 列表视图** — 在表格视图和缩略图视图之间切换。缩略图视图显示大型视频海报预览。

## 选择模式

点击右上角的 **「...」** 并选择**选择**进入选择模式。每个文件和文件夹旁边会出现复选框。点击选择一个或多个项目，然后执行批量操作：播放下一个、稍后播放、添加到媒体资料库、添加到播放列表、复制、上传、移动、重命名或删除。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 文件管理器中的选择模式" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

如果您希望将已连接的云存储视为只读（防止意外删除），请启用设置 → 文件管理器 → 编辑在线文件 → 关闭，以从界面中隐藏所有破坏性操作。

## 文件操作

点击文件标题旁边的 **「...」** 图标可显示其操作菜单：

- **播放下一个** — 将文件插入播放器队列顶部。
- **稍后播放** — 将文件追加到播放器队列底部。
- **添加到媒体资料库** — 将文件纳入媒体资料库，按专辑和流派组织。
- **添加到播放列表** — 将文件添加到现有播放列表或创建新播放列表。
- **编辑标签** — 打开内置标签编辑器修改元数据。对于在线文件，文件会临时下载、编辑，然后在您确认后重新上传。
- **添加到收藏夹** — 将文件添加到收藏夹列表以便快速访问。
- **下载** — 将文件或文件夹下载到设备以供离线使用。
- **重命名** — 直接在远程存储上重命名文件。
- **移动** — 将文件移动到云存储中的不同文件夹。
- **添加到归档** — 将文件打包成单个 ZIP 文件（Premium 功能）。
- **在...中打开** — 通过系统共享表将文件导出到其他兼容应用。
- **删除** — 永久删除文件。**此操作无法撤销。**

## 文件夹操作

对于云存储中的每个文件夹，通过点击文件夹标题旁边的 **「...」** 图标可以使用多项操作。

- **播放全部** — 用文件夹中的所有视频替换当前播放器队列。
- **播放下一个 / 稍后播放** — 将整个文件夹添加到队列。
- **添加到媒体资料库** — 将文件夹内容纳入媒体资料库。
- **添加到播放列表** — 将整个文件夹添加到播放列表。
- **添加到收藏夹** — 将文件夹添加到收藏夹。
- **启用离线模式** — 除了简单下载，这还会持续监控文件夹中的新文件，并在它们出现在线时自动下载。
- **下载** — 将文件夹的所有内容下载到设备以供离线访问。
- **重命名 / 移动** — 在远程存储上重命名或移动文件夹。
- **添加到归档** — 将文件夹内容打包成 ZIP 文件（Premium 功能）。
- **删除** — 永久删除文件夹及其内容。**此操作无法撤销。**

## 传输队列

文件标签页右上角有一个**传输**按钮（旋转箭头图标）。点击它可打开传输队列——所有来源的每个活动下载和上传的列表，带有实时进度、速度和每个文件的预计时间。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 文件传输队列" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

您可以暂停、恢复、重试失败的传输、重新排列项目以优先处理特定下载，或逐个取消。您还可以在设置 → 文件管理器中调整传输队列速度（最大并行任务数）、网络类型（仅 Wi-Fi 或 Wi-Fi + 蜂窝网络）和后台传输。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 文件传输队列上的操作" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## 离线模式和同步离线文件夹

离线模式是一项实用功能，让您即使在没有网络连接时也可以观看喜爱的视频。当您为任何文件夹、播放列表、专辑或流派启用离线模式时，该集合中的所有文件都会自动下载到设备以供离线播放。它们显示在离线文件夹部分。

当您向远程服务器添加新文件时，它们也会自动下载——因此您的离线集合始终保持最新，无需您做任何操作。要手动重新同步，点击离线文件夹右上角的三个点，选择同步。

您可以在设置 → 文件管理器 → 同步离线文件夹 → 时间间隔中调整同步超时。

详细说明可在[这里](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/)找到。

## 个性化

在设置 → 个性化中，您可以配置文件标签页的显示方式：

- **文件屏幕样式** — 纯菜单（直接显示文件夹列表）或分组菜单（按类别分组内容——快速访问、特殊文件夹、云存储等）。
