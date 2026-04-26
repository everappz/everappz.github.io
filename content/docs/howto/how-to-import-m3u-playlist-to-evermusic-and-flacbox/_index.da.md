---
title: "Sådan importerer du M3U-afspilningsliste til Evermusic og Flacbox"
date: 2024-01-31
description: "Lær hvordan du importerer M3U-, M3U8- og CUE-afspilningslistefiler fra sky, lokal lagring eller enhed til Evermusic og Flacbox."
keywords: ["evermusic", "flacbox", "afspilningsliste", "m3u", "m3u8", "cue", "importere", "musik-app"]
tags: ["evermusic", "importere", "afspilningslister", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Resumé:** Evermusic og Flacbox understøtter import af M3U-, M3U8- og CUE-afspilningslistefiler fra skylagring, lokale app-filer eller din enhed. Gå til Afspilningslister > Mere > Importer afspilningsliste, vælg en kilde, vælg din fil, og appen bygger din afspilningsliste automatisk.

M3U, som står for MP3 URL eller Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, er et computerfilformat, der bruges til multimedieafspilningslister. En af dets primære anvendelser er at oprette afspilningslistefiler med én post, der peger på streams på internettet. Disse filer giver nem adgang til streamingindhold og bruges ofte til downloads, e-mail og lytning til internetradio.

På trods af den udbredte brug er der ingen formel specifikation for M3U-formatet; det er blevet en de facto-standard. En M3U-fil er i bund og grund en ren tekstfil, der angiver placeringerne af en eller flere mediefiler. Afhængigt af kodningen gemmes den med enten filtypenavnet "m3u" eller "m3u8". Hver post i filen angiver en mediefils placering, som kan være et absolut lokalt stinavn, et lokalt stinavn relativt til M3U-filens placering eller en URL. Poster adskilles af linjeskift, hvor nogle enheder kræver linjeskift repræsenteret som CR LF.

Derudover kan M3U-filer indeholde kommentarer med præfikset "#". I udvidet M3U introducerer "#" udvidede M3U-direktiver, som kan understøtte parametre afsluttet med kolon ":".

I vores apps Evermusic og Flacbox har vi implementeret M3U-filimportfunktionalitet, hvilket eliminerer behovet for manuel oprettelse af afspilningslister. Denne guide vil lede dig gennem import af dine afspilningslister fra skylagring, lokale filer eller filer på din enhed direkte ind i appen.

Først navigerer du til sektionen 'Afspilningslister'. Dernæst trykker du på knappen 'Mere' i øverste højre hjørne. Fra menuen der vises, vælger du muligheden 'Importer afspilningsliste'.

![importer afspilningsliste-handling](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

På den næste skærm vælger du filplaceringen. Understøttede muligheder inkluderer:

- Forbundet skylagring;
- Filer i applikationen;
- Filer på din enhed;

![vælg filplacering](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Lad os vælge forbundet skylagring og åbne mappen, der indeholder afspilningslistefilen. Understøttede filtyper for afspilningslister inkluderer M3U, M3U8 og CUE. Vælg afspilningslistefilen og tryk 'Færdig' for at bekræfte dit valg.

![vælg M3U-fil](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Appen vil analysere afspilningslistefilen og oprette en liste over numre. Den vil derefter finde disse filer på lagringen og sammensætte en endelig afspilningsliste, der importeres til musikbiblioteket. Det er afgørende, at din M3U/CUE-fil indeholder de korrekte stier til mediefiler, og filerne skal befinde sig på disse stier i din lagring.

![importeret afspilningsliste](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Appen understøtter både relative stier og absolutte fil-URL'er.

For eksempel:

Afspilningsliste med relative stier:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Afspilningsliste med absolutte URL'er:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Hvis du importerer en afspilningslistefil, der er placeret i appen (sektionen Lokale filer), er der ingen yderligere trin nødvendige.

Hvis du dog vil importere en afspilningsliste, der er placeret på din enhed ved hjælp af systemets filvælger, er der en vigtig overvejelse at huske på.

På grund af sikkerhedspolitikker kan applikationen kun få adgang til den fil, du vælger ved hjælp af systemets filvælger. Afspilningslistefilen kan dog indeholde links til andre mediefiler på din enhed. For at importere en afspilningsliste fra din enhed skal du vælge en mappe, der indeholder både afspilningslistefilen og alle mediefiler, der er linket til den. I dette tilfælde vil appen scanne den valgte mappe, finde afspilningslistefilen, opbygge numlisten og importere den til musikbiblioteket.

Derudover kan du importere flere afspilningslister på én gang ved at trykke på knappen "Flere handlinger" og vælge "Importer afspilningslister fra en mappe". Appen vil derefter scanne mappens indhold, finde understøttede afspilningslistefiler og importere dem til biblioteket.

## Ofte stillede spørgsmål

{{% details title="Hvilke afspilningslisteformater understøtter Evermusic og Flacbox?" closed="true" %}}
Begge apps understøtter M3U-, M3U8- og CUE-afspilningslistefilformater. Disse dækker de mest almindelige afspilningslistestandarder, der bruges af musikafspillere og mediesoftware.
{{% /details %}}

{{% details title="Kan jeg importere afspilningslister fra skylagring?" closed="true" %}}
Ja. Du kan importere afspilningslistefiler fra enhver forbundet skylagringstjeneste, herunder Google Drive, Dropbox, OneDrive og WebDAV-servere.
{{% /details %}}

{{% details title="Hvorfor mangler nogle numre efter import?" closed="true" %}}
Afspilningslistefilen skal indeholde korrekte stier til dine mediefiler, og disse filer skal eksistere på de angivne placeringer i din lagring. Dobbelttjek at filstierne i din M3U- eller CUE-fil matcher de faktiske filplaceringer.
{{% /details %}}

{{% details title="Kan jeg importere flere afspilningslister på én gang?" closed="true" %}}
Ja. Brug knappen Flere handlinger og vælg "Importer afspilningslister fra en mappe". Appen scanner mappen for alle understøttede afspilningslistefiler og importerer dem i ét trin.
{{% /details %}}

{{% details title="Skal jeg oprette afspilningslister manuelt?" closed="true" %}}
Nej. Importfunktionen eliminerer manuel oprettelse af afspilningslister. Peg bare appen mod din eksisterende M3U-, M3U8- eller CUE-fil, og den bygger afspilningslisten automatisk.
{{% /details %}}
