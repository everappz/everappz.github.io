---
title: "Megosztás"
date: 2026-08-20
description: "Ismerd meg, hogyan működik a megosztás az Everdiskben: érintsd meg a Start gombot, hogy vezeték nélküli meghajtóvá alakítsd az iPhone-odat vagy iPad-edet, válaszd ki, mit osztasz meg (fájlokat, mappákat, fotókat és zenét), futtasd a négy kiszolgálót (DLNA, HTTP, WebDAV, FTP), olvasd le a csatlakozási címeket, nézd meg, ki csatlakozott, és tartsd folyamatosan a megosztást Wi-Fi-n vagy USB-kábelen keresztül."
keywords: ["Everdisk megosztás", "vezeték nélküli meghajtó iPhone", "megosztás indítása", "fájlok megosztása iPhone", "fotók megosztása hálózaton", "DLNA HTTP WebDAV FTP", "mit osszak meg", "hogyan csatlakozzak", "tartsd nyitva az alkalmazást", "megosztás Wi-Fi-n vagy USB-kábelen"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


A **Megosztás** fül az Everdisk szíve. Itt alakítod vezeték nélküli meghajtóvá az iPhone-odat vagy iPad-edet, itt választod ki pontosan, mit szeretnél megosztani, és itt kapod meg a címeket, amelyekkel a többi eszköz csatlakozik. Ez az első fül, amit az alkalmazás megnyitásakor látsz.

## A megosztás elindítása és leállítása

A Megosztás képernyő közepén egy nagy, kerek gomb található.

- Érintsd meg a **Start** gombot, hogy az összes engedélyezett kiszolgálót egyszerre online állapotba hozd. A gombon előbb a **Indítás...**, majd a megosztás elindulása után a **Stop** felirat jelenik meg.
- Érintsd meg a **Stop** gombot, hogy mindent újra offline állapotba hozz. A csatlakozott eszközök kapcsolata megszakad.

Amíg a megosztás fut, az általad kiválasztott fájlok, fotók és zenék elérhetők az azonos hálózaton lévő bármely eszközről, amely az alábbi négy módszer valamelyikével csatlakozik.

> A megosztás csak addig működik, amíg az alkalmazás nyitva van. Nézd meg az **Tartsd nyitva az alkalmazást** részt a lap vége felé, hogy megtudd, miért van így, és hogyan tarthatod folyamatban a nagy adatátviteleket.

## Válaszd ki, mit osztasz meg

Mielőtt elindítanád, érintsd meg a **Mit osztasz meg** fejlécet, hogy megnyisd a három csoportot. Ezek bármilyen keverékét megoszthatod, de legalább egy dolgot ki kell választanod, mielőtt a megosztás elindulhat.

**Fájlok és mappák**

- Az alkalmazás saját **Dokumentumok** mappája alapértelmezés szerint meg van osztva. Ha szeretnéd, leállíthatod a megosztását.
- Érintsd meg a **Mappa hozzáadása** gombot, hogy megossz egy mappát az eszközöd bármely részéről, vagy a **Fájl hozzáadása** gombot egyes fájlok megosztásához.
- Minden megosztott elemhez tartozik egy **Info** és egy **Megosztás leállítása** gomb.

**Fotók és videók**

- Kapcsold be a **Hozzáférés engedélyezése a teljes Fotók könyvtárhoz** lehetőséget a teljes fotó- és videógyűjteményed megosztásához, vagy
- érintsd meg a **Fotók hozzáadása** gombot, hogy egyesével válaszd ki, mely fotókat és videókat szeretnéd megosztani.

**Zene**

- Kapcsold be a **Hozzáférés engedélyezése a teljes Zene könyvtárhoz** lehetőséget a teljes zenegyűjteményed megosztásához, vagy
- érintsd meg a **Számok hozzáadása** gombot, hogy csak a kiválasztott dalokat osszd meg.
- A védett (DRM) számokat, illetve a csak a felhőben tárolt számokat nem lehet megosztani.

Ha úgy próbálod elindítani, hogy semmit sem választottál ki, az Everdisk egy **Nincs mit megosztani** üzenetet jelenít meg. Ha megosztás közben módosítod, mit osztasz meg, **állítsd le, majd indítsd újra** a megosztást a változtatás érvényesítéséhez.

## A négy kiszolgáló

Az Everdisk ugyanazt a tartalmat egyszerre négyféleképpen osztja meg. Mindegyik más-más típusú eszközhöz készült, és mindegyik ki- vagy bekapcsolható a **Beállítások → Megosztás → Kapcsolatok** menüben. Alapértelmezés szerint mind a négy be van kapcsolva.

- **TV és médiaközpont (DLNA)** - okostévékhez és médialejátszókhoz. Ezek maguktól felfedezik az eszközödet, és megjelenítik a fotóidat, videóidat és zenéidet, előnézeti bélyegképekkel.
- **Böngésző (HTTP)** - bármilyen telefonhoz, tablethez vagy számítógéphez. A másik fél egy webböngészőben megnyit egy hivatkozást, hogy böngéssze és letöltse a fájljaidat. Semmit sem kell telepíteni.
- **Számítógép (WebDAV)** - egy Machez, Windows PC-hez vagy Linux géphez. Az eszközöd megszokott hálózati meghajtóként jelenik meg, így mindkét irányban áthúzhatod a fájlokat.
- **Más alkalmazások és eszközök (FTP)** - azoknak a fájlalkalmazásoknak és haladó felhasználóknak, akik FTP-t használnak.

Az egyes típusokhoz tartozó lépésről lépésre haladó csatlakozási útmutatóért lásd az [Eszközeid csatlakoztatása](/docs/guide/everdisk/everdisk-guide-connect) oldalt.

## Hogyan csatlakozz és a csatlakozási címek

Miután megérintetted a Start gombot, a **Hogyan csatlakozz** szakasz minden aktív kiszolgálóhoz megjelenít egy kártyát a pontos **címmel**, amelyet a másik eszközön be kell írnod. Minden cím könnyen másolható - érintsd meg a másoláshoz, használd a **Megosztás** gombot az elküldéséhez, vagy érintsd meg az **info (ⓘ)** gombot a részletes, protokollonkénti utasításokért.

- A DLNA-kártya egy eszközleíró címet mutat, amely `/device-desc.xml` végződésű, azoknak a lejátszóknak, amelyek ezt kérik.
- Amikor az eszközöd kábellel csatlakozik egy Machez, egy további cím jelenik meg **Kábeles kapcsolat** jelzéssel, amely az eszközöd `.local` nevét használja.

A címet **QR-kódként** is megnyithatod, így egy másik eszköz kamerája egyből rá tud ugrani.

## Ki csatlakozott

A **Ki csatlakozott** szakasz valós időben listázza a hozzád jelenleg kapcsolódó eszközöket. Érintsd meg a további műveletek gombot bármelyik eszköz mellett, hogy **Blokkold ezt az eszközt**, ha nem ismered fel. A blokkolt eszközöket a [Hozzáférés és adatvédelem](/docs/guide/everdisk/everdisk-guide-access) oldalon kezelheted.

## Az eszközneved és avatarod

Minden eszköznek van egy barátságos neve (például "Speedy-Hare") és egy színes avatarja. Ezt a nevet mutatja egy TV, számítógép vagy más alkalmazás az eszközödről a hálózaton, így könnyű felismerni. A nevet és az avatart ingyen újragenerálhatod, vagy Premiummal egyéni nevet, ikont vagy fotóavatart állíthatsz be. Lásd a [Beállítások](/docs/guide/everdisk/everdisk-guide-settings) oldalt.

## Megosztás Wi-Fi-n vagy USB-kábelen

A megosztás két helyzetben futhat:

- **Wi-Fi-n keresztül** - az eszközöd és a többi eszköz ugyanazon a Wi-Fi hálózaton van.
- **USB-kábelen keresztül** - az eszközöd kábellel csatlakozik egy **Machez**, még akkor is, ha egyáltalán nincs Wi-Fi. Ez gyorsabb a Wi-Fi-nél, és működik repülőn, szállodában vagy zárt hálózaton is.

Ha sem Wi-Fi, sem kábel nem áll rendelkezésre, a **Start** gomb inaktív lesz, és egy **Nincs Wi-Fi kapcsolat** üzenet jelenik meg. Ha a kapcsolat megszakad megosztás közben, az Everdisk automatikusan leállítja a megosztást, és értesít róla. Érintsd meg az info gombot bármelyik ilyen üzeneten a teljes magyarázatért.

## Tartsd nyitva az alkalmazást

Mivel az iPhone-od vagy iPad-ed a kiszolgáló szerepét tölti be, **a megosztás csak addig működik, amíg az Everdisk nyitva van a képernyőn**. Ha bezárod az alkalmazást vagy hosszabb időre lezárod az eszközt, a rendszer felfüggesztheti az alkalmazást, és a megosztás leáll.

Nagy adatátvitelekhez:

- Tartsd az Everdisket nyitva és előtérben.
- Csatlakoztasd az eszközödet a töltőhöz.
- Az adatátvitel idejére állítsd az **Automatikus zárolás** beállítást **Soha** értékre az iOS Beállítások alkalmazásban.

Bekapcsolhatod a **Figyelmeztetés a lecsatlakozás előtt** lehetőséget (a Beállítások → Megosztás menüben), így az Everdisk emlékeztet, hogy nyisd meg újra az alkalmazást, mielőtt a rendszer felfüggeszti. Érintsd meg az info gombot a **Tartsd nyitva az alkalmazást** bannerén a további részletekért.

## Következő lépések

- [Eszközeid csatlakoztatása](/docs/guide/everdisk/everdisk-guide-connect) - csatlakoztass egy TV-t, számítógépet, böngészőt, telefont vagy USB-kábelt.
- [Hozzáférés és adatvédelem](/docs/guide/everdisk/everdisk-guide-access) - adj hozzá jelszót, és szabályozd a szerkesztést.
- [Beállítások](/docs/guide/everdisk/everdisk-guide-settings) - kapcsold be vagy ki a kiszolgálókat, és hangold a minőséget.
