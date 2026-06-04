---
title: "Koneksi"
date: 2020-02-01
description: "Pelajari cara menghubungkan layanan cloud dan perangkat NAS ke Flacbox. Streaming musik resolusi tinggi dari iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk, dan lainnya. Gunakan SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing, dan drive flash USB."
keywords: [
  "pengaturan cloud Flacbox", "menghubungkan Google Drive ke Flacbox", "streaming musik SMB",
  "pemutar iOS WebDAV", "aplikasi musik DLNA", "streaming audio NAS", "Wi-Fi Drive iPhone",
  "transfer file ke iPhone", "Flacbox iTunes File Sharing", "menghubungkan NAS ke iPhone",
  "aplikasi musik Synology Drive", "aplikasi musik QNAP", "aplikasi musik Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "aplikasi musik scrobbling Last.fm",
  "musik iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["panduan", "flacbox", "koneksi", "cloud", "NAS"]
readingTime: 12
---


Di layar ini, Anda dapat menghubungkan setiap sumber yang menyimpan musik Anda. Anda dapat mengintegrasikan layanan cloud populer seperti Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive, dan banyak lagi, serta Mac, PC, atau NAS Anda melalui protokol standar. Apakah koleksi Anda berada di layanan ramah streaming seperti Dropbox atau di NAS pribadi seperti Synology, QNAP, Buffalo, Apple Time Capsule, atau WD My Cloud Home, Flacbox terhubung ke semuanya dari satu layar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Koneksi Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Menghubungkan ke Cloud Storage

- Buka tab **Koneksi**.
- Pilih **Menghubungkan ke penyimpanan cloud** dari menu.
- Pilih layanan penyimpanan cloud dari daftar.
- Masukkan kredensial Anda di halaman otorisasi resmi yang disediakan oleh penyedia cloud, lalu ketuk **Selesai**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Menambahkan Layanan Cloud Storage" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Jika Anda mengalami masalah, periksa koneksi internet dan login / kata sandi Anda. Dalam versi Premium aplikasi, Anda dapat menambahkan layanan tanpa batas; versi gratis mendukung hingga tiga layanan.

## Layanan Cloud Storage, Server Media, dan Protokol yang Didukung

Flacbox mendukung berbagai sumber musik yang luar biasa luas. Semua di bawah ini berfungsi dari satu layar **Menghubungkan ke penyimpanan cloud**.

**Penyimpanan cloud pribadi:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Server yang di-hosting sendiri:** Plex · Jellyfin · Emby · Subsonic (dan setiap server yang kompatibel dengan Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (dan ownCloud melalui API bersama) · Synology Drive · QNAP.

**Protokol NAS dan berbagi file:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, autentikasi kata sandi atau kunci publik) · NFS · DLNA / UPnP (pemutaran dan unduhan).

**Penyimpanan objek kompatibel S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, dan layanan lain yang mengekspos endpoint S3-API.

**Penemuan jaringan lokal:** Bagian Perangkat yang Tersedia secara otomatis mencantumkan setiap layanan Bonjour / mDNS di jaringan Wi-Fi Anda sehingga Anda dapat mengetuk untuk terhubung tanpa mengetik alamat IP.

Setiap koneksi menggunakan **SDK resmi atau protokol terbuka** dari layanan tersebut, dengan otorisasi berbasis OAuth di mana didukung. Anda dapat menghubungkan beberapa akun dari layanan yang sama (misalnya, dua akun Google Drive, Dropbox pribadi di samping akun kerja, atau server Plex dan Jellyfin) dan menelusuri semuanya secara berdampingan di layar Koneksi.

## Keamanan dan Privasi

Kami hanya menggunakan SDK resmi dan koneksi aman untuk berinteraksi dengan layanan cloud yang terhubung. Login dan kata sandi Anda tidak dapat diakses oleh aplikasi — semua transfer dienkripsi dengan TLS.

Saat Anda memasukkan login dan kata sandi, aplikasi menampilkan halaman otorisasi resmi yang disediakan oleh penyedia layanan cloud, dan seluruh proses otorisasi berlangsung di luar aplikasi. Penyedia layanan cloud kemudian mengirim auth-token ke aplikasi setelah otorisasi berhasil, dan token tersebut digunakan untuk melakukan panggilan API.

Auth-token adalah kunci digital yang memungkinkan aplikasi pihak ketiga berinteraksi dengan penyimpanan cloud atas nama Anda. Token disimpan di perangkat Anda dalam penyimpanan sistem aman Apple (Keychain), yang dienkripsi saat tidak aktif dan dilindungi oleh kode sandi perangkat atau kunci biometrik Anda. Anda dapat mengunduh file dari layanan cloud yang terhubung ke perangkat Anda; file-file tersebut ditempatkan di direktori Dokumen aplikasi dan dapat dihapus kapan saja menggunakan manajer file bawaan.

Aplikasi tidak berbagi informasi apa pun dari akun cloud yang terhubung dengan Everappz, pengiklan, atau pihak ketiga mana pun. Anda dapat mencabut akses ke akun cloud Anda kapan saja dengan membuka halaman pengaturan akun di browser web Anda.

## Menolak Auth-Token

Untuk mencabut auth-token, masuk ke akun cloud Anda di browser web dan navigasikan ke halaman keamanan atau aplikasi yang terhubung. Di sana Anda dapat menemukan setiap aplikasi pihak ketiga yang terhubung ke akun cloud Anda dan menghapus yang mana pun jika Anda tidak ingin menggunakannya lagi. Instruksi terperinci untuk akun Google tersedia [di sini](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Anda juga dapat memutuskan koneksi akun cloud di dalam aplikasi itu sendiri — saat Anda melakukannya, auth-token segera dihapus dari perangkat Anda. Jika Anda menghapus instalasi aplikasi dari perangkat, semua data yang diunduh dan token akses dihapus secara otomatis bersamanya.

## Memutuskan Koneksi Cloud Storage atau Mengubah Konfigurasi

- **Akses opsi cloud storage** — temukan layanan yang terhubung di layar **Koneksi**.
- **Ketuk tombol "..."** di sebelah judul layanan untuk membuka opsi tambahan:
  - **Ganti nama** — ubah nama layanan cloud seperti yang muncul dalam daftar Anda.
  - **Pengaturan** — modifikasi konfigurasi atau data autentikasi. Kadang-kadang Anda mungkin perlu mengotorisasi ulang layanan cloud yang terhubung jika token otorisasi telah kedaluwarsa.
  - **Putuskan Koneksi** — sepenuhnya memutus koneksi antara aplikasi dan layanan cloud. Ini menghapus semua lagu yang terkait dengan layanan tersebut dari perpustakaan musik aplikasi, tetapi meninggalkannya tidak tersentuh di server.

## Menghubungkan ke Komputer atau NAS

Anda juga dapat menghubungkan komputer, NAS pribadi, atau perangkat jaringan lainnya menggunakan protokol SMB, DLNA, atau WebDAV. Ini adalah cara termudah untuk membawa perpustakaan musik rumah yang ada — baik di Mac, PC Windows, kotak Synology, atau NAS — ke Flacbox tanpa menyalin apa pun.

## Menghubungkan ke Komputer Menggunakan SMB

- Ketuk **Menghubungkan ke penyimpanan cloud → SMB**.
- Masukkan alamat IP komputer dan nama folder bersama di bidang URL menggunakan format `smb://computer-ip-address/shared-folder-name`.
- Pilih versi protokol: **Auto**, **SMB1**, atau **SMB2**.
- Masukkan login dan kata sandi Anda (jika diperlukan).
- Ketuk **Selesai**.

Jika koneksi berhasil, Anda akan melihat penyimpanan yang terhubung di bagian **Cloud Storage**. Tutorial lengkap tentang cara menghubungkan Mac atau PC menggunakan SMB tersedia [di sini](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Menghubungkan ke NAS Menggunakan WebDAV

Semua langkah sama dengan SMB, kecuali untuk bidang URL. URL harus dalam format `http://server-name` atau `https://server-name` jika server mendukung SSL. WebDAV berfungsi dengan **Synology, QNAP, Nextcloud, ownCloud,** dan banyak server lainnya — di mana pun endpoint WebDAV tersedia.

Tutorial lengkap tentang cara menghubungkan NAS menggunakan WebDAV tersedia [di sini](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Menghubungkan ke Komputer atau NAS Menggunakan DLNA

Anda juga dapat berbagi perpustakaan musik yang terletak di PC Windows atau NAS pribadi menggunakan protokol DLNA / UPnP dan mengakses perpustakaan tersebut di aplikasi seperti yang dijelaskan [di sini](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA adalah protokol yang populer dan didukung secara luas, tetapi hanya memungkinkan Anda memainkan atau mengunduh musik — Anda tidak dapat mengunggah file atau membuat folder baru di server DLNA.

## Menghubungkan ke NAS atau Server Menggunakan FTP, FTPS, atau SFTP

Flacbox juga mendukung protokol transfer file klasik. Untuk menghubungkan server melalui FTP atau FTPS, ketuk **Menghubungkan ke penyimpanan cloud → FTP**, masukkan URL host dalam bentuk `ftp://server-name` (atau `ftps://server-name` untuk koneksi terenkripsi), berikan login dan kata sandi Anda, lalu ketuk **Selesai**. Untuk **SFTP** (SSH File Transfer Protocol), pilih **SFTP** dan berikan kata sandi atau pasangan kunci SSH. Keduanya berfungsi dengan perangkat NAS, host Linux, dan server mana pun yang memiliki daemon FTP / FTPS / SSH.

## Menghubungkan ke NFS Share

Flacbox menyertakan dukungan **NFS** (Network File System) — berguna untuk host Linux, server BSD, dan perangkat NAS yang lebih memilih untuk mengekspos perpustakaan musik melalui NFS daripada SMB. Pilih **NFS** di menu **Menghubungkan ke penyimpanan cloud**, masukkan alamat server dan jalur yang diekspor, lalu ketuk **Selesai**.

## Menghubungkan Plex Media Server

Flacbox dapat terhubung langsung ke Plex Media Server dan menelusuri perpustakaan musik Anda berdasarkan Artis, Album, Genre, dan Daftar Putar. Ketuk **Menghubungkan ke penyimpanan cloud → Plex**, masuk dengan akun Plex Anda, pilih server, dan perpustakaan muncul di samping layanan cloud Anda. Server Plex di jaringan lokal yang sama juga ditemukan secara otomatis di bagian **Perangkat yang Tersedia**.

## Menghubungkan Server Jellyfin atau Emby

Baik **Jellyfin** (open-source) maupun **Emby** (komersial) bekerja secara native di Flacbox. Ketuk **Menghubungkan ke penyimpanan cloud → Jellyfin** atau **Emby**, masukkan URL server Anda (seperti `http://server-ip:8096`) dan kredensial, dan perpustakaan musik Anda siap untuk di-streaming. Seperti Plex, perpustakaan di jaringan lokal tercantum secara otomatis di **Perangkat yang Tersedia**.

## Menghubungkan Server Subsonic atau Navidrome

Flacbox menggunakan Subsonic API, yang berarti berfungsi dengan **Subsonic** itu sendiri, **Navidrome**, dan setiap server yang kompatibel dengan Subsonic lainnya — termasuk Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Ketuk **Menghubungkan ke penyimpanan cloud → Subsonic**, masukkan URL server dan kredensial, dan perpustakaan muncul di layar Koneksi.

## Menghubungkan ke S3-Compatible Object Storage

Flacbox menyertakan konektor yang kompatibel dengan S3. Ketuk **Menghubungkan ke penyimpanan cloud → S3 storage**, lalu masukkan URL endpoint, wilayah, kunci akses, kunci rahasia, dan nama bucket. Ini berfungsi dengan AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, dan layanan lain yang mengekspos endpoint S3-API.

## Perangkat yang Tersedia

Bagian ini menampilkan setiap perangkat di jaringan lokal Anda yang dapat Anda hubungkan dari Flacbox melalui penemuan Bonjour. Untuk membuat koneksi, ikuti langkah-langkah berikut:

- Buka aplikasi dan pergi ke bagian **Perangkat yang Tersedia** di bawah Koneksi.
- Ketuk perangkat yang ingin Anda hubungkan.
- Jika diperlukan, masukkan detail login Anda untuk menyelesaikan koneksi.

Ini adalah cara tercepat untuk menemukan SMB, WebDAV, berbagi DLNA di jaringan rumah Anda tanpa mengetik alamat IP secara manual.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Perangkat yang Tersedia di Jaringan Lokal" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive adalah teknologi yang memudahkan transfer file nirkabel dari komputer ke perangkat iOS Anda melalui browser desktop mana pun. Untuk menggunakan fitur ini secara efektif, pastikan perangkat dan komputer Anda terhubung ke jaringan Wi-Fi yang sama. Berikut panduan langkah demi langkah cara menggunakan Wi-Fi Drive.

### Mengaktifkan Wi-Fi Drive

- Buka aplikasi dan pergi ke tab **Koneksi**.
- Pilih **Menghubungkan melalui Wi-Fi** untuk mengakses layar utama Wi-Fi Drive.
- (Opsional) Atur nama pengguna dan kata sandi untuk server web tertanam guna melindungi akses.
- Ketuk **Mulai Wi-Fi Drive** untuk mengaktifkan Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Mengakses Wi-Fi Drive di Komputer Anda

- Di komputer Anda (desktop atau laptop), buka browser web (seperti Chrome, Firefox, atau Safari).
- Di bilah alamat browser, masukkan URL yang disediakan oleh aplikasi.

### Transfer File Secara Nirkabel

Setelah halaman web yang sesuai dengan perangkat iOS Anda terbuka di browser, Anda dapat dengan mudah menyeret dan menjatuhkan file dari komputer ke halaman web. File yang Anda jatuhkan akan mulai ditransfer ke perangkat iOS Anda dan akan dapat diakses di dalam Flacbox.

Anda juga dapat memasang Wi-Fi Drive langsung di Finder di macOS (Pergi → Hubungkan ke Server…) atau File Explorer di Windows (Petakan Drive Jaringan…) dan memperlakukan iPhone atau iPad Anda sebagai drive jaringan biasa.

Instruksi terperinci tentang cara mentransfer file secara nirkabel menggunakan Wi-Fi Drive tersedia [di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (sekarang Finder File Sharing di macOS Catalina dan yang lebih baru) adalah cara lain untuk mentransfer file dari komputer ke perangkat menggunakan kabel Lightning atau USB-C.

- Hubungkan perangkat ke komputer menggunakan kabel dan jalankan **Finder** di Mac (atau **iTunes** di Windows).
- Buka **Lokasi → Perangkat yang Terhubung → File** dan temukan aplikasi Flacbox.
- Ketuk ikon aplikasi untuk melihat semua folder bersama.
- Salin file dari komputer ke folder bersama di perangkat menggunakan seret dan jatuhkan.

Instruksi terperinci tentang cara menggunakan Finder File Sharing tersedia [di sini](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Menghubungkan Drive Flash USB

Jika Anda memiliki kartu SD atau drive USB, Anda dapat menghubungkannya menggunakan Lightning ke USB / SD Card Reader atau drive USB-C (di iPad dan iPhone 15 / 16 / 17 / Pro). Aplikasi mendukung pembaca kartu bersertifikat Apple dan iXpand Flash Drive. Dengan iXpand Flash Drive, masukkan ke port Lightning dan buka aplikasi — Anda akan melihat pesan Perangkat Eksternal Terhubung dan informasi perangkat. Ketuk ikon drive flash untuk mengakses folder musik dan ketuk file audio apa pun untuk mulai memutar.

Instruksi terperinci tentang cara menghubungkan drive flash USB ke iPhone dan mendengarkan musik atau mengelola file yang ada di dalamnya tersedia [di sini](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Manajer File

Setelah Anda menghubungkan layanan cloud storage, ketuk ikonnya untuk melihat semua file dan folder yang tersedia. Anda dapat menggunakan manajer file bawaan untuk bekerja dengan file-file ini — unduh, ganti nama, pindahkan, unggah, hapus, dan lainnya. Saat Anda memulai unduhan, file muncul dalam antrian transfer. Untuk membuka antrian transfer, pergi ke tab File Lokal dan ketuk ikon panah berputar di sudut kiri atas. Semua file dan folder yang diunduh tersedia di bagian File Lokal.

## Toolbar Atas

Toolbar atas, yang terletak di bawah bilah navigasi, menawarkan beberapa tindakan berguna untuk akses mudah. Anda dapat menampilkan atau menyembunyikannya dengan gerakan geser ke bawah sederhana.

- **Cari** — lakukan pencarian cepat dalam direktori saat ini, memudahkan pencarian file atau folder tertentu.
- **Lanjutkan Pemutaran** — jika diaktifkan dalam pengaturan aplikasi, ini memulihkan antrian pemutar audio dan posisi media terakhir untuk folder saat ini.
- **Putar Semua** — memindai folder saat ini dan subfolder-nya, lalu menambahkan semua file audio yang ditemukan ke antrian pemutar baru.
- **Acak Semua** — seperti Putar Semua, tetapi mengacak file sebelum menambahkannya ke antrian pemutar audio.

## Opsi Folder

Saat Anda membuka folder, Anda akan menemukan serangkaian tindakan yang tersedia dengan mengetuk tombol **"..."** di sudut kanan atas.

- **Pilih** — aktifkan mode pemilihan file. Ini memungkinkan Anda memilih satu atau lebih file dalam folder dan melakukan tindakan pada seluruh pilihan.
- **Folder Baru** — buat folder baru di folder saat ini.
- **Mengaktifkan mode offline** — aktifkan mode offline untuk folder saat ini. Mode offline tidak hanya mengunduh file tetapi juga aktif memantau perubahan folder.
- **Unggah File** — unggah file dari perangkat Anda ke folder online.
- **Cari** — cari file tertentu dalam folder saat ini.
- **Urutkan** — urutkan file berdasarkan nama, ukuran, tanggal dimodifikasi, atau berdasarkan metadata.
- **Tampilan Kisi / Daftar** — beralih antara tampilan tabel dan tampilan thumbnail.

## Mengedit File Online

Saat Anda perlu mengelola beberapa file di cloud storage, gunakan **Mode Pemilihan** untuk menyederhanakan tindakan Anda:

- **Aktifkan Mode Pemilihan** — ketuk tombol **"..."** di sudut kanan atas dan pilih **Pilih**.
- **Pilih File** — kotak centang muncul di sebelah setiap file dan folder. Ketuk untuk memilih satu atau beberapa item.
- **Lakukan Tindakan** — setelah Anda memilih file atau folder, Anda akan memiliki akses ke Putar Berikutnya, Putar Nanti, Tambah ke Perpustakaan Musik, Tambah ke Daftar Putar, Salin, Unggah, Pindah, Ganti Nama, dan Hapus.

Jika Anda lebih suka memperlakukan cloud storage yang terhubung sebagai hanya-baca (untuk mencegah penghapusan tidak sengaja), aktifkan Pengaturan → Manajer File → Mengedit File Online → Nonaktif untuk menyembunyikan semua operasi destruktif dari UI.

## Tindakan File

Ketuk ikon **"..."** di dekat judul file untuk menampilkan menu tindakannya:

- **Putar Berikutnya** — masukkan file di atas antrian pemutar, sehingga diputar setelah trek saat ini.
- **Putar Nanti** — tambahkan file ke bagian bawah antrian pemutar.
- **Tambah ke Perpustakaan Musik** — masukkan file ke perpustakaan musik Anda, diorganisir berdasarkan artis, album, genre, atau komposer.
- **Tambah ke Daftar Putar** — tambahkan file ke daftar putar yang ada atau buat yang baru.
- **Mengedit tag audio** — buka editor tag bawaan untuk memodifikasi metadata.
- **Tambah ke Favorit** — tambahkan file ke daftar favorit Anda untuk akses cepat.
- **Unduh** — unduh file atau folder ke perangkat Anda untuk digunakan secara offline.
- **Ganti Nama** — ganti nama file langsung di penyimpanan jarak jauh.
- **Pindah** — pindahkan file ke folder yang berbeda dalam cloud storage Anda.
- **Buka Di** — ekspor file ke aplikasi lain yang kompatibel.
- **Hapus** — hapus file secara permanen dari cloud storage Anda. **Tindakan ini tidak dapat dibatalkan.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lebih banyak tindakan untuk File di Cloud Storage yang Terhubung" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Jika daftar tindakan melebihi ruang layar yang tersedia, cukup gulir ke bawah dalam menu tindakan untuk mengakses opsi tambahan.

## Tindakan Folder

Untuk setiap folder di cloud storage Anda, berbagai tindakan tersedia dengan mengetuk ikon **"..."** di sebelah judul folder.

- **Putar Semua** — ganti antrian pemutar saat ini dengan setiap item di folder yang dipilih.
- **Putar Berikutnya** — tambahkan seluruh folder ke atas antrian pemutar.
- **Putar Nanti** — tambahkan konten folder ke bagian bawah antrian pemutar.
- **Tambah ke Perpustakaan Musik** — masukkan konten folder ke perpustakaan musik Anda.
- **Tambah ke Daftar Putar** — tambahkan seluruh folder ke daftar putar.
- **Tambah ke Favorit** — tambahkan folder ke favorit Anda untuk akses cepat.
- **Mengaktifkan mode offline** — selain unduhan sederhana, ini terus memantau folder untuk file baru dan mengunduhnya secara otomatis saat muncul online.
- **Unduh** — unduh semua konten folder ke perangkat Anda untuk akses offline.
- **Ganti Nama** — ganti nama folder langsung di penyimpanan jarak jauh.
- **Pindah** — pindahkan folder ke lokasi yang berbeda dalam cloud storage Anda.
- **Arsip (ZIP)** — bundel konten folder menjadi satu file ZIP (fitur Premium).
- **Hapus** — hapus folder dan kontennya secara permanen dari cloud storage Anda. **Tindakan ini tidak dapat dibatalkan.**

## Akses Cepat

Bagian Akses Cepat terletak di bagian atas layar. Ini memberi Anda akses cepat ke file dan folder favorit serta yang baru dibuka dari layanan cloud yang terhubung. Setiap kali Anda membuka file atau folder dari cloud, itu ditambahkan ke daftar Baru Dibuka. Untuk menghapus daftar ini, buka Terbaru, ketuk tombol Lebih banyak tindakan, dan pilih Hapus Daftar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Tautan Online dan Akses Cepat" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Layanan Lainnya

Bagian ini menampilkan fitur tambahan yang meningkatkan pengalaman Anda. Saat ini, aplikasi mendukung scrobbling **Last.fm** — saat terhubung, statistik pemutaran Anda secara otomatis dikirim ke akun Last.fm Anda. Instruksi pengaturan terperinci tersedia [di sini](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Koneksi Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
