---
title: "Zo stel je een WebDAV-server in op iPhone en iPad voor bestandstoegang en delen"
description: "Maak van je iPhone of iPad een WebDAV-server met Everdisk en koppel hem aan als netwerkschijf op Mac Finder, Windows Verkenner, Linux, Android of een andere iPhone via Wi-Fi. Volledige installatie, het WebDAV-adres en de poort, en stapsgewijze verbinding voor elk apparaat."
date: 2026-09-19
tags: ["everdisk", "webdav", "netwerkschijf", "bestanden delen", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV-server iPhone", "WebDAV-server iPad", "WebDAV instellen op iPhone", "iPhone aankoppelen als netwerkschijf", "iPhone verbinden met WebDAV Mac Finder", "WebDAV Windows Verkenner iPhone", "iphone netwerkschijf Windows", "WebDAV Linux iPhone", "iPhone-bestanden openen vanaf computer", "webdav iphone naar iphone", "bestanden delen iPhone WebDAV", "netwerkstation toewijzen iphone", "bestanden overzetten iphone webdav", "webdav-adres poort iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV verandert een map in een netwerkschijf die een computer in zijn gewone bestandsbeheer kan openen. Het draait over hetzelfde webprotocol dat je browser gebruikt, en daarom reist het goed over Mac, Windows en Linux zonder speciale stuurprogramma's. Met [Everdisk](/products/everdisk) kun je een WebDAV-server op je iPhone of iPad draaien, zodat de telefoon verschijnt als een schijf waar je vanaf bijna elke computer doorheen kunt bladeren, vanaf kunt kopiëren en naartoe kunt kopiëren.

WebDAV is de beste keuze wanneer Windows in beeld is, want de Windows Verkenner verbindt er netjes mee. Deze handleiding behandelt de installatie en hoe je verbindt vanaf een Mac, Windows, Linux, Android en een tweede iPhone.

## Wat je nodig hebt

- Een iPhone of iPad met [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) geïnstalleerd.
- Een computer of ander apparaat op **hetzelfde Wi-Fi-netwerk**.
- De bestanden die je wilt delen, in de map Documenten van Everdisk of in mappen die je toevoegt.

## Stel de WebDAV-server in Everdisk in

### Stap 1: Kies wat je deelt en stel toegang in

Open Everdisk, ga naar het tabblad **Delen** en tik op **Wat te delen**. De map Documenten wordt standaard gedeeld. Voeg er meer toe met **Map toevoegen** en **Bestand toevoegen**.

Open **Instellingen**, dan **Delen**, dan **Toegang**. Zet **Bestanden bewerken** aan als je wilt dat verbonden computers bestanden naar je telefoon kopiëren en hernoemen of verwijderen, of uit voor een alleen-lezenschijf. Stel hier een **Inlognaam** en **Wachtwoord** in als je een aanmelding wilt, of laat ze leeg voor gasttoegang.

### Stap 2: Zet de WebDAV-server aan

Ga naar **Instellingen**, dan **Delen**, dan **Verbindingen**, en zet **Computer** aan. Dat is de WebDAV-server (die draagt de WebDAV-tag).

### Stap 3: Begin met delen en noteer het adres

Ga terug naar het tabblad **Delen** en tik op **Start**. Het gedeelte **Hoe verbinden** toont het WebDAV-adres. Het ziet er zo uit:

```
http://192.168.1.20:8080
```

Het getal na de dubbele punt is de **poort**, die standaard **8080** is. Het eerste deel is het adres van je iPhone op het Wi-Fi, dus dat van jou verschilt. Houd Everdisk in beeld terwijl een apparaat verbonden is.

## Verbinden vanaf een Mac

1. Open **Finder**, kies **Ga**, dan **Verbind met server** (of druk op **Command en K**).
2. Typ het WebDAV-adres dat in Everdisk wordt getoond, bijvoorbeeld `http://192.168.1.20:8080`.
3. Klik op **Verbind**, kies dan **Gast** of voer je **Inlognaam** en **Wachtwoord** in.

Je iPhone opent in een Finder-venster en gedraagt zich als een gewone map. Kopieer bestanden in beide richtingen als Bestanden bewerken aanstaat.

## Verbinden vanaf Windows

Windows heeft een ingebouwde WebDAV-client, dus dit werkt vanuit de Verkenner.

1. Open **Verkenner**, klik met de rechtermuisknop op **Deze pc** in de zijbalk, en kies **Netwerklocatie toevoegen** (je kunt ook **Netwerkstation toewijzen** gebruiken).
2. Wanneer om het adres wordt gevraagd, typ je hetzelfde WebDAV-adres uit Everdisk, bijvoorbeeld `http://192.168.1.20:8080`, en klik je op **Volgende**.
3. Voer je **Inlognaam** en **Wachtwoord** in als je die hebt ingesteld.

Het apparaat verschijnt dan onder Deze pc als een netwerklocatie die je kunt openen en waarvandaan je bestanden kunt kopiëren. Als Windows de eerste keer weigert te verbinden, zorg dan dat de **WebClient**-service draait (zoek Services in het Startmenu, vind WebClient, en zet die op starten), en probeer het opnieuw.

## Verbinden vanaf Linux

1. Open je bestandsbeheer en kies **Verbind met server** of **Andere locaties**.
2. Voer het adres in met een WebDAV-voorvoegsel, bijvoorbeeld `dav://192.168.1.20:8080` (gebruik `davs://` alleen als je TLS hebt ingesteld).
3. Verbind als gast of voer je login in.

## Verbinden vanaf Android

Android heeft geen systeem-WebDAV-browser, dus gebruik een bestandsbeheer dat het ondersteunt:

1. Installeer een app zoals **Solid Explorer** of **CX File Explorer**.
2. Voeg een nieuwe **WebDAV**-verbinding toe.
3. Voer de host en **poort 8080** in, kies het `http`-schema, en voeg je login toe als je die hebt ingesteld.

## Verbinden vanaf een andere iPhone of iPad

De iOS Bestanden-app bevat geen WebDAV-client, dus gebruik een van deze:

- **Het eigen tabblad Apparaten van Everdisk.** Open op het tweede apparaat Everdisk, ga naar **Apparaten**, tik op **Nieuwe verbinding**, kies **WebDAV**, en voer het adres in, bijvoorbeeld `http://192.168.1.20:8080`. Dit is de eenvoudigste route en vergt niets extra's.
- **Een WebDAV-app** zoals Documents by Readdle, die een WebDAV-verbinding kan toevoegen met hetzelfde adres en login.

## Liever een snelle link dan een schijf?

Als je alleen snel een bestand wilt pakken en helemaal geen schijf wilt aankoppelen, zet dan de **Browser**-verbinding aan in Instellingen, Delen, Verbindingen. Everdisk geeft je dan een webadres dat je in elke browser op elk apparaat kunt openen om door je bestanden te bladeren en ze te downloaden. Het is de snelste manier om een bestand aan een Windows-pc, een Chromebook of de telefoon van een vriend te geven.

## Alleen-lezen of lezen en schrijven

De schakelaar **Bestanden bewerken** in Instellingen, Delen, Toegang bepaalt dit. Aan betekent dat verbonden computers kunnen uploaden, hernoemen en verwijderen. Uit betekent dat de schijf alleen-lezen is, zodat anderen je bestanden kunnen bekijken en kopiëren maar niet kunnen wijzigen.

## Praktijksituaties waarin mensen dit gebruiken

- **Kopieer bestanden naar je iPhone vanaf een Windows-pc** door hem als netwerklocatie toe te wijzen en ze over te slepen.
- **Zet foto's en documenten over naar een laptop** met het bestandsbeheer dat je al kent, zonder kabel en zonder iTunes.
- **Bewerk een document op zijn plek** vanaf je Mac, door het rechtstreeks vanaf de telefoon te openen en terug op te slaan.
- **Verplaats een map tussen een iPhone en een iPad** met het tabblad Apparaten van Everdisk op het ontvangende apparaat.

## Een paar tips

- Houd Everdisk open terwijl een apparaat verbonden is. Als je de telefoon lang vergrendelt, kan de app pauzeren.
- Als de verbinding op Windows mislukt, start dan de WebClient-service en probeer het adres opnieuw.
- WebDAV en SMB koppelen beide aan als netwerkschijf. Gebruik WebDAV wanneer Windows betrokken is, en [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) wanneer je Finder-snelheid en versleuteling wilt.
- Voor de snelste overdrachten houd je de foto- en videokwaliteit op Origineel in Instellingen.

## Veelgestelde vragen

{{% details title="Wat is het WebDAV-adres en de poort voor mijn iPhone?" closed="true" %}}
Nadat je met delen begint, toont Everdisk het adres op het scherm Delen. Het ziet er zo uit: http://192.168.1.20:8080. De 8080 is de poort die Everdisk voor WebDAV gebruikt, en het eerste deel is het adres van je iPhone op het Wi-Fi, dus dat van jou is anders.
{{% /details %}}

{{% details title="Hoe verbind ik vanaf Windows met mijn iPhone-WebDAV?" closed="true" %}}
Open Verkenner, klik met de rechtermuisknop op Deze pc, en kies Netwerklocatie toevoegen of Netwerkstation toewijzen. Voer het WebDAV-adres uit Everdisk in, bijvoorbeeld http://192.168.1.20:8080, en voer daarna je login in als je die hebt ingesteld. Als Windows niet wil verbinden, zorg dan dat de WebClient-service draait (zoek Services, vind WebClient, start hem) en probeer het opnieuw.
{{% /details %}}

{{% details title="Kan ik WebDAV gebruiken tussen twee iPhones?" closed="true" %}}
Ja, maar de iOS Bestanden-app heeft geen WebDAV-client, dus gebruik Everdisk op het tweede apparaat. Open het tabblad Apparaten, tik op Nieuwe verbinding, kies WebDAV, en voer het adres in dat op de eerste telefoon wordt getoond. Een WebDAV-app zoals Documents by Readdle werkt ook.
{{% /details %}}

{{% details title="Heeft WebDAV een wachtwoord nodig?" closed="true" %}}
Nee, een login is optioneel. Laat de Inlognaam en het Wachtwoord leeg in Instellingen, Delen, Toegang voor gasttoegang, of stel ze in als je wilt dat verbindingen inloggen.
{{% /details %}}

{{% details title="Kunnen andere mensen mijn bestanden wijzigen via WebDAV?" closed="true" %}}
Alleen als je het toestaat. De schakelaar Bestanden bewerken in Instellingen, Delen, Toegang bepaalt dit. Aan laat verbonden apparaten uploaden, hernoemen en verwijderen. Uit maakt de schijf alleen-lezen, zodat anderen kunnen bekijken en kopiëren maar niets kunnen wijzigen.
{{% /details %}}

{{% details title="WebDAV of SMB, wat is het verschil?" closed="true" %}}
Beide koppelen je iPhone aan als netwerkschijf. WebDAV draait over het webprotocol en verbindt netjes vanuit de Windows Verkenner, wat zijn belangrijkste sterke punt is. SMB is de eigen bestandsdeling op Mac, Linux en NAS-apparaten, is meestal sneller op een Mac, en is de enige Everdisk-verbinding die overdrachten kan versleutelen. Everdisk kan beide tegelijk draaien.
{{% /details %}}

{{% details title="Waarom verbreekt mijn WebDAV-schijf de verbinding?" closed="true" %}}
Je iPhone is de server, en iOS pauzeert apps die te lang op de achtergrond blijven. Houd Everdisk in beeld terwijl een apparaat verbonden is, en sluit aan op stroom voor lange overdrachten. Bevestig ook dat beide apparaten nog op hetzelfde Wi-Fi zitten.
{{% /details %}}

{{% details title="Kan ik verbinden via WebDAV zonder Wi-Fi?" closed="true" %}}
Ja, als je je iPhone met een kabel op een Mac aansluit. Everdisk toont dan een extra kabelverbindingsadres dat de verbonden Mac in Finder kan openen, wat zelfs zonder Wi-Fi werkt. Via de kabel kan alleen die Mac het apparaat bereiken.
{{% /details %}}

{{% details title="Is Everdisk gratis?" closed="true" %}}
Ja, Everdisk is gratis te downloaden en de WebDAV-server is inbegrepen. Een optionele eenmalige Premium-aankoop voegt extra's toe zoals aangepaste poorten en foto- en videoconversie. Je kunt WebDAV instellen en bestanden delen zonder te betalen.
{{% /details %}}

Klaar om het te proberen? [Download Everdisk in de App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) en koppel je iPhone in een paar minuten aan als schijf. Vragen of feedback? Mail ons op **support@everappz.com**.
