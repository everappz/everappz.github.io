---
title: "如何在Evermusic中在设备之间传输音乐库：分步指南"
description: "使用Wi-Fi Drive和备份工具，轻松将Evermusic音乐库、播放列表、专辑封面和设置从一台iPhone、iPad或Mac传输到另一台。"
date: 2024-12-29
tags: ["音乐库", "传输", "wifi", "备份", "webdav", "恢复"]
keywords: ["传输音乐库Evermusic", "备份和恢复播放列表Evermusic", "Evermusic WiFi Drive", "在设备之间同步Evermusic", "迁移Evermusic数据库", "Evermusic文件传输", "恢复音频播放器设置", "WebDAV音乐传输iOS"]
readingTime: 3
---

{{< author-byline >}}


**摘要：** 要将Evermusic库传输到新设备，请在源设备上创建备份，启动Wi-Fi Drive，通过同一网络连接第二台设备，下载备份和音乐文件，然后从备份恢复。整个过程大约需要10分钟，具体取决于库的大小。

在本指南中，我们将引导您完成将整个音乐库（包括数据库、专辑封面和设置）从一台设备（iPhone或Mac）传输到另一台设备的过程。虽然自动音乐库和播放列表同步是计划在未来推出的功能，但目前此过程必须手动完成。

## 第1步：在第一台设备上创建备份

1. **在第一台设备上打开应用**（拥有音乐库、播放列表和已连接云服务的设备）。
2. **导航到设置**，选择**备份和恢复**选项。

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. 在**备份和恢复**界面，选择要包含在备份文件中的项目：
   - **数据库**（包括音乐库和播放列表）
   - **专辑封面**
   - **设置**

这些选项默认已启用。

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. 点击**备份应用数据**开始备份过程。

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. 备份完成后，将出现一条信息提示。

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

点击**显示文件**以在**文档**目录中查看备份文件。备份文件通常保存在**Backup**文件夹中。

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## 第2步：启动Wi-Fi Drive服务器

1. 在应用中进入**连接**部分。
2. 向下滚动到**通过Wi-Fi连接**并点击。

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. 在下一个界面，点击**启动Wi-Fi Drive**。

- 您可以选择设置用户名和密码以增强安全性，但对于家庭网络来说这不是必需的。

4. 启动后，您将看到可用的服务器地址。这可以用于桌面浏览器或WebDAV应用，但在本指南中，我们将直接进入下一步。

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## 第3步：将第二台设备连接到第一台

1. 在第二台设备上打开应用（您要将库传输到的设备）。
2. 确保两台设备连接到同一Wi-Fi网络。
3. 在第二台设备上，打开**连接**标签页并选择**可用设备**。

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. 您应该会看到一个名为**Evermusic**的WebDAV连接（我们在第一台设备上启动的服务器）。点击它进行连接。

5. 连接后，您将看到第一台设备上的所有文件夹。

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## 第4步：准备文件传输

1. 在第二台设备上，进入**设置 > 文件管理器**并启用**将下载的文件保存到 - 每次询问**。

- 这确保您可以为每次下载选择目标文件夹。

2. 返回**连接**标签页并导航到已连接的WebDAV服务器。

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## 第5步：传输备份和音乐文件

1. 打开已连接WebDAV服务器上的**Backup**文件夹。

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. 点击备份文件旁边的**更多操作**按钮（三个点）并选择**下载**。

3. 在第二台设备上创建一个**Backup**文件夹来存储下载的文件。点击**完成**确认选择。

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. 传输任何其他音乐文件：
   - 检查WebDAV服务器上的**下载**文件夹或其他相关文件夹。

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- 使用**选择**选项选择文件，然后点击**更多操作 > 下载**。将它们保存到第二台设备上的相应文件夹中，以保持相同的目录结构。

目标是将第一台设备上的所有文件传输到当前设备，确保文件夹结构保持一致。这样，音乐库和播放列表中的链接将保持完好。请注意，存储在第一台设备应用文档目录之外的本地文件必须单独传输。由于应用在Wi-Fi Drive模式下无法访问这些文件，您需要使用系统文件应用进行传输。

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## 第6步：监控传输进度

1. 在第二台设备上，进入**本地文件**部分（或iPad/Mac上的**下载**标签页）。

2. 点击左上角的**传输活动**按钮来监控传输队列。

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## 第7步：从备份恢复数据

1. 备份文件和所有需要的音频文件下载到第二台设备后，打开**Backup**文件夹。

2. 点击备份文件，将出现确认消息。

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **注意：** 恢复将用备份数据替换当前所有音乐库数据、播放列表、设置和专辑封面。

3. 点击**恢复**开始过程。

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. 恢复完成后，提示将确认成功。

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

检查**播放列表**或**音乐库**部分以验证恢复。

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## 第8步：重新索引音乐库

1. 为获得最佳效果，请重新索引您的库以确保所有文件都被成功检测到。

2. 进入**设置 > 音乐库 > 离线音乐同步**并选择**开始扫描本地文件夹**。

按照这些步骤，您将成功将音乐库、播放列表和设置传输到另一台设备。如果遇到任何问题，请随时联系支持团队。

## 常见问题

{{% details title="我可以在没有Wi-Fi的情况下传输Evermusic库吗？" closed="true" %}}
Wi-Fi Drive要求两台设备在同一Wi-Fi网络上。目前没有蓝牙或蜂窝网络传输选项。您也可以使用AirDrop或文件应用在设备之间手动移动备份文件和音乐文件夹。
{{% /details %}}

{{% details title="云服务连接会随备份一起传输吗？" closed="true" %}}
备份包括数据库、播放列表、专辑封面和设置。出于安全原因，不包括云服务登录凭据。恢复后，您需要在新设备上重新连接云账户。
{{% /details %}}

{{% details title="第二台设备上的现有库会怎样？" closed="true" %}}
恢复备份将替换第二台设备上所有现有的音乐库数据、播放列表、设置和专辑封面。如果您想保留其数据，请先为第二台设备创建单独的备份。
{{% /details %}}

{{% details title="此过程在iPhone和Mac之间是否有效？" closed="true" %}}
是的。Evermusic支持在iPhone、iPad和Mac的任意组合之间进行Wi-Fi Drive传输。两台设备只需在同一Wi-Fi网络上即可。
{{% /details %}}

{{% details title="传输需要多长时间？" closed="true" %}}
传输时间取决于音乐库的大小和Wi-Fi速度。几个GB的典型库通过标准家庭网络传输需要5-15分钟。
{{% /details %}}
