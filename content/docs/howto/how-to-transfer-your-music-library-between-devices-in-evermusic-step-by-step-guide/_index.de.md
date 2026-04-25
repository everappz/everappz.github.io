---
title: "So übertragen Sie Ihre Musikbibliothek zwischen Geräten in Evermusic: Schritt-für-Schritt-Anleitung"
description: "Übertragen Sie ganz einfach Ihre Evermusic-Musikbibliothek, Wiedergabelisten, Albumcover und Einstellungen von einem iPhone, iPad oder Mac auf ein anderes mit Wi-Fi Drive und Backup-Tools."
date: 2024-12-29
tags: ["Musikbibliothek", "Übertragung", "WLAN", "Backup", "webdav", "Wiederherstellung"]
keywords: ["Musikbibliothek übertragen Evermusic", "Backup und Wiederherstellung Wiedergabelisten Evermusic", "Evermusic WiFi Drive", "Evermusic zwischen Geräten synchronisieren", "Evermusic Datenbank verschieben", "Evermusic Dateiübertragung", "Audioplayer Einstellungen wiederherstellen", "WebDAV Musikübertragung iOS"]
readingTime: 3
---

{{< author-byline >}}


**Kurzfassung:** Um Ihre Evermusic-Bibliothek auf ein neues Gerät zu übertragen, erstellen Sie ein Backup auf dem Quellgerät, starten Sie Wi-Fi Drive, verbinden Sie das zweite Gerät über dasselbe Netzwerk, laden Sie das Backup und die Musikdateien herunter und stellen Sie dann das Backup wieder her. Der gesamte Vorgang dauert je nach Bibliotheksgröße etwa 10 Minuten.

In dieser Anleitung führen wir Sie durch die Übertragung Ihrer gesamten Musikbibliothek — einschließlich Datenbank, Albumcover und Einstellungen — von einem Gerät (iPhone oder Mac) auf ein anderes. Während die automatische Synchronisierung von Musikbibliothek und Wiedergabelisten eine für die Zukunft geplante Funktion ist, muss dieser Vorgang derzeit manuell durchgeführt werden.

## Schritt 1: Backup auf dem ersten Gerät erstellen

1. **Öffnen Sie die App auf Ihrem ersten Gerät** (dem Gerät mit Ihrer Musikbibliothek, Wiedergabelisten und verbundenen Cloud-Diensten).
2. **Navigieren Sie zu Einstellungen** und wählen Sie die Option **Backup und Wiederherstellung**.

![Backup und Wiederherstellung](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Wählen Sie auf dem Bildschirm **Backup und Wiederherstellung** die Elemente aus, die in Ihre Backup-Datei aufgenommen werden sollen:
   - **Datenbank** (enthält Ihre Musikbibliothek und Wiedergabelisten)
   - **Albumcover**
   - **Einstellungen**

Diese Optionen sind standardmäßig aktiviert.

![Backup-Optionen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Tippen Sie auf **Anwendungsdaten sichern**, um den Vorgang zu starten.

![Anwendungsdaten sichern](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Sobald das Backup abgeschlossen ist, erscheint eine Informationsmeldung.

![Backup abgeschlossen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Tippen Sie auf **Datei anzeigen**, um die Backup-Datei im Verzeichnis **Dokumente** anzuzeigen. Backup-Dateien werden normalerweise im Ordner **Backup** gespeichert.

![Backup-Datei anzeigen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Schritt 2: Wi-Fi Drive-Server starten

1. Gehen Sie zum Bereich **Verbindungen** in der App.
2. Scrollen Sie nach unten zu **Über Wi-Fi verbinden** und tippen Sie darauf.

![Über Wi-Fi verbinden](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Tippen Sie auf dem nächsten Bildschirm auf **Wi-Fi Drive starten**.

- Optional können Sie einen Benutzernamen und ein Passwort für die Sicherheit festlegen, dies ist jedoch für Heimnetzwerke nicht erforderlich.

4. Nach dem Start sehen Sie die verfügbaren Serveradressen. Dies kann für Desktop-Browser oder WebDAV-Apps verwendet werden, aber in dieser Anleitung fahren wir direkt mit den nächsten Schritten fort.

![Wi-Fi Drive gestartet](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Schritt 3: Zweites Gerät mit dem ersten verbinden

1. Öffnen Sie die App auf Ihrem zweiten Gerät (auf das Sie die Bibliothek übertragen möchten).
2. Stellen Sie sicher, dass beide Geräte mit demselben Wi-Fi-Netzwerk verbunden sind.
3. Öffnen Sie auf dem zweiten Gerät den Tab **Verbindungen** und wählen Sie **Verfügbare Geräte**.

![Verfügbare Geräte](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Sie sollten eine WebDAV-Verbindung namens **Evermusic** sehen (den Server, den wir auf dem ersten Gerät gestartet haben). Tippen Sie darauf, um sich zu verbinden.

5. Nach der Verbindung sehen Sie alle Ordner vom ersten Gerät.

![Mit erstem Gerät verbunden](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Schritt 4: Dateiübertragung vorbereiten

1. Gehen Sie auf dem zweiten Gerät zu **Einstellungen > Dateimanager** und aktivieren Sie **Heruntergeladene Dateien speichern in - Jedes Mal fragen**.

- Dies stellt sicher, dass Sie den Zielordner für jeden Download auswählen können.

2. Kehren Sie zum Tab **Verbindungen** zurück und navigieren Sie zum verbundenen WebDAV-Server.

![Dateiübertragung vorbereiten](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Schritt 5: Backup und Musikdateien übertragen

1. Öffnen Sie den Ordner **Backup** auf dem verbundenen WebDAV-Server.

![Backup-Ordner](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Tippen Sie auf die Schaltfläche **Weitere Aktionen** (drei Punkte) neben der Backup-Datei und wählen Sie **Herunterladen**.

3. Erstellen Sie einen **Backup**-Ordner auf dem zweiten Gerät zum Speichern der heruntergeladenen Dateien. Bestätigen Sie Ihre Auswahl durch Tippen auf **Fertig**.

![Backup herunterladen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Übertragen Sie weitere Musikdateien:
   - Prüfen Sie den Ordner **Downloads** oder andere relevante Ordner auf dem WebDAV-Server.

![Musikdateien übertragen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Verwenden Sie die Option **Auswählen**, um Dateien auszuwählen, und tippen Sie dann auf **Weitere Aktionen > Herunterladen**. Speichern Sie sie im entsprechenden Ordner auf dem zweiten Gerät, um die gleiche Verzeichnisstruktur beizubehalten.

Das Ziel ist es, alle Dateien von Ihrem ersten Gerät auf Ihr aktuelles Gerät zu übertragen und sicherzustellen, dass die Ordnerstruktur identisch bleibt. So bleiben die Verknüpfungen in Ihrer Musikbibliothek und Ihren Wiedergabelisten intakt. Beachten Sie, dass lokale Dateien, die außerhalb des Dokumentenverzeichnisses der App auf Ihrem ersten Gerät gespeichert sind, separat übertragen werden müssen. Da die App im Wi-Fi Drive-Modus nicht auf diese Dateien zugreifen kann, müssen Sie die System-Dateien-App für deren Übertragung verwenden.

![Übertragung abgeschlossen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Schritt 6: Übertragungsfortschritt überwachen

1. Gehen Sie auf dem zweiten Gerät zum Bereich **Lokale Dateien** (oder Tab **Downloads** auf iPad/Mac).

2. Tippen Sie auf die Schaltfläche **Übertragungsaktivität** in der oberen linken Ecke, um die Übertragungswarteschlange zu überwachen.

![Übertragung überwachen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Schritt 7: Daten aus dem Backup wiederherstellen

1. Sobald die Backup-Datei und alle benötigten Audiodateien auf das zweite Gerät heruntergeladen wurden, öffnen Sie den Ordner **Backup**.

2. Tippen Sie auf die Backup-Datei, und eine Bestätigungsmeldung wird angezeigt.

![Backup wiederherstellen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Hinweis:** Die Wiederherstellung ersetzt alle aktuellen Musikbibliotheksdaten, Wiedergabelisten, Einstellungen und Albumcover durch die Backup-Daten.

3. Tippen Sie auf **Wiederherstellen**, um den Vorgang zu starten.

![Wiederherstellungsprozess](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Nach Abschluss der Wiederherstellung bestätigt eine Meldung den Erfolg.

![Wiederherstellung abgeschlossen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Überprüfen Sie die Bereiche **Wiedergabelisten** oder **Musikbibliothek**, um die Wiederherstellung zu bestätigen.

![Wiederherstellung überprüfen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Schritt 8: Musikbibliothek neu indexieren

1. Für beste Ergebnisse indexieren Sie Ihre Bibliothek neu, um sicherzustellen, dass alle Dateien erfolgreich erkannt werden.

2. Gehen Sie zu **Einstellungen > Musikbibliothek > Offline-Musiksynchronisierung** und wählen Sie **Lokale Ordner scannen starten**.

Wenn Sie diese Schritte befolgen, übertragen Sie erfolgreich Ihre Musikbibliothek, Wiedergabelisten und Einstellungen auf ein anderes Gerät. Wenn Sie auf Probleme stoßen, zögern Sie nicht, den Support zu kontaktieren.

## Häufig gestellte Fragen

{{% details title="Kann ich meine Evermusic-Bibliothek ohne Wi-Fi übertragen?" closed="true" %}}
Wi-Fi Drive erfordert, dass beide Geräte im selben Wi-Fi-Netzwerk sind. Es gibt derzeit keine Bluetooth- oder Mobilfunk-Übertragungsoption. Alternativ können Sie AirDrop oder die Dateien-App verwenden, um die Backup-Datei und Musikordner manuell zwischen Geräten zu verschieben.
{{% /details %}}

{{% details title="Werden meine Cloud-Dienst-Verbindungen mit dem Backup übertragen?" closed="true" %}}
Das Backup enthält Ihre Datenbank, Wiedergabelisten, Albumcover und Einstellungen. Anmeldedaten für Cloud-Dienste sind aus Sicherheitsgründen nicht enthalten. Sie müssen Ihre Cloud-Konten nach der Wiederherstellung auf dem neuen Gerät erneut verbinden.
{{% /details %}}

{{% details title="Was passiert mit meiner bestehenden Bibliothek auf dem zweiten Gerät?" closed="true" %}}
Die Wiederherstellung eines Backups ersetzt alle vorhandenen Musikbibliotheksdaten, Wiedergabelisten, Einstellungen und Albumcover auf dem zweiten Gerät. Erstellen Sie zuerst ein separates Backup des zweiten Geräts, wenn Sie dessen Daten beibehalten möchten.
{{% /details %}}

{{% details title="Funktioniert dieser Vorgang zwischen iPhone und Mac?" closed="true" %}}
Ja. Evermusic unterstützt die Wi-Fi Drive-Übertragung zwischen jeder Kombination von iPhone, iPad und Mac. Beide Geräte müssen nur im selben Wi-Fi-Netzwerk sein.
{{% /details %}}

{{% details title="Wie lange dauert die Übertragung?" closed="true" %}}
Die Übertragungszeit hängt von der Größe Ihrer Musikbibliothek und Ihrer Wi-Fi-Geschwindigkeit ab. Eine typische Bibliothek von einigen Gigabyte wird in 5-15 Minuten über ein Standard-Heimnetzwerk übertragen.
{{% /details %}}
