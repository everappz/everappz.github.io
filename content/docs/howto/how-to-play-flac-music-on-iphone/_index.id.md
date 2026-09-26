---
title: "Cara Memutar Musik FLAC (Lossless) di iPhone Saya"
date: 2024-01-29
lastmod: 2026-09-26
description: "Cara memutar FLAC di iPhone dan iPad pada tahun 2026 dengan Flacbox, pemutar hi-res dengan 120+ format, output hingga 384 kHz, dukungan USB DAC, equalizer 10 band, mesin audio BASS, efek real-time seperti reverb dan delay, prosesor DSP, dan visualizer musik dengan 500 preset. Streaming dari cloud atau NAS dan putar secara offline."
keywords: ["cara memutar flac di iphone", "pemutar flac iphone", "flac", "iphone", "lossless", "audio hi-res", "pemutar dsd ios", "usb dac iphone", "384khz", "musik", "flacbox", "stream", "offline", "equalizer", "dsp", "visualizer musik", "mesin bass"]
tags: ["musik", "cloud", "pemutar", "pengunduh", "equalizer", "lossless", "hi-res", "offline", "FLAC", "DSD", "DAC", "streamer", "visualizer", "DSP"]
readingTime: 8
---

{{< author-byline >}}


**Ringkasnya:** Untuk memutar FLAC di iPhone, Anda memerlukan pemutar pihak ketiga, karena aplikasi Musik dari Apple tidak mendukung FLAC. Pasang [Flacbox](/products/flacbox) (gratis), lalu transfer file Anda melalui Wi-Fi Drive atau USB, atau hubungkan penyimpanan cloud atau NAS Anda. Koleksi FLAC Anda diputar dalam kualitas penuh, hingga 384 kHz dan 32-bit melalui USB DAC. Flacbox juga memutar lebih dari 120 format, termasuk FLAC, DSD, ALAC, APE, WAV, OGG, dan OPUS, dan menambahkan equalizer 10 band, mesin audio BASS profesional dengan efek real-time, prosesor DSP, dan visualizer musik layar penuh.

[{{< figure src="/docs/howto/how-to-play-flac-music-on-iphone/Flacbox_Icon-App-1024x1024.webp" alt="Flacbox Icon - FLAC music player and downloader" width="160" >}}](/products/flacbox)

## Mengapa iPhone Saya Tidak Memutar FLAC Secara Native?

Apple memiliki format lossless sendiri yang disebut ALAC (Apple Lossless), dan aplikasi Musik dibangun di sekitar itu, bukan FLAC. Sejak iOS 11, aplikasi Files dapat menampilkan pratinjau satu file FLAC, tetapi tidak memiliki pustaka musik, daftar putar, antrean, equalizer, dan streaming cloud. Ini adalah penampil file, bukan pemutar musik.

Jadi Anda memiliki dua pilihan nyata:

1. Putar FLAC dengan aplikasi pemutar, sehingga file Anda tetap persis seperti apa adanya. Inilah yang kami rekomendasikan.
2. Konversikan FLAC ke ALAC, yang merupakan lossless ke lossless, lalu sinkronkan dengan aplikasi Musik.

Jika Anda memiliki koleksi FLAC yang sesungguhnya, pilihan pertama lebih baik. Anda menghindari pustaka ganda, Anda melewati waktu konversi, dan folder serta kualitas hi-res Anda tetap tidak tersentuh. Flacbox dibuat persis untuk ini.

## Opsi 1: Putar FLAC dengan Flacbox

Flacbox adalah pemutar musik hi-res untuk iPhone, iPad, dan Mac. Ia mengubah penyimpanan cloud, NAS, atau komputer Anda menjadi pustaka musik pribadi Anda sendiri, tanpa konversi dan tanpa langganan.

### Langkah 1. Pasang Flacbox

Flacbox dapat diunduh secara gratis dan berjalan di iPhone, iPad, dan Mac.

{{< app-details product="flacbox" >}}

### Langkah 2. Masukkan File FLAC Anda

Pilih cara yang paling mudah bagi Anda:

- **Wi-Fi Drive** — buka Koneksi, lalu Komputer, lalu Menghubungkan menggunakan Wi-Fi, dan seret file dari browser desktop mana pun. Lihat [panduan Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).
- **Penyimpanan cloud** — hubungkan iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive, dan 20 lainnya, lalu streaming langsung dari cloud.
- **NAS atau komputer** — hubungkan melalui SMB, WebDAV, DLNA, FTP, SFTP, atau NFS (Synology, QNAP, WD My Cloud, Time Capsule, atau berbagi Samba apa pun). Daftar lengkapnya ada di [panduan Koneksi](/docs/guide/flacbox/flacbox-guide-connections).
- **Flash drive USB** — colokkan SanDisk iXpand atau pembaca eksternal apa pun dan putar [langsung dari drive](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it), tanpa mengimpor.
- **Berbagi File iTunes atau Finder** — melalui kabel Lightning atau USB-C.

### Langkah 3. Tekan Putar

Lagu-lagu Anda muncul di pustaka dengan tag dan gambar sampul yang dibaca dari file itu sendiri, dikelompokkan menurut Album, Artis, Genre, dan Komposer. Setiap lagu menampilkan codec dan resolusi tepatnya, misalnya FLAC, 96 kHz, 24-bit.

## Output Hi-Res, USB DAC, dan Multi-Channel

Flacbox dibuat untuk orang yang peduli dengan kualitas suara, bukan hanya pemutaran biasa:

- **Sample rate** — memutar dari 8 kHz hingga 384 kHz, dengan output multi-channel dari 1 hingga 7 kanal (hingga 5.1 dan ITU BS.775-1).
- **Dukungan USB DAC** — apa pun di atas 48 kHz diputar pada resolusi aslinya melalui USB DAC. Melalui output bawaan iPhone, iOS melakukan resampling audio seperti yang dilakukannya untuk setiap aplikasi, jadi DAC adalah cara untuk mendapatkan hi-res bit-perfect.
- **Output yang dapat disesuaikan** — atur sample rate, jumlah kanal, dan durasi buffer IO (sekitar 5 ms untuk hi-res latensi rendah) di Pengaturan, lalu Pemutar Audio.
- **Pitch dan kecepatan** — koreksi pitch halus, ditambah kecepatan pemutaran dari 0.02× hingga 3.00×.

## Memutar Lebih dari 120 Format, Bukan Hanya FLAC

Selain FLAC, Flacbox menyertakan FFmpeg sehingga dapat memutar format yang tidak dapat dibuka iOS sendiri. Anda tidak perlu mengonversi atau membersihkan pustaka campuran terlebih dahulu:

- **Lossless dan hi-res** — FLAC, ALAC, WAV, AIFF, APE, WV (WavPack), dan DSD (DSF dan DFF, termasuk DSD64, DSD128, dan DSD256).
- **Lossy** — MP3, AAC, M4A, OGG, OPUS, WMA, MPC, dan lainnya.
- **Musik tracker dan MOD** — file chiptune dan demoscene klasik MOD, XM, IT, S3M, MTM, UMX, dan MO3 yang tidak dapat dibuka oleh sebagian besar pemutar.

Itu totalnya lebih dari 120 format, yang mencakup hampir semua hal dalam koleksi musik modern.

## Tiga Mesin Audio, Termasuk Mesin BASS

Anda dapat memilih mesin pemutaran di Pengaturan, lalu Pemutar Audio, lalu Codec Audio:

- **System Codec + FFmpeg** — kompatibilitas dan stabilitas maksimal.
- **FFmpeg** — memaksa jalur FFmpeg, yang membuka koreksi pitch dan sample rate output kustom.
- **Mesin BASS™** — inti pemutaran profesional yang ditambahkan di [Flacbox 7.6](/blog/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer). Ia membuka efek audio real-time, prosesor DSP, visualizer musik, pemutaran tracker dan MOD, dan resampling berkualitas tinggi. Ia juga menambahkan kontrol pitch independen (±60 semitone) dan kontrol tempo (0.1× hingga 4×).

## Equalizer 10 Band, Bass Boost, dan Preamp

Flacbox menyertakan equalizer grafis 10 band dengan preset bergaya iPod seperti Acoustic, Bass Booster, Rock, Pop, Jazz, Classical, dan Dance. Ada preamplifier untuk mengangkat lagu yang pelan tanpa clipping, dan Anda dapat menyimpan preset Anda sendiri. Setel untuk in-ear monitor, HomePod, atau stereo mobil. Untuk panduan lengkap, lihat [panduan equalizer](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalizer Pemutar Audio Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Efek Audio Real-Time

Ketika mesin BASS aktif, Anda mendapatkan sebelas efek real-time yang dapat Anda tumpuk dan sesuaikan saat musik diputar. Tidak ada yang di-encode ulang, dan mematikan efek akan langsung mengembalikan suara aslinya:

- **Reverb** — dari ruangan kecil hingga katedral.
- **Delay dan echo multi-tap** — dari slapback yang rapat hingga ekor ambient yang panjang.
- **Crossfeed** — memadukan kanal stereo sehingga headphone terdengar lebih seperti speaker sungguhan pada mix yang di-panning ekstrem.
- **Kompresor** — meratakan bagian keras dan pelan, yang bagus untuk mobil atau gym.
- **Chorus, Flanger, Phaser, Auto-Wah, Distortion, dan Stereo Rotation** — efek modulasi kreatif dan karakter.

Flacbox juga memiliki penyeimbangan volume otomatis berdasarkan standar kenyaringan EBU R128 kelas broadcast. Album dan daftar putar acak diputar pada tingkat yang stabil, jadi Anda tidak selalu meraih volume. Ia hadir dengan preset Light, Standard, Strong, dan Night.

## Bangun Prosesor DSP Anda Sendiri

Selain efek, Flacbox memberi Anda prosesor DSP 14 filter real-time yang Anda atur sendiri. Anda dapat menambahkan filter profesional dan band EQ parametrik, saturasi dan bit crusher, serta prosesor kreatif seperti tremolo, ring modulator, dan lebar stereo. Semuanya berjalan secara langsung pada apa pun yang Anda putar, dari FLAC lokal hingga stream cloud, dan pengaturan DSP bahkan tersedia di CarPlay.

## Visualizer Musik Layar Penuh

Flacbox memiliki visualizer musik bawaan yang melukis visual bergerak dan penuh warna seirama dengan musik Anda. Ia menggunakan mesin Milkdrop terkenal (projectM) dengan 500 preset, digambar dengan OpenGL di iPhone, iPad, dan Mac. Buka dari pemutar dengan mengetuk tombol Tindakan Lain lalu Visualisasi. Pilih preset, atau gunakan mode Auto untuk mengacaknya setiap 30 detik dengan crossfade yang mulus. Untuk bantuan langkah demi langkah, lihat panduan tentang [cara mengaktifkan visualizer musik](/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Visualizer Musik Flacbox (Milkdrop dan projectM)" image="/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac/music-visualizer-starfield-sectors-preset.webp" >}}
{{< /cards >}}

## Cloud, NAS, dan Pemutaran Offline

Streaming langsung dari lebih dari 30 layanan cloud, termasuk iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive, dan Internxt. Anda juga dapat menghubungkan server yang di-host sendiri seperti Plex, Jellyfin, Emby, Subsonic, dan Navidrome, dan NAS apa pun melalui SMB, WebDAV, DLNA, FTP, SFTP, atau NFS.

Ketika Anda ingin membawa musik Anda, pengelola unduhan bawaan menyimpan seluruh daftar putar, artis, album, atau folder untuk didengarkan secara offline. Mode Offline kemudian menyinkronkan lagu baru secara otomatis saat muncul di cloud. Kehabisan ruang? Bersihkan cache dengan satu ketukan dan terus streaming.

## Segala Hal Lain yang Diinginkan Pendengar Serius

- **Pustaka yang terorganisir** — dikelompokkan menurut Lagu, Album, Artis Album, Artis, Genre, dan Komposer, dengan pencarian cepat yang berfungsi offline.
- **Editor tag ID3** — perbaiki metadata yang berantakan dan encoding yang rusak (Sirilik, Jepang, Tionghoa) dan tulis perubahan kembali ke file.
- **Daftar putar** — buat, atur ulang, impor dan ekspor M3U, M3U8, dan CUE, dan jadikan tersedia secara offline.
- **Apple CarPlay** — layar dalam mobil khusus untuk pustaka, cloud, musik lokal, dan offline, dengan equalizer di dalamnya.
- **AirPlay 2 dan Chromecast** — cast ke HomePod, Apple TV, dan speaker berkemampuan Cast.
- **Alat audiobook** — beberapa bookmark, kecepatan yang dapat disesuaikan, timer tidur, dan lanjutkan dari tempat Anda berhenti.
- **Widget dan lainnya** — widget Layar Utama dan Layar Kunci, scrobbling Last.fm, lirik berwaktu dan LRC, serta aksesibilitas VoiceOver penuh.

Flacbox gratis untuk diunduh. Premium menghapus batasan versi gratis pada akun cloud, daftar putar, dan folder offline, dan tersedia sebagai pembelian seumur hidup sekali bayar atau langganan bulanan atau tahunan, dengan Berbagi Keluarga.

{{< app-details product="flacbox" >}}

## Opsi 2: Konversikan FLAC ke ALAC untuk Aplikasi Musik

Jika Anda benar-benar menginginkan hasil rip Anda di dalam aplikasi Musik Apple, Anda dapat mengonversinya. FLAC ke ALAC adalah lossless ke lossless, jadi Anda tidak kehilangan kualitas apa pun:

1. Di komputer Anda, konversi secara massal dengan alat gratis seperti XLD di Mac atau foobar2000 di Windows. Keduanya menjaga tag Anda.
2. Tambahkan file ALAC ke pustaka Musik atau iTunes Anda.
3. Sinkronkan ke iPhone dengan Finder di Mac atau aplikasi Apple Devices di Windows.

Kompromisnya nyata. Anda kini menyimpan dua salinan pustaka Anda, setiap pengeditan metadata berarti sinkronisasi lain, dan tata letak aplikasi Musik tetap tidak berubah, tanpa daftar putar berbasis aturan, tanpa equalizer, tanpa DSP, dan tanpa streaming cloud atau NAS di perangkat. Itulah sebabnya sebagian besar orang dengan koleksi FLAC yang serius memilih opsi pertama.

## FAQ

{{% details title="Bisakah iPhone memutar file FLAC secara native?" closed="true" %}}
Hanya secara terbatas. Aplikasi Files dapat menampilkan pratinjau satu file FLAC sejak iOS 11, tetapi tidak ada pustaka, daftar putar, antrean, equalizer, atau streaming cloud. Untuk mendengarkan dengan sungguhan, gunakan aplikasi pemutar seperti Flacbox.
{{% /details %}}

{{% details title="Bisakah saya memutar FLAC 24-bit atau 96kHz (atau lebih tinggi) di iPhone?" closed="true" %}}
Ya. Flacbox mendukung output hi-res hingga 384 kHz. Untuk memutar di atas 48 kHz pada resolusi asli, hubungkan USB DAC eksternal, karena output bawaan iPhone melakukan resampling audio untuk setiap aplikasi.
{{% /details %}}

{{% details title="Apakah Flacbox mengonversi FLAC ke format lain?" closed="true" %}}
Tidak. Flacbox memutar FLAC dalam kualitas lossless aslinya tanpa konversi. Efek dan DSP diterapkan secara langsung selama pemutaran saja, dan tidak pernah mengubah file Anda.
{{% /details %}}

{{% details title="Apakah saya kehilangan kualitas saat mengonversi FLAC ke ALAC?" closed="true" %}}
Tidak. FLAC dan ALAC keduanya lossless, jadi konversinya bit-perfect. Anda hanya menghabiskan waktu dan mengorbankan kenyamanan, karena Anda berakhir dengan dua pustaka yang harus dikelola dan Anda harus menyinkronkan ulang setelah pengeditan.
{{% /details %}}

{{% details title="Format audio apa yang didukung Flacbox?" closed="true" %}}
Lebih dari 120 format, termasuk FLAC, DSD (DSF dan DFF), ALAC, APE, WAV, AIFF, WV, OGG, OPUS, MP3, AAC, M4A, WMA, dan bahkan musik tracker dan MOD seperti MOD, XM, IT, dan S3M.
{{% /details %}}

{{% details title="Apakah Flacbox memiliki equalizer, efek, dan visualizer?" closed="true" %}}
Ya. Ia memiliki equalizer 10 band dengan preset dan preamp. Ia juga memiliki mesin BASS profesional dengan sebelas efek real-time (reverb, delay, echo multi-tap, crossfeed, kompresor, chorus, flanger, phaser, auto-wah, distortion, dan stereo rotation), ditambah penyeimbangan volume EBU R128, prosesor DSP 14 filter, dan visualizer Milkdrop layar penuh dengan 500 preset.
{{% /details %}}

{{% details title="Bisakah saya streaming FLAC dari NAS atau cloud saya?" closed="true" %}}
Ya. Flacbox terhubung ke lebih dari 30 layanan cloud dan ke NAS atau komputer melalui SMB, WebDAV, DLNA, FTP, SFTP, dan NFS. Seluruh pustaka Anda tersedia tanpa menyalin file ke iPhone Anda, dan Anda dapat mengunduh lagu untuk pemutaran offline kapan saja.
{{% /details %}}

{{% details title="Apakah Flacbox benar-benar gratis?" closed="true" %}}
Flacbox gratis untuk diunduh, dengan fitur inti seperti equalizer, streaming cloud, dan pemutaran offline. Premium menghapus batasan versi gratis pada akun cloud, daftar putar, dan folder offline, dan hadir sebagai pembelian seumur hidup sekali bayar atau langganan bulanan atau tahunan, dengan Berbagi Keluarga.
{{% /details %}}
