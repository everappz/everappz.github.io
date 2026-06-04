---
title: "Lydafspiller"
date: 2020-02-01
description: "Lær at bruge Flacbox lydafspiller på iPhone, iPad og Mac. Styr afspilning, administrer køer, konfigurer FFmpeg / system lydmotor, skift samplingfrekvens, tonejustering, IO-buffertid, equalizer, lydbogmærker, AirPlay 2, Google Cast, CarPlay, widgets og Mac-tastaturgenveje."
keywords: [
  "Flacbox afspillerguide", "lydafspillerindstillinger", "Flacbox equalizer",
  "AirPlay musikstreaming", "Google Cast musik", "lydbogmærker",
  "Flacbox afspilningskø", "Flacbox gentag og bland", "Flacbox lydstyrke",
  "macOS mini-afspiller", "VoiceOver musikapp",
  "FFmpeg Flacbox", "tonejustering Flacbox", "samplingfrekvens Flacbox",
  "ekstern DAC Flacbox", "surroundlyd Flacbox", "IO-buffer Flacbox",
  "afspilningshastighed Flacbox", "søvntimer Flacbox"
]
tags: ["guide", "flacbox", "afspiller"]
readingTime: 14
---


Lydafspilleren er appens hovedskærm, hvor du styrer musikken og de fleste afspilningsfunktioner. Det er også her Flacbox' hi-res lydmotor — bygget på systemkodeks plus det medfølgende **FFmpeg**-bibliotek — udfører det tunge arbejde. Lad os udforske, hvordan man bruger den.

## Adgang til lydafspilleren

Du kan komme til fuldskærmsafspilleren fra mini-afspillerbaren. På iPhone sidder mini-afspilleren i bunden af hovedskærmen. På iPad og Mac er den på venstre side. For at skjule mini-afspilleren på iPhone skal du trykke på den én gang og stryge ned. For at lukke fuldskærmsafspilleren helt skal du trykke på luk-knappen i nederste højre hjørne.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox lydafspillers hovedskærm" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Understøttede lydformater

Flacbox afspiller de mest populære lydformater — både Apples systemkodeks og mange yderligere formater håndteret af den medfølgende FFmpeg-motor:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Det dækker stort set alle moderne tabsgivende og tabsfrie formater, du sandsynligvis har i en personlig musiksamling.

## Afspilningskontroller

Nederst på afspillerskærmen ser du knapper til Afspil, Pause, Næste nummer og Forrige nummer. Der er også valgfrie knapper som Frem 30 sek og Tilbage 30 sek, som du kan aktivere i appindstillingerne (praktisk til lydbøger). Du kan spole hurtigt frem eller tilbage ved at holde Næste / Forrige knapperne nede. For at hoppe til en bestemt del af et nummer skal du trække afspilningsskyderen.

## Gentag og bland

Tryk på gentag-knappen for at skifte mellem gentagelsestilstande:

- **Gentag alle** — gentager alle numre i din kø.
- **Gentag ét** — gentager kun det aktuelle nummer.
- **Stop gentag** — sætter på pause, når det aktuelle nummer slutter.
- **Ingen gentagelse** — afspiller køen én gang uden gentagelse.

Brug knappen **Bland** til at tilfældigisere rækkefølgen af numre i køen.

## Lydstyrke

Åbn skærmen med lydindstillinger ved at trykke på lydikonet under afspilningskontrollerne for at få adgang til lydstyrkeknappen. Du finder også her knapper til **Google Cast** og **AirPlay**, så du hurtigt kan skifte afspilning til en anden enhed.

## Google Cast (Chromecast)

For Google Cast-brugere vises ikonet **Cast** nederst i afspilleren. Tryk på det for at vælge en enhed og starte streaming. Sørg for, at din enhed og Google Cast-modtageren er på det samme Wi-Fi-netværk. Bemærk: ikke alle lydformater er kompatible med Google Cast — nogle hi-res formater skal muligvis omkodes.

## AirPlay

For AirPlay skal du lede efter knappen **AirPlay** nederst i afspilleren. Tryk på den og vælg en enhed til streaming. Flacbox understøtter **AirPlay 2**, så du kan afspille til flere HomePods, Apple TV'er eller AirPlay-2-kompatible højttalere på samme tid.

## Lydequalizer

Flacbox inkluderer en **10-bånds equalizer** med iPod-stilede forudindstillinger. Tryk på Equalizer i lydstyrkevisningen, og skift den til med øverste højre hjørne. Du kan bruge forudindstillinger som Acoustic og Bass Booster, eller justere hvert frekvensbånd med skyderen. Lav dine egne forudindstillinger, gem dem under et vilkårligt navn, og øg den overordnede lydstyrke med forstærkeren. Vi har mere detaljerede instruktioner om, hvordan man bruger equalizeren [her](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox lydafspiller equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Afspillertilstandsværktøjslinje

For nogle afspillerstile er der en dedikeret værktøjslinje øverst i fuldskærmsafspilleren. Denne værktøjslinje huser tre nyttige knapper:

- **Søg** — find hurtigt et bestemt nummer i din afspillerkø.
- **Afspilningshastighedskontrol** — juster afspilningshastighed fra 0,02× til 3,00×. Perfekt til lydbøger, podcasts og foredrag. Tryk på Normal for at vende tilbage til standardhastighed.
- **Lydbogmærker** — opret flere bogmærker pr. nummer. Vi har fulde instruktioner om, hvordan man bruger bogmærker [her](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Afspillerkø

For at se din afspillerkø skal du trykke på kø-knappen på højre side af det aktuelle nummer. Hvert nummer i køen har flere handlinger — tryk på de tre prikker for at se dem. For at omarrangere et nummer i køen skal du bruge omarranger-indikatoren nær titlen og trække den til en ny position.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox afspilningskø" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Kommentarer / Sangtekster

For at se nummers kommentarer og indlejrede sangtekster samt LRC-filer skal du følge disse trin:

1. Åbn **Indstillinger**.
2. Gå til **Lydafspiller**.
3. Vælg **Personalisering**.
4. Tryk på **Knapper på hovedskærmen**.
5. Aktiver **Kommentarer**.

Tryk herefter på afspillerkø-knappen nederst på skærmen flere gange for at skifte fra coverbillede / kø-visning til kommentarvisningen. På skærmen Kommentarer skal du scrolle til højre for at skifte mellem **Kommentarer**, **Indlejrede sangtekster** og **LRC-filen**. Fulde instruktioner er tilgængelige [her](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox sangtekster og kommentarskærm" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Valgmenu

Hvert nummer i lydafspillerens kø har en menu med flere handlinger, tilgået ved at trykke på trepriks-knappen nær nummertitlen.

- **Afspil næste** — tilføjer nummeret til toppen af afspillerkøen.
- **Føj til afspilningsliste** — inkluderer nummeret i en afspilningsliste med mulighed for at oprette en ny.
- **Føj til favoritter** — markerer nummeret som en favorit for hurtig adgang.
- **Downloade** — gemmer nummeret til lokale filer og vises i fanen **Lokale filer** og afsnittet **Offline musik**.
- **Redigere lydtags** — åbner den indbyggede lydtags-editor til at rette manglende metadata og ændrer nummeret i dit lager.
- **Vis i mappe** — afslører mappen, hvor lydfilen er gemt.
- **Vis i Finder** — for filer importeret fra din Mac afslører dette mappen, hvor lydfilen er placeret på din Mac.
- **Åbn i** — eksporterer lydfilen til en anden app.
- **Slet fra kø** — fjerner det valgte nummer fra lydafspillerens kø.
- **Slette fra cloudtjeneste** — sletter nummeret fra både musikbiblioteket og cloudlagring. **Denne handling er irreversibel.**
- **Slette fra lokale filer** — sletter nummeret fra både musikbiblioteket og lokal lagring. **Denne handling er irreversibel.**
- **Slet fra musikbibliotek** — sletter nummeret fra dit musikbibliotek, mens filen bevares i lagringen.

De samme muligheder er tilgængelige for det aktuelt afspillede element i lydafspillerens kø, som du kan tilgå ved at trykke på ikonet **Flere handlinger** nær nummertitlen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox-indstillinger for et element i afspilningskøen" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Yderligere afspillerhandlinger

Tryk på knappen **Flere handlinger** "..." på venstre side af titlen på den aktuelt afspillende sang for at se yderligere handlinger.

- **Fortsæt afspilning** — genoptag fra, hvor du slap, inkl. kø og medieposition. Særligt nyttig til lydbøger. Aktiveres i appindstillingerne.
- **Søg** — find hurtigt et bestemt nummer i din lydafspillerkø.
- **Bogmærker** — vis din liste over oprettede lydbogmærker.
- **Kommentarer** — vis nummers kommentarer og indlejrede sangtekster samt LRC-filer. Fulde instruktioner [her](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Hastighed** — juster afspilningshastighed efter din smag.
- **Seneste** — tilgå en liste over nyligt afspillede sange.
- **Favoritter** — se din samling af favoriterede sange.
- **Lydequalizer** — aktiver lydequalizer.
- **Søvntimer** — indstil en timer til at stoppe afspilning efter et angivet interval. Fantastisk til de øjeblikke, hvor du vil sove til din musik.
- **Gem kø som afspilningsliste** — gem den aktuelle lydafspillerkø som en ny afspilningsliste.
- **Slet kø** — ryd din afspillerkø og stop afspilning.
- **Indstillinger** — tilgå lydafspillerindstillinger.
- **Hjælp** — find assistance og vejledning.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox lydafspiller – skærmen Flere handlinger" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Lydbogmærker

Denne funktion giver dig mulighed for at oprette flere bogmærker for numre i dit musikbibliotek — perfekt til lydbøger, foredrag, lange DJ-miks eller markering af omkvædet i et yndlingsnummer.

Sådan opretter du et nyt bogmærke:

- Begynd at afspille den ønskede sang.
- Åbn afspillerskærmen.
- Tryk på knappen **Bogmærker** på afspillertilstandsværktøjslinjen.
- Vælg **Tilføj bogmærke**.
- Vælg bogmærketid og tryk på **Færdig** i øverste højre hjørne.

Redigering af bogmærker for det aktuelle nummer er nemt: tryk på Rediger i øverste højre hjørne for at gå i redigeringstilstand. I denne tilstand kan du omarrengere bogmærker, slette dem, justere bogmærketid og ændre bogmærketitler. Mere detaljerede instruktioner om lydbogmærker er tilgængelige [her](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox lydbogmærkeskærm" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Seneste og favoritter

På afspillerskærmen skal du trykke på de tre prikker for at tilgå Seneste og Favoritter. I begge afsnit kan du søge efter sange, afspille alle, blande alle, eksportere listen og rydde listen. Vi har detaljerede instruktioner om, hvordan man eksporterer sanglister [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Tilslut din iPhone til din bil via USB eller trådløs Apple CarPlay, og Flacbox vises på din CarPlay-startskærm, klar til at afspille musik sikkert under kørslen. CarPlay-grænsefladen inkluderer dedikerede faner for Bibliotek, Forbindelser, Lokale filer og Indstillinger med afspilningskontroller, bland, gentag, kø-håndtering og lydequalizer — alt tilgængeligt uden at tage fat i din telefon. Konfigurer CarPlay-oplevelsen yderligere i Indstillinger → CarPlay — sorteringsmuligheder, paginering, farven på menuikonernes gradient, om billeder indlæses, og en mulighed for automatisk at sætte afspilning på pause, når CarPlay tilsluttes.

[Læs den fulde CarPlay-guide](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox på Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widgets på startskærmen (iPhone og iPad)

Flacbox understøtter iOS startskærm- og låseskærmswidgets, så du kan se og styre afspilning med ét blik. Sørg for, at Widgets er aktiveret i Indstillinger → Widgets → Aktiver widgets, tryk derefter længe på din startskærm eller låseskærm, tryk på **+**, søg efter **Flacbox**, og tilføj en widget. Widgetten opdateres under afspilning for at vise det aktuelle nummers coverbillede, titel og kunstner.

## Mini-afspillervindue (kun Mac)

Mac-brugere kan bruge en kompakt, altid-øverst mini-afspiller. Flyt din markør til det nederste højre hjørne af Flacbox-vinduet, tilpas det til den mindste størrelse, og tryk på skjulknappen. Hold det over hvert andet vindue ved at vælge Vindue → Vis vindue altid øverst i menulinjen — perfekt til at holde musikkontrollen synlig, mens du arbejder i en anden app.

## Tastaturgenveje (kun Mac)

For Mac-brugere er der en systemafspilningsmenu tilgængelig i statuslinjen med tastaturgenveje. Tryk for eksempel på mellemrumstasten for at Afspille / Sætte på pause. Genveje til Stop, Næste sang, Forrige sang, Spring tid, Gentag, Bland og Afspilningshastighed er også tilgængelige.

## Lydafspillerindstillinger

For at tilgå indstillinger skal du trykke på knappen Mere på afspillerskærmen og vælge Indstillinger. Her finder du flere afsnit som angivet nedenfor.

### Generelt

Disse indstillinger dækker de grundlæggende aspekter af lydafspilleren, herunder afspilningskøen, lydudgang og gemning af afspillerens tilstand.

- **Gentagelsestilstand** — vælg, hvordan lydafspilleren opfører sig, når et nummer slutter:
  - **Gentag alle** — afspiller alle numre i din kø igen.
  - **Gentag ét** — gentager kun det aktuelle nummer.
  - **Stop gentag** — sætter afspilning på pause, når det aktuelle nummer slutter.
  - **Ingen gentagelse** — lader din kø afspille uden gentagelse.
- **Blandingstilstand** — tilfældigiserer rækkefølgen af numre i din kø. Du kan slå det **Bland fra** eller **Bland til**.
- **Lydkodeks** — vælg den lydmotor, der bruges til afspilning:
  - **Systemkodeks + FFmpeg** — prioriterer systemets lydkodeks, hvor det er muligt, og forbedrer kompatibilitet og stabilitet. Tonejustering og justeringer af lydudgangssamplingfrekvens kan være begrænsede i denne tilstand.
  - **FFmpeg** — tvinger FFmpeg-kodeksen for alle lydfiler, så du kan finjustere tonejustering og lydudgangssamplingfrekvens.
- **Lydudgangssamplingfrekvens** — juster lydudgangssamplingfrekvensen for at optimere lydkvaliteten, særligt nyttig med en ekstern DAC. Tilgængelige værdier: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** og **96 kHz**.
- **Antal lydudgangskanaler** — for multikanals lydsystemer med en ekstern DAC skal du angive antallet af kanaler: **Mono, Stereo, Center / Venstre / Højre, Center / Venstre / Højre / Surround, ITU BS.775-1, 5.1 Surround** og **SDDS**.
- **Foretrukken IO-buffertid for lydudgang** — konfigurer input-/outputbuffertiden til lydafspilning. En typisk værdi for at minimere latens under afspilning af lyd med høj opløsning er ca. **5 millisekunder (0,005 sekunder)**. Den acceptable bufferstørrelse afhænger af dit hardware- og softwaremiljø, så test forskellige varigheder på din målenhed og vælg den, der bedst balancerer lav latens og fejlfri afspilning.
- **Lydudgangstilstand (kun iOS)** — konfigurer blandet lydudgangstilstand, så lyd fra Flacbox blandes med andre applikationer. Detaljerede instruktioner er [her](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Gem afspilningsposition** — sikrer, at applikationen gemmer og gendanner afspilningspositionen for sange i dit musikbibliotek.
- **Gem lydafspillertilstand** — bevarer din lydafspillers tilstand, inden du lukker appen. For at fortsætte afspilning skal du trykke på **Fortsæt afspilning** øverst i en vilkårlig mappe, album, kunstner eller genre, når du åbner appen igen. Du kan også gendanne afspilning for individuelle filer ved at trykke på det specifikke nummer.

Når du har aktiveret både **Gem afspilningsposition** og **Gem lydafspillertilstand**, skal du åbne en vilkårlig mappe, album, kunstner eller genre, og du vil se en knap **Fortsæt afspilning** øverst på skærmen sammen med det sidst gemte nummer og position. Tryk på den for at genoptage præcis, hvor du slap.

### Personalisering

Personalisering giver dig mulighed for at tilpasse udseendet af lydafspillerskærmen, ændre de tilgængelige kontroller på hovedskærmen, låseskærmen og statuslinjen og konfigurere spring-tid-kontroller.

- **Lydafspillerskærmstil** — konfigurer placeringen af elementer på lydafspillerskærmen.
- **Albumbilledernes scrollstil** — konfigurer den foretrukne scrollstil for albumbilleder.
- **Yderligere elementer** — aktiver ekstra elementer på lydafspillerskærmen. **Lydformatinfo** viser det aktuelt afspillede nummers lydinfo over coverbilledet; **Lydstyrkeindstilling** viser lydudgangsindstillingen under afspilningskontrollerne.
- **Handlinger på hovedskærmen** — konfigurer hvilke knapper der som standard skal være synlige på lydafspillerens hovedskærm: **Gentagelses- og blandingstilstand, Næste og forrige sang, Spring tid, Søvntimer, Google Chromecast, AirPlay og Bluetooth, Lydequalizer, Søg, Bogmærker, Hastighed, Tilføj bogmærke, Føj til favoritter, Kommentarer** og mere.
- **Afspilningskontroller på låseskærmen** — vælg hvilke kontroller der vises på låseskærmen. Mulige værdier: **Spring tid, Tilføj bogmærke, Føj til favoritter**.
- **Spring tid-knapper** — vælg tidsintervallet for knapperne **Spring tid**.

### Filindlæsning

Under filindlæsningsprocessen kan du ændre den netværkstype, der bruges til at indlæse sange. Tilgængelige muligheder: **Wi-Fi**, **Wi-Fi og mobildata**.

- **Forudindlæsningstid** — indstil buffertidsintervallet. Forøg dette, hvis du har en dårlig netværksforbindelse.
- **Brug direkte URL** — når det er aktiveret, bruges en direkte URL til at indlæse sangen, hvis serveren understøtter det. Dette kan fremskynde sangindlæsning, men kan påvirke afspilningsstabiliteten.

### Lydequalizer

Tilpas lydequalizerindstillingerne. Du kan læse mere om konfiguration af lydequalizeren [her](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Afspilningshastighed

Juster afspilningshastigheden for lydafspilleren fra **0,02× til 3,00×**. Tryk på konfigurationsikonet i øverste højre hjørne for at skifte til **præcis tilstand** for finere justeringer.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox afspilningshastighedsskærm" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Tonejustering

Skift tonejusteringsindstillinger ved hjælp af de foruddefinerede værdier. Du kan også skifte mellem foruddefinerede værdier og præcis tilstand ved at trykke på knappen i øverste højre hjørne. Tonejustering er tilgængelig i FFmpeg-kodekstien med et interval fra **-1000 til +1000**.

### Afspilningscache

Sange i lydafspillerens kø downloades automatisk for at sikre problemfri afspilning. Hvis du downloader lydfiler manuelt, kan du deaktivere denne mulighed for at undgå dubletter. Du kan også konfigurere lydafspillerens cachestørrelse her.

### Søvntimer

Aktiver en timer til automatisk at stoppe afspilning efter en specificeret periode — praktisk, når du vil falde i søvn til musik. Tryk på konfigurationsikonet i øverste højre hjørne for **præcis tilstand** med minut-for-minut-granularitet.

## Tilgængelighed

Flacbox er fuldt tilgængeligt med **VoiceOver**. Hver komponent har en veldesignet etiket og beskrivelse. Når VoiceOver er aktiv, skifter appen til **Teksttilstand**, så kun meningsfulde elementer vises — forbedring af navigationshastighed og klarhed. Du kan også aktivere Teksttilstand i **Indstillinger → Tilgængelighed → Teksttilstand**.

### Justering af skydere med VoiceOver

1. **Vælg skyderen** — stryg til venstre eller højre, indtil VoiceOver annoncerer den.
2. **Juster værdien** — dobbeltryk og hold skyderen, træk derefter op eller ned for hurtigt at ændre værdien. VoiceOver annoncerer den nye værdi, efterhånden som du går frem.

### Justering af nummers position på en liste med VoiceOver

1. Tryk på ikonet for omarranger-indikatoren nær nummertitlen for at give det fokus.
2. Dobbeltryk hurtigt på omarranger-indikatoren. Ved andet tryk skal du ikke slippe fingeren — hold den, indtil du hører en lyd, der indikerer, at cellen er klar til at blive flyttet.
3. Flyt cellen til dens nye position.

Andre komponenter fungerer som forventet ved hjælp af systemleverede VoiceOver-mønstre.
