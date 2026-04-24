---
title: "Phát trực tuyến âm thanh iOS với AVAssetResourceLoader"
date: 2015-06-20
description: "Tìm hiểu cách phát trực tuyến và lưu bộ nhớ đệm âm thanh trong iOS bằng AVAssetResourceLoaderDelegate và AVPlayer với các URL scheme tùy chỉnh và bộ nhớ đệm đĩa."
keywords: ["phát trực tuyến âm thanh iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "hướng dẫn AVPlayer", "AVFoundation âm thanh", "AVAssetResourceLoadingRequest", "trình phát âm thanh tùy chỉnh iOS", "phát trực tuyến âm thanh đám mây iOS", "lưu bộ nhớ đệm âm thanh iOS", "Swift AVPlayer scheme tùy chỉnh"]
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

**TL;DR:** Sử dụng `AVAssetResourceLoaderDelegate` với URL scheme tùy chỉnh để chặn việc tải tài nguyên của AVPlayer. Điều này cho phép bạn thêm header ủy quyền tùy chỉnh cho các dịch vụ đám mây, lưu bộ nhớ đệm âm thanh vào đĩa và kiểm soát hành vi phát trực tuyến -- tất cả mà không cần viết một proxy HTTP cục bộ. Mã nguồn đầy đủ có trên [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Tại sao AVPlayer cần bộ tải tài nguyên tùy chỉnh

`AVPlayer` phát âm thanh từ tệp cục bộ và URL từ xa. Đối với hầu hết các dịch vụ đám mây (Dropbox, Google Drive, Box), bạn có thể truyền URL tải xuống trực tiếp và phát lại hoạt động ngay lập tức.

Tuy nhiên, một số dịch vụ như **Yandex.Disk** và **WebDAV** yêu cầu header ủy quyền tùy chỉnh trong các yêu cầu GET. `AVPlayer` không cung cấp cách tích hợp sẵn để chèn các header này.

Giải pháp: sử dụng thuộc tính `resourceLoader` của `AVURLAsset`. API này chặn các yêu cầu tải tài nguyên, hoạt động như một proxy HTTP cục bộ mà không có sự phức tạp.

### Cách hoạt động

`AVPlayer` sử dụng `resourceLoader` khi không nhận ra URL scheme. Bằng cách thay `https://` bằng scheme tùy chỉnh (ví dụ: `customscheme://`), bạn buộc AVPlayer ủy quyền toàn bộ việc tải cho ứng dụng của mình.

Bạn cần triển khai hai phương thức `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- được gọi khi AVPlayer cần dữ liệu. Lưu `AVAssetResourceLoadingRequest` và bắt đầu thao tác tải dữ liệu.
2. **`resourceLoader:didCancelLoadingRequest:`** -- được gọi khi một yêu cầu bị hủy hoặc được thay thế.

## Cách tạo AVPlayer tùy chỉnh

Thiết lập AVPlayer với URL scheme tùy chỉnh:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Đoạn mã này:
- Định nghĩa URL với scheme tùy chỉnh
- Tạo `AVURLAsset` với delegate trên hàng đợi chính
- Xây dựng `AVPlayerItem` từ asset
- Khởi tạo `AVPlayer`

## Triển khai delegate của bộ tải tài nguyên

Tạo lớp `LSFilePlayerResourceLoader` để xử lý việc tải dữ liệu từ máy chủ và truyền lại cho `AVURLAsset`. Lưu các thể hiện của bộ tải trong từ điển được khóa theo URL tài nguyên.

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

Các phương thức này kiểm tra URL scheme, tạo hoặc lấy bộ tải, và thêm yêu cầu vào hàng đợi. Các scheme không được nhận dạng trả về `NO`.

## Giao diện LSFilePlayerResourceLoader

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

## Tải dữ liệu: Quy trình hai bước

Khi một yêu cầu tải vào hàng đợi, hai thao tác được thực hiện tuần tự:

- **contentInfoOperation** -- truy vấn độ dài nội dung, loại MIME và hỗ trợ byte-range
- **dataOperation** -- lấy dữ liệu tệp bắt đầu từ `requestedOffset`

## Chiến lược lưu bộ nhớ đệm đĩa

Dữ liệu đã tải được ghi vào tệp tạm thời trên đĩa. Các yêu cầu tiếp theo cho cùng nội dung được phục vụ từ bộ nhớ đệm này, tránh các lần gọi mạng dư thừa. Cách tiếp cận này:

- Giảm mức sử dụng băng thông
- Cho phép phát lại gần như tức thì
- Hỗ trợ thao tác tua trong các phạm vi đã lưu bộ nhớ đệm

## Xử lý các yêu cầu đang chờ

Phương thức `processPendingRequests` điền `contentInformationRequest` của mỗi yêu cầu với siêu dữ liệu và phân phối các phạm vi byte đã lưu bộ nhớ đệm. Các yêu cầu đã hoàn thành được xóa khỏi hàng đợi.

## Mã nguồn và các bước tiếp theo

Hướng dẫn này cung cấp tổng quan về việc triển khai `AVAssetResourceLoaderDelegate` để phát trực tuyến âm thanh đám mây với header ủy quyền tùy chỉnh. Mã nguồn đầy đủ có trên [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Phương pháp này hỗ trợ engine phát trực tuyến âm thanh trong [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), ứng dụng phát nhạc từ Dropbox, Google Drive, OneDrive, Yandex.Disk và các dịch vụ đám mây khác trên iOS và macOS.

## Câu hỏi thường gặp

{{% details title="Khi nào nên dùng AVAssetResourceLoaderDelegate thay vì URL trực tiếp?" closed="true" %}}
Sử dụng khi dịch vụ đám mây yêu cầu header ủy quyền tùy chỉnh, khi bạn cần lưu bộ nhớ đệm đĩa cho âm thanh phát trực tuyến, hoặc khi bạn muốn kiểm soát chi tiết cách dữ liệu được tải và đệm.
{{% /details %}}

{{% details title="Cách tiếp cận này có hoạt động với Swift không?" closed="true" %}}
Có. Giao thức `AVAssetResourceLoaderDelegate` hoạt động theo cách tương tự trong Swift. Các ví dụ Objective-C ở đây có thể dịch trực tiếp.
{{% /details %}}

{{% details title="Tôi có thể dùng điều này cho phát trực tuyến video không?" closed="true" %}}
Có. `AVAssetResourceLoaderDelegate` hoạt động với bất kỳ loại phương tiện nào mà AVPlayer hỗ trợ, bao gồm cả video. Cách tiếp cận scheme tùy chỉnh tương tự cũng áp dụng.
{{% /details %}}

{{% details title="Điều này có hỗ trợ phát lại âm thanh nền không?" closed="true" %}}
Có, miễn là bạn bật chế độ nền "Audio, AirPlay, and Picture in Picture" trong khả năng của ứng dụng và cấu hình `AVAudioSession` đúng cách.
{{% /details %}}
