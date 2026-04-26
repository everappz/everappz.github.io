---
title: "Hogyan importáljon M3U lejátszási listát az Evermusicbe és a Flacboxba"
date: 2024-01-31
description: "Ismerje meg, hogyan importálhat M3U, M3U8 és CUE lejátszási lista fájlokat felhőből, helyi tárolóból vagy eszközről az Evermusicbe és a Flacboxba."
keywords: ["evermusic", "flacbox", "lejátszási lista", "m3u", "m3u8", "cue", "importálás", "zenei alkalmazás"]
tags: ["evermusic", "importálás", "lejátszási listák", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Összefoglalás:** Az Evermusic és a Flacbox támogatja az M3U, M3U8 és CUE lejátszási lista fájlok importálását felhőtárolóból, helyi alkalmazásfájlokból vagy eszközéről. Lépjen a Lejátszási listák > Továbbiak > Lejátszási lista importálása menüpontra, válasszon forrást, válassza ki a fájlt, és az alkalmazás automatikusan létrehozza a lejátszási listát.

Az M3U, ami az MP3 URL vagy Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator rövidítése, egy számítógépes fájlformátum, amelyet multimédiás lejátszási listákhoz használnak. Az egyik fő felhasználási területe az egyetlen bejegyzésű lejátszási lista fájlok létrehozása, amelyek internetes streamekre mutatnak. Ezek a fájlok kényelmes hozzáférést biztosítanak a streaming tartalmakhoz, és gyakran használják letöltéshez, e-mailezéshez és internetes rádió hallgatásához.

Széles körű használata ellenére nincs formális specifikáció az M3U formátumhoz; de facto szabvánnyá vált. Egy M3U fájl lényegében egy egyszerű szöveges fájl, amely meghatározza egy vagy több médiafájl helyét. A kódolástól függően "m3u" vagy "m3u8" kiterjesztéssel mentik. A fájl minden bejegyzése egy médiafájl helyét adja meg, ami lehet abszolút helyi elérési út, az M3U fájl helyéhez viszonyított helyi elérési út vagy URL. A bejegyzéseket sortörések választják el, egyes eszközök CR LF formátumú sortöréseket igényelnek.

Ezenkívül az M3U fájlok tartalmazhatnak "#" karakterrel kezdődő megjegyzéseket. A kiterjesztett M3U-ban a "#" kiterjesztett M3U direktívákat vezet be, amelyek támogathatnak kettősponttal ":" lezárt paramétereket.

Az Evermusic és Flacbox alkalmazásainkban M3U fájl importálási funkciót valósítottunk meg, kiküszöbölve a manuális lejátszási lista létrehozás szükségességét. Ez az útmutató végigvezeti Önt a lejátszási listák importálásán felhőtárolóból, helyi fájlokból vagy eszközén lévő fájlokból közvetlenül az alkalmazásba.

Először navigáljon a 'Lejátszási listák' részhez. Ezután érintse meg a jobb felső sarokban található 'Továbbiak' gombot. A megjelenő menüből válassza a 'Lejátszási lista importálása' lehetőséget.

![lejátszási lista importálása művelet](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

A következő képernyőn válassza ki a fájl helyét. A támogatott lehetőségek:

- Csatlakoztatott felhőtároló;
- Fájlok az alkalmazásban;
- Fájlok az eszközén;

![fájl helye kiválasztása](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Válasszuk ki a csatlakoztatott felhőtárolót és nyissuk meg a lejátszási lista fájlt tartalmazó mappát. A támogatott lejátszási lista fájlkiterjesztések közé tartozik az M3U, M3U8 és CUE. Válassza ki a lejátszási lista fájlt és érintse meg a 'Kész' gombot a kiválasztás megerősítéséhez.

![M3U fájl kiválasztása](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Az alkalmazás elemzi a lejátszási lista fájlt és létrehozza a számok listáját. Ezután megkeresi ezeket a fájlokat a tárolón és összeállít egy végleges lejátszási listát, amelyet importál a zenei könyvtárba. Elengedhetetlen, hogy az M3U/CUE fájl tartalmazza a médiafájlok helyes elérési útjait, és a fájloknak ezeken az elérési utakon kell lenniük a tárolón.

![importált lejátszási lista](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Az alkalmazás relatív elérési utakat és abszolút fájl URL-eket egyaránt támogat.

Például:

Lejátszási lista relatív elérési utakkal:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Lejátszási lista abszolút URL-ekkel:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Ha az alkalmazáson belül található lejátszási lista fájlt importál (Helyi fájlok rész), nincs szükség további lépésekre.

Ha azonban az eszközén található lejátszási listát szeretné importálni a rendszer fájlválasztójával, van egy fontos szempont, amelyet szem előtt kell tartani.

Biztonsági házirendek miatt az alkalmazás csak ahhoz a fájlhoz férhet hozzá, amelyet a rendszer fájlválasztójával kiválaszt. A lejátszási lista fájl azonban tartalmazhat hivatkozásokat más médiafájlokra az eszközén. Az eszközéről történő lejátszási lista importáláshoz ki kell választania egy mappát, amely tartalmazza a lejátszási lista fájlt és az összes hozzá kapcsolódó médiafájlt. Ebben az esetben az alkalmazás átvizsgálja a kiválasztott mappát, megtalálja a lejátszási lista fájlt, felépíti a számsort és importálja a zenei könyvtárba.

Ezenkívül egyszerre több lejátszási listát is importálhat a "További műveletek" gomb megérintésével és a "Lejátszási listák importálása mappából" kiválasztásával. Az alkalmazás ezután átvizsgálja a mappa tartalmát, megtalálja a támogatott lejátszási lista fájlokat és importálja őket a könyvtárba.

## Gyakran ismételt kérdések

{{% details title="Milyen lejátszási lista formátumokat támogat az Evermusic és a Flacbox?" closed="true" %}}
Mindkét alkalmazás támogatja az M3U, M3U8 és CUE lejátszási lista fájlformátumokat. Ezek lefedik a zenelejátszók és médiaszoftverek által használt leggyakoribb lejátszási lista szabványokat.
{{% /details %}}

{{% details title="Importálhatok lejátszási listákat felhőtárolóból?" closed="true" %}}
Igen. Lejátszási lista fájlokat importálhat bármely csatlakoztatott felhőtároló szolgáltatásból, beleértve a Google Drive-ot, Dropboxot, OneDrive-ot és WebDAV szervereket.
{{% /details %}}

{{% details title="Miért hiányoznak egyes számok az importálás után?" closed="true" %}}
A lejátszási lista fájlnak tartalmaznia kell a médiafájlok helyes elérési útjait, és ezeknek a fájloknak a megadott helyeken kell létezniük a tárolón. Ellenőrizze, hogy az M3U vagy CUE fájlban lévő fájl elérési utak megfelelnek-e a tényleges fájl helyeknek.
{{% /details %}}

{{% details title="Importálhatok egyszerre több lejátszási listát?" closed="true" %}}
Igen. Használja a További műveletek gombot és válassza a "Lejátszási listák importálása mappából" lehetőséget. Az alkalmazás átvizsgálja a mappát az összes támogatott lejátszási lista fájl után és egy lépésben importálja őket.
{{% /details %}}

{{% details title="Manuálisan kell létrehoznom a lejátszási listákat?" closed="true" %}}
Nem. Az importálási funkció kiküszöböli a manuális lejátszási lista létrehozást. Egyszerűen irányítsa az alkalmazást a meglévő M3U, M3U8 vagy CUE fájlra, és az automatikusan létrehozza a lejátszási listát.
{{% /details %}}
