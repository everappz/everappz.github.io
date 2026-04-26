---
title: "Penstriman Audio iOS dengan AVAssetResourceLoader"
date: 2015-06-20
description: "Pelajari cara menstream dan menyimpan cache audio dalam iOS menggunakan AVAssetResourceLoaderDelegate dan AVPlayer dengan skim URL tersuai dan caching cakera."
keywords: ["penstriman audio iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "tutorial AVPlayer", "audio AVFoundation", "AVAssetResourceLoadingRequest", "pemain audio tersuai iOS", "penstriman audio awan iOS", "caching audio iOS", "Swift AVPlayer skim tersuai"]
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

**Ringkasan:** Gunakan `AVAssetResourceLoaderDelegate` dengan skim URL tersuai untuk memintas pemuatan sumber AVPlayer. Ini membolehkan anda menambah pengepala kebenaran tersuai untuk perkhidmatan awan, menyimpan cache audio ke cakera, dan mengawal tingkah laku penstriman -- semua tanpa menulis proksi HTTP setempat. Kod sumber penuh tersedia di [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Mengapa AVPlayer Memerlukan Pemuat Sumber Tersuai

`AVPlayer` memainkan audio daripada fail setempat dan URL jauh. Untuk kebanyakan perkhidmatan awan (Dropbox, Google Drive, Box), anda boleh menghantar URL muat turun terus dan main balik berfungsi dengan serta-merta.

Walau bagaimanapun, sesetengah perkhidmatan seperti **Yandex.Disk** dan **WebDAV** memerlukan pengepala kebenaran tersuai pada permintaan GET. `AVPlayer` tidak menyediakan cara terbina dalam untuk menyuntik pengepala ini.

Penyelesaian: gunakan sifat `resourceLoader` bagi `AVURLAsset`. API ini memintas permintaan pemuatan sumber, bertindak seperti proksi HTTP setempat tanpa kerumitan.

### Cara Ia Berfungsi

`AVPlayer` menggunakan `resourceLoader` apabila ia tidak mengenali skim URL. Dengan menggantikan `https://` dengan skim tersuai (cth. `customscheme://`), anda memaksa AVPlayer untuk mewakilkan semua pemuatan kepada aplikasi anda.

Anda perlu melaksanakan dua kaedah `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- dipanggil apabila AVPlayer memerlukan data. Simpan `AVAssetResourceLoadingRequest` dan mulakan operasi pemuatan data anda.
2. **`resourceLoader:didCancelLoadingRequest:`** -- dipanggil apabila permintaan dibatalkan atau digantikan.

## Cara Membuat AVPlayer Tersuai

Sediakan AVPlayer dengan skim URL tersuai:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Kod ini:
- Menentukan URL dengan skim tersuai anda
- Mencipta `AVURLAsset` dengan delegat pada baris gilir utama
- Membina `AVPlayerItem` daripada aset
- Memulakan `AVPlayer`

## Melaksanakan Delegat Pemuat Sumber

Cipta kelas bernama `LSFilePlayerResourceLoader` untuk mengendalikan pengambilan data daripada pelayan dan menghantarnya semula kepada `AVURLAsset`. Simpan contoh pemuat dalam kamus yang dikunci oleh URL sumber.

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

Kaedah-kaedah ini memeriksa skim URL, mencipta atau mendapatkan semula pemuat, dan menambah permintaan ke dalam baris gilir pemuat. Skim yang tidak dikenali mengembalikan `NO`.

## Antara Muka LSFilePlayerResourceLoader

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

## Pemuatan Data: Proses Dua Langkah

Apabila permintaan pemuatan masuk ke dalam baris gilir, dua operasi dilaksanakan secara berurutan:

- **contentInfoOperation** -- menanya panjang kandungan, jenis MIME, dan sokongan julat bait
- **dataOperation** -- mengambil data fail bermula dari `requestedOffset`

## Strategi Caching Cakera

Data yang dimuat turun ditulis ke fail sementara pada cakera. Permintaan seterusnya untuk kandungan yang sama dilayan daripada cache ini, mengelakkan panggilan rangkaian yang berlebihan. Pendekatan ini:

- Mengurangkan penggunaan lebar jalur
- Membolehkan main semula hampir serta-merta
- Menyokong operasi capaian dalam julat yang dicache

## Memproses Permintaan Tertangguh

Kaedah `processPendingRequests` mengisi `contentInformationRequest` setiap permintaan dengan metadata dan menghantar julat bait yang dicache. Permintaan yang selesai dikeluarkan daripada baris gilir.

## Kod Sumber dan Langkah Seterusnya

Tutorial ini memberikan gambaran keseluruhan pelaksanaan `AVAssetResourceLoaderDelegate` untuk penstriman audio awan dengan pengepala kebenaran tersuai. Kod sumber penuh tersedia di [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Pendekatan ini menjanakan enjin penstriman audio dalam [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), yang menstream muzik daripada Dropbox, Google Drive, OneDrive, Yandex.Disk, dan perkhidmatan awan lain pada iOS dan macOS.

## Soalan Lazim

{{% details title="Bilakah saya perlu menggunakan AVAssetResourceLoaderDelegate berbanding URL terus?" closed="true" %}}
Gunakan apabila perkhidmatan awan memerlukan pengepala kebenaran tersuai, apabila anda memerlukan caching cakera untuk audio yang distream, atau apabila anda mahukan kawalan terperinci ke atas cara data dimuatkan dan dibuffer.
{{% /details %}}

{{% details title="Adakah pendekatan ini berfungsi dengan Swift?" closed="true" %}}
Ya. Protokol `AVAssetResourceLoaderDelegate` berfungsi dengan cara yang sama dalam Swift. Contoh Objective-C di sini diterjemahkan secara langsung.
{{% /details %}}

{{% details title="Bolehkah saya menggunakan ini untuk penstriman video juga?" closed="true" %}}
Ya. `AVAssetResourceLoaderDelegate` berfungsi dengan mana-mana jenis media yang disokong AVPlayer, termasuk video. Pendekatan skim tersuai yang sama digunakan.
{{% /details %}}

{{% details title="Adakah ini menyokong main balik audio latar belakang?" closed="true" %}}
Ya, selagi anda mendayakan mod latar belakang "Audio, AirPlay, dan Picture in Picture" dalam keupayaan aplikasi anda dan mengkonfigurasi `AVAudioSession` anda dengan betul.
{{% /details %}}
