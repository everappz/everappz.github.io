---
title: "Tilgang og personvern"
date: 2026-08-20
description: "Hold Everdisk-delingen din trygg: beskytt tilgang med brukernavn og passord, krypter SMB-tilkoblingen med SMB3 (AES), styr om tilkoblede enheter kan laste opp, gi nytt navn og slette med Filredigering, blokker ukjente enheter, velg papirkurv kontra permanent sletting, og forstå hvorfor alt blir værende på ditt lokale nettverk."
keywords: ["Everdisk passordbeskyttelse", "SMB-kryptering", "SMB3 AES-kryptering", "filredigering-bryter", "blokker enhet", "blokkerte enheter", "slett filer permanent", "kun lokalt nettverk", "privat fildeling", "DLNA uten passord", "nettverkssikkerhet"]
tags: ["everdisk", "veiledning", "tilgang", "personvern", "sikkerhet"]
readingTime: 8
---


Everdisk holder filene dine på ditt eget nettverk og gir deg enkle kontroller over hvem som kan nå dem og hva de kan gjøre. Du finner disse kontrollene i **Innstillinger → Deling → Tilgang**, i tillegg til noen relaterte innstillinger i Filbehandler.

## Beskytt tilgang med brukernavn og passord

Som standard kan hvem som helst på samme nettverk som har adressen din åpne de delte filene dine. For å kreve en innlogging:

1. Gå til **Innstillinger → Deling → Tilgang**.
2. Skriv inn et **Brukernavn** og et **Passord**.
3. Nå ber **Nettleser (HTTP)**-, **Datamaskin (WebDAV)**-, **Datamaskin (avansert) (SMB)**- og **Andre apper og enheter (FTP)**-tilkoblingene alle om disse detaljene før de viser filene dine.

La begge feltene stå tomme for åpen tilgang. Passordet ditt lagres trygt i enhetens nøkkelring.

> **DLNA er alltid åpen.** TV og mediesenter (DLNA)-tilkoblingen kan ikke passordbeskyttes, så når den er på, kan hvilken som helst enhet på samme Wi-Fi bla i de delte mediene dine. Slå den av hvis du bare vil ha beskyttede tilkoblinger, og del bare på nettverk du stoler på.

## Krypter SMB-tilkoblingen (SMB3 / AES)

Et brukernavn og passord styrer **hvem** som kan koble til, men selve dataene sendes fortsatt i klartekst på de fleste tilkoblinger. **SMB er den eneste tilkoblingen Everdisk kan kryptere**, noe som forvansker hver overføring slik at ingen andre på samme nettverk kan lese den.

For å slå det på:

1. Sett opp et **Brukernavn** og **Passord** som over - krypterte tilkoblinger kan ikke være anonyme.
2. Gå til **Innstillinger → Deling** og slå på **Krev SMB-kryptering**.
3. **Stopp og Start** deling på nytt slik at endringen trer i kraft.

Hver SMB-overføring beskyttes da med **SMB3-kryptering (AES)**. Enheten som kobler til må støtte SMB3 - Finder på en moderne Mac, eller **Windows 10 og nyere**. Dette er et godt valg på Wi-Fi du ikke helt stoler på. SMB-kryptering er en Premium-funksjon.

## Tillat eller blokker redigering (Filredigering)

**Filredigering**-bryteren styrer om tilkoblede enheter bare kan se på filene dine, eller også endre dem.

- **På** (standard): tilkoblede enheter kan **laste opp, gi nytt navn og slette** de delte filene dine - slik at enheten din fungerer som en ekte toveis nettverksdisk.
- **Av**: de delte filene dine er **skrivebeskyttet**. Andre kan se og laste ned, men kan ikke legge til eller endre noe.

Å slå den på viser en kort advarsel fordi den lar andre personer endre filene dine. Den har et **Viktig**-merke mens den er på.

## Blokker en enhet

Hvis du ser en enhet du ikke kjenner igjen:

1. På Deling-skjermen finner du den under **Hvem er tilkoblet**.
2. Trykk på flere handlinger-knappen dens og velg **Blokker denne enheten**.

Blokkerte enheter listes opp i **Innstillinger → Deling → Tilgang → Blokkerte enheter**, der du kan **oppheve blokkeringen** av én eller **Opphev blokkering av alle**. Blokkeringen følger enheten selv om nettverksadressen dens endres (for Nettleser-, Datamaskin- og TV-tilkoblingene).

## Papirkurv kontra permanent sletting

Når en fil slettes - av deg i filbehandleren, eller av en tilkoblet enhet - går den normalt til en gjenopprettbar **papirkurv** slik at du kan få den tilbake.

Hvis du foretrekker at filer fjernes umiddelbart uten mulighet for gjenoppretting, slå på **Slett filer permanent** i **Innstillinger → Filbehandler → Slette filer**. Dette er av som standard. **Det påvirker filbehandleren på enheten** og **sletting gjort over nettverket**; det endrer ikke hvordan systemets Bilder-bibliotek eller Musikk-bibliotek håndterer sletting.

## Alt blir værende lokalt

Everdisk deler bare over ditt **lokale nettverk** - ingenting lastes opp til internett, og det finnes ingen skykonto i midten. Noen få ting det er verdt å vite:

- Everdisk trenger iOS-tillatelsen **Lokalt nettverk** slik at enheter i nærheten kan finne den. Hvis den tillatelsen er av, forklarer et varsel hvordan du slår den på igjen i iOS-innstillingene.
- For størst personvern, del bare mens du er på et **hjemme- eller privat Wi-Fi**-nettverk du stoler på, og vær forsiktig på offentlig Wi-Fi. Brukernavn og passord hjelper, men det er ingen erstatning for et betrodd nettverk.
- Det **aller mest private alternativet er en USB-kabel til en Mac** - dataene går rett over kabelen og rører aldri ruteren eller internett. Se [Koble til enhetene dine](/docs/guide/everdisk/everdisk-guide-connect).

## Neste steg

- [Deling](/docs/guide/everdisk/everdisk-guide-sharing) - velg hva du vil dele og start deling.
- [Innstillinger](/docs/guide/everdisk/everdisk-guide-settings) - alle Tilgang- og Filbehandler-innstillinger samlet på ett sted.
