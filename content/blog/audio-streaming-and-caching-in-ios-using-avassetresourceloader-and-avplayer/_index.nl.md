---
title: "iOS Audio Streaming met AVAssetResourceLoader"
date: 2015-06-20
description: "Leer hoe u audio kunt streamen en cachen in iOS met AVAssetResourceLoaderDelegate en AVPlayer met aangepaste URL-schema's en schijfcaching."
keywords: ["iOS audio streaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer tutorial", "AVFoundation audio", "AVAssetResourceLoadingRequest", "aangepaste audiospeler iOS", "cloud audio streaming iOS", "audio caching iOS", "Swift AVPlayer aangepast schema"]
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

**Samenvatting:** Gebruik `AVAssetResourceLoaderDelegate` met een aangepast URL-schema om het laden van AVPlayer-bronnen te onderscheppen. Hiermee kunt u aangepaste autorisatieheaders toevoegen voor cloudservices, audio naar schijf cachen en streaminggedrag beheren -- alles zonder een lokale HTTP-proxy te schrijven. De volledige broncode staat op [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Waarom AVPlayer een aangepaste bronlader nodig heeft

`AVPlayer` speelt audio af van lokale bestanden en externe URL's. Voor de meeste cloudservices (Dropbox, Google Drive, Box) kunt u een directe download-URL doorgeven en werkt afspelen direct.

Sommige services zoals **Yandex.Disk** en **WebDAV** vereisen echter aangepaste autorisatieheaders bij GET-verzoeken. `AVPlayer` biedt geen ingebouwde manier om deze headers in te voegen.

De oplossing: gebruik de eigenschap `resourceLoader` van `AVURLAsset`. Deze API onderschept verzoeken voor het laden van bronnen en werkt als een lokale HTTP-proxy zonder de complexiteit.

### Hoe het werkt

`AVPlayer` gebruikt `resourceLoader` wanneer het het URL-schema niet herkent. Door `https://` te vervangen door een aangepast schema (bijv. `customscheme://`) dwingt u AVPlayer om alle laadopdrachten te delegeren naar uw app.

U moet twee `AVAssetResourceLoaderDelegate`-methoden implementeren:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- wordt aangeroepen wanneer AVPlayer data nodig heeft. Sla de `AVAssetResourceLoadingRequest` op en start uw gegevenslaadbewerkng.
2. **`resourceLoader:didCancelLoadingRequest:`** -- wordt aangeroepen wanneer een verzoek wordt geannuleerd of vervangen.

## Een aangepaste AVPlayer aanmaken

Stel een AVPlayer in met een aangepast URL-schema:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Deze code:
- Definieert een URL met uw aangepaste schema
- Maakt een `AVURLAsset` aan met een delegate op de hoofdwachtrij
- Bouwt een `AVPlayerItem` vanuit het asset
- Initialiseert `AVPlayer`

## De bronlader-delegate implementeren

Maak een klasse genaamd `LSFilePlayerResourceLoader` om gegevens op te halen van de server en terug te geven aan `AVURLAsset`. Sla laderinstanties op in een woordenboek met de bron-URL als sleutel.

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

Deze methoden controleren het URL-schema, maken een lader aan of halen er een op, en voegen het verzoek toe aan de wachtrij van de lader. Niet-herkende schema's geven `NO` terug.

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

## Gegevens laden: tweestaps proces

Wanneer een laadverzoek de wachtrij binnenkomt, worden twee bewerkingen opeenvolgend uitgevoerd:

- **contentInfoOperation** -- vraagt inhoudslengte, MIME-type en ondersteuning voor bytebereiken op
- **dataOperation** -- haalt bestandsgegevens op vanaf de `requestedOffset`

## Schijfcachingstrategie

Gedownloade gegevens worden naar een tijdelijk bestand op schijf geschreven. Volgende verzoeken voor dezelfde inhoud worden vanuit deze cache bediend, waardoor overbodige netwerkaanroepen worden vermeden. Deze aanpak:

- Vermindert bandbreedtegebruik
- Maakt bijna-directe herhalingen mogelijk
- Ondersteunt zoekbewerkingen binnen gecachede bereiken

## Verwerken van openstaande verzoeken

De methode `processPendingRequests` vult de `contentInformationRequest` van elk verzoek met metadata en levert gecachede bytebereiken. Voltooide verzoeken worden uit de wachtrij verwijderd.

## Broncode en volgende stappen

Deze tutorial biedt een overzicht op hoog niveau van het implementeren van `AVAssetResourceLoaderDelegate` voor cloud-audiostreaming met aangepaste autorisatieheaders. De volledige broncode is beschikbaar op [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Deze aanpak drijft de audiostreaming-engine in [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), dat muziek streamt van Dropbox, Google Drive, OneDrive, Yandex.Disk en andere cloudservices op iOS en macOS.

## Veelgestelde vragen

{{% details title="Wanneer moet ik AVAssetResourceLoaderDelegate gebruiken in plaats van een directe URL?" closed="true" %}}
Gebruik het wanneer de cloudservice aangepaste autorisatieheaders vereist, wanneer u schijfcaching nodig heeft voor gestreamde audio, of wanneer u gedetailleerde controle wilt over hoe gegevens worden geladen en gebufferd.
{{% /details %}}

{{% details title="Werkt deze aanpak met Swift?" closed="true" %}}
Ja. Het `AVAssetResourceLoaderDelegate`-protocol werkt op dezelfde manier in Swift. De Objective-C-voorbeelden hier zijn direct te vertalen.
{{% /details %}}

{{% details title="Kan ik dit ook gebruiken voor videostreaming?" closed="true" %}}
Ja. `AVAssetResourceLoaderDelegate` werkt met elk mediatype dat AVPlayer ondersteunt, inclusief video. Dezelfde aanpak met het aangepaste schema is van toepassing.
{{% /details %}}

{{% details title="Ondersteunt dit achtergrond-audioweergave?" closed="true" %}}
Ja, zolang u de achtergrondmodus "Audio, AirPlay en Picture in Picture" inschakelt in de mogelijkheden van uw app en uw `AVAudioSession` correct configureert.
{{% /details %}}
