---
title: "Cara Mengimpor Daftar Putar M3U ke Evermusic dan Flacbox"
date: 2024-01-31
description: "Pelajari cara mengimpor file daftar putar M3U, M3U8, dan CUE dari cloud, penyimpanan lokal, atau perangkat ke Evermusic dan Flacbox."
keywords: ["evermusic", "flacbox", "daftar putar", "m3u", "m3u8", "cue", "impor", "aplikasi musik"]
tags: ["evermusic", "impor", "daftar putar", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Ringkasan:** Evermusic dan Flacbox mendukung pengimporan file daftar putar M3U, M3U8, dan CUE dari penyimpanan cloud, file aplikasi lokal, atau perangkat Anda. Buka Daftar Putar > Lainnya > Impor Daftar Putar, pilih sumber, pilih file Anda, dan aplikasi akan membuat daftar putar secara otomatis.

M3U, singkatan dari MP3 URL atau Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, adalah format file komputer yang digunakan untuk daftar putar multimedia. Salah satu penggunaan utamanya adalah membuat file daftar putar entri tunggal yang mengarah ke stream di internet. File-file ini menawarkan akses mudah ke konten streaming dan umumnya digunakan untuk unduhan, email, dan mendengarkan radio Internet.

Meskipun penggunaannya luas, tidak ada spesifikasi formal untuk format M3U; format ini telah menjadi standar de facto. File M3U pada dasarnya adalah file teks biasa yang menentukan lokasi satu atau lebih file media. Tergantung pada pengkodean, file disimpan dengan ekstensi "m3u" atau "m3u8". Setiap entri dalam file menentukan lokasi file media, yang dapat berupa nama jalur lokal absolut, nama jalur lokal relatif terhadap lokasi file M3U, atau URL. Entri dipisahkan oleh jeda baris, dengan beberapa perangkat memerlukan jeda baris yang direpresentasikan sebagai CR LF.

Selain itu, file M3U dapat menyertakan komentar yang diawali dengan karakter "#". Dalam M3U yang diperluas, "#" memperkenalkan direktif M3U yang diperluas, yang dapat mendukung parameter yang diakhiri dengan titik dua ":".

Di aplikasi kami Evermusic dan Flacbox, kami telah mengimplementasikan fungsionalitas impor file M3U, menghilangkan kebutuhan untuk membuat daftar putar secara manual. Panduan ini akan memandu Anda mengimpor daftar putar dari penyimpanan cloud, file lokal, atau file di perangkat Anda langsung ke aplikasi.

Pertama, navigasi ke bagian 'Daftar Putar'. Selanjutnya, ketuk tombol 'Lainnya' yang terletak di sudut kanan atas. Dari menu yang muncul, pilih opsi 'Impor daftar putar'.

![aksi impor daftar putar](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Di layar berikutnya, pilih lokasi file. Opsi yang didukung meliputi:

- Penyimpanan cloud yang terhubung;
- File di aplikasi;
- File di perangkat Anda;

![pilih lokasi file](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Mari pilih penyimpanan cloud yang terhubung dan buka folder yang berisi file daftar putar. Ekstensi file daftar putar yang didukung meliputi M3U, M3U8, dan CUE. Pilih file daftar putar dan ketuk 'Selesai' untuk mengonfirmasi pilihan Anda.

![pilih file M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Aplikasi akan mengurai file daftar putar dan membuat daftar trek. Kemudian akan menemukan file-file tersebut di penyimpanan dan menyusun daftar putar final yang akan diimpor ke perpustakaan musik. Sangat penting bahwa file M3U/CUE Anda berisi jalur yang benar untuk file media, dan file-file tersebut harus berada di jalur tersebut di penyimpanan Anda.

![daftar putar yang diimpor](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Aplikasi mendukung jalur relatif dan URL file absolut.

Contohnya:

Daftar putar dengan jalur relatif:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Daftar putar dengan URL absolut:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Jika Anda mengimpor file daftar putar yang terletak di dalam aplikasi (bagian File lokal), tidak ada langkah tambahan yang diperlukan.

Namun, jika Anda ingin mengimpor daftar putar yang terletak di perangkat Anda menggunakan pemilih file sistem, ada pertimbangan penting yang perlu diingat.

Karena kebijakan keamanan, aplikasi hanya dapat mengakses file yang Anda pilih menggunakan pemilih file sistem. Namun, file daftar putar mungkin menyertakan tautan ke file media lain di perangkat Anda. Untuk mengimpor daftar putar dari perangkat Anda, Anda harus memilih folder yang berisi file daftar putar dan semua file media yang ditautkan. Dalam hal ini, aplikasi akan memindai folder yang dipilih, menemukan file daftar putar, membangun daftar trek, dan mengimpornya ke perpustakaan musik.

Selain itu, Anda dapat mengimpor beberapa daftar putar sekaligus dengan mengetuk tombol "Lebih banyak tindakan" dan memilih "Impor Daftar Putar dari Folder." Aplikasi kemudian akan memindai konten folder, menemukan file daftar putar yang didukung, dan mengimpornya ke perpustakaan.

## Pertanyaan yang Sering Diajukan

{{% details title="Format daftar putar apa yang didukung Evermusic dan Flacbox?" closed="true" %}}
Kedua aplikasi mendukung format file daftar putar M3U, M3U8, dan CUE. Format ini mencakup standar daftar putar paling umum yang digunakan oleh pemutar musik dan perangkat lunak media.
{{% /details %}}

{{% details title="Bisakah saya mengimpor daftar putar dari penyimpanan cloud?" closed="true" %}}
Ya. Anda dapat mengimpor file daftar putar dari layanan penyimpanan cloud yang terhubung termasuk Google Drive, Dropbox, OneDrive, dan server WebDAV.
{{% /details %}}

{{% details title="Mengapa beberapa trek hilang setelah impor?" closed="true" %}}
File daftar putar harus berisi jalur yang benar ke file media Anda, dan file-file tersebut harus ada di lokasi yang ditentukan di penyimpanan Anda. Periksa kembali bahwa jalur file di file M3U atau CUE Anda sesuai dengan lokasi file yang sebenarnya.
{{% /details %}}

{{% details title="Bisakah saya mengimpor beberapa daftar putar sekaligus?" closed="true" %}}
Ya. Gunakan tombol Lebih banyak tindakan dan pilih "Impor Daftar Putar dari Folder." Aplikasi memindai folder untuk semua file daftar putar yang didukung dan mengimpornya dalam satu langkah.
{{% /details %}}

{{% details title="Apakah saya perlu membuat daftar putar secara manual?" closed="true" %}}
Tidak. Fitur impor menghilangkan pembuatan daftar putar manual. Cukup arahkan aplikasi ke file M3U, M3U8, atau CUE Anda yang sudah ada dan aplikasi akan membuat daftar putar secara otomatis.
{{% /details %}}
