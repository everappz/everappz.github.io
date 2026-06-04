---
title: "Pemutar Audio"
date: 2020-02-01
description: "Pelajari cara menggunakan pemutar audio Flacbox di iPhone, iPad, dan Mac. Kendalikan pemutaran, kelola antrian, konfigurasikan mesin audio FFmpeg / sistem, ubah sample rate, koreksi pitch, durasi buffer IO, equalizer, bookmark audio, AirPlay 2, Google Cast, CarPlay, widget, dan pintasan keyboard Mac."
keywords: [
  "panduan pemutar Flacbox", "pengaturan pemutar audio", "equalizer Flacbox",
  "streaming musik AirPlay", "musik Google Cast", "bookmark audio",
  "antrian pemutaran Flacbox", "pengulangan acak Flacbox", "kontrol volume Flacbox",
  "mini player macOS", "aplikasi musik voiceover",
  "Flacbox FFmpeg", "koreksi pitch Flacbox", "sample rate Flacbox",
  "DAC eksternal Flacbox", "surround sound Flacbox", "buffer IO Flacbox",
  "kecepatan pemutaran Flacbox", "sleep timer Flacbox"
]
tags: ["panduan", "flacbox", "pemutar"]
readingTime: 14
---


Pemutar Audio adalah layar utama aplikasi tempat Anda mengontrol musik dan sebagian besar fitur pemutaran. Di sinilah mesin audio hi-res Flacbox — yang dibangun di atas codec sistem ditambah perpustakaan **FFmpeg** yang disertakan — melakukan kerja keras. Mari jelajahi cara menggunakannya.

## Mengakses Pemutar Audio

Anda dapat membuka pemutar layar penuh dari bilah mini player. Di iPhone, mini player berada di bagian bawah layar utama. Di iPad dan Mac, ada di sisi kiri. Untuk menyembunyikan mini player di iPhone, ketuk sekali dan geser ke bawah. Untuk menutup sepenuhnya pemutar layar penuh, ketuk tombol tutup di sudut kanan bawah.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Utama Pemutar Audio Flacbox" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Format Audio yang Didukung

Flacbox memutar format audio paling populer — baik codec sistem Apple maupun banyak format tambahan yang ditangani oleh mesin FFmpeg yang disertakan:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

## Kontrol Pemutaran

Di bagian bawah layar pemutar, Anda akan melihat tombol untuk Putar, Jeda, Trek Berikutnya, dan Trek Sebelumnya. Ada juga tombol opsional seperti Berikutnya 30 dtk dan Sebelumnya 30 dtk yang dapat Anda aktifkan di pengaturan aplikasi. Anda dapat maju cepat atau mundur dengan menahan tombol Berikutnya / Sebelumnya. Untuk melompat ke bagian tertentu dari trek, seret slider pemutaran.

## Ulangi dan Acak

Ketuk tombol ulangi untuk beralih antara mode pengulangan:

- **Ulangi Semua** — memutar ulang semua trek dalam antrian.
- **Ulangi Satu** — mengulang hanya trek saat ini.
- **Berhenti Ulang** — menjeda saat trek saat ini berakhir.
- **Tanpa Pengulangan** — memutar antrian sekali tanpa mengulang.

Gunakan tombol **Acak** untuk mengacak urutan trek dalam antrian.

## Kontrol Volume

Buka layar Pengaturan Audio dengan mengetuk ikon suara di bawah kontrol pemutaran untuk mengakses slider volume. Anda juga akan menemukan tombol untuk **Google Cast** dan **AirPlay** di sini.

## Google Cast (Chromecast)

Untuk pengguna Google Cast, ikon **Cast** muncul di bagian bawah pemutar. Ketuk untuk memilih perangkat dan mulai streaming. Pastikan perangkat dan penerima Google Cast berada di jaringan Wi-Fi yang sama.

## AirPlay

Untuk AirPlay, cari tombol **AirPlay** di bagian bawah pemutar. Ketuk dan pilih perangkat untuk streaming. Flacbox mendukung **AirPlay 2**, sehingga Anda dapat memutar ke beberapa HomePod, Apple TV, atau speaker yang kompatibel dengan AirPlay 2 secara bersamaan.

## Equalizer Audio

Flacbox menyertakan **equalizer 10 band** dengan preset bergaya iPod. Ketuk Equalizer pada tampilan volume, lalu aktifkan di sudut kanan atas. Anda dapat menggunakan preset seperti Akustik dan Penguat Bass, atau menyesuaikan setiap band frekuensi dengan slider. Instruksi lebih terperinci tentang cara menggunakan equalizer tersedia [di sini](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalizer Pemutar Audio Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Toolbar Mode Pemutar

Untuk beberapa gaya pemutar, ada toolbar khusus di bagian atas pemutar layar penuh:

- **Cari** — cepat temukan trek tertentu dalam antrian pemutar.
- **Kontrol Kecepatan Pemutaran** — sesuaikan kecepatan pemutaran dari 0,02× hingga 3,00×.
- **Bookmark Audio** — buat beberapa bookmark per trek.

## Antrian Pemutar

Untuk melihat antrian pemutar, ketuk tombol antrian di sisi kanan lagu saat ini. Setiap lagu dalam antrian memiliki lebih banyak tindakan — ketuk tiga titik untuk melihatnya.

{{< cards cols="1">}}
  {{< card title="" subtitle="Antrian Pemutaran Flacbox" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Komentar / Lirik

Untuk melihat komentar trek dan lirik yang disematkan, serta file LRC, ikuti langkah-langkah berikut:

1. Buka **Pengaturan**.
2. Pergi ke **Pemutar Audio**.
3. Pilih **Personalisasi**.
4. Ketuk **Tombol di layar utama**.
5. Aktifkan **Komentar**.

Setelah ini, ketuk tombol antrian pemutar di bagian bawah layar beberapa kali untuk beralih dari tampilan artwork / antrian ke tampilan komentar. Instruksi lengkap tersedia [di sini](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Lirik dan Komentar Flacbox" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Menu Opsi

Setiap lagu dalam antrian pemutar audio memiliki menu dengan lebih banyak tindakan, dapat diakses dengan mengetuk tombol tiga titik di dekat judul lagu.

- **Putar Berikutnya** — menambahkan lagu ke atas antrian pemutar.
- **Tambah ke Daftar Putar** — menyertakan lagu dalam daftar putar.
- **Tambah ke Favorit** — menandai lagu sebagai favorit.
- **Unduh** — menyimpan lagu ke file lokal.
- **Mengedit tag audio** — membuka editor tag audio bawaan.
- **Tampilkan di Folder** — menampilkan folder tempat file audio disimpan.
- **Tampilkan di Finder** — untuk file yang diimpor dari Mac.
- **Buka Di** — mengekspor file audio ke aplikasi lain.
- **Hapus dari Antrian** — menghapus lagu yang dipilih dari antrian pemutar audio.
- **Hapus dari Layanan Cloud** — menghapus lagu dari perpustakaan musik dan cloud storage. **Tindakan ini tidak dapat dibalik.**
- **Hapus dari File Lokal** — menghapus lagu dari perpustakaan musik dan penyimpanan lokal. **Tindakan ini tidak dapat dibalik.**
- **Hapus dari Perpustakaan Musik** — menghapus lagu dari perpustakaan musik, sambil menyimpan file di penyimpanan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Opsi untuk Item dalam Antrian Pemutaran" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Tindakan Pemutar Tambahan

Ketuk tombol **Lebih banyak tindakan** "..." di sisi kiri judul lagu yang sedang diputar untuk melihat tindakan tambahan.

- **Lanjutkan Pemutaran** — lanjutkan dari tempat Anda berhenti.
- **Cari** — cepat temukan trek tertentu dalam antrian pemutar audio.
- **Tandai Halaman** — lihat daftar bookmark audio yang dibuat.
- **Komentar** — lihat komentar trek dan lirik yang disematkan.
- **Kecepatan** — sesuaikan kecepatan pemutaran sesuai selera.
- **Terbaru** — akses daftar lagu yang baru diputar.
- **Favorit** — lihat koleksi lagu favorit Anda.
- **Equalizer Audio** — aktifkan equalizer audio.
- **Sleep Timer** — atur timer untuk menghentikan pemutaran setelah interval tertentu.
- **Simpan Antrian ke Daftar Putar** — simpan antrian pemutar audio saat ini sebagai daftar putar baru.
- **Hapus Antrian** — bersihkan antrian pemutar dan hentikan pemutaran.
- **Pengaturan** — akses pengaturan pemutar audio.
- **Bantuan** — temukan bantuan dan panduan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Lebih banyak tindakan Pemutar Audio Flacbox" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Bookmark Audio

Fitur ini memungkinkan Anda membuat beberapa bookmark untuk trek dalam perpustakaan musik — sempurna untuk audiobook, kuliah, mix DJ panjang, atau menandai refrain trek favorit.

Untuk membuat bookmark baru:

- Mulai memainkan lagu yang diinginkan.
- Buka layar pemutar.
- Ketuk tombol **Tandai Halaman** pada toolbar mode pemutar.
- Pilih **Tambah Bookmark**.
- Pilih waktu bookmark dan ketuk **Selesai** di sudut kanan atas.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Bookmark Audio Flacbox" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Terbaru dan Favorit

Di layar pemutar, ketuk tiga titik untuk mengakses Terbaru dan Favorit. Instruksi terperinci tentang cara mengekspor daftar lagu tersedia [di sini](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Hubungkan iPhone ke mobil melalui USB atau Apple CarPlay nirkabel. Antarmuka CarPlay mencakup tab khusus untuk Perpustakaan, Koneksi, File Lokal, dan Pengaturan.

[Baca panduan CarPlay lengkap](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox di Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widget Layar Utama (iPhone & iPad)

Flacbox mendukung widget Layar Utama dan Layar Kunci iOS. Pastikan Widget diaktifkan di Pengaturan → Widget → Aktifkan Widget, lalu tekan lama Layar Utama atau Layar Kunci, ketuk **+**, cari **Flacbox**, dan tambahkan widget.

## Jendela Mini Player (Khusus Mac)

Pengguna Mac dapat menggunakan mini player kompak yang selalu di atas. Pindahkan kursor ke sudut kanan bawah jendela Flacbox, ubah ukurannya ke ukuran terkecil, dan ketuk tombol collapse.

## Pintasan Keyboard (Khusus Mac)

Untuk pengguna Mac, tekan spasi untuk Putar / Jeda. Pintasan untuk Stop, Lagu Berikutnya, Lagu Sebelumnya, Lewati Waktu, Ulangi, Acak, dan Kecepatan Pemutaran juga tersedia.

## Pengaturan Pemutar Audio

Untuk mengakses pengaturan, ketuk tombol Lebih di layar pemutar dan pilih Pengaturan.

### Umum

- **Mode Pengulangan** — pilih cara pemutar audio berperilaku saat trek selesai.
- **Mode Acak** — acak urutan trek dalam antrian.
- **Codec Audio** — pilih mesin audio yang digunakan untuk pemutaran (System Codec + FFmpeg atau FFmpeg).
- **Sample Rate Output Audio** — nilai yang tersedia: 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, dan 96 kHz.
- **Jumlah Saluran Output Audio** — Mono, Stereo, dll.
- **Durasi Buffer IO Output Audio yang Disukai** — konfigurasikan durasi buffer.
- **Mode Output Audio (hanya iOS)** — konfigurasikan mode output audio campuran.
- **Simpan Posisi Pemutaran** — memastikan aplikasi menyimpan dan memulihkan posisi pemutaran.
- **Simpan Status Pemutar Audio** — mempertahankan status pemutar audio sebelum Anda menutup aplikasi.

### Personalisasi

- **Gaya Layar Pemutar Audio** — konfigurasikan posisi elemen.
- **Gaya Gulir Sampul Album** — konfigurasikan gaya gulir yang disukai.
- **Elemen Tambahan** — aktifkan elemen ekstra di layar pemutar.
- **Tindakan Layar Utama** — konfigurasikan tombol mana yang terlihat.
- **Kontrol Pemutaran di Layar Kunci** — pilih kontrol mana yang muncul.
- **Tombol Lewati Waktu** — pilih interval waktu.

### Pemuatan File

- **Waktu Pra-muat** — atur interval waktu buffering.
- **Gunakan URL Langsung** — saat diaktifkan, URL langsung digunakan untuk memuat lagu.

### Equalizer Audio

Konfigurasikan equalizer audio 10 band. Baca lebih lanjut [di sini](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Kecepatan Pemutaran

Sesuaikan kecepatan pemutaran pemutar audio dari **0,02× hingga 3,00×**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Kecepatan Pemutaran Flacbox" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Koreksi Pitch

Ubah pengaturan koreksi pitch menggunakan nilai yang telah ditentukan. Rentang dari **-1000 hingga +1000**.

### Cache Pemutaran

Lagu dalam antrian pemutar audio diunduh secara otomatis untuk memastikan pemutaran yang lancar. Anda juga dapat mengonfigurasi ukuran cache pemutar audio di sini.

### Sleep Timer

Aktifkan timer untuk menghentikan pemutaran secara otomatis setelah periode tertentu.

## Aksesibilitas

Flacbox sepenuhnya dapat diakses dengan **VoiceOver**. Setiap komponen memiliki label dan deskripsi yang dirancang dengan baik. Ketika VoiceOver aktif, aplikasi beralih ke **Mode Teks**.

### Menyesuaikan Slider dengan VoiceOver

1. **Pilih slider** — geser kiri atau kanan sampai VoiceOver mengumumkannya.
2. **Sesuaikan nilainya** — ketuk dua kali dan tahan slider, lalu seret ke atas atau ke bawah.

### Menyesuaikan Posisi Trek dalam Daftar dengan VoiceOver

1. Ketuk ikon indikator urutan di dekat judul trek.
2. Ketuk dua kali indikator urutan dengan cepat. Pada ketukan kedua, jangan lepaskan jari.
3. Pindahkan sel ke posisi barunya.
