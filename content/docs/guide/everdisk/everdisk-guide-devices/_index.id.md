---
title: "Terhubung ke Server"
date: 2026-08-20
description: "Gunakan tab Perangkat di Everdisk untuk terhubung ke server lain di jaringan Anda. Tambahkan dan telusuri server DLNA, WebDAV, FTP, SFTP, dan SMB serta drive NAS, streaming audio dan video, unduh file, dan buat, unggah, ganti nama, pindahkan, atau hapus di server yang mengizinkannya."
keywords: ["tab Perangkat Everdisk", "hubungkan ke NAS", "klien DLNA iPhone", "klien WebDAV iPhone", "klien FTP iPhone", "klien SFTP iPhone", "klien SMB iPhone", "sambung ke share SMB", "telusuri server jaringan", "streaming dari NAS", "unduh dari server", "hubungkan cloud WebDAV"]
tags: ["everdisk", "panduan", "perangkat", "koneksi"]
readingTime: 9
---


Everdisk bukan sekadar drive nirkabel - aplikasi ini juga menjadi klien bagi perangkat lain di jaringan Anda. Tab **Perangkat** memungkinkan Anda terhubung ke server **DLNA**, **WebDAV**, **FTP**, **SFTP**, dan **SMB**, termasuk Mac, PC Windows, mesin Linux, drive NAS, dan media server, lalu menelusuri, streaming, dan mengunduh file mereka.

## Layar Perangkat

Tab Perangkat memiliki dua bagian:

- **Koneksi** - server yang sudah Anda simpan.
- **Perangkat yang Tersedia** - server yang ditemukan Everdisk secara otomatis di jaringan lokal Anda.

Untuk terhubung ke sesuatu yang sudah ditemukan Everdisk, cukup ketuk di **Perangkat yang Tersedia**. Untuk menambahkan server secara manual, ketuk tombol **plus (+)** atau **Koneksi Baru**.

## Menambahkan koneksi baru

Ketuk **Koneksi Baru** lalu pilih jenis server yang ingin Anda akses:

- **DLNA / UPnP** - paling cocok untuk media server. Streaming video, musik, dan foto dari pustaka media, drive penyimpanan jaringan, serta TV dan komputer yang mendukung DLNA. DLNA bersifat hanya-baca: Anda bisa menelusuri, streaming, dan mengunduh, tetapi tidak bisa mengunggah atau mengubah file.
- **WebDAV** - terhubung ke server file, drive penyimpanan jaringan, dan cloud drive yang mendukung WebDAV. Bisa baca dan tulis jika server mengizinkan.
- **FTP** - umum ada di router, drive penyimpanan jaringan, dan web hosting. Port default-nya 21 (990 untuk FTPS yang aman); Anda bisa mengatur port khusus dalam alamat, misalnya `ftp://host:2121`. Biarkan login dan kata sandi kosong untuk akses anonim.
- **SFTP** - terhubung secara aman melalui SSH. Port default-nya 22; gunakan port khusus dalam alamat jika perlu, misalnya `sftp://host:2222`.
- **SMB** - sambungkan ke Mac, PC Windows, server Linux, dan penyimpanan jaringan (NAS) yang berbagi folder melalui **SMB / CIFS**. Masukkan alamat seperti `smb://server-address/share-name/` (contoh: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB menambahkan dua kolom opsional: nama **Workgroup**, dan **Versi protokol** yang bisa Anda biarkan pada **Otomatis** atau paksa ke **SMB1** atau **SMB2**. Jika file atau folder dengan karakter khusus tidak mau terbuka, coba ganti versinya ke **SMB1**.

> Everdisk hanya terhubung ke protokol jaringan lokal dan yang dialamatkan secara langsung ini. Aplikasi ini tidak masuk ke akun cloud seperti Google Drive atau Dropbox. Sebuah cloud drive hanya bisa diakses jika layanan tersebut menyediakan alamat **WebDAV** yang bisa Anda ketik.

## Memasukkan alamat dan masuk

Di editor koneksi, isi:

- **Judul** - nama yang mudah dikenali untuk koneksi.
- **URL / alamat** - alamat server (contoh ditampilkan untuk tiap jenis).
- **Info Masuk** dan **Kata Sandi** - biarkan keduanya kosong jika server mengizinkan akses anonim.

Untuk WebDAV, Anda bisa mengizinkan sertifikat yang tidak valid jika server Anda memakai sertifikat yang ditandatangani sendiri. Jika identitas server yang aman tidak bisa diverifikasi, Everdisk meminta Anda mengonfirmasi sebelum mempercayainya.

Pengguna gratis bisa menyimpan hingga **10** koneksi. Premium menghilangkan batasan ini.

## Menelusuri, streaming, dan mengunduh

Setelah terhubung, ketuk server untuk membukanya:

- **Telusuri** folder dalam tampilan daftar atau kisi, urutkan, dan lihat thumbnail. Server DLNA juga menampilkan detail musik dan sampul.
- **Streaming** audio dan video. Audio masuk ke antrean mini player; video diputar layar penuh. Pencarian posisi tetap bekerja saat file di-streaming.
- **Unduh** file ke perangkat Anda. Pilih beberapa sekaligus untuk unduhan massal. Unduhan muncul di **Transfer File** dan tersimpan di folder **Dokumen** Anda.
- **Info** pada item mana pun menampilkan jenis, ukuran, tanggal, jalur, dan detail medianya.

## Mengubah file di server

Pada server yang mengizinkan penulisan - **WebDAV, FTP, SFTP, dan SMB** - Anda juga bisa mengelola file:

- **Folder Baru**
- **Unggah File** dari perangkat Anda
- **Ganti Nama**, **Pindahkan**, dan **Hapus** (satu item atau beberapa sekaligus)

Server **DLNA** bersifat hanya-baca, jadi tindakan ini tidak tersedia di sana.

## Melacak transfer Anda

Unduhan dan unggahan berjalan di latar belakang dan muncul di **Transfer File**, yang Anda buka dari pojok kiri atas tab **Dokumen**. Di sana Anda bisa memantau progres, serta menjeda, melanjutkan, mencoba lagi, membatalkan, atau membersihkan tugas. Anda juga bisa menyetel transfer di [Pengaturan → Jaringan](/docs/guide/everdisk/everdisk-guide-settings) (hanya Wi-Fi vs. Wi-Fi dan seluler, berapa banyak yang berjalan sekaligus, dan apakah lanjut di latar belakang).

## Langkah selanjutnya

- [File & Dokumen](/docs/guide/everdisk/everdisk-guide-files) - kelola semua yang Anda unduh.
- [Foto, Musik & Video](/docs/guide/everdisk/everdisk-guide-media) - putar apa yang Anda streaming.
- [Pengaturan](/docs/guide/everdisk/everdisk-guide-settings) - batas koneksi dan opsi transfer.
