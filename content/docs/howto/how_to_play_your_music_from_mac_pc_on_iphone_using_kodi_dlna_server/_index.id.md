---
title: "Cara memutar musik dari Mac / PC / Linux / NAS di iPhone menggunakan server Kodi DLNA"
date: 2025-07-25
description: "Streaming musik dari komputer atau NAS ke iPhone melalui Wi-Fi menggunakan Kodi DLNA dan aplikasi Evermusic."
keywords: ["server kodi dlna", "streaming musik ke iphone", "memutar musik dari nas", "evermusic dlna", "musik mac ke iphone", "musik windows ke iphone", "kodi dlna iphone", "streaming audio dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "streaming musik", "mac", "nas", "linux", "jaringan lokal"]
readingTime: 5
---

{{< author-byline >}}


**Ringkasan:** Instal Kodi di Mac, PC, Linux, atau NAS Anda, aktifkan server DLNA/UPnP, dan streaming seluruh perpustakaan musik Anda ke iPhone atau iPad menggunakan aplikasi gratis Evermusic atau Flacbox melalui Wi-Fi. Tidak perlu langganan.

## Pendahuluan

Jika Anda memiliki **Mac, PC Windows, mesin Linux, atau perangkat NAS**, Anda dapat dengan mudah mengubahnya menjadi **server musik pribadi** di rumah menggunakan [Kodi](https://kodi.tv/), platform media gratis dan open-source. Dengan server **DLNA/UPnP** bawaan Kodi, Anda dapat streaming seluruh perpustakaan musik ke klien yang kompatibel dengan DLNA — termasuk iPhone atau iPad Anda.

Dalam panduan ini, kami akan menunjukkan langkah demi langkah cara:

- Menginstal Kodi di Mac atau PC  
- Mengatur folder musik untuk berbagi  
- Mengaktifkan server musik DLNA  
- Mengakses musik tersebut menggunakan aplikasi **Evermusic** atau **Flacbox** untuk iOS

Pengaturan ini 100% gratis — tanpa langganan, hanya musik Anda sendiri yang di-streaming melalui jaringan Wi-Fi. Baik Anda mencoba mengatur koleksi MP3 yang besar, mendengarkan FLAC melalui Wi-Fi, atau sekadar menikmati musik lokal tanpa sinkronisasi melalui iTunes, pengaturan ini sempurna untuk Anda.

## Unduh dan Instal Kodi di Mac / PC / Linux / NAS

Pertama, kunjungi situs web resmi Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Halaman utama Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Klik **Unduh** dan gulir untuk menemukan versi untuk komputer Anda. Pilih sistem operasi Anda. Dalam contoh ini, kami akan menggunakan **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Halaman unduhan Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Klik **Intel (x86/64)** jika Anda memiliki Mac Intel atau **Apple Silicon** untuk M1, M2, M3 Mac untuk memulai unduhan.

{{< cards cols="1">}}
{{< card subtitle="Pilih installer macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Harap tunggu sebentar sementara installer diunduh.

{{< cards cols="1">}}
{{< card subtitle="Kodi terunduh" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Setelah diunduh, temukan file `.dmg` di folder **Unduhan** Anda.

{{< cards cols="1">}}
{{< card subtitle="Instal Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Klik dua kali file yang diunduh untuk meluncurkan installer. Seret Kodi ke folder **Aplikasi** untuk menginstal.

{{< cards cols="1">}}
{{< card title="" subtitle="Instal Kodi dengan menyeretnya ke Aplikasi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Luncurkan Kodi. Anda mungkin perlu mengizinkannya di **Preferensi Sistem → Keamanan & Privasi → Buka Tetap**.

{{< cards cols="1">}}
{{< card subtitle="Layar utama Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Tambahkan Musik ke Perpustakaan Kodi

Klik **ikon roda gigi** (Pengaturan) dari layar beranda.

{{< cards cols="1">}}
{{< card subtitle="Pengaturan Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Navigasi ke **Pengaturan Media → Perpustakaan**. Aktifkan **Perbarui perpustakaan saat startup** untuk perpustakaan video dan musik untuk pengindeksan otomatis.

{{< cards cols="1">}}
{{< card subtitle="Pengaturan perpustakaan" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Lalu pergi ke bagian **Musik** dan klik **Tambah Musik**.

{{< cards cols="1">}}
{{< card subtitle="Tambah folder musik" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Jelajahi dan pilih folder tempat musik Anda disimpan.

{{< cards cols="1">}}
{{< card subtitle="Pilih sumber musik" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Tambahkan sumber musik ke Kodi.

{{< cards cols="1">}}
{{< card subtitle="Tambah sumber musik" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Konfirmasi dan biarkan Kodi memindai perpustakaan musik Anda.

{{< cards cols="1">}}
{{< card subtitle="Konfirmasi sumber musik" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Tunggu sebentar sementara perpustakaan Anda dipindai dan dibangun sepenuhnya.

{{< cards cols="1">}}
{{< card subtitle="Memindai perpustakaan musik" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Aktifkan Server DLNA Kodi

Pergi ke **Pengaturan → Layanan → UPnP/DLNA**.

Aktifkan opsi: **Bagikan perpustakaan saya**.

Kodi sekarang bertindak sebagai server DLNA di jaringan Wi-Fi lokal Anda.

{{< cards cols="1">}}
{{< card subtitle="Aktifkan DLNA di Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Buka Perpustakaan Kodi

Klik kanan untuk menutup jendela pengaturan dan membuka perpustakaan utama Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Klik kanan untuk mengakses perpustakaan Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Unduh Aplikasi Streaming Musik untuk iOS

Dapatkan aplikasi klien DLNA gratis untuk iOS yang memungkinkan Anda streaming musik dari berbagai layanan penyimpanan cloud dan server DLNA.

- Gunakan **Evermusic** jika koleksi Anda sebagian besar MP3 dan format audio standar lainnya.
- Pilih **Flacbox** jika Anda memiliki perpustakaan musik hi-res dalam format seperti FLAC, ALAC, atau DSD.

Kedua aplikasi tersedia untuk **iOS** dan **macOS**, dan gratis untuk digunakan.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Unduh Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Unduh Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Tambahkan Sumber DLNA

Setelah mengunduh aplikasi iOS, buka bagian **Semua Koneksi**.

{{< cards cols="1">}}
{{< card title="" subtitle="Sidebar utama aplikasi Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Gulir ke bawah dan ketuk **Jaringan Lokal - Perangkat yang Tersedia** untuk menemukan server DLNA. Di bagian ini, Anda akan melihat semua perangkat yang tersedia di jaringan lokal Anda. **Server Kodi DLNA** Anda seharusnya muncul di sini. Ketuk server Kodi untuk terhubung.

{{< cards cols="1">}}
{{< card title="" subtitle="Perangkat DLNA tersedia di Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic akan menampilkan folder perpustakaan yang dibagikan melalui Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Perpustakaan musik Kodi di Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navigasi ke folder **Lagu** untuk melihat semua file audio yang tersedia di server DLNA Anda.

{{< cards cols="1">}}
{{< card title="" subtitle="Lagu yang terdaftar dari folder jarak jauh" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Ketuk file audio apa pun untuk mulai streaming secara instan.

{{< cards cols="1">}}
{{< card title="" subtitle="File MP3 diputar di Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Kembali ke bagian **Koneksi**. Server DLNA yang ditambahkan sekarang akan muncul di sini. Ketuk ikonnya untuk terhubung kembali kapan saja. Anda juga dapat menghubungkan layanan cloud lainnya dari layar ini menggunakan langkah yang sama.

Anda juga dapat mengaktifkan **scrobbling Last.fm** di sini. Statistik pemutaran akan disimpan ke akun Last.fm Anda, memberikan rekomendasi musik yang dipersonalisasi nanti.

{{< cards cols="1">}}
{{< card title="" subtitle="Koneksi di Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Bangun Perpustakaan Musik

Baik **Evermusic** maupun **Flacbox** memungkinkan Anda menambahkan musik ke perpustakaan dan mengaturnya berdasarkan **tag metadata** seperti artis, album, genre, dan komposer.

Untuk memulai, buka bagian **Perpustakaan Musik**. Gulir ke bawah ke **Alat dan Preferensi** dan ketuk **Tambah Musik**.

{{< cards cols="1">}}
{{< card title="" subtitle="Perpustakaan musik Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Pilih sumber musik — dalam hal ini, pilih **Koneksi**.

{{< cards cols="1">}}
{{< card title="" subtitle="Tambah musik baru di Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Temukan **server Kodi DLNA** di Koneksi dan ketuk untuk melihat folder dan file.

{{< cards cols="1">}}
{{< card title="" subtitle="Pilih server DLNA untuk mengimpor musik" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Pilih folder atau file yang ingin Anda tambahkan dan ketuk **Selesai**.

{{< cards cols="1">}}
{{< card title="" subtitle="Pilih folder musik untuk ditambahkan" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Aplikasi akan memindai file yang dipilih dan mengaturnya menggunakan metadata ke dalam bagian seperti Artis, Album, Genre, dan Komposer.

{{< cards cols="1">}}
{{< card title="" subtitle="Perpustakaan musik dengan kategori" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Buat Daftar Putar

Anda juga dapat membuat daftar putar sendiri.

Pertama, buka tab **Daftar Putar**.

{{< cards cols="1">}}
{{< card title="" subtitle="Tab Daftar Putar di Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Ketuk tombol **plus (+)** dan pilih **Daftar Putar Baru**.

{{< cards cols="1">}}
{{< card title="" subtitle="Buat daftar putar baru" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Masukkan nama untuk daftar putar Anda dan ketuk **Simpan**.

{{< cards cols="1">}}
{{< card title="" subtitle="Masukkan nama daftar putar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Selanjutnya, pilih sumber untuk menambahkan lagu — di sini, kami memilih **Perpustakaan**.

{{< cards cols="1">}}
{{< card title="" subtitle="Tambahkan lagu ke daftar putar baru" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Pilih lagu yang Anda inginkan dan ketuk **Selesai** untuk menambahkannya.

{{< cards cols="1">}}
{{< card title="" subtitle="Tambah musik dari perpustakaan ke daftar putar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Trek yang dipilih sekarang akan muncul di daftar putar yang dibuat.

{{< cards cols="1">}}
{{< card title="" subtitle="Daftar putar yang dibuat ditampilkan dalam daftar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Secara default, lagu tersedia untuk streaming. Untuk mendengarkan offline, aktifkan **Mode Offline** — aplikasi akan mengunduh semua trek daftar putar.

{{< cards cols="1">}}
{{< card title="" subtitle="Mode offline diaktifkan untuk daftar putar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Ketuk tombol **Lebih banyak tindakan** untuk menjelajahi opsi tambahan. Anda dapat:

- Mengarsipkan daftar putar  
- Mengubah sampul album  
- Mengurutkan ulang trek  
- Dan fitur berguna lainnya

{{< cards cols="1">}}
{{< card title="" subtitle="Lebih banyak tindakan daftar putar tersedia" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Kesimpulan

Dengan **Evermusic** dan **Flacbox**, mengubah iPhone, iPad, atau Mac Anda menjadi pemutar musik DLNA yang kuat itu mudah. Baik Anda menyimpan musik di cloud, di NAS, atau di server media rumah seperti **Kodi**, aplikasi ini memungkinkan Anda streaming, mengatur, dan menikmati koleksi Anda tanpa batas.

- Streaming MP3 atau FLAC hi-res langsung dari **server Kodi DLNA** Anda  
- Bangun perpustakaan musik pribadi yang dikelompokkan berdasarkan metadata (album, genre, komposer)  
- Buat dan kelola **daftar putar kustom**  
- Aktifkan **mode offline** untuk mendengarkan saat bepergian  
- Hubungkan ke **beberapa layanan cloud** dan **perangkat jaringan lokal**  
- Lacak kebiasaan mendengarkan Anda dengan **integrasi Last.fm**

Baik Anda seorang audiofil atau pendengar kasual, Evermusic dan Flacbox menawarkan semua yang Anda butuhkan untuk streaming dan pengaturan musik yang mulus.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Unduh Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Unduh Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Mulai bangun pengalaman musik pribadi Anda hari ini.

## FAQ

{{% details title="Apakah Kodi gratis untuk digunakan sebagai server DLNA?" closed="true" %}}
Ya. Kodi sepenuhnya gratis dan open-source. Berjalan di macOS, Windows, Linux, dan banyak perangkat NAS.
{{% /details %}}

{{% details title="Apakah Evermusic dan Flacbox mendukung streaming FLAC melalui DLNA?" closed="true" %}}
Ya. Flacbox dioptimalkan untuk format hi-res seperti FLAC, ALAC, dan DSD. Evermusic juga mendukung pemutaran FLAC bersama MP3 dan format standar lainnya.
{{% /details %}}

{{% details title="Bisakah saya mendengarkan offline setelah streaming dari Kodi?" closed="true" %}}
Ya. Aktifkan Mode Offline pada daftar putar apa pun, dan aplikasi akan mengunduh semua trek ke perangkat Anda untuk mendengarkan tanpa koneksi jaringan.
{{% /details %}}

{{% details title="Apakah saya memerlukan langganan premium untuk menggunakan DLNA?" closed="true" %}}
Versi gratis mendukung hingga 3 koneksi cloud atau jaringan. Premium menghapus batasan ini dan memungkinkan Anda menghubungkan layanan dan server DLNA tak terbatas.
{{% /details %}}

{{% details title="Apakah iPhone saya harus berada di jaringan Wi-Fi yang sama dengan Kodi?" closed="true" %}}
Ya. Streaming DLNA bekerja melalui jaringan lokal Anda. Baik server Kodi maupun perangkat iOS Anda harus terhubung ke jaringan Wi-Fi yang sama.
{{% /details %}}

{{% details title="Bisakah saya menggunakan pengaturan ini dengan NAS alih-alih Mac atau PC?" closed="true" %}}
Ya. Banyak perangkat NAS (Synology, QNAP, dll.) mendukung Kodi atau memiliki server DLNA bawaan sendiri. Evermusic dan Flacbox dapat terhubung ke server DLNA/UPnP standar apa pun.
{{% /details %}}
