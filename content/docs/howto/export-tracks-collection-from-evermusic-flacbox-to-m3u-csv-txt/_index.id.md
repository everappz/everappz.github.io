---
title: "Cara Mengekspor Koleksi Lagu ke M3U, CSV, dan TXT di Evermusic & Flacbox"
date: 2024-01-31
description: "Pelajari cara mengekspor terbaru, favorit, daftar putar, dan album dari Evermusic dan Flacbox ke format M3U, CSV, atau TXT. Sempurna untuk scrobbling Last.fm dan pemutaran di perangkat lain."
keywords: ["evermusic ekspor", "flacbox ekspor", "ekspor ke m3u", "ekspor daftar putar ke csv", "m3u txt csv daftar putar", "ekspor musik"]
tags: ["evermusic", "terbaru", "favorit", "ekspor", "m3u", "daftar putar", "csv", "txt", "album"]
---

{{< author-byline >}}


**Ringkasan:** Evermusic dan Flacbox memungkinkan Anda mengekspor koleksi lagu apa pun (terbaru, favorit, daftar putar, album) ke file CSV, TXT, atau M3U. Gunakan ekspor ini untuk scrobbling ke Last.fm, mencadangkan perpustakaan Anda, atau memutar daftar putar Anda di perangkat lain.

## Pendahuluan

Mengekspor terbaru, favorit, album, dan daftar putar Anda dari aplikasi ke file eksternal bisa sangat berguna. Anda dapat menggunakan file-file ini untuk memperbarui riwayat mendengarkan di layanan scrobbler seperti [Last.fm](http://Last.fm) atau mendengarkan daftar putar Anda di perangkat eksternal. Dengan Evermusic dan Flacbox, proses ini mudah. Di sini, kami akan menunjukkan cara mengekspor terbaru Anda ke CSV/TXT dan daftar putar Anda ke M3U. Namun, fungsionalitas ini tersedia untuk koleksi lagu apa pun di dalam aplikasi.

## Pilih Format

Untuk mengekspor terbaru Anda, buka bagian 'Perpustakaan Musik' dan pilih item menu 'Terbaru'.

![perpustakaan musik](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Di layar berikutnya, ketuk tombol 'Lainnya' di sudut kanan atas dan pilih 'Ekspor daftar lagu'.

![ekspor terbaru](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Di layar 'Pilih format file', Anda memiliki beberapa opsi - CSV, TXT, M3U.

- CSV

Ini adalah singkatan dari Comma-Separated Values, sempurna untuk mengorganisasi data Anda dalam format tabel yang rapi. Di file tujuan, Anda akan menemukan parameter seperti Nama Artis, Nama Album, Nama Lagu, Timestamp (waktu Anda mendengarkan lagu), Nama Artis Album, dan Durasi Lagu. Anda dapat menggunakan file tersebut nanti untuk memperbarui riwayat mendengarkan di layanan scrobbler seperti [Last.fm](http://Last.fm) seperti yang dijelaskan [di sini](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Di sini, kita berbicara tentang file teks biasa. Sederhana dan langsung, dengan parameter termasuk Nama Artis, Nama Album, Nama Lagu, dan Durasi. Berguna jika Anda hanya membutuhkan daftar lagu dalam presentasi teks.

- M3U

Format ini pada dasarnya adalah standar untuk membuat daftar putar. Bagus karena Anda dapat mengekspor daftar lagu dan menikmati lagu-lagu Anda di perangkat apa pun, bahkan jika Anda tidak memiliki file aslinya (jika Anda memilih opsi URL absolut untuk ekspor file media). Di file output, Anda akan menemukan parameter seperti Durasi, Nama Artis, Nama Lagu, dan Lokasi File Media.

## Format CSV

Sekarang, mari pilih CSV dan lihat apa yang akan kita dapatkan. Cukup pilih CSV dan tekan tombol 'Ekspor'.

![pilih format file](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Setelah ekspor selesai, Anda akan melihat notifikasi dengan dua opsi. Mengetuk 'Tampilkan file' akan menampilkan file hasil di direktori dokumen Anda.

![ekspor selesai](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Sekarang Anda dapat mengirim file tersebut, membukanya di editor teks eksternal, atau menggunakannya untuk memperbarui progres mendengarkan Anda di [Last.fm](http://Last.fm).

![folder ekspor dengan file hasil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

File CSV output akan berisi bidang dalam format berikut:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Contohnya:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![file csv yang diekspor](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Format TXT

File TXT output akan berisi bidang dalam format berikut:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Contohnya:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![file txt yang diekspor](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Format M3U

Selanjutnya, kami akan memandu Anda melalui ekspor daftar putar Anda ke format M3U, yang merupakan standar de facto untuk file daftar putar. Prasyarat utama untuk ekspor daftar putar yang berhasil adalah semua file dalam daftar putar harus berada di penyimpanan yang sama, baik itu layanan cloud seperti Google Drive Anda, file lokal, atau file di perangkat Anda. Untuk memulai proses ekspor, buka daftar putar mana pun dan ketuk tombol 'Lainnya' di sudut kanan atas, lalu pilih item menu 'Ekspor daftar lagu'.

![layar daftar putar](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Di layar berikutnya, pilih format file 'M3U', di mana Anda akan menemukan dua opsi untuk 'Tipe lokasi file media':

![layar pilih format file ekspor](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Jika Anda memilih 'Jalur relatif', daftar putar akan dibuat dengan lokasi file media yang ditulis relatif terhadap file daftar putar. Contohnya:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Dalam hal ini, hindari mengubah lokasi file M3U setelah ekspor selesai, karena hal tersebut akan merusak jalur untuk file media. Untuk memulai pemutaran daftar putar Anda, cukup ketuk file daftar putar yang diekspor, dan aplikasi akan secara otomatis menemukan file media di penyimpanan Anda dan memulai pemutaran. Bahkan Anda dapat mengekspor daftar putar Anda ke penyimpanan dan kemudian mengimpornya kembali di perangkat baru Anda.

2. Jika Anda memilih 'URL Absolut', aplikasi akan menghasilkan URL langsung untuk file media Anda. Ini memungkinkan Anda memutar daftar putar di perangkat/aplikasi apa pun tanpa perlu semua file media berada di penyimpanan yang sama dengan file daftar putar. Opsi ini hanya didukung untuk penyimpanan cloud yang mampu menghasilkan URL file langsung. Namun, perlu diingat bahwa dalam beberapa kasus, URL yang dihasilkan mungkin memiliki masa aktif terbatas dan dapat kedaluwarsa setelah beberapa waktu. Berikut daftar layanan cloud yang didukung: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (jika dalam mode tamu)  

URL file media output akan terlihat seperti ini:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Setelah Anda memilih 'Tipe lokasi file media', ketuk 'Ekspor'. Aplikasi akan meminta Anda untuk memilih folder tujuan untuk mengekspor file M3U. Ketuk 'Selesai' untuk mengonfirmasi pilihan Anda.

![pilih folder](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Aplikasi akan menghasilkan file M3U dan mengunggah/memindahkannya ke folder tujuan.

![mengunggah file m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Setelah ekspor selesai, notifikasi sistem akan muncul dengan opsi 'Tampilkan file'.

![notifikasi ekspor selesai](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Mengetuk ini akan menampilkan file yang diekspor di aplikasi.

![file m3u yang diekspor dalam daftar file](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Jika Anda memilih 'Jalur relatif' sebagai 'Tipe lokasi file media' di langkah sebelumnya, file output akan dalam format berikut:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![contoh m3u dengan jalur relatif](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Untuk opsi 'URL Absolut', aplikasi akan menghasilkan file M3U dalam format:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![contoh m3u dengan URL file absolut](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Anda dapat membuka file tersebut di perangkat/aplikasi apa pun yang mendukung daftar putar M3U.

![daftar putar m3u dibuka di aplikasi eksternal](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Penutup

Mengekspor lagu-lagu Anda dari Evermusic dan Flacbox memberi Anda kendali penuh atas data musik Anda. Baik Anda mencadangkan riwayat mendengarkan, melakukan scrobbling ke Last.fm, atau menikmati daftar putar di perangkat eksternal, opsi ekspor ini: M3U, CSV, dan TXT - adalah alat yang kuat yang dirancang untuk fleksibilitas dan kompatibilitas. Manfaatkan fitur-fitur ini untuk meningkatkan cara Anda mengorganisasi, membagikan, dan menikmati kembali koleksi musik Anda di berbagai platform.

## Pertanyaan yang Sering Diajukan

{{% details title="Format ekspor mana yang harus saya gunakan untuk scrobbling Last.fm?" closed="true" %}}
Gunakan CSV. Format ini mencakup timestamp dan metadata lengkap yang diperlukan oleh alat scrobbling seperti Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Bisakah saya mengekspor koleksi lagu apa pun, bukan hanya daftar putar?" closed="true" %}}
Ya. Anda dapat mengekspor terbaru, favorit, album, daftar putar, dan koleksi lagu lainnya di aplikasi menggunakan langkah-langkah yang sama.
{{% /details %}}

{{% details title="Apakah daftar putar M3U saya akan berfungsi di perangkat lain?" closed="true" %}}
Jika Anda memilih opsi URL Absolut selama ekspor, file M3U dapat diputar di perangkat apa pun yang mendukung daftar putar M3U. Perlu diperhatikan bahwa beberapa URL cloud mungkin kedaluwarsa seiring waktu.
{{% /details %}}

{{% details title="Apakah fitur ekspor gratis?" closed="true" %}}
Ya. Mengekspor koleksi lagu ke M3U, CSV, dan TXT tersedia di versi gratis maupun premium Evermusic dan Flacbox.
{{% /details %}}

{{% details title="Layanan cloud apa yang mendukung ekspor URL Absolut?" closed="true" %}}
Ekspor URL Absolut didukung untuk iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive, dan WebDAV (mode tamu).
{{% /details %}}
