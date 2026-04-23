---
title: "Streaming de audio en iOS con AVAssetResourceLoader"
date: 2015-06-20
description: "Aprenda a hacer streaming y almacenamiento en caché de audio en iOS usando AVAssetResourceLoaderDelegate y AVPlayer con esquemas de URL personalizados y caché en disco."
keywords: ["streaming de audio iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "tutorial AVPlayer", "AVFoundation audio", "AVAssetResourceLoadingRequest", "reproductor de audio personalizado iOS", "streaming de audio en la nube iOS", "caché de audio iOS", "Swift AVPlayer esquema personalizado"]
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

**TL;DR:** Use `AVAssetResourceLoaderDelegate` con un esquema de URL personalizado para interceptar la carga de recursos de AVPlayer. Esto le permite agregar cabeceras de autorización personalizadas para servicios en la nube, almacenar audio en caché en el disco y controlar el comportamiento del streaming -- todo sin necesidad de escribir un proxy HTTP local. El código fuente completo está en [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Por qué AVPlayer Necesita un Resource Loader Personalizado

`AVPlayer` reproduce audio desde archivos locales y URLs remotas. Para la mayoría de los servicios en la nube (Dropbox, Google Drive, Box), puede pasar una URL de descarga directa y la reproducción funciona de inmediato.

Sin embargo, algunos servicios como **Yandex.Disk** y **WebDAV** requieren cabeceras de autorización personalizadas en las solicitudes GET. `AVPlayer` no proporciona ninguna forma integrada de inyectar estas cabeceras.

La solución: use la propiedad `resourceLoader` de `AVURLAsset`. Esta API intercepta las solicitudes de carga de recursos, actuando como un proxy HTTP local sin la complejidad.

### Cómo Funciona

`AVPlayer` usa `resourceLoader` cuando no reconoce el esquema de URL. Al reemplazar `https://` con un esquema personalizado (p. ej., `customscheme://`), se fuerza a AVPlayer a delegar toda la carga en su aplicación.

Necesita implementar dos métodos de `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- se llama cuando AVPlayer necesita datos. Guarde el `AVAssetResourceLoadingRequest` e inicie su operación de carga de datos.
2. **`resourceLoader:didCancelLoadingRequest:`** -- se llama cuando una solicitud es cancelada o superada.

## Cómo Crear un AVPlayer Personalizado

Configure un AVPlayer con un esquema de URL personalizado:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Este código:
- Define una URL con su esquema personalizado
- Crea un `AVURLAsset` con un delegate en la cola principal
- Construye un `AVPlayerItem` a partir del asset
- Inicializa `AVPlayer`

## Implementación del Delegate del Resource Loader

Cree una clase llamada `LSFilePlayerResourceLoader` para gestionar la obtención de datos del servidor y entregarlos de vuelta a `AVURLAsset`. Almacene las instancias del loader en un diccionario con clave la URL del recurso.

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

Estos métodos verifican el esquema de URL, crean o recuperan un loader y agregan la solicitud a la cola del loader. Los esquemas no reconocidos devuelven `NO`.

## Interfaz de LSFilePlayerResourceLoader

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

## Carga de Datos: Proceso de Dos Pasos

Cuando una solicitud de carga entra en la cola, se ejecutan dos operaciones en secuencia:

- **contentInfoOperation** -- consulta la longitud del contenido, el tipo MIME y la compatibilidad con rangos de bytes
- **dataOperation** -- obtiene los datos del archivo comenzando desde el `requestedOffset`

## Estrategia de Caché en Disco

Los datos descargados se escriben en un archivo temporal en el disco. Las solicitudes posteriores del mismo contenido se sirven desde esta caché, evitando llamadas de red redundantes. Este enfoque:

- Reduce el uso de ancho de banda
- Permite reproducciones casi instantáneas
- Admite operaciones de búsqueda dentro de rangos almacenados en caché

## Procesamiento de Solicitudes Pendientes

El método `processPendingRequests` rellena el `contentInformationRequest` de cada solicitud con metadatos y entrega rangos de bytes almacenados en caché. Las solicitudes completadas se eliminan de la cola.

## Código Fuente y Próximos Pasos

Este tutorial ofrece una descripción general de alto nivel sobre la implementación de `AVAssetResourceLoaderDelegate` para streaming de audio en la nube con cabeceras de autorización personalizadas. El código fuente completo está disponible en [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Este enfoque impulsa el motor de streaming de audio en [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), que transmite música desde Dropbox, Google Drive, OneDrive, Yandex.Disk y otros servicios en la nube en iOS y macOS.

## Preguntas Frecuentes

{{% details title="¿Cuándo debo usar AVAssetResourceLoaderDelegate en lugar de una URL directa?" closed="true" %}}
Úselo cuando el servicio en la nube requiere cabeceras de autorización personalizadas, cuando necesita caché en disco para el audio en streaming, o cuando desea un control detallado sobre cómo se cargan y almacenan en búfer los datos.
{{% /details %}}

{{% details title="¿Funciona este enfoque con Swift?" closed="true" %}}
Sí. El protocolo `AVAssetResourceLoaderDelegate` funciona de la misma manera en Swift. Los ejemplos de Objective-C aquí se traducen directamente.
{{% /details %}}

{{% details title="¿Puedo usar esto también para streaming de video?" closed="true" %}}
Sí. `AVAssetResourceLoaderDelegate` funciona con cualquier tipo de medio que AVPlayer soporte, incluido el video. El mismo enfoque de esquema personalizado se aplica.
{{% /details %}}

{{% details title="¿Se admite la reproducción de audio en segundo plano?" closed="true" %}}
Sí, siempre que habilite el modo de fondo "Audio, AirPlay y Imagen en Imagen" en las capacidades de su aplicación y configure correctamente su `AVAudioSession`.
{{% /details %}}
