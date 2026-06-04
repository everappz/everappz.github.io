---
title: "Indstillinger"
date: 2020-01-01
description: "Udforsk alle indstillinger i Evermusic, herunder lydkonfiguration, synkronisering af musikbibliotek, offline mapper, metadata, personalisering, tilgængelighed, widgets, CarPlay og sikkerhedskopieringsindstillinger."
keywords: [
  "Evermusic", "indstillinger", "lydindstillinger", "synkronisering af musikbibliotek",
  "offline mapper", "equalizer", "crossfade", "afspilning uden pauser",
  "lydprocessor", "indstillinger for afspilningsliste", "premium-opgradering",
  "gendan køb", "filhåndtering", "tags-editor", "WiFi-drev",
  "voiceover", "app-sikkerhedskopi", "tilgængelighed", "lokalisering",
  "widgets", "CarPlay", "rumlig lyd", "lydtone"
]
tags: ["evermusic", "guide", "settings"]
readingTime: 16
---


Indstillingsskærmen er kontrolcenteret i Evermusic. Herfra kan du opgradere til Premium, konfigurere lydafspilleren, administrere dit musikbibliotek, konfigurere filhåndteringen, tilpasse grænsefladen, aktivere widgets og CarPlay, sikkerhedskopiere dine data og få adgang til hjælp og juridiske oplysninger. Sektioner er grupperet under overskrifter: **Køb og opdateringer**, apppræferencer, **Hjælp** og **Juridisk og privatliv**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Indstillingsskærm" image="/docs/guide/evermusic/evermusic-guide-settings/img/settings-main-screen.webp" >}}
{{< /cards >}}

## Køb og opdateringer

### Opgrader til Premium

Opgrader applikationen til Premium-versionen for at fjerne alle begrænsninger. Den gratis version tilbyder ét livslangt køb i appen og to abonnementsindstillinger, der låser op for hele funktionssættet.

Familiedeling er aktiveret for alle køb og planer, så du kan dele Premium-versionen med medlemmer af din familie.

Du kan læse mere om køb og Premium-versionen her: [Hvad er forskellen mellem Evermusic og Evermusic Premium](/docs/faq/evermusic/what-is-the-difference-between-evermusic-and-evermusic-premium/).

#### Evermusic Free (blåt ikon) vs Evermusic Pro (rødt ikon)

Evermusic udgives på App Store under to forskellige ikoner/farver:

- **Evermusic Free (blåt ikon)** er opdelt i **to separate App Store-apps med forskellige bundle-ID'er** — én til **iOS / iPadOS** og en dedikeret til **macOS** (Universal binary, der kører på både **Apple Silicon og Intel Mac**). Premium-køb i appen er **delt mellem iOS- og Mac-blåappsene via iCloud** — køb Premium på iPhone, og det aktiveres automatisk på Mac (og omvendt), så længe begge enheder bruger samme Apple ID med iCloud aktiveret.
- **Evermusic Pro (rødt ikon)** er en **enkelt App Store-app** med et **enkelt bundle-ID**, der kører på **iPhone, iPad og Apple Silicon Mac (M1 og nyere)**. Den har **samme funktionalitet som Evermusic Free med en aktiveret Premium-plan**. Den røde app **understøtter ikke Intel Mac**, hvilket er grunden til, at dens pris er lidt lavere end det tilsvarende Premium-køb i den blå app. Evermusic Pro **indsamler heller ikke nogen brugerdiagnostik eller analytics overhovedet** — analytics er fuldstændig deaktiveret i build'en uden mulighed for at tilmelde sig.

Da bundle-ID'erne er forskellige mellem blå og rød, låser et Premium-køb i appen aktiveret i den blå app ikke den røde app op gratis, og omvendt. Hvis du allerede bruger den blå app med Premium aktiveret, er der ingen grund til at installere den røde app — du har allerede alt, hvad Pro tilbyder.

### Deling af køb mellem iOS og Mac

Livstidskøb og abonnementer deles mellem iOS og Mac ved hjælp af iCloud. Hvis du allerede ejer Premium på iOS, skal du sørge for, at du har den nyeste version installeret, og at iCloud er aktiveret. Start appen på iOS og vent et minut, mens dine købsoplysninger uploades til iCloud.

Du kan også trykke på **Gendan køb** i appens indstillinger. Installer derefter den nyeste appversion fra App Store på din Mac og start appen. Sørg for, at du har en internetforbindelse og er logget ind med den samme iCloud- og App Store-konto på begge enheder. Vent et minut, mens appen downloader købsoplysninger fra iCloud. Premium-versionen bør aktiveres automatisk på din Mac.

### Gendan køb på en ny enhed

For at gendanne dit køb på en ny enhed skal du bruge **Køb → Gendan køb**. Du vil se en liste over dine køb. Hvis noget mangler, skal du bekræfte, at enheden er forbundet til den samme iTunes-konto, der blev brugt til at foretage købene, og at iCloud er aktiveret.

### Prøv Premium gratis

Du kan opgradere til Premium-versionen gratis i en begrænset periode ved hjælp af denne menu. Se en kort reklame eller del appen med venner for midlertidigt at låse Premium op.

### Køb

Gendan tidligere køb fra denne menu. Hvis du støder på aktivationsfejl, kan du prøve at aktivere indstillingen **Gendan køb ved appstart**.

### Softwareopdatering

Tryk på **Softwareopdatering** for at kontrollere, om en nyere version af Evermusic er tilgængelig. Appen vil sammenligne din installerede version med den nyeste version på App Store og fortælle dig, om en opdatering anbefales.

### Nyheder

Denne menu bliver tilgængelig, efter en ny version er udgivet. Den viser en oversigt over ændringerne og de nye funktioner inkluderet i den seneste opdatering.

## Indstillinger for lydafspiller

Alle indstillinger for lydafspilleren er grupperet her: equalizer, crossfade-afspilning, cache for lydafspiller, sangindlæsning og mere. Indstillingerne er organiseret i logiske undersektioner.

### Generelt

Denne undersektion indeholder generelle indstillinger for afspilningskø, lydoutput og gemning af tilstand.

#### Gentagelsestilstand

Angiver lydafspillerens adfærd, når et nummer afslutter afspilning:

- **Gentag alle** – gentager alle numre i din afspillerkø.
- **Gentag ét** – gentager kun det aktuelle nummer.
- **Gentag stop** – sætter afspilning på pause, når det aktuelle nummer slutter.
- **Ingen gentagelse** – lader din kø afspille igennem uden gentagelse.

#### Tilfældig tilstand

Afspiller numrene i tilfældig rækkefølge. Dette blander faktisk køen og afspiller numre ét efter ét i den nye rækkefølge. Tilgængelige værdier: **Tilfældig fra** og **Tilfældig til**.

#### Lydprocessor

Mulige værdier: **AVFoundation** og **CoreAudio**. Som standard bruges AVFoundation. På grund af et kendt problem med AVFoundation på iOS 17.0–17.6 kan crossfade-afspilning og lyd-equalizeren ikke bruges på samme tid. For at nyde både crossfade og equalizeren på disse iOS-versioner skal du skifte til CoreAudio-lydprocessoren.

Hvis du oplever problemer med afspilning uden pauser ved hjælp af AVFoundation, kan du også prøve CoreAudio. De eneste begrænsninger ved CoreAudio er internetstreaming af nogle radiostationer og visse lydformater, da den ikke understøtter alle systemlydformater (såsom M4A og et par andre).

#### Samplingshastighed for lydoutput

Indstil samplingshastigheden for lydoutput fra 8 KHz til 384 KHz. Denne indstilling er kun tilgængelig, når CoreAudio-processoren er valgt.

#### Antal kanaler for lydoutput

Indstil antallet af kanaler for lydoutput — **MONO** eller **STEREO**. Denne indstilling er kun tilgængelig, når CoreAudio-processoren er valgt.

#### Lydtonealgoritme

Vælg den algoritme, der bruges til tonekorrigering. Tilgængelige værdier er **Tidsdomæne**, **Spektral** og **Varispeed**. Nyttig, hvis du justerer afspilningshastighed og vil styre den resulterende lydkvalitet.

#### Rumlig lyd

Rumlig lyd bruger psykoakustiske metoder til at skabe en mere fordybende lydoplevelse på understøttede hovedtelefoner og højttaleropsætninger. Mulige værdier: **Deaktiveret**, **Mono og Stereo**, **Multikanal**, **Mono Stereo Multikanal**.

#### Lydoutputtilstand

Kun tilgængelig på iOS. Lader dig aktivere blandet tilstand, så lyd fra denne applikation blandes med andre applikationer. Du kan finde instruktioner om, hvordan du bruger blandet tilstand [her](/docs/howto/how-to-record-video-while-playing-music-on-iphone).

#### Gem afspilningsposition

Sikrer, at applikationen gemmer og gendanner afspilningspositionen for sange i dit musikbibliotek.

#### Gem lydafspillertilstand

Gemmer lydafspillertilstanden, inden applikationen lukkes, så det er nemt at genoptage fra det sted, du slap.

Når begge disse funktioner er aktiveret, skal du åbne en mappe, album, kunstner eller genre. Du vil se handlingen **Fortsæt afspilning** øverst på skærmen sammen med den sidst gemte sang og afspilningsposition. Tryk på **Fortsæt afspilning** for at gendanne. For at genoptage afspilning af en individuel fil skal du blot trykke på den fil.

### Personalisering

Tilpas udseendet af lydafspillerskærmen, vælg hvilke kontroller der er synlige på afspilleren, låseskærmen og statuslinjen, og konfigurer spring-tid-knapperne.

#### Stil for lydafspillerskærm

Konfigurer placeringen af værktøjslinjer og hovedkontroller på lydafspilleren.

#### Scrollestil for albumcovers

Vælg scrollestilen for albumcovers på lydafspillerskærmen.

#### Yderligere elementer

Aktivér ekstra elementer på lydafspillerskærmen. **Lydformatinfo** viser det aktuelt afspillende nummers tekniske info over kunstværket; **Lydvolumenskyder** viser lydoutputskyderen under afspilningskontrollerne.

#### Handlinger på hovedskærmen

Konfigurer hvilke knapper der er synlige på lydafspillerens hovedskærm. Tilgængelige muligheder inkluderer Gentag- og Tilfældig tilstand, Næste og Forrige sang, Springstid, Søvntimer, Google Chromecast, AirPlay og Bluetooth, Lyd-equalizer, Søg, Bogmærker, Hastighed, Tilføj bogmærke, Tilføj til favoritter, Kommentarer og mere.

#### Afspilningskontroller på låseskærmen

Vælg hvilke ekstra kontroller der er aktiveret på låseskærmen. Mulige værdier: **Springstid**, **Tilføj bogmærke** og **Tilføj til favoritter**.

#### Springstidsintervaller

Vælg de tidsintervaller, der bruges af fremad- og bagud-springstidsknapperne.

### Filindlæsning

Vælg den netværkstype, der bruges til at streame sange. Tilgængelige muligheder: **Wi-Fi** og **Wi-Fi og mobildata**.

#### Forudindlæsningstid

Indstil bufferingstidsintervallet. Øg denne værdi, hvis du har en dårlig netværksforbindelse.

#### Brug direkte URL

Når aktiveret, bruges en direkte URL til at indlæse sangen, hvis serveren understøtter det. Dette kan fremskynde sangindlæsning, men kan påvirke afspilningsstabiliteten en smule.

#### Optimer filindlæsning

Når aktiveret, optimerer systemet sangindlæsning for AVFoundation-lydprocessoren, hvilket kan forbedre afspilningsstabiliteten. Appen bruger den teknologi, der er beskrevet [her](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/).

### Lyd-equalizer

Konfigurer lyd-equalizeren. Du kan læse mere om forudindstillinger og EQ-konfigurationer [her](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Enheder

Opret forbindelse til en AirPlay- eller Google Chromecast-enhed (kun iOS).

### Afspilningshastighed

Juster afspilningshastigheden for lydafspilleren. For mere præcis kontrol skal du aktivere den præcise skyder ved at trykke på konfigurationsikonet i øverste højre hjørne.

### Crossfade-afspilning

Crossfade lader sange flyde problemfrit i et kontinuerligt mix — det næste sang begynder at afspille et par sekunder, før det aktuelle slutter. Crossfade er ikke tilgængeligt for AirPlay og Google Chromecast. På denne skærm kan du vælge, hvor længe det aktuelle og næste sang afspilles samtidigt. Hvis du oplever problemer med crossfade og lyd-equalizeren på samme tid, skal du skifte lydprocessoren som beskrevet ovenfor.

### Afspilning uden pauser

Afspilning uden pauser sikrer, at sange afspilles uden afbrydelse eller stilhed imellem. Det er perfekt til klassisk musik, liveoptagelser og konceptalbums. Hvis du har problemer med afspilning uden pauser, skal du skifte lydprocessoren som beskrevet ovenfor.

### Afspilningscache

Sange i lydafspillerkøen downloades automatisk for jævn afspilning. Hvis du downloader lydfiler manuelt, kan du deaktivere denne indstilling for at undgå dubletter. Du kan også konfigurere størrelsen på lydafspillerens cache her. Læs mere om offline-tilstand og afspilningscache her: [Afspil offline musik i Evermusic og Flacbox: Download og synkroniser fra cloud til lokale filer](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Søvntimer

Aktivér en timer til at stoppe afspilning efter en angivet timeout. For mere præcis kontrol skal du aktivere præcis tilstand ved at trykke på konfigurationsikonet i øverste højre hjørne.

## Bibliotek

Indstillinger for musikbibliotek — automatisk synkronisering, metadatalæsning, indlæsning af albumcovers, afspilningslister, seneste og favoritter — er her.

### Metadatalæsning

Når du tilføjer numre til biblioteket, behandler metadatalæseren dem i baggrunden og organiserer dem efter Kunstner, Album, Genre og Komponist. Du kan justere, hvor hurtigt metadata læses for at indlæse data hurtigere (på bekostning af mere batteri). Du kan også deaktivere metadatalæseren helt og vise filnavne i stedet for tag-oplysninger.

Metadatalæseren opdaterer kun musikbiblioteksdatabasen; den ændrer ikke filer gemt i din cloud-konto eller lokale lager. Hvis du skal redigere lydfilmetadata, skal du bruge den indbyggede tags-editor via den tilsvarende handling i indstillingsmenuen.

Når **Metadatalæsning i baggrunden** er aktiveret, fortsætter læseren med at arbejde i baggrundstilstand. Hvis appen bruger for meget energi under afspilning, kan iOS afbryde den.

Hvis du har en stor musiksamling, anbefales det at udføre metadatasynkronisering i desktopversionen af applikationen. Du kan derefter overføre det synkroniserede musikbibliotek til iOS ved hjælp af funktionen **Sikkerhedskopiér og gendan**.

Når **Normaliser metadatakodning** er aktiveret, normaliserer appen automatisk kodningen af metadata for alle sange. Dette løser problemer, hvor lydtag-kodning er ødelagt (f.eks. efter redigering af filer på en Windows-pc) og forhindrer forkerte tegn i at vises i nummeroplysninger.

**Genindlæs metadata** markerer hver fil i dit musikbibliotek som manglende metadata, hvilket medfører, at metadatalæseren opdaterer hver post.

**Start metadatalæsning** udløser metadatalæseren manuelt. Fremskridt vises under handlingen.

### Online synkronisering

Automatisk online musiksynk tilføjer numre fra tilsluttede cloud-tjenester til musikbiblioteket automatisk. For at aktivere det skal du åbne musikbiblioteksindstillingerne og vælge synkroniseringsmapper.

Med denne indstilling aktiveret scanner applikationen de valgte mapper, identificerer understøttede lydfiler og tilføjer dem til dit bibliotek. Start eller stop synkronisering med den tilsvarende menuhandling.

Online synk kører kun, når appen er i forgrunden, så synkronisering af et stort bibliotek kan tage noget tid. For at fremskynde tingene skal du holde appen åben, oprette forbindelse til en strømkilde og aktivere **Skærm → Altid aktiv** i indstillingerne.

Alternativt kan du udføre online synk på desktopversionen af appen og overføre musikbiblioteket til iOS ved hjælp af **Sikkerhedskopiér og gendan**.

Du kan også vælge, hvor ofte online synk kører. Indstilling af intervallet til **Straks** udløser en synk, hver gang du åbner applikationen.

### Offline synkronisering

Konfigurer offline musiksynkronisering.

#### Synkroniserede offline mapper

Når du markerer en online mappe på din cloud-server som tilgængelig offline (ved hjælp af menuen Flere handlinger), vises den her. Mappeindholdet downloades til **Lokale filer → Offline mapper**. Når den online mappe ændres (filer tilføjet, fjernet eller opdateret), kontrollerer appen for ændringer og opdaterer den lokale kopi på din enhed.

På denne skærm kan du manuelt starte synkronisering af offline mapper, vise offline-mappen i dens overordnede mappe og deaktivere offline-tilstand for mappen. Deaktivering af offline-tilstand fjerner alle lokale kopier af filer fra din enhed.

#### Tidsinterval

Vælg, hvor ofte appen kontrollerer offline mapper for ændringer.

#### Start scanning af lokale mapper

Scan alle lokale mapper i applikationens Documents-mappe for understøttede lydfiler. Fundne filer tilføjes automatisk til musikbiblioteket. Filer, der er placeret på din enhed, men uden for applikationens Documents-mappe, skal tilføjes til musikbiblioteket manuelt, da appen ikke kan få adgang til dem på grund af iOS/macOS-sikkerhedsbegrænsninger.

**Vigtigt:** Det anbefales periodisk at starte offline musiksynkronisering for at holde dit musikbibliotek opdateret med dine lokale filer.

### Personalisering

Konfigurer stilen for musikbiblioteksskærmen. Tre muligheder er tilgængelige: **Almindelig menu**, **Grupperet menu** og **Fanebladsmenu**. Du kan også aktivere eller deaktivere albumcovers på skærmen med albumdetaljer.

### Albumcovers

Vælg, hvordan applikationen indlæser og gemmer albumcovers.

- **Netværkstype** — vælg **Wi-Fi** eller **Wi-Fi og mobildata** til download af covers.
- **Indlæs albumcovers for online filer** — når aktiveret, indlæses indlejrede albumcovers for filer gemt i cloud-lager. Dette kan bruge yderligere netværksdata.
- **Søg i mappen** — når aktiveret, og et nummer ikke har et indlejret cover, leder appen efter JPEG- eller PNG-billeder i samme mappe og bruger dem som albumcover.
- **Coverkvalitet** — vælg kvaliteten af albumcovers gemt på din enhed.
- **Vis i mappe** — åbn den mappe, hvor albumcovers er cachelagret, så du kan administrere eller sikkerhedskopiere dem.
- **Slet alle** — slet cachelagrede albumcovers for at frigøre lagerplads og tvinge appen til at genindlæse dem efter behov.

### Afspilningslister

Aktivér muligheden for at tilføje den samme sang til en afspilningsliste to gange. Som standard er denne mulighed deaktiveret.

### Seneste

Administrer din liste over senest afspillede sange.

- **Slet liste** — slet hele listen over senest afspillede sange.
- **Skift listestørrelse** — angiv antallet af elementer, der vises i listen.
- **Eksporter sangliste** — eksporter din liste over senest afspillede sange som M3U, CSV eller TXT. Detaljerede instruktioner er tilgængelige [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritter

Administrer listen over dine yndlingssange.

- **Samtidig redigering** — når aktiveret, tilføjer en sang til favoritter den både i musikbiblioteket og filer-sektionen simultant.
- **Slet liste** — slet hele listen over yndlingssange.
- **Eksporter sangliste** — ligesom Seneste, eksporter favoritter som M3U, CSV eller TXT.

### Slet musikbibliotek

Slet musikbiblioteksdatabasen. Dine musikfiler på lageret forbliver urørte.

## Adgangskode

Aktiverer skærmen med adgangskodebeskyttelse, hvis du vil beskytte dine applikationsdata.

## Filhåndtering

Sektionen Filhåndtering styrer, hvordan filer overføres, gemmes og forhåndsvises.

### Filoverførsler

Vælg dine netværkspræferencer for at downloade filer til din enhed.

### Maksimalt antal parallelle opgaver

Indstil antallet af parallelle downloadtråde. Et højere tal fremskynder downloads, men kræver mere batteri.

### Filoverførselsopgaver

Viser aktuelt aktive upload- og downloadopgaver.

### Baggrundsnedlæsninger

Tillad downloads, mens appen er i baggrunden. Hvis baggrundsnedlæsninger forbruger meget energi, kan iOS afbryde appen.

### Gem downloadede filer til

Vælg standardmappen for downloads, eller lad appen spørge dig hver gang.

### Synkroniserede offline mapper

Administrer offline synk for valgte mapper. For at aktivere offline synk skal du trykke på trepriks-knappen ved siden af en mappe og vælge **Tilgængelig offline-tilstand**. Nye filer tilføjet til cloud-mappen downloades automatisk til din enhed. Læs mere om offline-tilstande [her](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Tidsinterval

Vælg, hvor ofte offline mapper synkroniseres. **Straks** udløser en synk, hver gang du åbner appen.

### Vis fulde filnavne

Vis komplette filnavne, inklusive filtypenavne, i filhåndteringen.

### Rediger online filer

Deaktiver online fileredigering for at skifte til skrivebeskyttet tilstand for tilsluttede cloud-tjenester og forhindre utilsigtede sletninger. Denne handling fjerner fileredigeringsoperationer fra brugergrænsefladen.

### Kopier filer ved åbning

Angiv, hvordan appen håndterer importerede filer fra andre applikationer.

### Miniaturebilleder for filer

Administrer og slet genererede filminiaturebilleder for at frigøre lagerplads.

### Slet midlertidige filer

Ryd applikationens cachemappe for at genvinde lagerplads.

## Lydtags-editor

Konfigurer den indbyggede lydtags-editor.

### Skalering af albumcover

Vælg den skaleringsmetode, der bruges, når et albumcover gemmes i lydtags.

### Opdater online filer

Når aktiveret, opdaterer applikationen automatisk en fils metadata på cloud-serveren, efter du er færdig med at redigere den.

### Slet fil efter redigering online

Vælg, om applikationen skal slette den downloadede kopi, efter du er færdig med at redigere en online fil på en cloud-server.

### Knapper på hovedskærmen

Vælg hvilke knapper der er synlige på lydtags-editorens hovedskærm.

## Widgets

Aktivér widgets, så appen opdaterer widget-data under afspilning. Widget-opdateringer kræver yderligere energi, så aktiver dette kun, hvis du faktisk bruger widgets på din startskærm eller låseskærm.

Du kan læse mere om Evermusic-widgets i [Navigationsguidet](/docs/guide/evermusic/evermusic-guide-navigation/).

## CarPlay

Skift CarPlay-indstillinger her. Denne menu er også tilgængelig inde i CarPlay-grænsefladen, så du kan justere oplevelsen, mens du kører.

### Sorter

Konfigurer sorteringsindstillinger for alle CarPlay-skærme.

### Grænse for indlæsning af indhold

Vælg, om appen bruger paginering på CarPlay-skærmen. Paginering holder menuer responsive på enheder med begrænset hukommelse og store biblioteker.

### Gradientfarve for menuikoner

Vælg farveskema for CarPlay-startskærmen.

### Vis billeder

Deaktiver billeder på CarPlay-skærmen for at optimere indlæsningshastighed og reducere hukommelsesforbrug på store biblioteker.

### Sæt afspilning på pause ved tilslutning

Aktivér dette for at undgå pludselig høj lyd, når du tilslutter din enhed til CarPlay.

## Wi-Fi-drev

Aktivér Wi-Fi-drev for at overføre filer fra en computer til din enhed ved hjælp af en desktop-webbrowser. Detaljerede instruktioner om, hvordan du bruger Wi-Fi-drev, er tilgængelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalisering

Tilpas brugergrænsefladen til dine præferencer.

### Applikationsikon

Vælg et alternativt applikationsikon til din startskærm.

### Farveskema

Vælg brugergradefladetemaet og aktivér mørk tilstand. Når **Standard** er valgt, følger applikationen enhedens udseendeindstillinger.

### Baggrundsstil

Rediger baggrundsstilen for applikationen. I øjeblikket er den eneste mulighed **Sløret albumcover**, som bruger det aktuelt afspillende nummers kunstværk som sløret appbaggrund.

### Udseende af elementer på listen

Finjuster, hvordan elementer vises på lister. Nyttigt på små skærme — du kan lade appen justere rækkehøjde automatisk baseret på indhold eller vise mindre ikoner i listeceller for at give teksten mere plads.

### Grænse for indlæsning af indhold

Som standard bruger applikationen paginering til at fremskynde indlæsning af indhold. Du kan deaktivere paginering for at indlæse alt på én gang.

### Stil for skærm med lokale filer

Skift præsentationsstilen for sektionen **Lokale filer**.

### Stil for musikbiblioteksskærm

Tilpas udseendet af skærmen **Musikbibliotek**.

### Stil for lydafspillerskærm

Konfigurer udseendet af skærmen **Lydafspiller**.

### Stil for kontekstmenu

Vælg stilen for den kontekstmenu, der vises, når du trykker på knappen Flere handlinger.

## Vindue

Tilgængeligt på Mac og Catalyst. Konfigurer vinduesrelaterede præferencer såsom standardstørrelse og adfærd ved opstart.

## Skærm

Vælg, om skærmen skal forblive aktiv, mens du bruger applikationen. Nyttigt ved scanning af store biblioteker eller ved langvarigt tag-redigeringsarbejde.

## Tilgængelighed

Aktivér **Teksttilstand** for at skjule alle billeder i brugergrænsefladen. Teksttilstand aktiveres automatisk, når VoiceOver er aktiv, og er også nyttig til meget små eller kun-tekst-opsætninger.

## Sprog

Skift applikationssproget og tilsidesæt systemstandarden. I øjeblikket understøtter appen følgende lokaliseringer: Afrikaans, Akan, Albansk, Amharisk, Arabisk, Armensk, Assamesisk, Aymara, Aserbajdsjansk, Bambara, Bengali, Baskisk, Hviderussisk, Bosnisk, Bulgarsk, Burmesisk, Catalansk, Cebuano, Forenklet Kinesisk, Traditionelt Kinesisk, Korsikansk, Kroatisk, Tjekkisk, Dansk, Dhivehi, Dogri, Hollandsk, Engelsk, Esperanto, Estisk, Ewe, Filippinsk, Finsk, Fransk, Galicisk, Ganda, Georgisk, Tysk, Græsk, Guarani, Gujarati, Haitisk Kreol, Hausa, Hawaiiansk, Hebraisk, Hindi, Hmong, Ungarsk, Islandsk, Igbo, Iloko, Indonesisk, Irsk, Italiensk, Japansk, Javanesisk, Kannada, Kasakhisk, Khmer, Kinyarwanda, Koreansk, Krio, Kurdisk, Sorani Kurdisk, Kirgisisk, Lao, Latin, Lettisk, Lingala, Litauisk, Luxembourgsk, Makedonsk, Maithili, Malagasisk, Malaysisk, Malayalam, Maltesisk, Maori, Marathi, Mizo, Mongolsk, Nepalesisk, Nordligt Sotho, Norsk Bokmål, Nyanja, Odia, Oromo, Pashto, Persisk, Polsk, Portugisisk, Punjabi, Rumænsk, Russisk, Samoansk, Sanskrit, Skotsk Gælisk, Serbisk, Shona, Sindhi, Singalesisk, Slovakisk, Slovensk, Somalisk, Sydligt Sotho, Spansk, Sundanesisk, Swahili, Svensk, Tadsjikisk, Tamil, Tatarisk, Telugu, Thai, Tsonga, Tyrkisk, Turkmensk, Ukrainsk, Urdu, Uygurisk, Usbekisk, Vietnamesisk, Walisisk, Xhosa, Jiddisch, Yoruba, Zulu.

## Sikkerhedskopiér og gendan

Sikkerhedskopiér alle dine applikationsdata eller migrer dem til en anden enhed. Du kan vælge, hvad der skal inkluderes:

- **Database** — alle dine musikbiblioteksnumre og afspilningslister. Offline numre er ikke inkluderet for at holde sikkerhedskopistørrelsen håndterbar.
- **Albumcovers** — alle dine cachelagrede albumcovers.
- **Indstillinger** — alle dine applikationsindstillinger.

Tryk på **Sikkerhedskopiér applikationsdata** for at starte sikkerhedskopieringsoperationen. Applikationsdataene skrives til en enkelt fil, som du kan bruge til at gendanne applikationstilstanden på en ny enhed eller efter geninstallation af appen.

For at gendanne applikationsdata på en ny enhed skal du flytte sikkerhedskopifilen til den nye enhed ved hjælp af en tilsluttet cloud-tjeneste eller iCloud og åbne den på den nye enhed.

Vi har en detaljeret trin-for-trin-guide her: [Sådan overfører du dit musikbibliotek mellem enheder i Evermusic: Trin-for-trin-guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Hjælp

Åbn applikationsguiden for hjælp og vejledning til effektiv brug af appen.

## Ofte stillede spørgsmål

Find svar på almindelige spørgsmål i FAQ-sektionen.

## Send feedback

Har du feedback eller brug for hjælp? Send din feedback til vores supportteam direkte fra appen.

## Del denne app

Del applikationen med dine venner for at hjælpe med at sprede ordet.

## Opdag flere apps

Udforsk andre apps fra Everappz.

## Vilkår og betingelser

Skitserer vilkårene og betingelserne for brug af applikationen. Læs det venligst, inden du bruger applikationen.

## Privatlivspolitik

Besøg siden med privatlivspolitik for at forstå vores databehandlingspraksis. Læs det venligst, inden du bruger applikationen.

## Analytics og dataindsamling

Kontroller hvilke tjenester der er aktiveret til analytics og dataindsamling, og deaktivér dem, du ikke ønsker.

I **Evermusic Free (blåt ikon)** er analytics og diagnostik aktiveret som standard for at hjælpe os med at forbedre appen — du kan slå dem fra her til enhver tid. **Evermusic Pro (rødt ikon) inkluderer ikke nogen analytics eller diagnostik overhovedet** — sektionen er tom (eller skjult), fordi intet indsamles, og der er ingen tilmeldingsmulighed.

## Juridiske meddelelser

Indeholder oplysninger om hvert bibliotek, der bruges i applikationen, sammen med appversionsnummeret og build-oplysninger.
