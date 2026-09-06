---
title: "Eszközeid csatlakoztatása"
date: 2026-08-20
description: "Lépésről lépésre utasítások az Everdisk vezeték nélküli meghajtódhoz való csatlakozáshoz: nézz tartalmat okostévén DLNA-n keresztül, nyisd meg a fájljaidat bármelyik webböngészőben, csatlakoztasd az eszközödet hálózati meghajtóként a Finderben, a Windowsban vagy a Linuxon WebDAV-on keresztül, csatlakoztass fájlalkalmazásokat FTP-n keresztül, és vigyél át adatot USB-kábelen egy Macre Wi-Fi nélkül."
keywords: ["csatlakozás Everdiskhez", "streamelés TV-re DLNA", "fájlok megnyitása böngészőben", "hálózati meghajtó csatlakoztatása Finder", "WebDAV Windows Linux", "FTP fájlalkalmazás", "USB-kábeles átvitel Mac", "iPhone csatlakoztatása számítógéphez", "hálózati meghajtó iPhone"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


Miután megérinted a **Start** gombot a [Megosztás](/docs/guide/everdisk/everdisk-guide-sharing) képernyőn, a többi eszköz négy különböző módon csatlakozhat a fájljaidhoz. Válaszd azt a módszert, amely megfelel a használni kívánt eszköznek. Minden esetben a szükséges pontos **címet** a Megosztás képernyő **Hogyan csatlakozz** szakaszában találod.

> Mindkét eszköznek **ugyanazon a Wi-Fi hálózaton** kell lennie - vagy Mac esetén **USB-kábellel** csatlakoztatva (lásd az utolsó szakaszt).

## Nézz tartalmat TV-n (DLNA)

Ezt akkor használd, ha fotókat, videókat és zenét szeretnél megjeleníteni egy okostévén vagy médialejátszón.

1. A **Beállítások → Megosztás → Kapcsolatok** menüben győződj meg róla, hogy a **TV és médiaközpont** be van kapcsolva (alapértelmezés szerint be van).
2. A Megosztás képernyőn érintsd meg a **Start** gombot.
3. A TV-n nyisd meg a beépített médialejátszót vagy médiakiszolgáló-alkalmazást (ennek neve lehet Media Player, SmartShare, AllShare vagy hasonló).
4. Az eszközöd a nevével (például "Speedy-Hare") jelenik meg a médiakiszolgálók listájában. Válaszd ki.
5. Böngéssz a megosztott fotóid, videóid és zenéid között, és indítsd el a lejátszást. Az előnézeti bélyegképek automatikusan megjelennek.

Megjegyzések:

- A DLNA nem védhető jelszóval, így ez a kapcsolat mindenki számára nyitva áll ugyanazon a Wi-Fi hálózaton, amíg be van kapcsolva.
- Ha egy videó nem játszható le egy régebbi TV-n, csökkentsd a videó minőségét a **Beállítások → Megosztás → Videók** menüben, hogy az Everdisk kompatibilisebb formátumba alakítsa.

## Nyisd meg webböngészőben (HTTP)

Ezt akkor használd, ha bárkinek át szeretnél adni fájlokat, akinek van webböngészője - nincs telepítendő alkalmazás.

1. A **Beállítások → Megosztás → Kapcsolatok** menüben győződj meg róla, hogy a **Böngésző** be van kapcsolva.
2. Érintsd meg a **Start** gombot.
3. A Megosztás képernyőn másold ki a **Böngésző** címet (vagy jelenítsd meg a QR-kódját).
4. A másik telefonon, tableten vagy számítógépen nyiss meg bármilyen webböngészőt (Safari, Chrome, Edge, Firefox), és írd be azt a címet.
5. Megnyílik az oldal a megosztott fájljaiddal.

A böngészőben a másik fél a következőket teheti:

- Válthat a **lista** és a **rács** nézet között, és rendezhet név, dátum vagy méret szerint.
- Valódi **bélyegképeket** láthat fotókhoz, videókhoz, PDF-ekhez és zenei borítókhoz.
- Megnyithat egy fotót teljes képernyős **galériában** húzással, csippentéses nagyítással és diavetítéssel.
- Zenét játszhat le egy beépített **lejátszóban** lejátszási sorral, keveréssel és ismétléssel.
- **Letölthet** bármelyik fájlt, vagy letölthet egy egész mappát (vagy több kiválasztott elemet) egyetlen **Archive.zip** fájlként.
- **Feltölthet** fájlokat vissza az eszközödre - de csak akkor, ha bekapcsoltad a **Fájlszerkesztés** funkciót (lásd [Hozzáférés és adatvédelem](/docs/guide/everdisk/everdisk-guide-access)).

## Használd hálózati meghajtóként (WebDAV)

Ezt akkor használd, ha azt szeretnéd, hogy az eszközöd megszokott lemezként jelenjen meg egy Macen, Windows PC-n vagy Linux gépen, így mindkét irányban áthúzhatod a fájlokat.

**Macen (Finder)**

1. A **Beállítások → Megosztás → Kapcsolatok** menüben győződj meg róla, hogy a **Számítógép** be van kapcsolva.
2. Érintsd meg a **Start** gombot, és jegyezd meg a **Számítógép (WebDAV)** címet.
3. A Finderben válaszd a **Ugrás → Csatlakozás kiszolgálóhoz** lehetőséget (vagy nyomd meg a **⌘K** billentyűkombinációt).
4. Írd be a WebDAV-címet pontosan úgy, ahogy megjelenik, majd kattints a **Csatlakozás** gombra.
5. Add meg a bejelentkezési nevet és jelszót, ha beállítottál ilyet, egyébként csatlakozz vendégként.
6. Az eszközöd megnyílik, mint bármely más hálózati meghajtó. Húzz be vagy ki fájlokat.

**Windowson**

1. Nyisd meg a **Fájlkezelőt**, kattints jobb gombbal az **Ez a gép** elemre, és válaszd a **Hálózati hely hozzáadása** lehetőséget (vagy csatlakoztass egy hálózati meghajtót).
2. Add meg az Everdiskben megjelenített WebDAV-címet.
3. Add meg a bejelentkezési nevet és jelszót, ha beállítottál ilyet.

**Linuxon**

1. Nyisd meg a fájlkezelődet, és válaszd a **Csatlakozás kiszolgálóhoz** lehetőséget (vagy használd a `davs://` / `dav://` előtagot).
2. Add meg az Everdiskben megjelenített WebDAV-címet.

Az, hogy a kapcsolat csak olvasható vagy kétirányú, a **Fájlszerkesztés** beállítástól függ. Bekapcsolva fájlokat másolhatsz az eszközödre, valamint átnevezheted és törölheted azokat; kikapcsolva a meghajtó csak olvasható.

## Csatlakoztass egy fájlalkalmazást (FTP)

Ezt azokhoz a fájlkezelő és átviteli alkalmazásokhoz használd, amelyek FTP-t használnak (például a FileZilla vagy a Cyberduck egy számítógépen).

1. A **Beállítások → Megosztás → Kapcsolatok** menüben győződj meg róla, hogy a **Más alkalmazások és eszközök** be van kapcsolva.
2. Érintsd meg a **Start** gombot, és jegyezd meg az **FTP**-címet.
3. Az FTP-alkalmazásodban adj hozzá egy új kapcsolatot ezzel a címmel.
4. Add meg a bejelentkezési nevet és jelszót, ha beállítottál ilyet, vagy hagyd üresen az anonim hozzáféréshez.

## Vigyél át adatot USB-kábelen (Mac, Wi-Fi nem szükséges)

Ezt akkor használd, ha nincs Wi-Fi, vagy ha a leggyorsabb és legbiztonságosabb átvitelt szeretnéd. Csak **Mac**kel működik.

1. Csatlakoztasd az iPhone-odat vagy iPad-edet a Machez a szokásos töltőkábellel.
2. Ha az eszköz rákérdez, érintsd meg a **Megbízom ebben a számítógépben** lehetőséget.
3. Az Everdiskben érintsd meg a **Start** gombot. Megjelenik egy **Gyors kapcsolat érhető el** üzenet, és a Megosztás képernyő egy további címet mutat **Kábeles kapcsolat** jelzéssel, amely `.local` végződésű.
4. A Macen nyisd meg a Findert → **Ugrás → Csatlakozás kiszolgálóhoz** (**⌘K**), és add meg azt a `.local` címet (ez működik mind a Böngésző, mind a Számítógép kapcsolathoz).
5. Az eszközöd megnyílik a kábelen keresztül - gyorsabban, mint Wi-Fi-n, és az adat soha nem érinti a routert vagy az internetet.

Megjegyzések:

- A **`.local` nevet** használd, ne IP-címet (az IP-címek csak Wi-Fi-n keresztül működnek), és soha ne a `localhost`-ot.
- A kábeles út **csak Machez** működik. A Windows PC-knek és Android-eszközöknek Wi-Fi-t kell használniuk.
- Fájlokat az Everdisk mappájába is behúzhatsz a Finder segítségével egy Macen, vagy az Apple Devices alkalmazással (illetve az iTunes-szal) Windowson, a szabványos iOS fájlmegosztáson keresztül.

## Következő lépések

- [Hozzáférés és adatvédelem](/docs/guide/everdisk/everdisk-guide-access) - adj hozzá jelszót, engedélyezd a feltöltéseket, blokkolj egy eszközt.
- [Fotók, zene és videó](/docs/guide/everdisk/everdisk-guide-media) - oszd meg a teljes gyűjteményedet, és állítsd be a minőséget.
- [Csatlakozás kiszolgálókhoz](/docs/guide/everdisk/everdisk-guide-devices) - érd el a többi eszközt az Everdiskből.
