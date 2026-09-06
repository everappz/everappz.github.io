---
title: "Je apparaten verbinden"
date: 2026-08-20
description: "Stapsgewijze instructies om verbinding te maken met je draadloze Everdisk-schijf: kijken op een smart-tv via DLNA, je bestanden openen in elke webbrowser, je apparaat als netwerkschijf koppelen in Finder, Windows of Linux via WebDAV, bestands-apps verbinden via FTP en overdragen via een USB-kabel naar een Mac zonder Wi-Fi."
keywords: ["verbinden met Everdisk", "streamen naar tv DLNA", "bestanden openen in browser", "netwerkschijf koppelen Finder", "WebDAV Windows Linux", "FTP bestands-app", "USB-kabeloverdracht Mac", "iPhone met computer verbinden", "netwerkschijf iPhone"]
tags: ["everdisk", "handleiding", "verbinden"]
readingTime: 11
---


Zodra je op **Start** tikt op het [Delen](/docs/guide/everdisk/everdisk-guide-sharing)-scherm, kunnen andere apparaten op vier verschillende manieren verbinding maken met je bestanden. Kies de methode die past bij het apparaat dat je wilt gebruiken. In elk geval wordt het exacte **adres** dat je nodig hebt getoond in het onderdeel **Hoe verbinden** van het Delen-scherm.

> Beide apparaten moeten op **hetzelfde Wi-Fi-netwerk** zitten - of, voor een Mac, verbonden zijn met een **USB-kabel** (zie het laatste onderdeel).

## Kijken op een tv (DLNA)

Gebruik dit om foto's, video's en muziek te tonen op een smart-tv of mediaspeler.

1. Zorg er in **Instellingen → Delen → Verbindingen** voor dat **Tv en mediacenter** aan staat (dit staat standaard aan).
2. Tik op het Delen-scherm op **Start**.
3. Open op je tv de ingebouwde mediaspeler of mediaserver-app (die kan Media Player, SmartShare, AllShare of iets vergelijkbaars heten).
4. Je apparaat verschijnt in de lijst met mediaservers onder zijn naam (bijvoorbeeld "Speedy-Hare"). Selecteer het.
5. Doorblader je gedeelde foto's, video's en muziek en begin met afspelen. Voorbeeldminiaturen verschijnen automatisch.

Opmerkingen:

- DLNA kan niet met een wachtwoord worden beveiligd, dus deze verbinding staat open voor iedereen op hetzelfde Wi-Fi zolang die aan staat.
- Speelt een video niet af op een oudere tv, verlaag dan de videokwaliteit in **Instellingen → Delen → Video's**, zodat Everdisk hem omzet naar een beter compatibel formaat.

## Openen in een webbrowser (HTTP)

Gebruik dit om bestanden door te geven aan iedereen met een webbrowser - geen app om te installeren.

1. Zorg er in **Instellingen → Delen → Verbindingen** voor dat **Browser** aan staat.
2. Tik op **Start**.
3. Kopieer op het Delen-scherm het **Browser**-adres (of toon de QR-code ervan).
4. Open op de andere telefoon, tablet of computer een willekeurige webbrowser (Safari, Chrome, Edge, Firefox) en tik dat adres in.
5. De pagina opent met je gedeelde bestanden.

In de browser kan de ander:

- Wisselen tussen **lijst**- en **rasterweergave** en sorteren op naam, datum of grootte.
- Echte **miniaturen** zien voor foto's, video's, PDF's en muziekhoezen.
- Een foto openen in een **galerij** op volledig scherm met vegen, knijpen om te zoomen en een diavoorstelling.
- Muziek afspelen in een ingebouwde **speler** met een wachtrij, shuffle en herhalen.
- Elk bestand **downloaden**, of een hele map (of meerdere geselecteerde items) downloaden als één **Archive.zip**.
- Bestanden terug naar je apparaat **uploaden** - alleen als je **Bestanden bewerken** hebt aangezet (zie [Toegang en privacy](/docs/guide/everdisk/everdisk-guide-access)).

## Gebruiken als netwerkschijf (WebDAV)

Gebruik dit om je apparaat als een gewone schijf op een Mac, Windows-pc of Linux-machine te laten verschijnen, zodat je bestanden beide kanten op kunt slepen.

**Op een Mac (Finder)**

1. Zorg er in **Instellingen → Delen → Verbindingen** voor dat **Computer** aan staat.
2. Tik op **Start** en noteer het adres bij **Computer (WebDAV)**.
3. Kies in Finder **Ga → Verbind met server** (of druk op **⌘K**).
4. Tik het WebDAV-adres exact zoals getoond in en klik op **Verbind**.
5. Voer de login en het wachtwoord in als je die hebt ingesteld, anders verbind je als gast.
6. Je apparaat opent als elke andere netwerkschijf. Sleep bestanden erin of eruit.

**Op Windows**

1. Open **Verkenner**, klik met de rechtermuisknop op **Deze pc** en kies **Een netwerklocatie toevoegen** (of een netwerkschijf toewijzen).
2. Voer het WebDAV-adres in dat in Everdisk wordt getoond.
3. Voer de login en het wachtwoord in als je die hebt ingesteld.

**Op Linux**

1. Open je bestandsbeheerder en kies **Verbind met server** (of gebruik `davs://` / `dav://`).
2. Voer het WebDAV-adres in dat in Everdisk wordt getoond.

Of de verbinding alleen-lezen of tweerichtings is, hangt af van de instelling **Bestanden bewerken**. Staat die aan, dan kun je bestanden naar je apparaat kopiëren en ze hernoemen of verwijderen; staat die uit, dan is de schijf alleen-lezen.

## Een bestands-app verbinden (FTP)

Gebruik dit voor bestandsbeheer- en overdracht-apps die FTP spreken (bijvoorbeeld FileZilla of Cyberduck op een computer).

1. Zorg er in **Instellingen → Delen → Verbindingen** voor dat **Andere apps en apparaten** aan staat.
2. Tik op **Start** en noteer het **FTP**-adres.
3. Voeg in je FTP-app een nieuwe verbinding toe met dat adres.
4. Voer de login en het wachtwoord in als je die hebt ingesteld, of laat ze leeg voor anonieme toegang.

## Overdragen via een USB-kabel (Mac, geen Wi-Fi nodig)

Gebruik dit wanneer er geen Wi-Fi is, of wanneer je de snelste en meest private overdracht wilt. Het werkt alleen met een **Mac**.

1. Sluit je iPhone of iPad met de normale oplaadkabel aan op de Mac.
2. Tik op **Vertrouw deze computer** als het apparaat daarom vraagt.
3. Tik in Everdisk op **Start**. Er verschijnt een melding **Snelle verbinding beschikbaar** en het Delen-scherm toont een extra adres met een badge **Kabelverbinding** dat eindigt op `.local`.
4. Open op de Mac Finder → **Ga → Verbind met server** (**⌘K**) en voer dat `.local`-adres in (het werkt voor zowel de Browser- als de Computer-verbinding).
5. Je apparaat opent via de kabel - sneller dan Wi-Fi, en de gegevens raken nooit de router of het internet.

Opmerkingen:

- Gebruik de **`.local`-naam**, geen IP-adres (IP-adressen werken alleen via Wi-Fi), en nooit `localhost`.
- Het kabelpad is **alleen voor Mac**. Windows-pc's en Android-apparaten moeten Wi-Fi gebruiken.
- Je kunt bestanden ook in de Everdisk-map slepen met Finder op een Mac, of met de app Apple Devices (of iTunes) op Windows, via de standaard iOS-bestandsdeling.

## Volgende stappen

- [Toegang en privacy](/docs/guide/everdisk/everdisk-guide-access) - voeg een wachtwoord toe, sta uploads toe, blokkeer een apparaat.
- [Foto's, muziek en video](/docs/guide/everdisk/everdisk-guide-media) - deel je hele bibliotheek en stel de kwaliteit in.
- [Verbinden met servers](/docs/guide/everdisk/everdisk-guide-devices) - bereik andere apparaten vanuit Everdisk.
