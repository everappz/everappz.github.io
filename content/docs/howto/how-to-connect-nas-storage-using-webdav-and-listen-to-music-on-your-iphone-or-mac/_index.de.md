---
title: "So verbinden Sie NAS-Speicher über WebDAV und hören Musik auf Ihrem iPhone oder Mac"
date: 2024-07-28
description: "Erfahren Sie, wie Sie WebDAV auf Ihrem Synology NAS konfigurieren und Musik auf Ihr iPhone oder Ihren Mac mit Evermusic oder Flacbox streamen. Folgen Sie unserer Schritt-für-Schritt-Anleitung."
keywords: ["NAS verbinden", "WebDAV Synology", "Musik streamen NAS", "Evermusic WebDAV", "Flacbox WebDAV", "WebDAV iPhone", "WebDAV Mac"]
tags: ["Musik", "Streaming", "Speicher", "NAS", "verbinden", "WebDAV"]
readingTime: 2
---

{{< author-byline >}}


**Kurzfassung:** Installieren und aktivieren Sie WebDAV auf Ihrem Synology NAS, konfigurieren Sie die Berechtigungen für freigegebene Ordner und verbinden Sie sich dann von Evermusic oder Flacbox aus mit der IP-Adresse des NAS und dem WebDAV-Port (Standard 5005/5006). Sie können Ihre gesamte Musikbibliothek streamen und verwalten, ohne Dateien auf Ihr Gerät zu kopieren.

Entdecken Sie, wie Sie Ihren NAS-Speicher über WebDAV verbinden und mühelos Ihre Musikbibliothek auf Ihr iPhone oder Ihren Mac streamen. WebDAV (Web-based Distributed Authoring and Versioning) ist ein Protokoll, mit dem Sie Dateien über das Internet verwalten und teilen können. Durch die Einrichtung von WebDAV auf Ihrem NAS können Sie auf Ihre Musiksammlung zugreifen und diese streamen, sodass Sie Ihre Lieblingssongs immer griffbereit haben.

In dieser Anleitung zeigen wir Ihnen, wie Sie eine WebDAV-Verbindung auf einem der beliebtesten NAS-Server, Synology NAS, einrichten. Folgen Sie unseren einfachen Schritten zur Konfiguration von WebDAV auf Ihrem Synology NAS, und Sie können Ihre Musikbibliothek direkt von Ihrem iPhone oder Mac aus durchsuchen, streamen und verwalten.

## Schritt 1: WebDAV auf Synology NAS installieren

1. Melden Sie sich bei Ihrem Synology NAS an und öffnen Sie das **Paketzentrum**.
2. Suchen Sie nach "webdav" und installieren Sie das WebDAV-Paket, falls es noch nicht installiert ist. Öffnen Sie den WebDAV-Server zur Konfiguration.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="WebDAV auf Synology installieren" width="600" >}}

## Schritt 2: WebDAV-Server konfigurieren

1. Aktivieren Sie auf der WebDAV-Einstellungsseite die Kontrollkästchen für **HTTP aktivieren**, **HTTPS aktivieren**, **Anonymes WebDAV aktivieren** und **DavDepthInfinity aktivieren**.
2. Klicken Sie auf **Übernehmen**, um die Änderungen zu speichern. Notieren Sie die Portnummern für HTTP- und HTTPS-Verbindungen, die standardmäßig 5005 und 5006 sind.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="WebDAV-Einstellungen konfigurieren" width="600" >}}

## Schritt 3: Berechtigungen für freigegebene Ordner konfigurieren

1. Öffnen Sie die **Systemsteuerung** und gehen Sie zum Abschnitt **Freigegebener Ordner**.
2. Wählen Sie den Ordner **Musik** und klicken Sie auf **Bearbeiten**.
3. Konfigurieren Sie auf der Registerkarte **Berechtigungen** die Berechtigungen. Aktivieren Sie den Gastzugang mit Nur-Lesen, wenn Sie nur Musik hören möchten, oder Lesen/Schreiben, wenn Sie Dateien ändern möchten. Speichern Sie die Änderungen.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Berechtigungen für freigegebene Ordner" width="600" >}}

## Schritt 4: IP-Adresse des Synology NAS finden

1. Öffnen Sie die **Systemsteuerung** und gehen Sie zur Registerkarte **Netzwerkschnittstelle**, oder verwenden Sie Ihren Webbrowser, um [find.synology.com](http://find.synology.com) zu besuchen.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="NAS-IP-Adresse finden" width="600" >}}

2. Notieren Sie die IP-Adresse Ihres Synology NAS (z. B. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP-Adresse" width="600" >}}

## Schritt 5: Mit Synology NAS über Evermusic/Flacbox verbinden

1. Öffnen Sie die Evermusic- oder Flacbox-App und gehen Sie zur Registerkarte **Verbindungen**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Registerkarte Verbindungen in Evermusic" width="600" >}}

2. Für die automatische Verbindung finden Sie Ihr Synology NAS im Abschnitt **Verfügbare Geräte** und tippen Sie darauf, um sich zu verbinden.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Liste der verfügbaren Geräte" width="600" >}}

3. Für die manuelle Verbindung wählen Sie **Cloud-Dienst verbinden** und wählen Sie **WebDAV**. Geben Sie die Serveradresse im Format ein: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (z. B. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Manuelle WebDAV-Konfiguration" width="600" >}}

4. Lassen Sie die Anmelde- und Passwortfelder für den Gastzugang leer, oder geben Sie Ihre Synology-Anmeldedaten ein. Tippen Sie auf **Anmelden**.

## Schritt 6: Musik durchsuchen und abspielen

1. Nach der Verbindung erscheint das Gerät in der Liste **Verbundene Zubehörteile**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Verbundene Geräte in Evermusic" width="600" >}}

2. Navigieren Sie zum Ordner **Musik** und tippen Sie auf eine beliebige Audiodatei, um die Wiedergabe zu starten.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Musikordner durchsuchen" width="600" >}}

## Schritt 7: Verbundenen Cloud-Ordner zur Musikbibliothek hinzufügen

1. Öffnen Sie den Abschnitt **Musikbibliothek** in der App.
2. Wählen Sie **Musik hinzufügen** und wählen Sie **Verbindungen**.
3. Wählen Sie Ihren verbundenen NAS-Server und den Ordner **Musik**. Tippen Sie auf **Fertig**.
4. Die App scannt den Musikordner und fügt unterstützte Audiodateien zur Musikbibliothek hinzu. Metadaten werden geladen und Ihre Titel werden nach Album, Künstler und Genre gruppiert.

## Fazit

Mit diesen Schritten können Sie ganz einfach eine WebDAV-Verbindung auf Ihrem Synology NAS einrichten und Ihre Musikbibliothek auf Ihr iPhone oder Ihren Mac mit Evermusic oder Flacbox streamen. Genießen Sie jederzeit nahtlosen Zugriff auf Ihre Lieblingssongs.

## FAQ

{{% details title="Welche NAS-Geräte unterstützen WebDAV?" closed="true" %}}
Die meisten beliebten NAS-Marken unterstützen WebDAV, darunter Synology, QNAP, TrueNAS und Western Digital. Überprüfen Sie die Dokumentation Ihres NAS-Herstellers für Anweisungen zur WebDAV-Einrichtung.
{{% /details %}}

{{% details title="Was ist der Unterschied zwischen WebDAV und SMB für das Musik-Streaming vom NAS?" closed="true" %}}
WebDAV funktioniert über HTTP/HTTPS und eignet sich besser für den Fernzugriff über das Internet. SMB ist in lokalen Netzwerken typischerweise schneller. Evermusic und Flacbox unterstützen beide Protokolle. Wählen Sie je nachdem, ob Sie lokalen oder Fernzugriff benötigen.
{{% /details %}}

{{% details title="Benötige ich einen Benutzernamen und ein Passwort für WebDAV auf Synology?" closed="true" %}}
Nein, wenn Sie den anonymen WebDAV-Zugang aktivieren und Gastberechtigungen für Ihren freigegebenen Ordner konfigurieren. Für bessere Sicherheit können Sie stattdessen Ihre Synology-Anmeldedaten verwenden.
{{% /details %}}

{{% details title="Kann ich FLAC und andere Hi-Res-Formate vom NAS über WebDAV streamen?" closed="true" %}}
Ja. Sowohl Evermusic als auch Flacbox unterstützen FLAC, ALAC, WAV, DSD und andere hochauflösende Formate beim Streamen vom NAS-Speicher über WebDAV.
{{% /details %}}

{{% details title="Warum kann die App meinen NAS nicht in den verfügbaren Geräten finden?" closed="true" %}}
Stellen Sie sicher, dass Ihr iPhone/Mac und der NAS im selben Wi-Fi-Netzwerk sind. Wenn die automatische Erkennung nicht funktioniert, verwenden Sie die manuelle Verbindungsoption und geben Sie die NAS-IP-Adresse und den WebDAV-Port direkt ein.
{{% /details %}}
