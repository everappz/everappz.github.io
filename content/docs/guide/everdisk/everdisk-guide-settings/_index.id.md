---
title: "Pengaturan"
date: 2026-08-20
description: "Panduan lengkap pengaturan Everdisk: profil perangkat (nama dan avatar), kelima server koneksi, kontrol akses, enkripsi SMB (SMB3/AES), kualitas foto dan video, port khusus, thumbnail DLNA, opsi jaringan dan transfer, opsi pengelola file, dan Premium."
keywords: ["pengaturan Everdisk", "nama avatar perangkat", "server koneksi", "kualitas foto video", "port khusus HTTP WebDAV FTP", "thumbnail DLNA", "transfer paralel", "hapus file permanen", "cache thumbnail", "Everdisk Premium"]
tags: ["everdisk", "panduan", "pengaturan"]
readingTime: 12
---


Tab **Pengaturan** mengelompokkan semuanya ke dalam tiga area utama - **Berbagi**, **Jaringan**, dan **Pengelola File** - ditambah Premium, umpan balik, dan tautan legal. Halaman ini menjelaskan setiap pengaturan beserta nilai default-nya.

## Premium

Di bagian atas Pengaturan Anda melihat status Premium Anda, atau tombol **Buka semua fitur**. Everdisk gratis digunakan dengan beberapa batasan; pembelian **Premium Seumur Hidup** sekali bayar menghilangkannya. Lihat [Premium](#premium-lifetime) di akhir halaman ini.

## Pengaturan Berbagi

### Umum

- **Mulai berbagi perangkat secara otomatis** - mulai berbagi begitu Anda membuka aplikasi. *(Premium.)*
- **Bagikan Folder Dokumen** - bagikan folder Dokumen milik aplikasi. Aktif secara default.
- **Beri tahu sebelum terputus** - mengingatkan Anda untuk membuka kembali aplikasi sebelum sistem menangguhkannya di latar belakang. Nonaktif secara default; meminta izin notifikasi pada kali pertama.

### Profil Perangkat

- **Nama Perangkat** - nama yang dilihat perangkat lain untuk Anda di jaringan. Ketuk untuk mengedit. *(Premium.)*
- **Avatar Perangkat** - ikon dan warna latar untuk perangkat Anda. Anda bisa memilih ikon, gradien latar, atau **memilih avatar dari Foto**. *(Premium.)*
- **Buat Ulang Nama & Avatar** dan **Buat Ulang Avatar** - dapatkan nama dan/atau avatar acak baru. *(Gratis.)*

### Akses

- **Info Masuk** dan **Kata Sandi** - wajibkan masuk untuk koneksi Peramban, Komputer, dan Aplikasi Lain.
- **Pengeditan File** - izinkan perangkat yang terhubung mengunggah, mengganti nama, dan menghapus. Aktif secara default.
- **Perangkat yang Diblokir** - kelola perangkat yang telah Anda blokir.

Lihat [Akses & Privasi](/docs/guide/everdisk/everdisk-guide-access) untuk detailnya.

### Koneksi

Nyalakan atau matikan tiap server. Kelimanya aktif secara default, dan masing-masing punya tombol info (ⓘ) dengan petunjuk koneksi:

- **TV & Pusat Media** (DLNA)
- **Peramban** (HTTP)
- **Komputer** (WebDAV)
- **Komputer (Lanjutan)** (SMB) - network drive untuk Mac, Windows, dan Linux; di Mac muncul dengan sendirinya di bilah samping Finder. Satu-satunya koneksi yang bisa dienkripsi.
- **Aplikasi & Perangkat Lain** (FTP)

### Foto

- **Format** - Asli atau Paling Kompatibel (JPEG).
- **Kualitas** - Asli, Tinggi, Sedang, atau Rendah.

Pengaturan apa pun selain Asli mengonversi foto saat dibagikan, yang lebih lambat. Konversi adalah fitur Premium.

### Video

- **Format** - Asli atau Paling Kompatibel (H.264 MP4).
- **Kualitas** - Asli, Tinggi, Sedang, atau Rendah.

Idenya sama seperti Foto: Asli paling cepat, dan konversi bersifat Premium. Turunkan kualitas jika TV lama tidak bisa memutar sebuah video.

### Lanjutan

- **Port HTTP** (default 80), **Port WebDAV** (default 8080), **Port SMB** (default 4455), **Port FTP** (default 2121). DLNA memilih port-nya secara otomatis. *(Mengubah port bersifat Premium; pengguna gratis bisa melihat nilainya.)*

### Enkripsi SMB

- **Wajibkan enkripsi SMB** - enkripsi setiap transfer SMB dengan **enkripsi SMB3 (AES)** sehingga tidak ada orang lain di jaringan yang bisa membaca file Anda. Nonaktif secara default. Ini memerlukan **login dan kata sandi** yang diatur di atas (koneksi terenkripsi tidak bisa anonim) dan klien yang mendukung SMB3, seperti Finder di Mac modern atau Windows 10 dan yang lebih baru. Perubahan berlaku saat Anda mulai berbagi berikutnya. *(Premium.)*

### Thumbnail DLNA

- **Tampilkan Thumbnail** - publikasikan gambar pratinjau untuk TV. Aktif secara default (gratis).
- Pilih ukuran mana yang dipublikasikan: **Kecil (160px)**, **Sedang (640px)**, **Besar (1024px)**, **Sangat Besar (4096px)**.

## Pengaturan Jaringan

- **Transfer File** - gunakan **Wi-Fi** saja, atau **Wi-Fi & Data Seluler**, untuk unduhan dan unggahan. Default Wi-Fi.
- **Batas Transfer Paralel** - berapa banyak transfer yang berjalan sekaligus. Default 5.
- **Transfer Latar Belakang** - biarkan transfer terus berjalan saat Anda memakai layar lain. Aktif secara default.
- **Thumbnail untuk File** - apakah mengambil thumbnail untuk file di perangkat lain lewat Wi-Fi saja atau juga seluler. Default Wi-Fi.

## Pengaturan Pengelola File

- **Hapus File Secara Permanen** - hapus langsung tanpa tempat sampah. Nonaktif secara default. Lihat [Akses & Privasi](/docs/guide/everdisk/everdisk-guide-access).
- **Atur Ulang Semua Pesan Pemberitahuan** - munculkan kembali banner tip yang telah Anda tutup.
- **Cache Thumbnail** - lihat berapa banyak ruang yang dipakai thumbnail dalam cache, dan **Bersihkan Cache Thumbnail**.

## Umpan balik dan legal

Di bagian bawah Anda bisa **Beri Nilai Aplikasi Ini**, **Kirim Umpan Balik**, **Dapatkan Aplikasi Lainnya**, serta membuka **Syarat dan Ketentuan** dan **Kebijakan Privasi**.

## Premium Lifetime

Everdisk gratis digunakan. Satu pembelian **Premium Seumur Hidup** - pembayaran sekali, bukan langganan - membuka:

- **Folder Tanpa Batas** - bagikan lebih dari 5 folder.
- **Koneksi Tanpa Batas** - simpan lebih dari 10 server di tab Perangkat.
- **Konversi Foto & Video** - bagikan dalam kualitas apa pun selain Asli.
- **Enkripsi SMB** - lindungi transfer SMB dengan enkripsi SMB3 (AES).
- **Port Khusus** - atur sendiri port HTTP, WebDAV, SMB, dan FTP Anda.
- **Berbagi Otomatis** - mulai berbagi otomatis saat Anda membuka aplikasi.
- **Kustomisasi Perangkat** - nama perangkat khusus, ikon avatar, gradien latar, atau avatar foto.

Premium terikat pada Apple ID Anda. Gunakan **Pulihkan Pembelian** untuk membukanya di perangkat lain Anda yang masuk dengan Apple ID yang sama.

## Langkah selanjutnya

- [Berbagi](/docs/guide/everdisk/everdisk-guide-sharing) - layar Berbagi secara terperinci.
- [Akses & Privasi](/docs/guide/everdisk/everdisk-guide-access) - kata sandi, pengeditan, dan pemblokiran.
- [FAQ](/docs/faq/everdisk) - jawaban cepat untuk pertanyaan umum.
