---
title: "Cara Menghubungkan Penyimpanan NAS Menggunakan WebDAV dan Mendengarkan Musik di iPhone atau Mac Anda"
date: 2024-07-28
description: "Pelajari cara mengonfigurasi WebDAV di Synology NAS Anda dan streaming musik ke iPhone atau Mac menggunakan Evermusic atau Flacbox. Ikuti panduan langkah demi langkah kami."
keywords: ["hubungkan nas", "webdav synology", "streaming musik nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["musik", "streaming", "penyimpanan", "nas", "hubungkan", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Ringkasan:** Instal dan aktifkan WebDAV di Synology NAS Anda, konfigurasikan izin folder bersama, lalu hubungkan dari Evermusic atau Flacbox menggunakan alamat IP NAS dan port WebDAV (default 5005/5006). Anda dapat streaming dan mengelola seluruh perpustakaan musik tanpa menyalin file ke perangkat Anda.

Temukan cara menghubungkan penyimpanan NAS Anda menggunakan WebDAV dan dengan mudah streaming perpustakaan musik ke iPhone atau Mac Anda. WebDAV (Web-based Distributed Authoring and Versioning) adalah protokol yang memungkinkan Anda mengelola dan berbagi file melalui Internet. Dengan menyiapkan WebDAV di NAS Anda, Anda dapat mengakses dan streaming koleksi musik Anda, memastikan lagu-lagu favorit Anda selalu dalam jangkauan.

Dalam panduan ini, kami akan menunjukkan cara menyiapkan koneksi WebDAV di salah satu server NAS paling populer, Synology NAS. Ikuti langkah-langkah sederhana kami untuk mengonfigurasi WebDAV di Synology NAS Anda, dan Anda akan dapat menelusuri, streaming, dan mengelola perpustakaan musik langsung dari iPhone atau Mac Anda.

## Langkah 1: Instal WebDAV di Synology NAS

1. Masuk ke Synology NAS Anda dan buka **Pusat Paket**.
2. Cari "webdav" dan instal paket WebDAV jika belum terinstal. Buka server WebDAV untuk mengonfigurasinya.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Instal WebDAV di Synology" width="600" >}}

## Langkah 2: Konfigurasikan Server WebDAV

1. Di halaman pengaturan WebDAV, centang kotak untuk **Aktifkan HTTP**, **Aktifkan HTTPS**, **Aktifkan WebDAV Anonim**, dan **Aktifkan DavDepthInfinity**.
2. Klik **Terapkan** untuk menyimpan perubahan. Catat nomor port untuk koneksi HTTP dan HTTPS, yaitu 5005 dan 5006 secara default.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfigurasikan pengaturan WebDAV" width="600" >}}

## Langkah 3: Konfigurasikan Izin Folder Bersama

1. Buka **Panel Kontrol** dan buka bagian **Folder Bersama**.
2. Pilih folder **Musik** dan klik **Edit**.
3. Di tab **Izin**, konfigurasikan izin. Aktifkan akses tamu dengan Hanya Baca jika Anda hanya perlu mendengarkan musik, atau Baca/Tulis jika Anda perlu memodifikasi file. Simpan perubahan.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Izin Folder Bersama" width="600" >}}

## Langkah 4: Temukan Alamat IP Synology NAS

1. Buka **Panel Kontrol** dan buka tab **Antarmuka Jaringan**, atau gunakan browser web untuk mengunjungi [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Temukan Alamat IP NAS" width="600" >}}

2. Catat alamat IP Synology NAS Anda (misalnya, 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Alamat IP Synology NAS" width="600" >}}

## Langkah 5: Hubungkan ke Synology NAS Menggunakan Evermusic/Flacbox

1. Buka aplikasi Evermusic atau Flacbox dan buka tab **Koneksi**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Tab Koneksi di Evermusic" width="600" >}}

2. Untuk koneksi otomatis, temukan Synology NAS Anda di bagian **Perangkat yang Tersedia** dan ketuk untuk terhubung.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Daftar Perangkat yang Tersedia" width="600" >}}

3. Untuk koneksi manual, pilih **Hubungkan layanan cloud** dan pilih **WebDAV**. Masukkan alamat server dalam format: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (misalnya, [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Konfigurasi WebDAV Manual" width="600" >}}

4. Biarkan kolom login dan kata sandi kosong untuk akses tamu, atau masukkan kredensial Synology Anda. Ketuk **Masuk**.

## Langkah 6: Navigasi dan Putar Musik

1. Setelah terhubung, perangkat akan muncul di daftar **Aksesori terhubung**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Perangkat Terhubung di Evermusic" width="600" >}}

2. Navigasi ke folder **Musik** dan ketuk file audio apa pun untuk mulai memutar.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Menjelajahi Folder Musik" width="600" >}}

## Langkah 7: Tambahkan Folder Cloud yang Terhubung ke Perpustakaan Musik

1. Buka bagian **Perpustakaan Musik** di aplikasi.
2. Pilih **Tambah Musik** dan pilih **Koneksi**.
3. Pilih server NAS yang terhubung dan pilih folder **Musik**. Ketuk **Selesai**.
4. Aplikasi akan memindai folder musik dan menambahkan file audio yang didukung ke perpustakaan musik. Metadata akan dimuat, dan trek Anda akan dikelompokkan berdasarkan album, artis, dan genre.

## Kesimpulan

Dengan mengikuti langkah-langkah ini, Anda dapat dengan mudah menyiapkan koneksi WebDAV di Synology NAS dan streaming perpustakaan musik ke iPhone atau Mac menggunakan Evermusic atau Flacbox. Nikmati akses tanpa hambatan ke lagu-lagu favorit Anda kapan saja.

## FAQ

{{% details title="Perangkat NAS mana yang mendukung WebDAV?" closed="true" %}}
Sebagian besar merek NAS populer mendukung WebDAV, termasuk Synology, QNAP, TrueNAS, dan Western Digital. Periksa dokumentasi produsen NAS Anda untuk instruksi pengaturan WebDAV.
{{% /details %}}

{{% details title="Apa perbedaan antara WebDAV dan SMB untuk streaming musik dari NAS?" closed="true" %}}
WebDAV bekerja melalui HTTP/HTTPS dan lebih cocok untuk akses jarak jauh melalui internet. SMB biasanya lebih cepat di jaringan lokal. Evermusic dan Flacbox mendukung kedua protokol, jadi pilih berdasarkan apakah Anda memerlukan akses lokal atau jarak jauh.
{{% /details %}}

{{% details title="Apakah saya memerlukan nama pengguna dan kata sandi untuk WebDAV di Synology?" closed="true" %}}
Tidak, jika Anda mengaktifkan akses WebDAV anonim dan mengonfigurasi izin tamu di folder bersama Anda. Untuk keamanan yang lebih baik, Anda dapat menggunakan kredensial Synology Anda.
{{% /details %}}

{{% details title="Bisakah saya streaming FLAC dan format hi-res lainnya dari NAS melalui WebDAV?" closed="true" %}}
Ya. Baik Evermusic maupun Flacbox mendukung FLAC, ALAC, WAV, DSD, dan format resolusi tinggi lainnya saat streaming dari penyimpanan NAS melalui WebDAV.
{{% /details %}}

{{% details title="Mengapa aplikasi tidak dapat menemukan NAS saya di Perangkat yang Tersedia?" closed="true" %}}
Pastikan iPhone/Mac dan NAS Anda berada di jaringan Wi-Fi yang sama. Jika penemuan otomatis tidak berfungsi, gunakan opsi koneksi manual dan masukkan alamat IP NAS dan port WebDAV secara langsung.
{{% /details %}}
