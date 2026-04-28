---
title: "Exportieren Sie Ihren vollständigen Hörverlauf von Evermusic und Flacbox zu Last.fm"
date: 2024-01-30
description: "Erfahren Sie, wie Sie Ihren Musikverlauf aus Evermusic und Flacbox exportieren und mit CSV-Dateien und dem Last.fm Scrubbler-Tool für Windows auf Last.fm hochladen."
keywords: ["evermusic", "flacbox", "lastfm", "Musikverlauf", "Scrobbling", "Titel exportieren", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "aktuell", "lastfm", "export", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Zusammenfassung:** Exportieren Sie Ihren Hörverlauf aus Evermusic oder Flacbox als CSV-Datei und laden Sie ihn dann mit dem kostenlosen Tool Last.fm-Scrubbler-WPF unter Windows auf Last.fm hoch. Automatisches Scrobbling ist auch nativ in beiden Apps verfügbar.

**Update:** Automatisches Scrobbling ist jetzt verfügbar! Erfahren Sie mehr hier: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling ist eine einfache Möglichkeit, grundlegende Details wie den Titel und Künstler des Songs, den Sie gerade hören, automatisch in einem Online-Dienst zu speichern. Später können Sie Ihren Hörverlauf überprüfen.

[Last.fm](https://www.last.fm/home), betrieben von einem Musikempfehlungssystem namens Audioscrobbler, bietet diesen Dienst kostenlos an. Es erstellt ein detailliertes Profil Ihres Musikgeschmacks, indem es die Titel aufzeichnet, die Sie hören, sei es von Internetradiosendern, Ihrem Computer oder verschiedenen tragbaren Musikgeräten. Sie können die Website später besuchen, um Empfehlungen für neue Künstler oder Alben zu erhalten, die Ihrem Musikgeschmack entsprechen.

Sie können Ihren Hörverlauf von den Evermusic- und Flacbox-Apps mit einem kostenlosen Tool auf [Last.fm](http://Last.fm) hochladen, und wir führen Sie durch den Prozess.

Öffnen Sie den Bereich 'Musikbibliothek' der Anwendung und scrollen Sie zum Bereich 'Schnellzugriff'. Tippen Sie auf den Menüpunkt 'Aktuell'.

![Musikbibliothek-Bildschirm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Auf dem Bildschirm 'Aktuell' tippen Sie auf die Schaltfläche 'Mehr' in der oberen rechten Ecke, um das Menü 'Weitere Aktionen' zu aktivieren. Tippen Sie auf den Menüpunkt 'Songliste exportieren'.

![Aktuell-Bildschirm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Auf dem Bildschirm 'Dateiformat wählen' haben Sie die Möglichkeit, das Format der Zieldatei auszuwählen. Verfügbare Optionen - CSV, TXT, M3U.

![Dateiformat wählen Bildschirm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Steht für kommagetrennte Werte, perfekt zum Organisieren Ihrer Daten in einem übersichtlichen Tabellenformat. In der Zieldatei finden Sie Parameter wie Künstlername, Albumname, Titelname, Zeitstempel (die Zeit, zu der Sie die Titel gehört haben), Album-Künstlername und Titeldauer.

TXT: Hier sprechen wir über eine reine Textdatei. Sie ist einfach und unkompliziert, mit Parametern wie Künstlername, Albumname, Titelname und Dauer.

M3U: Dieses Format ist im Wesentlichen der Standard für die Erstellung von Playlisten. Es ist großartig, weil Sie Ihre Songliste exportieren und Ihre Titel auf jedem Gerät genießen können, selbst wenn Sie nicht die Originaldateien haben (vorausgesetzt, Sie wählen die Option der absoluten URL für Mediendateien). In der Ausgabedatei finden Sie Parameter wie Dauer, Künstlername, Titelname und Mediendatei-Speicherort.

Für unsere Aufgabe ist die Auswahl von CSV der richtige Weg. Wir werden diese Datei mit der kostenlosen Software Last.fm-Scrubbler-WPF verwenden, um unseren Hörverlauf auf den [Last.fm](http://Last.fm)-Dienst hochzuladen. Wählen Sie einfach CSV und drücken Sie die Schaltfläche 'Exportieren'.

![Export abgeschlossen Bildschirm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Nach Abschluss des Exports tippen Sie einfach auf die Schaltfläche 'Datei anzeigen', und die App zeigt die erstellte Datei in Ihrem Dokumentenordner an. Tippen Sie dann auf die Schaltfläche 'Weitere Aktionen' neben dem Dateinamen und wählen Sie die Option 'Öffnen in' aus dem Menü. Unser nächster Schritt ist, die exportierte Datei auf Ihren Desktop-Computer zu kopieren. Sie können dies einfach tun, indem Sie die AirDrop-Option aus dem Menü 'Öffnen in' auswählen.

![Weitere Aktionen für exportierte Datei](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Als Nächstes verwenden wir einen kostenlosen Open-Source [Last.FM](http://Last.FM)-Client, der nur auf der Windows-Plattform verfügbar ist. Dieser Client ermöglicht es Ihnen, Ihren Hörverlauf auf [Last.FM](http://Last.FM) effizient mit der CSV-Datei zu aktualisieren, die wir gerade exportiert haben.

Wenn Sie derzeit keinen Windows-Computer verwenden, keine Sorge. Sie können auf diesen Client zugreifen, indem Sie VirtualBox auf Ihrem Mac installieren und die offizielle Windows-Entwicklungsumgebungs-Imagedatei verwenden.

Folgendes müssen Sie tun:

- Installieren Sie VirtualBox über folgenden Link: [VirtualBox herunterladen](https://www.virtualbox.org/wiki/Downloads)

- Laden Sie die Windows-Entwicklungsumgebung von diesem Link herunter und installieren Sie sie: [Windows-Entwicklungsumgebung](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Auf Ihrem Windows-Computer (oder der VirtualBox-App mit Windows Development-Image) laden Sie [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) herunter und installieren Sie es - kostenlose Open-Source-Software verfügbar auf GitHub. Wir haben Version 1.28 getestet, die Sie hier herunterladen können: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Last.fm-Scrubbler-WPF Download-Seite](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Unter dem Abschnitt 'Assets' klicken Sie auf [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip), um das Installationsarchiv herunterzuladen. Entpacken Sie die heruntergeladene Datei und öffnen Sie den entpackten Ordner.

- WICHTIG

Diese App befindet sich noch in der Beta-Phase. Die App-Ersteller haben nicht viel getestet. Sie empfehlen, zuerst an einem Testkonto zu scrobbeln und zu prüfen, ob die Dinge, die Sie scrobbeln möchten, korrekt funktionieren. Besonders wenn Sie viele Titel auf einmal scrobbeln. Bitte seien Sie vorsichtig mit Ihren Konten.

Starten Sie Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Auf dem Hauptbildschirm der Anwendung tippen Sie einfach auf 'Nicht angemeldet' in der unteren linken Ecke, um den Bildschirm 'Konto hinzufügen' zu aktivieren.

![Konto hinzufügen Bildschirm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Geben Sie Ihre Anmeldedaten ein.

![Anmeldedaten eingeben Bildschirm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Tippen Sie auf die Schaltfläche 'Anmelden', um Ihr Konto hinzuzufügen.

![Tippen Sie auf die Schaltfläche Anmelden, um Ihr Konto hinzuzufügen.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Öffnen Sie den Tab 'File Parse Scrobbler', um mit dem Import der CSV-Datei aus der Evermusic-App zu beginnen.

![Öffnen Sie den Tab File Parse Scrobbler, um mit dem Import der CSV-Datei aus der Evermusic-App zu beginnen.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Wählen Sie 'Parser: CSV' und tippen Sie auf die Schaltfläche 'Einstellungen'.

Auf dem nächsten Bildschirm können Sie die Reihenfolge der Parameter in Ihrer CSV-Datei wählen.

Einzelne Felder können in Anführungszeichen eingeschlossen sein und MÜSSEN in Anführungszeichen eingeschlossen sein, wenn das Feld eines der festgelegten Trennzeichen enthält. Zum Beispiel:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Lassen Sie also alle Einstellungen auf Standard, das Einzige, was Sie ändern müssen, ist das Aktivieren des Kontrollkästchens im Feld 'Has Fields Enclosed In Quotes'.

Tippen Sie auf 'Speichern und Schließen', um die Änderungen anzuwenden.

![Wählen Sie die Reihenfolge der Parameter in Ihrer CSV-Datei.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Das Dateianalyse-Scrobbling hat zwei Modi. Sie können mit der 'Scrobbling Mode'-Dropdown-Box geändert werden.

Normaler Modus: In diesem Modus werden die Titel mit dem Zeitstempel des analysierten Scrobbles gescrobbelt. Nur Scrobbles, die neuer als 14 Tage sind, können gescrobbelt werden.

Import-Modus: In diesem Modus werden die Titel mit dem Zeitstempel gescrobbelt, der aus der 'Endzeit' und der ausgewählten Dauer zwischen jedem Titel berechnet wird. Dies ermöglicht das Scrobbeln der Titel, auch wenn der Zeitstempel des analysierten Scrobbles älter als 14 Tage ist. Daher wird der erste (oberste) Titel in der CSV-Datei mit der 'Endzeit' gescrobbelt.

Wählen Sie eine zuvor generierte CSV-Datei aus der Evermusic-App im Feld 'File:' und tippen Sie auf 'Parse'. In einigen Fällen sehen Sie möglicherweise eine Fehlermeldung, dass einige Scrobbles nicht analysiert werden konnten. Es ist in Ordnung, wenn einige Titel unvollständige Metadaten wie den Künstlernamen haben.

![Einige Scrobbles konnten nicht analysiert werden](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Tippen Sie auf die Schaltfläche 'Alle auswählen', um alle analysierten Titel auszuwählen.

![Tippen Sie auf die Schaltfläche Alle auswählen, um alle analysierten Titel auszuwählen.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Tippen Sie auf die Schaltfläche 'Vorschau', um alle Änderungen zu überprüfen, die an den Server gesendet werden.

![Tippen Sie auf die Schaltfläche Vorschau, um alle Änderungen zu überprüfen, die an den Server gesendet werden.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Tippen Sie auf die Schaltfläche 'Scrobble', um alle Änderungen auf den Server hochzuladen.

![Tippen Sie auf die Schaltfläche Scrobble, um alle Änderungen auf den Server hochzuladen.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Zuvor hatte Last.fm-Scrubbler-WPF kein tägliches Scrobble-Limit. Dies hat sich nun geändert, da einige Personen den Scrubbler zum Scrobbeln so vieler Titel verwendet haben, dass es Probleme für die Last.fm-Seite verursachte. Das Scrobble-Limit liegt derzeit bei 2800 Scrobbles pro Tag. Wenn Sie versuchen, mehr zu scrobbeln, erhalten Sie eine Fehlermeldung. Es gibt Pläne, eine 'Scrobble-Warteschlange' hinzuzufügen, sodass, wenn Sie mehr als 2800 Titel scrobbeln müssen, diese einer Warteschlange hinzugefügt und nach einiger Zeit automatisch gescrobbelt werden. Sie können in der Benutzerauswahlansicht überprüfen, wie viele Scrobbles Ihnen noch verbleiben.

Sobald alle Einträge erfolgreich auf den Server hochgeladen wurden, sehen Sie eine Nachricht am unteren Rand des App-Fensters mit der Bestätigung: 'Ausgewählte Titel erfolgreich gescrobbelt.'

![Ausgewählte Titel erfolgreich gescrobbelt.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Jetzt können Sie Ihr Profil auf der [Last.fm](http://Last.fm)-Seite öffnen und alle Änderungen überprüfen.

![Ihr Profil auf der Last.fm-Seite](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Häufig gestellte Fragen

{{% details title="Kann ich automatisch scrobbeln, ohne CSV-Dateien zu exportieren?" closed="true" %}}
Ja. Sowohl Evermusic als auch Flacbox unterstützen jetzt automatisches Last.fm-Scrobbling. Siehe die Anleitung: [So scrobbeln Sie zu Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Was wenn meine CSV Titel enthält, die älter als 14 Tage sind?" closed="true" %}}
Verwenden Sie den Import-Modus in Last.fm-Scrubbler-WPF. Er berechnet Zeitstempel aus der Endzeit neu, sodass Sie Titel unabhängig von ihrem ursprünglichen Datum scrobbeln können.
{{% /details %}}

{{% details title="Ich habe keinen Windows-Computer. Kann ich Last.fm-Scrubbler trotzdem verwenden?" closed="true" %}}
Ja. Installieren Sie VirtualBox auf Ihrem Mac und laden Sie das kostenlose Windows-Entwicklungsumgebungs-Image von Microsoft herunter. Führen Sie Last.fm-Scrubbler-WPF in der virtuellen Maschine aus.
{{% /details %}}

{{% details title="Warum werden einige Scrobbles nicht analysiert?" closed="true" %}}
Titel, denen wesentliche Metadaten fehlen (wie der Künstlername), können nicht analysiert werden. Dies ist zu erwarten und hat keinen Einfluss auf andere Titel in der Datei.
{{% /details %}}

{{% details title="Gibt es ein tägliches Scrobble-Limit?" closed="true" %}}
Ja. Last.fm-Scrubbler-WPF erlaubt bis zu 2.800 Scrobbles pro Tag. Wenn Sie mehr scrobbeln müssen, verteilen Sie den Prozess auf mehrere Tage.
{{% /details %}}
