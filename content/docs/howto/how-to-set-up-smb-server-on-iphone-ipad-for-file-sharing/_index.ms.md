---
title: "Cara Menyediakan Pelayan SMB pada iPhone & iPad untuk Perkongsian Fail"
description: "Jadikan iPhone atau iPad anda pelayan fail SMB dengan Everdisk dan bukanya seperti pemacu rangkaian daripada Mac, iPhone lain, Linux atau Android melalui Wi-Fi. Penyediaan penuh, alamat dan port smb, penyulitan SMB3 pilihan, dan sambungan langkah demi langkah untuk setiap peranti."
date: 2026-09-19
tags: ["everdisk", "smb", "perkongsian fail", "pemacu rangkaian", "iphone", "ipad", "mac", "finder", "penyulitan", "wifi"]
keywords: ["pelayan SMB iPhone", "pelayan SMB iPad", "cara menyediakan SMB pada iPhone", "kongsi SMB iPhone", "sambung iPhone SMB Mac Finder", "smb iphone ke iphone", "aplikasi Files iOS sambung ke pelayan SMB", "kongsi fail iPhone SMB", "pemacu rangkaian iphone Finder", "penyulitan SMB3 iOS", "kongsi smb iPhone Android", "sambung ke SMB dari Linux", "iphone sebagai pemacu rangkaian", "kongsi fail antara iphone wifi", "petakan iphone sebagai pemacu rangkaian"]
readingTime: 10
---

{{< author-byline >}}

SMB ialah perkongsian fail yang terbina dalam macOS, Windows dan Linux, serta dalam hampir setiap pemacu rangkaian (NAS). Apabila anda menyambung ke folder kongsi pada komputer lain dan ia terbuka seperti cakera biasa dalam Finder atau File Explorer, itulah SMB yang bekerja. Dengan [Everdisk](/products/everdisk) anda boleh meletakkan perkongsian SMB pada iPhone atau iPad anda, jadi telefon itu sendiri muncul sebagai pemacu rangkaian yang boleh dilayari, disalin daripadanya, dan disalin kepadanya oleh peranti lain.

Inilah pilihan yang perlu dicapai apabila anda mahu iPhone anda berkelakuan seperti pemacu sebenar, bukan halaman web. Ia pantas, ia menyeret dan melepas ke dua-dua arah, dan ia satu-satunya jenis sambungan dalam Everdisk yang boleh menyulitkan setiap pemindahan. Panduan ini merangkumi penyediaan dan cara menyambung daripada Mac, iPhone atau iPad lain, Linux, Android dan Windows.

## Apa yang anda perlukan

- Sebuah iPhone atau iPad dengan [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dipasang.
- Peranti lain pada **rangkaian Wi-Fi yang sama**.
- Fail yang anda mahu kongsi, dalam folder Dokumen Everdisk atau dalam folder yang anda tambah.

## Sediakan pelayan SMB dalam Everdisk

### Langkah 1: Pilih apa untuk dikongsi dan siapa boleh menulis

Buka Everdisk, pergi ke tab **Perkongsian**, dan ketik **Apa untuk Dikongsi**. Folder Dokumen dikongsi secara lalai. Tambah lagi dengan **Tambah Folder** dan **Tambah Fail**, dan hidupkan pustaka Foto atau Muzik anda jika anda mahu itu turut tersedia.

Tentukan sama ada peranti lain hanya boleh membaca fail anda, atau turut mengubahnya. Buka **Tetapan**, kemudian **Perkongsian**, kemudian **Akses**, dan tetapkan **Penyuntingan Fail**. Dengan ia dihidupkan, peranti yang disambung boleh menyalin fail ke telefon anda serta menamakan semula atau memadamnya. Dengan ia dimatikan, perkongsian adalah baca sahaja.

Jika anda mahu log masuk, tetapkan **Log Masuk** dan **Kata Laluan** pada skrin Akses yang sama. Biarkan kedua-duanya kosong untuk membenarkan akses tetamu.

### Langkah 2: Hidupkan pelayan SMB

Pergi ke **Tetapan**, kemudian **Perkongsian**, kemudian **Sambungan**, dan hidupkan **Komputer (Lanjutan)**. Itulah pelayan SMB (ia membawa tag SMB).

### Langkah 3: Mula berkongsi dan catat alamat

Kembali ke tab **Perkongsian** dan ketik **Mula**. Bahagian **How to Connect** kini menunjukkan alamat SMB. Ia kelihatan seperti ini:

```
smb://192.168.1.20:4455/Share
```

Tiga perkara yang perlu diketahui tentang alamat itu:

- Nombor selepas titik bertindih ialah **port**. Everdisk menggunakan **4455** secara lalai.
- Perkongsian itu dinamakan **Share**.
- Bahagian pertama ialah alamat iPhone anda pada Wi-Fi, jadi ia akan berbeza pada rangkaian anda.

Kekalkan Everdisk terbuka semasa peranti disambung, kerana iOS menjeda aplikasi yang berada di latar belakang terlalu lama.

## Sambung daripada Mac

Inilah kes paling lancar, kerana macOS memahami SMB secara asli.

Cara paling pantas: buka **Finder** dan lihat dalam bar sisi di bawah **Locations** atau **Network**. Everdisk mengumumkan dirinya pada Wi-Fi, jadi iPhone anda selalunya muncul di situ dengan sendirinya. Klik padanya, kemudian klik **Connect As** dan pilih **Guest**, atau masukkan log masuk anda.

Untuk menyambung secara manual:

1. Dalam Finder, pilih **Go**, kemudian **Connect to Server** (atau tekan **Command dan K**).
2. Taip alamat SMB yang ditunjukkan dalam Everdisk, contohnya `smb://192.168.1.20:4455/Share`.
3. Klik **Connect**, kemudian pilih **Guest** atau masukkan **Log Masuk** dan **Kata Laluan** anda.

iPhone anda terbuka dalam tetingkap Finder. Salin fail masuk atau keluar dengan menyeret, tepat seperti mana-mana pemacu lain (jika Penyuntingan Fail dihidupkan).

## Sambung daripada iPhone atau iPad lain

iOS dan iPadOS boleh membuka perkongsian SMB dalam aplikasi **Files** terbina, yang menjadikan pemindahan telefon ke telefon bersih dan pantas.

Pada peranti kedua:

1. Buka aplikasi **Files**.
2. Ketik butang **more** (tiga titik, di kanan atas pada iPhone) dan pilih **Connect to Server**.
3. Masukkan alamat SMB daripada Everdisk, contohnya `smb://192.168.1.20:4455/Share`.
4. Pilih **Guest**, atau **Registered User** dan masukkan log masuk anda.
5. Perkongsian muncul di bawah Locations dalam Files. Layari dan salin ke mana-mana arah.

Anda juga boleh menggunakan tab **Peranti** milik Everdisk pada peranti kedua, yang menyertakan klien SMB. Buka Everdisk, pergi ke **Peranti**, ketik **Sambungan Baharu**, pilih **SMB**, dan masukkan alamat.

## Sambung daripada Linux

1. Buka pengurus fail anda (Files/Nautilus pada GNOME, Dolphin pada KDE).
2. Pilih **Other Locations** atau **Connect to Server**.
3. Masukkan alamat, contohnya `smb://192.168.1.20:4455/Share`.
4. Sambung sebagai tetamu, atau masukkan log masuk anda.

Daripada terminal anda juga boleh menjalankan `smbclient //192.168.1.20/Share -p 4455` dan masukkan log masuk anda apabila diminta.

## Sambung daripada Android

Android tidak mempunyai pelayar SMB sistem, jadi gunakan pengurus fail yang menyokong SMB:

1. Pasang aplikasi seperti **CX File Explorer**, **Solid Explorer**, atau **X-plore File Manager**.
2. Tambah sambungan **SMB** atau **LAN** baharu.
3. Masukkan hos (alamat Wi-Fi iPhone anda), tetapkan **port kepada 4455**, dan nama perkongsian **Share**.
4. Sambung sebagai tetamu atau dengan log masuk anda, kemudian layari dan salin.

## Sambung daripada Windows

Windows boleh membaca perkongsian SMB, dengan satu perkara yang patut diketahui lebih awal. File Explorer terbina hanya bercakap dengan SMB pada port piawai dan tidak membenarkan anda menaip port tersuai dalam laluan, dan Everdisk menggunakan port 4455. Jadi laluan **Map network drive** biasa selalunya tidak akan sampai kepadanya.

Anda mempunyai dua pilihan baik pada Windows:

- Gunakan pengurus fail atau klien SMB yang membenarkan anda menetapkan port tersuai, dan halakannya ke alamat iPhone anda dengan port **4455** dan nama perkongsian **Share**.
- Atau sambung daripada Windows menggunakan salah satu pelayan Everdisk yang lain sebagai ganti. [Penyediaan WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) dan [penyediaan FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) kedua-duanya berfungsi dengan baik daripada Windows File Explorer, dan pautan pelayar berfungsi dalam mana-mana pelayar.

Jika anda memang mahu mencuba Map network drive: buka **File Explorer**, klik kanan **This PC**, pilih **Map network drive**, dan masukkan hos serta nama perkongsian yang ditunjukkan dalam Everdisk. Jika ia tidak dapat menyambung, itulah had port di atas, jadi tukar ke WebDAV atau FTP.

## Hidupkan penyulitan untuk Wi-Fi yang tidak dipercayai

SMB ialah satu-satunya sambungan Everdisk yang boleh menyulitkan setiap pemindahan, yang penting pada Wi-Fi yang anda tidak kawal sepenuhnya, seperti kafe atau rangkaian pejabat.

1. Dalam **Tetapan**, **Perkongsian**, **Akses**, tetapkan **Log Masuk** dan **Kata Laluan**. Sambungan yang disulitkan tidak boleh tanpa nama, jadi langkah ini diperlukan.
2. Dalam **Tetapan**, **Perkongsian**, hidupkan **Wajibkan penyulitan SMB**.
3. Hentikan dan mulakan perkongsian sekali lagi supaya perubahan berkuat kuasa.

Setiap pemindahan SMB kemudian dilindungi dengan **penyulitan SMB3 (AES)**. Peranti yang menyambung perlu menyokong SMB3, iaitu yang dilakukan oleh Finder pada Mac moden dan Windows 10 atau lebih baharu. Penyulitan SMB adalah sebahagian daripada pembelian Premium sekali sahaja.

## Baca sahaja atau baca dan tulis

Suis **Penyuntingan Fail** dalam Tetapan, Perkongsian, Akses mengawal ini untuk setiap pelayan, termasuk SMB. Hidupkannya dan peranti yang disambung boleh memuat naik, menamakan semula dan memadam. Matikannya dan mereka hanya boleh melayari dan menyalin fail keluar dari telefon anda. Pilih baca sahaja apabila anda menyerahkan fail kepada seseorang yang anda tidak mahu mengubah apa-apa.

## Cara sebenar orang menggunakan ini

- **Pindahkan folder besar ke iPhone anda daripada Mac** dengan menyeretnya ke dalam tetingkap Finder, lebih laju daripada muat naik web.
- **Tarik sehari foto dan video keluar dari telefon anda** ke komputer riba tanpa iTunes atau kabel.
- **Hantar fail antara dua iPhone** melalui aplikasi Files, tanpa aplikasi ketiga di mana-mana pihak.
- **Bekerja dengan fail di tempatnya**, membuka dokumen terus daripada telefon dalam aplikasi pada Mac anda dan menyimpannya semula.

## Beberapa petua

- Kekalkan Everdisk terbuka semasa peranti disambung. Mengunci telefon untuk masa yang lama boleh menjeda aplikasi dan memutuskan sambungan.
- Jika Mac tidak dapat melihat telefon dalam bar sisi Finder, sambung secara manual dengan Connect to Server dan alamat smb penuh.
- Untuk kelajuan terbaik pada pemindahan besar, kekalkan kualiti foto dan video pada Asal dalam Tetapan.
- Pada rangkaian yang tidak dipercayai, hidupkan Wajibkan penyulitan SMB dan matikan pelayan lain semasa anda bekerja.

## Soalan Lazim

{{% details title="Apakah alamat dan port SMB untuk iPhone saya?" closed="true" %}}
Selepas anda mula berkongsi, Everdisk menunjukkan alamat pada skrin Perkongsian. Ia kelihatan seperti smb://192.168.1.20:4455/Share. 4455 ialah port yang Everdisk gunakan untuk SMB, dan Share ialah nama folder kongsi. Bahagian pertama ialah alamat iPhone anda pada Wi-Fi, jadi milik anda akan berbeza.
{{% /details %}}

{{% details title="Boleh saya sambung ke perkongsian SMB iPhone saya daripada Windows?" closed="true" %}}
Windows File Explorer hanya menyambung ke SMB pada port piawai dan tidak menerima port tersuai dalam laluan, manakala Everdisk menggunakan port 4455. Jadi laluan Map network drive biasa selalunya tidak akan sampai kepadanya. Gunakan pengurus fail yang membenarkan anda menetapkan port tersuai, atau sambung daripada Windows dengan WebDAV, FTP atau pautan pelayar sebagai ganti. Semua itu berfungsi daripada Windows tanpa masalah port.
{{% /details %}}

{{% details title="Bagaimana saya kongsi fail antara dua iPhone dengan SMB?" closed="true" %}}
Mula pelayan SMB pada iPhone pertama dalam Everdisk. Pada iPhone kedua, buka aplikasi Files, ketik butang more, pilih Connect to Server, dan masukkan alamat smb yang ditunjukkan dalam Everdisk (contohnya smb://192.168.1.20:4455/Share). Sambung sebagai Guest atau dengan log masuk anda, dan perkongsian muncul dalam Files. Anda juga boleh menggunakan tab Peranti milik Everdisk pada telefon kedua.
{{% /details %}}

{{% details title="Adakah iPhone saya muncul dalam bar sisi Mac Finder secara automatik?" closed="true" %}}
Biasanya ya. Everdisk mengumumkan perkongsian SMB pada Wi-Fi anda, jadi iPhone anda selalunya muncul di bawah Locations atau Network dalam bar sisi Finder. Klik padanya dan pilih Connect As, kemudian Guest atau log masuk anda. Jika ia tidak muncul, sambung secara manual dengan Go, Connect to Server dan alamat smb penuh.
{{% /details %}}

{{% details title="Perlukah saya kata laluan untuk menggunakan SMB?" closed="true" %}}
Tidak, log masuk adalah pilihan. Biarkan Log Masuk dan Kata Laluan kosong dalam Tetapan, Perkongsian, Akses untuk membenarkan akses tetamu. Tetapkannya jika anda mahu sambungan log masuk. Log masuk dan kata laluan diperlukan hanya jika anda menghidupkan Wajibkan penyulitan SMB, kerana sambungan yang disulitkan tidak boleh tanpa nama.
{{% /details %}}

{{% details title="Adakah sambungan SMB disulitkan?" closed="true" %}}
Ia boleh. SMB ialah satu-satunya sambungan Everdisk yang menyokong penyulitan. Tetapkan log masuk dan kata laluan, kemudian hidupkan Wajibkan penyulitan SMB dalam Tetapan, Perkongsian. Setiap pemindahan kemudian dilindungi dengan SMB3 (AES). Peranti yang lain perlu menyokong SMB3, iaitu yang dilakukan oleh Mac moden dan Windows 10 atau lebih baharu. Penyulitan ialah ciri Premium.
{{% /details %}}

{{% details title="Boleh orang mengubah atau memadam fail saya melalui SMB?" closed="true" %}}
Hanya jika anda membenarkannya. Suis Penyuntingan Fail dalam Tetapan, Perkongsian, Akses mengawal ini. Dengan ia dihidupkan, peranti yang disambung boleh memuat naik, menamakan semula dan memadam. Dengan ia dimatikan, perkongsian adalah baca sahaja dan orang lain boleh melayari dan menyalin fail keluar dari telefon anda tetapi tidak boleh mengubah apa-apa.
{{% /details %}}

{{% details title="Mengapa sambungan SMB saya terputus?" closed="true" %}}
iPhone anda ialah pelayan, dan iOS menjeda aplikasi yang berada di latar belakang terlalu lama. Kekalkan Everdisk terbuka pada skrin semasa peranti disambung, dan palamkan telefon ke sumber kuasa semasa pemindahan yang panjang. Pastikan juga kedua-dua peranti kekal pada Wi-Fi yang sama.
{{% /details %}}

{{% details title="SMB, WebDAV atau FTP, yang mana patut saya gunakan?" closed="true" %}}
Gunakan SMB apabila anda mahu telefon berkelakuan seperti pemacu rangkaian sebenar pada Mac, iPhone lain, Linux atau NAS, dan apabila anda mahukan penyulitan. Gunakan WebDAV apabila anda mahu pemacu rangkaian yang turut berfungsi dengan baik dari Windows. Gunakan FTP untuk keserasian paling luas dengan peranti dan aplikasi lama. Everdisk boleh menjalankan kesemuanya serentak, jadi anda tidak terkurung dengan satu sahaja.
{{% /details %}}

{{% details title="Adakah Everdisk percuma?" closed="true" %}}
Ya, Everdisk percuma untuk dimuat turun dan pelayan SMB disertakan. Pembelian Premium sekali sahaja pilihan menambah penyulitan SMB, port tersuai dan beberapa tambahan lain. Anda boleh menyediakan SMB dan berkongsi fail tanpa membayar.
{{% /details %}}

Sedia untuk mencuba? [Muat turun Everdisk dari App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dan buka iPhone anda dalam Finder dalam masa kira-kira seminit. Ada soalan atau maklum balas? E-mel kami di **support@everappz.com**.
