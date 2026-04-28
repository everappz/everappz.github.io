---
title: "Teljes hallgatási előzményeinek exportálása az Evermusicból és Flacboxból a Last.fm-re"
date: 2024-01-30
description: "Ismerje meg, hogyan exportálhatja zenei előzményeit az Evermusicból és Flacboxból, és hogyan töltheti fel a Last.fm-re CSV fájlok és a Last.fm Scrubbler eszköz segítségével Windowson."
keywords: ["evermusic", "flacbox", "lastfm", "zenei előzmények", "scrobbling", "számok exportálása", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "legutóbbiak", "lastfm", "exportálás", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Összefoglaló:** Exportálja hallgatási előzményeit az Evermusicból vagy Flacboxból CSV fájlként, majd töltse fel a Last.fm-re az ingyenes Last.fm-Scrubbler-WPF eszközzel Windowson. Az automatikus scrobbling natívan is elérhető mindkét alkalmazásban.

**Frissítés:** Az automatikus scrobbling most már elérhető! Tudjon meg többet itt: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

A scrobbling egy egyszerű módja annak, hogy automatikusan elmentse az éppen hallgatott dal alapvető adatait, mint a cím és az előadó, egy online szolgáltatásba. Később áttekintheti hallgatási előzményeit.

A [Last.fm](https://www.last.fm/home), amelyet az Audioscrobbler nevű zenei ajánlórendszer működtet, ingyenesen kínálja ezt a szolgáltatást. Részletes profilt hoz létre zenei ízléséről azáltal, hogy rögzíti a hallgatott számokat, legyen szó internetes rádióállomásokról, számítógépéről vagy különböző hordozható zenei eszközökről. Később meglátogathatja a weboldalt, hogy ajánlásokat kapjon új előadókra vagy albumokra, amelyek megfelelnek zenei ízlésének.

Feltöltheti hallgatási előzményeit a [Last.fm](http://Last.fm)-re az Evermusic és Flacbox alkalmazásokból egy ingyenes eszközzel, és mi végigvezetjük a folyamaton.

Nyissa meg az alkalmazás 'Zenekönyvtár' részét, és görgessen a 'Gyors hozzáférés' részhez. Koppintson a 'Legutóbbiak' menüpontra.

![zenekönyvtár képernyő](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

A 'Legutóbbiak' képernyőn koppintson a 'Több' gombra a jobb felső sarokban a 'További műveletek' menü aktiválásához. Koppintson a 'Dallista exportálása' menüpontra.

![legutóbbiak képernyő](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

A 'Fájlformátum kiválasztása' képernyőn lehetősége van kiválasztani a célfájl formátumát. Elérhető lehetőségek - CSV, TXT, M3U.

![fájlformátum kiválasztása képernyő](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Ez a vesszővel elválasztott értékeket jelenti, tökéletes az adatok rendezett táblázatos formátumba szervezéséhez. A célfájlban olyan paramétereket talál, mint az Előadó neve, Album neve, Szám neve, Időbélyeg (mikor hallgatta a számokat), Album előadója neve és Szám időtartama.

TXT: Itt egy egyszerű szöveges fájlról beszélünk. Egyszerű és közvetlen, olyan paraméterekkel, mint az Előadó neve, Album neve, Szám neve és Időtartam.

M3U: Ez a formátum lényegében a lejátszási listák létrehozásának szabványa. Nagyszerű, mert exportálhatja dallistáját és élvezheti számait bármilyen eszközön, még ha nincsenek is meg az eredeti fájlok (feltéve, hogy az abszolút URL opciót választja a médiafájlokhoz). A kimeneti fájlban olyan paramétereket talál, mint az Időtartam, Előadó neve, Szám neve és Médiafájl helye.

Feladatunkhoz a CSV kiválasztása a helyes út. Ezt a fájlt az ingyenes Last.fm-Scrubbler-WPF szoftverrel fogjuk használni hallgatási előzményeink feltöltéséhez a [Last.fm](http://Last.fm) szolgáltatásra. Egyszerűen válassza a CSV-t és nyomja meg az 'Exportálás' gombot.

![exportálás befejezve képernyő](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Az exportálás befejezése után egyszerűen koppintson a 'Fájl megjelenítése' gombra, és az alkalmazás megmutatja a létrehozott fájlt a dokumentumok mappájában. Ezután koppintson a 'További műveletek' gombra a fájlnév mellett, és válassza a 'Megnyitás itt' opciót a menüből. Következő lépésünk az exportált fájl másolása az asztali számítógépre. Ezt egyszerűen megteheti az AirDrop opció kiválasztásával a 'Megnyitás itt' menüből.

![további műveletek az exportált fájlhoz](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Ezután egy ingyenes nyílt forráskódú [Last.FM](http://Last.FM) klienst fogunk használni, amely csak Windows platformon érhető el. Ez a kliens lehetővé teszi hallgatási előzményeinek hatékony frissítését a [Last.FM](http://Last.FM)-en az imént exportált CSV fájl segítségével.

Ha jelenleg nem Windows számítógépet használ, ne aggódjon. Hozzáférhet ehhez a klienshez a VirtualBox telepítésével Mac-re és a hivatalos Windows fejlesztői környezet képfájl használatával.

Íme, amit tennie kell:

- Telepítse a VirtualBoxot a következő linkről: [VirtualBox letöltés](https://www.virtualbox.org/wiki/Downloads)

- Töltse le és telepítse a Windows fejlesztői környezetet erről a linkről: [Windows fejlesztői környezet](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Windows számítógépén (vagy VirtualBox alkalmazásban Windows Development képpel) töltse le és telepítse a [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF)-t - ingyenes nyílt forráskódú szoftver elérhető a GitHubon. Az 1.28-as verziót teszteltük, amelyet innen tölthet le: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Last.fm-Scrubbler-WPF letöltési oldal](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Az 'Assets' részben koppintson a [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) linkre a telepítési archívum letöltéséhez. Csomagolja ki a letöltött fájlt és nyissa meg a kicsomagolt mappát.

- FONTOS

Ez az alkalmazás még béta állapotban van. Az alkalmazás készítői nem végeztek sok tesztelést. Azt javasolják, hogy először próbáljon meg egy tesztfiókra scrobblálni, és nézze meg, hogy a scrobblálni kívánt dolgok megfelelően működnek-e. Különösen, ha egyszerre sok számot scrobblál. Kérjük, legyen óvatos fiókjaival.

Futtassa a Last.fm-Scrubbler-WPF.exe fájlt

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Az alkalmazás fő képernyőjén egyszerűen koppintson a 'Nincs bejelentkezve' feliratra, amely a bal alsó sarokban található, a 'Fiók hozzáadása' képernyő aktiválásához.

![fiók hozzáadása képernyő](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Adja meg bejelentkezési adatait.

![bejelentkezési adatok megadása képernyő](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Koppintson a 'Bejelentkezés' gombra fiókja hozzáadásához.

![Koppintson a Bejelentkezés gombra fiókja hozzáadásához.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Nyissa meg a 'File Parse Scrobbler' fület a CSV fájl importálásának megkezdéséhez az Evermusic alkalmazásból.

![Nyissa meg a File Parse Scrobbler fület a CSV fájl importálásának megkezdéséhez az Evermusic alkalmazásból.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Válassza a 'Parser: CSV' lehetőséget és koppintson a 'Beállítások' gombra.

A következő képernyőn kiválaszthatja a paraméterek sorrendjét a CSV fájlban.

Az egyes mezők idézőjelbe zárhatók, és idézőjelbe KELL zárni őket, ha a mező tartalmazza valamelyik beállított elválasztó karaktert. Például:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Tehát hagyja az összes beállítást alapértelmezetten, az egyetlen dolog, amit meg kell változtatnia, az a jelölőnégyzet engedélyezése a 'Has Fields Enclosed In Quotes' mezőben.

Koppintson a 'Mentés és bezárás' gombra a módosítások alkalmazásához.

![válassza ki a paraméterek sorrendjét a CSV fájlban.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

A fájl elemzés scrobbling két módot kínál. A 'Scrobbling Mode' legördülő listával változtathatók.

Normál mód: Ebben a módban a számok az elemzett scrobble időbélyegével lesznek scrobblálva. Csak a 14 napnál újabb scrobble-ok scrobblálhatók.

Importálás mód: Ebben a módban a számok a 'Befejezési idő' és az egyes számok közötti kiválasztott időtartam alapján kiszámított időbélyeggel lesznek scrobblálva. Ez lehetővé teszi a számok scrobblálását akkor is, ha az elemzett scrobble időbélyege régebbi 14 napnál. Ezért a CSV fájl első (legfelső) száma a 'Befejezési idővel' lesz scrobblálva.

Válasszon egy korábban létrehozott CSV fájlt az Evermusic alkalmazásból a 'File:' mezőben és koppintson a 'Parse' gombra. Néhány esetben hibaüzenetet láthat, amely szerint egyes scrobble-ok nem elemezhetők. Ez rendben van, ha vannak számok hiányos metaadatokkal, mint az Előadó neve.

![egyes scrobble-ok nem elemezhetők](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Koppintson az 'Összes kijelölése' gombra az összes elemzett szám kiválasztásához.

![Koppintson az Összes kijelölése gombra az összes elemzett szám kiválasztásához.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Koppintson az 'Előnézet' gombra a szerverre küldendő összes változás ellenőrzéséhez.

![Koppintson az Előnézet gombra a szerverre küldendő összes változás ellenőrzéséhez.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Koppintson a 'Scrobble' gombra az összes változás feltöltéséhez a szerverre.

![Koppintson a Scrobble gombra az összes változás feltöltéséhez a szerverre.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Korábban a Last.fm-Scrubbler-WPF-nek nem volt napi scrobble korlátja. Ez most megváltozott, mivel egyes emberek a Scrubblert annyi szám scrobblálására használták, hogy az problémákat okozott a Last.fm oldalon. A scrobble korlát jelenleg napi 2800 scrobble. Ha ennél többet próbál scrobblálni, hibaüzenetet kap. Tervek vannak egy 'scrobble sor' hozzáadására, így ha 2800-nál több számot kell scrobblálnia, azok sorba kerülnek és egy idő után automatikusan scrobblálódnak. A felhasználó kiválasztási nézetben ellenőrizheti, hány scrobble maradt.

Miután az összes rekord sikeresen feltöltődött a szerverre, az alkalmazás ablakának alján egy üzenetet fog látni, amely megerősíti: 'A kiválasztott számok sikeresen scrobblálva.'

![A kiválasztott számok sikeresen scrobblálva.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Most megnyithatja profilját a [Last.fm](http://Last.fm) oldalon és ellenőrizheti az összes változást.

![profilja a Last.fm oldalon](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Gyakran ismételt kérdések

{{% details title="Scrobblálhatok automatikusan CSV fájlok exportálása nélkül?" closed="true" %}}
Igen. Mind az Evermusic, mind a Flacbox most támogatja az automatikus Last.fm scrobblálást. Lásd az útmutatót: [Hogyan scrobbláljon a Last.fm-re](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Mi van, ha a CSV-mben 14 napnál régebbi számok vannak?" closed="true" %}}
Használja az Importálás módot a Last.fm-Scrubbler-WPF-ben. Újraszámítja az időbélyegeket a Befejezési időből, lehetővé téve a számok scrobblálását az eredeti dátumtól függetlenül.
{{% /details %}}

{{% details title="Nincs Windows számítógépem. Használhatom még a Last.fm-Scrubblert?" closed="true" %}}
Igen. Telepítse a VirtualBoxot Mac-re és töltse le az ingyenes Windows fejlesztői környezet képet a Microsofttól. Futtassa a Last.fm-Scrubbler-WPF-t a virtuális gépen belül.
{{% /details %}}

{{% details title="Miért nem elemezhetők egyes scrobble-ok?" closed="true" %}}
A lényeges metaadatokkal (mint az előadó neve) nem rendelkező számok nem elemezhetők. Ez várható, és nem befolyásolja a fájl többi számát.
{{% /details %}}

{{% details title="Van napi scrobble korlát?" closed="true" %}}
Igen. A Last.fm-Scrubbler-WPF naponta legfeljebb 2800 scrobble-t engedélyez. Ha többet kell scrobblálnia, ossza el a folyamatot több napra.
{{% /details %}}
