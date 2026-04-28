---
title: "So spielen Sie Ihre Musik von Mac / PC / Linux / NAS auf dem iPhone mit dem Kodi DLNA-Server ab"
date: 2025-07-25
description: "Streamen Sie Musik von Ihrem Computer oder NAS auf Ihr iPhone über Wi-Fi mit Kodi DLNA und der Evermusic-App."
keywords: ["kodi dlna server", "musik auf iphone streamen", "musik von nas abspielen", "evermusic dlna", "mac zu iphone musik", "windows zu iphone musik", "kodi dlna iphone", "dlna audio streaming"]
tags: ["dlna", "kodi", "evermusic", "iphone", "Musikstreaming", "mac", "nas", "linux", "lokales Netzwerk"]
readingTime: 5
---

{{< author-byline >}}


**Zusammenfassung:** Installieren Sie Kodi auf Ihrem Mac, PC, Linux oder NAS, aktivieren Sie den DLNA/UPnP-Server und streamen Sie Ihre gesamte Musikbibliothek auf iPhone oder iPad mit der kostenlosen Evermusic- oder Flacbox-App über Wi-Fi. Keine Abonnements erforderlich.

## Einführung

Wenn Sie einen **Mac, Windows-PC, Linux-Rechner oder ein NAS-Gerät** besitzen, können Sie ihn ganz einfach in einen **persönlichen Musikserver** zu Hause verwandeln, indem Sie [Kodi](https://kodi.tv/) verwenden, eine kostenlose und quelloffene Medienplattform. Mit Kodis integriertem **DLNA/UPnP-Server** können Sie Ihre gesamte Musikbibliothek auf jeden DLNA-kompatiblen Client streamen — einschließlich Ihrem iPhone oder iPad.

In dieser Anleitung zeigen wir Ihnen Schritt für Schritt, wie Sie:

- Kodi auf Ihrem Mac oder PC installieren  
- Ihre Musikordner zum Teilen einrichten  
- Den DLNA-Musikserver aktivieren  
- Auf diese Musik mit der **Evermusic**- oder **Flacbox**-App für iOS zugreifen

Diese Einrichtung ist zu 100% kostenlos — keine Abonnements, nur Ihre eigene Musik, die über Ihr Wi-Fi-Netzwerk gestreamt wird. Ob Sie versuchen, Ihre große MP3-Sammlung zu organisieren, FLAC über Wi-Fi zu hören oder einfach Ihre lokale Musik ohne Synchronisierung über iTunes zu genießen — diese Einrichtung ist perfekt für Sie.

## Kodi auf Ihrem Mac / PC / Linux / NAS herunterladen und installieren

Besuchen Sie zunächst die offizielle Kodi-Website:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi-Hauptseite" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Klicken Sie auf **Downloads** und scrollen Sie, um die Version für Ihren Computer zu finden.
Wählen Sie Ihr Betriebssystem. In diesem Beispiel verwenden wir **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Kodi-Downloadseite" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Klicken Sie auf **Intel (x86/64)**, wenn Sie einen Intel Mac haben, oder **Apple Silicon** für M1, M2, M3 Mac, um den Download zu starten.

{{< cards cols="1">}}
{{< card subtitle="macOS-Installationsprogramm wählen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Bitte warten Sie einen Moment, während das Installationsprogramm heruntergeladen wird.

{{< cards cols="1">}}
{{< card subtitle="Kodi heruntergeladen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Nach dem Download finden Sie die `.dmg`-Datei in Ihrem **Downloads**-Ordner.

{{< cards cols="1">}}
{{< card subtitle="Kodi installieren" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Doppelklicken Sie auf die heruntergeladene Datei, um das Installationsprogramm zu starten.
Ziehen Sie Kodi in Ihren **Programme**-Ordner, um die Installation durchzuführen.

{{< cards cols="1">}}
{{< card title="" subtitle="Installieren Sie Kodi durch Ziehen in Programme" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Starten Sie Kodi. Möglicherweise müssen Sie es unter **Systemeinstellungen → Sicherheit & Datenschutz → Trotzdem öffnen** erlauben.

{{< cards cols="1">}}
{{< card subtitle="Kodi-Hauptbildschirm" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Musik zur Kodi-Bibliothek hinzufügen

Klicken Sie auf das **Zahnradsymbol** (Einstellungen) auf dem Startbildschirm.

{{< cards cols="1">}}
{{< card subtitle="Kodi-Einstellungen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Navigieren Sie zu **Medieneinstellungen → Bibliothek**. Aktivieren Sie **Bibliothek beim Start aktualisieren** für Video- und Musikbibliothek zur automatischen Indizierung.

{{< cards cols="1">}}
{{< card subtitle="Bibliothekseinstellungen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Gehen Sie dann zum Bereich **Musik** und klicken Sie auf **Musik hinzufügen**.

{{< cards cols="1">}}
{{< card subtitle="Musikordner hinzufügen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Durchsuchen und wählen Sie den Ordner, in dem Ihre Musik gespeichert ist.

{{< cards cols="1">}}
{{< card subtitle="Musikquelle wählen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Fügen Sie die Musikquelle zu Kodi hinzu.

{{< cards cols="1">}}
{{< card subtitle="Musikquelle hinzufügen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Bestätigen Sie und lassen Sie Kodi Ihre Musikbibliothek scannen.

{{< cards cols="1">}}
{{< card subtitle="Musikquellen bestätigen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Warten Sie einen Moment, während Ihre Bibliothek gescannt und vollständig aufgebaut wird.

{{< cards cols="1">}}
{{< card subtitle="Musikbibliothek wird gescannt" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Kodis DLNA-Server aktivieren

Gehen Sie zu **Einstellungen → Dienste → UPnP/DLNA**.

Aktivieren Sie die Option: **Meine Bibliotheken freigeben**.

Kodi fungiert jetzt als DLNA-Server in Ihrem lokalen Wi-Fi-Netzwerk.

{{< cards cols="1">}}
{{< card subtitle="DLNA in Kodi aktivieren" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Kodi-Bibliothek öffnen

Klicken Sie mit der rechten Maustaste, um das Einstellungsfenster zu schließen und die Kodi-Hauptbibliothek zu öffnen.

{{< cards cols="1">}}
{{< card title="" subtitle="Rechtsklick für Zugriff auf die Kodi-Bibliothek" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Musikstreaming-App für iOS herunterladen

Holen Sie sich eine kostenlose iOS-DLNA-Client-App, mit der Sie Musik aus einer Vielzahl von Cloud-Speicherdiensten und DLNA-Servern streamen können.

- Verwenden Sie **Evermusic**, wenn Ihre Sammlung hauptsächlich aus MP3 und anderen Standard-Audioformaten besteht.
- Wählen Sie **Flacbox**, wenn Sie eine Hi-Res-Musikbibliothek in Formaten wie FLAC, ALAC oder DSD haben.

Beide Apps sind für **iOS** und **macOS** verfügbar und kostenlos nutzbar.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic herunterladen" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox herunterladen" icon="download" tag="Free" >}}
{{< /cards >}}

## DLNA-Quelle hinzufügen

Nachdem Sie die iOS-App heruntergeladen haben, öffnen Sie den Bereich **Alle Verbindungen**.

{{< cards cols="1">}}
{{< card title="" subtitle="Hauptseitenleiste der Evermusic-App" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Scrollen Sie nach unten und tippen Sie auf **Lokales Netzwerk - Verfügbare Geräte**, um DLNA-Server zu entdecken.
In diesem Bereich sehen Sie alle verfügbaren Geräte in Ihrem lokalen Netzwerk. Ihr **Kodi DLNA-Server** sollte hier erscheinen. Tippen Sie auf den Kodi-Server, um eine Verbindung herzustellen.

{{< cards cols="1">}}
{{< card title="" subtitle="Verfügbare DLNA-Geräte in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic zeigt die über Kodi freigegebenen Bibliotheksordner an.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi-Musikbibliothek in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navigieren Sie zum Ordner **Songs**, um alle verfügbaren Audiodateien auf Ihrem DLNA-Server anzuzeigen.

{{< cards cols="1">}}
{{< card title="" subtitle="Songs aus dem Remote-Ordner aufgelistet" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Tippen Sie auf eine beliebige Audiodatei, um sofort mit dem Streaming zu beginnen.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3-Datei wird in Evermusic abgespielt" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Kehren Sie zum Bereich **Verbindungen** zurück. Der hinzugefügte DLNA-Server erscheint nun hier. Tippen Sie auf sein Symbol, um jederzeit eine Verbindung herzustellen. Sie können auch andere Cloud-Dienste von diesem Bildschirm aus mit denselben Schritten verbinden.

Sie können hier auch **Last.fm-Scrobbling** aktivieren. Wiedergabestatistiken werden in Ihrem Last.fm-Konto gespeichert und bieten später personalisierte Musikempfehlungen.

{{< cards cols="1">}}
{{< card title="" subtitle="Verbindungen in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Musikbibliothek aufbauen

Sowohl **Evermusic** als auch **Flacbox** ermöglichen es Ihnen, Musik zu Ihrer Bibliothek hinzuzufügen und sie nach **Metadaten-Tags** wie Künstlern, Alben, Genres und Komponisten zu organisieren.

Öffnen Sie zunächst den Bereich **Musikbibliothek**. Scrollen Sie nach unten zu **Werkzeuge und Einstellungen** und tippen Sie auf **Musik hinzufügen**.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic-Musikbibliothek" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Wählen Sie die Musikquelle — in diesem Fall wählen Sie **Verbindungen**.

{{< cards cols="1">}}
{{< card title="" subtitle="Neue Musik in Evermusic hinzufügen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Finden Sie den **Kodi DLNA-Server** in den Verbindungen und tippen Sie, um Ordner und Dateien anzuzeigen.

{{< cards cols="1">}}
{{< card title="" subtitle="DLNA-Server für Musikimport wählen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Wählen Sie die Ordner oder Dateien, die Sie hinzufügen möchten, und tippen Sie auf **Fertig**.

{{< cards cols="1">}}
{{< card title="" subtitle="Musikordner zum Hinzufügen auswählen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Die App scannt Ihre ausgewählten Dateien und organisiert sie mithilfe von Metadaten in Bereiche wie Künstler, Alben, Genres und Komponisten.

{{< cards cols="1">}}
{{< card title="" subtitle="Musikbibliothek mit Kategorien" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Wiedergabelisten erstellen

Sie können auch Ihre eigenen Wiedergabelisten erstellen.

Öffnen Sie zunächst den Tab **Wiedergabelisten**.

{{< cards cols="1">}}
{{< card title="" subtitle="Tab Wiedergabelisten in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Tippen Sie auf die **Plus (+)**-Taste und wählen Sie **Neue Wiedergabeliste**.

{{< cards cols="1">}}
{{< card title="" subtitle="Neue Wiedergabeliste erstellen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Geben Sie einen Namen für Ihre Wiedergabeliste ein und tippen Sie auf **Speichern**.

{{< cards cols="1">}}
{{< card title="" subtitle="Wiedergabelistennamen eingeben" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Wählen Sie als Nächstes eine Quelle zum Hinzufügen von Songs — hier wählen wir die **Bibliothek**.

{{< cards cols="1">}}
{{< card title="" subtitle="Songs zur neuen Wiedergabeliste hinzufügen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Wählen Sie die gewünschten Songs und tippen Sie auf **Fertig**, um sie hinzuzufügen.

{{< cards cols="1">}}
{{< card title="" subtitle="Musik aus der Bibliothek zur Wiedergabeliste hinzufügen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Ihre ausgewählten Titel erscheinen nun in der erstellten Wiedergabeliste.

{{< cards cols="1">}}
{{< card title="" subtitle="Erstellte Wiedergabeliste in der Liste angezeigt" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Standardmäßig sind Songs zum Streaming verfügbar. Um offline zu hören, aktivieren Sie den **Offline-Modus** — die App lädt alle Wiedergabelisten-Titel herunter.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline-Modus für Wiedergabeliste aktiviert" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Tippen Sie auf die Schaltfläche **Weitere Aktionen**, um zusätzliche Optionen zu erkunden. Sie können:

- Die Wiedergabeliste archivieren  
- Das Albumcover ändern  
- Titel neu anordnen  
- Und weitere hilfreiche Funktionen

{{< cards cols="1">}}
{{< card title="" subtitle="Weitere Wiedergabelisten-Aktionen verfügbar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Fazit

Mit **Evermusic** und **Flacbox** ist es einfach, Ihr iPhone, iPad oder Mac in einen leistungsstarken DLNA-Musikplayer zu verwandeln. Ob Sie Ihre Musik in der Cloud, auf einem NAS oder auf einem Heimmedienserver wie **Kodi** speichern — diese Apps ermöglichen es Ihnen, Ihre Sammlung ohne Einschränkungen zu streamen, zu organisieren und zu genießen.

- Streamen Sie MP3 oder Hi-Res FLAC direkt von Ihrem **Kodi DLNA-Server**  
- Erstellen Sie eine persönliche Musikbibliothek, gruppiert nach Metadaten (Alben, Genres, Komponisten)  
- Erstellen und verwalten Sie **benutzerdefinierte Wiedergabelisten**  
- Aktivieren Sie den **Offline-Modus** zum Hören unterwegs  
- Verbinden Sie sich mit **mehreren Cloud-Diensten** und **lokalen Netzwerkgeräten**  
- Verfolgen Sie Ihre Hörgewohnheiten mit der **Last.fm-Integration**

Ob Sie ein Audiophiler oder ein Gelegenheitshörer sind — Evermusic und Flacbox bieten alles, was Sie für nahtloses Musikstreaming und Organisation brauchen.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic herunterladen" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox herunterladen" icon="download" tag="Free" >}}
{{< /cards >}}

Beginnen Sie noch heute mit dem Aufbau Ihres persönlichen Musikerlebnisses.

## FAQ

{{% details title="Ist Kodi als DLNA-Server kostenlos?" closed="true" %}}
Ja. Kodi ist vollständig kostenlos und quelloffen. Es läuft auf macOS, Windows, Linux und vielen NAS-Geräten.
{{% /details %}}

{{% details title="Unterstützen Evermusic und Flacbox FLAC-Streaming über DLNA?" closed="true" %}}
Ja. Flacbox ist für Hi-Res-Formate wie FLAC, ALAC und DSD optimiert. Evermusic unterstützt ebenfalls die FLAC-Wiedergabe neben MP3 und anderen Standardformaten.
{{% /details %}}

{{% details title="Kann ich nach dem Streaming von Kodi offline hören?" closed="true" %}}
Ja. Aktivieren Sie den Offline-Modus bei jeder Wiedergabeliste, und die App lädt alle Titel auf Ihr Gerät zum Hören ohne Netzwerkverbindung herunter.
{{% /details %}}

{{% details title="Brauche ich ein Premium-Abonnement, um DLNA zu nutzen?" closed="true" %}}
Die kostenlose Version unterstützt bis zu 3 Cloud- oder Netzwerkverbindungen. Premium entfernt dieses Limit und ermöglicht unbegrenzte Dienste und DLNA-Server.
{{% /details %}}

{{% details title="Muss mein iPhone im selben Wi-Fi-Netzwerk wie Kodi sein?" closed="true" %}}
Ja. DLNA-Streaming funktioniert über Ihr lokales Netzwerk. Sowohl der Kodi-Server als auch Ihr iOS-Gerät müssen mit demselben Wi-Fi-Netzwerk verbunden sein.
{{% /details %}}

{{% details title="Kann ich diese Einrichtung mit einem NAS statt einem Mac oder PC verwenden?" closed="true" %}}
Ja. Viele NAS-Geräte (Synology, QNAP usw.) unterstützen Kodi oder verfügen über einen eigenen integrierten DLNA-Server. Evermusic und Flacbox können sich mit jedem Standard-DLNA/UPnP-Server verbinden.
{{% /details %}}
