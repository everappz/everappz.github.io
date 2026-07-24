---
title: "Ako používať zvukové efekty a DSP vo Flacboxe: Compressor, Freeverb, Crossfeed, Echo, Volume Normalization a ďalšie"
date: 2026-07-24
description: "Kompletný sprievodca zvukom Flacboxu na iPhone, iPade a Macu. Zistite, ako funguje engine BASS, ktoré ďalšie formáty prehráva (vrátane MOD a tracker hudby a DSD) a čo presne robí každý efekt, každý posuvník a každý preset s vaším zvukom, plus 10-pásmový ekvalizér a vlastný DSP reťazec."
keywords: ["zvukové efekty Flacbox", "vysvetlenie presetov Flacbox", "engine BASS Flacbox", "zvuková knižnica BASS iOS", "prehrávač MOD hudby iPhone", "prehrávač tracker hudby iOS", "prehrávanie MOD XM IT S3M iPhone", "prehrávač DSD iOS", "prehrávač FLAC iPhone", "bezstratový hudobný prehrávač iOS", "presety ekvalizéra Flacbox", "10-pásmový ekvalizér iPhone", "normalizácia hlasitosti iPhone", "EBU R128 iOS", "normalizácia hlasitosti hudobný prehrávač", "crossfeed slúchadlá iOS", "bs2b crossfeed", "presety kompresora hudobný prehrávač", "freeverb reverb iOS", "echo delay hudobný prehrávač", "DSP reťazec hudobný prehrávač", "zosilnenie basov iPhone", "ako pridať efekty do hudby Flacbox", "najlepšie nastavenia ekvalizéra iPhone"]
tags: ["Flacbox", "Zvukové efekty", "Návod", "BASS", "Ekvalizér", "Zosilnenie basov", "Compressor", "Freeverb", "Crossfeed", "Echo", "Normalizácia hlasitosti", "EBU R128", "MOD hudba", "Tracker hudba", "DSD", "FLAC", "DSP", "Slúchadlá", "Presety"]
readingTime: 30
---

{{< author-byline >}}

{{< full-width-tables >}}

**Krátka odpoveď:** Vo Flacboxe si zvolíte jeden **Prehrávací engine** v **Nastavenia > Audio prehrávač**: **Standard** (systémový engine od Apple), **Universal** (engine FFmpeg) alebo **Sound FX** (**engine BASS™**). Engine, ktorý zvolíte, rozhoduje o tom, ktoré formáty súborov sa prehrajú, takže na tejto voľbe záleží. Engine **Sound FX** prehráva ďalšie formáty, ktoré väčšina iPhone aplikácií vynecháva (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus a staré **MOD a tracker hudbu** ako MOD, XM, IT a S3M) a je jediným enginom, ktorý poháňa zvukové nástroje: **10-pásmový ekvalizér**, **Volume Normalization**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** a vlastný **DSP reťazec**. Ak teda chcete používať efekty z tohto sprievodcu, najprv nastavte svoj Prehrávací engine na **Sound FX**. Každý nástroj má hotové **presety**. Otvorte ich v **Nastavenia > Audio prehrávač** (Zvukové efekty, Zvukový ekvalizér, Spracovanie signálu) alebo ťuknite na tlačidlo **⋯ (Viac)** na prehrávači a zvoľte **Zvukové efekty**. Nič z toho, čo tu urobíte, nikdy nezmení vaše súbory.

> Vysvetlenia posuvníkov a presetov nižšie sú tie isté krátke popisy, ktoré vám Flacbox zobrazuje v aplikácii, obohatené o trochu ďalšieho kontextu, aby ste mali úplný obraz skôr, než ťuknete.

## Ako čítať tohto sprievodcu

Každý nástroj funguje rovnako:

1. **Zapnite ho.** Každý efekt má vlastný vypínač zap/vyp. Na začiatku sú všetky vypnuté. Naraz môžete zapnúť koľko chcete.
2. **Vyberte preset.** Preset je hotové nastavenie. Ťuknite naň a zvuk sa okamžite zmení. Tento sprievodca uvádza, čo robí **každý** preset.
3. **Doladenie (voliteľné).** Otvorte posuvníky a upravte ich ručne. Vo chvíli, keď pohnete posuvníkom, efekt zobrazí **Manual**, takže viete, že ste opustili preset. Každý posuvník má tlačidlo na obnovenie.

Nič sa neuloží do vašich súborov. Sú to živé efekty. Vypnite efekt a váš pôvodný zvuk sa okamžite vráti.

## Vyberte si Prehrávací engine (efekty má Sound FX)

Flacbox enginy nekombinuje. Vyberiete si **jeden** v **Nastavenia > Audio prehrávač > Prehrávací engine** a engine, ktorý zvolíte, rozhoduje o tom, ktoré formáty súborov môžete prehrávať a či sú efekty dostupné. Sú tri možnosti, zobrazené v aplikácii pod týmito presnými názvami:

1. **Standard.** Vstavaný systémový engine od Apple. Používa hardvérové dekódovanie pre nižšiu spotrebu batérie.
2. **Universal.** Engine FFmpeg, ktorý otvára veľmi širokú škálu formátov.
3. **Sound FX.** **Engine BASS™**. Prehráva bezstratové súbory a súbory s vysokým rozlíšením s plnou presnosťou, pridáva modulovú (tracker) hudbu a poháňa každý efekt, 10-pásmový ekvalizér a DSP reťazec v tomto sprievodcovi.

Keďže každý engine podporuje vlastnú sadu formátov, súbory, ktoré môžete prehrávať, sa menia podľa toho, ktorý engine vyberiete. Ešte dôležitejšie je, že efekty, ekvalizér a DSP reťazec fungujú **iba** s enginom **Sound FX**, takže ak ich chcete používať, zvoľte ho ako prvé.

Sound FX je postavený na **BASS™**, profesionálnej zvukovej knižnici od Un4seen Developments. Viac sa o nej dozviete na jej domovskej stránke [un4seen.com](https://www.un4seen.com/).

## Hudobné formáty: čo pridáva engine Sound FX (BASS™) (vrátane MOD a tracker hudby)

Keď je zvolený engine **Sound FX (BASS™)**, Flacbox prehráva špecializované formáty nižšie, navyše k bežným. Najzvláštnejšia je **modulová hudba**, nazývaná aj **tracker hudba**. Modulový súbor nie je bežná nahrávka. Obsahuje malé zvuky nástrojov plus „partitúru“, ktorá hovorí, ako ich prehrať, a Flacbox skladbu z tejto partitúry naživo znovu skladá tak, ako mali byť tieto súbory prehrávané. Bežné prehrávače to nedokážu.

| Typ hudby | Formáty | Dobré vedieť |
|---|---|---|
| **Modulová / tracker hudba** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Znovu skladané naživo modulovým prehrávačom BASS™. Skvelé pre chiptunes a staré demoscene alebo Amiga skladby. |
| **Moderné bezstratové** | FLAC | Plná kvalita, menšie ako WAV. |
| **Iné bezstratové** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Menej bežné bezstratové typy, všetky podporované. |
| **DSD s vysokým rozlíšením** | DSF, DFF | Prehráva sa na bežnom hardvéri pomocou DSD cez PCM. |
| **Moderné stratové** | Opus, Ogg Vorbis, MP3 | Bežné typy pre streamovanie a sťahovanie. |

Engine Sound FX prehráva aj hlavné formáty Apple (AAC, ALAC, M4A, WAV, AIFF) a živé streamy, takže efekty a ekvalizér fungujú aj na nich.

**Prečo vám to pomáha:** ak máte zmes FLAC albumov, DSD súborov s vysokým rozlíšením a priečinok starých MOD alebo XM tracker skladieb, Flacbox ich všetky prehrá a ekvalizér aj efekty fungujú na každej z nich.

## Tri menu, ktoré budete používať

Flacbox uchováva svoje zvukové nástroje na troch miestach, všetky v nastaveniach audio prehrávača. Najprv sa uistite, že váš **Prehrávací engine** je nastavený na **Sound FX** (Nastavenia > Audio prehrávač > Prehrávací engine), pretože efekty, ekvalizér a DSP reťazec sú dostupné iba s týmto enginom.

- **Zvukové efekty** (rack efektov): otvorte prehrávač, ťuknite na **⋯ (Viac)**, ťuknite na **Zvukové efekty**. Alebo prejdite na **Nastavenia > Audio prehrávač > Zvukové efekty**.
- **Zvukový ekvalizér** (10 pásiem a presety): **Nastavenia > Audio prehrávač > Zvukový ekvalizér**.
- **Spracovanie signálu** (váš vlastný DSP reťazec): **Nastavenia > Audio prehrávač > Spracovanie signálu**.

V **Nastavenia > Audio prehrávač** môžete tiež nastaviť **výstupnú vzorkovaciu frekvenciu**, **kanály** a **veľkosť bufferu**.

## 10-pásmový ekvalizér

**Čo robí:** Mení tón hudby, od hlbokých basov po jasné výšky. Toto je najlepší nástroj na čisté **zosilnenie basov** alebo jasnejšiu, čistejšiu hornú časť. Predstavte si ho ako desať otočných gombíkov hlasitosti, každý pre inú časť zvuku. Zdvihnite pásmo, aby ste tú časť vyzdvihli, znížte ho, aby ste ju potlačili. Malé zmeny o pár dB zvyčajne znejú najlepšie a funguje to na všetkom, čo prehrávate.

**Ako to funguje:** Desať posuvníkov na **32, 64, 125, 250, 500 Hz a 1, 2, 4, 8, 16 kHz**. Každý ide od **-12 dB (rez)** po **+12 dB (zosilnenie)**. K dispozícii je aj **Predzosilňovač** od **-24 do +24 dB** pre celkovú úroveň. Vlastné presety si môžete uložiť a **exportovať alebo importovať** medzi zariadeniami.

**Čo robí každý vstavaný preset (22 presetov):**

| Preset | Čo robí s vaším zvukom |
|---|---|
| **Flat** | Žiadna zmena. Všetky pásma na nule. Čistý východiskový bod. |
| **Acoustic** | Teplé basy a ostré, prítomné výšky. Akustické gitary a hlasy pôsobia prirodzene a živo. |
| **Bass Booster** | Silné zdvihnutie spodných frekvencií, stredy a výšky nedotknuté. Viac úderu a váhy. |
| **Bass Reducer** | Reže spodné frekvencie. Užitočné pri dunivých miestnostiach, lacných slúchadlách alebo ťažkých skladbách. |
| **Treble Booster** | Zdvihne iba výšky. Pridáva iskru a vzduch, viac detailov. |
| **Treble Reducer** | Zmäkčuje výšky. Krotí ostré alebo prenikavé nahrávky. |
| **Classical** | Plné basy a jemné výšky s miernym poklesom stredov. Hladké a priestranné pre orchestrálnu hudbu. |
| **Dance** | Veľké basy a jasné výšky s vyhĺbenými stredmi. Údernú a energickú pre klubové skladby. |
| **Deep** | Teplé, husté spodné frekvencie s jemnejšími výškami. Útulný, uvoľnený zvuk. |
| **Electronic** | Silné basy a jasné výšky pre syntetizátory a beaty. Široké a moderné. |
| **Hip-Hop** | Ťažké basy a čisté výšky s kontrolovanými stredmi. Vážne a úderné. |
| **Jazz** | Teplé a hladké, s malým poklesom stredov. Ľahké a prirodzené pre akustický jazz. |
| **Latin** | Zosilnené spodné a horné frekvencie s čistými stredmi. Jasné a živé. |
| **Loudness** | Silne zosilňuje basy a výšky (krivka „úsmev“). Znie plnšie pri nízkej hlasitosti. |
| **Lounge** | Vyzdvihnuté stredy s mäkkými okrajmi. Uvoľnené a vhodné pre vokály. |
| **Piano** | Čisté stredy a výšky, aby klavírne tóny čisto zazneli. |
| **Pop** | Zdvihnuté stredy pre vokály, so spodnými a hornými frekvenciami stiahnutými dozadu. Hlasy sú v popredí. |
| **R&B** | Veľmi silná teplota nízkych stredov a čisté výšky. Hladké a bohaté. |
| **Rock** | Zosilnené spodné a horné frekvencie pre gitary a bubny. Energické a plné. |
| **Small Speakers** | Zosilňuje spodné frekvencie a reže výšky, aby maličké reproduktory zneli plnšie. |
| **Spoken Word** | Zdvihuje hlasový rozsah a reže hlboké basy. Reč je zrozumiteľná. |
| **Vocal Booster** | Vytláča stred, kde sídlia hlasy, a reže okolo nich. Vokály vyniknú. |

**Tip pre basy:** Začnite s **Bass Booster** a potom, ak to znie zablatene, stiahnite Predzosilňovač o 1 až 2 dB, aby sa nič neskreslilo.

## Volume Normalization (Vyrovnaná hlasitosť)

**Čo robí:** Niektoré skladby hrajú hlasnejšie ako iné, takže neustále meníte hlasitosť. Toto zabezpečí, že každá skladba hrá zhruba pri rovnakej hlasitosti sama od seba, takže to nemusíte robiť vy. Je to ideálne pre zamiešané playlisty, ktoré miešajú staré a nové nahrávky, rôzne albumy alebo rôzne zdroje, kde môže byť jedna skladba oveľa hlasnejšia ako ďalšia.

**Ako to funguje:** Počúva skutočnú hlasitosť každej skladby pomocou štandardu **EBU R128** (meranú v **LUFS**, tá istá myšlienka, akú používajú streamovacie služby) a potom každú skladbu upraví smerom k vášmu cieľu. Nepotrebuje žiadne tagy vo vašich súboroch a nikdy nemení zvuk. EBU R128 meria hlasitosť, ktorú vaše uši skutočne vnímajú počas celej skladby, nielen najvyšší vrchol, a preto zodpovedá tomu, ako hlasno sa vám skladby naozaj zdajú. Flacbox to počíta naživo počas prehrávania hudby (a keď môže, kontroluje hlasitosť vopred) a potom na skladbu aplikuje jednu stálu zmenu hlasitosti. Limit **Max boost** zabraňuje tomu, aby boli veľmi tiché nahrávky vytlačené tak silno, že by sa skreslili. Keďže číta samotný zvuk, funguje na akomkoľvek zdroji, vrátane cloudových súborov, živých streamov a modulovej hudby, aj keď súbory nemajú žiadne tagy hlasitosti.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Target loudness** | Nastavuje hlasitosť, ku ktorej sa každá skladba vyrovnáva. Vyššie hodnoty spôsobia, že všetko hrá celkovo hlasnejšie. | -30 až -6 LUFS (-16) |
| **Max boost** | Obmedzuje, o koľko sa tiché skladby môžu zosilniť. Vyššie hodnoty priblížia tiché nahrávky k cieľu. | 0 až 24 dB (12) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Light** | Jemné vyrovnávanie pre bežné počúvanie. Vyrovnáva zjavné skoky hlasitosti bez toho, aby tiché skladby silno vytláčalo. |
| **Standard** | Univerzálne predvolené. Cieľová hlasitosť v štýle streamovania, ktorá vyhovuje väčšine hudby. Začnite tu. |
| **Strong** | Agresívne prispôsobovanie, ktoré tiché skladby pevne vytláča hore. Najlepšie pre zmiešané knižnice s veľkými rozdielmi úrovní. |
| **Night** | Tichší celkový cieľ, ktorý stále zdvíha jemné pasáže, takže nočné počúvanie zostáva konzistentné a tiché. |

## Compressor (Vyrovnanie hlasných a tichých častí)

**Čo robí:** V jednej skladbe môžu byť tiché časti príliš jemné a hlasné časti príliš hlasné. Toto ich priblíži k sebe, takže celá skladba je ľahko počuteľná, aj v aute alebo na hlučnom mieste. Jemne stlmí najhlasnejšie momenty a zdvihne tie tichšie, takže počas jednej skladby prestanete siahať po hlasitosti. Toto sa líši od Volume Normalization: Compressor vyrovnáva veci **vnútri** jednej skladby, zatiaľ čo Volume Normalization zosúlaďuje hlasitosť **medzi** skladbami. Tie dve fungujú spolu dobre. Začnite s presetom a posuvníky otvorte iba vtedy, ak chcete väčšiu kontrolu.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Threshold** | Úroveň, kde sa kompresia začína. Nižšie hodnoty stláčajú viac zvuku, čím udržujú tiché a hlasné časti bližšie k sebe. | -60 až 0 dB (-20) |
| **Ratio** | Ako silno sú hlasné časti zadržané, keď prekročia prah. Vyššie hodnoty komprimujú tvrdšie, čím udržujú zvuk vyrovnanejší. | 1:1 až 30:1 (4:1) |
| **Attack** | Ako rýchlo efekt reaguje na náhly hlasný vrchol. Krátke hodnoty zachytávajú transienty; dlhšie ich prepustia. | 0,1 až 1000 ms (10 ms) |
| **Release** | Ako rýchlo efekt povolí po tom, čo hlasná časť prejde. Krátke hodnoty môžu pumpovať; dlhšie znejú hladšie. | 10 ms až 5 s (100 ms) |
| **Master gain** | Konečné zosilnenie výstupu aplikované po spracovaní. Zdvihnite ho, aby ste zvýšili celkovú hlasitosť po vyrovnaní dynamiky. | -30 až +30 dB (0) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Transparent** | Sotva prítomná bezpečnostná sieť. Takmer úplne zachováva dynamiku a zachytáva iba najhlasnejšie vrcholy. |
| **Soft** | Ľahké vyrovnávanie pre hi-fi počúvanie doma. Jemné vyhladenie bez stláčania hudby. |
| **Standard** | Rozumné predvolené pre každodenné prehrávanie hudby. Prvý preset, ktorý treba vyskúšať. |
| **Heavy** | Agresívne vyrovnávanie pre hlučné prostredia. Auto, preplnená miestnosť, počúvanie pri nízkej hlasitosti. |
| **Voice / Podcast** | Naladené na reč. Pomalší attack prepúšťa sykavky, štedrý makeup gain vytláča vokály hore. |
| **Old Recordings** | Staré albumy a obnovené vinyly, kde je priemerná úroveň nižšia ako pri moderných vydaniach. |
| **Late Night** | Silná kompresia plus veľké zosilnenie pre tiché počúvanie, keď záleží na susedoch alebo spiacej rodine. |
| **Movie Dialog** | Vytláča hovorené slovo oproti hudbe a zvukovým efektom v rozmanitej zvukovej stope. |
| **Streaming Match** | Cieli približne na normalizáciu hlasitosti moderných streamovacích služieb okolo -14 LUFS. |
| **Maximum Loudness** | Naplno. Zasiahne limiter; očakávajte stlačený, veľmi vyrovnaný signál. Doslova preset s maximálnou hlasitosťou. |

## Freeverb (Reverb, pocit priestoru)

**Čo robí:** Pridáva hudbe pocit priestoru, od malej miestnosti po veľkú sálu. Vyberte preset alebo si sami dolaďte suchú a mokrú zmes, veľkosť miestnosti, tlmenie a šírku. Reverb je prirodzená ozvena, ktorú počujete v akomkoľvek reálnom priestore, a Freeverb ju znovu vytvára v softvéri. Trochu z neho spôsobí, že ploché alebo zblízka snímané nahrávky pôsobia otvorenejšie a živšie. Veľa z neho umiestni hudbu do veľkého, vzdialeného priestoru. Je to kreatívny efekt, takže pre prirodzené výsledky udržujte mokrú zmes miernu.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Dry mix** | Koľko z pôvodného, nedotknutého zvuku sa zachová. Vyššie hodnoty ponechávajú v zmesi viac suchého signálu. | 0 až 1 (0.0) |
| **Wet mix** | Koľko reverbovaného zvuku sa pridá. Vyššie hodnoty spôsobia, že reverb je hlasnejší a zjavnejší. | 0 až 3 (1.0) |
| **Room size** | Veľkosť predstavovaného priestoru. Vyššie hodnoty dávajú dlhší, väčší chvost reverbu, od malej miestnosti po katedrálu. | 0 až 1 (0.5) |
| **Damp** | Ako rýchlo v chvoste miznú vysoké frekvencie. Vyššie hodnoty robia reverb tmavším a teplejším. | 0 až 1 (0.5) |
| **Width** | Stereo rozptyl reverbu. Vyššie hodnoty spôsobia, že priestor pôsobí širšie medzi ľavým a pravým kanálom. | 0 až 1 (1.0) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Room** | Malý, tesný priestor. Jemná atmosféra, ktorá pridáva pocit miesta bez zaplavenia zvuku. |
| **Studio** | Suchá, kontrolovaná nahrávacia miestnosť. Práve dosť odrazu, aby to znelo prirodzene. |
| **Hall** | Veľká koncertná sála. Dlhý, bohatý chvost, ktorý sedí orchestrálnej a akustickej hudbe. |
| **Cathedral** | Obrovský, ozývajúci sa kamenný priestor. Najdlhší, najdramatickejší chvost reverbu. |
| **Plate** | Jasný, hustý štúdiový plate reverb. Klasika pre vokály a bubny. |
| **Ambience** | Krátka, vzdušná atmosféra. Pridáva ľahký pocit priestoru pri prevažne suchom zvuku. |

## Auto Wah (Funky prechod filtrom)

**Čo robí:** Filter, ktorý sám prechádza hore a dole pre funky, hlasu podobný wah zvuk. Vyberte preset alebo si sami nastavte mokrú zmes, spätnú väzbu, rýchlosť, rozsah a frekvenciu. Je to ten istý „wah“ prechod, aký robí gitarový wah pedál, ale tu sa pohybuje sám v čase s hudbou. Skvelo znie na funku, disco a elektronických skladbách. Je to smelý, zjavný efekt, takže pri každodennom počúvaní stačí málo.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Wet mix** | Ako silný je wah efekt v zmesi. Vyššie hodnoty robia prechádzajúci filter zjavnejším. | -2 až +2 (1.5) |
| **Feedback** | Koľko výstupu sa privádza späť do efektu. Vyššie hodnoty robia wah rezonantnejším a výraznejším. | -1 až +1 (0.5) |
| **Rate** | Ako rýchlo filter prechádza hore a dole. Vyššie hodnoty dávajú rýchlejšie, rytmickejšie wah. | 0,1 až 9 Hz (2.0) |
| **Range** | Ako ďaleko filter prechádza, v oktávach. Vyššie hodnoty dávajú širší, dramatickejší prechod. | 0,1 až 9 oktáv (4.3) |
| **Frequency** | Základná frekvencia, okolo ktorej filter prechádza. Nižšie hodnoty znejú hlbšie; vyššie jasnejšie. | 1 až 1000 Hz (50) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Classic** | Vyvážený, klasický wah prechod. Dobrý východiskový bod pre funk a rock. |
| **Slow** | Pomalý, široký prechod, ktorý jemne pláva hore a dole. Skvelý pre pady a dlhé tóny. |
| **Funky** | Rýchly, úderný prechod s množstvom pohybu. Pridáva gitarám a syntetizátorom rytmický záhryz. |
| **Deep** | Hlboký, široký prechod začínajúci od nízkej frekvencie. Veľký a dramatický. |
| **Subtle** | Jemný, nenápadný pohyb. Pridáva charakter bez toho, aby ovládol zvuk. |
| **Resonant** | Ostré, rezonantné wah s vysokou spätnou väzbou. Hlasu podobné a expresívne. |

## Phaser (Vírivé zasvišťanie)

**Čo robí:** Prechádzajúci filter, ktorý pridáva zvuku vírivý, svišťavý pohyb. Vyberte preset alebo si sami nastavte spätnú väzbu, rýchlosť, rozsah a frekvenciu. Pridáva jemný pohyb a trblietanie bez zmeny tónov. Je jemný na vokáloch a padoch a dramatický na syntetizátoroch a gitarách. Vyskúšajte Slow pre snový pocit alebo Jet pre silné vírenie.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Feedback** | Koľko výstupu sa privádza späť do efektu. Vyššie hodnoty robia phaser rezonantnejším a výraznejším. | -1 až +1 (0.0) |
| **Rate** | Ako rýchlo filter prechádza hore a dole. Vyššie hodnoty dávajú rýchlejšie, rytmickejšie phasovanie. | 0,1 až 9 Hz (1.0) |
| **Range** | Ako ďaleko filter prechádza, v oktávach. Vyššie hodnoty dávajú širší, dramatickejší prechod. | 0,1 až 9 oktáv (4.0) |
| **Frequency** | Základná frekvencia, okolo ktorej filter prechádza. Nižšie hodnoty znejú hlbšie; vyššie jasnejšie. | 1 až 1000 Hz (100) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Classic** | Vyvážený, klasický phaser prechod. Dobrý východiskový bod pre gitary a klávesy. |
| **Slow** | Pomalý, široký prechod, ktorý jemne pláva hore a dole. Skvelý pre pady a dlhé tóny. |
| **Fast** | Rýchly, trblietavý prechod s množstvom pohybu. Pridáva pohyb a energiu. |
| **Deep** | Hlboký, široký prechod začínajúci od nízkej frekvencie. Veľký a dramatický. |
| **Subtle** | Jemný, nenápadný pohyb. Pridáva charakter bez toho, aby ovládol zvuk. |
| **Jet** | Intenzívny, rezonantný prechod s vysokou spätnou väzbou, klasické zasvišťanie prúdového lietadla. |

## Flanger (Prechod prúdového lietadla)

**Čo robí:** Krátke, pohybujúce sa oneskorenie, ktoré dáva zvuku prúdové, prechádzajúce zasvišťanie. Vyberte preset alebo si sami nastavte hĺbku, spätnú väzbu, rýchlosť a oneskorenie. Je to silnejší, kovovejší bratranec phasera, známy prechádzajúcim zasvišťaním v klasickom rocku a elektronickej hudbe. Jemné nastavenia pridávajú mierny pohyb, zatiaľ čo hlboké nastavenia sú dramatické a zjavné. Najlepšie sa používa striedmo, pre efekt.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Depth** | Ako silný je prechádzajúci efekt. Vyššie hodnoty robia flangovanie zjavnejším. | 0 až 100 % (25) |
| **Feedback** | Koľko výstupu sa privádza späť do efektu. Vyššie hodnoty robia flanger rezonantnejším a kovovejším. | -99 až +99 % (-50) |
| **Rate** | Ako rýchlo sa prechod pohybuje hore a dole. Vyššie hodnoty dávajú rýchlejší, trblietavejší pohyb. | 0 až 10 Hz (0.25) |
| **Delay** | Základný čas oneskorenia, na ktorom je prechod postavený. Vyššie hodnoty dávajú hlbší, dutejší charakter. | 0 až 4 ms (2.0) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Classic** | Vyvážený, klasický flanger. Dobrý východiskový bod pre gitary a klávesy. |
| **Subtle** | Jemný, nenápadný prechod. Pridáva pohyb bez toho, aby ovládol zvuk. |
| **Deep** | Hlboký, ťažký prechod so silnou spätnou väzbou. Veľký a dramatický. |
| **Jet** | Intenzívny prechod s pozitívnou spätnou väzbou, klasické zasvišťanie prúdového lietadla. |
| **Fast** | Rýchly, trblietavý prechod s množstvom pohybu a energie. |
| **Wide** | Pomalý, široký prechod s dlhým oneskorením. Bohatý a priestranný. |

## Echo (Opakovania)

**Čo robí:** Opakuje zvuk ako miznúce ozveny pre pocit priestoru a hĺbky. Vyberte preset alebo si sami nastavte mokrú zmes, spätnú väzbu a oneskorenie. Je to ako volanie v kaňone: zvuk sa vráti raz alebo viackrát po krátkej medzere. Jediné krátke opakovanie pridáva telo a retro pocit, zatiaľ čo dlhšie opakovania s väčšou spätnou väzbou vytvárajú priestranné, vlečúce sa chvosty. Preset Ping Pong odráža opakovania medzi vaším ľavým a pravým uchom, čo je zábavné na slúchadlách. Udržujte mokrú zmes miernu, aby ozveny hudbu podporovali, a nie ju prekrývali.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Wet mix** | Ako hlasné sú ozveny v porovnaní s pôvodným zvukom. Vyššie hodnoty spôsobia, že opakovania viac vyniknú. | -2 až +2 (0.6) |
| **Feedback** | Koľkokrát sa ozvena opakuje. Vyššie hodnoty dávajú viac opakovaní, ktoré trvá dlhšie, kým zmiznú. | -1 až +1 (0.5) |
| **Delay** | Čas medzi ozvenami. Kratšie hodnoty dávajú tesný slap-back; dlhšie dávajú rozostúpené opakovania. | 0,01 až 2 s (0.4) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Slapback** | Jediné, tesné opakovanie tesne za zvukom. Klasický rockabilly slap-back. |
| **Room** | Krátka, prirodzená ozvena, ako malá miestnosť. Pridáva priestor bez rozmazania zvuku. |
| **Tape** | Teplé, stredné opakovania, ktoré postupne miznú, ako staré páskové oneskorenie. |
| **Dub** | Dlhé, ťažké opakovania so silnou spätnou väzbou. Veľké, dubové a priestranné. |
| **Ping Pong** | Ozveny sa odrážajú medzi ľavým a pravým reproduktorom pre široký stereo efekt. |
| **Long** | Pomalé, široko rozostúpené opakovania, ktoré sa vlečú ďaleko za zvukom. |

## Chorus (Hustejší, širší zvuk)

**Čo robí:** Zahusťuje a rozširuje zvuk vrstvením posúvajúcej sa kópie cez originál. Vyberte preset alebo si sami nastavte mokrú/suchú zmes, hĺbku, rýchlosť a spätnú väzbu. Spôsobí, že jeden nástroj alebo hlas znie ako niekoľko hrajúcich spolu, pridaním mierne rozladených, pohybujúcich sa kópií. To pridáva bohatosť a jemné trblietanie. Jemné nastavenia veci zahrejú, zatiaľ čo silné nastavenia znejú bohato a snovo. Je obľúbený na gitarách, klávesoch a vokáloch.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Wet/Dry** | Koľko chorusu počujete v porovnaní s pôvodným zvukom. Vyššie hodnoty robia efekt zjavnejším. | 0 až 100 % (50) |
| **Depth** | Ako ďaleko sa výška kolíše hore a dole. Vyššie hodnoty dávajú hustejší, trblietavejší zvuk. | 0 až 100 % (25) |
| **Rate** | Ako rýchlo sa trblietanie pohybuje. Pomalšie rýchlosti znejú jemne a bohato; rýchlejšie znejú skôr ako vibrato. | 0 až 10 Hz (1.1) |
| **Feedback** | Koľko efektu sa privádza späť do seba. Vyššie hodnoty robia chorus rezonantnejším a intenzívnejším. | -99 až +99 % (25) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Subtle** | Jemné zahustenie, ktoré pridáva teplo bez toho, aby na seba upozorňovalo. |
| **Lush** | Bohatý, klasický chorus. Skvelé univerzálne nastavenie pre gitary a klávesy. |
| **Ensemble** | Plné, vrstvené trblietanie, vďaka ktorému jeden nástroj znie ako niekoľko. |
| **Vibrato** | Úplne mokré s rýchlym tempom, pre kolísavé vibrato namiesto jemného chorusu. |
| **Wide** | Pomalé, široké trblietanie, ktoré otvára stereo obraz. Priestranné a snové. |
| **Twelve-String** | Jasné, rezonantné trblietanie pripomínajúce dvanásťstrunovú gitaru. |

## Distortion (Zrnitosť a hrana)

**Čo robí:** Pridáva zrnitosť a hranu prebudením zvuku. Vyberte preset alebo si sami nastavte drive, výstup a tón. Zámerne zdrsňuje zvuk, od teplej, zrnitej hrany po zlomený, fuzz tón. Je to kreatívny, zábavný efekt, nie spôsob, ako zlepšiť kvalitu, takže ho používajte v malých množstvách. Je zábavný na elektronických, rockových a experimentálnych skladbách. Znížte Output, ak je ťažký preset príliš hlasný.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Drive** | Ako silno je zvuk skreslený. Vyššie hodnoty sú zrnitejšie a agresívnejšie. | 0 až 100 % (15) |
| **Output** | Výstupná úroveň po skreslení. Znížte ju, ak sa ťažké nastavenie stane príliš hlasným. | -60 až 0 dB (-18) |
| **Tone** | Zrezáva výšky pred skreslením. Nižšie hodnoty znejú tmavšie a teplejšie. | 100 až 8000 Hz (8000) |
| **Center** | Okolo ktorej frekvencie je skreslenie sústredené. Posúva charakter jasnejšie alebo tmavšie. | 100 až 8000 Hz (2400) |
| **Width** | Aké široké je toto sústredenie. Úzke znie ostro a nazálne; široké znie plno a otvorene. | 100 až 8000 Hz (2400) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Warm Drive** | Ľahká, teplá zrnitosť, ktorá pridáva hranu bez väčšej zmeny charakteru. |
| **Crunch** | Klasický chrumkavý overdrive, úderný a rytmický. |
| **Overdrive** | Jasný, budený tón s množstvom záhryzu. Skvelé pre sólo zvuky. |
| **Fuzz** | Hustý, nasýtený fuzz. Ťažký a plný harmonických tónov. |
| **Metal** | Tesný, na stredy zameraný high-gain tón pre agresívne, ťažké zvuky. |
| **Screamer** | Overdrive so zosilnenými stredmi, ktorý prerazí, ako tube screamer. |
| **LoFi** | Stlačené, úzkopásmové skreslenie pre zrnitý lo-fi charakter. |

## Rotate (Točiace sa stereo)

**Čo robí:** Točí zvuk okolo stereo poľa pre rotačný, vírivý efekt. Vyberte preset alebo si sami nastavte rýchlosť. Pomaly pohybuje zvuk okolo vášho ľavého a pravého kanála, trochu ako točiaci sa reproduktor, čo pridáva vírivý, hypnotický pocit. Pomalé nastavenia sú jemné a široké, zatiaľ čo rýchle nastavenia sú závratné a zjavné. Je to stereo efekt, takže je najzreteľnejší na slúchadlách alebo dobre umiestnených reproduktoroch.

**Posuvník:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Rate** | Ako rýchlo sa zvuk točí okolo stereo poľa. Záporné hodnoty točia opačným smerom; nula ho drží nehybne. | -5 až +5 Hz (1.0) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Slow Pan** | Pomalý, jemný posun zo strany na stranu. Jemné a široké. |
| **Sway** | Stále kolísanie zľava doprava. Pridáva stereo obrazu jemný pohyb. |
| **Rotary** | Stredné točenie pripomínajúce rotačný reproduktor. |
| **Fast Spin** | Rýchle točenie okolo stereo poľa pre závratný, vírivý efekt. |
| **Reverse** | Stredné točenie v opačnom smere. |
| **Whirl** | Veľmi rýchle vírenie. Intenzívne a dezorientujúce. |

## Crossfeed (Prirodzený zvuk na slúchadlách)

Na reproduktoroch každé z vašich uší počuje ľavý aj pravý reproduktor, len v mierne odlišných časoch a hlasitostiach. Na slúchadlách je toto prirodzené premiešanie preč: vaše ľavé ucho počuje iba ľavý kanál a pravé ucho iba pravý. Toto „super stereo“ môže spôsobiť, že hudba pôsobí, akoby bola rozdelená vo vašej hlave, a tvrdo panorámované nahrávky, kde nástroj sedí úplne na jednej strane, môžu pri dlhom počúvaní pôsobiť neprirodzene alebo únavne.

Crossfeed to opravuje premiešaním malého, filtrovaného množstva každého kanála do druhého, s malým oneskorením a jemným zrezaním vysokých frekvencií. To sa blíži k tomu, ako zvuk zo skutočných reproduktorov dosahuje obe vaše uši, vrátane spôsobu, akým vaša hlava mierne tieni vzdialenejšie ucho. Výsledkom je prirodzenejší, reproduktoru podobný obraz, ktorý sedí trochu pred vami namiesto vo vašej hlave, a znižuje únavu z počúvania pri dlhých reláciách. Flacbox používa dobre známu metódu **bs2b (Bauer stereophonic-to-binaural)**, uznávaný open-source crossfeed používaný mnohými audiofilskými prehrávačmi. O algoritme si môžete prečítať na [stránke projektu bs2b](https://bs2b.sourceforge.net/).

**Cutoff** riadi, ako teplo znie premiešanie, a **Feed level** riadi, aké silné je. Presety pokrývajú klasické úrovne bs2b, od sotva prítomného dotyku po pevné, reproduktoru podobné premiešanie. Crossfeed je efekt pre slúchadlá, takže ho nechajte vypnutý, keď počúvate na reproduktoroch.

**Posuvníky:**

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Cutoff** | Nastavuje, kde sa presakovanie medzi kanálmi začína zrezávať. Nižšie hodnoty dávajú teplejší, výraznejší efekt. | 300 až 2000 Hz (700) |
| **Feed level** | Riadi, koľko jedného kanála presakuje do druhého. Vyššie hodnoty produkujú reproduktoru podobnejší zvuk. | 1 až 15 dB (4.5) |

**Presety:**

| Preset | Čo robí |
|---|---|
| **Subtle** | Sotva prítomný crossfeed pre bežné počúvanie. Zmäkčuje tvrdo panorámované stereo bez zmeny tonálnej rovnováhy. |
| **Chu Moy** | Klasické univerzálne predvolené. Vyvážené a ľahko teplé, funguje takmer na akomkoľvek materiáli. Začnite tu. |
| **Strong** | Silnejšie presakovanie pre tvrdšie panorámované mixy. Zjavnejšie zúženie sterea. |
| **Jan Meier** | Obľúbené medzi nadšencami slúchadiel. Širšie feed, reproduktoru podobnejšia prezentácia, mierne zdvihnutie basov. |
| **Speaker-like** | Naladené na najprirodzenejšiu reprodukciu v štýle reproduktorov cez slúchadlá. |
| **Vintage Stereo** | Agresívny crossfeed naladený pre mixy zo 60. a 70. rokov s tvrdo panorámovanými bubnami a vokálmi. |

## Spracovanie signálu: Postavte si vlastný DSP reťazec

Okrem hotových efektov vám Flacbox umožňuje postaviť si vlastný reťazec v **Nastavenia > Audio prehrávač > Spracovanie signálu**. Ako aplikácia vysvetľuje, keď je reťazec prázdny: *„Ťuknutím na + pridáte efekt. Každý zapnite alebo vypnite jeho prepínačom, ťahaním zmeníte poradie, ťuknutím upravíte jeho parametre a dlhým podržaním duplikujete alebo odstránite.“*

**Na poradí záleží**: filter pred skreslením znie inak ako ten istý filter za ním. Celý reťazec môžete tiež namieriť na **Všetky kanály**, **Ľavý kanál** alebo **Pravý kanál**.

Nižšie je každý blok, s vlastným textom aplikácie pre každý posuvník a každý preset.

### Gain (Úprava úrovne)

Zvyšuje alebo znižuje úroveň v jednom bode reťazca.

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Gain** | Zosilňuje alebo reže úroveň v tomto bode reťazca. Použite ho na doplnenie úrovne po iných efektoch alebo na budenie tých, ktoré nasledujú. | -24 až +24 dB (0) |

| Preset | Čo robí |
|---|---|
| **Unity** | Žiadna zmena úrovne. Neutrálny východiskový bod. |
| **Cut** | Veľký rez. Krotí hlasný zdroj alebo robí miesto pred efektmi, ktoré nasledujú. |
| **Trim** | Jemný rez na mierne stiahnutie úrovne. |
| **Lift** | Mierne zosilnenie na zdvihnutie tichého zdroja. |
| **Boost** | Silné zosilnenie pre tichý materiál alebo na tvrdšie budenie nasledujúcich efektov. |
| **Max** | Maximálne zosilnenie. Hlasné, dávajte pozor na orezanie neskôr v reťazci. |

### Low Pass (Odstraňuje výšky)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Cutoff** | Nastavuje, kde filter začína zrezávať výšky. Znížte ho na stmavenie a zmäkčenie zvuku; zdvihnite ho k vrcholu na úplné otvorenie. | 20 Hz až 20 kHz (20 kHz) |
| **Resonance** | Zdôrazňuje frekvencie priamo pri cutoffe. Držte ho nízko pre čisté zrezanie; zdvihnite ho pre špicatú, pískavú hranu. | 0,1 až 10 (0.707) |

| Preset | Čo robí |
|---|---|
| **Air** | Zrezáva iba úplný vrchol. Uberá trochu hrany bez otupenia zvuku. |
| **Warm** | Jemné zrezanie výšok pre teplejší, oblejší tón. |
| **Mellow** | Zreteľne zmäkčené. Sťahuje jas dozadu pre uvoľnený pocit. |
| **Muffled** | Tmavé a tlmené, akoby počuté cez stenu. |
| **Telephone** | Úzky, rezonantný vrchol nízko v rozsahu. Tenký, telefónu podobný hlas. |

### High Pass (Odstraňuje basy)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Cutoff** | Nastavuje, kde filter začína zrezávať basy. Zdvihnite ho na stenčenie spodných frekvencií a odstránenie dunenia; znížte ho k spodku na úplné otvorenie. | 20 Hz až 20 kHz (20 Hz) |
| **Resonance** | Zdôrazňuje frekvencie priamo pri cutoffe. Držte ho nízko pre čisté zrezanie; zdvihnite ho pre špicatú, pískavú hranu. | 0,1 až 10 (0.707) |

| Preset | Čo robí |
|---|---|
| **Rumble Cut** | Odstraňuje subsonické dunenie a DC offset bez dotknutia sa počuteľných spodných frekvencií. |
| **Tighten** | Zrezáva dunivé nízke frekvencie pre tesnejšie, čistejšie basy. |
| **Thin** | Reže teplo a telo, čím zanecháva ľahší, tenší zvuk. |
| **Radio** | Zostávajú iba stredy a výšky, ako malý rádiový reproduktor. |
| **Telephone** | Úzky, rezonantný vrchol vysoko v rozsahu. Tenký, telefónu podobný hlas. |

### Band Pass (Ponecháva stredné pásmo)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Center** | Nastavuje frekvenciu, ktorú filter prepúšťa. Všetko nad a pod ňou je zrezané. Prechádzajte ním na vyzdvihnutie basov, stredov alebo výšok. | 20 Hz až 20 kHz (1 kHz) |
| **Resonance** | Riadi, aké široké je pásmo. Nízke hodnoty prepustia široký rozsah; zdvihnite ho na zúženie okolo stredu pre ostrý, rezonantný tón. | 0,1 až 10 (0.707) |

| Preset | Čo robí |
|---|---|
| **Voice** | Široké pásmo okolo stredného rozsahu, kde sedí väčšina vokálov. Neutrálny východiskový bod. |
| **Bass** | Izoluje spodné frekvencie, čím zanecháva iba basy a kick. |
| **Body** | Sústreďuje sa na nízke stredy pre teplé, hranaté telo. |
| **Presence** | Zdvíha horné stredy pre čistotu a prítomnosť. |
| **Telephone** | Úzke pásmo stredov. Tenký, telefónu podobný zvuk. |
| **Wah** | Veľmi úzky, rezonantný vrchol. Prechádzajte stredom pre wah efekt. |

### Notch (Odstraňuje jedno úzke pásmo)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Frequency** | Nastavuje frekvenciu, ktorú filter odstraňuje. Všetko nad a pod ňou prejde. Nalaďte ho na brum alebo rezonanciu, aby ste ich vyrezali. | 20 Hz až 20 kHz (60 Hz) |
| **Resonance** | Riadi, aký široký je rez. Nízke hodnoty vyhĺbia široký rozsah; zdvihnite ho na odstránenie iba bodového pásma a ponechanie zvyšku nedotknutého. | 0,1 až 10 (8.0) |

| Preset | Čo robí |
|---|---|
| **Mains Hum 60** | Odstraňuje 60 Hz elektrický brum (severoamerická sieť). Neutrálny východiskový bod. |
| **Mains Hum 50** | Odstraňuje 50 Hz elektrický brum (európska a iné siete). |
| **Rumble** | Reže nízkofrekvenčné dunenie alebo rezonanciu bez stenčenia celého spodku. |
| **Mud** | Vyhĺbi zablatenie nízkych stredov pre čistejší, jasnejší zvuk. |
| **Boxy** | Odstraňuje hranaté trúbenie stredov. |
| **Harsh** | Krotí ostrý, prenikavý vrchol v horných stredoch. |

### Peaking (Parametrické EQ pásmo)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Frequency** | Stred pásma na zosilnenie alebo rez. Prechádzajte ním na nájdenie frekvencie, ktorú chcete tvarovať. | 20 Hz až 20 kHz (1 kHz) |
| **Gain** | O koľko zosilniť alebo rezať v strede. Kladné zdvíha pásmo; záporné ho vyhĺbi. | -15 až +15 dB (0) |
| **Q factor** | Nastavuje, aké široké je pásmo. Nízke hodnoty tvarujú širokú oblasť; vysoké zúžia na chirurgické, bodové zmeny. | 0,1 až 10 (1.0) |

| Preset | Čo robí |
|---|---|
| **Presence** | Široké zdvihnutie horných stredov pre čistotu a prítomnosť. Neutrálny východiskový bod. |
| **Warmth** | Široké zosilnenie nízkych stredov, ktoré pridáva telo a teplo. |
| **Vocal Boost** | Zdvíha jadro vokálneho rozsahu, aby vytlačil hlasy dopredu. |
| **Cut Mud** | Vyhĺbi hranaté zablatenie nízkych stredov pre čistejší zvuk. |
| **Tame Harsh** | Úzky rez na skrotenie ostrého, prenikavého vrcholu. |
| **Punch** | Nízke zosilnenie, ktoré pridáva úder a náraz spodným frekvenciám. |
| **Sub Boost** | Hlboké zosilnenie na úplnom spodku pre extra váhu sub-basov. |
| **Air** | Široké zdvihnutie na vrchole pre otvorený, vzdušný lesk. |
| **Clarity** | Zdvíha vysoké stredy na pridanie definície a hrany. |
| **De-Ess** | Úzky rez v rozsahu sykaviek na skrotenie ostrých S zvukov. |
| **De-Boom** | Reže dunivé nízkofrekvenčné nahromadenie pre tesnejšie spodné frekvencie. |
| **Scoop** | Široký pokles stredov pre vyhĺbený, moderný tón. |

### Low Shelf (Ovládanie basov a zosilnenie basov)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Frequency** | Nastavuje roh, pod ktorým shelf pôsobí. Všetko pod ním je zosilnené alebo rezané spolu. | 20 až 2000 Hz (200) |
| **Gain** | O koľko zdvihnúť alebo znížiť spodné frekvencie. Kladné pridáva váhu a teplo; záporné ich stenčuje. | -15 až +15 dB (0) |

| Preset | Čo robí |
|---|---|
| **Warmth** | Jemné zdvihnutie spodných frekvencií pre teplo a telo. Neutrálny východiskový bod. |
| **Bass Boost** | Solídne zosilnenie basov pre váhu a úder. |
| **Fullness** | Vypĺňa nižšie stredy pre plnší, oblejší zvuk. |
| **Trim Bass** | Mierny rez na odľahčenie mixu s ťažkými basmi. |
| **Cut Lows** | Silný rez na stenčenie alebo odbúranie dunenia spodných frekvencií. |
| **Big Bottom** | Veľké zosilnenie spodných frekvencií pre maximálnu váhu a dunenie. |

### High Shelf (Ovládanie výšok)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Frequency** | Nastavuje roh, nad ktorým shelf pôsobí. Všetko nad ním je zosilnené alebo rezané spolu. | 1 až 20 kHz (8 kHz) |
| **Gain** | O koľko zdvihnúť alebo znížiť horné frekvencie. Kladné pridáva jas a vzduch; záporné vyhladzuje a stmavuje. | -15 až +15 dB (0) |

| Preset | Čo robí |
|---|---|
| **Presence** | Jemné zdvihnutie horných frekvencií pre čistotu a detail. Neutrálny východiskový bod. |
| **Air** | Otvára úplný vrchol pre vzdušný, otvorený zvuk. |
| **Bright** | Silné zosilnenie pre ostrý, jasný, dopredný tón. |
| **Soften** | Mierny rez na ubratie hrany ostrým výškam. |
| **Tame Highs** | Silný rez na stmavenie a vyhladenie príliš jasného zvuku. |
| **Sparkle** | Veľké zosilnenie vrcholu pre maximálne trblietanie a lesk. |

### Soft Clip (Teplá saturácia)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Drive** | Tlačí signál tvrdšie do waveshaperu. Malé množstvá pridávajú jemné teplo; veľké množstvá zaobľujú vrcholy do hustej saturácie a zrnitosti. | 0 až 40 dB (0) |

| Preset | Čo robí |
|---|---|
| **Warm** | Štipka drive pre jemné, analógové teplo. |
| **Drive** | Znateľná saturácia, ktorá zahusťuje a farbí zvuk. |
| **Crunch** | Ťažký drive s počuteľnou chrumkavou hranou. |
| **Fuzz** | Hustá, fuzz distorzia. Vrcholy sú tvrdo stlačené. |
| **Destroy** | Maximálny drive. Agresívna, plne nasýtená zrnitosť. |

### Bit Crusher (Retro lo-fi)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Bit depth** | Nastavuje, koľko bitov opisuje každú vzorku. Menej bitov znamená hrubšie kroky a viac kvantizačného šumu, pre chrumkavý, zrnitý digitálny zvuk. | 1 až 16 bitov (16) |
| **Sample rate** | Zníži vzorkovaciu frekvenciu zvuku. Pri sto percentách je frekvencia nedotknutá; znížte ju na dlhšie držanie každej vzorky, čím sa otupia výšky a pridá ostrá, aliasovaná hrana. | 1 % až 100 % (100 %) |

| Preset | Čo robí |
|---|---|
| **Vintage** | Jemný pokles kvality, ako raný digitálny sampler. |
| **LoFi** | Klasické 8-bitové, polovičnou frekvenciou lo-fi. Zrnité a retro. |
| **Crunch** | Ťažšie stláčanie s počuteľnou chrumkavou hranou. |
| **Gritty** | Hrubé a zrnité. Kroky medzi úrovňami sú zjavné. |
| **Destroy** | Extrémna redukcia. Ostré, zlomené, sotva rozpoznateľné. |

### Ring Modulator (Kovové a robotické tóny)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Carrier** | Nastavuje frekvenciu tónu, ktorým sa signál násobí. Pár hertzov dáva tremolo kolísanie; vyššie frekvencie pridávajú kovové, zvonovité a robotické tóny. | 1 až 4000 Hz (440) |
| **Mix** | Zmiešava modulovaný zvuk s originálom. Pri nula percentách počujete iba suchý signál; pri sto percentách iba plne modulovaný tón. | 0 % až 100 % (0 %) |

| Preset | Čo robí |
|---|---|
| **Tremolo** | Veľmi nízky carrier ho premení na amplitúdové tremolo, kolíšuce hlasitosť. |
| **Robot** | Stredný carrier pridáva rinčivé tóny pre klasický efekt robotického hlasu. |
| **Metallic** | Husté, neharmonické tóny pre ostrý, kovový tón. |
| **Bell** | Vyšší carrier dáva jasné, zvonovité rinčanie. |
| **Alien** | Plne mokré s vysokým carrierom. Extrémne, mimozemské, sotva rozpoznateľné. |

### Tremolo (Kolísanie hlasitosti)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Rate** | Nastavuje, ako rýchlo hlasitosť pulzuje. Pomalšie rýchlosti dávajú hladké kolísanie; rýchlejšie dávajú rýchle zajakávanie. | 0,1 až 20 Hz (5) |
| **Depth** | Nastavuje, o koľko hlasitosť klesne pri každom pulze. Pri nula percentách je úroveň stála; pri sto percentách klesá až do ticha. | 0 % až 100 % (0 %) |

| Preset | Čo robí |
|---|---|
| **Gentle** | Pomalé, plytké kolísanie. Jemný pohyb bez upútania pozornosti. |
| **Classic** | Klasické zosilňovačové tremolo: stredná rýchlosť a mierna hĺbka. |
| **Deep** | Silný, hlboký pulz, ktorý pri každom cykle takmer klesá do ticha. |
| **Fast** | Rýchle chvenie pre trblietavý, nervózny pocit. |
| **Chop** | Rýchle a s plnou hĺbkou. Tvrdé, zajakávajúce sekanie. |

### Delay (Echo)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Time** | Nastavuje medzeru pred každou ozvenou. Krátke časy dávajú tesný slapback; dlhšie časy rozostúpia opakovania ďalej od seba. | 0,01 až 2 s (0.25) |
| **Feedback** | Nastavuje, koľko každej ozveny sa privádza späť. Nízke hodnoty dávajú jedno opakovanie; vyššie hodnoty budujú dlhú, vlečúcu sa sériu ozvien. | 0 až 0.95 (0.4) |
| **Mix** | Zmiešava ozveny s originálom. Pri nula percentách počujete iba suchý signál; pri sto percentách iba ozveny. | 0 % až 100 % (0 %) |

| Preset | Čo robí |
|---|---|
| **Slapback** | Jediná krátka ozvena, tesne pri origináli. Rockabilly a zdvojenie vokálov. |
| **Echo** | Klasické echo: jasné opakovanie s niekoľkými vlečúcimi sa chvostmi. |
| **Ping** | Rýchle, odrážajúce sa opakovanie, ktoré pridáva rytmický pohyb. |
| **Ambient** | Dlhšie, jemnejšie opakovania, ktoré sa vytrácajú do priestranného chvosta. |
| **Dub** | Vysoká spätná väzba pre dlhé, dubové kaskády ozvien. |
| **Cavern** | Dlhé, hlboké opakovania, ako zvuk ozývajúci sa cez obrovský priestor. |

### Stereo Width (Zúženie alebo rozšírenie)

| Ovládač | Čo robí | Rozsah (predvolené) |
|---|---|---|
| **Width** | Zužuje alebo rozširuje stereo obraz. Nula percent zbalí do mono, sto percent ho ponechá nedotknutý a vyššie hodnoty tlačia strany širšie. Ovplyvňuje iba stereo skladby na cieli Všetky kanály. | 0 % až 200 % (100 %) |

| Preset | Čo robí |
|---|---|
| **Wide** | Jemné rozšírenie, ktoré otvára stereo obraz. Neutrálny východiskový bod. |
| **Wider** | Silnejší rozptyl pre veľké, pohlcujúce stereo pole. |
| **Max** | Maximálna šírka. Veľmi široké, ale dávajte pozor na problémy s mono kompatibilitou. |
| **Narrow** | Sťahuje strany dovnútra pre tesnejší, centrovanejší obraz. |
| **Focused** | Takmer centrované, len s náznakom sterea. |
| **Mono** | Úplne zbalené do mono. Oba reproduktory hrajú ten istý signál. |

## Ako to všetko funguje pod kapotou (jednoduchá verzia)

- **Enginy:** vyberiete si jeden v Nastavenia > Audio prehrávač > Prehrávací engine: **Standard** (systém), **Universal** (FFmpeg) alebo **Sound FX** (**engine BASS™** od [Un4seen Developments](https://www.un4seen.com/)). Engine, ktorý zvolíte, rozhoduje o tom, ktoré formáty sa prehrajú, a efekty, ekvalizér a DSP reťazec bežia iba v engine Sound FX.
- **Formáty:** engine BASS™ pridáva FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus a modulovú (tracker) hudbu navyše k systémovým a FFmpeg formátom.
- **Efekty:** ekvalizér, compressor a väčšina efektov používajú prídavné efektové moduly BASS™. Freeverb je reverb Freeverb. Chorus, Flanger a Distortion používajú klasické efekty v štýle DirectX s vlastnými ovládačmi.
- **Volume Normalization:** živý vyrovnávač hlasitosti **EBU R128** (štandard hlasitosti používaný vo vysielaní a streamovaní).
- **Crossfeed:** crossfeed **bs2b (Bauer)**, bežiaci vnútri enginu BASS™.
- **DSP reťazec:** vaše vlastné bloky, aplikované v presnom poradí, ktoré nastavíte, na všetkých kanáloch alebo iba na jednej strane.
- **Výstup:** môžete nastaviť vzorkovaciu frekvenciu, počet kanálov a veľkosť bufferu tak, aby ladili s vaším vybavením.

Keďže toto všetko beží naživo počas prehrávania hudby, efekty:

- Fungujú v **reálnom čase** na všetkom, vrátane cloudových súborov, streamov a modulovej hudby.
- **Nikdy nemenia ani znovu neukladajú** vaše súbory. Vypnite efekt a originál sa vráti.
- **Pamätajú si vaše nastavenia** pre každý efekt.
- Môžu byť voľne **kombinované**, keďže každý je samostatný.

## Jednoduché recepty na vyskúšanie

**Každodenné počúvanie**

- **Viac basov, čisto:** Ekvalizér > Bass Booster, potom znížte Predzosilňovač o 1 až 2 dB. Alebo pridajte DSP Low Shelf na Bass Boost.
- **Vyrovnaná hlasitosť v zmiešanom playliste:** Volume Normalization > Standard, plus Compressor > Soft.
- **Jemné celkové vyleštenie:** Compressor > Transparent, plus Volume Normalization > Light.
- **Čistejšie vokály:** Ekvalizér > Vocal Booster, alebo DSP blok Peaking na Vocal Boost.
- **Plnší zvuk na malých reproduktoroch telefónu:** Ekvalizér > Small Speakers.

**Slúchadlá**

- **Príjemnejšie, menej únavné na slúchadlách:** Crossfeed > Chu Moy alebo Jan Meier.
- **Širší zvuk na slúchadlách:** DSP Stereo Width > Wide, plus Crossfeed > Chu Moy.
- **Oprava tvrdo panorámovaných platní zo 60. a 70. rokov:** Crossfeed > Vintage Stereo.
- **Trochu vzduchu a priestoru:** Freeverb > Ambience, udržaný nízko, plus Crossfeed > Subtle.

**Tiché časy a hovorené audio**

- **Nočné tiché počúvanie:** Volume Normalization > Night, plus Compressor > Late Night.
- **Podcasty a audioknihy:** Compressor > Voice / Podcast, plus Ekvalizér > Spoken Word.
- **Najhlasnejší, najvyrovnanejší zvuk v hlučnom aute:** Volume Normalization > Strong, plus Compressor > Heavy.

**Riešenie problémov**

- **Skrotenie ostrej, jasnej nahrávky:** Ekvalizér > Treble Reducer, alebo DSP blok Peaking na Tame Harsh.
- **Odstránenie elektrického brumu:** DSP reťazec > Notch > Mains Hum 60 (alebo Mains Hum 50 v Európe).
- **Tesnejšie, čistejšie basy:** DSP High Pass > Tighten, na rezanie dunivých spodných frekvencií.
- **Menej dunenia v mixe s ťažkými basmi:** DSP Low Shelf > Trim Bass, alebo Peaking > De-Boom.

**Kreatívne a zábavné**

- **Teplý, priestranný pocit:** Freeverb > Hall, udržaný nízko.
- **Snové, priestranné gitary:** Chorus > Wide, plus Echo > Long.
- **Retro lo-fi:** DSP reťazec > Bit Crusher (LoFi) do Soft Clip (Warm).
- **Funky pohyb na elektronických skladbách:** Auto Wah > Funky, alebo Phaser > Fast.
- **Klasické zasvišťanie prúdového lietadla:** Flanger > Jet.

## Časté otázky

{{% details title="Aký zvukový engine používa Flacbox?" closed="true" %}}
Vyberiete si jeden Prehrávací engine v Nastavenia > Audio prehrávač: Standard (systémový engine od Apple), Universal (engine FFmpeg) alebo Sound FX (engine BASS™ od Un4seen Developments, un4seen.com). Engine, ktorý zvolíte, rozhoduje o tom, ktoré formáty súborov sa prehrajú. Sound FX je ten, ktorý prehráva ďalšie formáty ako FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus a MOD alebo tracker hudbu, a je jediným enginom, ktorý poskytuje živé efekty, 10-pásmový ekvalizér a DSP reťazec. Ak chcete používať efekty, nastavte Prehrávací engine na Sound FX.
{{% /details %}}

{{% details title="Dokáže Flacbox prehrávať MOD, XM, IT a inú tracker alebo modulovú hudbu?" closed="true" %}}
Áno. Engine BASS™ má vstavaný modulový prehrávač, ktorý načíta súbory MOD, XM, IT, S3M, MTM, UMX a MO3 a znovu skladá skladbu naživo z jej vzorov a zvukov nástrojov, tak ako sa má tracker hudba prehrávať. Bežné iPhone prehrávače to nedokážu. Efekty a ekvalizér fungujú aj na modulovej hudbe.
{{% /details %}}

{{% details title="Podporuje Flacbox DSD a súbory s vysokým rozlíšením?" closed="true" %}}
Áno. Flacbox prehráva DSD súbory (DSF a DFF) cez engine BASS™ pomocou DSD cez PCM, takže fungujú na bežnom výstupnom hardvéri, plus FLAC, WavPack, Monkey's Audio (APE), Musepack a TrueAudio pre bezstratové prehrávanie.
{{% /details %}}

{{% details title="Aké zvukové efekty má Flacbox?" closed="true" %}}
10-pásmový ekvalizér, Volume Normalization, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate a Crossfeed, plus vlastný DSP reťazec s filtrami, shelfmi, gainom, soft clipom, bit crusherom, ring modulátorom, tremolom, delayom a stereo šírkou. Každý je samostatný a dá sa kombinovať s ostatnými.
{{% /details %}}

{{% details title="Čo je preset?" closed="true" %}}
Preset je hotové nastavenie efektu. Namiesto toho, aby ste sami pohybovali posuvníkmi, ťuknete na preset a zvuk sa mu prispôsobí. Každý efekt vo Flacboxe má niekoľko presetov a tento sprievodca uvádza, čo každý z nich robí. Ak po výbere presetu pohnete posuvníkom, efekt zobrazí „Manual“, aby vám povedal, že teraz používa vaše vlastné hodnoty.
{{% /details %}}

{{% details title="Ako otvorím zvukové efekty vo Flacboxe?" closed="true" %}}
Otvorte prehrávač Práve hrá, ťuknite na tlačidlo ⋯ (Viac) a zvoľte Zvukové efekty. Alebo prejdite na Nastavenia > Audio prehrávač > Zvukové efekty. Ťuknite na efekt, zapnite jeho prepínač a vyberte preset, alebo otvorte posuvníky na doladenie.
{{% /details %}}

{{% details title="Kde je ekvalizér a aké sú najlepšie nastavenia?" closed="true" %}}
Prejdite na Nastavenia > Audio prehrávač > Zvukový ekvalizér. Má 10 pásiem od 32 Hz do 16 kHz, každé od -12 do +12 dB, plus Predzosilňovač od -24 do +24 dB a 22 presetov. Pre viac basov použite Bass Booster. Pre čistejšie hlasy použite Vocal Booster alebo Pop. Pre jasnejší zvuk použite Treble Booster. Potom upravte jednotlivé pásma podľa chuti.
{{% /details %}}

{{% details title="Ako zosilním basy vo Flacboxe?" closed="true" %}}
Dva jednoduché spôsoby. V Zvukovom ekvalizéri vyberte Bass Booster (alebo zdvihnite pásma 32 Hz a 64 Hz o pár dB). Alebo v Spracovaní signálu pridajte blok Low Shelf nastavený na Bass Boost. V oboch prípadoch znížte Predzosilňovač alebo pridajte blok Gain o 1 až 2 dB, aby basy zostali čisté a neskreslili sa.
{{% /details %}}

{{% details title="Ktorý preset ekvalizéra je najlepší pre moju hudbu?" closed="true" %}}
Rock a Electronic pridávajú energiu silnými spodnými a hornými frekvenciami. Acoustic, Jazz a Classical zostávajú teplé a prirodzené. Pop a Vocal Booster tlačia hlasy dopredu. Bass Booster a Hip-Hop pridávajú váhu. Deep a Loudness znejú plnšie pri nízkej hlasitosti. Začnite tým, ktorý zodpovedá vášmu žánru, potom dolaďte.
{{% /details %}}

{{% details title="Čo je Volume Normalization a čím sa líši od ReplayGain?" closed="true" %}}
Zabezpečí, že každá skladba hrá zhruba pri rovnakej hlasitosti. Meria skutočnú hlasitosť pomocou štandardu EBU R128 (v LUFS, ako streamovacie služby) a upravuje každú skladbu smerom k vášmu cieľu, s limitom max-boost. Na rozdiel od ReplayGain nepotrebuje žiadne tagy vo vašich súboroch a funguje na akomkoľvek zdroji, naživo, bez zmeny zvuku. Presety: Light, Standard, Strong a Night.
{{% /details %}}

{{% details title="Čo je Crossfeed a mal by som ho používať?" closed="true" %}}
Crossfeed zmiešava trochu ľavého a pravého kanála dokopy, takže slúchadlá pôsobia viac ako skutočné reproduktory a menej ako keby bol zvuk uväznený vo vašej hlave. Je iba pre slúchadlá, takže ho pre reproduktory vypnite. Flacbox používa metódu bs2b (Bauer), s presetmi ako Chu Moy a Jan Meier.
{{% /details %}}

{{% details title="Aký je rozdiel medzi Compressorom a Volume Normalization?" closed="true" %}}
Volume Normalization zosúlaďuje hlasitosť medzi rôznymi skladbami. Compressor vyrovnáva hlasné a tiché časti vnútri jednej skladby. Riešia rôzne problémy a fungujú spolu dobre, najmä v aute alebo na hlučnom mieste.
{{% /details %}}

{{% details title="Čo je reťazec Spracovanie signálu (DSP)?" closed="true" %}}
Je to vlastný rack v Nastavenia > Audio prehrávač > Spracovanie signálu. Pridajte bloky ako filtre, shelfy, gain, soft clip, bit crusher, ring modulátor, tremolo, delay a stereo šírku, dajte ich do ľubovoľného poradia, každý zapnite alebo vypnite a namierte reťazec na všetky kanály, ľavý alebo pravý. Keďže na poradí záleží, môžete navrhnúť presne taký zvuk, aký chcete.
{{% /details %}}

{{% details title="Aký je rozdiel medzi Ekvalizérom, efektmi a DSP reťazcom?" closed="true" %}}
Ekvalizér je jednoduché 10-pásmové ovládanie tónu. Zvukové efekty sú hotové nástroje (compressor, reverb, echo a tak ďalej) s presetmi. DSP reťazec je miesto, kde si postavíte vlastné poradie efektov z jednotlivých blokov. Všetky tri môžete spustiť súčasne.
{{% /details %}}

{{% details title="Menia alebo poškodzujú efekty moje hudobné súbory?" closed="true" %}}
Nie. Všetko sa aplikuje naživo počas prehrávania hudby. Vaše súbory sa nikdy nemenia ani znovu neukladajú. Vypnite efekt a pôvodný zvuk sa okamžite vráti.
{{% /details %}}

{{% details title="Môžem použiť viac ako jeden efekt súčasne?" closed="true" %}}
Áno. Každý efekt má vlastný prepínač a neexistuje žiadny hlavný prepínač, takže funguje akákoľvek kombinácia. Napríklad Volume Normalization plus Compressor pre vyrovnané počúvanie, alebo Freeverb plus Crossfeed na slúchadlách, s ekvalizérom navrchu.
{{% /details %}}

{{% details title="Prečo sú ovládače efektu zošednuté?" closed="true" %}}
Efekt je vypnutý. Zapnite jeho prepínač na vrchu editora, aby ste mohli používať ovládače. Každý efekt je predvolene vypnutý.
{{% /details %}}

{{% details title="Čo znamená označenie Manual?" closed="true" %}}
Znamená to, že ste pohli posuvníkom preč od presetu, takže efekt teraz používa vaše vlastné hodnoty namiesto pomenovaného presetu. Každý posuvník má tlačidlo na obnovenie a opätovný výber presetu nahradí vaše manuálne hodnoty.
{{% /details %}}

{{% details title="Môžem uložiť a zdieľať svoje presety ekvalizéra?" closed="true" %}}
Áno. Okrem 22 vstavaných presetov si môžete vytvoriť vlastné, zmeniť ich poradie a exportovať alebo importovať ich, aby ste svoje nastavenia preniesli na iné zariadenie.
{{% /details %}}

{{% details title="Fungujú efekty s CarPlay, streamovaním a prehrávaním na pozadí?" closed="true" %}}
Áno. Efekty bežia vnútri enginu BASS™, takže sa aplikujú na lokálne súbory, cloudové úložiská, mediálne servery, streamy a modulovú hudbu, a fungujú aj počas CarPlay a prehrávania na pozadí.
{{% /details %}}

{{% details title="Môžem zmeniť kvalitu zvukového výstupu?" closed="true" %}}
Áno. V Nastavenia > Audio prehrávač môžete nastaviť výstupnú vzorkovaciu frekvenciu, počet kanálov a veľkosť bufferu tak, aby ladili s vašimi slúchadlami, reproduktormi alebo DAC.
{{% /details %}}

{{% details title="Aké je dobré východiskové nastavenie pre slúchadlá?" closed="true" %}}
Zapnite Volume Normalization (Standard), pridajte ľahký Compressor (Soft), vyberte preset ekvalizéra, ktorý sa vám páči, a zapnite Crossfeed (Chu Moy alebo Jan Meier). Nechajte reverb, echo a distortion vypnuté, pokiaľ nechcete kreatívny zvuk.
{{% /details %}}

---

*BASS je ochranná známka Un4seen Developments Ltd. Pozrite [un4seen.com](https://www.un4seen.com/). Crossfeed používa algoritmus bs2b (Bauer stereophonic-to-binaural); pozrite [stránku projektu bs2b](https://bs2b.sourceforge.net/).*
