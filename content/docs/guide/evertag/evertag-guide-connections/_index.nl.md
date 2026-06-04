---
title: "Verbindingen"
date: 2020-02-01
description: "Leer hoe je cloudopslag, NAS en je computer verbindt met Evertag. Toegang tot en bewerking van audiobestanden rechtstreeks vanuit cloudopslag, persoonlijke NAS of Mac/PC."
keywords: [
  "Evertag cloud-instelling", "iCloud verbinden met Evertag", "SMB bestandstoegang iOS",
  "WebDAV audio-taggeditor", "NAS metadata-bewerking", "Wi-Fi Drive Evertag",
  "audiobestanden naar iPhone overdragen", "Evertag iTunes File Sharing", "FLAC-tags bewerken vanuit cloud"
]
tags: ["handleiding", "evertag", "verbindingen"]
readingTime: 11
---


Op dit scherm kun je verschillende bronnen verbinden die je audiobestanden bevatten. Je kunt populaire cloudservices zoals Google Drive, Dropbox, OneDrive, iCloud en andere integreren, maar ook je Mac of PC verbinden. Daarnaast heb je de mogelijkheid om audiobestanden te bewerken die zich in Apple Time Capsule, WD Cloud Home of een NAS bevinden die SMB of WebDAV ondersteunt.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Verbindingen Scherm" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Snelle toegang

Bovenaan het scherm Verbindingen vind je een lijst **Snelle toegang**. Elke cloudmap die je aan favorieten toevoegt — ook als die diep genest is — verschijnt hier zodat je er direct naartoe kunt zonder elke keer door de bovenliggende mappen te hoeven navigeren.

## Verbinding maken met cloudopslag

- Open het tabblad 'Verbindingen'  
- Selecteer 'Verbinding maken met cloudopslag' in het menu  
- Kies een cloudopslagservice uit de lijst  
- Voer je inloggegevens in en tik op 'Voltooid.'

Als je problemen ondervindt, controleer dan je internetverbinding en gebruikersnaam/wachtwoord.  
In de Premium-versie van de app kun je een onbeperkt aantal services toevoegen.

## Ondersteunde cloudopslagservices

Momenteel ondersteunt de applicatie de populairste cloudopslagservices: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), evenals elke SMB- of WebDAV-server.

## Beveiliging en privacy

We gebruiken alleen officiële SDK's en beveiligde verbindingen om te communiceren met verbonden cloudservices. Je gebruikersnaam en wachtwoord zijn niet toegankelijk voor de applicatie. Alle verzoeken van de applicatie naar de cloudservice zijn versleuteld.

Wanneer je je gebruikersnaam en wachtwoord invoert, toont de applicatie de officiële autorisatiepagina van de cloudserviceprovider en vindt het volledige autorisatieproces buiten de applicatie plaats. De cloudserviceprovider stuurt na succesvolle autorisatie een auth-token naar de applicatie, en dat token wordt gebruikt voor API-aanroepen.

Een auth-token is een digitale sleutel waarmee applicaties van derden kunnen communiceren met cloudopslag. Het auth-token wordt op je apparaat opgeslagen in een beveiligde systeemopslag genaamd Keychain. Je kunt bestanden van de verbonden cloudservice naar het apparaat downloaden, en die bestanden worden geplaatst in de map "Documenten" van de app. Je kunt deze bestanden altijd verwijderen via de ingebouwde bestandsbeheerder.

De applicatie deelt geen informatie van het verbonden cloudaccount. Je kunt de toegang tot je cloudaccount op elk moment intrekken door de accountinstellingenpagina in je webbrowser te openen.

## Auth-token intrekken

Log in op je account in een webbrowser en navigeer naar de instellingenpagina. Daar kun je alle applicaties van derden vinden die zijn verbonden met je cloudaccount en die verwijderen als je de applicatie niet meer wilt gebruiken. Gedetailleerde instructies zijn [hier](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) beschikbaar.

Je kunt ook de verbonden cloudaccounts in de applicatie verbreken, waarna het auth-token ook van je apparaat wordt verwijderd. Als je de applicatie van je apparaat verwijdert, worden alle gedownloade gegevens en toegangstokens ook verwijderd.

## Een cloudopslag verbreken of configuratie wijzigen

- Toegang tot Cloudopslag-opties: Zoek eerst de cloudopslag die je wilt beheren in de interface van de app.  
- Tik op de '...'-knop: Naast de servicetitel zie je een '...'-knop. Tik erop voor toegang tot extra opties.  
  - **Hernoemen**: Als je de naam van de cloudservice wilt wijzigen zoals deze in je lijst verschijnt, selecteer dan 'Hernoemen.'  
  - **Instellingen**: Om de configuratie of authenticatiegegevens van de cloudservice te wijzigen, kies je 'Instellingen.' Soms moet je de verbonden cloudservice opnieuw autoriseren als het autorisatietoken is verlopen.  
  - **Ontkoppelen**: Als je de verbinding tussen de app en de cloudservice volledig wilt verbreken, selecteer dan 'Ontkoppelen.' Wees er bewust van dat het kiezen van deze optie alle nummers die verband houden met deze cloudservice uit de muziekbibliotheek van je app verwijdert, maar ze blijven op de server.

## Verbinding maken met computer of NAS

Je kunt ook je computer, persoonlijke NAS of andere netwerkapparaten verbinden via het SMB-, DLNA- of WebDAV-protocol.

## Verbinding maken met computer via SMB

- Tik op "Verbinding maken met cloudopslag" → SMB.  
- Voer het IP-adres van de computer en de naam van de gedeelde map in het URL-veld in met het formaat smb://computer-ip-adres/gedeelde-map-naam  
- Kies protocolversie: Automatisch, SMB1, SMB2  
- Voer gebruikersnaam en wachtwoord in (indien vereist)  
- Tik op "Voltooid."

Als de verbinding succesvol is, zie je de verbonden opslag in de sectie "Cloudopslag".  
Een volledige handleiding over het verbinden van je Mac of PC via SMB is [hier](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) beschikbaar.

## Verbinding maken met NAS via WebDAV

Alle stappen zijn hetzelfde, behalve voor het URL-veld.  
De URL moet de indeling http://servernaam hebben, of https://servernaam als de server SSL ondersteunt.  
Een volledige handleiding over het verbinden van NAS via het WebDAV-protocol is [hier](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) beschikbaar.

## Beschikbare apparaten

Dit gedeelte toont alle apparaten in je lokale netwerk waarmee je verbinding kunt maken via de applicatie.  
Volg deze stappen om verbinding te maken met een apparaat:

- Open de app en ga naar het gedeelte "Beschikbare apparaten".  
- Tik op het apparaat waarmee je verbinding wilt maken in de lijst.  
- Voer indien nodig je inloggegevens in om de verbinding te voltooien.

## Wi-Fi Drive 

Wi-Fi Drive is een handige technologie waarmee je bestanden draadloos kunt overdragen van je computer naar je iOS-apparaat via een desktopbrowser.  
Zorg ervoor dat je apparaat en computer zijn verbonden met hetzelfde Wi-Fi-netwerk om deze functie effectief te gebruiken.  
Hier is een stapsgewijze handleiding voor het gebruik van Wi-Fi Drive.

## Wi-Fi Drive inschakelen

- Open de applicatie en ga naar het tabblad "Verbindingen".  
- Selecteer "Verbinden via Wi-Fi" voor toegang tot het Wi-Fi Drive-hoofdscherm.  
- Tik op "Wi-Fi Drive starten" om Wi-Fi Drive in te schakelen.

## Wi-Fi Drive openen op je computer

- Open op je computer (desktop of laptop) een webbrowser (zoals Chrome, Firefox of Safari).  
- Voer in de adresbalk van de browser de URL in die door de applicatie is opgegeven.

## Bestanden draadloos overdragen

Zodra de webpagina die overeenkomt met je iOS-apparaat in de browser opent, kun je eenvoudig bestanden van je computer naar de webpagina slepen en neerzetten.  
De bestanden die je sleept en neerzet, worden overgedragen naar je iOS-apparaat en zijn toegankelijk in de applicatie.

Gedetailleerde instructies voor het draadloos overdragen van bestanden via Wi-Fi Drive zijn [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) beschikbaar.

## iTunes File Sharing

iTunes File Sharing is een andere technologie waarmee je bestanden kunt overdragen van een computer naar een apparaat via de Finder-app op je Mac en een Lightning-kabel.  
- Verbind het apparaat gewoon met de computer via een kabel en start de Finder-app op je Mac.  
- Open "Locaties" → "Verbonden apparaat" → "Bestanden" → en vind de huidige app.  
- Tik op het app-pictogram om alle gedeelde mappen te zien.  
- Kopieer bestanden van de computer naar de gedeelde map op het apparaat via slepen en neerzetten.

Gedetailleerde instructies voor het gebruik van iTunes File Sharing zijn [hier](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) beschikbaar.

## Een USB-flashkaart verbinden

Als je een SD-kaart of USB-stick hebt, kun je deze verbinden via een Lightning- of USB-C-kaartlezer op iPhone/iPad, of rechtstreeks in een Mac stoppen. De app ondersteunt momenteel Apple-gecertificeerde kaartlezers. We hebben gedetailleerde instructies voor het verbinden van een USB-flashkaart met je iPhone of iPad en het beheren van bestanden erop, beschikbaar [hier](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Verbonden schijven verschijnen in het gedeelte **Externe accessoires** van het scherm Verbindingen.

## Bestandsbeheerder

Zodra je een cloudopslagservice hebt verbonden, tik je op het pictogram om alle beschikbare bestanden en mappen te bekijken. Je kunt de ingebouwde bestandsbeheerder gebruiken om met deze bestanden te werken — downloaden, hernoemen, verplaatsen en meer. Wanneer je een download start, verschijnt het bestand in de overdrachtsrij. Om de overdrachtsrij te bekijken, ga je naar het tabblad "Lokale bestanden" en tik je op de draaiende pijlen in de linkerbovenhoek. Alle gedownloade bestanden en mappen zijn beschikbaar in het gedeelte "Lokale bestanden".

## Bovenste werkbalk

De bovenste werkbalk, handig geplaatst onder de navigatiebalk, biedt verschillende nuttige acties voor eenvoudige toegang. Je kunt deze werkbalk tonen of verbergen met een eenvoudig veeggebaar naar beneden. Dit zijn de beschikbare acties:

- **Zoeken**: Met deze optie kun je snel zoeken in de huidige map, waardoor het eenvoudig is om specifieke bestanden of mappen te vinden.  

## Mapopties

Wanneer je een map opent in de app, vind je een handig set acties beschikbaar door op de "..."-knop in de rechterbovenhoek van het scherm te tikken.  
Dit zijn de beschikbare acties:

- **Selecteren**: Activeer de bestandsselectiemodus. Met deze modus kun je een of meer bestanden in de map kiezen, waardoor het eenvoudig is om acties uit te voeren op geselecteerde items.  
- **Nieuwe map**: Maak een nieuwe map aan in de huidige map. Met deze functie kun je je bestanden organiseren en je bibliotheek goed gestructureerd houden.   
- **Bestanden uploaden**: Upload bestanden van je apparaat naar de online map. Met deze actie kun je bestanden overdragen naar de cloud of server, zodat ze overal toegankelijk zijn.  
- **Zoeken**: Zoek naar specifieke bestanden in de huidige map. Dit is vooral handig om snel specifieke items te vinden in een grote collectie.  
- **Sorteren**: Sorteer bestanden in de map op criteria zoals naam, grootte of bewerkingsdatum. De standaard sorteermodus weerspiegelt doorgaans de sorteervolgorde op de server, maar je kunt deze aanpassen aan je voorkeur.  
- **Raster/Lijstweergave**: Schakel tussen twee weergavemodi: tabelweergave en miniatuurweergave. De tabelweergave toont bestanden in een lijst, terwijl de miniatuurweergave visuele weergaven van de bestanden toont, waardoor het gemakkelijker is om inhoud in één oogopslag te identificeren.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloudmap Sorteren" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Online bestanden bewerken

Wanneer je meerdere bestanden in je cloudopslag in deze app wilt beheren, kun je de selectiemodus gebruiken om je acties te stroomlijnen. Volg deze stappen voor effectief bestandsbeheer:

- **Selectiemodus activeren**: Open de app op je apparaat en navigeer naar het gedeelte met je cloudopslag. Zoek de rechterbovenhoek waar je de "..." (beletselteken)-knop vindt. Tik erop en kies het menu-item "Selecteren" om de selectiemodus te activeren.  
- **Bestanden kiezen**: Je zult zien dat er selectievakjes verschijnen naast elk bestand of map in de lijst. Kies een of meerdere bestanden of mappen door simpelweg op de selectievakjes ernaast te tikken.  
- **Verschillende acties uitvoeren**: Nadat je de bestanden of mappen hebt geselecteerd die je wilt beheren, heb je toegang tot verschillende op je behoeften afgestemde acties:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Bestand Selecteren" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Bestandsacties

Naast de bestandstitel zie je een beletselteken "..." (drie punten) – dit is het actiemenu.  
Tik erop om een lijst met beschikbare acties te onthullen:

- **Audio-tags bewerken**: Door deze optie te selecteren, krijg je toegang tot de ingebouwde taggeditor, waarmee je audiotags voor het gekozen bestand kunt wijzigen. Het bestand wordt tijdelijk gedownload naar een tijdelijke map en daarna geüpload naar de opslag nadat je de wijzigingen bevestigt.  
- **Toevoegen aan Favorieten**: Met deze actie voeg je het bestand toe aan je lijst met favoriete bestanden voor snelle en gemakkelijke toegang.  
- **Downloaden**: Kies deze actie om het bestand of de map naar je apparaat te downloaden, zodat het beschikbaar is voor offline gebruik.  
- **Hernoemen**: Met deze optie kun je het bestand rechtstreeks op de externe opslag hernoemen voor aangepaste bestandsnaamgeving.  
- **Verplaatsen**: Kies deze actie om het bestand naar een andere map in je cloudopslag te verplaatsen, wat helpt bij het handhaven van een georganiseerde bestandsstructuur.  
- **Openen in**: Gebruik deze actie om het bestand te exporteren naar een andere compatibele app. Het bestand wordt naar je apparaat gedownload en vervolgens verschijnt het dialoogvenster Delen voor verdere deling of interactie.  
- **Verwijderen**: Wees voorzichtig met deze actie, want hiermee wordt het bestand permanent verwijderd uit je cloudopslag. **Dit verwijderen kan niet ongedaan worden gemaakt**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Bestandsopties" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Als de lijst met acties de beschikbare schermruimte overschrijdt, scrol dan gewoon omlaag in het actiemenu voor toegang tot extra opties.

## Mapacties

Voor elke map in je cloudopslag zijn er verschillende acties beschikbaar. Om deze opties te openen, tik je eenvoudig op het beletseltekenpictogram "..." naast de maptitel. Als je niet alle acties ziet, scrol dan omlaag om meer opties te zien. Dit zijn de beschikbare acties:

- **Toevoegen aan Favorieten**: Gebruik deze actie om de map toe te voegen aan je lijst met favoriete bestanden voor snelle en gemakkelijke toegang.  
- **Downloaden**: Download alle inhoud van de map naar je apparaat voor offline toegang.  
- **Hernoemen**: Hernoem de map rechtstreeks op de externe opslag.  
- **Verplaatsen**: Verplaats de map naar een andere locatie in je cloudopslag.  
- **Verwijderen**: Wees voorzichtig met deze actie, want hiermee wordt de map en de inhoud ervan permanent verwijderd uit je cloudopslag. **Deze actie kan niet ongedaan worden gemaakt**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Mapopties" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
