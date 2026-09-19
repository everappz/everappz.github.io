---
title: "Sambung ke Pelayan"
date: 2026-08-20
description: "Gunakan tab Peranti dalam Everdisk untuk menyambung ke pelayan lain pada rangkaian anda. Tambah dan layari pelayan DLNA, WebDAV, FTP, SFTP dan SMB serta pemacu NAS, strim audio dan video, muat turun fail, serta cipta, muat naik, namakan semula, alih atau padam pada pelayan yang membenarkannya."
keywords: ["tab Peranti Everdisk", "sambung ke NAS", "klien DLNA iPhone", "klien WebDAV iPhone", "klien FTP iPhone", "klien SFTP iPhone", "klien SMB iPhone", "sambung ke kongsi SMB", "layari pelayan rangkaian", "strim dari NAS", "muat turun dari pelayan", "sambung awan WebDAV"]
tags: ["everdisk", "panduan", "peranti", "sambungan"]
readingTime: 9
---


Everdisk bukan sekadar pemacu tanpa wayar - ia juga merupakan klien untuk peranti lain pada rangkaian anda. Tab **Peranti** membolehkan anda menyambung ke pelayan **DLNA**, **WebDAV**, **FTP**, **SFTP** dan **SMB**, termasuk Mac, PC Windows, mesin Linux, pemacu NAS dan pelayan media, lalu melayari, menstrim dan memuat turun fail mereka.

## Skrin Peranti

Tab Peranti mempunyai dua bahagian:

- **Sambungan** - pelayan yang telah anda simpan.
- **Peranti yang tersedia** - pelayan yang ditemui Everdisk secara automatik pada rangkaian tempatan anda.

Untuk menyambung ke sesuatu yang telah pun ditemui Everdisk, cuma ketik ia dalam **Peranti yang tersedia**. Untuk menambah pelayan secara manual, ketik butang **tambah (+)** atau **Sambungan Baharu**.

## Tambah sambungan baharu

Ketik **Sambungan Baharu** dan pilih jenis pelayan yang ingin anda capai:

- **DLNA / UPnP** - terbaik untuk pelayan media. Strim video, muzik dan foto daripada pustaka media, pemacu storan rangkaian serta TV dan komputer yang berkeupayaan DLNA. DLNA adalah baca sahaja: anda boleh melayari, menstrim dan memuat turun, tetapi tidak boleh memuat naik atau mengubah fail.
- **WebDAV** - sambung ke pelayan fail, pemacu storan rangkaian, dan pemacu awan yang menyokong WebDAV. Baca dan tulis apabila pelayan membenarkannya.
- **FTP** - lazim pada penghala, pemacu storan rangkaian dan pengehosan web. Port lalai ialah 21 (990 untuk FTPS selamat); anda boleh menetapkan port tersuai dalam alamat, contohnya `ftp://host:2121`. Biarkan log masuk dan kata laluan kosong untuk akses tanpa nama.
- **SFTP** - sambung secara selamat menerusi SSH. Port lalai ialah 22; guna port tersuai dalam alamat jika perlu, contohnya `sftp://host:2222`.
- **SMB** - sambung ke Mac, PC Windows, pelayan Linux dan storan rangkaian (NAS) yang berkongsi folder melalui **SMB / CIFS**. Masukkan alamat seperti `smb://server-address/share-name/` (contoh: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB menambah dua medan pilihan: nama **Kumpulan kerja**, dan **Versi protokol** yang boleh anda biarkan pada **Automatik** atau paksa kepada **SMB1** atau **SMB2**. Jika fail atau folder dengan aksara khas tidak mahu dibuka, cuba tukar versi kepada **SMB1**.

> Everdisk hanya menyambung ke protokol rangkaian tempatan dan yang dialamatkan secara langsung ini. Ia tidak log masuk ke akaun awan seperti Google Drive atau Dropbox. Sesuatu pemacu awan hanya boleh dicapai jika perkhidmatan itu menawarkan alamat **WebDAV** yang boleh anda taip masuk.

## Masukkan alamat dan log masuk

Pada penyunting sambungan, isikan:

- **Tajuk** - nama mesra untuk sambungan itu.
- **URL / alamat** - alamat pelayan (contoh dipaparkan untuk setiap jenis).
- **Log masuk** dan **Kata laluan** - biarkan kedua-duanya kosong jika pelayan membenarkan akses tanpa nama.

Untuk WebDAV, anda boleh membenarkan sijil tidak sah jika pelayan anda menggunakan sijil tandatangan sendiri. Jika identiti pelayan selamat tidak dapat disahkan, Everdisk akan meminta anda mengesahkannya sebelum mempercayainya.

Pengguna percuma boleh menyimpan sehingga **10** sambungan. Premium menghapuskan had itu.

## Layari, strim dan muat turun

Sebaik sahaja bersambung, ketik pelayan itu untuk membukanya:

- **Layari** folder dalam senarai atau grid, susun ia, dan lihat lakaran kenit. Pelayan DLNA turut memaparkan butiran muzik dan seni album.
- **Strim** audio dan video. Audio pergi ke baris gilir pemain mini; video dimainkan skrin penuh. Pencarian berfungsi semasa fail sedang distrim.
- **Muat turun** fail ke peranti anda. Pilih beberapa sekali gus untuk muat turun berkelompok. Muat turun akan muncul dalam **Pemindahan Fail** dan mendarat dalam folder **Dokumen** anda.
- **Maklumat** pada mana-mana item menunjukkan jenis, saiz, tarikh, laluan dan butiran medianya.

## Ubah fail pada pelayan

Pada pelayan yang membenarkan penulisan - **WebDAV, FTP, SFTP dan SMB** - anda juga boleh mengurus fail:

- **Folder Baharu**
- **Muat Naik Fail** daripada peranti anda
- **Namakan Semula**, **Alih** dan **Padam** (satu item atau beberapa sekali gus)

Pelayan **DLNA** adalah baca sahaja, jadi tindakan ini tidak tersedia di sana.

## Jejaki pemindahan anda

Muat turun dan muat naik berjalan di latar belakang dan muncul dalam **Pemindahan Fail**, yang anda buka dari bahagian kiri atas tab **Dokumen**. Di sana anda boleh memerhati kemajuan, serta menjeda, menyambung semula, mencuba semula, membatal atau mengosongkan tugasan. Anda juga boleh melaraskan pemindahan dalam [Tetapan -> Rangkaian](/docs/guide/everdisk/everdisk-guide-settings) (Wi-Fi sahaja lawan Wi-Fi dan selular, berapa banyak berjalan serentak, dan sama ada ia diteruskan di latar belakang).

## Langkah seterusnya

- [Fail & Dokumen](/docs/guide/everdisk/everdisk-guide-files) - urus segala yang anda muat turun.
- [Foto, Muzik & Video](/docs/guide/everdisk/everdisk-guide-media) - mainkan apa yang anda strim.
- [Tetapan](/docs/guide/everdisk/everdisk-guide-settings) - had sambungan dan pilihan pemindahan.
