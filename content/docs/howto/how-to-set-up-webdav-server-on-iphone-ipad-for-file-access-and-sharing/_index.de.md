---
title: "WebDAV-Server auf iPhone & iPad fur Dateizugriff & Teilen einrichten"
description: "Verwandle dein iPhone oder iPad mit Everdisk in einen WebDAV-Server und binde es uber Wi-Fi als Netzlaufwerk im Mac-Finder, im Windows-Datei-Explorer, unter Linux, Android oder auf einem weiteren iPhone ein. Komplette Einrichtung, die WebDAV-Adresse und der Port und die Verbindung Schritt fur Schritt fur jedes Gerat."
date: 2026-09-19
tags: ["everdisk", "webdav", "netzlaufwerk", "dateien teilen", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV Server iPhone", "WebDAV Server iPad", "WebDAV auf iPhone einrichten", "iPhone als Netzlaufwerk einbinden", "iPhone WebDAV mit Mac Finder verbinden", "WebDAV Windows Datei-Explorer iPhone", "iphone Netzlaufwerk Windows", "WebDAV Linux iPhone", "auf iPhone-Dateien vom Computer zugreifen", "webdav iphone zu iphone", "Dateien vom iPhone per WebDAV teilen", "Netzlaufwerk iphone einbinden", "Dateien per webdav vom iphone ubertragen", "webdav Adresse Port iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV verwandelt einen Ordner in ein Netzlaufwerk, das ein Computer in seinem normalen Dateimanager offnen kann. Es lauft uber dasselbe Web-Protokoll, das dein Browser nutzt, weshalb es ohne spezielle Treiber gut zwischen Mac, Windows und Linux funktioniert. Mit [Everdisk](/products/everdisk) kannst du einen WebDAV-Server auf deinem iPhone oder iPad betreiben, sodass das Handy als Laufwerk erscheint, das du von fast jedem Computer durchsuchen, von dem du kopieren und auf das du kopieren kannst.

WebDAV ist die beste Wahl, wenn Windows im Spiel ist, denn der Windows-Datei-Explorer verbindet sich sauber damit. Diese Anleitung behandelt die Einrichtung und wie du dich von einem Mac, Windows, Linux, Android und einem zweiten iPhone verbindest.

## Was du brauchst

- Ein iPhone oder iPad mit installiertem [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Einen Computer oder ein weiteres Gerat im **selben Wi-Fi-Netzwerk**.
- Die Dateien, die du teilen willst, im Everdisk-Ordner Dokumente oder in Ordnern, die du hinzufugst.

## Den WebDAV-Server in Everdisk einrichten

### Schritt 1: Wahle aus, was geteilt wird und lege den Zugriff fest

Offne Everdisk, gehe zum Tab **Teilen** und tippe auf **Was geteilt wird**. Der Ordner Dokumente wird standardmassig geteilt. Fuge mehr mit **Ordner hinzufügen** und **Datei hinzufügen** hinzu.

Offne **Einstellungen**, dann **Teilen**, dann **Zugriff**. Aktiviere **Dateibearbeitung**, wenn du willst, dass verbundene Computer Dateien auf dein Handy kopieren und umbenennen oder loschen konnen, oder deaktiviere sie fur ein schreibgeschutztes Laufwerk. Lege hier einen **Anmeldename** und ein **Passwort** fest, wenn du eine Anmeldung willst, oder lass sie fur Gastzugriff leer.

### Schritt 2: Den WebDAV-Server einschalten

Gehe zu **Einstellungen**, dann **Teilen**, dann **Verbindungen** und aktiviere **Computer**. Das ist der WebDAV-Server (er tragt die Kennzeichnung WebDAV).

### Schritt 3: Teilen starten und die Adresse notieren

Kehre zum Tab **Teilen** zuruck und tippe auf **Start**. Der Abschnitt **So verbindest du dich** zeigt die WebDAV-Adresse. Sie sieht so aus:

```
http://192.168.1.20:8080
```

Die Zahl nach dem Doppelpunkt ist der **Port**, der standardmassig **8080** ist. Der erste Teil ist die Adresse deines iPhones im Wi-Fi, deiner wird also abweichen. Halte Everdisk auf dem Bildschirm offen, wahrend ein Gerat verbunden ist.

## Von einem Mac verbinden

1. Offne den **Finder**, wahle **Gehe zu**, dann **Mit Server verbinden** (oder drucke **Command und K**).
2. Gib die in Everdisk angezeigte WebDAV-Adresse ein, zum Beispiel `http://192.168.1.20:8080`.
3. Klicke auf **Verbinden**, dann wahle **Gast** oder gib deinen **Anmeldename** und dein **Passwort** ein.

Dein iPhone offnet sich in einem Finder-Fenster und verhalt sich wie ein normaler Ordner. Kopiere Dateien in beide Richtungen, wenn Dateibearbeitung aktiviert ist.

## Von Windows verbinden

Windows hat einen eingebauten WebDAV-Client, das funktioniert also aus dem Datei-Explorer.

1. Offne den **Datei-Explorer**, klicke mit der rechten Maustaste auf **Dieser PC** in der Seitenleiste und wahle **Netzwerkadresse hinzufügen** (du kannst auch **Netzlaufwerk verbinden** nutzen).
2. Wenn nach der Adresse gefragt wird, gib dieselbe WebDAV-Adresse aus Everdisk ein, zum Beispiel `http://192.168.1.20:8080`, dann klicke auf **Weiter**.
3. Gib deinen **Anmeldename** und dein **Passwort** ein, falls du eines festgelegt hast.

Das Gerat erscheint dann unter Dieser PC als Netzwerkadresse, die du offnen und von der du Dateien kopieren kannst. Wenn Windows sich beim ersten Mal weigert zu verbinden, stelle sicher, dass der Dienst **WebClient** lauft (suche im Startmenu nach Dienste, finde WebClient und setze ihn auf Starten), dann versuche es erneut.

## Von Linux verbinden

1. Offne deinen Dateimanager und wahle **Mit Server verbinden** oder **Andere Orte**.
2. Gib die Adresse mit einem WebDAV-Prafix ein, zum Beispiel `dav://192.168.1.20:8080` (nutze `davs://` nur, wenn du TLS eingerichtet hast).
3. Verbinde dich als Gast oder gib dein Login ein.

## Von Android verbinden

Android hat keinen System-WebDAV-Browser, nutze also einen Dateimanager, der ihn unterstutzt:

1. Installiere eine App wie **Solid Explorer** oder **CX File Explorer**.
2. Fuge eine neue **WebDAV**-Verbindung hinzu.
3. Gib den Host und **Port 8080** ein, wahle das `http`-Schema und fuge dein Login hinzu, falls du eines festgelegt hast.

## Von einem weiteren iPhone oder iPad verbinden

Die iOS-App Dateien enthalt keinen WebDAV-Client, nutze also eine der folgenden Moglichkeiten:

- **Everdisks eigener Tab Geräte.** Offne auf dem zweiten Gerat Everdisk, gehe zu **Geräte**, tippe auf **Neue Verbindung**, wahle **WebDAV** und gib die Adresse ein, zum Beispiel `http://192.168.1.20:8080`. Das ist der einfachste Weg und braucht nichts Zusatzliches.
- **Eine WebDAV-App** wie Documents by Readdle, die eine WebDAV-Verbindung mit derselben Adresse und demselben Login hinzufugen kann.

## Lieber ein schneller Link statt eines Laufwerks?

Wenn du nur schnell eine Datei greifen willst und uberhaupt kein Laufwerk einbinden mochtest, aktiviere die Verbindung **Browser** in Einstellungen, Teilen, Verbindungen. Everdisk gibt dir dann eine Webadresse, die du in jedem Browser auf jedem Gerat offnen kannst, um deine Dateien zu durchsuchen und herunterzuladen. Es ist der schnellste Weg, einem Windows-PC, einem Chromebook oder dem Handy eines Freundes eine Datei zu ubergeben.

## Nur lesen oder lesen und schreiben

Der Schalter **Dateibearbeitung** in Einstellungen, Teilen, Zugriff entscheidet das. Aktiviert bedeutet, dass verbundene Computer hochladen, umbenennen und loschen konnen. Deaktiviert bedeutet, dass das Laufwerk schreibgeschutzt ist, sodass andere deine Dateien ansehen und kopieren, aber nicht andern konnen.

## So nutzen Menschen das im Alltag

- **Dateien von einem Windows-PC auf dein iPhone kopieren**, indem du es als Netzwerkadresse einbindest und sie hinuberziehst.
- **Fotos und Dokumente auf einen Laptop auslagern** mit dem Dateimanager, den du bereits kennst, ohne Kabel und ohne iTunes.
- **Ein Dokument direkt bearbeiten** von deinem Mac aus, indem du es direkt vom Handy offnest und zuruckspeicherst.
- **Einen Ordner zwischen einem iPhone und einem iPad verschieben** uber Everdisks Tab Geräte auf dem empfangenden Gerat.

## Ein paar Tipps

- Halte Everdisk offen, wahrend ein Gerat verbunden ist. Das Handy lange zu sperren kann die App pausieren.
- Wenn unter Windows die Verbindung fehlschlagt, starte den Dienst WebClient und versuche die Adresse erneut.
- WebDAV und SMB binden beide als Netzlaufwerk ein. Nutze WebDAV, wenn Windows im Spiel ist, und [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), wenn du Finder-Geschwindigkeit und Verschlusselung willst.
- Fur schnellste Ubertragungen halte die Foto- und Videoqualitat in den Einstellungen auf Original.

## Haufig gestellte Fragen

{{% details title="Was sind die WebDAV-Adresse und der Port fur mein iPhone?" closed="true" %}}
Nachdem du das Teilen gestartet hast, zeigt Everdisk die Adresse auf dem Teilen-Bildschirm. Sie sieht aus wie http://192.168.1.20:8080. Die 8080 ist der Port, den Everdisk fur WebDAV nutzt, und der erste Teil ist die Adresse deines iPhones im Wi-Fi, deiner wird also anders sein.
{{% /details %}}

{{% details title="Wie verbinde ich mich von Windows mit meinem iPhone-WebDAV?" closed="true" %}}
Offne den Datei-Explorer, klicke mit der rechten Maustaste auf Dieser PC und wahle Netzwerkadresse hinzufügen oder Netzlaufwerk verbinden. Gib die WebDAV-Adresse aus Everdisk ein, zum Beispiel http://192.168.1.20:8080, dann gib dein Login ein, falls du eines festgelegt hast. Wenn Windows sich nicht verbindet, stelle sicher, dass der Dienst WebClient lauft (suche nach Dienste, finde WebClient, starte ihn) und versuche es erneut.
{{% /details %}}

{{% details title="Kann ich WebDAV zwischen zwei iPhones nutzen?" closed="true" %}}
Ja, aber die iOS-App Dateien hat keinen WebDAV-Client, nutze also Everdisk auf dem zweiten Gerat. Offne den Tab Geräte, tippe auf Neue Verbindung, wahle WebDAV und gib die auf dem ersten Handy angezeigte Adresse ein. Eine WebDAV-App wie Documents by Readdle funktioniert ebenfalls.
{{% /details %}}

{{% details title="Braucht WebDAV ein Passwort?" closed="true" %}}
Nein, ein Login ist optional. Lass Anmeldename und Passwort in Einstellungen, Teilen, Zugriff fur Gastzugriff leer oder lege sie fest, wenn du willst, dass sich Verbindungen anmelden.
{{% /details %}}

{{% details title="Konnen andere Leute meine Dateien uber WebDAV andern?" closed="true" %}}
Nur wenn du es erlaubst. Der Schalter Dateibearbeitung in Einstellungen, Teilen, Zugriff steuert das. Aktiviert lasst verbundene Gerate hochladen, umbenennen und loschen. Deaktiviert macht das Laufwerk schreibgeschutzt, sodass andere ansehen und kopieren, aber nichts andern konnen.
{{% /details %}}

{{% details title="WebDAV oder SMB, was ist der Unterschied?" closed="true" %}}
Beide binden dein iPhone als Netzlaufwerk ein. WebDAV lauft uber das Web-Protokoll und verbindet sich sauber aus dem Windows-Datei-Explorer, was seine Hauptstarke ist. SMB ist die native Dateifreigabe auf Mac, Linux und NAS-Geraten, ist auf einem Mac meist schneller und ist die einzige Everdisk-Verbindung, die Ubertragungen verschlusseln kann. Everdisk kann beide gleichzeitig betreiben.
{{% /details %}}

{{% details title="Warum trennt sich mein WebDAV-Laufwerk?" closed="true" %}}
Dein iPhone ist der Server, und iOS pausiert Apps, die zu lange im Hintergrund bleiben. Halte Everdisk auf dem Bildschirm offen, wahrend ein Gerat verbunden ist, und schliesse bei langen Ubertragungen den Strom an. Bestatige ausserdem, dass beide Gerate noch im selben Wi-Fi sind.
{{% /details %}}

{{% details title="Kann ich mich uber WebDAV ohne Wi-Fi verbinden?" closed="true" %}}
Ja, wenn du dein iPhone mit einem Kabel an einen Mac anschliesst. Everdisk zeigt dann eine zusatzliche Kabelverbindungsadresse, die der verbundene Mac im Finder offnen kann, was sogar ganz ohne Wi-Fi funktioniert. Uber das Kabel kann nur dieser Mac das Gerat erreichen.
{{% /details %}}

{{% details title="Ist Everdisk kostenlos?" closed="true" %}}
Ja, Everdisk ist ein kostenloser Download und der WebDAV-Server ist enthalten. Ein optionaler einmaliger Premium-Kauf fugt Extras hinzu, etwa individuelle Ports und Foto- und Videokonvertierung. Du kannst WebDAV einrichten und Dateien teilen, ohne zu zahlen.
{{% /details %}}

Bereit, es auszuprobieren? [Lade Everdisk aus dem App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) und binde dein iPhone in wenigen Minuten als Laufwerk ein. Fragen oder Feedback? Schreib uns an **support@everappz.com**.
</content>
