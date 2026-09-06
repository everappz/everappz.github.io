---
title: "Akses & Privasi"
date: 2026-08-20
description: "Jaga keamanan berbagi Everdisk Anda: lindungi akses dengan login dan kata sandi, atur apakah perangkat yang terhubung boleh mengunggah, mengganti nama, dan menghapus dengan Pengeditan File, blokir perangkat asing, pilih tempat sampah vs. hapus permanen, dan pahami mengapa semuanya tetap berada di jaringan lokal Anda."
keywords: ["proteksi kata sandi Everdisk", "sakelar pengeditan file", "blokir perangkat", "perangkat yang diblokir", "hapus file permanen", "hanya jaringan lokal", "berbagi file privat", "DLNA tanpa kata sandi", "keamanan jaringan"]
tags: ["everdisk", "panduan", "akses", "privasi", "keamanan"]
readingTime: 8
---


Everdisk menyimpan file Anda di jaringan Anda sendiri dan memberi Anda kontrol sederhana atas siapa yang bisa mengaksesnya dan apa yang bisa mereka lakukan. Anda menemukan kontrol ini di **Pengaturan → Berbagi → Akses**, ditambah beberapa pengaturan terkait di Pengelola File.

## Melindungi akses dengan login dan kata sandi

Secara default, siapa pun di jaringan yang sama yang memiliki alamat Anda bisa membuka file yang Anda bagikan. Untuk mewajibkan masuk:

1. Buka **Pengaturan → Berbagi → Akses**.
2. Masukkan **Login** dan **Kata Sandi**.
3. Kini koneksi **Peramban (HTTP)**, **Komputer (WebDAV)**, dan **Aplikasi & Perangkat Lain (FTP)** semuanya meminta detail tersebut sebelum menampilkan file Anda.

Biarkan kedua kolom kosong untuk akses terbuka. Kata sandi Anda disimpan dengan aman di Keychain perangkat.

> **DLNA selalu terbuka.** Koneksi TV & Pusat Media (DLNA) tidak bisa dilindungi kata sandi, jadi begitu aktif, perangkat mana pun di Wi-Fi yang sama bisa menelusuri media yang Anda bagikan. Matikan jika Anda hanya menginginkan koneksi yang terlindungi, dan hanya berbagi di jaringan yang Anda percayai.

## Mengizinkan atau memblokir pengeditan (Pengeditan File)

Sakelar **Pengeditan File** mengatur apakah perangkat yang terhubung hanya bisa melihat file Anda, atau juga mengubahnya.

- **Aktif** (default): perangkat yang terhubung bisa **mengunggah, mengganti nama, dan menghapus** file yang Anda bagikan - jadi perangkat Anda bekerja seperti network drive dua arah sungguhan.
- **Nonaktif**: file yang Anda bagikan bersifat **hanya-baca**. Orang lain bisa melihat dan mengunduh, tetapi tidak bisa menambah atau mengubah apa pun.

Mengaktifkannya menampilkan peringatan singkat karena hal ini membuat orang lain bisa memodifikasi file Anda. Fitur ini membawa lencana **Penting** selama aktif.

## Memblokir perangkat

Jika Anda melihat perangkat yang tidak Anda kenali:

1. Di layar Berbagi, temukan perangkat itu di bawah **Siapa yang Terhubung**.
2. Ketuk tombol tindakan lainnya lalu pilih **Blokir perangkat ini**.

Perangkat yang diblokir tercantum di **Pengaturan → Berbagi → Akses → Perangkat yang Diblokir**, tempat Anda bisa **membuka blokir** satu perangkat atau **Buka Blokir Semua**. Pemblokiran mengikuti perangkat bahkan jika alamat jaringannya berubah (untuk koneksi Peramban, Komputer, dan TV).

## Tempat sampah vs. hapus permanen

Saat sebuah file dihapus - oleh Anda di pengelola file, atau oleh perangkat yang terhubung - file itu biasanya masuk ke **tempat sampah** yang bisa dipulihkan sehingga Anda bisa mengambilnya kembali.

Jika Anda lebih suka file langsung dibuang tanpa pemulihan, aktifkan **Hapus File Secara Permanen** di **Pengaturan → Pengelola File → Menghapus File**. Ini nonaktif secara default. **Pengaturan ini memengaruhi pengelola file di perangkat** dan **penghapusan yang dilakukan lewat jaringan**; pengaturan ini tidak mengubah cara pustaka Foto sistem atau pustaka Musik menangani penghapusan.

## Semuanya tetap lokal

Everdisk hanya berbagi lewat **jaringan lokal** Anda - tidak ada yang diunggah ke internet dan tidak ada akun cloud di tengahnya. Beberapa hal yang perlu diketahui:

- Everdisk memerlukan izin **Jaringan Lokal** iOS agar perangkat di sekitar bisa menemukannya. Jika izin itu nonaktif, sebuah catatan menjelaskan cara menyalakannya kembali di aplikasi Pengaturan iOS.
- Untuk privasi maksimal, hanya berbagi saat Anda berada di jaringan **Wi-Fi rumah atau privat** yang Anda percayai, dan berhati-hatilah di Wi-Fi publik. Login dan kata sandi membantu, tetapi bukan pengganti jaringan yang tepercaya.
- **Opsi paling privat dari semuanya adalah kabel USB ke Mac** - datanya mengalir langsung lewat kabel dan tidak pernah menyentuh router atau internet. Lihat [Hubungkan Perangkat Anda](/docs/guide/everdisk/everdisk-guide-connect).

## Langkah selanjutnya

- [Berbagi](/docs/guide/everdisk/everdisk-guide-sharing) - pilih apa yang dibagikan dan mulai berbagi.
- [Pengaturan](/docs/guide/everdisk/everdisk-guide-settings) - semua pengaturan Akses dan Pengelola File di satu tempat.
