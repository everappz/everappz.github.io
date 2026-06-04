---
title: "Sambungan"
date: 2020-01-01
description: "Ketahui cara menyambungkan perkhidmatan awan, komputer, peranti NAS, dan mengurus fail muzik anda menggunakan Evermusic. Panduan langkah demi langkah untuk Wi-Fi Drive, SMB, DLNA, WebDAV, Perkongsian Fail iTunes, dan banyak lagi."
keywords: [
  "Evermusic", "pemain muzik awan", "penstriman NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "Perkongsian Fail iTunes",
  "sambung storan awan", "pemindahan muzik iPhone", "pengurus fail iOS"
]
tags: ["evermusic", "panduan", "sambungan"]
readingTime: 11
---


Pada skrin Sambungan anda boleh menyambungkan setiap sumber yang menyimpan muzik anda — perkhidmatan awan popular, pelayan media kendiri, Mac atau PC anda, NAS peribadi, Apple Time Capsule, WD My Cloud Home, malah pemacu kilat USB — dan menggunakannya semua dari satu antara muka bersepadu. Sambungan juga merupakan tempat anda menyediakan Akses Pantas ke folder awan yang bersarang dalam dan mengesahkan Last.fm untuk scrobbling.

Skrin dibahagikan kepada bahagian berlabel jelas supaya ia berskala dari satu akaun iCloud Drive ke perpustakaan yang tersebar di beberapa awan dan peranti NAS: Akses Pantas di atas (folder awan kegemaran anda), Storan awan (akaun yang telah anda tambahkan), Rangkaian tempatan (peranti yang ditemui Bonjour), Komputer (Wi-Fi Drive, Perkongsian Fail iTunes, SMB), Aksesori luaran (pemacu kilat USB yang disambungkan), dan Perkhidmatan lain (Last.fm dan seumpamanya).

{{< cards cols="1">}}
  {{< card title="" subtitle="Skrin Sambungan Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Sambung ke storan awan

- Buka tab Sambungan.
- Pilih Sambung ke storan awan dari menu.
- Pilih perkhidmatan storan awan dari senarai.
- Log masuk pada halaman kebenaran rasmi pembekal (Evermusic tidak pernah melihat kata laluan anda).
- Ketuk Selesai.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pemilih Pembekal Storan Awan yang Disambung" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Jika anda menghadapi sebarang masalah, semak semula sambungan internet dan kelayakan log masuk anda, dan pastikan pengesahan dua faktor dikonfigurasi dengan betul untuk perkhidmatan tersebut.  
Dalam versi Premium apl anda boleh menambah bilangan perkhidmatan yang tidak terhad. Pengguna percuma boleh menyambungkan satu akaun awan pada satu masa.

## Perkhidmatan storan awan yang disokong

Evermusic menyokong barisan penuh perkhidmatan awan dan kendiri yang popular. Pengguna percuma mendapat katalog pembekal yang sama tetapi dengan had satu akaun; Premium membuka kunci akaun tidak terhad dan menghapuskan kebanyakan had lain.

- **Akaun awan peribadi:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Pelayan kendiri dan perpustakaan media:** Plex · Jellyfin · Emby · Subsonic (dan setiap pelayan serasi Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (dan Owncloud, melalui API yang dikongsi) · Synology Drive · QNAP.
- **NAS dan protokol perkongsian fail:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (kata laluan atau pengesahan kunci awam), NFS, dan DLNA (baca sahaja — main balik dan muat turun).
- **Storan objek serasi S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage, atau mana-mana titik akhir API S3.
- **Penemuan rangkaian tempatan:** bahagian Peranti yang tersedia menyenaraikan secara automatik mana-mana peranti pada Wi-Fi anda yang mengiklankan dirinya melalui Bonjour / mDNS — pelayan Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, penghala AirPort dengan pemacu yang disambungkan, dan sebagainya.

## Keselamatan dan privasi

Kami hanya menggunakan SDK rasmi dan sambungan selamat untuk berinteraksi dengan perkhidmatan awan yang disambungkan. Log masuk dan kata laluan anda tidak tersedia untuk aplikasi. Semua permintaan dari aplikasi ke perkhidmatan awan adalah disulitkan.

Apabila anda memasukkan log masuk dan kata laluan anda, aplikasi menunjukkan halaman kebenaran rasmi yang disediakan oleh pembekal perkhidmatan awan dan semua proses kebenaran dibuat di luar aplikasi. Pembekal perkhidmatan awan menghantar token auth ke aplikasi selepas kebenaran berjaya dan token tersebut digunakan untuk membuat panggilan API.

Token auth ialah kunci digital yang membolehkan aplikasi pihak ketiga berinteraksi dengan storan awan. Token auth disimpan pada peranti anda dalam storan sistem selamat yang dipanggil Keychain. Anda boleh memuat turun fail anda dari perkhidmatan awan yang disambungkan ke peranti dan fail tersebut akan diletakkan dalam direktori "Dokumen" apl. Anda boleh mengalih keluar fail tersebut pada bila-bila masa menggunakan pengurus fail terbina dalam.

Aplikasi tidak berkongsi sebarang maklumat dari akaun awan yang disambungkan. Anda boleh membatalkan akses ke akaun awan anda pada bila-bila masa dengan membuka halaman tetapan akaun pada pelayar web anda.

## Tolak token auth

Log masuk ke akaun anda pada pelayar web dan navigasi ke halaman tetapan. Di sana anda boleh mencari semua apl pihak ketiga yang disambungkan ke akaun awan anda dan mengalih keluar mana-mana daripadanya jika anda tidak mahu menggunakan aplikasi tersebut lagi. Arahan terperinci tersedia [di sini](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Anda juga boleh memutuskan sambungan akaun awan yang disambungkan dalam aplikasi dan token auth juga akan dialih keluar dari peranti anda. Jika anda mengalih keluar aplikasi dari peranti anda semua data yang dimuat turun dan token akses juga akan dialih keluar.

## Putuskan sambungan storan awan atau ubah konfigurasi

- Akses Pilihan Storan Awan: pertama, cari storan awan yang ingin anda urus dalam antara muka apl.
- Ketuk Butang '...': di sebelah tajuk perkhidmatan, anda akan melihat butang '...'. Ketuk untuk mengakses pilihan tambahan.
  - **Namakan semula**: jika anda ingin menukar nama perkhidmatan awan seperti yang muncul dalam senarai anda, pilih 'Namakan semula.'
  - **Tetapan**: untuk mengubah suai konfigurasi atau data pengesahan untuk perkhidmatan awan, pilih 'Tetapan.' Kadang-kadang, anda mungkin perlu mengesahkan semula perkhidmatan awan yang disambungkan jika token kebenaran telah tamat tempoh.
  - **Putuskan Sambungan**: jika anda ingin memutuskan sepenuhnya sambungan antara apl dan perkhidmatan awan, pilih 'Putuskan Sambungan.' Sedar bahawa memilih pilihan ini akan mengalih keluar semua lagu yang berkaitan dengan perkhidmatan awan ini dari perpustakaan muzik apl anda, tetapi ia akan kekal di pelayan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Lebih banyak tindakan Storan Awan yang Disambung" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Sambung ke Komputer atau NAS

Anda juga boleh menyambungkan komputer, NAS peribadi, atau peranti rangkaian lain menggunakan protokol SMB, DLNA, atau WebDAV.

## Sambung ke komputer menggunakan SMB

- Ketuk "Sambung ke storan awan" → SMB.
- Masukkan alamat IP komputer dan nama folder dikongsi dalam medan URL menggunakan format smb://computer-ip-address/shared-folder-name
- Pilih versi protokol: Auto, SMB1, SMB2
- Masukkan log masuk dan kata laluan (jika diperlukan)
- Ketuk "Selesai".

Jika sambungan anda berjaya anda akan melihat storan yang disambungkan dalam bahagian "Storan awan".  
Tutorial penuh tentang cara menyambungkan MAC atau PC anda menggunakan SMB tersedia [di sini](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Tetapan Sambungan SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Sambung ke NAS menggunakan WebDAV

Semua langkah adalah sama kecuali medan URL.  
URL hendaklah dalam format http://server-name, atau https://server-name jika pelayan menyokong SSL.
Tutorial penuh tentang cara menyambungkan NAS menggunakan protokol WebDAV tersedia [di sini](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Tetapan Sambungan WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Sambung ke Komputer atau NAS menggunakan DLNA

Anda juga boleh berkongsi perpustakaan muzik yang terletak pada PC Windows atau NAS peribadi anda menggunakan protokol DLNA dan mengakses perpustakaan tersebut dalam apl seperti yang diterangkan [di sini](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA ialah protokol yang popular dan digunakan secara meluas, tetapi ia hanya membolehkan anda memainkan atau memuat turun muzik. Anda tidak boleh memuat naik fail atau membuat folder baru pada pelayan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tetapan Sambungan DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Peranti yang tersedia

Bahagian ini memaparkan semua peranti dalam rangkaian tempatan anda yang boleh anda sambungkan melalui aplikasi.  
Untuk mewujudkan sambungan dengan peranti, ikuti langkah-langkah berikut:

- Buka apl dan pergi ke bahagian "Peranti yang Tersedia".
- Ketuk peranti yang ingin anda sambungkan dari senarai.
- Jika diperlukan, masukkan butiran log masuk anda untuk melengkapkan sambungan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Peranti yang Tersedia di Rangkaian Tempatan" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive ialah teknologi yang mudah yang membolehkan pemindahan fail tanpa wayar dari komputer anda ke peranti iOS anda melalui pelayar desktop.  
Untuk menggunakan ciri ini dengan berkesan, pastikan peranti dan komputer anda disambungkan ke rangkaian Wi-Fi yang sama.  
Berikut ialah panduan langkah demi langkah tentang cara menggunakan Wi-Fi Drive.

## Aktifkan Wi-Fi Drive

- Buka aplikasi dan pergi ke tab "Sambungan".
- Pilih "Sambung melalui Wi-Fi" untuk mengakses skrin utama Wi-Fi Drive.
- Ketuk "Mulakan Wi-Fi Drive" untuk mengaktifkan Wi-Fi Drive.

## Akses Wi-Fi Drive pada Komputer Anda

- Pada komputer anda (desktop atau laptop), buka pelayar web (seperti Chrome, Firefox, atau Safari).
- Dalam bar alamat pelayar, masukkan URL yang disediakan oleh aplikasi.

## Pindahkan Fail Secara Tanpa Wayar

Setelah halaman web yang sepadan dengan peranti iOS anda dibuka dalam pelayar, anda boleh dengan mudah seret dan lepas fail dari komputer anda ke halaman web.  
Fail yang anda seret dan lepas akan mula dipindahkan ke peranti iOS anda dan akan dapat diakses dalam aplikasi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tetapan Pelayan Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Arahan terperinci tentang cara memindahkan fail secara tanpa wayar menggunakan WiFi-Drive tersedia [di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Perkongsian Fail iTunes

Perkongsian Fail iTunes ialah satu lagi teknologi yang membolehkan anda memindahkan fail dari komputer ke peranti menggunakan apl Finder pada Mac anda dan kabel lightning.  
- Hanya sambungkan peranti ke komputer menggunakan kabel dan jalankan apl Finder pada Mac anda.
- Buka "Lokasi" → "Peranti yang Disambungkan" → "Fail" → dan cari apl Evermusic.
- Ketuk ikon apl untuk melihat semua folder dikongsi.
- Salin fail dari komputer ke folder dikongsi pada peranti menggunakan seret dan lepas.  

Arahan terperinci tentang cara menggunakan perkongsian fail iTunes tersedia [di sini](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Perkongsian Fail iTunes / Finder pada Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Sambungkan kad kilat USB

Jika anda mempunyai kad SD, anda boleh menyambungkannya menggunakan pembaca kad lightning. Apl pada masa ini menyokong pembaca kad Apple Certified dan iXpand Flash Drive. Jika anda mempunyai iXpand Flash Drive - masukkannya ke dalam port lightning dan buka aplikasi. Anda akan melihat mesej 'Peranti luaran disambungkan' dan maklumat peranti. Hanya ketuk pada ikon pemacu kilat untuk mengakses folder muzik dan ketuk pada mana-mana fail audio untuk mula bermain. Kami mempunyai arahan terperinci tentang cara menyambungkan kad kilat USB ke iPhone dan mendengar muzik atau mengurus fail yang terletak padanya yang tersedia [di sini](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Pengurus Fail

Setelah anda menyambungkan perkhidmatan storan awan, ketuk ikonnya untuk melihat semua fail dan folder yang tersedia. Anda boleh menggunakan pengurus fail terbina dalam untuk bekerja dengan fail-fail ini — muat turun, namakan semula, alih, dan banyak lagi. Apabila anda memulakan muat turun, fail akan muncul dalam baris gilir pemindahan. Untuk melihat baris gilir pemindahan, pergi ke tab "Fail Tempatan" dan ketuk anak panah berputar di penjuru kiri atas. Semua fail dan folder yang dimuat turun tersedia dalam bahagian "Fail Tempatan".

## Bar Alat Atas

Bar alat atas, yang terletak dengan mudah di bawah bar navigasi, menawarkan beberapa tindakan berguna untuk akses mudah. Anda boleh menunjukkan atau menyembunyikan bar alat ini menggunakan isyarat luncur ke bawah yang mudah. Berikut ialah tindakan yang tersedia:

- **Cari**: Pilihan ini membolehkan anda melakukan carian pantas dalam direktori semasa, memudahkan untuk mencari fail atau folder tertentu.
- **Teruskan Main Balik**: Jika diaktifkan dalam tetapan aplikasi, ciri ini memulihkan baris gilir pemain audio dan kedudukan media terakhir untuk folder semasa. Ia ialah cara yang berguna untuk menyambung semula di tempat anda berhenti dalam perpustakaan muzik anda.
- **Main Semua**: Dengan memilih tindakan ini, apl akan mengimbas folder semasa dan subfoldernya, menambahkan semua fail audio yang ditemui ke baris gilir pemain baru. Ini berguna apabila anda ingin memainkan semua muzik dalam direktori tertentu.
- **Kocok Semua**: Sama seperti "Main Semua," tindakan ini mengimbas folder semasa dan subfoldernya tetapi mengocok fail sebelum menambahkannya ke baris gilir pemain audio. Ia ialah cara yang bagus untuk menikmati muzik anda dalam urutan rawak untuk sedikit variasi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Bar Alat Atas Dalam Folder Awan" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Pilihan Folder

Apabila anda membuka folder dalam apl, anda akan menemui satu set tindakan yang berguna dengan mengetuk butang "..." di penjuru kanan atas skrin.  
Berikut ialah pecahan tindakan-tindakan ini:

- **Pilih**: Aktifkan mod pemilihan fail. Mod ini membolehkan anda memilih satu atau lebih fail dalam folder, memudahkan untuk melaksanakan tindakan pada item yang dipilih.
- **Folder Baru**: Cipta folder baru dalam folder semasa. Ciri ini membolehkan anda mengatur fail anda dan menjaga perpustakaan anda teratur dengan baik.
- **Aktifkan Mod Luar Talian**: Togol mod luar talian untuk folder semasa. Mod luar talian melebihi muat turun mudah; ia secara aktif memantau folder untuk perubahan. Jika anda menambah fail baru ke folder dalam talian, apl akan memuat turun fail-fail ini ke peranti anda secara automatik. Ini memastikan perpustakaan tempatan anda sentiasa terkini dengan perubahan pada pelayan.
- **Muat Naik Fail**: Muat naik fail dari peranti anda ke folder dalam talian. Tindakan ini membolehkan anda memindahkan fail ke awan atau pelayan, menjadikannya boleh diakses dari mana-mana sahaja.
- **Cari**: Cari fail tertentu dalam folder semasa. Ini amat berguna untuk mencari item tertentu dengan cepat dalam koleksi yang besar.
- **Susun**: Susun fail dalam folder mengikut kriteria seperti nama, saiz, atau tarikh diedit. Mod susun lalai biasanya mencerminkan susunan pengurutan pada pelayan, tetapi anda boleh mengubahnya untuk memenuhi keutamaan anda.
- **Paparan Grid/Senarai**: Tukar antara dua mod paparan: paparan jadual dan paparan lakaran kecil. Paparan jadual menyampaikan fail dalam senarai, manakala paparan lakaran kecil memaparkan representasi visual fail, memudahkan untuk mengenal pasti kandungan secara sekilas.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Lebih banyak tindakan Folder Semasa" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Edit Fail Dalam Talian

Apabila anda perlu mengurus beberapa fail dalam storan awan anda di Evermusic, anda boleh menggunakan mod pilih untuk menyelaraskan tindakan anda. Ikuti langkah-langkah ini untuk pengurusan fail yang berkesan:

- **Aktifkan Mod Pemilihan**: Buka apl pada peranti anda dan navigasi ke bahagian yang mengandungi storan awan anda. Cari penjuru kanan atas di mana anda akan menemui butang "..." (elipsis). Ketuk padanya dan pilih item menu "Pilih" untuk mengaktifkan mod pemilihan.
- **Pilih Fail**: Anda akan melihat kotak semak muncul di sebelah setiap fail atau folder yang disenaraikan. Pilih satu atau beberapa fail atau folder dengan hanya mengetuk kotak semak di sebelahnya.
- **Laksanakan Pelbagai Tindakan**: Setelah anda memilih fail atau folder yang ingin anda urus, anda akan mempunyai akses kepada beberapa tindakan yang disesuaikan dengan keperluan anda:

{{< cards cols="1">}}
  {{< card title="" subtitle="Mod Pemilihan untuk Fail Dalam Talian" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Tindakan fail

Berhampiran tajuk fail, anda akan melihat simbol elipsis "..." (tiga titik) – ini berfungsi sebagai menu tindakan.  
Ketuk padanya untuk mendedahkan senarai tindakan yang tersedia:

- **Main Seterusnya**: Pilih tindakan ini untuk memasukkan fail yang dipilih di bahagian atas baris gilir pemain anda, memastikan ia dimainkan segera selepas item yang sedang dimainkan.
- **Main Kemudian**: Memilih pilihan ini menambah fail ke bahagian bawah baris gilir pemain anda, memastikan ia dimainkan selepas baris gilir yang sedia ada.
- **Tambah ke Perpustakaan Muzik**: Tindakan ini membolehkan anda memasukkan fail ke dalam perpustakaan muzik anda, menjadikannya mudah diakses dan tersusun rapi mengikut artis, album, genre, atau komposer.
- **Tambah ke Senarai Main**: Gunakan tindakan ini untuk menambah fail ke senarai main yang sedia ada atau cipta yang baru.
- **Edit tag audio**: Dengan memilih pilihan ini, anda boleh mengakses editor tag terbina dalam Evermusic, membolehkan anda mengubah suai tag audio untuk fail yang dipilih. Fail akan dimuat turun sementara ke direktori sementara dan kemudian dimuat naik ke storan selepas anda mengesahkan perubahan.
- **Tambah ke Kegemaran**: Tindakan ini menambah fail ke senarai fail kegemaran anda untuk akses cepat dan mudah.
- **Muat Turun**: Pilih tindakan ini untuk memuat turun fail atau folder ke peranti anda, menjadikannya boleh diakses untuk penggunaan luar talian.
- **Namakan Semula**: Pilihan ini membenarkan anda menamakan semula fail secara terus pada storan jauh, membolehkan penamaan fail yang disesuaikan.
- **Alih**: Pilih tindakan ini untuk memindahkan fail ke folder yang berbeza dalam storan awan anda, membantu dalam mengekalkan struktur fail yang teratur.
- **Buka Dalam**: Gunakan tindakan ini untuk mengeksport fail ke apl serasi lain. Fail akan dimuat turun ke peranti anda, dan kemudian dialog Kongsi akan muncul untuk perkongsian atau interaksi lanjut.
- **Padam**: Berhati-hati dengan tindakan ini, kerana ia secara kekal mengalih keluar fail dari storan awan anda. Pemadaman ini tidak boleh dibatalkan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Lebih banyak tindakan untuk Satu Fail" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Jika senarai tindakan melebihi ruang skrin yang tersedia, hanya tatal ke bawah dalam menu tindakan untuk mengakses pilihan tambahan.

## Tindakan folder

Untuk setiap folder dalam storan awan anda, anda mempunyai pelbagai tindakan yang tersedia. Untuk mengakses pilihan-pilihan ini, hanya ketuk ikon elipsis "..." yang terletak di sebelah tajuk folder. Jika anda tidak melihat semua tindakan, tatal ke bawah untuk mendedahkan lebih banyak pilihan. Berikut ialah tindakan yang tersedia:

- **Main Semua**: Gantikan baris gilir pemain semasa dengan semua item dari folder yang dipilih.
- **Main Seterusnya**: Tambah keseluruhan folder ke bahagian atas baris gilir pemain, betul-betul selepas item yang sedang dimainkan.
- **Main Kemudian**: Tambahkan kandungan folder ke bahagian bawah baris gilir pemain.
- **Tambah ke Perpustakaan Muzik**: Tindakan ini dengan lancar memasukkan kandungan folder ke dalam perpustakaan muzik anda, menjadikannya mudah diakses dan tersusun rapi mengikut artis, album, genre, atau komposer.
- **Tambah ke Senarai Main**: Anda boleh menyertakan keseluruhan folder dalam senarai main. Anda juga mempunyai pilihan untuk membuat senarai main baru, dan nama folder akan ditetapkan secara automatik.
- **Tambah ke Kegemaran**: Gunakan tindakan ini untuk menambah folder ke senarai fail kegemaran anda untuk akses cepat dan mudah.
- **Aktifkan Mod Luar Talian**: Dengan mengaktifkan mod luar talian untuk folder yang dipilih, aplikasi melebihi muat turun mudah. Ia secara berterusan mengimbas untuk perubahan, dan jika fail baru ditambah ke folder dalam talian, ia akan dimuat turun secara automatik ke apl.
- **Muat Turun**: Muat turun semua kandungan folder ke peranti anda untuk akses luar talian.
- **Namakan Semula**: Namakan semula folder secara terus pada storan jauh.
- **Alih**: Pindahkan folder ke lokasi yang berbeza dalam storan awan anda.
- **Padam**: Berhati-hati dengan tindakan ini kerana ia secara kekal mengalih keluar folder dan kandungannya dari storan awan anda. Tindakan ini tidak boleh dibatalkan.


## Akses Pantas

Bahagian Akses Pantas terletak di bahagian atas skrin. Ia memberi anda akses pantas ke fail kegemaran dan fail yang baru dibuka dari perkhidmatan awan yang disambungkan.
Setiap kali anda membuka fail atau folder dari awan, ia ditambahkan ke senarai "Baru Dibuka". Untuk mengosongkan senarai ini, buka "Terkini," ketuk butang "Lebih banyak tindakan", dan pilih "Padam Senarai." Anda juga boleh menanda folder yang bersarang dalam sebagai Kegemaran untuk mengaksesnya dengan cepat tanpa menggali melalui struktur direktori.

## Perkhidmatan Lain

Bahagian ini memaparkan ciri-ciri tambahan yang meningkatkan pengalaman anda. Pada masa ini, apl menyokong scrobbling Last.fm. Apabila disambungkan, statistik main balik anda dihantar secara automatik ke akaun Last.fm anda. Anda boleh melawati profil Last.fm anda kemudian untuk melihat analitik mendengar dan mendapatkan cadangan muzik yang diperibadikan. Arahan persediaan terperinci tersedia [di sini](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
