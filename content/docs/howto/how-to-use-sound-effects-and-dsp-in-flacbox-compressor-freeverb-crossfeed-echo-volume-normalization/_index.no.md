---
title: "Slik bruker du lydeffekter og DSP i Flacbox: Compressor, Freeverb, Crossfeed, Echo, volumnormalisering og mer (hver forhåndsinnstilling og innstilling forklart)"
date: 2026-07-24
description: "Den komplette guiden til Flacbox-lyd på iPhone, iPad og Mac. Lær hvordan BASS-motoren fungerer, hvilke ekstra formater den spiller (inkludert MOD- og tracker-musikk og DSD), og nøyaktig hva hver effekt, hver skyvekontroll og hver forhåndsinnstilling gjør med lyden din, pluss 10-bånds equalizeren og den tilpassede DSP-kjeden."
keywords: ["Flacbox lydeffekter", "Flacbox forhåndsinnstillinger forklart", "Flacbox BASS-motor", "BASS lydbibliotek iOS", "MOD musikkspiller iPhone", "tracker musikkspiller iOS", "spill MOD XM IT S3M iPhone", "DSD-spiller iOS", "FLAC-spiller iPhone", "tapsfri musikkspiller iOS", "Flacbox equalizer forhåndsinnstillinger", "10-bånds equalizer iPhone", "volumnormalisering iPhone", "EBU R128 iOS", "loudness-normalisering musikkspiller", "crossfeed hodetelefoner iOS", "bs2b crossfeed", "compressor forhåndsinnstillinger musikkspiller", "freeverb romklang iOS", "echo delay musikkspiller", "DSP-kjede musikkspiller", "bassforsterkning iPhone", "slik legger du til effekter på musikk Flacbox", "beste equalizer-innstillinger iPhone"]
tags: ["Flacbox", "Lydeffekter", "Veiledning", "BASS", "Equalizer", "Bassforsterkning", "Compressor", "Freeverb", "Crossfeed", "Echo", "Volumnormalisering", "EBU R128", "MOD-musikk", "Tracker-musikk", "DSD", "FLAC", "DSP", "Hodetelefoner", "Forhåndsinnstillinger"]
readingTime: 30
---

{{< author-byline >}}

**Kort svar:** I Flacbox velger du én **Avspillingsmotor** i **Innstillinger > Lydspiller**: **Standard** (Apples systemmotor), **Universal** (FFmpeg-motoren) eller **Sound FX** (**BASS™-motoren**). Motoren du velger avgjør hvilke filformater som spilles, så valget betyr noe. **Sound FX**-motoren spiller ekstra formater som de fleste iPhone-apper hopper over (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus og gammel **MOD- og tracker-musikk** som MOD, XM, IT og S3M), og den er den eneste motoren som driver lydverktøyene: en **10-bånds equalizer**, **volumnormalisering**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** og en lag-din-egen **DSP-kjede**. Så for å bruke effektene i denne guiden må du først sette avspillingsmotoren til **Sound FX**. Hvert verktøy har ferdiglagde **forhåndsinnstillinger**. Åpne dem i **Innstillinger > Lydspiller** (Lydeffekter, Lydequalizer, Signalbehandling), eller trykk på **⋯ (Flere handlinger)**-knappen på spilleren og velg **Lydeffekter**. Ingenting du gjør her endrer noen gang filene dine.

> Forklaringene på skyvekontroller og forhåndsinnstillinger nedenfor er de samme korte beskrivelsene som Flacbox viser deg inne i appen, blandet med litt ekstra bakgrunn slik at du får hele bildet før du trykker.

## Slik leser du denne guiden

Hvert verktøy fungerer på samme måte:

1. **Slå det på.** Hver effekt har sin egen av/på-bryter. De er alle av til å begynne med. Du kan slå på så mange du vil samtidig.
2. **Velg en forhåndsinnstilling.** En forhåndsinnstilling er en ferdiglaget innstilling. Trykk på én, og lyden endres med én gang. Denne guiden lister opp hva **hver** forhåndsinnstilling gjør.
3. **Finjuster (valgfritt).** Åpne skyvekontrollene for å justere for hånd. I det øyeblikket du flytter en skyvekontroll, viser effekten **Manuell**, så du vet at du har forlatt forhåndsinnstillingen. Hver skyvekontroll har en tilbakestillingsknapp.

Ingenting lagres i filene dine. Dette er sanntidseffekter. Slå en effekt av, og den opprinnelige lyden din kommer tilbake med én gang.

## Velg avspillingsmotoren din (Sound FX har effektene)

Flacbox blander ikke motorer sammen. Du velger **én** i **Innstillinger > Lydspiller > Avspillingsmotor**, og motoren du velger avgjør hvilke filformater du kan spille og om effektene er tilgjengelige. Det er tre valg, vist i appen under disse eksakte navnene:

1. **Standard.** Apples innebygde systemmotor. Bruker maskinvaredekoding for lavere batteribruk.
2. **Universal.** FFmpeg-motoren, som åpner et svært bredt spekter av formater.
3. **Sound FX.** **BASS™-motoren**. Den spiller tapsfrie filer og filer med høy oppløsning med full nøyaktighet, legger til modul- (tracker-) musikk, og driver hver effekt, 10-bånds equalizeren og DSP-kjeden i denne guiden.

Fordi hver motor støtter sitt eget sett med formater, endres filene du kan spille med motoren du velger. Enda viktigere: effektene, equalizeren og DSP-kjeden fungerer **kun** med **Sound FX**-motoren, så velg den først hvis du vil bruke dem.

Sound FX er bygget på **BASS™**, et profesjonelt lydbibliotek fra Un4seen Developments. Du kan lese mer om det på hjemmesiden på [un4seen.com](https://www.un4seen.com/).

## Musikkformater: hva Sound FX (BASS™)-motoren legger til (inkludert MOD- og tracker-musikk)

Med **Sound FX (BASS™)**-motoren valgt spiller Flacbox spesialistformatene nedenfor, i tillegg til de vanlige. Det mest spesielle er **modulmusikk**, også kalt **tracker-musikk**. En modulfil er ikke et vanlig opptak. Den inneholder små instrumentlyder pluss et «partitur» som sier hvordan de skal spilles, og Flacbox bygger sangen opp igjen i sanntid fra det partituret, slik disse filene var ment å spilles. Vanlige spillere kan ikke gjøre dette.

| Musikktype | Formater | Godt å vite |
|---|---|---|
| **Modul- / tracker-musikk** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Bygget opp i sanntid av BASS™-modulspilleren. Flott for chiptunes og gamle demoscene- eller Amiga-sanger. |
| **Moderne tapsfri** | FLAC | Full kvalitet, mindre enn WAV. |
| **Annen tapsfri** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Mindre vanlige tapsfrie typer, alle støttet. |
| **DSD med høy oppløsning** | DSF, DFF | Spilles på vanlig maskinvare ved hjelp av DSD over PCM. |
| **Moderne tapsbelagt** | Opus, Ogg Vorbis, MP3 | De vanlige strømme- og nedlastingstypene. |

Sound FX-motoren spiller også de vanlige Apple-formatene (AAC, ALAC, M4A, WAV, AIFF) og direktestrømmer, så effektene og equalizeren fungerer på dem også.

**Hvorfor dette hjelper deg:** hvis du har en blanding av FLAC-album, DSD-filer med høy oppløsning og en mappe med gamle MOD- eller XM-tracker-sanger, spiller Flacbox dem alle, og equalizeren og effektene fungerer på hver eneste av dem.

## De tre menyene du kommer til å bruke

Flacbox holder lydverktøyene sine på tre steder, alle inne i innstillingene for lydspilleren. Sørg først for at **Avspillingsmotoren** din er satt til **Sound FX** (Innstillinger > Lydspiller > Avspillingsmotor), fordi effektene, equalizeren og DSP-kjeden bare er tilgjengelige med den motoren.

- **Lydeffekter** (effektracket): åpne spilleren, trykk **⋯ (Flere handlinger)**, trykk **Lydeffekter**. Eller gå til **Innstillinger > Lydspiller > Lydeffekter**.
- **Lydequalizer** (10 bånd og forhåndsinnstillinger): **Innstillinger > Lydspiller > Lydequalizer**.
- **Signalbehandling** (din egen DSP-kjede): **Innstillinger > Lydspiller > Signalbehandling**.

Du kan også stille inn **utgangs-samplingsfrekvensen**, **kanalene** og **bufferstørrelsen** under **Innstillinger > Lydspiller**.

## 10-bånds equalizeren

**Hva den gjør:** Endrer tonen i musikken, fra dyp bass til lys diskant. Dette er det beste verktøyet for en ren **bassforsterkning** eller en lysere, klarere topp. Tenk på den som ti volumknapper, hver for en ulik del av lyden. Løft et bånd for å bringe den delen fram, senk det for å trekke den tilbake. Små endringer på noen få dB høres vanligvis best ut, og den fungerer på alt du spiller.

**Hvordan den fungerer:** Ti skyvekontroller på **32, 64, 125, 250, 500 Hz og 1, 2, 4, 8, 16 kHz**. Hver går fra **-12 dB (kutt)** til **+12 dB (forsterkning)**. Det er også en **Forforsterker** fra **-24 til +24 dB** for det generelle nivået. Du kan lagre dine egne forhåndsinnstillinger og **eksportere eller importere** dem mellom enheter.

**Hva hver innebygde forhåndsinnstilling gjør (22 forhåndsinnstillinger):**

| Forhåndsinnstilling | Hva den gjør med lyden din |
|---|---|
| **Flat** | Ingen endring. Alle bånd på null. Et rent utgangspunkt. |
| **Acoustic** | Varm bass og skarp, tilstedeværende diskant. Får akustiske gitarer og stemmer til å føles naturlige og livlige. |
| **Bass Booster** | Sterkt løft i det lave området, mellomtoner og diskant urørt. Mer trøkk og tyngde. |
| **Bass Reducer** | Kutter det lave området. Nyttig for drønnete rom, billige ørepropper eller tunge spor. |
| **Treble Booster** | Løfter kun diskanten. Gir glans og luft, mer detalj. |
| **Treble Reducer** | Mykner diskanten. Temmer skarpe eller harde opptak. |
| **Classical** | Full bass og myk diskant med et lite mellomtonedropp. Jevn og romslig for orkestermusikk. |
| **Dance** | Stor bass og lys diskant med senkede mellomtoner. Trøkkende og energisk for klubbspor. |
| **Deep** | Varmt, tykt lavområde med mykere diskant. En koselig, avslappet lyd. |
| **Electronic** | Sterk bass og lys diskant for synther og beats. Bred og moderne. |
| **Hip-Hop** | Tung bass og klar diskant med kontrollerte mellomtoner. Tung og trøkkende. |
| **Jazz** | Varm og jevn, med et lite mellomtonedropp. Lett og naturlig for akustisk jazz. |
| **Latin** | Forsterket bass og diskant med rene mellomtoner. Lys og livlig. |
| **Loudness** | Forsterker bass og diskant kraftig (en «smile»-kurve). Høres fyldigere ut ved lavt volum. |
| **Lounge** | Framtredende mellomtoner med myke kanter. Avslappet og stemmevennlig. |
| **Piano** | Klare mellomtoner og diskant slik at pianotoner ringer rent ut. |
| **Pop** | Løftede mellomtoner for vokal, med bass og diskant trukket tilbake. Stemmer sitter foran. |
| **R&B** | Svært sterk varme i de lave mellomtonene og klar diskant. Jevn og rik. |
| **Rock** | Forsterket bass og diskant for gitarer og trommer. Energisk og full. |
| **Small Speakers** | Forsterker bassen og kutter diskanten for å hjelpe små høyttalere å høres fyldigere ut. |
| **Spoken Word** | Løfter stemmeområdet og kutter den dype bassen. Gjør tale klar. |
| **Vocal Booster** | Skyver fram midten der stemmer bor, kutter rundt dem. Vokal skiller seg ut. |

**Tips for bass:** Start med **Bass Booster**, og hvis det høres grumsete ut, trekk Forforsterkeren ned 1 til 2 dB slik at ingenting forvrenges.

## Volumnormalisering (jevn loudness)

**Hva den gjør:** Noen sanger spiller høyere enn andre, så du endrer volumet hele tiden. Dette får hver sang til å spille på omtrent samme volum av seg selv, så du slipper. Det er perfekt for tilfeldig avspilte spillelister som blander gamle og nye opptak, ulike album eller ulike kilder, der ett spor kan være mye høyere enn det neste.

**Hvordan den fungerer:** Den lytter til den virkelige loudnessen til hvert spor ved hjelp av **EBU R128**-standarden (målt i **LUFS**, samme idé som strømmetjenester bruker), og justerer deretter hvert spor mot målet ditt. Den trenger ingen tagger i filene dine og endrer aldri lyden. EBU R128 måler loudnessen ørene dine faktisk føler gjennom hele sangen, ikke bare den høyeste toppen, og det er derfor den samsvarer med hvor høyt spor egentlig virker for deg. Flacbox regner dette ut i sanntid mens musikken spilles (og sjekker loudnessen på forhånd når det er mulig), og bruker deretter én jevn volumendring på sporet. **Maks forsterkning**-grensen hindrer svært stille opptak fra å bli skjøvet opp så hardt at de forvrenges. Fordi den leser selve lyden, fungerer den på enhver kilde, inkludert skyfiler, direktestrømmer og modulmusikk, selv når filene ikke har noen loudness-tagger i det hele tatt.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Mål-loudness** | Setter loudnessen hvert spor jevnes mot. Høyere verdier får alt til å spille høyere totalt sett. | -30 til -6 LUFS (-16) |
| **Maks forsterkning** | Begrenser hvor mye stille spor kan forsterkes. Høyere verdier bringer myke opptak nærmere målet. | 0 til 24 dB (12) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Light** | Skånsom jevning for avslappet lytting. Jevner ut åpenbare volumhopp uten å skyve stille spor hardt. |
| **Standard** | Allsidig standard. Et strømmelignende loudness-mål som passer det meste av musikk. Start her. |
| **Strong** | Aggressiv tilpasning som skyver stille spor bestemt opp. Best for blandede biblioteker med store nivåforskjeller. |
| **Night** | Et stillere overordnet mål som fortsatt løfter myke passasjer, så senkveldslytting holder seg jevn og lav. |

## Compressor (jevn ut høye og stille deler)

**Hva den gjør:** I én sang kan de stille delene være for svake og de høye delene for høye. Dette bringer dem nærmere hverandre, så hele sangen er lett å høre, selv i bilen eller på et støyende sted. Den skrur forsiktig ned de høyeste øyeblikkene og løfter de mykere, så du slutter å strekke deg etter volumet gjennom ett enkelt spor. Dette er forskjellig fra volumnormalisering: Compressor jevner ut ting **inne i** én sang, mens volumnormalisering matcher loudness **mellom** sanger. De to fungerer godt sammen. Start med en forhåndsinnstilling, og åpne kun skyvekontrollene hvis du vil ha mer kontroll.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Terskel** | Nivået der komprimeringen starter. Lavere verdier klemmer mer av lyden, og holder stille og høye deler nærmere sammen. | -60 til 0 dB (-20) |
| **Ratio** | Hvor sterkt de høye delene holdes tilbake når de passerer terskelen. Høyere verdier komprimerer hardere og holder lyden jevnere. | 1:1 til 30:1 (4:1) |
| **Attack** | Hvor raskt effekten reagerer på en plutselig høy topp. Korte verdier fanger transienter; lengre slipper dem gjennom. | 0,1 til 1000 ms (10 ms) |
| **Release** | Hvor raskt effekten slipper etter at den høye delen passerer. Korte verdier kan pumpe; lengre høres jevnere ut. | 10 ms til 5 s (100 ms) |
| **Master-gain** | Endelig utgangsforsterkning etter behandling. Løft denne for å heve den generelle loudnessen når dynamikken er jevnet ut. | -30 til +30 dB (0) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Transparent** | Nesten umerkelig sikkerhetsnett. Bevarer dynamikken nesten helt og fanger bare de høyeste toppene. |
| **Soft** | Lett jevning for hi-fi-lytting hjemme. Subtil utjevning uten å klemme musikken. |
| **Standard** | Fornuftig standard for daglig musikkavspilling. Den første forhåndsinnstillingen å prøve. |
| **Heavy** | Aggressiv jevning for støyende miljøer. Bil, fullt rom, lytting på lavt volum. |
| **Voice / Podcast** | Tilpasset tale. Tregere attack slipper sibilanter gjennom, sjenerøs makeup-gain trekker vokal opp. |
| **Old Recordings** | Gamle album og restaurert vinyl, der gjennomsnittsnivået er under moderne utgivelser. |
| **Late Night** | Tung komprimering pluss stor forsterkning for stille lytting når naboer eller sovende familie betyr noe. |
| **Movie Dialog** | Bringer tale opp mot musikk og lydeffekter i et variert lydspor. |
| **Streaming Match** | Sikter mot omtrent loudness-normaliseringen til moderne strømmetjenester rundt -14 LUFS. |
| **Maximum Loudness** | Alt inn. Treffer begrenseren; forvent et klemt, svært jevnt signal. Den bokstavelige maksvolum-forhåndsinnstillingen. |

## Freeverb (romklang, en følelse av rom)

**Hva den gjør:** Legger til en følelse av rom i musikken, fra et lite rom opp til en stor sal. Velg en forhåndsinnstilling, eller finjuster tørr- og våt-miksen, romstørrelse, demping og bredde selv. Romklang er det naturlige ekkoet du hører i ethvert virkelig rom, og Freeverb gjenskaper det i programvare. Litt får flate eller nær-mikkede opptak til å føles mer åpne og levende. Mye plasserer musikken i et stort, fjernt rom. Det er en kreativ effekt, så hold våt-miksen beskjeden for naturlige resultater.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Tørr-miks** | Hvor mye av den opprinnelige, urørte lyden som beholdes. Høyere verdier lar mer av det tørre signalet være i miksen. | 0 til 1 (0.0) |
| **Våt-miks** | Hvor mye av den etterklangsbehandlede lyden som legges til. Høyere verdier gjør romklangen høyere og mer tydelig. | 0 til 3 (1.0) |
| **Romstørrelse** | Størrelsen på det forestilte rommet. Høyere verdier gir en lengre, større klanghale, fra et lite rom opp til en katedral. | 0 til 1 (0.5) |
| **Demp** | Hvor raskt de høye frekvensene toner ut i halen. Høyere verdier gjør romklangen mørkere og varmere. | 0 til 1 (0.5) |
| **Bredde** | Stereospredningen til romklangen. Høyere verdier får rommet til å føles bredere mellom venstre og høyre kanal. | 0 til 1 (1.0) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Room** | Et lite, tett rom. Subtil ambiens som legger til en følelse av sted uten å vaske ut lyden. |
| **Studio** | Et tørt, kontrollert innspillingsrom. Akkurat nok refleksjon til å høres naturlig ut. |
| **Hall** | En stor konsertsal. En lang, frodig hale som passer orkester- og akustisk musikk. |
| **Cathedral** | Et enormt, ekkoende steinrom. Den lengste, mest dramatiske klanghalen. |
| **Plate** | En lys, tett studio-plateklang. Klassisk for vokal og trommer. |
| **Ambience** | En kort, luftig ambiens. Legger til en lett følelse av rom mens den holder seg for det meste tørr. |

## Auto Wah (funky filtersveip)

**Hva den gjør:** Et filter som sveiper opp og ned av seg selv for en funky, stemmelignende wah-lyd. Velg en forhåndsinnstilling, eller sett våt-miks, tilbakekobling, hastighet, område og frekvens selv. Det er det samme «wah»-sveipet en gitar-wah-pedal lager, men her beveger det seg av seg selv i takt med musikken. Det høres flott ut på funk, disco og elektroniske spor. Det er en dristig, tydelig effekt, så litt rekker langt på daglig lytting.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Våt-miks** | Hvor sterk wah-effekten er i miksen. Høyere verdier gjør det sveipende filteret mer tydelig. | -2 til +2 (1.5) |
| **Tilbakekobling** | Hvor mye av utgangen som mates tilbake til effekten. Høyere verdier gjør wahen mer resonant og markant. | -1 til +1 (0.5) |
| **Hastighet** | Hvor raskt filteret sveiper opp og ned. Høyere verdier gir en raskere, mer rytmisk wah. | 0,1 til 9 Hz (2.0) |
| **Område** | Hvor langt filteret sveiper, i oktaver. Høyere verdier gir et bredere, mer dramatisk sveip. | 0,1 til 9 oktaver (4.3) |
| **Frekvens** | Grunnfrekvensen filteret sveiper rundt. Lavere verdier høres dypere ut; høyere verdier høres lysere ut. | 1 til 1000 Hz (50) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Classic** | Et balansert, klassisk wah-sveip. Et godt utgangspunkt for funk og rock. |
| **Slow** | Et sakte, bredt sveip som driver forsiktig opp og ned. Flott for pads og lange toner. |
| **Funky** | Et raskt, trøkkende sveip med mye bevegelse. Gir rytmisk bitt til gitarer og synther. |
| **Deep** | Et dypt, bredt sveip som starter fra en lav frekvens. Stort og dramatisk. |
| **Subtle** | En skånsom, dempet bevegelse. Gir karakter uten å dominere lyden. |
| **Resonant** | En skarp, resonant wah med høy tilbakekobling. Stemmelignende og uttrykksfull. |

## Phaser (virvlende whoosh)

**Hva den gjør:** Et sveipende filter som legger til en virvlende, whooshende bevegelse i lyden. Velg en forhåndsinnstilling, eller sett tilbakekobling, hastighet, område og frekvens selv. Det legger til skånsom bevegelse og skimmer uten å endre tonene. Det er subtilt på vokal og pads, og dramatisk på synther og gitarer. Prøv Slow for en drømmende følelse eller Jet for en sterk virvel.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Tilbakekobling** | Hvor mye av utgangen som mates tilbake til effekten. Høyere verdier gjør phaseren mer resonant og markant. | -1 til +1 (0.0) |
| **Hastighet** | Hvor raskt filteret sveiper opp og ned. Høyere verdier gir en raskere, mer rytmisk phasing. | 0,1 til 9 Hz (1.0) |
| **Område** | Hvor langt filteret sveiper, i oktaver. Høyere verdier gir et bredere, mer dramatisk sveip. | 0,1 til 9 oktaver (4.0) |
| **Frekvens** | Grunnfrekvensen filteret sveiper rundt. Lavere verdier høres dypere ut; høyere verdier høres lysere ut. | 1 til 1000 Hz (100) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Classic** | Et balansert, klassisk phaser-sveip. Et godt utgangspunkt for gitarer og keys. |
| **Slow** | Et sakte, bredt sveip som driver forsiktig opp og ned. Flott for pads og lange toner. |
| **Fast** | Et raskt, skimrende sveip med mye bevegelse. Gir bevegelse og energi. |
| **Deep** | Et dypt, bredt sveip som starter fra en lav frekvens. Stort og dramatisk. |
| **Subtle** | En skånsom, dempet bevegelse. Gir karakter uten å dominere lyden. |
| **Jet** | Et intenst, resonant sveip med høy tilbakekobling, den klassiske jetfly-whooshen. |

## Flanger (jetfly-sveip)

**Hva den gjør:** En kort, bevegelig forsinkelse som gir lyden en jet-lignende, sveipende whoosh. Velg en forhåndsinnstilling, eller sett dybde, tilbakekobling, hastighet og forsinkelse selv. Det er en sterkere, mer metallisk fetter av phaseren, berømt for det whooshende sveipet i klassisk rock og elektronisk musikk. Subtile innstillinger gir skånsom bevegelse, mens dype innstillinger er dramatiske og tydelige. Best brukt sparsomt, for effekt.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Dybde** | Hvor sterk den sveipende effekten er. Høyere verdier gjør flangingen mer tydelig. | 0 til 100 % (25) |
| **Tilbakekobling** | Hvor mye av utgangen som mates tilbake til effekten. Høyere verdier gjør flangeren mer resonant og metallisk. | -99 til +99 % (-50) |
| **Hastighet** | Hvor raskt sveipet beveger seg opp og ned. Høyere verdier gir en raskere, mer skimrende bevegelse. | 0 til 10 Hz (0.25) |
| **Forsinkelse** | Grunnforsinkelsestiden sveipet er bygget på. Høyere verdier gir en dypere, mer hul karakter. | 0 til 4 ms (2.0) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Classic** | En balansert, klassisk flanger. Et godt utgangspunkt for gitarer og keys. |
| **Subtle** | Et skånsomt, dempet sveip. Gir bevegelse uten å dominere lyden. |
| **Deep** | Et dypt, tungt sveip med sterk tilbakekobling. Stort og dramatisk. |
| **Jet** | Et intenst sveip med positiv tilbakekobling, den klassiske jetfly-whooshen. |
| **Fast** | Et raskt, skimrende sveip med mye bevegelse og energi. |
| **Wide** | Et sakte, bredt sveip med en lang forsinkelse. Frodig og romslig. |

## Echo (gjentakelser)

**Hva den gjør:** Gjentar lyden som utfadende ekkoer for en følelse av rom og dybde. Velg en forhåndsinnstilling, eller sett våt-miks, tilbakekobling og forsinkelse selv. Det er som å rope ut i en canyon: lyden kommer tilbake én eller flere ganger etter et kort mellomrom. En enkelt kort gjentakelse legger til kropp og en retro følelse, mens lengre gjentakelser med mer tilbakekobling skaper romslige, etterslepende haler. Ping Pong-forhåndsinnstillingen spretter gjentakelsene mellom venstre og høyre øre, noe som er gøy på hodetelefoner. Hold våt-miksen beskjeden slik at ekkoene støtter musikken i stedet for å dekke den.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Våt-miks** | Hvor høye ekkoene er sammenlignet med den opprinnelige lyden. Høyere verdier får gjentakelsene til å skille seg mer ut. | -2 til +2 (0.6) |
| **Tilbakekobling** | Hvor mange ganger ekkoet gjentar seg. Høyere verdier gir flere gjentakelser som tar lengre tid å tone ut. | -1 til +1 (0.5) |
| **Forsinkelse** | Tiden mellom ekkoene. Kortere verdier gir en tett slap-back; lengre verdier gir spredte gjentakelser. | 0,01 til 2 s (0.4) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Slapback** | En enkelt, tett gjentakelse rett bak lyden. Klassisk rockabilly slap-back. |
| **Room** | Et kort, naturlig ekko, som et lite rom. Gir rom uten å smøre ut lyden. |
| **Tape** | Varme, medium gjentakelser som toner gradvis ut, som en gammel båndforsinkelse. |
| **Dub** | Lange, tunge gjentakelser med sterk tilbakekobling. Stort, dubbete og romslig. |
| **Ping Pong** | Ekkoer spretter mellom venstre og høyre høyttaler for en bred stereoeffekt. |
| **Long** | Sakte, vidt spredte gjentakelser som etterslepper langt bak lyden. |

## Chorus (tykkere, bredere lyd)

**Hva den gjør:** Tykner og utvider lyden ved å legge en skiftende kopi over originalen. Velg en forhåndsinnstilling, eller sett våt/tørr-miks, dybde, hastighet og tilbakekobling selv. Den får ett instrument eller én stemme til å høres ut som flere som spiller sammen, ved å legge til lett feilstemte, bevegelige kopier. Dette gir rikdom og et skånsomt skimmer. Subtile innstillinger varmer opp ting, mens sterke innstillinger høres frodige og drømmende ut. Den er populær på gitarer, keyboards og vokal.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Våt/Tørr** | Hvor mye av chorusen du hører sammenlignet med den opprinnelige lyden. Høyere verdier gjør effekten mer tydelig. | 0 til 100 % (50) |
| **Dybde** | Hvor langt tonehøyden vaier opp og ned. Høyere verdier gir en tykkere, mer skimrende lyd. | 0 til 100 % (25) |
| **Hastighet** | Hvor raskt skimmeret beveger seg. Tregere hastigheter høres skånsomme og frodige ut; raskere hastigheter høres mer ut som vibrato. | 0 til 10 Hz (1.1) |
| **Tilbakekobling** | Hvor mye av effekten som mates tilbake i seg selv. Høyere verdier gjør chorusen mer resonant og intens. | -99 til +99 % (25) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Subtle** | En skånsom tykning som gir varme uten å trekke oppmerksomhet til seg selv. |
| **Lush** | En rik, klassisk chorus. En flott allsidig innstilling for gitarer og keys. |
| **Ensemble** | Et fullt, lagdelt skimmer som får ett enkelt instrument til å høres ut som flere. |
| **Vibrato** | Helt våt med en rask hastighet, for et vaklende vibrato i stedet for en subtil chorus. |
| **Wide** | Et sakte, bredt skimmer som åpner opp stereobildet. Romslig og drømmende. |
| **Twelve-String** | Et lyst, resonant skimmer som minner om en tolvstrengs gitar. |

## Distortion (grus og kant)

**Hva den gjør:** Legger til grus og kant ved å overdrive lyden. Velg en forhåndsinnstilling, eller sett drive, utgang og tone selv. Den ruer bevisst opp lyden, fra en varm, grusete kant til en brutt, luddent tone. Det er en kreativ, for-moro-skyld-effekt snarere enn en måte å forbedre kvaliteten på, så bruk den i små mengder. Den er gøy på elektroniske, rock- og eksperimentelle spor. Senk Utgang hvis en tung forhåndsinnstilling blir for høy.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Drive** | Hvor hardt lyden forvrenges. Høyere verdier er grusetere og mer aggressive. | 0 til 100 % (15) |
| **Utgang** | Utgangsnivået etter forvrengning. Senk det hvis en tung innstilling blir for høy. | -60 til 0 dB (-18) |
| **Tone** | Ruller av diskanten før forvrengning. Lavere verdier høres mørkere og varmere ut. | 100 til 8000 Hz (8000) |
| **Senter** | Hvilken frekvens forvrengningen er fokusert rundt. Skifter karakteren lysere eller mørkere. | 100 til 8000 Hz (2400) |
| **Bredde** | Hvor bredt det fokuset er. Smalt høres skarpt og nasalt ut; bredt høres fullt og åpent ut. | 100 til 8000 Hz (2400) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Warm Drive** | En lett, varm grus som gir kant uten å endre karakteren mye. |
| **Crunch** | En klassisk knasende overdrive, trøkkende og rytmisk. |
| **Overdrive** | En lys, drevet tone med mye bitt. Flott for lead-lyder. |
| **Fuzz** | En tykk, mettet fuzz. Tung og full av harmonikk. |
| **Metal** | En tett, mellomtone-fokusert high-gain-tone for aggressive, tunge lyder. |
| **Screamer** | En mellomtone-forsterket overdrive som skjærer gjennom, som en tube screamer. |
| **LoFi** | En knust, smalbånds forvrengning for en grusete lo-fi-karakter. |

## Rotate (roterende stereo)

**Hva den gjør:** Spinner lyden rundt stereofeltet for en roterende, virvlende effekt. Velg en forhåndsinnstilling, eller sett hastigheten selv. Den beveger lyden sakte rundt venstre og høyre kanal, litt som en roterende høyttaler, noe som gir en virvlende, hypnotisk følelse. Sakte innstillinger er skånsomme og brede, mens raske innstillinger er svimlende og tydelige. Det er en stereoeffekt, så den er mest merkbar på hodetelefoner eller godt plasserte høyttalere.

**Skyvekontroll:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Hastighet** | Hvor raskt lyden spinner rundt stereofeltet. Negative verdier spinner motsatt vei; null holder den stille. | -5 til +5 Hz (1.0) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Slow Pan** | En sakte, skånsom drift fra side til side. Subtil og bred. |
| **Sway** | En jevn venstre-høyre vugging. Gir skånsom bevegelse til stereobildet. |
| **Rotary** | En medium spinn som minner om en roterende høyttaler. |
| **Fast Spin** | En rask spinn rundt stereofeltet for en svimlende, virvlende effekt. |
| **Reverse** | En medium spinn i motsatt retning. |
| **Whirl** | En svært rask virvel. Intens og desorienterende. |

## Crossfeed (naturlig lyd på hodetelefoner)

På høyttalere hører hvert av ørene dine både venstre og høyre høyttaler, bare til litt ulike tider og volum. På hodetelefoner er den naturlige blandingen borte: venstre øre hører bare venstre kanal og høyre øre bare høyre. Denne «superstereoen» kan få musikk til å føles som om den er splittet inne i hodet ditt, og hardt panorerte opptak, der et instrument sitter helt på én side, kan føles unaturlige eller slitsomme på lange lyttinger.

Crossfeed løser dette ved å blande en liten, filtrert mengde av hver kanal inn i den andre, med en bitteliten forsinkelse og en skånsom avrulling av de høye frekvensene. Det er nær hvordan lyd fra virkelige høyttalere når begge ørene dine, inkludert måten hodet ditt litt skygger for det fjerne øret. Resultatet er et mer naturlig, høyttalerlignende bilde som sitter litt foran deg i stedet for inne i hodet ditt, og det reduserer lyttetretthet på lange økter. Flacbox bruker den velkjente **bs2b (Bauer stereophonic-to-binaural)**-metoden, en respektert åpen kildekode-crossfeed brukt av mange audiofile spillere. Du kan lese om algoritmen på [bs2b-prosjektsiden](https://bs2b.sourceforge.net/).

**Cutoff** styrer hvor varm blandingen høres ut, og **Feed level** styrer hvor sterk den er. Forhåndsinnstillingene dekker de klassiske bs2b-nivåene, fra en så vidt merkbar berøring opp til en fast, høyttalerlignende blanding. Crossfeed er en hodetelefoneffekt, så la den være av når du lytter på høyttalere.

**Skyvekontroller:**

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Cutoff** | Setter hvor blødningen mellom kanaler begynner å rulle av. Lavere verdier gir en varmere, mer markant effekt. | 300 til 2000 Hz (700) |
| **Feed level** | Styrer hvor mye av én kanal som blør inn i den andre. Høyere verdier gir en mer høyttalerlignende lyd. | 1 til 15 dB (4.5) |

**Forhåndsinnstillinger:**

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Subtle** | Så vidt merkbar crossfeed for avslappet lytting. Mykner hardt panorert stereo uten å endre tonal balanse. |
| **Chu Moy** | Den klassiske allsidige standarden. Balansert og lett varm, den fungerer på nesten alt materiale. Start her. |
| **Strong** | Sterkere blødning for hardere panorerte mikser. Mer tydelig stereoinnsnevring. |
| **Jan Meier** | Populær blant hodetelefonentusiaster. Bredere feed, mer høyttalerlignende presentasjon, lett bassløft. |
| **Speaker-like** | Innstilt for den mest naturlige høyttalerlignende gjengivelsen over hodetelefoner. |
| **Vintage Stereo** | Aggressiv crossfeed innstilt for 1960- og 1970-talls mikser med hardt panorerte trommer og vokal. |

## Signalbehandling: bygg din egen DSP-kjede

Utover de ferdiglagde effektene lar Flacbox deg bygge din egen kjede i **Innstillinger > Lydspiller > Signalbehandling**. Som appen forklarer når kjeden er tom: *«Trykk + for å legge til en effekt. Slå hver enkelt på eller av med bryteren, dra for å endre rekkefølge, trykk for å redigere parameterne, og trykk og hold for å duplisere eller slette.»*

**Rekkefølgen betyr noe**: et filter før en forvrengning høres annerledes ut enn det samme filteret etter den. Du kan også rette hele kjeden mot **Alle kanaler**, **Venstre kanal** eller **Høyre kanal**.

Nedenfor er hver blokk, med appens egen tekst for hver skyvekontroll og hver forhåndsinnstilling.

### Gain (nivåtrim)

Hever eller senker nivået på ett punkt i kjeden.

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Gain** | Forsterker eller kutter nivået på dette punktet i kjeden. Bruk den til å kompensere for nivå etter andre effekter, eller til å drive de som følger. | -24 til +24 dB (0) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Unity** | Ingen endring i nivå. Et nøytralt utgangspunkt. |
| **Cut** | Et stort kutt. Temmer en høy kilde, eller gir rom før effektene som følger. |
| **Trim** | Et skånsomt kutt for å trekke nivået litt tilbake. |
| **Lift** | Et beskjedent løft for å bringe en stille kilde opp. |
| **Boost** | Et sterkt løft for stille materiale, eller for å drive de følgende effektene hardere. |
| **Max** | Maksimal forsterkning. Høyt, pass på klipping senere i kjeden. |

### Low Pass (fjerner diskant)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Cutoff** | Setter hvor filteret begynner å rulle av diskanten. Senk den for å gjøre lyden mørkere og mykere; hev den mot toppen for å åpne helt. | 20 Hz til 20 kHz (20 kHz) |
| **Resonans** | Fremhever frekvensene rett ved cutoff. Hold den lav for en ren avrulling; hev den for en spiss, plystrende kant. | 0,1 til 10 (0.707) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Air** | Trimmer bare den aller øverste. Tar litt kant av uten å gjøre lyden matt. |
| **Warm** | En skånsom avrulling av diskanten for en varmere, rundere tone. |
| **Mellow** | Merkbart mykere. Trekker lysheten tilbake for en avslappet følelse. |
| **Muffled** | Mørk og dempet, som om hørt gjennom en vegg. |
| **Telephone** | En smal, resonant topp lavt i området. En tynn, telefonlignende stemme. |

### High Pass (fjerner bass)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Cutoff** | Setter hvor filteret begynner å rulle av bassen. Hev den for å tynne ut det lave området og fjerne rumling; senk den mot bunnen for å åpne helt. | 20 Hz til 20 kHz (20 Hz) |
| **Resonans** | Fremhever frekvensene rett ved cutoff. Hold den lav for en ren avrulling; hev den for en spiss, plystrende kant. | 0,1 til 10 (0.707) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Rumble Cut** | Fjerner subsonisk rumling og DC-forskyvning uten å berøre det hørbare lave området. |
| **Tighten** | Trimmer drønnete lave frekvenser for en strammere, renere bass. |
| **Thin** | Kutter varmen og kroppen, og etterlater en lettere, tynnere lyd. |
| **Radio** | Bare mellomtonene og diskanten gjenstår, som en liten radiohøyttaler. |
| **Telephone** | En smal, resonant topp høyt i området. En tynn, telefonlignende stemme. |

### Band Pass (beholder et midtbånd)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Senter** | Setter frekvensen filteret slipper gjennom. Alt over og under rulles av. Sveip den for å plukke ut bass, mellomtoner eller diskant. | 20 Hz til 20 kHz (1 kHz) |
| **Resonans** | Styrer hvor bredt båndet er. Lave verdier slipper et bredt område gjennom; hev den for å snevre inn på senteret for en skarp, resonant tone. | 0,1 til 10 (0.707) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Voice** | Et bredt bånd rundt mellomtoneområdet der mesteparten av vokalen sitter. Et nøytralt utgangspunkt. |
| **Bass** | Isolerer det lave området, og etterlater bare bassen og kicken. |
| **Body** | Fokuserer på de lave mellomtonene for en varm, boksete kropp. |
| **Presence** | Løfter de øvre mellomtonene for klarhet og tilstedeværelse. |
| **Telephone** | Et smalt mellomtonebånd. En tynn, telefonlignende lyd. |
| **Wah** | En svært smal, resonant topp. Sveip senteret for en wah-effekt. |

### Notch (fjerner ett smalt bånd)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Frekvens** | Setter frekvensen filteret fjerner. Alt over og under passerer gjennom. Still den inn på en brumming eller resonans for å kutte den ut. | 20 Hz til 20 kHz (60 Hz) |
| **Resonans** | Styrer hvor bredt kuttet er. Lave verdier skoper ut et bredt område; hev den for å fjerne bare et punktbånd og la resten være urørt. | 0,1 til 10 (8.0) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Mains Hum 60** | Fjerner 60 Hz elektrisk brumming (nordamerikansk nettstrøm). Et nøytralt utgangspunkt. |
| **Mains Hum 50** | Fjerner 50 Hz elektrisk brumming (europeisk og annen nettstrøm). |
| **Rumble** | Kutter en lavfrekvent rumling eller resonans uten å tynne ut hele bunnen. |
| **Mud** | Skoper ut lavmellomtone-grums for en renere, klarere lyd. |
| **Boxy** | Fjerner en boksete mellomtone-tuting. |
| **Harsh** | Temmer en hard, gjennomtrengende topp i de øvre mellomtonene. |

### Peaking (parametrisk EQ-bånd)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Frekvens** | Senteret i båndet som skal forsterkes eller kuttes. Sveip den for å finne frekvensen du vil forme. | 20 Hz til 20 kHz (1 kHz) |
| **Gain** | Hvor mye som skal forsterkes eller kuttes i senteret. Positivt løfter båndet; negativt skoper det ut. | -15 til +15 dB (0) |
| **Q-faktor** | Setter hvor bredt båndet er. Lave verdier former et bredt område; høye verdier snevrer inn for kirurgiske, punktnøyaktige endringer. | 0,1 til 10 (1.0) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Presence** | Et bredt øvre mellomtoneløft for klarhet og tilstedeværelse. Et nøytralt utgangspunkt. |
| **Warmth** | Et bredt lavmellomtoneløft som gir kropp og varme. |
| **Vocal Boost** | Løfter kjernevokalområdet for å bringe stemmer fram. |
| **Cut Mud** | Skoper ut boksete lavmellomtone-grums for en renere lyd. |
| **Tame Harsh** | Et smalt kutt for å temme en hard, gjennomtrengende topp. |
| **Punch** | Et lavt løft som gir trøkk og slagkraft til det lave området. |
| **Sub Boost** | Et dypt løft helt i bunnen for ekstra sub-bass-tyngde. |
| **Air** | Et bredt løft i toppen for en åpen, luftig glans. |
| **Clarity** | Løfter de høye mellomtonene for å gi definisjon og kant. |
| **De-Ess** | Et smalt kutt i sibilansområdet for å temme harde S-lyder. |
| **De-Boom** | Kutter en drønnete lavfrekvent oppbygging for et strammere lavområde. |
| **Scoop** | Et bredt mellomtonedropp for en senket, moderne tone. |

### Low Shelf (basskontroll og bassforsterkning)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Frekvens** | Setter hjørnet under hvilket hyllen trer i kraft. Alt under det forsterkes eller kuttes sammen. | 20 til 2000 Hz (200) |
| **Gain** | Hvor mye det lave området skal løftes eller senkes. Positivt gir tyngde og varme; negativt tynner det ut. | -15 til +15 dB (0) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Warmth** | Et skånsomt lavområdeløft for varme og kropp. Et nøytralt utgangspunkt. |
| **Bass Boost** | Et solid løft av bassen for tyngde og trøkk. |
| **Fullness** | Fyller ut de lave mellomtonene for en fyldigere, rundere lyd. |
| **Trim Bass** | Et beskjedent kutt for å lette en basstung miks. |
| **Cut Lows** | Et sterkt kutt for å tynne ut eller de-drønne det lave området. |
| **Big Bottom** | Et stort lavområdeløft for maksimal tyngde og rumling. |

### High Shelf (diskantkontroll)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Frekvens** | Setter hjørnet over hvilket hyllen trer i kraft. Alt over det forsterkes eller kuttes sammen. | 1 til 20 kHz (8 kHz) |
| **Gain** | Hvor mye det høye området skal løftes eller senkes. Positivt gir lyshet og luft; negativt jevner ut og gjør mørkere. | -15 til +15 dB (0) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Presence** | Et skånsomt høyområdeløft for klarhet og detalj. Et nøytralt utgangspunkt. |
| **Air** | Åpner opp den aller øverste for en luftig, åpen lyd. |
| **Bright** | Et sterkt løft for en skarp, lys, framtredende tone. |
| **Soften** | Et beskjedent kutt for å ta kanten av hard diskant. |
| **Tame Highs** | Et sterkt kutt for å gjøre en altfor lys lyd mørkere og jevnere. |
| **Sparkle** | Et stort topp-løft for maksimal skimmer og glans. |

### Soft Clip (varm metning)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Drive** | Skyver signalet hardere inn i bølgeformeren. Lave mengder gir skånsom varme; høye mengder runder toppene til tykk metning og grus. | 0 til 40 dB (0) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Warm** | Et snev av drive for skånsom, analog-lignende varme. |
| **Drive** | Merkbar metning som tykner og farger lyden. |
| **Crunch** | Tung drive med en hørbar knasende kant. |
| **Fuzz** | Tykk, lodden forvrengning. Toppene er klemt hardt. |
| **Destroy** | Maksimal drive. Aggressiv, fullt mettet grus. |

### Bit Crusher (retro lo-fi)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Bitdybde** | Setter hvor mange bit som beskriver hvert sample. Færre bit betyr grovere trinn og mer kvantiseringsstøy, for en knasende, grusete digital lyd. | 1 til 16 bit (16) |
| **Samplingsfrekvens** | Nedsampler lyden. Ved hundre prosent er frekvensen urørt; senk den for å holde hvert sample lenger, noe som demper diskanten og legger til en hard, aliasert kant. | 1 % til 100 % (100 %) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Vintage** | Et subtilt fall i kvalitet, som en tidlig digital sampler. |
| **LoFi** | Klassisk 8-bit, halv-rate lo-fi. Kornete og retro. |
| **Crunch** | Tyngre knusing med en hørbar knasende kant. |
| **Gritty** | Grov og grusete. Trinnene mellom nivåene er tydelige. |
| **Destroy** | Ekstrem reduksjon. Hard, brutt, knapt gjenkjennelig. |

### Ring Modulator (metalliske og robotiske toner)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Bærer** | Setter frekvensen til tonen signalet multipliseres med. Noen få hertz gir en tremolo-vaklng; høyere frekvenser gir metalliske, bjellelignende og robotiske overtoner. | 1 til 4000 Hz (440) |
| **Miks** | Blander den modulerte lyden inn med originalen. Ved null prosent hører du bare det tørre signalet; ved hundre prosent bare den fullt modulerte tonen. | 0 % til 100 % (0 %) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Tremolo** | En svært lav bærer gjør den til en amplitude-tremolo, som vakler volumet. |
| **Robot** | En medium bærer legger til klangende overtoner for en klassisk robotstemme-effekt. |
| **Metallic** | Tette, inharmoniske overtoner for en hard, metallisk tone. |
| **Bell** | En høyere bærer gir lyst, bjellelignende ringing. |
| **Alien** | Helt våt med en høy bærer. Ekstrem, fremmed, knapt gjenkjennelig. |

### Tremolo (volum-vaklng)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Hastighet** | Setter hvor raskt volumet pulserer. Tregere hastigheter gir en jevn vugging; raskere hastigheter gir en rask stotring. | 0,1 til 20 Hz (5) |
| **Dybde** | Setter hvor mye volumet faller på hver puls. Ved null prosent er nivået jevnt; ved hundre prosent dipper det helt ned til stillhet. | 0 % til 100 % (0 %) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Gentle** | En sakte, grunn vugging. Subtil bevegelse uten å trekke oppmerksomhet. |
| **Classic** | Den klassiske forsterker-tremoloen: en medium hastighet og moderat dybde. |
| **Deep** | En sterk, dyp puls som nesten faller til stillhet hver syklus. |
| **Fast** | En rask flagring for en skimrende, nervøs følelse. |
| **Chop** | Raskt og full dybde. En hard, stotrende chop. |

### Delay (ekko)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Tid** | Setter mellomrommet før hvert ekko. Korte tider gir en tett slapback; lengre tider sprer gjentakelsene lenger fra hverandre. | 0,01 til 2 s (0.25) |
| **Tilbakekobling** | Setter hvor mye av hvert ekko som mates tilbake. Lave verdier gir en enkelt gjentakelse; høyere verdier bygger en lang, etterslepende serie ekkoer. | 0 til 0.95 (0.4) |
| **Miks** | Blander ekkoene inn med originalen. Ved null prosent hører du bare det tørre signalet; ved hundre prosent bare ekkoene. | 0 % til 100 % (0 %) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Slapback** | Et enkelt kort ekko, tett mot originalen. Rockabilly og vokal-dobling. |
| **Echo** | Det klassiske ekkoet: en klar gjentakelse med noen få etterslepende haler. |
| **Ping** | En rask, sprettende gjentakelse som gir rytmisk bevegelse. |
| **Ambient** | Lengre, mykere gjentakelser som vaskes ut i en romslig hale. |
| **Dub** | Høy tilbakekobling for lange, dubbete kaskader av ekko. |
| **Cavern** | Lange, dype gjentakelser, som lyd som ekker gjennom et enormt rom. |

### Stereo Width (smalne eller utvide)

| Kontroll | Hva den gjør | Område (standard) |
|---|---|---|
| **Bredde** | Smalner eller utvider stereobildet. Null prosent kollapser til mono, hundre prosent lar det være urørt, og høyere verdier skyver sidene bredere. Påvirker bare stereospor på Alle-kanaler-målet. | 0 % til 200 % (100 %) |

| Forhåndsinnstilling | Hva den gjør |
|---|---|
| **Wide** | En skånsom utvidelse som åpner opp stereobildet. Et nøytralt utgangspunkt. |
| **Wider** | En sterkere spredning for et stort, oppslukende stereofelt. |
| **Max** | Maksimal bredde. Svært bredt, men pass på mono-kompatibilitetsproblemer. |
| **Narrow** | Trekker sidene inn for et strammere, mer sentrert bilde. |
| **Focused** | Nesten sentrert, med bare et snev av stereo. |
| **Mono** | Fullt kollapset til mono. Begge høyttalere spiller samme signal. |

## Hvordan alt fungerer under panseret (enkel versjon)

- **Motorer:** du velger én i Innstillinger > Lydspiller > Avspillingsmotor: **Standard** (system), **Universal** (FFmpeg) eller **Sound FX** (**BASS™-motoren** fra [Un4seen Developments](https://www.un4seen.com/)). Motoren du velger avgjør hvilke formater som spilles, og effektene, equalizeren og DSP-kjeden kjører bare i Sound FX-motoren.
- **Formater:** BASS™-motoren legger til FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus og modul- (tracker-) musikk i tillegg til system- og FFmpeg-formatene.
- **Effekter:** equalizeren, compressoren og de fleste effektene bruker BASS™-effekttilleggene. Freeverb er Freeverb-romklangen. Chorus, Flanger og Distortion bruker klassiske DirectX-stil-effekter med sine egne kontroller.
- **Volumnormalisering:** en sanntids **EBU R128**-loudness-jevner (loudness-standarden brukt i kringkasting og strømming).
- **Crossfeed:** **bs2b (Bauer)**-crossfeeden, kjørt inne i BASS™-motoren.
- **DSP-kjede:** dine egendefinerte blokker, brukt i den eksakte rekkefølgen du setter, på alle kanaler eller bare én side.
- **Utgang:** du kan sette samplingsfrekvens, kanalantall og bufferstørrelse for å matche utstyret ditt.

Fordi alt dette kjører i sanntid mens musikken spilles, gjør effektene:

- Fungerer i **sanntid** på alt, inkludert skyfiler, strømmer og modulmusikk.
- **Endrer eller lagrer aldri** filene dine på nytt. Slå en effekt av, og originalen kommer tilbake.
- **Husker innstillingene dine** for hver effekt.
- Kan **blandes og kombineres** fritt, siden hver enkelt er separat.

## Enkle oppskrifter å prøve

**Daglig lytting**

- **Mer bass, rent:** Equalizer > Bass Booster, senk deretter Forforsterkeren 1 til 2 dB. Eller legg til en DSP Low Shelf på Bass Boost.
- **Jevnt volum over en blandet spilleliste:** Volumnormalisering > Standard, pluss Compressor > Soft.
- **Skånsom generell polering:** Compressor > Transparent, pluss Volumnormalisering > Light.
- **Klarere vokal:** Equalizer > Vocal Booster, eller en DSP Peaking-blokk på Vocal Boost.
- **Fyldigere lyd på små telefonhøyttalere:** Equalizer > Small Speakers.

**Hodetelefoner**

- **Finere, mindre slitsomt på hodetelefoner:** Crossfeed > Chu Moy eller Jan Meier.
- **Bredere lyd på hodetelefoner:** DSP Stereo Width > Wide, pluss Crossfeed > Chu Moy.
- **Fiks hardt panorerte 1960- og 1970-talls plater:** Crossfeed > Vintage Stereo.
- **Litt luft og rom:** Freeverb > Ambience, holdt lav, pluss Crossfeed > Subtle.

**Stille stunder og talelyd**

- **Senkvelds stille lytting:** Volumnormalisering > Night, pluss Compressor > Late Night.
- **Podkaster og lydbøker:** Compressor > Voice / Podcast, pluss Equalizer > Spoken Word.
- **Høyeste, jevneste lyd i en støyende bil:** Volumnormalisering > Strong, pluss Compressor > Heavy.

**Fikse problemer**

- **Tem et hardt, lyst opptak:** Equalizer > Treble Reducer, eller en DSP Peaking-blokk på Tame Harsh.
- **Fjern elektrisk brumming:** DSP-kjede > Notch > Mains Hum 60 (eller Mains Hum 50 i Europa).
- **Strammere, renere bass:** DSP High Pass > Tighten, for å kutte det drønnete lavområdet.
- **Mindre drønn i en basstung miks:** DSP Low Shelf > Trim Bass, eller Peaking > De-Boom.

**Kreativt og gøy**

- **Varm, romslig følelse:** Freeverb > Hall, holdt lav.
- **Drømmende, romslige gitarer:** Chorus > Wide, pluss Echo > Long.
- **Retro lo-fi:** DSP-kjede > Bit Crusher (LoFi) inn i Soft Clip (Warm).
- **Funky bevegelse på elektroniske spor:** Auto Wah > Funky, eller Phaser > Fast.
- **Klassisk jetfly-sveip:** Flanger > Jet.

## Vanlige spørsmål

{{% details title="Hvilken lydmotor bruker Flacbox?" closed="true" %}}
Du velger én avspillingsmotor i Innstillinger > Lydspiller: Standard (Apples systemmotor), Universal (FFmpeg-motoren) eller Sound FX (BASS™-motoren fra Un4seen Developments, un4seen.com). Motoren du velger avgjør hvilke filformater som spilles. Sound FX er den som spiller ekstra formater som FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus og MOD- eller tracker-musikk, og den er den eneste motoren som gir sanntidseffektene, 10-bånds equalizeren og DSP-kjeden. For å bruke effektene, sett avspillingsmotoren til Sound FX.
{{% /details %}}

{{% details title="Kan Flacbox spille MOD, XM, IT og annen tracker- eller modulmusikk?" closed="true" %}}
Ja. BASS™-motoren har en innebygd modulspiller som laster MOD-, XM-, IT-, S3M-, MTM-, UMX- og MO3-filer og bygger sangen opp igjen i sanntid fra dens mønstre og instrumentlyder, slik tracker-musikk er ment å spilles. Vanlige iPhone-spillere kan ikke gjøre dette. Effekter og equalizeren fungerer på modulmusikk også.
{{% /details %}}

{{% details title="Støtter Flacbox DSD og filer med høy oppløsning?" closed="true" %}}
Ja. Flacbox spiller DSD-filer (DSF og DFF) gjennom BASS™-motoren ved hjelp av DSD over PCM slik at de fungerer på vanlig utgangsmaskinvare, pluss FLAC, WavPack, Monkey's Audio (APE), Musepack og TrueAudio for tapsfri avspilling.
{{% /details %}}

{{% details title="Hvilke lydeffekter har Flacbox?" closed="true" %}}
En 10-bånds equalizer, volumnormalisering, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate og Crossfeed, pluss en lag-din-egen DSP-kjede med filtre, hyller, gain, soft clip, bit crusher, ring modulator, tremolo, delay og stereobredde. Hver enkelt er separat og kan kombineres med de andre.
{{% /details %}}

{{% details title="Hva er en forhåndsinnstilling?" closed="true" %}}
En forhåndsinnstilling er en ferdiglaget innstilling for en effekt. I stedet for å flytte skyvekontroller selv, trykker du på en forhåndsinnstilling og lyden endres for å matche. Hver effekt i Flacbox har flere forhåndsinnstillinger, og denne guiden lister opp hva hver enkelt gjør. Hvis du flytter en skyvekontroll etter å ha valgt en forhåndsinnstilling, viser effekten «Manuell» for å fortelle deg at den nå bruker dine egne verdier.
{{% /details %}}

{{% details title="Hvordan åpner jeg lydeffektene i Flacbox?" closed="true" %}}
Åpne Nå spilles-spilleren, trykk på ⋯ (Flere handlinger)-knappen, og velg Lydeffekter. Eller gå til Innstillinger > Lydspiller > Lydeffekter. Trykk på en effekt, slå på bryteren, og velg en forhåndsinnstilling, eller åpne skyvekontrollene for å finjustere.
{{% /details %}}

{{% details title="Hvor er equalizeren, og hva er de beste innstillingene?" closed="true" %}}
Gå til Innstillinger > Lydspiller > Lydequalizer. Den har 10 bånd fra 32 Hz til 16 kHz, hvert fra -12 til +12 dB, pluss en -24 til +24 dB Forforsterker og 22 forhåndsinnstillinger. For mer bass, bruk Bass Booster. For klarere stemmer, bruk Vocal Booster eller Pop. For en lysere lyd, bruk Treble Booster. Juster deretter enkeltbånd etter smak.
{{% /details %}}

{{% details title="Hvordan forsterker jeg bassen i Flacbox?" closed="true" %}}
To enkle måter. I Lydequalizeren, velg Bass Booster (eller hev 32 Hz- og 64 Hz-båndene noen få dB). Eller, i Signalbehandling, legg til en Low Shelf-blokk satt til Bass Boost. I begge tilfeller, senk Forforsterkeren eller legg til en Gain-blokk 1 til 2 dB slik at bassen holder seg ren og ikke forvrenges.
{{% /details %}}

{{% details title="Hvilken equalizer-forhåndsinnstilling er best for musikken min?" closed="true" %}}
Rock og Electronic gir energi med sterk bass og diskant. Acoustic, Jazz og Classical holder seg varme og naturlige. Pop og Vocal Booster skyver stemmer fram. Bass Booster og Hip-Hop gir tyngde. Deep og Loudness høres fyldigere ut ved lavt volum. Start med den som matcher sjangeren din, og finjuster deretter.
{{% /details %}}

{{% details title="Hva er volumnormalisering, og hvordan er den forskjellig fra ReplayGain?" closed="true" %}}
Den får hvert spor til å spille på omtrent samme loudness. Den måler den virkelige loudnessen ved hjelp av EBU R128-standarden (i LUFS, som strømmetjenester) og justerer hvert spor mot målet ditt, med en maks-forsterkning-grense. I motsetning til ReplayGain trenger den ingen tagger i filene dine og fungerer på enhver kilde, i sanntid, uten å endre lyden. Forhåndsinnstillinger: Light, Standard, Strong og Night.
{{% /details %}}

{{% details title="Hva er Crossfeed, og bør jeg bruke den?" closed="true" %}}
Crossfeed blander litt av venstre og høyre kanal sammen slik at hodetelefoner føles mer som virkelige høyttalere og mindre som om lyden sitter fast i hodet ditt. Den er bare for hodetelefoner, så slå den av for høyttalere. Flacbox bruker bs2b (Bauer)-metoden, med forhåndsinnstillinger som Chu Moy og Jan Meier.
{{% /details %}}

{{% details title="Hva er forskjellen mellom Compressor og volumnormalisering?" closed="true" %}}
Volumnormalisering matcher loudnessen mellom ulike sanger. Compressor jevner ut de høye og stille delene inne i én enkelt sang. De løser ulike problemer og fungerer godt sammen, spesielt i en bil eller på et støyende sted.
{{% /details %}}

{{% details title="Hva er Signalbehandling (DSP)-kjeden?" closed="true" %}}
Det er et lag-din-egen rack i Innstillinger > Lydspiller > Signalbehandling. Legg til blokker som filtre, hyller, gain, soft clip, bit crusher, ring modulator, tremolo, delay og stereobredde, sett dem i hvilken som helst rekkefølge, slå hver enkelt på eller av, og rett kjeden mot alle kanaler, venstre eller høyre. Fordi rekkefølgen betyr noe, kan du designe akkurat den lyden du vil ha.
{{% /details %}}

{{% details title="Hva er forskjellen mellom Equalizeren, effektene og DSP-kjeden?" closed="true" %}}
Equalizeren er en enkel 10-bånds tonekontroll. Lydeffektene er ferdiglagde verktøy (compressor, romklang, ekko og så videre) med forhåndsinnstillinger. DSP-kjeden er der du bygger din egen effektrekkefølge fra individuelle blokker. Du kan kjøre alle tre samtidig.
{{% /details %}}

{{% details title="Endrer eller skader effektene musikkfilene mine?" closed="true" %}}
Nei. Alt brukes i sanntid mens musikken spilles. Filene dine endres eller lagres aldri på nytt. Slå en effekt av, og den opprinnelige lyden kommer tilbake med én gang.
{{% /details %}}

{{% details title="Kan jeg bruke mer enn én effekt samtidig?" closed="true" %}}
Ja. Hver effekt har sin egen bryter og det er ingen hovedbryter, så enhver kombinasjon fungerer. For eksempel volumnormalisering pluss Compressor for jevn lytting, eller Freeverb pluss Crossfeed på hodetelefoner, med equalizeren på toppen.
{{% /details %}}

{{% details title="Hvorfor er effektkontrollene nedtonet?" closed="true" %}}
Effekten er slått av. Slå på bryteren øverst i redigeringsprogrammet for å bruke kontrollene. Hver effekt er av som standard.
{{% /details %}}

{{% details title="Hva betyr Manuell-etiketten?" closed="true" %}}
Det betyr at du flyttet en skyvekontroll bort fra en forhåndsinnstilling, så effekten bruker nå dine egne tilpassede verdier i stedet for en navngitt forhåndsinnstilling. Hver skyvekontroll har en tilbakestillingsknapp, og å velge en forhåndsinnstilling igjen erstatter de manuelle verdiene dine.
{{% /details %}}

{{% details title="Kan jeg lagre og dele equalizer-forhåndsinnstillingene mine?" closed="true" %}}
Ja. I tillegg til de 22 innebygde forhåndsinnstillingene kan du lage dine egne, endre rekkefølge på dem, og eksportere eller importere dem for å flytte innstillingene dine til en annen enhet.
{{% /details %}}

{{% details title="Fungerer effektene med CarPlay, strømming og bakgrunnsavspilling?" closed="true" %}}
Ja. Effektene kjører inne i BASS™-motoren, så de gjelder lokale filer, skydisker, medieservere, strømmer og modulmusikk, og de fortsetter å fungere under CarPlay og bakgrunnsavspilling.
{{% /details %}}

{{% details title="Kan jeg endre lydutgangskvaliteten?" closed="true" %}}
Ja. I Innstillinger > Lydspiller kan du sette utgangs-samplingsfrekvensen, antall kanaler og bufferstørrelsen for å matche hodetelefonene, høyttalerne eller DAC-en din.
{{% /details %}}

{{% details title="Hva er et godt utgangsoppsett for hodetelefoner?" closed="true" %}}
Slå på volumnormalisering (Standard), legg til en lett Compressor (Soft), velg en equalizer-forhåndsinnstilling du liker, og slå på Crossfeed (Chu Moy eller Jan Meier). La romklang, ekko og forvrengning være av med mindre du vil ha en kreativ lyd.
{{% /details %}}

---

*BASS er et varemerke for Un4seen Developments Ltd. Se [un4seen.com](https://www.un4seen.com/). Crossfeed bruker bs2b (Bauer stereophonic-to-binaural)-algoritmen; se [bs2b-prosjektsiden](https://bs2b.sourceforge.net/).*
