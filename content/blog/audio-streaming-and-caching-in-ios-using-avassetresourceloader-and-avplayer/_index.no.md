---
title: "iOS Lydstrømming med AVAssetResourceLoader"
date: 2015-06-20
description: "Lær hvordan du strømmer og cacher lyd i iOS ved hjelp av AVAssetResourceLoaderDelegate og AVPlayer med tilpassede URL-skjemaer og diskbufring."
keywords: ["iOS lydstrømming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer opplæring", "AVFoundation lyd", "AVAssetResourceLoadingRequest", "tilpasset lydspiller iOS", "skybasert lydstrømming iOS", "lydbufring iOS", "Swift AVPlayer tilpasset skjema"]
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
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**Oppsummering:** Bruk `AVAssetResourceLoaderDelegate` med et tilpasset URL-skjema for å avskjære AVPlayers ressurslasting. Dette lar deg legge til tilpassede autorisasjonshoder for skytjenester, bufre lyd til disk og kontrollere strømmingsatferd -- alt uten å skrive en lokal HTTP-proxy. Full kildekode er tilgjengelig på [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Hvorfor AVPlayer trenger en tilpasset ressurslaster

`AVPlayer` spiller av lyd fra lokale filer og eksterne URL-er. For de fleste skytjenester (Dropbox, Google Drive, Box) kan du sende en direkte nedlastings-URL og avspilling fungerer rett ut av boksen.

Noen tjenester som **Yandex.Disk** og **WebDAV** krever imidlertid tilpassede autorisasjonshoder på GET-forespørsler. `AVPlayer` har ingen innebygd måte å injisere disse hodene på.

Løsningen: bruk egenskapen `resourceLoader` til `AVURLAsset`. Dette API-et avskjærer ressurslastingsforespørsler og fungerer som en lokal HTTP-proxy uten kompleksiteten.

### Hvordan det fungerer

`AVPlayer` bruker `resourceLoader` når det ikke gjenkjenner URL-skjemaet. Ved å erstatte `https://` med et tilpasset skjema (f.eks. `customscheme://`) tvinger du AVPlayer til å delegere all lasting til appen din.

Du må implementere to `AVAssetResourceLoaderDelegate`-metoder:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- kalles når AVPlayer trenger data. Lagre `AVAssetResourceLoadingRequest` og start datalasteoperasjonen din.
2. **`resourceLoader:didCancelLoadingRequest:`** -- kalles når en forespørsel avbrytes eller erstattes.

## Slik oppretter du en tilpasset AVPlayer

Sett opp en AVPlayer med et tilpasset URL-skjema:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Denne koden:
- Definerer en URL med ditt tilpassede skjema
- Oppretter en `AVURLAsset` med en delegat på hovedkøen
- Bygger en `AVPlayerItem` fra ressursen
- Initialiserer `AVPlayer`

## Implementering av ressurslaster-delegaten

Opprett en klasse kalt `LSFilePlayerResourceLoader` for å håndtere datahenting fra serveren og sende den tilbake til `AVURLAsset`. Lagre lasterforekomster i en ordbok med ressurs-URL som nøkkel.

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

Disse metodene sjekker URL-skjemaet, oppretter eller henter en laster og legger forespørselen til lasterens kø. Ukjente skjemaer returnerer `NO`.

## LSFilePlayerResourceLoader-grensesnitt

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

## Datalasting: To-trinns prosess

Når en lasteforespørsel kommer inn i køen, utføres to operasjoner i rekkefølge:

- **contentInfoOperation** -- spør om innholdslengde, MIME-type og støtte for byteområder
- **dataOperation** -- henter fildata fra `requestedOffset`

## Diskbufringsstrategi

Nedlastede data skrives til en midlertidig fil på disken. Påfølgende forespørsler om det samme innholdet betjenes fra denne bufferen, noe som unngår overflødige nettverksanrop. Denne tilnærmingen:

- Reduserer båndbreddebruk
- Muliggjør nesten øyeblikkelige avspillinger på nytt
- Støtter søkeoperasjoner innenfor bufrede områder

## Behandling av ventende forespørsler

Metoden `processPendingRequests` fyller `contentInformationRequest` for hver forespørsel med metadata og leverer bufrede byteområder. Fullførte forespørsler fjernes fra køen.

## Kildekode og neste steg

Denne opplæringen gir en overordnet oversikt over implementering av `AVAssetResourceLoaderDelegate` for skybasert lydstrømming med tilpassede autorisasjonshoder. Full kildekode er tilgjengelig på [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Denne tilnærmingen driver lydstrømmingsmotoren i [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), som strømmer musikk fra Dropbox, Google Drive, OneDrive, Yandex.Disk og andre skytjenester på iOS og macOS.

## Ofte stilte spørsmål

{{% details title="Når bør jeg bruke AVAssetResourceLoaderDelegate i stedet for en direkte URL?" closed="true" %}}
Bruk det når skytjenesten krever tilpassede autorisasjonshoder, når du trenger diskbufring for strømmet lyd, eller når du vil ha detaljert kontroll over hvordan data lastes og bufres.
{{% /details %}}

{{% details title="Fungerer denne tilnærmingen med Swift?" closed="true" %}}
Ja. `AVAssetResourceLoaderDelegate`-protokollen fungerer på samme måte i Swift. Objective-C-eksemplene her oversettes direkte.
{{% /details %}}

{{% details title="Kan jeg bruke dette for videostrømming også?" closed="true" %}}
Ja. `AVAssetResourceLoaderDelegate` fungerer med alle medietyper som AVPlayer støtter, inkludert video. Den samme tilnærmingen med tilpasset skjema gjelder.
{{% /details %}}

{{% details title="Støtter dette lydavspilling i bakgrunnen?" closed="true" %}}
Ja, så lenge du aktiverer bakgrunnsmodus for "Audio, AirPlay og Picture in Picture" i appens funksjoner og konfigurerer `AVAudioSession` riktig.
{{% /details %}}
