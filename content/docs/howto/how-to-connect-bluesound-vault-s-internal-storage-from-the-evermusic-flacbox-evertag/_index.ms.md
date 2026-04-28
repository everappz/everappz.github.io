---
title: "Cara menyambung storan dalaman Bluesound VAULT dari Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Ketahui cara mengakses cakera keras dalaman Bluesound VAULT dari Evermusic, Flacbox, dan Evertag menggunakan protokol SMB untuk mengurus, mengedit, dan memainkan fail audio."
keywords: ["bluesound vault", "sambung storan smb", "evermusic smb", "flacbox vault", "evertag smb", "storan nas muzik", "pemacu dalaman vault"]
tags: ["evermusic", "sambung", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Ringkasan:** Sambung ke storan dalaman Bluesound VAULT anda melalui SMB menggunakan Evermusic, Flacbox, atau Evertag. Cari alamat IP VAULT dalam aplikasi BluOS, masukkannya sebagai sambungan SMB dengan akses tetamu, dan mula memainkan atau mengurus fail muzik anda.

Bluesound VAULT mempunyai cakera keras dalaman dan berfungsi sebagai Storan Bersambung Rangkaian (NAS). Mengakses cakera keras dalaman VAULT membolehkan anda menambah/memadam fail, mengedit tag metadata daripada aplikasi kami Evermusic, Flacbox, Evertag.

**Berikut adalah langkah-langkah untuk mengakses cakera keras dalaman VAULT anda:**

1. Dalam Aplikasi BluOS, pilih **Bantuan > Diagnostik**.

2. Dari halaman **Diagnostik**, dapatkan **Alamat IP** VAULT. **Alamat IP** ini akan digunakan dalam langkah seterusnya.

3. Buka Evermusic, Flacbox atau Evertag.

   ![Aplikasi Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Buka skrin "Sambungan" dan pilih item menu "Sambungkan perkhidmatan awan".

   ![Skrin Sambungan Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Pilih perkhidmatan awan "SMB".

   ![Skrin Sambungkan Perkhidmatan Awan Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Pada "Skrin konfigurasi SMB" masukkan URL dalam format berikut:

   ```
   SMB://<<VAULT-IP>>
   ```

   Gantikan `<<VAULT-IP>>` dengan **Alamat IP** yang diperoleh dalam Langkah 2.

   **Nota:** Biarkan medan Log Masuk dan Kata Laluan kosong kerana Storan VAULT menyokong mod TETAMU.

   ![Skrin sambungan SMB Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Ketik butang "Log masuk" untuk menyimpan konfigurasi.

8. Buka storan awan yang disambungkan dan navigasi ke dalam folder dengan fail audio dan ketik mana-mana fail untuk memulakan pemain audio.

   ![Skrin Pelayan SMB Terbuka Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Anda juga boleh mengedit fail menggunakan pengurus fail terbina dalam.

   ![Skrin Pengurus Fail Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Dengan langkah-langkah mudah ini, anda boleh mengakses cakera keras dalaman Bluesound VAULT dengan mudah dan mengawal perpustakaan muzik anda menggunakan Evermusic, Flacbox, atau Evertag.

## Soalan Lazim

{{% details title="Adakah saya memerlukan nama pengguna dan kata laluan untuk menyambung ke Bluesound VAULT?" closed="true" %}}
Tidak. Bluesound VAULT menyokong akses tetamu (tanpa nama) melalui SMB. Biarkan medan Log Masuk dan Kata Laluan kosong semasa mengkonfigurasi sambungan.
{{% /details %}}

{{% details title="Bolehkah saya mengedit tag muzik pada Bluesound VAULT?" closed="true" %}}
Ya. Menggunakan Evertag, anda boleh mengedit tag metadata (tajuk, artis, album, dll.) untuk fail audio yang disimpan terus pada cakera keras dalaman VAULT.
{{% /details %}}

{{% details title="Protokol apa yang disokong oleh Bluesound VAULT?" closed="true" %}}
Bluesound VAULT mendedahkan storan dalamannya melalui SMB (Server Message Block). Evermusic, Flacbox, dan Evertag semuanya menyokong sambungan SMB, menjadikan penyambungan mudah.
{{% /details %}}

{{% details title="Bolehkah saya menstrim muzik dari VAULT tanpa menyalin fail ke iPhone saya?" closed="true" %}}
Ya. Setelah disambungkan melalui SMB, anda boleh menstrim fail audio terus dari pemacu dalaman VAULT tanpa menyalinnya ke peranti anda.
{{% /details %}}
