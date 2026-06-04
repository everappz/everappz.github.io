---
title: "Hudební knihovna"
date: 2020-02-01
description: "Naučte se vytvářet, organizovat a synchronizovat svou hudební knihovnu ve Flacboxu na iPhonu, iPadu a Macu. Přidávejte skladby ručně nebo synchronizujte z cloudových služeb, spravujte metadata, obaly alb, seznamy skladeb, oblíbené, nedávné a záložky. Zahrnuje podporu Hi-Res zvuku, editor tagů MusicBrainz, online a offline synchronizaci a možnosti personalizace."
keywords: [
  "hudební knihovna Flacbox", "synchronizace hudby z cloudu", "organizace hudebních metadat",
  "úprava zvukových tagů Flacbox", "offline synchronizace hudby", "import místní hudby",
  "správa seznamů skladeb Flacbox", "hledání obalů alb Flacbox",
  "metadata hudby iPhone", "průvodce aplikací Flacbox",
  "Flacbox MusicBrainz", "normalizace tagů Flacbox",
  "hi-res hudební knihovna Flacbox", "knihovna FFmpeg Flacbox",
  "sólová alba Flacbox", "pohled skladatele Flacbox"
]
tags: ["hudba", "příručka", "flacbox", "knihovna"]
readingTime: 11
---


Správa vaší hudební knihovny je s Flacboxem hračka — snadno organizujete všechny vaše stopy — místní FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE a desítky dalších formátů — do jedné prohledávatelné sbírky. Pro sestavení hudební knihovny máte dvě možnosti: ruční přidávání (vy přesně určujete, co se přidá) nebo automatická synchronizace (Flacbox prohledává určené cloudové složky a automaticky přidává nové soubory, jakmile se objeví).

{{< cards cols="1">}}
  {{< card title="" subtitle="Zobrazení alb hudební knihovny Flacbox" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Ruční Přidávání

Chcete-li přidat stopy ručně, klepněte na ikonu **Přidat hudbu** v levém horním rohu a vyberte složky nebo soubory z připojené cloudové úložiště nebo soubory na vašem zařízení. Při přidávání stop do knihovny se vytváří pouze odkazy na tyto stopy — skutečné soubory zůstávají na svých původních místech, aby šetřily cenné místo na disku. Chcete-li mít stopy k dispozici offline, můžete použít akci Stáhnout z nabídky možností nebo povolit Offline režim pro seznamy skladeb a sbírky stop.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Přidat skladby do hudební knihovny" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Na verzi pro Mac můžete také přetáhnout soubory do knihovny nebo použít **Otevřít soubory…** / **Otevřít složku…** ze systémového výběru souborů na iPhonu a iPadu.

## Pokračovat v Přehrávání

Obnovte frontu přehrávače ze poslední uložené pozice, pokud je tato funkce povolena v nastavení aplikace. Povolte **Uložit stav přehrávače** i **Uložit pozici přehrávání** v Nastavení → Přehrávač zvuku → Obecné pro nejlepší zážitek. Po povolení se tlačítko **Pokračovat v přehrávání** zobrazí v horní části každé složky, alba, interpreta, žánru a obrazovky seznamu skladeb — klepnutím se okamžitě vrátíte na přesnou stopu a pozici, kde jste skončili.

## Umístění

Všechny stopy ve vaší knihovně jsou promyšleně seskupeny podle typu zdroje a hudebních tagů. Skladby můžete filtrovat podle umístění pomocí tlačítka **Další akce** v pravém horním rohu a výběrem **Filtr**.

### Online hudba

Tato sekce zobrazuje hudbu z vašich připojených cloudových úložišť. Stopy zde se přehrávají na vyžádání; nic nezabírá místní úložiště, dokud explicitně nestáhnete nebo nepovolíte offline režim.

### Soubory v Této Aplikaci

Zde najdete hudbu dostupnou pro offline přehrávání pocházející z vašich místních souborů. Zahrnuje soubory v adresáři Documents aplikace — vše, co jste stáhli, přenesli přes Wi-Fi Drive nebo importovali přes Sdílení souborů Finder.

### Soubory na Tomto iPhone / iPad / Mac

Tato kategorie zahrnuje hudbu importovanou do aplikace z vašeho zařízení, přidanou prostřednictvím systémového dialogu **Otevřít soubory…**. Původní soubory zůstávají na svém původním místě; Flacbox si pouze uchovává odkaz na ně.

## Kategorie

Když přidáte stopy do hudební knihovny, aplikace automaticky přečte jejich zvukové tagy a zorganizuje je do kategorií jako Skladby, Nepřehrané skladby, Alba, Interpreti alba, Interpreti, Žánry a Skladatelé.

## Seskupení Tagů

Tyto kategorie pomáhají organizovat vaše stopy podle hudebních tagů. Když přidáte stopy do hudební knihovny, aplikace přečte jejich metadata a seskupí je podle těchto kategorií. Pokud nevidíte všechna alba, ujistěte se, že aplikace prohledala každou stopu. Průběh prohledávání lze zkontrolovat v Nastavení → Hudební knihovna → Čtení metadat → Počet zpracovaných souborů v hudební knihovně. Pro místní soubory můžete také znovu prohledat offline složky v Nastavení → Hudební knihovna → Synchronizace offline složek → Spustit skenování místních složek. Po dokončení všech operací čtečkou metadat uvidíte ve své hudební knihovně tyto kategorie:

- **Skladby** — všechny skladby seskupené podle tagu TRACK_TITLE. Pořadí řazení lze zkontrolovat pomocí nabídky Další akce v pravém horním rohu.
- **Nepřehrané skladby** — všechny skladby, které nikdy nebyly přehrány.
- **Alba** — skladby seskupené podle tagu ALBUM_NAME, ignorující tagy interpreta, interpreta alba a skladatele. Máte-li několik alb se stejným názvem od různých interpretů, zvažte použití řazení Výhradní alba popsaného níže.
- **Interpreti alba** — skladby seskupené pouze podle tagu ALBUM_ARTIST_TAG. Užitečné pro přehledné oddělení kompilací a spoluprací od sólové tvorby.
- **Interpreti** — skladby seskupené pouze podle tagu ARTIST_TAG.
- **Žánry** — skladby seskupené podle tagu GENRE.
- **Skladatelé** — skladby seskupené podle tagu COMPOSER — neocenitelné pro knihovny klasické hudby, kde je „skladatel" primární navigační osou.

## Oblíbené

Skladby můžete označit jako oblíbené na obrazovce přehrávače zvuku nebo pomocí nabídky možností. Oblíbené se zobrazují ve vlastní sekci, takže je najdete jedním klepnutím.

## Nedávné

Tato sekce zobrazuje všechny naposledy přehrávané stopy. Počet položek, které seznam nedávných uchovává, lze přizpůsobit v Nastavení → Knihovna → Nedávné → Změnit velikost seznamu a seznam lze exportovat do M3U / CSV / TXT pro zálohu historii poslechu.

## Záložky

Při přehrávání skladby můžete vytvářet zvukové záložky a spravovat je na této obrazovce — ideální pro audioknihy, dlouhé mixety, přednášky nebo jen označení refrénu oblíbené stopy. Podrobné pokyny pro práci se zvukovými záložkami jsou k dispozici [zde](/docs/guide/evermusic/evermusic-guide-music-library).

## Horní Panel Nástrojů

Horní panel nástrojů umístěný bezprostředně pod navigační lištou nabízí několik pohodlných akcí: Hledat, Přehrát vše, Přehrát vše náhodně a Pokračovat v přehrávání. Panel nástrojů lze zobrazit nebo skrýt jednoduchým přejetím dolů.

## Vyhledávání

Funkce vyhledávání vám umožňuje najít konkrétní stopu, interpreta, album nebo žánr v hudební knihovně. Na obrazovce Vyhledávání máte přístup k akcím Seřadit, Filtrovat a zobrazení Mřížka / Seznam. Vyhledávání probíhá lokálně v databázi hudební knihovny, takže funguje plně offline a vrací výsledky při psaní.

{{< cards cols="1">}}
  {{< card title="" subtitle="Vyhledávání v hudební knihovně Flacbox" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Nabídka Možností

Každá skladba v hudební knihovně má nabídku s dalšími akcemi, přístupnou klepnutím na tlačítko se třemi tečkami vedle názvu skladby. Tyto akce se liší podle toho, zda jde o jednu skladbu nebo část sbírky.

### Pro Jednotlivé Skladby

- **Přehrát jako další** — přidá skladbu na vrchol fronty přehrávače.
- **Přehrát později** — přidá skladbu na konec fronty přehrávače.
- **Přidat do seznamu skladeb** — přidá skladbu do seznamu skladeb.
- **Přidat do oblíbených** — označí skladbu jako oblíbenou pro rychlý přístup.
- **Stáhnout** — uloží skladbu do místních souborů. Zobrazí se na kartě **Místní soubory** a v sekci **Offline hudba**.
- **Upravit audio tagy** — otevře vestavěný editor zvukových tagů pro opravu chybějících metadat; upozorňujeme, že tím se skladba na vašem úložišti změní.
- **Zobrazit ve složce** — odhalí složku, kde je zvukový soubor uložen.
- **Zobrazit ve Finderu** — pro soubory importované z Macu tato akce odhalí složku, kde se zvukový soubor na Macu nachází.
- **Otevřít v** — exportuje zvukový soubor do jiné aplikace.
- **Smazat z cloudové služby** — odstraní soubor jak z hudební knihovny, tak z cloudového úložiště. **Tato akce je nevratná.**
- **Smazat z hudební knihovny** — odstraní skladbu z hudební knihovny, ale soubor zůstane v úložišti. Pokud je automatická synchronizace povolena a soubor existuje na vzdáleném úložišti, po operaci synchronizace se v knihovně znovu objeví.

### Pro Sbírky Skladeb

Pro sbírky skladeb jako Alba, Interpreti, Žánry nebo Skladatelé nabídka možností zahrnuje tyto akce.

- **Přehrát vše** — nahradí frontu přehrávače skladbami z vybrané sbírky.
- **Přehrát jako další** — přidá skladby z této sbírky na vrchol fronty přehrávače.
- **Přehrát později** — přidá skladby z této sbírky na konec fronty přehrávače.
- **Přidat do seznamu skladeb** — zahrne skladby z této sbírky do seznamu, s možností vytvoření nového.
- **Povolit offline režim** — stáhne skladby z této sbírky do místních souborů. Soubory se zobrazí na kartě **Místní soubory** a v sekci **Offline hudba**. Pokud jsou na serveru přidány nové položky do sbírky, automaticky se stáhnou.
- **Upravit obrázek** — změní obal alba pro sbírku skladeb.
- **Přidat do archivu** — zabalí celou sbírku do jednoho ZIP souboru pro snadnou zálohu nebo přenos (funkce Premium).
- **Exportovat seznam skladeb** — exportuje sbírku do M3U, CSV nebo TXT pro použití v jiných přehrávačích nebo pro archivaci.
- **Smazat z hudební knihovny** — odstraní sbírku skladeb z hudební knihovny. Tato akce nesmaže skutečné soubory z úložiště. Pokud je automatická synchronizace povolena a soubory existují na vzdáleném úložišti, po operaci synchronizace se v knihovně znovu objeví.

## Režim Výběru

Režim výběru lze aktivovat pomocí tlačítka Další akce v pravém horním rohu. V tomto režimu můžete najednou vybrat více stop a provádět hromadné akce — přidat do seznamu, označit jako oblíbené, smazat z knihovny, stáhnout a další.

## Detail Alba

Při otevření sekcí Interpret, Interpret alba nebo Skladatel vidíte přepínač pro Skladby / Všechna alba / Výhradní alba / Sólová alba.

- **Skladby** — zobrazuje všechny skladby, kde se tento Interpret / Interpret alba / Skladatel vyskytuje v zvukových tazích.
- **Všechna alba** — zobrazuje kompilační alba a všechna alba, kde je interpret přítomen.
- **Výhradní alba** — zobrazuje alba, kde je zadaný interpret jediným interpretem s daným názvem alba.
- **Sólová alba** — zobrazuje alba, kde se vyskytují pouze stopy zadaného interpreta, i když jiní interpreté mají alba se stejným názvem.

To je obzvláště užitečné pro vyčištění nepřehledných kompilací „Různí interpreti" ve velkých knihovnách.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka detailu alba Flacbox" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Nastavení

Klepněte na Další akce → Nastavení pro konfiguraci předvoleb hudební knihovny.

### Čtení Metadat

Když přidáte stopy do knihovny, čtečka metadat se dá do práce. Tento proces na pozadí čte všechna metadata z vašich stop a organizuje je podle Interpreta, Alba, Žánru a Skladatele. Rychlost čtení metadat lze upravit pro rychlejší načítání dat — mějte na paměti, že rychlejší čtení spotřebuje více energie. Čtečku metadat lze také zcela deaktivovat a místo informací z tagů zobrazit názvy souborů.

Čtečka metadat **pouze aktualizuje metadata ve vaší hudební knihovně** a nemění soubory uložené ve vašem cloudovém účtu nebo místním úložišti. Chcete-li upravit metadata zvukových souborů, použijte vestavěný **editor tagů** prostřednictvím příslušné akce v nabídce možností.

### Dostupné Režimy Čtečky Metadat

- **Deaktivováno** — čtečka metadat je vypnutá a zobrazují se názvy souborů místo dat zvukových tagů.
- **Aktuální skladba** — aplikace čte metadata pouze pro aktuálně přehrávanou skladbu. Použijte tuto možnost, pokud máte pomalé síťové připojení, aby čtečka neposílala na cloudový server mnoho požadavků, které by mohly způsobit přerušení přehrávání.
- **Fronta přehrávání** — aplikace čte metadata pro všechny skladby ve frontě přehrávače.
- **Knihovna** — aplikace čte metadata pro všechny skladby v hudební knihovně.

Když je zapnutý přepínač **Čtení metadat na pozadí**, čtečka metadat pokračuje v práci v režimu na pozadí. Upozorňujeme, že pokud aplikace spotřebovává při přehrávání hodně energie, iOS ji může pozastavit.

Pokud tedy máte velkou hudební sbírku, doporučujeme provést synchronizaci metadat na desktopové verzi aplikace a poté přenést synchronizovanou hudební knihovnu na iOS pomocí funkce **Záloha a obnovení**.

Když je povolena možnost **Normalizovat kódování metadat**, aplikace automaticky normalizuje kódování metadat pro všechny skladby. Tím se opravují poškozená kódování tagů (například po úpravě souborů na Windows PC) a zabrání se zobrazení nesprávných znaků v informacích o stopě.

Akce **Načíst metadata** označí každý soubor v hudební knihovně jako soubor s chybějícími metadaty, čímž se spustí obnovení každého záznamu čtečkou.

Klepnutím na **Spustit čtení metadat** spustíte čtečku ručně. Průběh operace se zobrazí níže.

### Online Synchronizace

Automatická online synchronizace hudby přidává stopy z připojených cloudových služeb do hudební knihovny automaticky. Chcete-li ji aktivovat, otevřete nastavení hudební knihovny a vyberte složky pro synchronizaci.

S povolenou touto možností aplikace prohledá vybrané složky, identifikuje podporované zvukové soubory a přidá je do vaší knihovny. Synchronizaci spustíte nebo zastavíte příslušnou akcí v nabídce.

Online synchronizace běží pouze tehdy, když je aplikace v popředí, takže synchronizace velké knihovny může chvíli trvat. Chcete-li věci urychlit, nechte Flacbox otevřený, připojte zařízení k napájení a povolte **Nastavení → Obrazovka → Vždy aktivní**.

Alternativně proveďte online synchronizaci na desktopové verzi aplikace a přeneste výsledek na iOS pomocí **Záloha a obnovení**.

Také si můžete zvolit, jak často se online synchronizace spouští. Nastavení intervalu na **Okamžitě** spustí synchronizaci pokaždé, když aplikaci otevřete.

### Offline Synchronizace

Nakonfigurujte offline synchronizaci hudby.

#### Synchronizované Offline Složky

Když označíte online složku ve svém cloudovém serveru jako dostupnou offline (pomocí nabídky **Další akce**), zobrazí se zde. Obsah složky se stáhne do **Místní soubory → Offline složky**. Když se online složka změní (soubory přidány, odebrány nebo aktualizovány), aplikace zkontroluje změny a aktualizuje místní kopii na vašem zařízení.

Na této obrazovce můžete ručně spustit synchronizaci offline složky, odhalit offline složku v nadřazené složce a zakázat offline režim pro složku. Zakázáním offline režimu se ze zařízení odeberou všechny místní kopie souborů.

#### Časový Interval

Zvolte, jak často aplikace kontroluje offline složky na úpravy.

#### Spustit Skenování Místních Složek

Prohledá všechny místní složky v adresáři **Documents** aplikace pro podporované zvukové soubory. Nalezené soubory jsou automaticky přidány do hudební knihovny. Soubory umístěné na vašem zařízení mimo adresář Documents aplikace musí být do hudební knihovny přidány ručně, protože k nim aplikace nemůže přistupovat kvůli bezpečnostním omezením iOS / macOS.

**Důležité:** Doporučujeme pravidelně zahajovat offline synchronizaci hudby, aby byla hudební knihovna aktuální s vašimi místními soubory.

### Personalizace

V této sekci lze nakonfigurovat styl obrazovky hudební knihovny. Jsou k dispozici tři možnosti: Jednoduchá nabídka, Seskupená nabídka, Nabídka se záložkami. Také lze zapnout nebo vypnout zobrazení obalů alb na obrazovkách detailu alba.

### Obaly Alb

Nakonfigurujte, jak aplikace načítá a ukládá obaly alb.

- **Typ sítě** — zvolte **Wi-Fi** nebo **Wi-Fi a mobilní data** pro stahování obalů.
- **Načíst obaly alb pro online soubory** — při zapnutí se načítají vložené obaly alb pro soubory uložené v cloudovém úložišti. Může použít další síťová data.
- **Hledat ve složce** — při zapnutí, pokud stopa nemá vložený obal, aplikace hledá obrázky JPEG nebo PNG ve stejné složce a použije je jako obal alba.
- **Kvalita obalu** — zvolte kvalitu obalů alb uložených na vašem zařízení.
- **Zobrazit ve složce** — otevře složku s uloženými obaly alb v mezipaměti.
- **Smazat vše** — smaže obaly alb z mezipaměti pro uvolnění úložiště a přinutí aplikaci je znovu načíst na vyžádání.

### Seznamy Skladeb

Povolte možnost přidat stejnou skladbu do seznamu dvakrát. Výchozí nastavení je zakázáno.

### Nedávné

Spravujte seznam naposledy přehrávaných skladeb.

- **Smazat seznam** — smaže celý seznam naposledy přehrávaných skladeb.
- **Změnit velikost seznamu** — nastavte počet položek v seznamu.
- **Exportovat seznam skladeb** — exportujte seznam naposledy přehrávaných skladeb jako M3U, CSV nebo TXT. Podrobné pokyny jsou k dispozici [zde](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Oblíbené

Spravujte seznam oblíbených skladeb.

- **Simultánní úpravy** — při zapnutí přidání skladby do oblíbených ji přidá zároveň do hudební knihovny i sekce souborů.
- **Smazat seznam** — smaže celý seznam oblíbených skladeb.
- **Exportovat seznam skladeb** — stejně jako Nedávné, exportujte oblíbené jako M3U, CSV nebo TXT.

### Smazat Knihovnu

Tato akce vymaže databázi hudební knihovny. Vaše hudební soubory v úložišti zůstanou nedotčeny.

### Limit Načítání Obsahu

Výchozí nastavení aplikace používá stránkování pro urychlení načítání obsahu. Stránkování lze deaktivovat pro načtení všeho najednou. Chcete-li tak učinit, otevřete nastavení aplikace, přejděte dolů na Personalizace → Limit načítání obsahu a zvolte Deaktivováno.
