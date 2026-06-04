---
title: "Koneksi"
date: 2020-02-01
description: "Pelajari cara menghubungkan penyimpanan cloud, NAS, dan komputer Anda ke Evertag. Akses dan edit file audio langsung dari penyimpanan cloud, NAS pribadi, atau Mac/PC."
keywords: [
  "pengaturan cloud Evertag", "menghubungkan iCloud ke Evertag", "akses file SMB iOS",
  "editor tag audio WebDAV", "pengeditan metadata NAS", "Wi-Fi Drive Evertag",
  "transfer file audio ke iPhone", "Evertag iTunes File Sharing", "edit tag FLAC dari cloud"
]
tags: ["panduan", "evertag", "koneksi"]
readingTime: 11
---


Di layar ini, Anda dapat menghubungkan berbagai sumber yang berisi file audio Anda. Anda dapat mengintegrasikan layanan cloud populer seperti Google Drive, Dropbox, OneDrive, iCloud, dan lainnya, serta menghubungkan Mac atau PC Anda. Selain itu, Anda memiliki opsi untuk mengedit file audio yang terletak di Apple Time Capsule, WD Cloud Home, atau NAS apa pun yang mendukung SMB atau WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Koneksi Evertag" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Akses cepat

Di bagian atas layar Koneksi Anda akan menemukan daftar **Akses cepat**. Folder cloud apa pun yang Anda tambahkan ke favorit — bahkan yang tersembunyi beberapa level — muncul di sini sehingga Anda dapat langsung menuju ke sana tanpa menavigasi melalui folder induk setiap saat.

## Hubungkan ke penyimpanan cloud

- Buka tab 'Koneksi'  
- Pilih 'Hubungkan ke penyimpanan cloud' dari menu  
- Pilih layanan penyimpanan cloud dari daftar  
- Masukkan kredensial Anda, dan ketuk 'Selesai.'

Jika Anda menemui masalah, pastikan untuk memeriksa koneksi internet dan login/kata sandi Anda.  
Dalam versi Premium aplikasi, Anda dapat menambahkan layanan dalam jumlah tak terbatas.

## Layanan penyimpanan cloud yang didukung

Saat ini, aplikasi mendukung layanan penyimpanan cloud paling populer: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), serta server SMB atau WebDAV apa pun.

## Keamanan dan privasi

Kami hanya menggunakan SDK resmi dan koneksi aman untuk berinteraksi dengan layanan cloud yang terhubung. Login dan kata sandi Anda tidak dapat diakses oleh aplikasi. Semua permintaan dari aplikasi ke layanan cloud dienkripsi.

Saat Anda memasukkan login dan kata sandi, aplikasi menampilkan halaman otorisasi resmi yang disediakan oleh penyedia layanan cloud, dan seluruh proses otorisasi terjadi di luar aplikasi. Penyedia layanan cloud mengirimkan token auth ke aplikasi setelah otorisasi berhasil, dan token tersebut digunakan untuk melakukan panggilan API.

Token auth adalah kunci digital yang memungkinkan aplikasi pihak ketiga berinteraksi dengan penyimpanan cloud. Token auth disimpan di perangkat Anda dalam penyimpanan sistem aman yang disebut Keychain. Anda dapat mengunduh file dari layanan cloud yang terhubung ke perangkat, dan file tersebut akan ditempatkan di direktori "Documents" aplikasi. Anda dapat menghapus file tersebut kapan saja menggunakan pengelola file bawaan.

Aplikasi tidak berbagi informasi apa pun dari akun cloud yang terhubung. Anda dapat mencabut akses ke akun cloud Anda kapan saja dengan membuka halaman pengaturan akun di browser web Anda.

## Tolak auth-token

Masuk ke akun Anda di browser web dan navigasikan ke halaman pengaturan. Di sana, Anda dapat menemukan semua aplikasi pihak ketiga yang terhubung ke akun cloud Anda dan menghapus salah satunya jika Anda tidak ingin lagi menggunakan aplikasi tersebut. Instruksi terperinci tersedia [di sini](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Anda juga dapat memutuskan koneksi akun cloud yang terhubung di aplikasi, dan token auth juga akan dihapus dari perangkat Anda. Jika Anda menghapus aplikasi dari perangkat, semua data yang diunduh dan token akses juga akan dihapus.

## Putuskan koneksi penyimpanan cloud atau ubah konfigurasi

- Akses Opsi Penyimpanan Cloud: Pertama, temukan penyimpanan cloud yang ingin Anda kelola di dalam antarmuka aplikasi.  
- Ketuk tombol '...': Di sebelah judul layanan, Anda akan melihat tombol '...'. Ketuk untuk mengakses opsi tambahan.  
  - **Ganti Nama**: Jika Anda ingin mengubah nama layanan cloud seperti yang muncul di daftar Anda, pilih 'Ganti Nama.'  
  - **Pengaturan**: Untuk mengubah konfigurasi atau data autentikasi layanan cloud, pilih 'Pengaturan.' Terkadang, Anda mungkin perlu mengotorisasi ulang layanan cloud yang terhubung jika token otorisasi telah kedaluwarsa.  
  - **Putuskan Koneksi**: Jika Anda ingin benar-benar memutus koneksi antara aplikasi dan layanan cloud, pilih 'Putuskan Koneksi.' Perlu diketahui bahwa memilih opsi ini akan menghapus semua lagu yang terkait dengan layanan cloud ini dari perpustakaan musik aplikasi Anda, tetapi lagu tersebut akan tetap ada di server.

## Hubungkan ke Komputer atau NAS

Anda juga dapat menghubungkan komputer, NAS pribadi, atau perangkat jaringan lainnya menggunakan protokol SMB, DLNA, atau WebDAV.

## Hubungkan ke komputer menggunakan SMB

- Ketuk "Hubungkan ke penyimpanan cloud" → SMB.  
- Masukkan alamat IP komputer dan nama folder bersama di kolom URL menggunakan format smb://computer-ip-address/shared-folder-name  
- Pilih versi protokol: Auto, SMB1, SMB2  
- Masukkan login dan kata sandi (jika diperlukan)  
- Ketuk "Selesai."

Jika koneksi berhasil, Anda akan melihat penyimpanan yang terhubung di bagian "Penyimpanan cloud."  
Tutorial lengkap tentang cara menghubungkan Mac atau PC menggunakan SMB tersedia [di sini](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Hubungkan ke NAS menggunakan WebDAV

Semua langkahnya sama kecuali kolom URL.  
URL harus dalam format http://server-name, atau https://server-name jika server mendukung SSL.  
Tutorial lengkap tentang cara menghubungkan NAS menggunakan protokol WebDAV tersedia [di sini](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Perangkat yang tersedia

Bagian ini menampilkan semua perangkat dalam jaringan lokal Anda yang dapat Anda hubungkan melalui aplikasi.  
Untuk membuat koneksi dengan perangkat, ikuti langkah-langkah berikut:

- Buka aplikasi dan pergi ke bagian "Perangkat yang Tersedia".  
- Ketuk perangkat yang ingin Anda hubungkan dari daftar.  
- Jika diperlukan, masukkan detail login Anda untuk menyelesaikan koneksi.

## Wi-Fi Drive 

Wi-Fi Drive adalah teknologi yang memungkinkan transfer file nirkabel dari komputer ke perangkat iOS melalui browser desktop.  
Untuk menggunakan fitur ini secara efektif, pastikan perangkat dan komputer Anda terhubung ke jaringan Wi-Fi yang sama.  
Berikut panduan langkah demi langkah tentang cara menggunakan Wi-Fi Drive.

## Aktifkan Wi-Fi Drive

- Buka aplikasi dan pergi ke tab "Koneksi".  
- Pilih "Hubungkan melalui Wi-Fi" untuk mengakses layar utama Wi-Fi Drive.  
- Ketuk "Mulai Wi-Fi Drive" untuk mengaktifkan Wi-Fi Drive.

## Akses Wi-Fi Drive di Komputer Anda

- Di komputer Anda (desktop atau laptop), buka browser web (seperti Chrome, Firefox, atau Safari).  
- Di bilah alamat browser, masukkan URL yang disediakan oleh aplikasi.

## Transfer File Secara Nirkabel

Setelah halaman web yang sesuai dengan perangkat iOS Anda terbuka di browser, Anda dapat dengan mudah menyeret dan menjatuhkan file dari komputer ke halaman web.  
File yang Anda seret dan jatuhkan akan mulai ditransfer ke perangkat iOS Anda dan akan dapat diakses dalam aplikasi.

Instruksi terperinci tentang cara transfer file secara nirkabel menggunakan Wi-Fi Drive tersedia [di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing adalah teknologi lain yang memungkinkan Anda mentransfer file dari komputer ke perangkat menggunakan aplikasi Finder di Mac dan kabel Lightning.  
- Cukup hubungkan perangkat ke komputer menggunakan kabel dan jalankan aplikasi Finder di Mac Anda.  
- Buka "Lokasi" → "Perangkat yang Terhubung" → "File" → dan temukan aplikasi saat ini.  
- Ketuk ikon aplikasi untuk melihat semua folder bersama.  
- Salin file dari komputer ke folder bersama di perangkat menggunakan seret dan jatuhkan.

Instruksi terperinci tentang cara menggunakan iTunes File Sharing tersedia [di sini](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Hubungkan kartu flash USB

Jika Anda memiliki kartu SD atau USB stick, Anda dapat menghubungkannya menggunakan pembaca kartu Lightning atau USB-C di iPhone/iPad, atau langsung menancapkannya ke Mac. Aplikasi saat ini mendukung pembaca kartu bersertifikat Apple. Kami memiliki instruksi terperinci tentang cara menghubungkan kartu flash USB ke iPhone atau iPad dan mengelola file di dalamnya, tersedia [di sini](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Drive yang terhubung muncul di bagian **Aksesori terhubung** di layar Koneksi.

## Pengelola File

Setelah menghubungkan layanan penyimpanan cloud, ketuk ikonnya untuk melihat semua file dan folder yang tersedia. Anda dapat menggunakan pengelola file bawaan untuk bekerja dengan file-file ini — unduh, ganti nama, pindahkan, dan lainnya. Saat Anda memulai unduhan, file akan muncul di antrian transfer. Untuk melihat antrian transfer, buka tab "File Lokal" dan ketuk panah berputar di sudut kiri atas. Semua file dan folder yang diunduh tersedia di bagian "File Lokal".

## Toolbar Atas

Toolbar atas yang berada di bawah bilah navigasi menawarkan beberapa tindakan berguna untuk kemudahan akses. Anda dapat menampilkan atau menyembunyikan toolbar ini dengan gerakan geser ke bawah. Berikut tindakan yang tersedia:

- **Cari**: Opsi ini memungkinkan Anda melakukan pencarian cepat di direktori saat ini, memudahkan menemukan file atau folder tertentu.  

## Opsi Folder

Saat Anda membuka folder di dalam aplikasi, Anda akan menemukan serangkaian tindakan tersedia dengan mengetuk tombol "..." di sudut kanan atas layar.  
Berikut rincian tindakan tersebut:

- **Pilih**: Aktifkan mode pemilihan file. Mode ini memungkinkan Anda memilih satu atau lebih file di dalam folder.  
- **Folder Baru**: Buat folder baru di dalam folder saat ini. Fitur ini memungkinkan Anda mengatur file dan menjaga perpustakaan tetap terstruktur.  
- **Unggah File**: Unggah file dari perangkat Anda ke folder online. Tindakan ini memungkinkan Anda mentransfer file ke cloud atau server.  
- **Cari**: Cari file tertentu di dalam folder saat ini.  
- **Urutkan**: Urutkan file di dalam folder berdasarkan kriteria seperti nama, ukuran, atau tanggal diedit.  
- **Tampilan Kisi/Daftar**: Beralih antara dua mode tampilan: tampilan tabel dan tampilan thumbnail.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pengurutan Folder Cloud Evertag" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Edit File Online

Saat Anda perlu mengelola beberapa file dalam penyimpanan cloud di aplikasi ini, Anda dapat menggunakan mode pilih untuk menyederhanakan tindakan Anda. Ikuti langkah-langkah berikut untuk manajemen file yang efektif:

- **Aktifkan Mode Pemilihan**: Buka aplikasi di perangkat Anda dan navigasikan ke bagian yang berisi penyimpanan cloud Anda. Cari sudut kanan atas di mana Anda akan menemukan tombol "..." (elipsis). Ketuk dan pilih item menu "Pilih" untuk mengaktifkan mode pemilihan.  
- **Pilih File**: Anda akan melihat kotak centang muncul di sebelah setiap file atau folder yang terdaftar. Pilih satu atau beberapa file atau folder dengan mengetuk kotak centang di sebelahnya.  
- **Lakukan Berbagai Tindakan**: Setelah Anda memilih file atau folder yang ingin dikelola, Anda akan memiliki akses ke beberapa tindakan:

{{< cards cols="1">}}
  {{< card title="" subtitle="Pemilihan File Evertag" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Tindakan file

Di dekat judul file, Anda akan melihat simbol elipsis "..." (tiga titik) – ini berfungsi sebagai menu tindakan.  
Ketuk untuk menampilkan daftar tindakan yang tersedia:

- **Mengedit tag audio**: Dengan memilih opsi ini, Anda dapat mengakses editor tag bawaan, memungkinkan Anda memodifikasi tag audio untuk file yang dipilih. File akan diunduh sementara ke direktori sementara dan kemudian diunggah ke penyimpanan setelah Anda mengkonfirmasi perubahan.  
- **Tambahkan ke Favorit**: Tindakan ini menambahkan file ke daftar file favorit Anda untuk akses cepat dan mudah.  
- **Unduh**: Pilih tindakan ini untuk mengunduh file atau folder ke perangkat Anda, membuatnya dapat diakses secara offline.  
- **Ganti Nama**: Opsi ini memungkinkan Anda mengganti nama file langsung di penyimpanan jarak jauh.  
- **Pindahkan**: Pilih tindakan ini untuk memindahkan file ke folder lain di dalam penyimpanan cloud Anda.  
- **Buka Di**: Gunakan tindakan ini untuk mengekspor file ke aplikasi lain yang kompatibel. File akan diunduh ke perangkat Anda, dan kemudian dialog Berbagi akan muncul.  
- **Hapus**: Berhati-hatilah dengan tindakan ini, karena secara permanen menghapus file dari penyimpanan cloud Anda. **Penghapusan ini tidak dapat dibatalkan**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opsi File Evertag" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Jika daftar tindakan melebihi ruang layar yang tersedia, cukup gulir ke bawah dalam menu tindakan untuk mengakses opsi tambahan.

## Tindakan folder

Untuk setiap folder di penyimpanan cloud Anda, berbagai tindakan tersedia. Untuk mengakses opsi ini, cukup ketuk ikon elipsis "..." yang terletak di sebelah judul folder. Jika Anda tidak melihat semua tindakan, gulir ke bawah untuk mengungkapkan lebih banyak pilihan. Berikut tindakan yang tersedia:

- **Tambahkan ke Favorit**: Gunakan tindakan ini untuk menambahkan folder ke daftar file favorit Anda untuk akses cepat dan mudah.  
- **Unduh**: Unduh semua isi folder ke perangkat Anda untuk akses offline.  
- **Ganti Nama**: Ganti nama folder langsung di penyimpanan jarak jauh.  
- **Pindahkan**: Pindahkan folder ke lokasi lain di dalam penyimpanan cloud Anda.  
- **Hapus**: Berhati-hatilah dengan tindakan ini, karena secara permanen menghapus folder dan isinya dari penyimpanan cloud Anda. **Tindakan ini tidak dapat dibatalkan**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opsi Folder Evertag" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
