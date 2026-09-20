---
title: "Cara Menyiapkan Server SMB di iPhone & iPad untuk Berbagi File"
description: "Ubah iPhone atau iPad Anda jadi server file SMB dengan Everdisk dan bukalah seperti network drive dari Mac, iPhone lain, Linux, atau Android lewat Wi-Fi. Panduan lengkap, alamat serta port smb, enkripsi SMB3 opsional, dan langkah demi langkah koneksi untuk setiap perangkat."
date: 2026-09-19
tags: ["everdisk", "smb", "berbagi file", "network drive", "iphone", "ipad", "mac", "finder", "enkripsi", "wifi"]
keywords: ["server SMB iPhone", "server SMB iPad", "cara menyiapkan SMB di iPhone", "berbagi SMB iPhone", "sambungkan iPhone SMB Mac Finder", "smb iphone ke iphone", "aplikasi Files iOS sambung ke server SMB", "berbagi file iPhone SMB", "iphone network drive Finder", "enkripsi SMB3 iOS", "berbagi smb iPhone Android", "sambung ke SMB dari Linux", "iphone sebagai network drive", "berbagi file antar iphone wifi", "petakan iphone sebagai network drive"]
readingTime: 10
---

{{< author-byline >}}

SMB adalah fitur berbagi file yang tertanam di macOS, Windows, dan Linux, serta di hampir setiap network drive (NAS). Saat Anda menyambung ke folder bersama di komputer lain dan folder itu terbuka seperti disk biasa di Finder atau File Explorer, itulah SMB yang bekerja. Dengan [Everdisk](/products/everdisk) Anda bisa menempatkan berbagi SMB di iPhone atau iPad Anda, sehingga ponsel itu sendiri muncul sebagai network drive yang bisa dijelajahi, disalin darinya, dan disalin ke dalamnya oleh perangkat lain.

Inilah opsi yang perlu dituju saat Anda ingin iPhone berperilaku seperti drive sungguhan, bukan halaman web. Cepat, seret dan lepas ke dua arah, dan ini satu-satunya jenis koneksi di Everdisk yang bisa mengenkripsi setiap transfer. Panduan ini mencakup penyiapan serta cara menyambung dari Mac, iPhone atau iPad lain, Linux, Android, dan Windows.

## Yang Anda perlukan

- iPhone atau iPad dengan [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) terpasang.
- Perangkat lain di **jaringan Wi-Fi yang sama**.
- File yang ingin Anda bagikan, di folder Dokumen Everdisk atau di folder yang Anda tambahkan.

## Siapkan server SMB di Everdisk

### Langkah 1: Pilih apa yang dibagikan dan siapa yang bisa menulis

Buka Everdisk, masuk ke tab **Berbagi**, dan ketuk **Apa yang Dibagikan**. Folder Dokumen dibagikan secara bawaan. Tambahkan lebih banyak dengan **Tambah Folder** dan **Tambah Berkas**, dan aktifkan pustaka Foto atau Musik Anda jika ingin itu juga tersedia.

Putuskan apakah perangkat lain hanya bisa membaca file Anda, atau juga mengubahnya. Buka **Pengaturan**, lalu **Berbagi**, lalu **Akses**, dan atur **Pengeditan Berkas**. Dengan opsi ini aktif, perangkat yang terhubung bisa menyalin file ke ponsel Anda serta mengganti nama atau menghapusnya. Dengan opsi ini mati, berbagi bersifat hanya-baca.

Jika Anda ingin ada login, atur **Info Masuk** dan **Kata Sandi** di layar Akses yang sama. Biarkan keduanya kosong untuk mengizinkan akses tamu.

### Langkah 2: Aktifkan server SMB

Masuk ke **Pengaturan**, lalu **Berbagi**, lalu **Koneksi**, dan aktifkan **Komputer (Lanjutan)**. Itulah server SMB (membawa tag SMB).

### Langkah 3: Mulai berbagi dan catat alamatnya

Kembali ke tab **Berbagi** dan ketuk **Mulai**. Bagian **Cara Menghubungkan** kini menampilkan alamat SMB. Tampilannya seperti ini:

```
smb://192.168.1.20:4455/Share
```

Tiga hal yang perlu diketahui tentang alamat itu:

- Angka setelah titik dua adalah **port**. Everdisk memakai **4455** secara bawaan.
- Nama berbaginya adalah **Share**.
- Bagian pertama adalah alamat iPhone Anda di Wi-Fi, jadi akan berbeda di jaringan Anda.

Biarkan Everdisk tetap terbuka saat ada perangkat yang terhubung, karena iOS menjeda aplikasi yang terlalu lama berada di latar belakang.

## Sambung dari Mac

Ini kasus yang paling mulus, karena macOS berbicara SMB secara native.

Cara tercepat: buka **Finder** dan lihat di bilah samping bawah **Locations** atau **Network**. Everdisk mengumumkan dirinya di Wi-Fi, jadi iPhone Anda sering muncul di sana dengan sendirinya. Klik, lalu klik **Connect As** dan pilih **Guest**, atau masukkan login Anda.

Untuk menyambung secara manual:

1. Di Finder, pilih **Go**, lalu **Connect to Server** (atau tekan **Command dan K**).
2. Ketik alamat SMB yang ditampilkan di Everdisk, misalnya `smb://192.168.1.20:4455/Share`.
3. Klik **Connect**, lalu pilih **Guest** atau masukkan **Info Masuk** dan **Kata Sandi** Anda.

iPhone Anda terbuka di jendela Finder. Salin file masuk atau keluar dengan menyeret, persis seperti drive lainnya (jika Pengeditan Berkas aktif).

## Sambung dari iPhone atau iPad lain

iOS dan iPadOS bisa membuka berbagi SMB di aplikasi **Files** bawaan, yang membuat transfer antarponsel jadi rapi dan cepat.

Di perangkat kedua:

1. Buka aplikasi **Files**.
2. Ketuk tombol **more** (tiga titik, di kanan atas pada iPhone) dan pilih **Connect to Server**.
3. Masukkan alamat SMB dari Everdisk, misalnya `smb://192.168.1.20:4455/Share`.
4. Pilih **Guest**, atau **Registered User** lalu masukkan login Anda.
5. Berbaginya muncul di bawah Locations di Files. Jelajahi dan salin ke arah mana pun.

Anda juga bisa memakai tab **Perangkat** milik Everdisk di perangkat kedua, yang menyertakan klien SMB. Buka Everdisk, masuk ke **Perangkat**, ketuk **Koneksi Baru**, pilih **SMB**, lalu masukkan alamatnya.

## Sambung dari Linux

1. Buka pengelola file Anda (Files/Nautilus di GNOME, Dolphin di KDE).
2. Pilih **Other Locations** atau **Connect to Server**.
3. Masukkan alamatnya, misalnya `smb://192.168.1.20:4455/Share`.
4. Sambung sebagai tamu, atau masukkan login Anda.

Dari terminal Anda juga bisa menjalankan `smbclient //192.168.1.20/Share -p 4455` dan memasukkan login Anda saat diminta.

## Sambung dari Android

Android tidak punya browser SMB bawaan sistem, jadi gunakan pengelola file yang mendukung SMB:

1. Pasang aplikasi seperti **CX File Explorer**, **Solid Explorer**, atau **X-plore File Manager**.
2. Tambahkan koneksi **SMB** atau **LAN** baru.
3. Masukkan host (alamat Wi-Fi iPhone Anda), atur **port ke 4455**, dan nama berbagi **Share**.
4. Sambung sebagai tamu atau dengan login Anda, lalu jelajahi dan salin.

## Sambung dari Windows

Windows bisa membaca berbagi SMB, dengan satu kendala yang perlu diketahui sejak awal. File Explorer bawaan hanya berbicara SMB pada port standar dan tidak mengizinkan Anda mengetik port kustom di jalurnya, sedangkan Everdisk memakai port 4455. Jadi rute **Map network drive** polos sering kali tidak menjangkaunya.

Anda punya dua opsi bagus di Windows:

- Gunakan pengelola file atau klien SMB yang mengizinkan Anda mengatur port kustom, lalu arahkan ke alamat iPhone Anda dengan port **4455** dan nama berbagi **Share**.
- Atau sambung dari Windows menggunakan salah satu server Everdisk lainnya. [Penyiapan WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) dan [penyiapan FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) keduanya berfungsi baik dari Windows File Explorer, dan tautan browser berfungsi di browser apa pun.

Jika Anda tetap ingin mencoba Map network drive: buka **File Explorer**, klik kanan **This PC**, pilih **Map network drive**, dan masukkan host serta nama berbagi yang ditampilkan di Everdisk. Jika tidak bisa terhubung, itu karena batasan port di atas, jadi beralihlah ke WebDAV atau FTP.

## Aktifkan enkripsi untuk Wi-Fi yang tidak tepercaya

SMB adalah satu-satunya koneksi Everdisk yang bisa mengenkripsi setiap transfer, yang penting di Wi-Fi yang tidak sepenuhnya Anda kendalikan, seperti kafe atau jaringan kantor.

1. Di **Pengaturan**, **Berbagi**, **Akses**, atur **Info Masuk** dan **Kata Sandi**. Koneksi terenkripsi tidak bisa anonim, jadi langkah ini wajib.
2. Di **Pengaturan**, **Berbagi**, aktifkan **Wajibkan enkripsi SMB**.
3. Hentikan lalu mulai berbagi lagi agar perubahannya berlaku.

Setiap transfer SMB kemudian dilindungi dengan **enkripsi SMB3 (AES)**. Perangkat yang menyambung perlu mendukung SMB3, yang dimiliki Finder di Mac modern maupun Windows 10 atau yang lebih baru. Enkripsi SMB adalah bagian dari pembelian Premium sekali bayar.

## Hanya-baca atau baca dan tulis

Sakelar **Pengeditan Berkas** di Pengaturan, Berbagi, Akses mengendalikan ini untuk setiap server, termasuk SMB. Aktifkan dan perangkat yang terhubung bisa mengunggah, mengganti nama, dan menghapus. Matikan dan mereka hanya bisa menjelajah dan menyalin file dari ponsel Anda. Pilih hanya-baca saat Anda menyerahkan file kepada seseorang yang tidak ingin Anda beri kewenangan mengubah apa pun.

## Cara orang memakainya dalam kehidupan nyata

- **Pindahkan folder besar ke iPhone Anda dari Mac** dengan menyeretnya ke jendela Finder, lebih cepat daripada unggah lewat web.
- **Tarik foto dan video sehari penuh dari ponsel Anda** ke laptop tanpa iTunes atau kabel.
- **Kirim file antara dua iPhone** lewat aplikasi Files, tanpa aplikasi ketiga di sisi mana pun.
- **Kerjakan file di tempatnya**, membuka dokumen langsung dari ponsel di sebuah aplikasi di Mac Anda lalu menyimpannya kembali.

## Beberapa tips

- Biarkan Everdisk tetap terbuka saat sebuah perangkat terhubung. Mengunci ponsel dalam waktu lama bisa menjeda aplikasi dan memutus koneksi.
- Jika Mac tidak dapat melihat ponsel di bilah samping Finder, sambung secara manual dengan Connect to Server dan alamat smb lengkap.
- Untuk kecepatan terbaik pada transfer besar, jaga kualitas foto dan video pada Original di Pengaturan.
- Di jaringan yang tidak tepercaya, aktifkan Wajibkan enkripsi SMB dan matikan server lain selama Anda bekerja.

## Pertanyaan yang Sering Diajukan

{{% details title="Berapa alamat dan port SMB untuk iPhone saya?" closed="true" %}}
Setelah Anda mulai berbagi, Everdisk menampilkan alamatnya di layar Berbagi. Tampilannya seperti smb://192.168.1.20:4455/Share. Angka 4455 adalah port yang dipakai Everdisk untuk SMB, dan Share adalah nama folder yang dibagikan. Bagian pertama adalah alamat iPhone Anda di Wi-Fi, jadi milik Anda akan berbeda.
{{% /details %}}

{{% details title="Bisakah saya menyambung ke berbagi SMB iPhone dari Windows?" closed="true" %}}
Windows File Explorer hanya menyambung ke SMB pada port standar dan tidak menerima port kustom di jalurnya, sedangkan Everdisk memakai port 4455. Jadi rute Map network drive polos sering kali tidak menjangkaunya. Gunakan pengelola file yang mengizinkan Anda mengatur port kustom, atau sambung dari Windows dengan WebDAV, FTP, atau tautan browser sebagai gantinya. Semua itu berfungsi dari Windows tanpa masalah port.
{{% /details %}}

{{% details title="Bagaimana cara berbagi file antara dua iPhone dengan SMB?" closed="true" %}}
Mulai server SMB di iPhone pertama di Everdisk. Di iPhone kedua, buka aplikasi Files, ketuk tombol more, pilih Connect to Server, dan masukkan alamat smb yang ditampilkan di Everdisk (misalnya smb://192.168.1.20:4455/Share). Sambung sebagai Guest atau dengan login Anda, dan berbaginya muncul di Files. Anda juga bisa memakai tab Perangkat milik Everdisk di ponsel kedua.
{{% /details %}}

{{% details title="Apakah iPhone saya muncul di bilah samping Mac Finder secara otomatis?" closed="true" %}}
Biasanya ya. Everdisk mengumumkan berbagi SMB di Wi-Fi Anda, jadi iPhone Anda sering muncul di bawah Locations atau Network di bilah samping Finder. Klik dan pilih Connect As, lalu Guest atau login Anda. Jika tidak muncul, sambung secara manual dengan Go, Connect to Server dan alamat smb lengkap.
{{% /details %}}

{{% details title="Apakah saya perlu kata sandi untuk memakai SMB?" closed="true" %}}
Tidak, login bersifat opsional. Biarkan Info Masuk dan Kata Sandi kosong di Pengaturan, Berbagi, Akses untuk mengizinkan akses tamu. Atur keduanya jika Anda ingin koneksi masuk terlebih dahulu. Info masuk dan kata sandi hanya diperlukan jika Anda mengaktifkan Wajibkan enkripsi SMB, karena koneksi terenkripsi tidak bisa anonim.
{{% /details %}}

{{% details title="Apakah koneksi SMB terenkripsi?" closed="true" %}}
Bisa. SMB adalah satu-satunya koneksi Everdisk yang mendukung enkripsi. Atur info masuk dan kata sandi, lalu aktifkan Wajibkan enkripsi SMB di Pengaturan, Berbagi. Setiap transfer kemudian dilindungi dengan SMB3 (AES). Perangkat lain perlu mendukung SMB3, yang dimiliki Mac modern dan Windows 10 atau yang lebih baru. Enkripsi adalah fitur Premium.
{{% /details %}}

{{% details title="Bisakah orang mengubah atau menghapus file saya lewat SMB?" closed="true" %}}
Hanya jika Anda mengizinkannya. Sakelar Pengeditan Berkas di Pengaturan, Berbagi, Akses mengendalikan ini. Dengan aktif, perangkat yang terhubung bisa mengunggah, mengganti nama, dan menghapus. Dengan mati, berbaginya hanya-baca dan orang lain bisa menjelajah serta menyalin file dari ponsel Anda tetapi tidak bisa mengubah apa pun.
{{% /details %}}

{{% details title="Mengapa koneksi SMB saya terputus?" closed="true" %}}
iPhone Anda adalah server, dan iOS menjeda aplikasi yang terlalu lama berada di latar belakang. Biarkan Everdisk tetap terbuka di layar saat sebuah perangkat terhubung, dan colokkan ponsel ke sumber daya selama transfer yang panjang. Pastikan juga kedua perangkat tetap berada di Wi-Fi yang sama.
{{% /details %}}

{{% details title="SMB, WebDAV, atau FTP, mana yang harus saya pakai?" closed="true" %}}
Gunakan SMB saat Anda ingin ponsel berperilaku seperti network drive sungguhan di Mac, iPhone lain, Linux, atau NAS, dan saat Anda menginginkan enkripsi. Gunakan WebDAV saat Anda ingin network drive yang juga berfungsi baik dari Windows. Gunakan FTP untuk kompatibilitas terluas dengan perangkat dan aplikasi lawas. Everdisk bisa menjalankan semuanya sekaligus, jadi Anda tidak terkunci pada satu pilihan.
{{% /details %}}

{{% details title="Apakah Everdisk gratis?" closed="true" %}}
Ya, Everdisk gratis diunduh dan server SMB sudah termasuk. Pembelian Premium sekali bayar opsional menambahkan enkripsi SMB, port kustom, dan beberapa ekstra lain. Anda bisa menyiapkan SMB dan berbagi file tanpa membayar.
{{% /details %}}

Siap mencobanya? [Unduh Everdisk dari App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dan buka iPhone Anda di Finder dalam waktu sekitar satu menit. Ada pertanyaan atau masukan? Kirim email ke **support@everappz.com**.
</content>
