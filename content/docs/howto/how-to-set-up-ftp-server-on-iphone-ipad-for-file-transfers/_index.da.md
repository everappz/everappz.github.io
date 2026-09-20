---
title: "Sådan opsætter du en FTP-server på iPhone og iPad til filoverførsler"
description: "Gør din iPhone eller iPad til en FTP-server med Everdisk, og overfør filer fra en Mac, en Windows-pc, Linux, Android, en FTP-app som FileZilla eller en anden iPhone over Wi-Fi. Fuld opsætning, ftp-adressen og porten, gæsteadgang og trinvis forbindelse for hver enhed."
date: 2026-09-19
tags: ["everdisk", "ftp", "filoverførsel", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP-server iPhone", "FTP-server iPad", "sådan opsætter du FTP på iPhone", "iphone ftp-serverapp", "forbind FileZilla til iPhone", "Cyberduck iPhone FTP", "overfør filer iPhone FTP", "ftp iphone til computer", "ftp iphone til iphone", "forbind til iPhone FTP fra Windows", "ftp-adresse port iphone", "anonym ftp iphone", "del filer iphone ftp", "iphone ftp til kamera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP er den gamle pålidelige inden for filoverførsel. Den har eksisteret i årtier, hvilket er præcis grunden til, at den er så nyttig: næsten alt, der kan tale med en server, forstår den. Kameraer, smart-TV, routere, netværksdrev, automatiseringsværktøjer og enhver desktop-FTP-app taler FTP. Med [Everdisk](/products/everdisk) kan du køre en FTP-server på din iPhone eller iPad, så telefonen bliver et sted, som de enheder og apps kan forbinde til og flytte filer.

Grib fat i FTP, når de andre muligheder ikke passer, for eksempel en ældre enhed eller en app, der kun ved, hvordan man forbinder over FTP. Denne vejledning dækker opsætningen, og hvordan du forbinder fra en Mac, Windows, en FTP-app, Linux, Android og en anden iPhone.

## Det skal du bruge

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installeret.
- En computer, app eller enhed på **det samme Wi-Fi-netværk**.
- De filer, du vil dele, i Everdisks Dokumenter-mappe eller i mapper, du tilføjer.

## Opsæt FTP-serveren i Everdisk

### Trin 1: Vælg, hvad der skal deles, og indstil adgang

Åbn Everdisk, gå til fanen **Deling**, og tryk på **Hvad skal deles**. Dokumenter-mappen deles som standard. Tilføj mere med **Tilføj mappe** og **Tilføj fil**.

Åbn **Indstillinger**, derefter **Deling**, derefter **Adgang**. Slå **Filredigering** til, hvis du vil have folk til at uploade, omdøbe og slette, eller slå den fra for kun at tillade downloads. Indstil et **Login** og en **Adgangskode**, hvis du vil have et login, eller lad dem stå tomme, så alle kan forbinde som gæst.

### Trin 2: Slå FTP-serveren til

Gå til **Indstillinger**, derefter **Deling**, derefter **Forbindelser**, og slå **Andre apps og enheder** til. Det er FTP-serveren (den bærer FTP-mærket).

### Trin 3: Start deling, og notér adressen

Vend tilbage til fanen **Deling**, og tryk på **Start**. Afsnittet **Sådan opretter du forbindelse** viser FTP-adressen. Den ser sådan ud:

```
ftp://192.168.1.20:2121
```

Tallet efter kolon er **porten**, som er **2121** som standard. Den første del er din iPhones adresse på Wi-Fi, så din vil være anderledes. Hold Everdisk åben på skærmen, mens en enhed er forbundet.

## Forbind fra en Mac

1. Åbn **Finder**, vælg **Gå**, derefter **Opret forbindelse til server** (eller tryk på **Command og K**).
2. Indtast den FTP-adresse, der vises i Everdisk, for eksempel `ftp://192.168.1.20:2121`.
3. Klik på **Opret forbindelse**, og vælg derefter **Gæst**, eller indtast dit **Login** og din **Adgangskode**.

Finder tilslutter FTP-delingen, så du kan gennemse og kopiere filer over på din Mac. Bemærk, at Finder åbner FTP som skrivebeskyttet. Når du vil uploade fra en Mac, så brug en FTP-app som beskrevet nedenfor.

## Forbind fra Windows

1. Åbn **File Explorer**, og klik på adresselinjen øverst.
2. Skriv FTP-adressen fra Everdisk, for eksempel `ftp://192.168.1.20:2121`, og tryk på **Enter**.
3. Indtast dit **Login** og din **Adgangskode**, hvis du har indstillet et, eller fortsæt som gæst.

De delte filer vises i vinduet, og du kan kopiere dem over på din pc.

## Forbind med en FTP-app (FileZilla, Cyberduck)

Til uploads og fuld kontrol er en FTP-app det bedste værktøj. **FileZilla** og **Cyberduck** er gratis og kører på Windows, Mac og Linux.

1. Åbn appen, og opret en ny forbindelse.
2. Sæt **Host** til din iPhones Wi-Fi-adresse, og **Port** til **2121**.
3. Til login indtaster du dit **Login** og din **Adgangskode**, eller vælger **Anonymous**, hvis du ikke har indstillet et.
4. Forbind, og træk filer i begge retninger (uploads kræver, at Filredigering er slået til).

## Forbind fra Linux

1. Åbn din filhåndtering, og vælg **Connect to Server** eller **Other Locations**.
2. Indtast adressen, for eksempel `ftp://192.168.1.20:2121`.
3. Forbind som gæst eller med dit login.

Du kan også bruge enhver Linux-FTP-klient fra terminalen og pege den mod den samme host og port 2121.

## Forbind fra Android

Android har ingen system-FTP-browser, så brug en app:

1. Installer en FTP-klient såsom **AndFTP**, **FTPCafe** eller en filhåndtering med FTP-understøttelse som **Solid Explorer**.
2. Tilføj en forbindelse med værten, **port 2121** og dit login eller Anonymous.
3. Gennemse og overfør.

## Forbind fra en anden iPhone eller iPad

iOS Filer-appen indeholder ikke en FTP-klient, så brug en af disse på den anden enhed:

- **Everdisks egen fane Enheder.** Åbn Everdisk, gå til **Enheder**, tryk på **Ny forbindelse**, vælg **FTP**, og indtast adressen, for eksempel `ftp://192.168.1.20:2121`. Dette er den enkleste vej.
- **En dedikeret FTP-app** til iOS med den samme host, port 2121 og login.

## Forbind andet udstyr: kameraer, TV, routere og NAS

Det er her, FTP skinner. Mange enheder har en indbygget FTP-klient, der kan sende eller hente filer:

- **Kameraer**, der uploader billeder over FTP, kan sende dem direkte til din iPhone.
- **Smart-TV, routere, NAS-bokse og automatiseringsværktøjer**, der understøtter FTP, kan forbinde på samme måde.

Peg dem mod din iPhones Wi-Fi-adresse, port **2121** og dit login (eller Anonymous), ved hjælp af den adresse, der vises i Everdisk.

## Skrivebeskyttet eller læse og skrive

Kontakten **Filredigering** i Indstillinger, Deling, Adgang styrer dette. Slået til lader folk uploade, omdøbe og slette. Slået fra betyder, at de kun kan downloade. Vælg skrivebeskyttet, når du rækker filer ud og ikke vil have noget ændret på din telefon.

## Sådan bruger folk det i praksis

- **Forbind FileZilla til din iPhone**, og skub en portion filer over på telefonen på én gang.
- **Lad en gammel app eller enhed, der kun taler FTP**, nå dine filer, når intet andet vil forbinde.
- **Modtag billeder fra et kamera**, der uploader over FTP.
- **Flyt filer mellem en iPhone og en iPad** ved hjælp af Everdisks fane Enheder på den modtagende enhed.

## Et par tips

- Hold Everdisk åben, mens en enhed er forbundet, da iOS sætter baggrundsapps på pause efter et stykke tid.
- For at uploade fra en Mac skal du bruge FileZilla eller Cyberduck frem for Finder, fordi Finder åbner FTP som skrivebeskyttet.
- Lad login stå tomt for den bredeste kompatibilitet, og forbind derefter som Anonymous, hvilket de fleste FTP-klienter tilbyder.
- FTP krypterer ikke sin trafik. På et netværk, du ikke har tillid til, bruger du i stedet [SMB-serveren med kryptering](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Ofte stillede spørgsmål

{{% details title="Hvad er FTP-adressen og porten til min iPhone?" closed="true" %}}
Efter du starter deling, viser Everdisk adressen på Deling-skærmen. Den ser ud som ftp://192.168.1.20:2121. 2121 er den port, Everdisk bruger til FTP, og den første del er din iPhones adresse på Wi-Fi, så din vil være anderledes.
{{% /details %}}

{{% details title="Hvordan forbinder jeg FileZilla eller Cyberduck til min iPhone?" closed="true" %}}
Åbn appen, og opret en ny forbindelse. Sæt Host til din iPhones Wi-Fi-adresse og Port til 2121. Indtast dit Login og din Adgangskode, eller vælg Anonymous, hvis du ikke har indstillet et i Everdisk. Forbind, og du kan trække filer i begge retninger, når Filredigering er slået til.
{{% /details %}}

{{% details title="Kan jeg forbinde til min iPhones FTP fra Windows?" closed="true" %}}
Ja. Åbn File Explorer, klik på adresselinjen, skriv FTP-adressen fra Everdisk (for eksempel ftp://192.168.1.20:2121), og tryk på Enter. Indtast dit login, hvis du har indstillet et, eller fortsæt som gæst. Til uploads og mere kontrol bruger du i stedet en FTP-app som FileZilla.
{{% /details %}}

{{% details title="Kræver FTP et login?" closed="true" %}}
Nej, et login er valgfrit. Lad Login og Adgangskode stå tomme i Indstillinger, Deling, Adgang, og forbind som Anonymous, hvilket de fleste FTP-klienter tilbyder. Indstil et login, hvis du vil have forbindelser til at logge ind først.
{{% /details %}}

{{% details title="Hvorfor kan jeg kun downloade og ikke uploade over FTP?" closed="true" %}}
To grunde er almindelige. For det første skal kontakten Filredigering i Indstillinger, Deling, Adgang være slået til for at tillade uploads, omdøbninger og sletninger. For det andet åbner Mac Finder FTP som skrivebeskyttet, så brug en FTP-app som FileZilla eller Cyberduck, når du vil uploade.
{{% /details %}}

{{% details title="Kan jeg bruge FTP mellem to iPhones?" closed="true" %}}
Ja. Start FTP-serveren på den første iPhone. På den anden åbner du Everdisk, går til fanen Enheder, trykker på Ny forbindelse, vælger FTP og indtaster den adresse, der vises på den første telefon. En dedikeret FTP-app til iOS virker også, da iOS Filer-appen ikke indeholder en FTP-klient.
{{% /details %}}

{{% details title="Er FTP sikkert?" closed="true" %}}
Almindelig FTP krypterer ikke sin trafik, så behandl det som et værktøj til netværk, du har tillid til, som dit hjemme-Wi-Fi. På et netværk, du ikke kontrollerer, bruger du SMB-serveren med Kræv SMB-kryptering slået til, hvilket beskytter hver overførsel.
{{% /details %}}

{{% details title="Hvilke enheder kan forbinde over FTP?" closed="true" %}}
Næsten alt med en FTP-klient. Det inkluderer Mac-, Windows- og Linux-computere, FTP-apps som FileZilla og Cyberduck, Android-filhåndteringer og hardware som kameraer, smart-TV, routere, NAS-bokse og automatiseringsværktøjer. Den brede rækkevidde er hovedgrunden til at vælge FTP.
{{% /details %}}

{{% details title="Hvorfor faldt min FTP-forbindelse?" closed="true" %}}
Din iPhone er serveren, og iOS sætter apps på pause, der ligger for længe i baggrunden. Hold Everdisk åben på skærmen, mens en enhed er forbundet, og sæt til strøm ved lange overførsler. Sørg også for, at begge enheder stadig er på det samme Wi-Fi.
{{% /details %}}

{{% details title="Er Everdisk gratis?" closed="true" %}}
Ja, Everdisk er gratis at downloade, og FTP-serveren er inkluderet. Et valgfrit engangskøb af Premium tilføjer ekstra funktioner som brugerdefinerede porte og billed- og videokonvertering. Du kan opsætte FTP og overføre filer uden at betale.
{{% /details %}}

Klar til at prøve det? [Download Everdisk fra App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8), og forbind din første FTP-klient på et par minutter. Spørgsmål eller feedback? Skriv til os på **support@everappz.com**.
