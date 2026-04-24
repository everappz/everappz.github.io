---
title: "Stream je muziek van Mac of PC naar iPhone met SMB"
description: "Leer hoe je je muziekcollectie kunt streamen van Mac of Windows PC naar je iPhone of iPad met Evermusic en het SMB-protocol. Een eenvoudige stapsgewijze handleiding om te verbinden en te genieten van audio zonder synchronisatie."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["muziek streamen van Mac naar iPhone", "SMB audio streaming iOS", "Evermusic SMB instellen", "PC muziek verbinden iPhone", "Mac muziek delen iOS", "SMB Windows bestanden streamen", "Evermusic PC map toegang"]
---

{{< author-byline >}}


**Samenvatting:** Gebruik de Evermusic-app voor iPhone of iPad om muziek te streamen van je Mac of Windows PC via je lokale netwerk met SMB. Geen synchronisatie, geen kopiëren -- schakel gewoon bestandsdeling in op je computer, maak verbinding in de app en speel af. De installatie duurt minder dan 5 minuten.

Verdrink je in een zee van muziek op je MAC of PC en wil je er probleemloos van genieten op je iPhone of iPad? Zoek niet verder dan Evermusic. Met Evermusic is het ongelooflijk eenvoudig om je computer te verbinden via het SMB-protocol en je favoriete nummers te streamen zonder je zorgen te maken over extra opslagruimte of synchronisatieproblemen. Hier is een stapsgewijze handleiding om te beginnen:

## Stap 1: Schakel het SMB-protocol in op je computer

![Evermusic - SMB-ondersteuning - Mac deelscherm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Als je MAC gebruikt

- Open Systeemvoorkeuren -> Delen.
- Schakel de service Bestandsdeling in.
- Voeg in het gedeelte "Gedeelde mappen" je muziekmap toe, selecteer een gebruiker en stel de machtigingsniveaus in (Lezen en schrijven of Alleen lezen).
- Voor extra gemak kun je "Iedereen: Alleen lezen" selecteren voor de muziekmap, waardoor deze gemakkelijk toegankelijk is in Evermusic.
- Vergeet niet de URL van je computer (smb://192.168.xx.xx) te onthouden voor de volgende stappen.

![Evermusic - SMB-ondersteuning - Bestandsdelingscherm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Tik op "Opties" en schakel "Bestanden en mappen delen via SMB" in.
- Schakel "Windows Bestandsdeling" in voor beschikbare accounts.

![Evermusic - SMB-ondersteuning - Bestanden en mappen delen scherm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Als je een Windows PC gebruikt

![Evermusic - SMB-ondersteuning - Bestanden delen op Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Klik met de rechtermuisknop op je muziekmap.
- Selecteer "Eigenschappen."
- Open het tabblad "Delen."
- Klik op "Delen..."
- Kies de mensen met wie je wilt delen en stel hun machtigingsniveaus in.
- Net als bij MAC kun je kiezen voor "Iedereen: Lezen" voor de geselecteerde muziekmap.
- Klik op "Voltooid" om je instellingen op te slaan.

![Evermusic - SMB-ondersteuning - Gedeelde map op Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Stap 2: Voeg je computer automatisch toe

- Open nu Evermusic en ga naar het tabblad "Verbindingen" ("Netwerk" als je een oudere versie van de app gebruikt).
- Als je je computer ziet in het gedeelte "Beschikbare apparaten" ("Beschikbare shares" als je een oudere versie van de app gebruikt) en je hebt "Iedereen: Alleen lezen" geselecteerd in de vorige stap, tik dan gewoon op je computer en deze maakt automatisch verbinding.
- Als dit niet gebeurt, kun je je computer handmatig toevoegen.

![Evermusic - SMB-ondersteuning - Account verbinden scherm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Stap 3: Voeg je computer handmatig toe

- Tik op "Verbind een cloudservice" ("Account toevoegen" als je een oudere versie van de app gebruikt)
- Selecteer "SMB" uit de lijst met beschikbare servers op het volgende scherm.
- Op het "SMB" instellingenscherm:
  - Voer de server-URL in met het pad naar de gedeelde map. Je kunt de servernaam of het server-IP invoeren. Bijvoorbeeld:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Voer je gebruikersnaam en wachtwoord in of laat deze velden leeg als je "Iedereen: Alleen lezen" hebt geselecteerd in de vorige stap.
  - Het veld "WORKGROUP" is optioneel en moet worden gebruikt als je een Active Directory-domein hebt.

![Evermusic - SMB-ondersteuning - Inloggegevens invoeren scherm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Zodra je je SMB-account hebt verbonden, verschijnt het in het gedeelte "Cloudservices" ("Accounts"). Open het verbonden account door erop te tikken, navigeer naar de muziekmap en tik op een audiobestand om de speler te starten.

![Evermusic - SMB-ondersteuning - Verbonden map openen scherm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Geniet naadloos van je muziekcollectie op je iPhone of iPad met Evermusic.

![Evermusic - SMB-ondersteuning - Audiospeler scherm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Stap 4: SMB2-oplossing

Als je problemen ondervindt bij het bladeren door mappen of het afspelen van bestanden met speciale tekens (zoals ü, ö, é), kan dit verband houden met het SMB2-protocol. We werken actief aan het oplossen van dit probleem.

Als tijdelijke oplossing kun je proberen SMB 1 in te schakelen op je server en in de app-instellingen. Als alternatief kun je verbinding maken met je SMB-server via het systeemmenu voor het openen van bestanden. Zo doe je dat:

1. Navigeer naar "Lokale bestanden."
2. Scroll naar beneden naar het gedeelte "Bestanden op dit apparaat" en tik op "Bestanden openen..." of "Mappen openen..."
3. Zoek je server en selecteer de bestanden of mappen die je nodig hebt.
4. Tik op "Openen" om je selectie te bevestigen.

## Stap 5: WebDAV-oplossing

Daarnaast kun je proberen verbinding te maken met je NAS via WebDAV- of DLNA-protocollen als deze worden ondersteund.

Door deze stappen te volgen, kun je de problemen met speciale tekens in bestandsnamen omzeilen en blijven genieten van je mediabestanden.

P.S. Je kunt ook audiobestanden van je MAC/PC naar je iPhone overbrengen met iTunes Bestandsdeling en lokale audiobestanden afspelen. Lees meer over deze functie in onze handleiding: [Hoe iTunes-bestanden af te spelen op iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Veelgestelde vragen

{{% details title="Kan ik muziek streamen van mijn PC naar mijn iPhone zonder iTunes?" closed="true" %}}
Ja. Evermusic maakt verbinding met je PC via SMB op je lokale Wi-Fi-netwerk. iTunes is niet vereist. Schakel gewoon bestandsdeling in op je PC en maak verbinding in de app.
{{% /details %}}

{{% details title="Gebruikt SMB-streaming mobiele data?" closed="true" %}}
Nee. SMB werkt via je lokale Wi-Fi-netwerk. Er is geen internetverbinding of mobiele data nodig.
{{% /details %}}

{{% details title="Welke audioformaten ondersteunt Evermusic via SMB?" closed="true" %}}
Evermusic ondersteunt MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC en andere gangbare audioformaten. Bestanden worden rechtstreeks afgespeeld vanaf de SMB-share.
{{% /details %}}

{{% details title="Kan ik muziek streamen van een NAS naar mijn iPhone?" closed="true" %}}
Ja. Als je NAS SMB ondersteunt (de meeste doen dat, waaronder Synology, QNAP en WD My Cloud), kun je er verbinding mee maken met dezelfde stappen in deze handleiding.
{{% /details %}}

{{% details title="Moet ik mijn computer aan laten staan tijdens het streamen?" closed="true" %}}
Ja. Aangezien Evermusic bestanden rechtstreeks van je computer streamt, moet deze ingeschakeld zijn en verbonden met hetzelfde netwerk als je iPhone.
{{% /details %}}

{{% details title="Is er een bestandsgroottelimiet voor SMB-streaming?" closed="true" %}}
Nee. Evermusic streamt bestanden van elke grootte via SMB. Grote lossless bestanden (FLAC, WAV) werken zonder problemen.
{{% /details %}}
