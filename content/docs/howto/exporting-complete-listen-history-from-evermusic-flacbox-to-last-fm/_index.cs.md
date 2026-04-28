---
title: "Exportujte kompletní historii poslechu z Evermusic a Flacbox do Last.fm"
date: 2024-01-30
description: "Naučte se, jak exportovat historii hudby z Evermusic a Flacbox a nahrát ji na Last.fm pomocí souborů CSV a nástroje Last.fm Scrubbler pro Windows."
keywords: ["evermusic", "flacbox", "lastfm", "historie hudby", "scrobbling", "export skladeb", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "nedávné", "lastfm", "export", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Shrnutí:** Exportujte historii poslechu z Evermusic nebo Flacbox jako soubor CSV a poté ji nahrajte na Last.fm pomocí bezplatného nástroje Last.fm-Scrubbler-WPF pro Windows. Automatický scrobbling je také nativně dostupný v obou aplikacích.

**Aktualizace:** Automatický scrobbling je nyní k dispozici! Více informací zde: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling je jednoduchý způsob, jak automaticky uložit základní údaje, jako je název a interpret skladby, kterou právě přehráváte, do online služby. Později si můžete prohlédnout svou historii poslechu.

[Last.fm](https://www.last.fm/home), poháněný systémem doporučování hudby zvaným Audioscrobbler, nabízí tuto službu zdarma. Vytváří podrobný profil vašeho hudebního vkusu zaznamenáváním skladeb, které posloucháte, ať už z internetových rádií, vašeho počítače nebo různých přenosných hudebních zařízení. Později můžete navštívit webové stránky a získat doporučení na nové interprety nebo alba, která odpovídají vašemu hudebnímu vkusu.

Svou historii poslechu můžete nahrát na [Last.fm](http://Last.fm) z aplikací Evermusic a Flacbox pomocí bezplatného nástroje a my vás provedeme, jak na to.

Otevřete sekci 'Hudební knihovna' aplikace a přejděte do sekce 'Rychlý přístup'. Klepněte na položku nabídky 'Nedávné'.

![obrazovka hudební knihovny](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Na obrazovce 'Nedávné' klepněte na tlačítko 'Více' v pravém horním rohu pro aktivaci nabídky 'Další akce'. Klepněte na položku nabídky 'Exportovat seznam skladeb'.

![obrazovka nedávných](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Na obrazovce 'Vyberte formát souboru' máte možnost vybrat formát cílového souboru. Dostupné možnosti - CSV, TXT, M3U.

![obrazovka výběru formátu souboru](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Znamená hodnoty oddělené čárkami, ideální pro organizaci dat do přehledného tabulkového formátu. V cílovém souboru najdete parametry jako Jméno interpreta, Název alba, Název skladby, Časové razítko (čas, kdy jste skladby poslouchali), Jméno interpreta alba a Délka skladby.

TXT: Zde mluvíme o prostém textovém souboru. Je jednoduchý a přímočarý, s parametry včetně Jména interpreta, Názvu alba, Názvu skladby a Délky.

M3U: Tento formát je v podstatě standardem pro vytváření playlistů. Je skvělý, protože můžete exportovat seznam skladeb a přehrávat je na jakémkoli zařízení, i když nemáte originální soubory (za předpokladu, že vyberete možnost absolutní URL pro mediální soubory). Ve výstupním souboru najdete parametry jako Délka, Jméno interpreta, Název skladby a Umístění mediálního souboru.

Pro náš úkol je výběr CSV tou správnou cestou. Tento soubor použijeme s bezplatným softwarem Last.fm-Scrubbler-WPF k nahrání naší historie poslechu do služby [Last.fm](http://Last.fm). Jednoduše zvolte CSV a stiskněte tlačítko 'Exportovat'.

![obrazovka dokončeného exportu](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Po dokončení exportu jednoduše klepněte na tlačítko 'Zobrazit soubor' a aplikace zobrazí vytvořený soubor ve vaší složce dokumentů. Poté klepněte na tlačítko 'Další akce' vedle názvu souboru a z nabídky vyberte možnost 'Otevřít v'. Naším dalším krokem je zkopírovat exportovaný soubor do vašeho stolního počítače. Můžete to snadno provést výběrem možnosti AirDrop z nabídky 'Otevřít v'.

![další akce pro exportovaný soubor](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Dále budeme používat bezplatný open-source klient [Last.FM](http://Last.FM), který je dostupný pouze na platformě Windows. Tento klient vám umožní efektivně aktualizovat historii poslechu na [Last.FM](http://Last.FM) pomocí souboru CSV, který jsme právě exportovali.

Pokud aktuálně nepoužíváte počítač s Windows, nedělejte si starosti. K tomuto klientu se můžete dostat instalací VirtualBox na váš Mac a použitím oficiálního obrazu vývojového prostředí Windows.

Zde je, co musíte udělat:

- Nainstalujte VirtualBox z následujícího odkazu: [Stáhnout VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Stáhněte a nainstalujte vývojové prostředí Windows z tohoto odkazu: [Vývojové prostředí Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Na vašem počítači s Windows (nebo aplikaci VirtualBox s obrazem vývoje Windows) stáhněte a nainstalujte [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - bezplatný open-source software dostupný na GitHub. Testovali jsme verzi 1.28, kterou si můžete stáhnout zde: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![stránka ke stažení Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

V sekci 'Assets' klepněte na [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) pro stažení instalačního archivu. Rozbalte stažený soubor a otevřete rozbalenou složku.

- DŮLEŽITÉ

Tato aplikace je stále ve fázi beta. Tvůrci aplikace neprovedli mnoho testování. Doporučují nejprve zkusit scrobblovat na testovací účet a podívat se, zda věci, které chcete scrobblovat, fungují správně. Zejména pokud scrobblujete mnoho skladeb najednou. Buďte prosím opatrní se svými účty.

Spusťte Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Na hlavní obrazovce aplikace jednoduše klepněte na 'Nepřihlášen', umístěné v levém dolním rohu, pro aktivaci obrazovky 'Přidat účet'.

![obrazovka přidání účtu](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Zadejte své přihlašovací údaje.

![obrazovka zadání přihlašovacích údajů](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Klepněte na tlačítko 'Přihlásit' pro přidání vašeho účtu.

![Klepněte na tlačítko Přihlásit pro přidání vašeho účtu.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Otevřete kartu 'File Parse Scrobbler' pro zahájení importu souboru CSV z aplikace Evermusic.

![Otevřete kartu File Parse Scrobbler pro zahájení importu souboru CSV z aplikace Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Zvolte 'Parser: CSV' a klepněte na tlačítko 'Nastavení'.

Na další obrazovce můžete zvolit pořadí parametrů ve vašem souboru CSV.

Jednotlivá pole mohou být uzavřena v uvozovkách a MUSÍ být uzavřena v uvozovkách, pokud pole obsahuje některý z nastavených oddělovačů. Například:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Ponechte tedy všechna nastavení ve výchozím stavu, jediné, co musíte změnit, je zaškrtnutí políčka v poli 'Has Fields Enclosed In Quotes'.

Klepněte na 'Uložit a zavřít' pro použití změn.

![zvolit pořadí parametrů ve vašem souboru CSV.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Scrobbling analýzy souborů má dva režimy. Lze je změnit pomocí rozbalovací nabídky 'Scrobbling Mode'.

Normální režim: V tomto režimu budou skladby scrobblovány s časovým razítkem z analyzovaného scrobblu. Scrobblovat lze pouze scrobbly novější než 14 dní.

Režim importu: V tomto režimu budou skladby scrobblovány s časovým razítkem vypočítaným z 'Času dokončení' a vybrané délky mezi jednotlivými skladbami. To umožňuje scrobblování skladeb, i když je časové razítko analyzovaného scrobblu starší než 14 dní. Proto bude první (nejvrchnější) skladba v souboru CSV scrobblována s 'Časem dokončení'.

Zvolte dříve vygenerovaný soubor CSV z aplikace Evermusic v poli 'File:' a klepněte na 'Parse'. V některých případech se může zobrazit chybové upozornění, že některé scrobbly nemohly být analyzovány. Je to v pořádku, pokud máte některé skladby bez kompletních metadat, jako je Jméno interpreta.

![některé scrobbly nemohly být analyzovány](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Klepněte na tlačítko 'Vybrat vše' pro výběr všech analyzovaných skladeb.

![Klepněte na tlačítko Vybrat vše pro výběr všech analyzovaných skladeb.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Klepněte na tlačítko 'Náhled' pro kontrolu všech změn, které budou odeslány na server.

![Klepněte na tlačítko Náhled pro kontrolu všech změn, které budou odeslány na server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Klepněte na tlačítko 'Scrobble' pro nahrání všech změn na server.

![Klepněte na tlačítko Scrobble pro nahrání všech změn na server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Dříve Last.fm-Scrubbler-WPF neměl denní limit scrobblů. To se nyní změnilo, protože někteří lidé používali Scrubbler ke scrobblování tolika skladeb, že to způsobovalo problémy na stránce Last.fm. Limit scrobblování je aktuálně 2800 scrobblů za den. Když se pokusíte scrobblovat více, dostanete chybovou zprávu. Existují plány na přidání 'fronty scrobblování', takže pokud potřebujete scrobblovat více než 2800 skladeb, budou přidány do fronty a automaticky scrobblovány po nějaké době. Kolik scrobblů vám zbývá, můžete zkontrolovat v zobrazení výběru uživatele.

Jakmile jsou všechny záznamy úspěšně nahrány na server, uvidíte zprávu v dolní části okna aplikace potvrzující: 'Vybrané skladby úspěšně scrobblovány.'

![Vybrané skladby úspěšně scrobblovány.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Nyní můžete otevřít svůj profil na stránce [Last.fm](http://Last.fm) a zkontrolovat všechny změny.

![váš profil na stránce Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Často kladené otázky

{{% details title="Mohu scrobblovat automaticky bez exportování souborů CSV?" closed="true" %}}
Ano. Evermusic i Flacbox nyní podporují automatický scrobbling na Last.fm. Podívejte se na průvodce: [Jak scrobblovat na Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Co když můj CSV obsahuje skladby starší než 14 dní?" closed="true" %}}
Použijte Režim importu v Last.fm-Scrubbler-WPF. Přepočítá časová razítka z Času dokončení, což vám umožní scrobblovat skladby bez ohledu na jejich původní datum.
{{% /details %}}

{{% details title="Nemám počítač s Windows. Mohu stále používat Last.fm-Scrubbler?" closed="true" %}}
Ano. Nainstalujte VirtualBox na váš Mac a stáhněte si bezplatný obraz vývojového prostředí Windows od Microsoft. Spusťte Last.fm-Scrubbler-WPF uvnitř virtuálního stroje.
{{% /details %}}

{{% details title="Proč nejsou některé scrobbly analyzovány?" closed="true" %}}
Skladby, kterým chybí základní metadata (jako jméno interpreta), nelze analyzovat. To je očekávané a neovlivní to ostatní skladby v souboru.
{{% /details %}}

{{% details title="Existuje denní limit scrobblování?" closed="true" %}}
Ano. Last.fm-Scrubbler-WPF umožňuje až 2 800 scrobblů za den. Pokud potřebujete scrobblovat více, rozdělte proces do více dní.
{{% /details %}}
