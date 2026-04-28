---
title: "So verbinden Sie den internen Speicher des Bluesound VAULT mit Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Erfahren Sie, wie Sie von Evermusic, Flacbox und Evertag aus über das SMB-Protokoll auf die interne Festplatte des Bluesound VAULT zugreifen, um Audiodateien zu verwalten, zu bearbeiten und abzuspielen."
keywords: ["bluesound vault", "smb-speicher verbinden", "evermusic smb", "flacbox vault", "evertag smb", "nas-speicher musik", "vault internes laufwerk"]
tags: ["evermusic", "verbinden", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Zusammenfassung:** Verbinden Sie sich über SMB mit dem internen Speicher Ihres Bluesound VAULT mit Evermusic, Flacbox oder Evertag. Finden Sie die IP-Adresse des VAULT in der BluOS-App, geben Sie sie als SMB-Verbindung mit Gastzugang ein und beginnen Sie, Ihre Musikdateien abzuspielen oder zu verwalten.

Der Bluesound VAULT verfügt über eine interne Festplatte und fungiert als Netzwerkspeicher (NAS). Der Zugriff auf die interne Festplatte des VAULT ermöglicht es Ihnen, Dateien hinzuzufügen/zu löschen und Metadaten-Tags aus unseren Apps Evermusic, Flacbox, Evertag zu bearbeiten.

**Im Folgenden finden Sie die Schritte zum Zugriff auf die interne Festplatte Ihres VAULT:**

1. Wählen Sie in der BluOS-App **Hilfe > Diagnose**.

2. Ermitteln Sie auf der Seite **Diagnose** die **IP-Adresse** des VAULT. Diese **IP-Adresse** wird in den nächsten Schritten verwendet.

3. Öffnen Sie Evermusic, Flacbox oder Evertag.

   ![Everappz-Anwendungen](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Öffnen Sie den Bildschirm "Verbindungen" und wählen Sie den Menüpunkt "Cloud-Dienst verbinden".

   ![Evermusic Verbindungen-Bildschirm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Wählen Sie den Cloud-Dienst "SMB".

   ![Evermusic Cloud-Dienst verbinden-Bildschirm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Geben Sie auf dem "SMB-Konfigurationsbildschirm" die URL im folgenden Format ein:

   ```
   SMB://<<VAULT-IP>>
   ```

   Ersetzen Sie `<<VAULT-IP>>` durch die in Schritt 2 ermittelte **IP-Adresse**.

   **Hinweis:** Lassen Sie die Felder Benutzername und Passwort leer, da der VAULT-Speicher den GAST-Modus unterstützt.

   ![Evermusic SMB-Verbindungsbildschirm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Tippen Sie auf die Schaltfläche "Anmelden", um die Konfiguration zu speichern.

8. Öffnen Sie den verbundenen Cloud-Speicher, navigieren Sie in den Ordner mit Audiodateien und tippen Sie auf eine beliebige Datei, um den Audio-Player zu starten.

   ![Evermusic Geöffneter SMB-Server-Bildschirm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Sie können Dateien auch mit dem integrierten Dateimanager bearbeiten.

   ![Evermusic Dateimanager-Bildschirm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Mit diesen einfachen Schritten können Sie mühelos auf die interne Festplatte Ihres Bluesound VAULT zugreifen und Ihre Musikbibliothek mit Evermusic, Flacbox oder Evertag verwalten.

## FAQ

{{% details title="Benötige ich einen Benutzernamen und ein Passwort, um mich mit dem Bluesound VAULT zu verbinden?" closed="true" %}}
Nein. Der Bluesound VAULT unterstützt Gastzugang (anonym) über SMB. Lassen Sie die Felder Benutzername und Passwort bei der Konfiguration der Verbindung leer.
{{% /details %}}

{{% details title="Kann ich Musik-Tags auf dem Bluesound VAULT bearbeiten?" closed="true" %}}
Ja. Mit Evertag können Sie Metadaten-Tags (Titel, Künstler, Album usw.) von Audiodateien bearbeiten, die direkt auf der internen Festplatte des VAULT gespeichert sind.
{{% /details %}}

{{% details title="Welche Protokolle unterstützt der Bluesound VAULT?" closed="true" %}}
Der Bluesound VAULT stellt seinen internen Speicher über SMB (Server Message Block) zur Verfügung. Evermusic, Flacbox und Evertag unterstützen alle SMB-Verbindungen, was die Verbindung unkompliziert macht.
{{% /details %}}

{{% details title="Kann ich Musik vom VAULT streamen, ohne Dateien auf mein iPhone zu kopieren?" closed="true" %}}
Ja. Sobald Sie über SMB verbunden sind, können Sie Audiodateien direkt vom internen Laufwerk des VAULT streamen, ohne sie auf Ihr Gerät zu kopieren.
{{% /details %}}
