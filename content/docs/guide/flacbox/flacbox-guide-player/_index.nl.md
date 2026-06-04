---
title: "Audiospeler"
date: 2020-02-01
description: "Leer hoe je de Flacbox-audiospeler gebruikt op iPhone, iPad en Mac. Beheer afspelen, wachtrijen, configureer de FFmpeg / systeem audio-engine, wijzig samplerate, toonhoogtecorrectie, IO-bufferduur, equalizer, audiobladwijzers, AirPlay 2, Google Cast, CarPlay, widgets en Mac-sneltoetsen."
keywords: [
  "Flacbox spelersgids", "audiospeler instellingen", "Flacbox equalizer",
  "AirPlay muziekstreaming", "Google Cast muziek", "audiobladwijzers",
  "Flacbox afspeelwachtrij", "Flacbox herhalen shufflen", "Flacbox volumebeheer",
  "macOS minispeler", "voiceover muziekapp",
  "Flacbox FFmpeg", "Flacbox toonhoogtecorrectie", "Flacbox samplerate",
  "Flacbox externe DAC", "Flacbox surround geluid", "Flacbox IO-buffer",
  "Flacbox afspeelsnelheid", "Flacbox slaaptimer"
]
tags: ["gids", "flacbox", "speler"]
readingTime: 14
---


De Audiospeler is het hoofdscherm van de app waar je de muziek en de meeste afspeelfuncties beheert. Het is ook waar Flacbox' hi-res audio-engine — gebouwd op de systeemcodecs plus de meegeleverde **FFmpeg**-bibliotheek — het zware werk doet. Laten we verkennen hoe je hem gebruikt.

## De Audiospeler Openen

Je kunt naar de volledig scherm speler gaan via de minispelerbalk. Op iPhone bevindt de minispeler zich onderaan het hoofdscherm. Op iPad en Mac is hij aan de linkerkant. Om de minispeler op iPhone te verbergen, tik er eenmaal op en swipe omlaag. Om de volledig scherm speler volledig te sluiten, tik op de sluitknop in de rechteronderhoek.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audiospeler Hoofdscherm" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Ondersteunde Audioformaten

Flacbox speelt de populairste audioformaten — zowel Apple's systeemcodecs als vele aanvullende formaten die worden verwerkt door de meegeleverde FFmpeg-engine:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Dit dekt vrijwel elk modern lossy en lossless formaat dat je in een persoonlijke muziekcollectie kunt hebben.

## Afspeelbediening

Onderaan het spelerscherm zie je knoppen voor Afspelen, Pauzeren, Volgende Track en Vorige Track. Er zijn ook optionele knoppen zoals Volgende 30 sec en Vorige 30 sec die je kunt inschakelen in de app-instellingen (handig voor luisterboeken). Je kunt snel vooruit- of terugspoelen door de knoppen Volgende / Vorige ingedrukt te houden. Om naar een specifiek deel van een track te springen, sleep de afspeelschuifregelaar.

## Herhalen en Shufflen

Tik op de herhaalknop om door herhaalmodi te bladeren:

- **Alles herhalen** — herhaalt alle tracks in je wachtrij.
- **Één herhalen** — herhaalt alleen de huidige track.
- **Herhalen stoppen** — pauzeert wanneer de huidige track eindigt.
- **Niet herhalen** — speelt de wachtrij eenmalig af zonder te herhalen.

Gebruik de knop **Shufflen** om de volgorde van tracks in de wachtrij te willekeurig te maken.

## Volumebeheer

Open het scherm Audio-instellingen door op het geluidsicoon onder de afspeelbediening te tikken om de volumeschuifregelaar te openen. Je vindt hier ook knoppen voor **Google Cast** en **AirPlay** zodat je snel kunt overschakelen naar een ander apparaat.

## Google Cast (Chromecast)

Voor Google Cast-gebruikers verschijnt het **Cast**-pictogram onderaan de speler. Tik erop om een apparaat te kiezen en te beginnen met streamen. Zorg ervoor dat je apparaat en de Google Cast-ontvanger op hetzelfde Wi-Fi-netwerk zitten. Opmerking: niet elk audioformaat is compatibel met Google Cast — sommige hi-res formaten moeten mogelijk worden getranscodeerd.

## AirPlay

Voor AirPlay, zoek de knop **AirPlay** onderaan de speler. Tik erop en selecteer een apparaat voor streamen. Flacbox ondersteunt **AirPlay 2**, zodat je tegelijkertijd naar meerdere HomePods, Apple TV's of AirPlay-2-compatibele luidsprekers kunt spelen.

## Audio-equalizer

Flacbox bevat een **10-bands equalizer** met iPod-stijl presets. Tik op Equalizer in de volumeweergave en schakel hem in de rechterbovenhoek in. Je kunt presets gebruiken zoals Akoestisch en Basversterker, of elke frequentieband aanpassen met schuifregelaars. Maak je eigen presets, sla ze op onder elke naam en verhoog het totale volume met de preamplifier. We hebben meer gedetailleerde instructies over het gebruik van de equalizer [hier](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audiospeler Equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Spelermodus Werkbalk

Voor sommige spelerstijlen is er een speciale werkbalk bovenaan de volledig scherm speler. Deze werkbalk bevat drie handige knoppen:

- **Zoeken** — zoek snel een specifieke track in je spelerwachtrij.
- **Afspeelsnelheidsbeheer** — pas de afspeelsnelheid aan van 0,02× tot 3,00×. Perfect voor luisterboeken, podcasts en lezingen. Tik op Normaal om terug te keren naar de standaardsnelheid.
- **Audiobladwijzers** — maak meerdere bladwijzers per track. We hebben volledige instructies over het gebruik van bladwijzers [hier](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Spelerwachtrij

Om je spelerwachtrij te zien, tik op de wachtrijknop rechts van het huidige nummer. Elk nummer in de wachtrij heeft meer acties — tik op de drie puntjes om ze te bekijken. Om een nummer in de wachtrij te herordenen, gebruik de herordening-indicator bij de titel en sleep het naar een nieuwe positie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Afspeelwachtrij" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Opmerkingen / Songteksten

Om trackopmerkingen en ingesloten songteksten, evenals LRC-bestanden te bekijken, volg deze stappen:

1. Open **Instellingen**.
2. Ga naar **Audiospeler**.
3. Selecteer **Personalisatie**.
4. Tik op **Knoppen op het hoofdscherm**.
5. Schakel **Opmerkingen** in.

Tik daarna meerdere keren op de spelerwachtrijknop onderaan het scherm om te schakelen van de artwork / wachtrijweergave naar de opmerkingweergave. Scroll op het scherm Opmerkingen naar rechts om te schakelen tussen **Opmerkingen**, **Ingesloten songteksten** en het **LRC-bestand**. Volledige instructies zijn beschikbaar [hier](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Songteksten en Opmerkingen Scherm" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Optiesmenu

Elk nummer in de audiospelerwachtrij heeft een menu met meer acties, toegankelijk door op de drie-puntjes-knop bij de nummertitel te tikken.

- **Volgende afspelen** — voegt het nummer toe aan de top van de spelerwachtrij.
- **Toevoegen aan afspeellijst** — voegt het nummer toe aan een afspeellijst, met de optie om een nieuwe te maken.
- **Toevoegen aan favorieten** — markeert het nummer als favoriet voor snelle toegang.
- **Downloaden** — slaat het nummer op in lokale bestanden, verschijnt in het tabblad **Lokale bestanden** en de sectie **Offline muziek**.
- **Audiotags bewerken** — opent de ingebouwde audiotags-editor om ontbrekende metadata te corrigeren, waardoor het nummer in je opslag wordt gewijzigd.
- **Tonen in map** — onthult de map waar het audiobestand is opgeslagen.
- **Tonen in Finder** — voor bestanden geïmporteerd van je Mac, onthult dit de map waar het audiobestand zich op je Mac bevindt.
- **Openen in** — exporteert het audiobestand naar een andere app.
- **Verwijderen uit wachtrij** — verwijdert het geselecteerde nummer uit de audiospelerwachtrij.
- **Verwijderen uit cloudservice** — verwijdert het nummer uit zowel de muziekbibliotheek als de cloudopslag. **Deze actie is onomkeerbaar.**
- **Verwijderen uit lokale bestanden** — verwijdert het nummer uit zowel de muziekbibliotheek als de lokale opslag. **Deze actie is onomkeerbaar.**
- **Verwijderen uit muziekbibliotheek** — verwijdert het nummer uit je muziekbibliotheek, terwijl het bestand in opslag bewaard blijft.

Dezelfde opties zijn beschikbaar voor het nu-spelende item in de audiospelerwachtrij, die je kunt openen door op het pictogram **Meer acties** bij de tracktitel te tikken.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Opties voor een Item in de Afspeelwachtrij" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Aanvullende Spelacties

Tik op de knop **Meer acties** "..." links van de momenteel spelende nummertitel om aanvullende acties te zien.

- **Afspelen hervatten** — hervat vanaf waar je gebleven was, inclusief wachtrij en mediapositie. Bijzonder handig voor luisterboeken. Geactiveerd in de app-instellingen.
- **Zoeken** — zoek snel een specifieke track in je audiospelerwachtrij.
- **Bladwijzers** — bekijk je lijst met gemaakte audiobladwijzers.
- **Opmerkingen** — bekijk trackopmerkingen en ingesloten songteksten, evenals LRC-bestanden. Volledige instructies [hier](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Snelheid** — pas de afspeelsnelheid naar wens aan.
- **Recenties** — open een lijst met recent gespeelde nummers.
- **Favorieten** — bekijk je collectie favoriete nummers.
- **Audio-equalizer** — activeer de audio-equalizer.
- **Slaaptimer** — stel een timer in om het afspelen te stoppen na een opgegeven interval. Geweldig voor die momenten waarop je in slaap wilt vallen bij je muziek.
- **Wachtrij opslaan als afspeellijst** — sla de huidige audiospelerwachtrij op als een nieuwe afspeellijst.
- **Wachtrij verwijderen** — wis je spelerwachtrij en stop het afspelen.
- **Instellingen** — open audiospeler-instellingen.
- **Help** — vind hulp en begeleiding.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audiospeler Meer Acties Scherm" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Audiobladwijzers

Met deze functie kun je meerdere bladwijzers maken voor tracks in je muziekbibliotheek — perfect voor luisterboeken, lezingen, lange DJ-mixen of het markeren van het refrein van een favoriete track.

Om een nieuwe bladwijzer te maken:

- Begin met het afspelen van het gewenste nummer.
- Open het spelerscherm.
- Tik op de knop **Bladwijzers** op de werkbalk voor spelermodus.
- Selecteer **Bladwijzer toevoegen**.
- Kies de bladwijzertijd en tik op **Gereed** in de rechterbovenhoek.

Het bewerken van bladwijzers voor de huidige track is eenvoudig: tik op Bewerken in de rechterbovenhoek om de bewerkingsmodus te openen. In deze modus kun je bladwijzers herschikken, verwijderen, de bladwijzertijd aanpassen en bladwijzertitels wijzigen. Meer gedetailleerde instructies over audiobladwijzers zijn beschikbaar [hier](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audiobladwijzers Scherm" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Recenties en Favorieten

Tik op het spelerscherm op de drie puntjes om Recenties en Favorieten te openen. In beide secties kun je zoeken naar nummers, alles afspelen, alles shufflen, de lijst exporteren en de lijst wissen. We hebben gedetailleerde instructies over het exporteren van nummerlijsten [hier](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Verbind je iPhone met je auto via USB of draadloze Apple CarPlay en Flacbox verschijnt op je CarPlay-beginscherm, klaar om muziek veilig af te spelen tijdens het rijden. De CarPlay-interface bevat speciale tabbladen voor Bibliotheek, Verbindingen, Lokale bestanden en Instellingen, met afspeelbediening, shufflen, herhalen, wachtrijbeheer en de audio-equalizer allemaal beschikbaar zonder je telefoon op te pakken. Pas de CarPlay-ervaring verder aan in Instellingen → CarPlay — sorteeropties, paginering, kleurverloop van menu-iconen, of afbeeldingen worden geladen en een optie om afspelen automatisch te pauzeren wanneer CarPlay verbinding maakt.

[Lees de volledige CarPlay-gids](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox op Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Beginschermwidgets (iPhone & iPad)

Flacbox ondersteunt iOS Beginscherm- en Vergrendelschermwidgets zodat je het afspelen in één oogopslag kunt zien en beheren. Zorg ervoor dat Widgets zijn ingeschakeld in Instellingen → Widgets → Widgets inschakelen, houd dan je Beginscherm of Vergrendelscherm ingedrukt, tik op **+**, zoek naar **Flacbox** en voeg een widget toe. De widget vernieuwt tijdens het afspelen om het albumplaatje, de titel en de artiest van de huidige track te tonen.

## Minispelervenster (Mac Exclusief)

Mac-gebruikers kunnen een compacte, altijd-bovenop minispeler gebruiken. Beweeg je cursor naar de rechteronderrand van het Flacbox-venster, verklein het naar zijn kleinste formaat en tik op de samenvouwknop. Houd het bovenop elk ander venster door Venster → Venster altijd bovenop tonen te selecteren in de menubalk — perfect om muziekbediening zichtbaar te houden terwijl je in een andere app werkt.

## Sneltoetsen (Mac Exclusief)

Voor Mac-gebruikers is een systeemafspeelmenu beschikbaar in de statusbalk met sneltoetsen. Druk bijvoorbeeld op de spatiebalk voor Afspelen / Pauzeren. Sneltoetsen voor Stoppen, Volgend nummer, Vorig nummer, Tijd overslaan, Herhalen, Shufflen en Afspeelsnelheid zijn ook beschikbaar.

## Audiospeler Instellingen

Om toegang te krijgen tot instellingen, tik op de knop Meer op het spelerscherm en kies Instellingen. Hier vind je verschillende secties, hieronder vermeld.

### Algemeen

Deze instellingen omvatten de fundamentele aspecten van de audiospeler, inclusief de afspeelwachtrij, audio-uitvoer en het opslaan van de spelerstatus.

- **Herhaalmodus** — kies hoe de audiospeler zich gedraagt wanneer een track eindigt:
  - **Alles herhalen** — herhaalt alle tracks in je wachtrij.
  - **Één herhalen** — herhaalt alleen de huidige track.
  - **Herhalen stoppen** — pauzeert het afspelen wanneer de huidige track eindigt.
  - **Niet herhalen** — laat je wachtrij doorspelen zonder te herhalen.
- **Shufflemodus** — maak de volgorde van tracks in je wachtrij willekeurig. Je kunt het **Shuffle uit** of **Shuffle aan** zetten.
- **Audiocodec** — kies de audio-engine voor afspelen:
  - **Systeemcodec + FFmpeg** — geeft prioriteit aan de systeemcodec waar mogelijk, waardoor compatibiliteit en stabiliteit worden verbeterd. Toonhoogtecorrectie en aanpassingen van de audio-uitvoer samplerate kunnen beperkt zijn in deze modus.
  - **FFmpeg** — dwingt de FFmpeg-codec voor alle audiobestanden, waardoor je toonhoogtecorrectie en de audio-uitvoer samplerate kunt aanpassen.
- **Audio-uitvoer samplerate** — pas de audio-uitvoer samplerate aan om de geluidskwaliteit te optimaliseren, vooral nuttig met een externe DAC. Beschikbare waarden: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** en **96 kHz**.
- **Aantal kanalen audio-uitvoer** — voor multichannel-audiosystemen met een externe DAC, specificeer het aantal kanalen: **Mono, Stereo, Midden / Links / Rechts, Midden / Links / Rechts / Surround, ITU BS.775-1, 5.1 Surround** en **SDDS**.
- **Voorkeurs IO-bufferduur audio-uitvoer** — configureer de invoer / uitvoer bufferduur voor audio-afspelen. Een typische waarde voor het minimaliseren van latentie bij het afspelen van hoge-resolutie audio is ongeveer **5 milliseconden (0,005 seconden)**. De acceptabele buffergrootte hangt af van je hardware- en softwareomgeving, dus test verschillende duurlengtes op je doelapparaat en kies die het beste evenwicht houdt tussen lage latentie en storingsvrij afspelen.
- **Audio-uitvoermodus (alleen iOS)** — configureer gemengde audio-uitvoermodus zodat audio van Flacbox mengt met andere applicaties. Gedetailleerde instructies zijn [hier](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Afspeelpositie opslaan** — zorgt ervoor dat de applicatie de afspeelpositie voor nummers in je muziekbibliotheek opslaat en herstelt.
- **Audiospelerstatus opslaan** — bewaart de status van je audiospeler voordat je de app sluit. Om het afspelen te hervatten, tik op **Afspelen hervatten** bovenaan een willekeurige map, album, artiest of genre wanneer je de app heropent. Je kunt het afspelen ook herstellen voor afzonderlijke bestanden door op de specifieke track te tikken.

Zodra je zowel **Afspeelpositie opslaan** als **Audiospelerstatus opslaan** hebt ingeschakeld, open je een willekeurige map, album, artiest of genre en zie je een knop **Afspelen hervatten** bovenaan het scherm samen met de laatste opgeslagen track en positie. Tik erop om precies te hervatten waar je gebleven was.

### Personalisatie

Personalisatie stelt je in staat de look van het audiospelerscherm aan te passen, de beschikbare bedieningen op het hoofdscherm, vergrendelscherm en statusbalk te wijzigen, en overslaatijdbedieningen te configureren.

- **Audiospelerschermstijl** — configureer de positionering van elementen op het audiospelerscherm.
- **Scrollstijl albumhoezen** — configureer de gewenste scrollstijl voor albumhoezen.
- **Aanvullende elementen** — schakel extra elementen in op het audiospelerscherm. **Audio-indelingsinformatie** toont de audio-informatie van de huidige track boven het artwork; **Audio-volumeschuifregelaar** toont de audio-uitvoerschuifregelaar onder de afspeelbediening.
- **Acties op het hoofdscherm** — configureer welke knoppen standaard zichtbaar zijn op het hoofdscherm van de audiospeler: **Herhaal- en Shufflemodus, Volgend en Vorig nummer, Overslaatijd, Slaaptimer, Google Chromecast, AirPlay en Bluetooth, Audio-equalizer, Zoeken, Bladwijzers, Snelheid, Bladwijzer toevoegen, Toevoegen aan favorieten, Opmerkingen** en meer.
- **Afspeelbedieningen op het vergrendelscherm** — kies welke bedieningen op het vergrendelscherm verschijnen. Mogelijke waarden: **Overslaatijd, Bladwijzer toevoegen, Toevoegen aan favorieten**.
- **Overslaatijdknoppen** — kies het tijdsinterval voor de knoppen **Overslaatijd**.

### Bestanden Laden

Tijdens het laden van bestanden kun je het netwerktype wijzigen dat wordt gebruikt om nummers te laden. Beschikbare opties: **Wi-Fi**, **Wi-Fi & Mobiele data**.

- **Voorlaadtijd** — stel het bufferingstijdsinterval in. Verhoog dit als je een slechte netwerkverbinding hebt.
- **Directe URL gebruiken** — wanneer ingeschakeld, wordt een directe URL gebruikt om het nummer te laden als de server dit ondersteunt. Dit kan het laden van nummers versnellen maar kan de afspeelstabiliteit beïnvloeden.

### Audio-equalizer

Pas de audio-equalizerinstellingen aan. Je kunt meer lezen over het configureren van de audio-equalizer [hier](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Afspeelsnelheid

Pas de afspeelsnelheid van de audiospeler aan van **0,02× tot 3,00×**. Tik op het configuratiepictogram in de rechterbovenhoek om over te schakelen naar **precieze modus** voor fijnere aanpassingen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Afspeelsnelheid Scherm" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Toonhoogtecorrectie

Wijzig toonhoogtecorrectie-instellingen met behulp van de vooraf gedefinieerde waarden. Je kunt ook schakelen tussen vooraf gedefinieerde waarden en precieze modus door op de knop in de rechterbovenhoek te tikken. Toonhoogtecorrectie is beschikbaar in het FFmpeg-codecpad, met een bereik van **-1000 tot +1000**.

### Afspeelcache

Nummers in de audiospelerwachtrij worden automatisch gedownload voor soepel afspelen. Als je audiobestanden handmatig downloadt, kun je deze optie uitschakelen om duplicaten te voorkomen. Je kunt hier ook de cache-grootte van de audiospeler configureren.

### Slaaptimer

Activeer een timer om het afspelen automatisch te stoppen na een opgegeven periode — handig wanneer je bij muziek in slaap wilt vallen. Tik op het configuratiepictogram in de rechterbovenhoek voor **precieze modus** met minuut-voor-minuut granulariteit.

## Toegankelijkheid

Flacbox is volledig toegankelijk met **VoiceOver**. Elk onderdeel heeft een goed ontworpen label en beschrijving. Wanneer VoiceOver actief is, schakelt de app over naar **Tekstmodus** zodat alleen zinvolle elementen worden weergegeven — wat de navigatiesnelheid en duidelijkheid verbetert. Je kunt Tekstmodus ook activeren in **Instellingen → Toegankelijkheid → Tekstmodus**.

### Schuifregelaars Aanpassen met VoiceOver

1. **Selecteer de schuifregelaar** — veeg links of rechts totdat VoiceOver hem aankondigt.
2. **Pas de waarde aan** — dubbeltik en houd de schuifregelaar vast, sleep dan omhoog of omlaag om de waarde snel te wijzigen. VoiceOver kondigt de nieuwe waarde aan terwijl je beweegt.

### Trackpositie Aanpassen in een Lijst met VoiceOver

1. Tik op het herordenpictogram bij de tracktitel om er focus op te geven.
2. Dubbeltik snel op het herordenpictogram. Laat bij de tweede tik je vinger niet los — houd vast totdat je een geluid hoort dat aangeeft dat de cel klaar is om te worden verplaatst.
3. Verplaats de cel naar zijn nieuwe positie.

Andere componenten werken zoals verwacht, met behulp van door het systeem geleverde VoiceOver-patronen.
