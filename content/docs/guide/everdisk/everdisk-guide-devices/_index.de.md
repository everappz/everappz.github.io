---
title: "Mit Servern verbinden"
date: 2026-08-20
description: "Nutze den Tab Gerate in Everdisk, um dich mit anderen Servern in deinem Netzwerk zu verbinden. Fuge DLNA-, WebDAV-, FTP- und SFTP-Server sowie NAS-Laufwerke hinzu und durchsuche sie, streame Audio und Video, lade Dateien herunter und erstelle, lade hoch, benenne um, verschiebe oder losche auf Servern, die das erlauben."
keywords: ["Everdisk Gerate-Tab", "mit NAS verbinden", "DLNA Client iPhone", "WebDAV Client iPhone", "FTP Client iPhone", "SFTP Client iPhone", "Netzwerkserver durchsuchen", "von NAS streamen", "vom Server herunterladen", "Cloud WebDAV verbinden"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk ist nicht nur ein drahtloses Laufwerk - es ist auch ein Client fur die anderen Gerate in deinem Netzwerk. Der Tab **Gerate** ermoglicht es dir, dich mit **DLNA**-, **WebDAV**-, **FTP**- und **SFTP**-Servern zu verbinden, darunter NAS-Laufwerke und Media-Server, und anschliessend deren Dateien zu durchsuchen, zu streamen und herunterzuladen.

## Der Gerate-Bildschirm

Der Tab Gerate besteht aus zwei Teilen:

- **Verbindungen** - die Server, die du bereits gespeichert hast.
- **Verfugbare Gerate** - Server, die Everdisk automatisch in deinem lokalen Netzwerk findet.

Um dich mit etwas zu verbinden, das Everdisk bereits gefunden hat, tippe es einfach unter **Verfugbare Gerate** an. Um einen Server von Hand hinzuzufugen, tippe auf die Schaltflache **Plus (+)** oder auf **Neue Verbindung**.

## Eine neue Verbindung hinzufugen

Tippe auf **Neue Verbindung** und wahle den Typ des Servers, den du erreichen mochtest:

- **DLNA / UPnP** - am besten fur Media-Server. Streame Videos, Musik und Fotos von Medienbibliotheken, Netzwerkspeicher-Laufwerken und DLNA-fahigen TVs und Computern. DLNA ist schreibgeschutzt: Du kannst durchsuchen, streamen und herunterladen, aber nichts hochladen oder Dateien andern.
- **WebDAV** - verbinde dich mit Dateiservern, Netzwerkspeicher-Laufwerken und Cloud-Laufwerken, die WebDAV unterstutzen. Lesen und Schreiben, wenn der Server es erlaubt.
- **FTP** - haufig bei Routern, Netzwerkspeicher-Laufwerken und Webhosting. Der Standardport ist 21 (990 fur sicheres FTPS); du kannst in der Adresse einen eigenen Port angeben, zum Beispiel `ftp://host:2121`. Lasse Login und Passwort fur anonymen Zugriff leer.
- **SFTP** - verbinde dich sicher uber SSH. Der Standardport ist 22; verwende bei Bedarf einen eigenen Port in der Adresse, zum Beispiel `sftp://host:2222`.

> Everdisk verbindet sich nur mit diesen Protokollen im lokalen Netzwerk und direkt adressierbaren Protokollen. Es meldet sich nicht bei Cloud-Konten wie Google Drive oder Dropbox an. Ein Cloud-Laufwerk ist nur erreichbar, wenn dieser Dienst eine **WebDAV**-Adresse anbietet, die du eingeben kannst.

## Adresse eingeben und anmelden

Fulle im Verbindungseditor aus:

- **Titel** - ein freundlicher Name fur die Verbindung.
- **URL / Adresse** - die Serveradresse (fur jeden Typ werden Beispiele angezeigt).
- **Login** und **Passwort** - lasse beide leer, wenn der Server anonymen Zugriff erlaubt.

Fur WebDAV kannst du ungultige Zertifikate zulassen, falls dein Server ein selbstsigniertes verwendet. Wenn die Identitat eines sicheren Servers nicht uberpruft werden kann, bittet dich Everdisk um Bestatigung, bevor es ihm vertraut.

Kostenlose Nutzer konnen bis zu **10** Verbindungen speichern. Premium hebt das Limit auf.

## Durchsuchen, streamen und herunterladen

Sobald du verbunden bist, tippe auf den Server, um ihn zu offnen:

- **Durchsuche** die Ordner in Listen- oder Rasteransicht, sortiere sie und sieh Vorschaubilder. DLNA-Server zeigen ausserdem Musikdetails und Cover.
- **Streame** Audio und Video. Audio wandert in die Warteschlange des Mini-Players; Video wird im Vollbild abgespielt. Das Vorspulen funktioniert, wahrend eine Datei streamt.
- **Lade** Dateien auf dein Gerat herunter. Wahle mehrere auf einmal fur einen Stapel-Download. Downloads erscheinen unter **Dateiubertragungen** und landen in deinem Ordner **Dokumente**.
- **Info** zeigt bei jedem Element seinen Typ, seine Grosse, sein Datum, seinen Pfad und Mediendetails.

## Dateien auf einem Server andern

Auf Servern, die das Schreiben erlauben - **WebDAV, FTP und SFTP** - kannst du auch Dateien verwalten:

- **Neuer Ordner**
- **Dateien hochladen** von deinem Gerat
- **Umbenennen**, **Verschieben** und **Loschen** (ein Element oder mehrere auf einmal)

**DLNA**-Server sind schreibgeschutzt, daher sind diese Aktionen dort nicht verfugbar.

## Deine Ubertragungen verfolgen

Downloads und Uploads laufen im Hintergrund und erscheinen unter **Dateiubertragungen**, die du oben links im Tab **Dokumente** offnest. Dort kannst du den Fortschritt verfolgen und Aufgaben pausieren, fortsetzen, wiederholen, abbrechen oder loschen. Du kannst Ubertragungen auch unter [Einstellungen > Netzwerk](/docs/guide/everdisk/everdisk-guide-settings) anpassen (nur Wi-Fi oder Wi-Fi und Mobilfunk, wie viele gleichzeitig laufen und ob sie im Hintergrund weiterlaufen).

## Nachste Schritte

- [Dateien & Dokumente](/docs/guide/everdisk/everdisk-guide-files) - verwalte alles, was du herunterladst.
- [Fotos, Musik & Video](/docs/guide/everdisk/everdisk-guide-media) - spiele ab, was du streamst.
- [Einstellungen](/docs/guide/everdisk/everdisk-guide-settings) - Verbindungslimits und Ubertragungsoptionen.
