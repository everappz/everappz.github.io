---
title: "Hvordan eksportere sporsamlingen til M3U, CSV og TXT i Evermusic og Flacbox"
date: 2024-01-31
description: "Lær hvordan du eksporterer nylige, favoritter, spillelister og album fra Evermusic og Flacbox til M3U-, CSV- eller TXT-formater. Perfekt for Last.fm-scrobbling og avspilling på andre enheter."
keywords: ["evermusic eksport", "flacbox eksport", "eksporter til m3u", "eksporter spilleliste til csv", "m3u txt csv spilleliste", "musikkeksport"]
tags: ["evermusic", "recents", "favorites", "export", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**Kort fortalt:** Evermusic og Flacbox lar deg eksportere hvilken som helst sporsamling (nylige, favoritter, spillelister, album) til CSV-, TXT- eller M3U-filer. Bruk disse eksportene til å scrobble til Last.fm, sikkerhetskopiere biblioteket ditt eller spille spillelistene dine på andre enheter.

## Introduksjon

Å eksportere nylige, favoritter, album og spillelister fra appen til en ekstern fil kan være utrolig nyttig. Du kan bruke disse filene til å oppdatere lyttehistorikken din på scrobbler-tjenester som [Last.fm](http://Last.fm), eller lytte til spillelistene dine på eksterne enheter. Med Evermusic og Flacbox er denne prosessen enkel. Her viser vi deg hvordan du eksporterer nylige til CSV/TXT og spillelistene dine til M3U. Denne funksjonaliteten er imidlertid tilgjengelig for alle sporsamlinger i appen.

## Velg format

For å eksportere nylige, åpne seksjonen «Musikkbibliotek» og velg menyelementet «Nylige».

![musikkbibliotek](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

På neste skjermbilde trykker du på «Mer»-knappen øverst til høyre og velger «Eksporter sangliste».

![eksporter nylige](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

På skjermbildet «Velg filformat» har du flere alternativer – CSV, TXT, M3U.

- CSV

Dette står for Comma-Separated Values, perfekt for å organisere dataene dine i et ryddig tabellformat. I målfilen finner du parametere som artistnavn, albumnavn, spornavn, tidsstempel (tidspunktet du lyttet til sporene), albumartistnavn og sporvarighet. Du kan bruke denne filen senere til å oppdatere lyttehistorikken din på scrobbler-tjenester som [Last.fm](http://Last.fm) som beskrevet [her](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Her snakker vi om en ren tekstfil. Den er enkel og grei, med parametere som artistnavn, albumnavn, spornavn og varighet. Nyttig hvis du bare trenger en liste over spor i tekstformat.

- M3U

Dette formatet er i praksis standarden for å lage spillelister. Det er flott fordi du kan eksportere sanglisten din og nyte sporene dine på hvilken som helst enhet, selv om du ikke har originalfilene (hvis du velger alternativet for absolutt URL for mediefiler ved eksport). I utdatafilen finner du parametere som varighet, artistnavn, spornavn og mediefillokasjon.

## CSV-format

La oss nå velge CSV og se hva vi får. Velg bare CSV og trykk på «Eksporter»-knappen.

![velg filformat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Når eksporten er fullført, vil du se et varsel med to alternativer. Ved å trykke «Vis fil» vises den resulterende filen i dokumentmappen din.

![eksport fullført](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Nå kan du sende filen, åpne den i en ekstern teksteditor eller bruke den til å oppdatere lyttefremdriften din på [Last.fm](http://Last.fm).

![eksportmappe med resultatfiler](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

CSV-utdatafilen vil inneholde felt i følgende format:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

For eksempel:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![eksportert csv-fil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT-format

TXT-utdatafilen vil inneholde felt i følgende format:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

For eksempel:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![eksportert txt-fil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U-format

Nå vil vi guide deg gjennom eksportering av spillelisten din til M3U-format, som er den faktiske standarden for spillelistefiler. Hovedforutsetningen for vellykket spillelisteeksport er at alle filene i spillelisten må være plassert på samme lagringsplass, enten det er en skytjeneste som Google Drive, lokale filer eller filer på enheten din. For å starte eksportprosessen, åpne en spilleliste og trykk på «Mer»-knappen øverst til høyre, og velg deretter menyelementet «Eksporter sangliste».

![spillelisteskjerm](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

På neste skjermbilde velger du filformatet «M3U», der du vil møte to alternativer for «Type mediefillokasjon»:

![velg eksportfilformat-skjerm](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Hvis du velger «Relativ bane», vil spillelisten bli opprettet med mediefillokasjonene skrevet relativt til spillelistefilen. For eksempel:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   I dette tilfellet bør du unngå å endre plasseringen av M3U-filen etter at eksporten er fullført, da dette vil bryte stiene til mediefilene. For å starte avspilling av spillelisten, trykk bare på den eksporterte spillelistefilen, så vil appen automatisk finne mediefilene på lagringsplassen din og starte avspillingen. Du kan til og med eksportere spillelistene dine til lagringsplassen og deretter importere dem igjen på den nye enheten din.

2. Hvis du velger «Absolutt URL», vil appen generere direkte URLer for mediefilene dine. Dette lar deg spille spillelisten på hvilken som helst enhet/applikasjon uten at alle mediefilene trenger å være plassert på samme lagringsplass som spillelistefilen. Dette alternativet støttes kun for skylagring som kan generere direkte fil-URLer. Vær imidlertid oppmerksom på at de genererte URLene i noen tilfeller kan ha en begrenset levetid og kan utløpe etter en stund. Her er listen over støttede skytjenester: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (hvis i gjestemodul)  

Den resulterende mediefil-URLen vil se omtrent slik ut:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Når du har valgt «Type mediefillokasjon», trykker du «Eksporter». Appen vil be deg velge en målmappe for eksport av M3U-filen. Trykk «Ferdig» for å bekrefte valget.

![velg en mappe](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Appen vil generere en M3U-fil og laste opp/flytte den til målmappen.

![laster opp m3u-fil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Når eksporten er fullført, vises et systemvarsel med muligheten til å «Vise fil».

![eksport fullført-varsel](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Ved å trykke på dette vises den eksporterte filen i appen.

![eksportert m3u-fil i fillisten](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Hvis du valgte «Relativ bane» som «Type mediefillokasjon» i forrige trinn, vil utdatafilen være i følgende format:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![m3u-eksempel med relative baner](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

For alternativet «Absolutt URL» vil appen generere en M3U-fil i formatet:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![m3u-eksempel med absolutte fil-URLer](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Du kan åpne denne filen på hvilken som helst enhet/applikasjon som støtter M3U-spillelister.

![m3u-spilleliste åpnet i ekstern app](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Avsluttende tanker

Å eksportere sporene dine fra Evermusic og Flacbox gir deg full kontroll over musikkdataene dine. Enten du sikkerhetskopierer lyttehistorikken din, scrobbler til Last.fm eller nyter spillelister på eksterne enheter, er disse eksportalternativene – M3U, CSV og TXT – kraftige verktøy skreddersydd for fleksibilitet og kompatibilitet. Dra nytte av disse funksjonene for å forbedre måten du organiserer, deler og gjenopplever musikksamlingen din på tvers av plattformer.

## FAQ

{{% details title="Hvilket eksportformat bør jeg bruke for Last.fm-scrobbling?" closed="true" %}}
Bruk CSV. Det inkluderer tidsstempler og fullstendige metadata som kreves av scrobblerverktøy som Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Kan jeg eksportere hvilken som helst sporsamling, ikke bare spillelister?" closed="true" %}}
Ja. Du kan eksportere nylige, favoritter, album, spillelister og alle andre sporsamlinger i appen ved å bruke de samme trinnene.
{{% /details %}}

{{% details title="Vil M3U-spillelisten min fungere på andre enheter?" closed="true" %}}
Hvis du velger alternativet Absolutt URL under eksport, kan M3U-filen spilles av på hvilken som helst enhet som støtter M3U-spillelister. Merk at noen sky-URLer kan utløpe over tid.
{{% /details %}}

{{% details title="Er eksportfunksjonen gratis?" closed="true" %}}
Ja. Eksport av sporsamlinger til M3U, CSV og TXT er tilgjengelig i både gratis- og premiumversjonene av Evermusic og Flacbox.
{{% /details %}}

{{% details title="Hvilke skytjenester støtter eksport med absolutt URL?" closed="true" %}}
Eksport med absolutt URL støttes for iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive og WebDAV (gjestemodus).
{{% /details %}}
