---
title: "Conexiuni"
date: 2020-02-01
description: "Aflați cum să conectați servicii cloud și dispozitive NAS la Flacbox. Transmiteți muzică de înaltă rezoluție din iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk și altele. Folosiți SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, Partajare fișiere iTunes / Finder și unități USB flash."
keywords: [
  "configurare cloud Flacbox", "conectare Google Drive la Flacbox", "streaming SMB",
  "player WebDAV iOS", "aplicație DLNA", "streaming audio NAS", "Wi-Fi Drive iPhone",
  "transfer fișiere pe iPhone", "Flacbox Partajare fișiere iTunes", "conectare NAS la iPhone",
  "aplicație muzică Synology Drive", "aplicație muzică QNAP", "aplicație muzică Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "aplicație muzică scrobbling Last.fm",
  "muzică iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["ghid", "flacbox", "conexiuni", "cloud", "NAS"]
readingTime: 12
---


Pe acest ecran, puteți conecta fiecare sursă care conține muzica dvs. Puteți integra servicii cloud populare precum Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive și multe altele, precum și Mac-ul, PC-ul sau NAS-ul dvs. prin protocoale standard. Indiferent dacă colecția dvs. se află pe un serviciu prietenos cu streaming-ul precum Dropbox sau pe un NAS personal precum Synology, QNAP, Buffalo, Apple Time Capsule sau WD My Cloud Home, Flacbox se conectează la toate dintr-un singur ecran.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecranul Conexiuni al Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Conectare la Stocare în Cloud

- Deschideți fila **Conexiuni**.
- Selectați **Conectare la stocare în cloud** din meniu.
- Alegeți un serviciu de stocare în cloud din listă.
- Introduceți credențialele pe pagina oficială de autorizare furnizată de furnizorul cloud, apoi atingeți **Finalizat**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Adăugare Serviciu de Stocare în Cloud" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Dacă întâmpinați probleme, verificați conexiunea la internet și login-ul / parola. În versiunea Premium a aplicației, puteți adăuga un număr nelimitat de servicii; versiunea gratuită acceptă până la trei.

## Servicii de Stocare în Cloud, Servere Media și Protocoale Acceptate

Flacbox acceptă o gamă excepțional de largă de surse pentru muzica dvs. Totul de mai jos funcționează dintr-un singur ecran **Conectare la stocare în cloud**.

**Stocare personală în cloud:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Servere auto-găzduite:** Plex · Jellyfin · Emby · Subsonic (și orice server compatibil Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (și ownCloud prin API-ul partajat) · Synology Drive · QNAP.

**Protocoale NAS și partajare fișiere:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, parolă sau autentificare cu cheie publică) · NFS · DLNA / UPnP (redare și descărcare).

**Stocare de obiecte compatibilă S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces și orice alt endpoint S3-API.

**Descoperire în rețeaua locală:** Secțiunea Dispozitive disponibile listează automat fiecare serviciu Bonjour / mDNS din rețeaua Wi-Fi, astfel puteți conecta fără a tasta adrese IP.

Fiecare conexiune utilizează **SDK-ul oficial sau protocolul deschis** al serviciului, cu autorizare bazată pe OAuth unde este acceptată. Puteți conecta mai multe conturi ale aceluiași serviciu (de exemplu, două conturi Google Drive, un Dropbox personal alături de unul de serviciu, sau atât un server Plex, cât și unul Jellyfin) și le puteți naviga unul lângă celălalt în ecranul Conexiuni.

## Securitate și Confidențialitate

Folosim numai SDK-uri oficiale și conexiuni securizate pentru a interacționa cu serviciile cloud conectate. Login-ul și parola dvs. nu sunt accesibile aplicației — toate transferurile sunt criptate cu TLS.

Când introduceți login-ul și parola, aplicația vă arată pagina oficială de autorizare furnizată de furnizorul serviciului cloud, iar întregul proces de autorizare are loc în afara aplicației. Furnizorul serviciului cloud trimite apoi un token de autentificare aplicației după autorizarea reușită, iar acel token este folosit pentru apelurile API.

Un token de autentificare este o cheie digitală care permite aplicațiilor terțe să interacționeze cu stocarea în cloud în numele dvs. Token-ul este stocat pe dispozitivul dvs. în stocarea securizată a sistemului Apple (Keychain), care este criptată în repaus și protejată de codul de acces al dispozitivului sau blocarea biometrică. Puteți descărca fișiere din serviciile cloud conectate pe dispozitivul dvs.; acele fișiere sunt plasate în directorul Documente al aplicației și pot fi eliminate în orice moment folosind managerul de fișiere integrat.

Aplicația nu partajează nicio informație din conturile dvs. cloud conectate cu Everappz, agenți publicitari sau orice terță parte. Puteți revoca accesul la contul dvs. cloud în orice moment deschizând pagina de setări a contului în browserul web.

## Respingere Token de Autentificare

Pentru a revoca un token de autentificare, conectați-vă la contul dvs. cloud într-un browser web și navigați la pagina de securitate sau aplicații conectate. Acolo puteți găsi fiecare aplicație terță conectată la contul dvs. cloud și le puteți elimina pe oricare dacă nu mai doriți să o utilizați. Instrucțiuni detaliate pentru conturi Google sunt disponibile [aici](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Puteți, de asemenea, deconecta contul cloud din interiorul aplicației — când faceți asta, token-ul de autentificare este imediat șters de pe dispozitivul dvs. Dacă dezinstalați aplicația de pe dispozitivul dvs., toate datele descărcate și token-urile de acces sunt eliminate automat odată cu ea.

## Deconectare Stocare în Cloud sau Schimbare Configurație

- **Accesați opțiunile de stocare în cloud** — localizați serviciul conectat în ecranul **Conexiuni**.
- **Atingeți butonul „..."** de lângă titlul serviciului pentru a deschide opțiuni suplimentare:
  - **Redenumire** — schimbați numele serviciului cloud cum apare în lista dvs.
  - **Setări** — modificați configurația sau datele de autentificare. Uneori poate fi necesar să reautorizați serviciul cloud conectat dacă token-ul de autorizare a expirat.
  - **Deconectare** — tăiați complet conexiunea dintre aplicație și serviciul cloud. Aceasta elimină toate melodiile asociate acelui serviciu din biblioteca muzicală a aplicației, dar le lasă neatinse pe server.

## Conectare la Calculator sau NAS

Puteți, de asemenea, să conectați calculatorul, NAS-ul personal sau alte dispozitive de rețea utilizând protocoalele SMB, DLNA sau WebDAV. Aceasta este cea mai ușoară modalitate de a aduce o bibliotecă muzicală domestică existentă — fie ea pe un Mac, PC Windows, un dispozitiv Synology sau un NAS — în Flacbox fără a copia nimic.

## Conectare la Calculator Folosind SMB

- Atingeți **Conectare la stocare în cloud → SMB**.
- Introduceți adresa IP a calculatorului și numele folderului partajat în câmpul URL folosind formatul `smb://adresa-ip-calculator/nume-folder-partajat`.
- Alegeți versiunea protocolului: **Auto**, **SMB1** sau **SMB2**.
- Introduceți login-ul și parola (dacă este necesar).
- Atingeți **Finalizat**.

Dacă conexiunea este reușită, veți vedea stocarea conectată în secțiunea **Stocare în Cloud**. Un tutorial complet despre cum să conectați Mac-ul sau PC-ul folosind SMB este disponibil [aici](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Conectare la NAS Folosind WebDAV

Toți pașii sunt aceiași ca pentru SMB, cu excepția câmpului URL. URL-ul trebuie să fie în formatul `http://nume-server` sau `https://nume-server` dacă serverul acceptă SSL. WebDAV funcționează cu **Synology, QNAP, Nextcloud, ownCloud** și multe alte servere — oriunde este disponibil un endpoint WebDAV.

Un tutorial complet despre cum să conectați un NAS folosind WebDAV este disponibil [aici](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Conectare la Calculator sau NAS Folosind DLNA

Puteți, de asemenea, să partajați o bibliotecă muzicală situată pe PC-ul dvs. Windows sau NAS personal folosind protocolul DLNA / UPnP și să accesați acea bibliotecă în aplicație conform descrierii de [aici](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA este un protocol popular, larg acceptat, dar vă permite numai să redați sau să descărcați muzică — nu puteți încărca fișiere sau crea foldere noi pe un server DLNA.

## Conectare la NAS sau Server Folosind FTP, FTPS sau SFTP

Flacbox acceptă, de asemenea, protocoalele clasice de transfer de fișiere. Pentru a conecta un server prin FTP sau FTPS, atingeți **Conectare la stocare în cloud → FTP**, introduceți URL-ul gazdei în forma `ftp://nume-server` (sau `ftps://nume-server` pentru o conexiune criptată), furnizați login-ul și parola, apoi atingeți **Finalizat**. Pentru **SFTP** (SSH File Transfer Protocol), alegeți **SFTP** în schimb și furnizați fie o parolă, fie o pereche de chei SSH. Ambele funcționează cu dispozitive NAS, gazde Linux și orice server care are un daemon FTP / FTPS / SSH.

## Conectare la un Share NFS

Flacbox include suport **NFS** (Network File System) — util pentru gazde Linux, servere BSD și dispozitive NAS care preferă să expună bibliotecile muzicale prin NFS în loc de SMB. Alegeți **NFS** în meniul **Conectare la stocare în cloud**, introduceți adresa serverului și calea exportată, și atingeți **Finalizat**.

## Conectare la un Server Plex Media Server

Flacbox se poate conecta direct la un Plex Media Server și naviga biblioteca muzicală după Artiști, Albume, Genuri și Liste de redare. Atingeți **Conectare la stocare în cloud → Plex**, autentificați-vă cu contul Plex, alegeți un server, și biblioteca apare alături de serviciile dvs. cloud. Serverele Plex din aceeași rețea locală sunt, de asemenea, descoperite automat în secțiunea **Dispozitive disponibile**.

## Conectare la un Server Jellyfin sau Emby

Atât **Jellyfin** (open-source) cât și **Emby** (comercial) funcționează nativ în Flacbox. Atingeți **Conectare la stocare în cloud → Jellyfin** sau **Emby**, introduceți URL-ul serverului (ceva de genul `http://ip-server:8096`) și credențialele, și biblioteca dvs. muzicală este gata de transmis. Ca și cu Plex, bibliotecile din rețeaua locală sunt listate automat în **Dispozitive disponibile**.

## Conectare la un Server Subsonic sau Navidrome

Flacbox vorbește API-ul Subsonic, ceea ce înseamnă că funcționează cu **Subsonic** în sine, **Navidrome** și orice alt server compatibil Subsonic — inclusiv Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Atingeți **Conectare la stocare în cloud → Subsonic**, introduceți URL-ul serverului și credențialele, și biblioteca apare în ecranul Conexiuni. Aceasta este cea mai ușoară modalitate de a da Flacbox acces la o colecție muzicală auto-găzduită fără a expune share-ul de fișiere subiacent.

## Conectare la Stocare de Obiecte Compatibilă S3

Pentru cei care auto-găzduiesc și audiófilii care utilizează stocare de obiecte în cloud, Flacbox include un conector compatibil S3. Atingeți **Conectare la stocare în cloud → Stocare S3**, apoi introduceți URL-ul endpoint-ului, regiunea, cheia de acces, cheia secretă și numele bucket-ului. Funcționează cu AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces și orice alt serviciu care expune un endpoint S3-API.

## Dispozitive Disponibile

Această secțiune afișează fiecare dispozitiv din rețeaua locală la care vă puteți conecta din Flacbox prin descoperire Bonjour. Pentru a stabili o conexiune, urmați acești pași:

- Deschideți aplicația și mergeți la secțiunea **Dispozitive disponibile** din Conexiuni.
- Atingeți dispozitivul la care doriți să vă conectați.
- Dacă este necesar, introduceți datele de login pentru a finaliza conexiunea.

Aceasta este cea mai rapidă modalitate de a descoperi un share SMB, WebDAV, DLNA în rețeaua dvs. de acasă fără a tasta manual adrese IP.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Dispozitive Disponibile în Rețeaua Locală" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive este o tehnologie convenabilă care permite transferuri wireless de fișiere de pe computer pe dispozitivul iOS prin orice browser de desktop. Pentru a utiliza această funcție eficient, asigurați-vă că dispozitivul și computerul sunt conectate la aceeași rețea Wi-Fi. Iată un ghid pas cu pas despre cum să utilizați Wi-Fi Drive.

### Activare Wi-Fi Drive

- Deschideți aplicația și mergeți la fila **Conexiuni**.
- Selectați **Conectare prin Wi-Fi** pentru a accesa ecranul principal Wi-Fi Drive.
- (Opțional) Setați un nume de utilizator și o parolă pentru serverul web integrat pentru a proteja accesul.
- Atingeți **Pornire Wi-Fi Drive** pentru a activa Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Accesarea Wi-Fi Drive pe Calculator

- Pe calculatorul dvs. (desktop sau laptop), deschideți un browser (cum ar fi Chrome, Firefox sau Safari).
- În bara de adrese a browserului, introduceți URL-ul furnizat de aplicație.

### Transfer Wireless de Fișiere

Odată ce pagina web corespunzătoare dispozitivului dvs. iOS se deschide în browser, puteți trage și plasa cu ușurință fișiere de pe computer pe pagina web. Fișierele pe care le plasați vor începe să se transfere pe dispozitivul dvs. iOS și vor fi accesibile în Flacbox.

De asemenea, puteți monta Wi-Fi Drive direct în Finder pe macOS (Du-te → Conectare la server…) sau File Explorer pe Windows (Mapare unitate de rețea…) și tratați iPhone-ul sau iPad-ul ca o unitate de rețea obișnuită.

Instrucțiuni detaliate despre cum să transferați fișiere wireless folosind Wi-Fi Drive sunt disponibile [aici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Partajare Fișiere iTunes / Finder

Partajarea fișierelor iTunes (acum Partajarea fișierelor Finder pe macOS Catalina și versiunile ulterioare) este o altă modalitate de a transfera fișiere de la un computer la un dispozitiv folosind un cablu Lightning sau USB-C.

- Conectați dispozitivul la computer folosind un cablu și rulați **Finder** pe Mac (sau **iTunes** pe Windows).
- Deschideți **Locații → Dispozitivul Dvs. Conectat → Fișiere** și găsiți aplicația Flacbox.
- Atingeți pictograma aplicației pentru a vedea toate folderele partajate.
- Copiați fișiere de pe computer în folderul partajat de pe dispozitiv folosind drag-and-drop.

Instrucțiuni detaliate despre cum să utilizați Partajarea fișierelor Finder sunt disponibile [aici](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Conectare Unitate USB Flash

Dacă aveți un card SD sau o unitate USB, o puteți conecta folosind un cititor Lightning la USB / SD Card sau o unitate USB-C (pe iPad și iPhone 15 / 16 / 17 / Pro). Aplicația acceptă cititoare de carduri certificate de Apple și iXpand Flash Drives. Cu un iXpand Flash Drive, introduceți-l în portul Lightning și deschideți aplicația — veți vedea un mesaj Dispozitiv extern conectat și informațiile despre dispozitiv. Atingeți pictograma unității flash pentru a accesa folderul de muzică și atingeți orice fișier audio pentru a începe redarea.

Avem instrucțiuni detaliate despre cum să conectați o unitate USB flash la iPhone și să ascultați muzică sau să gestionați fișiere situate pe ea [aici](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Manager Fișiere

Odată ce ați conectat un serviciu de stocare în cloud, atingeți pictograma acestuia pentru a vedea toate fișierele și folderele disponibile. Puteți utiliza managerul de fișiere integrat pentru a lucra cu aceste fișiere — descărcare, redenumire, mutare, încărcare, ștergere și altele. Când începeți o descărcare, fișierul apare în coada de transfer. Pentru a deschide coada de transfer, mergeți la fila Fișiere Locale și atingeți pictograma săgeților rotative din colțul din stânga sus. Toate fișierele și folderele descărcate sunt disponibile în secțiunea Fișiere Locale.

## Bara de Instrumente Superioară

Bara de instrumente superioară, localizată convenabil sub bara de navigare, oferă câteva acțiuni utile pentru acces ușor. O puteți afișa sau ascunde cu un simplu gest de glisare în jos.

- **Căutare** — efectuați o căutare rapidă în directorul curent, facilitând localizarea fișierelor sau folderelor specifice.
- **Continuare Redare** — dacă este activat în setările aplicației, restaurează coada playerului audio și ultima poziție media pentru folderul curent. O modalitate practică de a relua de unde ați rămas.
- **Redare Toate** — scanează folderul curent și subfolderele sale, apoi adaugă toate fișierele audio găsite la o nouă coadă a playerului. Util când doriți să redați fiecare piesă dintr-un director.
- **Amestecare Toate** — ca Redare Toate, dar amestecă fișierele înainte de a le adăuga la coada playerului audio. Excelent pentru redescoperirea unui folder vechi de muzică.

## Opțiuni Folder

Când deschideți un folder, veți găsi un set practic de acțiuni disponibile atingând butonul **„..."** din colțul din dreapta sus.

- **Selectați** — activați modul de selectare a fișierelor. Aceasta vă permite să alegeți unul sau mai multe fișiere din folder și să efectuați acțiuni asupra întregii selecții.
- **Folder Nou** — creați un folder nou în folderul curent. Excelent pentru a vă menține biblioteca bine structurată.
- **Activare modul offline** — activați modul offline pentru folderul curent. Modul offline depășește descărcarea simplă: monitorizează activ folderul pentru modificări. Dacă adăugați fișiere noi online, acestea vor apărea automat pe dispozitivul dvs.
- **Încărcare Fișiere** — încărcați fișiere de pe dispozitivul dvs. în folderul online. Aceasta le face accesibile de oriunde prin același serviciu cloud.
- **Căutare** — căutați fișiere specifice în folderul curent.
- **Sortare** — sortați fișierele după nume, dimensiune, dată modificare sau după metadate. Modul de sortare implicit reflectă ordinea de sortare de pe server, dar o puteți schimba conform preferințelor dvs.
- **Grilă / Vizualizare Listă** — comutați între vizualizarea tabel și vizualizarea miniatură. Vizualizarea tabel arată o listă compactă; vizualizarea miniatură arată previzualizări mari ale copertelor pentru identificare vizuală rapidă.

## Editare Fișiere Online

Când trebuie să gestionați mai multe fișiere în stocarea dvs. cloud, utilizați **Modul Selecție** pentru a simplifica acțiunile:

- **Activare Mod Selecție** — atingeți butonul **„..."** din colțul din dreapta sus și alegeți **Selectați**.
- **Alegere Fișiere** — apar casete de bifare lângă fiecare fișier și folder. Atingeți pentru a selecta unul sau mai multe elemente.
- **Efectuare Acțiuni** — odată ce ați selectat fișierele sau folderele, veți avea acces la Redare Următoare, Redare Mai Târziu, Adăugare la Biblioteca Muzicală, Adăugare la o Listă de Redare, Copiere, Încărcare, Mutare, Redenumire și Ștergere.

Dacă preferați să tratați stocarea cloud conectată ca numai pentru citire (pentru a preveni ștergerile accidentale), activați Setări → Manager Fișiere → Editare Fișiere Online → Dezactivat pentru a ascunde toate operațiile distructive din interfață.

## Acțiuni Fișier

Atingeți pictograma **„..."** lângă titlul unui fișier pentru a-i dezvălui meniul de acțiuni:

- **Redare Următoare** — inserați fișierul în vârful cozii playerului, astfel încât să redea imediat după piesa curentă.
- **Redare Mai Târziu** — adăugați fișierul la sfârșitul cozii playerului.
- **Adăugare la Biblioteca Muzicală** — încorporați fișierul în biblioteca dvs. muzicală, organizată după artist, album, gen sau compozitor.
- **Adăugare la o Listă de Redare** — adăugați fișierul la o listă de redare existentă sau creați una nouă.
- **Editați etichetele audio** — deschideți editorul de etichete integrat pentru a modifica metadatele. Pentru fișierele online, piesa este temporar descărcată, editată și apoi reîncărcată după confirmare.
- **Adăugare la Preferințe** — adăugați fișierul la lista dvs. de preferințe pentru acces rapid.
- **Descărcați** — descărcați fișierul sau folderul pe dispozitivul dvs. pentru utilizare offline.
- **Redenumire** — redenumiți fișierul direct pe stocarea la distanță.
- **Mutare** — mutați fișierul într-un folder diferit din stocarea dvs. cloud.
- **Deschidere În** — exportați fișierul în altă aplicație compatibilă. Fișierul este descărcat pe dispozitivul dvs., apoi apare foaia de distribuire a sistemului.
- **Șterge** — eliminați permanent fișierul din stocarea dvs. cloud. **Această acțiune nu poate fi anulată.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Mai Multe Acțiuni pentru un Fișier în Stocarea Cloud Conectată" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Dacă lista de acțiuni depășește spațiul disponibil pe ecran, pur și simplu derulați în jos în meniul de acțiuni pentru a accesa opțiunile suplimentare.

## Acțiuni Folder

Pentru fiecare folder din stocarea dvs. cloud, aveți o varietate largă de acțiuni disponibile atingând pictograma **„..."** lângă titlul folderului. Dacă nu vedeți toate acțiunile, derulați în jos pentru a dezvălui mai multe.

- **Redare Toate** — înlocuiți coada curentă a playerului cu fiecare element din folderul selectat.
- **Redare Următoare** — adăugați întregul folder în vârful cozii playerului.
- **Redare Mai Târziu** — adăugați conținutul folderului la sfârșitul cozii playerului.
- **Adăugare la Biblioteca Muzicală** — încorporați conținutul folderului în biblioteca dvs. muzicală.
- **Adăugare la Listă de Redare** — adăugați întregul folder la o listă de redare. Aveți, de asemenea, opțiunea de a crea una nouă; numele acesteia este completat automat din numele folderului.
- **Adăugare la Preferințe** — adăugați folderul la preferințele dvs. pentru acces rapid.
- **Activare modul offline** — dincolo de o simplă descărcare, aceasta monitorizează continuu folderul pentru fișiere noi și le descarcă automat pe măsură ce apar online.
- **Descărcați** — descărcați toate conținuturile folderului pe dispozitivul dvs. pentru acces offline.
- **Redenumire** — redenumiți folderul direct pe stocarea la distanță.
- **Mutare** — mutați folderul într-o locație diferită din stocarea dvs. cloud.
- **Arhivă (ZIP)** — grupați conținuturile folderului într-un singur fișier ZIP (funcționalitate Premium).
- **Șterge** — eliminați permanent folderul și conținuturile sale din stocarea dvs. cloud. **Această acțiune nu poate fi anulată.**

## Acces Rapid

Secțiunea Acces Rapid este localizată în partea de sus a ecranului. Vă oferă acces rapid la fișierele dvs. preferate și recent deschise din serviciile cloud conectate. De fiecare dată când deschideți un fișier sau un folder din cloud, acesta este adăugat la lista Deschis Recent. Pentru a șterge această listă, deschideți Recente, atingeți butonul Mai Multe Acțiuni și alegeți Ștergere Listă. Puteți, de asemenea, marca folderele imbricate adânc ca Preferințe pentru a le accesa rapid fără a parcurge structura de directoare.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Linkuri Online și Acces Rapid" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Alte Servicii

Această secțiune afișează funcționalități suplimentare care vă îmbunătățesc experiența. În prezent, aplicația acceptă scrobbling-ul **Last.fm** — când este conectat, statisticile dvs. de redare sunt trimise automat contului dvs. Last.fm. Puteți ulterior vizita profilul dvs. Last.fm pentru a vedea analizele de ascultare și a obține recomandări muzicale personalizate. Instrucțiuni detaliate de configurare sunt disponibile [aici](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Conectare Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
