---
title: "Forbind dine enheder"
date: 2026-08-20
description: "Trinvise anvisninger til at oprette forbindelse til dit trådløse Everdisk-drev: se indhold på et smart-TV via DLNA, åbn dine filer i enhver webbrowser, monter din enhed som et netværksdrev i Finder, Windows eller Linux via WebDAV eller SMB (med valgfri SMB3/AES-kryptering), forbind filapps via FTP, og overfør over et USB-kabel til en Mac uden Wi-Fi."
keywords: ["opret forbindelse til Everdisk", "stream til TV DLNA", "åbn filer i browser", "monter netværksdrev Finder", "WebDAV Windows Linux", "FTP-filapp", "USB-kabeloverførsel Mac", "forbind iPhone til computer", "netværksdrev iPhone"]
tags: ["everdisk", "vejledning", "forbind"]
readingTime: 11
---


Når du har trykket på **Start** på [Deling](/docs/guide/everdisk/everdisk-guide-sharing)-skærmen, kan andre enheder oprette forbindelse til dine filer på fem forskellige måder. Vælg den metode, der passer til den enhed, du vil bruge. I alle tilfælde vises den præcise **adresse**, du skal bruge, i afsnittet **Sådan opretter du forbindelse** på Deling-skærmen.

> Begge enheder skal være på det **samme Wi-Fi-netværk** - eller, for en Mac, forbundet med et **USB-kabel** (se det sidste afsnit).

## Se indhold på et TV (DLNA)

Brug denne metode til at vise fotos, videoer og musik på et smart-TV eller en medieafspiller.

1. Under **Indstillinger → Deling → Forbindelser** skal du sikre dig, at **TV og Media Center** er slået til (det er slået til som standard).
2. På Deling-skærmen skal du trykke på **Start**.
3. På dit TV åbner du dets indbyggede medieafspiller eller medieserver-app (den kan hedde Media Player, SmartShare, AllShare eller lignende).
4. Din enhed vises på listen over medieservere med sit navn (for eksempel "Speedy-Hare"). Vælg den.
5. Gennemse dine delte fotos, videoer og din musik, og begynd at afspille. Miniaturer til forhåndsvisning dukker op automatisk.

Bemærkninger:

- DLNA kan ikke beskyttes med adgangskode, så denne forbindelse er åben for alle på det samme Wi-Fi, mens den er slået til.
- Hvis en video ikke vil afspille på et ældre TV, kan du sænke videokvaliteten under **Indstillinger → Deling → Videoer**, så Everdisk konverterer den til et mere kompatibelt format.

## Åbn i en webbrowser (HTTP)

Brug denne metode til at give filer til alle med en webbrowser - der er ingen app at installere.

1. Under **Indstillinger → Deling → Forbindelser** skal du sikre dig, at **Browser** er slået til.
2. Tryk på **Start**.
3. På Deling-skærmen kopierer du **Browser**-adressen (eller viser dens QR-kode).
4. På den anden telefon, tablet eller computer åbner du en hvilken som helst webbrowser (Safari, Chrome, Edge, Firefox) og indtaster adressen.
5. Siden åbner med dine delte filer.

I browseren kan den anden person:

- Skifte mellem **liste**- og **gittervisning** og sortere efter navn, dato eller størrelse.
- Se rigtige **miniaturer** til fotos, videoer, PDF-filer og musikillustrationer.
- Åbne et foto i et **galleri** i fuld skærm med swipe, knib-for-at-zoome og et diasshow.
- Afspille musik i en indbygget **afspiller** med kø, blanding og gentagelse.
- **Downloade** en hvilken som helst fil eller downloade en hel mappe (eller flere valgte elementer) som en enkelt **Archive.zip**.
- **Uploade** filer tilbage til din enhed - kun hvis du har slået **Redigering af filer** til (se [Adgang og privatliv](/docs/guide/everdisk/everdisk-guide-access)).

## Brug den som et netværksdrev (WebDAV)

Brug denne metode til at få din enhed til at vises som en almindelig disk på en Mac, Windows-PC eller Linux-maskine, så du kan trække filer begge veje.

**På en Mac (Finder)**

1. Under **Indstillinger → Deling → Forbindelser** skal du sikre dig, at **Computer** er slået til.
2. Tryk på **Start**, og notér **Computer (WebDAV)**-adressen.
3. I Finder vælger du **Gå → Opret forbindelse til server** (eller tryk på **⌘K**).
4. Indtast WebDAV-adressen præcis som vist, og klik på **Opret forbindelse**.
5. Indtast login og adgangskode, hvis du har angivet dem, ellers opret forbindelse som gæst.
6. Din enhed åbner ligesom et hvilket som helst andet netværksdrev. Træk filer ind eller ud.

**På Windows**

1. Åbn **Stifinder**, højreklik på **Denne pc**, og vælg **Tilføj en netværksplacering** (eller tilknyt et netværksdrev).
2. Indtast den WebDAV-adresse, der vises i Everdisk.
3. Indtast login og adgangskode, hvis du har angivet dem.

**På Linux**

1. Åbn din filhåndtering og vælg **Opret forbindelse til server** (eller brug `davs://` / `dav://`).
2. Indtast den WebDAV-adresse, der vises i Everdisk.

Om forbindelsen er skrivebeskyttet eller går begge veje, afhænger af indstillingen **Redigering af filer**. Når den er slået til, kan du kopiere filer over på din enhed og omdøbe eller slette dem; når den er slået fra, er drevet skrivebeskyttet.

## Forbind over SMB (krypteret netværksdrev)

SMB er et netværksdrev til Mac, Windows og Linux, bygget på den fildeling, der allerede findes i disse systemer, så din enhed dukker op som et helt almindeligt netværksdrev - og det er den eneste forbindelse, du kan kryptere.

1. Under **Indstillinger → Deling → Forbindelser** skal du sikre dig, at **Computer (avanceret)** (SMB-forbindelsen) er slået til.
2. Tryk på **Start**, og notér **SMB**-adressen, der ser sådan ud: `smb://192.168.1.20:4455/Share`.
3. Forbind fra din computer:
   - **Mac:** din enhed dukker op af sig selv i **Finder-sidebjælken** under **Placeringer** (Netværk) - klik blot på den og log ind. For at forbinde manuelt i stedet vælger du **Gå → Opret forbindelse til server** (**⌘K**) og indtaster adressen.
   - **Windows:** åbn **Stifinder**, højreklik på **Denne pc** og vælg **Tilslut netværksdrev**, og indtast derefter `\\<address>\Share` med værten og sharenavnet fra Deling-skærmen (eller skriv `smb://`-adressen i adresselinjen).
   - **Linux:** vælg **Opret forbindelse til server** i din filhåndtering og indtast adressen.
4. Indtast login og adgangskode, hvis du har angivet dem, ellers opret forbindelse som gæst.
5. Sharet hedder **Share**. Med **Redigering af filer** slået til kan du kopiere filer begge veje; med den slået fra er det skrivebeskyttet.

**Slå kryptering til (anbefales på Wi-Fi, du ikke stoler på)**

SMB er den eneste Everdisk-forbindelse, der kan krypteres. Sådan beskytter du hver overførsel med **SMB3-kryptering (AES)**:

1. Under **Indstillinger → Deling → Adgang** sætter du et **Login** og en **Adgangskode** - krypterede forbindelser kan ikke være anonyme.
2. Under **Indstillinger → Deling** slår du **Kræv SMB-kryptering** til.
3. **Stop og Start** deling igen, så ændringen træder i kraft.

Din klient skal understøtte SMB3 - Finder på en moderne Mac eller **Windows 10 og nyere**. SMB-kryptering er en Premium-funktion.

## Forbind en filapp (FTP)

Brug denne metode til filhåndterings- og overførselsapps, der taler FTP (for eksempel FileZilla eller Cyberduck på en computer).

1. Under **Indstillinger → Deling → Forbindelser** skal du sikre dig, at **Andre apps og enheder** er slået til.
2. Tryk på **Start**, og notér **FTP**-adressen.
3. I din FTP-app tilføjer du en ny forbindelse med den adresse.
4. Indtast login og adgangskode, hvis du har angivet dem, eller lad dem stå tomme for anonym adgang.

## Overfør over et USB-kabel (Mac, ingen Wi-Fi nødvendig)

Brug denne metode, når der ikke er noget Wi-Fi, eller når du vil have den hurtigste og mest private overførsel. Den virker kun med en **Mac**.

1. Tilslut din iPhone eller iPad til Mac'en med det almindelige opladerkabel.
2. Hvis du bliver spurgt på enheden, skal du trykke på **Stol på denne computer**.
3. I Everdisk trykker du på **Start**. En note om **Hurtig forbindelse tilgængelig** dukker op, og Deling-skærmen viser en ekstra adresse med et **Kabelforbindelse**-mærke, der ender på `.local`.
4. På Mac'en åbner du Finder → **Gå → Opret forbindelse til server** (**⌘K**) og indtaster den `.local`-adresse (den virker til både Browser- og Computer-forbindelserne).
5. Din enhed åbner over kablet - hurtigere end Wi-Fi, og dataene rører aldrig routeren eller internettet.

Bemærkninger:

- Brug **`.local`-navnet**, ikke en IP-adresse (IP-adresser virker kun over Wi-Fi), og aldrig `localhost`.
- Kabelvejen er **kun til Mac**. Windows-PC'er og Android-enheder skal bruge Wi-Fi.
- Du kan også trække filer ind i Everdisk-mappen med Finder på en Mac eller med appen Apple-enheder (eller iTunes) på Windows via standard fildeling i iOS.

## Næste skridt

- [Adgang og privatliv](/docs/guide/everdisk/everdisk-guide-access) - tilføj en adgangskode, tillad uploads, bloker en enhed.
- [Fotos, musik og video](/docs/guide/everdisk/everdisk-guide-media) - del hele dit bibliotek, og indstil kvaliteten.
- [Opret forbindelse til servere](/docs/guide/everdisk/everdisk-guide-devices) - nå andre enheder fra Everdisk.
