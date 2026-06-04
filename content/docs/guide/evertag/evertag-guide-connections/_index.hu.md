---
title: "Kapcsolatok"
date: 2020-02-01
description: "Ismerje meg, hogyan csatlakoztasson felhőtárolót, NAS-t és számítógépet az Evertag-hez. Érje el és szerkessze az audio fájlokat közvetlenül felhőtárolóból, személyes NAS-ból vagy Mac/PC-ről."
keywords: [
  "Evertag felhő beállítás", "iCloud csatlakoztatása az Evertag-hez", "SMB fájlhozzáférés iOS",
  "WebDAV audio tag szerkesztő", "NAS metaadat szerkesztés", "Wi-Fi Drive Evertag",
  "audio fájlok átvitele iPhone-ra", "Evertag iTunes File Sharing", "FLAC tag szerkesztés felhőből"
]
tags: ["útmutató", "evertag", "kapcsolatok"]
readingTime: 11
---


Ezen a képernyőn különböző forrásokat csatlakoztathat, amelyek audio fájljait tartalmazzák. Integrálhat népszerű felhőszolgáltatásokat, mint a Google Drive, Dropbox, OneDrive, iCloud és másokat, valamint csatlakoztathatja Mac-ét vagy PC-jét. Emellett szerkesztheti az Apple Time Capsule-on, WD Cloud Home-on vagy bármely SMB vagy WebDAV protokollt támogató NAS-on lévő audio fájlokat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Kapcsolatok képernyő" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Gyorselérés

A Kapcsolatok képernyő tetején egy **Gyorselérés** lista található. Bármely felhőmappa, amelyet a kedvencekhez ad – még egy mélyen beágyazott is – itt jelenik meg, így szülőmappákon való navigálás nélkül ugorhat rá.

## Csatlakozás felhőtárolóhoz

- Nyissa meg a 'Kapcsolatok' lapot  
- Válassza a 'Csatlakozás felhőtárolóhoz' lehetőséget a menüből  
- Válasszon egy felhőtároló szolgáltatást a listából  
- Adja meg hitelesítő adatait, majd koppintson a 'Kész' gombra.

Ha problémákba ütközik, ellenőrizze az internetkapcsolatot és a bejelentkezési adatokat.  
Az alkalmazás Prémium verziójában korlátlan számú szolgáltatást adhat hozzá.

## Támogatott felhőtároló szolgáltatások

Az alkalmazás jelenleg a legnépszerűbb felhőtároló szolgáltatásokat támogatja: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), valamint bármely SMB vagy WebDAV szerver.

## Biztonság és adatvédelem

Csak hivatalos SDK-kat és biztonságos kapcsolatokat használunk a csatlakoztatott felhőszolgáltatásokkal való interakcióhoz. A bejelentkezési neve és jelszava nem érhető el az alkalmazás számára. Az alkalmazás és a felhőszolgáltatás közötti összes kérés titkosított.

Amikor megadja bejelentkezési nevét és jelszavát, az alkalmazás a felhőszolgáltató által biztosított hivatalos engedélyezési oldalt jeleníti meg, és a teljes engedélyezési folyamat az alkalmazáson kívül zajlik. A felhőszolgáltató sikeres engedélyezés után auth tokent küld az alkalmazásnak, és ez a token az API hívásokhoz kerül felhasználásra.

Az auth token egy digitális kulcs, amely lehetővé teszi harmadik fél alkalmazások számára a felhőtárolóval való interakciót. Az auth token az eszközön egy Keychain nevű biztonságos rendszertárolóban tárolódik. Letöltheti fájljait a csatlakoztatott felhőszolgáltatásból az eszközre, és ezek a fájlok az alkalmazás "Documents" könyvtárába kerülnek. Ezeket a fájlokat bármikor eltávolíthatja a beépített fájlkezelővel.

Az alkalmazás nem oszt meg semmilyen információt a csatlakoztatott felhőfiókból. A felhőfiókhoz való hozzáférést bármikor visszavonhatja a fiókbeállítások oldalának megnyitásával a böngészőben.

## Auth-token visszavonása

Jelentkezzen be fiókjába böngészőben, és navigáljon a beállítások oldalra. Ott megtalálja az összes harmadik féltől származó alkalmazást, amelyek csatlakoznak a felhőfiókjához, és eltávolíthatja bármelyiket, ha már nem szeretné használni az adott alkalmazást. Részletes utasítások elérhetők [itt](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Az alkalmazásban is leválaszthatja a csatlakoztatott felhőfiókokat, és az auth token is eltávolításra kerül az eszközről. Ha eltávolítja az alkalmazást az eszközről, az összes letöltött adat és hozzáférési token is eltávolításra kerül.

## Felhőtároló leválasztása vagy konfiguráció módosítása

- Felhőtároló opciók elérése: Először keresse meg a kezelni kívánt felhőtárolót az alkalmazás felületén.  
- Koppintson a '...' gombra: A szolgáltatás neve mellett látni fog egy '...' gombot. Koppintson rá a további opciók eléréséhez.  
  - **Átnevezés**: Ha meg szeretné változtatni a felhőszolgáltatás nevét a listában, válassza az 'Átnevezés' lehetőséget.  
  - **Beállítások**: A felhőszolgáltatás konfigurációjának vagy hitelesítési adatainak módosításához válassza a 'Beállítások' lehetőséget. Néha előfordulhat, hogy újra kell engedélyezni a csatlakoztatott felhőszolgáltatást, ha az engedélyezési token lejárt.  
  - **Kibővítés megszüntetése**: Ha teljesen meg szeretné szüntetni az alkalmazás és a felhőszolgáltatás közötti kapcsolatot, válassza a 'Kibővítés megszüntetése' lehetőséget. Vegye figyelembe, hogy ez az opció eltávolítja az adott felhőszolgáltatáshoz tartozó összes dalt az alkalmazás zenekönyvtárából, de azok megmaradnak a szerveren.

## Csatlakozás számítógéphez vagy NAS-hoz

Csatlakoztathatja számítógépét, személyes NAS-át vagy más hálózati eszközöket SMB, DLNA vagy WebDAV protokoll segítségével.

## Csatlakozás számítógéphez SMB-n keresztül

- Koppintson a "Csatlakozás felhőtárolóhoz" → SMB elemre.  
- Adja meg a számítógép IP-címét és a megosztott mappa nevét az URL mezőben az smb://computer-ip-address/shared-folder-name formátumban  
- Válassza a protokoll verzióját: Auto, SMB1, SMB2  
- Adja meg a bejelentkezési nevet és jelszót (ha szükséges)  
- Koppintson a "Kész" gombra.

Ha a kapcsolat sikeres, a csatlakoztatott tárolót a "Felhőtároló" szakaszban látja majd.  
A Mac vagy PC SMB-vel való csatlakoztatásának teljes útmutatója elérhető [itt](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Csatlakozás NAS-hoz WebDAV-on keresztül

Az összes lépés ugyanaz, kivéve az URL mezőt.  
Az URL-nek http://server-name formátumban kell lennie, vagy https://server-name, ha a szerver támogatja az SSL-t.  
A NAS WebDAV protokollon keresztüli csatlakoztatásának teljes útmutatója elérhető [itt](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Elérhető eszközök

Ez a szakasz megjeleníti a helyi hálózaton belüli összes eszközt, amelyhez csatlakozhat az alkalmazáson keresztül.  
Eszközhöz való csatlakozáshoz kövesse az alábbi lépéseket:

- Nyissa meg az alkalmazást, és lépjen az "Elérhető eszközök" szakaszra.  
- Koppintson a listában a csatlakozni kívánt eszközre.  
- Szükség esetén adja meg bejelentkezési adatait a kapcsolat befejezéséhez.

## Wi-Fi Drive 

A Wi-Fi Drive egy kényelmes technológia, amely lehetővé teszi a vezeték nélküli fájlátvitelt a számítógépről iOS-eszközre asztali böngészőn keresztül.  
A funkció hatékony használatához győződjön meg arról, hogy eszköze és számítógépe ugyanahhoz a Wi-Fi hálózathoz csatlakozik.  
Íme a Wi-Fi Drive használatának lépésről lépésre szóló útmutatója.

## Wi-Fi Drive engedélyezése

- Nyissa meg az alkalmazást, és lépjen a "Kapcsolatok" lapra.  
- Válassza a "Csatlakozás Wi-Fi-n keresztül" lehetőséget a Wi-Fi Drive főképernyőjéhez.  
- Koppintson a "Wi-Fi Drive indítása" gombra a Wi-Fi Drive engedélyezéséhez.

## A Wi-Fi Drive elérése számítógépen

- A számítógépen nyisson meg egy böngészőt (pl. Chrome, Firefox vagy Safari).  
- A böngésző címsorába írja be az alkalmazás által megadott URL-t.

## Fájlok vezeték nélküli átvitele

Amint az iOS-eszközéhez tartozó weboldal megnyílik a böngészőben, egyszerűen húzza és ejtse a fájlokat a számítógépéről a weboldalra.  
A húzott és ejtett fájlok elkezdenek átkerülni iOS-eszközére, és elérhetők lesznek az alkalmazásban.

A Wi-Fi Drive segítségével történő vezeték nélküli fájlátvitel részletes utasításai elérhetők [itt](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

Az iTunes File Sharing egy másik technológia, amely lehetővé teszi a fájlok átvitelét számítógépről eszközre a Mac Finder alkalmazásával és Lightning kábellel.  
- Egyszerűen csatlakoztassa az eszközt a számítógéphez kábellel, és indítsa el a Finder alkalmazást Mac-én.  
- Nyissa meg a "Helyek" → "Csatlakoztatott eszköz" → "Fájlok" elemet, majd keresse meg az aktuális alkalmazást.  
- Koppintson az alkalmazás ikonjára az összes megosztott mappa megtekintéséhez.  
- Húzza-ejtés módszerrel másolja a fájlokat a számítógépről az eszköz megosztott mappájába.

Az iTunes File Sharing használatának részletes utasításai elérhetők [itt](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## USB flash meghajtó csatlakoztatása

Ha SD kártyával vagy USB stickkel rendelkezik, csatlakoztathatja azt Lightning vagy USB-C kártyaolvasóval iPhone/iPad eszközön, vagy közvetlenül bedughatja Mac-be. Az alkalmazás jelenleg az Apple Certified kártyaolvasókat támogatja. Részletes utasításokkal rendelkezünk arról, hogyan csatlakoztasson USB flash meghajtót iPhone-hoz vagy iPadhez, és kezelje rajta lévő fájlokat, amelyek elérhetők [itt](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). A csatlakoztatott meghajtók a Kapcsolatok képernyő **Csatlakoztatott kiegészítők** szakaszában jelennek meg.

## Fájlkezelő

Miután csatlakoztatott egy felhőtároló szolgáltatást, koppintson az ikonjára az összes elérhető fájl és mappa megtekintéséhez. A beépített fájlkezelővel dolgozhat ezekkel a fájlokkal – letölthet, átnevezhet, mozgathat és még sok mást. Amikor letöltést indít, a fájl megjelenik az átviteli sorban. Az átviteli sor megtekintéséhez lépjen a "Helyi fájlok" lapra, és koppintson a bal felső sarokban lévő forgó nyilakra. Az összes letöltött fájl és mappa a "Helyi fájlok" szakaszban érhető el.

## Felső eszköztár

A navigációs sáv alatt kényelmesen elhelyezett felső eszköztár több hasznos műveletet kínál könnyű hozzáféréshez. Ezt az eszköztárat egyszerű lefelé húzással jelenítheti meg vagy rejtheti el. Az elérhető műveletek:

- **Keresés**: Ez az opció lehetővé teszi az aktuális könyvtárban való gyors keresést, megkönnyítve meghatározott fájlok vagy mappák megtalálását.  

## Mappaopciók

Amikor mappát nyit meg az alkalmazásban, a képernyő jobb felső sarkában lévő "..." gombra koppintva hasznos műveletek sorát találja.  
Ezek a műveletek:

- **Kiválasztás**: Fájl kiválasztási mód aktiválása. Ez a mód lehetővé teszi egy vagy több fájl kiválasztását a mappán belül.  
- **Új mappa**: Új mappa létrehozása az aktuális mappán belül. Ez a funkció segít rendezni fájljait.  
- **Fájlok feltöltése**: Fájlok feltöltése az eszközről az online mappába. Ez a művelet lehetővé teszi fájlok átvitelét a felhőbe vagy szerverre.  
- **Keresés**: Konkrét fájlok keresése az aktuális mappán belül.  
- **Rendezés**: Fájlok rendezése a mappán belül olyan szempontok szerint, mint a név, méret vagy szerkesztési dátum.  
- **Rács/Lista nézet**: Váltás kétféle megjelenítési mód között: táblázat nézet és miniatűr nézet.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag felhőmappa rendezés" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Online fájlok szerkesztése

Ha az alkalmazásban több fájlt kell kezelni a felhőtárolójában, a kiválasztási mód segítségével egyszerűsítheti a műveleteket. Kövesse az alábbi lépéseket a hatékony fájlkezeléshez:

- **Kiválasztási mód aktiválása**: Nyissa meg az alkalmazást az eszközén, és navigáljon a felhőtárolót tartalmazó szakaszhoz. Keresse meg a jobb felső sarokban lévő "..." (három pont) gombot. Koppintson rá, és válassza a "Kiválasztás" menüpontot a kiválasztási mód aktiválásához.  
- **Fájlok kiválasztása**: Jelölőnégyzetek jelennek meg minden felsorolt fájl vagy mappa mellett. Válasszon egy vagy több fájlt vagy mappát a mellettük lévő jelölőnégyzetekre koppintva.  
- **Különböző műveletek végrehajtása**: Miután kiválasztotta a kezelni kívánt fájlokat vagy mappákat, számos műveletet hajthat végre:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag fájl kiválasztás" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Fájlműveletek

A fájl neve közelében egy "..." (három pont) szimbólumot láthat – ez a műveleti menü.  
Koppintson rá az elérhető műveletek listájának megjelenítéséhez:

- **Audio címkék szerkesztése**: Ezzel az opcióval hozzáférhet a beépített tag szerkesztőhöz, és módosíthatja a kiválasztott fájl audio tagjeit. A fájl ideiglenesen letöltődik egy ideiglenes könyvtárba, majd a módosítások megerősítése után feltöltődik a tárolóba.  
- **Hozzáadás a kedvencekhez**: Ez a művelet hozzáadja a fájlt a kedvenc fájlok listájához a gyors és kényelmes hozzáférés érdekében.  
- **Letöltés**: Ezzel a művelettel letöltheti a fájlt vagy mappát az eszközre offline használathoz.  
- **Átnevezés**: Ez az opció lehetővé teszi a fájl átnevezését közvetlenül a távoli tárhelyen.  
- **Áthelyezés**: Ezzel a művelettel áthelyezheti a fájlt a felhőtárolón belül egy másik mappába.  
- **Megnyitás más alkalmazásban**: Ezzel a művelettel exportálhatja a fájlt egy másik kompatibilis alkalmazásba. A fájl letöltődik az eszközre, majd megjelenik a Megosztás párbeszédpanel.  
- **Törlés**: Legyen óvatos ezzel a művelettel, mivel véglegesen eltávolítja a fájlt a felhőtárolóból. **Ez a törlés nem vonható vissza**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag fájl opciók" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Ha a műveletek listája meghaladja a rendelkezésre álló képernyőterületet, egyszerűen görgessen le a műveleti menüben a további opciók eléréséhez.

## Mappaműveletek

A felhőtárolón lévő minden mappához különböző műveletek állnak rendelkezésre. Az opciók eléréséhez koppintson a mappa neve melletti "..." ikonra. Ha nem látja az összes műveletet, görgessen le a további lehetőségek megjelenítéséhez. Az elérhető műveletek:

- **Hozzáadás a kedvencekhez**: Ezzel a művelettel hozzáadhatja a mappát a kedvenc fájlok listájához a gyors és kényelmes hozzáférés érdekében.  
- **Letöltés**: A mappa teljes tartalmának letöltése az eszközre offline hozzáféréshez.  
- **Átnevezés**: A mappa átnevezése közvetlenül a távoli tárhelyen.  
- **Áthelyezés**: A mappa áthelyezése egy másik helyre a felhőtárolón belül.  
- **Törlés**: Legyen óvatos ezzel a művelettel, mivel véglegesen eltávolítja a mappát és tartalmát a felhőtárolóból. **Ez a művelet nem vonható vissza**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag mappa opciók" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
