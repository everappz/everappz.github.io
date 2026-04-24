---
title: "Streame deine Musik vom Mac oder PC auf das iPhone mit SMB"
description: "Erfahre, wie du deine Musiksammlung vom Mac oder Windows-PC auf dein iPhone oder iPad mit Evermusic und dem SMB-Protokoll streamen kannst. Eine einfache Schritt-für-Schritt-Anleitung zum Verbinden und Genießen von Audio ohne Synchronisierung."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["Musik vom Mac auf iPhone streamen", "SMB Audio-Streaming iOS", "Evermusic SMB Einrichtung", "PC Musik mit iPhone verbinden", "Mac Musik teilen iOS", "SMB Windows Datei-Streaming", "Evermusic PC-Ordner Zugriff"]
---

{{< author-byline >}}


**Kurzfassung:** Verwende die Evermusic-App für iPhone oder iPad, um Musik von deinem Mac oder Windows-PC über dein lokales Netzwerk mit SMB zu streamen. Keine Synchronisierung, kein Kopieren -- aktiviere einfach die Dateifreigabe auf deinem Computer, verbinde dich in der App und spiele ab. Die Einrichtung dauert weniger als 5 Minuten.

Ertrinkst du in einem Meer von Musik auf deinem MAC oder PC und möchtest sie problemlos auf deinem iPhone oder iPad genießen? Dann ist Evermusic genau das Richtige für dich. Mit Evermusic ist es unglaublich einfach, deinen Computer über das SMB-Protokoll zu verbinden und deine Lieblingsmusik zu streamen, ohne dir Sorgen über zusätzlichen Speicherplatz oder Synchronisierungsprobleme machen zu müssen. Hier ist eine Schritt-für-Schritt-Anleitung zum Einstieg:

## Schritt 1: SMB-Protokoll auf deinem Computer aktivieren

![Evermusic - SMB-Unterstützung - Mac Freigabe-Bildschirm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Wenn du MAC verwendest

- Öffne Systemeinstellungen -> Freigabe.
- Aktiviere den Dateifreigabe-Dienst.
- Im Abschnitt "Freigegebene Ordner" füge deinen Musikordner hinzu, wähle einen Benutzer und stelle die Berechtigungsstufen ein (Lesen & Schreiben oder Nur Lesen).
- Für zusätzlichen Komfort kannst du "Jeder: Nur Lesen" für den Musikordner auswählen, wodurch er in Evermusic leicht zugänglich wird.
- Vergiss nicht, dir die URL deines Computers (smb://192.168.xx.xx) für die nächsten Schritte zu merken.

![Evermusic - SMB-Unterstützung - Dateifreigabe-Bildschirm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Tippe auf "Optionen" und aktiviere "Dateien und Ordner über SMB freigeben."
- Aktiviere "Windows-Dateifreigabe" für verfügbare Konten.

![Evermusic - SMB-Unterstützung - Dateien und Ordner freigeben Bildschirm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Wenn du einen Windows-PC verwendest

![Evermusic - SMB-Unterstützung - Dateien unter Windows freigeben](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Klicke mit der rechten Maustaste auf deinen Musikordner.
- Wähle "Eigenschaften."
- Öffne den Reiter "Freigabe."
- Klicke auf "Freigeben..."
- Wähle die Personen aus, mit denen du teilen möchtest, und stelle deren Berechtigungsstufen ein.
- Wie beim MAC kannst du "Jeder: Lesen" für den ausgewählten Musikordner wählen.
- Klicke auf "Fertig", um deine Einstellungen zu speichern.

![Evermusic - SMB-Unterstützung - Freigegebener Ordner unter Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Schritt 2: Deinen Computer automatisch hinzufügen

- Öffne nun Evermusic und gehe zum Tab "Verbindungen" ("Netzwerk" wenn du eine ältere App-Version verwendest).
- Wenn du deinen Computer im Abschnitt "Verfügbare Geräte" ("Verfügbare Freigaben" wenn du eine ältere App-Version verwendest) siehst und im vorherigen Schritt "Jeder: Nur Lesen" ausgewählt hast, tippe einfach auf deinen Computer und er verbindet sich automatisch.
- Falls dies nicht geschieht, kannst du deinen Computer manuell hinzufügen.

![Evermusic - SMB-Unterstützung - Konto verbinden Bildschirm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Schritt 3: Deinen Computer manuell hinzufügen

- Tippe auf "Cloud-Dienst verbinden" ("Konto hinzufügen" wenn du eine ältere App-Version verwendest)
- Wähle "SMB" aus der Liste der verfügbaren Server auf dem nächsten Bildschirm.
- Auf dem "SMB"-Einstellungsbildschirm:
  - Gib die Server-URL mit dem Pfad zum freigegebenen Ordner ein. Du kannst den Servernamen oder die Server-IP eingeben. Zum Beispiel:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Gib deinen Benutzernamen und dein Passwort ein oder lasse diese Felder leer, wenn du im vorherigen Schritt "Jeder: Nur Lesen" ausgewählt hast.
  - Das Feld "WORKGROUP" ist optional und sollte verwendet werden, wenn du eine Active Directory-Domäne hast.

![Evermusic - SMB-Unterstützung - Anmeldedaten eingeben Bildschirm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Sobald du dein SMB-Konto verbunden hast, erscheint es im Abschnitt "Cloud-Dienste" ("Konten"). Öffne das verbundene Konto durch Tippen, navigiere zum Musikordner und tippe auf eine beliebige Audiodatei, um den Player zu starten.

![Evermusic - SMB-Unterstützung - Verbundenen Ordner öffnen Bildschirm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Genieße deine Musiksammlung nahtlos auf deinem iPhone oder iPad mit Evermusic.

![Evermusic - SMB-Unterstützung - Audio-Player Bildschirm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Schritt 4: SMB2-Workaround

Wenn du Probleme beim Durchsuchen von Ordnern oder beim Abspielen von Dateien mit Sonderzeichen (wie ü, ö, é) hast, kann dies mit dem SMB2-Protokoll zusammenhängen. Wir arbeiten aktiv an der Lösung dieses Problems.

Als vorübergehende Lösung versuche bitte, SMB 1 auf deinem Server und in den App-Einstellungen zu aktivieren. Alternativ kannst du dich über das System-Dateiöffnungsmenü mit deinem SMB-Server verbinden. So geht's:

1. Navigiere zu "Lokale Dateien."
2. Scrolle nach unten zum Abschnitt "Dateien auf diesem Gerät" und tippe auf "Dateien öffnen..." oder "Ordner öffnen..."
3. Finde deinen Server und wähle die benötigten Dateien oder Ordner aus.
4. Tippe auf "Öffnen", um deine Auswahl zu bestätigen.

## Schritt 5: WebDAV-Workaround

Zusätzlich kannst du versuchen, dich mit deinem NAS über WebDAV- oder DLNA-Protokolle zu verbinden, sofern diese unterstützt werden.

Durch Befolgen dieser Schritte kannst du die Probleme mit Sonderzeichen in Dateinamen umgehen und deine Mediendateien weiterhin genießen.

P.S. Du kannst auch Audiodateien von deinem MAC/PC auf dein iPhone mit iTunes Dateifreigabe übertragen und lokale Audiodateien abspielen. Erfahre mehr über diese Funktion in unserem Leitfaden: [So spielst du iTunes-Dateien auf dem iPhone ab](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Häufig gestellte Fragen

{{% details title="Kann ich Musik von meinem PC auf mein iPhone ohne iTunes streamen?" closed="true" %}}
Ja. Evermusic verbindet sich über SMB mit deinem PC in deinem lokalen Wi-Fi-Netzwerk. iTunes ist nicht erforderlich. Aktiviere einfach die Dateifreigabe auf deinem PC und verbinde dich in der App.
{{% /details %}}

{{% details title="Verbraucht SMB-Streaming mobile Daten?" closed="true" %}}
Nein. SMB funktioniert über dein lokales Wi-Fi-Netzwerk. Keine Internetverbindung oder mobile Daten werden benötigt.
{{% /details %}}

{{% details title="Welche Audioformate unterstützt Evermusic über SMB?" closed="true" %}}
Evermusic unterstützt MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC und andere gängige Audioformate. Dateien werden direkt von der SMB-Freigabe abgespielt.
{{% /details %}}

{{% details title="Kann ich Musik von einem NAS auf mein iPhone streamen?" closed="true" %}}
Ja. Wenn dein NAS SMB unterstützt (die meisten tun das, einschließlich Synology, QNAP und WD My Cloud), kannst du dich mit den gleichen Schritten in dieser Anleitung verbinden.
{{% /details %}}

{{% details title="Muss ich meinen Computer während des Streamings eingeschaltet lassen?" closed="true" %}}
Ja. Da Evermusic Dateien direkt von deinem Computer streamt, muss er eingeschaltet und mit demselben Netzwerk wie dein iPhone verbunden sein.
{{% /details %}}

{{% details title="Gibt es ein Dateigrößenlimit für SMB-Streaming?" closed="true" %}}
Nein. Evermusic streamt Dateien jeder Größe über SMB. Große verlustfreie Dateien (FLAC, WAV) funktionieren ohne Probleme.
{{% /details %}}
