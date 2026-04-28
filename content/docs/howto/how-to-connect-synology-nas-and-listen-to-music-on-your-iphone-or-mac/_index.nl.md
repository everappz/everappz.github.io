---
title: "Hoe u Synology NAS aansluit en muziek beluistert op uw iPhone of Mac"
date: 2024-09-19
description: "Leer hoe u uw Synology NAS verbindt met de native API of QuickConnect en muziek van hoge kwaliteit streamt naar uw iPhone of Mac met Evermusic en Flacbox."
keywords: ["synology nas", "muziek streamen", "quickconnect", "evermusic synology", "flacbox synology", "nas muziekspeler", "iphone nas muziek"]
tags: ["muziek", "streaming", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Samenvatting:** Verbind uw Synology NAS met Evermusic of Flacbox via Synology's native API -- handmatig via IP-adres of automatisch via QuickConnect ID. Met QuickConnect kunt u op afstand muziek streamen zonder port forwarding. Beide apps ondersteunen FLAC, MP3, WAV en andere hi-res formaten.

Als u op zoek bent naar een naadloze manier om uw Synology NAS te verbinden en van uw muziekbibliotheek te genieten op uw iPhone of Mac, dan zijn de Evermusic en Flacbox apps de perfecte oplossingen. Deze apps ondersteunen een breed scala aan audioformaten, waaronder FLAC, MP3 en WAV, waardoor het eenvoudig is om muziek van hoge kwaliteit rechtstreeks vanaf uw Synology NAS te streamen en te beluisteren.

In deze handleiding laten we u zien hoe u uw Synology NAS verbindt met de Evermusic of Flacbox app met behulp van Synology's native API en QuickConnect-functie. Door gebruik te maken van Synology's directe API kunt u uw muziekbibliotheek veilig benaderen buiten uw thuisnetwerk zonder ingewikkelde configuraties zoals WebDAV, SMB, DLNA. Met QuickConnect kunt u uw muziek overal streamen en beheren, met uw iPhone of Mac.

## Stap 1: Machtigingen voor gedeelde mappen configureren (optioneel)

1. Open het **Configuratiescherm** en ga naar het gedeelte **Gedeelde map**.

![Gedeelde map](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Selecteer de map **Music** en klik op **Bewerken**.

3. Configureer in het tabblad **Machtigingen** de machtigingen. Schakel gasttoegang in met Alleen-lezen als u alleen muziek wilt beluisteren, of Lezen/Schrijven als u bestanden wilt wijzigen. Sla de wijzigingen op.

![Machtigingen](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Stap 2: Synology NAS IP-adres vinden

1. Open het **Configuratiescherm** en ga naar het tabblad **Netwerkinterface**.

![Netwerkinterface](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Of gebruik uw webbrowser om [find.synology.com](http://find.synology.com) te bezoeken.

![Synology zoeken](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Noteer het IP-adres van uw Synology NAS (bijv. 192.168.18.137).

## Stap 3: Synology NAS netwerkpoorten vinden

U kunt de officiële Synology-documentatie voor standaard DSM-netwerkpoorten vinden in dit [Synology Knowledge Center-artikel](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM gebruikt de volgende standaardpoorten:
- **HTTP (Webtoegang):** Poort **5000**
- **HTTPS (Beveiligde webtoegang):** Poort **5001**

Dit zijn de standaardpoorten voor toegang tot de DSM-interface.

![Netwerkpoorten](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Stap 4: QuickConnect ID-functie inschakelen

Een Synology QuickConnect ID is een unieke identificatiecode waarmee u op afstand toegang hebt tot uw Synology NAS via internet zonder ingewikkelde netwerkinstellingen zoals port forwarding te hoeven configureren. QuickConnect vereenvoudigt externe toegang door Synology's servers te gebruiken om een verbinding tot stand te brengen tussen uw NAS en uw apparaat, zoals uw smartphone of computer, via de QuickConnect ID.

**Hoe u uw QuickConnect ID vindt of instelt:**

1. **Meld u aan bij DSM.**
2. Ga naar **Configuratiescherm > Externe toegang > QuickConnect**.
3. **Schakel QuickConnect in** en maak uw unieke QuickConnect ID aan of bekijk deze.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Stap 5: Verbinding maken met Synology NAS op uw iPhone/Mac met Evermusic of Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) en [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) zijn beide muziekspeler-apps ontworpen voor iOS- en macOS-apparaten, elk met unieke functies en mogelijkheden voor het beheren en genieten van uw muziekbibliotheek.

1. Open de Evermusic of Flacbox app en ga naar het tabblad **Verbindingen**.

![Verbindingen](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Kies **Een cloudservice verbinden** en selecteer **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

U hebt twee verbindingsopties: **handmatig** met het IP-adres en de poort van de server, of **automatisch** via QuickConnect ID.

### Handmatige verbinding

Voor de handmatige methode hebt u het directe IP-adres en poortnummer nodig die u in eerdere stappen hebt verkregen.

1. Voer de server-URL in die u in stap 2 hebt verkregen, in het volgende formaat: PROTOCOL://IP_ADRES:POORTNUMMER
   - Gebruik **poort 5000** voor HTTP en **poort 5001** voor HTTPS-verbindingen.

   Bijvoorbeeld:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Het werkelijke poortnummer kan worden bevestigd in stap 3 van uw installatie.
3. Voer uw **gebruikersnaam** en **wachtwoord** in voor de Synology NAS.
4. Tik op **Aanmelden** om de verbinding tot stand te brengen.

![Handmatige verbinding](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automatische verbinding

Voor de automatische verbinding gebruikt u de **QuickConnect ID** uit stap 4. In plaats van handmatig het IP-adres en poortnummer voor uw Synology NAS in te voeren, voert u gewoon de **QuickConnect ID** in. De app haalt automatisch de benodigde verbindingsinformatie op.

Met deze methode kunt u op afstand toegang krijgen tot uw NAS, zelfs buiten uw thuisnetwerk, zodat u uw bestanden kunt beheren vanaf internet zonder port forwarding of statische IP-adressen te hoeven configureren.

![Automatische verbinding](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Tweefactorauthenticatie

Vanaf DSM 4.2 heeft Synology **tweestapsverificatie** geïntroduceerd om de beveiliging te verbeteren. Deze functie vereist een **eenmalig wachtwoord (OTP)**-code, gegenereerd door een authenticator-app, naast uw reguliere inloggegevens. Als u tweestapsverificatie hebt ingeschakeld, moet u na het invoeren van uw gebruikersnaam en wachtwoord ook de OTP invoeren om in te loggen bij uw DSM-sessie.

Let op: zodra uw sessie verloopt, moet de app handmatig opnieuw worden geautoriseerd. Om opnieuw te autoriseren:

1. Ga naar het tabblad **Verbindingen** in de app.
2. Tik op de knop **Meer acties** naast de servernaam.
3. Selecteer **Instellingen** in het menu om de nieuwe authenticatiecode in te voeren en het herautorisatieproces te voltooien.

Dit zorgt ervoor dat uw gegevens veilig blijven, zelfs wanneer u uw NAS benadert vanaf een onvertrouwd netwerk.

## Stap 6: Navigeren en muziek afspelen

1. Eenmaal verbonden verschijnt het apparaat in de lijst **Verbonden apparaten**.

![Verbonden apparaten](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navigeer naar de map **Music** en tik op een audiobestand om het afspelen te starten.

![Muziek afspelen](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Stap 7: Verbonden cloudmap toevoegen aan muziekbibliotheek

1. Open het gedeelte **Muziekbibliotheek** in de app.
2. Kies **Muziek toevoegen** en selecteer **Verbindingen**.
3. Kies uw verbonden NAS-server en selecteer de map **Music**. Tik op **Voltooid**.
4. De app scant de muziekmap en voegt ondersteunde audiobestanden toe aan de muziekbibliotheek. Metadata wordt geladen en uw tracks worden gegroepeerd op album, artiest en genre.

## Conclusie

Door deze stappen te volgen kunt u eenvoudig een verbinding instellen op uw Synology NAS en uw volledige muziekbibliotheek streamen naar uw iPhone of Mac met Evermusic of Flacbox. Of u nu thuis bent of onderweg, geniet van naadloze, hoogwaardige toegang tot uw favoriete tracks vanaf elke locatie met QuickConnect. Profiteer van de flexibiliteit en het gemak die deze apps bieden en begin uw muziekcollectie eenvoudig te beheren op al uw apparaten.

Met veilige externe toegang via QuickConnect en ondersteuning voor een breed scala aan audioformaten bent u nooit ver van uw muziek. Nu zijn uw op NAS opgeslagen bestanden slechts een tik verwijderd!

## FAQ

{{% details title="Wat is het verschil tussen handmatige verbinding en QuickConnect?" closed="true" %}}
Handmatige verbinding gebruikt het NAS IP-adres en de poort, wat werkt op uw lokale netwerk. QuickConnect gebruikt Synology's relayservice om een verbinding tot stand te brengen vanaf elke locatie via internet, zonder port forwarding.
{{% /details %}}

{{% details title="Kan ik muziek streamen vanaf Synology NAS buiten mijn thuisnetwerk?" closed="true" %}}
Ja. Schakel QuickConnect in op uw Synology NAS en gebruik de QuickConnect ID in Evermusic of Flacbox om muziek te streamen vanaf elke locatie met een internetverbinding.
{{% /details %}}

{{% details title="Welke audioformaten worden ondersteund bij het streamen vanaf Synology NAS?" closed="true" %}}
Evermusic en Flacbox ondersteunen FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD en vele andere formaten. Alle ondersteunde formaten werken bij het streamen vanaf Synology NAS.
{{% /details %}}

{{% details title="Heb ik tweefactorauthenticatie nodig om verbinding te maken?" closed="true" %}}
Nee, 2FA is optioneel. Als u echter tweestapsverificatie hebt ingeschakeld op uw Synology DSM, zal de app om een eenmalig wachtwoord vragen tijdens het inloggen. U moet opnieuw autoriseren wanneer de sessie verloopt.
{{% /details %}}

{{% details title="Moet ik Synology native API, WebDAV of SMB gebruiken om verbinding te maken?" closed="true" %}}
De Synology native API met QuickConnect is de beste keuze voor externe toegang. Voor lokaal netwerkgebruik is SMB doorgaans de snelste optie. WebDAV werkt goed voor zowel lokale als externe toegang. Evermusic en Flacbox ondersteunen alle drie de protocollen.
{{% /details %}}
