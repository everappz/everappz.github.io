---
title: "Mediaspelare"
date: 2020-02-01
lastmod: 2026-06-01
description: "Lär dig använda Evervideo mediaspelaren på iPhone, iPad och Mac. Picture-in-Picture, hårdvaruaccelererad H.264 / HEVC-avkodning, ljud- och videoekvalisatorer, primära och sekundära undertexter, val av ljud- och videospår, videoskalning och -rotation, uppspelningshastighet, sovtimer, AirPlay 2, Google Chromecast, RTSP-strömmar och den kompakta alltid-synliga spelaren."
keywords: [
  "Evervideo spelarguid", "videospelarinställningar", "Evervideo ekvalisator",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "videoundertexer iPhone", "externa SRT-undertexter",
  "ASS SSA undertextspelare", "libass iOS",
  "dubbla undertexter språkinlärning",
  "videoekvalisator ljusstyrka kontrast", "ljudekvalisator videospelare",
  "videospelares rotationslås", "videoskalningsläge iOS",
  "hårdvaru H.264 avkodare iPhone", "hårdvaru HEVC avkodare iPad",
  "uppspelningshastighet video", "FFmpeg videospelare iOS",
  "RTSP iPhone spelare", "kompakt videospelare",
  "VR 360 videospelare iPhone"
]
tags: ["guide", "evervideo", "spelare", "PiP", "undertexter", "videoekvalisator"]
readingTime: 14
---


Mediaspelaren är appens huvudskärm där du styr uppspelning och de flesta av Evervideo's funktioner. Den spelar både video- och ljudfiler och är byggd på en anpassad FFmpeg-baserad spelare med hårdvaruaccelererad H.264 och HEVC-avkodning som gör det tunga lyftet. Låt oss utforska hur man använder den.

## Åtkomst till mediaspelaren

Du kan komma till helskärmsspelaren från den kompakta spelaren. På iPhone sitter den kompakta spelaren längst upp på huvudskärmen. På iPad och Mac är den på vänster sida (eller toppen av huvudpanelen). För att fälla ihop helskärmsspelaren tillbaka till den kompakta vyn, tryck på stängknappen i det nedre högra hörnet eller svep nedåt. För att helt dölja den kompakta spelaren, tryck och svep nedåt en gång till.

Den kompakta spelaren förblir synlig medan du bläddrar i ditt bibliotek, din filhanterare eller dina inställningar, så du förlorar aldrig din video medan du letar efter nästa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo fullskärmsmediaspelare" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Stödda video- och ljudformat

Evervideo spelar praktiskt taget varje modern behållare och kodek via den medföljande FFmpeg-motorn, med hårdvaruaccelererad H.264 och HEVC-avkodning på stödda enheter.

- **Videobehållare:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — och många fler.
- **Videokodekar:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus praktiskt taget varje annan kodek som FFmpeg stöder.
- **Ljudkodekar:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — och många fler.
- **Undertextformat:** SRT, VTT (WebVTT), ASS / SSA och inbäddade text- eller bildundertextspår.
- **Strömningsprotokoll:** HTTP / HTTPS, HLS (m3u8), RTSP (IP-kameror och IPTV) och direkt filströmning via SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Det täcker praktiskt taget varje videofil du sannolikt stöter på — inklusive MKV-kopior, säkerhetskamera RTSP-strömmar och AV1 webm-webbhämtningar.

## Uppspelningskontroller

Längst ned på spelarskärmen ser du knappar för Spela, Pausa, Nästa och Föregående. Det finns också valfria knappar som Hoppa framåt och Hoppa bakåt (standard 10 sekunder) som du kan aktivera i appinställningarna. Håll ned Nästa / Föregående-knapparna för att snabbspola framåt eller bakåt. Dra uppspelningsreglaget för att hoppa till valfri position.

## Upprepa och blanda

Tryck på upprepningsknappen för att cykla igenom upprepningslägen:

- **Upprepa alla** — loopar varje video i din kö.
- **Upprepa en** — upprepar bara den aktuella videon.
- **Upprepa stopp** — pausar när den aktuella videon slutar.
- **Ingen upprepning** — spelar kön en gång igenom utan att upprepa.

Använd knappen **Blanda** för att slumpmässigt ordna videorna i kön.

## Picture-in-Picture (PiP)

På iPhone och iPad stöder Evervideo fullt ut Picture-in-Picture (PiP). Tryck på PiP-ikonen på spelarskärmen eller svep helt enkelt Evervideo till bakgrunden — videon fortsätter spelas i ett flytande fönster ovanför varje annan app. Dra det flytande fönstret till vilket hörn som helst; nyp för att ändra storlek; tryck en gång för att visa grundläggande play / paus / hoppa-kontroller; tryck på den lilla expanderingsknappen för att återgå till det fullständiga Evervideo.

PiP fungerar med alla videoformat som Evervideo spelar, inklusive molnströmmade filer och RTSP-strömmar. PiP fortsätter också att köra när din telefon är låst (beroende på din Auto-Lock-inställning).

## Kompakt spelare

Den kompakta spelaren är en beständig mini-spelare som stannar synlig längst upp på varje skärm i appen medan du bläddrar i biblioteket, filhanteraren eller inställningarna. Tryck på den för att expandera till helskärmsspelaren; svep nedåt för att fälla ihop den igen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo videoinställningar från den kompakta spelaren på huvudskärmen" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

För AirPlay, tryck på AirPlay-knappen på spelaren. Evervideo stöder AirPlay 2, så du kan strömma video till Apple TV, HomePod eller valfri AirPlay 2-kompatibel högtalare eller smart-TV. I en installation med flera AirPlay-enheter kan du dirigera ljud till flera mottagare samtidigt.

## Google Chromecast

För Google Cast-användare visas Cast-ikonen på spelaren. Tryck på den för att välja en enhet och börja casta. Se till att din telefon och Cast-mottagaren är på samma Wi-Fi-nätverk. Inte alla kodekar stöds av Chromecast-hårdvaran — vissa filer kan behöva transkodning.

## RTSP Live-strömmar

Evervideo kan spela RTSP-källor direkt — IP-kameror, dörrklockskameror, IPTV-strömmar, sändningsflöden och valfri `rtsp://`-URL. Lägg till strömmen som en RTSP-anslutning i Filer → Online-länkar → Lägg till länk, tryck sedan på den för att börja titta. RTSP-strömmar fungerar i Picture-in-Picture, den kompakta spelaren och de castar via AirPlay 2 och Chromecast precis som en vanlig video.

## Val av ljudspår

För videor med flera ljudspår (kommentar, alternativa språkdubbningar, regissörsspår), tryck på Fler åtgärder-knappen på spelaren och välj Ljudspår — välj sedan det spår du vill ha. Detta är viktigt för utländska filmer, BDMV / MKV-filer med flera dubbningar och instruktionsinnehåll med kommentarspår.

## Val av videospår

Vissa videofiler inkluderar flera videoströmmar (multi-vinkel Blu-rays, alternativa klippningar). Välj Videospår från Fler åtgärder-menyn för att växla mellan dem under uppspelning.

## Undertexter — interna och externa

Evervideo ger dig finkornig kontroll över undertexter:

- **Undertextspår** — välj från spår inbäddade i filen.
- **Externa undertextfiler** — ladda `.srt`, `.vtt`, `.ass` eller `.ssa`-filer från din enhet, iCloud Drive eller ansluten molntjänst.
- **Libass-rendering** — avancerad ASS / SSA-styling (teckensnitt, färger, positioner, karaoke-effekter) renderas korrekt tack vare medföljande libass.
- **Teckensnittsval** — välj ett anpassat teckensnitt för primära undertexter och ett separat teckensnitt för sekundära undertexter. Medföljande teckensnitt plus eventuella teckensnitt installerade på din enhet är tillgängliga.

Du kan konfigurera allt detta i Inställningar → Undertexter före uppspelning, eller använda Fler åtgärder → Undertexter från spelaren för att byta i farten.

## Ljudekvalisator

Evervideo inkluderar en full ljudekvalisator för att stämma videoens ljudspår för dina hörlurar, högtalare eller hi-fi-uppställning. Tryck på ekvalisatorikonen på volymvyn (eller åtgärden Ljudekvalisator på spelarens Fler åtgärder-meny), slå på ekvalisatorn med reglaget i det övre högra hörnet och välj antingen en förinställning eller dra bandreglagen för att bygga din egen. Anpassade förinställningar kan exporteras och importeras så att du kan dela dem mellan enheter eller säkerhetskopiera dem.

## Videoekvalisator

För att stämma bilden tillhandahåller Evervideo en dedikerad videoekvalisator — justera ljusstyrka, kontrast, mättnad och nyans i realtid under uppspelning. Precis som ljudekvalisatorn kan anpassade videoförinställningar exporteras och importeras för delning eller säkerhetskopiering. Använd den för att ljusa upp en mörk scen en solig dag, öka mättnaden på urtvättat innehåll eller värma upp ett kallt färgskifte.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo videoekvalisator" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Videoskalningsläge

Välj hur videon fyller skärmen:

- **Passa** — bevara det ursprungliga bildförhållandet; svarta fält där det behövs.
- **Fyll** — fyll hela skärmen, klipp videon om det behövs.
- **Sträck** — sträck videon för att fylla skärmen, förvrängning om nödvändigt.
- **Original** — behåll den ursprungliga upplösningen 1:1.

## Videorotation

För videor inspelade med fel orientering, välj **Fler åtgärder → Rotation** och välj **0°**, **90°**, **180°** eller **270°** för att rotera bilden utan att lämna spelaren.

## Hårdvaruavkodning (H.264 och HEVC)

I Inställningar → Spelare → Video kan du aktivera / inaktivera Hårdvaruavkoda H.264 och Hårdvaruavkoda H.265 (HEVC) oberoende. Hårdvaruavkodning är snabbare, använder mindre batteri och körs svalare — men i sällsynta fall (korrupta filer, exotiska profiler) kan du behöva inaktivera hårdvaruavkodning och falla tillbaka på mjukvaruavkodning med FFmpeg. Evervideo låter dig göra det fil-för-fil från spelarens Fler åtgärder-meny.

## VR 360° Viewport

Evervideo inkluderar ett VR / 360°-visningsfönster för sfäriska videofiler. När du spelar en 360°-video kan du dra för att titta runt, nypa för att zooma och Evervideo vrider renderingen i realtid.

## Uppspelningshastighet

Tryck på Hastighetskontrollen på spelarens verktygsfält för att ändra uppspelningshastigheten — sakta ner den för analys (0,25× eller 0,5×) eller snabba upp den för handledningar och föreläsningar (1,25×, 1,5×, 2× och upp till 3×). Tryck på konfigurationsikonen i det övre högra hörnet av Hastighetsskärmen för att växla till precist läge med finare justeringar. Tonhöjdskorrigering per spår är också tillgänglig.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo uppspelningshastighet på huvudverktygsfältet" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Spelarkö

För att se din spelarkö, tryck på kö-knappen på spelaren. Varje video i kön har fler åtgärder — tryck på de tre punkterna för att visa dem. För att ändra ordningen på en video i kön, använd omordningsindikator nära titeln och dra den till en ny position.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo uppspelningskö" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Sovtimer

Öppna Inställningar → Spelare → Sovtimer, slå på den och välj hur länge du vill att uppspelningen ska fortsätta innan den automatiskt stoppar. Du kan också lägga till Sovtimer-knappen direkt på spelarens huvudskärm via Inställningar → Spelare → Personalisering → Huvudskärmsåtgärder.

## Spelarbokmärken

Spara din plats i långa videor — föreläsningar, audioböcker-på-video, handledningar, timslånga YouTube-hämtningar — genom att trycka på Lägg till bokmärke från Fler åtgärder-menyn. Bokmärken visas i videons Fler åtgärder → Bokmärkeslista och kvarstår mellan sessioner.

## Fler åtgärder-menyn

Tryck på knappen **Fler åtgärder "..."** på spelaren för att komma åt ytterligare funktioner.

- **Fortsätt uppspelning** — återuppta kön från den senaste positionen.
- **Sök** — hitta en specifik video i din kö.
- **Bokmärken** — visa och hoppa till bokmärken.
- **Hastighet** — justera uppspelningshastigheten.
- **Senaste** — nyligen spelade videor.
- **Favoriter** — favoriserade videor.
- **Ljudekvalisator** — aktivera ljudekvalisatorn.
- **Videoekvalisator** — aktivera videoekvalisatorn.
- **Ljudspår** — välj ljudströmmen.
- **Videospår** — välj videoströmmen.
- **Undertexter** — primärt / sekundärt spår, extern fil, teckensnitt.
- **Rotation** — rotera bilden 0° / 90° / 180° / 270°.
- **Skalningsläge** — Passa / Fyll / Sträck / Original.
- **Picture-in-Picture** — gå in i PiP-läge.
- **AirPlay** / **Chromecast** — skicka till en enhet.
- **Sovtimer** — ange en timer för att stoppa uppspelning.
- **Spara kö till spellista** — spara den aktuella kön som en ny spellista.
- **Ta bort kö** — rensa kön och stoppa uppspelning.
- **Inställningar** — hoppa direkt till spelarinställningar.
- **Hjälp** — öppna vägledning.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo spelarens Fler åtgärder-skärm" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Spelarinställningar

Det fullständiga inställningsträdet för spelaren dokumenteras i [Inställningsguiden](/docs/guide/evervideo/evervideo-guide-settings/). De mest använda avsnitten:

- **Allmänt** — Upprepningsläge, Blandningsläge, Spara spelartillstånd, Spara uppspelningsposition, Hoppatidsintervaller.
- **Video** — Hårdvaruavkoda H.264 / HEVC, videoekvalisator, skalningsläge, rotation, visningsläge, föredragen FPS, föredraget pixelformat, VR-viewport.
- **Ljud** — Ljudekvalisator, samplingsfrekvens, kanaler, IO-buffertvaraktighet, blandat läge.
- **Undertexter** — Primärt / sekundärt spår, val av extern fil, teckensnitt, sekundärt teckensnitt.
- **Enheter** (iOS) — AirPlay / Chromecast.
- **Personalisering** — Spelarlayoutstil (Minimalt / Botten / Antikt / Klassiskt), huvudskärmsåtgärder, låsskärmskontroller.
- **Uppspelningscache** — diskcache för smidigare strömning.
- **Sovtimer** — automatiskt stopp.

## Tillgänglighet

Evervideo är fullt tillgängligt med VoiceOver. Varje komponent har en väldesignad etikett och beskrivning. När VoiceOver är aktivt växlar appen till Textläge så att bara meningsfulla element visas — vilket förbättrar navigeringshastigheten och tydligheten. Du kan också aktivera Textläge i Inställningar → Tillgänglighet → Textläge.

### Justera skjutreglage med VoiceOver

1. **Välj skjutreglaget** — svep vänster eller höger tills VoiceOver meddelar det.
2. **Justera värdet** — dubbeltryck och håll ned skjutreglaget, dra sedan uppåt eller nedåt för att snabbt ändra värdet. VoiceOver meddelar det nya värdet medan du går.

Andra komponenter fungerar som förväntat, med systemtillhandahållna VoiceOver-mönster.
