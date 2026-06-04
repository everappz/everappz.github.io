---
title: "Dateien"
date: 2020-02-01
lastmod: 2026-06-01
description: "Erfahren Sie, wie Sie den Dateien-Tab in Evervideo auf iPhone, iPad und Mac verwenden. Verbinden Sie Cloud-Dienste, NAS-Geräte, Medienserver und RTSP-Streams an einem Ort. Verwalten Sie Offline-Videos, die Übertragungswarteschlange, Downloads, Wi-Fi Drive, iTunes / Finder-Dateifreigabe und USB-Laufwerke. Enthält iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA und S3-kompatiblen Speicher."
keywords: [
  "Evervideo Dateien", "Evervideo Verbindungen", "Evervideo lokale Dateien",
  "Cloud-Video-Einrichtung iPhone", "Google Drive Video verbinden", "SMB Video-Streaming",
  "WebDAV Videoplayer iOS", "DLNA Video iPhone", "NAS Video-Streaming",
  "Wi-Fi Drive Videoübertragung", "Evervideo iTunes Dateifreigabe", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo Offline-Modus Video", "Evervideo Übertragungswarteschlange",
  "Evervideo Dateimanager", "Evervideo Dokumente Ordner",
  "Videoplayer Synology", "Videoplayer QNAP",
  "Videoplayer Apple Time Capsule", "USB DAC Video",
  "iXpand Videoplayer", "S3 Videoplayer"
]
tags: ["Anleitung", "evervideo", "Dateien", "Verbindungen", "Cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Der Dateien-Tab ist Evervideo's All-in-One-Dateimanager. Im Gegensatz zu den meisten Video-Apps, die Cloud-Speicher von lokalen Dateien in verschiedene Tabs aufteilen, fasst Evervideo beides in einem einzigen, scrollbaren Bildschirm zusammen, sodass Sie von einem Plex-Server zu einem Cloud-Ordner zu Ihrem iPhone-Dokumente-Ordner wechseln können, ohne zwischen Tabs zu wechseln.

Der Dateien-Tab ist in klare Abschnitte unterteilt, die in dieser Reihenfolge auf Ihrem Bildschirm erscheinen:

- **Schnellzugriff** — Aktuell und Favoriten für Dateien und Ordner, die Sie zuletzt geöffnet haben.
- **Dateien in dieser Anwendung** — was im sandboxed-Dokumente-Ordner von Evervideo liegt.
- **Dateien auf diesem iPhone / iPad / Mac** — Videos an anderer Stelle auf Ihrem Gerät, die über die Systemdateiauswahl angezeigt werden.
- **Cloud-Speicher** — jedes Cloud-Konto, jede NAS und jeder Medienserver, den Sie verbunden haben.
- **Verfügbare Geräte** — per Bonjour / mDNS automatisch erkannte Server und Laufwerke in Ihrem lokalen Netzwerk.

In der oberen rechten Ecke des Dateien-Bildschirms befindet sich eine Übertragungs-Schaltfläche (ein Symbol mit drehenden Pfeilen). Tippen Sie darauf, um die Übertragungswarteschlange zu öffnen, in der Sie jeden Download und Upload über alle Ihre Quellen hinweg überwachen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Dateien über verbundene Speicher" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Mit Cloud-Speicher verbinden

Der Cloud-Speicher-Abschnitt des Dateien-Tabs ist der Ort, an dem jedes verbundene Konto, jede NAS, jeder Medienserver und jeder Stream lebt — nebeneinander in einer einzigen scrollbaren Liste.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Cloud-Speicher-Abschnitt im Dateien-Tab" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Öffnen Sie den **Dateien**-Tab.
- Scrollen Sie zum **Cloud-Speicher**-Abschnitt.
- Tippen Sie auf **Mit Cloud-Speicher verbinden** aus dem Menü.
- Wählen Sie einen Cloud-Speicherdienst aus der Liste.
- Geben Sie Ihre Anmeldedaten auf der offiziellen Autorisierungsseite des Cloud-Anbieters ein und tippen Sie auf **Fertig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Mit einem Cloud-Speicherdienst verbinden" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Wenn Probleme auftreten, überprüfen Sie Ihre Internetverbindung und Ihren Benutzernamen / Ihr Passwort. In der Premium-Version der App können Sie eine unbegrenzte Anzahl von Diensten hinzufügen; die kostenlose Version unterstützt bis zu drei.

## Unterstützte Cloud-Speicherdienste, Medienserver und Protokolle

Evervideo unterstützt eine außergewöhnlich breite Palette von Quellen für Ihre Videos. Alles unten funktioniert über einen einzigen Verbindungs-zu-Cloud-Speicher-Ablauf.

**Persönlicher Cloud-Speicher:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Selbst gehostete Medienserver:** Plex · Jellyfin · Emby · Subsonic (und jeder Subsonic-kompatible Server — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (und ownCloud über die gemeinsame API) · Synology Drive · QNAP.

**NAS- und Dateifreigabe-Protokolle:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, Passwort oder Public-Key-Authentifizierung) · NFS · DLNA / UPnP (Wiedergabe und Download).

**Live- und IP-Kamera-Streams:** RTSP — richten Sie Evervideo auf eine beliebige `rtsp://`-URL und es spielt einfach ab. Ideal für Sicherheitskameras, IPTV-Streams, Türklingelkameras, Babymonitore und ähnliche Live-Quellen.

**S3-kompatibler Objektspeicher:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces und jeder andere S3-API-Endpunkt.

**Geräteinterne Bibliotheken:** die Fotos-Mediathek (alle Videos, Bildschirmaufnahmen, Fotoalben) und die Musik-App-Mediathek (Alben, Genres, Wiedergabelisten) — beide erscheinen innerhalb der Mediathek, sodass Sie nichts kopieren müssen.

**Lokale Netzwerkerkennung:** Der Abschnitt Verfügbare Geräte listet automatisch jeden Bonjour / mDNS-Dienst in Ihrem Wi-Fi-Netzwerk auf — Plex, Jellyfin, Emby-Server, Synology, QNAP, AirPort-Router mit angeschlossenen Laufwerken, Apple Time Capsule — sodass Sie tippen können, um sich zu verbinden, ohne eine IP-Adresse eingeben zu müssen.

Jede Verbindung verwendet das offizielle SDK oder das offene Protokoll des Dienstes, mit OAuth-basierter Autorisierung, wo unterstützt. Sie können mehrere Konten desselben Dienstes verbinden (zum Beispiel zwei Google Drive-Konten oder sowohl einen Plex- als auch einen Jellyfin-Server) und sie nebeneinander im Cloud-Speicher-Abschnitt durchsuchen.

## Sicherheit und Datenschutz

Evervideo verwendet nur offizielle SDKs und sichere Verbindungen für die Interaktion mit verbundenen Cloud-Diensten. Ihr Benutzername und Ihr Passwort sind für die Anwendung nicht zugänglich — alle Übertragungen sind TLS-verschlüsselt.

Wenn Sie Ihren Benutzernamen und Ihr Passwort eingeben, zeigt Ihnen die Anwendung die offizielle Autorisierungsseite des Cloud-Dienstanbieters, und der gesamte Autorisierungsprozess findet außerhalb der Anwendung statt. Der Cloud-Dienstanbieter sendet dann nach erfolgreicher Autorisierung ein Auth-Token an die Anwendung, und dieses Token wird für API-Aufrufe verwendet.

Ein Auth-Token ist ein digitaler Schlüssel, der es Drittanbieter-Anwendungen ermöglicht, im Namen des Benutzers mit dem Cloud-Speicher zu interagieren. Das Token wird auf Ihrem Gerät im sicheren Apple-Systemspeicher (Schlüsselbund) gespeichert, der im Ruhezustand verschlüsselt und durch Ihren Gerätepasscode oder Ihren biometrischen Sperrmechanismus geschützt ist. Sie können Dateien von verbundenen Cloud-Diensten auf Ihr Gerät herunterladen; diese Dateien werden im Dokumente-Verzeichnis der App abgelegt und können jederzeit mit dem integrierten Dateimanager entfernt werden.

Die Anwendung teilt keine Informationen aus Ihren verbundenen Cloud-Konten mit Everappz, Werbetreibenden oder Dritten. Sie können den Zugriff auf Ihr Cloud-Konto jederzeit widerrufen, indem Sie die Kontoeinstellungsseite in Ihrem Webbrowser öffnen.

## Auth-Token widerrufen

Um ein Auth-Token zu widerrufen, melden Sie sich in einem Webbrowser bei Ihrem Cloud-Konto an und navigieren Sie zur Seite Sicherheit oder Verbundene Apps. Dort können Sie jede Drittanbieter-App finden, die mit Ihrem Cloud-Konto verbunden ist, und jede davon entfernen, wenn Sie sie nicht mehr verwenden möchten. Detaillierte Anweisungen für Google-Konten sind [hier](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) verfügbar.

Sie können das Cloud-Konto auch innerhalb der Anwendung selbst trennen — wenn Sie dies tun, wird das Auth-Token sofort von Ihrem Gerät gelöscht. Wenn Sie die Anwendung von Ihrem Gerät deinstallieren, werden alle heruntergeladenen Daten und Zugriffstoken automatisch damit entfernt.

## Cloud-Speicher trennen oder Konfiguration ändern

- **Auf Cloud-Speicher-Optionen zugreifen** — suchen Sie den verbundenen Dienst im **Cloud-Speicher**-Abschnitt des Dateien-Tabs.
- **Tippen Sie auf die "..."-Schaltfläche** neben dem Servicetitel, um zusätzliche Optionen zu öffnen:
  - **Umbenennen** — den Namen des Cloud-Dienstes ändern, wie er in Ihrer Liste erscheint.
  - **Einstellungen** — Konfiguration oder Authentifizierungsdaten ändern. Manchmal müssen Sie den verbundenen Cloud-Dienst erneut autorisieren, wenn das Autorisierungstoken abgelaufen ist.
  - **Trennen** — die Verbindung zwischen der App und dem Cloud-Dienst vollständig unterbrechen. Dies entfernt alle mit diesem Dienst verknüpften Videos aus Ihrer Mediathek, lässt sie aber auf dem Server unberührt.

## Mit einem Computer oder NAS verbinden

Sie können Ihren Computer, Ihre persönliche NAS oder ein anderes Netzwerkgerät über das SMB-, WebDAV-, FTP / FTPS-, SFTP-, NFS- oder DLNA-Protokoll verbinden. Dies ist der einfachste Weg, eine bestehende Heim-Mediathek — ob sie auf einem Mac, Windows-PC, Synology, QNAP, Apple Time Capsule oder WD My Cloud Home lebt — ohne Kopieren in Evervideo zu integrieren.

### Mit einem Computer über SMB verbinden

- Tippen Sie auf **Mit Cloud-Speicher verbinden → SMB**.
- Geben Sie die IP-Adresse des Computers und den Namen des freigegebenen Ordners im Format `smb://computer-ip-address/shared-folder-name` ein.
- Wählen Sie die Protokollversion: **Auto**, **SMB1** oder **SMB2**.
- Geben Sie Ihren Benutzernamen und Ihr Passwort ein (falls erforderlich).
- Tippen Sie auf **Fertig**.

Wenn die Verbindung erfolgreich ist, erscheint die Freigabe im Cloud-Speicher-Abschnitt. Ein vollständiges Tutorial zum Verbinden Ihres Mac oder PCs über SMB ist [hier](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) verfügbar.

### Mit einer NAS über WebDAV verbinden

Alle Schritte sind die gleichen wie bei SMB, außer dem URL-Feld. Verwenden Sie `http://server-name` oder `https://server-name`, wenn der Server SSL unterstützt. WebDAV funktioniert mit Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home und jedem anderen Server mit einem WebDAV-Endpunkt.

Ein vollständiges Tutorial über WebDAV ist [hier](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) verfügbar.

### Über DLNA / UPnP verbinden

Teilen Sie eine Mediathek auf Ihrem Windows-PC oder NAS über das DLNA / UPnP-Protokoll und greifen Sie darauf in Evervideo zu, wie [hier](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) beschrieben. DLNA wird weitgehend unterstützt, aber es ermöglicht Ihnen nur, Videos abzuspielen oder herunterzuladen — Sie können keine Dateien auf einem DLNA-Server hochladen oder neue Ordner erstellen.

### Über FTP, FTPS oder SFTP verbinden

Evervideo unterstützt auch die klassischen Dateiübertragungsprotokolle. Um einen Server über FTP oder FTPS zu verbinden, tippen Sie auf Mit Cloud-Speicher verbinden → FTP, geben Sie die Host-URL in der Form `ftp://server-name` (oder `ftps://server-name` für eine verschlüsselte Verbindung) ein, geben Sie Ihren Benutzernamen und Ihr Passwort an, und tippen Sie auf Fertig. Für SFTP (SSH File Transfer Protocol) wählen Sie stattdessen SFTP und geben Sie entweder ein Passwort oder ein SSH-Schlüsselpaar an.

### Mit einer NFS-Freigabe verbinden

Evervideo enthält NFS (Network File System)-Unterstützung — praktisch für Linux-Hosts, BSD-Server und NAS-Geräte, die Videobibliotheken lieber über NFS als über SMB zugänglich machen. Wählen Sie NFS im Menü Mit Cloud-Speicher verbinden, geben Sie die Serveradresse und den exportierten Pfad ein und tippen Sie auf Fertig.

## Einen Plex Media Server verbinden

Evervideo kann sich direkt mit einem Plex Media Server verbinden und Ihre Filmbibliotheken, TV-Shows und Home Videos durchsuchen. Tippen Sie auf Mit Cloud-Speicher verbinden → Plex, melden Sie sich mit Ihrem Plex-Konto an, wählen Sie einen Server, und die Bibliothek erscheint neben Ihren Cloud-Diensten. Plex-Server im gleichen lokalen Netzwerk werden auch automatisch im Abschnitt Verfügbare Geräte erkannt.

## Einen Jellyfin- oder Emby-Server verbinden

Sowohl Jellyfin (Open-Source) als auch Emby (kommerziell) Medienserver funktionieren nativ in Evervideo. Tippen Sie auf Mit Cloud-Speicher verbinden → Jellyfin oder Emby, geben Sie Ihre Server-URL (typischerweise etwas wie `http://server-ip:8096`) und Ihre Anmeldedaten ein, und Ihre Bibliothek ist bereit zum Streamen.

## Einen Subsonic- oder Navidrome-Server verbinden

Evervideo spricht die Subsonic-API, was bedeutet, dass es mit Subsonic selbst, Navidrome und jedem anderen Subsonic-kompatiblen Server funktioniert — einschließlich Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) und Ampache. Tippen Sie auf Mit Cloud-Speicher verbinden → Subsonic, geben Sie die Server-URL und Ihre Anmeldedaten ein, und die Bibliothek erscheint im Cloud-Speicher-Abschnitt.

## Einen RTSP-Stream verbinden (IP-Kameras, Live-TV, IPTV)

Evervideo hat native RTSP-Unterstützung, sodass Sie es auf jede RTSP-Quelle richten können — Sicherheitskameras, Türklingelkameras, IPTV-Anbieter, Babymonitore, Sendungen — und Evervideo wird den Stream live abrufen und dekodieren. Tippen Sie auf Online-Links → Link hinzufügen, fügen Sie die vollständige URL (`rtsp://camera-ip:port/stream-path`) ein, geben Sie Benutzernamen und Passwort an, falls erforderlich, und tippen Sie auf Fertig.

## Mit S3-kompatiblem Objektspeicher verbinden

Für Selbsthosting-Nutzer und Power-User, die Cloud-Objektspeicher verwenden, enthält Evervideo einen S3-kompatiblen Konnektor. Tippen Sie auf Mit Cloud-Speicher verbinden → S3-Speicher, geben Sie dann die Endpunkt-URL, Region, Zugriffsschlüssel, geheimen Schlüssel und Bucket-Namen ein. Dies funktioniert mit AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces und jedem anderen S3-API-Endpunkt.

## Verfügbare Geräte

Dieser Abschnitt zeigt jedes Gerät in Ihrem lokalen Netzwerk, mit dem Sie sich von Evervideo aus über Bonjour / mDNS-Erkennung verbinden können — Plex, Jellyfin, Emby-Server, Synology, QNAP, AirPort-Router mit angeschlossenen Laufwerken, Apple Time Capsule und so weiter. So stellen Sie eine Verbindung her:

- Scrollen Sie zum Abschnitt Verfügbare Geräte im Dateien-Tab.
- Tippen Sie auf das Gerät, mit dem Sie sich verbinden möchten.
- Falls erforderlich, geben Sie Ihre Anmeldedaten ein, um die Verbindung abzuschließen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Verfügbare Geräte im lokalen Netzwerk" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive ermöglicht es Ihnen, Dateien kabellos von Ihrem Computer auf Ihr iOS-Gerät über einen Desktop-Browser, Finder oder den Datei-Explorer zu übertragen. Ihr Gerät und Ihr Computer müssen sich im gleichen Wi-Fi-Netzwerk befinden.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Drive aktivieren

- Scrollen Sie im Dateien-Tab zu Cloud-Speicher → Über Wi-Fi verbinden, um den Wi-Fi Drive-Hauptbildschirm zu öffnen.
- (Optional) Legen Sie einen Benutzernamen und ein Passwort für den eingebetteten Webserver fest.
- Tippen Sie auf Wi-Fi Drive starten.

### Auf Wi-Fi Drive auf Ihrem Computer zugreifen

- Öffnen Sie einen Webbrowser auf Ihrem Computer (Chrome, Firefox, Safari usw.).
- Geben Sie die von der Anwendung angezeigte URL ein.
- Ziehen Sie Dateien von Ihrem Computer auf die Webseite — sie beginnen auf Ihr iOS-Gerät zu übertragen.

Sie können Wi-Fi Drive auch direkt in **Finder** auf macOS (Gehe zu → Mit Server verbinden…) oder im Datei-Explorer unter Windows (Netzlaufwerk verbinden…) einbinden und Ihr iPhone oder iPad als reguläres Netzlaufwerk behandeln.

Detaillierte Anweisungen sind [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) verfügbar.

## iTunes / Finder-Dateifreigabe

iTunes-Dateifreigabe (jetzt Finder-Dateifreigabe auf macOS Catalina und später) ermöglicht die Übertragung von Dateien über ein Lightning- oder USB-C-Kabel. Verbinden Sie das Gerät, öffnen Sie Finder auf dem Mac (oder iTunes unter Windows), suchen Sie Evervideo in der Apps-Liste, und kopieren Sie Dateien in den freigegebenen Ordner.

## Ein USB-Flash-Laufwerk oder eine SD-Karte verbinden

Schließen Sie ein USB-Laufwerk oder eine SD-Karte über den Lightning-zu-USB / USB-C-Adapter oder Kartenleser an Ihr iPhone, iPad oder Mac an. Öffnen Sie Dateien → Dateien auf diesem iPhone → Ordner öffnen, navigieren Sie zum Laufwerk, und wählen Sie eine Videodatei oder einen Ordner. Evervideo spielt Dateien direkt vom Laufwerk ab, ohne sie in den internen Speicher zu kopieren — praktisch für sehr große 4K-Bibliotheken.

## Ordner-Navigation in verbundenen Speichern

Tippen Sie auf einen verbundenen Cloud-Dienst, um seinen Datei-Browser zu öffnen. Ordner zeigen Video-Miniaturbilder, wenn verfügbar, und das Tippen auf ein Video startet die Wiedergabe sofort, während der Rest der Datei im Hintergrund weiter gestreamt wird.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Ordner in verbundenen Speichern durchsuchen" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Schnellzugriff

Der Schnellzugriff-Abschnitt befindet sich oben im Dateien-Tab. Er gibt Ihnen schnellen Zugriff auf Ihre favorisierten und zuletzt geöffneten Dateien und Ordner — sowohl aus Cloud-Diensten als auch aus dem Gerätespeicher. Immer wenn Sie eine Datei oder einen Ordner aus der Cloud öffnen, wird sie zur Liste Zuletzt geöffnet hinzugefügt. Sie können tief verschachtelte Ordner als Favoriten markieren, um schnell auf sie zugreifen zu können, ohne durch die Verzeichnisstruktur zu navigieren.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Online-Links und Schnellzugriff" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Dateien in dieser Anwendung

Dieser Abschnitt zeigt Dateien und Ordner, die im sandboxed-Dokumente-Verzeichnis von Evervideo gespeichert sind — alles, was Sie aus der Cloud heruntergeladen, über Wi-Fi Drive übertragen, durch die Finder-Dateifreigabe kopiert oder aus einer anderen App importiert haben.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Dateien in dieser Anwendung" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Dokumente-Ordner

Der Dokumente-Ordner ist die Wurzel von allem innerhalb von Dateien in dieser Anwendung. Sie können Unterordner erstellen, Dateien umbenennen, sie verschieben und beliebig gruppieren.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Lokale Dateien — Dokumente-Ordner" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Dateien auf diesem iPhone / iPad / Mac

Dieser Abschnitt zeigt Videos, die sich auf Ihrem Gerät, aber in anderen Anwendungen befinden. Sie können sie mit der Systemdateiauswahl in Evervideo importieren:

- Tippen Sie auf Dateien öffnen…, um bestimmte Dateien auszuwählen.
- Tippen Sie auf Ordner öffnen…, um einen ganzen Ordner auszuwählen.

Sie können auch Einen Ordner verbinden verwenden, um einen Link zu einem Ordner auf Ihrem Gerät mit Lese- / Schreibzugriff zu erstellen — ideal für die Arbeit mit einem Ordner auf iCloud Drive oder einem angeschlossenen USB-Laufwerk, ohne etwas zu kopieren.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Dateien auf diesem Gerät" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Spezielle Ordner

Im Dateien-Tab sehen Sie mehrere spezielle Ordner, die Evervideo automatisch erstellt und verwendet:

- **Downloads** — jede aus der Cloud heruntergeladene Datei erscheint hier standardmäßig. Anpassen in Einstellungen → Dateimanager → Heruntergeladene Dateien speichern in.
- **Player-Cache** — der Media-Player-Cache. Standardmäßig lädt der Player bevorstehende Videos für eine reibungslose Wiedergabe herunter. Sie können den Cache in den App-Einstellungen deaktivieren oder einfach diesen Ordner löschen.
- **iCloud** — Dateien in diesem Ordner werden über alle Ihre mit demselben iCloud-Konto verbundenen Geräte synchronisiert.
- **Offline-Ordner** — wenn Sie einen Ordner, eine Wiedergabeliste, ein Album oder ein Genre als offline verfügbar markieren, werden die Dateien in diesen Ordner heruntergeladen.

## Obere Symbolleiste

Die obere Symbolleiste, unter der Navigationsleiste, bietet mehrere Aktionen, die Sie mit einer Wischgeste nach unten ein- oder ausblenden können:

- **Suche** — eine Suche im aktuellen Ordner oder Abschnitt durchführen.
- **Wiedergabe fortsetzen** — wenn in den Einstellungen aktiviert, Player-Warteschlange und letzte Videoposition für den aktuellen Ordner wiederherstellen.
- **Alle abspielen** — den aktuellen Ordner und seine Unterordner scannen und Dateien zur Player-Warteschlange hinzufügen.
- **Alle zufällig abspielen** — wie Alle abspielen, aber vor dem Hinzufügen mischen.

## Ordner-Optionen

Wenn Sie einen Ordner öffnen, tippen Sie auf die **"..."**-Schaltfläche in der oberen rechten Ecke für diese Aktionen:

- **Auswählen** — Dateiauswahlmodus aktivieren.
- **Neuer Ordner** — einen neuen Ordner innerhalb des aktuellen Ordners erstellen.
- **Offline-Modus aktivieren** — Offline-Synchronisierung für den aktuellen Ordner einschalten. Neu online hinzugefügte Dateien werden automatisch heruntergeladen.
- **Dateien hochladen** — Dateien von Ihrem Gerät in den Online-Ordner hochladen.
- **Suche** — innerhalb des Ordners suchen.
- **Sortieren** — Dateien nach Name, Größe, Änderungsdatum oder Metadaten sortieren.
- **Raster- / Listenansicht** — zwischen Tabellenansicht und Miniaturansicht wechseln. Die Miniaturansicht zeigt große Video-Poster-Vorschauen.

## Auswahlmodus

Tippen Sie auf **"..."** in der oberen rechten Ecke und wählen Sie **Auswählen**, um den Auswahlmodus zu aktivieren. Neben jeder Datei und jedem Ordner erscheinen Kontrollkästchen. Tippen Sie, um ein oder mehrere Elemente auszuwählen, und führen Sie dann Batch-Aktionen aus: Als nächstes abspielen, Später abspielen, Zur Mediathek hinzufügen, Zu einer Wiedergabeliste hinzufügen, Kopieren, Hochladen, Verschieben, Umbenennen oder Löschen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Auswahlmodus im Dateimanager" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Wenn Sie verbundenen Cloud-Speicher lieber als schreibgeschützt behandeln möchten (um versehentliche Löschungen zu verhindern), aktivieren Sie Einstellungen → Dateimanager → Online-Dateien bearbeiten → Aus, um alle destruktiven Operationen aus der Benutzeroberfläche auszublenden.

## Dateiaktionen

Tippen Sie auf das **"..."**-Symbol neben dem Titel einer Datei, um ihr Aktionsmenü anzuzeigen:

- **Als nächstes abspielen** — die Datei oben in die Player-Warteschlange einfügen.
- **Später abspielen** — die Datei unten an die Player-Warteschlange anhängen.
- **Zur Mediathek hinzufügen** — die Datei in Ihre Mediathek integrieren, geordnet nach Album und Genre.
- **Zu einer Wiedergabeliste hinzufügen** — die Datei zu einer bestehenden Wiedergabeliste hinzufügen oder eine neue erstellen.
- **Tags bearbeiten** — den integrierten Tag-Editor öffnen, um Metadaten zu ändern. Bei Online-Dateien wird die Datei vorübergehend heruntergeladen, bearbeitet und dann nach Ihrer Bestätigung erneut hochgeladen.
- **Zu Favoriten hinzufügen** — die Datei zur Favoritenliste für schnellen Zugriff hinzufügen.
- **Herunterladen** — die Datei oder den Ordner für die Offline-Nutzung auf Ihr Gerät herunterladen.
- **Umbenennen** — die Datei direkt im Remote-Speicher umbenennen.
- **Verschieben** — die Datei in einen anderen Ordner in Ihrem Cloud-Speicher verschieben.
- **Zum Archiv hinzufügen** — die Datei in eine einzelne ZIP-Datei bündeln (Premium-Funktion).
- **Öffnen in** — die Datei über das System-Share-Sheet in eine andere kompatible App exportieren.
- **Löschen** — die Datei dauerhaft entfernen. **Diese Aktion kann nicht rückgängig gemacht werden.**

## Ordneraktionen

Für jeden Ordner in Ihrem Cloud-Speicher stehen viele Aktionen zur Verfügung, indem Sie auf das **"..."**-Symbol neben dem Ordnertitel tippen.

- **Alle abspielen** — die aktuelle Player-Warteschlange durch jedes Video im Ordner ersetzen.
- **Als nächstes abspielen / Später abspielen** — den gesamten Ordner zur Warteschlange hinzufügen.
- **Zur Mediathek hinzufügen** — den Inhalt des Ordners in Ihre Mediathek integrieren.
- **Zur Wiedergabeliste hinzufügen** — den gesamten Ordner zu einer Wiedergabeliste hinzufügen.
- **Zu Favoriten hinzufügen** — den Ordner zu Ihren Favoriten hinzufügen.
- **Offline-Modus aktivieren** — über einen einfachen Download hinaus überwacht dies kontinuierlich den Ordner auf neue Dateien und lädt diese automatisch herunter, sobald sie online erscheinen.
- **Herunterladen** — alle Inhalte des Ordners für den Offline-Zugriff auf Ihr Gerät herunterladen.
- **Umbenennen / Verschieben** — den Ordner im Remote-Speicher umbenennen oder verschieben.
- **Zum Archiv hinzufügen** — den Ordnerinhalt in eine ZIP-Datei bündeln (Premium-Funktion).
- **Löschen** — den Ordner und seinen Inhalt dauerhaft entfernen. **Diese Aktion kann nicht rückgängig gemacht werden.**

## Übertragungswarteschlange

In der oberen rechten Ecke des Dateien-Tabs befindet sich eine **Übertragungs**-Schaltfläche (ein Symbol mit drehenden Pfeilen). Tippen Sie darauf, um die Übertragungswarteschlange zu öffnen — eine Liste jedes aktiven Downloads und Uploads über alle Ihre Quellen hinweg, mit Echtzeit-Fortschritt, Geschwindigkeit und Restzeit pro Datei.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Dateiübertragungswarteschlange" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Sie können Übertragungen pausieren, fortsetzen, fehlgeschlagene wiederholen, Elemente neu anordnen, um bestimmte Downloads zu priorisieren, oder sie einzeln abbrechen. Sie können auch die Übertragungswarteschlangengeschwindigkeit (maximale parallele Aufgaben), den Netzwerktyp (nur Wi-Fi oder Wi-Fi + Mobilfunk) und Hintergrundübertragungen in Einstellungen → Dateimanager anpassen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Aktionen in der Dateiübertragungswarteschlange" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offline-Modus und synchronisierte Offline-Ordner

Der Offline-Modus ist eine praktische Funktion, mit der Sie Ihre Lieblingsvideos ansehen können, auch wenn Sie nicht mit dem Internet verbunden sind. Wenn Sie den Offline-Modus für einen Ordner, eine Wiedergabeliste, ein Album oder ein Genre aktivieren, werden alle Dateien innerhalb dieser Sammlung automatisch auf Ihr Gerät zur Offline-Wiedergabe heruntergeladen. Sie erscheinen im Abschnitt Offline-Ordner.

Wenn Sie dem Remote-Server neue Dateien hinzufügen, werden diese auch automatisch heruntergeladen — sodass Ihre Offline-Sammlung aktuell bleibt, ohne dass Sie etwas tun müssen. Um manuell neu zu synchronisieren, tippen Sie auf die drei Punkte in der oberen rechten Ecke eines Offline-Ordners und wählen Sie Synchronisieren.

Sie können das Synchronisierungsintervall in Einstellungen → Dateimanager → Synchronisierte Offline-Ordner → Zeitintervall anpassen.

Detaillierte Anweisungen sind [hier](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/) verfügbar.

## Personalisierung

In Einstellungen → Personalisierung können Sie konfigurieren, wie der Dateien-Tab präsentiert wird:

- **Dateien-Bildschirm-Stil** — Einfaches Menü (zeigt die Ordnerliste direkt) oder Gruppiertes Menü (gruppiert Inhalte nach Kategorie — Schnellzugriff, Spezielle Ordner, Cloud-Speicher usw.).
