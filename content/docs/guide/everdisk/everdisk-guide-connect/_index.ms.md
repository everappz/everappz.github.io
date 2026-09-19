---
title: "Sambung Peranti Anda"
date: 2026-08-20
description: "Arahan langkah demi langkah untuk menyambung ke pemacu tanpa wayar Everdisk anda: tonton pada TV pintar menerusi DLNA, buka fail anda dalam mana-mana pelayar web, lekapkan peranti anda sebagai pemacu rangkaian dalam Finder, Windows atau Linux menerusi WebDAV atau SMB (dengan penyulitan SMB3/AES pilihan), sambung aplikasi fail menerusi FTP, dan pindahkan menerusi kabel USB ke Mac tanpa Wi-Fi."
keywords: ["sambung ke Everdisk", "strim ke TV DLNA", "buka fail dalam pelayar", "lekap pemacu rangkaian Finder", "WebDAV Windows Linux", "aplikasi fail FTP", "pemindahan kabel USB Mac", "sambung iPhone ke komputer", "pemacu rangkaian iPhone"]
tags: ["everdisk", "panduan", "sambung"]
readingTime: 11
---


Sebaik sahaja anda ketik **Mula** pada skrin [Perkongsian](/docs/guide/everdisk/everdisk-guide-sharing), peranti lain boleh menyambung ke fail anda dalam lima cara yang berbeza. Pilih kaedah yang sepadan dengan peranti yang ingin anda gunakan. Dalam setiap keadaan, **alamat** tepat yang anda perlukan dipaparkan dalam bahagian **Cara Menyambung** pada skrin Perkongsian.

> Kedua-dua peranti mesti berada pada **rangkaian Wi-Fi yang sama** - atau, untuk Mac, disambung dengan **kabel USB** (lihat bahagian terakhir).

## Tonton pada TV (DLNA)

Gunakan cara ini untuk memaparkan foto, video dan muzik pada TV pintar atau pemain media.

1. Dalam **Tetapan -> Perkongsian -> Sambungan**, pastikan **TV & Pusat Media** dihidupkan (ia dihidupkan secara lalai).
2. Pada skrin Perkongsian, ketik **Mula**.
3. Pada TV anda, buka pemain media terbina dalamnya atau aplikasi pelayan media (ia mungkin dipanggil Media Player, SmartShare, AllShare, atau yang seumpamanya).
4. Peranti anda akan muncul dalam senarai pelayan media mengikut namanya (contohnya "Speedy-Hare"). Pilih ia.
5. Layari foto, video dan muzik kongsian anda lalu mula memainkannya. Lakaran kenit pratonton akan muncul secara automatik.

Nota:

- DLNA tidak boleh dilindungi kata laluan, jadi sambungan ini terbuka kepada sesiapa sahaja pada Wi-Fi yang sama selagi ia dihidupkan.
- Jika sesuatu video enggan dimainkan pada TV lama, turunkan kualiti video dalam **Tetapan -> Perkongsian -> Video** supaya Everdisk menukarnya kepada format yang lebih serasi.

## Buka dalam pelayar web (HTTP)

Gunakan cara ini untuk menyerahkan fail kepada sesiapa sahaja yang mempunyai pelayar web - tiada aplikasi perlu dipasang.

1. Dalam **Tetapan -> Perkongsian -> Sambungan**, pastikan **Pelayar** dihidupkan.
2. Ketik **Mula**.
3. Pada skrin Perkongsian, salin alamat **Pelayar** (atau tunjukkan kod QRnya).
4. Pada telefon, tablet atau komputer lain, buka mana-mana pelayar web (Safari, Chrome, Edge, Firefox) dan taip alamat itu.
5. Halaman akan terbuka bersama fail kongsian anda.

Dalam pelayar, orang di sebelah sana boleh:

- Bertukar antara paparan **senarai** dan **grid** serta menyusun mengikut nama, tarikh atau saiz.
- Melihat **lakaran kenit** sebenar untuk foto, video, PDF dan seni muzik.
- Membuka foto kepada **galeri** skrin penuh dengan leret, cubit untuk zum dan tayangan slaid.
- Memainkan muzik dalam **pemain** terbina dalam dengan baris gilir, kocok dan ulang.
- **Memuat turun** mana-mana fail, atau memuat turun seluruh folder (atau beberapa item terpilih) sebagai satu **Archive.zip**.
- **Memuat naik** fail kembali ke peranti anda - hanya jika anda menghidupkan **Penyuntingan Fail** (lihat [Akses & Privasi](/docs/guide/everdisk/everdisk-guide-access)).

## Gunakan sebagai pemacu rangkaian (WebDAV)

Gunakan cara ini untuk menjadikan peranti anda muncul sebagai cakera biasa pada Mac, PC Windows atau mesin Linux, supaya anda boleh menyeret fail dalam dua arah.

**Pada Mac (Finder)**

1. Dalam **Tetapan -> Perkongsian -> Sambungan**, pastikan **Komputer** dihidupkan.
2. Ketik **Mula** dan catatkan alamat **Komputer (WebDAV)**.
3. Dalam Finder, pilih **Go -> Connect to Server** (atau tekan **⌘K**).
4. Taip alamat WebDAV tepat seperti yang dipaparkan dan klik **Connect**.
5. Masukkan log masuk dan kata laluan jika anda menetapkannya, jika tidak sambung sebagai tetamu.
6. Peranti anda akan terbuka seperti mana-mana pemacu rangkaian lain. Seret fail masuk atau keluar.

**Pada Windows**

1. Buka **File Explorer**, klik kanan **This PC**, dan pilih **Add a network location** (atau petakan pemacu rangkaian).
2. Masukkan alamat WebDAV yang dipaparkan dalam Everdisk.
3. Masukkan log masuk dan kata laluan jika anda menetapkannya.

**Pada Linux**

1. Buka pengurus fail anda dan pilih **Connect to Server** (atau guna `davs://` / `dav://`).
2. Masukkan alamat WebDAV yang dipaparkan dalam Everdisk.

Sama ada sambungan itu baca sahaja atau dua hala bergantung pada tetapan **Penyuntingan Fail**. Apabila ia dihidupkan, anda boleh menyalin fail ke peranti anda serta menamakan semula atau memadamnya; apabila ia dimatikan, pemacu itu adalah baca sahaja.

## Sambung menerusi SMB (pemacu rangkaian tersulit)

SMB ialah pemacu rangkaian untuk Mac, Windows dan Linux, dibina atas perkongsian fail yang sedia ada dalam sistem tersebut, jadi peranti anda muncul sebagai pemacu rangkaian biasa - dan ia satu-satunya sambungan yang boleh anda sulitkan.

1. Dalam **Tetapan -> Perkongsian -> Sambungan**, pastikan **Komputer (Lanjutan)** (sambungan SMB) dihidupkan.
2. Ketik **Mula** dan catatkan alamat **SMB**, yang kelihatan seperti `smb://192.168.1.20:4455/Share`.
3. Sambung dari komputer anda:
   - **Mac:** peranti anda muncul dengan sendirinya dalam **bar sisi Finder** di bawah **Locations** (Network) - klik sahaja padanya dan log masuk. Untuk menyambung secara manual, pilih **Go -> Connect to Server** (**⌘K**) dan masukkan alamat itu.
   - **Windows:** buka **File Explorer**, klik kanan **This PC** dan pilih **Map network drive**, kemudian masukkan `\\<address>\Share` menggunakan hos dan nama kongsi daripada skrin Perkongsian (atau taip alamat `smb://` dalam bar alamat).
   - **Linux:** dalam pengurus fail anda pilih **Connect to Server** dan masukkan alamat itu.
4. Masukkan log masuk dan kata laluan jika anda menetapkannya, jika tidak sambung sebagai tetamu.
5. Kongsi itu dinamakan **Share**. Dengan **Penyuntingan Fail** dihidupkan anda boleh menyalin fail ke dua-dua arah; dengan ia dimatikan ia baca sahaja.

**Hidupkan penyulitan (disyorkan pada Wi-Fi yang tidak dipercayai)**

SMB ialah satu-satunya sambungan Everdisk yang boleh disulitkan. Untuk melindungi setiap pemindahan dengan **penyulitan SMB3 (AES)**:

1. Dalam **Tetapan -> Perkongsian -> Akses**, tetapkan **Log Masuk** dan **Kata Laluan** - sambungan yang disulitkan tidak boleh tanpa nama.
2. Dalam **Tetapan -> Perkongsian**, hidupkan **Wajibkan penyulitan SMB**.
3. **Berhenti dan Mula** berkongsi semula supaya perubahan itu berkuat kuasa.

Klien anda mesti menyokong SMB3 - Finder pada Mac moden, atau **Windows 10 dan lebih baharu**. Penyulitan SMB ialah ciri Premium.

## Sambung aplikasi fail (FTP)

Gunakan cara ini untuk aplikasi pengurus fail dan pemindahan yang menggunakan FTP (contohnya FileZilla atau Cyberduck pada komputer).

1. Dalam **Tetapan -> Perkongsian -> Sambungan**, pastikan **Aplikasi & Peranti Lain** dihidupkan.
2. Ketik **Mula** dan catatkan alamat **FTP**.
3. Dalam aplikasi FTP anda, tambah sambungan baharu menggunakan alamat itu.
4. Masukkan log masuk dan kata laluan jika anda menetapkannya, atau biarkan kosong untuk akses tanpa nama.

## Pindahkan menerusi kabel USB (Mac, tiada Wi-Fi diperlukan)

Gunakan cara ini apabila tiada Wi-Fi, atau apabila anda mahukan pemindahan yang paling pantas dan paling peribadi. Ia hanya berfungsi dengan **Mac** sahaja.

1. Pasang iPhone atau iPad anda ke Mac dengan kabel pengecas biasa.
2. Jika ditanya pada peranti, ketik **Trust This Computer**.
3. Dalam Everdisk, ketik **Mula**. Nota **Sambungan Pantas Tersedia** akan muncul dan skrin Perkongsian akan memaparkan satu alamat tambahan dengan lencana **Sambungan Kabel** yang berakhir dengan `.local`.
4. Pada Mac, buka Finder -> **Go -> Connect to Server** (**⌘K**) dan masukkan alamat `.local` itu (ia berfungsi untuk kedua-dua sambungan Pelayar dan Komputer).
5. Peranti anda akan terbuka menerusi kabel - lebih pantas daripada Wi-Fi, dan data tidak pernah menyentuh penghala atau internet.

Nota:

- Guna **nama `.local`**, bukan alamat IP (alamat IP hanya berfungsi menerusi Wi-Fi), dan jangan sekali-kali `localhost`.
- Laluan kabel adalah **Mac sahaja**. PC Windows dan peranti Android mesti menggunakan Wi-Fi.
- Anda juga boleh menyeret fail ke dalam folder Everdisk menggunakan Finder pada Mac, atau aplikasi Apple Devices (atau iTunes) pada Windows, menerusi perkongsian fail iOS standard.

## Langkah seterusnya

- [Akses & Privasi](/docs/guide/everdisk/everdisk-guide-access) - tambah kata laluan, benarkan muat naik, sekat peranti.
- [Foto, Muzik & Video](/docs/guide/everdisk/everdisk-guide-media) - kongsi seluruh pustaka anda dan tetapkan kualiti.
- [Sambung ke Pelayan](/docs/guide/everdisk/everdisk-guide-devices) - capai peranti lain daripada Everdisk.
