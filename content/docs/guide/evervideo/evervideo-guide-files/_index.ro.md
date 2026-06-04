---
title: "Fișiere"
date: 2020-02-01
lastmod: 2026-06-01
description: "Aflați cum să utilizați tab-ul Fișiere în Evervideo pe iPhone, iPad și Mac. Conectați servicii cloud, dispozitive NAS, servere media și fluxuri RTSP într-un singur loc. Gestionați videoclipuri offline, coada de transferuri, descărcări, Wi-Fi Drive, iTunes / Finder File Sharing și unități USB. Include iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA și stocare compatibilă S3."
keywords: [
  "fișiere Evervideo", "conexiuni Evervideo", "fișiere locale Evervideo",
  "configurare video cloud iPhone", "conectare Google Drive video", "streaming SMB video",
  "player WebDAV iOS", "video DLNA iPhone", "streaming NAS video",
  "transfer video Wi-Fi Drive", "Evervideo iTunes File Sharing", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "mod offline video Evervideo", "coadă transferuri Evervideo",
  "manager fișiere Evervideo", "folder Documente Evervideo",
  "player video Synology", "player video QNAP",
  "player video Apple Time Capsule", "USB DAC video",
  "player video iXpand", "player video S3"
]
tags: ["ghid", "evervideo", "fișiere", "conexiuni", "cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Tab-ul Fișiere este managerul de fișiere all-in-one al Evervideo. Spre deosebire de majoritatea aplicațiilor video care separă stocarea cloud de fișierele locale în tab-uri diferite, Evervideo le îmbină pe ambele într-un singur ecran derulabil, astfel puteți trece de la un server Plex la un folder în cloud la folderul Documente de pe iPhone fără a sări între tab-uri.

Tab-ul Fișiere este împărțit în secțiuni clare care apar în această ordine pe ecran:

- **Acces Rapid** — recente și favorite pentru fișierele și folderele deschise cel mai recent.
- **Fișiere în Această Aplicație** — ce se află în folderul Documente în sandbox al Evervideo.
- **Fișiere pe Acest iPhone / iPad / Mac** — videoclipuri din alte locații de pe dispozitiv, accesate prin selectorul de fișiere al sistemului.
- **Stocare Cloud** — fiecare cont cloud, NAS și server media conectat.
- **Dispozitive disponibile** — servere și unități descoperite automat prin Bonjour / mDNS în rețeaua locală.

În colțul din dreapta sus al ecranului Fișiere se află un buton Transferuri (o pictogramă cu săgeți rotitoare). Atingeți-l pentru a deschide Coada de Transferuri unde monitorizați fiecare descărcare și încărcare din toate sursele.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Fișiere în Stocări Conectate" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Conectare la Stocare Cloud

Secțiunea Stocare Cloud a tab-ului Fișiere este locul unde trăiesc toate conturile conectate, NAS-urile, serverele media și fluxurile — unul lângă altul, într-o listă derulabilă.

{{< cards cols="1">}}
  {{< card title="" subtitle="Secțiunea Stocare Cloud în Tab-ul Fișiere Evervideo" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Deschideți tab-ul **Fișiere**.
- Derulați la secțiunea **Stocare Cloud**.
- Atingeți **Conectare la stocare cloud** din meniu.
- Alegeți un serviciu de stocare cloud din listă.
- Introduceți datele de autentificare pe pagina de autorizare oficială furnizată de furnizorul cloud, apoi atingeți **Finalizat**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Conectare la un Serviciu de Stocare Cloud" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Dacă întâmpinați probleme, verificați conexiunea la internet și login-ul / parola. În versiunea Premium a aplicației, puteți adăuga un număr nelimitat de servicii; versiunea gratuită suportă până la trei.

## Servicii de Stocare Cloud, Servere Media și Protocoale Suportate

Evervideo suportă o gamă excepțional de largă de surse pentru videoclipurile dvs. Tot ce urmează funcționează dintr-un singur flux de Conectare la stocare cloud.

**Stocare personală în cloud:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Servere media auto-găzduite:** Plex · Jellyfin · Emby · Subsonic (și fiecare server compatibil Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (și ownCloud prin API-ul partajat) · Synology Drive · QNAP.

**Protocoale NAS și partajare fișiere:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, parolă sau autentificare prin cheie publică) · NFS · DLNA / UPnP (redare și descărcare).

**Fluxuri live și camere IP:** RTSP — îndreptați Evervideo spre orice URL `rtsp://` și redă imediat. Excelent pentru camere de securitate, fluxuri IPTV, camere sonerie, monitoare pentru bebeluși și surse live similare.

**Stocare de obiecte compatibilă S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces și orice alt endpoint API S3.

**Biblioteci de pe dispozitiv:** biblioteca Fotografii (toate videoclipurile, înregistrări ecran, albume foto) și biblioteca aplicației Muzică (Albume, Genuri, Liste de redare) — ambele disponibile în interiorul Bibliotecii Media fără a copia nimic.

**Descoperire rețea locală:** secțiunea Dispozitive disponibile listează automat fiecare serviciu Bonjour / mDNS din rețeaua Wi-Fi — servere Plex, Jellyfin, Emby, Synology, QNAP, routere AirPort cu unități atașate, Apple Time Capsule — astfel puteți atinge pentru a vă conecta fără a tasta o adresă IP.

Fiecare conexiune folosește SDK-ul oficial sau protocolul deschis al serviciului, cu autorizare bazată pe OAuth unde este suportat. Puteți conecta mai multe conturi ale aceluiași serviciu (de exemplu, două conturi Google Drive sau atât un server Plex cât și unul Jellyfin) și le puteți naviga unul lângă altul în secțiunea Stocare Cloud.

## Securitate și Confidențialitate

Evervideo folosește numai SDK-uri oficiale și conexiuni securizate pentru a interacționa cu serviciile cloud conectate. Login-ul și parola dvs. nu sunt accesibile aplicației — toate transferurile sunt criptate TLS.

Când introduceți login-ul și parola, aplicația vă arată pagina de autorizare oficială furnizată de furnizorul de servicii cloud, iar întregul proces de autorizare are loc în afara aplicației. Furnizorul de servicii cloud trimite apoi un token de autentificare aplicației după autorizarea cu succes, iar acel token este folosit pentru a face apeluri API.

Un token de autentificare este o cheie digitală care permite aplicațiilor terțe să interacționeze cu stocarea cloud în numele dvs. Token-ul este stocat pe dispozitiv în stocarea securizată de sistem Apple (Keychain), care este criptată în repaus și protejată de codul de acces al dispozitivului sau blocarea biometrică. Puteți descărca fișiere din serviciile cloud conectate pe dispozitiv; aceste fișiere sunt plasate în directorul Documente al aplicației și pot fi eliminate oricând folosind managerul de fișiere incorporat.

Aplicația nu partajează nicio informație din conturile cloud conectate cu Everappz, agenți de publicitate sau orice terță parte. Puteți revoca accesul la contul cloud oricând deschizând pagina de setări a contului în browserul web.

## Revocare Token de Autentificare

Pentru a revoca un token de autentificare, conectați-vă la contul cloud într-un browser web și navigați la pagina de securitate sau aplicații conectate. Acolo puteți găsi fiecare aplicație terță conectată la contul cloud și le puteți elimina pe oricare dacă nu mai doriți să o utilizați. Instrucțiuni detaliate pentru conturile Google sunt disponibile [aici](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

De asemenea, puteți deconecta contul cloud în interiorul aplicației — când faceți acest lucru, token-ul de autentificare este șters imediat de pe dispozitiv. Dacă dezinstalați aplicația de pe dispozitiv, toate datele descărcate și token-urile de acces sunt eliminate automat împreună cu aceasta.

## Deconectare Stocare Cloud sau Modificare Configurație

- **Accesați opțiunile de stocare cloud** — localizați serviciul conectat în secțiunea **Stocare Cloud** a tab-ului Fișiere.
- **Atingeți butonul "..."** de lângă titlul serviciului pentru a deschide opțiuni suplimentare:
  - **Redenumire** — schimbați numele serviciului cloud cum apare în lista dvs.
  - **Setări** — modificați configurația sau datele de autentificare. Uneori poate fi necesar să re-autorizați serviciul cloud conectat dacă token-ul de autorizare a expirat.
  - **Deconectare** — întrerupeți complet conexiunea dintre aplicație și serviciul cloud. Aceasta elimină toate videoclipurile asociate cu acel serviciu din biblioteca media, dar le lasă neafectate pe server.

## Conectare la un Computer sau NAS

Puteți conecta calculatorul, NAS-ul personal sau alt dispozitiv de rețea folosind protocolul SMB, WebDAV, FTP / FTPS, SFTP, NFS sau DLNA. Aceasta este cea mai ușoară modalitate de a aduce o bibliotecă media de acasă existentă — fie că se află pe un Mac, PC Windows, Synology, QNAP, Apple Time Capsule sau WD My Cloud Home — în Evervideo fără a copia nimic.

### Conectare la un Computer Folosind SMB

- Atingeți **Conectare la stocare cloud → SMB**.
- Introduceți adresa IP a computerului și numele folderului partajat folosind formatul `smb://adresa-ip-computer/nume-folder-partajat`.
- Alegeți versiunea protocolului: **Auto**, **SMB1** sau **SMB2**.
- Introduceți login-ul și parola (dacă este necesar).
- Atingeți **Finalizat**.

Dacă conexiunea este reușită, partajarea apare în secțiunea Stocare Cloud. Un tutorial complet despre cum să conectați Mac-ul sau PC-ul folosind SMB este disponibil [aici](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Conectare la un NAS Folosind WebDAV

Toți pașii sunt aceiași ca pentru SMB, cu excepția câmpului URL. Folosiți `http://nume-server` sau `https://nume-server` dacă serverul suportă SSL. WebDAV funcționează cu Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home și orice alt server cu un endpoint WebDAV.

Un tutorial complet despre WebDAV este disponibil [aici](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Conectare prin DLNA / UPnP

Partajați o bibliotecă media aflată pe PC-ul Windows sau NAS-ul dvs. folosind protocolul DLNA / UPnP și accesați-o în Evervideo conform descrierii [aici](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA este larg suportat, dar permite numai redarea sau descărcarea videoclipurilor — nu puteți încărca fișiere sau crea foldere noi pe un server DLNA.

### Conectare Folosind FTP, FTPS sau SFTP

Evervideo suportă și protocoalele clasice de transfer de fișiere. Pentru a conecta un server prin FTP sau FTPS, atingeți Conectare la stocare cloud → FTP, introduceți URL-ul gazdei în formatul `ftp://nume-server` (sau `ftps://nume-server` pentru o conexiune criptată), furnizați login-ul și parola, apoi atingeți Finalizat. Pentru SFTP (SSH File Transfer Protocol), alegeți SFTP și furnizați fie o parolă, fie o pereche de chei SSH.

### Conectare la o Partajare NFS

Evervideo include suport NFS (Network File System) — util pentru gazde Linux, servere BSD și dispozitive NAS care preferă să expună bibliotecile video prin NFS în loc de SMB. Alegeți NFS în meniul Conectare la stocare cloud, introduceți adresa serverului și calea exportată, și atingeți Finalizat.

## Conectare la un Plex Media Server

Evervideo se poate conecta direct la un Plex Media Server și naviga în bibliotecile de Filme, Seriale TV și Videoclipuri de Acasă. Atingeți Conectare la stocare cloud → Plex, conectați-vă cu contul Plex, alegeți un server și biblioteca apare alături de serviciile cloud. Serverele Plex din aceeași rețea locală sunt de asemenea descoperite automat în secțiunea Dispozitive disponibile.

## Conectare la un Server Jellyfin sau Emby

Atât Jellyfin (open-source) cât și Emby (comercial) funcționează nativ în Evervideo. Atingeți Conectare la stocare cloud → Jellyfin sau Emby, introduceți URL-ul serverului (de obicei ceva de genul `http://ip-server:8096`) și credențialele, și biblioteca dvs. este gata de streaming.

## Conectare la un Server Subsonic sau Navidrome

Evervideo vorbește API-ul Subsonic, ceea ce înseamnă că funcționează cu Subsonic însuși, Navidrome și orice alt server compatibil Subsonic — inclusiv Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) și Ampache. Atingeți Conectare la stocare cloud → Subsonic, introduceți URL-ul serverului și credențialele, și biblioteca apare în secțiunea Stocare Cloud.

## Conectare la un Flux RTSP (Camere IP, Live TV, IPTV)

Evervideo are suport RTSP nativ, astfel puteți îndrepta aplicația spre orice sursă RTSP — camere de securitate, camere sonerie, furnizori IPTV, monitoare pentru bebeluși, fluxuri de difuzare — și Evervideo va prelua și decodifica fluxul live. Atingeți Linkuri Online → Adăugare link, lipiți URL-ul complet (`rtsp://ip-camera:port/cale-flux`), furnizați login și parolă dacă este necesar, și atingeți Finalizat.

## Conectare la Stocare de Obiecte Compatibilă S3

Pentru utilizatorii cu auto-găzduire și utilizatorii avansați care folosesc stocarea de obiecte în cloud, Evervideo include un conector compatibil S3. Atingeți Conectare la stocare cloud → Stocare S3, apoi introduceți URL-ul endpoint-ului, regiunea, cheia de acces, cheia secretă și numele bucket-ului. Funcționează cu AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces și orice alt endpoint API S3.

## Dispozitive Disponibile

Această secțiune afișează fiecare dispozitiv din rețeaua locală la care vă puteți conecta din Evervideo prin descoperire Bonjour / mDNS — servere Plex, Jellyfin, Emby, Synology, QNAP, routere AirPort cu unități atașate, Apple Time Capsule și altele. Pentru a stabili o conexiune:

- Derulați la secțiunea Dispozitive disponibile în tab-ul Fișiere.
- Atingeți dispozitivul la care doriți să vă conectați.
- Dacă este necesar, introduceți datele de autentificare pentru a finaliza conexiunea.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Dispozitive Disponibile în Rețeaua Locală" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive vă permite să transferați fișiere wireless de pe computer pe dispozitivul iOS prin orice browser de desktop, Finder sau File Explorer. Dispozitivul și computerul dvs. trebuie să fie în aceeași rețea Wi-Fi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Activare Wi-Fi Drive

- În tab-ul Fișiere, derulați la Stocare Cloud → Conectare prin Wi-Fi pentru a deschide ecranul principal Wi-Fi Drive.
- (Opțional) Setați un nume de utilizator și o parolă pentru serverul web incorporat.
- Atingeți Pornire Wi-Fi Drive.

### Accesare Wi-Fi Drive pe Computer

- Deschideți un browser web pe computer (Chrome, Firefox, Safari, etc.).
- Introduceți URL-ul afișat de aplicație.
- Trageți și plasați fișiere de pe computer pe pagina web — vor începe să se transfere pe dispozitivul iOS.

Puteți monta și Wi-Fi Drive direct în **Finder** pe macOS (Go → Conectare la Server…) sau File Explorer pe Windows (Mapare Unitate de Rețea…) și să tratați iPhone-ul sau iPad-ul ca o unitate de rețea obișnuită.

Instrucțiuni detaliate sunt disponibile [aici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (acum Finder File Sharing pe macOS Catalina și versiunile ulterioare) vă permite să transferați fișiere folosind un cablu Lightning sau USB-C. Conectați dispozitivul, deschideți Finder pe Mac (sau iTunes pe Windows), găsiți Evervideo în lista de aplicații și copiați fișierele în folderul partajat.

## Conectare Unitate USB Flash sau Card SD

Conectați o unitate USB sau un card SD la iPhone, iPad sau Mac prin adaptorul Lightning-la-USB / USB-C sau cititorul de carduri. Deschideți Fișiere → Fișiere pe Acest iPhone → Deschidere Folder, navigați la unitate și alegeți un fișier video sau folder. Evervideo redă fișierele direct de pe unitate fără a le copia în stocarea internă — util pentru biblioteci 4K foarte mari.

## Navigare Foldere în Stocări Conectate

Atingeți orice serviciu cloud conectat pentru a deschide browserul de fișiere. Folderele arată miniaturile video când sunt disponibile, iar atingerea unui videoclip pornește redarea imediat, continuând să transmită restul fișierului în fundal.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Navigare Foldere în Stocări Conectate" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Acces Rapid

Secțiunea Acces Rapid se află în partea de sus a tab-ului Fișiere. Oferă acces rapid la fișierele și folderele preferate și deschise recent — atât din serviciile cloud cât și din stocarea de pe dispozitiv. De fiecare dată când deschideți un fișier sau folder din cloud, acesta este adăugat la lista Deschis Recent. Puteți marca folderele profund imbricate ca Preferințe pentru a le accesa rapid fără a parcurge structura de directoare.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Linkuri Online și Acces Rapid" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Fișiere în Această Aplicație

Această secțiune afișează fișierele și folderele stocate în directorul Documente sandbox al Evervideo — tot ce ați descărcat din cloud, transferat prin Wi-Fi Drive, copiat prin Finder File Sharing sau importat din altă aplicație.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Fișiere în Această Aplicație" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Folderul Documente

Folderul Documente este rădăcina a tot ceea ce se află în Fișiere în Această Aplicație. Puteți crea subfoldere, redenumi fișiere, le puteți muta și le puteți grupa cum doriți.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Fișiere Locale — Folderul Documente" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Fișiere pe Acest iPhone / iPad / Mac

Această secțiune afișează videoclipuri situate pe dispozitiv dar în aplicații diferite. Le puteți importa în Evervideo folosind selectorul de fișiere al sistemului:

- Atingeți Deschidere Fișiere… pentru a selecta fișiere specifice.
- Atingeți Deschidere Folder… pentru a selecta un folder întreg.

Puteți folosi și Conectare Folder pentru a crea un link la un folder de pe dispozitiv cu acces de citire / scriere — perfect pentru a lucra cu un folder pe iCloud Drive sau o unitate USB atașată fără a copia nimic.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Fișiere pe Acest Dispozitiv" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Foldere Speciale

În tab-ul Fișiere veți vedea mai multe foldere speciale pe care Evervideo le creează și le utilizează automat:

- **Descărcări** — fiecare fișier descărcat din cloud apare aici implicit. Personalizați în Setări → Manager Fișiere → Salvare Fișiere Descărcate În.
- **Cache Player** — cache-ul playerului media. Implicit, playerul descarcă videoclipurile viitoare pentru o redare fluidă. Puteți dezactiva cache-ul în setările aplicației sau pur și simplu ștergeți acest folder.
- **iCloud** — fișierele din acest folder se sincronizează pe toate dispozitivele conectate la același cont iCloud.
- **Foldere offline** — când marcați un folder, o listă de redare, un album sau un gen ca disponibil offline, fișierele sunt descărcate în acest folder.

## Bara de Instrumente Superioară

Bara de instrumente superioară, localizată sub bara de navigare, oferă mai multe acțiuni pe care le puteți afișa sau ascunde cu un gest de glisare în jos:

- **Căutare** — efectuați o căutare în folderul sau secțiunea curentă.
- **Continuare Redare** — dacă este activat în setări, restaurați coada playerului și ultima poziție video pentru folderul curent.
- **Redare Toate** — scanați folderul curent și subfolderele sale și adăugați fișierele în coada playerului.
- **Amestecare Toate** — ca Redare Toate, dar amestecă înainte de adăugare.

## Opțiuni Folder

Când deschideți un folder, atingeți butonul **"..."** din colțul din dreapta sus pentru aceste acțiuni:

- **Selectați** — activați modul de selecție a fișierelor.
- **Folder Nou** — creați un folder nou în folderul curent.
- **Activare modul offline** — activați sincronizarea offline pentru folderul curent. Fișierele noi adăugate online sunt descărcate automat.
- **Încărcare Fișiere** — încărcați fișiere de pe dispozitiv în folderul online.
- **Căutare** — căutați în folder.
- **Sortare** — sortați fișierele după nume, dimensiune, dată modificare sau metadate.
- **Vizualizare Grilă / Listă** — comutați între vizualizarea tabel și vizualizarea miniatură. Vizualizarea miniatură afișează previzualizări mari ale posterelor video.

## Mod Selecție

Atingeți **"..."** în colțul din dreapta sus și alegeți **Selectați** pentru a intra în modul de selecție. Apar casete de selecție lângă fiecare fișier și folder. Atingeți pentru a selecta unul sau mai multe elemente, apoi efectuați acțiuni în lot: Redare Ulterioară, Redare Mai Târziu, Adăugare la Biblioteca Media, Adăugare la o Listă de Redare, Copiere, Încărcare, Mutare, Redenumire sau Ștergere.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Mod Selecție în Managerul de Fișiere" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Dacă preferați să tratați stocarea cloud conectată ca numai citire (pentru a preveni ștergerile accidentale), activați Setări → Manager Fișiere → Editare Fișiere Online → Oprit pentru a ascunde toate operațiunile distructive din interfață.

## Acțiuni Fișier

Atingeți pictograma **"..."** de lângă titlul unui fișier pentru a dezvălui meniul de acțiuni:

- **Redare Ulterioară** — inserați fișierul în partea de sus a cozii playerului.
- **Redare Mai Târziu** — adăugați fișierul la sfârșitul cozii playerului.
- **Adăugare la Biblioteca Media** — incorporați fișierul în biblioteca media, organizată după Album și Gen.
- **Adăugare la o Listă de Redare** — adăugați fișierul la o listă de redare existentă sau creați una nouă.
- **Editare Etichete** — deschideți editorul de etichete incorporat pentru a modifica metadatele. Pentru fișierele online, fișierul este temporar descărcat, editat și apoi re-încărcat după confirmare.
- **Adăugare la Preferințe** — adăugați fișierul la lista de preferințe pentru acces rapid.
- **Descărcați** — descărcați fișierul sau folderul pe dispozitiv pentru utilizare offline.
- **Redenumire** — redenumiți fișierul direct pe stocarea la distanță.
- **Mutare** — mutați fișierul într-un folder diferit din stocarea cloud.
- **Adăugare la Arhivă** — grupați fișierul într-un singur fișier ZIP (funcție Premium).
- **Deschidere În** — exportați fișierul într-o altă aplicație compatibilă prin foaia de partajare a sistemului.
- **Șterge** — eliminați permanent fișierul. **Această acțiune nu poate fi anulată.**

## Acțiuni Folder

Pentru fiecare folder din stocarea cloud, aveți multe acțiuni disponibile atingând pictograma **"..."** de lângă titlul folderului.

- **Redare Toate** — înlocuiți coada curentă a playerului cu fiecare videoclip din folder.
- **Redare Ulterioară / Redare Mai Târziu** — adăugați folderul întreg în coadă.
- **Adăugare la Biblioteca Media** — incorporați conținutul folderului în biblioteca media.
- **Adăugare la Listă de Redare** — adăugați folderul întreg la o listă de redare.
- **Adăugare la Preferințe** — adăugați folderul la preferințele dvs.
- **Activare Mod Offline** — dincolo de o simplă descărcare, monitorizează continuu folderul pentru fișiere noi și le descarcă automat pe măsură ce apar online.
- **Descărcați** — descărcați tot conținutul folderului pe dispozitiv pentru acces offline.
- **Redenumire / Mutare** — redenumiți sau mutați folderul în stocarea la distanță.
- **Adăugare la Arhivă** — grupați conținutul folderului într-un fișier ZIP (funcție Premium).
- **Șterge** — eliminați permanent folderul și conținutul său. **Această acțiune nu poate fi anulată.**

## Coada de Transferuri

În colțul din dreapta sus al tab-ului Fișiere se află un buton **Transferuri** (o pictogramă cu săgeți rotitoare). Atingeți-l pentru a deschide Coada de Transferuri — o listă cu fiecare descărcare și încărcare activă din toate sursele, cu progres în timp real, viteză și ETA per fișier.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Coadă de Transferuri Fișiere" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Puteți întrerupe, relua, reîncerca transferurile eșuate, rearanja elementele pentru a prioritiza descărcări specifice sau le puteți anula individual. Puteți ajusta și viteza cozii de transferuri (numărul maxim de sarcini paralele), tipul de rețea (numai Wi-Fi sau Wi-Fi + Celular) și transferurile în fundal în Setări → Manager Fișiere.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Acțiuni în Coada de Transferuri Fișiere" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Mod Offline și Foldere Offline Sincronizate

Modul offline este o funcție utilă care vă permite să vizionați videoclipurile preferate chiar și când nu sunteți conectat la internet. Când activați modul offline pentru orice folder, listă de redare, album sau gen, toate fișierele din acea colecție sunt descărcate automat pe dispozitiv pentru redare offline. Apar în secțiunea Foldere offline.

Când adăugați fișiere noi pe serverul la distanță, acestea sunt de asemenea descărcate automat — astfel colecția offline rămâne actualizată fără să faceți nimic. Pentru a resincroniza manual, atingeți cele trei puncte din colțul din dreapta sus al unui folder offline și selectați Sincronizați.

Puteți ajusta timeout-ul de sincronizare în Setări → Manager Fișiere → Foldere offline sincronizate → Interval de Timp.

Instrucțiuni detaliate sunt disponibile [aici](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalizare

În Setări → Personalizare puteți configura modul în care tab-ul Fișiere este prezentat:

- **Stilul Ecranului Fișiere** — Meniu Simplu (afișează direct lista de foldere) sau Meniu Grupat (grupează conținutul pe categorii — Acces Rapid, Foldere Speciale, Stocare Cloud, etc.).
