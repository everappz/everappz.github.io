---
title: "Jak používat zvukové efekty a DSP ve Flacboxu: Compressor, Freeverb, Crossfeed, Echo, normalizace hlasitosti a další (každý preset a nastavení vysvětleny)"
date: 2026-07-24
description: "Kompletní průvodce zvukem ve Flacboxu na iPhonu, iPadu a Macu. Zjistěte, jak funguje engine BASS, které další formáty přehrává (včetně hudby MOD a tracker music a DSD) a co přesně dělá s vaším zvukem každý efekt, každý posuvník a každý preset, plus 10pásmový ekvalizér a vlastní DSP řetězec."
keywords: ["Flacbox zvukové efekty", "Flacbox presety vysvětleny", "Flacbox engine BASS", "audio knihovna BASS iOS", "přehrávač MOD hudby iPhone", "přehrávač tracker music iOS", "přehrát MOD XM IT S3M iPhone", "DSD přehrávač iOS", "FLAC přehrávač iPhone", "bezztrátový hudební přehrávač iOS", "Flacbox presety ekvalizéru", "10pásmový ekvalizér iPhone", "normalizace hlasitosti iPhone", "EBU R128 iOS", "normalizace hlasitosti hudební přehrávač", "crossfeed sluchátka iOS", "bs2b crossfeed", "presety kompresoru hudební přehrávač", "freeverb reverb iOS", "echo delay hudební přehrávač", "DSP řetězec hudební přehrávač", "zesílení basů iPhone", "jak přidat efekty do hudby Flacbox", "nejlepší nastavení ekvalizéru iPhone"]
tags: ["Flacbox", "Zvukové efekty", "Návod", "BASS", "Ekvalizér", "Zesílení basů", "Compressor", "Freeverb", "Crossfeed", "Echo", "Normalizace hlasitosti", "EBU R128", "MOD hudba", "Tracker hudba", "DSD", "FLAC", "DSP", "Sluchátka", "Presety"]
readingTime: 30
---

{{< author-byline >}}

**Krátká odpověď:** Ve Flacboxu si zvolíte jeden **přehrávací engine** v **Nastavení > Audio přehrávač**: **Standard** (systémový engine Apple), **Universal** (engine FFmpeg) nebo **Sound FX** (**engine BASS™**). Engine, který zvolíte, rozhoduje o tom, které formáty souborů se přehrají, takže na volbě záleží. Engine **Sound FX** přehrává další formáty, které většina aplikací pro iPhone vynechává (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus a starou **hudbu MOD a tracker music** jako MOD, XM, IT a S3M), a je jediným enginem, který pohání zvukové nástroje: **10pásmový ekvalizér**, **normalizaci hlasitosti**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** a vlastní **DSP řetězec**. Chcete-li tedy používat efekty z tohoto průvodce, nastavte nejprve přehrávací engine na **Sound FX**. Každý nástroj má připravené **presety**. Otevřete je v **Nastavení > Audio přehrávač** (Audio efekty, Audio ekvalizér, Zpracování signálu), nebo klepněte na tlačítko **⋯ (Další akce)** v přehrávači a zvolte **Audio efekty**. Nic, co zde uděláte, nikdy nezmění vaše soubory.

> Vysvětlení posuvníků a presetů níže jsou stejné krátké popisy, které Flacbox zobrazuje uvnitř aplikace, doplněné o trochu více souvislostí, abyste měli úplný přehled, než klepnete.

## Jak číst tohoto průvodce

Každý nástroj funguje stejně:

1. **Zapněte ho.** Každý efekt má vlastní vypínač. Zpočátku jsou všechny vypnuté. Můžete jich zapnout současně tolik, kolik chcete.
2. **Vyberte preset.** Preset je připravené nastavení. Klepněte na některý a zvuk se okamžitě změní. Tento průvodce uvádí, co dělá **každý** preset.
3. **Dolaďte (volitelně).** Otevřete posuvníky a upravte je ručně. Ve chvíli, kdy posuvníkem pohnete, efekt zobrazí **Manual**, takže víte, že jste preset opustili. Každý posuvník má tlačítko reset.

Nic se neukládá do vašich souborů. Jsou to živé efekty. Vypněte efekt a váš původní zvuk se ihned vrátí.

## Vyberte si přehrávací engine (efekty má Sound FX)

Flacbox enginy nekombinuje dohromady. Vyberete si **jeden** v **Nastavení > Audio přehrávač > Přehrávací engine** a engine, který zvolíte, rozhoduje o tom, které formáty souborů můžete přehrávat a zda jsou efekty k dispozici. Existují tři volby, zobrazené v aplikaci pod těmito přesnými názvy:

1. **Standard.** Vestavěný systémový engine Apple. Používá hardwarové dekódování pro nižší spotřebu baterie.
2. **Universal.** Engine FFmpeg, který otevírá velmi širokou škálu formátů.
3. **Sound FX.** **Engine BASS™.** Přehrává bezztrátové a vysokorozlišené soubory s plnou přesností, přidává modulovou (tracker) hudbu a pohání každý efekt, 10pásmový ekvalizér a DSP řetězec z tohoto průvodce.

Protože každý engine podporuje vlastní sadu formátů, soubory, které můžete přehrávat, se mění podle zvoleného enginu. Ještě důležitější je, že efekty, ekvalizér a DSP řetězec fungují **pouze** s enginem **Sound FX**, takže jej zvolte jako první, pokud je chcete používat.

Sound FX je postaven na **BASS™**, profesionální audio knihovně od Un4seen Developments. Více se o ní dočtete na její domovské stránce [un4seen.com](https://www.un4seen.com/).

## Hudební formáty: co přidává engine Sound FX (BASS™) (včetně hudby MOD a tracker music)

S vybraným enginem **Sound FX (BASS™)** přehrává Flacbox níže uvedené specializované formáty navíc k těm každodenním. Nejzvláštnější je **modulová hudba**, také nazývaná **tracker music**. Modulový soubor není běžná nahrávka. Obsahuje malé zvuky nástrojů plus „partituru“, která říká, jak je přehrát, a Flacbox skladbu z této partitury živě znovu sestavuje, tak jak měly být tyto soubory přehrávány. Běžné přehrávače to nedokáží.

| Typ hudby | Formáty | Dobré vědět |
|---|---|---|
| **Modulová / tracker hudba** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Živě znovu sestavena modulovým přehrávačem BASS™. Skvělá pro chiptunes a staré písně demoscény nebo Amigy. |
| **Moderní bezztrátové** | FLAC | Plná kvalita, menší než WAV. |
| **Další bezztrátové** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Méně běžné bezztrátové typy, všechny podporovány. |
| **Vysokorozlišené DSD** | DSF, DFF | Přehrává se na běžném hardwaru pomocí DSD over PCM. |
| **Moderní ztrátové** | Opus, Ogg Vorbis, MP3 | Obvyklé streamovací a stahovací typy. |

Engine Sound FX přehrává také běžné formáty Apple (AAC, ALAC, M4A, WAV, AIFF) a živé streamy, takže efekty a ekvalizér fungují i na nich.

**Proč vám to pomáhá:** pokud máte směs alb FLAC, vysokorozlišené soubory DSD a složku starých písní MOD nebo XM tracker, Flacbox je přehraje všechny a ekvalizér i efekty fungují na každém z nich.

## Tři nabídky, které budete používat

Flacbox uchovává své zvukové nástroje na třech místech, všechny uvnitř nastavení audio přehrávače. Nejprve se ujistěte, že váš **přehrávací engine** je nastaven na **Sound FX** (Nastavení > Audio přehrávač > Přehrávací engine), protože efekty, ekvalizér a DSP řetězec jsou k dispozici pouze s tímto enginem.

- **Audio efekty** (rack efektů): otevřete přehrávač, klepněte na **⋯ (Další akce)**, klepněte na **Audio efekty**. Nebo přejděte na **Nastavení > Audio přehrávač > Audio efekty**.
- **Audio ekvalizér** (10 pásem a presety): **Nastavení > Audio přehrávač > Audio ekvalizér**.
- **Zpracování signálu** (váš vlastní DSP řetězec): **Nastavení > Audio přehrávač > Zpracování signálu**.

V **Nastavení > Audio přehrávač** můžete také nastavit **výstupní vzorkovací frekvenci**, **kanály** a **velikost bufferu**.

## 10pásmový ekvalizér

**Co dělá:** Mění tón hudby, od hlubokých basů po jasné výšky. Je to nejlepší nástroj pro čisté **zesílení basů** nebo jasnější, čistější horní pásmo. Představte si jej jako deset knoflíků hlasitosti, každý pro jiný výsek zvuku. Zvedněte pásmo, abyste tuto část přivedli dopředu, snižte jej, abyste ji stáhli zpět. Malé změny o pár dB obvykle znějí nejlépe a funguje to na všem, co přehráváte.

**Jak to funguje:** Deset posuvníků na **32, 64, 125, 250, 500 Hz a 1, 2, 4, 8, 16 kHz**. Každý jde od **-12 dB (cut)** do **+12 dB (boost)**. K dispozici je také **Preamplifier** od **-24 do +24 dB** pro celkovou úroveň. Můžete si uložit vlastní presety a **exportovat nebo importovat** je mezi zařízeními.

**Co dělá každý vestavěný preset (22 presetů):**

| Preset | Co dělá s vaším zvukem |
|---|---|
| **Flat** | Žádná změna. Všechna pásma na nule. Čistý výchozí bod. |
| **Acoustic** | Teplé basy a čisté, přítomné výšky. Akustické kytary a hlasy působí přirozeně a živě. |
| **Bass Booster** | Silné zvednutí v nízkém pásmu, středy a výšky nedotčeny. Více úderu a váhy. |
| **Bass Reducer** | Snižuje nízké pásmo. Užitečné pro dunivé místnosti, levná sluchátka nebo těžké skladby. |
| **Treble Booster** | Zvedá pouze výšky. Přidává jiskru a vzdušnost, více detailu. |
| **Treble Reducer** | Zjemňuje výšky. Krotí ostré nebo pronikavé nahrávky. |
| **Classical** | Plné basy a jemné výšky s mírným poklesem středů. Hladké a prostorné pro orchestrální hudbu. |
| **Dance** | Velké basy a jasné výšky s vydlabanými středy. Úderné a energické pro klubové skladby. |
| **Deep** | Teplé, husté nízké pásmo s jemnějšími výškami. Útulný, uvolněný zvuk. |
| **Electronic** | Silné basy a jasné výšky pro syntezátory a beaty. Široké a moderní. |
| **Hip-Hop** | Těžké basy a čisté výšky s kontrolovanými středy. Vážné a úderné. |
| **Jazz** | Teplé a hladké, s malým poklesem středů. Snadné a přirozené pro akustický jazz. |
| **Latin** | Zvednuté basy a výšky s čistými středy. Jasné a živé. |
| **Loudness** | Silně zvedá basy a výšky (křivka „smile“). Zní plněji při nízké hlasitosti. |
| **Lounge** | Vysunuté středy s měkkými hranami. Uvolněné a vhodné pro vokály. |
| **Piano** | Čisté středy a výšky, aby tóny klavíru zněly čistě. |
| **Pop** | Zvednuté středy pro vokály, s basy a výškami staženými zpět. Hlasy jsou v popředí. |
| **R&B** | Velmi silné teplo nízkých středů a čisté výšky. Hladké a bohaté. |
| **Rock** | Zvednuté basy a výšky pro kytary a bicí. Energické a plné. |
| **Small Speakers** | Zvedá basy a snižuje výšky, aby drobné reproduktory zněly plněji. |
| **Spoken Word** | Zvedá hlasové pásmo a snižuje hluboké basy. Řeč je zřetelná. |
| **Vocal Booster** | Vysunuje střed, kde sídlí hlasy, a snižuje okolí. Vokály vyniknou. |

**Tip pro basy:** Začněte s **Bass Booster**, a pokud to zní zabláceně, stáhněte Preamplifier o 1 až 2 dB, aby nic nezkreslovalo.

## Normalizace hlasitosti (vyrovnaná hlasitost)

**Co dělá:** Některé skladby hrají hlasitěji než jiné, takže neustále měníte hlasitost. Tohle způsobí, že každá skladba hraje sama o sobě zhruba stejně hlasitě, takže to nemusíte dělat vy. Je to ideální pro zamíchané playlisty, které kombinují staré a nové nahrávky, různá alba nebo různé zdroje, kde jedna skladba může být mnohem hlasitější než další.

**Jak to funguje:** Naslouchá skutečné hlasitosti každé skladby pomocí standardu **EBU R128** (měřeno v **LUFS**, stejný princip, jaký používají streamovací služby), a poté každou skladbu přizpůsobuje k vašemu cíli. Nepotřebuje žádné tagy ve vašich souborech a nikdy nemění zvuk. EBU R128 měří hlasitost, kterou vaše uši skutečně vnímají v celé skladbě, ne jen nejvyšší špičku, a proto odpovídá tomu, jak hlasité vám skladby doopravdy připadají. Flacbox to vypočítává živě, jak hudba hraje (a kontroluje hlasitost dopředu, když může), a poté na skladbu aplikuje jedinou, stálou změnu hlasitosti. Limit **Max boost** brání tomu, aby velmi tiché nahrávky byly zesíleny tak silně, že by zkreslovaly. Protože čte samotný zvuk, funguje na jakémkoli zdroji, včetně cloudových souborů, živých streamů a modulové hudby, i když soubory nemají žádné tagy hlasitosti.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Target loudness** | Nastavuje hlasitost, k níž je každá skladba vyrovnávána. Vyšší hodnoty způsobí, že vše hraje celkově hlasitěji. | -30 až -6 LUFS (-16) |
| **Max boost** | Omezuje, jak moc mohou být tiché skladby zesíleny. Vyšší hodnoty přiblíží tiché nahrávky k cíli. | 0 až 24 dB (12) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Light** | Jemné vyrovnání pro nenáročný poslech. Vyrovná zjevné skoky hlasitosti, aniž by tiché skladby silně vytlačoval. |
| **Standard** | Univerzální výchozí. Cíl hlasitosti ve stylu streamu, který vyhovuje většině hudby. Začněte zde. |
| **Strong** | Agresivní vyrovnání, které tiché skladby pevně vytlačuje nahoru. Nejlepší pro smíšené knihovny s velkými rozdíly v úrovni. |
| **Night** | Tišší celkový cíl, který stále pozvedá tiché pasáže, takže noční poslech zůstává konzistentní a tichý. |

## Compressor (vyrovnání hlasitých a tichých částí)

**Co dělá:** V jedné skladbě mohou být tiché části příliš tiché a hlasité části příliš hlasité. Tohle je přiblíží k sobě, takže je celá skladba dobře slyšet, i v autě nebo na hlučném místě. Jemně ztlumí nejhlasitější momenty a pozvedne tišší, takže během jedné skladby přestanete sahat po hlasitosti. To se liší od normalizace hlasitosti: Compressor vyrovnává věci **uvnitř** jedné skladby, zatímco normalizace hlasitosti sjednocuje hlasitost **mezi** skladbami. Ty dva spolu dobře fungují. Začněte s presetem a posuvníky otevřete jen tehdy, chcete-li větší kontrolu.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Threshold** | Úroveň, kde komprese začíná. Nižší hodnoty zmáčknou více zvuku a udrží tiché a hlasité části blíže u sebe. | -60 až 0 dB (-20) |
| **Ratio** | Jak silně jsou hlasité části drženy zpět, jakmile překročí práh. Vyšší hodnoty komprimují silněji a udrží zvuk vyrovnanější. | 1:1 až 30:1 (4:1) |
| **Attack** | Jak rychle efekt reaguje na náhlou hlasitou špičku. Krátké hodnoty zachytí transienty; delší je propustí. | 0,1 až 1000 ms (10 ms) |
| **Release** | Jak rychle efekt povolí poté, co hlasitá část odezní. Krátké hodnoty mohou pumpovat; delší znějí hladčeji. | 10 ms až 5 s (100 ms) |
| **Master gain** | Konečné zesílení výstupu aplikované po zpracování. Zvyšte je, abyste pozvedli celkovou hlasitost, jakmile je dynamika vyrovnaná. | -30 až +30 dB (0) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Transparent** | Sotva znatelná záchranná síť. Zachovává dynamiku téměř úplně a zachytí jen nejhlasitější špičky. |
| **Soft** | Lehké vyrovnání pro hi-fi poslech doma. Jemné vyhlazení bez zmáčknutí hudby. |
| **Standard** | Rozumné výchozí nastavení pro každodenní přehrávání hudby. První preset, který vyzkoušet. |
| **Heavy** | Agresivní vyrovnání pro hlučná prostředí. Auto, přeplněná místnost, poslech při nízké hlasitosti. |
| **Voice / Podcast** | Vyladěno pro řeč. Pomalejší attack propustí sykavky, štědrý makeup gain pozvedne vokály. |
| **Old Recordings** | Vintage alba a restaurované vinyly, kde je průměrná úroveň nižší než u moderních vydání. |
| **Late Night** | Silná komprese plus velké zesílení pro tichý poslech, když záleží na sousedech nebo spící rodině. |
| **Movie Dialog** | Pozvedne mluvené slovo proti hudbě a zvukovým efektům v pestrém soundtracku. |
| **Streaming Match** | Cílí přibližně na normalizaci hlasitosti moderních streamovacích služeb kolem -14 LUFS. |
| **Maximum Loudness** | Naplno. Naráží na limiter; očekávejte zmáčknutý, velmi vyrovnaný signál. Doslovný preset maximální hlasitosti. |

## Freeverb (reverb, pocit prostoru)

**Co dělá:** Přidává hudbě pocit prostoru, od malé místnosti až po velký sál. Vyberte preset, nebo si sami dolaďte poměr dry a wet, velikost místnosti, damping a šířku. Reverb je přirozený dozvuk, který slyšíte v jakémkoli reálném prostoru, a Freeverb jej znovu vytváří softwarově. Trocha způsobí, že ploché nebo zblízka nasnímané nahrávky působí otevřeněji a živěji. Hodně umístí hudbu do velkého, vzdáleného prostoru. Je to kreativní efekt, takže pro přirozené výsledky udržujte wet mix mírný.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Dry mix** | Kolik z původního, nedotčeného zvuku zůstane. Vyšší hodnoty ponechají v mixu více dry signálu. | 0 až 1 (0.0) |
| **Wet mix** | Kolik dozvučeného zvuku se přidá. Vyšší hodnoty učiní reverb hlasitějším a zřetelnějším. | 0 až 3 (1.0) |
| **Room size** | Velikost představovaného prostoru. Vyšší hodnoty dávají delší, větší dozvukový ocas, od malé místnosti po katedrálu. | 0 až 1 (0.5) |
| **Damp** | Jak rychle vysoké frekvence v ocase zanikají. Vyšší hodnoty učiní reverb tmavším a teplejším. | 0 až 1 (0.5) |
| **Width** | Stereo rozprostření reverbu. Vyšší hodnoty učiní prostor širším mezi levým a pravým kanálem. | 0 až 1 (1.0) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Room** | Malý, těsný prostor. Jemná ambience, která přidá pocit místa, aniž by zvuk zaplavila. |
| **Studio** | Suchá, kontrolovaná nahrávací místnost. Právě tolik odrazu, aby to znělo přirozeně. |
| **Hall** | Velký koncertní sál. Dlouhý, bujný ocas, který se hodí k orchestrální a akustické hudbě. |
| **Cathedral** | Obrovský, ozvěnou naplněný kamenný prostor. Nejdelší, nejdramatičtější dozvukový ocas. |
| **Plate** | Jasný, hustý studiový plátový reverb. Klasika pro vokály a bicí. |
| **Ambience** | Krátká, vzdušná ambience. Přidá lehký pocit prostoru a přitom zůstává většinou suchá. |

## Auto Wah (funkové ladění filtru)

**Co dělá:** Filtr, který sám od sebe přejíždí nahoru a dolů pro funkový, hlasu podobný zvuk wah. Vyberte preset, nebo si sami nastavte wet mix, feedback, rychlost, rozsah a frekvenci. Je to stejný sweep „wah“, jaký vytváří kytarový wah pedál, ale zde se pohybuje sám v rytmu hudby. Skvěle zní na funku, disku a elektronických skladbách. Je to výrazný, zjevný efekt, takže při každodenním poslechu vydrží trocha dlouho.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Wet mix** | Jak silný je efekt wah v mixu. Vyšší hodnoty učiní přejíždějící filtr zřetelnějším. | -2 až +2 (1.5) |
| **Feedback** | Kolik z výstupu je přiváděno zpět do efektu. Vyšší hodnoty učiní wah rezonantnějším a výraznějším. | -1 až +1 (0.5) |
| **Rate** | Jak rychle filtr přejíždí nahoru a dolů. Vyšší hodnoty dávají rychlejší, rytmičtější wah. | 0,1 až 9 Hz (2.0) |
| **Range** | Jak daleko filtr přejíždí, v oktávách. Vyšší hodnoty dávají širší, dramatičtější sweep. | 0,1 až 9 oktáv (4.3) |
| **Frequency** | Základní frekvence, kolem které filtr přejíždí. Nižší hodnoty znějí hlouběji; vyšší jasněji. | 1 až 1000 Hz (50) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Classic** | Vyvážený, klasický sweep wah. Dobrý výchozí bod pro funk a rock. |
| **Slow** | Pomalý, široký sweep, který jemně pluje nahoru a dolů. Skvělé pro pady a dlouhé tóny. |
| **Funky** | Rychlý, úderný sweep se spoustou pohybu. Přidá rytmické kousnutí kytarám a syntezátorům. |
| **Deep** | Hluboký, široký sweep začínající z nízké frekvence. Velký a dramatický. |
| **Subtle** | Jemný, nenápadný pohyb. Přidá charakter, aniž by ovládl zvuk. |
| **Resonant** | Ostré, rezonantní wah s vysokým feedbackem. Hlasu podobné a expresivní. |

## Phaser (vířivý whoosh)

**Co dělá:** Přejíždějící filtr, který přidává zvuku vířivý, svištivý pohyb. Vyberte preset, nebo si sami nastavte feedback, rychlost, rozsah a frekvenci. Přidá jemný pohyb a třpyt, aniž by měnil tóny. Na vokálech a padech je nenápadný, na syntezátorech a kytarách dramatický. Vyzkoušejte Slow pro snový pocit nebo Jet pro silný vír.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Feedback** | Kolik z výstupu je přiváděno zpět do efektu. Vyšší hodnoty učiní phaser rezonantnějším a výraznějším. | -1 až +1 (0.0) |
| **Rate** | Jak rychle filtr přejíždí nahoru a dolů. Vyšší hodnoty dávají rychlejší, rytmičtější phasing. | 0,1 až 9 Hz (1.0) |
| **Range** | Jak daleko filtr přejíždí, v oktávách. Vyšší hodnoty dávají širší, dramatičtější sweep. | 0,1 až 9 oktáv (4.0) |
| **Frequency** | Základní frekvence, kolem které filtr přejíždí. Nižší hodnoty znějí hlouběji; vyšší jasněji. | 1 až 1000 Hz (100) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Classic** | Vyvážený, klasický sweep phaseru. Dobrý výchozí bod pro kytary a klávesy. |
| **Slow** | Pomalý, široký sweep, který jemně pluje nahoru a dolů. Skvělé pro pady a dlouhé tóny. |
| **Fast** | Rychlý, třpytivý sweep se spoustou pohybu. Přidá pohyb a energii. |
| **Deep** | Hluboký, široký sweep začínající z nízké frekvence. Velký a dramatický. |
| **Subtle** | Jemný, nenápadný pohyb. Přidá charakter, aniž by ovládl zvuk. |
| **Jet** | Intenzivní, rezonantní sweep s vysokým feedbackem, klasický whoosh tryskového letadla. |

## Flanger (sweep tryskového letadla)

**Co dělá:** Krátké, pohyblivé zpoždění, které dodá zvuku tryskový, přejíždějící whoosh. Vyberte preset, nebo si sami nastavte hloubku, feedback, rychlost a zpoždění. Je to silnější, kovovější bratranec phaseru, proslulý svištivým sweepem v klasickém rocku a elektronické hudbě. Jemná nastavení přidají mírný pohyb, zatímco hluboká nastavení jsou dramatická a zjevná. Nejlépe je používat střídmě, pro efekt.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Depth** | Jak silný je přejíždějící efekt. Vyšší hodnoty učiní flanging zřetelnějším. | 0 až 100% (25) |
| **Feedback** | Kolik z výstupu je přiváděno zpět do efektu. Vyšší hodnoty učiní flanger rezonantnějším a kovovějším. | -99 až +99% (-50) |
| **Rate** | Jak rychle se sweep pohybuje nahoru a dolů. Vyšší hodnoty dávají rychlejší, třpytivější pohyb. | 0 až 10 Hz (0.25) |
| **Delay** | Základní čas zpoždění, na kterém je sweep postaven. Vyšší hodnoty dávají hlubší, dutější charakter. | 0 až 4 ms (2.0) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Classic** | Vyvážený, klasický flanger. Dobrý výchozí bod pro kytary a klávesy. |
| **Subtle** | Jemný, nenápadný sweep. Přidá pohyb, aniž by ovládl zvuk. |
| **Deep** | Hluboký, těžký sweep se silným feedbackem. Velký a dramatický. |
| **Jet** | Intenzivní sweep s kladným feedbackem, klasický whoosh tryskového letadla. |
| **Fast** | Rychlý, třpytivý sweep se spoustou pohybu a energie. |
| **Wide** | Pomalý, široký sweep s dlouhým zpožděním. Bujný a prostorný. |

## Echo (opakování)

**Co dělá:** Opakuje zvuk jako zanikající ozvěny pro pocit prostoru a hloubky. Vyberte preset, nebo si sami nastavte wet mix, feedback a zpoždění. Je to jako když voláte v kaňonu: zvuk se po krátké mezeře jednou nebo vícekrát vrátí. Jediné krátké opakování přidá tělo a retro pocit, zatímco delší opakování s větším feedbackem vytvářejí prostorné, táhlé ocasy. Preset Ping Pong odráží opakování mezi vaším levým a pravým uchem, což je zábavné na sluchátkách. Udržujte wet mix mírný, aby ozvěny hudbu podpořily, spíše než ji zakryly.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Wet mix** | Jak hlasité jsou ozvěny ve srovnání s původním zvukem. Vyšší hodnoty učiní opakování výraznějšími. | -2 až +2 (0.6) |
| **Feedback** | Kolikrát se echo opakuje. Vyšší hodnoty dávají více opakování, která zanikají déle. | -1 až +1 (0.5) |
| **Delay** | Čas mezi ozvěnami. Kratší hodnoty dávají těsný slap-back; delší dávají rozprostřená opakování. | 0,01 až 2 s (0.4) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Slapback** | Jediné, těsné opakování hned za zvukem. Klasický rockabilly slap-back. |
| **Room** | Krátká, přirozená ozvěna, jako malá místnost. Přidá prostor, aniž by zvuk rozmazala. |
| **Tape** | Teplá, střední opakování, která postupně zanikají, jako staré páskové delay. |
| **Dub** | Dlouhá, těžká opakování se silným feedbackem. Velké, dubové a prostorné. |
| **Ping Pong** | Ozvěny se odrážejí mezi levým a pravým reproduktorem pro široký stereo efekt. |
| **Long** | Pomalá, široce rozprostřená opakování, která se táhnou daleko za zvukem. |

## Chorus (hustší, širší zvuk)

**Co dělá:** Zahušťuje a rozšiřuje zvuk vrstvením posunuté kopie přes originál. Vyberte preset, nebo si sami nastavte poměr wet/dry, hloubku, rychlost a feedback. Způsobí, že jeden nástroj nebo hlas zní jako několik hrajících společně, přidáním mírně rozladěných, pohyblivých kopií. To přidá bohatost a jemný třpyt. Jemná nastavení věci zahřejí, zatímco silná nastavení znějí bujně a snově. Je oblíbený na kytarách, klávesách a vokálech.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Wet/Dry** | Kolik chorusu slyšíte ve srovnání s původním zvukem. Vyšší hodnoty učiní efekt zřetelnějším. | 0 až 100% (50) |
| **Depth** | Jak daleko výška kolísá nahoru a dolů. Vyšší hodnoty dávají hustší, třpytivější zvuk. | 0 až 100% (25) |
| **Rate** | Jak rychle se třpyt pohybuje. Pomalejší rychlosti znějí jemně a bujně; rychlejší více jako vibrato. | 0 až 10 Hz (1.1) |
| **Feedback** | Kolik z efektu je přiváděno zpět do sebe. Vyšší hodnoty učiní chorus rezonantnějším a intenzivnějším. | -99 až +99% (25) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Subtle** | Jemné zahuštění, které přidá teplo, aniž by na sebe upozorňovalo. |
| **Lush** | Bohatý, klasický chorus. Skvělé univerzální nastavení pro kytary a klávesy. |
| **Ensemble** | Plný, vrstvený třpyt, který způsobí, že jeden nástroj zní jako několik. |
| **Vibrato** | Plně wet s rychlým tempem, pro kolísavé vibrato místo jemného chorusu. |
| **Wide** | Pomalý, široký třpyt, který otevírá stereo obraz. Prostorný a snový. |
| **Twelve-String** | Jasný, rezonantní třpyt připomínající dvanáctistrunnou kytaru. |

## Distortion (drsnost a hrana)

**Co dělá:** Přidává drsnost a hranu přebuzením zvuku. Vyberte preset, nebo si sami nastavte drive, output a tón. Záměrně zdrsňuje zvuk, od teplé, drsné hrany po zlomený, zkreslený tón. Je to kreativní, zábavný efekt spíše než způsob, jak zlepšit kvalitu, takže jej používejte v malém množství. Je zábavný na elektronických, rockových a experimentálních skladbách. Snižte Output, pokud je těžký preset příliš hlasitý.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Drive** | Jak silně je zvuk zkreslen. Vyšší hodnoty jsou drsnější a agresivnější. | 0 až 100% (15) |
| **Output** | Výstupní úroveň po zkreslení. Snižte ji, pokud je těžké nastavení příliš hlasité. | -60 až 0 dB (-18) |
| **Tone** | Odřezává výšky před zkreslením. Nižší hodnoty znějí tmavěji a tepleji. | 100 až 8000 Hz (8000) |
| **Center** | Kolem které frekvence je zkreslení soustředěno. Posouvá charakter jasněji nebo tmavěji. | 100 až 8000 Hz (2400) |
| **Width** | Jak široké je toto soustředění. Úzké zní ostře a nosově; široké zní plně a otevřeně. | 100 až 8000 Hz (2400) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Warm Drive** | Lehká, teplá drsnost, která přidá hranu bez velké změny charakteru. |
| **Crunch** | Klasický chrupavý overdrive, úderný a rytmický. |
| **Overdrive** | Jasný, přebuzený tón se spoustou kousnutí. Skvělé pro sólové zvuky. |
| **Fuzz** | Hustý, nasycený fuzz. Těžký a plný harmonických. |
| **Metal** | Těsný, na středy zaměřený high-gain tón pro agresivní, těžké zvuky. |
| **Screamer** | Overdrive se zvednutými středy, který proráží, jako tube screamer. |
| **LoFi** | Rozdrcené, úzkopásmové zkreslení pro drsný lo-fi charakter. |

## Rotate (rotující stereo)

**Co dělá:** Roztáčí zvuk kolem stereo pole pro rotační, vířivý efekt. Vyberte preset, nebo si sami nastavte rychlost. Pomalu pohybuje zvukem kolem vašich levých a pravých kanálů, trochu jako rotující reproduktor, což přidá vířivý, hypnotický pocit. Pomalá nastavení jsou jemná a široká, zatímco rychlá nastavení jsou závratná a zjevná. Je to stereo efekt, takže je nejvíce patrný na sluchátkách nebo dobře umístěných reproduktorech.

**Posuvník:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Rate** | Jak rychle se zvuk točí kolem stereo pole. Záporné hodnoty točí opačným směrem; nula jej drží na místě. | -5 až +5 Hz (1.0) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Slow Pan** | Pomalý, jemný posun ze strany na stranu. Nenápadný a široký. |
| **Sway** | Stálé kolébání zleva doprava. Přidá jemný pohyb stereo obrazu. |
| **Rotary** | Střední otáčení připomínající rotující reproduktor. |
| **Fast Spin** | Rychlé otáčení kolem stereo pole pro závratný, vířivý efekt. |
| **Reverse** | Střední otáčení v opačném směru. |
| **Whirl** | Velmi rychlý vír. Intenzivní a dezorientující. |

## Crossfeed (přirozený zvuk na sluchátkách)

Na reproduktorech každé z vašich uší slyší jak levý, tak pravý reproduktor, jen v mírně odlišných časech a hlasitostech. Na sluchátkách je toto přirozené prolínání pryč: vaše levé ucho slyší pouze levý kanál a pravé ucho pouze pravý. Toto „super stereo“ může způsobit, že hudba působí, jako by byla rozdělena uvnitř vaší hlavy, a tvrdě panorámované nahrávky, kde nástroj sedí zcela na jedné straně, mohou při dlouhém poslechu působit nepřirozeně nebo únavně.

Crossfeed to opravuje tím, že vmíchá malé, filtrované množství každého kanálu do druhého, s nepatrným zpožděním a jemným odřezáním vysokých frekvencí. To se blíží tomu, jak zvuk z reálných reproduktorů dosahuje obou vašich uší, včetně toho, jak vaše hlava mírně zastiňuje vzdálenější ucho. Výsledkem je přirozenější, reproduktorům podobný obraz, který sedí trochu před vámi místo uvnitř vaší hlavy, a snižuje únavu z poslechu při dlouhých sezeních. Flacbox používá dobře známou metodu **bs2b (Bauer stereophonic-to-binaural)**, uznávaný open-source crossfeed používaný mnoha audiofilskými přehrávači. O algoritmu si můžete přečíst na [stránce projektu bs2b](https://bs2b.sourceforge.net/).

**Cutoff** řídí, jak teple prolnutí zní, a **Feed level** řídí, jak silné je. Presety pokrývají klasické úrovně bs2b, od sotva znatelného doteku po pevné, reproduktorům podobné prolnutí. Crossfeed je efekt pro sluchátka, takže jej při poslechu na reproduktorech nechte vypnutý.

**Posuvníky:**

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Cutoff** | Nastavuje, kde se prosakování mezi kanály začne odřezávat. Nižší hodnoty dávají teplejší, výraznější efekt. | 300 až 2000 Hz (700) |
| **Feed level** | Řídí, kolik jednoho kanálu prosakuje do druhého. Vyšší hodnoty produkují reproduktorům podobnější zvuk. | 1 až 15 dB (4.5) |

**Presety:**

| Preset | Co dělá |
|---|---|
| **Subtle** | Sotva znatelný crossfeed pro nenáročný poslech. Změkčí tvrdě panorámované stereo bez změny tonální rovnováhy. |
| **Chu Moy** | Klasický univerzální výchozí. Vyvážený a lehce teplý, funguje téměř na jakémkoli materiálu. Začněte zde. |
| **Strong** | Silnější prosakování pro tvrději panorámované mixy. Zřetelnější zúžení sterea. |
| **Jan Meier** | Oblíbený mezi nadšenci do sluchátek. Širší přívod, reproduktorům podobnější podání, mírné zvednutí basů. |
| **Speaker-like** | Vyladěno pro nejpřirozenější reproduktorové podání přes sluchátka. |
| **Vintage Stereo** | Agresivní crossfeed vyladěný pro mixy z 60. a 70. let s tvrdě panorámovanými bicími a vokály. |

## Zpracování signálu: postavte si vlastní DSP řetězec

Kromě připravených efektů vám Flacbox umožňuje postavit si vlastní řetězec v **Nastavení > Audio přehrávač > Zpracování signálu**. Jak aplikace vysvětluje, když je řetězec prázdný: *„Klepnutím na + přidejte efekt. Každý zapněte nebo vypněte jeho vypínačem, přetažením změňte pořadí, klepnutím upravte jeho parametry a dlouhým stiskem duplikujte nebo smažte.“*

**Na pořadí záleží**: filtr před zkreslením zní jinak než stejný filtr za ním. Celý řetězec můžete také zaměřit na **Všechny kanály**, **Levý kanál** nebo **Pravý kanál**.

Níže je každý blok, s vlastním textem aplikace pro každý posuvník a každý preset.

### Gain (úprava úrovně)

Zvyšuje nebo snižuje úroveň v jednom bodě řetězce.

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Gain** | Zvyšuje nebo snižuje úroveň v tomto bodě řetězce. Použijte ji k doplnění úrovně po jiných efektech nebo k přebuzení těch, které následují. | -24 až +24 dB (0) |

| Preset | Co dělá |
|---|---|
| **Unity** | Žádná změna úrovně. Neutrální výchozí bod. |
| **Cut** | Velké snížení. Zkrotí hlasitý zdroj nebo udělá místo před následujícími efekty. |
| **Trim** | Jemné snížení, které stáhne úroveň trochu zpět. |
| **Lift** | Mírné zvednutí, které pozvedne tichý zdroj. |
| **Boost** | Silné zvednutí pro tichý materiál nebo pro silnější přebuzení následujících efektů. |
| **Max** | Maximální zvednutí. Hlasité, pozor na clipping později v řetězci. |

### Low Pass (odstraňuje výšky)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Cutoff** | Nastavuje, kde filtr začne odřezávat výšky. Snižte jej pro ztmavení a změkčení zvuku; zvedněte jej směrem k vrcholu pro plné otevření. | 20 Hz až 20 kHz (20 kHz) |
| **Resonance** | Zdůrazňuje frekvence přímo na cutoffu. Udržujte ji nízko pro čisté odřezání; zvyšte ji pro špičatou, pískavou hranu. | 0,1 až 10 (0.707) |

| Preset | Co dělá |
|---|---|
| **Air** | Odřeže jen úplný vrchol. Ubere trochu hrany bez otupení zvuku. |
| **Warm** | Jemné odřezání výšek pro teplejší, kulatější tón. |
| **Mellow** | Znatelně změkčeno. Stáhne jas zpět pro uvolněný pocit. |
| **Muffled** | Tmavé a tlumené, jako by slyšeno přes zeď. |
| **Telephone** | Úzká, rezonantní špička nízko v rozsahu. Tenký, telefonu podobný hlas. |

### High Pass (odstraňuje basy)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Cutoff** | Nastavuje, kde filtr začne odřezávat basy. Zvedněte jej pro ztenčení nízkého pásma a odstranění dunění; snižte jej směrem ke dnu pro plné otevření. | 20 Hz až 20 kHz (20 Hz) |
| **Resonance** | Zdůrazňuje frekvence přímo na cutoffu. Udržujte ji nízko pro čisté odřezání; zvyšte ji pro špičatou, pískavou hranu. | 0,1 až 10 (0.707) |

| Preset | Co dělá |
|---|---|
| **Rumble Cut** | Odstraní subsonické dunění a stejnosměrný posun bez dotčení slyšitelného nízkého pásma. |
| **Tighten** | Odřeže dunivé nízké frekvence pro těsnější, čistší basy. |
| **Thin** | Odřeže teplo a tělo a zanechá lehčí, tenčí zvuk. |
| **Radio** | Zůstávají jen středy a výšky, jako malý rádiový reproduktor. |
| **Telephone** | Úzká, rezonantní špička vysoko v rozsahu. Tenký, telefonu podobný hlas. |

### Band Pass (ponechá střední pásmo)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Center** | Nastavuje frekvenci, kterou filtr propouští. Vše nad a pod ní je odřezáno. Přejíždějte jím pro výběr basů, středů nebo výšek. | 20 Hz až 20 kHz (1 kHz) |
| **Resonance** | Řídí, jak široké je pásmo. Nízké hodnoty propustí široký rozsah; zvyšte ji pro zúžení na střed pro ostrý, rezonantní tón. | 0,1 až 10 (0.707) |

| Preset | Co dělá |
|---|---|
| **Voice** | Široké pásmo kolem středního pásma, kde sedí většina vokálů. Neutrální výchozí bod. |
| **Bass** | Izoluje nízké pásmo a zanechá jen basy a kopák. |
| **Body** | Zaměřuje se na nízké středy pro teplé, hranaté tělo. |
| **Presence** | Zvedá horní středy pro čistotu a přítomnost. |
| **Telephone** | Úzké pásmo středů. Tenký, telefonu podobný zvuk. |
| **Wah** | Velmi úzká, rezonantní špička. Přejíždějte středem pro efekt wah. |

### Notch (odstraňuje jedno úzké pásmo)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Frequency** | Nastavuje frekvenci, kterou filtr odstraňuje. Vše nad a pod ní projde. Nalaďte jej na hum nebo rezonanci, abyste ji vyřízli. | 20 Hz až 20 kHz (60 Hz) |
| **Resonance** | Řídí, jak široký je řez. Nízké hodnoty vydlabou široký rozsah; zvyšte ji pro odstranění jen bodového pásma a ponechání zbytku nedotčeného. | 0,1 až 10 (8.0) |

| Preset | Co dělá |
|---|---|
| **Mains Hum 60** | Odstraní 60Hz elektrický hum (severoamerická síť). Neutrální výchozí bod. |
| **Mains Hum 50** | Odstraní 50Hz elektrický hum (evropská a jiná síť). |
| **Rumble** | Odřeže nízkofrekvenční dunění nebo rezonanci bez ztenčení celého spodku. |
| **Mud** | Vydlabe zabahnění nízkých středů pro čistší, zřetelnější zvuk. |
| **Boxy** | Odstraní hranaté troubení středů. |
| **Harsh** | Zkrotí drsnou, pronikavou špičku v horních středech. |

### Peaking (parametrické EQ pásmo)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Frequency** | Střed pásma, které se má zvednout nebo snížit. Přejíždějte jím pro nalezení frekvence, kterou chcete tvarovat. | 20 Hz až 20 kHz (1 kHz) |
| **Gain** | Kolik zvednout nebo snížit ve středu. Kladné zvedá pásmo; záporné jej vydlabe. | -15 až +15 dB (0) |
| **Q factor** | Nastavuje, jak široké je pásmo. Nízké hodnoty tvarují širokou oblast; vysoké hodnoty zužují pro chirurgické, bodové změny. | 0,1 až 10 (1.0) |

| Preset | Co dělá |
|---|---|
| **Presence** | Široké zvednutí horních středů pro čistotu a přítomnost. Neutrální výchozí bod. |
| **Warmth** | Široké zvednutí nízkých středů, které přidá tělo a teplo. |
| **Vocal Boost** | Zvedá jádro vokálního pásma, aby přivedlo hlasy dopředu. |
| **Cut Mud** | Vydlabe hranaté zabahnění nízkých středů pro čistší zvuk. |
| **Tame Harsh** | Úzký řez pro zkrocení drsné, pronikavé špičky. |
| **Punch** | Nízké zvednutí, které přidá úder a nápor nízkému pásmu. |
| **Sub Boost** | Hluboké zvednutí úplně dole pro extra sub-basovou váhu. |
| **Air** | Široké zvednutí nahoře pro otevřený, vzdušný lesk. |
| **Clarity** | Zvedá vysoké středy, aby přidal definici a hranu. |
| **De-Ess** | Úzký řez v pásmu sykavek pro zkrocení drsných zvuků S. |
| **De-Boom** | Odřeže dunivé nízkofrekvenční nahromadění pro těsnější nízké pásmo. |
| **Scoop** | Široký pokles středů pro vydlabaný, moderní tón. |

### Low Shelf (řízení basů a zesílení basů)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Frequency** | Nastavuje roh, pod nímž se shelf uplatní. Vše pod ním je zvednuto nebo sníženo společně. | 20 až 2000 Hz (200) |
| **Gain** | Kolik zvednout nebo snížit nízké pásmo. Kladné přidává váhu a teplo; záporné jej ztenčuje. | -15 až +15 dB (0) |

| Preset | Co dělá |
|---|---|
| **Warmth** | Jemné zvednutí nízkého pásma pro teplo a tělo. Neutrální výchozí bod. |
| **Bass Boost** | Solidní zvednutí basů pro váhu a úder. |
| **Fullness** | Zaplní nízké středy pro plnější, kulatější zvuk. |
| **Trim Bass** | Mírné snížení pro odlehčení mixu s těžkými basy. |
| **Cut Lows** | Silné snížení pro ztenčení nebo odbublání nízkého pásma. |
| **Big Bottom** | Velké zvednutí nízkého pásma pro maximální váhu a dunění. |

### High Shelf (řízení výšek)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Frequency** | Nastavuje roh, nad nímž se shelf uplatní. Vše nad ním je zvednuto nebo sníženo společně. | 1 až 20 kHz (8 kHz) |
| **Gain** | Kolik zvednout nebo snížit vysoké pásmo. Kladné přidává jas a vzdušnost; záporné vyhlazuje a ztmavuje. | -15 až +15 dB (0) |

| Preset | Co dělá |
|---|---|
| **Presence** | Jemné zvednutí vysokého pásma pro čistotu a detail. Neutrální výchozí bod. |
| **Air** | Otevírá úplný vrchol pro vzdušný, otevřený zvuk. |
| **Bright** | Silné zvednutí pro čistý, jasný, vysunutý tón. |
| **Soften** | Mírné snížení, které ubere hranu drsným výškám. |
| **Tame Highs** | Silné snížení pro ztmavení a vyhlazení přehnaně jasného zvuku. |
| **Sparkle** | Velké zvednutí vrcholu pro maximální třpyt a jiskru. |

### Soft Clip (teplá saturace)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Drive** | Tlačí signál silněji do waveshaperu. Nízké množství přidá jemné teplo; vysoké množství zaoblí špičky do husté saturace a drsnosti. | 0 až 40 dB (0) |

| Preset | Co dělá |
|---|---|
| **Warm** | Špetka drive pro jemné, analogové teplo. |
| **Drive** | Znatelná saturace, která zahušťuje a barví zvuk. |
| **Crunch** | Silný drive se slyšitelnou chrupavou hranou. |
| **Fuzz** | Husté, zkreslené fuzz. Špičky jsou tvrdě zmáčknuty. |
| **Destroy** | Maximální drive. Agresivní, plně nasycená drsnost. |

### Bit Crusher (retro lo-fi)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Bit depth** | Nastavuje, kolik bitů popisuje každý vzorek. Méně bitů znamená hrubší kroky a více kvantizačního šumu, pro chrupavý, drsný digitální zvuk. | 1 až 16 bitů (16) |
| **Sample rate** | Podvzorkuje zvuk. Na sto procentech je frekvence nedotčena; snižte ji, aby se každý vzorek držel déle, čímž otupíte výšky a přidáte drsnou, aliasovanou hranu. | 1% až 100% (100%) |

| Preset | Co dělá |
|---|---|
| **Vintage** | Jemný pokles kvality, jako raný digitální sampler. |
| **LoFi** | Klasické 8bitové lo-fi na poloviční frekvenci. Zrnité a retro. |
| **Crunch** | Silnější drcení se slyšitelnou chrupavou hranou. |
| **Gritty** | Hrubé a drsné. Kroky mezi úrovněmi jsou zjevné. |
| **Destroy** | Extrémní redukce. Drsné, zlomené, sotva rozpoznatelné. |

### Ring Modulator (kovové a robotické tóny)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Carrier** | Nastavuje frekvenci tónu, kterým je signál násoben. Několik hertzů dává tremolo kolísání; vyšší frekvence přidávají kovové, zvonu podobné a robotické alikvóty. | 1 až 4000 Hz (440) |
| **Mix** | Vmíchá modulovaný zvuk do originálu. Na nule procent slyšíte jen dry signál; na sto procentech jen plně modulovaný tón. | 0% až 100% (0%) |

| Preset | Co dělá |
|---|---|
| **Tremolo** | Velmi nízký carrier jej promění v amplitudové tremolo, kolísající hlasitost. |
| **Robot** | Střední carrier přidá řinčivé alikvóty pro klasický efekt robotího hlasu. |
| **Metallic** | Husté, disharmonické alikvóty pro drsný, kovový tón. |
| **Bell** | Vyšší carrier dává jasné, zvonu podobné vyzvánění. |
| **Alien** | Plně wet s vysokým carrierem. Extrémní, mimozemské, sotva rozpoznatelné. |

### Tremolo (kolísání hlasitosti)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Rate** | Nastavuje, jak rychle hlasitost pulzuje. Pomalejší rychlosti dávají hladké kolébání; rychlejší dávají rychlé přerušování. | 0,1 až 20 Hz (5) |
| **Depth** | Nastavuje, jak moc hlasitost klesá při každém pulzu. Na nule procent je úroveň stálá; na sto procentech klesá až do ticha. | 0% až 100% (0%) |

| Preset | Co dělá |
|---|---|
| **Gentle** | Pomalé, mělké kolébání. Nenápadný pohyb bez upoutání pozornosti. |
| **Classic** | Klasické zesilovačové tremolo: střední rychlost a mírná hloubka. |
| **Deep** | Silný, hluboký pulz, který každý cyklus téměř klesá do ticha. |
| **Fast** | Rychlé chvění pro třpytivý, nervózní pocit. |
| **Chop** | Rychlé a plná hloubka. Tvrdé, přerušované sekání. |

### Delay (echo)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Time** | Nastavuje mezeru před každou ozvěnou. Krátké časy dávají těsný slapback; delší časy rozprostírají opakování dál od sebe. | 0,01 až 2 s (0.25) |
| **Feedback** | Nastavuje, kolik z každé ozvěny je přiváděno zpět. Nízké hodnoty dávají jediné opakování; vyšší hodnoty budují dlouhou, táhlou sérii ozvěn. | 0 až 0.95 (0.4) |
| **Mix** | Vmíchá ozvěny do originálu. Na nule procent slyšíte jen dry signál; na sto procentech jen ozvěny. | 0% až 100% (0%) |

| Preset | Co dělá |
|---|---|
| **Slapback** | Jediné krátké echo, těsně u originálu. Rockabilly a zdvojení vokálů. |
| **Echo** | Klasické echo: čisté opakování s několika táhlými ocasy. |
| **Ping** | Rychlé, odrážející se opakování, které přidá rytmický pohyb. |
| **Ambient** | Delší, jemnější opakování, která se rozplynou do prostorného ocasu. |
| **Dub** | Vysoký feedback pro dlouhé, dubové kaskády ozvěn. |
| **Cavern** | Dlouhá, hluboká opakování, jako zvuk odrážející se obrovským prostorem. |

### Stereo Width (zúžení nebo rozšíření)

| Ovládání | Co dělá | Rozsah (výchozí) |
|---|---|---|
| **Width** | Zužuje nebo rozšiřuje stereo obraz. Nula procent zhroutí do mono, sto procent jej ponechá nedotčený a vyšší hodnoty tlačí strany šíře. Ovlivňuje pouze stereo skladby na cíli Všechny kanály. | 0% až 200% (100%) |

| Preset | Co dělá |
|---|---|
| **Wide** | Jemné rozšíření, které otevírá stereo obraz. Neutrální výchozí bod. |
| **Wider** | Silnější rozprostření pro velké, pohlcující stereo pole. |
| **Max** | Maximální šířka. Velmi široké, ale pozor na problémy s mono kompatibilitou. |
| **Narrow** | Stáhne strany dovnitř pro těsnější, více vycentrovaný obraz. |
| **Focused** | Téměř vycentrováno, jen s náznakem sterea. |
| **Mono** | Plně zhrouceno do mono. Oba reproduktory hrají stejný signál. |

## Jak to celé funguje pod kapotou (jednoduchá verze)

- **Enginy:** vyberete si jeden v Nastavení > Audio přehrávač > Přehrávací engine: **Standard** (systémový), **Universal** (FFmpeg) nebo **Sound FX** (**engine BASS™** od [Un4seen Developments](https://www.un4seen.com/)). Engine, který zvolíte, rozhoduje o tom, které formáty se přehrají, a efekty, ekvalizér a DSP řetězec běží pouze v enginu Sound FX.
- **Formáty:** engine BASS™ přidává FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus a modulovou (tracker) hudbu navíc k systémovým a FFmpeg formátům.
- **Efekty:** ekvalizér, kompresor a většina efektů používají doplňky efektů BASS™. Freeverb je reverb Freeverb. Chorus, Flanger a Distortion používají klasické efekty ve stylu DirectX s vlastními ovládacími prvky.
- **Normalizace hlasitosti:** živý vyrovnávač hlasitosti **EBU R128** (standard hlasitosti používaný ve vysílání a streamování).
- **Crossfeed:** crossfeed **bs2b (Bauer)**, běžící uvnitř enginu BASS™.
- **DSP řetězec:** vaše vlastní bloky, aplikované v přesném pořadí, které nastavíte, na všech kanálech nebo jen jedné straně.
- **Výstup:** můžete nastavit vzorkovací frekvenci, počet kanálů a velikost bufferu, aby odpovídaly vašemu vybavení.

Protože to celé běží živě, zatímco hudba hraje, efekty:

- Pracují v **reálném čase** na všem, včetně cloudových souborů, streamů a modulové hudby.
- **Nikdy nezmění ani znovu neuloží** vaše soubory. Vypněte efekt a originál se vrátí.
- **Zapamatují si vaše nastavení** pro každý efekt.
- Lze je **volně kombinovat a mísit**, protože každý je samostatný.

## Jednoduché recepty k vyzkoušení

**Každodenní poslech**

- **Více basů, čistě:** Ekvalizér > Bass Booster, poté snižte Preamplifier o 1 až 2 dB. Nebo přidejte DSP Low Shelf na Bass Boost.
- **Vyrovnaná hlasitost napříč smíšeným playlistem:** Normalizace hlasitosti > Standard, plus Compressor > Soft.
- **Jemné celkové vyleštění:** Compressor > Transparent, plus Normalizace hlasitosti > Light.
- **Čistší vokály:** Ekvalizér > Vocal Booster, nebo blok DSP Peaking na Vocal Boost.
- **Plnější zvuk na malých reproduktorech telefonu:** Ekvalizér > Small Speakers.

**Sluchátka**

- **Příjemnější, méně únavné na sluchátkách:** Crossfeed > Chu Moy nebo Jan Meier.
- **Širší zvuk na sluchátkách:** DSP Stereo Width > Wide, plus Crossfeed > Chu Moy.
- **Oprava tvrdě panorámovaných desek z 60. a 70. let:** Crossfeed > Vintage Stereo.
- **Trochu vzdušnosti a prostoru:** Freeverb > Ambience, udrženo nízko, plus Crossfeed > Subtle.

**Klidné časy a mluvené slovo**

- **Noční tichý poslech:** Normalizace hlasitosti > Night, plus Compressor > Late Night.
- **Podcasty a audioknihy:** Compressor > Voice / Podcast, plus Ekvalizér > Spoken Word.
- **Nejhlasitější, nejvyrovnanější zvuk v hlučném autě:** Normalizace hlasitosti > Strong, plus Compressor > Heavy.

**Řešení problémů**

- **Zkrocení drsné, jasné nahrávky:** Ekvalizér > Treble Reducer, nebo blok DSP Peaking na Tame Harsh.
- **Odstranění elektrického humu:** DSP řetězec > Notch > Mains Hum 60 (nebo Mains Hum 50 v Evropě).
- **Těsnější, čistší basy:** DSP High Pass > Tighten, k odřezání dunivého nízkého pásma.
- **Méně dunění v mixu s těžkými basy:** DSP Low Shelf > Trim Bass, nebo Peaking > De-Boom.

**Kreativní a zábavné**

- **Teplý, prostorný pocit:** Freeverb > Hall, udrženo nízko.
- **Snové, prostorné kytary:** Chorus > Wide, plus Echo > Long.
- **Retro lo-fi:** DSP řetězec > Bit Crusher (LoFi) do Soft Clip (Warm).
- **Funkový pohyb na elektronických skladbách:** Auto Wah > Funky, nebo Phaser > Fast.
- **Klasický sweep tryskového letadla:** Flanger > Jet.

## Časté dotazy

{{% details title="Jaký zvukový engine Flacbox používá?" closed="true" %}}
Zvolíte si jeden přehrávací engine v Nastavení > Audio přehrávač: Standard (systémový engine Apple), Universal (engine FFmpeg) nebo Sound FX (engine BASS™ od Un4seen Developments, un4seen.com). Engine, který zvolíte, rozhoduje o tom, které formáty souborů se přehrají. Sound FX je ten, který přehrává další formáty jako FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus a hudbu MOD nebo tracker music, a je jediným enginem, který poskytuje živé efekty, 10pásmový ekvalizér a DSP řetězec. Chcete-li používat efekty, nastavte přehrávací engine na Sound FX.
{{% /details %}}

{{% details title="Umí Flacbox přehrávat MOD, XM, IT a další tracker nebo modulovou hudbu?" closed="true" %}}
Ano. Engine BASS™ má vestavěný modulový přehrávač, který načítá soubory MOD, XM, IT, S3M, MTM, UMX a MO3 a znovu sestavuje skladbu živě z jejích patternů a zvuků nástrojů, tak jak má být tracker music přehrávána. Běžné přehrávače pro iPhone to nedokáží. Efekty a ekvalizér fungují i na modulové hudbě.
{{% /details %}}

{{% details title="Podporuje Flacbox DSD a vysokorozlišené soubory?" closed="true" %}}
Ano. Flacbox přehrává soubory DSD (DSF a DFF) přes engine BASS™ pomocí DSD over PCM, takže fungují na běžném výstupním hardwaru, plus FLAC, WavPack, Monkey's Audio (APE), Musepack a TrueAudio pro bezztrátové přehrávání.
{{% /details %}}

{{% details title="Jaké zvukové efekty Flacbox má?" closed="true" %}}
10pásmový ekvalizér, normalizaci hlasitosti, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate a Crossfeed, plus vlastní DSP řetězec s filtry, shelfy, gainem, soft clipem, bit crusherem, ring modulátorem, tremolem, delayem a stereo šířkou. Každý je samostatný a lze jej kombinovat s ostatními.
{{% /details %}}

{{% details title="Co je preset?" closed="true" %}}
Preset je připravené nastavení efektu. Místo abyste sami pohybovali posuvníky, klepnete na preset a zvuk se změní podle něj. Každý efekt ve Flacboxu má několik presetů a tento průvodce uvádí, co každý dělá. Pokud po výběru presetu pohnete posuvníkem, efekt zobrazí „Manual“, aby vám řekl, že nyní používá vaše vlastní hodnoty.
{{% /details %}}

{{% details title="Jak otevřu audio efekty ve Flacboxu?" closed="true" %}}
Otevřete přehrávač Now Playing, klepněte na tlačítko ⋯ (Další akce) a zvolte Audio efekty. Nebo přejděte na Nastavení > Audio přehrávač > Audio efekty. Klepněte na efekt, zapněte jeho vypínač a vyberte preset, nebo otevřete posuvníky k doladění.
{{% /details %}}

{{% details title="Kde je ekvalizér a jaká jsou nejlepší nastavení?" closed="true" %}}
Přejděte na Nastavení > Audio přehrávač > Audio ekvalizér. Má 10 pásem od 32 Hz do 16 kHz, každé od -12 do +12 dB, plus Preamplifier od -24 do +24 dB a 22 presetů. Pro více basů použijte Bass Booster. Pro čistší hlasy použijte Vocal Booster nebo Pop. Pro jasnější zvuk použijte Treble Booster. Poté upravte jednotlivá pásma podle chuti.
{{% /details %}}

{{% details title="Jak zesílím basy ve Flacboxu?" closed="true" %}}
Dva snadné způsoby. V Audio ekvalizéru vyberte Bass Booster (nebo zvedněte pásma 32 Hz a 64 Hz o pár dB). Nebo v Zpracování signálu přidejte blok Low Shelf nastavený na Bass Boost. V obou případech snižte Preamplifier nebo přidejte blok Gain o 1 až 2 dB, aby basy zůstaly čisté a nezkreslovaly.
{{% /details %}}

{{% details title="Který preset ekvalizéru je nejlepší pro mou hudbu?" closed="true" %}}
Rock a Electronic přidávají energii se silnými basy a výškami. Acoustic, Jazz a Classical zůstávají teplé a přirozené. Pop a Vocal Booster tlačí hlasy dopředu. Bass Booster a Hip-Hop přidávají váhu. Deep a Loudness znějí plněji při nízké hlasitosti. Začněte s tím, který odpovídá vašemu žánru, a poté dolaďte.
{{% /details %}}

{{% details title="Co je normalizace hlasitosti a čím se liší od ReplayGain?" closed="true" %}}
Způsobí, že každá skladba hraje zhruba stejně hlasitě. Měří skutečnou hlasitost pomocí standardu EBU R128 (v LUFS, jako streamovací služby) a přizpůsobuje každou skladbu k vašemu cíli, s limitem max-boost. Na rozdíl od ReplayGain nepotřebuje žádné tagy ve vašich souborech a funguje na jakémkoli zdroji, živě, bez změny zvuku. Presety: Light, Standard, Strong a Night.
{{% /details %}}

{{% details title="Co je Crossfeed a měl bych ho používat?" closed="true" %}}
Crossfeed vmíchá trochu levého a pravého kanálu dohromady, takže sluchátka působí spíše jako reálné reproduktory a méně jako by zvuk uvízl ve vaší hlavě. Je pouze pro sluchátka, takže jej pro reproduktory vypněte. Flacbox používá metodu bs2b (Bauer), s presety jako Chu Moy a Jan Meier.
{{% /details %}}

{{% details title="Jaký je rozdíl mezi Compressorem a normalizací hlasitosti?" closed="true" %}}
Normalizace hlasitosti sjednocuje hlasitost mezi různými skladbami. Compressor vyrovnává hlasité a tiché části uvnitř jedné skladby. Řeší různé problémy a dobře spolu fungují, zejména v autě nebo na hlučném místě.
{{% /details %}}

{{% details title="Co je řetězec Zpracování signálu (DSP)?" closed="true" %}}
Je to vlastní rack v Nastavení > Audio přehrávač > Zpracování signálu. Přidejte bloky jako filtry, shelfy, gain, soft clip, bit crusher, ring modulátor, tremolo, delay a stereo šířku, dejte je do libovolného pořadí, každý zapněte nebo vypněte a zaměřte řetězec na všechny kanály, levý nebo pravý. Protože na pořadí záleží, můžete navrhnout přesně ten zvuk, který chcete.
{{% /details %}}

{{% details title="Jaký je rozdíl mezi ekvalizérem, efekty a DSP řetězcem?" closed="true" %}}
Ekvalizér je jednoduché 10pásmové řízení tónu. Audio efekty jsou připravené nástroje (kompresor, reverb, echo atd.) s presety. DSP řetězec je místo, kde si stavíte vlastní pořadí efektů z jednotlivých bloků. Všechny tři můžete spustit současně.
{{% /details %}}

{{% details title="Mění nebo poškozují efekty mé hudební soubory?" closed="true" %}}
Ne. Vše se aplikuje živě, zatímco hudba hraje. Vaše soubory se nikdy nezmění ani znovu neuloží. Vypněte efekt a původní zvuk se ihned vrátí.
{{% /details %}}

{{% details title="Mohu použít více než jeden efekt současně?" closed="true" %}}
Ano. Každý efekt má vlastní vypínač a neexistuje žádný hlavní vypínač, takže funguje jakákoli kombinace. Například normalizace hlasitosti plus Compressor pro vyrovnaný poslech, nebo Freeverb plus Crossfeed na sluchátkách, s ekvalizérem navrch.
{{% /details %}}

{{% details title="Proč jsou ovládací prvky efektu zašedlé?" closed="true" %}}
Efekt je vypnutý. Zapněte jeho vypínač v horní části editoru, abyste ovládací prvky mohli používat. Každý efekt je ve výchozím stavu vypnutý.
{{% /details %}}

{{% details title="Co znamená označení Manual?" closed="true" %}}
Znamená to, že jste pohnuli posuvníkem pryč od presetu, takže efekt nyní používá vaše vlastní vlastní hodnoty místo pojmenovaného presetu. Každý posuvník má tlačítko reset a opětovný výběr presetu nahradí vaše ruční hodnoty.
{{% /details %}}

{{% details title="Mohu uložit a sdílet své presety ekvalizéru?" closed="true" %}}
Ano. Kromě 22 vestavěných presetů si můžete vytvořit vlastní, změnit jejich pořadí a exportovat nebo importovat je, abyste přesunuli svá nastavení do jiného zařízení.
{{% /details %}}

{{% details title="Fungují efekty s CarPlay, streamováním a přehráváním na pozadí?" closed="true" %}}
Ano. Efekty běží uvnitř enginu BASS™, takže se uplatní na lokální soubory, cloudová úložiště, mediální servery, streamy a modulovou hudbu a fungují i během CarPlay a přehrávání na pozadí.
{{% /details %}}

{{% details title="Mohu změnit kvalitu zvukového výstupu?" closed="true" %}}
Ano. V Nastavení > Audio přehrávač můžete nastavit výstupní vzorkovací frekvenci, počet kanálů a velikost bufferu, aby odpovídaly vašim sluchátkům, reproduktorům nebo DAC.
{{% /details %}}

{{% details title="Jaké je dobré výchozí nastavení pro sluchátka?" closed="true" %}}
Zapněte normalizaci hlasitosti (Standard), přidejte lehký Compressor (Soft), vyberte preset ekvalizéru, který se vám líbí, a zapněte Crossfeed (Chu Moy nebo Jan Meier). Reverb, echo a distortion nechte vypnuté, pokud nechcete kreativní zvuk.
{{% /details %}}

---

*BASS is a trademark of Un4seen Developments Ltd. See [un4seen.com](https://www.un4seen.com/). Crossfeed uses the bs2b (Bauer stereophonic-to-binaural) algorithm; see the [bs2b project page](https://bs2b.sourceforge.net/).*
