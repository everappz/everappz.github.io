---
title: "分步指南：将 iCloud 资料库导入 Evermusic 和 Flacbox"
description: "了解如何在 Evermusic 和 Flacbox 中同步和流式传输 iCloud 音乐资料库。本指南介绍了流式传输、元数据读取和离线同步的最佳实践。"
date: 2024-11-14
readingTime: 7
tags: ["音乐", "云", "流媒体", "同步", "icloud", "资料库"]
keywords: ["导入 iCloud 音乐 Evermusic", "Flacbox iCloud 同步", "Evermusic 从 iCloud 流式传输", "音乐资料库 iOS 应用", "Flacbox 元数据读取器", "iCloud 音乐流式传输 iPhone"]
---

{{< author-byline >}}


**摘要：** 您可以在 Evermusic 和 Flacbox 中流式传输 iCloud Drive 音乐资料库，无需将文件下载到设备。在应用中连接 iCloud Drive，启用在线音乐同步来构建资料库，配置元数据读取器按艺术家/专辑/流派整理，并可选择启用离线模式下载专辑以便在没有互联网的情况下收听。这些步骤也适用于 Google Drive、Dropbox、OneDrive 和其他支持的云服务。

如何将 iCloud 音乐资料库与 Flacbox 和 Evermusic 同步以实现流畅播放。最近，我们的一位订阅者就一个常见问题联系了 Everappz 支持团队：

> "您好 Flacbox 支持团队，我最近订阅了 Flacbox 一年，但在正确同步 iCloud 中的音乐方面遇到了很大困难。我的 iCloud 中存储了大约 60 张各种原声专辑，我想将它们整合到应用中。然而，导入 Flacbox 资料库的过程似乎并不像我希望的那样顺畅。即使加载一张专辑到应用中也需要非常长的时间。昨天，我花了几个小时尝试不同的方法来高效导入专辑，但没有找到满意的解决方案。我希望能获得任何指导或分步指南，了解如何导入 iCloud 音乐（不在 iPhone 上本地存储）而不会导致过长的加载时间。"

对于许多在 iCloud 中拥有大量音乐资料库的用户来说，将文件整合到 Flacbox 和 Evermusic 中有时会面临挑战，特别是在同步速度和效率方面。如果您遇到了类似的问题，本指南将引导您了解简化导入流程、最小化加载时间和轻松享受音乐的最佳实践。在本指南中，我们将使用 iCloud 存储，但这些步骤也适用于应用支持的任何其他云服务。您将在本指南中看到 Mac 截图，但在 iPhone 上，屏幕和功能位置相同。

## 导入您的 iCloud 资料库

首先打开 [iCloud.com](https://icloud.com) 并创建 Music 文件夹来整理您的资料库。使用电脑操作更简单，因为网站支持拖放。

![iCloud Music 文件夹](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_141e817570c34e6a8c528b65a99a5ba4~mv2.png)

等待所有文件完全上传到 iCloud 后再继续。

![iCloud 上传](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_6f9f363bd64e4ca58190541fcc1ed28e~mv2.png)

打开应用并导航到 **连接** 部分。点击 **连接云服务** 并选择 **iCloud Drive**。在下一个屏幕上点击 **选择文件夹**。在左侧面板中选择 **iCloud Drive**，导航到 Music 文件夹并点击 **打开**。

![连接部分](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_ccfbcec8308d4974b630bd1a0868dfd4~mv2.png)

云文件夹添加到应用后，将出现在 **连接** 部分。点击已连接云文件夹中的任何文件启动音频播放器——应用将流式传输文件而不下载。

![音频播放器](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_27d2d6ec37c648fdb7e84e82d52eb38b~mv2.png)

要将文件添加到音乐资料库，打开 **音乐资料库** 屏幕。点击 **更多操作** 按钮并选择 **设置**。重点关注 **在线音乐同步**。启用此功能并点击 **同步在线文件夹** 选择文件夹。点击 **完成** 确认。

![在线音乐同步](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_cc7a80af9d394d57979549b0a5b9c91d~mv2.png)

启用 **后台同步** 后，应用即使在后台运行也会继续扫描。点击 **开始同步**。

## 元数据读取

转到 **音乐资料库设置** 并点击 **元数据读取**。

![元数据读取](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_a74acfe948934fa48913bfcd8450b3ab~mv2.png)

**可用模式：** 停用、当前歌曲、音频播放器队列、音乐资料库。

**重要**，元数据读取器仅更新音乐资料库中的元数据，不会更改云账户或本地存储中的文件。

**重新加载元数据** 操作将标记所有文件为缺少元数据以触发更新。

## 离线音乐同步

离线访问的两个选项：

1. **下载** 操作下载整个文件夹内容。
2. **离线模式** ——应用定期检查云文件夹并自动下载新文件。

点击 **更多操作** 并选择 **启用离线模式**。

![启用离线模式](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_f77314386cab41349e0140311515f9f1~mv2.png)

下载的文件出现在 **本地文件 - 离线文件夹** 部分。在 **同步离线文件夹** 部分可以管理离线同步。

![同步离线文件夹](/docs/howto/step-by-step-guide-importing-your-icloud-library-into-evermusic-and-flacbox/21260c_bb941f44ec994437a05fc3bcdd121c91~mv2.png)

**重要：** 建议定期启动离线音乐同步以保持音乐资料库更新。

今天就到这里！希望本指南帮助您配置云服务器和设备之间的同步。

## 常见问题

{{% details title="我可以不下载文件到 iPhone 就流式传输 iCloud 音乐吗？" closed="true" %}}
可以。连接 iCloud Drive 并使用在线音乐同步后，应用创建到云文件的链接并按需流式传输。除非您明确启用离线模式，否则文件不会被下载。
{{% /details %}}

{{% details title="为什么 iCloud 音乐导入很慢？" closed="true" %}}
导入慢通常是因为通过移动连接读取大型资料库的元数据。启用后台同步并考虑使用 Mac 版本。
{{% /details %}}

{{% details title="本指南适用于 iCloud 以外的云服务吗？" closed="true" %}}
适用。相同步骤适用于 Google Drive、Dropbox、OneDrive、SMB、WebDAV 和所有其他支持的云服务。
{{% /details %}}

{{% details title="如何将音乐资料库从 Mac 传输到 iPhone？" closed="true" %}}
使用应用设置中的数据备份/恢复功能。先在 Mac 版本上同步和读取元数据，创建备份，然后在 iOS 版本上恢复。
{{% /details %}}

{{% details title="元数据读取器会更改我的原始音频文件吗？" closed="true" %}}
不会。元数据读取器仅更新音乐资料库中的显示信息。要编辑文件标签，请使用内置标签编辑器。
{{% /details %}}

{{% details title="如何使专辑可离线使用？" closed="true" %}}
点击云文件夹上的 **更多操作** 并选择 **启用离线模式**。应用下载所有文件并自动保持与云版本同步。
{{% /details %}}
