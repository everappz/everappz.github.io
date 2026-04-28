---
title: "如何使用 WebDAV 连接 NAS 存储并在 iPhone 或 Mac 上听音乐"
date: 2024-07-28
description: "了解如何在 Synology NAS 上配置 WebDAV，并使用 Evermusic 或 Flacbox 将音乐流式传输到 iPhone 或 Mac。按照我们的分步指南操作。"
keywords: ["连接 nas", "webdav synology", "流式传输音乐 nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["音乐", "流式传输", "存储", "nas", "连接", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**概要：**在 Synology NAS 上安装并启用 WebDAV，配置共享文件夹权限，然后使用 NAS IP 地址和 WebDAV 端口（默认 5005/5006）从 Evermusic 或 Flacbox 连接。您可以流式传输和管理整个音乐库，无需将文件复制到设备。

了解如何使用 WebDAV 连接您的 NAS 存储，并轻松将音乐库流式传输到 iPhone 或 Mac。WebDAV（Web-based Distributed Authoring and Versioning）是一种允许您通过互联网管理和共享文件的协议。通过在 NAS 上设置 WebDAV，您可以访问和流式传输音乐收藏，确保您最喜欢的歌曲随时触手可及。

在本指南中，我们将向您展示如何在最受欢迎的 NAS 服务器之一 Synology NAS 上设置 WebDAV 连接。按照我们简单的步骤在 Synology NAS 上配置 WebDAV，您将能够直接从 iPhone 或 Mac 浏览、流式传输和管理音乐库。

## 步骤 1：在 Synology NAS 上安装 WebDAV

1. 登录 Synology NAS 并打开**套件中心**。
2. 搜索"webdav"并安装 WebDAV 套件（如果尚未安装）。打开 WebDAV 服务器进行配置。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="在 Synology 上安装 WebDAV" width="600" >}}

## 步骤 2：配置 WebDAV 服务器

1. 在 WebDAV 设置页面，勾选**启用 HTTP**、**启用 HTTPS**、**启用匿名 WebDAV** 和**启用 DavDepthInfinity** 的复选框。
2. 点击**应用**保存更改。记下 HTTP 和 HTTPS 连接的端口号，默认为 5005 和 5006。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="配置 WebDAV 设置" width="600" >}}

## 步骤 3：配置共享文件夹权限

1. 打开**控制面板**并进入**共享文件夹**部分。
2. 选择**音乐**文件夹并点击**编辑**。
3. 在**权限**标签页中，配置权限。如果只需听音乐，启用只读的访客访问；如果需要修改文件，启用读/写权限。保存更改。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="共享文件夹权限" width="600" >}}

## 步骤 4：查找 Synology NAS IP 地址

1. 打开**控制面板**并进入**网络接口**标签页，或使用浏览器访问 [find.synology.com](http://find.synology.com)。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="查找 NAS IP 地址" width="600" >}}

2. 记下 Synology NAS 的 IP 地址（例如 192.168.18.137）。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP 地址" width="600" >}}

## 步骤 5：使用 Evermusic/Flacbox 连接 Synology NAS

1. 打开 Evermusic 或 Flacbox 应用并进入**连接**标签页。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Evermusic 中的连接标签页" width="600" >}}

2. 要自动连接，在**可用设备**部分找到 Synology NAS 并点击连接。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="可用设备列表" width="600" >}}

3. 要手动连接，选择**连接云服务**并选择 **WebDAV**。按以下格式输入服务器地址：PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER（例如 [https://192.168.18.137:5006](https://192.168.18.137:5006)）。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="手动配置 WebDAV" width="600" >}}

4. 访客访问时将登录名和密码字段留空，或输入 Synology 凭据。点击**登录**。

## 步骤 6：浏览和播放音乐

1. 连接后，设备将出现在**连接的配件**列表中。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Evermusic 中的已连接设备" width="600" >}}

2. 导航到**音乐**文件夹并点击任意音频文件开始播放。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="浏览音乐文件夹" width="600" >}}

## 步骤 7：将已连接的云文件夹添加到音乐库

1. 在应用中打开**音乐库**部分。
2. 选择**添加音乐**并选择**连接**。
3. 选择已连接的 NAS 服务器并选择**音乐**文件夹。点击**完成**。
4. 应用将扫描音乐文件夹并将支持的音频文件添加到音乐库。元数据将被加载，您的曲目将按专辑、艺术家和流派分组。

## 总结

按照这些步骤，您可以轻松地在 Synology NAS 上设置 WebDAV 连接，并使用 Evermusic 或 Flacbox 将音乐库流式传输到 iPhone 或 Mac。随时享受对您最喜欢的曲目的无缝访问。

## 常见问题

{{% details title="哪些 NAS 设备支持 WebDAV？" closed="true" %}}
大多数流行的 NAS 品牌都支持 WebDAV，包括 Synology、QNAP、TrueNAS 和 Western Digital。请查看您的 NAS 制造商的文档以获取 WebDAV 设置说明。
{{% /details %}}

{{% details title="WebDAV 和 SMB 在 NAS 音乐流式传输方面有什么区别？" closed="true" %}}
WebDAV 通过 HTTP/HTTPS 工作，更适合通过互联网进行远程访问。SMB 在局域网中通常更快。Evermusic 和 Flacbox 支持这两种协议，因此根据您需要本地还是远程访问来选择。
{{% /details %}}

{{% details title="在 Synology 上使用 WebDAV 需要用户名和密码吗？" closed="true" %}}
不需要，如果您启用了匿名 WebDAV 访问并在共享文件夹上配置了访客权限。为了更好的安全性，您可以使用 Synology 凭据。
{{% /details %}}

{{% details title="我可以通过 WebDAV 从 NAS 流式传输 FLAC 和其他高分辨率格式吗？" closed="true" %}}
可以。Evermusic 和 Flacbox 在通过 WebDAV 从 NAS 存储流式传输时都支持 FLAC、ALAC、WAV、DSD 和其他高分辨率格式。
{{% /details %}}

{{% details title="为什么应用在可用设备中找不到我的 NAS？" closed="true" %}}
确保您的 iPhone/Mac 和 NAS 在同一个 Wi-Fi 网络上。如果自动发现不起作用，请使用手动连接选项并直接输入 NAS IP 地址和 WebDAV 端口。
{{% /details %}}
