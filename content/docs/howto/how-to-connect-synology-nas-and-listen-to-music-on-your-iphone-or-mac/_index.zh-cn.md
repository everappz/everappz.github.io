---
title: "如何连接 Synology NAS 并在 iPhone 或 Mac 上收听音乐"
date: 2024-09-19
description: "了解如何使用原生 API 或 QuickConnect 连接您的 Synology NAS，并通过 Evermusic 和 Flacbox 在 iPhone 或 Mac 上串流高品质音乐。"
keywords: ["synology nas", "串流音乐", "quickconnect", "evermusic synology", "flacbox synology", "nas 音乐播放器", "iphone nas 音乐"]
tags: ["音乐", "串流", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**摘要：** 使用 Synology 的原生 API 将 Synology NAS 连接到 Evermusic 或 Flacbox —— 通过 IP 地址手动连接或通过 QuickConnect ID 自动连接。QuickConnect 让您无需端口转发即可远程串流音乐。两款应用都支持 FLAC、MP3、WAV 及其他高解析度格式。

如果您正在寻找一种无缝的方式来连接 Synology NAS 并在 iPhone 或 Mac 上享受音乐库，Evermusic 和 Flacbox 应用是完美的解决方案。这些应用支持多种音频格式，包括 FLAC、MP3 和 WAV，让您可以轻松地从 Synology NAS 直接串流和收听高品质音乐。

在本指南中，我们将向您展示如何使用 Synology 的原生 API 和 QuickConnect 功能将 Synology NAS 连接到 Evermusic 或 Flacbox 应用。通过利用 Synology 的直接 API，您可以在家庭网络之外安全地访问音乐库，无需 WebDAV、SMB、DLNA 等复杂配置。借助 QuickConnect，您可以使用 iPhone 或 Mac 从任何地方串流和管理音乐。

## 步骤 1：配置共享文件夹权限（可选）

1. 打开**控制面板**并转到**共享文件夹**部分。

![共享文件夹](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. 选择 **Music** 文件夹并点击**编辑**。

3. 在**权限**选项卡中配置权限。如果您只需要听音乐，请启用只读的访客访问；如果需要修改文件，请启用读写权限。保存更改。

![权限](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## 步骤 2：查找 Synology NAS IP 地址

1. 打开**控制面板**并转到**网络接口**选项卡。

![网络接口](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. 或使用浏览器访问 [find.synology.com](http://find.synology.com)。

![查找 Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. 记下 Synology NAS 的 IP 地址（例如 192.168.18.137）。

## 步骤 3：查找 Synology NAS 网络端口

您可以在此 [Synology 知识中心文章](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services)中找到 Synology 官方的 DSM 默认网络端口文档。

Synology DSM 使用以下默认端口：
- **HTTP（Web 访问）：** 端口 **5000**
- **HTTPS（安全 Web 访问）：** 端口 **5001**

这些是访问 DSM 界面的默认端口。

![网络端口](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## 步骤 4：启用 QuickConnect ID 功能

Synology QuickConnect ID 是一个唯一标识符，允许您通过互联网远程访问 Synology NAS，无需配置端口转发等复杂的网络设置。QuickConnect 通过使用 Synology 的服务器来建立 NAS 与您的设备（如智能手机或电脑）之间的连接，从而简化远程访问。

**如何查找或设置 QuickConnect ID：**

1. **登录 DSM。**
2. 转到**控制面板 > 外部访问 > QuickConnect**。
3. **启用 QuickConnect** 并创建或查看您的唯一 QuickConnect ID。

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## 步骤 5：使用 Evermusic 或 Flacbox 在 iPhone/Mac 上连接 Synology NAS

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) 和 [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) 都是为 iOS 和 macOS 设备设计的音乐播放器应用，各自提供独特的功能来管理和享受您的音乐库。

1. 打开 Evermusic 或 Flacbox 应用并转到**连接**选项卡。

![连接](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. 选择**连接云服务**并选择 **Synology Drive**。

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

您有两种连接选项：使用服务器 IP 地址和端口的**手动**连接，或通过 QuickConnect ID 的**自动**连接。

### 手动连接

对于手动方法，您需要在之前步骤中获取的直接 IP 地址和端口号。

1. 输入在步骤 2 中获取的服务器 URL，使用以下格式：协议://IP地址:端口号
   - HTTP 使用**端口 5000**，HTTPS 连接使用**端口 5001**。

   例如：
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. 实际端口号可在设置的步骤 3 中确认。
3. 输入 Synology NAS 的**用户名**和**密码**。
4. 点击**登录**以建立连接。

![手动连接](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### 自动连接

对于自动连接，您将使用步骤 4 中的 **QuickConnect ID**。无需手动输入 Synology NAS 的 IP 地址和端口号，只需输入 **QuickConnect ID**。应用将自动获取必要的连接信息。

此方法允许您远程访问 NAS，即使在家庭网络之外，也可以通过互联网管理文件，无需配置端口转发或静态 IP 地址。

![自动连接](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## 双重身份验证

从 DSM 4.2 开始，Synology 引入了**两步验证**以增强安全性。此功能需要由身份验证应用生成的**一次性密码 (OTP)** 代码，作为常规登录凭据的补充。如果您已启用两步验证，在输入用户名和密码后，还需要输入 OTP 才能登录 DSM 会话。

请注意，会话过期后，需要手动重新授权应用。要重新授权：

1. 转到应用中的**连接**选项卡。
2. 点击服务器名称旁边的**更多操作**按钮。
3. 从菜单中选择**设置**以输入新的身份验证代码并完成重新授权流程。

这确保即使您从不受信任的网络访问 NAS，您的数据也能保持安全。

## 步骤 6：浏览和播放音乐

1. 连接后，设备将出现在**已连接设备**列表中。

![已连接设备](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. 导航到 **Music** 文件夹，点击任意音频文件开始播放。

![播放音乐](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## 步骤 7：将已连接的云文件夹添加到音乐库

1. 在应用中打开**音乐库**部分。
2. 选择**添加音乐**并选择**连接**。
3. 选择已连接的 NAS 服务器并选择 **Music** 文件夹。点击**完成**。
4. 应用将扫描音乐文件夹并将支持的音频文件添加到音乐库。元数据将被加载，您的曲目将按专辑、艺术家和流派分组。

## 结语

按照这些步骤，您可以轻松地在 Synology NAS 上设置连接，并使用 Evermusic 或 Flacbox 将整个音乐库串流到 iPhone 或 Mac。无论是在家还是外出，都可以使用 QuickConnect 从任何地方无缝、高品质地访问您喜爱的曲目。充分利用这些应用提供的灵活性和便利性，轻松管理所有设备上的音乐收藏。

通过 QuickConnect 的安全远程访问和对多种音频格式的支持，您永远不会远离音乐。现在，NAS 上存储的文件只需轻轻一点！

## FAQ

{{% details title="手动连接和 QuickConnect 有什么区别？" closed="true" %}}
手动连接使用 NAS IP 地址和端口，在本地网络上运行。QuickConnect 使用 Synology 的中继服务从互联网上的任何地方建立连接，无需端口转发。
{{% /details %}}

{{% details title="我可以在家庭网络之外从 Synology NAS 串流音乐吗？" closed="true" %}}
可以。在 Synology NAS 上启用 QuickConnect，并在 Evermusic 或 Flacbox 中使用 QuickConnect ID，即可从任何有互联网连接的地方串流音乐。
{{% /details %}}

{{% details title="从 Synology NAS 串流时支持哪些音频格式？" closed="true" %}}
Evermusic 和 Flacbox 支持 FLAC、MP3、AAC、WAV、ALAC、OGG、WMA、DSD 及许多其他格式。从 Synology NAS 串流时，所有支持的格式均可使用。
{{% /details %}}

{{% details title="连接需要双重身份验证吗？" closed="true" %}}
不需要，2FA 是可选的。但是，如果您在 Synology DSM 上启用了两步验证，应用将在登录时要求输入一次性密码。会话过期时需要重新授权。
{{% /details %}}

{{% details title="应该使用 Synology 原生 API、WebDAV 还是 SMB 来连接？" closed="true" %}}
带有 QuickConnect 的 Synology 原生 API 是远程访问的最佳选择。对于本地网络使用，SMB 通常是最快的选项。WebDAV 在本地和远程访问中都表现良好。Evermusic 和 Flacbox 支持所有三种协议。
{{% /details %}}
