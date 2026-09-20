---
title: "如何在 iPhone 和 iPad 上搭建 SMB 服务器进行文件共享"
description: "用 Everdisk 把你的 iPhone 或 iPad 变成 SMB 文件服务器，通过 Wi-Fi 从 Mac、另一部 iPhone、Linux 或 Android 像访问网络硬盘一样打开它。完整设置、smb 地址和端口、可选的 SMB3 加密，以及每种设备的分步连接教程。"
date: 2026-09-19
tags: ["everdisk", "smb", "文件共享", "网络硬盘", "iphone", "ipad", "mac", "finder", "加密", "wifi"]
keywords: ["iPhone SMB 服务器", "iPad SMB 服务器", "如何在 iPhone 上搭建 SMB", "iPhone SMB 共享", "在 Mac Finder 连接 iPhone SMB", "iphone 到 iphone smb", "iOS 文件应用连接 SMB 服务器", "iPhone 共享文件 SMB", "iphone 网络硬盘 Finder", "iOS SMB3 加密", "iPhone Android smb 共享", "从 Linux 连接 SMB", "iphone 当作网络硬盘", "通过 wifi 在 iphone 之间共享文件", "把 iphone 映射为网络硬盘"]
readingTime: 10
---

{{< author-byline >}}

SMB 是内置于 macOS、Windows 和 Linux，以及几乎每一台网络硬盘 (NAS) 中的文件共享方式。当你连接到另一台电脑上的共享文件夹，它像一块普通硬盘一样在 Finder 或文件资源管理器中打开时，那就是 SMB 在起作用。有了 [Everdisk](/products/everdisk)，你可以在 iPhone 或 iPad 上放一个 SMB 共享，这样手机本身就会作为一块网络硬盘出现，供其他设备浏览、从中复制、以及往里复制。

当你想让 iPhone 表现得像一块真正的硬盘，而不是一个网页时，就该选这个选项。它速度快，双向拖放皆可，而且它是 Everdisk 中唯一能给每一次传输加密的连接类型。本指南涵盖设置，以及如何从 Mac、另一部 iPhone 或 iPad、Linux、Android 和 Windows 连接。

## 你需要什么

- 一部安装了 [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) 的 iPhone 或 iPad。
- 另一台处于**同一 Wi-Fi 网络**的设备。
- 你想共享的文件，放在 Everdisk 的 Documents 文件夹里，或放在你添加的文件夹里。

## 在 Everdisk 中设置 SMB 服务器

### 第 1 步：挑选要共享的内容以及谁能写入

打开 Everdisk，进入**共享**标签页，点击**分享什么**。Documents 文件夹默认会被共享。用**添加文件夹**和**添加文件**添加更多内容，如果你也想让照片或音乐库可用，就把它们开启。

决定其他设备是只能读取你的文件，还是也能更改它们。依次打开**设置** → **共享** → **访问**，并设置**文件编辑**。开启后，已连接的设备可以把文件复制到你的手机上，并重命名或删除。关闭后，共享为只读。

如果你想要登录，就在同一个访问界面上设置**登录名**和**密码**。两者都留空则允许访客访问。

### 第 2 步：开启 SMB 服务器

依次进入**设置** → **共享** → **连接**，并开启**电脑（高级）**。那就是 SMB 服务器 (它带有 SMB 标签)。

### 第 3 步：开始共享并记下地址

回到**共享**标签页，点击**开始**。现在**如何连接**部分会显示 SMB 地址。它看起来像这样：

```
smb://192.168.1.20:4455/Share
```

关于那个地址，有三件事要知道：

- 冒号后面的数字是**端口**。Everdisk 默认使用 **4455**。
- 共享名为 **Share**。
- 第一部分是你 iPhone 在 Wi-Fi 上的地址，所以在你的网络上它会不一样。

有设备连接时让 Everdisk 保持打开，因为 iOS 会暂停在后台停留太久的应用。

## 从 Mac 连接

这是最顺畅的情况，因为 macOS 原生支持 SMB。

最快的方式：打开 **Finder**，在侧边栏的**位置**或**网络**下查看。Everdisk 会在 Wi-Fi 上通告自己，所以你的 iPhone 常常会自行出现在那里。点击它，然后点击**连接身份**并选择**访客**，或输入你的登录名。

手动连接：

1. 在 Finder 中，选择**前往**，然后是**连接服务器** (或按 **Command 和 K**)。
2. 输入 Everdisk 中显示的 SMB 地址，例如 `smb://192.168.1.20:4455/Share`。
3. 点击**连接**，然后选择**访客**或输入你的**登录名**和**密码**。

你的 iPhone 会在一个 Finder 窗口中打开。通过拖放把文件复制进去或取出来，和任何其他硬盘完全一样 (前提是文件编辑已开启)。

## 从另一部 iPhone 或 iPad 连接

iOS 和 iPadOS 可以在内置的**文件**应用中打开 SMB 共享，这让手机到手机的传输干净又快捷。

在第二台设备上：

1. 打开**文件**应用。
2. 点击**更多**按钮 (在 iPhone 上是右上角的三个点)，选择**连接服务器**。
3. 输入 Everdisk 中的 SMB 地址，例如 `smb://192.168.1.20:4455/Share`。
4. 选择**访客**，或**注册用户**并输入你的登录名。
5. 该共享会出现在「文件」的「位置」下。可双向浏览和复制。

你也可以在第二台设备上使用 Everdisk 自己的**设备**标签页，它包含一个 SMB 客户端。打开 Everdisk，进入**设备**，点击**新建连接**，选择 **SMB**，然后输入地址。

## 从 Linux 连接

1. 打开你的文件管理器 (GNOME 上是 Files/Nautilus，KDE 上是 Dolphin)。
2. 选择 **Other Locations** 或 **Connect to Server**。
3. 输入地址，例如 `smb://192.168.1.20:4455/Share`。
4. 以访客身份连接，或输入你的登录名。

在终端里你也可以运行 `smbclient //192.168.1.20/Share -p 4455`，并在提示时输入你的登录名。

## 从 Android 连接

Android 没有系统级的 SMB 浏览器，所以要用一个支持 SMB 的文件管理器：

1. 安装一个应用，比如 **CX File Explorer**、**Solid Explorer** 或 **X-plore File Manager**。
2. 添加一个新的 **SMB** 或 **LAN** 连接。
3. 输入主机 (你 iPhone 的 Wi-Fi 地址)，把**端口设为 4455**，共享名为 **Share**。
4. 以访客身份或用你的登录名连接，然后浏览和复制。

## 从 Windows 连接

Windows 能读取 SMB 共享，但有一个值得先了解的问题。内置的文件资源管理器只能通过标准端口访问 SMB，并且不允许在路径中输入自定义端口，而 Everdisk 使用端口 4455。所以普通的**映射网络驱动器**方式往往无法访问到它。

在 Windows 上你有两个不错的选择：

- 使用一个允许设置自定义端口的文件管理器或 SMB 客户端，把它指向你 iPhone 的地址，端口为 **4455**，共享名为 **Share**。
- 或者改用 Everdisk 的其他服务器从 Windows 连接。[WebDAV 设置](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) 和 [FTP 设置](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) 都能很好地从 Windows 文件资源管理器工作，而浏览器链接在任何浏览器中都能用。

如果你确实想试试映射网络驱动器：打开**文件资源管理器**，右键点击**此电脑**，选择**映射网络驱动器**，并输入 Everdisk 中显示的主机和共享名。如果它无法连接，那就是上面所说的端口限制，请切换到 WebDAV 或 FTP。

## 为不受信任的 Wi-Fi 开启加密

SMB 是 Everdisk 中唯一能给每一次传输加密的连接，这在你无法完全掌控的 Wi-Fi 上很重要，比如咖啡馆或办公室网络。

1. 在**设置**、**共享**、**访问**中，设置一个**登录名**和**密码**。加密连接不能匿名，所以这一步是必需的。
2. 在**设置**、**共享**中，开启**要求 SMB 加密**。
3. 停止并重新开始共享，让更改生效。

这样每一次 SMB 传输都会用 **SMB3 加密 (AES)** 保护。连接的设备需要支持 SMB3，现代 Mac 上的 Finder 和 Windows 10 及更高版本都支持。SMB 加密是一次性 Premium 购买的一部分。

## 只读还是读写

**设置**、**共享**、**访问**中的**文件编辑**开关为每一个服务器 (包括 SMB) 控制这一点。开启后，已连接的设备可以上传、重命名和删除。关闭后，它们只能浏览并从你的手机复制文件。当你把文件交给不希望其更改任何东西的人时，就选只读。

## 人们在生活中怎么用它

- **从 Mac 把一个大文件夹搬到你的 iPhone 上**，只需把它拖进 Finder 窗口，比网页上传更快。
- **把一天拍的照片和视频从手机取到笔记本上**，无需 iTunes 或数据线。
- **在两部 iPhone 之间发送文件**，通过「文件」应用，两端都不用第三个应用。
- **就地处理文件**，在 Mac 上的某个应用中直接从手机打开一个文档并保存回去。

## 几点小提示

- 有设备连接时让 Everdisk 保持打开。长时间锁屏可能会暂停应用并中断连接。
- 如果 Mac 在 Finder 侧边栏看不到手机，就用「连接服务器」和完整的 smb 地址手动连接。
- 为了大批量传输的最佳速度，请在设置中把照片和视频质量保持为原始。
- 在不受信任的网络上，开启要求 SMB 加密，并在工作时关掉其他服务器。

## 常见问题

{{% details title="我 iPhone 的 SMB 地址和端口是什么？" closed="true" %}}
在你开始共享后，Everdisk 会在共享界面上显示地址。它看起来像 smb://192.168.1.20:4455/Share。其中 4455 是 Everdisk 用于 SMB 的端口，Share 是共享文件夹的名称。第一部分是你 iPhone 在 Wi-Fi 上的地址，所以你的会不一样。
{{% /details %}}

{{% details title="我能从 Windows 连接到我 iPhone 的 SMB 共享吗？" closed="true" %}}
Windows 文件资源管理器只能通过标准端口连接 SMB，并且不接受在路径中使用自定义端口，而 Everdisk 使用端口 4455。所以普通的映射网络驱动器方式往往无法访问到它。请使用一个允许设置自定义端口的文件管理器，或改用 WebDAV、FTP 或浏览器链接从 Windows 连接。所有这些都能从 Windows 使用，且没有端口方面的麻烦。
{{% /details %}}

{{% details title="如何用 SMB 在两部 iPhone 之间共享文件？" closed="true" %}}
在第一部 iPhone 上用 Everdisk 启动 SMB 服务器。在第二部 iPhone 上，打开「文件」应用，点击「更多」按钮，选择「连接服务器」，然后输入 Everdisk 中显示的 smb 地址 (例如 smb://192.168.1.20:4455/Share)。以访客身份或用你的登录名连接，共享就会出现在「文件」中。你也可以在第二部手机上使用 Everdisk 自己的设备标签页。
{{% /details %}}

{{% details title="我的 iPhone 会自动出现在 Mac Finder 侧边栏里吗？" closed="true" %}}
通常会。Everdisk 会在你的 Wi-Fi 上通告 SMB 共享，所以你的 iPhone 常常会出现在 Finder 侧边栏的「位置」或「网络」下。点击它并选择「连接身份」，然后是「访客」或你的登录名。如果它没有出现，就用「前往」、「连接服务器」和完整的 smb 地址手动连接。
{{% /details %}}

{{% details title="使用 SMB 需要密码吗？" closed="true" %}}
不需要，登录是可选的。在设置、共享、访问中把登录名和密码留空即可允许访客访问。如果你想让连接方登录，就设置它们。只有当你开启要求 SMB 加密时才需要登录名和密码，因为加密连接不能匿名。
{{% /details %}}

{{% details title="SMB 连接是加密的吗？" closed="true" %}}
可以是。SMB 是 Everdisk 中唯一支持加密的连接。设置登录名和密码，然后在设置、共享中开启要求 SMB 加密。这样每一次传输都会用 SMB3 (AES) 保护。对方设备需要支持 SMB3，现代 Mac 和 Windows 10 及更高版本都支持。加密是一项 Premium 功能。
{{% /details %}}

{{% details title="别人能通过 SMB 更改或删除我的文件吗？" closed="true" %}}
只有在你允许的情况下才行。设置、共享、访问中的文件编辑开关控制这一点。开启后，已连接的设备可以上传、重命名和删除。关闭后，共享为只读，其他人可以浏览并从你的手机复制文件，但不能更改任何东西。
{{% /details %}}

{{% details title="为什么我的 SMB 连接断了？" closed="true" %}}
你的 iPhone 是服务器，而 iOS 会暂停在后台停留太久的应用。有设备连接时让 Everdisk 保持在屏幕上打开，长时间传输时给手机接上电源。也要确保两台设备都停留在同一个 Wi-Fi 上。
{{% /details %}}

{{% details title="SMB、WebDAV 还是 FTP，我该用哪个？" closed="true" %}}
当你想让手机在 Mac、另一部 iPhone、Linux 或 NAS 上表现得像一块真正的网络硬盘，并且想要加密时，就用 SMB。当你想要一块在 Windows 上也运行良好的网络硬盘时，用 WebDAV。若要与旧设备和旧应用获得最广泛的兼容性，就用 FTP。Everdisk 可以同时运行所有这些，所以你不会被锁定在某一种上。
{{% /details %}}

{{% details title="Everdisk 免费吗？" closed="true" %}}
是的，Everdisk 可免费下载，且已包含 SMB 服务器。可选的一次性 Premium 购买会增加 SMB 加密、自定义端口以及其他一些额外功能。你无需付费就能设置 SMB 并共享文件。
{{% /details %}}

想试试吗？[从 App Store 下载 Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)，大约一分钟就能在 Finder 中打开你的 iPhone。有疑问或反馈？发邮件给我们：**support@everappz.com**。
