---
title: "Cara Mengaktifkan DLNA Media Server di Windows 10 dan Memutar Musik di iPhone"
date: 2019-11-26
description: "Aktifkan server DLNA di Windows 10 dan streaming musik ke iPhone dengan aplikasi Evermusic. Panduan pengaturan langkah demi langkah disertakan."
keywords: ["evermusic", "dlna", "windows 10", "streaming musik iphone", "server media", "jaringan lokal", "upnp"]
tags: ["evermusic", "musik", "cloud", "iphone", "penyimpanan", "lokal", "nas", "windows", "wifi", "dengarkan", "jaringan", "jarak jauh", "rumah", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Ringkasan:** Windows 10 memiliki server DLNA bawaan. Aktifkan di pengaturan Jaringan dan Berbagi, lalu gunakan aplikasi gratis **Evermusic** di iPhone Anda untuk streaming seluruh perpustakaan musik melalui Wi-Fi. Tidak perlu perangkat lunak server pihak ketiga.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Sampul Depan" caption="Streaming musik DLNA ke iPhone menggunakan Windows 10 dan Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) adalah alat yang kuat yang memungkinkan Anda dengan mudah streaming berbagai konten media, termasuk musik, antara perangkat yang mendukung DLNA di jaringan Anda. Kabar baiknya adalah Windows 10, dan versi sebelumnya, dilengkapi fitur DLNA bawaan, menghilangkan kebutuhan server media pihak ketiga. Berikut cara mengaktifkan DLNA Media Server di Windows 10 dan menikmati streaming musik di iPhone Anda.

## Cara Mengaktifkan DLNA Media Server di Windows 10

1. Klik tombol 'Start'.  
2. Pilih ikon 'Pengaturan'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Pengaturan Server" caption="Buka Pengaturan Windows" width="500" >}}

3. Di layar 'Pengaturan Windows', pilih 'Jaringan & Internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Pengaturan Windows" caption="Pilih Jaringan & Internet" width="500" >}}

4. Di bawah 'Jaringan', pilih 'Pusat Jaringan dan Berbagi'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Pusat Berbagi" caption="Buka Pusat Jaringan dan Berbagi" width="500" >}}

5. Di layar 'Pusat Jaringan dan Berbagi', klik 'Ubah pengaturan berbagi lanjutan' di menu kiri.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Pengaturan Berbagi Lanjutan" caption="Ubah pengaturan berbagi lanjutan" width="500" >}}

6. Di layar 'Pengaturan berbagi lanjutan', gulir ke bawah ke bagian 'Semua Jaringan' dan perluas dengan mengklik panah.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Aktifkan Penemuan" caption="Perluas pengaturan semua jaringan" width="500" >}}

7. Klik 'Aktifkan streaming media' untuk mengaktifkan server DLNA.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Aktifkan Server" caption="Aktifkan server streaming media" width="500" >}}

8. Beri nama perpustakaan media Anda dan pilih perangkat yang diizinkan mengaksesnya.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Nama Perpustakaan Media" caption="Beri nama perpustakaan media DLNA Anda" width="500" >}}

9. Klik 'OK' untuk mengonfirmasi. Sekarang, folder pribadi Anda seperti Musik, Gambar, dan Video akan terlihat oleh perangkat streaming apa pun dengan dukungan UPnP.

## Cara Menonaktifkan DLNA Media Server di Windows 10

1. Klik 'Start' dan ketik 'services' di kolom pencarian.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Layanan Windows" caption="Buka Layanan Windows" width="500" >}}

2. Di layar 'Layanan', gulir ke bawah untuk menemukan 'Windows Media Player Network Sharing Service'.  
3. Klik dua kali dan atur 'Jenis startup' ke 'Manual'.  
4. Hentikan layanan dengan mengklik tombol 'Berhenti'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Hentikan Layanan DLNA" caption="Nonaktifkan layanan berbagi jaringan DLNA" width="500" >}}

## Cara Memutar Musik dari Server DLNA di iPhone

1. Instal aplikasi gratis **Evermusic** dari App Store:  
   [Aplikasi Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Buka tab 'Koneksi' dan ketuk item 'Perangkat tersedia' di bagian 'Jaringan Lokal'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Koneksi Evermusic" caption="Evermusic: layar Koneksi" width="500" >}}

3. Tunggu beberapa detik saat daftar perangkat dimuat dan ketuk server Windows Media Player DLNA (misalnya, 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Perangkat Tersedia" caption="Server DLNA tersedia di Evermusic" width="500" >}}

4. Anda akan melihat daftar folder yang tersedia di server media.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Folder Evermusic" caption="Jelajahi folder bersama dari server DLNA" width="500" >}}

5. Buka folder apa pun yang berisi file audio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Isi Folder" caption="Lihat isi folder DLNA bersama" width="500" >}}

6. Ketuk file apa pun untuk memulai pemutar audio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Pemutar Audio" caption="Putar file audio dari DLNA di Evermusic" width="500" >}}

7. Untuk meningkatkan pengalaman audio Anda, ketuk ikon 'Equalizer' di dekat indikator volume di bagian bawah layar untuk mengaktifkan equalizer gaya iPod dengan preamplifier.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Equalizer" caption="Gunakan equalizer bawaan untuk pemutaran yang lebih baik" width="500" >}}

## Kesimpulan

Dengan DLNA Media Server di Windows 10 dan Evermusic di iPhone Anda, Anda dapat menikmati streaming musik yang mulus dari komputer ke perangkat seluler Anda. Ucapkan selamat tinggal pada keterbatasan penyimpanan dan sambut musik sesuai permintaan!

## Pertanyaan yang Sering Diajukan

{{% details title="Apakah saya perlu menginstal perangkat lunak server di Windows 10?" closed="true" %}}
Tidak. Windows 10 sudah menyertakan server media DLNA bawaan. Anda hanya perlu mengaktifkan streaming media di pengaturan Pusat Jaringan dan Berbagi. Tidak diperlukan perangkat lunak pihak ketiga.
{{% /details %}}

{{% details title="Apakah iPhone saya harus berada di jaringan Wi-Fi yang sama?" closed="true" %}}
Ya. Streaming DLNA bekerja melalui jaringan lokal Anda. Baik PC Windows 10 maupun iPhone Anda harus terhubung ke jaringan Wi-Fi yang sama agar Evermusic dapat menemukan server DLNA.
{{% /details %}}

{{% details title="Format audio apa yang bisa saya streaming melalui DLNA?" closed="true" %}}
Server Windows DLNA membagikan file dari folder Musik Anda terlepas dari formatnya. Evermusic mendukung MP3, FLAC, AAC, WAV, OGG, AIFF, dan banyak format lainnya, sehingga Anda dapat memutar hampir semua file audio dari server.
{{% /details %}}

{{% details title="Bisakah saya menggunakan Flacbox sebagai pengganti Evermusic?" closed="true" %}}
Ya. Flacbox juga mendukung penjelajahan dan pemutaran DLNA/UPnP. Anda dapat menggunakan salah satu aplikasi untuk menemukan dan memutar musik dari server Windows DLNA Anda.
{{% /details %}}

{{% details title="Apakah streaming DLNA menggunakan data seluler?" closed="true" %}}
Tidak. DLNA beroperasi sepenuhnya di jaringan Wi-Fi lokal Anda. Tidak menggunakan data seluler apa pun. Namun, kedua perangkat harus tetap terhubung ke jaringan yang sama selama pemutaran.
{{% /details %}}
