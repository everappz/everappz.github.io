---
title: "File"
date: 2020-02-01
lastmod: 2026-06-01
description: "Pelajari cara menggunakan tab File di Evervideo di iPhone, iPad, dan Mac. Hubungkan layanan cloud, perangkat NAS, server media, dan stream RTSP di satu tempat. Kelola video offline, antrean transfer, unduhan, Wi-Fi Drive, iTunes / Finder File Sharing, dan drive USB. Termasuk iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA, dan penyimpanan kompatibel S3."
keywords: [
  "file Evervideo", "koneksi Evervideo", "file lokal Evervideo",
  "pengaturan video cloud iPhone", "menghubungkan Google Drive video", "streaming video SMB",
  "pemutar video WebDAV iOS", "video DLNA iPhone", "streaming video NAS",
  "transfer video Wi-Fi Drive", "iTunes File Sharing Evervideo", "RTSP iPhone",
  "Plex Evervideo", "Jellyfin Evervideo", "Emby Evervideo",
  "Subsonic Evervideo", "Navidrome Evervideo",
  "mode offline video Evervideo", "antrean transfer Evervideo",
  "manajer file Evervideo", "folder Dokumen Evervideo",
  "pemutar video Synology", "pemutar video QNAP",
  "pemutar video Apple Time Capsule", "USB DAC video",
  "pemutar video iXpand", "pemutar video S3"
]
tags: ["panduan", "evervideo", "file", "koneksi", "cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Tab File adalah manajer file all-in-one Evervideo. Tidak seperti kebanyakan aplikasi video yang memisahkan penyimpanan cloud dari file lokal ke tab yang berbeda, Evervideo menggabungkan keduanya ke dalam satu layar yang dapat digulir sehingga Anda dapat beralih dari server Plex ke folder cloud ke folder Dokumen iPhone tanpa berpindah tab.

Tab File dibagi menjadi bagian-bagian yang jelas yang muncul dalam urutan ini di layar Anda:

- **Akses Cepat** — terbaru dan favorit untuk file dan folder yang paling baru Anda buka.
- **File di Aplikasi Ini** — apa yang ada di folder Dokumen terisolasi Evervideo.
- **File di iPhone / iPad / Mac Ini** — video di tempat lain di perangkat Anda, yang ditampilkan melalui pemilih file sistem.
- **Penyimpanan Cloud** — setiap akun cloud, NAS, dan server media yang telah Anda hubungkan.
- **Perangkat yang Tersedia** — server dan drive yang ditemukan secara otomatis oleh Bonjour / mDNS di jaringan lokal Anda.

Di pojok kanan atas layar File terdapat tombol Transfer (ikon panah berputar). Ketuk untuk membuka Antrean Transfer tempat Anda memantau setiap unduhan dan unggahan dari semua sumber Anda.

{{< cards cols="1">}}
  {{< card title="" subtitle="File Evervideo di Semua Penyimpanan yang Terhubung" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Hubungkan ke Penyimpanan Cloud

Bagian Penyimpanan Cloud dari tab File adalah tempat setiap akun yang terhubung, NAS, server media, dan stream berada — berdampingan, dalam satu daftar yang dapat digulir.

{{< cards cols="1">}}
  {{< card title="" subtitle="Bagian Penyimpanan Cloud Evervideo di Tab File" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Buka tab **File**.
- Gulir ke bagian **Penyimpanan Cloud**.
- Ketuk **Hubungkan ke penyimpanan cloud** dari menu.
- Pilih layanan penyimpanan cloud dari daftar.
- Masukkan kredensial Anda di halaman otorisasi resmi yang disediakan oleh penyedia cloud, lalu ketuk **Selesai**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Menghubungkan Layanan Penyimpanan Cloud" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Jika Anda mengalami masalah, periksa koneksi internet dan login / kata sandi Anda. Pada versi Premium aplikasi, Anda dapat menambahkan jumlah layanan yang tidak terbatas; versi gratis mendukung hingga tiga.

## Layanan Penyimpanan Cloud, Server Media, dan Protokol yang Didukung

Evervideo mendukung berbagai sumber video yang sangat luas. Semua di bawah ini berfungsi dari satu alur Hubungkan ke penyimpanan cloud.

**Penyimpanan cloud pribadi:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Server media yang dihosting sendiri:** Plex · Jellyfin · Emby · Subsonic (dan setiap server kompatibel Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (dan ownCloud melalui API bersama) · Synology Drive · QNAP.

**Protokol NAS dan berbagi file:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, autentikasi kata sandi atau kunci publik) · NFS · DLNA / UPnP (pemutaran dan unduhan).

**Stream langsung dan kamera IP:** RTSP — arahkan Evervideo ke URL `rtsp://` mana pun dan langsung diputar. Bagus untuk kamera keamanan, stream IPTV, kamera bel pintu, monitor bayi, dan sumber langsung serupa.

**Penyimpanan objek kompatibel S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, dan endpoint S3-API lainnya.

**Perpustakaan di perangkat:** perpustakaan Foto (semua video, rekaman layar, album foto) dan perpustakaan aplikasi Music (Album, Genre, Daftar Putar) — keduanya muncul di Perpustakaan Media sehingga Anda tidak perlu menyalin apa pun.

**Penemuan jaringan lokal:** bagian Perangkat yang Tersedia secara otomatis mencantumkan setiap layanan Bonjour / mDNS di jaringan Wi-Fi Anda — server Plex, Jellyfin, Emby, Synology, QNAP, router AirPort dengan drive terpasang, Apple Time Capsule — sehingga Anda dapat mengetuk untuk terhubung tanpa mengetik alamat IP.

Setiap koneksi menggunakan SDK resmi atau protokol terbuka dari layanan, dengan otorisasi berbasis OAuth di mana didukung. Anda dapat menghubungkan beberapa akun dari layanan yang sama (misalnya, dua akun Google Drive, atau baik server Plex maupun Jellyfin) dan menelusurinya berdampingan di bagian Penyimpanan Cloud.

## Keamanan dan Privasi

Evervideo hanya menggunakan SDK resmi dan koneksi aman untuk berinteraksi dengan layanan cloud yang terhubung. Login dan kata sandi Anda tidak dapat diakses oleh aplikasi — semua transfer dienkripsi TLS.

Saat Anda memasukkan login dan kata sandi, aplikasi menampilkan halaman otorisasi resmi yang disediakan oleh penyedia layanan cloud, dan seluruh proses otorisasi berlangsung di luar aplikasi. Penyedia layanan cloud kemudian mengirimkan token autentikasi ke aplikasi setelah otorisasi berhasil, dan token tersebut digunakan untuk melakukan panggilan API.

Token autentikasi adalah kunci digital yang memungkinkan aplikasi pihak ketiga berinteraksi dengan penyimpanan cloud atas nama Anda. Token disimpan di perangkat Anda di sistem penyimpanan aman Apple (Keychain), yang dienkripsi saat diam dan dilindungi oleh kode sandi perangkat atau kunci biometrik Anda. Anda dapat mengunduh file dari layanan cloud yang terhubung ke perangkat Anda; file-file tersebut ditempatkan di direktori Dokumen aplikasi dan dapat dihapus kapan saja menggunakan manajer file bawaan.

Aplikasi tidak berbagi informasi apa pun dari akun cloud yang terhubung dengan Everappz, pengiklan, atau pihak ketiga mana pun. Anda dapat mencabut akses ke akun cloud Anda kapan saja dengan membuka halaman pengaturan akun di browser web Anda.

## Menolak Token Autentikasi

Untuk mencabut token autentikasi, masuk ke akun cloud Anda di browser web dan navigasi ke halaman keamanan atau aplikasi yang terhubung. Di sana Anda dapat menemukan setiap aplikasi pihak ketiga yang terhubung ke akun cloud Anda dan menghapus mana saja yang tidak ingin Anda gunakan lagi. Petunjuk terperinci untuk akun Google tersedia [di sini](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Anda juga dapat memutuskan koneksi akun cloud di dalam aplikasi itu sendiri — ketika Anda melakukannya, token autentikasi segera dihapus dari perangkat Anda. Jika Anda menghapus instalasi aplikasi dari perangkat Anda, semua data yang diunduh dan token akses dihapus secara otomatis.

## Memutuskan Koneksi Penyimpanan Cloud atau Mengubah Konfigurasi

- **Akses opsi penyimpanan cloud** — temukan layanan yang terhubung di bagian **Penyimpanan Cloud** dari tab File.
- **Ketuk tombol "..."** di sebelah judul layanan untuk membuka opsi tambahan:
  - **Ganti nama** — ubah nama layanan cloud seperti yang muncul di daftar Anda.
  - **Pengaturan** — ubah konfigurasi atau data autentikasi. Terkadang Anda perlu mengotorisasi ulang layanan cloud yang terhubung jika token otorisasi telah kedaluwarsa.
  - **Putuskan Koneksi** — sepenuhnya memutuskan koneksi antara aplikasi dan layanan cloud. Ini menghapus semua video yang terkait dengan layanan tersebut dari perpustakaan media Anda, tetapi membiarkannya tidak tersentuh di server.

## Hubungkan ke Komputer atau NAS

Anda dapat menghubungkan komputer, NAS pribadi, atau perangkat jaringan lain menggunakan protokol SMB, WebDAV, FTP / FTPS, SFTP, NFS, atau DLNA. Ini adalah cara termudah untuk membawa perpustakaan media rumah yang ada — apakah ada di Mac, Windows PC, Synology, QNAP, Apple Time Capsule, atau WD My Cloud Home — ke Evervideo tanpa menyalin apa pun.

### Hubungkan ke Komputer Menggunakan SMB

- Ketuk **Hubungkan ke penyimpanan cloud → SMB**.
- Masukkan alamat IP komputer dan nama folder bersama menggunakan format `smb://computer-ip-address/shared-folder-name`.
- Pilih versi protokol: **Auto**, **SMB1**, atau **SMB2**.
- Masukkan login dan kata sandi Anda (jika diperlukan).
- Ketuk **Selesai**.

Jika koneksi berhasil, berbagi muncul di bagian Penyimpanan Cloud. Tutorial lengkap tentang cara menghubungkan Mac atau PC menggunakan SMB tersedia [di sini](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Hubungkan ke NAS Menggunakan WebDAV

Semua langkah sama seperti SMB, kecuali bidang URL. Gunakan `http://server-name` atau `https://server-name` jika server mendukung SSL. WebDAV bekerja dengan Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home, dan server lain dengan endpoint WebDAV.

Tutorial lengkap tentang WebDAV tersedia [di sini](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Hubungkan melalui DLNA / UPnP

Bagikan perpustakaan media yang ada di Windows PC atau NAS menggunakan protokol DLNA / UPnP dan aksesnya di dalam Evervideo seperti yang dijelaskan [di sini](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA didukung secara luas, tetapi hanya memungkinkan Anda memutar atau mengunduh video — Anda tidak dapat mengunggah file atau membuat folder baru di server DLNA.

### Hubungkan Menggunakan FTP, FTPS, atau SFTP

Evervideo juga mendukung protokol transfer file klasik. Untuk menghubungkan server melalui FTP atau FTPS, ketuk Hubungkan ke penyimpanan cloud → FTP, masukkan URL host dalam bentuk `ftp://server-name` (atau `ftps://server-name` untuk koneksi terenkripsi), berikan login dan kata sandi Anda, lalu ketuk Selesai. Untuk SFTP (SSH File Transfer Protocol), pilih SFTP dan berikan kata sandi atau pasangan kunci SSH.

### Hubungkan ke Berbagi NFS

Evervideo menyertakan dukungan NFS (Network File System) — berguna untuk host Linux, server BSD, dan perangkat NAS yang lebih suka mengekspos perpustakaan video melalui NFS daripada SMB. Pilih NFS di menu Hubungkan ke penyimpanan cloud, masukkan alamat server dan jalur yang diekspor, dan ketuk Selesai.

## Hubungkan Plex Media Server

Evervideo dapat terhubung langsung ke Plex Media Server dan menelusuri perpustakaan Film, Acara TV, dan Video Rumah Anda. Ketuk Hubungkan ke penyimpanan cloud → Plex, masuk dengan akun Plex Anda, pilih server, dan perpustakaan muncul bersama layanan cloud Anda. Server Plex di jaringan lokal yang sama juga ditemukan secara otomatis di bagian Perangkat yang Tersedia.

## Hubungkan Jellyfin atau Emby Server

Baik Jellyfin (open-source) maupun Emby (komersial) server media berfungsi secara native di Evervideo. Ketuk Hubungkan ke penyimpanan cloud → Jellyfin atau Emby, masukkan URL server Anda (biasanya seperti `http://server-ip:8096`) dan kredensial, dan perpustakaan Anda siap untuk di-streaming.

## Hubungkan Subsonic atau Navidrome Server

Evervideo menggunakan Subsonic API, yang berarti bekerja dengan Subsonic sendiri, Navidrome, dan setiap server kompatibel Subsonic lainnya — termasuk Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), dan Ampache. Ketuk Hubungkan ke penyimpanan cloud → Subsonic, masukkan URL server dan kredensial, dan perpustakaan muncul di bagian Penyimpanan Cloud.

## Hubungkan Stream RTSP (Kamera IP, TV Langsung, IPTV)

Evervideo memiliki dukungan RTSP native, sehingga Anda dapat mengarahkannya ke sumber RTSP mana pun — kamera keamanan, kamera bel pintu, penyedia IPTV, monitor bayi, siaran langsung — dan Evervideo akan menarik dan mendekode stream secara langsung. Ketuk Tautan Online → Tambahkan tautan, tempel URL lengkap (`rtsp://camera-ip:port/stream-path`), berikan login dan kata sandi jika diperlukan, dan ketuk Selesai.

## Hubungkan ke Penyimpanan Objek Kompatibel S3

Untuk pengguna self-host dan pengguna canggih yang menggunakan penyimpanan objek cloud, Evervideo menyertakan konektor kompatibel S3. Ketuk Hubungkan ke penyimpanan cloud → Penyimpanan S3, lalu masukkan URL endpoint, wilayah, kunci akses, kunci rahasia, dan nama bucket. Ini bekerja dengan AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, dan endpoint S3-API lainnya.

## Perangkat yang Tersedia

Bagian ini menampilkan setiap perangkat di jaringan lokal Anda yang dapat Anda hubungkan dari Evervideo melalui penemuan Bonjour / mDNS — server Plex, Jellyfin, Emby, Synology, QNAP, router AirPort dengan drive terpasang, Apple Time Capsule, dan sebagainya. Untuk membuat koneksi:

- Gulir ke bagian Perangkat yang Tersedia di tab File.
- Ketuk perangkat yang ingin Anda hubungkan.
- Jika diperlukan, masukkan detail login Anda untuk menyelesaikan koneksi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Perangkat yang Tersedia Evervideo di Jaringan Lokal" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive memungkinkan Anda mentransfer file secara nirkabel dari komputer ke perangkat iOS melalui browser desktop mana pun, Finder, atau File Explorer. Perangkat dan komputer Anda harus berada di jaringan Wi-Fi yang sama.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive Evervideo" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Aktifkan Wi-Fi Drive

- Di tab File, gulir ke Penyimpanan Cloud → Hubungkan melalui Wi-Fi untuk membuka layar utama Wi-Fi Drive.
- (Opsional) Atur nama pengguna dan kata sandi untuk server web yang tertanam.
- Ketuk Mulai Wi-Fi Drive.

### Akses Wi-Fi Drive di Komputer Anda

- Buka browser web di komputer Anda (Chrome, Firefox, Safari, dll.).
- Masukkan URL yang ditampilkan oleh aplikasi.
- Seret dan lepas file dari komputer Anda ke halaman web — mereka akan mulai mentransfer ke perangkat iOS Anda.

Anda juga dapat memasang Wi-Fi Drive langsung di **Finder** di macOS (Pergi → Hubungkan ke Server…) atau File Explorer di Windows (Petakan Drive Jaringan…) dan perlakukan iPhone atau iPad Anda sebagai drive jaringan biasa.

Petunjuk terperinci tersedia [di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (sekarang Finder File Sharing di macOS Catalina dan yang lebih baru) memungkinkan Anda mentransfer file menggunakan kabel Lightning atau USB-C. Hubungkan perangkat, buka Finder di Mac (atau iTunes di Windows), temukan Evervideo di daftar aplikasi, dan salin file ke folder bersamanya.

## Hubungkan Flash Drive USB atau Kartu SD

Pasang drive USB atau kartu SD ke iPhone, iPad, atau Mac Anda melalui adaptor Lightning-ke-USB / USB-C atau pembaca kartu. Buka File → File di iPhone Ini → Buka Folder, navigasi ke drive, dan pilih file video atau folder. Evervideo memutar file langsung dari drive tanpa menyalinnya ke penyimpanan internal — berguna untuk perpustakaan 4K yang sangat besar.

## Penjelajahan Folder di Penyimpanan yang Terhubung

Ketuk layanan cloud yang terhubung untuk membuka browser filenya. Folder menampilkan thumbnail video jika tersedia, dan mengetuk video langsung memulai pemutaran sambil terus melakukan streaming sisa file di latar belakang.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Menjelajahi Folder di Penyimpanan yang Terhubung" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Akses Cepat

Bagian Akses Cepat terletak di bagian atas tab File. Ini memberi Anda akses cepat ke file dan folder favorit dan yang baru dibuka — baik dari layanan cloud maupun dari penyimpanan di perangkat. Setiap kali Anda membuka file atau folder dari cloud, file tersebut ditambahkan ke daftar Baru Dibuka. Anda dapat menandai folder yang bersarang dalam sebagai Favorit untuk mengaksesnya dengan cepat tanpa menggali melalui struktur direktori.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tautan Online Evervideo dan Akses Cepat" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## File di Aplikasi Ini

Bagian ini menampilkan file dan folder yang disimpan di direktori Dokumen terisolasi Evervideo — semua yang telah Anda unduh dari cloud, transfer melalui Wi-Fi Drive, disalin melalui Finder File Sharing, atau diimpor dari aplikasi lain.

{{< cards cols="1">}}
  {{< card title="" subtitle="File di Aplikasi Ini Evervideo" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Folder Dokumen

Folder Dokumen adalah akar dari semua yang ada di File di Aplikasi Ini. Anda dapat membuat subfolder, mengganti nama file, memindahkannya, dan mengelompokkannya sesuai keinginan.

{{< cards cols="1">}}
  {{< card title="" subtitle="File Lokal Evervideo — Folder Dokumen" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## File di iPhone / iPad / Mac Ini

Bagian ini menampilkan video yang ada di perangkat Anda tetapi di aplikasi yang berbeda. Anda dapat mengimpornya ke Evervideo menggunakan pemilih file sistem:

- Ketuk Buka File… untuk memilih file tertentu.
- Ketuk Buka Folder… untuk memilih seluruh folder.

Anda juga dapat menggunakan Hubungkan Folder untuk membuat tautan ke folder di perangkat Anda dengan akses baca / tulis — sempurna untuk bekerja dengan folder di iCloud Drive atau drive USB yang terpasang tanpa menyalin apa pun.

{{< cards cols="1">}}
  {{< card title="" subtitle="File Evervideo di Perangkat Ini" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Folder Khusus

Di dalam tab File Anda akan melihat beberapa folder khusus yang dibuat dan digunakan Evervideo secara otomatis:

- **Unduhan** — setiap file yang diunduh dari cloud muncul di sini secara default. Sesuaikan di Pengaturan → Manajer File → Simpan File yang Diunduh Ke.
- **Cache Pemutar** — cache pemutar media. Secara default pemutar mengunduh video berikutnya untuk pemutaran yang mulus. Anda dapat menonaktifkan cache di pengaturan aplikasi atau cukup hapus folder ini.
- **iCloud** — file di folder ini disinkronkan di semua perangkat Anda yang terhubung ke akun iCloud yang sama.
- **Folder Offline** — saat Anda menandai folder, daftar putar, album, atau genre sebagai tersedia offline, file-filenya diunduh ke folder ini.

## Toolbar Atas

Toolbar atas, yang terletak di bawah bilah navigasi, menawarkan beberapa tindakan yang dapat Anda tampilkan atau sembunyikan dengan gestur geser ke bawah:

- **Cari** — lakukan pencarian dalam folder atau bagian saat ini.
- **Lanjutkan Pemutaran** — jika diaktifkan di pengaturan, pulihkan antrean pemutar dan posisi video terakhir untuk folder saat ini.
- **Putar Semua** — pindai folder saat ini dan subfoldernya dan tambahkan file ke antrean pemutar.
- **Acak Semua** — seperti Putar Semua, tetapi diacak sebelum ditambahkan.

## Opsi Folder

Saat Anda membuka folder, ketuk tombol **"..."** di pojok kanan atas untuk tindakan berikut:

- **Pilih** — aktifkan mode pemilihan file.
- **Folder Baru** — buat folder baru dalam folder saat ini.
- **Aktifkan Mode Offline** — nyalakan sinkronisasi offline untuk folder saat ini. File baru yang ditambahkan secara online diunduh secara otomatis.
- **Unggah File** — unggah file dari perangkat Anda ke folder online.
- **Cari** — cari di dalam folder.
- **Urutkan** — urutkan file berdasarkan nama, ukuran, tanggal dimodifikasi, atau metadata.
- **Tampilan Kisi / Daftar** — beralih antara tampilan tabel dan tampilan thumbnail. Tampilan thumbnail menampilkan pratinjau poster video yang besar.

## Mode Seleksi

Ketuk **"..."** di pojok kanan atas dan pilih **Pilih** untuk masuk ke mode seleksi. Kotak centang muncul di sebelah setiap file dan folder. Ketuk untuk memilih satu atau beberapa item, lalu lakukan tindakan batch: Putar Berikutnya, Putar Nanti, Tambahkan ke Perpustakaan Media, Tambahkan ke Daftar Putar, Salin, Unggah, Pindahkan, Ganti Nama, atau Hapus.

{{< cards cols="1">}}
  {{< card title="" subtitle="Mode Seleksi Evervideo di Manajer File" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Jika Anda lebih suka memperlakukan penyimpanan cloud yang terhubung sebagai hanya-baca (untuk mencegah penghapusan tidak sengaja), aktifkan Pengaturan → Manajer File → Edit File Online → Nonaktif untuk menyembunyikan semua operasi destruktif dari UI.

## Tindakan File

Ketuk ikon **"..."** dekat judul file untuk memunculkan menu tindakannya:

- **Putar Berikutnya** — masukkan file di bagian atas antrean pemutar.
- **Putar Nanti** — tambahkan file ke bagian bawah antrean pemutar.
- **Tambahkan ke Perpustakaan Media** — masukkan file ke perpustakaan media Anda, diatur berdasarkan Album dan Genre.
- **Tambahkan ke Daftar Putar** — tambahkan file ke daftar putar yang ada atau buat yang baru.
- **Edit Tag** — buka editor tag bawaan untuk memodifikasi metadata. Untuk file online, file diunduh sementara, diedit, lalu diunggah kembali setelah Anda konfirmasi.
- **Tambahkan ke Favorit** — tambahkan file ke daftar favorit Anda untuk akses cepat.
- **Unduh** — unduh file atau folder ke perangkat Anda untuk penggunaan offline.
- **Ganti Nama** — ganti nama file langsung di penyimpanan jarak jauh.
- **Pindahkan** — pindahkan file ke folder yang berbeda dalam penyimpanan cloud Anda.
- **Tambahkan ke Arsip** — bundel file ke dalam satu file ZIP (fitur Premium).
- **Buka Di** — ekspor file ke aplikasi kompatibel lain melalui lembar Berbagi sistem.
- **Hapus** — hapus file secara permanen. **Tindakan ini tidak dapat dibatalkan.**

## Tindakan Folder

Untuk setiap folder di penyimpanan cloud Anda, tersedia banyak tindakan dengan mengetuk ikon **"..."** di sebelah judul folder.

- **Putar Semua** — ganti antrean pemutar saat ini dengan setiap video di folder.
- **Putar Berikutnya / Putar Nanti** — tambahkan seluruh folder ke antrean.
- **Tambahkan ke Perpustakaan Media** — masukkan konten folder ke perpustakaan media Anda.
- **Tambahkan ke Daftar Putar** — tambahkan seluruh folder ke daftar putar.
- **Tambahkan ke Favorit** — tambahkan folder ke favorit Anda.
- **Aktifkan Mode Offline** — selain unduhan sederhana, ini terus memantau folder untuk file baru dan mengunduhnya secara otomatis saat muncul online.
- **Unduh** — unduh semua konten folder ke perangkat Anda untuk akses offline.
- **Ganti Nama / Pindahkan** — ganti nama atau pindahkan folder di penyimpanan jarak jauh.
- **Tambahkan ke Arsip** — bundel konten folder ke dalam file ZIP (fitur Premium).
- **Hapus** — hapus folder dan isinya secara permanen. **Tindakan ini tidak dapat dibatalkan.**

## Antrean Transfer

Di pojok kanan atas tab File terdapat tombol **Transfer** (ikon panah berputar). Ketuk untuk membuka Antrean Transfer — daftar setiap unduhan dan unggahan aktif dari semua sumber Anda, dengan kemajuan waktu nyata, kecepatan, dan ETA per file.

{{< cards cols="1">}}
  {{< card title="" subtitle="Antrean Transfer File Evervideo" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Anda dapat menjeda, melanjutkan, mencoba ulang transfer yang gagal, menyusun ulang item untuk memprioritaskan unduhan tertentu, atau membatalkannya satu per satu. Anda juga dapat menyesuaikan kecepatan antrean transfer (jumlah tugas paralel maksimum), jenis jaringan (hanya Wi-Fi atau Wi-Fi + Seluler), dan transfer latar belakang di Pengaturan → Manajer File.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tindakan Evervideo pada Antrean Transfer File" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Mode Offline dan Folder Offline yang Disinkronkan

Mode offline adalah fitur yang berguna yang memungkinkan Anda menonton video favorit bahkan saat tidak terhubung ke internet. Saat Anda mengaktifkan mode offline untuk folder, daftar putar, album, atau genre mana pun, semua file dalam koleksi tersebut diunduh secara otomatis ke perangkat Anda untuk pemutaran offline. Mereka muncul di bagian Folder Offline.

Saat Anda menambahkan file baru ke server jarak jauh, file tersebut juga diunduh secara otomatis — sehingga koleksi offline Anda tetap terkini tanpa Anda melakukan apa pun. Untuk menyinkronkan ulang secara manual, ketuk tiga titik di pojok kanan atas folder offline dan pilih Sinkronkan.

Anda dapat menyesuaikan batas waktu sinkronisasi di Pengaturan → Manajer File → Folder Offline yang Disinkronkan → Interval Waktu.

Petunjuk terperinci tersedia [di sini](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalisasi

Di Pengaturan → Personalisasi Anda dapat mengonfigurasi cara tab File disajikan:

- **Gaya Layar File** — Menu Polos (menampilkan daftar folder langsung) atau Menu Dikelompokkan (mengelompokkan konten berdasarkan kategori — Akses Cepat, Folder Khusus, Penyimpanan Cloud, dll.).
