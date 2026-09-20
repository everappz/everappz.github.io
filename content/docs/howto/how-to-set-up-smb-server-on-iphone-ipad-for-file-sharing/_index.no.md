---
title: "Slik setter du opp en SMB-server på iPhone og iPad for fildeling"
description: "Gjør iPhone eller iPad om til en SMB-filserver med Everdisk og åpne den som en nettverksdisk fra en Mac, en annen iPhone, Linux eller Android over Wi-Fi. Komplett oppsett, smb-adressen og porten, valgfri SMB3-kryptering og steg-for-steg-tilkobling for hver enhet."
date: 2026-09-19
tags: ["everdisk", "smb", "fildeling", "nettverksdisk", "iphone", "ipad", "mac", "finder", "kryptering", "wifi"]
keywords: ["SMB-server iPhone", "SMB-server iPad", "hvordan sette opp SMB på iPhone", "iPhone SMB-deling", "koble iPhone SMB Mac Finder", "smb iphone til iphone", "iOS Filer-app koble til server SMB", "del filer iPhone SMB", "iphone nettverksdisk Finder", "SMB3-kryptering iOS", "smb-deling iPhone Android", "koble til SMB fra Linux", "iphone som nettverksdisk", "del filer mellom iphoner wifi", "tilordne iphone som nettverksdisk"]
readingTime: 10
---

{{< author-byline >}}

SMB er fildelingen som er innebygd i macOS, Windows og Linux, og i nesten hver nettverksdisk (NAS). Når du kobler til en delt mappe på en annen datamaskin og den åpnes som en vanlig disk i Finder eller Filutforsker, er det SMB som gjør jobben. Med [Everdisk](/products/everdisk) kan du legge en SMB-deling på iPhone eller iPad, slik at telefonen selv dukker opp som en nettverksdisk andre enheter kan bla i, kopiere fra og kopiere til.

Dette er alternativet du bør ty til når du vil at iPhone skal oppføre seg som en ordentlig disk, ikke en nettside. Den er rask, den drar og slipper begge veier, og den er den eneste tilkoblingstypen i Everdisk som kan kryptere hver overføring. Denne veiledningen dekker oppsettet og hvordan du kobler til fra en Mac, en annen iPhone eller iPad, Linux, Android og Windows.

## Hva du trenger

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installert.
- En annen enhet på **samme Wi-Fi-nettverk**.
- Filene du vil dele, i Everdisks Dokumenter-mappe eller i mapper du legger til.

## Sett opp SMB-serveren i Everdisk

### Steg 1: Velg hva du vil dele og hvem som kan skrive

Åpne Everdisk, gå til **Deling**-fanen, og trykk **Hva du skal dele**. Dokumenter-mappen deles som standard. Legg til mer med **Legg til mappe** og **Legg til fil**, og slå på bilde- eller musikkbiblioteket ditt hvis du vil ha dem tilgjengelige også.

Bestem om andre enheter bare kan lese filene dine, eller også endre dem. Åpne **Innstillinger**, så **Deling**, så **Tilgang**, og still inn **Filredigering**. Med den på kan tilkoblede enheter kopiere filer til telefonen din og gi nytt navn eller slette dem. Med den av er delingen skrivebeskyttet.

Hvis du vil ha en innlogging, still inn en **Innlogging** og et **Passord** på den samme Tilgang-skjermen. La begge stå tomme for å tillate gjestetilgang.

### Steg 2: Slå på SMB-serveren

Gå til **Innstillinger**, så **Deling**, så **Tilkoblinger**, og slå på **Datamaskin (avansert)**. Det er SMB-serveren (den bærer SMB-merket).

### Steg 3: Start delingen og noter adressen

Gå tilbake til **Deling**-fanen og trykk **Start**. **Slik kobler du til**-delen viser nå SMB-adressen. Den ser slik ut:

```
smb://192.168.1.20:4455/Share
```

Tre ting du bør vite om den adressen:

- Tallet etter kolonet er **porten**. Everdisk bruker **4455** som standard.
- Delingen heter **Share**.
- Den første delen er iPhone-adressen din på Wi-Fi, så den vil være annerledes på ditt nettverk.

Hold Everdisk åpen mens enheter er tilkoblet, for iOS setter apper som ligger i bakgrunnen for lenge på pause.

## Koble til fra en Mac

Dette er det jevneste tilfellet, fordi macOS snakker SMB innfødt.

Den raskeste veien: åpne **Finder** og se i sidefeltet under **Steder** eller **Nettverk**. Everdisk gjør seg synlig på Wi-Fi, så iPhone dukker ofte opp der av seg selv. Klikk på den, klikk så **Koble til som** og velg **Gjest**, eller tast inn innloggingen din.

For å koble til manuelt:

1. I Finder velger du **Gå til**, så **Koble til tjener** (eller trykker **Command og K**).
2. Skriv inn SMB-adressen som vises i Everdisk, for eksempel `smb://192.168.1.20:4455/Share`.
3. Klikk **Koble til**, velg så **Gjest** eller tast inn **Innlogging** og **Passord**.

iPhone åpnes i et Finder-vindu. Kopier filer inn eller ut ved å dra, akkurat som en hvilken som helst annen disk (hvis Filredigering er på).

## Koble til fra en annen iPhone eller iPad

iOS og iPadOS kan åpne SMB-delinger i den innebygde **Filer**-appen, noe som gjør overføringer fra telefon til telefon rene og raske.

På den andre enheten:

1. Åpne **Filer**-appen.
2. Trykk på **mer**-knappen (de tre prikkene, øverst til høyre på iPhone) og velg **Koble til tjener**.
3. Skriv inn SMB-adressen fra Everdisk, for eksempel `smb://192.168.1.20:4455/Share`.
4. Velg **Gjest**, eller **Registrert bruker** og tast inn innloggingen din.
5. Delingen vises under Steder i Filer. Bla og kopier i begge retninger.

Du kan også bruke Everdisks egen **Enheter**-fane på den andre enheten, som inkluderer en SMB-klient. Åpne Everdisk, gå til **Enheter**, trykk **Ny tilkobling**, velg **SMB**, og skriv inn adressen.

## Koble til fra Linux

1. Åpne filbehandleren din (Files/Nautilus på GNOME, Dolphin på KDE).
2. Velg **Other Locations** eller **Connect to Server**.
3. Skriv inn adressen, for eksempel `smb://192.168.1.20:4455/Share`.
4. Koble til som gjest, eller tast inn innloggingen din.

Fra en terminal kan du også kjøre `smbclient //192.168.1.20/Share -p 4455` og taste inn innloggingen din når du blir bedt om det.

## Koble til fra Android

Android har ingen SMB-blaerer i systemet, så bruk en filbehandler som støtter SMB:

1. Installer en app som **CX File Explorer**, **Solid Explorer** eller **X-plore File Manager**.
2. Legg til en ny **SMB**- eller **LAN**-tilkobling.
3. Skriv inn verten (iPhone-adressen din på Wi-Fi), sett **porten til 4455**, og delingsnavnet **Share**.
4. Koble til som gjest eller med innloggingen din, og bla og kopier så.

## Koble til fra Windows

Windows kan lese SMB-delinger, med én hake det er verdt å kjenne til på forhånd. Den innebygde Filutforsker snakker bare med SMB på standardporten og lar deg ikke skrive inn en egendefinert port i banen, og Everdisk bruker port 4455. Så den vanlige **Tilordne nettverksstasjon**-veien når ofte ikke frem til den.

Du har to gode alternativer på Windows:

- Bruk en filbehandler eller SMB-klient som lar deg sette en egendefinert port, og rett den mot iPhone-adressen din med port **4455** og delingsnavnet **Share**.
- Eller koble til fra Windows med en av Everdisks andre servere i stedet. Både [WebDAV-oppsettet](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) og [FTP-oppsettet](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) fungerer godt fra Windows Filutforsker, og nettleserlenken fungerer i hvilken som helst nettleser.

Hvis du likevel vil prøve Tilordne nettverksstasjon: åpne **Filutforsker**, høyreklikk **Denne PC-en**, velg **Tilordne nettverksstasjon**, og skriv inn verten og delingsnavnet som vises i Everdisk. Hvis den ikke kan koble til, er det portbegrensningen over, så bytt til WebDAV eller FTP.

## Slå på kryptering for uklarert Wi-Fi

SMB er den eneste Everdisk-tilkoblingen som kan kryptere hver overføring, noe som betyr noe på Wi-Fi du ikke har full kontroll over, som en kafé eller et kontornettverk.

1. I **Innstillinger**, **Deling**, **Tilgang** setter du en **Innlogging** og et **Passord**. Krypterte tilkoblinger kan ikke være anonyme, så dette steget er påkrevd.
2. I **Innstillinger**, **Deling** slår du på **Krev SMB-kryptering**.
3. Stopp og start delingen på nytt slik at endringen trer i kraft.

Hver SMB-overføring er da beskyttet med **SMB3-kryptering (AES)**. Enheten som kobler til, må støtte SMB3, noe Finder på en moderne Mac og Windows 10 eller nyere begge gjør. SMB-kryptering er en del av engangskjøpet av Premium.

## Skrivebeskyttet eller lese og skrive

**Filredigering**-bryteren i Innstillinger, Deling, Tilgang styrer dette for hver server, inkludert SMB. Slå den på, så kan tilkoblede enheter laste opp, gi nytt navn og slette. Slå den av, så kan de bare bla i og kopiere filer av telefonen din. Velg skrivebeskyttet når du overleverer filer til noen du ikke vil skal endre noe.

## Måter folk bruker dette i hverdagen

- **Flytt en stor mappe over på iPhone fra en Mac** ved å dra den inn i Finder-vinduet, raskere enn en nettopplasting.
- **Hent en dag med bilder og videoer av telefonen** over på en bærbar uten iTunes eller kabel.
- **Send filer mellom to iPhoner** gjennom Filer-appen, uten en tredje app på noen av sidene.
- **Jobb med en fil på plass**, ved å åpne et dokument rett fra telefonen i en app på Mac-en og lagre det tilbake.

## Noen tips

- Hold Everdisk åpen mens en enhet er tilkoblet. Å låse telefonen lenge kan sette appen på pause og bryte tilkoblingen.
- Hvis en Mac ikke ser telefonen i Finder-sidefeltet, kobler du til manuelt med Koble til tjener og hele smb-adressen.
- For best hastighet på store overføringer holder du bilde- og videokvaliteten på Original i Innstillinger.
- På et uklarert nettverk slår du på Krev SMB-kryptering og slår av de andre serverne mens du jobber.

## Ofte stilte spørsmål

{{% details title="Hva er SMB-adressen og porten for iPhone?" closed="true" %}}
Etter at du starter delingen, viser Everdisk adressen på Deling-skjermen. Den ser slik ut: smb://192.168.1.20:4455/Share. 4455 er porten Everdisk bruker for SMB, og Share er navnet på den delte mappen. Den første delen er iPhone-adressen din på Wi-Fi, så din vil være annerledes.
{{% /details %}}

{{% details title="Kan jeg koble til iPhone SMB-delingen fra Windows?" closed="true" %}}
Windows Filutforsker kobler bare til SMB på standardporten og godtar ikke en egendefinert port i banen, mens Everdisk bruker port 4455. Så den vanlige Tilordne nettverksstasjon-veien når ofte ikke frem. Bruk en filbehandler som lar deg sette en egendefinert port, eller koble til fra Windows med WebDAV, FTP eller nettleserlenken i stedet. Alle disse fungerer fra Windows uten portproblemer.
{{% /details %}}

{{% details title="Hvordan deler jeg filer mellom to iPhoner med SMB?" closed="true" %}}
Start SMB-serveren på den første iPhone i Everdisk. På den andre iPhone åpner du Filer-appen, trykker på mer-knappen, velger Koble til tjener, og skriver inn smb-adressen som vises i Everdisk (for eksempel smb://192.168.1.20:4455/Share). Koble til som Gjest eller med innloggingen din, og delingen vises i Filer. Du kan også bruke Everdisks egen Enheter-fane på den andre telefonen.
{{% /details %}}

{{% details title="Dukker iPhone opp i Mac Finder-sidefeltet automatisk?" closed="true" %}}
Vanligvis ja. Everdisk gjør SMB-delingen synlig på Wi-Fi, så iPhone dukker ofte opp under Steder eller Nettverk i Finder-sidefeltet. Klikk på den og velg Koble til som, så Gjest eller innloggingen din. Hvis den ikke dukker opp, kobler du til manuelt med Gå til, Koble til tjener og hele smb-adressen.
{{% /details %}}

{{% details title="Trenger jeg et passord for å bruke SMB?" closed="true" %}}
Nei, en innlogging er valgfri. La Innlogging og Passord stå tomme i Innstillinger, Deling, Tilgang for å tillate gjestetilgang. Sett dem hvis du vil at tilkoblinger skal logge inn. En innlogging og et passord er bare påkrevd hvis du slår på Krev SMB-kryptering, fordi krypterte tilkoblinger ikke kan være anonyme.
{{% /details %}}

{{% details title="Er SMB-tilkoblingen kryptert?" closed="true" %}}
Den kan være det. SMB er den eneste Everdisk-tilkoblingen som støtter kryptering. Sett en innlogging og et passord, slå så på Krev SMB-kryptering i Innstillinger, Deling. Hver overføring er da beskyttet med SMB3 (AES). Den andre enheten må støtte SMB3, noe moderne Mac-er og Windows 10 eller nyere gjør. Kryptering er en Premium-funksjon.
{{% /details %}}

{{% details title="Kan folk endre eller slette filene mine over SMB?" closed="true" %}}
Bare hvis du tillater det. Filredigering-bryteren i Innstillinger, Deling, Tilgang styrer dette. Med den på kan tilkoblede enheter laste opp, gi nytt navn og slette. Med den av er delingen skrivebeskyttet, og andre kan bla i og kopiere filer av telefonen din, men ikke endre noe.
{{% /details %}}

{{% details title="Hvorfor falt SMB-tilkoblingen min ut?" closed="true" %}}
iPhone er serveren, og iOS setter apper som ligger i bakgrunnen for lenge på pause. Hold Everdisk åpen på skjermen mens en enhet er tilkoblet, og koble telefonen til strøm under lange overføringer. Sørg også for at begge enhetene ble værende på samme Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV eller FTP, hvilken bør jeg bruke?" closed="true" %}}
Bruk SMB når du vil at telefonen skal oppføre seg som en ekte nettverksdisk på en Mac, en annen iPhone, Linux eller en NAS, og når du vil ha kryptering. Bruk WebDAV når du vil ha en nettverksdisk som også fungerer godt fra Windows. Bruk FTP for den bredeste kompatibiliteten med eldre enheter og apper. Everdisk kan kjøre alle samtidig, så du er ikke låst til én.
{{% /details %}}

{{% details title="Er Everdisk gratis?" closed="true" %}}
Ja, Everdisk er gratis å laste ned, og SMB-serveren er inkludert. Det valgfrie engangskjøpet av Premium legger til SMB-kryptering, egendefinerte porter og noen andre ekstrafunksjoner. Du kan sette opp SMB og dele filer uten å betale.
{{% /details %}}

Klar til å prøve? [Last ned Everdisk fra App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) og åpne iPhone i Finder på omtrent et minutt. Spørsmål eller tilbakemeldinger? Send oss e-post på **support@everappz.com**.
