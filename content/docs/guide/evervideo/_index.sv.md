---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Lär dig använda Evervideo — den kompletta molnvideospelaren för iPhone, iPad och Mac. Strömma och ladda ner videor från iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA och S3 — plus Plex, Jellyfin, Emby, Subsonic och Navidrome. Picture-in-Picture, primära och sekundära undertexter, ljud- och videoekvalisatorer, RTSP IP-kameraströmmar, Chromecast, AirPlay 2, hårdvaruavkodning av H.264 / HEVC, integrering med Photos och Apple Music, och en kompakt alltid-synlig spelare.'
keywords: [
  "Evervideo guide", "Evervideo instruktioner", "molnvideospelare iPhone", "videospelare Mac",
  "MKV-spelare iOS", "FFmpeg videospelare", "HEVC videospelare iPhone",
  "Picture-in-Picture video iPhone", "PiP videospelare iPad",
  "RTSP-spelare iPhone", "IP-kameravisare", "DLNA videospelare",
  "Plex-klient iPhone", "Jellyfin-klient iOS", "Emby-klient iPad",
  "undertextspelare iOS", "SRT VTT ASS undertexter", "sekundära undertexter iPhone",
  "videoekvalisator iOS", "ljudekvalisator videospelare", "extern DAC video",
  "strömma video från Google Drive", "strömma video från Dropbox",
  "strömma video från OneDrive", "strömma video från iCloud Drive",
  "strömma video från MEGA", "strömma video från NAS",
  "Chromecast video iPhone", "AirPlay 2 video", "iCloud videospelare",
  "Photos-bibliotek videospelare", "Apple Music videospelare",
  "Wi-Fi Drive videoöverföring", "M3U videospellista",
  "Evervideo Premium", "Family Sharing videoapp"
]
tags: ["evervideo", "guide", "videospelare", "PiP", "undertexter", "RTSP", "moln", "FFmpeg"]
---


### Välkommen till Evervideo-guiden

Evervideo är en fullständig molnmediespelare för iPhone, iPad och Mac som förvandlar vilket molnlagringskonto, NAS eller mediaserver som helst till ditt personliga mediebibliotek — utan behov av att ladda upp på nytt och med full kontroll över dina filer.

Byggd på en anpassad FFmpeg-baserad spelmototur med hårdvaruaccelererad H.264- och HEVC-avkodning, spelar Evervideo praktiskt taget alla moderna behållare och kodekar — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS och den långa raden av FFmpeg-format — i full kvalitet, med smart buffring för smidig strömning via Wi-Fi eller mobilt nätverk. Picture-in-Picture håller din video ovanför alla andra appar, den kompakta alltid-synliga spelaren låter dig fortsätta titta medan du bläddrar i ditt bibliotek, och Chromecast och AirPlay 2 skickar uppspelning till din TV, HomePod eller högtalarkonfiguration med ett tryck.

Evervideo ansluter till en anmärkningsvärt bred lista med källor, allt från en app:

- **Personlig molnlagring:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Självhostade mediaservrar:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (och ownCloud via det delade API:et) · Synology Drive · QNAP.
- **NAS och fildelningsprotokoll:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (lösenord eller autentisering med offentlig nyckel) · NFS · DLNA · UPnP.
- **Live och IP-kameraströmmar:** RTSP — peka Evervideo på valfri RTSP-URL (`rtsp://camera-ip/stream`) och den spelar bara.
- **S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces och valfri annan S3-API-slutpunkt.
- **Källor på enheten:** Photos-biblioteket (Alla videor, Korta / Medellånga / Långa, Skärminspelningar, plus dina Fotoalbum), Music-appens bibliotek (Album, Genrer, Spellistor), USB / SD-kortdrivrutiner och Lokala filer.

### En spelare för alla format och kodekar

Där de flesta iOS-appar stannar vid H.264 / H.265 inuti MP4 / MOV, paketerar Evervideo FFmpeg tillsammans med Apples systemkodekar så att du kan spela format som systemet inte känner igen — MKV-behållare, VP9, AV1, MPEG-2, OGG, Vorbis och många fler — och växlar automatiskt mellan hårdvaru H.264 / HEVC-avkodning och mjukvaruavkodning baserat på filen och enheten.

Du kan välja videospår (flerchannel Blu-ray-rips), ljudspår (kommentarspår, alternativa dubbningar) och undertextspår. Externa SRT-, VTT- och ASS / SSA-undertextfiler laddas med ett tryck; avancerad ASS / SSA-styling renderas korrekt tack vare den medföljande libass.

### Smarta undertexter

- **Val av undertextspår** — perfekt för språkinlärning.
- **Externa undertextfiler** (`.srt`, `.vtt`, `.ass`, `.ssa`) laddade var som helst på din enhet eller från molnet.
- **libass** för fullt stilad ASS / SSA-rendering.
- **Teckensnittsval per spår och globalt** för undertexter.
- **Val av ljudspår** — välj dubbning, kommentar eller regissörens spår.
- **Val av videospår** för filer med flera vinklar eller versioner.

### Finjustera bilden och ljudet

Två ekvalisatorer sida vid sida: en ljudekvalisator för att justera bas och diskant (med import / export av anpassade förinställningar) och en videoekvalisator för att justera ljusstyrka, kontrast, mättnad och nyans (igen med import / export). Båda motorerna exponerar även audiofilvänliga kontroller: samplingsfrekvens för ljudutgång, kanalantal, IO-buffertvaraktighet och blandat läge — för användare med externa DAC:ar och hemmabio-receivers.

### Cast, AirPlay och Picture-in-Picture

- **Picture-in-Picture (PiP):** fortsätt titta medan du använder andra appar.
- **AirPlay 2:** skicka video till Apple TV, HomePod eller valfri AirPlay 2-högtalare / TV.
- **Google Chromecast:** casta direkt till en Chromecast eller Cast-aktiverad TV.
- **Kompakt spelare:** en beständig minispelare ovanpå varje skärm så att du kan bläddra i ditt bibliotek utan att förlora videon.

### Integritet och säkerhet

Evervideo använder officiella SDK:er och OAuth-baserade inloggningar från varje molnleverantör så att ditt lösenord aldrig når appen. Åtkomsttokens lagras krypterade i iOS/MacOS Keychain, varje överföring är TLS-skyddad och att återkalla åtkomst från ditt molnkonto (eller ta bort Evervideo från enheten) raderar allt omedelbart. Skydda ditt bibliotek med en valfri 4-siffrig lösenkod för ett extra lager av integritet.

### Komma igång med Evervideo

Den här guiden leder dig genom varje del av Evervideo på iPhone, iPad och Mac — från att ansluta molntjänster, bläddra i ditt bibliotek, ladda ner och överföra filer, hantera spellistor, till att finjustera mediespelaren, ekvalisatorer, undertexter och Picture-in-Picture. Använd korten nedan för att hoppa direkt till det avsnitt du behöver.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navigering" subtitle="Flikfält på iPhone, vänstermeny på iPad och Mac, kompakt alltid-synlig mediaspelare." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Filer" subtitle="En enhetlig flik för moln, NAS, RTSP-strömmar, lokala filer, USB-enheter och överföringskön." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Mediebibliotek" subtitle="Bläddra efter Album, Genrer, Senaste, Favoriter — plus iOS Photos-biblioteket och Apple Music-biblioteket." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Spellistor" subtitle="Bygg spellistor från moln, lokala filer, Photos eller Music-biblioteket, importera M3U / M3U8 / CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Mediespelare" subtitle="Picture-in-Picture, ljud- och videospår, undertexter, ljud- och videoekvalisatorer, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Inställningar" subtitle="Ljudmotor, videoavkodare, undertexter, bibliotek, filhanterare, widgets, personalisering, språk, säkerhetskopiering." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="FAQ" subtitle="Hitta svar på de vanligaste frågorna om Evervideo." >}}

{{< /cards >}}
