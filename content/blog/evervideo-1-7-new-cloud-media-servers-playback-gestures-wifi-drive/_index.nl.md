---
title: "Evervideo 1.7: nieuwe Plex, Jellyfin, cloud-streaming, afspeel-gebaren"
date: 2026-05-18
description: "Evervideo 1.7 voegt meer dan 10 nieuwe verbindingen toe — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — plus nieuwe afspeel-gebaren (dubbeltik om te zoeken, tik en houd vast voor 2x snelheid), een vernieuwde Wi-Fi Drive met batch-upload en Liquid Glass UI-updates voor iPhone, iPad en Mac."
keywords: ["Evervideo 1.7", "Evervideo update", "HD-videospeler iPhone", "Plex videospeler iOS", "Jellyfin iPhone-video", "Emby videospeler iOS", "Subsonic video iOS", "Navidrome video iOS", "Internxt videostreaming", "Proton Drive videospeler", "QNAP videospeler iPhone", "Nextcloud videospeler iOS", "Amazon S3 videostreaming", "SFTP videospeler iPhone", "FTP videospeler iOS", "NFS videostreaming iPhone", "video streamen van NAS iPhone", "MKV-speler iPhone", "videospeler-gebaren iOS", "dubbeltik om video te zoeken", "Wi-Fi Drive videoverdracht iPhone", "Liquid Glass-design", "cloud videospeler iOS 2026", "films streamen vanuit de cloud iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Afspeel-gebaren", "Liquid Glass", "Wat is nieuw"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Korte samenvatting:** [Evervideo 1.7](/products/evervideo) is een grote update voor de HD-videospeler op iPhone, iPad en Mac. De release voegt meer dan 10 nieuwe cloud-, NAS- en mediaserver-verbindingen toe — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, plus de populairste mediaservers **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** en **Emby**, en drie netwerkprotocollen: **FTP**, **SFTP** en **NFS**. Nieuwe **afspeel-gebaren** laten je dubbeltikken om vooruit of achteruit te springen, tikken en vasthouden voor 2x snelheid, en eenmaal tikken om de bedieningselementen te wisselen — allemaal zonder volledig scherm te verlaten. Wi-Fi Drive krijgt een vernieuwde interface met selectiemodus en een slimmere uploadwachtrij. De hele app is afgestemd op Apple's nieuwe **Liquid Glass**-design.

---

## Hallo allemaal!

Een grote Evervideo-update is er. Dit is een van de grootste releases die we hebben uitgebracht: **meer dan 10 nieuwe cloud-, server- en netwerkverbindingen**, gloednieuwe **afspeel-gebaren** voor snellere bediening in volledig scherm, een vernieuwde **Wi-Fi Drive**-ervaring en een UI afgestemd op **Liquid Glass** op iPhone, iPad en Mac.

[Download Evervideo 1.7 in de App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) of werk bij vanaf je bestaande versie. Mac-gebruikers kunnen [hier de desktopversie ophalen](https://apps.apple.com/app/evervideo/id6743504109).

## Meer dan 10 nieuwe cloud-, NAS- en mediaserver-verbindingen

Evervideo 1.7 verbreedt wat als jouw 'videobibliotheek' telt. Als je films, series of opnames op een cloud staan die je vertrouwt, op een NAS thuis of op een zelfgehoste mediaserver, kan Evervideo nu rechtstreeks vanaf die plek streamen — geen downloads, geen conversies, geen hercoderen.

### Privacygerichte cloudopslag: Internxt en Proton Drive

Geef je om end-to-end-encryptie en zero-knowledge-opslag, dan zijn twee van de meest gerespecteerde privacy-eerst-clouds nu native in Evervideo:

- **Internxt** — open-source, post-quantum versleutelde, AVG-conforme Spaanse cloud. Gratis abonnement beschikbaar.
- **Proton Drive** — end-to-end versleutelde opslag van de makers van Proton Mail en Proton VPN, gevestigd in Zwitserland. Gratis tier beschikbaar, met betaalde plannen voor grotere bibliotheken.

Verbind één keer en je video's stromen door de versleutelde tunnel — Evervideo ziet je gegevens nooit in onversleutelde vorm, en de server van de aanbieder ook niet.

### Zelfgehoste opslag: QNAP, Nextcloud, Amazon S3

Voor gebruikers die hun eigen infrastructuur draaien:

- **QNAP** — native API-verbinding met QNAP-NAS-apparaten voor snelle, betrouwbare video-afspeling via lokaal Wi-Fi of toegang op afstand. Stream 4K MKV-bestanden rechtstreeks zonder hercoderen.
- **Nextcloud** — verbind met elke zelfgehoste of beheerde Nextcloud-instantie. Geweldig als je om privacyredenen al van Google Drive of Dropbox bent overgestapt.
- **Amazon S3** — wijs Evervideo aan op elke S3-bucket (of S3-compatibele opslag zoals Backblaze B2, Wasabi, MinIO, Cloudflare R2) en stream je collectie rechtstreeks.

### <a id="media-servers"></a>Mediaservers: Plex, Subsonic, Navidrome, Jellyfin, Emby

Dit is het grote nieuws voor zelfgehoste videofans. Evervideo 1.7 maakt van je iPhone, iPad of Mac een eersteklas client voor de populairste open-source en freemium mediaservers:

- **Plex** — Plex Media Server is **gratis** om te downloaden en draaien, met een optioneel **Plex Pass**-abonnement voor functies als mobiele synchronisatie, hardware-transcoderen en live-tv. Evervideo werkt zowel met gratis als met Plex Pass-bibliotheken — stream je volledige film- en tv-collectie.
- **Subsonic** — de originele zelfgehoste streamingserver. De officiële Subsonic-server is **betaald** ($1/maand na een proefperiode van 30 dagen), en Evervideo spreekt ook de Subsonic-API met compatibele videoservers.
- **Navidrome** — moderne, lichtgewicht, **volledig gratis en open-source** server. Implementeert de Subsonic-API. Draait op een Raspberry Pi, een NAS of elke Linux-box.
- **Jellyfin** — **volledig gratis en open-source** mediaserver (een community-fork van Emby). Verwerkt films, tv, muziek, boeken en thuisvideo. Geen accounts, geen telemetrie, geen abonnementen. De favoriete keuze voor gebruikers die zelfgehoste streaming willen zonder commerciële verplichtingen.
- **Emby** — **freemium** mediaserver. De kernserver is gratis; **Emby Premiere** is een eenmalige of jaarlijkse aankoop die mobiele apps, offline synchronisatie, Cinema Mode en meer ontgrendelt. Evervideo verbindt met zowel gratis als Premiere-bibliotheken.

Welke server je ook draait, Evervideo streamt je volledige bibliotheek — films, series, thuisvideo en ingebedde ondertiteltracks — met de video-equalizer, 360°-ondersteuning, Picture-in-Picture, AirPlay en Chromecast.

### Nieuwe netwerkprotocollen: FTP, SFTP, NFS

Voor gebruikers met eigen servers, homelabs of generieke NAS-apparaten die niet met een gepolijste mobiele app worden geleverd, voegt Evervideo 1.7 drie klassieke protocollen toe:

- **SFTP (SSH File Transfer Protocol)** — het juiste antwoord voor **veilige extern streamen van video vanaf je eigen server**. SFTP draait bovenop SSH, dus de hele overdracht (authenticatie en videodata) is versleuteld. Heb je een VPS, dedicated server of een Linux-machine thuis met SSH-toegang, dan kun je een map met video's daarop zetten en streamen via het open internet zonder iets anders bloot te leggen. Ondersteunt zowel wachtwoord- als sleutel-authenticatie.
- **FTP** — de gevestigde standaard voor bestandsoverdracht. Handig als je **thuis-NAS** (oudere Synology, ASUS, D-Link, TerraMaster of generieke apparaten) een FTP-server aanbiedt maar geen native API-integratie heeft. Het beste binnen je lokale netwerk te gebruiken.
- **NFS (Network File System)** — het de-facto deelprotocol op Linux en de meeste NAS-apparaten. NFS-shares zijn gangbaar in homelabs en kleine zakelijke netwerken; Evervideo koppelt ze nu en streamt 4K- en HD-video met weinig overhead.

> **Tip:** SFTP is het protocol dat je wilt voor streamen via het open internet. FTP en NFS gebruik je het best binnen je lokale netwerk — laat ze niet open op het internet staan, tenzij je ze door een VPN tunnelt.

## Nieuwe afspeel-gebaren

Video kijken in volledig scherm moet moeiteloos voelen. Evervideo 1.7 introduceert een nette set tik-gebaren waarmee je de afspeling kunt regelen zonder de bedieningselementen op het scherm zichtbaar te maken — perfect voor films, lezingen of alles wat je ononderbroken wilt bekijken.

### Dubbeltik — vooruit of achteruit springen

Dubbeltik op de **rechterkant** van het scherm om **vooruit te springen** met een instelbaar aantal seconden. Dubbeltik op de **linkerkant** om **terug te springen**. Je kunt het interval (standaard: 10 seconden) wijzigen in **Instellingen → Afspelen → Sprong-interval gebaar** — kies alles van 5 seconden (voor fijn zoeken) tot 60 seconden (voor het overslaan van intro's).

Dit is het gebaar dat YouTube- en Netflix-gebruikers meteen herkennen, en het is nu native in Evervideo voor elke video, op elke bron.

### Tik en houd vast — tijdelijk 2x snelheid

Druk en houd ergens op het scherm vast om de **afspeling tijdelijk te versnellen naar 2x**. Laat los om terug te keren naar normale snelheid. Perfect voor:

- Door trage scènes heen springen zonder je vast te leggen op een permanente snelheidsverandering.
- Snel door lezingen, tutorials of podcasts scannen om het relevante gedeelte te vinden.
- Films proeven voordat je vastlegt om de volledige versie te bekijken.

Het vasthoudgebaar verandert je opgeslagen afspeelsnelheid niet — laat los en je bent terug waar je begon.

### Eén tik — bedieningselementen tonen / verbergen

Eén tik op het scherm wisselt de afspeel-bedieningselementen (afspelen, pauzeren, zoekbalk, ondertitels, equalizer). Tik eenmaal om ze tevoorschijn te halen, tik nogmaals om ze te verbergen. Gecombineerd met dubbeltik en vasthouden betekent dit dat je bijna een hele film in een schone volledige-scherm-modus kunt doorbrengen en nog steeds kunt zoeken, pauzeren en snelheid-scannen wanneer je dat wilt.

## Wi-Fi Drive: nieuwe UI en snellere uploads

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) is de ingebouwde functie van Evervideo om **video's draadloos van je computer naar je iPhone of iPad over te zetten — geen iTunes, geen kabels, geen cloud-account vereist**. Beide apparaten moeten op hetzelfde Wi-Fi-netwerk zitten. Je start de server in de iOS-app en doet vervolgens een van het volgende:

- Open de URL in elke desktopbrowser (Safari, Chrome, Firefox, Edge), sleep je videobestanden naar de pagina en ze worden rechtstreeks naar het apparaat geüpload, of
- Koppel het apparaat als netwerkshare via **Mac Finder** ('Verbind met server…') of **Windows Verkenner** (Netwerkstation toewijzen) met WebDAV.

Het is de snelste manier om een grote lokale videocollectie naar je telefoon of tablet te verplaatsen zonder enige externe dienst. Bekijk de [stapsgewijze handleiding hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

In Evervideo 1.7 krijgt Wi-Fi Drive:

- **Heringerichte gebruikersinterface** — overzichtelijker, sneller leesbaar in één oogopslag en bijgewerkt voor Liquid Glass.
- **Nieuwe selectiemodus voor batch-acties** — kies meerdere bestanden of mappen en bewerk ze in bulk (verwijderen, verplaatsen, kopiëren).
- **Verbeterde uploadwachtrij** — betere voortgangsfeedback en bestendigheid tegen netwerkonderbrekingen, zodat een wankele Wi-Fi-verbinding een overdracht van 30 GB niet meer verpest.
- **Betere algehele overdrachtsprestaties** — meetbaar snellere uploads voor grote bibliotheken, vooral voor 4K MKV-bestanden en filmcollecties.

## Andere verbeteringen

### Liquid Glass-designupdates

De interface van Evervideo 1.7 is bijgewerkt voor Apple's nieuwe **Liquid Glass**-materiaal in de hele app — doorschijnende oppervlakken, soepelere animaties en verfijnde bedieningselementen die natuurlijk passen in iOS 26, iPadOS 26 en macOS 26. Speelt nu af, de bestandsbrowser en de instellingenschermen zijn allemaal afgestemd op de nieuwe systeem-esthetiek.

### Bijgewerkte verbindingsbibliotheken

We hebben de onderliggende bibliotheken die Evervideo gebruikt om te praten met **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** en andere diensten ververst. Het resultaat: minder verbindingsfouten in randgevallen, betere ondersteuning voor recentere serverversies en verbeterde betrouwbaarheid bij het streamen van video op tragere of geografisch verre verbindingen.

### Bugfixes voor afspelen

- Afspeelproblemen opgelost op bepaalde zelfgehoste servers waar streams vastliepen na zoeken op grote MKV-bestanden.
- Beter hervat-gedrag wanneer het netwerk kort wegvalt midden in de afspeling.
- Soepelere ondertitel-synchronisatie op langere content.

### Lokalisatie-fixes

Vertaalfixes in meerdere talen op basis van directe gebruikersfeedback. Betere tekstpassing op kleinere knoppen en langere Europese talen (Duits, Nederlands, Frans).

### Kleinere verfijningen geïnspireerd op jouw feedback

Veel kleinere verbeteringen op basis van App Store-reviews en e-mails naar support@everappz.com. We lezen elk bericht.

## Waarom deze update ertoe doet

Evervideo 1.7 is gebouwd rond drie ideeën:

1. **Jouw video's, waar je ze ook bewaart.** Of je bibliotheek nu op iCloud Drive staat, in een privacy-eerst-cloud zoals Proton Drive of Internxt, op een mediaserver zoals Plex of Jellyfin, op een NAS thuis of op een Raspberry Pi die Navidrome draait — Evervideo verbindt er nu native mee, met overal dezelfde afspeel-ervaring.
2. **Volledig-scherm-video die moeiteloos voelt.** De nieuwe tik-gebaren (dubbeltik, tik en houd vast, één tik) brengen het soort vloeiende bediening waar streamingapps als YouTube en Netflix gebruikers aan hebben laten wennen, toegepast op *jouw* videocollectie.
3. **Snellere overdrachten van je computer.** Een vernieuwde Wi-Fi Drive met batch-selectie en een slimmere uploadwachtrij maakt het verplaatsen van grote 4K-filmcollecties naar je iPhone of iPad echt snel — geen kabels, geen iTunes, geen compressie.

## Pak Evervideo 1.7

[**Download Evervideo in de App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) of werk bij vanuit de App Store. De [Mac-versie](https://apps.apple.com/app/evervideo/id6743504109) is afzonderlijk beschikbaar als universele Mac-app. Evervideo is een gratis download met optionele in-app upgrades voor geavanceerde functies. De nieuwe cloud-verbindingen, mediaserver-ondersteuning, afspeel-gebaren, Wi-Fi Drive-verbeteringen en de Liquid Glass-UI horen bij de basisupdate.

Vind je de app leuk? Laat dan een beoordeling achter in de App Store — dat helpt echt. Heb je feedback of een probleem? Mail ons via **support@everappz.com**. We lezen elk bericht.

## Veelgestelde vragen

{{% details title="Wat is er nieuw in Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 introduceert ondersteuning voor meer dan 10 nieuwe verbindingen (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), nieuwe afspeel-gebaren (dubbeltik om te zoeken, tik en houd vast voor 2x snelheid, één tik om bedieningselementen te wisselen), een heringerichte Wi-Fi Drive met selectiemodus en een slimmere uploadwachtrij, Liquid Glass-designupdates, bijgewerkte verbindingsbibliotheken en veel bugfixes.
{{% /details %}}

{{% details title="Werkt Evervideo met Plex?" closed="true" %}}
Ja. Vanaf Evervideo 1.7 kun je verbinden met een Plex Media Server en je volledige videobibliotheek streamen — films, tv-series en thuisvideo. Plex Media Server is gratis om te draaien; Plex Pass is optioneel. Evervideo ondersteunt zowel gratis als Plex Pass-opstellingen, inclusief direct play van MKV, MP4, AVI, MOV en andere formaten zonder hercoderen.
{{% /details %}}

{{% details title="Worden Jellyfin of Navidrome ondersteund in Evervideo?" closed="true" %}}
Ja. Zowel Jellyfin als Navidrome worden volledig ondersteund in Evervideo 1.7. Jellyfin is een gratis, open-source mediaserver die video en audio verwerkt. Navidrome is een gratis, open-source server die de Subsonic-API implementeert. Evervideo verbindt native met beide.
{{% /details %}}

{{% details title="Zijn Plex, Jellyfin, Emby, Navidrome en Subsonic gratis?" closed="true" %}}
- **Plex** — de server is gratis; Plex Pass is een optionele betaalde upgrade.
- **Jellyfin** — volledig gratis en open-source.
- **Emby** — de server is gratis; Emby Premiere is betaald en ontgrendelt mobiele synchronisatie en offline.
- **Navidrome** — volledig gratis en open-source.
- **Subsonic** — de officiële server kost $1/maand na een proefperiode van 30 dagen, maar de API is open en veel gratis servers (waaronder Navidrome) implementeren hem.
{{% /details %}}

{{% details title="Kan ik streamen vanaf mijn thuis-NAS over SFTP, FTP of NFS?" closed="true" %}}
Ja. Evervideo 1.7 voegt SFTP, FTP en NFS toe als native verbindingstypes. SFTP is de aanbevolen keuze voor streamen vanaf je eigen server over het open internet omdat al het verkeer via SSH wordt versleuteld. FTP en NFS kun je het best binnen je lokale netwerk of achter een VPN gebruiken.
{{% /details %}}

{{% details title="Hoe verbind ik Evervideo met een aangepaste server via SFTP?" closed="true" %}}
Open Evervideo, ga naar Verbindingen, kies SFTP en voer de hostnaam of het IP van je server in, de poort (meestal 22), gebruikersnaam en óf een wachtwoord óf een privé-SSH-sleutel. Evervideo bladert door je externe mappen en streamt videobestanden rechtstreeks met end-to-end-encryptie.
{{% /details %}}

{{% details title="Ondersteunt Evervideo Internxt en Proton Drive?" closed="true" %}}
Ja. Beide privacygerichte clouds worden ondersteund vanaf Evervideo 1.7. Ze sluiten zich aan bij MEGA en andere privacy-eerst-diensten die al beschikbaar zijn in de app.
{{% /details %}}

{{% details title="Hoe werken de nieuwe afspeel-gebaren?" closed="true" %}}
In volledig-scherm-video-afspeling: **dubbeltik op de rechterkant** om vooruit te springen en **dubbeltik op de linkerkant** om terug te springen met een instelbaar interval (standaard 10 seconden — wijzig het in Instellingen). **Tik en houd vast** ergens op het scherm om tijdelijk te versnellen naar 2x; laat los om terug te keren naar normaal. **Eén tik** ergens om de afspeel-bedieningselementen te wisselen (tonen of verbergen).
{{% /details %}}

{{% details title="Kan ik het sprong-interval van de dubbeltik wijzigen?" closed="true" %}}
Ja. Ga naar **Instellingen → Afspelen → Sprong-interval gebaar** en kies een waarde tussen 5 en 60 seconden. De meeste gebruikers houden het op 10 of 15 seconden.
{{% /details %}}

{{% details title="Wat is Wi-Fi Drive in Evervideo?" closed="true" %}}
Wi-Fi Drive is de ingebouwde draadloze bestandsoverdracht-functie van Evervideo. Hiermee kun je video's vanaf je computer naar je iPhone of iPad uploaden via je lokale Wi-Fi-netwerk — geen iTunes, geen kabels, geen cloud-account. Je kunt elke desktopbrowser of een WebDAV-client zoals Mac Finder of Windows Verkenner gebruiken. Zie de [volledige Wi-Fi Drive-handleiding](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Speelt Evervideo MKV, AVI en andere formaten af vanuit Plex of Jellyfin?" closed="true" %}}
Ja. Evervideo speelt vrijwel elk videoformaat — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — en streamt ze rechtstreeks vanuit Plex, Jellyfin, Emby en andere mediaservers zonder transcoderen voor de meeste codecs. Dit betekent lagere CPU-belasting op je server en snellere starttijden.
{{% /details %}}

{{% details title="Is bijwerken naar Evervideo 1.7 gratis?" closed="true" %}}
Ja. Evervideo is een gratis download in de App Store, en 1.7 is een gratis update voor alle bestaande gebruikers. De nieuwe cloud-integraties, mediaserver-ondersteuning, afspeel-gebaren, Wi-Fi Drive-verbeteringen en de Liquid Glass-UI horen bij de basisupdate.
{{% /details %}}

{{% details title="Op welke apparaten is Evervideo 1.7 beschikbaar?" closed="true" %}}
Evervideo 1.7 draait op iPhone, iPad en Mac. Met AirPlay en Chromecast kun je de afspeling naar een groter scherm casten. iCloud Drive-synchronisatie houdt je bibliotheek en instellingen consistent over apparaten heen.
{{% /details %}}
