---
title: "Zeneszámgyűjtemény exportálása M3U, CSV és TXT formátumba az Evermusic és Flacbox alkalmazásokban"
date: 2024-01-31
description: "Ismerje meg, hogyan exportálhatja legutóbbiakat, kedvenceket, lejátszási listákat és albumokat az Evermusic és Flacbox alkalmazásokból M3U, CSV vagy TXT formátumba. Tökéletes Last.fm scrobbláláshoz és lejátszáshoz más eszközökön."
keywords: ["evermusic exportálás", "flacbox exportálás", "exportálás m3u-ba", "lejátszási lista exportálása csv-be", "m3u txt csv lejátszási lista", "zene exportálás"]
tags: ["evermusic", "legutóbbiak", "kedvencek", "exportálás", "m3u", "lejátszási lista", "csv", "txt", "album"]
---

{{< author-byline >}}


**Röviden:** Az Evermusic és Flacbox lehetővé teszi bármely zeneszámgyűjtemény (legutóbbiak, kedvencek, lejátszási listák, albumok) exportálását CSV, TXT vagy M3U fájlokba. Használja ezeket az exportokat Last.fm scrobbláláshoz, könyvtára biztonsági mentéséhez, vagy lejátszási listái más eszközökön történő lejátszásához.

## Bevezetés

A legutóbbiak, kedvencek, albumok és lejátszási listák exportálása az alkalmazásból külső fájlba rendkívül hasznos lehet. Ezeket a fájlokat használhatja hallgatási előzményeinek frissítésére scrobbler szolgáltatásokon, például a [Last.fm](http://Last.fm) oldalon, vagy lejátszási listáinak külső eszközökön történő meghallgatására. Az Evermusic és Flacbox segítségével ez a folyamat egyszerű. Itt megmutatjuk, hogyan exportálhatja legutóbbiait CSV/TXT formátumba és lejátszási listáit M3U formátumba. Ez a funkció azonban az alkalmazáson belüli bármely zeneszámgyűjteményre elérhető.

## Formátum kiválasztása

A legutóbbiak exportálásához nyissa meg a 'Zenetár' részt, és válassza a 'Legutóbbiak' menüpontot.

![zenetár](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

A következő képernyőn érintse meg a jobb felső sarokban lévő 'Továbbiak' gombot, és válassza a 'Dallista exportálása' lehetőséget.

![legutóbbiak exportálása](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

A 'Fájlformátum kiválasztása' képernyőn több lehetőség áll rendelkezésre - CSV, TXT, M3U.

- CSV

Ez a Comma-Separated Values (vesszővel elválasztott értékek) rövidítése, tökéletes az adatok rendezett táblázatos formátumba rendezéséhez. A célfájlban olyan paramétereket talál, mint az Előadó neve, Album neve, Szám neve, Időbélyeg (a számok hallgatásának időpontja), Albumelőadó neve és Szám időtartama. Ezt a fájlt később felhasználhatja hallgatási előzményeinek frissítésére scrobbler szolgáltatásokon, például a [Last.fm](http://Last.fm) oldalon, az [itt](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/) leírtak szerint.

- TXT

Itt egy egyszerű szöveges fájlról beszélünk. Egyszerű és egyértelmű, olyan paraméterekkel, mint az Előadó neve, Album neve, Szám neve és Időtartam. Hasznos, ha csak szöveges formátumban szeretné a számok listáját.

- M3U

Ez a formátum lényegében a lejátszási listák létrehozásának szabványa. Kiváló, mert exportálhatja a dallistáját, és bármely eszközön élvezheti zenéit, még akkor is, ha nem rendelkezik az eredeti fájlokkal (ha az abszolút URL opciót választja a médiafájlok exportálásánál). A kimeneti fájlban olyan paramétereket talál, mint az Időtartam, Előadó neve, Szám neve és Médiafájl helye.

## CSV formátum

Most válasszuk ki a CSV-t, és nézzük meg, mit kapunk. Egyszerűen válassza a CSV-t, és nyomja meg az 'Exportálás' gombot.

![fájlformátum kiválasztása](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Az exportálás befejezése után egy értesítés jelenik meg két lehetőséggel. A 'Fájl megjelenítése' gombra koppintva megjelenik az eredményfájl a dokumentumok könyvtárában.

![exportálás befejezve](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Most elküldheti a fájlt, megnyithatja egy külső szövegszerkesztőben, vagy felhasználhatja hallgatási előrehaladásának frissítésére a [Last.fm](http://Last.fm) oldalon.

![exportálási mappa az eredményfájlokkal](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

A kimeneti CSV fájl a következő formátumban tartalmazza a mezőket:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Például:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![exportált csv fájl](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT formátum

A kimeneti TXT fájl a következő formátumban tartalmazza a mezőket:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Például:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![exportált txt fájl](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U formátum

Ezután végigvezetjük a lejátszási lista M3U formátumba történő exportálásán, amely a lejátszási lista fájlok de facto szabványa. A sikeres lejátszási lista exportálás fő előfeltétele, hogy a lejátszási lista összes fájljának ugyanazon a tárhelyen kell lennie, legyen az egy felhőszolgáltatás, mint a Google Drive, helyi fájlok, vagy az eszközén lévő fájlok. Az exportálási folyamat megkezdéséhez nyisson meg bármely lejátszási listát, és érintse meg a jobb felső sarokban lévő 'Továbbiak' gombot, majd válassza a 'Dallista exportálása' menüpontot.

![lejátszási lista képernyő](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

A következő képernyőn válassza az 'M3U' fájlformátumot, ahol két lehetőséget talál a 'Médiafájl hely típusa' beállításnál:

![exportálási fájlformátum kiválasztása képernyő](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Ha a 'Relatív útvonal' lehetőséget választja, a lejátszási lista a médiafájlok helyeit a lejátszási lista fájlhoz viszonyítva írja le. Például:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Ebben az esetben kerülje az M3U fájl helyének megváltoztatását az exportálás befejezése után, mert ez érvényteleníti a médiafájlok útvonalait. A lejátszási lista lejátszásának megkezdéséhez egyszerűen érintse meg az exportált lejátszási lista fájlt, és az alkalmazás automatikusan megtalálja a médiafájlokat a tárhelyén, és elindítja a lejátszást. Sőt, exportálhatja lejátszási listáit a tárhelyre, majd újra importálhatja őket az új eszközére.

2. Ha az 'Abszolút URL' lehetőséget választja, az alkalmazás közvetlen URL-eket generál a médiafájljaihoz. Ez lehetővé teszi a lejátszási lista lejátszását bármely eszközön/alkalmazásban anélkül, hogy az összes médiafájlnak a lejátszási lista fájllal azonos tárhelyen kellene lennie. Ez az opció csak közvetlen fájl URL-ek generálására képes felhőtárhely-szolgáltatásoknál támogatott. Azonban vegye figyelembe, hogy egyes esetekben a generált URL-ek korlátozott élettartamúak lehetnek, és bizonyos idő után lejárhatnak. Íme a támogatott felhőszolgáltatások listája: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (ha vendég módban van)  

A kimeneti médiafájl URL valami ilyesmi lesz:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Miután kiválasztotta a 'Médiafájl hely típusa' beállítást, érintse meg az 'Exportálás' gombot. Az alkalmazás felkéri, hogy válasszon célmappát az M3U fájl exportálásához. Érintse meg a 'Kész' gombot a kiválasztás megerősítéséhez.

![mappa kiválasztása](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Az alkalmazás létrehozza az M3U fájlt, és feltölti/áthelyezi a célmappába.

![m3u fájl feltöltése](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Az exportálás befejezése után egy rendszerértesítés jelenik meg a 'Fájl megjelenítése' lehetőséggel.

![exportálás befejezve értesítés](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Erre koppintva megjelenik az exportált fájl az alkalmazásban.

![exportált m3u fájl a fájllistában](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Ha az előző lépésben a 'Relatív útvonal' lehetőséget választotta 'Médiafájl hely típusaként', a kimeneti fájl a következő formátumban lesz:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![m3u példa relatív útvonalakkal](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Az 'Abszolút URL' opciónál az alkalmazás a következő formátumban generálja az M3U fájlt:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![m3u példa abszolút fájl URL-ekkel](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Ezt a fájlt bármely M3U lejátszási listákat támogató eszközön/alkalmazásban megnyithatja.

![m3u lejátszási lista megnyitva külső alkalmazásban](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Záró gondolatok

A zeneszámok exportálása az Evermusic és Flacbox alkalmazásokból teljes kontrollt biztosít zenei adatai felett. Akár hallgatási előzményeit menti, akár a Last.fm-re scrobblál, akár külső eszközökön élvezi lejátszási listáit, ezek az exportálási lehetőségek: M3U, CSV és TXT - hatékony eszközök, amelyek rugalmasságra és kompatibilitásra lettek tervezve. Használja ki ezeket a funkciókat, hogy javítsa zenegyűjteménye rendszerezését, megosztását és újrafelfedezését a különböző platformokon.

## Gyakran ismételt kérdések

{{% details title="Melyik exportálási formátumot használjam a Last.fm scrobbláláshoz?" closed="true" %}}
Használja a CSV-t. Tartalmazza az időbélyegeket és a scrobblálási eszközök, például a Last.fm-Scrubbler-WPF által igényelt teljes metaadatokat.
{{% /details %}}

{{% details title="Exportálhatok bármilyen zeneszámgyűjteményt, nem csak lejátszási listákat?" closed="true" %}}
Igen. Exportálhatja a legutóbbiakat, kedvenceket, albumokat, lejátszási listákat és bármely más zeneszámgyűjteményt az alkalmazásban ugyanezekkel a lépésekkel.
{{% /details %}}

{{% details title="Működik az M3U lejátszási listám más eszközökön?" closed="true" %}}
Ha az exportálás során az Abszolút URL opciót választja, az M3U fájl bármely M3U lejátszási listákat támogató eszközön lejátszható. Vegye figyelembe, hogy egyes felhő URL-ek idővel lejárhatnak.
{{% /details %}}

{{% details title="Ingyenes az exportálási funkció?" closed="true" %}}
Igen. A zeneszámgyűjtemények exportálása M3U, CSV és TXT formátumba az Evermusic és Flacbox ingyenes és prémium verziójában egyaránt elérhető.
{{% /details %}}

{{% details title="Mely felhőszolgáltatások támogatják az Abszolút URL exportálást?" closed="true" %}}
Az Abszolút URL exportálás az iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive és WebDAV (vendég mód) szolgáltatásoknál támogatott.
{{% /details %}}
