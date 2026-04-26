---
title: "Cara Mengimport Senarai Main M3U ke Evermusic dan Flacbox"
date: 2024-01-31
description: "Ketahui cara mengimport fail senarai main M3U, M3U8 dan CUE dari awan, storan tempatan atau peranti ke Evermusic dan Flacbox."
keywords: ["evermusic", "flacbox", "senarai main", "m3u", "m3u8", "cue", "import", "aplikasi muzik"]
tags: ["evermusic", "import", "senarai main", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Ringkasan:** Evermusic dan Flacbox menyokong pengimportan fail senarai main M3U, M3U8 dan CUE dari storan awan, fail aplikasi tempatan atau peranti anda. Pergi ke Senarai Main > Lagi > Import Senarai Main, pilih sumber, pilih fail anda dan aplikasi akan membina senarai main anda secara automatik.

M3U, yang bermaksud MP3 URL atau Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, ialah format fail komputer yang digunakan untuk senarai main multimedia. Salah satu kegunaan utamanya ialah mencipta fail senarai main entri tunggal yang menunjuk ke strim di internet. Fail-fail ini menawarkan akses mudah kepada kandungan penstriman dan biasanya digunakan untuk muat turun, e-mel dan mendengar radio Internet.

Walaupun penggunaannya meluas, tiada spesifikasi rasmi untuk format M3U; ia telah menjadi standard de facto. Fail M3U pada dasarnya ialah fail teks biasa yang menentukan lokasi satu atau lebih fail media. Bergantung pada pengekodan, ia disimpan dengan sama ada sambungan nama fail "m3u" atau "m3u8". Setiap entri dalam fail menentukan lokasi fail media, yang boleh menjadi nama laluan tempatan mutlak, nama laluan tempatan relatif kepada lokasi fail M3U atau URL. Entri dipisahkan oleh pemisah baris, dengan sesetengah peranti memerlukan pemisah baris yang diwakili sebagai CR LF.

Selain itu, fail M3U boleh mengandungi ulasan yang diawali dengan aksara "#". Dalam M3U lanjutan, "#" memperkenalkan arahan M3U lanjutan, yang mungkin menyokong parameter yang ditamatkan oleh titik bertindih ":".

Dalam aplikasi kami Evermusic dan Flacbox, kami telah melaksanakan fungsi import fail M3U, menghapuskan keperluan untuk mencipta senarai main secara manual. Panduan ini akan membimbing anda melalui pengimportan senarai main anda dari storan awan, fail tempatan atau fail pada peranti anda terus ke dalam aplikasi.

Pertama, navigasi ke bahagian 'Senarai Main'. Seterusnya, ketik butang 'Lagi' yang terletak di sudut kanan atas. Dari menu yang muncul, pilih pilihan 'Import senarai main'.

![tindakan import senarai main](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Pada skrin seterusnya, pilih lokasi fail. Pilihan yang disokong termasuk:

- Storan awan yang disambungkan;
- Fail dalam aplikasi;
- Fail pada peranti anda;

![pilih lokasi fail](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Mari pilih storan awan yang disambungkan dan buka folder yang mengandungi fail senarai main. Sambungan fail senarai main yang disokong termasuk M3U, M3U8 dan CUE. Pilih fail senarai main dan ketik 'Selesai' untuk mengesahkan pilihan anda.

![pilih fail M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Aplikasi akan menghurai fail senarai main dan mencipta senarai trek. Ia kemudian akan mencari fail-fail tersebut pada storan dan menyusun senarai main akhir yang akan diimport ke pustaka muzik. Adalah penting bahawa fail M3U/CUE anda mengandungi laluan yang betul untuk fail media, dan fail-fail tersebut harus berada di laluan tersebut pada storan anda.

![senarai main yang diimport](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Aplikasi menyokong kedua-dua laluan relatif dan URL fail mutlak.

Contohnya:

Senarai main dengan laluan relatif:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Senarai main dengan URL mutlak:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Jika anda mengimport fail senarai main yang terletak dalam aplikasi (bahagian Fail tempatan), tiada langkah tambahan diperlukan.

Walau bagaimanapun, jika anda ingin mengimport senarai main yang terletak pada peranti anda menggunakan pemilih fail sistem, terdapat pertimbangan penting yang perlu diingat.

Disebabkan dasar keselamatan, aplikasi hanya boleh mengakses fail yang anda pilih menggunakan pemilih fail sistem. Walau bagaimanapun, fail senarai main mungkin mengandungi pautan ke fail media lain pada peranti anda. Untuk mengimport senarai main dari peranti anda, anda mesti memilih folder yang mengandungi kedua-dua fail senarai main dan semua fail media yang dipautkan kepadanya. Dalam kes ini, aplikasi akan mengimbas folder yang dipilih, mencari fail senarai main, membina senarai trek dan mengimportnya ke pustaka muzik.

Selain itu, anda boleh mengimport berbilang senarai main sekaligus dengan mengetik butang "Lebih banyak tindakan" dan memilih "Import Senarai Main dari Folder." Aplikasi kemudian akan mengimbas kandungan folder, mencari fail senarai main yang disokong dan mengimportnya ke pustaka.

## Soalan Lazim

{{% details title="Apakah format senarai main yang disokong oleh Evermusic dan Flacbox?" closed="true" %}}
Kedua-dua aplikasi menyokong format fail senarai main M3U, M3U8 dan CUE. Ini meliputi standard senarai main yang paling biasa digunakan oleh pemain muzik dan perisian media.
{{% /details %}}

{{% details title="Bolehkah saya mengimport senarai main dari storan awan?" closed="true" %}}
Ya. Anda boleh mengimport fail senarai main dari mana-mana perkhidmatan storan awan yang disambungkan termasuk Google Drive, Dropbox, OneDrive dan pelayan WebDAV.
{{% /details %}}

{{% details title="Mengapa sesetengah trek hilang selepas import?" closed="true" %}}
Fail senarai main mesti mengandungi laluan yang betul ke fail media anda, dan fail-fail tersebut mesti wujud di lokasi yang dinyatakan pada storan anda. Semak semula bahawa laluan fail dalam fail M3U atau CUE anda sepadan dengan lokasi fail sebenar.
{{% /details %}}

{{% details title="Bolehkah saya mengimport berbilang senarai main sekaligus?" closed="true" %}}
Ya. Gunakan butang Lebih banyak tindakan dan pilih "Import Senarai Main dari Folder." Aplikasi mengimbas folder untuk semua fail senarai main yang disokong dan mengimportnya dalam satu langkah.
{{% /details %}}

{{% details title="Adakah saya perlu mencipta senarai main secara manual?" closed="true" %}}
Tidak. Ciri import menghapuskan penciptaan senarai main secara manual. Hanya halakan aplikasi ke fail M3U, M3U8 atau CUE sedia ada anda dan ia membina senarai main secara automatik.
{{% /details %}}
