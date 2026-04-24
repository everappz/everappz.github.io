---
title: "Transfer File dari Komputer ke iPhone Menggunakan Protokol SMB"
description: "Pelajari cara mentransfer dan mengakses file besar dari Mac atau PC Windows ke iPhone atau iPad menggunakan Evermusic dan protokol SMB. Panduan langkah demi langkah untuk streaming dan manajemen file yang lancar."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["transfer file ke iPhone SMB", "streaming musik PC di iPhone", "menghubungkan Mac ke iPhone SMB", "pengaturan Evermusic SMB", "akses file komputer iPhone", "berbagi musik Windows iOS", "transfer file SMB Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Ringkasan:** Gunakan Evermusic di iPhone atau iPad Anda untuk mengakses file yang tersimpan di Mac atau PC Windows melalui jaringan lokal via SMB. Tanpa kabel, tanpa iTunes, tanpa perlu upload ke cloud. Aktifkan berbagi file di komputer Anda, hubungkan di aplikasi, dan jelajahi atau putar file Anda secara nirkabel.

Apakah Anda memiliki koleksi file besar yang luas di MAC atau PC dan ingin mengaksesnya dengan mudah dari iPhone atau iPad? Aplikasi kami menyediakan solusi sederhana.

Ikuti langkah-langkah ini untuk mengaktifkan akses yang lancar antara komputer dan perangkat iOS Anda menggunakan protokol SMB:

## Langkah 1: Aktifkan Protokol SMB di Komputer Anda

**Untuk MAC:**

1. Buka "Preferensi Sistem" di MAC Anda.
2. Klik "Berbagi".
3. Aktifkan layanan "Berbagi File".
4. Tambahkan folder musik Anda ke bagian "Folder Bersama". Tambahkan pengguna dan pilih tingkat izin (Baca & Tulis atau Hanya Baca). Anda dapat memilih "Semua Orang: Hanya Baca" untuk folder musik yang ditambahkan.

   ![Layar Pengaturan Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Ingat URL komputer (smb://192.168.xx.xx), karena Anda akan menggunakannya di langkah selanjutnya.
6. Klik "Opsi" dan aktifkan "Bagikan file dan folder menggunakan SMB".

   ![Layar Berbagi File Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Aktifkan "Berbagi File Windows" untuk akun yang tersedia.

   ![Layar Berbagi SMB Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Untuk Windows PC:**

1. Klik kanan pada folder musik Anda.
2. Pilih "Properti".
3. Navigasi ke tab "Berbagi".
4. Klik "Bagikan..."
5. Pilih individu yang ingin Anda ajak berbagi folder dan tentukan tingkat izin. Anda dapat memilih "Semua Orang: Baca" untuk folder musik yang dipilih.

   ![Layar Berbagi SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Klik "Selesai".
7. Klik "Selesai" di jendela "Berbagi File", dan ingat jalur folder.

   ![Folder Bersama SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Langkah 2: Hubungkan Perangkat iOS Anda

1. Buka aplikasi di iPhone atau iPad Anda.
2. Buka tab "Koneksi".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Layar Koneksi Evermusic"
  caption="Layar Koneksi Evermusic"
  width="400"
>}}

*Jika Komputer Anda Muncul di Bagian "Perangkat yang Tersedia":*

Jika komputer Anda terlihat di bagian "Perangkat yang Tersedia" dan Anda memilih "Semua Orang: Hanya Baca" di langkah sebelumnya, cukup ketuk komputer Anda dan akan terhubung secara otomatis.

*Jika Komputer Anda Tidak Muncul Secara Otomatis:*

1. Ketuk "Hubungkan layanan cloud".
2. Pilih "SMB" di layar "Hubungkan layanan cloud".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Layar Hubungkan Layanan Cloud Evermusic"
  caption="Layar Hubungkan Layanan Cloud Evermusic"
  width="400"
>}}

3. Di layar "Koneksi SMB", masukkan URL server dengan jalur folder bersama. Anda dapat menggunakan nama server atau IP server:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Masukkan Login dan Password Anda atau biarkan kolom ini kosong jika Anda memilih "Semua Orang: Hanya Baca" di langkah sebelumnya.
5. Kolom "WORKGROUP" bersifat opsional dan harus digunakan jika Anda memiliki Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Layar Konektor SMB Evermusic"
  caption="Layar Konektor SMB Evermusic"
  width="400"
>}}

6. Setelah Anda menghubungkan komputer menggunakan protokol SMB, komputer akan muncul di bagian "Layanan cloud" pada layar "Koneksi".
7. Buka layanan yang terhubung dan navigasi ke folder yang diinginkan.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Folder SMB yang Dibuka di Evermusic"
  caption="Folder SMB yang Dibuka di Evermusic"
  width="400"
>}}

8. Anda dapat menggunakan manajer file bawaan untuk mengedit file sesuai kebutuhan.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Manajer File Evermusic"
  caption="Manajer File Evermusic"
  width="400"
>}}

## Langkah 3: Solusi untuk Folder SMB2 dengan Karakter Khusus

Terkadang Anda mungkin mengalami masalah dengan folder yang mengandung karakter khusus saat menggunakan protokol SMB2. Berikut beberapa langkah untuk mengatasi masalah ini:

1. **Aktifkan SMB 1:**  
   • Sebagai solusi sementara, coba aktifkan SMB 1 di server Anda dan di pengaturan aplikasi. Ini dapat membantu melewati masalah terkait karakter khusus dalam nama folder.

2. **Gunakan Menu Buka File Sistem:**  
   • Navigasi ke "File lokal".  
   • Gulir ke bawah ke bagian "File di perangkat ini".  
   • Ketuk "Buka file..." atau "Buka folder...".  
   • Temukan server Anda dan pilih file atau folder yang Anda butuhkan.  
   • Ketuk "Buka" untuk mengonfirmasi pilihan Anda.

3. **Protokol Alternatif:**  
   • Jika masalah berlanjut, pertimbangkan untuk menghubungkan ke NAS Anda menggunakan protokol WebDAV atau DLNA jika NAS Anda mendukung opsi ini. Protokol ini mungkin menangani karakter khusus dengan lebih baik.

Dengan mengikuti langkah-langkah ini, Anda dapat mengatasi masalah karakter khusus dalam nama folder saat menggunakan protokol SMB2.

## Kesimpulan

Dengan langkah-langkah ini, Anda dapat dengan mudah mengakses koleksi file yang luas dari MAC atau PC di iPhone atau iPad menggunakan aplikasi kami.

## Pertanyaan yang Sering Diajukan

{{% details title="Bisakah saya mengakses file di PC dari iPhone tanpa iTunes?" closed="true" %}}
Ya. Evermusic terhubung ke komputer Anda melalui SMB di jaringan Wi-Fi lokal. Tidak perlu sinkronisasi iTunes atau Finder. Aktifkan berbagi file di PC Anda dan hubungkan langsung dari aplikasi.
{{% /details %}}

{{% details title="Apakah akses file SMB berfungsi melalui internet?" closed="true" %}}
Tidak. SMB adalah protokol jaringan lokal. iPhone dan komputer Anda harus berada di jaringan Wi-Fi yang sama. Untuk akses jarak jauh, unggah file ke layanan cloud seperti Google Drive atau Dropbox dan hubungkan ke sana di Evermusic.
{{% /details %}}

{{% details title="Jenis file apa yang bisa saya akses melalui SMB?" closed="true" %}}
Evermusic mendukung MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC, dan format audio lainnya. Anda juga dapat menjelajahi dan mengelola file non-audio menggunakan manajer file bawaan.
{{% /details %}}

{{% details title="Bisakah saya mentransfer file dari NAS ke iPhone menggunakan SMB?" closed="true" %}}
Ya. Sebagian besar perangkat NAS (Synology, QNAP, WD My Cloud, dan lainnya) mendukung SMB. Hubungkan ke NAS Anda menggunakan langkah yang sama dalam panduan ini.
{{% /details %}}

{{% details title="Apakah saya perlu menyalin file ke iPhone untuk memutarnya?" closed="true" %}}
Tidak. Evermusic melakukan streaming file langsung dari komputer atau NAS Anda melalui jaringan. File tidak disalin ke iPhone kecuali Anda memilih untuk mengunduhnya untuk pemutaran offline.
{{% /details %}}

{{% details title="Apakah berbagi file SMB aman?" closed="true" %}}
Berbagi file SMB hanya berfungsi di jaringan lokal Anda. Perangkat lain di jaringan yang berbeda tidak dapat mengakses folder bersama Anda. Untuk keamanan tambahan, gunakan login dan password daripada akses anonim (Semua Orang).
{{% /details %}}
