---
title: "Eksport Sejarah Pendengaran Lengkap dari Evermusic & Flacbox ke Last.fm"
date: 2024-01-30
description: "Ketahui cara mengeksport sejarah muzik anda dari Evermusic dan Flacbox dan memuat naiknya ke Last.fm menggunakan fail CSV dan alat Last.fm Scrubbler untuk Windows."
keywords: ["evermusic", "flacbox", "lastfm", "sejarah muzik", "scrobbling", "eksport lagu", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "terkini", "lastfm", "eksport", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Ringkasan:** Eksport sejarah pendengaran anda dari Evermusic atau Flacbox sebagai fail CSV, kemudian muat naik ke Last.fm menggunakan alat percuma Last.fm-Scrubbler-WPF pada Windows. Scrobbling automatik juga tersedia secara asli dalam kedua-dua aplikasi.

**Kemas kini:** Scrobbling automatik kini tersedia! Ketahui lebih lanjut di sini: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling ialah cara mudah untuk menyimpan butiran asas secara automatik seperti tajuk dan artis lagu yang sedang anda mainkan ke perkhidmatan dalam talian. Kemudian, anda boleh menyemak sejarah pendengaran anda.

[Last.fm](https://www.last.fm/home), dikuasakan oleh sistem pengesyoran muzik yang dipanggil Audioscrobbler, menawarkan perkhidmatan ini secara percuma. Ia mencipta profil terperinci mengenai citarasa muzik anda dengan merekodkan trek yang anda dengar, sama ada dari stesen radio internet, komputer anda, atau pelbagai peranti muzik mudah alih. Anda boleh melawat laman web kemudian untuk menerima cadangan artis atau album baharu yang sepadan dengan citarasa muzik anda.

Anda boleh memuat naik sejarah pendengaran anda ke [Last.fm](http://Last.fm) dari aplikasi Evermusic dan Flacbox menggunakan alat percuma, dan kami akan membimbing anda cara melakukannya.

Buka bahagian 'Pustaka Muzik' dalam aplikasi dan tatal ke bahagian 'Akses pantas'. Ketik item menu 'Terkini'.

![skrin pustaka muzik](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Pada skrin 'Terkini', ketik butang 'Lagi' di sudut kanan atas untuk mengaktifkan menu 'Lebih banyak tindakan'. Ketik item menu 'Eksport senarai lagu'.

![skrin terkini](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Pada skrin 'Pilih format fail', anda mempunyai pilihan untuk memilih format fail destinasi. Pilihan yang tersedia - CSV, TXT, M3U.

![skrin pilih format fail](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Ini bermaksud Comma-Separated Values, sesuai untuk menyusun data anda dalam format jadual yang kemas. Dalam fail destinasi, anda akan menemui parameter seperti Nama Artis, Nama Album, Nama Trek, Cap Masa (masa anda mendengar trek), Nama Artis Album, dan Tempoh Trek.

TXT: Di sini, kita bercakap tentang fail teks biasa. Ia mudah dan ringkas, dengan parameter termasuk Nama Artis, Nama Album, Nama Trek, dan Tempoh.

M3U: Format ini pada dasarnya adalah pilihan utama untuk mencipta senarai main. Ia bagus kerana anda boleh mengeksport senarai lagu anda dan menikmati trek anda pada mana-mana peranti, walaupun anda tidak mempunyai fail asal (dengan syarat anda memilih pilihan URL mutlak untuk fail media). Dalam fail output, anda akan menemui parameter seperti Tempoh, Nama Artis, Nama Trek, dan Lokasi Fail Media.

Untuk tugasan kita, memilih CSV adalah pilihan terbaik. Kita akan menggunakan fail ini dengan perisian percuma Last.fm-Scrubbler-WPF untuk memuat naik sejarah pendengaran kita ke perkhidmatan [Last.fm](http://Last.fm). Cukup pilih CSV dan tekan butang 'Eksport'.

![skrin eksport selesai](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Selepas eksport selesai, cukup ketik butang 'Tunjukkan fail', dan aplikasi akan mendedahkan fail yang dicipta dalam folder dokumen anda. Kemudian, ketik butang 'Lebih banyak tindakan' di sebelah nama fail dan pilih pilihan 'Buka dalam' dari menu. Langkah seterusnya adalah menyalin fail yang dieksport ke komputer meja anda. Anda boleh melakukannya dengan mudah dengan memilih pilihan AirDrop dari menu 'Buka dalam'.

![lebih banyak tindakan untuk fail yang dieksport](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Seterusnya, kita akan menggunakan klien sumber terbuka percuma [Last.FM](http://Last.FM) yang hanya tersedia pada platform Windows. Klien ini membolehkan anda mengemas kini sejarah pendengaran anda di [Last.FM](http://Last.FM) dengan cekap menggunakan fail CSV yang baru kita eksport.

Sekarang, jika anda tidak sedang menggunakan komputer Windows, jangan risau. Anda masih boleh mengakses klien ini dengan memasang VirtualBox pada Mac anda dan menggunakan fail imej persekitaran pembangunan Windows rasmi.

Inilah yang perlu anda lakukan:

- Pasang VirtualBox dari pautan berikut: [Muat Turun VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Muat turun dan pasang persekitaran pembangunan Windows dari pautan ini: [Persekitaran Pembangunan Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Pada komputer Windows anda (atau aplikasi VirtualBox dengan imej Pembangunan Windows) muat turun dan pasang [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - perisian sumber terbuka percuma yang tersedia di GitHub. Kami menguji pada versi 1.28 yang boleh anda muat turun di sini: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Halaman muat turun Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Di bawah bahagian 'Assets', ketik pada [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) untuk memuat turun arkib pemasangan. Nyaharkib fail yang dimuat turun dan buka folder yang dinyaharkib.

- PENTING

Aplikasi ini masih dalam beta. Pencipta aplikasi tidak mendapat banyak ujian. Mereka mengesyorkan mencuba scrobble ke akaun ujian terlebih dahulu dan lihat sama ada perkara yang anda ingin scrobble berfungsi dengan betul. Terutamanya jika anda scrobble banyak trek sekaligus. Sila berhati-hati dengan akaun anda.

Jalankan Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Pada skrin utama aplikasi, cukup ketik pada 'Belum log masuk,' yang terletak di sudut kiri bawah, untuk mengaktifkan skrin 'Tambah akaun'.

![Skrin tambah akaun](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Masukkan kelayakan log masuk anda.

![skrin masukkan kelayakan log masuk](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Ketik butang 'Log Masuk' untuk menambah akaun anda.

![Ketik butang Log Masuk untuk menambah akaun anda.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Buka tab 'File Parse Scrobbler' untuk mula mengimport fail CSV dari aplikasi Evermusic.

![Buka tab File Parse Scrobbler untuk mula mengimport fail CSV dari aplikasi Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Pilih 'Parser: CSV' dan ketik butang 'Settings'.

Pada skrin seterusnya, anda boleh memilih susunan parameter pada fail CSV anda.

Medan individu boleh dilampirkan dengan tanda petik dan PERLU dilampirkan dengan tanda petik jika medan mengandungi mana-mana pembatas yang ditetapkan. Contohnya:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Jadi biarkan semua tetapan secara lalai, satu-satunya perkara yang perlu anda ubah adalah mengaktifkan kotak semak dalam medan 'Has Fields Enclosed In Quotes'.

Ketik 'Save & Close' untuk menerapkan perubahan.

![pilih susunan parameter pada fail CSV anda.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Scrobbling penghuraian fail mempunyai dua mod. Ia boleh ditukar dengan ComboBox 'Scrobbling Mode'.

Mod Normal: Dalam mod ini, trek akan di-scrobble dengan cap masa dari scrobble yang dihuraikan. Hanya scrobble yang lebih baharu daripada 14 hari boleh di-scrobble.

Mod Import: Dalam mod ini, trek akan di-scrobble dengan cap masa yang dikira dari 'Finish Time' dan tempoh yang dipilih antara setiap trek. Ini membolehkan scrobbling trek walaupun cap masa scrobble yang dihuraikan lebih lama daripada 14 hari. Oleh itu, trek pertama (paling atas) dalam fail CSV akan di-scrobble dengan 'Finish Time'.

Pilih fail CSV yang dijana sebelum ini dari aplikasi Evermusic dalam medan 'File:' dan ketik 'Parse'. Dalam sesetengah kes, anda mungkin melihat amaran ralat yang mengatakan beberapa scrobble tidak dapat dihuraikan. Ia tidak mengapa jika anda mempunyai beberapa trek tanpa metadata lengkap seperti Nama Artis.

![beberapa scrobble tidak dapat dihuraikan](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Ketik butang 'Check All' untuk memilih semua trek yang dihuraikan.

![Ketik butang Check All untuk memilih semua trek yang dihuraikan.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Ketik butang 'Preview' untuk menyemak semua perubahan yang akan dihantar ke pelayan.

![Ketik butang Preview untuk menyemak semua perubahan yang akan dihantar ke pelayan.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Ketik butang 'Scrobble' untuk memuat naik semua perubahan ke pelayan.

![Ketik butang Scrobble untuk memuat naik semua perubahan ke pelayan.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Sebelum ini Last.fm-Scrubbler-WPF tidak mempunyai had scrobble sehari. Ini kini telah berubah kerana sesetengah orang menggunakan Scrubbler untuk scrobble begitu banyak trek sehingga menyebabkan masalah untuk halaman Last.fm. Had scrobble kini adalah 2800 scrobble sehari. Apabila anda cuba scrobble lebih daripada itu, anda akan mendapat mesej ralat. Terdapat rancangan untuk menambah 'baris gilir scrobble', jadi jika anda perlu scrobble lebih daripada 2800 trek, ia akan ditambah ke baris gilir dan di-scrobble secara automatik selepas beberapa ketika. Anda boleh menyemak berapa banyak scrobble yang tinggal dalam paparan pemilihan pengguna.

Setelah semua rekod berjaya dimuat naik ke pelayan, anda akan melihat mesej di bahagian bawah tetingkap aplikasi yang mengesahkan: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Kini anda boleh membuka profil anda di halaman [Last.fm](http://Last.fm) dan menyemak semua perubahan.

![profil anda di halaman Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Soalan Lazim

{{% details title="Bolehkah saya scrobble secara automatik tanpa mengeksport fail CSV?" closed="true" %}}
Ya. Kedua-dua Evermusic dan Flacbox kini menyokong scrobbling automatik ke Last.fm. Lihat panduan: [Cara Scrobble ke Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Bagaimana jika CSV saya mempunyai trek yang lebih lama daripada 14 hari?" closed="true" %}}
Gunakan Mod Import dalam Last.fm-Scrubbler-WPF. Ia mengira semula cap masa dari Finish Time, membolehkan anda scrobble trek tanpa mengira tarikh asalnya.
{{% /details %}}

{{% details title="Saya tidak mempunyai komputer Windows. Bolehkah saya masih menggunakan Last.fm-Scrubbler?" closed="true" %}}
Ya. Pasang VirtualBox pada Mac anda dan muat turun imej Persekitaran Pembangunan Windows percuma dari Microsoft. Jalankan Last.fm-Scrubbler-WPF di dalam mesin maya.
{{% /details %}}

{{% details title="Mengapa sesetengah scrobble tidak dihuraikan?" closed="true" %}}
Trek yang tiada metadata penting (seperti nama artis) tidak boleh dihuraikan. Ini dijangka dan tidak menjejaskan trek lain dalam fail.
{{% /details %}}

{{% details title="Adakah had scrobble harian?" closed="true" %}}
Ya. Last.fm-Scrubbler-WPF membenarkan sehingga 2,800 scrobble sehari. Jika anda perlu scrobble lebih banyak, bahagikan proses merentasi beberapa hari.
{{% /details %}}
