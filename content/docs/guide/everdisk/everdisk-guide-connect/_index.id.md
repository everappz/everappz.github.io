---
title: "Hubungkan Perangkat Anda"
date: 2026-08-20
description: "Petunjuk langkah demi langkah untuk terhubung ke drive nirkabel Everdisk Anda: tonton di smart TV lewat DLNA, buka file Anda di peramban web mana pun, pasang perangkat Anda sebagai network drive di Finder, Windows, atau Linux lewat WebDAV atau SMB (dengan enkripsi SMB3/AES opsional), hubungkan aplikasi file lewat FTP, dan transfer lewat kabel USB ke Mac tanpa Wi-Fi."
keywords: ["hubungkan ke Everdisk", "streaming ke TV DLNA", "buka file di peramban", "pasang network drive Finder", "WebDAV Windows Linux", "aplikasi file FTP", "transfer kabel USB Mac", "hubungkan iPhone ke komputer", "network drive iPhone"]
tags: ["everdisk", "panduan", "hubungkan"]
readingTime: 11
---


Setelah Anda mengetuk **Mulai** di layar [Berbagi](/docs/guide/everdisk/everdisk-guide-sharing), perangkat lain bisa terhubung ke file Anda dengan lima cara berbeda. Pilih metode yang sesuai dengan perangkat yang ingin Anda gunakan. Dalam setiap kasus, **alamat** persis yang Anda butuhkan ditampilkan di bagian **Cara Terhubung** pada layar Berbagi.

> Kedua perangkat harus berada di **jaringan Wi-Fi yang sama** - atau, untuk Mac, terhubung dengan **kabel USB** (lihat bagian terakhir).

## Menonton di TV (DLNA)

Gunakan ini untuk menampilkan foto, video, dan musik di smart TV atau media player.

1. Di **Pengaturan → Berbagi → Koneksi**, pastikan **TV & Pusat Media** aktif (aktif secara default).
2. Di layar Berbagi, ketuk **Mulai**.
3. Di TV Anda, buka media player bawaannya atau aplikasi media server (mungkin bernama Media Player, SmartShare, AllShare, atau semacamnya).
4. Perangkat Anda muncul dalam daftar media server dengan namanya (misalnya "Speedy-Hare"). Pilih perangkat itu.
5. Telusuri foto, video, dan musik yang Anda bagikan lalu mulai memutar. Thumbnail pratinjau muncul secara otomatis.

Catatan:

- DLNA tidak bisa dilindungi kata sandi, jadi koneksi ini terbuka untuk siapa saja di Wi-Fi yang sama selama aktif.
- Jika sebuah video tidak mau diputar di TV lama, turunkan kualitas video di **Pengaturan → Berbagi → Video** agar Everdisk mengonversinya ke format yang lebih kompatibel.

## Membuka di peramban web (HTTP)

Gunakan ini untuk memberikan file kepada siapa pun yang punya peramban web - tanpa aplikasi yang perlu diinstal.

1. Di **Pengaturan → Berbagi → Koneksi**, pastikan **Peramban** aktif.
2. Ketuk **Mulai**.
3. Di layar Berbagi, salin alamat **Peramban** (atau tampilkan kode QR-nya).
4. Di ponsel, tablet, atau komputer lain, buka peramban web apa pun (Safari, Chrome, Edge, Firefox) dan ketik alamat tersebut.
5. Halaman terbuka menampilkan file yang Anda bagikan.

Di peramban, orang lain bisa:

- Beralih antara tampilan **daftar** dan **kisi** serta mengurutkan berdasarkan nama, tanggal, atau ukuran.
- Melihat **thumbnail** asli untuk foto, video, PDF, dan sampul musik.
- Membuka foto ke **galeri** layar penuh dengan geser, cubit untuk memperbesar, dan slideshow.
- Memutar musik di **pemutar** bawaan dengan antrean, acak, dan ulang.
- **Mengunduh** file mana pun, atau mengunduh seluruh folder (atau beberapa item terpilih) sebagai satu **Archive.zip**.
- **Mengunggah** file kembali ke perangkat Anda - hanya jika Anda mengaktifkan **Pengeditan File** (lihat [Akses & Privasi](/docs/guide/everdisk/everdisk-guide-access)).

## Menggunakannya sebagai network drive (WebDAV)

Gunakan ini agar perangkat Anda muncul sebagai disk biasa di Mac, PC Windows, atau mesin Linux, sehingga Anda bisa menyeret file ke dua arah.

**Di Mac (Finder)**

1. Di **Pengaturan → Berbagi → Koneksi**, pastikan **Komputer** aktif.
2. Ketuk **Mulai** dan catat alamat **Komputer (WebDAV)**.
3. Di Finder, pilih **Go → Connect to Server** (atau tekan **⌘K**).
4. Ketik alamat WebDAV persis seperti yang ditampilkan lalu klik **Connect**.
5. Masukkan login dan kata sandi jika Anda mengaturnya, atau terhubung sebagai tamu.
6. Perangkat Anda terbuka seperti network drive lainnya. Seret file masuk atau keluar.

**Di Windows**

1. Buka **File Explorer**, klik kanan **This PC**, lalu pilih **Add a network location** (atau petakan network drive).
2. Masukkan alamat WebDAV yang ditampilkan di Everdisk.
3. Masukkan login dan kata sandi jika Anda mengaturnya.

**Di Linux**

1. Buka pengelola file Anda lalu pilih **Connect to Server** (atau gunakan `davs://` / `dav://`).
2. Masukkan alamat WebDAV yang ditampilkan di Everdisk.

Apakah koneksinya hanya-baca atau dua arah tergantung pada pengaturan **Pengeditan File**. Jika diaktifkan, Anda bisa menyalin file ke perangkat Anda serta mengganti nama atau menghapusnya; jika dimatikan, drive bersifat hanya-baca.

## Terhubung lewat SMB (network drive terenkripsi)

SMB adalah network drive untuk Mac, Windows, dan Linux, dibangun di atas berbagi file yang sudah ada di sistem tersebut, sehingga perangkat Anda muncul sebagai network drive biasa - dan ini satu-satunya koneksi yang bisa Anda enkripsi.

1. Di **Pengaturan → Berbagi → Koneksi**, pastikan **Komputer (Lanjutan)** (koneksi SMB) aktif.
2. Ketuk **Mulai** dan catat alamat **SMB**, yang tampak seperti `smb://192.168.1.20:4455/Share`.
3. Terhubung dari komputer Anda:
   - **Mac:** perangkat Anda muncul dengan sendirinya di **bilah samping Finder** di bawah **Locations** (Network) - cukup klik dan masuk. Untuk terhubung secara manual, pilih **Go → Connect to Server** (**⌘K**) dan masukkan alamatnya.
   - **Windows:** buka **File Explorer**, klik kanan **This PC** lalu pilih **Map network drive**, lalu masukkan `\\<address>\Share` menggunakan host dan nama share dari layar Berbagi (atau ketik alamat `smb://` di bilah alamat).
   - **Linux:** di pengelola file Anda pilih **Connect to Server** dan masukkan alamatnya.
4. Masukkan login dan kata sandi jika Anda mengaturnya, atau terhubung sebagai tamu.
5. Share tersebut bernama **Share**. Dengan **Pengeditan File** aktif, Anda bisa menyalin file ke dua arah; jika dimatikan, drive bersifat hanya-baca.

**Aktifkan enkripsi (disarankan di Wi-Fi yang tidak tepercaya)**

SMB adalah satu-satunya koneksi Everdisk yang bisa dienkripsi. Untuk melindungi setiap transfer dengan **enkripsi SMB3 (AES)**:

1. Di **Pengaturan → Berbagi → Akses**, atur **Info Masuk** dan **Kata Sandi** - koneksi terenkripsi tidak bisa anonim.
2. Di **Pengaturan → Berbagi**, aktifkan **Wajibkan enkripsi SMB**.
3. **Hentikan lalu Mulai** berbagi lagi agar perubahannya berlaku.

Klien Anda harus mendukung SMB3 - Finder di Mac modern, atau **Windows 10 dan yang lebih baru**. Enkripsi SMB adalah fitur Premium.

## Menghubungkan aplikasi file (FTP)

Gunakan ini untuk aplikasi pengelola file dan transfer yang memakai FTP (misalnya FileZilla atau Cyberduck di komputer).

1. Di **Pengaturan → Berbagi → Koneksi**, pastikan **Aplikasi & Perangkat Lain** aktif.
2. Ketuk **Mulai** dan catat alamat **FTP**.
3. Di aplikasi FTP Anda, tambahkan koneksi baru menggunakan alamat tersebut.
4. Masukkan login dan kata sandi jika Anda mengaturnya, atau biarkan kosong untuk akses anonim.

## Transfer lewat kabel USB (Mac, tanpa perlu Wi-Fi)

Gunakan ini saat tidak ada Wi-Fi, atau saat Anda ingin transfer tercepat dan paling privat. Cara ini hanya bekerja dengan **Mac**.

1. Hubungkan iPhone atau iPad Anda ke Mac dengan kabel pengisi daya biasa.
2. Jika diminta di perangkat, ketuk **Trust This Computer**.
3. Di Everdisk, ketuk **Mulai**. Muncul catatan **Koneksi Cepat Tersedia** dan layar Berbagi menampilkan alamat tambahan berlabel **Koneksi Kabel** yang berakhiran `.local`.
4. Di Mac, buka Finder → **Go → Connect to Server** (**⌘K**) dan masukkan alamat `.local` tersebut (alamat ini bekerja untuk koneksi Peramban maupun Komputer).
5. Perangkat Anda terbuka lewat kabel - lebih cepat daripada Wi-Fi, dan datanya tidak pernah menyentuh router atau internet.

Catatan:

- Gunakan **nama `.local`**, bukan alamat IP (alamat IP hanya bekerja lewat Wi-Fi), dan jangan pernah `localhost`.
- Jalur kabel **hanya untuk Mac**. PC Windows dan perangkat Android harus memakai Wi-Fi.
- Anda juga bisa menyeret file ke folder Everdisk menggunakan Finder di Mac, atau aplikasi Apple Devices (atau iTunes) di Windows, melalui berbagi file iOS standar.

## Langkah selanjutnya

- [Akses & Privasi](/docs/guide/everdisk/everdisk-guide-access) - tambahkan kata sandi, izinkan unggahan, blokir perangkat.
- [Foto, Musik & Video](/docs/guide/everdisk/everdisk-guide-media) - bagikan seluruh pustaka Anda dan atur kualitas.
- [Terhubung ke Server](/docs/guide/everdisk/everdisk-guide-devices) - akses perangkat lain dari Everdisk.
