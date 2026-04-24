---
title: "iOS Audio Streaming s AVAssetResourceLoader"
date: 2015-06-20
description: "Naučte sa streamovať a cachovať zvuk v iOS pomocou AVAssetResourceLoaderDelegate a AVPlayer s vlastnými URL schémami a ukladaním na disk."
keywords: ["iOS audio streaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer tutoriál", "AVFoundation audio", "AVAssetResourceLoadingRequest", "vlastný audio prehrávač iOS", "cloudový audio streaming iOS", "cachovanie zvuku iOS", "Swift AVPlayer vlastná schéma"]
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

**TL;DR:** Použite `AVAssetResourceLoaderDelegate` s vlastnou URL schémou na zachytenie načítavania zdrojov v AVPlayer. To vám umožní pridať vlastné autorizačné hlavičky pre cloudové služby, cachovať zvuk na disk a kontrolovať správanie streamovania -- bez nutnosti písať lokálny HTTP proxy. Kompletný zdrojový kód je na [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Prečo AVPlayer potrebuje vlastný resource loader

`AVPlayer` prehráva zvuk z lokálnych súborov a vzdialených URL adries. Pre väčšinu cloudových služieb (Dropbox, Google Drive, Box) môžete odovzdať priamu URL na stiahnutie a prehrávanie funguje hneď.

Niektoré služby ako **Yandex.Disk** a **WebDAV** však vyžadujú vlastné autorizačné hlavičky pri GET požiadavkách. `AVPlayer` neposkytuje žiadny vstavaný spôsob, ako tieto hlavičky vložiť.

Riešenie: použite vlastnosť `resourceLoader` triedy `AVURLAsset`. Toto API zachytáva požiadavky na načítanie zdrojov a funguje ako lokálny HTTP proxy bez jeho zložitosti.

### Ako to funguje

`AVPlayer` používa `resourceLoader`, keď nerozpozná URL schému. Nahradením `https://` vlastnou schémou (napr. `customscheme://`) prinútite AVPlayer delegovať všetko načítavanie na vašu aplikáciu.

Potrebujete implementovať dve metódy `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- volá sa, keď AVPlayer potrebuje dáta. Uložte `AVAssetResourceLoadingRequest` a spustite operáciu načítavania dát.
2. **`resourceLoader:didCancelLoadingRequest:`** -- volá sa, keď je požiadavka zrušená alebo nahradená.

## Ako vytvoriť vlastný AVPlayer

Nastavte AVPlayer s vlastnou URL schémou:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Tento kód:
- Definuje URL s vašou vlastnou schémou
- Vytvorí `AVURLAsset` s delegátom v hlavnom fronte
- Zostrojí `AVPlayerItem` z asset-u
- Inicializuje `AVPlayer`

## Implementácia delegáta resource loadera

Vytvorte triedu `LSFilePlayerResourceLoader` na spracovanie načítavania dát zo servera a ich odovzdanie späť do `AVURLAsset`. Ukladajte inštancie loadera do slovníka s kľúčom podľa URL zdroja.

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

Tieto metódy skontrolujú URL schému, vytvoria alebo načítajú loader a pridajú požiadavku do frontu loadera. Nerozpoznané schémy vrátia `NO`.

## Rozhranie LSFilePlayerResourceLoader

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

## Načítavanie dát: dvojkrokový proces

Keď požiadavka na načítanie vstúpi do frontu, vykonajú sa postupne dve operácie:

- **contentInfoOperation** -- zisťuje dĺžku obsahu, typ MIME a podporu rozsahu bajtov
- **dataOperation** -- načítava dáta súboru začínajúc od `requestedOffset`

## Stratégia cachovania na disk

Stiahnuté dáta sa zapisujú do dočasného súboru na disku. Následné požiadavky na rovnaký obsah sa obsluhujú z tejto vyrovnávacej pamäte, čím sa predchádzajú zbytočným sieťovým volaniam. Tento prístup:

- Znižuje spotrebu šírky pásma
- Umožňuje takmer okamžité opakované prehrávanie
- Podporuje operácie hľadania v cachovaných rozsahoch

## Spracovanie čakajúcich požiadaviek

Metóda `processPendingRequests` vyplní `contentInformationRequest` každej požiadavky metadátami a doručí cachované rozsahy bajtov. Dokončené požiadavky sú odstránené z frontu.

## Zdrojový kód a ďalšie kroky

Tento tutoriál poskytuje prehľad implementácie `AVAssetResourceLoaderDelegate` pre cloudový audio streaming s vlastnými autorizačnými hlavičkami. Kompletný zdrojový kód je dostupný na [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Tento prístup poháňa engine audio streamovania v [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), ktorý streamuje hudbu z Dropbox, Google Drive, OneDrive, Yandex.Disk a ďalších cloudových služieb na iOS a macOS.

## Často kladené otázky

{{% details title="Kedy mám použiť AVAssetResourceLoaderDelegate namiesto priamej URL?" closed="true" %}}
Použite ho, keď cloudová služba vyžaduje vlastné autorizačné hlavičky, keď potrebujete cachovanie na disk pre streamovaný zvuk, alebo keď chcete jemnú kontrolu nad tým, ako sa dáta načítavajú a ukladajú do vyrovnávacej pamäte.
{{% /details %}}

{{% details title="Funguje tento prístup so Swift?" closed="true" %}}
Áno. Protokol `AVAssetResourceLoaderDelegate` funguje rovnako v Swift. Príklady v Objective-C sa dajú priamo preložiť.
{{% /details %}}

{{% details title="Môžem to použiť aj pre video streaming?" closed="true" %}}
Áno. `AVAssetResourceLoaderDelegate` funguje s akýmkoľvek typom médií, ktorý AVPlayer podporuje, vrátane videa. Rovnaký prístup s vlastnou schémou platí aj tu.
{{% /details %}}

{{% details title="Podporuje to prehrávanie zvuku na pozadí?" closed="true" %}}
Áno, pokiaľ povolíte režim pozadia "Audio, AirPlay a Picture in Picture" v možnostiach vašej aplikácie a správne nakonfigurujete `AVAudioSession`.
{{% /details %}}
