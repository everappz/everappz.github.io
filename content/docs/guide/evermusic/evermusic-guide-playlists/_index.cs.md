---
title: "Seznamy skladeb"
date: 2020-01-01
description: "Naučte se vytvářet, importovat, přizpůsobovat a spravovat playlisty v Evermusic. Zahrnuje podrobné kroky pro úpravy, řazení, offline režim a přístupnost."
keywords: [
  "Evermusic", "playlisty", "správa playlistů", "import M3U playlistu",
  "úprava playlistu", "offline playlist", "změna pořadí playlistu", "obal playlistu",
  "přístupnost playlistu", "přehrávač zvuku"
]
tags: ["evermusic", "guide", "playlists"]
readingTime: 6
---


## Přehled

Sekce Seznamy skladeb vám poskytuje nástroje pro organizaci stop do seznamů. Zahrnuje zobrazení obsahu s přehledem všech vytvořených playlistů, tlačítko "..." v navigační liště nabízející různé akce relacionované s playlisty a navigační panel nástrojů s tlačítky "Hledat", "Přehrát vše" a "Zamíchat vše". Navíc každý jednotlivý playlist má tlačítko "..." vedle názvu playlistu, nabízející řadu akcí specifických pro daný playlist.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka Playlistů Evermusic" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-main.webp" >}}
{{< /cards >}}

## Vytvoření playlistu

Pro vytvoření nového playlistu klepněte na tlačítko "+" nebo tlačítko "..." v pravém horním rohu navigační lišty, vyberte "Nový playlist" a přiřaďte název playlistu. Po pojmenování klepněte na "Uložit".

{{< cards cols="1">}}
  {{< card title="" subtitle="Vytvoření nového playlistu" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-add-new.webp" >}}
{{< /cards >}}

Tím se otevře dialog "Přidat skladby", kde si můžete vybrat, které stopy přidat do nového playlistu. Stopy jsou kategorizovány podle typu zdroje a máte několik možností:

- **Knihovna**: Stopy z vaší hudební knihovny.
- **Soubory v této aplikaci**: Zvukové soubory uložené v adresáři Dokumenty aplikace.
- **Soubory na tomto iPhone/iPad/Macu**: Zvukové soubory umístěné v jiných složkách zařízení, mimo aplikaci.
- **Připojení**: Online soubory uložené v připojených cloudových úložných službách.

Ve výchozím nastavení můžete přidat stopu do playlistu pouze jednou. Pro povolení duplicitních skladeb v playlistu aktivujte tuto funkci v Nastavení aplikace - Hudební knihovna - Playlisty - Duplikáty v playlistu - Aktivovat.

## Import playlistu

V Evermusic jsme přidali funkci importu souborů M3U, takže nemusíte ručně vytvářet playlisty.

{{< cards cols="1">}}
  {{< card title="" subtitle="Import playlistu ze zdroje souborů" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-import-from-files.webp" >}}
{{< /cards >}}

Nejprve přejděte do sekce "Seznamy skladeb". Poté klepněte na tlačítko "Více" v pravém horním rohu. Z nabídky, která se zobrazí, vyberte možnost "Importovat playlist".

Na další obrazovce vyberte umístění souboru. Podporované možnosti zahrnují:

- Připojené cloudové úložiště
- Soubory v aplikaci
- Soubory na zařízení

Vyberme připojené cloudové úložiště a otevřeme složku obsahující soubor playlistu. Podporované přípony souborů playlistu zahrnují M3U, M3U8 a CUE. Vyberte soubor playlistu a klepněte na "Hotovo" pro potvrzení výběru.

Aplikace analyzuje soubor playlistu, vytvoří seznam stop a vyhledá tyto soubory v úložišti pro sestavení finálního playlistu, který bude importován do hudební knihovny. Je zásadní, aby váš soubor M3U/CUE obsahoval správné cesty pro mediální soubory, a soubory by měly být umístěny v těchto cestách ve vašem úložišti. Více o importu playlistů si přečtete [zde](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Obrazovka detailu playlistu

Když otevřete playlist, zobrazí se "Obrazovka detailu playlistu". Na této obrazovce najdete tlačítko "..." v pravém horním rohu s možnostmi playlistu a tři tlačítka pod obrázkem uměleckého díla: "Hledat", "Pokračovat v přehrávání", "Přehrát vše" a "Zamíchat vše". Navíc je zde zaškrtávací políčko "Offline režim".

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka detailu playlistu" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-detail-screen.webp" >}}
{{< /cards >}}

- **Pokračovat v přehrávání**: Obnoví pozici přehrávání pro tento playlist.
- **Hledat**: Provede vyhledávání v aktuálním playlistu.
- **Přehrát vše**: Přidá všechny stopy z aktuálního playlistu do fronty přehrávače.
- **Zamíchat vše**: Podobně jako "Přehrát vše", ale stopy před přidáním do fronty přehrávače zvuku zamíchá.
- **Offline režim**: Stáhne všechny stopy z tohoto playlistu do lokálních souborů. Jakékoli nové položky přidané do playlistu se automaticky stáhnou.

## Další akce pro playlist na obrazovce Playlistů

Akce playlistu získáte klepnutím na tlačítko "..." vedle názvu playlistu. Zde jsou dostupné akce:

- **Přehrát vše:** Přidá stopy playlistu do nové fronty přehrávače.
- **Přehrát jako další:** Přidá stopy playlistu na začátek existující fronty přehrávače.
- **Přehrát později:** Přidá stopy playlistu na konec existující fronty přehrávače.
- **Upravit obrázek:** Upraví obrázek uměleckého díla playlistu.
- **Aktivovat offline režim:** Aktivuje offline režim pro playlist. V tomto scénáři se jak existující, tak nové stopy automaticky stáhnou. Více o offline režimu si přečtete [zde](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Exportovat seznam skladeb:** Tento playlist můžete exportovat do různých formátů, jak je popsáno [zde](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Přidat do archivu:** Tento playlist včetně souboru m3u, obalu alba a všech stop můžete archivovat, jak je popsáno [zde](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Přidat skladby:** Přidejte do aktuálního playlistu další skladby.
- **Přejmenovat:** Přejmenujte playlist.
- **Smazat playlist:** Smazat playlist z hudební knihovny. Upozorňujeme, že tuto akci nelze vrátit zpět.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nabídka Další akce pro playlist" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-more-actions-for-separate-playlist.webp" >}}
{{< /cards >}}

## Další akce pro playlist na obrazovce detailu playlistu

Akce playlistu získáte klepnutím na tlačítko "..." v pravém horním rohu. Zde jsou dostupné akce:

- **Vybrat:** Aktivuje režim výběru stop, užitečný pro mazání více stop z playlistu nebo změnu jejich pořadí.
- **Přehrát jako další:** Přidá stopy playlistu na začátek existující fronty přehrávače.
- **Přehrát později:** Přidá stopy playlistu na konec existující fronty přehrávače.
- **Přidat skladby:** Přidejte nové skladby do playlistu.
- **Přeřadit skladby:** Ručně změňte pořadí skladeb v playlistu pomocí přetažení.
- **Přejmenovat:** Přejmenuje aktuální playlist.
- **Upravit obrázek:** Upraví obal alba pro aktuální playlist.
- **Exportovat seznam skladeb:** Exportuje tento playlist do různých formátů. Více si přečtete [zde](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Přidat do archivu:** Zkomprimuje aktuální playlist včetně všech stop a souboru m3u. Více si přečtete [zde](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Seřadit:** Změní pořadí stop v playlistu. Možnosti řazení zahrnují "Název skladby", "Číslo skladby", "Album", "Interpret", "Interpret alba", "Žánr", "Skladatel", "Hodnocení", "Rok", "Údery za minutu", "Délka", "Název souboru", "Datum změny souboru", "Datum vytvoření souboru" a "Ručně". Možnost řazení "Ručně" umožňuje ruční přeřazení skladeb pomocí přetažení.
- **Hledat:** Vyhledejte konkrétní skladbu v aktuálním playlistu.
- **Mřížka/Seznam:** Změňte prezentaci rozložení obrazovky.
- **Smazat playlist:** Smazat playlist z hudební knihovny. Důležité je, že tato akce nesmaže stopy z úložiště a nelze ji vrátit zpět.

## Změna pořadí skladeb v playlistu

Pro změnu pořadí skladeb v playlistu klepněte na tlačítko "..." v pravém horním rohu a vyberte "Vybrat" pro vstup do režimu výběru. Pro přesun stop nahoru nebo dolů použijte ovládací prvek přeřazení a gesta přetažení vedle každé stopy. Klepnutím na ovládací prvek přeřazení se stopa přesune na začátek seznamu. Pro opuštění režimu výběru a aplikaci změn klepněte na "Hotovo".

{{< cards cols="1">}}
  {{< card title="" subtitle="Změna pořadí skladeb v playlistu" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-change-songs-order.webp" >}}
{{< /cards >}}

## Změna obrázku obalu playlistu

Pro změnu obrázku obalu playlistu klepněte na tlačítko "..." v pravém horním rohu a vyberte "Upravit obrázek". Vyberte obrázek z dostupných zdrojů a klepnutím na "Hotovo" potvrďte změny.

## Přidání skladeb do playlistu

Otevřete playlist a klepněte na tlačítko "..." v pravém horním rohu, poté vyberte "Přidat skladby" pro otevření dialogu. Vyberte stopy, které chcete přidat, a klepnutím na "Hotovo" potvrďte změny.

## Mazání více skladeb z playlistu

Otevřete playlist, klepněte na tlačítko "..." v pravém horním rohu a vyberte "Vybrat" pro vstup do režimu výběru. Vyberte stopy, které chcete smazat, a klepněte na tlačítko "Smazat z playlistu" ve spodní části obrazovky. Klepnutím na "Hotovo" potvrďte změny.

{{< cards cols="1">}}
  {{< card title="" subtitle="Režim výběru uvnitř playlistu" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-selection-mode-in-playlist-details-screen.webp" >}}
{{< /cards >}}

## Možnosti stopy

Každá stopa v playlistu má seznam akcí, dostupných klepnutím na tlačítko "...". Pokud nevidíte všechny akce, posuňte se dolů pro jejich zobrazení. Stopu z playlistu můžete smazat, stáhnout, upravit audio tagy a další.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nabídka možností stopy v playlistu" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-track-options.webp" >}}
{{< /cards >}}

- **Přehrát jako další:** Přidá stopu na začátek fronty přehrávače.
- **Přehrát později:** Přidá stopu na konec fronty přehrávače.
- **Přidat do playlistu:** Přidá stopu do playlistu.
- **Přidat do oblíbených:** Označí stopu jako oblíbenou pro rychlý přístup.
- **Stáhnout:** Zpřístupní stopu offline. Zobrazí se ve frontě přenosů a na záložce "Lokální soubory" v sekci "Stažená hudba" hudební knihovny.
- **Upravit audio tagy:** Otevře vestavěný editor tagů pro změnu metadat stopy.
- **Otevřít v:** Exportuje stopu a otevře ji v jiné aplikaci.
- **Zobrazit ve složce:** Odhalí složku, kde se zvukový soubor nachází.
- **Zobrazit ve Finderu:** Pro soubory importované z Macu tato akce odhalí složku, kde se zvukový soubor nachází na Mac počítači.
- **Smazat z playlistu:** Smaže stopu z playlistu.
- **Smazat z cloudové služby:** Smaže stopu z playlistu a přidružené cloudové služby. Upozorňujeme, že tuto akci nelze vrátit zpět.
- **Smazat z hudební knihovny:** Smaže stopu z hudební knihovny a ponechá soubor v úložišti nedotčen.

## Přístupnost

Naše aplikace je plně přístupná s technologií VoiceOver, která zajišťuje, že každá komponenta má dobře navrženou popisku a popis. Když je VoiceOver aktivní, aplikace přeloží uživatelské rozhraní do textového režimu, zobrazujíce pouze přístupné a užitečné prvky pro zlepšení rychlosti navigace a pohodlí. Textový režim můžete také aktivovat v Nastavení > Přístupnost > Textový režim.

Pro nastavení pozice stopy v playlistu pomocí VoiceOver:

1. Otevřete playlist a klepněte na tlačítko "Více".
2. Vyberte "Změnit pořadí skladeb". Zobrazení se přepne do režimu úprav.
3. Klepněte na ikonu indikátoru přeřazení vedle názvu stopy pro její fokusování.
4. Rychle dvakrát klepněte na ikonu indikátoru přeřazení. Při druhém klepnutí neuvolňujte prst — podržte ho, dokud neuslyšíte zvuk označující, že buňka je připravena k přesunutí.
5. Nyní můžete buňku přesunout na novou pozici.

Ostatní komponenty fungují podle očekávání, využívajíce systémem poskytnuté vzory VoiceOver.
