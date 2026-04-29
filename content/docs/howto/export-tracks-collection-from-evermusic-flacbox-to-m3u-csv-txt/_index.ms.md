---
title: "Cara Mengeksport Koleksi Trek ke M3U, CSV dan TXT dalam Evermusic & Flacbox"
date: 2024-01-31
description: "Ketahui cara mengeksport terkini, kegemaran, senarai main dan album anda dari Evermusic dan Flacbox ke format M3U, CSV atau TXT. Sesuai untuk scrobbling Last.fm dan main balik pada peranti lain."
keywords: ["eksport evermusic", "eksport flacbox", "eksport ke m3u", "eksport senarai main ke csv", "m3u txt csv senarai main", "eksport muzik"]
tags: ["evermusic", "terkini", "kegemaran", "eksport", "m3u", "senarai main", "csv", "txt", "album"]
---

{{< author-byline >}}


**Ringkasan:** Evermusic dan Flacbox membolehkan anda mengeksport mana-mana koleksi trek (terkini, kegemaran, senarai main, album) ke fail CSV, TXT atau M3U. Gunakan eksport ini untuk scrobble ke Last.fm, membuat sandaran pustaka anda, atau memainkan senarai main anda pada peranti lain.

## Pengenalan

Mengeksport terkini, kegemaran, album dan senarai main anda dari aplikasi ke fail luaran boleh menjadi sangat berguna. Anda boleh menggunakan fail ini untuk mengemas kini sejarah pendengaran anda pada perkhidmatan scrobbler seperti [Last.fm](http://Last.fm) atau mendengar senarai main anda pada peranti luaran. Dengan Evermusic dan Flacbox, proses ini mudah. Di sini, kami akan menunjukkan cara mengeksport terkini anda ke CSV/TXT dan senarai main anda ke M3U. Walau bagaimanapun, fungsi ini tersedia untuk mana-mana koleksi trek dalam aplikasi.

## Pilih Format

Untuk mengeksport terkini anda, buka bahagian 'Pustaka Muzik' dan pilih item menu 'Terkini'.

![pustaka muzik](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Pada skrin seterusnya, ketik butang 'Lagi' di sudut kanan atas dan pilih 'Eksport senarai lagu'.

![eksport terkini](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Pada skrin 'Pilih format fail', anda mempunyai beberapa pilihan - CSV, TXT, M3U.

- CSV

Singkatan untuk Comma-Separated Values, sesuai untuk menyusun data anda dalam format jadual yang kemas. Dalam fail destinasi, anda akan menemui parameter seperti Nama Artis, Nama Album, Nama Trek, Cap Masa (masa anda mendengar trek), Nama Artis Album dan Tempoh Trek. Anda boleh menggunakan fail itu kemudian untuk mengemas kini sejarah pendengaran anda pada perkhidmatan scrobbler seperti [Last.fm](http://Last.fm) seperti yang diterangkan [di sini](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Di sini, kita bercakap tentang fail teks biasa. Ia mudah dan ringkas, dengan parameter termasuk Nama Artis, Nama Album, Nama Trek dan Tempoh. Berguna jika anda hanya memerlukan senarai trek dalam bentuk teks.

- M3U

Format ini pada dasarnya adalah pilihan utama untuk membuat senarai main. Ia bagus kerana anda boleh mengeksport senarai lagu anda dan menikmati trek anda pada mana-mana peranti, walaupun tanpa fail asal (jika anda memilih pilihan URL mutlak untuk fail media semasa eksport). Dalam fail output, anda akan menemui parameter seperti Tempoh, Nama Artis, Nama Trek dan Lokasi Fail Media.

## Format CSV

Sekarang, mari pilih CSV dan lihat apa yang akan kita terima. Cukup pilih CSV dan tekan butang 'Eksport'.

![pilih format fail](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Setelah eksport selesai, anda akan melihat amaran dengan dua pilihan. Mengetik 'Tunjuk fail' akan memaparkan fail hasil dalam direktori dokumen anda.

![eksport selesai](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Kini anda boleh menghantar fail itu, membukanya dalam penyunting teks luaran, atau menggunakannya untuk mengemas kini kemajuan pendengaran anda di [Last.fm](http://Last.fm).

![folder dengan fail hasil eksport](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Fail CSV output akan mengandungi medan dalam format berikut:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Contoh:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![fail CSV yang dieksport](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Format TXT

Fail TXT output akan mengandungi medan dalam format berikut:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Contoh:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![fail TXT yang dieksport](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Format M3U

Seterusnya, kami akan membimbing anda melalui pengeksportan senarai main anda ke format M3U, yang merupakan standard de facto untuk fail senarai main. Prasyarat utama untuk pengeksportan senarai main yang berjaya ialah semua fail dalam senarai main mesti berada pada storan yang sama, sama ada dalam perkhidmatan awan seperti Google Drive anda, fail tempatan, atau fail pada peranti anda. Untuk memulakan proses eksport, buka mana-mana senarai main dan ketik butang 'Lagi' di sudut kanan atas, kemudian pilih item menu 'Eksport senarai lagu'.

![skrin senarai main](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Pada skrin seterusnya, pilih format fail 'M3U', di mana anda akan menemui dua pilihan untuk 'Jenis lokasi fail media':

![skrin pilih format fail eksport](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Jika anda memilih 'Laluan relatif', senarai main akan dibuat dengan lokasi fail media ditulis secara relatif kepada fail senarai main. Contoh:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Dalam kes ini, elakkan menukar lokasi fail M3U selepas eksport selesai, kerana ini akan merosakkan laluan untuk fail media. Untuk memulakan main balik senarai main anda, cukup ketik pada fail senarai main yang dieksport, dan aplikasi akan secara automatik mencari fail media pada storan anda dan memulakan main balik. Atau anda juga boleh mengeksport senarai main anda ke storan dan kemudian mengimportnya semula pada peranti baharu anda.

2. Jika anda memilih 'URL Mutlak', aplikasi akan menjana URL langsung untuk fail media anda. Ini membolehkan anda memainkan senarai main pada mana-mana peranti/aplikasi tanpa memerlukan semua fail media berada pada storan yang sama dengan fail senarai main. Pilihan ini hanya disokong untuk storan awan yang mampu menjana URL fail langsung. Walau bagaimanapun, perlu diingat bahawa dalam sesetengah kes, URL yang dijana mungkin mempunyai jangka hayat terhad dan boleh tamat tempoh selepas beberapa waktu. Berikut adalah senarai perkhidmatan awan yang disokong: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (jika dalam mod tetamu)  

URL fail media output akan kelihatan seperti ini:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Setelah anda memilih 'Jenis lokasi fail media', ketik 'Eksport'. Aplikasi akan meminta anda memilih folder destinasi untuk mengeksport fail M3U. Ketik 'Selesai' untuk mengesahkan pilihan anda.

![pilih folder](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Aplikasi akan menjana fail M3U dan memuat naik/memindahkannya ke folder destinasi.

![memuat naik fail m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Setelah eksport selesai, amaran sistem akan muncul dengan pilihan untuk 'Tunjuk fail'.

![amaran eksport selesai](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Mengetiknya akan memaparkan fail yang dieksport dalam aplikasi.

![fail m3u yang dieksport dalam senarai fail](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Jika anda memilih 'Laluan relatif' sebagai 'Jenis lokasi fail media' dalam langkah sebelumnya, fail output akan dalam format berikut:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![contoh m3u dengan laluan relatif](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Untuk pilihan 'URL Mutlak', aplikasi akan menjana fail M3U dalam format:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![contoh m3u dengan URL fail mutlak](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Anda boleh membuka fail itu pada mana-mana peranti/aplikasi yang menyokong senarai main M3U.

![senarai main m3u dibuka dalam aplikasi luaran](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Penutup

Mengeksport trek anda dari Evermusic dan Flacbox memberi anda kawalan penuh terhadap data muzik anda. Sama ada anda membuat sandaran sejarah pendengaran, scrobbling ke Last.fm, atau menikmati senarai main pada peranti luaran, pilihan eksport ini: M3U, CSV dan TXT - adalah alat berkuasa yang direka untuk fleksibiliti dan keserasian. Manfaatkan ciri-ciri ini untuk meningkatkan cara anda menyusun, berkongsi dan melawat semula koleksi muzik anda merentasi platform.

## FAQ

{{% details title="Format eksport mana yang perlu saya gunakan untuk scrobbling Last.fm?" closed="true" %}}
Gunakan CSV. Ia termasuk cap masa dan metadata penuh yang diperlukan oleh alat scrobbling seperti Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Bolehkah saya mengeksport mana-mana koleksi trek, bukan hanya senarai main?" closed="true" %}}
Ya. Anda boleh mengeksport terkini, kegemaran, album, senarai main dan mana-mana koleksi trek lain dalam aplikasi menggunakan langkah yang sama.
{{% /details %}}

{{% details title="Adakah senarai main M3U saya berfungsi pada peranti lain?" closed="true" %}}
Jika anda memilih pilihan URL Mutlak semasa eksport, fail M3U boleh dimainkan pada mana-mana peranti yang menyokong senarai main M3U. Perlu diingat bahawa sesetengah URL awan mungkin tamat tempoh dari semasa ke semasa.
{{% /details %}}

{{% details title="Adakah ciri eksport percuma?" closed="true" %}}
Ya. Mengeksport koleksi trek ke M3U, CSV dan TXT tersedia dalam kedua-dua versi percuma dan premium Evermusic dan Flacbox.
{{% /details %}}

{{% details title="Perkhidmatan awan mana yang menyokong eksport URL Mutlak?" closed="true" %}}
Eksport URL Mutlak disokong untuk iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive dan WebDAV (mod tetamu).
{{% /details %}}
