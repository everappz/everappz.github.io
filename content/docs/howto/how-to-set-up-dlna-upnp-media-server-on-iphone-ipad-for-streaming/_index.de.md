---
title: "DLNA/UPnP-Medienserver auf iPhone & iPad zum Streamen einrichten"
description: "Verwandle dein iPhone oder iPad mit Everdisk in einen DLNA/UPnP-Medienserver und streame Fotos, Videos und Musik uber Wi-Fi auf einen Smart-TV, eine Spielkonsole, VLC oder Kodi. Komplette Einrichtung plus Anleitung zur Verbindung von Samsung-, LG- und Sony-TVs, Windows, Mac, Linux, Android und einem weiteren iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "medienserver", "streaming", "smart tv", "iphone", "ipad", "wifi"]
keywords: ["DLNA Server iPhone", "UPnP Server iPad", "DLNA auf iPhone einrichten", "vom iPhone auf Smart-TV streamen", "DLNA Medienserver iOS", "Videos ohne Kabel auf TV streamen", "iPhone Fotos auf TV abspielen", "Samsung TV DLNA iPhone", "LG TV DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA Medienserver", "UPnP AV Medienserver iOS", "Musik vom iPhone auf TV streamen", "iPhone Medienserver App"]
readingTime: 9
---

{{< author-byline >}}

DLNA (auch UPnP AV genannt) ist das stille Arbeitspferd hinter den meisten Smart-TVs. Es ist eine gemeinsame Sprache, die es einem TV oder Medienplayer erlaubt, eine Mediathek im selben Wi-Fi zu finden und daraus abzuspielen, ganz ohne etwas auf dem TV zu installieren. Wenn dein iPhone oder iPad als diese Mediathek fungieren kann, erscheinen deine Fotos, Videos und Musik von selbst auf dem grossen Bildschirm.

Diese Anleitung zeigt, wie du dein iPhone oder iPad mit [Everdisk](/products/everdisk) in einen DLNA/UPnP-Medienserver verwandelst und wie du diese Mediathek von einem Smart-TV, einer Spielkonsole, VLC, Kodi, einem Computer, einem Android-Handy und sogar einem zweiten iPhone offnest. Alles lauft uber dein lokales Wi-Fi, sodass nichts irgendwohin hochgeladen wird.

## Was du brauchst

- Ein iPhone oder iPad mit installiertem [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Einen TV, Player oder Computer im **selben Wi-Fi-Netzwerk** wie dein Gerat.
- Die Fotos, Videos oder Musik, die du abspielen willst, bereits auf deinem iPhone (in der Fotos-App, der Musik-App oder im Everdisk-Ordner Dokumente).

## Den DLNA-Server in Everdisk einrichten

### Schritt 1: Wahle aus, was geteilt wird

Offne Everdisk und gehe zum Tab **Teilen**. Tippe auf **Was geteilt wird** und wahle deine Inhalte aus:

- Aktiviere **Zugriff auf die gesamte Fotomediathek erlauben**, um jedes Album zu teilen, oder tippe auf **Fotos hinzufügen**, um einige auszuwahlen.
- Aktiviere **Zugriff auf die gesamte Musikmediathek erlauben**, um deine Titel zu teilen, oder tippe auf **Titel hinzufügen** fur eine Auswahl.
- Fuge beliebige Ordner oder Dateien mit **Ordner hinzufügen** und **Datei hinzufügen** hinzu. Der eigene Ordner Dokumente der App wird standardmassig geteilt.

Du musst mindestens ein Element ausgewahlt haben, bevor das Teilen starten kann.

### Schritt 2: TV & Media Center (DLNA) einschalten

Gehe zu **Einstellungen**, dann **Teilen**, dann **Verbindungen**. Stelle sicher, dass **TV & Media Center** aktiviert ist. Es ist standardmassig aktiviert und tragt die Kennzeichnung DLNA. Das ist der Server, nach dem TVs und Player suchen.

### Schritt 3: Teilen starten

Zuruck im Tab **Teilen** tippe auf die grosse Schaltflache **Start**. Dein Gerat ist jetzt ein Medienserver in deinem Wi-Fi. Es erscheint auf anderen Geraten unter seinem freundlichen Namen, dem, der in der App als dein Gerätename angezeigt wird (etwa "Speedy-Hare", bis du ihn anderst).

DLNA-Streaming ist immer offen, daher gibt es am TV kein Passwort einzugeben. Halte Everdisk beim Zusehen auf dem Bildschirm offen, denn iOS pausiert Apps, die vollstandig in den Hintergrund geschoben werden.

## Auf einem Smart-TV abspielen

Das ist der haufigste Fall und dauert meist etwa dreissig Sekunden.

1. Bringe den TV ins **selbe Wi-Fi** wie dein iPhone.
2. Offne den eingebauten Medienplayer des TVs. Der Name hangt von der Marke ab: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** oder **SmartThings** (Samsung), **Content Share** oder **SimplyShare**.
3. Suche nach der Liste der Medienserver oder Quellen. Dein Gerat erscheint dort unter seinem Namen.
4. Wahle es aus, navigiere in deine Fotos, Videos oder Musik und drucke auf Wiedergabe.

Vorschau-Miniaturbilder erscheinen automatisch, sodass du das richtige Urlaubsalbum oder den richtigen Film ohne Raten findest.

### Welche TVs funktionieren

Die meisten TVs von **Samsung, LG, Sony BRAVIA, Panasonic (VIERA-Firmware), Philips und Hisense** haben DLNA eingebaut und funktionieren sofort. **PlayStation- und Xbox-Konsolen und die meisten AV-Receiver** ebenfalls.

Ein paar Plattformen lassen es weg: **Roku-TVs, Amazon Fire TV, Vizio SmartCast und schlichtes Google TV** ohne eine Medien-App des Herstellers. Wenn dein TV einer davon ist und dein Gerat nicht findet, ist das meist der Grund. Installiere auf diesen TVs eine DLNA-Player-App wie VLC oder Kodi oder erreiche deine Dateien stattdessen uber einen Webbrowser mit der [WebDAV-Einrichtungsanleitung](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Manche Marken haben DLNA weiter funktionsfahig gehalten, selbst nachdem sie das offizielle DLNA-Logo entfernt haben. Wenn es also zu fehlen scheint, suche nach einem der oben genannten Medienplayer-Namen.

## In VLC oder Kodi unter Windows, Mac und Linux abspielen

VLC und Kodi sind kostenlos, laufen auf jedem Desktop-System und beherrschen DLNA gut. Sie sind der zuverlassige Weg, deine Everdisk-Mediathek auf einem Computer zu offnen.

**VLC (Windows, Mac, Linux):**

1. Offne VLC.
2. Zeige die Wiedergabeliste an (unter Windows und Linux drucke **Ctrl+L**, auf dem Mac offne die **Playlist** uber das Menu Ansicht).
3. Offne in der Seitenleiste **Universal Plug'n'Play** unter Lokales Netzwerk.
4. Dein Gerat erscheint in der Liste. Klicke hinein und wahle eine Datei.

**Kodi (Windows, Mac, Linux):**

1. Gehe zu **Videos**, **Music** oder **Pictures**, dann **Files**, dann **Add source** (oder **Browse**).
2. Wahle **UPnP devices**.
3. Wahle dein Gerat aus und durchsuche deine Mediathek.

Unter Windows kannst du auch den **Windows Media Player** offnen, in der Seitenleiste **Andere Bibliotheken** aufklappen und dein Gerat erscheint dort.

## Auf Android abspielen

Android-Handys und -Tablets haben keinen System-DLNA-Browser, nutze also eine App:

- **VLC fur Android**: offne das Seitenmenu, tippe auf **Lokales Netzwerk** und dein Gerat erscheint unter den UPnP-Servern.
- **BubbleUPnP** oder eine ahnliche UPnP-App: dein Gerat erscheint in der Serverliste, und diese Apps konnen die Wiedergabe auch an einen TV weiterreichen.

## Auf einem weiteren iPhone oder iPad abspielen

Zwei Gerate, eine Mediathek. Angenommen, die Fotos sind auf deinem iPhone und du willst sie auf deinem iPad ansehen.

- Der einfachste Weg ist Everdisks eigener Tab **Geräte** auf dem zweiten Gerat. Es funktioniert sowohl als DLNA-Client als auch als Server. Offne Everdisk auf dem iPad, gehe zu **Geräte** und dein iPhone erscheint unter **Verfügbare Geräte**. Tippe darauf, um zu durchsuchen und abzuspielen.
- Jede DLNA-Player-App fur iOS funktioniert ebenfalls, etwa VLC oder ein UPnP-Browser. Offne ihre Ansicht des lokalen Netzwerks und wahle dein iPhone.

## Auf einer Spielkonsole abspielen

- **PlayStation 5 und 4**: offne die App **Media** (Media Gallery) und dein Gerat erscheint als Medienserver, den du durchsuchen kannst.
- **Xbox**: nutze eine Medienplayer-App, die DLNA unterstutzt, und wahle dann dein Gerat aus der Serverliste.

## Wenn dein Gerat nicht in der Liste erscheint

Manche Player erlauben, einen Medienserver per Adresse hinzuzufugen, statt zu warten, bis er erkannt wird. Auf dem Everdisk-Bildschirm **Teilen** zeigt die DLNA-Karte eine Gerätebeschreibungsadresse, die auf `/device-desc.xml` endet. Gib diese Adresse im Feld zum Serverhinzufugen des Players ein.

Wenn es immer noch nicht erscheint, prufe drei Dinge: beide Gerate sind im selben Wi-Fi (nicht in einem Gastnetzwerk, das Gerat-zu-Gerat-Verkehr blockiert), Everdisk ist offen und das Teilen ist gestartet, und **TV & Media Center** ist in den Einstellungen aktiviert.

## Wenn ein Video nicht abspielt

DLNA gibt die Datei so, wie sie ist, an den TV weiter, und der TV muss sie dekodieren konnen. Wenn ein Clip die Wiedergabe verweigert, wird sein Format von diesem TV wahrscheinlich nicht unterstutzt. Zwei Losungen:

- Offne **Einstellungen**, dann **Teilen**, dann **Videos** und verringere die **Qualität**. Everdisk konvertiert das Video dann beim Streamen in ein kompatibleres Format. (Die Konvertierung ist eine Premium-Funktion.)
- Oder offne dieselbe Datei in einem Webbrowser uber den Browser-Link von Everdisk, der mit Formaten nachsichtiger umgeht.

## So nutzen Menschen das im Alltag

- **Familienfilmabend.** Mit dem Handy gedrehte Videos laufen auf dem Wohnzimmer-TV, ohne Kabel oder Apple TV.
- **Urlaubsfotos auf dem grossen Bildschirm.** Offne deine Fotomediathek auf dem TV und wische mit allen im Raum durch die Reise.
- **Hintergrundmusik auf einer Party.** Richte einen DLNA-Lautsprecher oder AV-Receiver auf deine Musikmediathek und lass sie laufen.
- **Auf einem Hotel-TV zusehen**, der einen Medienplayer hat, sobald beide Gerate im Wi-Fi des Zimmers sind.

## Ein paar Tipps

- Halte Everdisk beim Streamen offen. Wenn du das Handy lange sperrst, kann iOS die App pausieren und die Wiedergabe stoppt.
- Schliesse das Handy fur lange Filmsitzungen an den Strom an.
- Fur schnellstes Streaming halte **Format** und **Qualität** in den Einstellungen auf **Original** und verringere sie nur, wenn ein bestimmter TV mit einer Datei Muhe hat.
- DLNA dient nur dem Streamen. Niemand auf der TV-Seite kann deine Dateien andern oder loschen. Fur die Dateiubertragung in beide Richtungen nutze stattdessen den [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)-, [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/)- oder [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/)-Server.

## Haufig gestellte Fragen

{{% details title="Was ist der Unterschied zwischen DLNA und UPnP?" closed="true" %}}
Sie sind eng verwandt. UPnP ist der zugrunde liegende Netzwerkstandard und DLNA ist das darauf aufbauende Medienprofil, das TVs und Player nutzen, um Fotos, Videos und Musik zu teilen und abzuspielen. Im Alltag werden die Begriffe synonym verwendet. Wenn du TV & Media Center in Everdisk einschaltest, wird dein Gerat zu einem DLNA/UPnP-Medienserver, den jeder DLNA-Client durchsuchen kann.
{{% /details %}}

{{% details title="Muss ich etwas auf meinem TV installieren?" closed="true" %}}
Nein. Wenn dein TV DLNA unterstutzt, hat er bereits einen Medienplayer, der dein Gerat im Wi-Fi finden kann. Du installierst Everdisk nur auf dem iPhone oder iPad, das die Inhalte enthalt. Wenn dein TV DLNA nicht unterstutzt, installiere einen Player wie VLC oder Kodi auf einem damit verbundenen Gerat.
{{% /details %}}

{{% details title="Warum erscheint mein iPhone nicht auf dem TV?" closed="true" %}}
Prufe, ob beide Gerate im selben Wi-Fi-Netzwerk sind. Gastnetzwerke und manche Buro- oder Hotelnetzwerke verhindern, dass sich Gerate gegenseitig sehen, was DLNA stoppt. Bestatige dann, dass Everdisk offen und das Teilen gestartet ist und dass TV & Media Center in Einstellungen, Teilen, Verbindungen aktiviert ist. Wenn der TV es immer noch nicht findet, fuge den Server von Hand mit der Gerätebeschreibungsadresse hinzu, die auf /device-desc.xml endet.
{{% /details %}}

{{% details title="Braucht DLNA-Streaming ein Passwort?" closed="true" %}}
Nein. DLNA ist, solange es aktiv ist, immer fur jeden im selben Wi-Fi offen, weshalb es auf der TV-Seite kein Login gibt. In einem Heimnetzwerk, dem du vertraust, ist das in Ordnung. In einem Netzwerk, dem du nicht vertraust, schalte TV & Media Center aus, wenn du fertig bist, oder nutze stattdessen den SMB-Server mit Verschlusselung.
{{% /details %}}

{{% details title="Kann ich auf einen Chromecast oder Roku streamen?" closed="true" %}}
Chromecast und Roku fungieren von Haus aus nicht als DLNA-Player, daher finden sie dein Gerat nicht direkt. Die Losung ist, eine DLNA-App zu installieren, die casten kann, etwa VLC oder BubbleUPnP auf einem Handy, und die Wiedergabe von dort an den Chromecast oder Roku weiterzureichen. Auf den meisten anderen Smart-TVs funktioniert DLNA ohne all das.
{{% /details %}}

{{% details title="Ein Video spielt ohne Ton oder offnet sich nicht. Was kann ich tun?" closed="true" %}}
Das ist ein Format, das der TV nicht dekodieren kann. Offne Einstellungen, Teilen, Videos in Everdisk und verringere die Qualität, sodass die App das Video beim Streamen in ein kompatibleres Format konvertiert. Du kannst dieselbe Datei auch uber den Browser-Link offnen, der mehr Formate verarbeitet.
{{% /details %}}

{{% details title="Kann ich Musik streamen, nicht nur Video?" closed="true" %}}
Ja. Aktiviere Zugriff auf die gesamte Musikmediathek erlauben oder fuge bestimmte Titel hinzu, dann starte das Teilen. Deine Titel erscheinen auf jedem DLNA-Lautsprecher, AV-Receiver oder TV, mit Cover und Titeldetails. Musik wird immer in Originalqualitat geteilt.
{{% /details %}}

{{% details title="Muss die App offen bleiben, wahrend ich zusehe?" closed="true" %}}
Ja. Dein iPhone fungiert als Server, und iOS pausiert Apps, die lange vollstandig in den Hintergrund geschoben werden. Halte Everdisk beim Streamen auf dem Bildschirm und schliesse fur lange Sitzungen den Strom an.
{{% /details %}}

{{% details title="Wie streame ich von einem iPhone auf ein anderes iPad?" closed="true" %}}
Starte das Teilen auf dem iPhone, offne dann Everdisk auf dem iPad und gehe zum Tab Geräte. Das iPhone erscheint unter Verfügbare Geräte als Medienserver. Tippe darauf, um zu durchsuchen und abzuspielen. Everdisk funktioniert als DLNA-Client und Server, du brauchst also keine weitere App.
{{% /details %}}

{{% details title="Ist Everdisk kostenlos?" closed="true" %}}
Ja, Everdisk ist ein kostenloser Download und der DLNA-Medienserver ist enthalten. Ein optionaler einmaliger Premium-Lifetime-Kauf fugt Extras hinzu, etwa Foto- und Videokonvertierung fur altere TVs, individuelle Ports und mehr. Du kannst DLNA-Streaming einrichten und nutzen, ohne zu zahlen.
{{% /details %}}

Bereit, es auszuprobieren? [Lade Everdisk aus dem App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) und streame dein erstes Album in wenigen Minuten auf den TV. Fragen oder Feedback? Schreib uns an **support@everappz.com**.
</content>
</invoke>
