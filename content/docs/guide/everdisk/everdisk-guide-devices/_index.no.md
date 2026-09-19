---
title: "Koble til servere"
date: 2026-08-20
description: "Bruk Enheter-fanen i Everdisk for å koble til andre servere på nettverket ditt. Legg til og bla i DLNA-, WebDAV-, FTP-, SFTP- og SMB-servere og NAS-disker, stream lyd og video, last ned filer, og opprett, last opp, gi nytt navn, flytt eller slett på servere som tillater det."
keywords: ["Everdisk Enheter-fane", "koble til NAS", "DLNA-klient iPhone", "WebDAV-klient iPhone", "FTP-klient iPhone", "SFTP-klient iPhone", "SMB-klient iPhone", "koble til SMB-delt mappe", "bla i nettverksserver", "streame fra NAS", "laste ned fra server", "koble til sky WebDAV"]
tags: ["everdisk", "veiledning", "enheter", "tilkoblinger"]
readingTime: 9
---


Everdisk er ikke bare en trådløs disk - den er også en klient for de andre enhetene på nettverket ditt. **Enheter**-fanen lar deg koble til **DLNA**-, **WebDAV**-, **FTP**-, **SFTP**- og **SMB**-servere, inkludert Mac-er, Windows-PC-er, Linux-maskiner, NAS-disker og medieservere, for deretter å bla i, streame og laste ned filene deres.

## Enheter-skjermen

Enheter-fanen har to deler:

- **Tilkoblinger** - serverne du allerede har lagret.
- **Tilgjengelige enheter** - servere Everdisk finner automatisk på ditt lokale nettverk.

For å koble til noe Everdisk allerede har funnet, trykker du bare på det under **Tilgjengelige enheter**. For å legge til en server manuelt, trykk på **pluss (+)**-knappen eller **Ny tilkobling**.

## Legg til en ny tilkobling

Trykk **Ny tilkobling** og velg typen server du vil nå:

- **DLNA / UPnP** - best for medieservere. Stream video, musikk og bilder fra mediebiblioteker, nettverkslagringsdisker og DLNA-kompatible TV-er og datamaskiner. DLNA er skrivebeskyttet: du kan bla, streame og laste ned, men du kan ikke laste opp eller endre filer.
- **WebDAV** - koble til filservere, nettverkslagringsdisker og skydisker som støtter WebDAV. Les og skriv når serveren tillater det.
- **FTP** - vanlig på rutere, nettverkslagringsdisker og webhotell. Standardporten er 21 (990 for sikker FTPS); du kan angi en egendefinert port i adressen, for eksempel `ftp://host:2121`. La brukernavnet og passordet stå tomme for anonym tilgang.
- **SFTP** - koble til sikkert over SSH. Standardporten er 22; bruk en egendefinert port i adressen om nødvendig, for eksempel `sftp://host:2222`.
- **SMB** - koble til Mac-er, Windows-PC-er, Linux-servere og nettverkslagring (NAS) som deler mapper over **SMB / CIFS**. Skriv inn en adresse som `smb://server-address/share-name/` (eksempler: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB legger til to valgfrie felt: et **Arbeidsgruppe**-navn og en **Protokollversjon** du kan la stå på **Automatisk** eller tvinge til **SMB1** eller **SMB2**. Hvis filer eller mapper med spesialtegn ikke vil åpnes, prøv å bytte versjonen til **SMB1**.

> Everdisk kobler bare til disse protokollene på lokalnettet og direkte adresserte protokollene. Den logger ikke inn på skykontoer som Google Drive eller Dropbox. En skydisk er kun tilgjengelig hvis den tjenesten tilbyr en **WebDAV**-adresse du kan skrive inn.

## Skriv inn adressen og logg inn

I tilkoblingsredigereren fyller du inn:

- **Tittel** - et vennlig navn på tilkoblingen.
- **URL / adresse** - serveradressen (eksempler vises for hver type).
- **Brukernavn** og **Passord** - la begge stå tomme hvis serveren tillater anonym tilgang.

For WebDAV kan du tillate ugyldige sertifikater hvis serveren din bruker et selvsignert sertifikat. Hvis identiteten til en sikker server ikke kan bekreftes, ber Everdisk deg om å bekrefte før den stoler på den.

Gratisbrukere kan lagre opptil **10** tilkoblinger. Premium fjerner grensen.

## Bla, stream og last ned

Når du er tilkoblet, trykker du på serveren for å åpne den:

- **Bla** i mappene i liste eller rutenett, sorter dem og se miniatyrer. DLNA-servere viser også musikkdetaljer og omslag.
- **Stream** lyd og video. Lyd går til køen i minispilleren; video spilles av i fullskjerm. Spoling fungerer mens en fil streames.
- **Last ned** filer til enheten din. Velg flere om gangen for en samlet nedlasting. Nedlastinger vises i **Filoverføringer** og havner i **Dokumenter**-mappen din.
- **Info** på et hvilket som helst element viser typen, størrelsen, datoen, banen og mediedetaljene.

## Endre filer på en server

På servere som tillater skriving - **WebDAV, FTP, SFTP og SMB** - kan du også administrere filer:

- **Ny mappe**
- **Last opp filer** fra enheten din
- **Gi nytt navn**, **Flytt** og **Slett** (ett element eller flere om gangen)

**DLNA**-servere er skrivebeskyttet, så disse handlingene er ikke tilgjengelige der.

## Følg med på overføringene dine

Nedlastinger og opplastinger kjører i bakgrunnen og dukker opp i **Filoverføringer**, som du åpner øverst til venstre i **Dokumenter**-fanen. Der kan du følge fremdriften, og sette på pause, gjenoppta, prøve på nytt, avbryte eller tømme oppgaver. Du kan også justere overføringer i [Innstillinger → Nettverk](/docs/guide/everdisk/everdisk-guide-settings) (kun Wi-Fi kontra Wi-Fi og mobildata, hvor mange som kjører om gangen, og om de fortsetter i bakgrunnen).

## Neste steg

- [Filer og dokumenter](/docs/guide/everdisk/everdisk-guide-files) - administrer alt du laster ned.
- [Bilder, musikk og video](/docs/guide/everdisk/everdisk-guide-media) - spill av det du streamer.
- [Innstillinger](/docs/guide/everdisk/everdisk-guide-settings) - tilkoblingsgrenser og overføringsalternativer.
