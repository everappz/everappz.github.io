---
title: "Cara Menghubungkan Synology NAS dan Mendengarkan Musik di iPhone atau Mac Anda"
date: 2024-09-19
description: "Pelajari cara menghubungkan Synology NAS Anda menggunakan API native atau QuickConnect dan streaming musik berkualitas tinggi ke iPhone atau Mac Anda dengan Evermusic dan Flacbox."
keywords: ["synology nas", "streaming musik", "quickconnect", "evermusic synology", "flacbox synology", "pemutar musik nas", "musik iphone nas"]
tags: ["musik", "streaming", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Ringkasan:** Hubungkan Synology NAS Anda ke Evermusic atau Flacbox menggunakan API native Synology -- baik secara manual melalui alamat IP atau secara otomatis melalui QuickConnect ID. QuickConnect memungkinkan Anda streaming musik dari jarak jauh tanpa port forwarding. Kedua aplikasi mendukung FLAC, MP3, WAV, dan format hi-res lainnya.

Jika Anda mencari cara yang mulus untuk menghubungkan Synology NAS dan menikmati perpustakaan musik Anda di iPhone atau Mac, aplikasi Evermusic dan Flacbox adalah solusi sempurna. Aplikasi ini mendukung berbagai format audio, termasuk FLAC, MP3, dan WAV, memudahkan streaming dan mendengarkan musik berkualitas tinggi langsung dari Synology NAS Anda.

Dalam panduan ini, kami akan menunjukkan cara menghubungkan Synology NAS Anda ke aplikasi Evermusic atau Flacbox menggunakan API native Synology dan fitur QuickConnect. Dengan memanfaatkan API langsung Synology, Anda dapat mengakses perpustakaan musik Anda dengan aman di luar jaringan rumah tanpa memerlukan konfigurasi rumit seperti WebDAV, SMB, DLNA. Dengan QuickConnect, Anda akan dapat streaming dan mengelola musik dari mana saja, menggunakan iPhone atau Mac Anda.

## Langkah 1: Konfigurasi Izin Folder Bersama (Opsional)

1. Buka **Panel Kontrol** dan pergi ke bagian **Folder Bersama**.

![Folder Bersama](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Pilih folder **Musik** dan klik **Edit**.

3. Di tab **Izin**, konfigurasi izin. Aktifkan akses tamu dengan Hanya Baca jika Anda hanya perlu mendengarkan musik, atau Baca/Tulis jika Anda perlu memodifikasi file. Simpan perubahan.

![Izin](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Langkah 2: Temukan Alamat IP Synology NAS

1. Buka **Panel Kontrol** dan pergi ke tab **Antarmuka Jaringan**.

![Antarmuka Jaringan](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Atau gunakan browser web Anda untuk mengunjungi [find.synology.com](http://find.synology.com).

![Temukan Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Catat alamat IP Synology NAS Anda (misalnya, 192.168.18.137).

## Langkah 3: Temukan Port Jaringan Synology NAS

Anda dapat menemukan dokumentasi resmi Synology untuk port jaringan default DSM di [artikel Pusat Pengetahuan Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services) ini.

Synology DSM menggunakan port default berikut:
- **HTTP (Akses Web):** Port **5000**
- **HTTPS (Akses Web Aman):** Port **5001**

Ini adalah port default untuk mengakses antarmuka DSM.

![Port Jaringan](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Langkah 4: Aktifkan Fitur QuickConnect ID

QuickConnect ID Synology adalah pengidentifikasi unik yang memungkinkan Anda mengakses Synology NAS dari jarak jauh melalui internet tanpa perlu mengkonfigurasi pengaturan jaringan rumit seperti port forwarding. QuickConnect menyederhanakan akses jarak jauh dengan menggunakan server Synology untuk membuat koneksi antara NAS dan perangkat Anda, seperti smartphone atau komputer, melalui QuickConnect ID.

**Cara Menemukan atau Mengatur QuickConnect ID Anda:**

1. **Masuk ke DSM.**
2. Pergi ke **Panel Kontrol > Akses Eksternal > QuickConnect**.
3. **Aktifkan QuickConnect** dan buat atau lihat QuickConnect ID unik Anda.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Langkah 5: Hubungkan ke Synology NAS di iPhone/Mac Anda menggunakan Evermusic atau Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) dan [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) adalah aplikasi pemutar musik yang dirancang untuk perangkat iOS dan macOS, masing-masing menawarkan fitur dan kemampuan unik untuk mengelola dan menikmati perpustakaan musik Anda.

1. Buka aplikasi Evermusic atau Flacbox dan pergi ke tab **Koneksi**.

![Koneksi](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Pilih **Hubungkan layanan cloud** dan pilih **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Anda memiliki dua opsi koneksi: **manual** menggunakan alamat IP dan port server, atau **otomatis** melalui QuickConnect ID.

### Koneksi Manual

Untuk metode manual, Anda memerlukan alamat IP langsung dan nomor port yang Anda dapatkan di langkah sebelumnya.

1. Masukkan URL server yang Anda dapatkan di langkah 2, menggunakan format berikut: PROTOKOL://ALAMAT_IP:NOMOR_PORT
   - Gunakan **port 5000** untuk HTTP dan **port 5001** untuk koneksi HTTPS.

   Contoh:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Nomor port aktual dapat dikonfirmasi di langkah 3 pengaturan Anda.
3. Masukkan **login** dan **kata sandi** Anda untuk Synology NAS.
4. Ketuk **Masuk** untuk membuat koneksi.

![Koneksi Manual](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Koneksi Otomatis

Untuk koneksi otomatis, Anda akan menggunakan **QuickConnect ID** dari langkah 4. Alih-alih memasukkan alamat IP dan nomor port Synology NAS secara manual, cukup masukkan **QuickConnect ID**. Aplikasi akan secara otomatis mengambil informasi koneksi yang diperlukan.

Metode ini memungkinkan Anda mengakses NAS dari jarak jauh, bahkan di luar jaringan rumah Anda, sehingga Anda dapat mengelola file dari internet tanpa perlu mengkonfigurasi port forwarding atau alamat IP statis.

![Koneksi Otomatis](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Autentikasi Dua Faktor

Dimulai dari DSM 4.2, Synology memperkenalkan **verifikasi 2 langkah** untuk meningkatkan keamanan. Fitur ini memerlukan kode **kata sandi sekali pakai (OTP)**, yang dihasilkan oleh aplikasi autentikasi, selain kredensial login reguler Anda. Jika Anda telah mengaktifkan verifikasi 2 langkah, setelah memasukkan nama pengguna dan kata sandi, Anda juga perlu memasukkan OTP untuk masuk ke sesi DSM Anda.

Harap diperhatikan, setelah sesi Anda berakhir, aplikasi perlu diotorisasi ulang secara manual. Untuk mengotorisasi ulang:

1. Pergi ke tab **Koneksi** di aplikasi.
2. Ketuk tombol **Lebih banyak tindakan** di sebelah nama server.
3. Pilih **Pengaturan** dari menu untuk memasukkan kode autentikasi baru dan menyelesaikan proses otorisasi ulang.

Ini memastikan bahwa meskipun Anda mengakses NAS dari jaringan yang tidak tepercaya, data Anda tetap aman.

## Langkah 6: Navigasi dan Putar Musik

1. Setelah terhubung, perangkat akan muncul di daftar **Perangkat Terhubung**.

![Perangkat Terhubung](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navigasi ke folder **Musik** dan ketuk file audio apa pun untuk memulai pemutaran.

![Putar Musik](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Langkah 7: Tambahkan Folder Cloud yang Terhubung ke Perpustakaan Musik

1. Buka bagian **Perpustakaan Musik** di aplikasi.
2. Pilih **Tambah Musik** dan pilih **Koneksi**.
3. Pilih server NAS yang terhubung dan pilih folder **Musik**. Ketuk **Selesai**.
4. Aplikasi akan memindai folder musik dan menambahkan file audio yang didukung ke perpustakaan musik. Metadata akan dimuat, dan lagu Anda akan dikelompokkan berdasarkan album, artis, dan genre.

## Kesimpulan

Dengan mengikuti langkah-langkah ini, Anda dapat dengan mudah mengatur koneksi di Synology NAS dan streaming seluruh perpustakaan musik ke iPhone atau Mac menggunakan Evermusic atau Flacbox. Baik di rumah maupun saat bepergian, nikmati akses berkualitas tinggi yang mulus ke lagu favorit Anda dari mana saja menggunakan QuickConnect. Manfaatkan fleksibilitas dan kenyamanan yang ditawarkan aplikasi ini, dan mulai kelola koleksi musik Anda dengan mudah di semua perangkat.

Dengan akses jarak jauh yang aman melalui QuickConnect dan dukungan untuk berbagai format audio, Anda tidak akan pernah jauh dari musik Anda. Sekarang, file yang tersimpan di NAS Anda hanya tinggal satu ketukan!

## FAQ

{{% details title="Apa perbedaan antara koneksi manual dan QuickConnect?" closed="true" %}}
Koneksi manual menggunakan alamat IP dan port NAS, yang berfungsi di jaringan lokal Anda. QuickConnect menggunakan layanan relay Synology untuk membuat koneksi dari mana saja melalui internet, tanpa port forwarding.
{{% /details %}}

{{% details title="Bisakah saya streaming musik dari Synology NAS di luar jaringan rumah?" closed="true" %}}
Ya. Aktifkan QuickConnect di Synology NAS Anda dan gunakan QuickConnect ID di Evermusic atau Flacbox untuk streaming musik dari mana saja dengan koneksi internet.
{{% /details %}}

{{% details title="Format audio apa yang didukung saat streaming dari Synology NAS?" closed="true" %}}
Evermusic dan Flacbox mendukung FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD, dan banyak format lainnya. Semua format yang didukung berfungsi saat streaming dari Synology NAS.
{{% /details %}}

{{% details title="Apakah saya memerlukan autentikasi dua faktor untuk terhubung?" closed="true" %}}
Tidak, autentikasi dua faktor bersifat opsional. Namun, jika Anda telah mengaktifkan verifikasi 2 langkah di Synology DSM Anda, aplikasi akan meminta kata sandi sekali pakai saat login. Anda perlu mengotorisasi ulang saat sesi berakhir.
{{% /details %}}

{{% details title="Haruskah saya menggunakan API native Synology, WebDAV, atau SMB untuk terhubung?" closed="true" %}}
API native Synology dengan QuickConnect adalah pilihan terbaik untuk akses jarak jauh. Untuk penggunaan jaringan lokal, SMB biasanya opsi tercepat. WebDAV berfungsi baik untuk akses lokal dan jarak jauh. Evermusic dan Flacbox mendukung ketiga protokol tersebut.
{{% /details %}}
