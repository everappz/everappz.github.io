---
title: "Conexiuni"
date: 2020-01-01
description: "Aflați cum să conectați servicii cloud, computere, dispozitive NAS și să vă gestionați fișierele muzicale folosind Evermusic. Ghid pas cu pas pentru Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing și multe altele."
keywords: [
  "Evermusic", "player muzică cloud", "streaming NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "conectare stocare cloud", "transfer muzică iPhone", "manager fișiere iOS"
]
tags: ["evermusic", "ghid", "conexiuni"]
readingTime: 11
---


Pe ecranul Conexiuni puteți conecta orice sursă care vă stochează muzica — servicii populare în cloud, servere media auto-găzduite, Mac-ul sau PC-ul dvs., un NAS personal, Apple Time Capsule, WD My Cloud Home, chiar și o unitate flash USB — și le puteți folosi pe toate dintr-o interfață unificată. Conexiuni este, de asemenea, locul unde configurați Accesul Rapid la folderele cloud profund imbricate și unde autentificați Last.fm pentru scrobbling.

Ecranul este împărțit în secțiuni clar etichetate, astfel încât scalează de la un singur cont iCloud Drive la o bibliotecă distribuită pe mai multe cloud-uri și dispozitive NAS: Acces Rapid în partea de sus (folderele dvs. cloud preferate), Stocare cloud (conturile pe care le-ați adăugat), Rețea locală (dispozitive descoperite prin Bonjour), Calculator (Wi-Fi Drive, iTunes File Sharing, SMB), Accesorii externe (unități flash USB conectate) și Alte servicii (Last.fm și altele similare).

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecranul Conexiuni Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Conectare la stocarea cloud

- Deschideți fila Conexiuni.
- Selectați Conectare la stocarea cloud din meniu.
- Alegeți un serviciu de stocare cloud din listă.
- Conectați-vă pe pagina oficială de autorizare a furnizorului (Evermusic nu vede niciodată parola dvs.).
- Atingeți Finalizat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Selectorul furnizorului de stocare cloud" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Dacă întâmpinați probleme, verificați din nou conexiunea la internet și datele de autentificare și asigurați-vă că autentificarea cu doi factori este configurată corect pentru acel serviciu.  
În versiunea Premium a aplicației puteți adăuga un număr nelimitat de servicii. Utilizatorii gratuiți pot conecta un singur cont cloud la un moment dat.

## Servicii de stocare cloud acceptate

Evermusic suportă gama completă de servicii cloud populare și auto-găzduite. Utilizatorii gratuiți au același catalog de furnizori, dar cu limita de un singur cont; Premium deblochează conturi nelimitate și elimină majoritatea celorlalte limite.

- **Conturi cloud personale:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servere auto-găzduite și biblioteci media:** Plex · Jellyfin · Emby · Subsonic (și orice server compatibil Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (și Owncloud, via API-ul comun) · Synology Drive · QNAP.
- **Protocoale NAS și partajare fișiere:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (autentificare prin parolă sau cheie publică), NFS și DLNA (doar citire — redare și descărcare).
- **Stocare de obiecte compatibilă S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage sau orice endpoint S3-API.
- **Descoperire în rețeaua locală:** secțiunea Dispozitive disponibile listează automat toate dispozitivele din rețeaua dvs. Wi-Fi care se anunță via Bonjour / mDNS — servere Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, routere AirPort cu unități atașate și așa mai departe.

## Securitate și confidențialitate

Folosim doar SDK oficial și conexiuni securizate pentru a interacționa cu serviciile cloud conectate. Login-ul și parola dvs. nu sunt disponibile pentru aplicație. Toate cererile din aplicație către serviciul cloud sunt criptate.

Când introduceți login-ul și parola, aplicația vă arată pagina oficială de autorizare furnizată de furnizorul serviciului cloud și tot procesul de autorizare se face în afara aplicației. Furnizorul serviciului cloud trimite un token de autentificare către aplicație după autorizarea reușită și acel token este utilizat pentru a face apeluri API.

Token-ul de autentificare este o cheie digitală care permite aplicațiilor terțe să interacționeze cu stocarea cloud. Token-ul de autentificare este stocat pe dispozitivul dvs. într-un sistem de stocare securizat numit Keychain. Puteți descărca fișierele din serviciul cloud conectat pe dispozitiv și acele fișiere vor fi plasate în directorul "Documente" al aplicației. Puteți elimina aceste fișiere oricând folosind managerul de fișiere integrat.

Aplicația nu partajează nicio informație din contul cloud conectat. Puteți revoca accesul la contul dvs. cloud oricând deschizând pagina de setări a contului în browserul web.

## Respingerea token-ului de autentificare

Conectați-vă la contul dvs. în browserul web și navigați la pagina de setări. Acolo puteți găsi toate aplicațiile terțe conectate la contul dvs. cloud și puteți elimina oricare dintre ele dacă nu mai doriți să utilizați acea aplicație. Instrucțiuni detaliate disponibile [aici](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

De asemenea, puteți deconecta conturile cloud conectate în aplicație și token-ul de autentificare va fi și el eliminat de pe dispozitivul dvs. Dacă eliminați aplicația de pe dispozitiv, toate datele descărcate și token-urile de acces vor fi de asemenea eliminate.

## Deconectarea unui spațiu de stocare cloud sau schimbarea configurației

- Accesați Opțiunile de Stocare Cloud: mai întâi, localizați stocarea cloud pe care doriți să o gestionați în interfața aplicației.
- Atingeți butonul '...': lângă titlul serviciului, veți vedea un buton '...'. Atingeți-l pentru a accesa opțiuni suplimentare.
  - **Redenumire**: dacă doriți să schimbați numele serviciului cloud așa cum apare în lista dvs., selectați 'Redenumire'.
  - **Setări**: pentru a modifica configurația sau datele de autentificare pentru serviciul cloud, alegeți 'Setări'. Uneori, poate fi necesar să reautorizați serviciul cloud conectat dacă token-ul de autorizare a expirat.
  - **Deconectare**: dacă doriți să întrerupeți complet conexiunea dintre aplicație și serviciul cloud, selectați 'Deconectare'. Rețineți că alegerea acestei opțiuni va elimina toate melodiile asociate acestui serviciu cloud din biblioteca de muzică a aplicației, dar vor rămâne pe server.

{{< cards cols="1">}}
  {{< card title="" subtitle="Meniu Mai multe acțiuni pentru stocarea cloud conectată" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Conectare la Calculator sau NAS

De asemenea, puteți conecta computerul, NAS-ul personal sau alte dispozitive de rețea folosind protocolul SMB, DLNA sau WebDAV.

## Conectare la calculator prin SMB

- Atingeți "Conectare la stocarea cloud" → SMB.
- Introduceți adresa IP a calculatorului și numele folderului partajat în câmpul URL folosind formatul smb://adresa-ip-calculator/numele-folderului-partajat
- Alegeți versiunea protocolului: Auto, SMB1, SMB2
- Introduceți login-ul și parola (dacă este necesar)
- Atingeți "Finalizat".

Dacă conexiunea este reușită, veți vedea stocarea conectată în secțiunea "Stocare cloud".  
Un tutorial complet despre cum să conectați Mac-ul sau PC-ul dvs. folosind SMB este disponibil [aici](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Setările Conexiunii SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Conectare la NAS prin WebDAV

Toți pașii sunt la fel, cu excepția câmpului URL.  
URL-ul trebuie să fie în formatul http://numele-serverului, sau https://numele-serverului dacă serverul acceptă SSL.
Un tutorial complet despre cum să conectați stocarea NAS folosind protocolul WebDAV este disponibil [aici](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Setările Conexiunii WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Conectare la Calculator sau NAS prin DLNA

De asemenea, puteți partaja o bibliotecă de muzică situată pe PC-ul dvs. Windows sau NAS-ul personal folosind protocolul DLNA și accesa acea bibliotecă în aplicație conform descrierii [aici](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA este un protocol popular și larg utilizat, dar vă permite doar să redați sau să descărcați muzică. Nu puteți încărca fișiere sau crea foldere noi pe server.

{{< cards cols="1">}}
  {{< card title="" subtitle="Setările Conexiunii DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Dispozitive disponibile

Această secțiune afișează toate dispozitivele din rețeaua locală la care vă puteți conecta prin intermediul aplicației.  
Pentru a stabili o conexiune cu un dispozitiv, urmați acești pași:

- Deschideți aplicația și mergeți la secțiunea "Dispozitive Disponibile".
- Atingeți dispozitivul la care doriți să vă conectați din listă.
- Dacă este necesar, introduceți datele de autentificare pentru a finaliza conexiunea.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dispozitive Disponibile în Rețeaua Locală" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive este o tehnologie convenabilă care permite transferuri de fișiere fără fir de pe computer pe dispozitivul dvs. iOS printr-un browser de pe computer.  
Pentru a utiliza eficient această funcție, asigurați-vă că dispozitivul și computerul dvs. sunt conectate la aceeași rețea Wi-Fi.  
Iată un ghid pas cu pas despre cum să utilizați Wi-Fi Drive.

## Activare Wi-Fi Drive

- Deschideți aplicația și mergeți la fila "Conexiuni".
- Selectați "Conectare prin Wi-Fi" pentru a accesa ecranul principal Wi-Fi Drive.
- Atingeți "Pornire Wi-Fi Drive" pentru a activa Wi-Fi Drive.

## Accesarea Wi-Fi Drive pe Calculatorul dvs.

- Pe calculatorul dvs. (desktop sau laptop), deschideți un browser web (cum ar fi Chrome, Firefox sau Safari).
- În bara de adrese a browserului, introduceți URL-ul furnizat de aplicație.

## Transferul Fișierelor Fără Fir

Odată ce pagina web corespunzătoare dispozitivului dvs. iOS se deschide în browser, puteți trage și plasa ușor fișierele de pe computer pe pagina web.  
Fișierele pe care le trageți și le plasați vor începe să se transfere pe dispozitivul dvs. iOS și vor fi accesibile în cadrul aplicației.

{{< cards cols="1">}}
  {{< card title="" subtitle="Setările Serverului Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Instrucțiuni detaliate despre cum să transferați fișiere fără fir folosind WiFi-Drive sunt disponibile [aici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing este o altă tehnologie care vă permite să transferați fișiere de pe computer pe dispozitiv folosind aplicația Finder pe Mac și cablul lightning.  
- Conectați pur și simplu un dispozitiv la calculator folosind un cablu și rulați aplicația Finder pe Mac.
- Deschideți "Locații" → "Dispozitivul Dvs. Conectat" → "Fișiere" → și găsiți aplicația Evermusic.
- Atingeți pictograma aplicației pentru a vedea toate folderele partajate.
- Copiați fișierele de pe calculator în folderul partajat de pe dispozitiv folosind tragere și plasare.

Instrucțiuni detaliate despre cum să utilizați iTunes File Sharing sunt disponibile [aici](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing pe Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Conectarea unui card flash USB

Dacă aveți un card SD, îl puteți conecta folosind un cititor de carduri lightning. Aplicația suportă în prezent cititoare de carduri certificate Apple și iXpand Flash Drives. Dacă aveți un iXpand Flash Drive — introduceți-l în portul lightning și deschideți aplicația. Veți vedea un mesaj 'Dispozitiv extern conectat' și informații despre dispozitiv. Pur și simplu atingeți pictograma flash drive-ului pentru a accesa folderul de muzică și atingeți orice fișier audio pentru a începe redarea. Avem instrucțiuni detaliate despre cum să conectați un card flash USB la iPhone și să ascultați muzică sau să gestionați fișierele aflate pe el, disponibile [aici](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Manager de Fișiere

După ce ați conectat un serviciu de stocare cloud, atingeți pictograma acestuia pentru a vedea toate fișierele și folderele disponibile. Puteți utiliza managerul de fișiere integrat pentru a lucra cu aceste fișiere — descărcați, redenumiți, mutați și mai mult. Când începeți o descărcare, fișierul va apărea în coada de transfer. Pentru a vizualiza coada de transfer, mergeți la fila "Fișiere Locale" și atingeți săgețile care se rotesc din colțul din stânga sus. Toate fișierele și folderele descărcate sunt disponibile în secțiunea "Fișiere Locale".

## Bara de Instrumente Superioară

Bara de instrumente superioară, amplasată convenabil sub bara de navigare, oferă mai multe acțiuni utile pentru acces ușor. Puteți afișa sau ascunde această bară de instrumente folosind un simplu gest de glisare în jos. Iată acțiunile disponibile:

- **Căutare**: această opțiune vă permite să efectuați o căutare rapidă în directorul curent, facilitând localizarea fișierelor sau folderelor specifice.
- **Continuare Redare**: dacă este activat în setările aplicației, această funcție restaurează coada playerului audio și ultima poziție media pentru folderul curent. Este o modalitate convenabilă de a relua de unde ați rămas în biblioteca dvs. de muzică.
- **Redare Toate**: selectând această acțiune, aplicația va scana folderul curent și subfolderele sale, adăugând toate fișierele audio găsite la o nouă coadă a playerului. Aceasta este utilă când doriți să redați toată muzica dintr-un anumit director.
- **Amestecare Toate**: similar cu "Redare Toate", această acțiune scanează folderul curent și subfolderele sale, dar amestecă fișierele înainte de a le adăuga la coada playerului audio. Este o modalitate excelentă de a vă bucura de muzică într-o ordine aleatorie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Bara de Instrumente Superioară Dintr-un Folder Cloud" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Opțiuni Folder

Când deschideți un folder în aplicație, veți găsi un set util de acțiuni disponibile atingând butonul "..." din colțul din dreapta sus al ecranului.  
Iată o descriere a acestor acțiuni:

- **Selectați**: activați modul de selectare a fișierelor. Acest mod vă permite să alegeți unul sau mai multe fișiere din folder, facilitând efectuarea acțiunilor asupra elementelor selectate.
- **Folder Nou**: creați un folder nou în folderul curent. Această funcție vă permite să vă organizați fișierele și să vă mențineți biblioteca bine structurată.
- **Activare modul offline**: activați modul offline pentru folderul curent. Modul offline depășește simpla descărcare; monitorizează activ folderul pentru modificări. Dacă adăugați fișiere noi în folderul online, aplicația va descărca automat aceste fișiere pe dispozitivul dvs. Aceasta asigură că biblioteca locală rămâne actualizată cu modificările de pe server.
- **Încărcare Fișiere**: încărcați fișiere de pe dispozitiv în folderul online. Această acțiune vă permite să transferați fișiere în cloud sau pe server, făcându-le accesibile de oriunde.
- **Căutare**: căutați fișiere specifice în folderul curent. Aceasta este deosebit de utilă pentru localizarea rapidă a elementelor specifice dintr-o colecție mare.
- **Sortare**: sortați fișierele din folder după criterii cum ar fi numele, dimensiunea sau data editării. Modul de sortare implicit reflectă de obicei ordinea de sortare de pe server, dar puteți schimba aceasta după preferințele dvs.
- **Vizualizare Grilă/Listă**: comutați între două moduri de vizualizare: vizualizare tabel și vizualizare miniaturi. Vizualizarea tabel prezintă fișierele într-o listă, în timp ce vizualizarea miniaturi afișează reprezentări vizuale ale fișierelor, facilitând identificarea conținutului dintr-o privire.

{{< cards cols="1">}}
  {{< card title="" subtitle="Meniu Mai multe acțiuni pentru folderul curent" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Editarea Fișierelor Online

Când trebuie să gestionați mai multe fișiere în stocarea dvs. cloud pe Evermusic, puteți folosi modul de selectare pentru a vă simplifica acțiunile. Urmați acești pași pentru gestionarea eficientă a fișierelor:

- **Activarea Modului de Selectare**: deschideți aplicația pe dispozitivul dvs. și navigați la secțiunea care conține stocarea dvs. cloud. Căutați butonul "..." (puncte de suspensie) din colțul din dreapta sus. Atingeți-l și alegeți elementul de meniu "Selectați" pentru a activa modul de selectare.
- **Alegerea Fișierelor**: veți observa că apar casete de selectare lângă fiecare fișier sau folder listat. Alegeți unul sau mai multe fișiere sau foldere atingând pur și simplu casetele de selectare de lângă ele.
- **Efectuarea Diverselor Acțiuni**: odată ce ați selectat fișierele sau folderele pe care doriți să le gestionați, veți avea acces la mai multe acțiuni adaptate nevoilor dvs.

{{< cards cols="1">}}
  {{< card title="" subtitle="Modul de Selectare pentru Fișierele Online" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Acțiuni pentru fișier

Lângă titlul fișierului, veți observa un simbol de puncte de suspensie "..." (trei puncte) — acesta servește ca meniu de acțiuni.  
Atingeți-l pentru a dezvălui o listă de acțiuni disponibile:

- **Redare Următoare**: optați pentru această acțiune pentru a insera fișierul ales în partea de sus a cozii playerului dvs., asigurând că se redă imediat după elementul care se redă în prezent.
- **Redare Mai Târziu**: selectând această opțiune se adaugă fișierul în partea de jos a cozii playerului dvs., asigurând că se redă după coada existentă.
- **Adăugare în Biblioteca de Muzică**: această acțiune vă permite să incorporați fișierul în biblioteca dvs. de muzică, făcându-l ușor accesibil și ordonat după artist, album, gen sau compozitor.
- **Adăugare la o Listă de Redare**: folosiți această acțiune pentru a adăuga fișierul la o listă de redare existentă sau pentru a crea una nouă.
- **Editați etichetele audio**: selectând această opțiune, puteți accesa editorul de taguri integrat al Evermusic, permițându-vă să modificați tagurile audio pentru fișierul ales. Fișierul va fi temporar descărcat într-un director temporar și apoi încărcat în stocare după ce confirmați modificările.
- **Adăugare la Preferințe**: această acțiune adaugă fișierul la lista dvs. de fișiere preferate pentru acces rapid și convenabil.
- **Descărcați**: alegeți această acțiune pentru a descărca fișierul sau folderul pe dispozitivul dvs., făcându-l accesibil pentru utilizare offline.
- **Redenumire**: această opțiune vă permite să redenumiți fișierul direct pe stocarea de la distanță, permițând numirea personalizată a fișierelor.
- **Mutare**: optați pentru această acțiune pentru a reloca fișierul într-un alt folder din stocarea dvs. cloud, ajutând la menținerea unei structuri organizate de fișiere.
- **Deschide În**: folosiți această acțiune pentru a exporta fișierul în altă aplicație compatibilă. Fișierul va fi descărcat pe dispozitivul dvs. și apoi va apărea dialogul de Partajare.
- **Șterge**: fiți precaut cu această acțiune, deoarece elimină permanent fișierul din stocarea dvs. cloud. Această ștergere nu poate fi anulată.

{{< cards cols="1">}}
  {{< card title="" subtitle="Meniu Mai multe acțiuni pentru un singur fișier" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Dacă lista de acțiuni depășește spațiul disponibil pe ecran, defilați pur și simplu în jos în meniul de acțiuni pentru a accesa opțiuni suplimentare.

## Acțiuni pentru folder

Pentru fiecare folder din stocarea dvs. cloud, aveți diverse acțiuni disponibile. Pentru a accesa aceste opțiuni, atingeți pur și simplu pictograma punctelor de suspensie "..." situată lângă titlul folderului. Dacă nu vedeți toate acțiunile, defilați în jos pentru a dezvălui mai multe opțiuni. Iată acțiunile disponibile:

- **Redare Toate**: înlocuiți coada curentă a playerului cu toate elementele din folderul selectat.
- **Redare Următoare**: adăugați întregul folder în partea de sus a cozii playerului, imediat după elementul care se redă în prezent.
- **Redare Mai Târziu**: adăugați conținutul folderului în partea de jos a cozii playerului.
- **Adăugare în Biblioteca de Muzică**: această acțiune integrează perfect conținutul folderului în biblioteca dvs. de muzică, făcându-l ușor accesibil și organizat după artist, album, gen sau compozitor.
- **Adăugare la Listă de Redare**: puteți include întregul folder într-o listă de redare. Aveți și opțiunea de a crea o nouă listă de redare, iar numele folderului va fi atribuit automat.
- **Adăugare la Preferințe**: folosiți această acțiune pentru a adăuga folderul la lista dvs. de fișiere preferate pentru acces rapid și convenabil.
- **Activare modul offline**: activând modul offline pentru un folder selectat, aplicația depășește simpla descărcare. Scanează continuu modificările și, dacă fișiere noi sunt adăugate în folderul online, vor fi descărcate automat în aplicație.
- **Descărcați**: descărcați tot conținutul folderului pe dispozitivul dvs. pentru acces offline.
- **Redenumire**: redenumiți folderul direct pe stocarea de la distanță.
- **Mutare**: relocați folderul într-o altă locație din stocarea dvs. cloud.
- **Șterge**: fiți precaut cu această acțiune deoarece elimină permanent folderul și conținutul său din stocarea dvs. cloud. Această acțiune nu poate fi anulată.


## Acces Rapid

Secțiunea Acces Rapid este situată în partea de sus a ecranului. Vă oferă acces rapid la fișierele dvs. preferate și deschise recent din serviciile cloud conectate.
Ori de câte ori deschideți un fișier sau folder din cloud, acesta este adăugat la lista "Deschise Recent". Pentru a șterge această listă, deschideți "Recente", atingeți butonul "Mai Multe Acțiuni" și alegeți "Ștergere Listă". De asemenea, puteți marca folderele profund imbricate ca Preferințe pentru a le accesa rapid fără a căuta prin structura de directoare.

## Alte Servicii

Această secțiune afișează funcții suplimentare care vă îmbunătățesc experiența. În prezent, aplicația suportă scrobbling-ul Last.fm. Când este conectat, statisticile dvs. de redare sunt trimise automat la contul dvs. Last.fm. Puteți vizita profilul Last.fm mai târziu pentru a vizualiza analizele de ascultare și a obține recomandări muzicale personalizate. Instrucțiuni detaliate de configurare sunt disponibile [aici](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
