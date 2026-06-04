---
title: "Pengaturan"
date: 2020-02-01
description: "Jelajahi setiap pengaturan di Flacbox — dari preferensi pemutaran, mesin audio FFmpeg / sistem, output audio Hi-Res, penyesuaian equalizer, koreksi pitch, durasi IO buffer, sinkronisasi metadata, kontrol playlist, transfer file, widget Layar Beranda, Apple CarPlay, personalisasi UI, bahasa, kode sandi, cadangan & pemulihan, dan peningkatan Premium."
keywords: [
  "pengaturan Flacbox", "konfigurasi pemutar audio", "peningkatan premium Flacbox",
  "WiFi Drive", "sinkronisasi metadata", "equalizer", "kecepatan pemutaran",
  "duplikat playlist", "pengaturan manajer file", "sinkronisasi musik offline",
  "editor tag audio", "mode gelap", "pulihkan pembelian", "pengaturan cadangan",
  "pengaturan widget Flacbox", "pengaturan CarPlay Flacbox",
  "pengaturan FFmpeg Flacbox", "pengaturan sample rate Flacbox",
  "pengaturan koreksi pitch Flacbox", "IO buffer Flacbox",
  "kode sandi Flacbox", "bahasa Flacbox", "personalisasi Flacbox",
  "analitik Flacbox"
]
tags: ["panduan", "flacbox", "pengaturan"]
readingTime: 16
---


Layar Pengaturan adalah pusat kendali Flacbox. Dari sini Anda dapat meningkatkan ke Premium, mengonfigurasi mesin audio (codec sistem atau FFmpeg), mengelola perpustakaan musik, menyiapkan manajer file, menyesuaikan editor tag audio, mengaktifkan widget Layar Beranda dan Apple CarPlay, mencadangkan data Anda, dan mengakses bantuan serta informasi hukum.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Utama Pengaturan Flacbox" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Tingkatkan ke Premium

Tingkatkan aplikasi ke versi Premium untuk menghapus semua batasan. Versi gratis aplikasi menawarkan pembelian dalam aplikasi seumur hidup satu kali dan dua opsi berlangganan (1 bulan dan 1 tahun) untuk menghapus semua batasan dan meningkatkan ke Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Tingkatkan ke Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Berbagi Keluarga** diaktifkan untuk semua pembelian dan paket, sehingga Anda dapat berbagi versi Premium dengan hingga lima anggota keluarga tanpa biaya tambahan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Pilih Paket Premium" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Anda dapat membaca lebih lanjut tentang pembelian dan versi Premium di sini: [Apa perbedaan antara Flacbox dan Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Berbagi Pembelian antara iOS dan Mac

Pembelian seumur hidup dan langganan dibagikan antara iOS dan Mac, menggunakan iCloud untuk menyinkronkan informasi ini. Jika Anda memiliki versi Premium di perangkat iOS, pastikan Anda telah menginstal versi terbaru dan iCloud diaktifkan. Mulai aplikasi di iOS dan tunggu satu menit agar informasi pembelian Anda diunggah ke iCloud.

Anda juga dapat mencoba mengetuk tombol Pulihkan Pembelian di pengaturan aplikasi. Setelah itu, instal versi aplikasi terbaru dari App Store di Mac Anda dan mulai aplikasi.

## Pulihkan Pembelian di Perangkat Baru

Untuk memulihkan pembelian Anda di perangkat baru, gunakan menu Pembelian → Pulihkan Pembelian. Anda akan melihat daftar pembelian Anda. Jika Anda tidak melihat semuanya, konfirmasi perangkat terhubung ke Apple ID yang sama yang digunakan untuk melakukan pembelian, dan pastikan iCloud diaktifkan.

## Coba Premium Gratis

Anda dapat meningkatkan ke versi Premium secara gratis, untuk waktu terbatas, menggunakan menu ini.

## Pembelian

Anda dapat memulihkan pembelian sebelumnya dari menu ini. Jika Anda mengalami kesalahan aktivasi, coba aktifkan opsi Pulihkan Pembelian saat Peluncuran Aplikasi.

## Pembaruan Perangkat Lunak

Ketuk Pembaruan Perangkat Lunak untuk memeriksa apakah versi Flacbox yang lebih baru tersedia.

## Yang Baru

Menu ini tersedia setelah versi baru dirilis. Ini menampilkan ringkasan perubahan dan fitur baru dalam pembaruan terbaru.

## Pemutar Audio

Bagian ini mengonfigurasi pemutar audio dan mesin audio yang mendasarinya, termasuk pilihan FFmpeg / codec sistem dan opsi output audio Hi-Res.

### Umum

- **Mode Ulangi** — pilih bagaimana pemutar audio berperilaku ketika trek selesai:
  - **Ulangi Semua** — memutar ulang semua trek dalam antrean Anda.
  - **Ulangi Satu** — hanya mengulangi trek saat ini.
  - **Hentikan Ulangi** — menjeda pemutaran ketika trek saat ini berakhir.
  - **Tanpa Ulangi** — membiarkan antrean Anda diputar tanpa mengulangi.
- **Mode Acak** — mengacak urutan trek dalam antrean Anda. Dapat diatur **Acak Mati** atau **Acak Nyala**.
- **Codec Audio** — pilih mesin audio yang digunakan untuk pemutaran:
  - **System Codec + FFmpeg** — memprioritaskan codec audio sistem di mana memungkinkan, meningkatkan kompatibilitas dan stabilitas.
  - **FFmpeg** — memaksa codec FFmpeg untuk semua file audio, membuka koreksi pitch dan sample rate output audio.
- **Sample Rate Output Audio** — sesuaikan sample rate output audio untuk mengoptimalkan kualitas suara, sangat berguna dengan DAC eksternal. Nilai yang tersedia: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz,** dan **96 kHz**.
- **Jumlah Saluran Output Audio** — untuk sistem audio multisaluran dengan DAC eksternal, tentukan jumlah saluran: Mono, Stereo, Center / Left / Right, dll.
- **Durasi IO Buffer Output Audio yang Disukai** — konfigurasikan durasi buffer. Nilai tipikal untuk meminimalkan latensi adalah sekitar **5 milidetik (0,005 detik)**.
- **Mode Output Audio (hanya iOS)** — konfigurasikan mode output audio campuran. Instruksi terperinci [di sini](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Simpan Posisi Pemutaran** — menyimpan dan memulihkan posisi pemutaran.
- **Simpan Status Pemutar Audio** — mempertahankan status pemutar audio sebelum Anda menutup aplikasi.

### Personalisasi

- **Gaya Layar Pemutar Audio** — konfigurasikan pemosisian elemen.
- **Gaya Gulir Sampul Album** — konfigurasikan gaya gulir yang disukai.
- **Elemen Tambahan** — aktifkan elemen ekstra pada layar pemutar audio.
- **Aksi Layar Utama** — konfigurasikan tombol mana yang harus terlihat secara default.
- **Kontrol Pemutaran di Layar Kunci** — pilih kontrol mana yang muncul di layar kunci.
- **Tombol Lewati Waktu** — pilih interval waktu untuk tombol Lewati Waktu.

### Pemuatan File

- **Waktu Pramuat** — atur interval waktu buffering. Tingkatkan ini jika koneksi jaringan Anda buruk.
- **Gunakan URL Langsung** — jika diaktifkan, URL langsung digunakan untuk memuat lagu jika server mendukungnya.

### Equalizer Audio

Konfigurasikan equalizer audio 10-band. Baca lebih lanjut [di sini](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Kecepatan Pemutaran

Sesuaikan kecepatan pemutaran pemutar audio dari **0,02× hingga 3,00×**.

### Koreksi Pitch

Ubah pengaturan koreksi pitch menggunakan nilai yang telah ditentukan. Tersedia dalam jalur codec FFmpeg, dengan rentang dari **-1000 hingga +1000**.

### Cache Pemutaran

Lagu dalam antrean pemutar audio diunduh secara otomatis untuk memastikan pemutaran yang lancar. Anda juga dapat mengonfigurasi ukuran cache pemutar audio di sini.

### Timer Tidur

Aktifkan timer untuk secara otomatis menghentikan pemutaran setelah periode tertentu.

## Perpustakaan

Pengaturan perpustakaan musik Anda — sinkronisasi otomatis, pembacaan metadata, pemuatan sampul album, playlist, terkini, dan favorit — ada di sini.

### Pembacaan Metadata

Saat Anda menambahkan trek ke perpustakaan, **pembaca metadata** mulai bekerja. Proses latar belakang ini membaca semua metadata dari trek Anda dan mengaturnya berdasarkan Artis, Album, Genre, dan Komposer. Anda dapat menonaktifkan pembaca metadata dan menampilkan nama file sebagai gantinya.

**Normalisasi Pengkodean Metadata** secara otomatis menormalkan pengkodean metadata untuk semua lagu.

### Sinkronisasi Online

Sinkronisasi musik online otomatis menambahkan trek dari layanan cloud yang terhubung ke perpustakaan musik secara otomatis. Untuk mengaktifkannya, buka pengaturan perpustakaan musik dan pilih folder sinkronisasi.

### Sinkronisasi Offline

Konfigurasikan sinkronisasi musik offline. Jika Anda menandai folder online sebagai tersedia offline, folder tersebut muncul di sini. Konten diunduh ke **File Lokal → Folder Offline**.

### Personalisasi

Konfigurasikan gaya layar perpustakaan musik. Tiga opsi tersedia: **Menu Biasa, Menu Berkelompok, Menu Bertab**.

### Sampul Album

- **Jenis Jaringan** — pilih Wi-Fi atau Wi-Fi & Data Seluler.
- **Muat Sampul Album untuk File Online** — muat sampul album yang disematkan untuk file di penyimpanan cloud.
- **Cari di Folder** — jika trek tidak memiliki sampul yang disematkan, cari gambar JPEG atau PNG di folder yang sama.
- **Kualitas Sampul** — pilih kualitas sampul album.
- **Tampilkan di Folder** — buka folder tempat sampul album di-cache.
- **Hapus Semua** — hapus sampul album yang di-cache.

### Playlist

Aktifkan opsi untuk menambahkan lagu yang sama ke playlist dua kali.

### Terkini

- **Hapus Daftar** — hapus seluruh daftar lagu yang baru diputar.
- **Ubah Ukuran Daftar** — atur jumlah item yang muncul dalam daftar.
- **Ekspor Daftar Lagu** — ekspor daftar lagu yang baru diputar.

### Favorit

- **Pengeditan Simultan** — saat diaktifkan, menambahkan lagu ke favorit menambahkannya baik di perpustakaan musik maupun bagian file secara bersamaan.
- **Hapus Daftar** — hapus seluruh daftar lagu favorit.
- **Ekspor Daftar Lagu** — ekspor favorit.

### Hapus Perpustakaan Musik

Hapus database perpustakaan musik. File musik Anda di penyimpanan tidak tersentuh.

## Kode Sandi

Aktifkan layar kode sandi untuk melindungi data aplikasi Anda dengan kode sandi numerik 4 digit.

## Manajer File

Bagian Manajer File mengontrol cara file ditransfer, disimpan, dan dipratinjau.

### Transfer File

Pilih preferensi jaringan untuk mengunduh file ke perangkat Anda.

### Jumlah Maksimum Tugas Paralel

Atur jumlah thread unduhan paralel.

### Tugas Transfer File

Menampilkan tugas unggah dan unduhan yang sedang aktif.

### Transfer Latar Belakang

Izinkan unduhan saat aplikasi berada di latar belakang.

### Simpan File yang Diunduh Ke

Pilih direktori unduhan default.

### Folder Offline yang Disinkronkan

Kelola sinkronisasi offline untuk folder yang dipilih. Baca lebih lanjut tentang mode offline [di sini](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Interval Waktu

Pilih seberapa sering folder offline disinkronkan.

### Tampilkan Nama File Lengkap

Tampilkan nama file lengkap, termasuk ekstensi.

### Edit File Online

Nonaktifkan pengeditan file online untuk beralih ke mode hanya-baca.

### Salin File Saat Membuka

Tentukan cara aplikasi menangani file yang diimpor dari aplikasi lain.

### Thumbnail untuk File

Kelola dan hapus thumbnail file yang dihasilkan.

### Hapus File Sementara

Bersihkan folder cache aplikasi.

## Editor Tag Audio

Konfigurasikan editor tag audio bawaan.

### Penskalaan Sampul Album

Pilih metode penskalaan yang digunakan saat sampul album disimpan ke dalam tag audio.

### Perbarui File Online

Saat diaktifkan, aplikasi secara otomatis memperbarui metadata file di server cloud setelah selesai mengedit.

### Hapus File Setelah Mengedit Online

Pilih apakah aplikasi harus menghapus salinan yang diunduh setelah menyelesaikan pengeditan file online.

### Tombol Layar Utama

Pilih tombol mana yang terlihat di layar utama editor tag audio.

## Widget

Aktifkan widget agar aplikasi memperbarui data widget selama pemutaran. Pembaruan widget memerlukan energi tambahan, sehingga tombol ini mati secara default.

## CarPlay

Ubah pengaturan CarPlay di sini.

### Urutkan

Konfigurasikan opsi pengurutan untuk semua layar CarPlay.

### Batas Pemuatan Konten

Pilih apakah aplikasi menggunakan pagination pada layar CarPlay.

### Warna Gradien Ikon Menu

Pilih skema warna untuk layar beranda CarPlay.

### Tampilkan Gambar

Nonaktifkan gambar pada layar CarPlay untuk mengoptimalkan kecepatan pemuatan.

### Jeda Pemutaran Saat Terhubung

Aktifkan ini untuk menghindari audio keras tiba-tiba saat Anda menghubungkan perangkat ke CarPlay.

## Wi-Fi Drive

Aktifkan **Wi-Fi Drive** untuk mentransfer file dari komputer ke perangkat Anda menggunakan browser web desktop, Finder, atau File Explorer. Instruksi terperinci tersedia [di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalisasi

Sesuaikan antarmuka pengguna sesuai preferensi Anda.

### Ikon Aplikasi

Pilih ikon aplikasi alternatif untuk Layar Beranda Anda (Premium).

### Skema Warna

Pilih tema antarmuka pengguna dan aktifkan mode gelap.

### Gaya Latar Belakang

Modifikasi gaya latar belakang aplikasi. Saat ini satu-satunya opsi adalah **Sampul Album Buram**.

### Tampilan Item dalam Daftar

Sesuaikan cara item ditampilkan dalam daftar.

### Batas Pemuatan Konten

Secara default aplikasi menggunakan pagination untuk mempercepat pemuatan konten.

### Gaya Layar File Lokal

Ubah gaya presentasi bagian **File Lokal**.

### Gaya Layar Perpustakaan Musik

Sesuaikan tampilan layar **Perpustakaan Musik**.

### Gaya Layar Pemutar Audio

Konfigurasikan tampilan layar **Pemutar Audio**.

### Gaya Menu Konteks

Pilih gaya menu konteks yang ditampilkan saat Anda mengetuk tombol **Aksi Lainnya**.

## Jendela

Tersedia di Mac. Konfigurasikan preferensi terkait jendela.

## Layar

Pilih apakah layar harus tetap aktif saat Anda menggunakan aplikasi.

## Aksesibilitas

Aktifkan **Mode Teks** untuk menyembunyikan semua gambar di antarmuka pengguna. Mode Teks diaktifkan secara otomatis saat VoiceOver aktif.

## Bahasa

Ubah bahasa aplikasi dan timpa default sistem. Perubahan berlaku setelah Anda sepenuhnya keluar dan membuka kembali Flacbox.

## Cadangan & Pemulihan

Gunakan fitur ini untuk mencadangkan semua data aplikasi Anda atau memigrasikannya ke perangkat lain. Anda dapat memilih apa yang akan disertakan:

- **Database** — semua trek di perpustakaan musik Anda, termasuk playlist.
- **Sampul Album** — semua sampul album yang di-cache.
- **Pengaturan** — semua pengaturan aplikasi Anda.

Ketuk **Cadangkan Data Aplikasi** untuk memulai pencadangan.

Instruksi langkah demi langkah terperinci: [Cara Mentransfer Perpustakaan Musik Anda Antar Perangkat](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Bantuan

Akses panduan aplikasi untuk mendapatkan bantuan dan panduan.

## Pertanyaan yang Sering Diajukan

Temukan jawaban atas pertanyaan umum di bagian FAQ.

## Kirim Umpan Balik

Punya umpan balik atau butuh bantuan? Kirim umpan balik Anda ke tim dukungan kami langsung dari aplikasi.

## Bagikan Aplikasi Ini

Bagikan aplikasi dengan teman-teman Anda.

## Temukan Aplikasi Lainnya

Jelajahi aplikasi lain dari Everappz.

## Syarat dan Ketentuan

Menguraikan syarat dan ketentuan penggunaan aplikasi.

## Kebijakan Privasi

Kunjungi halaman kebijakan privasi untuk memahami praktik penanganan data kami.

## Analitik dan Pengumpulan Data

Periksa layanan mana yang diaktifkan untuk analitik dan pengumpulan data dan nonaktifkan yang tidak Anda inginkan.

## Pemberitahuan Hukum

Berisi informasi tentang setiap perpustakaan yang digunakan dalam aplikasi beserta nomor versi aplikasi dan informasi build.
