---
title: "Zo stel je een DLNA/UPnP-mediaserver in op iPhone en iPad om te streamen"
description: "Maak van je iPhone of iPad een DLNA/UPnP-mediaserver met Everdisk en stream foto's, video's en muziek naar een smart-tv, spelconsole, VLC of Kodi via Wi-Fi. Volledige installatie plus verbinden vanaf Samsung-, LG- en Sony-tv's, Windows, Mac, Linux, Android en een andere iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "mediaserver", "streamen", "smart-tv", "iphone", "ipad", "wifi"]
keywords: ["DLNA-server iPhone", "UPnP-server iPad", "DLNA instellen op iPhone", "streamen naar smart-tv vanaf iPhone", "DLNA-mediaserver iOS", "video's naar tv streamen zonder kabel", "iPhone-foto's op tv afspelen", "Samsung-tv DLNA iPhone", "LG-tv DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA-mediaserver", "UPnP AV-mediaserver iOS", "muziek naar tv streamen vanaf iPhone", "iPhone-mediaserver-app"]
readingTime: 9
---

{{< author-byline >}}

DLNA (ook UPnP AV genoemd) is de stille werkezel achter de meeste smart-tv's. Het is een gedeelde taal waarmee een tv of mediaspeler een mediabibliotheek op hetzelfde Wi-Fi kan vinden en ervan kan afspelen, zonder dat je iets op de tv hoeft te installeren. Als je iPhone of iPad die bibliotheek kan zijn, verschijnen je foto's, video's en muziek vanzelf op het grote scherm.

Deze handleiding laat zien hoe je je iPhone of iPad in een DLNA/UPnP-mediaserver verandert met [Everdisk](/products/everdisk), en hoe je die bibliotheek opent vanaf een smart-tv, een spelconsole, VLC, Kodi, een computer, een Android-telefoon en zelfs een tweede iPhone. Alles draait via je lokale Wi-Fi, dus er wordt niets ergens geüpload.

## Wat je nodig hebt

- Een iPhone of iPad met [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) geïnstalleerd.
- Een tv, speler of computer op **hetzelfde Wi-Fi-netwerk** als je apparaat.
- De foto's, video's of muziek die je wilt afspelen, al aanwezig op je iPhone (in de Foto's-app, de Muziek-app of de map Documenten van Everdisk).

## Stel de DLNA-server in Everdisk in

### Stap 1: Kies wat je deelt

Open Everdisk en ga naar het tabblad **Delen**. Tik op **Wat te delen** en kies je inhoud:

- Zet **Toegang tot volledige fotobibliotheek toestaan** aan om elk album te delen, of tik op **Foto's toevoegen** om er een paar te kiezen.
- Zet **Toegang tot volledige muziekbibliotheek toestaan** aan om je nummers te delen, of tik op **Nummers toevoegen** voor een selectie.
- Voeg mappen of bestanden toe met **Map toevoegen** en **Bestand toevoegen**. De eigen map Documenten van de app wordt standaard gedeeld.

Je moet minstens één item hebben geselecteerd voordat delen kan starten.

### Stap 2: Zet Tv en mediacentrum (DLNA) aan

Ga naar **Instellingen**, dan **Delen**, dan **Verbindingen**. Zorg dat **Tv en mediacentrum** aanstaat. Het staat standaard aan en draagt de DLNA-tag. Dit is de server die tv's en spelers zoeken.

### Stap 3: Begin met delen

Tik terug op het tabblad **Delen** op de grote knop **Start**. Je apparaat is nu een mediaserver op je Wi-Fi. Het verschijnt bij andere apparaten onder zijn vriendelijke naam, die als je apparaatnaam in de app wordt getoond (iets als "Speedy-Hare" totdat je hem wijzigt).

DLNA-streaming staat altijd open, dus er is geen wachtwoord dat je op de tv hoeft in te voeren. Houd Everdisk in beeld terwijl je kijkt, want iOS pauzeert apps die volledig naar de achtergrond worden geduwd.

## Afspelen op een smart-tv

Dit is het meest voorkomende geval, en het kost meestal ongeveer dertig seconden.

1. Zet de tv op **hetzelfde Wi-Fi** als je iPhone.
2. Open de ingebouwde mediaspeler van de tv. De naam hangt af van het merk: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** of **SmartThings** (Samsung), **Content Share** of **SimplyShare**.
3. Zoek naar de lijst met mediaservers of bronnen. Je apparaat verschijnt daar onder zijn naam.
4. Selecteer het, blader naar je foto's, video's of muziek, en druk op afspelen.

Voorbeeldminiaturen verschijnen vanzelf, zodat je het juiste vakantiealbum of de juiste film vindt zonder te gokken.

### Welke tv's werken

De meeste tv's van **Samsung, LG, Sony BRAVIA, Panasonic (VIERA-firmware), Philips en Hisense** hebben DLNA ingebouwd en werken meteen. **PlayStation- en Xbox-consoles en de meeste AV-receivers** ook.

Een paar platforms laten het weg: **Roku-tv's, Amazon Fire TV, Vizio SmartCast en gewone Google TV** zonder mediaapp van de maker. Als je tv een van deze is en je apparaat niet kan vinden, is dat meestal de reden. Installeer op die tv's een DLNA-spelerapp zoals VLC of Kodi, of bereik je bestanden via een webbrowser met de [WebDAV-instelhandleiding](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Sommige merken lieten DLNA werken zelfs nadat ze het officiële DLNA-logo hadden verwijderd, dus als het lijkt te ontbreken, zoek dan naar een van de mediaspelernamen hierboven.

## Afspelen in VLC of Kodi op Windows, Mac en Linux

VLC en Kodi zijn gratis, draaien op elk desktopsysteem en spreken DLNA goed. Ze zijn de betrouwbare manier om je Everdisk-bibliotheek op een computer te openen.

**VLC (Windows, Mac, Linux):**

1. Open VLC.
2. Toon de afspeellijst (druk op Windows en Linux op **Ctrl+L**, open op Mac de **Playlist** vanuit het View-menu).
3. Open in de zijbalk **Universal Plug'n'Play** onder Local Network.
4. Je apparaat verschijnt in de lijst. Klik erin en kies een bestand.

**Kodi (Windows, Mac, Linux):**

1. Ga naar **Videos**, **Music** of **Pictures**, dan **Files**, dan **Add source** (of **Browse**).
2. Kies **UPnP devices**.
3. Selecteer je apparaat en blader door je bibliotheek.

Op Windows kun je ook **Windows Media Player** openen, **Other Libraries** in de zijbalk uitvouwen, en je apparaat verschijnt daar.

## Afspelen op Android

Android-telefoons en -tablets hebben geen systeem-DLNA-browser, dus gebruik een app:

- **VLC voor Android**: open het zijmenu, tik op **Local Network**, en je apparaat verschijnt onder UPnP-servers.
- **BubbleUPnP** of een vergelijkbare UPnP-app: je apparaat verschijnt in de serverlijst, en deze apps kunnen het afspelen ook naar een tv sturen.

## Afspelen op een andere iPhone of iPad

Twee apparaten, één bibliotheek. Stel dat de foto's op je iPhone staan en je ze op je iPad wilt bekijken.

- De eenvoudigste route is het eigen tabblad **Apparaten** van Everdisk op het tweede apparaat. Het werkt zowel als DLNA-client als als server. Open Everdisk op de iPad, ga naar **Apparaten**, en je iPhone verschijnt onder **Beschikbare apparaten**. Tik erop om te bladeren en af te spelen.
- Elke DLNA-spelerapp voor iOS werkt ook, zoals VLC of een UPnP-browser. Open zijn weergave voor het lokale netwerk en kies je iPhone.

## Afspelen op een spelconsole

- **PlayStation 5 en 4**: open de **Media**-app (Media Gallery), en je apparaat verschijnt als een mediaserver waar je doorheen kunt bladeren.
- **Xbox**: gebruik een mediaspelerapp die DLNA ondersteunt en kies vervolgens je apparaat uit de serverlijst.

## Als je apparaat niet in de lijst verschijnt

Met sommige spelers kun je een mediaserver op adres toevoegen in plaats van te wachten tot hij wordt ontdekt. Op het scherm **Delen** van Everdisk toont de DLNA-kaart een adres voor de apparaatbeschrijving dat eindigt op `/device-desc.xml`. Voer dat adres in in het serverveld van de speler.

Als het nog steeds niet verschijnt, controleer dan drie dingen: beide apparaten zitten op hetzelfde Wi-Fi (niet een gastennetwerk dat verkeer tussen apparaten blokkeert), Everdisk is open en delen is gestart, en **Tv en mediacentrum** staat aan in Instellingen.

## Als een video niet wil afspelen

DLNA geeft het bestand ongewijzigd door aan de tv, en de tv moet het kunnen decoderen. Als een clip weigert af te spelen, wordt het formaat waarschijnlijk niet ondersteund door die tv. Twee oplossingen:

- Open **Instellingen**, dan **Delen**, dan **Video's**, en verlaag de **Kwaliteit**. Everdisk zet de video dan tijdens het streamen om naar een beter compatibel formaat. (Conversie is een Premium-functie.)
- Of open hetzelfde bestand in een webbrowser met de browserlink van Everdisk, die soepeler omgaat met formaten.

## Praktijksituaties waarin mensen dit gebruiken

- **Filmavond met het gezin.** Video's die je op je telefoon hebt gemaakt, spelen op de tv in de woonkamer zonder kabel of Apple TV.
- **Vakantiefoto's op het grote scherm.** Open je Foto's-bibliotheek op de tv en veeg door de reis met iedereen in de kamer.
- **Achtergrondmuziek op een feestje.** Richt een DLNA-speaker of AV-receiver op je Muziek-bibliotheek en laat het draaien.
- **Kijken op een hoteltv** met een mediaspeler, zodra beide apparaten op het Wi-Fi van de kamer zitten.

## Een paar tips

- Houd Everdisk open terwijl je streamt. Als je de telefoon lang vergrendelt, kan iOS de app pauzeren en stopt het afspelen.
- Sluit de telefoon aan op stroom voor lange filmsessies.
- Voor de snelste streaming houd je **Formaat** en **Kwaliteit** op **Origineel** in Instellingen, en verlaag je ze alleen als een specifieke tv moeite heeft met een bestand.
- DLNA is alleen streamen. Niemand aan de tv-kant kan je bestanden wijzigen of verwijderen. Gebruik voor bestandsoverdracht in twee richtingen in plaats daarvan de [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)-, [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/)- of [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/)-server.

## Veelgestelde vragen

{{% details title="Wat is het verschil tussen DLNA en UPnP?" closed="true" %}}
Ze zijn nauw verwant. UPnP is de onderliggende netwerkstandaard, en DLNA is het mediaprofiel dat erbovenop is gebouwd en dat tv's en spelers gebruiken om foto's, video's en muziek te delen en af te spelen. In het dagelijks gebruik zijn de woorden uitwisselbaar. Als je Tv en mediacentrum in Everdisk aanzet, wordt je apparaat een DLNA/UPnP-mediaserver die elke DLNA-client kan bekijken.
{{% /details %}}

{{% details title="Moet ik iets op mijn tv installeren?" closed="true" %}}
Nee. Als je tv DLNA ondersteunt, heeft hij al een mediaspeler die je apparaat op het Wi-Fi kan vinden. Je installeert Everdisk alleen op de iPhone of iPad die de inhoud bevat. Als je tv geen DLNA ondersteunt, installeer dan een speler zoals VLC of Kodi op een apparaat dat ermee is verbonden.
{{% /details %}}

{{% details title="Waarom verschijnt mijn iPhone niet op de tv?" closed="true" %}}
Controleer of beide apparaten op hetzelfde Wi-Fi-netwerk zitten. Gastennetwerken en sommige kantoor- of hotelnetwerken verhinderen dat apparaten elkaar zien, wat DLNA blokkeert. Bevestig vervolgens dat Everdisk open is met delen gestart, en dat Tv en mediacentrum aanstaat in Instellingen, Delen, Verbindingen. Als de tv het nog steeds niet kan vinden, voeg de server dan handmatig toe met het adres voor de apparaatbeschrijving dat eindigt op /device-desc.xml.
{{% /details %}}

{{% details title="Heeft DLNA-streaming een wachtwoord nodig?" closed="true" %}}
Nee. DLNA staat altijd open voor iedereen op hetzelfde Wi-Fi zolang het aanstaat, en daarom is er geen login aan de tv-kant. Dat is prima op een thuisnetwerk dat je vertrouwt. Op een netwerk dat je niet vertrouwt, zet je Tv en mediacentrum uit als je klaar bent, of gebruik je in plaats daarvan de SMB-server met versleuteling.
{{% /details %}}

{{% details title="Kan ik naar een Chromecast of Roku streamen?" closed="true" %}}
Chromecast en Roku werken standaard niet als DLNA-spelers, dus ze vinden je apparaat niet rechtstreeks. De oplossing is een DLNA-app te installeren die kan casten, zoals VLC of BubbleUPnP op een telefoon, en het afspelen van daaruit naar de Chromecast of Roku te sturen. Op de meeste andere smart-tv's werkt DLNA zonder dit alles.
{{% /details %}}

{{% details title="Een video speelt zonder geluid of gaat niet open. Wat kan ik doen?" closed="true" %}}
Dat is een formaat dat de tv niet kan decoderen. Open Instellingen, Delen, Video's in Everdisk en verlaag de Kwaliteit zodat de app de video tijdens het streamen omzet naar een beter compatibel formaat. Je kunt hetzelfde bestand ook via de browserlink openen, die meer formaten aankan.
{{% /details %}}

{{% details title="Kan ik muziek streamen, niet alleen video?" closed="true" %}}
Ja. Zet Toegang tot volledige muziekbibliotheek toestaan aan, of voeg specifieke nummers toe, en begin dan met delen. Je nummers verschijnen op elke DLNA-speaker, AV-receiver of tv, met albumhoezen en trackgegevens. Muziek wordt altijd in de originele kwaliteit gedeeld.
{{% /details %}}

{{% details title="Moet de app open blijven terwijl ik kijk?" closed="true" %}}
Ja. Je iPhone fungeert als de server, en iOS pauzeert apps die lang volledig naar de achtergrond worden geduwd. Houd Everdisk in beeld terwijl je streamt, en sluit aan op stroom voor lange sessies.
{{% /details %}}

{{% details title="Hoe stream ik van de ene iPhone naar een andere iPad?" closed="true" %}}
Begin met delen op de iPhone, open dan Everdisk op de iPad en ga naar het tabblad Apparaten. De iPhone verschijnt onder Beschikbare apparaten als mediaserver. Tik erop om te bladeren en af te spelen. Everdisk werkt als DLNA-client en server, dus je hebt geen andere app nodig.
{{% /details %}}

{{% details title="Is Everdisk gratis?" closed="true" %}}
Ja, Everdisk is gratis te downloaden en de DLNA-mediaserver is inbegrepen. Een optionele eenmalige Premium Lifetime-aankoop voegt extra's toe zoals foto- en videoconversie voor oudere tv's, aangepaste poorten en meer. Je kunt DLNA-streaming instellen en gebruiken zonder te betalen.
{{% /details %}}

Klaar om het te proberen? [Download Everdisk in de App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) en stream je eerste album in een paar minuten naar de tv. Vragen of feedback? Mail ons op **support@everappz.com**.
