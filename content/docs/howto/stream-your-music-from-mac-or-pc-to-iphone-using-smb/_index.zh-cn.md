---
title: "使用SMB从Mac或PC向iPhone串流音乐"
description: "了解如何使用Evermusic和SMB协议从Mac或Windows PC向iPhone或iPad串流您的音乐收藏。一个简单的分步指南，无需同步即可连接和享受音频。"
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["从Mac串流音乐到iPhone", "SMB音频串流iOS", "Evermusic SMB设置", "连接PC音乐iPhone", "Mac音乐共享iOS", "SMB Windows文件串流", "Evermusic PC文件夹访问"]
---

{{< author-byline >}}


**简要说明：** 使用Evermusic应用程序通过SMB在本地网络上从Mac或Windows PC向iPhone或iPad串流音乐。无需同步，无需复制——只需在计算机上启用文件共享，在应用中连接并播放。设置不到5分钟。

您是否淹没在MAC或PC上的音乐海洋中，想要在iPhone或iPad上轻松享受它们？Evermusic就是您的最佳选择。使用Evermusic，通过SMB协议连接您的计算机并串流您喜爱的音乐非常简单，无需担心占用额外的设备空间或处理同步问题。以下是入门的分步指南：

## 第1步：在计算机上启用SMB协议

![Evermusic - SMB支持 - Mac共享屏幕](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### 如果您使用MAC

- 打开系统偏好设置 -> 共享。
- 启用文件共享服务。
- 在"共享文件夹"部分，添加您的音乐文件夹，选择用户并设置权限级别（读写或只读）。
- 为方便起见，您可以为音乐文件夹选择"所有人：只读"，使其在Evermusic中轻松访问。
- 别忘记记住您计算机的URL（smb://192.168.xx.xx）以用于下一步。

![Evermusic - SMB支持 - 文件共享屏幕](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- 点击"选项"并启用"使用SMB共享文件和文件夹"。
- 为可用账户启用"Windows文件共享"。

![Evermusic - SMB支持 - 共享文件和文件夹屏幕](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### 如果您使用Windows PC

![Evermusic - SMB支持 - 在Windows上共享文件](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- 右键单击您的音乐文件夹。
- 选择"属性"。
- 打开"共享"选项卡。
- 单击"共享..."
- 选择要共享的人员并设置他们的权限级别。
- 与MAC一样，您可以为所选音乐文件夹选择"所有人：读取"。
- 单击"完成"保存设置。

![Evermusic - SMB支持 - Windows上的共享文件夹](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## 第2步：自动添加您的计算机

- 现在，打开Evermusic并转到"连接"选项卡（如果您使用旧版应用，则为"网络"）。
- 如果您在"可用设备"（如果您使用旧版应用，则为"可用共享"）部分看到您的计算机，并且在上一步中选择了"所有人：只读"，只需点击您的计算机，它将自动连接。
- 如果没有发生，您可以手动添加计算机。

![Evermusic - SMB支持 - 连接账户屏幕](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## 第3步：手动添加您的计算机

- 点击"连接云服务"（如果您使用旧版应用，则为"添加账户"）
- 在下一个屏幕上从可用服务器列表中选择"SMB"。
- 在"SMB"设置屏幕上：
  - 输入带有共享文件夹路径的服务器URL。您可以输入服务器名称或服务器IP。例如：
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - 输入您的登录名和密码，或者如果您在上一步中选择了"所有人：只读"，则将这些字段留空。
  - "WORKGROUP"字段是可选的，如果您有Active Directory域则应使用。

![Evermusic - SMB支持 - 输入凭据屏幕](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

连接SMB账户后，它将出现在"云服务"（"账户"）部分。点击打开已连接的账户，导航到音乐文件夹，然后点击任何音频文件以启动播放器。

![Evermusic - SMB支持 - 打开已连接文件夹屏幕](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

使用Evermusic在iPhone或iPad上无缝享受您的音乐收藏。

![Evermusic - SMB支持 - 音频播放器屏幕](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## 第4步：SMB2解决方案

如果您在浏览文件夹或播放包含特殊字符（如ü、ö、é）的文件时遇到问题，这可能与SMB2协议有关。我们正在积极解决这个问题。

作为临时解决方案，请尝试在服务器和应用设置中启用SMB 1。或者，您可以使用系统文件打开菜单连接到SMB服务器。方法如下：

1. 导航到"本地文件"。
2. 向下滚动到"此设备上的文件"部分，然后点击"打开文件..."或"打开文件夹..."
3. 找到您的服务器并选择所需的文件或文件夹。
4. 点击"打开"确认选择。

## 第5步：WebDAV解决方案

此外，如果支持，您可以尝试使用WebDAV或DLNA协议连接到NAS。

按照这些步骤，您可以绕过与文件名中特殊字符相关的问题，继续享受您的媒体文件。

附注：您还可以使用iTunes文件共享将音频文件从MAC/PC传输到iPhone，并播放本地音频文件。在我们的指南中了解有关此功能的更多信息：[如何在iPhone上播放iTunes文件](/docs/howto/how-to-play-local-itunes-files-on-my-iphone)。

## 常见问题

{{% details title="我可以不用iTunes从PC串流音乐到iPhone吗？" closed="true" %}}
可以。Evermusic通过本地Wi-Fi网络上的SMB连接到您的PC。不需要iTunes。只需在PC上启用文件共享并在应用中连接。
{{% /details %}}

{{% details title="SMB串流使用移动数据吗？" closed="true" %}}
不。SMB通过本地Wi-Fi网络工作。不需要互联网连接或移动数据。
{{% /details %}}

{{% details title="Evermusic通过SMB支持哪些音频格式？" closed="true" %}}
Evermusic支持MP3、FLAC、AAC、WAV、AIFF、OGG、WMA、ALAC和其他常见音频格式。文件直接从SMB共享播放。
{{% /details %}}

{{% details title="我可以从NAS串流音乐到iPhone吗？" closed="true" %}}
可以。如果您的NAS支持SMB（大多数支持，包括Synology、QNAP和WD My Cloud），您可以使用本指南中的相同步骤进行连接。
{{% /details %}}

{{% details title="串流时需要保持计算机开机吗？" closed="true" %}}
是的。由于Evermusic直接从计算机串流文件，计算机必须开机并连接到与iPhone相同的网络。
{{% /details %}}

{{% details title="SMB串流有文件大小限制吗？" closed="true" %}}
没有。Evermusic通过SMB串流任何大小的文件。大型无损文件（FLAC、WAV）可以正常工作。
{{% /details %}}
