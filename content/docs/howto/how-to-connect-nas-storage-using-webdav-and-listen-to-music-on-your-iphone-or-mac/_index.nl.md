---
title: "Hoe NAS-opslag verbinden via WebDAV en muziek luisteren op je iPhone of Mac"
date: 2024-07-28
description: "Leer hoe je WebDAV configureert op je Synology NAS en muziek streamt naar je iPhone of Mac met Evermusic of Flacbox. Volg onze stapsgewijze handleiding."
keywords: ["nas verbinden", "webdav synology", "muziek streamen nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["muziek", "streaming", "opslag", "nas", "verbinden", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Samenvatting:** Installeer en activeer WebDAV op je Synology NAS, configureer de machtigingen van de gedeelde map en maak vervolgens verbinding vanuit Evermusic of Flacbox met het IP-adres van de NAS en de WebDAV-poort (standaard 5005/5006). Je kunt je hele muziekbibliotheek streamen en beheren zonder bestanden naar je apparaat te kopiëren.

Ontdek hoe je je NAS-opslag verbindt via WebDAV en moeiteloos je muziekbibliotheek streamt naar je iPhone of Mac. WebDAV (Web-based Distributed Authoring and Versioning) is een protocol waarmee je bestanden kunt beheren en delen via internet. Door WebDAV in te stellen op je NAS, kun je je muziekcollectie openen en streamen, zodat je favoriete nummers altijd binnen handbereik zijn.

In deze handleiding laten we je zien hoe je een WebDAV-verbinding instelt op een van de populairste NAS-servers, Synology NAS. Volg onze eenvoudige stappen om WebDAV te configureren op je Synology NAS, en je kunt je muziekbibliotheek rechtstreeks vanaf je iPhone of Mac bladeren, streamen en beheren.

## Stap 1: WebDAV installeren op Synology NAS

1. Log in op je Synology NAS en open het **Pakketcentrum**.
2. Zoek naar "webdav" en installeer het WebDAV-pakket als het nog niet is geïnstalleerd. Open de WebDAV-server om deze te configureren.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="WebDAV installeren op Synology" width="600" >}}

## Stap 2: WebDAV-server configureren

1. Vink op de WebDAV-instellingenpagina de vakjes aan voor **HTTP inschakelen**, **HTTPS inschakelen**, **Anoniem WebDAV inschakelen** en **DavDepthInfinity inschakelen**.
2. Klik op **Toepassen** om de wijzigingen op te slaan. Noteer de poortnummers voor HTTP- en HTTPS-verbindingen, die standaard 5005 en 5006 zijn.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="WebDAV-instellingen configureren" width="600" >}}

## Stap 3: Machtigingen van gedeelde map configureren

1. Open het **Configuratiescherm** en ga naar de sectie **Gedeelde map**.
2. Selecteer de map **Muziek** en klik op **Bewerken**.
3. Configureer in het tabblad **Machtigingen** de machtigingen. Schakel gasttoegang in met Alleen-lezen als je alleen muziek wilt luisteren, of Lezen/Schrijven als je bestanden wilt wijzigen. Sla de wijzigingen op.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Machtigingen van gedeelde map" width="600" >}}

## Stap 4: IP-adres van Synology NAS vinden

1. Open het **Configuratiescherm** en ga naar het tabblad **Netwerkinterface**, of gebruik je webbrowser om [find.synology.com](http://find.synology.com) te bezoeken.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="NAS IP-adres vinden" width="600" >}}

2. Noteer het IP-adres van je Synology NAS (bijv. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP-adres" width="600" >}}

## Stap 5: Verbinden met Synology NAS via Evermusic/Flacbox

1. Open de Evermusic- of Flacbox-app en ga naar het tabblad **Verbindingen**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Tabblad Verbindingen in Evermusic" width="600" >}}

2. Voor automatische verbinding, zoek je Synology NAS in de sectie **Beschikbare apparaten** en tik erop om verbinding te maken.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Lijst met beschikbare apparaten" width="600" >}}

3. Voor handmatige verbinding, kies **Verbind een cloudservice** en selecteer **WebDAV**. Voer het serveradres in het formaat in: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (bijv. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Handmatige WebDAV-configuratie" width="600" >}}

4. Laat de inlog- en wachtwoordvelden leeg voor gasttoegang, of voer je Synology-inloggegevens in. Tik op **Inloggen**.

## Stap 6: Navigeren en muziek afspelen

1. Na verbinding verschijnt het apparaat in de lijst **Verbonden accessoires**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Verbonden apparaten in Evermusic" width="600" >}}

2. Navigeer naar de map **Muziek** en tik op een audiobestand om het afspelen te starten.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Door de muziekmap bladeren" width="600" >}}

## Stap 7: Verbonden cloudmap toevoegen aan muziekbibliotheek

1. Open de sectie **Muziekbibliotheek** in de app.
2. Kies **Muziek toevoegen** en selecteer **Verbindingen**.
3. Kies je verbonden NAS-server en selecteer de map **Muziek**. Tik op **Voltooid**.
4. De app scant de muziekmap en voegt ondersteunde audiobestanden toe aan de muziekbibliotheek. Metadata worden geladen en je nummers worden gegroepeerd op album, artiest en genre.

## Conclusie

Door deze stappen te volgen, kun je eenvoudig een WebDAV-verbinding instellen op je Synology NAS en je muziekbibliotheek streamen naar je iPhone of Mac met Evermusic of Flacbox. Geniet van naadloze toegang tot je favoriete nummers op elk moment.

## Veelgestelde vragen

{{% details title="Welke NAS-apparaten ondersteunen WebDAV?" closed="true" %}}
De meeste populaire NAS-merken ondersteunen WebDAV, waaronder Synology, QNAP, TrueNAS en Western Digital. Raadpleeg de documentatie van je NAS-fabrikant voor WebDAV-installatie-instructies.
{{% /details %}}

{{% details title="Wat is het verschil tussen WebDAV en SMB voor het streamen van muziek vanaf NAS?" closed="true" %}}
WebDAV werkt via HTTP/HTTPS en is beter geschikt voor externe toegang via internet. SMB is doorgaans sneller op lokale netwerken. Evermusic en Flacbox ondersteunen beide protocollen, dus kies op basis van of je lokale of externe toegang nodig hebt.
{{% /details %}}

{{% details title="Heb ik een gebruikersnaam en wachtwoord nodig voor WebDAV op Synology?" closed="true" %}}
Nee, als je anonieme WebDAV-toegang inschakelt en gastmachtigingen configureert voor je gedeelde map. Voor betere beveiliging kun je in plaats daarvan je Synology-inloggegevens gebruiken.
{{% /details %}}

{{% details title="Kan ik FLAC en andere hi-res formaten streamen vanaf NAS via WebDAV?" closed="true" %}}
Ja. Zowel Evermusic als Flacbox ondersteunen FLAC, ALAC, WAV, DSD en andere hoge-resolutieformaten bij het streamen vanaf NAS-opslag via WebDAV.
{{% /details %}}

{{% details title="Waarom kan de app mijn NAS niet vinden in Beschikbare apparaten?" closed="true" %}}
Zorg ervoor dat je iPhone/Mac en NAS zich op hetzelfde Wi-Fi-netwerk bevinden. Als automatische detectie niet werkt, gebruik dan de handmatige verbindingsoptie en voer het NAS IP-adres en de WebDAV-poort rechtstreeks in.
{{% /details %}}
