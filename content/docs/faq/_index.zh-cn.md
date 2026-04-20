---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: '常见问题解答'
description: '查找关于 Evermusic、Flacbox、Evervideo 和 Evertag 的常见问题解答。探索云端流媒体、文件管理、播放选项、元数据编辑等功能。'
keywords: [
  "Evermusic 常见问题", "Flacbox 支持", "Evervideo 帮助", "Evertag 问题",
  "如何使用 Evermusic", "云音乐播放器故障排除", "离线播放指南",
  "音频标签编辑器支持", "视频流问题", "文件传输教程"
]
tags: [
  "常见问题", "帮助", "支持", "evermusic", "flacbox", "evervideo", "evertag",
  "云设置", "播放问题", "文件管理", "元数据编辑",
  "故障排除", "离线模式", "音乐播放器", "视频播放器"
]
aliases:
  - /blog/categories/how-to/
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## 学习如何使用我们的应用

正在寻找使用我们某款应用的答案或帮助？您来对地方了。

我们的常见问题页面将帮助您连接云存储、管理音乐和视频文件、设置离线播放、调整均衡器设置、修复元数据等。

在下方浏览您的应用常见问题以开始，或查阅我们从用户邮件收到的常见问题和解答。

## 选择您的应用

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="播放 360° 视频，从 iCloud 流媒体，带字幕观看，应用视频均衡器，用播放列表组织内容，下载视频供离线观看。"
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="具有离线模式、音频均衡器、交叉淡入淡出、无缝播放、播放列表管理、完整音乐库和内置文件管理器的云音乐播放器。"
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="适用于 iPhone 和 Mac 的高解析度音频播放器。以 FLAC、ALAC、APE 和 DSD 等无损格式聆听音乐。通过高级音频设置精细调节输出。"
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="具有批量编辑功能的智能音乐标签编辑器。修复缺失的元数据、专辑封面等。编辑 ID3、FLAC、APE 标签——支持超过 120 个字段。" 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## 常见问题和解答

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="为什么我无法在旧版 iOS（15.8.4）上登录 pCloud？" closed="true" %}}
pCloud 的网页登录页面可能无法在 15.8.4 等旧版 iOS 上正常显示，从而导致无法在云连接界面中输入电子邮件和密码。<br><br>

作为解决方法，您可以使用 **WebDAV** 协议，该协议受 pCloud 支持，并在所有 iOS 版本上稳定运行。

**WebDAV 设置：**<br>
- **美国服务器：** `https://webdav.pcloud.com`  
- **欧洲服务器：** `https://ewebdav.pcloud.com`  
- **用户名：** 您的 pCloud 电子邮件地址  
- **密码：** 您的 pCloud 账户密码  

打开应用 → 连接 → 连接云存储 → 选择 **WebDAV** → 输入您的凭据和服务器 URL。

此方法将让您连接到 pCloud 存储并在旧设备上无障碍访问文件。
{{% /details %}}

{{% details title="如何在 Mac (macOS) 上通过 AirPlay 播放音乐？" closed="true" %}}
macOS 版应用不像 iOS 那样内置 AirPlay、Chromecast 或蓝牙连接按钮。<br><br>

要在 MacBook Pro 上使用 **AirPlay**，请按照以下步骤操作：

1. 转到屏幕**右上角**，打开**控制中心**（时钟旁边）。  
2. 点击**声音/音量**图标。  
3. 在下一个界面中，点击 **AirPlay** 查看所有可用 AirPlay 设备的列表。  
4. 选择所需设备开始播放音乐。  

这将把所有系统音频（包括来自 Evermusic 或 Flacbox 的音频）路由到您选择的 AirPlay 设备。
{{% /details %}}

{{% details title="为什么我在 iPhone 上购买的 Premium 没有在 Mac 上激活？" closed="true" %}}
终身购买和订阅通过 **iCloud** 在 iOS 和 Mac 之间同步。<br><br>

要在 Mac 上激活 Premium：<br>
- 确保两台设备上都安装了最新版本的应用<br>
- 在两台设备上启用 **iCloud**<br>
- 在 iOS 设备上启动应用，等待 1 分钟让购买信息上传<br>
- 在 Mac 上，使用**相同的 Apple ID** 从 App Store 安装应用<br>
- 启动应用并等待几秒钟让信息同步<br>
- 或者，在两台设备的应用设置中点击**恢复购买**<br><br>

您的 Premium 功能将自动在 Mac 上激活。
{{% /details %}}

{{% details title="如何在设备之间自动同步播放列表？" closed="true" %}}
目前播放列表**没有自动同步**功能。<br><br>

您可以使用以下选项之一：<br>
- 从应用设置中**备份和恢复** [如何在 Evermusic 设备之间传输音乐库：分步指南](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **将播放列表导出为 M3U**，然后在另一台设备上导入：<br>
  - [如何导出播放列表](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [如何导入播放列表](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **归档播放列表或专辑**并通过 ZIP 传输：<br>
  - [播放列表归档指南](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="您的应用安全吗？我可以禁用分析功能吗？" closed="true" %}}
是的，您的隐私是我们的首要任务。<br><br>

- 所有数据——音乐文件、设置、云登录——都保存在您的设备上<br>
- 登录凭据安全存储在 **iOS 钥匙串**中<br>
- 我们只收集匿名崩溃和使用报告<br>
- 您可以在**应用设置 → 分析**中选择退出<br><br>

更多信息：<br>
- [隐私政策](/legal/privacy-policy/)<br>
- [Apple 钥匙串安全](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

如果使用个性化广告，Google Mobile Ads 需要显示同意设置。<br>
Premium 用户看不到广告，广告 SDK 已完全禁用。
{{% /details %}}

{{% details title="您的应用支持家人共享吗？" closed="true" %}}
是的，支持家人共享。<br><br>

要共享应用内购买：<br>
- 确保购买已设置为与您的家庭群组共享<br>
- 在家庭成员的设备上，转到**设置 > 购买 > 恢复购买**<br>
- 这将从 Apple 服务器请求购买数据并在其设备上激活
{{% /details %}}

{{% details title="如何加快元数据和云同步速度？" closed="true" %}}
要提高同步速度，请启用后台任务：<br><br>

- **设置 → 音乐库 → 元数据读取 → 在后台读取元数据**<br>
- **设置 → 音乐库 → 在线音乐同步 → 后台同步**<br><br>

此外，在 macOS 上，通过**设置 → 音乐库**提高元数据读取速度。<br>
如果播放器处于活动状态（正在播放音频），iOS 不会挂起应用，从而实现持续同步。
{{% /details %}}

{{% details title="如何取消订阅？" closed="true" %}}
您可以按照 Apple 的官方说明取消订阅：<br>
👉 [如何取消订阅](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="如何连接并从 WD MyCloud EX2 Ultra 流式传输音频？" closed="true" %}}

当您通过应用中的**连接 > 连接云存储 > My Cloud Home** 添加连接时，该功能官方设计支持 **WD MyCloud Home** 设备。<br>
WD MyCloud EX2 Ultra 对应用使用受限访问。<br><br>

但是，如果您已成功连接到 **WD MyCloud EX2 Ultra**、**WD MyCloud Mirror** 或其他 **WD MyCloud** 存储型号，您仍可以通过以下解决方法使用它：<br><br>

1. 打开**连接 → 连接云存储 → My Cloud Home**<br>
2. 使用内置文件管理器创建文件夹<br>
3. 将音乐文件上传到此文件夹<br>
4. 这些文件将存储在仅应用可访问的"沙箱"中<br>
5. 您现在可以直接流式传输或下载它们<br><br>

⚠️ 只有通过应用创建的文件夹才能从 NAS 访问。
{{% /details %}}

{{% details title="如何连接到 Koofr.eu？" closed="true" %}}
您可以使用 **WebDAV** 连接 Koofr。<br><br>

- Koofr WebDAV 设置指南：[koofr.eu 博客](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Evermusic/Flacbox WebDAV 指南：[如何使用 WebDAV 连接 NAS 存储并在 iPhone 或 Mac 上听音乐](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="应用的 URL scheme 是什么？" closed="true" %}}
以下是支持的 scheme：<br><br>

**Evermusic**<br>
- iOS（蓝色图标）：`lsevermusic://`<br>
- macOS：`lsevermusicmac://`<br>
- iOS（红色图标）：`lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS：`lsflap://`<br>
- macOS：`lsflapmac://`<br><br>

**Evertag**<br>
- iOS：`lsevertag://`<br>
- macOS：`lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS：`lsevervideo://`<br>
- macOS：`lsevervideomac://`
{{% /details %}}

{{% details title="应用在后台时音乐停止播放——如何修复？" closed="true" %}}
如果应用在后台崩溃或暂停：<br>
- 转到**设置 > 音乐库 > 在线音乐同步 > 后台同步 → 禁用**<br>
- **设置 > 音乐库 > 元数据读取 > 在后台读取元数据 → 禁用**<br>
- **设置 > 文件管理器 > 后台传输 → 禁用**
{{% /details %}}

{{% details title="无缝播放不起作用——如何修复？" closed="true" %}}
无缝播放取决于 iOS 版本和音频引擎。<br>
尝试切换音频引擎：<br>
- 转到**设置 → 音频播放器 → 常规 → 音频处理器**<br>
- 选择 **Core Audio** 以获得更好的无缝播放支持
{{% /details %}}

{{% details title="为什么应用在列表中只显示 100 个项目？" closed="true" %}}
应用使用分页以提高性能。<br>
要禁用它：<br>
- 转到**设置 → 个性化 → 内容加载限制 → 已停用**<br>
现在所有项目将一次性加载。
{{% /details %}}

{{% details title="为什么元数据中有奇怪的字符？" closed="true" %}}
尝试启用元数据规范化：<br>
- **设置 → 音乐库 → 元数据读取 → 规范化元数据编码**
{{% /details %}}

{{% details title="为什么应用无法读取带有特殊字符的文件夹名称？" closed="true" %}}
这是 **SMB2 协议**的已知问题。<br><br>

尝试以下解决方案：<br>
- 在服务器和应用设置中启用 **SMB1**<br>
- 使用**系统文件选择器**：<br>
  - 转到**本地文件 > 此设备上的文件 > 打开文件...**<br>
  - 使用 Apple 的原生菜单选择文件夹/文件<br><br>

或者，如果您的 NAS 支持，可使用 **WebDAV** 或 **DLNA** 连接。
{{% /details %}}

{{% details title="如何在 iCloud 中上传和管理音乐？" closed="true" %}}
– **如何将音乐上传到 iCloud？**  <br>
在浏览器中转到 [https://www.icloud.com](https://www.icloud.com)，创建文件夹，然后直接从 Mac 或 PC 上传音乐文件。<br>

– **如何管理 iCloud 存储？**  <br>
您有两个选项：  <br>
1. 在浏览器中使用 [https://www.icloud.com](https://www.icloud.com) 组织、上传或删除文件。<br>  
2. 在应用中，通过**连接 → 连接云存储 → iCloud Drive** 连接到 iCloud 后，使用内置文件管理器直接在 iCloud 存储中上传、下载、重命名文件夹或删除文件——无需保存到设备。<br>

⚠️ 删除文件时请小心。应用会永久删除文件（不会进入回收站，无法恢复）。<br>

在此了解更多：[如何从 iCloud Drive 在 iPhone 或 Mac 上流式传输音乐](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="如何将 10GB 音乐库从 Windows 11 传输到 iPhone 进行离线播放？" closed="true" %}}

您有多种可靠的方式将音乐库从 Windows 11 PC 移动到 iPhone，并在应用中离线使用。选择最适合您的方法：

1. **使用数据线连接（推荐用于大型库）**  <br>
   在 Windows 11 上使用 **Apple Devices** 应用通过 USB 直接将文件传输到 iPhone。  
   请按照 Apple 的指南操作：  
   https://support.apple.com/en-ph/120402 <br>

2. **通过 Wi-Fi Drive 无线传输**  <br>
   在应用中启用 **WiFi Drive** 功能，并通过计算机上的浏览器上传音乐。  
   分步说明：  
   [如何不使用 iTunes 通过 WiFi-Drive 将音乐文件从计算机传输到 iPhone](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **使用 DLNA 服务器无线传输**  <br>
   在 Windows 计算机上打开 DLNA 媒体服务器，将库直接流式传输或传输到应用。  
   指南：  
   [如何在 Windows 10 上启用 DLNA 媒体服务器并在 iPhone 上播放音乐](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **使用 SMB 文件共享无线传输**  <br>
   在 PC 上启用 **SMB 文件共享**，在应用中连接后按文件夹浏览、下载或传输文件。  
   说明：  
   [使用 SMB 协议将文件从计算机传输到 iPhone](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ 传输大型库（10GB+）时，有线 USB 传输通常是最快且最稳定的选项。

{{% /details %}}

</div>
