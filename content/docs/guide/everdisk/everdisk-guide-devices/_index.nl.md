---
title: "Verbinden met servers"
date: 2026-08-20
description: "Gebruik het tabblad Apparaten in Everdisk om verbinding te maken met andere servers op je netwerk. Voeg DLNA-, WebDAV-, FTP-, SFTP- en SMB-servers en NAS-schijven toe en doorblader ze, stream audio en video, download bestanden en maak, upload, hernoem, verplaats of verwijder op servers die dat toestaan."
keywords: ["Everdisk tabblad Apparaten", "verbinden met NAS", "DLNA-client iPhone", "WebDAV-client iPhone", "FTP-client iPhone", "SFTP-client iPhone", "SMB-client iPhone", "verbinden met SMB-share", "netwerkserver doorbladeren", "streamen vanaf NAS", "downloaden van server", "verbinden cloud WebDAV"]
tags: ["everdisk", "handleiding", "apparaten", "verbindingen"]
readingTime: 9
---


Everdisk is niet alleen een draadloze schijf - het is ook een client voor de andere apparaten op je netwerk. Met het tabblad **Apparaten** maak je verbinding met **DLNA**-, **WebDAV**-, **FTP**-, **SFTP**- en **SMB**-servers, waaronder Macs, Windows-pc's, Linux-machines, NAS-schijven en mediaservers, om vervolgens hun bestanden te doorbladeren, te streamen en te downloaden.

## Het Apparaten-scherm

Het tabblad Apparaten bestaat uit twee delen:

- **Verbindingen** - de servers die je al hebt opgeslagen.
- **Beschikbare apparaten** - servers die Everdisk automatisch vindt op je lokale netwerk.

Om verbinding te maken met iets dat Everdisk al heeft gevonden, tik je het gewoon aan onder **Beschikbare apparaten**. Om handmatig een server toe te voegen, tik je op de knop **plus (+)** of op **Nieuwe verbinding**.

## Een nieuwe verbinding toevoegen

Tik op **Nieuwe verbinding** en kies het type server dat je wilt bereiken:

- **DLNA / UPnP** - het beste voor mediaservers. Stream video, muziek en foto's vanaf mediabibliotheken, netwerkopslagschijven en DLNA-tv's en -computers. DLNA is alleen-lezen: je kunt doorbladeren, streamen en downloaden, maar niet uploaden of bestanden wijzigen.
- **WebDAV** - maak verbinding met bestandsservers, netwerkopslagschijven en cloudschijven die WebDAV ondersteunen. Lezen en schrijven wanneer de server dat toestaat.
- **FTP** - gebruikelijk op routers, netwerkopslagschijven en webhosting. De standaardpoort is 21 (990 voor beveiligde FTPS); je kunt een aangepaste poort in het adres zetten, bijvoorbeeld `ftp://host:2121`. Laat de login en het wachtwoord leeg voor anonieme toegang.
- **SFTP** - maak veilig verbinding via SSH. De standaardpoort is 22; gebruik indien nodig een aangepaste poort in het adres, bijvoorbeeld `sftp://host:2222`.
- **SMB** - verbind met Macs, Windows-pc's, Linux-servers en netwerkopslag (NAS) die mappen delen via **SMB / CIFS**. Voer een adres in zoals `smb://server-address/share-name/` (voorbeelden: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB voegt twee optionele velden toe: een naam voor de **Werkgroep** en een **Protocolversie** die je op **Automatisch** kunt laten staan of kunt forceren naar **SMB1** of **SMB2**. Als bestanden of mappen met speciale tekens niet openen, probeer dan de versie op **SMB1** te zetten.

> Everdisk maakt alleen verbinding met deze protocollen op het lokale netwerk en met direct geadresseerde protocollen. Het logt niet in op cloudaccounts zoals Google Drive of Dropbox. Een cloudschijf is alleen bereikbaar als die dienst een **WebDAV**-adres biedt dat je kunt intikken.

## Voer het adres in en meld je aan

Vul in de verbindingseditor in:

- **Titel** - een herkenbare naam voor de verbinding.
- **URL / adres** - het serveradres (per type worden voorbeelden getoond).
- **Login** en **Wachtwoord** - laat beide leeg als de server anonieme toegang toestaat.

Bij WebDAV kun je ongeldige certificaten toestaan als je server een zelfondertekend certificaat gebruikt. Kan de identiteit van een beveiligde server niet worden geverifieerd, dan vraagt Everdisk je om dat te bevestigen voordat het de server vertrouwt.

Gratis gebruikers kunnen tot **10** verbindingen opslaan. Premium heft de limiet op.

## Doorbladeren, streamen en downloaden

Zodra je verbonden bent, tik je op de server om die te openen:

- **Doorblader** de mappen in lijst of raster, sorteer ze en bekijk miniaturen. DLNA-servers tonen ook muziekgegevens en hoezen.
- **Stream** audio en video. Audio gaat naar de wachtrij van de miniplayer; video speelt op volledig scherm. Vooruit- en achteruitspoelen werkt terwijl een bestand streamt.
- **Download** bestanden naar je apparaat. Selecteer er meerdere tegelijk voor een batchdownload. Downloads verschijnen in **Bestandsoverdrachten** en komen terecht in je map **Documenten**.
- **Info** op een item toont het type, de grootte, de datum, het pad en mediagegevens.

## Bestanden op een server wijzigen

Op servers die schrijven toestaan - **WebDAV, FTP, SFTP en SMB** - kun je ook bestanden beheren:

- **Nieuwe map**
- **Bestanden uploaden** vanaf je apparaat
- **Hernoemen**, **Verplaatsen** en **Verwijderen** (één item of meerdere tegelijk)

**DLNA**-servers zijn alleen-lezen, dus deze acties zijn daar niet beschikbaar.

## Houd je overdrachten in de gaten

Downloads en uploads lopen op de achtergrond en verschijnen in **Bestandsoverdrachten**, dat je linksboven op het tabblad **Documenten** opent. Daar kun je de voortgang volgen en taken pauzeren, hervatten, opnieuw proberen, annuleren of wissen. Je kunt overdrachten ook afstemmen in [Instellingen → Netwerk](/docs/guide/everdisk/everdisk-guide-settings) (alleen Wi-Fi of Wi-Fi en mobiel, hoeveel er tegelijk lopen en of ze op de achtergrond doorgaan).

## Volgende stappen

- [Bestanden en documenten](/docs/guide/everdisk/everdisk-guide-files) - beheer alles wat je downloadt.
- [Foto's, muziek en video](/docs/guide/everdisk/everdisk-guide-media) - speel af wat je streamt.
- [Instellingen](/docs/guide/everdisk/everdisk-guide-settings) - verbindingslimieten en overdrachtsopties.
