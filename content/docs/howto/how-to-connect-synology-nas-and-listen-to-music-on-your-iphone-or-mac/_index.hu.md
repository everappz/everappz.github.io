---
title: "Hogyan csatlakoztasd a Synology NAS-t és hallgass zenét az iPhone-on vagy Mac-en"
date: 2024-09-19
description: "Ismerd meg, hogyan csatlakoztasd a Synology NAS-t a natív API vagy QuickConnect segítségével, és hogyan streamelj kiváló minőségű zenét az iPhone-ra vagy Mac-re az Evermusic és Flacbox alkalmazásokkal."
keywords: ["synology nas", "zene streamelés", "quickconnect", "evermusic synology", "flacbox synology", "nas zenelejátszó", "iphone nas zene"]
tags: ["zene", "streamelés", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Összefoglaló:** Csatlakoztasd a Synology NAS-t az Evermusic vagy Flacbox alkalmazáshoz a Synology natív API-jával -- akár manuálisan IP-cím, akár automatikusan QuickConnect ID segítségével. A QuickConnect lehetővé teszi a zene távoli streamelését portátirányítás nélkül. Mindkét alkalmazás támogatja a FLAC, MP3, WAV és más hi-res formátumokat.

Ha zökkenőmentes módot keresel a Synology NAS csatlakoztatására és zenei könyvtárad élvezetére az iPhone-on vagy Mac-en, az Evermusic és Flacbox alkalmazások tökéletes megoldást nyújtanak. Ezek az alkalmazások az audioformátumok széles skáláját támogatják, beleértve a FLAC, MP3 és WAV formátumokat, így egyszerűen streamelhetsz és hallgathatsz kiváló minőségű zenét közvetlenül a Synology NAS-ról.

Ebben az útmutatóban megmutatjuk, hogyan csatlakoztasd a Synology NAS-t az Evermusic vagy Flacbox alkalmazáshoz a Synology natív API-ja és a QuickConnect funkció segítségével. A Synology közvetlen API-jának kihasználásával biztonságosan elérheted zenei könyvtáradat az otthoni hálózatodon kívülről, bonyolult konfigurációk, mint a WebDAV, SMB, DLNA nélkül. A QuickConnect segítségével bárhonnan streamelheted és kezelheted zenéidet az iPhone vagy Mac segítségével.

## 1. lépés: Megosztott mappa engedélyeinek beállítása (opcionális)

1. Nyisd meg a **Vezérlőpultot** és lépj a **Megosztott mappa** szakaszba.

![Megosztott mappa](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Válaszd ki a **Zene** mappát és kattints a **Szerkesztés** gombra.

3. Az **Engedélyek** lapon állítsd be az engedélyeket. Engedélyezd a vendég hozzáférést csak olvasási joggal, ha csak zenét szeretnél hallgatni, vagy olvasás/írás joggal, ha fájlokat kell módosítanod. Mentsd el a változtatásokat.

![Engedélyek](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## 2. lépés: A Synology NAS IP-címének megkeresése

1. Nyisd meg a **Vezérlőpultot** és lépj a **Hálózati interfész** lapra.

![Hálózati interfész](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Vagy használd a böngészőt a [find.synology.com](http://find.synology.com) meglátogatásához.

![Synology keresése](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Jegyezd fel a Synology NAS IP-címét (pl. 192.168.18.137).

## 3. lépés: A Synology NAS hálózati portjainak megkeresése

A DSM alapértelmezett hálózati portjainak hivatalos Synology dokumentációját ebben a [Synology Tudásközpont cikkben](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services) találod.

A Synology DSM a következő alapértelmezett portokat használja:
- **HTTP (Webes hozzáférés):** Port **5000**
- **HTTPS (Biztonságos webes hozzáférés):** Port **5001**

Ezek az alapértelmezett portok a DSM felület eléréséhez.

![Hálózati portok](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## 4. lépés: A QuickConnect ID funkció engedélyezése

A Synology QuickConnect ID egy egyedi azonosító, amely lehetővé teszi a Synology NAS távoli elérését az interneten keresztül, bonyolult hálózati beállítások, például portátirányítás konfigurálása nélkül. A QuickConnect egyszerűsíti a távoli hozzáférést a Synology szervereinek felhasználásával a NAS és az eszközöd, például okostelefonod vagy számítógéped közötti kapcsolat létrehozásához a QuickConnect ID-n keresztül.

**A QuickConnect ID megkeresése vagy beállítása:**

1. **Jelentkezz be a DSM-be.**
2. Lépj a **Vezérlőpult > Külső hozzáférés > QuickConnect** menüpontra.
3. **Engedélyezd a QuickConnect-et** és hozd létre vagy tekintsd meg az egyedi QuickConnect ID-det.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## 5. lépés: Csatlakozás a Synology NAS-hoz iPhone-on/Mac-en az Evermusic vagy Flacbox segítségével

Az [Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) és a [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) zenelejátszó alkalmazások, amelyeket iOS és macOS eszközökhöz terveztek, mindegyik egyedi funkciókat és képességeket kínál a zenei könyvtárad kezeléséhez és élvezetéhez.

1. Nyisd meg az Evermusic vagy Flacbox alkalmazást és lépj a **Kapcsolatok** lapra.

![Kapcsolatok](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Válaszd a **Felhőszolgáltatás csatlakoztatása** lehetőséget és válaszd a **Synology Drive**-ot.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Két csatlakozási lehetőséged van: **manuális** a szerver IP-címével és portjával, vagy **automatikus** a QuickConnect ID-n keresztül.

### Manuális csatlakozás

A manuális módszerhez szükséged lesz a közvetlen IP-címre és portszámra, amelyeket az előző lépésekben szereztél meg.

1. Add meg a szerver URL-jét, amelyet a 2. lépésben kaptál, a következő formátumban: PROTOKOLL://IP_CÍM:PORTSZÁM
   - Használd az **5000-es portot** HTTP-hez és az **5001-es portot** HTTPS-kapcsolatokhoz.

   Például:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. A tényleges portszám a beállítás 3. lépésében erősíthető meg.
3. Add meg a **felhasználóneved** és **jelszavad** a Synology NAS-hoz.
4. Érintsd meg a **Bejelentkezés** gombot a kapcsolat létrehozásához.

![Manuális csatlakozás](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automatikus csatlakozás

Az automatikus csatlakozáshoz a 4. lépésből származó **QuickConnect ID-t** használod. A Synology NAS IP-címének és portszámának manuális megadása helyett egyszerűen add meg a **QuickConnect ID-t**. Az alkalmazás automatikusan lekéri a szükséges csatlakozási információkat.

Ez a módszer lehetővé teszi a NAS távoli elérését, még az otthoni hálózaton kívül is, így a fájljaidat az internetről kezelheted portátirányítás vagy statikus IP-címek konfigurálása nélkül.

![Automatikus csatlakozás](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Kétfaktoros hitelesítés

A DSM 4.2-től kezdve a Synology bevezette a **kétlépcsős ellenőrzést** a biztonság növelése érdekében. Ez a funkció egy **egyszeri jelszó (OTP)** kódot igényel, amelyet egy hitelesítő alkalmazás generál, a szokásos bejelentkezési adatok mellett. Ha engedélyezted a kétlépcsős ellenőrzést, a felhasználónév és jelszó megadása után az OTP-t is meg kell adnod a DSM munkamenetbe való bejelentkezéshez.

Kérjük, vedd figyelembe, hogy a munkamenet lejártát követően az alkalmazást manuálisan kell újra engedélyezni. Az újbóli engedélyezéshez:

1. Lépj az alkalmazás **Kapcsolatok** lapjára.
2. Érintsd meg a **További műveletek** gombot a szerver neve mellett.
3. Válaszd a **Beállítások** menüpontot az új hitelesítési kód megadásához és az újbóli engedélyezési folyamat befejezéséhez.

Ez biztosítja, hogy még ha nem megbízható hálózatról éred el a NAS-t, az adataid biztonságban maradnak.

## 6. lépés: Navigálás és zenelejátszás

1. A csatlakozás után az eszköz megjelenik a **Csatlakoztatott eszközök** listában.

![Csatlakoztatott eszközök](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navigálj a **Zene** mappába és érintsd meg bármelyik hangfájlt a lejátszás indításához.

![Zene lejátszása](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## 7. lépés: Csatlakoztatott felhőmappa hozzáadása a zenei könyvtárhoz

1. Nyisd meg a **Zenei könyvtár** részt az alkalmazásban.
2. Válaszd a **Zene hozzáadása** lehetőséget és válaszd a **Kapcsolatok** opciót.
3. Válaszd ki a csatlakoztatott NAS szervert és válaszd a **Zene** mappát. Érintsd meg a **Kész** gombot.
4. Az alkalmazás átvizsgálja a zenemappát és hozzáadja a támogatott hangfájlokat a zenei könyvtárhoz. A metaadatok betöltődnek, és a számaid album, előadó és műfaj szerint csoportosítva jelennek meg.

## Következtetés

Ezeket a lépéseket követve könnyedén beállíthatsz egy kapcsolatot a Synology NAS-on és streamelheted teljes zenei könyvtáradat az iPhone-ra vagy Mac-re az Evermusic vagy Flacbox segítségével. Akár otthon, akár úton vagy, élvezd a zökkenőmentes, kiváló minőségű hozzáférést kedvenc számaidhoz bárhonnan a QuickConnect segítségével. Használd ki ezeknek az alkalmazásoknak a rugalmasságát és kényelmét, és kezdd el könnyedén kezelni zenei gyűjteményedet az összes eszközödön.

A QuickConnect-en keresztüli biztonságos távoli hozzáféréssel és az audioformátumok széles skálájának támogatásával soha nem leszel messze a zenédtől. Most a NAS-on tárolt fájljaid csupán egy érintésnyire vannak!

## Gyakran ismételt kérdések

{{% details title="Mi a különbség a manuális csatlakozás és a QuickConnect között?" closed="true" %}}
A manuális csatlakozás a NAS IP-címét és portját használja, amely a helyi hálózatodon működik. A QuickConnect a Synology közvetítő szolgáltatását használja a kapcsolat létrehozásához bárhonnan az interneten keresztül, portátirányítás nélkül.
{{% /details %}}

{{% details title="Streamelhetek zenét a Synology NAS-ról az otthoni hálózatomon kívül?" closed="true" %}}
Igen. Engedélyezd a QuickConnect-et a Synology NAS-on és használd a QuickConnect ID-t az Evermusic vagy Flacbox alkalmazásban a zene streameléshez bárhonnan internetkapcsolattal.
{{% /details %}}

{{% details title="Milyen audioformátumok támogatottak a Synology NAS-ról való streameléskor?" closed="true" %}}
Az Evermusic és a Flacbox támogatja a FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD és sok más formátumot. Az összes támogatott formátum működik a Synology NAS-ról való streameléskor.
{{% /details %}}

{{% details title="Szükségem van kétfaktoros hitelesítésre a csatlakozáshoz?" closed="true" %}}
Nem, a kétfaktoros hitelesítés opcionális. Ha azonban engedélyezted a kétlépcsős ellenőrzést a Synology DSM-en, az alkalmazás egyszeri jelszót kér a bejelentkezéskor. A munkamenet lejártakor újra kell engedélyezned.
{{% /details %}}

{{% details title="A Synology natív API-t, WebDAV-ot vagy SMB-t használjam a csatlakozáshoz?" closed="true" %}}
A Synology natív API a QuickConnect-tel a legjobb választás a távoli hozzáféréshez. Helyi hálózati használathoz az SMB általában a leggyorsabb lehetőség. A WebDAV jól működik mind helyi, mind távoli hozzáféréshez. Az Evermusic és Flacbox mindhárom protokollt támogatja.
{{% /details %}}
