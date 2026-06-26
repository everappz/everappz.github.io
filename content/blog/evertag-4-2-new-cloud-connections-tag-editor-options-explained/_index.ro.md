---
title: "Evertag 4.2: noi conexiuni cloud, setările editorului de etichete explicate"
date: 2026-05-09
description: "Evertag 4.2 adaugă conexiuni la Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP și NFS, reîmprospătează Wi-Fi Drive și actualizează interfața pentru Liquid Glass. Această postare explică, de asemenea, fiecare setare a editorului de etichete — incluzând ID3v2.4 vs ID3v2.3, scalarea coperții albumului, duplicarea etichetelor, modurile de încărcare în cloud și opțiunile potrivite pentru Spotify și alte servicii de streaming."
keywords: ["Evertag 4.2", "actualizare Evertag", "editor etichete ID3 iPhone", "ID3v2.4 vs ID3v2.3", "editare etichete FLAC iOS", "editare etichete MP3 iPhone", "editare copertă album iOS", "editor etichete pentru Spotify", "editor etichete Plex", "editor etichete Apple Music", "Evertag editor etichete cloud", "editor etichete Internxt", "editor etichete Proton Drive", "editor etichete QNAP", "editor etichete Nextcloud", "editor etichete Amazon S3", "editor etichete SFTP iPhone", "editor etichete audio FTP", "editor etichete NFS iPhone", "Wi-Fi Drive editor etichete", "duplicare etichete ID3", "scalare copertă", "design Liquid Glass", "editor metadate audio iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Editor etichete", "ID3", "ID3v2.4", "ID3v2.3", "Etichete FLAC", "Etichete MP3", "Copertă album", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Ce este nou"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**Pe scurt:** [Evertag 4.2](/products/evertag) este o actualizare majoră pentru editorul de etichete audio pe iPhone, iPad și Mac. Am rezolvat erorile cheie de editare a etichetelor și am adăugat peste 6 conexiuni noi de cloud și server — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** plus protocoalele **FTP**, **SFTP** și **NFS**. Wi-Fi Drive a primit o interfață reîmprospătată, mod de selecție multiplă, o coadă de încărcare mai inteligentă și transferuri mai rapide. Întreaga aplicație este reglată pentru designul **Liquid Glass**. Această postare aprofundează, de asemenea, setările editorului de etichete Evertag — explicând **ID3v2.4 vs ID3v2.3**, **scalarea coperții albumului**, **duplicarea etichetelor**, **modurile de încărcare în cloud**, **ștergerea fișierului descărcat** și exact ce opțiuni să alegi dacă pregătești audio pentru **Spotify**, **Apple Music**, **Plex**, **Jellyfin** sau orice alt serviciu de streaming.

---

## Salutare tuturor!

A sosit o actualizare mare a Evertag. Am rezolvat erori cheie de editare a etichetelor și am adăugat **peste 6 conexiuni noi de cloud și server** pentru a face gestionarea metadatelor audio mai ușoară ca niciodată — fie că biblioteca ta locuiește într-un cloud orientat spre confidențialitate, pe un NAS auto-găzduit sau pe un server FTP/SFTP/NFS generic.

[Descarcă Evertag 4.2 din App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) sau actualizează din versiunea ta actuală.

## Suport extins pentru cloud și server

Evertag se conectează acum nativ la o gamă mai largă de opțiuni de cloud și stocare auto-găzduită. Poți edita etichetele ID3, MP4, FLAC, OGG și APE pe fișiere oriunde s-ar afla.

### Stocare cloud orientată spre confidențialitate: Internxt și Proton Drive

Dacă îți pasă de criptarea end-to-end și stocarea zero-knowledge, două dintre cele mai respectate nume din zona cloud-urilor orientate spre confidențialitate sunt acum native în Evertag:

- **Internxt** — cloud spaniol open-source, criptat post-cuantic și conform GDPR. Plan gratuit disponibil.
- **Proton Drive** — stocare criptată end-to-end de la creatorii Proton Mail și Proton VPN, cu sediul în Elveția. Plan gratuit disponibil, planuri plătite pentru biblioteci mai mari.

Acum poți edita metadatele direct pe fișierele audio stocate în oricare dintre cele două servicii — fișierul rămâne criptat în tranzit, iar doar etichetele noi sunt scrise înapoi.

### Soluții auto-găzduite: QNAP, Nextcloud, Amazon S3

Pentru utilizatorii care își administrează propria infrastructură:

- **QNAP** — conexiune API nativă la dispozitivele QNAP NAS. Editează etichetele pe fișierele de pe QNAP-ul tău prin Wi-Fi local sau acces la distanță.
- **Nextcloud** — conectează-te la orice instanță Nextcloud, găzduită singur sau gestionată.
- **Amazon S3** — îndreaptă Evertag spre orice bucket S3 (sau stocare compatibilă S3 precum Backblaze B2, Wasabi, MinIO, Cloudflare R2) și editează metadatele pe loc.

### Protocoale de rețea noi: FTP, SFTP, NFS

Evertag 4.2 adaugă trei protocoale clasice pentru utilizatori cu servere personalizate, homelaburi sau dispozitive NAS generice:

- **SFTP (SSH File Transfer Protocol)** — răspunsul potrivit pentru **editarea sigură de la distanță a etichetelor de pe propriul server**. SFTP rulează peste SSH, deci întregul transfer (autentificare și date audio) este criptat. Dacă ai un VPS, un server dedicat sau o mașină Linux acasă cu acces SSH, poți edita etichete pe fișiere de la distanță fără a expune nimic altceva. Acceptă autentificare cu parolă și cu cheie.
- **FTP** — standardul îndelung stabilit pentru transferul de fișiere. Util pentru NAS-urile de acasă mai vechi care expun FTP, dar nu au integrare nativă API.
- **NFS (Network File System)** — protocolul de partajare de facto pe Linux și pe majoritatea dispozitivelor NAS. Suprasarcină mai mică decât SMB pe același hardware.

> **Sfat:** SFTP este protocolul pe care îl vrei pentru editarea de la distanță prin internetul deschis. FTP și NFS sunt cele mai potrivite în rețeaua locală — nu le expune pe internet decât dacă le împachetezi într-un VPN.

## Upgrade-uri Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) este caracteristica integrată Evertag pentru **transferul fișierelor audio fără fir între computer și iPhone-ul sau iPad-ul tău — fără iTunes, fără cabluri, fără cont cloud**. Ambele dispozitive trebuie să fie pe aceeași rețea Wi-Fi.

În Evertag 4.2, Wi-Fi Drive primește:

- **Interfață modernă reîmprospătată** — mai curată, mai ușor de citit dintr-o privire și actualizată pentru Liquid Glass.
- **Mod de selecție multiplă** — alege mai multe fișiere sau foldere și acționează asupra lor în masă.
- **Coadă de încărcare mai inteligentă** — feedback de progres mai bun și rezistență la întreruperile de rețea.
- **Viteză și fiabilitate generală îmbunătățite** — transferuri mai rapide pentru biblioteci mari.

Este cel mai rapid mod de a muta un lot de fișiere audio de pe computer pe telefon, de a le edita etichetele și de a le trimite înapoi — fără niciun serviciu terț.

## Setările editorului de etichete: o imersiune profundă

Aceasta este partea pe care majoritatea utilizatorilor nu o citesc niciodată — și partea care decide dacă etichetele tale funcționează peste tot sau doar în unele aplicații. Deschide Evertag, apoi mergi la secțiunea **setările editorului de etichete audio**. Iată ce face de fapt fiecare opțiune și pe care să o alegi în funcție de ceea ce încerci să obții.

### Scalarea coperții albumului

Când salvezi coperta albumului într-un fișier audio, Evertag poate redimensiona imaginea înainte de a o încorpora. Opțiunile disponibile sunt:

- **Mic** — cel mai mic impact asupra dimensiunii fișierului, calitate mai scăzută a imaginii.
- **Mediu** — alegere echilibrată pentru majoritatea utilizatorilor.
- **Mare** — calitate înaltă, potrivit pentru playere cu ecrane mari și CarPlay.
- **Foarte mare** — calitate foarte înaltă, creștere semnificativă a dimensiunii fișierului.
- **Original (Dezactivat)** — încorporează coperta la rezoluția originală. **Fără scalare.**

**De ce contează:**

- **Calitate mai mare = fișier mai mare.** O copertă de 3.000 × 3.000 pixeli poate adăuga mai mulți MB la fiecare piesă. Înmulțit cu un album întreg, costul de disc se acumulează rapid.
- **Unele playere nu gestionează bine imaginile încorporate foarte mari.** Dispozitivele mai vechi, anumite head unit-uri auto și unele playere desktop legacy se pot bloca pe coperți peste ~1.500 px sau pot refuza să le afișeze.
- **Pentru majoritatea fluxurilor cloud și de streaming**, **Mediu** sau **Mare** este punctul ideal. Folosește **Original** doar atunci când ai nevoie specific de calitate de arhivă sau pregătești fișiere pentru un player în care ai încredere.

> Opțiunea de dimensiune **Original** face parte din upgrade-ul de personalizare premium Evertag. Dimensiunile standard (Mic/Mediu/Mare/Foarte mare) sunt gratuite.

### Opțiuni de salvare a etichetelor: ID3v2.4 vs ID3v2.3

Aceasta este cea mai importantă setare individuală pentru compatibilitate. ID3v2 este formatul de metadate folosit în interiorul fișierelor MP3. Există două versiuni utilizate pe scară largă, iar acestea diferă în detalii subtile, dar importante.

#### ID3v2.4

- Mai nouă, suportă **codificarea text UTF-8** — gestionarea corectă a scrierilor non-latine (chineză, rusă, japoneză, arabă, ebraică etc.).
- Mai multe tipuri de cadre (volum relativ, presetări egalizator etc.).
- **Recomandată pentru playere moderne** care o suportă.

#### ID3v2.3

- Mai veche, dar **versiunea ID3 cu cea mai universală suportare**.
- Nu suportă UTF-8 direct (folosește UTF-16 pentru text Unicode).
- **Recomandată când ai nevoie de compatibilitate maximă** cu playere mai vechi, sisteme audio auto și anumite aplicații desktop.

#### Când să activezi ID3v2.4 în Evertag

- Folosești **playere audio moderne** precum Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (versiuni curente) sau playere Android moderne. ✅ **Pornește ID3v2.4.**
- Biblioteca ta conține **caractere non-latine** (chineză, coreeană, japoneză, rusă, arabă, greacă, ebraică). ✅ **Pornește ID3v2.4** — UTF-8 le gestionează mult mai curat.

#### Când să dezactivezi ID3v2.4 în Evertag (folosește ID3v2.3 în schimb)

- Pregătești fișiere pentru un **sistem audio auto sau unitate de bord mai vechi** care nu citește etichete v2.4.
- Vezi **text deformat sau etichete lipsă** în unele aplicații după editare — acesta este un semnal puternic că v2.4 nu este suportat acolo. Întoarce-te la v2.3.
- Țintești **playere desktop legacy** sau playere portabile mai vechi (iPod-urile timpurii, anumite playere MP3 din anii 2000–2010).

> **Regulă generală:** dacă etichetele tale apar corect peste tot cu v2.4, las-o pornită. Dacă chiar și un singur player important afișează caractere greșite, goluri sau nu citește etichetele, oprește v2.4 și salvează din nou.

#### Duplicarea etichetelor

Când activezi **Duplicarea etichetelor**, Evertag scrie câmpurile comune de metadate (titlu, artist, album etc.) în **ambele secțiuni ID3v1 și ID3v2** ale fișierului. Aceasta îmbunătățește compatibilitatea cu playere foarte vechi care citesc doar ID3v1 (eticheta originală de 128 de octeți de la sfârșitul fișierului).

- **Majoritatea utilizatorilor nu au nevoie de aceasta.** Playerele moderne citesc mai întâi ID3v2.
- **Activează doar dacă** lucrezi cu hardware vintage sau software specific care ignoră ID3v2.

### Actualizarea fișierelor online: cum gestionează Evertag editările cloud

Când editezi etichete pe un fișier stocat pe un cloud conectat (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP etc.), Evertag trebuie să încarce fișierul modificat înapoi. Tu controlezi cum:

- **Afișează mesajul de confirmare** *(implicit, recomandat)* — Evertag întreabă înainte de încărcare. Cel mai bun pentru utilizatorii precauți și bibliotecile partajate.
- **Actualizează automat metadatele fișierului** — încarcă silențios după fiecare editare. Cel mai bun pentru utilizatorii singuri cu conexiuni rapide și fiabile care editează mult.
- **Nu actualiza metadatele fișierului** — Evertag editează doar copia locală. Util pentru a previzualiza modificări fără a le împinge în cloud.

### Editarea fișierelor online: curățarea fișierului local

Pentru a edita un fișier de la distanță, Evertag îl descarcă mai întâi pe dispozitivul tău. După editare, alegi ce se întâmplă cu acea copie locală:

- **Șterge întotdeauna fișierul descărcat** — Evertag elimină fișierul temporar după editare. **Recomandat** dacă ai puțin spațiu de stocare sau lucrezi pe fișierele altcuiva.
- **Nu șterge fișierul descărcat** — păstrează fișierul editat pe dispozitivul tău. Util când vrei atât o copie offline, cât și o copie cloud actualizată.

### Butoanele de pe ecranul principal

Ecranul principal al editorului de etichete Evertag poate afișa sau ascunde butoane pentru operațiuni individuale. Activează doar pe cele pe care le folosești efectiv pentru a păstra interfața concentrată:

- **Caută etichete audio automat** — găsește metadatele lipsă online pe baza amprentei audio a fișierului.
- **Caută etichete audio manual** — caută după titlu/artist când căutarea automată ratează.
- **Caută coperta albumului** — găsește și încorporează coperți de înaltă calitate.
- **Salvează coperta albumului** — exportă coperta încorporată în biblioteca foto sau în fișiere.
- **Normalizează codificarea** — corectează textul non-latin deformat cauzat de codificări vechi (foarte util pentru piese chirilice, chineze și japoneze ripate cu software legacy).
- **Șterge etichetele audio** — elimină toate etichetele dintr-un fișier. Util înaintea unei re-etichetări curate.

### Afișează etichetele extinse

Comută aceasta pentru a afișa setul complet de câmpuri de metadate dincolo de titlul/artistul/albumul/anul de bază — incluzând BPM, dirijor, artist original, dispoziție, copyright, encoder, comentarii, versuri și altele. Funcție pentru utilizatori avansați; majoritatea utilizatorilor casual nu au nevoie.

### Editează fișierele simultan

Când este activată, Evertag îți permite să editezi metadatele pe **mai multe fișiere selectate simultan** — setează același album artist, an sau gen pentru un întreg album într-o singură operație. Acesta este cel mai rapid mod de a curăța o bibliotecă mare neorganizată.

## Editarea etichetelor pentru Spotify, Apple Music și platforme de streaming

O întrebare comună: «am editat etichetele în Evertag, am încărcat fișierele și serviciul de streaming arată metadate greșite. Ce se întâmplă?»

Răspunsul scurt: **serviciile de streaming nu respectă întotdeauna etichetele tale locale.** Apple Music și Spotify au propriile baze de date interne — când recunosc o piesă, suprascriu metadatele afișate cu propriile lor. Dar pentru **fișierele încărcate**, fișierele tale locale (funcția «Bibliotecă» Apple Music, Spotify Local Files) și **încărcările distribuitorilor pe platformele de streaming**, etichetele tale contează absolut. Iată cum să setezi Evertag pentru fiecare scenariu:

### Pregătirea fișierelor pentru Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music gestionează corect UTF-8.
- **Coperta albumului: Mare** — aplicațiile Apple redau bine coperțile mari; Original este excesiv.
- **Duplicarea etichetelor: OFF** — nu este necesar.
- Asigură-te că **Album Artist** este completat corect — Apple Music îl folosește pentru grupare.

### Pregătirea fișierelor pentru Spotify Local Files

Spotify Local Files afișează doar fișiere bine etichetate. Etichetele citite de Spotify sunt limitate.

- **ID3v2.4: ON** în majoritatea cazurilor. Dacă o piesă nu apare corect în Spotify după editare, **încearcă să salvezi cu ID3v2.4: OFF** (adică ca ID3v2.3) — parser-ul Spotify a fost istoric conservator în privința v2.4.
- **Coperta albumului: Mediu sau Mare** — Spotify oricum o redimensionează.
- Completează cel puțin **Titlu**, **Artist**, **Album** și **Număr piesă**.

### Pregătirea fișierelor pentru încărcare prin distribuitor (DistroKid, TuneCore, CD Baby etc.)

Dacă ești artist care încarcă propria muncă pe platforme de streaming, distribuitorul tău citește de obicei etichetele, dar cere și metadate în interfața sa. Oricum:

- **ID3v2.3** este adesea opțiunea implicită mai sigură — multe pipeline-uri de distribuitor au fost construite cu ani în urmă și preferă formatul mai vechi.
- Încorporează copertă **Mare** (majoritatea distribuitorilor cer copertă ≥ 1.400 × 1.400 px — verifică ghidurile lor).
- Nu te baza pe etichete extinse — distribuitorii citesc doar câmpurile de bază.

### Pregătirea fișierelor pentru Plex, Jellyfin, Navidrome, Subsonic, Emby

Aceste servere media auto-găzduite sunt foarte tolerante. Citesc atât v2.3, cât și v2.4 curat și gestionează bine UTF-8.

- **ID3v2.4: ON** este în regulă.
- **Coperta albumului: Mare** sau **Foarte mare** — aceste servere servesc coperți clienților mobili și ecranelor CarPlay, deci calitatea contează.
- **Album Artist** puternic recomandat — pe acesta îl folosesc Plex/Jellyfin pentru a grupa albumele după artist corect.

### Pregătirea fișierelor pentru sisteme audio auto și hardware mai vechi

- **ID3v2.4: OFF** (folosește ID3v2.3) — head unit-urile mai vechi adesea nu suportă v2.4.
- **Coperta albumului: Mediu** — multe display-uri auto se blochează pe coperți încorporate mari.
- **Duplicarea etichetelor: ON** — sistemele audio auto mai vechi citesc uneori doar fallback-ul ID3v1.

## Alte îmbunătățiri

### Designul Liquid Glass

Interfața Evertag 4.2 este reglată pentru noul material **Liquid Glass** de la Apple în întreaga aplicație — suprafețe translucide, animații mai fluide și controale rafinate care se potrivesc natural cu iOS, iPadOS și macOS.

### Bibliotecile de conexiune actualizate

Am reîmprospătat bibliotecile interne folosite de Evertag pentru a comunica cu **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** și alte servicii. Rezultatul: mai puține eșecuri de conexiune în cazurile marginale, suport mai bun pentru versiuni mai noi de servere și fiabilitate îmbunătățită la editarea etichetelor pe fișiere de la distanță.

### Corecții de traducere și localizare

Mai multe corecții lingvistice în UI bazate pe feedback direct de la utilizatori. Așezare mai bună a textului pe butoane mai mici în mai multe limbi.

### Rafinări mai mici inspirate de feedbackul tău

Multe îmbunătățiri minore bazate pe recenziile App Store și e-mailurile la support@everappz.com. Citim fiecare mesaj.

## Obține Evertag 4.2

[**Descarcă Evertag din App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) sau actualizează din App Store. Evertag se descarcă gratuit, cu actualizări opționale în aplicație pentru funcții avansate. Noile conexiuni cloud, protocoalele de rețea, îmbunătățirile Wi-Fi Drive și UI-ul Liquid Glass fac parte din actualizarea de bază.

Dacă îți place aplicația, lasă o evaluare în App Store — ne ajută foarte mult. Ai feedback sau ai întâmpinat o problemă? Scrie-ne la **support@everappz.com**. Citim fiecare mesaj.

## Întrebări frecvente

{{% details title="Ce este nou în Evertag 4.2?" closed="true" %}}
Evertag 4.2 adaugă peste 6 conexiuni noi de cloud și server (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), un Wi-Fi Drive reîmprospătat cu selecție multiplă și coadă de încărcare mai inteligentă, actualizări UI Liquid Glass, biblioteci de conexiune actualizate, corecții cheie ale erorilor de editare a etichetelor și îmbunătățiri ale traducerii.
{{% /details %}}

{{% details title="Ar trebui să folosesc ID3v2.4 sau ID3v2.3 în Evertag?" closed="true" %}}
Folosește **ID3v2.4** pentru playere moderne (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, aplicații Android moderne) și pentru biblioteci cu caractere non-latine — suportul UTF-8 înseamnă etichete mai curate în chineză, coreeană, japoneză, rusă, arabă și ebraică. Folosește **ID3v2.3** dacă etichetele tale se afișează incorect în unele aplicații, dacă țintești sisteme audio auto mai vechi sau dacă un pipeline de distribuitor de streaming respinge v2.4. Poți schimba oricând și salva din nou.
{{% /details %}}

{{% details title="De ce sunt etichetele mele greșite în Spotify după editare?" closed="true" %}}
Spotify afișează în mare parte metadate din propriul catalog — etichetele tale locale sunt folosite doar pentru «Local Files» sau conținut pe care l-ai încărcat ca artist. Dacă etichetezi fișiere pentru Spotify Local Files și nu se afișează corect, încearcă să dezactivezi ID3v2.4 în Evertag și să salvezi ca ID3v2.3 — parser-ul Spotify a fost istoric conservator în privința v2.4.
{{% /details %}}

{{% details title="Ce dimensiune de copertă a albumului ar trebui să aleg în Evertag?" closed="true" %}}
Pentru majoritatea utilizatorilor: **Mare**. Arată grozav pe telefoane, iPad-uri, Mac-uri și display-uri auto moderne fără să umfle prea mult fișierele. Folosește **Mediu** dacă ai o bibliotecă uriașă și vrei să economisești spațiu pe disc. Folosește **Original** (fără scalare) doar pentru master-uri de arhivă sau când chiar ai nevoie de calitate maximă — dar fii conștient că unele playere mai vechi se chinuie cu coperți încorporate foarte mari. **Original** face parte din upgrade-ul de personalizare premium Evertag.
{{% /details %}}

{{% details title="Coperțile mai mari îmi vor face fișierele mai mari?" closed="true" %}}
Da. Încorporarea unei coperți de 3.000 × 3.000 px poate adăuga mai mulți megabytes la un singur fișier audio. Pe o bibliotecă de 1.000 de piese, aceasta ajunge la gigabytes. Dacă spațiul de stocare este limitat, folosește Mediu sau Mare; dacă faci streaming dintr-un NAS unde dimensiunea nu contează, Foarte mare sau Original sunt în regulă.
{{% /details %}}

{{% details title="Ce sunt etichetele duplicate și ar trebui să le activez?" closed="true" %}}
Duplicarea etichetelor scrie metadatele de bază atât în secțiunile ID3v1 (legacy 128 octeți), cât și ID3v2 (modernă) ale fișierului. Activeaz-o doar dacă țintești playere foarte vechi sau hardware care citește ID3v1. Pentru tot ce este modern (smartphone-uri, computere, sisteme audio auto recente), las-o oprită.
{{% /details %}}

{{% details title="Editează Evertag etichetele direct pe fișierele cloud?" closed="true" %}}
Da. Conectează-te la cloud-ul tău (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 etc.) sau prin FTP/SFTP/NFS, deschide un fișier și editează etichetele ca și cum ar fi local. Evertag descarcă fișierul, aplică modificările tale și încarcă versiunea actualizată înapoi. Poți alege între modurile «Întreabă întotdeauna», «Auto-încărcare» sau «Nu încărca» în setări.
{{% /details %}}

{{% details title="Pot edita etichetele FLAC pe iPhone cu Evertag?" closed="true" %}}
Da. Evertag suportă FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE și alte formate importante cu suport complet de citire/scriere a etichetelor, inclusiv coperta încorporată.
{{% /details %}}

{{% details title="Cum editez etichetele în siguranță pe serverul meu de acasă cu SFTP?" closed="true" %}}
Deschide Evertag, mergi la Conexiuni, alege SFTP și introdu numele de gazdă sau IP-ul serverului tău, portul (de obicei 22), numele de utilizator și o parolă sau o cheie SSH privată. Evertag va parcurge folderele tale de la distanță și va edita etichetele direct cu criptare end-to-end peste SSH.
{{% /details %}}

{{% details title="Pot edita etichetele pe mai multe fișiere simultan?" closed="true" %}}
Da. Activează **Editare fișiere simultan** în setări. Selectează mai multe fișiere, deschide editorul de etichete și orice câmp pe care îl modifici va fi aplicat tuturor fișierelor selectate. Acesta este cel mai rapid mod de a seta același album artist, an sau gen pentru un întreg album.
{{% /details %}}

{{% details title="Este actualizarea la Evertag 4.2 gratuită?" closed="true" %}}
Da. Evertag se descarcă gratuit din App Store, iar 4.2 este o actualizare gratuită pentru toți utilizatorii existenți. Noile integrări cloud, îmbunătățirile Wi-Fi Drive și UI-ul Liquid Glass fac parte din actualizarea de bază.
{{% /details %}}

{{% details title="Pe ce dispozitive este disponibil Evertag 4.2?" closed="true" %}}
Evertag 4.2 rulează pe iPhone, iPad și Mac. Sincronizarea iCloud Drive menține setările editorului de etichete consistente între dispozitive.
{{% /details %}}
