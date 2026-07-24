---
title: "Hangeffektek és DSP használata a Flacboxban: kompresszor, Freeverb, Crossfeed, visszhang, hangerő-normalizálás és még sok más"
date: 2026-07-24
description: "A teljes útmutató a Flacbox hangzásához iPhone-on, iPaden és Macen. Ismerd meg, hogyan működik a BASS motor, milyen extra formátumokat játszik le (beleértve a MOD és tracker zenét, valamint a DSD-t), és pontosan mit csinál a hangzásoddal minden effekt, minden csúszka és minden preset, továbbá a 10 sávos hangszínszabályzó és az egyéni DSP-lánc."
keywords: ["Flacbox hangeffektek", "Flacbox presetek elmagyarázva", "Flacbox BASS motor", "BASS audio könyvtár iOS", "MOD zenelejátszó iPhone", "tracker zenelejátszó iOS", "MOD XM IT S3M lejátszása iPhone", "DSD lejátszó iOS", "FLAC lejátszó iPhone", "veszteségmentes zenelejátszó iOS", "Flacbox hangszínszabályzó presetek", "10 sávos hangszínszabályzó iPhone", "hangerő-normalizálás iPhone", "EBU R128 iOS", "hangosság-normalizálás zenelejátszó", "crossfeed fejhallgató iOS", "bs2b crossfeed", "kompresszor presetek zenelejátszó", "freeverb reverb iOS", "visszhang késleltetés zenelejátszó", "DSP-lánc zenelejátszó", "basszuskiemelés iPhone", "hogyan adjunk effekteket a zenéhez Flacbox", "legjobb hangszínszabályzó beállítások iPhone"]
tags: ["Flacbox", "Hangeffektek", "Útmutató", "BASS", "Hangszínszabályzó", "Basszuskiemelés", "Kompresszor", "Freeverb", "Crossfeed", "Visszhang", "Hangerő-normalizálás", "EBU R128", "MOD zene", "Tracker zene", "DSD", "FLAC", "DSP", "Fejhallgató", "Presetek"]
readingTime: 30
---

{{< author-byline >}}

**Rövid válasz:** A Flacboxban egyetlen **Lejátszási motort** választasz a **Beállítások > Audiolejátszó** menüben: **Standard** (az Apple rendszermotorja), **Universal** (az FFmpeg motor) vagy **Sound FX** (a **BASS™ motor**). A választott motor dönti el, mely fájlformátumok játszhatók le, ezért a döntés számít. A **Sound FX** motor olyan extra formátumokat játszik le, amelyeket a legtöbb iPhone-alkalmazás kihagy (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, és régi **MOD és tracker zenét**, mint a MOD, XM, IT és S3M), és ez az egyetlen motor, amely a hangeszközöket működteti: egy **10 sávos hangszínszabályzót**, **hangerő-normalizálást**, **kompresszort**, **Freeverbet**, **Auto Wah-t**, **Phasert**, **Flangert**, **visszhangot**, **Chorust**, **torzítást**, **Rotate-et**, **Crossfeedet** és egy saját összeállítású **DSP-láncot**. Tehát ahhoz, hogy ebben az útmutatóban szereplő effekteket használd, először állítsd a Lejátszási motort **Sound FX**-re. Minden eszköznek vannak kész **presetjei**. Nyisd meg őket a **Beállítások > Audiolejátszó** menüben (Hangeffektek, Hangszínszabályzó, Jelfeldolgozás), vagy koppints a lejátszón a **⋯ (Több)** gombra, és válaszd a **Hangeffektek** lehetőséget. Semmi, amit itt teszel, sosem változtatja meg a fájljaidat.

> Az alábbi csúszka- és preset-magyarázatok ugyanazok a rövid leírások, amelyeket a Flacbox az alkalmazáson belül mutat, kiegészítve egy kis háttérrel, hogy koppintás előtt teljes képet kapj.

## Hogyan olvasd ezt az útmutatót

Minden eszköz ugyanúgy működik:

1. **Kapcsold be.** Minden effektnek saját be/ki kapcsolója van. Kezdetben mind ki van kapcsolva. Egyszerre annyit kapcsolhatsz be, amennyit csak szeretnél.
2. **Válassz presetet.** A preset egy kész beállítás. Koppints rá, és a hangzás azonnal megváltozik. Ez az útmutató felsorolja, mit csinál **minden** preset.
3. **Finomhangolás (opcionális).** Nyisd meg a csúszkákat a kézi állításhoz. Amint elmozdítasz egy csúszkát, az effekt **Manuális** állapotot mutat, így tudod, hogy elhagytad a presetet. Minden csúszkának van visszaállító gombja.

Semmi nem mentődik el a fájljaidba. Ezek élő effektek. Kapcsolj ki egy effektet, és az eredeti hangzás azonnal visszatér.

## Válaszd ki a Lejátszási motort (a Sound FX-ben vannak az effektek)

A Flacbox nem keveri össze a motorokat. **Egyet** választasz a **Beállítások > Audiolejátszó > Lejátszási motor** menüben, és a választott motor dönti el, mely fájlformátumokat játszhatod le, és hogy elérhetők-e az effektek. Három lehetőség van, az alkalmazásban pontosan ezen a néven feltüntetve:

1. **Standard.** Az Apple beépített rendszermotorja. Hardveres dekódolást használ az alacsonyabb akkumulátorhasználatért.
2. **Universal.** Az FFmpeg motor, amely nagyon sokféle formátumot nyit meg.
3. **Sound FX.** A **BASS™ motor**. Teljes pontossággal játssza le a veszteségmentes és nagy felbontású fájlokat, hozzáadja a modul (tracker) zenét, és működteti ebben az útmutatóban minden effektet, a 10 sávos hangszínszabályzót és a DSP-láncot.

Mivel minden motor a saját formátumkészletét támogatja, a lejátszható fájlok a kiválasztott motorral változnak. Ami még fontosabb, az effektek, a hangszínszabályzó és a DSP-lánc **csak** a **Sound FX** motorral működnek, ezért ezt válaszd először, ha használni szeretnéd őket.

A Sound FX a **BASS™** alapokra épül, amely az Un4seen Developments professzionális audio könyvtára. Többet olvashatsz róla a kezdőoldalán: [un4seen.com](https://www.un4seen.com/).

## Zenei formátumok: mit ad hozzá a Sound FX (BASS™) motor (beleértve a MOD és tracker zenét)

A **Sound FX (BASS™)** motor kiválasztásával a Flacbox az alábbi specialista formátumokat is lejátssza a mindennapiak mellett. A legkülönlegesebb a **modul zene**, amelyet **tracker zenének** is neveznek. A modulfájl nem szokványos felvétel. Kis hangszerhangokat tartalmaz, plusz egy „kottát”, amely megmondja, hogyan kell lejátszani őket, és a Flacbox élőben újraépíti a dalt ebből a kottából, ahogyan ezeket a fájlokat lejátszani szánták. A normál lejátszók erre nem képesek.

| Zene típusa | Formátumok | Jó tudni |
|---|---|---|
| **Modul / tracker zene** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Élőben újraépíti a BASS™ modul lejátszó. Kiváló chiptune-okhoz és régi demoscene- vagy Amiga-dalokhoz. |
| **Modern veszteségmentes** | FLAC | Teljes minőség, kisebb, mint a WAV. |
| **Egyéb veszteségmentes** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Ritkább veszteségmentes típusok, mind támogatott. |
| **Nagy felbontású DSD** | DSF, DFF | Normál hardveren játszik le DSD over PCM segítségével. |
| **Modern veszteséges** | Opus, Ogg Vorbis, MP3 | A szokásos streaming és letöltési típusok. |

A Sound FX motor a fő Apple-formátumokat (AAC, ALAC, M4A, WAV, AIFF) és az élő adásokat is lejátssza, így az effektek és a hangszínszabályzó ezeken is működnek.

**Miért segít ez neked:** ha van FLAC albumaid, DSD nagy felbontású fájljaid és egy mappányi régi MOD vagy XM tracker dalod keveréke, a Flacbox mindet lejátssza, és a hangszínszabályzó és az effektek mindegyiken működnek.

## A három menü, amelyet használni fogsz

A Flacbox három helyen tartja a hangeszközeit, mind az audiolejátszó beállításain belül. Először győződj meg róla, hogy a **Lejátszási motor** **Sound FX**-re van állítva (Beállítások > Audiolejátszó > Lejátszási motor), mert az effektek, a hangszínszabályzó és a DSP-lánc csak azzal a motorral érhető el.

- **Hangeffektek** (az effektállvány): nyisd meg a lejátszót, koppints a **⋯ (Több)** gombra, koppints a **Hangeffektek** lehetőségre. Vagy menj a **Beállítások > Audiolejátszó > Hangeffektek** menübe.
- **Hangszínszabályzó** (10 sáv és presetek): **Beállítások > Audiolejátszó > Hangszínszabályzó**.
- **Jelfeldolgozás** (saját DSP-láncod): **Beállítások > Audiolejátszó > Jelfeldolgozás**.

A **kimeneti mintavételi frekvenciát**, a **csatornákat** és a **puffer méretét** is beállíthatod a **Beállítások > Audiolejátszó** menüben.

## A 10 sávos hangszínszabályzó

**Mit csinál:** Megváltoztatja a zene tónusát, a mély basszustól a fényes magasakig. Ez a legjobb eszköz a tiszta **basszuskiemeléshez** vagy egy fényesebb, tisztább felső véghez. Gondolj rá úgy, mint tíz hangerőgombra, mindegyik a hangzás egy-egy szeletéhez. Emelj meg egy sávot, hogy előrehozd azt a részt, csökkentsd, hogy visszahúzd. Néhány dB-es kis változtatások általában a legjobban szólnak, és mindenen működik, amit lejátszol.

**Hogyan működik:** Tíz csúszka **32, 64, 125, 250, 500 Hz és 1, 2, 4, 8, 16 kHz** frekvencián. Mindegyik **-12 dB (vágás)** és **+12 dB (kiemelés)** között mozog. Van egy **Előerősítő** is **-24 és +24 dB** között az általános szinthez. Elmentheted saját presetjeidet, és **exportálhatod vagy importálhatod** őket az eszközök között.

**Mit csinál minden beépített preset (22 preset):**

| Preset | Mit csinál a hangzásoddal |
|---|---|
| **Flat** | Nincs változás. Minden sáv nullán. Tiszta kiindulópont. |
| **Acoustic** | Meleg basszus és tiszta, jelenlévő magasak. Természetessé és élénkké teszi az akusztikus gitárokat és hangokat. |
| **Bass Booster** | Erős kiemelés a mély végben, a közepek és magasak érintetlenek. Több lökés és tömeg. |
| **Bass Reducer** | Levágja a mély véget. Hasznos zúgós szobákhoz, olcsó fülhallgatókhoz vagy nehéz számokhoz. |
| **Treble Booster** | Csak a magasakat emeli. Csillogást és levegőt ad, több részletet. |
| **Treble Reducer** | Lágyítja a magasakat. Megszelídíti a rikító vagy éles felvételeket. |
| **Classical** | Teljes mélyek és lágy magasak enyhe középvággyal. Sima és tágas a zenekari zenéhez. |
| **Dance** | Nagy mélyek és fényes magasak kivájt közepekkel. Lökésteljes és energikus klubszámokhoz. |
| **Deep** | Meleg, vastag mély vég lágyabb magasakkal. Barátságos, laza hangzás. |
| **Electronic** | Erős basszus és fényes magasak szintikhez és ütemekhez. Széles és modern. |
| **Hip-Hop** | Nehéz basszus és tiszta magasak kontrollált közepekkel. Súlyos és lökésteljes. |
| **Jazz** | Meleg és sima, kis középvággyal. Könnyed és természetes az akusztikus jazzhez. |
| **Latin** | Kiemelt mélyek és magasak tiszta közepekkel. Fényes és élénk. |
| **Loudness** | Erősen kiemeli a basszust és a magasakat (egy „mosoly” görbe). Teljesebben szól alacsony hangerőn. |
| **Lounge** | Előretolt közepek lágy szélekkel. Nyugodt és énekbarát. |
| **Piano** | Tiszta közepek és magasak, hogy a zongorahangok tisztán csengjenek ki. |
| **Pop** | Kiemelt közepek az énekhez, a mélyek és magasak visszahúzva. A hangok előre kerülnek. |
| **R&B** | Nagyon erős alsó-közép meleg és tiszta magasak. Sima és gazdag. |
| **Rock** | Kiemelt mélyek és magasak a gitárokhoz és dobokhoz. Energikus és teljes. |
| **Small Speakers** | Kiemeli a mélyeket és vágja a magasakat, hogy a pici hangszórók teljesebben szóljanak. |
| **Spoken Word** | Kiemeli a hangtartományt és vágja a mély basszust. Tisztává teszi a beszédet. |
| **Vocal Booster** | Előretolja a közepet, ahol a hangok élnek, körülöttük vág. Az ének kiemelkedik. |

**Tipp a basszushoz:** Kezdd a **Bass Boosterrel**, majd ha zavarosnak hangzik, húzd le az Előerősítőt 1-2 dB-lel, hogy semmi ne torzuljon.

## Hangerő-normalizálás (egyenletes hangosság)

**Mit csinál:** Egyes dalok hangosabban szólnak, mint mások, ezért folyamatosan állítgatod a hangerőt. Ez elintézi, hogy minden dal magától nagyjából ugyanolyan hangerőn szóljon, így neked nem kell. Tökéletes kevert lejátszási listákhoz, amelyek régi és új felvételeket, különböző albumokat vagy különböző forrásokat vegyítenek, ahol egyik szám sokkal hangosabb lehet a következőnél.

**Hogyan működik:** Meghallgatja minden szám valós hangosságát az **EBU R128** szabvány segítségével (**LUFS**-ban mérve, ugyanaz az elv, amit a streaming szolgáltatások használnak), majd minden számot a célértéked felé igazít. Nem igényel címkéket a fájljaidban, és sosem változtatja meg a hangot. Az EBU R128 azt a hangosságot méri, amelyet a füled valóban érzékel a teljes dalon át, nem csak a legmagasabb csúcsot, ezért egyezik azzal, mennyire hangosnak tűnnek valójában a számok. A Flacbox élőben számolja ki ezt lejátszás közben (és előre ellenőrzi a hangosságot, amikor tudja), majd egyetlen, egyenletes hangerő-változtatást alkalmaz a számra. A **Max kiemelés** korlát megakadályozza, hogy a nagyon halk felvételeket olyan erősen tolja fel, hogy torzuljanak. Mivel magát a hangot olvassa, bármely forráson működik, beleértve a felhőfájlokat, élő adásokat és a modul zenét, még akkor is, ha a fájloknak egyáltalán nincsenek hangossági címkéik.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Célhangosság** | Beállítja a hangosságot, amely felé minden szám igazodik. Magasabb értékek mindent hangosabban szólaltatnak meg összességében. | -30 és -6 LUFS között (-16) |
| **Max kiemelés** | Korlátozza, mennyire erősíthetők fel a halk számok. Magasabb értékek közelebb hozzák a halk felvételeket a célértékhez. | 0 és 24 dB között (12) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Light** | Enyhe kiegyenlítés lazább hallgatáshoz. Elsimítja a nyilvánvaló hangerő-ugrásokat anélkül, hogy erősen feltolná a halk számokat. |
| **Standard** | Az univerzális alapérték. Streaming-stílusú hangossági cél, amely a legtöbb zenéhez illik. Kezdd itt. |
| **Strong** | Agresszív illesztés, amely határozottan feltolja a halk számokat. A legjobb kevert könyvtárakhoz, nagy szinteltérésekkel. |
| **Night** | Egy halkabb általános cél, amely még mindig megemeli a halk részeket, így a késő esti hallgatás egyenletes és halk marad. |

## Kompresszor (a hangos és halk részek kiegyenlítése)

**Mit csinál:** Egyetlen dalon belül a halk részek túl lágyak, a hangos részek túl hangosak lehetnek. Ez közelebb hozza őket egymáshoz, így az egész dal könnyen hallható, akár autóban vagy zajos helyen is. Finoman lehalkítja a leghangosabb pillanatokat és megemeli a lágyabbakat, így nem kell egyetlen számon belül a hangerőhöz nyúlnod. Ez eltér a hangerő-normalizálástól: a Kompresszor **egyetlen** dalon **belül** egyenlít ki, míg a hangerő-normalizálás a dalok **között** illeszti a hangosságot. A kettő jól működik együtt. Kezdd egy presettel, és csak akkor nyisd meg a csúszkákat, ha több irányítást szeretnél.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Küszöb** | A szint, ahol a kompresszió elkezdődik. Alacsonyabb értékek a hangzás nagyobb részét nyomják össze, közelebb tartva a halk és hangos részeket. | -60 és 0 dB között (-20) |
| **Arány** | Milyen erősen tartja vissza a hangos részeket, miután átlépik a küszöböt. Magasabb értékek erősebben tömörítenek, egyenletesebben tartva a hangzást. | 1:1 és 30:1 között (4:1) |
| **Támadás** | Milyen gyorsan reagál az effekt egy hirtelen hangos csúcsra. Rövid értékek elkapják a tranzienseket, hosszabbak átengedik őket. | 0,1 és 1000 ms között (10 ms) |
| **Elengedés** | Milyen gyorsan enged el az effekt, miután a hangos rész elmúlt. Rövid értékek pumpálhatnak, hosszabbak simábban szólnak. | 10 ms és 5 s között (100 ms) |
| **Fő erősítés** | A feldolgozás után alkalmazott végső kimeneti erősítés. Emeld meg, hogy megemeld az általános hangosságot, ha a dinamika már ki van egyenlítve. | -30 és +30 dB között (0) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Transparent** | Alig érzékelhető biztonsági háló. Szinte teljesen megőrzi a dinamikát, és csak a leghangosabb csúcsokat kapja el. |
| **Soft** | Könnyű kiegyenlítés otthoni hi-fi hallgatáshoz. Finom simítás a zene összenyomása nélkül. |
| **Standard** | Ésszerű alapérték a mindennapi zenelejátszáshoz. Az első preset, amit kipróbálhatsz. |
| **Heavy** | Agresszív kiegyenlítés zajos környezethez. Autó, zsúfolt szoba, alacsony hangerejű hallgatás. |
| **Voice / Podcast** | Beszédre hangolt. A lassabb támadás átengedi a sziszegőket, a bőséges kompenzációs erősítés felhúzza a hangokat. |
| **Old Recordings** | Régi albumokhoz és felújított bakelithez, ahol az átlagszint a modern kiadások alatt van. |
| **Late Night** | Erős kompresszió plusz nagy kiemelés a halk hallgatáshoz, amikor a szomszédok vagy az alvó család számít. |
| **Movie Dialog** | Felhozza a beszédet a zenével és a hangeffektekkel szemben egy változatos hangsávban. |
| **Streaming Match** | Nagyjából a modern streaming szolgáltatások hangosság-normalizálását célozza, -14 LUFS körül. |
| **Maximum Loudness** | Minden bevetve. Eléri a limitert, számíts összenyomott, nagyon egyenletes jelre. A szó szerinti maximális hangerejű preset. |

## Freeverb (reverb, a tér érzete)

**Mit csinál:** A tér érzetét adja a zenéhez, egy kis szobától egészen egy nagy teremig. Válassz presetet, vagy finomhangold magad a száraz és nedves keverést, a szoba méretét, a csillapítást és a szélességet. A reverb az a természetes visszhang, amit bármely valós térben hallasz, és a Freeverb szoftveresen újraalkotja. Egy kevés nyitottabbá és élőbbé teszi a lapos vagy közeli mikrofonos felvételeket. Sok a zenét egy nagy, távoli térbe helyezi. Ez kreatív effekt, ezért tartsd a nedves keverést mérsékelten a természetes eredményekért.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Száraz keverés** | Mennyi maradjon meg az eredeti, érintetlen hangból. Magasabb értékek több száraz jelet hagynak a keverékben. | 0 és 1 között (0.0) |
| **Nedves keverés** | Mennyi zengetett hang adódik hozzá. Magasabb értékek hangosabbá és nyilvánvalóbbá teszik a reverbet. | 0 és 3 között (1.0) |
| **Szoba mérete** | Az elképzelt tér mérete. Magasabb értékek hosszabb, nagyobb reverb-utóhangot adnak, egy kis szobától egy katedrálisig. | 0 és 1 között (0.5) |
| **Csillapítás** | Milyen gyorsan halványulnak el a magas frekvenciák az utóhangban. Magasabb értékek sötétebbé és melegebbé teszik a reverbet. | 0 és 1 között (0.5) |
| **Szélesség** | A reverb sztereó kiterjedése. Magasabb értékek szélesebbé teszik a teret a bal és jobb csatorna között. | 0 és 1 között (1.0) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Room** | Egy kicsi, szűk tér. Finom légkör, amely helyérzetet ad anélkül, hogy elmosná a hangzást. |
| **Studio** | Egy száraz, kontrollált felvételi szoba. Épp csak annyi visszaverődés, hogy természetesen szóljon. |
| **Hall** | Egy nagy koncertterem. Hosszú, dús utóhang, amely a zenekari és akusztikus zenéhez illik. |
| **Cathedral** | Egy hatalmas, visszhangzó kőtér. A leghosszabb, legdrámaibb reverb-utóhang. |
| **Plate** | Egy fényes, sűrű stúdió lemezreverb. Klasszikus énekhez és dobokhoz. |
| **Ambience** | Egy rövid, levegős légkör. Könnyed térérzetet ad, miközben többnyire száraz marad. |

## Auto Wah (funky szűrősöprés)

**Mit csinál:** Egy szűrő, amely magától söpör fel-le egy funky, énekszerű wah hangzásért. Válassz presetet, vagy állítsd be magad a nedves keverést, a visszacsatolást, a sebességet, a tartományt és a frekvenciát. Ez ugyanaz a „wah” söprés, amit egy gitáros wah pedál csinál, de itt magától mozog a zenével együtt. Nagyszerűen szól funk, disco és elektronikus számokon. Ez merész, nyilvánvaló effekt, ezért egy kevés is sokat ér a mindennapi hallgatáshoz.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Nedves keverés** | Milyen erős a wah effekt a keverékben. Magasabb értékek nyilvánvalóbbá teszik a söprő szűrőt. | -2 és +2 között (1.5) |
| **Visszacsatolás** | Mennyi kimenet csatolódik vissza az effektbe. Magasabb értékek rezonánsabbá és kifejezettebbé teszik a wah-t. | -1 és +1 között (0.5) |
| **Sebesség** | Milyen gyorsan söpör a szűrő fel-le. Magasabb értékek gyorsabb, ritmikusabb wah-t adnak. | 0,1 és 9 Hz között (2.0) |
| **Tartomány** | Milyen messzire söpör a szűrő, oktávban. Magasabb értékek szélesebb, drámaibb söprést adnak. | 0,1 és 9 oktáv között (4.3) |
| **Frekvencia** | Az alapfrekvencia, amely körül a szűrő söpör. Alacsonyabb értékek mélyebben, magasabbak fényesebben szólnak. | 1 és 1000 Hz között (50) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Classic** | Egy kiegyensúlyozott, klasszikus wah söprés. Jó kiindulópont funkhoz és rockhoz. |
| **Slow** | Egy lassú, széles söprés, amely finoman sodródik fel-le. Kiváló padekhez és hosszú hangokhoz. |
| **Funky** | Egy gyors, lökésteljes söprés, sok mozgással. Ritmikus harapást ad a gitárokhoz és szintikhez. |
| **Deep** | Egy mély, széles söprés, amely alacsony frekvenciáról indul. Nagy és drámai. |
| **Subtle** | Egy finom, visszafogott mozgás. Karaktert ad anélkül, hogy uralná a hangzást. |
| **Resonant** | Egy éles, rezonáns wah magas visszacsatolással. Énekszerű és kifejező. |

## Phaser (örvénylő suhogás)

**Mit csinál:** Egy söprő szűrő, amely örvénylő, suhogó mozgást ad a hangzáshoz. Válassz presetet, vagy állítsd be magad a visszacsatolást, a sebességet, a tartományt és a frekvenciát. Finom mozgást és csillogást ad a hangok megváltoztatása nélkül. Finom az éneken és padeken, drámai a szintiken és gitárokon. Próbáld a Slow-t álmodozó érzethez, vagy a Jet-et erős örvényléshez.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Visszacsatolás** | Mennyi kimenet csatolódik vissza az effektbe. Magasabb értékek rezonánsabbá és kifejezettebbé teszik a phasert. | -1 és +1 között (0.0) |
| **Sebesség** | Milyen gyorsan söpör a szűrő fel-le. Magasabb értékek gyorsabb, ritmikusabb phasinget adnak. | 0,1 és 9 Hz között (1.0) |
| **Tartomány** | Milyen messzire söpör a szűrő, oktávban. Magasabb értékek szélesebb, drámaibb söprést adnak. | 0,1 és 9 oktáv között (4.0) |
| **Frekvencia** | Az alapfrekvencia, amely körül a szűrő söpör. Alacsonyabb értékek mélyebben, magasabbak fényesebben szólnak. | 1 és 1000 Hz között (100) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Classic** | Egy kiegyensúlyozott, klasszikus phaser söprés. Jó kiindulópont gitárokhoz és billentyűkhöz. |
| **Slow** | Egy lassú, széles söprés, amely finoman sodródik fel-le. Kiváló padekhez és hosszú hangokhoz. |
| **Fast** | Egy gyors, csillogó söprés, sok mozgással. Mozgást és energiát ad. |
| **Deep** | Egy mély, széles söprés, amely alacsony frekvenciáról indul. Nagy és drámai. |
| **Subtle** | Egy finom, visszafogott mozgás. Karaktert ad anélkül, hogy uralná a hangzást. |
| **Jet** | Egy intenzív, rezonáns söprés magas visszacsatolással, a klasszikus sugárhajtómű-suhogás. |

## Flanger (sugárhajtómű-söprés)

**Mit csinál:** Egy rövid, mozgó késleltetés, amely sugárhajtóműszerű, söprő suhogást ad a hangzásnak. Válassz presetet, vagy állítsd be magad a mélységet, a visszacsatolást, a sebességet és a késleltetést. Ez a phaser erősebb, fémesebb rokona, híres a klasszikus rock és elektronikus zene suhogó söpréséről. A finom beállítások enyhe mozgást adnak, míg a mély beállítások drámaiak és nyilvánvalóak. Legjobb takarékosan használni, hatáskeltésre.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Mélység** | Milyen erős a söprő effekt. Magasabb értékek nyilvánvalóbbá teszik a flangelést. | 0 és 100% között (25) |
| **Visszacsatolás** | Mennyi kimenet csatolódik vissza az effektbe. Magasabb értékek rezonánsabbá és fémesebbé teszik a flangert. | -99 és +99% között (-50) |
| **Sebesség** | Milyen gyorsan mozog a söprés fel-le. Magasabb értékek gyorsabb, csillogóbb mozgást adnak. | 0 és 10 Hz között (0.25) |
| **Késleltetés** | Az alapkésleltetési idő, amelyre a söprés épül. Magasabb értékek mélyebb, üregesebb karaktert adnak. | 0 és 4 ms között (2.0) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Classic** | Egy kiegyensúlyozott, klasszikus flanger. Jó kiindulópont gitárokhoz és billentyűkhöz. |
| **Subtle** | Egy finom, visszafogott söprés. Mozgást ad anélkül, hogy uralná a hangzást. |
| **Deep** | Egy mély, nehéz söprés erős visszacsatolással. Nagy és drámai. |
| **Jet** | Egy intenzív söprés pozitív visszacsatolással, a klasszikus sugárhajtómű-suhogás. |
| **Fast** | Egy gyors, csillogó söprés sok mozgással és energiával. |
| **Wide** | Egy lassú, széles söprés hosszú késleltetéssel. Dús és tágas. |

## Visszhang (ismétlések)

**Mit csinál:** Elhalványuló visszhangokként ismétli a hangzást a tér és mélység érzetéért. Válassz presetet, vagy állítsd be magad a nedves keverést, a visszacsatolást és a késleltetést. Olyan, mint egy kanyonban kiabálni: a hang egy rövid szünet után egyszer vagy többször visszatér. Egy rövid ismétlés testet és retró érzetet ad, míg a hosszabb ismétlések több visszacsatolással tágas, elhúzódó utóhangokat hoznak létre. A Ping Pong preset a bal és jobb füled között pattogtatja az ismétléseket, ami szórakoztató fejhallgatón. Tartsd mérsékelten a nedves keverést, hogy a visszhangok támogassák a zenét, ne pedig elfedjék.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Nedves keverés** | Milyen hangosak a visszhangok az eredeti hanghoz képest. Magasabb értékek jobban kiemelik az ismétléseket. | -2 és +2 között (0.6) |
| **Visszacsatolás** | Hányszor ismétlődik a visszhang. Magasabb értékek több ismétlést adnak, amelyek tovább halványulnak el. | -1 és +1 között (0.5) |
| **Késleltetés** | A visszhangok közötti idő. Rövidebb értékek szűk slap-backet adnak, hosszabbak egymástól távoli ismétléseket. | 0,01 és 2 s között (0.4) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Slapback** | Egyetlen, szűk ismétlés közvetlenül a hang mögött. Klasszikus rockabilly slap-back. |
| **Room** | Egy rövid, természetes visszhang, mint egy kis szoba. Teret ad a hangzás elmosása nélkül. |
| **Tape** | Meleg, közepes ismétlések, amelyek fokozatosan halványulnak, mint egy régi szalagos késleltetés. |
| **Dub** | Hosszú, nehéz ismétlések erős visszacsatolással. Nagy, dubos és tágas. |
| **Ping Pong** | A visszhangok a bal és jobb hangszóró között pattognak egy széles sztereó hatásért. |
| **Long** | Lassú, egymástól távoli ismétlések, amelyek messze a hang mögött húznak el. |

## Chorus (vastagabb, szélesebb hangzás)

**Mit csinál:** Megvastagítja és kiszélesíti a hangzást egy eltolódó másolat eredetire rétegzésével. Válassz presetet, vagy állítsd be magad a nedves/száraz keverést, a mélységet, a sebességet és a visszacsatolást. Úgy hangzik, mintha egy hangszer vagy hang több egyszerre játszóból állna, enyhén elhangolt, mozgó másolatok hozzáadásával. Ez gazdagságot és finom csillogást ad. A finom beállítások felmelegítenek, míg az erős beállítások dúsan és álmodozón szólnak. Népszerű gitárokon, billentyűkön és éneken.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Nedves/Száraz** | Mennyi chorust hallasz az eredeti hanghoz képest. Magasabb értékek nyilvánvalóbbá teszik az effektet. | 0 és 100% között (50) |
| **Mélység** | Milyen messzire ingadozik a hangmagasság fel-le. Magasabb értékek vastagabb, csillogóbb hangzást adnak. | 0 és 100% között (25) |
| **Sebesség** | Milyen gyorsan mozog a csillogás. A lassabb sebességek gyengéden és dúsan szólnak, a gyorsabbak inkább vibratóra hasonlítanak. | 0 és 10 Hz között (1.1) |
| **Visszacsatolás** | Mennyi effekt csatolódik vissza önmagába. Magasabb értékek rezonánsabbá és intenzívebbé teszik a chorust. | -99 és +99% között (25) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Subtle** | Egy finom megvastagítás, amely meleget ad anélkül, hogy magára vonná a figyelmet. |
| **Lush** | Egy gazdag, klasszikus chorus. Kiváló univerzális beállítás gitárokhoz és billentyűkhöz. |
| **Ensemble** | Egy teljes, rétegzett csillogás, amely egyetlen hangszert több hangszernek hangoztat. |
| **Vibrato** | Teljesen nedves, gyors sebességgel, egy remegő vibratóért egy finom chorus helyett. |
| **Wide** | Egy lassú, széles csillogás, amely kinyitja a sztereó képet. Tágas és álmodozó. |
| **Twelve-String** | Egy fényes, rezonáns csillogás, amely egy tizenkét húros gitárra emlékeztet. |

## Torzítás (érdesség és él)

**Mit csinál:** Érdességet és élt ad a hangzás túlvezérlésével. Válassz presetet, vagy állítsd be magad a meghajtást, a kimenetet és a tónust. Szándékosan durvábbá teszi a hangzást, egy meleg, érdes éltől egy tört, fuzzos tónusig. Ez inkább kreatív, szórakoztató effekt, mint a minőség javításának módja, ezért kis mennyiségben használd. Szórakoztató elektronikus, rock és kísérleti számokon. Csökkentsd a Kimenetet, ha egy nehéz preset túl hangos lesz.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Meghajtás** | Milyen erősen torzul a hang. Magasabb értékek érdesebbek és agresszívabbak. | 0 és 100% között (15) |
| **Kimenet** | A kimeneti szint a torzítás után. Csökkentsd, ha egy nehéz beállítás túl hangos lesz. | -60 és 0 dB között (-18) |
| **Tónus** | Levágja a magasakat a torzítás előtt. Alacsonyabb értékek sötétebben és melegebben szólnak. | 100 és 8000 Hz között (8000) |
| **Középpont** | Mely frekvencia köré összpontosul a torzítás. Fényesebbre vagy sötétebbre tolja a karaktert. | 100 és 8000 Hz között (2400) |
| **Szélesség** | Milyen széles ez a fókusz. A szűk élesen és orrhangúan szól, a széles teljesen és nyitottan. | 100 és 8000 Hz között (2400) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Warm Drive** | Egy könnyű, meleg érdesség, amely élt ad a karakter nagy megváltoztatása nélkül. |
| **Crunch** | Egy klasszikus ropogós túlvezérlés, lökésteljes és ritmikus. |
| **Overdrive** | Egy fényes, meghajtott tónus, sok harapással. Kiváló szólóhangzásokhoz. |
| **Fuzz** | Egy vastag, telített fuzz. Nehéz és felharmonikusokkal teli. |
| **Metal** | Egy szűk, közép-központú nagy meghajtású tónus agresszív, nehéz hangzásokhoz. |
| **Screamer** | Egy közép-kiemelt túlvezérlés, amely átvág, mint egy tube screamer. |
| **LoFi** | Egy összezúzott, keskeny sávú torzítás egy érdes lo-fi karakterért. |

## Rotate (forgó sztereó)

**Mit csinál:** Megforgatja a hangzást a sztereó mezőben egy forgó, örvénylő hatásért. Válassz presetet, vagy állítsd be magad a sebességet. Lassan mozgatja a hangzást a bal és jobb csatornád körül, kicsit mint egy forgó hangszóró, ami örvénylő, hipnotikus érzetet ad. A lassú beállítások gyengédek és szélesek, míg a gyors beállítások szédítők és nyilvánvalók. Ez sztereó effekt, ezért fejhallgatón vagy jól elhelyezett hangszórókon a legszembetűnőbb.

**Csúszka:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Sebesség** | Milyen gyorsan forog a hang a sztereó mezőben. A negatív értékek a másik irányba forgatnak, a nulla állva tartja. | -5 és +5 Hz között (1.0) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Slow Pan** | Egy lassú, gyengéd sodródás egyik oldalról a másikra. Finom és széles. |
| **Sway** | Egy egyenletes bal-jobb ringás. Gyengéd mozgást ad a sztereó képhez. |
| **Rotary** | Egy közepes forgás, amely egy forgó hangszóróra emlékeztet. |
| **Fast Spin** | Egy gyors forgás a sztereó mező körül egy szédítő, örvénylő hatásért. |
| **Reverse** | Egy közepes forgás az ellenkező irányban. |
| **Whirl** | Egy nagyon gyors örvénylés. Intenzív és dezorientáló. |

## Crossfeed (természetes hangzás fejhallgatón)

Hangszórókon mindkét füled hallja a bal és a jobb hangszórót is, csak kissé eltérő időben és hangerővel. Fejhallgatón ez a természetes keveredés eltűnik: a bal füled csak a bal csatornát hallja, a jobb füled pedig csak a jobbat. Ez a „szuper sztereó” azt az érzetet keltheti, hogy a zene a fejeden belülre hasad, és a keményen panorámázott felvételek, ahol egy hangszer teljesen az egyik oldalon ül, természetellenesnek vagy fárasztónak tűnhetnek hosszú hallgatáson.

A Crossfeed ezt úgy javítja, hogy egy kis, szűrt mennyiséget kever mindkét csatornából a másikba, egy apró késleltetéssel és a magas frekvenciák gyengéd levágásával. Ez közel áll ahhoz, ahogyan a valós hangszórókból származó hang eléri mindkét füledet, beleértve azt is, ahogyan a fejed enyhén árnyékolja a távolabbi fület. Az eredmény egy természetesebb, hangszóró-szerű kép, amely kissé előtted ül, nem pedig a fejeden belül, és csökkenti a hallgatási fáradtságot a hosszú üléseken. A Flacbox a jól ismert **bs2b (Bauer stereophonic-to-binaural)** módszert használja, egy elismert nyílt forráskódú crossfeedet, amelyet sok audiofil lejátszó használ. Az algoritmusról a [bs2b projektoldalon](https://bs2b.sourceforge.net/) olvashatsz.

A **Levágás** szabályozza, mennyire melegen szól a keverés, a **Betáplálási szint** pedig azt, mennyire erős. A presetek lefedik a klasszikus bs2b szinteket, egy alig érzékelhető érintéstől egy határozott, hangszóró-szerű keverésig. A Crossfeed egy fejhallgatós effekt, ezért hagyd kikapcsolva, amikor hangszórón hallgatsz.

**Csúszkák:**

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Levágás** | Beállítja, hol kezd lecsengeni a csatornák közötti átszivárgás. Alacsonyabb értékek melegebb, kifejezettebb hatást adnak. | 300 és 2000 Hz között (700) |
| **Betáplálási szint** | Szabályozza, mennyi szivárog át az egyik csatornából a másikba. Magasabb értékek hangszóró-szerűbb hangzást adnak. | 1 és 15 dB között (4.5) |

**Presetek:**

| Preset | Mit csinál |
|---|---|
| **Subtle** | Alig érzékelhető crossfeed lazább hallgatáshoz. Lágyítja a keményen panorámázott sztereót a tónusegyensúly megváltoztatása nélkül. |
| **Chu Moy** | A klasszikus univerzális alapérték. Kiegyensúlyozott és enyhén meleg, szinte bármilyen anyagon működik. Kezdd itt. |
| **Strong** | Erősebb átszivárgás a keményebben panorámázott keverésekhez. Nyilvánvalóbb sztereó szűkítés. |
| **Jan Meier** | Népszerű a fejhallgató-rajongók körében. Szélesebb betáplálás, hangszóró-szerűbb megjelenítés, enyhe basszuskiemelés. |
| **Speaker-like** | A leginkább természetes hangszóró-stílusú reprodukcióra hangolva fejhallgatón. |
| **Vintage Stereo** | Agresszív crossfeed az 1960-as és 1970-es évek keveréseihez hangolva, keményen panorámázott dobokkal és énekkel. |

## Jelfeldolgozás: építsd meg saját DSP-láncodat

A kész effekteken túl a Flacbox lehetővé teszi, hogy megépítsd saját láncodat a **Beállítások > Audiolejátszó > Jelfeldolgozás** menüben. Ahogy az alkalmazás magyarázza, amikor a lánc üres: *„Koppints a + gombra egy effekt hozzáadásához. Kapcsold be vagy ki mindegyiket a saját kapcsolójával, húzd az átrendezéshez, koppints a paraméterei szerkesztéséhez, és tartsd lenyomva a duplikáláshoz vagy törléshez.”*

A **sorrend számít**: egy szűrő egy torzítás előtt másképp szól, mint ugyanaz a szűrő utána. Az egész láncot ráirányíthatod az **Összes csatornára**, a **Bal csatornára** vagy a **Jobb csatornára** is.

Alább minden blokk szerepel, az alkalmazás saját szövegével minden csúszkához és minden presethez.

### Erősítés (szinttrimmelés)

Megemeli vagy csökkenti a szintet a lánc egy pontján.

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Erősítés** | Megemeli vagy csökkenti a szintet a lánc ezen a pontján. Használd a szint pótlására más effektek után, vagy az utána következők meghajtására. | -24 és +24 dB között (0) |

| Preset | Mit csinál |
|---|---|
| **Unity** | Nincs szintváltozás. Semleges kiindulópont. |
| **Cut** | Egy nagy vágás. Megszelídít egy hangos forrást, vagy helyet csinál az utána következő effektek előtt. |
| **Trim** | Egy gyengéd vágás, hogy kissé visszahúzza a szintet. |
| **Lift** | Egy szerény kiemelés egy halk forrás megemeléséhez. |
| **Boost** | Egy erős kiemelés halk anyaghoz, vagy a következő effektek erősebb meghajtásához. |
| **Max** | Maximális kiemelés. Hangos, figyelj a lánc későbbi részén a klippelésre. |

### Aluláteresztő (eltávolítja a magasakat)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Levágás** | Beállítja, hol kezdi a szűrő lecsengetni a magasakat. Csökkentsd a hangzás sötétítéséhez és lágyításához, emeld a tetejéig a teljes kinyitáshoz. | 20 Hz és 20 kHz között (20 kHz) |
| **Rezonancia** | Kiemeli a frekvenciákat pontosan a levágásnál. Tartsd alacsonyan a tiszta lecsengéshez, emeld a csúcsos, fütyülő élért. | 0,1 és 10 között (0.707) |

| Preset | Mit csinál |
|---|---|
| **Air** | Csak a legtetejét trimmeli. Levesz egy kis élt anélkül, hogy tompítaná a hangzást. |
| **Warm** | A magasak gyengéd lecsengetése egy melegebb, kerekebb tónusért. |
| **Mellow** | Észrevehetően lágyítva. Visszahúzza a fényességet egy laza érzetért. |
| **Muffled** | Sötét és tompa, mintha egy falon keresztül hallanád. |
| **Telephone** | Egy keskeny, rezonáns csúcs a tartomány alján. Egy vékony, telefonszerű hang. |

### Felüláteresztő (eltávolítja a mélyeket)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Levágás** | Beállítja, hol kezdi a szűrő lecsengetni a mélyeket. Emeld a mély vég vékonyításához és a dörgés eltávolításához, csökkentsd az aljáig a teljes kinyitáshoz. | 20 Hz és 20 kHz között (20 Hz) |
| **Rezonancia** | Kiemeli a frekvenciákat pontosan a levágásnál. Tartsd alacsonyan a tiszta lecsengéshez, emeld a csúcsos, fütyülő élért. | 0,1 és 10 között (0.707) |

| Preset | Mit csinál |
|---|---|
| **Rumble Cut** | Eltávolítja a szubszonikus dörgést és a DC-eltolódást a hallható mély vég érintése nélkül. |
| **Tighten** | Trimmeli a zúgós mély frekvenciákat egy szűkebb, tisztább basszusért. |
| **Thin** | Levágja a meleget és a testet, egy könnyebb, vékonyabb hangzást hagyva. |
| **Radio** | Csak a közepek és magasak maradnak, mint egy kis rádióhangszóró. |
| **Telephone** | Egy keskeny, rezonáns csúcs a tartomány tetején. Egy vékony, telefonszerű hang. |

### Sáváteresztő (megtart egy középső sávot)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Középpont** | Beállítja a frekvenciát, amelyet a szűrő átenged. Minden felette és alatta lecseng. Söpörd végig, hogy kiemeld a basszust, közepeket vagy magasakat. | 20 Hz és 20 kHz között (1 kHz) |
| **Rezonancia** | Szabályozza, milyen széles a sáv. Alacsony értékek széles tartományt engednek át, emeld a középpontra szűkítéshez egy éles, rezonáns tónusért. | 0,1 és 10 között (0.707) |

| Preset | Mit csinál |
|---|---|
| **Voice** | Egy széles sáv a középtartomány körül, ahol a legtöbb ének ül. Semleges kiindulópont. |
| **Bass** | Elszigeteli a mély véget, csak a basszust és a lábdobot hagyva. |
| **Body** | Az alsó-közepekre összpontosít egy meleg, dobozos testért. |
| **Presence** | Megemeli a felső-közepeket a tisztaságért és jelenlétért. |
| **Telephone** | Egy keskeny középtartományú sáv. Egy vékony, telefonszerű hangzás. |
| **Wah** | Egy nagyon keskeny, rezonáns csúcs. Söpörd a középpontot egy wah hatásért. |

### Kivágó (eltávolít egy keskeny sávot)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Frekvencia** | Beállítja a frekvenciát, amelyet a szűrő eltávolít. Minden felette és alatta átmegy. Hangold rá egy zúgásra vagy rezonanciára, hogy kivágd. | 20 Hz és 20 kHz között (60 Hz) |
| **Rezonancia** | Szabályozza, milyen széles a vágás. Alacsony értékek széles tartományt vájnak ki, emeld, hogy csak egy pontszerű sávot távolíts el, a többit érintetlenül hagyva. | 0,1 és 10 között (8.0) |

| Preset | Mit csinál |
|---|---|
| **Mains Hum 60** | Eltávolítja a 60 Hz-es elektromos zúgást (észak-amerikai hálózat). Semleges kiindulópont. |
| **Mains Hum 50** | Eltávolítja az 50 Hz-es elektromos zúgást (európai és egyéb hálózat). |
| **Rumble** | Levág egy mélyfrekvenciás dörgést vagy rezonanciát az egész mély vég vékonyítása nélkül. |
| **Mud** | Kivájja az alsó-közepes sarat egy tisztább, világosabb hangzásért. |
| **Boxy** | Eltávolítja a dobozos középtartományú tülkölést. |
| **Harsh** | Megszelídít egy rikító, átható csúcsot a felső-közepekben. |

### Kiemelő (parametrikus EQ-sáv)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Frekvencia** | A kiemelendő vagy vágandó sáv középpontja. Söpörd végig, hogy megtaláld a formálni kívánt frekvenciát. | 20 Hz és 20 kHz között (1 kHz) |
| **Erősítés** | Mennyivel emeld vagy vágd a középpontnál. A pozitív megemeli a sávot, a negatív kivájja. | -15 és +15 dB között (0) |
| **Q tényező** | Beállítja, milyen széles a sáv. Alacsony értékek széles területet formálnak, magas értékek sebészi, pontszerű változtatásokra szűkítenek. | 0,1 és 10 között (1.0) |

| Preset | Mit csinál |
|---|---|
| **Presence** | Egy széles felső-közép kiemelés a tisztaságért és jelenlétért. Semleges kiindulópont. |
| **Warmth** | Egy széles alsó-közép kiemelés, amely testet és meleget ad. |
| **Vocal Boost** | Megemeli a mag énektartományt, hogy előrehozza a hangokat. |
| **Cut Mud** | Kivájja a dobozos alsó-közepes sarat egy tisztább hangzásért. |
| **Tame Harsh** | Egy keskeny vágás egy rikító, átható csúcs megszelídítéséhez. |
| **Punch** | Egy mély kiemelés, amely lökést és ütést ad a mély véghez. |
| **Sub Boost** | Egy mély kiemelés a legalján az extra szub-basszus súlyért. |
| **Air** | Egy széles kiemelés a tetején egy nyitott, levegős fényért. |
| **Clarity** | Megemeli a magas-közepeket a meghatározottság és él hozzáadásához. |
| **De-Ess** | Egy keskeny vágás a sziszegési tartományban a rikító S hangok megszelídítéséhez. |
| **De-Boom** | Levág egy zúgós mélyfrekvenciás felépülést egy szűkebb mély végért. |
| **Scoop** | Egy széles középtartományú mélyedés egy kivájt, modern tónusért. |

### Basszuspolc (basszusvezérlés és basszuskiemelés)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Frekvencia** | Beállítja a sarkot, amely alatt a polc érvényesül. Minden alatta együtt emelkedik vagy vágódik. | 20 és 2000 Hz között (200) |
| **Erősítés** | Mennyivel emeld vagy csökkentsd a mély véget. A pozitív súlyt és meleget ad, a negatív elvékonyítja. | -15 és +15 dB között (0) |

| Preset | Mit csinál |
|---|---|
| **Warmth** | Egy gyengéd mély-végi kiemelés a melegért és testért. Semleges kiindulópont. |
| **Bass Boost** | Egy szilárd basszuskiemelés a súlyért és lökésért. |
| **Fullness** | Kitölti az alsó-közepeket egy teljesebb, kerekebb hangzásért. |
| **Trim Bass** | Egy szerény vágás egy basszus-nehéz keverés könnyítéséhez. |
| **Cut Lows** | Egy erős vágás a mély vég vékonyításához vagy zúgásmentesítéséhez. |
| **Big Bottom** | Egy nagy mély-végi kiemelés a maximális súlyért és dörgésért. |

### Magaspolc (magasvezérlés)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Frekvencia** | Beállítja a sarkot, amely felett a polc érvényesül. Minden felette együtt emelkedik vagy vágódik. | 1 és 20 kHz között (8 kHz) |
| **Erősítés** | Mennyivel emeld vagy csökkentsd a magas véget. A pozitív fényességet és levegőt ad, a negatív simít és sötétít. | -15 és +15 dB között (0) |

| Preset | Mit csinál |
|---|---|
| **Presence** | Egy gyengéd magas-végi kiemelés a tisztaságért és részletért. Semleges kiindulópont. |
| **Air** | Kinyitja a legtetejét egy levegős, nyitott hangzásért. |
| **Bright** | Egy erős kiemelés egy éles, fényes, előretolt tónusért. |
| **Soften** | Egy szerény vágás a rikító magasak élének levételéhez. |
| **Tame Highs** | Egy erős vágás egy túlságosan fényes hangzás sötétítéséhez és simításához. |
| **Sparkle** | Egy nagy felső-végi kiemelés a maximális csillogásért. |

### Lágy klipp (meleg telítettség)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Meghajtás** | Erősebben nyomja a jelet a hullámformálóba. Kis mennyiség gyengéd meleget ad, nagy mennyiség vastag telítettséggé és érdességgé kerekíti a csúcsokat. | 0 és 40 dB között (0) |

| Preset | Mit csinál |
|---|---|
| **Warm** | Egy csipetnyi meghajtás a gyengéd, analóg stílusú melegért. |
| **Drive** | Észrevehető telítettség, amely megvastagítja és színezi a hangzást. |
| **Crunch** | Nehéz meghajtás egy hallható ropogós éllel. |
| **Fuzz** | Vastag, fuzzos torzítás. A csúcsok erősen összenyomva. |
| **Destroy** | Maximális meghajtás. Agresszív, teljesen telített érdesség. |

### Bit Crusher (retró lo-fi)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Bitmélység** | Beállítja, hány bit írja le az egyes mintákat. A kevesebb bit durvább lépcsőket és több kvantálási zajt jelent, egy ropogós, érdes digitális hangzásért. | 1 és 16 bit között (16) |
| **Mintavételi frekvencia** | Lemintavételezi a hangot. Száz százalékon a frekvencia érintetlen, csökkentsd, hogy minden mintát tovább tarts, tompítva a magasakat és egy rikító, aliased élt adva. | 1% és 100% között (100%) |

| Preset | Mit csinál |
|---|---|
| **Vintage** | Egy finom minőségcsökkenés, mint egy korai digitális sampler. |
| **LoFi** | Klasszikus 8 bites, félsebességű lo-fi. Szemcsés és retró. |
| **Crunch** | Nehezebb összezúzás egy hallható ropogós éllel. |
| **Gritty** | Durva és érdes. A szintek közötti lépcsők nyilvánvalók. |
| **Destroy** | Extrém csökkentés. Rikító, tört, alig felismerhető. |

### Gyűrűmodulátor (fémes és robotikus tónusok)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Vivő** | Beállítja a tónus frekvenciáját, amellyel a jel megszorzódik. Néhány hertz tremolo-ingadozást ad, a magasabb frekvenciák fémes, harangszerű és robotikus felharmonikusokat adnak. | 1 és 4000 Hz között (440) |
| **Keverés** | Bekeveri a modulált hangot az eredetivel. Nulla százalékon csak a száraz jelet hallod, száz százalékon csak a teljesen modulált tónust. | 0% és 100% között (0%) |

| Preset | Mit csinál |
|---|---|
| **Tremolo** | Egy nagyon alacsony vivő amplitúdó-tremolóvá teszi, ingadoztatva a hangerőt. |
| **Robot** | Egy közepes vivő zörgő felharmonikusokat ad egy klasszikus robotanghatásért. |
| **Metallic** | Sűrű, inharmonikus felharmonikusok egy rikító, fémes tónusért. |
| **Bell** | Egy magasabb vivő fényes, harangszerű csengést ad. |
| **Alien** | Teljesen nedves, magas vivővel. Extrém, idegen, alig felismerhető. |

### Tremolo (hangerő-ingadozás)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Sebesség** | Beállítja, milyen gyorsan lüktet a hangerő. A lassabb sebességek sima ringást adnak, a gyorsabbak gyors stuttert. | 0,1 és 20 Hz között (5) |
| **Mélység** | Beállítja, mennyire esik a hangerő minden lüktetésnél. Nulla százalékon a szint egyenletes, száz százalékon egészen a csendig süllyed. | 0% és 100% között (0%) |

| Preset | Mit csinál |
|---|---|
| **Gentle** | Egy lassú, sekély ringás. Finom mozgás figyelemfelkeltés nélkül. |
| **Classic** | A klasszikus erősítő-tremolo: egy közepes sebesség és mérsékelt mélység. |
| **Deep** | Egy erős, mély lüktetés, amely minden ciklusban majdnem csendig esik. |
| **Fast** | Egy gyors csapkodás egy csillogó, ideges érzetért. |
| **Chop** | Gyors és teljes mélység. Egy kemény, akadozó vágás. |

### Késleltetés (visszhang)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Idő** | Beállítja a szünetet minden visszhang előtt. A rövid idők szűk slapbacket adnak, a hosszabbak jobban eltávolítják az ismétléseket. | 0,01 és 2 s között (0.25) |
| **Visszacsatolás** | Beállítja, mennyi visszhang csatolódik vissza. Alacsony értékek egyetlen ismétlést adnak, magasabbak egy hosszú, elhúzódó visszhangsorozatot építenek. | 0 és 0,95 között (0.4) |
| **Keverés** | Bekeveri a visszhangokat az eredetivel. Nulla százalékon csak a száraz jelet hallod, száz százalékon csak a visszhangokat. | 0% és 100% között (0%) |

| Preset | Mit csinál |
|---|---|
| **Slapback** | Egyetlen rövid visszhang, szorosan az eredeti mellett. Rockabilly és ének megkettőzés. |
| **Echo** | A klasszikus visszhang: egy tiszta ismétlés néhány elhúzódó utóhanggal. |
| **Ping** | Egy gyors, pattogó ismétlés, amely ritmikus mozgást ad. |
| **Ambient** | Hosszabb, lágyabb ismétlések, amelyek egy tágas utóhangba mosódnak. |
| **Dub** | Magas visszacsatolás hosszú, dubos visszhang-kaszkádokért. |
| **Cavern** | Hosszú, mély ismétlések, mint a hang egy hatalmas téren átvisszhangozva. |

### Sztereó szélesség (szűkít vagy szélesít)

| Vezérlő | Mit csinál | Tartomány (alapérték) |
|---|---|---|
| **Szélesség** | Szűkíti vagy szélesíti a sztereó képet. Nulla százalék monóba omlik, száz százalék érintetlenül hagyja, a magasabb értékek szélesebbre tolják az oldalakat. Csak sztereó számokat érint az Összes-csatorna célon. | 0% és 200% között (100%) |

| Preset | Mit csinál |
|---|---|
| **Wide** | Egy gyengéd szélesítés, amely kinyitja a sztereó képet. Semleges kiindulópont. |
| **Wider** | Egy erősebb kiterjedés egy nagy, magával ragadó sztereó mezőért. |
| **Max** | Maximális szélesség. Nagyon széles, de figyelj a mono-kompatibilitási problémákra. |
| **Narrow** | Behúzza az oldalakat egy szűkebb, központosabb képért. |
| **Focused** | Szinte központosított, épp csak egy csipetnyi sztereóval. |
| **Mono** | Teljesen monóba omlik. Mindkét hangszóró ugyanazt a jelet játssza. |

## Hogyan működik mindez a motorháztető alatt (egyszerű változat)

- **Motorok:** egyet választasz a Beállítások > Audiolejátszó > Lejátszási motor menüben: **Standard** (rendszer), **Universal** (FFmpeg) vagy **Sound FX** (a **BASS™ motor** az [Un4seen Developmentstől](https://www.un4seen.com/)). A választott motor dönti el, mely formátumok játszanak le, és az effektek, a hangszínszabályzó és a DSP-lánc csak a Sound FX motorban futnak.
- **Formátumok:** a BASS™ motor hozzáadja a FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus és modul (tracker) zenét a rendszer- és FFmpeg-formátumok tetejére.
- **Effektek:** a hangszínszabályzó, a kompresszor és a legtöbb effekt a BASS™ effekt-kiegészítőket használja. A Freeverb a Freeverb reverb. A Chorus, Flanger és torzítás klasszikus DirectX-stílusú effekteket használ saját vezérlőkkel.
- **Hangerő-normalizálás:** egy élő **EBU R128** hangosság-kiegyenlítő (a műsorszórásban és streamingben használt hangossági szabvány).
- **Crossfeed:** a **bs2b (Bauer)** crossfeed, a BASS™ motoron belül futtatva.
- **DSP-lánc:** a saját blokkjaid, pontosan abban a sorrendben alkalmazva, ahogy beállítod, minden csatornán vagy csak az egyik oldalon.
- **Kimenet:** beállíthatod a mintavételi frekvenciát, a csatornaszámot és a puffer méretét, hogy illeszkedjen a felszereléshez.

Mivel mindez élőben fut, miközben a zene szól, az effektek:

- **Valós időben** működnek mindenen, beleértve a felhőfájlokat, adásokat és a modul zenét.
- **Sosem változtatják meg vagy mentik újra** a fájljaidat. Kapcsolj ki egy effektet, és az eredeti visszatér.
- **Megjegyzik a beállításaidat** minden effekthez.
- Szabadon **keverhetők és párosíthatók**, mivel mindegyik külön van.

## Egyszerű receptek a kipróbáláshoz

**Mindennapi hallgatás**

- **Több basszus, tisztán:** Hangszínszabályzó > Bass Booster, majd csökkentsd az Előerősítőt 1-2 dB-lel. Vagy adj hozzá egy DSP Basszuspolcot Bass Boost beállításon.
- **Egyenletes hangerő egy kevert lejátszási listán:** Hangerő-normalizálás > Standard, plusz Kompresszor > Soft.
- **Gyengéd általános fényezés:** Kompresszor > Transparent, plusz Hangerő-normalizálás > Light.
- **Tisztább ének:** Hangszínszabályzó > Vocal Booster, vagy egy DSP Kiemelő blokk Vocal Boost beállításon.
- **Teljesebb hangzás kis telefonhangszórókon:** Hangszínszabályzó > Small Speakers.

**Fejhallgató**

- **Kellemesebb, kevésbé fárasztó fejhallgatón:** Crossfeed > Chu Moy vagy Jan Meier.
- **Szélesebb hangzás fejhallgatón:** DSP Sztereó szélesség > Wide, plusz Crossfeed > Chu Moy.
- **Keményen panorámázott 1960-as és 1970-es évekbeli lemezek javítása:** Crossfeed > Vintage Stereo.
- **Egy kis levegő és tér:** Freeverb > Ambience, alacsonyan tartva, plusz Crossfeed > Subtle.

**Csendes idők és beszédhang**

- **Késő esti csendes hallgatás:** Hangerő-normalizálás > Night, plusz Kompresszor > Late Night.
- **Podcastok és hangoskönyvek:** Kompresszor > Voice / Podcast, plusz Hangszínszabályzó > Spoken Word.
- **A leghangosabb, legegyenletesebb hangzás egy zajos autóban:** Hangerő-normalizálás > Strong, plusz Kompresszor > Heavy.

**Problémák javítása**

- **Egy rikító, fényes felvétel megszelídítése:** Hangszínszabályzó > Treble Reducer, vagy egy DSP Kiemelő blokk Tame Harsh beállításon.
- **Elektromos zúgás eltávolítása:** DSP-lánc > Kivágó > Mains Hum 60 (vagy Mains Hum 50 Európában).
- **Szűkebb, tisztább basszus:** DSP Felüláteresztő > Tighten, a zúgós mély vég levágásához.
- **Kevesebb zúgás egy basszus-nehéz keverésben:** DSP Basszuspolc > Trim Bass, vagy Kiemelő > De-Boom.

**Kreatív és szórakoztató**

- **Meleg, tágas érzet:** Freeverb > Hall, alacsonyan tartva.
- **Álmodozó, tágas gitárok:** Chorus > Wide, plusz Visszhang > Long.
- **Retró lo-fi:** DSP-lánc > Bit Crusher (LoFi) a Lágy klippbe (Warm).
- **Funky mozgás elektronikus számokon:** Auto Wah > Funky, vagy Phaser > Fast.
- **Klasszikus sugárhajtómű-söprés:** Flanger > Jet.

## GYIK

{{% details title="Milyen hangmotort használ a Flacbox?" closed="true" %}}
Egyetlen Lejátszási motort választasz a Beállítások > Audiolejátszó menüben: Standard (az Apple rendszermotorja), Universal (az FFmpeg motor) vagy Sound FX (a BASS™ motor az Un4seen Developmentstől, un4seen.com). A választott motor dönti el, mely fájlformátumok játszanak le. A Sound FX az, amely olyan extra formátumokat játszik le, mint a FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus és a MOD vagy tracker zene, és ez az egyetlen motor, amely biztosítja az élő effekteket, a 10 sávos hangszínszabályzót és a DSP-láncot. Az effektek használatához állítsd a Lejátszási motort Sound FX-re.
{{% /details %}}

{{% details title="Le tud játszani a Flacbox MOD, XM, IT és egyéb tracker vagy modul zenét?" closed="true" %}}
Igen. A BASS™ motornak van egy beépített modul lejátszója, amely betölti a MOD, XM, IT, S3M, MTM, UMX és MO3 fájlokat, és élőben újraépíti a dalt a mintáiból és hangszerhangjaiból, ahogyan a tracker zenét lejátszani szánták. A szokványos iPhone-lejátszók erre nem képesek. Az effektek és a hangszínszabályzó a modul zenén is működnek.
{{% /details %}}

{{% details title="Támogatja a Flacbox a DSD és nagy felbontású fájlokat?" closed="true" %}}
Igen. A Flacbox lejátssza a DSD fájlokat (DSF és DFF) a BASS™ motoron keresztül DSD over PCM segítségével, hogy normál kimeneti hardveren működjenek, plusz FLAC, WavPack, Monkey's Audio (APE), Musepack és TrueAudio a veszteségmentes lejátszáshoz.
{{% /details %}}

{{% details title="Milyen hangeffektjei vannak a Flacboxnak?" closed="true" %}}
Egy 10 sávos hangszínszabályzó, hangerő-normalizálás, kompresszor, Freeverb, Auto Wah, Phaser, Flanger, visszhang, Chorus, torzítás, Rotate és Crossfeed, plusz egy saját összeállítású DSP-lánc szűrőkkel, polcokkal, erősítéssel, lágy klippel, bit crusherrel, gyűrűmodulátorral, tremolóval, késleltetéssel és sztereó szélességgel. Mindegyik külön van, és kombinálható a többivel.
{{% /details %}}

{{% details title="Mi az a preset?" closed="true" %}}
A preset egy kész beállítás egy effekthez. Ahelyett, hogy magad mozgatnád a csúszkákat, koppintasz egy presetre, és a hangzás annak megfelelően megváltozik. A Flacbox minden effektjének több presetje van, és ez az útmutató felsorolja, mit csinál mindegyik. Ha egy preset kiválasztása után elmozdítasz egy csúszkát, az effekt «Manuális» állapotot mutat, hogy jelezze, most a saját értékeidet használja.
{{% /details %}}

{{% details title="Hogyan nyitom meg a hangeffekteket a Flacboxban?" closed="true" %}}
Nyisd meg az Épp játszott lejátszót, koppints a ⋯ (Több) gombra, és válaszd a Hangeffektek lehetőséget. Vagy menj a Beállítások > Audiolejátszó > Hangeffektek menübe. Koppints egy effektre, kapcsold be a kapcsolóját, és válassz presetet, vagy nyisd meg a csúszkákat a finomhangoláshoz.
{{% /details %}}

{{% details title="Hol van a hangszínszabályzó, és melyek a legjobb beállítások?" closed="true" %}}
Menj a Beállítások > Audiolejátszó > Hangszínszabályzó menübe. 10 sávja van 32 Hz-től 16 kHz-ig, mindegyik -12-től +12 dB-ig, plusz egy -24-től +24 dB-ig terjedő Előerősítő és 22 preset. Több basszushoz használd a Bass Boostert. Tisztább hangokhoz használd a Vocal Boostert vagy a Popot. Fényesebb hangzáshoz használd a Treble Boostert. Aztán állítsd az egyes sávokat ízlés szerint.
{{% /details %}}

{{% details title="Hogyan emelem ki a basszust a Flacboxban?" closed="true" %}}
Két egyszerű módon. A Hangszínszabályzóban válaszd a Bass Boostert (vagy emeld meg a 32 Hz-es és 64 Hz-es sávokat néhány dB-lel). Vagy a Jelfeldolgozásban adj hozzá egy Basszuspolc blokkot Bass Boost beállításon. Mindkét esetben csökkentsd az Előerősítőt, vagy adj hozzá egy Erősítés blokkot 1-2 dB-lel, hogy a basszus tiszta maradjon és ne torzuljon.
{{% /details %}}

{{% details title="Melyik hangszínszabályzó preset a legjobb a zenémhez?" closed="true" %}}
A Rock és Electronic energiát ad erős mélyekkel és magasakkal. Az Acoustic, Jazz és Classical meleg és természetes marad. A Pop és Vocal Booster előretolja a hangokat. A Bass Booster és Hip-Hop súlyt ad. A Deep és Loudness teljesebben szól alacsony hangerőn. Kezdd azzal, amelyik illik a műfajodhoz, aztán finomhangolj.
{{% /details %}}

{{% details title="Mi az a hangerő-normalizálás, és miben különbözik a ReplayGaintől?" closed="true" %}}
Minden számot nagyjából ugyanolyan hangosságon szólaltat meg. Méri a valós hangosságot az EBU R128 szabvány segítségével (LUFS-ban, mint a streaming szolgáltatások), és minden számot a célértéked felé igazít, egy max-kiemelés korláttal. A ReplayGaintől eltérően nem igényel címkéket a fájljaidban, és bármely forráson működik, élőben, a hang megváltoztatása nélkül. Presetek: Light, Standard, Strong és Night.
{{% /details %}}

{{% details title="Mi az a Crossfeed, és használjam?" closed="true" %}}
A Crossfeed egy kicsit összekever a bal és jobb csatornából, hogy a fejhallgató inkább valós hangszóróknak érződjön, és kevésbé úgy, mintha a hangzás a fejedben ragadt volna. Csak fejhallgatóra való, ezért kapcsold ki hangszórókhoz. A Flacbox a bs2b (Bauer) módszert használja, olyan presetekkel, mint a Chu Moy és Jan Meier.
{{% /details %}}

{{% details title="Mi a különbség a Kompresszor és a hangerő-normalizálás között?" closed="true" %}}
A hangerő-normalizálás a különböző dalok közötti hangosságot illeszti. A Kompresszor a hangos és halk részeket egyenlíti ki egyetlen dalon belül. Különböző problémákat oldanak meg, és jól működnek együtt, különösen autóban vagy zajos helyen.
{{% /details %}}

{{% details title="Mi az a Jelfeldolgozás (DSP) lánc?" closed="true" %}}
Ez egy saját összeállítású állvány a Beállítások > Audiolejátszó > Jelfeldolgozás menüben. Adj hozzá blokkokat, mint szűrők, polcok, erősítés, lágy klipp, bit crusher, gyűrűmodulátor, tremolo, késleltetés és sztereó szélesség, tedd őket bármilyen sorrendbe, kapcsold be vagy ki mindegyiket, és irányítsd a láncot az összes csatornára, a balra vagy a jobbra. Mivel a sorrend számít, pontosan azt a hangzást tervezheted meg, amit szeretnél.
{{% /details %}}

{{% details title="Mi a különbség a hangszínszabályzó, az effektek és a DSP-lánc között?" closed="true" %}}
A hangszínszabályzó egy egyszerű 10 sávos tónusvezérlő. A Hangeffektek kész eszközök (kompresszor, reverb, visszhang és így tovább) presetekkel. A DSP-lánc az, ahol saját effektsorrendedet építed meg egyedi blokkokból. Mindhármat futtathatod egyszerre.
{{% /details %}}

{{% details title="Megváltoztatják vagy károsítják az effektek a zenei fájljaimat?" closed="true" %}}
Nem. Minden élőben alkalmazódik, miközben a zene szól. A fájljaid sosem változnak meg vagy mentődnek újra. Kapcsolj ki egy effektet, és az eredeti hangzás azonnal visszatér.
{{% /details %}}

{{% details title="Használhatok egyszerre egynél több effektet?" closed="true" %}}
Igen. Minden effektnek saját kapcsolója van, és nincs fő kapcsoló, így bármely kombináció működik. Például hangerő-normalizálás plusz Kompresszor az egyenletes hallgatáshoz, vagy Freeverb plusz Crossfeed fejhallgatón, a hangszínszabályzóval a tetején.
{{% /details %}}

{{% details title="Miért szürkék az effekt vezérlői?" closed="true" %}}
Az effekt ki van kapcsolva. Kapcsold be a kapcsolóját a szerkesztő tetején a vezérlők használatához. Minden effekt alapból ki van kapcsolva.
{{% /details %}}

{{% details title="Mit jelent a Manuális címke?" closed="true" %}}
Azt jelenti, hogy elmozdítottál egy csúszkát egy presettől, így az effekt most a saját egyéni értékeidet használja egy megnevezett preset helyett. Minden csúszkának van visszaállító gombja, és egy preset újbóli kiválasztása felülírja a manuális értékeidet.
{{% /details %}}

{{% details title="Elmenthetem és megoszthatom a hangszínszabályzó presetjeimet?" closed="true" %}}
Igen. A 22 beépített preset mellett készíthetsz sajátokat, átrendezheted őket, és exportálhatod vagy importálhatod őket, hogy áthelyezd a beállításaidat egy másik eszközre.
{{% /details %}}

{{% details title="Működnek az effektek CarPlayjal, streaminggel és háttérlejátszással?" closed="true" %}}
Igen. Az effektek a BASS™ motoron belül futnak, így alkalmazódnak a helyi fájlokra, felhőmeghajtókra, médiaszerverekre, adásokra és a modul zenére, és tovább működnek a CarPlay és a háttérlejátszás alatt.
{{% /details %}}

{{% details title="Megváltoztathatom a hangkimenet minőségét?" closed="true" %}}
Igen. A Beállítások > Audiolejátszó menüben beállíthatod a kimeneti mintavételi frekvenciát, a csatornák számát és a puffer méretét, hogy illeszkedjen a fejhallgatódhoz, hangszóróidhoz vagy DAC-odhoz.
{{% /details %}}

{{% details title="Mi egy jó kiinduló beállítás fejhallgatóhoz?" closed="true" %}}
Kapcsold be a hangerő-normalizálást (Standard), adj hozzá egy könnyű Kompresszort (Soft), válassz egy hangszínszabályzó presetet, amit szeretsz, és kapcsold be a Crossfeedet (Chu Moy vagy Jan Meier). Hagyd kikapcsolva a reverbet, visszhangot és torzítást, hacsak nem szeretnél kreatív hangzást.
{{% /details %}}

---

*A BASS az Un4seen Developments Ltd. védjegye. Lásd: [un4seen.com](https://www.un4seen.com/). A Crossfeed a bs2b (Bauer stereophonic-to-binaural) algoritmust használja; lásd a [bs2b projektoldalt](https://bs2b.sourceforge.net/).*
