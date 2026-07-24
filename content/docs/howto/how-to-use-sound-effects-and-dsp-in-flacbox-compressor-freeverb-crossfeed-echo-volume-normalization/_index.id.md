---
title: "Cara Menggunakan Efek Suara dan DSP di Flacbox: Compressor, Freeverb, Crossfeed, Echo, Normalisasi Volume, dan lainnya (Setiap Preset dan Pengaturan Dijelaskan)"
date: 2026-07-24
description: "Panduan lengkap audio Flacbox di iPhone, iPad, dan Mac. Pelajari cara kerja engine BASS, format tambahan apa saja yang bisa diputar (termasuk musik MOD dan tracker serta DSD), dan apa persisnya yang dilakukan setiap efek, setiap slider, dan setiap preset terhadap suara Anda, ditambah equalizer 10 band dan rantai DSP kustom."
keywords: ["efek audio Flacbox", "preset Flacbox dijelaskan", "engine BASS Flacbox", "pustaka audio BASS iOS", "pemutar musik MOD iPhone", "pemutar musik tracker iOS", "putar MOD XM IT S3M iPhone", "pemutar DSD iOS", "pemutar FLAC iPhone", "pemutar musik lossless iOS", "preset equalizer Flacbox", "equalizer 10 band iPhone", "normalisasi volume iPhone", "EBU R128 iOS", "normalisasi kenyaringan pemutar musik", "crossfeed headphone iOS", "bs2b crossfeed", "preset compressor pemutar musik", "reverb freeverb iOS", "echo delay pemutar musik", "rantai DSP pemutar musik", "bass boost iPhone", "cara menambahkan efek ke musik Flacbox", "pengaturan equalizer terbaik iPhone"]
tags: ["Flacbox", "Efek Audio", "Cara", "BASS", "Equalizer", "Bass Boost", "Compressor", "Freeverb", "Crossfeed", "Echo", "Normalisasi Volume", "EBU R128", "Musik MOD", "Musik Tracker", "DSD", "FLAC", "DSP", "Headphone", "Preset"]
readingTime: 30
---

{{< author-byline >}}

**Jawaban singkat:** Di Flacbox Anda memilih satu **Playback engine** di **Pengaturan > Audio player**: **Standard** (engine sistem Apple), **Universal** (engine FFmpeg), atau **Sound FX** (**engine BASS™**). Engine yang Anda pilih menentukan format file mana yang dapat diputar, jadi pilihan ini penting. Engine **Sound FX** memutar format tambahan yang dilewati sebagian besar aplikasi iPhone (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, dan musik **MOD dan tracker** lama seperti MOD, XM, IT, dan S3M), dan ini adalah satu-satunya engine yang menjalankan alat suara: **equalizer 10 band**, **Normalisasi Volume**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed**, dan **rantai DSP** bikinan sendiri. Jadi untuk menggunakan efek dalam panduan ini, atur Playback engine Anda ke **Sound FX** terlebih dahulu. Setiap alat memiliki **preset** siap pakai. Buka mereka di **Pengaturan > Audio player** (Audio effects, Audio equalizer, Signal processing), atau ketuk tombol **⋯ (More)** pada pemutar dan pilih **Audio effects**. Apa pun yang Anda lakukan di sini tidak pernah mengubah file Anda.

> Penjelasan slider dan preset di bawah ini adalah deskripsi singkat yang sama yang ditampilkan Flacbox kepada Anda di dalam aplikasi, dipadukan dengan sedikit latar belakang tambahan agar Anda mendapatkan gambaran utuh sebelum mengetuk.

## Cara Membaca Panduan Ini

Setiap alat bekerja dengan cara yang sama:

1. **Nyalakan.** Setiap efek memiliki sakelar hidup/mati sendiri. Semuanya mati pada awalnya. Anda dapat menyalakan sebanyak yang Anda mau secara bersamaan.
2. **Pilih preset.** Preset adalah pengaturan siap pakai. Ketuk satu dan suara langsung berubah. Panduan ini mencantumkan apa yang dilakukan **setiap** preset.
3. **Sesuaikan halus (opsional).** Buka slider untuk menyesuaikan secara manual. Begitu Anda menggeser slider, efek menampilkan **Manual**, sehingga Anda tahu Anda telah meninggalkan preset. Setiap slider memiliki tombol reset.

Tidak ada yang disimpan ke dalam file Anda. Ini adalah efek langsung. Matikan efek dan suara asli Anda langsung kembali.

## Pilih Playback Engine Anda (Sound FX Memiliki Efek)

Flacbox tidak mencampur engine bersama-sama. Anda memilih **satu** di **Pengaturan > Audio player > Playback engine**, dan engine yang Anda pilih menentukan format file mana yang dapat Anda putar dan apakah efek tersedia. Ada tiga pilihan, ditampilkan di aplikasi dengan nama persis ini:

1. **Standard.** Engine sistem bawaan Apple. Menggunakan dekode perangkat keras untuk penggunaan baterai yang lebih rendah.
2. **Universal.** Engine FFmpeg, yang membuka rentang format yang sangat luas.
3. **Sound FX.** **Engine BASS™**. Ini memutar file lossless dan resolusi tinggi dengan akurasi penuh, menambahkan musik modul (tracker), dan menjalankan setiap efek, equalizer 10 band, dan rantai DSP dalam panduan ini.

Karena setiap engine mendukung set formatnya sendiri, file yang dapat Anda putar berubah sesuai engine yang Anda pilih. Yang lebih penting, efek, equalizer, dan rantai DSP bekerja **hanya** dengan engine **Sound FX**, jadi pilih itu terlebih dahulu jika Anda ingin menggunakannya.

Sound FX dibangun di atas **BASS™**, pustaka audio profesional dari Un4seen Developments. Anda dapat membaca lebih lanjut di halaman utamanya di [un4seen.com](https://www.un4seen.com/).

## Format Musik: Apa yang Ditambahkan Engine Sound FX (BASS™) (Termasuk Musik MOD dan Tracker)

Dengan engine **Sound FX (BASS™)** dipilih, Flacbox memutar format spesialis di bawah ini, di atas format sehari-hari. Yang paling istimewa adalah **musik modul**, juga disebut **musik tracker**. File modul bukanlah rekaman biasa. Ia menyimpan suara instrumen kecil ditambah sebuah "partitur" yang menyatakan cara memainkannya, dan Flacbox membangun ulang lagu secara langsung dari partitur itu, sebagaimana file-file ini dimaksudkan untuk dimainkan. Pemutar biasa tidak dapat melakukan ini.

| Jenis musik | Format | Perlu diketahui |
|---|---|---|
| **Musik modul / tracker** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Dibangun ulang secara langsung oleh pemutar modul BASS™. Bagus untuk chiptune dan lagu demoscene atau Amiga lama. |
| **Lossless modern** | FLAC | Kualitas penuh, lebih kecil dari WAV. |
| **Lossless lainnya** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Jenis lossless yang kurang umum, semuanya didukung. |
| **DSD resolusi tinggi** | DSF, DFF | Diputar pada perangkat keras biasa menggunakan DSD over PCM. |
| **Lossy modern** | Opus, Ogg Vorbis, MP3 | Jenis streaming dan unduhan yang biasa. |

Engine Sound FX juga memutar format arus utama Apple (AAC, ALAC, M4A, WAV, AIFF) dan streaming langsung, jadi efek dan equalizer bekerja pada format itu juga.

**Mengapa ini membantu Anda:** jika Anda memiliki campuran album FLAC, file DSD resolusi tinggi, dan folder lagu tracker MOD atau XM lama, Flacbox memutar semuanya, dan equalizer serta efek bekerja pada setiap satunya.

## Tiga Menu yang Akan Anda Gunakan

Flacbox menyimpan alat suaranya di tiga tempat, semuanya di dalam pengaturan audio player. Pertama pastikan **Playback engine** Anda diatur ke **Sound FX** (Pengaturan > Audio player > Playback engine), karena efek, equalizer, dan rantai DSP tersedia hanya dengan engine tersebut.

- **Audio effects** (rak efek): buka pemutar, ketuk **⋯ (More)**, ketuk **Audio effects**. Atau buka **Pengaturan > Audio player > Audio effects**.
- **Audio equalizer** (10 band dan preset): **Pengaturan > Audio player > Audio equalizer**.
- **Signal processing** (rantai DSP Anda sendiri): **Pengaturan > Audio player > Signal processing**.

Anda juga dapat mengatur **output sample rate**, **channels**, dan **buffer size** di **Pengaturan > Audio player**.

## Equalizer 10 Band

**Apa yang dilakukannya:** Mengubah nada musik, dari bass dalam hingga treble cerah. Ini adalah alat terbaik untuk **bass boost** yang bersih atau ujung atas yang lebih cerah dan lebih jernih. Anggap saja sebagai sepuluh kenop volume, masing-masing untuk irisan suara yang berbeda. Naikkan band untuk membawa bagian itu ke depan, turunkan untuk menariknya kembali. Perubahan kecil beberapa dB biasanya terdengar paling baik, dan ini bekerja pada semua yang Anda putar.

**Cara kerjanya:** Sepuluh slider pada **32, 64, 125, 250, 500 Hz dan 1, 2, 4, 8, 16 kHz**. Masing-masing berkisar dari **-12 dB (cut)** hingga **+12 dB (boost)**. Ada juga **Preamplifier** dari **-24 hingga +24 dB** untuk level keseluruhan. Anda dapat menyimpan preset Anda sendiri dan **mengekspor atau mengimpornya** antar perangkat.

**Apa yang dilakukan setiap preset bawaan (22 preset):**

| Preset | Apa yang dilakukannya terhadap suara Anda |
|---|---|
| **Flat** | Tidak ada perubahan. Semua band pada nol. Titik awal yang bersih. |
| **Acoustic** | Bass hangat dan highs yang renyah serta hadir. Membuat gitar akustik dan suara terasa alami dan hidup. |
| **Bass Booster** | Angkatan kuat di low end, mid dan high tak tersentuh. Lebih banyak punch dan bobot. |
| **Bass Reducer** | Memotong low end. Berguna untuk ruangan yang menggema, earbud murah, atau lagu yang berat. |
| **Treble Booster** | Mengangkat hanya highs. Menambahkan kilau dan udara, lebih banyak detail. |
| **Treble Reducer** | Melembutkan highs. Menjinakkan rekaman yang kasar atau tajam. |
| **Classical** | Low penuh dan high lembut dengan sedikit penurunan mid. Halus dan lapang untuk musik orkestra. |
| **Dance** | Low besar dan high cerah dengan mid yang dikeruk. Punchy dan energik untuk lagu klub. |
| **Deep** | Low end hangat dan tebal dengan high lebih lembut. Suara yang nyaman dan santai. |
| **Electronic** | Bass kuat dan high cerah untuk synth dan beat. Lebar dan modern. |
| **Hip-Hop** | Bass berat dan high jernih dengan mid terkendali. Berbobot dan punchy. |
| **Jazz** | Hangat dan halus, dengan sedikit penurunan mid. Mudah dan alami untuk jazz akustik. |
| **Latin** | Low dan high yang ditingkatkan dengan mid yang bersih. Cerah dan hidup. |
| **Loudness** | Menaikkan bass dan treble dengan kuat (kurva "senyum"). Terdengar lebih penuh pada volume rendah. |
| **Lounge** | Mid yang menonjol dengan tepi lembut. Santai dan ramah vokal. |
| **Piano** | Mid dan high jernih sehingga nada piano berbunyi dengan bersih. |
| **Pop** | Mid yang diangkat untuk vokal, dengan low dan high ditarik kembali. Suara duduk di depan. |
| **R&B** | Kehangatan low-mid yang sangat kuat dan high yang jernih. Halus dan kaya. |
| **Rock** | Low dan high yang ditingkatkan untuk gitar dan drum. Energik dan penuh. |
| **Small Speakers** | Menaikkan low dan memotong high untuk membantu speaker kecil terdengar lebih penuh. |
| **Spoken Word** | Mengangkat rentang suara dan memotong bass dalam. Membuat pembicaraan jelas. |
| **Vocal Booster** | Mendorong bagian tengah tempat suara berada, memotong di sekitarnya. Vokal menonjol. |

**Tips untuk bass:** Mulai dengan **Bass Booster**, lalu, jika terdengar keruh, turunkan Preamplifier 1 hingga 2 dB sehingga tidak ada yang terdistorsi.

## Normalisasi Volume (Kenyaringan Merata)

**Apa yang dilakukannya:** Beberapa lagu diputar lebih keras dari yang lain, jadi Anda terus mengubah volume. Ini membuat setiap lagu diputar pada volume yang kira-kira sama dengan sendirinya, sehingga Anda tidak perlu. Ini sempurna untuk daftar putar acak yang mencampur rekaman lama dan baru, album berbeda, atau sumber berbeda, di mana satu track bisa jauh lebih keras dari yang berikutnya.

**Cara kerjanya:** Ia mendengarkan kenyaringan sebenarnya dari setiap track menggunakan standar **EBU R128** (diukur dalam **LUFS**, ide yang sama yang digunakan layanan streaming), lalu menyesuaikan setiap track menuju target Anda. Ia tidak memerlukan tag dalam file Anda dan tidak pernah mengubah audio. EBU R128 mengukur kenyaringan yang benar-benar dirasakan telinga Anda di seluruh lagu, bukan hanya puncak tertinggi, itulah mengapa ia cocok dengan seberapa keras track benar-benar terdengar bagi Anda. Flacbox menghitung ini secara langsung saat musik diputar (dan memeriksa kenyaringan lebih awal bila memungkinkan), lalu menerapkan satu perubahan volume yang stabil ke track. Batas **Max boost** menghentikan rekaman yang sangat pelan agar tidak didorong naik begitu keras hingga terdistorsi. Karena ia membaca suara itu sendiri, ia bekerja pada sumber apa pun, termasuk file cloud, streaming langsung, dan musik modul, bahkan ketika file sama sekali tidak memiliki tag kenyaringan.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Target loudness** | Mengatur kenyaringan yang menjadi target perataan setiap track. Nilai lebih tinggi membuat semuanya diputar lebih keras secara keseluruhan. | -30 hingga -6 LUFS (-16) |
| **Max boost** | Membatasi seberapa banyak track pelan dapat diperkuat. Nilai lebih tinggi membawa rekaman lembut lebih dekat ke target. | 0 hingga 24 dB (12) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Light** | Perataan lembut untuk mendengarkan santai. Meratakan lonjakan volume yang jelas tanpa mendorong track pelan dengan keras. |
| **Standard** | Default serbaguna. Target kenyaringan gaya streaming yang cocok untuk sebagian besar musik. Mulai di sini. |
| **Strong** | Pencocokan agresif yang mendorong track pelan naik dengan tegas. Terbaik untuk pustaka campuran dengan perbedaan level besar. |
| **Night** | Target keseluruhan yang lebih pelan yang tetap mengangkat bagian lembut, sehingga mendengarkan larut malam tetap konsisten dan rendah. |

## Compressor (Meratakan Bagian Keras dan Pelan)

**Apa yang dilakukannya:** Dalam satu lagu, bagian pelan bisa terlalu lembut dan bagian keras terlalu keras. Ini membawa mereka lebih dekat bersama, sehingga seluruh lagu mudah didengar, bahkan di mobil atau tempat berisik. Ia dengan lembut menurunkan momen paling keras dan mengangkat yang lebih lembut, sehingga Anda berhenti meraih volume selama satu track. Ini berbeda dari Normalisasi Volume: Compressor meratakan **di dalam** satu lagu, sedangkan Normalisasi Volume mencocokkan kenyaringan **antar** lagu. Keduanya bekerja baik bersama-sama. Mulai dengan preset, dan buka slider hanya jika Anda ingin lebih banyak kontrol.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Threshold** | Level tempat kompresi dimulai. Nilai lebih rendah menekan lebih banyak suara, menjaga bagian pelan dan keras lebih dekat bersama. | -60 hingga 0 dB (-20) |
| **Ratio** | Seberapa kuat bagian keras ditahan setelah melewati threshold. Nilai lebih tinggi mengompresi lebih keras, menjaga suara lebih merata. | 1:1 hingga 30:1 (4:1) |
| **Attack** | Seberapa cepat efek merespons puncak keras mendadak. Nilai pendek menangkap transien; nilai lebih panjang membiarkannya lewat. | 0.1 hingga 1000 ms (10 ms) |
| **Release** | Seberapa cepat efek melepas setelah bagian keras berlalu. Nilai pendek dapat memompa; nilai lebih panjang terdengar lebih halus. | 10 ms hingga 5 s (100 ms) |
| **Master gain** | Peningkatan output akhir yang diterapkan setelah pemrosesan. Naikkan ini untuk mengangkat kenyaringan keseluruhan setelah dinamika diratakan. | -30 hingga +30 dB (0) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Transparent** | Jaring pengaman yang nyaris tak terasa. Mempertahankan dinamika hampir sepenuhnya dan hanya menangkap puncak paling keras. |
| **Soft** | Perataan ringan untuk mendengarkan hi-fi di rumah. Penghalusan halus tanpa menekan musik. |
| **Standard** | Default masuk akal untuk pemutaran musik sehari-hari. Preset pertama yang dicoba. |
| **Heavy** | Perataan agresif untuk lingkungan berisik. Mobil, ruangan ramai, mendengarkan volume rendah. |
| **Voice / Podcast** | Disetel untuk ucapan. Attack lebih lambat membiarkan sibilan lewat, makeup gain murah hati menarik vokal naik. |
| **Old Recordings** | Album vintage dan vinyl yang dipulihkan, di mana level rata-rata di bawah rilis modern. |
| **Late Night** | Kompresi berat ditambah boost besar untuk mendengarkan pelan saat tetangga atau keluarga yang tidur menjadi perhatian. |
| **Movie Dialog** | Membawa kata-kata yang diucapkan naik melawan musik dan efek suara dalam soundtrack yang bervariasi. |
| **Streaming Match** | Menargetkan kira-kira normalisasi kenyaringan layanan streaming modern sekitar -14 LUFS. |
| **Maximum Loudness** | All-in. Mencapai limiter; harapkan sinyal yang tertekan dan sangat merata. Preset volume-maksimum harfiah. |

## Freeverb (Reverb, Rasa Ruang)

**Apa yang dilakukannya:** Menambahkan rasa ruang ke musik, dari ruangan kecil hingga aula besar. Pilih preset, atau sesuaikan sendiri campuran dry dan wet, ukuran ruangan, damping, dan lebar. Reverb adalah gema alami yang Anda dengar di ruang nyata mana pun, dan Freeverb menciptakannya kembali dalam perangkat lunak. Sedikit membuat rekaman datar atau close-mic terasa lebih terbuka dan hidup. Banyak menempatkan musik di ruang yang besar dan jauh. Ini adalah efek kreatif, jadi jaga campuran wet tetap sederhana untuk hasil alami.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Dry mix** | Seberapa banyak suara asli yang tak tersentuh dipertahankan. Nilai lebih tinggi meninggalkan lebih banyak sinyal dry dalam campuran. | 0 hingga 1 (0.0) |
| **Wet mix** | Seberapa banyak suara bergema ditambahkan. Nilai lebih tinggi membuat reverb lebih keras dan lebih jelas. | 0 hingga 3 (1.0) |
| **Room size** | Ukuran ruang yang dibayangkan. Nilai lebih tinggi memberikan ekor reverb yang lebih panjang dan lebih besar, dari ruangan kecil hingga katedral. | 0 hingga 1 (0.5) |
| **Damp** | Seberapa cepat frekuensi tinggi memudar dalam ekor. Nilai lebih tinggi membuat reverb lebih gelap dan lebih hangat. | 0 hingga 1 (0.5) |
| **Width** | Sebaran stereo dari reverb. Nilai lebih tinggi membuat ruang terasa lebih lebar antara channel kiri dan kanan. | 0 hingga 1 (1.0) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Room** | Ruang kecil dan rapat. Ambience halus yang menambahkan rasa tempat tanpa menghapus suara. |
| **Studio** | Ruang rekaman yang kering dan terkendali. Cukup pantulan agar terdengar alami. |
| **Hall** | Aula konser besar. Ekor yang panjang dan subur yang cocok untuk musik orkestra dan akustik. |
| **Cathedral** | Ruang batu yang besar dan menggema. Ekor reverb yang paling panjang dan paling dramatis. |
| **Plate** | Plate reverb studio yang cerah dan padat. Klasik untuk vokal dan drum. |
| **Ambience** | Ambience yang pendek dan lapang. Menambahkan sedikit rasa ruang sambil tetap sebagian besar kering. |

## Auto Wah (Sapuan Filter Funky)

**Apa yang dilakukannya:** Filter yang menyapu naik dan turun dengan sendirinya untuk suara wah yang funky dan mirip vokal. Pilih preset, atau atur sendiri campuran wet, feedback, rate, range, dan frekuensi. Ini adalah sapuan "wah" yang sama yang dibuat pedal wah gitar, tetapi di sini ia bergerak dengan sendirinya seiring musik. Ini terdengar bagus pada lagu funk, disko, dan elektronik. Ini efek yang berani dan jelas, jadi sedikit sudah sangat berarti untuk mendengarkan sehari-hari.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Wet mix** | Seberapa kuat efek wah dalam campuran. Nilai lebih tinggi membuat filter menyapu lebih jelas. | -2 hingga +2 (1.5) |
| **Feedback** | Seberapa banyak output diumpankan kembali ke efek. Nilai lebih tinggi membuat wah lebih resonan dan menonjol. | -1 hingga +1 (0.5) |
| **Rate** | Seberapa cepat filter menyapu naik dan turun. Nilai lebih tinggi memberikan wah yang lebih cepat dan lebih ritmis. | 0.1 hingga 9 Hz (2.0) |
| **Range** | Seberapa jauh filter menyapu, dalam oktaf. Nilai lebih tinggi memberikan sapuan yang lebih lebar dan lebih dramatis. | 0.1 hingga 9 oktaf (4.3) |
| **Frequency** | Frekuensi dasar tempat filter menyapu. Nilai lebih rendah terdengar lebih dalam; nilai lebih tinggi terdengar lebih cerah. | 1 hingga 1000 Hz (50) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Classic** | Sapuan wah klasik yang seimbang. Titik awal yang baik untuk funk dan rock. |
| **Slow** | Sapuan lambat dan lebar yang melayang lembut naik dan turun. Bagus untuk pad dan nada panjang. |
| **Funky** | Sapuan cepat dan punchy dengan banyak gerakan. Menambahkan gigitan ritmis pada gitar dan synth. |
| **Deep** | Sapuan dalam dan lebar dimulai dari frekuensi rendah. Besar dan dramatis. |
| **Subtle** | Gerakan lembut dan tak mencolok. Menambahkan karakter tanpa mendominasi suara. |
| **Resonant** | Wah yang tajam dan resonan dengan feedback tinggi. Mirip vokal dan ekspresif. |

## Phaser (Whoosh Berputar)

**Apa yang dilakukannya:** Filter menyapu yang menambahkan gerakan berputar dan berdesir pada suara. Pilih preset, atau atur sendiri feedback, rate, range, dan frekuensi. Ini menambahkan gerakan lembut dan kilau tanpa mengubah nada. Ini halus pada vokal dan pad, dan dramatis pada synth dan gitar. Coba Slow untuk nuansa penuh mimpi atau Jet untuk putaran yang kuat.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Feedback** | Seberapa banyak output diumpankan kembali ke efek. Nilai lebih tinggi membuat phaser lebih resonan dan menonjol. | -1 hingga +1 (0.0) |
| **Rate** | Seberapa cepat filter menyapu naik dan turun. Nilai lebih tinggi memberikan phasing yang lebih cepat dan lebih ritmis. | 0.1 hingga 9 Hz (1.0) |
| **Range** | Seberapa jauh filter menyapu, dalam oktaf. Nilai lebih tinggi memberikan sapuan yang lebih lebar dan lebih dramatis. | 0.1 hingga 9 oktaf (4.0) |
| **Frequency** | Frekuensi dasar tempat filter menyapu. Nilai lebih rendah terdengar lebih dalam; nilai lebih tinggi terdengar lebih cerah. | 1 hingga 1000 Hz (100) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Classic** | Sapuan phaser klasik yang seimbang. Titik awal yang baik untuk gitar dan keyboard. |
| **Slow** | Sapuan lambat dan lebar yang melayang lembut naik dan turun. Bagus untuk pad dan nada panjang. |
| **Fast** | Sapuan cepat dan berkilau dengan banyak gerakan. Menambahkan gerakan dan energi. |
| **Deep** | Sapuan dalam dan lebar dimulai dari frekuensi rendah. Besar dan dramatis. |
| **Subtle** | Gerakan lembut dan tak mencolok. Menambahkan karakter tanpa mendominasi suara. |
| **Jet** | Sapuan intens dan resonan dengan feedback tinggi, whoosh pesawat jet klasik. |

## Flanger (Sapuan Pesawat Jet)

**Apa yang dilakukannya:** Delay pendek yang bergerak yang memberikan suara whoosh menyapu seperti jet. Pilih preset, atau atur sendiri depth, feedback, rate, dan delay. Ini adalah sepupu yang lebih kuat dan lebih metalik dari phaser, terkenal dengan sapuan berdesir dalam rock klasik dan musik elektronik. Pengaturan halus menambahkan gerakan lembut, sedangkan pengaturan dalam bersifat dramatis dan jelas. Paling baik digunakan hemat, untuk efek.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Depth** | Seberapa kuat efek menyapu. Nilai lebih tinggi membuat flanging lebih jelas. | 0 hingga 100% (25) |
| **Feedback** | Seberapa banyak output diumpankan kembali ke efek. Nilai lebih tinggi membuat flanger lebih resonan dan metalik. | -99 hingga +99% (-50) |
| **Rate** | Seberapa cepat sapuan bergerak naik dan turun. Nilai lebih tinggi memberikan gerakan yang lebih cepat dan lebih berkilau. | 0 hingga 10 Hz (0.25) |
| **Delay** | Waktu delay dasar tempat sapuan dibangun. Nilai lebih tinggi memberikan karakter yang lebih dalam dan lebih berongga. | 0 hingga 4 ms (2.0) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Classic** | Flanger klasik yang seimbang. Titik awal yang baik untuk gitar dan keyboard. |
| **Subtle** | Sapuan lembut dan tak mencolok. Menambahkan gerakan tanpa mendominasi suara. |
| **Deep** | Sapuan dalam dan berat dengan feedback kuat. Besar dan dramatis. |
| **Jet** | Sapuan intens dengan feedback positif, whoosh pesawat jet klasik. |
| **Fast** | Sapuan cepat dan berkilau dengan banyak gerakan dan energi. |
| **Wide** | Sapuan lambat dan lebar dengan delay panjang. Subur dan lapang. |

## Echo (Pengulangan)

**Apa yang dilakukannya:** Mengulang suara sebagai gema yang memudar untuk rasa ruang dan kedalaman. Pilih preset, atau atur sendiri campuran wet, feedback, dan delay. Ini seperti berteriak di ngarai: suara kembali satu kali atau lebih setelah jeda singkat. Satu pengulangan pendek menambahkan tubuh dan nuansa retro, sedangkan pengulangan lebih panjang dengan lebih banyak feedback menciptakan ekor yang lapang dan menjuntai. Preset Ping Pong memantulkan pengulangan antara telinga kiri dan kanan Anda, yang menyenangkan pada headphone. Jaga campuran wet tetap sederhana sehingga gema mendukung musik daripada menutupinya.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Wet mix** | Seberapa keras gema dibandingkan dengan suara asli. Nilai lebih tinggi membuat pengulangan lebih menonjol. | -2 hingga +2 (0.6) |
| **Feedback** | Berapa kali gema mengulang. Nilai lebih tinggi memberikan lebih banyak pengulangan yang lebih lama memudar. | -1 hingga +1 (0.5) |
| **Delay** | Waktu antara gema. Nilai lebih pendek memberikan slap-back yang rapat; nilai lebih panjang memberikan pengulangan yang berjarak. | 0.01 hingga 2 s (0.4) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Slapback** | Satu pengulangan rapat tepat di belakang suara. Slap-back rockabilly klasik. |
| **Room** | Gema pendek dan alami, seperti ruangan kecil. Menambahkan ruang tanpa mengaburkan suara. |
| **Tape** | Pengulangan sedang yang hangat yang memudar bertahap, seperti tape delay lama. |
| **Dub** | Pengulangan panjang dan berat dengan feedback kuat. Besar, dubby, dan lapang. |
| **Ping Pong** | Gema memantul antara speaker kiri dan kanan untuk efek stereo yang lebar. |
| **Long** | Pengulangan lambat dan berjarak lebar yang menjuntai jauh di belakang suara. |

## Chorus (Suara Lebih Tebal, Lebih Lebar)

**Apa yang dilakukannya:** Menebalkan dan melebarkan suara dengan melapisi salinan bergeser di atas aslinya. Pilih preset, atau atur sendiri campuran wet/dry, depth, rate, dan feedback. Ini membuat satu instrumen atau suara terdengar seperti beberapa yang dimainkan bersama, dengan menambahkan salinan yang sedikit detuned dan bergerak. Ini menambahkan kekayaan dan kilau lembut. Pengaturan halus menghangatkan, sedangkan pengaturan kuat terdengar subur dan penuh mimpi. Ini populer pada gitar, keyboard, dan vokal.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Wet/Dry** | Seberapa banyak chorus yang Anda dengar dibandingkan dengan suara asli. Nilai lebih tinggi membuat efek lebih jelas. | 0 hingga 100% (50) |
| **Depth** | Seberapa jauh pitch bergetar naik dan turun. Nilai lebih tinggi memberikan suara yang lebih tebal dan lebih berkilau. | 0 hingga 100% (25) |
| **Rate** | Seberapa cepat kilau bergerak. Rate lebih lambat terdengar lembut dan subur; rate lebih cepat terdengar lebih seperti vibrato. | 0 hingga 10 Hz (1.1) |
| **Feedback** | Seberapa banyak efek diumpankan kembali ke dirinya sendiri. Nilai lebih tinggi membuat chorus lebih resonan dan intens. | -99 hingga +99% (25) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Subtle** | Penebalan lembut yang menambahkan kehangatan tanpa menarik perhatian pada dirinya sendiri. |
| **Lush** | Chorus klasik yang kaya. Pengaturan serba guna yang bagus untuk gitar dan keyboard. |
| **Ensemble** | Kilau berlapis penuh yang membuat satu instrumen terdengar seperti beberapa. |
| **Vibrato** | Sepenuhnya wet dengan rate cepat, untuk vibrato bergoyang alih-alih chorus halus. |
| **Wide** | Kilau lambat dan lebar yang membuka citra stereo. Lapang dan penuh mimpi. |
| **Twelve-String** | Kilau cerah dan resonan yang mengingatkan pada gitar dua belas senar. |

## Distortion (Kekasaran dan Ketajaman)

**Apa yang dilakukannya:** Menambahkan kekasaran dan ketajaman dengan meng-overdrive suara. Pilih preset, atau atur sendiri drive, output, dan tone. Ini secara sengaja mengasarkan suara, dari tepi kasar yang hangat hingga nada pecah dan berbulu. Ini adalah efek kreatif untuk bersenang-senang daripada cara meningkatkan kualitas, jadi gunakan dalam jumlah kecil. Ini menyenangkan pada lagu elektronik, rock, dan eksperimental. Turunkan Output jika preset berat menjadi terlalu keras.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Drive** | Seberapa keras suara didistorsi. Nilai lebih tinggi lebih kasar dan lebih agresif. | 0 hingga 100% (15) |
| **Output** | Level output setelah distorsi. Turunkan jika pengaturan berat menjadi terlalu keras. | -60 hingga 0 dB (-18) |
| **Tone** | Menggulung highs sebelum distorsi. Nilai lebih rendah terdengar lebih gelap dan lebih hangat. | 100 hingga 8000 Hz (8000) |
| **Center** | Frekuensi mana distorsi difokuskan. Menggeser karakter lebih cerah atau lebih gelap. | 100 hingga 8000 Hz (2400) |
| **Width** | Seberapa lebar fokus itu. Sempit terdengar tajam dan sengau; lebar terdengar penuh dan terbuka. | 100 hingga 8000 Hz (2400) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Warm Drive** | Kekasaran ringan dan hangat yang menambahkan tepi tanpa banyak mengubah karakter. |
| **Crunch** | Overdrive renyah klasik, punchy dan ritmis. |
| **Overdrive** | Nada cerah dan bertenaga dengan banyak gigitan. Bagus untuk suara lead. |
| **Fuzz** | Fuzz tebal dan jenuh. Berat dan penuh harmonik. |
| **Metal** | Nada high-gain yang rapat dan fokus mid untuk suara agresif dan berat. |
| **Screamer** | Overdrive yang diboost mid yang menembus, seperti tube screamer. |
| **LoFi** | Distorsi pita sempit yang dihancurkan untuk karakter lo-fi yang kasar. |

## Rotate (Stereo Berputar)

**Apa yang dilakukannya:** Memutar suara di sekitar bidang stereo untuk efek rotari yang berputar. Pilih preset, atau atur sendiri rate. Ia perlahan menggerakkan suara di sekitar channel kiri dan kanan Anda, sedikit seperti speaker yang berputar, yang menambahkan nuansa berputar dan menghipnotis. Pengaturan lambat lembut dan lebar, sedangkan pengaturan cepat pusing dan jelas. Ini efek stereo, jadi paling terlihat pada headphone atau speaker yang ditempatkan dengan baik.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Rate** | Seberapa cepat suara berputar di sekitar bidang stereo. Nilai negatif berputar ke arah lain; nol menahannya diam. | -5 hingga +5 Hz (1.0) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Slow Pan** | Pergeseran lambat dan lembut dari sisi ke sisi. Halus dan lebar. |
| **Sway** | Ayunan kiri-kanan yang stabil. Menambahkan gerakan lembut pada citra stereo. |
| **Rotary** | Putaran sedang yang mengingatkan pada speaker rotari. |
| **Fast Spin** | Putaran cepat di sekitar bidang stereo untuk efek pusing dan berputar. |
| **Reverse** | Putaran sedang ke arah berlawanan. |
| **Whirl** | Pusaran yang sangat cepat. Intens dan membingungkan. |

## Crossfeed (Suara Alami pada Headphone)

Pada speaker, masing-masing telinga Anda mendengar speaker kiri dan kanan, hanya pada waktu dan volume yang sedikit berbeda. Pada headphone, pencampuran alami itu hilang: telinga kiri Anda hanya mendengar channel kiri dan telinga kanan Anda hanya kanan. "Super stereo" ini dapat membuat musik terasa seolah terbelah di dalam kepala Anda, dan rekaman yang di-pan keras, di mana instrumen sepenuhnya duduk di satu sisi, bisa terasa tidak alami atau melelahkan pada sesi panjang.

Crossfeed memperbaiki ini dengan mencampur sedikit jumlah yang difilter dari setiap channel ke channel lainnya, dengan delay kecil dan roll-off lembut dari frekuensi tinggi. Itu mendekati bagaimana suara dari speaker nyata mencapai kedua telinga Anda, termasuk cara kepala Anda sedikit menaungi telinga yang jauh. Hasilnya adalah citra yang lebih alami, mirip speaker, yang duduk sedikit di depan Anda alih-alih di dalam kepala Anda, dan ini mengurangi kelelahan mendengarkan pada sesi panjang. Flacbox menggunakan metode **bs2b (Bauer stereophonic-to-binaural)** yang terkenal, crossfeed open-source yang dihormati yang digunakan banyak pemutar audiophile. Anda dapat membaca tentang algoritmanya di [halaman proyek bs2b](https://bs2b.sourceforge.net/).

**Cutoff** mengontrol seberapa hangat campuran terdengar, dan **Feed level** mengontrol seberapa kuatnya. Preset mencakup level bs2b klasik, dari sentuhan yang nyaris tak terasa hingga campuran yang tegas dan mirip speaker. Crossfeed adalah efek headphone, jadi biarkan mati saat Anda mendengarkan pada speaker.

**Slider:**

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Cutoff** | Mengatur di mana bleed antar channel mulai bergulir. Nilai lebih rendah memberikan efek yang lebih hangat dan lebih menonjol. | 300 hingga 2000 Hz (700) |
| **Feed level** | Mengontrol seberapa banyak satu channel bleed ke channel lain. Nilai lebih tinggi menghasilkan suara yang lebih mirip speaker. | 1 hingga 15 dB (4.5) |

**Preset:**

| Preset | Apa yang dilakukannya |
|---|---|
| **Subtle** | Crossfeed yang nyaris tak terasa untuk mendengarkan santai. Melembutkan stereo yang di-pan keras tanpa mengubah keseimbangan nada. |
| **Chu Moy** | Default serbaguna klasik. Seimbang dan sedikit hangat, ini bekerja pada hampir semua materi. Mulai di sini. |
| **Strong** | Bleed lebih kuat untuk campuran yang di-pan lebih keras. Penyempitan stereo yang lebih jelas. |
| **Jan Meier** | Populer di kalangan penggemar headphone. Feed lebih lebar, presentasi lebih mirip speaker, sedikit angkatan bass. |
| **Speaker-like** | Disetel untuk reproduksi gaya speaker yang paling alami melalui headphone. |
| **Vintage Stereo** | Crossfeed agresif yang disetel untuk campuran tahun 1960-an dan 1970-an dengan drum dan vokal yang di-pan keras. |

## Signal Processing: Bangun Rantai DSP Anda Sendiri

Di luar efek siap pakai, Flacbox memungkinkan Anda membangun rantai Anda sendiri di **Pengaturan > Audio player > Signal processing**. Seperti yang dijelaskan aplikasi saat rantai kosong: *"Ketuk + untuk menambahkan efek. Nyalakan atau matikan masing-masing dengan sakelarnya, seret untuk mengatur ulang, ketuk untuk mengedit parameternya, dan tekan lama untuk menduplikasi atau menghapus."*

**Urutan itu penting**: filter sebelum distorsi terdengar berbeda dari filter yang sama setelahnya. Anda juga dapat mengarahkan seluruh rantai ke **All channels**, **Left channel**, atau **Right channel**.

Di bawah ini adalah setiap blok, dengan teks aplikasi sendiri untuk setiap slider dan setiap preset.

### Gain (Trim Level)

Menaikkan atau menurunkan level pada satu titik dalam rantai.

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Gain** | Menaikkan atau memotong level pada titik ini dalam rantai. Gunakan untuk memulihkan level setelah efek lain, atau untuk mendorong efek yang mengikuti. | -24 hingga +24 dB (0) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Unity** | Tidak ada perubahan level. Titik awal netral. |
| **Cut** | Pemotongan besar. Menjinakkan sumber keras, atau memberi ruang sebelum efek yang mengikuti. |
| **Trim** | Pemotongan lembut untuk menarik level kembali sedikit. |
| **Lift** | Boost sederhana untuk menaikkan sumber pelan. |
| **Boost** | Boost kuat untuk materi pelan, atau untuk mendorong efek berikutnya lebih keras. |
| **Max** | Boost maksimum. Keras, waspadai clipping di kemudian rantai. |

### Low Pass (Menghilangkan Highs)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Cutoff** | Mengatur di mana filter mulai menggulung highs. Turunkan untuk menggelapkan dan melembutkan suara; naikkan ke atas untuk membuka penuh. | 20 Hz hingga 20 kHz (20 kHz) |
| **Resonance** | Menekankan frekuensi tepat di cutoff. Jaga tetap rendah untuk roll-off bersih; naikkan untuk tepi yang berpuncak dan bersiul. | 0.1 hingga 10 (0.707) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Air** | Memangkas hanya bagian paling atas. Menghilangkan sedikit tepi tanpa menumpulkan suara. |
| **Warm** | Roll-off lembut dari highs untuk nada yang lebih hangat dan lebih bulat. |
| **Mellow** | Terlihat lebih lembut. Menarik kecerahan kembali untuk nuansa santai. |
| **Muffled** | Gelap dan teredam, seolah didengar melalui dinding. |
| **Telephone** | Puncak sempit dan resonan di bagian rendah rentang. Suara tipis, mirip telepon. |

### High Pass (Menghilangkan Lows)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Cutoff** | Mengatur di mana filter mulai menggulung lows. Naikkan untuk menipiskan low end dan menghilangkan gemuruh; turunkan ke bawah untuk membuka penuh. | 20 Hz hingga 20 kHz (20 Hz) |
| **Resonance** | Menekankan frekuensi tepat di cutoff. Jaga tetap rendah untuk roll-off bersih; naikkan untuk tepi yang berpuncak dan bersiul. | 0.1 hingga 10 (0.707) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Rumble Cut** | Menghilangkan gemuruh subsonik dan DC offset tanpa menyentuh low end yang terdengar. |
| **Tighten** | Memangkas frekuensi rendah yang menggema untuk bass yang lebih rapat dan lebih bersih. |
| **Thin** | Memotong kehangatan dan tubuh, meninggalkan suara yang lebih ringan dan lebih tipis. |
| **Radio** | Hanya mid dan high yang tersisa, seperti speaker radio kecil. |
| **Telephone** | Puncak sempit dan resonan di bagian tinggi rentang. Suara tipis, mirip telepon. |

### Band Pass (Menjaga Band Tengah)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Center** | Mengatur frekuensi yang dilewatkan filter. Semua di atas dan di bawahnya digulung. Sapu untuk memilih bass, mid, atau high. | 20 Hz hingga 20 kHz (1 kHz) |
| **Resonance** | Mengontrol seberapa lebar band. Nilai rendah membiarkan rentang luas lewat; naikkan untuk menyempit ke center untuk nada tajam dan resonan. | 0.1 hingga 10 (0.707) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Voice** | Band lebar di sekitar mid-range tempat sebagian besar vokal berada. Titik awal netral. |
| **Bass** | Mengisolasi low end, meninggalkan hanya bass dan kick. |
| **Body** | Fokus pada low-mid untuk tubuh yang hangat dan kotak. |
| **Presence** | Mengangkat upper-mid untuk kejernihan dan kehadiran. |
| **Telephone** | Band mid-range sempit. Suara tipis, mirip telepon. |
| **Wah** | Puncak yang sangat sempit dan resonan. Sapu center untuk efek wah. |

### Notch (Menghilangkan Satu Band Sempit)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Frequency** | Mengatur frekuensi yang dihilangkan filter. Semua di atas dan di bawahnya melewati. Setel ke dengung atau resonansi untuk memotongnya. | 20 Hz hingga 20 kHz (60 Hz) |
| **Resonance** | Mengontrol seberapa lebar pemotongan. Nilai rendah mengeruk rentang luas; naikkan untuk menghilangkan hanya band setitik dan biarkan sisanya tak tersentuh. | 0.1 hingga 10 (8.0) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Mains Hum 60** | Menghilangkan dengung listrik 60 Hz (listrik Amerika Utara). Titik awal netral. |
| **Mains Hum 50** | Menghilangkan dengung listrik 50 Hz (listrik Eropa dan lainnya). |
| **Rumble** | Memotong gemuruh atau resonansi frekuensi rendah tanpa menipiskan seluruh bagian bawah. |
| **Mud** | Mengeruk kekeruhan low-mid untuk suara yang lebih bersih dan lebih jernih. |
| **Boxy** | Menghilangkan honk mid-range yang kotak. |
| **Harsh** | Menjinakkan puncak yang kasar dan menusuk di upper-mid. |

### Peaking (Band EQ Parametrik)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Frequency** | Center dari band untuk di-boost atau dipotong. Sapu untuk menemukan frekuensi yang ingin Anda bentuk. | 20 Hz hingga 20 kHz (1 kHz) |
| **Gain** | Seberapa banyak untuk boost atau potong di center. Positif mengangkat band; negatif mengeruknya. | -15 hingga +15 dB (0) |
| **Q factor** | Mengatur seberapa lebar band. Nilai rendah membentuk area luas; nilai tinggi menyempit untuk perubahan bedah yang setitik. | 0.1 hingga 10 (1.0) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Presence** | Angkatan upper-mid yang luas untuk kejernihan dan kehadiran. Titik awal netral. |
| **Warmth** | Boost low-mid yang lebar yang menambahkan tubuh dan kehangatan. |
| **Vocal Boost** | Mengangkat rentang vokal inti untuk membawa suara ke depan. |
| **Cut Mud** | Mengeruk kekeruhan low-mid yang kotak untuk suara yang lebih bersih. |
| **Tame Harsh** | Pemotongan sempit untuk menjinakkan puncak yang kasar dan menusuk. |
| **Punch** | Boost rendah yang menambahkan punch dan dampak pada low end. |
| **Sub Boost** | Boost dalam di bagian paling bawah untuk bobot sub-bass ekstra. |
| **Air** | Angkatan luas di bagian atas untuk kilau terbuka dan lapang. |
| **Clarity** | Mengangkat high-mid untuk menambahkan definisi dan tepi. |
| **De-Ess** | Pemotongan sempit dalam rentang sibilan untuk menjinakkan suara S yang kasar. |
| **De-Boom** | Memotong penumpukan frekuensi rendah yang menggema untuk low end yang lebih rapat. |
| **Scoop** | Penurunan mid-range yang lebar untuk nada modern yang dikeruk. |

### Low Shelf (Kontrol Bass dan Bass Boost)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Frequency** | Mengatur sudut di bawah mana shelf berlaku. Semua di bawahnya di-boost atau dipotong bersama. | 20 hingga 2000 Hz (200) |
| **Gain** | Seberapa banyak untuk mengangkat atau menurunkan low end. Positif menambahkan bobot dan kehangatan; negatif menipiskannya. | -15 hingga +15 dB (0) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Warmth** | Angkatan low end yang lembut untuk kehangatan dan tubuh. Titik awal netral. |
| **Bass Boost** | Boost solid ke bass untuk bobot dan punch. |
| **Fullness** | Mengisi lower-mid untuk suara yang lebih penuh dan lebih bulat. |
| **Trim Bass** | Pemotongan sederhana untuk meringankan campuran bass-berat. |
| **Cut Lows** | Pemotongan kuat untuk menipiskan atau de-boom low end. |
| **Big Bottom** | Boost low end besar untuk bobot dan gemuruh maksimum. |

### High Shelf (Kontrol Treble)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Frequency** | Mengatur sudut di atas mana shelf berlaku. Semua di atasnya di-boost atau dipotong bersama. | 1 hingga 20 kHz (8 kHz) |
| **Gain** | Seberapa banyak untuk mengangkat atau menurunkan high end. Positif menambahkan kecerahan dan udara; negatif menghaluskan dan menggelapkan. | -15 hingga +15 dB (0) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Presence** | Angkatan high end yang lembut untuk kejernihan dan detail. Titik awal netral. |
| **Air** | Membuka bagian paling atas untuk suara yang lapang dan terbuka. |
| **Bright** | Boost kuat untuk nada renyah, cerah, dan menonjol. |
| **Soften** | Pemotongan sederhana untuk menghilangkan tepi dari highs yang kasar. |
| **Tame Highs** | Pemotongan kuat untuk menggelapkan dan menghaluskan suara yang terlalu cerah. |
| **Sparkle** | Boost top-end besar untuk kilau dan gemerlap maksimum. |

### Soft Clip (Saturasi Hangat)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Drive** | Mendorong sinyal lebih keras ke waveshaper. Jumlah rendah menambahkan kehangatan lembut; jumlah tinggi membulatkan puncak menjadi saturasi dan kekasaran tebal. | 0 hingga 40 dB (0) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Warm** | Sedikit drive untuk kehangatan lembut gaya analog. |
| **Drive** | Saturasi yang terlihat yang menebalkan dan mewarnai suara. |
| **Crunch** | Drive berat dengan tepi renyah yang terdengar. |
| **Fuzz** | Distorsi tebal dan berbulu. Puncak ditekan keras. |
| **Destroy** | Drive maksimum. Kekasaran yang agresif dan sepenuhnya jenuh. |

### Bit Crusher (Lo-Fi Retro)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Bit depth** | Mengatur berapa banyak bit yang menggambarkan setiap sampel. Lebih sedikit bit berarti langkah lebih kasar dan lebih banyak noise kuantisasi, untuk suara digital yang kasar dan berbutir. | 1 hingga 16 bit (16) |
| **Sample rate** | Menurunkan sampel audio. Pada seratus persen rate tak tersentuh; turunkan untuk menahan setiap sampel lebih lama, menumpulkan highs dan menambahkan tepi aliasing yang kasar. | 1% hingga 100% (100%) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Vintage** | Penurunan kualitas yang halus, seperti sampler digital awal. |
| **LoFi** | Lo-fi 8-bit half-rate klasik. Berbutir dan retro. |
| **Crunch** | Penghancuran lebih berat dengan tepi renyah yang terdengar. |
| **Gritty** | Kasar dan berbutir. Langkah antar level jelas. |
| **Destroy** | Pengurangan ekstrem. Kasar, pecah, hampir tak dikenali. |

### Ring Modulator (Nada Metalik dan Robotik)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Carrier** | Mengatur frekuensi nada yang mengalikan sinyal. Beberapa hertz memberikan getaran tremolo; frekuensi lebih tinggi menambahkan overtone metalik, seperti lonceng, dan robotik. | 1 hingga 4000 Hz (440) |
| **Mix** | Memadukan suara yang dimodulasi dengan aslinya. Pada nol persen Anda hanya mendengar sinyal dry; pada seratus persen hanya nada yang termodulasi penuh. | 0% hingga 100% (0%) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Tremolo** | Carrier yang sangat rendah mengubahnya menjadi tremolo amplitudo, menggetarkan volume. |
| **Robot** | Carrier mid menambahkan overtone berdenting untuk efek suara robot klasik. |
| **Metallic** | Overtone padat dan inharmonik untuk nada yang kasar dan metalik. |
| **Bell** | Carrier lebih tinggi memberikan dering cerah seperti lonceng. |
| **Alien** | Wet penuh dengan carrier tinggi. Ekstrem, asing, hampir tak dikenali. |

### Tremolo (Getaran Volume)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Rate** | Mengatur seberapa cepat volume berdenyut. Rate lebih lambat memberikan ayunan halus; rate lebih cepat memberikan gagap cepat. | 0.1 hingga 20 Hz (5) |
| **Depth** | Mengatur seberapa banyak volume turun pada setiap denyut. Pada nol persen level stabil; pada seratus persen ia turun sampai senyap. | 0% hingga 100% (0%) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Gentle** | Ayunan lambat dan dangkal. Gerakan halus tanpa menarik perhatian. |
| **Classic** | Tremolo amp klasik: rate sedang dan depth sedang. |
| **Deep** | Denyut kuat dan dalam yang hampir turun ke senyap setiap siklus. |
| **Fast** | Kepakan cepat untuk nuansa berkilau dan gugup. |
| **Chop** | Cepat dan depth penuh. Chop yang keras dan tergagap. |

### Delay (Echo)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Time** | Mengatur jeda sebelum setiap gema. Waktu pendek memberikan slapback rapat; waktu lebih panjang menjarakkan pengulangan lebih jauh. | 0.01 hingga 2 s (0.25) |
| **Feedback** | Mengatur seberapa banyak dari setiap gema diumpankan kembali. Nilai rendah memberikan pengulangan tunggal; nilai lebih tinggi membangun serangkaian gema panjang yang menjuntai. | 0 hingga 0.95 (0.4) |
| **Mix** | Memadukan gema dengan aslinya. Pada nol persen Anda hanya mendengar sinyal dry; pada seratus persen hanya gema. | 0% hingga 100% (0%) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Slapback** | Satu gema pendek, rapat terhadap aslinya. Rockabilly dan penggandaan vokal. |
| **Echo** | Echo klasik: pengulangan jelas dengan beberapa ekor menjuntai. |
| **Ping** | Pengulangan cepat dan memantul yang menambahkan gerakan ritmis. |
| **Ambient** | Pengulangan lebih panjang dan lebih lembut yang meluruh menjadi ekor yang lapang. |
| **Dub** | Feedback tinggi untuk kaskade echo panjang dan dubby. |
| **Cavern** | Pengulangan panjang dan dalam, seperti suara bergema melalui ruang besar. |

### Stereo Width (Menyempit atau Melebar)

| Kontrol | Apa yang dilakukannya | Rentang (default) |
|---|---|---|
| **Width** | Menyempit atau melebarkan citra stereo. Nol persen menyusut ke mono, seratus persen membiarkannya tak tersentuh, dan nilai lebih tinggi mendorong sisi lebih lebar. Hanya memengaruhi track stereo pada target All-channels. | 0% hingga 200% (100%) |

| Preset | Apa yang dilakukannya |
|---|---|
| **Wide** | Pelebaran lembut yang membuka citra stereo. Titik awal netral. |
| **Wider** | Sebaran lebih kuat untuk bidang stereo yang besar dan mendalam. |
| **Max** | Lebar maksimum. Sangat lebar, tetapi waspadai masalah kompatibilitas mono. |
| **Narrow** | Menarik sisi masuk untuk citra yang lebih rapat dan lebih terpusat. |
| **Focused** | Hampir terpusat, dengan hanya sedikit stereo. |
| **Mono** | Sepenuhnya menyusut ke mono. Kedua speaker memutar sinyal yang sama. |

## Cara Semuanya Bekerja di Balik Layar (Versi Sederhana)

- **Engine:** Anda memilih satu di Pengaturan > Audio player > Playback engine: **Standard** (sistem), **Universal** (FFmpeg), atau **Sound FX** (**engine BASS™** dari [Un4seen Developments](https://www.un4seen.com/)). Engine yang Anda pilih menentukan format mana yang diputar, dan efek, equalizer, serta rantai DSP berjalan hanya di engine Sound FX.
- **Format:** engine BASS™ menambahkan FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, dan musik modul (tracker) di atas format sistem dan FFmpeg.
- **Efek:** equalizer, compressor, dan sebagian besar efek menggunakan add-on efek BASS™. Freeverb adalah reverb Freeverb. Chorus, Flanger, dan Distortion menggunakan efek gaya DirectX klasik dengan kontrolnya sendiri.
- **Normalisasi Volume:** perata kenyaringan **EBU R128** langsung (standar kenyaringan yang digunakan dalam siaran dan streaming).
- **Crossfeed:** crossfeed **bs2b (Bauer)**, dijalankan di dalam engine BASS™.
- **Rantai DSP:** blok kustom Anda, diterapkan dalam urutan persis yang Anda atur, pada semua channel atau hanya satu sisi.
- **Output:** Anda dapat mengatur sample rate, jumlah channel, dan buffer size agar sesuai dengan perangkat Anda.

Karena semua ini berjalan langsung saat musik diputar, efek:

- Bekerja secara **real time** pada semuanya, termasuk file cloud, streaming, dan musik modul.
- **Tidak pernah mengubah atau menyimpan ulang** file Anda. Matikan efek dan aslinya kembali.
- **Mengingat pengaturan Anda** untuk setiap efek.
- Dapat **dicampur dan dipadukan** secara bebas, karena masing-masing terpisah.

## Resep Sederhana untuk Dicoba

**Mendengarkan sehari-hari**

- **Lebih banyak bass, dengan bersih:** Equalizer > Bass Booster, lalu turunkan Preamplifier 1 hingga 2 dB. Atau tambahkan DSP Low Shelf pada Bass Boost.
- **Volume merata di daftar putar campuran:** Normalisasi Volume > Standard, ditambah Compressor > Soft.
- **Pemolesan keseluruhan yang lembut:** Compressor > Transparent, ditambah Normalisasi Volume > Light.
- **Vokal lebih jernih:** Equalizer > Vocal Booster, atau blok DSP Peaking pada Vocal Boost.
- **Suara lebih penuh pada speaker ponsel kecil:** Equalizer > Small Speakers.

**Headphone**

- **Lebih enak, kurang melelahkan pada headphone:** Crossfeed > Chu Moy atau Jan Meier.
- **Suara lebih lebar pada headphone:** DSP Stereo Width > Wide, ditambah Crossfeed > Chu Moy.
- **Perbaiki rekaman tahun 1960-an dan 1970-an yang di-pan keras:** Crossfeed > Vintage Stereo.
- **Sedikit udara dan ruang:** Freeverb > Ambience, dijaga rendah, ditambah Crossfeed > Subtle.

**Waktu tenang dan audio ucapan**

- **Mendengarkan tenang larut malam:** Normalisasi Volume > Night, ditambah Compressor > Late Night.
- **Podcast dan buku audio:** Compressor > Voice / Podcast, ditambah Equalizer > Spoken Word.
- **Suara paling keras dan paling merata di mobil berisik:** Normalisasi Volume > Strong, ditambah Compressor > Heavy.

**Memperbaiki masalah**

- **Jinakkan rekaman yang kasar dan cerah:** Equalizer > Treble Reducer, atau blok DSP Peaking pada Tame Harsh.
- **Hilangkan dengung listrik:** rantai DSP > Notch > Mains Hum 60 (atau Mains Hum 50 di Eropa).
- **Bass lebih rapat dan lebih bersih:** DSP High Pass > Tighten, untuk memotong low end yang menggema.
- **Kurangi gema pada campuran bass-berat:** DSP Low Shelf > Trim Bass, atau Peaking > De-Boom.

**Kreatif dan menyenangkan**

- **Nuansa hangat dan lapang:** Freeverb > Hall, dijaga rendah.
- **Gitar penuh mimpi dan lapang:** Chorus > Wide, ditambah Echo > Long.
- **Lo-fi retro:** rantai DSP > Bit Crusher (LoFi) ke Soft Clip (Warm).
- **Gerakan funky pada lagu elektronik:** Auto Wah > Funky, atau Phaser > Fast.
- **Sapuan pesawat jet klasik:** Flanger > Jet.

## FAQ

{{% details title="Engine suara apa yang digunakan Flacbox?" closed="true" %}}
Anda memilih satu Playback engine di Pengaturan > Audio player: Standard (engine sistem Apple), Universal (engine FFmpeg), atau Sound FX (engine BASS™ dari Un4seen Developments, un4seen.com). Engine yang Anda pilih menentukan format file mana yang diputar. Sound FX adalah yang memutar format tambahan seperti FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, dan musik MOD atau tracker, dan ini adalah satu-satunya engine yang menyediakan efek langsung, equalizer 10 band, dan rantai DSP. Untuk menggunakan efek, atur Playback engine ke Sound FX.
{{% /details %}}

{{% details title="Bisakah Flacbox memutar MOD, XM, IT, dan musik tracker atau modul lainnya?" closed="true" %}}
Ya. Engine BASS™ memiliki pemutar modul bawaan yang memuat file MOD, XM, IT, S3M, MTM, UMX, dan MO3 dan membangun ulang lagu secara langsung dari pola dan suara instrumennya, sebagaimana musik tracker dimaksudkan untuk dimainkan. Pemutar iPhone biasa tidak dapat melakukan ini. Efek dan equalizer bekerja pada musik modul juga.
{{% /details %}}

{{% details title="Apakah Flacbox mendukung file DSD dan resolusi tinggi?" closed="true" %}}
Ya. Flacbox memutar file DSD (DSF dan DFF) melalui engine BASS™ menggunakan DSD over PCM sehingga mereka bekerja pada perangkat keras output biasa, ditambah FLAC, WavPack, Monkey's Audio (APE), Musepack, dan TrueAudio untuk pemutaran lossless.
{{% /details %}}

{{% details title="Efek suara apa saja yang dimiliki Flacbox?" closed="true" %}}
Equalizer 10 band, Normalisasi Volume, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate, dan Crossfeed, ditambah rantai DSP bikinan sendiri dengan filter, shelf, gain, soft clip, bit crusher, ring modulator, tremolo, delay, dan stereo width. Masing-masing terpisah dan dapat dikombinasikan dengan yang lain.
{{% /details %}}

{{% details title="Apa itu preset?" closed="true" %}}
Preset adalah pengaturan siap pakai untuk sebuah efek. Alih-alih menggeser slider sendiri, Anda mengetuk preset dan suara berubah sesuai. Setiap efek di Flacbox memiliki beberapa preset, dan panduan ini mencantumkan apa yang dilakukan masing-masing. Jika Anda menggeser slider setelah memilih preset, efek menampilkan «Manual» untuk memberi tahu Anda bahwa sekarang ia menggunakan nilai Anda sendiri.
{{% /details %}}

{{% details title="Bagaimana cara membuka efek audio di Flacbox?" closed="true" %}}
Buka pemutar Now Playing, ketuk tombol ⋯ (More), dan pilih Audio effects. Atau buka Pengaturan > Audio player > Audio effects. Ketuk efek, nyalakan sakelarnya, dan pilih preset, atau buka slider untuk menyesuaikan halus.
{{% /details %}}

{{% details title="Di mana equalizer, dan apa pengaturan terbaik?" closed="true" %}}
Buka Pengaturan > Audio player > Audio equalizer. Ia memiliki 10 band dari 32 Hz hingga 16 kHz, masing-masing dari -12 hingga +12 dB, ditambah Preamplifier -24 hingga +24 dB dan 22 preset. Untuk lebih banyak bass, gunakan Bass Booster. Untuk suara lebih jernih, gunakan Vocal Booster atau Pop. Untuk suara lebih cerah, gunakan Treble Booster. Lalu sesuaikan band tunggal sesuai selera.
{{% /details %}}

{{% details title="Bagaimana cara meningkatkan bass di Flacbox?" closed="true" %}}
Dua cara mudah. Di Audio equalizer, pilih Bass Booster (atau naikkan band 32 Hz dan 64 Hz beberapa dB). Atau, di Signal processing, tambahkan blok Low Shelf yang diatur ke Bass Boost. Dalam kedua kasus, turunkan Preamplifier atau tambahkan blok Gain 1 hingga 2 dB sehingga bass tetap bersih dan tidak terdistorsi.
{{% /details %}}

{{% details title="Preset equalizer mana yang terbaik untuk musik saya?" closed="true" %}}
Rock dan Electronic menambahkan energi dengan low dan high yang kuat. Acoustic, Jazz, dan Classical tetap hangat dan alami. Pop dan Vocal Booster mendorong suara ke depan. Bass Booster dan Hip-Hop menambahkan bobot. Deep dan Loudness terdengar lebih penuh pada volume rendah. Mulai dengan yang cocok dengan genre Anda, lalu sesuaikan halus.
{{% /details %}}

{{% details title="Apa itu Normalisasi Volume, dan apa bedanya dengan ReplayGain?" closed="true" %}}
Ini membuat setiap track diputar pada kenyaringan yang kira-kira sama. Ia mengukur kenyaringan sebenarnya menggunakan standar EBU R128 (dalam LUFS, seperti layanan streaming) dan menyesuaikan setiap track menuju target Anda, dengan batas max-boost. Berbeda dengan ReplayGain, ia tidak memerlukan tag dalam file Anda dan bekerja pada sumber apa pun, secara langsung, tanpa mengubah audio. Preset: Light, Standard, Strong, dan Night.
{{% /details %}}

{{% details title="Apa itu Crossfeed, dan haruskah saya menggunakannya?" closed="true" %}}
Crossfeed mencampur sedikit channel kiri dan kanan bersama sehingga headphone terasa lebih seperti speaker nyata dan tidak seperti suara terjebak di dalam kepala Anda. Ini hanya untuk headphone, jadi matikan untuk speaker. Flacbox menggunakan metode bs2b (Bauer), dengan preset seperti Chu Moy dan Jan Meier.
{{% /details %}}

{{% details title="Apa perbedaan antara Compressor dan Normalisasi Volume?" closed="true" %}}
Normalisasi Volume mencocokkan kenyaringan antara lagu-lagu yang berbeda. Compressor meratakan bagian keras dan pelan di dalam satu lagu. Keduanya menyelesaikan masalah yang berbeda dan bekerja baik bersama-sama, terutama di mobil atau tempat berisik.
{{% /details %}}

{{% details title="Apa itu rantai Signal processing (DSP)?" closed="true" %}}
Ini adalah rak bikinan sendiri di Pengaturan > Audio player > Signal processing. Tambahkan blok seperti filter, shelf, gain, soft clip, bit crusher, ring modulator, tremolo, delay, dan stereo width, susun dalam urutan apa pun, nyalakan atau matikan masing-masing, dan arahkan rantai ke semua channel, kiri, atau kanan. Karena urutan penting, Anda dapat merancang persis suara yang Anda inginkan.
{{% /details %}}

{{% details title="Apa perbedaan antara Equalizer, efek, dan rantai DSP?" closed="true" %}}
Equalizer adalah kontrol nada 10 band sederhana. Audio effects adalah alat siap pakai (compressor, reverb, echo, dan sebagainya) dengan preset. Rantai DSP adalah tempat Anda membangun urutan efek Anda sendiri dari blok individual. Anda dapat menjalankan ketiganya secara bersamaan.
{{% /details %}}

{{% details title="Apakah efek mengubah atau merusak file musik saya?" closed="true" %}}
Tidak. Semuanya diterapkan langsung saat musik diputar. File Anda tidak pernah diubah atau disimpan ulang. Matikan efek dan suara asli langsung kembali.
{{% /details %}}

{{% details title="Bisakah saya menggunakan lebih dari satu efek secara bersamaan?" closed="true" %}}
Ya. Setiap efek memiliki sakelarnya sendiri dan tidak ada sakelar utama, jadi kombinasi apa pun bekerja. Misalnya, Normalisasi Volume ditambah Compressor untuk mendengarkan yang merata, atau Freeverb ditambah Crossfeed pada headphone, dengan equalizer di atasnya.
{{% /details %}}

{{% details title="Mengapa kontrol efek berwarna abu-abu?" closed="true" %}}
Efek dimatikan. Nyalakan sakelarnya di bagian atas editor untuk menggunakan kontrol. Setiap efek mati secara default.
{{% /details %}}

{{% details title="Apa arti label Manual?" closed="true" %}}
Itu berarti Anda menggeser slider menjauh dari preset, sehingga efek sekarang menggunakan nilai kustom Anda sendiri alih-alih preset bernama. Setiap slider memiliki tombol reset, dan memilih preset lagi menggantikan nilai manual Anda.
{{% /details %}}

{{% details title="Bisakah saya menyimpan dan berbagi preset equalizer saya?" closed="true" %}}
Ya. Selain 22 preset bawaan, Anda dapat membuat preset Anda sendiri, mengaturnya ulang, dan mengekspor atau mengimpornya untuk memindahkan pengaturan Anda ke perangkat lain.
{{% /details %}}

{{% details title="Apakah efek bekerja dengan CarPlay, streaming, dan pemutaran latar belakang?" closed="true" %}}
Ya. Efek berjalan di dalam engine BASS™, jadi mereka berlaku untuk file lokal, drive cloud, server media, streaming, dan musik modul, dan mereka terus bekerja selama CarPlay dan pemutaran latar belakang.
{{% /details %}}

{{% details title="Bisakah saya mengubah kualitas output audio?" closed="true" %}}
Ya. Di Pengaturan > Audio player Anda dapat mengatur output sample rate, jumlah channel, dan buffer size agar sesuai dengan headphone, speaker, atau DAC Anda.
{{% /details %}}

{{% details title="Apa pengaturan awal yang baik untuk headphone?" closed="true" %}}
Nyalakan Normalisasi Volume (Standard), tambahkan Compressor ringan (Soft), pilih preset equalizer yang Anda suka, dan nyalakan Crossfeed (Chu Moy atau Jan Meier). Biarkan reverb, echo, dan distortion mati kecuali Anda menginginkan suara kreatif.
{{% /details %}}

---

*BASS adalah merek dagang dari Un4seen Developments Ltd. Lihat [un4seen.com](https://www.un4seen.com/). Crossfeed menggunakan algoritma bs2b (Bauer stereophonic-to-binaural); lihat [halaman proyek bs2b](https://bs2b.sourceforge.net/).*
