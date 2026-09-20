---
title: "Sådan opsætter du en WebDAV-server på iPhone og iPad til filadgang og deling"
description: "Gør din iPhone eller iPad til en WebDAV-server med Everdisk, og tilslut den som et netværksdrev i Mac Finder, Windows File Explorer, Linux, Android eller en anden iPhone over Wi-Fi. Fuld opsætning, WebDAV-adressen og porten samt trinvis forbindelse for hver enhed."
date: 2026-09-19
tags: ["everdisk", "webdav", "netværksdrev", "fildeling", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV-server iPhone", "WebDAV-server iPad", "sådan opsætter du WebDAV på iPhone", "tilslut iPhone som netværksdrev", "forbind iPhone WebDAV Mac Finder", "WebDAV Windows File Explorer iPhone", "iphone netværksdrev Windows", "WebDAV Linux iPhone", "få adgang til iPhone-filer fra computer", "webdav iphone til iphone", "del filer iPhone WebDAV", "tilslut netværksdrev iphone", "overfør filer iphone webdav", "webdav-adresse port iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV gør en mappe til et netværksdrev, som en computer kan åbne i sin normale filhåndtering. Det kører over den samme webprotokol, som din browser bruger, hvilket er grunden til, at det rejser godt på tværs af Mac, Windows og Linux uden særlige drivere. Med [Everdisk](/products/everdisk) kan du køre en WebDAV-server på din iPhone eller iPad, så telefonen dukker op som et drev, du kan gennemse, kopiere fra og kopiere til fra næsten enhver computer.

WebDAV er det bedste valg, når Windows er med i billedet, fordi Windows File Explorer forbinder til det rent. Denne vejledning dækker opsætningen, og hvordan du forbinder fra en Mac, Windows, Linux, Android og en anden iPhone.

## Det skal du bruge

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installeret.
- En computer eller en anden enhed på **det samme Wi-Fi-netværk**.
- De filer, du vil dele, i Everdisks Dokumenter-mappe eller i mapper, du tilføjer.

## Opsæt WebDAV-serveren i Everdisk

### Trin 1: Vælg, hvad der skal deles, og indstil adgang

Åbn Everdisk, gå til fanen **Deling**, og tryk på **Hvad skal deles**. Dokumenter-mappen deles som standard. Tilføj mere med **Tilføj mappe** og **Tilføj fil**.

Åbn **Indstillinger**, derefter **Deling**, derefter **Adgang**. Slå **Filredigering** til, hvis du vil have tilsluttede computere til at kopiere filer over på din telefon og omdøbe eller slette dem, eller slå den fra for et skrivebeskyttet drev. Indstil et **Login** og en **Adgangskode** her, hvis du vil have et login, eller lad dem stå tomme for gæsteadgang.

### Trin 2: Slå WebDAV-serveren til

Gå til **Indstillinger**, derefter **Deling**, derefter **Forbindelser**, og slå **Computer** til. Det er WebDAV-serveren (den bærer WebDAV-mærket).

### Trin 3: Start deling, og notér adressen

Vend tilbage til fanen **Deling**, og tryk på **Start**. Afsnittet **Sådan opretter du forbindelse** viser WebDAV-adressen. Den ser sådan ud:

```
http://192.168.1.20:8080
```

Tallet efter kolon er **porten**, som er **8080** som standard. Den første del er din iPhones adresse på Wi-Fi, så din vil være anderledes. Hold Everdisk åben på skærmen, mens en enhed er forbundet.

## Forbind fra en Mac

1. Åbn **Finder**, vælg **Gå**, derefter **Opret forbindelse til server** (eller tryk på **Command og K**).
2. Indtast den WebDAV-adresse, der vises i Everdisk, for eksempel `http://192.168.1.20:8080`.
3. Klik på **Opret forbindelse**, og vælg derefter **Gæst**, eller indtast dit **Login** og din **Adgangskode**.

Din iPhone åbnes i et Finder-vindue og opfører sig som en normal mappe. Kopier filer i begge retninger, hvis Filredigering er slået til.

## Forbind fra Windows

Windows har en indbygget WebDAV-klient, så dette virker fra File Explorer.

1. Åbn **File Explorer**, højreklik på **Denne pc** i sidebjælken, og vælg **Tilføj en netværksplacering** (du kan også bruge **Tilslut netværksdrev**).
2. Når du bliver bedt om adressen, skriver du den samme WebDAV-adresse fra Everdisk, for eksempel `http://192.168.1.20:8080`, og klikker derefter på **Næste**.
3. Indtast dit **Login** og din **Adgangskode**, hvis du har indstillet et.

Enheden vises derefter under Denne pc som en netværksplacering, du kan åbne og kopiere filer fra. Hvis Windows nægter at forbinde første gang, så sørg for, at tjenesten **WebClient** kører (søg efter Tjenester i Start-menuen, find WebClient, og indstil den til at starte), og prøv derefter igen.

## Forbind fra Linux

1. Åbn din filhåndtering, og vælg **Connect to Server** eller **Other Locations**.
2. Indtast adressen med et WebDAV-præfiks, for eksempel `dav://192.168.1.20:8080` (brug kun `davs://`, hvis du har opsat TLS).
3. Forbind som gæst, eller indtast dit login.

## Forbind fra Android

Android har ingen system-WebDAV-browser, så brug en filhåndtering, der understøtter det:

1. Installer en app såsom **Solid Explorer** eller **CX File Explorer**.
2. Tilføj en ny **WebDAV**-forbindelse.
3. Indtast værten og **port 8080**, vælg `http`-skemaet, og tilføj dit login, hvis du har indstillet et.

## Forbind fra en anden iPhone eller iPad

iOS Filer-appen indeholder ikke en WebDAV-klient, så brug en af disse:

- **Everdisks egen fane Enheder.** På den anden enhed åbner du Everdisk, går til **Enheder**, trykker på **Ny forbindelse**, vælger **WebDAV** og indtaster adressen, for eksempel `http://192.168.1.20:8080`. Dette er den enkleste vej og kræver intet ekstra.
- **En WebDAV-app** såsom Documents by Readdle, som kan tilføje en WebDAV-forbindelse med den samme adresse og det samme login.

## Foretrækker du et hurtigt link frem for et drev?

Hvis du kun har brug for at hente en fil hurtigt og slet ikke vil tilslutte et drev, så slå **Browser**-forbindelsen til i Indstillinger, Deling, Forbindelser. Everdisk giver dig så en webadresse, du kan åbne i enhver browser på enhver enhed for at gennemse og downloade dine filer. Det er den hurtigste måde at række en fil til en Windows-pc, en Chromebook eller en vens telefon.

## Skrivebeskyttet eller læse og skrive

Kontakten **Filredigering** i Indstillinger, Deling, Adgang afgør dette. Slået til betyder, at tilsluttede computere kan uploade, omdøbe og slette. Slået fra betyder, at drevet er skrivebeskyttet, så andre kan se og kopiere dine filer, men ikke ændre dem.

## Sådan bruger folk det i praksis

- **Kopier filer over på din iPhone fra en Windows-pc** ved at tilslutte den som en netværksplacering og trække dem over.
- **Flyt billeder og dokumenter over på en bærbar** med den filhåndtering, du allerede kender, uden kabel og uden iTunes.
- **Rediger et dokument på stedet** fra din Mac, ved at åbne det direkte fra telefonen og gemme det tilbage.
- **Flyt en mappe mellem en iPhone og en iPad** ved hjælp af Everdisks fane Enheder på den modtagende enhed.

## Et par tips

- Hold Everdisk åben, mens en enhed er forbundet. Hvis telefonen låses i lang tid, kan appen sættes på pause.
- På Windows starter du WebClient-tjenesten og prøver adressen igen, hvis forbindelsen fejler.
- WebDAV og SMB tilsluttes begge som netværksdrev. Brug WebDAV, når Windows er involveret, og [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), når du vil have Finder-hastighed og kryptering.
- For de hurtigste overførsler holder du billed- og videokvaliteten på Original i Indstillinger.

## Ofte stillede spørgsmål

{{% details title="Hvad er WebDAV-adressen og porten til min iPhone?" closed="true" %}}
Efter du starter deling, viser Everdisk adressen på Deling-skærmen. Den ser ud som http://192.168.1.20:8080. 8080 er den port, Everdisk bruger til WebDAV, og den første del er din iPhones adresse på Wi-Fi, så din vil være anderledes.
{{% /details %}}

{{% details title="Hvordan forbinder jeg til min iPhones WebDAV fra Windows?" closed="true" %}}
Åbn File Explorer, højreklik på Denne pc, og vælg Tilføj en netværksplacering eller Tilslut netværksdrev. Indtast WebDAV-adressen fra Everdisk, for eksempel http://192.168.1.20:8080, og indtast derefter dit login, hvis du har indstillet et. Hvis Windows ikke vil forbinde, så sørg for, at WebClient-tjenesten kører (søg efter Tjenester, find WebClient, start den), og prøv igen.
{{% /details %}}

{{% details title="Kan jeg bruge WebDAV mellem to iPhones?" closed="true" %}}
Ja, men iOS Filer-appen har ingen WebDAV-klient, så brug Everdisk på den anden enhed. Åbn fanen Enheder, tryk på Ny forbindelse, vælg WebDAV, og indtast den adresse, der vises på den første telefon. En WebDAV-app såsom Documents by Readdle virker også.
{{% /details %}}

{{% details title="Kræver WebDAV en adgangskode?" closed="true" %}}
Nej, et login er valgfrit. Lad Login og Adgangskode stå tomme i Indstillinger, Deling, Adgang for gæsteadgang, eller indstil dem, hvis du vil have forbindelser til at logge ind.
{{% /details %}}

{{% details title="Kan andre ændre mine filer over WebDAV?" closed="true" %}}
Kun hvis du tillader det. Kontakten Filredigering i Indstillinger, Deling, Adgang styrer dette. Slået til lader tilsluttede enheder uploade, omdøbe og slette. Slået fra gør drevet skrivebeskyttet, så andre kan se og kopiere, men ikke ændre noget.
{{% /details %}}

{{% details title="WebDAV eller SMB, hvad er forskellen?" closed="true" %}}
Begge tilslutter din iPhone som et netværksdrev. WebDAV kører over webprotokollen og forbinder rent fra Windows File Explorer, hvilket er dens største styrke. SMB er den indbyggede fildeling på Mac, Linux og NAS-enheder, er som regel hurtigere på en Mac og er den eneste Everdisk-forbindelse, der kan kryptere overførsler. Everdisk kan køre begge på én gang.
{{% /details %}}

{{% details title="Hvorfor bliver mit WebDAV-drev afbrudt?" closed="true" %}}
Din iPhone er serveren, og iOS sætter apps på pause, der ligger for længe i baggrunden. Hold Everdisk åben på skærmen, mens en enhed er forbundet, og sæt til strøm ved lange overførsler. Bekræft også, at begge enheder stadig er på det samme Wi-Fi.
{{% /details %}}

{{% details title="Kan jeg forbinde over WebDAV uden Wi-Fi?" closed="true" %}}
Ja, hvis du slutter din iPhone til en Mac med et kabel. Everdisk viser så en ekstra kabelforbindelsesadresse, som den tilsluttede Mac kan åbne i Finder, hvilket virker selv helt uden Wi-Fi. På kablet kan kun den Mac nå enheden.
{{% /details %}}

{{% details title="Er Everdisk gratis?" closed="true" %}}
Ja, Everdisk er gratis at downloade, og WebDAV-serveren er inkluderet. Et valgfrit engangskøb af Premium tilføjer ekstra funktioner som brugerdefinerede porte og billed- og videokonvertering. Du kan opsætte WebDAV og dele filer uden at betale.
{{% /details %}}

Klar til at prøve det? [Download Everdisk fra App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8), og tilslut din iPhone som et drev på et par minutter. Spørgsmål eller feedback? Skriv til os på **support@everappz.com**.
