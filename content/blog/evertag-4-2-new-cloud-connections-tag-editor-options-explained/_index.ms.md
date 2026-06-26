---
title: "Evertag 4.2: sambungan awan baharu, tetapan editor tag dijelaskan"
date: 2026-05-09
description: "Evertag 4.2 menambah sambungan ke Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP dan NFS, menyegarkan Wi-Fi Drive serta mengemas kini antara muka untuk Liquid Glass. Catatan ini juga menerangkan setiap tetapan editor tag — termasuk ID3v2.4 vs ID3v2.3, penskalaan kulit album, penduaan tag, mod muat naik awan, serta pilihan yang betul untuk Spotify dan perkhidmatan penstriman lain."
keywords: ["Evertag 4.2", "kemas kini Evertag", "editor tag ID3 iPhone", "ID3v2.4 vs ID3v2.3", "edit tag FLAC iOS", "edit tag MP3 iPhone", "edit kulit album iOS", "editor tag untuk Spotify", "editor tag Plex", "editor tag Apple Music", "editor tag awan Evertag", "editor tag Internxt", "editor tag Proton Drive", "editor tag QNAP", "editor tag Nextcloud", "editor tag Amazon S3", "editor tag SFTP iPhone", "editor tag audio FTP", "editor tag NFS iPhone", "Wi-Fi Drive editor tag", "duplikasi tag ID3", "penskalaan kulit album", "reka bentuk Liquid Glass", "editor metadata audio iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Editor tag", "ID3", "ID3v2.4", "ID3v2.3", "Tag FLAC", "Tag MP3", "Kulit album", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Apa yang baru"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**Ringkasan:** [Evertag 4.2](/products/evertag) ialah kemas kini besar untuk editor tag audio pada iPhone, iPad dan Mac. Kami menyelesaikan pepijat utama dalam penyuntingan tag dan menambah lebih daripada 6 sambungan awan dan pelayan baharu — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, serta protokol **FTP**, **SFTP** dan **NFS**. Wi-Fi Drive memperoleh antara muka segar, mod pemilihan berbilang, baris gilir muat naik yang lebih bijak dan pemindahan yang lebih pantas. Keseluruhan aplikasi telah diselaraskan untuk reka bentuk **Liquid Glass**. Catatan ini juga mendalami tetapan editor tag Evertag — menerangkan **ID3v2.4 vs ID3v2.3**, **penskalaan kulit album**, **penduaan tag**, **mod muat naik awan**, **memadam fail yang dimuat turun**, dan tepatnya pilihan mana yang patut anda pilih jika sedang menyediakan audio untuk **Spotify**, **Apple Music**, **Plex**, **Jellyfin** atau mana-mana perkhidmatan penstriman lain.

---

## Helo semua!

Kemas kini besar Evertag tiba. Kami menyelesaikan pepijat utama dalam penyuntingan tag dan menambah **lebih daripada 6 sambungan awan dan pelayan baharu** untuk menjadikan pengurusan metadata audio anda lebih mudah berbanding sebelum ini — sama ada perpustakaan anda berada di awan yang mengutamakan privasi, NAS yang anda hos sendiri, atau pelayan FTP/SFTP/NFS am.

[Muat turun Evertag 4.2 dari App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) atau kemas kini daripada versi sedia ada anda.

## Sokongan awan dan pelayan yang diperluaskan

Evertag kini menyambung secara native kepada lebih banyak pilihan storan awan dan storan yang dihos sendiri. Anda boleh menyunting tag ID3, MP4, FLAC, OGG dan APE pada fail di mana sahaja ia berada.

### Storan awan tertumpu privasi: Internxt dan Proton Drive

Jika anda mementingkan penyulitan hujung ke hujung dan storan tanpa pengetahuan, dua nama paling dihormati dalam awan keutamaan privasi kini disokong secara asli dalam Evertag:

- **Internxt** — awan Sepanyol sumber terbuka, disulitkan pasca-kuantum dan mematuhi GDPR. Tahap percuma tersedia.
- **Proton Drive** — storan disulitkan hujung ke hujung daripada pencipta Proton Mail dan Proton VPN, beribu pejabat di Switzerland. Tahap percuma tersedia, dengan pelan berbayar untuk perpustakaan yang lebih besar.

Kini anda boleh menyunting metadata terus pada fail audio yang disimpan dalam mana-mana perkhidmatan tersebut — fail kekal disulitkan semasa transit, dan hanya tag baharu yang ditulis semula.

### Penyelesaian dihos sendiri: QNAP, Nextcloud, Amazon S3

Untuk pengguna yang mengendalikan infrastruktur sendiri:

- **QNAP** — sambungan API asli ke peranti QNAP NAS. Sunting tag pada fail di QNAP anda melalui Wi-Fi tempatan atau akses jauh.
- **Nextcloud** — sambung kepada mana-mana instans Nextcloud, sama ada dihos sendiri atau diuruskan.
- **Amazon S3** — arahkan Evertag ke mana-mana baldi S3 (atau storan serasi S3 seperti Backblaze B2, Wasabi, MinIO, Cloudflare R2) dan sunting metadata di tempatnya.

### Protokol rangkaian baharu: FTP, SFTP, NFS

Evertag 4.2 menambah tiga protokol klasik untuk pengguna yang mempunyai pelayan tersuai, makmal rumah atau NAS am:

- **SFTP (SSH File Transfer Protocol)** — jawapan yang tepat untuk **penyuntingan tag jarak jauh yang selamat dari pelayan anda sendiri**. SFTP berjalan di atas SSH, jadi keseluruhan pemindahan (pengesahan dan data audio) disulitkan. Jika anda mempunyai VPS, pelayan khusus atau mesin Linux di rumah dengan akses SSH, anda boleh menyunting tag pada fail jauh tanpa mendedahkan apa-apa lagi. Menyokong pengesahan kata laluan dan kunci.
- **FTP** — standard yang lama kukuh untuk pemindahan fail. Berguna untuk NAS rumah lama yang mendedahkan FTP tetapi tidak mempunyai integrasi API asli.
- **NFS (Sistem Fail Rangkaian)** — protokol perkongsian de facto pada Linux dan kebanyakan peranti NAS. Beban lebih rendah daripada SMB pada perkakasan yang sama.

> **Petua:** SFTP ialah protokol yang anda mahukan untuk penyuntingan jarak jauh melalui Internet terbuka. FTP dan NFS lebih sesuai dalam rangkaian tempatan — jangan dedahkan ke Internet melainkan ia dibalut dalam VPN.

## Naik taraf Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) ialah ciri terbina dalam Evertag untuk **memindahkan fail audio tanpa wayar antara komputer anda dan iPhone atau iPad — tanpa iTunes, tanpa kabel dan tanpa akaun awan**. Kedua-dua peranti mesti berada pada rangkaian Wi-Fi yang sama.

Dalam Evertag 4.2, Wi-Fi Drive memperoleh:

- **Antara muka segar dan moden** — lebih kemas, lebih mudah dibaca sekali pandang dan dikemas kini untuk Liquid Glass.
- **Mod pemilihan berbilang** — pilih beberapa fail atau folder dan bertindak ke atasnya secara pukal.
- **Baris gilir muat naik lebih bijak** — maklum balas kemajuan yang lebih baik dan lebih tahan terhadap gangguan rangkaian.
- **Kelajuan dan kebolehpercayaan keseluruhan dipertingkat** — pemindahan lebih pantas untuk perpustakaan besar.

Ia adalah cara terpantas untuk memindahkan kelompok fail audio dari komputer ke telefon anda, menyunting tagnya dan menghantarnya kembali — tanpa sebarang perkhidmatan pihak ketiga.

## Tetapan editor tag: penelitian mendalam

Inilah bahagian yang kebanyakan pengguna tidak pernah baca — dan bahagian yang menentukan sama ada tag anda berfungsi di mana-mana atau hanya dalam sesetengah aplikasi. Buka Evertag, kemudian pergi ke bahagian **tetapan editor tag audio**. Berikut ialah apa yang sebenarnya dilakukan oleh setiap pilihan dan pilihan mana yang patut anda gunakan mengikut matlamat.

### Penskalaan kulit album

Apabila anda menyimpan kulit album ke dalam fail audio, Evertag boleh menskala imej sebelum menyemat. Pilihan yang ada:

- **Kecil** — kesan paling kecil pada saiz fail, kualiti imej lebih rendah.
- **Sederhana** — pilihan seimbang untuk kebanyakan pengguna.
- **Besar** — kualiti tinggi, sesuai untuk pemain skrin besar dan CarPlay.
- **Ekstra besar** — kualiti sangat tinggi, peningkatan saiz fail yang ketara.
- **Asli (Dilumpuhkan)** — menyemat kulit pada resolusi asli. **Tiada penskalaan langsung.**

**Mengapa ini penting:**

- **Kualiti lebih tinggi = fail lebih besar.** Kulit 3,000 × 3,000 piksel boleh menambah beberapa MB pada setiap trek. Darab dengan satu album penuh dan kos cakera meningkat dengan cepat.
- **Sesetengah pemain tidak mengendalikan imej terbenam yang sangat besar dengan baik.** Peranti lama, sesetengah unit kepala kereta, dan beberapa pemain desktop legasi boleh tersangkut pada kulit melebihi ~1,500 piks atau enggan memaparkannya.
- **Untuk kebanyakan aliran kerja awan dan penstriman**, **Sederhana** atau **Besar** adalah titik manis. Gunakan **Asli** hanya apabila anda benar-benar memerlukan kualiti arkib atau menyediakan fail untuk pemain yang anda yakin akan mengendalikannya.

> Pilihan saiz **Asli** adalah sebahagian daripada peningkatan personalisasi premium Evertag. Saiz piawai (Kecil/Sederhana/Besar/Ekstra besar) adalah percuma.

### Pilihan simpanan tag: ID3v2.4 vs ID3v2.3

Inilah tetapan tunggal yang paling penting untuk keserasian. ID3v2 ialah format metadata yang digunakan dalam fail MP3. Terdapat dua versi yang digunakan secara meluas, dan ia berbeza dalam butiran yang halus tetapi penting.

#### ID3v2.4

- Lebih baharu, menyokong **pengekodan teks UTF-8** — pengendalian tepat untuk skrip bukan-Latin (Cina, Rusia, Jepun, Arab, Ibrani, dsb.).
- Lebih banyak jenis bingkai (kelantangan relatif, prasetel penyamai, dsb.).
- **Disyorkan untuk pemain moden** yang menyokongnya.

#### ID3v2.3

- Lebih lama tetapi **versi ID3 paling disokong secara universal**.
- Tidak menyokong UTF-8 secara langsung (menggunakan UTF-16 untuk teks Unicode).
- **Disyorkan apabila anda perlukan keserasian maksimum** dengan pemain lama, stereo kereta dan sesetengah aplikasi desktop.

#### Bila perlu mengaktifkan ID3v2.4 dalam Evertag

- Anda menggunakan **pemain audio moden** seperti Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (versi semasa) atau pemain Android moden. ✅ **Hidupkan ID3v2.4.**
- Perpustakaan anda mengandungi **aksara bukan-Latin** (Cina, Korea, Jepun, Rusia, Arab, Yunani, Ibrani). ✅ **Hidupkan ID3v2.4** — UTF-8 mengendalikannya jauh lebih bersih.

#### Bila perlu menyahaktifkan ID3v2.4 dalam Evertag (gunakan ID3v2.3)

- Anda menyediakan fail untuk **stereo kereta atau unit papan pemuka yang lebih lama** yang tidak membaca tag v2.4.
- Anda nampak **teks bercelaru atau tag hilang** dalam sesetengah aplikasi selepas penyuntingan — itu petanda kuat bahawa v2.4 tidak disokong di sana. Beralih semula ke v2.3.
- Anda menyasarkan **pemain desktop legasi** atau pemain mudah alih lama (iPod awal, sesetengah pemain MP3 dari era 2000–2010).

> **Peraturan praktikal:** jika tag anda dipaparkan dengan betul di mana-mana dengan v2.4, biarkan ia hidup. Jika walau satu pemain penting menunjukkan aksara salah, kosong atau gagal membaca tag, matikan v2.4 dan simpan semula.

#### Penduaan tag

Apabila anda mengaktifkan **Penduaan tag**, Evertag menulis medan metadata umum (tajuk, artis, album, dsb.) ke dalam **kedua-dua bahagian ID3v1 dan ID3v2** fail. Ini meningkatkan keserasian dengan pemain yang sangat lama yang hanya membaca ID3v1 (tag asal 128-bait di hujung fail).

- **Kebanyakan pengguna tidak memerlukannya.** Pemain moden membaca ID3v2 dahulu.
- **Aktifkan hanya jika** anda berurusan dengan perkakasan vintaj atau perisian khusus yang mengabaikan ID3v2.

### Mengemas kini fail dalam talian: bagaimana Evertag mengendalikan suntingan awan

Apabila anda menyunting tag pada fail yang disimpan di awan tersambung (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP, dll.), Evertag perlu memuat naik fail yang diubah suai semula. Anda mengawal cara ini berlaku:

- **Tunjukkan mesej pengesahan** *(lalai, disyorkan)* — Evertag bertanya sebelum memuat naik. Terbaik untuk pengguna berhati-hati dan perpustakaan dikongsi.
- **Kemas kini metadata fail secara automatik** — memuat naik dengan senyap selepas setiap suntingan. Terbaik untuk pengguna solo dengan sambungan pantas dan boleh dipercayai yang banyak menyunting.
- **Jangan kemas kini metadata fail** — Evertag hanya menyunting salinan tempatan. Berguna untuk pratonton perubahan tanpa mendorongnya ke awan.

### Menyunting fail dalam talian: pembersihan fail tempatan

Untuk menyunting fail jauh, Evertag memuat turunnya ke peranti anda dahulu. Selepas penyuntingan, anda memilih apa yang berlaku kepada salinan tempatan itu:

- **Sentiasa padam fail yang dimuat turun** — Evertag mengeluarkan fail sementara selepas penyuntingan. **Disyorkan** jika ruang storan terhad atau anda bekerja pada fail orang lain.
- **Jangan padam fail yang dimuat turun** — mengekalkan fail yang disunting pada peranti anda. Berguna jika anda mahu kedua-dua salinan luar talian dan salinan awan yang dikemas kini.

### Butang pada skrin utama

Skrin utama editor tag Evertag boleh menunjukkan atau menyembunyikan butang untuk operasi individu. Aktifkan hanya yang anda gunakan secara sebenar bagi memastikan UI kekal fokus:

- **Cari tag audio secara automatik** — mencari metadata yang hilang dalam talian berdasarkan cap jari audio fail.
- **Cari tag audio secara manual** — cari mengikut tajuk/artis apabila pencarian automatik tergelincir.
- **Cari kulit album** — mencari dan menyemat kulit berkualiti tinggi.
- **Simpan kulit album** — mengeksport kulit terbenam ke perpustakaan foto atau fail anda.
- **Normalkan pengekodan** — membetulkan teks bukan-Latin yang bercelaru akibat pengekodan lama (sangat berguna untuk trek Cyril, Cina dan Jepun yang dirip dengan perisian legasi).
- **Padam tag audio** — mengeluarkan semua tag dari fail. Berguna sebelum tag semula yang bersih.

### Tunjukkan tag lanjutan

Aktifkan ini untuk memaparkan keseluruhan medan metadata melebihi tajuk/artis/album/tahun asas — termasuk BPM, konduktor, artis asal, mood, hak cipta, pengekod, ulasan, lirik dan banyak lagi. Ciri pengguna mahir; kebanyakan pengguna santai tidak memerlukannya.

### Sunting fail serentak

Apabila diaktifkan, Evertag membenarkan anda menyunting metadata pada **beberapa fail terpilih sekali gus** — tetapkan album artist, tahun atau genre yang sama untuk seluruh album dalam satu operasi. Ini cara terpantas untuk membersihkan perpustakaan besar yang tidak teratur.

## Menyunting tag untuk Spotify, Apple Music dan platform penstriman

Soalan biasa: «saya menyunting tag dalam Evertag, memuat naik fail, dan perkhidmatan penstriman menunjukkan metadata yang salah. Apa cerita?»

Jawapan ringkas: **perkhidmatan penstriman tidak selalu menghormati tag tempatan anda.** Apple Music dan Spotify mempunyai pangkalan data dalaman sendiri — apabila mereka mengenali sesuatu trek, mereka menulis ganti metadata yang dipaparkan dengan milik mereka. Tetapi untuk **fail yang dimuat naik**, fail tempatan anda (ciri «Pustaka» Apple Music, Spotify Local Files), dan **muat naik pengedar ke platform penstriman**, tag anda benar-benar penting. Berikut ialah cara menetapkan Evertag untuk setiap senario:

### Menyediakan fail untuk Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music mengendalikan UTF-8 dengan betul.
- **Kulit album: Besar** — aplikasi Apple memaparkan kulit besar dengan baik; Asli adalah berlebihan.
- **Penduaan tag: OFF** — tidak diperlukan.
- Pastikan **Album Artist** diisi dengan betul — Apple Music menggunakannya untuk pengelompokan.

### Menyediakan fail untuk Spotify Local Files

Spotify Local Files hanya memaparkan fail yang ditandai dengan baik. Tag yang Spotify baca adalah terhad.

- **ID3v2.4: ON** dalam kebanyakan kes. Jika trek tidak muncul dengan betul dalam Spotify selepas penyuntingan, **cuba simpan dengan ID3v2.4: OFF** (iaitu sebagai ID3v2.3) — penghurai Spotify secara sejarah konservatif terhadap v2.4.
- **Kulit album: Sederhana atau Besar** — Spotify tetap menskalanya semula.
- Isi sekurang-kurangnya **Tajuk**, **Artis**, **Album** dan **Nombor trek**.

### Menyediakan fail untuk muat naik pengedar (DistroKid, TuneCore, CD Baby, dsb.)

Jika anda artis yang memuat naik kerja sendiri ke platform penstriman, pengedar anda biasanya membaca tag tetapi juga meminta metadata dalam UI mereka. Apa pun:

- **ID3v2.3** sering kali pilihan lalai yang lebih selamat — banyak saluran paip pengedar dibina bertahun-tahun lalu dan lebih suka format lama.
- Sematkan kulit **Besar** (kebanyakan pengedar memerlukan kulit ≥ 1,400 × 1,400 piks — semak garis panduan mereka).
- Jangan bergantung pada tag lanjutan — pengedar hanya membaca medan teras.

### Menyediakan fail untuk Plex, Jellyfin, Navidrome, Subsonic, Emby

Pelayan media dihos sendiri ini sangat bertolak ansur. Mereka membaca v2.3 dan v2.4 dengan bersih dan mengendalikan UTF-8 dengan baik.

- **ID3v2.4: ON** boleh diterima.
- **Kulit album: Besar** atau **Ekstra besar** — pelayan ini menyajikan kulit kepada klien mudah alih dan skrin CarPlay, jadi kualiti penting.
- **Album Artist** sangat disyorkan — itulah yang Plex/Jellyfin gunakan untuk mengelompokkan album mengikut artis dengan betul.

### Menyediakan fail untuk stereo kereta dan perkakasan lebih lama

- **ID3v2.4: OFF** (gunakan ID3v2.3) — unit kepala lebih lama selalunya tidak menyokong v2.4.
- **Kulit album: Sederhana** — banyak paparan kereta tersangkut pada kulit terbenam yang besar.
- **Penduaan tag: ON** — stereo kereta lama kadang-kadang hanya membaca sandaran ID3v1.

## Penambahbaikan lain

### Reka bentuk Liquid Glass

Antara muka Evertag 4.2 diselaraskan untuk bahan **Liquid Glass** baharu Apple di seluruh aplikasi — permukaan separa lutsinar, animasi yang lebih lancar dan kawalan halus yang muat secara semula jadi dalam iOS, iPadOS dan macOS.

### Pustaka sambungan dikemas kini

Kami menyegarkan pustaka dalaman yang Evertag gunakan untuk berkomunikasi dengan **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** dan perkhidmatan lain. Hasilnya: kurang kegagalan sambungan dalam kes pinggir, sokongan lebih baik untuk versi pelayan terkini dan kebolehpercayaan lebih tinggi semasa menyunting tag pada fail jauh.

### Pembetulan terjemahan dan penyetempatan

Pembetulan bahasa berbilang dalam UI berdasarkan maklum balas langsung pengguna. Penjajaran teks lebih baik pada butang kecil dalam beberapa bahasa.

### Penyempurnaan kecil yang diilhamkan oleh maklum balas anda

Banyak penambahbaikan kecil berdasarkan ulasan App Store dan e-mel ke support@everappz.com. Kami membaca setiap mesej.

## Dapatkan Evertag 4.2

[**Muat turun Evertag dari App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) atau kemas kini melalui App Store. Evertag ialah muat turun percuma dengan naik taraf dalam aplikasi pilihan untuk ciri lanjutan. Sambungan awan baharu, protokol rangkaian, penambahbaikan Wi-Fi Drive dan UI Liquid Glass adalah sebahagian daripada kemas kini asas.

Jika anda menyukai aplikasi ini, sila tinggalkan penilaian di App Store — ia benar-benar membantu. Ada maklum balas atau menghadapi masalah? E-melkan kami di **support@everappz.com**. Kami membaca setiap mesej.

## Soalan Lazim

{{% details title="Apa yang baru dalam Evertag 4.2?" closed="true" %}}
Evertag 4.2 menambah lebih daripada 6 sambungan awan dan pelayan baharu (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), Wi-Fi Drive yang disegarkan dengan pemilihan berbilang dan baris gilir muat naik yang lebih bijak, kemas kini UI Liquid Glass, pustaka sambungan dikemas kini, pembetulan pepijat utama dalam penyuntingan tag dan penambahbaikan terjemahan.
{{% /details %}}

{{% details title="Saya patut gunakan ID3v2.4 atau ID3v2.3 dalam Evertag?" closed="true" %}}
Gunakan **ID3v2.4** untuk pemain moden (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, aplikasi Android moden) dan untuk perpustakaan dengan aksara bukan-Latin — sokongan UTF-8 bermaksud tag Cina, Korea, Jepun, Rusia, Arab dan Ibrani lebih bersih. Gunakan **ID3v2.3** jika tag anda dipaparkan dengan salah dalam sesetengah aplikasi, jika anda menyasarkan stereo kereta lebih lama, atau jika saluran paip pengedar penstriman menolak v2.4. Anda boleh sentiasa beralih dan simpan semula.
{{% /details %}}

{{% details title="Mengapa tag saya salah dalam Spotify selepas penyuntingan?" closed="true" %}}
Spotify kebanyakannya memaparkan metadata daripada katalog mereka sendiri — tag tempatan anda hanya digunakan untuk «Local Files» atau kandungan yang anda muat naik sebagai artis. Jika anda menandai fail untuk Spotify Local Files dan ia tidak dipaparkan dengan betul, cuba lumpuhkan ID3v2.4 dalam Evertag dan simpan sebagai ID3v2.3 — penghurai Spotify secara sejarah konservatif terhadap v2.4.
{{% /details %}}

{{% details title="Saiz kulit album mana yang patut saya pilih dalam Evertag?" closed="true" %}}
Untuk kebanyakan pengguna: **Besar**. Kelihatan hebat pada telefon, iPad, Mac dan paparan kereta moden tanpa membengkakkan fail terlalu banyak. Gunakan **Sederhana** jika anda mempunyai perpustakaan yang besar dan mahu menjimatkan cakera. Gunakan **Asli** (tanpa penskalaan) hanya untuk master arkib atau apabila anda benar-benar memerlukan kualiti maksimum — tetapi ambil maklum bahawa sesetengah pemain lebih lama bergelut dengan kulit terbenam yang sangat besar. **Asli** adalah sebahagian daripada peningkatan personalisasi premium Evertag.
{{% /details %}}

{{% details title="Adakah kulit album yang lebih besar menjadikan fail saya lebih besar?" closed="true" %}}
Ya. Membenamkan kulit 3,000 × 3,000 piks boleh menambah beberapa megabait pada satu fail audio. Pada perpustakaan 1,000 trek, ia mencapai gigabait. Jika storan terhad, gunakan Sederhana atau Besar; jika anda menstrim daripada NAS yang saiznya tidak penting, Ekstra besar atau Asli boleh.
{{% /details %}}

{{% details title="Apakah Penduaan tag dan patutkah saya mengaktifkannya?" closed="true" %}}
Penduaan tag menulis metadata teras pada bahagian ID3v1 (warisan 128-bait) dan ID3v2 (moden) fail. Aktifkan hanya jika anda menyasarkan pemain yang sangat lama atau perkakasan yang membaca ID3v1. Untuk semua yang moden (telefon pintar, komputer, stereo kereta terkini), biarkan dimatikan.
{{% /details %}}

{{% details title="Adakah Evertag menyunting tag terus pada fail awan?" closed="true" %}}
Ya. Sambung ke awan anda (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, dll.) atau melalui FTP/SFTP/NFS, kemudian buka fail dan sunting tag seolah-olah ia tempatan. Evertag memuat turun fail, menggunakan suntingan anda dan memuat naik versi dikemas kini semula. Anda boleh memilih antara mod «Sentiasa tanya», «Auto-muat naik» atau «Jangan muat naik» dalam tetapan.
{{% /details %}}

{{% details title="Bolehkah saya menyunting tag FLAC pada iPhone dengan Evertag?" closed="true" %}}
Boleh. Evertag menyokong FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE dan format penting lain dengan sokongan baca/tulis tag penuh termasuk kulit terbenam.
{{% /details %}}

{{% details title="Bagaimana saya menyunting tag dengan selamat pada pelayan rumah saya dengan SFTP?" closed="true" %}}
Buka Evertag, pergi ke Connections, pilih SFTP dan masukkan nama hos atau IP pelayan, port (biasanya 22), nama pengguna dan kata laluan atau kunci peribadi SSH. Evertag akan menyemak imbas folder jauh anda dan menyunting tag terus dengan penyulitan hujung ke hujung melalui SSH.
{{% /details %}}

{{% details title="Bolehkah saya menyunting tag pada beberapa fail sekali gus?" closed="true" %}}
Boleh. Aktifkan **Sunting fail serentak** dalam tetapan. Pilih beberapa fail, buka editor tag dan sebarang medan yang anda ubah akan dikenakan pada semua fail terpilih. Inilah cara terpantas menetapkan album artist, tahun atau genre yang sama merentasi seluruh album.
{{% /details %}}

{{% details title="Adakah kemas kini ke Evertag 4.2 percuma?" closed="true" %}}
Ya. Evertag ialah muat turun percuma dari App Store dan 4.2 ialah kemas kini percuma untuk semua pengguna sedia ada. Integrasi awan baharu, penambahbaikan Wi-Fi Drive dan UI Liquid Glass adalah sebahagian daripada kemas kini asas.
{{% /details %}}

{{% details title="Pada peranti apa Evertag 4.2 tersedia?" closed="true" %}}
Evertag 4.2 berjalan pada iPhone, iPad dan Mac. Penyegerakan iCloud Drive memastikan tetapan editor tag anda kekal konsisten merentasi peranti.
{{% /details %}}
