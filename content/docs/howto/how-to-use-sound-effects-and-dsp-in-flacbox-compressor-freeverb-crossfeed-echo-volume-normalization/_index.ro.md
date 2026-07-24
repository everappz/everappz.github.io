---
title: "Cum să folosiți efectele de sunet și DSP în Flacbox: Compressor, Freeverb, Crossfeed, Echo, normalizarea volumului și altele"
date: 2026-07-24
description: "Ghidul complet pentru audio Flacbox pe iPhone, iPad și Mac. Aflați cum funcționează motorul BASS, ce formate suplimentare redă (inclusiv MOD și muzica de tip tracker și DSD) și exact ce face fiecare efect, fiecare cursor și fiecare presetare asupra sunetului dumneavoastră, plus egalizatorul cu 10 benzi și lanțul DSP personalizat."
keywords: ["efecte audio Flacbox", "presetări Flacbox explicate", "motor BASS Flacbox", "bibliotecă audio BASS iOS", "player muzică MOD iPhone", "player muzică tracker iOS", "redare MOD XM IT S3M iPhone", "player DSD iOS", "player FLAC iPhone", "player muzică lossless iOS", "presetări egalizator Flacbox", "egalizator cu 10 benzi iPhone", "normalizare volum iPhone", "EBU R128 iOS", "normalizare intensitate sonoră player muzică", "crossfeed căști iOS", "crossfeed bs2b", "presetări compressor player muzică", "reverb freeverb iOS", "echo delay player muzică", "lanț DSP player muzică", "amplificare bas iPhone", "cum să adăugați efecte la muzică Flacbox", "cele mai bune setări egalizator iPhone"]
tags: ["Flacbox", "Efecte audio", "Cum să", "BASS", "Egalizator", "Amplificare bas", "Compressor", "Freeverb", "Crossfeed", "Echo", "Normalizarea volumului", "EBU R128", "Muzică MOD", "Muzică tracker", "DSD", "FLAC", "DSP", "Căști", "Presetări"]
readingTime: 30
---

{{< author-byline >}}

{{< full-width-tables >}}

**Răspuns scurt:** În Flacbox alegeți un singur **Motor de redare** în **Setări > Player audio**: **Standard** (motorul de sistem Apple), **Universal** (motorul FFmpeg) sau **Sound FX** (**motorul BASS™**). Motorul pe care îl alegeți decide ce formate de fișiere se redau, așa că alegerea contează. Motorul **Sound FX** redă formate suplimentare pe care majoritatea aplicațiilor iPhone le omit (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus și vechea **muzică MOD și tracker** precum MOD, XM, IT și S3M) și este singurul motor care pune în funcțiune instrumentele de sunet: un **egalizator cu 10 benzi**, **Normalizarea volumului**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** și un **lanț DSP** pe care îl construiți singur. Așadar, pentru a folosi efectele din acest ghid, setați mai întâi Motorul de redare pe **Sound FX**. Fiecare instrument are **presetări** gata făcute. Deschideți-le în **Setări > Player audio** (Efecte audio, Egalizator audio, Procesare semnal) sau atingeți butonul **⋯ (Mai multe)** din player și alegeți **Efecte audio**. Nimic din ce faceți aici nu vă modifică vreodată fișierele.

> Explicațiile pentru cursoare și presetări de mai jos sunt aceleași descrieri scurte pe care Flacbox vi le afișează în aplicație, îmbinate cu puțin context suplimentar, astfel încât să aveți imaginea completă înainte de a atinge.

## Cum să citiți acest ghid

Fiecare instrument funcționează la fel:

1. **Porniți-l.** Fiecare efect are propriul comutator pornit/oprit. Toate sunt oprite la început. Puteți porni câte doriți în același timp.
2. **Alegeți o presetare.** O presetare este o setare gata făcută. Atingeți una și sunetul se schimbă imediat. Acest ghid enumeră ce face **fiecare** presetare.
3. **Reglați fin (opțional).** Deschideți cursoarele pentru a ajusta manual. În momentul în care mișcați un cursor, efectul afișează **Manual**, ca să știți că ați părăsit presetarea. Fiecare cursor are un buton de resetare.

Nimic nu se salvează în fișierele dumneavoastră. Acestea sunt efecte în timp real. Opriți un efect și sunetul original revine pe loc.

## Alegeți-vă Motorul de redare (Sound FX are efectele)

Flacbox nu amestecă motoarele între ele. Alegeți **unul singur** în **Setări > Player audio > Motor de redare**, iar motorul pe care îl alegeți decide ce formate de fișiere puteți reda și dacă efectele sunt disponibile. Există trei opțiuni, afișate în aplicație sub aceste nume exacte:

1. **Standard.** Motorul de sistem încorporat de la Apple. Folosește decodarea hardware pentru un consum mai mic de baterie.
2. **Universal.** Motorul FFmpeg, care deschide o gamă foarte largă de formate.
3. **Sound FX.** **Motorul BASS™**. Redă fișiere lossless și de înaltă rezoluție cu acuratețe deplină, adaugă muzică de tip modul (tracker) și pune în funcțiune fiecare efect, egalizatorul cu 10 benzi și lanțul DSP din acest ghid.

Deoarece fiecare motor acceptă propriul set de formate, fișierele pe care le puteți reda se schimbă odată cu motorul pe care îl selectați. Mai important, efectele, egalizatorul și lanțul DSP funcționează **doar** cu motorul **Sound FX**, așa că alegeți-l mai întâi dacă doriți să le folosiți.

Sound FX este construit pe **BASS™**, o bibliotecă audio profesională de la Un4seen Developments. Puteți citi mai multe despre ea pe pagina sa principală la [un4seen.com](https://www.un4seen.com/).

## Formate muzicale: ce adaugă motorul Sound FX (BASS™) (inclusiv muzica MOD și tracker)

Cu motorul **Sound FX (BASS™)** selectat, Flacbox redă formatele specializate de mai jos, pe lângă cele obișnuite. Cea mai specială este **muzica de tip modul**, numită și **muzică tracker**. Un fișier modul nu este o înregistrare obișnuită. El conține mici sunete de instrumente plus o „partitură” care spune cum să le redai, iar Flacbox reconstruiește piesa în timp real din acea partitură, așa cum aceste fișiere erau menite să fie redate. Playerele obișnuite nu pot face acest lucru.

| Tip de muzică | Formate | Bine de știut |
|---|---|---|
| **Muzică modul / tracker** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Reconstruită în timp real de playerul de module BASS™. Excelentă pentru chiptune-uri și piese vechi din demoscene sau de pe Amiga. |
| **Lossless modern** | FLAC | Calitate deplină, mai mic decât WAV. |
| **Alte formate lossless** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Tipuri lossless mai puțin comune, toate acceptate. |
| **DSD de înaltă rezoluție** | DSF, DFF | Se redă pe hardware obișnuit folosind DSD peste PCM. |
| **Lossy modern** | Opus, Ogg Vorbis, MP3 | Tipurile obișnuite de streaming și descărcare. |

Motorul Sound FX redă și formatele Apple obișnuite (AAC, ALAC, M4A, WAV, AIFF) și fluxurile live, așa că efectele și egalizatorul funcționează și pe acelea.

**De ce vă ajută acest lucru:** dacă aveți un amestec de albume FLAC, fișiere DSD de înaltă rezoluție și un dosar cu piese vechi MOD sau XM de tip tracker, Flacbox le redă pe toate, iar egalizatorul și efectele funcționează pe fiecare dintre ele.

## Cele trei meniuri pe care le veți folosi

Flacbox își păstrează instrumentele de sunet în trei locuri, toate în setările playerului audio. Mai întâi asigurați-vă că **Motorul de redare** este setat pe **Sound FX** (Setări > Player audio > Motor de redare), deoarece efectele, egalizatorul și lanțul DSP sunt disponibile doar cu acel motor.

- **Efecte audio** (rack-ul de efecte): deschideți playerul, atingeți **⋯ (Mai multe)**, atingeți **Efecte audio**. Sau mergeți la **Setări > Player audio > Efecte audio**.
- **Egalizator audio** (10 benzi și presetări): **Setări > Player audio > Egalizator audio**.
- **Procesare semnal** (propriul lanț DSP): **Setări > Player audio > Procesare semnal**.

Puteți seta și **frecvența de eșantionare a ieșirii**, **canalele** și **dimensiunea bufferului** în **Setări > Player audio**.

## Egalizatorul cu 10 benzi

**Ce face:** Schimbă tonalitatea muzicii, de la basul profund la înaltele strălucitoare. Acesta este cel mai bun instrument pentru o **amplificare a basului** curată sau pentru un capăt de sus mai luminos și mai clar. Gândiți-vă la el ca la zece butoane de volum, fiecare pentru o felie diferită a sunetului. Ridicați o bandă pentru a aduce acea parte în față, coborâți-o pentru a o retrage. Modificările mici de câțiva dB sună de obicei cel mai bine și funcționează pe tot ce redați.

**Cum funcționează:** Zece cursoare la **32, 64, 125, 250, 500 Hz și 1, 2, 4, 8, 16 kHz**. Fiecare merge de la **-12 dB (tăiere)** la **+12 dB (amplificare)**. Există și un **Preamplificator** de la **-24 la +24 dB** pentru nivelul general. Vă puteți salva propriile presetări și le puteți **exporta sau importa** între dispozitive.

**Ce face fiecare presetare încorporată (22 de presetări):**

| Presetare | Ce face sunetului dumneavoastră |
|---|---|
| **Flat** | Fără modificări. Toate benzile la zero. Un punct de plecare curat. |
| **Acoustic** | Bas cald și înalte clare, prezente. Face chitarele acustice și vocile să pară naturale și vii. |
| **Bass Booster** | Ridicare puternică în capătul de jos, mediile și înaltele neatinse. Mai mult impact și greutate. |
| **Bass Reducer** | Taie capătul de jos. Util pentru camere cu ecou, căști ieftine sau piese grele. |
| **Treble Booster** | Ridică doar înaltele. Adaugă strălucire și aer, mai mult detaliu. |
| **Treble Reducer** | Atenuează înaltele. Îmblânzește înregistrările aspre sau tăioase. |
| **Classical** | Grave pline și înalte blânde cu o ușoară scădere în medii. Fin și spațios pentru muzica orchestrală. |
| **Dance** | Grave mari și înalte luminoase cu medii scobite. Energic și impactant pentru piesele de club. |
| **Deep** | Capăt de jos cald, dens, cu înalte mai blânde. Un sunet plăcut, relaxat. |
| **Electronic** | Bas puternic și înalte luminoase pentru sintetizatoare și ritmuri. Larg și modern. |
| **Hip-Hop** | Bas greu și înalte clare cu medii controlate. Consistent și impactant. |
| **Jazz** | Cald și fin, cu o mică scădere în medii. Ușor și natural pentru jazzul acustic. |
| **Latin** | Grave și înalte amplificate cu medii curate. Luminos și vioi. |
| **Loudness** | Amplifică puternic basul și înaltele (o curbă în „zâmbet”). Sună mai plin la volum mic. |
| **Lounge** | Medii în față cu margini blânde. Relaxat și prietenos cu vocile. |
| **Piano** | Medii și înalte clare, astfel încât notele de pian să răsune curat. |
| **Pop** | Medii ridicate pentru voci, cu grave și înalte retrase. Vocile stau în față. |
| **R&B** | Căldură foarte puternică în josul-mediilor și înalte clare. Fin și bogat. |
| **Rock** | Grave și înalte amplificate pentru chitare și tobe. Energic și plin. |
| **Small Speakers** | Amplifică gravele și taie înaltele pentru a ajuta difuzoarele mici să sune mai plin. |
| **Spoken Word** | Ridică registrul vocii și taie basul profund. Face vorbirea clară. |
| **Vocal Booster** | Împinge mediile unde se află vocile, taie în jurul lor. Vocile ies în evidență. |

**Sfat pentru bas:** Începeți cu **Bass Booster**, apoi, dacă sună tulbure, coborâți Preamplificatorul cu 1 până la 2 dB, astfel încât nimic să nu distorsioneze.

## Normalizarea volumului (intensitate uniformă)

**Ce face:** Unele piese se redau mai tare decât altele, așa că schimbați mereu volumul. Aceasta face ca fiecare piesă să se redea la aproximativ același volum de la sine, ca să nu fie nevoie să o faceți dumneavoastră. Este perfectă pentru listele redate aleatoriu care amestecă înregistrări vechi și noi, albume diferite sau surse diferite, unde o piesă poate fi mult mai tare decât următoarea.

**Cum funcționează:** Ascultă intensitatea reală a fiecărei piese folosind standardul **EBU R128** (măsurat în **LUFS**, aceeași idee pe care o folosesc serviciile de streaming), apoi ajustează fiecare piesă către ținta dumneavoastră. Nu are nevoie de etichete în fișiere și nu modifică niciodată sunetul. EBU R128 măsoară intensitatea pe care urechile dumneavoastră o simt de fapt de-a lungul întregii piese, nu doar vârful cel mai înalt, motiv pentru care se potrivește cu cât de tare par cu adevărat piesele. Flacbox calculează acest lucru în timp real, pe măsură ce muzica se redă (și verifică intensitatea din timp când poate), apoi aplică o singură modificare de volum, constantă, asupra piesei. Limita **Amplificare maximă** oprește înregistrările foarte silențioase de la a fi împinse atât de tare încât să distorsioneze. Deoarece citește sunetul în sine, funcționează pe orice sursă, inclusiv fișiere din cloud, fluxuri live și muzică modul, chiar și atunci când fișierele nu au deloc etichete de intensitate.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Intensitate țintă** | Setează intensitatea către care este nivelată fiecare piesă. Valorile mai mari fac totul să se redea mai tare în general. | -30 până la -6 LUFS (-16) |
| **Amplificare maximă** | Limitează cât de mult pot fi amplificate piesele silențioase. Valorile mai mari aduc înregistrările blânde mai aproape de țintă. | 0 până la 24 dB (12) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Light** | Nivelare blândă pentru ascultare relaxată. Egalizează salturile evidente de volum fără a împinge tare piesele silențioase. |
| **Standard** | Setarea implicită universală. O țintă de intensitate în stil streaming care se potrivește majorității muzicii. Începeți de aici. |
| **Strong** | Potrivire agresivă care împinge ferm piesele silențioase în sus. Cea mai bună pentru biblioteci mixte cu diferențe mari de nivel. |
| **Night** | O țintă generală mai silențioasă care totuși ridică pasajele blânde, astfel încât ascultarea de seară târziu să rămână consecventă și joasă. |

## Compressor (uniformizează părțile tari și silențioase)

**Ce face:** Într-o singură piesă, părțile silențioase pot fi prea slabe, iar cele tari prea puternice. Acesta le apropie, astfel încât întreaga piesă să fie ușor de auzit, chiar și în mașină sau într-un loc zgomotos. Coboară ușor momentele cele mai tari și ridică pe cele mai blânde, ca să nu mai fie nevoie să reglați volumul în timpul unei singure piese. Aceasta diferă de Normalizarea volumului: Compressor uniformizează lucrurile **în interiorul** unei piese, în timp ce Normalizarea volumului potrivește intensitatea **între** piese. Cele două funcționează bine împreună. Începeți cu o presetare și deschideți cursoarele doar dacă doriți mai mult control.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Threshold** | Nivelul la care începe compresia. Valorile mai mici comprimă mai mult din sunet, păstrând părțile silențioase și tari mai apropiate. | -60 până la 0 dB (-20) |
| **Ratio** | Cât de puternic sunt reținute părțile tari după ce depășesc pragul. Valorile mai mari comprimă mai puternic, păstrând sunetul mai uniform. | 1:1 până la 30:1 (4:1) |
| **Attack** | Cât de repede răspunde efectul la un vârf brusc și tare. Valorile scurte prind tranzientele; cele mai lungi le lasă să treacă. | 0.1 până la 1000 ms (10 ms) |
| **Release** | Cât de repede se eliberează efectul după ce trece partea tare. Valorile scurte pot pulsa; cele mai lungi sună mai fin. | 10 ms până la 5 s (100 ms) |
| **Master gain** | Amplificarea finală a ieșirii aplicată după procesare. Ridicați-o pentru a mări intensitatea generală după ce dinamica a fost uniformizată. | -30 până la +30 dB (0) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Transparent** | Plasă de siguranță abia perceptibilă. Păstrează dinamica aproape în întregime și prinde doar vârfurile cele mai tari. |
| **Soft** | Nivelare ușoară pentru ascultare hi-fi acasă. Netezire subtilă fără a comprima muzica. |
| **Standard** | Setare implicită rezonabilă pentru redarea muzicii de zi cu zi. Prima presetare de încercat. |
| **Heavy** | Uniformizare agresivă pentru medii zgomotoase. Mașină, cameră aglomerată, ascultare la volum mic. |
| **Voice / Podcast** | Reglat pentru vorbire. Attack-ul mai lent lasă sibilantele să treacă, gain-ul de compensare generos ridică vocile. |
| **Old Recordings** | Albume de epocă și vinil restaurat, unde nivelul mediu este sub cel al lansărilor moderne. |
| **Late Night** | Compresie puternică plus amplificare mare pentru ascultare silențioasă când vecinii sau familia care doarme contează. |
| **Movie Dialog** | Aduce vorbirea în față față de muzică și efecte sonore într-o coloană sonoră variată. |
| **Streaming Match** | Vizează aproximativ normalizarea intensității serviciilor moderne de streaming, în jurul valorii de -14 LUFS. |
| **Maximum Loudness** | Totul la maximum. Atinge limitatorul; așteptați-vă la un semnal comprimat, foarte uniform. Presetarea literală de volum maxim. |

## Freeverb (reverb, un simț al spațiului)

**Ce face:** Adaugă un simț al spațiului muzicii, de la o cameră mică până la o sală mare. Alegeți o presetare sau reglați singur amestecul uscat și umed, dimensiunea camerei, atenuarea și lățimea. Reverbul este ecoul natural pe care îl auziți în orice spațiu real, iar Freeverb îl recreează în software. Puțin face ca înregistrările plate sau cu microfon apropiat să pară mai deschise și mai vii. Mult plasează muzica într-un spațiu mare, îndepărtat. Este un efect creativ, așa că păstrați amestecul umed moderat pentru rezultate naturale.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Dry mix** | Cât din sunetul original, neatins, este păstrat. Valorile mai mari lasă mai mult din semnalul uscat în amestec. | 0 până la 1 (0.0) |
| **Wet mix** | Cât din sunetul cu reverb este adăugat. Valorile mai mari fac reverbul mai tare și mai evident. | 0 până la 3 (1.0) |
| **Room size** | Dimensiunea spațiului imaginat. Valorile mai mari dau o coadă de reverb mai lungă și mai mare, de la o cameră mică până la o catedrală. | 0 până la 1 (0.5) |
| **Damp** | Cât de repede se estompează frecvențele înalte în coadă. Valorile mai mari fac reverbul mai întunecat și mai cald. | 0 până la 1 (0.5) |
| **Width** | Răspândirea stereo a reverbului. Valorile mai mari fac spațiul să pară mai larg între canalele stânga și dreapta. | 0 până la 1 (1.0) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Room** | Un spațiu mic, strâns. Ambianță subtilă care adaugă un simț al locului fără a estompa sunetul. |
| **Studio** | O cameră de înregistrare uscată, controlată. Exact suficientă reflexie pentru a suna natural. |
| **Hall** | O sală mare de concerte. O coadă lungă și bogată, potrivită pentru muzica orchestrală și acustică. |
| **Cathedral** | Un spațiu de piatră imens, cu ecou. Cea mai lungă și mai dramatică coadă de reverb. |
| **Plate** | Un reverb de placă de studio luminos și dens. Clasic pentru voci și tobe. |
| **Ambience** | O ambianță scurtă și aerisită. Adaugă un simț ușor al spațiului rămânând în mare parte uscat. |

## Auto Wah (baleiaj funky de filtru)

**Ce face:** Un filtru care baleiază singur în sus și în jos pentru un sunet wah funky, asemănător vocii. Alegeți o presetare sau setați singur amestecul umed, feedback-ul, rata, intervalul și frecvența. Este același baleiaj „wah” pe care îl face o pedală wah de chitară, dar aici se mișcă singur în ritmul muzicii. Sună excelent pe piesele funk, disco și electronice. Este un efect îndrăzneț, evident, așa că puțin ajunge mult pe ascultarea de zi cu zi.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Wet mix** | Cât de puternic este efectul wah în amestec. Valorile mai mari fac filtrul baleiat mai evident. | -2 până la +2 (1.5) |
| **Feedback** | Cât din ieșire este readus în efect. Valorile mai mari fac wah-ul mai rezonant și mai pronunțat. | -1 până la +1 (0.5) |
| **Rate** | Cât de repede baleiază filtrul în sus și în jos. Valorile mai mari dau un wah mai rapid, mai ritmic. | 0.1 până la 9 Hz (2.0) |
| **Range** | Cât de departe baleiază filtrul, în octave. Valorile mai mari dau un baleiaj mai larg, mai dramatic. | 0.1 până la 9 octave (4.3) |
| **Frequency** | Frecvența de bază în jurul căreia baleiază filtrul. Valorile mai mici sună mai profund; cele mai mari sună mai luminos. | 1 până la 1000 Hz (50) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Classic** | Un baleiaj wah echilibrat, clasic. Un bun punct de plecare pentru funk și rock. |
| **Slow** | Un baleiaj lent, larg, care plutește blând în sus și în jos. Excelent pentru pad-uri și note lungi. |
| **Funky** | Un baleiaj rapid, impactant, cu multă mișcare. Adaugă mușcătură ritmică chitarelor și sintetizatoarelor. |
| **Deep** | Un baleiaj profund, larg, pornind de la o frecvență joasă. Mare și dramatic. |
| **Subtle** | O mișcare blândă, discretă. Adaugă caracter fără a domina sunetul. |
| **Resonant** | Un wah tăios, rezonant, cu feedback ridicat. Asemănător vocii și expresiv. |

## Phaser (vârtej de whoosh)

**Ce face:** Un filtru baleiat care adaugă o mișcare de vârtej, de whoosh, sunetului. Alegeți o presetare sau setați singur feedback-ul, rata, intervalul și frecvența. Adaugă o mișcare blândă și strălucire fără a schimba notele. Este subtil pe voci și pad-uri și dramatic pe sintetizatoare și chitare. Încercați Slow pentru o senzație visătoare sau Jet pentru un vârtej puternic.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Feedback** | Cât din ieșire este readus în efect. Valorile mai mari fac phaser-ul mai rezonant și mai pronunțat. | -1 până la +1 (0.0) |
| **Rate** | Cât de repede baleiază filtrul în sus și în jos. Valorile mai mari dau un efect de phasing mai rapid, mai ritmic. | 0.1 până la 9 Hz (1.0) |
| **Range** | Cât de departe baleiază filtrul, în octave. Valorile mai mari dau un baleiaj mai larg, mai dramatic. | 0.1 până la 9 octave (4.0) |
| **Frequency** | Frecvența de bază în jurul căreia baleiază filtrul. Valorile mai mici sună mai profund; cele mai mari sună mai luminos. | 1 până la 1000 Hz (100) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Classic** | Un baleiaj de phaser echilibrat, clasic. Un bun punct de plecare pentru chitare și clape. |
| **Slow** | Un baleiaj lent, larg, care plutește blând în sus și în jos. Excelent pentru pad-uri și note lungi. |
| **Fast** | Un baleiaj rapid, strălucitor, cu multă mișcare. Adaugă mișcare și energie. |
| **Deep** | Un baleiaj profund, larg, pornind de la o frecvență joasă. Mare și dramatic. |
| **Subtle** | O mișcare blândă, discretă. Adaugă caracter fără a domina sunetul. |
| **Jet** | Un baleiaj intens, rezonant, cu feedback ridicat, clasicul whoosh de avion cu reacție. |

## Flanger (baleiaj de avion cu reacție)

**Ce face:** O întârziere scurtă, în mișcare, care dă sunetului un whoosh de baleiaj asemănător cu un avion cu reacție. Alegeți o presetare sau setați singur adâncimea, feedback-ul, rata și întârzierea. Este un văr mai puternic și mai metalic al phaser-ului, faimos pentru baleiajul de whoosh din rockul clasic și muzica electronică. Setările subtile adaugă o mișcare blândă, în timp ce setările profunde sunt dramatice și evidente. Cel mai bine folosit cu moderație, pentru efect.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Depth** | Cât de puternic este efectul de baleiaj. Valorile mai mari fac flanging-ul mai evident. | 0 până la 100% (25) |
| **Feedback** | Cât din ieșire este readus în efect. Valorile mai mari fac flanger-ul mai rezonant și mai metalic. | -99 până la +99% (-50) |
| **Rate** | Cât de repede se mișcă baleiajul în sus și în jos. Valorile mai mari dau o mișcare mai rapidă, mai strălucitoare. | 0 până la 10 Hz (0.25) |
| **Delay** | Timpul de întârziere de bază pe care este construit baleiajul. Valorile mai mari dau un caracter mai profund, mai gol. | 0 până la 4 ms (2.0) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Classic** | Un flanger echilibrat, clasic. Un bun punct de plecare pentru chitare și clape. |
| **Subtle** | Un baleiaj blând, discret. Adaugă mișcare fără a domina sunetul. |
| **Deep** | Un baleiaj profund, greu, cu feedback puternic. Mare și dramatic. |
| **Jet** | Un baleiaj intens cu feedback pozitiv, clasicul whoosh de avion cu reacție. |
| **Fast** | Un baleiaj rapid, strălucitor, cu multă mișcare și energie. |
| **Wide** | Un baleiaj lent, larg, cu o întârziere lungă. Bogat și spațios. |

## Echo (repetări)

**Ce face:** Repetă sunetul sub formă de ecouri care se estompează pentru un simț al spațiului și al profunzimii. Alegeți o presetare sau setați singur amestecul umed, feedback-ul și întârzierea. Este ca și cum ai striga într-un canion: sunetul revine o dată sau de mai multe ori după o pauză scurtă. O singură repetare scurtă adaugă corp și o senzație retro, în timp ce repetările mai lungi cu mai mult feedback creează cozi spațioase, care se prelungesc. Presetarea Ping Pong sare repetările între urechea stângă și dreaptă, ceea ce este distractiv pe căști. Păstrați amestecul umed moderat, astfel încât ecourile să susțină muzica, nu să o acopere.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Wet mix** | Cât de tari sunt ecourile în comparație cu sunetul original. Valorile mai mari fac repetările să iasă mai mult în evidență. | -2 până la +2 (0.6) |
| **Feedback** | De câte ori se repetă ecoul. Valorile mai mari dau mai multe repetări care se estompează mai încet. | -1 până la +1 (0.5) |
| **Delay** | Timpul dintre ecouri. Valorile mai scurte dau un slap-back strâns; cele mai lungi dau repetări distanțate. | 0.01 până la 2 s (0.4) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Slapback** | O singură repetare strânsă, chiar în spatele sunetului. Clasicul slap-back rockabilly. |
| **Room** | Un ecou scurt, natural, ca o cameră mică. Adaugă spațiu fără a păta sunetul. |
| **Tape** | Repetări calde, medii, care se estompează treptat, ca o veche întârziere pe bandă. |
| **Dub** | Repetări lungi, grele, cu feedback puternic. Mare, dub și spațios. |
| **Ping Pong** | Ecourile sar între difuzoarele stânga și dreapta pentru un efect stereo larg. |
| **Long** | Repetări lente, larg distanțate, care se prelungesc departe în spatele sunetului. |

## Chorus (sunet mai gros, mai larg)

**Ce face:** Îngroașă și lărgește sunetul suprapunând o copie deplasată peste original. Alegeți o presetare sau setați singur amestecul umed/uscat, adâncimea, rata și feedback-ul. Face ca un singur instrument sau o singură voce să sune ca mai multe cântând împreună, adăugând copii ușor dezacordate, în mișcare. Aceasta adaugă bogăție și o strălucire blândă. Setările subtile încălzesc lucrurile, în timp ce setările puternice sună bogat și visător. Este popular pe chitare, claviaturi și voci.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Wet/Dry** | Cât din chorus auziți în comparație cu sunetul original. Valorile mai mari fac efectul mai evident. | 0 până la 100% (50) |
| **Depth** | Cât de mult oscilează înălțimea în sus și în jos. Valorile mai mari dau un sunet mai gros, mai strălucitor. | 0 până la 100% (25) |
| **Rate** | Cât de repede se mișcă strălucirea. Ratele mai lente sună blând și bogat; ratele mai rapide sună mai mult ca un vibrato. | 0 până la 10 Hz (1.1) |
| **Feedback** | Cât din efect este readus în el însuși. Valorile mai mari fac chorus-ul mai rezonant și mai intens. | -99 până la +99% (25) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Subtle** | O îngroșare blândă care adaugă căldură fără a atrage atenția asupra ei. |
| **Lush** | Un chorus bogat, clasic. O setare excelentă universală pentru chitare și clape. |
| **Ensemble** | O strălucire plină, stratificată, care face ca un singur instrument să sune ca mai multe. |
| **Vibrato** | Complet umed cu o rată rapidă, pentru un vibrato oscilant în loc de un chorus subtil. |
| **Wide** | O strălucire lentă, largă, care deschide imaginea stereo. Spațios și visător. |
| **Twelve-String** | O strălucire luminoasă, rezonantă, care amintește de o chitară cu douăsprezece corzi. |

## Distortion (asprime și margine)

**Ce face:** Adaugă asprime și margine prin supraîncărcarea sunetului. Alegeți o presetare sau setați singur drive-ul, ieșirea și tonul. Aspreşte deliberat sunetul, de la o margine caldă, aspră până la un ton spart, fuzz. Este un efect creativ, de distracție, mai degrabă decât o modalitate de a îmbunătăți calitatea, așa că folosiți-l în cantități mici. Este distractiv pe piesele electronice, rock și experimentale. Coborâți Ieșirea dacă o presetare grea devine prea tare.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Drive** | Cât de tare este distorsionat sunetul. Valorile mai mari sunt mai aspre și mai agresive. | 0 până la 100% (15) |
| **Output** | Nivelul ieșirii după distorsiune. Coborâți-l dacă o setare grea devine prea tare. | -60 până la 0 dB (-18) |
| **Tone** | Atenuează înaltele înainte de distorsiune. Valorile mai mici sună mai întunecat și mai cald. | 100 până la 8000 Hz (8000) |
| **Center** | În jurul cărei frecvențe este concentrată distorsiunea. Deplasează caracterul mai luminos sau mai întunecat. | 100 până la 8000 Hz (2400) |
| **Width** | Cât de larg este acel focus. Îngust sună tăios și nazal; larg sună plin și deschis. | 100 până la 8000 Hz (2400) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Warm Drive** | O asprime ușoară, caldă, care adaugă margine fără a schimba mult caracterul. |
| **Crunch** | Un overdrive crocant clasic, impactant și ritmic. |
| **Overdrive** | Un ton luminos, condus, cu multă mușcătură. Excelent pentru sunetele solo. |
| **Fuzz** | Un fuzz gros, saturat. Greu și plin de armonice. |
| **Metal** | Un ton tăios, concentrat pe medii, cu gain ridicat, pentru sunete agresive, grele. |
| **Screamer** | Un overdrive cu medii amplificate care răzbate, ca un tube screamer. |
| **LoFi** | O distorsiune comprimată, cu bandă îngustă, pentru un caracter lo-fi aspru. |

## Rotate (stereo rotativ)

**Ce face:** Rotește sunetul în jurul câmpului stereo pentru un efect rotativ, de vârtej. Alegeți o presetare sau setați singur rata. Mișcă lent sunetul în jurul canalelor stânga și dreapta, un pic ca un difuzor rotativ, ceea ce adaugă o senzație de vârtej, hipnotică. Setările lente sunt blânde și largi, în timp ce setările rapide sunt amețitoare și evidente. Este un efect stereo, așa că este cel mai observabil pe căști sau pe difuzoare bine plasate.

**Cursor:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Rate** | Cât de repede se rotește sunetul în jurul câmpului stereo. Valorile negative rotesc în cealaltă direcție; zero îl ține pe loc. | -5 până la +5 Hz (1.0) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Slow Pan** | O deplasare lentă, blândă dintr-o parte în alta. Subtil și larg. |
| **Sway** | O legănare constantă stânga-dreapta. Adaugă o mișcare blândă imaginii stereo. |
| **Rotary** | O rotire medie care amintește de un difuzor rotativ. |
| **Fast Spin** | O rotire rapidă în jurul câmpului stereo pentru un efect amețitor, de vârtej. |
| **Reverse** | O rotire medie în direcția opusă. |
| **Whirl** | Un vârtej foarte rapid. Intens și dezorientant. |

## Crossfeed (sunet natural pe căști)

Pe difuzoare, fiecare dintre urechile dumneavoastră aude atât difuzorul stâng, cât și cel drept, doar la momente și volume ușor diferite. Pe căști, această îmbinare naturală dispare: urechea stângă aude doar canalul stâng, iar urechea dreaptă doar pe cel drept. Acest „super stereo” poate face ca muzica să pară că este împărțită în interiorul capului, iar înregistrările puternic panoramate, unde un instrument stă complet pe o parte, pot părea nenaturale sau obositoare la ascultările lungi.

Crossfeed rezolvă acest lucru amestecând o cantitate mică, filtrată, din fiecare canal în celălalt, cu o întârziere minusculă și o atenuare blândă a frecvențelor înalte. Aceasta se apropie de modul în care sunetul de la difuzoare reale ajunge la ambele urechi, inclusiv de felul în care capul umbrește ușor urechea îndepărtată. Rezultatul este o imagine mai naturală, asemănătoare difuzoarelor, care stă puțin în fața dumneavoastră în loc de a fi în interiorul capului, și reduce oboseala de ascultare la sesiunile lungi. Flacbox folosește binecunoscuta metodă **bs2b (Bauer stereophonic-to-binaural)**, un crossfeed open-source respectat, folosit de multe playere audiofile. Puteți citi despre algoritm pe [pagina proiectului bs2b](https://bs2b.sourceforge.net/).

Controlul **Cutoff** stabilește cât de cald sună amestecul, iar **Feed level** controlează cât de puternic este. Presetările acoperă nivelurile clasice bs2b, de la o atingere abia perceptibilă până la un amestec ferm, asemănător difuzoarelor. Crossfeed este un efect pentru căști, așa că lăsați-l oprit când ascultați pe difuzoare.

**Cursoare:**

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Cutoff** | Setează unde începe să se atenueze scurgerea dintre canale. Valorile mai mici dau un efect mai cald, mai pronunțat. | 300 până la 2000 Hz (700) |
| **Feed level** | Controlează cât de mult se scurge un canal în celălalt. Valorile mai mari produc un sunet mai asemănător difuzoarelor. | 1 până la 15 dB (4.5) |

**Presetări:**

| Presetare | Ce face |
|---|---|
| **Subtle** | Crossfeed abia perceptibil pentru ascultare relaxată. Îmblânzește stereo-ul puternic panoramat fără a schimba echilibrul tonal. |
| **Chu Moy** | Setarea implicită universală clasică. Echilibrat și ușor cald, funcționează pe aproape orice material. Începeți de aici. |
| **Strong** | Scurgere mai puternică pentru mixuri mai puternic panoramate. Îngustare stereo mai evidentă. |
| **Jan Meier** | Popular printre entuziaștii de căști. Feed mai larg, prezentare mai asemănătoare difuzoarelor, ușoară ridicare a basului. |
| **Speaker-like** | Reglat pentru cea mai naturală reproducere în stil difuzor pe căști. |
| **Vintage Stereo** | Crossfeed agresiv reglat pentru mixurile din anii 1960 și 1970 cu tobe și voci puternic panoramate. |

## Procesare semnal: construiți-vă propriul lanț DSP

Dincolo de efectele gata făcute, Flacbox vă permite să vă construiți propriul lanț în **Setări > Player audio > Procesare semnal**. Așa cum explică aplicația când lanțul este gol: *„Atingeți + pentru a adăuga un efect. Porniți sau opriți fiecare cu comutatorul său, trageți pentru a reordona, atingeți pentru a-i edita parametrii și apăsați lung pentru a duplica sau șterge.”*

**Ordinea contează**: un filtru înaintea unei distorsiuni sună diferit de același filtru după ea. Puteți îndrepta întregul lanț și către **Toate canalele**, **Canalul stâng** sau **Canalul drept**.

Mai jos este fiecare bloc, cu propriul text al aplicației pentru fiecare cursor și fiecare presetare.

### Gain (ajustarea nivelului)

Ridică sau coboară nivelul într-un punct din lanț.

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Gain** | Amplifică sau taie nivelul în acest punct din lanț. Folosiți-l pentru a compensa nivelul după alte efecte sau pentru a conduce pe cele care urmează. | -24 până la +24 dB (0) |

| Presetare | Ce face |
|---|---|
| **Unity** | Fără modificare de nivel. Un punct de plecare neutru. |
| **Cut** | O tăiere mare. Îmblânzește o sursă tare sau face loc înaintea efectelor care urmează. |
| **Trim** | O tăiere blândă pentru a retrage puțin nivelul. |
| **Lift** | O amplificare modestă pentru a ridica o sursă silențioasă. |
| **Boost** | O amplificare puternică pentru material silențios sau pentru a conduce mai tare efectele care urmează. |
| **Max** | Amplificare maximă. Tare, atenție la clipping mai târziu în lanț. |

### Low Pass (elimină înaltele)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Cutoff** | Setează unde începe filtrul să atenueze înaltele. Coborâți-l pentru a întuneca și înmuia sunetul; ridicați-l spre vârf pentru a deschide complet. | 20 Hz până la 20 kHz (20 kHz) |
| **Resonance** | Accentuează frecvențele chiar la cutoff. Păstrați-l jos pentru o atenuare curată; ridicați-l pentru o margine ascuțită, șuierătoare. | 0.1 până la 10 (0.707) |

| Presetare | Ce face |
|---|---|
| **Air** | Ajustează doar vârful. Ia puțin din margine fără a estompa sunetul. |
| **Warm** | O atenuare blândă a înaltelor pentru un ton mai cald, mai rotund. |
| **Mellow** | Vizibil înmuiat. Retrage strălucirea pentru o senzație relaxată. |
| **Muffled** | Întunecat și înfundat, ca și cum ar fi auzit prin perete. |
| **Telephone** | Un vârf îngust, rezonant, jos în interval. O voce subțire, asemănătoare telefonului. |

### High Pass (elimină gravele)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Cutoff** | Setează unde începe filtrul să atenueze gravele. Ridicați-l pentru a subția capătul de jos și a elimina bubuitul; coborâți-l spre bază pentru a deschide complet. | 20 Hz până la 20 kHz (20 Hz) |
| **Resonance** | Accentuează frecvențele chiar la cutoff. Păstrați-l jos pentru o atenuare curată; ridicați-l pentru o margine ascuțită, șuierătoare. | 0.1 până la 10 (0.707) |

| Presetare | Ce face |
|---|---|
| **Rumble Cut** | Elimină bubuitul subsonic și decalajul DC fără a atinge capătul de jos audibil. |
| **Tighten** | Ajustează frecvențele joase bubuitoare pentru un bas mai strâns, mai curat. |
| **Thin** | Taie căldura și corpul, lăsând un sunet mai ușor, mai subțire. |
| **Radio** | Rămân doar mediile și înaltele, ca un difuzor mic de radio. |
| **Telephone** | Un vârf îngust, rezonant, sus în interval. O voce subțire, asemănătoare telefonului. |

### Band Pass (păstrează o bandă din mijloc)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Center** | Setează frecvența pe care o lasă filtrul să treacă. Tot ce este deasupra și dedesubt este atenuat. Baleiați-o pentru a alege gravele, mediile sau înaltele. | 20 Hz până la 20 kHz (1 kHz) |
| **Resonance** | Controlează cât de largă este banda. Valorile mici lasă să treacă un interval larg; ridicați-o pentru a se îngusta în jurul centrului pentru un ton tăios, rezonant. | 0.1 până la 10 (0.707) |

| Presetare | Ce face |
|---|---|
| **Voice** | O bandă largă în jurul registrului mediu unde se află majoritatea vocilor. Un punct de plecare neutru. |
| **Bass** | Izolează capătul de jos, lăsând doar basul și toba mare. |
| **Body** | Se concentrează pe josul-mediilor pentru un corp cald, cutiat. |
| **Presence** | Ridică susul-mediilor pentru claritate și prezență. |
| **Telephone** | O bandă îngustă din registrul mediu. Un sunet subțire, asemănător telefonului. |
| **Wah** | Un vârf foarte îngust, rezonant. Baleiați centrul pentru un efect wah. |

### Notch (elimină o bandă îngustă)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Frequency** | Setează frecvența pe care o elimină filtrul. Tot ce este deasupra și dedesubt trece. Reglați-o pe un zumzet sau o rezonanță pentru a o elimina. | 20 Hz până la 20 kHz (60 Hz) |
| **Resonance** | Controlează cât de largă este tăierea. Valorile mici scobesc un interval larg; ridicați-o pentru a elimina doar o bandă punctuală și a lăsa restul neatins. | 0.1 până la 10 (8.0) |

| Presetare | Ce face |
|---|---|
| **Mains Hum 60** | Elimină zumzetul electric de 60 Hz (rețeaua nord-americană). Un punct de plecare neutru. |
| **Mains Hum 50** | Elimină zumzetul electric de 50 Hz (rețeaua europeană și altele). |
| **Rumble** | Taie un bubuit sau o rezonanță de frecvență joasă fără a subția întregul capăt de jos. |
| **Mud** | Scobește tulbureala din josul-mediilor pentru un sunet mai curat, mai clar. |
| **Boxy** | Elimină un caracter cutiat, nazal din registrul mediu. |
| **Harsh** | Îmblânzește un vârf aspru, pătrunzător din susul-mediilor. |

### Peaking (bandă de EQ parametric)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Frequency** | Centrul benzii de amplificat sau tăiat. Baleiați-o pentru a găsi frecvența pe care doriți să o modelați. | 20 Hz până la 20 kHz (1 kHz) |
| **Gain** | Cât de mult să amplificați sau să tăiați la centru. Pozitiv ridică banda; negativ o scobește. | -15 până la +15 dB (0) |
| **Q factor** | Setează cât de largă este banda. Valorile mici modelează o zonă largă; valorile mari se îngustează pentru modificări chirurgicale, punctuale. | 0.1 până la 10 (1.0) |

| Presetare | Ce face |
|---|---|
| **Presence** | O ridicare largă în susul-mediilor pentru claritate și prezență. Un punct de plecare neutru. |
| **Warmth** | O amplificare largă în josul-mediilor care adaugă corp și căldură. |
| **Vocal Boost** | Ridică registrul vocal principal pentru a aduce vocile în față. |
| **Cut Mud** | Scobește tulbureala cutiată din josul-mediilor pentru un sunet mai curat. |
| **Tame Harsh** | O tăiere îngustă pentru a îmblânzi un vârf aspru, pătrunzător. |
| **Punch** | O amplificare joasă care adaugă impact și forță capătului de jos. |
| **Sub Boost** | O amplificare profundă chiar la bază pentru o greutate suplimentară de sub-bas. |
| **Air** | O ridicare largă la vârf pentru o strălucire deschisă, aerisită. |
| **Clarity** | Ridică susul-mediilor pentru a adăuga definiție și margine. |
| **De-Ess** | O tăiere îngustă în intervalul de sibilanță pentru a îmblânzi sunetele S aspre. |
| **De-Boom** | Taie o acumulare bubuitoare de frecvență joasă pentru un capăt de jos mai strâns. |
| **Scoop** | O scădere largă din registrul mediu pentru un ton scobit, modern. |

### Low Shelf (control al basului și amplificare a basului)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Frequency** | Setează colțul sub care intră în efect shelf-ul. Tot ce este sub el este amplificat sau tăiat împreună. | 20 până la 2000 Hz (200) |
| **Gain** | Cât de mult să ridicați sau să coborâți capătul de jos. Pozitiv adaugă greutate și căldură; negativ îl subțiază. | -15 până la +15 dB (0) |

| Presetare | Ce face |
|---|---|
| **Warmth** | O ridicare blândă a capătului de jos pentru căldură și corp. Un punct de plecare neutru. |
| **Bass Boost** | O amplificare solidă a basului pentru greutate și impact. |
| **Fullness** | Umple josul-mediilor pentru un sunet mai plin, mai rotund. |
| **Trim Bass** | O tăiere modestă pentru a ușura un mix cu bas greu. |
| **Cut Lows** | O tăiere puternică pentru a subția sau a de-bubui capătul de jos. |
| **Big Bottom** | O amplificare mare a capătului de jos pentru greutate și bubuit maxim. |

### High Shelf (control al înaltelor)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Frequency** | Setează colțul deasupra căruia intră în efect shelf-ul. Tot ce este peste el este amplificat sau tăiat împreună. | 1 până la 20 kHz (8 kHz) |
| **Gain** | Cât de mult să ridicați sau să coborâți capătul de sus. Pozitiv adaugă strălucire și aer; negativ netezește și întunecă. | -15 până la +15 dB (0) |

| Presetare | Ce face |
|---|---|
| **Presence** | O ridicare blândă a capătului de sus pentru claritate și detaliu. Un punct de plecare neutru. |
| **Air** | Deschide chiar vârful pentru un sunet aerisit, deschis. |
| **Bright** | O amplificare puternică pentru un ton tăios, luminos, în față. |
| **Soften** | O tăiere modestă pentru a lua din margine înaltelor aspre. |
| **Tame Highs** | O tăiere puternică pentru a întuneca și a netezi un sunet prea luminos. |
| **Sparkle** | O amplificare mare a capătului de sus pentru strălucire și scânteiere maximă. |

### Soft Clip (saturație caldă)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Drive** | Împinge semnalul mai tare în modelatorul de undă. Cantitățile mici adaugă căldură blândă; cele mari rotunjesc vârfurile într-o saturație groasă și asprime. | 0 până la 40 dB (0) |

| Presetare | Ce face |
|---|---|
| **Warm** | Un strop de drive pentru o căldură blândă, în stil analogic. |
| **Drive** | Saturație vizibilă care îngroașă și colorează sunetul. |
| **Crunch** | Drive greu cu o margine crocantă audibilă. |
| **Fuzz** | Distorsiune groasă, fuzz. Vârfurile sunt comprimate puternic. |
| **Destroy** | Drive maxim. Asprime agresivă, complet saturată. |

### Bit Crusher (lo-fi retro)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Bit depth** | Setează câți biți descriu fiecare eșantion. Mai puțini biți înseamnă pași mai grosolani și mai mult zgomot de cuantizare, pentru un sunet digital crocant, aspru. | 1 până la 16 biți (16) |
| **Sample rate** | Reduce frecvența de eșantionare a audio-ului. La o sută la sută rata este neatinsă; coborâți-o pentru a ține fiecare eșantion mai mult, estompând înaltele și adăugând o margine aspră, cu aliasing. | 1% până la 100% (100%) |

| Presetare | Ce face |
|---|---|
| **Vintage** | O scădere subtilă a calității, ca un sampler digital timpuriu. |
| **LoFi** | Clasicul lo-fi de 8 biți, la jumătate de rată. Granulos și retro. |
| **Crunch** | Comprimare mai grea cu o margine crocantă audibilă. |
| **Gritty** | Grosolan și aspru. Pașii dintre niveluri sunt evidenți. |
| **Destroy** | Reducere extremă. Aspru, spart, abia recognoscibil. |

### Ring Modulator (tonuri metalice și robotice)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Carrier** | Setează frecvența tonului cu care este înmulțit semnalul. Câțiva hertzi dau o oscilație de tremolo; frecvențele mai mari adaugă armonice metalice, de clopot și robotice. | 1 până la 4000 Hz (440) |
| **Mix** | Amestecă sunetul modulat cu originalul. La zero la sută auziți doar semnalul uscat; la o sută la sută doar tonul complet modulat. | 0% până la 100% (0%) |

| Presetare | Ce face |
|---|---|
| **Tremolo** | O purtătoare foarte joasă îl transformă într-un tremolo de amplitudine, oscilând volumul. |
| **Robot** | O purtătoare medie adaugă armonice metalice pentru un clasic efect de voce robotică. |
| **Metallic** | Armonice dense, inarmonice pentru un ton aspru, metalic. |
| **Bell** | O purtătoare mai înaltă dă un răsunet luminos, de clopot. |
| **Alien** | Complet umed cu o purtătoare înaltă. Extrem, extraterestru, abia recognoscibil. |

### Tremolo (oscilație de volum)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Rate** | Setează cât de repede pulsează volumul. Ratele mai lente dau o legănare fină; ratele mai rapide dau un tremur rapid. | 0.1 până la 20 Hz (5) |
| **Depth** | Setează cât de mult scade volumul la fiecare puls. La zero la sută nivelul este constant; la o sută la sută coboară până la tăcere. | 0% până la 100% (0%) |

| Presetare | Ce face |
|---|---|
| **Gentle** | O legănare lentă, superficială. Mișcare subtilă fără a atrage atenția. |
| **Classic** | Clasicul tremolo de amplificator: o rată medie și o adâncime moderată. |
| **Deep** | Un puls puternic, profund, care coboară aproape până la tăcere la fiecare ciclu. |
| **Fast** | Un tremur rapid pentru o senzație strălucitoare, nervoasă. |
| **Chop** | Rapid și cu adâncime completă. Un tremur dur, sacadat. |

### Delay (ecou)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Time** | Setează pauza înaintea fiecărui ecou. Timpii scurți dau un slapback strâns; timpii mai lungi distanțează repetările mai mult. | 0.01 până la 2 s (0.25) |
| **Feedback** | Setează cât din fiecare ecou este readus. Valorile mici dau o singură repetare; valorile mai mari construiesc o serie lungă de ecouri care se prelungește. | 0 până la 0.95 (0.4) |
| **Mix** | Amestecă ecourile cu originalul. La zero la sută auziți doar semnalul uscat; la o sută la sută doar ecourile. | 0% până la 100% (0%) |

| Presetare | Ce face |
|---|---|
| **Slapback** | Un singur ecou scurt, strâns lângă original. Dublare rockabilly și vocală. |
| **Echo** | Clasicul ecou: o repetare clară cu câteva cozi care se prelungesc. |
| **Ping** | O repetare rapidă, săltăreață, care adaugă mișcare ritmică. |
| **Ambient** | Repetări mai lungi, mai blânde, care se estompează într-o coadă spațioasă. |
| **Dub** | Feedback ridicat pentru cascade lungi, dub, de ecou. |
| **Cavern** | Repetări lungi, profunde, ca sunetul care răsună printr-un spațiu imens. |

### Stereo Width (îngustare sau lărgire)

| Control | Ce face | Interval (implicit) |
|---|---|---|
| **Width** | Îngustează sau lărgește imaginea stereo. Zero la sută colapsează la mono, o sută la sută o lasă neatinsă, iar valorile mai mari împing lateralele mai larg. Afectează doar piesele stereo pe ținta Toate canalele. | 0% până la 200% (100%) |

| Presetare | Ce face |
|---|---|
| **Wide** | O lărgire blândă care deschide imaginea stereo. Un punct de plecare neutru. |
| **Wider** | O răspândire mai puternică pentru un câmp stereo mare, imersiv. |
| **Max** | Lățime maximă. Foarte larg, dar atenție la problemele de compatibilitate mono. |
| **Narrow** | Trage lateralele înăuntru pentru o imagine mai strânsă, mai centrată. |
| **Focused** | Aproape centrat, cu doar un strop de stereo. |
| **Mono** | Complet colapsat la mono. Ambele difuzoare redau același semnal. |

## Cum funcționează totul în culise (versiunea simplă)

- **Motoare:** alegeți unul în Setări > Player audio > Motor de redare: **Standard** (sistem), **Universal** (FFmpeg) sau **Sound FX** (**motorul BASS™** de la [Un4seen Developments](https://www.un4seen.com/)). Motorul pe care îl alegeți decide ce formate se redau, iar efectele, egalizatorul și lanțul DSP rulează doar în motorul Sound FX.
- **Formate:** motorul BASS™ adaugă FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus și muzică modul (tracker) pe lângă formatele de sistem și FFmpeg.
- **Efecte:** egalizatorul, compressor-ul și majoritatea efectelor folosesc suplimentele de efecte BASS™. Freeverb este reverbul Freeverb. Chorus, Flanger și Distortion folosesc efecte clasice în stil DirectX cu propriile controale.
- **Normalizarea volumului:** un nivelator de intensitate **EBU R128** în timp real (standardul de intensitate folosit în difuzare și streaming).
- **Crossfeed:** crossfeed-ul **bs2b (Bauer)**, rulat în interiorul motorului BASS™.
- **Lanț DSP:** blocurile dumneavoastră personalizate, aplicate în ordinea exactă pe care o setați, pe toate canalele sau doar pe o parte.
- **Ieșire:** puteți seta frecvența de eșantionare, numărul de canale și dimensiunea bufferului pentru a se potrivi cu echipamentul dumneavoastră.

Deoarece toate acestea rulează în timp real în timp ce muzica se redă, efectele:

- Funcționează în **timp real** pe tot, inclusiv fișiere din cloud, fluxuri și muzică modul.
- **Nu modifică și nu re-salvează niciodată** fișierele dumneavoastră. Opriți un efect și originalul revine.
- **Rețin setările** pentru fiecare efect.
- Pot fi **combinate liber**, deoarece fiecare este separat.

## Rețete simple de încercat

**Ascultare de zi cu zi**

- **Mai mult bas, curat:** Egalizator > Bass Booster, apoi coborâți Preamplificatorul cu 1 până la 2 dB. Sau adăugați un Low Shelf DSP pe Bass Boost.
- **Volum uniform pe o listă mixtă:** Normalizarea volumului > Standard, plus Compressor > Soft.
- **Lustruire generală blândă:** Compressor > Transparent, plus Normalizarea volumului > Light.
- **Voci mai clare:** Egalizator > Vocal Booster, sau un bloc Peaking DSP pe Vocal Boost.
- **Sunet mai plin pe difuzoarele mici ale telefonului:** Egalizator > Small Speakers.

**Căști**

- **Mai plăcut, mai puțin obositor pe căști:** Crossfeed > Chu Moy sau Jan Meier.
- **Sunet mai larg pe căști:** Stereo Width DSP > Wide, plus Crossfeed > Chu Moy.
- **Corectarea discurilor puternic panoramate din anii 1960 și 1970:** Crossfeed > Vintage Stereo.
- **Puțin aer și spațiu:** Freeverb > Ambience, păstrat jos, plus Crossfeed > Subtle.

**Momente liniștite și audio vorbit**

- **Ascultare silențioasă de seară târziu:** Normalizarea volumului > Night, plus Compressor > Late Night.
- **Podcasturi și cărți audio:** Compressor > Voice / Podcast, plus Egalizator > Spoken Word.
- **Sunetul cel mai tare și mai uniform într-o mașină zgomotoasă:** Normalizarea volumului > Strong, plus Compressor > Heavy.

**Rezolvarea problemelor**

- **Îmblânzirea unei înregistrări aspre, luminoase:** Egalizator > Treble Reducer, sau un bloc Peaking DSP pe Tame Harsh.
- **Eliminarea zumzetului electric:** lanț DSP > Notch > Mains Hum 60 (sau Mains Hum 50 în Europa).
- **Bas mai strâns, mai curat:** DSP High Pass > Tighten, pentru a tăia capătul de jos bubuitor.
- **Mai puțin bubuit într-un mix cu bas greu:** DSP Low Shelf > Trim Bass, sau Peaking > De-Boom.

**Creativ și distractiv**

- **Senzație caldă, spațioasă:** Freeverb > Hall, păstrat jos.
- **Chitare visătoare, spațioase:** Chorus > Wide, plus Echo > Long.
- **Lo-fi retro:** lanț DSP > Bit Crusher (LoFi) în Soft Clip (Warm).
- **Mișcare funky pe piesele electronice:** Auto Wah > Funky, sau Phaser > Fast.
- **Clasicul baleiaj de avion cu reacție:** Flanger > Jet.

## Întrebări frecvente

{{% details title="Ce motor de sunet folosește Flacbox?" closed="true" %}}
Alegeți un singur Motor de redare în Setări > Player audio: Standard (motorul de sistem Apple), Universal (motorul FFmpeg) sau Sound FX (motorul BASS™ de la Un4seen Developments, un4seen.com). Motorul pe care îl alegeți decide ce formate de fișiere se redau. Sound FX este cel care redă formate suplimentare precum FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus și muzică MOD sau tracker și este singurul motor care oferă efectele în timp real, egalizatorul cu 10 benzi și lanțul DSP. Pentru a folosi efectele, setați Motorul de redare pe Sound FX.
{{% /details %}}

{{% details title="Poate Flacbox reda MOD, XM, IT și altă muzică tracker sau modul?" closed="true" %}}
Da. Motorul BASS™ are un player de module încorporat care încarcă fișiere MOD, XM, IT, S3M, MTM, UMX și MO3 și reconstruiește piesa în timp real din tiparele și sunetele de instrumente ale acesteia, așa cum este menită să se redea muzica tracker. Playerele obișnuite de iPhone nu pot face acest lucru. Efectele și egalizatorul funcționează și pe muzica modul.
{{% /details %}}

{{% details title="Acceptă Flacbox fișiere DSD și de înaltă rezoluție?" closed="true" %}}
Da. Flacbox redă fișiere DSD (DSF și DFF) prin motorul BASS™ folosind DSD peste PCM, astfel încât să funcționeze pe hardware de ieșire obișnuit, plus FLAC, WavPack, Monkey's Audio (APE), Musepack și TrueAudio pentru redare lossless.
{{% /details %}}

{{% details title="Ce efecte de sunet are Flacbox?" closed="true" %}}
Un egalizator cu 10 benzi, Normalizarea volumului, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate și Crossfeed, plus un lanț DSP pe care îl construiți singur, cu filtre, shelf-uri, gain, soft clip, bit crusher, ring modulator, tremolo, delay și stereo width. Fiecare este separat și poate fi combinat cu celelalte.
{{% /details %}}

{{% details title="Ce este o presetare?" closed="true" %}}
O presetare este o setare gata făcută pentru un efect. În loc să mișcați singur cursoarele, atingeți o presetare și sunetul se schimbă pentru a se potrivi. Fiecare efect din Flacbox are mai multe presetări, iar acest ghid enumeră ce face fiecare. Dacă mișcați un cursor după alegerea unei presetări, efectul afișează „Manual” pentru a vă spune că folosește acum propriile valori.
{{% /details %}}

{{% details title="Cum deschid efectele audio în Flacbox?" closed="true" %}}
Deschideți playerul Now Playing, atingeți butonul ⋯ (Mai multe) și alegeți Efecte audio. Sau mergeți la Setări > Player audio > Efecte audio. Atingeți un efect, porniți-i comutatorul și alegeți o presetare sau deschideți cursoarele pentru a regla fin.
{{% /details %}}

{{% details title="Unde este egalizatorul și care sunt cele mai bune setări?" closed="true" %}}
Mergeți la Setări > Player audio > Egalizator audio. Are 10 benzi de la 32 Hz la 16 kHz, fiecare de la -12 la +12 dB, plus un Preamplificator de la -24 la +24 dB și 22 de presetări. Pentru mai mult bas, folosiți Bass Booster. Pentru voci mai clare, folosiți Vocal Booster sau Pop. Pentru un sunet mai luminos, folosiți Treble Booster. Apoi ajustați benzile individuale după gust.
{{% /details %}}

{{% details title="Cum amplific basul în Flacbox?" closed="true" %}}
Două moduri ușoare. În Egalizatorul audio, alegeți Bass Booster (sau ridicați benzile de 32 Hz și 64 Hz cu câțiva dB). Sau, în Procesare semnal, adăugați un bloc Low Shelf setat pe Bass Boost. În ambele cazuri, coborâți Preamplificatorul sau adăugați un bloc Gain cu 1 până la 2 dB, astfel încât basul să rămână curat și să nu distorsioneze.
{{% /details %}}

{{% details title="Ce presetare de egalizator este cea mai bună pentru muzica mea?" closed="true" %}}
Rock și Electronic adaugă energie cu grave și înalte puternice. Acoustic, Jazz și Classical rămân calde și naturale. Pop și Vocal Booster împing vocile în față. Bass Booster și Hip-Hop adaugă greutate. Deep și Loudness sună mai plin la volum mic. Începeți cu cea care se potrivește genului dumneavoastră, apoi reglați fin.
{{% /details %}}

{{% details title="Ce este Normalizarea volumului și cu ce diferă de ReplayGain?" closed="true" %}}
Face ca fiecare piesă să se redea la aproximativ aceeași intensitate. Măsoară intensitatea reală folosind standardul EBU R128 (în LUFS, ca serviciile de streaming) și ajustează fiecare piesă către ținta dumneavoastră, cu o limită de amplificare maximă. Spre deosebire de ReplayGain, nu are nevoie de etichete în fișiere și funcționează pe orice sursă, în timp real, fără a modifica sunetul. Presetări: Light, Standard, Strong și Night.
{{% /details %}}

{{% details title="Ce este Crossfeed și ar trebui să îl folosesc?" closed="true" %}}
Crossfeed amestecă puțin din canalele stânga și dreapta împreună, astfel încât căștile să pară mai mult ca niște difuzoare reale și mai puțin ca și cum sunetul ar fi blocat în capul dumneavoastră. Este doar pentru căști, așa că opriți-l pentru difuzoare. Flacbox folosește metoda bs2b (Bauer), cu presetări precum Chu Moy și Jan Meier.
{{% /details %}}

{{% details title="Care este diferența dintre Compressor și Normalizarea volumului?" closed="true" %}}
Normalizarea volumului potrivește intensitatea între piese diferite. Compressor-ul uniformizează părțile tari și silențioase din interiorul unei singure piese. Rezolvă probleme diferite și funcționează bine împreună, mai ales într-o mașină sau într-un loc zgomotos.
{{% /details %}}

{{% details title="Ce este lanțul de Procesare semnal (DSP)?" closed="true" %}}
Este un rack pe care îl construiți singur în Setări > Player audio > Procesare semnal. Adăugați blocuri precum filtre, shelf-uri, gain, soft clip, bit crusher, ring modulator, tremolo, delay și stereo width, puneți-le în orice ordine, porniți sau opriți fiecare și îndreptați lanțul către toate canalele, stânga sau dreapta. Deoarece ordinea contează, puteți proiecta exact sunetul pe care îl doriți.
{{% /details %}}

{{% details title="Care este diferența dintre Egalizator, efecte și lanțul DSP?" closed="true" %}}
Egalizatorul este un control simplu de tonalitate cu 10 benzi. Efectele audio sunt instrumente gata făcute (compressor, reverb, echo și așa mai departe) cu presetări. Lanțul DSP este locul unde vă construiți propria ordine de efecte din blocuri individuale. Puteți rula toate trei în același timp.
{{% /details %}}

{{% details title="Efectele modifică sau deteriorează fișierele mele de muzică?" closed="true" %}}
Nu. Totul se aplică în timp real în timp ce muzica se redă. Fișierele dumneavoastră nu sunt niciodată modificate sau re-salvate. Opriți un efect și sunetul original revine pe loc.
{{% /details %}}

{{% details title="Pot folosi mai mult de un efect în același timp?" closed="true" %}}
Da. Fiecare efect are propriul comutator și nu există un comutator principal, așa că orice combinație funcționează. De exemplu, Normalizarea volumului plus Compressor pentru o ascultare uniformă, sau Freeverb plus Crossfeed pe căști, cu egalizatorul deasupra.
{{% /details %}}

{{% details title="De ce sunt controalele efectului estompate?" closed="true" %}}
Efectul este oprit. Porniți-i comutatorul din partea de sus a editorului pentru a folosi controalele. Fiecare efect este oprit implicit.
{{% /details %}}

{{% details title="Ce înseamnă eticheta Manual?" closed="true" %}}
Înseamnă că ați mișcat un cursor departe de o presetare, așa că efectul folosește acum propriile valori personalizate în loc de o presetare denumită. Fiecare cursor are un buton de resetare, iar alegerea din nou a unei presetări înlocuiește valorile dumneavoastră manuale.
{{% /details %}}

{{% details title="Pot salva și partaja presetările mele de egalizator?" closed="true" %}}
Da. Pe lângă cele 22 de presetări încorporate, vă puteți crea propriile, le puteți reordona și le puteți exporta sau importa pentru a vă muta setările pe alt dispozitiv.
{{% /details %}}

{{% details title="Funcționează efectele cu CarPlay, streaming și redare în fundal?" closed="true" %}}
Da. Efectele rulează în interiorul motorului BASS™, așa că se aplică fișierelor locale, unităților din cloud, serverelor media, fluxurilor și muzicii modul și continuă să funcționeze în timpul CarPlay și al redării în fundal.
{{% /details %}}

{{% details title="Pot schimba calitatea ieșirii audio?" closed="true" %}}
Da. În Setări > Player audio puteți seta frecvența de eșantionare a ieșirii, numărul de canale și dimensiunea bufferului pentru a se potrivi cu căștile, difuzoarele sau DAC-ul dumneavoastră.
{{% /details %}}

{{% details title="Care este o configurație bună de pornire pentru căști?" closed="true" %}}
Porniți Normalizarea volumului (Standard), adăugați un Compressor ușor (Soft), alegeți o presetare de egalizator care vă place și porniți Crossfeed (Chu Moy sau Jan Meier). Lăsați reverbul, echo-ul și distorsiunea oprite dacă nu doriți un sunet creativ.
{{% /details %}}

---

*BASS este o marcă comercială a Un4seen Developments Ltd. Vedeți [un4seen.com](https://www.un4seen.com/). Crossfeed folosește algoritmul bs2b (Bauer stereophonic-to-binaural); vedeți [pagina proiectului bs2b](https://bs2b.sourceforge.net/).*
