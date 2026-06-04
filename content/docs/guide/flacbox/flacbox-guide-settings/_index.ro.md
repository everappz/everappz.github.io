---
title: "Setări"
date: 2020-02-01
description: "Explorați fiecare setare din Flacbox — de la preferințele de redare, motorul audio FFmpeg / sistem, ieșirea audio Hi-Res, reglajele egalizatorului, corecția tonului, durata bufferului IO, sincronizarea metadatelor, controlul listelor de redare, transferurile de fișiere, widget-urile ecranului principal, Apple CarPlay, personalizarea interfeței, limbă, cod de acces, copie de rezervă și restaurare, și actualizarea Premium."
keywords: [
  "setări Flacbox", "configurare player audio", "actualizare Premium Flacbox",
  "WiFi Drive", "sincronizare metadate", "egalizator", "viteză redare",
  "duplicate listă de redare", "setări manager fișiere", "sincronizare muzică offline",
  "editor etichete audio", "mod întunecat", "restaurare achiziții", "copie rezervă setări",
  "setări widget-uri Flacbox", "setări CarPlay Flacbox",
  "Flacbox FFmpeg setări", "Flacbox setări rată eșantionare",
  "Flacbox setări corecție ton", "Flacbox buffer IO",
  "Flacbox cod acces", "limbă Flacbox", "personalizare Flacbox",
  "Flacbox analiză"
]
tags: ["ghid", "flacbox", "setari"]
readingTime: 16
---


Ecranul Setări este centrul de control al Flacbox. De aici puteți face upgrade la Premium, configura motorul audio (codecuri de sistem sau FFmpeg), gestiona biblioteca muzicală, configura managerul de fișiere, personaliza editorul de etichete audio, activa widget-urile ecranului principal și Apple CarPlay, face backup datelor și accesa ajutor și informații juridice. Secțiunile sunt grupate sub anteturi: Achiziții și Actualizări, Preferințe Aplicație, Ajutor și Legal & Confidențialitate.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Settings Main Screen" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Actualizare la Premium

Actualizați aplicația la versiunea Premium pentru a elimina toate limitele. Versiunea gratuită a aplicației oferă o achiziție unică pe viață în aplicație și două opțiuni de abonament (1 lună și 1 an) pentru a elimina toate restricțiile și a face upgrade la Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Upgrade to Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Partajarea în Familie** este activată pentru toate achizițiile și planurile, astfel puteți partaja versiunea Premium cu până la cinci membri ai familiei fără costuri suplimentare.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Select a Premium Plan" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Puteți citi mai mult despre achiziții și versiunea Premium aici: [Care este diferența dintre Flacbox și Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Partajarea Achizițiilor între iOS și Mac

Achizițiile pe viață și abonamentele sunt partajate între iOS și Mac, folosind iCloud pentru sincronizarea acestor informații. Dacă aveți versiunea Premium pe dispozitivul iOS, asigurați-vă că aveți cea mai recentă versiune instalată și că iCloud este activat. Porniți aplicația pe iOS și așteptați un minut pentru ca informațiile despre achiziții să fie încărcate în iCloud.

Puteți, de asemenea, încerca să atingeți butonul Restaurare Achiziții din setările aplicației. Ulterior, instalați cea mai recentă versiune a aplicației din App Store pe Mac și porniți aplicația. Asigurați-vă că aveți o conexiune la internet și că folosiți același cont iCloud și App Store pe Mac pe care l-ați folosit pe iOS. Așteptați un minut pentru ca aplicația să descarce informațiile despre achiziții din iCloud — versiunea Premium ar trebui să se activeze pe Mac-ul dvs. automat.

## Restaurarea Achizițiilor pe un Dispozitiv Nou

Pentru a restaura achiziția pe un dispozitiv nou, utilizați meniul Achiziții → Restaurare Achiziții. Veți vedea lista achizițiilor dvs. Dacă nu le vedeți pe toate, confirmați că dispozitivul este conectat la același Apple ID care a fost folosit pentru achiziții și că iCloud este activat.

## Încercați Premium Gratuit

Puteți face upgrade la versiunea Premium gratuit, pentru o perioadă limitată, folosind acest meniu. Urmăriți o reclamă sau spuneți prietenilor despre aplicație pentru a obține Premium gratuit.

## Achiziții

Puteți restaura achizițiile anterioare din acest meniu. Dacă întâmpinați erori de activare, încercați să activați opțiunea Restaurare Achiziții la Lansarea Aplicației.

## Actualizare Software

Atingeți Actualizare Software pentru a verifica dacă o versiune mai nouă de Flacbox este disponibilă. Aplicația va compara versiunea instalată cu cea mai recentă versiune din App Store și vă va informa dacă o actualizare este recomandată.

## Noutăți

Acest meniu este disponibil după lansarea unei noi versiuni. Afișează un rezumat al modificărilor și noilor funcții din cea mai recentă actualizare.

## Player Audio

Această secțiune configurează playerul audio și motorul audio de bază, inclusiv alegerea FFmpeg / codec sistem și opțiunile de ieșire audio Hi-Res.

### General

Aceste setări acoperă aspectele fundamentale ale playerului audio — coada de redare, ieșirea audio și salvarea stării playerului.

- **Mod de Repetare** — alegeți cum se comportă playerul audio când o piesă se termină:
  - **Repetare Toate** — redă din nou toate piesele din coada dvs.
  - **Repetare Una** — repetă doar piesa curentă.
  - **Oprire după Piesă** — face pauză la redare când piesa curentă se termină.
  - **Fără Repetare** — permite cozii dvs. să fie redată fără repetare.
- **Mod Aleatoriu** — randomizează ordinea pieselor din coada dvs. Îl puteți dezactiva sau activa.
- **Codec Audio** — alegeți motorul audio utilizat pentru redare:
  - **System Codec + FFmpeg** — prioritizează codecul audio al sistemului acolo unde este posibil, îmbunătățind compatibilitatea și stabilitatea. Corecția tonului și rata de eșantionare a ieșirii audio pot fi limitate.
  - **FFmpeg** — forțează codecul FFmpeg pentru toate fișierele audio, deblocând corecția tonului și rata de eșantionare a ieșirii audio.
- **Rata de Eșantionare a Ieșirii Audio** — ajustați rata de eșantionare a ieșirii audio. Valori disponibile: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** și **96 kHz**.
- **Numărul de Canale ale Ieșirii Audio** — pentru sisteme multicanal cu un DAC extern: Mono, Stereo, Center / Left / Right, Center / Left / Right / Surround, ITU BS.775-1, 5.1 Surround și SDDS.
- **Durata Preferată a Bufferului IO al Ieșirii Audio** — configurați durata bufferului. O valoare tipică pentru minimizarea latenței este de aproximativ **5 milisecunde (0,005 secunde)**. Testați diferite durate pe dispozitivul dvs. țintă.
- **Mod de Ieșire Audio (doar iOS)** — configurați modul de ieșire audio mixat. Instrucțiuni detaliate [aici](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Salvare Poziție Redare** — salvează și restaurează poziția de redare pentru piesele din biblioteca muzicală.
- **Salvare Stare Player Audio** — păstrează starea playerului audio înainte de a închide aplicația, facilitând reluarea de unde ați rămas.

Odată ce ați activat atât **Salvare Poziție Redare** cât și **Salvare Stare Player Audio**, deschideți orice dosar, album, artist sau gen și veți vedea un buton **Continuare Redare** în fruntea ecranului.

### Personalizare

Personalizarea vă permite să personalizați aspectul ecranului playerului audio, să schimbați controalele disponibile pe ecranul principal, ecranul de blocare și bara de stare și să configurați controalele de săritură a timpului.

- **Stil Ecran Player Audio** — configurați poziționarea elementelor pe ecranul playerului audio.
- **Stil Defilare Coperte Albume** — configurați stilul preferat de defilare pentru coperțile albumelor.
- **Elemente Suplimentare** — activați elemente suplimentare pe ecranul playerului audio. Informații Format Audio afișează informațiile audio ale piesei în curs de redare deasupra copertei; Cursor Volum Audio afișează cursorul de ieșire audio sub controalele de redare.
- **Acțiuni Ecran Principal** — configurați ce butoane ar trebui să fie vizibile implicit: Mod Repetare și Aleatoriu, Piesa Următoare și Anterioară, Săritură Timp, Temporizator Somn, Google Chromecast, AirPlay și Bluetooth, Egalizator Audio, Căutare, Marcaje, Viteză, Adăugare Marcaj, Adăugare la Favorite, Comentarii și altele.
- **Controale de Redare pe Ecranul de Blocare** — alegeți ce controale apar pe ecranul de blocare. Valori posibile: Săritură Timp, Adăugare Marcaj, Adăugare la Favorite.
- **Butoane Săritură Timp** — alegeți intervalul de timp pentru butoanele de Săritură Timp.

### Încărcare Fișiere

În timpul încărcării fișierelor, puteți schimba tipul de rețea. Opțiuni disponibile: **Wi-Fi**, **Wi-Fi și Date Celulare**.

- **Timp de Preîncărcare** — setați intervalul de timp de buffering. Măriți dacă aveți o conexiune de rețea slabă.
- **Utilizare URL Direct** — când este activat, se folosește un URL direct pentru a încărca piesa dacă serverul îl suportă. Poate accelera încărcarea, dar poate afecta stabilitatea.

### Egalizator Audio

Configurați egalizatorul audio cu 10 benzi, presetările și preamplificatorul. Puteți citi mai mult despre configurarea egalizatorului audio [aici](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Viteză de Redare

Ajustați viteza de redare de la **0,02× la 3,00×**. Atingeți pictograma de configurare din colțul din dreapta sus pentru a comuta la **modul precis**.

### Corecție Ton

Schimbați setările de corecție a tonului sau comutați la **modul precis** atingând butonul din colțul din dreapta sus. Disponibil în calea codecului FFmpeg, cu un interval de la **-1000 la +1000**.

### Cache Redare

Piesele din coadă sunt descărcate automat pentru a asigura o redare fluidă. Dacă descărcați manual fișiere audio, puteți dezactiva această opțiune. Puteți, de asemenea, configura dimensiunea cache-ului aici.

### Temporizator Somn

Activați un temporizator pentru a opri automat redarea după o perioadă specificată. Atingeți pictograma de configurare pentru **modul precis** cu granularitate minut cu minut.

## Bibliotecă

Setările bibliotecii dvs. muzicale — sincronizare automată, citire metadate, încărcare coperte album, liste de redare, recente și favorite — se află aici.

### Citire Metadate

Când adăugați piese în bibliotecă, **cititorul de metadate** intră în acțiune. Acest proces de fundal citește toate metadatele din piesele dvs. și le organizează după Artist, Album, Gen și Compozitor. Puteți ajusta viteza de citire a metadatelor pentru a încărca datele mai rapid (pe cheltuiala bateriei). Puteți, de asemenea, dezactiva cititorul de metadate și afișa numele fișierelor în loc de informațiile din etichete.

Cititorul de metadate **actualizează doar metadatele din biblioteca dvs. muzicală** și nu modifică fișierele stocate în contul dvs. cloud sau stocarea locală. Pentru a edita metadatele din fișierele audio propriu-zise, utilizați **editorul de etichete** integrat prin acțiunea corespunzătoare din meniul de opțiuni.

Când **Citire Metadate în Fundal** este activat, cititorul continuă să lucreze în modul de fundal. Dacă aplicația folosește prea multă energie în timpul redării audio, iOS poate să o suspende.

Dacă aveți o colecție muzicală mare, efectuați sincronizarea metadatelor pe versiunea desktop a aplicației și transferați biblioteca muzicală sincronizată pe iOS folosind **Copie de Rezervă și Restaurare**.

Când **Normalizare Codare Metadate** este activat, aplicația normalizează automat codarea metadatelor pentru toate piesele. Aceasta remediază codările de etichete corupte (de exemplu după editarea fișierelor pe un PC Windows) și previne apariția caracterelor incorecte în informațiile pieselor.

**Reîncărcare Metadate** marchează fiecare fișier din biblioteca dvs. muzicală ca având metadate lipsă, ceea ce determină cititorul de metadate să reîmprospăteze fiecare înregistrare.

**Pornire Citire Metadate** declanșează manual cititorul de metadate. Progresul este afișat sub acțiune.

### Sincronizare Online

Sincronizarea automată a muzicii online adaugă piese din serviciile cloud conectate la biblioteca muzicală automat. Pentru a o activa, deschideți setările bibliotecii muzicale și selectați dosarele de sincronizare.

Cu această opțiune activată, aplicația scanează dosarele selectate, identifică fișierele audio acceptate și le adaugă în bibliotecă. Porniți sau opriți sincronizarea cu acțiunea de meniu corespunzătoare.

Sincronizarea online rulează numai când aplicația este în prim-plan, deci sincronizarea unei biblioteci mari poate dura un timp. Pentru a accelera, mențineți Flacbox deschis, conectați dispozitivul la alimentare și activați **Setări → Ecran → Mereu Activ**.

Puteți, de asemenea, alege cât de des rulează sincronizarea online. Setarea intervalului la **Imediat** declanșează o sincronizare de fiecare dată când deschideți aplicația.

### Sincronizare Offline

Configurați sincronizarea muzicii offline.

#### Dosare Offline Sincronizate

Când marcați un dosar online de pe serverul dvs. cloud ca disponibil offline (folosind meniul **Mai Multe Acțiuni**), apare aici. Conținutul dosarului este descărcat în **Fișiere Locale → Dosare Offline**. Când dosarul online se modifică (fișiere adăugate, eliminate sau actualizate), aplicația verifică modificările și actualizează copia locală de pe dispozitivul dvs.

Pe acest ecran puteți porni manual sincronizarea dosarului offline, dezvălui dosarul offline în dosarul său de încadrare și dezactiva modul offline pentru dosar. Dezactivarea modului offline elimină toate copiile locale ale fișierelor de pe dispozitivul dvs.

#### Interval de Timp

Alegeți cât de des verifică aplicația dosarele offline pentru modificări.

#### Pornire Scanare Dosare Locale

Scanați toate dosarele locale din directorul **Documente** al aplicației pentru fișiere audio acceptate. Fișierele găsite sunt adăugate automat la biblioteca muzicală. Fișierele situate pe dispozitivul dvs. dar în afara directorului Documente al aplicației trebuie adăugate manual la biblioteca muzicală, deoarece aplicația nu le poate accesa din cauza restricțiilor de securitate iOS / macOS.

**Important:** Este recomandat să inițiați periodic sincronizarea muzicii offline pentru a menține biblioteca muzicală actualizată cu fișierele locale.

### Personalizare

Configurați stilul ecranului bibliotecii muzicale. Trei opțiuni disponibile: **Meniu Simplu, Meniu Grupat, Meniu cu File**. Puteți, de asemenea, activa sau dezactiva coperțile albumelor pe ecranul cu detaliile albumului.

### Coperte Albume

Configurați modul în care aplicația încarcă și stochează coperțile albumelor.

- **Tip Rețea** — alegeți **Wi-Fi** sau **Wi-Fi și Date Celulare** pentru descărcarea coperților.
- **Încărcare Coperte Albume pentru Fișiere Online** — când este activat, coperțile integrate sunt încărcate pentru fișierele stocate în stocarea cloud. Poate folosi date de rețea suplimentare.
- **Căutare în Dosar** — când este activat, dacă o piesă nu are copertă integrată, aplicația caută imagini JPEG sau PNG în același dosar.
- **Calitate Copertă** — selectați calitatea coperților de album stocate pe dispozitivul dvs.
- **Afișare în Dosar** — deschideți dosarul unde sunt stocate în cache coperțile albumelor.
- **Ștergere Toate** — ștergeți coperțile de album din cache pentru a elibera spațiu de stocare și a forța aplicația să le reîncarce la cerere.

### Liste de Redare

Activați opțiunea de a adăuga același cântec la o listă de redare de două ori. În mod implicit, această opțiune este dezactivată.

### Recente

Gestionați lista de cântece redate recent.

- **Ștergere Listă** — ștergeți întreaga listă de cântece redate recent.
- **Schimbare Dimensiune Listă** — setați numărul de elemente care apar în listă.
- **Exportare Listă Cântece** — exportați lista de cântece redate recent ca M3U, CSV sau TXT. Instrucțiuni detaliate disponibile [aici](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favorite

Gestionați lista cântecelor dvs. favorite.

- **Editare Simultană** — când este activat, adăugarea unui cântec la favorite îl adaugă atât în biblioteca muzicală, cât și în secțiunea de fișiere simultan.
- **Ștergere Listă** — ștergeți întreaga listă de cântece favorite.
- **Exportare Listă Cântece** — ca și Recente, exportați favoritele ca M3U, CSV sau TXT.

### Ștergere Bibliotecă Muzicală

Ștergeți baza de date a bibliotecii muzicale. Fișierele dvs. muzicale din stocare rămân neatinse.

## Cod de Acces

Activați ecranul de cod de acces pentru a proteja datele aplicației cu un cod numeric de 4 cifre. Când este activat, vi se va solicita să introduceți codul de acces de fiecare dată când aplicația este lansată. Combinați cu iOS Face ID / Touch ID pe dispozitiv pentru protecție suplimentară.

## Manager de Fișiere

Secțiunea Manager de Fișiere controlează modul în care fișierele sunt transferate, stocate și previzualizate.

### Transferuri de Fișiere

Alegeți preferința dvs. de rețea pentru descărcarea fișierelor pe dispozitivul dvs.

### Numărul Maxim de Sarcini Paralele

Setați numărul de fire de descărcare paralele. Un număr mai mare accelerează descărcările dar folosește mai multă baterie.

### Sarcini de Transfer Fișiere

Afișează sarcinile de încărcare și descărcare active în prezent.

### Transferuri în Fundal

Permiteți descărcările în timp ce aplicația este în fundal. Dacă transferurile în fundal consumă multă energie, iOS poate suspenda aplicația.

### Salvare Fișiere Descărcate În

Alegeți directorul de descărcări implicit sau permiteți aplicației să vă întrebe de fiecare dată.

### Dosare Offline Sincronizate

Gestionați sincronizarea offline pentru dosarele selectate. Pentru a activa sincronizarea offline, atingeți butonul cu trei puncte lângă un dosar și selectați **Mod Disponibil Offline**. Fișierele noi adăugate în dosarul cloud sunt descărcate pe dispozitivul dvs. automat. Citiți mai mult despre modurile offline [aici](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Interval de Timp

Alegeți cât de des sunt sincronizate dosarele offline. **Imediat** declanșează o sincronizare de fiecare dată când deschideți aplicația.

### Afișare Nume Fișiere Complete

Afișați numele complete ale fișierelor, inclusiv extensiile, în managerul de fișiere.

### Editare Fișiere Online

Dezactivați editarea fișierelor online pentru a comuta la modul numai citire pentru serviciile cloud conectate și a preveni ștergerile accidentale. Această acțiune elimină operațiunile de editare a fișierelor din interfața utilizatorului.

### Copiere Fișiere la Deschidere

Specificați modul în care aplicația gestionează fișierele importate din alte aplicații.

### Miniaturi pentru Fișiere

Gestionați și ștergeți miniaturile generate ale fișierelor pentru a elibera spațiu de stocare.

### Ștergere Fișiere Temporare

Goliți dosarul de cache al aplicației pentru a recupera spațiu de stocare.

## Editor Etichete Audio

Configurați editorul de etichete audio integrat — util pentru remedierea în lot a problemelor de artist / album / an / gen / copertă album în fișierele cloud și locale.

### Scalare Copertă Album

Alegeți metoda de scalare utilizată când o copertă de album este salvată în etichetele audio.

### Actualizare Fișiere Online

Când este activat, aplicația actualizează automat metadatele unui fișier pe serverul cloud după ce terminați editarea.

### Ștergere Fișier după Editare Online

Alegeți dacă aplicația ar trebui să șteargă copia descărcată după terminarea editării unui fișier online pe un server cloud.

### Butoane Ecran Principal

Alegeți ce butoane sunt vizibile pe ecranul principal al editorului de etichete audio.

Pentru editarea în lot mai profundă a mai multor fișiere odată, instalați aplicația noastră companion **Evertag**.

## Widget-uri

Activați widget-urile pentru ca aplicația să actualizeze datele widget-urilor în timpul redării. Actualizările widget-urilor necesită energie suplimentară, deci comutatorul este dezactivat implicit — activați-l numai dacă utilizați efectiv widget-uri pe Ecranul Principal sau Ecranul de Blocare.

Puteți adăuga widget-uri Flacbox apăsând lung Ecranul Principal sau Ecranul de Blocare, atingând **+**, căutând **Flacbox** și alegând o dimensiune de widget. Widget-urile afișează coperta curentă, titlul piesei și artistul și ating direct la playerul pe ecran complet. Widget-urile funcționează, de asemenea, pe macOS în Centrul de Notificări.

## CarPlay

Schimbați setările CarPlay aici. Acest meniu este, de asemenea, disponibil în interfața CarPlay pentru a putea ajusta experiența în timp ce conduceți.

### Sortare

Configurați opțiunile de sortare pentru toate ecranele CarPlay.

### Limită de Încărcare Conținut

Alegeți dacă aplicația folosește paginare pe ecranul CarPlay. Paginarea menține meniurile responsive pe biblioteci mari.

### Culoarea Gradientului Pictogramelor Meniului

Selectați schema de culori pentru ecranul principal CarPlay.

### Afișare Imagini

Dezactivați imaginile pe ecranul CarPlay pentru a optimiza viteza de încărcare și a reduce utilizarea memoriei pe biblioteci mari.

### Pauză Redare la Conectare

Activați aceasta pentru a evita audio tare brusc când vă conectați dispozitivul la CarPlay.

## Wi-Fi Drive

Activați **Wi-Fi Drive** pentru a transfera fișiere de la un calculator pe dispozitivul dvs. folosind un browser web de birou, Finder sau File Explorer. Instrucțiuni detaliate despre cum să utilizați Wi-Fi Drive sunt disponibile [aici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalizare

Personalizați interfața utilizatorului conform preferințelor dvs.

### Pictogramă Aplicație

Alegeți o pictogramă alternativă pentru aplicație pe Ecranul Principal (Premium).

### Schemă de Culori

Alegeți tema interfeței utilizatorului și activați modul întunecat. Când este selectat **Implicit**, aplicația urmează setările de aspect ale dispozitivului.

### Stil de Fundal

Modificați stilul de fundal al aplicației. În prezent singura opțiune este **Copertă Album Estompată**, care folosește coperta piesei în curs de redare ca fundal estompat al aplicației.

### Aspectul Elementelor din Listă

Reglați modul în care elementele sunt afișate în liste. Util pe ecrane mici — puteți lăsa aplicația să ajusteze automat înălțimea rândului în funcție de conținut sau să afișeze pictograme mai mici în celulele listei.

### Limită de Încărcare Conținut

În mod implicit, aplicația folosește paginare pentru a accelera încărcarea conținutului. Puteți dezactiva paginarea pentru a încărca totul deodată.

### Stil Ecran Fișiere Locale

Schimbați stilul de prezentare al secțiunii **Fișiere Locale**.

### Stil Ecran Bibliotecă Muzicală

Personalizați aspectul ecranului **Bibliotecă Muzicală**.

### Stil Ecran Player Audio

Configurați aspectul ecranului **Player Audio**.

### Stil Meniu Contextual

Alegeți stilul meniului contextual afișat când atingeți butonul **Mai Multe Acțiuni**.

## Fereastră

Disponibil pe Mac și Catalyst. Configurați preferințele legate de fereastră, cum ar fi dimensiunea implicită și comportamentul la lansare.

## Ecran

Alegeți dacă ecranul ar trebui să rămână activ în timp ce utilizați aplicația. Util la scanarea bibliotecilor mari sau la efectuarea de lucrări prelungite de editare a etichetelor.

## Accesibilitate

Activați **Modul Text** pentru a ascunde toate imaginile din interfața utilizatorului. Modul Text este activat automat când VoiceOver este activ și este, de asemenea, util pentru configurații foarte mici sau numai text.

## Limbă

Schimbați limba aplicației și suprascrieți cea implicită a sistemului. Modificarea se aplică după ce închideți complet și redeschideți Flacbox. Localizările acceptate în prezent includ: Afrikaans, Akan, Albaneză, Amharică, Arabă, Armeană, Assameză, Aymara, Azerbaijaneză, Bambara, Bengaleză, Bască, Belarusă, Bosniană, Bulgară, Birmaneză, Catalană, Cebuano, Chineză (Simplificată), Chineză (Tradițională), Corsicană, Croată, Cehă, Daneză, Dhivehi, Dogri, Olandeză, Engleză, Esperanto, Estonă, Ewe, Filipineză, Finlandeză, Franceză, Galiciană, Ganda, Georgiană, Germană, Greacă, Guarani, Gujarati, Creolă Haitiană, Hausa, Hawaiiană, Ebraică, Hindi, Hmong, Maghiară, Islandeză, Igbo, Iloko, Indoneziană, Irlandeză, Italiană, Japoneză, Javaneză, Kannada, Kazahă, Khmeră, Kinyarwanda, Coreeană, Krio, Kurdă, Kurdă Sorani, Kârgâză, Laoțiană, Latină, Letonă, Lingala, Lituaniană, Luxemburgheză, Macedoneană, Maithili, Malgașă, Malaieziană, Malayalam, Malteză, Māori, Marathi, Mizo, Mongolă, Nepaleză, Sotho de Nord, Norvegiană Bokmål, Nyanja, Odia, Oromo, Pashto, Persană, Poloneză, Portugheză, Punjabi, Română, Rusă, Samoană, Sanscrită, Gaelică Scoțiană, Sârbă, Shona, Sindhi, Sinhaleză, Slovacă, Slovenă, Somaleză, Sotho de Sud, Spaniolă, Sundaneză, Swahili, Suedeză, Tadjică, Tamilă, Tătară, Telugu, Tailandeză, Tsonga, Turcă, Turkmenă, Ucraineană, Urdu, Uigură, Uzbekă, Vietnameză, Galeză, Xhosa, Idiș, Yoruba, Zulu.

## Copie de Rezervă și Restaurare

Utilizați această funcție pentru a face backup tuturor datelor aplicației sau pentru a le migra pe alt dispozitiv. Puteți alege ce să includeți:

- **Bază de Date** — toate piesele dvs. din biblioteca muzicală, inclusiv listele de redare. Piesele offline nu sunt incluse pentru a menține dimensiunea fișierului de backup gestionabilă.
- **Coperte Albume** — toate coperțile de album din cache.
- **Setări** — toate setările aplicației dvs.

Atingeți **Copie de Rezervă Date Aplicație** pentru a porni backup-ul. Datele aplicației sunt scrise într-un singur fișier pe care îl puteți folosi mai târziu pentru a restaura starea aplicației pe un dispozitiv nou sau după reinstalarea aplicației.

Pentru a restaura datele aplicației pe un dispozitiv nou, mutați fișierul de backup pe noul dispozitiv folosind un serviciu cloud conectat sau iCloud și deschideți-l pe noul dispozitiv.

Instrucțiuni detaliate pas cu pas: [Cum să Transferați Biblioteca Muzicală între Dispozitive: Ghid Pas cu Pas](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Ajutor

Accesați ghidul aplicației pentru asistență și îndrumare privind utilizarea eficientă a aplicației.

## Întrebări Frecvente

Găsiți răspunsuri la întrebările obișnuite în secțiunea FAQ.

## Trimiteți Feedback

Aveți feedback sau aveți nevoie de asistență? Trimiteți feedback-ul dvs. direct din aplicație echipei noastre de suport.

## Distribuiți Această Aplicație

Distribuiți aplicația prietenilor dvs. pentru a răspândi vestea.

## Descoperire Mai Multe Aplicații

Explorați alte aplicații de la Everappz.

## Termeni și Condiții

Descrie termenii și condițiile pentru utilizarea aplicației. Vă rugăm să îi citiți înainte de a utiliza aplicația.

## Politică de Confidențialitate

Vizitați pagina politicii de confidențialitate pentru a înțelege practicile noastre de gestionare a datelor. Vă rugăm să o citiți înainte de a utiliza aplicația.

## Analiză și Colectare Date

Verificați ce servicii sunt activate pentru analiză și colectare date și dezactivați orice nu doriți.

## Notificări Juridice

Conține informații despre fiecare bibliotecă utilizată în aplicație împreună cu numărul versiunii aplicației și informațiile despre compilare.
