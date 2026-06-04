---
title: "Editor Tag"
date: 2020-02-01
description: "Pelajari cara menggunakan Editor Tag Evertag untuk memperbarui metadata musik, mengedit sampul album, mengedit beberapa file secara batch, dan mengelola tag dari MusicBrainz. Ideal untuk mengorganisir perpustakaan musik Anda di iOS dan Mac."
keywords: [
  "editor tag Evertag", "editor metadata audio", "editor tag musik",
  "edit tag audio iPhone", "editor sampul album", "edit tag audio batch",
  "metadata MusicBrainz", "aplikasi pengatur musik", "panduan Evertag", "editor tag ID3"
]
tags: ["panduan", "evertag", "editor tag"]
readingTime: 5
---


**Editor Tag** adalah layar utama aplikasi Evertag di mana Anda dapat melihat dan mengedit metadata file audio. Buka layar ini dengan mengetuk file dari bagian **File Lokal** atau dari akun **penyimpanan cloud** yang terhubung.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Editor Tag Evertag" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Mode Pengeditan

Evertag menyediakan dua mode pengeditan:

- **Mode file tunggal**  
  - Navigasi antar file dengan menggesek ke kiri atau kanan pada korsel karya seni.  

- **Mode batch**  
  - Edit beberapa file sekaligus dan terapkan metadata bersama.  
  - Untuk mengaktifkan, gulir ke bawah dan ketuk **Edit file secara bersamaan**.

## Mode File Tunggal

Secara default, aplikasi membuka editor tag dalam mode file tunggal dengan hanya opsi pengeditan utama yang diaktifkan. Dalam mode ini, Anda dapat mengedit kolom metadata paling umum, seperti:

**Judul Lagu, Subjudul, Artis Album, Album, Artis, Komposer, Pelaku, Genre, Komentar, Ketukan Per Menit, Podcast, Kompilasi, Nomor Disk, Nomor Lagu, Total Lagu, Peringkat, Tahun**

Untuk mengakses semua tag yang tersedia, gulir ke bagian bawah layar dan ketuk opsi **Tampilkan Tag Diperluas**. Ini akan mengalihkan editor ke mode diperluas, memungkinkan Anda mengedit lebih dari **120 kolom metadata**, termasuk **Tag MusicBrainz**, **Lirik**, **Peringkat Konsultasi**, nilai replay-gain, urutan pengurutan, metadata podcast, dan lainnya. Gunakan **Pengaturan → Editor tag audio → Tombol di layar utama** untuk secara permanen mengaktifkan Tampilkan Tag Diperluas agar selalu aktif.

{{< cards cols="1">}}
{{< card title="" subtitle="Panel Tindakan Bawah" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Mode Batch

Anda dapat masuk ke pengeditan batch dengan dua cara:

1. **Dari Pengelola File**  
   - Ketuk **Lebih banyak tindakan** (•••) di kanan atas.  
   - Ketuk **Pilih**, pilih beberapa file, lalu ketuk **Mengedit tag audio**.

2. **Dari Editor Tag**  
   - Buka file mana saja, gulir ke bawah, dan ketuk **Edit file secara bersamaan** untuk memuat semua file dari folder yang sama.

{{< cards cols="1">}}
{{< card title="" subtitle="Mode Pengeditan Batch" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Setelah mengedit, ketuk **Simpan** untuk menerapkan perubahan.

## Edit Lirik

Editor diperluas menampilkan kolom **Lirik**. Ketuk untuk membuka daftar lirik — setiap entri lirik memiliki bahasa dan deskripsi tersendiri, sehingga satu lagu dapat menyimpan beberapa terjemahan.

Anda tidak harus mengetik lirik dari awal. Editor menyertakan pintasan pencarian satu ketuk ke database lirik paling populer di web, yang diisi sebelumnya dengan artis dan judul lagu saat ini:

- **Lrclib** — database publik utama untuk **lirik bertanda waktu (gaya LRC)**. Gunakan saat Anda menginginkan lirik sinkron yang menggulir baris demi baris di pemutar yang mendukungnya.
- **Genius** — katalog besar dengan anotasi dan lirik teks biasa yang akurat.
- **Lyricsify** — database berbasis komunitas dengan lirik biasa dan bertanda waktu.
- **Google** — pencarian web umum sebagai cadangan ketika database khusus tidak memiliki kecocokan.

Setiap pintasan hanya muncul ketika layanan yang sesuai dapat dijangkau dari perangkat Anda. Ketuk layanan, salin lirik (atau cap waktu LRC) yang Anda inginkan, kembali ke Evertag, dan tempelkan ke kolom teks — lalu **Simpan** untuk menulis kembali lirik ke dalam tag file audio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Halaman Lirik" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Pilih bahasa dari pemilih:

{{< cards cols="1">}}
  {{< card title="" subtitle="Pemilih Bahasa Lirik" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Kemudian tempel atau ketik teks lirik. Evertag mendukung teks biasa dan lirik bertanda waktu (sinkronisasi) — tempat penampung menunjukkan contoh format gaya LRC, yang persis seperti yang dikembalikan Lrclib dan Lyricsify untuk hasil yang disinkronkan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Editor Teks Lirik" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Atur Peringkat dan Peringkat Konsultasi

Editor diperluas menawarkan kontrol bintang **Peringkat** bersama kontrol tersegmentasi **Peringkat Konsultasi**.

### Peringkat Bintang

Gunakan kolom **Peringkat** untuk memberi lagu skor pribadi dari satu hingga lima bintang. Nilainya ditulis ke tag peringkat standar file (POPM untuk ID3, `rate` untuk MP4, `RATING` untuk Vorbis/APE, dll.), sehingga aplikasi lain yang membaca tag ini — termasuk aplikasi Musik, Plex, Roon, dan sebagian besar editor tag desktop — akan langsung mengambil skor Anda.

{{< cards cols="1">}}
  {{< card title="" subtitle="Peringkat" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Peringkat Konsultasi

**Peringkat Konsultasi** menandai konten lagu menggunakan salah satu nilai dari standar Panduan Orang Tua yang digunakan iTunes Store dan sebagian besar platform musik:

- **Tidak Ofensif** — default untuk lagu tanpa informasi panduan orang tua. File dianggap cocok untuk semua pendengar dan tidak akan menampilkan label konsultasi apa pun di pemutar yang menghormati tag.
- **Eksplisit** — lagu mengandung bahasa atau konten eksplisit. Pemutar yang menghormati kontrol orang tua (aplikasi Musik, aplikasi Apple TV, ekspor Spotify, Plex, dll.) akan menampilkan lencana **E** di sebelah judul dan, ketika pembatasan diaktifkan pada perangkat atau akun, mungkin menyembunyikan lagu dari profil anak-anak atau menolak memutarnya.
- **Bersih** — versi tersensor atau diedit dari lagu eksplisit. Pemutar menampilkan lencana **C** sehingga pendengar dapat membedakan suntingan bersih dari master eksplisit asli, yang berguna ketika kedua versi ada di perpustakaan yang sama.

Anda ingin mengatur atau memperbaiki kolom ini ketika:

- File memiliki label yang salah (misalnya suntingan radio bersih yang secara keliru ditandai sebagai Eksplisit, atau sebaliknya).
- Lagu dirip atau diunduh tanpa tag dan sekarang muncul sebagai Tidak Ofensif meskipun mengandung konten eksplisit — diperlukan agar kontrol orang tua dan perpustakaan yang dibagikan keluarga bekerja dengan benar.
- Anda menyiapkan album untuk pengajuan atau berbagi dan perlu setiap lagu membawa metadata yang konsisten.
- Anda ingin CarPlay, Layar Kunci, pemutar bergaya Apple Music, atau perangkat lunak DJ menampilkan lencana **E** / **C** yang benar di sebelah judul lagu.

Nilainya disimpan di kolom peringkat-konsultasi standar untuk format file (`rtng` untuk MP4, `TXXX:ITUNESADVISORY` untuk ID3, `ITUNESADVISORY` untuk Vorbis), sehingga pemutar apa pun yang membaca metadata panduan orang tua akan melihat pembaruan Anda.

{{< cards cols="1">}}
  {{< card title="" subtitle="Peringkat Konsultasi Lirik" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Edit Sampul Album

Untuk mengubah sampul album:

1. Ketuk **ikon Kamera** di korsel karya seni.  
2. Pilih lokasi gambar: File Lokal, Cloud, Unduhan, atau Perpustakaan Foto.  
3. Pilih gambar untuk diterapkan sebagai seni sampul.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilih Gambar" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Lebih Banyak Tindakan di Editor Tag

Opsi pengeditan tambahan tersedia melalui toolbar di bawah tampilan karya seni.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Lebih Banyak Tindakan" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Pencarian Otomatis Tag Audio

Tindakan ini mengaktifkan mesin pencari tag cerdas, yang menemukan dan mengisi metadata lengkap untuk file audio Anda berdasarkan informasi yang ada.  
Aplikasi menggunakan database MusicBrainz — salah satu database tag paling komprehensif — dengan lebih dari **50 juta** lagu.

### Cari Sampul Album

Gunakan metadata untuk mencari di web karya seni album yang benar.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Cari Sampul Album" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Setelah ditemukan, simpan gambar ke **Foto** menggunakan menu konteks sistem.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tambahkan Gambar ke Foto" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Setelah itu, kembali ke editor tag, ketuk ikon Kamera, pergi ke **Perpustakaan Foto**, dan pilih gambar yang disimpan. Aplikasi akan menetapkannya sebagai sampul untuk file audio Anda.

Anda dapat menyesuaikan cara gambar sampul diskalakan di pengaturan aplikasi.

### Simpan Karya Seni Album

Tindakan ini menyimpan karya seni album saat ini ke folder **Documents**, sehingga Anda dapat menggunakannya kembali nanti.

### Normalisasi Pengkodean

Tindakan ini akan menormalisasi pengkodean teks dari semua tag dalam metadata file audio. Ini sangat membantu jika Anda beralih dari PC Windows, di mana file mungkin menggunakan pengkodean berbeda yang muncul sebagai karakter yang tidak terbaca atau rusak di Mac.

### Pencarian Tag Manual

Cari metadata album secara manual menggunakan database MusicBrainz.  

- Pilih album  

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilih Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Pilih lagu yang benar  

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilih Lagu" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Pilih tag mana yang akan diterapkan  

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilih Tag Audio" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Ketuk **Selesai** untuk menerapkan metadata yang dipilih ke lagu Anda.

### Hapus Tag Audio

Bersihkan semua kolom metadata untuk sebuah file. Berguna saat memulai dari awal. Ketuk **Simpan** untuk mengonfirmasi.

## Pengaturan Editor Tag

Navigasikan ke **Pengaturan → Editor tag audio** untuk menyesuaikan perilaku.

### Penskalaan Sampul Album

Pilih bagaimana sampul album harus diskalakan saat disimpan ke dalam file audio. Anda dapat menonaktifkan penskalaan untuk mempertahankan ukuran gambar asli, tetapi perlu diketahui bahwa beberapa pemutar mungkin tidak mendukung file karya seni besar. Opsi "ukuran asli" adalah bagian dari fitur personalisasi Premium.

### Opsi Penyimpanan Tag

- **ID3v2.4** — Ketika diaktifkan, aplikasi menyimpan tag dalam format ID3v2.4 jika memungkinkan. Nonaktifkan untuk kembali ke ID3v2.3 yang lebih banyak didukung jika tag audio Anda tidak ditampilkan dengan benar di pemutar atau perangkat lama.
- **Tag duplikat** — Ketika diaktifkan, kolom metadata umum diduplikasikan ke dalam kedua bagian tag file. Ini meningkatkan kompatibilitas dengan pemutar audio lama, tetapi dalam kebanyakan kasus tidak diperlukan.

### Opsi Pembaruan Metadata File Cloud

Anda dapat mengontrol bagaimana aplikasi memperbarui metadata untuk file audio yang tersimpan di layanan cloud:

- **Tampilkan pesan konfirmasi**  
  Minta sebelum menerapkan perubahan metadata ke file cloud.

- **Perbarui metadata file secara otomatis**  
  Simpan perubahan metadata ke file cloud secara otomatis setelah mengedit.

- **Jangan perbarui metadata file**  
  Lewati pembaruan file cloud — perubahan hanya akan diterapkan secara lokal.

### Edit File Online

Pilih apa yang terjadi pada salinan lokal yang diunduh dari file cloud setelah mengedit:

- **Selalu hapus file yang diunduh**  
  Hapus salinan lokal setelah menyimpan perubahan.

- **Jangan hapus file yang diunduh**  
  Simpan file yang diunduh di perangkat Anda setelah mengedit.

### Tombol Layar Utama

Sesuaikan tindakan mana yang muncul di layar utama editor tag (Pencarian otomatis tag audio, Pencarian manual tag audio, Cari karya seni album, Simpan karya seni album, Normalisasi pengkodean, Hapus tag audio). Anda juga dapat mengaktifkan **Tampilkan tag diperluas** dan **Edit file secara bersamaan** sehingga editor selalu terbuka dalam mode pilihan Anda.
