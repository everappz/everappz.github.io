---
title: "Musikbibliothek"
date: 2020-02-01
description: "Erfahren Sie, wie Sie Ihre Musikbibliothek in Flacbox auf iPhone, iPad und Mac aufbauen, organisieren und synchronisieren. Fügen Sie Titel manuell hinzu oder synchronisieren Sie von Cloud-Diensten, verwalten Sie Metadaten, Album-Cover, Playlists, Favoriten, Aktuell und Lesezeichen. Inklusive Hi-Res-Audio-Unterstützung, MusicBrainz-Tag-Editor, Online- und Offline-Synchronisation sowie Personalisierungsoptionen."
keywords: [
  "Flacbox Musikbibliothek", "Musik aus Cloud synchronisieren", "Musikmetadaten organisieren",
  "Audio-Tags bearbeiten Flacbox", "Offline-Musik synchronisieren", "lokale Musik importieren",
  "Flacbox Playlist-Verwaltung", "Album-Cover-Suche Flacbox",
  "iPhone Musikmetadaten", "Flacbox App-Anleitung",
  "Flacbox MusicBrainz", "Flacbox Tags normalisieren",
  "Flacbox Hi-Res Musikbibliothek", "Flacbox FFmpeg Bibliothek",
  "Flacbox Solo-Alben", "Flacbox Komponistenansicht"
]
tags: ["musik", "anleitung", "flacbox", "bibliothek"]
readingTime: 11
---


Das Verwalten Ihrer Musikbibliothek ist mit Flacbox ein Kinderspiel, wo Sie mühelos alle Ihre Titel — lokale FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE und Dutzende anderer Formate — in einer einzigen, durchsuchbaren Sammlung organisieren können. Sie haben zwei Optionen zum Aufbau Ihrer Musikbibliothek: manuelle Hinzufügung oder automatische Synchronisation.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Musikbibliothek Albenansicht" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Manuelle Hinzufügung

Um Titel manuell hinzuzufügen, tippen Sie auf das **Musik hinzufügen**-Symbol oben links und wählen Sie Ordner oder Dateien aus einem verbundenen Cloud-Speicherdienst oder Dateien auf Ihrem Gerät aus. Beim Hinzufügen von Titeln werden nur Links zu diesen Titeln erstellt — die eigentlichen Dateien verbleiben an ihren ursprünglichen Speicherorten.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Songs zur Musikbibliothek hinzufügen" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Sie können auf der Mac-Version auch Dateien per Drag-and-Drop in die Bibliothek ziehen oder auf iPhone und iPad **Dateien öffnen…** / **Ordner öffnen…** aus der Systemdateiauswahl verwenden.

## Wiedergabe fortsetzen

Stellen Sie die Audio-Player-Warteschlange aus der zuletzt gespeicherten Position wieder her, wenn diese Funktion in den Anwendungseinstellungen aktiviert ist. Aktivieren Sie sowohl **Audio-Player-Status speichern** als auch **Wiedergabeposition speichern** in **Einstellungen → Audio-Player → Allgemein**.

## Speicherorte

Alle Titel in Ihrer Bibliothek sind übersichtlich nach Quelltyp und Musik-Tags gruppiert. Sie können Songs nach Speicherort filtern, indem Sie auf die Schaltfläche **Weitere Aktionen** oben rechts tippen und **Filter** auswählen.

### Online-Musik

Dieser Bereich zeigt Musik aus Ihren verbundenen Cloud-Speicherdiensten.

### Dateien in dieser Anwendung

Hier finden Sie Musik, die für die Offline-Wiedergabe verfügbar ist, aus Ihren lokalen Dateien.

### Dateien auf diesem iPhone / iPad / Mac

Diese Kategorie umfasst Musik, die aus Ihrem Gerät in die Anwendung importiert wurde, hinzugefügt über den **Dateien öffnen…**-Systemdialog.

## Kategorien

Wenn Sie Titel zu Ihrer Musikbibliothek hinzufügen, liest die App automatisch deren Audio-Tags und organisiert sie in Kategorien wie Songs, Nicht gespielte Songs, Alben, Albumkünstler, Künstler, Genres und Komponisten.

## Tag-Gruppierung

Diese Kategorien helfen Ihnen, Ihre Titel nach Musik-Tags zu organisieren. Wenn Sie keine Alben sehen, stellen Sie sicher, dass die App jeden Titel gescannt hat. Den Fortschritt können Sie unter **Einstellungen → Musikbibliothek → Metadaten-Lesen** überprüfen.

- **Songs** — alle Songs, gruppiert nach dem TRACK_TITLE-Tag.
- **Nicht gespielte Songs** — alle Songs, die noch nie abgespielt wurden.
- **Alben** — Songs, gruppiert nach dem ALBUM_NAME-Tag.
- **Albumkünstler** — Songs, gruppiert nur nach dem ALBUM_ARTIST_TAG.
- **Künstler** — Songs, gruppiert nur nach dem ARTIST_TAG.
- **Genres** — Songs, gruppiert nach dem GENRE-Tag.
- **Komponisten** — Songs, gruppiert nach dem COMPOSER-Tag.

## Favoriten

Sie können Songs als Favoriten auf dem Audio-Player-Bildschirm oder über das Optionsmenü markieren.

## Aktuell

Dieser Bereich zeigt alle zuletzt gespielten Titel an. Sie können konfigurieren, wie viele Elemente die Aktuell-Liste behält unter **Einstellungen → Bibliothek → Aktuell → Listengröße ändern**, und die Liste in M3U / CSV / TXT exportieren.

## Lesezeichen

Sie können Audio-Lesezeichen erstellen, während ein Song abgespielt wird, und sie auf diesem Bildschirm verwalten. Detaillierte Anweisungen sind [hier](/docs/guide/evermusic/evermusic-guide-music-library) verfügbar.

## Obere Symbolleiste

Die obere Symbolleiste bietet mehrere praktische Aktionen: Suchen, Alle abspielen, Alles zufällig abspielen und Wiedergabe fortsetzen.

## Suche

Die Suchfunktion ermöglicht es Ihnen, einen bestimmten Titel, Künstler, Album oder Genre in Ihrer Musikbibliothek zu finden. Die Suche läuft lokal gegen die Musikbibliotheksdatenbank.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Musikbibliothek Suche" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Optionsmenü

Jeder Song in Ihrer Musikbibliothek hat ein Menü mit weiteren Aktionen, auf das Sie über die Drei-Punkte-Schaltfläche neben dem Songtitel zugreifen können.

### Für einzelne Songs

- **Weiter abspielen** — fügt den Song oben in die Warteschlange hinzu.
- **Später abspielen** — hängt den Song unten an die Warteschlange an.
- **Zur Playlist hinzufügen** — fügt den Song einer Playlist hinzu.
- **Zu Favoriten hinzufügen** — markiert den Song als Favorit.
- **Herunterladen** — speichert den Song in lokalen Dateien.
- **Audio-Tags bearbeiten** — öffnet den integrierten Audio-Tag-Editor.
- **Im Ordner anzeigen** — zeigt den Ordner, in dem die Audiodatei gespeichert ist.
- **Im Finder anzeigen** — für importierte Mac-Dateien zeigt den Ordner auf dem Mac.
- **Öffnen in** — exportiert die Audiodatei in eine andere App.
- **Aus Cloud-Dienst löschen** — entfernt die Datei aus der Bibliothek und dem Cloud-Speicher. **Diese Aktion ist irreversibel.**
- **Aus Musikbibliothek löschen** — löscht den Song aus Ihrer Bibliothek, aber die Datei bleibt im Speicher.

### Für Song-Sammlungen

Für Song-Sammlungen wie Alben, Künstler, Genres oder Komponisten umfasst das Optionsmenü folgende Aktionen:

- **Alle abspielen** — ersetzt die Warteschlange durch Songs aus der ausgewählten Sammlung.
- **Weiter abspielen** — fügt Songs oben in die Warteschlange hinzu.
- **Später abspielen** — hängt Songs unten an die Warteschlange an.
- **Zur Playlist hinzufügen** — schließt Songs aus dieser Sammlung in eine Playlist ein.
- **Offline-Modus aktivieren** — lädt Songs in lokale Dateien herunter.
- **Bild bearbeiten** — ändert das Album-Cover für die Song-Sammlung.
- **Zum Archiv hinzufügen** — bündelt die gesamte Sammlung in eine ZIP-Datei (Premium-Funktion).
- **Song-Liste exportieren** — exportiert die Sammlung in M3U, CSV oder TXT.
- **Aus Musikbibliothek löschen** — entfernt die Song-Sammlung aus Ihrer Bibliothek.

## Auswahlmodus

Sie können den Auswahlmodus über die Schaltfläche „Weitere Aktionen" oben rechts aktivieren.

## Album-Detail

Wenn Sie die Bereiche Künstler, Albumkünstler oder Komponisten öffnen, sehen Sie einen Umschalter für Songs / Alle Alben / Exklusive Alben / Solo-Alben.

- **Songs** — zeigt alle Songs, bei denen dieser Künstler / Albumkünstler / Komponist in den Audio-Tags erscheint.
- **Alle Alben** — zeigt Compilation-Alben und alle Alben, bei denen der Künstler vorkommt.
- **Exklusive Alben** — zeigt Alben, bei denen der angegebene Künstler der einzige Künstler mit diesem Albumnamen ist.
- **Solo-Alben** — zeigt Alben, bei denen nur die Titel des angegebenen Künstlers erscheinen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Album-Detail-Bildschirm" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Einstellungen

Tippen Sie auf „Weitere Aktionen" → Einstellungen, um Ihre Musikbibliotheks-Einstellungen zu konfigurieren.

### Metadaten-Lesen

Wenn Sie Titel zur Bibliothek hinzufügen, beginnt der Metadaten-Reader mit der Arbeit. Sie können die Geschwindigkeit des Metadaten-Lesens anpassen. Der Metadaten-Reader aktualisiert **nur Metadaten in Ihrer Musikbibliothek** und ändert keine in Ihrem Cloud-Konto oder lokalem Speicher gespeicherten Dateien.

Wenn **Normalize Metadata Encoding** aktiviert ist, normalisiert die App automatisch die Metadaten-Kodierung für alle Songs. Dadurch werden Probleme mit fehlerhafter Tag-Kodierung behoben.

### Verfügbare Modi für den Metadaten-Reader

- **Deaktiviert** — der Metadaten-Reader ist ausgeschaltet und Dateinamen werden angezeigt.
- **Aktueller Song** — die Anwendung liest Metadaten nur für den aktuell abgespielten Song.
- **Wiedergabe-Warteschlange** — die App liest Metadaten für alle Songs in der Warteschlange.
- **Bibliothek** — die App liest Metadaten für alle Songs in der Bibliothek.

### Online-Synchronisation

Die automatische Online-Musik-Synchronisation fügt Titel aus verbundenen Cloud-Diensten automatisch zur Musikbibliothek hinzu. Die Online-Synchronisation läuft nur, wenn die App im Vordergrund ist.

### Offline-Synchronisation

Hier konfigurieren Sie die Offline-Musik-Synchronisation.

#### Synchronisierte Offline-Ordner

Wenn Sie einen Cloud-Ordner offline verfügbar machen, erscheint er hier. Der Ordnerinhalt wird in **Lokale Dateien → Offline-Ordner** heruntergeladen.

#### Zeitintervall

Sie können das Zeitintervall einstellen, wie oft die App Offline-Ordner auf Änderungen prüfen soll.

#### Lokales Ordner-Scanning starten

Diese Option scannt alle lokalen Ordner im **Dokumente**-Verzeichnis der Anwendung nach unterstützten Audiodateien.

### Personalisierung

In diesem Abschnitt können Sie den Musikbibliotheks-Bildschirmstil konfigurieren. Drei Optionen sind verfügbar: Einfaches Menü, Gruppiertes Menü, Tab-Menü.

### Album-Cover

Hier konfigurieren Sie, wie die Anwendung Album-Artwork lädt und speichert.

- **Netzwerktyp** — Wi-Fi oder Wi-Fi & Mobilfunk für Cover-Downloads wählen.
- **Album-Cover für Online-Dateien laden** — wenn aktiviert, werden eingebettete Album-Cover für Dateien im Cloud-Speicher geladen.
- **Im Ordner suchen** — wenn aktiviert, sucht die App nach JPEG- oder PNG-Bildern im gleichen Ordner.
- **Cover-Qualität** — die Qualität der gespeicherten Album-Cover wählen.
- **Im Ordner anzeigen** — den Ordner öffnen, in dem Album-Cover gespeichert sind.
- **Alle löschen** — gespeicherte Album-Cover löschen.

### Playlists

Sie können die Option aktivieren, den gleichen Song zweimal zu einer Playlist hinzuzufügen. Standardmäßig ist diese Option deaktiviert.

### Aktuell

Sie können Ihre zuletzt gespielten Songs-Liste verwalten.

- **Liste löschen** — die gesamte Liste der zuletzt gespielten Songs löschen.
- **Listengröße ändern** — die Anzahl der in der Liste angezeigten Elemente festlegen.
- **Song-Liste exportieren** — Ihre zuletzt gespielten Songs-Liste in M3U, CSV oder TXT exportieren. Detaillierte Anweisungen sind [hier](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/) verfügbar.

### Favoriten

Sie können die Liste Ihrer Lieblingssongs verwalten.

- **Gleichzeitige Bearbeitung** — wenn aktiviert, wird ein Song, der zu Favoriten hinzugefügt wird, sowohl in der Musikbibliothek als auch im Dateibereich hinzugefügt.
- **Liste löschen** — die gesamte Liste der Lieblingssongs löschen.
- **Song-Liste exportieren** — ähnlich wie Aktuell, exportiert die Favoritenliste in M3U, CSV oder TXT.

### Bibliothek löschen

Diese Aktion löscht die Musikbibliotheksdatenbank, lässt aber Ihre Musikdateien im Speicher unberührt.

### Inhalt-Lade-Limit

Standardmäßig verwendet die Anwendung Paginierung, um die Ladezeit zu reduzieren. Sie können diese Option deaktivieren und der Anwendung erlauben, alle verfügbaren Daten auf einmal zu laden.
