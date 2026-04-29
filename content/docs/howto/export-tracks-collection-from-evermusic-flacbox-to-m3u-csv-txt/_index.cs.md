---
title: "Jak exportovat sbírku skladeb do M3U, CSV a TXT v Evermusic a Flacbox"
date: 2024-01-31
description: "Naučte se exportovat nedávné, oblíbené, seznamy skladeb a alba z Evermusic a Flacbox do formátů M3U, CSV nebo TXT. Ideální pro scrobbling na Last.fm a přehrávání na jiných zařízeních."
keywords: ["export evermusic", "export flacbox", "export do m3u", "export seznamu skladeb do csv", "m3u txt csv seznam skladeb", "export hudby"]
tags: ["evermusic", "nedávné", "oblíbené", "export", "m3u", "seznam skladeb", "csv", "txt", "album"]
---

{{< author-byline >}}


**Shrnutí:** Evermusic a Flacbox vám umožňují exportovat jakoukoli sbírku skladeb (nedávné, oblíbené, seznamy skladeb, alba) do souborů CSV, TXT nebo M3U. Tyto exporty použijte pro scrobbling na Last.fm, zálohování knihovny nebo přehrávání seznamů skladeb na jiných zařízeních.

## Úvod

Export vašich nedávných, oblíbených, alb a seznamů skladeb z aplikace do externího souboru může být nesmírně užitečný. Tyto soubory můžete použít k aktualizaci historie poslechu na scrobblovacích službách jako [Last.fm](http://Last.fm) nebo k poslechu vašich seznamů skladeb na externích zařízeních. S Evermusic a Flacbox je tento proces snadný. Zde vám ukážeme, jak exportovat nedávné do CSV/TXT a vaše seznamy skladeb do M3U. Tato funkce je však dostupná pro jakoukoli sbírku skladeb v aplikaci.

## Výběr formátu

Pro export nedávných otevřete sekci 'Hudební knihovna' a vyberte položku menu 'Nedávné'.

![hudební knihovna](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Na další obrazovce klepněte na tlačítko 'Další akce' v pravém horním rohu a zvolte 'Exportovat seznam skladeb'.

![export nedávných](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Na obrazovce 'Vybrat formát souboru' máte několik možností - CSV, TXT, M3U.

- CSV

Toto znamená hodnoty oddělené čárkami, ideální pro organizaci dat do přehledného tabulkového formátu. V cílovém souboru najdete parametry jako Jméno interpreta, Název alba, Název skladby, Časové razítko (čas poslechu skladeb), Jméno interpreta alba a Délka skladby. Tento soubor můžete později použít k aktualizaci historie poslechu na scrobblovacích službách jako [Last.fm](http://Last.fm), jak je popsáno [zde](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Zde mluvíme o prostém textovém souboru. Je jednoduchý a přímočarý, s parametry zahrnujícími Jméno interpreta, Název alba, Název skladby a Délku. Užitečné, pokud potřebujete pouze seznam skladeb v textové podobě.

- M3U

Tento formát je v podstatě první volbou pro vytváření seznamů skladeb. Je skvělý, protože můžete exportovat seznam skladeb a užívat si své skladby na jakémkoli zařízení, i když nemáte původní soubory (pokud vyberete možnost absolutní URL pro export mediálních souborů). Ve výstupním souboru najdete parametry jako Délka, Jméno interpreta, Název skladby a Umístění mediálního souboru.

## Formát CSV

Nyní vyberme CSV a podívejme se, co dostaneme. Jednoduše zvolte CSV a stiskněte tlačítko 'Exportovat'.

![výběr formátu souboru](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Po dokončení exportu uvidíte upozornění se dvěma možnostmi. Klepnutím na 'Zobrazit soubor' zobrazíte výsledný soubor ve vašem adresáři dokumentů.

![export dokončen](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Nyní můžete tento soubor odeslat, otevřít ho v externím textovém editoru nebo ho použít k aktualizaci vašeho pokroku poslechu na [Last.fm](http://Last.fm).

![složka exportu s výslednými soubory](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Výstupní soubor CSV bude obsahovat pole v následujícím formátu:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Například:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![exportovaný soubor csv](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Formát TXT

Výstupní soubor TXT bude obsahovat pole v následujícím formátu:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Například:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![exportovaný soubor txt](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Formát M3U

Dále vás provedeme exportem vašeho seznamu skladeb do formátu M3U, který je de facto standardem pro soubory seznamů skladeb. Hlavní podmínkou úspěšného exportu seznamu skladeb je, že všechny soubory v seznamu musí být umístěny na stejném úložišti, ať už v cloudové službě jako Google Drive, v lokálních souborech nebo souborech na vašem zařízení. Pro zahájení procesu exportu otevřete jakýkoli seznam skladeb a klepněte na tlačítko 'Další akce' v pravém horním rohu, poté zvolte položku menu 'Exportovat seznam skladeb'.

![obrazovka seznamu skladeb](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Na další obrazovce vyberte formát souboru 'M3U', kde se setkáte se dvěma možnostmi pro 'Typ umístění mediálního souboru':

![obrazovka výběru formátu exportního souboru](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Pokud zvolíte 'Relativní cesta', seznam skladeb bude vytvořen s umístěními mediálních souborů zapsanými relativně k souboru seznamu skladeb. Například:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   V tomto případě se vyhněte změně umístění souboru M3U po dokončení exportu, protože by to porušilo cesty k mediálním souborům. Pro zahájení přehrávání vašeho seznamu skladeb jednoduše klepněte na exportovaný soubor seznamu skladeb a aplikace automaticky vyhledá mediální soubory na vašem úložišti a zahájí přehrávání. Nebo můžete dokonce exportovat své seznamy skladeb na úložiště a poté je znovu importovat na novém zařízení.

2. Pokud zvolíte 'Absolutní URL', aplikace vygeneruje přímé URL adresy pro vaše mediální soubory. To vám umožní přehrávat seznam skladeb na jakémkoli zařízení/aplikaci bez nutnosti mít všechny mediální soubory na stejném úložišti jako soubor seznamu skladeb. Tato možnost je podporována pouze pro cloudové úložiště schopné generovat přímé URL adresy souborů. Mějte však na paměti, že v některých případech mohou mít vygenerované URL adresy omezenou životnost a mohou po nějaké době vypršet. Zde je seznam podporovaných cloudových služeb: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (v režimu hosta)  

Výstupní URL adresa mediálního souboru bude něco jako:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Po výběru 'Typu umístění mediálního souboru' klepněte na 'Exportovat'. Aplikace vás vyzve k výběru cílové složky pro export souboru M3U. Klepněte na 'Hotovo' pro potvrzení vašeho výběru.

![výběr složky](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Aplikace vygeneruje soubor M3U a nahraje/přesune ho do cílové složky.

![nahrávání souboru m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Po dokončení exportu se zobrazí systémové upozornění s možností 'Zobrazit soubor'.

![upozornění o dokončení exportu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Klepnutím na toto zobrazíte exportovaný soubor v aplikaci.

![exportovaný soubor m3u v seznamu souborů](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Pokud jste v předchozím kroku vybrali 'Relativní cesta' jako 'Typ umístění mediálního souboru', výstupní soubor bude v následujícím formátu:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![příklad m3u s relativními cestami](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Pro možnost 'Absolutní URL' aplikace vygeneruje soubor M3U ve formátu:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![příklad m3u s absolutními URL soubory](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Tento soubor můžete otevřít na jakémkoli zařízení/aplikaci, které podporuje seznamy skladeb M3U.

![seznam skladeb m3u otevřený v externí aplikaci](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Závěrečné myšlenky

Export vašich skladeb z Evermusic a Flacbox vám dává úplnou kontrolu nad vašimi hudebními daty. Ať už zálohujete historii poslechu, scrobblujete na Last.fm nebo si užíváte seznamy skladeb na externích zařízeních, tyto možnosti exportu: M3U, CSV a TXT - jsou výkonné nástroje přizpůsobené pro flexibilitu a kompatibilitu. Využijte tyto funkce k vylepšení způsobu, jakým organizujete, sdílíte a znovu navštěvujete svou hudební sbírku napříč platformami.

## Často kladené otázky

{{% details title="Který formát exportu bych měl použít pro scrobbling na Last.fm?" closed="true" %}}
Použijte CSV. Obsahuje časová razítka a úplná metadata vyžadovaná scrobblovacími nástroji jako Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Mohu exportovat jakoukoli sbírku skladeb, nejen seznamy skladeb?" closed="true" %}}
Ano. Můžete exportovat nedávné, oblíbené, alba, seznamy skladeb a jakoukoli jinou sbírku skladeb v aplikaci pomocí stejných kroků.
{{% /details %}}

{{% details title="Bude můj seznam skladeb M3U fungovat na jiných zařízeních?" closed="true" %}}
Pokud během exportu zvolíte možnost Absolutní URL, soubor M3U lze přehrát na jakémkoli zařízení, které podporuje seznamy skladeb M3U. Upozorňujeme, že některé cloudové URL adresy mohou časem vypršet.
{{% /details %}}

{{% details title="Je funkce exportu zdarma?" closed="true" %}}
Ano. Export sbírek skladeb do M3U, CSV a TXT je dostupný jak v bezplatných, tak v prémiových verzích Evermusic a Flacbox.
{{% /details %}}

{{% details title="Které cloudové služby podporují export Absolutní URL?" closed="true" %}}
Export Absolutní URL je podporován pro iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive a WebDAV (režim hosta).
{{% /details %}}
