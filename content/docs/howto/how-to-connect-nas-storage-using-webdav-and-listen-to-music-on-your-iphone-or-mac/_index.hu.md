---
title: "Hogyan csatlakoztasd a NAS tárolót WebDAV segítségével és hallgass zenét iPhone-on vagy Macen"
date: 2024-07-28
description: "Tanuld meg, hogyan konfigurálhatod a WebDAV-ot a Synology NAS-odon, és hogyan streamelhetsz zenét iPhone-ra vagy Macre az Evermusic vagy a Flacbox segítségével. Kövesd lépésről lépésre szóló útmutatónkat."
keywords: ["nas csatlakoztatás", "webdav synology", "zene streamelés nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["zene", "streamelés", "tárolás", "nas", "csatlakoztatás", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Röviden:** Telepítsd és engedélyezd a WebDAV-ot a Synology NAS-odon, konfiguráld a megosztott mappa jogosultságait, majd csatlakozz az Evermusic vagy Flacbox alkalmazásból a NAS IP-címe és a WebDAV port (alapértelmezett 5005/5006) használatával. Az egész zenei könyvtáradat streamelheted és kezelheted anélkül, hogy fájlokat másolnál az eszközödre.

Fedezd fel, hogyan csatlakoztathatod a NAS tárolódat WebDAV segítségével, és hogyan streamelheted könnyedén a zenei könyvtáradat iPhone-ra vagy Macre. A WebDAV (Web-based Distributed Authoring and Versioning) egy protokoll, amely lehetővé teszi fájlok kezelését és megosztását az interneten keresztül. A WebDAV beállításával a NAS-odon hozzáférhetsz a zenei gyűjteményedhez és streamelheted azt, biztosítva, hogy kedvenc dalaid mindig kéznél legyenek.

Ebben az útmutatóban megmutatjuk, hogyan állíthatsz be WebDAV kapcsolatot az egyik legnépszerűbb NAS szerveren, a Synology NAS-on. Kövesd egyszerű lépéseinket a WebDAV konfigurálásához a Synology NAS-odon, és böngészheted, streamelheted és kezelheted a zenei könyvtáradat közvetlenül iPhone-ról vagy Macről.

## 1. lépés: WebDAV telepítése a Synology NAS-ra

1. Jelentkezz be a Synology NAS-odra és nyisd meg a **Csomagközpontot**.
2. Keresd meg a "webdav" kifejezést, és telepítsd a WebDAV csomagot, ha még nincs telepítve. Nyisd meg a WebDAV szervert a konfiguráláshoz.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="WebDAV telepítése a Synologyra" width="600" >}}

## 2. lépés: WebDAV szerver konfigurálása

1. A WebDAV beállítások oldalán jelöld be a **HTTP engedélyezése**, **HTTPS engedélyezése**, **Anonim WebDAV engedélyezése** és **DavDepthInfinity engedélyezése** jelölőnégyzeteket.
2. Kattints az **Alkalmaz** gombra a módosítások mentéséhez. Jegyezd fel a HTTP és HTTPS kapcsolatok portszámait, amelyek alapértelmezés szerint 5005 és 5006.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="WebDAV beállítások konfigurálása" width="600" >}}

## 3. lépés: Megosztott mappa jogosultságainak konfigurálása

1. Nyisd meg a **Vezérlőpultot** és lépj a **Megosztott mappa** részhez.
2. Válaszd ki a **Zene** mappát és kattints a **Szerkesztés** gombra.
3. A **Jogosultságok** fülön konfiguráld a jogosultságokat. Engedélyezd a vendég hozzáférést Csak olvasás jogosultsággal, ha csak zenét szeretnél hallgatni, vagy Olvasás/Írás jogosultsággal, ha fájlokat kell módosítanod. Mentsd a módosításokat.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Megosztott mappa jogosultságai" width="600" >}}

## 4. lépés: Synology NAS IP-címének megkeresése

1. Nyisd meg a **Vezérlőpultot** és lépj a **Hálózati interfész** fülre, vagy használd a webböngészőt a [find.synology.com](http://find.synology.com) meglátogatásához.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="NAS IP-cím megkeresése" width="600" >}}

2. Jegyezd fel a Synology NAS IP-címét (pl. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP-cím" width="600" >}}

## 5. lépés: Csatlakozás a Synology NAS-hoz Evermusic/Flacbox segítségével

1. Nyisd meg az Evermusic vagy Flacbox alkalmazást és lépj a **Kapcsolatok** fülre.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Kapcsolatok fül az Evermusicban" width="600" >}}

2. Automatikus csatlakozáshoz keresd meg a Synology NAS-t az **Elérhető eszközök** részben, és érintsd meg a csatlakozáshoz.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Elérhető eszközök listája" width="600" >}}

3. Manuális csatlakozáshoz válaszd a **Felhőszolgáltatás csatlakoztatása** lehetőséget és válaszd a **WebDAV** opciót. Add meg a szerver címét a következő formátumban: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (pl. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Manuális WebDAV konfiguráció" width="600" >}}

4. Vendég hozzáféréshez hagyd üresen a bejelentkezési és jelszó mezőket, vagy add meg a Synology hitelesítő adataidat. Érintsd meg a **Bejelentkezés** gombot.

## 6. lépés: Navigálás és zenelejátszás

1. A csatlakozás után az eszköz megjelenik a **Csatlakoztatott kiegészítők** listájában.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Csatlakoztatott eszközök az Evermusicban" width="600" >}}

2. Navigálj a **Zene** mappához és érintsd meg bármelyik hangfájlt a lejátszás indításához.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Zene mappa böngészése" width="600" >}}

## 7. lépés: Csatlakoztatott felhőmappa hozzáadása a zenei könyvtárhoz

1. Nyisd meg a **Zenei könyvtár** részt az alkalmazásban.
2. Válaszd a **Zene hozzáadása** lehetőséget és válaszd a **Kapcsolatok** opciót.
3. Válaszd ki a csatlakoztatott NAS szervert és válaszd a **Zene** mappát. Érintsd meg a **Kész** gombot.
4. Az alkalmazás átvizsgálja a zene mappát és hozzáadja a támogatott hangfájlokat a zenei könyvtárhoz. A metaadatok betöltődnek, és a számaid album, előadó és műfaj szerint csoportosítva jelennek meg.

## Összefoglalás

Ezeket a lépéseket követve könnyedén beállíthatsz egy WebDAV kapcsolatot a Synology NAS-odon, és streamelheted a zenei könyvtáradat iPhone-ra vagy Macre az Evermusic vagy Flacbox segítségével. Élvezd a zökkenőmentes hozzáférést kedvenc dalaidhoz bármikor.

## GYIK

{{% details title="Mely NAS eszközök támogatják a WebDAV-ot?" closed="true" %}}
A legtöbb népszerű NAS márka támogatja a WebDAV-ot, beleértve a Synology, QNAP, TrueNAS és Western Digital márkákat. Ellenőrizd a NAS gyártójának dokumentációját a WebDAV beállítási utasításokért.
{{% /details %}}

{{% details title="Mi a különbség a WebDAV és az SMB között a NAS zenestreameléshez?" closed="true" %}}
A WebDAV HTTP/HTTPS-en keresztül működik, és jobban alkalmas az interneten keresztüli távoli hozzáférésre. Az SMB általában gyorsabb helyi hálózatokon. Az Evermusic és a Flacbox mindkét protokollt támogatja, tehát válassz aszerint, hogy helyi vagy távoli hozzáférésre van szükséged.
{{% /details %}}

{{% details title="Szükségem van felhasználónévre és jelszóra a WebDAV-hoz a Synologyn?" closed="true" %}}
Nem, ha engedélyezed az anonim WebDAV hozzáférést és konfiguráltad a vendég jogosultságokat a megosztott mappán. Jobb biztonság érdekében használhatod a Synology hitelesítő adataidat.
{{% /details %}}

{{% details title="Streamelhetek FLAC-ot és más nagy felbontású formátumokat NAS-ról WebDAV-on keresztül?" closed="true" %}}
Igen. Mind az Evermusic, mind a Flacbox támogatja a FLAC, ALAC, WAV, DSD és más nagy felbontású formátumokat NAS tárolóról WebDAV-on keresztüli streamelés esetén.
{{% /details %}}

{{% details title="Miért nem találja az alkalmazás a NAS-omat az Elérhető eszközökben?" closed="true" %}}
Győződj meg róla, hogy az iPhone/Mac és a NAS ugyanazon a Wi-Fi hálózaton van. Ha az automatikus felderítés nem működik, használd a manuális csatlakozás opciót, és add meg közvetlenül a NAS IP-címét és a WebDAV portot.
{{% /details %}}
