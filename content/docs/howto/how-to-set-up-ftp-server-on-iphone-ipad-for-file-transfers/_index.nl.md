---
title: "Zo stel je een FTP-server in op iPhone en iPad voor bestandsoverdracht"
description: "Maak van je iPhone of iPad een FTP-server met Everdisk en zet bestanden over vanaf een Mac, Windows-pc, Linux, Android, een FTP-app zoals FileZilla, of een andere iPhone via Wi-Fi. Volledige installatie, het ftp-adres en de poort, gasttoegang, en stapsgewijze verbinding voor elk apparaat."
date: 2026-09-19
tags: ["everdisk", "ftp", "bestandsoverdracht", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP-server iPhone", "FTP-server iPad", "FTP instellen op iPhone", "iphone ftp-server-app", "FileZilla verbinden met iPhone", "Cyberduck iPhone FTP", "bestanden overzetten iPhone FTP", "ftp iphone naar computer", "ftp iphone naar iphone", "verbinden met iPhone FTP vanaf Windows", "ftp-adres poort iphone", "anonieme ftp iphone", "bestanden delen iphone ftp", "iphone ftp voor camera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP is de oude betrouwbare kracht van bestandsoverdracht. Het bestaat al decennia, en juist daarom is het zo nuttig: bijna alles wat met een server kan praten, begrijpt het. Camera's, smart-tv's, routers, netwerkschijven, automatiseringstools en elke desktop-FTP-app spreken FTP. Met [Everdisk](/products/everdisk) kun je een FTP-server op je iPhone of iPad draaien, zodat de telefoon een plek wordt waar die apparaten en apps verbinding mee kunnen maken en bestanden kunnen verplaatsen.

Grijp naar FTP wanneer de andere opties niet passen, bijvoorbeeld een ouder apparaat of een app die alleen weet hoe hij via FTP moet verbinden. Deze handleiding behandelt de installatie en hoe je verbindt vanaf een Mac, Windows, een FTP-app, Linux, Android en een tweede iPhone.

## Wat je nodig hebt

- Een iPhone of iPad met [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) geïnstalleerd.
- Een computer, app of apparaat op **hetzelfde Wi-Fi-netwerk**.
- De bestanden die je wilt delen, in de map Documenten van Everdisk of in mappen die je toevoegt.

## Stel de FTP-server in Everdisk in

### Stap 1: Kies wat je deelt en stel toegang in

Open Everdisk, ga naar het tabblad **Delen** en tik op **Wat te delen**. De map Documenten wordt standaard gedeeld. Voeg er meer toe met **Map toevoegen** en **Bestand toevoegen**.

Open **Instellingen**, dan **Delen**, dan **Toegang**. Zet **Bestanden bewerken** aan als je wilt dat mensen kunnen uploaden, hernoemen en verwijderen, of uit om alleen downloads toe te staan. Stel een **Inlognaam** en **Wachtwoord** in als je een aanmelding wilt, of laat ze leeg zodat iedereen als gast kan verbinden.

### Stap 2: Zet de FTP-server aan

Ga naar **Instellingen**, dan **Delen**, dan **Verbindingen**, en zet **Andere apps en apparaten** aan. Dat is de FTP-server (die draagt de FTP-tag).

### Stap 3: Begin met delen en noteer het adres

Ga terug naar het tabblad **Delen** en tik op **Start**. Het gedeelte **Hoe verbinden** toont het FTP-adres. Het ziet er zo uit:

```
ftp://192.168.1.20:2121
```

Het getal na de dubbele punt is de **poort**, die standaard **2121** is. Het eerste deel is het adres van je iPhone op het Wi-Fi, dus dat van jou is anders. Houd Everdisk in beeld terwijl een apparaat verbonden is.

## Verbinden vanaf een Mac

1. Open **Finder**, kies **Ga**, dan **Verbind met server** (of druk op **Command en K**).
2. Typ het FTP-adres dat in Everdisk wordt getoond, bijvoorbeeld `ftp://192.168.1.20:2121`.
3. Klik op **Verbind**, kies dan **Gast** of voer je **Inlognaam** en **Wachtwoord** in.

Finder koppelt de FTP-share aan zodat je kunt bladeren en bestanden naar je Mac kunt kopiëren. Let op: Finder opent FTP als alleen-lezen. Als je vanaf een Mac wilt uploaden, gebruik dan een FTP-app zoals hieronder beschreven.

## Verbinden vanaf Windows

1. Open **Verkenner** en klik op de adresbalk bovenaan.
2. Typ het FTP-adres uit Everdisk, bijvoorbeeld `ftp://192.168.1.20:2121`, en druk op **Enter**.
3. Voer je **Inlognaam** en **Wachtwoord** in als je die hebt ingesteld, of ga verder als gast.

De gedeelde bestanden verschijnen in het venster en je kunt ze naar je pc kopiëren.

## Verbinden met een FTP-app (FileZilla, Cyberduck)

Voor uploads en volledige controle is een FTP-app het beste hulpmiddel. **FileZilla** en **Cyberduck** zijn gratis en draaien op Windows, Mac en Linux.

1. Open de app en maak een nieuwe verbinding.
2. Stel de **Host** in op het Wi-Fi-adres van je iPhone, en de **Poort** op **2121**.
3. Voer voor de login je **Inlognaam** en **Wachtwoord** in, of kies **Anonymous** als je er geen hebt ingesteld.
4. Verbind, en sleep bestanden in beide richtingen (uploads vereisen dat Bestanden bewerken aanstaat).

## Verbinden vanaf Linux

1. Open je bestandsbeheer en kies **Verbind met server** of **Andere locaties**.
2. Voer het adres in, bijvoorbeeld `ftp://192.168.1.20:2121`.
3. Verbind als gast of met je login.

Je kunt ook elke Linux-FTP-client vanuit de terminal gebruiken, gericht op dezelfde host en poort 2121.

## Verbinden vanaf Android

Android heeft geen systeem-FTP-browser, dus gebruik een app:

1. Installeer een FTP-client zoals **AndFTP**, **FTPCafe**, of een bestandsbeheer met FTP-ondersteuning zoals **Solid Explorer**.
2. Voeg een verbinding toe met de host, **poort 2121**, en je login of Anonymous.
3. Blader en zet over.

## Verbinden vanaf een andere iPhone of iPad

De iOS Bestanden-app bevat geen FTP-client, dus gebruik een van deze op het tweede apparaat:

- **Het eigen tabblad Apparaten van Everdisk.** Open Everdisk, ga naar **Apparaten**, tik op **Nieuwe verbinding**, kies **FTP**, en voer het adres in, bijvoorbeeld `ftp://192.168.1.20:2121`. Dit is de eenvoudigste route.
- **Een speciale FTP-app** voor iOS, met dezelfde host, poort 2121 en login.

## Verbind andere apparatuur: camera's, tv's, routers en NAS

Dit is waar FTP uitblinkt. Veel apparaten hebben een ingebouwde FTP-client die bestanden kan versturen of ophalen:

- **Camera's** die foto's via FTP uploaden, kunnen ze rechtstreeks naar je iPhone sturen.
- **Smart-tv's, routers, NAS-apparaten en automatiseringstools** die FTP ondersteunen, kunnen op dezelfde manier verbinden.

Richt ze op het Wi-Fi-adres van je iPhone, poort **2121**, en je login (of Anonymous), met het adres dat in Everdisk wordt getoond.

## Alleen-lezen of lezen en schrijven

De schakelaar **Bestanden bewerken** in Instellingen, Delen, Toegang bepaalt dit. Aan laat mensen uploaden, hernoemen en verwijderen. Uit betekent dat ze alleen kunnen downloaden. Kies alleen-lezen wanneer je bestanden uitdeelt en niet wilt dat er iets op je telefoon wordt gewijzigd.

## Praktijksituaties waarin mensen dit gebruiken

- **Verbind FileZilla met je iPhone** en zet in één keer een reeks bestanden op de telefoon.
- **Laat een oude app of apparaat dat alleen FTP spreekt** je bestanden bereiken wanneer niets anders wil verbinden.
- **Ontvang foto's van een camera** die via FTP uploadt.
- **Verplaats bestanden tussen een iPhone en een iPad** met het tabblad Apparaten van Everdisk op het ontvangende apparaat.

## Een paar tips

- Houd Everdisk open terwijl een apparaat verbonden is, want iOS pauzeert na een tijdje achtergrond-apps.
- Gebruik om vanaf een Mac te uploaden FileZilla of Cyberduck in plaats van Finder, want Finder opent FTP als alleen-lezen.
- Laat de login leeg voor de breedste compatibiliteit en verbind dan als Anonymous, wat de meeste FTP-clients aanbieden.
- FTP versleutelt zijn verkeer niet. Gebruik op een netwerk dat je niet vertrouwt in plaats daarvan de [SMB-server met versleuteling](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Veelgestelde vragen

{{% details title="Wat is het FTP-adres en de poort voor mijn iPhone?" closed="true" %}}
Nadat je met delen begint, toont Everdisk het adres op het scherm Delen. Het ziet er zo uit: ftp://192.168.1.20:2121. De 2121 is de poort die Everdisk voor FTP gebruikt, en het eerste deel is het adres van je iPhone op het Wi-Fi, dus dat van jou is anders.
{{% /details %}}

{{% details title="Hoe verbind ik FileZilla of Cyberduck met mijn iPhone?" closed="true" %}}
Open de app en maak een nieuwe verbinding. Stel de Host in op het Wi-Fi-adres van je iPhone en de Poort op 2121. Voer je Inlognaam en Wachtwoord in, of kies Anonymous als je er geen hebt ingesteld in Everdisk. Verbind, en je kunt bestanden in beide richtingen slepen wanneer Bestanden bewerken aanstaat.
{{% /details %}}

{{% details title="Kan ik vanaf Windows verbinden met mijn iPhone-FTP?" closed="true" %}}
Ja. Open Verkenner, klik op de adresbalk, typ het FTP-adres uit Everdisk (bijvoorbeeld ftp://192.168.1.20:2121), en druk op Enter. Voer je login in als je die hebt ingesteld, of ga verder als gast. Gebruik voor uploads en meer controle in plaats daarvan een FTP-app zoals FileZilla.
{{% /details %}}

{{% details title="Heb ik een login nodig voor FTP?" closed="true" %}}
Nee, een login is optioneel. Laat de Inlognaam en het Wachtwoord leeg in Instellingen, Delen, Toegang, en verbind als Anonymous, wat de meeste FTP-clients aanbieden. Stel een login in als je wilt dat verbindingen eerst inloggen.
{{% /details %}}

{{% details title="Waarom kan ik alleen downloaden en niet uploaden via FTP?" closed="true" %}}
Twee redenen komen vaak voor. Ten eerste moet de schakelaar Bestanden bewerken in Instellingen, Delen, Toegang aanstaan om uploads, hernoemingen en verwijderingen toe te staan. Ten tweede opent Mac Finder FTP als alleen-lezen, dus gebruik een FTP-app zoals FileZilla of Cyberduck wanneer je wilt uploaden.
{{% /details %}}

{{% details title="Kan ik FTP gebruiken tussen twee iPhones?" closed="true" %}}
Ja. Start de FTP-server op de eerste iPhone. Open op de tweede Everdisk, ga naar het tabblad Apparaten, tik op Nieuwe verbinding, kies FTP, en voer het adres in dat op de eerste telefoon wordt getoond. Een speciale FTP-app voor iOS werkt ook, aangezien de iOS Bestanden-app geen FTP-client bevat.
{{% /details %}}

{{% details title="Is FTP veilig?" closed="true" %}}
Gewone FTP versleutelt zijn verkeer niet, dus behandel het als een hulpmiddel voor netwerken die je vertrouwt, zoals je thuis-Wi-Fi. Gebruik op een netwerk dat je niet beheert de SMB-server met SMB-versleuteling vereisen aangezet, die elke overdracht beschermt.
{{% /details %}}

{{% details title="Welke apparaten kunnen verbinden via FTP?" closed="true" %}}
Bijna alles met een FTP-client. Dat omvat Mac-, Windows- en Linux-computers, FTP-apps zoals FileZilla en Cyberduck, Android-bestandsbeheerders, en hardware zoals camera's, smart-tv's, routers, NAS-apparaten en automatiseringstools. Dat brede bereik is de belangrijkste reden om voor FTP te kiezen.
{{% /details %}}

{{% details title="Waarom viel mijn FTP-verbinding weg?" closed="true" %}}
Je iPhone is de server, en iOS pauzeert apps die te lang op de achtergrond blijven. Houd Everdisk in beeld terwijl een apparaat verbonden is, en sluit aan op stroom voor lange overdrachten. Zorg er ook voor dat beide apparaten nog op hetzelfde Wi-Fi zitten.
{{% /details %}}

{{% details title="Is Everdisk gratis?" closed="true" %}}
Ja, Everdisk is gratis te downloaden en de FTP-server is inbegrepen. Een optionele eenmalige Premium-aankoop voegt extra's toe zoals aangepaste poorten en foto- en videoconversie. Je kunt FTP instellen en bestanden overzetten zonder te betalen.
{{% /details %}}

Klaar om het te proberen? [Download Everdisk in de App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) en verbind je eerste FTP-client in een paar minuten. Vragen of feedback? Mail ons op **support@everappz.com**.
