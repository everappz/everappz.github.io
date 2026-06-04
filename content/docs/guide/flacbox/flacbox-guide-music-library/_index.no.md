---
title: "Musikkbibliotek"
date: 2020-02-01
description: "Lær hvordan du bygger, organiserer og synkroniserer musikkbiblioteket ditt i Flacbox på iPhone, iPad og Mac. Legg til spor manuelt eller synkroniser fra skytjenester, administrer metadata, albumomslagsbilder, spillelister, favoritter, nylige og bokmerker. Inkluderer hi-res lydstøtte, MusicBrainz-taggredigerer, online og offline synkronisering og personaliseringsalternativer."
keywords: [
  "Flacbox musikkbibliotek", "synkroniser musikk fra sky", "organiser musikk-metadata",
  "rediger lydtagger Flacbox", "offline musikk synkronisering", "importer lokal musikk",
  "Flacbox spillelisteadministrasjon", "albumomslagssøk Flacbox",
  "iPhone musikk-metadata", "Flacbox app guide",
  "Flacbox MusicBrainz", "Flacbox normaliser tagger",
  "Flacbox hi-res musikkbibliotek", "Flacbox FFmpeg bibliotek",
  "Flacbox soloalbum", "Flacbox komponistvisning"
]
tags: ["musikk", "guide", "flacbox", "bibliotek"]
readingTime: 11
---


Å administrere musikkbiblioteket ditt er enkelt med Flacbox, der du uanstrengt kan organisere alle sporene dine — lokale FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE og dusinvis av andre formater — i én søkbar samling. Du har to alternativer for å bygge musikkbiblioteket ditt: manuell tillegging (du velger nøyaktig hva som legges til) eller automatisk synkronisering (Flacbox skanner utpekte skymapper og legger til nye filer automatisk når de dukker opp).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Musikkbibliotek Albumvisning" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Manuell Tillegging

For å legge til spor manuelt, trykk på ikonet **Legg til musikk** øverst til venstre og velg mapper eller filer fra en tilkoblet skylagringstjeneste eller filer på enheten din. Når du legger til spor i biblioteket, opprettes det bare lenker til disse sporene — de faktiske filene forblir på de opprinnelige stedene for å spare verdifull diskplass. Hvis du vil gjøre spor tilgjengelige offline, kan du bruke handlingen Last ned fra alternativmenyen eller aktivere frakoblet modus for spillelister og sporsamlinger.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Legg til sanger i musikkbiblioteket" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Du kan også dra-og-slippe filer inn i biblioteket i Mac-versjonen, eller bruke **Åpne filer…** / **Åpne mappe…** fra systemets filvelger på iPhone og iPad.

## Fortsett Avspilling

Gjenopprett lydspillerkøen fra den sist lagrede posisjonen hvis denne funksjonen er aktivert i applikasjonsinnstillingene. Aktiver både **Lagre lydspillerstatus** og **Lagre avspillingsposisjon** i Innstillinger → Lydspiller → Generelt for best opplevelse. Når aktivert, vises en knapp **Fortsett avspilling** øverst på hvert mappe-, album-, artist-, sjanger- og spillelisteskjerm.

## Plasseringer

Alle sporene i biblioteket ditt er gjennomtenkt gruppert etter kildetype og musikktagger. Du kan filtrere sanger etter plassering ved å bruke **Flere handlinger**-knappen øverst til høyre og velge **Filter**.

### Online Musikk

Denne seksjonen viser musikk fra dine tilkoblede skylagringstjenester. Sporene her strømmes på forespørsel; ingenting tar lokal lagringsplass med mindre du eksplisitt laster ned eller aktiverer frakoblet modus.

### Filer i Denne Applikasjonen

Her finner du musikk tilgjengelig for offline avspilling, hentet fra de lokale filene dine. Dette inkluderer filer i appens Documents-katalog.

### Filer på Denne iPhone / iPad / Mac

Denne kategorien inkluderer musikk importert til applikasjonen fra enheten din, lagt til via systemdialogen **Åpne filer…**. De originale filene forblir på sin opprinnelige plassering; Flacbox beholder bare en lenke til dem.

## Kategorier

Når du legger til spor i musikkbiblioteket ditt, leser appen automatisk lydtaggene deres og organiserer dem i kategorier som Sanger, Uspilte sanger, Album, Albumartister, Artister, Sjangre og Komponister.

## Tagg-gruppering

Disse kategoriene hjelper deg å organisere spor etter musikktagger. Når du legger til spor i musikkbiblioteket, leser appen metadataene og grupperer dem etter disse kategoriene. Hvis du ikke ser alle albumene dine, sørg for at appen har skannet hvert spor. Du kan sjekke skannefremdriften i Innstillinger → Musikkbibliotek → Metadataavlesning → Antall behandlede filer i musikkbiblioteket. Etter at metadataavleseren har fullført alle operasjoner, ser du følgende kategorier i musikkbiblioteket ditt:

- **Sanger** — alle sanger gruppert etter TRACK_TITLE-taggen. Du kan sjekke sorteringsrekkefølgen via menyen Flere handlinger øverst til høyre.
- **Uspilte sanger** — alle sanger som aldri har blitt spilt.
- **Album** — sanger gruppert etter ALBUM_NAME-taggen, og ignorerer artist-, albumartist- og komponisttagger.
- **Albumartister** — sanger gruppert kun etter ALBUM_ARTIST_TAG. Nyttig for å holde kompillasjoner og samarbeid ryddig adskilt fra soloarbeid.
- **Artister** — sanger gruppert kun etter ARTIST_TAG.
- **Sjangre** — sanger gruppert etter GENRE-taggen.
- **Komponister** — sanger gruppert etter COMPOSER-taggen — uvurderlig for klassiske musikkbiblioteker der 'komponist' er den primære navigasjonsaksen.

## Favoritter

Du kan merke sanger som favoritter på lydspillerskjermen eller ved hjelp av alternativmenyen. Favoritter vises i sin egen seksjon slik at du kan finne dem med ett trykk.

## Nylige

Denne seksjonen viser alle nylig avspilte spor. Du kan tilpasse hvor mange elementer listen beholder i Innstillinger → Bibliotek → Nylige → Endre listestørrelse, og eksportere listen til M3U / CSV / TXT for å sikkerhetskopiere lyttehistorikken din.

## Bokmerker

Du kan opprette lydbokmerker mens en sang spilles og administrere dem på dette skjermbildet — perfekt for lydbøker, lange mikser, forelesninger eller bare merke refrenet til et favorittspor. Detaljerte instruksjoner om å jobbe med lydbokmerker er tilgjengelige [her](/docs/guide/evermusic/evermusic-guide-music-library).

## Øverste Verktøylinje

Rett under navigasjonslinjen tilbyr den øverste verktøylinjen flere praktiske handlinger: Søk, Spill alle, Shuffle alle og Fortsett avspilling. Du kan vise eller skjule denne verktøylinjen med en enkel sveip ned-bevegelse.

## Søk

Søkefunksjonen lar deg finne et bestemt spor, artist, album eller sjanger i musikkbiblioteket ditt. Søk kjører lokalt mot musikkbibliotekdatabasen, så det fungerer fullt offline og returnerer resultater mens du skriver.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Musikkbibliotek Søk" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Alternativmeny

Hvert spor i musikkbiblioteket ditt har en meny med flere handlinger, tilgjengelig ved å trykke på tre-prikker-knappen nær spornavnet.

### For Individuelle Sanger

- **Spill neste** — legger sangen til toppen av spillerkøen.
- **Spill senere** — legger sangen til bunnen av spillerkøen.
- **Legg til i spilleliste** — legger sangen til en spilleliste.
- **Legg til i favoritter** — merker sangen som favoritt for rask tilgang.
- **Laste ned** — lagrer sangen i lokale filer. Den vises i **Lokale filer**-fanen og **Offline musikk**-seksjonen.
- **Redigere lydtagger** — åpner den innebygde lydtaggredigeren for å fikse manglende metadata.
- **Vis i mappe** — avslører mappen der lydfilen er lagret.
- **Vis i Finder** — for filer importert fra Mac, avslører denne handlingen mappen der lydfilen er plassert på Mac-en.
- **Åpne i** — eksporterer lydfilen til en annen app.
- **Slett fra skytjeneste** — fjerner filen fra både musikkbiblioteket og skylagringen. **Denne handlingen er irreversibel.**
- **Slett fra musikkbiblioteket** — sletter sangen fra musikkbiblioteket ditt, men filen forblir i lagringen.

### For Sangsamlinger

For sangsamlinger som Album, Artister, Sjangre eller Komponister, inkluderer alternativmenyen følgende handlinger.

- **Spill alle** — erstatter spillerkøen med sanger fra den valgte samlingen.
- **Spill neste** — legger til sanger fra denne samlingen øverst i spillerkøen.
- **Spill senere** — legger til sanger fra denne samlingen nederst i spillerkøen.
- **Legg til i spilleliste** — inkluderer sanger fra denne samlingen i en spilleliste, med mulighet for å opprette en ny.
- **Aktivere offline-modus** — laster ned sanger fra denne samlingen til lokale filer. Filer vises i **Lokale filer**-fanen og **Offline musikk**-seksjonen.
- **Rediger bilde** — endre albumomslagsbildet for sangsamlingen.
- **Legg til i arkiv** — pakk hele samlingen inn i én ZIP-fil for enkel sikkerhetskopiering eller overføring (Premium-funksjon).
- **Eksporter sangliste** — eksporter samlingen til M3U, CSV eller TXT for bruk i andre spillere eller for arkivering.
- **Slett fra musikkbiblioteket** — fjerner sangsamlingen fra musikkbiblioteket ditt. Denne handlingen sletter ikke de faktiske filene fra lagringen.

## Valgmodus

Du kan aktivere valgmodus ved hjelp av Flere handlinger-knappen øverst til høyre. I denne modusen kan du velge flere spor på en gang og utføre batchhandlinger.

## Albumdetaljer

Når du åpner seksjonene Artister, Albumartister eller Komponister, ser du en bryter for Sanger / Alle album / Eksklusive album / Soloalbum.

- **Sanger** — viser alle sanger der denne Artisten / Albumartisten / Komponisten vises i lydtaggene.
- **Alle album** — viser kompillasjonsalbum og alle album der artisten er til stede i det hele tatt.
- **Eksklusive album** — viser album der den angitte artisten er den eneste artisten med det albumnavnet.
- **Soloalbum** — viser album der bare den angitte artistens spor vises.

Dette er særlig nyttig for å rydde opp i rotete 'Various Artists'-kompillasjoner i store biblioteker.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Albumdetaljskjerm" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Innstillinger

Trykk på Flere handlinger → Innstillinger for å konfigurere musikkbibliotekpreferansene dine.

### Metadataavlesning

Når du legger til spor i biblioteket, begynner **metadataavleseren** å jobbe. Denne bakgrunnsprosessen leser alle metadata fra sporene dine og organiserer dem etter Artist, Album, Sjanger og Komponist.

**Metadataavlesning i bakgrunnen** når slått på, fortsetter avleseren å jobbe i bakgrunnsmodus.

**Normaliser metadata-koding** når aktivert, normaliserer appen automatisk metadata-koding for alle sanger.

**Laste inn metadata på nytt** merker hver fil i musikkbiblioteket ditt som manglende metadata, noe som får metadataavleseren til å oppdatere hver post.

**Start metadataavlesning** utløser avleseren manuelt.

### Online Synkronisering

Automatisk online musikk-sync legger automatisk til spor fra tilkoblede skytjenester i musikkbiblioteket. For å aktivere den, åpne musikkbibliotekinnstillingene og velg synkroniseringsmapper.

Online sync kjører bare når appen er i forgrunnen, så synkronisering av et stort bibliotek kan ta litt tid. For å fremskynde det, hold Flacbox åpen, koble enheten til strøm og aktiver **Innstillinger → Skjerm → Alltid aktiv**.

### Offline Synkronisering

Konfigurer offline musikk-synkronisering.

#### Synkroniserte Offline-mapper

Når du markerer en online mappe på skyserveren som tilgjengelig offline (via **Flere handlinger**-menyen), vises den her. Mappeinnholdet lastes ned til **Lokale filer → Offline-mapper**.

#### Tidsintervall

Velg hvor ofte appen sjekker offline mapper for endringer.

#### Start Skanning av Lokale Mapper

Skann alle lokale mapper i applikasjonens **Dokumenter**-katalog for støttede lydfiler.

**Viktig:** Det er tilrådelig å med jevne mellomrom starte offline musikk-synkronisering for å holde musikkbiblioteket ditt oppdatert med de lokale filene dine.

### Personalisering

Konfigurer stilen på musikkbibliotekskjermen. Tre alternativer er tilgjengelige: **Enkel meny, Gruppert meny, Tabbet meny**.

### Albumomslagsbilder

Konfigurer hvordan applikasjonen laster og lagrer albumomslag.

- **Nettverkstype** — velg **Wi-Fi** eller **Wi-Fi og mobildata** for nedlasting av omslag.
- **Last inn albumomslag for online filer** — når aktivert, lastes innebygde albumomslag for filer lagret i skylagring.
- **Søk i mappen** — når aktivert, hvis et spor ikke har et innebygd omslag, ser appen etter JPEG- eller PNG-bilder i samme mappe og bruker dem som albumomslag.
- **Omslagskvalitet** — velg kvaliteten på albumomslag lagret på enheten din.
- **Vis i mappe** — åpne mappen der albumomslag er cachet.
- **Slett alle** — slett cachede albumomslag for å frigjøre lagringsplass.

### Spillelister

Aktiver alternativet for å legge til det samme nummeret i en spilleliste to ganger. Som standard er dette alternativet deaktivert.

### Nylige

Administrer listen over nylig avspilte sanger.

- **Slett liste** — slett hele listen over nylig avspilte sanger.
- **Endre listestørrelse** — angi antallet elementer som vises i listen.
- **Eksporter sangliste** — eksporter listen over nylig avspilte sanger som M3U, CSV eller TXT. Detaljerte instruksjoner er tilgjengelige [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritter

Administrer listen over favorittsangene dine.

- **Samtidig redigering** — når aktivert, legger det å legge til en sang i favoritter den til i både musikkbiblioteket og filseksjonen på en gang.
- **Slett liste** — slett hele listen over favorittsanger.
- **Eksporter sangliste** — som Nylige, eksporter favoritter som M3U, CSV eller TXT.

### Slett Bibliotek

Slett musikkbibliotekdatabasen. Musikken din i lagringen forblir urørt.

### Innholdslastegrense

Som standard bruker applikasjonen paginering for å fremskynde innholdslasting. Du kan deaktivere paginering for å laste alt på en gang.
