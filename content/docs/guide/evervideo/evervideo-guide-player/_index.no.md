---
title: "Medieavspiller"
date: 2020-02-01
lastmod: 2026-06-01
description: "Lær hvordan du bruker Evervideo medieavspilleren på iPhone, iPad og Mac. Picture-in-Picture, maskinvareakselerert H.264 / HEVC-dekoding, lyd- og videoequalizer, primære og sekundære undertekster, valg av lyd- og videospor, videoskalering og -rotasjon, avspillingshastighet, sove-timer, AirPlay 2, Google Chromecast, RTSP-strømmer og den kompakte alltid-synlige avspilleren."
keywords: [
  "Evervideo avspillerguide", "videospiller innstillinger", "Evervideo equalizer",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "video undertekst iPhone", "ekstern SRT undertekst",
  "ASS SSA undertekstspiller", "libass iOS",
  "doble undertekster språklæring",
  "video-equalizer lysstyrke kontrast", "lyd-equalizer videospiller",
  "videospiller rotasjonslås", "videoskateringsmodus iOS",
  "maskinvare H.264 dekoder iPhone", "maskinvare HEVC dekoder iPad",
  "avspillingshastighet video", "FFmpeg videospiller iOS",
  "RTSP iPhone spiller", "kompakt videospiller",
  "VR 360 videospiller iPhone"
]
tags: ["guide", "evervideo", "avspiller", "PiP", "undertekster", "video-equalizer"]
readingTime: 14
---


Medieavspilleren er hovedskjermen i appen der du styrer avspilling og de fleste funksjonene i Evervideo. Den spiller av både video- og lydfiler og er bygget på en tilpasset FFmpeg-basert avspiller med maskinvareakselerert H.264- og HEVC-dekoding som gjør det tunge arbeidet. La oss utforske hvordan du bruker den.

## Tilgang til medieavspilleren

Du kan nå fullskjermsavspilleren fra den kompakte avspillerlinjen. På iPhone sitter den kompakte avspilleren øverst på hovedskjermen. På iPad og Mac befinner den seg på venstre side (eller øverst på hovedpanelet). For å kollapse fullskjermsavspilleren tilbake til kompakt visning, trykk på lukkeknappen nederst til høyre eller sveip ned. For å fullstendig skjule den kompakte avspilleren, trykk og sveip ned én gang til.

Den kompakte avspilleren forblir synlig mens du blar gjennom biblioteket, filbehandleren eller innstillingene, slik at du aldri mister videoen mens du leter etter den neste.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Fullskjerms Medieavspiller" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Støttede video- og lydformater

Evervideo spiller av praktisk talt alle moderne beholdere og kodeker via den innbygde FFmpeg-motoren, med maskinvareakselerert H.264- og HEVC-dekoding på støttede enheter.

- **Videobeholdere:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — og mange flere.
- **Videokodeker:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — pluss praktisk talt alle andre kodeker som FFmpeg støtter.
- **Lydkodeker:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — og mange flere.
- **Undertekstformater:** SRT, VTT (WebVTT), ASS / SSA, og innebygde tekst- eller bildeundertekstspor.
- **Streamingprotokoller:** HTTP / HTTPS, HLS (m3u8), RTSP (IP-kameraer og IPTV), og direkte filstreaming over SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Dette dekker praktisk talt alle videofiler du sannsynligvis vil støte på — inkludert MKV-rips, RTSP-strømmer fra overvåkningskameraer og AV1 webm-nettlastinger.

## Avspillingskontroller

Nederst på avspillerskjermen ser du knapper for Spill av, Pause, Neste og Forrige. Det finnes også valgfrie knapper som Hopp fremover og Hopp bakover (standard 10 sekunder) som du kan aktivere i appinnstillingene. Hold inne Neste / Forrige-knappene for å spole raskt frem eller tilbake. Dra avspillingsglideren for å hoppe til en hvilken som helst posisjon.

## Gjenta og bland

Trykk på gjentaknappen for å veksle mellom gjentaksmodi:

- **Gjenta alle** — gjentar alle videoer i køen.
- **Gjenta én** — gjentar bare den gjeldende videoen.
- **Gjenta stop** — pauser når den gjeldende videoen avsluttes.
- **Ingen gjentakelse** — spiller av køen én gang uten å gjenta.

Bruk **Bland**-knappen for å randomisere rekkefølgen på videoer i køen.

## Picture-in-Picture (PiP)

På iPhone og iPad støtter Evervideo fullt ut Picture-in-Picture (PiP). Trykk på PiP-ikonet på avspillerskjermen eller sveip Evervideo til bakgrunnen — videoen fortsetter å spille av i et flytende vindu over alle andre apper. Dra det flytende vinduet til et hjørne; klip for å endre størrelse; trykk én gang for å vise grunnleggende avspilling / pause / hopp-kontroller; trykk på den lille utvid-knappen for å gå tilbake til fullstendig Evervideo.

PiP fungerer med alle videoformater Evervideo spiller av, inkludert skystreamede filer og RTSP-strømmer. PiP fortsetter også å kjøre mens telefonen er låst (avhengig av Auto-lås-innstillingen din).

## Kompakt avspiller

Den kompakte avspilleren er en vedvarende mini-avspiller som forblir synlig øverst på alle skjermer i appen mens du blar gjennom biblioteket, filbehandleren eller innstillingene. Trykk på den for å utvide til fullskjermsavspilleren; sveip ned for å kollapse den igjen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Videoinnstillinger fra Kompakt Avspiller på Hovedskjermen" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

For AirPlay, trykk på AirPlay-knappen på avspilleren. Evervideo støtter AirPlay 2, slik at du kan streame video til Apple TV, HomePod eller en AirPlay 2-kompatibel høyttaler eller smart-TV. Ved et oppsett med flere AirPlay-enheter kan du rute lyd til flere mottakere samtidig.

## Google Chromecast

For Google Cast-brukere vises Cast-ikonet på avspilleren. Trykk på det for å velge en enhet og starte casting. Sørg for at telefonen og Cast-mottakeren er på det samme Wi-Fi-nettverket. Ikke alle kodeker støttes av Chromecast-maskinvare — noen filer kan trenge transkoding.

## RTSP Direktestrømmer

Evervideo kan spille av RTSP-kilder direkte — IP-kameraer, dørklokke-kameraer, IPTV-strømmer, kringkastingsfôr og alle andre `rtsp://`-URL-er. Legg til strømmen som en RTSP-tilkobling i Filer → Nettlenker → Legg til lenke, og trykk på den for å begynne å se. RTSP-strømmer fungerer i Picture-in-Picture, den kompakte avspilleren, og de castes over AirPlay 2 og Chromecast akkurat som en vanlig video.

## Valg av lydspor

For videoer med flere lydspor (kommentar, alternativ språkdubbing, regissørspor), trykk på Flere handlinger-knappen på avspilleren og velg Lydspor — velg deretter sporet du vil ha. Dette er essensielt for fremmedspråklige filmer, BDMV / MKV-filer med flere dubbinger og instruksjonsinnhold med kommentarspor.

## Valg av videospor

Noen videofiler inkluderer flere videostrømmer (Blu-rays med flere vinkler, alternative versjoner). Velg Videospor fra Flere handlinger-menyen for å bytte mellom dem under avspilling.

## Undertekster — interne og eksterne

Evervideo gir deg finkornet kontroll over undertekster:

- **Undertekstspor** — velg fra sporene som er innebygd i filen.
- **Eksterne undertekstfiler** — last inn `.srt`-, `.vtt`-, `.ass`- eller `.ssa`-filer fra enheten din, iCloud Drive eller en tilkoblet skytjeneste.
- **Libass-rendering** — avansert ASS / SSA-styling (skrifter, farger, posisjoner, karaoke-effekter) rendres korrekt takket være den inkluderte libass.
- **Skriftvalg** — velg en tilpasset skrift for primære undertekster og en separat skrift for sekundære undertekster. Inkluderte skrifter pluss alle skrifter installert på enheten din er tilgjengelige.

Du kan konfigurere alt dette i Innstillinger → Undertekster før avspilling, eller bruk Flere handlinger → Undertekster fra avspilleren for å bytte under flyvningen.

## Lyd-equalizer

Evervideo inkluderer en fullverdig lyd-equalizer for å justere videolydspor for hodetelefonene, høyttalerne eller hi-fi-oppsettet ditt. Trykk på equalizer-ikonet i volumvisningen (eller Lyd-equalizer-handlingen i avspillerens Flere handlinger-meny), slå på equalizeren med bryteren øverst til høyre, og enten velg en forhåndsinnstilling eller dra båndgliderne for å bygge din egen. Tilpassede forhåndsinnstillinger kan eksporteres og importeres slik at du kan dele dem på tvers av enheter eller ta sikkerhetskopi av dem.

## Video-equalizer

For å justere bildet tilbyr Evervideo en dedikert video-equalizer — juster lysstyrke, kontrast, metning og fargetone i sanntid under avspilling. Som lyd-equalizeren kan tilpassede videoforhåndsinnstillinger eksporteres og importeres for deling eller sikkerhetskopiering. Bruk den til å lyse opp en mørk scene på en solrik dag, øke metningen på falmet innhold eller varme opp en kald fargekast.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Video-equalizer" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Videoskateringsmodus

Velg hvordan videoen fyller skjermen:

- **Tilpass** — bevar det originale sideforholdet; svarte striper der det trengs.
- **Fyll** — fyll hele skjermen, og beskjær videoen om nødvendig.
- **Strekk** — strekk videoen for å fylle skjermen, forvrengning om nødvendig.
- **Originalt** — behold den native oppløsningen på 1:1.

## Videorotasjon

For videoer som er tatt opp med feil orientering, velg **Flere handlinger → Rotasjon** og velg **0°**, **90°**, **180°** eller **270°** for å rotere bildet uten å forlate avspilleren.

## Maskinvaredekoding (H.264 og HEVC)

I Innstillinger → Avspiller → Video kan du aktivere / deaktivere Maskinvaredekoding H.264 og Maskinvaredekoding H.265 (HEVC) uavhengig. Maskinvaredekoding er raskere, bruker mindre batteri og kjører kjøligere — men i sjeldne tilfeller (korrupte filer, eksotiske profiler) kan det hende du må deaktivere maskinvaredekoding og falle tilbake til programvare-FFmpeg-dekoding. Evervideo lar deg gjøre det fil for fil fra avspillerens Flere handlinger-meny.

## VR 360° Viewport

Evervideo inkluderer en VR / 360° viewport for sfæriske videofiler. Når du spiller av en 360°-video, kan du dra for å se rundt, klipe for å zoome, og Evervideo vil forvrenge renderingen i sanntid.

## Avspillingshastighet

Trykk på Hastighet-kontrollen på avspillerverktøylinjen for å endre avspillingshastigheten — senk den for analyse (0,25× eller 0,5×) eller øk den for veiledninger og forelesninger (1,25×, 1,5×, 2× og opptil 3×). Trykk på konfigurasjonsikonet øverst til høyre på Hastighet-skjermen for å bytte til presisjonsmodusen med finere justeringer. Per-spor tonehøydekorreksjon er også tilgjengelig.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Avspillingshastighet på Hovedverktøylinjen" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Avspillingskø

For å se avspillingskøen, trykk på kø-knappen på avspilleren. Hver video i køen har flere handlinger — trykk på de tre prikkene for å se dem. For å omorganisere en video i køen, bruk omordningsindikatoren nær tittelen og dra den til en ny posisjon.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Avspillingskø" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Sove-timer

Åpne Innstillinger → Avspiller → Sove-timer, slå den på, og velg hvor lenge du vil at avspillingen skal fortsette før den automatisk stopper. Du kan også legge til Sove-timer-knappen direkte til avspillerens hovedskjerm via Innstillinger → Avspiller → Personalisering → Handlinger på hovedskjermen.

## Avspillerbokmerkene

Lagre plassen din i lange videoer — forelesninger, lydbøker-på-video, veiledninger, timeslange YouTube-nedlastinger — ved å trykke Legg til bokmerke fra Flere handlinger-menyen. Bokmerker vises i videoens Flere handlinger → Bokmerker-liste og bevares mellom sesjoner.

## Menyen Flere handlinger

Trykk på knappen **Flere handlinger "..."** på avspilleren for å få tilgang til tilleggsfunksjoner.

- **Fortsett avspilling** — gjenoppta køen fra siste posisjon.
- **Søk** — finn en bestemt video i køen.
- **Bokmerker** — vis og hopp til bokmerker.
- **Hastighet** — juster avspillingshastigheten.
- **Nylige** — nylig avspilte videoer.
- **Favoritter** — favorittmarkerte videoer.
- **Lyd-equalizer** — aktiver lyd-equalizeren.
- **Video-equalizer** — aktiver video-equalizeren.
- **Lydspor** — velg lydstrømmen.
- **Videospor** — velg videostrømmen.
- **Undertekster** — primært / sekundært spor, ekstern fil, skrift.
- **Rotasjon** — roter bildet 0° / 90° / 180° / 270°.
- **Skateringsmodus** — Tilpass / Fyll / Strekk / Originalt.
- **Picture-in-Picture** — gå inn i PiP-modus.
- **AirPlay** / **Chromecast** — send til en enhet.
- **Sove-timer** — sett en timer for å stoppe avspilling.
- **Lagre kø som spilleliste** — lagre gjeldende kø som ny spilleliste.
- **Slett kø** — tøm køen og stopp avspilling.
- **Innstillinger** — gå direkte til avspillerinnstillinger.
- **Hjelp** — åpne veiledning.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Avspiller Flere handlinger Skjerm" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Avspillerinnstillinger

Det fullstendige innstillingstre for Avspilleren er dokumentert i [Innstillingsguiden](/docs/guide/evervideo/evervideo-guide-settings/). De mest brukte seksjonene:

- **Generelt** — Gjentaksmodus, Blandemodus, Lagre avspillerstatus, Lagre avspillingsposisjon, Hopp-tidsintervaller.
- **Video** — Maskinvaredekoding H.264 / HEVC, video-equalizer, skateringsmodus, rotasjon, visningsmodus, foretrukket FPS, foretrukket pikselformat, VR-viewport.
- **Lyd** — Lyd-equalizer, samplingsfrekvens, kanaler, IO-buffervarighet, blandet modus.
- **Undertekster** — Primært / sekundært spor, valg av ekstern fil, skrift, sekundær skrift.
- **Enheter** (iOS) — AirPlay / Chromecast.
- **Personalisering** — Avspilleroppsettsstil (Minimal / Bunn / Antikk / Klassisk), handlinger på hovedskjermen, låsskjermkontroller.
- **Avspillingsbuffer** — diskbuffer for jevnere strømming.
- **Sove-timer** — automatisk stopp.

## Tilgjengelighet

Evervideo er fullt tilgjengelig med VoiceOver. Hvert komponent har et godt designet etikett og beskrivelse. Når VoiceOver er aktiv, bytter appen til Tekstmodus slik at bare meningsfulle elementer vises — noe som forbedrer navigasjonshastighet og klarhet. Du kan også aktivere Tekstmodus i Innstillinger → Tilgjengelighet → Tekstmodus.

### Justere glidere med VoiceOver

1. **Velg glideren** — sveip venstre eller høyre til VoiceOver kunngjør den.
2. **Juster verdien** — dobbelttrykk og hold glideren, dra deretter opp eller ned for å endre verdien raskt. VoiceOver kunngjør den nye verdien mens du går.

Andre komponenter fungerer som forventet, med systemleverte VoiceOver-mønstre.
