---
title: "Sådan bruger du lydeffekter og DSP i Flacbox: Compressor, Freeverb, Crossfeed, Echo, Volume Normalization og mere"
date: 2026-07-24
description: "Den komplette guide til Flacbox-lyd på iPhone, iPad og Mac. Lær, hvordan BASS-motoren fungerer, hvilke ekstra formater den afspiller (herunder MOD- og tracker-musik og DSD), og præcis hvad hver effekt, hver skyder og hvert preset gør ved din lyd, plus den 10-bånds equalizer og den brugerdefinerede DSP-kæde."
keywords: ["Flacbox lydeffekter", "Flacbox presets forklaret", "Flacbox BASS-motor", "BASS lydbibliotek iOS", "MOD-musikafspiller iPhone", "tracker-musikafspiller iOS", "afspil MOD XM IT S3M iPhone", "DSD-afspiller iOS", "FLAC-afspiller iPhone", "lossless musikafspiller iOS", "Flacbox equalizer-presets", "10-bånds equalizer iPhone", "lydstyrkenormalisering iPhone", "EBU R128 iOS", "loudness-normalisering musikafspiller", "crossfeed hovedtelefoner iOS", "bs2b crossfeed", "compressor-presets musikafspiller", "freeverb rumklang iOS", "echo delay musikafspiller", "DSP-kæde musikafspiller", "bass boost iPhone", "sådan tilføjer du effekter til musik Flacbox", "bedste equalizer-indstillinger iPhone"]
tags: ["Flacbox", "Lydeffekter", "Sådan gør du", "BASS", "Equalizer", "Bass Boost", "Compressor", "Freeverb", "Crossfeed", "Echo", "Volume Normalization", "EBU R128", "MOD-musik", "Tracker-musik", "DSD", "FLAC", "DSP", "Hovedtelefoner", "Presets"]
readingTime: 30
---

{{< author-byline >}}

**Kort svar:** I Flacbox vælger du én **Afspilningsmotor** i **Indstillinger > Lydafspiller**: **Standard** (Apples systemmotor), **Universal** (FFmpeg-motoren) eller **Sound FX** (**BASS™-motoren**). Den motor, du vælger, bestemmer, hvilke filformater der afspilles, så valget betyder noget. **Sound FX**-motoren afspiller ekstra formater, som de fleste iPhone-apps springer over (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus og gammel **MOD- og tracker-musik** som MOD, XM, IT og S3M), og den er den eneste motor, der driver lydværktøjerne: en **10-bånds equalizer**, **Volume Normalization**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** og en byg-selv **DSP-kæde**. Så for at bruge effekterne i denne guide skal du først sætte din Afspilningsmotor til **Sound FX**. Hvert værktøj har færdiglavede **presets**. Åbn dem i **Indstillinger > Lydafspiller** (Lydeffekter, Lydequalizer, Signalbehandling), eller tryk på **⋯ (Mere)**-knappen på afspilleren og vælg **Lydeffekter**. Intet, du gør her, ændrer nogensinde dine filer.

> Forklaringerne på skydere og presets nedenfor er de samme korte beskrivelser, som Flacbox viser dig inde i appen, blandet med lidt ekstra baggrund, så du får det fulde billede, før du trykker.

## Sådan læser du denne guide

Hvert værktøj fungerer på samme måde:

1. **Tænd for det.** Hver effekt har sin egen tænd/sluk-kontakt. De er alle slukket i starten. Du kan tænde for så mange, du vil, på samme tid.
2. **Vælg et preset.** Et preset er en færdiglavet indstilling. Tryk på ét, og lyden ændrer sig med det samme. Denne guide angiver, hvad **hvert** preset gør.
3. **Finjuster (valgfrit).** Åbn skyderne for at justere manuelt. I det øjeblik du flytter en skyder, viser effekten **Manual**, så du ved, at du har forladt preset'et. Hver skyder har en nulstillingsknap.

Intet gemmes ind i dine filer. Dette er live-effekter. Sluk for en effekt, og din originale lyd kommer tilbage med det samme.

## Vælg din afspilningsmotor (Sound FX har effekterne)

Flacbox blander ikke motorer sammen. Du vælger **én** i **Indstillinger > Lydafspiller > Afspilningsmotor**, og den motor, du vælger, bestemmer, hvilke filformater du kan afspille, og om effekterne er tilgængelige. Der er tre valg, vist i appen under disse præcise navne:

1. **Standard.** Apples indbyggede systemmotor. Bruger hardware-afkodning for lavere batteriforbrug.
2. **Universal.** FFmpeg-motoren, som åbner en meget bred vifte af formater.
3. **Sound FX.** **BASS™-motoren**. Den afspiller lossless- og high-resolution-filer med fuld nøjagtighed, tilføjer modul-musik (tracker) og driver hver effekt, den 10-bånds equalizer og DSP-kæden i denne guide.

Fordi hver motor understøtter sit eget sæt af formater, ændrer de filer, du kan afspille, sig med den motor, du vælger. Endnu vigtigere fungerer effekterne, equalizeren og DSP-kæden **kun** med **Sound FX**-motoren, så vælg den først, hvis du vil bruge dem.

Sound FX er bygget på **BASS™**, et professionelt lydbibliotek fra Un4seen Developments. Du kan læse mere om det på dets hjemmeside på [un4seen.com](https://www.un4seen.com/).

## Musikformater: Hvad Sound FX (BASS™)-motoren tilføjer (herunder MOD- og tracker-musik)

Med **Sound FX (BASS™)**-motoren valgt afspiller Flacbox specialistformaterne nedenfor oven i de dagligdags. Det mest specielle er **modul-musik**, også kaldet **tracker-musik**. En modulfil er ikke en normal optagelse. Den indeholder små instrumentlyde plus et «partitur», der siger, hvordan de skal spilles, og Flacbox genopbygger sangen live ud fra det partitur, sådan som disse filer var tænkt at skulle afspilles. Normale afspillere kan ikke dette.

| Type musik | Formater | Godt at vide |
|---|---|---|
| **Modul- / tracker-musik** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Genopbygges live af BASS™-modulafspilleren. Fantastisk til chiptunes og gamle demoscene- eller Amiga-sange. |
| **Moderne lossless** | FLAC | Fuld kvalitet, mindre end WAV. |
| **Andre lossless** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Mindre almindelige lossless-typer, alle understøttet. |
| **High-resolution DSD** | DSF, DFF | Afspilles på normal hardware ved hjælp af DSD over PCM. |
| **Moderne lossy** | Opus, Ogg Vorbis, MP3 | De sædvanlige streaming- og downloadtyper. |

Sound FX-motoren afspiller også de almindelige Apple-formater (AAC, ALAC, M4A, WAV, AIFF) og live-streams, så effekterne og equalizeren fungerer også på dem.

**Hvorfor dette hjælper dig:** hvis du har en blanding af FLAC-albummer, DSD high-resolution-filer og en mappe med gamle MOD- eller XM-tracker-sange, afspiller Flacbox dem alle, og equalizeren og effekterne fungerer på hver enkelt af dem.

## De tre menuer, du vil bruge

Flacbox holder sine lydværktøjer på tre steder, alle inde i lydafspillerens indstillinger. Sørg først for, at din **Afspilningsmotor** er sat til **Sound FX** (Indstillinger > Lydafspiller > Afspilningsmotor), fordi effekterne, equalizeren og DSP-kæden kun er tilgængelige med den motor.

- **Lydeffekter** (effektracket): åbn afspilleren, tryk på **⋯ (Mere)**, tryk på **Lydeffekter**. Eller gå til **Indstillinger > Lydafspiller > Lydeffekter**.
- **Lydequalizer** (10 bånd og presets): **Indstillinger > Lydafspiller > Lydequalizer**.
- **Signalbehandling** (din egen DSP-kæde): **Indstillinger > Lydafspiller > Signalbehandling**.

Du kan også indstille **output-samplingsraten**, **kanalerne** og **bufferstørrelsen** under **Indstillinger > Lydafspiller**.

## Den 10-bånds equalizer

**Hvad den gør:** Ændrer musikkens tone, fra dyb bas til lys diskant. Dette er det bedste værktøj til en ren **bass boost** eller en lysere, klarere top. Tænk på den som ti lydstyrkeknapper, hver til en anden del af lyden. Hæv et bånd for at bringe den del frem, sænk det for at trække det tilbage. Små ændringer på et par dB lyder normalt bedst, og det fungerer på alt, du afspiller.

**Hvordan den fungerer:** Ti skydere ved **32, 64, 125, 250, 500 Hz og 1, 2, 4, 8, 16 kHz**. Hver går fra **-12 dB (cut)** til **+12 dB (boost)**. Der er også en **Preamplifier** fra **-24 til +24 dB** til det samlede niveau. Du kan gemme dine egne presets og **eksportere eller importere** dem mellem enheder.

**Hvad hvert indbygget preset gør (22 presets):**

| Preset | Hvad det gør ved din lyd |
|---|---|
| **Flat** | Ingen ændring. Alle bånd på nul. Et rent udgangspunkt. |
| **Acoustic** | Varm bas og skarp, tilstedeværende diskant. Får akustiske guitarer og stemmer til at føles naturlige og livlige. |
| **Bass Booster** | Kraftigt løft i bunden, mellemtoner og diskant urørte. Mere punch og vægt. |
| **Bass Reducer** | Skærer bunden ned. Praktisk til rungende rum, billige øretelefoner eller tunge numre. |
| **Treble Booster** | Løfter kun diskanten. Tilføjer glans og luft, mere detalje. |
| **Treble Reducer** | Blødgør diskanten. Tæmmer skarpe eller hårde optagelser. |
| **Classical** | Fuld bund og blid diskant med et lille mellemtonedyk. Glat og rummelig til orkestermusik. |
| **Dance** | Stor bund og lys diskant med udskårne mellemtoner. Punchy og energisk til klubnumre. |
| **Deep** | Varm, tyk bund med blødere diskant. En hyggelig, afslappet lyd. |
| **Electronic** | Kraftig bas og lys diskant til synths og beats. Bred og moderne. |
| **Hip-Hop** | Tung bas og klar diskant med kontrollerede mellemtoner. Vægtig og punchy. |
| **Jazz** | Varm og glat, med et lille mellemtonedyk. Let og naturlig til akustisk jazz. |
| **Latin** | Løftet bund og diskant med rene mellemtoner. Lys og livlig. |
| **Loudness** | Løfter bas og diskant kraftigt (en «smile»-kurve). Lyder fyldigere ved lav lydstyrke. |
| **Lounge** | Fremtrukne mellemtoner med bløde kanter. Afslappet og vokalvenlig. |
| **Piano** | Klare mellemtoner og diskant, så klavertoner klinger rent ud. |
| **Pop** | Løftede mellemtoner til vokal, med bund og diskant trukket tilbage. Stemmer sidder forrest. |
| **R&B** | Meget kraftig lav-mellemtonevarme og klar diskant. Glat og rig. |
| **Rock** | Løftet bund og diskant til guitarer og trommer. Energisk og fuld. |
| **Small Speakers** | Løfter bunden og skærer diskanten for at hjælpe små højttalere med at lyde fyldigere. |
| **Spoken Word** | Løfter stemmeområdet og skærer den dybe bas. Gør tale klar. |
| **Vocal Booster** | Skubber midten, hvor stemmer bor, skærer omkring dem. Vokal skiller sig ud. |

**Tip til bas:** Start med **Bass Booster**, og hvis det lyder mudret, så træk Preamplifier ned 1 til 2 dB, så intet forvrænges.

## Volume Normalization (jævn lydstyrke)

**Hvad den gør:** Nogle sange spiller højere end andre, så du bliver ved med at ændre lydstyrken. Dette får hver sang til at spille ved omtrent den samme lydstyrke af sig selv, så du ikke behøver. Den er perfekt til blandede afspilningslister, der mikser gamle og nye optagelser, forskellige albummer eller forskellige kilder, hvor et nummer kan være meget højere end det næste.

**Hvordan den fungerer:** Den lytter til den reelle loudness af hvert nummer ved hjælp af **EBU R128**-standarden (målt i **LUFS**, den samme idé, som streamingtjenester bruger), og justerer derefter hvert nummer mod dit mål. Den behøver ingen tags i dine filer og ændrer aldrig lyden. EBU R128 måler den loudness, dine ører faktisk mærker på tværs af hele sangen, ikke bare den højeste peak, hvilket er grunden til, at den matcher, hvor høje numre virkelig virker for dig. Flacbox regner dette ud live, mens musikken spiller (og tjekker loudness på forhånd, når den kan), og anvender derefter en enkelt, stabil lydstyrkeændring på nummeret. **Max boost**-grænsen forhindrer meget stille optagelser i at blive skubbet så hårdt op, at de forvrænges. Fordi den læser selve lyden, fungerer den på enhver kilde, herunder cloud-filer, live-streams og modul-musik, selv når filerne slet ingen loudness-tags har.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Target loudness** | Indstiller den loudness, hvert nummer nivelleres mod. Højere værdier får alt til at spille højere samlet set. | -30 til -6 LUFS (-16) |
| **Max boost** | Begrænser, hvor meget stille numre kan forstærkes. Højere værdier bringer bløde optagelser tættere på målet. | 0 til 24 dB (12) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Light** | Blid nivellering til afslappet lytning. Udjævner tydelige lydstyrkespring uden at skubbe stille numre hårdt. |
| **Standard** | Alsidig standard. Et streaming-lignende loudness-mål, der passer til det meste musik. Start her. |
| **Strong** | Aggressiv matchning, der skubber stille numre fast op. Bedst til blandede biblioteker med store niveauforskelle. |
| **Night** | Et generelt roligere mål, der stadig løfter bløde passager, så natlytning forbliver konsistent og lav. |

## Compressor (udjævn høje og stille dele)

**Hvad den gør:** I én sang kan de stille dele være for bløde og de høje dele for høje. Dette bringer dem tættere sammen, så hele sangen er let at høre, selv i bilen eller på et støjende sted. Den skruer forsigtigt ned for de højeste øjeblikke og løfter de blødere, så du holder op med at strække dig efter lydstyrken under et enkelt nummer. Dette er forskelligt fra Volume Normalization: Compressor udjævner tingene **inde i** én sang, mens Volume Normalization matcher loudness **mellem** sange. De to fungerer godt sammen. Start med et preset, og åbn kun skyderne, hvis du vil have mere kontrol.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Threshold** | Niveauet, hvor kompressionen starter. Lavere værdier klemmer mere af lyden, hvilket holder stille og høje dele tættere sammen. | -60 til 0 dB (-20) |
| **Ratio** | Hvor kraftigt de høje dele holdes tilbage, når de passerer tærsklen. Højere værdier komprimerer hårdere og holder lyden mere jævn. | 1:1 til 30:1 (4:1) |
| **Attack** | Hvor hurtigt effekten reagerer på en pludselig høj peak. Korte værdier fanger transienter; længere lader dem passere. | 0,1 til 1000 ms (10 ms) |
| **Release** | Hvor hurtigt effekten slipper, efter den høje del passerer. Korte værdier kan pumpe; længere lyder glattere. | 10 ms til 5 s (100 ms) |
| **Master gain** | Endelig output-boost anvendt efter behandling. Hæv denne for at løfte den samlede loudness, når dynamikken er udjævnet. | -30 til +30 dB (0) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Transparent** | Knap mærkbart sikkerhedsnet. Bevarer dynamikken næsten fuldstændigt og fanger kun de højeste peaks. |
| **Soft** | Let nivellering til hi-fi-lytning hjemme. Subtil udglatning uden at klemme musikken. |
| **Standard** | Fornuftig standard til daglig musikafspilning. Det første preset at prøve. |
| **Heavy** | Aggressiv udjævning til støjende miljøer. Bil, fyldt lokale, lytning ved lav lydstyrke. |
| **Voice / Podcast** | Tale-tunet. Langsommere attack lader sibilanter passere, generøs makeup gain trækker vokal op. |
| **Old Recordings** | Gamle albummer og restaureret vinyl, hvor gennemsnitsniveauet er under moderne udgivelser. |
| **Late Night** | Kraftig kompression plus stort boost til stille lytning, når naboer eller sovende familie betyder noget. |
| **Movie Dialog** | Bringer tale op mod musik og lydeffekter i et varieret lydspor. |
| **Streaming Match** | Sigter mod cirka loudness-normaliseringen fra moderne streamingtjenester omkring -14 LUFS. |
| **Maximum Loudness** | Alt-ind. Rammer limiteren; forvent et klemt, meget jævnt signal. Det bogstavelige max-volumen-preset. |

## Freeverb (rumklang, en fornemmelse af rum)

**Hvad den gør:** Tilføjer en fornemmelse af rum til musikken, fra et lille rum op til en stor sal. Vælg et preset, eller finjuster selv tør- og våd-mikset, rumstørrelse, dæmpning og bredde. Rumklang er det naturlige ekko, du hører i ethvert rigtigt rum, og Freeverb genskaber det i software. Lidt får flade eller tætmikrofonerede optagelser til at føles mere åbne og levende. Meget placerer musikken i et stort, fjernt rum. Det er en kreativ effekt, så hold våd-mikset moderat for naturlige resultater.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Dry mix** | Hvor meget af den originale, urørte lyd der bevares. Højere værdier efterlader mere af det tørre signal i mikset. | 0 til 1 (0,0) |
| **Wet mix** | Hvor meget af den rumklangede lyd der tilføjes. Højere værdier gør rumklangen højere og mere tydelig. | 0 til 3 (1,0) |
| **Room size** | Størrelsen på det forestillede rum. Højere værdier giver en længere, større rumklangshale, fra et lille rum op til en katedral. | 0 til 1 (0,5) |
| **Damp** | Hvor hurtigt de høje frekvenser falmer i halen. Højere værdier gør rumklangen mørkere og varmere. | 0 til 1 (0,5) |
| **Width** | Stereospredningen af rumklangen. Højere værdier får rummet til at føles bredere mellem venstre og højre kanal. | 0 til 1 (1,0) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Room** | Et lille, tæt rum. Subtil ambience, der tilføjer en fornemmelse af sted uden at udvaske lyden. |
| **Studio** | Et tørt, kontrolleret optagerum. Lige nok refleksion til at lyde naturlig. |
| **Hall** | En stor koncertsal. En lang, frodig hale, der passer til orkester- og akustisk musik. |
| **Cathedral** | Et enormt, ekkoende stenrum. Den længste, mest dramatiske rumklangshale. |
| **Plate** | En lys, tæt studieplade-rumklang. Klassisk til vokal og trommer. |
| **Ambience** | En kort, luftig ambience. Tilføjer en let fornemmelse af rum, mens den forbliver mest tør. |

## Auto Wah (funky filtersweep)

**Hvad den gør:** Et filter, der sweeper op og ned af sig selv for en funky, stemmelignende wah-lyd. Vælg et preset, eller indstil selv våd-mikset, feedback, rate, range og frekvens. Det er den samme «wah»-sweep, som en guitar-wah-pedal laver, men her bevæger den sig af sig selv i takt med musikken. Den lyder fantastisk på funk-, disco- og elektroniske numre. Det er en fed, tydelig effekt, så lidt rækker langt til daglig lytning.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Wet mix** | Hvor stærk wah-effekten er i mikset. Højere værdier gør det sweepende filter mere tydeligt. | -2 til +2 (1,5) |
| **Feedback** | Hvor meget af outputtet der føres tilbage i effekten. Højere værdier gør wah'en mere resonant og udtalt. | -1 til +1 (0,5) |
| **Rate** | Hvor hurtigt filteret sweeper op og ned. Højere værdier giver en hurtigere, mere rytmisk wah. | 0,1 til 9 Hz (2,0) |
| **Range** | Hvor langt filteret sweeper, i oktaver. Højere værdier giver en bredere, mere dramatisk sweep. | 0,1 til 9 oktaver (4,3) |
| **Frequency** | Basisfrekvensen, filteret sweeper omkring. Lavere værdier lyder dybere; højere værdier lyder lysere. | 1 til 1000 Hz (50) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Classic** | En balanceret, klassisk wah-sweep. Et godt udgangspunkt for funk og rock. |
| **Slow** | En langsom, bred sweep, der driver blidt op og ned. Fantastisk til pads og lange toner. |
| **Funky** | En hurtig, punchy sweep med masser af bevægelse. Tilføjer rytmisk bid til guitarer og synths. |
| **Deep** | En dyb, bred sweep, der starter fra en lav frekvens. Stor og dramatisk. |
| **Subtle** | En blid, underspillet bevægelse. Tilføjer karakter uden at dominere lyden. |
| **Resonant** | En skarp, resonant wah med høj feedback. Stemmelignende og udtryksfuld. |

## Phaser (hvirvlende whoosh)

**Hvad den gør:** Et sweepende filter, der tilføjer en hvirvlende, whooshende bevægelse til lyden. Vælg et preset, eller indstil selv feedback, rate, range og frekvens. Den tilføjer blid bevægelse og glimt uden at ændre tonerne. Den er subtil på vokal og pads, og dramatisk på synths og guitarer. Prøv Slow for en drømmende fornemmelse eller Jet for en stærk hvirvel.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Feedback** | Hvor meget af outputtet der føres tilbage i effekten. Højere værdier gør phaseren mere resonant og udtalt. | -1 til +1 (0,0) |
| **Rate** | Hvor hurtigt filteret sweeper op og ned. Højere værdier giver en hurtigere, mere rytmisk phasing. | 0,1 til 9 Hz (1,0) |
| **Range** | Hvor langt filteret sweeper, i oktaver. Højere værdier giver en bredere, mere dramatisk sweep. | 0,1 til 9 oktaver (4,0) |
| **Frequency** | Basisfrekvensen, filteret sweeper omkring. Lavere værdier lyder dybere; højere værdier lyder lysere. | 1 til 1000 Hz (100) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Classic** | En balanceret, klassisk phaser-sweep. Et godt udgangspunkt for guitarer og keys. |
| **Slow** | En langsom, bred sweep, der driver blidt op og ned. Fantastisk til pads og lange toner. |
| **Fast** | En hurtig, glimtende sweep med masser af bevægelse. Tilføjer bevægelse og energi. |
| **Deep** | En dyb, bred sweep, der starter fra en lav frekvens. Stor og dramatisk. |
| **Subtle** | En blid, underspillet bevægelse. Tilføjer karakter uden at dominere lyden. |
| **Jet** | En intens, resonant sweep med høj feedback, den klassiske jetfly-whoosh. |

## Flanger (jetfly-sweep)

**Hvad den gør:** En kort, bevægelig delay, der giver lyden en jet-lignende, sweepende whoosh. Vælg et preset, eller indstil selv depth, feedback, rate og delay. Den er en stærkere, mere metallisk fætter til phaseren, berømt for den whooshende sweep i klassisk rock og elektronisk musik. Subtile indstillinger tilføjer blid bevægelse, mens dybe indstillinger er dramatiske og tydelige. Bruges bedst sparsomt, som effekt.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Depth** | Hvor stærk den sweepende effekt er. Højere værdier gør flangingen mere tydelig. | 0 til 100 % (25) |
| **Feedback** | Hvor meget af outputtet der føres tilbage i effekten. Højere værdier gør flangeren mere resonant og metallisk. | -99 til +99 % (-50) |
| **Rate** | Hvor hurtigt sweepet bevæger sig op og ned. Højere værdier giver en hurtigere, mere glimtende bevægelse. | 0 til 10 Hz (0,25) |
| **Delay** | Basis-delaytiden, sweepet er bygget på. Højere værdier giver en dybere, mere hul karakter. | 0 til 4 ms (2,0) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Classic** | En balanceret, klassisk flanger. Et godt udgangspunkt for guitarer og keys. |
| **Subtle** | En blid, underspillet sweep. Tilføjer bevægelse uden at dominere lyden. |
| **Deep** | En dyb, tung sweep med stærk feedback. Stor og dramatisk. |
| **Jet** | En intens sweep med positiv feedback, den klassiske jetfly-whoosh. |
| **Fast** | En hurtig, glimtende sweep med masser af bevægelse og energi. |
| **Wide** | En langsom, bred sweep med en lang delay. Frodig og rummelig. |

## Echo (gentagelser)

**Hvad den gør:** Gentager lyden som falmende ekkoer for en fornemmelse af rum og dybde. Vælg et preset, eller indstil selv våd-mikset, feedback og delay. Det er som at råbe ud i en kløft: lyden kommer tilbage en eller flere gange efter et kort mellemrum. En enkelt kort gentagelse tilføjer krop og en retro-fornemmelse, mens længere gentagelser med mere feedback skaber rummelige, slæbende haler. Ping Pong-preset'et lader gentagelserne springe mellem dit venstre og højre øre, hvilket er sjovt på hovedtelefoner. Hold våd-mikset moderat, så ekkoerne understøtter musikken frem for at dække den.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Wet mix** | Hvor høje ekkoerne er sammenlignet med den originale lyd. Højere værdier får gentagelserne til at skille sig mere ud. | -2 til +2 (0,6) |
| **Feedback** | Hvor mange gange ekkoet gentages. Højere værdier giver flere gentagelser, der tager længere tid at falme. | -1 til +1 (0,5) |
| **Delay** | Tiden mellem ekkoer. Kortere værdier giver en tæt slap-back; længere værdier giver spredte gentagelser. | 0,01 til 2 s (0,4) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Slapback** | En enkelt, tæt gentagelse lige bag lyden. Klassisk rockabilly-slap-back. |
| **Room** | Et kort, naturligt ekko, som et lille rum. Tilføjer rum uden at udtvære lyden. |
| **Tape** | Varme, mellemlange gentagelser, der falmer gradvist, som en gammel tape-delay. |
| **Dub** | Lange, tunge gentagelser med stærk feedback. Stor, dubbet og rummelig. |
| **Ping Pong** | Ekkoer springer mellem venstre og højre højttaler for en bred stereoeffekt. |
| **Long** | Langsomme, bredt spredte gentagelser, der ebber ud langt bag lyden. |

## Chorus (tykkere, bredere lyd)

**Hvad den gør:** Fortykker og udvider lyden ved at lægge en skiftende kopi over originalen. Vælg et preset, eller indstil selv våd/tør-mikset, depth, rate og feedback. Den får ét instrument eller én stemme til at lyde som flere, der spiller sammen, ved at tilføje let fejlstemte, bevægelige kopier. Dette tilføjer fylde og et blidt glimt. Subtile indstillinger varmer tingene op, mens stærke indstillinger lyder frodige og drømmende. Den er populær på guitarer, keyboards og vokal.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Wet/Dry** | Hvor meget af chorussen du hører sammenlignet med den originale lyd. Højere værdier gør effekten mere tydelig. | 0 til 100 % (50) |
| **Depth** | Hvor langt pitchen svinger op og ned. Højere værdier giver en tykkere, mere glimtende lyd. | 0 til 100 % (25) |
| **Rate** | Hvor hurtigt glimtet bevæger sig. Langsommere rater lyder blide og frodige; hurtigere rater lyder mere som vibrato. | 0 til 10 Hz (1,1) |
| **Feedback** | Hvor meget af effekten der føres tilbage i sig selv. Højere værdier gør chorussen mere resonant og intens. | -99 til +99 % (25) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Subtle** | En blid fortykkelse, der tilføjer varme uden at trække opmærksomhed til sig selv. |
| **Lush** | En rig, klassisk chorus. En fantastisk alsidig indstilling til guitarer og keys. |
| **Ensemble** | Et fuldt, lagdelt glimt, der får et enkelt instrument til at lyde som flere. |
| **Vibrato** | Fuldt våd med en hurtig rate, for et bævrende vibrato i stedet for en subtil chorus. |
| **Wide** | Et langsomt, bredt glimt, der åbner stereobilledet op. Rummeligt og drømmende. |
| **Twelve-String** | Et lyst, resonant glimt, der minder om en tolvstrenget guitar. |

## Distortion (grus og kant)

**Hvad den gør:** Tilføjer grus og kant ved at overdrive lyden. Vælg et preset, eller indstil selv drive, output og tone. Den gør lyden bevidst grovere, fra en varm, gruset kant til en brudt, fuzzy tone. Det er en kreativ, for-sjov-effekt frem for en måde at forbedre kvaliteten på, så brug den i små mængder. Den er sjov på elektroniske, rock- og eksperimentelle numre. Sænk Output, hvis et tungt preset bliver for højt.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Drive** | Hvor hårdt lyden forvrænges. Højere værdier er mere grusede og aggressive. | 0 til 100 % (15) |
| **Output** | Output-niveauet efter distortion. Sænk det, hvis en tung indstilling bliver for høj. | -60 til 0 dB (-18) |
| **Tone** | Ruller diskanten af før distortion. Lavere værdier lyder mørkere og varmere. | 100 til 8000 Hz (8000) |
| **Center** | Hvilken frekvens distortionen er fokuseret omkring. Skifter karakteren lysere eller mørkere. | 100 til 8000 Hz (2400) |
| **Width** | Hvor bred den fokusering er. Smal lyder skarp og nasal; bred lyder fuld og åben. | 100 til 8000 Hz (2400) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Warm Drive** | Et let, varmt grus, der tilføjer kant uden at ændre karakteren meget. |
| **Crunch** | En klassisk crunchy overdrive, punchy og rytmisk. |
| **Overdrive** | En lys, driven tone med masser af bid. Fantastisk til lead-lyde. |
| **Fuzz** | En tyk, mættet fuzz. Tung og fuld af overtoner. |
| **Metal** | En tæt, mellemtone-fokuseret high-gain-tone til aggressive, tunge lyde. |
| **Screamer** | En mellemtone-boostet overdrive, der skærer igennem, som en tube screamer. |
| **LoFi** | En knust, smalbånds-distortion til en gruset lo-fi-karakter. |

## Rotate (roterende stereo)

**Hvad den gør:** Drejer lyden rundt i stereofeltet for en roterende, hvirvlende effekt. Vælg et preset, eller indstil selv rate. Den bevæger langsomt lyden rundt i dine venstre og højre kanaler, lidt som en roterende højttaler, hvilket tilføjer en hvirvlende, hypnotisk fornemmelse. Langsomme indstillinger er blide og brede, mens hurtige indstillinger er svimlende og tydelige. Det er en stereoeffekt, så den er mest mærkbar på hovedtelefoner eller velplacerede højttalere.

**Skyder:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Rate** | Hvor hurtigt lyden drejer rundt i stereofeltet. Negative værdier drejer den anden vej; nul holder den stille. | -5 til +5 Hz (1,0) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Slow Pan** | En langsom, blid drift fra side til side. Subtil og bred. |
| **Sway** | En stabil venstre-højre-svingning. Tilføjer blid bevægelse til stereobilledet. |
| **Rotary** | En medium rotation, der minder om en roterende højttaler. |
| **Fast Spin** | En hurtig rotation rundt i stereofeltet for en svimlende, hvirvlende effekt. |
| **Reverse** | En medium rotation i den modsatte retning. |
| **Whirl** | En meget hurtig hvirvel. Intens og desorienterende. |

## Crossfeed (naturlig lyd på hovedtelefoner)

På højttalere hører hvert af dine ører både den venstre og den højre højttaler, bare på lidt forskellige tidspunkter og ved forskellige lydstyrker. På hovedtelefoner er den naturlige blanding væk: dit venstre øre hører kun den venstre kanal og dit højre øre kun den højre. Denne «super-stereo» kan få musikken til at føles, som om den er delt inde i dit hoved, og hårdt panorerede optagelser, hvor et instrument sidder helt på den ene side, kan føles unaturlige eller trættende på lange lyttesessioner.

Crossfeed løser dette ved at blande en lille, filtreret mængde af hver kanal ind i den anden, med en lille forsinkelse og en blid udrulning af de høje frekvenser. Det er tæt på, hvordan lyd fra rigtige højttalere når begge dine ører, herunder den måde, hvorpå dit hoved lidt skygger for det fjerne øre. Resultatet er et mere naturligt, højttalerlignende billede, der sidder en smule foran dig i stedet for inde i dit hoved, og det reducerer lyttetræthed på lange sessioner. Flacbox bruger den velkendte **bs2b (Bauer stereophonic-to-binaural)**-metode, en respekteret open source-crossfeed brugt af mange audiofile afspillere. Du kan læse om algoritmen på [bs2b-projektsiden](https://bs2b.sourceforge.net/).

**Cutoff** styrer, hvor varm blandingen lyder, og **Feed level** styrer, hvor stærk den er. Preset'ene dækker de klassiske bs2b-niveauer, fra en knap mærkbar antydning op til en fast, højttalerlignende blanding. Crossfeed er en hovedtelefoneffekt, så lad den være slukket, når du lytter på højttalere.

**Skydere:**

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Cutoff** | Indstiller, hvor blødningen mellem kanaler begynder at rulle af. Lavere værdier giver en varmere, mere udtalt effekt. | 300 til 2000 Hz (700) |
| **Feed level** | Styrer, hvor meget af den ene kanal der bløder ind i den anden. Højere værdier producerer en mere højttalerlignende lyd. | 1 til 15 dB (4,5) |

**Presets:**

| Preset | Hvad det gør |
|---|---|
| **Subtle** | Knap mærkbar crossfeed til afslappet lytning. Blødgør hårdt panoreret stereo uden at ændre tonebalancen. |
| **Chu Moy** | Den klassiske alsidige standard. Balanceret og let varm, den fungerer på næsten ethvert materiale. Start her. |
| **Strong** | Stærkere blødning til hårdere panorerede mix. Mere tydelig stereoindsnævring. |
| **Jan Meier** | Populær blandt hovedtelefonentusiaster. Bredere feed, mere højttalerlignende gengivelse, let basløft. |
| **Speaker-like** | Tunet til den mest naturlige højttalerlignende gengivelse over hovedtelefoner. |
| **Vintage Stereo** | Aggressiv crossfeed tunet til 1960'er- og 1970'er-mix med hårdt panorerede trommer og vokal. |

## Signalbehandling: byg din egen DSP-kæde

Ud over de færdiglavede effekter lader Flacbox dig bygge din egen kæde i **Indstillinger > Lydafspiller > Signalbehandling**. Som appen forklarer, når kæden er tom: *«Tryk på + for at tilføje en effekt. Tænd og sluk for hver enkelt med dens kontakt, træk for at ændre rækkefølgen, tryk for at redigere dens parametre, og hold nede for at duplikere eller slette.»*

**Rækkefølgen betyder noget**: et filter før en distortion lyder anderledes end det samme filter efter den. Du kan også pege hele kæden mod **Alle kanaler**, **Venstre kanal** eller **Højre kanal**.

Nedenfor er hver blok, med appens egen tekst for hver skyder og hvert preset.

### Gain (niveautrim)

Hæver eller sænker niveauet på ét punkt i kæden.

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Gain** | Booster eller skærer niveauet på dette punkt i kæden. Brug den til at kompensere for niveau efter andre effekter, eller til at drive dem, der følger. | -24 til +24 dB (0) |

| Preset | Hvad det gør |
|---|---|
| **Unity** | Ingen ændring i niveau. Et neutralt udgangspunkt. |
| **Cut** | Et stort cut. Tæmmer en høj kilde, eller skaber plads før de effekter, der følger. |
| **Trim** | Et blidt cut for at trække niveauet lidt tilbage. |
| **Lift** | Et moderat boost for at bringe en stille kilde op. |
| **Boost** | Et stærkt boost til stille materiale, eller for at drive de følgende effekter hårdere. |
| **Max** | Maksimalt boost. Højt, pas på clipping senere i kæden. |

### Low Pass (fjerner diskant)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Cutoff** | Indstiller, hvor filteret begynder at rulle diskanten af. Sænk det for at gøre lyden mørkere og blødere; hæv det mod toppen for at åbne fuldt. | 20 Hz til 20 kHz (20 kHz) |
| **Resonance** | Fremhæver frekvenserne lige ved cutoff. Hold den lav for en ren udrulning; hæv den for en spids, hvinende kant. | 0,1 til 10 (0,707) |

| Preset | Hvad det gør |
|---|---|
| **Air** | Trimmer kun den allerøverste top. Tager lidt kant af uden at sløve lyden. |
| **Warm** | En blid udrulning af diskanten for en varmere, rundere tone. |
| **Mellow** | Mærkbart blødgjort. Trækker lysstyrken tilbage for en afslappet fornemmelse. |
| **Muffled** | Mørk og dæmpet, som hørt gennem en væg. |
| **Telephone** | En smal, resonant peak lavt i området. En tynd, telefonlignende stemme. |

### High Pass (fjerner bas)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Cutoff** | Indstiller, hvor filteret begynder at rulle bunden af. Hæv det for at tynde bunden ud og fjerne rumlen; sænk det mod bunden for at åbne fuldt. | 20 Hz til 20 kHz (20 Hz) |
| **Resonance** | Fremhæver frekvenserne lige ved cutoff. Hold den lav for en ren udrulning; hæv den for en spids, hvinende kant. | 0,1 til 10 (0,707) |

| Preset | Hvad det gør |
|---|---|
| **Rumble Cut** | Fjerner subsonisk rumlen og DC-offset uden at røre den hørbare bund. |
| **Tighten** | Trimmer rungende lave frekvenser for en strammere, renere bas. |
| **Thin** | Skærer varmen og kroppen, hvilket efterlader en lettere, tyndere lyd. |
| **Radio** | Kun mellemtonerne og diskanten er tilbage, som en lille radiohøjttaler. |
| **Telephone** | En smal, resonant peak højt i området. En tynd, telefonlignende stemme. |

### Band Pass (holder et midterbånd)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Center** | Indstiller den frekvens, filteret lader passere. Alt over og under den rulles af. Sweep den for at plukke bas, mellemtoner eller diskant ud. | 20 Hz til 20 kHz (1 kHz) |
| **Resonance** | Styrer, hvor bredt båndet er. Lave værdier lader et bredt område passere; hæv den for at indsnævre til centret for en skarp, resonant tone. | 0,1 til 10 (0,707) |

| Preset | Hvad det gør |
|---|---|
| **Voice** | Et bredt bånd omkring mellemtoneområdet, hvor det meste vokal sidder. Et neutralt udgangspunkt. |
| **Bass** | Isolerer bunden, hvilket kun efterlader bassen og kicket. |
| **Body** | Fokuserer på de lave mellemtoner for en varm, kasseagtig krop. |
| **Presence** | Løfter de øvre mellemtoner for klarhed og tilstedeværelse. |
| **Telephone** | Et smalt mellemtonebånd. En tynd, telefonlignende lyd. |
| **Wah** | En meget smal, resonant peak. Sweep centret for en wah-effekt. |

### Notch (fjerner ét smalt bånd)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Frequency** | Indstiller den frekvens, filteret fjerner. Alt over og under den passerer igennem. Indstil den på en brummen eller resonans for at skære den ud. | 20 Hz til 20 kHz (60 Hz) |
| **Resonance** | Styrer, hvor bredt cuttet er. Lave værdier skovler et bredt område ud; hæv den for kun at fjerne et punktbånd og lade resten være urørt. | 0,1 til 10 (8,0) |

| Preset | Hvad det gør |
|---|---|
| **Mains Hum 60** | Fjerner 60 Hz elektrisk brummen (nordamerikansk netstrøm). Et neutralt udgangspunkt. |
| **Mains Hum 50** | Fjerner 50 Hz elektrisk brummen (europæisk og anden netstrøm). |
| **Rumble** | Skærer en lavfrekvent rumlen eller resonans uden at tynde hele bunden ud. |
| **Mud** | Skovler lav-mellemtone-mudder ud for en renere, klarere lyd. |
| **Boxy** | Fjerner en kasseagtig mellemtone-honk. |
| **Harsh** | Tæmmer en hård, gennemtrængende peak i de øvre mellemtoner. |

### Peaking (parametrisk EQ-bånd)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Frequency** | Centret for båndet, der skal boostes eller skæres. Sweep den for at finde den frekvens, du vil forme. | 20 Hz til 20 kHz (1 kHz) |
| **Gain** | Hvor meget der skal boostes eller skæres ved centret. Positiv løfter båndet; negativ skovler det ud. | -15 til +15 dB (0) |
| **Q factor** | Indstiller, hvor bredt båndet er. Lave værdier former et bredt område; høje værdier indsnævrer for kirurgiske, punktvise ændringer. | 0,1 til 10 (1,0) |

| Preset | Hvad det gør |
|---|---|
| **Presence** | Et bredt øvre-mellemtoneløft for klarhed og tilstedeværelse. Et neutralt udgangspunkt. |
| **Warmth** | Et bredt lav-mellemtone-boost, der tilføjer krop og varme. |
| **Vocal Boost** | Løfter kerne-vokalområdet for at bringe stemmer frem. |
| **Cut Mud** | Skovler kasseagtigt lav-mellemtone-mudder ud for en renere lyd. |
| **Tame Harsh** | Et smalt cut for at tæmme en hård, gennemtrængende peak. |
| **Punch** | Et lavt boost, der tilføjer punch og gennemslagskraft til bunden. |
| **Sub Boost** | Et dybt boost i den allernederste bund for ekstra sub-bas-vægt. |
| **Air** | Et bredt løft i toppen for en åben, luftig glans. |
| **Clarity** | Løfter de høje mellemtoner for at tilføje definition og kant. |
| **De-Ess** | Et smalt cut i sibilansområdet for at tæmme hårde S-lyde. |
| **De-Boom** | Skærer en rungende lavfrekvent opbygning for en strammere bund. |
| **Scoop** | Et bredt mellemtonedyk for en udskåret, moderne tone. |

### Low Shelf (baskontrol og bass boost)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Frequency** | Indstiller hjørnet, under hvilket shelfen træder i kraft. Alt under det boostes eller skæres samlet. | 20 til 2000 Hz (200) |
| **Gain** | Hvor meget bunden skal løftes eller sænkes. Positiv tilføjer vægt og varme; negativ tynder den ud. | -15 til +15 dB (0) |

| Preset | Hvad det gør |
|---|---|
| **Warmth** | Et blidt bundløft for varme og krop. Et neutralt udgangspunkt. |
| **Bass Boost** | Et solidt boost af bassen for vægt og punch. |
| **Fullness** | Fylder de lave mellemtoner ud for en fyldigere, rundere lyd. |
| **Trim Bass** | Et moderat cut for at lette et bastungt mix. |
| **Cut Lows** | Et stærkt cut for at tynde ud eller de-boome bunden. |
| **Big Bottom** | Et stort bundløft for maksimal vægt og rumlen. |

### High Shelf (diskantkontrol)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Frequency** | Indstiller hjørnet, over hvilket shelfen træder i kraft. Alt over det boostes eller skæres samlet. | 1 til 20 kHz (8 kHz) |
| **Gain** | Hvor meget toppen skal løftes eller sænkes. Positiv tilføjer lysstyrke og luft; negativ udjævner og gør mørkere. | -15 til +15 dB (0) |

| Preset | Hvad det gør |
|---|---|
| **Presence** | Et blidt topløft for klarhed og detalje. Et neutralt udgangspunkt. |
| **Air** | Åbner den allerøverste top op for en luftig, åben lyd. |
| **Bright** | Et stærkt boost for en skarp, lys, fremtrukket tone. |
| **Soften** | Et moderat cut for at tage kanten af hård diskant. |
| **Tame Highs** | Et stærkt cut for at gøre en alt for lys lyd mørkere og glattere. |
| **Sparkle** | Et stort topboost for maksimalt glimt og glans. |

### Soft Clip (varm mætning)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Drive** | Skubber signalet hårdere ind i waveshaperen. Lave mængder tilføjer blid varme; høje mængder runder peaks til tyk mætning og grus. | 0 til 40 dB (0) |

| Preset | Hvad det gør |
|---|---|
| **Warm** | En anelse drive for blid, analog-agtig varme. |
| **Drive** | Mærkbar mætning, der fortykker og farver lyden. |
| **Crunch** | Kraftig drive med en hørbar crunchy kant. |
| **Fuzz** | Tyk, fuzzy distortion. Peaks er klemt hårdt. |
| **Destroy** | Maksimal drive. Aggressivt, fuldt mættet grus. |

### Bit Crusher (retro lo-fi)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Bit depth** | Indstiller, hvor mange bits der beskriver hver sample. Færre bits betyder grovere trin og mere kvantiseringsstøj, for en crunchy, gruset digital lyd. | 1 til 16 bits (16) |
| **Sample rate** | Nedsampler lyden. Ved hundrede procent er raten urørt; sænk den for at holde hver sample længere, hvilket sløver diskanten og tilføjer en hård, aliaset kant. | 1 % til 100 % (100 %) |

| Preset | Hvad det gør |
|---|---|
| **Vintage** | Et subtilt fald i kvalitet, som en tidlig digital sampler. |
| **LoFi** | Klassisk 8-bit, halv-rate lo-fi. Kornet og retro. |
| **Crunch** | Kraftigere knusning med en hørbar crunchy kant. |
| **Gritty** | Grov og gruset. Trinnene mellem niveauer er tydelige. |
| **Destroy** | Ekstrem reduktion. Hård, brudt, næppe genkendelig. |

### Ring Modulator (metalliske og robotagtige toner)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Carrier** | Indstiller frekvensen af den tone, signalet multipliceres med. Nogle få hertz giver en tremolo-vibreren; højere frekvenser tilføjer metalliske, klokkelignende og robotagtige overtoner. | 1 til 4000 Hz (440) |
| **Mix** | Blander den modulerede lyd ind med originalen. Ved nul procent hører du kun det tørre signal; ved hundrede procent kun den fuldt modulerede tone. | 0 % til 100 % (0 %) |

| Preset | Hvad det gør |
|---|---|
| **Tremolo** | En meget lav carrier gør den til en amplitude-tremolo, der vibrerer lydstyrken. |
| **Robot** | En medium carrier tilføjer klingende overtoner for en klassisk robotstemme-effekt. |
| **Metallic** | Tætte, inharmoniske overtoner for en hård, metallisk tone. |
| **Bell** | En højere carrier giver lys, klokkelignende ringen. |
| **Alien** | Fuldt våd med en høj carrier. Ekstrem, fremmedartet, næppe genkendelig. |

### Tremolo (lydstyrkevibreren)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Rate** | Indstiller, hvor hurtigt lydstyrken pulserer. Langsommere rater giver en glat svingning; hurtigere rater giver en hurtig stutter. | 0,1 til 20 Hz (5) |
| **Depth** | Indstiller, hvor meget lydstyrken falder ved hver puls. Ved nul procent er niveauet stabilt; ved hundrede procent dykker det helt ned til stilhed. | 0 % til 100 % (0 %) |

| Preset | Hvad det gør |
|---|---|
| **Gentle** | En langsom, overfladisk svingning. Subtil bevægelse uden at trække opmærksomhed. |
| **Classic** | Den klassiske forstærker-tremolo: en medium rate og moderat depth. |
| **Deep** | En stærk, dyb puls, der næsten dykker til stilhed hver cyklus. |
| **Fast** | En hurtig flagren for en glimtende, nervøs fornemmelse. |
| **Chop** | Hurtig og fuld depth. En hård, stutterende chop. |

### Delay (ekko)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Time** | Indstiller mellemrummet før hvert ekko. Korte tider giver en tæt slapback; længere tider spreder gentagelserne længere fra hinanden. | 0,01 til 2 s (0,25) |
| **Feedback** | Indstiller, hvor meget af hvert ekko der føres tilbage. Lave værdier giver en enkelt gentagelse; højere værdier bygger en lang, slæbende række af ekkoer. | 0 til 0,95 (0,4) |
| **Mix** | Blander ekkoerne ind med originalen. Ved nul procent hører du kun det tørre signal; ved hundrede procent kun ekkoerne. | 0 % til 100 % (0 %) |

| Preset | Hvad det gør |
|---|---|
| **Slapback** | Et enkelt kort ekko, tæt op mod originalen. Rockabilly og vokal-fordobling. |
| **Echo** | Det klassiske ekko: en klar gentagelse med et par slæbende haler. |
| **Ping** | En hurtig, hoppende gentagelse, der tilføjer rytmisk bevægelse. |
| **Ambient** | Længere, blødere gentagelser, der ebber ud i en rummelig hale. |
| **Dub** | Høj feedback for lange, dubbede kaskader af ekko. |
| **Cavern** | Lange, dybe gentagelser, som lyd der ekkoer gennem et enormt rum. |

### Stereo Width (indsnævr eller udvid)

| Kontrol | Hvad den gør | Interval (standard) |
|---|---|---|
| **Width** | Indsnævrer eller udvider stereobilledet. Nul procent kollapser til mono, hundrede procent lader det være urørt, og højere værdier skubber siderne bredere. Påvirker kun stereonumre på Alle-kanaler-målet. | 0 % til 200 % (100 %) |

| Preset | Hvad det gør |
|---|---|
| **Wide** | En blid udvidelse, der åbner stereobilledet op. Et neutralt udgangspunkt. |
| **Wider** | En stærkere spredning for et stort, medrivende stereofelt. |
| **Max** | Maksimal bredde. Meget bred, men pas på mono-kompatibilitetsproblemer. |
| **Narrow** | Trækker siderne ind for et strammere, mere centreret billede. |
| **Focused** | Næsten centreret, med kun en antydning af stereo. |
| **Mono** | Fuldt kollapset til mono. Begge højttalere spiller det samme signal. |

## Sådan fungerer det hele under motorhjelmen (simpel version)

- **Motorer:** du vælger én i Indstillinger > Lydafspiller > Afspilningsmotor: **Standard** (system), **Universal** (FFmpeg) eller **Sound FX** (**BASS™-motoren** fra [Un4seen Developments](https://www.un4seen.com/)). Den motor, du vælger, bestemmer, hvilke formater der afspilles, og effekterne, equalizeren og DSP-kæden kører kun i Sound FX-motoren.
- **Formater:** BASS™-motoren tilføjer FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus og modul-musik (tracker) oven i system- og FFmpeg-formaterne.
- **Effekter:** equalizeren, compressoren og de fleste effekter bruger BASS™-effekt-add-ons. Freeverb er Freeverb-rumklangen. Chorus, Flanger og Distortion bruger klassiske DirectX-lignende effekter med deres egne kontroller.
- **Volume Normalization:** en live **EBU R128**-loudness-niveaudeler (den loudness-standard, der bruges i broadcast og streaming).
- **Crossfeed:** **bs2b (Bauer)**-crossfeeden, kørt inde i BASS™-motoren.
- **DSP-kæde:** dine brugerdefinerede blokke, anvendt i præcis den rækkefølge, du indstiller, på alle kanaler eller kun én side.
- **Output:** du kan indstille samplingsraten, kanalantallet og bufferstørrelsen, så de matcher dit udstyr.

Fordi alt dette kører live, mens musikken spiller, gør effekterne:

- Fungerer i **realtid** på alt, herunder cloud-filer, streams og modul-musik.
- **Ændrer eller gemmer aldrig** dine filer igen. Sluk for en effekt, og originalen vender tilbage.
- **Husker dine indstillinger** for hver effekt.
- Kan **mikses og matches** frit, da hver enkelt er separat.

## Enkle opskrifter at prøve

**Daglig lytning**

- **Mere bas, rent:** Equalizer > Bass Booster, sænk derefter Preamplifier 1 til 2 dB. Eller tilføj en DSP Low Shelf på Bass Boost.
- **Jævn lydstyrke på tværs af en blandet afspilningsliste:** Volume Normalization > Standard, plus Compressor > Soft.
- **Blid samlet polering:** Compressor > Transparent, plus Volume Normalization > Light.
- **Klarere vokal:** Equalizer > Vocal Booster, eller en DSP Peaking-blok på Vocal Boost.
- **Fyldigere lyd på små telefonhøjttalere:** Equalizer > Small Speakers.

**Hovedtelefoner**

- **Rarere, mindre trættende på hovedtelefoner:** Crossfeed > Chu Moy eller Jan Meier.
- **Bredere lyd på hovedtelefoner:** DSP Stereo Width > Wide, plus Crossfeed > Chu Moy.
- **Fix hårdt panorerede 1960'er- og 1970'er-plader:** Crossfeed > Vintage Stereo.
- **Lidt luft og rum:** Freeverb > Ambience, holdt lavt, plus Crossfeed > Subtle.

**Stille tider og talt lyd**

- **Natlig stille lytning:** Volume Normalization > Night, plus Compressor > Late Night.
- **Podcasts og lydbøger:** Compressor > Voice / Podcast, plus Equalizer > Spoken Word.
- **Højeste, mest jævne lyd i en støjende bil:** Volume Normalization > Strong, plus Compressor > Heavy.

**Løsning af problemer**

- **Tæm en hård, lys optagelse:** Equalizer > Treble Reducer, eller en DSP Peaking-blok på Tame Harsh.
- **Fjern elektrisk brummen:** DSP-kæde > Notch > Mains Hum 60 (eller Mains Hum 50 i Europa).
- **Strammere, renere bas:** DSP High Pass > Tighten, for at skære den rungende bund.
- **Mindre boom i et bastungt mix:** DSP Low Shelf > Trim Bass, eller Peaking > De-Boom.

**Kreativt og sjovt**

- **Varm, rummelig fornemmelse:** Freeverb > Hall, holdt lavt.
- **Drømmende, rummelige guitarer:** Chorus > Wide, plus Echo > Long.
- **Retro lo-fi:** DSP-kæde > Bit Crusher (LoFi) ind i Soft Clip (Warm).
- **Funky bevægelse på elektroniske numre:** Auto Wah > Funky, eller Phaser > Fast.
- **Klassisk jetfly-sweep:** Flanger > Jet.

## FAQ

{{% details title="Hvilken lydmotor bruger Flacbox?" closed="true" %}}
Du vælger én Afspilningsmotor i Indstillinger > Lydafspiller: Standard (Apples systemmotor), Universal (FFmpeg-motoren) eller Sound FX (BASS™-motoren fra Un4seen Developments, un4seen.com). Den motor, du vælger, bestemmer, hvilke filformater der afspilles. Sound FX er den, der afspiller ekstra formater som FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus og MOD- eller tracker-musik, og den er den eneste motor, der leverer live-effekterne, den 10-bånds equalizer og DSP-kæden. For at bruge effekterne skal du sætte Afspilningsmotoren til Sound FX.
{{% /details %}}

{{% details title="Kan Flacbox afspille MOD, XM, IT og anden tracker- eller modul-musik?" closed="true" %}}
Ja. BASS™-motoren har en indbygget modulafspiller, der indlæser MOD-, XM-, IT-, S3M-, MTM-, UMX- og MO3-filer og genopbygger sangen live ud fra dens mønstre og instrumentlyde, sådan som tracker-musik er tænkt at skulle afspilles. Almindelige iPhone-afspillere kan ikke dette. Effekter og equalizeren fungerer også på modul-musik.
{{% /details %}}

{{% details title="Understøtter Flacbox DSD- og high-resolution-filer?" closed="true" %}}
Ja. Flacbox afspiller DSD-filer (DSF og DFF) gennem BASS™-motoren ved hjælp af DSD over PCM, så de fungerer på normal output-hardware, plus FLAC, WavPack, Monkey's Audio (APE), Musepack og TrueAudio til lossless-afspilning.
{{% /details %}}

{{% details title="Hvilke lydeffekter har Flacbox?" closed="true" %}}
En 10-bånds equalizer, Volume Normalization, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate og Crossfeed, plus en byg-selv DSP-kæde med filtre, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay og stereo width. Hver enkelt er separat og kan kombineres med de andre.
{{% /details %}}

{{% details title="Hvad er et preset?" closed="true" %}}
Et preset er en færdiglavet indstilling for en effekt. I stedet for selv at flytte skydere trykker du på et preset, og lyden ændrer sig, så den matcher. Hver effekt i Flacbox har flere presets, og denne guide angiver, hvad hver enkelt gør. Hvis du flytter en skyder efter at have valgt et preset, viser effekten «Manual» for at fortælle dig, at den nu bruger dine egne værdier.
{{% /details %}}

{{% details title="Hvordan åbner jeg lydeffekterne i Flacbox?" closed="true" %}}
Åbn Afspilles nu-afspilleren, tryk på ⋯ (Mere)-knappen, og vælg Lydeffekter. Eller gå til Indstillinger > Lydafspiller > Lydeffekter. Tryk på en effekt, tænd for dens kontakt, og vælg et preset, eller åbn skyderne for at finjustere.
{{% /details %}}

{{% details title="Hvor er equalizeren, og hvad er de bedste indstillinger?" closed="true" %}}
Gå til Indstillinger > Lydafspiller > Lydequalizer. Den har 10 bånd fra 32 Hz til 16 kHz, hver fra -12 til +12 dB, plus en -24 til +24 dB Preamplifier og 22 presets. For mere bas, brug Bass Booster. For klarere stemmer, brug Vocal Booster eller Pop. For en lysere lyd, brug Treble Booster. Juster derefter enkelte bånd efter smag.
{{% /details %}}

{{% details title="Hvordan booster jeg bassen i Flacbox?" closed="true" %}}
To nemme måder. I Lydequalizer, vælg Bass Booster (eller hæv 32 Hz- og 64 Hz-båndene et par dB). Eller, i Signalbehandling, tilføj en Low Shelf-blok sat til Bass Boost. I begge tilfælde skal du sænke Preamplifier eller tilføje en Gain-blok 1 til 2 dB, så bassen forbliver ren og ikke forvrænges.
{{% /details %}}

{{% details title="Hvilket equalizer-preset er bedst til min musik?" closed="true" %}}
Rock og Electronic tilføjer energi med stærk bund og diskant. Acoustic, Jazz og Classical forbliver varme og naturlige. Pop og Vocal Booster skubber stemmer frem. Bass Booster og Hip-Hop tilføjer vægt. Deep og Loudness lyder fyldigere ved lav lydstyrke. Start med den, der matcher din genre, og finjuster derefter.
{{% /details %}}

{{% details title="Hvad er Volume Normalization, og hvordan adskiller den sig fra ReplayGain?" closed="true" %}}
Den får hvert nummer til at spille ved omtrent den samme loudness. Den måler den reelle loudness ved hjælp af EBU R128-standarden (i LUFS, som streamingtjenester) og justerer hvert nummer mod dit mål, med en max-boost-grænse. I modsætning til ReplayGain behøver den ingen tags i dine filer og fungerer på enhver kilde, live, uden at ændre lyden. Presets: Light, Standard, Strong og Night.
{{% /details %}}

{{% details title="Hvad er Crossfeed, og bør jeg bruge den?" closed="true" %}}
Crossfeed blander lidt af de venstre og højre kanaler sammen, så hovedtelefoner føles mere som rigtige højttalere og mindre som om lyden sidder fast i dit hoved. Den er kun til hovedtelefoner, så sluk for den til højttalere. Flacbox bruger bs2b (Bauer)-metoden, med presets som Chu Moy og Jan Meier.
{{% /details %}}

{{% details title="Hvad er forskellen mellem Compressor og Volume Normalization?" closed="true" %}}
Volume Normalization matcher loudness mellem forskellige sange. Compressor udjævner de høje og stille dele inde i en enkelt sang. De løser forskellige problemer og fungerer godt sammen, især i en bil eller på et støjende sted.
{{% /details %}}

{{% details title="Hvad er Signalbehandlings-kæden (DSP)?" closed="true" %}}
Det er et byg-selv-rack i Indstillinger > Lydafspiller > Signalbehandling. Tilføj blokke som filtre, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay og stereo width, sæt dem i enhver rækkefølge, tænd og sluk for hver, og peg kæden mod alle kanaler, venstre eller højre. Fordi rækkefølgen betyder noget, kan du designe præcis den lyd, du vil have.
{{% /details %}}

{{% details title="Hvad er forskellen mellem equalizeren, effekterne og DSP-kæden?" closed="true" %}}
Equalizeren er en simpel 10-bånds tonekontrol. Lydeffekterne er færdiglavede værktøjer (compressor, rumklang, ekko og så videre) med presets. DSP-kæden er, hvor du bygger din egen effektrækkefølge fra individuelle blokke. Du kan køre alle tre på samme tid.
{{% /details %}}

{{% details title="Ændrer eller beskadiger effekterne mine musikfiler?" closed="true" %}}
Nej. Alt anvendes live, mens musikken spiller. Dine filer ændres eller gemmes aldrig igen. Sluk for en effekt, og den originale lyd vender tilbage med det samme.
{{% /details %}}

{{% details title="Kan jeg bruge mere end én effekt på samme tid?" closed="true" %}}
Ja. Hver effekt har sin egen kontakt, og der er ingen hovedkontakt, så enhver kombination fungerer. For eksempel Volume Normalization plus Compressor for jævn lytning, eller Freeverb plus Crossfeed på hovedtelefoner, med equalizeren oven i.
{{% /details %}}

{{% details title="Hvorfor er effektkontrollerne nedtonet?" closed="true" %}}
Effekten er slukket. Tænd for dens kontakt øverst i editoren for at bruge kontrollerne. Hver effekt er slukket som standard.
{{% /details %}}

{{% details title="Hvad betyder Manual-etiketten?" closed="true" %}}
Det betyder, at du flyttede en skyder væk fra et preset, så effekten nu bruger dine egne brugerdefinerede værdier i stedet for et navngivet preset. Hver skyder har en nulstillingsknap, og at vælge et preset igen erstatter dine manuelle værdier.
{{% /details %}}

{{% details title="Kan jeg gemme og dele mine equalizer-presets?" closed="true" %}}
Ja. Ud over de 22 indbyggede presets kan du lave dine egne, ændre deres rækkefølge og eksportere eller importere dem for at flytte dine indstillinger til en anden enhed.
{{% /details %}}

{{% details title="Fungerer effekterne med CarPlay, streaming og baggrundsafspilning?" closed="true" %}}
Ja. Effekterne kører inde i BASS™-motoren, så de anvendes på lokale filer, cloud-drev, medieservere, streams og modul-musik, og de bliver ved med at fungere under CarPlay og baggrundsafspilning.
{{% /details %}}

{{% details title="Kan jeg ændre lyd-output-kvaliteten?" closed="true" %}}
Ja. I Indstillinger > Lydafspiller kan du indstille output-samplingsraten, antallet af kanaler og bufferstørrelsen, så de matcher dine hovedtelefoner, højttalere eller DAC.
{{% /details %}}

{{% details title="Hvad er en god startopsætning til hovedtelefoner?" closed="true" %}}
Tænd for Volume Normalization (Standard), tilføj en let Compressor (Soft), vælg et equalizer-preset, du kan lide, og tænd for Crossfeed (Chu Moy eller Jan Meier). Lad rumklang, ekko og distortion være slukket, medmindre du ønsker en kreativ lyd.
{{% /details %}}

---

*BASS er et varemærke tilhørende Un4seen Developments Ltd. Se [un4seen.com](https://www.un4seen.com/). Crossfeed bruger bs2b (Bauer stereophonic-to-binaural)-algoritmen; se [bs2b-projektsiden](https://bs2b.sourceforge.net/).*
