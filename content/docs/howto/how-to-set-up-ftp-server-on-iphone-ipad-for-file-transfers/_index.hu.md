---
title: "Hogyan állíts be FTP szervert iPhone-on és iPad-en fájlátvitelhez"
description: "Alakítsd iPhone-odat vagy iPad-edet FTP szerverré az Everdiskkel, és vigyél át fájlokat egy Macről, Windows PC-ről, Linuxról, Androidról, egy FTP-alkalmazásból, mint a FileZilla, vagy egy másik iPhone-ról Wi-Fi felett. Teljes beállítás, az ftp-cím és a port, vendéghozzáférés, és lépésről lépésre csatlakozás minden eszközhöz."
date: 2026-09-19
tags: ["everdisk", "ftp", "fájlátvitel", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP szerver iPhone", "FTP szerver iPad", "hogyan állíts be FTP-t iPhone-on", "iphone ftp szerver alkalmazás", "FileZilla csatlakoztatása iPhone-hoz", "Cyberduck iPhone FTP", "fájlátvitel iPhone FTP", "ftp iphone-ról számítógépre", "ftp iphone-ról iphone-ra", "csatlakozás iPhone FTP-hez Windowsról", "ftp cím port iphone", "névtelen ftp iphone", "fájlok megosztása iphone ftp", "iphone ftp kamerához nas-hoz"]
readingTime: 9
---

{{< author-byline >}}

Az FTP a fájlátvitel régi megbízható eszköze. Évtizedek óta létezik, éppen ezért annyira hasznos: szinte minden, ami képes egy szerverrel kommunikálni, érti. A kamerák, a smart TV-k, a routerek, a hálózati meghajtók, az automatizálási eszközök és minden asztali FTP-alkalmazás beszéli az FTP-t. Az [Everdisk](/products/everdisk) segítségével FTP szervert futtathatsz az iPhone-odon vagy iPad-eden, így a telefon olyan hellyé válik, amelyhez ezek az eszközök és alkalmazások csatlakozhatnak és fájlokat mozgathatnak.

Akkor nyúlj az FTP-hez, amikor a többi lehetőség nem illik, például egy régebbi eszköznél vagy egy olyan alkalmazásnál, amely csak FTP felett tud csatlakozni. Ez az útmutató a beállítást és a Macről, Windowsról, egy FTP-alkalmazásból, Linuxról, Androidról és egy második iPhone-ról való csatlakozást ismerteti.

## Mire lesz szükséged

- Egy iPhone vagy iPad telepített [Everdiskkel](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Egy számítógép, alkalmazás vagy eszköz **ugyanazon a Wi-Fi hálózaton**.
- A fájlok, amelyeket meg szeretnél osztani, az Everdisk Dokumentumok mappájában vagy az általad hozzáadott mappákban.

## Az FTP szerver beállítása az Everdiskben

### 1. lépés: Válaszd ki, mit oszd meg és állítsd be a hozzáférést

Nyisd meg az Everdisket, lépj a **Megosztás** fülre, és érintsd meg a **Mit oszd meg** lehetőséget. A Dokumentumok mappa alapból meg van osztva. Adj hozzá többet a **Mappa hozzáadása** és **Fájl hozzáadása** gombokkal.

Nyisd meg a **Beállítások**, majd a **Megosztás**, majd a **Hozzáférés** menüt. Kapcsold be a **Fájlszerkesztés** lehetőséget, ha azt szeretnéd, hogy az emberek feltölthessenek, átnevezhessenek és törölhessenek, vagy kapcsold ki, hogy csak letöltést engedélyezz. Állíts be egy **Felhasználónevet** és **Jelszót**, ha bejelentkezést szeretnél, vagy hagyd őket üresen, hogy bárki vendégként csatlakozhasson.

### 2. lépés: Kapcsold be az FTP szervert

Lépj a **Beállítások**, majd a **Megosztás**, majd a **Kapcsolatok** menübe, és kapcsold be a **Más appok és eszközök** lehetőséget. Ez az FTP szerver (az FTP címkét viseli).

### 3. lépés: Indítsd el a megosztást és jegyezd fel a címet

Térj vissza a **Megosztás** fülre és érintsd meg a **Start** gombot. A **Hogyan csatlakozz** szakasz mutatja az FTP-címet. Így néz ki:

```
ftp://192.168.1.20:2121
```

A kettőspont utáni szám a **port**, amely alapból **2121**. Az első rész az iPhone-od Wi-Fi-címe, így a tiéd más lesz. Tartsd nyitva az Everdisket a képernyőn, amíg egy eszköz csatlakozik.

## Csatlakozás egy Macről

1. Nyisd meg a **Findert**, válaszd a **Go**, majd a **Connect to Server** menüpontot (vagy nyomd meg a **Command és K** billentyűket).
2. Írd be az Everdiskben megjelenő FTP-címet, például `ftp://192.168.1.20:2121`.
3. Kattints a **Connect** gombra, majd válaszd a **Guest** lehetőséget, vagy add meg a **Felhasználónevedet** és **Jelszavadat**.

A Finder csatlakoztatja az FTP-megosztást, így böngészhetsz és fájlokat másolhatsz a Macedre. Vedd figyelembe, hogy a Finder az FTP-t csak olvashatóként nyitja meg. Amikor egy Macről szeretnél feltölteni, használj egy FTP-alkalmazást az alábbiak szerint.

## Csatlakozás Windowsról

1. Nyisd meg a **Fájlkezelőt** és kattints a címsorra fent.
2. Írd be az Everdiskből származó FTP-címet, például `ftp://192.168.1.20:2121`, és nyomd meg az **Enter** billentyűt.
3. Add meg a **Felhasználónevedet** és **Jelszavadat**, ha beállítottál egyet, vagy folytasd vendégként.

A megosztott fájlok megjelennek az ablakban, és átmásolhatod őket a PC-dre.

## Csatlakozás egy FTP-alkalmazással (FileZilla, Cyberduck)

Feltöltésekhez és teljes körű vezérléshez egy FTP-alkalmazás a legjobb eszköz. A **FileZilla** és a **Cyberduck** ingyenes, és Windowson, Macen és Linuxon fut.

1. Nyisd meg az alkalmazást és hozz létre egy új kapcsolatot.
2. Állítsd be a **Host** mezőt az iPhone-od Wi-Fi-címére, a **Port** mezőt pedig **2121**-re.
3. A bejelentkezéshez add meg a **Felhasználónevedet** és **Jelszavadat**, vagy válaszd az **Anonymous** lehetőséget, ha nem állítottál be egyet.
4. Csatlakozz, és húzz fájlokat mindkét irányba (a feltöltésekhez be kell kapcsolni a Fájlszerkesztést).

## Csatlakozás Linuxról

1. Nyisd meg a fájlkezelődet és válaszd a **Connect to Server** vagy az **Other Locations** lehetőséget.
2. Add meg a címet, például `ftp://192.168.1.20:2121`.
3. Csatlakozz vendégként vagy a bejelentkezéseddel.

Bármely Linux FTP-klienst is használhatsz a terminálból, ugyanarra a hosztra és a 2121-es portra irányítva.

## Csatlakozás Androidról

Az Androidon nincs rendszerszintű FTP-böngésző, ezért használj egy alkalmazást:

1. Telepíts egy FTP-klienst, mint az **AndFTP**, az **FTPCafe**, vagy egy FTP-támogatással rendelkező fájlkezelőt, mint a **Solid Explorer**.
2. Adj hozzá egy kapcsolatot a hoszttal, a **2121-es porttal**, és a bejelentkezéseddel vagy az Anonymous lehetőséggel.
3. Böngéssz és vigyél át fájlokat.

## Csatlakozás egy másik iPhone-ról vagy iPad-ről

Az iOS Fájlok appja nem tartalmaz FTP-klienst, ezért használd ezek egyikét a második készüléken:

- **Az Everdisk saját Eszközök füle.** Nyisd meg az Everdisket, lépj az **Eszközök** fülre, érintsd meg az **Új kapcsolat** lehetőséget, válaszd az **FTP** lehetőséget, és add meg a címet, például `ftp://192.168.1.20:2121`. Ez a legegyszerűbb út.
- **Egy dedikált FTP-alkalmazás** iOS-re, ugyanazzal a hoszttal, a 2121-es porttal és a bejelentkezéssel.

## Csatlakozás más eszközökhöz: kamerák, TV-k, routerek és NAS

Itt ragyog az FTP. Sok eszközben van beépített FTP-kliens, amely fájlokat tud küldeni vagy lekérni:

- **A kamerák**, amelyek FTP felett töltenek fel fényképeket, egyenesen az iPhone-odra küldhetik őket.
- **A smart TV-k, routerek, NAS-dobozok és automatizálási eszközök**, amelyek támogatják az FTP-t, ugyanígy csatlakozhatnak.

Irányítsd őket az iPhone-od Wi-Fi-címére, a **2121**-es portra, és a bejelentkezésedre (vagy az Anonymous lehetőségre), az Everdiskben megjelenő cím segítségével.

## Csak olvasható vagy olvasható és írható

A **Fájlszerkesztés** kapcsoló a Beállítások, Megosztás, Hozzáférés menüben szabályozza ezt. A bekapcsolt állapot engedi az embereknek a feltöltést, átnevezést és törlést. A kikapcsolt állapot azt jelenti, hogy csak letölthetnek. Válaszd a csak olvashatót, amikor fájlokat adsz ki és nem szeretnéd, hogy bármit módosítsanak a telefonodon.

## Valós helyzetek, ahogy az emberek ezt használják

- **A FileZilla csatlakoztatása az iPhone-odhoz** és egy csomó fájl egyszerre való feltolása a telefonra.
- **Egy régi alkalmazás vagy eszköz, amely csak FTP-t beszél**, elérheti a fájljaidat, amikor semmi más nem csatlakozik.
- **Fényképek fogadása egy kamerából**, amely FTP felett tölt fel.
- **Fájlok áthelyezése egy iPhone és egy iPad között** az Everdisk Eszközök fülével a fogadó készüléken.

## Néhány tipp

- Tartsd nyitva az Everdisket, amíg egy eszköz csatlakozik, mivel az iOS egy idő után szünetelteti a háttéralkalmazásokat.
- Egy Macről való feltöltéshez használd a FileZillát vagy a Cyberduckot a Finder helyett, mert a Finder az FTP-t csak olvashatóként nyitja meg.
- Hagyd a bejelentkezést üresen a legszélesebb kompatibilitáshoz, majd csatlakozz Anonymous módon, amelyet a legtöbb FTP-kliens kínál.
- Az FTP nem titkosítja a forgalmát. Egy nem megbízható hálózaton használd inkább az [SMB szervert titkosítással](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Gyakran ismételt kérdések

{{% details title="Mi az iPhone-om FTP-címe és portja?" closed="true" %}}
Miután elindítod a megosztást, az Everdisk mutatja a címet a Megosztás képernyőn. Így néz ki: ftp://192.168.1.20:2121. A 2121 az a port, amelyet az Everdisk az FTP-hez használ, az első rész pedig az iPhone-od Wi-Fi-címe, így a tiéd más lesz.
{{% /details %}}

{{% details title="Hogyan csatlakoztatom a FileZillát vagy a Cyberduckot az iPhone-omhoz?" closed="true" %}}
Nyisd meg az alkalmazást és hozz létre egy új kapcsolatot. Állítsd be a Host mezőt az iPhone-od Wi-Fi-címére, a Port mezőt pedig 2121-re. Add meg a Felhasználónevedet és Jelszavadat, vagy válaszd az Anonymous lehetőséget, ha nem állítottál be egyet az Everdiskben. Csatlakozz, és mindkét irányba húzhatsz fájlokat, amikor a Fájlszerkesztés be van kapcsolva.
{{% /details %}}

{{% details title="Csatlakozhatok az iPhone-om FTP-jéhez Windowsról?" closed="true" %}}
Igen. Nyisd meg a Fájlkezelőt, kattints a címsorra, írd be az Everdiskből származó FTP-címet (például ftp://192.168.1.20:2121), és nyomd meg az Enter billentyűt. Add meg a bejelentkezésedet, ha beállítottál egyet, vagy folytasd vendégként. Feltöltésekhez és több vezérléshez használj inkább egy FTP-alkalmazást, mint a FileZilla.
{{% /details %}}

{{% details title="Kell bejelentkezés az FTP-hez?" closed="true" %}}
Nem, a bejelentkezés opcionális. Hagyd a Felhasználónevet és a Jelszót üresen a Beállítások, Megosztás, Hozzáférés menüben, és csatlakozz Anonymous módon, amelyet a legtöbb FTP-kliens kínál. Állíts be egy bejelentkezést, ha azt szeretnéd, hogy a kapcsolatok először bejelentkezzenek.
{{% /details %}}

{{% details title="Miért csak letölteni tudok, feltölteni nem FTP felett?" closed="true" %}}
Két gyakori ok van. Először, a Fájlszerkesztés kapcsolónak a Beállítások, Megosztás, Hozzáférés menüben be kell kapcsolva lennie a feltöltések, átnevezések és törlések engedélyezéséhez. Másodszor, a Mac Finder az FTP-t csak olvashatóként nyitja meg, ezért használj egy FTP-alkalmazást, mint a FileZilla vagy a Cyberduck, amikor fel szeretnél tölteni.
{{% /details %}}

{{% details title="Használhatok FTP-t két iPhone között?" closed="true" %}}
Igen. Indítsd el az FTP szervert az első iPhone-on. A másodikon nyisd meg az Everdisket, lépj az Eszközök fülre, érintsd meg az Új kapcsolat lehetőséget, válaszd az FTP lehetőséget, és add meg az első telefonon megjelenő címet. Egy dedikált FTP-alkalmazás iOS-re szintén működik, mivel az iOS Fájlok appja nem tartalmaz FTP-klienst.
{{% /details %}}

{{% details title="Biztonságos az FTP?" closed="true" %}}
A sima FTP nem titkosítja a forgalmát, ezért kezeld olyan hálózatokhoz való eszközként, amelyekben megbízol, mint az otthoni Wi-Fi-d. Egy olyan hálózaton, amelyet nem irányítasz, használd az SMB szervert bekapcsolt SMB-titkosítás megkövetelése lehetőséggel, amely minden átvitelt véd.
{{% /details %}}

{{% details title="Mely eszközök csatlakozhatnak FTP felett?" closed="true" %}}
Szinte minden FTP-klienssel rendelkező eszköz. Ide tartoznak a Mac, Windows és Linux számítógépek, az FTP-alkalmazások, mint a FileZilla és a Cyberduck, az Android fájlkezelők, és a hardverek, mint a kamerák, smart TV-k, routerek, NAS-dobozok és automatizálási eszközök. Ez a széles körű elérhetőség a fő ok az FTP választására.
{{% /details %}}

{{% details title="Miért szakadt meg az FTP kapcsolatom?" closed="true" %}}
Az iPhone-od a szerver, és az iOS szünetelteti a túl sokáig a háttérben maradó alkalmazásokat. Tartsd az Everdisket a képernyőn, amíg egy eszköz csatlakozik, és csatlakoztasd a hálózathoz a hosszú átvitelekhez. Győződj meg arról is, hogy mindkét eszköz még mindig ugyanazon a Wi-Fi hálózaton van.
{{% /details %}}

{{% details title="Ingyenes az Everdisk?" closed="true" %}}
Igen, az Everdisk ingyenesen letölthető és az FTP szerver benne van. Egy opcionális egyszeri Premium vásárlás olyan extrákat ad hozzá, mint az egyéni portok és a fénykép- és videóátalakítás. Az FTP-t fizetés nélkül beállíthatod és átvihetsz fájlokat.
{{% /details %}}

Készen állsz kipróbálni? [Töltsd le az Everdisket az App Store-ból](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) és pár perc alatt csatlakoztasd az első FTP-klienst. Kérdés vagy visszajelzés? Írj nekünk a **support@everappz.com** címre.
