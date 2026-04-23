---
title: "iOS Audio Streaming med AVAssetResourceLoader"
date: 2015-06-20
description: "Lär dig att streama och cacha ljud i iOS med AVAssetResourceLoaderDelegate och AVPlayer med anpassade URL-scheman och diskcachning."
keywords: ["iOS audio streaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer handledning", "AVFoundation audio", "AVAssetResourceLoadingRequest", "anpassad ljudspelare iOS", "moln-ljud-streaming iOS", "ljud-cachning iOS", "Swift AVPlayer anpassat schema"]
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

**TL;DR:** Använd `AVAssetResourceLoaderDelegate` med ett anpassat URL-schema för att avlyssna AVPlayers resursinläsning. Detta låter dig lägga till anpassade auktoriseringsrubriker för molntjänster, cacha ljud till disk och styra streamingbeteendet -- allt utan att skriva en lokal HTTP-proxy. Fullständig källkod finns på [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Varför AVPlayer behöver en anpassad resource loader

`AVPlayer` spelar upp ljud från lokala filer och fjärr-URL:er. För de flesta molntjänster (Dropbox, Google Drive, Box) kan du ange en direkt nedladdnings-URL och uppspelningen fungerar direkt.

Vissa tjänster som **Yandex.Disk** och **WebDAV** kräver dock anpassade auktoriseringsrubriker på GET-förfrågningar. `AVPlayer` erbjuder inget inbyggt sätt att injicera dessa rubriker.

Lösningen: använd egenskapen `resourceLoader` hos `AVURLAsset`. Detta API avlyssnar resursinläsningsförfrågningar och fungerar som en lokal HTTP-proxy utan komplexiteten.

### Hur det fungerar

`AVPlayer` använder `resourceLoader` när det inte känner igen URL-schemat. Genom att ersätta `https://` med ett anpassat schema (t.ex. `customscheme://`) tvingar du AVPlayer att delegera all inläsning till din app.

Du behöver implementera två `AVAssetResourceLoaderDelegate`-metoder:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- anropas när AVPlayer behöver data. Spara `AVAssetResourceLoadingRequest` och starta din datainläsningsoperation.
2. **`resourceLoader:didCancelLoadingRequest:`** -- anropas när en förfrågan avbryts eller ersätts.

## Hur man skapar en anpassad AVPlayer

Konfigurera en AVPlayer med ett anpassat URL-schema:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Den här koden:
- Definierar en URL med ditt anpassade schema
- Skapar en `AVURLAsset` med en delegat på huvudkön
- Bygger ett `AVPlayerItem` från tillgången
- Initierar `AVPlayer`

## Implementera resource loader-delegaten

Skapa en klass som heter `LSFilePlayerResourceLoader` för att hantera datahämtning från servern och skicka tillbaka den till `AVURLAsset`. Lagra loader-instanser i en ordbok med resurs-URL som nyckel.

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

Dessa metoder kontrollerar URL-schemat, skapar eller hämtar en loader och lägger till förfrågan i loaderns kö. Okända scheman returnerar `NO`.

## LSFilePlayerResourceLoader-gränssnittet

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

## Datainläsning: tvåstegsprocess

När en inläsningsförfrågan kommer in i kön utförs två operationer i sekvens:

- **contentInfoOperation** -- frågar efter innehållslängd, MIME-typ och stöd för byte-intervall
- **dataOperation** -- hämtar fildata med start från `requestedOffset`

## Diskcachningsstrategi

Nedladdade data skrivs till en temporär fil på disk. Efterföljande förfrågningar om samma innehåll hanteras från detta cacheminne, vilket undviker onödiga nätverksanrop. Detta tillvägagångssätt:

- Minskar bandbreddsanvändningen
- Möjliggör nästan omedelbar uppspelning igen
- Stöder sökoperationer inom cachade intervall

## Hantering av väntande förfrågningar

Metoden `processPendingRequests` fyller varje förfrågans `contentInformationRequest` med metadata och levererar cachade byte-intervall. Slutförda förfrågningar tas bort från kön.

## Källkod och nästa steg

Den här handledningen ger en överblick av hur man implementerar `AVAssetResourceLoaderDelegate` för moln-ljud-streaming med anpassade auktoriseringsrubriker. Den fullständiga källkoden finns på [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Det här tillvägagångssättet driver ljud-streaming-motorn i [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), som streamar musik från Dropbox, Google Drive, OneDrive, Yandex.Disk och andra molntjänster på iOS och macOS.

## Vanliga frågor

{{% details title="När ska jag använda AVAssetResourceLoaderDelegate istället för en direkt URL?" closed="true" %}}
Använd det när molntjänsten kräver anpassade auktoriseringsrubriker, när du behöver diskcachning för streamat ljud, eller när du vill ha detaljerad kontroll över hur data läses in och buffras.
{{% /details %}}

{{% details title="Fungerar det här tillvägagångssättet med Swift?" closed="true" %}}
Ja. Protokollet `AVAssetResourceLoaderDelegate` fungerar på samma sätt i Swift. Objective-C-exemplen här översätts direkt.
{{% /details %}}

{{% details title="Kan jag använda detta för video-streaming också?" closed="true" %}}
Ja. `AVAssetResourceLoaderDelegate` fungerar med alla medietyper som AVPlayer stöder, inklusive video. Samma anpassade schema-metod gäller.
{{% /details %}}

{{% details title="Stöder detta bakgrundsljuduppspelning?" closed="true" %}}
Ja, så länge du aktiverar bakgrundsläget "Audio, AirPlay och Picture in Picture" i din apps funktioner och konfigurerar din `AVAudioSession` korrekt.
{{% /details %}}
