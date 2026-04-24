---
title: "使用SMB协议将文件从电脑传输到iPhone"
description: "了解如何使用Evermusic和SMB协议将大文件从Mac或Windows PC传输并访问到iPhone或iPad。无缝流媒体和文件管理的分步指南。"
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["传输文件到iPhone SMB", "在iPhone上串流PC音乐", "Mac连接iPhone SMB", "Evermusic SMB设置", "访问电脑文件iPhone", "Windows音乐共享iOS", "SMB文件传输Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**摘要：** 在iPhone或iPad上使用Evermusic，通过SMB在本地网络上访问存储在Mac或Windows PC上的文件。无需数据线、无需iTunes、无需上传到云端。在电脑上启用文件共享，在应用中连接，即可无线浏览或播放文件。

您的MAC或PC上是否有大量文件，想要从iPhone或iPad轻松访问？我们的应用提供了简单的解决方案。

按照以下步骤，使用SMB协议在电脑和iOS设备之间实现无缝访问：

## 步骤1：在电脑上启用SMB协议

**对于MAC：**

1. 在MAC上打开"系统偏好设置"。
2. 点击"共享"。
3. 启用"文件共享"服务。
4. 将音乐文件夹添加到"共享文件夹"部分。添加用户并选择权限级别（读写或只读）。您可以为添加的音乐文件夹选择"所有人：只读"。

   ![Mac设置屏幕](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. 记住电脑URL（smb://192.168.xx.xx），因为您将在下一步中使用它。
6. 点击"选项"并激活"使用SMB共享文件和文件夹"。

   ![Mac文件共享屏幕](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. 为可用账户启用"Windows文件共享"。

   ![Mac SMB共享屏幕](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**对于Windows PC：**

1. 右键点击音乐文件夹。
2. 选择"属性"。
3. 导航到"共享"选项卡。
4. 点击"共享..."
5. 选择要与之共享文件夹的人员并指定权限级别。您可以为选择的音乐文件夹选择"所有人：读取"。

   ![Windows SMB共享屏幕](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. 点击"完成"。
7. 在"文件共享"窗口中点击"完成"，并记住文件夹路径。

   ![Windows SMB共享文件夹](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## 步骤2：连接iOS设备

1. 在iPhone或iPad上打开应用。
2. 转到"连接"选项卡。

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic连接屏幕"
  caption="Evermusic连接屏幕"
  width="400"
>}}

*如果您的电脑出现在"可用设备"部分：*

如果您的电脑在"可用设备"部分可见，并且您在上一步中选择了"所有人：只读"，只需点击您的电脑即可自动连接。

*如果您的电脑没有自动出现：*

1. 点击"连接云服务"。
2. 在"连接云服务"屏幕中选择"SMB"。

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic连接云服务屏幕"
  caption="Evermusic连接云服务屏幕"
  width="400"
>}}

3. 在"SMB连接"屏幕中，输入服务器URL和共享文件夹路径。您可以使用服务器名称或服务器IP：

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. 输入您的用户名和密码，或者如果您在上一步中选择了"所有人：只读"，则将这些字段留空。
5. "WORKGROUP"字段是可选的，如果您有Active Directory Domain，则应使用该字段。

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMB连接器屏幕"
  caption="Evermusic SMB连接器屏幕"
  width="400"
>}}

6. 使用SMB协议连接电脑后，它将出现在"连接"屏幕的"云服务"部分。
7. 打开已连接的服务并导航到所需文件夹。

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="在Evermusic中打开的SMB文件夹"
  caption="在Evermusic中打开的SMB文件夹"
  width="400"
>}}

8. 您可以使用内置文件管理器根据需要编辑文件。

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic文件管理器"
  caption="Evermusic文件管理器"
  width="400"
>}}

## 步骤3：包含特殊字符的SMB2文件夹解决方案

使用SMB2协议时，有时可能会遇到包含特殊字符的文件夹问题。以下是解决此问题的步骤：

1. **启用SMB 1：**  
   • 作为临时解决方案，尝试在服务器和应用设置中启用SMB 1。这可以帮助绕过与文件夹名称中特殊字符相关的问题。

2. **使用系统文件打开菜单：**  
   • 导航到"本地文件"。  
   • 向下滚动到"此设备上的文件"部分。  
   • 点击"打开文件..."或"打开文件夹..."。  
   • 找到您的服务器并选择所需的文件或文件夹。  
   • 点击"打开"确认您的选择。

3. **替代协议：**  
   • 如果问题持续存在，请考虑使用WebDAV或DLNA协议连接到NAS（如果您的NAS支持这些选项）。这些协议可能更好地处理特殊字符。

按照这些步骤，您可以减轻使用SMB2协议时文件夹名称中特殊字符的问题。

## 结论

通过这些步骤，您可以使用我们的应用轻松地从MAC或PC在iPhone或iPad上访问大量文件。

## 常见问题

{{% details title="我可以不用iTunes从iPhone访问PC上的文件吗？" closed="true" %}}
可以。Evermusic通过本地Wi-Fi网络上的SMB连接到您的电脑。不需要iTunes或Finder同步。在PC上启用文件共享，直接从应用连接即可。
{{% /details %}}

{{% details title="SMB文件访问可以通过互联网工作吗？" closed="true" %}}
不可以。SMB是本地网络协议。您的iPhone和电脑必须在同一个Wi-Fi网络上。要远程访问，请将文件上传到Google Drive或Dropbox等云服务，然后在Evermusic中连接。
{{% /details %}}

{{% details title="我可以通过SMB访问哪些文件类型？" closed="true" %}}
Evermusic支持MP3、FLAC、AAC、WAV、AIFF、OGG、WMA、ALAC和其他音频格式。您还可以使用内置文件管理器浏览和管理非音频文件。
{{% /details %}}

{{% details title="我可以使用SMB将文件从NAS传输到iPhone吗？" closed="true" %}}
可以。大多数NAS设备（Synology、QNAP、WD My Cloud等）都支持SMB。使用本指南中的相同步骤连接到您的NAS。
{{% /details %}}

{{% details title="我需要将文件复制到iPhone才能播放吗？" closed="true" %}}
不需要。Evermusic通过网络直接从您的电脑或NAS流式传输文件。除非您选择下载文件进行离线播放，否则文件不会复制到iPhone。
{{% /details %}}

{{% details title="SMB文件共享安全吗？" closed="true" %}}
SMB文件共享仅在本地网络上工作。其他网络上的设备无法访问您的共享文件夹。为了额外安全，请使用用户名和密码而不是匿名（所有人）访问。
{{% /details %}}
