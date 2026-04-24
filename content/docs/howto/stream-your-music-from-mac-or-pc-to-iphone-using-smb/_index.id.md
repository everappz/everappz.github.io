---
title: "Stream Musik dari Mac atau PC ke iPhone Menggunakan SMB"
description: "Pelajari cara streaming koleksi musik Anda dari Mac atau Windows PC ke iPhone atau iPad menggunakan Evermusic dan protokol SMB. Panduan langkah demi langkah sederhana untuk menghubungkan dan menikmati audio tanpa sinkronisasi."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["streaming musik dari Mac ke iPhone", "SMB audio streaming iOS", "pengaturan Evermusic SMB", "menghubungkan musik PC iPhone", "berbagi musik Mac iOS", "SMB Windows streaming file", "akses Evermusic folder PC"]
---

{{< author-byline >}}


**Ringkasan:** Gunakan aplikasi Evermusic untuk iPhone atau iPad untuk streaming musik dari Mac atau Windows PC Anda melalui jaringan lokal menggunakan SMB. Tanpa sinkronisasi, tanpa menyalin -- cukup aktifkan berbagi file di komputer Anda, hubungkan di aplikasi, dan putar. Pengaturan membutuhkan waktu kurang dari 5 menit.

Apakah Anda tenggelam dalam lautan musik di MAC atau PC Anda dan ingin menikmatinya tanpa repot di iPhone atau iPad Anda? Tidak perlu mencari lebih jauh dari Evermusic. Dengan Evermusic, sangat mudah untuk menghubungkan komputer Anda menggunakan protokol SMB dan streaming lagu-lagu favorit Anda tanpa khawatir menghabiskan ruang penyimpanan tambahan atau berurusan dengan masalah sinkronisasi. Berikut panduan langkah demi langkah untuk memulai:

## Langkah 1: Aktifkan Protokol SMB di Komputer Anda

![Evermusic - Dukungan SMB - Layar Berbagi Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Jika Anda menggunakan MAC

- Buka System Preferences -> Sharing.
- Aktifkan layanan File Sharing.
- Di bagian "Shared Folders", tambahkan folder musik Anda, pilih pengguna, dan atur tingkat izin (Read & Write atau Read Only).
- Untuk kemudahan tambahan, Anda dapat memilih "Everyone: Read Only" untuk folder musik, membuatnya mudah diakses di Evermusic.
- Jangan lupa untuk mengingat URL komputer Anda (smb://192.168.xx.xx) untuk langkah selanjutnya.

![Evermusic - Dukungan SMB - Layar Berbagi File](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Ketuk "Options" dan aktifkan "Share files and folders using SMB."
- Aktifkan "Windows File Sharing" untuk akun yang tersedia.

![Evermusic - Dukungan SMB - Layar Berbagi File dan Folder](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Jika Anda menggunakan Windows PC

![Evermusic - Dukungan SMB - Berbagi File di Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Klik kanan pada folder musik Anda.
- Pilih "Properties."
- Buka tab "Sharing."
- Klik "Share..."
- Pilih orang yang ingin Anda ajak berbagi dan atur tingkat izin mereka.
- Seperti di MAC, Anda dapat memilih "Everyone: Read" untuk folder musik yang dipilih.
- Klik "Selesai" untuk menyimpan pengaturan Anda.

![Evermusic - Dukungan SMB - Folder yang Dibagikan di Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Langkah 2: Tambahkan Komputer Anda Secara Otomatis

- Sekarang, buka Evermusic dan pergi ke tab "Koneksi" ("Jaringan" jika Anda menggunakan versi aplikasi lama).
- Jika Anda melihat komputer Anda di bagian "Perangkat yang Tersedia" ("Share yang tersedia" jika Anda menggunakan versi aplikasi lama) dan memilih "Everyone: Read Only" di langkah sebelumnya, cukup ketuk komputer Anda dan akan terhubung secara otomatis.
- Jika ini tidak terjadi, Anda dapat menambahkan komputer Anda secara manual.

![Evermusic - Dukungan SMB - Layar Hubungkan Akun](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Langkah 3: Tambahkan Komputer Anda Secara Manual

- Ketuk "Hubungkan layanan cloud" ("Tambah Akun" jika Anda menggunakan versi aplikasi lama)
- Pilih "SMB" dari daftar server yang tersedia di layar berikutnya.
- Di layar pengaturan "SMB":
  - Masukkan URL server dengan jalur folder yang dibagikan. Anda dapat memasukkan nama server atau IP server. Contoh:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Masukkan Login dan Password Anda atau biarkan kolom ini kosong jika Anda memilih "Everyone: Read Only" di langkah sebelumnya.
  - Kolom "WORKGROUP" bersifat opsional dan harus digunakan jika Anda memiliki Domain Active Directory.

![Evermusic - Dukungan SMB - Layar Masukkan Kredensial](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Setelah Anda menghubungkan Akun SMB, itu akan muncul di bagian "Layanan cloud" ("Akun"). Buka akun yang terhubung dengan mengetuknya, navigasi ke folder musik, dan ketuk file audio apa pun untuk memulai pemutar.

![Evermusic - Dukungan SMB - Layar Buka Folder yang Terhubung](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Nikmati koleksi musik Anda dengan lancar di iPhone atau iPad Anda dengan Evermusic.

![Evermusic - Dukungan SMB - Layar Pemutar Audio](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Langkah 4: Solusi SMB2

Jika Anda mengalami masalah dalam menelusuri folder atau memutar file yang mengandung simbol khusus (seperti ü, ö, é), ini mungkin terkait dengan protokol SMB2. Kami sedang aktif bekerja untuk menyelesaikan masalah ini.

Sebagai solusi sementara, silakan coba aktifkan SMB 1 di server Anda dan di pengaturan aplikasi. Alternatifnya, Anda dapat terhubung ke server SMB menggunakan menu buka file sistem. Begini caranya:

1. Navigasi ke "File lokal."
2. Gulir ke bawah ke bagian "File di perangkat ini" dan ketuk "Buka file..." atau "Buka folder..."
3. Temukan server Anda dan pilih file atau folder yang Anda butuhkan.
4. Ketuk "Buka" untuk mengonfirmasi pilihan Anda.

## Langkah 5: Solusi WebDAV

Selain itu, Anda dapat mencoba menghubungkan ke NAS menggunakan protokol WebDAV atau DLNA jika didukung.

Dengan mengikuti langkah-langkah ini, Anda dapat melewati masalah terkait simbol khusus dalam nama file dan terus menikmati file media Anda.

P.S. Anda juga dapat mentransfer file audio dari MAC/PC ke iPhone menggunakan iTunes File Sharing dan memutar file audio lokal. Pelajari lebih lanjut tentang fitur ini di panduan kami: [Cara Memutar File iTunes di iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Pertanyaan yang Sering Diajukan

{{% details title="Bisakah saya streaming musik dari PC ke iPhone tanpa iTunes?" closed="true" %}}
Ya. Evermusic terhubung ke PC Anda melalui SMB di jaringan Wi-Fi lokal Anda. iTunes tidak diperlukan. Cukup aktifkan berbagi file di PC Anda dan hubungkan di aplikasi.
{{% /details %}}

{{% details title="Apakah streaming SMB menggunakan data seluler?" closed="true" %}}
Tidak. SMB bekerja melalui jaringan Wi-Fi lokal Anda. Tidak diperlukan koneksi internet atau data seluler.
{{% /details %}}

{{% details title="Format audio apa yang didukung Evermusic melalui SMB?" closed="true" %}}
Evermusic mendukung MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC, dan format audio umum lainnya. File diputar langsung dari share SMB.
{{% /details %}}

{{% details title="Bisakah saya streaming musik dari NAS ke iPhone?" closed="true" %}}
Ya. Jika NAS Anda mendukung SMB (kebanyakan mendukung, termasuk Synology, QNAP, dan WD My Cloud), Anda dapat menghubungkannya menggunakan langkah-langkah yang sama di panduan ini.
{{% /details %}}

{{% details title="Apakah saya perlu menjaga komputer tetap menyala saat streaming?" closed="true" %}}
Ya. Karena Evermusic streaming file langsung dari komputer Anda, komputer harus menyala dan terhubung ke jaringan yang sama dengan iPhone Anda.
{{% /details %}}

{{% details title="Apakah ada batas ukuran file untuk streaming SMB?" closed="true" %}}
Tidak. Evermusic streaming file dengan ukuran berapa pun melalui SMB. File lossless besar (FLAC, WAV) bekerja tanpa masalah.
{{% /details %}}
