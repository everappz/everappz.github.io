---
title: "Cara Menyambung Storan NAS Menggunakan WebDAV dan Mendengar Muzik di iPhone atau Mac Anda"
date: 2024-07-28
description: "Ketahui cara mengkonfigurasi WebDAV pada Synology NAS anda dan strim muzik ke iPhone atau Mac menggunakan Evermusic atau Flacbox. Ikuti panduan langkah demi langkah kami."
keywords: ["sambung nas", "webdav synology", "strim muzik nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["muzik", "penstriman", "storan", "nas", "sambung", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Ringkasan:** Pasang dan aktifkan WebDAV pada Synology NAS anda, konfigurasikan kebenaran folder kongsi, kemudian sambung dari Evermusic atau Flacbox menggunakan alamat IP NAS dan port WebDAV (lalai 5005/5006). Anda boleh strim dan mengurus keseluruhan pustaka muzik tanpa menyalin fail ke peranti anda.

Ketahui cara menyambung storan NAS anda menggunakan WebDAV dan strim pustaka muzik anda ke iPhone atau Mac dengan mudah. WebDAV (Web-based Distributed Authoring and Versioning) ialah protokol yang membolehkan anda mengurus dan berkongsi fail melalui Internet. Dengan menyediakan WebDAV pada NAS anda, anda boleh mengakses dan strim koleksi muzik anda, memastikan lagu kegemaran anda sentiasa di hujung jari.

Dalam panduan ini, kami akan menunjukkan cara menyediakan sambungan WebDAV pada salah satu pelayan NAS yang paling popular, Synology NAS. Ikuti langkah mudah kami untuk mengkonfigurasi WebDAV pada Synology NAS anda, dan anda akan dapat melayari, strim, dan mengurus pustaka muzik terus dari iPhone atau Mac anda.

## Langkah 1: Pasang WebDAV pada Synology NAS

1. Log masuk ke Synology NAS anda dan buka **Pusat Pakej**.
2. Cari "webdav" dan pasang pakej WebDAV jika belum dipasang. Buka pelayan WebDAV untuk mengkonfigurasinya.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Pasang WebDAV pada Synology" width="600" >}}

## Langkah 2: Konfigurasikan Pelayan WebDAV

1. Di halaman tetapan WebDAV, tandakan kotak untuk **Aktifkan HTTP**, **Aktifkan HTTPS**, **Aktifkan WebDAV Tanpa Nama**, dan **Aktifkan DavDepthInfinity**.
2. Klik **Guna** untuk menyimpan perubahan. Catat nombor port untuk sambungan HTTP dan HTTPS, iaitu 5005 dan 5006 secara lalai.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfigurasikan tetapan WebDAV" width="600" >}}

## Langkah 3: Konfigurasikan Kebenaran Folder Kongsi

1. Buka **Panel Kawalan** dan pergi ke bahagian **Folder Kongsi**.
2. Pilih folder **Muzik** dan klik **Edit**.
3. Di tab **Kebenaran**, konfigurasikan kebenaran. Aktifkan akses tetamu dengan Baca Sahaja jika anda hanya perlu mendengar muzik, atau Baca/Tulis jika anda perlu mengubah suai fail. Simpan perubahan.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Kebenaran Folder Kongsi" width="600" >}}

## Langkah 4: Cari Alamat IP Synology NAS

1. Buka **Panel Kawalan** dan pergi ke tab **Antara Muka Rangkaian**, atau gunakan pelayar web untuk melawat [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Cari Alamat IP NAS" width="600" >}}

2. Catat alamat IP Synology NAS anda (contoh, 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Alamat IP Synology NAS" width="600" >}}

## Langkah 5: Sambung ke Synology NAS Menggunakan Evermusic/Flacbox

1. Buka aplikasi Evermusic atau Flacbox dan pergi ke tab **Sambungan**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Tab Sambungan di Evermusic" width="600" >}}

2. Untuk sambungan automatik, cari Synology NAS anda di bahagian **Peranti yang tersedia** dan ketuk untuk menyambung.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Senarai Peranti yang Tersedia" width="600" >}}

3. Untuk sambungan manual, pilih **Sambung perkhidmatan awan** dan pilih **WebDAV**. Masukkan alamat pelayan dalam format: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (contoh, [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Konfigurasi WebDAV Manual" width="600" >}}

4. Biarkan medan log masuk dan kata laluan kosong untuk akses tetamu, atau masukkan kelayakan Synology anda. Ketuk **Log Masuk**.

## Langkah 6: Navigasi dan Main Muzik

1. Setelah disambungkan, peranti akan muncul dalam senarai **Aksesori yang disambungkan**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Peranti Tersambung di Evermusic" width="600" >}}

2. Navigasi ke folder **Muzik** dan ketuk mana-mana fail audio untuk memulakan main balik.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Melayari Folder Muzik" width="600" >}}

## Langkah 7: Tambah Folder Awan yang Disambungkan ke Pustaka Muzik

1. Buka bahagian **Pustaka Muzik** dalam aplikasi.
2. Pilih **Tambah Muzik** dan pilih **Sambungan**.
3. Pilih pelayan NAS yang disambungkan dan pilih folder **Muzik**. Ketuk **Selesai**.
4. Aplikasi akan mengimbas folder muzik dan menambah fail audio yang disokong ke pustaka muzik. Metadata akan dimuatkan, dan trek anda akan dikumpulkan mengikut album, artis, dan genre.

## Kesimpulan

Dengan mengikuti langkah-langkah ini, anda boleh dengan mudah menyediakan sambungan WebDAV pada Synology NAS dan strim pustaka muzik ke iPhone atau Mac menggunakan Evermusic atau Flacbox. Nikmati akses lancar ke lagu kegemaran anda pada bila-bila masa.

## Soalan Lazim

{{% details title="Peranti NAS mana yang menyokong WebDAV?" closed="true" %}}
Kebanyakan jenama NAS popular menyokong WebDAV, termasuk Synology, QNAP, TrueNAS, dan Western Digital. Semak dokumentasi pengeluar NAS anda untuk arahan persediaan WebDAV.
{{% /details %}}

{{% details title="Apakah perbezaan antara WebDAV dan SMB untuk penstriman muzik NAS?" closed="true" %}}
WebDAV berfungsi melalui HTTP/HTTPS dan lebih sesuai untuk akses jauh melalui internet. SMB biasanya lebih pantas pada rangkaian tempatan. Evermusic dan Flacbox menyokong kedua-dua protokol, jadi pilih berdasarkan sama ada anda memerlukan akses tempatan atau jauh.
{{% /details %}}

{{% details title="Adakah saya memerlukan nama pengguna dan kata laluan untuk WebDAV pada Synology?" closed="true" %}}
Tidak, jika anda mengaktifkan akses WebDAV tanpa nama dan mengkonfigurasi kebenaran tetamu pada folder kongsi anda. Untuk keselamatan yang lebih baik, anda boleh menggunakan kelayakan Synology anda.
{{% /details %}}

{{% details title="Bolehkah saya strim FLAC dan format resolusi tinggi lain dari NAS melalui WebDAV?" closed="true" %}}
Ya. Kedua-dua Evermusic dan Flacbox menyokong FLAC, ALAC, WAV, DSD, dan format resolusi tinggi lain semasa strim dari storan NAS melalui WebDAV.
{{% /details %}}

{{% details title="Mengapa aplikasi tidak dapat mencari NAS saya dalam Peranti yang Tersedia?" closed="true" %}}
Pastikan iPhone/Mac dan NAS anda berada pada rangkaian Wi-Fi yang sama. Jika penemuan automatik tidak berfungsi, gunakan pilihan sambungan manual dan masukkan alamat IP NAS dan port WebDAV secara terus.
{{% /details %}}
