---
title: "Transferați fișiere de pe computer pe iPhone folosind protocolul SMB"
description: "Aflați cum să transferați și să accesați fișiere mari de pe Mac sau PC Windows pe iPhone sau iPad folosind Evermusic și protocolul SMB. Un ghid pas cu pas pentru streaming și gestionare de fișiere fără probleme."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["transfer fișiere pe iPhone SMB", "streaming muzică PC pe iPhone", "conectare Mac la iPhone SMB", "configurare Evermusic SMB", "acces fișiere computer iPhone", "partajare muzică Windows iOS", "transfer fișiere SMB Evermusic"]
---

{{< author-byline >}}


**Rezumat:** Folosiți Evermusic pe iPhone sau iPad pentru a accesa fișierele stocate pe Mac sau PC Windows prin rețeaua locală via SMB. Fără cabluri, fără iTunes, fără încărcare în cloud necesară. Activați partajarea fișierelor pe computer, conectați-vă în aplicație și navigați sau redați fișierele fără fir.

Aveți o colecție extinsă de fișiere mari pe MAC sau PC și doriți să le accesați cu ușurință de pe iPhone sau iPad? Aplicațiile noastre oferă o soluție simplă.

Urmați acești pași pentru a activa accesul fluid între computer și dispozitivul iOS folosind protocolul SMB:

## Pasul 1: Activați protocolul SMB pe computer

**Pentru MAC:**

1. Deschideți "Preferințe Sistem" pe MAC.
2. Faceți clic pe "Partajare".
3. Activați serviciul "Partajare Fișiere".
4. Adăugați folderul de muzică în secțiunea "Foldere Partajate". Adăugați un utilizator și alegeți nivelul de permisiune (Citire și Scriere sau Doar Citire). Puteți opta pentru "Toată lumea: Doar Citire" pentru folderul de muzică adăugat.

   ![Ecran setări Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Rețineți URL-ul computerului (smb://192.168.xx.xx), deoarece îl veți folosi în pașii următori.
6. Faceți clic pe "Opțiuni" și activați "Partajați fișiere și foldere folosind SMB".

   ![Ecran partajare fișiere Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Activați "Partajare Fișiere Windows" pentru conturile disponibile.

   ![Ecran partajare SMB Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Pentru Windows PC:**

1. Faceți clic dreapta pe folderul de muzică.
2. Selectați "Proprietăți".
3. Navigați la fila "Partajare".
4. Faceți clic pe "Partajați..."
5. Alegeți persoanele cu care doriți să partajați folderul și specificați nivelul de permisiune. Puteți selecta "Toată lumea: Citire" pentru folderul de muzică ales.

   ![Ecran partajare SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Faceți clic pe "Finalizat".
7. Faceți clic pe "Finalizat" în fereastra "Partajare Fișiere" și rețineți calea folderului.

   ![Folder partajat SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Pasul 2: Conectați dispozitivul iOS

1. Deschideți aplicația pe iPhone sau iPad.
2. Mergeți la fila "Conexiuni".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Ecran Conexiuni Evermusic"
  caption="Ecran Conexiuni Evermusic"
  width="400"
>}}

*Dacă computerul apare în secțiunea "Dispozitive disponibile":*

Dacă computerul este vizibil în secțiunea "Dispozitive disponibile" și ați selectat "Toată lumea: Doar Citire" în pasul anterior, atingeți pur și simplu computerul și se va conecta automat.

*Dacă computerul nu apare automat:*

1. Atingeți "Conectare serviciu cloud".
2. Selectați "SMB" în ecranul "Conectare serviciu cloud".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Ecran Conectare serviciu cloud Evermusic"
  caption="Ecran Conectare serviciu cloud Evermusic"
  width="400"
>}}

3. În ecranul "Conectare SMB", introduceți URL-ul serverului cu calea folderului partajat. Puteți folosi numele serverului sau IP-ul serverului:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Introduceți numele de utilizator și parola sau lăsați aceste câmpuri goale dacă ați selectat "Toată lumea: Doar Citire" în pasul anterior.
5. Câmpul "WORKGROUP" este opțional și trebuie folosit dacă aveți un Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Ecran conector SMB Evermusic"
  caption="Ecran conector SMB Evermusic"
  width="400"
>}}

6. După ce ați conectat computerul folosind protocolul SMB, va apărea în secțiunea "Servicii cloud" din ecranul "Conexiuni".
7. Deschideți serviciul conectat și navigați la folderul dorit.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Folder SMB deschis în Evermusic"
  caption="Folder SMB deschis în Evermusic"
  width="400"
>}}

8. Puteți utiliza managerul de fișiere integrat pentru a edita fișierele după cum este necesar.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Manager de fișiere Evermusic"
  caption="Manager de fișiere Evermusic"
  width="400"
>}}

## Pasul 3: Soluție pentru folderele SMB2 cu caractere speciale

Uneori puteți întâmpina probleme cu folderele care conțin caractere speciale când folosiți protocolul SMB2. Iată câțiva pași pentru a rezolva această problemă:

1. **Activați SMB 1:**  
   • Ca soluție temporară, încercați să activați SMB 1 pe serverul dvs. și în setările aplicației. Acest lucru poate ajuta la ocolirea problemelor legate de caracterele speciale din numele folderelor.

2. **Folosiți meniul de deschidere fișiere al sistemului:**  
   • Navigați la "Fișiere locale".  
   • Derulați în jos la secțiunea "Fișiere pe acest dispozitiv".  
   • Atingeți "Deschideți fișiere..." sau "Deschideți foldere...".  
   • Localizați serverul și selectați fișierele sau folderele de care aveți nevoie.  
   • Atingeți "Deschideți" pentru a confirma selecția.

3. **Protocoale alternative:**  
   • Dacă problema persistă, luați în considerare conectarea la NAS folosind protocoalele WebDAV sau DLNA dacă NAS-ul dvs. suportă aceste opțiuni. Aceste protocoale pot gestiona caracterele speciale mai bine.

Urmând acești pași, puteți atenua problemele cu caracterele speciale din numele folderelor când folosiți protocolul SMB2.

## Concluzie

Cu acești pași, puteți accesa cu ușurință colecția vastă de fișiere de pe MAC sau PC pe iPhone sau iPad folosind aplicațiile noastre.

## Întrebări frecvente

{{% details title="Pot accesa fișierele de pe PC de pe iPhone fără iTunes?" closed="true" %}}
Da. Evermusic se conectează la computer prin SMB pe rețeaua Wi-Fi locală. Nu este necesară sincronizarea iTunes sau Finder. Activați partajarea fișierelor pe PC și conectați-vă direct din aplicație.
{{% /details %}}

{{% details title="Funcționează accesul la fișiere SMB prin internet?" closed="true" %}}
Nu. SMB este un protocol de rețea locală. iPhone-ul și computerul trebuie să fie pe aceeași rețea Wi-Fi. Pentru acces la distanță, încărcați fișierele într-un serviciu cloud precum Google Drive sau Dropbox și conectați-vă la acesta în Evermusic.
{{% /details %}}

{{% details title="Ce tipuri de fișiere pot accesa prin SMB?" closed="true" %}}
Evermusic suportă MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC și alte formate audio. Puteți, de asemenea, să navigați și să gestionați fișiere non-audio folosind managerul de fișiere integrat.
{{% /details %}}

{{% details title="Pot transfera fișiere de pe un NAS pe iPhone folosind SMB?" closed="true" %}}
Da. Majoritatea dispozitivelor NAS (Synology, QNAP, WD My Cloud și altele) suportă SMB. Conectați-vă la NAS folosind aceiași pași din acest ghid.
{{% /details %}}

{{% details title="Trebuie să copiez fișierele pe iPhone pentru a le reda?" closed="true" %}}
Nu. Evermusic transmite fișierele direct de pe computer sau NAS prin rețea. Fișierele nu sunt copiate pe iPhone decât dacă alegeți să le descărcați pentru redare offline.
{{% /details %}}

{{% details title="Este securizată partajarea fișierelor SMB?" closed="true" %}}
Partajarea fișierelor SMB funcționează doar pe rețeaua locală. Alte dispozitive din rețele diferite nu pot accesa folderele partajate. Pentru securitate suplimentară, folosiți un nume de utilizator și o parolă în loc de acces anonim (Toată lumea).
{{% /details %}}
