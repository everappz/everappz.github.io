---
title: "Verbindingen"
date: 2020-01-01
description: "Leer hoe u cloudservices, computers, NAS-apparaten verbindt en uw muziekbestanden beheert met Evermusic. Stapsgewijze handleiding voor Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes-bestandsdeling en meer."
keywords: [
  "Evermusic", "cloudmuziekspeler", "NAS-streaming", "Wi-Fi Drive", 
  "SMB", "WebDAV", "DLNA", "iTunes-bestandsdeling", 
  "cloudopslag verbinden", "muziekoverdracht iPhone", "bestandsbeheerder iOS"
]
tags: ["evermusic", "gids", "verbindingen"]
readingTime: 11
---


Op het scherm Verbindingen kunt u elke bron met uw muziek verbinden — populaire cloudservices, zelfgehoste mediaservers, uw Mac of pc, een persoonlijke NAS, Apple Time Capsule, WD My Cloud Home, zelfs een USB-flashdrive — en ze allemaal gebruiken vanuit één uniforme interface. Verbindingen is ook waar u Snelle toegang instelt tot diep geneste cloudmappen en waar u Last.fm authenticeert voor scrobbling.

Het scherm is verdeeld in duidelijk gelabelde secties die schaalbaar zijn van een enkel iCloud Drive-account tot een bibliotheek verspreid over meerdere clouds en NAS-apparaten: Snelle toegang bovenaan (uw favoriete cloudmappen), Cloudopslag (de toegevoegde accounts), Lokaal netwerk (via Bonjour ontdekte apparaten), Computer (Wi-Fi Drive, iTunes-bestandsdeling, SMB), Externe accessoires (verbonden USB-flashdrives) en Andere services (Last.fm en vergelijkbare).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Verbindingenscherm" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Verbinding maken met cloudopslag

- Open het tabblad Verbindingen.
- Selecteer Verbinding maken met cloudopslag in het menu.
- Kies een cloudopslagservice uit de lijst.
- Meld u aan op de officiële autorisatiepagina van de aanbieder (Evermusic ziet uw wachtwoord nooit).
- Tik op Selesai.

{{< cards cols="1">}}
  {{< card title="" subtitle="Kiezer voor cloudopslagaanbieder" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Als u problemen ondervindt, controleer dan uw internetverbinding en inloggegevens, en zorg ervoor dat tweefactorauthenticatie correct is geconfigureerd voor die service.  
In de Premium-versie van de app kunt u een onbeperkt aantal services toevoegen. Gratis gebruikers kunnen tegelijk slechts één cloudaccount verbinden.

## Ondersteunde cloudopslagservices

Evermusic ondersteunt de volledige reeks populaire cloud- en zelfgehoste services. Gratis gebruikers krijgen dezelfde aanbiederscatalogus maar met de één-account-limiet; Premium ontgrendelt onbeperkte accounts en verwijdert de meeste andere beperkingen.

- **Persoonlijke cloudaccounts:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Zelfgehoste servers en mediabibliotheken:** Plex · Jellyfin · Emby · Subsonic (en elke Subsonic-compatibele server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (en Owncloud, via de gedeelde API) · Synology Drive · QNAP.
- **NAS- en bestandsdelingsprotocollen:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (wachtwoord- of publieke-sleutelauthenticatie), NFS en DLNA (alleen-lezen — afspelen en downloaden).
- **S3-compatibele objectopslag:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage of elk S3-API-eindpunt.
- **Lokaal netwerk ontdekken:** het gedeelte Beschikbare apparaten vermeldt automatisch elk apparaat op uw Wi-Fi dat zichzelf via Bonjour / mDNS bekendmaakt — Plex, Jellyfin, Emby-servers, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, AirPort-routers met aangesloten schijven enzovoort.

## Beveiliging en privacy

We gebruiken alleen officiële SDK en beveiligde verbinding voor interactie met verbonden cloudservices. Uw gebruikersnaam en wachtwoord zijn niet beschikbaar voor de applicatie. Alle verzoeken van de applicatie naar de cloudservice zijn versleuteld.

Wanneer u uw gebruikersnaam en wachtwoord invoert, toont de applicatie u de officiële autorisatiepagina die door de cloudserviceprovider wordt aangeboden en vindt het gehele autorisatieproces buiten de applicatie plaats. De cloudserviceprovider stuurt een auth-token naar de applicatie na succesvolle autorisatie en dat token wordt gebruikt voor API-aanroepen.

Auth-token is een digitale sleutel waarmee apps van derden kunnen communiceren met cloudopslag. Auth-token wordt op uw apparaat opgeslagen in een beveiligde systeemopslag genaamd Keychain. U kunt uw bestanden van de verbonden cloudservice naar het apparaat downloaden en die bestanden worden geplaatst in de map "Documenten" van de app. U kunt die bestanden op elk moment verwijderen met de ingebouwde bestandsbeheerder.

De applicatie deelt geen informatie van het verbonden cloudaccount. U kunt de toegang tot uw cloudaccount op elk moment intrekken door de accountinstellingenpagina in uw webbrowser te openen.

## Auth-token intrekken

Log in op uw account in de webbrowser en navigeer naar de instellingenpagina. Daar kunt u alle apps van derden vinden die verbonden zijn met uw cloudaccount en ze verwijderen als u die applicatie niet meer wilt gebruiken. Gedetailleerde instructies zijn beschikbaar [hier](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

U kunt ook de verbonden cloudaccounts in de applicatie verbreken en het auth-token wordt dan ook van uw apparaat verwijderd. Als u de applicatie van uw apparaat verwijdert, worden ook alle gedownloade gegevens en toegangstokens verwijderd.

## Een cloudopslag verbreken of configuratie wijzigen

- Toegang tot cloudopslagopties: zoek eerst de cloudopslag die u wilt beheren in de interface van de app.
- Tik op de knop '...': naast de servicetitel ziet u een knop '...'. Tik erop om aanvullende opties te openen.
  - **Hernoemen**: als u de naam van de cloudservice wilt wijzigen zoals deze in uw lijst verschijnt, selecteer dan 'Hernoemen.'
  - **Instellingen**: om de configuratie of authenticatiegegevens voor de cloudservice te wijzigen, kiest u 'Instellingen.' Soms moet u de verbonden cloudservice opnieuw autoriseren als het autorisatietoken is verlopen.
  - **Ontkoppelen**: als u de verbinding tussen de app en de cloudservice volledig wilt verbreken, selecteer dan 'Ontkoppelen.' Houd er rekening mee dat alle nummers die aan deze cloudservice zijn gekoppeld uit de muziekbibliotheek van uw app worden verwijderd, maar ze blijven op de server aanwezig.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu met meer acties voor verbonden cloudopslag" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Verbinding maken met computer of NAS

U kunt ook uw computer, persoonlijke NAS of andere netwerkapparaten verbinden via SMB, DLNA of WebDAV-protocol.

## Verbinding maken met computer via SMB

- Tik op "Verbinding maken met cloudopslag" → SMB.
- Voer het IP-adres van de computer en de naam van de gedeelde map in het URL-veld in met het formaat smb://computer-ip-adres/gedeelde-mapnaam
- Kies protocolversie: Auto, SMB1, SMB2
- Voer gebruikersnaam en wachtwoord in (indien vereist)
- Tik op "Voltooid".

Als uw verbinding geslaagd is, ziet u verbonden opslag in het gedeelte "Cloudopslag."  
Een volledige tutorial over hoe u uw Mac of pc verbindt via SMB is beschikbaar [hier](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB-verbindingsinstellingen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Verbinding maken met NAS via WebDAV

Alle stappen zijn hetzelfde, behalve het URL-veld.  
De URL moet de notatie http://servernaam hebben, of https://servernaam als de server SSL ondersteunt.
Een volledige tutorial over hoe u NAS verbindt via WebDAV-protocol is beschikbaar [hier](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV-verbindingsinstellingen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Verbinding maken met computer of NAS via DLNA

U kunt ook een muziekbibliotheek op uw Windows-pc of persoonlijke NAS delen via het DLNA-protocol en die bibliotheek in de app openen zoals beschreven [hier](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA is een populair en veel gebruikt protocol, maar u kunt er alleen muziek mee afspelen of downloaden. U kunt geen bestanden uploaden of nieuwe mappen op de server aanmaken.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA-verbindingsinstellingen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Beschikbare apparaten

Dit gedeelte toont alle apparaten in uw lokale netwerk waarmee u verbinding kunt maken via de applicatie.  
Volg deze stappen om verbinding te maken met een apparaat:

- Open de app en ga naar het gedeelte "Beschikbare apparaten".
- Tik op het apparaat waarmee u verbinding wilt maken vanuit de lijst.
- Voer indien nodig uw inloggegevens in om de verbinding te voltooien.

{{< cards cols="1">}}
  {{< card title="" subtitle="Beschikbare apparaten in het lokale netwerk" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive 

Wi-Fi Drive is een handige technologie waarmee u bestanden draadloos van uw computer naar uw iOS-apparaat kunt overbrengen via een desktopbrowser.  
Om deze functie effectief te gebruiken, zorg ervoor dat uw apparaat en computer verbonden zijn met hetzelfde Wi-Fi-netwerk.   
Hier is een stapsgewijze handleiding voor het gebruik van Wi-Fi Drive.

## Wi-Fi Drive inschakelen

- Open de applicatie en ga naar het tabblad "Verbindingen".
- Selecteer "Verbinding maken via Wi-Fi" om het hoofdscherm van Wi-Fi Drive te openen.
- Tik op "Wi-Fi Drive starten" om Wi-Fi Drive in te schakelen.

## Wi-Fi Drive openen op uw computer

- Open op uw computer (desktop of laptop) een webbrowser (zoals Chrome, Firefox of Safari).
- Voer in de adresbalk van de browser de URL in die door de applicatie is opgegeven.

## Bestanden draadloos overdragen

Zodra de webpagina van uw iOS-apparaat in de browser is geopend, kunt u eenvoudig bestanden van uw computer naar de webpagina slepen en neerzetten.  
De bestanden die u sleept en neerzet, worden overgebracht naar uw iOS-apparaat en zijn toegankelijk binnen de applicatie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive-serverinstellingen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Gedetailleerde instructies over hoe u bestanden draadloos overdraagt via Wi-Fi Drive zijn beschikbaar [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes-bestandsdeling

iTunes-bestandsdeling is een andere technologie waarmee u bestanden van uw computer naar uw apparaat kunt overbrengen via de Finder-app op uw Mac en een lightning-kabel.   
- Sluit een apparaat aan op de computer met een kabel en start de Finder-app op uw Mac. 
- Open "Locaties" → "Uw verbonden apparaat" → "Bestanden" → en zoek de Evermusic-app. 
- Tik op het app-pictogram om alle gedeelde mappen te zien. 
- Kopieer bestanden van de computer naar de gedeelde map op het apparaat via slepen en neerzetten.   

Gedetailleerde instructies over hoe u iTunes-bestandsdeling gebruikt zijn beschikbaar [hier](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder-bestandsdeling op Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Een USB-flashkaart verbinden

Als u een SD-kaart heeft, kunt u die verbinden via een lightning-kaartlezer. De app ondersteunt momenteel Apple Certified-kaartlezers en iXpand-flashdrives. Als u een iXpand-flashdrive heeft, steek die dan in de lightning-poort en open de applicatie. U ziet een bericht 'Extern apparaat verbonden' en apparaatinformatie. Tik gewoon op het flashdrive-pictogram om de muziekmap te openen en tik op een audiobestand om te beginnen met afspelen. We hebben gedetailleerde instructies over hoe u een USB-flashkaart verbindt met de iPhone en naar muziek luistert of bestanden beheert die beschikbaar zijn [hier](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Bestandsbeheerder

Zodra u een cloudopslagservice heeft verbonden, tikt u op het pictogram om alle beschikbare bestanden en mappen te bekijken. U kunt de ingebouwde bestandsbeheerder gebruiken om met deze bestanden te werken — downloaden, hernoemen, verplaatsen en meer. Wanneer u een download start, verschijnt het bestand in de overdrachtsrij. Om de overdrachtsrij te bekijken, gaat u naar het tabblad "Lokale bestanden" en tikt u op de draaiende pijlen in de linkerbovenhoek. Alle gedownloade bestanden en mappen zijn beschikbaar in het gedeelte "Lokale bestanden".

## Bovenste werkbalk

De bovenste werkbalk, handig onder de navigatiebalk, biedt verschillende handige acties voor eenvoudige toegang. U kunt deze werkbalk tonen of verbergen door een eenvoudige veegbeweging naar beneden te maken. Dit zijn de beschikbare acties:

- **Zoeken**: Met deze optie kunt u snel zoeken in de huidige map, zodat u eenvoudig specifieke bestanden of mappen kunt vinden.
- **Afspelen hervatten**: Als ingeschakeld in de applicatie-instellingen, herstelt deze functie de wachtrij van de audiospeler en de laatste mediapositie voor de huidige map. Het is een handige manier om verder te gaan waar u was gebleven in uw muziekbibliotheek.
- **Alles afspelen**: Door deze actie te selecteren, scant de app de huidige map en submappen en voegt alle gevonden audiobestanden toe aan een nieuwe speler-wachtrij. Dit is handig wanneer u alle muziek in een bepaalde map wilt afspelen.
- **Alles willekeurig afspelen**: Vergelijkbaar met "Alles afspelen", scant deze actie de huidige map en submappen, maar schudt de bestanden voordat ze aan de audiospelerwachtrij worden toegevoegd. Het is een geweldige manier om uw muziek in willekeurige volgorde te genieten voor wat variatie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Bovenste werkbalk in een cloudmap" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Mapopties

Wanneer u een map in de app opent, vindt u een handige set acties door op de knop "..." in de rechterbovenhoek van het scherm te tikken.   
Hier is een overzicht van deze acties:

- **Selecteren**: Activeer modus voor bestandsselectie. In deze modus kunt u een of meer bestanden in de map selecteren, waardoor het eenvoudig is acties uit te voeren op geselecteerde items.
- **Nieuwe map**: Maak een nieuwe map in de huidige map. Met deze functie kunt u uw bestanden organiseren en uw bibliotheek goed gestructureerd houden.
- **Offline modus inschakelen**: Schakel de offline modus in voor de huidige map. De offline modus gaat verder dan eenvoudig downloaden; het controleert actief de map op wijzigingen. Als u nieuwe bestanden online aan de map toevoegt, worden deze bestanden automatisch naar uw apparaat gedownload. Dit zorgt ervoor dat uw lokale bibliotheek up-to-date blijft met wijzigingen op de server.
- **Bestanden uploaden**: Upload bestanden van uw apparaat naar de online map. Met deze actie kunt u bestanden overbrengen naar de cloud of server, waardoor ze overal toegankelijk worden.
- **Zoeken**: Zoek naar specifieke bestanden in de huidige map. Dit is vooral handig voor het snel vinden van specifieke items in een grote collectie.
- **Sorteren**: Sorteer bestanden in de map op criteria zoals naam, grootte of bewerkingsdatum. De standaard sorteermodus weerspiegelt doorgaans de volgorde op de server, maar u kunt deze aanpassen aan uw voorkeuren.
- **Raster/Lijstweergave**: Schakel tussen twee weergavemodi: tabelweergave en miniatuurweergave. De tabelweergave toont bestanden in een lijst, terwijl de miniatuurweergave visuele representaties van de bestanden toont, zodat u de inhoud in één oogopslag gemakkelijk kunt identificeren.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu met meer acties voor de huidige map" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Online bestanden bewerken

Wanneer u meerdere bestanden in uw cloudopslag op Evermusic wilt beheren, kunt u de selectiemodus gebruiken om uw acties te stroomlijnen. Volg deze stappen voor effectief bestandsbeheer:

- **Selectiemodus activeren**: Open de app op uw apparaat en navigeer naar het gedeelte met uw cloudopslag. Zoek in de rechterbovenhoek de knop "..." (beletselteken). Tik erop en kies het menu-item "Selecteren" om de selectiemodus te activeren.
- **Bestanden kiezen**: U ziet selectievakjes verschijnen naast elk vermeld bestand of elke map. Kies een of meerdere bestanden of mappen door eenvoudig op de selectievakjes naast ze te tikken.
- **Verschillende acties uitvoeren**: Zodra u de te beheren bestanden of mappen heeft geselecteerd, heeft u toegang tot verschillende acties die zijn afgestemd op uw behoeften:

{{< cards cols="1">}}
  {{< card title="" subtitle="Selectiemodus voor online bestanden" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Bestandsacties

Naast de titel van het bestand ziet u een beletselteken "..." (drie puntjes) — dit is het actiemenu.  
Tik erop om een lijst met beschikbare acties te zien:

- **Volgende afspelen**: Kies deze actie om het gekozen bestand bovenaan uw speler-wachtrij in te voegen, zodat het onmiddellijk na het momenteel spelende item speelt.
- **Later afspelen**: Door deze optie te selecteren, wordt het bestand onderaan uw speler-wachtrij toegevoegd, zodat het na de bestaande wachtrij speelt.
- **Toevoegen aan muziekbibliotheek**: Met deze actie kunt u het bestand opnemen in uw muziekbibliotheek, zodat het gemakkelijk toegankelijk en netjes georganiseerd is op artiest, album, genre of componist.
- **Toevoegen aan afspeellijst**: Gebruik deze actie om het bestand toe te voegen aan een bestaande afspeellijst of een nieuwe te maken.
- **Audio-tags bewerken**: Door deze optie te selecteren, heeft u toegang tot de ingebouwde tag-editor van Evermusic, waarmee u audiotags voor het gekozen bestand kunt wijzigen. Het bestand wordt tijdelijk gedownload naar een tijdelijke map en vervolgens naar de opslag geüpload nadat u de wijzigingen bevestigt.
- **Toevoegen aan favorieten**: Met deze actie voegt u het bestand toe aan uw lijst met favoriete bestanden voor snelle en gemakkelijke toegang.
- **Downloaden**: Kies deze actie om het bestand of de map naar uw apparaat te downloaden, zodat het offline beschikbaar is.
- **Hernoemen**: Met deze optie kunt u het bestand rechtstreeks op de externe opslag hernoemen, zodat u aangepaste bestandsnamen kunt gebruiken.
- **Verplaatsen**: Kies deze actie om het bestand naar een andere map in uw cloudopslag te verplaatsen, wat helpt bij het onderhouden van een georganiseerde bestandsstructuur.
- **Openen in**: Gebruik deze actie om het bestand naar een andere compatibele app te exporteren. Het bestand wordt naar uw apparaat gedownload en vervolgens verschijnt het dialoogvenster Delen voor verdere deling of interactie.
- **Verwijderen**: Wees voorzichtig met deze actie, want het verwijdert het bestand permanent van uw cloudopslag. Deze verwijdering kan niet ongedaan worden gemaakt.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu met meer acties voor één bestand" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Als de lijst met acties de beschikbare schermruimte overschrijdt, scrol dan eenvoudig naar beneden in het actiemenu om aanvullende opties te zien.

## Mapacties

Voor elke map in uw cloudopslag zijn verschillende acties beschikbaar. Om toegang te krijgen tot deze opties, tikt u gewoon op het beletselteken "..." naast de maptitel. Als u niet alle acties ziet, scrol dan naar beneden om meer keuzes te zien. Dit zijn de beschikbare acties:

- **Alles afspelen**: Vervang de huidige speler-wachtrij door alle items uit de geselecteerde map.
- **Volgende afspelen**: Voeg de volledige map bovenaan de speler-wachtrij toe, direct na het momenteel spelende item.
- **Later afspelen**: Voeg de inhoud van de map onderaan de speler-wachtrij toe.
- **Toevoegen aan muziekbibliotheek**: Met deze actie integreert u de inhoud van de map naadloos in uw muziekbibliotheek, zodat deze gemakkelijk toegankelijk en netjes georganiseerd is op artiest, album, genre of componist.
- **Toevoegen aan afspeellijst**: U kunt de volledige map in een afspeellijst opnemen. U heeft ook de optie om een nieuwe afspeellijst te maken, waarbij de naam van de map automatisch wordt toegewezen.
- **Toevoegen aan favorieten**: Gebruik deze actie om de map toe te voegen aan uw lijst met favoriete bestanden voor snelle en gemakkelijke toegang.
- **Offline modus inschakelen**: Door de offline modus voor een geselecteerde map in te schakelen, gaat de applicatie verder dan eenvoudig downloaden. Het controleert continu op wijzigingen en als nieuwe bestanden aan de online map worden toegevoegd, worden ze automatisch naar de app gedownload.
- **Downloaden**: Download alle inhoud van de map naar uw apparaat voor offline toegang.
- **Hernoemen**: Hernoem de map rechtstreeks op de externe opslag.
- **Verplaatsen**: Verplaats de map naar een andere locatie in uw cloudopslag.
- **Verwijderen**: Wees voorzichtig met deze actie omdat het de map en de inhoud ervan permanent verwijdert van uw cloudopslag. Deze actie kan niet ongedaan worden gemaakt.


## Snelle toegang

Het gedeelte Snelle toegang bevindt zich bovenaan het scherm. Het geeft u snelle toegang tot uw favoriete en recent geopende bestanden van verbonden cloudservices.
Telkens wanneer u een bestand of map vanuit de cloud opent, wordt het toegevoegd aan de lijst "Recent geopend". Om deze lijst te wissen, opent u "Terkini", tikt u op de knop "Meer acties" en kiest u "Lijst verwijderen." U kunt ook diep geneste mappen als Favorieten markeren om er snel toegang toe te krijgen zonder door de mapstructuur te zoeken.

## Andere services

Dit gedeelte toont extra functies die uw ervaring verbeteren. Momenteel ondersteunt de app Last.fm-scrobbling. Wanneer verbonden, worden uw afspeelstatistieken automatisch naar uw Last.fm-account verzonden. U kunt later uw Last.fm-profiel bezoeken om luisteranalytics te bekijken en gepersonaliseerde muziekaanbevelingen te ontvangen. Gedetailleerde installatie-instructies zijn beschikbaar [hier](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
