---
title: "Tag szerkesztő"
date: 2020-02-01
description: "Ismerje meg, hogyan használja az Evertag Tag szerkesztőjét a zenei metaadatok frissítéséhez, albumborítók szerkesztéséhez, több fájl kötegelt szerkesztéséhez és a MusicBrainz tagek kezeléséhez. Ideális a zenekönyvtár rendezéséhez iOS-en és Macen."
keywords: [
  "Evertag tag szerkesztő", "audio metaadat szerkesztő", "zenei tag szerkesztő",
  "audio tagek szerkesztése iPhone-on", "albumborító szerkesztő", "audio tagek kötegelt szerkesztése",
  "MusicBrainz metaadat", "zeneszervező alkalmazás", "Evertag útmutató", "ID3 tag szerkesztő"
]
tags: ["útmutató", "evertag", "tag szerkesztő"]
readingTime: 5
---


A **Tag szerkesztő** az Evertag alkalmazás főképernyője, ahol megtekintheti és szerkesztheti az audio fájlok metaadatait. Nyissa meg ezt a képernyőt egy fájlra koppintva a **Helyi fájlok** szakaszból vagy bármely csatlakoztatott **felhőtároló** fiókból.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag szerkesztő képernyő" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Szerkesztési módok

Az Evertag két szerkesztési módot kínál:

- **Egyfájlos mód**  
  - Fájlok közötti navigálás az alkotói körhinta balra vagy jobbra húzásával.  

- **Kötegelt mód**  
  - Több fájl egyidejű szerkesztése és közös metaadatok alkalmazása.  
  - Az aktiváláshoz görgessen le, és koppintson a **Fájlok egyidejű szerkesztése** lehetőségre.

## Egyfájlos mód

Alapértelmezés szerint az alkalmazás egyfájlos módban nyitja meg a tag szerkesztőt, csak a fő szerkesztési opciókkal engedélyezve. Ebben a módban szerkesztheti a leggyakoribb metaadat mezőket, például:

**Zeneszám cím, Alcím, Album előadó, Album, Előadó, Zeneszerző, Előadó, Műfaj, Megjegyzés, Ütemes percenként, Podcast, Összeállítás, Lemezszám, Zeneszám szám, Zeneszám összesen, Értékelés, Év**

Az összes elérhető tag eléréséhez görgessen a képernyő aljára, és koppintson a **Bővített tagek megjelenítése** opcióra. Ez kiterjesztett módba kapcsolja a szerkesztőt, lehetővé téve több mint **120 metaadat mező** szerkesztését, beleértve a **MusicBrainz tageket**, **Dalszövegeket**, **Tanácsadói értékeléseket**, replay-gain értékeket, rendezési sorrendeket, podcast metaadatokat és egyebeket. A **Beállítások → Audio tag szerkesztő → Gombok a főképernyőn** segítségével véglegesen bekapcsolhatja a Bővített tagek megjelenítését, hogy mindig be legyen kapcsolva.

{{< cards cols="1">}}
{{< card title="" subtitle="Alsó műveletek panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Kötegelt mód

Kétféleképpen léphet be a kötegelt szerkesztésbe:

1. **Fájlkezelőből**  
   - Koppintson a **További műveletek** (•••) gombra a jobb felső sarokban.  
   - Koppintson a **Kiválasztás** gombra, válasszon ki több fájlt, majd koppintson az **Audio tagek szerkesztése** lehetőségre.

2. **Tag szerkesztőből**  
   - Nyisson meg bármely fájlt, görgessen le, és koppintson a **Fájlok egyidejű szerkesztése** lehetőségre az összes fájl betöltéséhez ugyanabból a mappából.

{{< cards cols="1">}}
{{< card title="" subtitle="Kötegelt szerkesztési mód" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

A szerkesztés után koppintson a **Mentés** gombra a változtatások alkalmazásához.

## Dalszövegek szerkesztése

A kiterjesztett szerkesztő megjeleníti a **Dalszövegek** mezőt. Koppintson rá a dalszövegek listájának megnyitásához – minden dalszöveg bejegyzésnek saját nyelve és leírása van, így egyetlen zeneszám több fordítást is tárolhat.

Nem kell nulláról beírni a dalszövegeket. A szerkesztő tartalmaz egy-koppintásos keresési hivatkozásokat a legpopulárisabb dalszöveg-adatbázisokhoz az interneten, előre kitöltve a jelenlegi zeneszám előadójával és címével:

- **Lrclib** — az elsődleges nyilvános adatbázis **időzített (LRC-stílusú) dalszövegekhez**. Akkor használja, ha szinkronizált dalszövegeket szeretne, amelyek sorról sorra görgetnek az azokat támogató lejátszókban.
- **Genius** — nagy katalógus megjegyzésekkel és pontos sima szöveges dalszövegekkel.
- **Lyricsify** — közösség által vezérelt adatbázis sima és időbélyegzett dalszövegekkel.
- **Google** — általános webes keresés tartalékként, ha a dedikált adatbázisokban nincs találat.

Minden hivatkozás csak akkor jelenik meg, ha a megfelelő szolgáltatás elérhető az eszközéről. Koppintson egy szolgáltatásra, másolja a kívánt dalszövegeket (vagy az LRC időbélyegeket), térjen vissza az Evertag-be, és illessze be őket a szövegmezőbe – majd koppintson a **Mentés** gombra a dalszövegek audio fájl tagjeibe való visszaírásához.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dalszöveg oldalak" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Válasszon nyelvet a választóból:

{{< cards cols="1">}}
  {{< card title="" subtitle="Dalszöveg nyelv kiválasztó" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Ezután illessze be vagy írja be a dalszöveg szöveget. Az Evertag támogatja a sima szöveget és az időbélyegzett (szinkronizált) dalszövegeket is – a helyőrző az LRC-stílusú formátum példáját mutatja, amelyet pontosan a Lrclib és a Lyricsify ad vissza szinkronizált eredményekre.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dalszöveg szövegszerkesztő" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Értékelés és tanácsadói értékelés beállítása

A kiterjesztett szerkesztő csillag **Értékelés** vezérlőt és **Tanácsadói értékelés** szegmentált vezérlőt kínál.

### Csillag értékelés

Használja az **Értékelés** mezőt, hogy egy-öt csillagos személyes pontszámot adjon egy zeneszámnak. Az érték a fájl szabványos értékelési tagjébe íródik (POPM az ID3-hoz, `rate` az MP4-hez, `RATING` a Vorbis/APE-hez stb.), így más alkalmazások, amelyek olvassák ezt a taget – beleértve a Zene alkalmazást, a Plexet, a Roont és a legtöbb asztali tag szerkesztőt – azonnal felveszik a pontszámokat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Értékelés" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Tanácsadói értékelés

A **Tanácsadói értékelés** egy zeneszám tartalmát jelöli az iTunes Store és a legtöbb zenei platform által használt Szülői tanácsadói szabvány értékeinek egyikével:

- **Sértődésmentes** — az alapértelmezett szülői tanácsadói információ nélküli zeneszámokhoz. A fájl mindenki számára alkalmasnak minősül, és nem jelenít meg semmilyen tanácsadói jelölést az azokat tisztelő lejátszókban.
- **Explicit** — a zeneszám explicit nyelvezetet vagy tartalmat tartalmaz. Az szülői ellenőrzést tisztelő lejátszók (a Zene alkalmazás, az Apple TV alkalmazás, Spotify exportok, Plex stb.) **E** jelvényt jelenítnek meg a cím mellett, és ha az eszközön vagy fiókban korlátozások vannak engedélyezve, elrejthetik a zeneszámot a gyermek profilokból vagy megtagadhatják a lejátszást.
- **Tiszta** — egy egyébként explicit zeneszám cenzúrázott vagy szerkesztett verziója. A lejátszók **C** jelvényt jelenítenek meg, hogy a hallgatók megkülönböztethessék a tiszta változatot az eredeti explicit mestertől, ami hasznos, ha mindkét verzió ugyanabban a könyvtárban van.

Ezt a mezőt beállítani vagy javítani kell, ha:

- Egy fájlon rossz jelölés van (például egy tiszta rádióverzión tévesen Explicit jelölés van, vagy fordítva).
- A zeneszámokat rippelték vagy töltötték le a tag nélkül, és most Sértődésmentesként jelennek meg, bár explicit tartalmat tartalmaznak – a szülői ellenőrzéshez és a Family Sharing könyvtárhoz szükséges.
- Albumot készít be benyújtásra vagy megosztásra, és minden zeneszámnak konzisztens metaadatot kell tartalmaznia.
- Azt szeretné, hogy a CarPlay, a Zárolt képernyő, az Apple Music-stílusú lejátszók vagy a DJ szoftver a zeneszám cím mellett a megfelelő **E** / **C** jelvényt jelenítse meg.

Az érték a fájlformátum szabványos tanácsadói értékelési mezőjébe kerül tárolásra (`rtng` az MP4-hez, `TXXX:ITUNESADVISORY` az ID3-hoz, `ITUNESADVISORY` a Vorbis-hoz), így bármely szülői tanácsadói metaadatot olvasó lejátszó látni fogja a frissítést.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dalszöveg tanácsadói értékelés" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Albumborító szerkesztése

Az albumborító megváltoztatásához:

1. Koppintson a **Kamera ikonra** az alkotói körhintában.  
2. Válassza ki a kép helyét: Helyi fájlok, Felhő, Letöltések vagy Fotó könyvtár.  
3. Válasszon ki egy képet borítóként való alkalmazáshoz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Kép kiválasztása" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## További műveletek a Tag szerkesztőben

Extra szerkesztési lehetőségek érhetők el az alkotói nézet alatti eszköztárán keresztül.

{{< cards cols="1">}}
  {{< card title="" subtitle="További műveletek menü" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Audio tagek automatikus keresése

Ez a művelet aktiválja az intelligens tag keresési motort, amely megtalálja és kitölti a teljes metaadatot az audio fájlhoz a meglévő információk alapján.  
Az alkalmazás a MusicBrainz adatbázist használja – az egyik legátfogóbb tag adatbázist – több mint **50 millió** zeneszámmal.

### Albumborító keresése

A metaadatok segítségével keressen a weben a megfelelő albumborítóhoz.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Albumborító keresése" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Ha megtalálta, mentse el a képet a **Fotók** alkalmazásba a rendszer helyi menü segítségével.

{{< cards cols="1">}}
  {{< card title="" subtitle="Kép hozzáadása a Fotókhoz" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Ezt követően térjen vissza a tag szerkesztőbe, koppintson a Kamera ikonra, lépjen a **Fotók könyvtárba**, és válassza ki a mentett képet. Az alkalmazás beállítja azt az audio fájl borítójaként.

Beállíthatja, hogyan méretezzék a borítóképeket az alkalmazás beállításaiban.

### Albumborító mentése

Ez a művelet az aktuális albumborítót a **Documents** mappába menti, hogy később újra felhasználhassa.

### Kódolás normalizálása

Ez a művelet normalizálja az audio fájl metaadatainak összes tagjének szövegkódolását. Különösen hasznos, ha Windows PC-ről vált, ahol a fájlok különböző kódolásokat használhatnak, amelyek olvashatatlan vagy torzított karakterekként jelennek meg Macen.

### Tagek kézi keresése

Keressen albummetaadatokat manuálisan a MusicBrainz adatbázisban.  

- Válassza ki az albumot  

{{< cards cols="1">}}
  {{< card title="" subtitle="Album kiválasztása" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Válassza ki a megfelelő dalt  

{{< cards cols="1">}}
  {{< card title="" subtitle="Dal kiválasztása" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Válassza ki, mely tageket kívánja alkalmazni  

{{< cards cols="1">}}
  {{< card title="" subtitle="Audio tagek kiválasztása" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Koppintson a **Kész** gombra a kiválasztott metaadat alkalmazásához a zeneszámra.

### Audio tagek törlése

Törölje az összes metaadat mezőt egy fájlhoz. Hasznos, ha nulláról kezd. Koppintson a **Mentés** gombra a megerősítéshez.

## Tag szerkesztő beállítások

Lépjen a **Beállítások → Audio tag szerkesztő** menübe a viselkedés testreszabásához.

### Albumborító méretezés

Válassza ki, hogyan méreteződjenek az albumborítók audio fájlokba mentéskor. Letilthatja a méretezést az eredeti képméret megtartásához, de vegye figyelembe, hogy néhány lejátszó nem támogat nagy borítófájlokat. Az "eredeti méret" opció a Prémium személyre szabási funkciók része.

### Tag mentési beállítások

- **ID3v2.4** — Engedélyezve esetén az alkalmazás ID3v2.4 formátumban menti a tageket, ha lehetséges. Tiltsa le, hogy a szélesebb körben támogatott ID3v2.3-ra váltson vissza, ha audio tagei nem jelennek meg helyesen régebbi lejátszókon vagy eszközökön.
- **Duplikált tagek** — Engedélyezve esetén a közös metaadat mezők mindkét tag szekciójába duplikálódnak. Ez javítja a kompatibilitást régebbi audio lejátszókkal, de a legtöbb esetben nem szükséges.

### Felhőfájl metaadat frissítési lehetőségek

Szabályozhatja, hogyan frissíti az alkalmazás a felhőszolgáltatásokban tárolt audio fájlok metaadatait:

- **Megerősítési üzenet megjelenítése**  
  A metaadat változások felhőfájlokra való alkalmazása előtt kérdezzen rá.

- **A fájl metaadatainak automatikus frissítése**  
  A szerkesztés után automatikusan mentse a metaadat változásokat a felhőfájlba.

- **Ne frissítse a fájl metaadatait**  
  Hagyja ki a felhőfájlok frissítését – a változások csak helyi szinten lesznek alkalmazva.

### Online fájlok szerkesztése

Válassza ki, mi történjen a felhőfájlok helyi letöltött másolataival szerkesztés után:

- **Letöltött fájl törlése mindig**  
  A mentés megerősítése után távolítsa el a helyi másolatot.

- **Letöltött fájl törlése soha**  
  Tartsa meg a letöltött fájlt az eszközén szerkesztés után.

### Főképernyő gombok

Testreszabhatja, milyen műveletek jelenjenek meg a tag szerkesztő főképernyőjén (Audio tagek automatikus keresése, Audio tagek kézi keresése, Albumborító keresése, Albumborító mentése, Kódolás normalizálása, Audio tagek törlése). A **Bővített tagek megjelenítése** és a **Fájlok egyidejű szerkesztése** is átkapcsolható, hogy a szerkesztő mindig a kívánt módban nyíljon meg.
