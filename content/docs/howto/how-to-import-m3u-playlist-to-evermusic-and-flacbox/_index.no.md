---
title: "Hvordan importere M3U-spilleliste til Evermusic og Flacbox"
date: 2024-01-31
description: "Lær hvordan du importerer M3U-, M3U8- og CUE-spillelistefiler fra sky, lokal lagring eller enhet til Evermusic og Flacbox."
keywords: ["evermusic", "flacbox", "spilleliste", "m3u", "m3u8", "cue", "importere", "musikk-app"]
tags: ["evermusic", "importere", "spillelister", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Sammendrag:** Evermusic og Flacbox støtter importering av M3U-, M3U8- og CUE-spillelistefiler fra skylagring, lokale appfiler eller enheten din. Gå til Spillelister > Mer > Importer spilleliste, velg en kilde, velg filen din, og appen bygger spillelisten automatisk.

M3U, som står for MP3 URL eller Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, er et datafilformat som brukes for multimediespillelister. En av de primære bruksområdene er å lage spillelistefiler med én oppføring som peker til strømmer på internett. Disse filene gir enkel tilgang til strømmeinnhold og brukes ofte til nedlastinger, e-post og lytting til internettradio.

Til tross for utbredt bruk finnes det ingen formell spesifikasjon for M3U-formatet; det har blitt en de facto-standard. En M3U-fil er i bunn og grunn en ren tekstfil som spesifiserer plasseringene til én eller flere mediefiler. Avhengig av kodingen lagres den med enten filtypen "m3u" eller "m3u8". Hver oppføring i filen spesifiserer plasseringen til en mediefil, som kan være et absolutt lokalt banenavn, et lokalt banenavn relativt til M3U-filens plassering eller en URL. Oppføringer skilles med linjeskift, og noen enheter krever linjeskift representert som CR LF.

I tillegg kan M3U-filer inneholde kommentarer som innledes med "#"-tegnet. I utvidet M3U introduserer "#" utvidede M3U-direktiver, som kan støtte parametere avsluttet med kolon ":".

I våre apper Evermusic og Flacbox har vi implementert M3U-filimportfunksjonalitet, som eliminerer behovet for manuell oppretting av spillelister. Denne veiledningen tar deg gjennom importering av spillelistene dine fra skylagring, lokale filer eller filer på enheten din direkte inn i appen.

Først navigerer du til 'Spillelister'-seksjonen. Deretter trykker du på 'Mer'-knappen øverst til høyre. Fra menyen som vises, velger du alternativet 'Importer spilleliste'.

![importer spilleliste-handling](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

På neste skjerm velger du filplasseringen. Støttede alternativer inkluderer:

- Tilkoblet skylagring;
- Filer i applikasjonen;
- Filer på enheten din;

![velg filplassering](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

La oss velge tilkoblet skylagring og åpne mappen som inneholder spillelistefilen. Støttede spillelistefiltyper inkluderer M3U, M3U8 og CUE. Velg spillelistefilen og trykk 'Ferdig' for å bekrefte valget ditt.

![velg M3U-fil](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Appen vil analysere spillelistefilen og opprette en liste over spor. Den vil deretter finne disse filene på lagringen og sette sammen en endelig spilleliste som importeres til musikkbiblioteket. Det er avgjørende at M3U/CUE-filen din inneholder riktige baner for mediefiler, og filene bør finnes på disse banene på lagringen din.

![importert spilleliste](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Appen støtter både relative baner og absolutte fil-URL-er.

For eksempel:

Spilleliste med relative baner:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Spilleliste med absolutte URL-er:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Hvis du importerer en spillelistefil som er plassert i appen (Lokale filer-seksjonen), kreves det ingen ekstra trinn.

Hvis du imidlertid ønsker å importere en spilleliste som er plassert på enheten din ved hjelp av systemfilvelgeren, er det et viktig hensyn å huske på.

På grunn av sikkerhetspolicyer kan applikasjonen bare få tilgang til filen du velger ved hjelp av systemfilvelgeren. Spillelistefilen kan imidlertid inneholde lenker til andre mediefiler på enheten din. For å importere en spilleliste fra enheten din må du velge en mappe som inneholder både spillelistefilen og alle mediefiler som er lenket til den. I dette tilfellet vil appen skanne den valgte mappen, finne spillelistefilen, bygge sporlisten og importere den til musikkbiblioteket.

I tillegg kan du importere flere spillelister samtidig ved å trykke på "Flere handlinger"-knappen og velge "Importer spillelister fra en mappe." Appen vil deretter skanne mappens innhold, finne støttede spillelistefiler og importere dem til biblioteket.

## Ofte stilte spørsmål

{{% details title="Hvilke spillelisteformater støtter Evermusic og Flacbox?" closed="true" %}}
Begge appene støtter M3U-, M3U8- og CUE-spillelistefilformater. Disse dekker de vanligste spillelistestandardene som brukes av musikkspillere og medieprogramvare.
{{% /details %}}

{{% details title="Kan jeg importere spillelister fra skylagring?" closed="true" %}}
Ja. Du kan importere spillelistefiler fra enhver tilkoblet skylagringstjeneste, inkludert Google Drive, Dropbox, OneDrive og WebDAV-servere.
{{% /details %}}

{{% details title="Hvorfor mangler noen spor etter import?" closed="true" %}}
Spillelistefilen må inneholde riktige baner til mediefilene dine, og disse filene må eksistere på de angitte plasseringene på lagringen din. Dobbeltsjekk at filbanene i M3U- eller CUE-filen din samsvarer med de faktiske filplasseringene.
{{% /details %}}

{{% details title="Kan jeg importere flere spillelister samtidig?" closed="true" %}}
Ja. Bruk knappen Flere handlinger og velg "Importer spillelister fra en mappe." Appen skanner mappen for alle støttede spillelistefiler og importerer dem i ett trinn.
{{% /details %}}

{{% details title="Må jeg opprette spillelister manuelt?" closed="true" %}}
Nei. Importfunksjonen eliminerer manuell oppretting av spillelister. Bare pek appen til din eksisterende M3U-, M3U8- eller CUE-fil, og den bygger spillelisten automatisk.
{{% /details %}}
