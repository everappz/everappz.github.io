---
title: "Indstillinger"
date: 2020-02-01
description: "Udforsk alle indstillinger i Flacbox — fra afspilningspræferencer, FFmpeg / system lydmotor, Hi-Res lydoutput, equalizer-justeringer, tonejustering, IO-buffertid, metadatasynkronisering, afspilningslistekontrol, filoverførsler, startskærmwidgets, Apple CarPlay, UI-personalisering, sprog, adgangskode, sikkerhedskopiering og gendannelse, og Premium-opgradering."
keywords: [
  "Flacbox indstillinger", "lydafspillerkonfiguration", "Premium-opgradering Flacbox",
  "WiFi Drive", "metadatasynkronisering", "equalizer", "afspilningshastighed",
  "afspilningslistedubletter", "filhåndteringsindstillinger", "offline musiksynkronisering",
  "lydtags-editor", "mørk tilstand", "gendan køb", "sikkerhedskopieringsindstillinger",
  "Flacbox widget-indstillinger", "Flacbox CarPlay-indstillinger",
  "Flacbox FFmpeg-indstillinger", "Flacbox samplingfrekvensindstillinger",
  "Flacbox tonejusteringsindstillinger", "Flacbox IO-buffer",
  "Flacbox adgangskode", "Flacbox sprog", "Flacbox personalisering",
  "Flacbox analytics"
]
tags: ["guide", "flacbox", "indstillinger"]
readingTime: 16
---


Indstillingsskærmen er kontrolcentret for Flacbox. Herfra kan du opgradere til Premium, konfigurere lydmotoren (systemkodeks eller FFmpeg), administrere dit musikbibliotek, konfigurere filhåndtering, tilpasse lydtags-editoren, aktivere startskærmswidgets og Apple CarPlay, sikkerhedskopiere dine data og tilgå hjælp og juridiske oplysninger. Sektioner er grupperet under overskrifter: Køb og opdateringer, Appræferencer, Hjælp og Juridisk og privatliv.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox indstillingers hovedskærm" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Opgradering til Premium

Opgrader applikationen til Premium-versionen for at fjerne alle begrænsninger. Den gratis version tilbyder et engangskøb til livstids brug og to abonnementsmuligheder (1 måned og 1 år) for at fjerne alle begrænsninger og opgradere til Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox opgradering til Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Familiedeling** er aktiveret for alle køb og planer, så du kan dele Premium-versionen med op til fem familiemedlemmer uden ekstra omkostninger.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox vælg en Premium-plan" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Du kan læse mere om køb og Premium-versionen her: [Hvad er forskellen mellem Flacbox og Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Deling af køb mellem iOS og Mac

Livstidskøb og abonnementer deles mellem iOS og Mac ved hjælp af iCloud til synkronisering af disse oplysninger. Hvis du har Premium-versionen på din iOS-enhed, skal du sørge for, at du har den seneste version installeret, og at iCloud er aktiveret. Start appen på iOS og vent et minut, så dine købsoplysninger kan uploades til iCloud.

Du kan også prøve at trykke på knappen Gendan køb i appindstillingerne. Installer derefter den seneste appversion fra App Store på din Mac og start appen. Sørg for, at du har en internetforbindelse og bruger den samme iCloud- og App Store-konto på Mac, som du brugte på iOS. Vent et minut, så appen kan downloade købsoplysninger fra iCloud — Premium-versionen skulle automatisk aktiveres på din Mac.

## Gendannelse af køb på en ny enhed

For at gendanne dit køb på en ny enhed skal du bruge menuen Køb → Gendan køb. Du vil se listen over dine køb. Hvis du ikke kan se alle, skal du bekræfte, at enheden er tilsluttet det samme Apple ID, der blev brugt til at foretage købene, og sørge for, at iCloud er aktiveret.

## Prøv Premium gratis

Du kan opgradere til Premium-versionen gratis i en begrænset periode ved hjælp af denne menu. Se bare en reklame eller fortæl dine venner om appen for at få Premium gratis.

## Køb

Du kan gendanne tidligere køb fra denne menu. Hvis du støder på aktiveringsfejl, kan du prøve at aktivere indstillingen Gendan køb ved appstart.

## Softwareopdatering

Tryk på Softwareopdatering for at kontrollere, om en nyere version af Flacbox er tilgængelig. Appen sammenligner din installerede version med den seneste version i App Store og fortæller dig, om en opdatering anbefales.

## Nyheder

Denne menu er tilgængelig efter frigivelse af en ny version. Den viser en oversigt over ændringerne og de nye funktioner i den seneste opdatering.

## Lydafspiller

Denne sektion konfigurerer lydafspilleren og den underliggende lydmotor, herunder FFmpeg / systemkodeksvalget og Hi-Res lydoutputmuligheder.

### Generelt

Disse indstillinger dækker de grundlæggende aspekter af lydafspilleren — afspilningskøen, lydoutput og gemning af afspillerens tilstand.

- **Gentagelsestilstand** — vælg, hvordan lydafspilleren opfører sig, når et nummer slutter:
  - **Gentag alle** — afspiller alle numre i din kø igen.
  - **Gentag ét** — gentager kun det aktuelle nummer.
  - **Stop gentag** — sætter afspilning på pause, når det aktuelle nummer slutter.
  - **Ingen gentagelse** — lader din kø afspille uden gentagelse.
- **Blandingstilstand** — tilfældigiserer rækkefølgen af numre i din kø. Du kan slå det **Bland fra** eller **Bland til**.
- **Lydkodeks** — vælg den lydmotor, der bruges til afspilning:
  - **Systemkodeks + FFmpeg** — prioriterer systemets lydkodeks, hvor det er muligt, og forbedrer kompatibilitet og stabilitet. Tonejustering og lydudgangssamplingfrekvens kan være begrænset.
  - **FFmpeg** — tvinger FFmpeg-kodeksen for alle lydfiler og låser op for tonejustering og lydudgangssamplingfrekvens.
- **Lydudgangssamplingfrekvens** — juster lydudgangssamplingfrekvensen for at optimere lydkvaliteten, særligt nyttig med en ekstern DAC. Tilgængelige værdier: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** og **96 kHz**.
- **Antal lydudgangskanaler** — for multikanals lydsystemer med en ekstern DAC skal du angive antallet af kanaler: Mono, Stereo, Center / Venstre / Højre, Center / Venstre / Højre / Surround, ITU BS.775-1, 5.1 Surround og SDDS.
- **Foretrukken IO-buffertid for lydudgang** — konfigurer input-/outputbuffertiden. En typisk værdi for at minimere latens under afspilning af lyd med høj opløsning er ca. **5 millisekunder (0,005 sekunder)**. Test forskellige varigheder på din målenhed for at finde den bedste balance mellem lav latens og fejlfri afspilning.
- **Lydudgangstilstand (kun iOS)** — konfigurer blandet lydudgangstilstand, så lyd fra Flacbox blandes med andre applikationer. Detaljerede instruktioner er [her](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Gem afspilningsposition** — gemmer og gendanner afspilningspositionen for sange i dit musikbibliotek.
- **Gem lydafspillertilstand** — bevarer lydafspillerens tilstand, inden du lukker appen, og gør det nemt at genoptage fra, hvor du slap.

Når du har aktiveret både **Gem afspilningsposition** og **Gem lydafspillertilstand**, skal du åbne en vilkårlig mappe, album, kunstner eller genre, og du vil se en knap **Fortsæt afspilning** øverst på skærmen.

### Personalisering

Personalisering giver dig mulighed for at tilpasse udseendet af lydafspillerskærmen, ændre de tilgængelige kontroller på hovedskærmen, låseskærmen og statuslinjen og konfigurere spring-tid-kontroller.

- **Lydafspillerskærmstil** — konfigurer placeringen af elementer på lydafspillerskærmen.
- **Albumbilledernes scrollstil** — konfigurer den foretrukne scrollstil for albumbilleder.
- **Yderligere elementer** — aktiver ekstra elementer på lydafspillerskærmen. Lydformatinfo viser det aktuelt afspillede nummers lydinfo over coverbilledet; Lydstyrkeindstilling viser lydudgangsindstillingen under afspilningskontrollerne.
- **Handlinger på hovedskærmen** — konfigurer hvilke knapper der som standard skal være synlige på lydafspillerens hovedskærm: gentagelses- og blandingstilstand, næste og forrige sang, spring tid, søvntimer, Google Chromecast, AirPlay og Bluetooth, lydequalizer, søg, bogmærker, hastighed, tilføj bogmærke, føj til favoritter, kommentarer og mere.
- **Afspilningskontroller på låseskærmen** — vælg hvilke kontroller der vises på låseskærmen. Mulige værdier: spring tid, tilføj bogmærke, føj til favoritter.
- **Spring tid-knapper** — vælg tidsintervallet for spring tid-knapperne.

### Filindlæsning

Under filindlæsning kan du ændre den netværkstype, der bruges til at indlæse sange. Tilgængelige muligheder: **Wi-Fi**, **Wi-Fi og mobildata**.

- **Forudindlæsningstid** — indstil buffertidsintervallet. Forøg dette, hvis du har en dårlig netværksforbindelse.
- **Brug direkte URL** — når det er aktiveret, bruges en direkte URL til at indlæse sangen, hvis serveren understøtter det. Dette kan fremskynde sangindlæsning, men kan påvirke afspilningsstabiliteten.

### Lydequalizer

Konfigurer 10-bånds lydequalizer, forudindstillinger og forstærker. Du kan læse mere om konfiguration af lydequalizeren [her](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Afspilningshastighed

Juster afspilningshastigheden for lydafspilleren fra **0,02× til 3,00×**. Tryk på konfigurationsikonet i øverste højre hjørne for at skifte til **præcis tilstand** for finere justeringer.

### Tonejustering

Skift tonejusteringsindstillinger ved hjælp af de foruddefinerede værdier, eller skift til **præcis tilstand** ved at trykke på knappen i øverste højre hjørne. Tonejustering er tilgængelig i FFmpeg-kodekstien med et interval fra **-1000 til +1000**.

### Afspilningscache

Sange i lydafspillerens kø downloades automatisk for at sikre problemfri afspilning. Hvis du downloader lydfiler manuelt, kan du deaktivere dette for at undgå dubletter. Du kan også konfigurere lydafspillerens cachestørrelse her.

### Søvntimer

Aktiver en timer til automatisk at stoppe afspilning efter en specificeret periode. Tryk på konfigurationsikonet i øverste højre hjørne for **præcis tilstand** med minut-for-minut-granularitet.

## Bibliotek

Dine musikbiblioteksindstillinger — automatisk synkronisering, metadatalæsning, albumcoverindlæsning, afspilningslister, seneste og favoritter — befinder sig her.

### Metadatalæsning

Når du tilføjer numre til biblioteket, begynder **metadatalæseren** at arbejde. Denne baggrundsproces læser alle metadata fra dine numre og organiserer dem efter Kunstner, Album, Genre og Komponist. Du kan justere hastigheden for metadatalæsning for at indlæse data hurtigere (på bekostning af mere batteri). Du kan også deaktivere metadatalæseren og vise filnavne i stedet for tagoplysninger.

Metadatalæseren **opdaterer kun metadata i dit musikbibliotek** og ændrer ikke filer gemt i din cloudkonto eller lokale lager. For at redigere metadata i selve lydfilerne skal du bruge den indbyggede **tag-editor** via den tilsvarende handling i valgmenuen.

Når **Metadatalæsning i baggrunden** er slået til, fortsætter læseren med at arbejde i baggrundstilstand. Hvis appen bruger for meget energi under lydafspilning, kan iOS suspendere den.

Hvis du har en stor musiksamling, skal du udføre metadatasynkronisering på desktopversionen af applikationen og overføre det synkroniserede musikbibliotek til iOS ved hjælp af **Sikkerhedskopiering og gendannelse**.

Når **Normaliser metadatakodning** er aktiveret, normaliserer appen automatisk kodningen af metadata for alle sange. Dette retter ødelagte tagkodninger (for eksempel efter redigering af filer på en Windows-pc) og forhindrer forkerte tegn i at vises i nummeroplysninger.

**Genindlæse metadata** markerer alle filer i dit musikbibliotek som havende manglende metadata, hvilket forårsager, at metadatalæseren opdaterer alle poster.

**Start metadatalæsning** udløser metadatalæseren manuelt. Fremskridt vises under handlingen.

### Online synkronisering

Automatisk online musiksynkronisering tilføjer numre fra tilsluttede cloudtjenester til musikbiblioteket automatisk. For at aktivere det skal du åbne musikbiblioteksindstillingerne og vælge synkroniseringsmapper.

Med denne mulighed aktiveret scanner applikationen de valgte mapper, identificerer understøttede lydfiler og tilføjer dem til dit bibliotek. Start eller stop synkronisering med den tilsvarende menuhandling.

Online synkronisering kører kun, når appen er i forgrunden, så synkronisering af et stort bibliotek kan tage et stykke tid. For at fremskynde tingene skal du holde Flacbox åben, tilslutte din enhed til strøm og aktivere **Indstillinger → Skærm → Altid aktiv**.

Alternativt kan du udføre online synkronisering på desktopversionen af appen og overføre resultatet til iOS ved hjælp af **Sikkerhedskopiering og gendannelse**.

Du kan også vælge, hvor ofte online synkronisering kører. Indstilling af intervallet til **Øjeblikkeligt** udløser en synkronisering, hver gang du åbner applikationen.

### Offline synkronisering

Konfigurer offline musiksynkronisering.

#### Synkroniserede offline mapper

Når du markerer en online mappe på din cloudserver som tilgængelig offline (ved hjælp af menuen **Flere handlinger**), vises den her. Mappeindholdet downloades til **Lokale filer → Offline mapper**. Når onlinemappen ændres (filer tilføjet, fjernet eller opdateret), kontrollerer appen for ændringer og opdaterer den lokale kopi på din enhed.

På denne skærm kan du manuelt starte offline mappesynkronisering, afsløre offline-mappen i dens indeholdende mappe og deaktivere offline-tilstand for mappen. Deaktivering af offline-tilstand fjerner alle lokale kopier af filer fra din enhed.

#### Tidsinterval

Vælg, hvor ofte appen kontrollerer offline mapper for ændringer.

#### Start scanning af lokale mapper

Scan alle lokale mapper i applikationens **Documents**-mappe for understøttede lydfiler. Fundne filer tilføjes automatisk til musikbiblioteket. Filer placeret på din enhed men uden for applikationens Documents-mappe skal tilføjes til musikbiblioteket manuelt, da appen ikke kan tilgå dem på grund af iOS / macOS-sikkerhedsbegrænsninger.

**Vigtigt:** Det tilrådes periodisk at starte offline musiksynkronisering for at holde dit musikbibliotek opdateret med dine lokale filer.

### Personalisering

Konfigurer musikbibliotekets skærmstil. Tre muligheder er tilgængelige: **Simpel menu, Grupperet menu, Fanebladsmenu**. Du kan også aktivere eller deaktivere albumbilleder på albumdetaljeskærmen.

### Albumbilleder

Konfigurer, hvordan applikationen indlæser og gemmer albumcovers.

- **Netværkstype** — vælg **Wi-Fi** eller **Wi-Fi og mobildata** for coverdownloads.
- **Indlæs albumbilleder for onlinefiler** — når det er aktiveret, indlæses indlejrede albumbilleder for filer gemt i cloudlagring. Dette kan bruge yderligere netværksdata.
- **Søg i mappen** — når det er aktiveret og et nummer ikke har noget indlejret cover, leder appen efter JPEG- eller PNG-billeder i samme mappe og bruger dem som albumcover.
- **Coverkvalitet** — vælg kvaliteten af albumbilleder gemt på din enhed.
- **Vis i mappe** — åbn mappen, hvor albumbilleder er cachet.
- **Slet alle** — slet cachede albumbilleder for at frigøre lager og tvinge appen til at genindlæse dem efter behov.

### Afspilningslister

Aktiver muligheden for at tilføje den samme sang til en afspilningsliste to gange. Som standard er denne mulighed deaktiveret.

### Seneste

Administrer din liste over nyligt afspillede sange.

- **Slet liste** — slet hele listen over nyligt afspillede sange.
- **Skift listestørrelse** — indstil antallet af elementer, der vises på listen.
- **Eksporter sangliste** — eksporter din liste over nyligt afspillede sange som M3U, CSV eller TXT. Detaljerede instruktioner er tilgængelige [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritter

Administrer listen over dine favoritssange.

- **Simultan redigering** — når det er aktiveret, tilføjer tilføjelse af en sang til favoritter den i både musikbiblioteket og filsektionen simultant.
- **Slet liste** — slet hele listen over favoritssange.
- **Eksporter sangliste** — som med Seneste, eksporter favoritter som M3U, CSV eller TXT.

### Slet musikbibliotek

Slet musikbiblioteksdatabasen. Dine musikfiler i lagringen forbliver uberørt.

## Adgangskode

Aktiver adgangskodeskærmen for at beskytte dine applikationsdata med en 4-cifret numerisk adgangskode. Når det er aktiveret, vil du blive bedt om at indtaste adgangskoden, hver gang appen starter. Kombiner den med iOS Face ID / Touch ID på enheden for ekstra beskyttelse.

## Filhåndtering

Sektionen Filhåndtering styrer, hvordan filer overføres, gemmes og forhåndsvises.

### Filoverførsler

Vælg din netværkspræference for download af filer til din enhed.

### Maksimalt antal parallelle opgaver

Indstil antallet af parallelle downloadtråde. Et højere tal fremskynder downloads men bruger mere batteri.

### Filoverførselsopgaver

Viser aktuelt aktive upload- og downloadopgaver.

### Baggrundsoverførsler

Tillad downloads, mens appen er i baggrunden. Hvis baggrundsoverførsler forbruger meget energi, kan iOS suspendere appen.

### Gem downloadede filer til

Vælg standarddownloadmappen, eller lad appen spørge dig hver gang.

### Synkroniserede offline mapper

Administrer offline synkronisering for valgte mapper. For at aktivere offline synkronisering skal du trykke på trepriks-knappen ved siden af en mappe og vælge **Tilgængelig offline-tilstand**. Nye filer tilføjet til cloudmappen downloades automatisk til din enhed. Læs mere om offline-tilstande [her](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Tidsinterval

Vælg, hvor ofte offline mapper synkroniseres. **Øjeblikkeligt** udløser en synkronisering, hver gang du åbner appen.

### Vis fulde filnavne

Vis komplette filnavne, inklusive udvidelser, i filhåndteringen.

### Rediger onlinefiler

Deaktiver online filredigering for at skifte til skrivebeskyttet tilstand for tilsluttede cloudtjenester og forhindre utilsigtede sletninger. Denne handling fjerner filredigeringsoperationer fra brugergrænsefladen.

### Kopier filer ved åbning

Angiv, hvordan appen håndterer importerede filer fra andre applikationer.

### Miniaturer for filer

Administrer og slet genererede filminiaturer for at frigøre lagerplads.

### Slet midlertidige filer

Ryd applikationens cachemappe for at genvinde lagerplads.

## Lydtags-editor

Konfigurer den indbyggede lydtags-editor — praktisk til batch-reparation af kunstner / album / år / genre / coverproblemerne på tværs af cloud- og lokale filer.

### Albumcover-skalering

Vælg den skaleringsmetode, der bruges, når et albumcover gemmes i lydtags.

### Opdater onlinefiler

Når det er aktiveret, opdaterer applikationen automatisk en fils metadata på cloudserveren, efter du er færdig med at redigere den.

### Slet fil efter online redigering

Vælg, om applikationen skal slette den downloadede kopi, efter at redigering af en onlinefil på en cloudserver er afsluttet.

### Knapper på hovedskærmen

Vælg, hvilke knapper der er synlige på lydtags-editorens hovedskærm.

For dybere batch-redigering af mange filer på én gang skal du installere vores ledsagerapp **Evertag**.

## Widgets

Aktiver widgets, så appen opdaterer widgetdata under afspilning. Widgetopdateringer kræver yderligere energi, så til/fra-knappen er slået fra som standard — aktiver den kun, hvis du faktisk bruger widgets på din startskærm eller låseskærm.

Du kan tilføje Flacbox-widgets ved at trykke og holde på din startskærm eller låseskærm, trykke på **+**, søge efter **Flacbox** og vælge en widgetstørrelse. Widgets viser det aktuelle coverbillede, nummertitel og kunstner og trykker direkte igennem til fuldskærmsafspilleren. Widgets fungerer også på macOS i Notifikationscenter.

## CarPlay

Skift CarPlay-indstillinger her. Denne menu er også tilgængelig inde i CarPlay-grænsefladen, så du kan justere oplevelsen under kørslen.

### Sorter

Konfigurer sorteringsmuligheder for alle CarPlay-skærme.

### Grænse for indlæsning af indhold

Vælg, om appen bruger paginering på CarPlay-skærmen. Paginering holder menuer responsive på store biblioteker.

### Menuikonernes gradientfarve

Vælg farvevalget for CarPlay-startskærmen.

### Vis billeder

Deaktiver billeder på CarPlay-skærmen for at optimere indlæsningshastigheden og reducere hukommelsesforbrug på store biblioteker.

### Sæt afspilning på pause ved tilslutning

Aktiver dette for at undgå pludselig høj lyd, når du tilslutter din enhed til CarPlay.

## Wi-Fi Drive

Aktiver **Wi-Fi Drive** for at overføre filer fra en computer til din enhed ved hjælp af en desktop-webbrowser, Finder eller File Explorer. Detaljerede instruktioner om, hvordan man bruger Wi-Fi Drive, er tilgængelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalisering

Tilpas brugergrænsefladen til dine præferencer.

### Appikon

Vælg et alternativt appikon til din startskærm (Premium).

### Farveskema

Vælg brugergrænsefladeens tema og aktiver mørk tilstand. Når **Standard** er valgt, følger applikationen enhedens systemdækkende udseendeindstillinger.

### Baggrundsstil

Modificer baggrundsstilen for applikationen. I øjeblikket er den eneste mulighed **Sløret albumcover**, som bruger det aktuelt afspillede nummers artwork som en sløret appbaggrund.

### Udseende af elementer på listen

Juster, hvordan elementer vises på lister. Nyttigt på små skærme — du kan lade appen justere rækkehøjden automatisk baseret på indhold, eller vise mindre ikoner i listeceller for at give tekst mere plads.

### Grænse for indlæsning af indhold

Som standard bruger applikationen paginering til at fremskynde indlæsning af indhold. Du kan deaktivere paginering for at indlæse alt på én gang.

### Skærmstil for lokale filer

Skift præsentationsstilen for sektionen **Lokale filer**.

### Musikbibliotekets skærmstil

Tilpas udseendet af skærmen **Musikbibliotek**.

### Lydafspillerens skærmstil

Konfigurer udseendet af skærmen **Lydafspiller**.

### Kontextmenustil

Vælg stilen på kontextmenuen, der vises, når du trykker på knappen **Flere handlinger**.

## Vindue

Tilgængeligt på Mac og Catalyst. Konfigurer vinduesrelaterede præferencer som standardstørrelse og adfærd ved opstart.

## Skærm

Vælg, om skærmen skal forblive aktiv, mens du bruger applikationen. Nyttigt ved scanning af store biblioteker eller ved langvarig tag-redigeringsarbejde.

## Tilgængelighed

Aktiver **Teksttilstand** for at skjule alle billeder i brugergrænsefladen. Teksttilstand aktiveres automatisk, når VoiceOver er aktiv, og er også nyttig til meget små eller kun-tekst-opsætninger.

## Sprog

Skift applikationssproget og tilsidesæt systemstandarden. Ændringen gælder, efter du fuldt ud afslutter og genåbner Flacbox. Aktuelt understøttede lokaliseringer inkluderer: Afrikaans, Akan, Albansk, Amharisk, Arabisk, Armensk, Assamesisk, Aymara, Aserbajdsjansk, Bambara, Bengalsk, Baskisk, Hviderussisk, Bosnisk, Bulgarsk, Burmesisk, Catalansk, Cebuanisk, Kinesisk (forenklet), Kinesisk (traditionelt), Korsikansk, Kroatisk, Tjekkisk, Dansk, Dhivehi, Dogri, Hollandsk, Engelsk, Esperanto, Estisk, Ewe, Filippinsk, Finsk, Fransk, Galisisk, Ganda, Georgisk, Tysk, Græsk, Guarani, Gujarati, Haitisk kreolsk, Hausa, Hawaiansk, Hebraisk, Hindi, Hmong, Ungarsk, Islandsk, Igbo, Ilocano, Indonesisk, Irsk, Italiensk, Japansk, Javanesisk, Kannada, Kasakhisk, Khmer, Kinyarwanda, Koreansk, Krio, Kurdisk, Kurdisk Sorani, Kirgisisk, Laotisk, Latin, Lettisk, Lingala, Litauisk, Luxembourgsk, Makedonsk, Maithili, Malagassisk, Malajisk, Malayalam, Maltesisk, Maori, Marathi, Mizo, Mongolsk, Nepalesisk, Nordlig Sotho, Norsk Bokmål, Nyanja, Odia, Oromo, Pashto, Persisk, Polsk, Portugisisk, Punjabi, Rumænsk, Russisk, Samoansk, Sanskrit, Skotsk gælisk, Serbisk, Shona, Sindhi, Sinhalesisk, Slovakisk, Slovensk, Somalisk, Sydlig Sotho, Spansk, Sundanesisk, Swahili, Svensk, Tadsjikisk, Tamil, Tatarisk, Telugu, Thailandsk, Tsonga, Tyrkisk, Turkmensk, Ukrainsk, Urdu, Uigurisk, Usbekisk, Vietnamesisk, Walisisk, Xhosa, Jiddisch, Yoruba, Zulu.

## Sikkerhedskopiering og gendannelse

Brug denne funktion til at sikkerhedskopiere alle dine applikationsdata eller migrere dem til en anden enhed. Du kan vælge, hvad du vil inkludere:

- **Database** — alle dine numre i musikbiblioteket, inklusive afspilningslister. Offline numre er ikke inkluderet for at holde sikkerhedskopifilstørrelsen håndterbar.
- **Albumbilleder** — alle dine cachede albumbilleder.
- **Indstillinger** — alle dine applikationsindstillinger.

Tryk på **Sikkerhedskopier applikationsdata** for at starte sikkerhedskopieringen. Applikationsdata skrives til en enkelt fil, som du kan bruge senere til at gendanne applikationstilstanden på en ny enhed eller efter geninstallation af applikationen.

For at gendanne applikationsdata på en ny enhed skal du flytte sikkerhedskopifilen til den nye enhed ved hjælp af en tilsluttet cloudtjeneste eller iCloud og åbne den på den nye enhed.

Detaljerede trin-for-trin-instruktioner: [Sådan overfører du dit musikbibliotek mellem enheder: Trin-for-trin-guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Hjælp

Tilgå applikationsguiden for assistance og vejledning til effektiv brug af appen.

## Ofte stillede spørgsmål

Find svar på almindelige spørgsmål i FAQ-sektionen.

## Send feedback

Har du feedback eller brug for assistance? Send din feedback til vores supportteam direkte fra appen.

## Del denne app

Del applikationen med dine venner for at sprede budskabet.

## Opdag flere apps

Udforsk andre apps fra Everappz.

## Vilkår og betingelser

Beskriver vilkårene og betingelserne for brug af applikationen. Læs dem venligst, inden du bruger applikationen.

## Privatlivspolitik

Besøg privatlivspolitiksiden for at forstå vores datahåndteringspraksis. Læs den venligst, inden du bruger applikationen.

## Analyse og dataindsamling

Kontrollér, hvilke tjenester der er aktiveret til analyse og dataindsamling, og deaktiver dem, du ikke ønsker.

## Juridiske meddelelser

Indeholder oplysninger om hvert bibliotek, der bruges i applikationen, sammen med appversionsnummeret og buildoplysninger.
