---
title: "使用 AVAssetResourceLoader 实现 iOS 音频流媒体播放"
date: 2015-06-20
description: "学习如何使用 AVAssetResourceLoaderDelegate 和 AVPlayer，通过自定义 URL 方案和磁盘缓存在 iOS 中实现音频流媒体传输与缓存。"
keywords: ["iOS 音频流媒体", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer 教程", "AVFoundation 音频", "AVAssetResourceLoadingRequest", "iOS 自定义音频播放器", "iOS 云端音频流", "iOS 音频缓存", "Swift AVPlayer 自定义方案"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**TL;DR：** 使用带有自定义 URL 方案的 `AVAssetResourceLoaderDelegate` 来拦截 AVPlayer 的资源加载。这让你可以为云服务添加自定义授权请求头、将音频缓存到磁盘，并控制流媒体行为——无需编写本地 HTTP 代理。完整源代码托管于 [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader)。

---

## 为什么 AVPlayer 需要自定义资源加载器

`AVPlayer` 可以播放本地文件和远程 URL 的音频。对于大多数云服务（Dropbox、Google Drive、Box），你可以传入直接下载链接，播放即可开箱即用。

然而，像 **Yandex.Disk** 和 **WebDAV** 这类服务在 GET 请求中需要自定义授权请求头。`AVPlayer` 没有内置方式来注入这些请求头。

解决方案：使用 `AVURLAsset` 的 `resourceLoader` 属性。该 API 拦截资源加载请求，如同本地 HTTP 代理，但没有复杂的实现难度。

### 工作原理

当 AVPlayer 无法识别 URL 方案时，会使用 `resourceLoader`。通过将 `https://` 替换为自定义方案（如 `customscheme://`），你可以强制 AVPlayer 将所有加载委托给你的应用。

你需要实现两个 `AVAssetResourceLoaderDelegate` 方法：

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- 当 AVPlayer 需要数据时调用。保存 `AVAssetResourceLoadingRequest` 并启动数据加载操作。
2. **`resourceLoader:didCancelLoadingRequest:`** -- 当请求被取消或被替代时调用。

## 如何创建自定义 AVPlayer

使用自定义 URL 方案设置 AVPlayer：

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

此代码：
- 定义带有自定义方案的 URL
- 在主队列上创建带有委托的 `AVURLAsset`
- 从资源构建 `AVPlayerItem`
- 初始化 `AVPlayer`

## 实现资源加载器委托

创建名为 `LSFilePlayerResourceLoader` 的类来处理从服务器获取数据并将其传回 `AVURLAsset`。将加载器实例存储在以资源 URL 为键的字典中。

```objc
- (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest *)loadingRequest {
    NSURL *resourceURL = [loadingRequest.request URL];
    if ([resourceURL.scheme isEqualToString:@"customscheme"]) {
        LSFilePlayerResourceLoader *loader = 
        [self resourceLoaderForRequest:loadingRequest];
        if (!loader) {
            loader = [[LSFilePlayerResourceLoader alloc] initWithResourceURL:resourceURL session:self.session];
            loader.delegate = self;
            [self.resourceLoaders setObject:loader forKey:[self keyForResourceLoaderWithURL:resourceURL]];
        }
        [loader addRequest:loadingRequest];
        return YES;
    }
    return NO;
}

- (void)resourceLoader:(AVAssetResourceLoader *)resourceLoader didCancelLoadingRequest:(AVAssetResourceLoadingRequest *)loadingRequest {
    LSFilePlayerResourceLoader *loader = [self resourceLoaderForRequest:loadingRequest];
    [loader removeRequest:loadingRequest];
}
```

这些方法检查 URL 方案，创建或获取加载器，并将请求添加到加载器队列。无法识别的方案返回 `NO`。

## LSFilePlayerResourceLoader 接口

```objc
@interface LSFilePlayerResourceLoader : NSObject

@property (nonatomic, readonly, strong) NSURL *resourceURL;
@property (nonatomic, readonly) NSArray *requests;
@property (nonatomic, readonly, strong) YDSession *session;
@property (nonatomic, readonly, assign) BOOL isCancelled;
@property (nonatomic, weak) id<LSFilePlayerResourceLoaderDelegate> delegate;

- (instancetype)initWithResourceURL:(NSURL *)url session:(YDSession *)session;
- (void)addRequest:(AVAssetResourceLoadingRequest *)loadingRequest;
- (void)removeRequest:(AVAssetResourceLoadingRequest *)loadingRequest;
- (void)cancel;

@end

@protocol LSFilePlayerResourceLoaderDelegate <NSObject>

@optional
- (void)filePlayerResourceLoader:(LSFilePlayerResourceLoader *)resourceLoader didFailWithError:(NSError *)error;
- (void)filePlayerResourceLoader:(LSFilePlayerResourceLoader *)resourceLoader didLoadResource:(NSURL *)resourceURL;

@end
```

## 数据加载：两步流程

当加载请求进入队列时，两个操作按顺序执行：

- **contentInfoOperation** -- 查询内容长度、MIME 类型和字节范围支持
- **dataOperation** -- 从 `requestedOffset` 开始获取文件数据

## 磁盘缓存策略

下载的数据被写入磁盘上的临时文件。后续对相同内容的请求从此缓存提供，避免冗余的网络调用。此方法：

- 减少带宽使用
- 实现几乎即时的重播
- 支持在缓存范围内的快进操作

## 处理待处理请求

`processPendingRequests` 方法用元数据填充每个请求的 `contentInformationRequest`，并传递缓存的字节范围。已完成的请求从队列中移除。

## 源代码与后续步骤

本教程提供了实现 `AVAssetResourceLoaderDelegate` 进行带自定义授权请求头的云端音频流媒体的高层次概述。完整源代码可在 [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader) 获取。

此方法为 [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) 的音频流媒体引擎提供支持，该应用可在 iOS 和 macOS 上从 Dropbox、Google Drive、OneDrive、Yandex.Disk 及其他云服务流式播放音乐。

## 常见问题

{{% details title="什么时候应该使用 AVAssetResourceLoaderDelegate 而不是直接 URL？" closed="true" %}}
当云服务需要自定义授权请求头、需要对流式音频进行磁盘缓存，或希望精细控制数据加载和缓冲方式时，请使用它。
{{% /details %}}

{{% details title="这种方法适用于 Swift 吗？" closed="true" %}}
是的。`AVAssetResourceLoaderDelegate` 协议在 Swift 中的工作方式完全相同。这里的 Objective-C 示例可以直接转换。
{{% /details %}}

{{% details title="这可以用于视频流媒体吗？" closed="true" %}}
可以。`AVAssetResourceLoaderDelegate` 适用于 AVPlayer 支持的任何媒体类型，包括视频。同样的自定义方案方法同样适用。
{{% /details %}}

{{% details title="这是否支持后台音频播放？" closed="true" %}}
是的，只要你在应用的功能中启用了"Audio, AirPlay, and Picture in Picture"后台模式，并正确配置了 `AVAudioSession`。
{{% /details %}}
