---
title: "Bestanden"
date: 2020-02-01
lastmod: 2026-06-01
description: "Leer hoe je het tabblad Bestanden gebruikt in Evervideo op iPhone, iPad en Mac. Verbind clouddiensten, NAS-apparaten, mediaservers en RTSP-streams op één plek. Beheer offlinevideo's, de overdrachtsrij, downloads, Wi-Fi Drive, iTunes / Finder Bestandsdeling en USB-schijven. Inclusief iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA en S3-compatibele opslag."
keywords: [
  "Evervideo bestanden", "Evervideo verbindingen", "Evervideo lokale bestanden",
  "cloud video instellen iPhone", "Google Drive video verbinden", "SMB videostreaming",
  "WebDAV videospeler iOS", "DLNA video iPhone", "NAS videostreaming",
  "Wi-Fi Drive videooverdracht", "Evervideo iTunes bestandsdeling", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo offline modus video", "Evervideo overdrachtsrij",
  "Evervideo bestandsbeheer", "Evervideo Documenten map",
  "videospeler Synology", "videospeler QNAP",
  "videospeler Apple Time Capsule", "USB DAC video",
  "iXpand videospeler", "S3 videospeler"
]
tags: ["handleiding", "evervideo", "bestanden", "verbindingen", "cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Het tabblad Bestanden is de alles-in-één bestandsbeheerder van Evervideo. In tegenstelling tot de meeste videoapps die cloudopslag en lokale bestanden in aparte tabbladen plaatsen, voegt Evervideo beide samen in één scrollbaar scherm zodat u van een Plex-server naar een cloudmap naar de Documenten-map van uw iPhone kunt gaan zonder tussen tabbladen te wisselen.

Het tabblad Bestanden is opgedeeld in duidelijke secties die in deze volgorde op uw scherm verschijnen:

- **Snelle toegang** — recente items en favorieten voor bestanden en mappen die u het meest recentelijk hebt geopend.
- **Bestanden in deze applicatie** — wat zich bevindt in de sandbox-Documenten-map van Evervideo.
- **Bestanden op deze iPhone / iPad / Mac** — video's elders op uw apparaat, beschikbaar via de systeembestandskiezer.
- **Cloudopslag** — elk cloudaccount, NAS en mediaserver die u hebt verbonden.
- **Beschikbare apparaten** — via Bonjour / mDNS automatisch ontdekte servers en schijven op uw lokale netwerk.

In de rechterbovenhoek van het scherm Bestanden is een knop Overdrachten (een pictogram met draaiende pijlen). Tik erop om de Overdrachtsrij te openen waar u elke download en upload via al uw bronnen bijhoudt.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Bestanden Across Verbonden Opslagplaatsen" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Verbinding maken met cloudopslag

De sectie Cloudopslag van het tabblad Bestanden is waar elk verbonden account, NAS, mediaserver en stream zich bevindt — naast elkaar, in één scrollbare lijst.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Cloudopslag Sectie in het tabblad Bestanden" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Open het tabblad **Bestanden**.
- Scroll naar de sectie **Cloudopslag**.
- Tik op **Verbinden met cloudopslag** in het menu.
- Kies een cloudopslagdienst uit de lijst.
- Voer uw inloggegevens in op de officiële autorisatiepagina van de cloudprovider en tik op **Voltooid**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Verbinding maken met een cloudopslagdienst" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Als u problemen ondervindt, controleer dan uw internetverbinding en uw gebruikersnaam / wachtwoord. In de Premium-versie van de app kunt u een onbeperkt aantal diensten toevoegen; de gratis versie ondersteunt maximaal drie.

## Ondersteunde cloudopslagdiensten, mediaservers en protocollen

Evervideo ondersteunt een uitzonderlijk breed scala aan bronnen voor uw video's. Alles hieronder werkt vanuit één Verbinding maken met cloudopslag-stroom.

**Persoonlijke cloudopslag:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Zelfgehoste mediaservers:** Plex · Jellyfin · Emby · Subsonic (en elke Subsonic-compatibele server — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (en ownCloud via de gedeelde API) · Synology Drive · QNAP.

**NAS- en bestandsdelingsprotocollen:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH-bestandsoverdrachtprotocol, wachtwoord of publieke-sleutelverificatie) · NFS · DLNA / UPnP (afspelen en downloaden).

**Live- en IP-camerastreams:** RTSP — wijs Evervideo naar een willekeurige `rtsp://`-URL en het speelt meteen af. Ideaal voor beveiligingscamera's, IPTV-streams, deurbelvideo's, babyfoons en vergelijkbare live bronnen.

**S3-compatibele objectopslag:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces en elk ander S3-API-eindpunt.

**Apparaatbibliotheken:** de Foto's-bibliotheek (alle video's, schermopnamen, fotoalbums) en de Muziek-appbibliotheek (Albums, Genres, Afspeellijsten) — beide worden weergegeven in de Mediabibliotheek zodat u niets hoeft te kopiëren.

**Lokaal netwerk ontdekken:** de sectie Beschikbare apparaten somt automatisch elke Bonjour / mDNS-dienst op uw Wi-Fi-netwerk op — Plex, Jellyfin, Emby, Synology, QNAP, AirPort-routers met aangesloten schijven, Apple Time Capsule — zodat u op één tik verbinding kunt maken zonder een IP-adres in te typen.

Elke verbinding gebruikt de officiële SDK of het open protocol van de dienst, met OAuth-gebaseerde autorisatie waar ondersteund. U kunt meerdere accounts van dezelfde dienst verbinden (bijvoorbeeld twee Google Drive-accounts, of zowel een Plex- als een Jellyfin-server) en ze naast elkaar bekijken in de sectie Cloudopslag.

## Beveiliging en privacy

Evervideo gebruikt alleen officiële SDK's en beveiligde verbindingen om te communiceren met verbonden clouddiensten. Uw gebruikersnaam en wachtwoord zijn niet toegankelijk voor de applicatie — alle overdrachten zijn TLS-versleuteld.

Wanneer u uw gebruikersnaam en wachtwoord invoert, toont de applicatie u de officiële autorisatiepagina van de cloudserviceprovider, en het volledige autorisatieproces vindt buiten de applicatie plaats. De cloudserviceprovider stuurt vervolgens een auth-token naar de applicatie na succesvolle autorisatie, en dat token wordt gebruikt voor API-aanroepen.

Een auth-token is een digitale sleutel waarmee toepassingen van derden namens u met cloudopslag kunnen communiceren. Het token wordt op uw apparaat opgeslagen in de beveiligde systeemopslag van Apple (Keychain), die versleuteld is in rust en beschermd door uw apparaatcode of biometrische vergrendeling. U kunt bestanden van verbonden clouddiensten naar uw apparaat downloaden; die bestanden worden geplaatst in de map Documenten van de app en kunnen op elk moment worden verwijderd via de ingebouwde bestandsbeheerder.

De applicatie deelt geen informatie van uw verbonden cloudaccounts met Everappz, adverteerders of derden. U kunt de toegang tot uw cloudaccount op elk moment intrekken door de accountinstellingspagina in uw webbrowser te openen.

## Auth-token weigeren

Om een auth-token in te trekken, logt u in op uw cloudaccount in een webbrowser en navigeert u naar de beveiligings- of verbonden-apps-pagina. Daar kunt u elke app van derden vinden die is verbonden met uw cloudaccount en verwijderen. Gedetailleerde instructies voor Google-accounts zijn [hier](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) beschikbaar.

U kunt het cloudaccount ook loskoppelen binnen de applicatie zelf — wanneer u dat doet, wordt het auth-token onmiddellijk van uw apparaat verwijderd. Als u de applicatie van uw apparaat verwijdert, worden alle gedownloade gegevens en toegangstokens automatisch meegenomen.

## Een cloudopslag loskoppelen of configuratie wijzigen

- **Toegang tot cloudopslagopties** — zoek de verbonden dienst in de sectie **Cloudopslag** van het tabblad Bestanden.
- **Tik op de knop "..."** naast de servicetitel om extra opties te openen:
  - **Hernoemen** — wijzig de naam van de clouddienst zoals die in uw lijst verschijnt.
  - **Instellingen** — wijzig de configuratie of verificatiegegevens. Soms moet u de verbonden clouddienst opnieuw autoriseren als het autorisatietoken is verlopen.
  - **Ontkoppelen** — verbreek de verbinding tussen de app en de clouddienst volledig. Dit verwijdert alle video's die aan die dienst zijn gekoppeld uit uw mediabibliotheek, maar laat ze ongewijzigd op de server.

## Verbinding maken met een computer of NAS

U kunt uw computer, persoonlijke NAS of ander netwerkapparaat verbinden via het SMB-, WebDAV-, FTP / FTPS-, SFTP-, NFS- of DLNA-protocol. Dit is de eenvoudigste manier om een bestaande thuis-mediabibliotheek — of die nu op een Mac, Windows-pc, Synology, QNAP, Apple Time Capsule of WD My Cloud Home staat — in Evervideo te brengen zonder iets te kopiëren.

### Verbinding maken met een computer via SMB

- Tik op **Verbinden met cloudopslag → SMB**.
- Voer het IP-adres van de computer en de gedeelde mapnaam in met het formaat `smb://computer-ip-address/shared-folder-name`.
- Kies de protocolversie: **Auto**, **SMB1** of **SMB2**.
- Voer uw gebruikersnaam en wachtwoord in (indien vereist).
- Tik op **Voltooid**.

Als de verbinding succesvol is, verschijnt de share in de sectie Cloudopslag. Een volledige handleiding over hoe u uw Mac of pc verbindt via SMB is [hier](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) beschikbaar.

### Verbinding maken met een NAS via WebDAV

Alle stappen zijn hetzelfde als bij SMB, behalve het URL-veld. Gebruik `http://server-name` of `https://server-name` als de server SSL ondersteunt. WebDAV werkt met Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home en elke andere server met een WebDAV-eindpunt.

Een volledige handleiding over WebDAV is [hier](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) beschikbaar.

### Verbinding via DLNA / UPnP

Deel een mediabibliotheek op uw Windows-pc of NAS via het DLNA / UPnP-protocol en open het in Evervideo zoals beschreven [hier](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA wordt breed ondersteund, maar hiermee kunt u alleen video's afspelen of downloaden — u kunt geen bestanden uploaden of nieuwe mappen maken op een DLNA-server.

### Verbinding via FTP, FTPS of SFTP

Evervideo ondersteunt ook de klassieke bestandsoverdrachtsprotocollen. Om een server via FTP of FTPS te verbinden, tikt u op Verbinding maken met cloudopslag → FTP, voert u de host-URL in als `ftp://server-name` (of `ftps://server-name` voor een versleutelde verbinding), geeft u uw gebruikersnaam en wachtwoord op en tikt u vervolgens op Voltooid. Voor SFTP (SSH-bestandsoverdrachtprotocol) kiest u SFTP en geeft u een wachtwoord of SSH-sleutelpaar op.

### Verbinding met een NFS-share

Evervideo bevat NFS-ondersteuning (Network File System) — handig voor Linux-hosts, BSD-servers en NAS-apparaten die liever videobibliotheken via NFS dan via SMB beschikbaar stellen. Kies NFS in het menu Verbinding maken met cloudopslag, voer het serveradres en het geëxporteerde pad in en tik op Voltooid.

## Een Plex Media Server verbinden

Evervideo kan rechtstreeks verbinding maken met een Plex Media Server en door uw Movies-, TV Shows- en Home Videos-bibliotheken bladeren. Tik op Verbinding maken met cloudopslag → Plex, meld u aan met uw Plex-account, kies een server en de bibliotheek verschijnt naast uw clouddiensten. Plex-servers op hetzelfde lokale netwerk worden ook automatisch ontdekt in de sectie Beschikbare apparaten.

## Een Jellyfin- of Emby-server verbinden

Zowel Jellyfin (open-source) als Emby (commercieel) mediaservers werken native in Evervideo. Tik op Verbinding maken met cloudopslag → Jellyfin of Emby, voer uw server-URL in (doorgaans iets als `http://server-ip:8096`) en uw inloggegevens en uw bibliotheek is klaar om te streamen.

## Een Subsonic- of Navidrome-server verbinden

Evervideo spreekt de Subsonic API, wat betekent dat het werkt met Subsonic zelf, Navidrome en elke andere Subsonic-compatibele server — inclusief Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) en Ampache. Tik op Verbinding maken met cloudopslag → Subsonic, voer de server-URL en inloggegevens in en de bibliotheek verschijnt in de sectie Cloudopslag.

## Een RTSP-stream verbinden (IP-camera's, live tv, IPTV)

Evervideo heeft native RTSP-ondersteuning, zodat u het kunt wijzen naar elke RTSP-bron — beveiligingscamera's, deurbelvideo's, IPTV-providers, babyfoons, uitzendfeeds — en Evervideo zal de stream live ophalen en decoderen. Tik op Online links → Link toevoegen, plak de volledige URL (`rtsp://camera-ip:port/stream-path`), geef gebruikersnaam en wachtwoord op indien vereist en tik op Voltooid.

## Verbinding maken met S3-compatibele objectopslag

Voor zelfhosters en gevorderde gebruikers die cloud-objectopslag gebruiken, bevat Evervideo een S3-compatibele connector. Tik op Verbinding maken met cloudopslag → S3-opslag en voer de eindpunt-URL, regio, toegangssleutel, geheime sleutel en bucketnaam in. Dit werkt met AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces en elk ander S3-API-eindpunt.

## Beschikbare apparaten

Deze sectie toont elk apparaat op uw lokale netwerk waarmee u verbinding kunt maken vanuit Evervideo via Bonjour / mDNS-ontdekking — Plex, Jellyfin, Emby, Synology, QNAP, AirPort-routers met aangesloten schijven, Apple Time Capsule enzovoort. Om een verbinding tot stand te brengen:

- Scroll naar de sectie Beschikbare apparaten in het tabblad Bestanden.
- Tik op het apparaat waarmee u verbinding wilt maken.
- Voer indien nodig uw aanmeldingsgegevens in om de verbinding te voltooien.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Beschikbare apparaten op het lokale netwerk" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Met Wi-Fi Drive kunt u bestanden draadloos van uw computer naar uw iOS-apparaat overdragen via elke desktopbrowser, Finder of File Explorer. Uw apparaat en computer moeten op hetzelfde Wi-Fi-netwerk zijn.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Drive inschakelen

- Scroll in het tabblad Bestanden naar Cloudopslag → Verbinden via Wi-Fi om het hoofdscherm van Wi-Fi Drive te openen.
- (Optioneel) Stel een gebruikersnaam en wachtwoord in voor de ingebouwde webserver.
- Tik op Wi-Fi Drive starten.

### Wi-Fi Drive openen op uw computer

- Open een webbrowser op uw computer (Chrome, Firefox, Safari, enz.).
- Voer de URL in die door de applicatie wordt getoond.
- Sleep bestanden van uw computer naar de webpagina — ze beginnen over te dragen naar uw iOS-apparaat.

U kunt Wi-Fi Drive ook rechtstreeks koppelen in **Finder** op macOS (Ga → Verbinding maken met server…) of File Explorer op Windows (Netwerkstation koppelen…) en uw iPhone of iPad behandelen als een gewone netwerkschijf.

Gedetailleerde instructies zijn [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) beschikbaar.

## iTunes / Finder Bestandsdeling

iTunes-bestandsdeling (nu Finder-bestandsdeling op macOS Catalina en hoger) laat u bestanden overdragen via een Lightning- of USB-C-kabel. Sluit het apparaat aan, open Finder op Mac (of iTunes op Windows), zoek Evervideo in de applijst en kopieer bestanden naar de gedeelde map.

## Een USB-flashdrive of SD-kaart verbinden

Sluit een USB-schijf of SD-kaart aan op uw iPhone, iPad of Mac via de Lightning-naar-USB / USB-C-adapter of kaartlezer. Open Bestanden → Bestanden op deze iPhone → Map openen, navigeer naar de schijf en selecteer een videobestand of -map. Evervideo speelt bestanden direct van de schijf af zonder ze naar de interne opslag te kopiëren — handig voor zeer grote 4K-bibliotheken.

## Mappen bekijken in verbonden opslag

Tik op een verbonden clouddienst om de bestandsbrowser te openen. Mappen tonen videominiaturen wanneer beschikbaar en het tikken op een video start het afspelen onmiddellijk terwijl het de rest van het bestand op de achtergrond blijft streamen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Mappen bekijken in verbonden opslag" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Snelle toegang

De sectie Snelle toegang bevindt zich bovenaan het tabblad Bestanden. Het geeft u snelle toegang tot uw favoriete en onlangs geopende bestanden en mappen — zowel van clouddiensten als van apparaatopslag. Wanneer u een bestand of map van de cloud opent, wordt het toegevoegd aan de lijst Onlangs geopend. U kunt diep geneste mappen als Favorieten markeren om ze snel te openen zonder door de mapstructuur te graven.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Online links en snelle toegang" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Bestanden in deze applicatie

Deze sectie toont bestanden en mappen die zijn opgeslagen in de sandbox-Documenten-map van Evervideo — alles wat u van de cloud hebt gedownload, via Wi-Fi Drive hebt overgedragen, via Finder-bestandsdeling hebt gekopieerd of vanuit een andere app hebt geïmporteerd.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Bestanden in deze applicatie" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Map Documenten

De map Documenten is de root van alles in Bestanden in deze applicatie. U kunt submappen maken, bestanden hernoemen, verplaatsen en ze naar wens groeperen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Lokale bestanden — Map Documenten" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Bestanden op deze iPhone / iPad / Mac

Deze sectie toont video's die zich op uw apparaat maar in andere applicaties bevinden. U kunt ze importeren in Evervideo via de systeembestandskiezer:

- Tik op Bestanden openen… om specifieke bestanden te selecteren.
- Tik op Map openen… om een hele map te selecteren.

U kunt ook Map verbinden gebruiken om een koppeling te maken naar een map op uw apparaat met lees- / schrijftoegang — perfect voor werken met een map op iCloud Drive of een aangesloten USB-schijf zonder iets te kopiëren.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Bestanden op dit apparaat" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Speciale mappen

In het tabblad Bestanden ziet u verschillende speciale mappen die Evervideo automatisch aanmaakt en gebruikt:

- **Downloads** — elk bestand dat van de cloud is gedownload, verschijnt hier standaard. Aanpasbaar via Instellingen → Bestandsbeheer → Gedownloade bestanden opslaan in.
- **Spelercache** — de cache van de mediaspeler. Standaard downloadt de speler aanstaande video's voor soepel afspelen. U kunt de cache uitschakelen in de appinstellingen of gewoon deze map verwijderen.
- **iCloud** — bestanden in deze map worden gesynchroniseerd op alle apparaten die zijn verbonden met hetzelfde iCloud-account.
- **Offline mappen** — wanneer u een map, afspeellijst, album of genre markeert als offline beschikbaar, worden de bestanden in deze map gedownload.

## Bovenwerkbalk

De bovenwerkbalk, onder de navigatiebalk, biedt verschillende acties die u kunt tonen of verbergen met een veegbeweging naar beneden:

- **Zoeken** — een zoekopdracht uitvoeren binnen de huidige map of sectie.
- **Verder afspelen** — als ingeschakeld in de instellingen, herstel de spelerswachtrij en laatste videopositie voor de huidige map.
- **Alles afspelen** — scan de huidige map en submappen en voeg bestanden toe aan de spelerswachtrij.
- **Alles shufflen** — zoals Alles afspelen, maar schud eerst.

## Mapopties

Wanneer u een map opent, tik op de **"..."** knop in de rechterbovenhoek voor deze acties:

- **Selecteren** — activeer de bestandsselectiemodus.
- **Nieuwe map** — maak een nieuwe map aan in de huidige map.
- **Offline-modus inschakelen** — schakel offlineSync in voor de huidige map. Nieuwe bestanden die online worden toegevoegd, worden automatisch gedownload.
- **Bestanden uploaden** — upload bestanden van uw apparaat naar de online map.
- **Zoeken** — zoek binnen de map.
- **Sorteren** — sorteer bestanden op naam, grootte, datum gewijzigd of metadata.
- **Raster / lijstweergave** — schakel tussen tabelweergave en miniatuurweergave. Miniatuurweergave toont grote videoposterpreviews.

## Selectiemodus

Tik op **"..."** in de rechterbovenhoek en kies **Selecteren** om de selectiemodus te activeren. Er verschijnen selectievakjes naast elk bestand en elke map. Tik om een of meerdere items te selecteren en voer vervolgens batchacties uit: Volgende afspelen, Later afspelen, Toevoegen aan mediabibliotheek, Toevoegen aan afspeellijst, Kopiëren, Uploaden, Verplaatsen, Hernoemen of Verwijderen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Selectiemodus in de bestandsbeheerder" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Als u verbonden cloudopslag liever als alleen-lezen wilt behandelen (om onbedoeld verwijderen te voorkomen), schakel dan Instellingen → Bestandsbeheer → Online bestanden bewerken → Uit in om alle destructieve bewerkingen uit de UI te verbergen.

## Bestandsacties

Tik op het **"..."** pictogram naast de bestandstitel om het actiemenu te tonen:

- **Volgende afspelen** — voeg het bestand in aan het begin van de spelerswachtrij.
- **Later afspelen** — voeg het bestand toe aan het einde van de spelerswachtrij.
- **Toevoegen aan mediabibliotheek** — neem het bestand op in uw mediabibliotheek, georganiseerd per Album en Genre.
- **Toevoegen aan afspeellijst** — voeg het bestand toe aan een bestaande afspeellijst of maak een nieuwe aan.
- **Tags bewerken** — open de ingebouwde tagbewerker om metadata te wijzigen. Voor onlinebestanden wordt het bestand tijdelijk gedownload, bewerkt en na bevestiging opnieuw geüpload.
- **Toevoegen aan favorieten** — voeg het bestand toe aan uw favorietenlijst voor snelle toegang.
- **Downloaden** — download het bestand of de map naar uw apparaat voor offline gebruik.
- **Hernoemen** — hernoem het bestand rechtstreeks op de externe opslag.
- **Verplaatsen** — verplaats het bestand naar een andere map binnen uw cloudopslag.
- **Toevoegen aan archief** — bundel het bestand in een enkel ZIP-bestand (Premium-functie).
- **Openen in** — exporteer het bestand naar een andere compatibele app via het systeem Deelblad.
- **Verwijderen** — verwijder het bestand permanent. **Deze actie kan niet ongedaan worden gemaakt.**

## Mapacties

Voor elke map in uw cloudopslag zijn er veel acties beschikbaar door op het pictogram **"..."** naast de maptitel te tikken.

- **Alles afspelen** — vervang de huidige spelerswachtrij door alle video's in de map.
- **Volgende afspelen / Later afspelen** — voeg de hele map toe aan de wachtrij.
- **Toevoegen aan mediabibliotheek** — voeg de inhoud van de map toe aan uw mediabibliotheek.
- **Toevoegen aan afspeellijst** — voeg de hele map toe aan een afspeellijst.
- **Toevoegen aan favorieten** — voeg de map toe aan uw favorieten.
- **Offline-modus inschakelen** — meer dan een eenvoudige download, dit bewaakt de map continu op nieuwe bestanden en downloadt ze automatisch zodra ze online verschijnen.
- **Downloaden** — download alle inhoud van de map naar uw apparaat voor offline toegang.
- **Hernoemen / Verplaatsen** — hernoem of verplaats de map op externe opslag.
- **Toevoegen aan archief** — bundel de mapinhoud in een ZIP-bestand (Premium-functie).
- **Verwijderen** — verwijder de map en zijn inhoud permanent. **Deze actie kan niet ongedaan worden gemaakt.**

## Overdrachtsrij

In de rechterbovenhoek van het tabblad Bestanden is een knop **Overdrachten** (een pictogram met draaiende pijlen). Tik erop om de Overdrachtsrij te openen — een lijst van elke actieve download en upload via al uw bronnen, met realtime voortgang, snelheid en ETA per bestand.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Bestandsoverdrachtsrij" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

U kunt overdrachten pauzeren, hervatten, mislukte overdrachten opnieuw proberen, items herordenen om specifieke downloads te prioriteren of ze afzonderlijk annuleren. U kunt ook de overdrachtsrijsnelheid (maximale parallelle taken), het netwerktype (alleen Wi-Fi of Wi-Fi + mobiele data) en achtergrondoverdrachten aanpassen in Instellingen → Bestandsbeheer.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Acties op de bestandsoverdrachtsrij" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offline modus en gesynchroniseerde offline mappen

De offline modus is een handige functie waarmee u uw favoriete video's kunt bekijken zelfs wanneer u niet verbonden bent met internet. Wanneer u de offline modus inschakelt voor een map, afspeellijst, album of genre, worden alle bestanden in die verzameling automatisch naar uw apparaat gedownload voor offline afspelen. Ze verschijnen in de sectie Offline mappen.

Wanneer u nieuwe bestanden aan de externe server toevoegt, worden ze ook automatisch gedownload — zodat uw offline verzameling actueel blijft zonder dat u iets hoeft te doen. Om handmatig opnieuw te synchroniseren, tikt u op de drie puntjes in de rechterbovenhoek van een offline map en selecteert u Synchroniseren.

U kunt de synchronisatietimeout aanpassen in Instellingen → Bestandsbeheer → Gesynchroniseerde offline mappen → Tijdsinterval.

Gedetailleerde instructies zijn [hier](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/) beschikbaar.

## Personalisatie

In Instellingen → Personalisatie kunt u instellen hoe het tabblad Bestanden wordt gepresenteerd:

- **Stijl bestandsscherm** — Gewoon menu (toont de mappenlijst direct) of Gegroepeerd menu (groepeert inhoud per categorie — Snelle toegang, Speciale mappen, Cloudopslag, enz.).
