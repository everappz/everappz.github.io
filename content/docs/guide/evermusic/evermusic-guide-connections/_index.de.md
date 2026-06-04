---
title: "Verbindungen"
date: 2020-01-01
description: "Erfahre, wie du Cloud-Dienste, Computer und NAS-Geräte verbindest und Musikdateien mit Evermusic verwaltest. Schritt-für-Schritt-Anleitung zu Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes-Dateifreigabe und mehr."
keywords: [
  "Evermusic", "Cloud-Musikplayer", "NAS-Streaming", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes-Dateifreigabe",
  "Cloud-Speicher verbinden", "Musikübertragung iPhone", "Dateimanager iOS"
]
tags: ["evermusic", "Anleitung", "Verbindungen"]
readingTime: 11
---


Auf dem Verbindungen-Bildschirm kannst du jede Quelle verbinden, die deine Musik enthält — beliebte Cloud-Dienste, selbst gehostete Medienserver, deinen Mac oder PC, ein persönliches NAS, Apple Time Capsule, WD My Cloud Home, sogar ein USB-Flash-Laufwerk — und alles über eine einheitliche Oberfläche nutzen. Verbindungen ist auch der Ort, wo du Schnellzugriff auf tief verschachtelte Cloud-Ordner einrichtest und Last.fm für Scrobbling authentifizierst.

Der Bildschirm ist in klar beschriftete Bereiche unterteilt, sodass er von einem einzelnen iCloud Drive-Konto bis zu einer über mehrere Clouds und NAS-Geräte verteilten Bibliothek skaliert: Schnellzugriff oben (deine bevorzugten Cloud-Ordner), Cloud-Speicher (die hinzugefügten Konten), Lokales Netzwerk (Bonjour-erkannte Geräte), Computer (Wi-Fi Drive, iTunes-Dateifreigabe, SMB), Externe Zubehörteile (verbundene USB-Flash-Laufwerke) und Andere Dienste (Last.fm und ähnliche).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Verbindungen-Bildschirm" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Mit Cloud-Speicher verbinden

- Öffne die Verbindungen-Registerkarte.
- Wähle 'Mit Cloud-Speicher verbinden' aus dem Menü.
- Wähle einen Cloud-Speicherdienst aus der Liste.
- Melde dich auf der offiziellen Autorisierungsseite des Anbieters an (Evermusic sieht dein Passwort nie).
- Tippe auf 'Fertig'.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cloud-Speicher-Anbieter-Auswahl" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Wenn Probleme auftreten, überprüfe deine Internetverbindung und Anmeldedaten und stelle sicher, dass die Zwei-Faktor-Authentifizierung für diesen Dienst korrekt konfiguriert ist.  
In der Premium-Version der App kannst du eine unbegrenzte Anzahl von Diensten hinzufügen. Kostenlose Nutzer können jeweils nur ein Cloud-Konto verbinden.

## Unterstützte Cloud-Speicherdienste

Evermusic unterstützt das gesamte Spektrum populärer Cloud- und selbst gehosteter Dienste. Kostenlose Nutzer erhalten denselben Anbieter-Katalog, jedoch mit der Ein-Konto-Beschränkung; Premium entsperrt unbegrenzte Konten und hebt die meisten anderen Einschränkungen auf.

- **Persönliche Cloud-Konten:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Selbst gehostete Server und Medienbibliotheken:** Plex · Jellyfin · Emby · Subsonic (und jeder Subsonic-kompatible Server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (und Owncloud über die gemeinsame API) · Synology Drive · QNAP.
- **NAS und Dateifreigabeprotokolle:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (Passwort oder Public-Key-Authentifizierung), NFS und DLNA (nur Lesezugriff — Wiedergabe und Download).
- **S3-kompatible Objektspeicher:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage oder beliebiger S3-API-Endpunkt.
- **Lokale Netzwerkerkennung:** Der Bereich 'Verfügbare Geräte' listet automatisch alle Geräte in deinem Wi-Fi auf, die sich über Bonjour / mDNS ankündigen — Plex, Jellyfin, Emby-Server, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, AirPort-Router mit angeschlossenen Laufwerken usw.

## Sicherheit und Datenschutz

Wir verwenden nur das offizielle SDK und sichere Verbindungen zur Interaktion mit verbundenen Cloud-Diensten. Dein Login und Passwort sind der App nicht zugänglich. Alle Anfragen der App an den Cloud-Dienst sind verschlüsselt.

Wenn du dein Login und Passwort eingibst, zeigt die App die offizielle Autorisierungsseite des Cloud-Dienstanbieters an, und der gesamte Autorisierungsprozess findet außerhalb der App statt. Der Cloud-Dienstanbieter sendet nach erfolgreicher Autorisierung ein Auth-Token an die App, das für API-Aufrufe verwendet wird.

Das Auth-Token ist ein digitaler Schlüssel, der Drittanwendungen die Interaktion mit Cloud-Speicher ermöglicht. Das Auth-Token wird auf deinem Gerät in einem sicheren Systemspeicher namens Keychain gespeichert. Du kannst Dateien vom verbundenen Cloud-Dienst auf dein Gerät herunterladen, und diese Dateien werden im Verzeichnis 'Dokumente' der App abgelegt. Du kannst diese Dateien jederzeit mit dem integrierten Dateimanager entfernen.

Die App teilt keine Informationen aus dem verbundenen Cloud-Konto. Du kannst den Zugriff auf dein Cloud-Konto jederzeit widerrufen, indem du die Kontoeinstellungsseite in deinem Webbrowser öffnest.

## Auth-Token ablehnen

Melde dich in deinem Webbrowser in deinem Konto an und gehe zur Einstellungsseite. Dort findest du alle Drittanwendungen, die mit deinem Cloud-Konto verbunden sind, und kannst jede davon entfernen, wenn du diese Anwendung nicht mehr verwenden möchtest. Detaillierte Anleitungen sind [hier](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) verfügbar.

Du kannst auch die verbundenen Cloud-Konten in der App trennen, wodurch das Auth-Token auch von deinem Gerät entfernt wird. Wenn du die App von deinem Gerät entfernst, werden alle heruntergeladenen Daten und Zugriffstoken ebenfalls entfernt.

## Cloud-Speicher trennen oder Konfiguration ändern

- Greife auf Cloud-Speicher-Optionen zu: Suche zunächst den Cloud-Speicher, den du in der App-Oberfläche verwalten möchtest.
- Tippe auf die Schaltfläche '...': Neben dem Diensttitel siehst du eine '...'-Schaltfläche. Tippe darauf, um weitere Optionen aufzurufen.
  - **Umbenennen**: Wenn du den Namen des Cloud-Dienstes in deiner Liste ändern möchtest, wähle 'Umbenennen'.
  - **Einstellungen**: Um die Konfiguration oder Authentifizierungsdaten für den Cloud-Dienst zu ändern, wähle 'Einstellungen'. Manchmal musst du den verbundenen Cloud-Dienst neu autorisieren, wenn das Autorisierungstoken abgelaufen ist.
  - **Trennen**: Wenn du die Verbindung zwischen der App und dem Cloud-Dienst vollständig trennen möchtest, wähle 'Trennen'. Beachte, dass dadurch alle Songs, die mit diesem Cloud-Dienst verknüpft sind, aus der Musikbibliothek der App entfernt werden, sie bleiben jedoch auf dem Server.

{{< cards cols="1">}}
  {{< card title="" subtitle="Weitere Aktionen für verbundenen Cloud-Speicher" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Mit Computer oder NAS verbinden

Du kannst auch deinen Computer, ein persönliches NAS oder andere Netzwerkgeräte über SMB, DLNA oder WebDAV verbinden.

## Computer über SMB verbinden

- Tippe auf 'Mit Cloud-Speicher verbinden' → SMB.
- Gib die IP-Adresse des Computers und den Namen des freigegebenen Ordners im URL-Feld im Format smb://computer-ip-adresse/freigegebener-ordnername ein.
- Wähle die Protokollversion: Auto, SMB1, SMB2.
- Gib Login und Passwort ein (falls erforderlich).
- Tippe auf 'Fertig'.

Wenn die Verbindung erfolgreich ist, siehst du den verbundenen Speicher im Bereich 'Cloud-Speicher'.  
Eine vollständige Anleitung zur Verbindung deines Mac oder PC über SMB ist [hier](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) verfügbar.

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB-Verbindungseinstellungen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## NAS über WebDAV verbinden

Alle Schritte sind gleich, außer im URL-Feld.  
Die URL sollte im Format http://servername oder https://servername angegeben werden, wenn der Server SSL unterstützt.
Eine vollständige Anleitung zur Verbindung von NAS über das WebDAV-Protokoll ist [hier](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) verfügbar.

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV-Verbindungseinstellungen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Computer oder NAS über DLNA verbinden

Du kannst eine Musikbibliothek auf deinem Windows-PC oder persönlichen NAS auch über das DLNA-Protokoll freigeben und wie [hier](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) beschrieben in der App aufrufen. DLNA ist ein beliebtes und weit verbreitetes Protokoll, ermöglicht jedoch nur das Abspielen oder Herunterladen von Musik. Du kannst keine Dateien hochladen oder neue Ordner auf dem Server erstellen.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA-Verbindungseinstellungen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Verfügbare Geräte

Dieser Bereich zeigt alle Geräte in deinem lokalen Netzwerk an, mit denen du dich über die App verbinden kannst.  
Um eine Verbindung zu einem Gerät herzustellen, gehe wie folgt vor:

- Öffne die App und gehe zum Bereich 'Verfügbare Geräte'.
- Tippe auf das Gerät, mit dem du dich verbinden möchtest.
- Gib bei Bedarf deine Anmeldedaten ein, um die Verbindung abzuschließen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Verfügbare Geräte im lokalen Netzwerk" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive ist eine praktische Technologie, die kabellose Dateiübertragungen von deinem Computer auf dein iOS-Gerät über einen Desktop-Browser ermöglicht.  
Um diese Funktion effektiv zu nutzen, stelle sicher, dass dein Gerät und dein Computer mit demselben Wi-Fi-Netzwerk verbunden sind.  
Hier ist eine Schritt-für-Schritt-Anleitung zur Nutzung von Wi-Fi Drive.

## Wi-Fi Drive aktivieren

- Öffne die App und gehe zur Registerkarte 'Verbindungen'.
- Wähle 'Über Wi-Fi verbinden', um den Wi-Fi Drive-Hauptbildschirm aufzurufen.
- Tippe auf 'Wi-Fi Drive starten', um Wi-Fi Drive zu aktivieren.

## Wi-Fi Drive auf deinem Computer aufrufen

- Öffne auf deinem Computer (Desktop oder Laptop) einen Webbrowser (z. B. Chrome, Firefox oder Safari).
- Gib in der Adressleiste des Browsers die von der App angegebene URL ein.

## Dateien kabellos übertragen

Sobald die Webseite deines iOS-Geräts im Browser geöffnet wird, kannst du Dateien von deinem Computer einfach per Drag-and-Drop auf die Webseite ziehen.  
Die Dateien, die du hinzifügst, werden auf dein iOS-Gerät übertragen und sind innerhalb der App zugänglich.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive Server-Einstellungen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Detaillierte Anleitungen zur kabellosen Dateiübertragung mit WiFi-Drive sind [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) verfügbar.

## iTunes-Dateifreigabe

iTunes-Dateifreigabe ist eine weitere Technologie, mit der du Dateien vom Computer auf dein Gerät über die Finder-App auf deinem Mac und ein Lightning-Kabel übertragen kannst.  
- Verbinde ein Gerät über ein Kabel mit dem Computer und starte die Finder-App auf deinem Mac.
- Öffne 'Standorte' → 'Dein verbundenes Gerät' → 'Dateien' → und finde die Evermusic-App.
- Tippe auf das App-Symbol, um alle freigegebenen Ordner anzuzeigen.
- Kopiere Dateien vom Computer in den freigegebenen Ordner auf dem Gerät per Drag-and-Drop.

Detaillierte Anleitungen zur Nutzung der iTunes-Dateifreigabe sind [hier](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) verfügbar.

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder-Dateifreigabe auf Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## USB-Flashkarte verbinden

Wenn du eine SD-Karte hast, kannst du sie mit einem Lightning-Kartenleser verbinden. Die App unterstützt derzeit Apple Certified Kartenleser und iXpand Flash Drives. Wenn du ein iXpand Flash Drive hast — stecke es in den Lightning-Anschluss und öffne die App. Du siehst die Meldung 'Externes Gerät verbunden' und Geräteinformationen. Tippe einfach auf das Flash-Drive-Symbol, um den Musikordner aufzurufen, und tippe auf eine Audiodatei, um die Wiedergabe zu starten. Detaillierte Anleitungen zum Verbinden einer USB-Flashkarte mit dem iPhone und zum Hören von Musik oder Verwalten von Dateien darauf sind [hier](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it) verfügbar.

## Dateimanager

Sobald du einen Cloud-Speicherdienst verbunden hast, tippe auf sein Symbol, um alle verfügbaren Dateien und Ordner anzuzeigen. Du kannst den integrierten Dateimanager verwenden, um mit diesen Dateien zu arbeiten — herunterladen, umbenennen, verschieben und mehr. Wenn du einen Download startest, erscheint die Datei in der Übertragungswarteschlange. Um die Übertragungswarteschlange anzuzeigen, gehe zur Registerkarte 'Lokale Dateien' und tippe auf das drehende Pfeile-Symbol in der oberen linken Ecke. Alle heruntergeladenen Dateien und Ordner sind im Bereich 'Lokale Dateien' verfügbar.

## Obere Symbolleiste

Die obere Symbolleiste, die sich unter der Navigationsleiste befindet, bietet mehrere nützliche Aktionen für den einfachen Zugriff. Du kannst diese Symbolleiste durch eine einfache Wisch-nach-unten-Geste ein- oder ausblenden. Folgende Aktionen sind verfügbar:

- **Suchen**: Mit dieser Option kannst du eine schnelle Suche im aktuellen Verzeichnis durchführen, um bestimmte Dateien oder Ordner mühelos zu finden.
- **Wiedergabe fortsetzen**: Wenn in den App-Einstellungen aktiviert, stellt diese Funktion die Audio-Player-Warteschlange und die letzte Medienposition für den aktuellen Ordner wieder her. So kannst du nahtlos da weitermachen, wo du aufgehört hast.
- **Alle abspielen**: Mit dieser Aktion scannt die App den aktuellen Ordner und seine Unterordner und fügt alle gefundenen Audiodateien einer neuen Player-Warteschlange hinzu. Nützlich, wenn du alle Musik in einem bestimmten Verzeichnis abspielen möchtest.
- **Alle zufällig abspielen**: Ähnlich wie 'Alle abspielen', aber die Dateien werden vor dem Hinzufügen zur Audio-Player-Warteschlange gemischt. Eine großartige Möglichkeit, deine Musik in zufälliger Reihenfolge zu genießen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obere Symbolleiste in einem Cloud-Ordner" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Ordneroptionen

Wenn du einen Ordner in der App öffnest, findest du eine Reihe von Aktionen, die über die Schaltfläche '...' oben rechts auf dem Bildschirm zugänglich sind.  
Hier ist eine Übersicht dieser Aktionen:

- **Auswählen**: Aktiviere den Dateiauswahlmodus. Dieser Modus ermöglicht es dir, eine oder mehrere Dateien im Ordner auszuwählen.
- **Neuer Ordner**: Erstelle einen neuen Ordner im aktuellen Ordner. Mit dieser Funktion kannst du deine Dateien organisieren und deine Bibliothek strukturiert halten.
- **Offline-Modus aktivieren**: Schalte den Offline-Modus für den aktuellen Ordner ein. Der Offline-Modus geht über einfaches Herunterladen hinaus; er überwacht den Ordner aktiv auf Änderungen. Wenn du neue Dateien online zum Ordner hinzufügst, lädt die App diese Dateien automatisch auf dein Gerät herunter.
- **Dateien hochladen**: Lade Dateien von deinem Gerät in den Online-Ordner hoch.
- **Suchen**: Suche nach bestimmten Dateien im aktuellen Ordner.
- **Sortieren**: Sortiere Dateien im Ordner nach Kriterien wie Name, Größe oder Änderungsdatum.
- **Raster-/Listenansicht**: Wechsle zwischen zwei Anzeigemodi: Tabellenansicht und Miniaturansicht.

{{< cards cols="1">}}
  {{< card title="" subtitle="Weitere Aktionen für aktuellen Ordner" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Online-Dateien bearbeiten

Wenn du mehrere Dateien in deinem Cloud-Speicher in Evermusic verwalten möchtest, kannst du den Auswahlmodus verwenden. Gehe wie folgt vor:

- **Auswahlmodus aktivieren**: Öffne die App und navigiere zum Bereich mit deinem Cloud-Speicher. Tippe auf die '...' (Auslassungspunkte)-Schaltfläche oben rechts und wähle 'Auswählen', um den Auswahlmodus zu aktivieren.
- **Dateien auswählen**: Neben jeder Datei oder jedem Ordner erscheinen Kontrollkästchen. Wähle eine oder mehrere Dateien oder Ordner aus, indem du auf die Kontrollkästchen tippst.
- **Verschiedene Aktionen ausführen**: Sobald du die Dateien oder Ordner ausgewählt hast, die du verwalten möchtest, stehen dir verschiedene Aktionen zur Verfügung.

{{< cards cols="1">}}
  {{< card title="" subtitle="Auswahlmodus für Online-Dateien" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Dateiaktionen

Neben dem Dateititel siehst du das Auslassungssymbol '...' (drei Punkte) — dies ist das Aktionsmenü.  
Tippe darauf, um eine Liste der verfügbaren Aktionen anzuzeigen:

- **Als nächstes abspielen**: Fügt die ausgewählte Datei an die Spitze deiner Player-Warteschlange ein, sodass sie unmittelbar nach dem aktuell abgespielten Element abgespielt wird.
- **Später abspielen**: Diese Option fügt die Datei am Ende deiner Player-Warteschlange hinzu.
- **Zur Musikbibliothek hinzufügen**: Mit dieser Aktion kannst du die Datei in deine Musikbibliothek aufnehmen, ordentlich nach Künstler, Album, Genre oder Komponist organisiert.
- **Zu einer Wiedergabeliste hinzufügen**: Mit dieser Aktion kannst du die Datei zu einer vorhandenen Wiedergabeliste hinzufügen oder eine neue erstellen.
- **Audio-Tags bearbeiten**: Mit dieser Option kannst du auf den integrierten Tags-Editor von Evermusic zugreifen. Die Datei wird vorübergehend in ein temporäres Verzeichnis heruntergeladen und nach der Bestätigung der Änderungen wieder in den Speicher hochgeladen.
- **Zu Favoriten hinzufügen**: Diese Aktion fügt die Datei zur Liste deiner Favoriten-Dateien hinzu.
- **Herunterladen**: Wähle diese Aktion, um die Datei oder den Ordner auf dein Gerät herunterzuladen.
- **Umbenennen**: Mit dieser Option kannst du die Datei direkt im Remote-Speicher umbenennen.
- **Verschieben**: Wähle diese Aktion, um die Datei in einen anderen Ordner in deinem Cloud-Speicher zu verlagern.
- **Öffnen in**: Mit dieser Aktion kannst du die Datei in eine andere kompatible App exportieren.
- **Löschen**: Sei bei dieser Aktion vorsichtig, da sie die Datei dauerhaft aus deinem Cloud-Speicher entfernt. Dieser Vorgang kann nicht rückgängig gemacht werden.

{{< cards cols="1">}}
  {{< card title="" subtitle="Weitere Aktionen für eine einzelne Datei" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Wenn die Liste der Aktionen den verfügbaren Bildschirmplatz überschreitet, scrolle einfach im Aktionsmenü nach unten.

## Ordneraktionen

Für jeden Ordner in deinem Cloud-Speicher stehen verschiedene Aktionen zur Verfügung. Tippe auf das Auslassungssymbol '...' neben dem Ordnertitel. Falls du nicht alle Aktionen siehst, scrolle nach unten. Folgende Aktionen sind verfügbar:

- **Alle abspielen**: Ersetze die aktuelle Player-Warteschlange durch alle Elemente aus dem ausgewählten Ordner.
- **Als nächstes abspielen**: Füge den gesamten Ordner an die Spitze der Player-Warteschlange hinzu.
- **Später abspielen**: Hänge den Ordnerinhalt am Ende der Player-Warteschlange an.
- **Zur Musikbibliothek hinzufügen**: Diese Aktion integriert den Inhalt des Ordners nahtlos in deine Musikbibliothek.
- **Zur Wiedergabeliste hinzufügen**: Du kannst den gesamten Ordner in eine Wiedergabeliste aufnehmen, wobei der Ordnername automatisch zugewiesen wird.
- **Zu Favoriten hinzufügen**: Füge den Ordner zur Liste deiner Favoriten-Dateien hinzu.
- **Offline-Modus aktivieren**: Durch Aktivieren des Offline-Modus für einen ausgewählten Ordner scannt die App kontinuierlich nach Änderungen und lädt neu hinzugefügte Dateien automatisch herunter.
- **Herunterladen**: Lade alle Inhalte des Ordners für den Offline-Zugriff auf dein Gerät herunter.
- **Umbenennen**: Benenne den Ordner direkt im Remote-Speicher um.
- **Verschieben**: Verlagere den Ordner an einen anderen Ort in deinem Cloud-Speicher.
- **Löschen**: Sei vorsichtig, da diese Aktion den Ordner und seinen Inhalt dauerhaft aus deinem Cloud-Speicher entfernt. Dieser Vorgang kann nicht rückgängig gemacht werden.


## Schnellzugriff

Der Schnellzugriff-Bereich befindet sich oben auf dem Bildschirm. Er gibt dir schnellen Zugang zu deinen Lieblingsordnern und zuletzt geöffneten Dateien aus verbundenen Cloud-Diensten.
Wann immer du eine Datei oder einen Ordner aus der Cloud öffnest, wird sie/er der Liste 'Zuletzt geöffnet' hinzugefügt. Um diese Liste zu löschen, öffne 'Aktuell', tippe auf die Schaltfläche 'Weitere Aktionen' und wähle 'Liste löschen'. Du kannst auch tief verschachtelte Ordner als Favoriten markieren, um schnell darauf zuzugreifen, ohne durch die Verzeichnisstruktur zu navigieren.

## Andere Dienste

Dieser Bereich zeigt zusätzliche Funktionen an. Derzeit unterstützt die App Last.fm-Scrobbling. Wenn verbunden, werden deine Wiedergabestatistiken automatisch an dein Last.fm-Konto gesendet. Du kannst dein Last.fm-Profil später aufrufen, um Höranalysen zu sehen und personalisierte Musikempfehlungen zu erhalten. Detaillierte Einrichtungsanleitungen sind [hier](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm) verfügbar.
