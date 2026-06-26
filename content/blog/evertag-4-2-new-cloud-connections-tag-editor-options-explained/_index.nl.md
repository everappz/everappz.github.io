---
title: "Evertag 4.2: nieuwe cloud-verbindingen, tag-editor-instellingen uitgelegd"
date: 2026-05-09
description: "Evertag 4.2 voegt verbindingen toe met Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP en NFS, vernieuwt Wi-Fi Drive en past de interface aan voor Liquid Glass. Dit bericht legt ook elke tag-editor-instelling uit — inclusief ID3v2.4 vs ID3v2.3, schalen van albumhoes, dubbele tags, cloud-uploadmodi en de juiste opties voor Spotify en andere streamingdiensten."
keywords: ["Evertag 4.2", "Evertag update", "ID3 tag-editor iPhone", "ID3v2.4 vs ID3v2.3", "FLAC-tags bewerken iOS", "MP3-tags bewerken iPhone", "albumhoes bewerken iOS", "tag-editor voor Spotify", "tag-editor Plex", "tag-editor Apple Music", "Evertag cloud tag-editor", "Internxt tag-editor", "Proton Drive tag-editor", "QNAP tag-editor", "Nextcloud tag-editor", "Amazon S3 tag-editor", "SFTP tag-editor iPhone", "FTP audio tag-editor", "NFS tag-editor iPhone", "Wi-Fi Drive tag-editor", "ID3-tags dupliceren", "albumhoes schalen", "Liquid Glass design", "audiometadata-editor iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Tag-editor", "ID3", "ID3v2.4", "ID3v2.3", "FLAC-tags", "MP3-tags", "Albumhoes", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Wat is nieuw"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Korte samenvatting:** [Evertag 4.2](/products/evertag) is een grote update voor de audio-tag-editor op iPhone, iPad en Mac. We hebben belangrijke bugs in tag-bewerking opgelost en meer dan 6 nieuwe cloud- en serververbindingen toegevoegd — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, plus de protocollen **FTP**, **SFTP** en **NFS**. Wi-Fi Drive heeft een vernieuwde interface, een meervoudige selectiemodus, een slimmere uploadwachtrij en snellere overdrachten. De hele app is afgestemd op het **Liquid Glass**-design. Dit bericht duikt ook diep in Evertags tag-editor-instellingen — met uitleg over **ID3v2.4 vs ID3v2.3**, **schalen van albumhoes**, **dubbele tags**, **cloud-uploadmodi**, **gedownload bestand verwijderen** en precies welke opties je moet kiezen als je audio voorbereidt voor **Spotify**, **Apple Music**, **Plex**, **Jellyfin** of een andere streamingdienst.

---

## Hallo allemaal!

Een grote Evertag-update is er. We hebben belangrijke tag-bewerkingsbugs opgelost en **meer dan 6 nieuwe cloud- en serververbindingen** toegevoegd zodat het beheren van je audiometadata makkelijker is dan ooit — of je bibliotheek nu in een privacy-eerst-cloud staat, op een zelfgehoste NAS of op een generieke FTP/SFTP/NFS-server.

[Download Evertag 4.2 in de App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) of werk bij vanaf je huidige versie.

## Uitgebreide cloud- en serverondersteuning

Evertag verbindt nu native met een breder scala aan cloud- en zelfgehoste opslagopties. Je kunt ID3-, MP4-, FLAC-, OGG- en APE-tags bewerken op bestanden waar ze ook staan.

### Privacygerichte cloudopslag: Internxt en Proton Drive

Geef je om end-to-end-encryptie en zero-knowledge-opslag, dan zijn twee van de meest gerespecteerde privacy-eerst-clouds nu native in Evertag:

- **Internxt** — open-source, post-quantum versleutelde, AVG-conforme Spaanse cloud. Gratis abonnement beschikbaar.
- **Proton Drive** — end-to-end versleutelde opslag van de makers van Proton Mail en Proton VPN, gevestigd in Zwitserland. Gratis tier beschikbaar, met betaalde plannen voor grotere bibliotheken.

Je kunt nu metadata rechtstreeks bewerken op audiobestanden die in een van beide diensten zijn opgeslagen — het bestand blijft tijdens transport versleuteld en alleen de nieuwe tags worden teruggeschreven.

### Zelfgehoste oplossingen: QNAP, Nextcloud, Amazon S3

Voor gebruikers met eigen infrastructuur:

- **QNAP** — native API-verbinding met QNAP-NAS-apparaten. Bewerk tags op bestanden op je QNAP via lokaal Wi-Fi of op afstand.
- **Nextcloud** — verbind met elke zelfgehoste of beheerde Nextcloud-instantie.
- **Amazon S3** — wijs Evertag aan op elke S3-bucket (of S3-compatibele opslag zoals Backblaze B2, Wasabi, MinIO, Cloudflare R2) en bewerk metadata ter plekke.

### Nieuwe netwerkprotocollen: FTP, SFTP, NFS

Evertag 4.2 voegt drie klassieke protocollen toe voor gebruikers met eigen servers, homelabs of generieke NAS-apparaten:

- **SFTP (SSH File Transfer Protocol)** — het juiste antwoord voor **veilig tag-bewerken op afstand vanaf je eigen server**. SFTP draait bovenop SSH, dus de hele overdracht (authenticatie en audiogegevens) is versleuteld. Heb je een VPS, dedicated server of een Linux-machine thuis met SSH-toegang, dan kun je tags bewerken op externe bestanden zonder iets anders bloot te leggen. Ondersteunt zowel wachtwoord- als sleutel-authenticatie.
- **FTP** — de gevestigde standaard voor bestandsoverdracht. Handig voor oudere thuis-NAS-apparaten die FTP aanbieden maar geen native API hebben.
- **NFS (Network File System)** — het de-facto deelprotocol op Linux en de meeste NAS-apparaten. Minder overhead dan SMB op dezelfde hardware.

> **Tip:** SFTP is het protocol dat je wilt voor extern bewerken via het open internet. FTP en NFS gebruik je het best binnen je lokale netwerk — laat ze niet open op het internet staan, tenzij je ze door een VPN tunnelt.

## Wi-Fi Drive-verbeteringen

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) is de ingebouwde functie van Evertag om audiobestanden draadloos over te zetten tussen je computer en je iPhone of iPad — zonder iTunes, zonder kabels, zonder cloudaccount. Beide apparaten moeten op hetzelfde Wi-Fi-netwerk zitten.

In Evertag 4.2 krijgt Wi-Fi Drive:

- **Vernieuwde, moderne interface** — overzichtelijker, sneller leesbaar en bijgewerkt voor Liquid Glass.
- **Meervoudige selectiemodus** — kies meerdere bestanden of mappen en bewerk ze in bulk.
- **Slimmere uploadwachtrij** — betere voortgangsfeedback en bestand tegen netwerkonderbrekingen.
- **Verbeterde snelheid en algehele betrouwbaarheid** — snellere overdrachten voor grote bibliotheken.

Het is de snelste manier om een batch audiobestanden van je computer naar je telefoon te verplaatsen, hun tags te bewerken en ze terug te sturen — zonder externe diensten.

## Tag-editor-instellingen: een diepe duik

Dit is het deel dat de meeste gebruikers nooit lezen — en het deel dat bepaalt of je tags overal werken of slechts in sommige apps. Open Evertag en ga naar het gedeelte **audio-tag-editor-instellingen**. Hier staat wat elke optie precies doet en welke je moet kiezen afhankelijk van wat je wilt bereiken.

### Schalen van albumhoes

Wanneer je albumhoes opslaat in een audiobestand, kan Evertag de afbeelding verkleinen voor het inbedden. De beschikbare opties zijn:

- **Klein** — kleinste impact op bestandsgrootte, lagere beeldkwaliteit.
- **Middel** — uitgebalanceerde keuze voor de meeste gebruikers.
- **Groot** — hoge kwaliteit, geschikt voor afspelers met grote schermen en CarPlay.
- **Extra groot** — zeer hoge kwaliteit, merkbare toename van bestandsgrootte.
- **Origineel (Uitgeschakeld)** — bedt de hoes in op de oorspronkelijke resolutie. **Geen schaling.**

**Waarom dit ertoe doet:**

- **Hogere kwaliteit = grotere bestanden.** Een hoes van 3.000 × 3.000 pixels kan meerdere MB toevoegen aan elk nummer. Vermenigvuldigd met een heel album loopt de schijfimpact snel op.
- **Sommige afspelers gaan slecht om met heel grote ingebedde afbeeldingen.** Oudere apparaten, bepaalde auto-headunits en sommige legacy desktop-afspelers kunnen vastlopen bij hoezen boven ~1.500 px of weigeren ze te tonen.
- **Voor de meeste cloud- en streaming-workflows** is **Middel** of **Groot** de sweet spot. Gebruik **Origineel** alleen als je archiefkwaliteit nodig hebt of bestanden voorbereidt voor een afspeler die je vertrouwt.

> De **Origineel**-grootte maakt deel uit van Evertags premium personalisatie-upgrade. Standaardgroottes (Klein/Middel/Groot/Extra groot) zijn gratis.

### Tag-opslagopties: ID3v2.4 vs ID3v2.3

Dit is de belangrijkste instelling voor compatibiliteit. ID3v2 is het metadataformaat dat in MP3-bestanden wordt gebruikt. Er zijn twee veelgebruikte versies, en ze verschillen op subtiele maar belangrijke punten.

#### ID3v2.4

- Nieuwer, ondersteunt **UTF-8-tekstcodering** — correcte verwerking van niet-Latijnse schriften (Chinees, Russisch, Japans, Arabisch, Hebreeuws, enz.).
- Meer frame-types (relatief volume, equalizer-presets, enz.).
- **Aanbevolen voor moderne afspelers** die het ondersteunen.

#### ID3v2.3

- Ouder, maar **de universeelst ondersteunde ID3-versie**.
- Ondersteunt UTF-8 niet rechtstreeks (gebruikt UTF-16 voor Unicode-tekst).
- **Aanbevolen wanneer je maximale compatibiliteit nodig hebt** met oudere afspelers, autoradio's en bepaalde desktop-apps.

#### Wanneer ID3v2.4 in Evertag inschakelen

- Je gebruikt **moderne audio-afspelers** zoals Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (huidige versies) of moderne Android-spelers. ✅ **Zet ID3v2.4 AAN.**
- Je bibliotheek bevat **niet-Latijnse tekens** (Chinees, Koreaans, Japans, Russisch, Arabisch, Grieks, Hebreeuws). ✅ **Zet ID3v2.4 AAN** — UTF-8 verwerkt deze veel schoner.

#### Wanneer ID3v2.4 in Evertag uitschakelen (gebruik ID3v2.3)

- Je bereidt bestanden voor voor een **oudere autoradio of in-dash-unit** die geen v2.4-tags leest.
- Je ziet **vervormde tekst of ontbrekende tags** in sommige apps na het bewerken — dat is een sterk signaal dat v2.4 daar niet wordt ondersteund. Schakel terug naar v2.3.
- Je richt je op **legacy desktop-afspelers** of oudere draagbare spelers (vroege iPods, bepaalde MP3-spelers uit de jaren 2000–2010).

> **Vuistregel:** als je tags overal correct verschijnen met v2.4, laat het aan staan. Als zelfs één belangrijke afspeler verkeerde tekens, lege velden of geen tags toont, schakel v2.4 uit en sla opnieuw op.

#### Dubbele tags

Wanneer je **Dubbele tags** inschakelt, schrijft Evertag gemeenschappelijke metadatavelden (titel, artiest, album enz.) in **zowel ID3v1- als ID3v2-secties** van het bestand. Dit verbetert de compatibiliteit met zeer oude afspelers die alleen ID3v1 lezen (de oorspronkelijke 128-byte tag aan het einde van het bestand).

- **De meeste gebruikers hebben dit niet nodig.** Moderne afspelers lezen ID3v2 eerst.
- **Schakel het alleen in als** je werkt met vintage hardware of specifieke software die ID3v2 negeert.

### Online bestanden bijwerken: hoe Evertag cloud-bewerkingen afhandelt

Wanneer je tags bewerkt op een bestand dat is opgeslagen op een verbonden cloud (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP enz.), moet Evertag het gewijzigde bestand terug uploaden. Jij bepaalt hoe:

- **Bevestigingsmelding tonen** *(standaard, aanbevolen)* — Evertag vraagt vóór het uploaden. Het beste voor voorzichtige gebruikers en gedeelde bibliotheken.
- **Metadata van bestand automatisch bijwerken** — uploadt geluidloos na elke bewerking. Het beste voor solo-gebruikers met snelle, betrouwbare verbindingen die veel bewerken.
- **Metadata van bestand niet bijwerken** — Evertag bewerkt alleen de lokale kopie. Handig om wijzigingen te bekijken zonder ze door te zetten naar de cloud.

### Online bestanden bewerken: lokale bestandsopruiming

Om een extern bestand te bewerken, downloadt Evertag het eerst naar je apparaat. Na het bewerken kies je wat er met die lokale kopie gebeurt:

- **Gedownload bestand altijd verwijderen** — Evertag verwijdert het tijdelijke bestand na het bewerken. **Aanbevolen** als je krap zit qua opslag of werkt aan andermans bestanden.
- **Gedownload bestand niet verwijderen** — houdt het bewerkte bestand op je apparaat. Handig als je zowel een offline kopie als een bijgewerkte cloud-kopie wilt.

### Knoppen op het hoofdscherm

Het hoofdscherm van Evertags tag-editor kan knoppen voor afzonderlijke handelingen tonen of verbergen. Activeer alleen de knoppen die je echt gebruikt om de UI gefocust te houden:

- **Audio-tags automatisch zoeken** — vindt ontbrekende metadata online op basis van de audio-vingerafdruk van het bestand.
- **Audio-tags handmatig zoeken** — zoek op titel/artiest wanneer automatisch zoeken faalt.
- **Albumhoes zoeken** — vindt en bedt hoogwaardige hoezen in.
- **Albumhoes opslaan** — exporteert de ingebedde hoes naar je foto- of bestandsbibliotheek.
- **Codering normaliseren** — herstelt vervormde niet-Latijnse tekst veroorzaakt door oude coderingen (handig voor cyrillische, Chinese en Japanse tracks die met legacy-software zijn geript).
- **Audio-tags verwijderen** — verwijdert alle tags uit een bestand. Handig vóór een schone hertaggening.

### Uitgebreide tags tonen

Schakel dit in om alle metadatavelden te tonen voorbij het basisset titel/artiest/album/jaar — inclusief BPM, dirigent, oorspronkelijke artiest, sfeer, copyright, encoder, opmerkingen, songteksten en meer. Power-user-functie; de meeste casual gebruikers hebben dit niet nodig.

### Bestanden tegelijk bewerken

Wanneer ingeschakeld, laat Evertag je metadata bewerken op **meerdere geselecteerde bestanden tegelijk** — stel dezelfde album-artiest, jaar of genre in voor een heel album in één bewerking. Dit is de snelste manier om een grote, ongeordende bibliotheek op orde te brengen.

## Tags bewerken voor Spotify, Apple Music en streamingplatforms

Een veelgestelde vraag: «ik heb mijn tags bewerkt in Evertag, de bestanden geüpload, en de streamingdienst toont verkeerde metadata. Wat is er aan de hand?»

Kort antwoord: **streamingdiensten respecteren je lokale tags niet altijd**. Apple Music en Spotify hebben hun eigen interne databases — als ze een nummer herkennen, overschrijven ze de getoonde metadata met die van hen. Maar voor **geüploade bestanden**, je lokale bestanden (Apple Music's «Bibliotheek»-functie, Spotify Local Files) en **distributeur-uploads naar streamingplatforms** doen je tags er absoluut toe. Hier staat hoe je Evertag voor elk scenario instelt:

### Bestanden voorbereiden voor Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: AAN** — Apple Music gaat correct om met UTF-8.
- **Albumhoes: Groot** — Apple's apps tonen grote hoezen goed; Origineel is overdreven.
- **Dubbele tags: UIT** — niet nodig.
- Zorg dat **Album-artiest** correct is ingevuld — Apple Music gebruikt het voor groepering.

### Bestanden voorbereiden voor Spotify Local Files

Spotify Local Files toont alleen goed getagde bestanden. De tags die Spotify leest zijn beperkt.

- **ID3v2.4: AAN** in de meeste gevallen. Als een nummer na bewerken niet correct verschijnt in Spotify, **probeer dan op te slaan met ID3v2.4 UIT** (dus als ID3v2.3) — de parser van Spotify is historisch terughoudend geweest met v2.4.
- **Albumhoes: Middel of Groot** — Spotify schaalt de hoes toch.
- Vul minstens **Titel**, **Artiest**, **Album** en **Tracknummer** in.

### Bestanden voorbereiden voor distributeur-upload (DistroKid, TuneCore, CD Baby enz.)

Als je als artiest je eigen werk uploadt naar streamingplatforms, leest je distributeur meestal de tags maar vraagt ook metadata in zijn UI. Hoe dan ook:

- **ID3v2.3** is vaak de veiliger standaardkeuze — veel distributeur-pijplijnen zijn jaren geleden gebouwd en geven de voorkeur aan het oudere formaat.
- Bed **Grote** hoes in (de meeste distributeurs eisen ≥ 1.400 × 1.400 px — controleer hun richtlijnen).
- Vertrouw niet op uitgebreide tags — distributeurs lezen alleen de basisvelden.

### Bestanden voorbereiden voor Plex, Jellyfin, Navidrome, Subsonic, Emby

Deze zelfgehoste mediaservers zijn zeer tolerant. Ze lezen zowel v2.3 als v2.4 schoon en gaan goed om met UTF-8.

- **ID3v2.4: AAN** is prima.
- **Albumhoes: Groot** of **Extra groot** — deze servers leveren hoezen aan mobiele clients en CarPlay-schermen, dus kwaliteit telt.
- **Album-artiest** sterk aanbevolen — daarop groeperen Plex/Jellyfin albums per artiest correct.

### Bestanden voorbereiden voor autoradio's en oudere hardware

- **ID3v2.4: UIT** (gebruik ID3v2.3) — oudere headunits ondersteunen v2.4 vaak niet.
- **Albumhoes: Middel** — veel autodisplays lopen vast op grote ingebedde hoezen.
- **Dubbele tags: AAN** — oudere autoradio's lezen soms alleen de ID3v1-fallback.

## Andere verbeteringen

### Liquid Glass-design

De interface van Evertag 4.2 is afgestemd op Apple's nieuwe **Liquid Glass**-materiaal in de hele app — doorschijnende oppervlakken, soepelere animaties en verfijnde knoppen die natuurlijk passen in iOS, iPadOS en macOS.

### Bijgewerkte verbindingsbibliotheken

We hebben de onderliggende bibliotheken die Evertag gebruikt om te praten met **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** en andere diensten ververst. Het resultaat: minder verbindingsfouten in randgevallen, betere ondersteuning voor recentere serverversies en meer betrouwbaarheid bij het bewerken van tags op externe bestanden.

### Vertaling- en lokalisatiefixes

Meerdere taalfixes in de UI op basis van directe feedback van gebruikers. Betere tekstpassing op kleinere knoppen in verschillende talen.

### Kleinere verfijningen geïnspireerd op jouw feedback

Veel kleinere verbeteringen op basis van App Store-reviews en e-mails naar support@everappz.com. We lezen elk bericht.

## Pak Evertag 4.2

[**Download Evertag in de App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) of werk bij via de App Store. Evertag is een gratis download met optionele in-app upgrades voor geavanceerde functies. De nieuwe cloud-verbindingen, netwerkprotocollen, Wi-Fi Drive-verbeteringen en de Liquid Glass-UI horen bij de basisupdate.

Vind je de app leuk? Laat dan een beoordeling achter in de App Store — dat helpt echt. Heb je feedback of een probleem? Mail ons via **support@everappz.com**. We lezen elk bericht.

## Veelgestelde vragen

{{% details title="Wat is er nieuw in Evertag 4.2?" closed="true" %}}
Evertag 4.2 voegt meer dan 6 nieuwe cloud- en serververbindingen toe (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), een vernieuwde Wi-Fi Drive met meervoudige selectie en een slimmere uploadwachtrij, Liquid Glass-UI-updates, bijgewerkte verbindingsbibliotheken, belangrijke fixes in tag-bewerking en vertaalverbeteringen.
{{% /details %}}

{{% details title="Moet ik in Evertag ID3v2.4 of ID3v2.3 gebruiken?" closed="true" %}}
Gebruik **ID3v2.4** voor moderne afspelers (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, moderne Android-apps) en voor bibliotheken met niet-Latijnse tekens — UTF-8-ondersteuning betekent schonere tags in Chinees, Koreaans, Japans, Russisch, Arabisch en Hebreeuws. Gebruik **ID3v2.3** als je tags niet correct worden weergegeven in sommige apps, als je oudere autoradio's bedient of als een streaming-distributeur-pijplijn v2.4 weigert. Je kunt altijd wisselen en opnieuw opslaan.
{{% /details %}}

{{% details title="Waarom kloppen mijn tags niet in Spotify na het bewerken?" closed="true" %}}
Spotify toont vooral metadata uit zijn eigen catalogus — je lokale tags worden alleen gebruikt voor «Local Files» of voor inhoud die je als artiest hebt geüpload. Als je bestanden tagt voor Spotify Local Files en ze niet correct verschijnen, probeer dan ID3v2.4 in Evertag uit te schakelen en als ID3v2.3 op te slaan — Spotify's parser is historisch terughoudend geweest met v2.4.
{{% /details %}}

{{% details title="Welke albumhoesgrootte moet ik kiezen in Evertag?" closed="true" %}}
Voor de meeste gebruikers: **Groot**. Het ziet er prima uit op telefoons, iPads, Macs en moderne autodisplays zonder de bestanden te veel op te blazen. Gebruik **Middel** als je een enorme bibliotheek hebt en schijfruimte wilt sparen. Gebruik **Origineel** (geen schaling) alleen voor archiefmasters of wanneer je echt maximale kwaliteit nodig hebt — let op dat sommige oudere afspelers moeite hebben met zeer grote ingebedde hoezen. **Origineel** maakt deel uit van Evertags premium personalisatie-upgrade.
{{% /details %}}

{{% details title="Worden mijn bestanden groter door grotere albumhoezen?" closed="true" %}}
Ja. Een hoes van 3.000 × 3.000 px inbedden kan meerdere megabytes toevoegen aan een enkel audiobestand. Over een bibliotheek van 1.000 nummers loopt dat op tot gigabytes. Bij krappe opslag gebruik Middel of Groot; als je vanuit een NAS streamt waar grootte er niet toe doet, zijn Extra groot of Origineel prima.
{{% /details %}}

{{% details title="Wat zijn dubbele tags en moet ik die inschakelen?" closed="true" %}}
Dubbele tags schrijven de kernmetadata in zowel de ID3v1- (legacy 128-byte) als ID3v2-secties (modern) van het bestand. Schakel het alleen in als je je richt op zeer oude afspelers of hardware die ID3v1 leest. Voor alles wat modern is (smartphones, computers, recente autoradio's) laat je het uit.
{{% /details %}}

{{% details title="Bewerkt Evertag tags rechtstreeks op cloudbestanden?" closed="true" %}}
Ja. Verbind met je cloud (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 enz.) of via FTP/SFTP/NFS, open een bestand en bewerk tags alsof het lokaal is. Evertag downloadt het bestand, past je wijzigingen toe en uploadt de bijgewerkte versie terug. Je kunt in de instellingen kiezen tussen «Altijd vragen», «Auto-upload» of «Niet uploaden».
{{% /details %}}

{{% details title="Kan ik FLAC-tags op iPhone bewerken met Evertag?" closed="true" %}}
Ja. Evertag ondersteunt FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE en andere belangrijke formaten met volledige lees-/schrijfondersteuning voor tags inclusief ingebedde hoes.
{{% /details %}}

{{% details title="Hoe bewerk ik tags veilig op mijn thuiserver met SFTP?" closed="true" %}}
Open Evertag, ga naar Verbindingen, kies SFTP en voer de hostnaam of IP van je server in, de poort (meestal 22), gebruikersnaam en óf een wachtwoord óf een privé-SSH-sleutel. Evertag bladert door je externe mappen en bewerkt tags rechtstreeks met end-to-end-encryptie via SSH.
{{% /details %}}

{{% details title="Kan ik tags op meerdere bestanden tegelijk bewerken?" closed="true" %}}
Ja. Schakel **Bestanden tegelijk bewerken** in de instellingen in. Selecteer meerdere bestanden, open de tag-editor en elk veld dat je wijzigt wordt toegepast op alle geselecteerde bestanden. Het is de snelste manier om dezelfde album-artiest, jaar of genre op een heel album in te stellen.
{{% /details %}}

{{% details title="Is bijwerken naar Evertag 4.2 gratis?" closed="true" %}}
Ja. Evertag is een gratis download in de App Store, en 4.2 is een gratis update voor alle bestaande gebruikers. De nieuwe cloud-integraties, Wi-Fi Drive-verbeteringen en Liquid Glass-UI horen bij de basisupdate.
{{% /details %}}

{{% details title="Op welke apparaten is Evertag 4.2 beschikbaar?" closed="true" %}}
Evertag 4.2 draait op iPhone, iPad en Mac. iCloud Drive-synchronisatie houdt je tag-editor-instellingen consistent over apparaten heen.
{{% /details %}}
