---
title: "Cara Menyiapkan Media Server DLNA/UPnP di iPhone & iPad untuk Streaming"
description: "Ubah iPhone atau iPad Anda jadi media server DLNA/UPnP dengan Everdisk dan streaming foto, video, serta musik ke smart TV, konsol game, VLC, atau Kodi lewat Wi-Fi. Panduan lengkap plus cara menyambung dari TV Samsung, LG, dan Sony, Windows, Mac, Linux, Android, serta iPhone lain."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "media server", "streaming", "smart tv", "iphone", "ipad", "wifi"]
keywords: ["server DLNA iPhone", "server UPnP iPad", "cara menyiapkan DLNA di iPhone", "streaming ke smart TV dari iPhone", "media server DLNA iOS", "streaming video ke TV tanpa kabel", "putar foto iPhone di TV", "TV Samsung DLNA iPhone", "TV LG DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "media server DLNA Kodi", "media server UPnP AV iOS", "streaming musik ke TV dari iPhone", "aplikasi media server iPhone"]
readingTime: 9
---

{{< author-byline >}}

DLNA (disebut juga UPnP AV) adalah mesin senyap di balik sebagian besar smart TV. Ini adalah bahasa bersama yang memungkinkan TV atau pemutar media menemukan koleksi media di Wi-Fi yang sama lalu memutarnya, tanpa perlu memasang apa pun di TV. Jika iPhone atau iPad Anda bisa berperan sebagai koleksi itu, foto, video, dan musik Anda muncul sendiri di layar besar.

Panduan ini menunjukkan cara mengubah iPhone atau iPad Anda jadi media server DLNA/UPnP menggunakan [Everdisk](/products/everdisk), dan cara membuka koleksi itu dari smart TV, konsol game, VLC, Kodi, komputer, ponsel Android, bahkan iPhone kedua. Semuanya berjalan lewat Wi-Fi lokal Anda, jadi tidak ada yang diunggah ke mana pun.

## Yang Anda perlukan

- iPhone atau iPad dengan [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) terpasang.
- TV, pemutar, atau komputer di **jaringan Wi-Fi yang sama** dengan perangkat Anda.
- Foto, video, atau musik yang ingin Anda putar, sudah ada di iPhone Anda (di aplikasi Photos, aplikasi Music, atau folder Dokumen Everdisk).

## Siapkan server DLNA di Everdisk

### Langkah 1: Pilih apa yang mau dibagikan

Buka Everdisk dan masuk ke tab **Berbagi**. Ketuk **Apa yang Dibagikan** lalu pilih konten Anda:

- Aktifkan **Izinkan akses ke seluruh Pustaka Foto** untuk membagikan setiap album, atau ketuk **Tambah Foto** untuk memilih beberapa.
- Aktifkan **Izinkan akses ke seluruh Pustaka Musik** untuk membagikan lagu Anda, atau ketuk **Tambah Lagu** untuk memilih beberapa.
- Tambahkan folder atau file apa pun dengan **Tambah Folder** dan **Tambah Berkas**. Folder Dokumen milik aplikasi dibagikan secara bawaan.

Anda perlu memilih setidaknya satu item sebelum berbagi bisa dimulai.

### Langkah 2: Aktifkan TV & Media Center (DLNA)

Masuk ke **Pengaturan**, lalu **Berbagi**, lalu **Koneksi**. Pastikan **TV & Media Center** aktif. Ini aktif secara bawaan dan membawa tag DLNA. Inilah server yang dicari TV dan pemutar.

### Langkah 3: Mulai berbagi

Kembali ke tab **Berbagi**, ketuk tombol besar **Mulai**. Perangkat Anda kini menjadi media server di Wi-Fi Anda. Perangkat lain melihatnya dengan nama ramahnya, yaitu nama yang ditampilkan sebagai nama perangkat Anda di aplikasi (semacam "Speedy-Hare" sampai Anda menggantinya).

Streaming DLNA selalu terbuka, jadi tidak ada kata sandi yang perlu dimasukkan di TV. Biarkan Everdisk tetap terbuka di layar sewaktu Anda menonton, karena iOS menjeda aplikasi yang didorong sepenuhnya ke latar belakang.

## Putar di smart TV

Ini kasus yang paling umum, dan biasanya cukup sekitar tiga puluh detik.

1. Letakkan TV di **Wi-Fi yang sama** dengan iPhone Anda.
2. Buka pemutar media bawaan TV. Namanya tergantung merek: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** atau **SmartThings** (Samsung), **Content Share**, atau **SimplyShare**.
3. Cari daftar media server atau sumber. Perangkat Anda muncul di sana dengan namanya.
4. Pilih perangkat itu, telusuri ke foto, video, atau musik Anda, lalu tekan putar.

Thumbnail pratinjau muncul secara otomatis, jadi Anda bisa menemukan album liburan atau film yang tepat tanpa menebak-nebak.

### TV mana yang mendukung

Sebagian besar TV dari **Samsung, LG, Sony BRAVIA, Panasonic (firmware VIERA), Philips, dan Hisense** sudah memiliki DLNA bawaan dan langsung berfungsi. **Konsol PlayStation dan Xbox serta sebagian besar AV receiver** juga demikian.

Beberapa platform tidak menyertakannya: **TV Roku, Amazon Fire TV, Vizio SmartCast, dan Google TV polos** tanpa aplikasi media dari pembuatnya. Jika TV Anda salah satunya dan tidak dapat menemukan perangkat Anda, biasanya itulah penyebabnya. Pada TV tersebut, pasang aplikasi pemutar DLNA seperti VLC atau Kodi, atau jangkau file Anda lewat browser web menggunakan [panduan penyiapan WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Beberapa merek tetap menjaga DLNA berfungsi bahkan setelah menghapus logo DLNA resmi, jadi jika tampak hilang, cari salah satu nama pemutar media di atas.

## Putar di VLC atau Kodi di Windows, Mac, dan Linux

VLC dan Kodi gratis, berjalan di setiap sistem desktop, dan berbicara DLNA dengan baik. Keduanya adalah cara andal untuk membuka koleksi Everdisk Anda di komputer.

**VLC (Windows, Mac, Linux):**

1. Buka VLC.
2. Tampilkan daftar putar (di Windows dan Linux tekan **Ctrl+L**, di Mac buka **Playlist** dari menu View).
3. Di bilah samping, buka **Universal Plug'n'Play** di bawah Local Network.
4. Perangkat Anda muncul di daftar. Klik untuk membukanya dan pilih file.

**Kodi (Windows, Mac, Linux):**

1. Masuk ke **Videos**, **Music**, atau **Pictures**, lalu **Files**, lalu **Add source** (atau **Browse**).
2. Pilih **UPnP devices**.
3. Pilih perangkat Anda dan telusuri koleksi Anda.

Di Windows Anda juga bisa membuka **Windows Media Player**, memperluas **Other Libraries** di bilah samping, dan perangkat Anda muncul di sana.

## Putar di Android

Ponsel dan tablet Android tidak punya browser DLNA bawaan sistem, jadi gunakan aplikasi:

- **VLC for Android**: buka menu samping, ketuk **Local Network**, dan perangkat Anda muncul di bawah server UPnP.
- **BubbleUPnP** atau aplikasi UPnP serupa: perangkat Anda muncul di daftar server, dan aplikasi ini juga bisa mengirim pemutaran ke TV.

## Putar di iPhone atau iPad lain

Dua perangkat, satu koleksi. Katakanlah foto ada di iPhone Anda dan Anda ingin menontonnya di iPad Anda.

- Rute paling sederhana adalah tab **Perangkat** milik Everdisk di perangkat kedua. Everdisk berfungsi sebagai klien DLNA sekaligus server. Buka Everdisk di iPad, masuk ke **Perangkat**, dan iPhone Anda muncul di bawah **Perangkat Tersedia**. Ketuk untuk menjelajah dan memutar.
- Aplikasi pemutar DLNA apa pun untuk iOS juga berfungsi, seperti VLC atau browser UPnP. Buka tampilan jaringan lokalnya dan pilih iPhone Anda.

## Putar di konsol game

- **PlayStation 5 dan 4**: buka aplikasi **Media** (Media Gallery), dan perangkat Anda muncul sebagai media server yang bisa Anda jelajahi.
- **Xbox**: gunakan aplikasi pemutar media yang mendukung DLNA, lalu pilih perangkat Anda dari daftar server.

## Jika perangkat Anda tidak muncul di daftar

Beberapa pemutar memungkinkan Anda menambahkan media server berdasarkan alamat alih-alih menunggunya ditemukan. Pada layar **Berbagi** Everdisk, kartu DLNA menampilkan alamat deskripsi perangkat yang berakhiran `/device-desc.xml`. Masukkan alamat itu di kolom tambah server pada pemutar.

Jika masih tidak muncul, periksa tiga hal: kedua perangkat berada di Wi-Fi yang sama (bukan jaringan tamu yang memblokir lalu lintas antarperangkat), Everdisk terbuka dan berbagi sudah dimulai, serta **TV & Media Center** aktif di Pengaturan.

## Jika sebuah video tidak mau diputar

DLNA menyerahkan file ke TV apa adanya, dan TV harus mampu mendekodenya. Jika sebuah klip menolak diputar, formatnya kemungkinan tidak didukung oleh TV tersebut. Dua solusi:

- Buka **Pengaturan**, lalu **Berbagi**, lalu **Video**, dan turunkan **Kualitas**. Everdisk kemudian mengonversi video ke format yang lebih kompatibel saat streaming. (Konversi adalah fitur Premium.)
- Atau buka file yang sama di browser web menggunakan tautan browser Everdisk, yang lebih toleran soal format.

## Cara orang memakainya dalam kehidupan nyata

- **Malam nonton keluarga.** Video yang direkam di ponsel Anda diputar di TV ruang keluarga tanpa kabel atau Apple TV.
- **Foto liburan di layar besar.** Buka pustaka Foto Anda di TV dan geser menyusuri perjalanan bersama semua orang di ruangan.
- **Musik latar di pesta.** Arahkan speaker DLNA atau AV receiver ke pustaka Musik Anda dan biarkan berjalan.
- **Menonton di TV hotel** yang memiliki pemutar media, setelah kedua perangkat berada di Wi-Fi kamar.

## Beberapa tips

- Biarkan Everdisk tetap terbuka saat Anda streaming. Jika Anda mengunci ponsel dalam waktu lama, iOS bisa menjeda aplikasi dan pemutaran berhenti.
- Colokkan ponsel ke sumber daya untuk sesi film yang panjang.
- Untuk streaming tercepat, jaga **Format** dan **Kualitas** pada **Original** di Pengaturan, dan turunkan hanya jika TV tertentu kesulitan dengan sebuah file.
- DLNA hanya untuk streaming. Tidak ada orang di sisi TV yang bisa mengubah atau menghapus file Anda. Untuk transfer file dua arah, gunakan server [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/), atau [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) sebagai gantinya.

## Pertanyaan yang Sering Diajukan

{{% details title="Apa bedanya DLNA dan UPnP?" closed="true" %}}
Keduanya berkaitan erat. UPnP adalah standar jaringan yang mendasarinya, dan DLNA adalah profil media yang dibangun di atasnya yang dipakai TV dan pemutar untuk berbagi dan memutar foto, video, dan musik. Dalam pemakaian sehari-hari kedua kata itu bisa dipertukarkan. Saat Anda mengaktifkan TV & Media Center di Everdisk, perangkat Anda menjadi media server DLNA/UPnP yang bisa dijelajahi klien DLNA mana pun.
{{% /details %}}

{{% details title="Apakah saya perlu memasang apa pun di TV saya?" closed="true" %}}
Tidak. Jika TV Anda mendukung DLNA, TV itu sudah memiliki pemutar media yang bisa menemukan perangkat Anda di Wi-Fi. Anda hanya memasang Everdisk di iPhone atau iPad yang menyimpan kontennya. Jika TV Anda tidak mendukung DLNA, pasang pemutar seperti VLC atau Kodi di perangkat yang terhubung ke TV.
{{% /details %}}

{{% details title="Mengapa iPhone saya tidak muncul di TV?" closed="true" %}}
Periksa bahwa kedua perangkat berada di jaringan Wi-Fi yang sama. Jaringan tamu dan beberapa jaringan kantor atau hotel memblokir perangkat agar tidak saling melihat, yang menghentikan DLNA. Lalu pastikan Everdisk terbuka dengan berbagi sudah dimulai, dan TV & Media Center aktif di Pengaturan, Berbagi, Koneksi. Jika TV masih tidak dapat menemukannya, tambahkan server secara manual menggunakan alamat deskripsi perangkat yang berakhiran /device-desc.xml.
{{% /details %}}

{{% details title="Apakah streaming DLNA memerlukan kata sandi?" closed="true" %}}
Tidak. DLNA selalu terbuka untuk siapa pun di Wi-Fi yang sama selama aktif, itulah sebabnya tidak ada login di sisi TV. Ini baik-baik saja di jaringan rumah yang Anda percayai. Di jaringan yang tidak Anda percayai, matikan TV & Media Center setelah selesai, atau gunakan server SMB dengan enkripsi sebagai gantinya.
{{% /details %}}

{{% details title="Bisakah saya streaming ke Chromecast atau Roku?" closed="true" %}}
Chromecast dan Roku tidak berperan sebagai pemutar DLNA secara bawaan, jadi keduanya tidak akan menemukan perangkat Anda secara langsung. Solusinya adalah memasang aplikasi DLNA yang bisa melakukan cast, seperti VLC atau BubbleUPnP di ponsel, dan mengirim pemutaran ke Chromecast atau Roku dari sana. Pada sebagian besar smart TV lainnya, DLNA berfungsi tanpa semua ini.
{{% /details %}}

{{% details title="Video diputar tanpa suara atau tidak mau terbuka. Apa yang bisa saya lakukan?" closed="true" %}}
Itu adalah format yang tidak dapat didekode oleh TV. Buka Pengaturan, Berbagi, Video di Everdisk dan turunkan Kualitas agar aplikasi mengonversi video ke format yang lebih kompatibel saat streaming. Anda juga bisa membuka file yang sama lewat tautan browser, yang menangani lebih banyak format.
{{% /details %}}

{{% details title="Bisakah saya streaming musik, bukan hanya video?" closed="true" %}}
Ya. Aktifkan Izinkan akses ke seluruh Pustaka Musik, atau tambahkan lagu tertentu, lalu mulai berbagi. Lagu Anda muncul di speaker DLNA, AV receiver, atau TV mana pun, lengkap dengan sampul dan detail lagu. Musik selalu dibagikan dalam kualitas aslinya.
{{% /details %}}

{{% details title="Apakah aplikasi harus tetap terbuka saat saya menonton?" closed="true" %}}
Ya. iPhone Anda berperan sebagai server, dan iOS menjeda aplikasi yang didorong sepenuhnya ke latar belakang dalam waktu lama. Biarkan Everdisk tetap di layar saat Anda streaming, dan colokkan ke sumber daya untuk sesi yang panjang.
{{% /details %}}

{{% details title="Bagaimana cara streaming dari satu iPhone ke iPad lain?" closed="true" %}}
Mulai berbagi di iPhone, lalu buka Everdisk di iPad dan masuk ke tab Perangkat. iPhone muncul di bawah Perangkat Tersedia sebagai media server. Ketuk untuk menjelajah dan memutar. Everdisk berfungsi sebagai klien DLNA sekaligus server, jadi Anda tidak memerlukan aplikasi lain.
{{% /details %}}

{{% details title="Apakah Everdisk gratis?" closed="true" %}}
Ya, Everdisk gratis diunduh dan media server DLNA sudah termasuk. Opsi pembelian sekali bayar Premium Lifetime menambahkan ekstra seperti konversi foto dan video untuk TV lawas, port kustom, dan lainnya. Anda bisa menyiapkan dan memakai streaming DLNA tanpa membayar.
{{% /details %}}

Siap mencobanya? [Unduh Everdisk dari App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) dan streaming album pertama Anda ke TV dalam beberapa menit. Ada pertanyaan atau masukan? Kirim email ke **support@everappz.com**.
</content>
</invoke>
