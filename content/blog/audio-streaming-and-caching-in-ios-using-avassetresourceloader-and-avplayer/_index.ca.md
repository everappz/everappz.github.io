---
title: "Streaming d'àudio en iOS amb AVAssetResourceLoader"
date: 2015-06-20
description: "Aprèn a fer streaming i emmagatzemar en memòria cau àudio en iOS utilitzant AVAssetResourceLoaderDelegate i AVPlayer amb esquemes d'URL personalitzats i memòria cau en disc."
keywords: ["streaming d'àudio iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "tutorial AVPlayer", "àudio AVFoundation", "AVAssetResourceLoadingRequest", "reproductor d'àudio personalitzat iOS", "streaming d'àudio al núvol iOS", "memòria cau d'àudio iOS", "Swift AVPlayer esquema personalitzat"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**Resum:** Utilitza `AVAssetResourceLoaderDelegate` amb un esquema d'URL personalitzat per interceptar la càrrega de recursos d'AVPlayer. Això et permet afegir capçaleres d'autorització personalitzades per a serveis al núvol, emmagatzemar àudio en memòria cau al disc i controlar el comportament del streaming -- tot sense escriure un proxy HTTP local. El codi font complet és a [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Per què AVPlayer necessita un carregador de recursos personalitzat

`AVPlayer` reprodueix àudio de fitxers locals i URL remotes. Per a la majoria de serveis al núvol (Dropbox, Google Drive, Box), pots passar una URL de descàrrega directa i la reproducció funciona de manera immediata.

No obstant, alguns serveis com **Yandex.Disk** i **WebDAV** requereixen capçaleres d'autorització personalitzades en les sol·licituds GET. `AVPlayer` no proporciona cap manera integrada d'injectar aquestes capçaleres.

La solució: utilitza la propietat `resourceLoader` de `AVURLAsset`. Aquesta API intercepta les sol·licituds de càrrega de recursos, actuant com un proxy HTTP local sense la complexitat habitual.

### Com funciona

`AVPlayer` utilitza `resourceLoader` quan no reconeix l'esquema d'URL. Substituint `https://` per un esquema personalitzat (p. ex., `customscheme://`), forces AVPlayer a delegar tota la càrrega a la teva aplicació.

Has d'implementar dos mètodes de `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- s'invoca quan AVPlayer necessita dades. Desa `AVAssetResourceLoadingRequest` i inicia la teva operació de càrrega de dades.
2. **`resourceLoader:didCancelLoadingRequest:`** -- s'invoca quan una sol·licitud es cancel·la o se substitueix.

## Com crear un AVPlayer personalitzat

Configura un AVPlayer amb un esquema d'URL personalitzat:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Aquest codi:
- Defineix una URL amb el teu esquema personalitzat
- Crea un `AVURLAsset` amb un delegat a la cua principal
- Construeix un `AVPlayerItem` a partir de l'asset
- Inicialitza `AVPlayer`

## Implementació del delegat del carregador de recursos

Crea una classe anomenada `LSFilePlayerResourceLoader` per gestionar la recuperació de dades del servidor i passar-les de tornada a `AVURLAsset`. Emmagatzema les instàncies del carregador en un diccionari indexat per l'URL del recurs.

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

Aquests mètodes comproven l'esquema d'URL, creen o recuperen un carregador, i afegeixen la sol·licitud a la cua del carregador. Els esquemes no reconeguts retornen `NO`.

## Interfície de LSFilePlayerResourceLoader

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

## Càrrega de dades: procés en dues etapes

Quan una sol·licitud de càrrega entra a la cua, s'executen dues operacions en seqüència:

- **contentInfoOperation** -- consulta la longitud del contingut, el tipus MIME i el suport de rangs de bytes
- **dataOperation** -- recupera les dades del fitxer a partir del `requestedOffset`

## Estratègia de memòria cau en disc

Les dades descarregades s'escriuen en un fitxer temporal al disc. Les sol·licituds posteriors del mateix contingut es serveixen des d'aquesta memòria cau, evitant crides de xarxa redundants. Aquest enfocament:

- Redueix l'ús d'amplada de banda
- Permet reproduccions gairebé instantànies
- Admet operacions de cerca dins dels rangs emmagatzemats en memòria cau

## Processament de sol·licituds pendents

El mètode `processPendingRequests` omple `contentInformationRequest` de cada sol·licitud amb metadades i lliura els rangs de bytes en memòria cau. Les sol·licituds completades s'eliminen de la cua.

## Codi font i passos següents

Aquest tutorial proporciona una visió general d'alt nivell de la implementació de `AVAssetResourceLoaderDelegate` per al streaming d'àudio al núvol amb capçaleres d'autorització personalitzades. El codi font complet està disponible a [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Aquest enfocament impulsa el motor de streaming d'àudio d'[Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), que fa streaming de música des de Dropbox, Google Drive, OneDrive, Yandex.Disk i altres serveis al núvol en iOS i macOS.

## Preguntes freqüents

{{% details title="Quan hauria d'utilitzar AVAssetResourceLoaderDelegate en lloc d'una URL directa?" closed="true" %}}
Utilitza'l quan el servei al núvol requereixi capçaleres d'autorització personalitzades, quan necessitis memòria cau en disc per a l'àudio en streaming, o quan vulguis un control detallat sobre com es carreguen i s'emmagatzemen en buffer les dades.
{{% /details %}}

{{% details title="Aquest enfocament funciona amb Swift?" closed="true" %}}
Sí. El protocol `AVAssetResourceLoaderDelegate` funciona de la mateixa manera en Swift. Els exemples en Objective-C d'aquí es tradueixen directament.
{{% /details %}}

{{% details title="Puc utilitzar-lo per al streaming de vídeo també?" closed="true" %}}
Sí. `AVAssetResourceLoaderDelegate` funciona amb qualsevol tipus de mitjans que AVPlayer admeti, inclòs el vídeo. S'aplica el mateix enfocament d'esquema personalitzat.
{{% /details %}}

{{% details title="Admet la reproducció d'àudio en segon pla?" closed="true" %}}
Sí, sempre que activis el mode de segon pla "Audio, AirPlay, and Picture in Picture" en les capacitats de la teva aplicació i configuris correctament el teu `AVAudioSession`.
{{% /details %}}
