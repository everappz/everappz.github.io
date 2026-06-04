---
title: "Pengaturan"
date: 2020-02-01
lastmod: 2026-06-01
description: "Jelajahi setiap pengaturan di Evervideo — Pemutar Media (Gambar dalam Gambar, decoding hardware H.264 / HEVC, ekualizer video, penskalaan, rotasi, viewport VR), Audio (ekualizer, sample rate, saluran, IO buffer, mode campuran), Subtitle (primer / sekunder, font, file eksternal, libass), Perpustakaan Media, Pengelola File, Wi-Fi Drive, Widget, Personalisasi, Bahasa, Kode Sandi, Pencadangan & Pemulihan — untuk iPhone, iPad, dan Mac."
keywords: [
  "pengaturan Evervideo", "konfigurasi pemutar video", "upgrade premium Evervideo",
  "pengaturan Gambar dalam Gambar", "pengaturan ekualizer video",
  "mode penskalaan video", "rotasi video", "decoder hardware iPhone",
  "pengaturan subtitle", "subtitle sekunder iOS", "pengaturan libass",
  "file subtitle eksternal", "font subtitle",
  "pengaturan ekualizer audio", "sample rate output audio",
  "saluran output audio", "durasi IO buffer", "mode campuran audio",
  "WiFi Drive video", "widget Evervideo",
  "backup pemulihan Evervideo", "kode sandi Evervideo",
  "bahasa Evervideo", "personalisasi Evervideo"
]
tags: ["panduan", "evervideo", "pengaturan"]
readingTime: 16
---


Layar Pengaturan adalah pusat kendali Evervideo. Dari sini Anda dapat meningkatkan ke Premium, mengonfigurasi mesin video dan audio (codec sistem atau FFmpeg), mengelola Gambar dalam Gambar, menyiapkan subtitle (primer, sekunder, libass, file eksternal, font), mengatur perpustakaan media, menyiapkan pengelola file, mengaktifkan widget Layar Utama, mencadangkan data Anda, dan mengakses bantuan serta informasi hukum. Bagian dikelompokkan di bawah header: Pembelian & Pembaruan, Preferensi aplikasi, Bantuan, Hukum & Privasi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Utama Pengaturan Evervideo" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Tingkatkan ke Premium

Tingkatkan aplikasi ke versi Premium untuk menghapus semua batasan. Versi gratis aplikasi menawarkan pembelian dalam aplikasi seumur hidup satu kali dan dua opsi langganan (1 bulan dan 1 tahun) untuk menghapus semua pembatasan dan meningkatkan ke Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Tingkatkan ke Premium" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

**Berbagi Keluarga** diaktifkan untuk semua pembelian dan paket, sehingga Anda dapat berbagi versi Premium dengan hingga lima anggota keluarga Anda tanpa biaya tambahan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Pilih Paket Premium" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Berbagi Pembelian Antara iOS dan Mac

Pembelian seumur hidup dan langganan dibagikan antara iOS dan Mac menggunakan **iCloud** untuk menyinkronkan informasi ini. Jika Anda memiliki Premium di perangkat iOS, pastikan Anda telah menginstal versi terbaru dan iCloud diaktifkan. Mulai aplikasi di iOS dan tunggu satu menit agar informasi pembelian diunggah ke iCloud, lalu jalankan versi Mac — Premium seharusnya aktif secara otomatis.

Anda juga dapat mengetuk tombol **Pulihkan Pembelian** di pengaturan aplikasi. Pastikan Anda memiliki koneksi internet dan masuk ke akun iCloud dan App Store yang sama di kedua perangkat.

## Pulihkan Pembelian di Perangkat Baru

Untuk memulihkan pembelian Anda di perangkat baru, gunakan menu **Pembelian → Pulihkan Pembelian**. Anda akan melihat daftar pembelian Anda. Jika Anda tidak melihat semuanya, konfirmasikan bahwa perangkat terhubung ke Apple ID yang sama yang digunakan untuk melakukan pembelian, dan pastikan iCloud diaktifkan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Pembelian Evervideo di Pengaturan" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Coba Premium Gratis

Anda dapat meningkatkan ke versi Premium secara gratis, untuk waktu terbatas, menggunakan menu ini. Cukup tonton iklan atau ceritakan kepada teman Anda tentang aplikasi ini.

## Pembaruan Perangkat Lunak

Ketuk **Pembaruan Perangkat Lunak** untuk memeriksa apakah versi Evervideo yang lebih baru tersedia di App Store.

## Yang Baru

Menu ini tersedia setelah versi baru dirilis. Ini menampilkan ringkasan perubahan dan fitur baru dalam pembaruan terbaru.

## Pemutar

Semua yang terkait dengan pemutaran ada di sini — audio, video, subtitle, perangkat, personalisasi, cache, dan timer tidur.

### Umum

Pengaturan ini mencakup aspek mendasar dari pemutar.

- **Mode Ulang** — pilih bagaimana pemutar berperilaku saat video selesai:
  - **Ulangi Semua** — memutar ulang setiap video dalam antrean Anda.
  - **Ulangi Satu** — hanya mengulang video saat ini.
  - **Berhenti Mengulang** — menjeda saat video saat ini berakhir.
  - **Tidak Ada Pengulangan** — memutar antrean sekali tanpa pengulangan.
- **Mode Acak** — mengacak urutan video dalam antrean Anda (**Aktif** atau **Nonaktif**).
- **Simpan Posisi Pemutaran** — menyimpan dan memulihkan posisi pemutaran untuk video di perpustakaan Anda.
- **Simpan Status Pemutar** — mempertahankan status pemutar sebelum Anda menutup aplikasi, sehingga Anda dapat melanjutkan dari tempat Anda berhenti.

### Video

Konfigurasikan cara Evervideo mendekode dan merender video.

- **Dekode Hardware H.264** — aktifkan / nonaktifkan dekoding AVC yang dipercepat hardware. Gunakan saat performa baterai dan termal penting; nonaktifkan untuk kompatibilitas dengan profil eksotis.
- **Dekode Hardware H.265 (HEVC)** — sama untuk HEVC. iPhone, iPad, dan Mac modern mendekode HEVC secara efisien.
- **Format Piksel Pilihan** — pilih format piksel yang disajikan pemutar ke renderer (default disetel untuk perangkat).
- **FPS Pilihan** — tetapkan target FPS pemutaran. Berguna untuk mencocokkan refresh rate monitor tertentu.
- **Mode Penskalaan Video** — Sesuaikan / Isi / Regangkan / Asli. Menentukan bagaimana gambar mengisi area tampilan.
- **Mode Tampilan Video** (iOS / iPadOS) — bagaimana video disajikan dalam tampilan pemutar.
- **Rotasi Video** — putar gambar secara manual 0° / 90° / 180° / 270° (berguna untuk video yang direkam dengan orientasi yang salah).
- **Ekualizer Video** — sesuaikan kecerahan, kontras, saturasi, dan rona dengan pratinjau real-time. Preset kustom dapat **diekspor dan diimpor**.
- **Viewport VR** (iOS / iPadOS) — untuk video sferis 360°. Seret untuk melihat sekeliling, cubit untuk memperbesar.
- **Gambar dalam Gambar (PiP)** (iOS / iPadOS) — aktifkan dukungan PiP; aplikasi akan beralih ke jendela pemutar mengambang saat Anda memindahkan aplikasi ke latar belakang atau mengetuk tombol PiP.

### Audio

Konfigurasikan pemutaran audio dan output.

- **Trek Audio** — pilih aliran audio saat video memiliki beberapa (komentar, dubbing, dll.).
- **Ekualizer Audio** — EQ 10 band dengan preset dan preamplifier. Preset kustom dapat diekspor / diimpor.
- **Sample Rate Output Audio** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Berguna dengan DAC eksternal.
- **Jumlah Saluran Output Audio** — Mono, Stereo, 5.1, ITU BS.775-1, SDDS, dan lainnya.
- **Durasi IO Buffer Output Audio Pilihan** — nilai tipikal untuk pemutaran hi-res latensi rendah adalah sekitar 5 ms (0,005 s). Sesuaikan untuk hardware Anda.
- **Mode Output Audio** (hanya iOS) — mode campuran memungkinkan audio Evervideo menyatu dengan aplikasi lain.

### Subtitle

Evervideo menyertakan dukungan subtitle yang komprehensif.

- **Trek Subtitle** — pilih dari trek subtitle yang tertanam dalam file.
- **File Subtitle Eksternal** — muat file `.srt`, `.vtt`, `.ass`, atau `.ssa` eksternal dari perangkat Anda atau layanan cloud yang terhubung.
- **Font** — pilih font untuk trek subtitle primer.

### Perangkat (Hanya iOS/iPadOS)

Pilih perangkat **AirPlay** atau **Google Chromecast** untuk output video.

### Personalisasi

- **Gaya Tata Letak Pemutar** — Minimal (default untuk Evervideo), Bawah, Antik, Klasik, dan lainnya.
- **Tindakan Layar Utama** — pilih tombol mana yang muncul di layar pemutar utama.
- **Kontrol Layar Kunci** — Waktu Lewati, Tambah Penanda, Tambah ke Favorit.
- **Interval Waktu Lewati** — pilih interval waktu untuk tombol lewati (5 dtk, 10 dtk, 15 dtk, 30 dtk, dll.).
- **Gaya Gulir Sampul Album** — gaya gulir pilihan untuk seni sampul.
- **Elemen Tambahan** — Info Format Audio, Penggeser Volume.

### Pemuatan File

Konfigurasikan cara data video di-streaming dari jaringan.

- **Jenis Jaringan** — hanya Wi-Fi, atau Wi-Fi + Seluler.
- **Waktu Pra-muat** — panjang buffer untuk pemutaran yang lebih lancar di jaringan lambat.
- **Gunakan URL Langsung** — saat didukung, gunakan URL langsung untuk pemuatan lebih cepat.

### Cache Pemutaran

Video dalam antrean pemutar diunduh secara otomatis untuk memastikan pemutaran yang lancar. Anda dapat menonaktifkan opsi ini atau mengonfigurasi ukuran cache di sini.

### Timer Tidur

Aktifkan timer untuk menghentikan pemutaran secara otomatis setelah periode yang ditentukan. Ketuk ikon konfigurasi untuk **mode presisi** dengan granularitas menit per menit.

## Perpustakaan Media

Kelola sinkronisasi otomatis, metadata, sampul album, daftar putar, terbaru, dan favorit.

### Pembacaan Metadata

Saat Anda menambahkan video ke perpustakaan, pembaca metadata memindainya di latar belakang dan mengaturnya berdasarkan Album dan Genre. Anda dapat menyesuaikan kecepatan pemindaian, menonaktifkan pembaca, atau memicu pemindaian ulang penuh dengan **Muat Ulang Metadata**. **Normalisasi Pengkodean Metadata** secara otomatis memperbaiki pengkodean karakter yang rusak (umum dengan file dari PC Windows).

### Sinkronisasi Online

Tambahkan video secara otomatis dari layanan cloud dan server media yang terhubung ke perpustakaan Anda. Pilih folder mana yang akan dipindai, konfigurasikan seberapa sering aplikasi harus disinkronkan, dan mulai / hentikan sinkronisasi secara manual. Sinkronisasi online hanya berjalan saat aplikasi aktif — untuk perpustakaan besar, gunakan versi desktop lalu transfer perpustakaan yang disinkronkan dengan **Cadangan & Pemulihan**.

### Sinkronisasi Offline

Saat Anda menandai folder cloud sebagai tersedia offline, folder tersebut muncul di **File → Folder Offline** dan diunduh secara otomatis. File baru yang ditambahkan secara online juga diunduh. Konfigurasikan interval waktu dan picu sinkronisasi manual dari layar ini.

### Personalisasi

- **Gaya Layar Perpustakaan Media** — Menu Polos, Menu Berkelompok, Menu Tab.
- Alihkan apakah akan menampilkan sampul album besar di layar detail.

### Sampul Album

- **Jenis Jaringan** — Wi-Fi atau Wi-Fi + Seluler.
- **Muat Sampul Album untuk File Online** — ambil karya seni tertanam dari file cloud (menggunakan data ekstra).
- **Cari di Folder** — gunakan gambar JPEG / PNG di folder yang sama saat video tidak memiliki sampul tertanam.
- **Kualitas Sampul** — sesuaikan resolusi penyimpanan sampul dalam cache.
- **Tampilkan di Folder** / **Hapus Semua** — kelola cache karya seni.

### Daftar Putar

Aktifkan penambahan video yang sama ke daftar putar dua kali (nonaktif secara default).

### Terbaru

Kelola daftar video yang baru saja diputar — ubah ukuran, hapus, atau ekspor sebagai M3U / CSV / TXT.

### Favorit

- **Pengeditan Bersamaan** — cerminkan favorit antara perpustakaan media dan bagian file.
- **Hapus Daftar** — bersihkan daftar favorit.
- **Ekspor Daftar Lagu** — ekspor favorit sebagai M3U / CSV / TXT.

### Hapus Perpustakaan Media

Hapus database perpustakaan media. File video dan audio Anda di penyimpanan tidak tersentuh.

## Kode Sandi

Lindungi Evervideo dengan **kode sandi numerik 4 digit**. Saat diaktifkan, Anda akan diminta memasukkan kode sandi setiap kali aplikasi diluncurkan. Gabungkan dengan iOS Face ID / Touch ID di perangkat untuk perlindungan ekstra.

## Pengelola File

Mengontrol cara file ditransfer, disimpan, dan dipratinjau.

- **Transfer File** — preferensi jaringan (hanya Wi-Fi atau Wi-Fi + Seluler).
- **Jumlah Maksimum Tugas Paralel** — atur jumlah thread unduhan paralel.
- **Tugas Transfer File** — lihat unggahan dan unduhan yang sedang aktif.
- **Transfer Latar Belakang** — izinkan unduhan saat aplikasi berada di latar belakang.
- **Simpan File yang Diunduh Ke** — direktori unduhan default.
- **Folder Offline yang Disinkronkan** — kelola folder mode offline.
- **Interval Waktu** — seberapa sering folder offline diperiksa perubahannya.
- **Tampilkan Nama File Lengkap** — tampilkan ekstensi di pengelola file.
- **Edit File Online** — nonaktifkan untuk beralih ke mode baca-saja untuk layanan cloud yang terhubung.
- **Salin File Saat Membuka** — cara menangani file yang diimpor dari aplikasi lain.
- **Thumbnail untuk File** — kelola thumbnail file yang dihasilkan.
- **Hapus File Sementara** — bersihkan folder cache aplikasi.

## Wi-Fi Drive

Aktifkan Wi-Fi Drive untuk mentransfer file dari komputer ke perangkat Anda menggunakan browser web desktop, Finder, atau File Explorer. Instruksi terperinci tersedia [di sini](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Widget

Aktifkan widget agar aplikasi memperbarui data widget selama pemutaran. Pembaruan widget memerlukan energi tambahan, sehingga tombol sakelar nonaktif secara default — aktifkan hanya jika Anda benar-benar menggunakan widget di Layar Utama atau Layar Kunci.

Anda dapat menambahkan widget Evervideo dengan menekan lama Layar Utama atau Layar Kunci, mengetuk **+**, mencari **Evervideo**, dan memilih ukuran widget. Widget menampilkan video yang sedang diputar dan langsung membuka pemutar layar penuh. Widget juga berfungsi di macOS di Pusat Notifikasi.

## Personalisasi

Sesuaikan antarmuka pengguna sesuai preferensi Anda.

- **Ikon Aplikasi** — ikon Layar Utama alternatif (Premium).
- **Skema Warna** — Gelap, Terang, atau Default (mengikuti tampilan sistem Anda).
- **Gaya Latar Belakang** — Sampul Album Buram atau warna solid.
- **Tampilan Item dalam Daftar** — sesuaikan tinggi baris secara otomatis; tampilkan thumbnail yang lebih kecil.
- **Batas Pemuatan Konten** — aktifkan / nonaktifkan paginasi.
- **Gaya Layar File** — Menu Polos atau Menu Berkelompok.
- **Gaya Layar Perpustakaan Media** — Menu Polos / Berkelompok / Tab.
- **Gaya Layar Pemutar** — Minimal / Bawah / Antik / Klasik.
- **Gaya Menu Konteks** — menu sistem atau gaya panel bawah.

## Jendela

Tersedia di Mac dan Catalyst. Konfigurasikan preferensi terkait jendela seperti ukuran default dan perilaku saat diluncurkan.

## Layar

Pilih apakah layar harus tetap aktif saat Anda menggunakan aplikasi.

## Aksesibilitas

Aktifkan **Mode Teks** untuk menyembunyikan gambar di antarmuka pengguna. Mode Teks diaktifkan secara otomatis saat VoiceOver aktif.

## Bahasa

Ubah bahasa aplikasi dan ganti default sistem. Perubahan berlaku setelah Anda sepenuhnya menutup dan membuka kembali Evervideo. Lebih dari 120 bahasa didukung.

## Cadangan & Pemulihan

Cadangkan semua data aplikasi Anda atau migrasikan ke perangkat lain. Pilih apa yang akan disertakan:

- **Database** — entri perpustakaan media, daftar putar, peringkat, favorit, riwayat tontonan. File offline tidak disertakan agar ukuran file tetap terkelola.
- **Sampul Album** — karya seni yang di-cache.
- **Pengaturan** — pengaturan aplikasi Anda.

Ketuk **Cadangkan Data Aplikasi** untuk memulai pencadangan. Untuk memulihkan di perangkat baru, pindahkan file cadangan melalui iCloud Drive, AirDrop, atau layanan cloud yang terhubung dan buka di perangkat baru.

## Bantuan

Akses panduan aplikasi untuk bantuan dan panduan dalam menggunakan aplikasi secara efektif.

## Pertanyaan yang Sering Diajukan

Temukan jawaban atas pertanyaan umum di bagian FAQ.

## Kirim Umpan Balik

Kirimkan umpan balik Anda ke tim dukungan kami langsung dari aplikasi, dengan informasi diagnostik yang dilampirkan secara otomatis.

## Bagikan Aplikasi Ini

Bagikan Evervideo dengan teman-teman Anda untuk menyebarkan informasinya.

## Temukan Lebih Banyak Aplikasi

Jelajahi aplikasi lain dari Everappz.

## Syarat dan Ketentuan

Baca syarat dan ketentuan sebelum menggunakan aplikasi.

## Kebijakan Privasi

Baca kebijakan privasi untuk memahami praktik penanganan data kami.

## Analitik dan Pengumpulan Data

Periksa layanan mana yang diaktifkan untuk analitik dan pengumpulan data dan nonaktifkan yang tidak Anda inginkan.

## Pemberitahuan Hukum

Informasi tentang setiap perpustakaan yang digunakan dalam aplikasi beserta nomor versi aplikasi dan informasi build.
