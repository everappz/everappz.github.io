# Audio Streaming and Caching in iOS using AVAssetResourceLoader and AVPlayer

![Audio Streaming and Caching in iOS using AVAssetResourceLoader and AVPlayer Scheme](21260c_cdf2746eb77b4dec82748f80dde7f13b~mv2.png)

## How to Use AVAssetResourceLoaderDelegate with Example App

Welcome to this tutorial where you'll learn how to harness the power of AVAssetResourceLoaderDelegate with a real-life example from our app, Evermusic 1.5. We recently introduced the ability to stream music from Yandex.Disk and Web Dav, in addition to Dropbox and Google Drive. If you're curious about how we implemented these services in Evermusic and how you can utilize AVAssetResourceLoader and AVPlayer in your own apps, read on.

## Understanding AVPlayer and Resource Loading

AVPlayer is a versatile tool for playing audio files from both local storage and remote hosts. To stream audio from a cloud service, you'd typically need a direct URL to the file and initialize AVPlayer with that URL. This method works for many cloud services like Dropbox, Box, and Google Drive. However, it falls short when playing audio from Yandex.Disk and Web Dav due to the authorization header required for GET requests. Unfortunately, AVPlayer doesn't offer a direct way to handle this.

So, we explored a solution and stumbled upon the resourceLoader object in AVURLAsset. This nifty API allows controlled access to remote files for AVPlayer, acting like a local HTTP proxy without the complexity.

The key insight here is that AVPlayer leverages resourceLoader when it doesn't know how to load a resource. We trick AVPlayer by changing the protocol, forcing it to delegate resource loading to our app. To achieve this, you'll need to implement two AVAssetResourceLoaderDelegate methods:

1. `resourceLoader:shouldWaitForLoadingOfRequestedResource:`: This method is called when the application's assistance is required to load a resource. Here, we save AVAssetResourceLoadingRequest and start data loading operations.

2. `resourceLoader:didCancelLoadingRequest:`: This method is invoked when data from the resource is no longer needed or when a loading request is superseded by newer requests.

## Creating Your Custom AVPlayer

Now, let's create a custom AVPlayer using a different scheme:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:playerItem];
[self addObserversForPlayer];
```

These lines define a custom URL with your scheme, set up an AVURLAsset with a delegate on the main queue, create an AVPlayerItem from the asset, and finally, initialize an AVPlayer.

## Custom Resource Loader

Next, create a custom class, such as LSFilePlayerResourceLoader, responsible for loading data from the server and passing it back to AVURLAsset. This class should have two parameters in its init method: the requested file URL and an object (e.g., YDSession) responsible for fetching data from the cloud server.

You'll store LSFilePlayerResourceLoader objects in a dictionary, using the resource URL as the key. The AVAssetResourceLoaderDelegate implementation will look like this:

```objc
- (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest *)loadingRequest {
    NSURL *resourceURL = [loadingRequest.request URL];
    if ([resourceURL.scheme isEqualToString:@"customscheme"]) {
        LSFilePlayerResourceLoader *loader = [self resourceLoaderForRequest:loadingRequest];
        if (loader == nil) {
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

These methods check the resourceURL scheme, get or create an LSFilePlayerResourceLoader, and add the loading request to the loader. If the scheme is not recognized, it returns NO.

The LSFilePlayerResourceLoader interface should look like this:

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

This interface provides methods for managing requests in the loader queue and defines delegate methods for handling resource loading status.

## Data Loading Operations

Now, when you add a loading request to the queue, it's saved in the pendingRequests array, and a data loading operation starts. This operation involves two steps: contentInfoOperation and dataOperation.

- `contentInfoOperation`: Identifies content length, content type, and whether the resource supports byte range requests. AVPlayer can optimize playback with byte range requests.

- `dataOperation`: Loads file data with an offset, utilizing requested data offset from AVAssetResourceLoadingDataRequest.

## Data Caching

Data received from the server is cached on disk, and a temporary file is used for this purpose. When data is needed, it's read from the cache.

## Processing Pending Requests

In the `processPendingRequests` method, content information is filled in, and cached data is written. Once all requested data is received, pending requests are removed from the queue.

This should give you a solid foundation for implementing AVAssetResourceLoaderDelegate with your app, specifically for streaming audio from cloud services that require custom handling of authorization headers.

Please note that this is a complex and detailed topic, and this tutorial provides a high-level overview. The source code mentioned in the tutorial is available on [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader) for further reference and exploration.

---

**Tags:** streaming, AVURLAsset, iOS, SDK, AVAssetResourceLoader, Framework, AVAssetResourceLoadingRequest, AVPlayer, AVFoundation

**Category:** Development