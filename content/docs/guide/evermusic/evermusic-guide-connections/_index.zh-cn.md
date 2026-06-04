---
title: "连接"
date: 2020-01-01
description: "了解如何使用 Evermusic 连接云服务、电脑、NAS 设备并管理音乐文件。Wi-Fi Drive、SMB、DLNA、WebDAV、iTunes 文件共享等的分步指南。"
keywords: [
  "Evermusic", "云端音乐播放器", "NAS 流媒体", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes 文件共享",
  "连接云存储", "iPhone 音乐传输", "iOS 文件管理器"
]
tags: ["evermusic", "指南", "连接"]
readingTime: 11
---


在「连接」屏幕上，您可以连接所有保存音乐的来源——流行的云服务、自托管媒体服务器、Mac 或 PC、个人 NAS、Apple Time Capsule、WD My Cloud Home，甚至 USB 闪存盘——并通过统一界面使用所有这些来源。「连接」也是您设置快速访问深层嵌套云文件夹以及为 Last.fm scrobbling 进行身份验证的地方。

屏幕被分为清晰标记的部分：顶部的快速访问（您收藏的云文件夹）、云存储（已添加的账户）、本地网络（Bonjour 发现的设备）、电脑（Wi-Fi Drive、iTunes 文件共享、SMB）、外部配件（已连接的 USB 闪存盘）以及其他服务（Last.fm 等）。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic 连接屏幕" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## 连接云存储

- 打开「连接」标签页。
- 从菜单中选择「连接云存储」。
- 从列表中选择云存储服务。
- 在提供商的官方授权页面登录（Evermusic 从不查看您的密码）。
- 点击「完成」。

{{< cards cols="1">}}
  {{< card title="" subtitle="连接云存储提供商选择器" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

如果遇到任何问题，请仔细检查您的网络连接和登录凭据，并确保该服务的双重认证配置正确。  
在应用程序的 Premium 版本中，您可以添加无限数量的服务。免费用户一次只能连接一个云账户。

## 支持的云存储服务

Evermusic 支持全系列流行的云和自托管服务。免费用户获得相同的提供商目录，但有单账户限制；Premium 解锁无限账户并取消大多数其他限制。

- **个人云账户：** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **自托管服务器和媒体库：** Plex · Jellyfin · Emby · Subsonic（以及所有 Subsonic 兼容服务器——Airsonic、Funkwhale、Gonic、Logitech Media Server、Ampache）· Navidrome · Nextcloud（以及通过共享 API 的 Owncloud）· Synology Drive · QNAP.
- **NAS 和文件共享协议：** SMB (SMB1, SMB2, Auto)、WebDAV (HTTP / HTTPS)、FTP / FTPS、SFTP（密码或公钥认证）、NFS 和 DLNA（只读——播放和下载）。
- **S3 兼容对象存储：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces、Linode Object Storage、IBM Cloud Object Storage 或任何 S3-API 端点。
- **本地网络发现：**「可用设备」部分自动列出您 Wi-Fi 上通过 Bonjour / mDNS 广播的任何设备——Plex、Jellyfin、Emby 服务器、Synology、QNAP、WD My Cloud Home、Apple Time Capsule、带附加硬盘的 AirPort 路由器等。

## 安全与隐私

我们仅使用官方 SDK 和安全连接与已连接的云服务交互。您的登录名和密码对应用程序不可见。从应用程序到云服务的所有请求均已加密。

当您输入登录名和密码时，应用程序会显示由云服务提供商提供的官方授权页面，所有授权过程均在应用程序外部进行。云服务提供商在成功授权后向应用程序发送 auth token，该 token 用于进行 API 调用。

Auth token 是允许第三方应用程序与云存储交互的数字密钥。Auth token 存储在您的设备上名为 Keychain 的安全系统存储中。您可以将文件从已连接的云服务下载到设备，这些文件将存放在应用程序的「Documents」目录中。您可以随时使用内置文件管理器删除这些文件。

应用程序不会共享已连接云账户中的任何信息。您可以随时通过在 Web 浏览器中打开账户设置页面来撤销对云账户的访问权限。

## 撤销 auth token

在 Web 浏览器中登录您的账户并导航到设置页面。在那里，您可以找到连接到您的云账户的所有第三方应用程序，并删除任何您不再想使用的应用程序。详细说明请参见[此处](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)。

您也可以在应用程序中断开已连接的云账户，auth token 也将从您的设备中删除。如果您从设备中删除应用程序，所有已下载的数据和访问令牌也将被删除。

## 断开云存储或更改配置

- 访问云存储选项：首先，在应用程序界面中找到您想管理的云存储。
- 点击「...」按钮：服务标题旁边，您会看到一个「...」按钮。点击它以访问其他选项。
  - **重命名**：如果您想更改云服务在列表中显示的名称，请选择「重命名」。
  - **设置**：要修改云服务的配置或认证数据，请选择「设置」。有时，如果授权令牌已过期，您可能需要重新授权已连接的云服务。
  - **断开连接**：如果您希望完全断开应用程序与云服务的连接，请选择「断开连接」。请注意，选择此选项将从应用程序的音乐库中删除与此云服务关联的所有歌曲，但它们将保留在服务器上。

{{< cards cols="1">}}
  {{< card title="" subtitle="已连接云存储的更多操作菜单" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## 连接电脑或 NAS

您也可以使用 SMB、DLNA 或 WebDAV 协议连接您的电脑、个人 NAS 或其他网络设备。

## 使用 SMB 连接电脑

- 点击「连接云存储」→ SMB。
- 在 URL 字段中输入电脑 IP 地址和共享文件夹名称，格式为 smb://computer-ip-address/shared-folder-name
- 选择协议版本：Auto、SMB1、SMB2
- 输入登录名和密码（如果需要）
- 点击「完成」。

如果连接成功，您将在「云存储」部分看到已连接的存储。  
关于如何使用 SMB 连接 Mac 或 PC 的完整教程请参见[此处](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)。

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB 连接设置" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## 使用 WebDAV 连接 NAS

所有步骤相同，除了 URL 字段。  
URL 应为 http://server-name 格式，如果服务器支持 SSL 则为 https://server-name。
关于如何使用 WebDAV 协议连接 NAS 存储的完整教程请参见[此处](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)。

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV 连接设置" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## 使用 DLNA 连接电脑或 NAS

您也可以使用 DLNA 协议共享位于 Windows PC 或个人 NAS 上的音乐库，并在应用程序中访问该库，如[此处](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)所述。DLNA 是一种流行且广泛使用的协议，但它只允许您播放或下载音乐。您无法上传文件或在服务器上创建新文件夹。

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA 连接设置" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## 可用设备

此部分显示您本地网络中可以通过应用程序连接的所有设备。  
要与设备建立连接，请按照以下步骤操作：

- 打开应用程序并进入「可用设备」部分。
- 从列表中点击您想连接的设备。
- 如有需要，输入您的登录信息以完成连接。

{{< cards cols="1">}}
  {{< card title="" subtitle="本地网络上的可用设备" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive 是一种便捷的技术，可通过桌面浏览器将文件从计算机无线传输到 iOS 设备。  
为了有效使用此功能，请确保您的设备和计算机连接到同一 Wi-Fi 网络。  
以下是如何使用 Wi-Fi Drive 的分步指南。

## 启用 Wi-Fi Drive

- 打开应用程序并进入「连接」标签页。
- 选择「通过 Wi-Fi 连接」以访问 Wi-Fi Drive 主屏幕。
- 点击「启动 Wi-Fi Drive」以启用 Wi-Fi Drive。

## 在您的电脑上访问 Wi-Fi Drive

- 在您的电脑（台式机或笔记本电脑）上，打开 Web 浏览器（如 Chrome、Firefox 或 Safari）。
- 在浏览器的地址栏中，输入应用程序提供的 URL。

## 无线传输文件

一旦 iOS 设备对应的网页在浏览器中打开，您就可以轻松地将文件从计算机拖放到网页上。  
您拖放的文件将开始传输到 iOS 设备，并可在应用程序中访问。

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive 服务器设置" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

关于如何使用 WiFi-Drive 无线传输文件的详细说明请参见[此处](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)。

## iTunes 文件共享

iTunes 文件共享是另一种技术，允许您使用 Mac 上的 Finder 应用程序和 lightning 数据线将文件从计算机传输到设备。  
- 只需使用数据线将设备连接到计算机并在 Mac 上运行 Finder 应用程序。 
- 打开「位置」→「已连接的设备」→「文件」→ 找到 Evermusic 应用程序。 
- 点击应用程序图标查看所有共享文件夹。 
- 使用拖放将文件从计算机复制到设备上的共享文件夹。  

关于如何使用 iTunes 文件共享的详细说明请参见[此处](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/)。

{{< cards cols="1">}}
  {{< card title="" subtitle="Mac 上的 iTunes / Finder 文件共享" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## 连接 USB 闪存盘

如果您有 SD 卡，可以使用 lightning 读卡器连接它。应用程序目前支持 Apple 认证读卡器和 iXpand Flash Drives。如果您有 iXpand Flash Drive - 将其插入 lightning 端口并打开应用程序。您将看到「已连接外部设备」消息和设备信息。只需点击闪存盘图标即可访问音乐文件夹，点击任何音频文件即可开始播放。关于如何将 USB 闪存盘连接到 iPhone 并收听音乐或管理其上文件的详细说明请参见[此处](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it)。

## 文件管理器

连接云存储服务后，点击其图标查看所有可用文件和文件夹。您可以使用内置文件管理器处理这些文件——下载、重命名、移动等等。开始下载时，文件将出现在传输队列中。要查看传输队列，转到「本地文件」标签页并点击左上角的旋转箭头图标。所有下载的文件和文件夹都在「本地文件」部分中可用。

## 顶部工具栏

顶部工具栏方便地位于导航栏下方，提供几个实用操作以便于访问。您可以通过向下滑动手势显示或隐藏此工具栏。以下是可用操作：

- **搜索**：此选项允许您在当前目录中执行快速搜索，轻松找到特定文件或文件夹。
- **继续播放**：如果在应用程序设置中启用，此功能将为当前文件夹恢复音频播放器队列和最后的媒体位置。
- **全部播放**：选择此操作时，应用程序将扫描当前文件夹及其子文件夹，将所有找到的音频文件添加到新的播放器队列中。
- **随机播放**：类似于「全部播放」，但在将文件添加到音频播放器队列之前对其进行随机排序。

{{< cards cols="1">}}
  {{< card title="" subtitle="云文件夹内的顶部工具栏" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## 文件夹选项

在应用程序中打开文件夹时，您会发现一组方便的操作，可通过点击屏幕右上角的「...」按钮访问。  
以下是这些操作的说明：

- **选择**：激活文件选择模式。此模式允许您选择文件夹内的一个或多个文件。
- **新建文件夹**：在当前文件夹内创建新文件夹。
- **启用离线模式**：为当前文件夹开启离线模式。离线模式不仅仅是简单的下载；它主动监控文件夹的变化。如果您在线向文件夹添加新文件，应用程序将自动将这些文件下载到您的设备。
- **上传文件**：将设备中的文件上传到在线文件夹。
- **搜索**：搜索当前文件夹中的特定文件。
- **排序**：按名称、大小或编辑日期等条件对文件夹中的文件进行排序。
- **网格/列表视图**：在表格视图和缩略图视图两种显示模式之间切换。

{{< cards cols="1">}}
  {{< card title="" subtitle="当前文件夹的更多操作菜单" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## 编辑在线文件

当您需要在 Evermusic 中管理云存储中的多个文件时，可以使用选择模式。请按照以下步骤操作：

- **激活选择模式**：打开应用程序并导航到包含云存储的部分。找到右上角的「...」（省略号）按钮。点击它并选择「选择」菜单项以激活选择模式。
- **选择文件**：您会注意到每个文件或文件夹旁边出现复选框。通过点击旁边的复选框选择一个或多个文件或文件夹。
- **执行各种操作**：选择要管理的文件或文件夹后，您将可以访问多个操作。

{{< cards cols="1">}}
  {{< card title="" subtitle="在线文件的选择模式" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## 文件操作

在文件标题旁边，您会注意到省略号符号「...」（三个点）——这是操作菜单。  
点击它以查看可用操作列表：

- **下一首播放**：选择此操作将所选文件插入播放器队列顶部，确保它在当前播放项目后立即播放。
- **稍后播放**：将文件添加到播放器队列底部。
- **添加到音乐库**：将文件合并到您的音乐库中。
- **添加到播放列表**：使用此操作将文件添加到现有播放列表或创建新播放列表。
- **编辑音频标签**：访问 Evermusic 的内置标签编辑器，修改所选文件的音频标签。
- **添加到收藏夹**：将文件添加到您的收藏夹列表。
- **下载**：将文件或文件夹下载到您的设备供离线使用。
- **重命名**：直接在远程存储上重命名文件。
- **移动**：将文件移动到云存储中的不同文件夹。
- **在其中打开**：将文件导出到另一个兼容应用程序。
- **删除**：此操作会永久从云存储中删除文件，此操作无法撤销。

{{< cards cols="1">}}
  {{< card title="" subtitle="单个文件的更多操作菜单" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

如果操作列表超出可用屏幕空间，只需在操作菜单中向下滚动以访问其他选项。

## 文件夹操作

对于云存储中的每个文件夹，都有各种可用操作。要访问这些选项，只需点击文件夹标题旁边的省略号图标「...」。以下是可用操作：

- **全部播放**：将当前播放器队列替换为所选文件夹中的所有项目。
- **下一首播放**：将整个文件夹添加到播放器队列顶部。
- **稍后播放**：将文件夹内容追加到播放器队列底部。
- **添加到音乐库**：将文件夹内容无缝整合到您的音乐库中。
- **添加到播放列表**：您可以将整个文件夹包含在播放列表中。
- **添加到收藏夹**：使用此操作将文件夹添加到您的收藏夹列表。
- **启用离线模式**：通过为所选文件夹启用离线模式，应用程序持续扫描变化并自动下载新文件。
- **下载**：将文件夹的所有内容下载到设备供离线访问。
- **重命名**：直接在远程存储上重命名文件夹。
- **移动**：将文件夹移动到云存储中的不同位置。
- **删除**：请谨慎使用此操作，因为它会永久从云存储中删除文件夹及其内容，此操作无法撤销。


## 快速访问

快速访问部分位于屏幕顶部。它让您快速访问已连接云服务中您收藏的和最近打开的文件。
每当您从云端打开文件或文件夹时，它都会被添加到「最近使用」列表中。要清除此列表，打开「最近使用」，点击「更多操作」按钮，然后选择「删除列表」。您还可以将深层嵌套的文件夹标记为收藏夹，以便快速访问而无需浏览目录结构。

## 其他服务

此部分显示增强您体验的额外功能。目前，应用程序支持 Last.fm scrobbling。连接后，您的播放统计数据会自动发送到您的 Last.fm 账户。您可以稍后访问您的 Last.fm 个人资料查看听歌分析并获取个性化音乐推荐。详细设置说明请参见[此处](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)。
