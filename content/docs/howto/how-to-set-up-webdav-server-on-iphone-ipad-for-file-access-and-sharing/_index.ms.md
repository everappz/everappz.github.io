---
title: "Cara Menyediakan Pelayan WebDAV pada iPhone & iPad untuk Akses & Perkongsian Fail"
description: "Jadikan iPhone atau iPad anda pelayan WebDAV dengan Everdisk dan lekapkannya sebagai pemacu rangkaian pada Mac Finder, Windows File Explorer, Linux, Android atau iPhone lain melalui Wi-Fi. Penyediaan penuh, alamat dan port WebDAV, dan sambungan langkah demi langkah untuk setiap peranti."
date: 2026-09-19
tags: ["everdisk", "webdav", "pemacu rangkaian", "perkongsian fail", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["pelayan WebDAV iPhone", "pelayan WebDAV iPad", "cara menyediakan WebDAV pada iPhone", "lekapkan iPhone sebagai pemacu rangkaian", "sambung iPhone WebDAV Mac Finder", "WebDAV Windows File Explorer iPhone", "pemacu rangkaian iphone Windows", "WebDAV Linux iPhone", "akses fail iPhone dari komputer", "webdav iphone ke iphone", "kongsi fail iPhone WebDAV", "petakan pemacu rangkaian iphone", "pindah fail iphone webdav", "alamat port webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV mengubah folder menjadi pemacu rangkaian yang boleh dibuka oleh komputer dalam pengurus fail biasanya. Ia berjalan pada protokol web yang sama seperti yang digunakan oleh pelayar anda, itulah sebabnya ia merentasi Mac, Windows dan Linux dengan baik tanpa pemacu khas. Dengan [Everdisk](/products/everdisk) anda boleh menjalankan pelayan WebDAV pada iPhone atau iPad anda, jadi telefon muncul sebagai pemacu yang boleh anda layari, salin daripadanya, dan salin kepadanya daripada hampir mana-mana komputer.

WebDAV ialah pilihan terbaik apabila Windows terlibat, kerana Windows File Explorer menyambung kepadanya dengan bersih. Panduan ini merangkumi penyediaan dan cara menyambung daripada Mac, Windows, Linux, Android dan iPhone kedua.

## Apa yang anda perlukan

- Sebuah iPhone atau iPad dengan [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dipasang.
- Sebuah komputer atau peranti lain pada **rangkaian Wi-Fi yang sama**.
- Fail yang anda mahu kongsi, dalam folder Dokumen Everdisk atau dalam folder yang anda tambah.

## Sediakan pelayan WebDAV dalam Everdisk

### Langkah 1: Pilih apa untuk dikongsi dan tetapkan akses

Buka Everdisk, pergi ke tab **Perkongsian**, dan ketik **Apa untuk Dikongsi**. Folder Dokumen dikongsi secara lalai. Tambah lagi dengan **Tambah Folder** dan **Tambah Fail**.

Buka **Tetapan**, kemudian **Perkongsian**, kemudian **Akses**. Hidupkan **Penyuntingan Fail** jika anda mahu komputer yang disambung menyalin fail ke telefon anda serta menamakan semula atau memadamnya, atau matikannya untuk pemacu baca sahaja. Tetapkan **Log Masuk** dan **Kata Laluan** di sini jika anda mahu log masuk, atau biarkannya kosong untuk akses tetamu.

### Langkah 2: Hidupkan pelayan WebDAV

Pergi ke **Tetapan**, kemudian **Perkongsian**, kemudian **Sambungan**, dan hidupkan **Komputer**. Itulah pelayan WebDAV (ia membawa tag WebDAV).

### Langkah 3: Mula berkongsi dan catat alamat

Kembali ke tab **Perkongsian** dan ketik **Mula**. Bahagian **How to Connect** menunjukkan alamat WebDAV. Ia kelihatan seperti ini:

```
http://192.168.1.20:8080
```

Nombor selepas titik bertindih ialah **port**, iaitu **8080** secara lalai. Bahagian pertama ialah alamat iPhone anda pada Wi-Fi, jadi milik anda akan berbeza. Kekalkan Everdisk terbuka pada skrin semasa peranti disambung.

## Sambung daripada Mac

1. Buka **Finder**, pilih **Go**, kemudian **Connect to Server** (atau tekan **Command dan K**).
2. Taip alamat WebDAV yang ditunjukkan dalam Everdisk, contohnya `http://192.168.1.20:8080`.
3. Klik **Connect**, kemudian pilih **Guest** atau masukkan **Log Masuk** dan **Kata Laluan** anda.

iPhone anda terbuka dalam tetingkap Finder dan berkelakuan seperti folder biasa. Salin fail ke mana-mana arah jika Penyuntingan Fail dihidupkan.

## Sambung daripada Windows

Windows mempunyai klien WebDAV terbina, jadi ini berfungsi daripada File Explorer.

1. Buka **File Explorer**, klik kanan **This PC** dalam bar sisi, dan pilih **Add a network location** (anda juga boleh menggunakan **Map network drive**).
2. Apabila diminta alamat, taip alamat WebDAV yang sama daripada Everdisk, contohnya `http://192.168.1.20:8080`, kemudian klik **Next**.
3. Masukkan **Log Masuk** dan **Kata Laluan** anda jika anda menetapkannya.

Peranti kemudian muncul di bawah This PC sebagai lokasi rangkaian yang boleh anda buka dan salin fail daripadanya. Jika Windows enggan menyambung pada kali pertama, pastikan perkhidmatan **WebClient** sedang berjalan (cari Services dalam menu Start, cari WebClient, dan tetapkannya untuk bermula), kemudian cuba lagi.

## Sambung daripada Linux

1. Buka pengurus fail anda dan pilih **Connect to Server** atau **Other Locations**.
2. Masukkan alamat dengan awalan WebDAV, contohnya `dav://192.168.1.20:8080` (gunakan `davs://` hanya jika anda menyediakan TLS).
3. Sambung sebagai tetamu atau masukkan log masuk anda.

## Sambung daripada Android

Android tidak mempunyai pelayar WebDAV sistem, jadi gunakan pengurus fail yang menyokongnya:

1. Pasang aplikasi seperti **Solid Explorer** atau **CX File Explorer**.
2. Tambah sambungan **WebDAV** baharu.
3. Masukkan hos dan **port 8080**, pilih skema `http`, dan tambah log masuk anda jika anda menetapkannya.

## Sambung daripada iPhone atau iPad lain

Aplikasi Files iOS tidak menyertakan klien WebDAV, jadi gunakan salah satu daripada ini:

- **Tab Peranti milik Everdisk.** Pada peranti kedua, buka Everdisk, pergi ke **Peranti**, ketik **Sambungan Baharu**, pilih **WebDAV**, dan masukkan alamat, contohnya `http://192.168.1.20:8080`. Inilah cara paling mudah dan tidak memerlukan apa-apa tambahan.
- **Aplikasi WebDAV** seperti Documents by Readdle, yang boleh menambah sambungan WebDAV dengan alamat dan log masuk yang sama.

## Lebih suka pautan pantas berbanding pemacu?

Jika anda hanya perlu mengambil fail dengan pantas dan tidak mahu melekapkan pemacu langsung, hidupkan sambungan **Pelayar** dalam Tetapan, Perkongsian, Sambungan. Everdisk kemudian memberi anda alamat web yang boleh anda buka dalam mana-mana pelayar pada mana-mana peranti untuk melayari dan memuat turun fail anda. Ia cara paling pantas untuk menyerahkan fail kepada PC Windows, Chromebook atau telefon rakan.

## Baca sahaja atau baca dan tulis

Suis **Penyuntingan Fail** dalam Tetapan, Perkongsian, Akses menentukan ini. Dihidupkan bermakna komputer yang disambung boleh memuat naik, menamakan semula dan memadam. Dimatikan bermakna pemacu adalah baca sahaja, jadi orang lain boleh melihat dan menyalin fail anda tetapi tidak boleh mengubahnya.

## Cara sebenar orang menggunakan ini

- **Salin fail ke iPhone anda daripada PC Windows** dengan memetakannya sebagai lokasi rangkaian dan menyeretnya merentas.
- **Pindahkan foto dan dokumen ke komputer riba** menggunakan pengurus fail yang sudah anda kenal, tanpa kabel dan tanpa iTunes.
- **Sunting dokumen di tempatnya** daripada Mac anda, membukanya terus daripada telefon dan menyimpannya semula.
- **Pindahkan folder antara iPhone dan iPad** menggunakan tab Peranti Everdisk pada peranti penerima.

## Beberapa petua

- Kekalkan Everdisk terbuka semasa peranti disambung. Mengunci telefon untuk masa yang lama boleh menjeda aplikasi.
- Pada Windows, jika sambungan gagal, mulakan perkhidmatan WebClient dan cuba alamat itu sekali lagi.
- WebDAV dan SMB kedua-duanya melekap sebagai pemacu rangkaian. Gunakan WebDAV apabila Windows terlibat, dan [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) apabila anda mahukan kelajuan Finder dan penyulitan.
- Untuk pemindahan terpantas, kekalkan kualiti foto dan video pada Asal dalam Tetapan.

## Soalan Lazim

{{% details title="Apakah alamat dan port WebDAV untuk iPhone saya?" closed="true" %}}
Selepas anda mula berkongsi, Everdisk menunjukkan alamat pada skrin Perkongsian. Ia kelihatan seperti http://192.168.1.20:8080. 8080 ialah port yang Everdisk gunakan untuk WebDAV, dan bahagian pertama ialah alamat iPhone anda pada Wi-Fi, jadi milik anda akan berbeza.
{{% /details %}}

{{% details title="Bagaimana saya sambung ke WebDAV iPhone saya daripada Windows?" closed="true" %}}
Buka File Explorer, klik kanan This PC, dan pilih Add a network location atau Map network drive. Masukkan alamat WebDAV daripada Everdisk, contohnya http://192.168.1.20:8080, kemudian masukkan log masuk anda jika anda menetapkannya. Jika Windows tidak mahu menyambung, pastikan perkhidmatan WebClient sedang berjalan (cari Services, cari WebClient, mulakannya) dan cuba lagi.
{{% /details %}}

{{% details title="Boleh saya guna WebDAV antara dua iPhone?" closed="true" %}}
Ya, tetapi aplikasi Files iOS tidak mempunyai klien WebDAV, jadi gunakan Everdisk pada peranti kedua. Buka tab Peranti, ketik Sambungan Baharu, pilih WebDAV, dan masukkan alamat yang ditunjukkan pada telefon pertama. Aplikasi WebDAV seperti Documents by Readdle turut berfungsi.
{{% /details %}}

{{% details title="Adakah WebDAV memerlukan kata laluan?" closed="true" %}}
Tidak, log masuk adalah pilihan. Biarkan Log Masuk dan Kata Laluan kosong dalam Tetapan, Perkongsian, Akses untuk akses tetamu, atau tetapkannya jika anda mahu sambungan log masuk.
{{% /details %}}

{{% details title="Boleh orang lain mengubah fail saya melalui WebDAV?" closed="true" %}}
Hanya jika anda membenarkannya. Suis Penyuntingan Fail dalam Tetapan, Perkongsian, Akses mengawal ini. Dihidupkan membenarkan peranti yang disambung memuat naik, menamakan semula dan memadam. Dimatikan menjadikan pemacu baca sahaja, jadi orang lain boleh melihat dan menyalin tetapi tidak boleh mengubah apa-apa.
{{% /details %}}

{{% details title="WebDAV atau SMB, apakah bezanya?" closed="true" %}}
Kedua-duanya melekapkan iPhone anda sebagai pemacu rangkaian. WebDAV berjalan pada protokol web dan menyambung dengan bersih daripada Windows File Explorer, itulah kekuatan utamanya. SMB ialah perkongsian fail asli pada Mac, Linux dan peranti NAS, biasanya lebih laju pada Mac, dan ialah satu-satunya sambungan Everdisk yang boleh menyulitkan pemindahan. Everdisk boleh menjalankan kedua-duanya serentak.
{{% /details %}}

{{% details title="Mengapa pemacu WebDAV saya terputus?" closed="true" %}}
iPhone anda ialah pelayan, dan iOS menjeda aplikasi yang berada di latar belakang terlalu lama. Kekalkan Everdisk terbuka pada skrin semasa peranti disambung, dan palamkan ke sumber kuasa untuk pemindahan yang panjang. Sahkan juga kedua-dua peranti masih berada pada Wi-Fi yang sama.
{{% /details %}}

{{% details title="Boleh saya sambung melalui WebDAV tanpa Wi-Fi?" closed="true" %}}
Ya, jika anda palamkan iPhone anda ke Mac dengan kabel. Everdisk kemudian menunjukkan alamat sambungan kabel tambahan yang boleh dibuka oleh Mac yang disambung dalam Finder, yang berfungsi walaupun tanpa Wi-Fi langsung. Pada kabel, hanya Mac itu boleh mencapai peranti.
{{% /details %}}

{{% details title="Adakah Everdisk percuma?" closed="true" %}}
Ya, Everdisk percuma untuk dimuat turun dan pelayan WebDAV disertakan. Pembelian Premium sekali sahaja pilihan menambah tambahan seperti port tersuai dan penukaran foto dan video. Anda boleh menyediakan WebDAV dan berkongsi fail tanpa membayar.
{{% /details %}}

Sedia untuk mencuba? [Muat turun Everdisk dari App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dan lekapkan iPhone anda sebagai pemacu dalam masa beberapa minit. Ada soalan atau maklum balas? E-mel kami di **support@everappz.com**.
