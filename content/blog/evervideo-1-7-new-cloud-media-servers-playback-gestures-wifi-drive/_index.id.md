---
title: "Evervideo 1.7: Plex, Jellyfin, streaming cloud, dan gestur pemutaran baru"
date: 2026-05-18
description: "Evervideo 1.7 menambahkan 10+ koneksi baru — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — plus gestur pemutaran baru (ketuk ganda untuk maju/mundur, ketuk dan tahan untuk kecepatan 2x), Wi-Fi Drive yang disegarkan dengan unggah massal, dan pembaruan UI Liquid Glass untuk iPhone, iPad, dan Mac."
keywords: ["Evervideo 1.7", "pembaruan Evervideo", "pemutar video HD iPhone", "pemutar video Plex iOS", "video Jellyfin iPhone", "pemutar video Emby iOS", "video Subsonic iOS", "video Navidrome iOS", "streaming video Internxt", "pemutar video Proton Drive", "pemutar video QNAP iPhone", "pemutar video Nextcloud iOS", "streaming video Amazon S3", "pemutar video SFTP iPhone", "pemutar video FTP iOS", "streaming video NFS iPhone", "streaming video dari NAS iPhone", "pemutar MKV iPhone", "gestur pemutar video iOS", "ketuk ganda untuk mencari video", "transfer video Wi-Fi Drive iPhone", "desain Liquid Glass", "pemutar video cloud iOS 2026", "streaming film dari cloud iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Gestur Pemutaran", "Liquid Glass", "Apa yang baru"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evervideo 1.7](/products/evervideo) adalah pembaruan besar untuk pemutar video HD di iPhone, iPad, dan Mac. Rilis ini menambahkan 10+ koneksi cloud, NAS, dan media server baru — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, plus media server paling populer **Plex**, **Subsonic**, **Navidrome**, **Jellyfin**, dan **Emby**, serta tiga protokol jaringan: **FTP**, **SFTP**, dan **NFS**. **Gestur pemutaran** baru memungkinkan Anda ketuk ganda untuk melompat maju atau mundur, ketuk dan tahan untuk berjalan pada 2x, dan ketuk sekali untuk mengaktifkan/menonaktifkan kontrol — semua tanpa keluar dari layar penuh. Wi-Fi Drive mendapat UI yang disegarkan dengan mode pemilihan dan antrean unggah yang lebih pintar. Seluruh aplikasi disesuaikan untuk desain **Liquid Glass** baru dari Apple.

---

## Halo semua!

Pembaruan besar Evervideo hadir. Ini adalah salah satu rilis terbesar yang pernah kami kirim: **10+ koneksi cloud, server, dan jaringan baru**, **gestur pemutaran** baru untuk kontrol lebih cepat dalam mode layar penuh, pengalaman **Wi-Fi Drive** yang disegarkan, dan UI yang disesuaikan untuk **Liquid Glass** di iPhone, iPad, dan Mac.

[Unduh Evervideo 1.7 dari App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) atau perbarui dari versi Anda yang sudah ada. Pengguna Mac dapat mengambil [versi desktop di sini](https://apps.apple.com/app/evervideo/id6743504109).

## 10+ koneksi cloud, NAS, dan media server baru

Evervideo 1.7 memperluas apa yang dianggap sebagai 'perpustakaan video' Anda. Jika film, acara, atau rekaman Anda berada di cloud yang Anda percayai, NAS di rumah, atau media server yang dihos sendiri, Evervideo kini dapat melakukan streaming langsung dari sana — tanpa unduhan, tanpa konversi, tanpa enkode ulang.

### Penyimpanan cloud yang fokus pada privasi: Internxt dan Proton Drive

Jika Anda peduli dengan enkripsi end-to-end dan penyimpanan zero-knowledge, dua cloud yang berfokus pada privasi yang paling dihormati kini hadir secara native di Evervideo:

- **Internxt** — cloud Spanyol open-source, terenkripsi post-quantum, dan sesuai GDPR. Tier gratis tersedia.
- **Proton Drive** — penyimpanan terenkripsi end-to-end dari pembuat Proton Mail dan Proton VPN, berbasis di Swiss. Tier gratis tersedia dengan paket berbayar untuk perpustakaan yang lebih besar.

Hubungkan sekali dan video Anda akan distreaming melalui terowongan terenkripsi — Evervideo tidak pernah melihat data Anda dalam bentuk tidak terenkripsi, dan server penyedia pun tidak.

### Penyimpanan yang dihos sendiri: QNAP, Nextcloud, Amazon S3

Untuk pengguna yang menjalankan infrastruktur sendiri:

- **QNAP** — koneksi API native ke perangkat QNAP NAS untuk pemutaran video yang cepat dan andal melalui Wi-Fi lokal atau akses jarak jauh. Streaming berkas 4K MKV secara langsung tanpa enkode ulang.
- **Nextcloud** — terhubung ke instance Nextcloud mana pun, baik yang dihos sendiri maupun dikelola. Bagus jika Anda sudah bermigrasi dari Google Drive atau Dropbox karena alasan privasi.
- **Amazon S3** — arahkan Evervideo ke bucket S3 mana pun (atau penyimpanan kompatibel S3 seperti Backblaze B2, Wasabi, MinIO, Cloudflare R2) dan streaming koleksi Anda secara langsung.

### <a id="media-servers"></a>Media server: Plex, Subsonic, Navidrome, Jellyfin, Emby

Ini adalah yang besar untuk penggemar video yang dihos sendiri. Evervideo 1.7 mengubah iPhone, iPad, atau Mac Anda menjadi klien kelas satu untuk media server open-source dan freemium paling populer:

- **Plex** — Plex Media Server **gratis** untuk diunduh dan dijalankan, dengan langganan opsional **Plex Pass** untuk fitur seperti sinkronisasi mobile, transcoding perangkat keras, dan TV langsung. Evervideo berfungsi dengan perpustakaan gratis maupun Plex Pass — streaming seluruh koleksi film dan TV Anda.
- **Subsonic** — server streaming yang dihos sendiri yang asli. Server Subsonic resmi **berbayar** ($1/bulan setelah uji coba 30 hari), dan Evervideo juga berbicara API Subsonic ke server video yang kompatibel.
- **Navidrome** — server modern, ringan, **sepenuhnya gratis dan open-source**. Mengimplementasikan API Subsonic. Berjalan di Raspberry Pi, NAS, atau kotak Linux mana pun.
- **Jellyfin** — media server **sepenuhnya gratis dan open-source** (fork komunitas dari Emby). Menangani film, TV, musik, buku, dan video rumah. Tanpa akun, tanpa telemetri, tanpa langganan. Pilihan utama untuk pengguna yang menginginkan streaming yang dihos sendiri tanpa ikatan komersial.
- **Emby** — media server **freemium**. Server inti gratis; **Emby Premiere** adalah pembelian satu kali atau tahunan yang membuka aplikasi mobile, sinkronisasi offline, Cinema Mode, dan lainnya. Evervideo terhubung ke perpustakaan gratis maupun Premiere.

Apa pun server yang Anda jalankan, Evervideo streaming seluruh perpustakaan Anda — film, acara, video rumah, dan track subtitle tertanam — dengan equalizer video, dukungan 360°, Picture-in-Picture, AirPlay, dan Chromecast.

### Protokol jaringan baru: FTP, SFTP, NFS

Untuk pengguna dengan server kustom, home lab, atau kotak NAS generik yang tidak menyediakan aplikasi mobile yang dipoles, Evervideo 1.7 menambahkan tiga protokol klasik:

- **SFTP (SSH File Transfer Protocol)** — jawaban yang tepat untuk **streaming video jarak jauh yang aman dari server Anda sendiri**. SFTP berjalan di atas SSH, sehingga seluruh transfer (autentikasi dan data video) terenkripsi. Jika Anda memiliki VPS, server dedikasi, atau kotak Linux di rumah dengan akses SSH, Anda dapat menjatuhkan folder video di atasnya dan streaming melalui internet publik tanpa mengekspos apa pun yang lain. Mendukung autentikasi berbasis kata sandi dan kunci.
- **FTP** — standar lama untuk transfer berkas. Berguna jika **NAS rumah** Anda (Synology, ASUS, D-Link, TerraMaster yang lebih lama, atau kotak generik) mengekspos server FTP tetapi tidak memiliki integrasi API native. Paling baik digunakan di dalam jaringan lokal Anda.
- **NFS (Network File System)** — protokol berbagi de facto di Linux dan sebagian besar perangkat NAS. Berbagi NFS umum di home lab dan jaringan bisnis kecil; Evervideo kini memasangnya dan streaming video 4K dan HD dengan overhead rendah.

> **Tip:** SFTP adalah protokol yang Anda inginkan untuk streaming melalui internet terbuka. FTP dan NFS paling baik di dalam jaringan lokal Anda — jauhkan dari internet publik kecuali Anda membungkusnya dalam VPN.

## Gestur pemutaran baru

Menonton video dalam mode layar penuh harus terasa mudah. Evervideo 1.7 memperkenalkan set gestur ketuk yang bersih yang memungkinkan Anda mengontrol pemutaran tanpa mengekspos kontrol di layar — sempurna untuk film, kuliah, atau apa pun yang ingin Anda tonton tanpa gangguan.

### Ketuk ganda — lompat maju atau mundur

Ketuk ganda **sisi kanan** layar untuk **melompat maju** sebanyak detik yang dapat dikonfigurasi. Ketuk ganda **sisi kiri** untuk **melompat mundur**. Anda dapat mengubah interval (default: 10 detik) di **Pengaturan → Pemutaran → Interval Lompat Gestur** — pilih apa pun dari 5 detik (untuk pencarian halus) hingga 60 detik (untuk melewati intro).

Ini adalah gestur yang akan langsung dikenali pengguna YouTube dan Netflix, dan kini native di Evervideo untuk video apa pun, dari sumber apa pun.

### Ketuk dan tahan — kecepatan 2x sementara

Tekan dan tahan di mana pun di layar untuk **mempercepat pemutaran sementara ke 2x**. Lepaskan untuk kembali ke kecepatan normal. Sempurna untuk:

- Melewati adegan lambat tanpa berkomitmen pada perubahan kecepatan permanen.
- Memindai cepat kuliah, tutorial, atau podcast untuk menemukan bagian yang relevan.
- Mencicipi film sebelum Anda berkomitmen untuk menonton versi lengkap.

Gestur tahan tidak mengubah kecepatan pemutaran yang disimpan — lepaskan dan Anda kembali ke posisi semula.

### Ketuk sekali — tampilkan / sembunyikan kontrol

Sekali ketukan di layar mengalihkan kontrol pemutaran (putar, jeda, bilah pencarian, subtitle, equalizer). Ketuk sekali untuk memunculkannya, ketuk lagi untuk menyembunyikannya. Dikombinasikan dengan ketuk ganda dan tahan, ini berarti Anda dapat menghabiskan hampir seluruh film dalam mode layar penuh yang bersih dan tetap dapat mencari, menjeda, dan memindai kecepatan kapan pun Anda perlu.

## Wi-Fi Drive: UI baru dan unggahan lebih cepat

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) adalah fitur bawaan Evervideo untuk **mentransfer video secara nirkabel dari komputer Anda ke iPhone atau iPad — tanpa iTunes, tanpa kabel, tanpa akun cloud yang diperlukan**. Kedua perangkat harus berada di jaringan Wi-Fi yang sama. Anda memulai server di aplikasi iOS dan kemudian:

- Buka URL di browser desktop mana pun (Safari, Chrome, Firefox, Edge), seret berkas video Anda ke halaman, dan akan diunggah langsung ke perangkat, atau
- Pasang perangkat sebagai berbagi jaringan melalui **Mac Finder** ('Hubungkan ke Server...') atau **Windows File Explorer** (Petakan Drive Jaringan) menggunakan WebDAV.

Ini adalah cara tercepat untuk memindahkan koleksi video lokal yang besar ke ponsel atau tablet Anda tanpa layanan pihak ketiga apa pun. Lihat [panduan langkah demi langkah di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

Di Evervideo 1.7, Wi-Fi Drive mendapatkan:

- **Antarmuka pengguna yang didesain ulang** — lebih bersih, lebih mudah dibaca sekilas, dan diperbarui untuk Liquid Glass.
- **Mode pemilihan baru untuk tindakan massal** — pilih beberapa berkas atau folder dan tindak lanjuti secara massal (hapus, pindahkan, salin).
- **Antrean unggah berkas yang ditingkatkan** — umpan balik progres yang lebih baik dan ketahanan terhadap gangguan jaringan sehingga koneksi Wi-Fi yang labil tidak lagi merusak transfer 30 GB.
- **Kinerja transfer keseluruhan yang lebih baik** — unggahan terukur lebih cepat untuk perpustakaan besar, terutama untuk berkas 4K MKV dan koleksi film.

## Peningkatan lainnya

### Pembaruan desain Liquid Glass

Antarmuka Evervideo 1.7 diperbarui untuk material **Liquid Glass** baru dari Apple di seluruh aplikasi — permukaan transparan, animasi yang lebih halus, dan kontrol yang disempurnakan yang cocok secara alami ke dalam iOS 26, iPadOS 26, dan macOS 26. Now Playing, browser berkas, dan layar pengaturan semuanya telah disetel ulang untuk menyesuaikan dengan estetika sistem baru.

### Pustaka koneksi yang diperbarui

Kami menyegarkan pustaka yang digunakan Evervideo untuk berbicara ke **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA**, dan layanan lainnya. Hasilnya: lebih sedikit kegagalan koneksi edge-case, dukungan yang lebih baik untuk versi server yang lebih baru, dan keandalan yang lebih baik saat streaming video pada koneksi yang lebih lambat atau berjarak jauh secara geografis.

### Perbaikan bug pemutaran

- Diperbaiki masalah pemutaran pada beberapa server yang dihos sendiri di mana stream akan terhenti setelah pencarian pada berkas MKV besar.
- Perilaku resume yang lebih baik ketika jaringan terputus sebentar di tengah pemutaran.
- Sinkronisasi subtitle yang lebih halus pada konten format panjang.

### Perbaikan lokalisasi

Perbaikan terjemahan di beberapa bahasa berdasarkan umpan balik pengguna langsung. Penempatan teks yang lebih baik pada tombol yang lebih kecil dan bahasa Eropa yang lebih panjang (Jerman, Belanda, Prancis).

### Penyempurnaan kecil yang terinspirasi oleh umpan balik Anda

Banyak peningkatan kecil berdasarkan ulasan App Store dan email ke support@everappz.com. Kami membaca setiap pesan.

## Mengapa pembaruan ini penting

Evervideo 1.7 dibangun di sekitar tiga gagasan:

1. **Video Anda, di mana pun Anda menyimpannya.** Apakah perpustakaan Anda berada di iCloud Drive, cloud yang berfokus pada privasi seperti Proton Drive atau Internxt, media server seperti Plex atau Jellyfin, NAS di rumah, atau Raspberry Pi yang menjalankan Navidrome — Evervideo kini terhubung dengannya secara native, dengan pengalaman pemutaran yang sama di mana saja.
2. **Video layar penuh yang terasa mudah.** Gestur ketuk baru (ketuk ganda, ketuk dan tahan, ketuk sekali) menghadirkan jenis kontrol mulus yang telah dilatih oleh aplikasi streaming seperti YouTube dan Netflix untuk diharapkan pengguna, diterapkan pada koleksi video *Anda*.
3. **Transfer lebih cepat dari komputer Anda.** Wi-Fi Drive yang disegarkan dengan pemilihan massal dan antrean unggah yang lebih pintar membuat pemindahan koleksi film 4K besar ke iPhone atau iPad Anda benar-benar cepat — tanpa kabel, tanpa iTunes, tanpa kompresi.

## Dapatkan Evervideo 1.7

[**Unduh Evervideo dari App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) atau perbarui dari dalam App Store. [Versi Mac](https://apps.apple.com/app/evervideo/id6743504109) tersedia secara terpisah sebagai aplikasi Mac universal. Evervideo adalah unduhan gratis dengan peningkatan dalam aplikasi opsional untuk fitur lanjutan. Koneksi cloud baru, dukungan media server, gestur pemutaran, peningkatan Wi-Fi Drive, dan UI Liquid Glass adalah bagian dari pembaruan dasar.

Jika Anda menikmati aplikasinya, silakan tinggalkan penilaian di App Store — itu sangat membantu. Memiliki umpan balik atau mengalami masalah? Kirim email ke **support@everappz.com**. Kami membaca setiap pesan.

## Pertanyaan yang sering diajukan

{{% details title="Apa yang baru di Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 memperkenalkan dukungan untuk 10+ koneksi baru (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), gestur pemutaran baru (ketuk ganda untuk mencari, ketuk dan tahan untuk kecepatan 2x, ketuk sekali untuk mengaktifkan/menonaktifkan kontrol), Wi-Fi Drive yang didesain ulang dengan mode pemilihan dan antrean unggah yang lebih pintar, pembaruan desain Liquid Glass, pustaka koneksi yang diperbarui, dan banyak perbaikan bug.
{{% /details %}}

{{% details title="Apakah Evervideo bekerja dengan Plex?" closed="true" %}}
Ya. Mulai dari Evervideo 1.7, Anda dapat terhubung ke Plex Media Server dan streaming seluruh perpustakaan video Anda — film, acara TV, dan video rumah. Plex Media Server gratis untuk dijalankan; Plex Pass opsional. Evervideo mendukung pengaturan gratis maupun Plex Pass, termasuk pemutaran langsung MKV, MP4, AVI, MOV, dan format lainnya tanpa enkode ulang.
{{% /details %}}

{{% details title="Apakah Jellyfin atau Navidrome didukung di Evervideo?" closed="true" %}}
Ya. Baik Jellyfin maupun Navidrome didukung sepenuhnya di Evervideo 1.7. Jellyfin adalah media server gratis dan open-source yang menangani video dan audio. Navidrome adalah server gratis dan open-source yang mengimplementasikan API Subsonic. Evervideo terhubung ke keduanya secara native.
{{% /details %}}

{{% details title="Apakah Plex, Jellyfin, Emby, Navidrome, dan Subsonic gratis?" closed="true" %}}
- **Plex** — server gratis; Plex Pass adalah peningkatan berbayar opsional.
- **Jellyfin** — sepenuhnya gratis dan open-source.
- **Emby** — server gratis; Emby Premiere berbayar dan membuka sinkronisasi mobile dan offline.
- **Navidrome** — sepenuhnya gratis dan open-source.
- **Subsonic** — server resmi seharga $1/bulan setelah uji coba 30 hari, tetapi API-nya terbuka dan banyak server gratis (termasuk Navidrome) yang mengimplementasikannya.
{{% /details %}}

{{% details title="Bisakah saya streaming dari NAS rumah saya melalui SFTP, FTP, atau NFS?" closed="true" %}}
Ya. Evervideo 1.7 menambahkan SFTP, FTP, dan NFS sebagai jenis koneksi native. SFTP adalah pilihan yang direkomendasikan untuk streaming dari server Anda sendiri melalui internet publik karena semua lalu lintas dienkripsi melalui SSH. FTP dan NFS paling baik digunakan di dalam jaringan lokal Anda atau di belakang VPN.
{{% /details %}}

{{% details title="Bagaimana cara menghubungkan Evervideo ke server kustom menggunakan SFTP?" closed="true" %}}
Buka Evervideo, masuk ke tab Koneksi, pilih SFTP, dan masukkan hostname atau IP server Anda, port (biasanya 22), nama pengguna, dan kata sandi atau kunci pribadi SSH. Evervideo akan menelusuri folder jarak jauh Anda dan streaming berkas video secara langsung dengan enkripsi end-to-end.
{{% /details %}}

{{% details title="Apakah Evervideo mendukung Internxt dan Proton Drive?" closed="true" %}}
Ya. Kedua cloud yang berfokus pada privasi didukung mulai dari Evervideo 1.7. Mereka bergabung dengan MEGA dan layanan privasi-pertama lainnya yang sudah tersedia di aplikasi.
{{% /details %}}

{{% details title="Bagaimana cara kerja gestur pemutaran baru?" closed="true" %}}
Saat pemutaran video layar penuh, **ketuk ganda sisi kanan** untuk melompat maju dan **ketuk ganda sisi kiri** untuk melompat mundur dengan interval yang dapat dikonfigurasi (default 10 detik — ubah di Pengaturan). **Ketuk dan tahan** di mana pun di layar untuk mempercepat sementara ke 2x; lepaskan untuk kembali ke normal. **Ketuk sekali** di mana pun untuk mengaktifkan/menonaktifkan kontrol pemutaran (tampilkan atau sembunyikan).
{{% /details %}}

{{% details title="Bisakah saya mengubah interval lompat ketuk ganda?" closed="true" %}}
Ya. Buka **Pengaturan → Pemutaran → Interval Lompat Gestur** dan pilih nilai antara 5 dan 60 detik. Sebagian besar pengguna mempertahankannya di 10 atau 15 detik.
{{% /details %}}

{{% details title="Apa itu Wi-Fi Drive di Evervideo?" closed="true" %}}
Wi-Fi Drive adalah fitur transfer berkas nirkabel bawaan Evervideo. Ini memungkinkan Anda mengunggah video dari komputer Anda ke iPhone atau iPad Anda melalui jaringan Wi-Fi lokal — tanpa iTunes, tanpa kabel, tanpa akun cloud. Anda dapat menggunakan browser desktop apa pun atau klien WebDAV seperti Mac Finder atau Windows File Explorer. Lihat [panduan Wi-Fi Drive lengkap](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Apakah Evervideo memutar MKV, AVI, dan format lain dari Plex atau Jellyfin?" closed="true" %}}
Ya. Evervideo memutar hampir semua format video — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — dan streaming langsung dari Plex, Jellyfin, Emby, dan media server lainnya tanpa memerlukan transcoding untuk sebagian besar codec. Ini berarti beban CPU yang lebih rendah di server Anda dan waktu mulai yang lebih cepat.
{{% /details %}}

{{% details title="Apakah Evervideo 1.7 gratis untuk diperbarui?" closed="true" %}}
Ya. Evervideo adalah unduhan gratis dari App Store, dan 1.7 adalah pembaruan gratis untuk semua pengguna yang sudah ada. Integrasi cloud baru, dukungan media server, gestur pemutaran, peningkatan Wi-Fi Drive, dan UI Liquid Glass adalah bagian dari pembaruan dasar.
{{% /details %}}

{{% details title="Pada perangkat apa Evervideo 1.7 tersedia?" closed="true" %}}
Evervideo 1.7 berjalan di iPhone, iPad, dan Mac. AirPlay dan Chromecast memungkinkan Anda meneruskan pemutaran ke layar yang lebih besar. Sinkronisasi iCloud Drive menjaga perpustakaan dan pengaturan Anda tetap konsisten di seluruh perangkat.
{{% /details %}}
