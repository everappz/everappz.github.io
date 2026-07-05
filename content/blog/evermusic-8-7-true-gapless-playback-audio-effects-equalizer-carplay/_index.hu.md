---
title: "Evermusic 8.7: valódi szünetmentes lejátszás, hangeffektek, hangerő-normalizálás, újratervezett hangszínszabályzó"
date: 2026-07-05
description: "Az Evermusic 8.7 iPhone-ra, iPadre és Mac-re valódi szünetmentes lejátszást, öt stúdiós hangeffektet (zengetés, visszhang, torzítás, kompresszor, keresztátfedés), EBU R128 hangerő-normalizálást, importálható/exportálható előbeállításokkal újratervezett 10 sávos hangszínszabályzót, FLAC és Ogg Vorbis támogatással újraépített AVAudioEngine streaming motort, valamint gyorsabb és pontosabb CarPlay-t és Most játszottat hoz."
keywords: ["Evermusic 8.7", "Evermusic frissítés", "valódi szünetmentes lejátszás iPhone", "szünetmentes zenelejátszó iOS", "szünetmentes lejátszás CarPlay", "zenelejátszó hangeffektek iPhone", "zengetés visszhang torzítás kompresszor keresztátfedés iOS", "keresztátfedés fejhallgató iOS", "hangerő-normalizálás iPhone", "hangosság-normalizálás zenelejátszó", "EBU R128 normalizálás iOS", "replay gain alternatíva iPhone", "10 sávos hangszínszabályzó iPhone", "grafikus hangszínszabályzó iOS app", "hangszínszabályzó előbeállítások importálás exportálás", "FLAC lejátszó iPhone", "Ogg Vorbis lejátszó iOS", "veszteségmentes zenelejátszó iPhone 2026", "AVAudioEngine zenelejátszó", "CarPlay zenelejátszó iPhone", "Most játszott zárolási képernyő pontosság", "felhő zenelejátszó iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Szünetmentes lejátszás", "Hangeffektek", "Zengetés", "Visszhang", "Torzítás", "Kompresszor", "Keresztátfedés", "Hangerő-normalizálás", "EBU R128", "Hangszínszabályzó", "FLAC", "Ogg Vorbis", "CarPlay", "Most játszott", "Liquid Glass", "Újdonságok"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Röviden:** Az [Evermusic 8.7](/products/evermusic) egy hangminőségre fókuszáló kiadás iPhone-ra, iPadre és Mac-re. **Valódi szünetmentes lejátszást** hoz (nincs szünet, kattanás vagy pattanás a számok között), egy teljes **stúdiós hangeffekt-készletet** — zengetés, visszhang, torzítás, kompresszor és keresztátfedés — valamint **EBU R128 hangerő-normalizálást**, amely ReplayGain-címkék nélkül tartja állandón a hangosságot dalról dalra. A **10 sávos hangszínszabályzót** új csúszkákkal, gyorsabb előbeállítás-váltással, importálható és exportálható egyéni előbeállításokkal, valamint jobb fekvő és iPad-elrendezéssel tervezték újra. A háttérben egy **újraépített AVAudioEngine streaming motor** javítja a megbízhatóságot és a formátumtámogatást, beleértve a **FLAC** és **Ogg Vorbis** formátumokat. A **CarPlay** és a **Most játszott** gyorsabb és pontosabb a zárolási képernyőn, az autóban és a fejhallgató távvezérlőin.

---

## Sziasztok!

Az Evermusic 8.7 letölthető. Ez a frissítés arról szól, hogyan *szól* a zenéd. Újraépítettük a lejátszómotort a valódi szünetmentes lejátszásért, hozzáadtunk egy stúdiós minőségű hangeffekt-készletet, bevezettük a hangerő-normalizálást, és a csúszkáktól kezdve újraterveztük a hangszínszabályzót. Mindezt az Apple új **Liquid Glass** dizájnjába csomagoltuk.

[Töltsd le az Evermusic 8.7-et az App Store-ból](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), vagy frissíts a meglévő verziódról. Az Evermusic ingyenesen letölthető, opcionális alkalmazáson belüli bővítésekkel.

## Valódi szünetmentes lejátszás

A szünetmentes lejátszás azt jelenti, hogy a két szám közötti csend eltűnt. Nincs szünet, nincs kattanás, nincs pattanás: az aktuális dal közvetlenül a következőbe folyik. Leginkább az olyan zenénél számít, amelyet egésznek szántak: **élő felvételek, DJ mixek, klasszikus művek és koncepcióalbumok**, ahol az egyik szám közvetlenül egy másikba tűnik.

Íme, mi változott technikailag. Az Evermusic hangmotorja egyszerre két számot tart lejátszásban: azt, amelyiket hallgatod, és a következőt a sorban. Miközben az aktuális szám szól, a következőt már **lekéri, dekódolja és előre pufferolja** a háttérben. Amikor az aktuális szám a végére ér, a motor **a lejátszón belül, nem a hangfolyamon belül** adja át a következő számnak. A kimeneti renderelési ciklus megállás nélkül folytatja a hangminták húzását egy folyamatos gyűrűpufferből, így a hallgató soha nem hall határt. A váltás a minták között történik, és pontosan ezért nincs hallható szünet.

Ez ugyanúgy működik, akár az eszközödön, akár a felhőben, akár egy médiaszerveren van a fájl: az előpufferelés távoli forrásoknál egyszerűen egy kicsit korábban kezdődik.

## Stúdiós hangeffektek

Az Evermusic 8.7 öt valós idejű hangeffektet ad hozzá, amelyeket a zenédre rétegezhetsz. Mindegyik natív hangfeldolgozó csomópontként fut a lejátszómotorban, így mindenre alkalmazódik, amit lejátszol — helyi fájlokra, felhőalapú streamekre és internetes rádióra egyaránt — újrakódolás nélkül.

Minden effekt egy **gondosan összeállított előbeállítás-könyvtárral** érkezik, hogy egyetlen koppintással remek hangzást érj el, és az Evermusic **megjegyzi a pontos beállításaidat** a munkamenetek között. Állíts bármelyik vezérlőn, és az effekt **Kézi** állapotba vált, így mindig tudod, mikor tértél el egy előbeállítástól.

### Zengetés

Teret ad a hangzásnak, egy feszes szobától egy katedrálisig. Az Apple `AVAudioUnitReverb` alapjaira épül, **13 teremelőbeállítást** kínál (Kis szoba, Közepes terem, Lemez, Katedrális és mások), valamint egy **wet/dry keverés** vezérlőt 0-tól 100%-ig, így te döntöd el, mennyi teret adsz hozzá.

### Visszhang (Echo)

Egy klasszikus visszhang **10 előbeállítással** — Slapback, Szalagvisszhang, Dub, Atmoszférikus és mások. Beállíthatod a **késleltetési időt** (akár 2 másodpercig), a **visszacsatolást** (hány ismétlés), egy **aluláteresztő levágást** az ismétlések melegítéséhez, valamint a **wet/dry keverést**.

### Torzítás

A finom érdességtől a teljes lo-fi rombolásig, amit az `AVAudioUnitDistortion` hajt **22 karakteres előbeállítással** (Bit Brush, Cellphone Concert, Radio Tower és mások), egy **elő-erősítés** meghajtó vezérlővel és egy wet/dry keveréssel, így visszakeverheted az effektet a tiszta jelbe.

### Kompresszor

Egy dinamikafeldolgozó (az Apple `AUDynamicsProcessor` egysége), amely kiegyenlíti a hangos és halk szakaszokat. A teljes professzionális vezérlőkészletet elérhetővé teszi — **küszöb, arány/fejtér, felfutás, lecsengés, expanzió és kiegyenlítő erősítés** — **10 előbeállítással**, amelyeket valós helyzetekre hangoltak: többek között Beszéd / Podcast, Késő éjszaka, Filmpárbeszéd, Streaming-illesztés és Maximális hangosság.

### Keresztátfedés

A keresztátfedés természetesebbé teszi a fejhallgatós hallgatást azáltal, hogy egy kicsit a bal csatornából a jobbba kever és fordítva, ahogyan a füled a valódi hangszórókat hallja. A jól ismert **Bauer stereophonic-to-binaural (bs2b)** algoritmusra épül, a **keresztátfedési szint** és a **levágási frekvencia** vezérlésével, valamint **6 előbeállítással**, köztük az audiofil kedvenc *Chu Moy* és *Jan Meier* beállításokkal. Különösen jól működik a régebbi, erősen szétpanorámázott 1960-as és 1970-es évekbeli sztereó keverékeken.

## Hangerő-normalizálás

Építettél már olyan lejátszási listát, ahol az egyik szám bömböl, a következő pedig suttog? A hangerő-normalizálás ezt orvosolja. Az Evermusic 8.7 **EBU R128 hangosságmérést** használ (ugyanaz az ITU-R BS.1770 szabvány, amelyet a műsorszórásban és a streaming szolgáltatásoknál használnak) minden szám valós észlelt hangosságának mérésére, és finoman egy állandó célérték felé tereli azt.

A ReplayGaintől eltérően **nem** igényel semmilyen címkét a fájljaidban, és **nem** módosítja a hangodat. Valós időben működik mindenen, amit lejátszol, beleértve a felhőalapú streameket és az élő rádiót, és tisztán visszaáll, amikor keresel vagy számot váltasz.

Négy előbeállítás fedi le a gyakori eseteket:

- **Enyhe** — finom kiegyenlítés (célérték −20 LUFS).
- **Normál** — az alapértelmezett, streaming stílusú hangosság (célérték −16 LUFS, akár +12 dB emelés a halk számoknál).
- **Erős** — agresszív illesztés a nagyon vegyes gyűjteményekhez (célérték −14 LUFS).
- **Éjszakai** — halkabb és állandó a kis hangerejű esti hallgatáshoz (célérték −23 LUFS).

Többé nem kell a hangerőhöz nyúlnod a dalok között.

## Újratervezett hangszínszabályzó

Az Evermusic **10 sávos grafikus hangszínszabályzója** teljes átalakításon esett át. A sávok **32 Hz-től 16 kHz-ig** terjednek (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), mindegyik **−12 dB-től +12 dB-ig** állítható finom, 0,1 dB-es lépésekben, egy **előerősítővel** −24 dB-től +24 dB-ig, hogy megelőzd a torzulást, amikor emelsz.

Mi az újdonság a 8.7-ben:

- **Új csúszkák** — precíz, reszponzív vezérlők, amelyek az iOS 26 natív rendszercsúszkájának megjelenését és a **Liquid Glass** anyagot veszik át.
- **Gyorsabb, simább előbeállítás-váltás** — ugorj az előbeállítások között azonnal, egy újratervezett vízszintes előbeállítás-sávval álló nézetben és egy függőleges előbeállítás-oszloppal fekvő nézetben.
- **Jobb elrendezés fekvő nézetben és iPaden** — a csúszkák és az előbeállítás-választó átrendeződik, hogy kihasználja a plusz szélességet, ahelyett, hogy egy telefonméretű oszlopba zsúfolódna.
- **Egyéni előbeállítások** — hozd létre és mentsd el a saját görbéidet, rendezd át őket, és **importáld és exportáld** az előbeállításokat `.eqp` fájlként, hogy áthelyezd őket az eszközök között vagy megoszd őket.

A hangszínszabályzó natívan fut a motorban (`AVAudioUnitEQ`), így minden forrásra alkalmazódik, és AirPlay, Chromecast és CarPlay felett is működik, ahol támogatott.

## Újraépített lejátszómotor

A háttérben az Evermusic 8.7 egy **újraépített streaming motoron** fut, amely az Apple `AVAudioEngine` egységére épül, egyedi renderelési folyamattal. Ez teszi lehetővé a szünetmentes átadást, az effektláncot és a hangszínszabályzót, és a mindennapi lejátszást is megbízhatóbbá teszi.

- **Továbbfejlesztett formátumtámogatás** — beleértve a **FLAC** (Core Audio révén) és **Ogg Vorbis** (a `libvorbisfile` révén) formátumokat, az MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF és mások mellett.
- **Okosabb pufferelés** — egy adaptív előpuffer a kapcsolatoddal skálázódik, egy folyamatos gyűrűpufferrel, amely táplálja a kimenetet, így a rövid hálózati zökkenők nem válnak kimaradásokká.
- **Automatikus helyreállítás** — egy újrapufferelési állapotgép és egy visszalépéses újrapróbálkozási logika tisztán folytatja a lejátszást egy gyenge jelű pillanat után, ahelyett, hogy leállítaná a számot.
- **Kevesebb megszakítás** — ugyanaz a motor hajtja a helyi fájlokat, a felhőalapú streameket, a médiaszervereket és az internetes rádiót, így a viselkedés mindenhol következetes.

## Most játszott és CarPlay

A képernyők, amelyeket valójában nézel hallgatás közben — a **zárolási képernyő**, a **CarPlay** és az autó vagy a fejhallgató távvezérlő gombjai — pontosabbak és gyorsabbak a 8.7-ben.

- **Pontosabb Most játszott információk.** Az Evermusic zárolás alatt rögzíti a lejátszó állapotát, mielőtt közzétenné, így a cím, az eltelt idő, a hossz és a lejátszás/szünet állapot soha nem mondhatnak ellent egymásnak a zárolási képernyőn vagy az autóban. A pufferelési és betöltési állapotok most már helyesen jelennek meg, ahelyett, hogy „lejátszást" mutatnának, miközben egy szám még lekérés alatt van.
- **Megbízható távvezérlők.** A lejátszás, szünet, következő, előző, keresés, ugrás, keverés, ismétlés és lejátszási sebesség mind következetesen reagál a fejhallgató gombjairól, az autó vezérlőiről és a zárolási képernyőről, amelyeket az `MPRemoteCommandCenter` hajt.
- **Gyorsabb CarPlay borítók.** Az albumborítók most többszörösen gyorsabban töltődnek be a hosszú listákon (a kötegütemezés 1,0 másodpercről 0,25 másodpercre csökkent, az első látható képernyő azonnal betöltődik), és most már megjelennek a kompakt iOS 26 CarPlay listasorokban, amelyek korábban nem mutattak borítót.
- **CarPlay rendezési és stabilitási javítások.** Gyorsabb rendezés nagy könyvtárakon, és megerősítés a szélsőséges esetekben előforduló összeomlások ellen hosszú listák görgetésekor.
- **Korlátozott metaadat-frissítések.** A Most játszott és a távvezérlő frissítései korlátozottak, így a gyors változások többé nem árasztják el a rendszert, ami reszponzívan tartja a zárolási képernyő és a CarPlay vezérlőit.

## További fejlesztések

- **Liquid Glass dizájn** finomítások az egész alkalmazásban — áttetsző felületek, simább animációk és letisztult vezérlők iOS-en, iPadOS-en és macOS-en.
- **Új kezdőképernyő-modulok** továbbfejlesztett frissítési logikával, amely szinkronban tartja őket anélkül, hogy extra akkumulátort merítene.
- Javítások a legutóbbi iOS-kiadásokhoz.
- Lokalizációs javítások több nyelven.
- Számos kisebb fejlesztés az e-mailjeitek és App Store-értékeléseitek alapján.

## Miért fontos ez a frissítés

Az Evermusic 8.7 egyetlen gondolat köré épül: **a zenédnek a legjobban kell szólnia, bármilyen forráson.**

1. **Teljes albumok, ahogyan szánták.** A valódi szünetmentes lejátszás azt jelenti, hogy az élő szettek, a DJ mixek és a koncepcióalbumok végre úgy szólnak, ahogyan az előadó maszterelte őket.
2. **Egy stúdió a zsebedben.** A zengetés, a visszhang, a torzítás, a kompresszor, a keresztátfedés, egy újratervezett hangszínszabályzó és a hangerő-normalizálás valódi irányítást ad a hangzásod felett, nem csak egy be/ki kapcsolót.
3. **Ugyanaz az élmény mindenhol.** A helyi fájlok, a felhőmeghajtók, a médiaszerverek és az internetes rádió mind ugyanazon az újraépített motoron futnak át, pontos Most játszottal és gyorsabb CarPlay-jel a tetején.

## Szerezd meg az Evermusic 8.7-et

[**Töltsd le az Evermusicot az App Store-ból**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), vagy frissíts az App Store-on belül. Az Evermusic ingyenesen letölthető, opcionális alkalmazáson belüli bővítésekkel a haladó funkciókhoz.

Ha tetszik az alkalmazás, kérjük, hagyj egy értékelést az App Store-ban — valóban sokat segít. Van visszajelzésed, vagy problémába ütköztél? Írj nekünk a **support@everappz.com** címre. Minden üzenetet elolvasunk.

## Gyakran ismételt kérdések

{{% details title="Mi az újdonság az Evermusic 8.7-ben?" closed="true" %}}
Az Evermusic 8.7 valódi szünetmentes lejátszást, öt stúdiós hangeffektet (zengetés, visszhang, torzítás, kompresszor és keresztátfedés), EBU R128 hangerő-normalizálást, egyéni előbeállításokkal és importtal/exporttal újratervezett 10 sávos hangszínszabályzót, továbbfejlesztett formátumtámogatással (beleértve a FLAC és Ogg Vorbis formátumokat) újraépített AVAudioEngine streaming motort, gyorsabb és pontosabb CarPlay-t és Most játszottat, Liquid Glass dizájnfrissítéseket, felfrissített kezdőképernyő-modulokat, valamint hiba- és lokalizációs javításokat ad hozzá.
{{% /details %}}

{{% details title="Van az Evermusicnak valódi szünetmentes lejátszása?" closed="true" %}}
Igen. Az Evermusic 8.7-tel kezdve a lejátszás valóban szünetmentes: nincs szünet, kattanás vagy pattanás a számok között. A motor előre pufferolja és dekódolja a következő számot, miközben az aktuális szól, majd egy folyamatos gyűrűpufferen a hangminták között adja át, így az átmenet hallhatatlan. Helyi fájlokkal, felhőalapú streamekkel és médiaszerverekkel is működik, és ideális élő albumokhoz, DJ mixekhez és koncepcióalbumokhoz.
{{% /details %}}

{{% details title="Milyen hangeffekteket tartalmaz az Evermusic 8.7?" closed="true" %}}
Öt valós idejű effektet: **zengetés** (13 teremelőbeállítás, wet/dry keverés), **visszhang/echo** (10 előbeállítás késleltetési idővel, visszacsatolással, aluláteresztővel és keveréssel), **torzítás** (22 karakteres előbeállítás elő-erősítéssel és keveréssel), **kompresszor** (egy teljes dinamikafeldolgozó küszöbbel, aránnyal, felfutással, lecsengéssel, expanzióval és kiegyenlítő erősítéssel, plusz 10 előbeállítással), és **keresztátfedés** (Bauer bs2b fejhallgatós keresztátfedés szint- és levágásvezérlőkkel és 6 előbeállítással). Minden effekt gondosan összeállított előbeállításokkal érkezik, és az egyéni beállításaidat megjegyzi a munkamenetek között.
{{% /details %}}

{{% details title="Mi a keresztátfedés, és miért használnám?" closed="true" %}}
A keresztátfedés mindkét sztereó csatornából egy kis, szűrt mennyiséget kever a másikba, ahogyan a füled természetesen hallja a valódi hangszórókat egy szobában. Fejhallgatón ez csökkenti a szétpanorámázott felvételek eltúlzott, „fejben lévő" szétválasztását, és kényelmesebbé teszi a hosszú hallgatást. Az Evermusic a jól ismert Bauer stereophonic-to-binaural (bs2b) algoritmust használja, és olyan előbeállításokat tartalmaz, mint a Chu Moy és a Jan Meier. Különösen hatékony a régebbi 1960-as és 1970-es évekbeli sztereó keverékeken.
{{% /details %}}

{{% details title="Hogyan működik a hangerő-normalizálás az Evermusicban?" closed="true" %}}
Az Evermusic 8.7 valós időben méri minden szám észlelt hangosságát az EBU R128 szabvánnyal (ITU-R BS.1770), és finoman egy állandó célérték felé állítja a szintet, hogy a számok ne ugorjanak hangerőben. Nem igényel ReplayGain-címkéket, és nem módosítja a fájljaidat. Négy előbeállítás érhető el — Enyhe (−20 LUFS), Normál (−16 LUFS), Erős (−14 LUFS) és Éjszakai (−23 LUFS) — és a normalizálás tisztán visszaáll, amikor keresel vagy számot váltasz.
{{% /details %}}

{{% details title="Az Evermusic hangerő-normalizálása ugyanaz, mint a ReplayGain?" closed="true" %}}
Ugyanazt a célt éri el — állandó hangosságot a számok között — de másképp működik. A ReplayGain a fájljaidban tárolt hangosságcímkékre támaszkodik. Az Evermusic normalizálója élőben méri a hangosságot az EBU R128 segítségével, így bármilyen forráson működik, beleértve a felhőalapú streameket és az internetes rádiót, még akkor is, ha a fájloknak egyáltalán nincsenek címkéik.
{{% /details %}}

{{% details title="Hány sávja van az Evermusic hangszínszabályzójának, és készíthetek saját előbeállításokat?" closed="true" %}}
Az Evermusic hangszínszabályzója egy 10 sávos grafikus hangszínszabályzó, amely 32 Hz-től 16 kHz-ig terjed, minden sáv −12 dB-től +12 dB-ig állítható 0,1 dB-es lépésekben, egy előerősítővel −24 dB-től +24 dB-ig. Beépített előbeállításokat tartalmaz, lehetővé teszi egyéni előbeállítások létrehozását és mentését, és támogatja az előbeállítások importálását és exportálását .eqp fájlként, így áthelyezheted vagy megoszthatod őket az eszközök között.
{{% /details %}}

{{% details title="Mi változott az Evermusic 8.7 hangszínszabályzójában?" closed="true" %}}
A hangszínszabályzót új, precízebb csúszkákkal tervezték újra, amelyek az iOS 26 rendszercsúszka és a Liquid Glass megjelenését veszik át, gyorsabb és simább előbeállítás-váltással, valamint jobb elrendezéssel fekvő nézetben és iPaden (vízszintes előbeállítás-sáv álló nézetben és függőleges előbeállítás-oszlop fekvő nézetben). Az egyéni előbeállítások és az .eqp import/export támogatott.
{{% /details %}}

{{% details title="Támogatja az Evermusic 8.7 a FLAC és Ogg Vorbis formátumokat?" closed="true" %}}
Igen. Az újraépített motor lejátssza a FLAC (Core Audio révén) és Ogg Vorbis (libvorbisfile révén) formátumokat, az MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF és mások mellett, helyi fájlokból, felhőmeghajtókról és médiaszerverekről.
{{% /details %}}

{{% details title="Mi javult a CarPlay-ben és a zárolási képernyőn?" closed="true" %}}
A CarPlay albumborítói többszörösen gyorsabban töltődnek be a hosszú listákon, és most már megjelennek a kompakt iOS 26 listasorokban, amelyek korábban egyáltalán nem mutattak. A Most játszott információk a zárolási képernyőn és a CarPlay-ben pontosabbak — a cím, az eltelt idő, a hossz és a lejátszás/szünet állapot együtt kerül rögzítésre, így nem mondhatnak ellent egymásnak, és a pufferelési állapotok helyesen jelennek meg. A távvezérlők (lejátszás, szünet, következő, előző, keresés, keverés, ismétlés, sebesség) megbízhatóan reagálnak a fejhallgatóról és az autóból, és a CarPlay rendezése nagy könyvtárakon gyorsabb.
{{% /details %}}

{{% details title="Működnek a hangeffektek és a hangszínszabályzó felhőalapú streameléssel és CarPlay-jel?" closed="true" %}}
Igen. Az effektek, a hangszínszabályzó és a hangerő-normalizálás natívan futnak a lejátszómotoron belül, így mindenre alkalmazódnak, amit az Evermusic lejátszik — helyi fájlokra, felhőmeghajtókra, médiaszerverekre és internetes rádióra — és továbbra is működnek CarPlay-lejátszás közben, valamint ahol támogatott, AirPlay és Chromecast felett.
{{% /details %}}

{{% details title="Ingyenes az Evermusic 8.7 frissítése, és mely eszközöket támogatja?" closed="true" %}}
Igen. Az Evermusic ingyenesen letölthető az App Store-ból, és a 8.7 ingyenes frissítés a meglévő felhasználók számára, opcionális alkalmazáson belüli bővítésekkel a haladó funkciókhoz. iPhone-on, iPaden és Mac-en fut. A CarPlay-hez CarPlay-kompatibilis jármű vagy fejegység szükséges.
{{% /details %}}
