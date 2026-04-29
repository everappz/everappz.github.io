---
title: "So exportieren Sie Ihre Titelsammlung in M3U, CSV und TXT in Evermusic & Flacbox"
date: 2024-01-31
description: "Erfahren Sie, wie Sie Ihre aktuellen, Favoriten, Wiedergabelisten und Alben aus Evermusic und Flacbox in die Formate M3U, CSV oder TXT exportieren. Perfekt für Last.fm-Scrobbling und Wiedergabe auf anderen Geräten."
keywords: ["Evermusic Export", "Flacbox Export", "Export nach M3U", "Wiedergabeliste in CSV exportieren", "M3U TXT CSV Wiedergabeliste", "Musik exportieren"]
tags: ["evermusic", "aktuell", "favoriten", "export", "m3u", "wiedergabeliste", "csv", "txt", "album"]
---

{{< author-byline >}}


**Kurzfassung:** Evermusic und Flacbox ermöglichen es Ihnen, jede Titelsammlung (Aktuell, Favoriten, Wiedergabelisten, Alben) in CSV-, TXT- oder M3U-Dateien zu exportieren. Nutzen Sie diese Exporte, um auf Last.fm zu scrobbeln, Ihre Bibliothek zu sichern oder Ihre Wiedergabelisten auf anderen Geräten abzuspielen.

## Einführung

Der Export Ihrer aktuellen Titel, Favoriten, Alben und Wiedergabelisten aus der App in eine externe Datei kann unglaublich nützlich sein. Sie können diese Dateien verwenden, um Ihren Hörverlauf bei Scrobbling-Diensten wie [Last.fm](http://Last.fm) zu aktualisieren oder Ihre Wiedergabelisten auf externen Geräten anzuhören. Mit Evermusic und Flacbox ist dieser Vorgang einfach. Hier zeigen wir Ihnen, wie Sie Ihre aktuellen Titel in CSV/TXT und Ihre Wiedergabelisten in M3U exportieren. Diese Funktionalität ist jedoch für jede Titelsammlung in der App verfügbar.

## Format wählen

Um Ihre aktuellen Titel zu exportieren, öffnen Sie den Bereich 'Musikbibliothek' und wählen Sie den Menüpunkt 'Aktuell'.

![Musikbibliothek](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Tippen Sie auf dem nächsten Bildschirm auf die Schaltfläche 'Weitere Aktionen' in der oberen rechten Ecke und wählen Sie 'Songliste exportieren'.

![Aktuell exportieren](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Auf dem Bildschirm 'Dateiformat auswählen' haben Sie mehrere Optionen - CSV, TXT, M3U.

- CSV

Dies steht für kommagetrennte Werte, perfekt zum Organisieren Ihrer Daten in einem übersichtlichen Tabellenformat. In der Zieldatei finden Sie Parameter wie Künstlername, Albumname, Titelname, Zeitstempel (die Zeit, zu der Sie die Titel gehört haben), Album-Künstlername und Titeldauer. Sie können diese Datei später verwenden, um Ihren Hörverlauf bei Scrobbling-Diensten wie [Last.fm](http://Last.fm) zu aktualisieren, wie [hier](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/) beschrieben.

- TXT

Hier sprechen wir von einer einfachen Textdatei. Sie ist einfach und unkompliziert, mit Parametern wie Künstlername, Albumname, Titelname und Dauer. Nützlich, wenn Sie nur eine Liste von Titeln in Textdarstellung benötigen.

- M3U

Dieses Format ist im Wesentlichen die erste Wahl für das Erstellen von Wiedergabelisten. Es ist großartig, weil Sie Ihre Songliste exportieren und Ihre Titel auf jedem Gerät genießen können, auch wenn Sie die Originaldateien nicht haben (wenn Sie die Option der absoluten URL für den Mediendatei-Export wählen). In der Ausgabedatei finden Sie Parameter wie Dauer, Künstlername, Titelname und Mediendatei-Speicherort.

## CSV-Format

Wählen wir nun CSV und sehen, was wir erhalten. Wählen Sie einfach CSV und drücken Sie die Schaltfläche 'Exportieren'.

![Dateiformat auswählen](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Sobald der Export abgeschlossen ist, sehen Sie eine Meldung mit zwei Optionen. Tippen auf 'Datei anzeigen' zeigt die resultierende Datei in Ihrem Dokumentenverzeichnis an.

![Export abgeschlossen](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Jetzt können Sie diese Datei senden, sie in einem externen Texteditor öffnen oder sie verwenden, um Ihren Hörfortschritt auf [Last.fm](http://Last.fm) zu aktualisieren.

![Exportordner mit Ergebnisdateien](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Die CSV-Ausgabedatei enthält Felder im folgenden Format:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Zum Beispiel:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![Exportierte CSV-Datei](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT-Format

Die TXT-Ausgabedatei enthält Felder im folgenden Format:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Zum Beispiel:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![Exportierte TXT-Datei](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U-Format

Als Nächstes führen wir Sie durch den Export Ihrer Wiedergabeliste in das M3U-Format, das der De-facto-Standard für Wiedergabelistendateien ist. Die Hauptvoraussetzung für einen erfolgreichen Export der Wiedergabeliste ist, dass sich alle Dateien in der Wiedergabeliste auf demselben Speicher befinden müssen, sei es in einem Cloud-Dienst wie Google Drive, lokalen Dateien oder Dateien auf Ihrem Gerät. Um den Exportvorgang zu starten, öffnen Sie eine beliebige Wiedergabeliste und tippen Sie auf die Schaltfläche 'Weitere Aktionen' in der oberen rechten Ecke, dann wählen Sie den Menüpunkt 'Songliste exportieren'.

![Wiedergabelisten-Bildschirm](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Auf dem nächsten Bildschirm wählen Sie das Dateiformat 'M3U', wo Sie auf zwei Optionen für 'Mediendatei-Speicherorttyp' stoßen:

![Bildschirm zur Auswahl des Exportdateiformats](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Wenn Sie 'Relativer Pfad' wählen, wird die Wiedergabeliste mit Mediendatei-Speicherorten erstellt, die relativ zur Wiedergabelistendatei geschrieben werden. Zum Beispiel:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Vermeiden Sie in diesem Fall, den Speicherort der M3U-Datei nach Abschluss des Exports zu ändern, da dies die Pfade zu den Mediendateien beschädigt. Um die Wiedergabe Ihrer Wiedergabeliste zu starten, tippen Sie einfach auf die exportierte Wiedergabelistendatei, und die App wird die Mediendateien auf Ihrem Speicher automatisch finden und die Wiedergabe starten. Sie können Ihre Wiedergabelisten sogar auf den Speicher exportieren und sie dann auf Ihrem neuen Gerät wieder importieren.

2. Wenn Sie 'Absolute URL' wählen, generiert die App direkte URLs für Ihre Mediendateien. Dies ermöglicht es Ihnen, die Wiedergabeliste auf jedem Gerät/jeder Anwendung abzuspielen, ohne dass sich alle Mediendateien auf demselben Speicher wie die Wiedergabelistendatei befinden müssen. Diese Option wird nur für Cloud-Speicher unterstützt, die direkte Datei-URLs generieren können. Beachten Sie jedoch, dass die generierten URLs in einigen Fällen eine begrenzte Lebensdauer haben und nach einiger Zeit ablaufen können. Hier ist die Liste der unterstützten Cloud-Dienste: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (im Gastmodus)  

Die Ausgabe-Mediendatei-URL sieht ungefähr so aus:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Nachdem Sie den 'Mediendatei-Speicherorttyp' ausgewählt haben, tippen Sie auf 'Exportieren'. Die App fordert Sie auf, einen Zielordner für den Export der M3U-Datei auszuwählen. Tippen Sie auf 'Fertig', um Ihre Auswahl zu bestätigen.

![Ordner auswählen](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Die App generiert eine M3U-Datei und lädt sie hoch/verschiebt sie in den Zielordner.

![M3U-Datei hochladen](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Sobald der Export abgeschlossen ist, erscheint eine Systemmeldung mit der Option 'Datei anzeigen'.

![Meldung Export abgeschlossen](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Tippen darauf zeigt die exportierte Datei in der App an.

![Exportierte M3U-Datei in der Dateiliste](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Wenn Sie im vorherigen Schritt 'Relativer Pfad' als 'Mediendatei-Speicherorttyp' ausgewählt haben, hat die Ausgabedatei das folgende Format:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![M3U-Beispiel mit relativen Pfaden](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Für die Option 'Absolute URL' generiert die App eine M3U-Datei im Format:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![M3U-Beispiel mit absoluten Datei-URLs](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Sie können diese Datei auf jedem Gerät/jeder Anwendung öffnen, die M3U-Wiedergabelisten unterstützt.

![M3U-Wiedergabeliste in externer App geöffnet](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Abschließende Gedanken

Der Export Ihrer Titel aus Evermusic und Flacbox gibt Ihnen die volle Kontrolle über Ihre Musikdaten. Ob Sie Ihren Hörverlauf sichern, auf Last.fm scrobbeln oder Wiedergabelisten auf externen Geräten genießen - diese Exportoptionen: M3U, CSV und TXT - sind leistungsstarke Werkzeuge, die auf Flexibilität und Kompatibilität ausgelegt sind. Nutzen Sie diese Funktionen, um die Art und Weise zu verbessern, wie Sie Ihre Musiksammlung plattformübergreifend organisieren, teilen und wieder besuchen.

## FAQ

{{% details title="Welches Exportformat sollte ich für Last.fm-Scrobbling verwenden?" closed="true" %}}
Verwenden Sie CSV. Es enthält Zeitstempel und vollständige Metadaten, die von Scrobbling-Tools wie Last.fm-Scrubbler-WPF benötigt werden.
{{% /details %}}

{{% details title="Kann ich jede Titelsammlung exportieren, nicht nur Wiedergabelisten?" closed="true" %}}
Ja. Sie können Aktuell, Favoriten, Alben, Wiedergabelisten und jede andere Titelsammlung in der App mit denselben Schritten exportieren.
{{% /details %}}

{{% details title="Funktioniert meine M3U-Wiedergabeliste auf anderen Geräten?" closed="true" %}}
Wenn Sie beim Export die Option Absolute URL wählen, kann die M3U-Datei auf jedem Gerät abgespielt werden, das M3U-Wiedergabelisten unterstützt. Beachten Sie, dass einige Cloud-URLs im Laufe der Zeit ablaufen können.
{{% /details %}}

{{% details title="Ist die Exportfunktion kostenlos?" closed="true" %}}
Ja. Der Export von Titelsammlungen in M3U, CSV und TXT ist sowohl in der kostenlosen als auch in der Premium-Version von Evermusic und Flacbox verfügbar.
{{% /details %}}

{{% details title="Welche Cloud-Dienste unterstützen den Export mit absoluter URL?" closed="true" %}}
Der Export mit absoluter URL wird für iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive und WebDAV (Gastmodus) unterstützt.
{{% /details %}}
