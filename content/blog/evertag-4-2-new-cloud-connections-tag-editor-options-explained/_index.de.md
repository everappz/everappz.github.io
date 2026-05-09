---
title: "Evertag 4.2: Neue Cloud-Verbindungen, Tag-Editor-Einstellungen erklärt"
date: 2026-05-09
description: "Evertag 4.2 fügt Verbindungen zu Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP und NFS hinzu, frischt Wi-Fi Drive auf und passt die Oberfläche an Liquid Glass an. Dieser Beitrag erklärt außerdem jede Tag-Editor-Einstellung — einschließlich ID3v2.4 vs. ID3v2.3, Skalierung des Albumcovers, Tag-Duplizierung, Cloud-Upload-Modi und der richtigen Optionen für Spotify und andere Streamingdienste."
keywords: ["Evertag 4.2", "Evertag Update", "ID3 Tag-Editor iPhone", "ID3v2.4 vs ID3v2.3", "FLAC Tags bearbeiten iOS", "MP3 Tags bearbeiten iPhone", "Albumcover bearbeiten iOS", "Tag-Editor für Spotify", "Tag-Editor Plex", "Tag-Editor Apple Music", "Evertag Cloud Tag-Editor", "Internxt Tag-Editor", "Proton Drive Tag-Editor", "QNAP Tag-Editor", "Nextcloud Tag-Editor", "Amazon S3 Tag-Editor", "SFTP Tag-Editor iPhone", "FTP Audio Tag-Editor", "NFS Tag-Editor iPhone", "Wi-Fi Drive Tag-Editor", "ID3-Tags duplizieren", "Albumcover-Skalierung", "Liquid Glass Design", "Audio-Metadaten-Editor iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Tag-Editor", "ID3", "ID3v2.4", "ID3v2.3", "FLAC-Tags", "MP3-Tags", "Albumcover", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Neuerungen"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**Kurzfassung:** [Evertag 4.2](/products/evertag) ist ein großes Update für den Audio-Tag-Editor auf iPhone, iPad und Mac. Wir haben wichtige Fehler bei der Tag-Bearbeitung beseitigt und mehr als 6 neue Cloud- und Server-Verbindungen ergänzt — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** sowie die Protokolle **FTP**, **SFTP** und **NFS**. Wi-Fi Drive bekam eine aufgefrischte Oberfläche, einen Mehrfachauswahlmodus, eine intelligentere Upload-Warteschlange und schnellere Übertragungen. Die ganze App ist auf das Design **Liquid Glass** abgestimmt. Dieser Beitrag geht außerdem tief auf Evertags Tag-Editor-Einstellungen ein — er erklärt **ID3v2.4 vs. ID3v2.3**, **Albumcover-Skalierung**, **Tag-Duplizierung**, **Cloud-Upload-Modi**, **heruntergeladene Datei löschen** und genau, welche Optionen du wählen solltest, wenn du Audio für **Spotify**, **Apple Music**, **Plex**, **Jellyfin** oder einen anderen Streamingdienst vorbereitest.

---

## Hallo zusammen!

Ein großes Evertag-Update ist da. Wir haben wichtige Tag-Bearbeitungs-Bugs gefixt und **mehr als 6 neue Cloud- und Server-Verbindungen** hinzugefügt, damit das Verwalten deiner Audio-Metadaten einfacher ist als je zuvor — egal, ob deine Bibliothek in einer datenschutzorientierten Cloud, auf einem selbst gehosteten NAS oder auf einem allgemeinen FTP/SFTP/NFS-Server liegt.

[Lade Evertag 4.2 aus dem App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) oder aktualisiere von deiner aktuellen Version.

## Erweiterte Cloud- und Server-Unterstützung

Evertag verbindet sich jetzt nativ mit einer breiteren Palette von Cloud- und selbst gehosteten Speicheroptionen. Du kannst ID3-, MP4-, FLAC-, OGG- und APE-Tags an Dateien bearbeiten, wo immer sie liegen.

### Datenschutzfreundlicher Cloud-Speicher: Internxt und Proton Drive

Wenn dir Ende-zu-Ende-Verschlüsselung und Zero-Knowledge-Speicher wichtig sind, sind zwei der angesehensten datenschutzorientierten Clouds jetzt nativ in Evertag verfügbar:

- **Internxt** — Open-Source, post-quanten-verschlüsselte, DSGVO-konforme spanische Cloud. Kostenloses Tier verfügbar.
- **Proton Drive** — Ende-zu-Ende-verschlüsselter Speicher von den Machern von Proton Mail und Proton VPN, mit Sitz in der Schweiz. Kostenloses Tier verfügbar, kostenpflichtige Pläne für größere Bibliotheken.

Du kannst jetzt Metadaten direkt auf Audiodateien bearbeiten, die in einem der beiden Dienste gespeichert sind — die Datei bleibt während der Übertragung verschlüsselt, und nur die neuen Tags werden zurückgeschrieben.

### Selbst gehostete Lösungen: QNAP, Nextcloud, Amazon S3

Für Nutzer, die eigene Infrastruktur betreiben:

- **QNAP** — native API-Verbindung zu QNAP-NAS-Geräten. Bearbeite Tags an Dateien auf deinem QNAP über lokales WLAN oder Fernzugriff.
- **Nextcloud** — verbinde dich mit jeder selbst gehosteten oder verwalteten Nextcloud-Instanz.
- **Amazon S3** — richte Evertag auf einen beliebigen S3-Bucket (oder S3-kompatiblen Speicher wie Backblaze B2, Wasabi, MinIO, Cloudflare R2) und bearbeite Metadaten direkt an Ort und Stelle.

### Neue Netzwerkprotokolle: FTP, SFTP, NFS

Evertag 4.2 ergänzt drei klassische Protokolle für Nutzer mit eigenen Servern, Homelabs oder generischen NAS-Geräten:

- **SFTP (SSH File Transfer Protocol)** — die richtige Antwort, um **Tags sicher aus der Ferne auf dem eigenen Server zu bearbeiten**. SFTP läuft über SSH, dadurch ist die gesamte Übertragung (Authentifizierung und Audiodaten) verschlüsselt. Hast du einen VPS, dedizierten Server oder einen Linux-Rechner zu Hause mit SSH-Zugriff, kannst du Tags an entfernten Dateien bearbeiten, ohne sonst etwas freizugeben. Unterstützt Passwort- und schlüsselbasierte Authentifizierung.
- **FTP** — der seit Jahrzehnten etablierte Standard für Dateiübertragungen. Praktisch für ältere Heim-NAS-Geräte, die FTP bereitstellen, aber keine native API haben.
- **NFS (Network File System)** — das De-facto-Freigabeprotokoll unter Linux und auf den meisten NAS-Geräten. Geringerer Overhead als SMB auf derselben Hardware.

> **Tipp:** SFTP ist das richtige Protokoll fürs Bearbeiten aus dem offenen Internet. FTP und NFS gehören eher ins lokale Netzwerk — exponiere sie nicht ungeschützt im Internet, außer hinter einem VPN.

## Wi-Fi-Drive-Verbesserungen

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) ist Evertags eingebaute Funktion, um Audiodateien drahtlos zwischen Computer und iPhone oder iPad zu übertragen — ohne iTunes, ohne Kabel und ohne Cloud-Konto. Beide Geräte müssen im selben WLAN sein.

In Evertag 4.2 erhält Wi-Fi Drive:

- **Aufgefrischte, moderne Oberfläche** — aufgeräumter, schneller erfassbar und auf Liquid Glass aktualisiert.
- **Mehrfachauswahlmodus** — wähle mehrere Dateien oder Ordner aus und bearbeite sie in einem Schwung.
- **Intelligentere Upload-Warteschlange** — bessere Fortschrittsanzeige und Robustheit gegen Netzwerkprobleme.
- **Verbesserte Geschwindigkeit und Zuverlässigkeit insgesamt** — schnellere Übertragungen für große Bibliotheken.

Es ist der schnellste Weg, einen Stapel Audiodateien vom Computer aufs Telefon zu übertragen, deren Tags zu bearbeiten und sie zurückzuschicken — ganz ohne Drittanbieterdienste.

## Tag-Editor-Einstellungen: Tiefer Einblick

Das ist der Teil, den die meisten Nutzer nie lesen — und genau er entscheidet, ob deine Tags überall funktionieren oder nur in einigen Apps. Öffne Evertag und gehe in den Bereich **Audio-Tag-Editor-Einstellungen**. Hier steht, was jede Option wirklich tut, und welche du wählen solltest — abhängig vom Ziel.

### Albumcover-Skalierung

Wenn du Albumcover in einer Audiodatei speicherst, kann Evertag das Bild vor dem Einbetten herunterskalieren. Verfügbar sind:

- **Klein** — geringster Einfluss auf die Dateigröße, niedrigere Bildqualität.
- **Mittel** — ausgewogene Wahl für die meisten Nutzer.
- **Groß** — hohe Qualität, geeignet für große Bildschirme und CarPlay.
- **Sehr groß** — sehr hohe Qualität, deutlicher Anstieg der Dateigröße.
- **Original (Deaktiviert)** — bettet das Cover in Originalauflösung ein. **Keine Skalierung.**

**Warum das wichtig ist:**

- **Mehr Qualität = größere Datei.** Ein 3.000 × 3.000 Pixel Cover kann jedem Track mehrere MB hinzufügen. Aufs gesamte Album multipliziert summiert sich der Speicherbedarf schnell.
- **Manche Player kommen mit sehr großen eingebetteten Bildern schlecht klar.** Ältere Geräte, einige Auto-Headunits und manche Legacy-Desktop-Player können bei Covern über ~1.500 px aussteigen oder sie nicht anzeigen.
- **Für die meisten Cloud- und Streaming-Workflows** ist **Mittel** oder **Groß** der Sweet Spot. **Original** nur dann, wenn du Archivqualität brauchst oder Dateien für einen Player vorbereitest, dem du das zutraust.

> Die Größe **Original** ist Teil von Evertags Premium-Personalisierungs-Upgrade. Die Standardgrößen (Klein/Mittel/Groß/Sehr groß) sind kostenlos.

### Tag-Speicheroptionen: ID3v2.4 vs. ID3v2.3

Das ist die wichtigste Einstellung für Kompatibilität. ID3v2 ist das Metadatenformat in MP3-Dateien. Es gibt zwei weit verbreitete Versionen, die sich in subtilen, aber wichtigen Punkten unterscheiden.

#### ID3v2.4

- Neuer, unterstützt **UTF-8-Textkodierung** — saubere Behandlung nicht-lateinischer Schriften (Chinesisch, Russisch, Japanisch, Arabisch, Hebräisch usw.).
- Mehr Frame-Typen (relative Lautstärke, Equalizer-Presets usw.).
- **Empfohlen für moderne Player**, die es unterstützen.

#### ID3v2.3

- Älter, aber **die universellste ID3-Version**.
- Unterstützt UTF-8 nicht direkt (verwendet UTF-16 für Unicode-Text).
- **Empfohlen, wenn du maximale Kompatibilität** mit alten Playern, Autoradios und bestimmten Desktop-Apps brauchst.

#### Wann ID3v2.4 in Evertag aktivieren

- Du nutzt **moderne Audio-Player** wie Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (aktuelle Versionen) oder moderne Android-Player. ✅ **ID3v2.4 EIN.**
- Deine Bibliothek enthält **nicht-lateinische Zeichen** (Chinesisch, Koreanisch, Japanisch, Russisch, Arabisch, Griechisch, Hebräisch). ✅ **ID3v2.4 EIN** — UTF-8 verarbeitet sie viel sauberer.

#### Wann ID3v2.4 in Evertag deaktivieren (stattdessen ID3v2.3)

- Du bereitest Dateien für ein **älteres Autoradio oder eine ältere Headunit** vor, die v2.4-Tags nicht liest.
- Du siehst **kaputten Text oder fehlende Tags** in einigen Apps nach der Bearbeitung — ein klares Zeichen, dass dort v2.4 nicht unterstützt wird. Schalte zurück auf v2.3.
- Du adressierst **Legacy-Desktop-Player** oder ältere tragbare Player (frühe iPods, bestimmte MP3-Player aus den 2000er–2010er-Jahren).

> **Faustregel:** Wenn deine Tags überall mit v2.4 korrekt angezeigt werden, lass es an. Wenn auch nur ein wichtiger Player falsche Zeichen, leere Felder zeigt oder die Tags nicht liest, schalte v2.4 aus und speichere neu.

#### Tag-Duplizierung

Wenn du **Tags duplizieren** aktivierst, schreibt Evertag gemeinsame Metadatenfelder (Titel, Künstler, Album usw.) in **die ID3v1- und die ID3v2-Sektion** der Datei. Das verbessert die Kompatibilität mit sehr alten Playern, die nur ID3v1 lesen (das ursprüngliche 128-Byte-Tag am Dateiende).

- **Die meisten Nutzer brauchen das nicht.** Moderne Player lesen zuerst ID3v2.
- **Aktiviere es nur, wenn** du mit Vintage-Hardware oder spezifischer Software arbeitest, die ID3v2 ignoriert.

### Online-Dateien aktualisieren: wie Evertag Cloud-Bearbeitungen handhabt

Wenn du Tags an einer Datei bearbeitest, die in einer verbundenen Cloud (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP usw.) liegt, muss Evertag die geänderte Datei zurückladen. Du steuerst, wie:

- **Bestätigungsmeldung anzeigen** *(Standard, empfohlen)* — Evertag fragt vor dem Hochladen. Am besten für vorsichtige Nutzer und geteilte Bibliotheken.
- **Metadaten der Datei automatisch aktualisieren** — lädt nach jeder Bearbeitung still hoch. Am besten für Solo-Nutzer mit schnellen, zuverlässigen Verbindungen, die viel bearbeiten.
- **Metadaten der Datei nicht aktualisieren** — Evertag bearbeitet nur die lokale Kopie. Praktisch, wenn du Änderungen vorab sehen möchtest, ohne sie in die Cloud zu übernehmen.

### Online-Dateien bearbeiten: lokale Datei aufräumen

Um eine entfernte Datei zu bearbeiten, lädt Evertag sie zuerst auf dein Gerät. Nach der Bearbeitung wählst du, was mit dieser lokalen Kopie passiert:

- **Heruntergeladene Datei immer löschen** — Evertag entfernt die temporäre Datei nach der Bearbeitung. **Empfohlen**, wenn der Speicher knapp ist oder du an fremden Dateien arbeitest.
- **Heruntergeladene Datei nicht löschen** — behält die bearbeitete Datei auf deinem Gerät. Praktisch, wenn du gleichzeitig eine Offline-Kopie und eine aktualisierte Cloud-Kopie willst.

### Schaltflächen auf dem Hauptbildschirm

Evertags Tag-Editor-Hauptbildschirm kann Schaltflächen einzelner Aktionen ein- oder ausblenden. Aktiviere nur das, was du wirklich nutzt, um die Oberfläche fokussiert zu halten:

- **Audio-Tags automatisch suchen** — findet fehlende Metadaten online anhand des Audiofingerabdrucks der Datei.
- **Audio-Tags manuell suchen** — Suche nach Titel/Künstler, wenn die automatische Suche scheitert.
- **Albumcover suchen** — findet und integriert hochwertige Cover.
- **Albumcover speichern** — exportiert das eingebettete Cover in deine Fotos oder Dateien.
- **Kodierung normalisieren** — repariert verkrüppelten nicht-lateinischen Text aus alten Kodierungen (sehr nützlich für kyrillische, chinesische und japanische Tracks aus Legacy-Software).
- **Audio-Tags löschen** — entfernt alle Tags aus einer Datei. Hilfreich vor sauberer Neu-Verschlagwortung.

### Erweiterte Tags anzeigen

Aktiviere dies, um den vollständigen Satz Metadatenfelder über das Standard-Trio Titel/Künstler/Album/Jahr hinaus anzuzeigen — inklusive BPM, Dirigent, Originalkünstler, Stimmung, Copyright, Encoder, Kommentare, Songtexte und mehr. Power-User-Funktion; die meisten Gelegenheitsnutzer brauchen sie nicht.

### Dateien gleichzeitig bearbeiten

Aktiviert, kannst du mit Evertag Metadaten für **mehrere ausgewählte Dateien gleichzeitig** bearbeiten — den gleichen Albumkünstler, das gleiche Jahr oder Genre für ein ganzes Album in einem Vorgang setzen. Der schnellste Weg, eine große, ungeordnete Bibliothek aufzuräumen.

## Tags für Spotify, Apple Music und Streamingplattformen bearbeiten

Eine häufige Frage: „Ich habe meine Tags in Evertag bearbeitet, die Dateien hochgeladen, und der Streamingdienst zeigt falsche Metadaten. Was ist los?"

Kurze Antwort: **Streamingdienste respektieren deine lokalen Tags nicht immer.** Apple Music und Spotify haben eigene interne Datenbanken — sobald sie einen Track erkennen, überschreiben sie die angezeigten Metadaten mit den eigenen. Aber für **hochgeladene Dateien**, deine lokalen Dateien (Apple Musics „Mediathek"-Funktion, Spotify Local Files) und **Distributor-Uploads zu Streamingplattformen** sind deine Tags absolut entscheidend. So konfigurierst du Evertag je nach Szenario:

### Dateien für Apple Music vorbereiten (Cloud Music Library / iTunes Match)

- **ID3v2.4: AN** — Apple Music geht korrekt mit UTF-8 um.
- **Albumcover: Groß** — Apples Apps zeigen große Cover gut; Original ist überdimensioniert.
- **Tags duplizieren: AUS** — nicht nötig.
- Stelle sicher, dass **Albumkünstler** korrekt gefüllt ist — Apple Music nutzt es zur Gruppierung.

### Dateien für Spotify Local Files vorbereiten

Spotify Local Files zeigt nur gut verschlagwortete Dateien an. Die von Spotify gelesenen Tags sind begrenzt.

- **ID3v2.4: AN** in den meisten Fällen. Wenn ein Track nach der Bearbeitung in Spotify nicht korrekt erscheint, **versuche, mit ID3v2.4 AUS zu speichern** (also als ID3v2.3) — Spotifys Parser war historisch konservativ bei v2.4.
- **Albumcover: Mittel oder Groß** — Spotify skaliert die Cover sowieso herunter.
- Fülle mindestens **Titel**, **Künstler**, **Album** und **Track-Nummer** aus.

### Dateien für Distributor-Uploads vorbereiten (DistroKid, TuneCore, CD Baby usw.)

Wenn du als Künstler eigene Werke auf Streamingplattformen hochlädst, liest dein Distributor in der Regel Tags, fragt aber auch Metadaten in seiner UI ab. So oder so:

- **ID3v2.3** ist oft die sicherere Standardwahl — viele Distributor-Pipelines wurden vor Jahren gebaut und bevorzugen das ältere Format.
- Bette **Großes** Cover ein (die meisten Distributoren verlangen ≥ 1.400 × 1.400 px — prüfe deren Vorgaben).
- Verlasse dich nicht auf erweiterte Tags — Distributoren lesen nur Kernfelder.

### Dateien für Plex, Jellyfin, Navidrome, Subsonic, Emby vorbereiten

Diese selbst gehosteten Mediaserver sind sehr tolerant. Sie lesen sowohl v2.3 als auch v2.4 sauber und kommen gut mit UTF-8 klar.

- **ID3v2.4: AN** ist okay.
- **Albumcover: Groß** oder **Sehr groß** — diese Server liefern Cover an mobile Clients und CarPlay-Bildschirme, also zählt Qualität.
- **Albumkünstler** dringend empfohlen — daran orientieren sich Plex/Jellyfin beim Gruppieren von Alben nach Künstler.

### Dateien für Autoradios und ältere Hardware vorbereiten

- **ID3v2.4: AUS** (stattdessen ID3v2.3) — ältere Headunits unterstützen v2.4 oft nicht.
- **Albumcover: Mittel** — viele Auto-Displays kommen mit großen eingebetteten Covern nicht klar.
- **Tags duplizieren: AN** — ältere Autoradios lesen manchmal nur den ID3v1-Fallback.

## Weitere Verbesserungen

### Liquid-Glass-Design

Die Oberfläche von Evertag 4.2 wurde an Apples neues **Liquid Glass**-Material in der gesamten App angepasst — durchscheinende Oberflächen, geschmeidigere Animationen und verfeinerte Bedienelemente, die sich natürlich in iOS, iPadOS und macOS einfügen.

### Aktualisierte Verbindungsbibliotheken

Wir haben die internen Bibliotheken aktualisiert, mit denen Evertag mit **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** und anderen Diensten kommuniziert. Das Ergebnis: weniger Verbindungsfehler in Sonderfällen, bessere Unterstützung für neuere Server-Versionen und mehr Zuverlässigkeit beim Bearbeiten von Tags an entfernten Dateien.

### Übersetzungs- und Lokalisierungsfixes

Mehrere Sprachfixes in der Oberfläche basierend auf direktem Nutzerfeedback. Bessere Textanpassung an kleineren Schaltflächen in mehreren Sprachen.

### Kleinere Verbesserungen, inspiriert von eurem Feedback

Viele kleinere Verbesserungen aus App-Store-Bewertungen und E-Mails an support@everappz.com. Wir lesen jede Nachricht.

## Hol dir Evertag 4.2

[**Lade Evertag aus dem App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) oder aktualisiere im App Store. Evertag ist ein kostenloser Download mit optionalen In-App-Upgrades für erweiterte Funktionen. Die neuen Cloud-Verbindungen, Netzwerkprotokolle, Wi-Fi-Drive-Verbesserungen und die Liquid-Glass-Oberfläche sind Teil des Basis-Updates.

Wenn dir die App gefällt, hinterlasse bitte eine Bewertung im App Store — das hilft wirklich. Feedback oder Probleme? Schreib uns an **support@everappz.com**. Wir lesen jede Nachricht.

## Häufig gestellte Fragen

{{% details title="Was ist neu in Evertag 4.2?" closed="true" %}}
Evertag 4.2 fügt mehr als 6 neue Cloud- und Server-Verbindungen hinzu (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), bringt ein aufgefrischtes Wi-Fi Drive mit Mehrfachauswahl und intelligenterer Upload-Warteschlange, Liquid-Glass-UI-Updates, aktualisierte Verbindungsbibliotheken, wichtige Fehlerbehebungen bei der Tag-Bearbeitung und Übersetzungsverbesserungen.
{{% /details %}}

{{% details title="Soll ich in Evertag ID3v2.4 oder ID3v2.3 verwenden?" closed="true" %}}
Verwende **ID3v2.4** für moderne Player (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, moderne Android-Apps) und für Bibliotheken mit nicht-lateinischen Zeichen — die UTF-8-Unterstützung sorgt für saubere Chinesisch-, Koreanisch-, Japanisch-, Russisch-, Arabisch- und Hebräisch-Tags. Verwende **ID3v2.3**, wenn deine Tags in einigen Apps falsch dargestellt werden, du auf ältere Autoradios zielst oder eine Streaming-Distributor-Pipeline v2.4 ablehnt. Du kannst jederzeit umschalten und neu speichern.
{{% /details %}}

{{% details title="Warum sind meine Tags nach dem Bearbeiten in Spotify falsch?" closed="true" %}}
Spotify zeigt überwiegend Metadaten aus dem eigenen Katalog — deine lokalen Tags werden nur für „Local Files" oder für Inhalte verwendet, die du als Künstler hochgeladen hast. Wenn du Dateien für Spotify Local Files verschlagwortest und sie nicht korrekt angezeigt werden, deaktiviere ID3v2.4 in Evertag und speichere als ID3v2.3 — Spotifys Parser war historisch konservativ bei v2.4.
{{% /details %}}

{{% details title="Welche Albumcover-Größe sollte ich in Evertag wählen?" closed="true" %}}
Für die meisten Nutzer: **Groß**. Sieht auf Smartphones, iPads, Macs und modernen Auto-Displays großartig aus, ohne die Dateien zu sehr aufzublähen. Verwende **Mittel**, wenn du eine riesige Bibliothek hast und Speicher sparen willst. Verwende **Original** (keine Skalierung) nur für Archiv-Master oder wenn du wirklich maximale Qualität brauchst — beachte aber, dass einige ältere Player mit sehr großen eingebetteten Covern Probleme haben. **Original** ist Teil des Premium-Personalisierungs-Upgrades von Evertag.
{{% /details %}}

{{% details title="Werden größere Albumcover meine Dateien größer machen?" closed="true" %}}
Ja. Ein 3.000 × 3.000 px Cover einzubetten kann einer einzelnen Audiodatei mehrere Megabyte hinzufügen. Über eine 1.000-Track-Bibliothek summiert sich das zu Gigabyte. Wenn der Speicher knapp ist, nutze Mittel oder Groß; wenn du von einem NAS streamst, wo Größe egal ist, sind Sehr groß oder Original okay.
{{% /details %}}

{{% details title="Was sind doppelte Tags und sollte ich sie aktivieren?" closed="true" %}}
Doppelte Tags schreiben die Kern-Metadaten sowohl in die ID3v1- (legacy 128 Byte) als auch in die ID3v2-Sektion (modern) der Datei. Aktiviere es nur, wenn du auf sehr alte Player oder Hardware zielst, die ID3v1 liest. Für alles Moderne (Smartphones, Computer, neuere Autoradios) lass es aus.
{{% /details %}}

{{% details title="Bearbeitet Evertag Tags direkt auf Cloud-Dateien?" closed="true" %}}
Ja. Verbinde dich mit deiner Cloud (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 usw.) oder via FTP/SFTP/NFS, öffne eine Datei und bearbeite Tags wie bei einer lokalen Datei. Evertag lädt die Datei herunter, wendet deine Bearbeitungen an und lädt die aktualisierte Version wieder hoch. In den Einstellungen kannst du zwischen den Modi „Immer fragen", „Auto-Upload" oder „Nicht hochladen" wählen.
{{% /details %}}

{{% details title="Kann ich FLAC-Tags auf dem iPhone mit Evertag bearbeiten?" closed="true" %}}
Ja. Evertag unterstützt FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE und andere wichtige Formate mit voller Lese-/Schreibunterstützung für Tags inklusive eingebetteter Cover.
{{% /details %}}

{{% details title="Wie bearbeite ich Tags sicher auf meinem Heimserver via SFTP?" closed="true" %}}
Öffne Evertag, gehe zu Verbindungen, wähle SFTP und gib Hostname oder IP-Adresse deines Servers, Port (in der Regel 22), Benutzernamen und entweder ein Passwort oder einen privaten SSH-Schlüssel ein. Evertag durchsucht deine entfernten Ordner und bearbeitet Tags direkt mit Ende-zu-Ende-Verschlüsselung über SSH.
{{% /details %}}

{{% details title="Kann ich Tags an mehreren Dateien gleichzeitig bearbeiten?" closed="true" %}}
Ja. Aktiviere **Dateien gleichzeitig bearbeiten** in den Einstellungen. Wähle mehrere Dateien aus, öffne den Tag-Editor und jedes Feld, das du änderst, wirkt sich auf alle ausgewählten Dateien aus. Der schnellste Weg, denselben Albumkünstler, das gleiche Jahr oder Genre für ein gesamtes Album zu setzen.
{{% /details %}}

{{% details title="Ist das Update auf Evertag 4.2 kostenlos?" closed="true" %}}
Ja. Evertag ist ein kostenloser Download im App Store, und 4.2 ist ein kostenloses Update für alle bestehenden Nutzer. Die neuen Cloud-Integrationen, Wi-Fi-Drive-Verbesserungen und die Liquid-Glass-Oberfläche sind Teil des Basis-Updates.
{{% /details %}}

{{% details title="Auf welchen Geräten ist Evertag 4.2 verfügbar?" closed="true" %}}
Evertag 4.2 läuft auf iPhone, iPad und Mac. Die iCloud-Drive-Synchronisierung hält deine Tag-Editor-Einstellungen geräteübergreifend konsistent.
{{% /details %}}
