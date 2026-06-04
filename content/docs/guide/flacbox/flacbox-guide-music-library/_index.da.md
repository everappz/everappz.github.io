---
title: "Musikbibliotek"
date: 2020-02-01
description: "Lær, hvordan du bygger, organiserer og synkroniserer dit musikbibliotek i Flacbox på iPhone, iPad og Mac. Tilføj numre manuelt eller synkronisér fra cloud-tjenester, administrér metadata, albumcovers, afspilningslister, favoritter, seneste og bogmærker. Inkluderer Hi-Res-lydunderstøttelse, MusicBrainz-tags-editor, online og offline-synkronisering og personaliseringsmuligheder."
keywords: [
  "Flacbox musikbibliotek", "synkronisér musik fra skyen", "organiser musikmetadata",
  "rediger lydtags Flacbox", "offline musiksynkronisering", "importér lokal musik",
  "Flacbox afspilningslistehåndtering", "søg albumcovers Flacbox",
  "musikmetadata iPhone", "Flacbox appvejledning",
  "Flacbox MusicBrainz", "normaliser tags Flacbox",
  "hi-res musikbibliotek Flacbox", "FFmpeg bibliotek Flacbox",
  "soloalbum Flacbox", "komponistvisning Flacbox"
]
tags: ["musik", "vejledning", "flacbox", "bibliotek"]
readingTime: 11
---


Det er nemt at administrere dit musikbibliotek med Flacbox, hvor du ubesværet kan organisere alle dine numre — lokale FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE og snesevis af andre formater — i én søgbar samling. Du har to muligheder for at bygge dit musikbibliotek: manuel tilføjelse (du vælger præcis, hvad der tilføjes) eller automatisk synkronisering (Flacbox scanner udpegede cloud-mapper og tilføjer nye filer automatisk, efterhånden som de vises).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Musikbibliotek Album-visning" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Manuel Tilføjelse

For manuelt at tilføje numre skal du trykke på ikonet **Tilføj musik** i øverste venstre hjørne og vælge mapper eller filer fra en tilsluttet cloud-lagringstjeneste eller filer på din enhed. Når du tilføjer numre til biblioteket, oprettes der kun links til disse numre — de faktiske filer forbliver på deres originale placeringer for at spare værdifuld diskplads. Hvis du ønsker at gøre numre tilgængelige offline, kan du bruge handlingen Download fra indstillingsmenuen eller aktivere Offline-tilstand for afspilningslister og nummers samlinger.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Tilføj sange til musikbiblioteket" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Du kan også trække og slippe filer til biblioteket på Mac-versionen eller bruge **Åbn filer…** / **Åbn mappe…** fra systemfilvælgeren på iPhone og iPad.

## Fortsæt Afspilning

Gendan afspillerkøen fra den sidst gemte position, hvis denne funktion er aktiveret i applikationsindstillingerne. Aktivér både **Gem lydafspillerens tilstand** og **Gem afspilningsposition** i Indstillinger → Lydafspiller → Generelt for den bedste oplevelse. Når aktiveret, vises en knap **Fortsæt afspilning** øverst på alle mapper, album, kunstner-, genre- og afspilningslisteskærme — tryk på den for at hoppe direkte tilbage til den præcise sang og position, du sidst forlod.

## Placeringer

Alle numre i dit bibliotek er tankevækkende grupperet efter kildetype og musik-tags. Du kan filtrere sange efter placering ved at bruge knappen **Flere handlinger** i øverste højre hjørne og vælge **Filtrer**.

### Online musik

Denne sektion viser musik fra dine tilsluttede cloud-lagringstjenester. Numrene her streames efter behov; intet optager lokalt lager, medmindre du eksplicit downloader eller aktiverer offline-tilstand.

### Filer i Denne Applikation

Her kan du finde musik tilgængelig til offline afspilning, der stammer fra dine lokale filer. Det inkluderer filer i appens Documents-mappe — alt hvad du har downloadet, overført via Wi-Fi Drive eller importeret via Finder-fildeling.

### Filer på Denne iPhone / iPad / Mac

Denne kategori inkluderer musik importeret til applikationen fra din enhed, tilføjet via systemdialogen **Åbn filer…**. De originale filer forbliver på deres originale placering; Flacbox beholder kun et link til dem.

## Kategorier

Når du tilføjer numre til dit musikbibliotek, læser appen automatisk deres lyd-tags og organiserer dem i kategorier som Sange, Ikke-afspillede sange, Album, Albumkunstnere, Kunstnere, Genrer og Komponister.

## Tags-gruppering

Disse kategorier hjælper dig med at organisere dine numre efter musik-tags. Når du tilføjer numre til musikbiblioteket, læser appen deres metadata og grupperer dem efter disse kategorier. Hvis du ikke kan se alle dine album, skal du sikre, at appen har skannet hvert nummer. Du kan tjekke scanningsprocessen i Indstillinger → Musikbibliotek → Metadatalæsning → Antal behandlede filer i musikbiblioteket. For lokale filer kan du også genskanne offline-mapper i Indstillinger → Musikbibliotek → Offline-mappers synkronisering → Start scanning af lokale mapper. Når metadatalæseren fuldfører alle operationer, vil du se følgende kategorier i dit musikbibliotek:

- **Sange** — alle sange grupperet efter TRACK_TITLE-tagget. Du kan tjekke sorteringsrækkefølgen ved hjælp af menuen Flere handlinger i øverste højre hjørne.
- **Ikke-afspillede sange** — alle sange, der aldrig er blevet afspillet.
- **Album** — sange grupperet efter ALBUM_NAME-tagget, ignorerer kunstner-, albumkunstner- og komponist-tags. Hvis du har flere album med samme navn men af forskellige kunstnere, kan du overveje at bruge sorteringen Eksklusive album beskrevet nedenfor.
- **Albumkunstnere** — sange grupperet kun efter ALBUM_ARTIST_TAG. Nyttigt til at holde kompilationer og samarbejder tydeligt adskilt fra soloarbejde.
- **Kunstnere** — sange grupperet kun efter ARTIST_TAG.
- **Genrer** — sange grupperet efter GENRE-tagget.
- **Komponister** — sange grupperet efter COMPOSER-tagget — uvurderlig for klassiske musikbiblioteker, hvor 'komponist' er den primære navigationsakse.

## Favoritter

Du kan markere sange som favoritter på lydafspillerens skærm eller ved hjælp af indstillingsmenuen. Favoritter vises i deres egen sektion, så du kan finde dem med ét tryk.

## Seneste

Denne sektion viser alle nyligt afspillede numre. Du kan tilpasse, hvor mange elementer listen over seneste beholder i Indstillinger → Bibliotek → Seneste → Ændre listestørrelse, og eksportere listen til M3U / CSV / TXT for at sikkerhedskopiere din lyttehistorik.

## Bogmærker

Du kan oprette lydbogmærker, mens en sang afspilles, og administrere dem på denne skærm — perfekt til lydbøger, lange mixsæt, forelæsninger eller bare at markere omkvædet på et yndlingsnummer. Detaljerede instruktioner til arbejde med lydbogmærker er tilgængelige [her](/docs/guide/evermusic/evermusic-guide-music-library).

## Øverste Værktøjslinje

Den øverste værktøjslinje, der er placeret lige under navigationslinjen, tilbyder flere praktiske handlinger: Søg, Afspil alt, Bland alt og Fortsæt afspilning. Du kan afsløre eller skjule denne værktøjslinje med et simpelt swipe-ned-gestus.

## Søg

Søgefunktionen giver dig mulighed for at finde et bestemt nummer, kunstner, album eller genre i dit musikbibliotek. På søgeskærmen har du adgang til handlingerne Sortér, Filtrer og Gitter / Listevisning. Søgningen kører lokalt mod musikbibliotekets database, så den fungerer fuldt offline og returnerer resultater, efterhånden som du skriver.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Musikbibliotek-søgning" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Indstillingsmenu

Hvert nummer i dit musikbibliotek har en menu med flere handlinger, der er tilgængelig ved at trykke på knappen med tre prikker ved siden af sangtitlen. Disse handlinger varierer afhængigt af, om det er en enkelt sang eller en del af en samling.

### For Individuelle Sange

- **Afspil næste** — tilføjer sangen øverst i afspillerkøen.
- **Afspil senere** — tilføjer sangen til bunden af afspillerkøen.
- **Føj til afspilningsliste** — tilføjer sangen til en afspilningsliste.
- **Føj til favoritter** — markerer sangen som en favorit for hurtig adgang.
- **Downloade** — gemmer sangen til lokale filer. Den vises i fanen **Lokale filer** og i sektionen **Offline musik**.
- **Redigere lydtags** — åbner den indbyggede lydtags-editor til at rette manglende metadata; bemærk, at dette vil ændre sangen i dit lager.
- **Vis i mappe** — afslører mappen, hvor lydfilen er gemt.
- **Vis i Finder** — for filer importeret fra din Mac afslører denne handling mappen, hvor lydfilen er placeret på din Mac.
- **Åbn med** — eksporterer lydfilen til en anden app.
- **Slet fra cloud-tjeneste** — fjerner filen fra både musikbiblioteket og cloud-lageret. **Denne handling er irreversibel.**
- **Slet fra musikbibliotek** — sletter sangen fra dit musikbibliotek, men filen forbliver i lageret. Hvis automatisk synkronisering er aktiveret og filen eksisterer på fjernlageret, vil den genoptræde i dit bibliotek efter en synkroniseringsoperation.

### For Sangsamlinger

For sangsamlinger som Album, Kunstnere, Genrer eller Komponister inkluderer indstillingsmenuen følgende handlinger.

- **Afspil alt** — erstatter afspillerkøen med sange fra den valgte samling.
- **Afspil næste** — tilføjer sangene fra denne samling øverst i afspillerkøen.
- **Afspil senere** — tilføjer sangene fra denne samling til bunden af afspillerkøen.
- **Føj til afspilningsliste** — inkluderer sange fra denne samling i en afspilningsliste, med mulighed for at oprette en ny.
- **Aktivere offline-tilstand** — downloader sange fra denne samling til lokale filer. Filer vises i fanen **Lokale filer** og i sektionen **Offline musik**. Hvis nye elementer tilføjes til samlingen på serveren, downloades de automatisk.
- **Rediger billede** — skift albumcover for sangsamlingen.
- **Føj til arkiv** — pakker hele samlingen ind i én ZIP-fil til nem sikkerhedskopiering eller overførsel (Premium-funktion).
- **Eksportér sangliste** — eksportér samlingen til M3U, CSV eller TXT til brug i andre afspillere eller til arkivering.
- **Slet fra musikbibliotek** — fjerner sangsamlingen fra dit musikbibliotek. Denne handling sletter ikke de faktiske filer fra lageret. Hvis automatisk synkronisering er aktiveret og filerne eksisterer på fjernlageret, vil de genoptræde i dit bibliotek efter en synkroniseringsoperation.

## Markeringstilstand

Du kan aktivere markeringstilstand ved at bruge knappen Flere handlinger i øverste højre hjørne. I denne tilstand kan du vælge flere numre på én gang og udføre batchhandlinger — tilføje til afspilningsliste, markere som favorit, slette fra bibliotek, downloade og mere.

## Albumdetaljer

Når du åbner sektionerne Kunstner, Albumkunstner eller Komponist, kan du se en skifter for Sange / Alle album / Eksklusive album / Solo-album.

- **Sange** — viser alle sange, hvor denne kunstner / albumkunstner / komponist vises i lyd-tags.
- **Alle album** — viser kompilationsalbum og alle album, hvor kunstneren er til stede.
- **Eksklusive album** — viser album, hvor den angivne kunstner er den eneste kunstner med det albumnavn.
- **Solo-album** — viser album, hvor kun den angivne kunstners numre vises, selv om andre kunstnere har album med det samme navn.

Dette er særligt nyttigt til at rydde op i rodede 'Diverse artister'-kompilationer i store biblioteker.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Albumdetalje-skærm" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Indstillinger

Tryk på Flere handlinger → Indstillinger for at konfigurere dine musikbibliotekets præferencer.

### Metadatalæsning

Når du tilføjer numre til biblioteket, går metadatalæseren i gang. Denne baggrundsproces læser alle metadata fra dine numre og organiserer dem efter Kunstner, Album, Genre og Komponist. Du kan justere hastigheden for metadatalæsning for at indlæse data hurtigere — vær opmærksom på, at hurtigere læsning bruger mere energi. Du kan også deaktivere metadatalæseren fuldstændigt og vise filnavne i stedet for tag-oplysninger.

Metadatalæseren **opdaterer kun metadata i dit musikbibliotek** og ændrer ikke filer gemt på din cloud-konto eller lokalt lager. Brug den indbyggede **tags-editor** via den tilsvarende handling i indstillingsmenuen til at redigere metadata i selve lydfilerne.

### Tilgængelige Tilstande for Metadatalæseren

- **Deaktiveret** — metadatalæseren er slukket og filnavne vises i stedet for lydtags-data.
- **Aktuel sang** — applikationen læser metadata kun for den aktuelt afspillede sang. Brug denne mulighed, hvis du har en langsom netværksforbindelse for at forhindre metadatalæseren i at sende mange anmodninger til cloud-serveren, hvilket kan forårsage afspilningsafbrydelser.
- **Afspilningskø** — appen læser metadata for alle sange i lydafspillerens kø.
- **Bibliotek** — appen læser metadata for alle sange i musikbiblioteket.

Når kontakten **Metadatalæsning i baggrunden** er tændt, fortsætter metadatalæseren med at arbejde i baggrundstilstand. Bemærk, at hvis appen forbruger meget energi under lydafspilning, kan iOS-operativsystemet suspendere den.

Hvis du har en stor musiksamling, anbefales det at udføre metadatasynkronisering på desktopversionen af applikationen og derefter overføre det synkroniserede musikbibliotek til iOS ved hjælp af **Sikkerhedskopiering og gendannelse**.

Når **Normaliser metadatakodning** er aktiveret, normaliserer appen automatisk metadatakodning for alle sange. Dette retter ødelagte tags-kodninger (f.eks. efter redigering af filer på en Windows-pc) og forhindrer forkerte tegn i at vises i nummersoplysninger.

Handlingen **Genindlæse metadata** markerer alle filer i dit musikbibliotek som manglende metadata, hvilket udløser metadatalæseren til at opdatere alle poster.

Tryk på **Start metadatalæsning** for at starte læseren manuelt. Operationsforløbet vises nedenfor.

### Online Synkronisering

Automatisk online musiksynkronisering tilføjer numre fra tilsluttede cloud-tjenester til musikbiblioteket automatisk. For at aktivere det skal du åbne musikbibliotekets indstillinger og vælge synkroniseringsmapper.

Med denne mulighed aktiveret scanner applikationen de valgte mapper, identificerer understøttede lydfiler og tilføjer dem til dit bibliotek. Start eller stop synkronisering med den tilsvarende menuhandling.

Online synkronisering kører kun, når appen er i forgrunden, så synkronisering af et stort bibliotek kan tage noget tid. For at fremskynde tingene skal du holde Flacbox åben, tilslutte din enhed til strøm og aktivere **Indstillinger → Skærm → Altid aktiv**.

Alternativt kan du udføre online synkronisering på desktopversionen af appen og overføre resultatet til iOS ved hjælp af **Sikkerhedskopiering og gendannelse**.

Du kan også vælge, hvor ofte online synkronisering kører. Indstilling af intervallet til **Straks** udløser en synkronisering, hver gang du åbner applikationen.

### Offline Synkronisering

Konfigurér offline musiksynkronisering.

#### Synkroniserede offline mapper

Når du markerer en online mappe på din cloud-server som tilgængelig offline (ved hjælp af menuen **Flere handlinger**), vises den her. Mappeindholdet downloades til **Lokale filer → Offline mapper**. Når onlinemappen ændres (filer tilføjet, fjernet eller opdateret), tjekker appen for ændringer og opdaterer den lokale kopi på din enhed.

På denne skærm kan du manuelt starte offline-mappesynkronisering, afsløre offline-mappen i dens overordnede mappe og deaktivere offline-tilstand for mappen. Deaktivering af offline-tilstand fjerner alle lokale kopier af filer fra din enhed.

#### Tidsinterval

Vælg, hvor ofte appen kontrollerer offline-mapper for ændringer.

#### Start Scanning af Lokale Mapper

Scanner alle lokale mapper i applikationens **Documents**-mappe for understøttede lydfiler. Fundne filer tilføjes automatisk til musikbiblioteket. Filer på din enhed uden for applikationens Documents-mappe skal tilføjes til musikbiblioteket manuelt, da appen ikke kan få adgang til dem på grund af iOS / macOS-sikkerhedsbegrænsninger.

**Vigtigt:** Det anbefales at starte offline musiksynkronisering med jævne mellemrum for at holde dit musikbibliotek opdateret med dine lokale filer.

### Personalisering

I denne sektion kan du konfigurere stilen på musikbiblioteksskærmen. Tre muligheder er tilgængelige: Simpel menu, Grupperet menu, Menu med faneblade. Du kan også aktivere eller deaktivere visning af albumcovers på albumdetaljeskærme.

### Albumcovers

Konfigurér, hvordan applikationen indlæser og gemmer albumcovers.

- **Netværkstype** — vælg **Wi-Fi** eller **Wi-Fi og mobildata** til cover-downloads.
- **Indlæs albumcovers til online filer** — når aktiveret, indlæses indlejrede albumcovers for filer gemt i cloud-lageret. Dette kan bruge yderligere netværksdata.
- **Søg i mappen** — når aktiveret, hvis et nummer ikke har et indlejret cover, søger appen efter JPEG- eller PNG-billeder i den samme mappe og bruger dem som albumcover.
- **Coverkvalitet** — vælg kvaliteten af albumcovers gemt på din enhed.
- **Vis i mappe** — åbn mappen, hvor albumcovers er cachelagret.
- **Slet alle** — slet cachelagrede albumcovers for at frigøre lager og tvinge appen til at genindlæse dem efter behov.

### Afspilningslister

Aktivér muligheden for at tilføje den samme sang til en afspilningsliste to gange. Som standard er denne mulighed deaktiveret.

### Seneste

Administrér din liste over nyligt afspillede sange.

- **Slet liste** — slet hele listen over nyligt afspillede sange.
- **Ændre listestørrelse** — angiv antallet af elementer, der vises på listen.
- **Eksportér sangliste** — eksportér din liste over nyligt afspillede sange som M3U, CSV eller TXT. Detaljerede instruktioner er tilgængelige [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritter

Administrér listen over dine yndlingssange.

- **Simultan redigering** — når aktiveret, tilføjer tilføjelse af en sang til favoritter den til både musikbiblioteket og filsektionen simultaneously.
- **Slet liste** — slet hele listen over yndlingssange.
- **Eksportér sangliste** — ligesom Seneste, eksportér favoritter som M3U, CSV eller TXT.

### Slet Bibliotek

Denne handling sletter musikbibliotekets database. Dine musikfiler i lageret efterlades urørte.

### Indholdslæsningsgrænse

Som standard bruger applikationen paginering til at fremskynde indlæsning af indhold. Du kan deaktivere paginering for at indlæse alt på én gang. For at gøre det skal du åbne applikationsindstillingerne, rulle ned til Personalisering → Indholdslæsningsgrænse og vælge Deaktiveret.
