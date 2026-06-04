---
title: "Conexiuni"
date: 2020-02-01
description: "Aflați cum să conectați stocarea în cloud, NAS și computerul la Evertag. Accesați și editați fișiere audio direct din stocarea în cloud, NAS personal sau Mac/PC."
keywords: [
  "configurare cloud Evertag", "conectare iCloud la Evertag", "acces fișiere SMB iOS",
  "editor etichete audio WebDAV", "editare metadate NAS", "Wi-Fi Drive Evertag",
  "transfer fișiere audio pe iPhone", "Evertag iTunes File Sharing", "editare etichete FLAC din cloud"
]
tags: ["ghid", "evertag", "conexiuni"]
readingTime: 11
---


Pe acest ecran, puteți conecta diverse surse care conțin fișierele dvs. audio. Puteți integra servicii cloud populare precum Google Drive, Dropbox, OneDrive, iCloud și altele, precum și conecta Mac-ul sau PC-ul dvs. În plus, aveți opțiunea de a edita fișiere audio localizate în Apple Time Capsule, WD Cloud Home sau orice NAS care utilizează SMB sau WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Connections Screen" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Acces rapid

În partea de sus a ecranului Conexiuni veți găsi o listă de **Acces rapid**. Orice folder cloud pe care îl adăugați la preferințe — chiar și unul îngropat la mai multe niveluri adâncime — apare aici, astfel încât să puteți sări la el fără a naviga prin folderele superioare de fiecare dată.

## Conectați la stocarea în cloud

- Deschideți fila 'Conexiuni'  
- Selectați 'Conectați la stocarea în cloud' din meniu  
- Alegeți un serviciu de stocare în cloud din listă  
- Introduceți acreditările dvs. și apăsați 'Finalizat.'

Dacă întâmpinați probleme, verificați conexiunea la internet și login-ul/parola.  
În versiunea Premium a aplicației, puteți adăuga un număr nelimitat de servicii.

## Servicii de stocare în cloud acceptate

În prezent, aplicația acceptă cele mai populare servicii de stocare în cloud: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), precum și orice server SMB sau WebDAV.

## Securitate și confidențialitate

Folosim doar SDK-uri oficiale și conexiuni securizate pentru a interacționa cu serviciile cloud conectate. Login-ul și parola dvs. nu sunt accesibile aplicației. Toate solicitările aplicației către serviciul cloud sunt criptate.

Când introduceți login-ul și parola, aplicația vă arată pagina oficială de autorizare furnizată de furnizorul serviciului cloud, iar întregul proces de autorizare are loc în afara aplicației. Furnizorul serviciului cloud trimite un token de autentificare aplicației după autorizarea reușită, iar acel token este folosit pentru apeluri API.

Un token de autentificare este o cheie digitală care permite aplicațiilor terțe să interacționeze cu stocarea în cloud. Token-ul de autentificare este stocat pe dispozitivul dvs. într-un sistem securizat de stocare numit Keychain. Puteți descărca fișierele de la serviciul cloud conectat pe dispozitiv, iar aceste fișiere vor fi plasate în directorul 'Documente' al aplicației. Puteți elimina acele fișiere oricând folosind managerul de fișiere integrat.

Aplicația nu partajează nicio informație din contul cloud conectat. Puteți revoca accesul la contul dvs. cloud oricând deschizând pagina de setări a contului în browserul web.

## Revocare token de autentificare

Conectați-vă la contul dvs. într-un browser web și navigați la pagina de setări. Acolo puteți găsi toate aplicațiile terțe conectate la contul dvs. cloud și le puteți elimina pe oricare dacă nu mai doriți să utilizați acea aplicație. Instrucțiuni detaliate sunt disponibile [aici](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Puteți, de asemenea, deconecta conturile cloud conectate în aplicație, iar token-ul de autentificare va fi, de asemenea, eliminat de pe dispozitivul dvs. Dacă eliminați aplicația de pe dispozitiv, toate datele descărcate și token-urile de acces vor fi, de asemenea, eliminate.

## Deconectați un serviciu cloud sau modificați configurația

- Accesați Opțiunile de Stocare în Cloud: mai întâi, localizați stocarea în cloud pe care doriți să o gestionați în interfața aplicației.  
- Apăsați Butonul '...': lângă titlul serviciului, veți vedea un buton '...'. Apăsați pe el pentru a accesa opțiuni suplimentare.  
  - **Redenumire**: dacă doriți să schimbați numele serviciului cloud așa cum apare în lista dvs., selectați 'Redenumire.'  
  - **Setări**: pentru a modifica configurația sau datele de autentificare pentru serviciul cloud, alegeți 'Setări.' Uneori, poate fi necesară reautorizarea serviciului cloud conectat dacă token-ul de autorizare a expirat.  
  - **Deconectare**: dacă doriți să întrerupeți complet conexiunea dintre aplicație și serviciul cloud, selectați 'Deconectare.' Rețineți că alegerea acestei opțiuni va elimina toate melodiile asociate cu acest serviciu cloud din biblioteca muzicală a aplicației, dar vor rămâne pe server.

## Conectare la Computer sau NAS

Puteți, de asemenea, conecta computerul, NAS-ul personal sau alte dispozitive de rețea folosind protocolul SMB, DLNA sau WebDAV.

## Conectare la computer folosind SMB

- Apăsați "Conectați la stocarea în cloud" → SMB.  
- Introduceți adresa IP a computerului și numele folderului partajat în câmpul URL folosind formatul smb://adresa-ip-computer/nume-folder-partajat  
- Alegeți versiunea protocolului: Auto, SMB1, SMB2  
- Introduceți login și parolă (dacă este necesar)  
- Apăsați "Finalizat."

Dacă conexiunea dvs. este reușită, veți vedea stocarea conectată în secțiunea "Stocare în cloud."  
Un tutorial complet despre cum să conectați Mac-ul sau PC-ul folosind SMB este disponibil [aici](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Conectare la NAS folosind WebDAV

Toți pașii sunt aceiași, cu excepția câmpului URL.  
URL-ul trebuie să fie în formatul http://nume-server sau https://nume-server dacă serverul acceptă SSL.  
Un tutorial complet despre cum să conectați NAS folosind protocolul WebDAV este disponibil [aici](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Dispozitive disponibile

Această secțiune afișează toate dispozitivele din rețeaua dvs. locală la care vă puteți conecta prin aplicație.  
Pentru a stabili o conexiune cu un dispozitiv, urmați acești pași:

- Deschideți aplicația și mergeți la secțiunea "Dispozitive disponibile."  
- Apăsați dispozitivul la care doriți să vă conectați din listă.  
- Dacă este necesar, introduceți datele dvs. de autentificare pentru a finaliza conexiunea.

## Wi-Fi Drive

Wi-Fi Drive este o tehnologie convenabilă care permite transferuri de fișiere fără fir de pe computer pe dispozitivul dvs. iOS printr-un browser de pe desktop.  
Pentru a utiliza această funcție eficient, asigurați-vă că dispozitivul și computerul dvs. sunt conectate la aceeași rețea Wi-Fi.  
Iată un ghid pas cu pas despre cum să utilizați Wi-Fi Drive.

## Activare Wi-Fi Drive

- Deschideți aplicația și mergeți la fila "Conexiuni."  
- Selectați "Conectare prin Wi-Fi" pentru a accesa ecranul principal al Wi-Fi Drive.  
- Apăsați "Pornire Wi-Fi Drive" pentru a activa Wi-Fi Drive.

## Accesați Wi-Fi Drive pe Computer

- Pe computerul dvs. (desktop sau laptop), deschideți un browser web (cum ar fi Chrome, Firefox sau Safari).  
- În bara de adrese a browserului, introduceți URL-ul furnizat de aplicație.

## Transferați Fișiere Fără Fir

Odată ce pagina web corespunzătoare dispozitivului dvs. iOS se deschide în browser, puteți trage și plasa ușor fișiere de pe computer pe pagina web.  
Fișierele pe care le trageți și plasați vor începe să se transfere pe dispozitivul dvs. iOS și vor fi accesibile în cadrul aplicației.

Instrucțiuni detaliate despre cum să transferați fișiere fără fir folosind Wi-Fi Drive sunt disponibile [aici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing este o altă tehnologie care vă permite să transferați fișiere de pe un computer pe un dispozitiv folosind aplicația Finder pe Mac și un cablu Lightning.  
- Conectați pur și simplu dispozitivul la computer folosind un cablu și rulați aplicația Finder pe Mac.  
- Deschideți "Locații" → "Dispozitivul Dvs. Conectat" → "Fișiere" → și găsiți aplicația curentă.  
- Apăsați pe pictograma aplicației pentru a vedea toate folderele partajate.  
- Copiați fișierele de pe computer în folderul partajat de pe dispozitiv folosind glisare și plasare.

Instrucțiuni detaliate despre cum să utilizați iTunes File Sharing sunt disponibile [aici](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Conectați o memorie USB

Dacă aveți un card SD sau un stick USB, îl puteți conecta folosind un cititor de carduri Lightning sau USB-C pe iPhone/iPad sau îl puteți conecta direct la un Mac. Aplicația acceptă în prezent cititoare de carduri certificate de Apple. Avem instrucțiuni detaliate despre cum să conectați o memorie USB la iPhone sau iPad și să gestionați fișierele de pe aceasta, disponibile [aici](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Unitățile conectate apar în secțiunea **Accesorii conectate** a ecranului Conexiuni.

## Manager de Fișiere

Odată ce ați conectat un serviciu de stocare în cloud, apăsați pictograma sa pentru a vedea toate fișierele și folderele disponibile. Puteți folosi managerul de fișiere integrat pentru a lucra cu aceste fișiere — descărcare, redenumire, mutare și altele. Când porniți o descărcare, fișierul va apărea în coada de transferuri. Pentru a vedea coada de transferuri, mergeți la fila "Fișiere locale" și apăsați săgețile care se rotesc din colțul din stânga sus. Toate fișierele și folderele descărcate sunt disponibile în secțiunea "Fișiere locale."

## Bara de Instrumente Superioară

Bara de instrumente superioară, convenabil situată sub bara de navigare, oferă mai multe acțiuni utile ușor de accesat. Puteți arăta sau ascunde această bară printr-un simplu gest de glisare în jos. Iată acțiunile disponibile:

- **Căutare**: această opțiune vă permite să efectuați o căutare rapidă în directorul curent, facilitând localizarea fișierelor sau folderelor specifice.  

## Opțiuni Folder

Când deschideți un folder în aplicație, veți găsi un set de acțiuni disponibile apăsând butonul "..." din colțul din dreapta sus al ecranului.  
Iată o prezentare a acestor acțiuni:

- **Selectați**: activați modul de selectare a fișierelor. Acest mod vă permite să alegeți unul sau mai multe fișiere din folder, facilitând efectuarea de acțiuni asupra elementelor selectate.  
- **Folder Nou**: creați un folder nou în folderul curent. Această funcție vă permite să organizați fișierele și să mențineți biblioteca bine structurată.   
- **Încărcați Fișiere**: încărcați fișiere de pe dispozitivul dvs. în folderul online. Această acțiune vă permite să transferați fișiere în cloud sau server, făcându-le accesibile de oriunde.  
- **Căutare**: căutați fișiere specifice în folderul curent. Aceasta este deosebit de utilă pentru localizarea rapidă a elementelor specifice dintr-o colecție mare.  
- **Sortare**: sortați fișierele din folder după criterii precum nume, dimensiune sau data editării. Modul de sortare implicit reflectă de obicei ordinea de sortare de pe server, dar o puteți schimba după preferințele dvs.  
- **Vizualizare Grilă/Listă**: comutați între două moduri de vizualizare: vizualizare tabel și vizualizare miniaturi. Vizualizarea tabel prezintă fișierele într-o listă, în timp ce vizualizarea miniaturi afișează reprezentări vizuale ale fișierelor, facilitând identificarea conținutului.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloud Folder Sort" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Editați Fișiere Online

Când trebuie să gestionați mai multe fișiere din stocarea dvs. cloud în această aplicație, puteți folosi modul de selectare pentru a vă simplifica acțiunile. Urmați acești pași pentru o gestionare eficientă a fișierelor:

- **Activare Mod Selectare**: deschideți aplicația pe dispozitivul dvs. și navigați la secțiunea care conține stocarea în cloud. Căutați colțul din dreapta sus unde veți găsi butonul "..." (puncte de suspensie). Apăsați pe el și alegeți elementul de meniu "Selectați" pentru a activa modul de selectare.  
- **Alegeți Fișiere**: veți observa casete de selectare apărând lângă fiecare fișier sau folder listat. Alegeți unul sau mai multe fișiere sau foldere atingând pur și simplu casetele de selectare de lângă ele.  
- **Efectuați Diverse Acțiuni**: odată ce ați selectat fișierele sau folderele pe care doriți să le gestionați, veți avea acces la mai multe acțiuni adaptate nevoilor dvs.:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Select" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Acțiuni fișier

Lângă titlul fișierului, veți observa un simbol elipsă "..." (trei puncte) — acesta servește ca meniu de acțiuni.  
Apăsați pe el pentru a dezvălui o listă de acțiuni disponibile:

- **Editați etichetele audio**: selectând această opțiune, puteți accesa editorul de etichete integrat, permițându-vă să modificați etichetele audio ale fișierului ales. Fișierul va fi descărcat temporar într-un director temporar și apoi încărcat în stocare după ce confirmați modificările.  
- **Adăugare la Preferințe**: această acțiune adaugă fișierul în lista dvs. de fișiere preferate pentru acces rapid și convenabil.  
- **Descărcați**: alegeți această acțiune pentru a descărca fișierul sau folderul pe dispozitivul dvs., făcându-l accesibil pentru utilizare offline.  
- **Redenumire**: această opțiune vă permite să redenumiți fișierul direct pe stocarea de la distanță, permițând denumirea personalizată a fișierelor.  
- **Mutare**: optați pentru această acțiune pentru a muta fișierul într-un alt folder din stocarea dvs. cloud, ajutând la menținerea unei structuri organizate de fișiere.  
- **Deschidere în**: folosiți această acțiune pentru a exporta fișierul într-o altă aplicație compatibilă. Fișierul va fi descărcat pe dispozitivul dvs. și apoi va apărea dialogul Partajare.  
- **Șterge**: fiți precauți cu această acțiune, deoarece elimină permanent fișierul din stocarea dvs. cloud. **Această ștergere nu poate fi anulată**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Options" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Dacă lista de acțiuni depășește spațiul disponibil pe ecran, derulați pur și simplu în jos în meniul de acțiuni pentru a accesa opțiuni suplimentare.

## Acțiuni folder

Pentru fiecare folder din stocarea dvs. cloud, aveți diverse acțiuni disponibile. Pentru a accesa aceste opțiuni, apăsați pur și simplu pictograma elipsă "..." situată lângă titlul folderului. Dacă nu vedeți toate acțiunile, derulați în jos pentru a dezvălui mai multe opțiuni. Iată acțiunile disponibile:

- **Adăugare la Preferințe**: folosiți această acțiune pentru a adăuga folderul în lista dvs. de fișiere preferate pentru acces rapid și convenabil.  
- **Descărcați**: descărcați tot conținutul folderului pe dispozitivul dvs. pentru acces offline.  
- **Redenumire**: redenumiți folderul direct pe stocarea de la distanță.  
- **Mutare**: mutați folderul într-o altă locație din stocarea dvs. cloud.  
- **Șterge**: fiți precauți cu această acțiune, deoarece elimină permanent folderul și conținutul său din stocarea dvs. cloud. **Această acțiune nu poate fi anulată**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Folder Options" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
