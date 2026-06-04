---
title: "Player Audio"
date: 2020-02-01
description: "Aflați cum să utilizați playerul audio Flacbox pe iPhone, iPad și Mac. Controlați redarea, gestionați cozile, configurați motorul audio FFmpeg / sistem, modificați rata de eșantionare, corecția înălțimii tonului, durata bufferului IO, egalizatorul, marcajele audio, AirPlay 2, Google Cast, CarPlay, widget-uri și scurtăturile de tastatură pentru Mac."
keywords: [
  "ghid player Flacbox", "setări player audio", "egalizator Flacbox",
  "streaming muzică AirPlay", "Google Cast muzică", "marcaje audio",
  "coadă redare Flacbox", "repetare aleatoriu Flacbox", "control volum Flacbox",
  "mini player macOS", "aplicație muzică VoiceOver",
  "Flacbox FFmpeg", "corecție ton Flacbox", "rată eșantionare Flacbox",
  "DAC extern Flacbox", "sunet surround Flacbox", "buffer IO Flacbox",
  "viteză redare Flacbox", "temporizator somn Flacbox"
]
tags: ["ghid", "flacbox", "player"]
readingTime: 14
---


Playerul Audio este ecranul principal al aplicației unde controlați muzica și majoritatea funcțiilor de redare. Este, de asemenea, locul unde motorul audio hi-res al Flacbox — construit pe codecurile sistemului plus biblioteca **FFmpeg** inclusă — face toată munca grea. Să explorăm cum să îl utilizați.

## Accesarea Playerului Audio

Puteți ajunge la playerul pe ecran complet din bara mini playerului. Pe iPhone, mini playerul se află în partea de jos a ecranului principal. Pe iPad și Mac, este pe partea stângă. Pentru a ascunde mini playerul pe iPhone, atingeți-l o dată și glisați în jos. Pentru a închide complet playerul pe ecran complet, atingeți butonul de închidere din colțul din dreapta jos.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player Main Screen" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Formate Audio Acceptate

Flacbox redă cele mai populare formate audio — atât codecurile de sistem Apple, cât și multe formate suplimentare gestionate de motorul FFmpeg inclus:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Aceasta acoperă practic fiecare format modern cu pierderi și fără pierderi pe care este posibil să îl aveți într-o colecție muzicală personală.

## Controale de Redare

În partea de jos a ecranului playerului, veți vedea butoane pentru Redare, Pauză, Piesa Următoare și Piesa Anterioară. Există, de asemenea, butoane opționale precum Următori 30 sec. și Anteriori 30 sec. pe care le puteți activa în setările aplicației (utile pentru audiobooks). Puteți derula rapid înainte sau înapoi ținând apăsate butoanele Următor / Anterior. Pentru a sări la o parte specifică a unei piese, trageți cursorul de redare.

## Repetare și Aleatoriu

Atingeți butonul de repetare pentru a trece prin modurile de repetare:

- **Repetare Toate** — repetă în buclă toate piesele din coada dvs.
- **Repetare Una** — repetă doar piesa curentă.
- **Oprire după Piesă** — face pauză când piesa curentă se termină.
- **Fără Repetare** — redă coada o singură dată fără a repeta.

Utilizați butonul **Aleatoriu** pentru a randomiza ordinea pieselor din coadă.

## Controlul Volumului

Deschideți ecranul Setări Audio atingând pictograma de sunet sub controalele de redare pentru a accesa cursorul de volum. Veți găsi, de asemenea, butoane aici pentru **Google Cast** și **AirPlay** astfel puteți comuta rapid redarea pe alt dispozitiv.

## Google Cast (Chromecast)

Pentru utilizatorii Google Cast, pictograma **Cast** apare în partea de jos a playerului. Atingeți-o pentru a alege un dispozitiv și a începe streaming-ul. Asigurați-vă că dispozitivul dvs. și receptorul Google Cast sunt în aceeași rețea Wi-Fi. Notă: nu fiecare format audio este compatibil cu Google Cast — unele formate hi-res pot necesita transcodare.

## AirPlay

Pentru AirPlay, căutați butonul **AirPlay** în partea de jos a playerului. Atingeți-l și selectați un dispozitiv pentru streaming. Flacbox suportă **AirPlay 2**, astfel puteți reda pe mai multe HomePod-uri, Apple TV-uri sau boxe compatibile AirPlay 2 simultan.

## Egalizator Audio

Flacbox include un **egalizator cu 10 benzi** cu presetări în stil iPod. Atingeți Egalizator în vizualizarea volumului, apoi porniți-l în colțul din dreapta sus. Puteți folosi presetări precum Acustic și Amplificare Bași sau ajusta fiecare bandă de frecvență cu cursoarele. Creați propriile presetări, salvați-le sub orice nume și amplificați volumul global cu preamplificatorul. Avem instrucțiuni mai detaliate despre cum să utilizați egalizatorul [aici](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player Equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Bara de Instrumente a Modului Player

Pentru unele stiluri de player, există o bară de instrumente dedicată în partea de sus a playerului pe ecran complet. Această bară de instrumente adăpostește trei butoane utile:

- **Căutare** — localizați rapid o piesă specifică în coada playerului dvs.
- **Control Viteză de Redare** — ajustați viteza de redare de la 0,02× la 3,00×. Perfect pentru audiobooks, podcasturi și prelegeri. Atingeți Normal pentru a reveni la viteza implicită.
- **Marcaje Audio** — creați mai multe marcaje pe piesă. Avem instrucțiuni complete despre cum să utilizați marcajele [aici](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Coada Playerului

Pentru a vedea coada playerului, atingeți butonul de coadă din partea dreaptă a piesei curente. Fiecare piesă din coadă are mai multe acțiuni — atingeți cele trei puncte pentru a le vizualiza. Pentru a reordona o piesă în coadă, utilizați indicatorul de reordonare lângă titlu și trageți-l la o nouă poziție.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Playback Queue" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Comentarii / Versuri

Pentru a vizualiza comentariile piesei și versurile integrate, precum și fișierele LRC, urmați acești pași:

1. Deschideți **Setări**.
2. Mergeți la **Player Audio**.
3. Selectați **Personalizare**.
4. Atingeți **Butoane pe ecranul principal**.
5. Activați **Comentarii**.

După aceea, atingeți butonul de coadă al playerului din partea de jos a ecranului de mai multe ori pentru a comuta de la vizualizarea cu copertă / coadă la vizualizarea cu comentarii. Pe ecranul Comentarii, glisați la dreapta pentru a comuta între **Comentarii**, **Versuri Integrate** și **Fișierul LRC**. Instrucțiuni complete sunt disponibile [aici](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lyrics and Comments Screen" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Meniu Opțiuni

Fiecare piesă din coada playerului audio are un meniu cu mai multe acțiuni, accesat atingând butonul cu trei puncte lângă titlul piesei.

- **Redare Următoare** — adaugă piesa în fruntea cozii playerului.
- **Adăugare la Listă de Redare** — include piesa într-o listă de redare, cu opțiunea de a crea una nouă.
- **Adăugare la Favorite** — marchează piesa ca favorită pentru acces rapid.
- **Descărcare** — salvează piesa în fișierele locale, apărând în fila **Fișiere Locale** și în secțiunea **Muzică Offline**.
- **Editare Etichete Audio** — deschide editorul de etichete audio integrat pentru a corecta metadatele lipsă, modificând piesa în stocarea dvs.
- **Afișare în Dosar** — dezvăluie dosarul unde este stocat fișierul audio.
- **Afișare în Finder** — pentru fișierele importate de pe Mac, dezvăluie dosarul unde se află fișierul audio pe Mac-ul dvs.
- **Deschidere În** — exportă fișierul audio în altă aplicație.
- **Ștergere din Coadă** — elimină piesa selectată din coada playerului audio.
- **Ștergere din Serviciul Cloud** — șterge piesa atât din biblioteca muzicală, cât și din stocarea cloud. **Această acțiune este ireversibilă.**
- **Ștergere din Fișierele Locale** — șterge piesa atât din biblioteca muzicală, cât și din stocarea locală. **Această acțiune este ireversibilă.**
- **Ștergere din Biblioteca Muzicală** — șterge piesa din biblioteca dvs. muzicală, păstrând fișierul în stocare.

Aceleași opțiuni sunt disponibile pentru elementul în curs de redare din coada playerului audio, pe care îl puteți accesa atingând pictograma **Mai Multe Acțiuni** lângă titlul piesei.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Options for an Item in the Playback Queue" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Acțiuni Suplimentare ale Playerului

Atingeți butonul **Mai Multe Acțiuni** «...» din partea stângă a titlului piesei în curs de redare pentru a vedea acțiuni suplimentare.

- **Continuare Redare** — reluați de unde ați rămas, inclusiv coada și poziția media. Deosebit de util pentru audiobooks. Activat în setările aplicației.
- **Căutare** — localizați rapid o piesă specifică în coada playerului audio.
- **Marcaje** — vizualizați lista marcajelor audio create.
- **Comentarii** — vizualizați comentariile piesei și versurile integrate, precum și fișierele LRC. Instrucțiuni complete [aici](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Viteză** — ajustați viteza de redare după preferință.
- **Recente** — accesați o listă de piese redate recent.
- **Favorite** — vizualizați colecția dvs. de piese favorite.
- **Egalizator Audio** — activați egalizatorul audio.
- **Temporizator Somn** — setați un temporizator pentru a opri redarea după un interval specificat. Excelent pentru acele momente când doriți să adormiți cu muzica preferată.
- **Salvare Coadă ca Listă de Redare** — salvați coada curentă a playerului audio ca o nouă listă de redare.
- **Ștergere Coadă** — goliți coada playerului și opriți redarea.
- **Setări** — accesați setările playerului audio.
- **Ajutor** — găsiți asistență și îndrumare.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player More Actions Screen" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Marcaje Audio

Această funcție vă permite să creați mai multe marcaje pentru piesele din biblioteca dvs. muzicală — perfect pentru audiobooks, prelegeri, mixuri DJ lungi sau marcarea refrenului unei piese preferate.

Pentru a crea un marcaj nou:

- Începeți să redați piesa dorită.
- Deschideți ecranul playerului.
- Atingeți butonul **Marcaje** pe bara de instrumente a modului player.
- Selectați **Adăugare Marcaj**.
- Alegeți ora marcajului și atingeți **Terminat** în colțul din dreapta sus.

Editarea marcajelor pentru piesa curentă este ușoară: atingeți Editare în colțul din dreapta sus pentru a intra în modul de editare. În acest mod, puteți reordona marcajele, șterge, ajusta ora marcajului și schimba titlurile marcajelor. Instrucțiuni mai detaliate despre marcajele audio sunt disponibile [aici](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Bookmarks Screen" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Recente și Favorite

Pe ecranul playerului, atingeți cele trei puncte pentru a accesa Recente și Favorite. În ambele secțiuni, puteți căuta piese, reda toate, amesteca toate, exporta lista și șterge lista. Avem instrucțiuni detaliate despre cum să exportați liste de piese [aici](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Conectați iPhone-ul la mașina dvs. prin USB sau Apple CarPlay wireless și Flacbox apare pe ecranul principal CarPlay, gata să redea muzică în siguranță în timp ce conduceți. Interfața CarPlay include file dedicate pentru Bibliotecă, Conexiuni, Fișiere Locale și Setări, cu controale de redare, aleatoriu, repetare, gestionarea cozii și egalizatorul audio, toate disponibile fără a ridica telefonul. Configurați experiența CarPlay în Setări → CarPlay — opțiuni de sortare, paginare, culoarea gradientului pictogramelor meniului, dacă imaginile sunt încărcate și o opțiune pentru a face pauză automată a redării când vă conectați la CarPlay.

[Citiți ghidul complet CarPlay](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox on Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widget-uri Ecran Principal (iPhone și iPad)

Flacbox suportă widget-urile Ecranului Principal și Ecranului de Blocare iOS pentru a putea vedea și controla redarea dintr-o privire. Asigurați-vă că Widget-urile sunt activate în Setări → Widget-uri → Activare Widget-uri, apoi apăsați lung Ecranul Principal sau Ecranul de Blocare, atingeți **+**, căutați **Flacbox** și adăugați un widget. Widget-ul se actualizează în timpul redării pentru a afișa coperta, titlul și artistul piesei în curs de redare.

## Fereastra Mini Player (exclusiv Mac)

Utilizatorii de Mac pot folosi un mini player compact mereu deasupra. Mutați cursorul în colțul din dreapta jos al ferestrei Flacbox, redimensionați-o la dimensiunea minimă și atingeți butonul de restrângere. Mențineți-o deasupra oricărei alte ferestre selectând Fereastră → Afișare Fereastră Mereu Deasupra din bara de meniuri — perfect pentru a menține vizibilitatea controalelor muzicii în timp ce lucrați în altă aplicație.

## Scurtături Tastatură (exclusiv Mac)

Pentru utilizatorii de Mac, un meniu de redare sistem este disponibil în bara de stare cu scurtături de tastatură. De exemplu, apăsați bara de spațiu pentru Redare / Pauză. Scurtăturile pentru Oprire, Piesa Următoare, Piesa Anterioară, Săritură Timp, Repetare, Aleatoriu și Viteză de Redare sunt, de asemenea, disponibile.

## Setările Playerului Audio

Pentru a accesa setările, atingeți butonul Mai Mult de pe ecranul playerului și alegeți Setări. Aici veți găsi mai multe secțiuni enumerate mai jos.

### General

Aceste setări acoperă aspectele fundamentale ale playerului audio, inclusiv coada de redare, ieșirea audio și salvarea stării playerului.

- **Mod de Repetare** — alegeți cum se comportă playerul audio când o piesă se termină:
  - **Repetare Toate** — redă din nou toate piesele din coada dvs.
  - **Repetare Una** — repetă doar piesa curentă.
  - **Oprire după Piesă** — face pauză la redare când piesa curentă se termină.
  - **Fără Repetare** — permite cozii dvs. să fie redată fără repetare.
- **Mod Aleatoriu** — randomizează ordinea pieselor din coada dvs. Îl puteți dezactiva sau activa.
- **Codec Audio** — alegeți motorul audio utilizat pentru redare:
  - **System Codec + FFmpeg** — prioritizează codecul audio al sistemului acolo unde este posibil, îmbunătățind compatibilitatea și stabilitatea. Corecția tonului și ajustările ratei de eșantionare a ieșirii audio pot fi limitate în acest mod.
  - **FFmpeg** — forțează codecul FFmpeg pentru toate fișierele audio, permițând ajustarea corecției tonului și a ratei de eșantionare a ieșirii audio.
- **Rata de Eșantionare a Ieșirii Audio** — ajustați rata de eșantionare a ieșirii audio pentru a optimiza calitatea sunetului, deosebit de utilă cu un DAC extern. Valori disponibile: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** și **96 kHz**.
- **Numărul de Canale ale Ieșirii Audio** — pentru sisteme audio multicanal cu un DAC extern, specificați numărul de canale: **Mono, Stereo, Center / Left / Right, Center / Left / Right / Surround, ITU BS.775-1, 5.1 Surround** și **SDDS**.
- **Durata Preferată a Bufferului IO al Ieșirii Audio** — configurați durata bufferului de intrare / ieșire pentru redarea audio. O valoare tipică pentru minimizarea latenței la redarea audio de înaltă rezoluție este de aproximativ **5 milisecunde (0,005 secunde)**. Dimensiunea acceptabilă a bufferului depinde de mediul dvs. hardware și software, deci testați diferite durate pe dispozitivul dvs. țintă și alegeți-o pe cea care echilibrează cel mai bine latența scăzută și redarea fără probleme.
- **Mod de Ieșire Audio (doar iOS)** — configurați modul de ieșire audio mixat astfel sunetul din Flacbox se amestecă cu alte aplicații. Instrucțiuni detaliate sunt [aici](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Salvare Poziție Redare** — asigură că aplicația salvează și restaurează poziția de redare pentru piesele din biblioteca muzicală.
- **Salvare Stare Player Audio** — păstrează starea playerului audio înainte de a închide aplicația. Pentru a continua redarea, atingeți **Continuare Redare** în fruntea oricărui dosar, album, artist sau gen când redeschideți aplicația. Puteți, de asemenea, restaura redarea pentru fișiere individuale atingând piesa specifică.

Odată ce ați activat atât **Salvare Poziție Redare** cât și **Salvare Stare Player Audio**, deschideți orice dosar, album, artist sau gen și veți vedea un buton **Continuare Redare** în fruntea ecranului împreună cu ultima piesă și poziție salvate. Atingeți-l pentru a relua exact de unde ați rămas.

### Personalizare

Personalizarea vă permite să personalizați aspectul ecranului playerului audio, să schimbați controalele disponibile pe ecranul principal, ecranul de blocare și bara de stare și să configurați controalele de săritură a timpului.

- **Stil Ecran Player Audio** — configurați poziționarea elementelor pe ecranul playerului audio.
- **Stil Defilare Coperte Albume** — configurați stilul preferat de defilare pentru coperțile albumelor.
- **Elemente Suplimentare** — activați elemente suplimentare pe ecranul playerului audio. **Informații Format Audio** afișează informațiile audio ale piesei în curs de redare deasupra copertei; **Cursor Volum Audio** afișează cursorul de ieșire audio sub controalele de redare.
- **Acțiuni Ecran Principal** — configurați ce butoane ar trebui să fie vizibile implicit pe ecranul principal al playerului audio: **Mod Repetare și Aleatoriu, Piesa Următoare și Anterioară, Săritură Timp, Temporizator Somn, Google Chromecast, AirPlay și Bluetooth, Egalizator Audio, Căutare, Marcaje, Viteză, Adăugare Marcaj, Adăugare la Favorite, Comentarii** și altele.
- **Controale de Redare pe Ecranul de Blocare** — alegeți ce controale apar pe ecranul de blocare. Valori posibile: **Săritură Timp, Adăugare Marcaj, Adăugare la Favorite**.
- **Butoane Săritură Timp** — alegeți intervalul de timp pentru butoanele de **Săritură Timp**.

### Încărcare Fișiere

În timpul procesului de încărcare a fișierelor, puteți schimba tipul de rețea utilizat pentru încărcarea pieselor. Opțiuni disponibile: **Wi-Fi**, **Wi-Fi și Date Celulare**.

- **Timp de Preîncărcare** — setați intervalul de timp de buffering. Măriți-l dacă aveți o conexiune de rețea slabă.
- **Utilizare URL Direct** — când este activat, se folosește un URL direct pentru a încărca piesa dacă serverul îl suportă. Aceasta poate accelera încărcarea pieselor dar poate afecta stabilitatea redării.

### Egalizator Audio

Personalizați setările egalizatorului audio. Puteți citi mai mult despre configurarea egalizatorului audio [aici](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Viteză de Redare

Ajustați viteza de redare a playerului audio de la **0,02× la 3,00×**. Atingeți pictograma de configurare din colțul din dreapta sus pentru a comuta la **modul precis** pentru ajustări mai fine.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Playback Speed Screen" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Corecție Ton

Schimbați setările de corecție a tonului folosind valorile predefinite. Puteți, de asemenea, comuta între valorile predefinite și modul precis atingând butonul din colțul din dreapta sus. Corecția tonului este disponibilă în calea codecului FFmpeg, cu un interval de la **-1000 la +1000**.

### Cache Redare

Piesele din coada playerului audio sunt descărcate automat pentru a asigura o redare fluidă. Dacă descărcați manual fișiere audio, puteți dezactiva această opțiune pentru a evita duplicatele. Puteți, de asemenea, configura dimensiunea cache-ului playerului audio aici.

### Temporizator Somn

Activați un temporizator pentru a opri automat redarea după o perioadă specificată — util când doriți să adormiți cu muzica preferată. Atingeți pictograma de configurare din colțul din dreapta sus pentru **modul precis** cu granularitate minut cu minut.

## Accesibilitate

Flacbox este complet accesibil cu **VoiceOver**. Fiecare componentă are o etichetă și descriere bine concepute. Când VoiceOver este activ, aplicația comută la **Modul Text** astfel numai elementele semnificative sunt afișate — îmbunătățind viteza de navigare și claritatea. Puteți, de asemenea, activa Modul Text în **Setări → Accesibilitate → Mod Text**.

### Ajustarea Cursoarelor cu VoiceOver

1. **Selectați cursorul** — glisați la stânga sau dreapta până când VoiceOver îl anunță.
2. **Ajustați valoarea** — atingeți de două ori și mențineți apăsat cursorul, apoi glisați în sus sau jos pentru a schimba valoarea rapid. VoiceOver anunță noua valoare pe măsură ce avansați.

### Ajustarea Poziției Piesei dintr-o Listă cu VoiceOver

1. Atingeți pictograma indicatorului de reordonare lângă titlul piesei pentru a-i da focus.
2. Atingeți rapid de două ori indicatorul de reordonare. La a doua atingere, nu eliberați degetul — mențineți-l apăsat până auziți un sunet care indică că celula este gata de mutat.
3. Mutați celula în noua sa poziție.

Alte componente funcționează conform așteptărilor, folosind modele VoiceOver furnizate de sistem.
