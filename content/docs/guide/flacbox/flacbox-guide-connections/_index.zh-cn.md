---
title: "连接"
date: 2020-02-01
description: "了解如何将云服务和 NAS 设备连接到 Flacbox。从 iCloud Drive、Dropbox、Google Drive、OneDrive、MEGA、Box、pCloud、Synology Drive、Yandex Disk 等流式传输高分辨率音乐。使用 SMB、WebDAV、DLNA、FTP / SFTP、Wi-Fi Drive、iTunes / Finder 文件共享和 USB 闪存驱动器。"
keywords: [
  "Flacbox 云设置", "连接 Google Drive 到 Flacbox", "SMB 音乐流",
  "WebDAV iOS 播放器", "DLNA 音乐应用", "NAS 音频流", "Wi-Fi Drive iPhone",
  "传输文件到 iPhone", "Flacbox iTunes 文件共享", "连接 NAS 到 iPhone",
  "Synology Drive 音乐应用", "QNAP 音乐应用", "Bluesound 音乐应用",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm 报告播放记录",
  "iXpand 闪存驱动器音乐", "USB DAC iPhone"
]
tags: ["指南", "flacbox", "连接", "云", "NAS"]
readingTime: 12
---


在此屏幕上，您可以连接存储音乐的所有来源。您可以集成 Dropbox、Google Drive、iCloud Drive、OneDrive、MEGA、Box、pCloud、Yandex Disk、Synology Drive 等热门云服务，以及通过标准协议连接 Mac、PC 或 NAS。无论您的音乐收藏存储在 Dropbox 等云服务还是 Synology、QNAP、Buffalo、Apple Time Capsule、WD My Cloud Home 等个人 NAS 上，Flacbox 都能从单一屏幕连接所有这些来源。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 连接屏幕" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## 连接到云存储

- 打开**连接**标签页。
- 从菜单中选择**连接到云存储**。
- 从列表中选择云存储服务。
- 在云服务提供商的官方授权页面上输入您的凭据，然后点击**完成**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 添加云存储服务" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

如果遇到问题，请检查网络连接和登录名 / 密码。在 Premium 版本中，您可以添加无限数量的服务；免费版本最多支持三个。

## 支持的云存储服务、媒体服务器和协议

Flacbox 支持极为丰富的音乐来源。以下所有内容都可通过一个**连接到云存储**屏幕访问。

**个人云存储：** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**自托管服务器：** Plex · Jellyfin · Emby · Subsonic（及所有 Subsonic 兼容服务器——Airsonic、Funkwhale、Gonic、Logitech Media Server、Ampache）· Navidrome · Nextcloud（以及通过共享 API 的 ownCloud）· Synology Drive · QNAP.

**NAS 和文件共享协议：** SMB（SMB1、SMB2、Auto）· WebDAV（HTTP / HTTPS）· FTP · FTPS · SFTP（SSH 文件传输协议，密码或公钥认证）· NFS · DLNA / UPnP（播放和下载）。

**S3 兼容对象存储：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 及任何其他 S3-API 端点。

**局域网发现：**「可用设备」区域自动列出 Wi-Fi 上的所有 Bonjour / mDNS 服务，无需输入 IP 地址即可轻触连接。

每个连接都使用服务的**官方 SDK 或开放协议**，并在支持的情况下使用 OAuth 授权。您可以连接同一服务的多个账户，并在连接屏幕中并排浏览它们。

## 安全与隐私

我们仅使用官方 SDK 和安全连接与已连接的云服务进行交互。您的登录名和密码无法被应用程序访问——所有传输均经过 TLS 加密。

当您输入登录名和密码时，应用程序会显示云服务提供商的官方授权页面，整个授权过程在应用程序外部进行。云服务提供商在成功授权后向应用程序发送 auth-token，该 token 用于进行 API 调用。

auth-token 是一种数字密钥，允许第三方应用程序代表您与云存储进行交互。token 存储在设备上 Apple 的安全系统存储（Keychain）中，静态加密并由设备密码或生物特征锁保护。

应用程序不会将您已连接云账户中的任何信息与 Everappz、广告商或任何第三方共享。您可以随时通过在网页浏览器中打开账户设置页面来撤销对您云账户的访问权限。

## 撤销 Auth-Token

要撤销 auth-token，请在网页浏览器中登录您的云账户并导航到安全或已连接应用页面。在那里您可以找到连接到您云账户的每个第三方应用程序，并移除不再需要的任何应用。Google 账户的详细说明请参阅[此处](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)。

您也可以在应用程序内断开云账户——此时 auth-token 立即从您的设备中删除。如果您从设备上卸载应用程序，所有下载的数据和访问令牌都会自动随之删除。

## 断开云存储或更改配置

- **访问云存储选项** — 在**连接**屏幕中找到已连接的服务。
- **点击服务标题旁的「...」按钮**以打开更多选项：
  - **重命名** — 更改云服务在列表中的显示名称。
  - **设置** — 修改配置或身份验证数据。有时您可能需要重新授权，如果授权 token 已过期。
  - **断开连接** — 完全切断应用程序与云服务之间的连接。这会从您的应用音乐库中删除与该服务关联的所有歌曲，但它们在服务器上保持不变。

## 连接到电脑或 NAS

您也可以使用 SMB、DLNA 或 WebDAV 协议连接电脑、个人 NAS 或其他网络设备。这是将现有家庭音乐库——无论存储在 Mac、Windows PC、Synology 还是 NAS 上——带入 Flacbox 而无需复制任何内容的最简便方式。

## 通过 SMB 连接到电脑

- 点击**连接到云存储 → SMB**。
- 在 URL 字段中以 `smb://computer-ip-address/shared-folder-name` 格式输入电脑 IP 地址和共享文件夹名称。
- 选择协议版本：**Auto**、**SMB1** 或 **SMB2**。
- 输入登录名和密码（如需要）。
- 点击**完成**。

如果连接成功，您将在**云存储**部分看到已连接的存储。关于如何使用 SMB 连接 Mac 或 PC 的完整教程请参阅[此处](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)。

## 通过 WebDAV 连接到 NAS

所有步骤与 SMB 相同，除了 URL 字段。URL 应为 `http://server-name` 或 `https://server-name`（如果服务器支持 SSL）。WebDAV 可与 **Synology、QNAP、Nextcloud、ownCloud** 及许多其他服务器配合使用。

关于如何使用 WebDAV 连接 NAS 的完整教程请参阅[此处](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)。

## 通过 DLNA 连接到电脑或 NAS

您也可以使用 DLNA / UPnP 协议共享 Windows PC 或个人 NAS 上的音乐库，如[此处](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)所述。DLNA 只允许播放或下载音乐，无法上传文件或在 DLNA 服务器上创建新文件夹。

## 通过 FTP、FTPS 或 SFTP 连接到 NAS 或服务器

Flacbox 还支持经典文件传输协议。要通过 FTP 或 FTPS 连接服务器，点击**连接到云存储 → FTP**，以 `ftp://server-name`（或加密连接为 `ftps://server-name`）格式输入主机 URL，提供登录名和密码，然后点击**完成**。对于 **SFTP**，选择 **SFTP** 并提供密码或 SSH 密钥对。

## 连接到 NFS 共享

Flacbox 支持 **NFS**（网络文件系统）。在**连接到云存储**菜单中选择 **NFS**，输入服务器地址和导出路径，然后点击**完成**。

## 连接 Plex Media Server

Flacbox 可以直接连接 Plex Media Server 并按艺术家、专辑、流派和播放列表浏览您的音乐库。点击**连接到云存储 → Plex**，用您的 Plex 账户登录，选择一个服务器——音乐库将与您的云服务一起显示。

## 连接 Jellyfin 或 Emby 服务器

**Jellyfin**（开源）和 **Emby**（商业）媒体服务器在 Flacbox 中均可原生使用。点击**连接到云存储 → Jellyfin** 或 **Emby**，输入服务器 URL 和凭据，音乐库即可流式传输。

## 连接 Subsonic 或 Navidrome 服务器

Flacbox 支持 Subsonic API，即可与 **Subsonic**、**Navidrome** 及每个其他 Subsonic 兼容服务器配合使用。点击**连接到云存储 → Subsonic**，输入服务器 URL 和凭据。

## 连接到 S3 兼容对象存储

点击**连接到云存储 → S3 存储**，然后输入端点 URL、区域、访问密钥、秘密密钥和存储桶名称。适用于 AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces 及任何其他 S3-API 服务。

## 可用设备

此部分通过 Bonjour 发现显示本地网络上您可以连接的每个设备。

- 打开应用并前往「连接」下的**可用设备**部分。
- 点击您要连接的设备。
- 如需要，输入登录信息以完成连接。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 本地网络上的可用设备" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive 是一种便捷技术，可通过任何桌面浏览器从电脑无线传输文件到 iOS 设备。请确保您的设备和电脑连接到同一 Wi-Fi 网络。

### 启用 Wi-Fi Drive

- 打开应用并转到**连接**标签页。
- 选择**通过 Wi-Fi 连接**以访问 Wi-Fi Drive 主屏幕。
- （可选）为嵌入式 Web 服务器设置用户名和密码以保护访问。
- 点击**启动 Wi-Fi Drive** 以启用 Wi-Fi Drive。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### 在电脑上访问 Wi-Fi Drive

- 在电脑上打开网页浏览器（如 Chrome、Firefox 或 Safari）。
- 在地址栏中输入应用程序提供的 URL。

### 无线传输文件

当与您 iOS 设备对应的网页在浏览器中打开后，您可以轻松地从电脑将文件拖放到网页上。您拖放的文件将开始传输到您的 iOS 设备，并可在 Flacbox 内访问。

您也可以在 macOS 的 Finder 中直接挂载 Wi-Fi Drive（前往 → 连接到服务器…）或在 Windows 的文件资源管理器中（映射网络驱动器…）。

关于如何使用 Wi-Fi Drive 无线传输文件的详细说明请参阅[此处](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)。

## iTunes / Finder 文件共享

iTunes 文件共享（在 macOS Catalina 及更高版本上现为 Finder 文件共享）是通过 Lightning 或 USB-C 线缆从电脑传输文件到设备的另一种方式。

- 使用线缆将设备连接到电脑，并在 Mac 上运行 **Finder**（或在 Windows 上运行 **iTunes**）。
- 打开**位置 → 您已连接的设备 → 文件**并找到 Flacbox 应用。
- 点击应用图标以查看所有共享文件夹。
- 通过拖放将文件从电脑复制到设备上的共享文件夹。

关于如何使用 Finder 文件共享的详细说明请参阅[此处](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/)。

## 连接 USB 闪存驱动器

如果您有 SD 卡或 USB 驱动器，可以使用 Lightning to USB / SD 读卡器或 USB-C 驱动器（在 iPad 和 iPhone 15 / 16 / 17 / Pro 上）连接。应用程序支持 Apple 认证的读卡器和 iXpand 闪存驱动器。

关于如何将 USB 闪存驱动器连接到 iPhone 的详细说明请参阅[此处](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it)。

## 文件管理器

连接云存储服务后，点击其图标查看所有可用文件和文件夹。您可以使用内置文件管理器处理这些文件——下载、重命名、移动、上传、删除等。

## 顶部工具栏

顶部工具栏方便地位于导航栏下方，提供几个常用操作。您可以通过向下轻扫手势显示或隐藏它。

- **搜索** — 在当前目录中执行快速搜索。
- **继续播放** — 如果在应用设置中启用，将恢复音频播放器队列和当前文件夹的最后媒体位置。
- **播放全部** — 扫描当前文件夹及其子文件夹，然后将所有找到的音频文件添加到新的播放器队列中。
- **随机播放全部** — 与播放全部相似，但在添加到音频播放器队列之前随机排列文件。

## 文件夹选项

打开文件夹时，点击右上角的 **«...»** 按钮可访问操作：

- **选择** — 激活文件选择模式。
- **新建文件夹** — 在当前文件夹中创建新文件夹。
- **启用离线模式** — 为当前文件夹切换离线模式，自动监控文件夹变化。
- **上传文件** — 将设备上的文件上传到在线文件夹。
- **搜索** — 在当前文件夹中搜索特定文件。
- **排序** — 按名称、大小、修改日期或元数据排序文件。
- **网格 / 列表视图** — 在表格视图和缩略图视图之间切换。

## 编辑在线文件

要管理云存储中的多个文件，使用**选择模式**：

- **激活选择模式** — 点击右上角的 **«...»** 按钮并选择**选择**。
- **选择文件** — 每个文件和文件夹旁边出现复选框。
- **执行操作** — 选择文件后，可进行：播放下一首、稍后播放、添加到音乐库、添加到播放列表、复制、上传、移动、重命名、删除。

## 文件操作

点击文件标题旁的 **«...»** 图标以显示操作菜单：

- **播放下一首** — 将文件插入播放器队列顶部。
- **稍后播放** — 将文件追加到播放器队列底部。
- **添加到音乐库** — 将文件纳入音乐库。
- **添加到播放列表** — 将文件添加到现有播放列表或创建新播放列表。
- **编辑音频标签** — 打开内置标签编辑器修改元数据。
- **添加到收藏夹** — 将文件添加到收藏夹以便快速访问。
- **下载** — 将文件或文件夹下载到设备以供离线使用。
- **重命名** — 直接在远程存储上重命名文件。
- **移动** — 将文件移动到云存储中的其他文件夹。
- **打开方式** — 将文件导出到另一个兼容应用。
- **删除** — 从云存储中永久删除文件。**此操作无法撤销。**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 已连接云存储中文件的更多操作" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

## 文件夹操作

对于云存储中的每个文件夹，点击文件夹标题旁的 **«...»** 图标可访问多种操作：

- **播放全部** — 用所选文件夹中的所有内容替换当前播放器队列。
- **播放下一首** — 将整个文件夹添加到播放器队列顶部。
- **稍后播放** — 将文件夹内容追加到播放器队列底部。
- **添加到音乐库** — 将文件夹内容纳入音乐库。
- **添加到播放列表** — 将整个文件夹添加到播放列表。
- **添加到收藏夹** — 将文件夹添加到收藏夹以便快速访问。
- **启用离线模式** — 持续监控文件夹并在文件出现时自动下载。
- **下载** — 将文件夹所有内容下载到设备以供离线访问。
- **重命名** — 直接在远程存储上重命名文件夹。
- **移动** — 将文件夹移动到云存储中的其他位置。
- **归档 (ZIP)** — 将文件夹内容打包成单个 ZIP 文件（Premium 功能）。
- **删除** — 从云存储中永久删除文件夹及其内容。**此操作无法撤销。**

## 快速访问

快速访问部分位于屏幕顶部。它让您快速访问已连接云服务中的收藏和最近打开的文件。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox 在线链接和快速访问" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## 其他服务

此部分显示增强使用体验的额外功能。目前，应用程序支持 **Last.fm** 报告播放记录——连接后，您的播放统计数据会自动发送到您的 Last.fm 账户。详细设置说明请参阅[此处](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)。

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm 连接" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
