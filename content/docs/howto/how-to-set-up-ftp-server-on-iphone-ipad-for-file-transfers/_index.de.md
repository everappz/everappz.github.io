---
title: "FTP-Server auf iPhone & iPad fur Dateiubertragungen einrichten"
description: "Verwandle dein iPhone oder iPad mit Everdisk in einen FTP-Server und ubertrage Dateien uber Wi-Fi von einem Mac, Windows-PC, Linux, Android, einer FTP-App wie FileZilla oder einem weiteren iPhone. Komplette Einrichtung, die ftp-Adresse und der Port, Gastzugriff und die Verbindung Schritt fur Schritt fur jedes Gerat."
date: 2026-09-19
tags: ["everdisk", "ftp", "dateiubertragung", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP Server iPhone", "FTP Server iPad", "FTP auf iPhone einrichten", "iphone ftp server app", "FileZilla mit iPhone verbinden", "Cyberduck iPhone FTP", "Dateien vom iPhone per FTP ubertragen", "ftp iphone zu computer", "ftp iphone zu iphone", "von Windows mit iPhone-FTP verbinden", "ftp Adresse Port iphone", "anonymes ftp iphone", "Dateien vom iphone per ftp teilen", "iphone ftp fur Kamera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP ist der alte Zuverlassige der Dateiubertragung. Es gibt es seit Jahrzehnten, und genau deshalb ist es so nutzlich: fast alles, was mit einem Server sprechen kann, versteht es. Kameras, Smart-TVs, Router, Netzlaufwerke, Automatisierungswerkzeuge und jede Desktop-FTP-App sprechen FTP. Mit [Everdisk](/products/everdisk) kannst du einen FTP-Server auf deinem iPhone oder iPad betreiben, sodass das Handy zu einem Ort wird, mit dem sich diese Gerate und Apps verbinden und zu dem sie Dateien verschieben konnen.

Greife zu FTP, wenn die anderen Optionen nicht passen, zum Beispiel bei einem alteren Gerat oder einer App, die sich nur uber FTP verbinden kann. Diese Anleitung behandelt die Einrichtung und wie du dich von einem Mac, Windows, einer FTP-App, Linux, Android und einem zweiten iPhone verbindest.

## Was du brauchst

- Ein iPhone oder iPad mit installiertem [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Einen Computer, eine App oder ein Gerat im **selben Wi-Fi-Netzwerk**.
- Die Dateien, die du teilen willst, im Everdisk-Ordner Dokumente oder in Ordnern, die du hinzufugst.

## Den FTP-Server in Everdisk einrichten

### Schritt 1: Wahle aus, was geteilt wird und lege den Zugriff fest

Offne Everdisk, gehe zum Tab **Teilen** und tippe auf **Was geteilt wird**. Der Ordner Dokumente wird standardmassig geteilt. Fuge mehr mit **Ordner hinzufügen** und **Datei hinzufügen** hinzu.

Offne **Einstellungen**, dann **Teilen**, dann **Zugriff**. Aktiviere **Dateibearbeitung**, wenn du willst, dass Leute hochladen, umbenennen und loschen konnen, oder deaktiviere sie, um nur Downloads zu erlauben. Lege einen **Anmeldename** und ein **Passwort** fest, wenn du eine Anmeldung willst, oder lass sie leer, damit sich jeder als Gast verbinden kann.

### Schritt 2: Den FTP-Server einschalten

Gehe zu **Einstellungen**, dann **Teilen**, dann **Verbindungen** und aktiviere **Andere Apps und Geräte**. Das ist der FTP-Server (er tragt die Kennzeichnung FTP).

### Schritt 3: Teilen starten und die Adresse notieren

Kehre zum Tab **Teilen** zuruck und tippe auf **Start**. Der Abschnitt **So verbindest du dich** zeigt die FTP-Adresse. Sie sieht so aus:

```
ftp://192.168.1.20:2121
```

Die Zahl nach dem Doppelpunkt ist der **Port**, der standardmassig **2121** ist. Der erste Teil ist die Adresse deines iPhones im Wi-Fi, deiner wird also anders sein. Halte Everdisk auf dem Bildschirm offen, wahrend ein Gerat verbunden ist.

## Von einem Mac verbinden

1. Offne den **Finder**, wahle **Gehe zu**, dann **Mit Server verbinden** (oder drucke **Command und K**).
2. Gib die in Everdisk angezeigte FTP-Adresse ein, zum Beispiel `ftp://192.168.1.20:2121`.
3. Klicke auf **Verbinden**, dann wahle **Gast** oder gib deinen **Anmeldename** und dein **Passwort** ein.

Der Finder bindet die FTP-Freigabe ein, sodass du Dateien durchsuchen und auf deinen Mac kopieren kannst. Beachte, dass der Finder FTP schreibgeschutzt offnet. Wenn du von einem Mac hochladen willst, nutze eine FTP-App wie unten beschrieben.

## Von Windows verbinden

1. Offne den **Datei-Explorer** und klicke oben auf die Adressleiste.
2. Gib die FTP-Adresse aus Everdisk ein, zum Beispiel `ftp://192.168.1.20:2121`, und drucke **Enter**.
3. Gib deinen **Anmeldename** und dein **Passwort** ein, falls du eines festgelegt hast, oder fahre als Gast fort.

Die geteilten Dateien erscheinen im Fenster und du kannst sie auf deinen PC kopieren.

## Mit einer FTP-App verbinden (FileZilla, Cyberduck)

Fur Uploads und volle Kontrolle ist eine FTP-App das beste Werkzeug. **FileZilla** und **Cyberduck** sind kostenlos und laufen unter Windows, Mac und Linux.

1. Offne die App und erstelle eine neue Verbindung.
2. Setze den **Host** auf die Wi-Fi-Adresse deines iPhones und den **Port** auf **2121**.
3. Gib fur das Login deinen **Anmeldename** und dein **Passwort** ein oder wahle **Anonymous**, falls du keines festgelegt hast.
4. Verbinde dich und ziehe Dateien in beide Richtungen (Uploads brauchen aktivierte Dateibearbeitung).

## Von Linux verbinden

1. Offne deinen Dateimanager und wahle **Mit Server verbinden** oder **Andere Orte**.
2. Gib die Adresse ein, zum Beispiel `ftp://192.168.1.20:2121`.
3. Verbinde dich als Gast oder mit deinem Login.

Du kannst auch jeden Linux-FTP-Client vom Terminal nutzen und ihn auf denselben Host und Port 2121 richten.

## Von Android verbinden

Android hat keinen System-FTP-Browser, nutze also eine App:

1. Installiere einen FTP-Client wie **AndFTP**, **FTPCafe** oder einen Dateimanager mit FTP-Unterstutzung wie **Solid Explorer**.
2. Fuge eine Verbindung mit dem Host, **Port 2121** und deinem Login oder Anonymous hinzu.
3. Durchsuche und ubertrage.

## Von einem weiteren iPhone oder iPad verbinden

Die iOS-App Dateien enthalt keinen FTP-Client, nutze also eine der folgenden Moglichkeiten auf dem zweiten Gerat:

- **Everdisks eigener Tab Geräte.** Offne Everdisk, gehe zu **Geräte**, tippe auf **Neue Verbindung**, wahle **FTP** und gib die Adresse ein, zum Beispiel `ftp://192.168.1.20:2121`. Das ist der einfachste Weg.
- **Eine dedizierte FTP-App** fur iOS, mit demselben Host, Port 2121 und Login.

## Andere Gerate verbinden: Kameras, TVs, Router und NAS

Hier glanzt FTP. Viele Gerate haben einen eingebauten FTP-Client, der Dateien senden oder abrufen kann:

- **Kameras**, die Fotos uber FTP hochladen, konnen sie direkt an dein iPhone senden.
- **Smart-TVs, Router, NAS-Boxen und Automatisierungswerkzeuge**, die FTP unterstutzen, konnen sich auf dieselbe Weise verbinden.

Richte sie auf die Wi-Fi-Adresse deines iPhones, Port **2121** und dein Login (oder Anonymous), mit der in Everdisk angezeigten Adresse.

## Nur lesen oder lesen und schreiben

Der Schalter **Dateibearbeitung** in Einstellungen, Teilen, Zugriff steuert das. Aktiviert lasst Leute hochladen, umbenennen und loschen. Deaktiviert bedeutet, dass sie nur herunterladen konnen. Wahle Nur lesen, wenn du Dateien austeilst und nicht willst, dass etwas auf deinem Handy geandert wird.

## So nutzen Menschen das im Alltag

- **FileZilla mit deinem iPhone verbinden** und eine Reihe von Dateien in einem Rutsch auf das Handy schieben.
- **Eine alte App oder ein Gerat, das nur FTP spricht**, deine Dateien erreichen lassen, wenn nichts anderes sich verbinden will.
- **Fotos von einer Kamera empfangen**, die uber FTP hochladt.
- **Dateien zwischen einem iPhone und einem iPad verschieben** uber Everdisks Tab Geräte auf dem empfangenden Gerat.

## Ein paar Tipps

- Halte Everdisk offen, wahrend ein Gerat verbunden ist, da iOS Hintergrund-Apps nach einer Weile pausiert.
- Um von einem Mac hochzuladen, nutze FileZilla oder Cyberduck statt des Finders, denn der Finder offnet FTP schreibgeschutzt.
- Lass das Login fur die breiteste Kompatibilitat leer und verbinde dich dann als Anonymous, was die meisten FTP-Clients anbieten.
- FTP verschlusselt seinen Datenverkehr nicht. In einem Netzwerk, dem du nicht vertraust, nutze stattdessen den [SMB-Server mit Verschlusselung](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Haufig gestellte Fragen

{{% details title="Was sind die FTP-Adresse und der Port fur mein iPhone?" closed="true" %}}
Nachdem du das Teilen gestartet hast, zeigt Everdisk die Adresse auf dem Teilen-Bildschirm. Sie sieht aus wie ftp://192.168.1.20:2121. Die 2121 ist der Port, den Everdisk fur FTP nutzt, und der erste Teil ist die Adresse deines iPhones im Wi-Fi, deiner wird also anders sein.
{{% /details %}}

{{% details title="Wie verbinde ich FileZilla oder Cyberduck mit meinem iPhone?" closed="true" %}}
Offne die App und erstelle eine neue Verbindung. Setze den Host auf die Wi-Fi-Adresse deines iPhones und den Port auf 2121. Gib deinen Anmeldename und dein Passwort ein oder wahle Anonymous, falls du in Everdisk keines festgelegt hast. Verbinde dich, und du kannst Dateien in beide Richtungen ziehen, wenn Dateibearbeitung aktiviert ist.
{{% /details %}}

{{% details title="Kann ich mich von Windows mit meinem iPhone-FTP verbinden?" closed="true" %}}
Ja. Offne den Datei-Explorer, klicke auf die Adressleiste, gib die FTP-Adresse aus Everdisk ein (zum Beispiel ftp://192.168.1.20:2121) und drucke Enter. Gib dein Login ein, falls du eines festgelegt hast, oder fahre als Gast fort. Fur Uploads und mehr Kontrolle nutze stattdessen eine FTP-App wie FileZilla.
{{% /details %}}

{{% details title="Brauche ich ein Login fur FTP?" closed="true" %}}
Nein, ein Login ist optional. Lass Anmeldename und Passwort in Einstellungen, Teilen, Zugriff leer und verbinde dich als Anonymous, was die meisten FTP-Clients anbieten. Lege ein Login fest, wenn du willst, dass sich Verbindungen zuerst anmelden.
{{% /details %}}

{{% details title="Warum kann ich uber FTP nur herunterladen und nicht hochladen?" closed="true" %}}
Zwei Grunde sind haufig. Erstens muss der Schalter Dateibearbeitung in Einstellungen, Teilen, Zugriff aktiviert sein, um Uploads, Umbenennungen und Loschungen zu erlauben. Zweitens offnet der Mac-Finder FTP schreibgeschutzt, nutze also eine FTP-App wie FileZilla oder Cyberduck, wenn du hochladen willst.
{{% /details %}}

{{% details title="Kann ich FTP zwischen zwei iPhones nutzen?" closed="true" %}}
Ja. Starte den FTP-Server auf dem ersten iPhone. Offne auf dem zweiten Everdisk, gehe zum Tab Geräte, tippe auf Neue Verbindung, wahle FTP und gib die auf dem ersten Handy angezeigte Adresse ein. Eine dedizierte FTP-App fur iOS funktioniert ebenfalls, da die iOS-App Dateien keinen FTP-Client enthalt.
{{% /details %}}

{{% details title="Ist FTP sicher?" closed="true" %}}
Einfaches FTP verschlusselt seinen Datenverkehr nicht, behandle es also als Werkzeug fur Netzwerke, denen du vertraust, wie dein Heim-Wi-Fi. In einem Netzwerk, das du nicht kontrollierst, nutze den SMB-Server mit aktivierter Option SMB-Verschlüsselung anfordern, die jede Ubertragung schutzt.
{{% /details %}}

{{% details title="Welche Gerate konnen sich uber FTP verbinden?" closed="true" %}}
Fast alles mit einem FTP-Client. Das umfasst Mac-, Windows- und Linux-Computer, FTP-Apps wie FileZilla und Cyberduck, Android-Dateimanager und Hardware wie Kameras, Smart-TVs, Router, NAS-Boxen und Automatisierungswerkzeuge. Diese breite Reichweite ist der Hauptgrund, FTP zu wahlen.
{{% /details %}}

{{% details title="Warum ist meine FTP-Verbindung abgebrochen?" closed="true" %}}
Dein iPhone ist der Server, und iOS pausiert Apps, die zu lange im Hintergrund bleiben. Halte Everdisk auf dem Bildschirm offen, wahrend ein Gerat verbunden ist, und schliesse bei langen Ubertragungen den Strom an. Stelle ausserdem sicher, dass beide Gerate noch im selben Wi-Fi sind.
{{% /details %}}

{{% details title="Ist Everdisk kostenlos?" closed="true" %}}
Ja, Everdisk ist ein kostenloser Download und der FTP-Server ist enthalten. Ein optionaler einmaliger Premium-Kauf fugt Extras hinzu, etwa individuelle Ports und Foto- und Videokonvertierung. Du kannst FTP einrichten und Dateien ubertragen, ohne zu zahlen.
{{% /details %}}

Bereit, es auszuprobieren? [Lade Everdisk aus dem App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) und verbinde deinen ersten FTP-Client in wenigen Minuten. Fragen oder Feedback? Schreib uns an **support@everappz.com**.
</content>
