---
title: "Streamování zvuku v iOS pomocí AVAssetResourceLoader"
date: 2015-06-20
description: "Naučte se, jak streamovat a ukládat zvuk do mezipaměti v iOS pomocí AVAssetResourceLoaderDelegate a AVPlayer s vlastními schématy URL a ukládáním na disk."
keywords: ["streamování zvuku iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "tutoriál AVPlayer", "zvuk AVFoundation", "AVAssetResourceLoadingRequest", "vlastní audio přehrávač iOS", "cloudové streamování zvuku iOS", "ukládání zvuku do mezipaměti iOS", "Swift AVPlayer vlastní schéma"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
draft: false
aliases:
  - /post/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
  - /single-post/Audio-Streaming-and-Caching-in-iOS-using-AVAssetResourceLoader-and-AVPlayer/
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**Stručně:** Použijte `AVAssetResourceLoaderDelegate` s vlastním schématem URL k zachycení načítání zdrojů AVPlayeru. To vám umožní přidat vlastní autorizační hlavičky pro cloudové služby, ukládat zvuk do mezipaměti na disk a řídit chování streamování -- vše bez nutnosti psát lokální HTTP proxy. Úplný zdrojový kód je k dispozici na [GitHubu](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Proč AVPlayer potřebuje vlastní zavaděč zdrojů

`AVPlayer` přehrává zvuk z lokálních souborů a vzdálených URL. U většiny cloudových služeb (Dropbox, Google Drive, Box) stačí předat přímou URL ke stažení a přehrávání funguje okamžitě.

Některé služby jako **Yandex.Disk** a **WebDAV** však vyžadují vlastní autorizační hlavičky v GET požadavcích. `AVPlayer` neposkytuje žádný vestavěný způsob, jak tyto hlavičky vložit.

Řešení: použijte vlastnost `resourceLoader` třídy `AVURLAsset`. Toto API zachytává požadavky na načítání zdrojů a funguje jako lokální HTTP proxy bez obvyklé složitosti.

### Jak to funguje

`AVPlayer` používá `resourceLoader`, pokud nerozpozná schéma URL. Nahrazením `https://` vlastním schématem (např. `customscheme://`) donutíte AVPlayer delegovat veškeré načítání na vaši aplikaci.

Musíte implementovat dvě metody `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- volána, když AVPlayer potřebuje data. Uložte `AVAssetResourceLoadingRequest` a spusťte svou operaci načítání dat.
2. **`resourceLoader:didCancelLoadingRequest:`** -- volána, když je požadavek zrušen nebo nahrazen.

## Jak vytvořit vlastní AVPlayer

Nastavte AVPlayer s vlastním schématem URL:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Tento kód:
- Definuje URL s vaším vlastním schématem
- Vytvoří `AVURLAsset` s delegátem na hlavní frontě
- Sestaví `AVPlayerItem` z assetu
- Inicializuje `AVPlayer`

## Implementace delegáta zavaděče zdrojů

Vytvořte třídu `LSFilePlayerResourceLoader` pro načítání dat ze serveru a jejich předání zpět do `AVURLAsset`. Instance zavaděče ukládejte do slovníku indexovaného URL zdrojem.

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

Tyto metody zkontrolují schéma URL, vytvoří nebo načtou zavaděč a přidají požadavek do fronty zavaděče. Nerozpoznaná schémata vrátí `NO`.

## Rozhraní LSFilePlayerResourceLoader

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

## Načítání dat: dvoustupňový proces

Když požadavek na načtení vstoupí do fronty, provedou se dvě operace v pořadí:

- **contentInfoOperation** -- dotazuje se na délku obsahu, typ MIME a podporu rozsahu bajtů
- **dataOperation** -- načítá data souboru počínaje `requestedOffset`

## Strategie ukládání do mezipaměti na disk

Stažená data jsou zapsána do dočasného souboru na disku. Následné požadavky na stejný obsah jsou obsluhovány z této mezipaměti, čímž se zabraňuje redundantním síťovým voláním. Tento přístup:

- Snižuje využití šířky pásma
- Umožňuje téměř okamžité opakované přehrávání
- Podporuje operace vyhledávání v rámci uložených rozsahů

## Zpracování čekajících požadavků

Metoda `processPendingRequests` naplní `contentInformationRequest` každého požadavku metadaty a doručí uložené rozsahy bajtů. Dokončené požadavky jsou odstraněny z fronty.

## Zdrojový kód a další kroky

Tento tutoriál poskytuje přehled vysoké úrovně implementace `AVAssetResourceLoaderDelegate` pro cloudové streamování zvuku s vlastními autorizačními hlavičkami. Úplný zdrojový kód je dostupný na [GitHubu](http://github.com/leshkoapps/AVAssetResourceLoader).

Tento přístup pohání engine pro streamování zvuku v aplikaci [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), která streamuje hudbu z Dropboxu, Google Drive, OneDrive, Yandex.Disku a dalších cloudových služeb na iOS a macOS.

## Nejčastější dotazy

{{% details title="Kdy bych měl použít AVAssetResourceLoaderDelegate místo přímé URL?" closed="true" %}}
Použijte jej, když cloudová služba vyžaduje vlastní autorizační hlavičky, když potřebujete ukládání streamovaného zvuku do mezipaměti na disk, nebo když chcete podrobnou kontrolu nad tím, jak jsou data načítána a ukládána do bufferu.
{{% /details %}}

{{% details title="Funguje tento přístup se Swiftem?" closed="true" %}}
Ano. Protokol `AVAssetResourceLoaderDelegate` funguje v Swiftu stejně. Příklady v Objective-C zde se přímo přeloží.
{{% /details %}}

{{% details title="Mohu to použít i pro streamování videa?" closed="true" %}}
Ano. `AVAssetResourceLoaderDelegate` funguje s jakýmkoli typem médií, který AVPlayer podporuje, včetně videa. Použije se stejný přístup s vlastním schématem.
{{% /details %}}

{{% details title="Podporuje přehrávání zvuku na pozadí?" closed="true" %}}
Ano, pokud povolíte režim pozadí "Audio, AirPlay, and Picture in Picture" v možnostech vaší aplikace a správně nakonfigurujete `AVAudioSession`.
{{% /details %}}
