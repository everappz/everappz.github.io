---
title: "Indstillinger"
date: 2020-02-01
lastmod: 2026-06-01
description: "Udforsk alle indstillinger i Evervideo — Medieafspiller (Picture-in-Picture, hardware H.264 / HEVC-dekodning, videoequalizer, skalering, rotation, VR-visning), Lyd (equalizer, samplingsfrekvens, kanaler, IO-buffer, blandet tilstand), Undertekster (primær / sekundær, skrifttype, ekstern fil, libass), Mediebibliotek, Filhåndtering, Wi-Fi Drive, Widgets, Personalisering, Sprog, Adgangskode, Sikkerhedskopi og gendannelse — til iPhone, iPad og Mac."
keywords: [
  "Evervideo indstillinger", "videoafspiller konfiguration", "premium opgradering Evervideo",
  "Picture-in-Picture indstillinger", "videoequalizer indstillinger",
  "videoskaleringstilstand", "videorotation", "hardwaredekoder iPhone",
  "undertekstindstillinger", "sekundær undertekst iOS", "libass indstillinger",
  "ekstern undertekstfil", "undertekstskrifttype",
  "lydequalizer indstillinger", "lydoutput samplingsfrekvens",
  "lydoutput kanaler", "IO-buffertid", "blandet tilstand lyd",
  "WiFi Drive video", "Evervideo widgets",
  "Evervideo sikkerhedskopi gendannelse", "Evervideo adgangskode",
  "Evervideo sprog", "Evervideo personalisering"
]
tags: ["guide", "evervideo", "indstillinger"]
readingTime: 16
---


Indstillingsskærmen er Evervideos kontrolcenter. Herfra kan du opgradere til Premium, konfigurere video- og lydmotorerne (systemcodecs eller FFmpeg), administrere Picture-in-Picture, konfigurere undertekster (primær, sekundær, libass, eksterne filer, skrifttyper), organisere mediebiblioteket, konfigurere filhåndteringen, aktivere startskærmwidgets, sikkerhedskopiere dine data og få adgang til hjælp og juridiske oplysninger. Sektioner er grupperet under overskrifter: Køb og opdateringer, App-præferencer, Hjælp, Juridisk og privatliv.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideos indstillingshovedskaerm" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Opgrader til Premium

Opgrader applikationen til Premium-versionen for at fjerne alle begrænsninger. Gratisversionen af applikationen tilbyder et engangskøb på livstid og to abonnementsindstillinger (1 måned og 1 år) for at fjerne alle begrænsninger og opgradere til Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo opgrader til Premium" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

**Family Sharing** er aktiveret for alle køb og planer, så du kan dele Premium-versionen med op til fem familiemedlemmer uden ekstra omkostninger.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo vælg en Premium-plan" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Deling af køb mellem iOS og Mac

Livstidskøb og abonnementer deles mellem iOS og Mac ved hjælp af **iCloud** til at synkronisere disse oplysninger. Hvis du har Premium på din iOS-enhed, skal du sikre dig, at du har den seneste version installeret, og at iCloud er aktiveret. Start appen på iOS og vent et minut, mens købsoplysninger uploades til iCloud, og start derefter Mac-versionen — Premium skal aktiveres automatisk.

Du kan også trykke på knappen **Gendan køb** i appindstillingerne. Sørg for, at du har en internetforbindelse og er logget ind på den samme iCloud- og App Store-konto på begge enheder.

## Gendan køb på en ny enhed

For at gendanne dit køb på en ny enhed skal du bruge menuen **Køb → Gendan køb**. Du vil se listen over dine køb. Hvis du ikke ser dem alle, skal du bekræfte, at enheden er tilsluttet det samme Apple-ID, der blev brugt til at foretage købene, og sørge for, at iCloud er aktiveret.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo købsmenu i indstillinger" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Prøv Premium gratis

Du kan opgradere til Premium-versionen gratis i en begrænset periode via denne menu. Se blot en annonce, eller fortæl dine venner om appen.

## Softwareopdatering

Tryk på **Softwareopdatering** for at kontrollere, om en nyere version af Evervideo er tilgængelig på App Store.

## Nyheder

Denne menu er tilgængelig, efter en ny version er udgivet. Den viser en oversigt over ændringerne og nye funktioner i den seneste opdatering.

## Afspiller

Alt relateret til afspilning befinder sig her — lyd, video, undertekster, enheder, personalisering, cache og den sovende timer.

### Generelt

Disse indstillinger dækker de grundlæggende aspekter af afspilleren.

- **Gentagelsestilstand** — vælg, hvordan afspilleren opfører sig, når en video er færdig:
  - **Gentag alle** — gentager alle videoer i din kø.
  - **Gentag én** — gentager kun den aktuelle video.
  - **Stop gentagelse** — sætter på pause, når den aktuelle video slutter.
  - **Ingen gentagelse** — afspiller køen én gang igennem uden at gentage.
- **Bland-tilstand** — randomiser rækkefølgen af videoer i din kø (**Til** eller **Fra**).
- **Gem afspilningsposition** — gemmer og gendanner afspilningspositionen for videoer i dit bibliotek.
- **Gem afspillertilstand** — bevarer afspillerens tilstand, inden du lukker appen, så du kan genoptage, hvor du slap.

### Video

Konfigurer, hvordan Evervideo dekoder og gengiver video.

- **Hardware-dekod H.264** — slå hardware-accelereret AVC-dekodning til / fra. Brug, når batteri og termisk ydelse er vigtige; slå fra for kompatibilitet med eksotiske profiler.
- **Hardware-dekod H.265 (HEVC)** — det samme for HEVC. Moderne iPhones, iPads og Macs dekoder HEVC effektivt.
- **Foretrukket pixelformat** — vælg det pixelformat, afspilleren præsenterer for rendereren (standarder er justeret til enheden).
- **Foretrukne FPS** — indstil en mål-afspilnings-FPS. Nyttigt til at matche en specifik skærmgenopfriskningshastighed.
- **Videoskaleringstilstand** — Tilpas / Udfyld / Stræk / Original. Bestemmer, hvordan billedet fylder visningsområdet.
- **Videovisningstilstand** (iOS / iPadOS) — hvordan videoen præsenteres i afspillervisningen.
- **Videorotation** — roter manuelt billedet 0° / 90° / 180° / 270° (nyttigt for videoer optaget med forkert orientering).
- **Videoequalizer** — juster lysstyrke, kontrast, mætning og farvetone med realtidsvisning. Brugerdefinerede forudindstillinger kan **eksporteres og importeres**.
- **VR-visning** (iOS / iPadOS) — til 360° sfæriske videoer. Træk for at se dig omkring, knib for at zoome.
- **Picture-in-Picture (PiP)** (iOS / iPadOS) — aktivér PiP-understøttelse; appen skifter til et flydende afspillervindue, når du sender appen til baggrunden eller trykker på PiP-knappen.

### Lyd

Konfigurer lydafspilning og -output.

- **Lydspor** — vælg lydstreamen, når en video har flere (kommentar, synkronisering osv.).
- **Lydequalizer** — 10-bånds EQ med forudindstillinger og en preamplifier. Brugerdefinerede forudindstillinger kan eksporteres / importeres.
- **Lydoutput-samplingsfrekvens** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Nyttigt med eksterne DACs.
- **Lydoutput antal kanaler** — Mono, Stereo, 5.1, ITU BS.775-1, SDDS og mere.
- **Lydoutput foretrukket IO-buffertid** — typisk værdi for lav-latens hi-res afspilning er omkring 5 ms (0,005 s). Juster til din hardware.
- **Lydoutput-tilstand** (kun iOS) — blandet tilstand lader Evervideos lyd blandes med andre apps.

### Undertekster

Evervideo inkluderer omfattende undertekststøtte.

- **Undertekstspor** — vælg fra indlejrede undertekstspor i filen.
- **Ekstern undertekstfil** — indlæs en ekstern `.srt`-, `.vtt`-, `.ass`- eller `.ssa`-fil fra din enhed eller enhver tilsluttet cloudtjeneste.
- **Skrifttype** — vælg en skrifttype til det primære undertekstspor.

### Enheder (kun iOS/iPadOS)

Vælg en **AirPlay**- eller **Google Chromecast**-enhed til videooutput.

### Personalisering

- **Afspillerlayout-stil** — Minimal (standard for Evervideo), Bund, Antik, Klassisk og mere.
- **Handlinger på hovedskærmen** — vælg, hvilke knapper der vises på afspillerens hovedskærm.
- **Låseskærmkontroller** — Spring tid, Tilføj bogmærke, Tilføj til favoritter.
- **Spring-tidsintervaller** — vælg tidsintervallet for spring-knapper (5 s, 10 s, 15 s, 30 s osv.).
- **Omslagsbillede-rulningsstil** — foretrukken rulningsstil til omslagskunst.
- **Yderligere elementer** — Lydformatinfo, Lydstyrkestrider.

### Filindlæsning

Konfigurer, hvordan videodata streames fra netværket.

- **Netværkstype** — kun Wi-Fi, eller Wi-Fi + Mobil.
- **Forudindlæsningstid** — bufferlængde for jævnere afspilning på langsomme netværk.
- **Brug direkte URL** — når det understøttes, brug en direkte URL til hurtigere indlæsning.

### Afspilnings-cache

Videoer i afspillerkøen downloades automatisk for at sikre jævn afspilning. Du kan deaktivere denne mulighed eller konfigurere cache-størrelsen her.

### Sovende timer

Aktiver en timer til automatisk at stoppe afspilning efter en specificeret periode. Tryk på konfigurationsikonet for **præcisionstilstand** med minut-for-minut granularitet.

## Mediebibliotek

Administrer automatisk synkronisering, metadata, albumomslag, afspilningslister, seneste og favoritter.

### Metadatalæsning

Når du tilføjer videoer til biblioteket, scanner metadatalæseren dem i baggrunden og organiserer dem efter Album og Genre. Du kan justere scanningshastighed, deaktivere læseren eller udløse en fuld genscanning med **Genindlæse metadata**. **Normaliser metadatakodning** retter automatisk ødelagte tegnsæt-kodninger (almindeligt med filer fra Windows PC'er).

### Online synkronisering

Tilføj automatisk videoer fra tilsluttede cloudtjenester og medieservere til dit bibliotek. Vælg, hvilke mapper der skal scannes, konfigurer, hvor ofte appen skal synkronisere, og start / stop synkronisering manuelt. Online synkronisering kører kun, mens appen er aktiv — til store biblioteker skal du bruge desktopversionen og derefter overføre det synkroniserede bibliotek med **Sikkerhedskopi og gendannelse**.

### Offline synkronisering

Når du markerer en cloudmappe som tilgængelig offline, vises den i **Filer → Offline mapper** og downloades automatisk. Nye filer tilføjet online downloades også. Konfigurer tidsintervallet og udløs manuelle synkroniseringer fra denne skærm.

### Personalisering

- **Mediebibliotek-skærmstil** — Simpel menu, Grupperet menu, Fanebladsmenu.
- Skift, om der skal vises store albumomslag på detaljeskærme.

### Albumomslag

- **Netværkstype** — Wi-Fi eller Wi-Fi + Mobil.
- **Indlæs albumomslag til online filer** — hent indlejret kunstværk fra cloudfiler (bruger ekstra data).
- **Søg i mappen** — brug JPEG / PNG-billeder i den samme mappe, når en video ikke har noget indlejret omslag.
- **Omslagskvalitet** — juster den opløsning, som omslag caches i.
- **Vis i mappe** / **Slet alle** — administrer kunstværks-cachen.

### Afspilningslister

Aktiver tilføjelse af den samme video til en afspilningsliste to gange (fra som standard).

### Seneste

Administrer listen over senest afspillede videoer — ændr størrelsen, slet eller eksporter som M3U / CSV / TXT.

### Favoritter

- **Samtidig redigering** — spejl favoritter mellem mediebiblioteket og filafsnittet.
- **Slet liste** — ryd favoritlisten.
- **Eksporter sangliste** — eksporter favoritter som M3U / CSV / TXT.

### Slet mediebibliotek

Slet mediebiblioteksdatabasen. Dine video- og lydfiler på lageret efterlades urørte.

## Adgangskode

Beskyt Evervideo med en **4-cifret numerisk adgangskode**. Når den er aktiveret, bliver du bedt om at indtaste adgangskoden, hver gang appen starter. Kombiner den med iOS Face ID / Touch ID på enheden for ekstra beskyttelse.

## Filhåndtering

Styrer, hvordan filer overføres, gemmes og forhåndsvises.

- **Filoverførsler** — netværkspræference (kun Wi-Fi eller Wi-Fi + Mobil).
- **Maksimalt antal parallelle opgaver** — indstil antallet af parallelle download-tråde.
- **Filoverførselsopgaver** — se aktuelt aktive uploads og downloads.
- **Baggrundsoverførsler** — tillad downloads, mens appen er i baggrunden.
- **Gem downloadede filer til** — standard downloads-mappe.
- **Synkroniserede offline mapper** — administrer offline-tilstandsmapper.
- **Tidsinterval** — hvor ofte offline mapper kontrolleres for ændringer.
- **Vis fulde filnavne** — vis udvidelser i filhåndteringen.
- **Rediger online filer** — deaktiver for at skifte til skrivebeskyttet tilstand for tilsluttede cloudtjenester.
- **Kopier filer ved åbning** — hvordan importerede filer fra andre apps håndteres.
- **Miniaturebilleder til filer** — administrer genererede filminiaturebilleder.
- **Slet midlertidige filer** — ryd applikationens cache-mappe.

## Wi-Fi Drive

Aktiver Wi-Fi Drive for at overføre filer fra en computer til din enhed ved hjælp af en skrivebordsbrowser, Finder eller File Explorer. Detaljerede instruktioner er tilgængelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Widgets

Aktiver widgets, så appen opdaterer widgetdata under afspilning. Widget-opdateringer kræver ekstra energi, så kontakten er fra som standard — aktiver den kun, hvis du faktisk bruger widgets på din startskærm eller låseskærm.

Du kan tilføje Evervideo-widgets ved at trykke længe på din startskærm eller låseskærm, trykke på **+**, søge **Evervideo** og vælge en widget-størrelse. Widgets viser den aktuelle video og trykker direkte igennem til fuldskærmsafspilleren. Widgets fungerer også på macOS i Meddelelsescenter.

## Personalisering

Tilpas brugerfladen til dine præferencer.

- **Applikationsikon** — alternativt startskærmsikon (Premium).
- **Farveskema** — Mørkt, Lyst eller Standard (følger dit systems udseende).
- **Baggrundsstil** — Sløret albumomslag eller ensfarvet farve.
- **Elementers udseende på listen** — auto-juster rækkehøjde; vis mindre miniaturebilleder.
- **Indholdindlæsningsgrænse** — slå paginering til / fra.
- **Filer-skærmstil** — Simpel menu eller Grupperet menu.
- **Mediebibliotek-skærmstil** — Simpel / Grupperet / Fanebladsmenu.
- **Afspillerskærmstil** — Minimal / Bund / Antik / Klassisk.
- **Kontekstmenu-stil** — systemmenu eller bundark-stil.

## Vindue

Tilgængelig på Mac og Catalyst. Konfigurer vinduesrelaterede præferencer såsom standardstørrelse og opførsel ved start.

## Skærm

Vælg, om skærmen skal forblive aktiv, mens du bruger applikationen.

## Tilgængelighed

Aktiver **Teksttilstand** for at skjule billeder i brugerfladen. Teksttilstand aktiveres automatisk, når VoiceOver er aktivt.

## Sprog

Skift applikationssprog og tilsidesæt systemstandarden. Ændringen træder i kraft, efter du fuldt ud afslutter og genåbner Evervideo. Over 120 sprog understøttes.

## Sikkerhedskopi og gendannelse

Sikkerhedskopier alle dine applikationsdata, eller flyt dem til en anden enhed. Vælg, hvad der skal inkluderes:

- **Database** — dine mediebiblioteksindtastninger, afspilningslister, vurderinger, favoritter, se-historik. Offline filer er ikke inkluderet for at holde filstørrelsen håndterbar.
- **Albumomslag** — dit cachede kunstværk.
- **Indstillinger** — dine applikationsindstillinger.

Tryk på **Sikkerhedskopier applikationsdata** for at starte sikkerhedskopieringen. For at gendanne på en ny enhed skal du flytte sikkerhedskopifilen via iCloud Drive, AirDrop eller en tilsluttet cloudtjeneste og åbne den på den nye enhed.

## Hjælp

Få adgang til applikationsguiden for hjælp og vejledning om effektiv brug af appen.

## Ofte stillede spørgsmål

Find svar på almindelige spørgsmål i FAQ-sektionen.

## Send feedback

Send din feedback til vores supportteam direkte fra appen med diagnostisk information vedhæftet automatisk.

## Del denne app

Del Evervideo med dine venner for at sprede budskabet.

## Opdag flere apps

Udforsk andre apps fra Everappz.

## Vilkår og betingelser

Læs vilkår og betingelser, inden du bruger applikationen.

## Fortrolighedspolitik

Læs fortrolighedspolitikken for at forstå vores datahåndteringspraksis.

## Analyse og dataindsamling

Tjek, hvilke tjenester der er aktiveret til analyse og dataindsamling, og deaktiver dem, du ikke ønsker.

## Juridiske meddelelser

Oplysninger om hvert bibliotek, der bruges i applikationen, samt appversionsnummeret og byggeoplysninger.
