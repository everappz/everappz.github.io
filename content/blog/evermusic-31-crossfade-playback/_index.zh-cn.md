---
title: "Evermusic 3.1：Crossfade、音乐库同步与备份"
date: 2018-06-19
description: "Evermusic 3.1 新增交叉淡入淡出播放、重新设计的音乐库、云端备份和恢复、iPod 集成以及改进的 iOS 标签编辑功能。"
keywords: ["Evermusic 更新", "交叉淡入淡出播放 iOS", "云音乐应用", "音乐备份应用", "音频播放器队列", "音乐标签编辑器", "ID3 标签更新", "iPod 音乐库集成", "音乐播放器 iPhone", "交叉淡入淡出音乐 iOS", "音乐库同步云端", "备份音乐播放列表 iOS"]
tags: ["Evermusic", "交叉淡入淡出", "音乐库", "备份", "音频队列", "标签", "云播放器", "离线播放器", "编辑器", "iPod 音乐库"]
draft: false
aliases:
  - /post/evermusic-31-crossfade-playback/
  - /amp/evermusic-31-crossfade-playback/
  - /single-post/Evermusic-Sync-your-Music-Library-Save-playback-position-Correct-music-tags/
  - /amp/Evermusic-Sync-your-Music-Library-Save-playback-position-Correct-music-tags/
  - /index.php/2016/05/26/evermusic-2-3-sync-you-music-library-automatically/
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Evermusic 3.1：有何变化及其重要性

**TL;DR：** Evermusic 3.1 引入交叉淡入淡出播放（3-15 秒）、带同步功能的重新设计音乐库、完整的云存储备份/恢复、iPod 音乐库浏览、改进的队列控制和更好的 ID3 标签编辑。

此版本在播放、音乐库管理和数据安全方面带来了有意义的升级。以下是 3.1 版本的所有新内容。

### 交叉淡入淡出播放

交叉淡入淡出通过将一首歌的结尾与下一首歌的开头混合来消除曲目之间的静音。适用于：

- 古典音乐和现场录音
- DJ 风格的播放列表
- 连续背景收听

您可以将交叉淡入淡出时长设置为 **3 到 15 秒**，也可以完全关闭。

`Settings → Audio Player → Crossfade Playback`

### 重新设计的音乐库

音乐库界面已重建，更快速、更清晰：

- 在更简洁的布局中浏览歌曲、艺术家和专辑
- 将新曲目上传到云存储后，点击 **Synchronization** 按钮刷新
- 按名称、大小、曲目编号、专辑或艺术家排序
- 调整**元数据扫描速度**以平衡性能和电池续航

`Settings → Music Library → Metadata Reading`

### 音乐库备份和恢复

一键保护您的音乐数据：

- 备份播放列表、歌曲元数据、封面和应用设置
- 将单个存档文件保存到已连接的云存储
- 在任何设备上一键恢复所有内容

`Settings → Backup & Restore`

### 增强的音频播放器队列

新的队列控制提供更大的灵活性：

- **Play Next** — 在当前曲目之后插入一首歌
- **Play Later** — 将歌曲添加到队列末尾
- 通过简单手势重新排列或移除曲目

### iPod 音乐库集成

直接从 Evermusic 主屏幕浏览您的 iPod 音乐库。您可以将 iPod 曲目添加到播放队列或将其复制到应用的 Files 部分。

可用分类：

- 播放列表
- 专辑
- 艺术家
- 流派

### 云账户编辑

编辑任何已连接云服务的登录凭据，无需删除并重新添加账户。当密码更改或令牌过期时可节省时间。

### 改进的标签编辑器

**Audio Tags Editor** 现在更可靠地处理元数据纠正：

- 使用 **Identify** 操作扫描文件名并自动更新 ID3 标签
- 修复损坏的元数据或批量添加缺失的专辑信息

[从 App Store 下载 Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198)，立即试用这些功能。

---

## 常见问题

{{% details title="Evermusic 中的交叉淡入淡出播放是什么？" closed="true" %}}
交叉淡入淡出播放将一首曲目的结尾与下一首的开头混合，创造无缝过渡。您可以在 Settings → Audio Player → Crossfade Playback 中将时长设置为 3 到 15 秒。
{{% /details %}}

{{% details title="我可以将 Evermusic 播放列表备份到云存储吗？" closed="true" %}}
可以。Evermusic 3.1 允许您将整个音乐库——包括播放列表、元数据、封面和设置——备份到任何已连接的云服务，保存为单个文件。
{{% /details %}}

{{% details title="Evermusic 支持 iPod 音乐库浏览吗？" closed="true" %}}
支持。您可以直接从 Evermusic 主屏幕按播放列表、专辑、艺术家和流派浏览 iPod 音乐库，并将曲目添加到队列。
{{% /details %}}

{{% details title="如何修复 Evermusic 中不正确的歌曲标签？" closed="true" %}}
使用内置的 Tags Editor 并点击 Identify 操作。Evermusic 会扫描您的文件名并自动用纠正后的元数据更新 ID3 标签。
{{% /details %}}

{{% details title="Evermusic 支持哪些云服务？" closed="true" %}}
Evermusic 支持 Dropbox、Google Drive、OneDrive、MEGA、Box、Yandex.Disk、WebDAV、SMB/CIFS 和 FTP 服务器。
{{% /details %}}
