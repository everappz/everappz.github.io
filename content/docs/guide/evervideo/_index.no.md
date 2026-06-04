---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Lær hvordan du bruker Evervideo — alt-i-ett skyvideoavspilleren for iPhone, iPad og Mac. Stream og last ned videoer fra iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA og S3 — pluss Plex, Jellyfin, Emby, Subsonic og Navidrome. Picture-in-Picture, primære og sekundære undertekster, lyd- og videoequalizer, RTSP IP-kamerastrømmer, Chromecast, AirPlay 2, maskinvareakselerert H.264 / HEVC-dekoding, integrering med Bilder og Apple Music, og en kompakt alltid-synlig avspiller.'
keywords: [
  "Evervideo guide", "Evervideo hvordan", "sky-videospiller iPhone", "videospiller Mac",
  "MKV-spiller iOS", "FFmpeg videospiller", "HEVC videospiller iPhone",
  "Picture-in-Picture video iPhone", "PiP videospiller iPad",
  "RTSP-spiller iPhone", "IP-kameravisning", "DLNA videospiller",
  "Plex-klient iPhone", "Jellyfin-klient iOS", "Emby-klient iPad",
  "undertekstspiller iOS", "SRT VTT ASS undertekster", "sekundære undertekster iPhone",
  "video-equalizer iOS", "lyd-equalizer videospiller", "ekstern DAC video",
  "stream video fra Google Drive", "stream video fra Dropbox",
  "stream video fra OneDrive", "stream video fra iCloud Drive",
  "stream video fra MEGA", "stream video fra NAS",
  "Chromecast video iPhone", "AirPlay 2 video", "iCloud videospiller",
  "Bilder-bibliotek videospiller", "Apple Music videospiller",
  "Wi-Fi Drive videooverføring", "M3U videospilleliste",
  "Evervideo Premium", "Family Sharing video-app"
]
tags: ["evervideo", "guide", "videospiller", "PiP", "undertekster", "RTSP", "sky", "FFmpeg"]
---


### Velkommen til Evervideo-guiden

Evervideo er en fullverdig skymediaspiller for iPhone, iPad og Mac som gjør enhver skylagringskonto, NAS eller medieserver om til ditt personlige mediebibliotek, uten behov for å laste opp noe på nytt og mens du beholder full kontroll over filene dine.

Bygget på en tilpasset FFmpeg-basert spillermotor med maskinvareakselerert H.264- og HEVC-dekoding, spiller Evervideo praktisk talt alle moderne beholdere og kodeker — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS og den lange halen av FFmpeg-formater — i full kvalitet, med smart bufring for jevn strømming over Wi-Fi eller mobilnett. Picture-in-Picture holder videoen din på toppen av alle andre apper, den kompakte alltid-synlige avspilleren lar deg fortsette å se mens du blar gjennom biblioteket, og Chromecast og AirPlay 2 sender avspillingen til TV-en, HomePod eller høyttaleroppsettet ditt med ett trykk.

Evervideo kobler til en bemerkelsesverdig bred liste over kilder, alle fra én app:

- **Personlig skylagring:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Selvhostede medieservere:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (og ownCloud via den delte API-en) · Synology Drive · QNAP.
- **NAS- og fildeleprotokoller:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (passord eller offentlig nøkkel-godkjenning) · NFS · DLNA · UPnP.
- **Direktestrøm og IP-kamerastrømmer:** RTSP — pek Evervideo mot en hvilken som helst RTSP-URL (`rtsp://camera-ip/stream`) og den spilles av umiddelbart.
- **S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og alle andre S3-API-endepunkter.
- **Enhetskilder:** Bilder-biblioteket (Alle videoer, Kort / Middels / Lang, Skjermopptak, pluss Fotoalbumene dine), Musikk-appbiblioteket (Album, Sjangre, Spillelister), USB- / SD-kortstasjoner og Lokale filer.

### Én avspiller for alle formater og kodeker

Der de fleste iOS-apper stopper ved H.264 / H.265 i MP4 / MOV, inkluderer Evervideo FFmpeg ved siden av Apples systemkodeker slik at du kan spille av formater systemet ikke gjenkjenner — MKV-beholdere, VP9, AV1, MPEG-2, OGG, Vorbis og mange flere — og bytter automatisk mellom maskinvare H.264 / HEVC-dekoding og programvaredekoding basert på filen og enheten.

Du kan velge videospor (multi-stream Blu-ray-rip), lydspor (kommentarspor, alternative dubbinger) og undertekstspor. Eksterne SRT-, VTT- og ASS / SSA-undertekstfiler lastes med ett trykk; avansert ASS / SSA-styling rendres korrekt takket være den inkluderte libass.

### Smarte undertekster

- **Valg av undertekstspor** perfekt for språklæring.
- **Eksterne undertekstfiler** (`.srt`, `.vtt`, `.ass`, `.ssa`) lastet fra hvor som helst på enheten eller fra skyen.
- **libass** for fullt stilt ASS / SSA-rendering.
- **Per-spor og global skriftvalg** for undertekster.
- **Valg av lydspor** velg dubbing, kommentar eller regissørspor.
- **Valg av videospor** for filer med flere vinkler eller versjoner.

### Finjuster bildet og lyden

To equalizer-er, side om side: en lyd-equalizer for å justere bass og diskant (med import / eksport av egne forhåndsinnstillinger), og en video-equalizer for å justere lysstyrke, kontrast, metning og fargetone (igjen med import / eksport). Begge motorene eksponerer også audiofil-kontroller: lydutgangssamplingsfrekvens, kanalantall, IO-buffervarighet og blandet modus — for brukere med eksterne DAC-er og hjemmekino-mottakere.

### Kast, AirPlay og Picture-in-Picture

- **Picture-in-Picture (PiP):** fortsett å se mens du bruker andre apper.
- **AirPlay 2:** send video til Apple TV, HomePod eller en AirPlay 2-kompatibel høyttaler / TV.
- **Google Chromecast:** kast direkte til en Chromecast eller Cast-kompatibel TV.
- **Kompakt avspiller:** en vedvarende mini-avspiller på toppen av alle skjermer slik at du kan bla gjennom biblioteket uten å miste videoen.

### Personvern og sikkerhet

Evervideo bruker offisielle SDK-er og OAuth-baserte pålogginger fra alle skyleverandører slik at passordet ditt aldri når appen. Tilgangstokener lagres kryptert i iOS/MacOS Keychain, alle overføringer er TLS-beskyttet, og tilbakekalling av tilgang fra skykontoen din (eller fjerning av Evervideo fra enheten) sletter alt umiddelbart. Beskytt biblioteket ditt med en valgfri 4-sifret kode for et ekstra lag med personvern.

### Kom i gang med Evervideo

Denne guiden tar deg gjennom alle deler av Evervideo på iPhone, iPad og Mac — fra tilkobling av skytjenester, browsing av biblioteket, nedlasting og overføring av filer, administrering av spillelister, til finjustering av mediespilleren, equalizer-er, undertekster og Picture-in-Picture. Bruk kortene nedenfor for å hoppe direkte til seksjonen du trenger.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navigasjon" subtitle="Fanestripe på iPhone, Venstremeny på iPad og Mac, kompakt alltid-synlig medieavspiller." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Filer" subtitle="Én samlet fane for sky, NAS, RTSP-strømmer, lokale filer, USB-stasjoner og overføringskøen." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Mediebibliotek" subtitle="Bla gjennom etter Album, Sjangre, Nylige, Favoritter — pluss iOS Bilder-biblioteket og Apple Music-biblioteket." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Spillelister" subtitle="Bygg spillelister fra sky, lokalt, Bilder eller Musikk-biblioteket, importer M3U / M3U8 / CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Medieavspiller" subtitle="Picture-in-Picture, lyd- og videospor, undertekster, lyd + video-equalizer, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Innstillinger" subtitle="Lydmotor, videodekoder, undertekster, bibliotek, filbehandling, widgets, tilpasning, språk, sikkerhetskopi." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="Vanlige spørsmål" subtitle="Finn svar på de vanligste spørsmålene om Evervideo." >}}

{{< /cards >}}
