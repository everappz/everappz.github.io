---
title: "Evermusic 8.7: redare fără pauze reală, efecte audio, normalizarea volumului, egalizator reproiectat"
date: 2026-07-05
description: "Evermusic 8.7 pentru iPhone, iPad și Mac adaugă redare fără pauze reală, cinci efecte audio de studio (reverb, delay, distorsiune, compresor, crossfeed), normalizarea volumului EBU R128, un egalizator cu 10 benzi reproiectat cu import/export de preseturi, un motor de streaming AVAudioEngine reconstruit cu suport pentru FLAC și Ogg Vorbis, plus CarPlay și Se redă acum mai rapide și mai precise."
keywords: ["Evermusic 8.7", "actualizare Evermusic", "redare fără pauze reală iPhone", "player muzică fără pauze iOS", "redare fără pauze CarPlay", "efecte audio player muzică iPhone", "reverb delay distorsiune compresor crossfeed iOS", "crossfeed căști iOS", "normalizarea volumului iPhone", "normalizarea intensității sonore player muzică", "normalizare EBU R128 iOS", "alternativă la replay gain iPhone", "egalizator cu 10 benzi iPhone", "egalizator grafic aplicație iOS", "import export preseturi egalizator", "player FLAC iPhone", "player Ogg Vorbis iOS", "player muzică lossless iPhone 2026", "player muzică AVAudioEngine", "player muzică CarPlay iPhone", "precizie Se redă acum ecran blocat", "player muzică în cloud iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Redare fără pauze", "Efecte audio", "Reverb", "Delay", "Distorsiune", "Compresor", "Crossfeed", "Normalizarea volumului", "EBU R128", "Egalizator", "FLAC", "Ogg Vorbis", "CarPlay", "Se redă acum", "Liquid Glass", "Noutăți"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Pe scurt:** [Evermusic 8.7](/products/evermusic) este o versiune axată pe calitatea sunetului pentru iPhone, iPad și Mac. Aduce **redare fără pauze reală** (fără pauze, clicuri sau pârâituri între piese), un set complet de **efecte audio de studio** — reverb, delay, distorsiune, compresor și crossfeed — și **normalizarea volumului EBU R128** care menține intensitatea sonoră constantă de la o melodie la alta fără etichete ReplayGain. **Egalizatorul cu 10 benzi** este reproiectat cu glisoare noi, comutare mai rapidă a preseturilor, preseturi personalizate pe care le poți importa și exporta, și un aspect mai bun în modul peisaj și pe iPad. În profunzime, un **motor de streaming AVAudioEngine reconstruit** îmbunătățește fiabilitatea și suportul pentru formate, inclusiv **FLAC** și **Ogg Vorbis**. **CarPlay** și **Se redă acum** sunt mai rapide și mai precise pe ecranul blocat, în mașină și de la telecomenzile căștilor.

---

## Salutare tuturor!

Evermusic 8.7 este disponibil pentru descărcare. Această actualizare este despre cum *sună* muzica ta. Am reconstruit motorul de redare pentru o redare fără pauze reală, am adăugat o suită de efecte audio de nivel de studio, am introdus normalizarea intensității sonore și am reproiectat egalizatorul de la glisoare în sus. Totul este învelit în noul design **Liquid Glass** de la Apple.

[Descarcă Evermusic 8.7 din App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) sau actualizează din versiunea ta existentă. Evermusic este o descărcare gratuită, cu upgrade-uri opționale în aplicație.

## Redare fără pauze reală

Redarea fără pauze înseamnă că liniștea dintre două piese a dispărut. Fără pauză, fără clic, fără pârâit — melodia curentă curge direct în următoarea. Contează cel mai mult pentru muzica concepută pentru a fi ascultată ca un tot: **înregistrări live, mixuri DJ, lucrări clasice și albume conceptuale** în care o piesă se estompează direct în alta.

Iată ce s-a schimbat tehnic. Motorul audio al Evermusic menține două piese în redare în același timp: cea pe care o auzi și următoarea din listă. În timp ce piesa curentă se redă, următoarea este deja **descărcată, decodată și pre-încărcată în buffer** în fundal. Când piesa curentă ajunge la sfârșit, motorul face trecerea la piesa următoare **în interiorul playerului, nu în interiorul fluxului audio**. Bucla de randare a ieșirii continuă să extragă eșantioane audio dintr-un buffer inelar continuu fără să se oprească vreodată, așa că ascultătorul nu aude niciodată o graniță. Comutarea are loc între eșantioane, exact de aceea nu există niciun gol audibil.

Acest lucru funcționează la fel indiferent dacă fișierul este pe dispozitivul tău, în cloud sau pe un server media — pre-încărcarea în buffer începe doar puțin mai devreme pentru sursele la distanță.

## Efecte audio de studio

Evermusic 8.7 adaugă cinci efecte audio în timp real pe care le poți suprapune peste muzica ta. Fiecare rulează ca un nod nativ de procesare audio în motorul de redare, așa că se aplică la tot ce redai — fișiere locale, fluxuri din cloud și radio pe internet deopotrivă — fără recodare.

Fiecare efect vine cu o **bibliotecă selectată de preseturi** pentru a-ți oferi un sunet excelent cu o singură apăsare, iar Evermusic **reține setările tale exacte** între sesiuni. Ajustează orice comandă și efectul comută în starea **Manual**, așa că știi mereu când te-ai îndepărtat de un preset.

### Reverb

Adaugă un sentiment de spațiu, de la o cameră strâmtă la o catedrală. Construit pe `AVAudioUnitReverb` de la Apple, oferă **13 preseturi de încăpere** (Cameră mică, Sală medie, Plate, Catedrală și altele), plus o comandă de **mix wet/dry** de la 0 la 100%, astfel încât tu decizi cât spațiu adaugi.

### Delay (ecou)

Un ecou clasic cu **10 preseturi** — Slapback, Ecou de bandă, Dub, Ambiental și altele. Poți regla **timpul de delay** (până la 2 secunde), **feedback**-ul (câte repetări), o **tăiere trece-jos** pentru a încălzi repetările și **mix**-ul wet/dry.

### Distorsiune

De la asprime subtilă la distrugere lo-fi completă, condusă de `AVAudioUnitDistortion` cu **22 de preseturi de caracter** (Bit Brush, Cellphone Concert, Radio Tower și altele), o comandă de drive **pre-amplificare** și un mix wet/dry, ca să poți amesteca efectul înapoi în semnalul curat.

### Compresor

Un procesor de dinamică (`AUDynamicsProcessor` de la Apple) care echilibrează pasajele tari și slabe. Expune setul complet de comenzi profesionale — **prag, raport/rezervă, atac, eliberare, expansiune și amplificare de compensare** — cu **10 preseturi** reglate pentru situații reale: Voce / Podcast, Târziu în noapte, Dialog de film, Potrivire streaming și Intensitate sonoră maximă, printre altele.

### Crossfeed

Crossfeed face ascultarea la căști să sune mai natural amestecând puțin din canalul stâng în cel drept și invers, așa cum urechile tale aud difuzoare reale. Este construit pe binecunoscutul algoritm **Bauer stereophonic-to-binaural (bs2b)**, cu control asupra **nivelului de crossfeed** și a **frecvenței de tăiere**, și **6 preseturi**, inclusiv setările favorite ale audiofililor *Chu Moy* și *Jan Meier*. Este deosebit de bun pe mixajele stereo mai vechi, cu panoramare extremă, din anii 1960 și 1970.

## Normalizarea volumului

Ai construit vreodată un playlist în care o piesă bubuie, iar următoarea este o șoaptă? Normalizarea volumului rezolvă asta. Evermusic 8.7 folosește **măsurarea intensității sonore EBU R128** (același standard ITU-R BS.1770 folosit în difuzare și de serviciile de streaming) pentru a măsura intensitatea sonoră reală percepută a fiecărei piese și a o dirija ușor către o țintă constantă.

Spre deosebire de ReplayGain, **nu** necesită etichete în fișierele tale și **nu** modifică sunetul. Funcționează în timp real pe orice redai, inclusiv fluxuri din cloud și radio live, și se resetează curat când derulezi sau schimbi piesele.

Patru preseturi acoperă cazurile comune:

- **Ușor** — nivelare blândă (țintă −20 LUFS).
- **Standard** — cel implicit, intensitate sonoră în stil streaming (țintă −16 LUFS, până la +12 dB de amplificare pentru piesele slabe).
- **Puternic** — potrivire agresivă pentru biblioteci foarte variate (țintă −14 LUFS).
- **Nocturn** — mai liniștit și constant pentru ascultare serală la volum redus (țintă −23 LUFS).

Nu mai trebuie să ajustezi volumul între melodii.

## Egalizator reproiectat

**Egalizatorul grafic cu 10 benzi** al Evermusic a primit o reproiectare completă. Benzile acoperă de la **32 Hz la 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), fiecare reglabilă de la **−12 dB la +12 dB** în pași fini de 0,1 dB, cu un **preamp** de la −24 dB la +24 dB pentru a preveni clipping-ul când amplifici.

Ce este nou în 8.7:

- **Glisoare noi** — comenzi precise și receptive care adoptă aspectul glisorului nativ al sistemului iOS 26 și materialul **Liquid Glass**.
- **Comutare a preseturilor mai rapidă și mai fluidă** — sari între preseturi instantaneu, cu o bară de preseturi orizontală reproiectată în modul portret și o coloană de preseturi verticală în modul peisaj.
- **Aspect mai bun în modul peisaj și pe iPad** — glisoarele și selectorul de preseturi se rearanjează pentru a folosi lățimea suplimentară, în loc să se înghesuie într-o coloană de dimensiunea unui telefon.
- **Preseturi personalizate** — creează și salvează propriile curbe, reordonează-le și **importă și exportă** preseturi ca fișiere `.eqp` pentru a le muta între dispozitive sau a le partaja.

Egalizatorul rulează nativ în motor (`AVAudioUnitEQ`), așa că se aplică la fiecare sursă și funcționează, de asemenea, prin AirPlay, Chromecast și CarPlay unde este acceptat.

## Motor de redare reconstruit

În profunzime, Evermusic 8.7 rulează pe un **motor de streaming reconstruit** bazat pe `AVAudioEngine` de la Apple cu un pipeline de randare personalizat. Acesta este ceea ce face posibile trecerea fără pauze, lanțul de efecte și egalizatorul și, de asemenea, face redarea de zi cu zi mai fiabilă.

- **Suport îmbunătățit pentru formate** — inclusiv **FLAC** (prin Core Audio) și **Ogg Vorbis** (prin `libvorbisfile`), alături de MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF și altele.
- **Buffering mai inteligent** — un pre-buffer adaptiv se scalează cu conexiunea ta, cu un buffer inelar continuu care alimentează ieșirea, astfel încât micile sughițuri de rețea să nu se transforme în întreruperi.
- **Recuperare automată** — o mașină de stări de rebuffering și o logică de reîncercare cu temporizare reiau redarea curat după un moment de semnal slab, în loc să oprească piesa.
- **Mai puține întreruperi** — același motor conduce fișiere locale, fluxuri din cloud, servere media și radio pe internet, așa că comportamentul este constant peste tot.

## Se redă acum și CarPlay

Ecranele la care te uiți efectiv în timp ce asculți — **ecranul blocat**, **CarPlay** și butoanele de telecomandă ale mașinii sau ale căștilor — sunt mai precise și mai rapide în 8.7.

- **Informații Se redă acum mai precise.** Evermusic captează starea playerului sub un blocaj înainte de a o publica, astfel încât titlul, timpul scurs, durata și starea de redare/pauză nu pot fi niciodată în dezacord între ele pe ecranul blocat sau în mașină. Stările de buffering și încărcare sunt acum raportate corect, în loc să afișeze „se redă" în timp ce o piesă este încă descărcată.
- **Comenzi la distanță fiabile.** Redare, pauză, următoarea, anterioara, derulare, sărire, aleatoriu, repetare și viteza de redare răspund constant de la butoanele căștilor, comenzile mașinii și ecranul blocat, conduse de `MPRemoteCommandCenter`.
- **Coperți CarPlay mai rapide.** Coperțile de album se încarcă acum de câteva ori mai rapid pe listele lungi (ritmul pe loturi redus de la 1,0 s la 0,25 s, primul ecran vizibil încărcându-se imediat), și acum apar în rândurile compacte de listă CarPlay din iOS 26 care anterior nu afișau nicio copertă.
- **Corecții de sortare și stabilitate CarPlay.** Sortare mai rapidă pe bibliotecile mari și protecție împotriva blocărilor în cazuri extreme la derularea listelor lungi.
- **Actualizări de metadate limitate.** Actualizările Se redă acum și ale comenzilor la distanță sunt limitate, astfel încât schimbările rapide să nu mai inunde sistemul, ceea ce menține comenzile de pe ecranul blocat și CarPlay receptive.

## Alte îmbunătățiri

- **Rafinamente ale designului Liquid Glass** în toată aplicația — suprafețe translucide, animații mai fluide și comenzi rafinate pe iOS, iPadOS și macOS.
- **Noi widgeturi pentru ecranul principal** cu logică de actualizare îmbunătățită care le menține sincronizate fără a consuma baterie suplimentară.
- Corecții pentru versiunile recente de iOS.
- Corecții de localizare în mai multe limbi.
- Multe îmbunătățiri mai mici bazate pe e-mailurile voastre și recenziile din App Store.

## De ce contează această actualizare

Evermusic 8.7 este construit în jurul unei singure idei: **muzica ta ar trebui să sune cât mai bine, din orice sursă.**

1. **Albume întregi, așa cum au fost gândite.** Redarea fără pauze reală înseamnă că seturile live, mixurile DJ și albumele conceptuale se redau în sfârșit așa cum le-a masterizat artistul.
2. **Un studio în buzunarul tău.** Reverb, delay, distorsiune, compresor, crossfeed, un egalizator reproiectat și normalizarea intensității sonore îți oferă control real asupra sunetului, nu doar un comutator pornit/oprit.
3. **Aceeași experiență peste tot.** Fișiere locale, drive-uri în cloud, servere media și radio pe internet trec toate prin același motor reconstruit, cu un Se redă acum precis și un CarPlay mai rapid deasupra.

## Obține Evermusic 8.7

[**Descarcă Evermusic din App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) sau actualizează din interiorul App Store. Evermusic este o descărcare gratuită, cu upgrade-uri opționale în aplicație pentru funcții avansate.

Dacă îți place aplicația, te rugăm să lași o evaluare în App Store — chiar ajută. Ai vreo părere sau ai întâmpinat o problemă? Scrie-ne la **support@everappz.com**. Citim fiecare mesaj.

## Întrebări frecvente

{{% details title="Ce este nou în Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 adaugă redare fără pauze reală, cinci efecte audio de studio (reverb, delay, distorsiune, compresor și crossfeed), normalizarea volumului EBU R128, un egalizator cu 10 benzi reproiectat cu preseturi personalizate și import/export, un motor de streaming AVAudioEngine reconstruit cu suport îmbunătățit pentru formate (inclusiv FLAC și Ogg Vorbis), CarPlay și Se redă acum mai rapide și mai precise, actualizări ale designului Liquid Glass, widgeturi reîmprospătate pentru ecranul principal și corecții de erori și de localizare.
{{% /details %}}

{{% details title="Are Evermusic redare fără pauze reală?" closed="true" %}}
Da. Începând cu Evermusic 8.7, redarea este cu adevărat fără pauze: nu există pauză, clic sau pârâit între piese. Motorul pre-încarcă în buffer și decodează piesa următoare în timp ce cea curentă se redă și face trecerea între eșantioane audio pe un buffer inelar continuu, astfel încât tranziția este inaudibilă. Funcționează cu fișiere locale, fluxuri din cloud și servere media și este ideală pentru albume live, mixuri DJ și albume conceptuale.
{{% /details %}}

{{% details title="Ce efecte audio include Evermusic 8.7?" closed="true" %}}
Cinci efecte în timp real: **reverb** (13 preseturi de încăpere, mix wet/dry), **delay/ecou** (10 preseturi cu timp de delay, feedback, trece-jos și mix), **distorsiune** (22 de preseturi de caracter cu pre-amplificare și mix), **compresor** (un procesor de dinamică complet cu prag, raport, atac, eliberare, expansiune și amplificare de compensare, plus 10 preseturi) și **crossfeed** (crossfeed pentru căști Bauer bs2b cu comenzi de nivel și tăiere și 6 preseturi). Fiecare efect vine cu preseturi selectate, iar setările tale personalizate sunt reținute între sesiuni.
{{% /details %}}

{{% details title="Ce este crossfeed și de ce l-aș folosi?" closed="true" %}}
Crossfeed amestecă o cantitate mică, filtrată din fiecare canal stereo în celălalt, așa cum urechile tale aud în mod natural difuzoare reale într-o cameră. La căști, acest lucru reduce separarea exagerată, „în cap", a înregistrărilor cu panoramare extremă și face ascultarea îndelungată mai confortabilă. Evermusic folosește binecunoscutul algoritm Bauer stereophonic-to-binaural (bs2b) și include preseturi precum Chu Moy și Jan Meier. Este deosebit de eficient pe mixajele stereo mai vechi din anii 1960 și 1970.
{{% /details %}}

{{% details title="Cum funcționează normalizarea volumului în Evermusic?" closed="true" %}}
Evermusic 8.7 măsoară intensitatea sonoră percepută a fiecărei piese folosind standardul EBU R128 (ITU-R BS.1770) în timp real și ajustează ușor nivelul către o țintă constantă, astfel încât piesele să nu sară în volum. Nu necesită etichete ReplayGain și nu îți modifică fișierele. Sunt disponibile patru preseturi — Ușor (−20 LUFS), Standard (−16 LUFS), Puternic (−14 LUFS) și Nocturn (−23 LUFS) — iar normalizarea se resetează curat când derulezi sau schimbi piesele.
{{% /details %}}

{{% details title="Normalizarea volumului din Evermusic este același lucru cu ReplayGain?" closed="true" %}}
Atinge același scop — intensitate sonoră constantă între piese — dar funcționează diferit. ReplayGain se bazează pe etichete de intensitate sonoră stocate în fișierele tale. Normalizatorul Evermusic măsoară intensitatea sonoră live folosind EBU R128, așa că funcționează pe orice sursă, inclusiv fluxuri din cloud și radio pe internet, chiar și când fișierele nu au deloc etichete.
{{% /details %}}

{{% details title="Câte benzi are egalizatorul Evermusic și pot crea propriile preseturi?" closed="true" %}}
Egalizatorul Evermusic este un egalizator grafic cu 10 benzi care acoperă de la 32 Hz la 16 kHz, cu fiecare bandă reglabilă de la −12 dB la +12 dB în pași de 0,1 dB și un preamp de la −24 dB la +24 dB. Include preseturi integrate, îți permite să creezi și să salvezi preseturi personalizate și acceptă importul și exportul preseturilor ca fișiere .eqp, astfel încât să le poți muta sau partaja între dispozitive.
{{% /details %}}

{{% details title="Ce s-a schimbat la egalizatorul Evermusic 8.7?" closed="true" %}}
Egalizatorul a fost reproiectat cu glisoare noi, mai precise, care adoptă aspectul glisorului sistemului iOS 26 și Liquid Glass, comutare a preseturilor mai rapidă și mai fluidă, și un aspect mai bun în modul peisaj și pe iPad (o bară de preseturi orizontală în modul portret și o coloană de preseturi verticală în modul peisaj). Sunt acceptate preseturi personalizate și import/export .eqp.
{{% /details %}}

{{% details title="Evermusic 8.7 acceptă FLAC și Ogg Vorbis?" closed="true" %}}
Da. Motorul reconstruit redă FLAC (prin Core Audio) și Ogg Vorbis (prin libvorbisfile), alături de MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF și altele, din fișiere locale, drive-uri în cloud și servere media.
{{% /details %}}

{{% details title="Ce s-a îmbunătățit la CarPlay și pe ecranul blocat?" closed="true" %}}
Coperțile de album CarPlay se încarcă de câteva ori mai rapid pe listele lungi și apar acum în rândurile compacte de listă din iOS 26 care anterior nu afișau niciuna. Informațiile Se redă acum de pe ecranul blocat și din CarPlay sunt mai precise — titlul, timpul scurs, durata și starea de redare/pauză sunt captate împreună, astfel încât să nu poată fi în dezacord, iar stările de buffering sunt raportate corect. Comenzile la distanță (redare, pauză, următoarea, anterioara, derulare, aleatoriu, repetare, viteză) răspund fiabil de la căști și din mașină, iar sortarea CarPlay pe bibliotecile mari este mai rapidă.
{{% /details %}}

{{% details title="Efectele audio și egalizatorul funcționează cu streaming din cloud și CarPlay?" closed="true" %}}
Da. Efectele, egalizatorul și normalizarea volumului rulează nativ în interiorul motorului de redare, așa că se aplică la tot ce redă Evermusic — fișiere locale, drive-uri în cloud, servere media și radio pe internet — și continuă să funcționeze în timpul redării prin CarPlay și, unde este acceptat, prin AirPlay și Chromecast.
{{% /details %}}

{{% details title="Actualizarea la Evermusic 8.7 este gratuită și ce dispozitive acceptă?" closed="true" %}}
Da. Evermusic este o descărcare gratuită din App Store, iar 8.7 este o actualizare gratuită pentru utilizatorii existenți, cu upgrade-uri opționale în aplicație pentru funcții avansate. Rulează pe iPhone, iPad și Mac. CarPlay necesită un vehicul sau o unitate centrală compatibilă cu CarPlay.
{{% /details %}}
