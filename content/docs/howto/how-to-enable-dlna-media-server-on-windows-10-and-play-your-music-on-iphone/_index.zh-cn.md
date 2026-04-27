---
title: "如何在 Windows 10 上启用 DLNA 媒体服务器并在 iPhone 上播放音乐"
date: 2019-11-26
description: "在 Windows 10 上启用 DLNA 服务器，并使用 Evermusic 应用将音乐流式传输到 iPhone。包含分步设置指南。"
keywords: ["evermusic", "dlna", "windows 10", "iphone 音乐流媒体", "媒体服务器", "本地网络", "upnp"]
tags: ["evermusic", "音乐", "云端", "iphone", "存储", "本地", "nas", "windows", "wifi", "聆听", "网络", "远程", "家庭", "在线", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**摘要：** Windows 10 内置了 DLNA 服务器。在网络和共享设置中启用它，然后使用 iPhone 上的免费 **Evermusic** 应用通过 Wi-Fi 流式传输整个音乐库。无需第三方服务器软件。

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA：封面" caption="使用 Windows 10 和 Evermusic 将音乐通过 DLNA 流式传输到 iPhone" width="800" >}}

DLNA（数字生活网络联盟）是一个强大的工具，可以让您轻松地在网络上的 DLNA 支持设备之间流式传输各种媒体内容，包括音乐。好消息是，Windows 10 及之前的版本都内置了 DLNA 功能，无需第三方媒体服务器。以下是如何在 Windows 10 上启用 DLNA 媒体服务器并在 iPhone 上享受音乐流媒体。

## 如何在 Windows 10 上启用 DLNA 媒体服务器

1. 点击"开始"按钮。  
2. 选择"设置"图标。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="服务器设置" caption="打开 Windows 设置" width="500" >}}

3. 在"Windows 设置"屏幕上，选择"网络和 Internet"。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows 设置" caption="选择网络和 Internet" width="500" >}}

4. 在"网络"下，选择"网络和共享中心"。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="共享中心" caption="打开网络和共享中心" width="500" >}}

5. 在"网络和共享中心"屏幕上，点击左侧菜单中的"更改高级共享设置"。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="高级共享设置" caption="更改高级共享设置" width="500" >}}

6. 在"高级共享设置"屏幕上，向下滚动到"所有网络"部分，点击箭头展开。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="开启发现" caption="展开所有网络设置" width="500" >}}

7. 点击"启用媒体流"以激活 DLNA 服务器。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="开启服务器" caption="启用媒体流服务器" width="500" >}}

8. 为媒体库命名并选择允许访问的设备。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="媒体库名称" caption="命名您的 DLNA 媒体库" width="500" >}}

9. 点击"确定"确认操作。现在，您的个人文件夹（如音乐、图片和视频）将对任何支持 UPnP 的流媒体设备可见。

## 如何在 Windows 10 上禁用 DLNA 媒体服务器

1. 点击"开始"并在搜索栏中输入"services"。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows 服务" caption="打开 Windows 服务" width="500" >}}

2. 在"服务"屏幕上，向下滚动找到"Windows Media Player Network Sharing Service"。  
3. 双击它并将"启动类型"设置为"手动"。  
4. 点击"停止"按钮停止服务。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="停止 DLNA 服务" caption="禁用 DLNA 网络共享服务" width="500" >}}

## 如何在 iPhone 上从 DLNA 服务器播放音乐

1. 从 App Store 安装免费的 **Evermusic** 应用：  
   [Evermusic 应用](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. 打开"连接"标签页，点击"本地网络"部分中的"可用设备"。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic 连接" caption="Evermusic：连接屏幕" width="500" >}}

3. 等待几秒钟设备列表加载完成，然后点击 Windows Media Player DLNA 服务器（例如"MSEDGEWIN10: My Windows Library"）。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="可用设备" caption="Evermusic 中可用的 DLNA 服务器" width="500" >}}

4. 您将看到媒体服务器上可用文件夹的列表。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic 文件夹" caption="浏览 DLNA 服务器的共享文件夹" width="500" >}}

5. 打开任何包含音频文件的文件夹。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="文件夹内容" caption="查看共享 DLNA 文件夹的内容" width="500" >}}

6. 点击任何文件启动音频播放器。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="音频播放器" caption="在 Evermusic 中播放 DLNA 的音频文件" width="500" >}}

7. 要增强音频体验，点击屏幕底部音量指示器旁的"均衡器"图标，启用带前置放大器的 iPod 风格均衡器。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="均衡器" caption="使用内置均衡器增强播放效果" width="500" >}}

## 总结

通过 Windows 10 上的 DLNA 媒体服务器和 iPhone 上的 Evermusic，您可以享受从电脑到移动设备的无缝音乐流媒体。告别存储限制，拥抱点播音乐！

## 常见问题

{{% details title="我需要在 Windows 10 上安装服务器软件吗？" closed="true" %}}
不需要。Windows 10 包含内置的 DLNA 媒体服务器。您只需在网络和共享中心设置中启用媒体流即可。无需第三方软件。
{{% /details %}}

{{% details title="我的 iPhone 需要在同一个 Wi-Fi 网络上吗？" closed="true" %}}
是的。DLNA 流媒体通过本地网络工作。您的 Windows 10 电脑和 iPhone 都必须连接到同一个 Wi-Fi 网络，Evermusic 才能发现 DLNA 服务器。
{{% /details %}}

{{% details title="我可以通过 DLNA 流式传输哪些音频格式？" closed="true" %}}
Windows DLNA 服务器会共享音乐文件夹中的文件，不受格式限制。Evermusic 支持 MP3、FLAC、AAC、WAV、OGG、AIFF 等多种格式，因此您几乎可以播放服务器上的任何音频文件。
{{% /details %}}

{{% details title="我可以使用 Flacbox 代替 Evermusic 吗？" closed="true" %}}
可以。Flacbox 也支持 DLNA/UPnP 浏览和播放。您可以使用任一应用来发现和播放 Windows DLNA 服务器上的音乐。
{{% /details %}}

{{% details title="DLNA 流媒体会使用移动数据吗？" closed="true" %}}
不会。DLNA 完全在本地 Wi-Fi 网络上运行。不使用任何移动数据。但是，播放期间两台设备都必须保持连接到同一网络。
{{% /details %}}
