---
title: "iOS AVAssetResourceLoader를 활용한 오디오 스트리밍"
date: 2015-06-20
description: "AVAssetResourceLoaderDelegate와 AVPlayer를 사용하여 커스텀 URL 스킴과 디스크 캐싱으로 iOS에서 오디오를 스트리밍하고 캐싱하는 방법을 알아보세요."
keywords: ["iOS 오디오 스트리밍", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer 튜토리얼", "AVFoundation 오디오", "AVAssetResourceLoadingRequest", "커스텀 오디오 플레이어 iOS", "클라우드 오디오 스트리밍 iOS", "오디오 캐싱 iOS", "Swift AVPlayer 커스텀 스킴"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
draft: false
aliases:
  - /post/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
  - /amp/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
  - /single-post/Audio-Streaming-and-Caching-in-iOS-using-AVAssetResourceLoader-and-AVPlayer/
  - /index.php/2015/02/10/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**요약:** 커스텀 URL 스킴과 함께 `AVAssetResourceLoaderDelegate`를 사용하여 AVPlayer의 리소스 로딩을 가로채세요. 이를 통해 클라우드 서비스를 위한 커스텀 인증 헤더를 추가하고, 오디오를 디스크에 캐싱하며, 로컬 HTTP 프록시 없이 스트리밍 동작을 제어할 수 있습니다. 전체 소스 코드는 [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader)에 있습니다.

---

## AVPlayer에 커스텀 리소스 로더가 필요한 이유

`AVPlayer`는 로컬 파일과 원격 URL에서 오디오를 재생합니다. 대부분의 클라우드 서비스(Dropbox, Google Drive, Box)에서는 직접 다운로드 URL을 전달하면 재생이 바로 작동합니다.

그러나 **Yandex.Disk**와 **WebDAV** 같은 일부 서비스는 GET 요청에 커스텀 인증 헤더를 필요로 합니다. `AVPlayer`는 이러한 헤더를 삽입할 수 있는 내장 방법을 제공하지 않습니다.

해결책: `AVURLAsset`의 `resourceLoader` 속성을 사용하세요. 이 API는 리소스 로딩 요청을 가로채며, 복잡한 과정 없이 로컬 HTTP 프록시처럼 동작합니다.

### 작동 원리

`AVPlayer`는 URL 스킴을 인식하지 못할 때 `resourceLoader`를 사용합니다. `https://`를 커스텀 스킴(예: `customscheme://`)으로 교체하면 AVPlayer가 모든 로딩을 앱에 위임하도록 강제할 수 있습니다.

두 가지 `AVAssetResourceLoaderDelegate` 메서드를 구현해야 합니다:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- AVPlayer가 데이터를 필요로 할 때 호출됩니다. `AVAssetResourceLoadingRequest`를 저장하고 데이터 로딩 작업을 시작하세요.
2. **`resourceLoader:didCancelLoadingRequest:`** -- 요청이 취소되거나 대체될 때 호출됩니다.

## 커스텀 AVPlayer 생성 방법

커스텀 URL 스킴으로 AVPlayer를 설정하세요:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

이 코드는:
- 커스텀 스킴으로 URL을 정의합니다
- 메인 큐에 델리게이트를 가진 `AVURLAsset`을 생성합니다
- 에셋에서 `AVPlayerItem`을 빌드합니다
- `AVPlayer`를 초기화합니다

## 리소스 로더 델리게이트 구현

서버에서 데이터를 가져와 `AVURLAsset`에 전달하는 `LSFilePlayerResourceLoader` 클래스를 생성하세요. 리소스 URL을 키로 하는 딕셔너리에 로더 인스턴스를 저장하세요.

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

이 메서드들은 URL 스킴을 확인하고, 로더를 생성하거나 가져와서 요청을 로더의 큐에 추가합니다. 인식되지 않는 스킴은 `NO`를 반환합니다.

## LSFilePlayerResourceLoader 인터페이스

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

## 데이터 로딩: 두 단계 프로세스

로딩 요청이 큐에 들어오면 두 가지 작업이 순서대로 실행됩니다:

- **contentInfoOperation** -- 콘텐츠 길이, MIME 타입, 바이트 범위 지원을 조회합니다
- **dataOperation** -- `requestedOffset`에서 시작하는 파일 데이터를 가져옵니다

## 디스크 캐싱 전략

다운로드된 데이터는 디스크의 임시 파일에 기록됩니다. 동일한 콘텐츠에 대한 후속 요청은 이 캐시에서 처리되어 불필요한 네트워크 호출을 방지합니다. 이 방식은:

- 대역폭 사용량을 줄입니다
- 거의 즉각적인 재생을 가능하게 합니다
- 캐시된 범위 내에서 탐색 작업을 지원합니다

## 대기 중인 요청 처리

`processPendingRequests` 메서드는 각 요청의 `contentInformationRequest`를 메타데이터로 채우고 캐시된 바이트 범위를 전달합니다. 완료된 요청은 큐에서 제거됩니다.

## 소스 코드 및 다음 단계

이 튜토리얼은 커스텀 인증 헤더를 사용한 클라우드 오디오 스트리밍을 위한 `AVAssetResourceLoaderDelegate` 구현의 개요를 제공합니다. 전체 소스 코드는 [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader)에서 확인할 수 있습니다.

이 방식은 iOS 및 macOS에서 Dropbox, Google Drive, OneDrive, Yandex.Disk 및 기타 클라우드 서비스의 음악을 스트리밍하는 [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198)의 오디오 스트리밍 엔진을 지원합니다.

## 자주 묻는 질문

{{% details title="직접 URL 대신 AVAssetResourceLoaderDelegate를 언제 사용해야 하나요?" closed="true" %}}
클라우드 서비스에 커스텀 인증 헤더가 필요한 경우, 스트리밍 오디오의 디스크 캐싱이 필요한 경우, 또는 데이터가 로드되고 버퍼링되는 방식을 세밀하게 제어하려는 경우에 사용하세요.
{{% /details %}}

{{% details title="이 방식이 Swift에서도 작동하나요?" closed="true" %}}
네. `AVAssetResourceLoaderDelegate` 프로토콜은 Swift에서도 동일하게 작동합니다. 여기의 Objective-C 예제는 직접 변환할 수 있습니다.
{{% /details %}}

{{% details title="동영상 스트리밍에도 사용할 수 있나요?" closed="true" %}}
네. `AVAssetResourceLoaderDelegate`는 동영상을 포함하여 AVPlayer가 지원하는 모든 미디어 타입에서 작동합니다. 동일한 커스텀 스킴 방식이 적용됩니다.
{{% /details %}}

{{% details title="백그라운드 오디오 재생을 지원하나요?" closed="true" %}}
네. 앱의 기능에서 "오디오, AirPlay 및 PiP" 백그라운드 모드를 활성화하고 `AVAudioSession`을 올바르게 구성하기만 하면 됩니다.
{{% /details %}}
