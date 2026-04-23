---
title: "iOS-äänisuoratoisto AVAssetResourceLoaderilla"
date: 2015-06-20
description: "Opi suoratoistamaan ja välimuistittamaan ääntä iOS:ssa käyttämällä AVAssetResourceLoaderDelegate- ja AVPlayer-komponentteja mukautetuilla URL-skeemoilla ja levyvälimuistilla."
keywords: ["iOS äänisuoratoisto", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer opas", "AVFoundation ääni", "AVAssetResourceLoadingRequest", "mukautettu äänisoitin iOS", "pilvipalvelun äänisuoratoisto iOS", "äänivälimuisti iOS", "Swift AVPlayer mukautettu skeema"]
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

**TL;DR:** Käytä `AVAssetResourceLoaderDelegate`-protokollaa mukautetun URL-skeeman kanssa siepaten AVPlayerin resurssien lataaminen. Tämä mahdollistaa mukautettujen valtuutusotsikoiden lisäämisen pilvipalveluille, äänen välimuistittamisen levylle ja suoratoistokäyttäytymisen hallinnan -- ilman paikallisen HTTP-proxyn kirjoittamista. Koko lähdekoodi on saatavilla [GitHubissa](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Miksi AVPlayer Tarvitsee Mukautetun Resource Loaderin

`AVPlayer` toistaa ääntä paikallisista tiedostoista ja etä-URL-osoitteista. Useimmille pilvipalveluille (Dropbox, Google Drive, Box) voit välittää suoran latauslinkin ja toisto toimii heti.

Jotkut palvelut, kuten **Yandex.Disk** ja **WebDAV**, vaativat kuitenkin mukautettuja valtuutusotsikoita GET-pyyntoihin. `AVPlayer` ei tarjoa sisäänrakennettua tapaa lisätä näitä otsikoita.

Ratkaisu: käytä `AVURLAsset`-kohteen `resourceLoader`-ominaisuutta. Tämä API sieppaa resurssien latauspyynnöt toimien kuin paikallinen HTTP-proxy ilman sen monimutkaisuutta.

### Miten Se Toimii

`AVPlayer` käyttää `resourceLoader`-komponenttia, kun se ei tunnista URL-skeemaa. Korvaamalla `https://` mukautetulla skeemalla (esim. `customscheme://`) pakotat AVPlayerin delegoimaan kaiken lataamisen sovelluksellesi.

Sinun täytyy toteuttaa kaksi `AVAssetResourceLoaderDelegate`-metodia:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- kutsutaan, kun AVPlayer tarvitsee dataa. Tallenna `AVAssetResourceLoadingRequest` ja käynnistä datan latausoperaatio.
2. **`resourceLoader:didCancelLoadingRequest:`** -- kutsutaan, kun pyynto peruutetaan tai korvataan.

## Mukautetun AVPlayerin Luominen

Aseta AVPlayer mukautetulla URL-skeemalla:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Tämä koodi:
- Määrittelee URL-osoitteen mukautetulla skeemalla
- Luo `AVURLAsset`-kohteen delegatella paasäikeessä
- Rakentaa `AVPlayerItem`-kohteen assetista
- Alustaa `AVPlayer`-soittimen

## Resource Loader Delegate -toteutus

Luo luokka nimeltä `LSFilePlayerResourceLoader` hoitamaan datan hakemista palvelimelta ja sen palauttamista `AVURLAsset`-kohteelle. Tallenna loader-instanssit sanakirjaan resurssien URL-osoitteen mukaan.

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

Nämä metodit tarkistavat URL-skeeman, luovat tai hakevat loaderin ja lisäävät pyynnön loaderin jonoon. Tunnistamattomille skeemoille palautetaan `NO`.

## LSFilePlayerResourceLoader-rajapinta

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

## Datan Lataus: Kaksivaiheinen Prosessi

Kun latauspyynto saapuu jonoon, kaksi operaatiota suoritetaan järjestyksessä:

- **contentInfoOperation** -- kyselee sisallon pituuden, MIME-tyypin ja tavualueen tuen
- **dataOperation** -- hakee tiedostodatan alkaen `requestedOffset`-kohdasta

## Levyvälimuistitusstrategia

Ladattu data kirjoitetaan väliaikaiseen tiedostoon levylle. Myohemmät pyynnot samalle sisallolle palvellaan tästä välimuistista, mikä välttää tarpeettomia verkkokyselyitä. Tämä lähestymistapa:

- Vähentää kaistanleveyden käyttöä
- Mahdollistaa lähes välittömät uusinnat
- Tukee hakuoperaatioita välimuistitettujen alueiden sisällä

## Odottavien Pyyntojen Käsittely

`processPendingRequests`-metodi täyttää jokaisen pyynnon `contentInformationRequest`-kohteen metadatalla ja toimittaa välimuistitetut tavualueet. Valmiit pyynnöt poistetaan jonosta.

## Lähdekoodi ja Seuraavat Vaiheet

Tämä opas tarjoaa korkean tason yleiskatsauksen `AVAssetResourceLoaderDelegate`-protokollan toteuttamiseen pilvipalvelun äänisuoratoistoon mukautetuilla valtuutusotsikoilla. Koko lähdekoodi on saatavilla [GitHubissa](http://github.com/leshkoapps/AVAssetResourceLoader).

Tämä lähestymistapa toimii [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198)-sovelluksen äänisuoratoistomoottorin pohjana, joka suoratoistaa musiikkia Dropboxista, Google Drivesta, OneDrivesta, Yandex.Diskista ja muista pilvipalveluista iOS:ssa ja macOS:ssa.

## Usein Kysytyt Kysymykset

{{% details title="Milloin minun pitäisi käyttää AVAssetResourceLoaderDelegate-protokollaa suoran URL-osoitteen sijaan?" closed="true" %}}
Käytä sitä, kun pilvipalvelu vaatii mukautettuja valtuutusotsikoita, kun tarvitset levyvälimuistitusta suoratoistetulle äänelle tai kun haluat tarkan hallinnan siitä, miten data ladataan ja puskuroidaan.
{{% /details %}}

{{% details title="Toimiiko tämä lähestymistapa Swiftin kanssa?" closed="true" %}}
Kyllä. `AVAssetResourceLoaderDelegate`-protokolla toimii samalla tavalla Swiftissä. Tämän artikkelin Objective-C-esimerkit kääntyvät suoraan.
{{% /details %}}

{{% details title="Voinko käyttää tätä myös videosuoratoistoon?" closed="true" %}}
Kyllä. `AVAssetResourceLoaderDelegate` toimii minkä tahansa AVPlayerin tukeman mediatyypin kanssa, mukaan lukien video. Sama mukautetun skeeman lähestymistapa pätee.
{{% /details %}}

{{% details title="Tukeeko tämä äänen toistoa taustalla?" closed="true" %}}
Kyllä, kunhan otat käyttöön "Audio, AirPlay ja kuva kuvassa" -taustatilan sovelluksesi ominaisuuksissa ja konfiguroit `AVAudioSession`-kohteen oikein.
{{% /details %}}
