---
title: "Cara Menyediakan Pelayan FTP pada iPhone & iPad untuk Pemindahan Fail"
description: "Jadikan iPhone atau iPad anda pelayan FTP dengan Everdisk dan pindahkan fail daripada Mac, PC Windows, Linux, Android, aplikasi FTP seperti FileZilla, atau iPhone lain melalui Wi-Fi. Penyediaan penuh, alamat dan port ftp, akses tetamu, dan sambungan langkah demi langkah untuk setiap peranti."
date: 2026-09-19
tags: ["everdisk", "ftp", "pemindahan fail", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["pelayan FTP iPhone", "pelayan FTP iPad", "cara menyediakan FTP pada iPhone", "aplikasi pelayan ftp iphone", "sambung FileZilla ke iPhone", "Cyberduck iPhone FTP", "pindah fail iPhone FTP", "ftp iphone ke komputer", "ftp iphone ke iphone", "sambung ke FTP iPhone dari Windows", "alamat port ftp iphone", "ftp tanpa nama iphone", "kongsi fail iphone ftp", "iphone ftp untuk kamera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP ialah kaedah lama yang boleh dipercayai untuk pemindahan fail. Ia telah wujud selama beberapa dekad, dan itulah tepatnya sebab ia sangat berguna: hampir apa sahaja yang boleh bercakap dengan pelayan memahaminya. Kamera, TV pintar, penghala, pemacu rangkaian, alat automasi dan setiap aplikasi FTP desktop memahami FTP. Dengan [Everdisk](/products/everdisk) anda boleh menjalankan pelayan FTP pada iPhone atau iPad anda, jadi telefon menjadi tempat yang boleh disambung oleh peranti dan aplikasi tersebut untuk memindahkan fail.

Capai FTP apabila pilihan lain tidak sesuai, contohnya peranti lama atau aplikasi yang hanya tahu cara menyambung melalui FTP. Panduan ini merangkumi penyediaan dan cara menyambung daripada Mac, Windows, aplikasi FTP, Linux, Android dan iPhone kedua.

## Apa yang anda perlukan

- Sebuah iPhone atau iPad dengan [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dipasang.
- Sebuah komputer, aplikasi atau peranti pada **rangkaian Wi-Fi yang sama**.
- Fail yang anda mahu kongsi, dalam folder Dokumen Everdisk atau dalam folder yang anda tambah.

## Sediakan pelayan FTP dalam Everdisk

### Langkah 1: Pilih apa untuk dikongsi dan tetapkan akses

Buka Everdisk, pergi ke tab **Perkongsian**, dan ketik **Apa untuk Dikongsi**. Folder Dokumen dikongsi secara lalai. Tambah lagi dengan **Tambah Folder** dan **Tambah Fail**.

Buka **Tetapan**, kemudian **Perkongsian**, kemudian **Akses**. Hidupkan **Penyuntingan Fail** jika anda mahu orang memuat naik, menamakan semula dan memadam, atau matikannya untuk membenarkan muat turun sahaja. Tetapkan **Log Masuk** dan **Kata Laluan** jika anda mahu log masuk, atau biarkannya kosong supaya sesiapa sahaja boleh menyambung sebagai tetamu.

### Langkah 2: Hidupkan pelayan FTP

Pergi ke **Tetapan**, kemudian **Perkongsian**, kemudian **Sambungan**, dan hidupkan **Apl dan peranti lain**. Itulah pelayan FTP (ia membawa tag FTP).

### Langkah 3: Mula berkongsi dan catat alamat

Kembali ke tab **Perkongsian** dan ketik **Mula**. Bahagian **How to Connect** menunjukkan alamat FTP. Ia kelihatan seperti ini:

```
ftp://192.168.1.20:2121
```

Nombor selepas titik bertindih ialah **port**, iaitu **2121** secara lalai. Bahagian pertama ialah alamat iPhone anda pada Wi-Fi, jadi milik anda akan berbeza. Kekalkan Everdisk terbuka pada skrin semasa peranti disambung.

## Sambung daripada Mac

1. Buka **Finder**, pilih **Go**, kemudian **Connect to Server** (atau tekan **Command dan K**).
2. Taip alamat FTP yang ditunjukkan dalam Everdisk, contohnya `ftp://192.168.1.20:2121`.
3. Klik **Connect**, kemudian pilih **Guest** atau masukkan **Log Masuk** dan **Kata Laluan** anda.

Finder melekapkan perkongsian FTP supaya anda boleh melayari dan menyalin fail ke Mac anda. Ambil perhatian bahawa Finder membuka FTP sebagai baca sahaja. Apabila anda mahu memuat naik daripada Mac, gunakan aplikasi FTP seperti yang diterangkan di bawah.

## Sambung daripada Windows

1. Buka **File Explorer** dan klik bar alamat di bahagian atas.
2. Taip alamat FTP daripada Everdisk, contohnya `ftp://192.168.1.20:2121`, dan tekan **Enter**.
3. Masukkan **Log Masuk** dan **Kata Laluan** anda jika anda menetapkannya, atau teruskan sebagai tetamu.

Fail kongsi muncul dalam tetingkap dan anda boleh menyalinnya ke PC anda.

## Sambung dengan aplikasi FTP (FileZilla, Cyberduck)

Untuk muat naik dan kawalan penuh, aplikasi FTP ialah alat terbaik. **FileZilla** dan **Cyberduck** adalah percuma dan berjalan pada Windows, Mac dan Linux.

1. Buka aplikasi dan cipta sambungan baharu.
2. Tetapkan **Host** kepada alamat Wi-Fi iPhone anda, dan **Port** kepada **2121**.
3. Untuk log masuk, masukkan **Log Masuk** dan **Kata Laluan** anda, atau pilih **Anonymous** jika anda tidak menetapkannya.
4. Sambung, dan seret fail ke dua-dua arah (muat naik memerlukan Penyuntingan Fail dihidupkan).

## Sambung daripada Linux

1. Buka pengurus fail anda dan pilih **Connect to Server** atau **Other Locations**.
2. Masukkan alamat, contohnya `ftp://192.168.1.20:2121`.
3. Sambung sebagai tetamu atau dengan log masuk anda.

Anda juga boleh menggunakan mana-mana klien FTP Linux daripada terminal, menghalakannya ke hos dan port 2121 yang sama.

## Sambung daripada Android

Android tidak mempunyai pelayar FTP sistem, jadi gunakan sebuah aplikasi:

1. Pasang klien FTP seperti **AndFTP**, **FTPCafe**, atau pengurus fail dengan sokongan FTP seperti **Solid Explorer**.
2. Tambah sambungan dengan hos, **port 2121**, dan log masuk anda atau Anonymous.
3. Layari dan pindahkan.

## Sambung daripada iPhone atau iPad lain

Aplikasi Files iOS tidak menyertakan klien FTP, jadi gunakan salah satu daripada ini pada peranti kedua:

- **Tab Peranti milik Everdisk.** Buka Everdisk, pergi ke **Peranti**, ketik **Sambungan Baharu**, pilih **FTP**, dan masukkan alamat, contohnya `ftp://192.168.1.20:2121`. Inilah cara paling mudah.
- **Aplikasi FTP khusus** untuk iOS, menggunakan hos, port 2121 dan log masuk yang sama.

## Sambung peralatan lain: kamera, TV, penghala dan NAS

Di sinilah FTP bersinar. Banyak peranti mempunyai klien FTP terbina yang boleh menghantar atau mengambil fail:

- **Kamera** yang memuat naik foto melalui FTP boleh menghantarnya terus ke iPhone anda.
- **TV pintar, penghala, kotak NAS dan alat automasi** yang menyokong FTP boleh menyambung dengan cara yang sama.

Halakan mereka ke alamat Wi-Fi iPhone anda, port **2121**, dan log masuk anda (atau Anonymous), menggunakan alamat yang ditunjukkan dalam Everdisk.

## Baca sahaja atau baca dan tulis

Suis **Penyuntingan Fail** dalam Tetapan, Perkongsian, Akses mengawal ini. Dihidupkan membenarkan orang memuat naik, menamakan semula dan memadam. Dimatikan bermakna mereka hanya boleh memuat turun. Pilih baca sahaja apabila anda menyerahkan fail dan tidak mahu apa-apa diubah pada telefon anda.

## Cara sebenar orang menggunakan ini

- **Sambung FileZilla ke iPhone anda** dan tolak sekumpulan fail ke telefon dalam satu langkah.
- **Biarkan aplikasi atau peranti lama yang hanya memahami FTP** mencapai fail anda apabila tiada apa lagi yang boleh menyambung.
- **Terima foto daripada kamera** yang memuat naik melalui FTP.
- **Pindahkan fail antara iPhone dan iPad** menggunakan tab Peranti Everdisk pada peranti penerima.

## Beberapa petua

- Kekalkan Everdisk terbuka semasa peranti disambung, kerana iOS menjeda aplikasi latar belakang selepas seketika.
- Untuk memuat naik daripada Mac, gunakan FileZilla atau Cyberduck berbanding Finder, kerana Finder membuka FTP sebagai baca sahaja.
- Biarkan log masuk kosong untuk keserasian paling luas, kemudian sambung sebagai Anonymous, yang ditawarkan oleh kebanyakan klien FTP.
- FTP tidak menyulitkan trafiknya. Pada rangkaian yang anda tidak percayai, gunakan [pelayan SMB dengan penyulitan](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) sebagai ganti.

## Soalan Lazim

{{% details title="Apakah alamat dan port FTP untuk iPhone saya?" closed="true" %}}
Selepas anda mula berkongsi, Everdisk menunjukkan alamat pada skrin Perkongsian. Ia kelihatan seperti ftp://192.168.1.20:2121. 2121 ialah port yang Everdisk gunakan untuk FTP, dan bahagian pertama ialah alamat iPhone anda pada Wi-Fi, jadi milik anda akan berbeza.
{{% /details %}}

{{% details title="Bagaimana saya sambung FileZilla atau Cyberduck ke iPhone saya?" closed="true" %}}
Buka aplikasi dan cipta sambungan baharu. Tetapkan Host kepada alamat Wi-Fi iPhone anda dan Port kepada 2121. Masukkan Log Masuk dan Kata Laluan anda, atau pilih Anonymous jika anda tidak menetapkannya dalam Everdisk. Sambung, dan anda boleh menyeret fail ke dua-dua arah apabila Penyuntingan Fail dihidupkan.
{{% /details %}}

{{% details title="Boleh saya sambung ke FTP iPhone saya daripada Windows?" closed="true" %}}
Ya. Buka File Explorer, klik bar alamat, taip alamat FTP daripada Everdisk (contohnya ftp://192.168.1.20:2121), dan tekan Enter. Masukkan log masuk anda jika anda menetapkannya, atau teruskan sebagai tetamu. Untuk muat naik dan lebih kawalan, gunakan aplikasi FTP seperti FileZilla sebagai ganti.
{{% /details %}}

{{% details title="Perlukah saya log masuk untuk FTP?" closed="true" %}}
Tidak, log masuk adalah pilihan. Biarkan Log Masuk dan Kata Laluan kosong dalam Tetapan, Perkongsian, Akses, dan sambung sebagai Anonymous, yang ditawarkan oleh kebanyakan klien FTP. Tetapkan log masuk jika anda mahu sambungan log masuk dahulu.
{{% /details %}}

{{% details title="Mengapa saya hanya boleh memuat turun dan tidak memuat naik melalui FTP?" closed="true" %}}
Dua sebab yang biasa. Pertama, suis Penyuntingan Fail dalam Tetapan, Perkongsian, Akses mesti dihidupkan untuk membenarkan muat naik, penamaan semula dan pemadaman. Kedua, Mac Finder membuka FTP sebagai baca sahaja, jadi gunakan aplikasi FTP seperti FileZilla atau Cyberduck apabila anda mahu memuat naik.
{{% /details %}}

{{% details title="Boleh saya guna FTP antara dua iPhone?" closed="true" %}}
Ya. Mula pelayan FTP pada iPhone pertama. Pada iPhone kedua, buka Everdisk, pergi ke tab Peranti, ketik Sambungan Baharu, pilih FTP, dan masukkan alamat yang ditunjukkan pada telefon pertama. Aplikasi FTP khusus untuk iOS turut berfungsi, kerana aplikasi Files iOS tidak menyertakan klien FTP.
{{% /details %}}

{{% details title="Adakah FTP selamat?" closed="true" %}}
FTP biasa tidak menyulitkan trafiknya, jadi anggaplah ia sebagai alat untuk rangkaian yang anda percayai, seperti Wi-Fi rumah anda. Pada rangkaian yang anda tidak kawal, gunakan pelayan SMB dengan Wajibkan penyulitan SMB dihidupkan, yang melindungi setiap pemindahan.
{{% /details %}}

{{% details title="Peranti mana yang boleh menyambung melalui FTP?" closed="true" %}}
Hampir apa sahaja dengan klien FTP. Itu termasuk komputer Mac, Windows dan Linux, aplikasi FTP seperti FileZilla dan Cyberduck, pengurus fail Android, dan perkakasan seperti kamera, TV pintar, penghala, kotak NAS dan alat automasi. Jangkauan luas itu ialah sebab utama untuk memilih FTP.
{{% /details %}}

{{% details title="Mengapa sambungan FTP saya terputus?" closed="true" %}}
iPhone anda ialah pelayan, dan iOS menjeda aplikasi yang berada di latar belakang terlalu lama. Kekalkan Everdisk terbuka pada skrin semasa peranti disambung, dan palamkan ke sumber kuasa untuk pemindahan yang panjang. Pastikan juga kedua-dua peranti masih berada pada Wi-Fi yang sama.
{{% /details %}}

{{% details title="Adakah Everdisk percuma?" closed="true" %}}
Ya, Everdisk percuma untuk dimuat turun dan pelayan FTP disertakan. Pembelian Premium sekali sahaja pilihan menambah tambahan seperti port tersuai dan penukaran foto dan video. Anda boleh menyediakan FTP dan memindahkan fail tanpa membayar.
{{% /details %}}

Sedia untuk mencuba? [Muat turun Everdisk dari App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dan sambung klien FTP pertama anda dalam masa beberapa minit. Ada soalan atau maklum balas? E-mel kami di **support@everappz.com**.
