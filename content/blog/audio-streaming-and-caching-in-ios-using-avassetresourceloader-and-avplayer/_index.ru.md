---
title: "Потоковое воспроизведение аудио в iOS с AVAssetResourceLoader"
date: 2015-06-20
description: "Узнайте, как организовать потоковое воспроизведение и кэширование аудио в iOS с помощью AVAssetResourceLoaderDelegate и AVPlayer с пользовательскими схемами URL и кэшем на диске."
keywords: ["потоковое аудио iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "руководство AVPlayer", "AVFoundation аудио", "AVAssetResourceLoadingRequest", "пользовательский аудиоплеер iOS", "потоковое аудио из облака iOS", "кэширование аудио iOS", "Swift AVPlayer пользовательская схема"]
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

**TL;DR:** Используйте `AVAssetResourceLoaderDelegate` с пользовательской схемой URL для перехвата загрузки ресурсов AVPlayer. Это позволяет добавлять пользовательские заголовки авторизации для облачных сервисов, кэшировать аудио на диск и управлять поведением потоковой передачи — без написания локального HTTP-прокси. Полный исходный код доступен на [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Зачем AVPlayer нужен пользовательский загрузчик ресурсов

`AVPlayer` воспроизводит аудио из локальных файлов и удалённых URL. Для большинства облачных сервисов (Dropbox, Google Drive, Box) можно передать прямую ссылку для скачивания, и воспроизведение заработает сразу.

Однако некоторые сервисы, например **Yandex.Disk** и **WebDAV**, требуют пользовательских заголовков авторизации в GET-запросах. `AVPlayer` не предоставляет встроенного способа для их добавления.

Решение: используйте свойство `resourceLoader` класса `AVURLAsset`. Этот API перехватывает запросы на загрузку ресурсов, работая как локальный HTTP-прокси без сопутствующей сложности.

### Как это работает

`AVPlayer` использует `resourceLoader`, когда не распознаёт схему URL. Заменив `https://` на пользовательскую схему (например, `customscheme://`), вы заставляете AVPlayer делегировать всю загрузку вашему приложению.

Необходимо реализовать два метода `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- вызывается, когда AVPlayer нуждается в данных. Сохраните `AVAssetResourceLoadingRequest` и запустите операцию загрузки данных.
2. **`resourceLoader:didCancelLoadingRequest:`** -- вызывается, когда запрос отменяется или заменяется.

## Как создать пользовательский AVPlayer

Настройте AVPlayer с пользовательской схемой URL:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Этот код:
- Определяет URL с вашей пользовательской схемой
- Создаёт `AVURLAsset` с делегатом на главной очереди
- Создаёт `AVPlayerItem` из ассета
- Инициализирует `AVPlayer`

## Реализация делегата загрузчика ресурсов

Создайте класс `LSFilePlayerResourceLoader` для обработки получения данных с сервера и их передачи обратно в `AVURLAsset`. Храните экземпляры загрузчика в словаре с ключом по URL ресурса.

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

Эти методы проверяют схему URL, создают или получают загрузчик и добавляют запрос в очередь загрузчика. Нераспознанные схемы возвращают `NO`.

## Интерфейс LSFilePlayerResourceLoader

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

## Загрузка данных: двухэтапный процесс

Когда запрос на загрузку поступает в очередь, последовательно выполняются две операции:

- **contentInfoOperation** -- запрашивает длину контента, MIME-тип и поддержку диапазонов байт
- **dataOperation** -- получает данные файла начиная с `requestedOffset`

## Стратегия кэширования на диске

Загруженные данные записываются во временный файл на диске. Последующие запросы на тот же контент обслуживаются из этого кэша, что позволяет избежать лишних сетевых вызовов. Такой подход:

- Снижает использование полосы пропускания
- Обеспечивает почти мгновенное повторное воспроизведение
- Поддерживает операции перемотки в пределах кэшированных диапазонов

## Обработка ожидающих запросов

Метод `processPendingRequests` заполняет `contentInformationRequest` каждого запроса метаданными и передаёт кэшированные диапазоны байт. Завершённые запросы удаляются из очереди.

## Исходный код и дальнейшие шаги

Это руководство даёт общий обзор реализации `AVAssetResourceLoaderDelegate` для потокового воспроизведения аудио из облака с пользовательскими заголовками авторизации. Полный исходный код доступен на [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Данный подход лежит в основе механизма потоковой передачи аудио в [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), который транслирует музыку из Dropbox, Google Drive, OneDrive, Yandex.Disk и других облачных сервисов на iOS и macOS.

## Часто задаваемые вопросы

{{% details title="Когда следует использовать AVAssetResourceLoaderDelegate вместо прямого URL?" closed="true" %}}
Используйте его, когда облачный сервис требует пользовательских заголовков авторизации, когда вам нужно кэширование на диске для потокового аудио или когда вы хотите детально управлять тем, как данные загружаются и буферизуются.
{{% /details %}}

{{% details title="Этот подход работает со Swift?" closed="true" %}}
Да. Протокол `AVAssetResourceLoaderDelegate` работает точно так же в Swift. Примеры на Objective-C переносятся напрямую.
{{% /details %}}

{{% details title="Можно ли использовать это для потоковой передачи видео?" closed="true" %}}
Да. `AVAssetResourceLoaderDelegate` работает с любым типом медиа, поддерживаемым AVPlayer, включая видео. Тот же подход с пользовательской схемой применим.
{{% /details %}}

{{% details title="Поддерживается ли фоновое воспроизведение аудио?" closed="true" %}}
Да, при условии что вы включите фоновый режим «Аудио, AirPlay и Картинка в картинке» в возможностях вашего приложения и правильно настроите `AVAudioSession`.
{{% /details %}}
