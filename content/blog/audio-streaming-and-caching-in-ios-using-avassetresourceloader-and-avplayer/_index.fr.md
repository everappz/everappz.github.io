---
title: "Streaming audio iOS avec AVAssetResourceLoader"
date: 2015-06-20
description: "Apprenez à diffuser et mettre en cache de l'audio sur iOS avec AVAssetResourceLoaderDelegate et AVPlayer, en utilisant des schémas d'URL personnalisés et un cache sur disque."
keywords: ["streaming audio iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "tutoriel AVPlayer", "audio AVFoundation", "AVAssetResourceLoadingRequest", "lecteur audio personnalisé iOS", "streaming audio cloud iOS", "mise en cache audio iOS", "Swift AVPlayer schéma personnalisé"]
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

**En résumé :** Utilisez `AVAssetResourceLoaderDelegate` avec un schéma d'URL personnalisé pour intercepter le chargement des ressources par AVPlayer. Cela vous permet d'ajouter des en-têtes d'autorisation personnalisés pour les services cloud, de mettre en cache l'audio sur disque et de contrôler le comportement du streaming -- sans écrire de proxy HTTP local. Le code source complet est sur [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Pourquoi AVPlayer a besoin d'un chargeur de ressources personnalisé

`AVPlayer` lit de l'audio depuis des fichiers locaux et des URL distantes. Pour la plupart des services cloud (Dropbox, Google Drive, Box), vous pouvez passer une URL de téléchargement directe et la lecture fonctionne immédiatement.

Cependant, certains services comme **Yandex.Disk** et **WebDAV** exigent des en-têtes d'autorisation personnalisés dans les requêtes GET. `AVPlayer` ne fournit aucun moyen intégré d'injecter ces en-têtes.

La solution : utiliser la propriété `resourceLoader` de `AVURLAsset`. Cette API intercepte les requêtes de chargement de ressources, agissant comme un proxy HTTP local sans la complexité.

### Comment ça fonctionne

`AVPlayer` utilise `resourceLoader` lorsqu'il ne reconnaît pas le schéma d'URL. En remplaçant `https://` par un schéma personnalisé (par ex. `customscheme://`), vous forcez AVPlayer à déléguer tout le chargement à votre application.

Vous devez implémenter deux méthodes `AVAssetResourceLoaderDelegate` :

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- appelée quand AVPlayer a besoin de données. Sauvegardez l'`AVAssetResourceLoadingRequest` et démarrez votre opération de chargement de données.
2. **`resourceLoader:didCancelLoadingRequest:`** -- appelée quand une requête est annulée ou remplacée.

## Comment créer un AVPlayer personnalisé

Configurez un AVPlayer avec un schéma d'URL personnalisé :

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Ce code :
- Définit une URL avec votre schéma personnalisé
- Crée un `AVURLAsset` avec un délégué sur la file principale
- Construit un `AVPlayerItem` à partir de l'asset
- Initialise `AVPlayer`

## Implémentation du délégué du chargeur de ressources

Créez une classe appelée `LSFilePlayerResourceLoader` pour gérer la récupération des données depuis le serveur et les transmettre à `AVURLAsset`. Stockez les instances de chargeur dans un dictionnaire indexé par l'URL de la ressource.

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

Ces méthodes vérifient le schéma d'URL, créent ou récupèrent un chargeur, et ajoutent la requête à la file du chargeur. Les schémas non reconnus retournent `NO`.

## Interface LSFilePlayerResourceLoader

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

## Chargement des données : processus en deux étapes

Lorsqu'une requête de chargement entre dans la file, deux opérations s'exécutent en séquence :

- **contentInfoOperation** -- interroge la longueur du contenu, le type MIME et la prise en charge des plages d'octets
- **dataOperation** -- récupère les données du fichier à partir du `requestedOffset`

## Stratégie de mise en cache sur disque

Les données téléchargées sont écrites dans un fichier temporaire sur disque. Les requêtes suivantes pour le même contenu sont servies depuis ce cache, évitant les appels réseau redondants. Cette approche :

- Réduit la consommation de bande passante
- Permet des relectures quasi instantanées
- Prend en charge les opérations de défilement dans les plages mises en cache

## Traitement des requêtes en attente

La méthode `processPendingRequests` remplit le `contentInformationRequest` de chaque requête avec des métadonnées et fournit les plages d'octets mises en cache. Les requêtes terminées sont supprimées de la file.

## Code source et prochaines étapes

Ce tutoriel offre une vue d'ensemble de l'implémentation d'`AVAssetResourceLoaderDelegate` pour le streaming audio cloud avec des en-têtes d'autorisation personnalisés. Le code source complet est disponible sur [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Cette approche alimente le moteur de streaming audio dans [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), qui diffuse de la musique depuis Dropbox, Google Drive, OneDrive, Yandex.Disk et d'autres services cloud sur iOS et macOS.

## Foire aux questions

{{% details title="Quand utiliser AVAssetResourceLoaderDelegate plutôt qu'une URL directe ?" closed="true" %}}
Utilisez-le lorsque le service cloud exige des en-têtes d'autorisation personnalisés, lorsque vous avez besoin d'un cache disque pour l'audio diffusé, ou lorsque vous souhaitez un contrôle précis sur la façon dont les données sont chargées et mises en mémoire tampon.
{{% /details %}}

{{% details title="Cette approche fonctionne-t-elle avec Swift ?" closed="true" %}}
Oui. Le protocole `AVAssetResourceLoaderDelegate` fonctionne de la même manière en Swift. Les exemples Objective-C présentés ici se traduisent directement.
{{% /details %}}

{{% details title="Puis-je utiliser ceci pour le streaming vidéo aussi ?" closed="true" %}}
Oui. `AVAssetResourceLoaderDelegate` fonctionne avec tout type de média pris en charge par AVPlayer, y compris la vidéo. La même approche avec un schéma personnalisé s'applique.
{{% /details %}}

{{% details title="Cela prend-il en charge la lecture audio en arrière-plan ?" closed="true" %}}
Oui, à condition d'activer le mode d'arrière-plan « Audio, AirPlay et Image dans l'image » dans les capacités de votre application et de configurer correctement votre `AVAudioSession`.
{{% /details %}}
