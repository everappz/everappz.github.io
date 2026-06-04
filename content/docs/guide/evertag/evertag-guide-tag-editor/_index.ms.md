---
title: "Penyunting Tag"
date: 2020-02-01
description: "Ketahui cara menggunakan Penyunting Tag Evertag untuk mengemas kini metadata muzik, menyunting kulit album, menyunting kelompok berbilang fail, dan mengurus tag dari MusicBrainz. Sesuai untuk mengatur perpustakaan muzik anda pada iOS dan Mac."
keywords: [
  "penyunting tag Evertag", "penyunting metadata audio", "penyunting tag muzik",
  "sunting tag audio iPhone", "penyunting kulit album", "sunting tag audio kelompok",
  "metadata MusicBrainz", "aplikasi pengatur muzik", "panduan Evertag", "penyunting tag ID3"
]
tags: ["panduan", "evertag", "penyunting tag"]
readingTime: 5
---


**Penyunting Tag** adalah skrin utama aplikasi Evertag di mana anda boleh melihat dan menyunting metadata fail audio. Buka skrin ini dengan mengetik fail dari bahagian **Fail Tempatan** atau dari mana-mana akaun **storan awan** yang disambungkan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Skrin Penyunting Tag Evertag" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Mod Pengeditan

Evertag menyediakan dua mod pengeditan:

- **Mod fail tunggal**  
  - Navigasi antara fail dengan meleret ke kiri atau kanan pada karusel karya seni.  

- **Mod kelompok**  
  - Sunting berbilang fail sekaligus dan terapkan metadata yang dikongsi.  
  - Untuk mengaktifkan, tatal ke bawah dan ketik **Sunting fail secara serentak**.

## Mod Fail Tunggal

Secara lalai, aplikasi membuka penyunting tag dalam mod fail tunggal dengan hanya pilihan pengeditan utama yang diaktifkan. Dalam mod ini, anda boleh menyunting medan metadata yang paling biasa, seperti:

**Tajuk Lagu, Sarikata, Artis Album, Album, Artis, Komposer, Pemain, Genre, Komen, Bit Per Minit, Podcast, Kompilasi, Nombor Cakera, Nombor Lagu, Jumlah Lagu, Penilaian, Tahun**

Untuk mengakses semua tag yang tersedia, tatal ke bawah skrin dan ketik pilihan **Tunjukkan Tag Lanjutan**. Ini akan menukar penyunting ke mod lanjutan, membolehkan anda menyunting lebih daripada **120 medan metadata**, termasuk **Tag MusicBrainz**, **Lirik**, **Penilaian Penasihat**, nilai replay-gain, susunan isih, metadata podcast, dan banyak lagi. Gunakan **Tetapan → Penyunting tag audio → Butang pada skrin utama** untuk sentiasa menghidupkan Tunjukkan Tag Lanjutan secara kekal.

{{< cards cols="1">}}
{{< card title="" subtitle="Panel Tindakan Bawah" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Mod Kelompok

Anda boleh memasuki pengeditan kelompok dengan dua cara:

1. **Dari Pengurus Fail**  
   - Ketik **Lebih banyak tindakan** (•••) di bahagian kanan atas.  
   - Ketik **Pilih**, pilih berbilang fail, dan kemudian ketik **Edit tag audio**.

2. **Dari Penyunting Tag**  
   - Buka mana-mana fail, tatal ke bawah, dan ketik **Sunting fail secara serentak** untuk memuatkan semua fail dari folder yang sama.

{{< cards cols="1">}}
{{< card title="" subtitle="Mod Pengeditan Kelompok" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Selepas menyunting, ketik **Simpan** untuk menerapkan perubahan.

## Sunting Lirik

Penyunting lanjutan mendedahkan medan **Lirik**. Ketik untuk membuka senarai lirik — setiap entri lirik mempunyai bahasa dan deskripsi sendiri, jadi satu lagu boleh menyimpan beberapa terjemahan.

Anda tidak perlu menaip lirik dari awal. Penyunting menyertakan pintasan carian satu ketukan ke pangkalan data lirik paling popular di web, yang telah diisi lebih awal dengan artis dan tajuk lagu semasa:

- **Lrclib** — pangkalan data awam utama untuk **lirik berwaktu (gaya LRC)**. Gunakannya apabila anda mahukan lirik segerak yang menatal baris demi baris dalam pemain yang menyokongnya.
- **Genius** — katalog besar dengan anotasi dan lirik teks biasa yang tepat.
- **Lyricsify** — pangkalan data berasaskan komuniti dengan lirik biasa dan bertimestamp.
- **Google** — carian web umum sebagai alternatif apabila pangkalan data khusus tidak mempunyai padanan.

Setiap pintasan hanya muncul apabila perkhidmatan yang sepadan boleh dicapai dari peranti anda. Ketik perkhidmatan, salin lirik (atau timestamp LRC) yang anda mahukan, kembali ke Evertag, dan tampalnya ke dalam medan teks — kemudian **Simpan** untuk menulis lirik kembali ke dalam tag fail audio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Halaman Lirik" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Pilih bahasa dari pemilih:

{{< cards cols="1">}}
  {{< card title="" subtitle="Pemilih Bahasa Lirik" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Kemudian tampal atau taip teks lirik. Evertag menyokong kedua-dua teks biasa dan lirik bertimestamp (disegerakkan) — ruang letak menunjukkan contoh format gaya LRC, yang merupakan tepat apa yang Lrclib dan Lyricsify kembalikan untuk keputusan yang disegerakkan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Penyunting Teks Lirik" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Tetapkan Penilaian dan Penilaian Penasihat

Penyunting lanjutan menawarkan kawalan **Penilaian** bintang bersama kawalan bersegmen **Penilaian Penasihat**.

### Penilaian Bintang

Gunakan medan **Penilaian** untuk memberi lagu skor peribadi dari satu hingga lima bintang. Nilai ditulis ke dalam tag penilaian standard fail (POPM untuk ID3, `rate` untuk MP4, `RATING` untuk Vorbis/APE, dll.), jadi aplikasi lain yang membaca tag ini — termasuk aplikasi Muzik, Plex, Roon, dan kebanyakan penyunting tag desktop — akan mengenali skor anda dengan segera.

{{< cards cols="1">}}
  {{< card title="" subtitle="Penilaian" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Penilaian Penasihat

**Penilaian Penasihat** menandai kandungan lagu menggunakan salah satu nilai dari standard Penasihat Ibu Bapa yang digunakan oleh iTunes Store dan kebanyakan platform muzik:

- **Tidak menyinggung** — lalai untuk lagu tanpa maklumat penasihat ibu bapa. Fail dianggap sesuai untuk semua pendengar dan tidak akan menunjukkan label penasihat dalam pemain yang menghormati tag.
- **Eksplisit** — lagu mengandungi bahasa atau kandungan eksplisit. Pemain yang menghormati kawalan ibu bapa (aplikasi Muzik, aplikasi Apple TV, eksport Spotify, Plex, dll.) akan memaparkan lencana **E** di sebelah tajuk dan, apabila sekatan diaktifkan pada peranti atau akaun, mungkin menyembunyikan lagu dari profil kanak-kanak atau menolak memainkannya.
- **Bersih** — versi yang ditapis atau disunting dari lagu yang sebaliknya eksplisit. Pemain memaparkan lencana **C** supaya pendengar boleh membezakan edit bersih dari master eksplisit asal, yang berguna apabila kedua-dua versi berada dalam perpustakaan yang sama.

Anda perlu menetapkan atau membetulkan medan ini apabila:

- Fail mempunyai label yang salah (contohnya edit radio bersih yang salah ditag sebagai Eksplisit, atau sebaliknya).
- Lagu telah dirip atau dimuat turun tanpa tag dan kini ditunjukkan sebagai Tidak Menyinggung walaupun mengandungi kandungan eksplisit — perlu untuk kawalan ibu bapa dan perpustakaan yang dikongsi keluarga berfungsi dengan betul.
- Anda sedang mempersiapkan album untuk penyerahan atau perkongsian dan memerlukan setiap lagu membawa metadata yang konsisten.
- Anda mahu CarPlay, Skrin Kunci, pemain gaya Apple Music, atau perisian DJ memaparkan lencana **E** / **C** yang betul di sebelah tajuk lagu.

Nilai disimpan dalam medan penilaian penasihat standard untuk format fail (`rtng` untuk MP4, `TXXX:ITUNESADVISORY` untuk ID3, `ITUNESADVISORY` untuk Vorbis), jadi pemain mana-mana yang membaca metadata penasihat ibu bapa akan melihat kemas kini anda.

{{< cards cols="1">}}
  {{< card title="" subtitle="Penilaian Penasihat Lirik" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Sunting Kulit Album

Untuk menukar kulit album:

1. Ketik **ikon Kamera** dalam karusel karya seni.  
2. Pilih lokasi imej: Fail Tempatan, Awan, Muat Turun, atau Perpustakaan Foto.  
3. Pilih imej untuk diterapkan sebagai seni kulit.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilih Imej" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Lebih Banyak Tindakan dalam Penyunting Tag

Pilihan pengeditan tambahan tersedia melalui bar alat di bawah paparan karya seni.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Lebih Banyak Tindakan" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Carian Automatik Tag Audio

Tindakan ini mengaktifkan enjin carian tag pintar, yang mencari dan mengisi metadata lengkap untuk fail audio anda berdasarkan maklumat yang sedia ada.  
Aplikasi menggunakan pangkalan data MusicBrainz — salah satu pangkalan data tag paling komprehensif — dengan lebih daripada **50 juta** lagu.

### Cari Kulit Album

Gunakan metadata untuk mencari karya seni album yang betul di web.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Cari Kulit Album" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Setelah dijumpai, simpan imej ke **Foto** menggunakan menu konteks sistem.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tambah Imej ke Foto" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Selepas itu, kembali ke penyunting tag, ketik ikon Kamera, pergi ke **Perpustakaan Foto**, dan pilih imej yang disimpan. Aplikasi akan menetapkannya sebagai kulit untuk fail audio anda.

Anda boleh menyesuaikan cara imej kulit diskalakan dalam tetapan aplikasi.

### Simpan Karya Seni Album

Tindakan ini menyimpan karya seni album semasa ke folder **Dokumen**, supaya anda boleh menggunakannya semula kemudian.

### Normalkan Pengekodan

Tindakan ini akan menormalkan pengekodan teks semua tag dalam metadata fail audio. Ini amat berguna jika anda beralih dari PC Windows, di mana fail mungkin menggunakan pengekodan yang berbeza yang muncul sebagai aksara tidak terbaca atau bercelaru pada Mac.

### Carian Tag Manual

Cari metadata album secara manual menggunakan pangkalan data MusicBrainz.  

- Pilih album  

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilih Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Pilih lagu yang betul  

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilih Lagu" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Pilih tag yang hendak diterapkan  

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilih Tag Audio" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Ketik **Selesai** untuk menerapkan metadata yang dipilih ke lagu anda.

### Padam Tag Audio

Kosongkan semua medan metadata untuk fail. Berguna apabila memulakan dari awal. Ketik **Simpan** untuk mengesahkan.

## Tetapan Penyunting Tag

Navigasi ke **Tetapan → Penyunting tag audio** untuk menyesuaikan tingkah laku.

### Penskalaan Kulit Album

Pilih cara kulit album sepatutnya diskalakan apabila disimpan ke dalam fail audio. Anda boleh menyahaktifkan penskalaan untuk memastikan saiz imej asal, tetapi sedar bahawa sesetengah pemain mungkin tidak menyokong fail karya seni yang besar. Pilihan "saiz asal" adalah sebahagian daripada ciri personalisasi Premium.

### Pilihan Penyimpanan Tag

- **ID3v2.4** — Apabila diaktifkan, aplikasi menyimpan tag dalam format ID3v2.4 apabila mungkin. Nyahaktifkan untuk kembali ke ID3v2.3 yang lebih disokong secara meluas jika tag audio anda tidak dipaparkan dengan betul pada pemain atau peranti lama.
- **Tag duplikat** — Apabila diaktifkan, medan metadata biasa diduplikasikan ke dalam kedua-dua bahagian tag fail. Ini meningkatkan keserasian dengan pemain audio lama, tetapi dalam kebanyakan kes tidak diperlukan.

### Pilihan Kemas Kini Metadata Fail Awan

Anda boleh mengawal cara aplikasi mengemas kini metadata untuk fail audio yang disimpan dalam perkhidmatan awan:

- **Tunjukkan mesej pengesahan**  
  Tanya sebelum menerapkan perubahan metadata ke fail awan.

- **Kemas kini metadata fail secara automatik**  
  Simpan perubahan metadata ke fail awan secara automatik selepas menyunting.

- **Jangan kemas kini metadata fail**  
  Langkau mengemas kini fail awan — perubahan akan diterapkan secara tempatan sahaja.

### Sunting Fail Dalam Talian

Pilih apa yang berlaku pada salinan yang dimuat turun secara tempatan bagi fail awan selepas menyunting:

- **Sentiasa padam fail yang dimuat turun**  
  Buang salinan tempatan selepas menyimpan perubahan.

- **Jangan padam fail yang dimuat turun**  
  Simpan fail yang dimuat turun pada peranti anda selepas menyunting.

### Butang Skrin Utama

Sesuaikan tindakan yang muncul pada skrin utama penyunting tag (Carian automatik tag audio, Carian manual tag audio, Cari karya seni album, Simpan karya seni album, Normalkan pengekodan, Padam tag audio). Anda juga boleh beralih **Tunjukkan tag lanjutan** dan **Sunting fail secara serentak** supaya penyunting sentiasa dibuka dalam mod pilihan anda.
