---
date: '2025-06-12T17:00:00+00:00'
title: 'Evervideo'
description: 'FAQ Evervideo: pemain video awan HD dan 4K untuk iPhone, iPad, dan Mac. Strim dan muat turun video dari iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP/SFTP, DLNA, dan S3 — serta Plex, Jellyfin, Emby, Subsonic, dan Navidrome. Jawapan tentang MKV, HEVC, AV1, video 360°/VR, PiP, sari kata, penyama audio dan video, strim kamera IP RTSP, AirPlay 2, Chromecast, Family Sharing, dan pelan Premium.'
keywords: [
  "FAQ Evervideo", "Evervideo iPhone", "Evervideo iPad", "Evervideo Mac",
  "pemain video awan", "pemain video HD iOS", "pemain video 4K iPhone",
  "pemain MKV iOS", "pemain HEVC iPhone", "pemain AV1 iOS",
  "pemain video FFmpeg", "pemain MP4 Mac", "pemain AVI iOS",
  "pemain video 360 iPhone", "pemain video VR iPhone", "pemain video Insta360",
  "video PiP iPhone", "pemain video PiP iPad",
  "pemain RTSP iPhone", "pemapar kamera IP", "pemain video DLNA",
  "klien Plex iPhone", "klien Jellyfin iOS", "klien Emby iPad",
  "video Subsonic", "klien Navidrome", "pemain sari kata video",
  "sari kata SRT VTT ASS", "sari kata sekunder iPhone", "sari kata dua",
  "penyama video iOS", "pratetap penyama video",
  "strim video dari Google Drive", "strim video dari Dropbox",
  "strim video dari OneDrive", "strim video dari iCloud Drive",
  "strim video dari NAS", "Chromecast video iPhone", "AirPlay 2 video",
  "pemain video pustaka Foto", "pemain video Apple Music",
  "pemindahan video Wi-Fi Drive", "senarai main video M3U", "pemacu USB video iPhone",
  "Evervideo Premium", "apl video Family Sharing", "pemain video gaya YouTube"
]
tags: ["evervideo", "faq", "penstriman video", "pemain luar talian", "apl video iOS", "PiP", "sari kata", "video 360", "FFmpeg", "Plex", "RTSP"]
---


<div class="hx:mt-6"></div>

Evervideo ialah **pemain video awan** HD dan 4K untuk **iPhone, iPad, dan Mac** yang menstrim dan memuat turun video dari iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology, QNAP, dan mana-mana sumber WebDAV, SMB, NFS, FTP/SFTP, DLNA, atau S3 — serta pelayan media hos kendiri seperti **Plex, Jellyfin, Emby, Subsonic,** dan **Navidrome**, dan strim **RTSP** langsung daripada kamera IP. Dibina pada enjin pemain berasaskan **FFmpeg** tersuai dengan **penyahkodan H.264/HEVC dipercepatkan perkakasan**, trek sari kata utama dan sekunder (SRT/VTT/ASS/libass), penyama video dengan pratetap, penyama audio, **Picture-in-Picture**, **main semula 360°/VR** untuk rakaman Insta360 dan GoPro Max, pemutus **AirPlay 2** dan **Chromecast**, dan pemain padat sentiasa di skrin. FAQ ini menjawab soalan yang paling kerap dihantar pengguna. Untuk panduan yang lebih mendalam, lihat [Panduan Pengguna Evervideo](/docs/guide/evervideo/).

<div class="hx:w-full">

{{% details title="Apakah itu Evervideo?" closed="true" %}}
**Evervideo ialah pemain video awan HD dan 4K berfungsi penuh untuk iPhone, iPad, dan Mac** yang mengubah mana-mana akaun storan awan, NAS, atau pelayan media menjadi pustaka video peribadi anda dengan kawalan penuh terhadap fail anda.<br><br>

Dibina pada enjin pemain berasaskan FFmpeg tersuai dengan penyahkodan H.264 dan HEVC dipercepatkan perkakasan, Evervideo memainkan hampir setiap bekas dan kodek moden (MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS, dan format FFmpeg yang panjang), menyokong sari kata utama dan sekunder, termasuk penyama audio dan video, dan berfungsi dalam mod Picture-in-Picture supaya anda boleh terus menonton semasa menggunakan apl lain.
{{% /details %}}

{{% details title="Adakah Evervideo percuma? Apakah perbezaan antara Percuma dan Premium?" closed="true" %}}
**Ya — Evervideo percuma untuk dimuat turun dan digunakan**, dengan pembelian dalam apl pilihan untuk menghapuskan had dan membuka kunci set ciri Premium penuh.<br><br>

Premium tersedia sebagai **pembelian seumur hidup satu kali** atau sebagai **langganan bulanan atau tahunan**, jadi anda boleh memilih pilihan yang paling sesuai. Harga mungkin berbeza mengikut negara. **Family Sharing** didayakan untuk setiap pelan, jadi anda boleh berkongsi Premium dengan sehingga lima ahli keluarga. Pembelian seumur hidup dan langganan dikongsi antara iOS dan macOS melalui iCloud — pasang versi terkini pada setiap peranti, daftar masuk dengan Apple ID yang sama, dan tunggu kira-kira satu minit untuk maklumat pembelian disegerakkan.<br><br>

**Evervideo Premium** menghapuskan setiap had versi percuma: main balik bebas iklan, senarai main tanpa had, perkhidmatan awan bersambung tanpa had, kegemaran tanpa had, muat turun luar talian tanpa had, arkib (ZIP) koleksi media, dan pemperibadian penuh (ikon apl tersuai, tema, skim warna).<br><br>

[Baca perbandingan Percuma vs Premium penuh](/docs/faq/evervideo/what-is-the-difference-between-evervideo-and-evervideo-premium/)
{{% /details %}}

{{% details title="Adakah Evervideo Selamat?" closed="true" %}}
Evervideo menggunakan hanya SDK rasmi dan sambungan selamat untuk berinteraksi dengan perkhidmatan awan yang disambungkan. Log masuk dan kata laluan anda tidak tersedia untuk aplikasi. Semua permintaan dari aplikasi ke perkhidmatan awan disulitkan.<br>
Apabila anda memasukkan log masuk dan kata laluan, aplikasi menunjukkan halaman kebenaran rasmi yang disediakan oleh pembekal perkhidmatan awan dan semua proses kebenaran dibuat di luar aplikasi. Pembekal perkhidmatan awan menghantar token-auth ke aplikasi selepas kebenaran berjaya dan token tersebut digunakan untuk membuat panggilan API.<br><br>

Token-auth ialah kunci digital yang membolehkan aplikasi pihak ketiga berinteraksi dengan storan awan. Token-auth disimpan pada peranti anda dalam storan sistem selamat yang dipanggil Keychain. Anda boleh memuat turun fail anda dari perkhidmatan awan yang disambungkan ke peranti dan fail tersebut akan diletakkan dalam direktori "Documents" apl. Anda boleh membuang fail tersebut pada bila-bila masa menggunakan pengurus fail terbina dalam.<br>
Aplikasi tidak berkongsi sebarang maklumat dari akaun awan yang disambungkan. Anda boleh membatalkan akses ke akaun awan anda pada bila-bila masa dengan membuka halaman tetapan akaun pada penyemak imbas web anda.<br><br>

Untuk menolak token-auth, log masuk ke akaun anda pada penyemak imbas web dan navigasi ke halaman tetapan. Di sana anda boleh mencari semua apl pihak ketiga yang disambungkan ke akaun awan anda dan membuang mana-mana yang anda tidak mahu gunakan lagi.<br><br>

Tutorial penuh tersedia di sini:<br>
[Cara memutuskan sambungan apl pihak ketiga dari akaun Google anda](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account/)<br><br>

Anda juga boleh memutuskan sambungan akaun awan yang disambungkan dalam aplikasi dan token-auth juga akan dibuang dari peranti anda. Jika anda membuang aplikasi dari peranti anda, semua data yang dimuat turun dan token akses juga akan dibuang.<br><br>

{{% /details %}}

{{% details title="Format video apakah yang disokong Evervideo?" closed="true" %}}
**Evervideo memainkan hampir setiap bekas dan kodek video moden pada iPhone, iPad, dan Mac** berkat enjin FFmpeg terbungkus yang digabungkan dengan penyahkodan H.264/HEVC dipercepatkan perkakasan.<br><br>

**Bekas:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT, dan banyak lagi.<br>
**Kodek video:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV, dan hampir setiap kodek lain yang disokong FFmpeg.<br>
**Kodek audio (dalam video):** AAC, MP3, FLAC, ALAC, OGG/Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE.<br>
**Sari kata:** SRT, VTT (WebVTT), ASS/SSA (dirender melalui libass), trek imej dan teks terbenam.<br>
**Protokol penstriman:** HTTP/HTTPS, HLS (m3u8), RTSP (kamera IP dan IPTV).<br>
**Penstriman terus:** SMB/WebDAV/FTP/SFTP/NFS/DLNA.<br>
{{% /details %}}

{{% details title="Adakah Evervideo memainkan fail MKV pada iPhone?" closed="true" %}}
**Ya — Evervideo memainkan fail MKV secara asli pada iPhone, iPad, dan Mac** tanpa penukaran diperlukan, termasuk bekas MKV dengan video H.264, HEVC, VP9, atau AV1, pelbagai trek audio, dan sari kata SRT/ASS terbenam.<br><br>

Ini adalah salah satu sebab utama orang memasang Evervideo berbanding pemain lalai Apple: iOS tidak membuka MKV sama sekali, tetapi Evervideo mengendalikannya melalui enjin FFmpeg terbungkus. Anda boleh menstrim fail MKV terus dari storan awan atau NAS tanpa memuat turun.
{{% /details %}}

{{% details title="Adakah Evervideo menyokong video 4K dan HDR?" closed="true" %}}
**Ya — Evervideo memainkan video 4K (Ultra HD) dan kandungan berkod HDR** pada setiap peranti yang mempunyai perkakasan untuk menyahkodnya. iPhone, iPad, dan Mac Apple Silicon moden semua menyahkod 4K H.264 dan 4K HEVC dalam perkakasan, jadi main balik lancar dan mesra bateri.<br><br>

Untuk hasil terbaik pada 4K strim awan, tingkatkan **Masa Pramuatan** dalam **Tetapan → Player → File Loading** supaya penimbal dapat mengikuti fail kadar bit tinggi, dan sambung ke rangkaian Wi-Fi berbanding selular.
{{% /details %}}

{{% details title="Adakah Evervideo menyokong penyahkodan H.264 dan HEVC perkakasan?" closed="true" %}}
**Ya — Evervideo menggunakan penyahkod H.264 (AVC) dan H.265 (HEVC) perkakasan secara lalai** pada setiap iPhone, iPad, dan Mac yang menyokongnya, yang bermaksud main balik lebih lancar, penggunaan bateri lebih rendah, dan suhu peranti lebih sejuk berbanding dengan penyahkodan perisian tulen.<br><br>

Anda boleh togol penyahkodan perkakasan secara bebas untuk H.264 dan HEVC dalam **Tetapan → Player → Video → Hardware Decode H.264/H.265**. Jika fail tertentu mempunyai isu keserasian (strim rosak, profil eksotik), lumpuhkan penyahkodan perkakasan untuk fail tersebut untuk beralih ke penyahkodan perisian FFmpeg.
{{% /details %}}

{{% details title="Adakah Evervideo menyokong Picture-in-Picture (PiP)?" closed="true" %}}
**Ya — Evervideo menyokong sepenuhnya Picture-in-Picture pada iPhone dan iPad.** Apabila anda mengetuk ikon PiP pada pemain, video terus dimainkan dalam tetingkap terapung di atas setiap apl lain.<br><br>

Seret tetingkap terapung ke mana-mana sudut, cubit untuk mengubah saiz, ketuk sekali untuk membawa kawalan main/jeda/langkau asas, dan ketuk butang kembang kecil untuk kembali ke Evervideo. PiP berfungsi dengan **setiap format video yang dimainkan Evervideo**, termasuk fail strim awan dan strim kamera IP RTSP, dan terus berjalan semasa telefon anda dikunci.
{{% /details %}}

{{% details title="Adakah Evervideo mempunyai UI pemain gaya YouTube untuk video tempatan saya?" closed="true" %}}
**Ya — susun atur lalai Evervideo dibina di sekitar pengalaman gaya YouTube untuk video anda sendiri: pemain video padat sentiasa kelihatan di bahagian atas skrin semasa anda melayari pustaka anda di bawah.**<br><br>

**Pemain padat** kekal di skrin merentasi setiap tab — Terkini, Kegemaran, Pustaka Media, Senarai Main, Fail, dan Tetapan — jadi anda boleh melayari, mencari, mengatur, dan membaris video seterusnya tanpa mengganggu main balik. Ketuk pemain padat untuk meluaskannya ke paparan skrin penuh; leret ke bawah untuk melipatnya kembali ke padat tanpa menghentikan video. Pada macOS, pemain padat boleh dilepaskan ke **tetingkap terapung sentiasa-atas** berasingan untuk multitugas gaya picture-in-picture sebenar pada desktop.<br><br>

Tidak seperti YouTube, tiada iklan, tiada cadangan algoritma, tiada gesaan main semula automatik, dan tiada penjejakan — anda mempunyai kawalan penuh ke atas pustaka video anda sendiri dari iCloud, Google Drive, Dropbox, NAS, Plex/Jellyfin/Emby, atau mana-mana tempat lain.
{{% /details %}}

{{% details title="Adakah Evervideo memainkan video 360° dari Insta360 dan kamera 360 lain?" closed="true" %}}
**Ya — Evervideo memainkan video 360°/VR (sfera) secara terus, tanpa pra-pemprosesan atau penukaran diperlukan**, termasuk rakaman dari Insta360 (One X, X3, X4, ONE RS, GO 3), GoPro Max, Ricoh Theta, Samsung Gear 360, Vuze, dan mana-mana sumber 360° equirectangular lain.<br><br>

Letakkan saja video 360° ke dalam iCloud Drive, Google Drive, Dropbox, NAS anda, atau mainkan dari pustaka Foto iOS — Evervideo mengenali format sfera dan beralih ke rendering viewport VR secara automatik. Dari sana anda boleh:<br>

- **Putar peranti anda** — condong dan putar iPhone atau iPad anda secara fizikal dan viewport video berputar secara masa nyata untuk melihat sekeliling pemandangan.<br>
- **Seret dengan jari anda** untuk mengimbas ke mana-mana arah tanpa menggerakkan peranti.<br>
- **Cubit untuk zum** masuk dan keluar paparan sfera.<br>
- Tukar mod unjuran/paparan dalam menu Lebih banyak tindakan pemain, dan gunakan sarung kepala VR untuk pengalaman yang benar-benar imersif.<br><br>

Ini bermakna rakaman Insta360 anda berfungsi serta-merta pada iPhone dan iPad — tiada apl tambahan, tiada transkod, tiada langganan awan diperlukan.
{{% /details %}}

{{% details title="Bagaimana saya menggunakan penyama video dan pratetap?" closed="true" %}}
**Buka pemain, ketuk Lebih banyak tindakan → Penyama Video, kemudian seret gelangsar untuk kecerahan, kontras, ketepuan, dan rona — atau pilih pratetap.**<br><br>

**Penyama video** Evervideo ialah alat pelarasan gambar masa nyata yang berjalan di dalam saluran paip rendering FFmpeg:<br>

- **Kecerahan** — tingkatkan pemandangan gelap yang diambil dalam cahaya rendah, atau kurangkan pendedahan yang terlalu cerah.<br>
- **Kontras** — tambahkan ketajaman kepada kandungan yang pudar atau lembutkan sumber yang terlalu kontras.<br>
- **Ketepuan** — hangatkan warna yang kusam atau desaturate untuk tampilan sinematik.<br>
- **Rona** — alihkan keseimbangan warna untuk membetulkan pelaburan hijau atau magenta.<br><br>

Anda boleh menyimpan tetapan kegemaran anda sebagai **pratetap tersuai** dan menggunakannya semula dengan satu ketukan pada mana-mana video masa hadapan. Pratetap juga boleh **dieksport dan diimport** supaya anda boleh berkongsinya merentasi iPhone, iPad, dan Mac, atau menyandarkannya. Gabungkan penyama video dengan **penyama audio** (10-band EQ dengan pustaka pratetap sendiri) untuk kawalan penuh terhadap gambar dan bunyi.
{{% /details %}}

{{% details title="Bagaimana saya memutar atau menukar mod skala video?" closed="true" %}}
**Ketuk Lebih banyak tindakan pada pemain dan pilih Putaran (0°/90°/180°/270°) atau Mod Skala (Muat/Isi/Regangan/Asal).**<br><br>

**Putaran** berguna untuk video yang dirakam secara menyamping atau terbalik — putar gambar tanpa meninggalkan pemain. **Mod Skala** mengawal cara gambar memenuhi skrin:<br>

- **Muat** — kekalkan nisbah aspek asal dengan bar hitam jika diperlukan.<br>
- **Isi** — isi keseluruhan skrin, memotong video jika perlu.<br>
- **Regangan** — regangkan untuk memenuhi skrin, mengherotkan gambar.<br>
- **Asal** — kekalkan resolusi asli pada 1:1.
{{% /details %}}

{{% details title="Bagaimana saya memilih trek audio berbeza (sinkronisasi, ulasan) dalam video?" closed="true" %}}
**Ketuk butang Lebih banyak tindakan ('...') pada pemain dan pilih Trek Audio — kemudian pilih trek yang anda mahukan dari senarai.**<br><br>

Untuk video dengan pelbagai trek audio (sinkronisasi bahasa lain, ulasan pengarah, campuran asal/langsung), Evervideo menunjukkan setiap trek terbenam dengan bahasa dan kodeknya. Ini berfungsi untuk MKV, MP4, M2TS, dan mana-mana bekas lain yang mendedahkan pelbagai strim audio.
{{% /details %}}

{{% details title="Bagaimana saya menambah atau menukar sari kata dalam Evervideo?" closed="true" %}}
**Ketuk butang Lebih banyak tindakan ('...') pada pemain dan pilih Sari Kata — kemudian pilih trek sari kata terbenam, muatkan fail sari kata luaran, atau tukar fon.**<br><br>

Evervideo secara automatik menyenaraikan setiap trek sari kata yang terbenam dalam video. Untuk memuatkan fail sari kata luaran, pilih **Fail Luaran** dan pilih fail `.srt`, `.vtt`, `.ass`, atau `.ssa` dari peranti, iCloud Drive, atau mana-mana perkhidmatan awan yang disambungkan. Anda juga boleh mengkonfigurasi kelakuan sari kata lalai dalam **Tetapan → Player → Sari Kata**.
{{% /details %}}

{{% details title="Adakah Evervideo menyokong fail sari kata SRT, VTT, dan ASS luaran?" closed="true" %}}
**Ya — Evervideo memuatkan fail sari kata luaran dalam format SRT, VTT (WebVTT), ASS, dan SSA** dari mana-mana sahaja pada peranti anda atau mana-mana perkhidmatan awan yang disambungkan.<br><br>

Fail ASS/SSA dengan penggayaan lanjutan (fon tersuai, warna, kedudukan, kesan karaoke) dirender dengan betul berkat pustaka **libass** yang terbungkus — sempurna untuk anime fansub, fail kapsyen profesional, dan pembentangan. Anda juga boleh menetapkan fon tertentu untuk sari kata dalam **Tetapan → Player → Sari Kata → Fon**.
{{% /details %}}

{{% details title="Bagaimana saya memadamkan video dari Evervideo tanpa memadamnya dari storan awan saya?" closed="true" %}}
**Pada mana-mana video, ketuk '...' → Padam dari Pustaka Media — ini membuang entri dari pangkalan data pustaka anda tetapi meninggalkan fail asal tidak tersentuh dalam storan awan, NAS, atau pustaka Foto iOS anda.**<br><br>

Jika anda juga mahu membuang fail dari sumbernya, pilih **Padam dari Perkhidmatan Awan** atau **Padam dari Fail Tempatan** sebaliknya. Tindakan merosakkan ini tidak boleh dibatalkan, jadi berhati-hati apabila anda mempunyai beberapa video dipilih.<br><br>

Untuk membuang salinan yang dimuat turun tanpa menyentuh apa-apa dalam awan, buka tab **Fail**, cari video di bawah **Fail dalam Aplikasi Ini** atau **Folder Luar Talian**, dan gunakan **'...' → Padam**. Asal awan kekal tepat di tempat ia berada — Evervideo hanya membuang salinan tempatan.
{{% /details %}}

{{% details title="Bagaimana saya menukar kelajuan main balik dalam Evervideo?" closed="true" %}}
**Buka pemain, ketuk kawalan Kelajuan pada bar alat, dan seret gelangsar — kelajuan dari 0.25× hingga 3.00× disokong.**<br><br>

Anda boleh melambatkan kandungan untuk analisis bingkai demi bingkai (0.25×/0.5×) atau mempercepatkannya untuk tutorial dan kuliah (1.25×/1.5×/2×). Ketuk ikon konfigurasi di sudut kanan atas skrin Kelajuan untuk beralih ke mod tepat untuk pelarasan yang lebih halus. Pembetulan pic per-trek mengekalkan bunyi audio yang semula jadi pada kelajuan bukan 1×.
{{% /details %}}

{{% details title="Bagaimana saya menetapkan pemasa tidur dalam Evervideo?" closed="true" %}}
**Buka Tetapan → Player → Pemasa Tidur, hidupkan, dan pilih berapa lama anda mahu main balik diteruskan sebelum berhenti secara automatik.**<br><br>

Anda juga boleh menambah butang **Pemasa Tidur** terus ke skrin pemain utama melalui **Tetapan → Player → Pemperibadian → Tindakan Skrin Utama**. Ketuk ikon konfigurasi untuk mod tepat dengan kebutiran minit demi minit — berguna untuk tertidur semasa menonton rancangan.
{{% /details %}}

{{% details title="Bagaimana saya menanda halaman kedudukan tertentu dalam video?" closed="true" %}}
**Buka pemain dan ketuk Tambah Penanda Buku dari menu Lebih banyak tindakan untuk menyimpan kedudukan main balik semasa — penanda buku muncul di bawah Lebih banyak tindakan → Penanda Buku.**<br><br>

Penanda buku disimpan per-video dan kekal antara sesi, menjadikannya sempurna untuk video panjang, kuliah, buku audio video, siri tutorial, dan rakaman konsert di mana anda ingin melompat kembali ke saat tertentu.
{{% /details %}}

{{% details title="Bagaimana saya boleh meneruskan senarai main dari tempat saya berhenti?" closed="true" %}}
Pertama, pastikan 'Simpan Keadaan Pemain Media' didayakan dalam Tetapan > Pemain Media > Umum. Apabila anda beralih ke senarai main lain dan kembali, anda akan melihat empat tindakan pada bar alat atas di bawah karya seni album: 'Cari,' 'Teruskan Main Balik,' 'Main Semua,' dan 'Kocok Semua.' Ketuk 'Teruskan Main Balik' untuk meneruskan senarai main dari keadaan tersimpan terakhir dan kedudukan media.
{{% /details %}}

{{% details title="Bagaimana saya menayangkan video dari Evervideo ke Chromecast atau AirPlay?" closed="true" %}}
**Buka pemain video, ketuk ikon AirPlay atau Chromecast, dan pilih TV, Apple TV, HomePod, atau pembesar suara pintar anda dari senarai.**<br><br>

Kedua-dua **AirPlay 2** dan **Google Chromecast** disokong pada iOS. AirPlay 2 juga membolehkan anda menstrim ke beberapa peranti yang serasi pada masa yang sama. Sesetengah fail hi-res atau HEVC mungkin perlu dikod semula untuk perkakasan Chromecast.
{{% /details %}}

{{% details title="Adakah Evervideo menyokong Apple CarPlay?" closed="true" %}}
**Tidak — Evervideo tidak menyokong Apple CarPlay.** Apple CarPlay terhad kepada apl audio sahaja (muzik, podcast, buku audio, navigasi), jadi pemain video tidak boleh dijalankan pada skrin CarPlay mengikut dasar Apple.<br><br>

Jika anda mahukan apl sambungan awan yang menyokong CarPlay, apl muzik kami **Evermusic** dan **Flacbox** keduanya berfungsi sepenuhnya pada CarPlay dengan tab khusus untuk Pustaka, Sambungan, Fail Tempatan, dan Tetapan.
{{% /details %}}

{{% details title="Perkhidmatan awan apakah yang disokong Evervideo?" closed="true" %}}
**Evervideo menyambung ke hampir setiap pembekal storan awan popular, pelayan media hos kendiri, dan protokol perkongsian fail — semua dari satu skrin Sambung ke storan awan.**<br><br>

**Storan awan peribadi:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).<br>

**Pelayan media hos kendiri:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud · Synology Drive · QNAP.<br>

**Protokol NAS:** SMB · WebDAV · FTP/FTPS · SFTP · NFS · DLNA/UPnP.<br>

**Strim langsung dan kamera IP:** RTSP.<br>

**Storan objek serasi S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces.<br><br>

Pengguna Premium boleh menyambung bilangan perkhidmatan yang tidak terhad; versi percuma terhad kepada tiga.
{{% /details %}}

{{% details title="Adakah Evervideo menyokong Plex, Jellyfin, Emby, Subsonic, dan Navidrome?" closed="true" %}}
**Ya — Evervideo menyambung secara asli ke Plex Media Server, Jellyfin, Emby, Subsonic, dan Navidrome**, jadi anda boleh menstrim pustaka video hos kendiri anda secara terus tanpa mendedahkan perkongsian fail yang mendasari.<br><br>

- **Plex Media Server** — ketuk **Fail → Sambung ke storan awan → Plex**, daftar masuk dengan akaun Plex anda, dan pilih pelayan. Pelayan Plex pada rangkaian setempat yang sama juga ditemui secara automatik dalam bahagian **Peranti yang Tersedia**.<br>
- **Jellyfin** (sumber terbuka) — ketuk **Fail → Sambung ke storan awan → Jellyfin**, masukkan URL pelayan anda (seperti `http://server-ip:8096`) dan kelayakan.<br>
- **Emby** (komersial) — ketuk **Fail → Sambung ke storan awan → Emby** dan masukkan URL pelayan dan log masuk.<br>
- **Subsonic dan pelayan serasi Subsonic** — ketuk **Fail → Sambung ke storan awan → Subsonic**, masukkan URL pelayan dan kelayakan. Laluan API yang sama berfungsi dengan **Navidrome**, **Airsonic**, **Funkwhale**, **Gonic**, **Logitech Media Server (LMS)**, dan **Ampache**.<br><br>

Setelah disambungkan, setiap pelayan muncul bersama akaun awan anda dalam tab Fail. Anda boleh melayari Filem, Rancangan TV, Video Rumah, Muzik, Senarai Main, dan koleksi; muat turun untuk main balik luar talian; baris item dalam pemain; dan menariknya ke Pustaka Media global anda — semua tanpa meninggalkan Evervideo.
{{% /details %}}

{{% details title="Adakah Evervideo menyambung melalui SMB, WebDAV, FTP/SFTP, NFS, dan DLNA?" closed="true" %}}
**Ya — Evervideo menyokong setiap protokol NAS dan perkongsian fail utama: SMB (SMB1, SMB2, Auto), WebDAV (HTTP/HTTPS), FTP/FTPS, SFTP (kata laluan atau pengesahan kunci awam), NFS, dan DLNA/UPnP.**<br><br>

Ini membolehkan anda menyambung ke hampir mana-mana peranti NAS (Synology, QNAP, WD My Cloud Home, Buffalo, Apple Time Capsule), perkongsian fail Linux/macOS/Windows, pelayan Nextcloud/ownCloud hos kendiri, atau mana-mana pelayan media UPnP/DLNA, semuanya dari menu **Fail → Sambung ke storan awan**.
{{% /details %}}

{{% details title="Adakah Evervideo menyokong storan objek serasi S3?" closed="true" %}}
**Ya — Evervideo termasuk penyambung serasi S3** yang berfungsi dengan **AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces,** dan mana-mana perkhidmatan lain yang mendedahkan titik hujung S3-API.<br><br>

Ketuk **Fail → Sambung ke storan awan → S3 storage**, kemudian masukkan URL titik hujung, rantau, kunci akses, kunci rahsia, dan nama baldi. Setelah disambungkan, baldi berkelakuan seperti mana-mana awan lain — layar, strim, muat turun, baris, dan tambah ke pustaka anda.
{{% /details %}}

{{% details title="Bolehkah saya memainkan strim RTSP (kamera IP, IPTV) dalam Evervideo?" closed="true" %}}
**Ya — Evervideo mempunyai sokongan RTSP asli**, jadi anda boleh menunjukkannya ke mana-mana URL `rtsp://` — kamera keselamatan, kamera loceng pintu, monitor bayi, pembekal IPTV, suapan siaran — dan Evervideo akan menarik dan menyahkod strim langsung.<br><br>

Ketuk **Fail → Pautan Dalam Talian → Tambah pautan**, tampal URL penuh (`rtsp://camera-ip:port/stream-path`), berikan log masuk dan kata laluan jika diperlukan, dan ketuk **Selesai**. Strim RTSP berfungsi dalam Picture-in-Picture, pemain padat, dan mereka menayangkan melalui AirPlay 2 dan Chromecast seperti video biasa.
{{% /details %}}

{{% details title="Bagaimana saya memindahkan video ke Evervideo dari komputer saya?" closed="true" %}}
Anda boleh menyambungkan komputer atau NAS peribadi anda menggunakan protokol SMB, WebDAV, atau DLNA. Sebagai alternatif, gunakan iTunes File Sharing untuk memindahkan fail media.<br><br>

Untuk menyambungkan komputer menggunakan protokol SMB, ketuk 'Fail' 'Sambung ke storan awan' → SMB. Masukkan alamat IP komputer dan nama folder dikongsi dalam medan URL menggunakan format smb://computer-ip-address/shared-folder-name, masukkan log masuk dan kata laluan dan ketuk 'Selesai'. Jika sambungan anda berjaya, anda akan melihat storan yang disambungkan dalam bahagian 'Storan Awan'.<br><br>

Tutorial penuh tersedia di sini:<br>
[Pindahkan fail anda dari komputer ke iPhone menggunakan protokol SMB](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/)<br><br>

Untuk protokol WebDAV, semua langkah adalah sama kecuali medan URL. URL hendaklah dalam format http://server-name atau https://server-name jika pelayan menyokong SSL.<br><br>

Tutorial penuh tersedia di sini:<br>
[Cara Menyambung Storan NAS Menggunakan WebDAV dan Mendengar Muzik pada iPhone atau Mac Anda](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)<br><br>

Wi-Fi Drive ialah teknologi popular yang membolehkan anda memindahkan fail dari komputer ke peranti iOS secara wayarles menggunakan penyemak imbas desktop. Untuk menggunakan ciri ini, peranti dan komputer anda perlu disambungkan ke rangkaian Wi-Fi yang sama. Buka 'Fail' → 'Komputer' → 'Sambung menggunakan Wi-Fi' dan dayakan pelayan. Selepas ini, buka penyemak imbas desktop dan masukkan URL dari aplikasi. Anda boleh seret-jatuh fail dari komputer ke halaman web yang dibuka dan ia akan muncul pada peranti.<br>
Tutorial lebih terperinci tersedia di sini:<br>
[Cara memindahkan fail secara wayarles dari komputer ke iPhone menggunakan WiFi-Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)<br><br>

iTunes File Sharing ialah satu lagi teknologi yang membolehkan anda memindahkan fail dari komputer ke peranti menggunakan iTunes dan kabel kilat. Sambungkan sahaja peranti ke komputer menggunakan kabel dan jalankan iTunes. Buka iTunes → 'Bahagian Aplikasi' → dan cari Evervideo. Ketuk ikon apl untuk melihat folder dikongsi. Salin fail dari komputer ke folder dikongsi pada peranti.<br><br>

Arahan terperinci tersedia di sini:<br>
[Cara memainkan fail tempatan (fail iTunes) pada iPhone saya](/docs/howto/how-to-play-local-itunes-files-on-my-iphone)<br><br>

{{% /details %}}

{{% details title="Bagaimana saya menggunakan ciri Wi-Fi Drive dalam Evervideo?" closed="true" %}}

**Pemindahan wayarles menggunakan penyemak imbas desktop**<br>
1. Lancarkan apl: Buka Evervideo.<br>
2. Sambung melalui Wi-Fi: Pergi ke Fail → 'Komputer' → 'Sambung melalui Wi-Fi'.<br>
3. (Pilihan) Tambah keselamatan: Masukkan nama pengguna dan kata laluan jika diperlukan.<br>
4. Mulakan Wi-Fi Drive: Ketuk 'Mulakan Wi-Fi Drive' dan salin URL yang diberikan.<br>
5. Buka penyemak imbas (Safari, Chrome, Opera, Firefox, dll.) dan masukkan URL.<br>
6. Gunakan pengurus fail terbina dalam untuk memuat naik, memuat turun, menamakan semula, atau memadamkan fail. Anda boleh seret dan jatuh fail terus ke iPhone anda.<br>
7. Setelah selesai, ketuk 'Hentikan Wi-Fi Drive' pada iPhone anda.<br><br>

Nota: Pastikan JavaScript didayakan dan anda menggunakan versi penyemak imbas terkini untuk prestasi terbaik.<br><br>

**Pindahkan fail menggunakan Mac Finder**<br>
1. Dalam Finder, klik 'Pergi' → 'Sambung ke Pelayan…'.<br>
2. Masukkan URL pelayan yang ditunjukkan dalam apl Evervideo.<br>
3. Klik 'Sambung' dan urus fail pada iPhone anda seperti mana-mana pemacu rangkaian.<br><br>

**Pindahkan fail menggunakan Windows File Explorer**<br>
1. Klik kanan 'PC Ini' → 'Petakan Pemacu Rangkaian…'.<br>
2. Masukkan URL pelayan dari apl Evervideo dalam medan 'Folder'.<br>
3. Pilih huruf pemacu, klik 'Selesai', dan layari fail iPhone anda secara terus.<br><br>

[Baca lebih lanjut](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)

{{% /details %}}

{{% details title="Bagaimana saya menggunakan pemacu kilat USB atau kad SD dengan Evervideo pada iPhone?" closed="true" %}}
**Pasangkan pemacu ke iPhone, iPad, atau Mac anda melalui Lightning-to-USB, USB-C, atau pembaca kad, kemudian dalam Evervideo buka Fail → Fail pada iPhone Ini → Buka Folder, navigasi ke pemacu, dan pilih video.**<br><br>

Evervideo memainkan fail terus dari pemacu tanpa menyalinnya ke storan dalaman — sempurna untuk pustaka 4K atau HDR yang sangat besar. Berfungsi dengan pembaca kad Apple Certified.
{{% /details %}}

{{% details title="Bagaimana saya mengimport video dari pustaka Foto iOS?" closed="true" %}}
**Buka tab Pustaka Media → Pustaka Foto untuk melayari setiap video dalam apl Foto iOS anda, diatur mengikut Semua Video, Pendek, Sederhana, Panjang, Rakaman Skrin, dan Album Foto.**<br><br>

Anda tidak perlu menyalin apa-apa dari Foto — Evervideo memainkannya di tempat, dengan sokongan sari kata penuh, Picture-in-Picture, penyama, dan Chromecast/AirPlay. Rakaman kamera, klip yang di-AirDrop, album dikongsi iCloud, dan Album Pintar semuanya disertakan.
{{% /details %}}

{{% details title="Bagaimana saya mencari video, album, atau genre dalam Evervideo?" closed="true" %}}
**Ketuk ikon kaca pembesar dalam mana-mana senarai — Pustaka Media, Senarai Main, Album, Genre, Terkini, Kegemaran, atau dalam folder — dan taip nama untuk menapis keputusan dengan serta-merta.**<br><br>

Carian adalah setempat dan dijalankan terhadap pangkalan data pustaka video, jadi keputusan muncul semasa anda menaip walaupun pada rangkaian perlahan. Anda juga boleh mencari dalam senarai main, album, atau folder tertentu untuk mencari satu video di antara ratusan. Tajuk, album, genre, folder, dan senarai main semuanya boleh dicari.
{{% /details %}}

{{% details title="Bagaimana saya melihat video yang baru-baru ini ditonton dengan kemajuan main balik?" closed="true" %}}
**Buka tab Terkini (Evervideo dibuka di sini secara lalai) untuk melihat setiap video yang baru-baru ini anda tonton, masing-masing dengan lakaran kecil dan bar kemajuan tonton per-fail supaya anda boleh meneruskan mana-mana daripada mereka dengan satu ketukan.**<br><br>

Evervideo menjejaki kedudukan main balik setiap video yang anda tonton, jadi walaupun video yang anda tidak tandai secara eksplisit boleh dilanjutkan tepat di tempat anda berhenti. Tukar berapa banyak entri yang disimpan senarai Terkini melalui **Tetapan → Pustaka Media → Terkini → Tukar Saiz Senarai**. Anda juga boleh mengeksport senarai ke M3U, CSV, atau TXT untuk menyandarkan sejarah tontonan anda, atau membersihkannya dengan **Padam Senarai** untuk permulaan baharu.
{{% /details %}}

{{% details title="Bagaimana saya menambah video ke kegemaran dalam Evervideo?" closed="true" %}}
**Ketuk '...' pada mana-mana video dan pilih Tambah ke Kegemaran — kegemaran muncul di bawah Pustaka Media → Kegemaran dan, secara pilihan, di bawah Fail → Kegemaran.**<br><br>

Dayakan **Pengeditan Serentak** dalam **Tetapan → Pustaka Media → Kegemaran** untuk mencerminkan kegemaran antara bahagian pustaka media dan bahagian fail. Anda juga boleh mengeksport senarai kegemaran ke M3U, CSV, atau TXT untuk sandaran, dan mencapai kegemaran dari tab **Kegemaran** khusus dalam bar tab bawah.
{{% /details %}}

{{% details title="Bagaimana saya membuat senarai main pada Evervideo?" closed="true" %}}
- Buka bahagian Senarai Main.<br>
- Ketuk butang '+' atau butang '...' di sudut kanan atas dan pilih 'Senarai Main Baharu'.<br>
- Masukkan nama untuk senarai main dan ketuk 'Simpan'. Dialog 'Tambah Fail Media' akan muncul.<br>
- Pilih trek yang ingin anda tambahkan ke senarai main.<br><br>

{{% /details %}}

{{% details title="Bagaimana saya mengimport senarai main M3U, M3U8, atau CUE ke dalam Evervideo?" closed="true" %}}
**Buka tab Senarai Main, ketuk menu '...', pilih Import Senarai Main, kemudian pilih fail .m3u, .m3u8, atau .cue dari storan awan atau peranti anda.**<br><br>

Evervideo menghurai fail senarai main, mencari setiap video yang dirujuk pada storan anda, dan mencipta senarai main sebenar dalam pustaka anda. Pastikan laluan dalam fail senarai main sepadan dengan tempat fail video sebenarnya berada.
{{% /details %}}

{{% details title="Cara memainkan video yang Dimuat Turun secara tempatan pada iPhone?" closed="true" %}}
Setelah anda memasang aplikasi, buka skrin 'Fail' dan tatal ke bawah ke bahagian 'Fail pada iPhone ini'. Dari sana, pilih 'Buka fail...' jika anda perlu memilih beberapa fail atau 'Buka folder...' jika anda ingin memilih folder media. Apl akan mengimbas kandungan folder, dan semua fail media yang ditemui akan dipilih. Navigasi ke folder media anda, ketuk 'Buka' untuk mengesahkan pilihan anda, dan fail akan ditambahkan ke baris pemain. Fail-fail ini akan dimainkan terus dari lokasi yang dipilih tanpa disalin ke bundel aplikasi.<br><br>

**Menambah Folder ke Kegemaran untuk Akses Pantas**<br>
Ringkaskan proses dengan menambah folder yang terletak pada peranti anda ke kegemaran anda. Dengan cara ini, anda tidak perlu mengulangi langkah setiap kali anda mahu memainkan muzik. Buka skrin 'Fail', tatal ke bahagian 'Akses Pantas', dan ketuk 'Kegemaran' untuk mengakses skrin 'Fail Kegemaran'. Ketuk butang tindakan lanjut (tiga titik) di sudut kanan atas dan pilih 'Tambah Folder'. Navigasi ke folder yang anda inginkan dan ketuk 'Buka' untuk mengesahkan. Folder anda akan ditambahkan ke 'Fail Kegemaran', menyediakan akses pantas ke fail media anda.<br><br>

**Mengimport Fail Tempatan ke Pustaka**<br>
Jika anda lebih suka mengatur fail tempatan anda dalam pustaka anda, buka skrin 'Pustaka', ketuk butang tiga titik di sudut kanan atas, dan pilih '+ Tambah fail media'. Pilih item menu 'Fail pada peranti ini', dan ketuk 'Buka Fail...'. Pilih fail yang ingin anda tambahkan dan ketuk 'Buka' untuk mengesahkan. Apl akan mengimbas fail yang dipilih dan menambahkannya ke pustaka anda, mengaturnya mengikut metadata.<br><br>

**Menambah Fail Tempatan ke Senarai Main**<br>
Untuk menambah fail tempatan ke senarai main, buka skrin 'Senarai Main' dan ketuk butang lanjut di sudut kanan atas. Pilih '+ Senarai Main Baharu', masukkan nama untuk senarai main baharu anda, dan pada skrin seterusnya, pilih pilihan 'Fail pada peranti ini' dan ketuk 'Buka Fail...'. Pilih fail media yang ingin anda tambahkan dan ketuk 'Buka' untuk mengesahkan. Fail akan ditambahkan ke senarai main anda, di mana anda boleh menukar susunan trek dan melakukan tindakan lain menggunakan butang lanjut.<br><br>

{{% /details %}}

{{% details title="Bagaimana saya mendayakan mod luar talian dalam Evervideo?" closed="true" %}}
- Sambung ke Storan Awan:<br>
 • Pergi ke tab 'Fail'.<br>
 • Pilih 'Sambung ke storan awan' dan ikuti arahan untuk menyambung perkhidmatan yang anda inginkan.<br><br>

- Navigasi ke Folder Fail Media:<br>
 • Buka perkhidmatan storan awan yang disambungkan dan cari folder media anda.<br><br>

- Dayakan Mod Luar Talian:<br>
 • Ketuk butang 'Lebih banyak tindakan' di sebelah nama folder.<br>
 • Pilih 'Mengaktifkan mod luar talian'.<br><br>

- Muat Turun Kandungan:<br>
 • Folder yang dipilih dan semua kandungannya akan dimuat turun ke 'Fail' > 'Folder luar talian'.<br><br>

- Kemas Kini Automatik:<br>
 • Apl akan sentiasa mengimbas perubahan. Fail baharu yang ditambahkan ke folder dalam talian akan dimuat turun secara automatik.<br><br>

- Konfigurasi Tamat Masa Imbasan:<br>
 • Pergi ke 'Tetapan' > 'Pengurus fail' > 'Folder luar talian' > 'Selang masa' untuk menetapkan kekerapan imbasan.<br><br>

- Penyegerakan Manual:<br>
 • Untuk menyegerakkan secara manual, pergi ke 'Tetapan' > 'Pengurus fail' > 'Folder luar talian' > 'Folder luar talian yang diselaraskan'.<br>
 • Ketuk 'Lebih banyak tindakan' dan pilih 'Mulakan penyegerakan'.<br><br>

{{% /details %}}

{{% details title="Cara memuat turun video?" closed="true" %}}
Sebelum anda boleh memuat turun video dan menontonnya secara luar talian, anda perlu menyambung storan awan.<br>
Buka sahaja skrin 'Fail' dan sambungkan storan awan anda.<br>
Setelah anda menambahkannya, anda boleh memuat turun video anda dari awan.<br><br>

**Untuk memuat turun video dari awan**<br>
– Buka storan awan yang disambungkan.<br>
– Navigasi ke dalam folder yang ingin anda muat turun.<br>
– Ketuk butang tindakan lanjut '...' di sudut kanan atas dan pilih item menu 'Pilih'.<br>
– Pilih fail yang ingin anda muat turun dan ketuk butang 'Muat Turun'.<br><br>

**Untuk mendayakan mod luar talian untuk Artis/Senarai Main/Album**<br>
– Buka Skrin Artis/Album/Senarai Main<br>
– Ketuk kotak semak 'Mod luar talian'<br>
– Artis/Album/Senarai Main Luar Talian akan muncul dalam bahagian 'Fail' -> 'Folder luar talian'.<br><br>

Pilihan lain ialah memuat turun video dari YouTube dan mengimportnya ke dalam Evervideo, seperti yang diterangkan di sini:<br>
[Cara memuat turun muzik dari YouTube dan mendengar muzik luar talian pada iPhone](/docs/howto/how-to-download-music-from-youtube-and-listen-to-offline-music-on-iphone/)<br><br>

{{% /details %}}

{{% details title="Bolehkah saya menggunakan Evervideo tanpa sambungan internet?" closed="true" %}}
**Ya — setelah anda memuat turun video atau mendayakan mod luar talian untuk folder, Evervideo memainkan semuanya sepenuhnya luar talian.**<br><br>

Kandungan luar talian berada di bawah **Fail → Fail dalam Aplikasi Ini** dan terus berfungsi dalam mod kapal terbang, semasa penerbangan, dan di mana-mana tanpa Wi-Fi atau data selular. Video awan sahaja (yang tidak anda muat turun) akan digrekan sehingga anda mendapat semula sambungan. Untuk perjalanan, dayakan **Mod Luar Talian** untuk folder yang berkaitan atau muat turun video tertentu sebelum anda pergi.
{{% /details %}}

{{% details title="Bagaimana saya mendayakan mod gelap dalam Evervideo?" closed="true" %}}
**Buka Tetapan → Pemperibadian → Skim Warna, kemudian pilih Gelap, Terang, atau Lalai (yang mengikut penampilan sistem anda).**<br><br>

Anda juga boleh memilih ikon apl alternatif dalam **Tetapan → Pemperibadian → Ikon Aplikasi** (Premium), dan memilih poster kabur sebagai latar belakang apl di bawah **Gaya Latar Belakang**.
{{% /details %}}

{{% details title="Bagaimana saya menukar bahasa antara muka Evervideo?" closed="true" %}}
**Buka Tetapan → Bahasa, pilih dari lebih 120 bahasa yang disokong, kemudian mulakan semula apl untuk perubahan berkuat kuasa.**<br><br>

Apl ini menyokong penyetempatan termasuk Bahasa Inggeris, Perancis, Jerman, Sepanyol, Itali, Portugis, Rusia, Ukraine, Poland, Belanda, Arab, Ibrani, Hindi, Jepun, Korea, Cina (Ringkas dan Tradisional), Vietnam, Turki, dan banyak lagi. Pilih **Lalai** untuk mengikut tetapan bahasa peranti secara automatik.
{{% /details %}}

{{% details title="Bagaimana saya melindungi Evervideo dengan kod laluan?" closed="true" %}}
**Buka Tetapan → Kod Laluan, ketuk Dayakan, dan pilih kod 4 digit — anda akan diminta memasukkannya setiap kali apl dilancarkan.**<br><br>

Evervideo menggunakan kod laluan angka 4 digit tetap. Kod laluan menghalang sesiapa yang mempunyai akses ke peranti anda daripada membuka Evervideo dan melayari akaun awan yang disambungkan, video yang dimuat turun, dan pustaka. Gabungkannya dengan iOS Face ID/Touch ID pada peranti untuk perlindungan tambahan.
{{% /details %}}

{{% details title="Bagaimana saya mendayakan widget Evervideo pada Skrin Utama atau Skrin Kunci iPhone saya?" closed="true" %}}
**Dayakan kemas kini widget dalam Tetapan → Widget, kemudian tekan lama Skrin Utama atau Skrin Kunci anda, ketuk '+', cari 'Evervideo', dan pilih saiz widget.**<br><br>

Widget menunjukkan video yang sedang dimainkan dengan tajuk, poster, dan kawalan asas. Oleh kerana segar semula widget menggunakan sedikit tenaga, togol **Dayakan Widget** dimatikan secara lalai — hidupkan hanya jika anda menggunakan widget secara aktif. Widget berfungsi pada Skrin Utama dan Skrin Kunci iPhone dan iPad, dan pada macOS dalam Pusat Pemberitahuan.
{{% /details %}}

{{% details title="Bagaimana saya berkongsi Evervideo Premium dengan keluarga saya?" closed="true" %}}
**Semua pelan Evervideo Premium: seumur hidup, bulanan, dan tahunan berfungsi dengan Apple Family Sharing, jadi sesiapa dalam kumpulan keluarga anda boleh memasang Evervideo dan menggunakan Premium tanpa kos tambahan.**<br><br>

Sediakan Family Sharing dalam iOS/macOS **Tetapan → Keluarga**, kemudian minta setiap ahli keluarga memasang Evervideo dari App Store dan menjalankannya sekali semasa log masuk ke Apple ID mereka sendiri. Premium diiktiraf secara automatik dalam masa satu minit. Pelan yang sama dikongsi antara iPhone, iPad, dan Mac untuk setiap ahli keluarga.
{{% /details %}}

{{% details title="Bagaimana saya membatalkan langganan Evervideo Premium saya?" closed="true" %}}
**Buka iOS atau macOS Tetapan → [nama anda] → Langganan, cari Evervideo, dan ketuk Batal Langganan — ciri Premium anda kekal aktif sehingga akhir tempoh pengebilan semasa.**<br><br>

Pembelian dalam apl seumur hidup bukan langganan dan tidak perlu dibatalkan. Untuk bayaran balik, gunakan halaman **Laporkan Masalah** Apple (`reportaproblem.apple.com`) — bayaran balik dikeluarkan oleh Apple, bukan oleh Everappz.
{{% /details %}}

{{% details title="Bagaimana saya menyandarkan dan memulihkan pustaka Evervideo saya?" closed="true" %}}
**Buka Tetapan → Sandaran & Pulih, pilih apa yang hendak disertakan (Pangkalan Data, Penutup Album, Tetapan), ketuk 'Sandarkan Data Aplikasi', dan simpan fail sandaran — buka pada peranti lain untuk memulihkan.**<br><br>

Sandaran mengandungi entri pustaka media anda, senarai main, kegemaran, kemajuan tonton, tetapan, dan cache poster. Ia **tidak** termasuk fail video yang dimuat turun secara luar talian (ia akan menjadikan sandaran sangat besar). Pindahkan fail sandaran ke peranti baharu melalui iCloud Drive, AirDrop, atau mana-mana perkhidmatan awan yang disambungkan, kemudian buka dalam Evervideo untuk menggunakannya.
{{% /details %}}

{{% details title="Bagaimana saya membebaskan storan yang digunakan oleh Evervideo?" closed="true" %}}
**Buka Tetapan → Pengurus Fail → Padam Fail Sementara dan Tetapan → Pustaka Media → Penutup Album → Padam Semua untuk membersihkan cache; gunakan tab Fail untuk memadamkan video yang dimuat turun yang tidak lagi anda perlukan.**<br><br>

Anda juga boleh membuang folder luar talian individu dalam **Tetapan → Pengurus Fail → Folder Luar Talian yang Diselaraskan → '...' → Lumpuhkan Mod Luar Talian**, yang memadamkan salinan tempatan. Video strim sahaja tidak menggunakan storan peranti sama sekali. Membersihkan folder **Cache Pemain** di bawah **Fail → Fail dalam Aplikasi Ini** juga boleh membebaskan beberapa gigabait selepas main balik kandungan 4K kadar bit tinggi yang banyak.
{{% /details %}}

{{% details title="Mengapa video awan saya mengalami penyangga atau gagap?" closed="true" %}}
**Penyangga hampir selalu disebabkan oleh rangkaian perlahan, saiz fail besar, atau tetapan penimbal pemain yang rendah — tingkatkan Masa Pramuatan dan tukar ke rangkaian yang lebih pantas atau muat turun fail.**<br><br>

Beberapa petua praktikal:<br>

- **Tingkatkan penimbal** dalam **Tetapan → Player → File Loading → Masa Pramuatan** untuk kandungan 4K atau HEVC kadar bit tinggi.<br>
- **Tukar ke Wi-Fi** jika anda menggunakan selular, atau pindah lebih dekat ke penghala anda.<br>
- **Dayakan Penyahkodan Perkakasan** untuk H.264 dan HEVC dalam **Tetapan → Player → Video** supaya CPU bukan kesesakan.<br>
- **Muat turun fail untuk main balik luar talian** jika sumber lebih perlahan dari kelajuan tontonan anda — fail 4K besar boleh melebihi lebar jalur selular dengan mudah.<br>
- **Izinkan semula akaun awan anda** dalam tab Fail jika sambungan telah tamat tempoh.
{{% /details %}}

{{% details title="Bagaimana saya menghubungi sokongan Evervideo?" closed="true" %}}
**Buka Tetapan → Hantar Maklum Balas untuk menghantar e-mel terus ke pasukan sokongan kami dari apl, dengan maklumat diagnostik dilampirkan secara automatik.**<br><br>

Anda juga boleh melawat [Pusat Bantuan](/docs/), melayari [panduan Cara-buat](/docs/howto/), atau semak [FAQ](/docs/faq/) yang lebih luas untuk jawapan layan diri. Kami biasanya membalas dalam satu hari perniagaan.
{{% /details %}}

</div>
