---
title: "Evermusic 8.7: ægte gapless-afspilning, lydeffekter, volumennormalisering, redesignet equalizer"
date: 2026-07-05
description: "Evermusic 8.7 til iPhone, iPad og Mac tilføjer ægte gapless-afspilning, fem studielydeffekter (rumklang, delay, forvrængning, kompressor, crossfeed), EBU R128-volumennormalisering, en redesignet 10-bånds equalizer med import/eksport af forudindstillinger, en genopbygget AVAudioEngine-streamingmotor med FLAC- og Ogg Vorbis-understøttelse og hurtigere, mere præcis CarPlay og Spiller nu."
keywords: ["Evermusic 8.7", "Evermusic-opdatering", "ægte gapless-afspilning iPhone", "gapless musikafspiller iOS", "gapless-afspilning CarPlay", "lydeffekter musikafspiller iPhone", "rumklang delay forvrængning kompressor crossfeed iOS", "crossfeed hovedtelefoner iOS", "volumennormalisering iPhone", "loudness-normalisering musikafspiller", "EBU R128-normalisering iOS", "replay gain-alternativ iPhone", "10-bånds equalizer iPhone", "grafisk equalizer iOS-app", "import eksport af equalizer-forudindstillinger", "FLAC-afspiller iPhone", "Ogg Vorbis-afspiller iOS", "tabsfri musikafspiller iPhone 2026", "AVAudioEngine musikafspiller", "CarPlay musikafspiller iPhone", "Spiller nu låseskærm præcision", "sky-musikafspiller iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Gapless-afspilning", "Lydeffekter", "Rumklang", "Delay", "Forvrængning", "Kompressor", "Crossfeed", "Volumennormalisering", "EBU R128", "Equalizer", "FLAC", "Ogg Vorbis", "CarPlay", "Spiller nu", "Liquid Glass", "Nyheder"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Kort fortalt:** [Evermusic 8.7](/products/evermusic) er en udgivelse med fokus på lydkvalitet til iPhone, iPad og Mac. Den leverer **ægte gapless-afspilning** (ingen pauser, klik eller tik mellem numre), et fuldt sæt **studielydeffekter** – rumklang, delay, forvrængning, kompressor og crossfeed – og **EBU R128-volumennormalisering**, der holder loudness ensartet fra sang til sang uden ReplayGain-tags. **10-bånds equalizeren** er redesignet med nye skydere, hurtigere skift af forudindstillinger, brugerdefinerede forudindstillinger, du kan importere og eksportere, og et bedre layout i liggende format og på iPad. Under motorhjelmen forbedrer en **genopbygget AVAudioEngine-streamingmotor** pålideligheden og formatunderstøttelsen, herunder **FLAC** og **Ogg Vorbis**. **CarPlay** og **Spiller nu** er hurtigere og mere præcise på låseskærmen, i bilen og fra hovedtelefonfjernbetjeninger.

---

## Hej alle sammen!

Evermusic 8.7 er klar til download. Denne opdatering handler helt om, hvordan din musik *lyder*. Vi har genopbygget afspilningsmotoren til ægte gapless-afspilning, tilføjet et sæt lydeffekter i studiekvalitet, introduceret loudness-normalisering og redesignet equalizeren fra skyderne og op. Det hele er pakket ind i Apples nye **Liquid Glass**-design.

[Download Evermusic 8.7 fra App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), eller opdater fra din eksisterende version. Evermusic er en gratis download med valgfrie opgraderinger i appen.

## Ægte gapless-afspilning

Gapless-afspilning betyder, at stilheden mellem to numre er væk. Ingen pause, intet klik, intet tik – den aktuelle sang flyder direkte over i den næste. Det betyder mest for musik, der er designet til at høres som en helhed: **liveoptagelser, DJ-mix, klassiske værker og konceptalbum**, hvor ét nummer fader direkte over i et andet.

Her er, hvad der er ændret teknisk. Evermusics lydmotor holder to numre i spil på én gang: det, du hører, og det næste i køen. Mens det aktuelle nummer spiller, er det næste nummer allerede ved at blive **hentet, afkodet og forbuffret** i baggrunden. Når det aktuelle nummer når sin slutning, overdrager motoren til det næste nummer **inde i afspilleren, ikke inde i lydstrømmen**. Udgangens renderingsløkke bliver ved med at trække lydsamples fra en sammenhængende ringbuffer uden nogensinde at stoppe, så lytteren aldrig hører en overgang. Skiftet sker mellem samples, hvilket er præcis grunden til, at der ikke er noget hørbart hul.

Det fungerer ens, uanset om filen er på din enhed, i skyen eller på en medieserver – forbuffringen starter blot lidt tidligere for fjernkilder.

## Studielydeffekter

Evermusic 8.7 tilføjer fem lydeffekter i realtid, som du kan stable oven på din musik. Hver enkelt kører som en native lydbehandlingsknude i afspilningsmotoren, så den anvendes på alt, du afspiller – lokale filer, skystreams og internetradio – uden genkodning.

Hver effekt leveres med et **kurateret bibliotek af forudindstillinger**, så du får en fremragende lyd med ét tryk, og Evermusic **husker dine præcise indstillinger** mellem sessioner. Juster en hvilken som helst kontrol, og effekten skifter til en **Manuel** tilstand, så du altid ved, hvornår du har bevæget dig væk fra en forudindstilling.

### Rumklang

Tilføjer en fornemmelse af rum, fra et stramt lokale til en katedral. Bygget på Apples `AVAudioUnitReverb` tilbyder den **13 rumforudindstillinger** (Lille lokale, Mellemstor sal, Plade, Katedral og flere) plus en **wet/dry-mix**-kontrol fra 0 til 100 %, så du bestemmer, hvor meget rum du vil tilføje.

### Delay (ekko)

Et klassisk ekko med **10 forudindstillinger** – Slapback, Båndekko, Dub, Atmosfærisk og andre. Du kan indstille **delay-tid** (op til 2 sekunder), **feedback** (hvor mange gentagelser), et **lavpasfilter** til at varme gentagelserne op og **wet/dry-mixet**.

### Forvrængning

Fra subtil grovhed til fuld lo-fi-destruktion, drevet af `AVAudioUnitDistortion` med **22 karakterforudindstillinger** (Bit Brush, Cellphone Concert, Radio Tower og flere), en **pre-gain**-drivkontrol og et wet/dry-mix, så du kan blande effekten tilbage i det rene signal.

### Kompressor

En dynamikprocessor (Apples `AUDynamicsProcessor`), der udjævner høje og lave passager. Den giver adgang til det fulde professionelle kontrolsæt – **tærskel, ratio/headroom, attack, release, ekspansion og makeup-gain** – med **10 forudindstillinger** afstemt til virkelige situationer: blandt andet Stemme / Podcast, Sen aften, Filmdialog, Streaming-match og Maksimal loudness.

### Crossfeed

Crossfeed får lytning i hovedtelefoner til at lyde mere naturlig ved at blande lidt af den venstre kanal ind i den højre og omvendt, sådan som dine ører hører rigtige højttalere. Den er bygget på den velkendte **Bauer stereophonic-to-binaural (bs2b)**-algoritme, med kontrol over **crossfeed-niveau** og **cutoff-frekvens** og **6 forudindstillinger**, herunder de audiofil-favoritte *Chu Moy*- og *Jan Meier*-indstillinger. Den er især god på ældre, hårdt panorerede stereomix fra 1960'erne og 1970'erne.

## Volumennormalisering

Har du nogensinde lavet en playliste, hvor ét nummer buldrer, og det næste er en hvisken? Volumennormalisering løser det. Evermusic 8.7 bruger **EBU R128-loudness-måling** (samme ITU-R BS.1770-standard, som bruges i broadcast og af streamingtjenester) til at måle hvert nummers reelle oplevede loudness og blidt styre det mod et ensartet mål.

I modsætning til ReplayGain kræver den **ingen** tags i dine filer, og den ændrer **ikke** din lyd. Den fungerer i realtid på alt, du afspiller, inklusive skystreams og live radio, og nulstilles rent, når du spoler eller skifter numre.

Fire forudindstillinger dækker de almindelige tilfælde:

- **Let** – blid nivellering (mål −20 LUFS).
- **Standard** – standardvalget, streaming-agtig loudness (mål −16 LUFS, op til +12 dB løft for stille numre).
- **Kraftig** – aggressiv matchning til meget blandede biblioteker (mål −14 LUFS).
- **Nat** – mere stille og ensartet til aftenlytning ved lav lydstyrke (mål −23 LUFS).

Du behøver ikke længere række ud efter lydstyrken mellem sange.

## Redesignet equalizer

Evermusics **10-bånds grafiske equalizer** har fået et fuldt redesign. Båndene dækker **32 Hz til 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), hver justerbar fra **−12 dB til +12 dB** i fine trin på 0,1 dB, med en **preamp** fra −24 dB til +24 dB, der forhindrer klipping, når du booster.

Nyt i 8.7:

- **Nye skydere** – præcise, responsive kontroller, der overtager udseendet af den native iOS 26-systemskyder og **Liquid Glass**-materialet.
- **Hurtigere, mere jævnt skift af forudindstillinger** – hop mellem forudindstillinger øjeblikkeligt, med en redesignet vandret forudindstillingslinje i stående format og en lodret forudindstillingskolonne i liggende format.
- **Bedre layout i liggende format og på iPad** – skyderne og forudindstillingsvælgeren omarrangeres for at udnytte den ekstra bredde i stedet for at proppe sig sammen i en telefonstor kolonne.
- **Brugerdefinerede forudindstillinger** – opret og gem dine egne kurver, omarranger dem, og **importer og eksporter** forudindstillinger som `.eqp`-filer for at flytte dem mellem enheder eller dele dem.

Equalizeren kører native i motoren (`AVAudioUnitEQ`), så den anvendes på enhver kilde, og den fungerer også over AirPlay, Chromecast og CarPlay, hvor det understøttes.

## Genopbygget afspilningsmotor

Under motorhjelmen kører Evermusic 8.7 på en **genopbygget streamingmotor** bygget på Apples `AVAudioEngine` med en tilpasset renderingspipeline. Det er dette, der gør gapless-overdragelsen, effektkæden og equalizeren mulig, og det gør også dagligdags afspilning mere pålidelig.

- **Forbedret formatunderstøttelse** – herunder **FLAC** (via Core Audio) og **Ogg Vorbis** (via `libvorbisfile`), sammen med MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF og mere.
- **Smartere buffring** – en adaptiv forbuffer skaleres med din forbindelse, med en sammenhængende ringbuffer, der føder udgangen, så korte netværkshak ikke bliver til udfald.
- **Automatisk gendannelse** – en genbuffrings-tilstandsmaskine og retry-logik med backoff genoptager afspilningen rent efter et øjeblik med svagt signal i stedet for at stoppe nummeret.
- **Færre afbrydelser** – den samme motor driver lokale filer, skystreams, medieservere og internetradio, så adfærden er ensartet overalt.

## Spiller nu og CarPlay

De skærme, du faktisk kigger på, mens du lytter – **låseskærmen**, **CarPlay** og din bils eller dine hovedtelefoners fjernbetjeningsknapper – er mere præcise og hurtigere i 8.7.

- **Mere præcis Spiller nu-info.** Evermusic fanger afspillerens tilstand under en lås, før den publiceres, så titel, forløbet tid, varighed og afspilnings-/pausetilstand aldrig kan modsige hinanden på låseskærmen eller i bilen. Buffrings- og indlæsningstilstande rapporteres nu korrekt i stedet for at vise "afspiller", mens et nummer stadig hentes.
- **Pålidelige fjernbetjeninger.** Afspil, pause, næste, forrige, spol, spring over, bland, gentag og afspilningshastighed reagerer alle ensartet fra hovedtelefonknapper, bilkontroller og låseskærmen, drevet af `MPRemoteCommandCenter`.
- **Hurtigere CarPlay-cover.** Albumcover indlæses nu flere gange hurtigere i lange lister (batch-tempo skåret fra 1,0 s til 0,25 s, med den første synlige skærm indlæst med det samme), og det vises nu i de kompakte iOS 26-CarPlay-listerækker, der tidligere ikke viste noget cover.
- **Rettelser af CarPlay-sortering og -stabilitet.** Hurtigere sortering på store biblioteker og hærdning mod kantsag-nedbrud ved rulning gennem lange lister.
- **Begrænsede metadataopdateringer.** Spiller nu- og fjernkommandoopdateringer begrænses, så hurtige ændringer ikke længere oversvømmer systemet, hvilket holder låseskærms- og CarPlay-kontroller responsive.

## Andre forbedringer

- **Liquid Glass-designforbedringer** på tværs af appen – gennemsigtige overflader, jævnere animationer og forfinede kontroller på iOS, iPadOS og macOS.
- **Nye hjemmeskærms-widgets** med forbedret opdateringslogik, der holder dem synkroniseret uden at dræne ekstra batteri.
- Rettelser til de seneste iOS-udgivelser.
- Lokaliseringsrettelser på tværs af flere sprog.
- Mange mindre forbedringer baseret på jeres e-mails og App Store-anmeldelser.

## Hvorfor denne opdatering betyder noget

Evermusic 8.7 er bygget omkring én idé: **din musik skal lyde bedst muligt, fra enhver kilde.**

1. **Hele album, som tænkt.** Ægte gapless-afspilning betyder, at livesæt, DJ-mix og konceptalbum endelig afspilles, som kunstneren masterede dem.
2. **Et studie i lommen.** Rumklang, delay, forvrængning, kompressor, crossfeed, en redesignet equalizer og loudness-normalisering giver dig reel kontrol over din lyd, ikke bare en til/fra-kontakt.
3. **Den samme oplevelse overalt.** Lokale filer, skydrev, medieservere og internetradio kører alle gennem den samme genopbyggede motor, med præcis Spiller nu og en hurtigere CarPlay ovenpå.

## Få Evermusic 8.7

[**Download Evermusic fra App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), eller opdater inde fra App Store. Evermusic er en gratis download med valgfrie opgraderinger i appen til avancerede funktioner.

Hvis du nyder appen, så efterlad gerne en bedømmelse i App Store – det hjælper virkelig. Har du feedback eller er stødt på et problem? Skriv til os på **support@everappz.com**. Vi læser hver eneste besked.

## Ofte stillede spørgsmål

{{% details title="Hvad er nyt i Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 tilføjer ægte gapless-afspilning, fem studielydeffekter (rumklang, delay, forvrængning, kompressor og crossfeed), EBU R128-volumennormalisering, en redesignet 10-bånds equalizer med brugerdefinerede forudindstillinger og import/eksport, en genopbygget AVAudioEngine-streamingmotor med forbedret formatunderstøttelse (herunder FLAC og Ogg Vorbis), hurtigere og mere præcis CarPlay og Spiller nu, Liquid Glass-designopdateringer, opfriskede hjemmeskærms-widgets samt fejl- og lokaliseringsrettelser.
{{% /details %}}

{{% details title="Har Evermusic ægte gapless-afspilning?" closed="true" %}}
Ja. Fra og med Evermusic 8.7 er afspilning ægte gapless: der er ingen pause, klik eller tik mellem numre. Motoren forbuffrer og afkoder det næste nummer, mens det aktuelle spiller, og overdrager mellem lydsamples på en sammenhængende ringbuffer, så overgangen er uhørlig. Det virker med lokale filer, skystreams og medieservere og er ideelt til livealbum, DJ-mix og konceptalbum.
{{% /details %}}

{{% details title="Hvilke lydeffekter indeholder Evermusic 8.7?" closed="true" %}}
Fem effekter i realtid: **rumklang** (13 rumforudindstillinger, wet/dry-mix), **delay/ekko** (10 forudindstillinger med delay-tid, feedback, lavpas og mix), **forvrængning** (22 karakterforudindstillinger med pre-gain og mix), **kompressor** (en fuld dynamikprocessor med tærskel, ratio, attack, release, ekspansion og makeup-gain plus 10 forudindstillinger) og **crossfeed** (Bauer bs2b-hovedtelefon-crossfeed med niveau- og cutoff-kontroller og 6 forudindstillinger). Hver effekt leveres med kuraterede forudindstillinger, og dine brugerdefinerede indstillinger huskes mellem sessioner.
{{% /details %}}

{{% details title="Hvad er crossfeed, og hvorfor skulle jeg bruge det?" closed="true" %}}
Crossfeed blander en lille, filtreret mængde af hver stereokanal ind i den anden, sådan som dine ører naturligt hører rigtige højttalere i et rum. I hovedtelefoner reducerer dette den overdrevne "inde i hovedet"-adskillelse af hårdt panorerede optagelser og gør lang lytning mere behagelig. Evermusic bruger den velkendte Bauer stereophonic-to-binaural (bs2b)-algoritme og indeholder forudindstillinger som Chu Moy og Jan Meier. Den er især effektiv på ældre stereomix fra 1960'erne og 1970'erne.
{{% /details %}}

{{% details title="Hvordan fungerer volumennormalisering i Evermusic?" closed="true" %}}
Evermusic 8.7 måler hvert nummers oplevede loudness med EBU R128-standarden (ITU-R BS.1770) i realtid og justerer blidt niveauet mod et ensartet mål, så numre ikke springer i lydstyrke. Det kræver ingen ReplayGain-tags og ændrer ikke dine filer. Fire forudindstillinger er tilgængelige – Let (−20 LUFS), Standard (−16 LUFS), Kraftig (−14 LUFS) og Nat (−23 LUFS) – og normaliseringen nulstilles rent, når du spoler eller skifter numre.
{{% /details %}}

{{% details title="Er Evermusics volumennormalisering det samme som ReplayGain?" closed="true" %}}
Den opnår samme mål – ensartet loudness mellem numre – men fungerer anderledes. ReplayGain er afhængig af loudness-tags gemt inde i dine filer. Evermusics normalisering måler loudness live med EBU R128, så den fungerer på enhver kilde, inklusive skystreams og internetradio, selv når filerne slet ingen tags har.
{{% /details %}}

{{% details title="Hvor mange bånd har Evermusics equalizer, og kan jeg lave mine egne forudindstillinger?" closed="true" %}}
Evermusics equalizer er en 10-bånds grafisk equalizer, der dækker 32 Hz til 16 kHz, med hvert bånd justerbart fra −12 dB til +12 dB i trin på 0,1 dB og en preamp fra −24 dB til +24 dB. Den indeholder indbyggede forudindstillinger, lader dig oprette og gemme brugerdefinerede forudindstillinger og understøtter import og eksport af forudindstillinger som .eqp-filer, så du kan flytte eller dele dem mellem enheder.
{{% /details %}}

{{% details title="Hvad ændrede sig i Evermusic 8.7-equalizeren?" closed="true" %}}
Equalizeren blev redesignet med nye, mere præcise skydere, der overtager iOS 26-systemskyderens og Liquid Glass-udseendet, hurtigere og mere jævnt skift af forudindstillinger og et bedre layout i liggende format og på iPad (en vandret forudindstillingslinje i stående format og en lodret forudindstillingskolonne i liggende format). Brugerdefinerede forudindstillinger og .eqp-import/eksport understøttes.
{{% /details %}}

{{% details title="Understøtter Evermusic 8.7 FLAC og Ogg Vorbis?" closed="true" %}}
Ja. Den genopbyggede motor afspiller FLAC (via Core Audio) og Ogg Vorbis (via libvorbisfile), sammen med MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF og mere, fra lokale filer, skydrev og medieservere.
{{% /details %}}

{{% details title="Hvad blev forbedret i CarPlay og på låseskærmen?" closed="true" %}}
CarPlay-albumcover indlæses flere gange hurtigere i lange lister og vises nu i de kompakte iOS 26-listerækker, der tidligere ikke viste nogen. Spiller nu-information på låseskærmen og i CarPlay er mere præcis – titel, forløbet tid, varighed og afspilnings-/pausetilstand fanges samlet, så de ikke kan modsige hinanden, og buffringstilstande rapporteres korrekt. Fjernbetjeninger (afspil, pause, næste, forrige, spol, bland, gentag, hastighed) reagerer pålideligt fra hovedtelefoner og bilen, og CarPlay-sortering på store biblioteker er hurtigere.
{{% /details %}}

{{% details title="Fungerer lydeffekterne og equalizeren med skystreaming og CarPlay?" closed="true" %}}
Ja. Effekterne, equalizeren og volumennormaliseringen kører native inde i afspilningsmotoren, så de anvendes på alt, Evermusic afspiller – lokale filer, skydrev, medieservere og internetradio – og de bliver ved med at fungere under CarPlay-afspilning og, hvor det understøttes, over AirPlay og Chromecast.
{{% /details %}}

{{% details title="Er Evermusic 8.7 gratis at opdatere, og hvilke enheder understøtter den?" closed="true" %}}
Ja. Evermusic er en gratis download fra App Store, og 8.7 er en gratis opdatering for eksisterende brugere, med valgfrie opgraderinger i appen til avancerede funktioner. Den kører på iPhone, iPad og Mac. CarPlay kræver et CarPlay-kompatibelt køretøj eller en head unit.
{{% /details %}}
