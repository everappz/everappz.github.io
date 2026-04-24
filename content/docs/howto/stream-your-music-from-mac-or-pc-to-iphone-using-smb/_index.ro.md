---
title: "Transmite muzica de pe Mac sau PC pe iPhone folosind SMB"
description: "Află cum să transmiți colecția ta de muzică de pe Mac sau Windows PC pe iPhone sau iPad folosind Evermusic și protocolul SMB. Un ghid simplu pas cu pas pentru conectare și ascultarea audio fără sincronizare."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["transmitere muzică de pe Mac pe iPhone", "SMB audio streaming iOS", "configurare Evermusic SMB", "conectare muzică PC iPhone", "partajare muzică Mac iOS", "SMB Windows streaming fișiere", "acces Evermusic foldere PC"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**Pe scurt:** Folosește aplicația Evermusic pentru iPhone sau iPad pentru a transmite muzică de pe Mac sau Windows PC prin rețeaua ta locală folosind SMB. Fără sincronizare, fără copiere -- doar activează partajarea fișierelor pe computer, conectează-te în aplicație și redă. Configurarea durează mai puțin de 5 minute.

Te îneci într-o mare de muzică pe MAC-ul sau PC-ul tău și vrei să te bucuri de ea fără bătăi de cap pe iPhone sau iPad? Nu căuta mai departe de Evermusic. Cu Evermusic, este incredibil de simplu să conectezi computerul folosind protocolul SMB și să transmiți melodiile tale preferate fără să-ți faci griji că ocupi spațiu suplimentar pe dispozitiv sau te confrunți cu probleme de sincronizare. Iată un ghid pas cu pas pentru a începe:

## Pasul 1: Activează protocolul SMB pe computerul tău

![Evermusic - Suport SMB - Ecran partajare Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Dacă folosești MAC

- Deschide Preferințe Sistem -> Partajare.
- Activează serviciul de Partajare Fișiere.
- În secțiunea "Foldere partajate", adaugă folderul tău de muzică, selectează un utilizator și setează nivelurile de permisiuni (Citire și Scriere sau Doar Citire).
- Pentru mai multă comoditate, poți selecta "Toți: Doar Citire" pentru folderul de muzică, făcându-l ușor accesibil în Evermusic.
- Nu uita să reții URL-ul computerului tău (smb://192.168.xx.xx) pentru pașii următori.

![Evermusic - Suport SMB - Ecran partajare fișiere](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Apasă "Opțiuni" și activează "Partajează fișiere și foldere folosind SMB."
- Activează "Partajare fișiere Windows" pentru conturile disponibile.

![Evermusic - Suport SMB - Ecran partajare fișiere și foldere](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Dacă folosești un Windows PC

![Evermusic - Suport SMB - Partajare fișiere pe Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Click dreapta pe folderul tău de muzică.
- Selectează "Proprietăți."
- Deschide tab-ul "Partajare."
- Click pe "Partajează..."
- Alege persoanele cu care să partajezi și setează nivelurile lor de permisiuni.
- Ca și la MAC, poți opta pentru "Toți: Citire" pentru folderul de muzică selectat.
- Click pe "Finalizat" pentru a salva setările.

![Evermusic - Suport SMB - Folder partajat pe Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Pasul 2: Adaugă computerul tău automat

- Acum, deschide Evermusic și mergi la tab-ul "Conexiuni" ("Rețea" dacă folosești o versiune veche a aplicației).
- Dacă vezi computerul tău în secțiunea "Dispozitive disponibile" ("Partajări disponibile" dacă folosești o versiune veche a aplicației) și ai selectat "Toți: Doar Citire" în pasul anterior, pur și simplu apasă pe computerul tău și se va conecta automat.
- Dacă acest lucru nu se întâmplă, poți adăuga computerul manual.

![Evermusic - Suport SMB - Ecran conectare cont](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Pasul 3: Adaugă computerul tău manual

- Apasă "Conectare serviciu cloud" ("Adaugă cont" dacă folosești o versiune veche a aplicației)
- Selectează "SMB" din lista serverelor disponibile pe ecranul următor.
- Pe ecranul de setări "SMB":
  - Introdu URL-ul serverului cu calea folderului partajat. Poți introduce numele serverului sau IP-ul serverului. De exemplu:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Introdu numele de utilizator și parola sau lasă aceste câmpuri goale dacă ai selectat "Toți: Doar Citire" în pasul anterior.
  - Câmpul "WORKGROUP" este opțional și ar trebui folosit dacă ai un domeniu Active Directory.

![Evermusic - Suport SMB - Ecran introducere credențiale](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

După ce ai conectat contul SMB, acesta va apărea în secțiunea "Servicii cloud" ("Conturi"). Deschide contul conectat apăsând pe el, navighează la folderul de muzică și apasă pe orice fișier audio pentru a porni playerul.

![Evermusic - Suport SMB - Ecran deschidere folder conectat](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Bucură-te de colecția ta de muzică fără probleme pe iPhone sau iPad cu Evermusic.

![Evermusic - Suport SMB - Ecran player audio](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Pasul 4: Soluție alternativă SMB2

Dacă întâmpini probleme la navigarea folderelor sau redarea fișierelor care conțin caractere speciale (precum ü, ö, é), acest lucru poate fi legat de protocolul SMB2. Lucrăm activ la rezolvarea acestei probleme.

Ca soluție temporară, te rugăm să încerci să activezi SMB 1 pe serverul tău și în setările aplicației. Alternativ, te poți conecta la serverul SMB folosind meniul de deschidere fișiere al sistemului. Iată cum:

1. Navighează la "Fișiere locale."
2. Derulează în jos la secțiunea "Fișiere pe acest dispozitiv" și apasă "Deschide fișiere..." sau "Deschide foldere..."
3. Localizează serverul tău și selectează fișierele sau folderele de care ai nevoie.
4. Apasă "Deschide" pentru a confirma selecția.

## Pasul 5: Soluție alternativă WebDAV

În plus, poți încerca să te conectezi la NAS-ul tău folosind protocoalele WebDAV sau DLNA dacă sunt acceptate.

Urmând acești pași, poți ocoli problemele legate de caracterele speciale din numele fișierelor și continua să te bucuri de fișierele media.

P.S. Poți de asemenea să transferi fișiere audio de pe MAC/PC pe iPhone folosind Partajarea Fișierelor iTunes și să redai fișiere audio locale. Află mai multe despre această funcție în ghidul nostru: [Cum să redai fișierele iTunes pe iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Întrebări frecvente

{{% details title="Pot transmite muzică de pe PC pe iPhone fără iTunes?" closed="true" %}}
Da. Evermusic se conectează la PC-ul tău prin SMB pe rețeaua ta Wi-Fi locală. iTunes nu este necesar. Doar activează partajarea fișierelor pe PC și conectează-te în aplicație.
{{% /details %}}

{{% details title="Streaming-ul SMB folosește date mobile?" closed="true" %}}
Nu. SMB funcționează prin rețeaua ta Wi-Fi locală. Nu este necesară conexiune la internet sau date mobile.
{{% /details %}}

{{% details title="Ce formate audio suportă Evermusic prin SMB?" closed="true" %}}
Evermusic suportă MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC și alte formate audio comune. Fișierele sunt redate direct din partajarea SMB.
{{% /details %}}

{{% details title="Pot transmite muzică de pe un NAS pe iPhone?" closed="true" %}}
Da. Dacă NAS-ul tău suportă SMB (majoritatea o fac, inclusiv Synology, QNAP și WD My Cloud), te poți conecta la el folosind aceiași pași din acest ghid.
{{% /details %}}

{{% details title="Trebuie să țin computerul pornit în timpul transmiterii?" closed="true" %}}
Da. Deoarece Evermusic transmite fișierele direct de pe computer, acesta trebuie să fie pornit și conectat la aceeași rețea ca iPhone-ul tău.
{{% /details %}}

{{% details title="Există o limită de dimensiune a fișierului pentru streaming SMB?" closed="true" %}}
Nu. Evermusic transmite fișiere de orice dimensiune prin SMB. Fișierele mari lossless (FLAC, WAV) funcționează fără probleme.
{{% /details %}}
