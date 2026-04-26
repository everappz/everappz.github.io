---
title: "Jak importovat seznam skladeb M3U do Evermusic a Flacbox"
date: 2024-01-31
description: "Zjistěte, jak importovat soubory seznamů skladeb M3U, M3U8 a CUE z cloudu, místního úložiště nebo zařízení do Evermusic a Flacbox."
keywords: ["evermusic", "flacbox", "seznam skladeb", "m3u", "m3u8", "cue", "import", "hudební aplikace"]
tags: ["evermusic", "import", "seznamy skladeb", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Shrnutí:** Evermusic a Flacbox podporují import souborů seznamů skladeb M3U, M3U8 a CUE z cloudového úložiště, místních souborů aplikace nebo vašeho zařízení. Přejděte na Seznamy skladeb > Více > Importovat seznam skladeb, vyberte zdroj, zvolte soubor a aplikace automaticky vytvoří váš seznam skladeb.

M3U, což znamená MP3 URL nebo Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, je formát počítačového souboru používaný pro multimediální seznamy skladeb. Jedním z jeho hlavních využití je vytváření souborů seznamů skladeb s jedním záznamem, které odkazují na streamy na internetu. Tyto soubory nabízejí pohodlný přístup ke streamovanému obsahu a běžně se používají pro stahování, e-maily a poslech internetového rádia.

Navzdory širokému používání neexistuje formální specifikace formátu M3U; stal se de facto standardem. Soubor M3U je v podstatě prostý textový soubor, který určuje umístění jednoho nebo více mediálních souborů. V závislosti na kódování se ukládá s příponou "m3u" nebo "m3u8". Každý záznam v souboru určuje umístění mediálního souboru, což může být absolutní místní cesta, místní cesta relativní k umístění souboru M3U nebo URL. Záznamy jsou odděleny konci řádků, přičemž některá zařízení vyžadují konce řádků reprezentované jako CR LF.

Kromě toho mohou soubory M3U obsahovat komentáře uvozené znakem "#". V rozšířeném M3U "#" zavádí rozšířené direktivy M3U, které mohou podporovat parametry ukončené dvojtečkou ":".

V našich aplikacích Evermusic a Flacbox jsme implementovali funkci importu souborů M3U, čímž odpadá nutnost ručního vytváření seznamů skladeb. Tato příručka vás provede importem vašich seznamů skladeb z cloudového úložiště, místních souborů nebo souborů na vašem zařízení přímo do aplikace.

Nejprve přejděte do sekce 'Seznamy skladeb'. Poté klepněte na tlačítko 'Více' v pravém horním rohu. Z nabídky, která se zobrazí, vyberte možnost 'Importovat seznam skladeb'.

![akce importu seznamu skladeb](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Na další obrazovce zvolte umístění souboru. Podporované možnosti zahrnují:

- Připojené cloudové úložiště;
- Soubory v aplikaci;
- Soubory na vašem zařízení;

![výběr umístění souboru](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Vyberme připojené cloudové úložiště a otevřeme složku obsahující soubor seznamu skladeb. Podporované přípony souborů seznamů skladeb zahrnují M3U, M3U8 a CUE. Vyberte soubor seznamu skladeb a klepněte na 'Hotovo' pro potvrzení výběru.

![výběr souboru M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Aplikace analyzuje soubor seznamu skladeb a vytvoří seznam skladeb. Poté tyto soubory najde v úložišti a sestaví konečný seznam skladeb, který bude importován do hudební knihovny. Je zásadní, aby váš soubor M3U/CUE obsahoval správné cesty k mediálním souborům a soubory se nacházely na těchto cestách ve vašem úložišti.

![importovaný seznam skladeb](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Aplikace podporuje jak relativní cesty, tak absolutní URL souborů.

Například:

Seznam skladeb s relativními cestami:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Seznam skladeb s absolutními URL:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Pokud importujete soubor seznamu skladeb umístěný v aplikaci (sekce Místní soubory), nejsou potřeba žádné další kroky.

Pokud však chcete importovat seznam skladeb umístěný na vašem zařízení pomocí systémového výběru souborů, je třeba mít na paměti důležitou skutečnost.

Kvůli bezpečnostním zásadám může aplikace přistupovat pouze k souboru, který vyberete pomocí systémového výběru souborů. Soubor seznamu skladeb však může obsahovat odkazy na další mediální soubory na vašem zařízení. Pro import seznamu skladeb z vašeho zařízení musíte vybrat složku obsahující jak soubor seznamu skladeb, tak všechny mediální soubory, na které odkazuje. V tomto případě aplikace prohledá vybranou složku, najde soubor seznamu skladeb, sestaví seznam skladeb a importuje jej do hudební knihovny.

Kromě toho můžete importovat více seznamů skladeb najednou klepnutím na tlačítko "Další akce" a výběrem "Importovat seznamy skladeb ze složky". Aplikace poté prohledá obsah složky, najde podporované soubory seznamů skladeb a importuje je do knihovny.

## Často kladené otázky

{{% details title="Jaké formáty seznamů skladeb podporují Evermusic a Flacbox?" closed="true" %}}
Obě aplikace podporují formáty souborů seznamů skladeb M3U, M3U8 a CUE. Tyto pokrývají nejběžnější standardy seznamů skladeb používané hudebními přehrávači a multimediálním softwarem.
{{% /details %}}

{{% details title="Mohu importovat seznamy skladeb z cloudového úložiště?" closed="true" %}}
Ano. Můžete importovat soubory seznamů skladeb z jakékoli připojené cloudové úložné služby včetně Google Drive, Dropbox, OneDrive a serverů WebDAV.
{{% /details %}}

{{% details title="Proč po importu chybí některé skladby?" closed="true" %}}
Soubor seznamu skladeb musí obsahovat správné cesty k vašim mediálním souborům a tyto soubory musí existovat na uvedených umístěních ve vašem úložišti. Zkontrolujte, zda cesty k souborům ve vašem souboru M3U nebo CUE odpovídají skutečným umístěním souborů.
{{% /details %}}

{{% details title="Mohu importovat více seznamů skladeb najednou?" closed="true" %}}
Ano. Použijte tlačítko Další akce a vyberte "Importovat seznamy skladeb ze složky". Aplikace prohledá složku a najde všechny podporované soubory seznamů skladeb a importuje je v jednom kroku.
{{% /details %}}

{{% details title="Musím vytvářet seznamy skladeb ručně?" closed="true" %}}
Ne. Funkce importu odstraňuje nutnost ručního vytváření seznamů skladeb. Stačí nasměrovat aplikaci na váš existující soubor M3U, M3U8 nebo CUE a ta automaticky vytvoří seznam skladeb.
{{% /details %}}
