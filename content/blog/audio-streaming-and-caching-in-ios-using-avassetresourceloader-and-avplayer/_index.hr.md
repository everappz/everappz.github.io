---
title: "iOS audio streaming s AVAssetResourceLoader"
date: 2015-06-20
description: "Naučite kako streamati i cachirati audio na iOS-u koristeći AVAssetResourceLoaderDelegate i AVPlayer s prilagođenim URL shemama i pohranom na disk."
keywords: ["iOS audio streaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer vodič", "AVFoundation audio", "AVAssetResourceLoadingRequest", "prilagođeni audio player iOS", "cloud audio streaming iOS", "audio caching iOS", "Swift AVPlayer prilagođena shema"]
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

**Ukratko:** Koristite `AVAssetResourceLoaderDelegate` s prilagođenom URL shemom za presretanje učitavanja resursa u AVPlayeru. To vam omogućuje dodavanje prilagođenih zaglavlja autorizacije za cloud usluge, pohranu audija na disk i kontrolu ponašanja streaminga -- sve bez pisanja lokalnog HTTP proxyja. Cijeli izvorni kod dostupan je na [GitHubu](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Zašto AVPlayer treba prilagođeni učitavač resursa

`AVPlayer` reproducira audio iz lokalnih datoteka i udaljenih URL-ova. Za većinu cloud usluga (Dropbox, Google Drive, Box) možete proslijediti izravni URL za preuzimanje i reprodukcija radi odmah.

Međutim, neke usluge poput **Yandex.Disk** i **WebDAV** zahtijevaju prilagođena zaglavlja autorizacije u GET zahtjevima. `AVPlayer` ne pruža ugrađen način za ubacivanje ovih zaglavlja.

Rješenje: koristite svojstvo `resourceLoader` od `AVURLAsset`. Ovaj API presreće zahtjeve za učitavanje resursa, djelujući poput lokalnog HTTP proxyja bez složenosti.

### Kako funkcionira

`AVPlayer` koristi `resourceLoader` kada ne prepoznaje URL shemu. Zamjenom `https://` prilagođenom shemom (npr. `customscheme://`), prisiljavate AVPlayer da delegira svo učitavanje vašoj aplikaciji.

Trebate implementirati dvije metode `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- poziva se kada AVPlayer treba podatke. Pohranite `AVAssetResourceLoadingRequest` i pokrenite operaciju učitavanja podataka.
2. **`resourceLoader:didCancelLoadingRequest:`** -- poziva se kada se zahtjev otkaže ili zamijeni.

## Kako stvoriti prilagođeni AVPlayer

Postavite AVPlayer s prilagođenom URL shemom:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Ovaj kod:
- Definira URL s vašom prilagođenom shemom
- Stvara `AVURLAsset` s delegatom na glavnom redu
- Gradi `AVPlayerItem` iz asseta
- Inicijalizira `AVPlayer`

## Implementacija delegata učitavača resursa

Stvorite klasu pod nazivom `LSFilePlayerResourceLoader` za upravljanje dohvaćanjem podataka sa servera i njihovim prosljeđivanjem natrag `AVURLAsset`-u. Pohranite instance učitavača u rječnik s ključem URL resursa.

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

Ove metode provjera URL shemu, stvaraju ili dohvaćaju učitavač te dodaju zahtjev u red učitavača. Neprepoznate sheme vraćaju `NO`.

## Sučelje LSFilePlayerResourceLoader

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

## Učitavanje podataka: dvostupanjski proces

Kada zahtjev za učitavanje uđe u red, dvije operacije izvršavaju se redom:

- **contentInfoOperation** -- upituje duljinu sadržaja, MIME tip i podršku za raspon bajtova
- **dataOperation** -- dohvaća podatke datoteke počevši od `requestedOffset`

## Strategija pohrane na disk

Preuzeti podaci zapisuju se u privremenu datoteku na disku. Naknadni zahtjevi za isti sadržaj posluživani su iz ovog cachea, izbjegavajući redundantne mrežne pozive. Ovaj pristup:

- Smanjuje potrošnju propusnosti
- Omogućuje gotovo trenutačno ponavljanje reproduciranja
- Podržava operacije premotavanja unutar cachiranih raspona

## Obrada čekajućih zahtjeva

Metoda `processPendingRequests` popunjava `contentInformationRequest` svakog zahtjeva metapodacima i isporučuje cachirane raspone bajtova. Dovršeni zahtjevi uklanjaju se iz reda.

## Izvorni kod i sljedeći koraci

Ovaj vodič pruža pregled na visokoj razini implementacije `AVAssetResourceLoaderDelegate` za cloud audio streaming s prilagođenim zaglavljima autorizacije. Cijeli izvorni kod dostupan je na [GitHubu](http://github.com/leshkoapps/AVAssetResourceLoader).

Ovaj pristup pokreće engine za audio streaming u [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), koji streamuje glazbu iz Dropboxa, Google Drivea, OneDrivea, Yandex.Diska i drugih cloud usluga na iOS-u i macOS-u.

## Često postavljana pitanja

{{% details title="Kada koristiti AVAssetResourceLoaderDelegate umjesto izravnog URL-a?" closed="true" %}}
Koristite ga kada cloud usluga zahtijeva prilagođena zaglavlja autorizacije, kada trebate disk cache za streamani audio, ili kada želite preciznu kontrolu nad načinom učitavanja i međupohranjivanja podataka.
{{% /details %}}

{{% details title="Funkcionira li ovaj pristup sa Swiftom?" closed="true" %}}
Da. Protokol `AVAssetResourceLoaderDelegate` funkcionira na isti način u Swiftu. Ovdje prikazani Objective-C primjeri izravno se prevode.
{{% /details %}}

{{% details title="Mogu li ovo koristiti i za video streaming?" closed="true" %}}
Da. `AVAssetResourceLoaderDelegate` funkcionira s bilo kojom vrstom medija koju AVPlayer podržava, uključujući video. Isti pristup s prilagođenom shemom se primjenjuje.
{{% /details %}}

{{% details title="Podržava li ovo reprodukciju audija u pozadini?" closed="true" %}}
Da, sve dok omogućite pozadinski način rada "Audio, AirPlay, and Picture in Picture" u mogućnostima vaše aplikacije i ispravno konfigurirate svoj `AVAudioSession`.
{{% /details %}}
