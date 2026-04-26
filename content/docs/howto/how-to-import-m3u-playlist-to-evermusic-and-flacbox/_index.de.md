---
title: "So importieren Sie eine M3U-Wiedergabeliste in Evermusic und Flacbox"
date: 2024-01-31
description: "Erfahren Sie, wie Sie M3U-, M3U8- und CUE-Wiedergabelistendateien aus der Cloud, dem lokalen Speicher oder Ihrem Gerät in Evermusic und Flacbox importieren."
keywords: ["evermusic", "flacbox", "Wiedergabeliste", "m3u", "m3u8", "cue", "importieren", "Musik-App"]
tags: ["evermusic", "importieren", "Wiedergabelisten", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Zusammenfassung:** Evermusic und Flacbox unterstützen den Import von M3U-, M3U8- und CUE-Wiedergabelistendateien aus Cloud-Speicher, lokalen App-Dateien oder Ihrem Gerät. Gehen Sie zu Wiedergabelisten > Mehr > Wiedergabeliste importieren, wählen Sie eine Quelle, wählen Sie Ihre Datei, und die App erstellt Ihre Wiedergabeliste automatisch.

M3U, was für MP3 URL oder Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator steht, ist ein Computerdateiformat für Multimedia-Wiedergabelisten. Eine der Hauptverwendungen ist die Erstellung von Wiedergabelistendateien mit einem einzelnen Eintrag, die auf Streams im Internet verweisen. Diese Dateien bieten bequemen Zugang zu Streaming-Inhalten und werden häufig für Downloads, E-Mails und das Hören von Internetradio verwendet.

Trotz seiner weit verbreiteten Nutzung gibt es keine formale Spezifikation für das M3U-Format; es ist zum De-facto-Standard geworden. Eine M3U-Datei ist im Wesentlichen eine reine Textdatei, die die Speicherorte einer oder mehrerer Mediendateien angibt. Je nach Kodierung wird sie mit der Dateierweiterung "m3u" oder "m3u8" gespeichert. Jeder Eintrag in der Datei gibt den Speicherort einer Mediendatei an, der ein absoluter lokaler Pfadname, ein lokaler Pfadname relativ zum Speicherort der M3U-Datei oder eine URL sein kann. Einträge werden durch Zeilenumbrüche getrennt, wobei einige Geräte Zeilenumbrüche als CR LF erfordern.

Zusätzlich können M3U-Dateien Kommentare enthalten, die mit dem Zeichen "#" eingeleitet werden. Im erweiterten M3U führt "#" erweiterte M3U-Direktiven ein, die Parameter unterstützen können, die mit einem Doppelpunkt ":" abgeschlossen werden.

In unseren Apps Evermusic und Flacbox haben wir eine M3U-Dateiimportfunktion implementiert, die das manuelle Erstellen von Wiedergabelisten überflüssig macht. Diese Anleitung führt Sie durch den Import Ihrer Wiedergabelisten aus Cloud-Speicher, lokalen Dateien oder Dateien auf Ihrem Gerät direkt in die App.

Navigieren Sie zunächst zum Bereich 'Wiedergabelisten'. Tippen Sie dann auf die Schaltfläche 'Mehr' in der oberen rechten Ecke. Wählen Sie aus dem erscheinenden Menü die Option 'Wiedergabeliste importieren'.

![Wiedergabeliste importieren Aktion](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Wählen Sie auf dem nächsten Bildschirm den Dateispeicherort. Unterstützte Optionen sind:

- Verbundener Cloud-Speicher;
- Dateien in der Anwendung;
- Dateien auf Ihrem Gerät;

![Dateispeicherort auswählen](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Wählen wir den verbundenen Cloud-Speicher und öffnen den Ordner, der die Wiedergabelistendatei enthält. Unterstützte Dateierweiterungen für Wiedergabelisten sind M3U, M3U8 und CUE. Wählen Sie die Wiedergabelistendatei und tippen Sie auf 'Fertig', um Ihre Auswahl zu bestätigen.

![M3U-Datei auswählen](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Die App wird die Wiedergabelistendatei analysieren und eine Titelliste erstellen. Anschließend werden die Dateien im Speicher gefunden und eine endgültige Wiedergabeliste zusammengestellt, die in die Musikbibliothek importiert wird. Es ist entscheidend, dass Ihre M3U/CUE-Datei die korrekten Pfade für Mediendateien enthält und die Dateien sich an diesen Pfaden in Ihrem Speicher befinden.

![Importierte Wiedergabeliste](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Die App unterstützt sowohl relative Pfade als auch absolute Datei-URLs.

Zum Beispiel:

Wiedergabeliste mit relativen Pfaden:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Wiedergabeliste mit absoluten URLs:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Wenn Sie eine Wiedergabelistendatei importieren, die sich in der App befindet (Bereich Lokale Dateien), sind keine zusätzlichen Schritte erforderlich.

Wenn Sie jedoch eine Wiedergabeliste importieren möchten, die sich auf Ihrem Gerät befindet und den Systemdateiauswahldialog verwenden, gibt es eine wichtige Überlegung zu beachten.

Aufgrund von Sicherheitsrichtlinien kann die Anwendung nur auf die Datei zugreifen, die Sie über den Systemdateiauswahldialog auswählen. Die Wiedergabelistendatei kann jedoch Links zu anderen Mediendateien auf Ihrem Gerät enthalten. Um eine Wiedergabeliste von Ihrem Gerät zu importieren, müssen Sie einen Ordner auswählen, der sowohl die Wiedergabelistendatei als auch alle verknüpften Mediendateien enthält. In diesem Fall scannt die App den ausgewählten Ordner, findet die Wiedergabelistendatei, erstellt die Titelliste und importiert sie in die Musikbibliothek.

Außerdem können Sie mehrere Wiedergabelisten gleichzeitig importieren, indem Sie auf die Schaltfläche "Weitere Aktionen" tippen und "Wiedergabelisten aus einem Ordner importieren" auswählen. Die App scannt dann den Inhalt des Ordners, findet unterstützte Wiedergabelistendateien und importiert sie in die Bibliothek.

## Häufig gestellte Fragen

{{% details title="Welche Wiedergabelistenformate unterstützen Evermusic und Flacbox?" closed="true" %}}
Beide Apps unterstützen die Dateiformate M3U, M3U8 und CUE für Wiedergabelisten. Diese decken die gängigsten Wiedergabelistenstandards ab, die von Musikplayern und Mediensoftware verwendet werden.
{{% /details %}}

{{% details title="Kann ich Wiedergabelisten aus Cloud-Speicher importieren?" closed="true" %}}
Ja. Sie können Wiedergabelistendateien von jedem verbundenen Cloud-Speicherdienst importieren, einschließlich Google Drive, Dropbox, OneDrive und WebDAV-Server.
{{% /details %}}

{{% details title="Warum fehlen nach dem Import einige Titel?" closed="true" %}}
Die Wiedergabelistendatei muss korrekte Pfade zu Ihren Mediendateien enthalten, und diese Dateien müssen an den angegebenen Speicherorten in Ihrem Speicher vorhanden sein. Überprüfen Sie, ob die Dateipfade in Ihrer M3U- oder CUE-Datei mit den tatsächlichen Dateispeicherorten übereinstimmen.
{{% /details %}}

{{% details title="Kann ich mehrere Wiedergabelisten gleichzeitig importieren?" closed="true" %}}
Ja. Verwenden Sie die Schaltfläche Weitere Aktionen und wählen Sie "Wiedergabelisten aus einem Ordner importieren". Die App durchsucht den Ordner nach allen unterstützten Wiedergabelistendateien und importiert sie in einem Schritt.
{{% /details %}}

{{% details title="Muss ich Wiedergabelisten manuell erstellen?" closed="true" %}}
Nein. Die Importfunktion macht das manuelle Erstellen von Wiedergabelisten überflüssig. Verweisen Sie die App einfach auf Ihre vorhandene M3U-, M3U8- oder CUE-Datei, und sie erstellt die Wiedergabeliste automatisch.
{{% /details %}}
