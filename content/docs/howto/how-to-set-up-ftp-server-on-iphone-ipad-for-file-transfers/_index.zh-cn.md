---
title: "如何在 iPhone 和 iPad 上搭建 FTP 服务器进行文件传输"
description: "用 Everdisk 把你的 iPhone 或 iPad 变成 FTP 服务器，通过 Wi-Fi 从 Mac、Windows PC、Linux、Android、像 FileZilla 这样的 FTP 应用，或另一部 iPhone 传输文件。完整设置、ftp 地址和端口、访客访问，以及每种设备的分步连接教程。"
date: 2026-09-19
tags: ["everdisk", "ftp", "文件传输", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["iPhone FTP 服务器", "iPad FTP 服务器", "如何在 iPhone 上搭建 FTP", "iphone ftp 服务器应用", "把 FileZilla 连接到 iPhone", "Cyberduck iPhone FTP", "通过 FTP 传输 iPhone 文件", "ftp iphone 到电脑", "ftp iphone 到 iphone", "从 Windows 连接到 iPhone FTP", "iphone ftp 地址端口", "匿名 ftp iphone", "iphone 共享文件 ftp", "iphone ftp 用于相机 nas"]
readingTime: 9
---

{{< author-byline >}}

FTP 是文件传输领域的老牌可靠工具。它已经存在了几十年，而这恰恰是它如此有用的原因：几乎任何能与服务器通信的东西都懂它。相机、智能电视、路由器、网络硬盘、自动化工具，以及每一个桌面 FTP 应用都支持 FTP。有了 [Everdisk](/products/everdisk)，你可以在 iPhone 或 iPad 上运行一个 FTP 服务器，这样手机就成了那些设备和应用可以连接并搬运文件的地方。

当其他选项都不合适时就选 FTP，比如面对一台较旧的设备，或一个只知道通过 FTP 连接的应用。本指南涵盖设置，以及如何从 Mac、Windows、一个 FTP 应用、Linux、Android 和第二部 iPhone 连接。

## 你需要什么

- 一部安装了 [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) 的 iPhone 或 iPad。
- 一台处于**同一 Wi-Fi 网络**的电脑、应用或设备。
- 你想共享的文件，放在 Everdisk 的 Documents 文件夹里，或放在你添加的文件夹里。

## 在 Everdisk 中设置 FTP 服务器

### 第 1 步：选择要共享的内容并设置访问权限

打开 Everdisk，进入**共享**标签页，点击**分享什么**。Documents 文件夹默认会被共享。用**添加文件夹**和**添加文件**添加更多内容。

依次打开**设置** → **共享** → **访问**。如果你想让别人上传、重命名和删除，就开启**文件编辑**；若只想允许下载则关闭它。如果你想要登录，就设置一个**登录名**和**密码**，或留空以便任何人都能以访客身份连接。

### 第 2 步：开启 FTP 服务器

依次进入**设置** → **共享** → **连接**，并开启**其他应用和设备**。那就是 FTP 服务器 (它带有 FTP 标签)。

### 第 3 步：开始共享并记下地址

回到**共享**标签页，点击**开始**。**如何连接**部分会显示 FTP 地址。它看起来像这样：

```
ftp://192.168.1.20:2121
```

冒号后面的数字是**端口**，默认是 **2121**。第一部分是你 iPhone 在 Wi-Fi 上的地址，所以你的会不一样。有设备连接时让 Everdisk 保持在屏幕上打开。

## 从 Mac 连接

1. 打开 **Finder**，选择**前往**，然后是**连接服务器** (或按 **Command 和 K**)。
2. 输入 Everdisk 中显示的 FTP 地址，例如 `ftp://192.168.1.20:2121`。
3. 点击**连接**，然后选择**访客**或输入你的**登录名**和**密码**。

Finder 会挂载这个 FTP 共享，让你浏览并把文件复制到你的 Mac 上。请注意，Finder 是以只读方式打开 FTP 的。当你想从 Mac 上传时，请按下文所述使用一个 FTP 应用。

## 从 Windows 连接

1. 打开**文件资源管理器**，点击顶部的地址栏。
2. 键入 Everdisk 中的 FTP 地址，例如 `ftp://192.168.1.20:2121`，然后按**回车**。
3. 如果你设置了登录，就输入你的**登录名**和**密码**，或以访客身份继续。

共享的文件会出现在窗口中，你可以把它们复制到你的 PC 上。

## 用 FTP 应用连接 (FileZilla、Cyberduck)

若要上传和完全掌控，FTP 应用是最好的工具。**FileZilla** 和 **Cyberduck** 都是免费的，并且在 Windows、Mac 和 Linux 上运行。

1. 打开应用并创建一个新连接。
2. 把**主机**设为你 iPhone 的 Wi-Fi 地址，把**端口**设为 **2121**。
3. 对于登录，输入你的**登录名**和**密码**，或者如果你没有设置就选择**匿名**。
4. 连接，然后双向拖放文件 (上传需要开启文件编辑)。

## 从 Linux 连接

1. 打开你的文件管理器，选择 **Connect to Server** 或 **Other Locations**。
2. 输入地址，例如 `ftp://192.168.1.20:2121`。
3. 以访客身份或用你的登录名连接。

你也可以在终端里使用任何 Linux FTP 客户端，把它指向相同的主机和端口 2121。

## 从 Android 连接

Android 没有系统级的 FTP 浏览器，所以要用一个应用：

1. 安装一个 FTP 客户端，比如 **AndFTP**、**FTPCafe**，或一个支持 FTP 的文件管理器，比如 **Solid Explorer**。
2. 用主机、**端口 2121** 以及你的登录名或匿名添加一个连接。
3. 浏览并传输。

## 从另一部 iPhone 或 iPad 连接

iOS 的「文件」应用不包含 FTP 客户端，所以请在第二台设备上使用下面这两种方式之一：

- **Everdisk 自己的设备标签页。** 打开 Everdisk，进入**设备**，点击**新建连接**，选择 **FTP**，然后输入地址，例如 `ftp://192.168.1.20:2121`。这是最简单的方式。
- **一个专门的 FTP 应用** for iOS，使用相同的主机、端口 2121 和登录名。

## 连接其他设备：相机、电视、路由器和 NAS

这正是 FTP 大显身手的地方。许多设备都有内置的 FTP 客户端，可以发送或获取文件：

- **通过 FTP 上传照片的相机**可以把照片直接发到你的 iPhone。
- **支持 FTP 的智能电视、路由器、NAS 盒子和自动化工具**都能以同样的方式连接。

用 Everdisk 中显示的地址，把它们指向你 iPhone 的 Wi-Fi 地址、端口 **2121** 和你的登录名 (或匿名)。

## 只读还是读写

**设置**、**共享**、**访问**中的**文件编辑**开关控制这一点。开启让别人可以上传、重命名和删除。关闭意味着他们只能下载。当你把文件分发出去、又不希望手机上的任何东西被更改时，就选只读。

## 人们在生活中怎么用它

- **把 FileZilla 连接到你的 iPhone**，一次性把一批文件推到手机上。
- **让一个只支持 FTP 的旧应用或旧设备**在其他方式都无法连接时访问你的文件。
- **接收来自相机的照片**，那台相机通过 FTP 上传。
- **在 iPhone 和 iPad 之间移动文件**，在接收设备上使用 Everdisk 的设备标签页。

## 几点小提示

- 有设备连接时让 Everdisk 保持打开，因为 iOS 会在一段时间后暂停后台应用。
- 若要从 Mac 上传，请使用 FileZilla 或 Cyberduck 而不是 Finder，因为 Finder 是以只读方式打开 FTP 的。
- 为了最广泛的兼容性，把登录名留空，然后以匿名身份连接，大多数 FTP 客户端都提供这一选项。
- FTP 不会加密其流量。在你不信任的网络上，请改用[带加密的 SMB 服务器](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)。

## 常见问题

{{% details title="我 iPhone 的 FTP 地址和端口是什么？" closed="true" %}}
在你开始共享后，Everdisk 会在共享界面上显示地址。它看起来像 ftp://192.168.1.20:2121。其中 2121 是 Everdisk 用于 FTP 的端口，第一部分是你 iPhone 在 Wi-Fi 上的地址，所以你的会不一样。
{{% /details %}}

{{% details title="如何把 FileZilla 或 Cyberduck 连接到我的 iPhone？" closed="true" %}}
打开应用并创建一个新连接。把主机设为你 iPhone 的 Wi-Fi 地址，把端口设为 2121。输入你的登录名和密码，或者如果你没有在 Everdisk 中设置就选择匿名。连接后，当文件编辑开启时你可以双向拖放文件。
{{% /details %}}

{{% details title="我能从 Windows 连接到我 iPhone 的 FTP 吗？" closed="true" %}}
可以。打开文件资源管理器，点击地址栏，键入 Everdisk 中的 FTP 地址 (例如 ftp://192.168.1.20:2121)，然后按回车。如果你设置了登录就输入它，或以访客身份继续。若要上传和更多控制，请改用像 FileZilla 这样的 FTP 应用。
{{% /details %}}

{{% details title="FTP 需要登录吗？" closed="true" %}}
不需要，登录是可选的。在设置、共享、访问中把登录名和密码留空，然后以匿名身份连接，大多数 FTP 客户端都提供这一选项。如果你想让连接方先登录，就设置一个登录名。
{{% /details %}}

{{% details title="为什么我通过 FTP 只能下载而不能上传？" closed="true" %}}
常见有两个原因。第一，设置、共享、访问中的文件编辑开关必须开启，才能允许上传、重命名和删除。第二，Mac Finder 是以只读方式打开 FTP 的，所以当你想上传时，请使用像 FileZilla 或 Cyberduck 这样的 FTP 应用。
{{% /details %}}

{{% details title="我能在两部 iPhone 之间使用 FTP 吗？" closed="true" %}}
可以。在第一部 iPhone 上启动 FTP 服务器。在第二部上，打开 Everdisk，进入设备标签页，点击新建连接，选择 FTP，然后输入第一部手机上显示的地址。一个专门 for iOS 的 FTP 应用也可以，因为 iOS 的「文件」应用不包含 FTP 客户端。
{{% /details %}}

{{% details title="FTP 安全吗？" closed="true" %}}
普通 FTP 不会加密其流量，所以请把它当作用于你信任的网络 (比如你的家庭 Wi-Fi) 的工具。在你无法掌控的网络上，请使用开启了要求 SMB 加密的 SMB 服务器，它会保护每一次传输。
{{% /details %}}

{{% details title="哪些设备可以通过 FTP 连接？" closed="true" %}}
几乎任何带有 FTP 客户端的东西。这包括 Mac、Windows 和 Linux 电脑，像 FileZilla 和 Cyberduck 这样的 FTP 应用，Android 文件管理器，以及相机、智能电视、路由器、NAS 盒子和自动化工具等硬件。这种广泛的适用范围正是选择 FTP 的主要原因。
{{% /details %}}

{{% details title="为什么我的 FTP 连接断了？" closed="true" %}}
你的 iPhone 是服务器，而 iOS 会暂停在后台停留太久的应用。有设备连接时让 Everdisk 保持在屏幕上打开，长时间传输时接上电源。也要确保两台设备仍在同一个 Wi-Fi 上。
{{% /details %}}

{{% details title="Everdisk 免费吗？" closed="true" %}}
是的，Everdisk 可免费下载，且已包含 FTP 服务器。可选的一次性 Premium 购买会增加一些额外功能，比如自定义端口以及照片和视频转换。你无需付费就能设置 FTP 并传输文件。
{{% /details %}}

想试试吗？[从 App Store 下载 Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)，几分钟内就能连接你的第一个 FTP 客户端。有疑问或反馈？发邮件给我们：**support@everappz.com**。
