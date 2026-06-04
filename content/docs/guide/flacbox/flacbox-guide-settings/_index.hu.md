---
title: "Beállítások"
date: 2020-02-01
description: "Fedezzen fel minden beállítást a Flacboxban — a lejátszási preferenciáktól az FFmpeg / rendszer hangmotoron, Hi-Res audio kimeneten, equalizer beállításokon, hangmagasság-korrektúrán, IO puffer időtartamán, metaadat szinkronizáláson, lejátszási lista vezérlésen, fájlátviteleken, kezdőképernyő widgeteken, Apple CarPlay-en, UI személyre szabáson, nyelven, jelszavin, biztonsági mentésen és visszaállításon, valamint Prémium frissítésen át."
keywords: [
  "Flacbox beállítások", "audiojátszó konfiguráció", "prémium frissítés Flacbox",
  "WiFi Drive", "metaadat szinkronizáció", "equalizer", "lejátszási sebesség",
  "lejátszási lista duplikátumok", "fájlkezelő beállítások", "offline zene szinkron",
  "audio tagok szerkesztő", "sötét mód", "vásárlás visszaállítása", "biztonsági mentés beállítások",
  "Flacbox widget beállítások", "Flacbox CarPlay beállítások",
  "Flacbox FFmpeg beállítások", "Flacbox mintavételezési frekvencia beállítások",
  "Flacbox hangmagasság-korrekció beállítások", "Flacbox IO puffer",
  "Flacbox jelszó", "Flacbox nyelv", "Flacbox személyre szabás",
  "Flacbox analitika"
]
tags: ["útmutató", "flacbox", "beállítások"]
readingTime: 16
---


A Beállítások képernyő a Flacbox vezérlőközpontja. Innen frissíthet Prémiumra, konfigurálhatja a hangmotort (rendszer kodekek vagy FFmpeg), kezelheti a zenetárat, beállíthatja a fájlkezelőt, testreszabhatja az audio tagok szerkesztőjét, engedélyezheti a Kezdőképernyő widgeteket és az Apple CarPlay-t, biztonsági másolatot készíthet az adatairól, és hozzáférhet a súgóhoz és jogi információkhoz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Beállítások főképernyő" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Frissítés Prémiumra

Frissítse az alkalmazást Prémium verzióra az összes korlát eltávolításához. Az alkalmazás ingyenes verziója egyszeri élettartamú alkalmazáson belüli vásárlást és két előfizetési lehetőséget (1 hónap és 1 év) kínál az összes korlátozás eltávolításához és a Prémiumra való frissítéshez.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Frissítés Prémiumra" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

A **Családi megosztás** engedélyezett minden vásárlásnál és terven, így a Prémium verziót megoszthatja legfeljebb öt családtaggal extra költség nélkül.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Prémium terv kiválasztása" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Tudjon meg többet a vásárlásokról és a Prémium verzióról: [Mi a különbség a Flacbox és a Flacbox Prémium között](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Vásárlások megosztása iOS és Mac között

Az élettartamú vásárlások és előfizetések meg vannak osztva iOS és Mac között, az iCloud segítségével szinkronizálva ezeket az információkat. Ha az iOS eszközén van a Prémium verzió, győződjön meg arról, hogy telepítve van a legújabb verzió és az iCloud engedélyezve van. Indítsa el az alkalmazást iOS-on és várjon egy percet, hogy a vásárlási információk feltöltődjenek az iCloudba.

Megpróbálhatja az alkalmazás beállításaiban a Vásárlások visszaállítása gombra koppintani is. Ezt követően telepítse a legújabb alkalmazásverziót az App Store-ból Macen és indítsa el az alkalmazást.

## Vásárlások visszaállítása új eszközön

A vásárlások új eszközön való visszaállításához használja a Vásárlások → Vásárlások visszaállítása menüt. Megjelenik a vásárlások listája. Ha nem látja az összeset, erősítse meg, hogy az eszköz ugyanahhoz az Apple ID-hoz van csatlakoztatva, amellyel a vásárlásokat végezte, és győződjön meg arról, hogy az iCloud engedélyezve van.

## Próbálja ki ingyenesen a Prémiumot

Frissíthet a Prémium verzióra ingyenesen, korlátozott ideig, ennek a menünek a segítségével.

## Vásárlások

Visszaállíthatja korábbi vásárlásait ebből a menüből. Ha aktiválási hibákba ütközik, próbálja engedélyezni az Alkalmazás indulásakor visszaállítandó vásárlások opciót.

## Szoftverfrissítés

Koppintson a Szoftverfrissítésre annak ellenőrzéséhez, hogy elérhető-e a Flacbox újabb verziója.

## Újdonságok

Ez a menü egy új verzió kiadása után érhető el. Összefoglalást mutat a legutóbbi frissítés változásairól és új funkcióiról.

## Audiojátszó

Ez a szekció konfigurálja az audiojátszót és az alapul szolgáló hangmotort, beleértve az FFmpeg / rendszer kodek választást és a Hi-Res audio kimenet beállításokat.

### Általános

- **Ismétlési mód** — válassza ki, hogyan viselkedjen az audiojátszó, amikor egy szám véget ér:
  - **Összes ismétlése** — újrajátssza az összes számot a sorban.
  - **Egy ismétlése** — csak az aktuális számot ismétli.
  - **Ismétlés leállítása** — szünetel a lejátszás, amikor az aktuális szám véget ér.
  - **Nincs ismétlés** — hagyja, hogy a sor végigmenjen ismétlés nélkül.
- **Keverési mód** — véletlenszerűsíti a számok sorrendjét. **Keverés ki** vagy **Keverés be** állítható.
- **Audio kodek** — válassza a lejátszáshoz használt hangmotort:
  - **System Codec + FFmpeg** — ahol lehetséges, előnyben részesíti a rendszer audio kodeket, javítva a kompatibilitást és stabilitást.
  - **FFmpeg** — az FFmpeg kodeket kényszeríti minden hangfájlra, feloldva a hangmagasság-korrekciót és az audio kimenet mintavételezési frekvenciát.
- **Audio kimenet mintavételezési frekvencia** — állítsa be a hangminőség optimalizálásához. Elérhető értékek: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** és **96 kHz**.
- **Audio kimenet csatornák száma** — Mono, Sztereó, Center / Left / Right, stb.
- **Audio kimenet preferált IO puffer időtartama** — konfigurálja a puffer időtartamát az audio lejátszáshoz.
- **Audio kimenet mód (csak iOS)** — konfigurálja a kevert audio kimenet módot. Részletes útmutató [itt](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Lejátszási pozíció mentése** — elmenti és visszaállítja a lejátszási pozíciót.
- **Audiojátszó állapot mentése** — megőrzi az audiojátszó állapotát az alkalmazás bezárása előtt.

### Személyre szabás

- **Audiojátszó képernyő stílus** — konfigurálja az elemek elhelyezkedését.
- **Albumborítók görgetési stílusa** — konfigurálja a preferált görgetési stílust.
- **További elemek** — extra elemek engedélyezése az audiojátszó képernyőn.
- **Főképernyő műveletek** — konfigurálja, mely gombok legyenek láthatók.
- **Lejátszásvezérlők a záróképernyőn** — válassza ki, mely vezérlők jelenjenek meg.
- **Idő kihagyása gombok** — válasszon idő intervallumot.

### Fájl betöltés

- **Előbetöltési idő** — állítsa be a pufferelési idő intervallumát.
- **Közvetlen URL használata** — ha engedélyezve van, közvetlen URL-t használ a dal betöltéséhez.

### Audio equalizer

Konfigurálja a 10 sávos audio equalizert. Részletes útmutató [itt](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Lejátszási sebesség

Állítsa be az audiojátszó lejátszási sebességét **0,02×-tól 3,00×-ig**.

### Hangmagasság-korrekció

Módosítsa a hangmagasság-korrekció beállításait. Az elérhető értékek tartománya **-1000-től +1000-ig** terjed.

### Lejátszási gyorsítótár

A lejátszósorban lévő dalokat automatikusan letöltik a gördülékeny lejátszás biztosításához. Beállíthatja a gyorsítótár méretét is.

### Alvásidőzítő

Aktiváljon egy időzítőt a lejátszás automatikus leállításához.

## Könyvtár

A zenetár beállításai — automatikus szinkronizálás, metaadat olvasás, albumborító betöltés, lejátszási listák, legutóbbiak és kedvencek — itt találhatók.

### Metaadat olvasás

A zenetárhoz számokat hozzáadva a **metaadat olvasó** munkába lép. Ez a háttérfolyamat beolvassa az összes metaadatot és szervezi azokat Előadó, Album, Műfaj és Zeneszerző szerint. Megadhatja a metaadat olvasás sebességét. Letilthatja a metaadat olvasót és fájlneveket jeleníthet meg a tag információk helyett.

**Normalizálás metaadat kódolás** engedélyezésekor az alkalmazás automatikusan normalizálja az összes dal metaadatának kódolását.

### Online szinkronizálás

Az automatikus online zene szinkronizálás automatikusan hozzáadja a csatlakoztatott felhőszolgáltatások számait a zenetárhoz. Az engedélyezéséhez nyissa meg a zenetár beállításait és válassza ki a szinkronizálási mappákat.

### Offline szinkronizálás

Konfigurálja az offline zene szinkronizálást. Ha egy online mappát offline elérhetőként jelöl meg, megjelenik itt. A tartalom letöltődik a **Helyi fájlok → Offline mappák** helyre.

### Személyre szabás

Konfigurálja a zenetár képernyő stílusát. Három lehetőség érhető el: **Egyszerű menü, Csoportosított menü, Füles menü**.

### Albumborítók

- **Hálózat típusa** — Wi-Fi vagy Wi-Fi és mobiladat.
- **Albumborítók betöltése online fájlokhoz** — beágyazott albumborítók betöltése.
- **Keresés a mappában** — ha nincs beágyazott borító, JPEG vagy PNG képeket keres ugyanabban a mappában.
- **Borítókép minősége** — válassza ki az albumborítók minőségét.
- **Megjelenítés mappában** — nyissa meg a gyorsítótárazott albumborítók mappáját.
- **Összes törlése** — törli a gyorsítótárazott albumborítókat.

### Lejátszási listák

Engedélyezze az azonos dal kétszeri hozzáadásának lehetőségét egy lejátszási listához. Alapértelmezés szerint ez az opció le van tiltva.

### Legutóbbiak

- **Lista törlése** — törli a nemrég lejátszott dalok teljes listáját.
- **Lista méretének módosítása** — állítsa be a listában megjelenő elemek számát.
- **Dalok listájának exportálása** — exportálja a nemrég lejátszott dalok listáját.

### Kedvencek

- **Egyidejű szerkesztés** — ha engedélyezve van, egy dal kedvencekhez való hozzáadása azt mind a zenetárban, mind a fájlok szekcióban egyszerre hozzáadja.
- **Lista törlése** — törli a kedvenc dalok teljes listáját.
- **Dalok listájának exportálása** — exportálja a kedvenceket.

### Zenetár törlése

Törli a zenetár adatbázisát. A tárhelyen lévő zenefájlok érintetlenek maradnak.

## Jelszó

Aktiválja a jelszó képernyőt az alkalmazásadatok védelmére 4 jegyű numerikus jelszóval.

## Fájlkezelő

A Fájlkezelő szekció szabályozza a fájlok átvitelét, tárolását és előnézetét.

### Fájlátvitelek

Válassza ki a hálózati preferenciát a fájlok letöltéséhez.

### Párhuzamos feladatok maximális száma

Állítsa be a párhuzamos letöltési szálak számát.

### Fájlátviteli feladatok

Megjeleníti az aktuálisan aktív feltöltési és letöltési feladatokat.

### Háttérben történő átvitelek

Lehetővé teszi a letöltéseket, miközben az alkalmazás a háttérben fut.

### Letöltött fájlok mentése

Válassza az alapértelmezett letöltési könyvtárat, vagy minden alkalommal kérje meg az alkalmazást.

### Szinkronizált offline mappák

Kezelje az offline szinkronizálást a kiválasztott mappákhoz. Tudjon meg többet az offline módokról [itt](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Időintervallum

Válassza meg, milyen gyakran szinkronizálódjanak az offline mappák.

### Teljes fájlnév megjelenítése

Mutassa a teljes fájlneveket, beleértve a kiterjesztéseket.

### Online fájlok szerkesztése

Tiltsa le az online fájlszerkesztést a csatlakoztatott felhőszolgáltatások csak olvasható módjára való váltáshoz.

### Fájlok másolása megnyitáskor

Adja meg, hogyan kezeli az alkalmazás a más alkalmazásokból importált fájlokat.

### Miniatűrök fájlokhoz

Kezelje és törölje a generált fájlminiatűröket.

### Ideiglenes fájlok törlése

Törölje az alkalmazás gyorsítótár mappáját.

## Audio tagok szerkesztő

Konfigurálja a beépített audio tagok szerkesztőjét.

### Albumborító méretezés

Válassza ki a méretezési módszert, amelyet az albumborító audio tagokba mentésekor használ.

### Online fájlok frissítése

Ha engedélyezve van, az alkalmazás automatikusan frissíti egy fájl metaadatait a felhőszerveren szerkesztés után.

### Fájl törlése online szerkesztés után

Válassza, hogy az alkalmazás törölje-e a letöltött másolatot az online fájl szerkesztésének befejezése után.

### Főképernyő gombok

Válassza ki, mely gombok jelenjenek meg az audio tagok szerkesztőjének főképernyőjén.

## Widgetek

Engedélyezze a widgeteket, hogy az alkalmazás frissítse a widget adatokat lejátszás közben. Widget frissítések további energiát igényelnek, ezért az alapértelmezett beállítás ki.

## CarPlay

Módosítsa a CarPlay beállításait itt.

### Rendezés

Konfigurálja a rendezési opciókat az összes CarPlay képernyőhöz.

### Tartalombetöltési korlát

Válassza, hogy az alkalmazás használjon-e lapozást a CarPlay képernyőn.

### Menüikonok átmenetes színe

Válassza ki a CarPlay kezdőképernyő színsémáját.

### Képek megjelenítése

Tiltsa le a képeket a CarPlay képernyőn a betöltési sebesség optimalizálásához.

### Lejátszás szüneteltetése csatlakozáskor

Engedélyezze ezt, hogy elkerülje a hirtelen hangos hangot CarPlay csatlakozáskor.

## Wi-Fi meghajtó

Aktiválja a **Wi-Fi meghajtót** a fájlok számítógépről való átviteléhez asztali böngésző, Finder vagy File Explorer segítségével. Részletes útmutató [itt](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Személyre szabás

Testreszabhatja a felhasználói felületet preferenciái szerint.

### Alkalmazásikon

Válasszon alternatív alkalmazásikont a kezdőképernyőjéhez (Prémium).

### Színséma

Válassza ki a felhasználói felület témáját és engedélyezze a sötét módot.

### Háttér stílus

Módosítsa az alkalmazás háttér stílusát. Jelenleg az egyetlen lehetőség az **Elmosódott albumborító**.

### Elemek megjelenése a listában

Állítsa be, hogyan jelenjenek meg az elemek a listákban.

### Tartalombetöltési korlát

Alapértelmezés szerint az alkalmazás lapozást használ a tartalombetöltés felgyorsításához.

### Helyi fájlok képernyő stílus

Módosítsa a **Helyi fájlok** szekció megjelenítési stílusát.

### Zenetár képernyő stílus

Testreszabja a **Zenetár** képernyő megjelenését.

### Audiojátszó képernyő stílus

Konfigurálja az **Audiojátszó** képernyő megjelenését.

### Helyi menü stílus

Válassza ki a helyi menü stílusát, amely megjelenik a **További műveletek** gombra koppintáskor.

## Ablak

Elérhető Macen. Konfigurálja az ablakhoz kapcsolódó preferenciákat.

## Képernyő

Válassza, hogy a képernyő aktív maradjon-e az alkalmazás használata közben.

## Akadálymentesítés

Aktiválja a **Szöveges módot** az összes kép elrejtéséhez a felhasználói felületen. A Szöveges mód automatikusan aktiválódik, amikor a VoiceOver aktív.

## Nyelv

Módosítsa az alkalmazás nyelvét és felülírja a rendszer alapértelmezettjét. A változás az alkalmazás teljes bezárása és újbóli megnyitása után lép életbe.

## Biztonsági mentés és visszaállítás

Ezzel a funkcióval biztonsági másolatot készíthet az összes alkalmazásadatáról, vagy átviheti azokat egy másik eszközre. Megadhatja, mit tartalmazzon:

- **Adatbázis** — az összes szám a zenetárban, beleértve a lejátszási listákat.
- **Albumborítók** — az összes gyorsítótárazott albumborító.
- **Beállítások** — az összes alkalmazásbeállítás.

Koppintson az **Alkalmazásadatok biztonsági mentése** gombra a biztonsági mentés megkezdéséhez.

Részletes útmutató: [Hogyan viheti át a zenetárát eszközök között](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Súgó

Hozzáférhet az alkalmazás útmutatójához.

## Gyakran ismételt kérdések

Találjon válaszokat a gyakori kérdésekre a GYIK szekcióban.

## Visszajelzés küldése

Visszajelzéssel rendelkezik vagy segítségre van szüksége? Küldjön visszajelzést az ügyfélszolgálati csapatnak közvetlenül az alkalmazásból.

## Az alkalmazás megosztása

Ossza meg az alkalmazást barátaival.

## Fedezzen fel több alkalmazást

Fedezze fel az Everappz többi alkalmazását.

## Felhasználási feltételek

Az alkalmazás használatának feltételeit ismerteti.

## Adatvédelmi irányelvek

Látogassa meg az adatvédelmi irányelvek oldalát.

## Analitika és adatgyűjtés

Ellenőrizze, hogy mely szolgáltatások vannak engedélyezve az analitikához és adatgyűjtéshez.

## Jogi megjegyzések

Az alkalmazásban használt összes könyvtárra vonatkozó információkat tartalmazza, az alkalmazás verziószámával együtt.
