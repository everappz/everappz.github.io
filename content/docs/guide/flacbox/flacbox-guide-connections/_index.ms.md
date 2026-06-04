---
title: "Sambungan"
date: 2020-02-01
description: "Ketahui cara menyambungkan perkhidmatan awan dan peranti NAS ke Flacbox. Strim muzik resolusi tinggi dari iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk dan banyak lagi. Gunakan SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing dan pemacu kilat USB."
keywords: [
  "persediaan awan Flacbox", "sambungkan Google Drive ke Flacbox", "penstriman muzik SMB",
  "pemain WebDAV iOS", "aplikasi muzik DLNA", "penstriman audio NAS", "Wi-Fi Drive iPhone",
  "pindahkan fail ke iPhone", "Flacbox iTunes File Sharing", "sambungkan NAS ke iPhone",
  "aplikasi muzik Synology Drive", "aplikasi muzik QNAP", "aplikasi muzik Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "aplikasi muzik scrobbling Last.fm",
  "muzik iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["panduan", "flacbox", "sambungan", "awan", "NAS"]
readingTime: 12
---


Pada skrin ini, anda boleh menyambungkan setiap sumber yang menyimpan muzik anda. Anda boleh mengintegrasikan perkhidmatan awan popular seperti Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive dan banyak lagi, serta Mac, PC atau NAS anda melalui protokol standard. Sama ada koleksi anda berada di perkhidmatan mesra penstriman seperti Dropbox atau di NAS peribadi seperti Synology, QNAP, Buffalo, Apple Time Capsule atau WD My Cloud Home, Flacbox menyambungkan semuanya dari satu skrin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Skrin Sambungan Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Sambungkan ke Storan Awan

- Buka tab **Sambungan**.
- Pilih **Sambungkan ke storan awan** dari menu.
- Pilih perkhidmatan storan awan dari senarai.
- Masukkan kelayakan anda di halaman kebenaran rasmi yang disediakan oleh pembekal awan, kemudian ketik **Selesai**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Tambah Perkhidmatan Storan Awan" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Jika anda menghadapi masalah, semak sambungan internet dan log masuk / kata laluan anda. Dalam versi Premium aplikasi, anda boleh menambah bilangan perkhidmatan yang tidak terhad; versi percuma menyokong sehingga tiga.

## Perkhidmatan Storan Awan, Pelayan Media dan Protokol yang Disokong

Flacbox menyokong pelbagai sumber muzik yang luar biasa. Semua yang di bawah berfungsi dari satu skrin **Sambungkan ke storan awan**.

**Storan awan peribadi:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Pelayan yang dihoskan sendiri:** Plex · Jellyfin · Emby · Subsonic (dan setiap pelayan serasi Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (dan ownCloud melalui API yang dikongsi) · Synology Drive · QNAP.

**Protokol NAS dan perkongsian fail:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (Protokol Pemindahan Fail SSH, kata laluan atau pengesahan kunci awam) · NFS · DLNA / UPnP (main balik dan muat turun).

**Storan objek serasi S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces dan mana-mana titik akhir S3-API yang lain.

**Penemuan rangkaian tempatan:** Bahagian Peranti yang Tersedia menyenaraikan secara automatik setiap perkhidmatan Bonjour / mDNS pada rangkaian Wi-Fi anda supaya anda boleh mengetik untuk menyambung tanpa menaip alamat IP.

Setiap sambungan menggunakan **SDK rasmi atau protokol terbuka** perkhidmatan, dengan kebenaran berasaskan OAuth di mana disokong. Anda boleh menyambungkan berbilang akaun perkhidmatan yang sama dan menyemaknya secara serentak dalam skrin Sambungan.

## Keselamatan dan Privasi

Kami hanya menggunakan SDK rasmi dan sambungan selamat untuk berinteraksi dengan perkhidmatan awan yang disambungkan. Log masuk dan kata laluan anda tidak boleh diakses oleh aplikasi — semua pemindahan disulitkan dengan TLS.

Apabila anda memasukkan log masuk dan kata laluan, aplikasi menunjukkan halaman kebenaran rasmi yang disediakan oleh pembekal perkhidmatan awan, dan keseluruhan proses kebenaran berlaku di luar aplikasi. Pembekal perkhidmatan awan kemudian menghantar token-auth ke aplikasi selepas kebenaran berjaya, dan token itu digunakan untuk membuat panggilan API.

Token-auth adalah kunci digital yang membolehkan aplikasi pihak ketiga berinteraksi dengan storan awan bagi pihak anda. Token disimpan pada peranti anda dalam storan sistem selamat Apple (Keychain), yang disulitkan semasa rehat dan dilindungi oleh kod laluan peranti atau kunci biometrik anda. Anda boleh memuat turun fail dari perkhidmatan awan yang disambungkan ke peranti anda; fail tersebut diletakkan dalam direktori Documents aplikasi dan boleh dialih keluar pada bila-bila masa menggunakan pengurus fail terbina dalam.

Aplikasi tidak berkongsi sebarang maklumat dari akaun awan anda yang disambungkan dengan Everappz, pengiklan atau mana-mana pihak ketiga. Anda boleh membatalkan akses ke akaun awan anda pada bila-bila masa dengan membuka halaman tetapan akaun dalam pelayar web anda.

## Tolak Token-Auth

Untuk membatalkan token-auth, log masuk ke akaun awan anda dalam pelayar web dan navigasi ke halaman keselamatan atau aplikasi yang disambungkan. Di sana anda boleh mencari setiap aplikasi pihak ketiga yang disambungkan ke akaun awan anda dan mengalih keluar mana-mana daripadanya jika anda tidak lagi ingin menggunakannya. Arahan terperinci untuk akaun Google tersedia [di sini](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Anda juga boleh memutuskan sambungan akaun awan di dalam aplikasi itu sendiri — apabila anda berbuat demikian, token-auth segera dipadam dari peranti anda. Jika anda menyahpasang aplikasi dari peranti anda, semua data yang dimuat turun dan token akses dialih keluar secara automatik bersamanya.

## Putuskan Sambungan Storan Awan atau Tukar Konfigurasi

- **Akses pilihan storan awan** — cari perkhidmatan yang disambungkan dalam skrin **Sambungan**.
- **Ketik butang "..."** di sebelah tajuk perkhidmatan untuk membuka pilihan tambahan:
  - **Namakan semula** — tukar nama perkhidmatan awan seperti yang muncul dalam senarai anda.
  - **Tetapan** — ubah suai konfigurasi atau data pengesahan. Kadang-kadang anda mungkin perlu mengizinkan semula perkhidmatan awan yang disambungkan jika token kebenaran telah tamat tempoh.
  - **Putuskan Sambungan** — putuskan sepenuhnya sambungan antara aplikasi dan perkhidmatan awan. Ini mengalih keluar semua lagu yang berkaitan dengan perkhidmatan itu dari perpustakaan muzik aplikasi anda, tetapi membiarkannya tidak berubah pada pelayan.

## Sambungkan ke Komputer atau NAS

Anda juga boleh menyambungkan komputer, NAS peribadi atau peranti rangkaian lain menggunakan protokol SMB, DLNA atau WebDAV. Ini adalah cara paling mudah untuk membawa perpustakaan muzik rumah sedia ada ke dalam Flacbox tanpa menyalin apa pun.

## Sambungkan ke Komputer Menggunakan SMB

- Ketik **Sambungkan ke storan awan → SMB**.
- Masukkan alamat IP komputer dan nama folder yang dikongsi dalam medan URL menggunakan format `smb://computer-ip-address/shared-folder-name`.
- Pilih versi protokol: **Auto**, **SMB1** atau **SMB2**.
- Masukkan log masuk dan kata laluan anda (jika diperlukan).
- Ketik **Selesai**.

Jika sambungan berjaya, anda akan melihat storan yang disambungkan dalam bahagian **Storan Awan**. Tutorial penuh tentang cara menyambungkan Mac atau PC menggunakan SMB tersedia [di sini](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Sambungkan ke NAS Menggunakan WebDAV

Semua langkah adalah sama seperti SMB, kecuali untuk medan URL. URL hendaklah dalam format `http://server-name` atau `https://server-name` jika pelayan menyokong SSL. WebDAV berfungsi dengan **Synology, QNAP, Nextcloud, ownCloud** dan banyak pelayan lain.

Tutorial penuh tentang cara menyambungkan NAS menggunakan WebDAV tersedia [di sini](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Sambungkan ke Komputer atau NAS Menggunakan DLNA

Anda juga boleh berkongsi perpustakaan muzik yang terletak di Windows PC atau NAS peribadi anda menggunakan protokol DLNA / UPnP dan mengakses perpustakaan itu dalam aplikasi seperti yang diterangkan [di sini](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA adalah protokol yang popular dan disokong secara meluas, tetapi ia hanya membolehkan anda memainkan atau memuat turun muzik — anda tidak boleh memuat naik fail atau mencipta folder baru pada pelayan DLNA.

## Sambungkan ke NAS atau Pelayan Menggunakan FTP, FTPS atau SFTP

Flacbox juga menyokong protokol pemindahan fail klasik. Untuk menyambungkan pelayan melalui FTP atau FTPS, ketik **Sambungkan ke storan awan → FTP**, masukkan URL hos dalam bentuk `ftp://server-name` (atau `ftps://server-name` untuk sambungan yang disulitkan), berikan log masuk dan kata laluan anda, kemudian ketik **Selesai**. Untuk **SFTP** (Protokol Pemindahan Fail SSH), pilih **SFTP** dan berikan sama ada kata laluan atau pasangan kunci SSH.

## Sambungkan Perkongsian NFS

Flacbox termasuk sokongan **NFS** (Sistem Fail Rangkaian) — berguna untuk hos Linux, pelayan BSD dan peranti NAS. Pilih **NFS** dalam menu **Sambungkan ke storan awan**, masukkan alamat pelayan dan laluan yang dieksport, dan ketik **Selesai**.

## Sambungkan Plex Media Server

Flacbox boleh menyambung terus ke Plex Media Server dan melayari perpustakaan muzik anda mengikut Artis, Album, Genre dan Senarai Main. Ketik **Sambungkan ke storan awan → Plex**, log masuk dengan akaun Plex anda, pilih pelayan, dan perpustakaan muncul bersama perkhidmatan awan anda. Pelayan Plex pada rangkaian tempatan yang sama juga ditemui secara automatik dalam bahagian **Peranti yang Tersedia**.

## Sambungkan Pelayan Jellyfin atau Emby

Kedua-dua **Jellyfin** (sumber terbuka) dan **Emby** (komersial) berfungsi secara asli dalam Flacbox. Ketik **Sambungkan ke storan awan → Jellyfin** atau **Emby**, masukkan URL pelayan anda (seperti `http://server-ip:8096`) dan kelayakan, dan perpustakaan muzik anda sedia untuk distrim.

## Sambungkan Pelayan Subsonic atau Navidrome

Flacbox menyokong Subsonic API, yang bermakna ia berfungsi dengan **Subsonic** sendiri, **Navidrome** dan setiap pelayan serasi Subsonic lain — termasuk Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Ketik **Sambungkan ke storan awan → Subsonic**, masukkan URL pelayan dan kelayakan, dan perpustakaan muncul dalam skrin Sambungan.

## Sambungkan ke Storan Objek Serasi S3

Untuk pengguna storan objek awan, Flacbox termasuk penyambung serasi S3. Ketik **Sambungkan ke storan awan → Storan S3**, kemudian masukkan URL titik akhir, rantau, kunci akses, kunci rahsia dan nama baldi.

## Peranti yang Tersedia

Bahagian ini memaparkan setiap peranti pada rangkaian tempatan anda yang boleh anda sambungkan dari Flacbox melalui penemuan Bonjour. Untuk mewujudkan sambungan, ikuti langkah-langkah ini:

- Buka aplikasi dan pergi ke bahagian **Peranti yang Tersedia** di bawah Sambungan.
- Ketik peranti yang ingin anda sambungkan.
- Jika perlu, masukkan butiran log masuk anda untuk melengkapkan sambungan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Peranti Tersedia di Rangkaian Tempatan" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive adalah teknologi yang membolehkan pemindahan fail wayarles dari komputer anda ke peranti iOS anda melalui mana-mana pelayar desktop. Untuk menggunakan ciri ini dengan berkesan, pastikan peranti dan komputer anda disambungkan ke rangkaian Wi-Fi yang sama.

### Aktifkan Wi-Fi Drive

- Buka aplikasi dan pergi ke tab **Sambungan**.
- Pilih **Sambung melalui Wi-Fi** untuk mengakses skrin utama Wi-Fi Drive.
- (Pilihan) Tetapkan nama pengguna dan kata laluan untuk pelayan web terbenam untuk melindungi akses.
- Ketik **Mulakan Wi-Fi Drive** untuk mengaktifkan Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Akses Wi-Fi Drive di Komputer Anda

- Di komputer anda (desktop atau laptop), buka pelayar web (seperti Chrome, Firefox atau Safari).
- Dalam bar alamat pelayar, masukkan URL yang disediakan oleh aplikasi.

### Pindahkan Fail Secara Wayarles

Sebaik sahaja halaman web yang sepadan dengan peranti iOS anda dibuka dalam pelayar, anda boleh dengan mudah seret dan lepas fail dari komputer anda ke halaman web. Fail yang anda lepas akan mula dipindahkan ke peranti iOS anda dan boleh diakses di dalam Flacbox.

Anda juga boleh memasang Wi-Fi Drive terus dalam Finder di macOS (Pergi → Sambung ke Pelayan…) atau File Explorer di Windows (Peta Pemacu Rangkaian…) dan menganggap iPhone atau iPad anda sebagai pemacu rangkaian biasa.

Arahan terperinci tentang cara memindahkan fail secara wayarles menggunakan Wi-Fi Drive tersedia [di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (kini Finder File Sharing di macOS Catalina dan kemudian) adalah cara lain untuk memindahkan fail dari komputer ke peranti menggunakan kabel Lightning atau USB-C.

- Sambungkan peranti ke komputer menggunakan kabel dan jalankan **Finder** di Mac (atau **iTunes** di Windows).
- Buka **Lokasi → Peranti yang Disambungkan → Fail** dan cari aplikasi Flacbox.
- Ketik ikon aplikasi untuk melihat semua folder yang dikongsi.
- Salin fail dari komputer ke folder yang dikongsi pada peranti menggunakan seret-dan-lepas.

Arahan terperinci tentang cara menggunakan Finder File Sharing tersedia [di sini](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Sambungkan Pemacu Kilat USB

Jika anda mempunyai kad SD atau pemacu USB, anda boleh menyambungkannya menggunakan Lightning ke USB / Pembaca Kad SD atau pemacu USB-C (pada iPad dan iPhone 15 / 16 / 17 / Pro). Aplikasi menyokong pembaca kad bersertifikasi Apple dan iXpand Flash Drive. Dengan iXpand Flash Drive, masukkannya ke port Lightning dan buka aplikasi — anda akan melihat mesej Peranti Luaran Disambungkan dan maklumat peranti. Ketik ikon pemacu kilat untuk mengakses folder muzik dan ketik mana-mana fail audio untuk mula bermain.

Arahan terperinci tentang cara menyambungkan pemacu kilat USB ke iPhone anda dan mendengar muzik tersedia [di sini](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Pengurus Fail

Setelah menyambungkan perkhidmatan storan awan, ketik ikonnya untuk melihat semua fail dan folder yang tersedia. Anda boleh menggunakan pengurus fail terbina dalam untuk bekerja dengan fail ini — muat turun, namakannya semula, pindahkan, muat naik, padam dan lain-lain. Apabila anda memulakan muat turun, fail muncul dalam baris gilir pemindahan. Untuk membuka baris gilir pemindahan, pergi ke tab Fail Tempatan dan ketik ikon anak panah berputar di sudut kiri atas. Semua fail dan folder yang dimuat turun tersedia dalam bahagian Fail Tempatan.

## Bar Alat Atas

Bar alat atas, terletak dengan mudah di bawah bar navigasi, menawarkan beberapa tindakan berguna untuk akses mudah. Anda boleh menunjukkan atau menyembunyikannya dengan isyarat leret ke bawah yang mudah.

- **Cari** — lakukan carian pantas dalam direktori semasa.
- **Teruskan Main Balik** — jika diaktifkan dalam tetapan aplikasi, ini memulihkan baris gilir pemain audio dan kedudukan media terakhir untuk folder semasa.
- **Main Semua** — mengimbas folder semasa dan subfolder, kemudian menambah semua fail audio yang ditemui ke baris gilir pemain baru.
- **Kocok Semua** — seperti Main Semua, tetapi mengocok fail sebelum menambahnya ke baris gilir pemain audio.

## Pilihan Folder

Apabila anda membuka folder, anda akan menemui set tindakan yang berguna dengan mengetik butang **"..."** di sudut kanan atas.

- **Pilih** — aktifkan mod pemilihan fail. Ini membolehkan anda memilih satu atau lebih fail dalam folder dan melakukan tindakan pada keseluruhan pilihan.
- **Folder Baru** — cipta folder baru dalam folder semasa.
- **Mengaktifkan mod luar talian** — hidupkan mod luar talian untuk folder semasa. Mod luar talian memantau folder secara aktif untuk perubahan.
- **Muat Naik Fail** — muat naik fail dari peranti anda ke folder dalam talian.
- **Cari** — cari fail tertentu dalam folder semasa.
- **Isih** — isih fail mengikut nama, saiz, tarikh diubah suai atau mengikut metadata.
- **Paparan Grid / Senarai** — tukar antara paparan jadual dan paparan lakaran kecil.

## Edit Fail Dalam Talian

Apabila anda perlu mengurus berbilang fail dalam storan awan anda, gunakan **Mod Pilihan** untuk memperkemas tindakan anda:

- **Aktifkan Mod Pilihan** — ketik butang **"..."** di sudut kanan atas dan pilih **Pilih**.
- **Pilih Fail** — kotak semak muncul di sebelah setiap fail dan folder. Ketik untuk memilih satu atau beberapa item.
- **Lakukan Tindakan** — setelah memilih fail atau folder, anda akan mempunyai akses ke Main Seterusnya, Main Kemudian, Tambah ke Perpustakaan Muzik, Tambah ke Senarai Main, Salin, Muat Naik, Pindahkan, Namakan Semula dan Padam.

## Tindakan Fail

Ketik ikon **"..."** berhampiran tajuk fail untuk mendedahkan menu tindakannya:

- **Main Seterusnya** — sisipkan fail di bahagian atas baris gilir pemain, supaya ia dimainkan selepas trek semasa.
- **Main Kemudian** — tambahkan fail ke bahagian bawah baris gilir pemain.
- **Tambah ke Perpustakaan Muzik** — masukkan fail ke dalam perpustakaan muzik anda, dianjurkan mengikut artis, album, genre atau penggubah.
- **Tambah ke Senarai Main** — tambahkan fail ke senarai main sedia ada atau cipta yang baru.
- **Edit tag audio** — buka editor tag terbina dalam untuk mengubah suai metadata.
- **Tambah ke Kegemaran** — tambahkan fail ke senarai kegemaran anda untuk akses pantas.
- **Muat Turun** — muat turun fail atau folder ke peranti anda untuk kegunaan luar talian.
- **Namakan Semula** — namakannya semula fail terus pada storan jauh.
- **Pindahkan** — pindahkan fail ke folder lain dalam storan awan anda.
- **Buka Dalam** — eksport fail ke aplikasi lain yang serasi.
- **Padam** — alih keluar fail secara kekal dari storan awan anda. **Tindakan ini tidak boleh dibatalkan.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lebih Banyak Tindakan untuk Fail dalam Storan Awan yang Disambungkan" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

## Tindakan Folder

Untuk setiap folder dalam storan awan anda, pelbagai tindakan tersedia dengan mengetik ikon **"..."** di sebelah tajuk folder.

- **Main Semua** — gantikan baris gilir pemain semasa dengan setiap item dalam folder yang dipilih.
- **Main Seterusnya** — tambahkan keseluruhan folder ke bahagian atas baris gilir pemain.
- **Main Kemudian** — tambahkan kandungan folder ke bahagian bawah baris gilir pemain.
- **Tambah ke Perpustakaan Muzik** — masukkan kandungan folder ke dalam perpustakaan muzik anda.
- **Tambah ke Senarai Main** — tambahkan keseluruhan folder ke senarai main. Anda juga mempunyai pilihan untuk mencipta senarai main baru; namanya diisi secara automatik dari nama folder.
- **Tambah ke Kegemaran** — tambahkan folder ke kegemaran anda untuk akses pantas.
- **Mengaktifkan mod luar talian** — melampaui muat turun mudah, ini memantau folder secara berterusan untuk fail baru dan memuat turunnya secara automatik apabila ia muncul dalam talian.
- **Muat Turun** — muat turun semua kandungan folder ke peranti anda untuk akses luar talian.
- **Namakan Semula** — namakannya semula folder terus pada storan jauh.
- **Pindahkan** — pindahkan folder ke lokasi lain dalam storan awan anda.
- **Arkib (ZIP)** — bundel kandungan folder ke dalam satu fail ZIP (ciri Premium).
- **Padam** — alih keluar folder dan kandungannya secara kekal dari storan awan anda. **Tindakan ini tidak boleh dibatalkan.**

## Akses Pantas

Bahagian Akses Pantas terletak di bahagian atas skrin. Ia memberi anda akses pantas ke fail dan folder kegemaran dan baru-baru ini dibuka dari perkhidmatan awan yang disambungkan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Pautan Dalam Talian dan Akses Pantas" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Perkhidmatan Lain

Bahagian ini memaparkan ciri tambahan yang meningkatkan pengalaman anda. Pada masa ini, aplikasi menyokong scrobbling **Last.fm** — apabila disambungkan, statistik main balik anda dihantar secara automatik ke akaun Last.fm anda. Arahan persediaan terperinci tersedia [di sini](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Sambungan Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
