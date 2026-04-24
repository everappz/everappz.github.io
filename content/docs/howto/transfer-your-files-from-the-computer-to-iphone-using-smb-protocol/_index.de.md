---
title: "Dateien vom Computer auf das iPhone übertragen mit dem SMB-Protokoll"
description: "Erfahren Sie, wie Sie große Dateien von Ihrem Mac oder Windows PC auf Ihr iPhone oder iPad mit Evermusic und dem SMB-Protokoll übertragen und darauf zugreifen. Eine Schritt-für-Schritt-Anleitung für nahtloses Streaming und Dateiverwaltung."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["Dateien auf iPhone übertragen SMB", "PC-Musik auf iPhone streamen", "Mac mit iPhone verbinden SMB", "Evermusic SMB Einrichtung", "auf Computerdateien vom iPhone zugreifen", "Windows Musikfreigabe iOS", "SMB Dateiübertragung Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Kurzfassung:** Verwenden Sie Evermusic auf Ihrem iPhone oder iPad, um auf Dateien zuzugreifen, die auf Ihrem Mac oder Windows PC über Ihr lokales Netzwerk via SMB gespeichert sind. Keine Kabel, kein iTunes, kein Cloud-Upload erforderlich. Aktivieren Sie die Dateifreigabe auf Ihrem Computer, verbinden Sie sich in der App und durchsuchen oder spielen Sie Ihre Dateien drahtlos ab.

Haben Sie eine umfangreiche Sammlung großer Dateien auf Ihrem MAC oder PC und möchten mühelos von Ihrem iPhone oder iPad darauf zugreifen? Unsere Apps bieten eine einfache Lösung.

Befolgen Sie diese Schritte, um den nahtlosen Zugriff zwischen Ihrem Computer und iOS-Gerät mit dem SMB-Protokoll zu ermöglichen:

## Schritt 1: SMB-Protokoll auf Ihrem Computer aktivieren

**Für MAC:**

1. Öffnen Sie die "Systemeinstellungen" auf Ihrem MAC.
2. Klicken Sie auf "Freigabe".
3. Aktivieren Sie den Dienst "Dateifreigabe".
4. Fügen Sie Ihren Musikordner zum Abschnitt "Freigegebene Ordner" hinzu. Fügen Sie einen Benutzer hinzu und wählen Sie die Berechtigungsstufe (Lesen & Schreiben oder Nur Lesen). Sie können "Jeder: Nur Lesen" für den hinzugefügten Musikordner wählen.

   ![Mac Einstellungsbildschirm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Merken Sie sich die Computer-URL (smb://192.168.xx.xx), da Sie diese in den nächsten Schritten benötigen.
6. Klicken Sie auf "Optionen" und aktivieren Sie "Dateien und Ordner über SMB freigeben".

   ![Mac Dateifreigabe-Bildschirm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Aktivieren Sie "Windows-Dateifreigabe" für verfügbare Konten.

   ![Mac SMB-Freigabe-Bildschirm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Für Windows PC:**

1. Klicken Sie mit der rechten Maustaste auf Ihren Musikordner.
2. Wählen Sie "Eigenschaften".
3. Navigieren Sie zur Registerkarte "Freigabe".
4. Klicken Sie auf "Freigeben..."
5. Wählen Sie die Personen aus, mit denen Sie den Ordner teilen möchten, und legen Sie die Berechtigungsstufe fest. Sie können "Jeder: Lesen" für den gewählten Musikordner auswählen.

   ![Windows SMB-Freigabe-Bildschirm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Klicken Sie auf "Fertig".
7. Klicken Sie im Fenster "Dateifreigabe" auf "Fertig" und merken Sie sich den Ordnerpfad.

   ![Windows SMB freigegebener Ordner](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Schritt 2: Ihr iOS-Gerät verbinden

1. Öffnen Sie die App auf Ihrem iPhone oder iPad.
2. Gehen Sie zur Registerkarte "Verbindungen".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic Verbindungen-Bildschirm"
  caption="Evermusic Verbindungen-Bildschirm"
  width="400"
>}}

*Wenn Ihr Computer im Abschnitt "Verfügbare Geräte" erscheint:*

Wenn Ihr Computer im Abschnitt "Verfügbare Geräte" sichtbar ist und Sie im vorherigen Schritt "Jeder: Nur Lesen" ausgewählt haben, tippen Sie einfach auf Ihren Computer und er wird automatisch verbunden.

*Wenn Ihr Computer nicht automatisch erscheint:*

1. Tippen Sie auf "Cloud-Dienst verbinden".
2. Wählen Sie "SMB" auf dem Bildschirm "Cloud-Dienst verbinden".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic Cloud-Dienst verbinden Bildschirm"
  caption="Evermusic Cloud-Dienst verbinden Bildschirm"
  width="400"
>}}

3. Geben Sie auf dem Bildschirm "SMB-Verbindung" die Server-URL mit dem Pfad des freigegebenen Ordners ein. Sie können den Servernamen oder die Server-IP verwenden:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Geben Sie Ihren Benutzernamen und Ihr Passwort ein oder lassen Sie diese Felder leer, wenn Sie im vorherigen Schritt "Jeder: Nur Lesen" ausgewählt haben.
5. Das Feld "WORKGROUP" ist optional und sollte verwendet werden, wenn Sie ein Active Directory Domain haben.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMB-Connector-Bildschirm"
  caption="Evermusic SMB-Connector-Bildschirm"
  width="400"
>}}

6. Nachdem Sie Ihren Computer über das SMB-Protokoll verbunden haben, erscheint er im Abschnitt "Cloud-Dienste" auf dem Bildschirm "Verbindungen".
7. Öffnen Sie den verbundenen Dienst und navigieren Sie zum gewünschten Ordner.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Evermusic geöffneter SMB-Ordner"
  caption="Evermusic geöffneter SMB-Ordner"
  width="400"
>}}

8. Sie können den integrierten Dateimanager verwenden, um Ihre Dateien nach Bedarf zu bearbeiten.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic Dateimanager"
  caption="Evermusic Dateimanager"
  width="400"
>}}

## Schritt 3: Workaround für SMB2-Ordner mit Sonderzeichen

Manchmal können Probleme mit Ordnern auftreten, die Sonderzeichen enthalten, wenn Sie das SMB2-Protokoll verwenden. Hier sind einige Schritte zur Lösung dieses Problems:

1. **SMB 1 aktivieren:**  
   • Als vorübergehende Lösung versuchen Sie, SMB 1 auf Ihrem Server und in den App-Einstellungen zu aktivieren. Dies kann helfen, die Probleme mit Sonderzeichen in Ordnernamen zu umgehen.

2. **System-Dateiöffnungsmenü verwenden:**  
   • Navigieren Sie zu "Lokale Dateien".  
   • Scrollen Sie nach unten zum Abschnitt "Dateien auf diesem Gerät".  
   • Tippen Sie auf "Dateien öffnen..." oder "Ordner öffnen...".  
   • Finden Sie Ihren Server und wählen Sie die benötigten Dateien oder Ordner aus.  
   • Tippen Sie auf "Öffnen", um Ihre Auswahl zu bestätigen.

3. **Alternative Protokolle:**  
   • Wenn das Problem weiterhin besteht, erwägen Sie die Verbindung zu Ihrem NAS über WebDAV- oder DLNA-Protokolle, falls Ihr NAS diese Optionen unterstützt. Diese Protokolle können Sonderzeichen möglicherweise besser verarbeiten.

Durch Befolgen dieser Schritte können Sie die Probleme mit Sonderzeichen in Ordnernamen bei Verwendung des SMB2-Protokolls beheben.

## Fazit

Mit diesen Schritten können Sie mühelos auf Ihre umfangreiche Sammlung von Dateien von Ihrem MAC oder PC auf Ihrem iPhone oder iPad mit unseren Apps zugreifen.

## Häufig gestellte Fragen

{{% details title="Kann ich ohne iTunes auf Dateien auf meinem PC von meinem iPhone zugreifen?" closed="true" %}}
Ja. Evermusic verbindet sich über SMB in Ihrem lokalen Wi-Fi-Netzwerk mit Ihrem Computer. Keine iTunes- oder Finder-Synchronisierung erforderlich. Aktivieren Sie die Dateifreigabe auf Ihrem PC und verbinden Sie sich direkt über die App.
{{% /details %}}

{{% details title="Funktioniert der SMB-Dateizugriff über das Internet?" closed="true" %}}
Nein. SMB ist ein lokales Netzwerkprotokoll. Ihr iPhone und Computer müssen sich im selben Wi-Fi-Netzwerk befinden. Für den Fernzugriff laden Sie Dateien in einen Cloud-Dienst wie Google Drive oder Dropbox hoch und verbinden Sie sich in Evermusic damit.
{{% /details %}}

{{% details title="Auf welche Dateitypen kann ich über SMB zugreifen?" closed="true" %}}
Evermusic unterstützt MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC und andere Audioformate. Sie können auch Nicht-Audio-Dateien mit dem integrierten Dateimanager durchsuchen und verwalten.
{{% /details %}}

{{% details title="Kann ich Dateien von einem NAS auf mein iPhone per SMB übertragen?" closed="true" %}}
Ja. Die meisten NAS-Geräte (Synology, QNAP, WD My Cloud und andere) unterstützen SMB. Verbinden Sie sich mit Ihrem NAS mit denselben Schritten in dieser Anleitung.
{{% /details %}}

{{% details title="Muss ich Dateien auf mein iPhone kopieren, um sie abzuspielen?" closed="true" %}}
Nein. Evermusic streamt Dateien direkt von Ihrem Computer oder NAS über das Netzwerk. Dateien werden nicht auf Ihr iPhone kopiert, es sei denn, Sie wählen, sie für die Offline-Wiedergabe herunterzuladen.
{{% /details %}}

{{% details title="Ist SMB-Dateifreigabe sicher?" closed="true" %}}
Die SMB-Dateifreigabe funktioniert nur in Ihrem lokalen Netzwerk. Andere Geräte in anderen Netzwerken können nicht auf Ihre freigegebenen Ordner zugreifen. Für zusätzliche Sicherheit verwenden Sie einen Benutzernamen und ein Passwort anstelle des anonymen (Jeder) Zugangs.
{{% /details %}}
