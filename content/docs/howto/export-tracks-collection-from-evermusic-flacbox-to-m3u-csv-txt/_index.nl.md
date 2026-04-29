---
title: "Hoe je een trackverzameling exporteert naar M3U, CSV en TXT in Evermusic & Flacbox"
date: 2024-01-31
description: "Leer hoe je je recenties, favorieten, afspeellijsten en albums uit Evermusic en Flacbox exporteert naar M3U-, CSV- of TXT-formaat. Ideaal voor Last.fm-scrobbling en afspelen op andere apparaten."
keywords: ["evermusic exporteren", "flacbox exporteren", "exporteren naar m3u", "afspeellijst naar csv exporteren", "m3u txt csv afspeellijst", "muziek exporteren"]
tags: ["evermusic", "recenties", "favorieten", "exporteren", "m3u", "afspeellijst", "csv", "txt", "album"]
---

{{< author-byline >}}


**Samenvatting:** Met Evermusic en Flacbox kun je elke trackverzameling (recenties, favorieten, afspeellijsten, albums) exporteren naar CSV-, TXT- of M3U-bestanden. Gebruik deze exports om te scrobblen naar Last.fm, je bibliotheek te back-uppen of je afspeellijsten op andere apparaten af te spelen.

## Introductie

Het exporteren van je recenties, favorieten, albums en afspeellijsten vanuit de app naar een extern bestand kan ontzettend handig zijn. Je kunt deze bestanden gebruiken om je luistergeschiedenis bij te werken op scrobbler-services zoals [Last.fm](http://Last.fm) of om je afspeellijsten op externe apparaten te beluisteren. Met Evermusic en Flacbox is dit proces eenvoudig. Hier laten we je zien hoe je je recenties exporteert naar CSV/TXT en je afspeellijsten naar M3U. Deze functionaliteit is echter beschikbaar voor elke trackverzameling binnen de app.

## Kies een formaat

Om je recenties te exporteren, open je het gedeelte 'Muziekbibliotheek' en selecteer je het menu-item 'Recenties'.

![muziekbibliotheek](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Tik op het volgende scherm op de knop 'Meer' in de rechterbovenhoek en kies 'Songslijst exporteren'.

![recenties exporteren](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Op het scherm 'Selecteer bestandsformaat' heb je verschillende opties - CSV, TXT, M3U.

- CSV

Dit staat voor Comma-Separated Values, ideaal om je gegevens in een overzichtelijk tabelformaat te ordenen. In het doelbestand vind je parameters zoals Artiestnaam, Albumnaam, Tracknaam, Tijdstempel (het tijdstip waarop je de tracks hebt beluisterd), Albumartiestnaam en Trackduur. Je kunt dat bestand later gebruiken om je luistergeschiedenis bij te werken op scrobbler-services zoals [Last.fm](http://Last.fm), zoals beschreven [hier](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Hier hebben we het over een gewoon tekstbestand. Het is eenvoudig en overzichtelijk, met parameters zoals Artiestnaam, Albumnaam, Tracknaam en Duur. Handig als je gewoon een lijst van tracks in tekstvorm nodig hebt.

- M3U

Dit formaat is dé standaard voor het maken van afspeellijsten. Het is geweldig omdat je je songlijst kunt exporteren en je tracks op elk apparaat kunt afspelen, zelfs als je de originele bestanden niet hebt (als je de optie absolute URL voor mediabestanden selecteert bij het exporteren). In het uitvoerbestand vind je parameters zoals Duur, Artiestnaam, Tracknaam en Mediabestandslocatie.

## CSV-formaat

Laten we nu CSV selecteren en kijken wat we ontvangen. Kies gewoon CSV en druk op de knop 'Exporteren'.

![selecteer bestandsformaat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Zodra het exporteren is voltooid, zie je een melding met twee opties. Door op 'Toon bestand' te tikken, wordt het resulterende bestand in je documentenmap getoond.

![exporteren voltooid](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Nu kun je dat bestand versturen, openen in een externe teksteditor, of gebruiken om je luistervoortgang op [Last.fm](http://Last.fm) bij te werken.

![exportmap met resultaatbestanden](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Het CSV-uitvoerbestand bevat velden in het volgende formaat:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Bijvoorbeeld:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![geëxporteerd CSV-bestand](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT-formaat

Het TXT-uitvoerbestand bevat velden in het volgende formaat:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Bijvoorbeeld:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![geëxporteerd TXT-bestand](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U-formaat

Vervolgens begeleiden we je bij het exporteren van je afspeellijst naar M3U-formaat, de de facto standaard voor afspeellijstbestanden. De belangrijkste voorwaarde voor een succesvol afspeellijst-export is dat alle bestanden in de afspeellijst op dezelfde opslaglocatie staan, of dat nu een cloudservice is zoals je Google Drive, lokale bestanden of bestanden op je apparaat. Om het exportproces te starten, open je een willekeurige afspeellijst en tik je op de knop 'Meer' in de rechterbovenhoek, en kies vervolgens het menu-item 'Songslijst exporteren'.

![afspeellijstscherm](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Selecteer op het volgende scherm het bestandsformaat 'M3U', waar je twee opties ziet voor 'Type mediabestandslocatie':

![scherm bestandsformaat voor export selecteren](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Als je 'Relatief pad' kiest, wordt de afspeellijst aangemaakt met mediabestandslocaties die relatief zijn ten opzichte van het afspeellijstbestand. Bijvoorbeeld:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Vermijd in dit geval het wijzigen van de M3U-bestandslocatie na het voltooien van de export, aangezien dit de paden naar mediabestanden zal verbreken. Om het afspelen van je afspeellijst te starten, tik je gewoon op het geëxporteerde afspeellijstbestand en de app zal automatisch de mediabestanden op je opslag vinden en het afspelen starten. Je kunt ook je afspeellijsten naar de opslag exporteren en ze vervolgens opnieuw importeren op je nieuwe apparaat.

2. Als je 'Absolute URL' kiest, genereert de app directe URL's voor je mediabestanden. Hierdoor kun je de afspeellijst op elk apparaat/elke applicatie afspelen zonder dat alle mediabestanden op dezelfde opslag hoeven te staan als het afspeellijstbestand. Deze optie wordt alleen ondersteund voor cloudopslag die directe bestands-URL's kan genereren. Houd er echter rekening mee dat de gegenereerde URL's in sommige gevallen een beperkte levensduur kunnen hebben en na verloop van tijd kunnen verlopen. Hier is de lijst met ondersteunde cloudservices: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (als in gastmodus)  

De URL van het uitvoermediabestand ziet er ongeveer zo uit:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Zodra je het 'Type mediabestandslocatie' hebt geselecteerd, tik je op 'Exporteren'. De app vraagt je om een doelmap te kiezen voor het exporteren van het M3U-bestand. Tik op 'Voltooid' om je selectie te bevestigen.

![selecteer een map](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

De app genereert een M3U-bestand en uploadt/verplaatst het naar de doelmap.

![m3u-bestand uploaden](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Zodra het exporteren is voltooid, verschijnt er een systeemmelding met de optie 'Toon bestand'.

![melding exporteren voltooid](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Door hierop te tikken wordt het geëxporteerde bestand in de app getoond.

![geëxporteerd m3u-bestand in bestandenlijst](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Als je in de vorige stap 'Relatief pad' hebt geselecteerd als 'Type mediabestandslocatie', heeft het uitvoerbestand het volgende formaat:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![m3u-voorbeeld met relatieve paden](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Voor de optie 'Absolute URL' genereert de app een M3U-bestand in het formaat:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![m3u-voorbeeld met absolute bestands-URL's](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Je kunt dat bestand openen op elk apparaat/elke applicatie die M3U-afspeellijsten ondersteunt.

![m3u-afspeellijst geopend in externe app](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Slotgedachten

Het exporteren van je tracks uit Evermusic en Flacbox geeft je volledige controle over je muziekgegevens. Of je nu je luistergeschiedenis back-upt, scrobbelt naar Last.fm of afspeellijsten op externe apparaten geniet, deze exportopties: M3U, CSV en TXT - zijn krachtige hulpmiddelen ontworpen voor flexibiliteit en compatibiliteit. Maak gebruik van deze functies om de manier waarop je je muziekverzameling organiseert, deelt en herbezoekt op verschillende platformen te verbeteren.

## FAQ

{{% details title="Welk exportformaat moet ik gebruiken voor Last.fm-scrobbling?" closed="true" %}}
Gebruik CSV. Het bevat tijdstempels en volledige metadata die vereist zijn door scrobbling-tools zoals Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Kan ik elke trackverzameling exporteren, niet alleen afspeellijsten?" closed="true" %}}
Ja. Je kunt recenties, favorieten, albums, afspeellijsten en elke andere trackverzameling in de app exporteren met dezelfde stappen.
{{% /details %}}

{{% details title="Werkt mijn M3U-afspeellijst op andere apparaten?" closed="true" %}}
Als je de optie Absolute URL kiest tijdens het exporteren, kan het M3U-bestand worden afgespeeld op elk apparaat dat M3U-afspeellijsten ondersteunt. Houd er rekening mee dat sommige cloud-URL's na verloop van tijd kunnen verlopen.
{{% /details %}}

{{% details title="Is de exportfunctie gratis?" closed="true" %}}
Ja. Het exporteren van trackverzamelingen naar M3U, CSV en TXT is beschikbaar in zowel de gratis als de premium versie van Evermusic en Flacbox.
{{% /details %}}

{{% details title="Welke cloudservices ondersteunen Absolute URL-export?" closed="true" %}}
Absolute URL-export wordt ondersteund voor iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive en WebDAV (gastmodus).
{{% /details %}}
