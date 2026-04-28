---
title: "Sådan tilslutter du NAS-lagring via WebDAV og lytter til musik på din iPhone eller Mac"
date: 2024-07-28
description: "Lær hvordan du konfigurerer WebDAV på din Synology NAS og streamer musik til din iPhone eller Mac med Evermusic eller Flacbox. Følg vores trin-for-trin guide."
keywords: ["tilslut nas", "webdav synology", "stream musik nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["musik", "streaming", "lagring", "nas", "tilslut", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Kort sagt:** Installer og aktiver WebDAV på din Synology NAS, konfigurer tilladelser for delte mapper, og forbind derefter fra Evermusic eller Flacbox ved hjælp af NAS IP-adressen og WebDAV-porten (standard 5005/5006). Du kan streame og administrere hele dit musikbibliotek uden at kopiere filer til din enhed.

Opdag hvordan du tilslutter dit NAS-lagring via WebDAV og ubesværet streamer dit musikbibliotek til din iPhone eller Mac. WebDAV (Web-based Distributed Authoring and Versioning) er en protokol, der giver dig mulighed for at administrere og dele filer over internettet. Ved at opsætte WebDAV på din NAS kan du få adgang til og streame din musiksamling, så du altid har dine yndlingsnumre lige ved hånden.

I denne guide viser vi dig, hvordan du opsætter en WebDAV-forbindelse på en af de mest populære NAS-servere, Synology NAS. Følg vores enkle trin for at konfigurere WebDAV på din Synology NAS, og du vil kunne gennemse, streame og administrere dit musikbibliotek direkte fra din iPhone eller Mac.

## Trin 1: Installer WebDAV på Synology NAS

1. Log ind på din Synology NAS og åbn **Pakkecenter**.
2. Søg efter "webdav" og installer WebDAV-pakken, hvis den ikke allerede er installeret. Åbn WebDAV-serveren for at konfigurere den.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Installer WebDAV på Synology" width="600" >}}

## Trin 2: Konfigurer WebDAV-serveren

1. På WebDAV-indstillingssiden skal du markere boksene for **Aktiver HTTP**, **Aktiver HTTPS**, **Aktiver anonym WebDAV** og **Aktiver DavDepthInfinity**.
2. Klik på **Anvend** for at gemme ændringerne. Bemærk portnumrene for HTTP- og HTTPS-forbindelser, som er 5005 og 5006 som standard.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfigurer WebDAV-indstillinger" width="600" >}}

## Trin 3: Konfigurer tilladelser for delt mappe

1. Åbn **Kontrolpanel** og gå til sektionen **Delt mappe**.
2. Vælg mappen **Musik** og klik på **Rediger**.
3. Under fanen **Tilladelser** konfigurer tilladelserne. Aktiver gæsteadgang med skrivebeskyttet, hvis du kun har brug for at lytte til musik, eller læse/skrive, hvis du har brug for at ændre filer. Gem ændringerne.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Tilladelser for delt mappe" width="600" >}}

## Trin 4: Find IP-adressen på Synology NAS

1. Åbn **Kontrolpanel** og gå til fanen **Netværksinterface**, eller brug din webbrowser til at besøge [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Find NAS IP-adresse" width="600" >}}

2. Notér IP-adressen på din Synology NAS (f.eks. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP-adresse" width="600" >}}

## Trin 5: Forbind til Synology NAS med Evermusic/Flacbox

1. Åbn Evermusic eller Flacbox appen og gå til fanen **Forbindelser**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Fanen Forbindelser i Evermusic" width="600" >}}

2. For automatisk forbindelse, find din Synology NAS i sektionen **Tilgængelige enheder** og tryk på den for at forbinde.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Liste over tilgængelige enheder" width="600" >}}

3. For manuel forbindelse, vælg **Forbind en cloudtjeneste** og vælg **WebDAV**. Indtast serveradressen i formatet: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (f.eks. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Manuel WebDAV-konfiguration" width="600" >}}

4. Lad login- og adgangskodefelterne stå tomme for gæsteadgang, eller indtast dine Synology-loginoplysninger. Tryk på **Log ind**.

## Trin 6: Navigér og afspil musik

1. Når forbindelsen er oprettet, vises enheden på listen **Forbundne tilbehør**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Forbundne enheder i Evermusic" width="600" >}}

2. Navigér til mappen **Musik** og tryk på en lydfil for at starte afspilning.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Gennemse musikmappen" width="600" >}}

## Trin 7: Tilføj forbundet cloudmappe til musikbiblioteket

1. Åbn sektionen **Musikbibliotek** i appen.
2. Vælg **Tilføj musik** og vælg **Forbindelser**.
3. Vælg din forbundne NAS-server og vælg mappen **Musik**. Tryk på **Færdig**.
4. Appen vil scanne musikmappen og tilføje understøttede lydfiler til musikbiblioteket. Metadata vil blive indlæst, og dine numre vil blive grupperet efter album, kunstner og genre.

## Konklusion

Ved at følge disse trin kan du nemt opsætte en WebDAV-forbindelse på din Synology NAS og streame dit musikbibliotek til din iPhone eller Mac med Evermusic eller Flacbox. Nyd problemfri adgang til dine yndlingsnumre når som helst.

## FAQ

{{% details title="Hvilke NAS-enheder understøtter WebDAV?" closed="true" %}}
De fleste populære NAS-mærker understøtter WebDAV, herunder Synology, QNAP, TrueNAS og Western Digital. Tjek din NAS-producents dokumentation for instruktioner til opsætning af WebDAV.
{{% /details %}}

{{% details title="Hvad er forskellen mellem WebDAV og SMB til musikstreaming fra NAS?" closed="true" %}}
WebDAV fungerer over HTTP/HTTPS og er bedre egnet til fjernadgang over internettet. SMB er typisk hurtigere på lokale netværk. Evermusic og Flacbox understøtter begge protokoller, så vælg baseret på om du har brug for lokal eller fjern adgang.
{{% /details %}}

{{% details title="Har jeg brug for et brugernavn og en adgangskode til WebDAV på Synology?" closed="true" %}}
Nej, hvis du aktiverer anonym WebDAV-adgang og konfigurerer gæstetilladelser på din delte mappe. For bedre sikkerhed kan du bruge dine Synology-loginoplysninger i stedet.
{{% /details %}}

{{% details title="Kan jeg streame FLAC og andre hi-res formater fra NAS via WebDAV?" closed="true" %}}
Ja. Både Evermusic og Flacbox understøtter FLAC, ALAC, WAV, DSD og andre højopløsningsformater ved streaming fra NAS-lagring via WebDAV.
{{% /details %}}

{{% details title="Hvorfor kan appen ikke finde min NAS i Tilgængelige enheder?" closed="true" %}}
Sørg for, at din iPhone/Mac og NAS er på det samme Wi-Fi-netværk. Hvis automatisk opdagelse ikke virker, brug den manuelle forbindelsesmulighed og indtast NAS IP-adressen og WebDAV-porten direkte.
{{% /details %}}
