---
title: "Zo stel je een SMB-server in op iPhone en iPad om bestanden te delen"
description: "Maak van je iPhone of iPad een SMB-bestandsserver met Everdisk en open hem als netwerkschijf vanaf een Mac, een andere iPhone, Linux of Android via Wi-Fi. Volledige installatie, het smb-adres en de poort, optionele SMB3-versleuteling, en stapsgewijze verbinding voor elk apparaat."
date: 2026-09-19
tags: ["everdisk", "smb", "bestanden delen", "netwerkschijf", "iphone", "ipad", "mac", "finder", "versleuteling", "wifi"]
keywords: ["SMB-server iPhone", "SMB-server iPad", "SMB instellen op iPhone", "iPhone SMB-share", "iPhone verbinden met SMB Mac Finder", "smb iphone naar iphone", "iOS Bestanden-app verbinden met server SMB", "bestanden delen iPhone SMB", "iphone netwerkschijf Finder", "SMB3-versleuteling iOS", "smb-share iPhone Android", "verbinden met SMB vanaf Linux", "iphone als netwerkschijf", "bestanden delen tussen iphones wifi", "iphone koppelen als netwerkschijf"]
readingTime: 10
---

{{< author-byline >}}

SMB is de bestandsdeling die is ingebouwd in macOS, Windows en Linux, en in bijna elke netwerkschijf (NAS). Als je verbindt met een gedeelde map op een andere computer en die opent als een gewone schijf in Finder of Verkenner, dan doet SMB het werk. Met [Everdisk](/products/everdisk) kun je een SMB-share op je iPhone of iPad zetten, zodat de telefoon zelf als netwerkschijf verschijnt waar andere apparaten doorheen bladeren, vanaf kopiëren en naartoe kopiëren.

Dit is de optie om naar te grijpen wanneer je wilt dat je iPhone zich gedraagt als een echte schijf, niet als een webpagina. Het is snel, het sleept in beide richtingen, en het is het enige verbindingstype in Everdisk dat elke overdracht kan versleutelen. Deze handleiding behandelt de installatie en hoe je verbindt vanaf een Mac, een andere iPhone of iPad, Linux, Android en Windows.

## Wat je nodig hebt

- Een iPhone of iPad met [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) geïnstalleerd.
- Een ander apparaat op **hetzelfde Wi-Fi-netwerk**.
- De bestanden die je wilt delen, in de map Documenten van Everdisk of in mappen die je toevoegt.

## Stel de SMB-server in Everdisk in

### Stap 1: Kies wat je deelt en wie mag schrijven

Open Everdisk, ga naar het tabblad **Delen** en tik op **Wat te delen**. De map Documenten wordt standaard gedeeld. Voeg er meer toe met **Map toevoegen** en **Bestand toevoegen**, en zet je Foto's- of Muziek-bibliotheek aan als je die ook beschikbaar wilt maken.

Beslis of andere apparaten je bestanden alleen mogen lezen, of ze ook mogen wijzigen. Open **Instellingen**, dan **Delen**, dan **Toegang**, en stel **Bestanden bewerken** in. Als het aanstaat, kunnen verbonden apparaten bestanden naar je telefoon kopiëren en hernoemen of verwijderen. Als het uitstaat, is de share alleen-lezen.

Als je een login wilt, stel dan een **Inlognaam** en **Wachtwoord** in op hetzelfde scherm Toegang. Laat beide leeg om gasttoegang toe te staan.

### Stap 2: Zet de SMB-server aan

Ga naar **Instellingen**, dan **Delen**, dan **Verbindingen**, en zet **Computer (geavanceerd)** aan. Dat is de SMB-server (die draagt de SMB-tag).

### Stap 3: Begin met delen en noteer het adres

Ga terug naar het tabblad **Delen** en tik op **Start**. Het gedeelte **Hoe verbinden** toont nu het SMB-adres. Het ziet er zo uit:

```
smb://192.168.1.20:4455/Share
```

Drie dingen om over dat adres te weten:

- Het getal na de dubbele punt is de **poort**. Everdisk gebruikt standaard **4455**.
- De share heet **Share**.
- Het eerste deel is het adres van je iPhone op het Wi-Fi, dus dat is anders op jouw netwerk.

Houd Everdisk open terwijl apparaten verbonden zijn, want iOS pauzeert apps die te lang op de achtergrond blijven.

## Verbinden vanaf een Mac

Dit is het soepelste geval, want macOS spreekt SMB van nature.

De snelste manier: open **Finder** en kijk in de zijbalk onder **Locaties** of **Netwerk**. Everdisk kondigt zichzelf aan op het Wi-Fi, dus je iPhone verschijnt daar vaak vanzelf. Klik erop, klik dan op **Verbind als** en kies **Gast**, of voer je login in.

Handmatig verbinden:

1. Kies in Finder **Ga**, dan **Verbind met server** (of druk op **Command en K**).
2. Typ het SMB-adres dat in Everdisk wordt getoond, bijvoorbeeld `smb://192.168.1.20:4455/Share`.
3. Klik op **Verbind**, kies dan **Gast** of voer je **Inlognaam** en **Wachtwoord** in.

Je iPhone opent in een Finder-venster. Kopieer bestanden erin of eruit door te slepen, precies zoals bij elke andere schijf (als Bestanden bewerken aanstaat).

## Verbinden vanaf een andere iPhone of iPad

iOS en iPadOS kunnen SMB-shares openen in de ingebouwde **Bestanden**-app, wat overdrachten van telefoon naar telefoon schoon en snel maakt.

Op het tweede apparaat:

1. Open de **Bestanden**-app.
2. Tik op de **meer**-knop (de drie stippen, rechtsboven op iPhone) en kies **Verbind met server**.
3. Voer het SMB-adres uit Everdisk in, bijvoorbeeld `smb://192.168.1.20:4455/Share`.
4. Kies **Gast**, of **Geregistreerde gebruiker** en voer je login in.
5. De share verschijnt onder Locaties in Bestanden. Blader en kopieer in beide richtingen.

Je kunt ook het eigen tabblad **Apparaten** van Everdisk op het tweede apparaat gebruiken, dat een SMB-client bevat. Open Everdisk, ga naar **Apparaten**, tik op **Nieuwe verbinding**, kies **SMB**, en voer het adres in.

## Verbinden vanaf Linux

1. Open je bestandsbeheer (Files/Nautilus op GNOME, Dolphin op KDE).
2. Kies **Andere locaties** of **Verbind met server**.
3. Voer het adres in, bijvoorbeeld `smb://192.168.1.20:4455/Share`.
4. Verbind als gast, of voer je login in.

Vanuit een terminal kun je ook `smbclient //192.168.1.20/Share -p 4455` uitvoeren en je login invoeren wanneer daarom wordt gevraagd.

## Verbinden vanaf Android

Android heeft geen systeem-SMB-browser, dus gebruik een bestandsbeheer dat SMB ondersteunt:

1. Installeer een app zoals **CX File Explorer**, **Solid Explorer** of **X-plore File Manager**.
2. Voeg een nieuwe **SMB**- of **LAN**-verbinding toe.
3. Voer de host in (het Wi-Fi-adres van je iPhone), stel de **poort in op 4455**, en de sharenaam **Share**.
4. Verbind als gast of met je login, blader dan en kopieer.

## Verbinden vanaf Windows

Windows kan SMB-shares lezen, met één kanttekening die vooraf de moeite waard is om te weten. De ingebouwde Verkenner praat alleen met SMB op de standaardpoort en laat je geen aangepaste poort in het pad typen, en Everdisk gebruikt poort 4455. Dus de gewone route via **Netwerkstation toewijzen** bereikt het vaak niet.

Je hebt twee goede opties op Windows:

- Gebruik een bestandsbeheer of SMB-client waarmee je een aangepaste poort kunt instellen, en richt die op het adres van je iPhone met poort **4455** en de sharenaam **Share**.
- Of verbind vanaf Windows via een van de andere servers van Everdisk. De [WebDAV-installatie](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) en [FTP-installatie](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) werken beide goed vanuit de Windows Verkenner, en de browserlink werkt in elke browser.

Als je Netwerkstation toewijzen toch wilt proberen: open **Verkenner**, klik met de rechtermuisknop op **Deze pc**, kies **Netwerkstation toewijzen**, en voer de host en sharenaam in die in Everdisk worden getoond. Als het geen verbinding kan maken, is dat de poortbeperking hierboven, dus schakel over naar WebDAV of FTP.

## Zet versleuteling aan voor onbetrouwbaar Wi-Fi

SMB is de enige Everdisk-verbinding die elke overdracht kan versleutelen, wat belangrijk is op Wi-Fi dat je niet volledig beheert, zoals een café of een kantoornetwerk.

1. Stel in **Instellingen**, **Delen**, **Toegang** een **Inlognaam** en **Wachtwoord** in. Versleutelde verbindingen kunnen niet anoniem zijn, dus deze stap is vereist.
2. Zet in **Instellingen**, **Delen** de optie **SMB-versleuteling vereisen** aan.
3. Stop en start delen opnieuw zodat de wijziging van kracht wordt.

Elke SMB-overdracht wordt dan beschermd met **SMB3-versleuteling (AES)**. Het verbindende apparaat moet SMB3 ondersteunen, wat de Finder op een moderne Mac en Windows 10 of later beide doen. SMB-versleuteling is onderdeel van de eenmalige Premium-aankoop.

## Alleen-lezen of lezen en schrijven

De schakelaar **Bestanden bewerken** in Instellingen, Delen, Toegang bepaalt dit voor elke server, inclusief SMB. Zet hem aan en verbonden apparaten kunnen uploaden, hernoemen en verwijderen. Zet hem uit en ze kunnen alleen bladeren en bestanden van je telefoon kopiëren. Kies alleen-lezen wanneer je bestanden overhandigt aan iemand die je niets wilt laten wijzigen.

## Praktijksituaties waarin mensen dit gebruiken

- **Verplaats een grote map van een Mac naar je iPhone** door hem in het Finder-venster te slepen, sneller dan een webupload.
- **Haal een dag aan foto's en video's van je telefoon** op een laptop zonder iTunes of een kabel.
- **Stuur bestanden tussen twee iPhones** via de Bestanden-app, zonder een derde app aan beide kanten.
- **Werk met een bestand op zijn plek**, door een document rechtstreeks vanaf de telefoon in een app op je Mac te openen en terug op te slaan.

## Een paar tips

- Houd Everdisk open terwijl een apparaat verbonden is. Als je de telefoon lang vergrendelt, kan de app pauzeren en de verbinding wegvallen.
- Als een Mac de telefoon niet in de Finder-zijbalk ziet, verbind dan handmatig met Verbind met server en het volledige smb-adres.
- Voor de beste snelheid bij grote overdrachten houd je de foto- en videokwaliteit op Origineel in Instellingen.
- Zet op een onbetrouwbaar netwerk SMB-versleuteling vereisen aan en zet de andere servers uit terwijl je werkt.

## Veelgestelde vragen

{{% details title="Wat is het SMB-adres en de poort voor mijn iPhone?" closed="true" %}}
Nadat je met delen begint, toont Everdisk het adres op het scherm Delen. Het ziet er zo uit: smb://192.168.1.20:4455/Share. De 4455 is de poort die Everdisk voor SMB gebruikt, en Share is de naam van de gedeelde map. Het eerste deel is het adres van je iPhone op het Wi-Fi, dus dat van jou is anders.
{{% /details %}}

{{% details title="Kan ik vanaf Windows verbinden met mijn iPhone-SMB-share?" closed="true" %}}
De Windows Verkenner verbindt alleen met SMB op de standaardpoort en accepteert geen aangepaste poort in het pad, terwijl Everdisk poort 4455 gebruikt. Dus de gewone route via Netwerkstation toewijzen bereikt het vaak niet. Gebruik een bestandsbeheer waarmee je een aangepaste poort kunt instellen, of verbind vanaf Windows in plaats daarvan met WebDAV, FTP of de browserlink. Die werken allemaal vanaf Windows zonder poortproblemen.
{{% /details %}}

{{% details title="Hoe deel ik bestanden tussen twee iPhones met SMB?" closed="true" %}}
Start de SMB-server op de eerste iPhone in Everdisk. Open op de tweede iPhone de Bestanden-app, tik op de meer-knop, kies Verbind met server, en voer het smb-adres in dat in Everdisk wordt getoond (bijvoorbeeld smb://192.168.1.20:4455/Share). Verbind als Gast of met je login, en de share verschijnt in Bestanden. Je kunt ook het eigen tabblad Apparaten van Everdisk op de tweede telefoon gebruiken.
{{% /details %}}

{{% details title="Verschijnt mijn iPhone automatisch in de Finder-zijbalk op de Mac?" closed="true" %}}
Meestal wel. Everdisk kondigt de SMB-share aan op je Wi-Fi, dus je iPhone verschijnt vaak onder Locaties of Netwerk in de Finder-zijbalk. Klik erop en kies Verbind als, dan Gast of je login. Als hij niet verschijnt, verbind dan handmatig met Ga, Verbind met server en het volledige smb-adres.
{{% /details %}}

{{% details title="Heb ik een wachtwoord nodig om SMB te gebruiken?" closed="true" %}}
Nee, een login is optioneel. Laat de Inlognaam en het Wachtwoord leeg in Instellingen, Delen, Toegang om gasttoegang toe te staan. Stel ze in als je wilt dat verbindingen inloggen. Een inlognaam en wachtwoord zijn alleen vereist als je SMB-versleuteling vereisen aanzet, omdat versleutelde verbindingen niet anoniem kunnen zijn.
{{% /details %}}

{{% details title="Is de SMB-verbinding versleuteld?" closed="true" %}}
Dat kan. SMB is de enige Everdisk-verbinding die versleuteling ondersteunt. Stel een inlognaam en wachtwoord in, zet dan SMB-versleuteling vereisen aan in Instellingen, Delen. Elke overdracht wordt dan beschermd met SMB3 (AES). Het andere apparaat moet SMB3 ondersteunen, wat moderne Macs en Windows 10 of later doen. Versleuteling is een Premium-functie.
{{% /details %}}

{{% details title="Kunnen mensen mijn bestanden wijzigen of verwijderen via SMB?" closed="true" %}}
Alleen als je het toestaat. De schakelaar Bestanden bewerken in Instellingen, Delen, Toegang bepaalt dit. Als hij aanstaat, kunnen verbonden apparaten uploaden, hernoemen en verwijderen. Als hij uitstaat, is de share alleen-lezen en kunnen anderen bladeren en bestanden van je telefoon kopiëren, maar niets wijzigen.
{{% /details %}}

{{% details title="Waarom viel mijn SMB-verbinding weg?" closed="true" %}}
Je iPhone is de server, en iOS pauzeert apps die te lang op de achtergrond blijven. Houd Everdisk in beeld terwijl een apparaat verbonden is, en sluit de telefoon aan op stroom tijdens lange overdrachten. Zorg er ook voor dat beide apparaten op hetzelfde Wi-Fi zijn gebleven.
{{% /details %}}

{{% details title="SMB, WebDAV of FTP, welke moet ik gebruiken?" closed="true" %}}
Gebruik SMB wanneer je wilt dat de telefoon zich gedraagt als een echte netwerkschijf op een Mac, een andere iPhone, Linux of een NAS, en wanneer je versleuteling wilt. Gebruik WebDAV wanneer je een netwerkschijf wilt die ook goed werkt vanaf Windows. Gebruik FTP voor de breedste compatibiliteit met oudere apparaten en apps. Everdisk kan ze allemaal tegelijk draaien, dus je zit niet vast aan één.
{{% /details %}}

{{% details title="Is Everdisk gratis?" closed="true" %}}
Ja, Everdisk is gratis te downloaden en de SMB-server is inbegrepen. De optionele eenmalige Premium-aankoop voegt SMB-versleuteling, aangepaste poorten en een paar andere extra's toe. Je kunt SMB instellen en bestanden delen zonder te betalen.
{{% /details %}}

Klaar om het te proberen? [Download Everdisk in de App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) en open je iPhone in Finder in ongeveer een minuut. Vragen of feedback? Mail ons op **support@everappz.com**.
