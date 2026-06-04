---
date: 2020-01-01
title: 'Flacbox'
description: "Leer hoe je Flacbox gebruikt — de hi-res FLAC, DSD, ALAC en FFmpeg-aangedreven cloudmuziekspeler voor iPhone, iPad en Mac. Verbind iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB en DLNA. Stream en download hoge-resolutie audio, bewerk metadata, luister naar audioboeken, scrobble naar Last.fm, gebruik Apple CarPlay en beginschermwidgets en pas de 10-band equalizer aan."
keywords: [
  "Flacbox gebruikersgids", "Flacbox handleiding", "hi-res muziekspeler iPhone", "FLAC-speler iPhone",
  "DSD-speler iOS", "ALAC-speler Mac", "lossless muziekapp", "cloudmuziekspeler iPhone",
  "offline FLAC-speler Mac", "muziekbibliotheekbeheer", "audiotag-editor",
  "CarPlay FLAC-speler", "Chromecast audio-app", "AirPlay 2 muziek",
  "Flacbox widgets", "Flacbox CarPlay", "FFmpeg muziekspeler iOS",
  "audioboekspeler iPhone", "audio bladwijzers iOS", "toonhoogtecorrectie muziekapp",
  "audio-uitvoer samplerate", "externe DAC iPhone", "USB DAC Mac",
  "Synology muziekapp", "QNAP muziekapp", "NAS muziekspeler iPhone",
  "WebDAV muziekspeler", "SMB muziekstreaming", "DLNA muziekspeler",
  "iCloud Drive muziek", "Google Drive FLAC", "Dropbox FLAC-speler",
  "Wi-Fi Drive muziekoverdracht", "M3U afspeellijst importeren", "Last.fm scrobbling"
]
tags: ["flacbox", "gids", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widgets"]
---


### Welkom bij de Flacbox Gids

Flacbox is een hoge-resolutie muziekspeler voor iPhone, iPad en Mac waarmee je je favoriete cloudopslag, NAS en mediaservers kunt omzetten in je eigen persoonlijke streamingdienst.

Flacbox verbindt met een indrukwekkend breed scala aan bronnen, allemaal in één app:

- **Persoonlijke cloudopslag:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Zelf-gehoste servers:** Plex · Jellyfin · Emby · Subsonic (en elke Subsonic-compatibele server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (en ownCloud via de gedeelde API) · Synology Drive · QNAP.
- **NAS en bestandsdelingsprotocollen:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (wachtwoord of publieke-sleutelauthenticatie) · NFS · DLNA / UPnP (afspelen en downloaden). Werkt met Apple Time Capsule, Synology, QNAP, WD My Cloud, elke Linux Samba / NFS / SSH-host of een gedeelde map op je Mac of Windows-pc.
- **S3-compatibele objectopslag:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces en elk ander S3-API-eindpunt.
- **Lokaal netwerk ontdekking:** De sectie Beschikbare apparaten toont automatisch elke Bonjour / mDNS-service op je Wi-Fi — Plex, Jellyfin, Emby-servers, Synology, QNAP, AirPort-routers met aangesloten schijven, Time Capsule — zodat je kunt tikken om verbinding te maken zonder een IP-adres in te typen.

Waar de meeste muziekapps vasthouden aan de ingebouwde audio-engine van Apple, bundelt Flacbox **FFmpeg** naast de systeemcodecs zodat je formaten kunt afspelen die iOS niet standaard ondersteunt — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, plus de reguliere familie MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. Gecombineerd met een configureerbare audio-uitvoer samplerate (44,1 / 48 / 64 / 88,2 / 96 kHz), meerkanaals uitvoer (Mono → 5.1 → SDDS → ITU BS.775-1), IO-buffer afstemming en toonhoogtecorrectie geeft Flacbox audiofiele controle die de meeste consumenten muziekapps eenvoudigweg niet bieden.

### Geniet van Vloeiend Streamen en Offline Afspelen

Flacbox heeft slimme buffering voor vloeiend streamen en een ingebouwde downloadmanager zodat je volledige afspeellijsten, artiesten, albums, mappen of individuele nummers naar je apparaat kunt downloaden voor offline gebruik. Als je opslagruimte opraakt, verwijder je gecachte bestanden met één tik en ga je door met streamen vanuit de cloud. De offlinemodus voor mappen, afspeellijsten, albums en artiesten synchroniseert ook automatisch nieuwe nummers zodra ze in de cloud verschijnen, zodat je offline collectie altijd actueel blijft.

### Automatisch Georganiseerde Muziekbibliotheek

Wanneer je audiotracks importeert, scant Flacbox hun metadata en organiseert ze in een overzichtelijke muziekbibliotheek — gegroepeerd op Nummers, Niet-afgespeelde nummers, Albums, Albumartiesten, Artiesten, Genres en Componisten. Gebruik de ingebouwde zoekfunctie om alles in seconden te vinden, filter op bron (online cloud / offline / apparaat) en kies tussen de bibliotheekindelingen Eenvoudig / Gegroepeerd / Tabbladen. Voor bibliotheken met gemengde compilaties met 'verschillende artiesten' biedt Flacbox speciale weergaven Alle Albums / Exclusieve Albums / Solo Albums om de juiste resultaten te tonen zonder ruis.

### Metadata Repareren en Muziek Taggen

Als je beschadigde tags of rommelige coderingen tegenkomt (een veelvoorkomend probleem bij geripte of oudere bestanden), kan de ingebouwde ID3-tageditor ze opschonen — handmatig of met automatische MusicBrainz-lookups. Je kunt ook gebroken tekencodering normaliseren (geweldig voor Cyrillische, Japanse of Chinese tags van Windows-pc's), ontbrekende albumhoezen zoeken en wijzigingen automatisch terugschrijven naar het originele bestand in de cloud. Voor diepgaandere batchbewerking, installeer onze bijgeleverde app Evertag.

### Eenvoudige Overdrachten van Mac, PC of NAS

Verplaats muziek tussen je computer en je iPhone of iPad met een van deze tools: SMB, WebDAV, DLNA, Wi-Fi Drive (slepen en neerzetten in elke desktopbrowser), iTunes / Finder Bestandsdeling via een Lightning- of USB-C-kabel, USB-flashdrives of iXpand-flashdrives. Heb je een Apple Time Capsule, WD My Cloud, Synology, QNAP of een andere NAS die SMB / WebDAV / DLNA / FTP / SFTP biedt? Verbind één keer en stream je hele bibliotheek zonder opslagruimte op je apparaat te gebruiken.

### Pas Je Geluid Aan met de Equalizer

Flacbox bevat een 10-band equalizer met iPod-stijl presets (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz en nog veel meer), een voorversterker en de mogelijkheid om je eigen presets op te slaan. Of je nu afstemt voor een paar audiofiele IEM's, een HomePod mini of een autoradio, je kunt het geluid precies naar wens vormgeven.

### Audioboek Vriendelijk

Flacbox is een geweldige audiospeler voor audioboeken — meerdere bladwijzers per track, nauwkeurige afspeelsnelheid (0,02× tot 3,00×), doorgaan met afspelen om precies te hervatten waar je gestopt was, aanpasbare overslaknoppen en een slaaptimer die zachtjes vervaagt bij bedtijd. M4B-hoofdstukmarkeringen en lange bestanden worden volledig ondersteund.

### Stream Overal — Ook in Je Auto en op Je Beginscherm

Stream muziek naar Apple TV / HomePod via AirPlay 2, stuur het naar Google Chromecast-luidsprekers en Cast-compatibele tv's en neem alles mee onderweg met Apple CarPlay. Gebruik beginschermwidgets op iPhone en iPad om het huidige nummer in één oogopslag te zien, en Last.fm-scrobbling om je luistergeschiedenis bij te houden in alle apps.

### Privacy en Beveiliging

Flacbox gebruikt alleen officiële SDK's en OAuth-gebaseerde logins van elke cloudprovider — je wachtwoord bereikt de app nooit. Toegangstokens worden versleuteld opgeslagen in de iOS Keychain, alle overdrachten zijn TLS-beveiligd en het intrekken van toegang in je cloudaccount of het verwijderen van Flacbox van het apparaat verwijdert alles onmiddellijk. Bescherm je bibliotheek met een optionele toegangscode voor een extra laag privacy.

### Aan de Slag met Flacbox

Deze gids leidt je door elk onderdeel van Flacbox op iPhone, iPad en Mac — van het verbinden van clouddiensten, het organiseren van je bibliotheek, het overdragen van bestanden en het beheren van afspeellijsten, tot het fijn afstellen van de equalizer en het configureren van de audio-engine. Gebruik de kaarten hieronder om direct naar het gewenste gedeelte te springen.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigatie" subtitle="Tabbalk op iPhone, Linkermenu op iPad en Mac, minispeler, widgets, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Verbindingen" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Muziekbibliotheek" subtitle="Nummers, Albums, Artiesten, Genres, Componisten — synchroniseer, zoek, bewerk metadata." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Afspeellijsten" subtitle="Maak aan, importeer M3U / M3U8 / CUE, herorden en exporteer naar M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Lokale Bestanden" subtitle="Offline muziek, USB-schijven, Wi-Fi Drive, bestandsbeheer, offline mappen." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Audiospeler" subtitle="Hi-res uitvoer, equalizer, toonhoogte, bladwijzers, AirPlay, Chromecast, snelheid, slaaptimer." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Instellingen" subtitle="Audio-engine, bibliotheek, bestandsbeheer, CarPlay, widgets, personalisatie, taal, back-up." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="Veelgestelde vragen" subtitle="Vind antwoorden op de 50 meest gestelde vragen over Flacbox." >}}

{{< /cards >}}
