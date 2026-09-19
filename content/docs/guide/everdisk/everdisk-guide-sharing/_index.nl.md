---
title: "Delen"
date: 2026-08-20
description: "Ontdek hoe delen werkt in Everdisk: tik op Start om van je iPhone of iPad een draadloze schijf te maken, kies wat je deelt (bestanden, mappen, foto's en muziek), draai de vijf servers (DLNA, HTTP, WebDAV, SMB, FTP), versleutel de SMB-verbinding met SMB3 (AES), lees de verbindingsadressen, zie wie er verbonden is en houd delen draaiende via Wi-Fi of een USB-kabel."
keywords: ["Everdisk delen", "draadloze schijf iPhone", "delen starten", "bestanden delen iPhone", "foto's delen via netwerk", "DLNA HTTP WebDAV FTP", "wat te delen", "hoe verbinden", "app open houden", "delen via Wi-Fi of USB-kabel"]
tags: ["everdisk", "handleiding", "delen"]
readingTime: 9
---


Het tabblad **Delen** is het hart van Everdisk. Hier maak je van je iPhone of iPad een draadloze schijf, kies je precies wat je wilt delen en krijg je de adressen die andere apparaten gebruiken om verbinding te maken. Dit is het eerste tabblad dat je ziet als je de app opent.

## Delen starten en stoppen

Midden op het Delen-scherm staat een grote ronde knop.

- Tik op **Start** om al je ingeschakelde servers in één keer online te brengen. De knop toont **Starten...** en daarna **Stop** zodra het delen actief is.
- Tik op **Stop** om alles weer offline te halen. Verbonden apparaten worden losgekoppeld.

Zolang delen actief is, zijn de door jou gekozen bestanden, foto's en muziek beschikbaar voor elk apparaat op hetzelfde netwerk dat verbinding maakt via een van de vijf onderstaande methoden.

> Delen werkt alleen zolang de app open is. Zie **Houd de app open** aan het einde van deze pagina voor het waarom, en voor hoe je grote overdrachten door laat lopen.

## Kies wat je deelt

Tik voordat je begint op de kop **Wat je deelt** om drie groepen te openen. Je kunt elke combinatie ervan delen, en je moet minstens één ding kiezen voordat delen kan starten.

**Bestanden en mappen**

- De eigen map **Documenten** van je app wordt standaard gedeeld. Je kunt het delen ervan stoppen als je dat liever hebt.
- Tik op **Map toevoegen** om een map ergens vanaf je apparaat te delen, of op **Bestand toevoegen** om losse bestanden te delen.
- Elk gedeeld item heeft een knop **Info** en een knop **Delen stoppen**.

**Foto's en video's**

- Zet **Toegang tot volledige fotobibliotheek toestaan** aan om je hele foto- en videobibliotheek te delen, of
- tik op **Foto's toevoegen** om alleen de foto's en video's te kiezen die je wilt delen.

**Muziek**

- Zet **Toegang tot volledige muziekbibliotheek toestaan** aan om je hele muziekbibliotheek te delen, of
- tik op **Nummers toevoegen** om alleen geselecteerde nummers te delen.
- Nummers die beveiligd zijn (DRM) of alleen in de cloud staan, kunnen niet worden gedeeld.

Als je probeert te starten zonder iets te selecteren, toont Everdisk de melding **Niets om te delen**. Wijzig je wat er gedeeld wordt terwijl delen actief is, **stop en start dan opnieuw** om de wijziging toe te passen.

## De vijf servers

Everdisk deelt dezelfde inhoud tegelijk op vijf manieren. Elke manier is ontworpen voor een ander soort apparaat, en elke kun je aan- of uitzetten in **Instellingen → Delen → Verbindingen**. Standaard staan alle vijf aan.

- **Tv en mediacenter (DLNA)** - voor smart-tv's en mediaspelers. Ze ontdekken je apparaat helemaal zelf en tonen je foto's, video's en muziek, met voorbeeldminiaturen.
- **Browser (HTTP)** - voor elke telefoon, tablet of computer. De ander opent een link in een webbrowser om je bestanden te doorbladeren en te downloaden. Niets te installeren.
- **Computer (WebDAV)** - voor een Mac, Windows-pc of Linux-machine. Je apparaat verschijnt als een gewone netwerkschijf, zodat je bestanden in beide richtingen kunt slepen.
- **Computer (geavanceerd) (SMB)** - een netwerkschijf voor Mac, Windows en Linux. Op een Mac verschijnt hij vanzelf in de Finder-navigatiekolom; op Windows open je hem in de Verkenner met een `smb://`-adres. Dit is de enige verbinding die je kunt **versleutelen**, met SMB3-versleuteling (AES).
- **Andere apps en apparaten (FTP)** - voor bestands-apps en gevorderde gebruikers die FTP spreken.

Voor stapsgewijze verbindingsinstructies per type, zie [Je apparaten verbinden](/docs/guide/everdisk/everdisk-guide-connect).

## Hoe verbinden en verbindingsadressen

Nadat je op Start hebt getikt, toont het onderdeel **Hoe verbinden** een kaart voor elke actieve server met het exacte **adres** dat je op het andere apparaat intikt. Elk adres is eenvoudig te kopiëren - tik erop om te kopiëren, gebruik de knop **Delen** om het te versturen, of tik op de knop **info (ⓘ)** voor gedetailleerde instructies per protocol.

- De DLNA-kaart toont een apparaatbeschrijvingsadres dat eindigt op `/device-desc.xml` voor spelers die daarom vragen.
- Wanneer je apparaat met een kabel op een Mac is aangesloten, verschijnt er een extra adres met een badge **Kabelverbinding** dat de `.local`-naam van je apparaat gebruikt.

Je kunt het adres ook als **QR-code** openen, zodat de camera van een ander apparaat er meteen naartoe kan springen.

## Wie is verbonden

Het onderdeel **Wie is verbonden** toont in realtime de apparaten die op dat moment met je verbonden zijn. Tik op de knop Meer acties naast een apparaat om **Dit apparaat blokkeren** als je het niet herkent. Geblokkeerde apparaten beheer je in [Toegang en privacy](/docs/guide/everdisk/everdisk-guide-access).

## Je apparaatnaam en avatar

Elk apparaat heeft een herkenbare naam (zoals "Speedy-Hare") en een gekleurde avatar. Dit is de naam die een tv, computer of andere app op het netwerk voor je apparaat toont, zodat het makkelijk te herkennen is. Je kunt de naam en avatar gratis opnieuw genereren, of met Premium een eigen naam, icoon of foto-avatar instellen. Zie [Instellingen](/docs/guide/everdisk/everdisk-guide-settings).

## Delen via Wi-Fi of een USB-kabel

Delen kan in twee situaties werken:

- **Via Wi-Fi** - je apparaat en de andere apparaten zitten op hetzelfde Wi-Fi-netwerk.
- **Via een USB-kabel** - je apparaat is met een kabel op een **Mac** aangesloten, zelfs als er helemaal geen Wi-Fi is. Dit is sneller dan Wi-Fi en blijft werken in een vliegtuig, in een hotel of op een vergrendeld netwerk.

Als er geen Wi-Fi en geen kabel beschikbaar is, is de knop **Start** uitgeschakeld en verschijnt de melding **Geen Wi-Fi-verbinding**. Valt de verbinding weg terwijl je deelt, dan stopt Everdisk het delen automatisch en laat het je dat weten. Tik op de infoknop bij een van deze meldingen voor een volledige uitleg.

## Houd de app open

Omdat je iPhone of iPad de rol van server vervult, **werkt delen alleen zolang Everdisk op het scherm open is**. Als je de app sluit of het apparaat lang vergrendelt, kan het systeem de app pauzeren en stopt het delen.

Voor grote overdrachten:

- Houd Everdisk open en op de voorgrond.
- Sluit je apparaat aan op de stroom.
- Zet **Automatisch slot** op **Nooit** in de iOS-app Instellingen terwijl je overdraagt.

Je kunt **Waarschuwen voor loskoppelen** aanzetten (in Instellingen → Delen), zodat Everdisk je eraan herinnert de app opnieuw te openen voordat het systeem hem onderbreekt. Tik op de infoknop op de banner **Houd de app open** voor meer details.

## Volgende stappen

- [Je apparaten verbinden](/docs/guide/everdisk/everdisk-guide-connect) - verbind een tv, computer, browser, telefoon of USB-kabel.
- [Toegang en privacy](/docs/guide/everdisk/everdisk-guide-access) - voeg een wachtwoord toe en beheer bewerken.
- [Instellingen](/docs/guide/everdisk/everdisk-guide-settings) - zet servers aan of uit en stel de kwaliteit af.
