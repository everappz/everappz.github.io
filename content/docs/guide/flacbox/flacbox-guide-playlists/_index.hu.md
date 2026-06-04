---
title: "Lejátszási listák"
date: 2020-02-01
description: "Ismerje meg, hogyan hozhat létre, importálhat, kezelhet és testreszabhat lejátszási listákat a Flacboxban iPhone-on, iPaden és Macon. Lejátszási listákat hozhat létre felhő- és helyi fájlokból, importálhat M3U / M3U8 / CUE formátumot, átrendezheti a dalokat, szerkesztheti a borítóképet, archiválhat ZIP formátumba, exportálhat M3U / CSV / TXT formátumba, és használhatja az offline módot."
keywords: [
  "Flacbox lejátszási listák", "M3U lejátszási lista importálás", "lejátszási lista kezelő",
  "lejátszási lista létrehozása iPhone-on", "audio lejátszási listák Flacbox",
  "egyéni lejátszási lista kép", "dalok törlése lejátszási listából",
  "lejátszási lista rendezés Flacbox", "VoiceOver lejátszási lista átrendezés",
  "Flacbox M3U export", "Flacbox CSV export", "Flacbox lejátszási lista archív",
  "Flacbox lejátszási lista offline mód", "Flacbox CUE importálás", "Flacbox duplikált dalok"
]
tags: ["útmutató", "flacbox", "lejátszási listák"]
readingTime: 7
---


A Lejátszási listák szekcióban hasznos eszközöket talál a zenegyűjtemények kezeléséhez. Ez a terület az összes lejátszási listát egy helyen jeleníti meg. A tetején van egy **"..."** gomb a navigációs sávban, amely megnyit egy menüt a különböző lejátszási lista opciókkal, plusz egy eszköztárat gyors műveletekkel mint Keresés, Összes lejátszása és Összes keverése. Minden lejátszási listának van saját **"..."** gombja a cím mellett, amely további opciókat kínál az adott lejátszási listához.

A Flacbox lejátszási listái tartalmazhatnak online felhőbeli zeneszámokat, offline letöltött fájlokat és az eszközön lévő helyi fájlokat — mind egy lejátszási listában — és zökkenőmentesen játsszák le azokat egymás után.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lejátszási listák főképernyő" image="/docs/guide/flacbox/img/playlists-main.webp" >}}
{{< /cards >}}

## Lejátszási lista létrehozása

Új lejátszási lista létrehozása egyszerű. Két lehetősége van: koppintson a **+** gombra, vagy koppintson a navigációs sáv jobb felső sarkában lévő **"..."** gombra és válassza az Új lejátszási lista lehetőséget. Adjon az lejátszási listának egy értelmes nevet, majd koppintson a Mentés gombra.

Ez megnyitja a Dalok hozzáadása párbeszédablakot, ahol kézzel kiválaszthatja az új lejátszási listájába felvenni kívánt számokat. A számok forrástípus szerint vannak kategorizálva:

- **Könyvtár** — a zenetárban már megtalálható számok.
- **Fájlok ebben az alkalmazásban** — az alkalmazás Dokumentumok mappájában lévő hangfájlok.
- **Fájlok ezen az eszközön** — az eszközön máshol található hangfájlok.
- **Kapcsolatok** — a csatlakoztatott felhőtárhelyeken lévő online fájlok.

Alapértelmezés szerint csak egyszer adhat hozzá egy számot egy lejátszási listához. Ha duplikátumokat szeretne engedélyezni, engedélyezze ezt a funkciót a Beállítások → Zenetár → Lejátszási listák → Duplikátumok a lejátszási listában → Engedélyezés menüpontban.

## Lejátszási lista importálása

A Flacboxban hozzáadtuk az M3U / M3U8 / CUE fájl importálást, hogy ne kelljen manuálisan újra létrehozni a lejátszási listákat más lejátszóról való váltás után.

Először menjen a Lejátszási listák szekcióba. Majd koppintson a jobb felső sarokban lévő Tovább gombra. A menüből válassza az Lejátszási lista importálása lehetőséget.

A következő képernyőn válassza ki a fájl helyét. A támogatott lehetőségek a következők:

- Csatlakoztatott felhőtárhelyek
- Alkalmazásban lévő fájlok
- Az eszközön lévő fájlok

Válasszon csatlakoztatott felhőtárhelyet és nyissa meg a lejátszási lista fájlt tartalmazó mappát. A támogatott lejátszási lista fájlkiterjesztések: M3U, M3U8 és CUE. Válassza ki a lejátszási lista fájlt és koppintson a Kész gombra a kiválasztás megerősítéséhez.

Az alkalmazás értelmezi a lejátszási lista fájlt, létrehozza a számok listáját és megkeresi azokat a tárhelyen, hogy összeállítson egy végleges lejátszási listát, amelyet aztán importál a zenetárba. Fontos: az M3U / CUE fájlnak tartalmaznia kell a médiafájlok helyes elérési útját, és a fájloknak valóban léteznie kell azon az elérési úton. Tudjon meg többet a lejátszási lista importálásról [itt](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Lejátszási lista részletei képernyő

Amikor megnyit egy lejátszási listát, megjelenik a Lejátszási lista részletei képernyő. A jobb felső sarokban találja a **"..."** gombot a lejátszási lista opcióival, és három gomb az aртвerk alatt: Keresés, Lejátszás folytatása, Összes lejátszása és Összes keverése. Van egy Offline mód jelölőnégyzet is az egész lejátszási lista offline szinkronizálásához.

- **Lejátszás folytatása** — visszaállítja az utolsó mentett lejátszási pozíciót ehhez a lejátszási listához.
- **Keresés** — keresést végez az aktuális lejátszási listán belül.
- **Összes lejátszása** — hozzáadja az aktuális lejátszási lista összes számát a lejátszósorhoz.
- **Összes keverése** — mint az **Összes lejátszása**, de megkeveri a számokat az audiojátszó sorhoz való hozzáadás előtt.
- **Offline mód** — letölti az összes számot ebből a lejátszási listából a helyi fájlokba. A lejátszási listához hozzáadott új elemek is automatikusan letöltődnek.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lejátszási lista részletei képernyő" image="/docs/guide/flacbox/img/playlist-details-screen.webp" >}}
{{< /cards >}}

## További műveletek egy lejátszási listához a Lejátszási listák képernyőn

Egy lejátszási lista műveleteihez a lejátszási lista cím melletti **"..."** gombra koppintva férhet hozzá. Elérhető műveletek:

- **Összes lejátszása** — hozzáadja a lejátszási lista számait egy új lejátszósorhoz.
- **Következőként lejátszik** — hozzáadja a lejátszási lista számait a meglévő lejátszósor tetejéhez.
- **Később lejátszik** — hozzáadja a lejátszási lista számait a meglévő lejátszósor aljára.
- **Kép szerkesztése** — megváltoztatja a lejátszási lista borítóképét.
- **Offline mód engedélyezése** — bekapcsolja az offline módot a lejátszási listához. A meglévő és az új számok automatikusan letöltődnek. Tudjon meg többet az offline módról [itt](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Dalok listájának exportálása** — exportálja ezt a lejátszási listát **M3U / M3U8 / CSV / TXT** formátumba.
- **Hozzáadás archívumhoz** — archiválja ezt a lejátszási listát (beleértve az m3u fájlt, albumborítót és az összes számot) egyetlen ZIP fájlba. Prémium funkció.
- **Dalok hozzáadása** — további dalok hozzáadása az aktuális lejátszási listához.
- **Átnevezés** — átnevezi a lejátszási listát.
- **Lejátszási lista törlése** — törli a lejátszási listát a zenetárból. **Ez a művelet nem vonható vissza.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox További műveletek a lejátszási listához a főképernyőn" image="/docs/guide/flacbox/img/more-actions-for-playlist-in-playlists-main-screen.webp" >}}
{{< /cards >}}

## További műveletek a Lejátszási lista részletei képernyőn

A jobb felső sarokban lévő **"..."** gombra koppintva férhet hozzá egy lejátszási lista műveleteihez. Elérhető műveletek:

- **Kiválasztás** — aktiválja a szám-kiválasztási módot, hasznos több szám törléséhez a lejátszási listából vagy sorrendjük megváltoztatásához.
- **Következőként lejátszik** — hozzáadja a lejátszási lista számait a meglévő lejátszósor tetejéhez.
- **Később lejátszik** — hozzáadja a lejátszási lista számait a meglévő lejátszósor aljára.
- **Dalok hozzáadása** — új dalok hozzáadása a lejátszási listához.
- **Dalok átrendezése** — manuálisan megváltoztatja a dalok sorrendjét a lejátszási listában húzás-és-ejtés segítségével.
- **Átnevezés** — átnevezi az aktuális lejátszási listát.
- **Kép szerkesztése** — megváltoztatja az aktuális lejátszási lista albumborítóját.
- **Dalok listájának exportálása** — exportálja ezt a lejátszási listát **M3U / M3U8 / CSV / TXT** formátumba.
- **Hozzáadás archívumhoz** — ZIP tömörítés az aktuális lejátszási listából beleértve az összes számot és az m3u fájlt.
- **Rendezés** — megváltoztatja a lejátszási lista számainak sorrendjét. Rendezési lehetőségek: **Dal cím, Dal szám, Album, Előadó, Album előadó, Műfaj, Zeneszerző, Értékelés, Év, Ütem per perc, Időtartam, Fájlnév, Fájl módosítási dátuma, Fájl létrehozási dátuma** és **Kézi**. A **Kézi** rendezési lehetőség lehetővé teszi a dalok kézi átrendezését húzás-és-ejtéssel.
- **Keresés** — megkeresi a megadott dalt az aktuális lejátszási listán.
- **Rács / Lista** — megváltoztatja a képernyő megjelenítési módját.
- **Lejátszási lista törlése** — törli a lejátszási listát a zenetárból. Ez a művelet nem törli a számokat a tárhelyről, de **nem vonható vissza**.

## Dalok sorrendjének megváltoztatása egy lejátszási listában

A lejátszási lista dalainak sorrendjét a jobb felső sarokban lévő **"..."** gombra koppintással és a **Kiválasztás** lehetőség választásával lehet megváltoztatni. Használja az átrendezés vezérlőt és a húzás-és-ejtés mozdulatokat az egyes számok felfelé vagy lefelé mozgatásához. Az átrendezés vezérlőre koppintva a számot a lista tetejére viszi. A kiválasztási módból való kilépéshez és a módosítások alkalmazásához koppintson a **Kész** gombra.

A hosszabb lejátszási listáknál egyszerűbb munkamenethez válassza a További műveletek → Dalok átrendezése lehetőséget a dedikált húzás-és-ejtés átrendezési módba való belépéshez.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Dalok átrendezése a lejátszási listában" image="/docs/guide/flacbox/img/playlist-details-rearange-songs.webp" >}}
{{< /cards >}}

## A lejátszási lista borítóképének megváltoztatása

A lejátszási lista borítóképének megváltoztatásához koppintson a jobb felső sarokban lévő **"..."** gombra és válassza a **Kép szerkesztése** lehetőséget. Válasszon képet az elérhető forrásokból (Fotók, Fájlok, felhőtárhelyek vagy a lejátszási lista egyik számából generált borítókép), majd erősítse meg a **Kész** gombra koppintással.

## Dalok hozzáadása egy lejátszási listához

Nyissa meg a lejátszási listát és koppintson a jobb felső sarokban lévő **"..."** gombra, majd válassza a **Dalok hozzáadása** lehetőséget a párbeszédablak megnyitásához. Válassza ki a felvenni kívánt számokat és erősítse meg a **Kész** gombra koppintással.

## Több dal törlése egy lejátszási listából

Nyissa meg a lejátszási listát, koppintson a jobb felső sarokban lévő **"..."** gombra és válassza a **Kiválasztás** lehetőséget a kiválasztási módba való belépéshez. Válassza ki a törölni kívánt számokat és koppintson a képernyő alján lévő **Törlés a lejátszási listából** gombra. Erősítse meg a **Kész** gombra koppintással.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Kiválasztási mód a lejátszási lista részletei képernyőn" image="/docs/guide/flacbox/img/selection-mode-playlist-details-screen.webp" >}}
{{< /cards >}}

## Szám opciók

A lejátszási lista minden számához elérhető egy műveletlista, amelyet a **"..."** gombra koppintással érhet el. Ha nem látja az összes műveletet, görgessen le azok megtekintéséhez. Törölheti a számot a lejátszási listából, letöltheti, szerkesztheti az audio tagokat és sok mást.

- **Következőként lejátszik** — hozzáadja a számot a lejátszósor tetejéhez.
- **Később lejátszik** — hozzáfűzi a számot a lejátszósor aljára.
- **Hozzáadás lejátszási listához** — hozzáadja a számot egy másik lejátszási listához.
- **Hozzáadás a kedvencekhez** — kedvencként jelöli a számot.
- **Letöltés** — offline elérhetővé teszi a számot.
- **Audio tagek szerkesztése** — megnyitja a beépített tag szerkesztőt a szám metaadatainak megváltoztatásához.
- **Megnyitás más alkalmazásban** — exportálja a számot és megnyitja egy másik alkalmazásban.
- **Megjelenítés mappában** — feltárja a hangfájl helyét.
- **Megjelenítés a Finderben** — Mac-ről importált fájlok esetén.
- **Törlés a lejátszási listából** — törli a számot a lejátszási listából.
- **Törlés a felhőszolgáltatásból** — törli a számot a lejátszási listából és a kapcsolódó felhőszolgáltatásból. **Ez a művelet nem vonható vissza.**
- **Törlés a zenetárból** — törli a számot a zenetárból, de a fájl a tárhelyen marad.

## Akadálymentesítés

A Flacbox teljesen hozzáférhető **VoiceOver** technológiával. Amikor a VoiceOver aktív, az alkalmazás az felhasználói felületet **Szöveges módra** fordítja, csak akadálymentes és hasznos elemeket jelenítve meg. A Szöveges módot a Beállítások → Akadálymentesítés → Szöveges mód menüpontban is aktiválhatja.

### VoiceOver-rel egy szám pozíciójának beállítása egy lejátszási listában

1. Nyisson meg egy lejátszási listát és koppintson a **Tovább** gombra.
2. Válassza a **Dalok sorrendjének módosítása** lehetőséget. A nézet szerkesztési módba vált.
3. Koppintson az átrendezés jelző ikonra a szám neve mellett, hogy fókuszt adjon neki.
4. Gyorsan **koppintson duplán** az átrendezés jelző ikonra. A második koppintásnál ne engedje fel az ujját — tartsa addig, amíg nem hall egy hangot, amely jelzi, hogy a cella készen áll az áthelyezésre.
5. Most már áthelyezheti a cellát az új pozíciójára.

A többi komponens a rendszer által biztosított VoiceOver mintákat használva az elvárásoknak megfelelően működik.
