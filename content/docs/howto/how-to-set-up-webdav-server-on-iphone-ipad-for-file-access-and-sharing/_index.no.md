---
title: "Slik setter du opp en WebDAV-server på iPhone og iPad for filtilgang og deling"
description: "Gjør iPhone eller iPad om til en WebDAV-server med Everdisk og monter den som en nettverksdisk i Mac Finder, Windows Filutforsker, Linux, Android eller en annen iPhone over Wi-Fi. Komplett oppsett, WebDAV-adressen og porten, og steg-for-steg-tilkobling for hver enhet."
date: 2026-09-19
tags: ["everdisk", "webdav", "nettverksdisk", "fildeling", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV-server iPhone", "WebDAV-server iPad", "hvordan sette opp WebDAV på iPhone", "monter iPhone som nettverksdisk", "koble iPhone WebDAV Mac Finder", "WebDAV Windows Filutforsker iPhone", "iphone nettverksdisk Windows", "WebDAV Linux iPhone", "få tilgang til iPhone-filer fra datamaskin", "webdav iphone til iphone", "del filer iPhone WebDAV", "tilordne nettverksstasjon iphone", "overfør filer iphone webdav", "webdav-adresse port iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV gjør en mappe om til en nettverksdisk som en datamaskin kan åpne i sin vanlige filbehandler. Den kjører over den samme webprotokollen som nettleseren din bruker, og det er derfor den reiser godt på tvers av Mac, Windows og Linux uten spesielle drivere. Med [Everdisk](/products/everdisk) kan du kjøre en WebDAV-server på iPhone eller iPad, slik at telefonen dukker opp som en disk du kan bla i, kopiere fra og kopiere til fra nesten hvilken som helst datamaskin.

WebDAV er det beste valget når Windows er med i bildet, fordi Windows Filutforsker kobler til den rent. Denne veiledningen dekker oppsettet og hvordan du kobler til fra en Mac, Windows, Linux, Android og en annen iPhone.

## Hva du trenger

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installert.
- En datamaskin eller en annen enhet på **samme Wi-Fi-nettverk**.
- Filene du vil dele, i Everdisks Dokumenter-mappe eller i mapper du legger til.

## Sett opp WebDAV-serveren i Everdisk

### Steg 1: Velg hva du vil dele og still inn tilgang

Åpne Everdisk, gå til **Deling**-fanen, og trykk **Hva du skal dele**. Dokumenter-mappen deles som standard. Legg til mer med **Legg til mappe** og **Legg til fil**.

Åpne **Innstillinger**, så **Deling**, så **Tilgang**. Slå på **Filredigering** hvis du vil at tilkoblede datamaskiner skal kunne kopiere filer til telefonen din og gi nytt navn eller slette dem, eller av for en skrivebeskyttet disk. Sett en **Innlogging** og et **Passord** her hvis du vil ha en pålogging, eller la dem stå tomme for gjestetilgang.

### Steg 2: Slå på WebDAV-serveren

Gå til **Innstillinger**, så **Deling**, så **Tilkoblinger**, og slå på **Datamaskin**. Det er WebDAV-serveren (den bærer WebDAV-merket).

### Steg 3: Start delingen og noter adressen

Gå tilbake til **Deling**-fanen og trykk **Start**. **Slik kobler du til**-delen viser WebDAV-adressen. Den ser slik ut:

```
http://192.168.1.20:8080
```

Tallet etter kolonet er **porten**, som er **8080** som standard. Den første delen er iPhone-adressen din på Wi-Fi, så din vil være annerledes. Hold Everdisk åpen på skjermen mens en enhet er tilkoblet.

## Koble til fra en Mac

1. Åpne **Finder**, velg **Gå til**, så **Koble til tjener** (eller trykk **Command og K**).
2. Skriv inn WebDAV-adressen som vises i Everdisk, for eksempel `http://192.168.1.20:8080`.
3. Klikk **Koble til**, velg så **Gjest** eller tast inn **Innlogging** og **Passord**.

iPhone åpnes i et Finder-vindu og oppfører seg som en vanlig mappe. Kopier filer i begge retninger hvis Filredigering er på.

## Koble til fra Windows

Windows har en innebygd WebDAV-klient, så dette fungerer fra Filutforsker.

1. Åpne **Filutforsker**, høyreklikk **Denne PC-en** i sidefeltet, og velg **Legg til en nettverksplassering** (du kan også bruke **Tilordne nettverksstasjon**).
2. Når du blir bedt om adressen, skriver du inn den samme WebDAV-adressen fra Everdisk, for eksempel `http://192.168.1.20:8080`, og klikker så **Neste**.
3. Tast inn **Innlogging** og **Passord** hvis du satte det.

Enheten vises da under Denne PC-en som en nettverksplassering du kan åpne og kopiere filer fra. Hvis Windows nekter å koble til første gang, sørg for at **WebClient**-tjenesten kjører (søk etter Tjenester i Start-menyen, finn WebClient og sett den til å starte), og prøv så igjen.

## Koble til fra Linux

1. Åpne filbehandleren din og velg **Connect to Server** eller **Other Locations**.
2. Skriv inn adressen med et WebDAV-prefiks, for eksempel `dav://192.168.1.20:8080` (bruk `davs://` bare hvis du satte opp TLS).
3. Koble til som gjest eller tast inn innloggingen din.

## Koble til fra Android

Android har ingen WebDAV-blaerer i systemet, så bruk en filbehandler som støtter det:

1. Installer en app som **Solid Explorer** eller **CX File Explorer**.
2. Legg til en ny **WebDAV**-tilkobling.
3. Skriv inn verten og **port 8080**, velg `http`-skjemaet, og legg til innloggingen din hvis du satte en.

## Koble til fra en annen iPhone eller iPad

iOS Filer-appen inkluderer ingen WebDAV-klient, så bruk en av disse:

- **Everdisks egen Enheter-fane.** På den andre enheten åpner du Everdisk, går til **Enheter**, trykker **Ny tilkobling**, velger **WebDAV**, og skriver inn adressen, for eksempel `http://192.168.1.20:8080`. Dette er den enkleste veien og trenger ingenting ekstra.
- **En WebDAV-app** som Documents by Readdle, som kan legge til en WebDAV-tilkobling med samme adresse og innlogging.

## Foretrekker du en rask lenke fremfor en disk?

Hvis du bare trenger å hente en fil raskt og ikke vil montere en disk i det hele tatt, slår du på **Nettleser**-tilkoblingen i Innstillinger, Deling, Tilkoblinger. Everdisk gir deg da en nettadresse du kan åpne i hvilken som helst nettleser på hvilken som helst enhet for å bla i og laste ned filene dine. Det er den raskeste måten å overlevere en fil til en Windows-PC, en Chromebook eller en venns telefon.

## Skrivebeskyttet eller lese og skrive

**Filredigering**-bryteren i Innstillinger, Deling, Tilgang bestemmer dette. På betyr at tilkoblede datamaskiner kan laste opp, gi nytt navn og slette. Av betyr at disken er skrivebeskyttet, så andre kan se og kopiere filene dine, men ikke endre dem.

## Måter folk bruker dette i hverdagen

- **Kopier filer over på iPhone fra en Windows-PC** ved å tilordne den som en nettverksplassering og dra dem over.
- **Last av bilder og dokumenter til en bærbar** med filbehandleren du allerede kjenner, uten kabel og uten iTunes.
- **Rediger et dokument på plass** fra Mac-en, ved å åpne det rett fra telefonen og lagre tilbake.
- **Flytt en mappe mellom en iPhone og en iPad** med Everdisks Enheter-fane på den mottakende enheten.

## Noen tips

- Hold Everdisk åpen mens en enhet er tilkoblet. Å låse telefonen lenge kan sette appen på pause.
- På Windows, hvis tilkoblingen mislykkes, start WebClient-tjenesten og prøv adressen igjen.
- WebDAV og SMB monteres begge som nettverksdisker. Bruk WebDAV når Windows er involvert, og [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) når du vil ha Finder-hastighet og kryptering.
- For raskest overføringer holder du bilde- og videokvaliteten på Original i Innstillinger.

## Ofte stilte spørsmål

{{% details title="Hva er WebDAV-adressen og porten for iPhone?" closed="true" %}}
Etter at du starter delingen, viser Everdisk adressen på Deling-skjermen. Den ser slik ut: http://192.168.1.20:8080. 8080 er porten Everdisk bruker for WebDAV, og den første delen er iPhone-adressen din på Wi-Fi, så din vil være annerledes.
{{% /details %}}

{{% details title="Hvordan kobler jeg til iPhone WebDAV fra Windows?" closed="true" %}}
Åpne Filutforsker, høyreklikk Denne PC-en, og velg Legg til en nettverksplassering eller Tilordne nettverksstasjon. Skriv inn WebDAV-adressen fra Everdisk, for eksempel http://192.168.1.20:8080, og tast så inn innloggingen din hvis du satte en. Hvis Windows ikke vil koble til, sørg for at WebClient-tjenesten kjører (søk etter Tjenester, finn WebClient, start den) og prøv igjen.
{{% /details %}}

{{% details title="Kan jeg bruke WebDAV mellom to iPhoner?" closed="true" %}}
Ja, men iOS Filer-appen har ingen WebDAV-klient, så bruk Everdisk på den andre enheten. Åpne Enheter-fanen, trykk Ny tilkobling, velg WebDAV, og skriv inn adressen som vises på den første telefonen. En WebDAV-app som Documents by Readdle fungerer også.
{{% /details %}}

{{% details title="Trenger WebDAV et passord?" closed="true" %}}
Nei, en innlogging er valgfri. La Innlogging og Passord stå tomme i Innstillinger, Deling, Tilgang for gjestetilgang, eller sett dem hvis du vil at tilkoblinger skal logge inn.
{{% /details %}}

{{% details title="Kan andre endre filene mine over WebDAV?" closed="true" %}}
Bare hvis du tillater det. Filredigering-bryteren i Innstillinger, Deling, Tilgang styrer dette. På lar tilkoblede enheter laste opp, gi nytt navn og slette. Av gjør disken skrivebeskyttet, så andre kan se og kopiere, men ikke endre noe.
{{% /details %}}

{{% details title="WebDAV eller SMB, hva er forskjellen?" closed="true" %}}
Begge monterer iPhone som en nettverksdisk. WebDAV kjører over webprotokollen og kobler rent til fra Windows Filutforsker, noe som er dens viktigste styrke. SMB er den innfødte fildelingen på Mac-, Linux- og NAS-enheter, er som regel raskere på en Mac, og er den eneste Everdisk-tilkoblingen som kan kryptere overføringer. Everdisk kan kjøre begge samtidig.
{{% /details %}}

{{% details title="Hvorfor kobler WebDAV-disken min fra?" closed="true" %}}
iPhone er serveren, og iOS setter apper som ligger i bakgrunnen for lenge på pause. Hold Everdisk åpen på skjermen mens en enhet er tilkoblet, og koble til strøm ved lange overføringer. Bekreft også at begge enhetene fortsatt er på samme Wi-Fi.
{{% /details %}}

{{% details title="Kan jeg koble til over WebDAV uten Wi-Fi?" closed="true" %}}
Ja, hvis du kobler iPhone til en Mac med en kabel. Everdisk viser da en ekstra kabeltilkoblingsadresse som den tilkoblede Mac-en kan åpne i Finder, som fungerer selv helt uten Wi-Fi. På kabelen er det bare den Mac-en som kan nå enheten.
{{% /details %}}

{{% details title="Er Everdisk gratis?" closed="true" %}}
Ja, Everdisk er gratis å laste ned, og WebDAV-serveren er inkludert. Et valgfritt engangskjøp av Premium legger til ekstrafunksjoner som egendefinerte porter og konvertering av bilder og video. Du kan sette opp WebDAV og dele filer uten å betale.
{{% /details %}}

Klar til å prøve? [Last ned Everdisk fra App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) og monter iPhone som en disk på et par minutter. Spørsmål eller tilbakemeldinger? Send oss e-post på **support@everappz.com**.
