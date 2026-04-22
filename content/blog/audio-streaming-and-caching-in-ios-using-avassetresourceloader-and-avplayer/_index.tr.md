---
title: "AVAssetResourceLoader ile iOS Ses Akışı"
date: 2015-06-20
description: "Özel URL şemaları ve disk önbelleği kullanarak AVAssetResourceLoaderDelegate ve AVPlayer ile iOS'ta ses akışı ve önbelleğe almanın nasıl yapılacağını öğrenin."
keywords: ["iOS ses akışı", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer eğitimi", "AVFoundation ses", "AVAssetResourceLoadingRequest", "özel ses oynatıcı iOS", "bulut ses akışı iOS", "ses önbelleği iOS", "Swift AVPlayer özel şema"]
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

**TL;DR:** AVPlayer'ın kaynak yüklemesini durdurmak için özel bir URL şemasıyla `AVAssetResourceLoaderDelegate` kullanın. Bu, bulut hizmetleri için özel yetkilendirme başlıkları eklemenizi, sesi diske önbelleğe almanızı ve yerel bir HTTP proxy yazmadan akış davranışını kontrol etmenizi sağlar. Tam kaynak kodu [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader) üzerindedir.

---

## AVPlayer Neden Özel Bir Resource Loader'a İhtiyaç Duyar

`AVPlayer`, yerel dosyalardan ve uzak URL'lerden ses çalar. Çoğu bulut hizmeti (Dropbox, Google Drive, Box) için doğrudan bir indirme URL'si verebilirsiniz ve oynatma kutudan çıkar çıkmaz çalışır.

Ancak **Yandex.Disk** ve **WebDAV** gibi bazı hizmetler, GET isteklerinde özel yetkilendirme başlıkları gerektirir. `AVPlayer`, bu başlıkları yerleştirmek için yerleşik bir yol sunmaz.

Çözüm: `AVURLAsset`'in `resourceLoader` özelliğini kullanın. Bu API, kaynak yükleme isteklerini durdurarak karmaşıklık olmadan yerel bir HTTP proxy gibi davranır.

### Nasıl Çalışır

`AVPlayer`, URL şemasını tanımadığında `resourceLoader`'ı kullanır. `https://`'yi özel bir şemayla değiştirerek (ör. `customscheme://`) AVPlayer'ı tüm yüklemeyi uygulamanıza devretmeye zorlarsınız.

İki `AVAssetResourceLoaderDelegate` metodunu uygulamanız gerekir:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- AVPlayer veri ihtiyaç duyduğunda çağrılır. `AVAssetResourceLoadingRequest`'i kaydedin ve veri yükleme işleminizi başlatın.
2. **`resourceLoader:didCancelLoadingRequest:`** -- bir istek iptal edildiğinde veya değiştirildiğinde çağrılır.

## Özel AVPlayer Nasıl Oluşturulur

Özel bir URL şemasıyla AVPlayer'ı kurun:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Bu kod:
- Özel şemanızla bir URL tanımlar
- Ana kuyrukta bir delegate ile `AVURLAsset` oluşturur
- Asset'ten bir `AVPlayerItem` oluşturur
- `AVPlayer`'ı başlatır

## Resource Loader Delegate'in Uygulanması

Sunucudan veri çekme ve bunu `AVURLAsset`'e geri iletme işlemlerini yönetmek için `LSFilePlayerResourceLoader` adlı bir sınıf oluşturun. Loader örneklerini, kaynak URL'sine göre anahtar kullanan bir sözlükte saklayın.

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

Bu metodlar URL şemasını kontrol eder, bir loader oluşturur veya alır ve isteği loader'ın kuyruğuna ekler. Tanınmayan şemalar `NO` döndürür.

## LSFilePlayerResourceLoader Arayüzü

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

## Veri Yükleme: İki Adımlı Süreç

Bir yükleme isteği kuyruğa girdiğinde, sırayla iki işlem gerçekleştirilir:

- **contentInfoOperation** -- içerik uzunluğunu, MIME türünü ve bayt aralığı desteğini sorgular
- **dataOperation** -- `requestedOffset`'ten başlayarak dosya verilerini getirir

## Disk Önbelleğe Alma Stratejisi

İndirilen veriler diskteki geçici bir dosyaya yazılır. Aynı içerik için sonraki istekler bu önbellekten karşılanır ve gereksiz ağ çağrıları önlenir. Bu yaklaşım:

- Bant genişliği kullanımını azaltır
- Neredeyse anında tekrar oynatmayı sağlar
- Önbelleğe alınmış aralıklar içinde arama işlemlerini destekler

## Bekleyen İsteklerin İşlenmesi

`processPendingRequests` metodu, her isteğin `contentInformationRequest`'ini meta verilerle doldurur ve önbelleğe alınmış bayt aralıklarını teslim eder. Tamamlanan istekler kuyruktan kaldırılır.

## Kaynak Kodu ve Sonraki Adımlar

Bu eğitim, özel yetkilendirme başlıklarıyla bulut ses akışı için `AVAssetResourceLoaderDelegate` uygulamasına üst düzey bir genel bakış sunar. Tam kaynak kodu [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader) üzerinde mevcuttur.

Bu yaklaşım, iOS ve macOS'ta Dropbox, Google Drive, OneDrive, Yandex.Disk ve diğer bulut hizmetlerinden müzik akışı yapan [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198)'teki ses akışı motorunu güçlendirmektedir.

## Sıkça Sorulan Sorular

{{% details title="AVAssetResourceLoaderDelegate'i doğrudan URL yerine ne zaman kullanmalıyım?" closed="true" %}}
Bulut hizmeti özel yetkilendirme başlıkları gerektirdiğinde, akışlı ses için disk önbelleğine ihtiyaç duyduğunuzda veya verinin nasıl yüklenip arabelleğe alındığı konusunda ayrıntılı kontrol istediğinizde kullanın.
{{% /details %}}

{{% details title="Bu yaklaşım Swift ile çalışır mı?" closed="true" %}}
Evet. `AVAssetResourceLoaderDelegate` protokolü Swift'te aynı şekilde çalışır. Buradaki Objective-C örnekleri doğrudan çevrilebilir.
{{% /details %}}

{{% details title="Bunu video akışı için de kullanabilir miyim?" closed="true" %}}
Evet. `AVAssetResourceLoaderDelegate`, video dahil AVPlayer'ın desteklediği tüm medya türleriyle çalışır. Aynı özel şema yaklaşımı geçerlidir.
{{% /details %}}

{{% details title="Bu arka plan ses çalmayı destekliyor mu?" closed="true" %}}
Evet, uygulamanızın yeteneklerinde "Audio, AirPlay ve Picture in Picture" arka plan modunu etkinleştirdiğiniz ve `AVAudioSession`'ı doğru şekilde yapılandırdığınız sürece.
{{% /details %}}
