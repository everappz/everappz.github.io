---
title: "iOS Audio Streaming AVAssetResourceLoader segítségével"
date: 2015-06-20
description: "Ismerje meg, hogyan streamelhető és gyorsítótárazható az audio iOS rendszeren az AVAssetResourceLoaderDelegate és az AVPlayer segítségével egyéni URL-sémákkal és lemezgyorsítótárral."
keywords: ["iOS audio streaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer útmutató", "AVFoundation audio", "AVAssetResourceLoadingRequest", "egyéni audio lejátszó iOS", "felhő audio streaming iOS", "audio gyorsítótárazás iOS", "Swift AVPlayer egyéni séma"]
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

**TL;DR:** Használja az `AVAssetResourceLoaderDelegate`-t egyéni URL-sémával az AVPlayer erőforrás-betöltésének elfogásához. Ez lehetővé teszi egyéni engedélyezési fejlécek hozzáadását felhőszolgáltatásokhoz, az audio lemezre való gyorsítótárazását és a streaming viselkedés vezérlését -- mindezt helyi HTTP proxy nélkül. A teljes forráskód elérhető a [GitHubon](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Miért van szüksége az AVPlayernek egyéni erőforrás-betöltőre?

Az `AVPlayer` helyi fájlokból és távoli URL-ekből játszik le hangot. A legtöbb felhőszolgáltatásnál (Dropbox, Google Drive, Box) elegendő egy közvetlen letöltési URL-t megadni, és a lejátszás azonnal működik.

Egyes szolgáltatások, mint a **Yandex.Disk** és a **WebDAV**, azonban egyéni engedélyezési fejléceket igényelnek a GET kérésekben. Az `AVPlayer` nem biztosít beépített megoldást ezek hozzáadásához.

A megoldás: használja az `AVURLAsset` `resourceLoader` tulajdonságát. Ez az API elfogja az erőforrás-betöltési kéréseket, és helyi HTTP proxyként működik anélkül, hogy annak bonyolultságát hordozná.

### Hogyan működik?

Az `AVPlayer` a `resourceLoader`-t használja, ha nem ismeri fel az URL-sémát. Az `https://` helyére egyéni sémát helyezve (pl. `customscheme://`) az AVPlayer az összes betöltést az alkalmazásra delegálja.

Két `AVAssetResourceLoaderDelegate` metódust kell megvalósítani:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- akkor hívódik meg, amikor az AVPlayernek adatra van szüksége. Mentse el az `AVAssetResourceLoadingRequest`-et, és indítsa el az adatbetöltési műveletet.
2. **`resourceLoader:didCancelLoadingRequest:`** -- akkor hívódik meg, ha egy kérést visszavonnak vagy felülírnak.

## Egyéni AVPlayer létrehozása

Az AVPlayer beállítása egyéni URL-sémával:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Ez a kód:
- Meghatároz egy URL-t az egyéni sémával
- Létrehoz egy `AVURLAsset`-et delegáttal a főszálon
- Felépít egy `AVPlayerItem`-et az eszközből
- Inicializálja az `AVPlayer`-t

## Az erőforrás-betöltő delegált megvalósítása

Hozzon létre egy `LSFilePlayerResourceLoader` nevű osztályt a kiszolgálóról való adatlekérés kezelésére és az adatok visszaküldésére az `AVURLAsset`-nek. Tárolja a betöltő példányokat egy szótárban, amelynek kulcsa az erőforrás URL-je.

```objc
- (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest *)loadingRequest {
    NSURL *resourceURL = [loadingRequest.request URL];
    if ([resourceURL.scheme isEqualToString:@"customscheme"]) {
        LSFilePlayerResourceLoader *loader = [self resourceLoaderForRequest:loadingRequest];
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

Ezek a metódusok ellenőrzik az URL-sémát, létrehozzák vagy lekérik a betöltőt, és hozzáadják a kérést a betöltő várólistájához. Az ismeretlen sémák `NO` értéket adnak vissza.

## Az LSFilePlayerResourceLoader interfész

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

## Adatbetöltés: kétlépéses folyamat

Amikor egy betöltési kérés bekerül a várólistába, két művelet fut egymás után:

- **contentInfoOperation** -- lekérdezi a tartalom hosszát, MIME-típusát és a bájttartomány-támogatást
- **dataOperation** -- lekéri a fájl adatait a `requestedOffset`-től kezdve

## Lemezgyorsítótárazási stratégia

A letöltött adatokat egy ideiglenes fájlba írja a lemezre. Az ugyanazon tartalom iránti következő kérések ebből a gyorsítótárból kerülnek kiszolgálásra, elkerülve a felesleges hálózati hívásokat. Ez a megközelítés:

- Csökkenti a sávszélesség-felhasználást
- Szinte azonnali újrajátszást tesz lehetővé
- Támogatja a keresési műveleteket a gyorsítótárazott tartományokon belül

## Függőben lévő kérések feldolgozása

A `processPendingRequests` metódus minden kérés `contentInformationRequest`-jét feltölti metaadatokkal, és kiszolgálja a gyorsítótárazott bájttartományokat. A teljesített kérések eltávolításra kerülnek a várólistából.

## Forráskód és következő lépések

Ez az útmutató magas szintű áttekintést nyújt az `AVAssetResourceLoaderDelegate` megvalósításáról felhő audio streamingnél egyéni engedélyezési fejlécekkel. A teljes forráskód elérhető a [GitHubon](http://github.com/leshkoapps/AVAssetResourceLoader).

Ez a megközelítés az [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) audio streaming motorját hajtja, amely a Dropbox, Google Drive, OneDrive, Yandex.Disk és más felhőszolgáltatásokból streamel zenét iOS és macOS rendszeren.

## Gyakran ismételt kérdések

{{% details title="Mikor érdemes az AVAssetResourceLoaderDelegate-t közvetlen URL helyett használni?" closed="true" %}}
Akkor használja, ha a felhőszolgáltatás egyéni engedélyezési fejléceket igényel, ha lemezgyorsítótárazásra van szüksége a streamelt audiónál, vagy ha részletes vezérlést szeretne az adatok betöltése és pufferelése felett.
{{% /details %}}

{{% details title="Ez a megközelítés működik Swift-tel is?" closed="true" %}}
Igen. Az `AVAssetResourceLoaderDelegate` protokoll ugyanúgy működik Swift-ben is. Az itt szereplő Objective-C példák közvetlenül lefordíthatók.
{{% /details %}}

{{% details title="Használható ez videó streamingnél is?" closed="true" %}}
Igen. Az `AVAssetResourceLoaderDelegate` bármilyen médiatípussal működik, amelyet az AVPlayer támogat, beleértve a videót is. Ugyanaz az egyéni séma megközelítés alkalmazható.
{{% /details %}}

{{% details title="Támogatja a háttérben való audiolejátszást?" closed="true" %}}
Igen, feltéve, hogy engedélyezi az "Audio, AirPlay és Picture in Picture" háttér módot az alkalmazás képességei között, és megfelelően konfigurálja az `AVAudioSession`-t.
{{% /details %}}
