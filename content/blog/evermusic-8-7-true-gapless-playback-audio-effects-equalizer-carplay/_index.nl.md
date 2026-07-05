---
title: "Evermusic 8.7: echt naadloos afspelen, audio-effecten, volumenormalisatie, opnieuw ontworpen equalizer"
date: 2026-07-05
description: "Evermusic 8.7 voor iPhone, iPad en Mac voegt echt naadloos afspelen toe, vijf studio-audio-effecten (Reverb, Delay, Distortion, Compressor, Crossfeed), EBU R128 volumenormalisatie, een opnieuw ontworpen 10-bands equalizer met import/export van presets, een herbouwde AVAudioEngine-streamengine met ondersteuning voor FLAC en Ogg Vorbis, en een snellere, nauwkeurigere CarPlay en Nu speelt."
keywords: ["Evermusic 8.7", "Evermusic-update", "echt naadloos afspelen iPhone", "naadloze muziekspeler iOS", "naadloos afspelen CarPlay", "audio-effecten muziekspeler iPhone", "reverb delay distortion compressor crossfeed iOS", "crossfeed koptelefoon iOS", "volumenormalisatie iPhone", "luidheidsnormalisatie muziekspeler", "EBU R128 normalisatie iOS", "replaygain-alternatief iPhone", "10-bands equalizer iPhone", "grafische equalizer iOS-app", "equalizer-presets import export", "FLAC-speler iPhone", "Ogg Vorbis-speler iOS", "lossless muziekspeler iPhone 2026", "AVAudioEngine muziekspeler", "CarPlay muziekspeler iPhone", "Nu speelt vergrendelscherm nauwkeurigheid", "cloud-muziekspeler iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Naadloos afspelen", "Audio-effecten", "Reverb", "Delay", "Distortion", "Compressor", "Crossfeed", "Volumenormalisatie", "EBU R128", "Equalizer", "FLAC", "Ogg Vorbis", "CarPlay", "Nu speelt", "Liquid Glass", "Wat is nieuw"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Kort samengevat:** [Evermusic 8.7](/products/evermusic) is een release rond geluidskwaliteit voor iPhone, iPad en Mac. Het brengt **echt naadloos afspelen** (geen pauzes, klikken of tikken tussen nummers), een volledige set **studio-audio-effecten** — Reverb, Delay, Distortion, Compressor en Crossfeed — en **EBU R128 volumenormalisatie** die de luidheid van nummer tot nummer consistent houdt zonder ReplayGain-tags. De **10-bands equalizer** is opnieuw ontworpen met nieuwe schuifregelaars, sneller schakelen tussen presets, aangepaste presets die je kunt importeren en exporteren, en een betere lay-out in liggend formaat en op iPad. Onder de motorkap verbetert een **herbouwde AVAudioEngine-streamengine** de betrouwbaarheid en formaatondersteuning, inclusief **FLAC** en **Ogg Vorbis**. **CarPlay** en **Nu speelt** zijn sneller en nauwkeuriger op het vergrendelscherm, in de auto en vanaf koptelefoonafstandsbedieningen.

---

## Hallo allemaal!

Evermusic 8.7 is beschikbaar om te downloaden. Deze update draait helemaal om hoe je muziek *klinkt*. We hebben de afspeelengine herbouwd voor echt naadloos afspelen, een reeks studiokwaliteit audio-effecten toegevoegd, luidheidsnormalisatie geïntroduceerd en de equalizer vanaf de schuifregelaars opnieuw ontworpen. Alles is verpakt in Apple's nieuwe **Liquid Glass**-ontwerp.

[Download Evermusic 8.7 uit de App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) of werk bij vanuit je bestaande versie. Evermusic is een gratis download met optionele in-app upgrades.

## Echt naadloos afspelen

Naadloos afspelen betekent dat de stilte tussen twee nummers verdwenen is. Geen pauze, geen klik, geen tik — het huidige nummer stroomt rechtstreeks over in het volgende. Het is het belangrijkst voor muziek die is ontworpen om als geheel te worden gehoord: **live-opnames, DJ-mixen, klassieke werken en conceptalbums** waar het ene nummer rechtstreeks in het andere overvloeit.

Dit is wat er technisch is veranderd. De audio-engine van Evermusic houdt twee nummers tegelijk in afspeelstatus: het nummer dat je hoort en het volgende in de wachtrij. Terwijl het huidige nummer speelt, wordt het volgende nummer op de achtergrond al **opgehaald, gedecodeerd en voorgebufferd**. Wanneer het huidige nummer zijn einde bereikt, draagt de engine de overdracht over aan het volgende nummer **binnen de speler, niet binnen de audiostroom**. De uitvoer-renderlus blijft audiosamples uit een doorlopende ringbuffer trekken zonder ooit te stoppen, zodat de luisteraar nooit een grens hoort. De overschakeling gebeurt tussen samples, en precies daarom is er geen hoorbaar gaatje.

Dit werkt hetzelfde of het bestand nu op je apparaat, in de cloud of op een mediaserver staat — het voorbufferen begint voor externe bronnen gewoon iets eerder.

## Studio-audio-effecten

Evermusic 8.7 voegt vijf realtime audio-effecten toe die je op je muziek kunt stapelen. Elk draait als een native audioverwerkingsknooppunt in de afspeelengine, zodat het op alles wat je afspeelt wordt toegepast — lokale bestanden, cloudstreams en internetradio — zonder opnieuw te coderen.

Elk effect wordt geleverd met een **samengestelde bibliotheek van presets** om met één tik een geweldig geluid te krijgen, en Evermusic **onthoudt je exacte instellingen** tussen sessies. Verstel een bediening en het effect schakelt naar een **Handmatige** status, zodat je altijd weet wanneer je van een preset bent afgeweken.

### Reverb

Voegt een gevoel van ruimte toe, van een strakke kamer tot een kathedraal. Gebouwd op Apple's `AVAudioUnitReverb` biedt het **13 ruimte-presets** (Kleine kamer, Middelgrote zaal, Plate, Kathedraal en meer) plus een **wet/dry-mix**-regeling van 0 tot 100% zodat jij bepaalt hoeveel ruimte je toevoegt.

### Delay (Echo)

Een klassieke echo met **10 presets** — Slapback, Tape-echo, Dub, Ambient en andere. Je kunt de **delaytijd** (tot 2 seconden), **feedback** (aantal herhalingen), een **low-pass cutoff** om de herhalingen te verwarmen en de **wet/dry-mix** instellen.

### Distortion

Van subtiele grit tot volledige lo-fi-destructie, aangedreven door `AVAudioUnitDistortion` met **22 karakter-presets** (Bit Brush, Cellphone Concert, Radio Tower en meer), een **pre-gain**-drive-regeling en een wet/dry-mix zodat je het effect terug kunt mengen in het schone signaal.

### Compressor

Een dynamiekprocessor (Apple's `AUDynamicsProcessor`) die luide en zachte passages vereffent. Het biedt de volledige professionele set bedieningen — **drempel, ratio/headroom, attack, release, expansie en makeup-gain** — met **10 presets** afgestemd op echte situaties: Spraak / Podcast, Late avond, Filmdialoog, Streaming-match en Maximale luidheid daaronder.

### Crossfeed

Crossfeed laat luisteren met een koptelefoon natuurlijker klinken door een beetje van het linkerkanaal in het rechter te mengen en vice versa, zoals je oren echte luidsprekers horen. Het is gebouwd op het bekende **Bauer stereophonic-to-binaural (bs2b)** algoritme, met controle over het **crossfeed-niveau** en de **cutoff-frequentie**, en **6 presets** waaronder de audiofiel-favoriete instellingen *Chu Moy* en *Jan Meier*. Het is vooral goed op oudere, hard gepande stereomixen uit de jaren 60 en 70.

## Volumenormalisatie

Ooit een afspeellijst gemaakt waarin het ene nummer knalt en het volgende een gefluister is? Volumenormalisatie lost dat op. Evermusic 8.7 gebruikt **EBU R128 luidheidsmeting** (dezelfde ITU-R BS.1770-standaard die in de omroep en door streamingdiensten wordt gebruikt) om de werkelijke waargenomen luidheid van elk nummer te meten en het voorzichtig naar een consistent doel te sturen.

In tegenstelling tot ReplayGain vereist het **geen** tags in je bestanden en wijzigt het je audio **niet**. Het werkt in realtime op alles wat je afspeelt, inclusief cloudstreams en live radio, en het reset netjes wanneer je zoekt of van nummer wisselt.

Vier presets dekken de gebruikelijke gevallen:

- **Licht** — zachte nivellering (doel −20 LUFS).
- **Standaard** — de standaard, streaming-achtige luidheid (doel −16 LUFS, tot +12 dB versterking voor zachte nummers).
- **Sterk** — agressieve afstemming voor sterk gemengde bibliotheken (doel −14 LUFS).
- **Nacht** — zachter en consistent voor luisteren op laag volume in de avond (doel −23 LUFS).

Je hoeft niet langer tussen nummers naar het volume te grijpen.

## Opnieuw ontworpen equalizer

De **10-bands grafische equalizer** van Evermusic kreeg een volledige herziening. De banden bestrijken **32 Hz tot 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), elk instelbaar van **−12 dB tot +12 dB** in fijne stappen van 0,1 dB, met een **preamp** van −24 dB tot +24 dB om clipping te voorkomen wanneer je boost.

Wat is nieuw in 8.7:

- **Nieuwe schuifregelaars** — precieze, responsieve bedieningen die de look van de native iOS 26-systeemschuifregelaar en het **Liquid Glass**-materiaal overnemen.
- **Sneller, soepeler schakelen tussen presets** — spring direct tussen presets, met een opnieuw ontworpen horizontale preset-balk in staand formaat en een verticale preset-kolom in liggend formaat.
- **Betere lay-out in liggend formaat en op iPad** — de schuifregelaars en preset-kiezer herschikken zich om de extra breedte te gebruiken in plaats van te worden geperst in een kolom ter grootte van een telefoon.
- **Aangepaste presets** — maak en bewaar je eigen curven, wijzig de volgorde, en **importeer en exporteer** presets als `.eqp`-bestanden om ze tussen apparaten te verplaatsen of te delen.

De equalizer draait native in de engine (`AVAudioUnitEQ`), dus hij wordt op elke bron toegepast, en hij werkt ook via AirPlay, Chromecast en CarPlay waar ondersteund.

## Herbouwde afspeelengine

Onder de motorkap draait Evermusic 8.7 op een **herbouwde streamengine** gebouwd op Apple's `AVAudioEngine` met een aangepaste render-pipeline. Dit is wat de naadloze overdracht, de effectketen en de equalizer mogelijk maakt, en het maakt ook het dagelijkse afspelen betrouwbaarder.

- **Verbeterde formaatondersteuning** — inclusief **FLAC** (via Core Audio) en **Ogg Vorbis** (via `libvorbisfile`), naast MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF en meer.
- **Slimmer bufferen** — een adaptieve voorbuffer schaalt mee met je verbinding, met een doorlopende ringbuffer die de uitvoer voedt zodat korte netwerkhaperingen niet uitmonden in uitval.
- **Automatisch herstel** — een herbufferingsstatusmachine en herhaallogica met backoff hervatten het afspelen netjes na een moment van zwak signaal in plaats van het nummer te stoppen.
- **Minder onderbrekingen** — dezelfde engine stuurt lokale bestanden, cloudstreams, mediaservers en internetradio aan, dus het gedrag is overal consistent.

## Nu speelt en CarPlay

De schermen die je daadwerkelijk bekijkt tijdens het luisteren — het **vergrendelscherm**, **CarPlay** en de afstandsbedieningsknoppen van je auto of koptelefoon — zijn nauwkeuriger en sneller in 8.7.

- **Nauwkeurigere Nu speelt-info.** Evermusic legt de status van de speler onder een lock vast voordat deze wordt gepubliceerd, zodat de titel, verstreken tijd, duur en afspeel-/pauzestatus het nooit oneens kunnen zijn met elkaar op het vergrendelscherm of in de auto. Buffer- en laadstatussen worden nu correct gerapporteerd in plaats van "spelend" te tonen terwijl een nummer nog wordt opgehaald.
- **Betrouwbare afstandsbediening.** Afspelen, pauzeren, volgende, vorige, zoeken, overslaan, shuffle, herhalen en afspeelsnelheid reageren allemaal consistent vanaf koptelefoonknoppen, autobediening en het vergrendelscherm, aangedreven door `MPRemoteCommandCenter`.
- **Snellere CarPlay-albumhoezen.** Albumhoezen laden nu meerdere keren sneller in lange lijsten (batch-tempo teruggebracht van 1,0s naar 0,25s, waarbij het eerste zichtbare scherm direct laadt), en ze verschijnen nu in de compacte iOS 26 CarPlay-lijstrijen die eerder geen hoes toonden.
- **CarPlay-sortering en stabiliteitsverbeteringen.** Snellere sortering in grote bibliotheken en versteviging tegen randgevalcrashes bij het scrollen door lange lijsten.
- **Beperkte metadata-updates.** Nu speelt- en afstandsbedieningsupdates worden beperkt zodat snelle wijzigingen het systeem niet langer overspoelen, wat de bediening op het vergrendelscherm en in CarPlay responsief houdt.

## Overige verbeteringen

- **Liquid Glass-ontwerpverfijningen** door de hele app — doorschijnende oppervlakken, soepelere animaties en verfijnde bediening op iOS, iPadOS en macOS.
- **Nieuwe beginschermwidgets** met verbeterde updatelogica die ze synchroon houdt zonder extra batterij te verbruiken.
- Oplossingen voor recente iOS-releases.
- Lokalisatieoplossingen in meerdere talen.
- Veel kleinere verbeteringen op basis van je e-mails en App Store-recensies.

## Waarom deze update ertoe doet

Evermusic 8.7 is opgebouwd rond één idee: **je muziek zou op zijn best moeten klinken, op elke bron.**

1. **Hele albums, zoals bedoeld.** Echt naadloos afspelen betekent dat livesets, DJ-mixen en conceptalbums eindelijk klinken zoals de artiest ze heeft gemasterd.
2. **Een studio in je zak.** Reverb, Delay, Distortion, Compressor, Crossfeed, een opnieuw ontworpen equalizer en luidheidsnormalisatie geven je echte controle over je geluid, niet zomaar een aan/uit-schakelaar.
3. **Overal dezelfde ervaring.** Lokale bestanden, cloudschijven, mediaservers en internetradio lopen allemaal door dezelfde herbouwde engine, met een nauwkeurige Nu speelt en een snellere CarPlay erbovenop.

## Haal Evermusic 8.7

[**Download Evermusic uit de App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) of werk bij vanuit de App Store. Evermusic is een gratis download met optionele in-app upgrades voor geavanceerde functies.

Als je de app leuk vindt, laat dan een beoordeling achter in de App Store — dat helpt echt. Feedback of loop je tegen een probleem aan? Mail ons op **support@everappz.com**. We lezen elk bericht.

## Veelgestelde vragen

{{% details title="Wat is nieuw in Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 voegt echt naadloos afspelen toe, vijf studio-audio-effecten (Reverb, Delay, Distortion, Compressor en Crossfeed), EBU R128 volumenormalisatie, een opnieuw ontworpen 10-bands equalizer met aangepaste presets en import/export, een herbouwde AVAudioEngine-streamengine met verbeterde formaatondersteuning (inclusief FLAC en Ogg Vorbis), een snellere en nauwkeurigere CarPlay en Nu speelt, Liquid Glass-ontwerpupdates, vernieuwde beginschermwidgets, en bug- en lokalisatieoplossingen.
{{% /details %}}

{{% details title="Heeft Evermusic echt naadloos afspelen?" closed="true" %}}
Ja. Vanaf Evermusic 8.7 is het afspelen echt naadloos: er is geen pauze, klik of tik tussen nummers. De engine buffert en decodeert het volgende nummer alvast terwijl het huidige speelt en draagt de overdracht over tussen audiosamples op een doorlopende ringbuffer, zodat de overgang onhoorbaar is. Het werkt voor lokale bestanden, cloudstreams en mediaservers, en is ideaal voor livealbums, DJ-mixen en conceptalbums.
{{% /details %}}

{{% details title="Welke audio-effecten bevat Evermusic 8.7?" closed="true" %}}
Vijf realtime effecten: **Reverb** (13 ruimte-presets, wet/dry-mix), **Delay/Echo** (10 presets met delaytijd, feedback, low-pass en mix), **Distortion** (22 karakter-presets met pre-gain en mix), **Compressor** (een volwaardige dynamiekprocessor met drempel, ratio, attack, release, expansie en makeup-gain, plus 10 presets) en **Crossfeed** (Bauer bs2b koptelefoon-crossfeed met niveau- en cutoff-bedieningen en 6 presets). Elk effect wordt geleverd met samengestelde presets, en je aangepaste instellingen worden tussen sessies onthouden.
{{% /details %}}

{{% details title="Wat is Crossfeed en waarom zou ik het gebruiken?" closed="true" %}}
Crossfeed mengt een kleine, gefilterde hoeveelheid van elk stereokanaal in het andere, zoals je oren van nature echte luidsprekers in een ruimte horen. Op een koptelefoon vermindert dit de overdreven "in-je-hoofd"-scheiding van hard gepande opnames en maakt het lang luisteren comfortabeler. Evermusic gebruikt het bekende Bauer stereophonic-to-binaural (bs2b) algoritme en bevat presets zoals Chu Moy en Jan Meier. Het is vooral effectief op oudere stereomixen uit de jaren 60 en 70.
{{% /details %}}

{{% details title="Hoe werkt volumenormalisatie in Evermusic?" closed="true" %}}
Evermusic 8.7 meet de waargenomen luidheid van elk nummer met de EBU R128-standaard (ITU-R BS.1770) in realtime en past het niveau voorzichtig aan naar een consistent doel zodat nummers niet in volume springen. Het vereist geen ReplayGain-tags en wijzigt je bestanden niet. Vier presets zijn beschikbaar — Licht (−20 LUFS), Standaard (−16 LUFS), Sterk (−14 LUFS) en Nacht (−23 LUFS) — en de normalisatie reset netjes wanneer je zoekt of van nummer wisselt.
{{% /details %}}

{{% details title="Is de volumenormalisatie van Evermusic hetzelfde als ReplayGain?" closed="true" %}}
Het bereikt hetzelfde doel — consistente luidheid tussen nummers — maar werkt anders. ReplayGain vertrouwt op luidheidstags die in je bestanden zijn opgeslagen. De normalisator van Evermusic meet de luidheid live met EBU R128, dus hij werkt op elke bron, inclusief cloudstreams en internetradio, zelfs als de bestanden helemaal geen tags hebben.
{{% /details %}}

{{% details title="Hoeveel banden heeft de Evermusic-equalizer, en kan ik mijn eigen presets maken?" closed="true" %}}
De Evermusic-equalizer is een 10-bands grafische equalizer die 32 Hz tot 16 kHz bestrijkt, met elke band instelbaar van −12 dB tot +12 dB in stappen van 0,1 dB en een preamp van −24 dB tot +24 dB. Hij bevat ingebouwde presets, laat je aangepaste presets maken en bewaren, en ondersteunt het importeren en exporteren van presets als .eqp-bestanden zodat je ze tussen apparaten kunt verplaatsen of delen.
{{% /details %}}

{{% details title="Wat is er veranderd in de equalizer van Evermusic 8.7?" closed="true" %}}
De equalizer is opnieuw ontworpen met nieuwe, preciezere schuifregelaars die de iOS 26-systeemschuifregelaar en Liquid Glass-look overnemen, sneller en soepeler schakelen tussen presets, en een betere lay-out in liggend formaat en op iPad (een horizontale preset-balk in staand formaat en een verticale preset-kolom in liggend formaat). Aangepaste presets en .eqp import/export worden ondersteund.
{{% /details %}}

{{% details title="Ondersteunt Evermusic 8.7 FLAC en Ogg Vorbis?" closed="true" %}}
Ja. De herbouwde engine speelt FLAC (via Core Audio) en Ogg Vorbis (via libvorbisfile), samen met MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF en meer, vanaf lokale bestanden, cloudschijven en mediaservers.
{{% /details %}}

{{% details title="Wat is verbeterd in CarPlay en op het vergrendelscherm?" closed="true" %}}
CarPlay-albumhoezen laden meerdere keren sneller in lange lijsten en verschijnen nu in de compacte iOS 26-lijstrijen die er eerder geen toonden. Nu speelt-informatie op het vergrendelscherm en in CarPlay is nauwkeuriger — de titel, verstreken tijd, duur en afspeel-/pauzestatus worden samen vastgelegd zodat ze het niet oneens kunnen zijn, en bufferstatussen worden correct gerapporteerd. Afstandsbedieningen (afspelen, pauzeren, volgende, vorige, zoeken, shuffle, herhalen, snelheid) reageren betrouwbaar vanaf koptelefoons en de auto, en CarPlay-sortering in grote bibliotheken is sneller.
{{% /details %}}

{{% details title="Werken de audio-effecten en equalizer met cloudstreaming en CarPlay?" closed="true" %}}
Ja. De effecten, equalizer en volumenormalisatie draaien native binnen de afspeelengine, dus ze worden toegepast op alles wat Evermusic afspeelt — lokale bestanden, cloudschijven, mediaservers en internetradio — en ze blijven werken tijdens het afspelen via CarPlay en, waar ondersteund, via AirPlay en Chromecast.
{{% /details %}}

{{% details title="Is Evermusic 8.7 gratis om bij te werken, en welke apparaten worden ondersteund?" closed="true" %}}
Ja. Evermusic is een gratis download uit de App Store, en 8.7 is een gratis update voor bestaande gebruikers, met optionele in-app upgrades voor geavanceerde functies. Het draait op iPhone, iPad en Mac. CarPlay vereist een CarPlay-compatibel voertuig of hoofdunit.
{{% /details %}}
