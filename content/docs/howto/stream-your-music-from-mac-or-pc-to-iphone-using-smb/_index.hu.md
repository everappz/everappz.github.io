---
title: "Zenéd streamelése Macről vagy PC-ről iPhone-ra SMB használatával"
description: "Ismerd meg, hogyan streamelheted zenegyűjteményedet Macről vagy Windows PC-ről iPhone-ra vagy iPadre az Evermusic és az SMB protokoll segítségével. Egyszerű lépésről lépésre útmutató a csatlakozáshoz és a zene élvezetéhez szinkronizálás nélkül."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["zene streamelése Macről iPhone-ra", "SMB audio streaming iOS", "Evermusic SMB beállítás", "PC zene csatlakoztatása iPhone", "Mac zene megosztás iOS", "SMB Windows fájl streaming", "Evermusic PC mappa hozzáférés"]
---

{{< author-byline >}}


**Röviden:** Használd az Evermusic alkalmazást iPhone-hoz vagy iPadhez, hogy zenét streamelj a Macedről vagy Windows PC-dről a helyi hálózatodon keresztül SMB használatával. Nincs szinkronizálás, nincs másolás -- csak engedélyezd a fájlmegosztást a számítógépeden, csatlakozz az alkalmazásban és játszd le. A beállítás kevesebb mint 5 percet vesz igénybe.

Elmerülsz a zene tengerében a MAC-eden vagy PC-den, és gondtalanul szeretnéd élvezni az iPhone-odon vagy iPadeden? Ne keress tovább, mint az Evermusic. Az Evermusic segítségével hihetetlenül egyszerű csatlakoztatni a számítógépedet az SMB protokoll használatával és streamelni kedvenc dalaidat anélkül, hogy aggódnál az extra tárhely foglalása vagy a szinkronizálási problémák miatt. Íme egy lépésről lépésre útmutató a kezdéshez:

## 1. lépés: SMB protokoll engedélyezése a számítógépeden

![Evermusic - SMB támogatás - Mac megosztási képernyő](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Ha MAC-et használsz

- Nyisd meg a Rendszerbeállítások -> Megosztás menüt.
- Engedélyezd a Fájlmegosztás szolgáltatást.
- A "Megosztott mappák" részben add hozzá a zenei mappádat, válassz egy felhasználót és állítsd be a jogosultsági szinteket (Olvasás és írás vagy Csak olvasás).
- A nagyobb kényelem érdekében választhatod az "Mindenki: Csak olvasás" lehetőséget a zenei mappához, így könnyen hozzáférhető lesz az Evermusic-ban.
- Ne felejtsd el megjegyezni a számítógéped URL-jét (smb://192.168.xx.xx) a következő lépésekhez.

![Evermusic - SMB támogatás - Fájlmegosztás képernyő](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Érintsd meg a "Beállítások" gombot és engedélyezd a "Fájlok és mappák megosztása SMB használatával" opciót.
- Engedélyezd a "Windows fájlmegosztás" opciót az elérhető fiókokhoz.

![Evermusic - SMB támogatás - Fájlok és mappák megosztása képernyő](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Ha Windows PC-t használsz

![Evermusic - SMB támogatás - Fájlok megosztása Windowson](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Kattints jobb gombbal a zenei mappádra.
- Válaszd a "Tulajdonságok" lehetőséget.
- Nyisd meg a "Megosztás" fület.
- Kattints a "Megosztás..." gombra.
- Válaszd ki azokat a személyeket, akikkel meg szeretnéd osztani, és állítsd be jogosultsági szintjeiket.
- A MAC-hez hasonlóan választhatod a "Mindenki: Olvasás" lehetőséget a kiválasztott zenei mappához.
- Kattints a "Kész" gombra a beállítások mentéséhez.

![Evermusic - SMB támogatás - Megosztott mappa Windowson](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## 2. lépés: Számítógéped automatikus hozzáadása

- Most nyisd meg az Evermusic-ot és menj a "Kapcsolatok" fülre ("Hálózat" ha régebbi alkalmazásverziót használsz).
- Ha látod a számítógépedet az "Elérhető eszközök" ("Elérhető megosztások" ha régebbi alkalmazásverziót használsz) részben, és az előző lépésben a "Mindenki: Csak olvasás" lehetőséget választottad, egyszerűen érintsd meg a számítógépedet, és automatikusan csatlakozik.
- Ha ez nem történik meg, manuálisan is hozzáadhatod a számítógépedet.

![Evermusic - SMB támogatás - Fiók csatlakoztatása képernyő](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## 3. lépés: Számítógéped manuális hozzáadása

- Érintsd meg a "Felhőszolgáltatás csatlakoztatása" gombot ("Fiók hozzáadása" ha régebbi alkalmazásverziót használsz)
- Válaszd az "SMB" lehetőséget az elérhető szerverek listájából a következő képernyőn.
- Az "SMB" beállítások képernyőn:
  - Add meg a szerver URL-jét a megosztott mappa elérési útjával. Megadhatod a szerver nevét vagy a szerver IP-címét. Például:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Add meg a felhasználónevedet és jelszavadat, vagy hagyd üresen ezeket a mezőket, ha az előző lépésben a "Mindenki: Csak olvasás" lehetőséget választottad.
  - A "WORKGROUP" mező opcionális, és akkor kell használni, ha Active Directory tartományod van.

![Evermusic - SMB támogatás - Hitelesítő adatok megadása képernyő](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Miután csatlakoztattad az SMB fiókodat, megjelenik a "Felhőszolgáltatások" ("Fiókok") részben. Nyisd meg a csatlakoztatott fiókot megérintésével, navigálj a zenei mappához, és érintsd meg bármelyik hangfájlt a lejátszó elindításához.

![Evermusic - SMB támogatás - Csatlakoztatott mappa megnyitása képernyő](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Élvezd zenegyűjteményedet zökkenőmentesen iPhone-odon vagy iPadeden az Evermusic segítségével.

![Evermusic - SMB támogatás - Hanglejátszó képernyő](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## 4. lépés: SMB2 megkerülő megoldás

Ha problémákat tapasztalsz a mappák böngészésével vagy a speciális karaktereket (például ü, ö, é) tartalmazó fájlok lejátszásával, ez az SMB2 protokollhoz kapcsolódhat. Aktívan dolgozunk a probléma megoldásán.

Ideiglenes megoldásként próbáld meg engedélyezni az SMB 1-et a szervereden és az alkalmazás beállításaiban. Alternatívaként csatlakozhatsz az SMB szerveredhez a rendszer fájlmegnyitó menüjén keresztül. Így teheted meg:

1. Navigálj a "Helyi fájlok" részhez.
2. Görgess le a "Fájlok ezen az eszközön" részhez és érintsd meg a "Fájlok megnyitása..." vagy "Mappák megnyitása..." lehetőséget.
3. Keresd meg a szerveredet és válaszd ki a szükséges fájlokat vagy mappákat.
4. Érintsd meg a "Megnyitás" gombot a választás megerősítéséhez.

## 5. lépés: WebDAV megkerülő megoldás

Ezenkívül megpróbálhatsz csatlakozni a NAS-odhoz WebDAV vagy DLNA protokollokkal, ha támogatottak.

Ezeket a lépéseket követve megkerülheted a fájlnevekben lévő speciális karakterekkel kapcsolatos problémákat, és továbbra is élvezheted médiafájljaidat.

U.i. Hangfájlokat is átvihetsz a MAC/PC-dről az iPhone-odra az iTunes fájlmegosztás segítségével, és lejátszhatsz helyi hangfájlokat. Tudj meg többet erről a funkcióról útmutatónkban: [Hogyan játszd le az iTunes fájlokat iPhone-on](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Gyakran ismételt kérdések

{{% details title="Streamelhetek zenét a PC-mről az iPhone-omra iTunes nélkül?" closed="true" %}}
Igen. Az Evermusic SMB-n keresztül csatlakozik a PC-dhez a helyi Wi-Fi hálózatodon. Nincs szükség iTunes-ra. Csak engedélyezd a fájlmegosztást a PC-den és csatlakozz az alkalmazásban.
{{% /details %}}

{{% details title="Az SMB streaming mobiladatot használ?" closed="true" %}}
Nem. Az SMB a helyi Wi-Fi hálózatodon keresztül működik. Nincs szükség internetkapcsolatra vagy mobiladatra.
{{% /details %}}

{{% details title="Milyen hangformátumokat támogat az Evermusic SMB-n keresztül?" closed="true" %}}
Az Evermusic támogatja az MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC és más általános hangformátumokat. A fájlok közvetlenül az SMB megosztásról játszódnak le.
{{% /details %}}

{{% details title="Streamelhetek zenét NAS-ról az iPhone-omra?" closed="true" %}}
Igen. Ha a NAS-od támogatja az SMB-t (a legtöbb igen, beleértve a Synology, QNAP és WD My Cloud eszközöket), ugyanezekkel a lépésekkel csatlakozhatsz hozzá.
{{% /details %}}

{{% details title="Be kell kapcsolva hagynom a számítógépemet streamelés közben?" closed="true" %}}
Igen. Mivel az Evermusic közvetlenül a számítógépedről streameli a fájlokat, annak bekapcsolva és ugyanahhoz a hálózathoz csatlakozva kell lennie, mint az iPhone-od.
{{% /details %}}

{{% details title="Van fájlméret-korlát az SMB streamelésnél?" closed="true" %}}
Nem. Az Evermusic bármilyen méretű fájlt streamel SMB-n keresztül. A nagy veszteségmentes fájlok (FLAC, WAV) probléma nélkül működnek.
{{% /details %}}
