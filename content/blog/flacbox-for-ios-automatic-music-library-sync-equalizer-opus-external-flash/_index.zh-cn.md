---
title: "Flacbox 1.6：自动同步、均衡器、OPUS 支持"
date: 2017-01-25
description: "iOS 版 Flacbox 1.6 新增自动云同步、10 段均衡器、OPUS 格式支持以及 iPhone 和 iPad 的外置闪存驱动器播放功能。"
keywords: ["Flacbox 更新", "FLAC 播放器 iOS", "10 段均衡器 iPhone", "自动音乐同步", "在 iPhone 上播放 OPUS", "外置闪存驱动器音乐", "FLAC 流式播放 iOS", "hi-res 音乐应用 iPhone", "Flacbox 均衡器", "SD 卡音乐播放器 iOS"]
tags: ["Flacbox", "均衡器", "音乐库", "OPUS", "FLAC", "外部存储", "同步", "音频播放器", "iOS 应用", "更新"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**Flacbox 1.6** 为 iPhone 和 iPad 的 FLAC 音乐播放器带来了重大新功能。

**摘要：** 此更新新增自动云库同步、带自定义预设的 10 段均衡器、OPUS 格式支持以及从外置 SD 卡播放音乐的功能。FLAC 播放错误也已修复。

## Flacbox 1.6 的新功能

### 自动云音乐库同步

不再需要手动刷新音乐库。新的同步引擎自动扫描选定的云文件夹并实时更新您的音乐库。

- 通过以下位置启用：**Settings → Music Library → Automatic Sync**
- 通过 **Sync Folder → Change Settings** 选择文件夹
- 选择同步模式：仅 Wi-Fi 或 Wi-Fi + 蜂窝数据
- 启用 **Background Sync** 在播放器活跃时自动更新（增加电池消耗）

您的云音乐收藏无需手动干预即可保持最新。

### 10 段均衡器定制音效

使用内置的 **10 段均衡器**调整音效，可从播放器屏幕或设置中访问。

- 在 **-12 dB** 和 **+12 dB** 之间调整频率
- 使用内置预设或创建自己的
- 微调前置放大器功率（注意保护听力）

这让您在 iPhone 或 iPad 上拥有录音棚级别的音频控制。

### OPUS 文件格式支持

Flacbox 现在可以播放 **OPUS** 文件，以及 FLAC、ALAC、MP3 和其他格式。OPUS 是一种广泛用于语音和音乐的高效编解码器。OPUS 播放完全支持均衡器。

### 从外置 SD 卡播放音乐

直接从连接到 iPhone 或 iPad 的 SD 或 microSD 卡播放音乐：

- 使用 **Lightning to SD Card Camera Reader Adapter**
- 插入卡片并连接到设备
- 打开 Flacbox -- 自动识别卡片
- 通过 **Services → PowerDrive** 部分浏览和播放文件

这非常适合在不使用设备存储的情况下扩展音乐库。

### FLAC 播放错误修复

**FLAC 文件末尾的 2 秒跳过**问题已完全解决。曲目现在从头到尾无缝播放。

## 下载 Flacbox

Flacbox 1.6 现已在 App Store 上提供。[下载 Flacbox](https://itunes.apple.com/us/app/flacbox-flac-player-music/id1097564256?mt=8) 并立即试用这些功能。

有反馈或功能请求？联系我们 -- 我们根据用户需求构建 Flacbox。

## 常见问题

{{% details title="Flacbox 支持哪些音频格式？" closed="true" %}}
Flacbox 支持 FLAC、ALAC、MP3、AAC、OGG、OPUS、WAV、AIFF、DSD 和其他流行的音频格式。所有格式均可使用内置均衡器。
{{% /details %}}

{{% details title="我可以在 iPhone 上从 SD 卡播放音乐吗？" closed="true" %}}
可以。使用 Lightning to SD Card Camera Reader Adapter 连接 SD 或 microSD 卡。Flacbox 自动检测卡片，让您直接从外部存储浏览和播放文件。
{{% /details %}}

{{% details title="Flacbox 能自动与云存储同步吗？" closed="true" %}}
能。从 1.6 版本开始，Flacbox 可以自动从云文件夹同步您的音乐库。在设置中启用自动同步并选择要监控的文件夹。
{{% /details %}}

{{% details title="Flacbox 均衡器可以自定义吗？" closed="true" %}}
可以。10 段均衡器允许您在 -12 dB 和 +12 dB 之间调整各个频率级别。您可以使用内置预设或保存自己的自定义设置。
{{% /details %}}
