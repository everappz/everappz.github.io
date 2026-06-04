---
title: "Innstillinger"
date: 2020-02-01
description: "Utforsk alle innstillinger i Flacbox — fra avspillingspreferanser, FFmpeg / system-lydmotoren, Hi-Res lydutgang, equalizer-justeringer, tonehøydekorrigering, IO-bufferlengde, metadatasynkronisering, spillelistekontroll, filoverføringer, hjemskjerm-widgets, Apple CarPlay, UI-personalisering, språk, passord, sikkerhetskopiering og gjenoppretting, og Premium-oppgradering."
keywords: [
  "Flacbox innstillinger", "lydspillerkonfigurasjon", "premium oppgradering Flacbox",
  "WiFi Drive", "metadatasynkronisering", "equalizer", "avspillingshastighet",
  "spilleliste duplikater", "filhåndterer innstillinger", "frakoblet musikk synk",
  "lydtagger-editor", "mørk modus", "gjenopprett kjøp", "innstillingssikkerhetskopi",
  "Flacbox widget-innstillinger", "Flacbox CarPlay-innstillinger",
  "Flacbox FFmpeg-innstillinger", "Flacbox samplingsfrekvens-innstillinger",
  "Flacbox tonehøydekorrigerings-innstillinger", "Flacbox IO-buffer",
  "Flacbox passord", "Flacbox språk", "Flacbox personalisering",
  "Flacbox analyse"
]
tags: ["guide", "flacbox", "innstillinger"]
readingTime: 16
---


Innstillingsskjermen er kontrollsenteret til Flacbox. Herfra kan du oppgradere til Premium, konfigurere lydmotoren (systemkodeker eller FFmpeg), administrere musikkbiblioteket ditt, sette opp filbehandleren, tilpasse lydtagger-editoren, aktivere hjemskjerm-widgets og Apple CarPlay, sikkerhetskopiere dataene dine, og få tilgang til hjelp og juridisk informasjon. Seksjoner er gruppert under overskrifter: Kjøp og oppdateringer, App-preferanser, Hjelp, og Juridisk og personvern.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Innstillinger Hovedskjerm" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Oppgrader til Premium

Oppgrader applikasjonen til Premium-versjonen for å fjerne alle begrensninger. Den gratis versjonen av applikasjonen tilbyr et engangs livstids app-kjøp og to abonnementsalternativer (1 måned og 1 år) for å fjerne alle begrensninger og oppgradere til Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Oppgrader til Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Familiedeling** er aktivert for alle kjøp og planer, slik at du kan dele Premium-versjonen med opptil fem familiemedlemmer uten ekstra kostnad.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Velg en Premium-plan" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Du kan lese mer om kjøp og Premium-versjonen her: [Hva er forskjellen mellom Flacbox og Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Dele Kjøp Mellom iOS og Mac

Livstidskjøp og abonnementer deles mellom iOS og Mac, og bruker iCloud for å synkronisere denne informasjonen. Hvis du har Premium-versjonen på iOS-enheten din, sørg for at du har den nyeste versjonen installert og at iCloud er aktivert. Start appen på iOS og vent ett minutt på at kjøpsinformasjonen din lastes opp til iCloud.

Du kan også prøve å trykke på knappen Gjenopprett kjøp i app-innstillingene. Installer deretter den nyeste app-versjonen fra App Store på Mac-en din og start appen. Sørg for at du har en internettforbindelse og bruker den samme iCloud- og App Store-kontoen på Mac som du brukte på iOS. Vent ett minutt på at appen laster ned kjøpsinformasjon fra iCloud — Premium-versjonen bør aktiveres automatisk på Mac-en din.

## Gjenopprette Kjøp på en Ny Enhet

For å gjenopprette kjøpet ditt på en ny enhet, bruk menyen Kjøp → Gjenopprett kjøp. Du vil se listen over kjøpene dine. Hvis du ikke ser alle, bekreft at enheten er koblet til den samme Apple ID-en som ble brukt til å gjøre kjøpene, og sørg for at iCloud er aktivert.

## Prøv Premium Gratis

Du kan oppgradere til Premium-versjonen gratis, for en begrenset tid, ved hjelp av denne menyen. Se bare en annonse eller fortell vennene dine om appen for å få Premium gratis.

## Kjøp

Du kan gjenopprette tidligere kjøp fra denne menyen. Hvis du støter på aktiveringsfeil, prøv å aktivere alternativet Gjenopprett kjøp ved appstart.

## Programvareoppdatering

Trykk på Programvareoppdatering for å sjekke om en nyere versjon av Flacbox er tilgjengelig. Appen vil sammenligne den installerte versjonen din med den nyeste versjonen i App Store og gi deg beskjed hvis en oppdatering anbefales.

## Hva er Nytt

Denne menyen er tilgjengelig etter at en ny versjon er utgitt. Den viser et sammendrag av endringene og nye funksjoner i den nyeste oppdateringen.

## Lydspiller

Denne seksjonen konfigurerer lydspilleren og den underliggende lydmotoren, inkludert FFmpeg / systemkodek-valget og Hi-Res lydutgangsalternativer.

### Generelt

Disse innstillingene dekker de grunnleggende aspektene av lydspilleren — avspillingskøen, lydutgang og lagring av spillerens tilstand.

- **Gjentagelsesmodus** — velg hvordan lydspilleren oppfører seg når et spor er ferdig:
  - **Gjenta alle** — spiller alle sporene i køen på nytt.
  - **Gjenta én** — gjentar bare det gjeldende sporet.
  - **Gjenta stopp** — setter avspillingen på pause når det gjeldende sporet slutter.
  - **Ingen gjentakelse** — lar køen spilles gjennom uten å gjenta.
- **Stokkemodus** — tilfeldiggjør rekkefølgen på spor i køen. Du kan slå det **Stokk av** eller **Stokk på**.
- **Lydkodek** — velg lydmotoren som brukes for avspilling:
  - **Systemkodek + FFmpeg** — prioriterer systemets lydkodek der det er mulig, og forbedrer kompatibilitet og stabilitet. Tonehøydekorrigering og lydutgangs-samplingsfrekvens kan være begrenset.
  - **FFmpeg** — tvinger FFmpeg-kodeken for alle lydfiler, og låser opp tonehøydekorrigering og lydutgangs-samplingsfrekvensen.
- **Lydutgangs-samplingsfrekvens** — juster lydutgangs-samplingsfrekvensen for å optimalisere lydkvaliteten, særlig nyttig med en ekstern DAC. Tilgjengelige verdier: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** og **96 kHz**.
- **Antall kanaler for lydutgang** — for flerkanalslyd-systemer med ekstern DAC, angi antall kanaler: Mono, Stereo, Senter / Venstre / Høyre, Senter / Venstre / Høyre / Surround, ITU BS.775-1, 5.1 Surround og SDDS.
- **Foretrukket IO-bufferlengde for lydutgang** — konfigurer inn- / ut-bufferlengden. En typisk verdi for å minimere latens ved avspilling av høyoppløsningslyd er omtrent **5 millisekunder (0,005 sekunder)**. Test ulike lengder på målenheten din for å finne den beste balansen mellom lav latens og feilfri avspilling.
- **Lydutgangsmodus (bare iOS)** — konfigurer blandet lydutgang slik at lyd fra Flacbox blandes med andre applikasjoner. Detaljerte instruksjoner er [her](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Lagre avspillingsposisjon** — lagrer og gjenoppretter avspillingsposisjonen for sanger i musikkbiblioteket ditt.
- **Lagre lydspillertilstand** — bevarer lydspillerens tilstand før du lukker appen, noe som gjør det enkelt å fortsette fra der du slapp.

Når du har aktivert både **Lagre avspillingsposisjon** og **Lagre lydspillertilstand**, åpne en mappe, album, artist eller sjanger og du vil se en knapp **Fortsett avspilling** øverst på skjermen.

### Personalisering

Personalisering lar deg tilpasse utseendet på lydspillerskjermen, endre tilgjengelige kontroller på hovedskjermen, låsskjermen og statuslinjen, og konfigurere hoppetidskontroller.

- **Lydspiller-skjermstil** — konfigurer plasseringen av elementer på lydspillerskjermen.
- **Rullelstil for albumomslag** — konfigurer den foretrukne rullingesstilen for albumomslag.
- **Tilleggselementer** — aktiver ekstra elementer på lydspillerskjermen. Lydformat-info viser lydinfo for det nå-spillende sporet over kunstverket; Lydvolum-glidebryter viser lydutgangs-glidebryteren under avspillingskontrollene.
- **Handlinger på hovedskjermen** — konfigurer hvilke knapper som skal være synlige på lydspillerens hovedskjerm som standard: Gjenta- og Stokkemodus, Neste og Forrige sang, Hoppetid, Sovtimer, Google Chromecast, AirPlay og Bluetooth, Lyd-Equalizer, Søk, Bokmerker, Hastighet, Legg til bokmerke, Legg til favoritter, Kommentarer og mer.
- **Avspillingskontroller på låsskjermen** — velg hvilke kontroller som vises på låsskjermen. Mulige verdier: Hoppetid, Legg til bokmerke, Legg til favoritter.
- **Hoppetidsknapper** — velg tidsintervallet for Hoppetids-knappene.

### Fillasting

Under fillasting kan du endre nettverkstypen som brukes til å laste inn sanger. Tilgjengelige alternativer: **Wi-Fi**, **Wi-Fi og mobildata**.

- **Forhåndsinnlastingstid** — sett bufringtidsintervallet. Øk dette hvis du har en dårlig nettverkstilkobling.
- **Bruk direkte URL** — når aktivert, brukes en direkte URL for å laste inn sangen hvis serveren støtter det. Dette kan øke sanglastingshastigheten, men kan påvirke avspillingsstabiliteten.

### Lyd-Equalizer

Konfigurer den 10-bands lyd-equalizeren, forhåndsinnstillingene og preamplifikatoren. Du kan lese mer om å konfigurere lyd-equalizeren [her](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Avspillingshastighet

Juster avspillingshastigheten til lydspilleren fra **0,02× til 3,00×**. Trykk på konfigurasjonikonet i øvre høyre hjørne for å bytte til **presisjonsmodusen** for finere justeringer.

### Tonehøydekorrigering

Endre tonehøydekorrigeringsinnstillinger ved å bruke de forhåndsdefinerte verdiene, eller bytt til **presisjonsmodusen** ved å trykke på knappen i øvre høyre hjørne. Tonehøydekorrigering er tilgjengelig i FFmpeg-kodekbanen, med et område fra **-1000 til +1000**.

### Avspillingsbuffer

Sanger i lydspillerkøen lastes automatisk ned for å sikre jevn avspilling. Hvis du manuelt laster ned lydfiler, kan du deaktivere dette for å unngå duplikater. Du kan også konfigurere lydspillerens bufferstørrelse her.

### Sovtimer

Aktiver en timer for automatisk å stoppe avspillingen etter en bestemt periode. Trykk på konfigurasjonikonet i øvre høyre hjørne for **presisjonsmodusen** med minutt-for-minutt granularitet.

## Bibliotek

Musikkbibliotekinnstillingene dine — automatisk synkronisering, metadata-lesing, albumomslastning, spillelister, nylige og favoritter — finner du her.

### Metadata-lesing

Når du legger til spor i biblioteket, går **metadatalesseren** i gang. Denne bakgrunnsprosessen leser all metadata fra sporene dine og organiserer dem etter Artist, Album, Sjanger og Komponist. Du kan justere hastigheten på metadata-lesingen for å laste data raskere (på bekostning av mer batteri). Du kan også deaktivere metadatalesseren og vise filnavn i stedet for taginformasjon.

Metadatalesseren **oppdaterer bare metadata i musikkbiblioteket ditt** og endrer ikke filene som er lagret i skykontoen din eller lokal lagring. For å redigere metadata i selve lydfilene, bruk den innebygde **taggeditoren** via den tilsvarende handlingen i alternativmenyen.

Når **Metadata-lesing i bakgrunnen** er på, fortsetter leseren å jobbe i bakgrunnsmodus. Hvis appen bruker for mye energi under lydavspilling, kan iOS suspendere den.

Hvis du har en stor musikksamling, utfør metadatasynkronisering på desktopversjonen av applikasjonen og overfør det synkroniserte musikkbiblioteket til iOS ved hjelp av **Sikkerhetskopiering og gjenoppretting**.

Når **Normaliser metadata-koding** er aktivert, normaliserer appen automatisk kodingen av metadata for alle sanger. Dette fikser ødelagte tagkodinger (f.eks. etter å ha redigert filer på en Windows-PC) og forhindrer at feil tegn vises i sporinfo.

**Last inn metadata på nytt** merker alle filer i musikkbiblioteket ditt som manglende metadata, noe som gjør at metadatalesseren oppdaterer alle poster.

**Start metadata-lesing** utløser metadatalesseren manuelt. Fremgangen vises under handlingen.

### Online Synkronisering

Automatisk online musikknkronisering legger til spor fra tilkoblede skytjenester i musikkbiblioteket automatisk. For å aktivere det, åpne musikkbibliotekinnstillingene og velg synkroniseringsmapper.

Med dette alternativet aktivert, skanner applikasjonen de valgte mappene, identifiserer støttede lydfiler og legger dem til i biblioteket ditt. Start eller stopp synkronisering med den tilsvarende menyhandlingen.

Online synkronisering kjører bare når appen er i forgrunnen, så synkronisering av et stort bibliotek kan ta litt tid. For å øke hastigheten, hold Flacbox åpen, koble enheten til strøm og aktiver **Innstillinger → Skjerm → Alltid aktiv**.

Alternativt, utfør online synkronisering på desktopversjonen av appen og overfør resultatet til iOS ved hjelp av **Sikkerhetskopiering og gjenoppretting**.

Du kan også velge hvor ofte online synkronisering kjøres. Å sette intervallet til **Umiddelbart** utløser en synkronisering hver gang du åpner applikasjonen.

### Frakoblet Synkronisering

Konfigurer frakoblet musikknkronisering.

#### Synkroniserte Frakoblede Mapper

Når du merker en online mappe på skyserveren din som tilgjengelig frakoblet (ved hjelp av menyen **Flere handlinger**), vises den her. Mappeinnholdet lastes ned til **Lokale filer → Frakoblede mapper**. Når den online mappen endres (filer lagt til, fjernet eller oppdatert), sjekker appen for endringer og oppdaterer den lokale kopien på enheten din.

På denne skjermen kan du starte frakoblet mappesynkronisering manuelt, vise den frakoblede mappen i den overordnede mappen, og deaktivere frakoblet modus for mappen. Deaktivering av frakoblet modus fjerner alle lokale kopier av filer fra enheten din.

#### Tidsintervall

Velg hvor ofte appen sjekker frakoblede mapper for endringer.

#### Start Skanning av Lokale Mapper

Skann alle lokale mapper i applikasjonens **Documents**-mappe for støttede lydfiler. Funne filer legges automatisk til musikkbiblioteket. Filer som befinner seg på enheten din, men utenfor applikasjonens Documents-mappe, må legges til i musikkbiblioteket manuelt, ettersom appen ikke kan få tilgang til dem på grunn av iOS / macOS-sikkerhetsbegrensninger.

**Viktig:** Det anbefales å starte frakoblet musikknkronisering periodisk for å holde musikkbiblioteket oppdatert med de lokale filene dine.

### Personalisering

Konfigurer stilen på musikkbibliotekskjermen. Tre alternativer er tilgjengelige: **Enkel meny, Gruppert meny, Flikbasert meny**. Du kan også aktivere eller deaktivere albumomslag på albumdetaljskjermen.

### Albumomslag

Konfigurer hvordan applikasjonen laster og lagrer albumkunstverk.

- **Nettverkstype** — velg **Wi-Fi** eller **Wi-Fi og mobildata** for å laste ned omslag.
- **Last albumomslag for online filer** — når aktivert, lastes innebygde albumomslag for filer lagret i skylagring. Dette kan bruke ekstra nettverksdata.
- **Søk i mappe** — når aktivert, hvis et spor ikke har et innebygd omslag, ser appen etter JPEG- eller PNG-bilder i samme mappe og bruker dem som albumkunstverk.
- **Omslagskvalitet** — velg kvaliteten på albumomslag som er lagret på enheten din.
- **Vis i mappe** — åpne mappen der albumomslag er bufret.
- **Slett alle** — slett bufrede albumomslag for å frigjøre lagring og tvinge appen til å laste dem inn på nytt ved behov.

### Spillelister

Aktiver alternativet for å legge til den samme sangen i en spilleliste to ganger. Som standard er dette alternativet deaktivert.

### Nylige

Administrer listen over nylig avspilte sanger.

- **Slett liste** — slett hele listen over nylig avspilte sanger.
- **Endre listestørrelse** — sett antallet elementer som vises i listen.
- **Eksporter sangliste** — eksporter den nylig avspilte sanglisten som M3U, CSV eller TXT. Detaljerte instruksjoner er tilgjengelige [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritter

Administrer listen over favorittsangene dine.

- **Simultan redigering** — når aktivert, legger det å legge til en sang i favoritter den til både i musikkbiblioteket og filer-seksjonen samtidig.
- **Slett liste** — slett hele listen over favorittsanger.
- **Eksporter sangliste** — som Nylige, eksporter favoritter som M3U, CSV eller TXT.

### Slett Musikkbibliotek

Slett musikkbibliotekdatabasen. Musikfilene dine i lagringen forblir urørt.

## Passord

Aktiver passordskjermen for å beskytte applikasjonsdataene dine med en 4-sifret numerisk passord. Når aktivert, blir du bedt om å oppgi passordet hver gang appen starter. Kombiner det med iOS Face ID / Touch ID på enheten for ekstra beskyttelse.

## Filbehandler

Filbehandler-seksjonen styrer hvordan filer overføres, lagres og forhåndsvises.

### Filoverføringer

Velg nettverkspreferansen din for nedlasting av filer til enheten din.

### Maksimalt Antall Parallelle Oppgaver

Sett antallet parallelle nedlastingstråder. Et høyere tall øker nedlastingshastighetene men bruker mer batteri.

### Filoverføringsoppgaver

Viser for øyeblikket aktive opp- og nedlastingsoppgaver.

### Bakgrunnsoverføringer

Tillat nedlastinger mens appen er i bakgrunnen. Hvis bakgrunnsoverføringer forbruker mye energi, kan iOS suspendere appen.

### Lagre Nedlastede Filer Til

Velg standard nedlastingskatalog, eller la appen spørre deg hver gang.

### Synkroniserte Frakoblede Mapper

Administrer frakoblet synkronisering for valgte mapper. For å aktivere frakoblet synkronisering, trykk på tre-prikker-knappen ved siden av en mappe og velg **Tilgjengelig frakoblet modus**. Nye filer som legges til skymappen, lastes automatisk ned til enheten din. Les mer om frakoblede modi [her](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Tidsintervall

Velg hvor ofte frakoblede mapper synkroniseres. **Umiddelbart** utløser en synkronisering hver gang du åpner appen.

### Vis Fulle Filnavn

Vis fullstendige filnavn, inkludert utvidelser, i filbehandleren.

### Rediger Online Filer

Deaktiver redigering av online filer for å bytte til skrivebeskyttet modus for tilkoblede skytjenester og forhindre utilsiktede slettinger. Denne handlingen fjerner filredigeringsoperasjoner fra brukergrensesnittet.

### Kopier Filer ved Åpning

Spesifiser hvordan appen håndterer importerte filer fra andre applikasjoner.

### Miniatyrbilder for Filer

Administrer og slett genererte filminiatyrbilder for å frigjøre lagringsplass.

### Slett Midlertidige Filer

Tøm applikasjonens hurtigbuffermappe for å gjenvinne lagringsplass.

## Lydtagger-Editor

Konfigurer den innebygde lydtagger-editoren — nyttig for masseretting av artist / album / år / sjanger / omslags-problemer på tvers av sky- og lokale filer.

### Albumomslags Skalering

Velg skaleringsmetoden som brukes når et albumomslag lagres i lydtagger.

### Oppdater Online Filer

Når aktivert, oppdaterer applikasjonen automatisk en fils metadata på skyserveren etter at du er ferdig med å redigere den.

### Slett Fil Etter Online Redigering

Velg om applikasjonen skal slette den nedlastede kopien etter å ha fullført redigeringen av en online fil på en skyserver.

### Knapper på Hovedskjermen

Velg hvilke knapper som er synlige på lydtagger-editorens hovedskjerm.

For dypere massredigering av mange filer på én gang, installer følgeappen vår **Evertag**.

## Widgets

Aktiver widgets slik at appen oppdaterer widgetdata under avspilling. Widgetoppdateringer krever ekstra energi, så bryteren er av som standard — aktiver det bare hvis du faktisk bruker widgets på hjemskjermen eller låsskjermen din.

Du kan legge til Flacbox-widgets ved å trykke lenge på hjemskjermen eller låsskjermen, trykke på **+**, søke etter **Flacbox** og velge en widgetstørrelse. Widgets viser gjeldende kunstverk, sporsittel og artist, og trykk direkte til fullskjermspilleren. Widgets fungerer også på macOS i Varslingssenter.

## CarPlay

Endre CarPlay-innstillinger her. Denne menyen er også tilgjengelig i CarPlay-grensesnittet slik at du kan justere opplevelsen under kjøring.

### Sorter

Konfigurer sorteringsalternativer for alle CarPlay-skjermer.

### Innholdslastings-begrensning

Velg om appen bruker paginering på CarPlay-skjermen. Paginering holder menyene responsive på store biblioteker.

### Menyikonets Fargegradienten

Velg fargeopplegget for CarPlay-hjemskjermen.

### Vis Bilder

Deaktiver bilder på CarPlay-skjermen for å optimalisere lastingshastigheten og redusere minnebruk på store biblioteker.

### Sett Avspilling på Pause ved Tilkobling

Aktiver dette for å unngå plutselig høy lyd når du kobler enheten til CarPlay.

## Wi-Fi Drive

Aktiver **Wi-Fi Drive** for å overføre filer fra en datamaskin til enheten din ved hjelp av en desktop-nettleser, Finder eller Filutforsker. Detaljerte instruksjoner om bruk av Wi-Fi Drive er tilgjengelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalisering

Tilpass brukergrensesnittet etter dine preferanser.

### Applikasjonsikon

Velg et alternativt applikasjonsikon for hjemskjermen din (Premium).

### Fargevalg

Velg brukergrensesnittets tema og aktiver mørk modus. Når **Standard** er valgt, følger applikasjonen enhetens globale utseendeinnstillinger.

### Bakgrunnsstil

Endre bakgrunnsstilen til applikasjonen. For øyeblikket er det eneste alternativet **Uskarp albumomslag**, som bruker det nå-spillende sporets kunstverk som uskarp app-bakgrunn.

### Utseende av Elementer i Listen

Juster hvordan elementer vises i lister. Nyttig på små skjermer — du kan la appen justere radhøyden automatisk basert på innhold, eller vise mindre ikoner i listeceller for å gi tekst mer plass.

### Innholdslastings-begrensning

Som standard bruker applikasjonen paginering for å øke hastigheten på innlasting av innhold. Du kan deaktivere paginering for å laste alt på én gang.

### Lokale filer Skjermstil

Endre presentasjonsstilen for **Lokale filer**-seksjonen.

### Musikkbibliotek Skjermstil

Tilpass utseendet på **Musikkbibliotek**-skjermen.

### Lydspiller Skjermstil

Konfigurer utseendet på **Lydspiller**-skjermen.

### Kontekstmenystil

Velg stilen på kontekstmenyen som vises når du trykker på **Flere handlinger**-knappen.

## Vindu

Tilgjengelig på Mac og Catalyst. Konfigurer vindusrelaterte preferanser som standard størrelse og oppførsel ved oppstart.

## Skjerm

Velg om skjermen skal forbli aktiv mens du bruker applikasjonen. Nyttig ved skanning av store biblioteker eller langvarig tagge-redigeringsarbeid.

## Tilgjengelighet

Aktiver **Tekstmodus** for å skjule alle bilder i brukergrensesnittet. Tekstmodus aktiveres automatisk når VoiceOver er aktiv og er også nyttig for svært små eller tekstbaserte oppsett.

## Språk

Endre applikasjonsspråket og overstyr systemstandarden. Endringen trer i kraft etter at du helt lukker og åpner Flacbox på nytt. Støttede lokaliseringer inkluderer for øyeblikket: Afrikaans, Akan, Albansk, Amharisk, Arabisk, Armensk, Assamisk, Aymara, Aserbajdsjansk, Bambara, Bengalsk, Baskisk, Hviterussisk, Bosnisk, Bulgarsk, Burmesisk, Katalansk, Cebuano, Kinesisk (forenklet), Kinesisk (tradisjonelt), Korsikansk, Kroatisk, Tsjekkisk, Dansk, Divehi, Dogri, Nederlandsk, Engelsk, Esperanto, Estisk, Ewe, Filippinsk, Finsk, Fransk, Galisisk, Ganda, Georgisk, Tysk, Gresk, Guarani, Gujarati, Haitisk kreolsk, Hausa, Hawaiisk, Hebraisk, Hindi, Hmong, Ungarsk, Islandsk, Igbo, Iloko, Indonesisk, Irsk, Italiensk, Japansk, Javanesisk, Kannada, Kasakhisk, Khmer, Kinyarwanda, Koreansk, Krio, Kurdisk, Kurdisk Sorani, Kirgisisk, Laotisk, Latin, Latvisk, Lingala, Litauisk, Luxemburgsk, Makedonsk, Maithili, Malagassisk, Malayisk, Malayalam, Maltesisk, Maori, Marathi, Mizo, Mongolsk, Nepalesisk, Nordlig Sotho, Norsk Bokmål, Nyanja, Odia, Oromo, Pashto, Persisk, Polsk, Portugisisk, Punjabi, Rumensk, Russisk, Samoisk, Sanskrit, Skotsk gælisk, Serbisk, Shona, Sindhi, Singalesisk, Slovakisk, Slovensk, Somalisk, Sørlig Sotho, Spansk, Sundanesisk, Swahili, Svensk, Tadsjikisk, Tamilsk, Tatarisk, Telugisk, Thailandsk, Tsonga, Tyrkisk, Turkmensk, Ukrainsk, Urdu, Uigurisk, Usbekisk, Vietnamesisk, Walisisk, Xhosa, Jiddisk, Yoruba, Zulu.

## Sikkerhetskopiering og Gjenoppretting

Bruk denne funksjonen til å sikkerhetskopiere alle applikasjonsdataene dine eller migrere dem til en annen enhet. Du kan velge hva som skal inkluderes:

- **Database** — alle sporene dine i musikkbiblioteket, inkludert spillelister. Frakoblede spor er ikke inkludert for å holde sikkerhetskopifilen håndterbar.
- **Albumomslag** — alle bufrede albumomslag.
- **Innstillinger** — alle applikasjonsinnstillingene dine.

Trykk på **Sikkerhetskopier applikasjonsdata** for å starte sikkerhetskopieringen. Applikasjonsdata skrives til én fil du kan bruke senere til å gjenopprette applikasjonstilstanden på en ny enhet eller etter å ha installert applikasjonen på nytt.

For å gjenopprette applikasjonsdata på en ny enhet, flytt sikkerhetskopifilen til den nye enheten ved hjelp av en tilkoblet skytjeneste eller iCloud og åpne den på den nye enheten.

Detaljerte trinn-for-trinn-instruksjoner: [Slik overfører du musikkbiblioteket ditt mellom enheter: Trinn-for-trinn-guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Hjelp

Åpne applikasjonsveiledningen for hjelp og veiledning om effektiv bruk av appen.

## Ofte Stilte Spørsmål

Finn svar på vanlige spørsmål i FAQ-seksjonen.

## Send Tilbakemelding

Har du tilbakemelding eller trenger du hjelp? Send tilbakemeldingen din til støtteteamet vårt direkte fra appen.

## Del Denne Appen

Del applikasjonen med vennene dine for å spre ordet.

## Oppdag Flere Apper

Utforsk andre apper fra Everappz.

## Vilkår og Betingelser

Beskriver vilkårene og betingelsene for bruk av applikasjonen. Les dem før du bruker applikasjonen.

## Personvernerklæring

Besøk personvernerklæringssiden for å forstå vår datahåndteringspraksis. Les den før du bruker applikasjonen.

## Analyse og Datainnsamling

Sjekk hvilke tjenester som er aktivert for analyse og datainnsamling og deaktiver de du ikke ønsker.

## Juridiske Merknader

Inneholder informasjon om hvert bibliotek som brukes i applikasjonen, sammen med app-versjonsnummer og bygge-informasjon.
