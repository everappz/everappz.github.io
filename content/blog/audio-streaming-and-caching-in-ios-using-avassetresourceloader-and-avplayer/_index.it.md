---
title: "iOS Audio Streaming con AVAssetResourceLoader"
date: 2015-06-20
description: "Scopri come eseguire lo streaming e la cache dell'audio su iOS utilizzando AVAssetResourceLoaderDelegate e AVPlayer con schemi URL personalizzati e cache su disco."
keywords: ["iOS audio streaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "tutorial AVPlayer", "AVFoundation audio", "AVAssetResourceLoadingRequest", "player audio personalizzato iOS", "cloud audio streaming iOS", "cache audio iOS", "Swift AVPlayer schema personalizzato"]
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

**TL;DR:** Usa `AVAssetResourceLoaderDelegate` con uno schema URL personalizzato per intercettare il caricamento delle risorse di AVPlayer. Questo ti consente di aggiungere header di autorizzazione personalizzati per i servizi cloud, memorizzare l'audio su disco e controllare il comportamento dello streaming -- il tutto senza scrivere un proxy HTTP locale. Il codice sorgente completo è disponibile su [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Perché AVPlayer ha bisogno di un Resource Loader personalizzato?

`AVPlayer` riproduce audio da file locali e URL remote. Per la maggior parte dei servizi cloud (Dropbox, Google Drive, Box), è sufficiente passare un URL di download diretto e la riproduzione funziona immediatamente.

Tuttavia, alcuni servizi come **Yandex.Disk** e **WebDAV** richiedono header di autorizzazione personalizzati nelle richieste GET. `AVPlayer` non fornisce alcun modo integrato per iniettare questi header.

La soluzione: usa la proprietà `resourceLoader` di `AVURLAsset`. Questa API intercetta le richieste di caricamento delle risorse, agendo come un proxy HTTP locale senza la sua complessità.

### Come Funziona

`AVPlayer` usa `resourceLoader` quando non riconosce lo schema URL. Sostituendo `https://` con uno schema personalizzato (ad esempio `customscheme://`), si forza AVPlayer a delegare tutto il caricamento all'app.

È necessario implementare due metodi `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- chiamato quando AVPlayer ha bisogno di dati. Salva l'`AVAssetResourceLoadingRequest` e avvia l'operazione di caricamento dati.
2. **`resourceLoader:didCancelLoadingRequest:`** -- chiamato quando una richiesta viene annullata o sostituita.

## Come Creare un AVPlayer Personalizzato

Configura un AVPlayer con uno schema URL personalizzato:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Questo codice:
- Definisce un URL con lo schema personalizzato
- Crea un `AVURLAsset` con un delegato sulla coda principale
- Costruisce un `AVPlayerItem` dall'asset
- Inizializza `AVPlayer`

## Implementazione del Delegato Resource Loader

Crea una classe chiamata `LSFilePlayerResourceLoader` per gestire il recupero dei dati dal server e restituirli ad `AVURLAsset`. Archivia le istanze del loader in un dizionario indicizzato dall'URL della risorsa.

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

Questi metodi verificano lo schema URL, creano o recuperano un loader e aggiungono la richiesta alla coda del loader. Gli schemi non riconosciuti restituiscono `NO`.

## Interfaccia LSFilePlayerResourceLoader

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

## Caricamento Dati: Processo in Due Fasi

Quando una richiesta di caricamento entra nella coda, vengono eseguite due operazioni in sequenza:

- **contentInfoOperation** -- interroga la lunghezza del contenuto, il tipo MIME e il supporto degli intervalli di byte
- **dataOperation** -- recupera i dati del file a partire dal `requestedOffset`

## Strategia di Cache su Disco

I dati scaricati vengono scritti in un file temporaneo su disco. Le richieste successive per lo stesso contenuto vengono servite da questa cache, evitando chiamate di rete ridondanti. Questo approccio:

- Riduce l'utilizzo della banda
- Consente ripetizioni quasi istantanee
- Supporta operazioni di seek negli intervalli memorizzati nella cache

## Elaborazione delle Richieste in Sospeso

Il metodo `processPendingRequests` riempie il `contentInformationRequest` di ogni richiesta con i metadati e consegna gli intervalli di byte memorizzati nella cache. Le richieste completate vengono rimosse dalla coda.

## Codice Sorgente e Passi Successivi

Questo tutorial fornisce una panoramica di alto livello dell'implementazione di `AVAssetResourceLoaderDelegate` per lo streaming audio cloud con header di autorizzazione personalizzati. Il codice sorgente completo è disponibile su [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Questo approccio alimenta il motore di streaming audio di [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), che trasmette musica da Dropbox, Google Drive, OneDrive, Yandex.Disk e altri servizi cloud su iOS e macOS.

## Domande Frequenti

{{% details title="Quando dovrei usare AVAssetResourceLoaderDelegate invece di un URL diretto?" closed="true" %}}
Usalo quando il servizio cloud richiede header di autorizzazione personalizzati, quando hai bisogno della cache su disco per l'audio in streaming, o quando vuoi un controllo dettagliato su come i dati vengono caricati e bufferizzati.
{{% /details %}}

{{% details title="Questo approccio funziona con Swift?" closed="true" %}}
Sì. Il protocollo `AVAssetResourceLoaderDelegate` funziona allo stesso modo in Swift. Gli esempi Objective-C qui presenti si traducono direttamente.
{{% /details %}}

{{% details title="Posso usare questo approccio anche per lo streaming video?" closed="true" %}}
Sì. `AVAssetResourceLoaderDelegate` funziona con qualsiasi tipo di media supportato da AVPlayer, incluso il video. Lo stesso approccio con schema personalizzato si applica.
{{% /details %}}

{{% details title="Supporta la riproduzione audio in background?" closed="true" %}}
Sì, a condizione che tu abilitino la modalità background "Audio, AirPlay e Picture in Picture" nelle capacità della tua app e configuri correttamente l'`AVAudioSession`.
{{% /details %}}
