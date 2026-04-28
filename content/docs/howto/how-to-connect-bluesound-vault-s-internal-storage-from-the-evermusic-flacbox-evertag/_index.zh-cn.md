---
title: "如何从Evermusic、Flacbox、Evertag连接Bluesound VAULT的内部存储"
date: 2022-03-10
description: "了解如何使用SMB协议从Evermusic、Flacbox和Evertag访问Bluesound VAULT的内部硬盘，以管理、编辑和播放音频文件。"
keywords: ["bluesound vault", "连接smb存储", "evermusic smb", "flacbox vault", "evertag smb", "nas存储音乐", "vault内部驱动器"]
tags: ["evermusic", "连接", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**摘要：** 使用Evermusic、Flacbox或Evertag通过SMB连接到Bluesound VAULT的内部存储。在BluOS应用中找到VAULT的IP地址，将其作为SMB连接输入并使用访客访问，然后开始播放或管理您的音乐文件。

Bluesound VAULT拥有内部硬盘，可作为网络附加存储（NAS）使用。访问VAULT的内部硬盘可以让您从我们的应用Evermusic、Flacbox、Evertag中添加/删除文件、编辑元数据标签。

**以下是访问VAULT内部硬盘的步骤：**

1. 在BluOS应用中，选择**帮助 > 诊断**。

2. 从**诊断**页面获取VAULT的**IP地址**。此**IP地址**将在后续步骤中使用。

3. 打开Evermusic、Flacbox或Evertag。

   ![Everappz应用程序](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. 打开"连接"界面，选择"连接云服务"菜单项。

   ![Evermusic连接界面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. 选择"SMB"云服务。

   ![Evermusic连接云服务界面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. 在"SMB配置界面"中按以下格式输入URL：

   ```
   SMB://<<VAULT-IP>>
   ```

   将`<<VAULT-IP>>`替换为步骤2中获取的**IP地址**。

   **注意：** 将登录名和密码字段留空，因为VAULT存储支持访客（GUEST）模式。

   ![Evermusic SMB连接界面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. 点击"登录"按钮保存配置。

8. 打开已连接的云存储，导航到包含音频文件的文件夹，点击任意文件启动音频播放器。

   ![Evermusic已打开的SMB服务器界面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. 您还可以使用内置文件管理器编辑文件。

   ![Evermusic文件管理器界面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

通过这些简单的步骤，您可以轻松访问Bluesound VAULT的内部硬盘，并使用Evermusic、Flacbox或Evertag控制您的音乐库。

## 常见问题

{{% details title="连接Bluesound VAULT需要用户名和密码吗？" closed="true" %}}
不需要。Bluesound VAULT支持通过SMB进行访客（匿名）访问。配置连接时将登录名和密码字段留空即可。
{{% /details %}}

{{% details title="我可以在Bluesound VAULT上编辑音乐标签吗？" closed="true" %}}
可以。使用Evertag，您可以编辑直接存储在VAULT内部硬盘上的音频文件的元数据标签（标题、艺术家、专辑等）。
{{% /details %}}

{{% details title="Bluesound VAULT支持哪些协议？" closed="true" %}}
Bluesound VAULT通过SMB（Server Message Block）公开其内部存储。Evermusic、Flacbox和Evertag都支持SMB连接，使连接变得简单。
{{% /details %}}

{{% details title="我可以在不将文件复制到iPhone的情况下从VAULT串流音乐吗？" closed="true" %}}
可以。通过SMB连接后，您可以直接从VAULT的内部驱动器串流音频文件，无需将其复制到您的设备。
{{% /details %}}
