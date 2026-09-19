---
title: "Akses & Privasi"
date: 2026-08-20
description: "Pastikan perkongsian Everdisk anda selamat: lindungi akses dengan log masuk dan kata laluan, sulitkan sambungan SMB dengan SMB3 (AES), kawal sama ada peranti yang bersambung boleh memuat naik, menamakan semula dan memadam dengan Penyuntingan Fail, sekat peranti yang tidak dikenali, pilih tong sampah lawan padam kekal, dan fahami sebab semuanya kekal pada rangkaian tempatan anda."
keywords: ["perlindungan kata laluan Everdisk", "penyulitan SMB", "penyulitan SMB3 AES", "togol penyuntingan fail", "sekat peranti", "peranti disekat", "padam fail secara kekal", "rangkaian tempatan sahaja", "perkongsian fail peribadi", "DLNA tiada kata laluan", "keselamatan rangkaian"]
tags: ["everdisk", "panduan", "akses", "privasi", "keselamatan"]
readingTime: 8
---


Everdisk memastikan fail anda kekal pada rangkaian anda sendiri dan memberi anda kawalan mudah ke atas siapa yang boleh mencapainya dan apa yang boleh mereka lakukan. Anda temui kawalan ini dalam **Tetapan -> Perkongsian -> Akses**, ditambah beberapa tetapan berkaitan dalam Pengurus Fail.

## Lindungi akses dengan log masuk dan kata laluan

Secara lalai, sesiapa sahaja pada rangkaian yang sama yang mempunyai alamat anda boleh membuka fail kongsian anda. Untuk mewajibkan log masuk:

1. Pergi ke **Tetapan -> Perkongsian -> Akses**.
2. Masukkan **Log Masuk** dan **Kata Laluan**.
3. Kini sambungan **Pelayar (HTTP)**, **Komputer (WebDAV)**, **Komputer (Lanjutan) (SMB)** dan **Aplikasi & Peranti Lain (FTP)** kesemuanya akan meminta butiran itu sebelum memaparkan fail anda.

Biarkan kedua-dua medan kosong untuk akses terbuka. Kata laluan anda disimpan dengan selamat dalam Keychain peranti.

> **DLNA sentiasa terbuka.** Sambungan TV & Pusat Media (DLNA) tidak boleh dilindungi kata laluan, jadi sebaik sahaja ia dihidupkan, mana-mana peranti pada Wi-Fi yang sama boleh melayari media kongsian anda. Matikan ia jika anda hanya mahukan sambungan yang dilindungi, dan hanya berkongsi pada rangkaian yang anda percayai.

## Sulitkan sambungan SMB (SMB3 / AES)

Log masuk dan kata laluan mengawal **siapa** yang boleh menyambung, tetapi data itu sendiri masih bergerak secara terbuka pada kebanyakan sambungan. **SMB ialah satu-satunya sambungan yang boleh disulitkan oleh Everdisk**, yang mengacak setiap pemindahan supaya tiada sesiapa lain pada rangkaian yang sama boleh membacanya.

Untuk menghidupkannya:

1. Tetapkan **Log Masuk** dan **Kata Laluan** seperti di atas - sambungan yang disulitkan tidak boleh tanpa nama.
2. Pergi ke **Tetapan -> Perkongsian** dan hidupkan **Wajibkan penyulitan SMB**.
3. **Berhenti dan Mula** berkongsi semula supaya perubahan itu berkuat kuasa.

Setiap pemindahan SMB kemudian dilindungi dengan **penyulitan SMB3 (AES)**. Peranti yang menyambung mesti menyokong SMB3 - Finder pada Mac moden, atau **Windows 10 dan lebih baharu**. Ini pilihan yang bagus pada Wi-Fi yang anda tidak percayai sepenuhnya. Penyulitan SMB ialah ciri Premium.

## Benarkan atau sekat penyuntingan (Penyuntingan Fail)

Togol **Penyuntingan Fail** mengawal sama ada peranti yang bersambung hanya boleh melihat fail anda, atau turut boleh mengubahnya.

- **Hidup** (lalai): peranti yang bersambung boleh **memuat naik, menamakan semula dan memadam** fail kongsian anda - jadi peranti anda berfungsi seperti pemacu rangkaian dua hala yang sebenar.
- **Mati**: fail kongsian anda adalah **baca sahaja**. Orang lain boleh melihat dan memuat turun, tetapi tidak boleh menambah atau mengubah apa-apa.

Menghidupkannya akan menunjukkan amaran ringkas kerana ia membenarkan orang lain mengubah suai fail anda. Ia membawa lencana **Penting** semasa ia dihidupkan.

## Sekat peranti

Jika anda melihat peranti yang tidak anda kenali:

1. Pada skrin Perkongsian, cari ia di bawah **Siapa yang Bersambung**.
2. Ketik butang lebih tindakannya dan pilih **Sekat peranti ini**.

Peranti yang disekat disenaraikan dalam **Tetapan -> Perkongsian -> Akses -> Peranti Disekat**, tempat anda boleh **nyahsekat** satu atau **Nyahsekat Semua**. Penyekatan akan mengikuti peranti walaupun alamat rangkaiannya berubah (untuk sambungan Pelayar, Komputer dan TV).

## Tong sampah lawan padam kekal

Apabila sesuatu fail dipadam - oleh anda dalam pengurus fail, atau oleh peranti yang bersambung - ia biasanya pergi ke **tong sampah** yang boleh dipulihkan supaya anda boleh mendapatkannya semula.

Jika anda lebih suka fail dibuang serta-merta tanpa pemulihan, hidupkan **Padam Fail Secara Kekal** dalam **Tetapan -> Pengurus Fail -> Memadam Fail**. Ini dimatikan secara lalai. **Ia mempengaruhi pengurus fail pada peranti** serta **pemadaman yang dibuat menerusi rangkaian**; ia tidak mengubah cara pustaka Foto atau pustaka Muzik sistem mengendalikan pemadaman.

## Semuanya kekal tempatan

Everdisk hanya berkongsi menerusi **rangkaian tempatan** anda - tiada apa-apa dimuat naik ke internet dan tiada akaun awan di tengah-tengah. Beberapa perkara yang patut diketahui:

- Everdisk memerlukan kebenaran **Rangkaian Tempatan** iOS supaya peranti berdekatan dapat menemuinya. Jika kebenaran itu dimatikan, satu nota akan menerangkan cara menghidupkannya semula dalam aplikasi Tetapan iOS.
- Untuk privasi maksimum, berkongsilah hanya semasa anda berada pada rangkaian **Wi-Fi rumah atau peribadi** yang anda percayai, dan berhati-hati pada Wi-Fi awam. Log masuk dan kata laluan membantu, tetapi ia bukan pengganti kepada rangkaian yang dipercayai.
- **Pilihan yang paling peribadi sekali ialah kabel USB ke Mac** - data pergi terus menerusi kabel dan tidak pernah menyentuh penghala atau internet. Lihat [Sambung Peranti Anda](/docs/guide/everdisk/everdisk-guide-connect).

## Langkah seterusnya

- [Perkongsian](/docs/guide/everdisk/everdisk-guide-sharing) - pilih apa yang hendak dikongsi dan mula berkongsi.
- [Tetapan](/docs/guide/everdisk/everdisk-guide-settings) - semua tetapan Akses dan Pengurus Fail di satu tempat.
