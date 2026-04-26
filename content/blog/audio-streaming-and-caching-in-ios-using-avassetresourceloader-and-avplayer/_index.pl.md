---
title: "Strumieniowanie audio iOS z AVAssetResourceLoader"
date: 2015-06-20
description: "Dowiedz się, jak strumieniować i buforować audio w iOS za pomocą AVAssetResourceLoaderDelegate i AVPlayer z niestandardowymi schematami URL i pamięcią podręczną na dysku."
keywords: ["strumieniowanie audio iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "poradnik AVPlayer", "AVFoundation audio", "AVAssetResourceLoadingRequest", "niestandardowy odtwarzacz audio iOS", "strumieniowanie audio z chmury iOS", "buforowanie audio iOS", "Swift AVPlayer niestandardowy schemat"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**TL;DR:** Użyj `AVAssetResourceLoaderDelegate` z niestandardowym schematem URL, aby przechwytywać ładowanie zasobów przez AVPlayer. Pozwala to dodawać niestandardowe nagłówki autoryzacji dla usług chmurowych, buforować audio na dysku i kontrolować zachowanie strumieniowania — bez konieczności pisania lokalnego proxy HTTP. Pełny kod źródłowy dostępny jest na [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Dlaczego AVPlayer potrzebuje niestandardowego ładowarki zasobów

`AVPlayer` odtwarza audio z plików lokalnych i zdalnych adresów URL. W przypadku większości usług chmurowych (Dropbox, Google Drive, Box) możesz przekazać bezpośredni URL pobierania, a odtwarzanie działa od razu.

Jednak niektóre usługi, takie jak **Yandex.Disk** i **WebDAV**, wymagają niestandardowych nagłówków autoryzacji w żądaniach GET. `AVPlayer` nie zapewnia wbudowanego sposobu na ich wstrzyknięcie.

Rozwiązanie: użyj właściwości `resourceLoader` klasy `AVURLAsset`. Ten interfejs API przechwytuje żądania ładowania zasobów, działając jak lokalne proxy HTTP bez związanej z tym złożoności.

### Jak to działa

`AVPlayer` używa `resourceLoader`, gdy nie rozpoznaje schematu URL. Zastępując `https://` niestandardowym schematem (np. `customscheme://`), zmuszasz AVPlayer do delegowania całego ładowania do Twojej aplikacji.

Musisz zaimplementować dwie metody `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- wywoływana, gdy AVPlayer potrzebuje danych. Zapisz `AVAssetResourceLoadingRequest` i uruchom operację ładowania danych.
2. **`resourceLoader:didCancelLoadingRequest:`** -- wywoływana, gdy żądanie zostanie anulowane lub zastąpione.

## Jak stworzyć niestandardowy AVPlayer

Skonfiguruj AVPlayer z niestandardowym schematem URL:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Ten kod:
- Definiuje URL z Twoim niestandardowym schematem
- Tworzy `AVURLAsset` z delegatem na głównej kolejce
- Buduje `AVPlayerItem` z zasobu
- Inicjalizuje `AVPlayer`

## Implementacja delegata ładowarki zasobów

Utwórz klasę o nazwie `LSFilePlayerResourceLoader` do obsługi pobierania danych z serwera i przekazywania ich z powrotem do `AVURLAsset`. Przechowuj instancje ładowarki w słowniku kluczowanym przez URL zasobu.

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

Te metody sprawdzają schemat URL, tworzą lub pobierają ładowarkę i dodają żądanie do kolejki ładowarki. Nierozpoznane schematy zwracają `NO`.

## Interfejs LSFilePlayerResourceLoader

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

## Ładowanie danych: proces dwuetapowy

Gdy żądanie ładowania trafia do kolejki, wykonywane są sekwencyjnie dwie operacje:

- **contentInfoOperation** -- pobiera długość zawartości, typ MIME i obsługę zakresów bajtów
- **dataOperation** -- pobiera dane pliku począwszy od `requestedOffset`

## Strategia buforowania na dysku

Pobrane dane są zapisywane do tymczasowego pliku na dysku. Kolejne żądania dotyczące tej samej zawartości są obsługiwane z tej pamięci podręcznej, co pozwala uniknąć zbędnych wywołań sieciowych. Takie podejście:

- Zmniejsza zużycie przepustowości
- Umożliwia niemal natychmiastowe ponowne odtwarzanie
- Obsługuje operacje przewijania w buforowanych zakresach

## Przetwarzanie oczekujących żądań

Metoda `processPendingRequests` wypełnia `contentInformationRequest` każdego żądania metadanymi i dostarcza buforowane zakresy bajtów. Ukończone żądania są usuwane z kolejki.

## Kod źródłowy i następne kroki

Ten poradnik przedstawia ogólne omówienie implementacji `AVAssetResourceLoaderDelegate` do strumieniowania audio z chmury z niestandardowymi nagłówkami autoryzacji. Pełny kod źródłowy dostępny jest na [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

To podejście napędza silnik strumieniowania audio w [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), który strumieniuje muzykę z Dropbox, Google Drive, OneDrive, Yandex.Disk i innych usług chmurowych na iOS i macOS.

## Często zadawane pytania

{{% details title="Kiedy powinienem używać AVAssetResourceLoaderDelegate zamiast bezpośredniego URL?" closed="true" %}}
Użyj go, gdy usługa chmurowa wymaga niestandardowych nagłówków autoryzacji, gdy potrzebujesz buforowania na dysku dla strumieniowanego audio lub gdy chcesz mieć szczegółową kontrolę nad tym, jak dane są ładowane i buforowane.
{{% /details %}}

{{% details title="Czy to podejście działa ze Swift?" closed="true" %}}
Tak. Protokół `AVAssetResourceLoaderDelegate` działa w taki sam sposób w Swift. Przykłady w Objective-C przekładają się bezpośrednio.
{{% /details %}}

{{% details title="Czy mogę tego używać również do strumieniowania wideo?" closed="true" %}}
Tak. `AVAssetResourceLoaderDelegate` działa z każdym typem mediów obsługiwanym przez AVPlayer, w tym z wideo. To samo podejście z niestandardowym schematem ma zastosowanie.
{{% /details %}}

{{% details title="Czy to obsługuje odtwarzanie audio w tle?" closed="true" %}}
Tak, pod warunkiem że włączysz tryb tła „Audio, AirPlay i Obraz w obrazie" w możliwościach aplikacji i poprawnie skonfigurujesz `AVAudioSession`.
{{% /details %}}
