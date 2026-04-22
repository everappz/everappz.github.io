---
title: "iOS-Audio-Streaming mit AVAssetResourceLoader"
date: 2015-06-20
description: "Erfahren Sie, wie Sie Audio in iOS mit AVAssetResourceLoaderDelegate und AVPlayer mit benutzerdefinierten URL-Schemata und Disk-Caching streamen und zwischenspeichern."
keywords: ["iOS Audio-Streaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer Tutorial", "AVFoundation Audio", "AVAssetResourceLoadingRequest", "benutzerdefinierter Audio-Player iOS", "Cloud-Audio-Streaming iOS", "Audio-Caching iOS", "Swift AVPlayer benutzerdefiniertes Schema"]
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

**TL;DR:** Verwenden Sie `AVAssetResourceLoaderDelegate` mit einem benutzerdefinierten URL-Schema, um das Laden von Ressourcen durch AVPlayer abzufangen. Damit können Sie benutzerdefinierte Autorisierungs-Header für Cloud-Dienste hinzufugen, Audio auf der Festplatte zwischenspeichern und das Streaming-Verhalten steuern -- ohne einen lokalen HTTP-Proxy schreiben zu mussen. Der vollstandige Quellcode ist auf [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader) verfugbar.

---

## Warum AVPlayer einen benutzerdefinierten Resource Loader benotigt

`AVPlayer` spielt Audio aus lokalen Dateien und Remote-URLs ab. Bei den meisten Cloud-Diensten (Dropbox, Google Drive, Box) können Sie eine direkte Download-URL übergeben und die Wiedergabe funktioniert sofort.

Einige Dienste wie **Yandex.Disk** und **WebDAV** erfordern jedoch benutzerdefinierte Autorisierungs-Header bei GET-Anfragen. `AVPlayer` bietet keine integrierte Moglichkeit, diese Header einzufügen.

Die Losung: Verwenden Sie die `resourceLoader`-Eigenschaft von `AVURLAsset`. Diese API fängt Ressourcen-Ladeanfragen ab und fungiert wie ein lokaler HTTP-Proxy ohne die Komplexität.

### Funktionsweise

`AVPlayer` verwendet `resourceLoader`, wenn es das URL-Schema nicht erkennt. Indem Sie `https://` durch ein benutzerdefiniertes Schema ersetzen (z. B. `customscheme://`), zwingen Sie AVPlayer, das gesamte Laden an Ihre App zu delegieren.

Sie mussen zwei `AVAssetResourceLoaderDelegate`-Methoden implementieren:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- wird aufgerufen, wenn AVPlayer Daten benotigt. Speichern Sie das `AVAssetResourceLoadingRequest` und starten Sie Ihren Datenladevorgang.
2. **`resourceLoader:didCancelLoadingRequest:`** -- wird aufgerufen, wenn eine Anfrage abgebrochen oder uberholt wurde.

## So erstellen Sie einen benutzerdefinierten AVPlayer

Richten Sie einen AVPlayer mit einem benutzerdefinierten URL-Schema ein:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Dieser Code:
- Definiert eine URL mit Ihrem benutzerdefinierten Schema
- Erstellt ein `AVURLAsset` mit einem Delegate im Hauptthread
- Erstellt ein `AVPlayerItem` aus dem Asset
- Initialisiert `AVPlayer`

## Implementierung des Resource Loader Delegate

Erstellen Sie eine Klasse namens `LSFilePlayerResourceLoader`, um Daten vom Server abzurufen und an `AVURLAsset` zurückzugeben. Speichern Sie Loader-Instanzen in einem Dictionary mit der Ressourcen-URL als Schlüssel.

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

Diese Methoden prüfen das URL-Schema, erstellen oder rufen einen Loader ab und fügen die Anfrage zur Warteschlange des Loaders hinzu. Nicht erkannte Schemata geben `NO` zurück.

## LSFilePlayerResourceLoader-Schnittstelle

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

## Datenladen: Zweistufiger Prozess

Wenn eine Ladeanfrage in die Warteschlange kommt, werden zwei Operationen nacheinander ausgefuhrt:

- **contentInfoOperation** -- fragt Inhaltslaenge, MIME-Typ und Byte-Bereich-Unterstutzung ab
- **dataOperation** -- ruft Dateidaten ab, beginnend vom `requestedOffset`

## Disk-Caching-Strategie

Heruntergeladene Daten werden in eine temporäre Datei auf der Festplatte geschrieben. Nachfolgende Anfragen für denselben Inhalt werden aus diesem Cache bedient, wodurch redundante Netzwerkaufrufe vermieden werden. Dieser Ansatz:

- Reduziert die Bandbreitennutzung
- Ermoglicht nahezu sofortige Wiedergaben
- Unterstutzt Suchoperationen innerhalb zwischengespeicherter Bereiche

## Verarbeitung ausstehender Anfragen

Die Methode `processPendingRequests` fullt das `contentInformationRequest` jeder Anfrage mit Metadaten und liefert zwischengespeicherte Byte-Bereiche. Abgeschlossene Anfragen werden aus der Warteschlange entfernt.

## Quellcode und nachste Schritte

Dieses Tutorial bietet einen allgemeinen Überblick uber die Implementierung von `AVAssetResourceLoaderDelegate` fur Cloud-Audio-Streaming mit benutzerdefinierten Autorisierungs-Headern. Der vollständige Quellcode ist auf [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader) verfügbar.

Dieser Ansatz betreibt die Audio-Streaming-Engine in [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), das Musik von Dropbox, Google Drive, OneDrive, Yandex.Disk und anderen Cloud-Diensten auf iOS und macOS streamt.

## Häufig gestellte Fragen

{{% details title="Wann sollte ich AVAssetResourceLoaderDelegate anstelle einer direkten URL verwenden?" closed="true" %}}
Verwenden Sie es, wenn der Cloud-Dienst benutzerdefinierte Autorisierungs-Header erfordert, wenn Sie Disk-Caching fur gestreamtes Audio benotigen oder wenn Sie eine feingranulare Kontrolle uber das Laden und Puffern von Daten wunschen.
{{% /details %}}

{{% details title="Funktioniert dieser Ansatz mit Swift?" closed="true" %}}
Ja. Das `AVAssetResourceLoaderDelegate`-Protokoll funktioniert in Swift auf die gleiche Weise. Die Objective-C-Beispiele hier lassen sich direkt ubertragen.
{{% /details %}}

{{% details title="Kann ich dies auch fur Video-Streaming verwenden?" closed="true" %}}
Ja. `AVAssetResourceLoaderDelegate` funktioniert mit jedem Medientyp, den AVPlayer unterstuzt, einschliesslich Video. Derselbe benutzerdefinierte Schema-Ansatz gilt.
{{% /details %}}

{{% details title="Wird die Hintergrund-Audio-Wiedergabe unterstuzt?" closed="true" %}}
Ja, solange Sie den Hintergrundmodus "Audio, AirPlay und Bild im Bild" in den Fähigkeiten Ihrer App aktivieren und Ihre `AVAudioSession` korrekt konfigurieren.
{{% /details %}}
