---
title: "So verbinden Sie Synology NAS und hören Musik auf Ihrem iPhone oder Mac"
date: 2024-09-19
description: "Erfahren Sie, wie Sie Ihr Synology NAS über die native API oder QuickConnect verbinden und hochwertige Musik auf Ihrem iPhone oder Mac mit Evermusic und Flacbox streamen."
keywords: ["synology nas", "Musik streamen", "quickconnect", "evermusic synology", "flacbox synology", "nas Musikplayer", "iphone nas Musik"]
tags: ["Musik", "Streaming", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Zusammenfassung:** Verbinden Sie Ihr Synology NAS mit Evermusic oder Flacbox über die native Synology-API -- entweder manuell über die IP-Adresse oder automatisch über die QuickConnect ID. QuickConnect ermöglicht es Ihnen, Musik aus der Ferne zu streamen, ohne Portweiterleitung. Beide Apps unterstützen FLAC, MP3, WAV und andere Hi-Res-Formate.

Wenn Sie nach einer nahtlosen Möglichkeit suchen, Ihr Synology NAS zu verbinden und Ihre Musikbibliothek auf Ihrem iPhone oder Mac zu genießen, sind die Evermusic und Flacbox Apps die perfekten Lösungen. Diese Apps unterstützen eine breite Palette von Audioformaten, darunter FLAC, MP3 und WAV, wodurch es einfach wird, hochwertige Musik direkt von Ihrem Synology NAS zu streamen und anzuhören.

In dieser Anleitung zeigen wir Ihnen, wie Sie Ihr Synology NAS mit der Evermusic oder Flacbox App über die native Synology-API und die QuickConnect-Funktion verbinden. Durch die Nutzung der direkten Synology-API können Sie sicher auf Ihre Musikbibliothek außerhalb Ihres Heimnetzwerks zugreifen, ohne komplizierte Konfigurationen wie WebDAV, SMB, DLNA einrichten zu müssen. Mit QuickConnect können Sie Ihre Musik von überall aus streamen und verwalten, mit Ihrem iPhone oder Mac.

## Schritt 1: Berechtigungen für freigegebene Ordner konfigurieren (Optional)

1. Öffnen Sie die **Systemsteuerung** und gehen Sie zum Abschnitt **Gemeinsamer Ordner**.

![Gemeinsamer Ordner](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Wählen Sie den Ordner **Musik** und klicken Sie auf **Bearbeiten**.

3. Konfigurieren Sie auf der Registerkarte **Berechtigungen** die Zugriffsrechte. Aktivieren Sie den Gastzugang mit Nur-Lesen-Berechtigung, wenn Sie nur Musik hören möchten, oder Lesen/Schreiben, wenn Sie Dateien ändern müssen. Speichern Sie die Änderungen.

![Berechtigungen](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Schritt 2: IP-Adresse des Synology NAS finden

1. Öffnen Sie die **Systemsteuerung** und gehen Sie zur Registerkarte **Netzwerkschnittstelle**.

![Netzwerkschnittstelle](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Oder verwenden Sie Ihren Webbrowser, um [find.synology.com](http://find.synology.com) zu besuchen.

![Synology finden](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Notieren Sie die IP-Adresse Ihres Synology NAS (z.B. 192.168.18.137).

## Schritt 3: Netzwerkports des Synology NAS finden

Die offizielle Synology-Dokumentation für die Standard-Netzwerkports von DSM finden Sie in diesem [Synology Knowledge Center-Artikel](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM verwendet die folgenden Standardports:
- **HTTP (Webzugriff):** Port **5000**
- **HTTPS (Sicherer Webzugriff):** Port **5001**

Dies sind die Standardports für den Zugriff auf die DSM-Oberfläche.

![Netzwerkports](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Schritt 4: QuickConnect ID-Funktion aktivieren

Eine Synology QuickConnect ID ist eine eindeutige Kennung, mit der Sie von überall aus über das Internet auf Ihr Synology NAS zugreifen können, ohne komplizierte Netzwerkeinstellungen wie Portweiterleitung konfigurieren zu müssen. QuickConnect vereinfacht den Fernzugriff, indem es die Server von Synology nutzt, um eine Verbindung zwischen Ihrem NAS und Ihrem Gerät, wie Ihrem Smartphone oder Computer, über die QuickConnect ID herzustellen.

**So finden oder richten Sie Ihre QuickConnect ID ein:**

1. **Melden Sie sich bei DSM an.**
2. Gehen Sie zu **Systemsteuerung > Externer Zugriff > QuickConnect**.
3. **Aktivieren Sie QuickConnect** und erstellen oder sehen Sie Ihre eindeutige QuickConnect ID.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Schritt 5: Verbindung zum Synology NAS auf Ihrem iPhone/Mac mit Evermusic oder Flacbox herstellen

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) und [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) sind Musikplayer-Apps, die für iOS- und macOS-Geräte entwickelt wurden, die jeweils einzigartige Funktionen und Möglichkeiten zur Verwaltung und zum Genuss Ihrer Musikbibliothek bieten.

1. Öffnen Sie die Evermusic oder Flacbox App und gehen Sie zur Registerkarte **Verbindungen**.

![Verbindungen](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Wählen Sie **Cloud-Dienst verbinden** und wählen Sie **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Sie haben zwei Verbindungsoptionen: **manuell** über die IP-Adresse und den Port des Servers, oder **automatisch** über die QuickConnect ID.

### Manuelle Verbindung

Für die manuelle Methode benötigen Sie die direkte IP-Adresse und Portnummer, die Sie in den vorherigen Schritten ermittelt haben.

1. Geben Sie die Server-URL ein, die Sie in Schritt 2 erhalten haben, im folgenden Format: PROTOKOLL://IP_ADRESSE:PORTNUMMER
   - Verwenden Sie **Port 5000** für HTTP und **Port 5001** für HTTPS-Verbindungen.

   Zum Beispiel:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Die tatsächliche Portnummer kann in Schritt 3 Ihrer Einrichtung bestätigt werden.
3. Geben Sie Ihren **Benutzernamen** und Ihr **Passwort** für das Synology NAS ein.
4. Tippen Sie auf **Anmelden**, um die Verbindung herzustellen.

![Manuelle Verbindung](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automatische Verbindung

Für die automatische Verbindung verwenden Sie die **QuickConnect ID** aus Schritt 4. Anstatt die IP-Adresse und Portnummer Ihres Synology NAS manuell einzugeben, geben Sie einfach die **QuickConnect ID** ein. Die App ruft automatisch die erforderlichen Verbindungsinformationen ab.

Diese Methode ermöglicht es Ihnen, auch außerhalb Ihres Heimnetzwerks auf Ihr NAS zuzugreifen, sodass Sie Ihre Dateien über das Internet verwalten können, ohne Portweiterleitung oder statische IP-Adressen konfigurieren zu müssen.

![Automatische Verbindung](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Zwei-Faktor-Authentifizierung

Ab DSM 4.2 führte Synology die **2-Schritt-Verifizierung** ein, um die Sicherheit zu erhöhen. Diese Funktion erfordert zusätzlich zu Ihren regulären Anmeldedaten einen **Einmalpasswort (OTP)**-Code, der von einer Authentifizierungs-App generiert wird. Wenn Sie die 2-Schritt-Verifizierung aktiviert haben, müssen Sie nach der Eingabe Ihres Benutzernamens und Passworts auch das OTP eingeben, um sich bei Ihrer DSM-Sitzung anzumelden.

Bitte beachten Sie, dass die App nach Ablauf Ihrer Sitzung manuell erneut autorisiert werden muss. Zur erneuten Autorisierung:

1. Gehen Sie zur Registerkarte **Verbindungen** in der App.
2. Tippen Sie auf die Schaltfläche **Weitere Aktionen** neben dem Servernamen.
3. Wählen Sie **Einstellungen** aus dem Menü, um den neuen Authentifizierungscode einzugeben und den Prozess der erneuten Autorisierung abzuschließen.

Dies stellt sicher, dass Ihre Daten auch dann sicher bleiben, wenn Sie von einem nicht vertrauenswürdigen Netzwerk auf Ihr NAS zugreifen.

## Schritt 6: Navigieren und Musik abspielen

1. Nach der Verbindung wird das Gerät in der Liste **Verbundene Geräte** angezeigt.

![Verbundene Geräte](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navigieren Sie zum Ordner **Musik** und tippen Sie auf eine beliebige Audiodatei, um die Wiedergabe zu starten.

![Musik abspielen](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Schritt 7: Verbundenen Cloud-Ordner zur Musikbibliothek hinzufügen

1. Öffnen Sie den Abschnitt **Musikbibliothek** in der App.
2. Wählen Sie **Musik hinzufügen** und wählen Sie **Verbindungen**.
3. Wählen Sie Ihren verbundenen NAS-Server und den Ordner **Musik**. Tippen Sie auf **Fertig**.
4. Die App scannt den Musikordner und fügt unterstützte Audiodateien zur Musikbibliothek hinzu. Metadaten werden geladen und Ihre Titel werden nach Album, Künstler und Genre gruppiert.

## Fazit

Wenn Sie diese Schritte befolgen, können Sie ganz einfach eine Verbindung auf Ihrem Synology NAS einrichten und Ihre gesamte Musikbibliothek mit Evermusic oder Flacbox auf Ihrem iPhone oder Mac streamen. Ob zu Hause oder unterwegs -- genießen Sie nahtlosen, hochwertigen Zugriff auf Ihre Lieblingsstücke von überall mit QuickConnect. Nutzen Sie die Flexibilität und den Komfort, den diese Apps bieten, und beginnen Sie, Ihre Musiksammlung mühelos auf all Ihren Geräten zu verwalten.

Mit sicherem Fernzugriff über QuickConnect und Unterstützung für eine breite Palette von Audioformaten sind Sie nie weit von Ihrer Musik entfernt. Jetzt sind Ihre auf dem NAS gespeicherten Dateien nur einen Fingertipp entfernt!

## FAQ

{{% details title="Was ist der Unterschied zwischen manueller Verbindung und QuickConnect?" closed="true" %}}
Die manuelle Verbindung verwendet die IP-Adresse und den Port des NAS, was in Ihrem lokalen Netzwerk funktioniert. QuickConnect nutzt den Relay-Dienst von Synology, um eine Verbindung von überall über das Internet herzustellen, ohne Portweiterleitung.
{{% /details %}}

{{% details title="Kann ich Musik vom Synology NAS außerhalb meines Heimnetzwerks streamen?" closed="true" %}}
Ja. Aktivieren Sie QuickConnect auf Ihrem Synology NAS und verwenden Sie die QuickConnect ID in Evermusic oder Flacbox, um Musik von überall mit einer Internetverbindung zu streamen.
{{% /details %}}

{{% details title="Welche Audioformate werden beim Streaming vom Synology NAS unterstützt?" closed="true" %}}
Evermusic und Flacbox unterstützen FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD und viele andere Formate. Alle unterstützten Formate funktionieren beim Streaming vom Synology NAS.
{{% /details %}}

{{% details title="Benötige ich Zwei-Faktor-Authentifizierung zum Verbinden?" closed="true" %}}
Nein, 2FA ist optional. Wenn Sie jedoch die 2-Schritt-Verifizierung auf Ihrem Synology DSM aktiviert haben, fragt die App während der Anmeldung nach einem Einmalpasswort. Sie müssen sich erneut autorisieren, wenn die Sitzung abläuft.
{{% /details %}}

{{% details title="Sollte ich die native Synology-API, WebDAV oder SMB zum Verbinden verwenden?" closed="true" %}}
Die native Synology-API mit QuickConnect ist die beste Wahl für den Fernzugriff. Für die Nutzung im lokalen Netzwerk ist SMB typischerweise die schnellste Option. WebDAV funktioniert gut für lokalen und Fernzugriff. Evermusic und Flacbox unterstützen alle drei Protokolle.
{{% /details %}}
