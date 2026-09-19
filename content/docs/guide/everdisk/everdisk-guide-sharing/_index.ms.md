---
title: "Perkongsian"
date: 2026-08-20
description: "Ketahui cara perkongsian berfungsi dalam Everdisk: ketik Mula untuk mengubah iPhone atau iPad anda menjadi pemacu tanpa wayar, pilih apa yang hendak dikongsi (fail, folder, foto dan muzik), jalankan lima pelayan (DLNA, HTTP, WebDAV, SMB, FTP), sulitkan sambungan SMB dengan SMB3 (AES), baca alamat sambungan, lihat siapa yang bersambung, dan pastikan perkongsian terus berjalan menerusi Wi-Fi atau kabel USB."
keywords: ["perkongsian Everdisk", "pemacu tanpa wayar iPhone", "mula perkongsian", "kongsi fail iPhone", "kongsi foto menerusi rangkaian", "DLNA HTTP WebDAV FTP", "apa yang hendak dikongsi", "cara menyambung", "kekalkan aplikasi terbuka", "perkongsian Wi-Fi atau kabel USB"]
tags: ["everdisk", "panduan", "perkongsian"]
readingTime: 9
---


Tab **Perkongsian** ialah nadi Everdisk. Di sinilah anda mengubah iPhone atau iPad anda menjadi pemacu tanpa wayar, memilih tepat-tepat apa yang ingin anda kongsi, dan mendapatkan alamat yang digunakan peranti lain untuk menyambung. Ini ialah tab pertama yang anda lihat apabila membuka aplikasi.

## Mula dan hentikan perkongsian

Di tengah-tengah skrin Perkongsian terdapat sebuah butang bulat yang besar.

- Ketik **Mula** untuk membawa semua pelayan yang anda dayakan dalam talian sekali gus. Butang akan memaparkan **Sedang bermula...**, kemudian **Henti** sebaik sahaja perkongsian aktif.
- Ketik **Henti** untuk menyahaktifkan semuanya semula. Peranti yang bersambung akan diputuskan.

Semasa perkongsian berjalan, fail, foto dan muzik pilihan anda tersedia untuk mana-mana peranti pada rangkaian yang sama yang menyambung menggunakan salah satu daripada lima kaedah di bawah.

> Perkongsian hanya berjalan selagi aplikasi terbuka. Lihat **Kekalkan aplikasi terbuka** menjelang penghujung halaman ini untuk mengetahui sebabnya, dan cara memastikan pemindahan besar terus berjalan.

## Pilih apa yang hendak dikongsi

Sebelum anda mula, ketik tajuk **Apa yang Hendak Dikongsi** untuk membuka tiga kumpulan. Anda boleh mengongsi apa-apa gabungan daripadanya, dan anda mesti memilih sekurang-kurangnya satu perkara sebelum perkongsian boleh dimulakan.

**Fail dan Folder**

- Folder **Dokumen** milik aplikasi anda dikongsi secara lalai. Anda boleh berhenti mengongsinya jika lebih suka begitu.
- Ketik **Tambah Folder** untuk mengongsi folder dari mana-mana lokasi pada peranti anda, atau **Tambah Fail** untuk mengongsi fail secara individu.
- Setiap item yang dikongsi mempunyai butang **Maklumat** dan butang **Berhenti Kongsi**.

**Foto dan Video**

- Hidupkan **Benarkan akses kepada seluruh Pustaka Foto** untuk mengongsi seluruh pustaka foto dan video anda, atau
- Ketik **Tambah Foto** untuk memilih sendiri hanya foto dan video yang ingin anda kongsi.

**Muzik**

- Hidupkan **Benarkan akses kepada seluruh Pustaka Muzik** untuk mengongsi seluruh pustaka muzik anda, atau
- Ketik **Tambah Lagu** untuk mengongsi hanya lagu terpilih.
- Lagu yang dilindungi (DRM) atau yang disimpan hanya dalam awan tidak boleh dikongsi.

Jika anda cuba memulakan tanpa apa-apa dipilih, Everdisk akan menunjukkan nota **Tiada untuk Dikongsi**. Jika anda menukar apa yang dikongsi semasa perkongsian sedang berjalan, **Henti dan Mula semula** untuk melaksanakan perubahan itu.

## Lima pelayan

Everdisk mengongsi kandungan yang sama dalam lima cara serentak. Setiap satunya direka untuk jenis peranti yang berbeza, dan setiap satunya boleh dihidupkan atau dimatikan dalam **Tetapan -> Perkongsian -> Sambungan**. Secara lalai, kelima-limanya dihidupkan.

- **TV & Pusat Media (DLNA)** - untuk TV pintar dan pemain media. Ia menemui peranti anda dengan sendiri dan memaparkan foto, video dan muzik anda, lengkap dengan lakaran kenit pratonton.
- **Pelayar (HTTP)** - untuk mana-mana telefon, tablet atau komputer. Orang di sebelah sana cuma membuka pautan dalam pelayar web untuk melayari dan memuat turun fail anda. Tiada apa-apa perlu dipasang.
- **Komputer (WebDAV)** - untuk Mac, PC Windows atau mesin Linux. Peranti anda muncul sebagai pemacu rangkaian biasa supaya anda boleh menyeret fail dalam kedua-dua arah.
- **Komputer (Lanjutan) (SMB)** - pemacu rangkaian untuk Mac, Windows dan Linux. Pada Mac ia muncul dengan sendirinya dalam bar sisi Finder; pada Windows, bukanya dalam File Explorer dengan alamat `smb://`. Ia satu-satunya sambungan yang boleh anda **sulitkan**, dengan penyulitan SMB3 (AES).
- **Aplikasi & Peranti Lain (FTP)** - untuk aplikasi fail dan pengguna lanjutan yang menggunakan FTP.

Untuk arahan sambungan langkah demi langkah bagi setiap jenis, lihat [Sambung Peranti Anda](/docs/guide/everdisk/everdisk-guide-connect).

## Cara Menyambung dan alamat sambungan

Selepas anda ketik Mula, bahagian **Cara Menyambung** akan menunjukkan kad bagi setiap pelayan aktif berserta **alamat** tepat untuk ditaip pada peranti di sebelah sana. Setiap alamat mudah disalin - ketik untuk menyalin, guna butang **Kongsi** untuk menghantarnya, atau ketik butang **maklumat (ⓘ)** untuk arahan terperinci bagi setiap protokol.

- Kad DLNA memaparkan alamat penerangan peranti yang berakhir dengan `/device-desc.xml` untuk pemain yang memintanya.
- Apabila peranti anda dipasang ke Mac dengan kabel, satu alamat tambahan akan muncul dengan lencana **Sambungan Kabel** yang menggunakan nama `.local` peranti anda.

Anda juga boleh membuka alamat itu sebagai **kod QR** supaya kamera peranti lain boleh terus melompat kepadanya.

## Siapa yang bersambung

Bahagian **Siapa yang Bersambung** menyenaraikan peranti yang sedang bersambung dengan anda secara masa nyata. Ketik butang lebih tindakan di sebelah mana-mana peranti untuk **Sekat peranti ini** jika anda tidak mengenalinya. Peranti yang disekat diuruskan dalam [Akses & Privasi](/docs/guide/everdisk/everdisk-guide-access).

## Nama dan avatar peranti anda

Setiap peranti mempunyai nama mesra (seperti "Speedy-Hare") dan avatar berwarna. Inilah nama yang dipaparkan oleh TV, komputer atau aplikasi lain bagi peranti anda pada rangkaian, jadi ia mudah dikenal pasti. Anda boleh menjana semula nama dan avatar secara percuma, atau menetapkan nama tersuai, ikon atau avatar foto dengan Premium. Lihat [Tetapan](/docs/guide/everdisk/everdisk-guide-settings).

## Perkongsian menerusi Wi-Fi atau kabel USB

Perkongsian boleh berjalan dalam dua situasi:

- **Menerusi Wi-Fi** - peranti anda dan peranti lain berada pada rangkaian Wi-Fi yang sama.
- **Menerusi kabel USB** - peranti anda dipasang ke **Mac** dengan kabel, walaupun tiada langsung Wi-Fi. Cara ini lebih pantas daripada Wi-Fi dan terus berfungsi di dalam pesawat, di hotel, atau pada rangkaian yang dikunci.

Jika Wi-Fi mahupun kabel tiada, butang **Mula** akan dinyahdayakan dan nota **Tiada Sambungan Wi-Fi** akan muncul. Jika sambungan terputus semasa perkongsian, Everdisk akan menghentikan perkongsian secara automatik dan memberitahu anda. Ketik butang maklumat pada mana-mana nota ini untuk penerangan penuh.

## Kekalkan aplikasi terbuka

Oleh sebab iPhone atau iPad anda bertindak sebagai pelayan, **perkongsian hanya berfungsi selagi Everdisk terbuka pada skrin**. Jika anda menutup aplikasi atau mengunci peranti untuk tempoh yang lama, sistem boleh menjeda aplikasi dan perkongsian akan berhenti.

Untuk pemindahan besar:

- Pastikan Everdisk terbuka dan berada di latar depan.
- Pasang peranti anda ke sumber kuasa.
- Tetapkan **Kunci Auto** kepada **Tidak Sekali** dalam aplikasi Tetapan iOS semasa anda memindahkan fail.

Anda boleh menghidupkan **Beritahu sebelum memutuskan sambungan** (dalam Tetapan -> Perkongsian) supaya Everdisk mengingatkan anda untuk membuka semula aplikasi sebelum sistem menggantungkannya. Ketik butang maklumat pada sepanduk **Kekalkan aplikasi terbuka** untuk butiran lanjut.

## Langkah seterusnya

- [Sambung Peranti Anda](/docs/guide/everdisk/everdisk-guide-connect) - sambungkan TV, komputer, pelayar, telefon, atau kabel USB.
- [Akses & Privasi](/docs/guide/everdisk/everdisk-guide-access) - tambah kata laluan dan kawal penyuntingan.
- [Tetapan](/docs/guide/everdisk/everdisk-guide-settings) - hidupkan atau matikan pelayan dan laraskan kualiti.
