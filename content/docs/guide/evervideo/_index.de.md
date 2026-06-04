---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Erfahren Sie, wie Sie Evervideo nutzen — den All-in-One-Cloud-Videoplayer für iPhone, iPad und Mac. Streamen und laden Sie Videos von iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA und S3 — sowie Plex, Jellyfin, Emby, Subsonic und Navidrome. Picture-in-Picture, primäre und sekundäre Untertitel, Audio- und Video-Equalizer, RTSP-IP-Kamera-Streams, Chromecast, AirPlay 2, Hardware-H.264/HEVC-Dekodierung, Integration der Fotos- und Apple Music-Mediathek und ein kompakter Always-on-top-Player.'
keywords: [
  "Evervideo Anleitung", "Evervideo Anleitung", "Cloud-Videoplayer iPhone", "Videoplayer Mac",
  "MKV-Player iOS", "FFmpeg-Videoplayer", "HEVC-Videoplayer iPhone",
  "Picture-in-Picture Video iPhone", "PiP-Videoplayer iPad",
  "RTSP-Player iPhone", "IP-Kamera-Viewer", "DLNA-Videoplayer",
  "Plex-Client iPhone", "Jellyfin-Client iOS", "Emby-Client iPad",
  "Untertitel-Player iOS", "SRT VTT ASS Untertitel", "sekundäre Untertitel iPhone",
  "Video-Equalizer iOS", "Audio-Equalizer Videoplayer", "externer DAC Video",
  "Video von Google Drive streamen", "Video von Dropbox streamen",
  "Video von OneDrive streamen", "Video von iCloud Drive streamen",
  "Video von MEGA streamen", "Video von NAS streamen",
  "Chromecast Video iPhone", "AirPlay 2 Video", "iCloud Videoplayer",
  "Fotos-Mediathek Videoplayer", "Apple Music Videoplayer",
  "Wi-Fi Drive Videoübertragung", "M3U Videowiedergabeliste",
  "Evervideo Premium", "Family Sharing Video-App"
]
tags: ["evervideo", "Anleitung", "Videoplayer", "PiP", "Untertitel", "RTSP", "Cloud", "FFmpeg"]
---


### Willkommen beim Evervideo-Handbuch

Evervideo ist ein voll ausgestatteter Cloud-Media-Player für iPhone, iPad und Mac, der jeden Cloud-Speicher, jede NAS oder jeden Medienserver in Ihre persönliche Mediathek verwandelt — ohne erneutes Hochladen und mit voller Kontrolle über Ihre Dateien.

Aufgebaut auf einer benutzerdefinierten FFmpeg-basierten Player-Engine mit hardwarebeschleunigter H.264- und HEVC-Dekodierung, spielt Evervideo praktisch jeden modernen Container und Codec — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS und die langen Reihen von FFmpeg-Formaten — in voller Qualität, mit intelligentem Puffern für flüssiges Streaming über Wi-Fi oder Mobilfunk. Picture-in-Picture hält Ihr Video über jeder anderen App, der kompakte Always-on-Screen-Player lässt Sie beim Durchsuchen Ihrer Mediathek weiter zuschauen, und Chromecast sowie AirPlay 2 übertragen die Wiedergabe mit einem Tippen auf Ihr TV-Gerät, Ihren HomePod oder Ihr Lautsprecher-Setup.

Evervideo verbindet sich mit einer bemerkenswert breiten Liste von Quellen, alles aus einer App:

- **Persönlicher Cloud-Speicher:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Selbst gehostete Medienserver:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (und ownCloud über die gemeinsame API) · Synology Drive · QNAP.
- **NAS- und Dateifreigabe-Protokolle:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (Passwort- oder Public-Key-Authentifizierung) · NFS · DLNA · UPnP.
- **Live- und IP-Kamera-Streams:** RTSP — richten Sie Evervideo auf eine beliebige RTSP-URL (`rtsp://camera-ip/stream`) und es spielt einfach ab.
- **S3-kompatibler Objektspeicher:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces und jeder andere S3-API-Endpunkt.
- **Geräteinterne Quellen:** die Fotos-Mediathek (Alle Videos, Kurz / Mittel / Lang, Bildschirmaufnahmen, plus Ihre Fotoalben), die Musik-App-Mediathek (Alben, Genres, Wiedergabelisten), USB / SD-Kartenlaufwerke und lokale Dateien.

### Ein Player für jedes Format und jeden Codec

Während die meisten iOS-Apps bei H.264 / H.265 innerhalb von MP4 / MOV aufhören, bündelt Evervideo FFmpeg neben Apples Systemcodecs, damit Sie Formate abspielen können, die das System nicht erkennt — MKV-Container, VP9, AV1, MPEG-2, OGG, Vorbis und viele mehr — und wechselt automatisch zwischen Hardware-H.264/HEVC-Dekodierung und Software-Dekodierung, basierend auf der Datei und dem Gerät.

Sie können die Videospur (Multi-Stream-Blu-ray-Rips), die Audiospur (Kommentarspuren, alternative Synchronisierungen) und die Untertitelspur auswählen. Externe SRT-, VTT- und ASS/SSA-Untertiteldateien werden mit einem Tippen geladen; erweitertes ASS/SSA-Styling wird dank der enthaltenen libass korrekt gerendert.

### Intelligente Untertitel

- **Untertitelspurauswahl** perfekt für das Sprachenlernen.
- **Externe Untertiteldateien** (`.srt`, `.vtt`, `.ass`, `.ssa`) von überall auf Ihrem Gerät oder aus der Cloud geladen.
- **libass** für vollständig gestyltes ASS/SSA-Rendering.
- **Pro-Spur- und globale Schriftartauswahl** für Untertitel.
- **Audiospurauswahl** — wählen Sie die Synchronisierung, den Kommentar oder die Regisseursspur.
- **Videospurauswahl** für Multi-Winkel- oder Multi-Version-Dateien.

### Bild und Ton einstellen

Zwei Equalizer nebeneinander: ein Audio-Equalizer zum Abstimmen von Bass und Höhen (mit Import / Export benutzerdefinierter Presets) und ein Video-Equalizer zum Anpassen von Helligkeit, Kontrast, Sättigung und Farbton (ebenfalls mit Import / Export). Beide Engines bieten auch audiophile Steuerungen: Audio-Ausgabe-Abtastrate, Kanalanzahl, IO-Pufferdauer und gemischter Modus — für Nutzer mit externen DACs und Heimkinoreceivern.

### Cast, AirPlay und Picture-in-Picture

- **Picture-in-Picture (PiP):** weiter zuschauen, während Sie andere Apps nutzen.
- **AirPlay 2:** Video an Apple TV, HomePod oder beliebigen AirPlay 2-Lautsprecher / -Fernseher senden.
- **Google Chromecast:** direkt auf ein Chromecast- oder Cast-fähiges TV-Gerät übertragen.
- **Kompakter Player:** ein dauerhafter Mini-Player oben auf jedem Bildschirm, damit Sie Ihre Mediathek durchsuchen können, ohne das Video zu verlieren.

### Datenschutz und Sicherheit

Evervideo verwendet offizielle SDKs und OAuth-basierte Anmeldungen von jedem Cloud-Anbieter, sodass Ihr Passwort nie die App erreicht. Zugriffstoken werden verschlüsselt im iOS/MacOS-Schlüsselbund gespeichert, jede Übertragung ist TLS-geschützt, und das Widerrufen des Zugriffs von Ihrem Cloud-Konto (oder das Entfernen von Evervideo vom Gerät) löscht alles sofort. Schützen Sie Ihre Mediathek optional mit einem 4-stelligen Passcode für eine zusätzliche Datenschutzebene.

### Erste Schritte mit Evervideo

Dieses Handbuch führt Sie durch jeden Teil von Evervideo auf iPhone, iPad und Mac — vom Verbinden von Cloud-Diensten, Durchsuchen Ihrer Mediathek, Herunterladen und Übertragen von Dateien, Verwalten von Wiedergabelisten bis hin zum Feinabstimmen des Media Players, der Equalizer, Untertitel und Picture-in-Picture. Verwenden Sie die Karten unten, um direkt zu dem Abschnitt zu springen, den Sie benötigen.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navigation" subtitle="Tab-Leiste auf iPhone, linkes Menü auf iPad und Mac, kompakter Always-on-Screen-Media-Player." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Dateien" subtitle="Ein einheitlicher Tab für Cloud, NAS, RTSP-Streams, lokale Dateien, USB-Laufwerke und die Übertragungswarteschlange." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Mediathek" subtitle="Nach Alben, Genres, Aktuell, Favoriten durchsuchen — plus die iOS-Fotos-Mediathek und Apple Music-Mediathek." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Wiedergabelisten" subtitle="Wiedergabelisten aus Cloud, lokalen Dateien, Fotos oder der Musik-Mediathek erstellen, M3U / M3U8 / CUE importieren." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Media Player" subtitle="Picture-in-Picture, Audio- und Videospuren, Untertitel, Audio- + Video-Equalizer, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Einstellungen" subtitle="Audio-Engine, Video-Decoder, Untertitel, Mediathek, Dateimanager, Widgets, Personalisierung, Sprache, Backup." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="FAQ" subtitle="Finden Sie Antworten auf die häufigsten Fragen zu Evervideo." >}}

{{< /cards >}}
