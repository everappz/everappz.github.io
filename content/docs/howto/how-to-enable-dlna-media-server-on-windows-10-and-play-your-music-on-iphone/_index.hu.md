---
title: "Hogyan engedélyezd a DLNA Media Servert Windows 10-en és játszd le a zenédet iPhone-on"
date: 2019-11-26
description: "Engedélyezd a DLNA szervert Windows 10-en és streameld a zenédet iPhone-ra az Evermusic alkalmazással. Lépésről lépésre beállítási útmutató mellékelve."
keywords: ["evermusic", "dlna", "windows 10", "iphone zene streaming", "médiaszerver", "helyi hálózat", "upnp"]
tags: ["evermusic", "zene", "felhő", "iphone", "tárhely", "helyi", "nas", "windows", "wifi", "hallgatás", "hálózat", "távoli", "otthon", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Röviden:** A Windows 10 beépített DLNA szerverrel rendelkezik. Engedélyezd a Hálózati és megosztási beállításokban, majd használd az ingyenes **Evermusic** alkalmazást iPhone-odon a teljes zenei könyvtárad streameléséhez Wi-Fi-n keresztül. Nincs szükség harmadik féltől származó szerverszoftverre.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Borító" caption="DLNA zenei streaming iPhone-ra Windows 10 és Evermusic használatával" width="800" >}}

A DLNA (Digital Living Network Alliance) egy hatékony eszköz, amely lehetővé teszi különféle médiatartalmak, köztük zene könnyű streamelését a hálózatodon lévő DLNA-támogatott eszközök között. A jó hír az, hogy a Windows 10, és korábbi verziók, beépített DLNA funkcióval rendelkeznek, így nincs szükség harmadik féltől származó médiaszerverekre. Íme, hogyan engedélyezd a DLNA Media Servert Windows 10-en és élvezd a zenei streaminget iPhone-odon.

## Hogyan engedélyezd a DLNA Media Servert Windows 10-en

1. Kattints a 'Start' gombra.  
2. Válaszd a 'Beállítások' ikont.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Szerver beállítás" caption="Nyisd meg a Windows beállításokat" width="500" >}}

3. A 'Windows beállítások' képernyőn válaszd a 'Hálózat és internet' lehetőséget.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows beállítások" caption="Válaszd a Hálózat és internet lehetőséget" width="500" >}}

4. A 'Hálózat' alatt válaszd a 'Hálózati és megosztási központ' lehetőséget.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Megosztási központ" caption="Nyisd meg a Hálózati és megosztási központot" width="500" >}}

5. A 'Hálózati és megosztási központ' képernyőn kattints a 'Speciális megosztási beállítások módosítása' lehetőségre a bal oldali menüben.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Speciális megosztási beállítások" caption="Speciális megosztási beállítások módosítása" width="500" >}}

6. A 'Speciális megosztási beállítások' képernyőn görgess le az 'Összes hálózat' szekcióhoz és bontsd ki a nyílra kattintva.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Felderítés bekapcsolása" caption="Bontsd ki az összes hálózat beállításait" width="500" >}}

7. Kattints a 'Média streaming bekapcsolása' lehetőségre a DLNA szerver aktiválásához.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Szerver bekapcsolása" caption="Engedélyezd a média streaming szervert" width="500" >}}

8. Adj nevet a médiakönyvtáradnak és válaszd ki az eszközöket, amelyek hozzáférhetnek.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Médiakönyvtár neve" caption="Nevezd el a DLNA médiakönyvtáradat" width="500" >}}

9. Kattints az 'OK' gombra a megerősítéshez. Most a személyes mappáid, mint a Zene, Képek és Videók, láthatóak lesznek minden UPnP-támogatású streaming eszköz számára.

## Hogyan tiltsd le a DLNA Media Servert Windows 10-en

1. Kattints a 'Start' gombra és írd be a 'services' szót a keresőmezőbe.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows szolgáltatások" caption="Nyisd meg a Windows szolgáltatásokat" width="500" >}}

2. A 'Szolgáltatások' képernyőn görgess le a 'Windows Media Player Network Sharing Service' megkereséséhez.  
3. Kattints rá duplán és állítsd az 'Indítás típusa' értékét 'Manuális'-ra.  
4. Állítsd le a szolgáltatást a 'Leállítás' gombra kattintva.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="DLNA szolgáltatás leállítása" caption="Tiltsd le a DLNA hálózati megosztási szolgáltatást" width="500" >}}

## Hogyan játssz le zenét a DLNA szerverről iPhone-on

1. Telepítsd az ingyenes **Evermusic** alkalmazást az App Store-ból:  
   [Evermusic alkalmazás](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Nyisd meg a 'Kapcsolatok' fület és érintsd meg az 'Elérhető eszközök' elemet a 'Helyi hálózat' szekcióban.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic kapcsolatok" caption="Evermusic: Kapcsolatok képernyő" width="500" >}}

3. Várj néhány másodpercet az eszközlista betöltéséig és érintsd meg a Windows Media Player DLNA szervert (pl. 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Elérhető eszközök" caption="Elérhető DLNA szerverek az Evermusic-ban" width="500" >}}

4. Megjelenik a médiaszerveren elérhető mappák listája.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic mappák" caption="Böngészd a megosztott mappákat a DLNA szerverről" width="500" >}}

5. Nyiss meg bármilyen mappát, amely hangfájlokat tartalmaz.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Mappa tartalma" caption="Megosztott DLNA mappák tartalmának megtekintése" width="500" >}}

6. Érintsd meg bármelyik fájlt a lejátszó elindításához.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Lejátszó" caption="Hangfájl lejátszása DLNA-ról az Evermusic-ban" width="500" >}}

7. A hangélmény javításához érintsd meg az 'Equalizer' ikont a hangerőjelző közelében a képernyő alján az iPod-stílusú equalizer előerősítővel történő aktiválásához.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Equalizer" caption="Használd a beépített equalizert a jobb lejátszáshoz" width="500" >}}

## Összefoglalás

A Windows 10 DLNA Media Serverével és az Evermusic-kal iPhone-odon zökkenőmentes zenei streaminget élvezhetsz számítógépedről mobileszközödre. Mondj búcsút a tárhelykorlátoknak és üdvözöld az igény szerinti zenét!

## Gyakran ismételt kérdések

{{% details title="Kell szerverszoftvert telepítenem Windows 10-re?" closed="true" %}}
Nem. A Windows 10 beépített DLNA médiaszerverrel rendelkezik. Csak a média streaminget kell engedélyezned a Hálózati és megosztási központ beállításaiban. Nem szükséges harmadik féltől származó szoftver.
{{% /details %}}

{{% details title="Ugyanazon a Wi-Fi hálózaton kell lennie az iPhone-omnak?" closed="true" %}}
Igen. A DLNA streaming a helyi hálózatodon működik. Mind a Windows 10 PC-dnek, mind az iPhone-odnak ugyanahhoz a Wi-Fi hálózathoz kell csatlakoznia, hogy az Evermusic felfedezhesse a DLNA szervert.
{{% /details %}}

{{% details title="Milyen hangformátumokat streamelhetek DLNA-n keresztül?" closed="true" %}}
A Windows DLNA szerver formátumtól függetlenül megosztja a Zene mappád fájljait. Az Evermusic támogatja az MP3, FLAC, AAC, WAV, OGG, AIFF és sok más formátumot, így gyakorlatilag bármilyen hangfájlt lejátszhatsz a szerverről.
{{% /details %}}

{{% details title="Használhatom a Flacbox-ot az Evermusic helyett?" closed="true" %}}
Igen. A Flacbox is támogatja a DLNA/UPnP böngészést és lejátszást. Bármelyik alkalmazást használhatod zenék felfedezéséhez és lejátszásához a Windows DLNA szerveredről.
{{% /details %}}

{{% details title="A DLNA streaming használ mobiladatot?" closed="true" %}}
Nem. A DLNA kizárólag a helyi Wi-Fi hálózatodon működik. Nem használ mobiladatot. Mindkét eszköznek azonban a lejátszás alatt ugyanahhoz a hálózathoz kell csatlakozva maradnia.
{{% /details %}}
