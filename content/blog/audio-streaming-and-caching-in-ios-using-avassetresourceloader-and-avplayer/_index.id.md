---
title: "iOS Audio Streaming dengan AVAssetResourceLoader"
date: 2015-06-20
description: "Pelajari cara melakukan streaming dan cache audio di iOS menggunakan AVAssetResourceLoaderDelegate dan AVPlayer dengan skema URL kustom dan cache disk."
keywords: ["iOS audio streaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "tutorial AVPlayer", "AVFoundation audio", "AVAssetResourceLoadingRequest", "pemutar audio kustom iOS", "cloud audio streaming iOS", "cache audio iOS", "Swift AVPlayer skema kustom"]
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

**TL;DR:** Gunakan `AVAssetResourceLoaderDelegate` dengan skema URL kustom untuk mencegat pemuatan sumber daya AVPlayer. Ini memungkinkan Anda menambahkan header otorisasi kustom untuk layanan cloud, menyimpan audio ke disk, dan mengontrol perilaku streaming -- semuanya tanpa menulis proxy HTTP lokal. Kode sumber lengkap tersedia di [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Mengapa AVPlayer Memerlukan Resource Loader Kustom?

`AVPlayer` memutar audio dari file lokal dan URL jarak jauh. Untuk sebagian besar layanan cloud (Dropbox, Google Drive, Box), Anda dapat meneruskan URL unduhan langsung dan pemutaran berjalan secara otomatis.

Namun, beberapa layanan seperti **Yandex.Disk** dan **WebDAV** memerlukan header otorisasi kustom pada permintaan GET. `AVPlayer` tidak menyediakan cara bawaan untuk menyuntikkan header ini.

Solusinya: gunakan properti `resourceLoader` dari `AVURLAsset`. API ini mencegat permintaan pemuatan sumber daya, bertindak seperti proxy HTTP lokal tanpa kerumitannya.

### Cara Kerjanya

`AVPlayer` menggunakan `resourceLoader` ketika tidak mengenali skema URL. Dengan mengganti `https://` dengan skema kustom (misalnya `customscheme://`), Anda memaksa AVPlayer untuk mendelegasikan semua pemuatan ke aplikasi Anda.

Anda perlu mengimplementasikan dua metode `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- dipanggil saat AVPlayer membutuhkan data. Simpan `AVAssetResourceLoadingRequest` dan mulai operasi pemuatan data Anda.
2. **`resourceLoader:didCancelLoadingRequest:`** -- dipanggil saat permintaan dibatalkan atau digantikan.

## Cara Membuat AVPlayer Kustom

Siapkan AVPlayer dengan skema URL kustom:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Kode ini:
- Mendefinisikan URL dengan skema kustom Anda
- Membuat `AVURLAsset` dengan delegasi pada antrean utama
- Membangun `AVPlayerItem` dari aset
- Menginisialisasi `AVPlayer`

## Mengimplementasikan Delegasi Resource Loader

Buat kelas bernama `LSFilePlayerResourceLoader` untuk menangani pengambilan data dari server dan meneruskannya kembali ke `AVURLAsset`. Simpan instans loader dalam kamus yang dikunci berdasarkan URL sumber daya.

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

Metode-metode ini memeriksa skema URL, membuat atau mengambil loader, dan menambahkan permintaan ke antrean loader. Skema yang tidak dikenali mengembalikan `NO`.

## Antarmuka LSFilePlayerResourceLoader

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

Ketika permintaan pemuatan masuk ke antrean, dua operasi dijalankan secara berurutan:

- **contentInfoOperation** -- mengambil panjang konten, tipe MIME, dan dukungan rentang byte
- **dataOperation** -- mengambil data file mulai dari `requestedOffset`

## Strategi Cache Disk

Data yang diunduh ditulis ke file sementara di disk. Permintaan berikutnya untuk konten yang sama dilayani dari cache ini, menghindari panggilan jaringan yang tidak perlu. Pendekatan ini:

- Mengurangi penggunaan bandwidth
- Memungkinkan pemutaran ulang yang hampir instan
- Mendukung operasi seek dalam rentang yang telah di-cache

## Memproses Permintaan yang Tertunda

Metode `processPendingRequests` mengisi `contentInformationRequest` setiap permintaan dengan metadata dan mengirimkan rentang byte yang telah di-cache. Permintaan yang selesai dihapus dari antrean.

## Kode Sumber dan Langkah Selanjutnya

Tutorial ini memberikan gambaran tingkat tinggi tentang implementasi `AVAssetResourceLoaderDelegate` untuk streaming audio cloud dengan header otorisasi kustom. Kode sumber lengkap tersedia di [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Pendekatan ini mendukung mesin streaming audio di [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), yang melakukan streaming musik dari Dropbox, Google Drive, OneDrive, Yandex.Disk, dan layanan cloud lainnya di iOS dan macOS.

## Pertanyaan yang Sering Diajukan

{{% details title="Kapan sebaiknya menggunakan AVAssetResourceLoaderDelegate daripada URL langsung?" closed="true" %}}
Gunakan ketika layanan cloud memerlukan header otorisasi kustom, ketika Anda membutuhkan cache disk untuk audio yang di-stream, atau ketika Anda menginginkan kontrol mendetail atas cara data dimuat dan di-buffer.
{{% /details %}}

{{% details title="Apakah pendekatan ini bekerja dengan Swift?" closed="true" %}}
Ya. Protokol `AVAssetResourceLoaderDelegate` bekerja dengan cara yang sama di Swift. Contoh Objective-C di sini dapat diterjemahkan secara langsung.
{{% /details %}}

{{% details title="Bisakah ini digunakan untuk streaming video juga?" closed="true" %}}
Ya. `AVAssetResourceLoaderDelegate` bekerja dengan semua jenis media yang didukung AVPlayer, termasuk video. Pendekatan skema kustom yang sama berlaku.
{{% /details %}}

{{% details title="Apakah ini mendukung pemutaran audio di latar belakang?" closed="true" %}}
Ya, selama Anda mengaktifkan mode latar belakang "Audio, AirPlay, and Picture in Picture" di kemampuan aplikasi Anda dan mengonfigurasi `AVAudioSession` dengan benar.
{{% /details %}}
