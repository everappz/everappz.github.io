---
title: "Deine Gerate verbinden"
date: 2026-08-20
description: "Schritt-fur-Schritt-Anleitungen, um dich mit deinem drahtlosen Everdisk-Laufwerk zu verbinden: auf einem Smart-TV uber DLNA schauen, deine Dateien in jedem Webbrowser offnen, dein Gerat als Netzlaufwerk im Finder, unter Windows oder Linux uber WebDAV einbinden, Datei-Apps uber FTP verbinden und ohne Wi-Fi uber ein USB-Kabel zu einem Mac ubertragen."
keywords: ["mit Everdisk verbinden", "auf TV streamen DLNA", "Dateien im Browser offnen", "Netzlaufwerk im Finder einbinden", "WebDAV Windows Linux", "FTP Datei-App", "USB-Kabel Ubertragung Mac", "iPhone mit Computer verbinden", "Netzlaufwerk iPhone"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


Sobald du auf dem [Teilen](/docs/guide/everdisk/everdisk-guide-sharing)-Bildschirm auf **Start** tippst, konnen sich andere Gerate auf vier verschiedene Arten mit deinen Dateien verbinden. Wahle die Methode, die zu dem Gerat passt, das du verwenden mochtest. In jedem Fall wird die genaue **Adresse**, die du brauchst, im Abschnitt **Wie verbinden** des Teilen-Bildschirms angezeigt.

> Beide Gerate mussen sich im **selben Wi-Fi-Netzwerk** befinden - oder bei einem Mac uber ein **USB-Kabel** verbunden sein (siehe letzter Abschnitt).

## Auf einem TV schauen (DLNA)

Nutze dies, um Fotos, Videos und Musik auf einem Smart-TV oder Media-Player anzuzeigen.

1. Stelle unter **Einstellungen > Teilen > Verbindungen** sicher, dass **TV & Media Center** aktiviert ist (standardmassig ist es an).
2. Tippe auf dem Teilen-Bildschirm auf **Start**.
3. Offne auf deinem TV den integrierten Media-Player oder die Media-Server-App (sie heisst moglicherweise Media Player, SmartShare, AllShare oder ahnlich).
4. Dein Gerat erscheint in der Liste der Media-Server mit seinem Namen (zum Beispiel "Speedy-Hare"). Wahle es aus.
5. Durchsuche deine geteilten Fotos, Videos und Musik und starte die Wiedergabe. Vorschaubilder erscheinen automatisch.

Hinweise:

- DLNA lasst sich nicht mit einem Passwort schutzen, daher ist diese Verbindung fur jeden im selben Wi-Fi offen, solange sie aktiviert ist.
- Wenn ein Video auf einem alteren TV nicht abgespielt wird, senke die Videoqualitat unter **Einstellungen > Teilen > Videos**, sodass Everdisk es in ein kompatibleres Format umwandelt.

## In einem Webbrowser offnen (HTTP)

Nutze dies, um jedem mit einem Webbrowser Dateien zu ubergeben - ohne dass eine App installiert werden muss.

1. Stelle unter **Einstellungen > Teilen > Verbindungen** sicher, dass **Browser** aktiviert ist.
2. Tippe auf **Start**.
3. Kopiere auf dem Teilen-Bildschirm die **Browser**-Adresse (oder zeige ihren QR-Code an).
4. Offne auf dem anderen Telefon, Tablet oder Computer einen beliebigen Webbrowser (Safari, Chrome, Edge, Firefox) und gib diese Adresse ein.
5. Die Seite offnet sich mit deinen geteilten Dateien.

Im Browser kann die andere Person:

- Zwischen **Listen**- und **Rasteransicht** wechseln und nach Name, Datum oder Grosse sortieren.
- Echte **Vorschaubilder** fur Fotos, Videos, PDFs und Musik-Cover sehen.
- Ein Foto in einer **Vollbild-Galerie** offnen, mit Wischen, Zoomen per Fingergeste und einer Diashow.
- Musik in einem integrierten **Player** mit Warteschlange, Zufallswiedergabe und Wiederholung abspielen.
- Jede Datei **herunterladen** oder einen ganzen Ordner (bzw. mehrere ausgewahlte Elemente) als einzelnes **Archive.zip** herunterladen.
- Dateien zuruck auf dein Gerat **hochladen** - aber nur, wenn du **Dateibearbeitung** aktiviert hast (siehe [Zugriff & Privatsphare](/docs/guide/everdisk/everdisk-guide-access)).

## Als Netzlaufwerk nutzen (WebDAV)

Nutze dies, damit dein Gerat als ganz normales Laufwerk auf einem Mac, Windows-PC oder Linux-Rechner erscheint, sodass du Dateien in beide Richtungen ziehen kannst.

**Auf einem Mac (Finder)**

1. Stelle unter **Einstellungen > Teilen > Verbindungen** sicher, dass **Computer** aktiviert ist.
2. Tippe auf **Start** und notiere die Adresse **Computer (WebDAV)**.
3. Wahle im Finder **Gehe zu > Mit Server verbinden** (oder drucke **⌘K**).
4. Gib die WebDAV-Adresse genau wie angezeigt ein und klicke auf **Verbinden**.
5. Gib Login und Passwort ein, falls du eines festgelegt hast, andernfalls verbinde dich als Gast.
6. Dein Gerat offnet sich wie jedes andere Netzlaufwerk. Ziehe Dateien hinein oder heraus.

**Unter Windows**

1. Offne den **Datei-Explorer**, klicke mit der rechten Maustaste auf **Dieser PC** und wahle **Netzwerkadresse hinzufugen** (oder verbinde ein Netzlaufwerk).
2. Gib die in Everdisk angezeigte WebDAV-Adresse ein.
3. Gib Login und Passwort ein, falls du eines festgelegt hast.

**Unter Linux**

1. Offne deinen Dateimanager und wahle **Mit Server verbinden** (oder verwende `davs://` / `dav://`).
2. Gib die in Everdisk angezeigte WebDAV-Adresse ein.

Ob die Verbindung schreibgeschutzt oder in beide Richtungen moglich ist, hangt von der Einstellung **Dateibearbeitung** ab. Ist sie aktiviert, kannst du Dateien auf dein Gerat kopieren sowie umbenennen oder loschen; ist sie deaktiviert, ist das Laufwerk schreibgeschutzt.

## Eine Datei-App verbinden (FTP)

Nutze dies fur Dateimanager- und Ubertragungs-Apps, die FTP beherrschen (zum Beispiel FileZilla oder Cyberduck auf einem Computer).

1. Stelle unter **Einstellungen > Teilen > Verbindungen** sicher, dass **Andere Apps & Gerate** aktiviert ist.
2. Tippe auf **Start** und notiere die **FTP**-Adresse.
3. Fuge in deiner FTP-App eine neue Verbindung mit dieser Adresse hinzu.
4. Gib Login und Passwort ein, falls du eines festgelegt hast, oder lasse sie fur anonymen Zugriff leer.

## Uber ein USB-Kabel ubertragen (Mac, kein Wi-Fi notig)

Nutze dies, wenn kein Wi-Fi vorhanden ist oder wenn du die schnellste und privateste Ubertragung mochtest. Es funktioniert nur mit einem **Mac**.

1. Schliesse dein iPhone oder iPad mit dem normalen Ladekabel an den Mac an.
2. Tippe auf dem Gerat auf **Diesem Computer vertrauen**, falls du danach gefragt wirst.
3. Tippe in Everdisk auf **Start**. Der Hinweis **Schnelle Verbindung verfugbar** erscheint und der Teilen-Bildschirm zeigt eine zusatzliche Adresse mit dem Abzeichen **Kabelverbindung**, die auf `.local` endet.
4. Offne auf dem Mac Finder > **Gehe zu > Mit Server verbinden** (**⌘K**) und gib diese `.local`-Adresse ein (sie funktioniert sowohl fur die Browser- als auch fur die Computer-Verbindung).
5. Dein Gerat offnet sich uber das Kabel - schneller als Wi-Fi, und die Daten erreichen niemals den Router oder das Internet.

Hinweise:

- Verwende den **`.local`-Namen**, nicht eine IP-Adresse (IP-Adressen funktionieren nur uber Wi-Fi) und niemals `localhost`.
- Der Weg uber Kabel gilt **nur fur den Mac**. Windows-PCs und Android-Gerate mussen Wi-Fi verwenden.
- Du kannst Dateien auch mit dem Finder auf einem Mac oder mit der App Apple-Gerate (bzw. iTunes) unter Windows in den Everdisk-Ordner ziehen, uber die standardmassige iOS-Dateifreigabe.

## Nachste Schritte

- [Zugriff & Privatsphare](/docs/guide/everdisk/everdisk-guide-access) - richte ein Passwort ein, erlaube Uploads, blockiere ein Gerat.
- [Fotos, Musik & Video](/docs/guide/everdisk/everdisk-guide-media) - teile deine gesamte Bibliothek und lege die Qualitat fest.
- [Mit Servern verbinden](/docs/guide/everdisk/everdisk-guide-devices) - erreiche andere Gerate von Everdisk aus.
