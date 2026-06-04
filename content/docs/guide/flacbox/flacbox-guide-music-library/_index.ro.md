---
title: "Bibliotecă Muzicală"
date: 2020-02-01
description: "Aflați cum să construiți, organizați și sincronizați biblioteca muzicală în Flacbox pe iPhone, iPad și Mac. Adăugați piese manual sau sincronizați din servicii cloud, gestionați metadate, coperți de album, liste de redare, preferințe, recente și marcaje. Include suport audio Hi-Res, editor de etichete MusicBrainz, sincronizare online și offline, și opțiuni de personalizare."
keywords: [
  "bibliotecă muzicală Flacbox", "sincronizare muzică din cloud", "organizare metadate muzică",
  "editare etichete audio Flacbox", "sincronizare muzică offline", "importare muzică locală",
  "gestionare liste de redare Flacbox", "căutare coperți album Flacbox",
  "metadate muzică iPhone", "ghid aplicație Flacbox",
  "Flacbox MusicBrainz", "Flacbox normalizare etichete",
  "bibliotecă muzică hi-res Flacbox", "bibliotecă FFmpeg Flacbox",
  "albume solo Flacbox", "vizualizare compozitor Flacbox"
]
tags: ["muzică", "ghid", "flacbox", "bibliotecă"]
readingTime: 11
---


Gestionarea bibliotecii muzicale este simplă cu Flacbox, unde puteți organiza fără efort toate piesele dvs. — FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE locale și zeci de alte formate — într-o colecție unică, căutabilă. Aveți două opțiuni pentru a construi biblioteca muzicală: adăugare manuală (alegeți exact ce se adaugă) sau sincronizare automată (Flacbox scanează foldere cloud desemnate și adaugă automat fișiere noi pe măsură ce apar).

{{< cards cols="1">}}
  {{< card title="" subtitle="Vizualizare Albume Bibliotecă Muzicală Flacbox" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Adăugare Manuală

Pentru a adăuga manual piese, atingeți pictograma **Adăugare Muzică** situată în colțul din stânga sus și alegeți foldere sau fișiere dintr-un serviciu de stocare cloud conectat sau fișiere situate pe dispozitivul dvs. Când adăugați piese la bibliotecă, se creează doar linkuri la acele piese — fișierele reale rămân în locațiile lor originale pentru a economisi spațiu de stocare valoros. Dacă doriți să faceți piesele disponibile offline, puteți folosi acțiunea Descărcare din meniul de opțiuni sau activa Modul Offline pentru liste de redare și colecții de piese.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Adăugare Cântece la Biblioteca Muzicală" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Puteți, de asemenea, să glisați și să plasați fișiere în bibliotecă pe versiunea Mac, sau să folosiți **Deschidere Fișiere…** / **Deschidere Folder…** din selectorul de fișiere al sistemului pe iPhone și iPad.

## Continuare Redare

Restaurați coada playerului audio de la ultima poziție salvată dacă această funcție este activată în setările aplicației. Activați atât **Salvare Stare Player Audio** cât și **Salvare Poziție Redare** în Setări → Player Audio → General pentru cea mai bună experiență. Odată activat, un buton **Continuare Redare** apare în partea de sus a fiecărui ecran de folder, album, artist, gen și listă de redare — atingeți-l pentru a sări direct înapoi la piesa și poziția exactă unde ați rămas.

## Locații

Toate piesele din biblioteca dvs. sunt grupate în mod atent după tipul sursei și etichetele muzicale. Puteți filtra cântecele după locație folosind butonul **Mai Multe Acțiuni** din colțul din dreapta sus și selectând **Filtrare**.

### Muzică Online

Această secțiune prezintă muzică din serviciile dvs. de stocare cloud conectate. Piesele de aici sunt transmise la cerere; nimic nu ocupă stocare locală până când nu descărcați explicit sau activați modul offline.

### Fișiere în Această Aplicație

Aici puteți găsi muzică disponibilă pentru redare offline, provenită din fișierele dvs. locale. Aceasta include fișiere din directorul Documente al aplicației — orice ați descărcat, transferat via Wi-Fi Drive sau importat prin Partajare Fișiere Finder.

### Fișiere pe Acest iPhone / iPad / Mac

Această categorie include muzică importată în aplicație de pe dispozitivul dvs., adăugată prin dialogul de sistem **Deschidere Fișiere…**. Fișierele originale rămân în locația lor originală; Flacbox păstrează doar un link la ele.

## Categorii

Când adăugați piese la biblioteca muzicală, aplicația citește automat etichetele lor audio și le organizează în categorii precum Cântece, Cântece Neredate, Albume, Artiști de Album, Artiști, Genuri și Compozitori.

## Grupare Etichete

Aceste categorii vă ajută să organizați piesele după etichete muzicale. Când adăugați piese la biblioteca muzicală, aplicația citește metadatele acestora și le grupează după aceste categorii. Dacă nu vedeți toate albumele, asigurați-vă că aplicația a scanat fiecare piesă. Puteți verifica progresul scanării în Setări → Bibliotecă Muzicală → Citire Metadate → Număr de Fișiere Procesate în Biblioteca Muzicală. Pentru fișierele locale, puteți, de asemenea, să rescanaţi folderele offline în Setări → Bibliotecă Muzicală → Sincronizare Foldere Offline → Pornire Scanare Foldere Locale. După ce cititorul de metadate finalizează toate operațiunile, veți vedea următoarele categorii în biblioteca muzicală:

- **Cântece** — toate cântecele grupate după eticheta TRACK_TITLE. Puteți verifica ordinea de sortare folosind meniul Mai Multe Acțiuni din colțul din dreapta sus.
- **Cântece Neredate** — toate cântecele care nu au fost niciodată redate.
- **Albume** — cântece grupate după eticheta ALBUM_NAME, ignorând etichetele de artist, artist de album și compozitor. Dacă aveți mai multe albume cu același nume dar artiști diferiți, luați în considerare utilizarea sortării Albume Exclusive descrisă mai jos.
- **Artiști de Album** — cântece grupate numai după ALBUM_ARTIST_TAG. Util pentru a menține compilațiile și colaborările clar separate de munca solo.
- **Artiști** — cântece grupate numai după ARTIST_TAG.
- **Genuri** — cântece grupate după eticheta GENRE.
- **Compozitori** — cântece grupate după eticheta COMPOSER — de neprețuit pentru bibliotecile de muzică clasică unde „compozitorul" este axa primară de navigare.

## Preferințe

Puteți marca cântecele ca preferate pe ecranul playerului audio sau folosind meniul de opțiuni. Preferințele apar în propria lor secțiune pentru a le putea găsi cu o singură atingere.

## Recente

Această secțiune afișează toate piesele redate recent. Puteți personaliza câte elemente menține lista de recente în Setări → Bibliotecă → Recente → Schimbare Dimensiune Listă, și exportați lista în M3U / CSV / TXT pentru a face copie de rezervă a istoricului dvs. de ascultare.

## Marcaje

Puteți crea marcaje audio în timp ce un cântec se redă și să le gestionați pe acest ecran — perfect pentru cărți audio, mixuri lungi, prelegeri sau pentru a marca refrenul unei piese preferate. Instrucțiuni detaliate despre lucrul cu marcajele audio sunt disponibile [aici](/docs/guide/evermusic/evermusic-guide-music-library).

## Bara de Instrumente Superioară

Situată imediat sub bara de navigare, bara de instrumente superioară oferă mai multe acțiuni convenabile: Căutare, Redare Toate, Amestecare Toate și Continuare Redare. Puteți dezvălui sau ascunde această bară de instrumente cu un simplu gest de glisare în jos.

## Căutare

Funcția de căutare vă dă puterea să localizați o piesă, artist, album sau gen specific în biblioteca muzicală. Pe ecranul de Căutare, aveți acces la acțiunile Sortare, Filtrare și vedere Grilă / Listă. Căutarea rulează local față de baza de date a bibliotecii muzicale, deci funcționează complet offline și returnează rezultate pe măsură ce tastați.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Căutare în Biblioteca Muzicală" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Meniu Opțiuni

Fiecare cântec din biblioteca muzicală are un meniu cu mai multe acțiuni, accesat atingând butonul cu trei puncte lângă titlul cântecului. Aceste acțiuni variază în funcție de dacă este un cântec individual sau parte dintr-o colecție.

### Pentru Cântece Individuale

- **Redare Următoare** — adaugă cântecul în vârful cozii playerului.
- **Redare Mai Târziu** — adaugă cântecul la sfârșitul cozii playerului.
- **Adăugare la Listă de Redare** — adaugă cântecul la o listă de redare.
- **Adăugare la Preferințe** — marchează cântecul ca preferat pentru acces rapid.
- **Descărcați** — salvează cântecul în fișierele locale. Apare în fila **Fișiere Locale** și secțiunea **Muzică Offline**.
- **Editați etichetele audio** — deschide editorul de etichete audio integrat pentru a remedia metadatele lipsă; notați că aceasta va altera cântecul pe stocarea dvs.
- **Afișare în Folder** — dezvăluie folderul unde este stocată fișierul audio.
- **Afișare în Finder** — pentru fișierele importate de pe Mac-ul dvs., această acțiune dezvăluie folderul unde este localizat fișierul audio pe Mac-ul dvs.
- **Deschidere În** — exportă fișierul audio în altă aplicație.
- **Ștergere din Serviciul Cloud** — elimină fișierul atât din biblioteca muzicală cât și din stocarea cloud. **Această acțiune este ireversibilă.**
- **Ștergere din Biblioteca Muzicală** — șterge cântecul din biblioteca muzicală, dar fișierul rămâne în stocare. Dacă sincronizarea automată este activată și fișierul există pe stocarea la distanță, va reapărea în biblioteca dvs. după o operațiune de sincronizare.

### Pentru Colecții de Cântece

Pentru colecții de cântece precum Albume, Artiști, Genuri sau Compozitori, meniul de opțiuni include următoarele acțiuni.

- **Redare Toate** — înlocuiește coada playerului cu cântece din colecția selectată.
- **Redare Următoare** — adaugă cântecele din această colecție în vârful cozii playerului.
- **Redare Mai Târziu** — adaugă cântecele din această colecție la sfârșitul cozii playerului.
- **Adăugare la Listă de Redare** — include cântece din această colecție într-o listă de redare, cu opțiunea de a crea una nouă.
- **Activare Mod Offline** — descarcă cântece din această colecție în fișierele locale. Fișierele apar în fila **Fișiere Locale** și secțiunea **Muzică Offline**. Dacă sunt adăugate elemente noi la colecție pe server, vor fi descărcate automat.
- **Editare Imagine** — schimbați coperta albumului pentru colecția de cântece.
- **Adăugare la Arhivă** — grupați întreaga colecție într-un singur fișier ZIP pentru copie de rezervă sau transfer ușor (funcționalitate Premium).
- **Exportare Listă Cântece** — exportați colecția în M3U, CSV sau TXT pentru utilizare în alți playere sau pentru arhivare.
- **Ștergere din Biblioteca Muzicală** — elimină colecția de cântece din biblioteca muzicală. Această acțiune nu șterge fișierele reale din stocare. Dacă sincronizarea automată este activată și fișierele există pe stocarea la distanță, vor reapărea în biblioteca dvs. după o operațiune de sincronizare.

## Modul Selecție

Puteți activa modul de selecție folosind butonul Mai Multe Acțiuni din colțul din dreapta sus. În acest mod, puteți selecta mai multe piese simultan și efectua acțiuni în lot — adăugare la listă de redare, marcare ca preferate, ștergere din bibliotecă, descărcare și altele.

## Detaliu Album

Când deschideți secțiunile Artist, Artist de Album sau Compozitor, puteți vedea un comutator pentru Cântece / Toate Albumele / Albume Exclusive / Albume Solo.

- **Cântece** — afișează toate cântecele unde acest Artist / Artist de Album / Compozitor apare în etichetele audio.
- **Toate Albumele** — arată albumele de compilație și toate albumele unde artistul este prezent.
- **Albume Exclusive** — arată albumele unde artistul specificat este singurul artist cu acel nume de album.
- **Albume Solo** — arată albumele unde apar numai piesele artistului specificat, chiar dacă alți artiști au albume cu același nume.

Aceasta este deosebit de utilă pentru curățarea compilațiilor aglomerate de «Artiști Diferiți» în biblioteci mari.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Ecran Detaliu Album" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Setări

Atingeți Mai Multe Acțiuni → Setări pentru a configura preferințele bibliotecii muzicale.

### Citire Metadate

Când adăugați piese la bibliotecă, cititorul de metadate începe lucrul. Acest proces de fundal citește toate metadatele din piesele dvs. și le organizează după Artist, Album, Gen și Compozitor. Puteți ajusta viteza de citire a metadatelor pentru a încărca datele mai rapid — fiți conștient că o citire mai rapidă folosește mai multă energie. Puteți, de asemenea, dezactiva complet cititorul de metadate și afișa numele fișierelor în loc de informațiile din etichete.

Important, cititorul de metadate actualizează numai metadatele din biblioteca dvs. muzicală și nu alterează fișierele stocate în contul dvs. cloud sau stocarea locală. Dacă doriți să editați metadatele pentru fișierele audio, puteți face asta folosind editorul de etichete integrat, pe care îl puteți activa din acțiunea corespunzătoare din meniul de opțiuni.

### Moduri Disponibile pentru Cititorul de Metadate

- **Dezactivat** — cititorul de metadate este oprit și numele fișierelor sunt afișate în loc de datele din etichetele audio.
- **Cântec Curent** — aplicația citește metadatele numai pentru cântecul redat în prezent. Folosiți această opțiune dacă aveți o conexiune de rețea lentă pentru a preveni cititorul de metadate să trimită multe cereri serverului cloud, ceea ce poate cauza întreruperi în redare.
- **Coadă Redare** — aplicația citește metadatele pentru toate cântecele din coada playerului audio.
- **Bibliotecă** — aplicația citește metadatele pentru toate cântecele din biblioteca muzicală.

Când comutatorul **Citire Metadate în Fundal** este activ, cititorul de metadate continuă să lucreze în modul de fundal. Notați că dacă aplicația consumă multă energie în timpul redării audio, sistemul de operare iOS poate o suspenda.

Deci, dacă aveți o colecție muzicală mare, este recomandabil să folosiți versiunea desktop a aplicației pentru sincronizarea metadatelor. Puteți apoi folosi funcția Copie de Rezervă și Restaurare din setările aplicației pentru a transfera biblioteca sincronizată de pe desktop pe mobil.

Când opțiunea **Normalizare Codificare Metadate** este activată, aplicația normalizează automat codificarea metadatelor pentru toate cântecele din biblioteca muzicală. Aceasta remediază problemele în care codificarea etichetelor audio este deteriorată (cum ar fi după editarea fișierelor pe un PC Windows) și previne afișarea caracterelor incorecte în informațiile pieselor.

Acțiunea **Reîncărcare metadate** marchează fiecare fișier din biblioteca muzicală ca având metadate lipsă, determinând cititorul de metadate să actualizeze fiecare înregistrare.

Atingeți **Pornire Citire Metadate** pentru a declanșa manual cititorul. Progresul operațiunii este afișat mai jos.

### Sincronizare Online

Sincronizarea automată a muzicii online permite adăugarea automată a pieselor din serviciile cloud conectate la biblioteca muzicală. Pentru a activa această funcționalitate, mergeți la Setările Bibliotecii Muzicale și selectați folderele de sincronizare.

Cu această opțiune activată, aplicația scanează toate folderele selectate, identifică fișierele audio acceptate și le integrează perfect în biblioteca dvs. Puteți porni sau opri sincronizarea atingând acțiunea de meniu corespunzătoare.

Sincronizarea muzicii online funcționează exclusiv când aplicația este în prim-plan, ceea ce înseamnă că sincronizarea unei biblioteci mari poate dura ceva timp. Pentru a accelera procesul, lăsați aplicația deschisă, conectați-o la o sursă de alimentare și activați Ecran → Mereu Activ în setările aplicației.

Alternativ, puteți efectua sincronizarea muzicii online pe versiunea desktop a aplicației și transfera biblioteca muzicală la versiunea iOS folosind funcționalitatea Copie de Rezervă și Restaurare.

Puteți, de asemenea, seta cât de des doriți să sincronizați biblioteca de muzică online. Dacă setați intervalul la Imediat, sincronizarea online va porni de fiecare dată când deschideți aplicația.

### Sincronizare Offline

Aici puteți configura sincronizarea muzicii offline.

#### Foldere Offline Sincronizate

Când faceți un folder cloud disponibil offline (prin meniul Mai Multe Acțiuni), acesta apare în secțiunea Fișiere Locale → Foldere Offline. Aplicația descarcă conținutul său pe dispozitivul dvs. Dacă faceți modificări la folder în cloud — cum ar fi adăugarea, eliminarea sau actualizarea fișierelor — aplicația detectează acele modificări și actualizează automat copia locală.

Pe acest ecran, puteți porni manual sincronizarea folderului offline, dezvălui folderul offline în folderul său înconjurător și dezactiva modul offline pentru folder. Dezactivarea modului offline elimină toate copiile locale ale fișierelor de pe dispozitivul dvs.

#### Interval de Timp

Puteți seta intervalul de timp pentru cât de des ar trebui să verifice aplicația folderele offline pentru modificări.

#### Pornire Scanare Foldere Locale

Această opțiune scanează toate folderele locale situate în directorul Documente al aplicației pentru a găsi fișiere audio acceptate. Toate aceste fișiere locale sunt adăugate perfect la biblioteca muzicală. Fișierele locale situate pe dispozitivul dvs. dar în afara acestei aplicații trebuie adăugate la biblioteca muzicală manual, deoarece aplicația nu are acces la fișierele din afara directorului Documente al aplicației din cauza restricțiilor de securitate iOS / macOS.

#### Important

Este recomandat să inițiați periodic sincronizarea muzicii offline pentru a vă menține biblioteca muzicală actualizată cu fișierele locale.

### Personalizare

În această secțiune, puteți configura stilul ecranului bibliotecii muzicale conform preferințelor dvs. Sunt disponibile trei opțiuni: Meniu Simplu, Meniu Grupat, Meniu cu File. Puteți, de asemenea, activa sau dezactiva afișarea coperților de album în ecranele de detaliu ale albumelor.

### Coperți de Album

Aici, puteți configura modul în care aplicația încarcă și stochează copertele albumelor.

- **Tip Rețea** — alegeți Wi-Fi sau Wi-Fi și Date Celulare pentru descărcările de coperți.
- **Încărcare Coperți Album pentru Fișiere Online** — când este activat, coperțile de album încorporate sunt încărcate pentru fișierele stocate în stocarea cloud. Aceasta poate utiliza date suplimentare de rețea.
- **Căutare în Folder** — când este activat, dacă o piesă nu are copertă încorporată, aplicația caută imagini JPEG sau PNG în același folder și le folosește ca copertă album.
- **Calitate Copertă** — alegeți calitatea coperților de album stocate pe dispozitivul dvs.
- **Afișare în Folder** — deschideți folderul unde sunt memorate în cache coperțile albumelor.
- **Ștergere Toate** — ștergeți coperțile albumelor memorate în cache pentru a elibera spațiu de stocare și a forța aplicația să le reîncarce la cerere.

În mod implicit, aplicația verifică coperțile de album încorporate în piesele dvs. și le afișează dacă sunt disponibile. Dacă nu există coperți de album încorporate și opțiunea **Căutare în Folder** este activată, aplicația verifică folderul înconjurător pentru imagini JPEG sau PNG și le folosește ca coperți de album pentru toate piesele din acel folder.

### Liste de Redare

Puteți activa opțiunea de a adăuga același cântec la o listă de redare de două ori. În mod implicit, această opțiune este dezactivată.

### Recente

Puteți gestiona lista de cântece redate recent.

- **Ștergere Listă** — ștergeți întreaga listă de cântece redate recent.
- **Schimbare Dimensiune Listă** — setați numărul de elemente care apar în listă.
- **Exportare Listă Cântece** — exportați lista de cântece redate recent în M3U, CSV sau TXT. Instrucțiuni detaliate sunt disponibile [aici](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Preferințe

Puteți gestiona lista cântecelor dvs. preferate.

- **Editare Simultană** — când este activat, adăugarea unui cântec la preferințe îl adaugă atât în biblioteca muzicală cât și în secțiunea de fișiere simultan.
- **Ștergere Listă** — ștergeți întreaga listă de cântece preferate.
- **Exportare Listă Cântece** — similar cu Recente, exportați lista de preferințe în M3U, CSV sau TXT.

### Ștergere Bibliotecă

Această acțiune va șterge baza de date a bibliotecii muzicale, dar va lăsa fișierele muzicale neatinse în stocare.

### Limită Încărcare Conținut

În mod implicit, aplicația folosește paginare pentru a reduce timpul de încărcare a conținutului și a menține bibliotecile mari receptive. Totuși, puteți dezactiva această opțiune și permite aplicației să încarce toate datele disponibile dintr-o dată. Pentru aceasta, deschideți setările aplicației, derulați în jos la Personalizare → Limită Încărcare Conținut și alegeți Dezactivat.
