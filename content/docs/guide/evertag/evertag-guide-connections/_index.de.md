---
title: "Verbindungen"
date: 2020-02-01
description: "Erfahren Sie, wie Sie Cloud-Speicher, NAS und Ihren Computer mit Evertag verbinden. Greifen Sie direkt von Cloud-Speicher, persönlichem NAS oder Mac/PC auf Audiodateien zu und bearbeiten Sie diese."
keywords: [
  "Evertag Cloud-Einrichtung", "iCloud mit Evertag verbinden", "SMB-Dateizugriff iOS",
  "WebDAV Audio-Tag-Editor", "NAS Metadaten-Bearbeitung", "Wi-Fi Drive Evertag",
  "Audiodateien auf iPhone übertragen", "Evertag iTunes File Sharing", "FLAC-Tags aus Cloud bearbeiten"
]
tags: ["anleitung", "evertag", "verbindungen"]
readingTime: 11
---


Auf diesem Bildschirm können Sie verschiedene Quellen mit Ihren Audiodateien verbinden. Sie können beliebte Cloud-Dienste wie Google Drive, Dropbox, OneDrive, iCloud und andere integrieren sowie Ihren Mac oder PC verbinden. Darüber hinaus haben Sie die Möglichkeit, Audiodateien auf Apple Time Capsule, WD Cloud Home oder einem NAS zu bearbeiten, das SMB oder WebDAV unterstützt.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Connections Screen" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Schnellzugriff

Am oberen Rand des Verbindungen-Bildschirms finden Sie eine **Schnellzugriff**-Liste. Jeder Cloud-Ordner, den Sie zu den Favoriten hinzufügen – auch einer, der mehrere Ebenen tief vergraben ist – erscheint hier, damit Sie ihn aufrufen können, ohne jedes Mal durch übergeordnete Ordner navigieren zu müssen.

## Mit Cloud-Speicher verbinden

- Öffnen Sie die Registerkarte „Verbindungen"
- Wählen Sie „Mit Cloud-Speicher verbinden" aus dem Menü
- Wählen Sie einen Cloud-Speicherdienst aus der Liste
- Geben Sie Ihre Anmeldedaten ein und tippen Sie auf „Fertig."

Wenn Probleme auftreten, überprüfen Sie Ihre Internetverbindung und Ihren Benutzernamen/Ihr Passwort.
In der Premium-Version der App können Sie eine unbegrenzte Anzahl von Diensten hinzufügen.

## Unterstützte Cloud-Speicherdienste

Derzeit unterstützt die Anwendung die beliebtesten Cloud-Speicherdienste: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘) sowie jeden SMB- oder WebDAV-Server.

## Sicherheit und Datenschutz

Wir verwenden nur offizielle SDKs und sichere Verbindungen für die Interaktion mit verbundenen Cloud-Diensten. Ihr Benutzername und Ihr Passwort sind für die Anwendung nicht zugänglich. Alle Anfragen der Anwendung an den Cloud-Dienst sind verschlüsselt.

Wenn Sie Ihren Benutzernamen und Ihr Passwort eingeben, zeigt die Anwendung die offizielle Autorisierungsseite des Cloud-Dienstanbieters an, und der gesamte Autorisierungsprozess findet außerhalb der Anwendung statt. Nach erfolgreicher Autorisierung sendet der Cloud-Dienstanbieter ein Auth-Token an die Anwendung, das für API-Aufrufe verwendet wird.

Ein Auth-Token ist ein digitaler Schlüssel, der Drittanbieter-Apps die Interaktion mit dem Cloud-Speicher ermöglicht. Das Auth-Token wird auf Ihrem Gerät in einem sicheren Systemspeicher namens Keychain gespeichert. Sie können Ihre Dateien vom verbundenen Cloud-Dienst auf das Gerät herunterladen; diese Dateien werden im Verzeichnis „Documents" der App abgelegt. Sie können diese Dateien jederzeit mit dem integrierten Dateimanager entfernen.

Die Anwendung gibt keine Informationen aus dem verbundenen Cloud-Konto weiter. Sie können den Zugriff auf Ihr Cloud-Konto jederzeit widerrufen, indem Sie die Kontoeinstellungsseite in Ihrem Webbrowser öffnen.

## Auth-Token widerrufen

Melden Sie sich in einem Webbrowser bei Ihrem Konto an und navigieren Sie zur Einstellungsseite. Dort finden Sie alle mit Ihrem Cloud-Konto verbundenen Drittanbieter-Apps und können diese entfernen, wenn Sie die Anwendung nicht mehr verwenden möchten. Detaillierte Anweisungen sind [hier](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) verfügbar.

Sie können auch die verbundenen Cloud-Konten in der Anwendung trennen, und das Auth-Token wird ebenfalls von Ihrem Gerät entfernt. Wenn Sie die Anwendung von Ihrem Gerät entfernen, werden alle heruntergeladenen Daten und Zugriffstoken ebenfalls entfernt.

## Cloud-Speicher trennen oder Konfiguration ändern

- Auf Cloud-Speicheroptionen zugreifen: Suchen Sie zunächst den Cloud-Speicher, den Sie in der App-Oberfläche verwalten möchten.
- Auf die Schaltfläche „..." tippen: Neben dem Diensttitel sehen Sie eine „..."-Schaltfläche. Tippen Sie darauf, um auf weitere Optionen zuzugreifen.
  - **Umbenennen**: Wenn Sie den Namen des Cloud-Dienstes in Ihrer Liste ändern möchten, wählen Sie „Umbenennen."
  - **Einstellungen**: Um die Konfiguration oder Authentifizierungsdaten des Cloud-Dienstes zu ändern, wählen Sie „Einstellungen." Manchmal müssen Sie den verbundenen Cloud-Dienst erneut autorisieren, wenn das Autorisierungstoken abgelaufen ist.
  - **Trennen**: Wenn Sie die Verbindung zwischen der App und dem Cloud-Dienst vollständig trennen möchten, wählen Sie „Trennen." Beachten Sie, dass dadurch alle mit diesem Cloud-Dienst verknüpften Songs aus der Musikbibliothek Ihrer App entfernt werden, diese aber auf dem Server verbleiben.

## Mit Computer oder NAS verbinden

Sie können auch Ihren Computer, ein persönliches NAS oder andere Netzwerkgeräte über das SMB-, DLNA- oder WebDAV-Protokoll verbinden.

## Mit Computer über SMB verbinden

- Tippen Sie auf „Mit Cloud-Speicher verbinden" → SMB.
- Geben Sie die IP-Adresse des Computers und den Namen des freigegebenen Ordners im URL-Feld im Format smb://computer-ip-adresse/freigegebener-ordner-name ein
- Wählen Sie die Protokollversion: Auto, SMB1, SMB2
- Geben Sie Benutzername und Passwort ein (falls erforderlich)
- Tippen Sie auf „Fertig."

Wenn die Verbindung erfolgreich ist, sehen Sie den verbundenen Speicher im Abschnitt „Cloud-Speicher."
Eine vollständige Anleitung zum Verbinden Ihres Mac oder PCs über SMB ist [hier](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) verfügbar.

## Mit NAS über WebDAV verbinden

Alle Schritte sind dieselben, außer für das URL-Feld.
Die URL sollte im Format http://server-name oder https://server-name angegeben werden, wenn der Server SSL unterstützt.
Eine vollständige Anleitung zum Verbinden eines NAS über das WebDAV-Protokoll ist [hier](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) verfügbar.

## Verfügbare Geräte

Dieser Abschnitt zeigt alle Geräte in Ihrem lokalen Netzwerk an, mit denen Sie sich über die Anwendung verbinden können.
Gehen Sie folgendermaßen vor, um eine Verbindung mit einem Gerät herzustellen:

- Öffnen Sie die App und gehen Sie zum Abschnitt „Verfügbare Geräte."
- Tippen Sie auf das Gerät, mit dem Sie sich verbinden möchten, in der Liste.
- Geben Sie bei Bedarf Ihre Anmeldedaten ein, um die Verbindung abzuschließen.

## Wi-Fi Drive

Wi-Fi Drive ist eine praktische Technologie, die drahtlose Dateiübertragungen von Ihrem Computer auf Ihr iOS-Gerät über einen Desktop-Browser ermöglicht.
Um diese Funktion effektiv nutzen zu können, stellen Sie sicher, dass Ihr Gerät und Ihr Computer mit demselben Wi-Fi-Netzwerk verbunden sind.
Hier finden Sie eine Schritt-für-Schritt-Anleitung zur Verwendung von Wi-Fi Drive.

## Wi-Fi Drive aktivieren

- Öffnen Sie die Anwendung und gehen Sie zur Registerkarte „Verbindungen."
- Wählen Sie „Über Wi-Fi verbinden," um zum Wi-Fi Drive-Hauptbildschirm zu gelangen.
- Tippen Sie auf „Wi-Fi Drive starten," um Wi-Fi Drive zu aktivieren.

## Auf Wi-Fi Drive von Ihrem Computer aus zugreifen

- Öffnen Sie auf Ihrem Computer (Desktop oder Laptop) einen Webbrowser (z. B. Chrome, Firefox oder Safari).
- Geben Sie in der Adressleiste des Browsers die von der Anwendung bereitgestellte URL ein.

## Dateien drahtlos übertragen

Sobald die Ihrer iOS-Gerät entsprechende Webseite im Browser geöffnet wird, können Sie Dateien ganz einfach per Drag & Drop von Ihrem Computer auf die Webseite ziehen.
Die Dateien, die Sie ziehen und ablegen, werden auf Ihr iOS-Gerät übertragen und sind in der Anwendung zugänglich.

Detaillierte Anweisungen zur drahtlosen Dateiübertragung mit Wi-Fi Drive sind [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) verfügbar.

## iTunes File Sharing

iTunes File Sharing ist eine weitere Technologie, mit der Sie Dateien mithilfe der Finder-App auf Ihrem Mac und einem Lightning-Kabel von einem Computer auf ein Gerät übertragen können.
- Verbinden Sie das Gerät einfach über ein Kabel mit dem Computer und starten Sie die Finder-App auf Ihrem Mac.
- Öffnen Sie „Standorte" → „Ihr verbundenes Gerät" → „Dateien" → und suchen Sie die aktuelle App.
- Tippen Sie auf das App-Symbol, um alle freigegebenen Ordner anzuzeigen.
- Kopieren Sie Dateien per Drag & Drop vom Computer in den freigegebenen Ordner auf dem Gerät.

Detaillierte Anweisungen zur Verwendung von iTunes File Sharing sind [hier](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) verfügbar.

## USB-Flashkarte verbinden

Wenn Sie eine SD-Karte oder einen USB-Stick haben, können Sie diese über einen Lightning- oder USB-C-Kartenleser auf iPhone/iPad verbinden oder direkt an einen Mac anschließen. Die App unterstützt derzeit Apple Certified-Kartenleser. Wir haben detaillierte Anweisungen zum Verbinden einer USB-Flashkarte mit Ihrem iPhone oder iPad und zur Verwaltung der darauf befindlichen Dateien [hier](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Verbundene Laufwerke erscheinen im Abschnitt **Verbundene Zubehörteile** des Verbindungen-Bildschirms.

## Dateimanager

Sobald Sie einen Cloud-Speicherdienst verbunden haben, tippen Sie auf dessen Symbol, um alle verfügbaren Dateien und Ordner anzuzeigen. Sie können den integrierten Dateimanager verwenden, um mit diesen Dateien zu arbeiten – herunterladen, umbenennen, verschieben und mehr. Wenn Sie einen Download starten, erscheint die Datei in der Übertragungswarteschlange. Um die Übertragungswarteschlange anzuzeigen, gehen Sie zur Registerkarte „Lokale Dateien" und tippen Sie auf die sich drehenden Pfeile in der oberen linken Ecke. Alle heruntergeladenen Dateien und Ordner sind im Abschnitt „Lokale Dateien" verfügbar.

## Obere Symbolleiste

Die obere Symbolleiste, die sich praktischerweise unter der Navigationsleiste befindet, bietet mehrere nützliche Aktionen für einfachen Zugriff. Sie können diese Symbolleiste durch eine einfache Wischgeste nach unten ein- oder ausblenden. Hier sind die verfügbaren Aktionen:

- **Suche**: Mit dieser Option können Sie eine schnelle Suche im aktuellen Verzeichnis durchführen, was es mühelos macht, bestimmte Dateien oder Ordner zu finden.

## Ordneroptionen

Wenn Sie einen Ordner in der App öffnen, finden Sie eine praktische Reihe von Aktionen, auf die Sie durch Tippen auf die Schaltfläche „..." in der oberen rechten Ecke des Bildschirms zugreifen können.
Hier ist eine Übersicht dieser Aktionen:

- **Auswählen**: Aktivieren Sie den Dateiauswahlmodus. In diesem Modus können Sie eine oder mehrere Dateien im Ordner auswählen, was es einfach macht, Aktionen auf ausgewählte Elemente durchzuführen.
- **Neuer Ordner**: Erstellen Sie einen neuen Ordner im aktuellen Ordner. Mit dieser Funktion können Sie Ihre Dateien organisieren und Ihre Bibliothek gut strukturiert halten.
- **Dateien hochladen**: Laden Sie Dateien von Ihrem Gerät in den Online-Ordner hoch. Mit dieser Aktion können Sie Dateien in die Cloud oder auf einen Server übertragen und von überall darauf zugreifen.
- **Suche**: Suchen Sie nach bestimmten Dateien im aktuellen Ordner. Dies ist besonders nützlich, um bestimmte Elemente in einer großen Sammlung schnell zu finden.
- **Sortieren**: Sortieren Sie Dateien im Ordner nach Kriterien wie Name, Größe oder Bearbeitungsdatum. Der Standard-Sortiermodus spiegelt in der Regel die Sortierreihenfolge auf dem Server wider, Sie können ihn jedoch nach Ihren Wünschen ändern.
- **Raster-/Listenansicht**: Wechseln Sie zwischen zwei Ansichtsmodi: Tabellenansicht und Miniaturansicht. Die Tabellenansicht zeigt Dateien in einer Liste, während die Miniaturansicht visuelle Darstellungen der Dateien anzeigt, was die Identifizierung von Inhalten auf einen Blick erleichtert.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloud Folder Sort" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Online-Dateien bearbeiten

Wenn Sie mehrere Dateien in Ihrem Cloud-Speicher in dieser App verwalten müssen, können Sie den Auswahlmodus verwenden, um Ihre Aktionen zu optimieren. Befolgen Sie diese Schritte für eine effektive Dateiverwaltung:

- **Auswahlmodus aktivieren**: Öffnen Sie die App auf Ihrem Gerät und navigieren Sie zum Abschnitt mit Ihrem Cloud-Speicher. Suchen Sie in der oberen rechten Ecke nach der Schaltfläche „..." (Auslassungspunkte). Tippen Sie darauf und wählen Sie den Menüpunkt „Auswählen," um den Auswahlmodus zu aktivieren.
- **Dateien auswählen**: Sie sehen Kontrollkästchen neben jeder aufgelisteten Datei oder jedem Ordner. Wählen Sie eine oder mehrere Dateien oder Ordner aus, indem Sie einfach auf die Kontrollkästchen neben ihnen tippen.
- **Verschiedene Aktionen ausführen**: Sobald Sie die Dateien oder Ordner ausgewählt haben, die Sie verwalten möchten, haben Sie Zugriff auf mehrere auf Ihre Bedürfnisse zugeschnittene Aktionen:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Select" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Dateiaktionen

Neben dem Titel der Datei sehen Sie ein Auslassungszeichen „..." (drei Punkte) – das ist das Aktionsmenü.
Tippen Sie darauf, um eine Liste verfügbarer Aktionen anzuzeigen:

- **Audio-Tags bearbeiten**: Durch Auswahl dieser Option können Sie auf den integrierten Tag-Editor zugreifen, mit dem Sie Audio-Tags für die ausgewählte Datei ändern können. Die Datei wird vorübergehend in ein temporäres Verzeichnis heruntergeladen und nach Bestätigung der Änderungen wieder in den Speicher hochgeladen.
- **Zu Favoriten hinzufügen**: Diese Aktion fügt die Datei zu Ihrer Liste der Favoritendateien für schnellen und komfortablen Zugriff hinzu.
- **Herunterladen**: Wählen Sie diese Aktion, um die Datei oder den Ordner auf Ihr Gerät herunterzuladen und sie für die Offline-Nutzung zugänglich zu machen.
- **Umbenennen**: Mit dieser Option können Sie die Datei direkt auf dem Remote-Speicher umbenennen, was eine individuelle Dateinamenvergabe ermöglicht.
- **Verschieben**: Wählen Sie diese Aktion, um die Datei in einen anderen Ordner in Ihrem Cloud-Speicher zu verschieben, was bei der Aufrechterhaltung einer organisierten Dateistruktur hilft.
- **Öffnen in**: Verwenden Sie diese Aktion, um die Datei in eine andere kompatible App zu exportieren. Die Datei wird auf Ihr Gerät heruntergeladen, und anschließend wird das Teilen-Dialogfeld für weitere Freigabe oder Interaktion angezeigt.
- **Löschen**: Seien Sie vorsichtig mit dieser Aktion, da sie die Datei dauerhaft aus Ihrem Cloud-Speicher entfernt. **Diese Löschung kann nicht rückgängig gemacht werden**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Options" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Wenn die Aktionsliste den verfügbaren Bildschirmbereich überschreitet, scrollen Sie einfach nach unten im Aktionsmenü, um weitere Optionen anzuzeigen.

## Ordneraktionen

Für jeden Ordner in Ihrem Cloud-Speicher stehen verschiedene Aktionen zur Verfügung. Um auf diese Optionen zuzugreifen, tippen Sie einfach auf das Auslassungssymbol „..." neben dem Ordnertitel. Wenn nicht alle Aktionen sichtbar sind, scrollen Sie nach unten, um weitere anzuzeigen. Hier sind die verfügbaren Aktionen:

- **Zu Favoriten hinzufügen**: Verwenden Sie diese Aktion, um den Ordner zu Ihrer Liste der Favoritendateien für schnellen und komfortablen Zugriff hinzuzufügen.
- **Herunterladen**: Laden Sie alle Inhalte des Ordners auf Ihr Gerät für den Offline-Zugriff herunter.
- **Umbenennen**: Benennen Sie den Ordner direkt auf dem Remote-Speicher um.
- **Verschieben**: Verschieben Sie den Ordner an einen anderen Ort in Ihrem Cloud-Speicher.
- **Löschen**: Seien Sie vorsichtig mit dieser Aktion, da sie den Ordner und seinen Inhalt dauerhaft aus Ihrem Cloud-Speicher entfernt. **Diese Aktion kann nicht rückgängig gemacht werden**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Folder Options" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
