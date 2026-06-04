---
title: "Audiojátszó"
date: 2020-02-01
description: "Ismerje meg, hogyan használja a Flacbox audiojátszóját iPhone-on, iPaden és Macon. Vezérelje a lejátszást, kezelje a sorokat, konfigurálja az FFmpeg / rendszer hangmotort, változtassa meg a mintavételezési frekvenciát, hangmagasság-korrekciót, IO puffer időtartamát, equalizert, audio könyvjelzőket, AirPlay 2-t, Google Cast-ot, CarPlay-t, widgeteket és Mac billentyűparancsokat."
keywords: [
  "Flacbox lejátszó útmutató", "audiojátszó beállítások", "Flacbox equalizer",
  "AirPlay zene streaming", "Google Cast zene", "audio könyvjelzők",
  "Flacbox lejátszási sor", "Flacbox ismétlés keverés", "Flacbox hangerő vezérlés",
  "macOS mini lejátszó", "VoiceOver zene app",
  "Flacbox FFmpeg", "Flacbox hangmagasság-korrekció", "Flacbox mintavételezési frekvencia",
  "Flacbox külső DAC", "Flacbox surround hang", "Flacbox IO puffer",
  "Flacbox lejátszási sebesség", "Flacbox alvásidőzítő"
]
tags: ["útmutató", "flacbox", "lejátszó"]
readingTime: 14
---


Az Audiojátszó az alkalmazás fő képernyője, ahol vezérli a zenét és a legtöbb lejátszási funkciót. Itt végzi a Flacbox hi-res hangmotor — a rendszer kodekekre és a beépített **FFmpeg** könyvtárra épülve — a nehéz munkát. Fedezzük fel, hogyan használja.

## Az Audiojátszó elérése

A teljes képernyős lejátszóhoz a mini lejátszó sávból juthat. iPhone-on a mini lejátszó a főképernyő alján található. iPaden és Macon a bal oldalon. A mini lejátszó iPhone-on való elrejtéséhez koppintson egyszer és húzza le. A teljes képernyős lejátszó teljes bezárásához koppintson a bezárás gombra a jobb alsó sarokban.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audiojátszó főképernyő" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Támogatott hangformátumok

A Flacbox a legnépszerűbb hangformátumokat játssza le — mind az Apple rendszer kodekjeit, mind a beépített FFmpeg motor által kezelt formátumokat:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

## Lejátszás vezérlők

A lejátszó képernyő alján megtalálja a Lejátszás, Szünet, Következő szám és Előző szám gombokat. Vannak opcionális gombok is, mint a Következő 30 mp és Előző 30 mp, amelyeket az alkalmazás beállításaiban engedélyezhet. Gyorsan előre- vagy visszatekerhet a Következő / Előző gombokat nyomva tartva. A szám egy adott részére való ugráshoz húzza a lejátszási csúszkát.

## Ismétlés és keverés

Koppintson az ismétlés gombra az ismétlési módok közötti váltáshoz:

- **Összes ismétlése** — a sorban lévő összes számot hurokba helyezi.
- **Egy ismétlése** — csak az aktuális számot ismétli.
- **Ismétlés leállítása** — szünetel, amikor az aktuális szám véget ér.
- **Nincs ismétlés** — egyszer lejátssza a sort ismétlés nélkül.

Használja a **Keverés** gombot a sorban lévő számok sorrendjének véletlenszerűsítéséhez.

## Hangerő vezérlés

Nyissa meg a Hangbeállítások képernyőt a lejátszás vezérlők alatti hangikon megnyomásával a hangerő csúszka eléréséhez. Itt talál gombokat is a **Google Cast** és **AirPlay** számára a lejátszás gyors átváltásához egy másik eszközre.

## Google Cast (Chromecast)

Google Cast felhasználók számára a **Cast** ikon megjelenik a lejátszó alján. Koppintson rá egy eszköz kiválasztásához és a streaming megkezdéséhez. Győződjön meg arról, hogy az eszköze és a Google Cast vevő ugyanazon a Wi-Fi hálózaton vannak.

## AirPlay

Az AirPlay esetén keresse az **AirPlay** gombot a lejátszó alján. Koppintson rá és válasszon eszközt a streaminghez. A Flacbox támogatja az **AirPlay 2**-t, így egyszerre több HomePodra, Apple TV-re vagy AirPlay 2-kompatibilis hangszóróra tud lejátszani.

## Audio equalizer

A Flacbox tartalmaz egy **10 sávos equalizert** iPod-stílusú előbeállításokkal. Koppintson az Equalizer lehetőségre a hangerő nézeten, majd kapcsolja be a jobb felső sarokban. Használhat előbeállításokat, mint az Akusztikus és Bass Booster, vagy állítsa be az egyes frekvenciasávokat csúszkákkal. Készítse el saját előbeállításait, mentse azokat bármilyen névvel, és növelje az általános hangerőt a preamplifikátorral. Részletesebb útmutató az equalizer használatáról [itt](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox) érhető el.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audiojátszó Equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Lejátszó mód eszköztár

Néhány lejátszó stílusnál van egy dedikált eszköztár a teljes képernyős lejátszó tetején:

- **Keresés** — gyorsan megtalálhat egy adott számot a lejátszósorban.
- **Lejátszási sebesség vezérlés** — állítsa be a lejátszási sebességet 0,02×-tól 3,00×-ig.
- **Audio könyvjelzők** — számokhoz több könyvjelzőt hozhat létre.

## Lejátszási sor

A lejátszási sor megtekintéséhez koppintson az aktuális dal jobb oldalán lévő sor gombra. A sorban lévő minden dalhoz elérhető további műveletek — koppintson a három pontra a megtekintésükhez. Egy dal sorban való átrendezéséhez használja a cím melletti átrendezés jelzőt és húzza új pozícióba.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lejátszási sor" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Megjegyzések / Dalszövegek

A szám megjegyzéseinek, beágyazott dalszövegek és LRC fájlok megtekintéséhez kövesse az alábbi lépéseket:

1. Nyissa meg a **Beállítások** menüt.
2. Menjen az **Audiojátszó** lehetőségre.
3. Válassza a **Személyre szabás** lehetőséget.
4. Koppintson a **Gombok a főképernyőn** lehetőségre.
5. Engedélyezze a **Megjegyzések** lehetőséget.

Ezt követően koppintson a képernyő alján lévő lejátszási sor gombra többször a borítókép / sor nézet és a megjegyzések nézet közötti váltáshoz. Részletes útmutató [itt](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox) érhető el.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Dalszövegek és megjegyzések képernyő" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Beállítások menü

A lejátszási sorban lévő minden dalhoz tartozik egy menü a dal neve melletti hárompontos gombra koppintva.

- **Következőként lejátszik** — hozzáadja a dalt a lejátszósor tetejéhez.
- **Hozzáadás lejátszási listához** — a dalt egy lejátszási listába foglalja.
- **Hozzáadás a kedvencekhez** — kedvencként jelöli a dalt.
- **Letöltés** — a dalt a helyi fájlokba menti.
- **Audio tagek szerkesztése** — megnyitja a beépített audio tagok szerkesztőjét.
- **Megjelenítés mappában** — feltárja a hangfájl tárolási mappáját.
- **Megjelenítés a Finderben** — Mac-ről importált fájlok esetén.
- **Megnyitás más alkalmazásban** — exportálja a hangfájlt egy másik alkalmazásba.
- **Törlés a sorból** — eltávolítja a kiválasztott dalt az audiojátszó sorából.
- **Törlés a felhőszolgáltatásból** — törli a dalt mind a zenetárból, mind a felhőtárhelyről. **Ez a művelet visszafordíthatatlan.**
- **Törlés a helyi fájlokból** — törli a dalt mind a zenetárból, mind a helyi tárhelyről. **Ez a művelet visszafordíthatatlan.**
- **Törlés a zenetárból** — törli a dalt a zenetárból, miközben a fájl a tárhelyen marad.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Beállítások a lejátszási sorban lévő elemhez" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## További lejátszó műveletek

Koppintson az aktuálisan lejátszott dal nevének bal oldalán lévő **További műveletek** "..." gombra a további műveletek megtekintéséhez.

- **Lejátszás folytatása** — folytatja onnan, ahol abbahagyta.
- **Keresés** — gyorsan megtalálhat egy adott számot az audiojátszó sorában.
- **Könyvjelzők** — megtekintheti a létrehozott audio könyvjelzők listáját.
- **Megjegyzések** — megtekintheti a szám megjegyzéseit és beágyazott dalszövegeket.
- **Sebesség** — beállíthatja a lejátszási sebességet ízlése szerint.
- **Legutóbbiak** — hozzáférhet a nemrég lejátszott dalok listájához.
- **Kedvencek** — megtekintheti kedvenc dalainak gyűjteményét.
- **Audio equalizer** — aktiválhatja az audio equalizert.
- **Alvásidőzítő** — beállíthat egy időzítőt a lejátszás leállítására egy meghatározott időintervallum után.
- **Sor mentése lejátszási listaként** — az aktuális audiojátszó sort új lejátszási listaként menti.
- **Sor törlése** — törli a lejátszósorát és leállítja a lejátszást.
- **Beállítások** — hozzáférhet az audiojátszó beállításaihoz.
- **Súgó** — segítséget és útmutatást kap.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audiojátszó További műveletek képernyő" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Audio könyvjelzők

Ez a funkció lehetővé teszi, hogy több könyvjelzőt hozzon létre a zenetárban lévő számokhoz — tökéletes hangoskönyvekhez, előadásokhoz, hosszú DJ miksekhez vagy kedvenc szám refrén jelöléséhez.

Új könyvjelző létrehozásához:

- Kezdje el a kívánt dal lejátszását.
- Nyissa meg a lejátszó képernyőt.
- Koppintson a **Könyvjelzők** gombra a lejátszó mód eszköztáron.
- Válassza a **Könyvjelző hozzáadása** lehetőséget.
- Válassza ki a könyvjelző idejét és koppintson a **Kész** gombra a jobb felső sarokban.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio könyvjelzők képernyő" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Legutóbbiak és kedvencek

A lejátszó képernyőn koppintson a három pontra a Legutóbbiak és Kedvencek eléréséhez. Részletes útmutató a dal listák exportálásáról [itt](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/) érhető el.

## Apple CarPlay (iPhone)

Csatlakoztassa iPhone-ját autójához USB vagy vezeték nélküli Apple CarPlay segítségével. A CarPlay felület tartalmaz dedikált lapokat a Könyvtárhoz, Kapcsolatokhoz, Helyi fájlokhoz és Beállításokhoz, lejátszásvezérlőkkel, keveréssel, ismétléssel, sor kezeléssel és audio equalizerrel.

[Olvassa el a teljes CarPlay útmutatót](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Apple CarPlay-en" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Kezdőképernyő widgetek (iPhone & iPad)

A Flacbox támogatja az iOS kezdőképernyő és záróképernyő widgeteket. Győződjön meg arról, hogy a Widgetek engedélyezve vannak a Beállítások → Widgetek → Widgetek engedélyezése menüpontban, majd nyomja meg hosszan a kezdőképernyőt vagy záróképernyőt, koppintson a **+** gombra, keresse meg a **Flacboxot** és adjon hozzá egy widgetet.

## Mini lejátszó ablak (csak Mac)

A Mac felhasználók kompakt, mindig a többi ablak felett lebegő mini lejátszót használhatnak. Vigye a kurzort a Flacbox ablak jobb alsó sarkára, méretezze le, majd koppintson az összecsukás gombra.

## Billentyűparancsok (csak Mac)

Mac felhasználók számára elérhető a szóköz gomb lejátszás / szünet funkcióhoz. Állj meg, Következő dal, Előző dal, Idő kihagyása, Ismétlés, Keverés és Lejátszási sebesség parancsok is elérhetők.

## Audiojátszó beállítások

A beállítások eléréséhez koppintson a Tovább gombra a lejátszó képernyőn és válassza a Beállítások lehetőséget.

### Általános

- **Ismétlési mód** — válassza ki, hogyan viselkedjen az audiojátszó, amikor egy szám véget ér.
- **Keverési mód** — véletlenszerűsítse a számok sorrendjét.
- **Audio kodek** — válassza a lejátszáshoz használt hangmotort (System Codec + FFmpeg vagy FFmpeg).
- **Audio kimenet mintavételezési frekvencia** — beállítható értékek: 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz és 96 kHz.
- **Audio kimenet csatornák száma** — Mono, Sztereó, Center / Left / Right, stb.
- **Audio kimenet preferált IO puffer időtartama** — konfigurálja a puffer időtartamát.
- **Audio kimenet mód (csak iOS)** — konfigurálja a kevert audio kimenet módot.
- **Lejátszási pozíció mentése** — elmenti és visszaállítja a lejátszási pozíciót.
- **Audiojátszó állapot mentése** — megőrzi az audiojátszó állapotát.

### Személyre szabás

- **Audiojátszó képernyő stílus** — konfigurálja az elemek elhelyezkedését.
- **Albumborítók görgetési stílusa** — konfigurálja a preferált görgetési stílust.
- **További elemek** — extra elemek engedélyezése a lejátszó képernyőn.
- **Főképernyő műveletek** — konfigurálja, mely gombok legyenek láthatók.
- **Lejátszásvezérlők a záróképernyőn** — válassza ki, mely vezérlők jelenjenek meg.
- **Idő kihagyása gombok** — válasszon idő intervallumot.

### Fájl betöltés

- **Előbetöltési idő** — állítsa be a pufferelési idő intervallumát.
- **Közvetlen URL használata** — ha engedélyezve van, közvetlen URL-t használ a dal betöltéséhez.

### Audio equalizer

Konfigurálja a 10 sávos audio equalizert. Részletes útmutató [itt](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox) érhető el.

### Lejátszási sebesség

Állítsa be a lejátszási sebességet **0,02×-tól 3,00×-ig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lejátszási sebesség képernyő" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Hangmagasság-korrekció

Módosítsa a hangmagasság-korrekció beállításait. Az elérhető értékek tartománya **-1000-től +1000-ig** terjed.

### Lejátszási gyorsítótár

A lejátszósorban lévő dalokat automatikusan letöltik a gördülékeny lejátszás biztosításához. Beállíthatja az audiojátszó gyorsítótár méretét is.

### Alvásidőzítő

Aktiváljon egy időzítőt a lejátszás automatikus leállításához egy meghatározott időszak után.

## Akadálymentesítés

A Flacbox teljesen hozzáférhető **VoiceOver**-rel. Minden komponensnek jól megtervezett jelölése és leírása van. Amikor a VoiceOver aktív, az alkalmazás **Szöveges módra** vált.

### Csúszkák beállítása VoiceOver-rel

1. **Válassza ki a csúszkát** — húzza balra vagy jobbra, amíg a VoiceOver be nem jelenti.
2. **Módosítsa az értéket** — koppintson duplán és tartsa a csúszkát, majd húzza fel vagy le.

### Szám pozíciójának beállítása listában VoiceOver-rel

1. Koppintson az átrendezés jelző ikonra a szám neve mellett.
2. Gyorsan koppintson duplán az átrendezés jelzőre. A második koppintásnál ne engedje fel az ujját.
3. Mozgassa a cellát az új pozíciójára.
