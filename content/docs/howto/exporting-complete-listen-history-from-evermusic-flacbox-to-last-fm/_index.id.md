---
title: "Ekspor Riwayat Mendengarkan Lengkap dari Evermusic & Flacbox ke Last.fm"
date: 2024-01-30
description: "Pelajari cara mengekspor riwayat musik Anda dari Evermusic dan Flacbox dan mengunggahnya ke Last.fm menggunakan file CSV dan alat Last.fm Scrubbler untuk Windows."
keywords: ["evermusic", "flacbox", "lastfm", "riwayat musik", "scrobbling", "ekspor lagu", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "terbaru", "lastfm", "ekspor", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Ringkasan:** Ekspor riwayat mendengarkan Anda dari Evermusic atau Flacbox sebagai file CSV, lalu unggah ke Last.fm menggunakan alat gratis Last.fm-Scrubbler-WPF di Windows. Scrobbling otomatis juga tersedia secara bawaan di kedua aplikasi.

**Pembaruan:** Scrobbling otomatis sekarang tersedia! Pelajari lebih lanjut di sini: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling adalah cara sederhana untuk secara otomatis menyimpan detail dasar seperti judul dan artis lagu yang sedang Anda putar ke layanan online. Nantinya, Anda dapat meninjau riwayat mendengarkan Anda.

[Last.fm](https://www.last.fm/home), didukung oleh sistem rekomendasi musik bernama Audioscrobbler, menawarkan layanan ini secara gratis. Layanan ini membuat profil terperinci tentang selera musik Anda dengan merekam lagu yang Anda dengarkan, baik dari stasiun radio internet, komputer Anda, atau berbagai perangkat musik portabel. Anda dapat mengunjungi situs web nanti untuk menerima rekomendasi artis atau album baru yang sesuai dengan selera musik Anda.

Anda dapat mengunggah riwayat mendengarkan ke [Last.fm](http://Last.fm) dari aplikasi Evermusic dan Flacbox menggunakan alat gratis, dan kami akan memandu Anda melalui prosesnya.

Buka bagian 'Pustaka Musik' aplikasi dan gulir ke bagian 'Akses cepat'. Ketuk item menu 'Terbaru'.

![layar pustaka musik](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Di layar 'Terbaru' ketuk tombol 'Lainnya' di sudut kanan atas untuk mengaktifkan menu 'Lebih banyak tindakan'. Ketuk item menu 'Ekspor daftar lagu'.

![layar terbaru](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Di layar 'Pilih format file' Anda memiliki kemungkinan untuk memilih format file tujuan. Opsi yang tersedia - CSV, TXT, M3U.

![layar pilih format file](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Singkatan dari Comma-Separated Values, sempurna untuk mengatur data Anda ke dalam format tabel yang rapi. Di file tujuan, Anda akan menemukan parameter seperti Nama Artis, Nama Album, Nama Lagu, Stempel Waktu (waktu Anda mendengarkan lagu), Nama Artis Album, dan Durasi Lagu.

TXT: Di sini, kita berbicara tentang file teks biasa. Sederhana dan langsung, dengan parameter termasuk Nama Artis, Nama Album, Nama Lagu, dan Durasi.

M3U: Format ini pada dasarnya adalah standar untuk membuat daftar putar. Bagus karena Anda dapat mengekspor daftar lagu dan menikmati lagu Anda di perangkat apa pun, bahkan jika Anda tidak memiliki file asli (asalkan Anda memilih opsi URL absolut untuk file media). Di file output, Anda akan menemukan parameter seperti Durasi, Nama Artis, Nama Lagu, dan Lokasi File Media.

Untuk tugas kita, memilih CSV adalah cara yang tepat. Kita akan menggunakan file ini dengan perangkat lunak gratis Last.fm-Scrubbler-WPF untuk mengunggah riwayat mendengarkan kita ke layanan [Last.fm](http://Last.fm). Cukup pilih CSV dan tekan tombol 'Ekspor'.

![layar ekspor selesai](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Setelah ekspor selesai, cukup ketuk tombol 'Tampilkan file', dan aplikasi akan menampilkan file yang dibuat di folder dokumen Anda. Kemudian, ketuk tombol 'Lebih banyak tindakan' di sebelah nama file dan pilih opsi 'Buka di' dari menu. Langkah selanjutnya adalah menyalin file yang diekspor ke komputer desktop Anda. Anda dapat dengan mudah melakukannya dengan memilih opsi AirDrop dari menu 'Buka di'.

![lebih banyak tindakan untuk file yang diekspor](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Selanjutnya, kita akan menggunakan klien [Last.FM](http://Last.FM) gratis sumber terbuka yang hanya tersedia di platform Windows. Klien ini memungkinkan Anda memperbarui riwayat mendengarkan Anda secara efisien di [Last.FM](http://Last.FM) menggunakan file CSV yang baru saja kita ekspor.

Sekarang, jika Anda saat ini tidak menggunakan komputer Windows, jangan khawatir. Anda masih dapat mengakses klien ini dengan menginstal VirtualBox di Mac Anda dan menggunakan file gambar lingkungan pengembangan Windows resmi.

Berikut yang perlu Anda lakukan:

- Instal VirtualBox dari tautan berikut: [Unduh VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Unduh dan instal lingkungan pengembangan Windows dari tautan ini: [Lingkungan Pengembangan Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Di komputer Windows Anda (atau aplikasi VirtualBox dengan gambar Windows Development) unduh dan instal [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - perangkat lunak gratis sumber terbuka yang tersedia di GitHub. Kami menguji versi 1.28 yang dapat Anda unduh di sini: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![halaman unduh Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Di bagian 'Assets' ketuk [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) untuk mengunduh arsip instalasi. Ekstrak file yang diunduh dan buka folder yang diekstrak.

- PENTING

Aplikasi ini masih dalam tahap beta. Pembuat aplikasi belum melakukan banyak pengujian. Mereka merekomendasikan untuk mencoba scrobble ke akun uji coba terlebih dahulu dan melihat apakah hal-hal yang ingin Anda scrobble berjalan dengan benar. Terutama jika Anda scrobble banyak lagu sekaligus. Harap berhati-hati dengan akun Anda.

Jalankan Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Di layar utama aplikasi, cukup ketuk 'Belum masuk', yang terletak di sudut kiri bawah, untuk mengaktifkan layar 'Tambah akun'.

![layar tambah akun](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Masukkan kredensial login Anda.

![layar masukkan kredensial login](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Ketuk tombol 'Login' untuk menambahkan akun Anda.

![Ketuk tombol Login untuk menambahkan akun Anda.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Buka tab 'File Parse Scrobbler' untuk mulai mengimpor file CSV dari aplikasi Evermusic.

![Buka tab File Parse Scrobbler untuk mulai mengimpor file CSV dari aplikasi Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Pilih 'Parser: CSV' dan ketuk tombol 'Pengaturan'.

Di layar berikutnya, Anda dapat memilih urutan parameter di file CSV Anda.

Field individual dapat diapit oleh tanda kutip dan HARUS diapit oleh tanda kutip jika field mengandung salah satu delimiter yang ditetapkan. Contoh:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Jadi biarkan semua pengaturan secara default, satu-satunya hal yang perlu Anda ubah adalah mengaktifkan kotak centang di field 'Has Fields Enclosed In Quotes'.

Ketuk 'Simpan & Tutup' untuk menerapkan perubahan.

![pilih urutan parameter di file CSV Anda.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Scrobbling parse file memiliki dua mode. Dapat diubah dengan ComboBox 'Scrobbling Mode'.

Mode Normal: Dalam mode ini, lagu akan di-scrobble dengan stempel waktu dari scrobble yang diparse. Hanya scrobble yang lebih baru dari 14 hari yang dapat di-scrobble.

Mode Impor: Dalam mode ini, lagu akan di-scrobble dengan stempel waktu yang dihitung dari 'Waktu Selesai' dan durasi yang dipilih antara setiap lagu. Ini memungkinkan scrobbling lagu bahkan jika stempel waktu scrobble yang diparse lebih lama dari 14 hari. Oleh karena itu lagu pertama (paling atas) di file CSV akan di-scrobble dengan 'Waktu Selesai'.

Pilih file CSV yang sebelumnya dihasilkan dari aplikasi Evermusic di field 'File:' dan ketuk 'Parse'. Dalam beberapa kasus, Anda mungkin melihat peringatan error yang mengatakan bahwa beberapa scrobble tidak dapat diparse. Tidak apa-apa jika Anda memiliki beberapa lagu tanpa metadata lengkap seperti Nama Artis.

![beberapa scrobble tidak dapat diparse](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Ketuk tombol 'Pilih Semua' untuk memilih semua lagu yang diparse.

![Ketuk tombol Pilih Semua untuk memilih semua lagu yang diparse.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Ketuk tombol 'Pratinjau' untuk memeriksa semua perubahan yang akan diposting ke server.

![Ketuk tombol Pratinjau untuk memeriksa semua perubahan yang akan diposting ke server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Ketuk tombol 'Scrobble' untuk mengunggah semua perubahan ke server.

![Ketuk tombol Scrobble untuk mengunggah semua perubahan ke server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Sebelumnya Last.fm-Scrubbler-WPF tidak memiliki batas scrobble per hari. Ini sekarang telah berubah karena beberapa orang menggunakan Scrubbler untuk scrobble begitu banyak lagu sehingga menyebabkan masalah pada halaman Last.fm. Batas scrobble saat ini adalah 2800 scrobble per hari. Ketika Anda mencoba scrobble lebih dari itu Anda akan mendapat pesan error. Ada rencana untuk menambahkan 'antrian scrobble', jadi jika Anda perlu scrobble lebih dari 2800 lagu, mereka akan ditambahkan ke antrian dan secara otomatis di-scrobble setelah beberapa waktu. Anda dapat memeriksa berapa banyak scrobble yang tersisa di tampilan pemilihan pengguna.

Setelah semua rekaman berhasil diunggah ke server, Anda akan melihat pesan di bagian bawah jendela aplikasi yang mengonfirmasi: 'Lagu yang dipilih berhasil di-scrobble.'

![Lagu yang dipilih berhasil di-scrobble.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Sekarang Anda dapat membuka profil Anda di halaman [Last.fm](http://Last.fm) dan memeriksa semua perubahan.

![profil Anda di halaman Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## FAQ

{{% details title="Bisakah saya scrobble secara otomatis tanpa mengekspor file CSV?" closed="true" %}}
Ya. Baik Evermusic maupun Flacbox sekarang mendukung scrobbling Last.fm otomatis. Lihat panduan: [Cara Scrobble ke Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Bagaimana jika CSV saya memiliki lagu yang lebih lama dari 14 hari?" closed="true" %}}
Gunakan Mode Impor di Last.fm-Scrubbler-WPF. Mode ini menghitung ulang stempel waktu dari Waktu Selesai, memungkinkan Anda scrobble lagu terlepas dari tanggal aslinya.
{{% /details %}}

{{% details title="Saya tidak punya komputer Windows. Bisakah saya tetap menggunakan Last.fm-Scrubbler?" closed="true" %}}
Ya. Instal VirtualBox di Mac Anda dan unduh gambar lingkungan pengembangan Windows gratis dari Microsoft. Jalankan Last.fm-Scrubbler-WPF di dalam mesin virtual.
{{% /details %}}

{{% details title="Mengapa beberapa scrobble tidak diparse?" closed="true" %}}
Lagu yang tidak memiliki metadata penting (seperti nama artis) tidak dapat diparse. Ini diharapkan dan tidak mempengaruhi lagu lain di file.
{{% /details %}}

{{% details title="Apakah ada batas scrobble harian?" closed="true" %}}
Ya. Last.fm-Scrubbler-WPF memungkinkan hingga 2.800 scrobble per hari. Jika Anda perlu scrobble lebih banyak, bagi prosesnya ke beberapa hari.
{{% /details %}}
