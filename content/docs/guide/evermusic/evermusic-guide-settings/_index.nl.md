---
title: "Instellingen"
date: 2020-01-01
description: "Verken alle instellingen in Evermusic, inclusief audioconfiguratie, muziekbibliotheeKsynchronisatie, offline mappen, metadata, personalisatie, toegankelijkheid, widgets, CarPlay en back-upopties."
keywords: [
  "Evermusic", "instellingen", "audio-instellingen", "muziekbibliotheeKsynchronisatie",
  "offline mappen", "equalizer", "crossfade", "gapless afspelen",
  "audioverwerker", "afspeellijstinstellingen", "premium upgrade",
  "aankopen herstellen", "bestandsbeheerder", "tag-editor", "WiFi drive",
  "voiceover", "app back-up", "toegankelijkheid", "lokalisatie",
  "widgets", "CarPlay", "ruimtelijk geluid", "audiotoonhoogte"
]
tags: ["evermusic", "gids", "instellingen"]
readingTime: 16
---


Het Instellingenscherm is het controlecentrum van Evermusic. Van hieruit kunt u upgraden naar Premium, de audiospeler configureren, uw muziekbibliotheek beheren, de bestandsbeheerder instellen, de interface aanpassen, widgets en CarPlay inschakelen, een back-up van uw gegevens maken en help- en juridische informatie raadplegen. Secties zijn gegroepeerd onder headers: **Aankopen & updates**, app-voorkeuren, **Help** en **Juridisch & privacy**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic instellingenscherm" image="/docs/guide/evermusic/evermusic-guide-settings/img/settings-main-screen.webp" >}}
{{< /cards >}}

## Aankopen & Updates

### Upgraden naar Premium

Upgrade de applicatie naar de Premium-versie om alle beperkingen te verwijderen. De gratis versie biedt één lifetime in-app aankoop en twee abonnementsopties die de volledige functieset ontgrendelen.

Gezinsdeling is ingeschakeld voor alle aankopen en plannen, zodat u de Premium-versie kunt delen met leden van uw gezin.

U kunt meer lezen over aankopen en de Premium-versie hier: [Wat is het verschil tussen Evermusic en Evermusic Premium](/docs/faq/evermusic/what-is-the-difference-between-evermusic-and-evermusic-premium/).

#### Evermusic Free (Blauw pictogram) vs Evermusic Pro (Rood pictogram)

Evermusic is gepubliceerd in de App Store onder twee verschillende pictogrammen / kleuren:

- **Evermusic Free (blauw pictogram)** is opgesplitst in **twee afzonderlijke App Store-apps met verschillende bundle-ID's** — één voor **iOS / iPadOS** en een speciale voor **macOS** (Universele binaire code die zowel op **Apple Silicon als Intel Macs** werkt). Premium in-app aankopen worden **gedeeld tussen de iOS- en Mac blauwe apps via iCloud** — koop Premium op iPhone en het wordt automatisch geactiveerd op de Mac (en vice versa), zolang beide apparaten hetzelfde Apple ID met iCloud ingeschakeld gebruiken.
- **Evermusic Pro (rood pictogram)** is een **enkele App Store-app** met een **enkele bundle-ID** die werkt op **iPhone, iPad en Apple Silicon Macs (M1 en later)**. Het heeft **dezelfde functionaliteit als Evermusic Free met een geactiveerd Premium-plan**. De rode app **ondersteunt geen Intel Macs**, waardoor de prijs iets lager is dan de equivalente Premium-aankoop in de blauwe app. Evermusic Pro **verzamelt ook helemaal geen gebruikersdiagnostiek of analytics** — analytics zijn volledig uitgeschakeld in de build, zonder opt-in-optie.

Omdat de bundle-ID's verschillen tussen blauw en rood, ontgrendelt een Premium in-app aankoop geactiveerd in de blauwe app de rode app niet gratis, en vice versa. Als u de blauwe app al gebruikt met Premium geactiveerd, is er geen reden om de rode app te installeren — u heeft al alles wat Pro biedt.

### Aankopen delen tussen iOS en Mac

Lifetime-aankopen en abonnementen worden gedeeld tussen iOS en Mac via iCloud. Als u al Premium op iOS bezit, zorg er dan voor dat u de nieuwste versie heeft geïnstalleerd en dat iCloud is ingeschakeld. Start de app op iOS en wacht een minuut totdat uw aankoopinformatie naar iCloud is geüpload.

U kunt ook op **Aankopen herstellen** tikken in de app-instellingen. Installeer daarna de nieuwste app-versie van de App Store op uw Mac en start de app. Zorg ervoor dat u een internetverbinding heeft en bent ingelogd met hetzelfde iCloud- en App Store-account op beide apparaten. Wacht een minuut totdat de app aankoopinformatie van iCloud heeft gedownload. De Premium-versie moet automatisch op uw Mac worden geactiveerd.

### Aankopen herstellen op een nieuw apparaat

Om uw aankoop op een nieuw apparaat te herstellen, gebruikt u **Aankopen → Aankopen herstellen**. U ziet de lijst met uw aankopen. Als er iets ontbreekt, controleer dan of het apparaat is verbonden met hetzelfde iTunes-account dat is gebruikt voor de aankopen en of iCloud is ingeschakeld.

### Premium gratis proberen

U kunt voor een beperkte tijd gratis upgraden naar de Premium-versie via dit menu. Bekijk een korte advertentie of deel de app met vrienden om Premium tijdelijk te ontgrendelen.

### Aankopen

Herstel eerdere aankopen via dit menu. Als u activeringsfouten ondervindt, probeer dan de optie **Aankopen herstellen bij app-start** in te schakelen.

### Software-update

Tik op **Software-update** om te controleren of er een nieuwere versie van Evermusic beschikbaar is. De app vergelijkt uw geïnstalleerde versie met de nieuwste versie in de App Store en laat u weten of een update wordt aanbevolen.

### Wat is er nieuw

Dit menu wordt beschikbaar nadat een nieuwe versie is uitgebracht. Het toont een samenvatting van de wijzigingen en nieuwe functies in de meest recente update.

## Audiospelerinstellingen

Alle audiospelerinstellingen zijn hier gegroepeerd: equalizer, crossfade-afspelen, audiospelercache, laden van nummers en meer. Instellingen zijn georganiseerd in logische subsecties.

### Algemeen

Deze subsectie bevat algemene instellingen voor afspeelwachtrij, audio-uitvoer en het opslaan van staat.

#### Herhaalmodus

Specificeert het gedrag van de audiospeler wanneer een nummer klaar is met afspelen:

- **Alles herhalen** – herhaalt alle nummers in uw speler-wachtrij.
- **Eén herhalen** – herhaalt alleen het huidige nummer.
- **Herhalen stoppen** – pauzeert het afspelen wanneer het huidige nummer eindigt.
- **Niet herhalen** – laat uw wachtrij afspelen zonder herhaling.

#### Willekeurige modus

Speelt nummers af in een willekeurige volgorde. Dit schudt de wachtrij en speelt nummers één voor één af in de nieuwe volgorde. Beschikbare waarden: **Willekeurig uit** en **Willekeurig aan**.

#### Audioverwerker

Mogelijke waarden: **AVFoundation** en **CoreAudio**. Standaard wordt AVFoundation gebruikt. Vanwege een bekend probleem met AVFoundation op iOS 17.0–17.6 kunnen crossfade-afspelen en de audio-equalizer niet tegelijkertijd worden gebruikt. Om zowel crossfade als de equalizer op die iOS-versies te genieten, schakelt u over naar de CoreAudio-audioverwerker.

Als u problemen ondervindt met gapless afspelen via AVFoundation, probeer dan ook CoreAudio. De enige beperkingen van CoreAudio zijn internetstreaming van sommige radiostations en bepaalde audioformaten, omdat het niet elk systeemaudioformaat ondersteunt (zoals M4A en een paar andere).

#### Samplefrequentie audio-uitvoer

Stel de samplefrequentie van de audio-uitvoer in van 8 KHz tot 384 KHz. Deze optie is alleen beschikbaar als de CoreAudio-verwerker is geselecteerd.

#### Aantal kanalen audio-uitvoer

Stel het aantal kanalen van de audio-uitvoer in — **MONO** of **STEREO**. Deze optie is alleen beschikbaar als de CoreAudio-verwerker is geselecteerd.

#### Toonhoogte-algoritme audio

Kies het algoritme dat wordt gebruikt voor toonhoogtecorrectie. Beschikbare waarden zijn **Time Domain**, **Spectral** en **Varispeed**. Handig als u de afspeelsnelheid aanpast en de resulterende audiokwaliteit wilt bepalen.

#### Ruimtelijk geluid

Ruimtelijk geluid gebruikt psychoacustische methoden om een meeslepende audio-ervaring te creëren op ondersteunde hoofdtelefoons en luidsprekeropstellingen. Mogelijke waarden: **Gedeactiveerd**, **Mono en Stereo**, **Meerkanaals**, **Mono Stereo Meerkanaals**.

#### Modus audio-uitvoer

Alleen beschikbaar op iOS. Hiermee kunt u de gemengde modus inschakelen zodat audio van deze applicatie wordt gemengd met andere applicaties. U kunt instructies vinden over hoe u de gemengde modus gebruikt [hier](/docs/howto/how-to-record-video-while-playing-music-on-iphone).

#### Afspeelpositie opslaan

Zorgt ervoor dat de applicatie de afspeelpositie voor nummers in uw muziekbibliotheek opslaat en herstelt.

#### Staat audiospeler opslaan

Slaat de staat van de audiospeler op voor het sluiten van de applicatie, zodat het eenvoudig is om te hervatten vanaf waar u was gebleven.

Zodra beide functies zijn ingeschakeld, opent u een map, album, artiest of genre. U ziet een actie **Afspelen hervatten** bovenaan het scherm, samen met het laatste opgeslagen nummer en de afspeelpositie. Tik op **Afspelen hervatten** om te herstellen. Om het afspelen voor een individueel bestand te hervatten, tikt u gewoon op dat bestand.

### Personalisatie

Pas het uiterlijk van het audiospelerscherm aan, kies welke bedieningen zichtbaar zijn op de speler, het vergrendelscherm en de statusbalk, en configureer de tijdoverlaaanknoppen.

#### Stijl audiospelerscherm

Configureer de positionering van werkbalken en hoofdbedieningen op de audiospeler.

#### Scrollstijl albumhoezen

Kies de scrollstijl voor albumhoezen op het audiospelerscherm.

#### Aanvullende elementen

Schakel extra elementen in op het audiospelerscherm. **Audio-formaatinfo** toont de technische informatie van het momenteel spelende nummer boven het artwork; **Audio-volumeschuifregelaar** toont de schuifregelaar voor audio-uitvoer onder de afspeelknoppen.

#### Acties op hoofdscherm

Configureer welke knoppen zichtbaar zijn op het hoofdscherm van de audiospeler. Beschikbare opties zijn Herhaal- en willekeurige modus, Volgend en vorig nummer, Tijdoverslaan, Slaaptimer, Google Chromecast, AirPlay en Bluetooth, Audio-equalizer, Zoeken, Bladwijzers, Snelheid, Bladwijzer toevoegen, Toevoegen aan favorieten, Opmerkingen en meer.

#### Afspeelbediening op het vergrendelscherm

Kies welke extra bedieningen zijn ingeschakeld op het vergrendelscherm. Mogelijke waarden: **Tijdoverslaan**, **Bladwijzer toevoegen** en **Toevoegen aan favorieten**.

#### Intervallen voor tijdoverslaan

Selecteer de tijdsintervallen die worden gebruikt door de knoppen voor voorwaarts en achterwaarts tijdoverslaan.

### Bestanden laden

Kies het netwerktype dat wordt gebruikt voor het streamen van nummers. Beschikbare opties: **Wi-Fi** en **Wi-Fi & mobiele data**.

#### Voorlaadtijd

Stel het bufferingsinterval in. Verhoog deze waarde als u een slechte netwerkverbinding heeft.

#### Directe URL gebruiken

Wanneer ingeschakeld, wordt een directe URL gebruikt om het nummer te laden als de server dit ondersteunt. Dit kan het laden van nummers versnellen, maar kan de afspeelstabiliteit enigszins beïnvloeden.

#### Laden van bestanden optimaliseren

Wanneer ingeschakeld, optimaliseert het systeem het laden van nummers voor de AVFoundation-audioverwerker, wat de afspeelstabiliteit kan verbeteren. De app gebruikt de technologie die hier is beschreven [hier](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/).

### Audio-equalizer

Configureer de audio-equalizer. U kunt meer lezen over presets en EQ-configuraties [hier](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Apparaten

Verbinding maken met een AirPlay- of Google Chromecast-apparaat (alleen iOS).

### Afspeelsnelheid

Pas de afspeelsnelheid van de audiospeler aan. Voor nauwkeurigere bediening schakelt u de precieze schuifregelaar in door op het configuratiepictogram in de rechterbovenhoek te tikken.

### Crossfade afspelen

Crossfade laat nummers naadloos doorlopen in een continue mix — het volgende nummer begint een paar seconden te spelen voordat het huidige nummer eindigt. Crossfade is niet beschikbaar voor AirPlay en Google Chromecast. Op dit scherm kiest u hoe lang het huidige en volgende nummer gelijktijdig worden afgespeeld. Als u problemen ondervindt met crossfade en de audio-equalizer tegelijkertijd, schakelt u de audioverwerker over zoals hierboven beschreven.

### Gapless afspelen

Gapless afspelen zorgt ervoor dat nummers worden afgespeeld zonder onderbrekingen of stilte ertussen. Het is perfect voor klassieke muziek, live-opnames en conceptalbums. Als u problemen ondervindt met gapless afspelen, schakelt u de audioverwerker over zoals hierboven beschreven.

### Afspeelcache

Nummers in de audiospelerwachtrij worden automatisch gedownload voor soepel afspelen. Als u audiobestanden handmatig downloadt, kunt u deze optie uitschakelen om duplicaten te vermijden. U kunt hier ook de cachegrootte van de audiospeler configureren. Lees meer over offline modus en afspeelcache hier: [Offline muziek afspelen in Evermusic & Flacbox: Downloaden en synchroniseren vanuit cloud naar lokale bestanden](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Slaaptimer

Schakel een timer in om het afspelen na een opgegeven timeout te stoppen. Voor nauwkeurigere bediening schakelt u de precieze modus in door op het configuratiepictogram in de rechterbovenhoek te tikken.

## Bibliotheek

Muziekbibliotheekinstellingen — automatische synchronisatie, metadatalezen, laden van albumhoezen, afspeellijsten, recenten en favorieten — staan hier.

### Metadata lezen

Wanneer u nummers aan de bibliotheek toevoegt, verwerkt de metadata-lezer ze op de achtergrond en organiseert ze op Artiest, Album, Genre en Componist. U kunt aanpassen hoe snel metadata wordt gelezen om gegevens sneller te laden (ten koste van meer batterij). U kunt de metadata-lezer ook volledig uitschakelen en bestandsnamen weergeven in plaats van tag-informatie.

De metadata-lezer werkt alleen de muziekbibliotheekdatabase bij; het wijzigt geen bestanden die zijn opgeslagen in uw cloudaccount of lokale opslag. Als u metadata van audiobestanden wilt bewerken, gebruikt u de ingebouwde tag-editor via de bijbehorende actie in het opties-menu.

Wanneer **Metadata lezen op de achtergrond** is ingeschakeld, werkt de lezer in achtergrondmodus. Als de app te veel energie verbruikt tijdens het afspelen, kan iOS deze onderbreken.

Als u een grote muziekcollectie heeft, is het raadzaam om metadatasynchronisatie uit te voeren op de desktopversie van de applicatie. U kunt vervolgens de gesynchroniseerde muziekbibliotheek overbrengen naar iOS via de functie **Back-up en herstel**.

Wanneer **Normaliseer metadata-codering** is ingeschakeld, normaliseert de app automatisch de codering van metadata voor alle nummers. Dit verhelpt problemen waarbij de codering van audiotags beschadigd is (bijvoorbeeld na het bewerken van bestanden op een Windows-pc) en voorkomt dat onjuiste tekens in nummerinformatie verschijnen.

**Metadata opnieuw laden** markeert elk bestand in uw muziekbibliotheek als ontbrekende metadata, waardoor de metadata-lezer elk record vernieuwt.

**Metadata lezen starten** start de metadata-lezer handmatig. De voortgang wordt weergegeven onder de actie.

### Online synchronisatie

Automatische online muzieksynch voegt nummers van verbonden cloudservices automatisch toe aan de muziekbibliotheek. Om het in te schakelen, opent u de muziekbibliotheekinstellingen en selecteert u synchronisatiemappen.

Met deze optie ingeschakeld, scant de applicatie de geselecteerde mappen, identificeert ondersteunde audiobestanden en voegt ze toe aan uw bibliotheek. Start of stop synchronisatie met de bijbehorende menuactie.

Online synchronisatie wordt alleen uitgevoerd wanneer de app op de voorgrond staat, dus het synchroniseren van een grote bibliotheek kan enige tijd duren. Om het te versnellen, houd de app open, sluit aan op een stroombron en schakel **Scherm → Altijd actief** in de instellingen in.

Als alternatief voert u online synchronisatie uit op de desktopversie van de app en brengt u de muziekbibliotheek over naar iOS via **Back-up en herstel**.

U kunt ook kiezen hoe vaak online synchronisatie wordt uitgevoerd. Als u het interval instelt op **Onmiddellijk**, wordt er een synchronisatie gestart elke keer dat u de applicatie opent.

### Offline synchronisatie

Configureer offline muzieksynch.

#### Gesynchroniseerde offline mappen

Wanneer u een online map op uw cloudserver markeert als offline beschikbaar (via het menu Meer acties), verschijnt deze hier. De inhoud van de map wordt gedownload naar **Lokale bestanden → Offline mappen**. Wanneer de online map wijzigt (bestanden toegevoegd, verwijderd of bijgewerkt), controleert de app op wijzigingen en werkt de lokale kopie op uw apparaat bij.

Op dit scherm kunt u handmatig offline mapsynchronisatie starten, de offline map in de bovenliggende map weergeven en de offline modus voor de map uitschakelen. Het uitschakelen van de offline modus verwijdert alle lokale kopieën van bestanden van uw apparaat.

#### Tijdsinterval

Kies hoe vaak de app offline mappen controleert op wijzigingen.

#### Lokale mappen scannen starten

Scan alle lokale mappen in de map Documenten van de applicatie op ondersteunde audiobestanden. Gevonden bestanden worden automatisch aan de muziekbibliotheek toegevoegd. Bestanden op uw apparaat maar buiten de map Documenten van de applicatie moeten handmatig aan de muziekbibliotheek worden toegevoegd, omdat de app er geen toegang toe heeft vanwege iOS/macOS-beveiligingsbeperkingen.

**Belangrijk:** Het is raadzaam om periodiek offline muzieksynch te starten om uw muziekbibliotheek up-to-date te houden met uw lokale bestanden.

### Personalisatie

Configureer de stijl van het muziekbibliotheeKscherm. Drie opties zijn beschikbaar: **Eenvoudig menu**, **Gegroepeerd menu** en **Tabblad-menu**. U kunt ook albumhoezen in het albumdetailscherm in- of uitschakelen.

### Albumhoezen

Kies hoe de applicatie albumhoezen laadt en opslaat.

- **Netwerktype** — kies **Wi-Fi** of **Wi-Fi & mobiele data** voor het downloaden van hoezen.
- **Albumhoezen laden voor online bestanden** — wanneer ingeschakeld, worden ingebedde albumhoezen geladen voor bestanden die zijn opgeslagen in cloudopslag. Dit kan aanvullende netwerkgegevens gebruiken.
- **Zoeken in map** — wanneer ingeschakeld, zoekt de app naar JPEG- of PNG-afbeeldingen in dezelfde map als het nummer geen ingebedde hoes heeft, en gebruikt deze als albumhoes.
- **Kwaliteit hoes** — selecteer de kwaliteit van albumhoezen die op uw apparaat zijn opgeslagen.
- **Tonen in map** — open de map waar albumhoezen zijn gecached zodat u ze kunt beheren of er een back-up van kunt maken.
- **Alles verwijderen** — verwijder gecachte albumhoezen om opslagruimte vrij te maken en de app te dwingen ze op verzoek opnieuw te laden.

### Afspeellijsten

Schakel de optie in om hetzelfde nummer twee keer aan een afspeellijst toe te voegen. Standaard is deze optie uitgeschakeld.

### Terkini

Beheer uw lijst met recent afgespeelde nummers.

- **Lijst verwijderen** — verwijder de volledige lijst met recent afgespeelde nummers.
- **Lijstgrootte wijzigen** — stel het aantal items in dat in de lijst verschijnt.
- **Nummerlijst exporteren** — exporteer uw lijst met recent afgespeelde nummers als M3U, CSV of TXT. Gedetailleerde instructies zijn beschikbaar [hier](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favorieten

Beheer de lijst met uw favoriete nummers.

- **Gelijktijdig bewerken** — wanneer ingeschakeld, voegt het toevoegen van een nummer aan favorieten het zowel in de muziekbibliotheek als in het bestandengedeelte tegelijkertijd toe.
- **Lijst verwijderen** — verwijder de volledige lijst met favoriete nummers.
- **Nummerlijst exporteren** — net als Terkini, exporteer favorieten als M3U, CSV of TXT.

### Muziekbibliotheek verwijderen

Wis de muziekbibliotheekdatabase. Uw muziekbestanden op de opslag blijven onaangeroerd.

## Toegangscode

Activeert het scherm voor wachtwoordbeveiliging als u uw applicatiegegevens wilt beschermen.

## Bestandsbeheerder

Het gedeelte Bestandsbeheerder bepaalt hoe bestanden worden overgedragen, opgeslagen en bekeken.

### Bestandsoverdrachten

Kies uw netwerkvoorkeur voor het downloaden van bestanden naar uw apparaat.

### Maximum aantal parallelle taken

Stel het aantal parallelle downloadthreads in. Een hoger getal versnelt downloads maar vereist meer batterij.

### Bestandsoverdrachtstaken

Toont momenteel actieve upload- en downloadtaken.

### Achtergrondoverdrachten

Sta downloads toe terwijl de app op de achtergrond staat. Als achtergrondoverdrachten veel energie verbruiken, kan iOS de app onderbreken.

### Gedownloade bestanden opslaan in

Kies de standaarddownloadmap, of laat de app u elke keer vragen.

### Gesynchroniseerde offline mappen

Beheer offline synchronisatie voor geselecteerde mappen. Om offline synchronisatie in te schakelen, tikt u op de drie-puntjesknop naast een map en selecteert u **Offline beschikbaar modus**. Nieuwe bestanden die aan de cloudmap worden toegevoegd, worden automatisch naar uw apparaat gedownload. Lees meer over offline modi [hier](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Tijdsinterval

Kies hoe vaak offline mappen worden gesynchroniseerd. **Onmiddellijk** start een synchronisatie elke keer dat u de app opent.

### Volledige bestandsnamen tonen

Toon volledige bestandsnamen, inclusief extensies, in de bestandsbeheerder.

### Online bestanden bewerken

Schakel online bestandsbewerking uit om over te schakelen naar alleen-lezen modus voor verbonden cloudservices en onbedoelde verwijderingen te voorkomen. Deze actie verwijdert bestandsbewerkingsbewerkingen uit de gebruikersinterface.

### Bestanden kopiëren bij openen

Geef aan hoe de app geïmporteerde bestanden van andere applicaties verwerkt.

### Miniaturen voor bestanden

Beheer en verwijder gegenereerde bestandsminiaturen om opslagruimte vrij te maken.

### Tijdelijke bestanden verwijderen

Maak de cachemap van de applicatie leeg om opslagruimte terug te winnen.

## Audio-tag-editor

Configureer de ingebouwde audio-tag-editor.

### Schalen albumhoezen

Kies de schaalvergelijkingsmethode die wordt gebruikt wanneer een albumhoes in audiotags wordt opgeslagen.

### Online bestanden bijwerken

Wanneer ingeschakeld, werkt de applicatie automatisch de metadata van een bestand op de cloudserver bij nadat u klaar bent met bewerken.

### Bestand verwijderen na online bewerken

Kies of de applicatie de gedownloade kopie moet verwijderen na het voltooien van het bewerken van een online bestand op een cloudserver.

### Knoppen op hoofdscherm

Kies welke knoppen zichtbaar zijn op het hoofdscherm van de audio-tag-editor.

## Widgets

Schakel widgets in zodat de app widgetgegevens bijwerkt tijdens het afspelen. Widgetupdates vereisen extra energie, dus schakel dit alleen in als u werkelijk widgets gebruikt op uw beginscherm of vergrendelscherm.

U kunt meer lezen over Evermusic-widgets in de [Navigatiegids](/docs/guide/evermusic/evermusic-guide-navigation/).

## CarPlay

Wijzig CarPlay-instellingen hier. Dit menu is ook beschikbaar in de CarPlay-interface zodat u de ervaring kunt aanpassen tijdens het rijden.

### Sorteren

Configureer sorteeropties voor alle CarPlay-schermen.

### Limiet voor laden van inhoud

Kies of de app paginering gebruikt op het CarPlay-scherm. Paginering houdt menu's responsief op apparaten met beperkt geheugen en grote bibliotheken.

### Kleur verloopmenuiconen

Selecteer het kleurenschema voor het hoofdscherm van CarPlay.

### Afbeeldingen tonen

Schakel afbeeldingen op het CarPlay-scherm uit om de laadsnelheid te optimaliseren en geheugengebruik te verminderen bij grote bibliotheken.

### Afspelen pauzeren bij verbinding

Schakel dit in om plotseling hard audio te vermijden wanneer u uw apparaat verbindt met CarPlay.

## Wi-Fi Drive

Activeer Wi-Fi Drive om bestanden van een computer naar uw apparaat over te dragen via een desktopwebbrowser. Gedetailleerde instructies over hoe u Wi-Fi Drive gebruikt, zijn beschikbaar [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalisatie

Pas de gebruikersinterface aan uw voorkeuren aan.

### Applicatiepictogram

Kies een alternatief applicatiepictogram voor uw beginscherm.

### Kleurenschema

Kies het thema van de gebruikersinterface en schakel de donkere modus in. Wanneer **Standaard** is geselecteerd, volgt de applicatie de apparaatbrede weergave-instellingen.

### Achtergrondstijl

Wijzig de achtergrondstijl van de applicatie. Momenteel is de enige optie **Vervaagde albumhoes**, die het artwork van het momenteel spelende nummer gebruikt als vervagde app-achtergrond.

### Weergave van items in de lijst

Stel in hoe items worden weergegeven in lijsten. Handig op kleine schermen — u kunt de app de rijhoogte automatisch laten aanpassen op basis van inhoud, of kleinere pictogrammen in lijstcellen weergeven om tekst meer ruimte te geven.

### Limiet voor laden van inhoud

Standaard gebruikt de applicatie paginering om het laden van inhoud te versnellen. U kunt paginering uitschakelen om alles tegelijk te laden.

### Stijl lokale bestanden-scherm

Wijzig de presentatiestijl van het gedeelte **Lokale bestanden**.

### Stijl muziekbibliotheeKscherm

Pas het uiterlijk van het scherm **Muziekbibliotheek** aan.

### Stijl audiospelerscherm

Configureer het uiterlijk van het scherm **Audiospeler**.

### Stijl contextmenu

Kies de stijl van het contextmenu dat wordt weergegeven wanneer u op de knop Meer acties tikt.

## Venster

Beschikbaar op Mac en Catalyst. Configureer venstergerelateerde voorkeuren zoals standaardgrootte en gedrag bij opstarten.

## Scherm

Kies of het scherm actief moet blijven terwijl u de applicatie gebruikt. Handig bij het scannen van grote bibliotheken of bij langdurig tag-bewerkingswerk.

## Toegankelijkheid

Activeer **Tekstmodus** om alle afbeeldingen in de gebruikersinterface te verbergen. Tekstmodus wordt automatisch ingeschakeld wanneer VoiceOver actief is en is ook handig voor zeer kleine of alleen-tekst-instellingen.

## Taal

Wijzig de taal van de applicatie en overschrijf de systeemstandaard. Momenteel ondersteunt de app de volgende lokalisaties: Afrikaans, Akan, Albanees, Amhaars, Arabisch, Armeens, Assamees, Aymara, Azerbeidzjaans, Bambara, Bengaals, Baskisch, Wit-Russisch, Bosnisch, Bulgaars, Birmees, Catalaans, Cebuano, Vereenvoudigd Chinees, Traditioneel Chinees, Corsicaans, Kroatisch, Tsjechisch, Deens, Dhivehi, Dogri, Nederlands, Engels, Esperanto, Ests, Ewe, Filipijns, Fins, Frans, Galicisch, Ganda, Georgisch, Duits, Grieks, Guaraní, Gujarati, Haïtiaans Creools, Hausa, Hawaïaans, Hebreeuws, Hindi, Hmong, Hongaars, IJslands, Igbo, Iloko, Indonesisch, Iers, Italiaans, Japans, Javaans, Kannada, Kazachs, Khmer, Kinyarwanda, Koreaans, Krio, Koerdisch, Sorani Koerdisch, Kirgizisch, Laotisch, Latijn, Lets, Lingala, Litouws, Luxemburgs, Macedonisch, Maithili, Malagasi, Maleis, Malayalam, Maltees, Māori, Marathi, Mizo, Mongools, Nepalees, Noord-Sotho, Noors Bokmål, Nyanja, Odia, Oromo, Pasjtoe, Perzisch, Pools, Portugees, Punjabi, Roemeens, Russisch, Samoaans, Sanskrit, Schots Gaelisch, Servisch, Shona, Sindhi, Singalees, Slowaaks, Sloveens, Somalisch, Zuid-Sotho, Spaans, Soendanees, Swahili, Zweeds, Tadzjieks, Tamil, Tataars, Telugu, Thai, Tsonga, Turks, Turkmeens, Oekraïens, Urdu, Oeigoers, Oezbeeks, Vietnamees, Welsh, Xhosa, Jiddisch, Yoruba, Zoeloe.

## Back-up en herstel

Maak een back-up van al uw applicatiegegevens of migreer naar een ander apparaat. U kunt kiezen wat u wilt opnemen:

- **Database** — al uw muziekbibliotheEKnummers en afspeellijsten. Offline nummers zijn niet inbegrepen om de back-upgrootte beheersbaar te houden.
- **Albumhoezen** — al uw gecachte albumhoezen.
- **Instellingen** — al uw applicatie-instellingen.

Tik op **Back-up applicatiegegevens** om de back-upbewerking te starten. De applicatiegegevens worden naar één bestand geschreven dat u later kunt gebruiken om de applicatiestatus te herstellen op een nieuw apparaat of na het opnieuw installeren van de app.

Om applicatiegegevens op een nieuw apparaat te herstellen, verplaatst u het back-upbestand naar het nieuwe apparaat via een verbonden cloudservice of iCloud en opent u het op het nieuwe apparaat.

We hebben een gedetailleerde stapsgewijze handleiding hier: [Hoe u uw muziekbibliotheek kunt overbrengen tussen apparaten in Evermusic: Stapsgewijze handleiding](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Help

Open de applicatiegids voor hulp en begeleiding bij het effectief gebruiken van de app.

## Veelgestelde vragen

Vind antwoorden op veelgestelde vragen in het FAQ-gedeelte.

## Feedback sturen

Heeft u feedback of heeft u hulp nodig? Stuur uw feedback rechtstreeks vanuit de app naar ons ondersteuningsteam.

## Deze app delen

Deel de applicatie met uw vrienden om het woord te verspreiden.

## Meer apps ontdekken

Verken andere apps van Everappz.

## Algemene voorwaarden

Beschrijft de algemene voorwaarden voor het gebruik van de applicatie. Lees deze voordat u de applicatie gebruikt.

## Privacybeleid

Bezoek de pagina met het privacybeleid om onze gegevensbeheer-praktijken te begrijpen. Lees deze voordat u de applicatie gebruikt.

## Analytics en gegevensverzameling

Controleer welke services zijn ingeschakeld voor analytics en gegevensverzameling en deactiveer elke service die u niet wilt.

In **Evermusic Free (blauw pictogram)** zijn analytics en diagnostiek standaard ingeschakeld om ons te helpen de app te verbeteren — u kunt ze hier op elk moment uitschakelen. **Evermusic Pro (rood pictogram) bevat helemaal geen analytics of diagnostiek** — het gedeelte is leeg (of verborgen) omdat er niets wordt verzameld, en er is geen opt-in-optie.

## Juridische kennisgevingen

Bevat informatie over elke bibliotheek die in de applicatie wordt gebruikt, samen met het versienummer van de app en build-informatie.
