---
date: '2025-06-12T17:00:00+00:00'
title: 'Gyakran ismételt kérdések'
description: 'Találjon válaszokat az Evermusic, Flacbox, Evervideo és Evertag alkalmazásokkal kapcsolatos általános kérdésekre. Fedezze fel a cloud streaming, fájlkezelés, lejátszási lehetőségek, metaadat-szerkesztés és más funkciók részleteit.'
keywords: [
  "Evermusic GYIK", "Flacbox támogatás", "Evervideo segítség", "Evertag kérdések",
  "hogyan kell használni az Evermusicot", "cloud zenelejátszó hibaelhárítás", "offline lejátszás útmutató",
  "hangtag-szerkesztő támogatás", "videostreaming problémák", "fájlátvitel útmutató"
]
tags: [
  "GYIK", "segítség", "támogatás", "evermusic", "flacbox", "evervideo", "evertag",
  "felhő beállítás", "lejátszási problémák", "fájlkezelés", "metaadat-szerkesztés",
  "hibaelhárítás", "offline mód", "zenelejátszó", "videolejátszó"
]
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## Ismerje meg alkalmazásainkat

Válaszokat vagy segítséget keres egyik alkalmazásunk használatához? Jó helyen jár.

GYIK-oldalaink segítenek Önnek cloud tárhely csatlakoztatásában, zene- és videofájlok kezelésében, offline lejátszás beállításában, hangszínszabályozó beállítások megadásában, metaadatok javításában és sok másban.

Tekintse meg az alkalmazásához tartozó GYIK-et alább a kezdéshez, vagy böngéssze át a felhasználóktól kapott e-mailekből összegyűjtött általános kérdéseket és válaszokat.

## Válassza ki alkalmazását

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="Játsszon le 360°-os videókat, streamelje az iCloudból, nézze feliratokkal, alkalmazzon video hangszínszabályozót, rendezze a tartalmat lejátszási listákkal és töltse le a videókat offline megtekintéshez."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="Felhő-zenelejátszó offline móddal, hang-hangszínszabályozóval, crossfade-del, zökkenőmentes lejátszással, lejátszási lista kezeléssel, teljes zenei könyvtárral és beépített fájlkezelővel."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="Nagy felbontású audiolejátszó iPhone-ra és Macre. Hallgasson veszteségmentes formátumokat, például FLAC, ALAC, APE és DSD. Finomhangolja a kimenetet speciális hangbeállításokkal."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="Intelligens zenecímke-szerkesztő kötegelt szerkesztéssel. Javítsa a hiányzó metaadatokat, album borítókat és egyebeket. Szerkessze az ID3, FLAC, APE címkéket — több mint 120 mező támogatott." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## Általános problémák és válaszok

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="Miért nem tudok bejelentkezni a pCloudba régebbi iOS verzión (15.8.4)?" closed="true" %}}
A pCloud webes bejelentkezési oldala előfordulhat, hogy nem jelenik meg helyesen régebbi iOS verziókon, például a 15.8.4-en, ami megakadályozza az e-mail és jelszó megadását a felhőkapcsolat képernyőjén.<br><br>

Megkerülő megoldásként a **WebDAV** protokollt használhatja, amelyet a pCloud támogat, és megbízhatóan működik minden iOS verzión.

**WebDAV beállítás:**<br>
- **US szerverek:** `https://webdav.pcloud.com`  
- **Európai szerverek:** `https://ewebdav.pcloud.com`  
- **Felhasználónév:** pCloud e-mail cím  
- **Jelszó:** pCloud fiók jelszava  

Nyissa meg az alkalmazást → Kapcsolatok → Csatlakozás felhőtárhelyhez → Válassza a **WebDAV** lehetőséget → Adja meg hitelesítő adatait és a szerver URL-jét.

Ez a módszer lehetővé teszi, hogy csatlakozzon a pCloud tárhelyéhez és hozzáférjen fájljaihoz gond nélkül régebbi eszközökön is.
{{% /details %}}

{{% details title="Hogyan játszhatok zenét AirPlay-en Mac-en (macOS)?" closed="true" %}}
Az alkalmazás macOS verziója nem tartalmaz beépített AirPlay, Chromecast vagy Bluetooth csatlakozási gombokat, mint az iOS verzió.<br><br>

Az **AirPlay** MacBook Pro-n való használatához kövesse ezeket a lépéseket:

1. Lépjen a képernyő **jobb felső sarkába**, és nyissa meg a **Vezérlőközpontot** (az óra közelében).  
2. Kattintson a **Hang/Hangerő** ikonra.  
3. A következő képernyőn kattintson az **AirPlay** lehetőségre az összes elérhető AirPlay eszköz listájának megtekintéséhez.  
4. Válassza ki a kívánt eszközt a zene streamelésének megkezdéséhez.  

Ez az összes rendszerhangot (beleértve az Evermusic vagy Flacbox hangját) a kiválasztott AirPlay eszközre irányítja.
{{% /details %}}

{{% details title="Miért nincs aktiválva a Premium vásárlásom Mac-en, ha iPhone-on vettem?" closed="true" %}}
Az élethosszig tartó vásárlások és előfizetések iOS és Mac között az **iCloud** segítségével szinkronizálódnak.<br><br>

A Premium Mac-en való aktiválásához:<br>
- Győződjön meg arról, hogy mindkét eszközre telepítve van az alkalmazás legújabb verziója<br>
- Engedélyezze az **iCloud**-ot mindkét eszközön<br>
- Indítsa el az alkalmazást iOS eszközén, és várjon 1 percet, amíg a vásárlási adatok feltöltődnek<br>
- Mac-en telepítse az alkalmazást az App Store-ból **ugyanazzal az Apple ID-vel**<br>
- Indítsa el az alkalmazást, és várjon néhány másodpercet az adatok szinkronizálásáig<br>
- Alternatívaként érintse meg a **Vásárlások visszaállítása** lehetőséget mindkét eszköz alkalmazásbeállításaiban<br><br>

Ezután a Premium funkciók automatikusan aktiválódnak Mac-en.
{{% /details %}}

{{% details title="Hogyan szinkronizálhatom automatikusan a lejátszási listákat az eszközök között?" closed="true" %}}
Jelenleg **nincs automatikus szinkronizálás** lejátszási listákhoz.<br><br>

Az alábbi lehetőségek egyikét használhatja:<br>
- **Biztonsági mentés és visszaállítás** az Alkalmazás beállításaiból [Hogyan vigyük át a zenei könyvtárat az eszközök között az Evermusicban: Lépésről lépésre útmutató](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **Lejátszási lista exportálása M3U-ba**, majd importálás másik eszközre:<br>
  - [Lejátszási listák exportálása](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [Lejátszási listák importálása](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **Lejátszási lista vagy albumok archiválása** és átvitel ZIP-en keresztül:<br>
  - [Lejátszási lista archiválási útmutató](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="Biztonságos az alkalmazásait használni? Ki lehet kapcsolni az analitikát?" closed="true" %}}
Igen, az Ön adatvédelme a legfontosabb számunkra.<br><br>

- Minden adat — zenefájlok, beállítások, felhő bejelentkezések — az eszközén marad<br>
- A bejelentkezési adatok biztonságosan tárolódnak az **iOS Keychain**-ben<br>
- Csak névtelen összeomlási és használati jelentéseket gyűjtünk<br>
- Letilthatja ezt az **Alkalmazás beállításai → Analitika** menüpontban<br><br>

További információ:<br>
- [Adatvédelmi irányelvek](/legal/privacy-policy/)<br>
- [Apple Keychain biztonság](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

Személyre szabott hirdetések esetén a Google Mobile Ads megköveteli az adatkezelési hozzájárulás megjelenítését.<br>
A Premium felhasználók nem látnak hirdetéseket, és a hirdetési SDK teljesen le van tiltva.
{{% /details %}}

{{% details title="Támogatják az alkalmazásai a Családi megosztást?" closed="true" %}}
Igen, a Családi megosztás támogatott.<br><br>

Az alkalmazáson belüli vásárlások megosztásához:<br>
- Győződjön meg arról, hogy a vásárlás be van állítva a családi csoportjával való megosztásra<br>
- A családtag eszközén lépjen a **Beállítások > Vásárlások > Vásárlások visszaállítása** menüpontba<br>
- Ez kéri az Apple szervereiről a vásárlási adatokat, és aktiválja azokat az eszközén
{{% /details %}}

{{% details title="Hogyan gyorsíthatom fel a metaadat- és felhőszinkronizálást?" closed="true" %}}
A szinkronizálás sebességének javításához engedélyezze a háttérfeladatokat:<br><br>

- **Beállítások → Zenei könyvtár → Metaadat olvasás → Metaadat olvasás háttérben**<br>
- **Beállítások → Zenei könyvtár → Online zene szinkronizálása → Háttér szinkronizálás**<br><br>

Ezenkívül macOS-en növelje a metaadat olvasási sebességet a **Beállítások → Zenei könyvtár** menüpontban.<br>
Ha a lejátszó aktív (hang lejátszódik), az iOS nem felfüggeszti az alkalmazást, lehetővé téve a folyamatos szinkronizálást.
{{% /details %}}

{{% details title="Hogyan mondhatom le az előfizetésemet?" closed="true" %}}
Az előfizetését az Apple hivatalos utasításai alapján mondhatja le:<br>
👉 [Hogyan lehet lemondani egy előfizetést](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="Hogyan csatlakozhatom és streamelhetem a hangot a WD MyCloud EX2 Ultra-ból?" closed="true" %}}

Amikor az alkalmazásban kapcsolatot ad hozzá a **Kapcsolatok > Csatlakozás felhőtárhelyhez > My Cloud Home** menüponton keresztül, ez hivatalosan a **WD MyCloud Home** eszközök támogatására lett tervezve.<br>
A WD MyCloud EX2 Ultra korlátozott hozzáférést alkalmaz az alkalmazások számára.<br><br>

Ha azonban sikeresen csatlakozott egy **WD MyCloud EX2 Ultra**, **WD MyCloud Mirror** vagy más **WD MyCloud** tárolómodellhez, akkor is használhatja a következő megkerülő megoldással:<br><br>

1. Nyissa meg a **Kapcsolatok → Csatlakozás felhőtárhelyhez → My Cloud Home** menüpontot<br>
2. Hozzon létre egy mappát a beépített fájlkezelővel<br>
3. Töltsön fel zenefájlokat ebbe a mappába<br>
4. Ezek egy "homokozóban" tárolódnak, amelyhez csak az alkalmazás fér hozzá<br>
5. Most már közvetlenül streamelheti vagy letöltheti ezeket<br><br>

⚠️ Csak az alkalmazáson keresztül létrehozott mappák lesznek elérhetők a NAS-ból.
{{% /details %}}

{{% details title="Hogyan csatlakozhatom a Koofr.eu-hoz?" closed="true" %}}
A Koofrt a **WebDAV** segítségével csatlakoztathatja.<br><br>

- Koofr WebDAV beállítási útmutató: [koofr.eu blog](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Evermusic/Flacbox WebDAV útmutató: [Hogyan csatlakoztassunk NAS tárolót WebDAV-on keresztül és hallgassunk zenét iPhone-on vagy Mac-en](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="Mik az alkalmazás URL sémái?" closed="true" %}}
Az alábbi sémák támogatottak:<br><br>

**Evermusic**<br>
- iOS (kék ikon): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (piros ikon): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="A zene leáll, amikor az alkalmazás a háttérben van — hogyan javítható?" closed="true" %}}
Ha az alkalmazás összeomlik vagy szünetel a háttérben:<br>
- Lépjen a **Beállítások > Zenei könyvtár > Online zene szinkronizálása > Háttér szinkronizálás → Letiltás** menüpontba<br>
- **Beállítások > Zenei könyvtár > Metaadat olvasás > Metaadat olvasás háttérben → Letiltás**<br>
- **Beállítások > Fájlkezelő > Háttér átvitelek → Letiltás**
{{% /details %}}

{{% details title="A zökkenőmentes lejátszás nem működik — hogyan javítható?" closed="true" %}}
A zökkenőmentes lejátszás az iOS verziótól és a hangmotortól függ.<br>
Próbálja meg átváltani a hangmotort:<br>
- Lépjen a **Beállítások → Audiolejátszó → Általános → Audioprocesszor** menüpontba<br>
- Válassza a **Core Audio** lehetőséget a jobb zökkenőmentes támogatáshoz
{{% /details %}}

{{% details title="Miért csak 100 elemet mutat az alkalmazás egy listában?" closed="true" %}}
Az alkalmazás lapozást alkalmaz a teljesítmény érdekében.<br>
A letiltáshoz:<br>
- Lépjen a **Beállítások → Személyre szabás → Tartalombetöltési korlát → Inaktív** menüpontba<br>
Most minden elem egyszerre töltődik be.
{{% /details %}}

{{% details title="Miért vannak furcsa karakterek a metaadatokban?" closed="true" %}}
Próbálja engedélyezni a metaadat normalizálást:<br>
- **Beállítások → Zenei könyvtár → Metaadat olvasás → Metaadat kódolás normalizálása**
{{% /details %}}

{{% details title="Miért nem tudja az alkalmazás olvasni a különleges karaktereket tartalmazó mappaneveket?" closed="true" %}}
Ez egy ismert probléma az **SMB2 protokollal**.<br><br>

Próbálja az alábbi megoldásokat:<br>
- Engedélyezze az **SMB1**-et a szerveren és az alkalmazás beállításaiban<br>
- Használja a **rendszer fájlválasztót**:<br>
  - Lépjen a **Helyi fájlok > Fájlok ezen az eszközön > Fájlok megnyitása...** menüpontba<br>
  - Válasszon mappákat/fájlokat az Apple natív menüjét használva<br><br>

Alternatívaként csatlakozzon **WebDAV** vagy **DLNA** segítségével, ha a NAS támogatja ezeket.
{{% /details %}}

{{% details title="Hogyan tölthetek fel és kezelhetek zenét az iCloudban?" closed="true" %}}
– **Hogyan tölthetek fel zenét az iCloudba?**  <br>
Lépjen a [https://www.icloud.com](https://www.icloud.com) oldalra böngészőjében, hozzon létre egy mappát, és töltse fel zenefájljait közvetlenül Mac-ről vagy PC-ről.<br>

– **Hogyan kezelhetem az iCloud tárhelyet?**  <br>
Két lehetősége van:  <br>
1. Használja a [https://www.icloud.com](https://www.icloud.com) oldalt böngészőjében a fájlok rendezéséhez, feltöltéséhez vagy törléséhez.<br>  
2. Az alkalmazásban, miután csatlakozott az iCloudhoz a **Kapcsolatok → Csatlakozás felhőtárhelyhez → iCloud Drive** menüponton keresztül, használja a beépített fájlkezelőt fájlok feltöltéséhez, letöltéséhez, mappák átnevezéséhez vagy fájlok törléséhez közvetlenül az iCloud tárhelyén — az eszközre való mentés nélkül.<br>

⚠️ Legyen óvatos a fájlok törlésénél. Az alkalmazás véglegesen törli azokat (nem kerülnek a kukába és nem állíthatók vissza).<br>

Tudjon meg többet itt: [Hogyan streameljünk zenét az iCloud Drive-ból iPhone-on vagy Mac-en](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="Hogyan vihetem át 10 GB-os zenei könyvtáramat Windows 11-ről iPhone-ra offline lejátszáshoz?" closed="true" %}}

Számos megbízható lehetőség áll rendelkezésére a zenei könyvtár átviteléhez Windows 11 PC-ről iPhone-ra és offline használathoz az alkalmazásban. Válassza az Önnek legjobban megfelelő módszert:

1. **Kábeles csatlakozás használata (nagy könyvtárakhoz ajánlott)**  <br>
   Használja az **Apple Devices** alkalmazást Windows 11-en a fájlok közvetlen átviteléhez iPhone-ra USB-n keresztül.  
   Kövesse az Apple útmutatóját itt:  
   https://support.apple.com/en-ph/120402 <br>

2. **Vezeték nélkül Wi-Fi Drive segítségével**  <br>
   Engedélyezze a **WiFi Drive** funkciót az alkalmazásban, és töltse fel zenéjét böngészőn keresztül a számítógépéről.  
   Lépésről lépésre útmutató itt:  
   [Hogyan vigyünk át zenefájlokat számítógépről iPhone-ra iTunes nélkül WiFi-Drive segítségével](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **Vezeték nélkül DLNA szerver használatával**  <br>
   Kapcsolja be a DLNA médiaszert Windows számítógépén, és streamelje vagy vigye át a könyvtárát közvetlenül az alkalmazásba.  
   Útmutató:  
   [Hogyan engedélyezzük a DLNA médiaszervert Windows 10-en és játsszunk zenét iPhone-on](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **Vezeték nélkül SMB fájlmegosztás használatával**  <br>
   Engedélyezze az **SMB fájlmegosztást** PC-jén, és csatlakozzon hozzá az alkalmazásban a fájlok mappánkénti böngészéséhez, letöltéséhez vagy átviteléhez.  
   Útmutató:  
   [Fájlok átvitele számítógépről iPhone-ra SMB protokoll segítségével](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ Nagy könyvtárak (10 GB+) átvitelekor a kábeles USB átvitel általában a leggyorsabb és legstabilabb lehetőség.

{{% /details %}}

</div>
