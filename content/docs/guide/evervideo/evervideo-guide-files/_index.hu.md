---
title: "Fájlok"
date: 2020-02-01
lastmod: 2026-06-01
description: "Ismerje meg, hogyan használhatja a Fájlok lapot az Evervideóban iPhone-on, iPaden és Macon. Csatlakoztassa a felhőszolgáltatásokat, NAS-eszközöket, médiaszervereket és RTSP streameket egy helyen. Kezelje az offline videókat, az átviteli sort, letöltéseket, Wi-Fi Drive-ot, iTunes / Finder fájlmegosztást és USB-meghajtókat. Tartalmazza az iCloud Drive-ot, Google Drive-ot, Dropboxot, OneDrive-ot, MEGÁt, Boxot, pCloudot, Synologyt, QNAP-et, Plexet, Jellyfint, Emby-t, Subsonicot, Navidromet, SMB-t, WebDAV-ot, NFS-t, FTP / SFTP-t, DLNA-t és S3-kompatibilis tárolót."
keywords: [
  "Evervideo fájlok", "Evervideo kapcsolatok", "Evervideo helyi fájlok",
  "felhővideó beállítás iPhone", "Google Drive videó csatlakoztatása", "SMB videó streaming",
  "WebDAV videólejátszó iOS", "DLNA videó iPhone", "NAS videó streaming",
  "Wi-Fi Drive videóátvitel", "Evervideo iTunes fájlmegosztás", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo offline mód videó", "Evervideo átviteli sor",
  "Evervideo fájlkezelő", "Evervideo Dokumentumok mappa",
  "videólejátszó Synology", "videólejátszó QNAP",
  "videólejátszó Apple Time Capsule", "USB DAC videó",
  "iXpand videólejátszó", "S3 videólejátszó"
]
tags: ["útmutató", "evervideo", "fájlok", "kapcsolatok", "felhő", "NAS", "Plex", "RTSP"]
readingTime: 14
---

A Fájlok lap az Evervideo mindent-egyben fájlkezelője. A legtöbb videóalkalmazással ellentétben, amelyek a felhőtárhelyet és a helyi fájlokat különböző lapokba osztják, az Evervideo mindkettőt egyetlen, görgethető képernyőre olvasztja össze, így a Plex-szervertől a felhőmappán át az iPhone Dokumentumok mappájáig válthat lapok közötti ugrás nélkül.

A Fájlok lap világos részekre oszlik, amelyek ebben a sorrendben jelennek meg a képernyőn:

- **Gyors hozzáférés** — legutóbbiak és kedvencek a legutóbb megnyitott fájlokhoz és mappákhoz.
- **Fájlok ebben az alkalmazásban** — ami az Evervideo sandboxolt Dokumentumok mappájában él.
- **Fájlok ezen az iPhone-on / iPaden / Macon** — az eszközén máshol lévő videók, amelyek a rendszer fájlválasztón keresztül érhetők el.
- **Felhőtárhely** — minden csatlakoztatott felhőfiók, NAS és médiaserver.
- **Elérhető eszközök** — Bonjour / mDNS által automatikusan felderített szerverek és meghajtók a helyi hálózaton.

A Fájlok képernyő jobb felső sarkában található egy Átvitelek gomb (egy forgó nyilakból álló ikon). Érintse meg az Átviteli sor megnyitásához, ahol figyelemmel kísérhet minden letöltést és feltöltést az összes forrásból.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo fájlok csatlakoztatott tárolókon" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Csatlakozás felhőtárhelyhez

A Fájlok lap Felhőtárhely szakasza az a hely, ahol minden csatlakoztatott fiók, NAS, médiaserver és stream él — egymás mellett, egyetlen görgethető listában.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo felhőtárhely szakasz a Fájlok lapon" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Nyissa meg a **Fájlok** lapot.
- Görgessen a **Felhőtárhely** szakaszhoz.
- Érintse meg a **Csatlakozás felhőtárhelyhez** lehetőséget a menüből.
- Válasszon egy felhőtároló-szolgáltatást a listából.
- Adja meg hitelesítési adatait a felhőszolgáltató által megadott hivatalos jogosultságkezelési oldalon, majd érintse meg a **Kész** lehetőséget.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo felhőtároló-szolgáltatás csatlakoztatása" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Ha bármilyen problémába ütközik, ellenőrizze internetkapcsolatát és bejelentkezési / jelszóát. Az alkalmazás Premium verziójában korlátlan számú szolgáltatást adhat hozzá; az ingyenes verzió legfeljebb hármat támogat.

## Támogatott felhőtároló-szolgáltatások, médiaszerverek és protokollok

Az Evervideo rendkívül széles forráskészletet támogat videóihoz. Minden alábbi egységes Csatlakozás felhőtárhelyhez folyamatból működik.

**Személyes felhőtárhely:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Önhostolt médiaszerverek:** Plex · Jellyfin · Emby · Subsonic (és minden Subsonic-kompatibilis szerver — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (és ownCloud a megosztott API-n keresztül) · Synology Drive · QNAP.

**NAS és fájlmegosztási protokollok:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH fájlátviteli protokoll, jelszavas vagy nyilvános kulcsú hitelesítés) · NFS · DLNA / UPnP (lejátszás és letöltés).

**Élő és IP-kamera streamek:** RTSP — irányítsa az Evervideót bármely `rtsp://` URL-re és azonnal lejátssza. Kiváló biztonsági kamerákhoz, IPTV streamekhez, kaputelefon kamerákhoz, babaőrőkhöz és hasonló élő forrásokhoz.

**S3-kompatibilis objektumtároló:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces és bármely más S3-API végpont.

**Eszközön lévő könyvtárak:** a Fotók könyvtár (összes videó, képernyőfelvételek, fotoalbumok) és a Music alkalmazás könyvtára (Albumok, Műfajok, Lejátszási listák) — mindkettő a Médiakönyvtárban jelenik meg, így nem kell semmit másolnia.

**Helyi hálózat felfedezése:** az Elérhető eszközök szakasz automatikusan felsorolja az összes Bonjour / mDNS szolgáltatást a Wi-Fi hálózaton — Plex, Jellyfin, Emby szerverek, Synology, QNAP, AirPort útválasztók csatolt meghajtókkal, Apple Time Capsule — így IP-cím beírása nélkül csatlakozhat.

Minden kapcsolat a szolgáltatás hivatalos SDK-ját vagy nyílt protokollját használja, ahol elérhető OAuth-alapú engedélyezéssel. Több fiókot csatlakoztathat ugyanahhoz a szolgáltatáshoz (például két Google Drive fiókot, vagy egyszerre Plex és Jellyfin szerverekat) és böngészheti őket egymás mellett a Felhőtárhely szakaszban.

## Biztonság és adatvédelem

Az Evervideo csak hivatalos SDK-kat és biztonságos kapcsolatokat használ a csatlakoztatott felhőszolgáltatásokkal való interakcióhoz. Bejelentkezési neve és jelszava nem érhető el az alkalmazás számára — minden átvitel TLS-titkosított.

Amikor megadja bejelentkezési nevét és jelszavát, az alkalmazás megmutatja a felhőszolgáltató által megadott hivatalos jogosultságkezelési oldalt, és a teljes jogosultságkezelési folyamat az alkalmazáson kívül zajlik. A felhőszolgáltató ezután egy hitelesítési tokent küld az alkalmazásnak a sikeres engedélyezés után, és ezt a tokent használják az API-hívásokhoz.

A hitelesítési token egy digitális kulcs, amely lehetővé teszi harmadik fél alkalmazásoknak, hogy az Ön nevében interakcióba lépjenek a felhőtárhellyel. A token az eszközön tárolódik az Apple biztonságos rendszertároló helyen (Keychain), amely titkosítva van és eszköz PIN-kódjával vagy biometrikus zárral védett. A csatlakoztatott felhőszolgáltatásokból fájlokat tölthet le az eszközére; ezek a fájlok az alkalmazás Dokumentumok könyvtárába kerülnek és bármikor eltávolíthatók a beépített fájlkezelővel.

Az alkalmazás nem oszt meg semmilyen információt a csatlakoztatott felhőfiókokból az Everappz-dzal, hirdetőkkel vagy harmadik felekkel. Bármikor visszavonhatja a felhőfiókjához való hozzáférést a böngészőben a fiókbeállítások oldalának megnyitásával.

## Hitelesítési token visszavonása

Egy hitelesítési token visszavonásához jelentkezzen be felhőfiókjába egy webböngészőben, és navigáljon a biztonsági vagy csatlakoztatott alkalmazások oldalra. Ott megtalálhatja az összes harmadik fél alkalmazást, amely csatlakoztatva van a felhőfiókjához, és eltávolíthatja bármelyiket, amelyet már nem kíván használni. A Google-fiókokra vonatkozó részletes utasítások [itt](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) találhatók.

Az alkalmazáson belül is leválaszthatja a felhőfiókot — amikor ezt megteszi, a hitelesítési token azonnal törlődik az eszközéről. Ha eltávolítja az alkalmazást az eszközéről, az összes letöltött adat és hozzáférési token automatikusan törlődik.

## Felhőtároló leválasztása vagy konfiguráció módosítása

- **Felhőtároló lehetőségek elérése** — keresse meg a csatlakoztatott szolgáltatást a Fájlok lap **Felhőtárhely** szakaszában.
- **Érintse meg a „..." gombot** a szolgáltatás neve mellett a további lehetőségek megnyitásához:
  - **Átnevezés** — változtassa meg a felhőszolgáltatás nevét a listában való megjelenítéshez.
  - **Beállítások** — módosítsa a konfigurációt vagy a hitelesítési adatokat. Néha előfordulhat, hogy újra kell engedélyeznie a csatlakoztatott felhőszolgáltatást, ha a hitelesítési token lejárt.
  - **Leválasztás** — teljesen megszakítja az alkalmazás és a felhőszolgáltatás közötti kapcsolatot. Ez eltávolít minden videót, amely ehhez a szolgáltatáshoz van társítva a médiakönyvtárból, de érintetlenül hagyja őket a szerveren.

## Csatlakozás számítógéphez vagy NAS-hoz

Csatlakoztathatja számítógépét, személyes NAS-ját vagy más hálózati eszközét SMB, WebDAV, FTP / FTPS, SFTP, NFS vagy DLNA protokollon keresztül. Ez a legegyszerűbb módja annak, hogy egy meglévő otthoni médiakönyvtárat — legyen az Mac-en, Windows PC-n, Synologyn, QNAP-en, Apple Time Capsule-on vagy WD My Cloud Home-on — az Evervideóba hozzon anélkül, hogy bármit másolna.

### Csatlakozás számítógéphez SMB-n keresztül

- Érintse meg a **Csatlakozás felhőtárhelyhez → SMB** lehetőséget.
- Adja meg a számítógép IP-címét és a megosztott mappa nevét `smb://computer-ip-address/shared-folder-name` formátumban.
- Válassza ki a protokollverziót: **Auto**, **SMB1** vagy **SMB2**.
- Adja meg bejelentkezési nevét és jelszavát (ha szükséges).
- Érintse meg a **Kész** lehetőséget.

Ha a kapcsolat sikeres, a megosztás megjelenik a Felhőtárhely szakaszban. A Mac vagy PC SMB-n keresztüli csatlakoztatásának teljes oktatóanyaga [itt](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) érhető el.

### Csatlakozás NAS-hoz WebDAV-on keresztül

Minden lépés ugyanaz, mint az SMB esetén, kivéve az URL mezőt. Használja a `http://server-name` vagy `https://server-name` formátumot, ha a szerver támogatja az SSL-t. A WebDAV együttműködik Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home és bármely más WebDAV végponttal rendelkező szerverrel.

A WebDAV-ról szóló teljes oktatóanyag [itt](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) érhető el.

### Csatlakozás DLNA / UPnP-n keresztül

Osszon meg egy médiakönyvtárat a Windows PC-jén vagy NAS-án DLNA / UPnP protokollon keresztül, és érje el azt az Evervideón belül az [itt](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) leírtak szerint. A DLNA széles körben támogatott, de csak lejátszást vagy letöltést tesz lehetővé — DLNA szerverre nem tölthet fel fájlokat és nem hozhat létre új mappákat.

### Csatlakozás FTP, FTPS vagy SFTP protokollon

Az Evervideo támogatja a klasszikus fájlátviteli protokollokat is. FTP vagy FTPS szerverre való csatlakozáshoz érintse meg a Csatlakozás felhőtárhelyhez → FTP lehetőséget, adja meg az állomás URL-jét `ftp://server-name` formátumban (vagy `ftps://server-name` titkosított kapcsolathoz), adja meg bejelentkezési nevét és jelszavát, majd érintse meg a Kész lehetőséget. Az SFTP (SSH fájlátviteli protokoll) esetén válassza az SFTP lehetőséget, és adjon meg jelszót vagy SSH kulcspárt.

### Csatlakozás NFS-megosztáshoz

Az Evervideo NFS (hálózati fájlrendszer) támogatást is tartalmaz — hasznos Linux gazdagépekhez, BSD szerverekhez és NAS-eszközökhöz, amelyek inkább NFS-en keresztül teszik elérhetővé a videokönyvtárakat, mint SMB-n. Válassza az NFS-t a Csatlakozás felhőtárhelyhez menüben, adja meg a szerver címét és az exportált útvonalat, majd érintse meg a Kész lehetőséget.

## Plex médiaserver csatlakoztatása

Az Evervideo közvetlenül csatlakozhat egy Plex médiaserverhez, és böngészheti a Filmek, Tévésorozatok és Otthoni videók könyvtárait. Érintse meg a Csatlakozás felhőtárhelyhez → Plex lehetőséget, jelentkezzen be Plex-fiókjával, válasszon ki egy szervert, és a könyvtár megjelenik a felhőszolgáltatások mellett. Az ugyanazon helyi hálózaton lévő Plex-szerverek az Elérhető eszközök szakaszban is automatikusan felderíthetők.

## Jellyfin vagy Emby szerver csatlakoztatása

Mind a Jellyfin (nyílt forráskódú) mind az Emby (kereskedelmi) médiaszerverek natívan működnek az Evervideóban. Érintse meg a Csatlakozás felhőtárhelyhez → Jellyfin vagy Emby lehetőséget, adja meg a szerver URL-jét (általában valami hasonló `http://server-ip:8096`) és hitelesítési adatait, és könyvtára készen áll a streamelésre.

## Subsonic vagy Navidrome szerver csatlakoztatása

Az Evervideo a Subsonic API-t használja, ami azt jelenti, hogy működik a Subsonic-szal, a Navidrome-mal és minden más Subsonic-kompatibilis szerverrel — beleértve az Airsonicot, Funkwhale-t, Gonicot, Logitech Media Servert (LMS) és az Ampache-t. Érintse meg a Csatlakozás felhőtárhelyhez → Subsonic lehetőséget, adja meg a szerver URL-jét és hitelesítési adatait, és a könyvtár megjelenik a Felhőtárhely szakaszban.

## RTSP stream csatlakoztatása (IP kamerák, élő TV, IPTV)

Az Evervideo natív RTSP-támogatással rendelkezik, így bármely RTSP forrásra ráirányíthatja — biztonsági kamerák, kaputelefon kamerák, IPTV-szolgáltatók, babaőrők, közvetítési feedek — és az Evervideo élőben lekéri és dekódolja a streamet. Érintse meg az Online linkek → Link hozzáadása lehetőséget, illessze be a teljes URL-t (`rtsp://camera-ip:port/stream-path`), adja meg a bejelentkezési nevet és jelszót, ha szükséges, majd érintse meg a Kész lehetőséget.

## Csatlakozás S3-kompatibilis objektumtárolóhoz

Önhosztoló és profi felhasználóknak, akik felhőobjektum-tárolást használnak, az Evervideo S3-kompatibilis összekötőt tartalmaz. Érintse meg a Csatlakozás felhőtárhelyhez → S3 tároló lehetőséget, majd adja meg a végpont URL-jét, régiót, hozzáférési kulcsot, titkos kulcsot és bucket nevet. Ez működik az AWS S3-mal, Backblaze B2-vel, Wasabi-val, Cloudflare R2-vel, MinIO-val, DigitalOcean Spaces-szel és bármely más S3-API végponttal.

## Elérhető eszközök

Ez a szakasz megjeleníti a helyi hálózaton lévő összes eszközt, amelyhez Bonjour / mDNS felfedezés révén csatlakozhat az Evervideóból — Plex, Jellyfin, Emby szerverek, Synology, QNAP, AirPort útválasztók csatolt meghajtókkal, Apple Time Capsule stb. A kapcsolat létrehozásához:

- Görgessen az Elérhető eszközök szakaszhoz a Fájlok lapban.
- Érintse meg azt az eszközt, amelyhez csatlakozni kíván.
- Ha szükséges, adja meg bejelentkezési adatait a kapcsolat befejezéséhez.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo elérhető eszközök a helyi hálózaton" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

A Wi-Fi Drive lehetővé teszi fájlok vezeték nélküli átvitelét számítógépéről iOS-eszközére bármely asztali böngészőn, Finderen vagy Fájlkezelőn keresztül. Az eszközének és számítógépének ugyanazon a Wi-Fi hálózaton kell lenniük.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Drive engedélyezése

- A Fájlok lapon görgessen a Felhőtárhely → Csatlakozás Wi-Fi-n keresztül lehetőséghez a Wi-Fi Drive főképernyő megnyitásához.
- (Opcionális) Állítson be felhasználónevet és jelszót a beágyazott webszerver számára.
- Érintse meg a Wi-Fi Drive indítása lehetőséget.

### A Wi-Fi Drive elérése számítógépen

- Nyisson meg egy webböngészőt a számítógépen (Chrome, Firefox, Safari stb.).
- Adja meg az alkalmazás által megjelenített URL-t.
- Húzza és ejtse fájljait a számítógépről a weboldalra — megkezdik az iOS-eszközre való átvitelt.

A Wi-Fi Drive-ot közvetlenül a **Finderben** is csatlakoztathatja macOS-en (Ugrás → Csatlakozás szerverhez…) vagy a Fájlkezelőben Windows-on (Hálózati meghajtó leképezése…), és iPhone-ját vagy iPadját rendszeres hálózati meghajtóként kezelheti.

Részletes utasítások [itt](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) érhetők el.

## iTunes / Finder fájlmegosztás

Az iTunes fájlmegosztás (macOS Catalina és újabb rendszereken Finder fájlmegosztás) lehetővé teszi fájlok átvitelét Lightning vagy USB-C kábelen keresztül. Csatlakoztassa az eszközt, nyissa meg a Findert Macon (vagy az iTunes-t Windowson), keresse meg az Evervideót az alkalmazások listájában, és másolja a fájlokat a megosztott mappájába.

## USB flash meghajtó vagy SD kártya csatlakoztatása

Csatlakoztasson USB-meghajtót vagy SD-kártyát iPhone-jához, iPadjéhez vagy Macjéhez Lightning-USB / USB-C adapterrel vagy kártyaolvasóval. Nyissa meg a Fájlok → Fájlok ezen az iPhone-on → Mappa megnyitása lehetőséget, navigáljon a meghajtóhoz, és válasszon ki egy videófájlt vagy mappát. Az Evervideo közvetlenül a meghajtóról játssza le a fájlokat, anélkül, hogy azokat a belső tárolóba másolná — praktikus nagy 4K könyvtárakhoz.

## Mappaböngészés csatlakoztatott tárolókban

Érintsen meg bármely csatlakoztatott felhőszolgáltatást a fájlböngésző megnyitásához. A mappák videóbélyegképeket jelenítenek meg, ha rendelkezésre állnak, és egy videóra koppintva azonnal elindul a lejátszás, miközben a fájl többi részének streamelése a háttérben folytatódik.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo mappaböngészés csatlakoztatott tárolókban" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Gyors hozzáférés

A Gyors hozzáférés szakasz a Fájlok lap tetején található. Gyors hozzáférést biztosít a kedvenc és a legutóbb megnyitott fájlokhoz és mappákhoz — mind felhőszolgáltatásokból, mind az eszközön lévő tárolóból. Amikor megnyit egy fájlt vagy mappát a felhőből, az hozzáadódik a Legutóbb megnyitott listához. A mélyen beágyazott mappákat Kedvencekként jelölheti meg, hogy gyorsan hozzáférjen hozzájuk anélkül, hogy átásná magát a könyvtárstruktúrán.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo online linkek és gyors hozzáférés" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Fájlok ebben az alkalmazásban

Ez a szakasz az Evervideo sandboxolt Dokumentumok könyvtárában tárolt fájlokat és mappákat mutatja — mindent, amit letöltött a felhőből, átvitt Wi-Fi Drive-on keresztül, másolt Finder fájlmegosztással, vagy importált egy másik alkalmazásból.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo fájlok ebben az alkalmazásban" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Dokumentumok mappa

A Dokumentumok mappa a Fájlok ebben az alkalmazásban összes tartalmának gyökere. Almappákat hozhat létre, fájlokat nevezhet át, mozgathatja őket, és tetszés szerint csoportosíthatja.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo helyi fájlok — Dokumentumok mappa" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Fájlok ezen az iPhone-on / iPaden / Macon

Ez a szakasz az eszközön, de különböző alkalmazásokban lévő videókat mutatja. Importálhatja őket az Evervideóba a rendszer fájlválasztóval:

- Érintse meg a Fájlok megnyitása… lehetőséget adott fájlok kiválasztásához.
- Érintse meg a Mappa megnyitása… lehetőséget egy teljes mappa kiválasztásához.

Használhatja a Mappa csatlakoztatása lehetőséget is, hogy olvasási / írási hozzáféréssel rendelkező hivatkozást hozzon létre az eszközön lévő mappához — tökéletes iCloud Drive-on vagy csatlakoztatott USB-meghajtón lévő mappával való munkához, anélkül, hogy bármit másolna.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo fájlok ezen az eszközön" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Különleges mappák

A Fájlok lapon belül látni fog néhány különleges mappát, amelyeket az Evervideo automatikusan létrehoz és használ:

- **Letöltések** — minden felhőből letöltött fájl alapértelmezés szerint itt jelenik meg. Testreszabható a Beállítások → Fájlkezelő → Letöltött fájlok mentési helye menüpontban.
- **Lejátszó gyorsítótár** — a médialejátszó gyorsítótára. Alapértelmezés szerint a lejátszó letölti a következő videókat a folyamatos lejátszáshoz. Letilthatja a gyorsítótárat az alkalmazásbeállításokban, vagy egyszerűen törölheti ezt a mappát.
- **iCloud** — az ebben a mappában lévő fájlok szinkronizálódnak az összes, ugyanahhoz az iCloud-fiókhoz csatlakoztatott eszközön.
- **Offline mappák** — amikor egy mappát, lejátszási listát, albumot vagy műfajt offline elérhetőként jelöl meg, a fájlok letöltődnek ebbe a mappába.

## Felső eszköztár

A navigációs sáv alatt található felső eszköztár több műveletet kínál, amelyeket lefelé húzással mutathat vagy rejthet el:

- **Keresés** — keresés végrehajtása az aktuális mappán vagy szakaszon belül.
- **Lejátszás folytatása** — ha engedélyezve van a beállításokban, visszaállítja a lejátszási sort és az utolsó videópozíciót az aktuális mappához.
- **Összes lejátszása** — megvizsgálja az aktuális mappát és almappáit, és fájlokat ad hozzá a lejátszási sorhoz.
- **Összes keverése** — mint az Összes lejátszása, de keverés előtt.

## Mappa lehetőségek

Amikor megnyit egy mappát, érintse meg a **„..."** gombot a jobb felső sarokban a következő műveletekhez:

- **Kiválasztás** — fájlkiválasztási mód aktiválása.
- **Új mappa** — új mappa létrehozása az aktuális mappán belül.
- **Offline mód engedélyezése** — offline szinkronizálás bekapcsolása az aktuális mappához. Az online hozzáadott új fájlok automatikusan letöltődnek.
- **Fájlok feltöltése** — fájlok feltöltése az eszközről az online mappába.
- **Keresés** — keresés a mappán belül.
- **Rendezés** — fájlok rendezése név, méret, módosítás dátuma vagy metaadatok szerint.
- **Rács / Lista nézet** — váltás táblázatos nézet és bélyegkép nézet között. A bélyegkép nézet nagy videóborító előnézeteket mutat.

## Kiválasztási mód

Érintse meg a **„..."** gombot a jobb felső sarokban, és válassza a **Kiválasztás** lehetőséget a kiválasztási módba való belépéshez. Jelölőnégyzetek jelennek meg minden fájl és mappa mellett. Érintse meg egy vagy több elem kiválasztásához, majd végezzen kötegelt műveleteket: Következőnek lejátszás, Később lejátszás, Hozzáadás médiakönyvtárhoz, Hozzáadás lejátszási listához, Másolás, Feltöltés, Mozgatás, Átnevezés vagy Törlés.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo kiválasztási mód a fájlkezelőben" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Ha a csatlakoztatott felhőtárhelyet csak olvashatóként kívánja kezelni (a véletlen törlések megelőzése érdekében), engedélyezze a Beállítások → Fájlkezelő → Online fájlok szerkesztése → Ki lehetőséget az összes pusztító művelet elrejtéséhez a felhasználói felületről.

## Fájl műveletek

Érintse meg a **„..."** ikont egy fájlcím közelében a műveletek menü megjelenítéséhez:

- **Következőnek lejátszás** — a fájl beillesztése a lejátszási sor tetejére.
- **Később lejátszás** — a fájl hozzáfűzése a lejátszási sor aljára.
- **Hozzáadás médiakönyvtárhoz** — a fájl beépítése a médiakönyvtárba, Album és Műfaj szerint rendezve.
- **Hozzáadás lejátszási listához** — a fájl hozzáadása egy meglévő lejátszási listához vagy új létrehozása.
- **Címkék szerkesztése** — a beépített címkeszerkesztő megnyitása a metaadatok módosításához. Online fájlok esetén a fájl ideiglenesen letöltődik, szerkesztve, majd megerősítés után újra feltöltve.
- **Hozzáadás kedvencekhez** — a fájl hozzáadása a kedvencek listájához a gyors hozzáférés érdekében.
- **Letöltés** — a fájl vagy mappa letöltése az eszközre offline használathoz.
- **Átnevezés** — a fájl átnevezése közvetlenül a remote tárolón.
- **Mozgatás** — a fájl áthelyezése egy másik mappába a felhőtárhelyen belül.
- **Hozzáadás archívumhoz** — a fájl becsomagolása egyetlen ZIP fájlba (Premium funkció).
- **Megnyitás…-ban** — a fájl exportálása egy másik kompatibilis alkalmazásba a rendszer megosztási lapon keresztül.
- **Törlés** — a fájl végleges eltávolítása. **Ez a művelet nem vonható vissza.**

## Mappa műveletek

A felhőtárhelyén lévő minden mappához számos művelet érhető el a mappa neve melletti **„..."** ikon megérintésével.

- **Összes lejátszása** — az aktuális lejátszási sor cseréje a mappában lévő összes videóra.
- **Következőnek lejátszás / Később lejátszás** — a teljes mappa hozzáadása a sorhoz.
- **Hozzáadás médiakönyvtárhoz** — a mappa tartalmának beépítése a médiakönyvtárba.
- **Hozzáadás lejátszási listához** — a teljes mappa hozzáadása egy lejátszási listához.
- **Hozzáadás kedvencekhez** — a mappa hozzáadása a kedvencekhez.
- **Offline mód engedélyezése** — az egyszerű letöltésen túl ez folyamatosan figyeli a mappát az új fájlok szempontjából, és automatikusan letölti azokat, amint megjelennek online.
- **Letöltés** — a mappa összes tartalmának letöltése az eszközre offline hozzáféréshez.
- **Átnevezés / Mozgatás** — a mappa átnevezése vagy áthelyezése a remote tárolón.
- **Hozzáadás archívumhoz** — a mappa tartalmának ZIP fájlba csomagolása (Premium funkció).
- **Törlés** — a mappa és tartalmának végleges eltávolítása. **Ez a művelet nem vonható vissza.**

## Átviteli sor

A Fájlok lap jobb felső sarkában található egy **Átvitelek** gomb (egy forgó nyilakból álló ikon). Érintse meg az Átviteli sor megnyitásához — az összes aktív letöltés és feltöltés listája az összes forrásból, valós idejű folyamat, sebesség és ETA per fájl.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo fájlátviteli sor" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Szüneteltetheti, folytathatja, megismételheti a sikertelen átviteleket, átrendezheti az elemeket adott letöltések prioritásának meghatározásához, vagy egyenként törölheti azokat. Beállíthatja az átviteli sor sebességét (maximális párhuzamos feladatok), a hálózati típust (csak Wi-Fi vagy Wi-Fi + Mobiladat) és a háttérben történő átviteleket a Beállítások → Fájlkezelő menüpontban.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo műveletek a fájlátviteli soron" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offline mód és szinkronizált offline mappák

Az offline mód egy hasznos funkció, amely lehetővé teszi kedvenc videóinak megtekintését még akkor is, ha nincs internetkapcsolat. Amikor engedélyezi az offline módot bármely mappához, lejátszási listához, albumhoz vagy műfajhoz, a gyűjteményen belüli összes fájl automatikusan letöltődik az eszközére offline lejátszáshoz. Megjelennek az Offline mappák szakaszban.

Amikor új fájlokat ad hozzá a remote szerverhez, azok is automatikusan letöltődnek — így az offline gyűjtemény naprakész marad anélkül, hogy bármit kellene tennie. A manuális újraszinkronizáláshoz érintse meg a három pontot egy offline mappa jobb felső sarkában, és válassza a Szinkronizálás lehetőséget.

Beállíthatja a szinkronizálási időközt a Beállítások → Fájlkezelő → Szinkronizált offline mappák → Időköz menüpontban.

Részletes utasítások [itt](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/) érhetők el.

## Személyre szabás

A Beállítások → Személyre szabás menüpontban konfigurálhatja a Fájlok lap megjelenítését:

- **Fájlok képernyő stílusa** — Egyszerű menü (közvetlenül a mappalistát mutatja) vagy Csoportosított menü (tartalom csoportosítása kategóriák szerint — Gyors hozzáférés, Különleges mappák, Felhőtárhely stb.).
