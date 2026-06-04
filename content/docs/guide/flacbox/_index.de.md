---
date: 2020-01-01
title: 'Flacbox'
description: 'Erfahren Sie, wie Sie Flacbox verwenden — den hochauflösenden FLAC-, DSD-, ALAC- und FFmpeg-betriebenen Cloud-Musikplayer für iPhone, iPad und Mac. Verbinden Sie iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB und DLNA. Streamen und laden Sie hochauflösendes Audio herunter, bearbeiten Sie Metadaten, hören Sie Hörbücher, scrobblen Sie zu Last.fm, nutzen Sie Apple CarPlay und Home-Screen-Widgets und passen Sie den 10-Band-Equalizer an.'
keywords: [
  "Flacbox Benutzerhandbuch", "Flacbox Anleitung", "Hi-Res Musikplayer iPhone", "FLAC-Player iPhone",
  "DSD-Player iOS", "ALAC-Player Mac", "verlustfreie Musik-App", "Cloud-Musikplayer iPhone",
  "Offline-FLAC-Player Mac", "Musikbibliotheksmanager", "Audio-Tag-Editor",
  "CarPlay FLAC-Player", "Chromecast Audio-App", "AirPlay 2 Musik",
  "Flacbox Widgets", "Flacbox CarPlay", "FFmpeg Musikplayer iOS",
  "Hörbuch-Player iPhone", "Audio-Lesezeichen iOS", "Tonhöhenkorrektur Musik-App",
  "Audio-Ausgabe Abtastrate", "externer DAC iPhone", "USB DAC Mac",
  "Synology Musik-App", "QNAP Musik-App", "NAS Musikplayer iPhone",
  "WebDAV Musikplayer", "SMB Musik-Streaming", "DLNA Musikplayer",
  "iCloud Drive Musik", "Google Drive FLAC", "Dropbox FLAC-Player",
  "Wi-Fi Drive Musikübertragung", "M3U Playlist importieren", "Last.fm Scrobbling"
]
tags: ["flacbox", "anleitung", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widgets"]
---


### Willkommen beim Flacbox-Handbuch

Flacbox ist ein hochauflösender Musikplayer für iPhone, iPad und Mac, mit dem Sie Ihren bevorzugten Cloud-Speicher, NAS und Medienserver in Ihren eigenen persönlichen Streaming-Dienst verwandeln können.

Flacbox verbindet sich mit einer bemerkenswert breiten Liste von Quellen — alles in einer App:

- **Persönlicher Cloud-Speicher:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Selbst gehostete Server:** Plex · Jellyfin · Emby · Subsonic (und jeder Subsonic-kompatible Server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (und ownCloud über die gemeinsame API) · Synology Drive · QNAP.
- **NAS- und Dateifreigabe-Protokolle:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (Passwort- oder Public-Key-Auth) · NFS · DLNA / UPnP (Wiedergabe und Download). Funktioniert mit Apple Time Capsule, Synology, QNAP, WD My Cloud, jedem Linux Samba / NFS / SSH-Host oder einem freigegebenen Ordner auf Ihrem Mac oder Windows-PC.
- **S3-kompatible Objektspeicherung:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces und jeder andere S3-API-Endpunkt.
- **Lokale Netzwerkerkennung:** Der Bereich „Verfügbare Geräte" listet automatisch jeden Bonjour / mDNS-Dienst in Ihrem Wi-Fi auf — Plex, Jellyfin, Emby-Server, Synology, QNAP, AirPort-Router mit angeschlossenen Laufwerken, Time Capsule — sodass Sie tippen können, um eine Verbindung herzustellen, ohne eine IP-Adresse einzugeben.

Während die meisten Musik-Apps auf Apples eingebaute Audio-Engine beschränkt sind, bündelt Flacbox **FFmpeg** neben den System-Codecs, sodass Sie Formate abspielen können, die iOS nicht von Haus aus unterstützt — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV sowie die reguläre MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC-Familie. Kombiniert mit einer konfigurierbaren Audio-Ausgabe-Abtastrate (44,1 / 48 / 64 / 88,2 / 96 kHz), Mehrkanal-Ausgabe (Mono → 5.1 → SDDS → ITU BS.775-1), IO-Puffer-Abstimmung und Tonhöhenkorrektur bietet Flacbox Audiophilen eine Kontrolle, die die meisten Consumer-Musik-Apps schlicht nicht bieten.

### Genießen Sie reibungsloses Streaming und Offline-Wiedergabe

Flacbox verfügt über intelligentes Buffering für reibungsloses Streaming und einen integrierten Download-Manager, mit dem Sie ganze Playlists, Künstler, Alben, Ordner oder einzelne Titel auf Ihr Gerät herunterladen können. Wenn der Speicher knapp wird, löschen Sie gecachte Dateien mit einem Tipp und streamen Sie weiter aus der Cloud. Der Offline-Modus für Ordner, Playlists, Alben und Künstler synchronisiert auch automatisch neue Titel, sobald sie in der Cloud erscheinen, damit Ihre Offline-Sammlung immer aktuell bleibt.

### Automatisch organisierte Musikbibliothek

Wenn Sie Audiotitel importieren, scannt Flacbox deren Metadaten und organisiert sie in einer übersichtlichen Musikbibliothek — gruppiert nach Songs, Nicht gespielte Songs, Alben, Albumkünstler, Künstler, Genres und Komponisten. Nutzen Sie die integrierte Suche, um in Sekunden etwas zu finden, filtern Sie nach Quelle (Online-Cloud / offline / Gerät) und wählen Sie zwischen einfachem, gruppierten und Tab-basierten Bibliotheks-Layouts.

### Metadaten reparieren und Musik taggen

Wenn Sie auf beschädigte Tags oder unordentliche Kodierungen stoßen, kann der integrierte ID3-Tag-Editor diese bereinigen — manuell oder mit automatischen MusicBrainz-Lookups. Sie können auch fehlerhafte Zeichenkodierungen normalisieren, nach fehlenden Album-Covern suchen und Änderungen automatisch in die Originaldatei in der Cloud zurückschreiben.

### Einfache Übertragungen von Mac, PC oder NAS

Übertragen Sie Musik zwischen Ihrem Computer und Ihrem iPhone oder iPad mit einem dieser Tools: SMB, WebDAV, DLNA, Wi-Fi Drive (Drag-and-Drop in jedem Desktop-Browser), iTunes / Finder-Dateifreigabe über ein Lightning- oder USB-C-Kabel, USB-Flash-Laufwerke oder iXpand Flash Drives.

### Passen Sie Ihren Klang mit dem Equalizer an

Flacbox enthält einen 10-Band-Equalizer mit iPod-artigen Presets (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz und viele mehr), einen Vorverstärker und die Möglichkeit, eigene Presets zu speichern.

### Hörbuch-freundlich

Flacbox ist ein großartiger Hörbuch-Player — mehrere Lesezeichen pro Titel, fein abgestufte Wiedergabegeschwindigkeit (0,02× bis 3,00×), Wiedergabe fortsetzen, um genau dort weiterzumachen, wo Sie aufgehört haben, anpassbare Sprung-Zeit-Tasten und ein Einschlaf-Timer. M4B-Kapitelmarkierungen und lange Dateien werden vollständig unterstützt.

### Überall streamen — auch im Auto und auf dem Home-Screen

Streamen Sie Musik über AirPlay 2 zu Apple TV / HomePod, senden Sie es an Google Chromecast-Lautsprecher und Cast-fähige TVs und nehmen Sie alles mit Apple CarPlay mit. Nutzen Sie Home-Screen-Widgets auf iPhone und iPad, um den aktuell abgespielten Titel auf einen Blick zu sehen, und Last.fm-Scrobbling, um Ihren Hörverlauf über Apps hinweg zu behalten.

### Datenschutz und Sicherheit

Flacbox verwendet nur offizielle SDKs und OAuth-basierte Logins von jedem Cloud-Anbieter — Ihr Passwort gelangt nie in die App. Zugriffstoken werden verschlüsselt im iOS Keychain gespeichert, alle Übertragungen sind TLS-geschützt, und das Widerrufen des Zugriffs in Ihrem Cloud-Konto oder das Entfernen von Flacbox vom Gerät löscht alles sofort.

### Erste Schritte mit Flacbox

Dieses Handbuch führt Sie durch jeden Teil von Flacbox auf iPhone, iPad und Mac — vom Verbinden von Cloud-Diensten, Organisieren Ihrer Bibliothek, Übertragen von Dateien und Verwalten von Playlists bis hin zur Feinabstimmung des Equalizers und der Konfiguration der Audio-Engine.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigation" subtitle="Tab-Leiste auf iPhone, linkes Menü auf iPad und Mac, Mini-Player, Widgets, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Verbindungen" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Musikbibliothek" subtitle="Songs, Alben, Künstler, Genres, Komponisten — synchronisieren, suchen, Metadaten bearbeiten." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Wiedergabelisten" subtitle="Erstellen, M3U / M3U8 / CUE importieren, neu anordnen und in M3U / CSV / TXT exportieren." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Lokale Dateien" subtitle="Offline-Musik, USB-Laufwerke, Wi-Fi Drive, Datei-Manager, Offline-Ordner." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Audio-Player" subtitle="Hi-Res-Ausgabe, Equalizer, Tonhöhe, Lesezeichen, AirPlay, Chromecast, Geschwindigkeit, Einschlaf-Timer." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Einstellungen" subtitle="Audio-Engine, Bibliothek, Datei-Manager, CarPlay, Widgets, Personalisierung, Sprache, Backup." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Finden Sie Antworten auf die 50 häufigsten Fragen zu Flacbox." >}}

{{< /cards >}}
