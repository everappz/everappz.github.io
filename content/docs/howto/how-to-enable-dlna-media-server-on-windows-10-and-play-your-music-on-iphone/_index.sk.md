---
title: "Ako povoliť DLNA Media Server v systéme Windows 10 a prehrávať hudbu na iPhone"
date: 2019-11-26
description: "Povoľte DLNA server v systéme Windows 10 a streamujte hudbu na iPhone pomocou aplikácie Evermusic. Vrátane podrobného návodu na nastavenie."
keywords: ["evermusic", "dlna", "windows 10", "streamovanie hudby na iphone", "mediálny server", "lokálna sieť", "upnp"]
tags: ["evermusic", "hudba", "cloud", "iphone", "úložisko", "lokálny", "nas", "windows", "wifi", "počúvanie", "sieť", "vzdialený", "domov", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Zhrnutie:** Windows 10 má vstavaný DLNA server. Povoľte ho v nastaveniach Siete a zdieľania, potom použite bezplatnú aplikáciu **Evermusic** na vašom iPhone na streamovanie celej hudobnej knižnice cez Wi-Fi. Nie je potrebný žiadny serverový softvér tretích strán.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Predná strana" caption="Streamovanie hudby cez DLNA na iPhone pomocou Windows 10 a Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) je mocný nástroj, ktorý vám umožňuje jednoducho streamovať rôzny mediálny obsah vrátane hudby medzi zariadeniami s podporou DLNA vo vašej sieti. Dobrá správa je, že Windows 10 aj predchádzajúce verzie obsahujú vstavanú funkciu DLNA, čím odpadá potreba mediálnych serverov tretích strán. Tu je návod, ako povoliť DLNA Media Server v systéme Windows 10 a užívať si streamovanie hudby na iPhone.

## Ako povoliť DLNA Media Server v systéme Windows 10

1. Kliknite na tlačidlo 'Štart'.  
2. Vyberte ikonu 'Nastavenia'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Nastavenie servera" caption="Otvorte Nastavenia Windows" width="500" >}}

3. Na obrazovke 'Nastavenia Windows' zvoľte 'Sieť a internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Nastavenia Windows" caption="Vyberte Sieť a internet" width="500" >}}

4. V časti 'Sieť' vyberte 'Centrum sietí a zdieľania'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Centrum zdieľania" caption="Otvorte Centrum sietí a zdieľania" width="500" >}}

5. Na obrazovke 'Centrum sietí a zdieľania' kliknite na 'Zmeniť rozšírené nastavenia zdieľania' v ľavom menu.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Rozšírené nastavenia zdieľania" caption="Zmeniť rozšírené nastavenia zdieľania" width="500" >}}

6. Na obrazovke 'Rozšírené nastavenia zdieľania' prejdite nadol k sekcii 'Všetky siete' a rozbaľte ju kliknutím na šípku.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Zapnúť zisťovanie" caption="Rozbaľte nastavenia všetkých sietí" width="500" >}}

7. Kliknite na 'Zapnúť streamovanie médií' pre aktiváciu DLNA servera.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Zapnúť server" caption="Povoľte server na streamovanie médií" width="500" >}}

8. Pomenujte svoju mediálnu knižnicu a vyberte zariadenia, ktoré k nej majú prístup.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Názov mediálnej knižnice" caption="Pomenujte svoju DLNA mediálnu knižnicu" width="500" >}}

9. Kliknite na 'OK' pre potvrdenie. Teraz budú vaše osobné priečinky ako Hudba, Obrázky a Videá viditeľné pre všetky streamovacie zariadenia s podporou UPnP.

## Ako zakázať DLNA Media Server v systéme Windows 10

1. Kliknite na 'Štart' a do vyhľadávacieho poľa napíšte 'services'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Služby Windows" caption="Otvorte Služby Windows" width="500" >}}

2. Na obrazovke 'Služby' prejdite nadol a nájdite 'Windows Media Player Network Sharing Service'.  
3. Dvakrát naň kliknite a nastavte 'Typ spustenia' na 'Ručne'.  
4. Zastavte službu kliknutím na tlačidlo 'Zastaviť'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Zastaviť službu DLNA" caption="Zakážte službu zdieľania siete DLNA" width="500" >}}

## Ako prehrávať hudbu z DLNA servera na iPhone

1. Nainštalujte bezplatnú aplikáciu **Evermusic** z App Store:  
   [Aplikácia Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Otvorte záložku 'Pripojenia' a ťuknite na 'Dostupné zariadenia' v sekcii 'Lokálna sieť'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Pripojenia Evermusic" caption="Evermusic: obrazovka Pripojenia" width="500" >}}

3. Počkajte niekoľko sekúnd, kým sa načíta zoznam zariadení, a ťuknite na Windows Media Player DLNA server (napr. 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Dostupné zariadenia" caption="Dostupné DLNA servery v Evermusic" width="500" >}}

4. Uvidíte zoznam priečinkov dostupných na mediálnom serveri.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Priečinky Evermusic" caption="Prehliadajte zdieľané priečinky z DLNA servera" width="500" >}}

5. Otvorte ľubovoľný priečinok obsahujúci audio súbory.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Obsah priečinka" caption="Zobrazenie obsahu zdieľaných DLNA priečinkov" width="500" >}}

6. Ťuknite na ľubovoľný súbor pre spustenie audio prehrávača.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Audio prehrávač" caption="Prehrávanie audio súboru z DLNA v Evermusic" width="500" >}}

7. Pre zlepšenie zvukového zážitku ťuknite na ikonu 'Ekvalizér' pri indikátore hlasitosti v spodnej časti obrazovky pre aktiváciu ekvalizéra v štýle iPod s predzosilňovačom.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Ekvalizér" caption="Použite vstavaný ekvalizér pre lepšie prehrávanie" width="500" >}}

## Záver

S DLNA Media Serverom v systéme Windows 10 a Evermusic na vašom iPhone si môžete užívať plynulé streamovanie hudby z počítača na mobilné zariadenie. Rozlúčte sa s obmedzeniami úložiska a privítajte hudbu na požiadanie!

## Často kladené otázky

{{% details title="Musím na Windows 10 inštalovať nejaký serverový softvér?" closed="true" %}}
Nie. Windows 10 obsahuje vstavaný DLNA mediálny server. Stačí iba povoliť streamovanie médií v nastaveniach Centra sietí a zdieľania. Nie je potrebný žiadny softvér tretích strán.
{{% /details %}}

{{% details title="Musí byť môj iPhone na rovnakej Wi-Fi sieti?" closed="true" %}}
Áno. Streamovanie DLNA funguje cez vašu lokálnu sieť. Váš počítač s Windows 10 aj iPhone musia byť pripojené k rovnakej Wi-Fi sieti, aby Evermusic mohol objaviť DLNA server.
{{% /details %}}

{{% details title="Aké audio formáty môžem streamovať cez DLNA?" closed="true" %}}
Windows DLNA server zdieľa súbory z priečinka Hudba bez ohľadu na formát. Evermusic podporuje MP3, FLAC, AAC, WAV, OGG, AIFF a mnoho ďalších formátov, takže môžete prehrať prakticky akýkoľvek audio súbor zo servera.
{{% /details %}}

{{% details title="Môžem použiť Flacbox namiesto Evermusic?" closed="true" %}}
Áno. Flacbox tiež podporuje prehliadanie a prehrávanie DLNA/UPnP. Môžete použiť ktorúkoľvek z oboch aplikácií na objavenie a prehrávanie hudby z vášho Windows DLNA servera.
{{% /details %}}

{{% details title="Spotrebuje streamovanie DLNA mobilné dáta?" closed="true" %}}
Nie. DLNA funguje výhradne na vašej lokálnej Wi-Fi sieti. Nespotrebováva žiadne mobilné dáta. Obe zariadenia však musia zostať pripojené k rovnakej sieti počas prehrávania.
{{% /details %}}
