---
title: "Cara Menyiapkan Server FTP di iPhone & iPad untuk Transfer File"
description: "Ubah iPhone atau iPad Anda jadi server FTP dengan Everdisk dan transfer file dari Mac, PC Windows, Linux, Android, aplikasi FTP seperti FileZilla, atau iPhone lain lewat Wi-Fi. Panduan lengkap, alamat serta port ftp, akses tamu, dan langkah demi langkah koneksi untuk setiap perangkat."
date: 2026-09-19
tags: ["everdisk", "ftp", "transfer file", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["server FTP iPhone", "server FTP iPad", "cara menyiapkan FTP di iPhone", "aplikasi server ftp iphone", "sambungkan FileZilla ke iPhone", "Cyberduck iPhone FTP", "transfer file iPhone FTP", "ftp iphone ke komputer", "ftp iphone ke iphone", "sambung ke FTP iPhone dari Windows", "alamat port ftp iphone", "ftp anonim iphone", "berbagi file iphone ftp", "ftp iphone untuk kamera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP adalah andalan lama transfer file. Sudah ada selama beberapa dekade, dan justru itulah yang membuatnya begitu berguna: hampir apa pun yang bisa berbicara dengan server memahaminya. Kamera, smart TV, router, network drive, alat otomasi, dan setiap aplikasi FTP desktop berbicara FTP. Dengan [Everdisk](/products/everdisk) Anda bisa menjalankan server FTP di iPhone atau iPad Anda, sehingga ponsel menjadi tempat yang bisa disambungi perangkat dan aplikasi tersebut untuk memindahkan file.

Tuju FTP saat opsi lain tidak cocok, misalnya perangkat lawas atau aplikasi yang hanya tahu cara menyambung lewat FTP. Panduan ini mencakup penyiapan serta cara menyambung dari Mac, Windows, aplikasi FTP, Linux, Android, dan iPhone kedua.

## Yang Anda perlukan

- iPhone atau iPad dengan [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) terpasang.
- Komputer, aplikasi, atau perangkat di **jaringan Wi-Fi yang sama**.
- File yang ingin Anda bagikan, di folder Dokumen Everdisk atau di folder yang Anda tambahkan.

## Siapkan server FTP di Everdisk

### Langkah 1: Pilih apa yang dibagikan dan atur akses

Buka Everdisk, masuk ke tab **Berbagi**, dan ketuk **Apa yang Dibagikan**. Folder Dokumen dibagikan secara bawaan. Tambahkan lebih banyak dengan **Tambah Folder** dan **Tambah Berkas**.

Buka **Pengaturan**, lalu **Berbagi**, lalu **Akses**. Aktifkan **Pengeditan Berkas** jika Anda ingin orang bisa mengunggah, mengganti nama, dan menghapus, atau matikan untuk mengizinkan unduhan saja. Atur **Info Masuk** dan **Kata Sandi** jika Anda ingin ada masuk, atau biarkan keduanya kosong agar siapa pun bisa menyambung sebagai tamu.

### Langkah 2: Aktifkan server FTP

Masuk ke **Pengaturan**, lalu **Berbagi**, lalu **Koneksi**, dan aktifkan **Aplikasi dan perangkat lain**. Itulah server FTP (membawa tag FTP).

### Langkah 3: Mulai berbagi dan catat alamatnya

Kembali ke tab **Berbagi** dan ketuk **Mulai**. Bagian **Cara Menghubungkan** menampilkan alamat FTP. Tampilannya seperti ini:

```
ftp://192.168.1.20:2121
```

Angka setelah titik dua adalah **port**, yaitu **2121** secara bawaan. Bagian pertama adalah alamat iPhone Anda di Wi-Fi, jadi milik Anda akan berbeda. Biarkan Everdisk tetap terbuka di layar saat sebuah perangkat terhubung.

## Sambung dari Mac

1. Buka **Finder**, pilih **Go**, lalu **Connect to Server** (atau tekan **Command dan K**).
2. Ketik alamat FTP yang ditampilkan di Everdisk, misalnya `ftp://192.168.1.20:2121`.
3. Klik **Connect**, lalu pilih **Guest** atau masukkan **Info Masuk** dan **Kata Sandi** Anda.

Finder memasang berbagi FTP sehingga Anda bisa menjelajah dan menyalin file ke Mac Anda. Perhatikan bahwa Finder membuka FTP sebagai hanya-baca. Saat Anda ingin mengunggah dari Mac, gunakan aplikasi FTP seperti dijelaskan di bawah.

## Sambung dari Windows

1. Buka **File Explorer** dan klik bilah alamat di bagian atas.
2. Ketik alamat FTP dari Everdisk, misalnya `ftp://192.168.1.20:2121`, lalu tekan **Enter**.
3. Masukkan **Info Masuk** dan **Kata Sandi** Anda jika Anda mengaturnya, atau lanjutkan sebagai tamu.

File yang dibagikan muncul di jendela dan Anda bisa menyalinnya ke PC Anda.

## Sambung dengan aplikasi FTP (FileZilla, Cyberduck)

Untuk unggahan dan kendali penuh, aplikasi FTP adalah alat terbaik. **FileZilla** dan **Cyberduck** gratis dan berjalan di Windows, Mac, serta Linux.

1. Buka aplikasi dan buat koneksi baru.
2. Atur **Host** ke alamat Wi-Fi iPhone Anda, dan **Port** ke **2121**.
3. Untuk login, masukkan **Info Masuk** dan **Kata Sandi** Anda, atau pilih **Anonymous** jika Anda tidak mengaturnya.
4. Sambung, lalu seret file ke dua arah (unggahan memerlukan Pengeditan Berkas aktif).

## Sambung dari Linux

1. Buka pengelola file Anda dan pilih **Connect to Server** atau **Other Locations**.
2. Masukkan alamatnya, misalnya `ftp://192.168.1.20:2121`.
3. Sambung sebagai tamu atau dengan login Anda.

Anda juga bisa memakai klien FTP Linux apa pun dari terminal, mengarahkannya ke host dan port 2121 yang sama.

## Sambung dari Android

Android tidak punya browser FTP bawaan sistem, jadi gunakan aplikasi:

1. Pasang klien FTP seperti **AndFTP**, **FTPCafe**, atau pengelola file dengan dukungan FTP seperti **Solid Explorer**.
2. Tambahkan koneksi dengan host, **port 2121**, dan login Anda atau Anonymous.
3. Jelajahi dan transfer.

## Sambung dari iPhone atau iPad lain

Aplikasi Files iOS tidak menyertakan klien FTP, jadi gunakan salah satu dari ini di perangkat kedua:

- **Tab Perangkat milik Everdisk.** Buka Everdisk, masuk ke **Perangkat**, ketuk **Koneksi Baru**, pilih **FTP**, dan masukkan alamatnya, misalnya `ftp://192.168.1.20:2121`. Ini rute paling sederhana.
- **Aplikasi FTP khusus** untuk iOS, memakai host, port 2121, dan login yang sama.

## Sambungkan perangkat lain: kamera, TV, router, dan NAS

Di sinilah FTP bersinar. Banyak perangkat memiliki klien FTP bawaan yang bisa mengirim atau mengambil file:

- **Kamera** yang mengunggah foto lewat FTP bisa mengirimnya langsung ke iPhone Anda.
- **Smart TV, router, kotak NAS, dan alat otomasi** yang mendukung FTP bisa menyambung dengan cara yang sama.

Arahkan mereka ke alamat Wi-Fi iPhone Anda, port **2121**, dan login Anda (atau Anonymous), menggunakan alamat yang ditampilkan di Everdisk.

## Hanya-baca atau baca dan tulis

Sakelar **Pengeditan Berkas** di Pengaturan, Berbagi, Akses mengendalikan ini. Aktif membuat orang bisa mengunggah, mengganti nama, dan menghapus. Mati berarti mereka hanya bisa mengunduh. Pilih hanya-baca saat Anda membagikan file dan tidak ingin apa pun diubah di ponsel Anda.

## Cara orang memakainya dalam kehidupan nyata

- **Sambungkan FileZilla ke iPhone Anda** dan dorong sekumpulan file ke ponsel sekaligus.
- **Biarkan aplikasi atau perangkat lawas yang hanya berbicara FTP** menjangkau file Anda saat tidak ada yang lain mau menyambung.
- **Terima foto dari kamera** yang mengunggah lewat FTP.
- **Pindahkan file antara iPhone dan iPad** menggunakan tab Perangkat milik Everdisk di perangkat penerima.

## Beberapa tips

- Biarkan Everdisk tetap terbuka saat sebuah perangkat terhubung, karena iOS menjeda aplikasi latar belakang setelah beberapa saat.
- Untuk mengunggah dari Mac, gunakan FileZilla atau Cyberduck alih-alih Finder, karena Finder membuka FTP sebagai hanya-baca.
- Biarkan login kosong untuk kompatibilitas terluas, lalu sambung sebagai Anonymous, yang ditawarkan sebagian besar klien FTP.
- FTP tidak mengenkripsi lalu lintasnya. Di jaringan yang tidak Anda percayai, gunakan [server SMB dengan enkripsi](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) sebagai gantinya.

## Pertanyaan yang Sering Diajukan

{{% details title="Berapa alamat dan port FTP untuk iPhone saya?" closed="true" %}}
Setelah Anda mulai berbagi, Everdisk menampilkan alamatnya di layar Berbagi. Tampilannya seperti ftp://192.168.1.20:2121. Angka 2121 adalah port yang dipakai Everdisk untuk FTP, dan bagian pertama adalah alamat iPhone Anda di Wi-Fi, jadi milik Anda akan berbeda.
{{% /details %}}

{{% details title="Bagaimana cara menyambungkan FileZilla atau Cyberduck ke iPhone saya?" closed="true" %}}
Buka aplikasi dan buat koneksi baru. Atur Host ke alamat Wi-Fi iPhone Anda dan Port ke 2121. Masukkan Info Masuk dan Kata Sandi Anda, atau pilih Anonymous jika Anda tidak mengaturnya di Everdisk. Sambung, dan Anda bisa menyeret file ke dua arah saat Pengeditan Berkas aktif.
{{% /details %}}

{{% details title="Bisakah saya menyambung ke FTP iPhone dari Windows?" closed="true" %}}
Ya. Buka File Explorer, klik bilah alamat, ketik alamat FTP dari Everdisk (misalnya ftp://192.168.1.20:2121), lalu tekan Enter. Masukkan login Anda jika Anda mengaturnya, atau lanjutkan sebagai tamu. Untuk unggahan dan kendali lebih, gunakan aplikasi FTP seperti FileZilla sebagai gantinya.
{{% /details %}}

{{% details title="Apakah saya perlu login untuk FTP?" closed="true" %}}
Tidak, login bersifat opsional. Biarkan Info Masuk dan Kata Sandi kosong di Pengaturan, Berbagi, Akses, dan sambung sebagai Anonymous, yang ditawarkan sebagian besar klien FTP. Atur login jika Anda ingin koneksi masuk terlebih dahulu.
{{% /details %}}

{{% details title="Mengapa saya hanya bisa mengunduh dan tidak bisa mengunggah lewat FTP?" closed="true" %}}
Dua alasan yang umum. Pertama, sakelar Pengeditan Berkas di Pengaturan, Berbagi, Akses harus aktif untuk mengizinkan unggahan, penggantian nama, dan penghapusan. Kedua, Mac Finder membuka FTP sebagai hanya-baca, jadi gunakan aplikasi FTP seperti FileZilla atau Cyberduck saat Anda ingin mengunggah.
{{% /details %}}

{{% details title="Bisakah saya memakai FTP antara dua iPhone?" closed="true" %}}
Ya. Mulai server FTP di iPhone pertama. Di iPhone kedua, buka Everdisk, masuk ke tab Perangkat, ketuk Koneksi Baru, pilih FTP, dan masukkan alamat yang ditampilkan di ponsel pertama. Aplikasi FTP khusus untuk iOS juga berfungsi, karena aplikasi Files iOS tidak menyertakan klien FTP.
{{% /details %}}

{{% details title="Apakah FTP aman?" closed="true" %}}
FTP polos tidak mengenkripsi lalu lintasnya, jadi perlakukan sebagai alat untuk jaringan yang Anda percayai, seperti Wi-Fi rumah Anda. Di jaringan yang tidak Anda kendalikan, gunakan server SMB dengan Wajibkan enkripsi SMB diaktifkan, yang melindungi setiap transfer.
{{% /details %}}

{{% details title="Perangkat mana yang bisa menyambung lewat FTP?" closed="true" %}}
Hampir apa pun dengan klien FTP. Itu mencakup komputer Mac, Windows, dan Linux, aplikasi FTP seperti FileZilla dan Cyberduck, pengelola file Android, serta perangkat keras seperti kamera, smart TV, router, kotak NAS, dan alat otomasi. Jangkauan luas itulah alasan utama memilih FTP.
{{% /details %}}

{{% details title="Mengapa koneksi FTP saya terputus?" closed="true" %}}
iPhone Anda adalah server, dan iOS menjeda aplikasi yang terlalu lama berada di latar belakang. Biarkan Everdisk tetap terbuka di layar saat sebuah perangkat terhubung, dan colokkan ke sumber daya untuk transfer yang panjang. Pastikan juga kedua perangkat masih berada di Wi-Fi yang sama.
{{% /details %}}

{{% details title="Apakah Everdisk gratis?" closed="true" %}}
Ya, Everdisk gratis diunduh dan server FTP sudah termasuk. Pembelian Premium sekali bayar opsional menambahkan ekstra seperti port kustom serta konversi foto dan video. Anda bisa menyiapkan FTP dan mentransfer file tanpa membayar.
{{% /details %}}

Siap mencobanya? [Unduh Everdisk dari App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dan sambungkan klien FTP pertama Anda dalam beberapa menit. Ada pertanyaan atau masukan? Kirim email ke **support@everappz.com**.
</content>
