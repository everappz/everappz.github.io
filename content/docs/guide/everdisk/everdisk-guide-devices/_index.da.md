---
title: "Opret forbindelse til servere"
date: 2026-08-20
description: "Brug fanen Enheder i Everdisk til at oprette forbindelse til andre servere på dit netværk. Tilføj og gennemse DLNA-, WebDAV-, FTP-, SFTP- og SMB-servere og NAS-drev, stream lyd og video, download filer, og opret, upload, omdøb, flyt eller slet på servere, der tillader det."
keywords: ["Everdisk fanen Enheder", "opret forbindelse til NAS", "DLNA-klient iPhone", "WebDAV-klient iPhone", "FTP-klient iPhone", "SFTP-klient iPhone", "SMB-klient iPhone", "forbind til SMB-share", "gennemse netværksserver", "stream fra NAS", "download fra server", "forbind cloud WebDAV"]
tags: ["everdisk", "vejledning", "enheder", "forbindelser"]
readingTime: 9
---


Everdisk er ikke kun et trådløst drev - den er også en klient til de andre enheder på dit netværk. Fanen **Enheder** lader dig oprette forbindelse til **DLNA**-, **WebDAV**-, **FTP**-, **SFTP**- og **SMB**-servere, herunder Mac-computere, Windows-pc'er, Linux-maskiner, NAS-drev og medieservere, og derefter gennemse, streame og downloade deres filer.

## Enheder-skærmen

Fanen Enheder har to dele:

- **Forbindelser** - de servere, du allerede har gemt.
- **Tilgængelige enheder** - servere, som Everdisk finder automatisk på dit lokale netværk.

For at oprette forbindelse til noget, Everdisk allerede har fundet, skal du bare trykke på det under **Tilgængelige enheder**. For at tilføje en server manuelt trykker du på **plus (+)**-knappen eller **Ny forbindelse**.

## Tilføj en ny forbindelse

Tryk på **Ny forbindelse**, og vælg den type server, du vil nå:

- **DLNA / UPnP** - bedst til medieservere. Stream video, musik og fotos fra mediebiblioteker, netværksdrev og DLNA-aktiverede TV og computere. DLNA er skrivebeskyttet: du kan gennemse, streame og downloade, men du kan ikke uploade eller ændre filer.
- **WebDAV** - opret forbindelse til filservere, netværksdrev og cloud-drev, der understøtter WebDAV. Læs og skriv, når serveren tillader det.
- **FTP** - almindelig på routere, netværksdrev og webhosting. Standardporten er 21 (990 til sikker FTPS); du kan angive en brugerdefineret port i adressen, for eksempel `ftp://host:2121`. Lad login og adgangskode stå tomme for anonym adgang.
- **SFTP** - opret sikker forbindelse over SSH. Standardporten er 22; brug om nødvendigt en brugerdefineret port i adressen, for eksempel `sftp://host:2222`.
- **SMB** - opret forbindelse til Mac-computere, Windows-pc'er, Linux-servere og netværkslager (NAS), der deler mapper via **SMB / CIFS**. Indtast en adresse som `smb://server-address/share-name/` (eksempler: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB tilføjer to valgfrie felter: et **Arbejdsgruppe**-navn og en **Protokolversion**, som du kan lade stå på **Automatisk version** eller tvinge til **SMB1** eller **SMB2**. Hvis filer eller mapper med specialtegn ikke vil åbne, så prøv at skifte versionen til **SMB1**.

> Everdisk forbinder kun til disse protokoller på det lokale netværk og til direkte adresserede servere. Den logger ikke ind på cloud-konti som Google Drive eller Dropbox. Et cloud-drev kan kun nås, hvis den pågældende tjeneste tilbyder en **WebDAV**-adresse, du kan indtaste.

## Indtast adressen, og log ind

I forbindelseseditoren udfylder du:

- **Titel** - et venligt navn til forbindelsen.
- **URL / adresse** - serverens adresse (eksempler vises for hver type).
- **Login** og **Adgangskode** - lad begge stå tomme, hvis serveren tillader anonym adgang.

For WebDAV kan du tillade ugyldige certifikater, hvis din server bruger et selvsigneret certifikat. Hvis en sikker servers identitet ikke kan bekræftes, beder Everdisk dig om at bekræfte, før den stoler på den.

Gratis brugere kan gemme op til **10** forbindelser. Premium fjerner grænsen.

## Gennemse, stream og download

Når forbindelsen er oprettet, trykker du på serveren for at åbne den:

- **Gennemse** mapperne i liste- eller gittervisning, sortér dem, og se miniaturer. DLNA-servere viser også musikdetaljer og illustrationer.
- **Stream** lyd og video. Lyd føjes til miniafspillerens kø; video afspilles i fuld skærm. Du kan søge i en fil, mens den streames.
- **Download** filer til din enhed. Vælg flere på én gang for at downloade i én omgang. Downloads vises under **Filoverførsler** og lander i din mappe **Dokumenter**.
- **Info** på et element viser dets type, størrelse, dato, sti og mediedetaljer.

## Ændr filer på en server

På servere, der tillader skrivning - **WebDAV, FTP, SFTP og SMB** - kan du også håndtere filer:

- **Ny mappe**
- **Upload filer** fra din enhed
- **Omdøb**, **Flyt** og **Slet** (ét element eller flere på én gang)

**DLNA**-servere er skrivebeskyttede, så disse handlinger er ikke tilgængelige der.

## Følg dine overførsler

Downloads og uploads kører i baggrunden og vises under **Filoverførsler**, som du åbner øverst til venstre på fanen **Dokumenter**. Der kan du følge forløbet og sætte opgaver på pause, genoptage, prøve igen, annullere eller rydde dem. Du kan også justere overførsler under [Indstillinger → Netværk](/docs/guide/everdisk/everdisk-guide-settings) (kun Wi-Fi vs. Wi-Fi og mobildata, hvor mange der kører samtidig, og om de fortsætter i baggrunden).

## Næste skridt

- [Filer og dokumenter](/docs/guide/everdisk/everdisk-guide-files) - håndtér alt, hvad du downloader.
- [Fotos, musik og video](/docs/guide/everdisk/everdisk-guide-media) - afspil det, du streamer.
- [Indstillinger](/docs/guide/everdisk/everdisk-guide-settings) - forbindelsesgrænser og overførselsmuligheder.
