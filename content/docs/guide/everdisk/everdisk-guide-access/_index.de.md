---
title: "Zugriff & Privatsphare"
date: 2026-08-20
description: "Halte dein Teilen in Everdisk sicher: schutze den Zugriff mit Login und Passwort, steuere mit der Dateibearbeitung, ob verbundene Gerate hochladen, umbenennen und loschen durfen, blockiere unbekannte Gerate, wahle zwischen Papierkorb und endgultigem Loschen und verstehe, warum alles in deinem lokalen Netzwerk bleibt."
keywords: ["Everdisk Passwortschutz", "Dateibearbeitung Schalter", "Gerat blockieren", "blockierte Gerate", "Dateien endgultig loschen", "nur lokales Netzwerk", "privates Teilen von Dateien", "DLNA kein Passwort", "Netzwerksicherheit"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Everdisk behalt deine Dateien in deinem eigenen Netzwerk und gibt dir einfache Kontrollen daruber, wer sie erreichen kann und was er damit tun darf. Diese Kontrollen findest du unter **Einstellungen > Teilen > Zugriff**, dazu einige verwandte Einstellungen im Dateimanager.

## Zugriff mit Login und Passwort schutzen

Standardmassig kann jeder im selben Netzwerk, der deine Adresse hat, deine geteilten Dateien offnen. Um eine Anmeldung zu verlangen:

1. Gehe zu **Einstellungen > Teilen > Zugriff**.
2. Gib einen **Login** und ein **Passwort** ein.
3. Nun fragen die Verbindungen **Browser (HTTP)**, **Computer (WebDAV)** und **Andere Apps & Gerate (FTP)** alle nach diesen Angaben, bevor sie deine Dateien anzeigen.

Lasse beide Felder fur offenen Zugriff leer. Dein Passwort wird sicher im Schlusselbund des Gerats gespeichert.

> **DLNA ist immer offen.** Die Verbindung TV & Media Center (DLNA) lasst sich nicht mit einem Passwort schutzen, daher kann jedes Gerat im selben Wi-Fi deine geteilten Medien durchsuchen, sobald sie aktiviert ist. Schalte sie aus, wenn du nur geschutzte Verbindungen mochtest, und teile nur in Netzwerken, denen du vertraust.

## Bearbeiten erlauben oder verbieten (Dateibearbeitung)

Der Schalter **Dateibearbeitung** steuert, ob verbundene Gerate deine Dateien nur ansehen oder auch andern durfen.

- **Ein** (Standard): verbundene Gerate konnen deine geteilten Dateien **hochladen, umbenennen und loschen** - so funktioniert dein Gerat wie ein echtes Netzlaufwerk in beide Richtungen.
- **Aus**: deine geteilten Dateien sind **schreibgeschutzt**. Andere konnen ansehen und herunterladen, aber nichts hinzufugen oder andern.

Das Aktivieren zeigt eine kurze Warnung an, weil es anderen erlaubt, deine Dateien zu andern. Solange es aktiv ist, tragt es das Abzeichen **Wichtig**.

## Ein Gerat blockieren

Wenn du ein Gerat siehst, das du nicht kennst:

1. Finde es auf dem Teilen-Bildschirm unter **Wer ist verbunden**.
2. Tippe auf seine Schaltflache fur weitere Aktionen und wahle **Dieses Gerat blockieren**.

Blockierte Gerate werden unter **Einstellungen > Teilen > Zugriff > Blockierte Gerate** aufgelistet, wo du eines **entsperren** oder **Alle entsperren** kannst. Das Blockieren folgt dem Gerat, selbst wenn sich seine Netzwerkadresse andert (fur die Verbindungen Browser, Computer und TV).

## Papierkorb vs. endgultiges Loschen

Wenn eine Datei geloscht wird - von dir im Dateimanager oder von einem verbundenen Gerat - wandert sie normalerweise in einen wiederherstellbaren **Papierkorb**, sodass du sie zuruckholen kannst.

Wenn du es vorziehst, dass Dateien sofort und ohne Wiederherstellung entfernt werden, aktiviere **Dateien endgultig loschen** unter **Einstellungen > Dateimanager > Dateien loschen**. Dies ist standardmassig deaktiviert. **Es betrifft den Dateimanager auf dem Gerat** und **uber das Netzwerk vorgenommene Loschungen**; es andert nicht, wie die System-Fotomediathek oder Musikmediathek mit dem Loschen umgeht.

## Alles bleibt lokal

Everdisk teilt nur uber dein **lokales Netzwerk** - nichts wird ins Internet hochgeladen und es gibt kein Cloud-Konto dazwischen. Ein paar Dinge sind wissenswert:

- Everdisk benotigt die iOS-Berechtigung **Lokales Netzwerk**, damit nahegelegene Gerate es finden konnen. Ist diese Berechtigung deaktiviert, erklart ein Hinweis, wie du sie in der iOS-Einstellungen-App wieder aktivierst.
- Fur die grosste Privatsphare teile nur, wahrend du in einem **privaten oder Heim-Wi-Fi** bist, dem du vertraust, und sei in offentlichem Wi-Fi vorsichtig. Login und Passwort helfen, sind aber kein Ersatz fur ein vertrauenswurdiges Netzwerk.
- Die **allerprivateste Option ist ein USB-Kabel zu einem Mac** - die Daten laufen direkt uber das Kabel und erreichen niemals den Router oder das Internet. Siehe [Deine Gerate verbinden](/docs/guide/everdisk/everdisk-guide-connect).

## Nachste Schritte

- [Teilen](/docs/guide/everdisk/everdisk-guide-sharing) - wahle aus, was du teilst, und starte das Teilen.
- [Einstellungen](/docs/guide/everdisk/everdisk-guide-settings) - alle Einstellungen fur Zugriff und Dateimanager an einem Ort.
