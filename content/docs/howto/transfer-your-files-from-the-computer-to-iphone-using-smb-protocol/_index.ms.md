---
title: "Pindahkan Fail dari Komputer ke iPhone Menggunakan Protokol SMB"
description: "Ketahui cara memindahkan dan mengakses fail besar dari Mac atau PC Windows anda ke iPhone atau iPad anda menggunakan Evermusic dan protokol SMB. Panduan langkah demi langkah untuk penstriman dan pengurusan fail yang lancar."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["pindah fail ke iPhone SMB", "strim muzik PC di iPhone", "sambung Mac ke iPhone SMB", "persediaan Evermusic SMB", "akses fail komputer iPhone", "kongsi muzik Windows iOS", "pemindahan fail SMB Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Ringkasan:** Gunakan Evermusic pada iPhone atau iPad anda untuk mengakses fail yang disimpan pada Mac atau PC Windows anda melalui rangkaian tempatan melalui SMB. Tanpa kabel, tanpa iTunes, tanpa muat naik awan diperlukan. Dayakan perkongsian fail pada komputer anda, sambung dalam aplikasi, dan layari atau mainkan fail anda secara tanpa wayar.

Adakah anda mempunyai koleksi fail besar yang luas pada MAC atau PC anda dan ingin mengaksesnya dengan mudah dari iPhone atau iPad anda? Aplikasi kami menyediakan penyelesaian yang mudah.

Ikuti langkah-langkah ini untuk mendayakan akses lancar antara komputer dan peranti iOS anda menggunakan protokol SMB:

## Langkah 1: Dayakan Protokol SMB pada Komputer Anda

**Untuk MAC:**

1. Buka "Keutamaan Sistem" pada MAC anda.
2. Klik pada "Perkongsian".
3. Dayakan perkhidmatan "Perkongsian Fail".
4. Tambah folder muzik anda ke bahagian "Folder Dikongsi". Tambah pengguna dan pilih tahap kebenaran (Baca & Tulis atau Baca Sahaja). Anda boleh memilih "Semua Orang: Baca Sahaja" untuk folder muzik yang ditambah.

   ![Skrin Tetapan Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Ingat URL komputer (smb://192.168.xx.xx), kerana anda akan menggunakannya dalam langkah seterusnya.
6. Klik pada "Pilihan" dan aktifkan "Kongsi fail dan folder menggunakan SMB".

   ![Skrin Perkongsian Fail Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Dayakan "Perkongsian Fail Windows" untuk akaun yang tersedia.

   ![Skrin Perkongsian SMB Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Untuk Windows PC:**

1. Klik kanan pada folder muzik anda.
2. Pilih "Sifat".
3. Navigasi ke tab "Perkongsian".
4. Klik "Kongsi..."
5. Pilih individu yang ingin anda kongsi folder dan nyatakan tahap kebenaran. Anda boleh memilih "Semua Orang: Baca" untuk folder muzik yang dipilih.

   ![Skrin Perkongsian SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Klik "Selesai".
7. Klik "Selesai" dalam tetingkap "Perkongsian Fail", dan ingat laluan folder.

   ![Folder Dikongsi SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Langkah 2: Sambungkan Peranti iOS Anda

1. Buka aplikasi pada iPhone atau iPad anda.
2. Pergi ke tab "Sambungan".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Skrin Sambungan Evermusic"
  caption="Skrin Sambungan Evermusic"
  width="400"
>}}

*Jika Komputer Anda Muncul dalam Bahagian "Peranti yang tersedia":*

Jika komputer anda kelihatan dalam bahagian "Peranti yang tersedia" dan anda memilih "Semua Orang: Baca Sahaja" pada langkah sebelumnya, hanya ketik pada komputer anda dan ia akan menyambung secara automatik.

*Jika Komputer Anda Tidak Muncul Secara Automatik:*

1. Ketik "Sambung perkhidmatan awan".
2. Pilih "SMB" dalam skrin "Sambung perkhidmatan awan".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Skrin Sambung Perkhidmatan Awan Evermusic"
  caption="Skrin Sambung Perkhidmatan Awan Evermusic"
  width="400"
>}}

3. Dalam skrin "Sambungan SMB", masukkan URL pelayan dengan laluan folder dikongsi. Anda boleh menggunakan nama pelayan atau IP pelayan:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Masukkan Log Masuk dan Kata Laluan anda atau biarkan medan ini kosong jika anda memilih "Semua Orang: Baca Sahaja" pada langkah sebelumnya.
5. Medan "WORKGROUP" adalah pilihan dan perlu digunakan jika anda mempunyai Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Skrin Penyambung SMB Evermusic"
  caption="Skrin Penyambung SMB Evermusic"
  width="400"
>}}

6. Setelah anda menyambungkan komputer menggunakan protokol SMB, ia akan muncul dalam bahagian "Perkhidmatan awan" pada skrin "Sambungan".
7. Buka perkhidmatan yang disambungkan dan navigasi ke folder yang dikehendaki.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Folder SMB Dibuka di Evermusic"
  caption="Folder SMB Dibuka di Evermusic"
  width="400"
>}}

8. Anda boleh menggunakan pengurus fail terbina dalam untuk mengedit fail anda mengikut keperluan.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Pengurus Fail Evermusic"
  caption="Pengurus Fail Evermusic"
  width="400"
>}}

## Langkah 3: Penyelesaian untuk Folder SMB2 dengan Aksara Khas

Kadangkala anda mungkin menghadapi masalah dengan folder yang mengandungi aksara khas apabila menggunakan protokol SMB2. Berikut adalah beberapa langkah untuk menyelesaikan masalah ini:

1. **Dayakan SMB 1:**  
   • Sebagai penyelesaian sementara, cuba dayakan SMB 1 pada pelayan anda dan dalam tetapan aplikasi. Ini boleh membantu mengatasi masalah berkaitan aksara khas dalam nama folder.

2. **Gunakan Menu Buka Fail Sistem:**  
   • Navigasi ke "Fail tempatan".  
   • Tatal ke bawah ke bahagian "Fail pada peranti ini".  
   • Ketik "Buka fail..." atau "Buka folder...".  
   • Cari pelayan anda dan pilih fail atau folder yang anda perlukan.  
   • Ketik "Buka" untuk mengesahkan pilihan anda.

3. **Protokol Alternatif:**  
   • Jika masalah berterusan, pertimbangkan untuk menyambung ke NAS anda menggunakan protokol WebDAV atau DLNA jika NAS anda menyokong pilihan ini. Protokol ini mungkin mengendalikan aksara khas dengan lebih baik.

Dengan mengikuti langkah-langkah ini, anda boleh mengurangkan masalah aksara khas dalam nama folder apabila menggunakan protokol SMB2.

## Kesimpulan

Dengan langkah-langkah ini, anda boleh mengakses koleksi fail yang luas dari MAC atau PC anda pada iPhone atau iPad dengan mudah menggunakan aplikasi kami.

## Soalan Lazim

{{% details title="Bolehkah saya mengakses fail pada PC dari iPhone tanpa iTunes?" closed="true" %}}
Ya. Evermusic menyambung ke komputer anda melalui SMB pada rangkaian Wi-Fi tempatan anda. Tiada penyegerakan iTunes atau Finder diperlukan. Dayakan perkongsian fail pada PC anda dan sambung terus dari aplikasi.
{{% /details %}}

{{% details title="Adakah akses fail SMB berfungsi melalui internet?" closed="true" %}}
Tidak. SMB adalah protokol rangkaian tempatan. iPhone dan komputer anda mesti berada pada rangkaian Wi-Fi yang sama. Untuk akses jauh, muat naik fail ke perkhidmatan awan seperti Google Drive atau Dropbox dan sambung kepadanya di Evermusic.
{{% /details %}}

{{% details title="Apakah jenis fail yang boleh saya akses melalui SMB?" closed="true" %}}
Evermusic menyokong MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC dan format audio lain. Anda juga boleh melayari dan mengurus fail bukan audio menggunakan pengurus fail terbina dalam.
{{% /details %}}

{{% details title="Bolehkah saya memindahkan fail dari NAS ke iPhone menggunakan SMB?" closed="true" %}}
Ya. Kebanyakan peranti NAS (Synology, QNAP, WD My Cloud dan lain-lain) menyokong SMB. Sambung ke NAS anda menggunakan langkah yang sama dalam panduan ini.
{{% /details %}}

{{% details title="Adakah saya perlu menyalin fail ke iPhone untuk memainkannya?" closed="true" %}}
Tidak. Evermusic menstrim fail terus dari komputer atau NAS anda melalui rangkaian. Fail tidak disalin ke iPhone anda melainkan anda memilih untuk memuat turunnya untuk main balik luar talian.
{{% /details %}}

{{% details title="Adakah perkongsian fail SMB selamat?" closed="true" %}}
Perkongsian fail SMB hanya berfungsi pada rangkaian tempatan anda. Peranti lain pada rangkaian berbeza tidak boleh mengakses folder dikongsi anda. Untuk keselamatan tambahan, gunakan log masuk dan kata laluan daripada akses tanpa nama (Semua Orang).
{{% /details %}}
