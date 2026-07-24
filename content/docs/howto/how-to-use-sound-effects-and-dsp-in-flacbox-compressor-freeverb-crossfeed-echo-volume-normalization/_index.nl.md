---
title: "Geluidseffecten en DSP gebruiken in Flacbox: Compressor, Freeverb, Crossfeed, Echo, Volumenormalisatie en meer (elke preset en instelling uitgelegd)"
date: 2026-07-24
description: "De complete gids voor Flacbox-audio op iPhone, iPad en Mac. Ontdek hoe de BASS-engine werkt, welke extra formaten hij afspeelt (waaronder MOD- en trackermuziek en DSD), en precies wat elk effect, elke schuifregelaar en elke preset met je geluid doet, plus de 10-bands equalizer en de aangepaste DSP-keten."
keywords: ["Flacbox audio-effecten", "Flacbox presets uitgelegd", "Flacbox BASS-engine", "BASS audiobibliotheek iOS", "MOD-muziekspeler iPhone", "trackermuziekspeler iOS", "MOD XM IT S3M afspelen iPhone", "DSD-speler iOS", "FLAC-speler iPhone", "lossless muziekspeler iOS", "Flacbox equalizer presets", "10-bands equalizer iPhone", "volumenormalisatie iPhone", "EBU R128 iOS", "loudness-normalisatie muziekspeler", "crossfeed koptelefoon iOS", "bs2b crossfeed", "compressor presets muziekspeler", "freeverb reverb iOS", "echo delay muziekspeler", "DSP-keten muziekspeler", "bass boost iPhone", "effecten toevoegen aan muziek Flacbox", "beste equalizer-instellingen iPhone"]
tags: ["Flacbox", "Audio-effecten", "Handleiding", "BASS", "Equalizer", "Bass Boost", "Compressor", "Freeverb", "Crossfeed", "Echo", "Volumenormalisatie", "EBU R128", "MOD-muziek", "Trackermuziek", "DSD", "FLAC", "DSP", "Koptelefoon", "Presets"]
readingTime: 30
---

{{< author-byline >}}

**Kort antwoord:** In Flacbox kies je één **Afspeelengine** in **Instellingen > Audiospeler**: **Standard** (de systeemengine van Apple), **Universal** (de FFmpeg-engine), of **Sound FX** (de **BASS™-engine**). De engine die je kiest bepaalt welke bestandsformaten worden afgespeeld, dus de keuze doet ertoe. De **Sound FX**-engine speelt extra formaten af die de meeste iPhone-apps overslaan (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, en oude **MOD- en trackermuziek** zoals MOD, XM, IT en S3M), en het is de enige engine die de geluidstools aandrijft: een **10-bands equalizer**, **Volumenormalisatie**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed**, en een zelf te bouwen **DSP-keten**. Om de effecten uit deze gids te gebruiken, zet je je Afspeelengine dus eerst op **Sound FX**. Elke tool heeft kant-en-klare **presets**. Open ze in **Instellingen > Audiospeler** (Audio-effecten, Audio-equalizer, Signaalverwerking), of tik op de **⋯ (Meer)**-knop in de speler en kies **Audio-effecten**. Niets wat je hier doet verandert ooit je bestanden.

> De uitleg over de schuifregelaars en presets hieronder bevat dezelfde korte beschrijvingen die Flacbox je in de app toont, aangevuld met wat extra achtergrond zodat je het volledige beeld hebt voordat je tikt.

## Hoe je deze gids leest

Elke tool werkt op dezelfde manier:

1. **Zet hem aan.** Elk effect heeft zijn eigen aan/uit-schakelaar. Ze staan in het begin allemaal uit. Je kunt er zoveel tegelijk aanzetten als je wilt.
2. **Kies een preset.** Een preset is een kant-en-klare instelling. Tik erop en het geluid verandert meteen. Deze gids beschrijft wat **elke** preset doet.
3. **Fijnafstemmen (optioneel).** Open de schuifregelaars om met de hand bij te stellen. Zodra je een schuifregelaar verplaatst, toont het effect **Manual**, zodat je weet dat je de preset hebt verlaten. Elke schuifregelaar heeft een resetknop.

Er wordt niets in je bestanden opgeslagen. Dit zijn live effecten. Zet een effect uit en je oorspronkelijke geluid komt meteen terug.

## Kies je Afspeelengine (Sound FX heeft de effecten)

Flacbox mengt engines niet met elkaar. Je kiest er **één** in **Instellingen > Audiospeler > Afspeelengine**, en de engine die je kiest bepaalt welke bestandsformaten je kunt afspelen en of de effecten beschikbaar zijn. Er zijn drie keuzes, weergegeven in de app onder deze exacte namen:

1. **Standard.** De ingebouwde systeemengine van Apple. Gebruikt hardwaredecodering voor een lager batterijverbruik.
2. **Universal.** De FFmpeg-engine, die een zeer breed scala aan formaten opent.
3. **Sound FX.** De **BASS™-engine**. Hij speelt lossless en high-resolution bestanden met volledige nauwkeurigheid af, voegt module- (tracker-)muziek toe, en drijft elk effect, de 10-bands equalizer en de DSP-keten in deze gids aan.

Omdat elke engine zijn eigen set formaten ondersteunt, veranderen de bestanden die je kunt afspelen met de engine die je selecteert. Nog belangrijker: de effecten, equalizer en DSP-keten werken **alleen** met de **Sound FX**-engine, dus kies die eerst als je ze wilt gebruiken.

Sound FX is gebouwd op **BASS™**, een professionele audiobibliotheek van Un4seen Developments. Je kunt er meer over lezen op de homepage op [un4seen.com](https://www.un4seen.com/).

## Muziekformaten: wat de Sound FX (BASS™)-engine toevoegt (waaronder MOD- en trackermuziek)

Met de **Sound FX (BASS™)**-engine geselecteerd speelt Flacbox de gespecialiseerde formaten hieronder af, bovenop de alledaagse. Het meest bijzondere is **modulemuziek**, ook wel **trackermuziek** genoemd. Een modulebestand is geen normale opname. Het bevat kleine instrumentgeluiden plus een 'partituur' die aangeeft hoe ze gespeeld moeten worden, en Flacbox bouwt het nummer live opnieuw op vanuit die partituur, zoals deze bestanden bedoeld waren om afgespeeld te worden. Normale spelers kunnen dit niet.

| Soort muziek | Formaten | Goed om te weten |
|---|---|---|
| **Module- / trackermuziek** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Live opnieuw opgebouwd door de BASS™-modulespeler. Geweldig voor chiptunes en oude demoscene- of Amiga-nummers. |
| **Modern lossless** | FLAC | Volledige kwaliteit, kleiner dan WAV. |
| **Overig lossless** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Minder gangbare lossless-typen, allemaal ondersteund. |
| **High-resolution DSD** | DSF, DFF | Speelt af op normale hardware met DSD over PCM. |
| **Modern lossy** | Opus, Ogg Vorbis, MP3 | De gebruikelijke streaming- en downloadtypen. |

De Sound FX-engine speelt ook de gangbare Apple-formaten af (AAC, ALAC, M4A, WAV, AIFF) en live streams, dus de effecten en equalizer werken ook daarop.

**Waarom dit je helpt:** als je een mix hebt van FLAC-albums, DSD high-resolution bestanden en een map met oude MOD- of XM-trackernummers, speelt Flacbox ze allemaal af, en werken de equalizer en effecten op elk daarvan.

## De drie menu's die je gaat gebruiken

Flacbox houdt zijn geluidstools op drie plekken, allemaal in de instellingen van de audiospeler. Zorg er eerst voor dat je **Afspeelengine** op **Sound FX** staat (Instellingen > Audiospeler > Afspeelengine), want de effecten, equalizer en DSP-keten zijn alleen met die engine beschikbaar.

- **Audio-effecten** (de effectenrack): open de speler, tik op **⋯ (Meer)**, tik op **Audio-effecten**. Of ga naar **Instellingen > Audiospeler > Audio-effecten**.
- **Audio-equalizer** (10 banden en presets): **Instellingen > Audiospeler > Audio-equalizer**.
- **Signaalverwerking** (je eigen DSP-keten): **Instellingen > Audiospeler > Signaalverwerking**.

Je kunt ook de **uitvoer-samplerate**, **kanalen** en **buffergrootte** instellen onder **Instellingen > Audiospeler**.

## De 10-bands equalizer

**Wat het doet:** Verandert de klankkleur van de muziek, van diepe bas tot heldere hoge tonen. Dit is de beste tool voor een schone **bass boost** of een helderder, duidelijker hoog. Zie het als tien volumeknoppen, elk voor een ander stukje van het geluid. Verhoog een band om dat deel naar voren te brengen, verlaag hem om het terug te trekken. Kleine wijzigingen van een paar dB klinken meestal het beste, en het werkt op alles wat je afspeelt.

**Hoe het werkt:** Tien schuifregelaars op **32, 64, 125, 250, 500 Hz en 1, 2, 4, 8, 16 kHz**. Elk gaat van **-12 dB (verlaging)** tot **+12 dB (verhoging)**. Er is ook een **Voorversterker** van **-24 tot +24 dB** voor het algehele niveau. Je kunt je eigen presets opslaan en ze **exporteren of importeren** tussen apparaten.

**Wat elke ingebouwde preset doet (22 presets):**

| Preset | Wat het met je geluid doet |
|---|---|
| **Flat** | Geen verandering. Alle banden op nul. Een schoon vertrekpunt. |
| **Acoustic** | Warme bas en heldere, aanwezige hoge tonen. Laat akoestische gitaren en stemmen natuurlijk en levendig klinken. |
| **Bass Booster** | Sterke verhoging in het laag, midden en hoog onaangeroerd. Meer punch en gewicht. |
| **Bass Reducer** | Verlaagt het laag. Handig voor galmende ruimtes, goedkope oordopjes of zware nummers. |
| **Treble Booster** | Verhoogt alleen het hoog. Voegt sprankeling en lucht toe, meer detail. |
| **Treble Reducer** | Verzacht het hoog. Temt schelle of scherpe opnames. |
| **Classical** | Vol laag en zacht hoog met een lichte middendip. Soepel en ruimtelijk voor orkestmuziek. |
| **Dance** | Groot laag en helder hoog met uitgeholde middentonen. Punchy en energiek voor clubnummers. |
| **Deep** | Warm, dik laag met zachter hoog. Een behaaglijk, ontspannen geluid. |
| **Electronic** | Sterke bas en helder hoog voor synths en beats. Breed en modern. |
| **Hip-Hop** | Zware bas en helder hoog met beheerste middentonen. Zwaar en punchy. |
| **Jazz** | Warm en soepel, met een kleine middendip. Gemakkelijk en natuurlijk voor akoestische jazz. |
| **Latin** | Verhoogd laag en hoog met schone middentonen. Helder en levendig. |
| **Loudness** | Verhoogt bas en hoog sterk (een 'smile'-curve). Klinkt voller op laag volume. |
| **Lounge** | Naar voren gebrachte middentonen met zachte randen. Ontspannen en stemvriendelijk. |
| **Piano** | Heldere middentonen en hoog zodat pianonoten schoon doorklinken. |
| **Pop** | Verhoogde middentonen voor zang, met laag en hoog teruggetrokken. Stemmen staan vooraan. |
| **R&B** | Zeer sterke laag-mid-warmte en helder hoog. Soepel en rijk. |
| **Rock** | Verhoogd laag en hoog voor gitaren en drums. Energiek en vol. |
| **Small Speakers** | Verhoogt het laag en snijdt het hoog om kleine luidsprekers voller te laten klinken. |
| **Spoken Word** | Verhoogt het stembereik en snijdt de diepe bas weg. Maakt spraak helder. |
| **Vocal Booster** | Duwt het midden waar stemmen zitten omhoog, snijdt eromheen. Zang springt eruit. |

**Tip voor bas:** Begin met **Bass Booster**, en als het modderig klinkt, trek dan de Voorversterker 1 tot 2 dB omlaag zodat er niets vervormt.

## Volumenormalisatie (gelijkmatig volume)

**Wat het doet:** Sommige nummers spelen luider af dan andere, dus je blijft het volume aanpassen. Dit zorgt ervoor dat elk nummer vanzelf ongeveer even hard speelt, zodat jij dat niet hoeft te doen. Het is perfect voor shuffle-afspeellijsten die oude en nieuwe opnames, verschillende albums of verschillende bronnen door elkaar mengen, waarbij het ene nummer veel luider kan zijn dan het volgende.

**Hoe het werkt:** Het luistert naar de werkelijke luidheid van elk nummer met de **EBU R128**-standaard (gemeten in **LUFS**, hetzelfde idee dat streamingdiensten gebruiken), en past elk nummer aan naar jouw doel. Het heeft geen tags in je bestanden nodig en verandert de audio nooit. EBU R128 meet de luidheid die je oren daadwerkelijk ervaren over het hele nummer, niet alleen de hoogste piek, en daarom komt het overeen met hoe luid nummers echt lijken. Flacbox berekent dit live terwijl de muziek speelt (en controleert de luidheid van tevoren wanneer het kan), en past dan een enkele, gelijkmatige volumeverandering op het nummer toe. De **Max boost**-limiet voorkomt dat zeer stille opnames zo hard omhoog worden geduwd dat ze vervormen. Omdat het het geluid zelf leest, werkt het op elke bron, waaronder cloudbestanden, live streams en modulemuziek, zelfs wanneer de bestanden helemaal geen luidheidstags hebben.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Target loudness** | Stelt de luidheid in waar elk nummer naartoe wordt genivelleerd. Hogere waarden laten alles over het geheel luider spelen. | -30 tot -6 LUFS (-16) |
| **Max boost** | Beperkt hoeveel stille nummers versterkt kunnen worden. Hogere waarden brengen zachte opnames dichter bij het doel. | 0 tot 24 dB (12) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Light** | Zachte nivellering voor ontspannen luisteren. Egaliseert duidelijke volumesprongen zonder stille nummers hard omhoog te duwen. |
| **Standard** | De veelzijdige standaard. Een streaming-achtig luidheidsdoel dat bij de meeste muziek past. Begin hier. |
| **Strong** | Agressieve afstemming die stille nummers stevig omhoog duwt. Het beste voor gemengde bibliotheken met grote niveauverschillen. |
| **Night** | Een over het geheel stiller doel dat toch zachte passages optilt, zodat laatavondluisteren consistent en laag blijft. |

## Compressor (egaliseer luide en zachte delen)

**Wat het doet:** In één nummer kunnen de zachte delen te zacht zijn en de luide delen te hard. Dit brengt ze dichter bij elkaar, zodat het hele nummer goed te horen is, zelfs in de auto of op een luidruchtige plek. Het draait de luidste momenten voorzichtig omlaag en tilt de zachtere op, zodat je tijdens één nummer niet meer naar het volume grijpt. Dit is anders dan Volumenormalisatie: de Compressor egaliseert dingen **binnen** één nummer, terwijl Volumenormalisatie de luidheid **tussen** nummers afstemt. Die twee werken goed samen. Begin met een preset, en open de schuifregelaars alleen als je meer controle wilt.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Threshold** | Het niveau waar compressie begint. Lagere waarden pletten meer van het geluid en houden zachte en luide delen dichter bij elkaar. | -60 tot 0 dB (-20) |
| **Ratio** | Hoe sterk de luide delen worden ingehouden zodra ze de drempel passeren. Hogere waarden comprimeren harder en houden het geluid gelijkmatiger. | 1:1 tot 30:1 (4:1) |
| **Attack** | Hoe snel het effect reageert op een plotselinge luide piek. Korte waarden vangen transiënten; langere laten ze door. | 0,1 tot 1000 ms (10 ms) |
| **Release** | Hoe snel het effect loslaat nadat het luide deel voorbij is. Korte waarden kunnen pompen; langere klinken soepeler. | 10 ms tot 5 s (100 ms) |
| **Master gain** | Uiteindelijke uitvoerversterking die na de verwerking wordt toegepast. Verhoog dit om de algehele luidheid op te tillen zodra de dynamiek is geëgaliseerd. | -30 tot +30 dB (0) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Transparent** | Nauwelijks merkbaar vangnet. Behoudt de dynamiek vrijwel volledig en vangt alleen de luidste pieken. |
| **Soft** | Lichte nivellering voor hifi-luisteren thuis. Subtiele afvlakking zonder de muziek te pletten. |
| **Standard** | Verstandige standaard voor alledaags muziek afspelen. De eerste preset om te proberen. |
| **Heavy** | Agressieve egalisatie voor luidruchtige omgevingen. Auto, drukke ruimte, luisteren op laag volume. |
| **Voice / Podcast** | Op spraak afgestemd. Een tragere attack laat sisklanken door, ruime makeup gain trekt stemmen omhoog. |
| **Old Recordings** | Vintage albums en gerestaureerd vinyl, waar het gemiddelde niveau onder moderne releases ligt. |
| **Late Night** | Zware compressie plus grote verhoging voor stil luisteren wanneer buren of slapende familie ertoe doen. |
| **Movie Dialog** | Brengt gesproken woord op tegen muziek en geluidseffecten in een gevarieerde soundtrack. |
| **Streaming Match** | Richt zich ongeveer op de luidheidsnormalisatie van moderne streamingdiensten rond -14 LUFS. |
| **Maximum Loudness** | Alles erop en eraan. Raakt de limiter; verwacht een geplet, zeer egaal signaal. De letterlijke maximaal-volume-preset. |

## Freeverb (reverb, een gevoel van ruimte)

**Wat het doet:** Voegt een gevoel van ruimte aan de muziek toe, van een kleine kamer tot een grote zaal. Kies een preset, of stem de dry- en wet-mix, ruimtegrootte, demping en breedte zelf af. Reverb is de natuurlijke echo die je in elke echte ruimte hoort, en Freeverb bootst die na in software. Een beetje laat vlakke of van dichtbij opgenomen opnames opener en levendiger aanvoelen. Veel plaatst de muziek in een grote, verre ruimte. Het is een creatief effect, dus houd de wet-mix bescheiden voor natuurlijke resultaten.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Dry mix** | Hoeveel van het oorspronkelijke, onaangeroerde geluid behouden blijft. Hogere waarden laten meer van het droge signaal in de mix. | 0 tot 1 (0.0) |
| **Wet mix** | Hoeveel van het nagalmde geluid wordt toegevoegd. Hogere waarden maken de reverb luider en duidelijker. | 0 tot 3 (1.0) |
| **Room size** | De grootte van de ingebeelde ruimte. Hogere waarden geven een langere, grotere reverb-staart, van een kleine kamer tot een kathedraal. | 0 tot 1 (0.5) |
| **Damp** | Hoe snel de hoge frequenties in de staart wegvallen. Hogere waarden maken de reverb donkerder en warmer. | 0 tot 1 (0.5) |
| **Width** | De stereospreiding van de reverb. Hogere waarden laten de ruimte breder aanvoelen tussen het linker- en rechterkanaal. | 0 tot 1 (1.0) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Room** | Een kleine, strakke ruimte. Subtiele ambiance die een gevoel van plek toevoegt zonder het geluid weg te spoelen. |
| **Studio** | Een droge, gecontroleerde opnameruimte. Net genoeg reflectie om natuurlijk te klinken. |
| **Hall** | Een grote concertzaal. Een lange, weelderige staart die bij orkest- en akoestische muziek past. |
| **Cathedral** | Een enorme, galmende stenen ruimte. De langste, meest dramatische reverb-staart. |
| **Plate** | Een heldere, dichte studioplaatreverb. Klassiek voor zang en drums. |
| **Ambience** | Een korte, luchtige ambiance. Voegt een licht gevoel van ruimte toe terwijl het grotendeels droog blijft. |

## Auto Wah (funky filtersweep)

**Wat het doet:** Een filter dat vanzelf op en neer sweept voor een funky, stemachtig wah-geluid. Kies een preset, of stel de wet-mix, feedback, snelheid, bereik en frequentie zelf in. Het is dezelfde 'wah'-sweep die een gitaar-wahpedaal maakt, maar hier beweegt hij vanzelf in de maat van de muziek. Het klinkt geweldig op funk, disco en elektronische nummers. Het is een gedurfd, opvallend effect, dus een beetje gaat een heel eind bij alledaags luisteren.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Wet mix** | Hoe sterk het wah-effect in de mix is. Hogere waarden maken het sweepende filter duidelijker. | -2 tot +2 (1.5) |
| **Feedback** | Hoeveel van de uitvoer terug in het effect wordt gevoerd. Hogere waarden maken de wah resonanter en uitgesprokener. | -1 tot +1 (0.5) |
| **Rate** | Hoe snel het filter op en neer sweept. Hogere waarden geven een snellere, ritmischere wah. | 0,1 tot 9 Hz (2.0) |
| **Range** | Hoe ver het filter sweept, in octaven. Hogere waarden geven een bredere, dramatischere sweep. | 0,1 tot 9 octaven (4.3) |
| **Frequency** | De basisfrequentie waaromheen het filter sweept. Lagere waarden klinken dieper; hogere waarden klinken helderder. | 1 tot 1000 Hz (50) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Classic** | Een gebalanceerde, klassieke wah-sweep. Een goed vertrekpunt voor funk en rock. |
| **Slow** | Een trage, brede sweep die zachtjes op en neer drijft. Geweldig voor pads en lange noten. |
| **Funky** | Een snelle, punchy sweep met veel beweging. Voegt ritmische bite toe aan gitaren en synths. |
| **Deep** | Een diepe, brede sweep die vanaf een lage frequentie begint. Groot en dramatisch. |
| **Subtle** | Een zachte, ingetogen beweging. Voegt karakter toe zonder het geluid te overheersen. |
| **Resonant** | Een scherpe, resonante wah met hoge feedback. Stemachtig en expressief. |

## Phaser (wervelende woosh)

**Wat het doet:** Een sweepend filter dat een wervelende, woeshende beweging aan het geluid toevoegt. Kies een preset, of stel de feedback, snelheid, bereik en frequentie zelf in. Het voegt zachte beweging en glinstering toe zonder de noten te veranderen. Het is subtiel op zang en pads, en dramatisch op synths en gitaren. Probeer Slow voor een dromerig gevoel of Jet voor een sterke werveling.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Feedback** | Hoeveel van de uitvoer terug in het effect wordt gevoerd. Hogere waarden maken de phaser resonanter en uitgesprokener. | -1 tot +1 (0.0) |
| **Rate** | Hoe snel het filter op en neer sweept. Hogere waarden geven een snellere, ritmischere phasing. | 0,1 tot 9 Hz (1.0) |
| **Range** | Hoe ver het filter sweept, in octaven. Hogere waarden geven een bredere, dramatischere sweep. | 0,1 tot 9 octaven (4.0) |
| **Frequency** | De basisfrequentie waaromheen het filter sweept. Lagere waarden klinken dieper; hogere waarden klinken helderder. | 1 tot 1000 Hz (100) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Classic** | Een gebalanceerde, klassieke phaser-sweep. Een goed vertrekpunt voor gitaren en toetsen. |
| **Slow** | Een trage, brede sweep die zachtjes op en neer drijft. Geweldig voor pads en lange noten. |
| **Fast** | Een snelle, glinsterende sweep met veel beweging. Voegt beweging en energie toe. |
| **Deep** | Een diepe, brede sweep die vanaf een lage frequentie begint. Groot en dramatisch. |
| **Subtle** | Een zachte, ingetogen beweging. Voegt karakter toe zonder het geluid te overheersen. |
| **Jet** | Een intense, resonante sweep met hoge feedback, de klassieke straaljager-woosh. |

## Flanger (straaljager-sweep)

**Wat het doet:** Een korte, bewegende delay die het geluid een straaljager-achtige, sweepende woosh geeft. Kies een preset, of stel de diepte, feedback, snelheid en delay zelf in. Het is een sterkere, metaligere neef van de phaser, beroemd om de woeshende sweep in klassieke rock en elektronische muziek. Subtiele instellingen voegen zachte beweging toe, terwijl diepe instellingen dramatisch en opvallend zijn. Het beste spaarzaam te gebruiken, voor effect.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Depth** | Hoe sterk het sweepende effect is. Hogere waarden maken de flanging duidelijker. | 0 tot 100% (25) |
| **Feedback** | Hoeveel van de uitvoer terug in het effect wordt gevoerd. Hogere waarden maken de flanger resonanter en metaliger. | -99 tot +99% (-50) |
| **Rate** | Hoe snel de sweep op en neer beweegt. Hogere waarden geven een snellere, glinsterendere beweging. | 0 tot 10 Hz (0.25) |
| **Delay** | De basisdelaytijd waarop de sweep is gebouwd. Hogere waarden geven een dieper, holler karakter. | 0 tot 4 ms (2.0) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Classic** | Een gebalanceerde, klassieke flanger. Een goed vertrekpunt voor gitaren en toetsen. |
| **Subtle** | Een zachte, ingetogen sweep. Voegt beweging toe zonder het geluid te overheersen. |
| **Deep** | Een diepe, zware sweep met sterke feedback. Groot en dramatisch. |
| **Jet** | Een intense sweep met positieve feedback, de klassieke straaljager-woosh. |
| **Fast** | Een snelle, glinsterende sweep met veel beweging en energie. |
| **Wide** | Een trage, brede sweep met een lange delay. Weelderig en ruimtelijk. |

## Echo (herhalingen)

**Wat het doet:** Herhaalt het geluid als wegstervende echo's voor een gevoel van ruimte en diepte. Kies een preset, of stel de wet-mix, feedback en delay zelf in. Het is als roepen in een kloof: het geluid komt een of meer keer terug na een korte pauze. Een enkele korte herhaling voegt body en een retro-gevoel toe, terwijl langere herhalingen met meer feedback ruimtelijke, nagalmende staarten creëren. De Ping Pong-preset laat de herhalingen tussen je linker- en rechteroor stuiteren, wat leuk is op een koptelefoon. Houd de wet-mix bescheiden zodat de echo's de muziek ondersteunen in plaats van overstemmen.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Wet mix** | Hoe luid de echo's zijn vergeleken met het oorspronkelijke geluid. Hogere waarden laten de herhalingen meer opvallen. | -2 tot +2 (0.6) |
| **Feedback** | Hoe vaak de echo herhaalt. Hogere waarden geven meer herhalingen die er langer over doen om weg te sterven. | -1 tot +1 (0.5) |
| **Delay** | De tijd tussen echo's. Kortere waarden geven een strakke slap-back; langere waarden geven uit elkaar geplaatste herhalingen. | 0,01 tot 2 s (0.4) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Slapback** | Een enkele, strakke herhaling vlak achter het geluid. Klassieke rockabilly slap-back. |
| **Room** | Een korte, natuurlijke echo, als een kleine kamer. Voegt ruimte toe zonder het geluid uit te smeren. |
| **Tape** | Warme, middellange herhalingen die geleidelijk wegvallen, als een oude tape-delay. |
| **Dub** | Lange, zware herhalingen met sterke feedback. Groot, dubby en ruimtelijk. |
| **Ping Pong** | Echo's stuiteren tussen de linker- en rechterluidspreker voor een breed stereo-effect. |
| **Long** | Trage, ver uit elkaar geplaatste herhalingen die ver achter het geluid wegstervend uitlopen. |

## Chorus (dikker, breder geluid)

**Wat het doet:** Verdikt en verbreedt het geluid door een verschuivende kopie over het origineel te leggen. Kies een preset, of stel de wet/dry-mix, diepte, snelheid en feedback zelf in. Het laat één instrument of stem klinken als meerdere die samen spelen, door licht ontstemde, bewegende kopieën toe te voegen. Dit voegt rijkdom en een zachte glinstering toe. Subtiele instellingen verwarmen dingen op, terwijl sterke instellingen weelderig en dromerig klinken. Het is populair op gitaren, toetsen en zang.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Wet/Dry** | Hoeveel van de chorus je hoort vergeleken met het oorspronkelijke geluid. Hogere waarden maken het effect duidelijker. | 0 tot 100% (50) |
| **Depth** | Hoe ver de toonhoogte op en neer schommelt. Hogere waarden geven een dikker, glinsterender geluid. | 0 tot 100% (25) |
| **Rate** | Hoe snel de glinstering beweegt. Tragere snelheden klinken zacht en weelderig; snellere snelheden klinken meer als vibrato. | 0 tot 10 Hz (1.1) |
| **Feedback** | Hoeveel van het effect terug in zichzelf wordt gevoerd. Hogere waarden maken de chorus resonanter en intenser. | -99 tot +99% (25) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Subtle** | Een zachte verdikking die warmte toevoegt zonder de aandacht op zichzelf te vestigen. |
| **Lush** | Een rijke, klassieke chorus. Een geweldige allround-instelling voor gitaren en toetsen. |
| **Ensemble** | Een volle, gelaagde glinstering die één instrument als meerdere laat klinken. |
| **Vibrato** | Volledig wet met een snelle rate, voor een schommelende vibrato in plaats van een subtiele chorus. |
| **Wide** | Een trage, brede glinstering die het stereobeeld opent. Ruimtelijk en dromerig. |
| **Twelve-String** | Een heldere, resonante glinstering die doet denken aan een twaalfsnarige gitaar. |

## Distortion (grit en scherpte)

**Wat het doet:** Voegt grit en scherpte toe door het geluid te oversturen. Kies een preset, of stel de drive, uitvoer en toon zelf in. Het verruwt het geluid opzettelijk, van een warme, gruizige rand tot een gebroken, fuzzy toon. Het is een creatief, plezierig effect in plaats van een manier om de kwaliteit te verbeteren, dus gebruik het in kleine hoeveelheden. Het is leuk op elektronische, rock- en experimentele nummers. Verlaag de Output als een zware preset te luid wordt.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Drive** | Hoe hard het geluid wordt vervormd. Hogere waarden zijn gruiziger en agressiever. | 0 tot 100% (15) |
| **Output** | Het uitvoerniveau na vervorming. Verlaag het als een zware instelling te luid wordt. | -60 tot 0 dB (-18) |
| **Tone** | Rolt het hoog af vóór de vervorming. Lagere waarden klinken donkerder en warmer. | 100 tot 8000 Hz (8000) |
| **Center** | Rond welke frequentie de vervorming is gericht. Verschuift het karakter helderder of donkerder. | 100 tot 8000 Hz (2400) |
| **Width** | Hoe breed die focus is. Smal klinkt scherp en nasaal; breed klinkt vol en open. | 100 tot 8000 Hz (2400) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Warm Drive** | Een lichte, warme grit die scherpte toevoegt zonder het karakter veel te veranderen. |
| **Crunch** | Een klassieke crunchy overdrive, punchy en ritmisch. |
| **Overdrive** | Een heldere, gedreven toon met veel bite. Geweldig voor leadgeluiden. |
| **Fuzz** | Een dikke, verzadigde fuzz. Zwaar en vol harmonischen. |
| **Metal** | Een strakke, mid-gerichte high-gain toon voor agressieve, zware geluiden. |
| **Screamer** | Een mid-verhoogde overdrive die doorsnijdt, als een tube screamer. |
| **LoFi** | Een geplette, smalbandige vervorming voor een gruizig lo-fi karakter. |

## Rotate (draaiende stereo)

**Wat het doet:** Draait het geluid rond het stereoveld voor een draaiend, wervelend effect. Kies een preset, of stel de snelheid zelf in. Het beweegt het geluid langzaam rond je linker- en rechterkanaal, een beetje als een draaiende luidspreker, wat een wervelend, hypnotiserend gevoel toevoegt. Trage instellingen zijn zacht en breed, terwijl snelle instellingen duizelig en opvallend zijn. Het is een stereo-effect, dus het is het meest merkbaar op een koptelefoon of goed geplaatste luidsprekers.

**Schuifregelaar:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Rate** | Hoe snel het geluid rond het stereoveld draait. Negatieve waarden draaien de andere kant op; nul houdt het stil. | -5 tot +5 Hz (1.0) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Slow Pan** | Een trage, zachte drift van links naar rechts. Subtiel en breed. |
| **Sway** | Een gestage links-rechts wieging. Voegt zachte beweging toe aan het stereobeeld. |
| **Rotary** | Een gemiddelde draai die doet denken aan een draaiende luidspreker. |
| **Fast Spin** | Een snelle draai rond het stereoveld voor een duizelig, wervelend effect. |
| **Reverse** | Een gemiddelde draai in de tegenovergestelde richting. |
| **Whirl** | Een zeer snelle werveling. Intens en desoriënterend. |

## Crossfeed (natuurlijk geluid op een koptelefoon)

Bij luidsprekers hoort elk van je oren zowel de linker- als de rechterluidspreker, alleen op iets verschillende tijden en volumes. Bij een koptelefoon is die natuurlijke vermenging weg: je linkeroor hoort alleen het linkerkanaal en je rechteroor alleen het rechter. Deze 'superstereo' kan muziek laten aanvoelen alsof die in je hoofd is gesplitst, en hard-gepande opnames, waarbij een instrument volledig aan één kant zit, kunnen onnatuurlijk of vermoeiend aanvoelen bij langdurig luisteren.

Crossfeed lost dit op door een kleine, gefilterde hoeveelheid van elk kanaal in het andere te mengen, met een minieme vertraging en een zachte afrol van de hoge frequenties. Dat komt dicht bij hoe geluid van echte luidsprekers beide oren bereikt, inclusief de manier waarop je hoofd het verre oor licht afschermt. Het resultaat is een natuurlijker, luidspreker-achtig beeld dat iets vóór je zit in plaats van in je hoofd, en het vermindert luistermoeheid bij lange sessies. Flacbox gebruikt de bekende **bs2b (Bauer stereophonic-to-binaural)**-methode, een gerespecteerde open-source crossfeed die door veel audiofiele spelers wordt gebruikt. Je kunt over het algoritme lezen op de [bs2b projectpagina](https://bs2b.sourceforge.net/).

De **Cutoff** bepaalt hoe warm de vermenging klinkt, en het **Feed level** bepaalt hoe sterk die is. De presets dekken de klassieke bs2b-niveaus, van een nauwelijks merkbaar tikje tot een stevige, luidspreker-achtige vermenging. Crossfeed is een koptelefooneffect, dus laat het uit wanneer je op luidsprekers luistert.

**Schuifregelaars:**

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Cutoff** | Stelt in waar het overvloeien tussen kanalen begint af te rollen. Lagere waarden geven een warmer, uitgesprokener effect. | 300 tot 2000 Hz (700) |
| **Feed level** | Bepaalt hoeveel van het ene kanaal in het andere overvloeit. Hogere waarden produceren een meer luidspreker-achtig geluid. | 1 tot 15 dB (4.5) |

**Presets:**

| Preset | Wat het doet |
|---|---|
| **Subtle** | Nauwelijks merkbare crossfeed voor ontspannen luisteren. Verzacht hard-gepande stereo zonder de klankbalans te veranderen. |
| **Chu Moy** | De klassieke veelzijdige standaard. Gebalanceerd en licht warm, werkt op vrijwel elk materiaal. Begin hier. |
| **Strong** | Sterkere overvloeiing voor harder gepande mixen. Duidelijkere stereoversmalling. |
| **Jan Meier** | Populair onder koptelefoonliefhebbers. Bredere feed, meer luidspreker-achtige weergave, lichte basverhoging. |
| **Speaker-like** | Afgestemd op de meest natuurlijke luidspreker-achtige weergave via een koptelefoon. |
| **Vintage Stereo** | Agressieve crossfeed afgestemd op mixen uit de jaren 1960 en 1970 met hard-gepande drums en zang. |

## Signaalverwerking: bouw je eigen DSP-keten

Naast de kant-en-klare effecten laat Flacbox je je eigen keten bouwen in **Instellingen > Audiospeler > Signaalverwerking**. Zoals de app uitlegt wanneer de keten leeg is: *«Tik op + om een effect toe te voegen. Zet elk effect aan of uit met zijn schakelaar, sleep om te herordenen, tik om de parameters te bewerken, en houd ingedrukt om te dupliceren of te verwijderen.»*

De **volgorde doet ertoe**: een filter vóór een vervorming klinkt anders dan hetzelfde filter erna. Je kunt de hele keten ook richten op **Alle kanalen**, **Linkerkanaal** of **Rechterkanaal**.

Hieronder staat elk blok, met de eigen tekst van de app voor elke schuifregelaar en elke preset.

### Gain (niveautrim)

Verhoogt of verlaagt het niveau op één punt in de keten.

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Gain** | Verhoogt of verlaagt het niveau op dit punt in de keten. Gebruik het om niveau bij te vullen na andere effecten, of om de volgende aan te sturen. | -24 tot +24 dB (0) |

| Preset | Wat het doet |
|---|---|
| **Unity** | Geen verandering in niveau. Een neutraal vertrekpunt. |
| **Cut** | Een grote verlaging. Temt een luide bron, of maakt ruimte vóór de effecten die volgen. |
| **Trim** | Een zachte verlaging om het niveau een beetje terug te trekken. |
| **Lift** | Een bescheiden verhoging om een stille bron omhoog te brengen. |
| **Boost** | Een sterke verhoging voor stil materiaal, of om de volgende effecten harder aan te sturen. |
| **Max** | Maximale verhoging. Luid, let op clipping later in de keten. |

### Low Pass (verwijdert hoog)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Cutoff** | Stelt in waar het filter het hoog begint af te rollen. Verlaag het om het geluid donkerder en zachter te maken; verhoog het richting de top om volledig te openen. | 20 Hz tot 20 kHz (20 kHz) |
| **Resonance** | Benadrukt de frequenties precies bij de cutoff. Houd het laag voor een schone afrol; verhoog het voor een piekerige, fluitende rand. | 0,1 tot 10 (0.707) |

| Preset | Wat het doet |
|---|---|
| **Air** | Trimt alleen het allerhoogste. Neemt een beetje scherpte weg zonder het geluid dof te maken. |
| **Warm** | Een zachte afrol van het hoog voor een warmere, rondere toon. |
| **Mellow** | Merkbaar verzacht. Trekt de helderheid terug voor een ontspannen gevoel. |
| **Muffled** | Donker en gedempt, alsof gehoord door een muur. |
| **Telephone** | Een smalle, resonante piek laag in het bereik. Een dunne, telefoonachtige stem. |

### High Pass (verwijdert laag)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Cutoff** | Stelt in waar het filter het laag begint af te rollen. Verhoog het om het laag uit te dunnen en gerommel te verwijderen; verlaag het richting de bodem om volledig te openen. | 20 Hz tot 20 kHz (20 Hz) |
| **Resonance** | Benadrukt de frequenties precies bij de cutoff. Houd het laag voor een schone afrol; verhoog het voor een piekerige, fluitende rand. | 0,1 tot 10 (0.707) |

| Preset | Wat het doet |
|---|---|
| **Rumble Cut** | Verwijdert subsonisch gerommel en DC-offset zonder het hoorbare laag aan te raken. |
| **Tighten** | Trimt galmende lage frequenties voor een strakkere, schonere bas. |
| **Thin** | Snijdt de warmte en body weg, waardoor een lichter, dunner geluid overblijft. |
| **Radio** | Alleen de middentonen en het hoog blijven, als een kleine radioluidspreker. |
| **Telephone** | Een smalle, resonante piek hoog in het bereik. Een dunne, telefoonachtige stem. |

### Band Pass (behoudt een middenband)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Center** | Stelt de frequentie in die het filter doorlaat. Alles erboven en eronder wordt afgerold. Sweep het om bas, middentonen of hoog eruit te lichten. | 20 Hz tot 20 kHz (1 kHz) |
| **Resonance** | Bepaalt hoe breed de band is. Lage waarden laten een breed bereik door; verhoog het om in te zoomen op het midden voor een scherpe, resonante toon. | 0,1 tot 10 (0.707) |

| Preset | Wat het doet |
|---|---|
| **Voice** | Een brede band rond het middenbereik waar de meeste zang zit. Een neutraal vertrekpunt. |
| **Bass** | Isoleert het laag, waardoor alleen de bas en kick overblijven. |
| **Body** | Focust op de laag-middentonen voor een warme, boxy body. |
| **Presence** | Verhoogt de boven-middentonen voor helderheid en aanwezigheid. |
| **Telephone** | Een smalle middentoonband. Een dun, telefoonachtig geluid. |
| **Wah** | Een zeer smalle, resonante piek. Sweep het midden voor een wah-effect. |

### Notch (verwijdert één smalle band)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Frequency** | Stelt de frequentie in die het filter verwijdert. Alles erboven en eronder gaat door. Stem het af op een brom of resonantie om die eruit te snijden. | 20 Hz tot 20 kHz (60 Hz) |
| **Resonance** | Bepaalt hoe breed de verlaging is. Lage waarden scheppen een breed bereik uit; verhoog het om alleen een pinpoint-band te verwijderen en de rest onaangeroerd te laten. | 0,1 tot 10 (8.0) |

| Preset | Wat het doet |
|---|---|
| **Mains Hum 60** | Verwijdert 60 Hz elektrische brom (Noord-Amerikaanse netstroom). Een neutraal vertrekpunt. |
| **Mains Hum 50** | Verwijdert 50 Hz elektrische brom (Europese en andere netstroom). |
| **Rumble** | Snijdt een laagfrequent gerommel of resonantie weg zonder het hele laag uit te dunnen. |
| **Mud** | Schept laag-mid-modder uit voor een schoner, helderder geluid. |
| **Boxy** | Verwijdert een boxy middentoon-honk. |
| **Harsh** | Temt een schelle, doordringende piek in de boven-middentonen. |

### Peaking (parametrische EQ-band)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Frequency** | Het midden van de band om te verhogen of te verlagen. Sweep het om de frequentie te vinden die je wilt vormgeven. | 20 Hz tot 20 kHz (1 kHz) |
| **Gain** | Hoeveel je in het midden verhoogt of verlaagt. Positief tilt de band op; negatief schept hem uit. | -15 tot +15 dB (0) |
| **Q factor** | Bepaalt hoe breed de band is. Lage waarden vormen een breed gebied; hoge waarden zoomen in voor chirurgische, pinpoint-wijzigingen. | 0,1 tot 10 (1.0) |

| Preset | Wat het doet |
|---|---|
| **Presence** | Een brede boven-middentoonverhoging voor helderheid en aanwezigheid. Een neutraal vertrekpunt. |
| **Warmth** | Een brede laag-middentoonverhoging die body en warmte toevoegt. |
| **Vocal Boost** | Verhoogt het kernstembereik om stemmen naar voren te brengen. |
| **Cut Mud** | Schept boxy laag-mid-modder uit voor een schoner geluid. |
| **Tame Harsh** | Een smalle verlaging om een schelle, doordringende piek te temmen. |
| **Punch** | Een lage verhoging die punch en impact aan het laag toevoegt. |
| **Sub Boost** | Een diepe verhoging helemaal onderaan voor extra sub-bas-gewicht. |
| **Air** | Een brede verhoging bovenaan voor een open, luchtige glans. |
| **Clarity** | Verhoogt de hoog-middentonen om definitie en scherpte toe te voegen. |
| **De-Ess** | Een smalle verlaging in het sisklankbereik om schelle S-klanken te temmen. |
| **De-Boom** | Snijdt een galmende laagfrequente opbouw weg voor een strakker laag. |
| **Scoop** | Een brede middentoondip voor een uitgeholde, moderne toon. |

### Low Shelf (basregeling en bass boost)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Frequency** | Stelt de hoek in waaronder de shelf van kracht wordt. Alles eronder wordt samen verhoogd of verlaagd. | 20 tot 2000 Hz (200) |
| **Gain** | Hoeveel je het laag optilt of verlaagt. Positief voegt gewicht en warmte toe; negatief dunt het uit. | -15 tot +15 dB (0) |

| Preset | Wat het doet |
|---|---|
| **Warmth** | Een zachte laag-verhoging voor warmte en body. Een neutraal vertrekpunt. |
| **Bass Boost** | Een stevige verhoging van de bas voor gewicht en punch. |
| **Fullness** | Vult de laag-middentonen op voor een voller, ronder geluid. |
| **Trim Bass** | Een bescheiden verlaging om een bas-zware mix lichter te maken. |
| **Cut Lows** | Een sterke verlaging om het laag uit te dunnen of te de-boomen. |
| **Big Bottom** | Een grote laag-verhoging voor maximaal gewicht en gerommel. |

### High Shelf (trebleregeling)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Frequency** | Stelt de hoek in waarboven de shelf van kracht wordt. Alles erboven wordt samen verhoogd of verlaagd. | 1 tot 20 kHz (8 kHz) |
| **Gain** | Hoeveel je het hoog optilt of verlaagt. Positief voegt helderheid en lucht toe; negatief verzacht en verdonkert. | -15 tot +15 dB (0) |

| Preset | Wat het doet |
|---|---|
| **Presence** | Een zachte hoog-verhoging voor helderheid en detail. Een neutraal vertrekpunt. |
| **Air** | Opent het allerhoogste voor een luchtig, open geluid. |
| **Bright** | Een sterke verhoging voor een heldere, frisse, naar voren gebrachte toon. |
| **Soften** | Een bescheiden verlaging om de scherpte van schelle hoge tonen weg te nemen. |
| **Tame Highs** | Een sterke verlaging om een te helder geluid te verdonkeren en te verzachten. |
| **Sparkle** | Een grote hoog-verhoging voor maximale glinstering en sprankeling. |

### Soft Clip (warme verzadiging)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Drive** | Duwt het signaal harder in de waveshaper. Kleine hoeveelheden voegen zachte warmte toe; grote hoeveelheden ronden de pieken af tot dikke verzadiging en grit. | 0 tot 40 dB (0) |

| Preset | Wat het doet |
|---|---|
| **Warm** | Een vleugje drive voor zachte, analoog-achtige warmte. |
| **Drive** | Merkbare verzadiging die het geluid verdikt en kleurt. |
| **Crunch** | Zware drive met een hoorbare crunchy rand. |
| **Fuzz** | Dikke, fuzzy vervorming. De pieken worden hard geplet. |
| **Destroy** | Maximale drive. Agressieve, volledig verzadigde grit. |

### Bit Crusher (retro lo-fi)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Bit depth** | Stelt in hoeveel bits elk sample beschrijven. Minder bits betekenen grovere stappen en meer kwantiseringsruis, voor een crunchy, gruizig digitaal geluid. | 1 tot 16 bits (16) |
| **Sample rate** | Downsamplet de audio. Bij honderd procent blijft de rate onaangeroerd; verlaag het om elk sample langer vast te houden, wat het hoog dof maakt en een schelle, aliased rand toevoegt. | 1% tot 100% (100%) |

| Preset | Wat het doet |
|---|---|
| **Vintage** | Een subtiele daling in kwaliteit, als een vroege digitale sampler. |
| **LoFi** | Klassiek 8-bit, half-rate lo-fi. Korrelig en retro. |
| **Crunch** | Zwaarder crushen met een hoorbare crunchy rand. |
| **Gritty** | Grof en gruizig. De stappen tussen niveaus zijn duidelijk. |
| **Destroy** | Extreme reductie. Schel, gebroken, nauwelijks herkenbaar. |

### Ring Modulator (metalige en robotachtige tonen)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Carrier** | Stelt de frequentie in van de toon waarmee het signaal wordt vermenigvuldigd. Een paar hertz geeft een tremolo-schommeling; hogere frequenties voegen metalige, bel-achtige en robotachtige boventonen toe. | 1 tot 4000 Hz (440) |
| **Mix** | Mengt het gemoduleerde geluid met het origineel. Bij nul procent hoor je alleen het droge signaal; bij honderd procent alleen de volledig gemoduleerde toon. | 0% tot 100% (0%) |

| Preset | Wat het doet |
|---|---|
| **Tremolo** | Een zeer lage carrier verandert het in een amplitude-tremolo, die het volume laat schommelen. |
| **Robot** | Een middencarrier voegt klinkende boventonen toe voor een klassiek robotstem-effect. |
| **Metallic** | Dichte, inharmonische boventonen voor een schelle, metalige toon. |
| **Bell** | Een hogere carrier geeft heldere, bel-achtige rinkeling. |
| **Alien** | Volledig wet met een hoge carrier. Extreem, buitenaards, nauwelijks herkenbaar. |

### Tremolo (volumeschommeling)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Rate** | Stelt in hoe snel het volume pulseert. Tragere snelheden geven een soepele wieging; snellere snelheden geven een snelle stotter. | 0,1 tot 20 Hz (5) |
| **Depth** | Stelt in hoeveel het volume bij elke puls daalt. Bij nul procent is het niveau constant; bij honderd procent zakt het helemaal weg tot stilte. | 0% tot 100% (0%) |

| Preset | Wat het doet |
|---|---|
| **Gentle** | Een trage, ondiepe wieging. Subtiele beweging zonder de aandacht te trekken. |
| **Classic** | De klassieke versterker-tremolo: een gemiddelde rate en gematigde diepte. |
| **Deep** | Een sterke, diepe puls die elke cyclus bijna tot stilte zakt. |
| **Fast** | Een snelle flikkering voor een glinsterend, nerveus gevoel. |
| **Chop** | Snel en volledige diepte. Een harde, stotterende chop. |

### Delay (echo)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Time** | Stelt de pauze in vóór elke echo. Korte tijden geven een strakke slapback; langere tijden plaatsen de herhalingen verder uit elkaar. | 0,01 tot 2 s (0.25) |
| **Feedback** | Stelt in hoeveel van elke echo wordt teruggevoerd. Lage waarden geven een enkele herhaling; hogere waarden bouwen een lange, nagalmende reeks echo's op. | 0 tot 0.95 (0.4) |
| **Mix** | Mengt de echo's met het origineel. Bij nul procent hoor je alleen het droge signaal; bij honderd procent alleen de echo's. | 0% tot 100% (0%) |

| Preset | Wat het doet |
|---|---|
| **Slapback** | Een enkele korte echo, strak tegen het origineel. Rockabilly en zangverdubbeling. |
| **Echo** | De klassieke echo: een heldere herhaling met een paar nagalmende staarten. |
| **Ping** | Een snelle, stuiterende herhaling die ritmische beweging toevoegt. |
| **Ambient** | Langere, zachtere herhalingen die uitwassen tot een ruimtelijke staart. |
| **Dub** | Hoge feedback voor lange, dubby cascades van echo. |
| **Cavern** | Lange, diepe herhalingen, als geluid dat door een enorme ruimte echoot. |

### Stereo Width (versmallen of verbreden)

| Regelaar | Wat het doet | Bereik (standaard) |
|---|---|---|
| **Width** | Versmalt of verbreedt het stereobeeld. Nul procent klapt in tot mono, honderd procent laat het onaangeroerd, en hogere waarden duwen de zijkanten breder. Beïnvloedt alleen stereonummers op het All-channels-doel. | 0% tot 200% (100%) |

| Preset | Wat het doet |
|---|---|
| **Wide** | Een zachte verbreding die het stereobeeld opent. Een neutraal vertrekpunt. |
| **Wider** | Een sterkere spreiding voor een groot, meeslepend stereoveld. |
| **Max** | Maximale breedte. Zeer breed, maar let op mono-compatibiliteitsproblemen. |
| **Narrow** | Trekt de zijkanten in voor een strakker, meer gecentreerd beeld. |
| **Focused** | Bijna gecentreerd, met slechts een vleugje stereo. |
| **Mono** | Volledig ingeklapt tot mono. Beide luidsprekers spelen hetzelfde signaal. |

## Hoe het allemaal onder de motorkap werkt (eenvoudige versie)

- **Engines:** je kiest er één in Instellingen > Audiospeler > Afspeelengine: **Standard** (systeem), **Universal** (FFmpeg), of **Sound FX** (de **BASS™-engine** van [Un4seen Developments](https://www.un4seen.com/)). De engine die je kiest bepaalt welke formaten afspelen, en de effecten, equalizer en DSP-keten draaien alleen in de Sound FX-engine.
- **Formaten:** de BASS™-engine voegt FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus en module- (tracker-)muziek toe bovenop de systeem- en FFmpeg-formaten.
- **Effecten:** de equalizer, compressor en de meeste effecten gebruiken de BASS™-effecten-add-ons. Freeverb is de Freeverb-reverb. Chorus, Flanger en Distortion gebruiken klassieke DirectX-achtige effecten met hun eigen regelaars.
- **Volumenormalisatie:** een live **EBU R128**-loudness-egalisator (de loudness-standaard die in broadcast en streaming wordt gebruikt).
- **Crossfeed:** de **bs2b (Bauer)**-crossfeed, draaiend binnen de BASS™-engine.
- **DSP-keten:** je aangepaste blokken, toegepast in de exacte volgorde die je instelt, op alle kanalen of slechts één kant.
- **Uitvoer:** je kunt de samplerate, het aantal kanalen en de buffergrootte instellen om bij je apparatuur te passen.

Omdat dit alles live draait terwijl de muziek speelt, doen de effecten het volgende:

- Werken in **realtime** op alles, waaronder cloudbestanden, streams en modulemuziek.
- **Veranderen of heropslaan nooit** je bestanden. Zet een effect uit en het origineel keert terug.
- **Onthouden je instellingen** voor elk effect.
- Kunnen vrij worden **gemengd en gecombineerd**, aangezien elk apart is.

## Eenvoudige recepten om te proberen

**Alledaags luisteren**

- **Meer bas, schoon:** Equalizer > Bass Booster, verlaag daarna de Voorversterker 1 tot 2 dB. Of voeg een DSP Low Shelf op Bass Boost toe.
- **Egaal volume over een gemengde afspeellijst:** Volumenormalisatie > Standard, plus Compressor > Soft.
- **Zachte algehele afwerking:** Compressor > Transparent, plus Volumenormalisatie > Light.
- **Helderdere zang:** Equalizer > Vocal Booster, of een DSP Peaking-blok op Vocal Boost.
- **Voller geluid op kleine telefoonluidsprekers:** Equalizer > Small Speakers.

**Koptelefoon**

- **Prettiger, minder vermoeiend op een koptelefoon:** Crossfeed > Chu Moy of Jan Meier.
- **Breder geluid op een koptelefoon:** DSP Stereo Width > Wide, plus Crossfeed > Chu Moy.
- **Herstel hard-gepande platen uit de jaren 1960 en 1970:** Crossfeed > Vintage Stereo.
- **Een beetje lucht en ruimte:** Freeverb > Ambience, laag gehouden, plus Crossfeed > Subtle.

**Rustige momenten en gesproken audio**

- **Stil laatavondluisteren:** Volumenormalisatie > Night, plus Compressor > Late Night.
- **Podcasts en audioboeken:** Compressor > Voice / Podcast, plus Equalizer > Spoken Word.
- **Luidst, meest egale geluid in een luidruchtige auto:** Volumenormalisatie > Strong, plus Compressor > Heavy.

**Problemen oplossen**

- **Tem een schelle, heldere opname:** Equalizer > Treble Reducer, of een DSP Peaking-blok op Tame Harsh.
- **Verwijder elektrische brom:** DSP-keten > Notch > Mains Hum 60 (of Mains Hum 50 in Europa).
- **Strakkere, schonere bas:** DSP High Pass > Tighten, om het galmende laag weg te snijden.
- **Minder gedreun in een bas-zware mix:** DSP Low Shelf > Trim Bass, of Peaking > De-Boom.

**Creatief en leuk**

- **Warm, ruimtelijk gevoel:** Freeverb > Hall, laag gehouden.
- **Dromerige, ruimtelijke gitaren:** Chorus > Wide, plus Echo > Long.
- **Retro lo-fi:** DSP-keten > Bit Crusher (LoFi) in Soft Clip (Warm).
- **Funky beweging op elektronische nummers:** Auto Wah > Funky, of Phaser > Fast.
- **Klassieke straaljager-sweep:** Flanger > Jet.

## FAQ

{{% details title="Welke geluidsengine gebruikt Flacbox?" closed="true" %}}
Je kiest één Afspeelengine in Instellingen > Audiospeler: Standard (de systeemengine van Apple), Universal (de FFmpeg-engine), of Sound FX (de BASS™-engine van Un4seen Developments, un4seen.com). De engine die je kiest bepaalt welke bestandsformaten afspelen. Sound FX is degene die extra formaten afspeelt zoals FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus en MOD- of trackermuziek, en het is de enige engine die de live effecten, de 10-bands equalizer en de DSP-keten biedt. Om de effecten te gebruiken, zet je de Afspeelengine op Sound FX.
{{% /details %}}

{{% details title="Kan Flacbox MOD, XM, IT en andere tracker- of modulemuziek afspelen?" closed="true" %}}
Ja. De BASS™-engine heeft een ingebouwde modulespeler die MOD-, XM-, IT-, S3M-, MTM-, UMX- en MO3-bestanden laadt en het nummer live opnieuw opbouwt vanuit zijn patronen en instrumentgeluiden, zoals trackermuziek bedoeld is om te spelen. Gewone iPhone-spelers kunnen dit niet. Effecten en de equalizer werken ook op modulemuziek.
{{% /details %}}

{{% details title="Ondersteunt Flacbox DSD- en high-resolution bestanden?" closed="true" %}}
Ja. Flacbox speelt DSD-bestanden (DSF en DFF) af via de BASS™-engine met DSD over PCM zodat ze werken op normale uitvoerhardware, plus FLAC, WavPack, Monkey's Audio (APE), Musepack en TrueAudio voor lossless afspelen.
{{% /details %}}

{{% details title="Welke geluidseffecten heeft Flacbox?" closed="true" %}}
Een 10-bands equalizer, Volumenormalisatie, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate en Crossfeed, plus een zelf te bouwen DSP-keten met filters, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay en stereobreedte. Elk effect is apart en kan met de andere worden gecombineerd.
{{% /details %}}

{{% details title="Wat is een preset?" closed="true" %}}
Een preset is een kant-en-klare instelling voor een effect. In plaats van zelf schuifregelaars te verplaatsen, tik je op een preset en verandert het geluid dienovereenkomstig. Elk effect in Flacbox heeft meerdere presets, en deze gids beschrijft wat elk ervan doet. Als je een schuifregelaar verplaatst nadat je een preset hebt gekozen, toont het effect 'Manual' om je te vertellen dat het nu je eigen waarden gebruikt.
{{% /details %}}

{{% details title="Hoe open ik de audio-effecten in Flacbox?" closed="true" %}}
Open de Now Playing-speler, tik op de ⋯ (Meer)-knop en kies Audio-effecten. Of ga naar Instellingen > Audiospeler > Audio-effecten. Tik op een effect, zet zijn schakelaar aan en kies een preset, of open de schuifregelaars om fijn af te stemmen.
{{% /details %}}

{{% details title="Waar is de equalizer, en wat zijn de beste instellingen?" closed="true" %}}
Ga naar Instellingen > Audiospeler > Audio-equalizer. Hij heeft 10 banden van 32 Hz tot 16 kHz, elk van -12 tot +12 dB, plus een -24 tot +24 dB Voorversterker en 22 presets. Voor meer bas gebruik je Bass Booster. Voor helderdere stemmen gebruik je Vocal Booster of Pop. Voor een helderder geluid gebruik je Treble Booster. Stel daarna losse banden naar smaak af.
{{% /details %}}

{{% details title="Hoe versterk ik de bas in Flacbox?" closed="true" %}}
Twee eenvoudige manieren. Kies in de Audio-equalizer Bass Booster (of verhoog de 32 Hz- en 64 Hz-banden een paar dB). Of voeg in Signaalverwerking een Low Shelf-blok toe ingesteld op Bass Boost. In beide gevallen verlaag je de Voorversterker of voeg je een Gain-blok toe van 1 tot 2 dB zodat de bas schoon blijft en niet vervormt.
{{% /details %}}

{{% details title="Welke equalizer-preset is het beste voor mijn muziek?" closed="true" %}}
Rock en Electronic voegen energie toe met sterk laag en hoog. Acoustic, Jazz en Classical blijven warm en natuurlijk. Pop en Vocal Booster duwen stemmen naar voren. Bass Booster en Hip-Hop voegen gewicht toe. Deep en Loudness klinken voller op laag volume. Begin met degene die bij je genre past, en stem daarna fijn af.
{{% /details %}}

{{% details title="Wat is Volumenormalisatie, en hoe verschilt het van ReplayGain?" closed="true" %}}
Het laat elk nummer op ongeveer dezelfde luidheid spelen. Het meet de werkelijke luidheid met de EBU R128-standaard (in LUFS, zoals streamingdiensten) en past elk nummer aan naar jouw doel, met een max-boost-limiet. Anders dan ReplayGain heeft het geen tags in je bestanden nodig en werkt het op elke bron, live, zonder de audio te veranderen. Presets: Light, Standard, Strong en Night.
{{% /details %}}

{{% details title="Wat is Crossfeed, en zou ik het moeten gebruiken?" closed="true" %}}
Crossfeed mengt een beetje van het linker- en rechterkanaal samen zodat een koptelefoon meer aanvoelt als echte luidsprekers en minder alsof het geluid vastzit in je hoofd. Het is alleen voor een koptelefoon, dus zet het uit voor luidsprekers. Flacbox gebruikt de bs2b (Bauer)-methode, met presets zoals Chu Moy en Jan Meier.
{{% /details %}}

{{% details title="Wat is het verschil tussen de Compressor en Volumenormalisatie?" closed="true" %}}
Volumenormalisatie stemt de luidheid tussen verschillende nummers af. De Compressor egaliseert de luide en zachte delen binnen één nummer. Ze lossen verschillende problemen op en werken goed samen, vooral in een auto of op een luidruchtige plek.
{{% /details %}}

{{% details title="Wat is de Signaalverwerking (DSP)-keten?" closed="true" %}}
Het is een zelf te bouwen rack in Instellingen > Audiospeler > Signaalverwerking. Voeg blokken toe zoals filters, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay en stereobreedte, zet ze in elke volgorde, zet elk aan of uit, en richt de keten op alle kanalen, links of rechts. Omdat de volgorde ertoe doet, kun je precies het geluid ontwerpen dat je wilt.
{{% /details %}}

{{% details title="Wat is het verschil tussen de Equalizer, de effecten en de DSP-keten?" closed="true" %}}
De Equalizer is een eenvoudige 10-bands klankregeling. De Audio-effecten zijn kant-en-klare tools (compressor, reverb, echo, enzovoort) met presets. De DSP-keten is waar je je eigen effectvolgorde bouwt uit individuele blokken. Je kunt alle drie tegelijk draaien.
{{% /details %}}

{{% details title="Veranderen of beschadigen de effecten mijn muziekbestanden?" closed="true" %}}
Nee. Alles wordt live toegepast terwijl de muziek speelt. Je bestanden worden nooit veranderd of heropgeslagen. Zet een effect uit en het oorspronkelijke geluid keert meteen terug.
{{% /details %}}

{{% details title="Kan ik meer dan één effect tegelijk gebruiken?" closed="true" %}}
Ja. Elk effect heeft zijn eigen schakelaar en er is geen hoofdschakelaar, dus elke combinatie werkt. Bijvoorbeeld Volumenormalisatie plus Compressor voor egaal luisteren, of Freeverb plus Crossfeed op een koptelefoon, met de equalizer erbovenop.
{{% /details %}}

{{% details title="Waarom zijn de effectregelaars grijs?" closed="true" %}}
Het effect staat uit. Zet zijn schakelaar bovenaan de editor aan om de regelaars te gebruiken. Elk effect staat standaard uit.
{{% /details %}}

{{% details title="Wat betekent het label Manual?" closed="true" %}}
Het betekent dat je een schuifregelaar van een preset af hebt bewogen, dus het effect gebruikt nu je eigen aangepaste waarden in plaats van een benoemde preset. Elke schuifregelaar heeft een resetknop, en het opnieuw kiezen van een preset vervangt je handmatige waarden.
{{% /details %}}

{{% details title="Kan ik mijn equalizer-presets opslaan en delen?" closed="true" %}}
Ja. Naast de 22 ingebouwde presets kun je je eigen presets maken, ze herordenen, en ze exporteren of importeren om je instellingen naar een ander apparaat te verplaatsen.
{{% /details %}}

{{% details title="Werken de effecten met CarPlay, streaming en achtergrondafspelen?" closed="true" %}}
Ja. De effecten draaien binnen de BASS™-engine, dus ze zijn van toepassing op lokale bestanden, cloud drives, mediaservers, streams en modulemuziek, en ze blijven werken tijdens CarPlay en achtergrondafspelen.
{{% /details %}}

{{% details title="Kan ik de audio-uitvoerkwaliteit wijzigen?" closed="true" %}}
Ja. In Instellingen > Audiospeler kun je de uitvoer-samplerate, het aantal kanalen en de buffergrootte instellen om bij je koptelefoon, luidsprekers of DAC te passen.
{{% /details %}}

{{% details title="Wat is een goede startopstelling voor een koptelefoon?" closed="true" %}}
Zet Volumenormalisatie aan (Standard), voeg een lichte Compressor toe (Soft), kies een equalizer-preset die je bevalt, en zet Crossfeed aan (Chu Moy of Jan Meier). Laat reverb, echo en distortion uit tenzij je een creatief geluid wilt.
{{% /details %}}

---

*BASS is een handelsmerk van Un4seen Developments Ltd. Zie [un4seen.com](https://www.un4seen.com/). Crossfeed gebruikt het bs2b (Bauer stereophonic-to-binaural)-algoritme; zie de [bs2b projectpagina](https://bs2b.sourceforge.net/).*
