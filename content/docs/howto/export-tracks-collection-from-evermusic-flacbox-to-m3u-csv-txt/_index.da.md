---
title: "Sådan eksporterer du sporsamling til M3U, CSV og TXT i Evermusic og Flacbox"
date: 2024-01-31
description: "Lær hvordan du eksporterer dine seneste, favoritter, afspilningslister og albums fra Evermusic og Flacbox til M3U-, CSV- eller TXT-formater. Perfekt til Last.fm-scrobbling og afspilning på andre enheder."
keywords: ["evermusic eksport", "flacbox eksport", "eksporter til m3u", "eksporter afspilningsliste til csv", "m3u txt csv afspilningsliste", "musik eksport"]
tags: ["evermusic", "seneste", "favoritter", "eksport", "m3u", "afspilningsliste", "csv", "txt", "album"]
---

{{< author-byline >}}


**Kort sagt:** Evermusic og Flacbox lader dig eksportere enhver sporsamling (seneste, favoritter, afspilningslister, albums) til CSV-, TXT- eller M3U-filer. Brug disse eksporter til at scrobble til Last.fm, sikkerhedskopiere dit bibliotek eller afspille dine afspilningslister på andre enheder.

## Introduktion

Eksport af dine seneste, favoritter, albums og afspilningslister fra appen til en ekstern fil kan være utroligt nyttigt. Du kan bruge disse filer til at opdatere din lyttehistorik på scrobbling-tjenester som [Last.fm](http://Last.fm) eller lytte til dine afspilningslister på eksterne enheder. Med Evermusic og Flacbox er denne proces nem. Her viser vi dig, hvordan du eksporterer dine seneste til CSV/TXT og dine afspilningslister til M3U. Denne funktionalitet er dog tilgængelig for enhver sporsamling i appen.

## Vælg format

For at eksportere dine seneste, åbn sektionen 'Musikbibliotek' og vælg menupunktet 'Seneste'.

![musikbibliotek](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

På næste skærm tryk på knappen 'Flere handlinger' i øverste højre hjørne og vælg 'Eksporter sangliste'.

![eksporter seneste](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

På skærmen 'Vælg filformat' har du flere muligheder - CSV, TXT, M3U.

- CSV

Dette står for kommaseparerede værdier, perfekt til at organisere dine data i et pænt tabelformat. I destinationsfilen finder du parametre som kunstnernavn, albumnavn, spornavn, tidsstempel (tidspunktet du lyttede til sporene), albumkunstnernavn og sporvarighed. Du kan bruge denne fil senere til at opdatere din lyttehistorik på scrobbling-tjenester som [Last.fm](http://Last.fm) som beskrevet [her](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Her taler vi om en almindelig tekstfil. Den er enkel og ligetil med parametre, der inkluderer kunstnernavn, albumnavn, spornavn og varighed. Nyttig hvis du bare har brug for en liste over spor i tekstpræsentation.

- M3U

Dette format er i bund og grund go-to for oprettelse af afspilningslister. Det er fantastisk, fordi du kan eksportere din sangliste og nyde dine spor på enhver enhed, selv hvis du ikke har de originale filer (hvis du vælger den absolutte URL for mediefilernes eksportmulighed). I outputfilen finder du parametre som varighed, kunstnernavn, spornavn og mediefilplacering.

## CSV-format

Lad os nu vælge CSV og se, hvad vi modtager. Vælg blot CSV og tryk på knappen 'Eksporter'.

![vælg filformat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Når eksporten er fuldført, vil du se en advarsel med to muligheder. Tryk på 'Vis fil' for at afsløre den resulterende fil i din dokumentmappe.

![eksport fuldført](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Nu kan du sende denne fil, åbne den i en ekstern teksteditor eller bruge den til at opdatere din lyttefremgang på [Last.fm](http://Last.fm).

![eksportmappe med resultatfiler](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Output-CSV-filen vil indeholde felter i følgende format:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

For eksempel:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![eksporteret csv-fil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT-format

Output-TXT-filen vil indeholde felter i følgende format:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

For eksempel:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![eksporteret txt-fil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U-format

Dernæst guider vi dig gennem eksport af din afspilningsliste til M3U-format, som er de facto-standarden for afspilningslistefiler. Hovedforudsætningen for vellykket eksport af afspilningsliste er, at alle filer i afspilningslisten skal være placeret på det samme lager, uanset om det er i en cloudtjeneste som Google Drive, lokale filer eller filer på din enhed. For at starte eksportprocessen skal du åbne en afspilningsliste og trykke på knappen 'Flere handlinger' i øverste højre hjørne og derefter vælge menupunktet 'Eksporter sangliste'.

![afspilningslisteskærm](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

På næste skærm skal du vælge filformatet 'M3U', hvor du vil støde på to muligheder for 'Mediefilplaceringstype':

![vælg eksportfilformatskærm](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Hvis du vælger 'Relativ sti', vil afspilningslisten blive oprettet med mediefilplaceringer skrevet relativt til afspilningslistefilen. For eksempel:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   I dette tilfælde skal du undgå at ændre M3U-filplaceringen efter eksportens fuldførelse, da dette vil bryde stierne til mediefiler. For at starte afspilning af din afspilningsliste skal du blot trykke på den eksporterede afspilningslistefil, og appen vil automatisk finde mediefilerne på dit lager og starte afspilningen. Eller du kan endda eksportere dine afspilningslister til lageret og derefter importere dem igen på din nye enhed.

2. Hvis du vælger 'Absolut URL', vil appen generere direkte URL'er til dine mediefiler. Dette giver dig mulighed for at afspille afspilningslisten på enhver enhed/applikation uden at alle mediefiler skal være placeret på det samme lager som afspilningslistefilen. Denne mulighed understøttes kun af cloudlager, der er i stand til at generere direkte fil-URL'er. Husk dog, at de genererede URL'er i nogle tilfælde kan have en begrænset levetid og kan udløbe efter nogen tid. Her er listen over understøttede cloudtjenester: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (i gæstetilstand)  

Output-mediefil-URL'en vil være noget som:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Når du har valgt 'Mediefilplaceringstype', tryk på 'Eksporter'. Appen vil bede dig om at vælge en destinationsmappe til eksport af M3U-filen. Tryk på 'Færdig' for at bekræfte dit valg.

![vælg en mappe](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Appen vil generere en M3U-fil og uploade/flytte den til destinationsmappen.

![uploader m3u-fil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Når eksporten er fuldført, vises en systemadvarsel med muligheden 'Vis fil'.

![eksport fuldført advarsel](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Tryk på dette for at afsløre den eksporterede fil i appen.

![eksporteret m3u-fil i filliste](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Hvis du valgte 'Relativ sti' som 'Mediefilplaceringstype' i det forrige trin, vil outputfilen være i følgende format:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![m3u-eksempel med relative stier](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

For muligheden 'Absolut URL' vil appen generere en M3U-fil i formatet:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![m3u-eksempel med absolutte fil-URL'er](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Du kan åbne denne fil på enhver enhed/applikation, der understøtter M3U-afspilningslister.

![m3u-afspilningsliste åbnet i ekstern app](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Afsluttende tanker

Eksport af dine spor fra Evermusic og Flacbox giver dig fuld kontrol over dine musikdata. Uanset om du sikkerhedskopierer din lyttehistorik, scrobbler til Last.fm eller nyder afspilningslister på eksterne enheder, er disse eksportmuligheder: M3U, CSV og TXT - kraftfulde værktøjer skræddersyet til fleksibilitet og kompatibilitet. Udnyt disse funktioner til at forbedre, hvordan du organiserer, deler og genbesøger din musiksamling på tværs af platforme.

## FAQ

{{% details title="Hvilket eksportformat skal jeg bruge til Last.fm-scrobbling?" closed="true" %}}
Brug CSV. Det inkluderer tidsstempler og fulde metadata, som kræves af scrobbling-værktøjer som Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Kan jeg eksportere enhver sporsamling, ikke kun afspilningslister?" closed="true" %}}
Ja. Du kan eksportere seneste, favoritter, albums, afspilningslister og enhver anden sporsamling i appen ved hjælp af de samme trin.
{{% /details %}}

{{% details title="Vil min M3U-afspilningsliste fungere på andre enheder?" closed="true" %}}
Hvis du vælger muligheden Absolut URL under eksport, kan M3U-filen afspilles på enhver enhed, der understøtter M3U-afspilningslister. Bemærk, at nogle cloud-URL'er kan udløbe over tid.
{{% /details %}}

{{% details title="Er eksportfunktionen gratis?" closed="true" %}}
Ja. Eksport af sporsamlinger til M3U, CSV og TXT er tilgængelig i både de gratis og premium-versioner af Evermusic og Flacbox.
{{% /details %}}

{{% details title="Hvilke cloudtjenester understøtter Absolut URL-eksport?" closed="true" %}}
Absolut URL-eksport understøttes af iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive og WebDAV (gæstetilstand).
{{% /details %}}
