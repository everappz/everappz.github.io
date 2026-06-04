---
title: "Kapcsolatok"
date: 2020-01-01
description: "Tanuld meg, hogyan csatlakoztathatsz felhőszolgáltatásokat, számítógépeket, NAS eszközöket és kezelheted zenefájljaidat az Evermusicban. Lépésről lépésre útmutató a Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing és egyéb funkciókhoz."
keywords: [
  "Evermusic", "felhőalapú zenei lejátszó", "NAS streaming", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "felhőtárhely csatlakoztatása", "zenei átvitel iPhone", "fájlkezelő iOS"
]
tags: ["evermusic", "útmutató", "kapcsolatok"]
readingTime: 11
---


A Kapcsolatok képernyőn csatlakoztathatod az összes zenétárhelyed — népszerű felhőszolgáltatások, saját hosztolt médiaszerverek, Mac-ed vagy PC-d, személyes NAS, Apple Time Capsule, WD My Cloud Home, még USB flash meghajtó is — és mindet egyetlen egységes felületen kezelheted. A Kapcsolatok képernyőn állíthatod be a Gyors hozzáférést a mélyebben beágyazott felhőmappákhoz is, és itt hitelesítheted a Last.fm-t a scrobbling-hoz.

A képernyő egyértelműen jelölt szakaszokra van felosztva, így akár egyetlen iCloud Drive fióktól egészen több felhő- és NAS-eszközre kiterjedő könyvtárig skálázható: Gyors hozzáférés a tetején (kedvenc felhőmappáid), Felhőtárhely (hozzáadott fiókok), Helyi hálózat (Bonjour-felderített eszközök), Számítógép (Wi-Fi Drive, iTunes File Sharing, SMB), Külső kiegészítők (csatlakoztatott USB flash meghajtók) és Egyéb szolgáltatások (Last.fm és hasonlók).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Kapcsolatok képernyő" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Csatlakozás felhőtárhelyhez

- Nyisd meg a Kapcsolatok lapot.
- Válaszd a Csatlakozás felhőtárhelyhez menüpontot.
- Válassz egy felhőtárhely-szolgáltatást a listából.
- Jelentkezz be a szolgáltató hivatalos engedélyezési oldalán (az Evermusic soha nem látja a jelszavadat).
- Koppints a Kész gombra.

{{< cards cols="1">}}
  {{< card title="" subtitle="Felhőtárhely-szolgáltató kiválasztó" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Ha bármilyen problémába ütközöl, ellenőrizd az internetkapcsolatot és a bejelentkezési adatokat, és győződj meg arról, hogy a kétfaktoros hitelesítés megfelelően van konfigurálva az adott szolgáltatásnál.  
Az alkalmazás Premium verziójában korlátlan számú szolgáltatást adhatsz hozzá. Az ingyenes felhasználók egyszerre egyetlen felhőfiókot csatlakoztathatnak.

## Támogatott felhőtárhely-szolgáltatások

Az Evermusic a népszerű felhő- és saját hosztolt szolgáltatások teljes kínálatát támogatja. Az ingyenes felhasználók ugyanazt a szolgáltatói katalógust kapják, de egy fiók korláttal; a Premium korlátlan fiókokat nyit meg és eltávolítja a legtöbb más korlátot.

- **Személyes felhőfiókok:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Saját hosztolt szerverek és médiakönyvtárak:** Plex · Jellyfin · Emby · Subsonic (és minden Subsonic-kompatibilis szerver — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (és Owncloud, a megosztott API-n keresztül) · Synology Drive · QNAP.
- **NAS és fájlmegosztási protokollok:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (jelszó vagy nyilvános kulcs alapú hitelesítés), NFS, és DLNA (csak olvasható — lejátszás és letöltés).
- **S3-kompatibilis objektumtároló:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage, vagy bármely S3-API végpont.
- **Helyi hálózati felfedezés:** az Elérhető eszközök szakasz automatikusan listázza azokat az eszközöket a Wi-Fi hálózaton, amelyek Bonjour / mDNS-en keresztül hirdetik magukat — Plex, Jellyfin, Emby szerverek, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, csatolt meghajtójú AirPort routerek stb.

## Biztonság és adatvédelem

Csak hivatalos SDK-t és biztonságos kapcsolatot használunk a csatlakoztatott felhőszolgáltatásokkal való interakcióhoz. A bejelentkezési neved és jelszavad nem érhető el az alkalmazás számára. Az alkalmazás és a felhőszolgáltatás közötti összes kérés titkosított.

Amikor megadod a bejelentkezési adatokat, az alkalmazás a felhőszolgáltató által biztosított hivatalos engedélyezési oldalt jeleníti meg, és az összes engedélyezési folyamat az alkalmazáson kívül zajlik. A felhőszolgáltató sikeres engedélyezés után auth-tokent küld az alkalmazásnak, amelyet API-hívásokhoz használ.

Az auth-token egy digitális kulcs, amely lehetővé teszi harmadik fél alkalmazások számára a felhőtárhellyel való interakciót. Az auth-token az eszközödön a Keychain nevű biztonságos rendszertárhelyen van tárolva. Letöltheted a csatlakoztatott felhőszolgáltatásból fájljaidat az eszközre, és azok az alkalmazás „Documents" könyvtárába kerülnek. Ezeket a fájlokat bármikor törölheted a beépített fájlkezelővel.

Az alkalmazás nem oszt meg semmilyen információt a csatlakoztatott felhőfiókból. A felhőfiókodhoz való hozzáférést bármikor visszavonhatod a fiókbeállítások megnyitásával a webböngészőben.

## Auth-token visszavonása

Jelentkezz be a fiókodba a webböngészőn, és navigálj a beállítások oldalra. Ott megtalálhatod az összes felhőfiókodhoz csatlakoztatott harmadik féltől származó alkalmazást, és eltávolíthatod azokat, amelyeket nem szeretnél tovább használni. Részletes utasítások [itt](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) találhatók.

A csatlakoztatott felhőfiókokat az alkalmazásban is leválaszthatod, és az auth-token is törlődik az eszközödről. Ha eltávolítod az alkalmazást az eszközödről, az összes letöltött adat és hozzáférési token szintén törlődik.

## Felhőtárhely leválasztása vagy konfiguráció módosítása

- Felhőtárhely-beállítások elérése: először keresd meg a kezelni kívánt felhőtárhelyet az alkalmazás felületén.
- Koppints a '...' gombra: a szolgáltatás neve melletti '...' gombra koppintva érheted el a további beállításokat.
  - **Átnevezés**: ha meg szeretnéd változtatni a felhőszolgáltatás nevét a listában, válaszd az „Átnevezés" lehetőséget.
  - **Beállítások**: a felhőszolgáltatás konfigurációjának vagy hitelesítési adatainak módosításához válaszd a „Beállítások" lehetőséget. Néha szükség lehet a csatlakoztatott felhőszolgáltatás újbóli engedélyezésére, ha az engedélyezési token lejárt.
  - **Leválasztás**: ha teljesen meg szeretnéd szüntetni az alkalmazás és a felhőszolgáltatás közötti kapcsolatot, válaszd a „Leválasztás" lehetőséget. Figyelem: ez a lehetőség eltávolítja az ehhez a felhőszolgáltatáshoz tartozó összes dalt az alkalmazás zenei könyvtárából, de a szerveren megmaradnak.

{{< cards cols="1">}}
  {{< card title="" subtitle="Csatlakoztatott felhőtárhely további műveletek menüje" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Csatlakozás számítógéphez vagy NAS-hoz

Csatlakoztathatod a számítógépedet, személyes NAS-odat vagy más hálózati eszközöket SMB, DLNA vagy WebDAV protokoll segítségével.

## Csatlakozás számítógéphez SMB-n keresztül

- Koppints a „Csatlakozás felhőtárhelyhez" → SMB lehetőségre.
- Add meg a számítógép IP-címét és a megosztott mappa nevét az URL mezőben, a következő formátumban: smb://computer-ip-address/shared-folder-name
- Válassz protokollverziót: Auto, SMB1, SMB2
- Add meg a bejelentkezési nevet és jelszót (ha szükséges)
- Koppints a „Kész" gombra.

Ha a kapcsolat sikeres, a csatlakoztatott tárhely megjelenik a „Felhőtárhely" szakaszban.  
A Mac vagy PC SMB-n keresztüli csatlakoztatásáról szóló teljes oktatóanyag [itt](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) érhető el.

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB kapcsolat beállításai" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Csatlakozás NAS-hoz WebDAV-on keresztül

Minden lépés azonos, kivéve az URL mezőt.  
Az URL formátuma http://server-name legyen, vagy https://server-name, ha a szerver SSL-t támogat.
A NAS WebDAV protokollon keresztüli csatlakoztatásáról szóló teljes oktatóanyag [itt](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) érhető el.

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV kapcsolat beállításai" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Csatlakozás számítógéphez vagy NAS-hoz DLNA-n keresztül

Megoszthatod a Windows PC-den vagy személyes NAS-odon lévő zenei könyvtárat a DLNA protokoll segítségével, és az alkalmazásban elérheted azt a [itt](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) leírtak szerint. A DLNA népszerű és széles körben használt protokoll, de csak a zene lejátszását vagy letöltését teszi lehetővé. Nem tölthetsz fel fájlokat és nem hozhatsz létre új mappákat a szerveren.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA kapcsolat beállításai" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Elérhető eszközök

Ez a szakasz megjeleníti a helyi hálózaton lévő összes eszközt, amelyhez az alkalmazáson keresztül csatlakozhatsz.  
Eszközhöz való csatlakozáshoz kövesd ezeket a lépéseket:

- Nyisd meg az alkalmazást, és menj az „Elérhető eszközök" szakaszba.
- Koppints a listából arra az eszközre, amelyhez csatlakozni szeretnél.
- Ha szükséges, add meg a bejelentkezési adatokat a kapcsolat befejezéséhez.

{{< cards cols="1">}}
  {{< card title="" subtitle="Elérhető eszközök a helyi hálózaton" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

A Wi-Fi Drive egy kényelmes technológia, amely lehetővé teszi a vezeték nélküli fájlátvitelt a számítógépről az iOS-eszközre egy asztali böngészőn keresztül.  
A funkció hatékony használatához győződj meg arról, hogy az eszközöd és a számítógéped ugyanahhoz a Wi-Fi hálózathoz csatlakozik.  
Íme egy lépésről lépésre útmutató a Wi-Fi Drive használatához.

## Wi-Fi Drive engedélyezése

- Nyisd meg az alkalmazást, és menj a „Kapcsolatok" lapra.
- Válaszd a „Csatlakozás Wi-Fi-n keresztül" lehetőséget a Wi-Fi Drive főképernyőjének eléréséhez.
- Koppints a „Wi-Fi Drive indítása" gombra a Wi-Fi Drive engedélyezéséhez.

## Wi-Fi Drive elérése a számítógépről

- A számítógépeden (asztali vagy laptopszámítógépen) nyiss meg egy webböngészőt (pl. Chrome, Firefox vagy Safari).
- A böngésző címsorában add meg az alkalmazás által megadott URL-t.

## Fájlok vezeték nélküli átvitele

Amint az iOS-eszközödhöz tartozó weboldal megnyílik a böngészőben, egyszerűen drag-and-drop módszerrel húzhatod a fájlokat a számítógépről a weboldalra.  
A drag-and-drop-pal áthelyezett fájlok megkezdik az átvitelt az iOS-eszközre, és elérhetővé válnak az alkalmazáson belül.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive szerver beállításai" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Részletes utasítások arról, hogyan lehet fájlokat vezeték nélkül átvinni a WiFi-Drive segítségével, [itt](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) érhetők el.

## iTunes File Sharing

Az iTunes File Sharing egy másik technológia, amely lehetővé teszi fájlok átvitelét számítógépről eszközre a Mac Finder alkalmazásával és lightning-kábellel.  
- Csak csatlakoztasd az eszközt a számítógéphez kábellel, majd futtasd a Finder alkalmazást a Macon.
- Nyisd meg a „Helyek" → „Csatlakoztatott eszközöd" → „Fájlok" elemet → és keresd meg az Evermusic alkalmazást.
- Koppints az alkalmazás ikonra az összes megosztott mappa megtekintéséhez.
- Másold a fájlokat a számítógépről az eszközön lévő megosztott mappába drag-and-drop segítségével.

Részletes utasítások az iTunes file sharing használatáról [itt](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) érhetők el.

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing Macon" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## USB flash meghajtó csatlakoztatása

Ha van SD-kártyád, lightning kártyaolvasóval csatlakoztathatod. Az alkalmazás jelenleg az Apple Certified kártyaolvasókat és az iXpand Flash Drive-okat támogatja. Ha iXpand Flash Drive-od van, helyezd be a lightning portba, és nyisd meg az alkalmazást. Megjelenik egy „Külső eszköz csatlakoztatva" üzenet és az eszköz adatai. Egyszerűen koppints a flash meghajtó ikonra a zenei mappa eléréséhez, majd koppints bármely hangfájlra a lejátszás megkezdéséhez. Részletes utasítások arról, hogyan csatlakoztathatsz USB flash meghajtót az iPhone-hoz és hallgathatsz zenét, vagy kezelheted a rajta lévő fájlokat, [itt](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it) érhetők el.

## Fájlkezelő

Miután csatlakoztattál egy felhőtárhely-szolgáltatást, koppints az ikonjára az összes elérhető fájl és mappa megtekintéséhez. A beépített fájlkezelővel dolgozhatod fel ezeket a fájlokat — letöltés, átnevezés, áthelyezés és más műveletek. Amikor elindítasz egy letöltést, a fájl megjelenik az átviteli várólistában. Az átviteli várólista megtekintéséhez menj a „Helyi fájlok" lapra, és koppints a bal felső sarokban lévő forgó nyilakra. Az összes letöltött fájl és mappa a „Helyi fájlok" szakaszban érhető el.

## Felső eszköztár

A felső eszköztár a navigációs sáv alatt található, és számos hasznos műveletet kínál könnyű hozzáféréshez. Ezt az eszköztárat egyszerű lefelé húzó mozdulattal jelenítheted meg vagy rejtheted el. Íme az elérhető műveletek:

- **Keresés**: ez a lehetőség lehetővé teszi a gyors keresést az aktuális könyvtárban, megkönnyítve az adott fájlok vagy mappák megtalálását.
- **Lejátszás folytatása**: ha engedélyezve van az alkalmazás beállításaiban, ez a funkció visszaállítja a hanglejátszó várólistáját és az aktuális mappa utolsó médiahelyzetét. Ez egy praktikus módja a zenei könyvtárban való folytatásnak.
- **Összes lejátszása**: ha kiválasztod ezt a műveletet, az alkalmazás megvizsgálja az aktuális mappát és almappáit, és az összes talált hangfájlt hozzáadja egy új lejátszóvárólistához. Ez akkor hasznos, ha egy adott könyvtárban lévő összes zenét le szeretnéd játszani.
- **Összes keverése**: hasonló az „Összes lejátszása" funkcióhoz, de a fájlokat megkeveri, mielőtt hozzáadja őket a hanglejátszó várólistájához. Ez egy remek módja a zene véletlen sorrendben való élvezetének.

{{< cards cols="1">}}
  {{< card title="" subtitle="Felső eszköztár egy felhőmappán belül" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Mappabeállítások

Amikor megnyitsz egy mappát az alkalmazásban, a képernyő jobb felső sarkában lévő „..." gombra koppintva hasznos műveletek állnak rendelkezésre.  
Íme ezeknek a műveleteknek a leírása:

- **Kiválasztás**: fájlkijelölési mód aktiválása. Ez a mód lehetővé teszi, hogy egy vagy több fájlt válassz ki a mappán belül, megkönnyítve a kijelölt elemeken végzett műveleteket.
- **Új mappa**: új mappa létrehozása az aktuális mappán belül. Ez a funkció lehetővé teszi fájljaid rendezését és a könyvtár jó szervezésének megőrzését.
- **Offline mód engedélyezése**: az offline mód bekapcsolása az aktuális mappához. Az offline mód az egyszerű letöltésen túl aktívan figyeli a mappa változásait. Ha online új fájlokat adsz hozzá a mappához, az alkalmazás automatikusan letölti ezeket az eszközre. Ez biztosítja, hogy a helyi könyvtár naprakész maradjon a szerveren lévő változásokkal.
- **Fájlok feltöltése**: fájlok feltöltése az eszközről az online mappába. Ez a művelet lehetővé teszi fájlok átvitelét a felhőbe vagy szerverre, hogy bárhonnan elérhetők legyenek.
- **Keresés**: keresés adott fájlok között az aktuális mappán belül. Ez különösen hasznos az adott elemek gyors megtalálásához egy nagy gyűjteményben.
- **Rendezés**: fájlok rendezése a mappán belül kritériumok szerint, például név, méret vagy szerkesztési dátum alapján. Az alapértelmezett rendezési mód általában tükrözi a szerveren lévő rendezési sorrendet, de megváltoztathatod a saját preferenciáid szerint.
- **Rács/lista nézet**: váltás a két nézeti mód között: táblázatos nézet és bélyegkép nézet. A táblázatos nézet listában jeleníti meg a fájlokat, míg a bélyegkép nézet vizuális ábrázolásokat mutat, megkönnyítve a tartalom azonosítását egy pillantással.

{{< cards cols="1">}}
  {{< card title="" subtitle="Aktuális mappa további műveletek menüje" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Online fájlok szerkesztése

Amikor több fájlt kell kezelned az Evermusicban lévő felhőtárhelyeden, a kijelölési módot használhatod a műveletek egyszerűsítéséhez. Kövesd ezeket a lépéseket a hatékony fájlkezeléshez:

- **Kijelölési mód aktiválása**: nyisd meg az alkalmazást az eszközödön, és navigálj a felhőtárhelyet tartalmazó szakaszhoz. Keresd a jobb felső sarokba a „..." (ellipszis) gombot. Koppints rá, és válaszd a „Kiválasztás" menüpontot a kijelölési mód aktiválásához.
- **Fájlok kiválasztása**: jelölőnégyzetek jelennek meg minden listázott fájl vagy mappa mellett. Válassz egy vagy több fájlt vagy mappát, egyszerűen koppintva a mellettük lévő jelölőnégyzetekre.
- **Különböző műveletek végrehajtása**: miután kiválasztottad a kezelni kívánt fájlokat vagy mappákat, hozzáférhetsz az igényeidnek megfelelő számos művelethez.

{{< cards cols="1">}}
  {{< card title="" subtitle="Kijelölési mód online fájlokhoz" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Fájlműveletek

A fájl neve mellett egy ellipszis szimbólumot „..." (három pont) láthatod — ez a műveletek menüje.  
Koppints rá az elérhető műveletek listájának megjelenítéséhez:

- **Lejátszás következőként**: válaszd ezt a műveletet, hogy a kiválasztott fájlt a lejátszóvárólista tetejére helyezd, biztosítva, hogy az éppen lejátszott elem után azonnal lejátssza.
- **Lejátszás később**: ez a lehetőség hozzáadja a fájlt a lejátszóvárólista aljához, biztosítva, hogy a meglévő várólista után játssza le.
- **Hozzáadás a zenei könyvtárhoz**: ez a művelet lehetővé teszi a fájl beillesztését a zenei könyvtárba, könnyen elérhetővé és előadó, album, műfaj vagy zeneszerző szerint rendezetten teszi.
- **Hozzáadás lejátszólistához**: ezzel a művelettel hozzáadhatod a fájlt egy meglévő lejátszólistához, vagy létrehozhatsz egy újat.
- **Audio-tagek szerkesztése**: ha kiválasztod ezt a lehetőséget, hozzáférhetsz az Evermusic beépített tag-szerkesztőjéhez, lehetővé téve a kiválasztott fájl audio-tagjainak módosítását. A fájl ideiglenesen letöltődik egy ideiglenes könyvtárba, majd a változtatások megerősítése után feltöltődik a tárhelyre.
- **Hozzáadás a kedvencekhez**: ez a művelet hozzáadja a fájlt a kedvenc fájlok listájához a gyors és kényelmes hozzáférés érdekében.
- **Letöltés**: válaszd ezt a műveletet, hogy letöltsd a fájlt vagy mappát az eszközre, offline használatra.
- **Átnevezés**: ez a lehetőség lehetővé teszi a fájl közvetlen átnevezését a távoli tárhelyen, egyéni fájlelnevezés céljából.
- **Áthelyezés**: válaszd ezt a műveletet, hogy egy másik mappába helyezd a fájlt a felhőtárhelyen belül, elősegítve a rendezett fájlstruktúra fenntartását.
- **Megnyitás a következővel**: ezzel a művelettel exportálhatod a fájlt egy másik kompatibilis alkalmazásba. A fájl letöltődik az eszközre, majd megjelenik a Megosztás párbeszédpanel a további megosztáshoz vagy interakcióhoz.
- **Törlés**: légy óvatos ezzel a művelettel, mivel véglegesen eltávolítja a fájlt a felhőtárhelyről. Ez a törlés nem vonható vissza.

{{< cards cols="1">}}
  {{< card title="" subtitle="Egyetlen fájl további műveletek menüje" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Ha a műveletek listája meghaladja a rendelkezésre álló képernyőterületet, görgess le a műveletek menüjén belül a további lehetőségek eléréséhez.

## Mappaműveletek

A felhőtárhelyeden lévő minden mappához különböző műveletek érhetők el. Ezek eléréshez egyszerűen koppints a mappa neve melletti „..." ellipszis ikonra. Ha nem látod az összes műveletet, görgess le a további lehetőségek megjelenítéséhez. Íme az elérhető műveletek:

- **Összes lejátszása**: a jelenlegi lejátszóvárólistát lecseréli a kiválasztott mappában lévő összes elemre.
- **Lejátszás következőként**: az egész mappát hozzáadja a lejátszóvárólista tetejéhez, közvetlenül az éppen lejátszott elem után.
- **Lejátszás később**: hozzáfűzi a mappa tartalmát a lejátszóvárólista aljához.
- **Hozzáadás a zenei könyvtárhoz**: ez a művelet zökkenőmentesen beilleszti a mappa tartalmát a zenei könyvtárba, könnyen elérhetővé és előadó, album, műfaj vagy zenszerző szerint rendezetten teszi.
- **Hozzáadás lejátszólistához**: az egész mappát belefoglalhatod egy lejátszólistába. Lehetőséged van új lejátszólista létrehozására is, és a mappa neve automatikusan hozzárendelődik.
- **Hozzáadás a kedvencekhez**: ezzel a művelettel hozzáadhatod a mappát a kedvenc fájlok listájához a gyors és kényelmes hozzáférés érdekében.
- **Offline mód engedélyezése**: ha engedélyezed az offline módot a kiválasztott mappához, az alkalmazás az egyszerű letöltésen túl folyamatosan figyeli a változásokat, és ha új fájlokat adnak hozzá az online mappához, azok automatikusan letöltődnek az alkalmazásba.
- **Letöltés**: az összes mappa tartalmának letöltése az eszközre offline hozzáférés céljából.
- **Átnevezés**: a mappa közvetlen átnevezése a távoli tárhelyen.
- **Áthelyezés**: a mappa más helyre való áthelyezése a felhőtárhelyen belül.
- **Törlés**: légy óvatos ezzel a művelettel, mivel véglegesen eltávolítja a mappát és tartalmát a felhőtárhelyről. Ez a művelet nem vonható vissza.


## Gyors hozzáférés

A Gyors hozzáférés szakasz a képernyő tetején található. Gyors hozzáférést biztosít a csatlakoztatott felhőszolgáltatásokból kedvenc és nemrég megnyitott fájljaidhoz.
Amikor megnyitsz egy fájlt vagy mappát a felhőből, az hozzáadódik a „Nemrég megnyitott" listához. A lista törléséhez nyisd meg a „Legutóbbiak" részt, koppints a „További műveletek" gombra, és válaszd a „Lista törlése" lehetőséget. A mélyen beágyazott mappákat is megjelölheted kedvencként, hogy gyorsan hozzáférhess hozzájuk a könyvtárstruktúra böngészése nélkül.

## Egyéb szolgáltatások

Ez a szakasz olyan extra funkciókat jelenít meg, amelyek javítják a felhasználói élményt. Jelenleg az alkalmazás támogatja a Last.fm scrobbling-ot. Csatlakoztatáskor a lejátszási statisztikáid automatikusan elküldésre kerülnek a Last.fm fiókodba. Később meglátogathatod a Last.fm profilodat, ahol megtekintheted a hallgatási elemzéseket és személyre szabott zenei ajánlásokat kaphatsz. Részletes beállítási utasítások [itt](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm) érhetők el.
