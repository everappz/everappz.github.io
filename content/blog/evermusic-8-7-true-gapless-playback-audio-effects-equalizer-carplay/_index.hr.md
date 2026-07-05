---
title: "Evermusic 8.7: prava reprodukcija bez pauza, audio efekti, normalizacija glasnoće, redizajnirani ekvilajzer"
date: 2026-07-05
description: "Evermusic 8.7 za iPhone, iPad i Mac dodaje pravu reprodukciju bez pauza, pet studijskih audio efekata (reverb, delay, distorziju, kompresor, crossfeed), normalizaciju glasnoće EBU R128, redizajnirani 10-pojasni ekvilajzer s uvozom/izvozom predložaka, ponovno izrađen AVAudioEngine streaming mehanizam s podrškom za FLAC i Ogg Vorbis te brži i točniji CarPlay i Sada svira."
keywords: ["Evermusic 8.7", "Evermusic ažuriranje", "prava reprodukcija bez pauza iPhone", "gapless glazbeni player iOS", "gapless reprodukcija CarPlay", "audio efekti glazbeni player iPhone", "reverb delay distorzija kompresor crossfeed iOS", "crossfeed slušalice iOS", "normalizacija glasnoće iPhone", "normalizacija glasnoće glazbeni player", "EBU R128 normalizacija iOS", "ReplayGain alternativa iPhone", "10-pojasni ekvilajzer iPhone", "grafički ekvilajzer iOS aplikacija", "uvoz izvoz predložaka ekvilajzera", "FLAC player iPhone", "Ogg Vorbis player iOS", "bezgubitni glazbeni player iPhone 2026", "AVAudioEngine glazbeni player", "CarPlay glazbeni player iPhone", "točnost Sada svira zaključani zaslon", "cloud glazbeni player iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Reprodukcija bez pauza", "Audio efekti", "Reverb", "Delay", "Distorzija", "Kompresor", "Crossfeed", "Normalizacija glasnoće", "EBU R128", "Ekvilajzer", "FLAC", "Ogg Vorbis", "CarPlay", "Sada svira", "Liquid Glass", "Novosti"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Ukratko:** [Evermusic 8.7](/products/evermusic) izdanje je usmjereno na kvalitetu zvuka za iPhone, iPad i Mac. Donosi **pravu reprodukciju bez pauza** (bez pauza, klikova ili tiktaka između pjesama), potpun skup **studijskih audio efekata** — reverb, delay, distorziju, kompresor i crossfeed — te **normalizaciju glasnoće EBU R128** koja održava glasnoću dosljednom od pjesme do pjesme bez ReplayGain oznaka. **10-pojasni ekvilajzer** redizajniran je s novim klizačima, bržim prebacivanjem predložaka, prilagođenim predlošcima koje možete uvoziti i izvoziti te boljim rasporedom u pejzažnoj orijentaciji i na iPadu. Ispod haube, **ponovno izrađen AVAudioEngine streaming mehanizam** poboljšava pouzdanost i podršku za formate, uključujući **FLAC** i **Ogg Vorbis**. **CarPlay** i **Sada svira** brži su i točniji na zaključanom zaslonu, u autu i s daljinskih upravljača slušalica.

---

## Pozdrav svima!

Evermusic 8.7 dostupan je za preuzimanje. Ovo ažuriranje u potpunosti je o tome kako vaša glazba *zvuči*. Ponovno smo izradili mehanizam za reprodukciju radi prave reprodukcije bez pauza, dodali skup audio efekata studijske kvalitete, uveli normalizaciju glasnoće i redizajnirali ekvilajzer od klizača naviše. Sve je omotano u Appleov novi dizajn **Liquid Glass**.

[Preuzmite Evermusic 8.7 s App Storea](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) ili ažurirajte s postojeće verzije. Evermusic je besplatno preuzimanje s opcionalnim nadogradnjama unutar aplikacije.

## Prava reprodukcija bez pauza

Reprodukcija bez pauza znači da je tišina između dvije pjesme nestala. Bez pauze, bez klika, bez tiktaka — trenutna pjesma prelazi izravno u sljedeću. Najviše je važna za glazbu koja je osmišljena da se sluša kao cjelina: **live snimke, DJ mixeve, klasična djela i koncept albume** gdje jedna pjesma izblijedi izravno u drugu.

Evo što se tehnički promijenilo. Evermusicov audio mehanizam drži dvije pjesme u reprodukciji istovremeno: onu koju čujete i sljedeću u redu. Dok trenutna pjesma svira, sljedeća se već **dohvaća, dekodira i unaprijed pohranjuje u međuspremnik** u pozadini. Kad trenutna pjesma dođe do kraja, mehanizam predaje reprodukciju sljedećoj pjesmi **unutar playera, a ne unutar audio toka**. Petlja renderiranja izlaza nastavlja povlačiti audio uzorke iz neprekinutog kružnog međuspremnika (ring buffer) bez ikakvog zaustavljanja, pa slušatelj nikad ne čuje prijelaz. Prebacivanje se događa između uzoraka, što je upravo razlog zašto nema čujne pauze.

To radi jednako bez obzira je li datoteka na vašem uređaju, u oblaku ili na medijskom poslužitelju — unaprijedno pohranjivanje u međuspremnik jednostavno počinje malo ranije za udaljene izvore.

## Studijski audio efekti

Evermusic 8.7 dodaje pet audio efekata u stvarnom vremenu koje možete naslagati na svoju glazbu. Svaki se pokreće kao izvorni čvor za audio obradu u mehanizmu za reprodukciju, pa se primjenjuje na sve što reproducirate — lokalne datoteke, streamove iz oblaka i internetski radio — bez ponovnog kodiranja.

Svaki efekt dolazi s **pomno biranom bibliotekom predložaka** kako biste jednim dodirom dobili sjajan zvuk, a Evermusic **pamti vaše točne postavke** između sesija. Podesite bilo koju kontrolu i efekt se prebacuje u stanje **Ručno**, pa uvijek znate kada ste odstupili od predloška.

### Reverb

Dodaje osjećaj prostora, od uske sobe do katedrale. Izrađen na Appleovom `AVAudioUnitReverb`, nudi **13 predložaka prostora** (Mala soba, Srednja dvorana, Plate, Katedrala i drugi) te kontrolu **miješanja wet/dry** od 0 do 100% tako da vi odlučujete koliko prostora dodati.

### Delay (jeka)

Klasična jeka s **10 predložaka** — Slapback, Vrpčana jeka, Dub, Ambijentalan i drugi. Možete namjestiti **vrijeme kašnjenja** (do 2 sekunde), **povratnu vezu** (koliko ponavljanja), **niskopropusnu graničnu frekvenciju** za zagrijavanje ponavljanja i **miješanje wet/dry**.

### Distorzija

Od suptilne hrapavosti do potpunog lo-fi razaranja, pogonjena `AVAudioUnitDistortion`-om s **22 predloška s karakterom** (Bit Brush, Cellphone Concert, Radio Tower i drugi), kontrolom pogona **predpojačanja** i miješanjem wet/dry kako biste efekt vratili u čisti signal.

### Kompresor

Procesor dinamike (Appleov `AUDynamicsProcessor`) koji izjednačuje glasne i tihe dionice. Izlaže potpun profesionalni skup kontrola — **prag, omjer/rezervu, napad, otpuštanje, ekspanziju i kompenzacijsko pojačanje** — s **10 predložaka** ugođenih za stvarne situacije: Glas / Podcast, Kasna noć, Filmski dijalog, Usklađen sa streamingom i Najveća glasnoća među njima.

### Crossfeed

Crossfeed čini slušanje na slušalicama prirodnijim miješanjem malo lijevog kanala u desni i obrnuto, onako kako vaše uši čuju prave zvučnike. Izrađen je na dobro poznatom algoritmu **Bauer stereophonic-to-binaural (bs2b)**, s kontrolom nad **razinom crossfeeda** i **graničnom frekvencijom** te **6 predložaka** uključujući postavke *Chu Moy* i *Jan Meier*, miljenike audiofila. Osobito je dobar na starijim stereo miksevima iz 1960-ih i 1970-ih s oštrom panoramom.

## Normalizacija glasnoće

Jeste li ikad složili playlistu u kojoj jedna pjesma tutnji, a sljedeća je šapat? Normalizacija glasnoće to rješava. Evermusic 8.7 koristi **mjerenje glasnoće EBU R128** (isti standard ITU-R BS.1770 koji se koristi u emitiranju i kod streaming usluga) za mjerenje stvarne percipirane glasnoće svake pjesme i nježno je usmjerava prema dosljednom cilju.

Za razliku od ReplayGaina, **ne** zahtijeva nikakve oznake u vašim datotekama i **ne** mijenja vaš audio. Radi u stvarnom vremenu na svemu što reproducirate, uključujući streamove iz oblaka i radio uživo, te se čisto resetira kada premotavate ili mijenjate pjesme.

Četiri predloška pokrivaju uobičajene slučajeve:

- **Lagana** — nježno izjednačavanje (cilj −20 LUFS).
- **Standardna** — zadana, glasnoća u stilu streaminga (cilj −16 LUFS, do +12 dB pojačanja za tihe pjesme).
- **Jaka** — agresivno usklađivanje za vrlo mješovite biblioteke (cilj −14 LUFS).
- **Noć** — tiša i dosljedna za večernje slušanje na niskoj glasnoći (cilj −23 LUFS).

Više ne morate posezati za glasnoćom između pjesama.

## Redizajnirani ekvilajzer

Evermusicov **10-pojasni grafički ekvilajzer** dobio je potpuni redizajn. Pojasevi pokrivaju **32 Hz do 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), svaki podesiv od **−12 dB do +12 dB** u finim koracima od 0,1 dB, s **predpojačalom** od −24 dB do +24 dB za sprječavanje izobličenja (clipping) kada pojačavate.

Što je novo u 8.7:

- **Novi klizači** — precizne, responzivne kontrole koje usvajaju izgled izvornog sistemskog klizača iOS-a 26 i materijal **Liquid Glass**.
- **Brže, glatko prebacivanje predložaka** — skačite između predložaka trenutačno, s redizajniranom vodoravnom trakom predložaka u portretnoj orijentaciji i okomitim stupcem predložaka u pejzažnoj.
- **Bolji raspored u pejzažnoj orijentaciji i na iPadu** — klizači i birač predložaka preraspoređuju se kako bi iskoristili dodatnu širinu umjesto da se stiskaju u stupac veličine telefona.
- **Prilagođeni predlošci** — stvarajte i spremajte vlastite krivulje, prerasporedite ih te **uvozite i izvozite** predloške kao `.eqp` datoteke za premještanje između uređaja ili dijeljenje.

Ekvilajzer se izvorno pokreće u mehanizmu (`AVAudioUnitEQ`), pa se primjenjuje na svaki izvor, a radi i putem AirPlaya, Chromecasta i CarPlaya gdje je podržan.

## Ponovno izrađen mehanizam za reprodukciju

Ispod haube, Evermusic 8.7 radi na **ponovno izrađenom streaming mehanizmu** izgrađenom na Appleovom `AVAudioEngine`-u s prilagođenim renderirajućim procesnim lancem. To omogućuje predaju bez pauza, lanac efekata i ekvilajzer, a čini i svakodnevnu reprodukciju pouzdanijom.

- **Poboljšana podrška za formate** — uključujući **FLAC** (putem Core Audio) i **Ogg Vorbis** (putem `libvorbisfile`), uz MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF i druge.
- **Pametnije pohranjivanje u međuspremnik** — prilagodljivi unaprijedni međuspremnik koji se skalira s vašom vezom, s neprekinutim kružnim međuspremnikom koji hrani izlaz kako kratki mrežni zastoji ne bi prerasli u prekide.
- **Automatski oporavak** — stroj stanja za ponovno pohranjivanje u međuspremnik i logika ponovnih pokušaja s odgodom čisto nastavljaju reprodukciju nakon trenutka slabog signala umjesto zaustavljanja pjesme.
- **Manje prekida** — isti mehanizam pogoni lokalne datoteke, streamove iz oblaka, medijske poslužitelje i internetski radio, pa je ponašanje dosljedno svugdje.

## Sada svira i CarPlay

Zasloni koje uistinu gledate dok slušate — **zaključani zaslon**, **CarPlay** i tipke daljinskog upravljača vašeg auta ili slušalica — točniji su i brži u 8.7.

- **Točnije informacije Sada svira.** Evermusic hvata stanje playera pod zaključavanjem prije objavljivanja, pa se naslov, proteklo vrijeme, trajanje i stanje reprodukcije/pauze nikad ne mogu međusobno razlikovati na zaključanom zaslonu ili u autu. Stanja pohranjivanja u međuspremnik i učitavanja sada se ispravno prijavljuju umjesto prikaza „svira” dok se pjesma još dohvaća.
- **Pouzdane daljinske kontrole.** Reprodukcija, pauza, sljedeća, prethodna, premotavanje, preskakanje, nasumično, ponavljanje i brzina reprodukcije dosljedno reagiraju s tipki slušalica, kontrola auta i zaključanog zaslona, pogonjeni `MPRemoteCommandCenter`-om.
- **Brži CarPlay omoti.** Omoti albuma sada se učitavaju nekoliko puta brže na dugim popisima (tempo skupne obrade smanjen s 1,0 s na 0,25 s, uz trenutačno učitavanje prvog vidljivog zaslona), a sada se pojavljuju u kompaktnim redcima CarPlay popisa u iOS-u 26 koji prije nisu prikazivali omote.
- **Ispravci sortiranja i stabilnosti CarPlaya.** Brže sortiranje na velikim bibliotekama i otpornost na rubne padove pri pomicanju kroz duge popise.
- **Prigušena ažuriranja metapodataka.** Ažuriranja Sada svira i daljinskih naredbi sada su prigušena kako brze promjene više ne bi preplavljivale sustav, što kontrole zaključanog zaslona i CarPlaya drži responzivnima.

## Ostala poboljšanja

- **Dizajn Liquid Glass** dorađen u cijeloj aplikaciji — prozirne površine, glatkije animacije i profinjene kontrole na iOS-u, iPadOS-u i macOS-u.
- **Novi widgeti početnog zaslona** s poboljšanom logikom ažuriranja koja ih drži usklađenima bez dodatnog trošenja baterije.
- Ispravci za nedavna iOS izdanja.
- Ispravci lokalizacije na više jezika.
- Mnoga manja poboljšanja temeljena na vašim e-porukama i recenzijama na App Storeu.

## Zašto je ovo ažuriranje važno

Evermusic 8.7 izgrađen je oko jedne ideje: **vaša glazba treba zvučati najbolje, na bilo kojem izvoru.**

1. **Cijeli albumi, kako je zamišljeno.** Prava reprodukcija bez pauza znači da live setovi, DJ mixevi i koncept albumi napokon sviraju onako kako ih je izvođač masterirao.
2. **Studio u vašem džepu.** Reverb, delay, distorzija, kompresor, crossfeed, redizajnirani ekvilajzer i normalizacija glasnoće daju vam stvarnu kontrolu nad vašim zvukom, a ne samo prekidač za uključivanje/isključivanje.
3. **Isti doživljaj svugdje.** Lokalne datoteke, pogoni u oblaku, medijski poslužitelji i internetski radio prolaze kroz isti ponovno izrađeni mehanizam, uz točan Sada svira i brži CarPlay povrh toga.

## Nabavite Evermusic 8.7

[**Preuzmite Evermusic s App Storea**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) ili ažurirajte iz App Storea. Evermusic je besplatno preuzimanje s opcionalnim nadogradnjama unutar aplikacije za napredne značajke.

Ako uživate u aplikaciji, ostavite ocjenu na App Storeu — to uistinu pomaže. Imate povratnu informaciju ili ste naišli na problem? Pišite nam na **support@everappz.com**. Čitamo svaku poruku.

## Često postavljana pitanja

{{% details title="Što je novo u Evermusicu 8.7?" closed="true" %}}
Evermusic 8.7 dodaje pravu reprodukciju bez pauza, pet studijskih audio efekata (reverb, delay, distorziju, kompresor i crossfeed), normalizaciju glasnoće EBU R128, redizajnirani 10-pojasni ekvilajzer s prilagođenim predlošcima i uvozom/izvozom, ponovno izrađen AVAudioEngine streaming mehanizam s poboljšanom podrškom za formate (uključujući FLAC i Ogg Vorbis), brži i točniji CarPlay i Sada svira, ažuriranja dizajna Liquid Glass, osvježene widgete početnog zaslona te ispravke pogrešaka i lokalizacije.
{{% /details %}}

{{% details title="Ima li Evermusic pravu reprodukciju bez pauza?" closed="true" %}}
Da. Počevši od Evermusica 8.7, reprodukcija je uistinu bez pauza: nema pauze, klika ili tiktaka između pjesama. Mehanizam unaprijed pohranjuje u međuspremnik i dekodira sljedeću pjesmu dok trenutna svira te predaje reprodukciju između audio uzoraka na neprekinutom kružnom međuspremniku, pa je prijelaz nečujan. Radi za lokalne datoteke, streamove iz oblaka i medijske poslužitelje te je idealan za live albume, DJ mixeve i koncept albume.
{{% /details %}}

{{% details title="Koje audio efekte Evermusic 8.7 uključuje?" closed="true" %}}
Pet efekata u stvarnom vremenu: **Reverb** (13 predložaka prostora, miješanje wet/dry), **Delay/jeka** (10 predložaka s vremenom kašnjenja, povratnom vezom, niskopropusnim filtrom i miješanjem), **Distorzija** (22 predloška s karakterom s predpojačanjem i miješanjem), **Kompresor** (potpun procesor dinamike s pragom, omjerom, napadom, otpuštanjem, ekspanzijom i kompenzacijskim pojačanjem, plus 10 predložaka) i **Crossfeed** (Bauer bs2b crossfeed za slušalice s kontrolama razine i granične frekvencije te 6 predložaka). Svaki efekt dolazi s pomno biranim predlošcima, a vaše prilagođene postavke pamte se između sesija.
{{% /details %}}

{{% details title="Što je Crossfeed i zašto bih ga koristio?" closed="true" %}}
Crossfeed umiješava malu, filtriranu količinu svakog stereo kanala u drugi, onako kako vaše uši prirodno čuju prave zvučnike u prostoriji. Na slušalicama to smanjuje pretjerano, „unutar glave” odvajanje snimaka s oštrom panoramom i čini dugo slušanje ugodnijim. Evermusic koristi dobro poznat algoritam Bauer stereophonic-to-binaural (bs2b) i uključuje predloške poput Chu Moy i Jan Meier. Osobito je učinkovit na starijim stereo miksevima iz 1960-ih i 1970-ih.
{{% /details %}}

{{% details title="Kako normalizacija glasnoće funkcionira u Evermusicu?" closed="true" %}}
Evermusic 8.7 mjeri percipiranu glasnoću svake pjesme koristeći standard EBU R128 (ITU-R BS.1770) u stvarnom vremenu i nježno prilagođava razinu prema dosljednom cilju tako da pjesme ne skaču u glasnoći. Ne zahtijeva ReplayGain oznake i ne mijenja vaše datoteke. Dostupna su četiri predloška — Lagana (−20 LUFS), Standardna (−16 LUFS), Jaka (−14 LUFS) i Noć (−23 LUFS) — a normalizacija se čisto resetira kada premotavate ili mijenjate pjesme.
{{% /details %}}

{{% details title="Je li Evermusicova normalizacija glasnoće isto što i ReplayGain?" closed="true" %}}
Postiže isti cilj — dosljednu glasnoću između pjesama — ali radi drukčije. ReplayGain se oslanja na oznake glasnoće pohranjene unutar vaših datoteka. Evermusicov normalizator mjeri glasnoću uživo koristeći EBU R128, pa radi na bilo kojem izvoru, uključujući streamove iz oblaka i internetski radio, čak i kada datoteke uopće nemaju oznaka.
{{% /details %}}

{{% details title="Koliko pojaseva ima Evermusicov ekvilajzer i mogu li izraditi vlastite predloške?" closed="true" %}}
Evermusicov ekvilajzer je 10-pojasni grafički ekvilajzer koji pokriva 32 Hz do 16 kHz, sa svakim pojasom podesivim od −12 dB do +12 dB u koracima od 0,1 dB i predpojačalom od −24 dB do +24 dB. Uključuje ugrađene predloške, omogućuje stvaranje i spremanje prilagođenih predložaka te podržava uvoz i izvoz predložaka kao .eqp datoteka kako biste ih premještali ili dijelili između uređaja.
{{% /details %}}

{{% details title="Što se promijenilo u ekvilajzeru Evermusica 8.7?" closed="true" %}}
Ekvilajzer je redizajniran s novim, preciznijim klizačima koji usvajaju izgled sistemskog klizača iOS-a 26 i Liquid Glass, bržim i glatkijim prebacivanjem predložaka te boljim rasporedom u pejzažnoj orijentaciji i na iPadu (vodoravna traka predložaka u portretnoj orijentaciji i okomiti stupac predložaka u pejzažnoj). Podržani su prilagođeni predlošci i uvoz/izvoz .eqp datoteka.
{{% /details %}}

{{% details title="Podržava li Evermusic 8.7 FLAC i Ogg Vorbis?" closed="true" %}}
Da. Ponovno izrađeni mehanizam reproducira FLAC (putem Core Audio) i Ogg Vorbis (putem libvorbisfile), uz MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF i druge, iz lokalnih datoteka, pogona u oblaku i medijskih poslužitelja.
{{% /details %}}

{{% details title="Što je poboljšano u CarPlayu i na zaključanom zaslonu?" closed="true" %}}
CarPlay omoti albuma učitavaju se nekoliko puta brže na dugim popisima i sada se pojavljuju u kompaktnim redcima popisa iOS-a 26 koji prije nisu prikazivali nijedan. Informacije Sada svira na zaključanom zaslonu i u CarPlayu točnije su — naslov, proteklo vrijeme, trajanje i stanje reprodukcije/pauze hvataju se zajedno tako da se ne mogu razlikovati, a stanja pohranjivanja u međuspremnik ispravno se prijavljuju. Daljinske kontrole (reprodukcija, pauza, sljedeća, prethodna, premotavanje, nasumično, ponavljanje, brzina) pouzdano reagiraju sa slušalica i iz auta, a sortiranje u CarPlayu na velikim bibliotekama je brže.
{{% /details %}}

{{% details title="Rade li audio efekti i ekvilajzer s cloud streamingom i CarPlayem?" closed="true" %}}
Da. Efekti, ekvilajzer i normalizacija glasnoće izvorno se pokreću unutar mehanizma za reprodukciju, pa se primjenjuju na sve što Evermusic reproducira — lokalne datoteke, pogone u oblaku, medijske poslužitelje i internetski radio — te nastavljaju raditi tijekom reprodukcije putem CarPlaya i, gdje je podržano, putem AirPlaya i Chromecasta.
{{% /details %}}

{{% details title="Je li ažuriranje na Evermusic 8.7 besplatno i koje uređaje podržava?" closed="true" %}}
Da. Evermusic je besplatno preuzimanje s App Storea, a 8.7 je besplatno ažuriranje za postojeće korisnike, s opcionalnim nadogradnjama unutar aplikacije za napredne značajke. Radi na iPhoneu, iPadu i Macu. CarPlay zahtijeva vozilo ili glavnu jedinicu kompatibilnu s CarPlayem.
{{% /details %}}
