---
title: "Deling"
date: 2026-08-20
description: "Lær hvordan deling fungerer i Everdisk: trykk Start for å gjøre din iPhone eller iPad om til en trådløs disk, velg hva du vil dele (filer, mapper, bilder og musikk), kjør de fem serverne (DLNA, HTTP, WebDAV, SMB, FTP), krypter SMB-tilkoblingen med SMB3 (AES), les tilkoblingsadressene, se hvem som er tilkoblet, og hold delingen i gang over Wi-Fi eller en USB-kabel."
keywords: ["Everdisk deling", "trådløs disk iPhone", "start deling", "dele filer iPhone", "dele bilder over nettverk", "DLNA HTTP WebDAV FTP", "hva du skal dele", "hvordan koble til", "hold appen åpen", "deling over Wi-Fi eller USB"]
tags: ["everdisk", "veiledning", "deling"]
readingTime: 9
---


**Deling**-fanen er hjertet i Everdisk. Det er her du gjør din iPhone eller iPad om til en trådløs disk, velger nøyaktig hva du vil dele, og får adressene som andre enheter bruker for å koble til. Dette er den første fanen du ser når du åpner appen.

## Start og stopp deling

Midt på Deling-skjermen finner du en stor, rund knapp.

- Trykk **Start** for å sette alle de aktiverte serverne dine på nett samtidig. Knappen viser **Starter...**, og deretter **Stopp** når delingen er i gang.
- Trykk **Stopp** for å ta alt av nett igjen. Tilkoblede enheter blir koblet fra.

Mens deling er i gang, er de valgte filene, bildene og musikken din tilgjengelig for enhver enhet på samme nettverk som kobler til med en av de fem metodene nedenfor.

> Deling kjører bare mens appen er åpen. Se **Hold appen åpen** nær slutten av denne siden for hvorfor, og hvordan du holder store overføringer i gang.

## Velg hva du vil dele

Før du starter, trykk på overskriften **Hva som skal deles** for å åpne tre grupper. Du kan dele en hvilken som helst kombinasjon av dem, og du må velge minst én ting før delingen kan starte.

**Filer og mapper**

- Appens egen **Dokumenter**-mappe deles som standard. Du kan slutte å dele den hvis du foretrekker det.
- Trykk **Legg til mappe** for å dele en mappe fra hvor som helst på enheten din, eller **Legg til fil** for å dele enkeltfiler.
- Hvert delt element har en **Info**-knapp og en **Slutt å dele**-knapp.

**Bilder og videoer**

- Slå på **Tillat tilgang til hele bildebiblioteket** for å dele hele foto- og videobiblioteket ditt, eller
- Trykk **Legg til bilder** for å plukke ut kun de bildene og videoene du vil dele.

**Musikk**

- Slå på **Tillat tilgang til hele musikkbiblioteket** for å dele hele musikkbiblioteket ditt, eller
- Trykk **Legg til spor** for å dele bare utvalgte sanger.
- Spor som er beskyttet (DRM) eller kun lagret i skyen kan ikke deles.

Hvis du prøver å starte uten å ha valgt noe, viser Everdisk et varsel om at det er **Ingenting å dele**. Hvis du endrer hva som deles mens delingen er i gang, trykk **Stopp og start på nytt** for å ta i bruk endringen.

## De fem serverne

Everdisk deler det samme innholdet på fem måter samtidig. Hver av dem er laget for en bestemt type enhet, og hver kan slås av eller på i **Innstillinger → Deling → Tilkoblinger**. Som standard er alle fem på.

- **TV og mediesenter (DLNA)** - for smart-TV-er og mediespillere. De oppdager enheten din helt av seg selv og viser bildene, videoene og musikken din, med forhåndsvisningsminiatyrer.
- **Nettleser (HTTP)** - for enhver telefon, nettbrett eller datamaskin. Den andre personen åpner en lenke i en nettleser for å bla i og laste ned filene dine. Ingenting å installere.
- **Datamaskin (WebDAV)** - for en Mac, Windows-PC eller Linux-maskin. Enheten din dukker opp som en vanlig nettverksdisk, slik at du kan dra filer begge veier.
- **Datamaskin (avansert) (SMB)** - en nettverksdisk for Mac, Windows og Linux. På en Mac dukker den opp helt av seg selv i Finder-sidefeltet; på Windows åpner du den i Filutforsker med en `smb://`-adresse. Det er den eneste tilkoblingen du kan **kryptere**, med SMB3-kryptering (AES).
- **Andre apper og enheter (FTP)** - for filapper og avanserte brukere som snakker FTP.

For trinnvise tilkoblingsinstruksjoner for hver type, se [Koble til enhetene dine](/docs/guide/everdisk/everdisk-guide-connect).

## Slik kobler du til, og tilkoblingsadresser

Etter at du trykker Start, viser **Slik kobler du til**-seksjonen et kort for hver aktive server med den nøyaktige **adressen** du skal skrive inn på den andre enheten. Hver adresse er enkel å kopiere - trykk på den for å kopiere, bruk **Del**-knappen for å sende den, eller trykk på **info (ⓘ)**-knappen for detaljerte instruksjoner per protokoll.

- DLNA-kortet viser en enhetsbeskrivelsesadresse som slutter på `/device-desc.xml` for spillere som ber om en slik.
- Når enheten din er koblet til en Mac med kabel, dukker det opp en ekstra adresse med et **Kabeltilkobling**-merke som bruker enhetens `.local`-navn.

Du kan også åpne adressen som en **QR-kode**, slik at kameraet på en annen enhet kan hoppe rett til den.

## Hvem er tilkoblet

Seksjonen **Hvem er tilkoblet** viser i sanntid enhetene som er koblet til deg akkurat nå. Trykk på flere handlinger-knappen ved siden av en enhet for å **Blokkere denne enheten** hvis du ikke kjenner den igjen. Blokkerte enheter administreres i [Tilgang og personvern](/docs/guide/everdisk/everdisk-guide-access).

## Enhetsnavnet og avataren din

Hver enhet har et vennlig navn (som Speedy-Hare) og en farget avatar. Dette er navnet en TV, datamaskin eller annen app viser for enheten din på nettverket, slik at den er lett å kjenne igjen. Du kan generere navnet og avataren på nytt gratis, eller angi et egendefinert navn, ikon eller foto-avatar med Premium. Se [Innstillinger](/docs/guide/everdisk/everdisk-guide-settings).

## Deling over Wi-Fi eller en USB-kabel

Deling kan kjøre i to situasjoner:

- **Over Wi-Fi** - enheten din og de andre enhetene er på samme Wi-Fi-nettverk.
- **Over en USB-kabel** - enheten din er koblet til en **Mac** med en kabel, selv når det ikke finnes noe Wi-Fi i det hele tatt. Dette er raskere enn Wi-Fi og fungerer fortsatt på et fly, på et hotell eller på et låst nettverk.

Hvis verken Wi-Fi eller en kabel er tilgjengelig, er **Start**-knappen deaktivert, og et varsel om **Ingen Wi-Fi-tilkobling** vises. Hvis tilkoblingen faller ut mens deling pågår, stopper Everdisk delingen automatisk og gir deg beskjed. Trykk på info-knappen på et av disse varslene for en fullstendig forklaring.

## Hold appen åpen

Fordi din iPhone eller iPad fungerer som serveren, **fungerer deling bare mens Everdisk er åpen på skjermen**. Hvis du lukker appen eller låser enheten over lengre tid, kan systemet sette appen på pause, og delingen stopper.

For store overføringer:

- Hold Everdisk åpen og i forgrunnen.
- Koble enheten til strøm.
- Sett **Auto-lås** til **Aldri** i iOS-innstillingene mens du overfører.

Du kan slå på **Varsle før frakobling** (i Innstillinger → Deling), slik at Everdisk minner deg på å åpne appen igjen før systemet setter den på pause. Trykk på info-knappen på banneret **Hold appen åpen** for flere detaljer.

## Neste steg

- [Koble til enhetene dine](/docs/guide/everdisk/everdisk-guide-connect) - koble til en TV, datamaskin, nettleser, telefon eller USB-kabel.
- [Tilgang og personvern](/docs/guide/everdisk/everdisk-guide-access) - legg til et passord og kontroller redigering.
- [Innstillinger](/docs/guide/everdisk/everdisk-guide-settings) - slå servere av eller på og juster kvaliteten.
