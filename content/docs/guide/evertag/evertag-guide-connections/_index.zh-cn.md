---
title: "连接"
date: 2020-02-01
description: "了解如何将云存储、NAS 和电脑连接到 Evertag。直接从云存储、个人 NAS 或 Mac/PC 访问和编辑音频文件。"
keywords: [
  "Evertag 云设置", "连接 iCloud 到 Evertag", "iOS SMB 文件访问",
  "WebDAV 音频标签编辑器", "NAS 元数据编辑", "Wi-Fi Drive Evertag",
  "传输音频文件到 iPhone", "Evertag iTunes File Sharing", "从云端编辑 FLAC 标签"
]
tags: ["指南", "evertag", "连接"]
readingTime: 11
---


在此屏幕上，您可以连接各种包含音频文件的来源。您可以集成 Google Drive、Dropbox、OneDrive、iCloud 等流行云服务，以及连接您的 Mac 或 PC。此外，您还可以选择编辑存储在 Apple Time Capsule、WD Cloud Home 或任何支持 SMB 或 WebDAV 的 NAS 上的音频文件。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Connections Screen" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## 快速访问

在连接屏幕顶部，您会找到一个**快速访问**列表。任何添加到收藏夹的云文件夹——即使嵌套在多层目录中——都会显示在这里，让您无需每次都浏览父文件夹即可直接跳转。

## 连接到云存储

- 打开「连接」标签页  
- 从菜单中选择「连接到云存储」  
- 从列表中选择云存储服务  
- 输入您的凭据，然后点击「完成」。

如果遇到任何问题，请检查您的互联网连接和登录名/密码。  
在应用的高级版本中，您可以添加无限数量的服务。

## 支持的云存储服务

目前，应用支持最流行的云存储服务：iCloud Drive、Google Drive、Dropbox、OneDrive、Box、MEGA、Yandex.Disk、pCloud、Synology Drive、MediaFire、WD My Cloud Home、InfiniCLOUD (TeraCLOUD)、HiDrive、OpenDrive、MyDrive、Put.io、Cloud Mail.ru、百度网盘，以及任何 SMB 或 WebDAV 服务器。

## 安全与隐私

我们仅使用官方 SDK 和安全连接与已连接的云服务交互。您的登录名和密码对应用程序不可访问。应用程序向云服务发出的所有请求都经过加密。

当您输入登录名和密码时，应用程序会显示云服务提供商提供的官方授权页面，整个授权过程在应用程序外部进行。授权成功后，云服务提供商将授权令牌发送给应用程序，该令牌用于进行 API 调用。

授权令牌是允许第三方应用程序与云存储交互的数字密钥。授权令牌存储在设备上名为 Keychain 的安全系统存储中。您可以将文件从已连接的云服务下载到设备，这些文件将存放在应用的「文档」目录中。您可以随时使用内置文件管理器删除这些文件。

应用程序不会共享来自已连接云账户的任何信息。您可以随时通过在网络浏览器中打开账户设置页面来撤销对云账户的访问权限。

## 撤销授权令牌

在网络浏览器中登录您的账户并导航到设置页面。在那里，您可以找到所有连接到您云账户的第三方应用，并在不想继续使用时删除其中任何一个。详细说明可在[此处](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)找到。

您也可以在应用程序中断开已连接的云账户，授权令牌也将从您的设备中删除。如果您从设备中删除应用程序，所有已下载的数据和访问令牌也将被删除。

## 断开云存储或更改配置

- 在应用界面中找到您要管理的云存储。  
- 点击服务标题旁边的「...」按钮以访问更多选项。  
  - **重命名**：更改云服务在列表中显示的名称。  
  - **设置**：修改云服务的配置或身份验证数据。如果授权令牌已过期，有时可能需要重新授权已连接的云服务。  
  - **断开连接**：完全切断应用与云服务之间的连接。请注意，选择此选项将从应用的音乐库中删除与此云服务关联的所有歌曲，但它们仍将保留在服务器上。

## 连接到电脑或 NAS

您还可以使用 SMB、DLNA 或 WebDAV 协议连接您的电脑、个人 NAS 或其他网络设备。

## 通过 SMB 连接到电脑

- 点击「连接到云存储」→ SMB。  
- 在 URL 字段中输入电脑 IP 地址和共享文件夹名称，格式为 smb://computer-ip-address/shared-folder-name  
- 选择协议版本：Auto、SMB1、SMB2  
- 输入登录名和密码（如果需要）  
- 点击「完成」。

如果连接成功，您将在「云存储」部分看到已连接的存储。  
有关如何使用 SMB 连接 Mac 或 PC 的完整教程，请访问[此处](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)。

## 通过 WebDAV 连接到 NAS

所有步骤相同，只是 URL 字段不同。  
URL 应采用 http://server-name 格式，如果服务器支持 SSL，则使用 https://server-name。  
有关如何使用 WebDAV 协议连接 NAS 的完整教程，请访问[此处](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)。

## 可用设备

此部分显示您本地网络中所有可通过应用连接的设备。  
要与设备建立连接，请按以下步骤操作：

- 打开应用并转到「可用设备」部分。  
- 从列表中点击您要连接的设备。  
- 如果需要，输入您的登录详细信息以完成连接。

## Wi-Fi Drive

Wi-Fi Drive 是一种便捷技术，可通过桌面浏览器将文件从电脑无线传输到 iOS 设备。  
要有效使用此功能，请确保您的设备和电脑连接到同一 Wi-Fi 网络。  
以下是使用 Wi-Fi Drive 的分步指南。

## 启用 Wi-Fi Drive

- 打开应用并转到「连接」标签页。  
- 选择「通过 Wi-Fi 连接」以访问 Wi-Fi Drive 主屏幕。  
- 点击「启动 Wi-Fi Drive」以启用 Wi-Fi Drive。

## 在电脑上访问 Wi-Fi Drive

- 在电脑（台式机或笔记本电脑）上，打开网络浏览器（如 Chrome、Firefox 或 Safari）。  
- 在浏览器的地址栏中，输入应用程序提供的 URL。

## 无线传输文件

当对应您 iOS 设备的网页在浏览器中打开后，您可以轻松地将文件从电脑拖放到网页上。  
您拖放的文件将开始传输到您的 iOS 设备，并可在应用程序内访问。

有关如何使用 Wi-Fi Drive 无线传输文件的详细说明，请访问[此处](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)。

## iTunes File Sharing

iTunes File Sharing 是另一种技术，允许您使用 Mac 上的 Finder 应用和 Lightning 数据线从电脑向设备传输文件。  
- 只需使用数据线将设备连接到电脑，然后在 Mac 上运行 Finder 应用。  
- 打开「位置」→「您的已连接设备」→「文件」→ 找到当前应用。  
- 点击应用图标查看所有共享文件夹。  
- 使用拖放方式将文件从电脑复制到设备上的共享文件夹。

有关如何使用 iTunes File Sharing 的详细说明，请访问[此处](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/)。

## 连接 USB 闪存盘

如果您有 SD 卡或 USB 闪存盘，可以在 iPhone/iPad 上使用 Lightning 或 USB-C 读卡器连接，或直接插入 Mac。应用目前支持 Apple 认证的读卡器。我们有关于如何将 USB 闪存盘连接到 iPhone 或 iPad 并管理其中文件的详细说明，请访问[此处](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it)。已连接的驱动器将显示在连接屏幕的**连接的配件**部分。

## 文件管理器

连接云存储服务后，点击其图标查看所有可用文件和文件夹。您可以使用内置文件管理器处理这些文件——下载、重命名、移动等。开始下载时，文件将出现在传输队列中。要查看传输队列，请转到「本地文件」标签页，点击左上角的旋转箭头图标。所有已下载的文件和文件夹均可在「本地文件」部分访问。

## 顶部工具栏

顶部工具栏位于导航栏下方，提供几个便捷操作的快速访问。您可以通过向下滑动手势显示或隐藏此工具栏。可用操作：

- **搜索**：在当前目录中执行快速搜索，轻松找到特定文件或文件夹。  

## 文件夹选项

当您在应用中打开文件夹时，点击屏幕右上角的「...」按钮即可找到一组便捷操作。  
可用操作：

- **选择**：激活文件选择模式，在文件夹中选择一个或多个文件。  
- **新建文件夹**：在当前文件夹中创建新文件夹以组织文件。  
- **上传文件**：将设备中的文件上传到在线文件夹。  
- **搜索**：在当前文件夹中搜索特定文件。  
- **排序**：按名称、大小或编辑日期对文件夹中的文件进行排序。  
- **网格/列表视图**：在表格视图和缩略图视图之间切换。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloud Folder Sort" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## 编辑在线文件

当需要管理云存储中的多个文件时，可以使用选择模式来简化操作。步骤如下：

- **激活选择模式**：打开应用并导航到包含云存储的部分。点击右上角的「...」按钮，选择「选择」菜单项以激活选择模式。  
- **选择文件**：每个文件或文件夹旁边会出现复选框。点击旁边的复选框选择一个或多个文件或文件夹。  
- **执行各种操作**：选择文件或文件夹后，您将可以访问针对您需求定制的多种操作。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Select" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## 文件操作

在文件标题附近，您会看到省略号符号「...」（三个点）——这是操作菜单。  
点击它可显示可用操作列表：

- **编辑音频标签**：访问内置标签编辑器，修改所选文件的音频标签。文件将临时下载到临时目录，确认更改后上传回存储。  
- **添加到收藏夹**：将文件添加到收藏文件列表以便快速访问。  
- **下载**：将文件或文件夹下载到设备以供离线使用。  
- **重命名**：直接在远程存储上重命名文件。  
- **移动**：将文件移动到云存储中的其他文件夹。  
- **打开方式**：将文件导出到其他兼容应用。文件将下载到设备，然后显示分享对话框。  
- **删除**：此操作会从云存储中永久删除文件。**此删除操作无法撤销**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Options" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

如果操作列表超出屏幕可用空间，只需在操作菜单中向下滚动即可访问更多选项。

## 文件夹操作

对于云存储中的每个文件夹，您都有多种可用操作。只需点击文件夹标题旁边的省略号图标「...」。如果看不到所有操作，请向下滚动以显示更多选项。可用操作：

- **添加到收藏夹**：将文件夹添加到收藏列表以便快速访问。  
- **下载**：将文件夹的所有内容下载到设备以供离线访问。  
- **重命名**：直接在远程存储上重命名文件夹。  
- **移动**：将文件夹移动到云存储中的其他位置。  
- **删除**：此操作会从云存储中永久删除文件夹及其内容。**此操作无法撤销**。

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Folder Options" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
