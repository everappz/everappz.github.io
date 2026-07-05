---
title: "Evertag 4.2: koneksi cloud baru, pengaturan editor tag dijelaskan"
date: 2026-05-09
description: "Evertag 4.2 menambahkan koneksi ke Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, dan NFS, menyegarkan Wi-Fi Drive, dan memperbarui antarmuka untuk Liquid Glass. Postingan ini juga menjelaskan setiap pengaturan editor tag — termasuk ID3v2.4 vs ID3v2.3, penskalaan sampul album, duplikasi tag, mode unggah cloud, dan opsi yang tepat untuk Spotify dan layanan streaming lainnya."
keywords: ["Evertag 4.2", "pembaruan Evertag", "editor tag ID3 iPhone", "ID3v2.4 vs ID3v2.3", "edit tag FLAC iOS", "edit tag MP3 iPhone", "edit sampul album iOS", "editor tag untuk Spotify", "editor tag Plex", "editor tag Apple Music", "editor tag cloud Evertag", "editor tag Internxt", "editor tag Proton Drive", "editor tag QNAP", "editor tag Nextcloud", "editor tag Amazon S3", "editor tag SFTP iPhone", "editor tag audio FTP", "editor tag NFS iPhone", "Wi-Fi Drive editor tag", "duplikat tag ID3", "penskalaan sampul album", "desain Liquid Glass", "editor metadata audio iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Editor tag", "ID3", "ID3v2.4", "ID3v2.3", "Tag FLAC", "Tag MP3", "Sampul album", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Apa yang baru"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evertag 4.2](/products/evertag) adalah pembaruan besar untuk editor tag audio di iPhone, iPad, dan Mac. Kami memperbaiki bug penyuntingan tag yang penting dan menambahkan 6+ koneksi cloud dan server baru — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, plus protokol **FTP**, **SFTP**, dan **NFS**. Wi-Fi Drive memperoleh antarmuka yang disegarkan, mode pilih banyak, antrean unggah yang lebih pintar, dan transfer yang lebih cepat. Seluruh aplikasi disesuaikan untuk desain **Liquid Glass**. Postingan ini juga membahas mendalam pengaturan editor tag Evertag — menjelaskan **ID3v2.4 vs ID3v2.3**, **penskalaan sampul album**, **duplikasi tag**, **mode unggah cloud**, **menghapus berkas yang diunduh**, dan tepatnya opsi mana yang harus dipilih jika Anda menyiapkan audio untuk **Spotify**, **Apple Music**, **Plex**, **Jellyfin**, atau layanan streaming lainnya.

---

## Halo semua!

Pembaruan besar Evertag hadir. Kami memperbaiki bug penyuntingan tag yang penting dan menambahkan **6+ koneksi cloud dan server baru** untuk membuat pengelolaan metadata audio lebih mudah dari sebelumnya — baik perpustakaan Anda berada di cloud yang fokus privasi, NAS yang dihos sendiri, atau server FTP/SFTP/NFS generik.

[Unduh Evertag 4.2 dari App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) atau perbarui dari versi Anda saat ini.

## Dukungan cloud dan server yang diperluas

Evertag kini terhubung secara native ke berbagai opsi cloud dan penyimpanan yang dihos sendiri yang lebih luas. Anda dapat mengedit tag ID3, MP4, FLAC, OGG, dan APE pada berkas di mana pun.

### Penyimpanan cloud yang fokus pada privasi: Internxt dan Proton Drive

Jika Anda peduli pada enkripsi ujung-ke-ujung dan penyimpanan tanpa pengetahuan, dua nama paling dihormati di kategori cloud privasi-utama kini hadir secara native di Evertag:

- **Internxt** — cloud Spanyol open-source, terenkripsi pasca-kuantum, dan patuh GDPR. Tersedia tier gratis.
- **Proton Drive** — penyimpanan terenkripsi ujung-ke-ujung dari pembuat Proton Mail dan Proton VPN, berbasis di Swiss. Tersedia tier gratis, dengan paket berbayar untuk perpustakaan yang lebih besar.

Kini Anda dapat mengedit metadata langsung pada berkas audio yang disimpan di salah satu layanan tersebut — berkas tetap terenkripsi saat transit, dan hanya tag baru yang ditulis kembali.

### Solusi self-hosted: QNAP, Nextcloud, Amazon S3

Untuk pengguna yang menjalankan infrastruktur sendiri:

- **QNAP** — koneksi API native ke perangkat QNAP NAS. Edit tag pada berkas di QNAP Anda melalui Wi-Fi lokal atau akses jarak jauh.
- **Nextcloud** — terhubung ke instance Nextcloud apa pun, baik self-hosted maupun terkelola.
- **Amazon S3** — arahkan Evertag ke bucket S3 mana pun (atau penyimpanan kompatibel S3 seperti Backblaze B2, Wasabi, MinIO, Cloudflare R2) dan edit metadata di tempat.

### Protokol jaringan baru: FTP, SFTP, NFS

Untuk pengguna dengan server kustom, homelab, atau NAS generik tanpa aplikasi mobile yang dipoles, Evertag 4.2 menambahkan tiga protokol klasik:

- **SFTP (SSH File Transfer Protocol)** — jawaban yang tepat untuk **penyuntingan tag jarak jauh yang aman dari server Anda sendiri**. SFTP berjalan di atas SSH, sehingga seluruh transfer (autentikasi dan data audio) dienkripsi. Jika Anda punya VPS, server dedicated, atau mesin Linux di rumah dengan akses SSH, Anda dapat mengedit tag pada berkas jarak jauh tanpa membuka apa pun yang lain. Mendukung autentikasi password maupun kunci.
- **FTP** — standar lama untuk transfer berkas. Berguna untuk NAS rumah lama yang membuka FTP tetapi tanpa integrasi API native.
- **NFS (Network File System)** — protokol berbagi de facto pada Linux dan kebanyakan NAS. Beban lebih rendah dibandingkan SMB pada perangkat keras yang sama.

> **Tip:** SFTP adalah protokol yang Anda inginkan untuk penyuntingan jarak jauh melalui internet terbuka. FTP dan NFS paling baik digunakan di jaringan lokal — jangan ekspos ke internet kecuali dibungkus VPN.

## Peningkatan Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) adalah fitur bawaan Evertag untuk **memindahkan berkas audio secara nirkabel antara komputer Anda dan iPhone atau iPad — tanpa iTunes, tanpa kabel, tanpa akun cloud**. Kedua perangkat harus berada di jaringan Wi-Fi yang sama.

Pada Evertag 4.2, Wi-Fi Drive mendapatkan:

- **Antarmuka modern yang disegarkan** — lebih bersih, lebih mudah dibaca sekilas, dan diperbarui untuk Liquid Glass.
- **Mode pilih banyak** — pilih beberapa berkas atau folder dan tindak secara massal.
- **Antrean unggah lebih pintar** — feedback progres lebih jelas dan tahan terhadap gangguan jaringan.
- **Kecepatan dan keandalan keseluruhan ditingkatkan** — transfer lebih cepat untuk perpustakaan besar.

Ini adalah cara tercepat memindahkan sekelompok berkas audio dari komputer ke ponsel, mengedit tag-nya, dan mengembalikannya — tanpa layanan pihak ketiga apa pun.

## Pengaturan editor tag: telaah mendalam

Ini adalah bagian yang sebagian besar pengguna tidak pernah baca — dan bagian yang menentukan apakah tag Anda berfungsi di mana saja atau hanya di beberapa aplikasi. Buka Evertag, lalu buka bagian **pengaturan editor tag audio**. Berikut yang sebenarnya dilakukan setiap opsi, dan opsi mana yang harus dipilih sesuai tujuan Anda.

### Penskalaan sampul album

Ketika Anda menyimpan sampul album ke dalam berkas audio, Evertag dapat menskalakan gambar sebelum menyematkannya. Opsi yang tersedia:

- **Kecil** — dampak terkecil pada ukuran berkas, kualitas gambar lebih rendah.
- **Sedang** — pilihan seimbang untuk sebagian besar pengguna.
- **Besar** — kualitas tinggi, cocok untuk pemutar layar besar dan CarPlay.
- **Sangat besar** — kualitas sangat tinggi, peningkatan ukuran berkas yang nyata.
- **Asli (Dinonaktifkan)** — menyematkan sampul pada resolusi asli. **Tanpa penskalaan.**

**Mengapa hal ini penting:**

- **Kualitas lebih tinggi = berkas lebih besar.** Sampul 3.000 × 3.000 piksel dapat menambah beberapa MB ke setiap track. Kalikan dengan satu album dan beban disk meningkat dengan cepat.
- **Beberapa pemutar tidak menangani gambar tertanam yang sangat besar dengan baik.** Perangkat lebih lama, beberapa head unit mobil, dan beberapa pemutar desktop legacy dapat tersangkut pada sampul di atas ~1.500 px atau menolak menampilkannya.
- **Untuk sebagian besar alur kerja cloud dan streaming**, **Sedang** atau **Besar** adalah titik manis. Gunakan **Asli** hanya bila Anda secara khusus memerlukan kualitas arsip atau menyiapkan berkas untuk pemutar yang Anda percaya.

> Opsi ukuran **Asli** adalah bagian dari peningkatan personalisasi premium Evertag. Ukuran standar (Kecil/Sedang/Besar/Sangat besar) gratis.

### Opsi penyimpanan tag: ID3v2.4 vs ID3v2.3

Ini adalah pengaturan tunggal yang paling penting untuk kompatibilitas. ID3v2 adalah format metadata yang digunakan di dalam berkas MP3. Ada dua versi yang banyak dipakai, dan keduanya berbeda dalam cara halus tetapi penting.

#### ID3v2.4

- Lebih baru, mendukung **encoding teks UTF-8** — penanganan yang benar untuk aksara non-Latin (Mandarin, Rusia, Jepang, Arab, Ibrani, dll).
- Lebih banyak jenis frame (volume relatif, preset equalizer, dll).
- **Direkomendasikan untuk pemutar modern** yang mendukungnya.

#### ID3v2.3

- Lebih lama tetapi **versi ID3 yang paling didukung secara universal**.
- Tidak mendukung UTF-8 secara langsung (memakai UTF-16 untuk teks Unicode).
- **Direkomendasikan ketika Anda perlu kompatibilitas maksimum** dengan pemutar lawas, stereo mobil, dan beberapa aplikasi desktop.

#### Kapan mengaktifkan ID3v2.4 di Evertag

- Anda memakai **pemutar audio modern** seperti Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (versi terkini), atau pemutar Android modern. ✅ **Aktifkan ID3v2.4.**
- Perpustakaan Anda berisi **karakter non-Latin** (Mandarin, Korea, Jepang, Rusia, Arab, Yunani, Ibrani). ✅ **Aktifkan ID3v2.4** — UTF-8 menangani ini jauh lebih bersih.

#### Kapan menonaktifkan ID3v2.4 di Evertag (gunakan ID3v2.3 sebagai gantinya)

- Anda menyiapkan berkas untuk **stereo mobil atau in-dash unit yang lebih tua** yang tidak membaca tag v2.4.
- Anda melihat **teks rusak atau tag hilang** di beberapa aplikasi setelah penyuntingan — itu sinyal kuat bahwa v2.4 tidak didukung di sana. Beralih kembali ke v2.3.
- Anda menargetkan **pemutar desktop legacy** atau pemutar portable yang lebih lama (iPod awal, beberapa pemutar MP3 dari era 2000–2010).

> **Aturan praktis:** jika tag Anda ditampilkan dengan benar di mana pun dengan v2.4, biarkan tetap aktif. Jika satu pemutar penting saja menampilkan karakter salah, kosong, atau gagal membaca tag, matikan v2.4 dan simpan ulang.

#### Duplikasi tag

Ketika Anda mengaktifkan **Duplikasi tag**, Evertag menulis bidang metadata umum (judul, artis, album, dll) ke **kedua bagian ID3v1 dan ID3v2** dari berkas. Hal ini meningkatkan kompatibilitas dengan pemutar yang sangat lama yang hanya membaca ID3v1 (tag 128-byte asli di akhir berkas).

- **Sebagian besar pengguna tidak memerlukannya.** Pemutar modern membaca ID3v2 terlebih dahulu.
- **Aktifkan hanya jika** Anda berurusan dengan perangkat keras vintage atau perangkat lunak tertentu yang mengabaikan ID3v2.

### Memperbarui berkas online: bagaimana Evertag menangani penyuntingan cloud

Ketika Anda mengedit tag pada berkas yang disimpan di cloud yang terhubung (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP, dll), Evertag harus mengunggah berkas yang dimodifikasi kembali. Anda mengontrol caranya:

- **Tampilkan pesan konfirmasi** *(default, direkomendasikan)* — Evertag menanyakan sebelum mengunggah. Terbaik untuk pengguna hati-hati dan perpustakaan bersama.
- **Perbarui metadata berkas secara otomatis** — mengunggah diam-diam setelah setiap penyuntingan. Terbaik untuk pengguna tunggal dengan koneksi cepat dan andal yang banyak menyunting.
- **Jangan perbarui metadata berkas** — Evertag hanya mengedit salinan lokal. Berguna untuk pratinjau perubahan tanpa mengirimkannya ke cloud.

### Mengedit berkas online: pembersihan berkas lokal

Untuk mengedit berkas jarak jauh, Evertag mengunduhnya ke perangkat Anda terlebih dahulu. Setelah penyuntingan, Anda memilih apa yang terjadi pada salinan lokal itu:

- **Selalu hapus berkas yang diunduh** — Evertag menghapus berkas sementara setelah penyuntingan. **Direkomendasikan** jika ruang penyimpanan terbatas atau Anda mengerjakan berkas orang lain.
- **Jangan hapus berkas yang diunduh** — menyimpan berkas yang disunting di perangkat Anda. Berguna jika Anda menginginkan baik salinan offline maupun salinan cloud yang diperbarui.

### Tombol di layar utama

Layar utama editor tag Evertag dapat menampilkan atau menyembunyikan tombol untuk operasi individual. Aktifkan hanya yang benar-benar Anda gunakan agar UI tetap fokus:

- **Cari tag audio otomatis** — menemukan metadata yang hilang secara online berdasarkan sidik jari audio berkas.
- **Cari tag audio manual** — cari berdasarkan judul/artis bila pencarian otomatis meleset.
- **Cari sampul album** — menemukan dan menyematkan sampul berkualitas tinggi.
- **Simpan sampul album** — mengekspor sampul yang disematkan ke pustaka foto atau berkas Anda.
- **Normalisasi encoding** — memperbaiki teks non-Latin yang rusak akibat encoding lama (sangat berguna untuk track Sirilik, Mandarin, dan Jepang yang di-rip dengan perangkat lunak legacy).
- **Hapus tag audio** — menghapus semua tag dari berkas. Berguna sebelum penyetelan tag yang bersih.

### Tampilkan tag yang diperluas

Aktifkan ini untuk menampilkan kumpulan lengkap bidang metadata di luar judul/artis/album/tahun dasar — termasuk BPM, konduktor, artis asli, suasana, hak cipta, encoder, komentar, lirik, dan lainnya. Fitur untuk pengguna mahir; sebagian besar pengguna kasual tidak memerlukannya.

### Edit berkas secara bersamaan

Ketika diaktifkan, Evertag memungkinkan Anda mengedit metadata di **beberapa berkas yang dipilih sekaligus** — atur album artist, tahun, atau genre yang sama untuk seluruh album dalam satu operasi. Ini cara tercepat membersihkan perpustakaan besar yang tidak terorganisir.

## Mengedit tag untuk Spotify, Apple Music, dan platform streaming

Pertanyaan umum: «saya mengedit tag di Evertag, mengunggah berkas, dan layanan streaming menampilkan metadata yang salah. Ada apa?»

Jawaban singkat: **layanan streaming tidak selalu menghormati tag lokal Anda.** Apple Music dan Spotify memiliki basis data internal sendiri — saat mereka mengenali sebuah trek, mereka menimpa metadata yang ditampilkan dengan milik mereka. Tetapi untuk **berkas yang diunggah**, berkas lokal Anda (fitur «Library» Apple Music, Spotify Local Files), dan **unggahan distributor ke platform streaming**, tag Anda jelas penting. Berikut cara mengatur Evertag untuk setiap skenario:

### Menyiapkan berkas untuk Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music menangani UTF-8 dengan benar.
- **Sampul album: Besar** — aplikasi Apple merender sampul besar dengan baik; Asli berlebihan.
- **Duplikasi tag: OFF** — tidak diperlukan.
- Pastikan **Album Artist** terisi dengan benar — Apple Music menggunakannya untuk pengelompokan.

### Menyiapkan berkas untuk Spotify Local Files

Spotify Local Files hanya menampilkan berkas yang ditandai dengan baik. Tag yang dibaca Spotify terbatas.

- **ID3v2.4: ON** dalam sebagian besar kasus. Jika sebuah trek tidak muncul dengan benar di Spotify setelah penyuntingan, **coba simpan dengan ID3v2.4: OFF** (yaitu sebagai ID3v2.3) — parser Spotify secara historis konservatif terhadap v2.4.
- **Sampul album: Sedang atau Besar** — Spotify tetap menyusutkannya.
- Isi minimal **Judul**, **Artis**, **Album**, dan **Nomor track**.

### Menyiapkan berkas untuk unggahan distributor (DistroKid, TuneCore, CD Baby, dll)

Jika Anda artis yang mengunggah karya sendiri ke platform streaming, distributor biasanya membaca tag tetapi juga meminta metadata di UI mereka. Bagaimanapun:

- **ID3v2.3** sering kali default yang lebih aman — banyak pipeline distributor dibangun bertahun-tahun lalu dan lebih menyukai format lama.
- Sematkan sampul **Besar** (kebanyakan distributor mensyaratkan sampul ≥ 1.400 × 1.400 px — periksa pedoman mereka).
- Jangan bergantung pada tag yang diperluas — distributor hanya membaca bidang inti.

### Menyiapkan berkas untuk Plex, Jellyfin, Navidrome, Subsonic, Emby

Server media self-hosted ini sangat toleran. Mereka membaca v2.3 dan v2.4 dengan rapi serta menangani UTF-8 dengan baik.

- **ID3v2.4: ON** tidak masalah.
- **Sampul album: Besar** atau **Sangat besar** — server-server ini menyajikan sampul ke klien mobile dan layar CarPlay, sehingga kualitas penting.
- **Album Artist** sangat direkomendasikan — itulah yang Plex/Jellyfin gunakan untuk mengelompokkan album berdasarkan artis dengan benar.

### Menyiapkan berkas untuk stereo mobil dan perangkat keras lebih tua

- **ID3v2.4: OFF** (gunakan ID3v2.3) — head unit lama sering tidak mendukung v2.4.
- **Sampul album: Sedang** — banyak layar mobil tersangkut pada sampul tertanam yang besar.
- **Duplikasi tag: ON** — stereo mobil yang lebih tua kadang hanya membaca fallback ID3v1.

## Peningkatan lainnya

### Desain Liquid Glass

Antarmuka Evertag 4.2 disesuaikan untuk material **Liquid Glass** baru Apple di seluruh aplikasi — permukaan tembus cahaya, animasi yang lebih halus, dan kontrol yang dipoles agar pas dengan iOS, iPadOS, dan macOS.

### Pustaka koneksi diperbarui

Kami menyegarkan pustaka internal yang digunakan Evertag untuk berbicara dengan **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, dan layanan lain. Hasilnya: lebih sedikit kegagalan koneksi pada kasus ekstrem, dukungan yang lebih baik untuk versi server terbaru, dan keandalan yang lebih baik saat menyunting tag pada berkas jarak jauh.

### Perbaikan terjemahan dan lokalisasi

Beberapa perbaikan bahasa di UI berdasarkan umpan balik langsung dari pengguna. Penataan teks yang lebih baik pada tombol kecil di beberapa bahasa.

### Penyempurnaan kecil yang terinspirasi oleh masukan Anda

Banyak perbaikan kecil berdasarkan ulasan App Store dan email ke support@everappz.com. Kami membaca setiap pesan.

## Dapatkan Evertag 4.2

[**Unduh Evertag dari App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) atau perbarui dari App Store. Evertag adalah unduhan gratis dengan upgrade dalam aplikasi opsional untuk fitur lanjutan. Koneksi cloud baru, protokol jaringan, peningkatan Wi-Fi Drive, dan UI Liquid Glass adalah bagian dari pembaruan dasar.

Jika Anda menyukai aplikasi ini, mohon tinggalkan rating di App Store — itu sangat membantu. Punya umpan balik atau menemukan masalah? Email kami ke **support@everappz.com**. Kami membaca setiap pesan.

## Pertanyaan yang Sering Diajukan

{{% details title="Apa yang baru di Evertag 4.2?" closed="true" %}}
Evertag 4.2 menambahkan 6+ koneksi cloud dan server baru (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), Wi-Fi Drive yang disegarkan dengan pilih banyak dan antrean unggah lebih pintar, pembaruan UI Liquid Glass, pustaka koneksi yang diperbarui, perbaikan bug penyuntingan tag yang penting, dan peningkatan terjemahan.
{{% /details %}}

{{% details title="Saya harus menggunakan ID3v2.4 atau ID3v2.3 di Evertag?" closed="true" %}}
Gunakan **ID3v2.4** untuk pemutar modern (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, aplikasi Android modern) dan untuk perpustakaan dengan karakter non-Latin — dukungan UTF-8 berarti tag Mandarin, Korea, Jepang, Rusia, Arab, dan Ibrani lebih bersih. Gunakan **ID3v2.3** jika tag Anda tampil salah di beberapa aplikasi, jika Anda menargetkan stereo mobil yang lebih lama, atau jika pipeline distributor streaming menolak v2.4. Anda selalu dapat beralih dan menyimpan ulang.
{{% /details %}}

{{% details title="Mengapa tag saya salah di Spotify setelah penyuntingan?" closed="true" %}}
Spotify sebagian besar menampilkan metadata dari katalog mereka sendiri — tag lokal Anda hanya digunakan untuk «Local Files» atau konten yang Anda unggah sebagai artis. Jika Anda menandai berkas untuk Spotify Local Files dan tidak ditampilkan dengan benar, coba nonaktifkan ID3v2.4 di Evertag dan simpan sebagai ID3v2.3 — parser Spotify secara historis konservatif terhadap v2.4.
{{% /details %}}

{{% details title="Ukuran sampul album mana yang harus saya pilih di Evertag?" closed="true" %}}
Untuk sebagian besar pengguna: **Besar**. Tampak hebat di ponsel, iPad, Mac, dan layar mobil modern tanpa membengkakkan berkas terlalu banyak. Gunakan **Sedang** jika perpustakaan Anda sangat besar dan ingin menghemat disk. Gunakan **Asli** (tanpa penskalaan) hanya untuk master arsip atau ketika Anda benar-benar memerlukan kualitas maksimum — tetapi perhatikan bahwa beberapa pemutar lebih lama kesulitan dengan sampul tertanam yang sangat besar. **Asli** adalah bagian dari peningkatan personalisasi premium Evertag.
{{% /details %}}

{{% details title="Apakah sampul album yang lebih besar membuat berkas saya lebih besar?" closed="true" %}}
Ya. Menyematkan sampul 3.000 × 3.000 px dapat menambah beberapa megabyte pada satu berkas audio. Pada perpustakaan 1.000 track, itu mencapai gigabyte. Jika ruang penyimpanan terbatas, gunakan Sedang atau Besar; jika Anda streaming dari NAS yang ukurannya tidak masalah, Sangat besar atau Asli boleh.
{{% /details %}}

{{% details title="Apa itu Duplikasi tag dan haruskah saya mengaktifkannya?" closed="true" %}}
Duplikasi tag menulis metadata inti ke bagian ID3v1 (warisan 128-byte) dan ID3v2 (modern) dari berkas. Aktifkan hanya jika Anda menargetkan pemutar yang sangat lama atau perangkat keras yang membaca ID3v1. Untuk semua yang modern (smartphone, komputer, stereo mobil terbaru), biarkan mati.
{{% /details %}}

{{% details title="Apakah Evertag mengedit tag langsung pada berkas cloud?" closed="true" %}}
Ya. Sambungkan ke cloud Anda (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, dll) atau melalui FTP/SFTP/NFS, lalu buka berkas dan edit tag seolah-olah berkas itu lokal. Evertag mengunduh berkas, menerapkan penyuntingan Anda, dan mengunggah versi yang diperbarui kembali. Anda dapat memilih antara mode «Selalu tanya», «Auto-upload», atau «Jangan upload» di pengaturan.
{{% /details %}}

{{% details title="Bisakah saya mengedit tag FLAC di iPhone dengan Evertag?" closed="true" %}}
Ya. Evertag mendukung FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE, dan format penting lainnya dengan dukungan baca/tulis tag penuh termasuk sampul tertanam.
{{% /details %}}

{{% details title="Bagaimana cara mengedit tag dengan aman di server rumah saya dengan SFTP?" closed="true" %}}
Buka Evertag, buka Connections, pilih SFTP, dan masukkan hostname atau IP server, port (biasanya 22), nama pengguna, dan kata sandi atau kunci pribadi SSH. Evertag akan menelusuri folder jarak jauh Anda dan mengedit tag langsung dengan enkripsi ujung-ke-ujung melalui SSH.
{{% /details %}}

{{% details title="Bisakah saya mengedit tag pada beberapa berkas sekaligus?" closed="true" %}}
Ya. Aktifkan **Edit berkas secara bersamaan** di pengaturan. Pilih beberapa berkas, buka editor tag, dan setiap bidang yang Anda ubah akan diterapkan ke semua berkas yang dipilih. Ini cara tercepat untuk mengatur album artist, tahun, atau genre yang sama untuk seluruh album.
{{% /details %}}

{{% details title="Apakah pembaruan ke Evertag 4.2 gratis?" closed="true" %}}
Ya. Evertag adalah unduhan gratis dari App Store, dan 4.2 adalah pembaruan gratis untuk semua pengguna yang sudah ada. Integrasi cloud baru, peningkatan Wi-Fi Drive, dan UI Liquid Glass adalah bagian dari pembaruan dasar.
{{% /details %}}

{{% details title="Di perangkat apa saja Evertag 4.2 tersedia?" closed="true" %}}
Evertag 4.2 berjalan di iPhone, iPad, dan Mac. Sinkronisasi iCloud Drive menjaga pengaturan editor tag Anda tetap konsisten antar perangkat.
{{% /details %}}
