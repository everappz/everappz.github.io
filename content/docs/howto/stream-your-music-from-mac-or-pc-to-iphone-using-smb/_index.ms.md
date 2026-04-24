---
title: "Strim Muzik Anda dari Mac atau PC ke iPhone Menggunakan SMB"
description: "Ketahui cara menstrim koleksi muzik anda dari Mac atau Windows PC ke iPhone atau iPad anda menggunakan Evermusic dan protokol SMB. Panduan langkah demi langkah yang mudah untuk menyambung dan menikmati audio tanpa penyegerakan."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["strim muzik dari Mac ke iPhone", "SMB audio streaming iOS", "persediaan Evermusic SMB", "sambung muzik PC iPhone", "perkongsian muzik Mac iOS", "SMB Windows penstriman fail", "akses Evermusic folder PC"]
---

{{< author-byline >}}


**Ringkasan:** Gunakan aplikasi Evermusic untuk iPhone atau iPad untuk menstrim muzik dari Mac atau Windows PC anda melalui rangkaian tempatan menggunakan SMB. Tiada penyegerakan, tiada penyalinan -- hanya aktifkan perkongsian fail pada komputer anda, sambung dalam aplikasi dan mainkan. Persediaan mengambil masa kurang daripada 5 minit.

Adakah anda lemas dalam lautan muzik pada MAC atau PC anda dan ingin menikmatinya tanpa kerumitan pada iPhone atau iPad anda? Tidak perlu mencari lebih jauh daripada Evermusic. Dengan Evermusic, ia sangat mudah untuk menyambungkan komputer anda menggunakan protokol SMB dan menstrim lagu kegemaran anda tanpa perlu risau tentang menggunakan ruang peranti tambahan atau berurusan dengan masalah penyegerakan. Berikut adalah panduan langkah demi langkah untuk bermula:

## Langkah 1: Aktifkan Protokol SMB pada Komputer Anda

![Evermusic - Sokongan SMB - Skrin Perkongsian Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Jika anda menggunakan MAC

- Buka System Preferences -> Sharing.
- Aktifkan perkhidmatan File Sharing.
- Dalam bahagian "Shared Folders", tambah folder muzik anda, pilih pengguna dan tetapkan tahap kebenaran (Read & Write atau Read Only).
- Untuk kemudahan tambahan, anda boleh memilih "Everyone: Read Only" untuk folder muzik, menjadikannya mudah diakses dalam Evermusic.
- Jangan lupa untuk mengingat URL komputer anda (smb://192.168.xx.xx) untuk langkah seterusnya.

![Evermusic - Sokongan SMB - Skrin Perkongsian Fail](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Ketik "Options" dan aktifkan "Share files and folders using SMB."
- Aktifkan "Windows File Sharing" untuk akaun yang tersedia.

![Evermusic - Sokongan SMB - Skrin Kongsi Fail dan Folder](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Jika anda menggunakan Windows PC

![Evermusic - Sokongan SMB - Kongsi Fail pada Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Klik kanan pada folder muzik anda.
- Pilih "Properties."
- Buka tab "Sharing."
- Klik "Share..."
- Pilih orang untuk dikongsi dan tetapkan tahap kebenaran mereka.
- Seperti MAC, anda boleh memilih "Everyone: Read" untuk folder muzik yang dipilih.
- Klik "Selesai" untuk menyimpan tetapan anda.

![Evermusic - Sokongan SMB - Folder Dikongsi pada Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Langkah 2: Tambah Komputer Anda Secara Automatik

- Sekarang, buka Evermusic dan pergi ke tab "Sambungan" ("Rangkaian" jika anda menggunakan versi aplikasi lama).
- Jika anda melihat komputer anda dalam bahagian "Peranti yang tersedia" ("Perkongsian yang tersedia" jika anda menggunakan versi aplikasi lama) dan memilih "Everyone: Read Only" dalam langkah sebelumnya, hanya ketik pada komputer anda dan ia akan disambungkan secara automatik.
- Jika ini tidak berlaku, anda boleh menambah komputer anda secara manual.

![Evermusic - Sokongan SMB - Skrin Sambung Akaun](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Langkah 3: Tambah Komputer Anda Secara Manual

- Ketik "Sambung perkhidmatan awan" ("Tambah Akaun" jika anda menggunakan versi aplikasi lama)
- Pilih "SMB" dari senarai pelayan yang tersedia pada skrin seterusnya.
- Pada skrin tetapan "SMB":
  - Masukkan URL pelayan dengan laluan folder yang dikongsi. Anda boleh memasukkan nama pelayan atau IP pelayan. Contoh:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Masukkan Login dan Kata Laluan anda atau biarkan medan ini kosong jika anda memilih "Everyone: Read Only" dalam langkah sebelumnya.
  - Medan "WORKGROUP" adalah pilihan dan harus digunakan jika anda mempunyai Domain Active Directory.

![Evermusic - Sokongan SMB - Skrin Masukkan Kelayakan](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Setelah anda menyambungkan Akaun SMB anda, ia akan muncul dalam bahagian "Perkhidmatan awan" ("Akaun"). Buka akaun yang disambungkan dengan mengetiknya, navigasi ke folder muzik dan ketik pada mana-mana fail audio untuk memulakan pemain.

![Evermusic - Sokongan SMB - Skrin Buka Folder yang Disambungkan](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Nikmati koleksi muzik anda dengan lancar pada iPhone atau iPad anda dengan Evermusic.

![Evermusic - Sokongan SMB - Skrin Pemain Audio](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Langkah 4: Penyelesaian SMB2

Jika anda mengalami masalah dengan melayari folder atau memainkan fail yang mengandungi simbol khas (seperti ü, ö, é), ini mungkin berkaitan dengan protokol SMB2. Kami sedang giat berusaha menyelesaikan masalah ini.

Sebagai penyelesaian sementara, sila cuba aktifkan SMB 1 pada pelayan anda dan dalam tetapan aplikasi. Sebagai alternatif, anda boleh menyambung ke pelayan SMB anda menggunakan menu buka fail sistem. Begini caranya:

1. Navigasi ke "Fail tempatan."
2. Tatal ke bawah ke bahagian "Fail pada peranti ini" dan ketik "Buka fail..." atau "Buka folder..."
3. Cari pelayan anda dan pilih fail atau folder yang anda perlukan.
4. Ketik "Buka" untuk mengesahkan pilihan anda.

## Langkah 5: Penyelesaian WebDAV

Selain itu, anda boleh cuba menyambung ke NAS anda menggunakan protokol WebDAV atau DLNA jika disokong.

Dengan mengikuti langkah-langkah ini, anda boleh mengatasi masalah berkaitan simbol khas dalam nama fail dan terus menikmati fail media anda.

P.S. Anda juga boleh memindahkan fail audio dari MAC/PC anda ke iPhone anda menggunakan iTunes File Sharing dan memainkan fail audio tempatan. Ketahui lebih lanjut tentang ciri ini dalam panduan kami: [Cara Memainkan Fail iTunes pada iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Soalan Lazim

{{% details title="Bolehkah saya menstrim muzik dari PC ke iPhone tanpa iTunes?" closed="true" %}}
Ya. Evermusic menyambung ke PC anda melalui SMB pada rangkaian Wi-Fi tempatan anda. iTunes tidak diperlukan. Hanya aktifkan perkongsian fail pada PC anda dan sambung dalam aplikasi.
{{% /details %}}

{{% details title="Adakah penstriman SMB menggunakan data mudah alih?" closed="true" %}}
Tidak. SMB berfungsi melalui rangkaian Wi-Fi tempatan anda. Tiada sambungan internet atau data mudah alih diperlukan.
{{% /details %}}

{{% details title="Apakah format audio yang disokong Evermusic melalui SMB?" closed="true" %}}
Evermusic menyokong MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC dan format audio biasa yang lain. Fail dimainkan terus dari perkongsian SMB.
{{% /details %}}

{{% details title="Bolehkah saya menstrim muzik dari NAS ke iPhone?" closed="true" %}}
Ya. Jika NAS anda menyokong SMB (kebanyakan menyokong, termasuk Synology, QNAP dan WD My Cloud), anda boleh menyambung kepadanya menggunakan langkah yang sama dalam panduan ini.
{{% /details %}}

{{% details title="Adakah saya perlu memastikan komputer saya dihidupkan semasa penstriman?" closed="true" %}}
Ya. Oleh kerana Evermusic menstrim fail terus dari komputer anda, ia mesti dihidupkan dan disambungkan ke rangkaian yang sama dengan iPhone anda.
{{% /details %}}

{{% details title="Adakah had saiz fail untuk penstriman SMB?" closed="true" %}}
Tidak. Evermusic menstrim fail dalam apa-apa saiz melalui SMB. Fail lossless besar (FLAC, WAV) berfungsi tanpa masalah.
{{% /details %}}
