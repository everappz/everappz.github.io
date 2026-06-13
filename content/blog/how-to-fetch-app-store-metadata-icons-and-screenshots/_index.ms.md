---
title: "Cara Mendapatkan Metadata, Ikon dan Tangkapan Skrin App Store Secara Percuma"
date: 2026-06-13
description: "Panduan langkah demi langkah untuk mendapatkan metadata, ikon, tangkapan skrin dan butiran App Store yang disetempatkan bagi mana-mana aplikasi iOS menggunakan AppLookup.pro, alat pelayar percuma yang dikuasakan oleh iTunes Search API rasmi."
keywords: [
  "metadata App Store", "dapatkan data App Store", "muat turun ikon App Store",
  "muat turun tangkapan skrin App Store", "alat carian App Store", "iTunes Search API",
  "pengekstrak metadata aplikasi", "metadata aplikasi iOS", "alat App Store API percuma",
  "muat turun ikon aplikasi resolusi tinggi", "penyelidikan pesaing App Store",
  "data App Store setempat", "carian negara App Store", "alat penyelidikan ASO percuma"
]
tags: [
  "Metadata App Store", "App Lookup", "iTunes Search API",
  "Muat Turun Ikon Aplikasi", "Tangkapan Skrin Aplikasi", "Penyelidikan ASO"
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

## Dapatkan Data App Store dalam Beberapa Saat

**Versi pendek:** [AppLookup.pro](https://applookup.pro) ialah alat percuma yang menarik data awam untuk mana-mana aplikasi iOS, iPadOS, macOS atau tvOS. Anda mendapat tajuk, penerangan, apa yang baharu, versi, harga, penilaian, ikon aplikasi, tangkapan skrin, peranti yang disokong dan respons mentah iTunes API. Setiap medan mempunyai butang salin satu ketuk. Buka tapak, tampal pautan App Store atau taipkan nama aplikasi, dan anda sudah mempunyai data tersebut.

Gunakannya untuk:

- **Penyelidikan ASO.** Lihat bagaimana aplikasi teratas menulis tajuk, sari kata, penerangan dan kata kunci mereka.
- **Pemantauan pesaing.** Semak kemas kini versi, penilaian dan harga merentas pasaran.
- **Muat turun aset.** Simpan ikon aplikasi rasmi dan tangkapan skrin saiz penuh dalam satu ZIP.
- **Pemeriksaan penyetempatan.** Bandingkan penerangan, apa yang baharu dan tangkapan skrin merentas lebih 40 negara App Store.
- **Pengujian API.** Salin JSON mentah iTunes Search API terus ke kod atau Postman anda.

## Apakah AppLookup.pro?

[AppLookup.pro](https://applookup.pro) ialah alat carian App Store percuma berasaskan pelayar. Ia berjalan sepenuhnya pada peranti anda. Setiap hasil datang terus daripada [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) rasmi Apple. Tiada scraping. Tiada pendaftaran. Tiada penjejakan.

### Apa yang Anda Dapat

- **Carian mengikut nama aplikasi atau URL App Store.** Pelengkap auto menunjukkan hasil langsung semasa anda menaip.
- **Lebih 40 kedai negara.** Tukar antara AS, UK, Jepun, Jerman, Perancis, Brazil dan lain-lain.
- **Metadata penuh.** Tajuk, sari kata, pembangun, Bundle ID, versi, harga, saiz fail, penilaian, tarikh keluaran, penarafan kandungan, bahasa dan peranti yang disokong.
- **Aset resolusi tinggi.** Ikon aplikasi dan tangkapan skrin untuk iPhone, iPad, macOS dan Apple TV.
- **Muat turun ZIP pukal.** Dapatkan setiap ikon atau setiap tangkapan skrin dalam satu arkib.
- **JSON mentah iTunes API.** Respons tepat daripada Apple, sedia untuk disalin.
- **Butang salin pada setiap medan.** Satu ketuk meletakkan nilai dalam papan keratan anda.

## Cara Guna AppLookup.pro Langkah demi Langkah

### Langkah 1. Masukkan Nama Aplikasi atau Tampal URL App Store

Buka [applookup.pro](https://applookup.pro) dan mula menaip nama aplikasi. Pelengkap auto menunjukkan hasil App Store langsung semasa anda menaip.

Anda juga boleh menampal pautan App Store terus seperti `https://apps.apple.com/us/app/instagram/id389801252` atau hanya ID aplikasi. Alat ini akan mengekstrak ID untuk anda. Ia juga mengendalikan URL ubah hala Google.

![Masukkan nama aplikasi atau URL App Store ke dalam AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Langkah 2. Dapatkan Maklumat Aplikasi dan Muat Turun Ikon

Klik **Lookup** atau tekan Enter. Alat ini memanggil iTunes Search API rasmi dan menunjukkan ikon aplikasi, nama pembangun, penilaian, versi dan harga dalam masa kurang sesaat.

Tatal ke bahagian **App Icon**. Setiap saiz ikon yang dikembalikan Apple muncul sebagai kad. Setiap kad mempunyai:

- **Direct Link.** Membuka imej saiz penuh dalam tab baharu.
- **Download.** Menyimpan fail ke komputer anda.

Gunakan **Download All Icons (ZIP)** untuk mendapatkan setiap saiz ikon dalam satu arkib. Perkara yang sama untuk tangkapan skrin: setiap bahagian platform mempunyai butang **Download All (ZIP)** tersendiri.

![Muat turun ikon aplikasi dan tangkapan skrin daripada AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Langkah 3. Baca Butiran Aplikasi dan Salin Mana-mana Medan

Tatal ke **App Details**. Anda akan melihat Bundle ID, versi, harga, saiz fail, OS minimum, tarikh keluaran, tarikh kemas kini terakhir, penarafan kandungan, genre, ID genre, bahasa, penjual, ID artis dan ID trek.

Ketuk butang **Copy** pada mana-mana kad. Nilai akan masuk ke papan keratan anda dan butang akan memaparkan tanda 'Copied' hijau.

Perkara yang sama berlaku untuk **Description**, **What's New** dan **Supported Devices**. Bahagian-bahagian ini boleh ditatal supaya anda boleh membaca teks penuh tanpa kehilangan kedudukan, dan butang Copy meletakkan keseluruhan medan pada papan keratan anda.

![Lihat butiran App Store penuh dan salin mana-mana medan dengan satu ketuk](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Langkah 4. Lihat Respons Mentah App Store API

Perlu JSON tepat yang dikembalikan Apple? Tatal ke **Raw API Response**. Muatan iTunes Search API penuh ditunjukkan dalam pemapar yang boleh ditatal dengan butang **Copy** di bahagian atas. Satu ketuk akan menyalin keseluruhan objek JSON.

**iTunes Lookup URL** ditunjukkan tepat di atasnya. Tampal ke Postman, curl atau pelayar anda untuk memainkan semula permintaan yang sama.

![Lihat dan salin respons JSON mentah iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Langkah 5. Tukar Negara untuk Melihat Versi Setempat

Metadata App Store berubah mengikut negara. Aplikasi yang sama selalunya mempunyai tajuk, sari kata, penerangan, tangkapan skrin dan harga yang berbeza di setiap pasaran.

Pilih negara daripada menu lungsur di bahagian atas. URL dalam kotak input akan dikemas kini secara automatik. Klik **Lookup** semula untuk mengambil semula aplikasi di pasaran tersebut.

Ini adalah cara terpantas untuk menyemak bagaimana pesaing mempersembahkan aplikasi mereka di Jepun, Jerman, Brazil atau mana-mana daripada lebih 40 negara yang disokong.

![Tukar kedai negara untuk melihat metadata App Store yang disetempatkan](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Langkah 6. Salin Metadata yang Disetempatkan

Setelah hasil negara dimuatkan, setiap medan berfungsi dengan cara yang sama. Ketuk **Copy** pada penerangan, apa yang baharu, nama aplikasi, pembangun, Bundle ID atau mana-mana kad butiran untuk menangkap teks yang disetempatkan.

Ini memudahkan untuk membina hamparan perbandingan bersebelahan atau memasukkan salinan yang disetempatkan ke dalam semakan terjemahan.

![Salin penerangan dan metadata App Store yang disetempatkan dengan satu ketuk](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Siapa Yang Menggunakan AppLookup.pro

- **Pembangun indie** yang melakukan penyelidikan ASO sebelum pelancaran.
- **Pasukan ASO dan pemasaran** yang menjejaki kemas kini dan harga pesaing.
- **Pereka bentuk** yang mengambil ikon aplikasi rasmi resolusi tinggi dan tangkapan skrin untuk kit akhbar dan kajian kes.
- **Pasukan penyetempatan** yang mengaudit pasaran mana yang diliputi dan di mana salinan bahasa Inggeris lalai masih dihantar.
- **Jurutera backend dan QA** yang menguji integrasi iTunes Search API tanpa menulis scraper.
- **Penulis dan blogger** yang memerlukan ikon aplikasi rasmi dan beberapa tangkapan skrin untuk pos.

## Privasi dan Penafian

AppLookup.pro berjalan dalam pelayar anda. Tiada log masuk. Tiada penjejakan. Tiada pengelogan pelayan untuk aplikasi yang anda cari. Permintaan dihantar terus dari pelayar anda ke [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) Apple.

Alat ini adalah untuk **tujuan pendidikan dan penyelidikan sahaja**. Semua data diambil dari API awam rasmi Apple dan kekal sebagai milik Apple Inc. dan penerbit aplikasi yang disenaraikan. Penggunaan alat ini tertakluk kepada [Terma dan Syarat Perkhidmatan Media Apple](https://www.apple.com/legal/internet-services/terms/site.html). Sila hormati had kadar Apple dan jangan agihkan semula aset berhak cipta.

## Cuba Sekarang

Anda tidak memerlukan kunci API, akaun pembangun atau pelan berbayar untuk memeriksa data App Store. Buka [applookup.pro](https://applookup.pro), tampal mana-mana URL App Store, dan anda akan mempunyai metadata, ikon dan JSON mentah dalam beberapa saat.

## Sumber Terbuka

AppLookup.pro adalah sumber terbuka. Laporan pepijat, penambahan negara dan pull request dialu-alukan.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro di GitHub" icon="github" tag="sumber terbuka" >}}
{{< /cards >}}

---

## Soalan Lazim

{{% details title="Adakah AppLookup.pro benar-benar percuma?" closed="true" %}}
Ya. AppLookup.pro adalah 100 peratus percuma dan sumber terbuka. Ia berjalan dalam pelayar anda. Tiada pendaftaran, tiada peringkat berbayar dan tiada had penggunaan selain had iTunes Search API Apple sendiri.
{{% /details %}}

{{% details title="Dari manakah data datang?" closed="true" %}}
Setiap hasil diambil dalam masa nyata daripada [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) rasmi Apple. Alat ini tidak melakukan scraping halaman App Store dan tidak menyimpan cache respons pada mana-mana pelayan.
{{% /details %}}

{{% details title="Bolehkah saya memuat turun ikon aplikasi dalam resolusi tinggi?" closed="true" %}}
Ya. Bahagian **App Icon** menunjukkan setiap URL ikon yang dikembalikan Apple. Setiap kad mempunyai butang Direct Link dan Download, dan butang Download All Icons ZIP mengemas mereka dalam satu arkib.
{{% /details %}}

{{% details title="Bolehkah saya memuat turun semua tangkapan skrin App Store sekaligus?" closed="true" %}}
Ya. Setiap bahagian tangkapan skrin (iPhone, iPad, macOS dan Apple TV) mempunyai butang **Download All (ZIP)** yang menggabungkan setiap tangkapan skrin pada resolusi penuh.
{{% /details %}}

{{% details title="Bagaimanakah saya boleh melihat rupa aplikasi di negara lain?" closed="true" %}}
Pilih negara dalam menu lungsur di bahagian atas halaman. Lebih 40 kedai disokong. Klik **Lookup** semula dan alat akan mengambil semula aplikasi untuk negara tersebut, menunjukkan tajuk, penerangan, tangkapan skrin, apa yang baharu dan harga yang disetempatkan.
{{% /details %}}

{{% details title="Bolehkah saya menyalin medan tunggal seperti Bundle ID atau tarikh keluaran?" closed="true" %}}
Ya. Setiap medan teks dalam hasil mempunyai butang Copy sendiri: nama aplikasi, pembangun, penerangan, apa yang baharu, Bundle ID, versi, harga, saiz fail, OS minimum, tarikh keluaran, penarafan kandungan, bahasa, peranti yang disokong dan JSON mentah.
{{% /details %}}

{{% details title="Adakah AppLookup.pro berfungsi untuk mana-mana aplikasi iOS?" closed="true" %}}
Ia berfungsi untuk mana-mana aplikasi yang disenaraikan secara umum di sekurang-kurangnya satu negara App Store dan dikembalikan oleh iTunes Search API. Aplikasi yang tidak disenaraikan, dialih keluar atau diedarkan untuk perusahaan tidak akan muncul.
{{% /details %}}

{{% details title="Adakah ia menyokong aplikasi macOS dan Apple TV?" closed="true" %}}
Ya. Jika aplikasi mempunyai tangkapan skrin macOS atau Apple TV dalam respons iTunes Search API, AppLookup.pro menunjukkannya dalam panel boleh tatal tersendiri dengan butang muat turun.
{{% /details %}}

{{% details title="Bolehkah saya menggunakan JSON mentah dalam kod saya sendiri?" closed="true" %}}
Ya. Bahagian Raw API Response menunjukkan JSON tepat yang dikembalikan Apple. Salin ke Postman, ujian unit atau saluran paip backend. Sila hormati terma API Apple dan had kadar yang munasabah.
{{% /details %}}

{{% details title="Adakah selamat untuk menampal URL App Store ke dalam alat?" closed="true" %}}
Ya. URL diuraikan dalam pelayar anda. Satu-satunya panggilan rangkaian keluar ialah carian ke iTunes Search API Apple.
{{% /details %}}

{{% details title="Apakah perbezaan antara AppLookup.pro dan AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) adalah untuk membaca metadata App Store daripada mana-mana aplikasi yang diterbitkan: penyelidikan pesaing, muat turun aset, pemeriksaan penyetempatan. [AppKeywords.pro](https://appkeywords.pro) adalah untuk menulis metadata App Store untuk aplikasi anda sendiri: pengoptimuman tajuk, sari kata dan kata kunci dengan sokongan Fastlane. Kedua-dua alat ini berfungsi dengan baik bersama.
{{% /details %}}
