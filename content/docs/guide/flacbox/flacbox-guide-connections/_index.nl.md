---
title: "Verbindingen"
date: 2020-02-01
description: "Leer hoe je cloudservices en NAS-apparaten verbindt met Flacbox. Stream hoge-resolutie muziek van iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk en meer. Gebruik SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder Bestandsdeling en USB-flashdrives."
keywords: [
  "Flacbox cloud instellen", "Google Drive verbinden met Flacbox", "SMB muziekstreaming",
  "WebDAV iOS speler", "DLNA muziekapp", "NAS audio streaming", "Wi-Fi Drive iPhone",
  "bestanden overzetten naar iPhone", "Flacbox iTunes bestandsdeling", "NAS verbinden met iPhone",
  "Synology Drive muziekapp", "QNAP muziekapp", "Bluesound muziekapp",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm scrobbling muziekapp",
  "iXpand Flash Drive muziek", "USB DAC iPhone"
]
tags: ["gids", "flacbox", "verbindingen", "cloud", "NAS"]
readingTime: 12
---


Op dit scherm kun je elke bron verbinden die je muziek bevat. Je kunt populaire cloudservices integreren zoals Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive en nog veel meer, evenals je Mac, pc of NAS via standaardprotocollen. Of je collectie nu op een streamingvriendelijke service als Dropbox staat of op een persoonlijke NAS zoals Synology, QNAP, Buffalo, Apple Time Capsule of WD My Cloud Home, Flacbox verbindt ze allemaal vanuit één scherm.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Verbindingen Scherm" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Verbinden met Cloudopslag

- Open het tabblad **Verbindingen**.
- Selecteer **Verbinden met cloudopslag** uit het menu.
- Kies een cloudopslagdienst uit de lijst.
- Voer je gegevens in op de officiële autorisatiepagina van de cloudprovider en tik op **Voltooid**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Een Cloudopslagservice Toevoegen" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Als je problemen ondervindt, controleer dan je internetverbinding en je gebruikersnaam / wachtwoord. In de Premium-versie van de app kun je een onbeperkt aantal services toevoegen; de gratis versie ondersteunt tot drie.

## Ondersteunde Cloudopslagservices, Mediaservers en Protocollen

Flacbox ondersteunt een uitzonderlijk breed scala aan muziekbronnen. Alles hieronder werkt vanaf één **Verbinden met cloudopslag**-scherm.

**Persoonlijke cloudopslag:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Zelf-gehoste servers:** Plex · Jellyfin · Emby · Subsonic (en elke Subsonic-compatibele server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (en ownCloud via de gedeelde API) · Synology Drive · QNAP.

**NAS en bestandsdelingsprotocollen:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH-bestandsoverdrachtsprotocol, wachtwoord of publieke-sleutelauthenticatie) · NFS · DLNA / UPnP (afspelen en downloaden).

**S3-compatibele objectopslag:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces en elk ander S3-API-eindpunt.

**Lokaal netwerk ontdekking:** De sectie Beschikbare apparaten toont automatisch elke Bonjour / mDNS-service op je Wi-Fi-netwerk zodat je kunt tikken om verbinding te maken zonder een IP-adres in te typen.

Elke verbinding gebruikt de **officiële SDK of het open protocol** van de service, met OAuth-autorisatie waar ondersteund. Je kunt meerdere accounts van dezelfde service verbinden en ze naast elkaar bekijken in het Verbindingen-scherm.

## Beveiliging en Privacy

We gebruiken alleen officiële SDK's en beveiligde verbindingen om te communiceren met verbonden cloudservices. Je gebruikersnaam en wachtwoord zijn niet toegankelijk voor de applicatie — alle overdrachten zijn TLS-versleuteld.

Wanneer je je gebruikersnaam en wachtwoord invoert, toont de applicatie de officiële autorisatiepagina van de cloudserviceprovider, en vindt het volledige autorisatieproces buiten de applicatie plaats. De cloudserviceprovider stuurt vervolgens een auth-token naar de applicatie na succesvolle autorisatie, en dat token wordt gebruikt voor API-aanroepen.

Een auth-token is een digitale sleutel die externe applicaties toestaat om namens jou met cloudopslag te communiceren. Het token wordt op je apparaat opgeslagen in Apple's beveiligde systeemopslag (Keychain), die in rust versleuteld is en beschermd wordt door je apparaatwachtwoord of biometrische vergrendeling. Je kunt bestanden downloaden van verbonden cloudservices naar je apparaat; die bestanden worden geplaatst in de Documents-map van de app en kunnen op elk moment worden verwijderd met behulp van de ingebouwde bestandsbeheerder.

De applicatie deelt geen informatie van je verbonden cloudaccounts met Everappz, adverteerders of derden. Je kunt op elk moment toegang tot je cloudaccount intrekken door de accountinstellingenpagina in je webbrowser te openen.

## Auth-Token Weigeren

Om een auth-token in te trekken, log in bij je cloudaccount in een webbrowser en ga naar de beveiligingspagina of de pagina voor verbonden apps. Daar vind je elke externe app die is verbonden met je cloudaccount en kun je ze verwijderen als je ze niet meer wilt gebruiken. Gedetailleerde instructies voor Google-accounts zijn beschikbaar [hier](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Je kunt ook het cloudaccount binnen de applicatie zelf verbreken — wanneer je dat doet, wordt het auth-token onmiddellijk van je apparaat verwijderd. Als je de applicatie van je apparaat verwijdert, worden alle gedownloade gegevens en toegangstokens automatisch mee verwijderd.

## Een Cloudopslag Verbreken of Configuratie Wijzigen

- **Toegang tot cloudopslagopties** — zoek de verbonden service in het **Verbindingen**-scherm.
- **Tik op de "..."-knop** naast de servicetitel om aanvullende opties te openen:
  - **Hernoemen** — verander de naam van de cloudservice zoals die in je lijst verschijnt.
  - **Instellingen** — wijzig de configuratie of authenticatiegegevens. Soms moet je de verbonden cloudservice opnieuw autoriseren als het autorisatietoken is verlopen.
  - **Ontkoppelen** — verbreek volledig de verbinding tussen de app en de cloudservice. Dit verwijdert alle liedjes van die service uit je muziekbibliotheek in de app, maar laat ze onaangeroerd op de server.

## Verbinden met een Computer of NAS

Je kunt ook je computer, persoonlijke NAS of andere netwerkapparaten verbinden met behulp van de SMB-, DLNA- of WebDAV-protocollen. Dit is de eenvoudigste manier om een bestaande thuis-muziekbibliotheek — of die nu op een Mac, Windows-pc, Synology-box of NAS staat — in Flacbox te brengen zonder iets te kopiëren.

## Verbinden met een Computer via SMB

- Tik op **Verbinden met cloudopslag → SMB**.
- Voer het IP-adres van de computer en de naam van de gedeelde map in het URL-veld in met het formaat `smb://computer-ip-address/shared-folder-name`.
- Kies de protocolversie: **Auto**, **SMB1** of **SMB2**.
- Voer je gebruikersnaam en wachtwoord in (indien vereist).
- Tik op **Voltooid**.

Als de verbinding succesvol is, zie je de verbonden opslag in de sectie **Cloudopslag**. Een volledige tutorial over het verbinden van je Mac of pc via SMB is beschikbaar [hier](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Verbinden met een NAS via WebDAV

Alle stappen zijn hetzelfde als bij SMB, behalve het URL-veld. De URL moet het formaat `http://server-name` of `https://server-name` hebben als de server SSL ondersteunt. WebDAV werkt met **Synology, QNAP, Nextcloud, ownCloud** en vele andere servers.

Een volledige tutorial over het verbinden van een NAS via WebDAV is beschikbaar [hier](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Verbinden met een Computer of NAS via DLNA

Je kunt ook een muziekbibliotheek op je Windows-pc of persoonlijke NAS delen via het DLNA / UPnP-protocol en die bibliotheek in de app openen zoals beschreven [hier](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA is een populair, breed ondersteund protocol, maar het staat je alleen toe muziek af te spelen of te downloaden — je kunt geen bestanden uploaden of nieuwe mappen aanmaken op een DLNA-server.

## Verbinden met een NAS of Server via FTP, FTPS of SFTP

Flacbox ondersteunt ook de klassieke bestandsoverdrachtsprotocollen. Om een server via FTP of FTPS te verbinden, tik op **Verbinden met cloudopslag → FTP**, voer de host-URL in de vorm `ftp://server-name` in (of `ftps://server-name` voor een versleutelde verbinding), geef je gebruikersnaam en wachtwoord op en tik op **Voltooid**. Kies voor **SFTP** (SSH-bestandsoverdrachtsprotocol) **SFTP** in plaats daarvan en geef een wachtwoord of SSH-sleutelpaar op.

## Verbinden met een NFS-share

Flacbox bevat **NFS**-ondersteuning (Network File System) — handig voor Linux-hosts, BSD-servers en NAS-apparaten. Kies **NFS** in het menu **Verbinden met cloudopslag**, voer het serveradres en het geëxporteerde pad in, en tik op **Voltooid**.

## Verbinden met een Plex Media Server

Flacbox kan direct verbinden met een Plex Media Server en je muziekbibliotheek bladeren op Artiesten, Albums, Genres en Afspeellijsten. Tik op **Verbinden met cloudopslag → Plex**, log in met je Plex-account, kies een server en de bibliotheek verschijnt naast je cloudservices. Plex-servers op hetzelfde lokale netwerk worden ook automatisch ontdekt in de sectie **Beschikbare apparaten**.

## Verbinden met een Jellyfin- of Emby-server

Zowel **Jellyfin** (open-source) als **Emby** (commercieel) werken native in Flacbox. Tik op **Verbinden met cloudopslag → Jellyfin** of **Emby**, voer je server-URL in (zoals `http://server-ip:8096`) en je inloggegevens, en je muziekbibliotheek is klaar om te streamen.

## Verbinden met een Subsonic- of Navidrome-server

Flacbox ondersteunt de Subsonic API, wat betekent dat het werkt met **Subsonic** zelf, **Navidrome** en elke andere Subsonic-compatibele server — inclusief Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Tik op **Verbinden met cloudopslag → Subsonic**, voer de server-URL en inloggegevens in, en de bibliotheek verschijnt in het Verbindingen-scherm.

## Verbinden met S3-compatibele Objectopslag

Voor zelf-hosters die cloudopslag gebruiken, bevat Flacbox een S3-compatibele connector. Tik op **Verbinden met cloudopslag → S3-opslag**, voer dan de eindpunt-URL, regio, toegangssleutel, geheime sleutel en bucketnaam in.

## Beschikbare Apparaten

Deze sectie toont elk apparaat op je lokale netwerk waarmee je vanuit Flacbox verbinding kunt maken via Bonjour-ontdekking. Volg deze stappen om een verbinding te maken:

- Open de app en ga naar de sectie **Beschikbare apparaten** onder Verbindingen.
- Tik op het apparaat waarmee je verbinding wilt maken.
- Voer indien nodig je inloggegevens in om de verbinding te voltooien.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Beschikbare Apparaten op het Lokale Netwerk" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive is een handige technologie waarmee je bestanden draadloos kunt overzetten van je computer naar je iOS-apparaat via elke desktopbrowser. Zorg ervoor dat je apparaat en computer verbonden zijn met hetzelfde Wi-Fi-netwerk.

### Wi-Fi Drive Inschakelen

- Open de applicatie en ga naar het tabblad **Verbindingen**.
- Selecteer **Verbinden via Wi-Fi** om toegang te krijgen tot het Wi-Fi Drive-hoofdscherm.
- (Optioneel) Stel een gebruikersnaam en wachtwoord in voor de ingebedde webserver om de toegang te beschermen.
- Tik op **Wi-Fi Drive starten** om Wi-Fi Drive in te schakelen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Drive Openen op je Computer

- Open op je computer een webbrowser (zoals Chrome, Firefox of Safari).
- Voer in de adresbalk van de browser de URL in die de applicatie heeft opgegeven.

### Bestanden Draadloos Overzetten

Zodra de webpagina voor je iOS-apparaat in de browser wordt geopend, kun je eenvoudig bestanden van je computer naar de webpagina slepen en neerzetten. De bestanden die je neerzet beginnen over te worden gezet naar je iOS-apparaat en zijn toegankelijk in Flacbox.

Je kunt Wi-Fi Drive ook direct koppelen in Finder op macOS (Ga → Maak verbinding met server…) of Verkenner op Windows (Netwerkstation koppelen…) en je iPhone of iPad behandelen als een gewoon netwerkstation.

Gedetailleerde instructies over het draadloos overzetten van bestanden via Wi-Fi Drive zijn beschikbaar [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder Bestandsdeling

iTunes Bestandsdeling (nu Finder Bestandsdeling op macOS Catalina en later) is een andere manier om bestanden over te zetten van een computer naar een apparaat via een Lightning- of USB-C-kabel.

- Verbind het apparaat met de computer via een kabel en start **Finder** op Mac (of **iTunes** op Windows).
- Open **Locaties → Verbonden apparaat → Bestanden** en zoek de Flacbox-app.
- Tik op het app-pictogram om alle gedeelde mappen te zien.
- Kopieer bestanden van de computer naar de gedeelde map op het apparaat via slepen-en-neerzetten.

Gedetailleerde instructies over het gebruik van Finder Bestandsdeling zijn beschikbaar [hier](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Een USB-flashdrive Verbinden

Als je een SD-kaart of USB-schijf hebt, kun je deze verbinden via een Lightning-naar-USB / SD-kaartlezer of een USB-C-schijf (op iPad en iPhone 15 / 16 / 17 / Pro). De app ondersteunt Apple-gecertificeerde kaartlezers en iXpand-flashdrives. Steek bij een iXpand-flashdrive hem in de Lightning-poort en open de applicatie — je ziet een bericht Extern apparaat verbonden en de apparaatinformatie. Tik op het flashdrive-pictogram om toegang te krijgen tot de muziekmap en tik op een audiobestand om te beginnen met afspelen.

Gedetailleerde instructies over het verbinden van een USB-flashdrive met je iPhone zijn beschikbaar [hier](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Bestandsbeheerder

Nadat je een cloudopslagservice hebt verbonden, tik op het pictogram om alle beschikbare bestanden en mappen te bekijken. Je kunt de ingebouwde bestandsbeheerder gebruiken om met deze bestanden te werken — downloaden, hernoemen, verplaatsen, uploaden, verwijderen en meer. Wanneer je een download start, verschijnt het bestand in de overdrachtwachtrij. Om de overdrachtwachtrij te openen, ga naar het tabblad Lokale bestanden en tik op het roterende pijlen-pictogram in de linkerbovenhoek. Alle gedownloade bestanden en mappen zijn beschikbaar in de sectie Lokale bestanden.

## Bovenste Werkbalk

De bovenste werkbalk, handig geplaatst onder de navigatiebalk, biedt verschillende handige acties voor eenvoudige toegang. Je kunt hem tonen of verbergen met een eenvoudige swipe-down-beweging.

- **Zoeken** — voer een snelle zoekopdracht uit in de huidige map.
- **Afspelen Hervatten** — als ingeschakeld in de applicatie-instellingen, herstelt dit de audiospelerwachtrij en de laatste mediapositie voor de huidige map.
- **Alles Afspelen** — scant de huidige map en submappen, voegt dan alle gevonden audiobestanden toe aan een nieuwe spelerwachtrij.
- **Alles Shufflen** — net als Alles afspelen, maar shufflet de bestanden voordat ze aan de audiospelerwachtrij worden toegevoegd.

## Mapopties

Wanneer je een map opent, vind je een handige set acties door op de **"..."**-knop in de rechterbovenhoek te tikken.

- **Selecteren** — activeer de bestandsselectiemodus.
- **Nieuwe map** — maak een nieuwe map aan in de huidige map.
- **Offline-modus inschakelen** — schakel de offlinemodus in voor de huidige map.
- **Bestanden uploaden** — upload bestanden van je apparaat naar de online map.
- **Zoeken** — zoek naar specifieke bestanden in de huidige map.
- **Sorteren** — sorteer bestanden op naam, grootte, wijzigingsdatum of op metadata.
- **Raster / lijstweergave** — schakel tussen tabelweergave en miniatuurweergave.

## Online Bestanden Bewerken

Wanneer je meerdere bestanden in je cloudopslag moet beheren, gebruik **Selectiemodus** om je acties te stroomlijnen:

- **Selectiemodus Activeren** — tik op de **"..."**-knop in de rechterbovenhoek en kies **Selecteren**.
- **Bestanden Kiezen** — selectievakjes verschijnen naast elk bestand en elke map.
- **Acties Uitvoeren** — zodra je de bestanden of mappen hebt geselecteerd, heb je toegang tot Volgende afspelen, Later afspelen, Toevoegen aan muziekbibliotheek, Toevoegen aan afspeellijst, Kopiëren, Uploaden, Verplaatsen, Hernoemen en Verwijderen.

## Bestandsacties

Tik op het **"..."**-pictogram naast de bestandstitel om het actiemenu te openen:

- **Volgende afspelen** — voeg het bestand in aan de bovenkant van de spelerwachtrij.
- **Later afspelen** — voeg het bestand toe aan de onderkant van de spelerwachtrij.
- **Toevoegen aan muziekbibliotheek** — voeg het bestand toe aan je muziekbibliotheek.
- **Toevoegen aan afspeellijst** — voeg het bestand toe aan een bestaande afspeellijst of maak een nieuwe aan.
- **Audio-tags bewerken** — open de ingebouwde tageditor om metadata te wijzigen.
- **Toevoegen aan favorieten** — voeg het bestand toe aan je favorietenlijst voor snelle toegang.
- **Downloaden** — download het bestand of de map naar je apparaat voor offline gebruik.
- **Hernoemen** — hernoem het bestand direct op de externe opslag.
- **Verplaatsen** — verplaats het bestand naar een andere map in je cloudopslag.
- **Openen in** — exporteer het bestand naar een andere compatibele app.
- **Verwijderen** — verwijder het bestand permanent uit je cloudopslag. **Deze actie kan niet ongedaan worden gemaakt.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Meer Acties voor een Bestand in Verbonden Cloudopslag" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

## Mapacties

Voor elke map in je cloudopslag zijn een breed scala aan acties beschikbaar door op het **"..."**-pictogram naast de maptitel te tikken.

- **Alles afspelen** — vervang de huidige spelerwachtrij door elk item in de geselecteerde map.
- **Volgende afspelen** — voeg de hele map toe aan de bovenkant van de spelerwachtrij.
- **Later afspelen** — voeg de mapinhoud toe aan de onderkant van de spelerwachtrij.
- **Toevoegen aan muziekbibliotheek** — voeg de inhoud van de map toe aan je muziekbibliotheek.
- **Toevoegen aan afspeellijst** — voeg de hele map toe aan een afspeellijst.
- **Toevoegen aan favorieten** — voeg de map toe aan je favorieten voor snelle toegang.
- **Offline-modus inschakelen** — behalve een eenvoudige download, monitort dit continu de map op nieuwe bestanden en downloadt ze automatisch wanneer ze online verschijnen.
- **Downloaden** — download alle inhoud van de map naar je apparaat voor offline toegang.
- **Hernoemen** — hernoem de map direct op de externe opslag.
- **Verplaatsen** — verplaats de map naar een andere locatie in je cloudopslag.
- **Archiveren (ZIP)** — bundel de mapinhoud in een enkel ZIP-bestand (Premium-functie).
- **Verwijderen** — verwijder de map en de inhoud permanent uit je cloudopslag. **Deze actie kan niet ongedaan worden gemaakt.**

## Snelle Toegang

De sectie Snelle toegang bevindt zich bovenaan het scherm. Het geeft je snelle toegang tot je favoriete en recent geopende bestanden van verbonden cloudservices.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Online Links en Snelle Toegang" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Overige Services

Deze sectie toont extra functies die je ervaring verbeteren. Momenteel ondersteunt de app **Last.fm**-scrobbling — wanneer verbonden worden je afspeelstatistieken automatisch naar je Last.fm-account gestuurd. Gedetailleerde installatie-instructies zijn beschikbaar [hier](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm Verbinding" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
