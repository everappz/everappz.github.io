---
title: "Hogyan állíts be WebDAV szervert iPhone-on és iPad-en fájleléréshez és megosztáshoz"
description: "Alakítsd iPhone-odat vagy iPad-edet WebDAV szerverré az Everdiskkel, és csatlakoztasd hálózati meghajtóként a Mac Finderben, a Windows Fájlkezelőben, Linuxon, Androidon vagy egy másik iPhone-on Wi-Fi felett. Teljes beállítás, a WebDAV-cím és a port, és lépésről lépésre csatlakozás minden eszközhöz."
date: 2026-09-19
tags: ["everdisk", "webdav", "hálózati meghajtó", "fájlmegosztás", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV szerver iPhone", "WebDAV szerver iPad", "hogyan állíts be WebDAV-ot iPhone-on", "iphone csatlakoztatása hálózati meghajtóként", "iPhone WebDAV csatlakozás Mac Finder", "WebDAV Windows Fájlkezelő iPhone", "iphone hálózati meghajtó Windows", "WebDAV Linux iPhone", "iPhone fájlok elérése számítógépről", "webdav iphone-ról iphone-ra", "fájlok megosztása iPhone WebDAV", "hálózati meghajtó csatlakoztatása iphone", "fájlátvitel iphone webdav", "webdav cím port iphone"]
readingTime: 9
---

{{< author-byline >}}

A WebDAV egy mappát olyan hálózati meghajtóvá alakít, amelyet egy számítógép meg tud nyitni a normál fájlkezelőjében. Ugyanazon a webprotokollon fut, amelyet a böngésződ használ, ezért jól utazik Mac, Windows és Linux között speciális illesztőprogramok nélkül. Az [Everdisk](/products/everdisk) segítségével WebDAV szervert futtathatsz az iPhone-odon vagy iPad-eden, így a telefon meghajtóként jelenik meg, amelyet böngészhetsz, amelyről másolhatsz, és amelyre másolhatsz szinte bármelyik számítógépről.

A WebDAV a legjobb választás, amikor a Windows is szóba jön, mert a Windows Fájlkezelő tisztán csatlakozik hozzá. Ez az útmutató a beállítást és a Macről, Windowsról, Linuxról, Androidról és egy második iPhone-ról való csatlakozást ismerteti.

## Mire lesz szükséged

- Egy iPhone vagy iPad telepített [Everdiskkel](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Egy számítógép vagy másik eszköz **ugyanazon a Wi-Fi hálózaton**.
- A fájlok, amelyeket meg szeretnél osztani, az Everdisk Dokumentumok mappájában vagy az általad hozzáadott mappákban.

## A WebDAV szerver beállítása az Everdiskben

### 1. lépés: Válaszd ki, mit oszd meg és állítsd be a hozzáférést

Nyisd meg az Everdisket, lépj a **Megosztás** fülre, és érintsd meg a **Mit oszd meg** lehetőséget. A Dokumentumok mappa alapból meg van osztva. Adj hozzá többet a **Mappa hozzáadása** és **Fájl hozzáadása** gombokkal.

Nyisd meg a **Beállítások**, majd a **Megosztás**, majd a **Hozzáférés** menüt. Kapcsold be a **Fájlszerkesztés** lehetőséget, ha azt szeretnéd, hogy a csatlakozó számítógépek fájlokat másolhassanak a telefonodra, valamint átnevezhessenek vagy törölhessenek, vagy kapcsold ki egy csak olvasható meghajtóhoz. Állíts be itt egy **Felhasználónevet** és **Jelszót**, ha bejelentkezést szeretnél, vagy hagyd őket üresen a vendéghozzáféréshez.

### 2. lépés: Kapcsold be a WebDAV szervert

Lépj a **Beállítások**, majd a **Megosztás**, majd a **Kapcsolatok** menübe, és kapcsold be a **Számítógép** lehetőséget. Ez a WebDAV szerver (a WebDAV címkét viseli).

### 3. lépés: Indítsd el a megosztást és jegyezd fel a címet

Térj vissza a **Megosztás** fülre és érintsd meg a **Start** gombot. A **Hogyan csatlakozz** szakasz mutatja a WebDAV-címet. Így néz ki:

```
http://192.168.1.20:8080
```

A kettőspont utáni szám a **port**, amely alapból **8080**. Az első rész az iPhone-od Wi-Fi-címe, így a tiéd más lesz. Tartsd nyitva az Everdisket a képernyőn, amíg egy eszköz csatlakozik.

## Csatlakozás egy Macről

1. Nyisd meg a **Findert**, válaszd a **Go**, majd a **Connect to Server** menüpontot (vagy nyomd meg a **Command és K** billentyűket).
2. Írd be az Everdiskben megjelenő WebDAV-címet, például `http://192.168.1.20:8080`.
3. Kattints a **Connect** gombra, majd válaszd a **Guest** lehetőséget, vagy add meg a **Felhasználónevedet** és **Jelszavadat**.

Az iPhone-od megnyílik egy Finder-ablakban és normál mappaként viselkedik. Másolj fájlokat mindkét irányba, ha a Fájlszerkesztés be van kapcsolva.

## Csatlakozás Windowsról

A Windowsban van beépített WebDAV-kliens, így ez a Fájlkezelőből működik.

1. Nyisd meg a **Fájlkezelőt**, kattints jobb gombbal az **Ez a gép** elemre az oldalsávban, és válaszd a **Hálózati hely hozzáadása** lehetőséget (a **Hálózati meghajtó csatlakoztatása** lehetőséget is használhatod).
2. Amikor a cím után kérdez, írd be ugyanazt a WebDAV-címet az Everdiskből, például `http://192.168.1.20:8080`, majd kattints a **Tovább** gombra.
3. Add meg a **Felhasználónevedet** és **Jelszavadat**, ha beállítottál egyet.

A készülék ekkor megjelenik az Ez a gép alatt hálózati helyként, amelyet megnyithatsz és amelyről fájlokat másolhatsz. Ha a Windows először nem hajlandó csatlakozni, győződj meg róla, hogy a **WebClient** szolgáltatás fut (keresd a Szolgáltatásokat a Start menüben, keresd meg a WebClientet, és állítsd indításra), majd próbáld újra.

## Csatlakozás Linuxról

1. Nyisd meg a fájlkezelődet és válaszd a **Connect to Server** vagy az **Other Locations** lehetőséget.
2. Add meg a címet WebDAV-előtaggal, például `dav://192.168.1.20:8080` (a `davs://` előtagot csak akkor használd, ha beállítottál TLS-t).
3. Csatlakozz vendégként vagy add meg a bejelentkezésedet.

## Csatlakozás Androidról

Az Androidon nincs rendszerszintű WebDAV-böngésző, ezért használj egy azt támogató fájlkezelőt:

1. Telepíts egy alkalmazást, mint a **Solid Explorer** vagy a **CX File Explorer**.
2. Adj hozzá egy új **WebDAV** kapcsolatot.
3. Add meg a hosztot és a **8080-as portot**, válaszd a `http` sémát, és add meg a bejelentkezésedet, ha beállítottál egyet.

## Csatlakozás egy másik iPhone-ról vagy iPad-ről

Az iOS Fájlok appja nem tartalmaz WebDAV-klienst, ezért használd ezek egyikét:

- **Az Everdisk saját Eszközök füle.** A második készüléken nyisd meg az Everdisket, lépj az **Eszközök** fülre, érintsd meg az **Új kapcsolat** lehetőséget, válaszd a **WebDAV** lehetőséget, és add meg a címet, például `http://192.168.1.20:8080`. Ez a legegyszerűbb út és semmi extra nem kell hozzá.
- **Egy WebDAV-alkalmazás**, mint a Documents by Readdle, amely ugyanazzal a címmel és bejelentkezéssel hozzá tud adni egy WebDAV-kapcsolatot.

## Inkább egy gyors linket szeretnél meghajtó helyett?

Ha csak gyorsan meg szeretnél fogni egy fájlt és egyáltalán nem szeretnél meghajtót csatlakoztatni, kapcsold be a **Böngésző** kapcsolatot a Beállítások, Megosztás, Kapcsolatok menüben. Az Everdisk ekkor ad egy webcímet, amelyet bármely eszköz bármely böngészőjében megnyithatsz a fájljaid böngészéséhez és letöltéséhez. Ez a leggyorsabb módszer egy fájl átadására egy Windows PC-nek, egy Chromebooknak vagy egy barát telefonjának.

## Csak olvasható vagy olvasható és írható

A **Fájlszerkesztés** kapcsoló a Beállítások, Megosztás, Hozzáférés menüben dönti el ezt. A bekapcsolt állapot azt jelenti, hogy a csatlakozó számítógépek feltölthetnek, átnevezhetnek és törölhetnek. A kikapcsolt állapot azt jelenti, hogy a meghajtó csak olvasható, így mások megtekinthetik és lemásolhatják a fájljaidat, de nem módosíthatják őket.

## Valós helyzetek, ahogy az emberek ezt használják

- **Fájlok másolása az iPhone-odra egy Windows PC-ről** úgy, hogy hálózati helyként csatlakoztatod és áthúzod őket.
- **Fényképek és dokumentumok áthelyezése egy laptopra** a már ismert fájlkezelővel, kábel és iTunes nélkül.
- **Egy dokumentum helyben szerkesztése** a Macedről, közvetlenül a telefonról megnyitva és visszamentve.
- **Egy mappa áthelyezése egy iPhone és egy iPad között** az Everdisk Eszközök fülével a fogadó készüléken.

## Néhány tipp

- Tartsd nyitva az Everdisket, amíg egy eszköz csatlakozik. A telefon hosszú időre való lezárása szüneteltetheti az alkalmazást.
- Windowson, ha a kapcsolat sikertelen, indítsd el a WebClient szolgáltatást és próbáld újra a címet.
- A WebDAV és az SMB egyaránt hálózati meghajtóként csatlakozik. Használd a WebDAV-ot, amikor Windows is szerepel, és az [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) szervert, amikor Finder-sebességet és titkosítást szeretnél.
- A leggyorsabb átvitelekhez tartsd a fénykép- és videóminőséget Eredetin a Beállításokban.

## Gyakran ismételt kérdések

{{% details title="Mi az iPhone-om WebDAV-címe és portja?" closed="true" %}}
Miután elindítod a megosztást, az Everdisk mutatja a címet a Megosztás képernyőn. Így néz ki: http://192.168.1.20:8080. A 8080 az a port, amelyet az Everdisk a WebDAV-hoz használ, az első rész pedig az iPhone-od Wi-Fi-címe, így a tiéd más lesz.
{{% /details %}}

{{% details title="Hogyan csatlakozom az iPhone-om WebDAV-jához Windowsról?" closed="true" %}}
Nyisd meg a Fájlkezelőt, kattints jobb gombbal az Ez a gép elemre, és válaszd a Hálózati hely hozzáadása vagy a Hálózati meghajtó csatlakoztatása lehetőséget. Add meg az Everdiskből származó WebDAV-címet, például http://192.168.1.20:8080, majd add meg a bejelentkezésedet, ha beállítottál egyet. Ha a Windows nem hajlandó csatlakozni, győződj meg róla, hogy a WebClient szolgáltatás fut (keresd a Szolgáltatásokat, keresd meg a WebClientet, indítsd el) és próbáld újra.
{{% /details %}}

{{% details title="Használhatok WebDAV-ot két iPhone között?" closed="true" %}}
Igen, de az iOS Fájlok appjának nincs WebDAV-kliense, ezért használd az Everdisket a második készüléken. Nyisd meg az Eszközök fület, érintsd meg az Új kapcsolat lehetőséget, válaszd a WebDAV lehetőséget, és add meg az első telefonon megjelenő címet. Egy WebDAV-alkalmazás, mint a Documents by Readdle, szintén működik.
{{% /details %}}

{{% details title="Kell jelszó a WebDAV-hoz?" closed="true" %}}
Nem, a bejelentkezés opcionális. Hagyd a Felhasználónevet és a Jelszót üresen a Beállítások, Megosztás, Hozzáférés menüben a vendéghozzáféréshez, vagy állítsd be őket, ha azt szeretnéd, hogy a kapcsolatok bejelentkezzenek.
{{% /details %}}

{{% details title="Módosíthatják mások a fájljaimat WebDAV felett?" closed="true" %}}
Csak ha megengeded. A Fájlszerkesztés kapcsoló a Beállítások, Megosztás, Hozzáférés menüben szabályozza ezt. A bekapcsolt állapot engedi a csatlakozó eszközöknek a feltöltést, átnevezést és törlést. A kikapcsolt állapot csak olvashatóvá teszi a meghajtót, így mások megtekinthetik és lemásolhatják, de nem módosíthatnak semmit.
{{% /details %}}

{{% details title="WebDAV vagy SMB, mi a különbség?" closed="true" %}}
Mindkettő hálózati meghajtóként csatlakoztatja az iPhone-odat. A WebDAV a webprotokollon fut és tisztán csatlakozik a Windows Fájlkezelőből, ami a fő erőssége. Az SMB a natív fájlmegosztás Macen, Linuxon és NAS-eszközökön, általában gyorsabb egy Macen, és ez az egyetlen Everdisk-kapcsolat, amely titkosítani tudja az átviteleket. Az Everdisk mindkettőt egyszerre futtatja.
{{% /details %}}

{{% details title="Miért szakad meg a WebDAV meghajtóm?" closed="true" %}}
Az iPhone-od a szerver, és az iOS szünetelteti a túl sokáig a háttérben maradó alkalmazásokat. Tartsd az Everdisket a képernyőn, amíg egy eszköz csatlakozik, és csatlakoztasd a hálózathoz a hosszú átvitelekhez. Győződj meg arról is, hogy mindkét eszköz még mindig ugyanazon a Wi-Fi hálózaton van.
{{% /details %}}

{{% details title="Csatlakozhatok WebDAV felett Wi-Fi nélkül?" closed="true" %}}
Igen, ha az iPhone-odat egy Machez csatlakoztatod egy kábellel. Az Everdisk ekkor mutat egy extra kábeles kapcsolat címet, amelyet a csatlakoztatott Mac megnyithat a Finderben, ami Wi-Fi nélkül is működik. A kábelen csak az a Mac éri el a készüléket.
{{% /details %}}

{{% details title="Ingyenes az Everdisk?" closed="true" %}}
Igen, az Everdisk ingyenesen letölthető és a WebDAV szerver benne van. Egy opcionális egyszeri Premium vásárlás olyan extrákat ad hozzá, mint az egyéni portok és a fénykép- és videóátalakítás. A WebDAV-ot fizetés nélkül beállíthatod és megoszthatsz fájlokat.
{{% /details %}}

Készen állsz kipróbálni? [Töltsd le az Everdisket az App Store-ból](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) és pár perc alatt csatlakoztasd az iPhone-odat meghajtóként. Kérdés vagy visszajelzés? Írj nekünk a **support@everappz.com** címre.
