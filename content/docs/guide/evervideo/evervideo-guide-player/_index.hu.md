---
title: "Médialejátszó"
date: 2020-02-01
lastmod: 2026-06-01
description: "Ismerje meg, hogyan használhatja az Evervideo médialejátszóját iPhone-on, iPaden és Macon. Kép-a-képben, hardveres H.264 / HEVC dekódolás, hang- és videóegyenlítők, elsődleges és másodlagos feliratok, hang- és videósáv-kiválasztás, videó méretezés és forgatás, lejátszási sebesség, elalvásidőzítő, AirPlay 2, Google Chromecast, RTSP streamek és a kompakt, mindig látható lejátszó."
keywords: [
  "Evervideo lejátszó útmutató", "videólejátszó beállítások", "Evervideo egyenlítő",
  "Kép-a-képben iPhone", "PiP videó iPad", "PiP videó Mac",
  "AirPlay 2 videó", "Google Chromecast videó",
  "videófelirat iPhone", "külső SRT feliratok",
  "ASS SSA feliratlejátszó", "libass iOS",
  "kettős feliratok nyelvtanuláshoz",
  "videóegyenlítő fényerő kontraszt", "hangegyenlítő videólejátszó",
  "videólejátszó forgatás zár", "videó méretezési mód iOS",
  "hardveres H.264 dekóder iPhone", "hardveres HEVC dekóder iPad",
  "lejátszási sebesség videó", "FFmpeg videólejátszó iOS",
  "RTSP iPhone lejátszó", "kompakt videólejátszó",
  "VR 360 fokos videólejátszó iPhone"
]
tags: ["útmutató", "evervideo", "lejátszó", "PiP", "feliratok", "videóegyenlítő"]
readingTime: 14
---


A Médialejátszó az alkalmazás főképernyője, ahol irányíthatja a lejátszást és az Evervideo legtöbb funkcióját. Mind videó, mind hangfájlokat lejátssza, és egyedi FFmpeg-alapú lejátszóra épül, hardveres H.264 és HEVC dekódolással. Fedezzük fel, hogyan kell használni.

## A Médialejátszó elérése

A teljes képernyős lejátszóhoz a kompakt lejátszósávból juthat el. iPhone-on a kompakt lejátszó a főképernyő tetején található. iPaden és Macon a bal oldalon (vagy a főpanel tetején) van. A teljes képernyős lejátszónak kompakt nézetbe való visszazárásához érintse meg a jobb alsó sarokban lévő bezárás gombot, vagy húzzon le. A kompakt lejátszó teljes elrejtéséhez érintse meg és húzza le még egyszer.

A kompakt lejátszó látható marad, miközben böngészi a könyvtárat, a fájlkezelőt vagy a beállításokat, így soha nem veszíti el a videóját, miközben a következőt keresi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo teljes képernyős médialejátszó" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Támogatott videó- és hangformátumok

Az Evervideo a beágyazott FFmpeg motoron keresztül szinte minden modern tárolóformátumot és kodeket lejátssza, hardveres H.264 és HEVC dekódolással a támogatott eszközökön.

- **Videótárolók:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — és sok más.
- **Videokodekek:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plusz szinte minden más, amit az FFmpeg támogat.
- **Hangkodekek:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — és sok más.
- **Felirat formátumok:** SRT, VTT (WebVTT), ASS / SSA és beágyazott szöveges vagy képes feliratsávok.
- **Streaming protokollok:** HTTP / HTTPS, HLS (m3u8), RTSP (IP kamerák és IPTV) és közvetlen fájlstreaming SMB / WebDAV / FTP / SFTP / NFS / DLNA protokollokon.

Ez szinte minden valószínűleg előforduló videófájlt lefed — beleértve az MKV rippeket, a biztonsági kamera RTSP streameket és az AV1 webm webes letöltéseket.

## Lejátszásvezérlők

A lejátszóképernyő alján Lejátszás, Szünet, Következő és Előző gombokat talál. Opcionális gombok is elérhetők, mint például az Ugrás előre és az Ugrás hátra (alapértelmezés szerint 10 másodperc), amelyeket engedélyezhet az alkalmazásbeállításokban. Tartsa lenyomva a Következő / Előző gombokat a gyors előre- vagy visszatekeréshez. Húzza a lejátszási csúszkát bármely pozícióba való ugráshoz.

## Ismétlés és keverés

Érintse meg az ismétlés gombot az ismétlési módok váltogatásához:

- **Összes ismétlése** — a sor összes videóját ismételve lejátssza.
- **Egy ismétlése** — csak az aktuális videót ismétli.
- **Ismétlés leállítása** — szünetel, amikor az aktuális videó véget ér.
- **Nincs ismétlés** — a sort egyszer lejátssza ismétlés nélkül.

Használja a **Keverés** gombot a videók sorrendjének véletlenszerűsítéséhez.

## Kép-a-képben (PiP)

iPhone-on és iPaden az Evervideo teljes mértékben támogatja a Kép-a-képben (PiP) funkciót. Érintse meg a PiP ikont a lejátszóképernyőn, vagy egyszerűen húzza az Evervideót a háttérbe — a videó folytatódik egy lebegő ablakban minden más alkalmazás felett. Húzza a lebegő ablakot bármelyik sarokba; csippentsen az átméretezéshez; érintse meg egyszer az alapvető lejátszás / szünet / ugrás vezérlők megjelenítéséhez; érintse meg a kis kibontás gombot a teljes Evervideo visszatéréséhez.

A PiP az Evervideo által lejátszott minden videoformátummal működik, beleértve a felhőről streamelt fájlokat és az RTSP streameket. A PiP a telefon zárolása közben is fut (az Auto-Lock beállításától függően).

## Kompakt lejátszó

A kompakt lejátszó egy állandó mini lejátszó, amely az alkalmazás minden képernyőjének tetején látható, miközben böngészi a könyvtárat, a fájlkezelőt vagy a beállításokat. Érintse meg a teljes képernyős lejátszóba való kibontáshoz; húzza le a visszazáráshoz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo videóbeállítások a kompakt lejátszóból a főképernyőn" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Az AirPlay-hez érintse meg az AirPlay gombot a lejátszón. Az Evervideo támogatja az AirPlay 2-t, így videót streamelhet Apple TV-re, HomePodra vagy bármely AirPlay 2-kompatibilis hangszóróra vagy okos TV-re. Több AirPlay-eszközzel rendelkező beállítás esetén egyszerre több fogadóra is irányíthatja a hangot.

## Google Chromecast

Google Cast felhasználóknak a Cast ikon megjelenik a lejátszón. Érintse meg az eszköz kiválasztásához és a leadás megkezdéséhez. Győződjön meg arról, hogy a telefon és a Cast-fogadó ugyanazon a Wi-Fi hálózaton van. Nem minden kodeket támogat a Chromecast hardver — egyes fájlokhoz transzkódolásra lehet szükség.

## RTSP élő streamek

Az Evervideo közvetlenül tud lejátszani RTSP forrásokat — IP kamerák, kaputelefon kamerák, IPTV streamek, közvetítési feedek és bármely más `rtsp://` URL. Adja hozzá a streamt RTSP kapcsolatként a Fájlok → Online linkek → Link hozzáadása menüpontban, majd érintse meg a megtekintés megkezdéséhez. Az RTSP streamek Kép-a-képben módban, a kompakt lejátszóban is működnek, és AirPlay 2-n és Chromecaston keresztül is leadhatók, mint egy normál videó.

## Hangsáv-kiválasztás

Több hangsávval rendelkező videókhoz (kommentár, alternatív szinkronizálás, rendező sávja) érintse meg a Több műveletek gombot a lejátszón, és válassza a Hangsáv lehetőséget — majd válassza ki a kívánt sávot. Ez elengedhetetlen idegen nyelvű filmekhez, BDMV / MKV fájlokhoz több szinkronizálással, valamint magyarázó sávokkal rendelkező oktatási tartalmakhoz.

## Videósáv-kiválasztás

Egyes videófájlok több videóstreamet tartalmaznak (multi-szögű Blu-ray-k, alternatív verziók). Válassza a Videósáv lehetőséget a Több műveletek menüből, hogy lejátszás közben váltson közöttük.

## Feliratok — Belső és Külső

Az Evervideo részletes irányítást biztosít a feliratok felett:

- **Felirat sáv** — válasszon a fájlba beágyazott sávok közül.
- **Külső feliratfájlok** — töltse be a `.srt`, `.vtt`, `.ass` vagy `.ssa` fájlokat az eszközéről, iCloud Drive-ról vagy bármely csatlakoztatott felhőszolgáltatásból.
- **Libass renderelés** — fejlett ASS / SSA stílusozás (betűtípusok, színek, pozíciók, karaoke effektek) helyesen renderelve a beágyazott libass köszönhetően.
- **Betűtípus-kiválasztás** — egyéni betűtípus az elsődleges feliratokhoz és külön a másodlagos feliratokhoz. Beépített betűtípusok és az eszközre telepített betűtípusok is elérhetők.

Mindezeket a Beállítások → Feliratok menüpontban konfigurálhatja lejátszás előtt, vagy a Több műveletek → Feliratok lehetőséget használhatja a lejátszóból menet közbeni váltáshoz.

## Hangegyenlítő

Az Evervideo teljes hangegyenlítőt tartalmaz a videó hangsávok headfones, hangszórós vagy hi-fi beállítás szerint való hangolásához. Érintse meg az egyenlítő ikont a hangerő nézeten (vagy a Hangegyenlítő műveletet a lejátszó Több műveletek menüjében), kapcsolja be az egyenlítőt a jobb felső sarokban lévő kapcsolóval, majd válasszon egy előbeállítást vagy húzza a sávcsúszkákat saját előbeállítás készítéséhez. Az egyéni előbeállítások exportálhatók és importálhatók, így megoszthatja azokat eszközök között vagy biztonsági másolatot készíthet róluk.

## Videóegyenlítő

A kép hangolásához az Evervideo egy dedikált videóegyenlítőt biztosít — állítsa be valós időben a fényerőt, kontrasztot, telítettséget és árnyalatot lejátszás közben. A hangegyenlítőhöz hasonlóan az egyéni videóelőbeállítások exportálhatók és importálhatók megosztáshoz vagy biztonsági mentéshez. Használja napos napon egy sötét jelenet megvilágításához, kimosott tartalom telítettségének fokozásához vagy hideg szín árnyalatának melegítéséhez.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo videóegyenlítő" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Videó méretezési mód

Válassza ki, hogyan töltse be a videó a képernyőt:

- **Illeszkedés** — megőrzi az eredeti képarányt; szükség esetén fekete sávok.
- **Kitöltés** — kitölti a teljes képernyőt, szükség esetén levágva a videót.
- **Nyújtás** — szükség esetén eltorzítva kinyújtja a videót a képernyő kitöltéséhez.
- **Eredeti** — megtartja az natív felbontást 1:1 arányban.

## Videó forgatás

Helytelen tájolással rögzített videókhoz válassza a **Több műveletek → Forgatás** lehetőséget, és válasszon **0°**, **90°**, **180°** vagy **270°** fokot a kép forgatásához anélkül, hogy elhagyná a lejátszót.

## Hardveres dekódolás (H.264 és HEVC)

A Beállítások → Lejátszó → Videó menüpontban engedélyezheti / letilthatja a Hardveres dekódolás H.264 és Hardveres dekódolás H.265 (HEVC) funkciókat egymástól függetlenül. A hardveres dekódolás gyorsabb, kevesebb akkumulátort fogyaszt és kevésbé melegszik — de ritka esetekben (sérült fájlok, egzotikus profilok) előfordulhat, hogy le kell tiltania a hardveres dekódolást és vissza kell térnie a szoftveres FFmpeg dekódoláshoz. Az Evervideo lehetővé teszi ezt fájlonként a lejátszó Több műveletek menüjéből.

## VR 360°-os nézőpont

Az Evervideo VR / 360°-os nézőpontot tartalmaz gömbös videofájlokhoz. Egy 360°-os videó lejátszásakor húzással körülnézhet, csippentéssel nagyíthat, és az Evervideo valós időben torzítja a renderelést.

## Lejátszási sebesség

Érintse meg a Sebesség vezérlőt a lejátszó eszköztáron a lejátszási sebesség megváltoztatásához — lassítsa le elemzéshez (0,25× vagy 0,5×) vagy gyorsítsa fel oktatóanyagokhoz és előadásokhoz (1,25×, 1,5×, 2× és egészen 3×-ig). Érintse meg a konfigurációs ikont a Sebesség képernyő jobb felső sarkában a pontos mód finomabb beállításaihoz való átváltáshoz. Sávonkénti hangmagasság-korrekció is elérhető.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo lejátszási sebesség a fő eszköztáron" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Lejátszási sor

A lejátszási sor megtekintéséhez érintse meg a sor gombot a lejátszón. A sorban lévő minden videónak van több művelete — érintse meg a három pontot azok megtekintéséhez. A videók sorban való átrendezéséhez használja az átrendezési jelzőt a cím közelében, és húzza az új pozícióba.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo lejátszási sor" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Elalvásidőzítő

Nyissa meg a Beállítások → Lejátszó → Elalvásidőzítő menüpontot, kapcsolja be, és válassza ki, mennyi ideig folytatódjon a lejátszás az automatikus leállítás előtt. Az Elalvásidőzítő gombot közvetlenül a fő lejátszóképernyőre is hozzáadhatja a Beállítások → Lejátszó → Személyre szabás → Fő képernyő műveletek menüpontban.

## Lejátszókönyvjelzők

Mentse el helyét hosszú videókban — előadások, video-hangoskönyvek, oktatóanyagok, egyórás YouTube letöltések — a Könyvjelző hozzáadása gomb megérintésével a Több műveletek menüből. A könyvjelzők megjelennek a videó Több műveletek → Könyvjelzők listájában, és munkamenetek között is megmaradnak.

## Több műveletek menü

Érintse meg a **Több műveletek „..."** gombot a lejátszón további funkciók eléréséhez.

- **Lejátszás folytatása** — a sor folytatása az utolsó pozícióból.
- **Keresés** — adott videó keresése a sorban.
- **Könyvjelzők** — könyvjelzők megtekintése és azokra való ugrás.
- **Sebesség** — lejátszási sebesség beállítása.
- **Legutóbbiak** — nemrégiben lejátszott videók.
- **Kedvencek** — kedvencként jelölt videók.
- **Hangegyenlítő** — a hangegyenlítő aktiválása.
- **Videóegyenlítő** — a videóegyenlítő aktiválása.
- **Hangsáv** — hangsugárzó kiválasztása.
- **Videósáv** — videóstream kiválasztása.
- **Feliratok** — elsődleges / másodlagos sáv, külső fájl, betűtípus.
- **Forgatás** — kép forgatása 0° / 90° / 180° / 270°.
- **Méretezési mód** — Illeszkedés / Kitöltés / Nyújtás / Eredeti.
- **Kép-a-képben** — PiP mód megnyitása.
- **AirPlay** / **Chromecast** — küldés eszközre.
- **Elalvásidőzítő** — időzítő beállítása a lejátszás leállítására.
- **Sor mentése lejátszási listaként** — az aktuális sor mentése új lejátszási listaként.
- **Sor törlése** — a sor törlése és a lejátszás leállítása.
- **Beállítások** — ugrás közvetlenül a lejátszóbeállításokhoz.
- **Súgó** — útmutató megnyitása.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo lejátszó Több műveletek képernyő" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Lejátszóbeállítások

A teljes lejátszóbeállítások fája a [Beállítások útmutatóban](/docs/guide/evervideo/evervideo-guide-settings/) van dokumentálva. A leggyakrabban használt szakaszok:

- **Általános** — Ismétlési mód, Keverési mód, Lejátszó állapot mentése, Lejátszási pozíció mentése, Ugrási időintervallumok.
- **Videó** — Hardveres dekódolás H.264 / HEVC, videóegyenlítő, méretezési mód, forgatás, megjelenítési mód, előnyben részesített FPS, előnyben részesített pixelformátum, VR nézőpont.
- **Hang** — Hangegyenlítő, mintavételezési frekvencia, csatornák, IO puffer időtartama, vegyes mód.
- **Feliratok** — Elsődleges / másodlagos sáv, külső fájl kiválasztása, betűtípus, másodlagos betűtípus.
- **Eszközök** (iOS) — AirPlay / Chromecast.
- **Személyre szabás** — Lejátszó elrendezési stílus (Minimális / Alsó / Antik / Klasszikus), fő képernyő műveletek, zárolt képernyő vezérlők.
- **Lejátszó gyorsítótár** — lemezgyorsítótár simább streameléshez.
- **Elalvásidőzítő** — automatikus leállítás.

## Akadálymentesítés

Az Evervideo teljesen akadálymentes a VoiceOver segítségével. Minden komponensnek jól megtervezett felirata és leírása van. A VoiceOver aktiválásakor az alkalmazás Szöveges módra vált, így csak az értelmes elemek jelennek meg — javítva a navigációs sebességet és érthetőséget. A Szöveges módot a Beállítások → Akadálymentesítés → Szöveges mód menüpontban is aktiválhatja.

### Csúszkák beállítása VoiceOver segítségével

1. **Válassza ki a csúszkát** — húzzon balra vagy jobbra, amíg a VoiceOver be nem jelenti.
2. **Állítsa be az értéket** — dupla érintéssel tartsa lenyomva a csúszkát, majd húzzon fel vagy le az érték gyors módosításához. A VoiceOver bejelenti az új értéket, ahogy halad.

Más komponensek a várt módon működnek, a rendszer által biztosított VoiceOver mintákat használva.
