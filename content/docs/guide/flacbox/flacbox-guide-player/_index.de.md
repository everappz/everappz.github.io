---
title: "Audio-Player"
date: 2020-02-01
description: "Lernen Sie, wie Sie den Flacbox-Audio-Player auf iPhone, iPad und Mac verwenden. Steuern Sie die Wiedergabe, verwalten Sie Warteschlangen, konfigurieren Sie die FFmpeg / System-Audio-Engine, ändern Sie die Abtastrate, Tonhöhenkorrektur, IO-Pufferdauer, Equalizer, Audio-Lesezeichen, AirPlay 2, Google Cast, CarPlay, Widgets und Mac-Tastaturkürzel."
keywords: [
  "Flacbox Player-Anleitung", "Audio-Player Einstellungen", "Flacbox Equalizer",
  "AirPlay Musik-Streaming", "Google Cast Musik", "Audio-Lesezeichen",
  "Flacbox Wiedergabe-Warteschlange", "Flacbox Wiederholen Mischen", "Flacbox Lautstärkeregelung",
  "macOS Mini-Player", "VoiceOver Musik-App",
  "Flacbox FFmpeg", "Flacbox Tonhöhenkorrektur", "Flacbox Abtastrate",
  "Flacbox externer DAC", "Flacbox Surround-Sound", "Flacbox IO-Puffer",
  "Flacbox Wiedergabegeschwindigkeit", "Flacbox Einschlaf-Timer"
]
tags: ["anleitung", "flacbox", "player"]
readingTime: 14
---


Der Audio-Player ist der Hauptbildschirm der App, auf dem Sie die Musik steuern und die meisten Wiedergabefunktionen nutzen. Es ist auch der Ort, wo Flacbox's Hi-Res-Audio-Engine — aufgebaut auf den System-Codecs plus der integrierten **FFmpeg**-Bibliothek — die schwere Arbeit erledigt.

## Zugriff auf den Audio-Player

Sie können den Vollbild-Player über die Mini-Player-Leiste aufrufen. Auf iPhone befindet sich der Mini-Player am unteren Rand des Hauptbildschirms. Auf iPad und Mac befindet er sich auf der linken Seite. Um den Mini-Player auf iPhone auszublenden, tippen Sie einmal darauf und wischen Sie nach unten.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio-Player Hauptbildschirm" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Unterstützte Audioformate

Flacbox spielt die beliebtesten Audioformate ab — sowohl Apples System-Codecs als auch viele weitere Formate, die von der integrierten FFmpeg-Engine verarbeitet werden:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

## Wiedergabesteuerung

Am unteren Rand des Player-Bildschirms sehen Sie Tasten für Wiedergabe, Pause, Nächster Titel und Vorheriger Titel. Es gibt auch optionale Tasten für Vorwärts 30 Sek. und Zurück 30 Sek. Um zu einem bestimmten Teil eines Titels zu springen, ziehen Sie den Wiedergabe-Schieberegler.

## Wiederholen und Mischen

Tippen Sie auf die Wiederholen-Taste, um durch die Wiederholungsmodi zu wechseln:

- **Alle wiederholen** — alle Titel in der Warteschlange in einer Schleife abspielen.
- **Einen wiederholen** — nur den aktuellen Titel wiederholen.
- **Wiederholen stoppen** — pausiert, wenn der aktuelle Titel endet.
- **Nicht wiederholen** — spielt die Warteschlange einmal durch ohne Wiederholung.

Verwenden Sie die **Mischen**-Taste, um die Reihenfolge der Titel in der Warteschlange zufällig zu gestalten.

## Lautstärkeregelung

Öffnen Sie den Audio-Einstellungen-Bildschirm durch Tippen auf das Sound-Symbol unter den Wiedergabekontrollen, um den Lautstärke-Schieberegler aufzurufen. Hier finden Sie auch Schaltflächen für **Google Cast** und **AirPlay**.

## Google Cast (Chromecast)

Das **Cast**-Symbol erscheint am unteren Rand des Players. Tippen Sie darauf, um ein Gerät auszuwählen und das Streaming zu starten. Stellen Sie sicher, dass Ihr Gerät und der Google Cast-Empfänger im selben Wi-Fi-Netzwerk sind.

## AirPlay

Für AirPlay tippen Sie auf die **AirPlay**-Schaltfläche am unteren Rand des Players. Flacbox unterstützt **AirPlay 2**, sodass Sie auf mehrere HomePods, Apple TVs oder AirPlay-2-kompatible Lautsprecher gleichzeitig abspielen können.

## Audio-Equalizer

Flacbox enthält einen **10-Band-Equalizer** mit iPod-artigen Presets. Tippen Sie auf „Equalizer" in der Lautstärkeansicht, schalten Sie ihn dann oben rechts ein. Wir haben detailliertere Anweisungen zur Verwendung des Equalizers [hier](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio-Player Equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Player-Modus-Symbolleiste

Für einige Player-Stile gibt es eine dedizierte Symbolleiste am oberen Rand des Vollbild-Players mit drei nützlichen Schaltflächen:

- **Suchen** — schnell einen bestimmten Titel in der Player-Warteschlange finden.
- **Wiedergabegeschwindigkeits-Steuerung** — Wiedergabegeschwindigkeit von 0,02× bis 3,00× anpassen.
- **Audio-Lesezeichen** — mehrere Lesezeichen pro Titel erstellen. Wir haben vollständige Anweisungen [hier](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Player-Warteschlange

Um Ihre Player-Warteschlange anzuzeigen, tippen Sie auf die Warteschlange-Schaltfläche rechts neben dem aktuellen Song. Jeder Song in der Warteschlange hat weitere Aktionen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wiedergabe-Warteschlange" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Kommentare / Liedtexte

Um Track-Kommentare und eingebettete Liedtexte sowie LRC-Dateien anzuzeigen:

1. Öffnen Sie **Einstellungen**.
2. Gehen Sie zu **Audio-Player**.
3. Wählen Sie **Personalisierung**.
4. Tippen Sie auf **Schaltflächen auf dem Hauptbildschirm**.
5. Aktivieren Sie **Kommentare**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Liedtexte und Kommentare Bildschirm" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Optionsmenü

Jeder Song in der Audio-Player-Warteschlange hat ein Menü mit weiteren Aktionen:

- **Weiter abspielen** — fügt den Song oben in die Warteschlange hinzu.
- **Zur Playlist hinzufügen** — schließt den Song in eine Playlist ein.
- **Zu Favoriten hinzufügen** — markiert den Song als Favorit.
- **Herunterladen** — speichert den Song in lokalen Dateien.
- **Audio-Tags bearbeiten** — öffnet den integrierten Audio-Tags-Editor.
- **Im Ordner anzeigen** — zeigt den Ordner, in dem die Audiodatei gespeichert ist.
- **Im Finder anzeigen** — für importierte Mac-Dateien zeigt den Ordner auf dem Mac.
- **Öffnen in** — exportiert die Audiodatei in eine andere App.
- **Aus der Warteschlange entfernen** — entfernt den ausgewählten Song aus der Warteschlange.
- **Aus Cloud-Dienst löschen** — löscht den Song aus der Bibliothek und dem Cloud-Speicher. **Diese Aktion ist irreversibel.**
- **Aus lokalen Dateien löschen** — löscht den Song aus der Bibliothek und dem lokalen Speicher. **Diese Aktion ist irreversibel.**
- **Aus Musikbibliothek löschen** — löscht den Song aus Ihrer Bibliothek, während die Datei im Speicher verbleibt.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Optionen für ein Element in der Wiedergabe-Warteschlange" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Zusätzliche Player-Aktionen

Tippen Sie auf die **Weitere Aktionen** „..."-Schaltfläche auf der linken Seite des aktuell abgespielten Song-Titels, um zusätzliche Aktionen zu sehen:

- **Wiedergabe fortsetzen** — genau da weitermachen, wo Sie aufgehört haben.
- **Suchen** — schnell einen bestimmten Titel in der Warteschlange finden.
- **Lesezeichen** — Ihre Liste der erstellten Audio-Lesezeichen anzeigen.
- **Kommentare** — Track-Kommentare und eingebettete Liedtexte anzeigen.
- **Geschwindigkeit** — die Wiedergabegeschwindigkeit anpassen.
- **Aktuell** — auf eine Liste der zuletzt gespielten Songs zugreifen.
- **Favoriten** — Ihre Sammlung der favorisierten Songs anzeigen.
- **Audio-Equalizer** — den Audio-Equalizer aktivieren.
- **Einschlaf-Timer** — einen Timer einstellen, um die Wiedergabe nach einem bestimmten Intervall zu stoppen.
- **Warteschlange als Playlist speichern** — die aktuelle Audio-Player-Warteschlange als neue Playlist speichern.
- **Warteschlange löschen** — Ihre Player-Warteschlange leeren und die Wiedergabe stoppen.
- **Einstellungen** — auf Audio-Player-Einstellungen zugreifen.
- **Hilfe** — Hilfe und Anleitung finden.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio-Player Weitere Aktionen Bildschirm" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Audio-Lesezeichen

Mit dieser Funktion können Sie mehrere Lesezeichen für Titel in Ihrer Musikbibliothek erstellen — perfekt für Hörbücher, Vorlesungen, lange DJ-Mixes oder das Markieren des Refrains eines Lieblingslieds.

So erstellen Sie ein neues Lesezeichen:

- Beginnen Sie mit dem Abspielen des gewünschten Songs.
- Öffnen Sie den Player-Bildschirm.
- Tippen Sie auf die **Lesezeichen**-Schaltfläche in der Player-Modus-Symbolleiste.
- Wählen Sie **Lesezeichen hinzufügen**.
- Wählen Sie die Lesezeichenzeit und tippen Sie oben rechts auf **Fertig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio-Lesezeichen Bildschirm" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Aktuell und Favoriten

Auf dem Player-Bildschirm tippen Sie auf die drei Punkte, um auf Aktuell und Favoriten zuzugreifen. Wir haben detaillierte Anweisungen, wie Sie Song-Listen exportieren können [hier](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Verbinden Sie Ihr iPhone über USB oder kabelloses Apple CarPlay mit Ihrem Auto, und Flacbox erscheint auf Ihrem CarPlay-Startbildschirm. Konfigurieren Sie das CarPlay-Erlebnis in **Einstellungen → CarPlay**.

[Lesen Sie den vollständigen CarPlay-Leitfaden](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox auf Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Home-Screen-Widgets (iPhone & iPad)

Flacbox unterstützt iOS Home-Screen- und Sperrbildschirm-Widgets. Stellen Sie sicher, dass Widgets in **Einstellungen → Widgets → Widgets aktivieren** aktiviert sind, dann drücken Sie lange auf Ihren Home-Screen oder Sperrbildschirm, tippen Sie auf **+**, suchen Sie nach **Flacbox** und fügen Sie ein Widget hinzu.

## Mini-Player-Fenster (nur Mac)

Mac-Benutzer können einen kompakten, immer-oben-liegenden Mini-Player verwenden.

## Tastaturkürzel (nur Mac)

Für Mac-Benutzer ist ein System-Wiedergabemenü in der Statusleiste mit Tastaturkürzeln verfügbar. Drücken Sie zum Beispiel die Leertaste zum Abspielen / Pausieren.

## Audio-Player-Einstellungen

Um auf die Einstellungen zuzugreifen, tippen Sie auf die Mehr-Schaltfläche auf dem Player-Bildschirm und wählen Sie Einstellungen.

### Allgemein

- **Wiederholungsmodus** — wählen Sie das Verhalten: Alle wiederholen, Einen wiederholen, Wiederholen stoppen, Nicht wiederholen.
- **Misch-Modus** — randomisieren Sie die Reihenfolge der Titel: **Mischen aus** oder **Mischen ein**.
- **Audio-Codec** — wählen Sie die Audio-Engine: **System-Codec + FFmpeg** oder **FFmpeg**.
- **Audio-Ausgabe Abtastrate** — verfügbare Werte: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** und **96 kHz**.
- **Audio-Ausgabe Kanalanzahl** — für Mehrkanal-Audiosysteme: **Mono, Stereo, Center / Links / Rechts, Center / Links / Rechts / Surround, ITU BS.775-1, 5.1 Surround** und **SDDS**.
- **Audio-Ausgabe Bevorzugte IO-Pufferdauer** — konfigurieren Sie die IO-Pufferdauer. Ein typischer Wert für minimale Latenz ist etwa **5 Millisekunden (0,005 Sekunden)**.
- **Audio-Ausgabe Modus (nur iOS)** — konfigurieren Sie den gemischten Audio-Ausgabemodus.
- **Wiedergabeposition speichern** — speichert und stellt die Wiedergabeposition für Songs wieder her.
- **Audio-Player-Status speichern** — bewahrt den Audio-Player-Status vor dem Schließen der App.

### Personalisierung

- **Audio-Player-Bildschirm-Stil** — konfigurieren Sie die Positionierung der Elemente auf dem Audio-Player-Bildschirm.
- **Album-Cover-Scroll-Stil** — konfigurieren Sie den bevorzugten Scroll-Stil für Album-Cover.
- **Zusätzliche Elemente** — aktivieren Sie zusätzliche Elemente auf dem Audio-Player-Bildschirm.
- **Hauptbildschirm-Aktionen** — konfigurieren Sie, welche Schaltflächen auf dem Hauptbildschirm sichtbar sein sollen.
- **Wiedergabesteuerung auf dem Sperrbildschirm** — wählen Sie, welche Steuerelemente auf dem Sperrbildschirm erscheinen.
- **Sprung-Zeit-Schaltflächen** — wählen Sie das Zeitintervall für die Sprung-Zeit-Schaltflächen.

### Datei-Laden

- **Vorladezeit** — legen Sie das Puffer-Zeitintervall fest.
- **Direkte URL verwenden** — wenn aktiviert, wird eine direkte URL zum Laden des Songs verwendet.

### Audio-Equalizer

Passen Sie die Audio-Equalizer-Einstellungen an. Mehr über die Konfiguration des Audio-Equalizers [hier](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Wiedergabegeschwindigkeit

Passen Sie die Wiedergabegeschwindigkeit von **0,02× bis 3,00×** an.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wiedergabegeschwindigkeit Bildschirm" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Tonhöhenkorrektur

Ändern Sie die Tonhöhenkorrektur-Einstellungen. Die Tonhöhenkorrektur ist im FFmpeg-Codec-Pfad verfügbar, mit einem Bereich von **-1000 bis +1000**.

### Wiedergabe-Cache

Songs in der Audio-Player-Warteschlange werden automatisch heruntergeladen, um eine reibungslose Wiedergabe zu gewährleisten. Sie können hier auch die Cache-Größe konfigurieren.

### Einschlaf-Timer

Aktivieren Sie einen Timer, um die Wiedergabe nach einem bestimmten Zeitraum automatisch zu stoppen.

## Barrierefreiheit

Flacbox ist vollständig mit **VoiceOver** zugänglich. Wenn VoiceOver aktiv ist, wechselt die App in den **Text-Modus**. Sie können Text-Modus auch in **Einstellungen → Barrierefreiheit → Text-Modus** aktivieren.

### Slider mit VoiceOver anpassen

1. **Slider auswählen** — nach links oder rechts wischen, bis VoiceOver ihn ansagt.
2. **Wert anpassen** — doppeltippen und Slider festhalten, dann nach oben oder unten ziehen.

### Titelposition in einer Liste mit VoiceOver anpassen

1. Tippen Sie auf das Neuanordnungs-Symbol neben dem Titel.
2. Doppeltippen Sie schnell auf das Neuanordnungs-Symbol. Beim zweiten Tippen halten Sie den Finger.
3. Verschieben Sie die Zelle an ihre neue Position.
