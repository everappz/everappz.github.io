---
title: "如何在 iPhone 和 iPad 上搭建 WebDAV 服务器以访问和共享文件"
description: "用 Everdisk 把你的 iPhone 或 iPad 变成 WebDAV 服务器，通过 Wi-Fi 在 Mac Finder、Windows 文件资源管理器、Linux、Android 或另一部 iPhone 上把它挂载为网络硬盘。完整设置、WebDAV 地址和端口，以及每种设备的分步连接教程。"
date: 2026-09-19
tags: ["everdisk", "webdav", "网络硬盘", "文件共享", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["iPhone WebDAV 服务器", "iPad WebDAV 服务器", "如何在 iPhone 上搭建 WebDAV", "把 iPhone 挂载为网络硬盘", "在 Mac Finder 连接 iPhone WebDAV", "iPhone WebDAV Windows 文件资源管理器", "iphone 网络硬盘 Windows", "Linux iPhone WebDAV", "从电脑访问 iPhone 文件", "iphone 到 iphone webdav", "iPhone 共享文件 WebDAV", "把 iphone 映射为网络硬盘", "通过 webdav 传输 iphone 文件", "iphone webdav 地址端口"]
readingTime: 9
---

{{< author-byline >}}

WebDAV 把一个文件夹变成网络硬盘，让电脑能在其常规的文件管理器中打开它。它运行在与你浏览器所用相同的网络协议之上，这正是它能在 Mac、Windows 和 Linux 之间通行无阻、无需特殊驱动的原因。有了 [Everdisk](/products/everdisk)，你可以在 iPhone 或 iPad 上运行一个 WebDAV 服务器，这样手机就会作为一块硬盘出现，让你几乎从任何电脑浏览、从中复制、以及往里复制。

当涉及 Windows 时，WebDAV 是最佳选择，因为 Windows 文件资源管理器能干净利落地连接到它。本指南涵盖设置，以及如何从 Mac、Windows、Linux、Android 和第二部 iPhone 连接。

## 你需要什么

- 一部安装了 [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) 的 iPhone 或 iPad。
- 一台处于**同一 Wi-Fi 网络**的电脑或另一台设备。
- 你想共享的文件，放在 Everdisk 的 Documents 文件夹里，或放在你添加的文件夹里。

## 在 Everdisk 中设置 WebDAV 服务器

### 第 1 步：选择要共享的内容并设置访问权限

打开 Everdisk，进入**共享**标签页，点击**分享什么**。Documents 文件夹默认会被共享。用**添加文件夹**和**添加文件**添加更多内容。

依次打开**设置** → **共享** → **访问**。如果你想让已连接的电脑把文件复制到你的手机上并重命名或删除，就开启**文件编辑**；若想要只读硬盘则关闭它。如果你想要登录，就在这里设置**登录名**和**密码**，或留空以允许访客访问。

### 第 2 步：开启 WebDAV 服务器

依次进入**设置** → **共享** → **连接**，并开启**电脑**。那就是 WebDAV 服务器 (它带有 WebDAV 标签)。

### 第 3 步：开始共享并记下地址

回到**共享**标签页，点击**开始**。**如何连接**部分会显示 WebDAV 地址。它看起来像这样：

```
http://192.168.1.20:8080
```

冒号后面的数字是**端口**，默认是 **8080**。第一部分是你 iPhone 在 Wi-Fi 上的地址，所以你的会不一样。有设备连接时让 Everdisk 保持在屏幕上打开。

## 从 Mac 连接

1. 打开 **Finder**，选择**前往**，然后是**连接服务器** (或按 **Command 和 K**)。
2. 输入 Everdisk 中显示的 WebDAV 地址，例如 `http://192.168.1.20:8080`。
3. 点击**连接**，然后选择**访客**或输入你的**登录名**和**密码**。

你的 iPhone 会在一个 Finder 窗口中打开，表现得像一个普通文件夹。若文件编辑已开启，可双向复制文件。

## 从 Windows 连接

Windows 有内置的 WebDAV 客户端，所以这能从文件资源管理器工作。

1. 打开**文件资源管理器**，在侧边栏右键点击**此电脑**，选择**添加网络位置** (你也可以用**映射网络驱动器**)。
2. 在要求输入地址时，键入 Everdisk 中相同的 WebDAV 地址，例如 `http://192.168.1.20:8080`，然后点击**下一步**。
3. 如果你设置了登录，就输入你的**登录名**和**密码**。

该设备随后会作为一个网络位置出现在「此电脑」下，你可以打开它并从中复制文件。如果 Windows 第一次拒绝连接，请确保 **WebClient** 服务正在运行 (在开始菜单中搜索「服务」，找到 WebClient，将其设为启动)，然后重试。

## 从 Linux 连接

1. 打开你的文件管理器，选择 **Connect to Server** 或 **Other Locations**。
2. 输入带 WebDAV 前缀的地址，例如 `dav://192.168.1.20:8080` (仅在你设置了 TLS 时才用 `davs://`)。
3. 以访客身份连接，或输入你的登录名。

## 从 Android 连接

Android 没有系统级的 WebDAV 浏览器，所以要用一个支持它的文件管理器：

1. 安装一个应用，比如 **Solid Explorer** 或 **CX File Explorer**。
2. 添加一个新的 **WebDAV** 连接。
3. 输入主机和**端口 8080**，选择 `http` 方案，如果你设置了登录就把它加上。

## 从另一部 iPhone 或 iPad 连接

iOS 的「文件」应用不包含 WebDAV 客户端，所以请用下面这两种方式之一：

- **Everdisk 自己的设备标签页。** 在第二台设备上，打开 Everdisk，进入**设备**，点击**新建连接**，选择 **WebDAV**，然后输入地址，例如 `http://192.168.1.20:8080`。这是最简单的方式，不需要任何额外的东西。
- **一个 WebDAV 应用**，比如 Documents by Readdle，它可以用相同的地址和登录名添加一个 WebDAV 连接。

## 更想要一个快速链接而不是硬盘？

如果你只需要快速抓取一个文件，完全不想挂载硬盘，就在设置、共享、连接中开启**浏览器**连接。Everdisk 随后会给你一个网址，你可以在任何设备的任意浏览器中打开它来浏览和下载你的文件。这是把文件递给 Windows PC、Chromebook 或朋友手机的最快方式。

## 只读还是读写

**设置**、**共享**、**访问**中的**文件编辑**开关决定这一点。开启意味着已连接的电脑可以上传、重命名和删除。关闭意味着硬盘为只读，其他人可以查看并复制你的文件，但不能更改它们。

## 人们在生活中怎么用它

- **从 Windows PC 把文件复制到你的 iPhone 上**，把它映射为一个网络位置，然后把文件拖过去。
- **用你已经熟悉的文件管理器把照片和文档卸载到笔记本上**，无需数据线也无需 iTunes。
- **就地编辑文档**，从 Mac 直接从手机打开它并保存回去。
- **在 iPhone 和 iPad 之间移动一个文件夹**，在接收设备上使用 Everdisk 的设备标签页。

## 几点小提示

- 有设备连接时让 Everdisk 保持打开。长时间锁屏可能会暂停应用。
- 在 Windows 上，如果连接失败，就启动 WebClient 服务并重试地址。
- WebDAV 和 SMB 都会挂载为网络硬盘。涉及 Windows 时用 WebDAV，想要 Finder 速度和加密时用 [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)。
- 为了最快的传输，请在设置中把照片和视频质量保持为原始。

## 常见问题

{{% details title="我 iPhone 的 WebDAV 地址和端口是什么？" closed="true" %}}
在你开始共享后，Everdisk 会在共享界面上显示地址。它看起来像 http://192.168.1.20:8080。其中 8080 是 Everdisk 用于 WebDAV 的端口，第一部分是你 iPhone 在 Wi-Fi 上的地址，所以你的会不一样。
{{% /details %}}

{{% details title="如何从 Windows 连接到我 iPhone 的 WebDAV？" closed="true" %}}
打开文件资源管理器，右键点击此电脑，选择添加网络位置或映射网络驱动器。输入 Everdisk 中的 WebDAV 地址，例如 http://192.168.1.20:8080，如果你设置了登录就输入它。如果 Windows 无法连接，请确保 WebClient 服务正在运行 (搜索「服务」，找到 WebClient，启动它)，然后重试。
{{% /details %}}

{{% details title="我能在两部 iPhone 之间使用 WebDAV 吗？" closed="true" %}}
可以，但 iOS 的「文件」应用没有 WebDAV 客户端，所以请在第二台设备上使用 Everdisk。打开设备标签页，点击新建连接，选择 WebDAV，然后输入第一部手机上显示的地址。像 Documents by Readdle 这样的 WebDAV 应用也可以。
{{% /details %}}

{{% details title="WebDAV 需要密码吗？" closed="true" %}}
不需要，登录是可选的。在设置、共享、访问中把登录名和密码留空即可实现访客访问，或者如果你想让连接方登录就设置它们。
{{% /details %}}

{{% details title="别人能通过 WebDAV 更改我的文件吗？" closed="true" %}}
只有在你允许的情况下才行。设置、共享、访问中的文件编辑开关控制这一点。开启让已连接的设备可以上传、重命名和删除。关闭让硬盘变为只读，其他人可以查看和复制，但不能更改任何东西。
{{% /details %}}

{{% details title="WebDAV 还是 SMB，有什么区别？" closed="true" %}}
两者都会把你的 iPhone 挂载为网络硬盘。WebDAV 运行在网络协议之上，能从 Windows 文件资源管理器干净地连接，这是它的主要优势。SMB 是 Mac、Linux 和 NAS 设备上的原生文件共享方式，在 Mac 上通常更快，而且是 Everdisk 中唯一能给传输加密的连接。Everdisk 可以同时运行两者。
{{% /details %}}

{{% details title="为什么我的 WebDAV 硬盘会断开？" closed="true" %}}
你的 iPhone 是服务器，而 iOS 会暂停在后台停留太久的应用。有设备连接时让 Everdisk 保持在屏幕上打开，长时间传输时接上电源。也要确认两台设备仍在同一个 Wi-Fi 上。
{{% /details %}}

{{% details title="没有 Wi-Fi 我能通过 WebDAV 连接吗？" closed="true" %}}
可以，如果你用数据线把 iPhone 插到 Mac 上。Everdisk 随后会显示一个额外的数据线连接地址，相连的 Mac 可以在 Finder 中打开它，这即使完全没有 Wi-Fi 也能用。通过数据线，只有那台 Mac 能访问到设备。
{{% /details %}}

{{% details title="Everdisk 免费吗？" closed="true" %}}
是的，Everdisk 可免费下载，且已包含 WebDAV 服务器。可选的一次性 Premium 购买会增加一些额外功能，比如自定义端口以及照片和视频转换。你无需付费就能设置 WebDAV 并共享文件。
{{% /details %}}

想试试吗？[从 App Store 下载 Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)，几分钟内就能把你的 iPhone 挂载为一块硬盘。有疑问或反馈？发邮件给我们：**support@everappz.com**。
