---
title: "Flacbox 7.4: CarPlay Dibangun Ulang, Plex, Jellyfin, Subsonic, SFTP untuk Audio Hi-Res"
date: 2026-05-20
description: "Flacbox 7.4 menghadirkan pengalaman CarPlay yang dibangun ulang dari awal dan menambahkan 10+ cara baru untuk memutar pustaka lossless Anda — Plex, Subsonic, Navidrome, Jellyfin, Emby, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, ditambah FTP, SFTP, dan NFS. Termasuk widget Layar Beranda yang diperbarui, desain Liquid Glass, dan pustaka jaringan yang lebih kuat untuk pemutaran FLAC, DSD, ALAC, dan APE di iPhone dan Mac."
keywords: ["Flacbox 7.4", "pembaruan Flacbox", "pemutar audio hi-res CarPlay", "pemutar FLAC CarPlay iPhone", "musik hi-res Plex iPhone", "streaming lossless Plex", "pemutar FLAC Jellyfin iOS", "musik lossless Emby iOS", "Subsonic FLAC iPhone", "klien lossless Navidrome iOS", "streaming FLAC Internxt", "musik lossless Proton Drive", "pemutar musik hi-res QNAP", "streaming FLAC Nextcloud iOS", "audio lossless Amazon S3 iPhone", "pemutar SFTP FLAC iPhone", "audio hi-res FTP iOS", "streaming lossless NFS iPhone", "stream DSD dari NAS iPhone", "pemutar DSD iPhone 2026", "pemutar ALAC iOS", "pemutar musik lossless iPhone", "aplikasi audio Liquid Glass", "pemutar audio hi-res iOS 2026"]
tags: ["Flacbox", "Flacbox 7.4", "CarPlay", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Widget Layar Beranda", "Liquid Glass", "Audio Hi-Res", "FLAC", "DSD", "ALAC", "Apa yang Baru"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Flacbox 7.4](/products/flacbox) adalah rilis besar untuk pemutar audio hi-res iPhone dan Mac. CarPlay telah dibangun ulang dari nol — pengurutan cepat, beberapa tema warna, layar Sedang Diputar yang baru, antrian putar lengkap dalam sekilas, dan indeks huruf untuk pustaka besar. Pembaruan ini menambahkan 10+ cara baru untuk mengakses musik Anda — cloud yang mengutamakan privasi **Internxt** dan **Proton Drive**, server pribadi **QNAP**, **Nextcloud**, dan **Amazon S3**, server streaming **Plex**, **Subsonic**, **Navidrome**, **Jellyfin**, dan **Emby**, ditambah protokol jaringan **FTP**, **SFTP**, dan **NFS**. Antarmuka disesuaikan untuk material **Liquid Glass** baru dari Apple, pustaka jaringan dasar lebih kuat, dan widget Layar Beranda menyegarkan lebih andal.

---

## Halo semua!

Pembaruan besar Flacbox telah hadir. Kami membangun ulang CarPlay dari awal dan menambahkan lebih dari sepuluh cara baru untuk terhubung ke pustaka lossless Anda — dari penyimpanan cloud yang mengutamakan privasi hingga server media yang di-host sendiri yang populer dan protokol jaringan klasik.

[Unduh Flacbox 7.4 dari App Store](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) atau perbarui dari versi yang sudah ada. Pengguna Mac dapat mengambil [versi desktop di sini](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8).

## CarPlay, Dibangun Ulang dari Awal

Kami mendesain ulang **Apple CarPlay** untuk Flacbox dari awal sehingga mendengarkan di jalan terasa lebih aman dan mudah. Setiap detail — dari cara menemukan lagu hingga cara pemutaran dikontrol — telah disesuaikan kembali untuk pengalaman di dalam mobil.

- **Pengurutan cepat** — capai lagu apa pun dalam sekejap di seluruh album, artis, daftar putar, dan folder tanpa pengguliran tanpa henti.
- **Tema warna yang sesuai dengan mobil Anda** — pilih tema yang cocok dengan dasbor atau pencahayaan interior Anda, siang atau malam.
- **Layar Sedang Diputar yang baru** — sampul lebih besar, kontrol lebih jelas, dan tindakan pemutaran baru yang dapat diakses dengan satu ketukan.
- **Antrian putar lengkap Anda dalam sekilas** — lihat apa yang akan datang tanpa meninggalkan layar saat ini.
- **Indeks huruf untuk pustaka besar** — lompati puluhan ribu trek FLAC, DSD, ALAC, dan APE dengan satu sentuhan.
- **Pemuatan lebih cepat, tidak ada jeda lagi** — membuka folder besar, direktori cloud, atau pustaka server media terasa seketika.

Jika Anda melakukan streaming audio lossless saat berkendara — dari Dropbox, Google Drive, OneDrive, iCloud Drive, [Plex](#media-servers), [Jellyfin](#media-servers), Subsonic, atau sumber lainnya — pengalaman CarPlay yang dibangun ulang membuat seluruh alur terasa native di mobil.

## 10+ Cara Baru untuk Menghubungkan Musik Anda

Flacbox 7.4 memperluas apa yang dianggap sebagai 'pustaka musik' Anda. Jika file hi-res Anda berada di cloud yang Anda percayai, NAS di rumah, atau server streaming yang di-host sendiri, Flacbox sekarang memutar langsung darinya — tanpa sinkronisasi, tanpa ekspor, tanpa konversi format.

### Cloud Pribadi: Internxt dan Proton Drive

Jika enkripsi end-to-end dan penyimpanan zero-knowledge penting bagi Anda, dua cloud yang mengutamakan privasi yang paling dihormati sekarang native di Flacbox:

- **Internxt** — cloud Spanyol open-source, terenkripsi pasca-kuantum, sesuai GDPR. Tingkat gratis tersedia.
- **Proton Drive** — penyimpanan terenkripsi end-to-end dari pembuat Proton Mail dan Proton VPN, berbasis di Swiss. Tingkat gratis tersedia dengan paket berbayar untuk pustaka yang lebih besar.

Hubungkan sekali dan file FLAC, DSD, atau ALAC Anda mengalir melalui terowongan terenkripsi — Flacbox tidak pernah melihat data Anda dalam bentuk teks biasa, begitu juga server penyedia.

### Server Pribadi: QNAP, Nextcloud, Amazon S3

Untuk pendengar yang menjalankan infrastruktur mereka sendiri:

- **QNAP** — koneksi API native ke perangkat QNAP NAS untuk pemutaran cepat dan andal melalui Wi-Fi lokal atau akses jarak jauh. Streamingkan FLAC dan DSD bitrate tinggi langsung tanpa pengkodean ulang.
- **Nextcloud** — terhubung ke instans Nextcloud yang di-host sendiri atau dikelola. Pilihan bagus jika Anda sudah pindah dari Google Drive atau Dropbox karena alasan privasi.
- **Amazon S3** — arahkan Flacbox ke bucket S3 apa pun (atau penyimpanan yang kompatibel dengan S3 seperti Backblaze B2, Wasabi, MinIO, Cloudflare R2) dan streamingkan koleksi Anda langsung.

### <a id="media-servers"></a>Server Streaming: Plex, Subsonic, Navidrome, Jellyfin, Emby

Ini adalah yang utama untuk penggemar musik yang di-host sendiri. Flacbox 7.4 mengubah iPhone atau Mac Anda menjadi klien hi-res kelas satu untuk server media open-source dan freemium yang paling populer:

- **Plex** — Plex Media Server **gratis** untuk diunduh dan dijalankan. Langganan **Plex Pass** bersifat opsional dan membuka sinkronisasi seluler, transcoding perangkat keras, dan ekstra lainnya. Flacbox bekerja dengan pustaka gratis maupun Plex Pass.
- **Subsonic** — server streaming musik asli yang di-host sendiri. Server Subsonic resmi **berbayar** ($1/bulan setelah uji coba 30 hari), dan Flacbox juga berbicara API Subsonic ke puluhan server yang kompatibel.
- **Navidrome** — server musik modern, ringan, **sepenuhnya gratis dan open-source** yang ditulis dalam Go. Mengimplementasikan API Subsonic. Berjalan di Raspberry Pi, NAS, atau kotak Linux apa pun. Sangat direkomendasikan untuk koleksi lossless hingga beberapa ratus ribu trek.
- **Jellyfin** — server media **sepenuhnya gratis dan open-source** (fork komunitas dari Emby). Menangani musik, film, TV, dan buku audio. Tanpa akun, tanpa telemetri, tanpa langganan.
- **Emby** — server media **freemium**. Server inti gratis; **Emby Premiere** adalah pembelian satu kali atau tahunan yang membuka aplikasi seluler, sinkronisasi offline, dan banyak lagi. Flacbox terhubung ke pustaka gratis maupun Premiere.

Server mana pun yang Anda jalankan, Flacbox melakukan streaming seluruh koleksi Anda — album, artis, daftar putar, genre, dan sampul tertanam — dengan output bit-perfect ke DAC USB, equalizer 10 band, crossfade dan pemutaran gapless, AirPlay, Chromecast, dan pengalaman **CarPlay** yang dibangun ulang. Server Anda menyimpan riwayat mendengarkan; Flacbox menghormatinya.

### Metode Transfer Baru: FTP, SFTP, NFS

Untuk pendengar dengan server kustom, lab rumah, atau kotak NAS generik yang tidak dilengkapi aplikasi seluler yang dipoles, Flacbox 7.4 menambahkan tiga protokol jaringan klasik:

- **SFTP (SSH File Transfer Protocol)** — jawaban yang tepat untuk **streaming jarak jauh yang aman dari server Anda sendiri**. SFTP berjalan di atas SSH, sehingga seluruh transfer (autentikasi dan data audio) terenkripsi. Jika Anda memiliki VPS, server khusus, atau kotak Linux di rumah dengan akses SSH, Anda dapat menjatuhkan folder FLAC atau DSD di dalamnya dan melakukan streaming melalui internet publik tanpa mengekspos hal lain. Mendukung autentikasi berbasis kata sandi dan kunci.
- **FTP** — standar lama untuk transfer file. Berguna jika **NAS rumah** Anda (Synology lama, ASUS, D-Link, TerraMaster, atau kotak generik) mengekspos server FTP tetapi tidak memiliki integrasi API native. Paling baik digunakan di dalam jaringan lokal Anda.
- **NFS (Network File System)** — protokol berbagi de facto di Linux dan kebanyakan perangkat NAS. Berbagi NFS umum di lab rumah dan jaringan bisnis kecil; Flacbox sekarang memasangnya dan melakukan streaming audio bit-perfect langsung. Overhead lebih rendah daripada SMB pada perangkat keras yang sama.

> **Tip:** SFTP adalah protokol yang Anda inginkan untuk streaming dari internet terbuka. FTP dan NFS paling baik digunakan di dalam jaringan lokal Anda — jauhkan dari internet publik kecuali Anda membungkusnya dalam VPN.

## Peningkatan Lainnya

### Tampilan Baru yang Sesuai dengan Liquid Glass

Antarmuka Flacbox 7.4 diperbarui untuk material **Liquid Glass** baru dari Apple di seluruh aplikasi — permukaan tembus pandang, animasi yang lebih halus, dan kontrol yang disempurnakan yang cocok secara alami di iOS 26 dan macOS 26. Pustaka, Sedang Diputar, equalizer, dan layar pengaturan semuanya telah disesuaikan kembali untuk estetika sistem baru.

### Pustaka Jaringan yang Lebih Kuat

Kami menyegarkan pustaka dasar yang digunakan Flacbox untuk berkomunikasi dengan **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA**, dan layanan lainnya. Terjemahan: lebih sedikit kegagalan koneksi kasus tepi, dukungan yang lebih baik untuk versi server yang lebih baru, dan keandalan yang lebih baik saat streaming audio bitrate tinggi pada koneksi yang lebih lambat atau jauh secara geografis.

### Pemutaran Diperbaiki pada Beberapa Server

Kami melacak dan memperbaiki beberapa masalah pemutaran pada server tertentu yang di-host sendiri — termasuk macet setelah mencari di file FLAC dan DSD besar, dan waktu mulai yang lambat pada pustaka dengan daftar file yang sangat panjang. Streaming seharusnya terasa lebih bersih end-to-end.

### Widget Layar Beranda Baru dengan Pembaruan Lebih Baik

Widget Layar Beranda — Sedang Diputar, Antrian Pemutaran, Baru Saja Diputar — telah didesain ulang dengan tata letak yang lebih bersih dan kebijakan pembaruan yang lebih cerdas. Mereka tetap selaras dengan aplikasi tanpa membakar baterai ekstra, dan beberapa ukuran widget baru memberi Anda lebih banyak kontrol atas apa yang terlihat sekilas.

### Perbaikan Terjemahan

Banyak perbaikan lokalisasi kecil di beberapa bahasa berdasarkan masukan pengguna langsung. Teks lebih pas pada tombol yang lebih kecil dan pada bahasa Eropa yang lebih panjang (Jerman, Belanda, Prancis, Spanyol).

### Pemolesan Kecil Terinspirasi oleh Pesan Anda

Banyak peningkatan kecil berdasarkan ulasan App Store dan email ke support@everappz.com. Kami membaca setiap pesan.

## Mengapa Pembaruan Ini Penting

Flacbox 7.4 dibangun di sekitar dua ide:

1. **Musik hi-res Anda, di mana pun Anda menyimpannya.** Apakah pustaka lossless Anda berada di iCloud Drive, cloud yang mengutamakan privasi seperti Proton Drive atau Internxt, server media seperti Plex atau Jellyfin, NAS di rumah, atau Raspberry Pi yang menjalankan Navidrome — Flacbox sekarang terhubung dengannya secara native, dengan pengalaman pemutaran bit-perfect yang sama di mana pun.
2. **Lebih baik di mobil.** CarPlay adalah layar yang paling banyak dilihat oleh banyak pendengar, dan pengalaman yang dibangun ulang mencerminkan hal itu — lebih cepat, lebih aman, dan dibangun di sekitar cara pengemudi sungguhan meraih musik mereka.

## Dapatkan Flacbox 7.4

[**Unduh Flacbox dari App Store**](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) atau perbarui dari dalam App Store. [Versi Mac](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8) tersedia secara terpisah sebagai aplikasi Mac universal. Flacbox adalah unduhan gratis dengan peningkatan dalam aplikasi opsional untuk fitur lanjutan. CarPlay yang dibangun ulang, semua koneksi cloud dan server baru, widget Layar Beranda yang diperbarui, dan UI Liquid Glass adalah bagian dari pembaruan dasar.

Jika aplikasi membuat hari Anda lebih baik, peringkat di App Store sangat membantu. Ada pertanyaan atau masalah? Tulis ke **support@everappz.com** dan orang sungguhan akan membalas.

## Pertanyaan yang Sering Diajukan

{{% details title="Apa yang baru di Flacbox 7.4?" closed="true" %}}
Flacbox 7.4 menghadirkan pengalaman CarPlay yang sepenuhnya dibangun ulang dan menambahkan 10+ koneksi baru — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS. Rilis ini juga membawa penyegaran desain Liquid Glass, pustaka jaringan yang lebih kuat, widget Layar Beranda yang didesain ulang dengan pembaruan lebih cerdas, perbaikan pemutaran pada beberapa server, peningkatan terjemahan, dan banyak item pemolesan kecil.
{{% /details %}}

{{% details title="Apakah Flacbox bekerja dengan Plex untuk FLAC dan audio lossless?" closed="true" %}}
Ya. Mulai dari Flacbox 7.4 Anda dapat terhubung ke Plex Media Server dan melakukan streaming seluruh pustaka hi-res Anda — FLAC, ALAC, WAV, AIFF, OGG, OPUS, dan format lossless lainnya. Plex Media Server gratis untuk dijalankan; Plex Pass bersifat opsional. Flacbox mendukung pengaturan gratis dan Plex Pass.
{{% /details %}}

{{% details title="Apakah Jellyfin atau Navidrome didukung di Flacbox?" closed="true" %}}
Ya. Keduanya didukung penuh di Flacbox 7.4. Jellyfin adalah server media gratis dan open-source. Navidrome adalah server musik gratis dan open-source yang mengimplementasikan API Subsonic. Flacbox terhubung dengan keduanya secara native dan melakukan streaming pustaka lossless Anda dengan metadata dan sampul lengkap.
{{% /details %}}

{{% details title="Apakah Plex, Jellyfin, Emby, Navidrome, dan Subsonic gratis?" closed="true" %}}
- **Plex** — server gratis; Plex Pass adalah peningkatan berbayar opsional.
- **Jellyfin** — sepenuhnya gratis dan open-source.
- **Emby** — server gratis; Emby Premiere berbayar dan membuka sinkronisasi seluler dan offline.
- **Navidrome** — sepenuhnya gratis dan open-source.
- **Subsonic** — server resmi berharga $1/bulan setelah uji coba 30 hari, tetapi API-nya terbuka dan banyak server gratis (termasuk Navidrome) mengimplementasikannya.
{{% /details %}}

{{% details title="Bisakah saya streaming FLAC dan DSD dari NAS rumah saya melalui SFTP, FTP, atau NFS?" closed="true" %}}
Ya. Flacbox 7.4 menambahkan SFTP, FTP, dan NFS sebagai tipe koneksi native. SFTP adalah pilihan yang direkomendasikan untuk streaming dari server Anda sendiri melalui internet publik karena semua lalu lintas dienkripsi melalui SSH. FTP dan NFS paling baik digunakan di dalam jaringan lokal Anda atau di belakang VPN.
{{% /details %}}

{{% details title="Bagaimana cara menghubungkan Flacbox ke server kustom menggunakan SFTP?" closed="true" %}}
Buka Flacbox, buka tab Connections, pilih SFTP, dan masukkan nama host atau IP server Anda, port (biasanya 22), nama pengguna, dan kata sandi atau kunci pribadi SSH. Flacbox akan menjelajahi folder jarak jauh Anda dan melakukan streaming file audio langsung dengan enkripsi end-to-end.
{{% /details %}}

{{% details title="Apakah Flacbox mendukung Internxt dan Proton Drive?" closed="true" %}}
Ya. Kedua cloud yang berfokus pada privasi didukung mulai dari Flacbox 7.4. Mereka bergabung dengan MEGA dan layanan yang mengutamakan privasi lainnya yang sudah tersedia di aplikasi.
{{% /details %}}

{{% details title="Apakah Flacbox memutar file DSD dari Plex, Jellyfin, atau NAS?" closed="true" %}}
Ya. Flacbox memutar file DSD64, DSD128, dan DSD256 (kontainer DSF dan DFF) yang di-stream dari Plex, Jellyfin, Emby, server yang kompatibel dengan Subsonic, QNAP, Nextcloud, Amazon S3, dan melalui SFTP, FTP, dan NFS. Output bit-perfect ke DAC USB didukung di iPhone, iPad, dan Mac.
{{% /details %}}

{{% details title="Bagaimana cara kerja layar CarPlay yang didesain ulang?" closed="true" %}}
Antarmuka CarPlay Flacbox telah dibangun ulang dengan pengurutan cepat di album, artis, daftar putar, dan folder; beberapa tema warna yang cocok dengan berbagai interior mobil; layar Sedang Diputar yang baru dengan kontrol baru; antrian putar lengkap dalam sekilas; indeks huruf untuk melompat ke pustaka besar; dan pemuatan lebih cepat pada folder besar dan direktori cloud.
{{% /details %}}

{{% details title="Apakah pembaruan Flacbox 7.4 gratis?" closed="true" %}}
Ya. Flacbox adalah unduhan gratis dari App Store, dan 7.4 adalah pembaruan gratis untuk semua pengguna yang ada. CarPlay yang dibangun ulang, semua koneksi cloud dan server baru, widget Layar Beranda yang diperbarui, dan UI Liquid Glass adalah bagian dari pembaruan dasar.
{{% /details %}}

{{% details title="Di perangkat mana saja Flacbox 7.4 tersedia?" closed="true" %}}
Flacbox 7.4 berjalan di iPhone, iPad, dan Mac. Dukungan CarPlay memerlukan kendaraan atau head unit aftermarket yang kompatibel dengan CarPlay. AirPlay dan Chromecast memungkinkan Anda melakukan cast pemutaran ke sistem yang lebih besar; DAC USB didukung untuk output lossless bit-perfect.
{{% /details %}}
