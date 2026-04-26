---
title: "Streaming de Áudio iOS com AVAssetResourceLoader"
date: 2015-06-20
description: "Aprenda a fazer streaming e cache de áudio no iOS usando AVAssetResourceLoaderDelegate e AVPlayer com esquemas de URL personalizados e cache em disco."
keywords: ["streaming de áudio iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "tutorial AVPlayer", "AVFoundation áudio", "AVAssetResourceLoadingRequest", "player de áudio personalizado iOS", "streaming de áudio na nuvem iOS", "cache de áudio iOS", "Swift AVPlayer esquema personalizado"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**TL;DR:** Use `AVAssetResourceLoaderDelegate` com um esquema de URL personalizado para interceptar o carregamento de recursos do AVPlayer. Isso permite adicionar cabeçalhos de autorização personalizados para serviços na nuvem, fazer cache de áudio em disco e controlar o comportamento do streaming -- tudo sem escrever um proxy HTTP local. O código-fonte completo está no [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Por que o AVPlayer precisa de um carregador de recursos personalizado

`AVPlayer` reproduz áudio de arquivos locais e URLs remotas. Para a maioria dos serviços na nuvem (Dropbox, Google Drive, Box), você pode passar uma URL de download direto e a reprodução funciona imediatamente.

No entanto, alguns serviços como **Yandex.Disk** e **WebDAV** exigem cabeçalhos de autorização personalizados nas solicitações GET. O `AVPlayer` não oferece nenhuma maneira integrada de injetar esses cabeçalhos.

A solução: use a propriedade `resourceLoader` de `AVURLAsset`. Esta API intercepta solicitações de carregamento de recursos, funcionando como um proxy HTTP local sem a complexidade associada.

### Como funciona

`AVPlayer` usa `resourceLoader` quando não reconhece o esquema de URL. Ao substituir `https://` por um esquema personalizado (ex.: `customscheme://`), você força o AVPlayer a delegar todo o carregamento ao seu aplicativo.

Você precisa implementar dois métodos de `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- chamado quando o AVPlayer precisa de dados. Salve o `AVAssetResourceLoadingRequest` e inicie sua operação de carregamento de dados.
2. **`resourceLoader:didCancelLoadingRequest:`** -- chamado quando uma solicitação é cancelada ou substituída.

## Como criar um AVPlayer personalizado

Configure um AVPlayer com um esquema de URL personalizado:

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
- Define uma URL com seu esquema personalizado
- Cria um `AVURLAsset` com um delegate na fila principal
- Constrói um `AVPlayerItem` a partir do asset
- Inicializa o `AVPlayer`

## Implementando o delegate do carregador de recursos

Crie uma classe chamada `LSFilePlayerResourceLoader` para lidar com a busca de dados do servidor e repassá-los ao `AVURLAsset`. Armazene instâncias do carregador em um dicionário indexado pela URL do recurso.

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

Esses métodos verificam o esquema de URL, criam ou recuperam um carregador e adicionam a solicitação à fila do carregador. Esquemas não reconhecidos retornam `NO`.

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

## Carregamento de dados: processo em duas etapas

Quando uma solicitação de carregamento entra na fila, duas operações são executadas em sequência:

- **contentInfoOperation** -- consulta o tamanho do conteúdo, o tipo MIME e o suporte a intervalos de bytes
- **dataOperation** -- busca os dados do arquivo a partir do `requestedOffset`

## Estratégia de cache em disco

Os dados baixados são gravados em um arquivo temporário no disco. Solicitações subsequentes para o mesmo conteúdo são atendidas a partir desse cache, evitando chamadas de rede redundantes. Esta abordagem:

- Reduz o uso de largura de banda
- Permite reproduções quase instantâneas
- Suporta operações de busca dentro de intervalos em cache

## Processando solicitações pendentes

O método `processPendingRequests` preenche o `contentInformationRequest` de cada solicitação com metadados e entrega intervalos de bytes em cache. As solicitações concluídas são removidas da fila.

## Código-fonte e próximos passos

Este tutorial fornece uma visão geral de alto nível sobre a implementação de `AVAssetResourceLoaderDelegate` para streaming de áudio na nuvem com cabeçalhos de autorização personalizados. O código-fonte completo está disponível no [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Essa abordagem alimenta o mecanismo de streaming de áudio do [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), que transmite música do Dropbox, Google Drive, OneDrive, Yandex.Disk e outros serviços na nuvem no iOS e macOS.

## Perguntas frequentes

{{% details title="Quando devo usar AVAssetResourceLoaderDelegate em vez de uma URL direta?" closed="true" %}}
Use-o quando o serviço na nuvem exigir cabeçalhos de autorização personalizados, quando você precisar de cache em disco para áudio transmitido ou quando quiser controle detalhado sobre como os dados são carregados e armazenados em buffer.
{{% /details %}}

{{% details title="Essa abordagem funciona com Swift?" closed="true" %}}
Sim. O protocolo `AVAssetResourceLoaderDelegate` funciona da mesma forma em Swift. Os exemplos em Objective-C se traduzem diretamente.
{{% /details %}}

{{% details title="Posso usar isso para streaming de vídeo também?" closed="true" %}}
Sim. `AVAssetResourceLoaderDelegate` funciona com qualquer tipo de mídia suportado pelo AVPlayer, incluindo vídeo. A mesma abordagem de esquema personalizado se aplica.
{{% /details %}}

{{% details title="Isso suporta reprodução de áudio em segundo plano?" closed="true" %}}
Sim, desde que você ative o modo de segundo plano "Áudio, AirPlay e Picture in Picture" nas capacidades do seu aplicativo e configure corretamente o `AVAudioSession`.
{{% /details %}}
