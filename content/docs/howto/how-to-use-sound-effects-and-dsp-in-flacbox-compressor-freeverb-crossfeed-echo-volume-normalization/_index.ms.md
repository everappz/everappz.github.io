---
title: "Cara Menggunakan Kesan Bunyi dan DSP dalam Flacbox: Compressor, Freeverb, Crossfeed, Echo, Penormalan Kelantangan, dan banyak lagi"
date: 2026-07-24
description: "Panduan lengkap untuk audio Flacbox pada iPhone, iPad, dan Mac. Ketahui cara enjin BASS berfungsi, format tambahan yang dimainkannya (termasuk muzik MOD dan tracker serta DSD), dan apa sebenarnya yang dilakukan oleh setiap kesan, setiap gelangsar, dan setiap pratetap terhadap bunyi anda, tambahan lagi penyama 10 jalur dan rantaian DSP tersuai."
keywords: ["kesan audio Flacbox", "pratetap Flacbox dijelaskan", "enjin BASS Flacbox", "pustaka audio BASS iOS", "pemain muzik MOD iPhone", "pemain muzik tracker iOS", "main MOD XM IT S3M iPhone", "pemain DSD iOS", "pemain FLAC iPhone", "pemain muzik lossless iOS", "pratetap penyama Flacbox", "penyama 10 jalur iPhone", "penormalan kelantangan iPhone", "EBU R128 iOS", "penormalan kekuatan bunyi pemain muzik", "crossfeed fon kepala iOS", "crossfeed bs2b", "pratetap compressor pemain muzik", "reverb freeverb iOS", "echo delay pemain muzik", "rantaian DSP pemain muzik", "peningkatan bass iPhone", "cara menambah kesan pada muzik Flacbox", "tetapan penyama terbaik iPhone"]
tags: ["Flacbox", "Kesan Audio", "Cara", "BASS", "Penyama", "Peningkatan Bass", "Compressor", "Freeverb", "Crossfeed", "Echo", "Penormalan Kelantangan", "EBU R128", "Muzik MOD", "Muzik Tracker", "DSD", "FLAC", "DSP", "Fon Kepala", "Pratetap"]
readingTime: 30
---

{{< author-byline >}}

**Jawapan ringkas:** Dalam Flacbox anda memilih satu **Enjin main balik** dalam **Tetapan > Pemain audio**: **Standard** (enjin sistem Apple), **Universal** (enjin FFmpeg), atau **Sound FX** (**enjin BASS™**). Enjin yang anda pilih menentukan format fail yang dimainkan, jadi pilihan itu penting. Enjin **Sound FX** memainkan format tambahan yang kebanyakan aplikasi iPhone langkau (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, dan muzik **MOD dan tracker** lama seperti MOD, XM, IT, dan S3M), dan ia adalah satu-satunya enjin yang menggerakkan alat bunyi: **penyama 10 jalur**, **Penormalan Kelantangan**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed**, dan **rantaian DSP** yang boleh anda bina sendiri. Jadi untuk menggunakan kesan dalam panduan ini, tetapkan Enjin main balik anda kepada **Sound FX** dahulu. Setiap alat mempunyai **pratetap** siap sedia. Buka ia dalam **Tetapan > Pemain audio** (Kesan audio, Penyama audio, Pemprosesan isyarat), atau ketik butang **⋯ (Lebih banyak tindakan)** pada pemain dan pilih **Kesan audio**. Tiada apa yang anda lakukan di sini akan mengubah fail anda.

> Penjelasan gelangsar dan pratetap di bawah adalah huraian ringkas yang sama seperti yang ditunjukkan Flacbox di dalam aplikasi, digabungkan dengan sedikit latar belakang tambahan supaya anda mendapat gambaran penuh sebelum anda mengetik.

## Cara Membaca Panduan Ini

Setiap alat berfungsi dengan cara yang sama:

1. **Hidupkan.** Setiap kesan mempunyai suisnya sendiri hidup/mati. Semuanya mati pada mulanya. Anda boleh menghidupkan seberapa banyak yang anda suka pada masa yang sama.
2. **Pilih pratetap.** Pratetap ialah tetapan siap sedia. Ketik satu dan bunyi berubah serta-merta. Panduan ini menyenaraikan apa yang dilakukan oleh **setiap** pratetap.
3. **Perhalusi (pilihan).** Buka gelangsar untuk melaras dengan tangan. Sebaik sahaja anda menggerakkan gelangsar, kesan menunjukkan **Manual**, jadi anda tahu anda telah meninggalkan pratetap. Setiap gelangsar mempunyai butang set semula.

Tiada apa yang disimpan ke dalam fail anda. Ini adalah kesan langsung. Matikan kesan dan bunyi asal anda kembali serta-merta.

## Pilih Enjin Main Balik Anda (Sound FX Mempunyai Kesan)

Flacbox tidak menggabungkan enjin bersama-sama. Anda memilih **satu** dalam **Tetapan > Pemain audio > Enjin main balik**, dan enjin yang anda pilih menentukan format fail yang boleh anda mainkan dan sama ada kesan tersedia. Terdapat tiga pilihan, ditunjukkan dalam aplikasi di bawah nama tepat ini:

1. **Standard.** Enjin sistem terbina dalam Apple. Menggunakan penyahkodan perkakasan untuk penggunaan bateri yang lebih rendah.
2. **Universal.** Enjin FFmpeg, yang membuka pelbagai format yang sangat luas.
3. **Sound FX.** **Enjin BASS™**. Ia memainkan fail lossless dan resolusi tinggi dengan ketepatan penuh, menambah muzik modul (tracker), dan menggerakkan setiap kesan, penyama 10 jalur, dan rantaian DSP dalam panduan ini.

Kerana setiap enjin menyokong set formatnya sendiri, fail yang boleh anda mainkan berubah dengan enjin yang anda pilih. Lebih penting lagi, kesan, penyama, dan rantaian DSP berfungsi **hanya** dengan enjin **Sound FX**, jadi pilih ia dahulu jika anda mahu menggunakannya.

Sound FX dibina di atas **BASS™**, pustaka audio profesional daripada Un4seen Developments. Anda boleh membaca lebih lanjut mengenainya di laman utamanya di [un4seen.com](https://www.un4seen.com/).

## Format Muzik: Apa yang Ditambah oleh Enjin Sound FX (BASS™) (Termasuk Muzik MOD dan Tracker)

Dengan enjin **Sound FX (BASS™)** dipilih, Flacbox memainkan format khusus di bawah, tambahan lagi format harian. Yang paling istimewa ialah **muzik modul**, juga dipanggil **muzik tracker**. Fail modul bukanlah rakaman biasa. Ia mengandungi bunyi instrumen kecil serta "skor" yang menyatakan cara memainkannya, dan Flacbox membina semula lagu itu secara langsung daripada skor tersebut, mengikut cara fail ini sepatutnya dimainkan. Pemain biasa tidak boleh melakukan ini.

| Jenis muzik | Format | Baik untuk diketahui |
|---|---|---|
| **Muzik modul / tracker** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Dibina semula secara langsung oleh pemain modul BASS™. Hebat untuk chiptunes dan lagu demoscene atau Amiga lama. |
| **Lossless moden** | FLAC | Kualiti penuh, lebih kecil daripada WAV. |
| **Lossless lain** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Jenis lossless yang kurang biasa, semuanya disokong. |
| **DSD resolusi tinggi** | DSF, DFF | Dimainkan pada perkakasan biasa menggunakan DSD over PCM. |
| **Lossy moden** | Opus, Ogg Vorbis, MP3 | Jenis penstriman dan muat turun yang biasa. |

Enjin Sound FX juga memainkan format Apple arus perdana (AAC, ALAC, M4A, WAV, AIFF) dan strim langsung, jadi kesan dan penyama berfungsi pada format tersebut juga.

**Kenapa ini membantu anda:** jika anda mempunyai campuran album FLAC, fail DSD resolusi tinggi, dan folder lagu tracker MOD atau XM lama, Flacbox memainkan kesemuanya, dan penyama serta kesan berfungsi pada setiap satu daripadanya.

## Tiga Menu yang Akan Anda Gunakan

Flacbox menyimpan alat bunyinya di tiga tempat, semuanya di dalam tetapan pemain audio. Mula-mula pastikan **Enjin main balik** anda ditetapkan kepada **Sound FX** (Tetapan > Pemain audio > Enjin main balik), kerana kesan, penyama, dan rantaian DSP hanya tersedia dengan enjin tersebut.

- **Kesan audio** (rak kesan): buka pemain, ketik **⋯ (Lebih banyak tindakan)**, ketik **Kesan audio**. Atau pergi ke **Tetapan > Pemain audio > Kesan audio**.
- **Penyama audio** (10 jalur dan pratetap): **Tetapan > Pemain audio > Penyama audio**.
- **Pemprosesan isyarat** (rantaian DSP anda sendiri): **Tetapan > Pemain audio > Pemprosesan isyarat**.

Anda juga boleh menetapkan **kadar sampel output**, **saluran**, dan **saiz penimbal** di bawah **Tetapan > Pemain audio**.

## Penyama 10 Jalur

**Apa yang dilakukannya:** Mengubah nada muzik, dari bass yang dalam ke trebel yang cerah. Ini adalah alat terbaik untuk **peningkatan bass** yang bersih atau bahagian atas yang lebih cerah dan jelas. Anggap ia sebagai sepuluh tombol kelantangan, setiap satu untuk kepingan bunyi yang berbeza. Naikkan jalur untuk membawa bahagian itu ke hadapan, turunkan untuk menariknya ke belakang. Perubahan kecil beberapa dB biasanya berbunyi paling baik, dan ia berfungsi pada semua yang anda mainkan.

**Cara ia berfungsi:** Sepuluh gelangsar pada **32, 64, 125, 250, 500 Hz dan 1, 2, 4, 8, 16 kHz**. Setiap satu berjulat dari **-12 dB (potong)** hingga **+12 dB (naik)**. Terdapat juga **Praamplifier** dari **-24 hingga +24 dB** untuk aras keseluruhan. Anda boleh menyimpan pratetap anda sendiri dan **eksport atau import** ia antara peranti.

**Apa yang dilakukan oleh setiap pratetap terbina dalam (22 pratetap):**

| Pratetap | Apa yang dilakukannya terhadap bunyi anda |
|---|---|
| **Flat** | Tiada perubahan. Semua jalur pada sifar. Titik permulaan yang bersih. |
| **Acoustic** | Bass hangat dan bahagian tinggi yang jelas serta hadir. Menjadikan gitar akustik dan suara terasa semula jadi dan bertenaga. |
| **Bass Booster** | Angkat kuat pada bahagian rendah, mid dan tinggi tidak disentuh. Lebih pukulan dan berat. |
| **Bass Reducer** | Memotong bahagian rendah. Berguna untuk bilik yang bergema, fon telinga murah, atau trek yang berat. |
| **Treble Booster** | Mengangkat hanya bahagian tinggi. Menambah kilauan dan udara, lebih perincian. |
| **Treble Reducer** | Melembutkan bahagian tinggi. Menjinakkan rakaman yang keras atau tajam. |
| **Classical** | Bahagian rendah penuh dan bahagian tinggi lembut dengan sedikit penurunan mid. Halus dan lapang untuk muzik orkestra. |
| **Dance** | Bahagian rendah besar dan bahagian tinggi cerah dengan mid yang diceduk. Berpukulan dan bertenaga untuk trek kelab. |
| **Deep** | Bahagian rendah yang hangat dan tebal dengan bahagian tinggi yang lebih lembut. Bunyi yang selesa dan santai. |
| **Electronic** | Bass kuat dan bahagian tinggi cerah untuk synth dan rentak. Luas dan moden. |
| **Hip-Hop** | Bass berat dan bahagian tinggi jelas dengan mid terkawal. Berat dan berpukulan. |
| **Jazz** | Hangat dan halus, dengan sedikit penurunan mid. Mudah dan semula jadi untuk jazz akustik. |
| **Latin** | Bahagian rendah dan tinggi dinaikkan dengan mid yang bersih. Cerah dan bertenaga. |
| **Loudness** | Menaikkan bass dan trebel dengan kuat (lengkung "senyum"). Berbunyi lebih penuh pada kelantangan rendah. |
| **Lounge** | Mid ke hadapan dengan tepi lembut. Santai dan mesra vokal. |
| **Piano** | Mid dan tinggi jelas supaya not piano berbunyi dengan bersih. |
| **Pop** | Mid dinaikkan untuk vokal, dengan bahagian rendah dan tinggi ditarik ke belakang. Suara berada di hadapan. |
| **R&B** | Kehangatan low-mid yang sangat kuat dan bahagian tinggi jelas. Halus dan kaya. |
| **Rock** | Bahagian rendah dan tinggi dinaikkan untuk gitar dan dram. Bertenaga dan penuh. |
| **Small Speakers** | Menaikkan bahagian rendah dan memotong bahagian tinggi untuk membantu pembesar suara kecil berbunyi lebih penuh. |
| **Spoken Word** | Menaikkan julat suara dan memotong bass dalam. Menjadikan pertuturan jelas. |
| **Vocal Booster** | Menolak bahagian tengah tempat suara berada, memotong di sekelilingnya. Vokal menonjol. |

**Tip untuk bass:** Mula dengan **Bass Booster**, kemudian, jika ia berbunyi berlumpur, turunkan Praamplifier 1 hingga 2 dB supaya tiada apa yang herot.

## Penormalan Kelantangan (Kekuatan Bunyi Sekata)

**Apa yang dilakukannya:** Sesetengah lagu dimainkan lebih kuat daripada yang lain, jadi anda sentiasa menukar kelantangan. Ini menjadikan setiap lagu dimainkan pada kelantangan yang lebih kurang sama dengan sendirinya, jadi anda tidak perlu. Ia sesuai untuk senarai main rawak yang mencampurkan rakaman lama dan baru, album berbeza, atau sumber berbeza, di mana satu trek boleh jauh lebih kuat daripada yang seterusnya.

**Cara ia berfungsi:** Ia mendengar kekuatan bunyi sebenar setiap trek menggunakan standard **EBU R128** (diukur dalam **LUFS**, idea yang sama digunakan perkhidmatan penstriman), kemudian melaras setiap trek ke arah sasaran anda. Ia tidak memerlukan tag dalam fail anda dan tidak pernah mengubah audio. EBU R128 mengukur kekuatan bunyi yang telinga anda benar-benar rasa sepanjang keseluruhan lagu, bukan hanya puncak tertinggi, sebab itulah ia sepadan dengan betapa kuatnya trek benar-benar kelihatan kepada anda. Flacbox mengira ini secara langsung semasa muzik dimainkan (dan memeriksa kekuatan bunyi terlebih dahulu apabila boleh), kemudian menggunakan satu perubahan kelantangan yang tetap dan mantap pada trek. Had **Naik maks** menghalang rakaman yang sangat perlahan daripada ditolak terlalu kuat sehingga herot. Kerana ia membaca bunyi itu sendiri, ia berfungsi pada mana-mana sumber, termasuk fail awan, strim langsung, dan muzik modul, walaupun apabila fail tidak mempunyai tag kekuatan bunyi langsung.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Kekuatan bunyi sasaran** | Menetapkan kekuatan bunyi yang setiap trek dilaraskan ke arahnya. Nilai lebih tinggi menjadikan segalanya dimainkan lebih kuat secara keseluruhan. | -30 hingga -6 LUFS (-16) |
| **Naik maks** | Mengehadkan berapa banyak trek perlahan boleh diperkuat. Nilai lebih tinggi membawa rakaman lembut lebih dekat kepada sasaran. | 0 hingga 24 dB (12) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Light** | Pelarasan lembut untuk mendengar santai. Meratakan lonjakan kelantangan yang jelas tanpa menolak trek perlahan dengan kuat. |
| **Standard** | Lalai serba guna. Sasaran kekuatan bunyi bergaya penstriman yang sesuai untuk kebanyakan muzik. Mula di sini. |
| **Strong** | Pemadanan agresif yang menolak trek perlahan ke atas dengan tegas. Terbaik untuk pustaka bercampur dengan perbezaan aras yang besar. |
| **Night** | Sasaran keseluruhan yang lebih senyap yang masih mengangkat petikan lembut, supaya mendengar lewat malam kekal konsisten dan rendah. |

## Compressor (Ratakan Bahagian Kuat dan Perlahan)

**Apa yang dilakukannya:** Dalam satu lagu, bahagian perlahan boleh terlalu lembut dan bahagian kuat terlalu kuat. Ini membawanya lebih dekat bersama, supaya keseluruhan lagu mudah didengar, walaupun di dalam kereta atau tempat yang bising. Ia menurunkan detik-detik paling kuat dengan lembut dan mengangkat yang lebih lembut, supaya anda berhenti mencapai kelantangan semasa satu trek. Ini berbeza daripada Penormalan Kelantangan: Compressor meratakan sesuatu **di dalam** satu lagu, manakala Penormalan Kelantangan memadankan kekuatan bunyi **antara** lagu. Kedua-duanya berfungsi dengan baik bersama-sama. Mula dengan pratetap, dan hanya buka gelangsar jika anda mahu lebih kawalan.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Threshold** | Aras di mana pemampatan bermula. Nilai lebih rendah memicit lebih banyak bunyi, mengekalkan bahagian perlahan dan kuat lebih dekat bersama. | -60 hingga 0 dB (-20) |
| **Ratio** | Betapa kuat bahagian kuat ditahan sebaik sahaja ia melepasi threshold. Nilai lebih tinggi memampat lebih keras, mengekalkan bunyi lebih sekata. | 1:1 hingga 30:1 (4:1) |
| **Attack** | Betapa cepat kesan bertindak balas terhadap puncak kuat yang tiba-tiba. Nilai pendek menangkap transien; yang lebih panjang membiarkannya lalu. | 0.1 hingga 1000 ms (10 ms) |
| **Release** | Betapa cepat kesan melepaskan selepas bahagian kuat berlalu. Nilai pendek boleh mengepam; yang lebih panjang berbunyi lebih halus. | 10 ms hingga 5 s (100 ms) |
| **Master gain** | Peningkatan output akhir digunakan selepas pemprosesan. Naikkan ini untuk mengangkat kekuatan bunyi keseluruhan sebaik sahaja dinamik diratakan. | -30 hingga +30 dB (0) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Transparent** | Jaring keselamatan yang hampir tidak wujud. Mengekalkan dinamik hampir sepenuhnya dan hanya menangkap puncak paling kuat. |
| **Soft** | Pelarasan ringan untuk mendengar hi-fi di rumah. Pelicinan halus tanpa memicit muzik. |
| **Standard** | Lalai munasabah untuk main balik muzik harian. Pratetap pertama untuk dicuba. |
| **Heavy** | Pelarasan agresif untuk persekitaran bising. Kereta, bilik sesak, mendengar kelantangan rendah. |
| **Voice / Podcast** | Ditala untuk pertuturan. Attack lebih perlahan membiarkan sibilan lalu, gain solek murah hati menarik vokal ke atas. |
| **Old Recordings** | Album vintaj dan vinil yang dipulihkan, di mana aras purata di bawah keluaran moden. |
| **Late Night** | Pemampatan berat tambahan peningkatan besar untuk mendengar senyap apabila jiran atau keluarga yang tidur penting. |
| **Movie Dialog** | Membawa pertuturan naik menentang muzik dan kesan bunyi dalam runut bunyi yang pelbagai. |
| **Streaming Match** | Menyasarkan lebih kurang penormalan kekuatan bunyi perkhidmatan penstriman moden sekitar -14 LUFS. |
| **Maximum Loudness** | Semua masuk. Mencapai pengehad; jangka isyarat yang dipicit dan sangat sekata. Pratetap kelantangan maksimum harfiah. |

## Freeverb (Reverb, Rasa Ruang)

**Apa yang dilakukannya:** Menambah rasa ruang pada muzik, dari bilik kecil hingga dewan besar. Pilih pratetap, atau perhalusi campuran kering dan basah, saiz bilik, redaman dan lebar sendiri. Reverb ialah gema semula jadi yang anda dengar dalam mana-mana ruang sebenar, dan Freeverb mencipta semula ia dalam perisian. Sedikit menjadikan rakaman yang rata atau mikrofon dekat terasa lebih terbuka dan bertenaga. Banyak meletakkan muzik dalam ruang besar dan jauh. Ia adalah kesan kreatif, jadi kekalkan campuran basah sederhana untuk hasil semula jadi.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Dry mix** | Berapa banyak bunyi asal yang tidak disentuh dikekalkan. Nilai lebih tinggi meninggalkan lebih banyak isyarat kering dalam campuran. | 0 hingga 1 (0.0) |
| **Wet mix** | Berapa banyak bunyi bergema ditambah. Nilai lebih tinggi menjadikan reverb lebih kuat dan lebih jelas. | 0 hingga 3 (1.0) |
| **Room size** | Saiz ruang yang dibayangkan. Nilai lebih tinggi memberikan ekor reverb yang lebih panjang dan besar, dari bilik kecil hingga katedral. | 0 hingga 1 (0.5) |
| **Damp** | Betapa cepat frekuensi tinggi pudar dalam ekor. Nilai lebih tinggi menjadikan reverb lebih gelap dan hangat. | 0 hingga 1 (0.5) |
| **Width** | Sebaran stereo reverb. Nilai lebih tinggi menjadikan ruang terasa lebih luas antara saluran kiri dan kanan. | 0 hingga 1 (1.0) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Room** | Ruang kecil dan ketat. Ambien halus yang menambah rasa tempat tanpa membasuh bunyi. |
| **Studio** | Bilik rakaman kering dan terkawal. Cukup pantulan untuk berbunyi semula jadi. |
| **Hall** | Dewan konsert besar. Ekor yang panjang dan subur yang sesuai untuk muzik orkestra dan akustik. |
| **Cathedral** | Ruang batu besar yang bergema. Ekor reverb terpanjang dan paling dramatik. |
| **Plate** | Reverb plat studio yang cerah dan padat. Klasik untuk vokal dan dram. |
| **Ambience** | Ambien pendek dan lapang. Menambah rasa ruang ringan sambil kekal kebanyakannya kering. |

## Auto Wah (Sapuan Penapis Funky)

**Apa yang dilakukannya:** Penapis yang menyapu naik dan turun dengan sendirinya untuk bunyi wah yang funky dan seperti suara. Pilih pratetap, atau tetapkan campuran basah, maklum balas, kadar, julat dan frekuensi sendiri. Ia adalah sapuan "wah" yang sama yang dibuat oleh pedal wah gitar, tetapi di sini ia bergerak dengan sendirinya seiring dengan muzik. Ia berbunyi hebat pada trek funk, disko, dan elektronik. Ia adalah kesan yang berani dan jelas, jadi sedikit sudah cukup untuk mendengar harian.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Wet mix** | Betapa kuat kesan wah dalam campuran. Nilai lebih tinggi menjadikan penapis menyapu lebih jelas. | -2 hingga +2 (1.5) |
| **Feedback** | Berapa banyak output disalurkan semula ke dalam kesan. Nilai lebih tinggi menjadikan wah lebih resonan dan ketara. | -1 hingga +1 (0.5) |
| **Rate** | Betapa cepat penapis menyapu naik dan turun. Nilai lebih tinggi memberikan wah yang lebih pantas dan berirama. | 0.1 hingga 9 Hz (2.0) |
| **Range** | Sejauh mana penapis menyapu, dalam oktaf. Nilai lebih tinggi memberikan sapuan yang lebih luas dan dramatik. | 0.1 hingga 9 oktaf (4.3) |
| **Frequency** | Frekuensi asas yang penapis sapu di sekelilingnya. Nilai lebih rendah berbunyi lebih dalam; nilai lebih tinggi berbunyi lebih cerah. | 1 hingga 1000 Hz (50) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Classic** | Sapuan wah klasik yang seimbang. Titik permulaan yang baik untuk funk dan rock. |
| **Slow** | Sapuan perlahan dan luas yang hanyut lembut naik dan turun. Hebat untuk pad dan not panjang. |
| **Funky** | Sapuan pantas dan berpukulan dengan banyak pergerakan. Menambah gigitan berirama pada gitar dan synth. |
| **Deep** | Sapuan dalam dan luas bermula dari frekuensi rendah. Besar dan dramatik. |
| **Subtle** | Pergerakan lembut dan sederhana. Menambah watak tanpa mendominasi bunyi. |
| **Resonant** | Wah tajam dan resonan dengan maklum balas tinggi. Seperti suara dan ekspresif. |

## Phaser (Bunyi Berpusar)

**Apa yang dilakukannya:** Penapis menyapu yang menambah gerakan berpusar dan berbunyi pada bunyi. Pilih pratetap, atau tetapkan maklum balas, kadar, julat dan frekuensi sendiri. Ia menambah pergerakan lembut dan kilauan tanpa mengubah not. Ia halus pada vokal dan pad, dan dramatik pada synth dan gitar. Cuba Slow untuk rasa seperti mimpi atau Jet untuk pusaran yang kuat.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Feedback** | Berapa banyak output disalurkan semula ke dalam kesan. Nilai lebih tinggi menjadikan phaser lebih resonan dan ketara. | -1 hingga +1 (0.0) |
| **Rate** | Betapa cepat penapis menyapu naik dan turun. Nilai lebih tinggi memberikan phasing yang lebih pantas dan berirama. | 0.1 hingga 9 Hz (1.0) |
| **Range** | Sejauh mana penapis menyapu, dalam oktaf. Nilai lebih tinggi memberikan sapuan yang lebih luas dan dramatik. | 0.1 hingga 9 oktaf (4.0) |
| **Frequency** | Frekuensi asas yang penapis sapu di sekelilingnya. Nilai lebih rendah berbunyi lebih dalam; nilai lebih tinggi berbunyi lebih cerah. | 1 hingga 1000 Hz (100) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Classic** | Sapuan phaser klasik yang seimbang. Titik permulaan yang baik untuk gitar dan kekunci. |
| **Slow** | Sapuan perlahan dan luas yang hanyut lembut naik dan turun. Hebat untuk pad dan not panjang. |
| **Fast** | Sapuan pantas dan berkilauan dengan banyak pergerakan. Menambah gerakan dan tenaga. |
| **Deep** | Sapuan dalam dan luas bermula dari frekuensi rendah. Besar dan dramatik. |
| **Subtle** | Pergerakan lembut dan sederhana. Menambah watak tanpa mendominasi bunyi. |
| **Jet** | Sapuan sengit dan resonan dengan maklum balas tinggi, bunyi pesawat jet klasik. |

## Flanger (Sapuan Pesawat Jet)

**Apa yang dilakukannya:** Delay pendek yang bergerak yang memberikan bunyi sapuan seperti jet. Pilih pratetap, atau tetapkan kedalaman, maklum balas, kadar dan delay sendiri. Ia adalah sepupu phaser yang lebih kuat dan lebih metalik, terkenal dengan sapuan berbunyi dalam rock klasik dan muzik elektronik. Tetapan halus menambah pergerakan lembut, manakala tetapan dalam adalah dramatik dan jelas. Terbaik digunakan dengan berhemah, untuk kesan.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Depth** | Betapa kuat kesan menyapu. Nilai lebih tinggi menjadikan flanging lebih jelas. | 0 hingga 100% (25) |
| **Feedback** | Berapa banyak output disalurkan semula ke dalam kesan. Nilai lebih tinggi menjadikan flanger lebih resonan dan metalik. | -99 hingga +99% (-50) |
| **Rate** | Betapa cepat sapuan bergerak naik dan turun. Nilai lebih tinggi memberikan gerakan yang lebih pantas dan berkilauan. | 0 hingga 10 Hz (0.25) |
| **Delay** | Masa delay asas yang sapuan dibina di atasnya. Nilai lebih tinggi memberikan watak yang lebih dalam dan berongga. | 0 hingga 4 ms (2.0) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Classic** | Flanger klasik yang seimbang. Titik permulaan yang baik untuk gitar dan kekunci. |
| **Subtle** | Sapuan lembut dan sederhana. Menambah pergerakan tanpa mendominasi bunyi. |
| **Deep** | Sapuan dalam dan berat dengan maklum balas kuat. Besar dan dramatik. |
| **Jet** | Sapuan sengit dengan maklum balas positif, bunyi pesawat jet klasik. |
| **Fast** | Sapuan pantas dan berkilauan dengan banyak gerakan dan tenaga. |
| **Wide** | Sapuan perlahan dan luas dengan delay panjang. Subur dan lapang. |

## Echo (Ulangan)

**Apa yang dilakukannya:** Mengulang bunyi sebagai gema yang pudar untuk rasa ruang dan kedalaman. Pilih pratetap, atau tetapkan campuran basah, maklum balas dan delay sendiri. Ia seperti menjerit di dalam ngarai: bunyi kembali satu atau lebih kali selepas jeda pendek. Satu ulangan pendek menambah tubuh dan rasa retro, manakala ulangan lebih panjang dengan lebih banyak maklum balas mencipta ekor yang lapang dan berlarutan. Pratetap Ping Pong melantunkan ulangan antara telinga kiri dan kanan anda, yang menyeronokkan pada fon kepala. Kekalkan campuran basah sederhana supaya gema menyokong muzik dan bukan menutupinya.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Wet mix** | Betapa kuat gema berbanding bunyi asal. Nilai lebih tinggi menjadikan ulangan lebih menonjol. | -2 hingga +2 (0.6) |
| **Feedback** | Berapa kali echo mengulang. Nilai lebih tinggi memberikan lebih banyak ulangan yang mengambil masa lebih lama untuk pudar. | -1 hingga +1 (0.5) |
| **Delay** | Masa antara gema. Nilai lebih pendek memberikan slap-back ketat; nilai lebih panjang memberikan ulangan berjarak. | 0.01 hingga 2 s (0.4) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Slapback** | Satu ulangan tunggal dan ketat tepat di belakang bunyi. Slap-back rockabilly klasik. |
| **Room** | Echo pendek dan semula jadi, seperti bilik kecil. Menambah ruang tanpa mengaburkan bunyi. |
| **Tape** | Ulangan hangat dan sederhana yang pudar secara beransur-ansur, seperti tape delay lama. |
| **Dub** | Ulangan panjang dan berat dengan maklum balas kuat. Besar, dubby dan lapang. |
| **Ping Pong** | Gema melantun antara pembesar suara kiri dan kanan untuk kesan stereo yang luas. |
| **Long** | Ulangan perlahan dan berjarak luas yang berlarutan jauh di belakang bunyi. |

## Chorus (Bunyi Lebih Tebal, Lebih Luas)

**Apa yang dilakukannya:** Menebalkan dan meluaskan bunyi dengan melapiskan salinan yang beralih di atas yang asal. Pilih pratetap, atau tetapkan campuran basah/kering, kedalaman, kadar dan maklum balas sendiri. Ia menjadikan satu instrumen atau suara berbunyi seperti beberapa yang bermain bersama, dengan menambah salinan yang sedikit ditala dan bergerak. Ini menambah kekayaan dan kilauan lembut. Tetapan halus menghangatkan sesuatu, manakala tetapan kuat berbunyi subur dan seperti mimpi. Ia popular pada gitar, papan kekunci, dan vokal.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Wet/Dry** | Berapa banyak chorus yang anda dengar berbanding bunyi asal. Nilai lebih tinggi menjadikan kesan lebih jelas. | 0 hingga 100% (50) |
| **Depth** | Sejauh mana pic bergoyang naik dan turun. Nilai lebih tinggi memberikan bunyi yang lebih tebal dan berkilauan. | 0 hingga 100% (25) |
| **Rate** | Betapa cepat kilauan bergerak. Kadar lebih perlahan berbunyi lembut dan subur; kadar lebih pantas berbunyi lebih seperti vibrato. | 0 hingga 10 Hz (1.1) |
| **Feedback** | Berapa banyak kesan disalurkan semula ke dalam dirinya. Nilai lebih tinggi menjadikan chorus lebih resonan dan sengit. | -99 hingga +99% (25) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Subtle** | Penebalan lembut yang menambah kehangatan tanpa menarik perhatian kepada dirinya. |
| **Lush** | Chorus yang kaya dan klasik. Tetapan serba boleh yang hebat untuk gitar dan kekunci. |
| **Ensemble** | Kilauan penuh dan berlapis yang menjadikan satu instrumen berbunyi seperti beberapa. |
| **Vibrato** | Sepenuhnya basah dengan kadar pantas, untuk vibrato bergoyang dan bukan chorus halus. |
| **Wide** | Kilauan perlahan dan luas yang membuka imej stereo. Lapang dan seperti mimpi. |
| **Twelve-String** | Kilauan cerah dan resonan yang mengingatkan gitar dua belas tali. |

## Distortion (Kekasaran dan Tepi)

**Apa yang dilakukannya:** Menambah kekasaran dan tepi dengan memacu berlebihan bunyi. Pilih pratetap, atau tetapkan drive, output dan tone sendiri. Ia sengaja mengasarkan bunyi, dari tepi hangat dan kasar hingga nada pecah dan berbulu. Ia adalah kesan kreatif dan menyeronokkan dan bukan cara untuk meningkatkan kualiti, jadi gunakannya dalam jumlah kecil. Ia menyeronokkan pada trek elektronik, rock, dan eksperimental. Turunkan Output jika pratetap berat menjadi terlalu kuat.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Drive** | Betapa keras bunyi diherotkan. Nilai lebih tinggi lebih kasar dan lebih agresif. | 0 hingga 100% (15) |
| **Output** | Aras output selepas distortion. Turunkannya jika tetapan berat menjadi terlalu kuat. | -60 hingga 0 dB (-18) |
| **Tone** | Menggulung bahagian tinggi sebelum distortion. Nilai lebih rendah berbunyi lebih gelap dan hangat. | 100 hingga 8000 Hz (8000) |
| **Center** | Frekuensi mana distortion difokuskan. Mengalihkan watak lebih cerah atau lebih gelap. | 100 hingga 8000 Hz (2400) |
| **Width** | Betapa luas fokus itu. Sempit berbunyi tajam dan sengau; luas berbunyi penuh dan terbuka. | 100 hingga 8000 Hz (2400) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Warm Drive** | Kekasaran ringan dan hangat yang menambah tepi tanpa banyak mengubah watak. |
| **Crunch** | Overdrive rangup klasik, berpukulan dan berirama. |
| **Overdrive** | Nada cerah dan terpacu dengan banyak gigitan. Hebat untuk bunyi utama. |
| **Fuzz** | Fuzz tebal dan tepu. Berat dan penuh harmonik. |
| **Metal** | Nada gain tinggi yang ketat dan tertumpu pada mid untuk bunyi agresif dan berat. |
| **Screamer** | Overdrive dinaikkan mid yang menembusi, seperti tube screamer. |
| **LoFi** | Distortion jalur sempit yang dihancurkan untuk watak lo-fi yang kasar. |

## Rotate (Stereo Berputar)

**Apa yang dilakukannya:** Memutarkan bunyi di sekeliling medan stereo untuk kesan berputar dan berpusar. Pilih pratetap, atau tetapkan kadar sendiri. Ia perlahan-lahan menggerakkan bunyi di sekeliling saluran kiri dan kanan anda, sedikit seperti pembesar suara berputar, yang menambah rasa berpusar dan menghipnosis. Tetapan perlahan lembut dan luas, manakala tetapan pantas pening dan jelas. Ia adalah kesan stereo, jadi ia paling ketara pada fon kepala atau pembesar suara yang diletakkan dengan baik.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Rate** | Betapa cepat bunyi berputar di sekeliling medan stereo. Nilai negatif berputar arah lain; sifar menahannya diam. | -5 hingga +5 Hz (1.0) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Slow Pan** | Hanyut perlahan dan lembut dari sisi ke sisi. Halus dan luas. |
| **Sway** | Ayunan kiri-kanan yang mantap. Menambah gerakan lembut pada imej stereo. |
| **Rotary** | Putaran sederhana yang mengingatkan pembesar suara berputar. |
| **Fast Spin** | Putaran pantas di sekeliling medan stereo untuk kesan pening dan berpusar. |
| **Reverse** | Putaran sederhana dalam arah bertentangan. |
| **Whirl** | Pusaran yang sangat pantas. Sengit dan mengelirukan. |

## Crossfeed (Bunyi Semula Jadi pada Fon Kepala)

Pada pembesar suara, setiap telinga anda mendengar kedua-dua pembesar suara kiri dan kanan, cuma pada masa dan kelantangan yang sedikit berbeza. Pada fon kepala, gabungan semula jadi itu hilang: telinga kiri anda mendengar hanya saluran kiri dan telinga kanan anda hanya kanan. "Stereo super" ini boleh menjadikan muzik terasa seperti terpecah di dalam kepala anda, dan rakaman yang dipan keras, di mana instrumen berada sepenuhnya pada satu sisi, boleh terasa tidak semula jadi atau meletihkan pada sesi mendengar yang panjang.

Crossfeed membetulkan ini dengan mencampurkan sedikit jumlah setiap saluran yang ditapis ke dalam yang lain, dengan delay kecil dan gulungan lembut frekuensi tinggi. Itu hampir dengan cara bunyi dari pembesar suara sebenar sampai ke kedua-dua telinga anda, termasuk cara kepala anda sedikit membayangi telinga yang jauh. Hasilnya ialah imej yang lebih semula jadi dan seperti pembesar suara yang berada sedikit di hadapan anda dan bukan di dalam kepala anda, dan ia mengurangkan keletihan mendengar pada sesi panjang. Flacbox menggunakan kaedah **bs2b (Bauer stereophonic-to-binaural)** yang terkenal, crossfeed sumber terbuka yang dihormati yang digunakan oleh banyak pemain audiophile. Anda boleh membaca tentang algoritma pada [halaman projek bs2b](https://bs2b.sourceforge.net/).

**Cutoff** mengawal betapa hangat campuran itu berbunyi, dan **Feed level** mengawal betapa kuatnya. Pratetap meliputi aras bs2b klasik, dari sentuhan yang hampir tidak wujud hingga campuran tegas seperti pembesar suara. Crossfeed ialah kesan fon kepala, jadi biarkan ia mati apabila anda mendengar pada pembesar suara.

**Gelangsar:**

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Cutoff** | Menetapkan di mana lelehan antara saluran mula bergulung. Nilai lebih rendah memberikan kesan yang lebih hangat dan lebih ketara. | 300 hingga 2000 Hz (700) |
| **Feed level** | Mengawal berapa banyak satu saluran meleleh ke dalam yang lain. Nilai lebih tinggi menghasilkan bunyi yang lebih seperti pembesar suara. | 1 hingga 15 dB (4.5) |

**Pratetap:**

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Subtle** | Crossfeed yang hampir tidak wujud untuk mendengar santai. Melembutkan stereo yang dipan keras tanpa mengubah keseimbangan nada. |
| **Chu Moy** | Lalai serba guna klasik. Seimbang dan sedikit hangat, ia berfungsi pada hampir mana-mana bahan. Mula di sini. |
| **Strong** | Lelehan lebih kuat untuk campuran yang dipan lebih keras. Penyempitan stereo yang lebih jelas. |
| **Jan Meier** | Popular dalam kalangan peminat fon kepala. Feed lebih luas, persembahan lebih seperti pembesar suara, sedikit peningkatan bass. |
| **Speaker-like** | Ditala untuk pengeluaran semula gaya pembesar suara yang paling semula jadi melalui fon kepala. |
| **Vintage Stereo** | Crossfeed agresif yang ditala untuk campuran 1960-an dan 1970-an dengan dram dan vokal yang dipan keras. |

## Pemprosesan Isyarat: Bina Rantaian DSP Anda Sendiri

Selain kesan siap sedia, Flacbox membolehkan anda membina rantaian anda sendiri dalam **Tetapan > Pemain audio > Pemprosesan isyarat**. Seperti yang dijelaskan aplikasi apabila rantaian kosong: *"Ketik + untuk menambah kesan. Hidupkan atau matikan setiap satu dengan suisnya, seret untuk menyusun semula, ketik untuk mengedit parameternya, dan tekan lama untuk menduplikasi atau memadam."*

**Susunan penting**: penapis sebelum distortion berbunyi berbeza daripada penapis yang sama selepasnya. Anda juga boleh menghalakan keseluruhan rantaian ke **Semua saluran**, **Saluran kiri**, atau **Saluran kanan**.

Di bawah ialah setiap blok, dengan teks aplikasi sendiri untuk setiap gelangsar dan setiap pratetap.

### Gain (Pemangkasan Aras)

Menaikkan atau menurunkan aras pada satu titik dalam rantaian.

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Gain** | Menaikkan atau memotong aras pada titik ini dalam rantaian. Gunakannya untuk mengganti aras selepas kesan lain, atau untuk memacu yang mengikuti. | -24 hingga +24 dB (0) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Unity** | Tiada perubahan aras. Titik permulaan neutral. |
| **Cut** | Potongan besar. Menjinakkan sumber yang kuat, atau memberi ruang sebelum kesan yang mengikuti. |
| **Trim** | Potongan lembut untuk menarik aras ke belakang sedikit. |
| **Lift** | Peningkatan sederhana untuk menaikkan sumber yang perlahan. |
| **Boost** | Peningkatan kuat untuk bahan perlahan, atau untuk memacu kesan yang mengikuti dengan lebih keras. |
| **Max** | Peningkatan maksimum. Kuat, berhati-hati dengan keratan kemudian dalam rantaian. |

### Low Pass (Membuang Bahagian Tinggi)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Cutoff** | Menetapkan di mana penapis mula menggulung bahagian tinggi. Turunkannya untuk menggelapkan dan melembutkan bunyi; naikkannya ke arah puncak untuk membuka sepenuhnya. | 20 Hz hingga 20 kHz (20 kHz) |
| **Resonance** | Menekankan frekuensi tepat pada cutoff. Kekalkan ia rendah untuk gulungan bersih; naikkannya untuk tepi memuncak dan bersiul. | 0.1 hingga 10 (0.707) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Air** | Memangkas hanya bahagian atas sekali. Mengambil sedikit tepi tanpa menumpulkan bunyi. |
| **Warm** | Gulungan lembut bahagian tinggi untuk nada yang lebih hangat dan bulat. |
| **Mellow** | Dilembutkan dengan ketara. Menarik kecerahan ke belakang untuk rasa santai. |
| **Muffled** | Gelap dan perlahan, seolah-olah didengar melalui dinding. |
| **Telephone** | Puncak sempit dan resonan rendah dalam julat. Suara nipis seperti telefon. |

### High Pass (Membuang Bahagian Rendah)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Cutoff** | Menetapkan di mana penapis mula menggulung bahagian rendah. Naikkannya untuk menipiskan bahagian rendah dan membuang gemuruh; turunkannya ke arah bawah untuk membuka sepenuhnya. | 20 Hz hingga 20 kHz (20 Hz) |
| **Resonance** | Menekankan frekuensi tepat pada cutoff. Kekalkan ia rendah untuk gulungan bersih; naikkannya untuk tepi memuncak dan bersiul. | 0.1 hingga 10 (0.707) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Rumble Cut** | Membuang gemuruh subsonik dan offset DC tanpa menyentuh bahagian rendah yang boleh didengar. |
| **Tighten** | Memangkas frekuensi rendah bergema untuk bass yang lebih ketat dan bersih. |
| **Thin** | Memotong kehangatan dan tubuh, meninggalkan bunyi yang lebih ringan dan nipis. |
| **Radio** | Hanya mid dan bahagian tinggi kekal, seperti pembesar suara radio kecil. |
| **Telephone** | Puncak sempit dan resonan tinggi dalam julat. Suara nipis seperti telefon. |

### Band Pass (Mengekalkan Jalur Tengah)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Center** | Menetapkan frekuensi yang penapis lalukan. Segala di atas dan di bawahnya digulung. Sapu ia untuk memilih bass, mid, atau bahagian tinggi. | 20 Hz hingga 20 kHz (1 kHz) |
| **Resonance** | Mengawal betapa luas jalur itu. Nilai rendah membiarkan julat luas lalu; naikkannya untuk mempersempit ke tengah untuk nada tajam dan resonan. | 0.1 hingga 10 (0.707) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Voice** | Jalur luas sekitar julat pertengahan tempat kebanyakan vokal berada. Titik permulaan neutral. |
| **Bass** | Mengasingkan bahagian rendah, meninggalkan hanya bass dan kick. |
| **Body** | Fokus pada low-mid untuk tubuh yang hangat dan berkotak. |
| **Presence** | Mengangkat upper-mid untuk kejelasan dan kehadiran. |
| **Telephone** | Jalur julat pertengahan yang sempit. Bunyi nipis seperti telefon. |
| **Wah** | Puncak yang sangat sempit dan resonan. Sapu tengah untuk kesan wah. |

### Notch (Membuang Satu Jalur Sempit)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Frequency** | Menetapkan frekuensi yang penapis buang. Segala di atas dan di bawahnya lalu. Talakan ia pada dengung atau resonans untuk memotongnya. | 20 Hz hingga 20 kHz (60 Hz) |
| **Resonance** | Mengawal betapa luas potongan itu. Nilai rendah menceduk julat luas; naikkannya untuk membuang hanya jalur setepat mungkin dan biarkan selebihnya tidak disentuh. | 0.1 hingga 10 (8.0) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Mains Hum 60** | Membuang dengung elektrik 60 Hz (kuasa utama Amerika Utara). Titik permulaan neutral. |
| **Mains Hum 50** | Membuang dengung elektrik 50 Hz (kuasa utama Eropah dan lain-lain). |
| **Rumble** | Memotong gemuruh atau resonans frekuensi rendah tanpa menipiskan keseluruhan bahagian bawah. |
| **Mud** | Menceduk lumpur low-mid untuk bunyi yang lebih bersih dan jelas. |
| **Boxy** | Membuang bunyi mid berkotak. |
| **Harsh** | Menjinakkan puncak keras yang menusuk dalam upper-mid. |

### Peaking (Jalur EQ Parametrik)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Frequency** | Pusat jalur untuk dinaikkan atau dipotong. Sapu ia untuk mencari frekuensi yang anda mahu bentuk. | 20 Hz hingga 20 kHz (1 kHz) |
| **Gain** | Berapa banyak untuk dinaikkan atau dipotong pada pusat. Positif mengangkat jalur; negatif mencedukkannya. | -15 hingga +15 dB (0) |
| **Q factor** | Menetapkan betapa luas jalur itu. Nilai rendah membentuk kawasan luas; nilai tinggi mempersempit untuk perubahan pembedahan yang tepat. | 0.1 hingga 10 (1.0) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Presence** | Peningkatan upper-mid yang luas untuk kejelasan dan kehadiran. Titik permulaan neutral. |
| **Warmth** | Peningkatan low-mid yang luas yang menambah tubuh dan kehangatan. |
| **Vocal Boost** | Mengangkat julat vokal teras untuk membawa suara ke hadapan. |
| **Cut Mud** | Menceduk lumpur low-mid berkotak untuk bunyi yang lebih bersih. |
| **Tame Harsh** | Potongan sempit untuk menjinakkan puncak keras yang menusuk. |
| **Punch** | Peningkatan rendah yang menambah pukulan dan impak pada bahagian rendah. |
| **Sub Boost** | Peningkatan dalam pada bahagian paling bawah untuk berat sub-bass tambahan. |
| **Air** | Angkat luas pada bahagian atas untuk kilauan yang terbuka dan lapang. |
| **Clarity** | Mengangkat high-mid untuk menambah definisi dan tepi. |
| **De-Ess** | Potongan sempit dalam julat sibilan untuk menjinakkan bunyi S yang keras. |
| **De-Boom** | Memotong pembinaan frekuensi rendah bergema untuk bahagian rendah yang lebih ketat. |
| **Scoop** | Cedukan julat pertengahan yang luas untuk nada tercedok dan moden. |

### Low Shelf (Kawalan Bass dan Peningkatan Bass)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Frequency** | Menetapkan sudut di bawahnya shelf mengambil kesan. Segala di bawahnya dinaikkan atau dipotong bersama. | 20 hingga 2000 Hz (200) |
| **Gain** | Berapa banyak untuk mengangkat atau menurunkan bahagian rendah. Positif menambah berat dan kehangatan; negatif menipiskannya. | -15 hingga +15 dB (0) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Warmth** | Angkat bahagian rendah yang lembut untuk kehangatan dan tubuh. Titik permulaan neutral. |
| **Bass Boost** | Peningkatan kukuh pada bass untuk berat dan pukulan. |
| **Fullness** | Mengisi low-mid untuk bunyi yang lebih penuh dan bulat. |
| **Trim Bass** | Potongan sederhana untuk meringankan campuran yang berat dengan bass. |
| **Cut Lows** | Potongan kuat untuk menipiskan atau mengurangkan gema bahagian rendah. |
| **Big Bottom** | Peningkatan bahagian rendah yang besar untuk berat dan gemuruh maksimum. |

### High Shelf (Kawalan Trebel)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Frequency** | Menetapkan sudut di atasnya shelf mengambil kesan. Segala di atasnya dinaikkan atau dipotong bersama. | 1 hingga 20 kHz (8 kHz) |
| **Gain** | Berapa banyak untuk mengangkat atau menurunkan bahagian tinggi. Positif menambah kecerahan dan udara; negatif melicinkan dan menggelapkan. | -15 hingga +15 dB (0) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Presence** | Angkat bahagian tinggi yang lembut untuk kejelasan dan perincian. Titik permulaan neutral. |
| **Air** | Membuka bahagian paling atas untuk bunyi yang lapang dan terbuka. |
| **Bright** | Peningkatan kuat untuk nada yang segar, cerah, dan ke hadapan. |
| **Soften** | Potongan sederhana untuk mengambil tepi daripada bahagian tinggi yang keras. |
| **Tame Highs** | Potongan kuat untuk menggelapkan dan melicinkan bunyi yang terlalu cerah. |
| **Sparkle** | Peningkatan bahagian atas yang besar untuk kilauan dan cahaya maksimum. |

### Soft Clip (Ketepuan Hangat)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Drive** | Menolak isyarat lebih keras ke dalam pembentuk gelombang. Jumlah rendah menambah kehangatan lembut; jumlah tinggi membulatkan puncak menjadi ketepuan tebal dan kekasaran. | 0 hingga 40 dB (0) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Warm** | Sedikit drive untuk kehangatan gaya analog yang lembut. |
| **Drive** | Ketepuan ketara yang menebalkan dan mewarnai bunyi. |
| **Crunch** | Drive berat dengan tepi rangup yang boleh didengar. |
| **Fuzz** | Distortion tebal dan berbulu. Puncak dipicit keras. |
| **Destroy** | Drive maksimum. Kekasaran agresif dan tepu sepenuhnya. |

### Bit Crusher (Lo-Fi Retro)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Bit depth** | Menetapkan berapa banyak bit menerangkan setiap sampel. Kurang bit bermakna langkah lebih kasar dan lebih banyak bunyi kuantisasi, untuk bunyi digital yang rangup dan kasar. | 1 hingga 16 bit (16) |
| **Sample rate** | Mengurangkan sampel audio. Pada seratus peratus kadar tidak disentuh; turunkannya untuk menahan setiap sampel lebih lama, menumpulkan bahagian tinggi dan menambah tepi keras yang beralias. | 1% hingga 100% (100%) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Vintage** | Penurunan halus dalam kualiti, seperti pensampel digital awal. |
| **LoFi** | Lo-fi 8-bit klasik, separuh kadar. Berbutir dan retro. |
| **Crunch** | Penghancuran lebih berat dengan tepi rangup yang boleh didengar. |
| **Gritty** | Kasar dan berkasar. Langkah antara aras adalah jelas. |
| **Destroy** | Pengurangan melampau. Keras, pecah, hampir tidak dapat dikenali. |

### Ring Modulator (Nada Metalik dan Robotik)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Carrier** | Menetapkan frekuensi nada yang isyarat didarabkan dengannya. Beberapa hertz memberikan goyangan tremolo; frekuensi lebih tinggi menambah nada tambahan metalik, seperti loceng, dan robotik. | 1 hingga 4000 Hz (440) |
| **Mix** | Mengadun bunyi yang dimodulasi dengan yang asal. Pada sifar peratus anda mendengar hanya isyarat kering; pada seratus peratus hanya nada yang dimodulasi sepenuhnya. | 0% hingga 100% (0%) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Tremolo** | Carrier yang sangat rendah menjadikannya tremolo amplitud, menggoyangkan kelantangan. |
| **Robot** | Carrier pertengahan menambah nada tambahan berdenting untuk kesan suara robot klasik. |
| **Metallic** | Nada tambahan padat dan tidak harmonik untuk nada yang keras dan metalik. |
| **Bell** | Carrier lebih tinggi memberikan dering cerah seperti loceng. |
| **Alien** | Basah penuh dengan carrier tinggi. Melampau, asing, hampir tidak dapat dikenali. |

### Tremolo (Goyangan Kelantangan)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Rate** | Menetapkan betapa cepat kelantangan berdenyut. Kadar lebih perlahan memberikan ayunan licin; kadar lebih pantas memberikan gagap pantas. | 0.1 hingga 20 Hz (5) |
| **Depth** | Menetapkan berapa banyak kelantangan menurun pada setiap denyut. Pada sifar peratus aras mantap; pada seratus peratus ia menurun sepenuhnya ke senyap. | 0% hingga 100% (0%) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Gentle** | Ayunan perlahan dan cetek. Pergerakan halus tanpa menarik perhatian. |
| **Classic** | Tremolo amp klasik: kadar sederhana dan kedalaman sederhana. |
| **Deep** | Denyut kuat dan dalam yang hampir menurun ke senyap setiap kitaran. |
| **Fast** | Kibaran pantas untuk rasa berkilauan dan gugup. |
| **Chop** | Pantas dan kedalaman penuh. Cincangan yang keras dan menggagap. |

### Delay (Echo)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Time** | Menetapkan jeda sebelum setiap echo. Masa pendek memberikan slapback ketat; masa lebih panjang menjarakkan ulangan lebih jauh. | 0.01 hingga 2 s (0.25) |
| **Feedback** | Menetapkan berapa banyak setiap echo disalurkan semula. Nilai rendah memberikan satu ulangan; nilai lebih tinggi membina siri echo yang panjang dan berlarutan. | 0 hingga 0.95 (0.4) |
| **Mix** | Mengadun echo dengan yang asal. Pada sifar peratus anda mendengar hanya isyarat kering; pada seratus peratus hanya echo. | 0% hingga 100% (0%) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Slapback** | Satu echo pendek, ketat menentang yang asal. Rockabilly dan penggandaan vokal. |
| **Echo** | Echo klasik: ulangan jelas dengan beberapa ekor berlarutan. |
| **Ping** | Ulangan pantas dan melantun yang menambah pergerakan berirama. |
| **Ambient** | Ulangan lebih panjang dan lebih lembut yang membasuh ke dalam ekor yang lapang. |
| **Dub** | Maklum balas tinggi untuk lata echo yang panjang dan dubby. |
| **Cavern** | Ulangan panjang dan dalam, seperti bunyi bergema melalui ruang yang besar. |

### Stereo Width (Sempit atau Luas)

| Kawalan | Apa yang dilakukannya | Julat (lalai) |
|---|---|---|
| **Width** | Menyempitkan atau meluaskan imej stereo. Sifar peratus runtuh ke mono, seratus peratus membiarkannya tidak disentuh, dan nilai lebih tinggi menolak sisi lebih luas. Hanya menjejaskan trek stereo pada sasaran Semua saluran. | 0% hingga 200% (100%) |

| Pratetap | Apa yang dilakukannya |
|---|---|
| **Wide** | Pelebaran lembut yang membuka imej stereo. Titik permulaan neutral. |
| **Wider** | Sebaran lebih kuat untuk medan stereo yang besar dan menyeluruh. |
| **Max** | Lebar maksimum. Sangat luas, tetapi berhati-hati dengan isu keserasian mono. |
| **Narrow** | Menarik sisi ke dalam untuk imej yang lebih ketat dan berpusat. |
| **Focused** | Hampir berpusat, dengan hanya sedikit stereo. |
| **Mono** | Runtuh sepenuhnya ke mono. Kedua-dua pembesar suara memainkan isyarat yang sama. |

## Bagaimana Semuanya Berfungsi di Sebalik Tabir (Versi Ringkas)

- **Enjin:** anda memilih satu dalam Tetapan > Pemain audio > Enjin main balik: **Standard** (sistem), **Universal** (FFmpeg), atau **Sound FX** (**enjin BASS™** daripada [Un4seen Developments](https://www.un4seen.com/)). Enjin yang anda pilih menentukan format yang dimainkan, dan kesan, penyama, dan rantaian DSP hanya berjalan dalam enjin Sound FX.
- **Format:** enjin BASS™ menambah FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, dan muzik modul (tracker) di atas format sistem dan FFmpeg.
- **Kesan:** penyama, compressor, dan kebanyakan kesan menggunakan tambahan kesan BASS™. Freeverb ialah reverb Freeverb. Chorus, Flanger, dan Distortion menggunakan kesan gaya DirectX klasik dengan kawalan mereka sendiri.
- **Penormalan Kelantangan:** peleveling kekuatan bunyi **EBU R128** langsung (standard kekuatan bunyi yang digunakan dalam penyiaran dan penstriman).
- **Crossfeed:** crossfeed **bs2b (Bauer)**, dijalankan di dalam enjin BASS™.
- **Rantaian DSP:** blok tersuai anda, digunakan dalam susunan tepat yang anda tetapkan, pada semua saluran atau hanya satu sisi.
- **Output:** anda boleh menetapkan kadar sampel, kiraan saluran, dan saiz penimbal untuk sepadan dengan peralatan anda.

Kerana semua ini berjalan secara langsung semasa muzik dimainkan, kesan:

- Berfungsi dalam **masa nyata** pada segalanya, termasuk fail awan, strim, dan muzik modul.
- **Tidak pernah mengubah atau menyimpan semula** fail anda. Matikan kesan dan yang asal kembali.
- **Mengingati tetapan anda** untuk setiap kesan.
- Boleh **dicampur dan dipadankan** secara bebas, kerana setiap satu berasingan.

## Resipi Ringkas untuk Dicuba

**Mendengar harian**

- **Lebih banyak bass, dengan bersih:** Penyama > Bass Booster, kemudian turunkan Praamplifier 1 hingga 2 dB. Atau tambah DSP Low Shelf pada Bass Boost.
- **Kelantangan sekata merentasi senarai main bercampur:** Penormalan Kelantangan > Standard, tambah Compressor > Soft.
- **Kilauan keseluruhan yang lembut:** Compressor > Transparent, tambah Penormalan Kelantangan > Light.
- **Vokal lebih jelas:** Penyama > Vocal Booster, atau blok DSP Peaking pada Vocal Boost.
- **Bunyi lebih penuh pada pembesar suara telefon kecil:** Penyama > Small Speakers.

**Fon kepala**

- **Lebih baik, kurang meletihkan pada fon kepala:** Crossfeed > Chu Moy atau Jan Meier.
- **Bunyi lebih luas pada fon kepala:** DSP Stereo Width > Wide, tambah Crossfeed > Chu Moy.
- **Betulkan rakaman 1960-an dan 1970-an yang dipan keras:** Crossfeed > Vintage Stereo.
- **Sedikit udara dan ruang:** Freeverb > Ambience, dikekalkan rendah, tambah Crossfeed > Subtle.

**Masa senyap dan audio pertuturan**

- **Mendengar senyap lewat malam:** Penormalan Kelantangan > Night, tambah Compressor > Late Night.
- **Podcast dan buku audio:** Compressor > Voice / Podcast, tambah Penyama > Spoken Word.
- **Bunyi paling kuat dan paling sekata dalam kereta yang bising:** Penormalan Kelantangan > Strong, tambah Compressor > Heavy.

**Menyelesaikan masalah**

- **Jinakkan rakaman yang keras dan cerah:** Penyama > Treble Reducer, atau blok DSP Peaking pada Tame Harsh.
- **Buang dengung elektrik:** Rantaian DSP > Notch > Mains Hum 60 (atau Mains Hum 50 di Eropah).
- **Bass lebih ketat dan bersih:** DSP High Pass > Tighten, untuk memotong bahagian rendah yang bergema.
- **Kurang gema dalam campuran yang berat dengan bass:** DSP Low Shelf > Trim Bass, atau Peaking > De-Boom.

**Kreatif dan menyeronokkan**

- **Rasa hangat dan lapang:** Freeverb > Hall, dikekalkan rendah.
- **Gitar yang seperti mimpi dan lapang:** Chorus > Wide, tambah Echo > Long.
- **Lo-fi retro:** Rantaian DSP > Bit Crusher (LoFi) ke Soft Clip (Warm).
- **Pergerakan funky pada trek elektronik:** Auto Wah > Funky, atau Phaser > Fast.
- **Sapuan pesawat jet klasik:** Flanger > Jet.

## Soalan Lazim

{{% details title="Enjin bunyi apa yang digunakan Flacbox?" closed="true" %}}
Anda memilih satu Enjin main balik dalam Tetapan > Pemain audio: Standard (enjin sistem Apple), Universal (enjin FFmpeg), atau Sound FX (enjin BASS™ daripada Un4seen Developments, un4seen.com). Enjin yang anda pilih menentukan format fail yang dimainkan. Sound FX ialah yang memainkan format tambahan seperti FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, dan muzik MOD atau tracker, dan ia adalah satu-satunya enjin yang menyediakan kesan langsung, penyama 10 jalur, dan rantaian DSP. Untuk menggunakan kesan, tetapkan Enjin main balik kepada Sound FX.
{{% /details %}}

{{% details title="Bolehkah Flacbox memainkan MOD, XM, IT, dan muzik tracker atau modul lain?" closed="true" %}}
Ya. Enjin BASS™ mempunyai pemain modul terbina dalam yang memuatkan fail MOD, XM, IT, S3M, MTM, UMX, dan MO3 dan membina semula lagu secara langsung daripada corak dan bunyi instrumennya, mengikut cara muzik tracker sepatutnya dimainkan. Pemain iPhone biasa tidak boleh melakukan ini. Kesan dan penyama berfungsi pada muzik modul juga.
{{% /details %}}

{{% details title="Adakah Flacbox menyokong fail DSD dan resolusi tinggi?" closed="true" %}}
Ya. Flacbox memainkan fail DSD (DSF dan DFF) melalui enjin BASS™ menggunakan DSD over PCM supaya ia berfungsi pada perkakasan output biasa, tambahan lagi FLAC, WavPack, Monkey's Audio (APE), Musepack, dan TrueAudio untuk main balik lossless.
{{% /details %}}

{{% details title="Apakah kesan bunyi yang ada pada Flacbox?" closed="true" %}}
Penyama 10 jalur, Penormalan Kelantangan, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate, dan Crossfeed, tambahan lagi rantaian DSP yang boleh anda bina sendiri dengan penapis, shelf, gain, soft clip, bit crusher, ring modulator, tremolo, delay, dan stereo width. Setiap satu berasingan dan boleh digabungkan dengan yang lain.
{{% /details %}}

{{% details title="Apakah pratetap itu?" closed="true" %}}
Pratetap ialah tetapan siap sedia untuk kesan. Daripada menggerakkan gelangsar sendiri, anda ketik pratetap dan bunyi berubah untuk sepadan. Setiap kesan dalam Flacbox mempunyai beberapa pratetap, dan panduan ini menyenaraikan apa yang dilakukan oleh setiap satu. Jika anda menggerakkan gelangsar selepas memilih pratetap, kesan menunjukkan 'Manual' untuk memberitahu anda ia kini menggunakan nilai anda sendiri.
{{% /details %}}

{{% details title="Bagaimana saya membuka kesan audio dalam Flacbox?" closed="true" %}}
Buka pemain Now Playing, ketik butang ⋯ (Lebih banyak tindakan), dan pilih Kesan audio. Atau pergi ke Tetapan > Pemain audio > Kesan audio. Ketik kesan, hidupkan suisnya, dan pilih pratetap, atau buka gelangsar untuk memperhalusi.
{{% /details %}}

{{% details title="Di mana penyama, dan apakah tetapan terbaik?" closed="true" %}}
Pergi ke Tetapan > Pemain audio > Penyama audio. Ia mempunyai 10 jalur dari 32 Hz hingga 16 kHz, setiap satu dari -12 hingga +12 dB, tambahan lagi Praamplifier -24 hingga +24 dB dan 22 pratetap. Untuk lebih banyak bass, gunakan Bass Booster. Untuk suara lebih jelas, gunakan Vocal Booster atau Pop. Untuk bunyi lebih cerah, gunakan Treble Booster. Kemudian laraskan jalur tunggal mengikut selera.
{{% /details %}}

{{% details title="Bagaimana saya meningkatkan bass dalam Flacbox?" closed="true" %}}
Dua cara mudah. Dalam Penyama audio, pilih Bass Booster (atau naikkan jalur 32 Hz dan 64 Hz beberapa dB). Atau, dalam Pemprosesan isyarat, tambah blok Low Shelf ditetapkan kepada Bass Boost. Dalam kedua-dua kes, turunkan Praamplifier atau tambah blok Gain 1 hingga 2 dB supaya bass kekal bersih dan tidak herot.
{{% /details %}}

{{% details title="Pratetap penyama mana yang terbaik untuk muzik saya?" closed="true" %}}
Rock dan Electronic menambah tenaga dengan bahagian rendah dan tinggi yang kuat. Acoustic, Jazz, dan Classical kekal hangat dan semula jadi. Pop dan Vocal Booster menolak suara ke hadapan. Bass Booster dan Hip-Hop menambah berat. Deep dan Loudness berbunyi lebih penuh pada kelantangan rendah. Mula dengan yang sepadan dengan genre anda, kemudian perhalusi.
{{% /details %}}

{{% details title="Apakah Penormalan Kelantangan, dan bagaimana ia berbeza daripada ReplayGain?" closed="true" %}}
Ia menjadikan setiap trek dimainkan pada kekuatan bunyi yang lebih kurang sama. Ia mengukur kekuatan bunyi sebenar menggunakan standard EBU R128 (dalam LUFS, seperti perkhidmatan penstriman) dan melaras setiap trek ke arah sasaran anda, dengan had naik maksimum. Tidak seperti ReplayGain, ia tidak memerlukan tag dalam fail anda dan berfungsi pada mana-mana sumber, secara langsung, tanpa mengubah audio. Pratetap: Light, Standard, Strong, dan Night.
{{% /details %}}

{{% details title="Apakah Crossfeed, dan patutkah saya menggunakannya?" closed="true" %}}
Crossfeed mencampurkan sedikit saluran kiri dan kanan bersama supaya fon kepala terasa lebih seperti pembesar suara sebenar dan kurang seperti bunyi tersekat di dalam kepala anda. Ia hanya untuk fon kepala, jadi matikannya untuk pembesar suara. Flacbox menggunakan kaedah bs2b (Bauer), dengan pratetap seperti Chu Moy dan Jan Meier.
{{% /details %}}

{{% details title="Apakah perbezaan antara Compressor dan Penormalan Kelantangan?" closed="true" %}}
Penormalan Kelantangan memadankan kekuatan bunyi antara lagu berbeza. Compressor meratakan bahagian kuat dan perlahan di dalam satu lagu. Ia menyelesaikan masalah berbeza dan berfungsi dengan baik bersama-sama, terutamanya di dalam kereta atau tempat yang bising.
{{% /details %}}

{{% details title="Apakah rantaian Pemprosesan isyarat (DSP)?" closed="true" %}}
Ia adalah rak yang boleh anda bina sendiri dalam Tetapan > Pemain audio > Pemprosesan isyarat. Tambah blok seperti penapis, shelf, gain, soft clip, bit crusher, ring modulator, tremolo, delay, dan stereo width, susun dalam sebarang susunan, hidupkan atau matikan setiap satu, dan halakan rantaian ke semua saluran, kiri, atau kanan. Kerana susunan penting, anda boleh mereka bentuk bunyi yang anda mahu dengan tepat.
{{% /details %}}

{{% details title="Apakah perbezaan antara Penyama, kesan, dan rantaian DSP?" closed="true" %}}
Penyama ialah kawalan nada 10 jalur yang mudah. Kesan audio ialah alat siap sedia (compressor, reverb, echo, dan sebagainya) dengan pratetap. Rantaian DSP ialah tempat anda membina susunan kesan anda sendiri daripada blok individu. Anda boleh menjalankan ketiga-tiganya pada masa yang sama.
{{% /details %}}

{{% details title="Adakah kesan mengubah atau merosakkan fail muzik saya?" closed="true" %}}
Tidak. Segalanya digunakan secara langsung semasa muzik dimainkan. Fail anda tidak pernah diubah atau disimpan semula. Matikan kesan dan bunyi asal kembali serta-merta.
{{% /details %}}

{{% details title="Bolehkah saya menggunakan lebih daripada satu kesan pada masa yang sama?" closed="true" %}}
Ya. Setiap kesan mempunyai suisnya sendiri dan tiada suis induk, jadi sebarang gabungan berfungsi. Contohnya, Penormalan Kelantangan tambah Compressor untuk mendengar yang sekata, atau Freeverb tambah Crossfeed pada fon kepala, dengan penyama di atasnya.
{{% /details %}}

{{% details title="Mengapa kawalan kesan kelabu?" closed="true" %}}
Kesan itu dimatikan. Hidupkan suisnya di bahagian atas editor untuk menggunakan kawalan. Setiap kesan mati secara lalai.
{{% /details %}}

{{% details title="Apakah maksud label Manual?" closed="true" %}}
Ia bermakna anda menggerakkan gelangsar jauh dari pratetap, jadi kesan kini menggunakan nilai tersuai anda sendiri dan bukan pratetap bernama. Setiap gelangsar mempunyai butang set semula, dan memilih pratetap sekali lagi menggantikan nilai manual anda.
{{% /details %}}

{{% details title="Bolehkah saya menyimpan dan berkongsi pratetap penyama saya?" closed="true" %}}
Ya. Selain 22 pratetap terbina dalam, anda boleh membuat sendiri, menyusun semula, dan eksport atau import ia untuk memindahkan tetapan anda ke peranti lain.
{{% /details %}}

{{% details title="Adakah kesan berfungsi dengan CarPlay, penstriman, dan main balik latar belakang?" closed="true" %}}
Ya. Kesan berjalan di dalam enjin BASS™, jadi ia dikenakan pada fail tempatan, pemacu awan, pelayan media, strim, dan muzik modul, dan ia terus berfungsi semasa CarPlay dan main balik latar belakang.
{{% /details %}}

{{% details title="Bolehkah saya menukar kualiti output audio?" closed="true" %}}
Ya. Dalam Tetapan > Pemain audio anda boleh menetapkan kadar sampel output, bilangan saluran, dan saiz penimbal untuk sepadan dengan fon kepala, pembesar suara, atau DAC anda.
{{% /details %}}

{{% details title="Apakah persediaan permulaan yang baik untuk fon kepala?" closed="true" %}}
Hidupkan Penormalan Kelantangan (Standard), tambah Compressor ringan (Soft), pilih pratetap penyama yang anda suka, dan hidupkan Crossfeed (Chu Moy atau Jan Meier). Biarkan reverb, echo, dan distortion mati melainkan anda mahu bunyi kreatif.
{{% /details %}}

---

*BASS ialah tanda dagangan Un4seen Developments Ltd. Lihat [un4seen.com](https://www.un4seen.com/). Crossfeed menggunakan algoritma bs2b (Bauer stereophonic-to-binaural); lihat [halaman projek bs2b](https://bs2b.sourceforge.net/).*
