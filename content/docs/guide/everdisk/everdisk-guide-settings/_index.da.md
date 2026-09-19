---
title: "Indstillinger"
date: 2026-08-20
description: "En komplet rundvisning i Everdisks indstillinger: enhedsprofil (navn og avatar), de fem forbindelsesservere, adgangskontroller, SMB-kryptering (SMB3/AES), foto- og videokvalitet, brugerdefinerede porte, DLNA-miniaturer, netværks- og overførselsmuligheder, muligheder for filhåndtering og Premium."
keywords: ["Everdisk indstillinger", "enhedsnavn avatar", "forbindelsesservere", "foto- og videokvalitet", "brugerdefinerede porte HTTP WebDAV FTP", "DLNA-miniaturer", "parallelle overførsler", "slet filer permanent", "miniature-cache", "Everdisk Premium"]
tags: ["everdisk", "vejledning", "indstillinger"]
readingTime: 12
---


Fanen **Indstillinger** samler alt i tre hovedområder - **Deling**, **Netværk** og **Filhåndtering** - plus Premium, feedback og juridiske links. Denne side forklarer hver indstilling og dens standardværdi.

## Premium

Øverst i Indstillinger ser du din Premium-status eller en knap til at **Lås op for alle funktioner**. Everdisk er gratis at bruge med få begrænsninger; et engangskøb af **Premium Lifetime** fjerner dem. Se [Premium](#premium-lifetime) i slutningen af denne side.

## Deling-indstillinger

### Generelt

- **Start enhedsdeling automatisk** - start deling, så snart du åbner appen. *(Premium.)*
- **Del Dokumenter-mappen** - del appens egen mappe Dokumenter. Slået til som standard.
- **Giv besked før frakobling** - mind dig om at åbne appen igen, før systemet suspenderer den i baggrunden. Slået fra som standard; beder om tilladelse til notifikationer første gang.

### Enhedsprofil

- **Enhedsnavn** - det navn, andre enheder ser for dig på netværket. Tryk for at redigere. *(Premium.)*
- **Enhedsavatar** - ikonet og baggrundsfarven for din enhed. Du kan vælge et ikon, en baggrundsgradient eller **vælge en avatar fra Fotos**. *(Premium.)*
- **Generer navn og avatar på ny** og **Generer avatar på ny** - få et nyt tilfældigt navn og/eller en ny avatar. *(Gratis.)*

### Adgang

- **Login** og **Adgangskode** - kræv et login til forbindelserne Browser, Computer og Andre apps.
- **Redigering af filer** - lad forbundne enheder uploade, omdøbe og slette. Slået til som standard.
- **Blokerede enheder** - håndtér de enheder, du har blokeret.

Se [Adgang og privatliv](/docs/guide/everdisk/everdisk-guide-access) for detaljer.

### Forbindelser

Slå hver server til eller fra. Alle fem er slået til som standard, og hver har en info (ⓘ)-knap med forbindelsesanvisninger:

- **TV og Media Center** (DLNA)
- **Browser** (HTTP)
- **Computer** (WebDAV)
- **Computer (avanceret)** (SMB) - et netværksdrev til Mac, Windows og Linux; på en Mac dukker det op af sig selv i Finder-sidebjælken. Den eneste forbindelse, der kan krypteres.
- **Andre apps og enheder** (FTP)

### Fotos

- **Format** - Original eller Mest kompatibel (JPEG).
- **Kvalitet** - Original, Høj, Middel eller Lav.

Alt andet end Original konverterer fotos, når de deles, hvilket er langsommere. Konvertering er en Premium-funktion.

### Videoer

- **Format** - Original eller Mest kompatibel (H.264 MP4).
- **Kvalitet** - Original, Høj, Middel eller Lav.

Samme idé som ved Fotos: Original er hurtigst, og konvertering er Premium. Sænk kvaliteten, hvis et ældre TV ikke kan afspille en video.

### Avanceret

- **HTTP-port** (standard 80), **WebDAV-port** (standard 8080), **SMB-port** (standard 4455), **FTP-port** (standard 2121). DLNA vælger selv sin port. *(Ændring af porte er Premium; gratis brugere kan se værdierne.)*

### SMB-kryptering

- **Kræv SMB-kryptering** - kryptér hver SMB-overførsel med **SMB3-kryptering (AES)**, så ingen andre på netværket kan læse dine filer. Slået fra som standard. Det kræver et **login og en adgangskode** angivet ovenfor (krypterede forbindelser kan ikke være anonyme) og en klient, der understøtter SMB3, såsom Finder på en moderne Mac eller Windows 10 og nyere. Ændringer træder i kraft, næste gang du starter deling. *(Premium.)*

### DLNA-miniaturer

- **Vis miniaturer** - offentliggør billeder til forhåndsvisning for TV. Slået til som standard (gratis).
- Vælg hvilke størrelser der skal offentliggøres: **Lille (160px)**, **Middel (640px)**, **Stor (1024px)**, **Ekstra stor (4096px)**.

## Netværks-indstillinger

- **Filoverførsler** - brug kun **Wi-Fi** eller **Wi-Fi og mobildata** til downloads og uploads. Standard Wi-Fi.
- **Grænse for parallelle overførsler** - hvor mange overførsler der kører samtidig. Standard 5.
- **Baggrundsoverførsler** - hold overførsler kørende, mens du bruger andre skærme. Slået til som standard.
- **Miniaturer til filer** - om der skal hentes miniaturer til filer på andre enheder kun over Wi-Fi eller også over mobildata. Standard Wi-Fi.

## Filhåndterings-indstillinger

- **Slet filer permanent** - slet med det samme uden papirkurv. Slået fra som standard. Se [Adgang og privatliv](/docs/guide/everdisk/everdisk-guide-access).
- **Nulstil alle beskeder** - hent de tip-bannere tilbage, du har lukket.
- **Miniature-cache** - se hvor meget plads cachelagrede miniaturer bruger, og **Ryd miniature-cache**.

## Feedback og juridisk

I bunden kan du **Bedøm denne app**, **Send feedback**, **Få flere apps** og åbne **Vilkår og betingelser** samt **Privatlivspolitik**.

## Premium Lifetime

Everdisk er gratis at bruge. Et enkelt køb af **Premium Lifetime** - en engangsbetaling, ikke et abonnement - låser op for:

- **Ubegrænsede mapper** - del mere end 5 mapper.
- **Ubegrænsede forbindelser** - gem mere end 10 servere på fanen Enheder.
- **Konvertering af fotos og video** - del i en hvilken som helst kvalitet ud over Original.
- **SMB-kryptering** - beskyt SMB-overførsler med SMB3-kryptering (AES).
- **Brugerdefinerede porte** - angiv dine egne HTTP-, WebDAV-, SMB- og FTP-porte.
- **Automatisk start af deling** - start deling automatisk, når du åbner appen.
- **Tilpasning af enhed** - et brugerdefineret enhedsnavn, avatarikon, baggrundsgradient eller en fotoavatar.

Premium er knyttet til dit Apple ID. Brug **Gendan køb** for at låse op for det på dine andre enheder, der er logget ind med det samme Apple ID.

## Næste skridt

- [Deling](/docs/guide/everdisk/everdisk-guide-sharing) - Deling-skærmen i detaljer.
- [Adgang og privatliv](/docs/guide/everdisk/everdisk-guide-access) - adgangskoder, redigering og blokering.
- [FAQ](/docs/faq/everdisk) - hurtige svar på almindelige spørgsmål.
