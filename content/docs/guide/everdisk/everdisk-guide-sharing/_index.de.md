---
title: "Teilen"
date: 2026-08-20
description: "Erfahre, wie das Teilen in Everdisk funktioniert: Tippe auf Start, um dein iPhone oder iPad in ein drahtloses Laufwerk zu verwandeln, wahle aus, was du teilst (Dateien, Ordner, Fotos und Musik), betreibe die funf Server (DLNA, HTTP, WebDAV, SMB, FTP), verschlussele die SMB-Verbindung mit SMB3 (AES), lies die Verbindungsadressen ab, sieh, wer verbunden ist, und halte das Teilen uber Wi-Fi oder ein USB-Kabel am Laufen."
keywords: ["Everdisk Teilen", "drahtloses Laufwerk iPhone", "Teilen starten", "Dateien teilen iPhone", "Fotos uber Netzwerk teilen", "DLNA HTTP WebDAV FTP", "was teilen", "wie verbinden", "App geoffnet lassen", "Teilen uber Wi-Fi oder USB-Kabel"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


Der Tab **Teilen** ist das Herzstuck von Everdisk. Hier verwandelst du dein iPhone oder iPad in ein drahtloses Laufwerk, wahlst genau aus, was du teilen mochtest, und erhaltst die Adressen, uber die sich andere Gerate verbinden. Das ist der erste Tab, den du siehst, wenn du die App offnest.

## Teilen starten und stoppen

In der Mitte des Teilen-Bildschirms befindet sich eine grosse runde Schaltflache.

- Tippe auf **Start**, um alle aktivierten Server auf einmal online zu bringen. Die Schaltflache zeigt zuerst **Wird gestartet...** und dann **Stopp**, sobald das Teilen aktiv ist.
- Tippe auf **Stopp**, um alles wieder offline zu nehmen. Verbundene Gerate werden getrennt.

Wahrend das Teilen lauft, sind deine ausgewahlten Dateien, Fotos und Musik fur jedes Gerat im selben Netzwerk verfugbar, das sich uber eine der funf Methoden unten verbindet.

> Das Teilen lauft nur, solange die App geoffnet ist. Weiter unten auf dieser Seite unter **Halte die App geoffnet** erfahrst du, warum das so ist und wie du grosse Ubertragungen am Laufen haltst.

## Wahle aus, was du teilst

Bevor du startest, tippe auf die Uberschrift **Was geteilt wird**, um drei Gruppen zu offnen. Du kannst sie beliebig kombinieren und musst mindestens eine Sache auswahlen, bevor das Teilen starten kann.

**Dateien und Ordner**

- Der eigene Ordner **Dokumente** deiner App wird standardmassig geteilt. Wenn du mochtest, kannst du das Teilen deaktivieren.
- Tippe auf **Ordner hinzufugen**, um einen Ordner von einer beliebigen Stelle deines Gerats zu teilen, oder auf **Datei hinzufugen**, um einzelne Dateien zu teilen.
- Jedes geteilte Element hat eine Schaltflache **Info** und eine Schaltflache **Teilen beenden**.

**Fotos und Videos**

- Aktiviere **Zugriff auf gesamte Fotomediathek erlauben**, um deine komplette Foto- und Videobibliothek zu teilen, oder
- Tippe auf **Fotos hinzufugen**, um gezielt nur die Fotos und Videos auszuwahlen, die du teilen mochtest.

**Musik**

- Aktiviere **Zugriff auf gesamte Musikmediathek erlauben**, um deine komplette Musikbibliothek zu teilen, oder
- Tippe auf **Titel hinzufugen**, um nur ausgewahlte Songs zu teilen.
- Titel, die geschutzt sind (DRM) oder nur in der Cloud liegen, konnen nicht geteilt werden.

Wenn du zu starten versuchst, ohne etwas ausgewahlt zu haben, zeigt Everdisk den Hinweis **Nichts zum Teilen** an. Wenn du anderst, was geteilt wird, wahrend das Teilen lauft, **stoppe und starte erneut**, damit die Anderung wirksam wird.

## Die funf Server

Everdisk teilt denselben Inhalt gleichzeitig auf funf Arten. Jede ist fur einen anderen Geratetyp gedacht, und jede lasst sich unter **Einstellungen > Teilen > Verbindungen** ein- oder ausschalten. Standardmassig sind alle funf aktiv.

- **TV & Media Center (DLNA)** - fur Smart-TVs und Media-Player. Sie finden dein Gerat von selbst und zeigen deine Fotos, Videos und Musik mit Vorschaubildern an.
- **Browser (HTTP)** - fur jedes Telefon, Tablet oder jeden Computer. Die andere Person offnet einen Link im Webbrowser, um deine Dateien zu durchsuchen und herunterzuladen. Nichts zu installieren.
- **Computer (WebDAV)** - fur einen Mac, Windows-PC oder Linux-Rechner. Dein Gerat erscheint als ganz normales Netzlaufwerk, sodass du Dateien in beide Richtungen ziehen kannst.
- **Computer (Erweitert) (SMB)** - ein Netzlaufwerk fur Mac, Windows und Linux. Auf einem Mac erscheint es von selbst in der Finder-Seitenleiste; unter Windows offnest du es im Datei-Explorer mit einer `smb://`-Adresse. Es ist die einzige Verbindung, die du **verschlusseln** kannst, mit SMB3-Verschlusselung (AES).
- **Andere Apps & Gerate (FTP)** - fur Datei-Apps und erfahrene Nutzer, die FTP beherrschen.

Schritt-fur-Schritt-Anleitungen zum Verbinden fur jeden Typ findest du unter [Deine Gerate verbinden](/docs/guide/everdisk/everdisk-guide-connect).

## Verbinden und Verbindungsadressen

Nachdem du auf Start getippt hast, zeigt der Abschnitt **Wie verbinden** fur jeden aktiven Server eine Karte mit der genauen **Adresse**, die du auf dem anderen Gerat eingeben musst. Jede Adresse lasst sich leicht kopieren - tippe sie an, um sie zu kopieren, nutze die Schaltflache **Teilen**, um sie zu versenden, oder tippe auf die Schaltflache **Info (ⓘ)** fur ausfuhrliche Anleitungen pro Protokoll.

- Die DLNA-Karte zeigt eine Gerateadresse, die auf `/device-desc.xml` endet, fur Player, die danach fragen.
- Wenn dein Gerat per Kabel an einen Mac angeschlossen ist, erscheint eine zusatzliche Adresse mit dem Abzeichen **Kabelverbindung**, die den `.local`-Namen deines Gerats verwendet.

Du kannst die Adresse auch als **QR-Code** offnen, damit die Kamera eines anderen Gerats direkt dorthin springt.

## Wer ist verbunden

Der Abschnitt **Wer ist verbunden** listet in Echtzeit die Gerate auf, die aktuell mit dir verbunden sind. Tippe neben einem beliebigen Gerat auf die Schaltflache fur weitere Aktionen, um **Dieses Gerat blockieren** zu wahlen, falls du es nicht kennst. Blockierte Gerate werden unter [Zugriff & Privatsphare](/docs/guide/everdisk/everdisk-guide-access) verwaltet.

## Dein Geratename und Avatar

Jedes Gerat hat einen freundlichen Namen (wie "Speedy-Hare") und einen farbigen Avatar. Das ist der Name, den ein TV, Computer oder eine andere App im Netzwerk fur dein Gerat anzeigt, damit es leicht zu erkennen ist. Du kannst den Namen und Avatar kostenlos neu generieren oder mit Premium einen eigenen Namen, ein eigenes Symbol oder einen Foto-Avatar festlegen. Siehe [Einstellungen](/docs/guide/everdisk/everdisk-guide-settings).

## Teilen uber Wi-Fi oder ein USB-Kabel

Das Teilen kann in zwei Situationen laufen:

- **Uber Wi-Fi** - dein Gerat und die anderen Gerate befinden sich im selben Wi-Fi-Netzwerk.
- **Uber ein USB-Kabel** - dein Gerat ist per Kabel an einen **Mac** angeschlossen, sogar dann, wenn uberhaupt kein Wi-Fi vorhanden ist. Das ist schneller als Wi-Fi und funktioniert weiterhin im Flugzeug, im Hotel oder in einem gesperrten Netzwerk.

Wenn weder Wi-Fi noch ein Kabel verfugbar ist, ist die Schaltflache **Start** deaktiviert und der Hinweis **Keine Wi-Fi-Verbindung** erscheint. Bricht die Verbindung wahrend des Teilens ab, stoppt Everdisk das Teilen automatisch und weist dich darauf hin. Tippe auf die Info-Schaltflache eines dieser Hinweise fur eine ausfuhrliche Erklarung.

## Halte die App geoffnet

Da dein iPhone oder iPad als Server fungiert, **funktioniert das Teilen nur, solange Everdisk auf dem Bildschirm geoffnet ist**. Wenn du die App schliesst oder das Gerat langere Zeit sperrst, kann das System die App pausieren und das Teilen stoppt.

Bei grossen Ubertragungen:

- Halte Everdisk geoffnet und im Vordergrund.
- Schliesse dein Gerat an den Strom an.
- Stelle in der iOS-Einstellungen-App **Automatische Sperre** auf **Nie**, wahrend du ubertragst.

Du kannst **Vor dem Trennen benachrichtigen** (unter Einstellungen > Teilen) aktivieren, damit Everdisk dich daran erinnert, die App erneut zu offnen, bevor das System sie aussetzt. Tippe auf die Info-Schaltflache im Banner **Halte die App geoffnet** fur weitere Details.

## Nachste Schritte

- [Deine Gerate verbinden](/docs/guide/everdisk/everdisk-guide-connect) - verbinde einen TV, Computer, Browser, ein Telefon oder ein USB-Kabel.
- [Zugriff & Privatsphare](/docs/guide/everdisk/everdisk-guide-access) - richte ein Passwort ein und steuere das Bearbeiten.
- [Einstellungen](/docs/guide/everdisk/everdisk-guide-settings) - schalte Server ein oder aus und passe die Qualitat an.
