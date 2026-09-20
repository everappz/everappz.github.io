---
title: "Hogyan állíts be SMB szervert iPhone-on és iPad-en fájlmegosztáshoz"
description: "Alakítsd iPhone-odat vagy iPad-edet SMB fájlszerverré az Everdiskkel, és nyisd meg hálózati meghajtóként egy Macről, egy másik iPhone-ról, Linuxról vagy Androidról Wi-Fi felett. Teljes beállítás, az smb-cím és a port, opcionális SMB3-titkosítás, és lépésről lépésre csatlakozás minden eszközhöz."
date: 2026-09-19
tags: ["everdisk", "smb", "fájlmegosztás", "hálózati meghajtó", "iphone", "ipad", "mac", "finder", "titkosítás", "wifi"]
keywords: ["SMB szerver iPhone", "SMB szerver iPad", "hogyan állíts be SMB-t iPhone-on", "iPhone SMB megosztás", "iPhone SMB csatlakozás Mac Finder", "smb iphone-ról iphone-ra", "iOS Fájlok app csatlakozás szerverhez SMB", "fájlok megosztása iPhone SMB", "iphone hálózati meghajtó Finder", "SMB3-titkosítás iOS", "smb megosztás iPhone Android", "csatlakozás SMB-hez Linuxról", "iphone mint hálózati meghajtó", "fájlok megosztása iphone-ok között wifi", "iphone csatlakoztatása hálózati meghajtóként"]
readingTime: 10
---

{{< author-byline >}}

Az SMB a macOS-be, a Windowsba és a Linuxba, valamint szinte minden hálózati meghajtóba (NAS) beépített fájlmegosztás. Amikor egy másik számítógép megosztott mappájához csatlakozol és az normál lemezként nyílik meg a Finderben vagy a Fájlkezelőben, azt az SMB végzi. Az [Everdisk](/products/everdisk) segítségével elhelyezhetsz egy SMB-megosztást az iPhone-odon vagy iPad-eden, így maga a telefon jelenik meg hálózati meghajtóként, amelyet a többi eszköz böngész, amelyről másol, és amelyre másol.

Ez az a lehetőség, amelyhez akkor nyúlj, ha azt szeretnéd, hogy az iPhone-od egy rendes meghajtóként viselkedjen, ne egy weboldalként. Gyors, mindkét irányba fog és visz, és ez az egyetlen kapcsolattípus az Everdiskben, amely minden átvitelt titkosítani tud. Ez az útmutató a beállítást és a Macről, egy másik iPhone-ról vagy iPad-ről, Linuxról, Androidról és Windowsról való csatlakozást ismerteti.

## Mire lesz szükséged

- Egy iPhone vagy iPad telepített [Everdiskkel](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Egy másik eszköz **ugyanazon a Wi-Fi hálózaton**.
- A fájlok, amelyeket meg szeretnél osztani, az Everdisk Dokumentumok mappájában vagy az általad hozzáadott mappákban.

## Az SMB szerver beállítása az Everdiskben

### 1. lépés: Válaszd ki, mit oszd meg és ki írhat

Nyisd meg az Everdisket, lépj a **Megosztás** fülre, és érintsd meg a **Mit oszd meg** lehetőséget. A Dokumentumok mappa alapból meg van osztva. Adj hozzá többet a **Mappa hozzáadása** és **Fájl hozzáadása** gombokkal, és kapcsold be a Fényképek vagy a Zene könyvtáradat, ha azokat is elérhetővé szeretnéd tenni.

Döntsd el, hogy a többi eszköz csak olvashatja a fájljaidat, vagy módosíthatja is őket. Nyisd meg a **Beállítások**, majd a **Megosztás**, majd a **Hozzáférés** menüt, és állítsd be a **Fájlszerkesztés** lehetőséget. Bekapcsolva a csatlakozó eszközök fájlokat másolhatnak a telefonodra, valamint átnevezhetnek vagy törölhetnek. Kikapcsolva a megosztás csak olvasható.

Ha bejelentkezést szeretnél, állíts be egy **Felhasználónevet** és **Jelszót** ugyanazon a Hozzáférés képernyőn. Hagyd mindkettőt üresen a vendéghozzáférés engedélyezéséhez.

### 2. lépés: Kapcsold be az SMB szervert

Lépj a **Beállítások**, majd a **Megosztás**, majd a **Kapcsolatok** menübe, és kapcsold be a **Számítógép (speciális)** lehetőséget. Ez az SMB szerver (az SMB címkét viseli).

### 3. lépés: Indítsd el a megosztást és jegyezd fel a címet

Lépj vissza a **Megosztás** fülre és érintsd meg a **Start** gombot. A **Hogyan csatlakozz** szakasz most már mutatja az SMB-címet. Így néz ki:

```
smb://192.168.1.20:4455/Share
```

Három dolgot érdemes tudni erről a címről:

- A kettőspont utáni szám a **port**. Az Everdisk alapból a **4455**-öt használja.
- A megosztás neve **Share**.
- Az első rész az iPhone-od Wi-Fi-címe, így a te hálózatodon más lesz.

Tartsd nyitva az Everdisket, amíg eszközök csatlakoznak, mert az iOS szünetelteti a túl sokáig a háttérben lévő alkalmazásokat.

## Csatlakozás egy Macről

Ez a legzökkenőmentesebb eset, mert a macOS natívan beszéli az SMB-t.

A leggyorsabb út: nyisd meg a **Findert** és nézd meg az oldalsávot a **Locations** vagy **Network** alatt. Az Everdisk bejelenti magát a Wi-Fi hálózaton, így az iPhone-od gyakran magától megjelenik ott. Kattints rá, majd kattints a **Connect As** gombra és válaszd a **Guest** lehetőséget, vagy add meg a bejelentkezésedet.

Csatlakozás kézzel:

1. A Finderben válaszd a **Go**, majd a **Connect to Server** menüpontot (vagy nyomd meg a **Command és K** billentyűket).
2. Írd be az Everdiskben megjelenő SMB-címet, például `smb://192.168.1.20:4455/Share`.
3. Kattints a **Connect** gombra, majd válaszd a **Guest** lehetőséget, vagy add meg a **Felhasználónevedet** és **Jelszavadat**.

Az iPhone-od megnyílik egy Finder-ablakban. Másolj be vagy ki fájlokat húzással, pontosan úgy, mint bármely más meghajtón (ha a Fájlszerkesztés be van kapcsolva).

## Csatlakozás egy másik iPhone-ról vagy iPad-ről

Az iOS és az iPadOS meg tud nyitni SMB-megosztásokat a beépített **Fájlok** appban, ami tisztává és gyorssá teszi a telefonok közötti átvitelt.

A második készüléken:

1. Nyisd meg a **Fájlok** appot.
2. Érintsd meg a **továbbiak** gombot (a három pont, iPhone-on jobbra fent) és válaszd a **Connect to Server** lehetőséget.
3. Add meg az Everdiskből származó SMB-címet, például `smb://192.168.1.20:4455/Share`.
4. Válaszd a **Guest** lehetőséget, vagy a **Registered User** lehetőséget és add meg a bejelentkezésedet.
5. A megosztás megjelenik a Locations alatt a Fájlokban. Böngéssz és másolj mindkét irányba.

Használhatod az Everdisk saját **Eszközök** fülét is a második készüléken, amely tartalmaz egy SMB-klienst. Nyisd meg az Everdisket, lépj az **Eszközök** fülre, érintsd meg az **Új kapcsolat** lehetőséget, válaszd az **SMB** lehetőséget, és add meg a címet.

## Csatlakozás Linuxról

1. Nyisd meg a fájlkezelődet (Files/Nautilus GNOME-on, Dolphin KDE-n).
2. Válaszd az **Other Locations** vagy a **Connect to Server** lehetőséget.
3. Add meg a címet, például `smb://192.168.1.20:4455/Share`.
4. Csatlakozz vendégként, vagy add meg a bejelentkezésedet.

Egy terminálból a `smbclient //192.168.1.20/Share -p 4455` parancsot is futtathatod, és rákérdezéskor megadhatod a bejelentkezésedet.

## Csatlakozás Androidról

Az Androidon nincs rendszerszintű SMB-böngésző, ezért használj egy SMB-t támogató fájlkezelőt:

1. Telepíts egy alkalmazást, mint a **CX File Explorer**, a **Solid Explorer** vagy az **X-plore File Manager**.
2. Adj hozzá egy új **SMB** vagy **LAN** kapcsolatot.
3. Add meg a hosztot (az iPhone-od Wi-Fi-címét), állítsd be a **portot 4455-re**, és a megosztás nevét **Share**-re.
4. Csatlakozz vendégként vagy a bejelentkezéseddel, majd böngéssz és másolj.

## Csatlakozás Windowsról

A Windows tud olvasni SMB-megosztásokat, egy előre érdemes tudni való bökkenővel. A beépített Fájlkezelő csak a szabványos porton beszél SMB-t és nem engedi, hogy egyéni portot írj be az elérési útba, az Everdisk pedig a 4455-ös portot használja. Így a sima **Hálózati meghajtó csatlakoztatása** útvonal gyakran nem éri el.

Két jó lehetőséged van Windowson:

- Használj egy olyan fájlkezelőt vagy SMB-klienst, amely lehetővé teszi egyéni port beállítását, és irányítsd az iPhone-od címére a **4455**-ös porttal és a **Share** megosztásnévvel.
- Vagy csatlakozz Windowsról inkább az Everdisk másik szerverei egyikével. A [WebDAV-beállítás](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) és az [FTP-beállítás](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) egyaránt jól működik a Windows Fájlkezelőből, a böngészőlink pedig bármely böngészőben.

Ha mégis ki szeretnéd próbálni a Hálózati meghajtó csatlakoztatása lehetőséget: nyisd meg a **Fájlkezelőt**, kattints jobb gombbal az **Ez a gép** elemre, válaszd a **Hálózati meghajtó csatlakoztatása** lehetőséget, és add meg az Everdiskben megjelenő hosztot és megosztásnevet. Ha nem tud csatlakozni, az a fenti portkorlátozás, ezért válts WebDAV-ra vagy FTP-re.

## Kapcsold be a titkosítást a nem megbízható Wi-Fi-hez

Az SMB az egyetlen Everdisk-kapcsolat, amely minden átvitelt titkosítani tud, ami számít az olyan Wi-Fi-n, amelyet nem irányítasz teljesen, mint egy kávézó vagy egy irodai hálózat.

1. A **Beállítások**, **Megosztás**, **Hozzáférés** menüben állíts be egy **Felhasználónevet** és **Jelszót**. A titkosított kapcsolatok nem lehetnek névtelenek, ezért ez a lépés kötelező.
2. A **Beállítások**, **Megosztás** menüben kapcsold be az **SMB-titkosítás megkövetelése** lehetőséget.
3. Állítsd le és indítsd újra a megosztást, hogy a módosítás életbe lépjen.

Ekkor minden SMB-átvitelt **SMB3-titkosítás (AES)** véd. A csatlakozó eszköznek támogatnia kell az SMB3-at, amit egy modern Macen a Finder és a Windows 10 vagy újabb egyaránt megtesz. Az SMB-titkosítás az egyszeri Premium vásárlás része.

## Csak olvasható vagy olvasható és írható

A **Fájlszerkesztés** kapcsoló a Beállítások, Megosztás, Hozzáférés menüben minden szervernél ezt szabályozza, az SMB-t is beleértve. Kapcsold be és a csatlakozó eszközök feltölthetnek, átnevezhetnek és törölhetnek. Kapcsold ki és csak böngészhetnek és lemásolhatnak fájlokat a telefonodról. Válaszd a csak olvashatót, amikor olyasvalakinek adsz át fájlokat, akit nem szeretnél, hogy bármit módosítson.

## Valós helyzetek, ahogy az emberek ezt használják

- **Egy nagy mappa áthelyezése az iPhone-odra egy Macről** úgy, hogy behúzod a Finder-ablakba, gyorsabban mint egy webes feltöltés.
- **Egy nap fényképeinek és videóinak leszedése a telefonodról** egy laptopra iTunes vagy kábel nélkül.
- **Fájlok küldése két iPhone között** a Fájlok appon keresztül, harmadik alkalmazás nélkül egyik oldalon sem.
- **Egy fájllal helyben dolgozni**, egy dokumentumot közvetlenül a telefonról megnyitva egy alkalmazásban a Macen és visszamentve.

## Néhány tipp

- Tartsd nyitva az Everdisket, amíg egy eszköz csatlakozik. A telefon hosszú időre való lezárása szüneteltetheti az alkalmazást és megszakíthatja a kapcsolatot.
- Ha egy Mac nem látja a telefont a Finder oldalsávjában, csatlakozz kézzel a Connect to Server lehetőséggel és a teljes smb-címmel.
- A nagy átvitelek legjobb sebességéhez tartsd a fénykép- és videóminőséget Eredetin a Beállításokban.
- Egy nem megbízható hálózaton kapcsold be az SMB-titkosítás megkövetelése lehetőséget és kapcsold ki a többi szervert, amíg dolgozol.

## Gyakran ismételt kérdések

{{% details title="Mi az iPhone-om SMB-címe és portja?" closed="true" %}}
Miután elindítod a megosztást, az Everdisk mutatja a címet a Megosztás képernyőn. Így néz ki: smb://192.168.1.20:4455/Share. A 4455 az a port, amelyet az Everdisk az SMB-hez használ, a Share pedig a megosztott mappa neve. Az első rész az iPhone-od Wi-Fi-címe, így a tiéd más lesz.
{{% /details %}}

{{% details title="Csatlakozhatok az iPhone-om SMB-megosztásához Windowsról?" closed="true" %}}
A Windows Fájlkezelő csak a szabványos porton csatlakozik SMB-hez és nem fogad el egyéni portot az elérési útban, az Everdisk pedig a 4455-ös portot használja. Így a sima Hálózati meghajtó csatlakoztatása útvonal gyakran nem éri el. Használj egy olyan fájlkezelőt, amely lehetővé teszi egyéni port beállítását, vagy csatlakozz Windowsról inkább WebDAV-val, FTP-vel vagy a böngészőlinkkel. Ezek mind portgondok nélkül működnek Windowsról.
{{% /details %}}

{{% details title="Hogyan osztok meg fájlokat két iPhone között SMB-vel?" closed="true" %}}
Indítsd el az SMB szervert az első iPhone-on az Everdiskben. A második iPhone-on nyisd meg a Fájlok appot, érintsd meg a továbbiak gombot, válaszd a Connect to Server lehetőséget, és add meg az Everdiskben megjelenő smb-címet (például smb://192.168.1.20:4455/Share). Csatlakozz Guest lehetőséggel vagy a bejelentkezéseddel, és a megosztás megjelenik a Fájlokban. Használhatod az Everdisk saját Eszközök fülét is a második telefonon.
{{% /details %}}

{{% details title="Automatikusan megjelenik az iPhone-om a Mac Finder oldalsávjában?" closed="true" %}}
Általában igen. Az Everdisk bejelenti az SMB-megosztást a Wi-Fi hálózatodon, így az iPhone-od gyakran megjelenik a Locations vagy a Network alatt a Finder oldalsávjában. Kattints rá és válaszd a Connect As, majd a Guest lehetőséget vagy a bejelentkezésedet. Ha nem jelenik meg, csatlakozz kézzel a Go, Connect to Server lehetőséggel és a teljes smb-címmel.
{{% /details %}}

{{% details title="Kell jelszó az SMB használatához?" closed="true" %}}
Nem, a bejelentkezés opcionális. Hagyd a Felhasználónevet és a Jelszót üresen a Beállítások, Megosztás, Hozzáférés menüben a vendéghozzáférés engedélyezéséhez. Állítsd be őket, ha azt szeretnéd, hogy a kapcsolatok bejelentkezzenek. Felhasználónév és jelszó csak akkor kötelező, ha bekapcsolod az SMB-titkosítás megkövetelése lehetőséget, mert a titkosított kapcsolatok nem lehetnek névtelenek.
{{% /details %}}

{{% details title="Titkosított az SMB kapcsolat?" closed="true" %}}
Lehet. Az SMB az egyetlen Everdisk-kapcsolat, amely támogatja a titkosítást. Állíts be egy felhasználónevet és jelszót, majd kapcsold be az SMB-titkosítás megkövetelése lehetőséget a Beállítások, Megosztás menüben. Ekkor minden átvitelt SMB3 (AES) véd. A másik eszköznek támogatnia kell az SMB3-at, amit a modern Macek és a Windows 10 vagy újabb megtesznek. A titkosítás Premium funkció.
{{% /details %}}

{{% details title="Módosíthatják vagy törölhetik mások a fájljaimat SMB felett?" closed="true" %}}
Csak ha megengeded. A Fájlszerkesztés kapcsoló a Beállítások, Megosztás, Hozzáférés menüben szabályozza ezt. Bekapcsolva a csatlakozó eszközök feltölthetnek, átnevezhetnek és törölhetnek. Kikapcsolva a megosztás csak olvasható, és mások böngészhetnek és lemásolhatnak fájlokat a telefonodról, de nem módosíthatnak semmit.
{{% /details %}}

{{% details title="Miért szakadt meg az SMB kapcsolatom?" closed="true" %}}
Az iPhone-od a szerver, és az iOS szünetelteti a túl sokáig a háttérben maradó alkalmazásokat. Tartsd az Everdisket a képernyőn, amíg egy eszköz csatlakozik, és csatlakoztasd a telefont a hálózathoz a hosszú átvitelek alatt. Győződj meg arról is, hogy mindkét eszköz ugyanazon a Wi-Fi hálózaton maradt.
{{% /details %}}

{{% details title="SMB, WebDAV vagy FTP, melyiket használjam?" closed="true" %}}
Használd az SMB-t, amikor azt szeretnéd, hogy a telefon valódi hálózati meghajtóként viselkedjen egy Macen, egy másik iPhone-on, Linuxon vagy egy NAS-on, és amikor titkosítást szeretnél. Használd a WebDAV-ot, amikor egy olyan hálózati meghajtót szeretnél, amely Windowsról is jól működik. Használd az FTP-t a legszélesebb kompatibilitáshoz régebbi eszközökkel és alkalmazásokkal. Az Everdisk mindegyiket egyszerre futtatja, így nem vagy egyhez kötve.
{{% /details %}}

{{% details title="Ingyenes az Everdisk?" closed="true" %}}
Igen, az Everdisk ingyenesen letölthető és az SMB szerver benne van. Az opcionális egyszeri Premium vásárlás hozzáadja az SMB-titkosítást, az egyéni portokat és néhány más extrát. Az SMB-t fizetés nélkül beállíthatod és megoszthatsz fájlokat.
{{% /details %}}

Készen állsz kipróbálni? [Töltsd le az Everdisket az App Store-ból](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) és körülbelül egy perc alatt nyisd meg az iPhone-odat a Finderben. Kérdés vagy visszajelzés? Írj nekünk a **support@everappz.com** címre.
