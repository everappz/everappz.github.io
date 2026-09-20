---
title: "Cara Menyiapkan Server WebDAV di iPhone & iPad untuk Akses & Berbagi File"
description: "Ubah iPhone atau iPad Anda jadi server WebDAV dengan Everdisk dan pasang sebagai network drive di Mac Finder, Windows File Explorer, Linux, Android, atau iPhone lain lewat Wi-Fi. Panduan lengkap, alamat serta port WebDAV, dan langkah demi langkah koneksi untuk setiap perangkat."
date: 2026-09-19
tags: ["everdisk", "webdav", "network drive", "berbagi file", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["server WebDAV iPhone", "server WebDAV iPad", "cara menyiapkan WebDAV di iPhone", "pasang iPhone sebagai network drive", "sambungkan iPhone WebDAV Mac Finder", "WebDAV Windows File Explorer iPhone", "iphone network drive Windows", "WebDAV Linux iPhone", "akses file iPhone dari komputer", "webdav iphone ke iphone", "berbagi file iPhone WebDAV", "petakan network drive iphone", "transfer file iphone webdav", "alamat port webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV mengubah sebuah folder menjadi network drive yang bisa dibuka komputer di pengelola filenya yang biasa. WebDAV berjalan di atas protokol web yang sama dengan yang dipakai browser Anda, itulah sebabnya ia bepergian dengan baik lintas Mac, Windows, dan Linux tanpa driver khusus. Dengan [Everdisk](/products/everdisk) Anda bisa menjalankan server WebDAV di iPhone atau iPad Anda, sehingga ponsel muncul sebagai drive yang bisa Anda jelajahi, salin darinya, dan salin ke dalamnya dari hampir semua komputer.

WebDAV adalah pilihan terbaik saat Windows terlibat, karena Windows File Explorer menyambung ke sana dengan bersih. Panduan ini mencakup penyiapan serta cara menyambung dari Mac, Windows, Linux, Android, dan iPhone kedua.

## Yang Anda perlukan

- iPhone atau iPad dengan [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) terpasang.
- Komputer atau perangkat lain di **jaringan Wi-Fi yang sama**.
- File yang ingin Anda bagikan, di folder Dokumen Everdisk atau di folder yang Anda tambahkan.

## Siapkan server WebDAV di Everdisk

### Langkah 1: Pilih apa yang dibagikan dan atur akses

Buka Everdisk, masuk ke tab **Berbagi**, dan ketuk **Apa yang Dibagikan**. Folder Dokumen dibagikan secara bawaan. Tambahkan lebih banyak dengan **Tambah Folder** dan **Tambah Berkas**.

Buka **Pengaturan**, lalu **Berbagi**, lalu **Akses**. Aktifkan **Pengeditan Berkas** jika Anda ingin komputer yang terhubung bisa menyalin file ke ponsel Anda serta mengganti nama atau menghapusnya, atau matikan untuk drive hanya-baca. Atur **Info Masuk** dan **Kata Sandi** di sini jika Anda ingin ada masuk, atau biarkan keduanya kosong untuk akses tamu.

### Langkah 2: Aktifkan server WebDAV

Masuk ke **Pengaturan**, lalu **Berbagi**, lalu **Koneksi**, dan aktifkan **Komputer**. Itulah server WebDAV (membawa tag WebDAV).

### Langkah 3: Mulai berbagi dan catat alamatnya

Kembali ke tab **Berbagi** dan ketuk **Mulai**. Bagian **Cara Menghubungkan** menampilkan alamat WebDAV. Tampilannya seperti ini:

```
http://192.168.1.20:8080
```

Angka setelah titik dua adalah **port**, yaitu **8080** secara bawaan. Bagian pertama adalah alamat iPhone Anda di Wi-Fi, jadi milik Anda akan berbeda. Biarkan Everdisk tetap terbuka di layar saat sebuah perangkat terhubung.

## Sambung dari Mac

1. Buka **Finder**, pilih **Go**, lalu **Connect to Server** (atau tekan **Command dan K**).
2. Ketik alamat WebDAV yang ditampilkan di Everdisk, misalnya `http://192.168.1.20:8080`.
3. Klik **Connect**, lalu pilih **Guest** atau masukkan **Info Masuk** dan **Kata Sandi** Anda.

iPhone Anda terbuka di jendela Finder dan berperilaku seperti folder biasa. Salin file ke arah mana pun jika Pengeditan Berkas aktif.

## Sambung dari Windows

Windows punya klien WebDAV bawaan, jadi ini berfungsi dari File Explorer.

1. Buka **File Explorer**, klik kanan **This PC** di bilah samping, dan pilih **Add a network location** (Anda juga bisa memakai **Map network drive**).
2. Saat diminta alamat, ketik alamat WebDAV yang sama dari Everdisk, misalnya `http://192.168.1.20:8080`, lalu klik **Next**.
3. Masukkan **Info Masuk** dan **Kata Sandi** Anda jika Anda mengaturnya.

Perangkat kemudian muncul di bawah This PC sebagai lokasi jaringan yang bisa Anda buka dan salin filenya. Jika Windows menolak menyambung pada percobaan pertama, pastikan layanan **WebClient** berjalan (cari Services di menu Start, temukan WebClient, dan atur agar mulai), lalu coba lagi.

## Sambung dari Linux

1. Buka pengelola file Anda dan pilih **Connect to Server** atau **Other Locations**.
2. Masukkan alamat dengan awalan WebDAV, misalnya `dav://192.168.1.20:8080` (pakai `davs://` hanya jika Anda menyiapkan TLS).
3. Sambung sebagai tamu atau masukkan login Anda.

## Sambung dari Android

Android tidak punya browser WebDAV bawaan sistem, jadi gunakan pengelola file yang mendukungnya:

1. Pasang aplikasi seperti **Solid Explorer** atau **CX File Explorer**.
2. Tambahkan koneksi **WebDAV** baru.
3. Masukkan host dan **port 8080**, pilih skema `http`, dan tambahkan login Anda jika Anda mengaturnya.

## Sambung dari iPhone atau iPad lain

Aplikasi Files iOS tidak menyertakan klien WebDAV, jadi gunakan salah satu dari ini:

- **Tab Perangkat milik Everdisk.** Di perangkat kedua, buka Everdisk, masuk ke **Perangkat**, ketuk **Koneksi Baru**, pilih **WebDAV**, dan masukkan alamatnya, misalnya `http://192.168.1.20:8080`. Ini rute paling sederhana dan tidak memerlukan apa pun tambahan.
- **Aplikasi WebDAV** seperti Documents by Readdle, yang bisa menambahkan koneksi WebDAV dengan alamat dan login yang sama.

## Lebih suka tautan cepat daripada drive?

Jika Anda hanya perlu mengambil file dengan cepat dan sama sekali tidak ingin memasang drive, aktifkan koneksi **Peramban** di Pengaturan, Berbagi, Koneksi. Everdisk kemudian memberi Anda alamat web yang bisa Anda buka di browser apa pun di perangkat apa pun untuk menjelajah dan mengunduh file Anda. Ini cara tercepat untuk mengoper file ke PC Windows, Chromebook, atau ponsel teman.

## Hanya-baca atau baca dan tulis

Sakelar **Pengeditan Berkas** di Pengaturan, Berbagi, Akses menentukan ini. Aktif berarti komputer yang terhubung bisa mengunggah, mengganti nama, dan menghapus. Mati berarti drive hanya-baca, jadi orang lain bisa melihat dan menyalin file Anda tetapi tidak bisa mengubahnya.

## Cara orang memakainya dalam kehidupan nyata

- **Salin file ke iPhone Anda dari PC Windows** dengan memetakannya sebagai lokasi jaringan dan menyeretnya masuk.
- **Pindahkan foto dan dokumen ke laptop** menggunakan pengelola file yang sudah Anda kenal, tanpa kabel dan tanpa iTunes.
- **Edit dokumen di tempatnya** dari Mac Anda, membukanya langsung dari ponsel dan menyimpannya kembali.
- **Pindahkan folder antara iPhone dan iPad** menggunakan tab Perangkat milik Everdisk di perangkat penerima.

## Beberapa tips

- Biarkan Everdisk tetap terbuka saat sebuah perangkat terhubung. Mengunci ponsel dalam waktu lama bisa menjeda aplikasi.
- Di Windows, jika koneksi gagal, mulai layanan WebClient dan coba alamatnya lagi.
- WebDAV dan SMB keduanya dipasang sebagai network drive. Gunakan WebDAV saat Windows terlibat, dan [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) saat Anda menginginkan kecepatan Finder dan enkripsi.
- Untuk transfer tercepat, jaga kualitas foto dan video pada Original di Pengaturan.

## Pertanyaan yang Sering Diajukan

{{% details title="Berapa alamat dan port WebDAV untuk iPhone saya?" closed="true" %}}
Setelah Anda mulai berbagi, Everdisk menampilkan alamatnya di layar Berbagi. Tampilannya seperti http://192.168.1.20:8080. Angka 8080 adalah port yang dipakai Everdisk untuk WebDAV, dan bagian pertama adalah alamat iPhone Anda di Wi-Fi, jadi milik Anda akan berbeda.
{{% /details %}}

{{% details title="Bagaimana cara menyambung ke WebDAV iPhone dari Windows?" closed="true" %}}
Buka File Explorer, klik kanan This PC, dan pilih Add a network location atau Map network drive. Masukkan alamat WebDAV dari Everdisk, misalnya http://192.168.1.20:8080, lalu masukkan login Anda jika Anda mengaturnya. Jika Windows tidak mau menyambung, pastikan layanan WebClient berjalan (cari Services, temukan WebClient, mulai) lalu coba lagi.
{{% /details %}}

{{% details title="Bisakah saya memakai WebDAV antara dua iPhone?" closed="true" %}}
Ya, tetapi aplikasi Files iOS tidak punya klien WebDAV, jadi gunakan Everdisk di perangkat kedua. Buka tab Perangkat, ketuk Koneksi Baru, pilih WebDAV, dan masukkan alamat yang ditampilkan di ponsel pertama. Aplikasi WebDAV seperti Documents by Readdle juga berfungsi.
{{% /details %}}

{{% details title="Apakah WebDAV memerlukan kata sandi?" closed="true" %}}
Tidak, login bersifat opsional. Biarkan Info Masuk dan Kata Sandi kosong di Pengaturan, Berbagi, Akses untuk akses tamu, atau atur keduanya jika Anda ingin koneksi masuk terlebih dahulu.
{{% /details %}}

{{% details title="Bisakah orang lain mengubah file saya lewat WebDAV?" closed="true" %}}
Hanya jika Anda mengizinkannya. Sakelar Pengeditan Berkas di Pengaturan, Berbagi, Akses mengendalikan ini. Aktif membuat perangkat yang terhubung bisa mengunggah, mengganti nama, dan menghapus. Mati membuat drive hanya-baca, jadi orang lain bisa melihat dan menyalin tetapi tidak bisa mengubah apa pun.
{{% /details %}}

{{% details title="WebDAV atau SMB, apa bedanya?" closed="true" %}}
Keduanya memasang iPhone Anda sebagai network drive. WebDAV berjalan di atas protokol web dan menyambung dengan bersih dari Windows File Explorer, itulah kekuatan utamanya. SMB adalah berbagi file native di perangkat Mac, Linux, dan NAS, biasanya lebih cepat di Mac, dan merupakan satu-satunya koneksi Everdisk yang bisa mengenkripsi transfer. Everdisk bisa menjalankan keduanya sekaligus.
{{% /details %}}

{{% details title="Mengapa drive WebDAV saya terputus?" closed="true" %}}
iPhone Anda adalah server, dan iOS menjeda aplikasi yang terlalu lama berada di latar belakang. Biarkan Everdisk tetap terbuka di layar saat sebuah perangkat terhubung, dan colokkan ke sumber daya untuk transfer yang panjang. Pastikan juga kedua perangkat masih berada di Wi-Fi yang sama.
{{% /details %}}

{{% details title="Bisakah saya menyambung lewat WebDAV tanpa Wi-Fi?" closed="true" %}}
Ya, jika Anda mencolokkan iPhone ke Mac dengan kabel. Everdisk kemudian menampilkan alamat koneksi kabel tambahan yang bisa dibuka Mac yang terhubung di Finder, yang berfungsi bahkan tanpa Wi-Fi sama sekali. Lewat kabel, hanya Mac itu yang bisa menjangkau perangkat.
{{% /details %}}

{{% details title="Apakah Everdisk gratis?" closed="true" %}}
Ya, Everdisk gratis diunduh dan server WebDAV sudah termasuk. Pembelian Premium sekali bayar opsional menambahkan ekstra seperti port kustom serta konversi foto dan video. Anda bisa menyiapkan WebDAV dan berbagi file tanpa membayar.
{{% /details %}}

Siap mencobanya? [Unduh Everdisk dari App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dan pasang iPhone Anda sebagai drive dalam beberapa menit. Ada pertanyaan atau masukan? Kirim email ke **support@everappz.com**.
</content>
