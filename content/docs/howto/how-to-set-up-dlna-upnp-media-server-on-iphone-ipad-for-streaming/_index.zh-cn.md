---
title: "如何在 iPhone 和 iPad 上搭建 DLNA/UPnP 媒体服务器进行流媒体播放"
description: "用 Everdisk 把你的 iPhone 或 iPad 变成 DLNA/UPnP 媒体服务器，通过 Wi-Fi 把照片、视频和音乐流式播放到智能电视、游戏主机、VLC 或 Kodi。完整设置教程，并附上如何从三星、LG 和索尼电视，以及 Windows、Mac、Linux、Android 和另一部 iPhone 连接。"
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "媒体服务器", "流媒体", "智能电视", "iphone", "ipad", "wifi"]
keywords: ["iPhone DLNA 服务器", "iPad UPnP 服务器", "如何在 iPhone 上搭建 DLNA", "从 iPhone 流媒体到智能电视", "iOS DLNA 媒体服务器", "无需数据线把视频流式播放到电视", "在电视上播放 iPhone 照片", "三星电视 DLNA iPhone", "LG 电视 DLNA iPhone", "索尼 Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA 媒体服务器", "iOS UPnP AV 媒体服务器", "从 iPhone 把音乐流式播放到电视", "iPhone 媒体服务器应用"]
readingTime: 9
---

{{< author-byline >}}

DLNA (也叫 UPnP AV) 是大多数智能电视背后默默工作的主力。它是一种共享语言，让电视或媒体播放器在同一个 Wi-Fi 上找到媒体库并从中播放，电视上什么都不用装。如果你的 iPhone 或 iPad 可以充当那个媒体库，你的照片、视频和音乐就会自动出现在大屏上。

本指南将介绍如何用 [Everdisk](/products/everdisk) 把你的 iPhone 或 iPad 变成 DLNA/UPnP 媒体服务器，以及如何从智能电视、游戏主机、VLC、Kodi、电脑、Android 手机，甚至第二部 iPhone 打开那个媒体库。一切都在你的本地 Wi-Fi 上运行，所以任何东西都不会被上传到别处。

## 你需要什么

- 一部安装了 [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) 的 iPhone 或 iPad。
- 一台与你的设备处于**同一 Wi-Fi 网络**的电视、播放器或电脑。
- 你想播放的照片、视频或音乐，已经在你的 iPhone 上 (在照片应用、音乐应用，或 Everdisk 的 Documents 文件夹里)。

## 在 Everdisk 中设置 DLNA 服务器

### 第 1 步：选择要共享的内容

打开 Everdisk，进入**共享**标签页。点击**分享什么**并挑选你的内容：

- 开启**允许访问整个照片图库**以共享每一个相簿，或点击**添加照片**挑选几张。
- 开启**允许访问整个音乐资料库**以共享你的歌曲，或点击**添加歌曲**做一个选择。
- 用**添加文件夹**和**添加文件**添加任意文件夹或文件。应用自己的 Documents 文件夹默认会被共享。

在共享开始之前，你至少需要选中一项内容。

### 第 2 步：开启电视与媒体中心 (DLNA)

依次进入**设置** → **共享** → **连接**。确保**电视与媒体中心**已开启。它默认是开着的，并带有 DLNA 标签。这就是电视和播放器要寻找的服务器。

### 第 3 步：开始共享

回到**共享**标签页，点击大大的**开始**按钮。你的设备现在就是你 Wi-Fi 上的一台媒体服务器了。它会以友好的名称出现在其他设备上，也就是应用中显示的设备名称 (在你更改之前，可能是「Speedy-Hare」之类的名字)。

DLNA 流媒体始终是开放的，所以在电视上不用输入密码。观看时请让 Everdisk 保持在屏幕上打开，因为 iOS 会暂停被完全推入后台的应用。

## 在智能电视上播放

这是最常见的情况，通常只需大约三十秒。

1. 让电视和你的 iPhone 处于**同一 Wi-Fi**。
2. 打开电视内置的媒体播放器。名称因品牌而异：**Media Player**、**Gallery**、**SmartShare** (LG)、**AllShare** 或 **SmartThings** (Samsung)、**Content Share** 或 **SimplyShare**。
3. 找到媒体服务器或来源的列表。你的设备会以它的名称出现在那里。
4. 选中它，浏览进入你的照片、视频或音乐，然后按播放。

预览缩略图会自动显示，所以你无需靠猜就能找到那个假期相簿或那部电影。

### 哪些电视可用

大多数**三星、LG、索尼 BRAVIA、松下 (VIERA 固件)、飞利浦和海信**的电视都内置了 DLNA，可以立即使用。**PlayStation 和 Xbox 主机以及大多数 AV 功放**也可以。

有几个平台把它省掉了：**Roku 电视、Amazon Fire TV、Vizio SmartCast，以及没有厂商媒体应用的原生 Google TV**。如果你的电视是这几种之一，找不到你的设备，通常就是这个原因。在那些电视上，安装一个像 VLC 或 Kodi 这样的 DLNA 播放器应用，或者改用 [WebDAV 设置指南](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) 通过网页浏览器访问你的文件。

有些品牌即便移除了官方的 DLNA 标志，DLNA 仍然可用，所以如果看起来缺失，就去找一找上面提到的某个媒体播放器名称。

## 在 Windows、Mac 和 Linux 的 VLC 或 Kodi 中播放

VLC 和 Kodi 都是免费的，在每一个桌面系统上都能运行，并且很好地支持 DLNA。它们是在电脑上打开 Everdisk 媒体库的可靠方式。

**VLC (Windows、Mac、Linux)：**

1. 打开 VLC。
2. 显示播放列表 (在 Windows 和 Linux 上按 **Ctrl+L**，在 Mac 上从「显示」菜单打开**播放列表**)。
3. 在侧边栏中，展开「本地网络」下的 **Universal Plug'n'Play**。
4. 你的设备会出现在列表里。点进去挑一个文件。

**Kodi (Windows、Mac、Linux)：**

1. 进入**视频**、**音乐**或**图片**，然后是**文件**，再点**添加源** (或**浏览**)。
2. 选择 **UPnP devices**。
3. 选中你的设备并浏览你的媒体库。

在 Windows 上，你也可以打开 **Windows Media Player**，在侧边栏中展开 **Other Libraries**，你的设备就会显示在那里。

## 在 Android 上播放

Android 手机和平板没有系统级的 DLNA 浏览器，所以要用一个应用：

- **VLC for Android**：打开侧边菜单，点击 **Local Network**，你的设备就会出现在 UPnP 服务器下。
- **BubbleUPnP** 或类似的 UPnP 应用：你的设备会显示在服务器列表中，这些应用还能把播放推送到电视上。

## 在另一部 iPhone 或 iPad 上播放

两台设备，一个媒体库。比如照片在你的 iPhone 上，而你想在 iPad 上观看它们。

- 最简单的方法是在第二台设备上用 Everdisk 自己的**设备**标签页。它既能当 DLNA 客户端，也能当服务器。在 iPad 上打开 Everdisk，进入**设备**，你的 iPhone 就会出现在**可用设备**下。点击它即可浏览和播放。
- 任何 iOS 上的 DLNA 播放器应用也可以，比如 VLC 或某个 UPnP 浏览器。打开它的本地网络视图并选中你的 iPhone。

## 在游戏主机上播放

- **PlayStation 5 和 4**：打开 **Media** 应用 (媒体库)，你的设备就会作为一台可浏览的媒体服务器显示出来。
- **Xbox**：使用一个支持 DLNA 的媒体播放器应用，然后从服务器列表中选中你的设备。

## 如果你的设备没有出现在列表里

有些播放器允许你通过地址添加媒体服务器，而不用等它被自动发现。在 Everdisk 的**共享**界面上，DLNA 卡片会显示一个以 `/device-desc.xml` 结尾的设备描述地址。把那个地址输入到播放器的添加服务器字段里。

如果还是不显示，检查三件事：两台设备是否在同一个 Wi-Fi 上 (不是那种会阻止设备间互访的访客网络)、Everdisk 是否已打开且共享已开始，以及**电视与媒体中心**在设置中是否已开启。

## 如果视频无法播放

DLNA 会原样把文件交给电视，而电视得能解码它。如果某段视频拒绝播放，很可能是它的格式不被那台电视支持。有两个办法：

- 依次打开**设置** → **共享** → **视频**，并调低**质量**。Everdisk 会在流式播放时把视频转换成更兼容的格式。(转换是 Premium 功能。)
- 或者用 Everdisk 的浏览器链接在网页浏览器中打开同一个文件，它对格式更宽容。

## 人们在生活中怎么用它

- **家庭电影夜。** 用手机拍的视频在客厅电视上播放，无需数据线或 Apple TV。
- **大屏上的假期照片。** 在电视上打开你的照片库，和满屋子的人一起滑动浏览这趟旅程。
- **聚会上的背景音乐。** 让一台 DLNA 音箱或 AV 功放对准你的音乐库，任它一直播放。
- **在酒店电视上观看**，只要电视带有媒体播放器，且两台设备都连上了房间的 Wi-Fi。

## 几点小提示

- 流式播放时让 Everdisk 保持打开。如果你把手机锁屏很久，iOS 可能会暂停应用，播放就会停止。
- 长时间看电影时给手机接上电源。
- 为了最快的流媒体速度，请在设置中把**格式**和**质量**保持为**原始**，只在某台特定电视处理某个文件吃力时才调低它们。
- DLNA 只用于流式播放。电视那端的任何人都无法更改或删除你的文件。若要双向传输文件，请改用 [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)、[WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) 或 [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) 服务器。

## 常见问题

{{% details title="DLNA 和 UPnP 有什么区别？" closed="true" %}}
它们关系密切。UPnP 是底层的网络标准，而 DLNA 是构建在它之上的媒体规范，电视和播放器用它来共享和播放照片、视频和音乐。在日常使用中，这两个词可以互换。当你在 Everdisk 中开启电视与媒体中心时，你的设备就成了一台任何 DLNA 客户端都能浏览的 DLNA/UPnP 媒体服务器。
{{% /details %}}

{{% details title="我需要在电视上安装什么吗？" closed="true" %}}
不需要。如果你的电视支持 DLNA，它已经有一个能在 Wi-Fi 上找到你设备的媒体播放器了。你只需在存放内容的那部 iPhone 或 iPad 上安装 Everdisk。如果你的电视不支持 DLNA，就在与它相连的设备上安装一个像 VLC 或 Kodi 这样的播放器。
{{% /details %}}

{{% details title="为什么我的 iPhone 没有出现在电视上？" closed="true" %}}
检查两台设备是否在同一个 Wi-Fi 网络上。访客网络以及某些办公室或酒店网络会阻止设备之间互相发现，这会中断 DLNA。然后确认 Everdisk 已打开且共享已开始，并且电视与媒体中心在设置、共享、连接中已开启。如果电视还是找不到它，就用以 /device-desc.xml 结尾的设备描述地址手动添加服务器。
{{% /details %}}

{{% details title="DLNA 流媒体需要密码吗？" closed="true" %}}
不需要。DLNA 开启时始终对同一 Wi-Fi 上的任何人开放，这就是为什么电视那端没有登录。在你信任的家庭网络上这没问题。在你不信任的网络上，用完后关掉电视与媒体中心，或改用带加密的 SMB 服务器。
{{% /details %}}

{{% details title="我能流式播放到 Chromecast 或 Roku 吗？" closed="true" %}}
Chromecast 和 Roku 开箱即用时并不充当 DLNA 播放器，所以它们不会直接找到你的设备。变通办法是安装一个能投屏的 DLNA 应用，比如手机上的 VLC 或 BubbleUPnP，然后从那里把播放推送到 Chromecast 或 Roku。在大多数其他智能电视上，DLNA 无需这些操作即可工作。
{{% /details %}}

{{% details title="视频播放时没有声音或无法打开，我该怎么办？" closed="true" %}}
那是一种电视无法解码的格式。在 Everdisk 中打开设置、共享、视频，调低质量，让应用在流式播放时把视频转换成更兼容的格式。你也可以通过浏览器链接打开同一个文件，它能处理更多格式。
{{% /details %}}

{{% details title="我能只播放音乐，而不只是视频吗？" closed="true" %}}
可以。开启允许访问整个音乐资料库，或添加特定的歌曲，然后开始共享。你的歌曲会出现在任何 DLNA 音箱、AV 功放或电视上，并附有专辑封面和曲目详情。音乐始终以原始质量共享。
{{% /details %}}

{{% details title="观看时应用必须一直开着吗？" closed="true" %}}
是的。你的 iPhone 正充当服务器，而 iOS 会暂停被长时间完全推入后台的应用。流式播放时让 Everdisk 保持在屏幕上，长时间观看时接上电源。
{{% /details %}}

{{% details title="如何从一部 iPhone 流式播放到另一部 iPad？" closed="true" %}}
在 iPhone 上开始共享，然后在 iPad 上打开 Everdisk 并进入设备标签页。iPhone 会作为一台媒体服务器出现在可用设备下。点击它即可浏览和播放。Everdisk 既能当 DLNA 客户端也能当服务器，所以你不需要另一个应用。
{{% /details %}}

{{% details title="Everdisk 免费吗？" closed="true" %}}
是的，Everdisk 可免费下载，且已包含 DLNA 媒体服务器。可选的一次性 Premium Lifetime 购买会增加一些额外功能，比如为旧电视做照片和视频转换、自定义端口等等。你无需付费就能设置和使用 DLNA 流媒体。
{{% /details %}}

想试试吗？[从 App Store 下载 Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)，几分钟内就能把第一张专辑流式播放到电视上。有疑问或反馈？发邮件给我们：**support@everappz.com**。
