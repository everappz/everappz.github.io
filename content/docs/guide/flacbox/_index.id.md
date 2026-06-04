---
date: 2020-01-01
title: 'Flacbox'
description: 'Pelajari cara menggunakan Flacbox — pemutar musik cloud bertenaga hi-res FLAC, DSD, ALAC, dan FFmpeg untuk iPhone, iPad, dan Mac. Hubungkan iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, dan DLNA. Streaming dan unduh audio resolusi tinggi, edit metadata, dengarkan audiobook, scrobble ke Last.fm, gunakan Apple CarPlay dan widget Layar Utama, serta sesuaikan equalizer 10 band.'
keywords: [
  "panduan pengguna Flacbox", "cara menggunakan Flacbox", "pemutar musik hi-res iPhone", "pemutar FLAC iPhone",
  "pemutar DSD iOS", "pemutar ALAC Mac", "aplikasi musik lossless", "pemutar musik cloud iPhone",
  "pemutar FLAC offline Mac", "pengelola perpustakaan musik", "editor tag audio",
  "pemutar FLAC CarPlay", "aplikasi audio Chromecast", "musik AirPlay 2",
  "widget Flacbox", "Flacbox CarPlay", "pemutar musik FFmpeg iOS",
  "pemutar audiobook iPhone", "bookmark audio iOS", "aplikasi koreksi pitch musik",
  "sample rate output audio", "DAC eksternal iPhone", "USB DAC Mac",
  "aplikasi musik Synology", "aplikasi musik QNAP", "pemutar musik NAS iPhone",
  "pemutar musik WebDAV", "streaming musik SMB", "pemutar musik DLNA",
  "musik iCloud Drive", "FLAC Google Drive", "pemutar FLAC Dropbox",
  "transfer musik Wi-Fi Drive", "impor playlist M3U", "scrobbling Last.fm"
]
tags: ["flacbox", "panduan", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widget"]
---


### Selamat Datang di Panduan Flacbox

Flacbox adalah pemutar musik resolusi tinggi untuk iPhone, iPad, dan Mac yang memungkinkan Anda mengubah penyimpanan cloud, NAS, dan server media favorit menjadi layanan streaming pribadi Anda sendiri.

Flacbox terhubung ke berbagai sumber yang luar biasa luas, semuanya dalam satu aplikasi:

- **Penyimpanan cloud pribadi:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Server yang di-hosting sendiri:** Plex · Jellyfin · Emby · Subsonic (dan setiap server yang kompatibel dengan Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (dan ownCloud melalui API bersama) · Synology Drive · QNAP.
- **Protokol NAS dan berbagi file:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (autentikasi kata sandi atau kunci publik) · NFS · DLNA / UPnP (pemutaran dan unduhan). Berfungsi dengan Apple Time Capsule, Synology, QNAP, WD My Cloud, host Linux Samba / NFS / SSH apa pun, atau folder bersama di Mac atau PC Windows Anda.
- **Penyimpanan objek kompatibel S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, dan endpoint S3-API lainnya.
- **Penemuan jaringan lokal:** Bagian Perangkat yang Tersedia secara otomatis mencantumkan setiap layanan Bonjour / mDNS di Wi-Fi Anda — server Plex, Jellyfin, Emby, Synology, QNAP, router AirPort dengan drive terpasang, Time Capsule — sehingga Anda dapat mengetuk untuk terhubung tanpa mengetik alamat IP.

Di mana sebagian besar aplikasi musik menggunakan mesin audio bawaan Apple, Flacbox menyertakan **FFmpeg** bersama codec sistem sehingga Anda dapat memutar format yang tidak didukung iOS secara bawaan — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, ditambah keluarga MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC biasa. Dikombinasikan dengan sample rate output audio yang dapat dikonfigurasi (44,1 / 48 / 64 / 88,2 / 96 kHz), output multisaluran (Mono → 5.1 → SDDS → ITU BS.775-1), penyetelan buffer IO, dan koreksi pitch, Flacbox memberi audiophile kendali yang tidak ditawarkan oleh sebagian besar aplikasi musik konsumen.

### Nikmati Streaming Lancar dan Pemutaran Offline

Flacbox dilengkapi buffering cerdas untuk streaming yang lancar dan manajer unduhan bawaan sehingga Anda dapat mengunduh seluruh Daftar Putar, Artis, Album, Folder, atau trek individual ke perangkat Anda untuk digunakan secara offline. Ketika penyimpanan hampir penuh, hapus file yang di-cache dengan satu ketukan dan terus streaming dari cloud. Mode Offline untuk folder, daftar putar, album, dan artis juga secara otomatis menyinkronkan trek baru begitu muncul di cloud, sehingga koleksi offline Anda selalu terkini.

### Perpustakaan Musik yang Terorganisir Secara Otomatis

Saat Anda mengimpor trek audio, Flacbox memindai metadata mereka dan mengaturnya ke dalam Perpustakaan Musik yang bersih — dikelompokkan berdasarkan Lagu, Lagu yang Belum Diputar, Album, Album Artis, Artis, Genre, dan Komposer. Gunakan pencarian bawaan untuk menemukan apa pun dalam hitungan detik, filter berdasarkan sumber (cloud online / offline / perangkat), dan pilih antara tata letak perpustakaan Biasa / Dikelompokkan / Bertab. Untuk perpustakaan dengan kompilasi "berbagai artis" yang bercampur, Flacbox menyediakan tampilan Semua Album / Album Eksklusif / Album Solo.

### Perbaiki Metadata dan Beri Tag Musik Anda

Jika Anda menemukan tag yang rusak atau pengkodean yang berantakan (masalah umum untuk file yang di-rip atau file lama), editor ID3 Tags bawaan dapat membersihkannya — secara manual atau dengan pencarian MusicBrainz otomatis. Anda juga dapat menormalkan pengkodean karakter yang rusak (bagus untuk tag Sirilik, Jepang, atau Cina yang berasal dari PC Windows), mencari artwork album yang hilang, dan menulis perubahan kembali ke file asli di cloud secara otomatis. Untuk pengeditan batch yang lebih mendalam, instal aplikasi pendamping kami Evertag.

### Transfer Mudah dari Mac, PC, atau NAS

Pindahkan musik antara komputer dan iPhone atau iPad Anda dengan salah satu alat berikut: SMB, WebDAV, DLNA, Wi-Fi Drive (seret dan jatuhkan di browser desktop mana pun), iTunes / Finder File Sharing melalui kabel Lightning atau USB-C, drive flash USB, atau iXpand Flash Drive. Punya Apple Time Capsule, WD My Cloud, Synology, QNAP, atau NAS lain yang mengekspos SMB / WebDAV / DLNA / FTP / SFTP? Hubungkan sekali dan streaming seluruh perpustakaan Anda tanpa menggunakan penyimpanan perangkat apa pun.

### Sesuaikan Suara Anda dengan Equalizer

Flacbox menyertakan equalizer 10 band dengan preset bergaya iPod (Akustik, Penguat Bass, Klasik, Dance, Rock, Pop, Jazz, dan banyak lagi), preamplifier, dan kemampuan untuk menyimpan preset Anda sendiri. Baik Anda menyetel untuk sepasang IEM audiophile, HomePod mini, atau stereo mobil, Anda dapat membentuk suara persis seperti yang Anda inginkan.

### Ramah Audiobook

Flacbox adalah pemutar audiobook yang hebat — beberapa bookmark per trek, kecepatan pemutaran yang dapat disesuaikan (0,02× hingga 3,00×), lanjutkan pemutaran tepat di tempat Anda berhenti, tombol skip-time yang dapat dikustomisasi, dan sleep timer yang memudar dengan lembut saat tidur. Penanda bab M4B dan file panjang sepenuhnya didukung.

### Streaming di Mana Saja — Termasuk di Mobil dan Layar Utama

Streaming musik ke Apple TV / HomePod melalui AirPlay 2, kirim ke speaker Google Chromecast dan TV yang mendukung Cast, dan bawa semuanya di jalan dengan Apple CarPlay. Gunakan widget Layar Utama di iPhone dan iPad untuk melihat trek yang sedang diputar sekilas, dan scrobbling Last.fm untuk menyimpan riwayat mendengarkan Anda lintas aplikasi.

### Privasi dan Keamanan

Flacbox hanya menggunakan SDK resmi dan login berbasis OAuth dari setiap penyedia cloud — kata sandi Anda tidak pernah sampai ke aplikasi. Token akses disimpan terenkripsi di iOS Keychain, semua transfer dilindungi TLS, dan mencabut akses di akun cloud Anda atau menghapus Flacbox dari perangkat akan menghapus semuanya seketika. Lindungi perpustakaan Anda dengan kode sandi opsional untuk lapisan privasi ekstra.

### Memulai dengan Flacbox

Panduan ini memandu Anda melalui setiap bagian Flacbox di iPhone, iPad, dan Mac — dari menghubungkan layanan cloud, mengatur perpustakaan, mentransfer file, dan mengelola daftar putar, hingga menyetel equalizer dan mengonfigurasi mesin audio. Gunakan kartu di bawah ini untuk langsung menuju bagian yang Anda butuhkan.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigasi" subtitle="Tab Bar di iPhone, Menu Kiri di iPad dan Mac, mini player, widget, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Koneksi" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Perpustakaan Musik" subtitle="Lagu, Album, Artis, Genre, Komposer — sinkronisasi, pencarian, edit metadata." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Daftar Putar" subtitle="Buat, impor M3U / M3U8 / CUE, susun ulang, dan ekspor ke M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="File Lokal" subtitle="Musik offline, drive USB, Wi-Fi Drive, manajer file, folder offline." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Pemutar Audio" subtitle="Output hi-res, equalizer, pitch, bookmark, AirPlay, Chromecast, kecepatan, sleep timer." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Pengaturan" subtitle="Mesin audio, perpustakaan, manajer file, CarPlay, widget, personalisasi, bahasa, backup." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Temukan jawaban untuk 50 pertanyaan paling umum tentang Flacbox." >}}

{{< /cards >}}
