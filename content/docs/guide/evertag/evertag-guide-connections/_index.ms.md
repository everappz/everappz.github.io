---
title: "Sambungan"
date: 2020-02-01
description: "Ketahui cara menyambungkan storan awan, NAS, dan komputer anda ke Evertag. Akses dan sunting fail audio terus dari storan awan, NAS peribadi, atau Mac/PC."
keywords: [
  "persediaan awan Evertag", "sambung iCloud ke Evertag", "akses fail SMB iOS",
  "penyunting tag audio WebDAV", "pengeditan metadata NAS", "Wi-Fi Drive Evertag",
  "pindahkan fail audio ke iPhone", "iTunes File Sharing Evertag", "sunting tag FLAC dari awan"
]
tags: ["panduan", "evertag", "sambungan"]
readingTime: 11
---


Pada skrin ini, anda boleh menyambungkan pelbagai sumber yang mengandungi fail audio anda. Anda boleh menyepadukan perkhidmatan awan popular seperti Google Drive, Dropbox, OneDrive, iCloud, dan lain-lain, serta menyambungkan Mac atau PC anda. Selain itu, anda mempunyai pilihan untuk menyunting fail audio yang terletak di Apple Time Capsule, WD Cloud Home, atau mana-mana NAS yang menggunakan SMB atau WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Skrin Sambungan Evertag" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Akses pantas

Di bahagian atas skrin Sambungan anda akan menemui senarai **Akses pantas**. Mana-mana folder awan yang anda tambahkan ke kegemaran — walaupun yang tersembunyi beberapa aras dalam — muncul di sini supaya anda boleh melompat ke dalamnya tanpa perlu menavigasi folder induk setiap kali.

## Sambungkan ke storan awan

- Buka tab 'Sambungan'  
- Pilih 'Sambungkan ke storan awan' dari menu  
- Pilih perkhidmatan storan awan dari senarai  
- Masukkan kelayakan anda, dan ketik 'Selesai.'

Jika anda menghadapi sebarang masalah, pastikan anda menyemak sambungan internet dan log masuk/kata laluan anda.  
Dalam versi Premium aplikasi, anda boleh menambah bilangan perkhidmatan tanpa had.

## Perkhidmatan storan awan yang disokong

Pada masa ini, aplikasi menyokong perkhidmatan storan awan paling popular: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), serta mana-mana pelayan SMB atau WebDAV.

## Keselamatan dan privasi

Kami hanya menggunakan SDK rasmi dan sambungan selamat untuk berinteraksi dengan perkhidmatan awan yang disambungkan. Log masuk dan kata laluan anda tidak boleh diakses oleh aplikasi. Semua permintaan dari aplikasi ke perkhidmatan awan adalah disulitkan.

Apabila anda memasukkan log masuk dan kata laluan, aplikasi menunjukkan halaman kebenaran rasmi yang disediakan oleh pembekal perkhidmatan awan, dan keseluruhan proses kebenaran berlaku di luar aplikasi. Pembekal perkhidmatan awan menghantar token pengesahan ke aplikasi selepas kebenaran berjaya, dan token tersebut digunakan untuk membuat panggilan API.

Token pengesahan adalah kunci digital yang membolehkan aplikasi pihak ketiga berinteraksi dengan storan awan. Token pengesahan disimpan di peranti anda dalam storan sistem selamat yang dipanggil Keychain. Anda boleh memuat turun fail anda dari perkhidmatan awan yang disambungkan ke peranti, dan fail tersebut akan ditempatkan dalam direktori "Dokumen" aplikasi. Anda boleh membuang fail tersebut bila-bila masa menggunakan pengurus fail terbina dalam.

Aplikasi tidak berkongsi sebarang maklumat dari akaun awan yang disambungkan. Anda boleh membatalkan akses ke akaun awan anda pada bila-bila masa dengan membuka halaman tetapan akaun dalam pelayar web anda.

## Tolak token auth

Log masuk ke akaun anda dalam pelayar web dan navigasi ke halaman tetapan. Di sana, anda boleh menemui semua aplikasi pihak ketiga yang disambungkan ke akaun awan anda dan membuang mana-mana daripadanya jika anda tidak lagi mahu menggunakan aplikasi tersebut. Arahan terperinci tersedia [di sini](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Anda juga boleh memutuskan sambungan akaun awan yang disambungkan dalam aplikasi, dan token pengesahan juga akan dibuang dari peranti anda. Jika anda membuang aplikasi dari peranti anda, semua data yang dimuat turun dan token akses juga akan dibuang.

## Putuskan sambungan storan awan atau ubah konfigurasi

- Akses Pilihan Storan Awan: Pertama, cari storan awan yang ingin anda urus dalam antara muka aplikasi.  
- Ketik Butang '...': Di sebelah tajuk perkhidmatan, anda akan melihat butang '...'. Ketik padanya untuk mengakses pilihan tambahan.  
  - **Namakan semula**: Jika anda ingin menukar nama perkhidmatan awan seperti yang muncul dalam senarai anda, pilih 'Namakan semula.'  
  - **Tetapan**: Untuk mengubah suai konfigurasi atau data pengesahan untuk perkhidmatan awan, pilih 'Tetapan.' Kadang-kadang, anda mungkin perlu membenarkan semula perkhidmatan awan yang disambungkan jika token kebenaran telah tamat tempoh.  
  - **Putuskan Sambungan**: Jika anda ingin memutuskan sepenuhnya sambungan antara aplikasi dan perkhidmatan awan, pilih 'Putuskan Sambungan.' Sedar bahawa memilih pilihan ini akan membuang semua lagu yang berkaitan dengan perkhidmatan awan ini dari perpustakaan muzik aplikasi anda, tetapi ia akan kekal di pelayan.

## Sambungkan ke Komputer atau NAS

Anda juga boleh menyambungkan komputer, NAS peribadi, atau peranti rangkaian lain menggunakan protokol SMB, DLNA, atau WebDAV.

## Sambungkan ke komputer menggunakan SMB

- Ketik "Sambungkan ke storan awan" → SMB.  
- Masukkan alamat IP komputer dan nama folder kongsi dalam medan URL menggunakan format smb://alamat-ip-komputer/nama-folder-kongsi  
- Pilih versi protokol: Auto, SMB1, SMB2  
- Masukkan log masuk dan kata laluan (jika diperlukan)  
- Ketik "Selesai."

Jika sambungan anda berjaya, anda akan melihat storan yang disambungkan dalam bahagian "Storan awan".  
Tutorial lengkap tentang cara menyambungkan Mac atau PC anda menggunakan SMB tersedia [di sini](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Sambungkan ke NAS menggunakan WebDAV

Semua langkah adalah sama kecuali untuk medan URL.  
URL hendaklah dalam format http://nama-pelayan, atau https://nama-pelayan jika pelayan menyokong SSL.  
Tutorial lengkap tentang cara menyambungkan NAS menggunakan protokol WebDAV tersedia [di sini](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Peranti yang tersedia

Bahagian ini memaparkan semua peranti dalam rangkaian tempatan anda yang boleh anda sambungkan melalui aplikasi.  
Untuk menjalin sambungan dengan peranti, ikuti langkah-langkah ini:

- Buka aplikasi dan pergi ke bahagian "Peranti yang Tersedia".  
- Ketik peranti yang ingin anda sambungkan dari senarai.  
- Jika perlu, masukkan butiran log masuk anda untuk melengkapkan sambungan.

## Wi-Fi Drive 

Wi-Fi Drive adalah teknologi mudah yang membolehkan pemindahan fail tanpa wayar dari komputer ke peranti iOS anda melalui pelayar desktop.  
Untuk menggunakan ciri ini dengan berkesan, pastikan peranti dan komputer anda disambungkan ke rangkaian Wi-Fi yang sama.  
Berikut adalah panduan langkah demi langkah tentang cara menggunakan Wi-Fi Drive.

## Aktifkan Wi-Fi Drive

- Buka aplikasi dan pergi ke tab "Sambungan".  
- Pilih "Sambung melalui Wi-Fi" untuk mengakses skrin utama Wi-Fi Drive.  
- Ketik "Mulakan Wi-Fi Drive" untuk mengaktifkan Wi-Fi Drive.

## Akses Wi-Fi Drive pada Komputer Anda

- Pada komputer anda (desktop atau laptop), buka pelayar web (seperti Chrome, Firefox, atau Safari).  
- Dalam bar alamat pelayar, masukkan URL yang disediakan oleh aplikasi.

## Pindahkan Fail Secara Tanpa Wayar

Setelah halaman web yang sepadan dengan peranti iOS anda dibuka dalam pelayar, anda boleh dengan mudah menyeret dan menjatuhkan fail dari komputer anda ke halaman web.  
Fail yang anda seret dan jatuhkan akan mula dipindahkan ke peranti iOS anda dan akan boleh diakses dalam aplikasi.

Arahan terperinci tentang cara memindahkan fail secara tanpa wayar menggunakan Wi-Fi Drive tersedia [di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing adalah teknologi lain yang membolehkan anda memindahkan fail dari komputer ke peranti menggunakan aplikasi Finder di Mac dan kabel Lightning.  
- Hanya sambungkan peranti ke komputer menggunakan kabel dan jalankan aplikasi Finder di Mac anda.  
- Buka "Lokasi" → "Peranti yang Disambungkan" → "Fail" → dan cari aplikasi semasa.  
- Ketik ikon aplikasi untuk melihat semua folder kongsi.  
- Salin fail dari komputer ke folder kongsi pada peranti menggunakan seret dan lepas.

Arahan terperinci tentang cara menggunakan iTunes File Sharing tersedia [di sini](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Sambungkan kad kilat USB

Jika anda mempunyai kad SD atau pemacu kilat USB, anda boleh menyambungkannya menggunakan pembaca kad Lightning atau USB-C pada iPhone/iPad, atau pasangkan terus ke Mac. Aplikasi ini pada masa ini menyokong pembaca kad Bersertifikat Apple. Kami mempunyai arahan terperinci tentang cara menyambungkan kad kilat USB ke iPhone atau iPad anda dan mengurus fail yang terletak padanya, tersedia [di sini](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Pemacu yang disambungkan muncul dalam bahagian **Aksesori luaran** skrin Sambungan.

## Pengurus Fail

Setelah anda menyambungkan perkhidmatan storan awan, ketik ikonnya untuk melihat semua fail dan folder yang tersedia. Anda boleh menggunakan pengurus fail terbina dalam untuk bekerja dengan fail ini — muat turun, namakan semula, alih, dan banyak lagi. Apabila anda memulakan muat turun, fail akan muncul dalam baris gilir pemindahan. Untuk melihat baris gilir pemindahan, pergi ke tab "Fail Tempatan" dan ketik anak panah berputar di sudut kiri atas. Semua fail dan folder yang dimuat turun tersedia dalam bahagian "Fail Tempatan".

## Bar Alat Atas

Bar alat atas, yang terletak dengan mudah di bawah bar navigasi, menawarkan beberapa tindakan berguna untuk akses mudah. Anda boleh menunjukkan atau menyembunyikan bar alat ini dengan menggunakan gerak isyarat leret ke bawah yang mudah. Berikut adalah tindakan yang tersedia:

- **Cari**: Pilihan ini membolehkan anda melakukan carian pantas dalam direktori semasa, memudahkan mencari fail atau folder tertentu.  

## Pilihan Folder

Apabila anda membuka folder dalam aplikasi, anda akan menemui set tindakan berguna yang tersedia dengan mengetik butang "..." di sudut kanan atas skrin.  
Berikut adalah pecahan tindakan ini:

- **Pilih**: Aktifkan mod pemilihan fail. Mod ini membolehkan anda memilih satu atau lebih fail dalam folder, memudahkan untuk melakukan tindakan pada item yang dipilih.  
- **Folder Baru**: Buat folder baru dalam folder semasa. Ciri ini membolehkan anda mengatur fail anda dan memastikan perpustakaan anda teratur dengan baik.   
- **Muat Naik Fail**: Muat naik fail dari peranti anda ke folder dalam talian. Tindakan ini membolehkan anda memindahkan fail ke awan atau pelayan, menjadikannya boleh diakses dari mana-mana.  
- **Cari**: Cari fail tertentu dalam folder semasa. Ini amat berguna untuk mencari item tertentu dengan cepat dalam koleksi yang besar.  
- **Isih**: Isih fail dalam folder mengikut kriteria seperti nama, saiz, atau tarikh diedit. Mod isih lalai biasanya mencerminkan susunan pengisihan pada pelayan, tetapi anda boleh mengubahnya mengikut keutamaan anda.  
- **Paparan Grid/Senarai**: Tukar antara dua mod paparan: paparan jadual dan paparan lakaran kecil. Paparan jadual menyajikan fail dalam senarai, manakala paparan lakaran kecil memaparkan representasi visual fail, memudahkan pengenalpastian kandungan secara sekilas.

{{< cards cols="1">}}
  {{< card title="" subtitle="Isih Folder Awan Evertag" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Sunting Fail Dalam Talian

Apabila anda perlu mengurus berbilang fail dalam storan awan anda pada aplikasi ini, anda boleh menggunakan mod pilih untuk menyelaraskan tindakan anda. Ikuti langkah-langkah ini untuk pengurusan fail yang berkesan:

- **Aktifkan Mod Pemilihan**: Buka aplikasi pada peranti anda dan navigasi ke bahagian yang mengandungi storan awan anda. Cari sudut kanan atas di mana anda akan menemui butang "..." (elipsis). Ketik padanya dan pilih item menu "Pilih" untuk mengaktifkan mod pemilihan.  
- **Pilih Fail**: Anda akan melihat kotak semak muncul di sebelah setiap fail atau folder yang disenaraikan. Pilih satu atau berbilang fail atau folder dengan hanya mengetik kotak semak di sebelahnya.  
- **Lakukan Pelbagai Tindakan**: Setelah anda memilih fail atau folder yang ingin anda urus, anda akan mempunyai akses kepada beberapa tindakan yang disesuaikan mengikut keperluan anda:

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilih Fail Evertag" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Tindakan fail

Berhampiran tajuk fail, anda akan melihat simbol elipsis "..." (tiga titik) – ini berfungsi sebagai menu tindakan.  
Ketik padanya untuk mendedahkan senarai tindakan yang tersedia:

- **Edit tag audio**: Dengan memilih pilihan ini, anda boleh mengakses penyunting tag terbina dalam, membolehkan anda mengubah suai tag audio untuk fail yang dipilih. Fail akan dimuat turun sementara ke direktori sementara dan kemudian dimuat naik ke storan selepas anda mengesahkan perubahan.  
- **Tambah ke Kegemaran**: Tindakan ini menambahkan fail ke senarai fail kegemaran anda untuk akses yang cepat dan mudah.  
- **Muat Turun**: Pilih tindakan ini untuk memuat turun fail atau folder ke peranti anda, menjadikannya boleh diakses untuk kegunaan luar talian.  
- **Namakan semula**: Pilihan ini membolehkan anda menamakan semula fail terus pada storan jauh, membolehkan penamaan fail tersuai.  
- **Alih**: Pilih tindakan ini untuk memindahkan fail ke folder lain dalam storan awan anda, membantu dalam mengekalkan struktur fail yang teratur.  
- **Buka Dalam**: Gunakan tindakan ini untuk mengeksport fail ke aplikasi lain yang serasi. Fail akan dimuat turun ke peranti anda, dan kemudian dialog Kongsi akan muncul untuk perkongsian atau interaksi selanjutnya.  
- **Padam**: Berhati-hati dengan tindakan ini, kerana ia membuang fail dari storan awan anda secara kekal. **Pemadaman ini tidak boleh dibatalkan**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilihan Fail Evertag" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Jika senarai tindakan melebihi ruang skrin yang tersedia, tatal ke bawah dalam menu tindakan untuk mengakses pilihan tambahan.

## Tindakan folder

Untuk setiap folder dalam storan awan anda, pelbagai tindakan tersedia. Untuk mengakses pilihan ini, hanya ketik ikon elipsis "..." yang terletak di sebelah tajuk folder. Jika anda tidak melihat semua tindakan, tatal ke bawah untuk mendedahkan lebih banyak pilihan. Berikut adalah tindakan yang tersedia:

- **Tambah ke Kegemaran**: Gunakan tindakan ini untuk menambahkan folder ke senarai fail kegemaran anda untuk akses yang cepat dan mudah.  
- **Muat Turun**: Muat turun semua kandungan folder ke peranti anda untuk akses luar talian.  
- **Namakan semula**: Namakan semula folder terus pada storan jauh.  
- **Alih**: Pindahkan folder ke lokasi lain dalam storan awan anda.  
- **Padam**: Berhati-hati dengan tindakan ini, kerana ia membuang folder dan kandungannya dari storan awan anda secara kekal. **Tindakan ini tidak boleh dibatalkan**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilihan Folder Evertag" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
