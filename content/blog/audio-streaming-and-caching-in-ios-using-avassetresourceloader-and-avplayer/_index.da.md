---
title: "iOS-lydstreaming med AVAssetResourceLoader"
date: 2015-06-20
description: "Lær, hvordan du streamer og cacher lyd i iOS ved hjælp af AVAssetResourceLoaderDelegate og AVPlayer med brugerdefinerede URL-skemaer og diskcaching."
keywords: ["iOS lydstreaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer vejledning", "AVFoundation lyd", "AVAssetResourceLoadingRequest", "brugerdefineret lydafspiller iOS", "cloud lydstreaming iOS", "lydcaching iOS", "Swift AVPlayer brugerdefineret skema"]
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

**Kort sagt:** Brug `AVAssetResourceLoaderDelegate` med et brugerdefineret URL-skema til at opsnappe AVPlayers ressourceindlæsning. Dette giver dig mulighed for at tilføje brugerdefinerede autorisationsheadere til cloudtjenester, cache lyd til disk og styre streamingadfærd -- alt sammen uden at skrive en lokal HTTP-proxy. Den fulde kildekode findes på [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Hvorfor AVPlayer har brug for en brugerdefineret ressourceindlæser

`AVPlayer` afspiller lyd fra lokale filer og fjern-URL'er. For de fleste cloudtjenester (Dropbox, Google Drive, Box) kan du angive en direkte download-URL, og afspilning virker ud af boksen.

Nogle tjenester som **Yandex.Disk** og **WebDAV** kræver dog brugerdefinerede autorisationsheadere i GET-anmodninger. `AVPlayer` har ingen indbygget måde at injicere disse headere på.

Løsningen: brug egenskaben `resourceLoader` på `AVURLAsset`. Denne API opsnapper ressourceindlæsningsanmodninger og fungerer som en lokal HTTP-proxy uden kompleksiteten.

### Sådan fungerer det

`AVPlayer` bruger `resourceLoader`, når det ikke genkender URL-skemaet. Ved at erstatte `https://` med et brugerdefineret skema (f.eks. `customscheme://`) tvinger du AVPlayer til at delegere al indlæsning til din app.

Du skal implementere to `AVAssetResourceLoaderDelegate`-metoder:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- kaldes, når AVPlayer har brug for data. Gem `AVAssetResourceLoadingRequest` og start din dataindlæsningsoperation.
2. **`resourceLoader:didCancelLoadingRequest:`** -- kaldes, når en anmodning annulleres eller erstattes.

## Sådan opretter du en brugerdefineret AVPlayer

Opsæt en AVPlayer med et brugerdefineret URL-skema:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Denne kode:
- Definerer en URL med dit brugerdefinerede skema
- Opretter en `AVURLAsset` med en delegat på hovedkøen
- Bygger et `AVPlayerItem` fra asset'et
- Initialiserer `AVPlayer`

## Implementering af ressourceindlæser-delegaten

Opret en klasse kaldet `LSFilePlayerResourceLoader` til at håndtere datahentning fra serveren og sende den tilbage til `AVURLAsset`. Gem indlæserforekomster i en ordbog, der er nøglet af ressource-URL'en.

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

Disse metoder kontrollerer URL-skemaet, opretter eller henter en indlæser og tilføjer anmodningen til indlæserens kø. Ukendte skemaer returnerer `NO`.

## LSFilePlayerResourceLoader-interface

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

## Dataindlæsning: to-trinsproces

Når en indlæsningsanmodning kommer i køen, udføres to operationer i rækkefølge:

- **contentInfoOperation** -- forespørger indholdslængde, MIME-type og understøttelse af byte-range
- **dataOperation** -- henter fildata startende fra `requestedOffset`

## Diskcaching-strategi

Downloadede data skrives til en midlertidig fil på disk. Efterfølgende anmodninger om det samme indhold betjenes fra denne cache, hvilket undgår overflødige netværkskald. Denne tilgang:

- Reducerer båndbreddeforbrug
- Muliggør næsten øjeblikkelig genafspilning
- Understøtter søgeoperationer inden for cachede intervaller

## Behandling af ventende anmodninger

Metoden `processPendingRequests` udfylder `contentInformationRequest` for hver anmodning med metadata og leverer cachede byte-intervaller. Færdige anmodninger fjernes fra køen.

## Kildekode og næste skridt

Denne vejledning giver et overordnet overblik over implementering af `AVAssetResourceLoaderDelegate` til cloud-lydstreaming med brugerdefinerede autorisationsheadere. Den fulde kildekode er tilgængelig på [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Denne tilgang driver lydstreaming-motoren i [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), som streamer musik fra Dropbox, Google Drive, OneDrive, Yandex.Disk og andre cloudtjenester på iOS og macOS.

## Ofte stillede spørgsmål

{{% details title="Hvornår skal jeg bruge AVAssetResourceLoaderDelegate i stedet for en direkte URL?" closed="true" %}}
Brug det, når cloudtjenesten kræver brugerdefinerede autorisationsheadere, når du har brug for diskcaching af streamet lyd, eller når du ønsker finkornet kontrol over, hvordan data indlæses og buffres.
{{% /details %}}

{{% details title="Virker denne tilgang med Swift?" closed="true" %}}
Ja. Protokollen `AVAssetResourceLoaderDelegate` fungerer på samme måde i Swift. Objective-C-eksemplerne her oversættes direkte.
{{% /details %}}

{{% details title="Kan jeg bruge dette til videostreaming også?" closed="true" %}}
Ja. `AVAssetResourceLoaderDelegate` fungerer med enhver medietype, som AVPlayer understøtter, herunder video. Den samme brugerdefinerede skematilgang gælder.
{{% /details %}}

{{% details title="Understøtter dette lydafspilning i baggrunden?" closed="true" %}}
Ja, så længe du aktiverer baggrundstilstanden "Audio, AirPlay, and Picture in Picture" i din apps funktioner og konfigurerer din `AVAudioSession` korrekt.
{{% /details %}}
