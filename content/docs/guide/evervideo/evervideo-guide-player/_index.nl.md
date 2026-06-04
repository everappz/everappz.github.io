---
title: "Mediaspeler"
date: 2020-02-01
lastmod: 2026-06-01
description: "Leer hoe je de Evervideo mediaspeler gebruikt op iPhone, iPad en Mac. Picture-in-Picture, hardwareversnelde H.264 / HEVC-decodering, audio- en video-equalizers, primaire en secundaire ondertitels, selectie van audio- en videosporen, videoschaling en -rotatie, afspeelsnelheid, slaaptimer, AirPlay 2, Google Chromecast, RTSP-streams en de compacte altijd-zichtbare speler."
keywords: [
  "Evervideo spelerhandleiding", "videospeler instellingen", "Evervideo equalizer",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "video ondertitel iPhone", "externe SRT ondertitels",
  "ASS SSA ondertitelspeler", "libass iOS",
  "dubbele ondertitels taalleren",
  "video-equalizer helderheid contrast", "audio-equalizer videospeler",
  "videospeler rotatieslot", "videoschalingsmodus iOS",
  "hardware H.264 decoder iPhone", "hardware HEVC decoder iPad",
  "afspeelsnelheid video", "FFmpeg videospeler iOS",
  "RTSP iPhone speler", "compacte videospeler",
  "VR 360 videospeler iPhone"
]
tags: ["handleiding", "evervideo", "speler", "PiP", "ondertitels", "video-equalizer"]
readingTime: 14
---


De Mediaspeler is het hoofdscherm van de app waar u het afspelen en de meeste functies van Evervideo beheert. Het speelt zowel video- als audiobestanden af en is gebouwd op een aangepaste FFmpeg-speler met hardwareversnelde H.264- en HEVC-decodering. Laten we eens bekijken hoe u het gebruikt.

## Toegang tot de mediaspeler

U kunt de volledige speler bereiken vanuit de compacte spelerbalk. Op iPhone zit de compacte speler bovenaan het hoofdscherm. Op iPad en Mac bevindt die zich aan de linkerkant (of boven aan het hoofdpaneel). Om de volledige speler terug te klappen naar de compacte weergave, tikt u op de sluitknop rechtsonder of veegt u omlaag. Om de compacte speler volledig te verbergen, tikt u nogmaals en veegt u omlaag.

De compacte speler blijft zichtbaar terwijl u door uw bibliotheek, bestandsbeheer of instellingen bladert, zodat u uw video nooit verliest terwijl u naar het volgende zoekt.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Volledige Mediaspeler" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Ondersteunde video- en audioformaten

Evervideo speelt vrijwel elke moderne container en codec af via de meegeleverde FFmpeg-engine, met hardwareversnelde H.264- en HEVC-decodering op ondersteunde apparaten.

- **Videocontainers:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — en nog veel meer.
- **Videocodecs:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus vrijwel elke andere codec die FFmpeg ondersteunt.
- **Audiocodecs:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — en nog veel meer.
- **Ondertitelformaten:** SRT, VTT (WebVTT), ASS / SSA, en ingebedde tekst- of beeldondertitelsporen.
- **Streamingprotocollen:** HTTP / HTTPS, HLS (m3u8), RTSP (IP-camera's en IPTV), en directe bestandsstreaming via SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Dit omvat vrijwel elk videobestand dat u tegenkomt — inclusief MKV-rips, RTSP-streams van beveiligingscamera's en AV1 webm-webdownloads.

## Afspeelknoppen

Onderaan het spelerscherm ziet u knoppen voor Afspelen, Pauzeren, Volgende en Vorige. Er zijn ook optionele knoppen zoals Snel vooruitspoelen en Snel terugspoelen (standaard 10 seconden) die u in de app-instellingen kunt inschakelen. Houd de knoppen Volgende / Vorige ingedrukt om snel voor- of terug te spoelen. Sleep de afspeelschuifregelaar om naar een willekeurige positie te springen.

## Herhalen en shufflen

Tik op de herhaalknop om door de herhaalmodi te bladeren:

- **Alles herhalen** — herhaalt elke video in uw wachtrij.
- **Eén herhalen** — herhaalt alleen de huidige video.
- **Herhalen stoppen** — pauzeert wanneer de huidige video eindigt.
- **Niet herhalen** — speelt de wachtrij één keer af zonder herhaling.

Gebruik de **Shuffle**-knop om de volgorde van video's in de wachtrij te willekeurig maken.

## Picture-in-Picture (PiP)

Op iPhone en iPad ondersteunt Evervideo volledig Picture-in-Picture (PiP). Tik op het PiP-pictogram op het spelerscherm of veeg Evervideo gewoon naar de achtergrond — de video speelt door in een zwevend venster boven elke andere app. Sleep het zwevende venster naar een hoek; knijp om het formaat te wijzigen; tik eenmaal om basiscontroles voor afspelen / pauzeren / overslaan te tonen; tik op de kleine uitvouwknop om terug te keren naar volledig Evervideo.

PiP werkt met elk videoformaat dat Evervideo afspeelt, inclusief cloudgestreamde bestanden en RTSP-streams. PiP blijft ook actief terwijl uw telefoon vergrendeld is (afhankelijk van uw Auto-vergrendeling-instelling).

## Compacte speler

De compacte speler is een permanente minispeler die zichtbaar blijft bovenaan elk scherm in de app terwijl u door de bibliotheek, de bestandsbeheerder of de instellingen bladert. Tik erop om de volledige speler te openen; veeg omlaag om hem terug te klappen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Video-instellingen vanuit de Compacte Speler op het Hoofdscherm" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Voor AirPlay tikt u op de AirPlay-knop op de speler. Evervideo ondersteunt AirPlay 2, zodat u video kunt streamen naar Apple TV, HomePod of een AirPlay 2-compatibele speaker of smart-tv. Bij een opstelling met meerdere AirPlay-apparaten kunt u audio tegelijkertijd naar meerdere ontvangers sturen.

## Google Chromecast

Voor Google Cast-gebruikers verschijnt het Cast-pictogram op de speler. Tik erop om een apparaat te kiezen en het casten te starten. Zorg ervoor dat uw telefoon en de Cast-ontvanger op hetzelfde Wi-Fi-netwerk zijn. Niet elke codec wordt ondersteund door Chromecast-hardware — sommige bestanden hebben mogelijk transcodering nodig.

## RTSP-directestreams

Evervideo kan RTSP-bronnen direct afspelen — IP-camera's, deurbelvideo's, IPTV-streams, uitzendingen en elke andere `rtsp://`-URL. Voeg de stream toe als RTSP-verbinding in Bestanden → Online links → Link toevoegen, tik erop om te beginnen met kijken. RTSP-streams werken in Picture-in-Picture, de compacte speler en ze worden uitgezonden via AirPlay 2 en Chromecast net als een gewone video.

## Selectie van audiospoor

Voor video's met meerdere audiosporen (commentaar, taaldubbing, regisseurssporen), tikt u op de knop Meer acties op de speler en kiest u Audiospoor — dan selecteert u het gewenste spoor. Dit is essentieel voor buitenlandse films, BDMV / MKV-bestanden met meerdere nagesynchronisaties en instructiemateriaal met commentaarsporen.

## Selectie van videospoor

Sommige videobestanden bevatten meerdere videostreams (Blu-rays met meerdere hoeken, alternatieve versies). Kies Videospoor in het menu Meer acties om tijdens het afspelen tussen hen te schakelen.

## Ondertitels — intern en extern

Evervideo geeft u fijnmazig controle over ondertitels:

- **Ondertitelspoor** — kies uit de in het bestand ingebedde sporen.
- **Externe ondertitelbestanden** — laad `.srt`-, `.vtt`-, `.ass`- of `.ssa`-bestanden van uw apparaat, iCloud Drive of een verbonden clouddienst.
- **Libass-rendering** — geavanceerde ASS / SSA-opmaak (lettertypen, kleuren, posities, karaoke-effecten) wordt correct gerenderd dankzij de meegeleverde libass.
- **Lettertypeselectie** — kies een aangepast lettertype voor primaire ondertitels en een apart lettertype voor secundaire ondertitels. Meegeleverde lettertypen plus elk op uw apparaat geïnstalleerd lettertype zijn beschikbaar.

U kunt dit alles configureren in Instellingen → Ondertitels vóór het afspelen, of gebruik Meer acties → Ondertitels in de speler om tijdens het afspelen te wisselen.

## Audio-equalizer

Evervideo bevat een volledige audio-equalizer om videosoundtracks af te stemmen voor uw koptelefoon, speakers of hi-fi-opstelling. Tik op het equalizer-pictogram in de volumeweergave (of de Audio-equalizer-actie in het menu Meer acties van de speler), zet de equalizer aan met de schakelaar in de rechterbovenhoek en kies een preset of sleep de bandschuifregelaars om uw eigen preset te bouwen. Aangepaste presets kunnen worden geëxporteerd en geïmporteerd zodat u ze kunt delen tussen apparaten of een back-up kunt maken.

## Video-equalizer

Voor het afstemmen van het beeld biedt Evervideo een speciale video-equalizer — pas helderheid, contrast, verzadiging en tint in realtime aan tijdens het afspelen. Net als de audio-equalizer kunnen aangepaste videopresets worden geëxporteerd en geïmporteerd voor delen of back-up. Gebruik het om een donker ​​scène op een zonnige dag op te helderen, de verzadiging van uitgebleekte inhoud te verhogen of een koude kleurcast op te warmen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Video-equalizer" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Videoschalingsmodus

Kies hoe de video het scherm vult:

- **Passend** — bewaar de originele beeldverhouding; zwarte balken waar nodig.
- **Vullen** — vul het hele scherm, waarbij de video indien nodig wordt bijgesneden.
- **Uitrekken** — rek de video uit om het scherm te vullen, indien nodig vervormd.
- **Origineel** — behoud de native resolutie op 1:1.

## Videorotatie

Voor video's die met de verkeerde oriëntatie zijn opgenomen, kiest u **Meer acties → Rotatie** en selecteert u **0°**, **90°**, **180°** of **270°** om het beeld te roteren zonder de speler te verlaten.

## Hardwaredecodering (H.264 en HEVC)

In Instellingen → Speler → Video kunt u Hardwarematig H.264 decoderen en Hardwarematig H.265 (HEVC) decoderen onafhankelijk in- of uitschakelen. Hardwaredecodering is sneller, verbruikt minder batterij en draait koeler — maar in zeldzame gevallen (beschadigde bestanden, exotische profielen) moet u hardwaredecodering mogelijk uitschakelen en terugvallen op software-FFmpeg-decodering. Evervideo laat u dit bestandsgewijs doen vanuit het menu Meer acties van de speler.

## VR 360° Viewport

Evervideo bevat een VR / 360° viewport voor sferische videobestanden. Bij het afspelen van een 360°-video kunt u slepen om rond te kijken, knijpen om te zoomen en Evervideo past de rendering in realtime aan.

## Afspeelsnelheid

Tik op het snelheidsbesturingselement op de spelerwerkbalk om de afspeelsnelheid te wijzigen — vertraag voor analyse (0,25× of 0,5×) of versnel voor tutorials en lezingen (1,25×, 1,5×, 2× en tot 3×). Tik op het configuratiepictogram in de rechterbovenhoek van het snelheidsscherm om naar de precieze modus te schakelen met fijnere aanpassingen. Toonhoogtecorrectie per spoor is ook beschikbaar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Afspeelsnelheid op de Hoofdwerkbalk" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Spelerswachtrij

Om uw spelerswachtrij te bekijken, tikt u op de wachtrij-knop op de speler. Elke video in de wachtrij heeft meer acties — tik op de drie puntjes om ze te bekijken. Om een video in de wachtrij te herordenen, gebruik de herordeneringsindicator bij de titel en sleep het naar een nieuwe positie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Afspeelwachtrij" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Slaaptimer

Open Instellingen → Speler → Slaaptimer, zet hem aan en kies hoe lang u wilt dat het afspelen doorgaat voordat het automatisch stopt. U kunt de slaaptimer-knop ook rechtstreeks aan het hoofdspelerscherm toevoegen via Instellingen → Speler → Personalisatie → Hoofdschermacties.

## Spelerbladwijzers

Sla uw positie op in lange video's — lezingen, audioboeken-op-video, tutorials, uurlange YouTube-downloads — door op Bladwijzer toevoegen te tikken in het menu Meer acties. Bladwijzers verschijnen in de lijst Meer acties → Bladwijzers van de video en blijven bewaard tussen sessies.

## Menu Meer acties

Tik op de knop **Meer acties "..."** op de speler om toegang te krijgen tot extra functies.

- **Verder afspelen** — hervat de wachtrij vanaf de laatste positie.
- **Zoeken** — zoek een specifieke video in uw wachtrij.
- **Bladwijzers** — bekijk en spring naar bladwijzers.
- **Snelheid** — pas de afspeelsnelheid aan.
- **Recenties** — onlangs afgespeelde video's.
- **Favorieten** — als favoriet gemarkeerde video's.
- **Audio-equalizer** — activeer de audio-equalizer.
- **Video-equalizer** — activeer de video-equalizer.
- **Audiospoor** — kies de audiostream.
- **Videospoor** — kies de videostream.
- **Ondertitels** — primair / secundair spoor, extern bestand, lettertype.
- **Rotatie** — draai het beeld 0° / 90° / 180° / 270°.
- **Schalingsmodus** — Passend / Vullen / Uitrekken / Origineel.
- **Picture-in-Picture** — activeer PiP-modus.
- **AirPlay** / **Chromecast** — stuur naar een apparaat.
- **Slaaptimer** — stel een timer in om het afspelen te stoppen.
- **Wachtrij opslaan als afspeellijst** — sla de huidige wachtrij op als nieuwe afspeellijst.
- **Wachtrij verwijderen** — maak de wachtrij leeg en stop het afspelen.
- **Instellingen** — ga direct naar spelerseinstellingen.
- **Help** — open hulp.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Speler Meer acties Scherm" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Spelerinstellingen

De volledige instellingenboom voor de Speler is gedocumenteerd in de [Instellingen handleiding](/docs/guide/evervideo/evervideo-guide-settings/). De meest gebruikte secties:

- **Algemeen** — Herhalingsmodus, Shufflemodus, Spelerstatus opslaan, Afspeelpositie opslaan, Overslaan-tijdsintervallen.
- **Video** — Hardwarematig H.264 / HEVC decoderen, video-equalizer, schalingsmodus, rotatie, weergavemodus, voorkeurs-FPS, voorkeurs-pixelformaat, VR-viewport.
- **Audio** — Audio-equalizer, samplefrequentie, kanalen, IO-bufferduur, gemengde modus.
- **Ondertitels** — Primair / secundair spoor, selectie van extern bestand, lettertype, secundair lettertype.
- **Apparaten** (iOS) — AirPlay / Chromecast.
- **Personalisatie** — Spelersindeling (Minimaal / Onderaan / Antiek / Klassiek), hoofdschermacties, vergrendelingsschermbediening.
- **Afspeelcache** — schijfcache voor soepeler streamen.
- **Slaaptimer** — automatisch stoppen.

## Toegankelijkheid

Evervideo is volledig toegankelijk met VoiceOver. Elk onderdeel heeft een goed ontworpen label en beschrijving. Wanneer VoiceOver actief is, schakelt de app over naar Tekstmodus zodat alleen zinvolle elementen worden weergegeven — wat de navigatiesnelheid en helderheid verbetert. U kunt Tekstmodus ook activeren in Instellingen → Toegankelijkheid → Tekstmodus.

### Schuifregelaars aanpassen met VoiceOver

1. **Selecteer de schuifregelaar** — veeg links of rechts totdat VoiceOver hem aankondigt.
2. **Pas de waarde aan** — dubbeltik en houd de schuifregelaar vast, sleep dan omhoog of omlaag om de waarde snel te wijzigen. VoiceOver kondigt de nieuwe waarde aan terwijl u gaat.

Andere onderdelen werken zoals verwacht, met systeemgeleverde VoiceOver-patronen.
