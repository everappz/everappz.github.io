---
title: "Medieafspiller"
date: 2020-02-01
lastmod: 2026-06-01
description: "Lær at bruge Evervideo medieafspilleren på iPhone, iPad og Mac. Picture-in-Picture, hardware-accelereret H.264 / HEVC-dekodning, lyd- og videoequalizers, primære og sekundære undertekster, lyd- og videosporvalg, videoskalering og rotation, afspilningshastighed, sovende timer, AirPlay 2, Google Chromecast, RTSP-streams og den kompakte altid-synlige afspiller."
keywords: [
  "Evervideo afspiller guide", "videoafspiller indstillinger", "Evervideo equalizer",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "video undertekst iPhone", "eksterne SRT undertekster",
  "ASS SSA undertekstafspiller", "libass iOS",
  "dobbelte undertekster sprogindlæring",
  "videoequalizer lysstyrke kontrast", "lydequalizer videoafspiller",
  "videoafspiller rotationslås", "videoskaleringstilstand iOS",
  "hardware H.264 dekoder iPhone", "hardware HEVC dekoder iPad",
  "afspilningshastighed video", "FFmpeg videoafspiller iOS",
  "RTSP iPhone afspiller", "kompakt videoafspiller",
  "VR 360 videoafspiller iPhone"
]
tags: ["guide", "evervideo", "afspiller", "PiP", "undertekster", "videoequalizer"]
readingTime: 14
---


Medieafspilleren er appens hovedskærm, hvor du styrer afspilning og de fleste af Evervideos funktioner. Den afspiller både video- og lydfiler og er bygget på en brugerdefineret FFmpeg-baseret afspiller med hardware-accelereret H.264 og HEVC-dekodning, der gør det tunge arbejde. Lad os udforske, hvordan man bruger den.

## Adgang til medieafspilleren

Du kan komme til fuldskærmsafspilleren fra den kompakte afspillerbar. På iPhone sidder den kompakte afspiller øverst på hovedskærmen. På iPad og Mac er den på venstre side (eller toppen af ​​hovedpanelet). For at sammenfoldse fuldskærmsafspilleren tilbage til kompakt visning skal du trykke på lukkeknappen i nederste højre hjørne eller swipe ned. For at skjule den kompakte afspiller fuldstændigt skal du trykke og swipe ned endnu en gang.

Den kompakte afspiller forbliver synlig, mens du gennemser dit bibliotek, din filhåndtering eller dine indstillinger, så du aldrig mister din video, mens du leder efter den næste.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo fuldskærms medieafspiller" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Understøttede video- og lydformater

Evervideo afspiller næsten alle moderne containere og codecs via den medfølgende FFmpeg-motor med hardware-accelereret H.264 og HEVC-dekodning på understøttede enheder.

- **Videocontainere:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — og mange flere.
- **Videocodecs:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus næsten alle andre codecs, som FFmpeg understøtter.
- **Lydcodecs:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — og mange flere.
- **Undertekstformater:** SRT, VTT (WebVTT), ASS / SSA og indlejrede tekst- eller billedundertekstspor.
- **Streamingprotokoller:** HTTP / HTTPS, HLS (m3u8), RTSP (IP-kameraer og IPTV) og direkte filstreaming over SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Det dækker næsten alle videofiler, du sandsynligvis vil støde på — herunder MKV-rips, sikkerhedskamera RTSP-streams og AV1 webm-webdownloads.

## Afspilningskontroller

Nederst på afspillerskærmen ser du knapper til Afspil, Pause, Næste og Forrige. Der er også valgfrie knapper som Spring frem og Spring tilbage (standard 10 sekunder), som du kan aktivere i appindstillingerne. Hold Næste / Forrige-knapperne nede for at spole hurtigt frem eller tilbage. Træk afspilningsskyderen for at hoppe til en vilkårlig position.

## Gentagelse og bland

Tryk på gentagelsesknappen for at skifte mellem gentagelsestilstande:

- **Gentag alle** — looper alle videoer i din kø.
- **Gentag én** — gentager kun den aktuelle video.
- **Stop gentagelse** — sætter på pause, når den aktuelle video slutter.
- **Ingen gentagelse** — afspiller køen én gang igennem uden at gentage.

Brug knappen **Bland** til at randomisere rækkefølgen af ​​videoer i køen.

## Picture-in-Picture (PiP)

På iPhone og iPad understøtter Evervideo fuldt ud Picture-in-Picture (PiP). Tryk på PiP-ikonet på afspillerskærmen, eller swipe blot Evervideo i baggrunden — videoen fortsætter med at spille i et flydende vindue over alle andre apps. Træk det flydende vindue til et vilkårligt hjørne; knib for at ændre størrelse; tryk én gang for at få grundlæggende afspil / pause / spring-kontroller frem; tryk på den lille udvid-knap for at vende tilbage til fuld Evervideo.

PiP fungerer med alle videoformater, Evervideo afspiller, herunder cloud-streamede filer og RTSP-streams. PiP fortsætter også med at køre, mens din telefon er låst (afhænger af din Auto-lås-indstilling).

## Kompakt afspiller

Den kompakte afspiller er en vedvarende mini-afspiller, der forbliver synlig øverst på alle skærme i appen, mens du gennemser biblioteket, filhåndteringen eller indstillingerne. Tryk på den for at udvide til fuldskærmsafspilleren; swipe ned for at sammenfoldse den igen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo videoindstillinger fra den kompakte afspiller på startskærmen" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

For AirPlay skal du trykke på AirPlay-knappen på afspilleren. Evervideo understøtter AirPlay 2, så du kan streame video til Apple TV, HomePod eller enhver AirPlay 2-kompatibel højttaler eller smart-TV. På en opsætning med flere AirPlay-enheder kan du route lyd til flere modtagere samtidigt.

## Google Chromecast

For Google Cast-brugere vises Cast-ikonet på afspilleren. Tryk på det for at vælge en enhed og starte casting. Sørg for, at din telefon og Cast-modtageren er på det samme Wi-Fi-netværk. Ikke alle codecs understøttes af Chromecast-hardware — nogle filer skal muligvis omkodes.

## RTSP live-streams

Evervideo kan afspille RTSP-kilder direkte — IP-kameraer, dørklokke-kameraer, IPTV-streams, udsendelsesfeeds og enhver anden `rtsp://` URL. Tilføj streamen som en RTSP-forbindelse i Filer → Online links → Tilføj link, og tryk derefter på den for at begynde at se. RTSP-streams fungerer i Picture-in-Picture, den kompakte afspiller, og de castes over AirPlay 2 og Chromecast ligesom en almindelig video.

## Valg af lydspor

For videoer med flere lydspor (kommentar, alternative sprogsynkroniseringer, instruktørspor) skal du trykke på knappen Flere handlinger på afspilleren og vælge Lydspor — og derefter vælge det spor, du ønsker. Dette er afgørende for fremmedsprogfilm, BDMV / MKV-filer med flere synkroniseringer og instruktionsmateriale med kommentarspor.

## Valg af videospor

Nogle videofiler inkluderer flere videostreams (multi-vinkel Blu-rays, alternative klip). Vælg Videospor fra menuen Flere handlinger for at skifte mellem dem midt i afspilningen.

## Undertekster — interne og eksterne

Evervideo giver dig finkornet kontrol over undertekster:

- **Undertekstspor** — vælg fra sporene indlejret i filen.
- **Eksterne undertekstfiler** — indlæs `.srt`-, `.vtt`-, `.ass`- eller `.ssa`-filer fra din enhed, iCloud Drive eller enhver tilsluttet cloudtjeneste.
- **Libass-gengivelse** — avanceret ASS / SSA-styling (skrifttyper, farver, positioner, karaoke-effekter) gengives korrekt takket være den medfølgende libass.
- **Skrifttypevalg** — vælg en brugerdefineret skrifttype til primære undertekster og en separat skrifttype til sekundære undertekster. Medfølgende skrifttyper plus alle skrifttyper installeret på din enhed er tilgængelige.

Du kan konfigurere alt dette i Indstillinger → Undertekster før afspilning, eller bruge Flere handlinger → Undertekster fra afspilleren for at skifte undervejs.

## Lydequalizer

Evervideo inkluderer en fuld lydequalizer til at tune videolydsporet til dine høretelefoner, højttalere eller hi-fi-opsætning. Tryk på equalizer-ikonet på lydstyrkevisningen (eller handlingen Lydequalizer i afspillerens menu Flere handlinger), slå equalizeren til med kontakten i øverste højre hjørne, og vælg enten en forudindstilling eller træk båndskyderene for at bygge din egen forudindstilling. Brugerdefinerede forudindstillinger kan eksporteres og importeres, så du kan dele dem på tværs af enheder eller sikkerhedskopiere dem.

## Videoequalizer

Til justering af billedet leverer Evervideo en dedikeret videoequalizer — juster lysstyrke, kontrast, mætning og farvetone i realtid under afspilning. Ligesom lydequalizer kan brugerdefinerede videoforudindstillinger eksporteres og importeres til deling eller sikkerhedskopi. Brug den til at lyse en mørk scene op på en solrig dag, booste mætning på udvasket indhold eller varme en kold farvecast op.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo videoequalizer" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Videoskaleringstilstand

Vælg, hvordan videoen fylder skærmen:

- **Tilpas** — bevar det originale billedformat; sorte bjælker hvor nødvendigt.
- **Udfyld** — udfyld hele skærmen, beskær videoen om nødvendigt.
- **Stræk** — stræk videoen til at udfylde skærmen, forvreng om nødvendigt.
- **Original** — behold den native opløsning ved 1:1.

## Videorotation

For videoer optaget med forkert orientering skal du vælge **Flere handlinger → Rotation** og vælge **0°**, **90°**, **180°** eller **270°** for at rotere billedet uden at forlade afspilleren.

## Hardwaredekodning (H.264 og HEVC)

I Indstillinger → Afspiller → Video kan du aktivere / deaktivere Hardware-dekod H.264 og Hardware-dekod H.265 (HEVC) uafhængigt. Hardwaredekodning er hurtigere, bruger mindre batteri og kører køligere — men i sjældne tilfælde (korrupte filer, eksotiske profiler) kan det være nødvendigt at deaktivere hardwaredekodning og falde tilbage til software FFmpeg-dekodning. Evervideo lader dig gøre det fil-for-fil fra afspillerens menu Flere handlinger.

## VR 360°-visning

Evervideo inkluderer en VR / 360°-visning til sfæriske videofiler. Når du afspiller en 360°-video, kan du trække for at se dig omkring, knibe for at zoome, og Evervideo vil forvrænge gengivelsen i realtid.

## Afspilningshastighed

Tryk på Hastighedsstyringen på afspilleren for at ændre afspilningshastighed — sænk den til analyse (0,25× eller 0,5×) eller øg den til tutorials og forelæsninger (1,25×, 1,5×, 2× og op til 3×). Tryk på konfigurationsikonet i øverste højre hjørne af Hastighedsskærmen for at skifte til præcisionstilstand med finere justeringer. Tonehøjdekorrektion per spor er også tilgængelig.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo afspilningshastighed på den primære værktøjslinje" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Afspillerkø

For at se din afspillerkø skal du trykke på køknappen på afspilleren. Hver video i køen har flere handlinger — tryk på de tre prikker for at se dem. For at omarrangere en video i køen skal du bruge omorganiserings-indikatoren nær titlen og trække den til en ny position.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo afspilningskø" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Sovende timer

Åbn Indstillinger → Afspiller → Sovende timer, slå den til, og vælg, hvor lang tid du vil have afspilning til at fortsætte, før den stopper automatisk. Du kan også tilføje knappen Sovende timer direkte til afspillerens hovedskærm via Indstillinger → Afspiller → Personalisering → Handlinger på hovedskærmen.

## Afspillerbogmærker

Gem din plads i lange videoer — forelæsninger, lydbøger-på-video, tutorials, timeslange YouTube-downloads — ved at trykke på Tilføj bogmærke fra menuen Flere handlinger. Bogmærker vises i videoens Flere handlinger → Bogmærker-liste og bevares mellem sessioner.

## Menuen Flere handlinger

Tryk på knappen **Flere handlinger "..."** på afspilleren for at få adgang til yderligere funktioner.

- **Fortsæt afspilning** — genoptag køen fra den sidste position.
- **Søg** — find en specifik video i din kø.
- **Bogmærker** — vis og hop til bogmærker.
- **Hastighed** — juster afspilningshastighed.
- **Seneste** — senest afspillede videoer.
- **Favoritter** — foretrukne videoer.
- **Lydequalizer** — aktiver lydequalizer.
- **Videoequalizer** — aktiver videoequalizer.
- **Lydspor** — vælg lydstreamen.
- **Videospor** — vælg videostreamen.
- **Undertekster** — primært / sekundært spor, ekstern fil, skrifttype.
- **Rotation** — roter billedet 0° / 90° / 180° / 270°.
- **Skaleringstilstand** — Tilpas / Udfyld / Stræk / Original.
- **Picture-in-Picture** — gå ind i PiP-tilstand.
- **AirPlay** / **Chromecast** — send til en enhed.
- **Sovende timer** — indstil en timer til at stoppe afspilning.
- **Gem kø som afspilningsliste** — gem den aktuelle kø som en ny afspilningsliste.
- **Slet kø** — ryd køen og stop afspilning.
- **Indstillinger** — hop direkte til afspillerindstillinger.
- **Hjælp** — åbn vejledning.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo afspiller Flere handlinger-skærm" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Afspillerindstillinger

Det fulde afspillerindstillingstræ er dokumenteret i [Indstillingsguiden](/docs/guide/evervideo/evervideo-guide-settings/). De mest brugte sektioner:

- **Generelt** — Gentagelsestilstand, Bland-tilstand, Gem afspillertilstand, Gem afspilningsposition, Spring-tidsintervaller.
- **Video** — Hardware-dekod H.264 / HEVC, videoequalizer, skaleringstilstand, rotation, visningstilstand, foretrukne FPS, foretrukket pixelformat, VR-visning.
- **Lyd** — Lydequalizer, samplingsfrekvens, kanaler, IO-buffertid, blandet tilstand.
- **Undertekster** — Primært / sekundært spor, valg af ekstern fil, skrifttype, sekundær skrifttype.
- **Enheder** (iOS) — AirPlay / Chromecast.
- **Personalisering** — Afspillerlayout-stil (Minimal / Bund / Antik / Klassisk), handlinger på hovedskærmen, låseskærmkontroller.
- **Afspilnings-cache** — diskcache til jævnere streaming.
- **Sovende timer** — automatisk stop.

## Tilgængelighed

Evervideo er fuldt tilgængeligt med VoiceOver. Hver komponent har et veldesignet mærkat og beskrivelse. Når VoiceOver er aktivt, skifter appen til Teksttilstand, så kun meningsfulde elementer vises — forbedrer navigationshastighed og klarhed. Du kan også aktivere Teksttilstand i Indstillinger → Tilgængelighed → Teksttilstand.

### Justering af skydere med VoiceOver

1. **Vælg skyderen** — swipe venstre eller højre, indtil VoiceOver annoncerer den.
2. **Juster værdien** — dobbelttryk og hold skyderen, og træk derefter op eller ned for at ændre værdien hurtigt. VoiceOver annoncerer den nye værdi, mens du går.

Andre komponenter fungerer som forventet med systemleverede VoiceOver-mønstre.
