---
title: "Ako exportovať kolekciu skladieb do M3U, CSV a TXT v Evermusic a Flacbox"
date: 2024-01-31
description: "Naučte sa, ako exportovať nedávne, obľúbené, playlisty a albumy z Evermusic a Flacbox do formátov M3U, CSV alebo TXT. Ideálne pre scrobblovanie Last.fm a prehrávanie na iných zariadeniach."
keywords: ["export evermusic", "export flacbox", "export do m3u", "export playlistu do csv", "m3u txt csv playlist", "export hudby"]
tags: ["evermusic", "nedávne", "obľúbené", "export", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**Zhrnutie:** Evermusic a Flacbox vám umožňujú exportovať akúkoľvek kolekciu skladieb (nedávne, obľúbené, playlisty, albumy) do súborov CSV, TXT alebo M3U. Tieto exporty použite na scrobblovanie do Last.fm, zálohovanie knižnice alebo prehrávanie playlistov na iných zariadeniach.

## Úvod

Export nedávnych, obľúbených, albumov a playlistov z aplikácie do externého súboru môže byť neuveriteľne užitočný. Tieto súbory môžete použiť na aktualizáciu histórie počúvania v scrobblovacích službách, ako je [Last.fm](http://Last.fm), alebo na počúvanie playlistov na externých zariadeniach. S Evermusic a Flacbox je tento proces jednoduchý. Tu vám ukážeme, ako exportovať nedávne do CSV/TXT a playlisty do M3U. Táto funkcia je však dostupná pre akúkoľvek kolekciu skladieb v aplikácii.

## Výber formátu

Na export nedávnych otvorte sekciu «Hudobná knižnica» a vyberte položku ponuky «Nedávne».

![hudobná knižnica](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Na ďalšej obrazovke klepnite na tlačidlo «Viac» v pravom hornom rohu a vyberte «Export zoznamu skladieb».

![export nedávnych](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Na obrazovke «Výber formátu súboru» máte niekoľko možností — CSV, TXT, M3U.

- CSV

Toto je formát hodnôt oddelených čiarkami, ideálny na organizáciu údajov do prehľadného tabuľkového formátu. V cieľovom súbore nájdete parametre ako meno interpreta, názov albumu, názov skladby, časová pečiatka (čas, kedy ste skladby počúvali), meno interpreta albumu a trvanie skladby. Tento súbor môžete neskôr použiť na aktualizáciu histórie počúvania v scrobblovacích službách, ako je [Last.fm](http://Last.fm), ako je popísané [tu](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Tu hovoríme o jednoduchom textovom súbore. Je jednoduchý a priamočiary, s parametrami zahŕňajúcimi meno interpreta, názov albumu, názov skladby a trvanie. Užitočný, ak potrebujete len zoznam skladieb v textovej podobe.

- M3U

Tento formát je de facto štandardom pre vytváranie playlistov. Je skvelý, pretože môžete exportovať zoznam skladieb a užívať si svoje skladby na akomkoľvek zariadení, aj keď nemáte pôvodné súbory (ak vyberiete možnosť exportu s absolútnou URL pre mediálne súbory). Vo výstupnom súbore nájdete parametre ako trvanie, meno interpreta, názov skladby a umiestnenie mediálneho súboru.

## Formát CSV

Teraz vyberme CSV a pozrime sa, čo dostaneme. Jednoducho vyberte CSV a stlačte tlačidlo «Export».

![výber formátu súboru](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Po dokončení exportu sa zobrazí upozornenie s dvoma možnosťami. Klepnutím na «Zobraziť súbor» zobrazíte výsledný súbor v priečinku dokumentov.

![export dokončený](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Teraz môžete tento súbor odoslať, otvoriť ho v externom textovom editore alebo ho použiť na aktualizáciu pokroku počúvania na [Last.fm](http://Last.fm).

![priečinok exportu s výslednými súbormi](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Výstupný súbor CSV bude obsahovať polia v nasledujúcom formáte:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Napríklad:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![exportovaný súbor csv](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Formát TXT

Výstupný súbor TXT bude obsahovať polia v nasledujúcom formáte:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Napríklad:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![exportovaný súbor txt](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Formát M3U

Ďalej vás prevedieme exportom playlistu do formátu M3U, čo je de facto štandard pre súbory playlistov. Hlavnou podmienkou pre úspešný export playlistu je, že všetky súbory v playliste musia byť umiestnené na rovnakom úložisku, či už ide o cloudovú službu ako Google Drive, lokálne súbory alebo súbory na vašom zariadení. Na začatie procesu exportu otvorte akýkoľvek playlist a klepnite na tlačidlo «Viac» v pravom hornom rohu, potom vyberte položku ponuky «Export zoznamu skladieb».

![obrazovka playlistu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Na ďalšej obrazovke vyberte formát súboru «M3U», kde nájdete dve možnosti pre «Typ umiestnenia mediálnych súborov»:

![obrazovka výberu formátu exportu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Ak vyberiete «Relatívna cesta», playlist sa vytvorí s umiestnením mediálnych súborov zapísaným relatívne k súboru playlistu. Napríklad:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   V tomto prípade sa vyhnite zmene umiestnenia súboru M3U po dokončení exportu, pretože to naruší cesty k mediálnym súborom. Na začatie prehrávania playlistu jednoducho klepnite na exportovaný súbor playlistu a aplikácia automaticky nájde mediálne súbory vo vašom úložisku a začne prehrávanie. Dokonca môžete exportovať playlisty do úložiska a potom ich znova importovať na novom zariadení.

2. Ak vyberiete «Absolútna URL», aplikácia vygeneruje priame URL adresy pre vaše mediálne súbory. To vám umožní prehrávať playlist na akomkoľvek zariadení/aplikácii bez potreby mať všetky mediálne súbory umiestnené na rovnakom úložisku ako súbor playlistu. Táto možnosť je podporovaná len pre cloudové úložiská schopné generovať priame URL adresy súborov. Majte však na pamäti, že v niektorých prípadoch môžu mať vygenerované URL adresy obmedzenú životnosť a môžu po určitom čase vypršať. Tu je zoznam podporovaných cloudových služieb: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (v hosťovskom režime)  

Výstupná URL mediálneho súboru bude vyzerať približne takto:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Po výbere «Typu umiestnenia mediálnych súborov» klepnite na «Export». Aplikácia vás vyzve, aby ste vybrali cieľový priečinok pre export súboru M3U. Klepnite na «Hotovo» na potvrdenie výberu.

![výber priečinka](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Aplikácia vygeneruje súbor M3U a nahrá/presunie ho do cieľového priečinka.

![nahrávanie súboru m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Po dokončení exportu sa zobrazí systémové upozornenie s možnosťou «Zobraziť súbor».

![upozornenie o dokončení exportu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Klepnutím na ňu zobrazíte exportovaný súbor v aplikácii.

![exportovaný súbor m3u v zozname súborov](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Ak ste na predchádzajúcom kroku vybrali «Relatívna cesta» ako «Typ umiestnenia mediálnych súborov», výstupný súbor bude v nasledujúcom formáte:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![príklad m3u s relatívnymi cestami](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Pre možnosť «Absolútna URL» aplikácia vygeneruje súbor M3U vo formáte:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![príklad m3u s absolútnymi URL súborov](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Tento súbor môžete otvoriť na akomkoľvek zariadení/aplikácii, ktorá podporuje playlisty M3U.

![playlist m3u otvorený v externej aplikácii](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Záver

Export skladieb z Evermusic a Flacbox vám dáva úplnú kontrolu nad vašimi hudobnými údajmi. Či už zálohujete históriu počúvania, scrobblujete do Last.fm alebo si užívate playlisty na externých zariadeniach, tieto možnosti exportu — M3U, CSV a TXT — sú výkonné nástroje prispôsobené pre flexibilitu a kompatibilitu. Využite tieto funkcie na vylepšenie organizácie, zdieľania a opätovného prístupu k vašej hudobnej kolekcii na rôznych platformách.

## Často kladené otázky

{{% details title="Ktorý formát exportu mám použiť pre scrobblovanie Last.fm?" closed="true" %}}
Použite CSV. Obsahuje časové pečiatky a úplné metadáta potrebné pre scrobblovacie nástroje ako Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Môžem exportovať akúkoľvek kolekciu skladieb, nielen playlisty?" closed="true" %}}
Áno. Môžete exportovať nedávne, obľúbené, albumy, playlisty a akúkoľvek inú kolekciu skladieb v aplikácii pomocou rovnakých krokov.
{{% /details %}}

{{% details title="Bude môj playlist M3U fungovať na iných zariadeniach?" closed="true" %}}
Ak si počas exportu vyberiete možnosť Absolútna URL, súbor M3U je možné prehrávať na akomkoľvek zariadení, ktoré podporuje playlisty M3U. Upozorňujeme, že niektoré cloudové URL adresy môžu časom vypršať.
{{% /details %}}

{{% details title="Je funkcia exportu zadarmo?" closed="true" %}}
Áno. Export kolekcií skladieb do M3U, CSV a TXT je dostupný v bezplatnej aj prémiovej verzii Evermusic a Flacbox.
{{% /details %}}

{{% details title="Ktoré cloudové služby podporujú export s absolútnou URL?" closed="true" %}}
Export s absolútnou URL je podporovaný pre iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive a WebDAV (hosťovský režim).
{{% /details %}}
