---
title: "Cara Menyambungkan Synology NAS dan Mendengar Muzik di iPhone atau Mac Anda"
date: 2024-09-19
description: "Ketahui cara menyambungkan Synology NAS anda menggunakan API natif atau QuickConnect dan strim muzik berkualiti tinggi ke iPhone atau Mac anda dengan Evermusic dan Flacbox."
keywords: ["synology nas", "strim muzik", "quickconnect", "evermusic synology", "flacbox synology", "pemain muzik nas", "muzik nas iphone"]
tags: ["muzik", "penstriman", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Ringkasan:** Sambungkan Synology NAS anda ke Evermusic atau Flacbox menggunakan API natif Synology -- sama ada secara manual melalui alamat IP atau secara automatik melalui QuickConnect ID. QuickConnect membolehkan anda menstrim muzik dari jauh tanpa pemajuan port. Kedua-dua aplikasi menyokong FLAC, MP3, WAV dan format resolusi tinggi yang lain.

Jika anda mencari cara yang lancar untuk menyambungkan Synology NAS anda dan menikmati perpustakaan muzik anda di iPhone atau Mac, aplikasi Evermusic dan Flacbox adalah penyelesaian yang sempurna. Aplikasi ini menyokong pelbagai format audio, termasuk FLAC, MP3 dan WAV, menjadikannya mudah untuk menstrim dan mendengar muzik berkualiti tinggi terus dari Synology NAS anda.

Dalam panduan ini, kami akan menunjukkan cara menyambungkan Synology NAS anda ke aplikasi Evermusic atau Flacbox menggunakan API natif Synology dan ciri QuickConnect. Dengan memanfaatkan API langsung Synology, anda boleh mengakses perpustakaan muzik anda dengan selamat di luar rangkaian rumah tanpa memerlukan konfigurasi rumit seperti WebDAV, SMB, DLNA. Dengan QuickConnect, anda boleh menstrim dan menguruskan muzik anda dari mana-mana sahaja, menggunakan iPhone atau Mac anda.

## Langkah 1: Konfigurasikan Kebenaran Folder Kongsi (Pilihan)

1. Buka **Panel Kawalan** dan pergi ke bahagian **Folder Kongsi**.

![Folder Kongsi](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Pilih folder **Music** dan klik **Edit**.

3. Dalam tab **Kebenaran**, konfigurasikan kebenaran. Aktifkan akses tetamu dengan Baca sahaja jika anda hanya perlu mendengar muzik, atau Baca/Tulis jika anda perlu mengubah suai fail. Simpan perubahan.

![Kebenaran](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Langkah 2: Cari Alamat IP Synology NAS

1. Buka **Panel Kawalan** dan pergi ke tab **Antara Muka Rangkaian**.

![Antara Muka Rangkaian](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Atau gunakan pelayar web anda untuk melawati [find.synology.com](http://find.synology.com).

![Cari Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Catatkan alamat IP Synology NAS anda (contohnya, 192.168.18.137).

## Langkah 3: Cari Port Rangkaian Synology NAS

Anda boleh mencari dokumentasi rasmi Synology untuk port rangkaian lalai DSM di [artikel Pusat Pengetahuan Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services) ini.

Synology DSM menggunakan port lalai berikut:
- **HTTP (Akses Web):** Port **5000**
- **HTTPS (Akses Web Selamat):** Port **5001**

Ini adalah port lalai untuk mengakses antara muka DSM.

![Port Rangkaian](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Langkah 4: Aktifkan Ciri QuickConnect ID

Synology QuickConnect ID ialah pengecam unik yang membolehkan anda mengakses Synology NAS anda dari jauh melalui internet tanpa perlu mengkonfigurasi tetapan rangkaian yang rumit seperti pemajuan port. QuickConnect memudahkan akses jauh dengan menggunakan pelayan Synology untuk mewujudkan sambungan antara NAS anda dan peranti anda, seperti telefon pintar atau komputer, melalui QuickConnect ID.

**Cara Mencari atau Menyediakan QuickConnect ID Anda:**

1. **Log masuk ke DSM.**
2. Pergi ke **Panel Kawalan > Akses Luaran > QuickConnect**.
3. **Aktifkan QuickConnect** dan sama ada cipta atau lihat QuickConnect ID unik anda.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Langkah 5: Sambungkan ke Synology NAS pada iPhone/Mac Anda Menggunakan Evermusic atau Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) dan [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) adalah kedua-dua aplikasi pemain muzik yang direka untuk peranti iOS dan macOS, masing-masing menawarkan ciri dan keupayaan unik untuk menguruskan dan menikmati perpustakaan muzik anda.

1. Buka aplikasi Evermusic atau Flacbox dan pergi ke tab **Sambungan**.

![Sambungan](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Pilih **Sambungkan perkhidmatan awan** dan pilih **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Anda mempunyai dua pilihan sambungan: **manual** menggunakan alamat IP dan port pelayan, atau **automatik** melalui QuickConnect ID.

### Sambungan Manual

Untuk kaedah manual, anda memerlukan alamat IP langsung dan nombor port yang anda peroleh dalam langkah sebelumnya.

1. Masukkan URL pelayan yang anda peroleh dalam langkah 2, menggunakan format berikut: PROTOCOL://IP_ADDRESS:PORT_NUMBER
   - Gunakan **port 5000** untuk HTTP dan **port 5001** untuk sambungan HTTPS.

   Contohnya:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Nombor port sebenar boleh disahkan dalam langkah 3 persediaan anda.
3. Masukkan **log masuk** dan **kata laluan** anda untuk Synology NAS.
4. Ketik **Log Masuk** untuk mewujudkan sambungan.

![Sambungan Manual](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Sambungan Automatik

Untuk sambungan automatik, anda akan menggunakan **QuickConnect ID** dari langkah 4. Daripada memasukkan alamat IP dan nombor port untuk Synology NAS anda secara manual, cukup masukkan **QuickConnect ID**. Aplikasi akan mendapatkan maklumat sambungan yang diperlukan secara automatik.

Kaedah ini membolehkan anda mengakses NAS anda dari jauh, walaupun di luar rangkaian rumah anda, supaya anda boleh menguruskan fail anda dari internet tanpa perlu mengkonfigurasi pemajuan port atau alamat IP statik.

![Sambungan Automatik](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Pengesahan Dua Faktor

Bermula dengan DSM 4.2, Synology memperkenalkan **pengesahan 2 langkah** untuk meningkatkan keselamatan. Ciri ini memerlukan kod **kata laluan sekali guna (OTP)**, yang dijana oleh aplikasi pengesah, sebagai tambahan kepada kelayakan log masuk biasa anda. Jika anda telah mengaktifkan pengesahan 2 langkah, selepas memasukkan nama pengguna dan kata laluan, anda juga perlu memasukkan OTP untuk log masuk ke sesi DSM anda.

Sila ambil perhatian, sebaik sahaja sesi anda tamat tempoh, aplikasi perlu dibenarkan semula secara manual. Untuk membenarkan semula:

1. Pergi ke tab **Sambungan** dalam aplikasi.
2. Ketik butang **Lebih banyak tindakan** di sebelah nama pelayan.
3. Pilih **Tetapan** dari menu untuk memasukkan kod pengesahan baharu dan melengkapkan proses kebenaran semula.

Ini memastikan bahawa walaupun anda mengakses NAS anda dari rangkaian yang tidak dipercayai, data anda kekal selamat.

## Langkah 6: Navigasi dan Main Muzik

1. Setelah disambungkan, peranti akan muncul dalam senarai **Peranti Bersambung**.

![Peranti Bersambung](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navigasi ke folder **Music** dan ketik mana-mana fail audio untuk memulakan main balik.

![Main Muzik](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Langkah 7: Tambah Folder Awan Bersambung ke Perpustakaan Muzik

1. Buka bahagian **Perpustakaan Muzik** dalam aplikasi.
2. Pilih **Tambah Muzik** dan pilih **Sambungan**.
3. Pilih pelayan NAS bersambung anda dan pilih folder **Music**. Ketik **Selesai**.
4. Aplikasi akan mengimbas folder muzik dan menambah fail audio yang disokong ke perpustakaan muzik. Metadata akan dimuatkan, dan trek anda akan dikumpulkan mengikut album, artis dan genre.

## Kesimpulan

Dengan mengikuti langkah-langkah ini, anda boleh dengan mudah menyediakan sambungan pada Synology NAS anda dan menstrim seluruh perpustakaan muzik anda ke iPhone atau Mac menggunakan Evermusic atau Flacbox. Sama ada anda di rumah atau dalam perjalanan, nikmati akses lancar dan berkualiti tinggi ke trek kegemaran anda dari mana-mana sahaja menggunakan QuickConnect. Manfaatkan fleksibiliti dan kemudahan yang ditawarkan oleh aplikasi ini, dan mula menguruskan koleksi muzik anda dengan mudah di semua peranti anda.

Dengan akses jauh selamat melalui QuickConnect dan sokongan untuk pelbagai format audio, anda tidak akan pernah jauh dari muzik anda. Sekarang, fail yang disimpan di NAS anda hanya satu ketikan sahaja!

## FAQ

{{% details title="Apakah perbezaan antara sambungan manual dan QuickConnect?" closed="true" %}}
Sambungan manual menggunakan alamat IP dan port NAS, yang berfungsi pada rangkaian tempatan anda. QuickConnect menggunakan perkhidmatan geganti Synology untuk mewujudkan sambungan dari mana-mana sahaja melalui internet, tanpa pemajuan port.
{{% /details %}}

{{% details title="Bolehkah saya menstrim muzik dari Synology NAS di luar rangkaian rumah saya?" closed="true" %}}
Ya. Aktifkan QuickConnect pada Synology NAS anda dan gunakan QuickConnect ID dalam Evermusic atau Flacbox untuk menstrim muzik dari mana-mana sahaja dengan sambungan internet.
{{% /details %}}

{{% details title="Format audio manakah yang disokong semasa menstrim dari Synology NAS?" closed="true" %}}
Evermusic dan Flacbox menyokong FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD dan banyak format lain. Semua format yang disokong berfungsi semasa menstrim dari Synology NAS.
{{% /details %}}

{{% details title="Adakah saya memerlukan pengesahan dua faktor untuk menyambung?" closed="true" %}}
Tidak, 2FA adalah pilihan. Walau bagaimanapun, jika anda telah mengaktifkan pengesahan 2 langkah pada Synology DSM anda, aplikasi akan meminta kata laluan sekali guna semasa log masuk. Anda perlu membenarkan semula apabila sesi tamat tempoh.
{{% /details %}}

{{% details title="Patutkah saya menggunakan API natif Synology, WebDAV, atau SMB untuk menyambung?" closed="true" %}}
API natif Synology dengan QuickConnect adalah pilihan terbaik untuk akses jauh. Untuk penggunaan rangkaian tempatan, SMB biasanya merupakan pilihan terpantas. WebDAV berfungsi dengan baik untuk akses tempatan dan jauh. Evermusic dan Flacbox menyokong ketiga-tiga protokol.
{{% /details %}}
