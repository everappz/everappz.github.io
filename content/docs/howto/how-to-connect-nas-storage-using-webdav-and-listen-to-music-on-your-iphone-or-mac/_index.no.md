---
title: "Slik kobler du NAS-lagring via WebDAV og lytter til musikk på iPhone eller Mac"
date: 2024-07-28
description: "Lær hvordan du konfigurerer WebDAV på din Synology NAS og strømmer musikk til iPhone eller Mac med Evermusic eller Flacbox. Følg vår steg-for-steg-guide."
keywords: ["koble nas", "webdav synology", "strømme musikk nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["musikk", "strømming", "lagring", "nas", "koble", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Kort oppsummert:** Installer og aktiver WebDAV på din Synology NAS, konfigurer tillatelser for delt mappe, og koble deretter til fra Evermusic eller Flacbox med NAS IP-adressen og WebDAV-porten (standard 5005/5006). Du kan strømme og administrere hele musikkbiblioteket ditt uten å kopiere filer til enheten din.

Oppdag hvordan du kobler NAS-lagringen din via WebDAV og enkelt strømmer musikkbiblioteket ditt til iPhone eller Mac. WebDAV (Web-based Distributed Authoring and Versioning) er en protokoll som lar deg administrere og dele filer over internett. Ved å sette opp WebDAV på NAS-en din kan du få tilgang til og strømme musikksamlingen din, slik at du alltid har favorittlåtene dine innen rekkevidde.

I denne guiden viser vi deg hvordan du setter opp en WebDAV-tilkobling på en av de mest populære NAS-serverne, Synology NAS. Følg våre enkle trinn for å konfigurere WebDAV på din Synology NAS, og du kan bla gjennom, strømme og administrere musikkbiblioteket ditt direkte fra iPhone eller Mac.

## Trinn 1: Installer WebDAV på Synology NAS

1. Logg inn på Synology NAS og åpne **Pakkesenter**.
2. Søk etter "webdav" og installer WebDAV-pakken hvis den ikke allerede er installert. Åpne WebDAV-serveren for å konfigurere den.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Installer WebDAV på Synology" width="600" >}}

## Trinn 2: Konfigurer WebDAV-serveren

1. På WebDAV-innstillingssiden, kryss av boksene for **Aktiver HTTP**, **Aktiver HTTPS**, **Aktiver anonym WebDAV** og **Aktiver DavDepthInfinity**.
2. Klikk **Bruk** for å lagre endringene. Merk deg portnumrene for HTTP- og HTTPS-tilkoblinger, som er 5005 og 5006 som standard.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfigurer WebDAV-innstillinger" width="600" >}}

## Trinn 3: Konfigurer tillatelser for delt mappe

1. Åpne **Kontrollpanel** og gå til seksjonen **Delt mappe**.
2. Velg **Musikk**-mappen og klikk **Rediger**.
3. I fanen **Tillatelser**, konfigurer tillatelsene. Aktiver gjestetilgang med Skrivebeskyttet hvis du bare trenger å lytte til musikk, eller Lese/Skrive hvis du trenger å endre filer. Lagre endringene.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Tillatelser for delt mappe" width="600" >}}

## Trinn 4: Finn IP-adressen til Synology NAS

1. Åpne **Kontrollpanel** og gå til fanen **Nettverksgrensesnitt**, eller bruk nettleseren til å besøke [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Finn NAS IP-adresse" width="600" >}}

2. Noter IP-adressen til din Synology NAS (f.eks. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP-adresse" width="600" >}}

## Trinn 5: Koble til Synology NAS med Evermusic/Flacbox

1. Åpne Evermusic- eller Flacbox-appen og gå til fanen **Tilkoblinger**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Tilkoblinger-fanen i Evermusic" width="600" >}}

2. For automatisk tilkobling, finn din Synology NAS i seksjonen **Tilgjengelige enheter** og trykk for å koble til.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Liste over tilgjengelige enheter" width="600" >}}

3. For manuell tilkobling, velg **Koble til en skytjeneste** og velg **WebDAV**. Skriv inn serveradressen i formatet: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (f.eks. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Manuell WebDAV-konfigurasjon" width="600" >}}

4. La innlogging- og passordfeltene stå tomme for gjestetilgang, eller skriv inn Synology-legitimasjonen din. Trykk **Logg inn**.

## Trinn 6: Naviger og spill musikk

1. Når du er tilkoblet, vises enheten i listen **Tilkoblede tilbehør**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Tilkoblede enheter i Evermusic" width="600" >}}

2. Naviger til **Musikk**-mappen og trykk på en lydfil for å starte avspilling.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Bla gjennom musikkmappen" width="600" >}}

## Trinn 7: Legg til tilkoblet skymappe i musikkbiblioteket

1. Åpne seksjonen **Musikkbibliotek** i appen.
2. Velg **Legg til musikk** og velg **Tilkoblinger**.
3. Velg din tilkoblede NAS-server og velg **Musikk**-mappen. Trykk **Ferdig**.
4. Appen vil skanne musikkmappen og legge til støttede lydfiler i musikkbiblioteket. Metadata lastes inn, og sporene dine grupperes etter album, artist og sjanger.

## Konklusjon

Ved å følge disse trinnene kan du enkelt sette opp en WebDAV-tilkobling på din Synology NAS og strømme musikkbiblioteket ditt til iPhone eller Mac med Evermusic eller Flacbox. Nyt sømløs tilgang til favorittlåtene dine når som helst.

## Vanlige spørsmål

{{% details title="Hvilke NAS-enheter støtter WebDAV?" closed="true" %}}
De fleste populære NAS-merker støtter WebDAV, inkludert Synology, QNAP, TrueNAS og Western Digital. Sjekk dokumentasjonen til NAS-produsenten din for instruksjoner om WebDAV-oppsett.
{{% /details %}}

{{% details title="Hva er forskjellen mellom WebDAV og SMB for musikkstrømming fra NAS?" closed="true" %}}
WebDAV fungerer over HTTP/HTTPS og er bedre egnet for fjerntilgang over internett. SMB er vanligvis raskere på lokale nettverk. Evermusic og Flacbox støtter begge protokollene, så velg basert på om du trenger lokal eller ekstern tilgang.
{{% /details %}}

{{% details title="Trenger jeg brukernavn og passord for WebDAV på Synology?" closed="true" %}}
Nei, hvis du aktiverer anonym WebDAV-tilgang og konfigurerer gjestetillatelser på den delte mappen. For bedre sikkerhet kan du bruke Synology-legitimasjonen din i stedet.
{{% /details %}}

{{% details title="Kan jeg strømme FLAC og andre hi-res-formater fra NAS via WebDAV?" closed="true" %}}
Ja. Både Evermusic og Flacbox støtter FLAC, ALAC, WAV, DSD og andre høyoppløsningsformater ved strømming fra NAS-lagring via WebDAV.
{{% /details %}}

{{% details title="Hvorfor kan ikke appen finne NAS-en min i Tilgjengelige enheter?" closed="true" %}}
Sørg for at iPhone/Mac og NAS er på samme Wi-Fi-nettverk. Hvis automatisk oppdagelse ikke fungerer, bruk manuell tilkoblingsalternativet og skriv inn NAS IP-adressen og WebDAV-porten direkte.
{{% /details %}}
