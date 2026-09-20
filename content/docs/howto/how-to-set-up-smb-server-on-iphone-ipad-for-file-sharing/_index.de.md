---
title: "SMB-Server auf iPhone & iPad zum Teilen von Dateien einrichten"
description: "Verwandle dein iPhone oder iPad mit Everdisk in einen SMB-Dateiserver und offne es uber Wi-Fi wie ein Netzlaufwerk von einem Mac, einem weiteren iPhone, Linux oder Android. Komplette Einrichtung, die smb-Adresse und der Port, optionale SMB3-Verschlusselung und die Verbindung Schritt fur Schritt fur jedes Gerat."
date: 2026-09-19
tags: ["everdisk", "smb", "dateien teilen", "netzlaufwerk", "iphone", "ipad", "mac", "finder", "verschlusselung", "wifi"]
keywords: ["SMB Server iPhone", "SMB Server iPad", "SMB auf iPhone einrichten", "iPhone SMB Freigabe", "iPhone SMB mit Mac Finder verbinden", "smb iphone zu iphone", "iOS Dateien App mit SMB Server verbinden", "Dateien vom iPhone per SMB teilen", "iphone Netzlaufwerk Finder", "SMB3 Verschlusselung iOS", "smb Freigabe iPhone Android", "mit SMB von Linux verbinden", "iphone als Netzlaufwerk", "Dateien zwischen iphones per wifi teilen", "iphone als Netzlaufwerk einbinden"]
readingTime: 10
---

{{< author-byline >}}

SMB ist die Dateifreigabe, die in macOS, Windows und Linux und in fast jedes Netzlaufwerk (NAS) eingebaut ist. Wenn du dich mit einem geteilten Ordner auf einem anderen Computer verbindest und er sich wie eine normale Festplatte im Finder oder Datei-Explorer offnet, ist das SMB bei der Arbeit. Mit [Everdisk](/products/everdisk) kannst du eine SMB-Freigabe auf deinem iPhone oder iPad einrichten, sodass das Handy selbst als Netzlaufwerk erscheint, das andere Gerate durchsuchen, von dem sie kopieren und auf das sie kopieren.

Das ist die Wahl, wenn dein iPhone sich wie eine echte Festplatte verhalten soll und nicht wie eine Webseite. Es ist schnell, es zieht und legt in beide Richtungen ab, und es ist der einzige Verbindungstyp in Everdisk, der jede Ubertragung verschlusseln kann. Diese Anleitung behandelt die Einrichtung und wie du dich von einem Mac, einem weiteren iPhone oder iPad, Linux, Android und Windows verbindest.

## Was du brauchst

- Ein iPhone oder iPad mit installiertem [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Ein weiteres Gerat im **selben Wi-Fi-Netzwerk**.
- Die Dateien, die du teilen willst, im Everdisk-Ordner Dokumente oder in Ordnern, die du hinzufugst.

## Den SMB-Server in Everdisk einrichten

### Schritt 1: Wahle aus, was geteilt wird und wer schreiben darf

Offne Everdisk, gehe zum Tab **Teilen** und tippe auf **Was geteilt wird**. Der Ordner Dokumente wird standardmassig geteilt. Fuge mehr mit **Ordner hinzufügen** und **Datei hinzufügen** hinzu und aktiviere deine Foto- oder Musikmediathek, wenn du auch diese verfugbar machen willst.

Entscheide, ob andere Gerate deine Dateien nur lesen oder auch andern konnen. Offne **Einstellungen**, dann **Teilen**, dann **Zugriff** und stelle **Dateibearbeitung** ein. Mit aktivierter Option konnen verbundene Gerate Dateien auf dein Handy kopieren und umbenennen oder loschen. Mit deaktivierter Option ist die Freigabe schreibgeschutzt.

Wenn du ein Login willst, lege einen **Anmeldename** und ein **Passwort** auf demselben Zugriff-Bildschirm fest. Lass beide leer, um Gastzugriff zu erlauben.

### Schritt 2: Den SMB-Server einschalten

Gehe zu **Einstellungen**, dann **Teilen**, dann **Verbindungen** und aktiviere **Computer (Erweitert)**. Das ist der SMB-Server (er tragt die Kennzeichnung SMB).

### Schritt 3: Teilen starten und die Adresse notieren

Gehe zuruck zum Tab **Teilen** und tippe auf **Start**. Der Abschnitt **So verbindest du dich** zeigt nun die SMB-Adresse. Sie sieht so aus:

```
smb://192.168.1.20:4455/Share
```

Drei Dinge, die du uber diese Adresse wissen solltest:

- Die Zahl nach dem Doppelpunkt ist der **Port**. Everdisk nutzt standardmassig **4455**.
- Die Freigabe heisst **Share**.
- Der erste Teil ist die Adresse deines iPhones im Wi-Fi, daher ist er in deinem Netzwerk anders.

Halte Everdisk offen, wahrend Gerate verbunden sind, denn iOS pausiert Apps, die zu lange im Hintergrund liegen.

## Von einem Mac verbinden

Das ist der reibungsloseste Fall, weil macOS SMB nativ beherrscht.

Der schnellste Weg: offne den **Finder** und schau in der Seitenleiste unter **Orte** oder **Netzwerk**. Everdisk kundigt sich im Wi-Fi an, sodass dein iPhone dort oft von selbst erscheint. Klicke darauf, dann auf **Verbinden als** und wahle **Gast** oder gib dein Login ein.

Um von Hand zu verbinden:

1. Wahle im Finder **Gehe zu**, dann **Mit Server verbinden** (oder drucke **Command und K**).
2. Gib die in Everdisk angezeigte SMB-Adresse ein, zum Beispiel `smb://192.168.1.20:4455/Share`.
3. Klicke auf **Verbinden**, dann wahle **Gast** oder gib deinen **Anmeldename** und dein **Passwort** ein.

Dein iPhone offnet sich in einem Finder-Fenster. Kopiere Dateien durch Ziehen hinein oder heraus, genau wie bei jeder anderen Festplatte (wenn Dateibearbeitung aktiviert ist).

## Von einem weiteren iPhone oder iPad verbinden

iOS und iPadOS konnen SMB-Freigaben in der eingebauten App **Dateien** offnen, was Ubertragungen von Handy zu Handy sauber und schnell macht.

Auf dem zweiten Gerat:

1. Offne die App **Dateien**.
2. Tippe auf die Schaltflache **Mehr** (die drei Punkte, oben rechts auf dem iPhone) und wahle **Mit Server verbinden**.
3. Gib die SMB-Adresse aus Everdisk ein, zum Beispiel `smb://192.168.1.20:4455/Share`.
4. Wahle **Gast** oder **Registrierter Benutzer** und gib dein Login ein.
5. Die Freigabe erscheint unter Orte in Dateien. Durchsuche und kopiere in beide Richtungen.

Du kannst auf dem zweiten Gerat auch Everdisks eigenen Tab **Geräte** nutzen, der einen SMB-Client enthalt. Offne Everdisk, gehe zu **Geräte**, tippe auf **Neue Verbindung**, wahle **SMB** und gib die Adresse ein.

## Von Linux verbinden

1. Offne deinen Dateimanager (Files/Nautilus unter GNOME, Dolphin unter KDE).
2. Wahle **Andere Orte** oder **Mit Server verbinden**.
3. Gib die Adresse ein, zum Beispiel `smb://192.168.1.20:4455/Share`.
4. Verbinde dich als Gast oder gib dein Login ein.

Von einem Terminal kannst du auch `smbclient //192.168.1.20/Share -p 4455` ausfuhren und dein Login eingeben, wenn du danach gefragt wirst.

## Von Android verbinden

Android hat keinen System-SMB-Browser, nutze also einen Dateimanager, der SMB unterstutzt:

1. Installiere eine App wie **CX File Explorer**, **Solid Explorer** oder **X-plore File Manager**.
2. Fuge eine neue **SMB**- oder **LAN**-Verbindung hinzu.
3. Gib den Host (die Wi-Fi-Adresse deines iPhones) ein, setze den **Port auf 4455** und den Freigabenamen **Share**.
4. Verbinde dich als Gast oder mit deinem Login, dann durchsuche und kopiere.

## Von Windows verbinden

Windows kann SMB-Freigaben lesen, mit einer Einschrankung, die man vorab kennen sollte. Der eingebaute Datei-Explorer spricht SMB nur uber den Standardport und lasst dich keinen individuellen Port in den Pfad eingeben, und Everdisk nutzt Port 4455. Daher erreicht der schlichte Weg **Netzlaufwerk verbinden** ihn oft nicht.

Du hast unter Windows zwei gute Optionen:

- Nutze einen Dateimanager oder SMB-Client, der einen individuellen Port erlaubt, und richte ihn auf die Adresse deines iPhones mit Port **4455** und dem Freigabenamen **Share**.
- Oder verbinde dich von Windows stattdessen uber einen der anderen Server von Everdisk. Die [WebDAV-Einrichtung](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) und die [FTP-Einrichtung](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) funktionieren beide gut aus dem Windows-Datei-Explorer, und der Browser-Link funktioniert in jedem Browser.

Wenn du Netzlaufwerk verbinden dennoch versuchen willst: offne den **Datei-Explorer**, klicke mit der rechten Maustaste auf **Dieser PC**, wahle **Netzlaufwerk verbinden** und gib den in Everdisk angezeigten Host und Freigabenamen ein. Wenn es sich nicht verbinden kann, liegt das an der oben genannten Port-Einschrankung, wechsle also zu WebDAV oder FTP.

## Verschlusselung fur nicht vertrauenswurdiges Wi-Fi einschalten

SMB ist die einzige Everdisk-Verbindung, die jede Ubertragung verschlusseln kann, was in einem Wi-Fi zahlt, das du nicht vollstandig kontrollierst, etwa in einem Cafe oder einem Buronetzwerk.

1. Lege in **Einstellungen**, **Teilen**, **Zugriff** einen **Anmeldename** und ein **Passwort** fest. Verschlusselte Verbindungen konnen nicht anonym sein, daher ist dieser Schritt erforderlich.
2. Aktiviere in **Einstellungen**, **Teilen** die Option **SMB-Verschlüsselung anfordern**.
3. Stoppe das Teilen und starte es erneut, damit die Anderung wirksam wird.

Jede SMB-Ubertragung ist dann mit **SMB3-Verschlusselung (AES)** geschutzt. Das verbindende Gerat muss SMB3 unterstutzen, was der Finder auf einem modernen Mac und Windows 10 oder neuer beide tun. Die SMB-Verschlusselung ist Teil des einmaligen Premium-Kaufs.

## Nur lesen oder lesen und schreiben

Der Schalter **Dateibearbeitung** in Einstellungen, Teilen, Zugriff steuert das fur jeden Server, einschliesslich SMB. Aktiviere ihn und verbundene Gerate konnen hochladen, umbenennen und loschen. Deaktiviere ihn und sie konnen Dateien nur durchsuchen und von deinem Handy kopieren. Wahle Nur lesen, wenn du Dateien an jemanden ubergibst, von dem du nicht willst, dass er etwas andert.

## So nutzen Menschen das im Alltag

- **Einen grossen Ordner von einem Mac auf dein iPhone verschieben**, indem du ihn in das Finder-Fenster ziehst, schneller als ein Web-Upload.
- **Einen Tag voller Fotos und Videos von deinem Handy holen** auf einen Laptop, ohne iTunes oder Kabel.
- **Dateien zwischen zwei iPhones senden** uber die App Dateien, ohne eine dritte App auf beiden Seiten.
- **Direkt mit einer Datei arbeiten**, indem du ein Dokument direkt vom Handy in einer App auf deinem Mac offnest und zuruckspeicherst.

## Ein paar Tipps

- Halte Everdisk offen, wahrend ein Gerat verbunden ist. Das Handy lange zu sperren kann die App pausieren und die Verbindung trennen.
- Wenn ein Mac das Handy nicht in der Finder-Seitenleiste sieht, verbinde dich von Hand mit Mit Server verbinden und der vollstandigen smb-Adresse.
- Fur beste Geschwindigkeit bei grossen Ubertragungen halte die Foto- und Videoqualitat in den Einstellungen auf Original.
- In einem nicht vertrauenswurdigen Netzwerk aktiviere SMB-Verschlüsselung anfordern und schalte die anderen Server aus, wahrend du arbeitest.

## Haufig gestellte Fragen

{{% details title="Was sind die SMB-Adresse und der Port fur mein iPhone?" closed="true" %}}
Nachdem du das Teilen gestartet hast, zeigt Everdisk die Adresse auf dem Teilen-Bildschirm. Sie sieht aus wie smb://192.168.1.20:4455/Share. Die 4455 ist der Port, den Everdisk fur SMB nutzt, und Share ist der Name des geteilten Ordners. Der erste Teil ist die Adresse deines iPhones im Wi-Fi, deiner wird also anders sein.
{{% /details %}}

{{% details title="Kann ich mich mit meiner iPhone-SMB-Freigabe von Windows verbinden?" closed="true" %}}
Der Windows-Datei-Explorer verbindet sich nur uber den Standardport mit SMB und akzeptiert keinen individuellen Port im Pfad, wahrend Everdisk Port 4455 nutzt. Daher erreicht der schlichte Weg Netzlaufwerk verbinden ihn oft nicht. Nutze einen Dateimanager, der einen individuellen Port erlaubt, oder verbinde dich von Windows stattdessen mit WebDAV, FTP oder dem Browser-Link. All diese funktionieren von Windows ohne Port-Probleme.
{{% /details %}}

{{% details title="Wie teile ich Dateien zwischen zwei iPhones mit SMB?" closed="true" %}}
Starte den SMB-Server auf dem ersten iPhone in Everdisk. Offne auf dem zweiten iPhone die App Dateien, tippe auf die Schaltflache Mehr, wahle Mit Server verbinden und gib die in Everdisk angezeigte smb-Adresse ein (zum Beispiel smb://192.168.1.20:4455/Share). Verbinde dich als Gast oder mit deinem Login, und die Freigabe erscheint in Dateien. Du kannst auf dem zweiten Handy auch Everdisks eigenen Tab Geräte nutzen.
{{% /details %}}

{{% details title="Erscheint mein iPhone automatisch in der Mac-Finder-Seitenleiste?" closed="true" %}}
Meistens ja. Everdisk kundigt die SMB-Freigabe in deinem Wi-Fi an, sodass dein iPhone oft unter Orte oder Netzwerk in der Finder-Seitenleiste erscheint. Klicke darauf und wahle Verbinden als, dann Gast oder dein Login. Wenn es nicht erscheint, verbinde dich von Hand mit Gehe zu, Mit Server verbinden und der vollstandigen smb-Adresse.
{{% /details %}}

{{% details title="Brauche ich ein Passwort, um SMB zu nutzen?" closed="true" %}}
Nein, ein Login ist optional. Lass Anmeldename und Passwort in Einstellungen, Teilen, Zugriff leer, um Gastzugriff zu erlauben. Lege sie fest, wenn du willst, dass sich Verbindungen anmelden. Ein Anmeldename und ein Passwort sind nur erforderlich, wenn du SMB-Verschlüsselung anfordern aktivierst, denn verschlusselte Verbindungen konnen nicht anonym sein.
{{% /details %}}

{{% details title="Ist die SMB-Verbindung verschlusselt?" closed="true" %}}
Sie kann es sein. SMB ist die einzige Everdisk-Verbindung, die Verschlusselung unterstutzt. Lege einen Anmeldename und ein Passwort fest, aktiviere dann SMB-Verschlüsselung anfordern in Einstellungen, Teilen. Jede Ubertragung ist dann mit SMB3 (AES) geschutzt. Das andere Gerat muss SMB3 unterstutzen, was moderne Macs und Windows 10 oder neuer tun. Die Verschlusselung ist eine Premium-Funktion.
{{% /details %}}

{{% details title="Konnen Leute meine Dateien uber SMB andern oder loschen?" closed="true" %}}
Nur wenn du es erlaubst. Der Schalter Dateibearbeitung in Einstellungen, Teilen, Zugriff steuert das. Mit aktivierter Option konnen verbundene Gerate hochladen, umbenennen und loschen. Mit deaktivierter Option ist die Freigabe schreibgeschutzt, und andere konnen Dateien durchsuchen und von deinem Handy kopieren, aber nichts andern.
{{% /details %}}

{{% details title="Warum ist meine SMB-Verbindung abgebrochen?" closed="true" %}}
Dein iPhone ist der Server, und iOS pausiert Apps, die zu lange im Hintergrund bleiben. Halte Everdisk auf dem Bildschirm offen, wahrend ein Gerat verbunden ist, und schliesse das Handy bei langen Ubertragungen an den Strom an. Stelle ausserdem sicher, dass beide Gerate im selben Wi-Fi geblieben sind.
{{% /details %}}

{{% details title="SMB, WebDAV oder FTP, was soll ich nutzen?" closed="true" %}}
Nutze SMB, wenn sich das Handy wie ein echtes Netzlaufwerk auf einem Mac, einem weiteren iPhone, Linux oder einem NAS verhalten soll und wenn du Verschlusselung willst. Nutze WebDAV, wenn du ein Netzlaufwerk willst, das auch von Windows gut funktioniert. Nutze FTP fur die breiteste Kompatibilitat mit alteren Geraten und Apps. Everdisk kann sie alle gleichzeitig betreiben, du bist also nicht auf eines festgelegt.
{{% /details %}}

{{% details title="Ist Everdisk kostenlos?" closed="true" %}}
Ja, Everdisk ist ein kostenloser Download und der SMB-Server ist enthalten. Der optionale einmalige Premium-Kauf fugt SMB-Verschlusselung, individuelle Ports und ein paar weitere Extras hinzu. Du kannst SMB einrichten und Dateien teilen, ohne zu zahlen.
{{% /details %}}

Bereit, es auszuprobieren? [Lade Everdisk aus dem App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) und offne dein iPhone in etwa einer Minute im Finder. Fragen oder Feedback? Schreib uns an **support@everappz.com**.
</content>
