---
title: "Einstellungen"
date: 2020-02-01
lastmod: 2026-06-01
description: "Erkunden Sie alle Einstellungen in Evervideo — Mediaplayer (Bild-in-Bild, Hardware-H.264/HEVC-Decodierung, Video-Equalizer, Skalierung, Rotation, VR-Ansichtsfenster), Audio (Equalizer, Abtastrate, Kanäle, IO-Puffer, Mischmodus), Untertitel (primär/sekundär, Schriftart, externe Datei, libass), Mediathek, Dateimanager, WLAN-Laufwerk, Widgets, Personalisierung, Sprache, Passcode, Sichern & Wiederherstellen — für iPhone, iPad und Mac."
keywords: [
  "Evervideo Einstellungen", "Videoplayer-Konfiguration", "Premium-Upgrade Evervideo",
  "Bild-in-Bild Einstellungen", "Video-Equalizer Einstellungen",
  "Videoskalierungsmodus", "Videorotation", "Hardware-Decoder iPhone",
  "Untertitel-Einstellungen", "sekundäre Untertitel iOS", "libass Einstellungen",
  "externe Untertiteldatei", "Untertitelschriftart",
  "Audio-Equalizer Einstellungen", "Audio-Ausgabe-Abtastrate",
  "Audio-Ausgabe-Kanäle", "IO-Pufferdauer", "Audio-Mischmodus",
  "WLAN-Laufwerk Video", "Evervideo Widgets",
  "Evervideo sichern wiederherstellen", "Evervideo Passcode",
  "Evervideo Sprache", "Evervideo Personalisierung"
]
tags: ["Anleitung", "evervideo", "Einstellungen"]
readingTime: 16
---


Der Einstellungsbildschirm ist die Steuerzentrale von Evervideo. Von hier aus können Sie auf Premium upgraden, die Video- und Audio-Engines konfigurieren (System-Codecs oder FFmpeg), Bild-in-Bild verwalten, Untertitel einrichten (primär, sekundär, libass, externe Dateien, Schriftarten), die Mediathek organisieren, den Dateimanager einrichten, Home-Screen-Widgets aktivieren, Ihre Daten sichern und auf Hilfe und rechtliche Informationen zugreifen. Die Abschnitte sind unter Überschriften gruppiert: Käufe & Updates, App-Einstellungen, Hilfe, Rechtliches & Datenschutz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Einstellungen Hauptbildschirm" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Auf Premium upgraden

Upgraden Sie die App auf die Premium-Version, um alle Einschränkungen zu entfernen. Die kostenlose Version bietet einen einmaligen Lebzeiten-In-App-Kauf und zwei Abonnementoptionen (1 Monat und 1 Jahr), um alle Einschränkungen zu entfernen und auf Premium upzugraden.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Auf Premium upgraden" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

**Familienfreigabe** ist für alle Käufe und Tarife aktiviert, sodass Sie die Premium-Version mit bis zu fünf Familienmitgliedern ohne zusätzliche Kosten teilen können.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Premium-Tarif auswählen" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Käufe zwischen iOS und Mac teilen

Lebzeiten-Käufe und Abonnements werden zwischen iOS und Mac über **iCloud** synchronisiert. Wenn Sie Premium auf Ihrem iOS-Gerät haben, stellen Sie sicher, dass die neueste Version installiert ist und iCloud aktiviert ist. Starten Sie die App auf iOS und warten Sie eine Minute, damit die Kaufinformationen in iCloud hochgeladen werden, dann starten Sie die Mac-Version — Premium sollte sich automatisch aktivieren.

Sie können auch auf die Schaltfläche **Käufe wiederherstellen** in den App-Einstellungen tippen. Stellen Sie sicher, dass Sie eine Internetverbindung haben und auf beiden Geräten mit demselben iCloud- und App-Store-Konto angemeldet sind.

## Käufe auf einem neuen Gerät wiederherstellen

Um Ihren Kauf auf einem neuen Gerät wiederherzustellen, verwenden Sie das Menü **Käufe → Käufe wiederherstellen**. Sie sehen die Liste Ihrer Käufe. Wenn nicht alle angezeigt werden, bestätigen Sie, dass das Gerät mit derselben Apple-ID verbunden ist, die für die Käufe verwendet wurde, und stellen Sie sicher, dass iCloud aktiviert ist.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Käufe-Menü in den Einstellungen" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Premium kostenlos testen

Sie können die Premium-Version für einen begrenzten Zeitraum kostenlos upgraden, indem Sie dieses Menü verwenden. Schauen Sie sich einfach eine Werbung an oder erzählen Sie Ihren Freunden von der App.

## Software-Update

Tippen Sie auf **Software-Update**, um zu prüfen, ob eine neuere Version von Evervideo im App Store verfügbar ist.

## Neuigkeiten

Dieses Menü ist nach der Veröffentlichung einer neuen Version verfügbar. Es zeigt eine Zusammenfassung der Änderungen und neuen Funktionen des letzten Updates.

## Player

Alles rund um die Wiedergabe ist hier — Audio, Video, Untertitel, Geräte, Personalisierung, Cache und der Schlaf-Timer.

### Allgemein

Diese Einstellungen decken die grundlegenden Aspekte des Players ab.

- **Wiederholungsmodus** — wählen Sie, wie der Player sich verhält, wenn ein Video endet:
  - **Alle wiederholen** — spielt alle Videos in Ihrer Warteschlange erneut ab.
  - **Eines wiederholen** — wiederholt nur das aktuelle Video.
  - **Wiederholen stoppen** — pausiert, wenn das aktuelle Video endet.
  - **Nicht wiederholen** — spielt die Warteschlange einmal durch ohne Wiederholung.
- **Zufallsmodus** — zufällige Reihenfolge der Videos in Ihrer Warteschlange (**Ein** oder **Aus**).
- **Wiedergabeposition speichern** — speichert und stellt die Wiedergabeposition für Videos in Ihrer Bibliothek wieder her.
- **Player-Status speichern** — bewahrt den Status des Players, bevor Sie die App schließen, damit Sie dort weitermachen können, wo Sie aufgehört haben.

### Video

Konfigurieren Sie, wie Evervideo Video dekodiert und rendert.

- **Hardware-Dekodierung H.264** — Hardware-beschleunigte AVC-Dekodierung ein-/ausschalten. Verwenden Sie diese Option, wenn Akku- und Thermoleistung wichtig sind; ausschalten für Kompatibilität mit exotischen Profilen.
- **Hardware-Dekodierung H.265 (HEVC)** — dasselbe für HEVC. Moderne iPhones, iPads und Macs dekodieren HEVC effizient.
- **Bevorzugtes Pixelformat** — wählen Sie das Pixelformat, das der Player dem Renderer präsentiert (Standardwerte sind für das Gerät optimiert).
- **Bevorzugte FPS** — legen Sie eine Ziel-Wiedergabe-FPS fest. Nützlich, um eine bestimmte Monitorbildwiederholrate anzupassen.
- **Videoskalierungsmodus** — Anpassen / Füllen / Strecken / Original. Bestimmt, wie das Bild den Anzeigebereich füllt.
- **Videoanzeigemodus** (iOS / iPadOS) — wie das Video in der Player-Ansicht präsentiert wird.
- **Videorotation** — drehen Sie das Bild manuell um 0° / 90° / 180° / 270° (hilfreich für Videos, die in der falschen Ausrichtung aufgenommen wurden).
- **Video-Equalizer** — Helligkeit, Kontrast, Sättigung und Farbton mit Echtzeit-Vorschau anpassen. Benutzerdefinierte Presets können **exportiert und importiert** werden.
- **VR-Ansichtsfenster** (iOS / iPadOS) — für 360°-Kugelvideos. Ziehen zum Umschauen, Zusammendrücken zum Zoomen.
- **Bild-in-Bild (BiB)** (iOS / iPadOS) — BiB-Unterstützung aktivieren; die App wechselt zu einem schwebenden Player-Fenster, wenn Sie die App in den Hintergrund verlagern oder auf die BiB-Schaltfläche tippen.

### Audio

Konfigurieren Sie die Audio-Wiedergabe und -Ausgabe.

- **Audiospur** — wählen Sie den Audiostream, wenn ein Video mehrere hat (Kommentar, Synchronisation usw.).
- **Audio-Equalizer** — 10-Band-EQ mit Presets und einem Vorverstärker. Benutzerdefinierte Presets können exportiert/importiert werden.
- **Audio-Ausgabe-Abtastrate** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Nützlich mit externen DACs.
- **Anzahl der Audio-Ausgabe-Kanäle** — Mono, Stereo, 5.1, ITU BS.775-1, SDDS und mehr.
- **Bevorzugte IO-Pufferdauer der Audio-Ausgabe** — typischer Wert für latenzarme Hi-Res-Wiedergabe liegt bei etwa 5 ms (0,005 s). Abstimmen für Ihre Hardware.
- **Audio-Ausgabe-Modus** (nur iOS) — Mischmodus lässt Evervideo-Audio mit anderen Apps vermischen.

### Untertitel

Evervideo bietet umfassende Untertitelunterstützung.

- **Untertitelspur** — wählen Sie aus eingebetteten Untertitelspuren in der Datei.
- **Externe Untertiteldatei** — laden Sie eine externe `.srt`-, `.vtt`-, `.ass`- oder `.ssa`-Datei von Ihrem Gerät oder einem verbundenen Cloud-Dienst.
- **Schriftart** — wählen Sie eine Schriftart für die primäre Untertitelspur.

### Geräte (nur iOS/iPadOS)

Wählen Sie ein **AirPlay**- oder **Google Chromecast**-Gerät für die Videoausgabe.

### Personalisierung

- **Player-Layout-Stil** — Minimal (Standard für Evervideo), Unten, Antik, Klassisch und mehr.
- **Hauptbildschirm-Aktionen** — wählen Sie, welche Schaltflächen auf dem Haupt-Player-Bildschirm erscheinen.
- **Sperrbildschirm-Steuerungen** — Zeit überspringen, Lesezeichen hinzufügen, Zu Favoriten hinzufügen.
- **Überspringen-Zeitintervalle** — wählen Sie das Zeitintervall für Überspringen-Schaltflächen (5 s, 10 s, 15 s, 30 s usw.).
- **Album-Cover-Scrollstil** — bevorzugter Scroll-Stil für Cover-Artwork.
- **Zusätzliche Elemente** — Audio-Format-Info, Lautstärke-Schieberegler.

### Dateiladen

Konfigurieren Sie, wie Videodaten aus dem Netzwerk gestreamt werden.

- **Netzwerktyp** — nur WLAN oder WLAN + Mobilfunk.
- **Vorladezeit** — Pufferlänge für reibungslosere Wiedergabe in langsamen Netzwerken.
- **Direkte URL verwenden** — wenn unterstützt, verwenden Sie eine direkte URL für schnelleres Laden.

### Wiedergabe-Cache

Videos in der Player-Warteschlange werden automatisch heruntergeladen, um eine reibungslose Wiedergabe zu gewährleisten. Sie können diese Option deaktivieren oder die Cache-Größe hier konfigurieren.

### Schlaf-Timer

Aktivieren Sie einen Timer, um die Wiedergabe nach einem bestimmten Zeitraum automatisch zu stoppen. Tippen Sie auf das Konfigurationssymbol für den **Präzisionsmodus** mit minutengenauer Granularität.

## Mediathek

Verwalten Sie automatische Synchronisierung, Metadaten, Album-Cover, Wiedergabelisten, zuletzt Gespieltes und Favoriten.

### Metadaten-Lesen

Wenn Sie Videos zur Bibliothek hinzufügen, scannt der Metadaten-Leser sie im Hintergrund und organisiert sie nach Album und Genre. Sie können die Scan-Geschwindigkeit anpassen, den Leser deaktivieren oder einen vollständigen Rescan mit **Metadaten neu laden** auslösen. **Metadaten-Codierung normalisieren** behebt automatisch fehlerhafte Zeichenkodierungen (häufig bei Dateien von Windows-PCs).

### Online-Synchronisierung

Fügen Sie automatisch Videos von verbundenen Cloud-Diensten und Medienservern zu Ihrer Bibliothek hinzu. Wählen Sie, welche Ordner gescannt werden sollen, konfigurieren Sie, wie oft die App synchronisieren soll, und starten/stoppen Sie die Synchronisierung manuell. Die Online-Synchronisierung läuft nur, während die App aktiv ist — für große Bibliotheken verwenden Sie die Desktop-Version und übertragen Sie dann die synchronisierte Bibliothek mit **Sichern & Wiederherstellen**.

### Offline-Synchronisierung

Wenn Sie einen Cloud-Ordner als offline verfügbar markieren, erscheint er in **Dateien → Offline-Ordner** und wird automatisch heruntergeladen. Neue online hinzugefügte Dateien werden ebenfalls heruntergeladen. Konfigurieren Sie das Zeitintervall und starten Sie manuelle Syncs von diesem Bildschirm aus.

### Personalisierung

- **Mediathek-Bildschirmstil** — Einfaches Menü, Gruppiertes Menü, Tabbed-Menü.
- Umschalten, ob große Album-Cover in Detailbildschirmen angezeigt werden sollen.

### Album-Cover

- **Netzwerktyp** — WLAN oder WLAN + Mobilfunk.
- **Album-Cover für Online-Dateien laden** — eingebettete Grafiken aus Cloud-Dateien abrufen (verbraucht zusätzliche Daten).
- **Im Ordner suchen** — JPEG/PNG-Bilder im selben Ordner verwenden, wenn ein Video kein eingebettetes Cover hat.
- **Cover-Qualität** — passen Sie die Auflösung an, mit der Cover zwischengespeichert werden.
- **Im Ordner anzeigen** / **Alle löschen** — verwalten Sie den Artwork-Cache.

### Wiedergabelisten

Ermöglichen Sie, dasselbe Video zweimal zu einer Wiedergabeliste hinzuzufügen (standardmäßig deaktiviert).

### Zuletzt gespielt

Verwalten Sie die zuletzt gespielten Videos-Liste — ändern Sie die Größe, löschen oder exportieren Sie als M3U / CSV / TXT.

### Favoriten

- **Gleichzeitiges Bearbeiten** — Favoriten zwischen der Mediathek und dem Dateibereich spiegeln.
- **Liste löschen** — die Favoritenliste leeren.
- **Songliste exportieren** — Favoriten als M3U / CSV / TXT exportieren.

### Mediathek löschen

Die Mediathek-Datenbank löschen. Ihre Video- und Audiodateien im Speicher bleiben unberührt.

## Passcode

Schützen Sie Evervideo mit einem **4-stelligen numerischen Passcode**. Wenn aktiviert, werden Sie beim Start der App jedes Mal aufgefordert, den Passcode einzugeben. Kombinieren Sie ihn mit iOS Face ID / Touch ID auf dem Gerät für zusätzlichen Schutz.

## Dateimanager

Steuert, wie Dateien übertragen, gespeichert und in der Vorschau angezeigt werden.

- **Dateiübertragungen** — Netzwerkpräferenz (nur WLAN oder WLAN + Mobilfunk).
- **Maximale Anzahl paralleler Aufgaben** — legen Sie die Anzahl der parallelen Download-Threads fest.
- **Dateiübertragungsaufgaben** — aktuelle Uploads und Downloads anzeigen.
- **Hintergrundübertragungen** — Downloads erlauben, während die App im Hintergrund ist.
- **Heruntergeladene Dateien speichern in** — Standard-Download-Verzeichnis.
- **Synchronisierte Offline-Ordner** — verwalten Sie Offline-Modus-Ordner.
- **Zeitintervall** — wie oft Offline-Ordner auf Änderungen überprüft werden.
- **Vollständige Dateinamen anzeigen** — Erweiterungen im Dateimanager anzeigen.
- **Online-Dateien bearbeiten** — deaktivieren, um auf Nur-Lese-Modus für verbundene Cloud-Dienste umzustellen.
- **Dateien beim Öffnen kopieren** — wie importierte Dateien von anderen Apps behandelt werden.
- **Vorschaubilder für Dateien** — generierte Dateivorschaubilder verwalten.
- **Temporäre Dateien löschen** — den Cache-Ordner der App leeren.

## WLAN-Laufwerk

Aktivieren Sie das WLAN-Laufwerk, um Dateien von einem Computer auf Ihr Gerät über einen Desktop-Webbrowser, Finder oder Datei-Explorer zu übertragen. Detaillierte Anweisungen sind [hier](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) verfügbar.

## Widgets

Aktivieren Sie Widgets, damit die App Widget-Daten während der Wiedergabe aktualisiert. Widget-Updates erfordern zusätzliche Energie, daher ist der Schalter standardmäßig deaktiviert — aktivieren Sie ihn nur, wenn Sie tatsächlich Widgets auf Ihrem Home-Screen oder Sperrbildschirm verwenden.

Sie können Evervideo-Widgets hinzufügen, indem Sie Ihren Home-Screen oder Sperrbildschirm lange drücken, auf **+** tippen, **Evervideo** suchen und eine Widget-Größe auswählen. Widgets zeigen das gerade gespielte Video und führen direkt zum Vollbild-Player. Widgets funktionieren auch auf macOS im Benachrichtigungscenter.

## Personalisierung

Passen Sie die Benutzeroberfläche nach Ihren Wünschen an.

- **App-Symbol** — alternatives Home-Screen-Symbol (Premium).
- **Farbschema** — Dunkel, Hell oder Standard (folgt Ihrer Systemdarstellung).
- **Hintergrundstil** — Verschwommenes Album-Cover oder einfarbig.
- **Erscheinungsbild der Elemente in der Liste** — Zeilenhöhe automatisch anpassen; kleinere Vorschaubilder anzeigen.
- **Inhaltslade-Limit** — Seitennavigation ein-/ausschalten.
- **Dateien-Bildschirmstil** — Einfaches Menü oder Gruppiertes Menü.
- **Mediathek-Bildschirmstil** — Einfach / Gruppiert / Tabbed-Menü.
- **Player-Bildschirmstil** — Minimal / Unten / Antik / Klassisch.
- **Kontextmenü-Stil** — Systemmenü oder Bottom-Sheet-Stil.

## Fenster

Verfügbar auf Mac und Catalyst. Konfigurieren Sie fensterbezogene Einstellungen wie Standardgröße und Verhalten beim Start.

## Bildschirm

Wählen Sie, ob der Bildschirm aktiv bleiben soll, während Sie die App verwenden.

## Barrierefreiheit

Aktivieren Sie den **Textmodus**, um Bilder in der Benutzeroberfläche auszublenden. Der Textmodus wird automatisch aktiviert, wenn VoiceOver aktiv ist.

## Sprache

Ändern Sie die App-Sprache und überschreiben Sie den Systemstandard. Die Änderung wird wirksam, nachdem Sie Evervideo vollständig beenden und erneut öffnen. Über 120 Sprachen werden unterstützt.

## Sichern & Wiederherstellen

Sichern Sie alle Ihre App-Daten oder migrieren Sie sie auf ein anderes Gerät. Wählen Sie, was eingeschlossen werden soll:

- **Datenbank** — Ihre Mediathek-Einträge, Wiedergabelisten, Bewertungen, Favoriten, Wiederschauverlauf. Offline-Dateien sind nicht enthalten, um die Dateigröße überschaubar zu halten.
- **Album-Cover** — Ihr zwischengespeichertes Artwork.
- **Einstellungen** — Ihre App-Einstellungen.

Tippen Sie auf **App-Daten sichern**, um die Sicherung zu starten. Um auf einem neuen Gerät wiederherzustellen, verschieben Sie die Sicherungsdatei über iCloud Drive, AirDrop oder einen verbundenen Cloud-Dienst und öffnen Sie sie auf dem neuen Gerät.

## Hilfe

Greifen Sie auf die App-Anleitung zu, um Hilfe und Anleitungen zur effektiven Nutzung der App zu erhalten.

## Häufig gestellte Fragen

Finden Sie Antworten auf häufige Fragen im FAQ-Bereich.

## Feedback senden

Senden Sie Ihr Feedback direkt aus der App an unser Support-Team, mit automatisch angehängten Diagnoseinformationen.

## Diese App teilen

Teilen Sie Evervideo mit Ihren Freunden, um die Botschaft zu verbreiten.

## Weitere Apps entdecken

Entdecken Sie weitere Apps von Everappz.

## Nutzungsbedingungen

Lesen Sie die Nutzungsbedingungen, bevor Sie die App verwenden.

## Datenschutzrichtlinie

Lesen Sie die Datenschutzrichtlinie, um unsere Datenpraktiken zu verstehen.

## Analyse und Datenerfassung

Prüfen Sie, welche Dienste für Analysen und Datenerfassung aktiviert sind, und deaktivieren Sie alle, die Sie nicht möchten.

## Rechtliche Hinweise

Informationen zu jeder in der App verwendeten Bibliothek sowie Versionsnummer und Build-Informationen der App.
