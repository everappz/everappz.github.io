---
title: "Потокова передача та кешування аудіо в iOS за допомогою AVAssetResourceLoader"
date: 2015-06-20
description: "Дізнайтеся, як організувати потокову передачу та кешування аудіо в iOS за допомогою AVAssetResourceLoaderDelegate та AVPlayer із власними схемами URL і дисковим кешуванням."
keywords: ["потокова передача аудіо iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "підручник AVPlayer", "AVFoundation аудіо", "AVAssetResourceLoadingRequest", "власний аудіоплеєр iOS", "потокове хмарне аудіо iOS", "кешування аудіо iOS", "Swift AVPlayer власна схема"]
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

**TL;DR:** Використовуйте `AVAssetResourceLoaderDelegate` із власною схемою URL, щоб перехоплювати завантаження ресурсів AVPlayer. Це дозволяє додавати власні заголовки авторизації для хмарних сервісів, кешувати аудіо на диск і контролювати поведінку потокової передачі — без написання локального HTTP-проксі. Повний вихідний код доступний на [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Навіщо AVPlayer потрібен власний завантажувач ресурсів

`AVPlayer` відтворює аудіо з локальних файлів і віддалених URL. Для більшості хмарних сервісів (Dropbox, Google Drive, Box) можна передати пряме посилання для завантаження, і відтворення працюватиме одразу.

Однак деякі сервіси, зокрема **Yandex.Disk** та **WebDAV**, вимагають власних заголовків авторизації в GET-запитах. `AVPlayer` не надає вбудованого способу їх вставки.

Рішення: використати властивість `resourceLoader` об'єкта `AVURLAsset`. Цей API перехоплює запити на завантаження ресурсів, діючи як локальний HTTP-проксі, але без зайвої складності.

### Як це працює

`AVPlayer` використовує `resourceLoader`, коли не розпізнає схему URL. Замінивши `https://` на власну схему (наприклад, `customscheme://`), ви змушуєте AVPlayer делегувати все завантаження вашому застосунку.

Потрібно реалізувати два методи `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- викликається, коли AVPlayer потребує даних. Збережіть `AVAssetResourceLoadingRequest` і розпочніть операцію завантаження даних.
2. **`resourceLoader:didCancelLoadingRequest:`** -- викликається, коли запит скасовано або замінено.

## Як створити власний AVPlayer

Налаштуйте AVPlayer із власною схемою URL:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Цей код:
- Визначає URL із власною схемою
- Створює `AVURLAsset` з делегатом у головній черзі
- Будує `AVPlayerItem` на основі ресурсу
- Ініціалізує `AVPlayer`

## Реалізація делегата завантажувача ресурсів

Створіть клас `LSFilePlayerResourceLoader` для отримання даних із сервера та їх передачі до `AVURLAsset`. Зберігайте екземпляри завантажувача у словнику за ключем URL ресурсу.

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

Ці методи перевіряють схему URL, створюють або отримують завантажувач і додають запит до його черги. Нерозпізнані схеми повертають `NO`.

## Інтерфейс LSFilePlayerResourceLoader

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

## Завантаження даних: двоетапний процес

Коли запит на завантаження потрапляє до черги, виконуються дві операції послідовно:

- **contentInfoOperation** -- запитує довжину вмісту, MIME-тип і підтримку діапазонів байтів
- **dataOperation** -- отримує дані файлу починаючи з `requestedOffset`

## Стратегія дискового кешування

Завантажені дані записуються до тимчасового файлу на диску. Наступні запити на той самий вміст обслуговуються з цього кешу, уникаючи зайвих мережевих викликів. Такий підхід:

- Зменшує використання трафіку
- Забезпечує майже миттєве повторне відтворення
- Підтримує операції перемотування в межах кешованих діапазонів

## Обробка очікуючих запитів

Метод `processPendingRequests` заповнює `contentInformationRequest` кожного запиту метаданими та передає кешовані діапазони байтів. Виконані запити видаляються з черги.

## Вихідний код і наступні кроки

Цей підручник надає загальний огляд реалізації `AVAssetResourceLoaderDelegate` для потокової передачі хмарного аудіо з власними заголовками авторизації. Повний вихідний код доступний на [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Цей підхід лежить в основі рушія потокової передачі аудіо в [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), який транслює музику з Dropbox, Google Drive, OneDrive, Yandex.Disk та інших хмарних сервісів на iOS і macOS.

## Часті запитання

{{% details title="Коли варто використовувати AVAssetResourceLoaderDelegate замість прямого URL?" closed="true" %}}
Використовуйте його, коли хмарний сервіс вимагає власних заголовків авторизації, коли потрібне дискове кешування для потокового аудіо або коли ви хочете детально контролювати спосіб завантаження та буферизації даних.
{{% /details %}}

{{% details title="Чи працює цей підхід зі Swift?" closed="true" %}}
Так. Протокол `AVAssetResourceLoaderDelegate` працює однаково у Swift. Наведені приклади на Objective-C безпосередньо перекладаються.
{{% /details %}}

{{% details title="Чи можна використовувати це для потокової передачі відео?" closed="true" %}}
Так. `AVAssetResourceLoaderDelegate` працює з будь-яким типом медіа, який підтримує AVPlayer, включно з відео. Той самий підхід із власною схемою застосовується й тут.
{{% /details %}}

{{% details title="Чи підтримується фонове відтворення аудіо?" closed="true" %}}
Так, за умови що ви ввімкнули фоновий режим "Audio, AirPlay, and Picture in Picture" в можливостях вашого застосунку та правильно налаштували `AVAudioSession`.
{{% /details %}}
