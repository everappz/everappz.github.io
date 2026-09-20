---
title: "Slik setter du opp en FTP-server på iPhone og iPad for filoverføringer"
description: "Gjør iPhone eller iPad om til en FTP-server med Everdisk og overfør filer fra en Mac, Windows-PC, Linux, Android, en FTP-app som FileZilla, eller en annen iPhone over Wi-Fi. Komplett oppsett, ftp-adressen og porten, gjestetilgang og steg-for-steg-tilkobling for hver enhet."
date: 2026-09-19
tags: ["everdisk", "ftp", "filoverføring", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP-server iPhone", "FTP-server iPad", "hvordan sette opp FTP på iPhone", "iphone ftp-serverapp", "koble FileZilla til iPhone", "Cyberduck iPhone FTP", "overfør filer iPhone FTP", "ftp iphone til datamaskin", "ftp iphone til iphone", "koble til iPhone FTP fra Windows", "ftp-adresse port iphone", "anonym ftp iphone", "del filer iphone ftp", "iphone ftp for kamera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP er den gamle pålitelige innen filoverføring. Den har vært rundt i flere tiår, og det er nettopp derfor den er så nyttig: nesten alt som kan snakke med en server, forstår den. Kameraer, smart-TV-er, rutere, nettverksdisker, automatiseringsverktøy og hver desktop-FTP-app snakker FTP. Med [Everdisk](/products/everdisk) kan du kjøre en FTP-server på iPhone eller iPad, slik at telefonen blir et sted disse enhetene og appene kan koble til og flytte filer.

Ty til FTP når de andre alternativene ikke passer, for eksempel en eldre enhet eller en app som bare kan koble til over FTP. Denne veiledningen dekker oppsettet og hvordan du kobler til fra en Mac, Windows, en FTP-app, Linux, Android og en annen iPhone.

## Hva du trenger

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installert.
- En datamaskin, app eller enhet på **samme Wi-Fi-nettverk**.
- Filene du vil dele, i Everdisks Dokumenter-mappe eller i mapper du legger til.

## Sett opp FTP-serveren i Everdisk

### Steg 1: Velg hva du vil dele og still inn tilgang

Åpne Everdisk, gå til **Deling**-fanen, og trykk **Hva du skal dele**. Dokumenter-mappen deles som standard. Legg til mer med **Legg til mappe** og **Legg til fil**.

Åpne **Innstillinger**, så **Deling**, så **Tilgang**. Slå på **Filredigering** hvis du vil at folk skal kunne laste opp, gi nytt navn og slette, eller av for å tillate bare nedlastinger. Sett en **Innlogging** og et **Passord** hvis du vil ha en pålogging, eller la dem stå tomme så hvem som helst kan koble til som gjest.

### Steg 2: Slå på FTP-serveren

Gå til **Innstillinger**, så **Deling**, så **Tilkoblinger**, og slå på **Andre apper og enheter**. Det er FTP-serveren (den bærer FTP-merket).

### Steg 3: Start delingen og noter adressen

Gå tilbake til **Deling**-fanen og trykk **Start**. **Slik kobler du til**-delen viser FTP-adressen. Den ser slik ut:

```
ftp://192.168.1.20:2121
```

Tallet etter kolonet er **porten**, som er **2121** som standard. Den første delen er iPhone-adressen din på Wi-Fi, så din vil være annerledes. Hold Everdisk åpen på skjermen mens en enhet er tilkoblet.

## Koble til fra en Mac

1. Åpne **Finder**, velg **Gå til**, så **Koble til tjener** (eller trykk **Command og K**).
2. Skriv inn FTP-adressen som vises i Everdisk, for eksempel `ftp://192.168.1.20:2121`.
3. Klikk **Koble til**, velg så **Gjest** eller tast inn **Innlogging** og **Passord**.

Finder monterer FTP-delingen slik at du kan bla i og kopiere filer til Mac-en. Merk at Finder åpner FTP som skrivebeskyttet. Når du vil laste opp fra en Mac, bruker du en FTP-app som beskrevet nedenfor.

## Koble til fra Windows

1. Åpne **Filutforsker** og klikk på adresselinjen øverst.
2. Skriv inn FTP-adressen fra Everdisk, for eksempel `ftp://192.168.1.20:2121`, og trykk **Enter**.
3. Tast inn **Innlogging** og **Passord** hvis du satte det, eller fortsett som gjest.

De delte filene vises i vinduet, og du kan kopiere dem til PC-en.

## Koble til med en FTP-app (FileZilla, Cyberduck)

For opplastinger og full kontroll er en FTP-app det beste verktøyet. **FileZilla** og **Cyberduck** er gratis og kjører på Windows, Mac og Linux.

1. Åpne appen og opprett en ny tilkobling.
2. Sett **Host** til iPhone-adressen din på Wi-Fi, og **Port** til **2121**.
3. For innloggingen taster du inn **Innlogging** og **Passord**, eller velger **Anonymous** hvis du ikke satte noen.
4. Koble til, og dra filer i begge retninger (opplastinger krever at Filredigering er på).

## Koble til fra Linux

1. Åpne filbehandleren din og velg **Connect to Server** eller **Other Locations**.
2. Skriv inn adressen, for eksempel `ftp://192.168.1.20:2121`.
3. Koble til som gjest eller med innloggingen din.

Du kan også bruke hvilken som helst Linux-FTP-klient fra terminalen, og peke den mot samme vert og port 2121.

## Koble til fra Android

Android har ingen FTP-blaerer i systemet, så bruk en app:

1. Installer en FTP-klient som **AndFTP**, **FTPCafe**, eller en filbehandler med FTP-støtte som **Solid Explorer**.
2. Legg til en tilkobling med verten, **port 2121**, og innloggingen din eller Anonymous.
3. Bla og overfør.

## Koble til fra en annen iPhone eller iPad

iOS Filer-appen inkluderer ingen FTP-klient, så bruk en av disse på den andre enheten:

- **Everdisks egen Enheter-fane.** Åpne Everdisk, gå til **Enheter**, trykk **Ny tilkobling**, velg **FTP**, og skriv inn adressen, for eksempel `ftp://192.168.1.20:2121`. Dette er den enkleste veien.
- **En dedikert FTP-app** for iOS, med samme vert, port 2121 og innlogging.

## Koble til annet utstyr: kameraer, TV-er, rutere og NAS

Det er her FTP skinner. Mange enheter har en innebygd FTP-klient som kan sende eller hente filer:

- **Kameraer** som laster opp bilder over FTP kan sende dem rett til iPhone.
- **Smart-TV-er, rutere, NAS-bokser og automatiseringsverktøy** som støtter FTP kan koble til på samme måte.

Rett dem mot iPhone-adressen din på Wi-Fi, port **2121**, og innloggingen din (eller Anonymous), med adressen som vises i Everdisk.

## Skrivebeskyttet eller lese og skrive

**Filredigering**-bryteren i Innstillinger, Deling, Tilgang styrer dette. På lar folk laste opp, gi nytt navn og slette. Av betyr at de bare kan laste ned. Velg skrivebeskyttet når du deler ut filer og ikke vil at noe skal endres på telefonen din.

## Måter folk bruker dette i hverdagen

- **Koble FileZilla til iPhone** og skyv en bunke filer over på telefonen i én omgang.
- **La en gammel app eller enhet som bare snakker FTP** nå filene dine når ingenting annet vil koble til.
- **Motta bilder fra et kamera** som laster opp over FTP.
- **Flytt filer mellom en iPhone og en iPad** med Everdisks Enheter-fane på den mottakende enheten.

## Noen tips

- Hold Everdisk åpen mens en enhet er tilkoblet, siden iOS setter bakgrunnsapper på pause etter en stund.
- For å laste opp fra en Mac, bruk FileZilla eller Cyberduck i stedet for Finder, fordi Finder åpner FTP som skrivebeskyttet.
- La innloggingen stå tom for den bredeste kompatibiliteten, og koble så til som Anonymous, noe de fleste FTP-klienter tilbyr.
- FTP krypterer ikke trafikken sin. På et nettverk du ikke stoler på, bruk [SMB-serveren med kryptering](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) i stedet.

## Ofte stilte spørsmål

{{% details title="Hva er FTP-adressen og porten for iPhone?" closed="true" %}}
Etter at du starter delingen, viser Everdisk adressen på Deling-skjermen. Den ser slik ut: ftp://192.168.1.20:2121. 2121 er porten Everdisk bruker for FTP, og den første delen er iPhone-adressen din på Wi-Fi, så din vil være annerledes.
{{% /details %}}

{{% details title="Hvordan kobler jeg FileZilla eller Cyberduck til iPhone?" closed="true" %}}
Åpne appen og opprett en ny tilkobling. Sett Host til iPhone-adressen din på Wi-Fi og Port til 2121. Tast inn Innlogging og Passord, eller velg Anonymous hvis du ikke satte noen i Everdisk. Koble til, og du kan dra filer i begge retninger når Filredigering er på.
{{% /details %}}

{{% details title="Kan jeg koble til iPhone FTP fra Windows?" closed="true" %}}
Ja. Åpne Filutforsker, klikk på adresselinjen, skriv inn FTP-adressen fra Everdisk (for eksempel ftp://192.168.1.20:2121), og trykk Enter. Tast inn innloggingen din hvis du satte en, eller fortsett som gjest. For opplastinger og mer kontroll, bruk en FTP-app som FileZilla i stedet.
{{% /details %}}

{{% details title="Trenger jeg en innlogging for FTP?" closed="true" %}}
Nei, en innlogging er valgfri. La Innlogging og Passord stå tomme i Innstillinger, Deling, Tilgang, og koble til som Anonymous, noe de fleste FTP-klienter tilbyr. Sett en innlogging hvis du vil at tilkoblinger skal logge inn først.
{{% /details %}}

{{% details title="Hvorfor kan jeg bare laste ned og ikke laste opp over FTP?" closed="true" %}}
To grunner er vanlige. For det første må Filredigering-bryteren i Innstillinger, Deling, Tilgang være på for å tillate opplastinger, navneendringer og slettinger. For det andre åpner Mac Finder FTP som skrivebeskyttet, så bruk en FTP-app som FileZilla eller Cyberduck når du vil laste opp.
{{% /details %}}

{{% details title="Kan jeg bruke FTP mellom to iPhoner?" closed="true" %}}
Ja. Start FTP-serveren på den første iPhone. På den andre åpner du Everdisk, går til Enheter-fanen, trykker Ny tilkobling, velger FTP, og skriver inn adressen som vises på den første telefonen. En dedikert FTP-app for iOS fungerer også, siden iOS Filer-appen ikke inkluderer en FTP-klient.
{{% /details %}}

{{% details title="Er FTP sikker?" closed="true" %}}
Vanlig FTP krypterer ikke trafikken sin, så behandle den som et verktøy for nettverk du stoler på, som hjemme-Wi-Fi. På et nettverk du ikke kontrollerer, bruk SMB-serveren med Krev SMB-kryptering slått på, som beskytter hver overføring.
{{% /details %}}

{{% details title="Hvilke enheter kan koble til over FTP?" closed="true" %}}
Nesten alt med en FTP-klient. Det inkluderer Mac-, Windows- og Linux-datamaskiner, FTP-apper som FileZilla og Cyberduck, Android-filbehandlere, og maskinvare som kameraer, smart-TV-er, rutere, NAS-bokser og automatiseringsverktøy. Den brede rekkevidden er hovedgrunnen til å velge FTP.
{{% /details %}}

{{% details title="Hvorfor falt FTP-tilkoblingen min ut?" closed="true" %}}
iPhone er serveren, og iOS setter apper som ligger i bakgrunnen for lenge på pause. Hold Everdisk åpen på skjermen mens en enhet er tilkoblet, og koble til strøm ved lange overføringer. Sørg også for at begge enhetene fortsatt er på samme Wi-Fi.
{{% /details %}}

{{% details title="Er Everdisk gratis?" closed="true" %}}
Ja, Everdisk er gratis å laste ned, og FTP-serveren er inkludert. Et valgfritt engangskjøp av Premium legger til ekstrafunksjoner som egendefinerte porter og konvertering av bilder og video. Du kan sette opp FTP og overføre filer uten å betale.
{{% /details %}}

Klar til å prøve? [Last ned Everdisk fra App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) og koble til din første FTP-klient på et par minutter. Spørsmål eller tilbakemeldinger? Send oss e-post på **support@everappz.com**.
