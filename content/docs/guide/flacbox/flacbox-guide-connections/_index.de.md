---
title: "Verbindungen"
date: 2020-02-01
description: "Erfahren Sie, wie Sie Cloud-Dienste und NAS-Geräte mit Flacbox verbinden. Streamen Sie hochauflösende Musik von iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk und mehr. Verwenden Sie SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing und USB-Flash-Laufwerke."
keywords: [
  "Flacbox Cloud-Einrichtung", "Google Drive mit Flacbox verbinden", "SMB Musik-Streaming",
  "WebDAV iOS-Player", "DLNA Musik-App", "NAS Audio-Streaming", "Wi-Fi Drive iPhone",
  "Dateien auf iPhone übertragen", "Flacbox iTunes File Sharing", "NAS mit iPhone verbinden",
  "Synology Drive Musik-App", "QNAP Musik-App", "Bluesound Musik-App",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm Scrobbling Musik-App",
  "iXpand Flash Drive Musik", "USB DAC iPhone"
]
tags: ["anleitung", "flacbox", "verbindungen", "cloud", "NAS"]
readingTime: 12
---


Auf diesem Bildschirm können Sie jede Quelle verbinden, die Ihre Musik enthält. Sie können beliebte Cloud-Dienste wie Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive und viele mehr integrieren sowie Ihren Mac, PC oder NAS über Standardprotokolle verbinden.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Verbindungen-Bildschirm" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Mit Cloud-Speicher verbinden

- Öffnen Sie den **Verbindungen**-Tab.
- Wählen Sie **Mit Cloud-Speicher verbinden** aus dem Menü.
- Wählen Sie einen Cloud-Speicherdienst aus der Liste.
- Geben Sie Ihre Zugangsdaten auf der offiziellen Autorisierungsseite des Cloud-Anbieters ein und tippen Sie dann auf **Fertig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Cloud-Speicherdienst hinzufügen" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Bei Problemen überprüfen Sie Ihre Internetverbindung und Ihre Anmeldedaten. In der Premium-Version können Sie eine unbegrenzte Anzahl von Diensten hinzufügen; die kostenlose Version unterstützt bis zu drei.

## Unterstützte Cloud-Speicherdienste, Medienserver und Protokolle

Flacbox unterstützt eine außergewöhnlich breite Palette von Quellen für Ihre Musik. Alles unten Aufgeführte funktioniert über einen einzigen **Mit Cloud-Speicher verbinden**-Bildschirm.

**Persönlicher Cloud-Speicher:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Selbst gehostete Server:** Plex · Jellyfin · Emby · Subsonic (und jeder Subsonic-kompatible Server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (und ownCloud über die gemeinsame API) · Synology Drive · QNAP.

**NAS- und Dateifreigabe-Protokolle:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, Passwort oder Public-Key-Auth) · NFS · DLNA / UPnP (Wiedergabe und Download).

**S3-kompatible Objektspeicherung:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces und jeder andere S3-API-Endpunkt.

**Lokale Netzwerkerkennung:** Der Bereich „Verfügbare Geräte" listet automatisch jeden Bonjour / mDNS-Dienst in Ihrem Wi-Fi-Netzwerk auf, sodass Sie tippen können, um eine Verbindung herzustellen, ohne eine IP-Adresse einzugeben.

Jede Verbindung verwendet das **offizielle SDK oder offene Protokoll** des Dienstes mit OAuth-basierter Autorisierung, wo unterstützt.

## Sicherheit und Datenschutz

Wir verwenden nur offizielle SDKs und sichere Verbindungen für die Interaktion mit verbundenen Cloud-Diensten. Ihr Login und Passwort sind für die Anwendung nicht zugänglich — alle Übertragungen sind TLS-verschlüsselt.

Wenn Sie Ihren Login und Ihr Passwort eingeben, zeigt Ihnen die Anwendung die offizielle Autorisierungsseite des Cloud-Dienstanbieters an. Der Cloud-Dienstanbieter sendet dann nach erfolgreicher Autorisierung einen Auth-Token an die Anwendung, und dieser Token wird für API-Aufrufe verwendet.

Ein Auth-Token ist ein digitaler Schlüssel, der Drittanbieter-Anwendungen ermöglicht, mit Cloud-Speicher in Ihrem Namen zu interagieren. Der Token wird auf Ihrem Gerät im sicheren Systemspeicher von Apple (Keychain) gespeichert.

Die Anwendung teilt keine Informationen aus Ihren verbundenen Cloud-Konten mit Everappz, Werbetreibenden oder Dritten.

## Auth-Token widerrufen

Um einen Auth-Token zu widerrufen, melden Sie sich in Ihrem Cloud-Konto in einem Webbrowser an und navigieren Sie zur Sicherheits- oder Verbundene-Apps-Seite. Detaillierte Anweisungen für Google-Konten sind [hier](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) verfügbar.

Sie können das Cloud-Konto auch innerhalb der Anwendung selbst trennen — dabei wird der Auth-Token sofort von Ihrem Gerät gelöscht.

## Cloud-Speicher trennen oder Konfiguration ändern

- **Auf Cloud-Speicheroptionen zugreifen** — finden Sie den verbundenen Dienst im **Verbindungen**-Bildschirm.
- **Tippen Sie auf die „..."-Schaltfläche** neben dem Diensttitel, um weitere Optionen zu öffnen:
  - **Umbenennen** — ändern Sie den Namen des Cloud-Dienstes in Ihrer Liste.
  - **Einstellungen** — ändern Sie die Konfiguration oder Authentifizierungsdaten.
  - **Trennen** — trennen Sie die Verbindung vollständig zwischen der App und dem Cloud-Dienst.

## Mit einem Computer oder NAS verbinden

Sie können Ihren Computer, ein persönliches NAS oder andere Netzwerkgeräte auch über die SMB-, DLNA- oder WebDAV-Protokolle verbinden.

## Mit einem Computer über SMB verbinden

- Tippen Sie auf **Mit Cloud-Speicher verbinden → SMB**.
- Geben Sie die IP-Adresse des Computers und den Namen des freigegebenen Ordners im URL-Feld ein: `smb://computer-ip-adresse/freigegebener-ordner`.
- Wählen Sie die Protokollversion: **Auto**, **SMB1** oder **SMB2**.
- Geben Sie Ihren Login und Ihr Passwort ein (falls erforderlich).
- Tippen Sie auf **Fertig**.

Ein vollständiges Tutorial zur SMB-Verbindung ist [hier](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) verfügbar.

## Mit einem NAS über WebDAV verbinden

Alle Schritte sind dieselben wie bei SMB, außer für das URL-Feld. Die URL sollte das Format `http://server-name` oder `https://server-name` haben. WebDAV funktioniert mit **Synology, QNAP, Nextcloud, ownCloud** und vielen anderen Servern.

Ein vollständiges Tutorial ist [hier](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) verfügbar.

## Mit einem Computer oder NAS über DLNA verbinden

Sie können eine Musikbibliothek auf Ihrem Windows-PC oder NAS über das DLNA / UPnP-Protokoll freigeben, wie [hier](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) beschrieben. DLNA ermöglicht nur das Abspielen oder Herunterladen von Musik — Sie können keine Dateien hochladen.

## Mit einem NAS oder Server über FTP, FTPS oder SFTP verbinden

Tippen Sie auf **Mit Cloud-Speicher verbinden → FTP**, geben Sie die Host-URL im Format `ftp://server-name` ein (oder `ftps://server-name` für eine verschlüsselte Verbindung), geben Sie Login und Passwort ein und tippen Sie auf **Fertig**. Für **SFTP** wählen Sie stattdessen **SFTP** und stellen entweder ein Passwort oder ein SSH-Schlüsselpaar zur Verfügung.

## Mit einer NFS-Freigabe verbinden

Flacbox unterstützt **NFS** (Network File System). Wählen Sie **NFS** im **Mit Cloud-Speicher verbinden**-Menü, geben Sie die Serveradresse und den exportierten Pfad ein und tippen Sie auf **Fertig**.

## Einen Plex Media Server verbinden

Tippen Sie auf **Mit Cloud-Speicher verbinden → Plex**, melden Sie sich mit Ihrem Plex-Konto an, wählen Sie einen Server aus, und die Bibliothek erscheint neben Ihren Cloud-Diensten.

## Einen Jellyfin- oder Emby-Server verbinden

Tippen Sie auf **Mit Cloud-Speicher verbinden → Jellyfin** oder **Emby**, geben Sie Ihre Server-URL und Zugangsdaten ein, und Ihre Musikbibliothek ist bereit zum Streamen.

## Einen Subsonic- oder Navidrome-Server verbinden

Tippen Sie auf **Mit Cloud-Speicher verbinden → Subsonic**, geben Sie die Server-URL und Zugangsdaten ein, und die Bibliothek erscheint im Verbindungen-Bildschirm.

## Mit S3-kompatiblem Objektspeicher verbinden

Tippen Sie auf **Mit Cloud-Speicher verbinden → S3-Speicher**, geben Sie dann die Endpunkt-URL, Region, Zugriffsschlüssel, geheimen Schlüssel und Bucket-Namen ein.

## Verfügbare Geräte

Dieser Bereich zeigt jedes Gerät in Ihrem lokalen Netzwerk, das Sie über Bonjour-Erkennung verbinden können.

- Öffnen Sie die App und gehen Sie zum Bereich **Verfügbare Geräte** unter Verbindungen.
- Tippen Sie auf das Gerät, mit dem Sie sich verbinden möchten.
- Geben Sie bei Bedarf Ihre Anmeldedaten ein.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Verfügbare Geräte im lokalen Netzwerk" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive ist eine praktische Technologie, die drahtlose Dateiübertragungen von Ihrem Computer auf Ihr iOS-Gerät über jeden Desktop-Browser ermöglicht.

### Wi-Fi Drive aktivieren

- Öffnen Sie die Anwendung und gehen Sie zum **Verbindungen**-Tab.
- Wählen Sie **Über Wi-Fi verbinden**, um den Wi-Fi Drive Hauptbildschirm zu öffnen.
- (Optional) Legen Sie einen Benutzernamen und ein Passwort für den eingebetteten Webserver fest.
- Tippen Sie auf **Wi-Fi Drive starten**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Drive auf Ihrem Computer aufrufen

- Öffnen Sie auf Ihrem Computer einen Webbrowser (wie Chrome, Firefox oder Safari).
- Geben Sie in die Adressleiste des Browsers die von der Anwendung bereitgestellte URL ein.

### Dateien drahtlos übertragen

Sobald die Webseite Ihres iOS-Geräts im Browser geöffnet ist, können Sie Dateien per Drag-and-Drop darauf ziehen.

Sie können Wi-Fi Drive auch direkt in Finder unter macOS einbinden (Gehe zu → Mit Server verbinden…) oder im Datei-Explorer unter Windows (Netzlaufwerk verbinden…).

Detaillierte Anweisungen sind [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) verfügbar.

## iTunes / Finder File Sharing

iTunes File Sharing (jetzt Finder File Sharing unter macOS Catalina und später) ist eine weitere Möglichkeit, Dateien per Lightning- oder USB-C-Kabel zu übertragen.

- Verbinden Sie das Gerät per Kabel mit dem Computer und starten Sie **Finder** auf dem Mac (oder **iTunes** unter Windows).
- Öffnen Sie **Speicherorte → Ihr verbundenes Gerät → Dateien** und finden Sie die Flacbox-App.
- Tippen Sie auf das App-Symbol, um alle freigegebenen Ordner anzuzeigen.
- Kopieren Sie Dateien per Drag-and-Drop in den freigegebenen Ordner.

Detaillierte Anweisungen sind [hier](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) verfügbar.

## Ein USB-Flash-Laufwerk verbinden

Wenn Sie eine SD-Karte oder ein USB-Laufwerk haben, können Sie es mit einem Lightning-zu-USB / SD-Kartenleser oder einem USB-C-Laufwerk (auf iPad und iPhone 15 / 16 / 17 / Pro) verbinden.

Detaillierte Anweisungen sind [hier](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it) verfügbar.

## Datei-Manager

Tippen Sie auf das Symbol eines verbundenen Cloud-Speicherdienstes, um alle verfügbaren Dateien und Ordner anzuzeigen.

## Obere Symbolleiste

Die obere Symbolleiste bietet mehrere nützliche Aktionen für schnellen Zugriff.

- **Suchen** — schnelle Suche im aktuellen Verzeichnis.
- **Wiedergabe fortsetzen** — stellt die Audio-Player-Warteschlange und die letzte Medienposition für den aktuellen Ordner wieder her.
- **Alle abspielen** — scannt den aktuellen Ordner und seine Unterordner und fügt alle gefundenen Audiodateien zu einer neuen Warteschlange hinzu.
- **Alles zufällig abspielen** — wie „Alle abspielen", mischt aber die Dateien vorher.

## Ordner-Optionen

Wenn Sie einen Ordner öffnen, finden Sie nützliche Aktionen über die **„..."**-Schaltfläche oben rechts.

- **Auswählen** — Dateiauswahlmodus aktivieren.
- **Neuer Ordner** — einen neuen Ordner im aktuellen Ordner erstellen.
- **Offline-Modus aktivieren** — Offline-Modus für den aktuellen Ordner einschalten.
- **Dateien hochladen** — Dateien von Ihrem Gerät in den Online-Ordner hochladen.
- **Suchen** — nach bestimmten Dateien im aktuellen Ordner suchen.
- **Sortieren** — Dateien nach Name, Größe, Änderungsdatum oder Metadaten sortieren.
- **Raster- / Listenansicht** — zwischen Tabellenansicht und Miniaturansicht wechseln.

## Online-Dateien bearbeiten

Wenn Sie mehrere Dateien in Ihrem Cloud-Speicher verwalten möchten, verwenden Sie den **Auswahlmodus**:

- **Auswahlmodus aktivieren** — tippen Sie auf die **„..."**-Schaltfläche oben rechts und wählen Sie **Auswählen**.
- **Dateien auswählen** — Kontrollkästchen erscheinen neben jeder Datei und jedem Ordner.
- **Aktionen ausführen** — einmal ausgewählt, haben Sie Zugriff auf „Weiter abspielen", „Später abspielen", „Zur Musikbibliothek hinzufügen", „Zu einer Playlist hinzufügen", „Kopieren", „Hochladen", „Verschieben", „Umbenennen" und „Löschen".

## Dateiaktionen

Tippen Sie auf das **„..."**-Symbol neben dem Dateititel, um das Aktionsmenü zu öffnen:

- **Weiter abspielen** — die Datei oben in die Player-Warteschlange einfügen.
- **Später abspielen** — die Datei unten in die Player-Warteschlange anhängen.
- **Zur Musikbibliothek hinzufügen** — die Datei in Ihre Musikbibliothek integrieren.
- **Zu einer Playlist hinzufügen** — die Datei zu einer vorhandenen Playlist hinzufügen oder eine neue erstellen.
- **Audio-Tags bearbeiten** — den integrierten Tag-Editor öffnen.
- **Zu Favoriten hinzufügen** — die Datei zu Ihrer Favoritenliste hinzufügen.
- **Herunterladen** — die Datei oder den Ordner für die Offline-Nutzung herunterladen.
- **Umbenennen** — die Datei direkt im Remote-Speicher umbenennen.
- **Verschieben** — die Datei in einen anderen Ordner in Ihrem Cloud-Speicher verschieben.
- **Öffnen in** — die Datei in eine andere kompatible App exportieren.
- **Löschen** — die Datei dauerhaft aus Ihrem Cloud-Speicher entfernen. **Diese Aktion kann nicht rückgängig gemacht werden.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Weitere Aktionen für eine Datei im verbundenen Cloud-Speicher" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

## Ordneraktionen

Tippen Sie auf das **„..."**-Symbol neben dem Ordnertitel für verfügbare Aktionen:

- **Alle abspielen** — die aktuelle Player-Warteschlange durch alle Elemente im ausgewählten Ordner ersetzen.
- **Weiter abspielen** — den gesamten Ordner oben in die Player-Warteschlange hinzufügen.
- **Später abspielen** — den Ordnerinhalt unten in die Player-Warteschlange anhängen.
- **Zur Musikbibliothek hinzufügen** — den Ordnerinhalt in Ihre Musikbibliothek integrieren.
- **Zu Playlist hinzufügen** — den gesamten Ordner zu einer Playlist hinzufügen.
- **Zu Favoriten hinzufügen** — den Ordner zu Ihren Favoriten hinzufügen.
- **Offline-Modus aktivieren** — den Ordner kontinuierlich auf neue Dateien überwachen.
- **Herunterladen** — alle Inhalte des Ordners herunterladen.
- **Umbenennen** — den Ordner direkt im Remote-Speicher umbenennen.
- **Verschieben** — den Ordner an einen anderen Speicherort verschieben.
- **Archivieren (ZIP)** — den Ordnerinhalt in eine ZIP-Datei bündeln (Premium-Funktion).
- **Löschen** — den Ordner und seinen Inhalt dauerhaft entfernen. **Diese Aktion kann nicht rückgängig gemacht werden.**

## Schnellzugriff

Der Schnellzugriff-Bereich befindet sich oben auf dem Bildschirm und bietet schnellen Zugriff auf Ihre Lieblings- und zuletzt geöffneten Dateien aus verbundenen Cloud-Diensten.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Online-Links und Schnellzugriff" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Weitere Dienste

Dieser Bereich zeigt zusätzliche Funktionen. Derzeit unterstützt die App **Last.fm**-Scrobbling — wenn verbunden, werden Ihre Wiedergabestatistiken automatisch an Ihr Last.fm-Konto gesendet. Detaillierte Setup-Anweisungen sind [hier](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm) verfügbar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm verbinden" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
