---
title: "Streaming Audio iOS cu AVAssetResourceLoader"
date: 2015-06-20
description: "Aflați cum să faceți streaming și cache de audio în iOS folosind AVAssetResourceLoaderDelegate și AVPlayer cu scheme URL personalizate și cache pe disc."
keywords: ["streaming audio iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "tutorial AVPlayer", "AVFoundation audio", "AVAssetResourceLoadingRequest", "player audio personalizat iOS", "streaming audio din cloud iOS", "cache audio iOS", "Swift AVPlayer schemă personalizată"]
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

**TL;DR:** Utilizați `AVAssetResourceLoaderDelegate` cu o schemă URL personalizată pentru a intercepta încărcarea resurselor AVPlayer. Aceasta vă permite să adăugați antete de autorizare personalizate pentru serviciile cloud, să memorați audio pe disc și să controlați comportamentul de streaming -- fără a scrie un proxy HTTP local. Codul sursă complet se află pe [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## De ce AVPlayer are nevoie de un încărcător de resurse personalizat

`AVPlayer` redă audio din fișiere locale și URL-uri la distanță. Pentru majoritatea serviciilor cloud (Dropbox, Google Drive, Box), puteți transmite un URL de descărcare directă și redarea funcționează imediat.

Cu toate acestea, unele servicii precum **Yandex.Disk** și **WebDAV** necesită antete de autorizare personalizate la solicitările GET. `AVPlayer` nu oferă nicio modalitate integrată de a injecta aceste antete.

Soluția: utilizați proprietatea `resourceLoader` a `AVURLAsset`. Acest API interceptează solicitările de încărcare a resurselor, acționând ca un proxy HTTP local fără complexitatea asociată.

### Cum funcționează

`AVPlayer` utilizează `resourceLoader` atunci când nu recunoaște schema URL. Înlocuind `https://` cu o schemă personalizată (ex.: `customscheme://`), forțați AVPlayer să delege toată încărcarea aplicației dvs.

Trebuie să implementați două metode `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- apelată când AVPlayer are nevoie de date. Salvați `AVAssetResourceLoadingRequest` și începeți operațiunea de încărcare a datelor.
2. **`resourceLoader:didCancelLoadingRequest:`** -- apelată când o solicitare este anulată sau înlocuită.

## Cum se creează un AVPlayer personalizat

Configurați un AVPlayer cu o schemă URL personalizată:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Acest cod:
- Definește un URL cu schema dvs. personalizată
- Creează un `AVURLAsset` cu un delegate pe coada principală
- Construiește un `AVPlayerItem` din asset
- Inițializează `AVPlayer`

## Implementarea delegatului încărcătorului de resurse

Creați o clasă numită `LSFilePlayerResourceLoader` pentru a gestiona preluarea datelor de pe server și transmiterea lor înapoi la `AVURLAsset`. Stocați instanțele încărcătorului într-un dicționar indexat după URL-ul resursei.

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

Aceste metode verifică schema URL, creează sau recuperează un încărcător și adaugă solicitarea în coada încărcătorului. Schemele nerecunoscute returnează `NO`.

## Interfața LSFilePlayerResourceLoader

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

## Încărcarea datelor: proces în două etape

Când o solicitare de încărcare intră în coadă, două operațiuni se execută în secvență:

- **contentInfoOperation** -- interogă lungimea conținutului, tipul MIME și suportul pentru intervale de octeți
- **dataOperation** -- preia datele fișierului începând de la `requestedOffset`

## Strategia de cache pe disc

Datele descărcate sunt scrise într-un fișier temporar pe disc. Solicitările ulterioare pentru același conținut sunt servite din acest cache, evitând apelurile de rețea redundante. Această abordare:

- Reduce utilizarea lățimii de bandă
- Permite reluări aproape instantanee
- Suportă operațiuni de căutare în intervalele din cache

## Procesarea solicitărilor în așteptare

Metoda `processPendingRequests` completează `contentInformationRequest` al fiecărei solicitări cu metadate și livrează intervalele de octeți din cache. Solicitările finalizate sunt eliminate din coadă.

## Cod sursă și pașii următori

Acest tutorial oferă o prezentare generală a implementării `AVAssetResourceLoaderDelegate` pentru streaming audio din cloud cu antete de autorizare personalizate. Codul sursă complet este disponibil pe [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Această abordare alimentează motorul de streaming audio din [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), care transmite muzică din Dropbox, Google Drive, OneDrive, Yandex.Disk și alte servicii cloud pe iOS și macOS.

## Întrebări frecvente

{{% details title="Când ar trebui să folosesc AVAssetResourceLoaderDelegate în loc de un URL direct?" closed="true" %}}
Utilizați-l atunci când serviciul cloud necesită antete de autorizare personalizate, când aveți nevoie de cache pe disc pentru audio transmis în flux sau când doriți un control detaliat asupra modului în care datele sunt încărcate și memorate în buffer.
{{% /details %}}

{{% details title="Această abordare funcționează cu Swift?" closed="true" %}}
Da. Protocolul `AVAssetResourceLoaderDelegate` funcționează în același mod în Swift. Exemplele din Objective-C se traduc direct.
{{% /details %}}

{{% details title="Pot folosi aceasta și pentru streaming video?" closed="true" %}}
Da. `AVAssetResourceLoaderDelegate` funcționează cu orice tip de media pe care AVPlayer îl suportă, inclusiv video. Aceeași abordare cu schemă personalizată se aplică.
{{% /details %}}

{{% details title="Aceasta suportă redarea audio în fundal?" closed="true" %}}
Da, atâta timp cât activați modul de fundal „Audio, AirPlay și Picture in Picture" în capabilitățile aplicației dvs. și configurați corect `AVAudioSession`.
{{% /details %}}
