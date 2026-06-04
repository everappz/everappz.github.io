---
title: "Koneksi"
date: 2020-01-01
description: "Pelajari cara menghubungkan layanan cloud, komputer, perangkat NAS, dan mengelola file musik Anda menggunakan Evermusic. Panduan langkah demi langkah untuk Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing, dan lainnya."
keywords: [
  "Evermusic", "pemutar musik cloud", "streaming NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "menghubungkan penyimpanan cloud", "transfer musik iPhone", "manajer file iOS"
]
tags: ["evermusic", "panduan", "koneksi"]
readingTime: 11
---


Di layar Koneksi Anda dapat menghubungkan setiap sumber yang menyimpan musik Anda — layanan cloud populer, server media self-hosted, Mac atau PC Anda, NAS pribadi, Apple Time Capsule, WD My Cloud Home, bahkan flash drive USB — dan menggunakannya semua dari satu antarmuka terpadu. Koneksi juga merupakan tempat Anda mengatur Akses Cepat ke folder cloud yang tersarang jauh dan tempat Anda mengautentikasi Last.fm untuk scrobbling.

Layar dibagi menjadi bagian-bagian yang diberi label jelas sehingga dapat diskalakan dari satu akun iCloud Drive hingga perpustakaan yang tersebar di beberapa cloud dan perangkat NAS: Akses Cepat di bagian atas (folder cloud favorit Anda), Penyimpanan cloud (akun yang telah Anda tambahkan), Jaringan lokal (perangkat yang ditemukan Bonjour), Komputer (Wi-Fi Drive, iTunes File Sharing, SMB), Aksesori eksternal (flash drive USB yang terhubung), dan Layanan lain (Last.fm dan sejenisnya).

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Koneksi Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Hubungkan ke penyimpanan cloud

- Buka tab Koneksi.
- Pilih Hubungkan ke penyimpanan cloud dari menu.
- Pilih layanan penyimpanan cloud dari daftar.
- Masuk di halaman otorisasi resmi penyedia (Evermusic tidak pernah melihat kata sandi Anda).
- Ketuk Selesai.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pemilih Penyedia Penyimpanan Cloud" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Jika Anda mengalami masalah, periksa kembali koneksi internet dan kredensial login Anda, dan pastikan autentikasi dua faktor dikonfigurasi dengan benar untuk layanan tersebut.  
Dalam versi Premium aplikasi, Anda dapat menambahkan layanan dalam jumlah tak terbatas. Pengguna gratis dapat menghubungkan satu akun cloud sekaligus.

## Layanan penyimpanan cloud yang didukung

Evermusic mendukung seluruh rangkaian layanan cloud dan self-hosted yang populer. Pengguna gratis mendapatkan katalog penyedia yang sama tetapi dengan batasan satu akun; Premium membuka akun tak terbatas dan menghapus sebagian besar batasan lainnya.

- **Akun cloud pribadi:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Server self-hosted dan perpustakaan media:** Plex · Jellyfin · Emby · Subsonic (dan setiap server kompatibel Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (dan Owncloud, melalui API bersama) · Synology Drive · QNAP.
- **NAS dan protokol berbagi file:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (autentikasi kata sandi atau kunci publik), NFS, dan DLNA (hanya baca — pemutaran dan pengunduhan).
- **Penyimpanan objek kompatibel S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage, atau endpoint S3-API apapun.
- **Penemuan jaringan lokal:** bagian Perangkat yang Tersedia secara otomatis mencantumkan perangkat apapun di Wi-Fi Anda yang mengiklankan dirinya melalui Bonjour / mDNS — server Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, router AirPort dengan drive terpasang, dan sebagainya.

## Keamanan dan privasi

Kami hanya menggunakan SDK resmi dan koneksi aman untuk berinteraksi dengan layanan cloud yang terhubung. Login dan kata sandi Anda tidak tersedia untuk aplikasi. Semua permintaan dari aplikasi ke layanan cloud dienkripsi.

Ketika Anda memasukkan login dan kata sandi, aplikasi menampilkan halaman otorisasi resmi yang disediakan oleh penyedia layanan cloud dan semua proses otorisasi dilakukan di luar aplikasi. Penyedia layanan cloud mengirimkan token autentikasi ke aplikasi setelah otorisasi berhasil dan token tersebut digunakan untuk melakukan panggilan API.

Token autentikasi adalah kunci digital yang memungkinkan aplikasi pihak ketiga berinteraksi dengan penyimpanan cloud. Token autentikasi disimpan di perangkat Anda dalam penyimpanan sistem yang aman yang disebut Keychain. Anda dapat mengunduh file dari layanan cloud yang terhubung ke perangkat dan file-file tersebut akan ditempatkan di direktori "Documents" aplikasi. Anda dapat menghapus file tersebut kapan saja menggunakan manajer file bawaan.

Aplikasi tidak berbagi informasi apapun dari akun cloud yang terhubung. Anda dapat mencabut akses ke akun cloud Anda kapan saja dengan membuka halaman pengaturan akun di browser web Anda.

## Tolak token autentikasi

Masuk ke akun Anda di browser web dan buka halaman pengaturan. Di sana Anda dapat menemukan semua aplikasi pihak ketiga yang terhubung ke akun cloud Anda dan menghapus salah satunya jika Anda tidak ingin menggunakan aplikasi tersebut lagi. Instruksi terperinci tersedia [di sini](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Anda juga dapat memutuskan koneksi akun cloud yang terhubung di aplikasi dan token autentikasi juga akan dihapus dari perangkat Anda. Jika Anda menghapus aplikasi dari perangkat, semua data yang diunduh dan token akses juga akan dihapus.

## Putuskan koneksi penyimpanan cloud atau ubah konfigurasi

- Akses Opsi Penyimpanan Cloud: pertama, temukan penyimpanan cloud yang ingin Anda kelola di antarmuka aplikasi.
- Ketuk Tombol '...': di sebelah judul layanan, Anda akan melihat tombol '...'. Ketuk untuk mengakses opsi tambahan.
  - **Ganti nama**: jika Anda ingin mengubah nama layanan cloud seperti yang muncul di daftar Anda, pilih 'Ganti nama.'
  - **Pengaturan**: untuk mengubah konfigurasi atau data autentikasi layanan cloud, pilih 'Pengaturan.' Terkadang, Anda mungkin perlu mengotorisasi ulang layanan cloud yang terhubung jika token otorisasi telah kedaluwarsa.
  - **Putuskan Koneksi**: jika Anda ingin benar-benar memutuskan koneksi antara aplikasi dan layanan cloud, pilih 'Putuskan Koneksi.' Ketahuilah bahwa memilih opsi ini akan menghapus semua lagu yang terkait dengan layanan cloud ini dari perpustakaan musik aplikasi Anda, tetapi lagu-lagu tersebut akan tetap ada di server.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Lebih Banyak Tindakan Penyimpanan Cloud yang Terhubung" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Hubungkan ke Komputer atau NAS

Anda juga dapat menghubungkan komputer, NAS pribadi, atau perangkat jaringan lainnya menggunakan protokol SMB, DLNA, atau WebDAV.

## Hubungkan ke komputer menggunakan SMB

- Ketuk "Hubungkan ke penyimpanan cloud" → SMB.
- Masukkan alamat IP komputer dan nama folder bersama di kolom URL menggunakan format smb://computer-ip-address/shared-folder-name
- Pilih versi protokol: Auto, SMB1, SMB2
- Masukkan login dan kata sandi (jika diperlukan)
- Ketuk "Selesai".

Jika koneksi berhasil, Anda akan melihat penyimpanan yang terhubung di bagian "Penyimpanan cloud".  
Tutorial lengkap tentang cara menghubungkan MAC atau PC menggunakan SMB tersedia [di sini](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Pengaturan Koneksi SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Hubungkan ke NAS menggunakan WebDAV

Semua langkah sama kecuali pada kolom URL.  
URL harus dalam format http://server-name, atau https://server-name jika server mendukung SSL.
Tutorial lengkap tentang cara menghubungkan NAS menggunakan protokol WebDAV tersedia [di sini](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Pengaturan Koneksi WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Hubungkan ke Komputer atau NAS menggunakan DLNA

Anda juga dapat berbagi perpustakaan musik yang terletak di PC Windows atau NAS pribadi menggunakan protokol DLNA dan mengakses perpustakaan tersebut di aplikasi seperti yang dijelaskan [di sini](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA adalah protokol yang populer dan banyak digunakan, tetapi hanya memungkinkan Anda memutar atau mengunduh musik. Anda tidak dapat mengunggah file atau membuat folder baru di server.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pengaturan Koneksi DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Perangkat yang Tersedia

Bagian ini menampilkan semua perangkat dalam jaringan lokal Anda yang dapat Anda hubungkan melalui aplikasi.  
Untuk membuat koneksi dengan perangkat, ikuti langkah-langkah berikut:

- Buka aplikasi dan buka bagian "Perangkat yang Tersedia".
- Ketuk perangkat yang ingin Anda hubungkan dari daftar.
- Jika diperlukan, masukkan detail login Anda untuk menyelesaikan koneksi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Perangkat yang Tersedia di Jaringan Lokal" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive adalah teknologi praktis yang memungkinkan transfer file nirkabel dari komputer ke perangkat iOS Anda melalui browser desktop.  
Untuk menggunakan fitur ini secara efektif, pastikan perangkat dan komputer Anda terhubung ke jaringan Wi-Fi yang sama.  
Berikut panduan langkah demi langkah tentang cara menggunakan Wi-Fi Drive.

## Aktifkan Wi-Fi Drive

- Buka aplikasi dan buka tab "Koneksi".
- Pilih "Hubungkan melalui Wi-Fi" untuk mengakses layar utama Wi-Fi Drive.
- Ketuk "Mulai Wi-Fi Drive" untuk mengaktifkan Wi-Fi Drive.

## Akses Wi-Fi Drive di Komputer Anda

- Di komputer Anda (desktop atau laptop), buka browser web (seperti Chrome, Firefox, atau Safari).
- Di bilah alamat browser, masukkan URL yang disediakan oleh aplikasi.

## Transfer File Secara Nirkabel

Setelah halaman web yang sesuai dengan perangkat iOS Anda terbuka di browser, Anda dapat dengan mudah menyeret dan melepas file dari komputer ke halaman web.  
File yang Anda seret dan lepas akan mulai ditransfer ke perangkat iOS Anda dan akan dapat diakses di dalam aplikasi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pengaturan Server Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Instruksi terperinci tentang cara mentransfer file secara nirkabel menggunakan WiFi-Drive tersedia [di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing adalah teknologi lain yang memungkinkan Anda mentransfer file dari komputer ke perangkat menggunakan aplikasi Finder di Mac dan kabel lightning.  
- Cukup hubungkan perangkat ke komputer menggunakan kabel dan jalankan aplikasi Finder di Mac Anda.
- Buka "Lokasi" → "Perangkat yang Terhubung" → "File" → dan temukan aplikasi Evermusic.
- Ketuk ikon aplikasi untuk melihat semua folder bersama.
- Salin file dari komputer ke folder bersama di perangkat menggunakan drag-and-drop.

Instruksi terperinci tentang cara menggunakan iTunes file sharing tersedia [di sini](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing di Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Hubungkan flash drive USB

Jika Anda memiliki kartu SD, Anda dapat menghubungkannya menggunakan pembaca kartu lightning. Aplikasi saat ini mendukung pembaca kartu Apple Certified dan iXpand Flash Drive. Jika Anda memiliki iXpand Flash Drive - masukkan ke port lightning dan buka aplikasi. Anda akan melihat pesan 'Perangkat eksternal terhubung' dan informasi perangkat. Cukup ketuk ikon flash drive untuk mengakses folder musik dan ketuk file audio manapun untuk mulai memutar. Kami memiliki instruksi terperinci tentang cara menghubungkan flash drive USB ke iPhone dan mendengarkan musik atau mengelola file yang ada di dalamnya, yang tersedia [di sini](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Manajer File

Setelah Anda menghubungkan layanan penyimpanan cloud, ketuk ikonnya untuk melihat semua file dan folder yang tersedia. Anda dapat menggunakan manajer file bawaan untuk bekerja dengan file-file ini — mengunduh, mengganti nama, memindahkan, dan banyak lagi. Ketika Anda memulai unduhan, file akan muncul di antrean transfer. Untuk melihat antrean transfer, buka tab "File Lokal" dan ketuk ikon panah berputar di sudut kiri atas. Semua file dan folder yang diunduh tersedia di bagian "File Lokal".

## Toolbar Atas

Toolbar atas, yang terletak di bawah bilah navigasi, menawarkan beberapa tindakan berguna untuk akses mudah. Anda dapat menampilkan atau menyembunyikan toolbar ini menggunakan gerakan gesek ke bawah yang sederhana. Berikut tindakan yang tersedia:

- **Cari**: opsi ini memungkinkan Anda melakukan pencarian cepat di direktori saat ini, sehingga mudah menemukan file atau folder tertentu.
- **Lanjutkan Pemutaran**: jika diaktifkan di pengaturan aplikasi, fitur ini memulihkan antrean pemutar audio dan posisi media terakhir untuk folder saat ini. Ini adalah cara praktis untuk melanjutkan dari tempat Anda berhenti di perpustakaan musik Anda.
- **Putar Semua**: dengan memilih tindakan ini, aplikasi akan memindai folder saat ini dan sub-foldernya, menambahkan semua file audio yang ditemukan ke antrean pemutar baru. Ini berguna ketika Anda ingin memutar semua musik dalam direktori tertentu.
- **Acak Semua**: mirip dengan "Putar Semua," tindakan ini memindai folder saat ini dan sub-foldernya tetapi mengacak file sebelum menambahkannya ke antrean pemutar audio. Ini adalah cara yang bagus untuk menikmati musik Anda dalam urutan acak untuk sedikit variasi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Toolbar Atas di Dalam Folder Cloud" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Opsi Folder

Ketika Anda membuka folder dalam aplikasi, Anda akan menemukan serangkaian tindakan yang berguna dengan mengetuk tombol "..." di sudut kanan atas layar.  
Berikut uraian tindakan-tindakan tersebut:

- **Pilih**: aktifkan mode pemilihan file. Mode ini memungkinkan Anda memilih satu atau lebih file dalam folder, sehingga mudah melakukan tindakan pada item yang dipilih.
- **Folder Baru**: buat folder baru di dalam folder saat ini. Fitur ini memungkinkan Anda mengatur file dan menjaga perpustakaan Anda terstruktur dengan baik.
- **Aktifkan Mode Offline**: aktifkan mode offline untuk folder saat ini. Mode offline melampaui pengunduhan sederhana; ia secara aktif memantau perubahan folder. Jika Anda menambahkan file baru ke folder secara online, aplikasi akan secara otomatis mengunduh file-file ini ke perangkat Anda. Ini memastikan perpustakaan lokal Anda tetap terkini dengan perubahan di server.
- **Unggah File**: unggah file dari perangkat Anda ke folder online. Tindakan ini memungkinkan Anda mentransfer file ke cloud atau server, sehingga dapat diakses dari mana saja.
- **Cari**: cari file tertentu di dalam folder saat ini. Ini sangat berguna untuk menemukan item tertentu dengan cepat dalam koleksi besar.
- **Urutkan**: urutkan file dalam folder berdasarkan kriteria seperti nama, ukuran, atau tanggal pengeditan. Mode pengurutan default biasanya mencerminkan urutan pengurutan di server, tetapi Anda dapat mengubahnya sesuai preferensi.
- **Tampilan Grid/Daftar**: beralih antara dua mode tampilan: tampilan tabel dan tampilan gambar mini. Tampilan tabel menyajikan file dalam daftar, sementara tampilan gambar mini menampilkan representasi visual dari file, sehingga lebih mudah mengidentifikasi konten sekilas.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Lebih Banyak Tindakan Folder Saat Ini" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Edit File Online

Ketika Anda perlu mengelola beberapa file dalam penyimpanan cloud Anda di Evermusic, Anda dapat menggunakan mode pilih untuk menyederhanakan tindakan Anda. Ikuti langkah-langkah berikut untuk manajemen file yang efektif:

- **Aktifkan Mode Pemilihan**: buka aplikasi di perangkat Anda dan navigasi ke bagian yang berisi penyimpanan cloud Anda. Cari tombol "..." (elipsis) di sudut kanan atas. Ketuk dan pilih item menu "Pilih" untuk mengaktifkan mode pemilihan.
- **Pilih File**: Anda akan melihat kotak centang muncul di sebelah setiap file atau folder yang terdaftar. Pilih satu atau beberapa file atau folder dengan mengetuk kotak centang di sebelahnya.
- **Lakukan Berbagai Tindakan**: setelah Anda memilih file atau folder yang ingin dikelola, Anda akan memiliki akses ke beberapa tindakan yang disesuaikan dengan kebutuhan Anda.

{{< cards cols="1">}}
  {{< card title="" subtitle="Mode Pemilihan untuk File Online" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Tindakan file

Di dekat judul file, Anda akan melihat simbol elipsis "..." (tiga titik) — ini berfungsi sebagai menu tindakan.  
Ketuk untuk memperlihatkan daftar tindakan yang tersedia:

- **Putar Berikutnya**: pilih tindakan ini untuk menyisipkan file yang dipilih di bagian atas antrean pemutar Anda, memastikannya diputar segera setelah item yang sedang diputar.
- **Putar Nanti**: memilih opsi ini menambahkan file ke bagian bawah antrean pemutar Anda, memastikannya diputar setelah antrean yang ada.
- **Tambahkan ke Perpustakaan Musik**: tindakan ini memungkinkan Anda memasukkan file ke perpustakaan musik Anda, sehingga mudah diakses dan terorganisir rapi berdasarkan artis, album, genre, atau komposer.
- **Tambahkan ke Daftar Putar**: gunakan tindakan ini untuk menambahkan file ke daftar putar yang sudah ada atau membuat yang baru.
- **Mengedit tag audio**: dengan memilih opsi ini, Anda dapat mengakses editor tag bawaan Evermusic, yang memungkinkan Anda mengubah tag audio untuk file yang dipilih. File akan diunduh sementara ke direktori sementara lalu diunggah ke penyimpanan setelah Anda mengonfirmasi perubahan.
- **Tambahkan ke Favorit**: tindakan ini menambahkan file ke daftar file favorit Anda untuk akses cepat dan mudah.
- **Unduh**: pilih tindakan ini untuk mengunduh file atau folder ke perangkat Anda, sehingga dapat diakses untuk digunakan offline.
- **Ganti Nama**: opsi ini memungkinkan Anda mengganti nama file langsung di penyimpanan jarak jauh, memungkinkan penamaan file yang disesuaikan.
- **Pindah**: pilih tindakan ini untuk memindahkan file ke folder berbeda dalam penyimpanan cloud Anda, membantu menjaga struktur file yang terorganisir.
- **Buka Dengan**: gunakan tindakan ini untuk mengekspor file ke aplikasi kompatibel lainnya. File akan diunduh ke perangkat Anda, lalu dialog Berbagi akan muncul untuk berbagi atau interaksi lebih lanjut.
- **Hapus**: berhati-hatilah dengan tindakan ini, karena tindakan ini menghapus file dari penyimpanan cloud Anda secara permanen. Penghapusan ini tidak dapat dibatalkan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Lebih Banyak Tindakan untuk Satu File" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Jika daftar tindakan melebihi ruang layar yang tersedia, gulir ke bawah di dalam menu tindakan untuk mengakses opsi tambahan.

## Tindakan folder

Untuk setiap folder dalam penyimpanan cloud Anda, berbagai tindakan tersedia. Untuk mengakses opsi ini, cukup ketuk ikon elipsis "..." yang terletak di sebelah judul folder. Jika Anda tidak melihat semua tindakan, gulir ke bawah untuk memperlihatkan lebih banyak pilihan. Berikut tindakan yang tersedia:

- **Putar Semua**: ganti antrean pemutar saat ini dengan semua item dari folder yang dipilih.
- **Putar Berikutnya**: tambahkan seluruh folder ke bagian atas antrean pemutar, tepat setelah item yang sedang diputar.
- **Putar Nanti**: tambahkan konten folder ke bagian bawah antrean pemutar.
- **Tambahkan ke Perpustakaan Musik**: tindakan ini secara mulus memasukkan konten folder ke perpustakaan musik Anda, sehingga mudah diakses dan terorganisir berdasarkan artis, album, genre, atau komposer.
- **Tambahkan ke Daftar Putar**: Anda dapat menyertakan seluruh folder dalam daftar putar. Anda juga memiliki opsi untuk membuat daftar putar baru, dan nama folder akan ditetapkan secara otomatis.
- **Tambahkan ke Favorit**: gunakan tindakan ini untuk menambahkan folder ke daftar file favorit Anda untuk akses cepat dan mudah.
- **Aktifkan Mode Offline**: dengan mengaktifkan mode offline untuk folder yang dipilih, aplikasi melampaui pengunduhan sederhana. Aplikasi terus memindai perubahan, dan jika file baru ditambahkan ke folder online, file tersebut akan diunduh secara otomatis ke aplikasi.
- **Unduh**: unduh semua konten folder ke perangkat Anda untuk akses offline.
- **Ganti Nama**: ganti nama folder langsung di penyimpanan jarak jauh.
- **Pindah**: pindahkan folder ke lokasi berbeda dalam penyimpanan cloud Anda.
- **Hapus**: berhati-hatilah dengan tindakan ini karena tindakan ini menghapus folder dan isinya dari penyimpanan cloud Anda secara permanen. Tindakan ini tidak dapat dibatalkan.


## Akses Cepat

Bagian Akses Cepat terletak di bagian atas layar. Ini memberi Anda akses cepat ke file favorit dan yang baru dibuka dari layanan cloud yang terhubung.
Setiap kali Anda membuka file atau folder dari cloud, file tersebut ditambahkan ke daftar "Baru Dibuka". Untuk menghapus daftar ini, buka "Terbaru," ketuk tombol "Lebih banyak tindakan", dan pilih "Hapus Daftar." Anda juga dapat menandai folder yang tersarang jauh sebagai Favorit untuk mengaksesnya dengan cepat tanpa harus menggali melalui struktur direktori.

## Layanan Lain

Bagian ini menampilkan fitur ekstra yang meningkatkan pengalaman Anda. Saat ini, aplikasi mendukung scrobbling Last.fm. Saat terhubung, statistik pemutaran Anda secara otomatis dikirim ke akun Last.fm Anda. Anda dapat mengunjungi profil Last.fm Anda nanti untuk melihat analitik mendengarkan dan mendapatkan rekomendasi musik yang dipersonalisasi. Instruksi pengaturan terperinci tersedia [di sini](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
