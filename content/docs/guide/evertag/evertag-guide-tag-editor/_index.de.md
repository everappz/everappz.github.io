---
title: "Tag-Editor"
date: 2020-02-01
description: "Erfahren Sie, wie Sie den Evertag Tag-Editor verwenden, um Musik-Metadaten zu aktualisieren, Albumcover zu bearbeiten, mehrere Dateien gleichzeitig zu bearbeiten und Tags von MusicBrainz zu verwalten. Ideal für die Organisation Ihrer Musikbibliothek auf iOS und Mac."
keywords: [
  "Evertag Tag-Editor", "Audio-Metadaten-Editor", "Musik-Tag-Editor",
  "Audio-Tags iPhone bearbeiten", "Albumcover-Editor", "Audio-Tags stapelweise bearbeiten",
  "MusicBrainz Metadaten", "Musikorganisations-App", "Evertag Anleitung", "ID3 Tag-Editor"
]
tags: ["anleitung", "evertag", "tag-editor"]
readingTime: 5
---


Der **Tag-Editor** ist der Hauptbildschirm der Evertag-App, auf dem Sie Audio-Datei-Metadaten anzeigen und bearbeiten können. Öffnen Sie diesen Bildschirm, indem Sie eine Datei aus dem Abschnitt **Lokale Dateien** oder einem verbundenen **Cloud-Speicher**-Konto antippen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag Editor Screen" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Bearbeitungsmodi

Evertag bietet zwei Bearbeitungsmodi:

- **Einzeldatei-Modus**
  - Navigieren Sie zwischen Dateien, indem Sie auf dem Artwork-Karussell nach links oder rechts wischen.

- **Stapelmodus**
  - Bearbeiten Sie mehrere Dateien gleichzeitig und wenden Sie gemeinsame Metadaten an.
  - Zum Aktivieren: Scrollen Sie nach unten und tippen Sie auf **Dateien gleichzeitig bearbeiten**.

## Einzeldatei-Modus

Standardmäßig öffnet die App den Tag-Editor im Einzeldatei-Modus mit nur den Hauptbearbeitungsoptionen. In diesem Modus können Sie die gängigsten Metadatenfelder bearbeiten, wie z. B.:

**Titel, Untertitel, Albumkünstler, Album, Künstler, Komponist, Interpret, Genre, Kommentar, Beats per Minute, Podcast, Kompilation, CD-Nummer, Tracknummer, Track-Gesamtzahl, Bewertung, Jahr**

Um auf alle verfügbaren Tags zuzugreifen, scrollen Sie zum Ende des Bildschirms und tippen Sie auf die Option **Erweiterte Tags anzeigen**. Dadurch wechselt der Editor in den erweiterten Modus, in dem Sie über **120 Metadatenfelder** bearbeiten können, darunter **MusicBrainz-Tags**, **Lyrics**, **Jugendschutz-Bewertungen**, Replay-Gain-Werte, Sortierreihenfolgen, Podcast-Metadaten und mehr. Verwenden Sie **Einstellungen → Audio-Tags-Editor → Schaltflächen auf dem Hauptbildschirm**, um «Erweiterte Tags anzeigen» dauerhaft einzuschalten, damit es immer aktiviert ist.

{{< cards cols="1">}}
{{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Stapelmodus

Sie können die Stapelbearbeitung auf zwei Arten aufrufen:

1. **Vom Dateimanager aus**
   - Tippen Sie auf **Weitere Aktionen** (•••) oben rechts.
   - Tippen Sie auf **Auswählen**, wählen Sie mehrere Dateien aus und tippen Sie dann auf **Audio-Tags bearbeiten**.

2. **Vom Tag-Editor aus**
   - Öffnen Sie eine beliebige Datei, scrollen Sie nach unten und tippen Sie auf **Dateien gleichzeitig bearbeiten**, um alle Dateien aus demselben Ordner zu laden.

{{< cards cols="1">}}
{{< card title="" subtitle="Batch Editing Mode" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Nach der Bearbeitung tippen Sie auf **Speichern**, um Änderungen anzuwenden.

## Lyrics bearbeiten

Der erweiterte Editor zeigt das Feld **Lyrics**. Tippen Sie darauf, um die Lyrics-Liste zu öffnen – jeder Lyrics-Eintrag hat seine eigene Sprache und Beschreibung, sodass ein einzelner Track mehrere Übersetzungen speichern kann.

Sie müssen Lyrics nicht von Grund auf eintippen. Der Editor enthält Ein-Tipp-Suchverknüpfungen zu den beliebtesten Lyrics-Datenbanken im Web, vorausgefüllt mit dem aktuellen Künstler und Titel des Tracks:

- **Lrclib** — die führende öffentliche Datenbank für **zeitgestempelte (LRC-Stil) Lyrics**. Verwenden Sie es, wenn Sie synchronisierte Lyrics möchten, die in Playern, die sie unterstützen, zeilenweise scrollen.
- **Genius** — große Katalog mit Anmerkungen und genauen Klartext-Lyrics.
- **Lyricsify** — community-basierte Datenbank mit einfachen und zeitgestempelten Lyrics.
- **Google** — eine allgemeine Websuche als Fallback, wenn die speziellen Datenbanken keine Übereinstimmung haben.

Jede Verknüpfung erscheint nur, wenn der entsprechende Dienst von Ihrem Gerät aus erreichbar ist. Tippen Sie auf einen Dienst, kopieren Sie die Lyrics (oder die LRC-Zeitstempel), die Sie möchten, kehren Sie zu Evertag zurück und fügen Sie sie in das Textfeld ein – dann **Speichern**, um die Lyrics zurück in die Tags der Audiodatei zu schreiben.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Pages" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Wählen Sie eine Sprache aus der Auswahlliste:

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Language Selector" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Fügen Sie dann die Lyrics ein oder tippen Sie sie ein. Evertag unterstützt sowohl einfachen Text als auch zeitgestempelte (synchronisierte) Lyrics – der Platzhalter zeigt ein Beispiel des LRC-Stilformats, das genau das ist, was Lrclib und Lyricsify für synchronisierte Ergebnisse zurückgeben.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Text Editor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Bewertung und Jugendschutz-Bewertung setzen

Der erweiterte Editor bietet ein Stern-**Bewertungs**-Steuerelement neben einem **Jugendschutz-Bewertungs**-Segmentsteuerung.

### Stern-Bewertung

Verwenden Sie das Feld **Bewertung**, um einem Track eine persönliche Punktzahl von einem bis fünf Sternen zu geben. Der Wert wird in das Standard-Bewertungs-Tag der Datei geschrieben (POPM für ID3, `rate` für MP4, `RATING` für Vorbis/APE usw.), sodass andere Apps, die dieses Tag lesen – einschließlich der Musik-App, Plex, Roon und die meisten Desktop-Tag-Editoren – Ihre Bewertungen sofort übernehmen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Rating" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Jugendschutz-Bewertung

Die **Jugendschutz-Bewertung** markiert den Inhalt eines Tracks mit einem der Werte aus dem Parental Advisory-Standard, den der iTunes Store und die meisten Musikplattformen verwenden:

- **Unbedenklich** — der Standard für Tracks ohne Elternberatungs-Informationen. Die Datei wird als für alle Zuhörer geeignet behandelt und zeigt in Playern, die das Tag respektieren, kein Beratungslabel an.
- **Explizit** — der Track enthält explizite Sprache oder Inhalte. Player, die Kindersicherungen beachten (die Musik-App, die Apple TV-App, Spotify-Exporte, Plex usw.), zeigen neben dem Titel ein **E**-Abzeichen an und können bei aktivierten Einschränkungen auf dem Gerät oder Konto den Track aus Kinderprofilen ausblenden oder die Wiedergabe verweigern.
- **Bereinigt** — eine zensierte oder bearbeitete Version eines ansonsten expliziten Tracks. Player zeigen ein **C**-Abzeichen an, damit Zuhörer eine bereinigte Version vom originalen expliziten Master unterscheiden können, was nützlich ist, wenn beide Versionen in derselben Bibliothek vorhanden sind.

Sie sollten dieses Feld festlegen oder korrigieren, wenn:

- Eine Datei die falsche Bezeichnung hat (zum Beispiel eine bereinigte Radio-Version, die fälschlicherweise als explizit gekennzeichnet wurde, oder umgekehrt).
- Tracks ohne Tag aufgenommen oder heruntergeladen wurden und jetzt als unbedenklich angezeigt werden, obwohl sie explizite Inhalte enthalten – notwendig für Kindersicherung und familiengeteilte Bibliotheken.
- Sie ein Album zur Einreichung oder Weitergabe vorbereiten und sicherstellen müssen, dass jeder Track konsistente Metadaten trägt.
- Sie möchten, dass CarPlay, der Sperrbildschirm, Apple Music-ähnliche Player oder DJ-Software das korrekte **E** / **C**-Abzeichen neben dem Tracktitel anzeigen.

Der Wert wird im Standard-Jugendschutz-Bewertungsfeld für das Dateiformat gespeichert (`rtng` für MP4, `TXXX:ITUNESADVISORY` für ID3, `ITUNESADVISORY` für Vorbis), sodass jeder Player, der Elternberatungs-Metadaten liest, Ihre Aktualisierung sieht.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Advisory Rating" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Albumcover bearbeiten

So ändern Sie ein Albumcover:

1. Tippen Sie auf das **Kamera-Symbol** im Artwork-Karussell.
2. Wählen Sie den Bildstandort: Lokale Dateien, Cloud, Downloads oder Fotobibliothek.
3. Wählen Sie ein Bild aus, das als Coverart angewendet werden soll.

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Weitere Aktionen im Tag-Editor

Zusätzliche Bearbeitungsoptionen sind über die Symbolleiste unter der Artwork-Ansicht verfügbar.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Audio-Tags automatisch suchen

Diese Aktion aktiviert die intelligente Tag-Suchmaschine, die vollständige Metadaten für Ihre Audiodatei anhand der vorhandenen Informationen findet und ausfüllt.
Die App verwendet die MusicBrainz-Datenbank – eine der umfassendsten Tag-Datenbanken – mit über **50 Millionen** Tracks.

### Albumcover suchen

Verwenden Sie Metadaten, um im Web nach dem korrekten Albumcover zu suchen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Search Album Cover" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Sobald es gefunden wurde, speichern Sie das Bild in Ihre **Fotos** über das Systemkontextmenü.

{{< cards cols="1">}}
  {{< card title="" subtitle="Add Image to Photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Kehren Sie danach zum Tag-Editor zurück, tippen Sie auf das Kamera-Symbol, gehen Sie zu **Fotobibliothek** und wählen Sie das gespeicherte Bild aus. Die App legt es als Cover für Ihre Audiodatei fest.

Sie können anpassen, wie Coverbilder in den App-Einstellungen skaliert werden.

### Album-Artwork speichern

Diese Aktion speichert das aktuelle Album-Artwork im Ordner **Documents**, damit Sie es später wiederverwenden können.

### Kodierung normalisieren

Diese Aktion normalisiert die Textkodierung aller Tags in den Metadaten der Audiodatei. Besonders hilfreich, wenn Sie von einem Windows-PC wechseln, wo Dateien möglicherweise unterschiedliche Kodierungen verwenden, die auf einem Mac als unleserliche oder verstümmelte Zeichen erscheinen.

### Tags manuell suchen

Suchen Sie manuell nach Album-Metadaten über die MusicBrainz-Datenbank.

- Wählen Sie das Album aus

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Wählen Sie den richtigen Song aus

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Song" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Wählen Sie aus, welche Tags angewendet werden sollen

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Audio Tags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Tippen Sie auf **Fertig**, um die ausgewählten Metadaten auf Ihren Track anzuwenden.

### Audio-Tags löschen

Alle Metadatenfelder für eine Datei löschen. Nützlich, wenn Sie von Grund auf neu beginnen. Tippen Sie zur Bestätigung auf **Speichern**.

## Tag-Editor-Einstellungen

Navigieren Sie zu **Einstellungen → Audio-Tags-Editor**, um das Verhalten anzupassen.

### Albumcover-Skalierung

Wählen Sie, wie Albumcover beim Speichern in Audiodateien skaliert werden sollen. Sie können die Skalierung deaktivieren, um die Originalgröße beizubehalten, sollten aber beachten, dass einige Player möglicherweise keine großen Artwork-Dateien unterstützen. Die Option «Originalgröße» ist Teil der Premium-Personalisierungsfunktionen.

### Tag-Speicheroptionen

- **ID3v2.4** — Wenn aktiviert, speichert die App Tags im ID3v2.4-Format, wenn möglich. Deaktivieren Sie es, um auf das breiter unterstützte ID3v2.3 zurückzufallen, wenn Ihre Audio-Tags auf älteren Playern oder Geräten nicht korrekt angezeigt werden.
- **Doppelte Tags** — Wenn aktiviert, werden allgemeine Metadatenfelder in beide Tag-Abschnitte der Datei dupliziert. Dies verbessert die Kompatibilität mit älteren Audio-Playern, ist aber in den meisten Fällen nicht erforderlich.

### Cloud-Datei-Metadaten-Update-Optionen

Sie können steuern, wie die App Metadaten für Audiodateien aktualisiert, die in Cloud-Diensten gespeichert sind:

- **Bestätigungsnachricht anzeigen**
  Vor dem Anwenden von Metadatenänderungen auf Cloud-Dateien fragen.

- **Metadaten der Datei automatisch aktualisieren**
  Metadatenänderungen nach der Bearbeitung automatisch in der Cloud-Datei speichern.

- **Metadaten der Datei nicht aktualisieren**
  Cloud-Dateien nicht aktualisieren – Änderungen werden nur lokal angewendet.

### Online-Dateien bearbeiten

Wählen Sie, was mit lokal heruntergeladenen Kopien von Cloud-Dateien nach der Bearbeitung passiert:

- **Heruntergeladene Datei immer löschen**
  Die lokale Kopie nach dem Speichern von Änderungen entfernen.

- **Heruntergeladene Datei nicht löschen**
  Die heruntergeladene Datei nach der Bearbeitung auf Ihrem Gerät behalten.

### Hauptbildschirmschaltflächen

Passen Sie an, welche Aktionen auf dem Hauptbildschirm des Tag-Editors erscheinen (Automatische Suche nach Audio-Tags, Manuelle Suche nach Audio-Tags, Album-Artwork suchen, Album-Artwork speichern, Kodierung normalisieren, Audio-Tags löschen). Sie können auch **Erweiterte Tags anzeigen** und **Dateien gleichzeitig bearbeiten** umschalten, damit der Editor immer in Ihrem bevorzugten Modus öffnet.
