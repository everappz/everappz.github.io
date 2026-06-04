---
title: "Media Player"
date: 2020-02-01
lastmod: 2026-06-01
description: "Erfahren Sie, wie Sie den Evervideo Media Player auf iPhone, iPad und Mac verwenden. Picture-in-Picture, hardwarebeschleunigte H.264/HEVC-Dekodierung, Audio- und Video-Equalizer, primäre und sekundäre Untertitel, Audio- und Videospurauswahl, Video-Skalierung und -Rotation, Wiedergabegeschwindigkeit, Schlaf-Timer, AirPlay 2, Google Chromecast, RTSP-Streams und der kompakte Always-on-Screen-Player."
keywords: [
  "Evervideo Player Anleitung", "Videoplayer Einstellungen", "Evervideo Equalizer",
  "Picture-in-Picture iPhone", "PiP Video iPad", "PiP Video Mac",
  "AirPlay 2 Video", "Google Chromecast Video",
  "Video Untertitel iPhone", "externe SRT Untertitel",
  "ASS SSA Untertitel Player", "libass iOS",
  "duale Untertitel Sprachlernen",
  "Video Equalizer Helligkeit Kontrast", "Audio Equalizer Videoplayer",
  "Videoplayer Rotation sperren", "Video Skalierungsmodus iOS",
  "Hardware H.264 Decoder iPhone", "Hardware HEVC Decoder iPad",
  "Wiedergabegeschwindigkeit Video", "FFmpeg Videoplayer iOS",
  "RTSP iPhone Player", "kompakter Videoplayer",
  "VR 360 Videoplayer iPhone"
]
tags: ["Anleitung", "evervideo", "Player", "PiP", "Untertitel", "Video Equalizer"]
readingTime: 14
---


Der Media Player ist der Hauptbildschirm der App, auf dem Sie die Wiedergabe und die meisten Funktionen von Evervideo steuern. Er spielt sowohl Video- als auch Audiodateien ab und basiert auf einem benutzerdefinierten FFmpeg-Player mit hardwarebeschleunigter H.264- und HEVC-Dekodierung. Erkunden wir, wie man ihn verwendet.

## Zugriff auf den Media Player

Sie gelangen zum Vollbild-Player über die kompakte Player-Leiste. Auf iPhone befindet sich der kompakte Player oben auf dem Hauptbildschirm. Auf iPad und Mac ist er auf der linken Seite (oder oben im Hauptbereich). Um den Vollbild-Player wieder in die kompakte Ansicht zu reduzieren, tippen Sie auf die Schließen-Schaltfläche in der unteren rechten Ecke oder wischen Sie nach unten. Um den kompakten Player vollständig auszublenden, tippen und wischen Sie noch einmal nach unten.

Der kompakte Player bleibt sichtbar, während Sie Ihre Mediathek, Ihren Dateimanager oder Ihre Einstellungen durchsuchen, sodass Sie Ihr Video nie verlieren, während Sie nach dem nächsten suchen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Vollbild-Media-Player" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Unterstützte Video- und Audioformate

Evervideo spielt praktisch jeden modernen Container und Codec über die mitgelieferte FFmpeg-Engine ab, mit hardwarebeschleunigter H.264- und HEVC-Dekodierung auf unterstützten Geräten.

- **Video-Container:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — und viele mehr.
- **Video-Codecs:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus praktisch jeder andere Codec, den FFmpeg unterstützt.
- **Audio-Codecs:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — und viele mehr.
- **Untertitelformate:** SRT, VTT (WebVTT), ASS / SSA und eingebettete Text- oder Bild-Untertitelspuren.
- **Streaming-Protokolle:** HTTP / HTTPS, HLS (m3u8), RTSP (IP-Kameras und IPTV) und direktes Datei-Streaming über SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Das deckt praktisch jede Videodatei ab, der Sie begegnen werden — einschließlich MKV-Rips, Sicherheitskamera-RTSP-Streams und AV1-WebM-Web-Downloads.

## Wiedergabesteuerungen

Am unteren Ende des Player-Bildschirms sehen Sie Schaltflächen für Wiedergabe, Pause, Weiter und Zurück. Es gibt auch optionale Schaltflächen wie Vorwärts springen und Rückwärts springen (Standard 10 Sekunden), die Sie in den App-Einstellungen aktivieren können. Halten Sie die Weiter- / Zurück-Schaltflächen gedrückt, um schnell vor- oder zurückzuspulen. Ziehen Sie den Wiedergabe-Schieberegler, um zu einer beliebigen Position zu springen.

## Wiederholen und Zufällig abspielen

Tippen Sie auf die Wiederholen-Schaltfläche, um zwischen den Wiederholungsmodi zu wechseln:

- **Alle wiederholen** — jeden Video in Ihrer Warteschlange wiederholen.
- **Eines wiederholen** — nur das aktuelle Video wiederholen.
- **Anhalten bei Ende** — pausieren, wenn das aktuelle Video endet.
- **Nicht wiederholen** — die Warteschlange einmal abspielen ohne zu wiederholen.

Verwenden Sie die **Zufällig**-Schaltfläche, um die Reihenfolge der Videos in der Warteschlange zu randomisieren.

## Picture-in-Picture (PiP)

Auf iPhone und iPad unterstützt Evervideo vollständig Picture-in-Picture (PiP). Tippen Sie auf das PiP-Symbol auf dem Player-Bildschirm oder wischen Sie Evervideo einfach in den Hintergrund — das Video läuft in einem schwebenden Fenster über jeder anderen App weiter. Ziehen Sie das schwebende Fenster in eine beliebige Ecke; zusammendrücken zum Verkleinern; einmal tippen, um grundlegende Wiedergabe- / Pause- / Überspringen-Steuerungen zu öffnen; tippen Sie auf die kleine Erweiterungsschaltfläche, um zu vollständigem Evervideo zurückzukehren.

PiP funktioniert mit jedem Videoformat, das Evervideo abspielt, einschließlich Cloud-gestreamter Dateien und RTSP-Streams. PiP läuft auch weiter, während Ihr Telefon gesperrt ist (abhängig von Ihrer Automatisch sperren-Einstellung).

## Kompakter Player

Der kompakte Player ist ein dauerhafter Mini-Player, der oben auf jedem Bildschirm in der App sichtbar bleibt, während Sie die Mediathek, den Dateimanager oder die Einstellungen durchsuchen. Tippen Sie darauf, um ihn auf den Vollbild-Player zu erweitern; nach unten wischen, um ihn wieder zu reduzieren.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Video-Einstellungen vom kompakten Player auf dem Hauptbildschirm" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Für AirPlay tippen Sie auf die AirPlay-Schaltfläche auf dem Player. Evervideo unterstützt AirPlay 2, sodass Sie Video an Apple TV, HomePod oder jeden AirPlay 2-kompatiblen Lautsprecher oder Smart TV streamen können. Bei einem Setup mit mehreren AirPlay-Geräten können Sie Audio gleichzeitig an mehrere Empfänger routen.

## Google Chromecast

Für Google Cast-Nutzer erscheint das Cast-Symbol auf dem Player. Tippen Sie darauf, um ein Gerät auszuwählen und das Casting zu starten. Stellen Sie sicher, dass Ihr Telefon und der Cast-Empfänger im selben Wi-Fi-Netzwerk sind. Nicht jeder Codec wird von der Chromecast-Hardware unterstützt — einige Dateien müssen möglicherweise transcodiert werden.

## RTSP Live-Streams

Evervideo kann RTSP-Quellen direkt abspielen — IP-Kameras, Türklingelkameras, IPTV-Streams, Sendungen und jede andere `rtsp://`-URL. Fügen Sie den Stream als RTSP-Verbindung in Dateien → Online-Links → Link hinzufügen ein, dann tippen Sie darauf, um mit dem Ansehen zu beginnen. RTSP-Streams funktionieren in Picture-in-Picture, dem kompakten Player und werden genau wie ein normales Video über AirPlay 2 und Chromecast übertragen.

## Audiospurauswahl

Für Videos mit mehreren Audiospuren (Kommentar, alternative Sprach-Synchronisierungen, Regisseursspuren) tippen Sie auf die Weitere Aktionen-Schaltfläche auf dem Player und wählen Sie Audiospur — dann wählen Sie die gewünschte Spur. Dies ist unerlässlich für fremdsprachige Filme, BDMV / MKV-Dateien mit mehreren Synchronisierungen und Lehrinhalt mit Kommentarspuren.

## Videospurauswahl

Einige Videodateien enthalten mehrere Videostreams (Multi-Winkel-Blu-rays, alternative Schnitte). Wählen Sie Videospur aus dem Weitere Aktionen-Menü, um während der Wiedergabe zwischen ihnen zu wechseln.

## Untertitel — Intern und Extern

Evervideo gibt Ihnen feinkörnige Kontrolle über Untertitel:

- **Untertitelspur** — aus den im File eingebetteten Spuren auswählen.
- **Externe Untertiteldateien** — `.srt`, `.vtt`, `.ass` oder `.ssa`-Dateien von Ihrem Gerät, iCloud Drive oder einem verbundenen Cloud-Dienst laden.
- **Libass-Rendering** — erweitertes ASS / SSA-Styling (Schriften, Farben, Positionen, Karaoke-Effekte) wird dank der mitgelieferten libass korrekt gerendert.
- **Schriftartauswahl** — wählen Sie eine benutzerdefinierte Schriftart für primäre Untertitel und eine separate Schriftart für sekundäre Untertitel. Mitgelieferte Schriftarten plus alle auf Ihrem Gerät installierten Schriftarten sind verfügbar.

Sie können all dies in Einstellungen → Untertitel vor der Wiedergabe konfigurieren oder Weitere Aktionen → Untertitel vom Player aus verwenden, um spontan zu wechseln.

## Audio-Equalizer

Evervideo enthält einen vollständigen Audio-Equalizer zum Abstimmen von Video-Soundtracks für Ihre Kopfhörer, Lautsprecher oder Hi-Fi-Setup. Tippen Sie auf das Equalizer-Symbol in der Lautstärkeanzeige (oder die Aktion Audio-Equalizer im Weitere Aktionen-Menü des Players), schalten Sie den Equalizer mit dem Schalter in der oberen rechten Ecke ein, und wählen Sie entweder ein Preset oder ziehen Sie die Band-Schieberegler, um Ihr eigenes Preset zu erstellen. Benutzerdefinierte Presets können exportiert und importiert werden, um sie über Geräte zu teilen oder zu sichern.

## Video-Equalizer

Zur Bildanpassung bietet Evervideo einen dedizierten Video-Equalizer — passen Sie Helligkeit, Kontrast, Sättigung und Farbton in Echtzeit während der Wiedergabe an. Wie der Audio-Equalizer können benutzerdefinierte Video-Presets für die gemeinsame Nutzung oder Sicherung exportiert und importiert werden. Verwenden Sie ihn, um eine dunkle Szene an einem sonnigen Tag aufzuhellen, die Sättigung bei ausgewaschenem Inhalt zu erhöhen oder eine kalte Farbtemperatur aufzuwärmen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Video-Equalizer" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Video-Skalierungsmodus

Wählen Sie, wie das Video den Bildschirm füllt:

- **Anpassen** — ursprüngliches Seitenverhältnis beibehalten; schwarze Balken wo nötig.
- **Füllen** — den gesamten Bildschirm füllen, das Video bei Bedarf beschneiden.
- **Strecken** — das Video strecken, um den Bildschirm zu füllen, bei Bedarf verzerren.
- **Original** — native Auflösung bei 1:1 beibehalten.

## Video-Rotation

Für Videos, die mit falscher Ausrichtung aufgenommen wurden, wählen Sie **Weitere Aktionen → Rotation** und wählen Sie **0°**, **90°**, **180°** oder **270°**, um das Bild zu drehen, ohne den Player zu verlassen.

## Hardware-Dekodierung (H.264 und HEVC)

In Einstellungen → Player → Video können Sie Hardware-Dekodierung H.264 und Hardware-Dekodierung H.265 (HEVC) unabhängig aktivieren / deaktivieren. Hardware-Dekodierung ist schneller, verbraucht weniger Akku und läuft kühler — aber in seltenen Fällen (korrupte Dateien, exotische Profile) müssen Sie möglicherweise die Hardware-Dekodierung deaktivieren und auf Software-FFmpeg-Dekodierung zurückfallen. Evervideo ermöglicht Ihnen das dateiweise über das Weitere Aktionen-Menü des Players.

## VR 360°-Viewport

Evervideo enthält einen VR / 360°-Viewport für sphärische Videodateien. Beim Abspielen eines 360°-Videos können Sie ziehen, um sich umzusehen, zusammendrücken zum Zoomen, und Evervideo verformt das Rendering in Echtzeit.

## Wiedergabegeschwindigkeit

Tippen Sie auf die Geschwindigkeitssteuerung in der Player-Symbolleiste, um die Wiedergabegeschwindigkeit zu ändern — verlangsamen Sie für Analysen (0,25× oder 0,5×) oder beschleunigen Sie für Tutorials und Vorlesungen (1,25×, 1,5×, 2× und bis zu 3×). Tippen Sie auf das Konfigurationssymbol in der oberen rechten Ecke des Geschwindigkeitsbildschirms, um in den Präzisionsmodus mit feineren Anpassungen zu wechseln. Pro-Spur-Tonhöhenkorrektur ist ebenfalls verfügbar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wiedergabegeschwindigkeit in der Hauptsymbolleiste" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Player-Warteschlange

Um Ihre Player-Warteschlange zu sehen, tippen Sie auf die Warteschlangen-Schaltfläche auf dem Player. Jedes Video in der Warteschlange hat weitere Aktionen — tippen Sie auf die drei Punkte, um sie anzuzeigen. Um ein Video in der Warteschlange neu anzuordnen, verwenden Sie den Neuanordnungs-Indikator neben dem Titel und ziehen Sie es auf eine neue Position.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wiedergabewarteschlange" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Schlaf-Timer

Öffnen Sie Einstellungen → Player → Schlaf-Timer, schalten Sie ihn ein und wählen Sie, wie lange die Wiedergabe fortgesetzt werden soll, bevor sie automatisch stoppt. Sie können die Schlaf-Timer-Schaltfläche auch direkt über Einstellungen → Player → Personalisierung → Hauptbildschirm-Aktionen zum Hauptplayerbildschirm hinzufügen.

## Player-Lesezeichen

Speichern Sie Ihre Stelle in langen Videos — Vorlesungen, Bücher-als-Video, Tutorials, stundenlange YouTube-Downloads — indem Sie auf Lesezeichen hinzufügen im Weitere Aktionen-Menü tippen. Lesezeichen erscheinen in der Weitere Aktionen → Lesezeichen-Liste des Videos und bleiben zwischen Sitzungen erhalten.

## Weitere Aktionen-Menü

Tippen Sie auf die Weitere Aktionen "..."-Schaltfläche auf dem Player, um auf zusätzliche Funktionen zuzugreifen.

- **Wiedergabe fortsetzen** — die Warteschlange von der letzten Position fortsetzen.
- **Suche** — ein bestimmtes Video in Ihrer Warteschlange finden.
- **Lesezeichen** — Lesezeichen anzeigen und zu ihnen springen.
- **Geschwindigkeit** — Wiedergabegeschwindigkeit anpassen.
- **Aktuell** — zuletzt abgespielte Videos.
- **Favoriten** — favorisierte Videos.
- **Audio-Equalizer** — Audio-Equalizer aktivieren.
- **Video-Equalizer** — Video-Equalizer aktivieren.
- **Audiospur** — Audiostream auswählen.
- **Videospur** — Videostream auswählen.
- **Untertitel** — primäre / sekundäre Spur, externe Datei, Schrift.
- **Rotation** — Bild 0° / 90° / 180° / 270° drehen.
- **Skalierungsmodus** — Anpassen / Füllen / Strecken / Original.
- **Picture-in-Picture** — PiP-Modus aktivieren.
- **AirPlay** / **Chromecast** — an ein Gerät senden.
- **Schlaf-Timer** — Timer zum Stoppen der Wiedergabe einstellen.
- **Warteschlange als Wiedergabeliste speichern** — aktuelle Warteschlange als neue Wiedergabeliste speichern.
- **Warteschlange löschen** — Warteschlange leeren und Wiedergabe stoppen.
- **Einstellungen** — direkt zu den Player-Einstellungen springen.
- **Hilfe** — Anleitungen öffnen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Player Weitere Aktionen Bildschirm" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Player-Einstellungen

Der vollständige Player-Einstellungsbaum ist in der [Einstellungs-Anleitung](/docs/guide/evervideo/evervideo-guide-settings/) dokumentiert. Die am häufigsten verwendeten Abschnitte:

- **Allgemein** — Wiederholungsmodus, Zufallsmodus, Player-Status speichern, Wiedergabeposition speichern, Sprung-Zeitintervalle.
- **Video** — Hardware-Dekodierung H.264 / HEVC, Video-Equalizer, Skalierungsmodus, Rotation, Anzeigemodus, bevorzugte FPS, bevorzugtes Pixelformat, VR-Viewport.
- **Audio** — Audio-Equalizer, Abtastrate, Kanäle, IO-Pufferdauer, gemischter Modus.
- **Untertitel** — primäre / sekundäre Spur, externe Dateiauswahl, Schrift, sekundäre Schrift.
- **Geräte** (iOS) — AirPlay / Chromecast.
- **Personalisierung** — Player-Layout-Stil (Minimal / Unten / Antik / Klassisch), Hauptbildschirm-Aktionen, Sperrbildschirm-Steuerungen.
- **Wiedergabe-Cache** — Festplatten-Cache für flüssigeres Streaming.
- **Schlaf-Timer** — automatischer Stop.

## Barrierefreiheit

Evervideo ist vollständig mit VoiceOver zugänglich. Jede Komponente hat ein gut gestaltetes Label und eine Beschreibung. Wenn VoiceOver aktiv ist, wechselt die App in den Textmodus, sodass nur bedeutungsvolle Elemente angezeigt werden — was die Navigationsgeschwindigkeit und Klarheit verbessert. Sie können den Textmodus auch in Einstellungen → Barrierefreiheit → Textmodus aktivieren.

### Schieberegler mit VoiceOver anpassen

1. **Schieberegler auswählen** — wischen Sie nach links oder rechts, bis VoiceOver ihn ankündigt.
2. **Wert anpassen** — doppeltippen und halten Sie den Schieberegler, ziehen Sie dann nach oben oder unten, um den Wert schnell zu ändern. VoiceOver gibt den neuen Wert an, während Sie fortfahren.

Andere Komponenten funktionieren wie erwartet und verwenden systemseitig bereitgestellte VoiceOver-Muster.
