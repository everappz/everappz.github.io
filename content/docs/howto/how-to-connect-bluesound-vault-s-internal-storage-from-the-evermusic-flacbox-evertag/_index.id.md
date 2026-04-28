---
title: "Cara menghubungkan penyimpanan internal Bluesound VAULT dari Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Pelajari cara mengakses hard drive internal Bluesound VAULT dari Evermusic, Flacbox, dan Evertag menggunakan protokol SMB untuk mengelola, mengedit, dan memutar file audio."
keywords: ["bluesound vault", "hubungkan penyimpanan smb", "evermusic smb", "flacbox vault", "evertag smb", "penyimpanan nas musik", "drive internal vault"]
tags: ["evermusic", "hubungkan", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Ringkasan:** Hubungkan ke penyimpanan internal Bluesound VAULT Anda melalui SMB menggunakan Evermusic, Flacbox, atau Evertag. Temukan alamat IP VAULT di aplikasi BluOS, masukkan sebagai koneksi SMB dengan akses tamu, dan mulai memutar atau mengelola file musik Anda.

Bluesound VAULT memiliki hard drive internal dan berfungsi sebagai Network Attached Storage (NAS). Mengakses hard drive internal VAULT memungkinkan Anda menambah/menghapus file, mengedit tag metadata dari aplikasi kami Evermusic, Flacbox, Evertag.

**Berikut adalah langkah-langkah untuk mengakses hard drive internal VAULT Anda:**

1. Di Aplikasi BluOS, pilih **Bantuan > Diagnostik**.

2. Dari halaman **Diagnostik**, dapatkan **Alamat IP** VAULT. **Alamat IP** ini akan digunakan di langkah selanjutnya.

3. Buka Evermusic, Flacbox atau Evertag.

   ![Aplikasi Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Buka layar "Koneksi" dan pilih item menu "Hubungkan layanan cloud".

   ![Layar Koneksi Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Pilih layanan cloud "SMB".

   ![Layar Hubungkan Layanan Cloud Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Di "Layar konfigurasi SMB" masukkan URL dalam format berikut:

   ```
   SMB://<<VAULT-IP>>
   ```

   Ganti `<<VAULT-IP>>` dengan **Alamat IP** yang diperoleh di Langkah 2.

   **Catatan:** Biarkan kolom Login dan Kata Sandi kosong karena Penyimpanan VAULT mendukung mode TAMU.

   ![Layar Koneksi SMB Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Ketuk tombol "Masuk" untuk menyimpan konfigurasi.

8. Buka penyimpanan cloud yang terhubung dan navigasi ke dalam folder dengan file audio dan ketuk file apa pun untuk memulai pemutar audio.

   ![Layar Server SMB Terbuka Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Anda juga dapat mengedit file menggunakan pengelola file bawaan.

   ![Layar Pengelola File Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Dengan langkah-langkah sederhana ini, Anda dapat dengan mudah mengakses hard drive internal Bluesound VAULT dan mengontrol perpustakaan musik Anda menggunakan Evermusic, Flacbox, atau Evertag.

## FAQ

{{% details title="Apakah saya memerlukan nama pengguna dan kata sandi untuk terhubung ke Bluesound VAULT?" closed="true" %}}
Tidak. Bluesound VAULT mendukung akses tamu (anonim) melalui SMB. Biarkan kolom Login dan Kata Sandi kosong saat mengonfigurasi koneksi.
{{% /details %}}

{{% details title="Bisakah saya mengedit tag musik di Bluesound VAULT?" closed="true" %}}
Ya. Menggunakan Evertag, Anda dapat mengedit tag metadata (judul, artis, album, dll.) untuk file audio yang disimpan langsung di hard drive internal VAULT.
{{% /details %}}

{{% details title="Protokol apa yang didukung Bluesound VAULT?" closed="true" %}}
Bluesound VAULT mengekspos penyimpanan internalnya melalui SMB (Server Message Block). Evermusic, Flacbox, dan Evertag semuanya mendukung koneksi SMB, sehingga memudahkan koneksi.
{{% /details %}}

{{% details title="Bisakah saya streaming musik dari VAULT tanpa menyalin file ke iPhone saya?" closed="true" %}}
Ya. Setelah terhubung melalui SMB, Anda dapat streaming file audio langsung dari drive internal VAULT tanpa menyalinnya ke perangkat Anda.
{{% /details %}}
