---
title: "Pemutar Media"
date: 2020-02-01
lastmod: 2026-06-01
description: "Pelajari cara menggunakan pemutar media Evervideo di iPhone, iPad, dan Mac. Picture-in-Picture, dekoding hardware H.264 / HEVC, equalizer audio dan video, subtitle primer dan sekunder, pemilihan trek audio dan video, penskalaan dan rotasi video, kecepatan pemutaran, sleep timer, AirPlay 2, Google Chromecast, stream RTSP, dan pemutar kompak yang selalu aktif di layar."
keywords: [
  "panduan pemutar Evervideo", "pengaturan pemutar video", "equalizer Evervideo",
  "Picture-in-Picture iPhone", "video PiP iPad", "video PiP Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "subtitle video iPhone", "subtitle SRT eksternal",
  "pemutar subtitle ASS SSA", "libass iOS",
  "dual subtitle belajar bahasa",
  "kecerahan kontras equalizer video", "equalizer audio pemutar video",
  "kunci rotasi pemutar video", "mode penskalaan video iOS",
  "decoder H.264 hardware iPhone", "decoder HEVC hardware iPad",
  "kecepatan pemutaran video", "pemutar video FFmpeg iOS",
  "pemutar RTSP iPhone", "pemutar video kompak",
  "pemutar video VR 360 iPhone"
]
tags: ["panduan", "evervideo", "pemutar", "PiP", "subtitle", "equalizer video"]
readingTime: 14
---


Pemutar Media adalah layar utama aplikasi tempat Anda mengontrol pemutaran dan sebagian besar fitur Evervideo. Ini memutar file video maupun audio dan dibangun di atas pemutar berbasis FFmpeg kustom dengan dekoding H.264 dan HEVC yang dipercepat perangkat keras. Mari kita jelajahi cara menggunakannya.

## Mengakses Pemutar Media

Anda dapat membuka pemutar layar penuh dari bilah pemutar kompak. Di iPhone, pemutar kompak berada di bagian atas layar utama. Di iPad dan Mac, pemutar kompak berada di sisi kiri (atau bagian atas panel utama). Untuk menutup pemutar layar penuh kembali ke tampilan kompak, ketuk tombol tutup di pojok kanan bawah atau geser ke bawah. Untuk menyembunyikan pemutar kompak sepenuhnya, ketuk dan geser ke bawah sekali lagi.

Pemutar kompak tetap terlihat saat Anda menelusuri perpustakaan, manajer file, atau pengaturan, sehingga Anda tidak pernah kehilangan video saat mencari video berikutnya.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pemutar Media Layar Penuh Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Format Video dan Audio yang Didukung

Evervideo memutar hampir semua kontainer dan codec modern melalui mesin FFmpeg yang disertakan, dengan dekoding H.264 dan HEVC yang dipercepat perangkat keras pada perangkat yang didukung.

- **Kontainer video:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — dan banyak lagi.
- **Codec video:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — ditambah hampir semua codec lain yang didukung FFmpeg.
- **Codec audio:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — dan banyak lagi.
- **Format subtitle:** SRT, VTT (WebVTT), ASS / SSA, dan trek subtitle teks atau gambar yang tertanam.
- **Protokol streaming:** HTTP / HTTPS, HLS (m3u8), RTSP (kamera IP dan IPTV), dan streaming file langsung melalui SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Ini mencakup hampir setiap file video yang mungkin Anda temui — termasuk rip MKV, stream RTSP kamera keamanan, dan unduhan web AV1 webm.

## Kontrol Pemutaran

Di bagian bawah layar pemutar, Anda akan melihat tombol Putar, Jeda, Berikutnya, dan Sebelumnya. Ada juga tombol opsional seperti Lewati Maju dan Lewati Mundur (default 10 detik) yang dapat Anda aktifkan di pengaturan aplikasi. Tahan tombol Berikutnya / Sebelumnya untuk maju cepat atau mundur. Seret slider pemutaran untuk melompat ke posisi mana pun.

## Ulangi dan Acak

Ketuk tombol ulangi untuk beralih antara mode ulangi:

- **Ulangi Semua** — mengulang setiap video dalam antrean Anda.
- **Ulangi Satu** — mengulangi video saat ini saja.
- **Hentikan Ulangi** — berhenti ketika video saat ini berakhir.
- **Tidak Ada Pengulangan** — memutar antrean sekali tanpa mengulang.

Gunakan tombol **Acak** untuk mengacak urutan video dalam antrean.

## Picture-in-Picture (PiP)

Di iPhone dan iPad, Evervideo sepenuhnya mendukung Picture-in-Picture (PiP). Ketuk ikon PiP pada layar pemutar atau cukup geser Evervideo ke latar belakang — video terus diputar dalam jendela mengambang di atas setiap aplikasi lain. Seret jendela mengambang ke sudut mana pun; cubit untuk mengubah ukuran; ketuk sekali untuk memunculkan kontrol dasar putar / jeda / lewati; ketuk tombol perluas kecil untuk kembali ke Evervideo penuh.

PiP bekerja dengan setiap format video yang diputar Evervideo, termasuk file yang di-streaming cloud dan stream RTSP. PiP juga terus berjalan saat ponsel Anda terkunci (tergantung pengaturan Auto-Lock Anda).

## Pemutar Kompak

Pemutar kompak adalah pemutar mini persisten yang tetap terlihat di bagian atas setiap layar di aplikasi saat Anda menelusuri perpustakaan, manajer file, atau pengaturan. Ketuk untuk memperluas ke pemutar layar penuh; geser ke bawah untuk melipatnya kembali.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pengaturan Video Evervideo dari Tampilan Pemutar Kompak di Layar Utama" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Untuk AirPlay, ketuk tombol AirPlay pada pemutar. Evervideo mendukung AirPlay 2, sehingga Anda dapat melakukan streaming video ke Apple TV, HomePod, atau speaker atau smart TV yang kompatibel dengan AirPlay 2. Pada pengaturan dengan beberapa perangkat AirPlay, Anda dapat mengarahkan audio ke beberapa penerima secara bersamaan.

## Google Chromecast

Untuk pengguna Google Cast, ikon Cast muncul pada pemutar. Ketuk untuk memilih perangkat dan mulai melakukan casting. Pastikan ponsel dan penerima Cast berada di jaringan Wi-Fi yang sama. Tidak setiap codec didukung oleh perangkat keras Chromecast — beberapa file mungkin perlu transcoding.

## Stream RTSP Langsung

Evervideo dapat memutar sumber RTSP secara langsung — kamera IP, kamera bel pintu, stream IPTV, siaran langsung, dan URL `rtsp://` lainnya. Tambahkan stream sebagai koneksi RTSP di File → Tautan Online → Tambahkan tautan, lalu ketuk untuk mulai menonton. Stream RTSP bekerja dalam Picture-in-Picture, pemutar kompak, dan dapat dicast melalui AirPlay 2 dan Chromecast seperti video biasa.

## Pemilihan Trek Audio

Untuk video dengan beberapa trek audio (komentar, dubbing bahasa alternatif, trek sutradara), ketuk tombol Lebih banyak tindakan pada pemutar dan pilih Trek Audio — lalu pilih trek yang diinginkan. Ini penting untuk film berbahasa asing, file BDMV / MKV dengan beberapa dubbing, dan konten instruksional dengan trek komentar.

## Pemilihan Trek Video

Beberapa file video menyertakan beberapa aliran video (Blu-ray multi-sudut, potongan alternatif). Pilih Trek Video dari menu Lebih banyak tindakan untuk beralih di antara keduanya saat pemutaran berlangsung.

## Subtitle — Internal dan Eksternal

Evervideo memberi Anda kontrol yang halus atas subtitle:

- **Trek subtitle** — pilih dari trek yang tertanam dalam file.
- **File subtitle eksternal** — muat file `.srt`, `.vtt`, `.ass`, atau `.ssa` dari perangkat, iCloud Drive, atau layanan cloud yang terhubung.
- **Rendering Libass** — gaya ASS / SSA lanjutan (font, warna, posisi, efek karaoke) dirender dengan benar berkat libass yang disertakan.
- **Pemilihan font** — pilih font kustom untuk subtitle primer dan font terpisah untuk subtitle sekunder. Font bawaan ditambah font yang diinstal di perangkat tersedia.

Anda dapat mengonfigurasi semua ini di Pengaturan → Subtitle sebelum pemutaran, atau gunakan Lebih banyak tindakan → Subtitle dari pemutar untuk beralih saat sedang berjalan.

## Equalizer Audio

Evervideo menyertakan equalizer audio penuh untuk menyetel soundtrack video untuk headphone, speaker, atau pengaturan hi-fi Anda. Ketuk ikon equalizer pada tampilan volume (atau tindakan Equalizer Audio pada menu Lebih banyak tindakan pemutar), nyalakan equalizer dengan sakelar di pojok kanan atas, dan pilih preset atau seret slider band untuk membuat preset Anda sendiri. Preset kustom dapat diekspor dan diimpor sehingga Anda dapat berbaginya di seluruh perangkat atau mencadangkannya.

## Equalizer Video

Untuk menyetel gambar, Evervideo menyediakan equalizer video khusus — sesuaikan kecerahan, kontras, saturasi, dan rona secara real time selama pemutaran. Seperti equalizer audio, preset video kustom dapat diekspor dan diimpor untuk berbagi atau pencadangan. Gunakan untuk mencerahkan adegan gelap di hari yang cerah, meningkatkan saturasi pada konten yang pudar, atau menghangatkan cast warna dingin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalizer Video Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Mode Penskalaan Video

Pilih cara video mengisi layar:

- **Pas** — pertahankan rasio aspek asli; bilah hitam jika diperlukan.
- **Isi** — isi seluruh layar, memotong video jika diperlukan.
- **Regangkan** — regangkan video untuk mengisi layar, mendistorsi jika diperlukan.
- **Asli** — pertahankan resolusi asli pada 1:1.

## Rotasi Video

Untuk video yang direkam dengan orientasi yang salah, pilih **Lebih banyak tindakan → Rotasi** dan pilih **0°**, **90°**, **180°**, atau **270°** untuk memutar gambar tanpa meninggalkan pemutar.

## Dekoding Hardware (H.264 dan HEVC)

Di Pengaturan → Pemutar → Video, Anda dapat mengaktifkan / menonaktifkan Dekoding Hardware H.264 dan Dekoding Hardware H.265 (HEVC) secara independen. Dekoding hardware lebih cepat, menggunakan lebih sedikit baterai, dan berjalan lebih dingin — tetapi dalam kasus yang jarang terjadi (file rusak, profil eksotis) Anda mungkin perlu menonaktifkan dekoding hardware dan kembali ke dekoding FFmpeg perangkat lunak. Evervideo memungkinkan Anda melakukan itu per file dari menu Lebih banyak tindakan pemutar.

## Viewport VR 360°

Evervideo menyertakan viewport VR / 360° untuk file video sferis. Saat memutar video 360°, Anda dapat menyeret untuk melihat sekeliling, mencubit untuk memperbesar, dan Evervideo akan memperbarui rendering secara real time.

## Kecepatan Pemutaran

Ketuk kontrol Kecepatan pada toolbar pemutar untuk mengubah kecepatan pemutaran — perlambat untuk analisis (0,25× atau 0,5×) atau percepat untuk tutorial dan kuliah (1,25×, 1,5×, 2×, dan hingga 3×). Ketuk ikon konfigurasi di pojok kanan atas layar Kecepatan untuk beralih ke mode presisi dengan penyesuaian yang lebih halus. Koreksi pitch per-trek juga tersedia.

{{< cards cols="1">}}
  {{< card title="" subtitle="Kecepatan Pemutaran Evervideo di Toolbar Utama" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Antrean Pemutar

Untuk melihat antrean pemutar, ketuk tombol antrean pada pemutar. Setiap video dalam antrean memiliki lebih banyak tindakan — ketuk tiga titik untuk melihatnya. Untuk menyusun ulang video dalam antrean, gunakan indikator urutan ulang dekat judul dan seret ke posisi baru.

{{< cards cols="1">}}
  {{< card title="" subtitle="Antrean Pemutaran Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Sleep Timer

Buka Pengaturan → Pemutar → Sleep Timer, nyalakan, dan pilih berapa lama Anda ingin pemutaran berlanjut sebelum berhenti otomatis. Anda juga dapat menambahkan tombol Sleep Timer langsung ke layar pemutar utama melalui Pengaturan → Pemutar → Personalisasi → Tindakan Layar Utama.

## Bookmark Pemutar

Simpan tempat Anda dalam video panjang — kuliah, audiobook-on-video, tutorial, unduhan YouTube satu jam — dengan mengetuk Tambahkan Bookmark dari menu Lebih banyak tindakan. Bookmark muncul di daftar Lebih banyak tindakan → Bookmark video dan bertahan antar sesi.

## Menu Lebih banyak tindakan

Ketuk tombol **Lebih banyak tindakan "..."** pada pemutar untuk mengakses fungsi tambahan.

- **Lanjutkan Pemutaran** — lanjutkan antrean dari posisi terakhir.
- **Cari** — temukan video tertentu dalam antrean.
- **Bookmark** — lihat dan lompat ke bookmark.
- **Kecepatan** — sesuaikan kecepatan pemutaran.
- **Terbaru** — video yang baru diputar.
- **Favorit** — video yang difavoritkan.
- **Equalizer Audio** — aktifkan equalizer audio.
- **Equalizer Video** — aktifkan equalizer video.
- **Trek Audio** — pilih aliran audio.
- **Trek Video** — pilih aliran video.
- **Subtitle** — trek primer / sekunder, file eksternal, font.
- **Rotasi** — putar gambar 0° / 90° / 180° / 270°.
- **Mode Penskalaan** — Pas / Isi / Regangkan / Asli.
- **Picture-in-Picture** — masuk ke mode PiP.
- **AirPlay** / **Chromecast** — kirim ke perangkat.
- **Sleep Timer** — atur timer untuk menghentikan pemutaran.
- **Simpan Antrean ke Daftar Putar** — simpan antrean saat ini sebagai daftar putar baru.
- **Hapus Antrean** — bersihkan antrean dan hentikan pemutaran.
- **Pengaturan** — langsung ke pengaturan pemutar.
- **Bantuan** — buka panduan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Layar Lebih Banyak Tindakan Pemutar Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Pengaturan Pemutar

Pohon pengaturan Pemutar lengkap didokumentasikan dalam [panduan Pengaturan](/docs/guide/evervideo/evervideo-guide-settings/). Bagian yang paling sering digunakan:

- **Umum** — Mode Ulangi, Mode Acak, Simpan Status Pemutar, Simpan Posisi Pemutaran, Interval waktu lewati.
- **Video** — Dekoding hardware H.264 / HEVC, equalizer video, mode penskalaan, rotasi, mode tampilan, FPS pilihan, format piksel pilihan, viewport VR.
- **Audio** — Equalizer audio, laju sampel, saluran, durasi buffer IO, mode campuran.
- **Subtitle** — Trek primer / sekunder, pemilihan file eksternal, font, font sekunder.
- **Perangkat** (iOS) — AirPlay / Chromecast.
- **Personalisasi** — Gaya tata letak pemutar (Minimal / Bawah / Antik / Klasik), tindakan layar utama, kontrol layar kunci.
- **Cache Pemutaran** — cache disk untuk streaming yang lebih lancar.
- **Sleep Timer** — berhenti otomatis.

## Aksesibilitas

Evervideo sepenuhnya dapat diakses dengan VoiceOver. Setiap komponen memiliki label dan deskripsi yang dirancang dengan baik. Saat VoiceOver aktif, aplikasi beralih ke Mode Teks sehingga hanya elemen yang bermakna yang ditampilkan — meningkatkan kecepatan navigasi dan kejelasan. Anda juga dapat mengaktifkan Mode Teks di Pengaturan → Aksesibilitas → Mode Teks.

### Menyesuaikan Slider dengan VoiceOver

1. **Pilih slider** — geser kiri atau kanan hingga VoiceOver mengumumkannya.
2. **Sesuaikan nilainya** — ketuk dua kali dan tahan slider, lalu seret ke atas atau ke bawah untuk mengubah nilai dengan cepat. VoiceOver mengumumkan nilai baru saat Anda melakukan perubahan.

Komponen lain bekerja seperti yang diharapkan, menggunakan pola VoiceOver yang disediakan sistem.
