---
title: "Instellingen"
date: 2020-02-01
description: "Verken elke instelling in Flacbox — van afspeelvoorkeuren, de FFmpeg / systeem audio-engine, Hi-Res audio-uitvoer, equalizer-aanpassingen, toonhoogtecorrectie, IO-bufferduur, metadatasynchronisatie, afspeellijstbeheer, bestandsoverdrachten, beginschermwidgets, Apple CarPlay, UI-personalisatie, taal, toegangscode, back-up en herstel, en Premium-upgrade."
keywords: [
  "Flacbox instellingen", "audiospeler configuratie", "premium upgrade Flacbox",
  "WiFi Drive", "metadatasynchronisatie", "equalizer", "afspeelsnelheid",
  "afspeellijst duplicaten", "bestandsbeheer instellingen", "offline muziek sync",
  "audiotags editor", "donkere modus", "aankopen herstellen", "instellingen back-up",
  "Flacbox widget instellingen", "Flacbox CarPlay instellingen",
  "Flacbox FFmpeg instellingen", "Flacbox samplerate instellingen",
  "Flacbox toonhoogtecorrectie instellingen", "Flacbox IO-buffer",
  "Flacbox toegangscode", "Flacbox taal", "Flacbox personalisatie",
  "Flacbox analyse"
]
tags: ["gids", "flacbox", "instellingen"]
readingTime: 16
---


Het scherm Instellingen is het controlecentrum van Flacbox. Van hier kun je upgraden naar Premium, de audio-engine configureren (systeemcodecs of FFmpeg), je muziekbibliotheek beheren, de bestandsbeheerder instellen, de audiotags-editor aanpassen, beginschermwidgets en Apple CarPlay inschakelen, je gegevens back-uppen en hulp en juridische informatie openen. Secties zijn gegroepeerd onder headers: Aankopen & Updates, App-voorkeuren, Hulp, en Juridisch & Privacy.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Instellingen Hoofdscherm" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Upgraden naar Premium

Upgrade de applicatie naar de Premium-versie om alle beperkingen te verwijderen. De gratis versie van de applicatie biedt een eenmalige levenslange in-app aankoop en twee abonnementsopties (1 maand en 1 jaar) om alle beperkingen te verwijderen en te upgraden naar Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Upgraden naar Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Gezinsdeling** is ingeschakeld voor alle aankopen en abonnementen, zodat je de Premium-versie kunt delen met maximaal vijf familieleden zonder extra kosten.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Selecteer een Premium Abonnement" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Je kunt meer lezen over aankopen en de Premium-versie hier: [Wat is het verschil tussen Flacbox en Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Aankopen Delen tussen iOS en Mac

Levenslange aankopen en abonnementen worden gedeeld tussen iOS en Mac, waarbij iCloud wordt gebruikt om deze informatie te synchroniseren. Als je de Premium-versie op je iOS-apparaat hebt, zorg er dan voor dat je de nieuwste versie hebt geïnstalleerd en dat iCloud is ingeschakeld. Start de app op iOS en wacht een minuut totdat je aankoopinformatie naar iCloud is geüpload.

Je kunt ook proberen op de knop Aankopen herstellen in de app-instellingen te tikken. Installeer daarna de nieuwste app-versie vanuit de App Store op je Mac en start de app. Zorg ervoor dat je een internetverbinding hebt en dat je hetzelfde iCloud- en App Store-account op Mac gebruikt als op iOS. Wacht een minuut totdat de app aankoopinformatie van iCloud heeft gedownload — de Premium-versie zou automatisch op je Mac moeten worden geactiveerd.

## Aankopen Herstellen op een Nieuw Apparaat

Om je aankoop op een nieuw apparaat te herstellen, gebruik het menu Aankopen → Aankopen herstellen. Je ziet de lijst van je aankopen. Als je ze niet allemaal ziet, bevestig dan dat het apparaat is verbonden met dezelfde Apple ID die werd gebruikt om de aankopen te doen, en zorg ervoor dat iCloud is ingeschakeld.

## Probeer Premium Gratis

Je kunt de Premium-versie gratis upgraden, voor een beperkte tijd, via dit menu. Kijk gewoon een advertentie of vertel je vrienden over de app om Premium gratis te krijgen.

## Aankopen

Je kunt vorige aankopen herstellen via dit menu. Als je activeringsfouten tegenkomt, probeer dan de optie Aankopen herstellen bij App-start in te schakelen.

## Software-update

Tik op Software-update om te controleren of er een nieuwere versie van Flacbox beschikbaar is. De app vergelijkt je geïnstalleerde versie met de nieuwste versie in de App Store en laat je weten of een update wordt aanbevolen.

## Wat is Nieuw

Dit menu is beschikbaar na het uitbrengen van een nieuwe versie. Het toont een samenvatting van de wijzigingen en nieuwe functies in de meest recente update.

## Audiospeler

Deze sectie configureert de audiospeler en de onderliggende audio-engine, inclusief de FFmpeg / systeemcodec-keuze en Hi-Res audio-uitvoer opties.

### Algemeen

Deze instellingen omvatten de fundamentele aspecten van de audiospeler — afspeelwachtrij, audio-uitvoer en het opslaan van de spelerstatus.

- **Herhaalmodus** — kies hoe de audiospeler zich gedraagt wanneer een track eindigt:
  - **Alles herhalen** — herhaalt alle tracks in je wachtrij.
  - **Één herhalen** — herhaalt alleen de huidige track.
  - **Herhalen stoppen** — pauzeert het afspelen wanneer de huidige track eindigt.
  - **Niet herhalen** — laat je wachtrij doorspelen zonder te herhalen.
- **Shufflemodus** — maak de volgorde van tracks in je wachtrij willekeurig. Je kunt het **Shuffle uit** of **Shuffle aan** zetten.
- **Audiocodec** — kies de audio-engine voor afspelen:
  - **Systeemcodec + FFmpeg** — geeft prioriteit aan de systeemcodec waar mogelijk, waardoor compatibiliteit en stabiliteit worden verbeterd. Toonhoogtecorrectie en de audio-uitvoer samplerate kunnen beperkt zijn.
  - **FFmpeg** — dwingt de FFmpeg-codec voor alle audiobestanden, waardoor toonhoogtecorrectie en de audio-uitvoer samplerate worden ontgrendeld.
- **Audio-uitvoer samplerate** — pas de audio-uitvoer samplerate aan om de geluidskwaliteit te optimaliseren, vooral nuttig met een externe DAC. Beschikbare waarden: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** en **96 kHz**.
- **Aantal kanalen audio-uitvoer** — voor multichannel-audiosystemen met een externe DAC, specificeer het aantal kanalen: Mono, Stereo, Midden / Links / Rechts, Midden / Links / Rechts / Surround, ITU BS.775-1, 5.1 Surround en SDDS.
- **Voorkeurs IO-bufferduur audio-uitvoer** — configureer de invoer / uitvoer bufferduur. Een typische waarde voor het minimaliseren van latentie bij het afspelen van hoge-resolutie audio is ongeveer **5 milliseconden (0,005 seconden)**. Test verschillende duurlengtes op je doelapparaat om het beste evenwicht te vinden tussen lage latentie en storingsvrij afspelen.
- **Audio-uitvoermodus (alleen iOS)** — configureer gemengde audio-uitvoer zodat audio van Flacbox mengt met andere applicaties. Gedetailleerde instructies zijn [hier](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Afspeelpositie opslaan** — slaat de afspeelpositie voor nummers in je muziekbibliotheek op en herstelt deze.
- **Audiospelerstatus opslaan** — bewaart de status van de audiospeler voordat je de app sluit, waardoor het eenvoudig is om te hervatten waar je gebleven was.

Zodra je zowel **Afspeelpositie opslaan** als **Audiospelerstatus opslaan** hebt ingeschakeld, open je een willekeurige map, album, artiest of genre en zie je een knop **Afspelen hervatten** bovenaan het scherm.

### Personalisatie

Personalisatie stelt je in staat de look van het audiospelerscherm aan te passen, de beschikbare bedieningen op het hoofdscherm, vergrendelscherm en statusbalk te wijzigen, en overslaatijdbedieningen te configureren.

- **Audiospelerschermstijl** — configureer de positionering van elementen op het audiospelerscherm.
- **Scrollstijl albumhoezen** — configureer de gewenste scrollstijl voor albumhoezen.
- **Aanvullende elementen** — schakel extra elementen in op het audiospelerscherm. Audio-indelingsinformatie toont de audio-informatie van de huidige track boven het artwork; Audio-volumeschuifregelaar toont de audio-uitvoerschuifregelaar onder de afspeelbediening.
- **Acties op het hoofdscherm** — configureer welke knoppen standaard zichtbaar zijn op het hoofdscherm van de audiospeler: Herhaal- en Shufflemodus, Volgend en Vorig nummer, Overslaatijd, Slaaptimer, Google Chromecast, AirPlay en Bluetooth, Audio-equalizer, Zoeken, Bladwijzers, Snelheid, Bladwijzer toevoegen, Toevoegen aan favorieten, Opmerkingen en meer.
- **Afspeelbedieningen op het vergrendelscherm** — kies welke bedieningen op het vergrendelscherm verschijnen. Mogelijke waarden: Overslaatijd, Bladwijzer toevoegen, Toevoegen aan favorieten.
- **Overslaatijdknoppen** — kies het tijdsinterval voor de Overslaatijd-knoppen.

### Bestanden Laden

Tijdens het laden van bestanden kun je het netwerktype wijzigen dat wordt gebruikt om nummers te laden. Beschikbare opties: **Wi-Fi**, **Wi-Fi & Mobiele data**.

- **Voorlaadtijd** — stel het bufferingstijdsinterval in. Verhoog dit als je een slechte netwerkverbinding hebt.
- **Directe URL gebruiken** — wanneer ingeschakeld, wordt een directe URL gebruikt om het nummer te laden als de server dit ondersteunt. Dit kan het laden van nummers versnellen maar kan de afspeelstabiliteit beïnvloeden.

### Audio-equalizer

Configureer de 10-bands audio-equalizer, presets en preamplifier. Je kunt meer lezen over het configureren van de audio-equalizer [hier](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Afspeelsnelheid

Pas de afspeelsnelheid van de audiospeler aan van **0,02× tot 3,00×**. Tik op het configuratiepictogram in de rechterbovenhoek om over te schakelen naar **precieze modus** voor fijnere aanpassingen.

### Toonhoogtecorrectie

Wijzig toonhoogtecorrectie-instellingen met behulp van de vooraf gedefinieerde waarden, of schakel over naar **precieze modus** door op de knop in de rechterbovenhoek te tikken. Toonhoogtecorrectie is beschikbaar in het FFmpeg-codecpad, met een bereik van **-1000 tot +1000**.

### Afspeelcache

Nummers in de audiospelerwachtrij worden automatisch gedownload voor soepel afspelen. Als je audiobestanden handmatig downloadt, kun je dit uitschakelen om duplicaten te voorkomen. Je kunt hier ook de cache-grootte van de audiospeler configureren.

### Slaaptimer

Activeer een timer om het afspelen automatisch te stoppen na een opgegeven periode. Tik op het configuratiepictogram in de rechterbovenhoek voor **precieze modus** met minuut-voor-minuut granulariteit.

## Bibliotheek

Je muziekbibliotheekinstellingen — automatische synchronisatie, metadataverwerking, albumhoezen laden, afspeellijsten, recenties en favorieten — vind je hier.

### Metadataverwerking

Wanneer je tracks aan de bibliotheek toevoegt, gaat de **metadatalezer** aan het werk. Dit achtergrondproces leest alle metadata van je tracks en organiseert ze op Artiest, Album, Genre en Componist. Je kunt de snelheid van metadataverwerking aanpassen om gegevens sneller te laden (ten koste van meer batterij). Je kunt de metadatalezer ook uitschakelen en bestandsnamen weergeven in plaats van taginformatie.

De metadatalezer **werkt alleen metadata bij in je muziekbibliotheek** en wijzigt de bestanden die zijn opgeslagen in je cloudaccount of lokale opslag niet. Om metadata in de audiobestanden zelf te bewerken, gebruik de ingebouwde **tageditor** via de overeenkomstige actie in het optiesmenu.

Wanneer **Metadata lezen op de achtergrond** is ingeschakeld, blijft de lezer werken in de achtergrondmodus. Als de app te veel energie verbruikt tijdens het afspelen van audio, kan iOS de app opschorten.

Als je een grote muziekcollectie hebt, voer metadatasynchronisatie uit op de desktopversie van de applicatie en breng de gesynchroniseerde muziekbibliotheek over naar iOS met **Back-up & Herstel**.

Wanneer **Metadata-codering normaliseren** is ingeschakeld, normaliseert de app automatisch de codering van metadata voor alle nummers. Dit verhelpt kapotte tagcoderingen (bijv. na het bewerken van bestanden op een Windows-pc) en voorkomt dat onjuiste tekens verschijnen in trackinformatie.

**Metadata herladen** markeert elk bestand in je muziekbibliotheek als ontbrekende metadata, waardoor de metadatalezer elk record vernieuwt.

**Metadataverwerking starten** activeert de metadatalezer handmatig. De voortgang wordt onder de actie weergegeven.

### Online Synchronisatie

Automatische online muziekssynchronisatie voegt tracks van verbonden cloudservices automatisch toe aan de muziekbibliotheek. Om dit in te schakelen, open de muziekbibliotheekinstellingen en selecteer synchronisatiemappen.

Met deze optie ingeschakeld scant de applicatie de geselecteerde mappen, identificeert ondersteunde audiobestanden en voegt ze toe aan je bibliotheek. Start of stop synchronisatie met de overeenkomstige menuactie.

Online synchronisatie wordt alleen uitgevoerd wanneer de app op de voorgrond is, dus het synchroniseren van een grote bibliotheek kan even duren. Om het te versnellen, houd Flacbox open, sluit je apparaat aan op stroom en schakel **Instellingen → Scherm → Altijd actief** in.

Als alternatief, voer online synchronisatie uit op de desktopversie van de app en breng het resultaat over naar iOS met **Back-up & Herstel**.

Je kunt ook kiezen hoe vaak online synchronisatie wordt uitgevoerd. Het instellen van het interval op **Onmiddellijk** activeert een synchronisatie elke keer dat je de applicatie opent.

### Offline Synchronisatie

Configureer offline muzieknchronisatie.

#### Gesynchroniseerde Offline Mappen

Wanneer je een online map op je cloudserver als offline beschikbaar markeert (via het menu **Meer acties**), verschijnt het hier. De mapinhoud wordt gedownload naar **Lokale bestanden → Offline mappen**. Wanneer de online map verandert (bestanden toegevoegd, verwijderd of bijgewerkt), controleert de app op wijzigingen en werkt de lokale kopie op je apparaat bij.

Op dit scherm kun je offline mapsynchronisatie handmatig starten, de offline map in de bijbehorende map onthullen en de offline modus voor de map uitschakelen. Het uitschakelen van de offline modus verwijdert alle lokale kopieën van bestanden van je apparaat.

#### Tijdsinterval

Kies hoe vaak de app offline mappen controleert op wijzigingen.

#### Lokale Mappen Scannen Starten

Scan alle lokale mappen in de **Documents**-map van de applicatie op ondersteunde audiobestanden. Gevonden bestanden worden automatisch toegevoegd aan de muziekbibliotheek. Bestanden die zich op je apparaat bevinden maar buiten de Documents-map van de applicatie, moeten handmatig aan de muziekbibliotheek worden toegevoegd, omdat de app er vanwege iOS / macOS-beveiligingsbeperkingen geen toegang tot heeft.

**Belangrijk:** Het is raadzaam om periodiek offline muzieknchronisatie te starten om je muziekbibliotheek up-to-date te houden met je lokale bestanden.

### Personalisatie

Configureer de stijl van het muziekbibliotheekkscherm. Drie opties zijn beschikbaar: **Eenvoudig menu, Gegroepeerd menu, Tabbladen menu**. Je kunt ook albumhoezen in het albumdetailscherm in- of uitschakelen.

### Albumhoezen

Configureer hoe de applicatie albumartwork laadt en opslaat.

- **Netwerktype** — kies **Wi-Fi** of **Wi-Fi & Mobiele data** voor het downloaden van hoezen.
- **Albumhoezen laden voor online bestanden** — wanneer ingeschakeld, worden ingesloten albumhoezen geladen voor bestanden die zijn opgeslagen in cloudopslag. Dit kan extra netwerkgegevens gebruiken.
- **Zoeken in de map** — wanneer ingeschakeld, als een track geen ingesloten hoes heeft, zoekt de app naar JPEG- of PNG-afbeeldingen in dezelfde map en gebruikt ze als albumartwork.
- **Hoeskwaliteit** — selecteer de kwaliteit van albumhoezen die op je apparaat zijn opgeslagen.
- **Tonen in map** — open de map waar albumhoezen zijn gecached.
- **Alles verwijderen** — verwijder gecachede albumhoezen om opslag vrij te maken en de app te dwingen ze op aanvraag opnieuw te laden.

### Afspeellijsten

Schakel de optie in om hetzelfde nummer twee keer aan een afspeellijst toe te voegen. Standaard is deze optie uitgeschakeld.

### Recenties

Beheer je lijst met recentelijk afgespeelde nummers.

- **Lijst verwijderen** — verwijder de volledige lijst met recentelijk afgespeelde nummers.
- **Lijstgrootte wijzigen** — stel het aantal items in dat in de lijst verschijnt.
- **Nummerlijst exporteren** — exporteer je recentelijk afgespeelde nummerlijst als M3U, CSV of TXT. Gedetailleerde instructies zijn beschikbaar [hier](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favorieten

Beheer de lijst met je favoriete nummers.

- **Gelijktijdig bewerken** — wanneer ingeschakeld, voegt het toevoegen van een nummer aan favorieten het zowel in de muziekbibliotheek als de bestandssectie tegelijkertijd toe.
- **Lijst verwijderen** — verwijder de volledige lijst met favoriete nummers.
- **Nummerlijst exporteren** — zoals Recenties, exporteer favorieten als M3U, CSV of TXT.

### Muziekbibliotheek Verwijderen

Wis de muziekbibliotheekdatabase. Je muziekbestanden in de opslag blijven onaangetast.

## Toegangscode

Activeer het toegangscode-scherm om je applicatiegegevens te beschermen met een 4-cijferige numerieke toegangscode. Wanneer ingeschakeld, wordt je gevraagd de toegangscode in te voeren elke keer dat de app wordt gestart. Combineer het met iOS Face ID / Touch ID op het apparaat voor extra bescherming.

## Bestandsbeheerder

De sectie Bestandsbeheerder bepaalt hoe bestanden worden overgedragen, opgeslagen en bekeken.

### Bestandsoverdrachten

Kies je netwerkvoorkeur voor het downloaden van bestanden naar je apparaat.

### Maximum Aantal Parallelle Taken

Stel het aantal parallelle downloadthreads in. Een hoger getal versnelt downloads maar verbruikt meer batterij.

### Bestandsoverdrachttaken

Toont momenteel actieve upload- en downloadtaken.

### Achtergrondoverdrachten

Sta downloads toe terwijl de app op de achtergrond is. Als achtergrondoverdrachten veel energie verbruiken, kan iOS de app opschorten.

### Gedownloade Bestanden Opslaan In

Kies de standaard downloadmap, of laat de app je elke keer vragen.

### Gesynchroniseerde Offline Mappen

Beheer offline synchronisatie voor geselecteerde mappen. Om offline synchronisatie in te schakelen, tik op de drie-puntjes-knop naast een map en selecteer **Offline modus beschikbaar**. Nieuwe bestanden die aan de cloudmap worden toegevoegd, worden automatisch naar je apparaat gedownload. Lees meer over offline modi [hier](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Tijdsinterval

Kies hoe vaak offline mappen worden gesynchroniseerd. **Onmiddellijk** activeert een synchronisatie elke keer dat je de app opent.

### Volledige Bestandsnamen Tonen

Toon volledige bestandsnamen, inclusief extensies, in de bestandsbeheerder.

### Online Bestanden Bewerken

Schakel het online bestanden bewerken uit om over te schakelen naar de alleen-lezen modus voor verbonden cloudservices en onbedoelde verwijderingen te voorkomen. Deze actie verwijdert bestandsbewerkingsbewerkingen uit de gebruikersinterface.

### Bestanden Kopiëren bij Openen

Geef aan hoe de app omgaat met geïmporteerde bestanden van andere applicaties.

### Miniaturen voor Bestanden

Beheer en verwijder gegenereerde bestandsminiaturen om opslagruimte vrij te maken.

### Tijdelijke Bestanden Verwijderen

Wis de cachemap van de applicatie om opslagruimte terug te winnen.

## Audiotags Editor

Configureer de ingebouwde audiotags-editor — handig voor het batchgewijs oplossen van artiest / album / jaar / genre / albumhoesproblemen in cloud- en lokale bestanden.

### Albumhoes Schalen

Kies de schaalingsmethode die wordt gebruikt wanneer een albumhoes in audiotags wordt opgeslagen.

### Online Bestanden Bijwerken

Wanneer ingeschakeld, werkt de applicatie automatisch de metadata van een bestand op de cloudserver bij nadat je klaar bent met bewerken.

### Bestand Verwijderen na Online Bewerken

Kies of de applicatie de gedownloade kopie moet verwijderen na het voltooien van het bewerken van een online bestand op een cloudserver.

### Hoofdschermknoppen

Kies welke knoppen zichtbaar zijn op het hoofdscherm van de audiotags-editor.

Voor diepgaandere batchbewerking van veel bestanden tegelijk, installeer onze compagnon-app **Evertag**.

## Widgets

Schakel widgets in zodat de app widgetgegevens bijwerkt tijdens het afspelen. Widgetupdates vereisen extra energie, dus de schakelaar staat standaard uit — schakel hem alleen in als je widgets daadwerkelijk gebruikt op je Beginscherm of Vergrendelscherm.

Je kunt Flacbox-widgets toevoegen door je Beginscherm of Vergrendelscherm lang ingedrukt te houden, op **+** te tikken, **Flacbox** te zoeken en een widgetgrootte te kiezen. Widgets tonen het huidige artwork, de tracktitel en de artiest, en tikken direct door naar de volledig scherm speler. Widgets werken ook op macOS in het Berichtencentrum.

## CarPlay

Wijzig hier CarPlay-instellingen. Dit menu is ook beschikbaar in de CarPlay-interface zodat je de ervaring kunt aanpassen tijdens het rijden.

### Sorteren

Configureer sorteeropties voor alle CarPlay-schermen.

### Inhoudslaadlimiet

Kies of de app paginering gebruikt op het CarPlay-scherm. Paginering houdt menu's responsief op grote bibliotheken.

### Kleurverloop Menu-iconen

Selecteer het kleurenschema voor het CarPlay-beginscherm.

### Afbeeldingen Tonen

Schakel afbeeldingen op het CarPlay-scherm uit om de laadsnelheid te optimaliseren en het geheugengebruik op grote bibliotheken te verminderen.

### Afspelen Pauzeren bij Verbinding

Schakel dit in om plotseling hard geluid te voorkomen wanneer je apparaat verbinding maakt met CarPlay.

## Wi-Fi Drive

Activeer **Wi-Fi Drive** om bestanden van een computer naar je apparaat over te zetten via een desktop-webbrowser, Finder of File Explorer. Gedetailleerde instructies over het gebruik van Wi-Fi Drive zijn beschikbaar [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalisatie

Pas de gebruikersinterface aan je voorkeuren aan.

### Applicatie-icoon

Kies een alternatief applicatie-icoon voor je Beginscherm (Premium).

### Kleurenschema

Kies het thema van de gebruikersinterface en schakel de donkere modus in. Wanneer **Standaard** is geselecteerd, volgt de applicatie de apparaatbrede weergave-instellingen.

### Achtergrondstijl

Wijzig de achtergrondstijl van de applicatie. Momenteel is de enige optie **Wazige albumhoes**, die het artwork van de huidige track gebruikt als wazige app-achtergrond.

### Weergave van Items in de Lijst

Pas aan hoe items worden weergegeven in lijsten. Nuttig op kleine schermen — je kunt de app de rijhoogte automatisch laten aanpassen op basis van inhoud, of kleinere pictogrammen in lijstcellen tonen om meer ruimte aan tekst te geven.

### Inhoudslaadlimiet

Standaard gebruikt de applicatie paginering om het laden van inhoud te versnellen. Je kunt paginering uitschakelen om alles tegelijk te laden.

### Stijl Lokale Bestanden Scherm

Wijzig de presentatiestijl van de sectie **Lokale bestanden**.

### Stijl Muziekbibliotheek Scherm

Pas de look van het scherm **Muziekbibliotheek** aan.

### Stijl Audiospeler Scherm

Configureer de look van het scherm **Audiospeler**.

### Contextmenustijl

Kies de stijl van het contextmenu dat wordt weergegeven wanneer je op de knop **Meer acties** tikt.

## Venster

Beschikbaar op Mac en Catalyst. Configureer venstergerelateerde voorkeuren zoals standaardgrootte en gedrag bij het opstarten.

## Scherm

Kies of het scherm actief moet blijven terwijl je de applicatie gebruikt. Nuttig bij het scannen van grote bibliotheken of langdurig tagbewerkingswerk.

## Toegankelijkheid

Activeer **Tekstmodus** om alle afbeeldingen in de gebruikersinterface te verbergen. Tekstmodus wordt automatisch ingeschakeld wanneer VoiceOver actief is en is ook nuttig voor zeer kleine of tekstgerichte instellingen.

## Taal

Wijzig de applicatietaal en overschrijf de systeemstandaard. De wijziging wordt van kracht nadat je Flacbox volledig afsluit en opnieuw opent. Momenteel ondersteunde lokalisaties zijn: Afrikaans, Akan, Albanees, Amhaars, Arabisch, Armeens, Assamees, Aymara, Azerbeidzjaans, Bambara, Bengaals, Baskisch, Belarussisch, Bosnisch, Bulgaars, Birmees, Catalaans, Cebuano, Chinees (Vereenvoudigd), Chinees (Traditioneel), Corsicaans, Kroatisch, Tsjechisch, Deens, Dhivehi, Dogri, Nederlands, Engels, Esperanto, Ests, Ewe, Filipijns, Fins, Frans, Galicisch, Ganda, Georgisch, Duits, Grieks, Guarani, Gujarati, Haïtiaans Creools, Hausa, Hawaiiaans, Hebreeuws, Hindi, Hmong, Hongaars, IJslands, Igbo, Iloko, Indonesisch, Iers, Italiaans, Japans, Javaans, Kannada, Kazachs, Khmer, Kinyarwanda, Koreaans, Krio, Koerdisch, Koerdisch Sorani, Kirgizisch, Laotiaans, Latijn, Lets, Lingala, Litouws, Luxemburgs, Macedonisch, Maithili, Malagassisch, Maleis, Malayalam, Maltees, Maori, Marathi, Mizo, Mongools, Nepalees, Noord-Sotho, Noors Bokmål, Nyanja, Odia, Oromo, Pasjtoe, Perzisch, Pools, Portugees, Punjabi, Roemeens, Russisch, Samoaans, Sanskriet, Schots Gaelisch, Servisch, Shona, Sindhi, Singalees, Slowaaks, Sloveens, Somalisch, Zuid-Sotho, Spaans, Sundanees, Swahili, Zweeds, Tadzjieks, Tamil, Tataars, Telugu, Thais, Tsonga, Turks, Turkmeens, Oekraïens, Urdu, Oeigoers, Oezbeeks, Vietnamees, Welsh, Xhosa, Jiddisch, Yoruba, Zulu.

## Back-up & Herstel

Gebruik deze functie om al je applicatiegegevens te back-uppen of deze naar een ander apparaat te migreren. Je kunt kiezen wat je wilt opnemen:

- **Database** — alle tracks in de muziekbibliotheek, inclusief afspeellijsten. Offline tracks zijn niet opgenomen om de back-upbestandsgrootte beheersbaar te houden.
- **Albumhoezen** — al je gecachede albumhoezen.
- **Instellingen** — al je applicatie-instellingen.

Tik op **Back-up maken van applicatiegegevens** om de back-up te starten. Applicatiegegevens worden naar één bestand geschreven dat je later kunt gebruiken om de applicatiestatus te herstellen op een nieuw apparaat of na het opnieuw installeren van de applicatie.

Om applicatiegegevens op een nieuw apparaat te herstellen, verplaats het back-upbestand naar het nieuwe apparaat via een verbonden cloudservice of iCloud en open het op het nieuwe apparaat.

Gedetailleerde stapsgewijze instructies: [Hoe je je Muziekbibliotheek Overzet tussen Apparaten: Stapsgewijze Gids](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Hulp

Open de applicatiegids voor hulp en begeleiding bij het effectief gebruiken van de app.

## Veelgestelde Vragen

Vind antwoorden op veelgestelde vragen in de FAQ-sectie.

## Feedback Sturen

Heb je feedback of heb je hulp nodig? Stuur je feedback rechtstreeks vanuit de app naar ons ondersteuningsteam.

## Deel Deze App

Deel de applicatie met je vrienden om het woord te verspreiden.

## Ontdek Meer Apps

Verken andere apps van Everappz.

## Algemene Voorwaarden

Beschrijft de algemene voorwaarden voor het gebruik van de applicatie. Lees ze vóór gebruik van de applicatie.

## Privacybeleid

Bezoek de pagina met het privacybeleid om onze gegevensverwerking te begrijpen. Lees het vóór gebruik van de applicatie.

## Analyse en Gegevensverzameling

Controleer welke services zijn ingeschakeld voor analyse en gegevensverzameling en deactiveer alle services die je niet wilt.

## Juridische Kennisgevingen

Bevat informatie over elke bibliotheek die in de applicatie wordt gebruikt, samen met het app-versienummer en build-informatie.
