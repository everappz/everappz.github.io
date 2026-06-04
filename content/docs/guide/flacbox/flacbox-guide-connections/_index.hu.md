---
title: "Kapcsolatok"
date: 2020-02-01
description: "Ismerje meg, hogyan csatlakoztathat felhőszolgáltatásokat és NAS-eszközöket a Flacboxhoz. Streamelje a nagy felbontású zenét az iCloud Drive-ból, a Dropboxból, a Google Drive-ból, az OneDrive-ból, a MEGA-ból, a Boxból, a pCloudból, a Synology Drive-ból, a Yandex Diskből és másokból. Használja az SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder fájlmegosztást és USB flash meghajtókat."
keywords: [
  "Flacbox felhő beállítás", "Google Drive csatlakoztatása Flacboxhoz", "SMB zene streaming",
  "WebDAV iOS lejátszó", "DLNA zene app", "NAS audio streaming", "Wi-Fi Drive iPhone",
  "fájlok átvitele iPhone-ra", "Flacbox iTunes fájlmegosztás", "NAS csatlakoztatása iPhone-hoz",
  "Synology Drive zene app", "QNAP zene app", "Bluesound zene app",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm scrobbling zene app",
  "iXpand Flash Drive zene", "USB DAC iPhone"
]
tags: ["útmutató", "flacbox", "kapcsolatok", "felhő", "NAS"]
readingTime: 12
---


Ezen a képernyőn csatlakoztathatja az összes zenéjét tároló forrást. Integrálhat népszerű felhőszolgáltatásokat, mint a Dropbox, a Google Drive, az iCloud Drive, az OneDrive, a MEGA, a Box, a pCloud, a Yandex Disk, a Synology Drive és még sok más, valamint Mac-et, PC-t vagy NAS-t szabványos protokollokon keresztül. Akár a Dropbox-hoz hasonló streaming-barát szolgáltatáson, akár személyes NAS-on (Synology, QNAP, Buffalo, Apple Time Capsule vagy WD My Cloud Home) él a gyűjteménye, a Flacbox egyetlen képernyőről mindenhez csatlakozik.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Kapcsolatok képernyő" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Csatlakozás felhőtárhelyhez

- Nyissa meg a **Kapcsolatok** lapot.
- Válassza a **Csatlakozás felhőtárhelyhez** lehetőséget a menüből.
- Válasszon felhőtárhely-szolgáltatást a listából.
- Adja meg a hitelesítő adatait a felhőszolgáltató által biztosított hivatalos engedélyezési oldalon, majd koppintson a **Kész** gombra.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Felhőtárhely-szolgáltatás hozzáadása" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Ha problémákba ütközik, ellenőrizze az internetkapcsolatát és a bejelentkezési adatait / jelszavát. Az alkalmazás prémium verziójában korlátlan számú szolgáltatást adhat hozzá; az ingyenes verzió legfeljebb három szolgáltatást támogat.

## Támogatott felhőtárhely-szolgáltatások, médiaszerverek és protokollok

A Flacbox kivételesen széles körű forrásokat támogat a zenéjéhez. Az alábbiak mindegyike egyetlen **Csatlakozás felhőtárhelyhez** képernyőről működik.

**Személyes felhőtárhely:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Saját hosztolt szerverek:** Plex · Jellyfin · Emby · Subsonic (és minden Subsonic-kompatibilis szerver — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (és ownCloud a közös API-n keresztül) · Synology Drive · QNAP.

**NAS és fájlmegosztási protokollok:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH fájlátviteli protokoll, jelszavas vagy nyilvános kulcsos hitelesítés) · NFS · DLNA / UPnP (lejátszás és letöltés).

**S3-kompatibilis objektumtárhely:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces és bármilyen más S3 API-végpont.

**Helyi hálózat felfedezése:** Az Elérhető eszközök szakasz automatikusan listázza az összes Bonjour / mDNS-szolgáltatást a Wi-Fi hálózaton, így IP-cím beírása nélkül csatlakozhat.

Minden kapcsolat a szolgáltatás **hivatalos SDK-ját vagy nyílt protokollját** használja, ahol lehetséges OAuth-alapú engedélyezéssel. Ugyanannak a szolgáltatásnak több fiókját is csatlakoztathatja (például két Google Drive fiókot, egy személyes és egy munkahelyi Dropboxot, vagy egy Plex és egy Jellyfin szervert), és egymás mellett böngészheti őket a Kapcsolatok képernyőn.

## Biztonság és adatvédelem

Csak hivatalos SDK-kat és biztonságos kapcsolatokat használunk a csatlakoztatott felhőszolgáltatásokkal való interakcióhoz. A bejelentkezési neve és jelszava nem érhető el az alkalmazás számára — minden átvitel TLS-titkosított.

Amikor beírja a bejelentkezési adatait és jelszavát, az alkalmazás a felhőszolgáltató által biztosított hivatalos engedélyezési oldalt jeleníti meg, és a teljes engedélyezési folyamat az alkalmazáson kívül zajlik. A felhőszolgáltató ezután sikeres engedélyezés után auth-tokent küld az alkalmazásnak, amelyet API-hívásokhoz használnak.

Az auth-token egy digitális kulcs, amely lehetővé teszi harmadik felek alkalmazásainak, hogy az Ön nevében interakcióba lépjenek a felhőtárhellyel. A token az Apple biztonságos rendszertárhelyén (Keychain) tárolódik az eszközön, amely titkosítva van és az eszköz jelszókódjával vagy biometrikus zárolásával védett. Fájlokat tölthet le a csatlakoztatott felhőszolgáltatásokból az eszközére; ezek a fájlok az alkalmazás Dokumentumok könyvtárába kerülnek, és bármikor eltávolíthatók a beépített fájlkezelővel.

Az alkalmazás nem oszt meg semmilyen információt a csatlakoztatott felhőfiókjaiból az Everappz-zel, hirdetőkkel vagy harmadik felekkel. A felhőfiókjához való hozzáférést bármikor visszavonhatja a fiókbeállítások oldalának webböngészőben való megnyitásával.

## Auth-token visszavonása

Egy auth-token visszavonásához jelentkezzen be felhőfiókjába webböngészőben, és navigáljon a biztonsági vagy csatlakoztatott alkalmazások oldalára. Ott megtalálhatja az összes felhőfiókjához csatlakoztatott harmadik féltől származó alkalmazást, és eltávolíthat bármelyiket, amelyet már nem szeretne használni. Részletes utasítások a Google-fiókokhoz [itt](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) érhetők el.

A felhőfiókot magán az alkalmazáson belül is lecsatlakoztathatja — amikor ezt teszi, az auth-token azonnal törlődik az eszközéről. Ha eltávolítja az alkalmazást az eszközéről, az összes letöltött adat és hozzáférési token automatikusan törlődik.

## Felhőtárhely lecsatlakoztatása vagy konfiguráció módosítása

- **Felhőtárhely-beállítások elérése** — keresse meg a csatlakoztatott szolgáltatást a **Kapcsolatok** képernyőn.
- **Koppintson a "..." gombra** a szolgáltatás neve mellett a további lehetőségek megnyitásához:
  - **Átnevezés** — módosítsa a felhőszolgáltatás nevét, ahogy a listában megjelenik.
  - **Beállítások** — módosítsa a konfigurációt vagy a hitelesítési adatokat. Néha szükség lehet a csatlakoztatott felhőszolgáltatás ismételt engedélyezésére, ha az engedélyezési token lejárt.
  - **Kibővítés megszüntetése** — teljesen szakítsa meg a kapcsolatot az alkalmazás és a felhőszolgáltatás között. Ez eltávolítja az adott szolgáltatáshoz társított összes dalt az alkalmazás zenetárából, de a szerveren érintetlenül hagyja azokat.

## Csatlakozás számítógéphez vagy NAS-hoz

Csatlakoztathatja számítógépét, személyes NAS-át vagy más hálózati eszközöket az SMB, DLNA vagy WebDAV protokollok használatával. Ez a legegyszerűbb módja egy meglévő otthoni zenegyűjtemény — legyen az Mac-en, Windows PC-n, Synology dobozban vagy NAS-on — Flacboxba való behozatalának másolás nélkül.

## Csatlakozás számítógéphez SMB-vel

- Koppintson a **Csatlakozás felhőtárhelyhez → SMB** lehetőségre.
- Adja meg a számítógép IP-címét és megosztott mappa nevét az URL-mezőben a következő formátumban: `smb://computer-ip-address/shared-folder-name`.
- Válassza ki a protokoll verzióját: **Auto**, **SMB1** vagy **SMB2**.
- Adja meg a bejelentkezési nevet és jelszót (ha szükséges).
- Koppintson a **Kész** gombra.

Ha a kapcsolat sikeres, a **Felhőtárhely** szakaszban látni fogja a csatlakoztatott tárhelyet. A Mac vagy PC SMB-vel való csatlakoztatásának teljes útmutatója [itt](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) érhető el.

## Csatlakozás NAS-hoz WebDAV-on keresztül

Minden lépés ugyanaz, mint az SMB esetén, kivéve az URL-mezőt. Az URL-nek `http://server-name` vagy `https://server-name` formátumban kell lennie, ha a szerver támogatja az SSL-t. A WebDAV működik a **Synology, QNAP, Nextcloud, ownCloud** és sok más szerverrel — mindenhol, ahol WebDAV-végpont elérhető.

A NAS WebDAV-on való csatlakoztatásának teljes útmutatója [itt](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) érhető el.

## Csatlakozás számítógéphez vagy NAS-hoz DLNA-n keresztül

Megoszthatja a Windows PC-n vagy személyes NAS-on tárolt zenegyűjteményt DLNA / UPnP protokollon keresztül, és [itt](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) leírt módon érheti el az alkalmazásban. A DLNA népszerű, széles körben támogatott protokoll, de csak zenék lejátszását vagy letöltését teszi lehetővé — DLNA szerverre nem tölthet fel fájlokat, és nem hozhat létre új mappákat.

## Csatlakozás NAS-hoz vagy szerverhez FTP, FTPS vagy SFTP protokollon

A Flacbox a klasszikus fájlátviteli protokollokat is támogatja. FTP vagy FTPS szerveren való csatlakozáshoz koppintson a **Csatlakozás felhőtárhelyhez → FTP** lehetőségre, adja meg a gazdagép URL-jét `ftp://server-name` formátumban (vagy `ftps://server-name` titkosított kapcsolathoz), adja meg a bejelentkezési adatait és jelszavát, majd koppintson a **Kész** gombra. **SFTP** (SSH fájlátviteli protokoll) esetén válassza az **SFTP** lehetőséget, és adjon meg jelszót vagy SSH kulcspárt. Mindkettő működik NAS-eszközökkel, Linux gazdagépekkel és bármilyen FTP / FTPS / SSH démonnal rendelkező szerverrel.

## Csatlakozás NFS-megosztáshoz

A Flacbox tartalmaz **NFS** (hálózati fájlrendszer) támogatást — hasznos Linux gazdagépek, BSD szerverek és NAS-eszközök számára, amelyek inkább NFS-en keresztül teszik elérhetővé a zenegyűjteményeket. Válassza az **NFS** lehetőséget a **Csatlakozás felhőtárhelyhez** menüben, adja meg a szerver címét és az exportált elérési utat, majd koppintson a **Kész** gombra.

## Plex Media Server csatlakoztatása

A Flacbox közvetlenül csatlakozhat egy Plex Media Serverhez, és Előadók, Albumok, Műfajok és Lejátszási listák szerint böngészheti zenegyűjteményét. Koppintson a **Csatlakozás felhőtárhelyhez → Plex** lehetőségre, jelentkezzen be Plex-fiókjával, válasszon egy szervert, és a könyvtár megjelenik a felhőszolgáltatások mellett. Az azonos helyi hálózaton lévő Plex szerverek az **Elérhető eszközök** szakaszban is automatikusan felfedezhetők.

## Jellyfin vagy Emby szerver csatlakoztatása

Mind a **Jellyfin** (nyílt forráskódú), mind az **Emby** (kereskedelmi) médiaszerverek natívan működnek a Flacboxban. Koppintson a **Csatlakozás felhőtárhelyhez → Jellyfin** vagy **Emby** lehetőségre, adja meg a szerver URL-jét (valami ilyesmi: `http://server-ip:8096`) és a hitelesítő adatait, és zenegyűjteménye készen áll a streamelésre. A Plexhez hasonlóan a helyi hálózaton lévő könyvtárak automatikusan megjelennek az **Elérhető eszközök** listában.

## Subsonic vagy Navidrome szerver csatlakoztatása

A Flacbox a Subsonic API-t használja, ami azt jelenti, hogy működik magával a **Subsonic**-cal, a **Navidrome**-mal és minden más Subsonic-kompatibilis szerverrel — beleértve az Airsonic-ot, Funkwhale-t, Gonic-ot, Logitech Media Servert (LMS) és Ampache-t. Koppintson a **Csatlakozás felhőtárhelyhez → Subsonic** lehetőségre, adja meg a szerver URL-jét és hitelesítő adatait, és a könyvtár megjelenik a Kapcsolatok képernyőn.

## Csatlakozás S3-kompatibilis objektumtárhelyhez

A Flacbox tartalmaz S3-kompatibilis csatlakozót. Koppintson a **Csatlakozás felhőtárhelyhez → S3 tárhely** lehetőségre, majd adja meg a végpont URL-jét, régiót, hozzáférési kulcsot, titkos kulcsot és a tároló nevét. Ez működik AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces és bármilyen más S3 API-végpontot elérhetővé tevő szolgáltatással.

## Elérhető eszközök

Ez a szakasz minden olyan eszközt megjelenít a helyi hálózaton, amelyhez a Bonjour-felfedezésen keresztül csatlakozhat a Flacboxból. Kapcsolat létrehozásához kövesse az alábbi lépéseket:

- Nyissa meg az alkalmazást, és menjen a Kapcsolatok alatt az **Elérhető eszközök** szakaszhoz.
- Koppintson arra az eszközre, amelyhez csatlakozni szeretne.
- Ha szükséges, adja meg a bejelentkezési adatait a kapcsolat befejezéséhez.

Ez a leggyorsabb módja SMB, WebDAV, DLNA-megosztás felfedezésének az otthoni hálózaton IP-cím manuális beírása nélkül.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Elérhető eszközök a helyi hálózaton" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

A Wi-Fi Drive egy kényelmes technológia, amely lehetővé teszi a vezeték nélküli fájlátvitelt a számítógépről iOS-eszközére bármilyen asztali böngészőn keresztül. A funkció hatékony használatához győződjön meg arról, hogy az eszköze és a számítógépe ugyanahhoz a Wi-Fi hálózathoz csatlakozik. Íme a Wi-Fi Drive használatának lépésenkénti útmutatója.

### Wi-Fi Drive engedélyezése

- Nyissa meg az alkalmazást, és menjen a **Kapcsolatok** lapra.
- Válassza a **Csatlakozás Wi-Fi-n keresztül** lehetőséget a Wi-Fi Drive főképernyőjéhez való hozzáféréshez.
- (Opcionális) Állítson be felhasználónevet és jelszót a beépített webkiszolgáló védelméhez.
- Koppintson a **Wi-Fi Drive indítása** gombra a Wi-Fi Drive engedélyezéséhez.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Drive elérése a számítógépen

- A számítógépén (asztali vagy laptop) nyisson meg egy webböngészőt (például Chrome-ot, Firefoxot vagy Safarit).
- A böngésző címsorában adja meg az alkalmazás által biztosított URL-t.

### Fájlok vezeték nélküli átvitele

Amint az iOS-eszközének megfelelő weboldal megnyílik a böngészőben, könnyen húzhat és ejthet fájlokat a számítógépéről a weboldalra. Az ejtett fájlok elkezdődnek átvitelre az iOS-eszközére, és elérhetők lesznek a Flacboxban.

A Wi-Fi Drive-ot közvetlenül a Finderben is csatlakoztathatja macOS-en (Ugrás → Csatlakozás szerverhez…) vagy a Fájlkezelőben Windows-on (Hálózati meghajtó hozzárendelése…), és úgy kezelheti iPhone-ját vagy iPadjét, mint egy hagyományos hálózati meghajtót.

Részletes utasítások a fájlok Wi-Fi Drive segítségével való vezeték nélküli átviteléhez [itt](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) érhetők el.

## iTunes / Finder fájlmegosztás

Az iTunes fájlmegosztás (macOS Catalina és újabb verziókon Finder fájlmegosztás) egy másik módja a fájlok számítógépről eszközre való átvitelének Lightning vagy USB-C kábel használatával.

- Csatlakoztassa az eszközt a számítógéphez kábellel, és futtassa a **Findert** Mac-en (vagy az **iTunes**-t Windows-on).
- Nyissa meg a **Helyek → Csatlakoztatott eszköze → Fájlok** részt, és keresse meg a Flacbox alkalmazást.
- Koppintson az alkalmazás ikonra az összes megosztott mappa megtekintéséhez.
- Másolja a fájlokat a számítógépről az eszközön lévő megosztott mappába húzással és ejtéssel.

Részletes utasítások a Finder fájlmegosztás használatához [itt](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) érhetők el.

## USB flash meghajtó csatlakoztatása

Ha SD-kártyája vagy USB-meghajtója van, csatlakoztathatja Lightning-USB / SD-kártyaolvasóval vagy USB-C meghajtóval (iPaden és iPhone 15 / 16 / 17 / Pro-n). Az alkalmazás támogatja az Apple tanúsított kártyaolvasókat és az iXpand Flash Drive-okat. iXpand Flash Drive esetén illessze be a Lightning-portba, és nyissa meg az alkalmazást — látni fogja a Külső eszköz csatlakoztatva üzenetet és az eszközinformációkat. Koppintson a flash meghajtó ikonra a zenei mappa eléréséhez, majd koppintson bármelyik hangfájlra a lejátszás megkezdéséhez.

Részletes utasítások arra vonatkozóan, hogyan csatlakoztathat USB flash meghajtót iPhone-jához és hallgathat zenét vagy kezelheti a rajta lévő fájlokat, [itt](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it) érhetők el.

## Fájlkezelő

Miután csatlakoztatott egy felhőtárhely-szolgáltatást, koppintson az ikonjára az összes elérhető fájl és mappa megtekintéséhez. A beépített fájlkezelővel dolgozhat ezekkel a fájlokkal — letölthet, átnevezhet, áthelyezhet, feltölthet, törölhet és még sok más műveletet végezhet. Amikor letöltést indít, a fájl megjelenik az átviteli sorban. Az átviteli sor megnyitásához menjen a Helyi fájlok lapra, és koppintson a forgó nyilak ikonra a bal felső sarokban. Az összes letöltött fájl és mappa elérhető a Helyi fájlok szakaszban.

## Felső eszköztár

A felső eszköztár, amely kényelmesen a navigációs sáv alatt található, számos hasznos műveletet kínál a könnyű hozzáférés érdekében. Egyszerű lefelé húzó mozdulattal megjelenítheti vagy elrejtheti.

- **Keresés** — gyors keresés az aktuális könyvtárban, megkönnyítve adott fájlok vagy mappák megtalálását.
- **Lejátszás folytatása** — ha engedélyezve van az alkalmazás beállításaiban, visszaállítja az audiojátszó sorát és az aktuális mappa utolsó média pozícióját. Praktikus módja a folytatásnak ott, ahol abbahagyta.
- **Összes lejátszása** — megvizsgálja az aktuális mappát és almappáit, majd az összes talált hangfájlt hozzáadja egy új lejátszósorhoz.
- **Összes keverése** — mint az Összes lejátszása, de a fájlokat kever, mielőtt hozzáadná az audiojátszó sorához.

## Mappa beállítások

Amikor megnyit egy mappát, a jobb felső sarokban lévő **"..."** gombra koppintva hasznos műveletek találhatók.

- **Kiválasztás** — aktiválja a fájlkiválasztási módot. Ez lehetővé teszi egy vagy több fájl kiválasztását a mappában és műveletek végrehajtását a teljes kijelölésen.
- **Új mappa** — új mappa létrehozása az aktuális mappában.
- **Offline mód engedélyezése** — kapcsolja be az offline módot az aktuális mappához. Az offline mód az egyszerű letöltésen túl aktívan figyeli a mappa változásait.
- **Fájlok feltöltése** — töltse fel a fájlokat az eszközéről az online mappába.
- **Keresés** — keressen megadott fájlokat az aktuális mappában.
- **Rendezés** — rendezze a fájlokat név, méret, módosítás dátuma szerint vagy metaadatok alapján.
- **Rács / Lista nézet** — váltson a táblázatos nézet és a bélyegkép nézet között.

## Online fájlok szerkesztése

Ha több fájlt kell kezelnie a felhőtárhelyen, használja a **Kiválasztás módot** a műveletek egyszerűsítéséhez:

- **Kiválasztás mód aktiválása** — koppintson a **"..."** gombra a jobb felső sarokban, és válassza a **Kiválasztás** lehetőséget.
- **Fájlok kiválasztása** — jelölőnégyzetek jelennek meg minden fájl és mappa mellett. Koppintson egy vagy több elem kiválasztásához.
- **Műveletek végrehajtása** — a fájlok vagy mappák kiválasztása után hozzáférhet a Következőként lejátszik, Később lejátszik, Hozzáadás a zenetárhoz, Hozzáadás lejátszási listához, Másolás, Feltöltés, Áthelyezés, Átnevezés és Törlés lehetőségekhez.

Ha inkább csak olvashatóként szeretné kezelni a csatlakoztatott felhőtárhelyet (a véletlen törlések megelőzése érdekében), engedélyezze a Beállítások → Fájlkezelő → Online fájlok szerkesztése → Ki lehetőséget az összes romboló művelet elrejtéséhez a felhasználói felületről.

## Fájl műveletek

Koppintson a fájl neve melletti **"..."** ikonra a műveletek menüjének megjelenítéséhez:

- **Következőként lejátszik** — a fájlt a lejátszósor tetejére illeszti.
- **Később lejátszik** — a fájlt a lejátszósor aljára fűzi.
- **Hozzáadás a zenetárhoz** — a fájlt beépíti a zenetárba, előadó, album, műfaj vagy szerző szerint rendezve.
- **Hozzáadás lejátszási listához** — a fájlt hozzáadja egy meglévő lejátszási listához vagy újat hoz létre.
- **Audio címkék szerkesztése** — megnyitja a beépített tagszerkesztőt a metaadatok módosításához.
- **Hozzáadás a kedvencekhez** — a fájlt hozzáadja a kedvencek listájához a gyors hozzáférés érdekében.
- **Letöltés** — letölti a fájlt vagy mappát az eszközére offline használatra.
- **Átnevezés** — a fájl átnevezése közvetlenül a távoli tárhelyen.
- **Áthelyezés** — a fájl áthelyezése a felhőtárhelyen belül más mappába.
- **Megnyitás más alkalmazásban** — a fájl exportálása egy másik kompatibilis alkalmazásba.
- **Törlés** — a fájl végleges eltávolítása a felhőtárhelyéről. **Ez a művelet nem vonható vissza.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox További műveletek a csatlakoztatott felhőtárhelyen lévő fájlhoz" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Ha a műveletek listája meghaladja a rendelkezésre álló képernyőterületet, egyszerűen görgessen le a műveletek menüjében a további lehetőségek eléréséhez.

## Mappa műveletek

A felhőtárhelyen lévő minden mappához számos művelet érhető el a mappa neve melletti **"..."** ikonra koppintva.

- **Összes lejátszása** — a kiválasztott mappa összes elemével helyettesíti az aktuális lejátszósorát.
- **Következőként lejátszik** — hozzáadja az egész mappát a lejátszósor tetejéhez.
- **Később lejátszik** — a mappa tartalmát hozzáfűzi a lejátszósor aljához.
- **Hozzáadás a zenetárhoz** — beépíti a mappa tartalmát a zenetárba.
- **Hozzáadás lejátszási listához** — hozzáadja az egész mappát egy lejátszási listához.
- **Hozzáadás a kedvencekhez** — a mappát hozzáadja a kedvencekhez a gyors hozzáférés érdekében.
- **Offline mód engedélyezése** — az egyszerű letöltésen túl folyamatosan figyeli a mappát új fájlok megjelenése esetén és automatikusan letölti azokat.
- **Letöltés** — letölti a mappa összes tartalmát az eszközére offline hozzáféréshez.
- **Átnevezés** — a mappa átnevezése közvetlenül a távoli tárhelyen.
- **Áthelyezés** — a mappa áthelyezése a felhőtárhelyen belül más helyre.
- **Archívum (ZIP)** — a mappa tartalmát egyetlen ZIP fájlba csomagolja (Prémium funkció).
- **Törlés** — a mappa és tartalmának végleges eltávolítása a felhőtárhelyéről. **Ez a művelet nem vonható vissza.**

## Gyors hozzáférés

A Gyors hozzáférés szakasz a képernyő tetején található. Gyors hozzáférést biztosít a csatlakoztatott felhőszolgáltatások kedvenc és nemrég megnyitott fájljaihoz. Amikor megnyit egy fájlt vagy mappát a felhőből, az hozzáadódik a Legutóbb megnyitott listához. A lista törléséhez nyissa meg a Legutóbbiakat, koppintson a További műveletek gombra, és válassza a Lista törlése lehetőséget.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Online hivatkozások és gyors hozzáférés" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Egyéb szolgáltatások

Ez a szakasz olyan extra funkciókat jelenít meg, amelyek javítják az élményt. Jelenleg az alkalmazás a **Last.fm** scrobbling-ot támogatja — csatlakoztatva a lejátszási statisztikáit automatikusan elküldi Last.fm-fiókjára. Részletes beállítási utasítások [itt](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm) érhetők el.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm csatlakoztatása" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
