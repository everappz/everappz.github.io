---
title: "Hogyan játssza le zenéjét Mac / PC / Linux / NAS eszközről iPhone-on a Kodi DLNA szerver segítségével"
date: 2025-07-25
description: "Zenét streamelhet számítógépéről vagy NAS-ról iPhone-jára Wi-Fi-n keresztül a Kodi DLNA és az Evermusic alkalmazás segítségével."
keywords: ["kodi dlna szerver", "zene streamelés iphone-ra", "zene lejátszás nas-ról", "evermusic dlna", "mac-ről iphone-ra zene", "windows-ról iphone-ra zene", "kodi dlna iphone", "dlna audio streaming"]
tags: ["dlna", "kodi", "evermusic", "iphone", "zene streamelés", "mac", "nas", "linux", "helyi hálózat"]
readingTime: 5
---

{{< author-byline >}}


**Összefoglaló:** Telepítse a Kodi-t Mac-re, PC-re, Linux-ra vagy NAS-ra, engedélyezze a DLNA/UPnP szervert, és streamelje teljes zenekönyvtárát iPhone-ra vagy iPad-re az ingyenes Evermusic vagy Flacbox alkalmazással Wi-Fi-n keresztül. Előfizetés nem szükséges.

## Bevezetés

Ha van **Mac-je, Windows PC-je, Linux gépe vagy NAS eszköze**, könnyen átalakíthatja **személyes zenei szerverré** otthon a [Kodi](https://kodi.tv/) segítségével, amely egy ingyenes és nyílt forráskódú médiaplatform. A Kodi beépített **DLNA/UPnP szerverével** teljes zenekönyvtárát streamelheti bármely DLNA-kompatibilis kliensre — beleértve iPhone-ját vagy iPad-jét.

Ebben az útmutatóban lépésről lépésre megmutatjuk, hogyan:

- Telepítse a Kodi-t Mac-re vagy PC-re  
- Állítsa be a zenemappákat megosztáshoz  
- Engedélyezze a DLNA zenei szervert  
- Érje el a zenét az **Evermusic** vagy **Flacbox** iOS alkalmazással

Ez a beállítás 100%-ban ingyenes — nincs előfizetés, csak a saját zenéje, streamed a Wi-Fi hálózatán. Akár nagy MP3 gyűjteményét próbálja rendezni, FLAC-ot hallgatni Wi-Fi-n, vagy egyszerűen élvezni helyi zenéjét iTunes szinkronizálás nélkül, ez a beállítás tökéletes Önnek.

## Kodi letöltése és telepítése Mac / PC / Linux / NAS eszközre

Először látogasson el a Kodi hivatalos weboldalára:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi főoldal" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Kattintson a **Letöltések** gombra, és görgessen le a számítógépéhez tartozó verzió megtalálásához. Válassza ki az operációs rendszerét. Ebben a példában **macOS**-t használunk.

{{< cards cols="1">}}
{{< card subtitle="Kodi letöltési oldal" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Kattintson az **Intel (x86/64)** opcióra, ha Intel Mac-je van, vagy az **Apple Silicon** opcióra M1, M2, M3 Mac esetén a letöltés elindításához.

{{< cards cols="1">}}
{{< card subtitle="macOS telepítő kiválasztása" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Kérjük, várjon egy pillanatot, amíg a telepítő letöltődik.

{{< cards cols="1">}}
{{< card subtitle="Kodi letöltve" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Letöltés után keresse meg a `.dmg` fájlt a **Letöltések** mappában.

{{< cards cols="1">}}
{{< card subtitle="Kodi telepítése" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Kattintson duplán a letöltött fájlra a telepítő elindításához. Húzza a Kodi-t az **Alkalmazások** mappába a telepítéshez.

{{< cards cols="1">}}
{{< card title="" subtitle="Telepítse a Kodi-t az Alkalmazásokba húzással" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Indítsa el a Kodi-t. Előfordulhat, hogy engedélyeznie kell a **Rendszerbeállítások → Biztonság és adatvédelem → Megnyitás mindenképpen** menüpontban.

{{< cards cols="1">}}
{{< card subtitle="Kodi főképernyő" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Zene hozzáadása a Kodi könyvtárhoz

Kattintson a **fogaskerék ikonra** (Beállítások) a kezdőképernyőn.

{{< cards cols="1">}}
{{< card subtitle="Kodi beállítások" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Navigáljon a **Média beállítások → Könyvtár** menüponthoz. Engedélyezze a **Könyvtár frissítése indításkor** opciót a videó- és zenekönyvtár automatikus indexeléséhez.

{{< cards cols="1">}}
{{< card subtitle="Könyvtár beállítások" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Majd lépjen a **Zene** szekcióba és kattintson a **Zene hozzáadása** gombra.

{{< cards cols="1">}}
{{< card subtitle="Zenemappa hozzáadása" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Böngésszen és válassza ki a mappát, ahol a zenéje van tárolva.

{{< cards cols="1">}}
{{< card subtitle="Zeneforrás kiválasztása" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Adja hozzá a zeneforrást a Kodi-hoz.

{{< cards cols="1">}}
{{< card subtitle="Zeneforrás hozzáadása" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Erősítse meg, és hagyja, hogy a Kodi átvizsgálja a zenekönyvtárát.

{{< cards cols="1">}}
{{< card subtitle="Zeneforrások megerősítése" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Várjon egy pillanatot, amíg a könyvtár vizsgálata és felépítése befejeződik.

{{< cards cols="1">}}
{{< card subtitle="Zenekönyvtár vizsgálata" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Kodi DLNA szerver engedélyezése

Lépjen a **Beállítások → Szolgáltatások → UPnP/DLNA** menüpontra.

Engedélyezze az opciót: **Könyvtáraim megosztása**.

A Kodi most DLNA szerverként működik a helyi Wi-Fi hálózatán.

{{< cards cols="1">}}
{{< card subtitle="DLNA engedélyezése a Kodi-ban" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Kodi könyvtár megnyitása

Kattintson jobb gombbal a beállítások ablak bezárásához és a Kodi fő könyvtár megnyitásához.

{{< cards cols="1">}}
{{< card title="" subtitle="Jobb klikk a Kodi könyvtár eléréséhez" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Zene streaming alkalmazás letöltése iOS-re

Szerezzen be egy ingyenes iOS DLNA kliens alkalmazást, amely lehetővé teszi a zene streamelését felhőtárhely-szolgáltatásokból és DLNA szerverekből.

- Használja az **Evermusic**-ot, ha gyűjteménye főleg MP3 és más szabványos hangformátumokból áll.
- Válassza a **Flacbox**-ot, ha hi-res zenekönyvtára van FLAC, ALAC vagy DSD formátumokban.

Mindkét alkalmazás elérhető **iOS**-re és **macOS**-re, és ingyenesen használható.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic letöltése" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox letöltése" icon="download" tag="Free" >}}
{{< /cards >}}

## DLNA forrás hozzáadása

Az iOS alkalmazás letöltése után nyissa meg az **Összes Kapcsolatok** szekciót.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic alkalmazás fő oldalsáv" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Görgessen le és érintse meg a **Helyi hálózat - Elérhető eszközök** opciót a DLNA szerverek felfedezéséhez. Ebben a szekcióban látni fogja az összes elérhető eszközt a helyi hálózatán. A **Kodi DLNA szervere** itt jelenik meg. Érintse meg a Kodi szervert a csatlakozáshoz.

{{< cards cols="1">}}
{{< card title="" subtitle="Elérhető DLNA eszközök az Evermusic-ban" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Az Evermusic megjeleníti a Kodi-n keresztül megosztott könyvtármappákat.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi zenekönyvtár az Evermusic-ban" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navigáljon a **Dalok** mappához a DLNA szerveren elérhető összes hangfájl megtekintéséhez.

{{< cards cols="1">}}
{{< card title="" subtitle="Dalok a távoli mappából" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Érintsen meg bármely hangfájlt az azonnali streamelés elindításához.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3 fájl lejátszása az Evermusic-ban" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Térjen vissza a **Kapcsolatok** szekcióba. A hozzáadott DLNA szerver most itt jelenik meg. Érintse meg az ikonját a bármikori újracsatlakozáshoz. Ugyanerről a képernyőről más felhőszolgáltatásokat is csatlakoztathat ugyanezekkel a lépésekkel.

Itt engedélyezheti a **Last.fm scrobbling**-ot is. A lejátszási statisztikák a Last.fm fiókjába mentődnek, személyre szabott zenei ajánlásokat biztosítva később.

{{< cards cols="1">}}
{{< card title="" subtitle="Kapcsolatok az Evermusic-ban" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Zenekönyvtár építése

Az **Evermusic** és a **Flacbox** egyaránt lehetővé teszi a zene hozzáadását a könyvtárához és rendezését **metaadat-címkék** szerint, mint előadók, albumok, műfajok és zeneszerzők.

Kezdéshez nyissa meg a **Zenekönyvtár** szekciót. Görgessen le az **Eszközök és beállítások** részhez és érintse meg a **Zene hozzáadása** gombot.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic zenekönyvtár" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Válassza ki a zeneforrást — ebben az esetben válassza a **Kapcsolatok** opciót.

{{< cards cols="1">}}
{{< card title="" subtitle="Új zene hozzáadása az Evermusic-ban" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Keresse meg a **Kodi DLNA szervert** a Kapcsolatokban és érintse meg a mappák és fájlok megtekintéséhez.

{{< cards cols="1">}}
{{< card title="" subtitle="DLNA szerver kiválasztása zene importáláshoz" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Válassza ki a hozzáadni kívánt mappákat vagy fájlokat és érintse meg a **Kész** gombot.

{{< cards cols="1">}}
{{< card title="" subtitle="Zenemappa kiválasztása hozzáadáshoz" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Az alkalmazás átvizsgálja a kiválasztott fájlokat és metaadatok segítségével rendezi azokat szekciókba, mint Előadók, Albumok, Műfajok és Zeneszerzők.

{{< cards cols="1">}}
{{< card title="" subtitle="Zenekönyvtár kategóriákkal" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Lejátszási listák létrehozása

Saját lejátszási listákat is létrehozhat.

Először nyissa meg a **Lejátszási listák** fület.

{{< cards cols="1">}}
{{< card title="" subtitle="Lejátszási listák fül az Evermusic-ban" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Érintse meg a **plusz (+)** gombot és válassza az **Új lejátszási lista** opciót.

{{< cards cols="1">}}
{{< card title="" subtitle="Új lejátszási lista létrehozása" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Adjon nevet a lejátszási listájának és érintse meg a **Mentés** gombot.

{{< cards cols="1">}}
{{< card title="" subtitle="Lejátszási lista nevének megadása" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Válasszon forrást dalok hozzáadásához — itt a **Könyvtárat** választjuk.

{{< cards cols="1">}}
{{< card title="" subtitle="Dalok hozzáadása az új lejátszási listához" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Válassza ki a kívánt dalokat és érintse meg a **Kész** gombot a hozzáadáshoz.

{{< cards cols="1">}}
{{< card title="" subtitle="Zene hozzáadása a könyvtárból a lejátszási listához" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

A kiválasztott számok most megjelennek a létrehozott lejátszási listában.

{{< cards cols="1">}}
{{< card title="" subtitle="Létrehozott lejátszási lista a listában" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Alapértelmezés szerint a dalok streamelésre elérhetők. Offline hallgatáshoz engedélyezze az **Offline módot** — az alkalmazás letölti az összes lejátszási lista számot.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline mód engedélyezve a lejátszási listához" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Érintse meg a **További műveletek** gombot további lehetőségek felfedezéséhez. Lehetőségei:

- Lejátszási lista archiválása  
- Albumborító módosítása  
- Számok átrendezése  
- És más hasznos funkciók

{{< cards cols="1">}}
{{< card title="" subtitle="További lejátszási lista műveletek" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Következtetés

Az **Evermusic** és **Flacbox** segítségével iPhone-ja, iPad-je vagy Mac-je egyszerűen erős DLNA zenelejátszóvá alakítható. Akár felhőben, NAS-on vagy otthoni médiaszerverén, mint a **Kodi**, tárolja zenéjét, ezek az alkalmazások lehetővé teszik a streamelést, rendezést és élvezetet korlátozások nélkül.

- Streameljen MP3-at vagy hi-res FLAC-ot közvetlenül a **Kodi DLNA szerverről**  
- Építsen személyes zenekönyvtárat metaadatok szerint csoportosítva (albumok, műfajok, zeneszerzők)  
- Hozzon létre és kezeljen **egyéni lejátszási listákat**  
- Engedélyezze az **offline módot** útközbeni hallgatáshoz  
- Csatlakozzon **több felhőszolgáltatáshoz** és **helyi hálózati eszközhöz**  
- Kövesse hallgatási szokásait a **Last.fm integrációval**

Akár audiofil, akár alkalmi hallgató, az Evermusic és Flacbox mindent kínál, amire szüksége van a zökkenőmentes zene streameléshez és rendezéshez.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic letöltése" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox letöltése" icon="download" tag="Free" >}}
{{< /cards >}}

Kezdje el személyes zenei élményének építését még ma.

## GYIK

{{% details title="Ingyenes a Kodi DLNA szerverként?" closed="true" %}}
Igen. A Kodi teljesen ingyenes és nyílt forráskódú. Fut macOS-en, Windows-on, Linux-on és sok NAS eszközön.
{{% /details %}}

{{% details title="Támogatja az Evermusic és Flacbox a FLAC streamelést DLNA-n keresztül?" closed="true" %}}
Igen. A Flacbox hi-res formátumokra optimalizált, mint FLAC, ALAC és DSD. Az Evermusic szintén támogatja a FLAC lejátszást MP3 és más szabványos formátumok mellett.
{{% /details %}}

{{% details title="Hallgathatok offline a Kodi-ról történő streamelés után?" closed="true" %}}
Igen. Engedélyezze az Offline módot bármely lejátszási listán, és az alkalmazás letölti az összes számot az eszközére hálózati kapcsolat nélküli hallgatáshoz.
{{% /details %}}

{{% details title="Szükségem van prémium előfizetésre a DLNA használatához?" closed="true" %}}
Az ingyenes verzió legfeljebb 3 felhő- vagy hálózati kapcsolatot támogat. A Premium eltávolítja ezt a korlátot, és korlátlan szolgáltatás és DLNA szerver csatlakoztatását teszi lehetővé.
{{% /details %}}

{{% details title="Az iPhone-omnak ugyanazon a Wi-Fi hálózaton kell lennie, mint a Kodi-nak?" closed="true" %}}
Igen. A DLNA streamelés a helyi hálózaton működik. Mind a Kodi szervernek, mind az iOS eszközének ugyanahhoz a Wi-Fi hálózathoz kell csatlakoznia.
{{% /details %}}

{{% details title="Használhatom ezt a beállítást NAS-szal Mac vagy PC helyett?" closed="true" %}}
Igen. Sok NAS eszköz (Synology, QNAP stb.) támogatja a Kodi-t vagy saját beépített DLNA szerverrel rendelkezik. Az Evermusic és Flacbox bármely szabványos DLNA/UPnP szerverhez csatlakozhat.
{{% /details %}}
