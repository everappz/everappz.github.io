---
title: "Cara Mengambil Metadata, Ikon, dan Tangkapan Layar App Store Secara Gratis"
date: 2026-06-13
description: "Panduan langkah demi langkah untuk mengambil metadata, ikon, tangkapan layar, dan detail App Store yang dilokalkan untuk aplikasi iOS apa pun menggunakan AppLookup.pro, alat browser gratis yang ditenagai oleh iTunes Search API resmi."
keywords: [
  "metadata App Store", "ambil data App Store", "unduh ikon App Store",
  "unduh tangkapan layar App Store", "alat pencarian App Store", "iTunes Search API",
  "ekstrak metadata aplikasi", "metadata aplikasi iOS", "alat App Store API gratis",
  "unduh ikon aplikasi resolusi tinggi", "riset kompetitor App Store",
  "data App Store lokal", "pencarian negara App Store", "alat riset ASO gratis"
]
tags: [
  "Metadata App Store", "App Lookup", "iTunes Search API",
  "Unduh Ikon Aplikasi", "Tangkapan Layar Aplikasi", "Riset ASO"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Dapatkan Data App Store dalam Hitungan Detik

**Versi singkat:** [AppLookup.pro](https://applookup.pro) adalah alat gratis yang menarik data publik untuk aplikasi iOS, iPadOS, macOS, atau tvOS apa pun. Anda mendapatkan judul, deskripsi, apa yang baru, versi, harga, peringkat, ikon aplikasi, tangkapan layar, perangkat yang didukung, dan respons mentah iTunes API. Setiap kolom memiliki tombol salin sekali ketuk. Buka situs, tempel tautan App Store atau ketik nama aplikasi, dan data sudah ada di tangan Anda.

Gunakan untuk:

- **Riset ASO.** Lihat bagaimana aplikasi populer menulis judul, subjudul, deskripsi, dan kata kunci mereka.
- **Pelacakan kompetitor.** Periksa pembaruan versi, peringkat, dan harga lintas pasar.
- **Unduh aset.** Simpan ikon aplikasi resmi dan tangkapan layar ukuran penuh dalam satu ZIP.
- **Pemeriksaan lokalisasi.** Bandingkan deskripsi, apa yang baru, dan tangkapan layar di lebih dari 40 negara App Store.
- **Pengujian API.** Salin JSON mentah iTunes Search API langsung ke kode atau Postman Anda.

## Apa Itu AppLookup.pro?

[AppLookup.pro](https://applookup.pro) adalah alat pencarian App Store gratis berbasis browser. Alat ini berjalan sepenuhnya di perangkat Anda. Setiap hasil berasal langsung dari [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) resmi Apple. Tanpa scraping. Tanpa pendaftaran. Tanpa pelacakan.

### Apa yang Anda Dapatkan

- **Pencarian berdasarkan nama aplikasi atau URL App Store.** Autocomplete menampilkan hasil langsung saat Anda mengetik.
- **Lebih dari 40 toko negara.** Beralih antara AS, Inggris, Jepang, Jerman, Prancis, Brasil, dan lainnya.
- **Metadata lengkap.** Judul, subjudul, pengembang, Bundle ID, versi, harga, ukuran file, peringkat, tanggal rilis, peringkat konten, bahasa, dan perangkat yang didukung.
- **Aset resolusi tinggi.** Ikon aplikasi dan tangkapan layar untuk iPhone, iPad, macOS, dan Apple TV.
- **Unduhan ZIP massal.** Ambil setiap ikon atau setiap tangkapan layar dalam satu arsip.
- **JSON mentah iTunes API.** Respons persis dari Apple, siap untuk disalin.
- **Tombol salin di setiap kolom.** Satu ketukan akan memasukkan nilai ke clipboard Anda.

## Cara Menggunakan AppLookup.pro Langkah demi Langkah

### Langkah 1. Masukkan Nama Aplikasi atau Tempel URL App Store

Buka [applookup.pro](https://applookup.pro) dan mulai mengetik nama aplikasi. Autocomplete menampilkan hasil App Store langsung saat Anda mengetik.

Anda juga dapat menempelkan tautan App Store langsung seperti `https://apps.apple.com/us/app/instagram/id389801252` atau hanya ID aplikasi. Alat ini akan mengekstrak ID untuk Anda. Ia juga menangani URL pengalihan Google.

![Masukkan nama aplikasi atau URL App Store ke AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Langkah 2. Ambil Info Aplikasi dan Unduh Ikon

Klik **Lookup** atau tekan Enter. Alat ini memanggil iTunes Search API resmi dan menampilkan ikon aplikasi, nama pengembang, peringkat, versi, dan harga dalam waktu kurang dari satu detik.

Gulir ke bagian **App Icon**. Setiap ukuran ikon yang dikembalikan Apple muncul sebagai kartu. Setiap kartu memiliki:

- **Direct Link.** Membuka gambar ukuran penuh di tab baru.
- **Download.** Menyimpan file ke komputer Anda.

Gunakan **Download All Icons (ZIP)** untuk mengambil setiap ukuran ikon dalam satu arsip. Hal yang sama berlaku untuk tangkapan layar: setiap bagian platform memiliki tombol **Download All (ZIP)** sendiri.

![Unduh ikon aplikasi dan tangkapan layar dari AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Langkah 3. Baca Detail Aplikasi dan Salin Kolom Apa Pun

Gulir ke **App Details**. Anda akan melihat Bundle ID, versi, harga, ukuran file, OS minimum, tanggal rilis, tanggal pembaruan terakhir, peringkat konten, genre, ID genre, bahasa, penjual, ID artis, dan ID track.

Ketuk tombol **Copy** pada kartu mana pun. Nilai akan masuk ke clipboard Anda dan tombol akan menampilkan tanda centang hijau 'Copied'.

Hal yang sama berlaku untuk **Description**, **What's New**, dan **Supported Devices**. Bagian-bagian ini dapat digulir sehingga Anda dapat membaca teks lengkap tanpa kehilangan posisi, dan tombol Copy memasukkan seluruh kolom ke clipboard Anda.

![Lihat detail App Store lengkap dan salin kolom apa pun dengan satu ketukan](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Langkah 4. Lihat Respons Mentah App Store API

Butuh JSON persis yang dikembalikan Apple? Gulir ke **Raw API Response**. Payload iTunes Search API lengkap ditampilkan dalam penampil yang dapat digulir dengan tombol **Copy** di bagian atas. Satu ketukan akan menyalin seluruh objek JSON.

**iTunes Lookup URL** ditampilkan tepat di atasnya. Tempel ke Postman, curl, atau browser Anda untuk memutar ulang permintaan yang sama.

![Lihat dan salin respons JSON mentah iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Langkah 5. Ubah Negara untuk Melihat Versi Lokal

Metadata App Store berubah berdasarkan negara. Aplikasi yang sama sering memiliki judul, subjudul, deskripsi, tangkapan layar, dan harga yang berbeda di setiap pasar.

Pilih negara dari dropdown di bagian atas. URL di kotak input akan diperbarui secara otomatis. Klik **Lookup** lagi untuk mengambil ulang aplikasi di pasar tersebut.

Ini adalah cara tercepat untuk memeriksa bagaimana kompetitor menyajikan aplikasi mereka di Jepang, Jerman, Brasil, atau salah satu dari lebih dari 40 negara yang didukung.

![Beralih toko negara untuk melihat metadata App Store yang dilokalkan](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Langkah 6. Salin Metadata yang Dilokalkan

Setelah hasil negara dimuat, setiap kolom berfungsi dengan cara yang sama. Ketuk **Copy** pada deskripsi, apa yang baru, nama aplikasi, pengembang, Bundle ID, atau kartu detail mana pun untuk menangkap teks yang dilokalkan.

Ini memudahkan untuk membangun spreadsheet perbandingan berdampingan atau memasukkan salinan yang dilokalkan ke dalam tinjauan terjemahan.

![Salin deskripsi dan metadata App Store yang dilokalkan dengan satu ketukan](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Siapa yang Menggunakan AppLookup.pro

- **Pengembang indie** yang melakukan riset ASO sebelum peluncuran.
- **Tim ASO dan pemasaran** yang melacak pembaruan dan harga kompetitor.
- **Desainer** yang mengambil ikon aplikasi resmi resolusi tinggi dan tangkapan layar untuk press kit dan studi kasus.
- **Tim lokalisasi** yang mengaudit pasar mana yang dicakup dan di mana salinan bahasa Inggris default masih dikirim.
- **Insinyur backend dan QA** yang menguji integrasi iTunes Search API tanpa menulis scraper.
- **Penulis dan blogger** yang membutuhkan ikon aplikasi resmi dan beberapa tangkapan layar untuk postingan.

## Privasi dan Penafian

AppLookup.pro berjalan di browser Anda. Tidak ada login. Tidak ada pelacakan. Tidak ada pencatatan server untuk aplikasi yang Anda cari. Permintaan langsung dari browser Anda ke [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) Apple.

Alat ini hanya untuk **tujuan pendidikan dan penelitian**. Semua data diambil dari API publik resmi Apple dan tetap menjadi milik Apple Inc. dan penerbit aplikasi yang terdaftar. Penggunaan alat ini tunduk pada [Syarat dan Ketentuan Layanan Media Apple](https://www.apple.com/legal/internet-services/terms/site.html). Mohon hormati batas tarif Apple dan jangan mendistribusikan ulang aset yang dilindungi hak cipta.

## Coba Sekarang

Anda tidak memerlukan kunci API, akun pengembang, atau paket berbayar untuk memeriksa data App Store. Buka [applookup.pro](https://applookup.pro), tempel URL App Store apa pun, dan Anda akan mendapatkan metadata, ikon, dan JSON mentah dalam hitungan detik.

## Sumber Terbuka

AppLookup.pro adalah sumber terbuka. Laporan bug, penambahan negara, dan pull request dipersilakan.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro di GitHub" icon="github" tag="sumber terbuka" >}}
{{< /cards >}}

---

## Pertanyaan yang Sering Diajukan

{{% details title="Apakah AppLookup.pro benar-benar gratis?" closed="true" %}}
Ya. AppLookup.pro 100 persen gratis dan sumber terbuka. Ia berjalan di browser Anda. Tidak ada pendaftaran, tidak ada tingkat berbayar, dan tidak ada batas penggunaan selain batas iTunes Search API milik Apple sendiri.
{{% /details %}}

{{% details title="Dari mana data berasal?" closed="true" %}}
Setiap hasil diambil secara real-time dari [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) resmi Apple. Alat ini tidak melakukan scraping halaman App Store dan tidak menyimpan respons di server mana pun.
{{% /details %}}

{{% details title="Bisakah saya mengunduh ikon aplikasi dalam resolusi tinggi?" closed="true" %}}
Ya. Bagian **App Icon** menampilkan setiap URL ikon yang dikembalikan Apple. Setiap kartu memiliki tombol Direct Link dan Download, dan tombol Download All Icons ZIP mengemas semuanya dalam satu arsip.
{{% /details %}}

{{% details title="Bisakah saya mengunduh semua tangkapan layar App Store sekaligus?" closed="true" %}}
Ya. Setiap bagian tangkapan layar (iPhone, iPad, macOS, dan Apple TV) memiliki tombol **Download All (ZIP)** yang menggabungkan setiap tangkapan layar pada resolusi penuh.
{{% /details %}}

{{% details title="Bagaimana cara melihat tampilan aplikasi di negara lain?" closed="true" %}}
Pilih negara dari dropdown di bagian atas halaman. Lebih dari 40 toko didukung. Klik **Lookup** lagi dan alat akan mengambil ulang aplikasi untuk negara tersebut, menampilkan judul, deskripsi, tangkapan layar, apa yang baru, dan harga yang dilokalkan.
{{% /details %}}

{{% details title="Bisakah saya menyalin kolom tunggal seperti Bundle ID atau tanggal rilis?" closed="true" %}}
Ya. Setiap kolom teks dalam hasil memiliki tombol Copy sendiri: nama aplikasi, pengembang, deskripsi, apa yang baru, Bundle ID, versi, harga, ukuran file, OS minimum, tanggal rilis, peringkat konten, bahasa, perangkat yang didukung, dan JSON mentah.
{{% /details %}}

{{% details title="Apakah AppLookup.pro berfungsi untuk semua aplikasi iOS?" closed="true" %}}
Berfungsi untuk aplikasi apa pun yang terdaftar secara publik di setidaknya satu negara App Store dan dikembalikan oleh iTunes Search API. Aplikasi yang tidak terdaftar, dihapus, atau didistribusikan untuk perusahaan tidak akan muncul.
{{% /details %}}

{{% details title="Apakah mendukung aplikasi macOS dan Apple TV?" closed="true" %}}
Ya. Jika aplikasi memiliki tangkapan layar macOS atau Apple TV dalam respons iTunes Search API, AppLookup.pro menampilkannya di panel yang dapat digulir sendiri dengan tombol unduh.
{{% /details %}}

{{% details title="Bisakah saya menggunakan JSON mentah dalam kode saya sendiri?" closed="true" %}}
Ya. Bagian Raw API Response menampilkan JSON persis yang dikembalikan Apple. Salin ke Postman, unit test, atau pipeline backend. Mohon hormati ketentuan API Apple dan batas tarif yang wajar.
{{% /details %}}

{{% details title="Apakah aman menempelkan URL App Store ke alat?" closed="true" %}}
Ya. URL diuraikan di browser Anda. Satu-satunya panggilan jaringan keluar adalah pencarian ke iTunes Search API Apple.
{{% /details %}}

{{% details title="Apa perbedaan antara AppLookup.pro dan AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) adalah untuk membaca metadata App Store dari aplikasi yang dipublikasikan: riset kompetitor, unduhan aset, pemeriksaan lokalisasi. [AppKeywords.pro](https://appkeywords.pro) adalah untuk menulis metadata App Store untuk aplikasi Anda sendiri: optimasi judul, subjudul, dan kata kunci dengan dukungan Fastlane. Kedua alat ini bekerja sama dengan baik.
{{% /details %}}
