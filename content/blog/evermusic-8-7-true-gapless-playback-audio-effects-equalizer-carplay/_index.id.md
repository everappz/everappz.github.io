---
title: "Evermusic 8.7: Pemutaran Tanpa Jeda Sesungguhnya, Efek Audio, Normalisasi Volume, Equalizer yang Didesain Ulang"
date: 2026-07-05
description: "Evermusic 8.7 untuk iPhone, iPad, dan Mac menambahkan pemutaran tanpa jeda yang sesungguhnya, lima efek audio studio (Reverb, Delay, Distorsi, Kompresor, Crossfeed), normalisasi volume EBU R128, equalizer 10-band yang didesain ulang dengan impor/ekspor preset, mesin streaming AVAudioEngine yang dibangun ulang dengan dukungan FLAC dan Ogg Vorbis, serta CarPlay dan Sedang Diputar yang lebih cepat dan akurat."
keywords: ["Evermusic 8.7", "pembaruan Evermusic", "pemutaran tanpa jeda sesungguhnya iPhone", "pemutar musik tanpa jeda iOS", "pemutaran tanpa jeda CarPlay", "efek audio pemutar musik iPhone", "reverb delay distorsi kompresor crossfeed iOS", "crossfeed headphone iOS", "normalisasi volume iPhone", "normalisasi kekerasan pemutar musik", "normalisasi EBU R128 iOS", "alternatif replay gain iPhone", "equalizer 10-band iPhone", "equalizer grafis aplikasi iOS", "impor ekspor preset equalizer", "pemutar FLAC iPhone", "pemutar Ogg Vorbis iOS", "pemutar musik lossless iPhone 2026", "pemutar musik AVAudioEngine", "pemutar musik CarPlay iPhone", "akurasi Sedang Diputar layar kunci", "pemutar musik cloud iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Pemutaran Tanpa Jeda", "Efek Audio", "Reverb", "Delay", "Distorsi", "Kompresor", "Crossfeed", "Normalisasi Volume", "EBU R128", "Equalizer", "FLAC", "Ogg Vorbis", "CarPlay", "Sedang Diputar", "Liquid Glass", "Yang Baru"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Ringkasan:** [Evermusic 8.7](/products/evermusic) adalah rilis yang berfokus pada kualitas suara untuk iPhone, iPad, dan Mac. Rilis ini menghadirkan **pemutaran tanpa jeda yang sesungguhnya** (tanpa jeda, klik, atau bunyi antar lagu), satu set lengkap **efek audio studio** — Reverb, Delay, Distorsi, Kompresor, dan Crossfeed — serta **normalisasi volume EBU R128** yang menjaga kekerasan tetap konsisten dari lagu ke lagu tanpa tag ReplayGain. **Equalizer 10-band** didesain ulang dengan slider baru, peralihan preset yang lebih cepat, preset kustom yang dapat Anda impor dan ekspor, serta tata letak lanskap dan iPad yang lebih baik. Di balik layar, **mesin streaming AVAudioEngine yang dibangun ulang** meningkatkan keandalan dan dukungan format, termasuk **FLAC** dan **Ogg Vorbis**. **CarPlay** dan **Sedang Diputar** lebih cepat dan lebih akurat di Layar Kunci, di mobil, dan dari remote headphone.

---

## Halo semuanya!

Evermusic 8.7 sudah tersedia untuk diunduh. Pembaruan ini sepenuhnya tentang bagaimana musik Anda *terdengar*. Kami membangun ulang mesin pemutaran untuk pemutaran tanpa jeda yang sesungguhnya, menambahkan rangkaian efek audio kelas studio, memperkenalkan normalisasi kekerasan, dan mendesain ulang equalizer mulai dari slider-nya. Semuanya dibungkus dalam desain **Liquid Glass** baru dari Apple.

[Unduh Evermusic 8.7 dari App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) atau perbarui dari versi Anda yang sudah ada. Evermusic adalah unduhan gratis dengan peningkatan dalam aplikasi opsional.

## Pemutaran Tanpa Jeda Sesungguhnya

Pemutaran tanpa jeda berarti keheningan antara dua lagu hilang. Tanpa jeda, tanpa klik, tanpa bunyi — lagu saat ini mengalir langsung ke lagu berikutnya. Ini paling penting untuk musik yang dirancang untuk didengar sebagai satu kesatuan: **rekaman live, DJ mix, karya klasik, dan album konsep** di mana satu lagu memudar langsung ke lagu lain.

Berikut apa yang berubah secara teknis. Mesin audio Evermusic menjaga dua lagu tetap diputar sekaligus: yang Anda dengar dan yang berikutnya dalam antrean. Saat lagu saat ini diputar, lagu berikutnya sudah **diambil, didekode, dan di-pra-buffer** di latar belakang. Ketika lagu saat ini mencapai akhirnya, mesin berpindah ke lagu berikutnya **di dalam pemutar, bukan di dalam aliran audio**. Loop render output terus menarik sampel audio dari ring buffer berkelanjutan tanpa pernah berhenti, sehingga pendengar tidak pernah mendengar batas. Perpindahan terjadi di antara sampel, yang persis mengapa tidak ada jeda yang terdengar.

Ini bekerja sama saja baik file berada di perangkat Anda, di cloud, atau di server media — pra-buffering hanya dimulai sedikit lebih awal untuk sumber jarak jauh.

## Efek Audio Studio

Evermusic 8.7 menambahkan lima efek audio real-time yang dapat Anda tumpuk di atas musik Anda. Masing-masing berjalan sebagai node pemrosesan audio native di mesin pemutaran, sehingga berlaku untuk semua yang Anda putar — file lokal, streaming cloud, dan radio internet sekaligus — tanpa pengodean ulang.

Setiap efek dilengkapi dengan **pustaka preset yang dikurasi** untuk memberi Anda suara yang hebat dengan satu ketukan, dan Evermusic **mengingat pengaturan persis Anda** antar sesi. Sesuaikan kontrol apa pun dan efek beralih ke keadaan **Manual** sehingga Anda selalu tahu kapan Anda telah menyimpang dari preset.

### Reverb

Menambahkan kesan ruang, dari kamar yang rapat hingga katedral. Dibangun di atas `AVAudioUnitReverb` milik Apple, menawarkan **13 preset ruang** (Kamar Kecil, Aula Sedang, Plate, Katedral, dan lainnya) plus kontrol **mix wet/dry** dari 0 hingga 100% sehingga Anda memutuskan seberapa banyak ruang yang ditambahkan.

### Delay (Gema)

Gema klasik dengan **10 preset** — Slapback, Tape Echo, Dub, Ambient, dan lainnya. Anda dapat mengatur **waktu delay** (hingga 2 detik), **feedback** (berapa banyak pengulangan), **cutoff low-pass** untuk menghangatkan pengulangan, dan **mix wet/dry**.

### Distorsi

Dari tekstur halus hingga penghancuran lo-fi penuh, digerakkan oleh `AVAudioUnitDistortion` dengan **22 preset karakter** (Bit Brush, Cellphone Concert, Radio Tower, dan lainnya), kontrol drive **pre-gain**, dan mix wet/dry sehingga Anda dapat memadukan efek kembali ke sinyal bersih.

### Kompresor

Prosesor dinamika (`AUDynamicsProcessor` milik Apple) yang meratakan bagian keras dan pelan. Ia menampilkan set kontrol profesional lengkap — **ambang, rasio/headroom, attack, release, ekspansi, dan makeup gain** — dengan **10 preset** yang disetel untuk situasi nyata: Suara / Podcast, Larut Malam, Dialog Film, Penyesuaian Streaming, dan Kekerasan Maksimum di antaranya.

### Crossfeed

Crossfeed membuat mendengarkan dengan headphone terdengar lebih alami dengan memadukan sedikit kanal kiri ke kanan dan sebaliknya, seperti cara telinga Anda mendengar speaker sungguhan. Dibangun di atas algoritma **Bauer stereophonic-to-binaural (bs2b)** yang terkenal, dengan kontrol atas **level crossfeed** dan **frekuensi cutoff**, serta **6 preset** termasuk pengaturan favorit audiophile *Chu Moy* dan *Jan Meier*. Ini sangat bagus pada mix stereo lama dengan panning ekstrem dari tahun 1960-an dan 1970-an.

## Normalisasi Volume

Pernah membuat playlist di mana satu lagu menggelegar dan lagu berikutnya berbisik? Normalisasi volume mengatasinya. Evermusic 8.7 menggunakan **pengukuran kekerasan EBU R128** (standar ITU-R BS.1770 yang sama yang digunakan dalam siaran dan oleh layanan streaming) untuk mengukur kekerasan yang benar-benar dirasakan dari setiap lagu dan dengan lembut mengarahkannya menuju target yang konsisten.

Tidak seperti ReplayGain, ia **tidak** memerlukan tag apa pun pada file Anda dan **tidak** memodifikasi audio Anda. Ia bekerja secara real-time pada apa pun yang Anda putar, termasuk streaming cloud dan radio langsung, dan ia mereset dengan bersih saat Anda mencari atau mengganti lagu.

Empat preset mencakup kasus umum:

- **Ringan** — perataan lembut (target −20 LUFS).
- **Standar** — bawaan, kekerasan gaya streaming (target −16 LUFS, hingga +12 dB peningkatan untuk lagu yang pelan).
- **Kuat** — pencocokan agresif untuk pustaka yang sangat beragam (target −14 LUFS).
- **Malam** — lebih pelan dan konsisten untuk mendengarkan malam hari dengan volume rendah (target −23 LUFS).

Anda tidak perlu lagi mengatur volume di antara lagu.

## Equalizer yang Didesain Ulang

**Equalizer grafis 10-band** Evermusic mendapatkan desain ulang penuh. Band mencakup **32 Hz hingga 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), masing-masing dapat disesuaikan dari **−12 dB hingga +12 dB** dalam langkah halus 0,1 dB, dengan **preamp** dari −24 dB hingga +24 dB untuk mencegah clipping saat Anda meningkatkan.

Yang baru di 8.7:

- **Slider baru** — kontrol yang presisi dan responsif yang mengadopsi tampilan slider sistem native iOS 26 dan material **Liquid Glass**.
- **Peralihan preset yang lebih cepat dan mulus** — beralih antar preset seketika, dengan bilah preset horizontal yang didesain ulang dalam mode potret dan kolom preset vertikal dalam mode lanskap.
- **Tata letak yang lebih baik dalam lanskap dan di iPad** — slider dan pemilih preset menata ulang untuk memanfaatkan lebar ekstra alih-alih berdesakan dalam kolom seukuran ponsel.
- **Preset kustom** — buat dan simpan kurva Anda sendiri, atur ulang urutannya, dan **impor serta ekspor** preset sebagai file `.eqp` untuk memindahkannya antar perangkat atau membagikannya.

Equalizer berjalan secara native di mesin (`AVAudioUnitEQ`), sehingga berlaku untuk setiap sumber, dan juga bekerja melalui AirPlay, Chromecast, dan CarPlay jika didukung.

## Mesin Pemutaran yang Dibangun Ulang

Di balik layar, Evermusic 8.7 berjalan pada **mesin streaming yang dibangun ulang** di atas `AVAudioEngine` milik Apple dengan pipeline render kustom. Inilah yang memungkinkan perpindahan tanpa jeda, rantai efek, dan equalizer, dan juga membuat pemutaran sehari-hari lebih andal.

- **Dukungan format yang ditingkatkan** — termasuk **FLAC** (melalui Core Audio) dan **Ogg Vorbis** (melalui `libvorbisfile`), bersama MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF, dan lainnya.
- **Buffering yang lebih cerdas** — pra-buffer adaptif menyesuaikan dengan koneksi Anda, dengan ring buffer berkelanjutan yang memberi makan output sehingga gangguan jaringan singkat tidak berubah menjadi putus-putus.
- **Pemulihan otomatis** — mesin status re-buffering dan logika retry dengan backoff melanjutkan pemutaran dengan bersih setelah momen sinyal lemah alih-alih menghentikan lagu.
- **Lebih sedikit gangguan** — mesin yang sama menggerakkan file lokal, streaming cloud, server media, dan radio internet, sehingga perilaku konsisten di mana-mana.

## Sedang Diputar dan CarPlay

Layar yang benar-benar Anda lihat saat mendengarkan — **Layar Kunci**, **CarPlay**, dan tombol remote mobil atau headphone Anda — lebih akurat dan lebih cepat di 8.7.

- **Info Sedang Diputar yang lebih akurat.** Evermusic menangkap status pemutar di bawah lock sebelum menerbitkannya, sehingga judul, waktu berlalu, durasi, dan status putar/jeda tidak pernah dapat bertentangan satu sama lain di Layar Kunci atau di mobil. Status buffering dan pemuatan kini dilaporkan dengan benar alih-alih menampilkan "diputar" saat lagu masih diambil.
- **Kontrol remote yang andal.** Putar, jeda, berikutnya, sebelumnya, cari, lewati, acak, ulangi, dan kecepatan pemutaran semuanya merespons secara konsisten dari tombol headphone, kontrol mobil, dan Layar Kunci, digerakkan oleh `MPRemoteCommandCenter`.
- **Sampul album CarPlay yang lebih cepat.** Sampul album kini dimuat beberapa kali lebih cepat pada daftar panjang (pengaturan tempo batch dipangkas dari 1,0 dtk menjadi 0,25 dtk, dengan layar pertama yang terlihat dimuat seketika), dan kini muncul di baris daftar CarPlay iOS 26 yang ringkas yang sebelumnya tidak menampilkan sampul.
- **Perbaikan penyortiran dan stabilitas CarPlay.** Penyortiran yang lebih cepat pada pustaka besar dan penguatan terhadap crash kasus tepi saat menggulir daftar panjang.
- **Pembaruan metadata yang dibatasi.** Pembaruan Sedang Diputar dan perintah remote dibatasi sehingga perubahan cepat tidak lagi membanjiri sistem, yang menjaga kontrol layar kunci dan CarPlay tetap responsif.

## Peningkatan Lainnya

- **Penyempurnaan desain Liquid Glass** di seluruh aplikasi — permukaan tembus pandang, animasi yang lebih mulus, dan kontrol yang disempurnakan di iOS, iPadOS, dan macOS.
- **Widget Layar Utama baru** dengan logika pembaruan yang ditingkatkan yang menjaga mereka tetap sinkron tanpa menguras baterai ekstra.
- Perbaikan untuk rilis iOS terbaru.
- Perbaikan lokalisasi di berbagai bahasa.
- Banyak peningkatan kecil berdasarkan email dan ulasan App Store Anda.

## Mengapa Pembaruan Ini Penting

Evermusic 8.7 dibangun di sekitar satu gagasan: **musik Anda harus terdengar sebaik mungkin, di sumber apa pun.**

1. **Album utuh, sebagaimana dimaksudkan.** Pemutaran tanpa jeda yang sesungguhnya berarti set live, DJ mix, dan album konsep akhirnya diputar sebagaimana sang seniman me-master-nya.
2. **Studio di saku Anda.** Reverb, Delay, Distorsi, Kompresor, Crossfeed, equalizer yang didesain ulang, dan normalisasi kekerasan memberi Anda kontrol nyata atas suara Anda, bukan sekadar sakelar hidup/mati.
3. **Pengalaman yang sama di mana-mana.** File lokal, drive cloud, server media, dan radio internet semuanya berjalan melalui mesin yang sama yang dibangun ulang, dengan Sedang Diputar yang akurat dan CarPlay yang lebih cepat di atasnya.

## Dapatkan Evermusic 8.7

[**Unduh Evermusic dari App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) atau perbarui dari dalam App Store. Evermusic adalah unduhan gratis dengan peningkatan dalam aplikasi opsional untuk fitur lanjutan.

Jika Anda menikmati aplikasinya, mohon berikan peringkat di App Store — ini benar-benar membantu. Punya masukan atau mengalami masalah? Email kami di **support@everappz.com**. Kami membaca setiap pesan.

## Pertanyaan yang Sering Diajukan

{{% details title="Apa yang baru di Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 menambahkan pemutaran tanpa jeda yang sesungguhnya, lima efek audio studio (Reverb, Delay, Distorsi, Kompresor, dan Crossfeed), normalisasi volume EBU R128, equalizer 10-band yang didesain ulang dengan preset kustom dan impor/ekspor, mesin streaming AVAudioEngine yang dibangun ulang dengan dukungan format yang ditingkatkan (termasuk FLAC dan Ogg Vorbis), CarPlay dan Sedang Diputar yang lebih cepat dan akurat, pembaruan desain Liquid Glass, widget Layar Utama yang disegarkan, serta perbaikan bug dan lokalisasi.
{{% /details %}}

{{% details title="Apakah Evermusic memiliki pemutaran tanpa jeda yang sesungguhnya?" closed="true" %}}
Ya. Mulai dari Evermusic 8.7, pemutaran benar-benar tanpa jeda: tidak ada jeda, klik, atau bunyi antar lagu. Mesin melakukan pra-buffer dan mendekode lagu berikutnya saat lagu saat ini diputar dan berpindah di antara sampel audio pada ring buffer berkelanjutan, sehingga transisinya tidak terdengar. Ini berfungsi untuk file lokal, streaming cloud, dan server media, dan ideal untuk album live, DJ mix, dan album konsep.
{{% /details %}}

{{% details title="Efek audio apa saja yang disertakan Evermusic 8.7?" closed="true" %}}
Lima efek real-time: **Reverb** (13 preset ruang, mix wet/dry), **Delay/Gema** (10 preset dengan waktu delay, feedback, low-pass, dan mix), **Distorsi** (22 preset karakter dengan pre-gain dan mix), **Kompresor** (prosesor dinamika lengkap dengan ambang, rasio, attack, release, ekspansi, dan makeup gain, plus 10 preset), dan **Crossfeed** (crossfeed headphone Bauer bs2b dengan kontrol level dan cutoff serta 6 preset). Setiap efek dilengkapi dengan preset yang dikurasi, dan pengaturan kustom Anda diingat antar sesi.
{{% /details %}}

{{% details title="Apa itu Crossfeed dan mengapa saya menggunakannya?" closed="true" %}}
Crossfeed memadukan sedikit jumlah yang difilter dari setiap kanal stereo ke kanal lainnya, seperti cara telinga Anda secara alami mendengar speaker sungguhan di ruangan. Pada headphone ini mengurangi pemisahan "di dalam kepala" yang berlebihan dari rekaman dengan panning ekstrem dan membuat mendengarkan lama lebih nyaman. Evermusic menggunakan algoritma Bauer stereophonic-to-binaural (bs2b) yang terkenal dan menyertakan preset seperti Chu Moy dan Jan Meier. Ini sangat efektif pada mix stereo lama dari tahun 1960-an dan 1970-an.
{{% /details %}}

{{% details title="Bagaimana cara kerja normalisasi volume di Evermusic?" closed="true" %}}
Evermusic 8.7 mengukur kekerasan yang dirasakan dari setiap lagu menggunakan standar EBU R128 (ITU-R BS.1770) secara real-time dan dengan lembut menyesuaikan level menuju target yang konsisten sehingga lagu tidak melonjak dalam volume. Ia tidak memerlukan tag ReplayGain dan tidak mengubah file Anda. Tersedia empat preset — Ringan (−20 LUFS), Standar (−16 LUFS), Kuat (−14 LUFS), dan Malam (−23 LUFS) — dan normalisasi mereset dengan bersih saat Anda mencari atau mengganti lagu.
{{% /details %}}

{{% details title="Apakah normalisasi volume Evermusic sama dengan ReplayGain?" closed="true" %}}
Ia mencapai tujuan yang sama — kekerasan yang konsisten antar lagu — tetapi bekerja secara berbeda. ReplayGain bergantung pada tag kekerasan yang disimpan di dalam file Anda. Normalizer Evermusic mengukur kekerasan secara langsung menggunakan EBU R128, sehingga berfungsi pada sumber apa pun, termasuk streaming cloud dan radio internet, bahkan ketika file tidak memiliki tag sama sekali.
{{% /details %}}

{{% details title="Berapa banyak band yang dimiliki equalizer Evermusic, dan bisakah saya membuat preset sendiri?" closed="true" %}}
Equalizer Evermusic adalah equalizer grafis 10-band yang mencakup 32 Hz hingga 16 kHz, dengan setiap band dapat disesuaikan dari −12 dB hingga +12 dB dalam langkah 0,1 dB dan preamp dari −24 dB hingga +24 dB. Ia menyertakan preset bawaan, memungkinkan Anda membuat dan menyimpan preset kustom, dan mendukung impor serta ekspor preset sebagai file .eqp sehingga Anda dapat memindahkan atau membagikannya antar perangkat.
{{% /details %}}

{{% details title="Apa yang berubah pada equalizer Evermusic 8.7?" closed="true" %}}
Equalizer didesain ulang dengan slider baru yang lebih presisi yang mengadopsi tampilan slider sistem iOS 26 dan Liquid Glass, peralihan preset yang lebih cepat dan mulus, serta tata letak yang lebih baik dalam lanskap dan di iPad (bilah preset horizontal dalam potret dan kolom preset vertikal dalam lanskap). Preset kustom dan impor/ekspor .eqp didukung.
{{% /details %}}

{{% details title="Apakah Evermusic 8.7 mendukung FLAC dan Ogg Vorbis?" closed="true" %}}
Ya. Mesin yang dibangun ulang memutar FLAC (melalui Core Audio) dan Ogg Vorbis (melalui libvorbisfile), bersama MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF, dan lainnya, dari file lokal, drive cloud, dan server media.
{{% /details %}}

{{% details title="Apa yang ditingkatkan pada CarPlay dan Layar Kunci?" closed="true" %}}
Sampul album CarPlay dimuat beberapa kali lebih cepat pada daftar panjang dan kini muncul di baris daftar iOS 26 yang ringkas yang sebelumnya tidak menampilkan apa pun. Info Sedang Diputar di Layar Kunci dan di CarPlay lebih akurat — judul, waktu berlalu, durasi, dan status putar/jeda ditangkap bersama sehingga tidak dapat bertentangan, dan status buffering dilaporkan dengan benar. Kontrol remote (putar, jeda, berikutnya, sebelumnya, cari, acak, ulangi, kecepatan) merespons dengan andal dari headphone dan mobil, dan penyortiran CarPlay pada pustaka besar lebih cepat.
{{% /details %}}

{{% details title="Apakah efek audio dan equalizer berfungsi dengan streaming cloud dan CarPlay?" closed="true" %}}
Ya. Efek, equalizer, dan normalisasi volume berjalan secara native di dalam mesin pemutaran, sehingga berlaku untuk semua yang diputar Evermusic — file lokal, drive cloud, server media, dan radio internet — dan terus berfungsi selama pemutaran CarPlay dan, jika didukung, melalui AirPlay dan Chromecast.
{{% /details %}}

{{% details title="Apakah Evermusic 8.7 gratis untuk diperbarui, dan perangkat apa saja yang didukungnya?" closed="true" %}}
Ya. Evermusic adalah unduhan gratis dari App Store, dan 8.7 adalah pembaruan gratis untuk pengguna yang sudah ada, dengan peningkatan dalam aplikasi opsional untuk fitur lanjutan. Ia berjalan di iPhone, iPad, dan Mac. CarPlay memerlukan kendaraan atau head unit yang kompatibel dengan CarPlay.
{{% /details %}}
