---
title: "Editor tagů"
date: 2020-02-01
description: "Naučte se používat Editor tagů Evertag pro aktualizaci hudebních metadat, úpravu obalů alb, hromadnou úpravu více souborů a správu tagů z MusicBrainz. Ideální pro organizaci hudební knihovny na iOS a Mac."
keywords: [
  "editor tagů Evertag", "editor audio metadat", "editor hudebních tagů",
  "úprava audio tagů iPhone", "editor obalů alb", "hromadná úprava audio tagů",
  "metadata MusicBrainz", "aplikace pro organizaci hudby", "průvodce Evertag", "editor ID3 tagů"
]
tags: ["průvodce", "evertag", "editor tagů"]
readingTime: 5
---


**Editor tagů** je hlavní obrazovka aplikace Evertag, kde můžete zobrazovat a upravovat metadata audio souborů. Tuto obrazovku otevřete klepnutím na soubor ze sekce **Místní soubory** nebo z libovolného připojeného účtu **cloudového úložiště**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka Editoru tagů Evertag" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Režimy úprav

Evertag poskytuje dva režimy úprav:

- **Režim jednoho souboru**  
  - Procházení mezi soubory přejetím doleva nebo doprava na karuselu obalů.  

- **Hromadný režim**  
  - Úprava více souborů najednou a aplikace sdílených metadat.  
  - Pro aktivaci se posuňte dolů a klepněte na **Upravit více souborů současně**.

## Režim jednoho souboru

Ve výchozím nastavení aplikace otevírá editor tagů v režimu jednoho souboru s povolenou pouze hlavními možnostmi úprav. V tomto režimu můžete upravovat nejběžnější pole metadat, jako jsou:

**Název skladby, Podtitul, Interpret alba, Album, Interpret, Skladatel, Performer, Žánr, Komentář, Tempo, Podcast, Kompilace, Číslo disku, Číslo skladby, Celkem skladeb, Hodnocení, Rok**

Pro přístup ke všem dostupným tagům se posuňte dolů na obrazovce a klepněte na možnost **Zobrazit rozšířené tagy**. Tím se editor přepne do rozšířeného režimu, který umožňuje upravovat více než **120 polí metadat**, včetně **MusicBrainz tagů**, **Textů**, **Poradních hodnocení**, hodnot replay-gain, pořadí řazení, metadat podcastů a dalšího. Použijte **Nastavení → Editor audio tagů → Tlačítka na hlavní obrazovce** pro trvalé přepnutí Zobrazit rozšířené tagy, aby bylo vždy zapnuté.

{{< cards cols="1">}}
{{< card title="" subtitle="Panel akcí na spodní části" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Hromadný režim

Do hromadných úprav lze vstoupit dvěma způsoby:

1. **Ze Správce souborů**  
   - Klepněte na **Další akce** (•••) v pravém horním rohu.  
   - Klepněte na **Vybrat**, vyberte více souborů a poté klepněte na **Upravit audio tagy**.

2. **Z Editoru tagů**  
   - Otevřete libovolný soubor, posuňte se dolů a klepněte na **Upravit soubory současně** pro načtení všech souborů ze stejné složky.

{{< cards cols="1">}}
{{< card title="" subtitle="Hromadný režim úprav" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Po úpravách klepněte na **Uložit** pro použití změn.

## Úprava textů

Rozšířený editor zpřístupňuje pole **Texty**. Klepnutím na něj otevřete seznam textů — každý záznam textů má vlastní jazyk a popis, takže jedna skladba může ukládat několik překladů.

Texty nemusíte psát od nuly. Editor obsahuje zkratky pro vyhledávání jedním klepnutím k nejoblíbenějším databázím textů na webu, předvyplněné aktuálním interpretem a názvem skladby:

- **Lrclib** — preferovaná veřejná databáze pro **časované (LRC styl) texty**. Použijte ji, když chcete synchronizované texty, které se v přehrávačích, jež je podporují, posouvají řádek po řádku.
- **Genius** — velký katalog s komentáři a přesnými texty v prostém textu.
- **Lyricsify** — komunitní databáze s prostými a časovanými texty.
- **Google** — obecné webové vyhledávání jako záložní možnost, když specializované databáze nemají shodu.

Každá zkratka se zobrazí pouze tehdy, když je příslušná služba dostupná z vašeho zařízení. Klepněte na službu, zkopírujte texty (nebo LRC časové značky), které chcete, vraťte se do Evertag a vložte je do textového pole — poté **Uložit** pro zápis textů zpět do tagů audio souboru.

{{< cards cols="1">}}
  {{< card title="" subtitle="Stránky textů" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Vyberte jazyk z výběru:

{{< cards cols="1">}}
  {{< card title="" subtitle="Výběr jazyka textů" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Poté vložte nebo napište text textů. Evertag podporuje prostý text i časované (synchronizované) texty — zástupný text zobrazuje příklad formátu LRC, který je přesně to, co Lrclib a Lyricsify vrací pro synchronizované výsledky.

{{< cards cols="1">}}
  {{< card title="" subtitle="Editor textu textů" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Nastavení hodnocení a poradního hodnocení

Rozšířený editor nabízí hvězdičkový ovládací prvek **Hodnocení** spolu s segmentovaným ovládacím prvkem **Poradní hodnocení**.

### Hvězdičkové hodnocení

Použijte pole **Hodnocení** pro přiřazení osobního skóre od jedné do pěti hvězdiček. Hodnota se zapíše do standardního tagu hodnocení souboru (POPM pro ID3, `rate` pro MP4, `RATING` pro Vorbis/APE atd.), takže ostatní aplikace, které čtou tento tag — včetně aplikace Music, Plex, Roon a většiny desktopových editorů tagů — ihned zachytí vaše hodnocení.

{{< cards cols="1">}}
  {{< card title="" subtitle="Hodnocení" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Poradní hodnocení

**Poradní hodnocení** označuje obsah skladby pomocí jedné z hodnot ze standardu Parental Advisory, který iTunes Store a většina hudebních platforem používá:

- **Bezpečné** — výchozí pro skladby bez informací o rodičovské kontrole. Soubor je považován za vhodný pro všechny posluchače a nezobrazí žádné poradní označení v přehrávačích, které tag respektují.
- **Explicitní** — skladba obsahuje explicitní jazyk nebo obsah. Přehrávače, které respektují rodičovské kontroly (aplikace Music, aplikace Apple TV, exporty Spotify, Plex atd.) zobrazí odznak **E** vedle názvu a při povolených omezeních na zařízení nebo účtu mohou skrýt skladbu z dětských profilů nebo odmítnout ji přehrát.
- **Čisté** — cenzurovaná nebo upravená verze jinak explicitní skladby. Přehrávače zobrazují odznak **C**, aby posluchači mohli rozlišit čistou úpravu od původního explicitního masteru, což je užitečné, když obě verze žijí ve stejné knihovně.

Toto pole budete chtít nastavit nebo opravit, když:

- Soubor má nesprávné označení (například čistý rozhlasový střih nesprávně označený jako Explicitní nebo naopak).
- Skladby byly ripovány nebo staženy bez tagu a nyní se zobrazují jako Bezpečné, přestože obsahují explicitní obsah — nezbytné pro správnou funkci rodičovských kontrol a rodinných sdílených knihoven.
- Připravujete album pro odeslání nebo sdílení a potřebujete, aby každá skladba nesla konzistentní metadata.
- Chcete, aby CarPlay, Zamykací obrazovka, přehrávače ve stylu Apple Music nebo DJ software zobrazoval správný odznak **E** / **C** vedle názvu skladby.

Hodnota je uložena ve standardním poli poradního hodnocení pro formát souboru (`rtng` pro MP4, `TXXX:ITUNESADVISORY` pro ID3, `ITUNESADVISORY` pro Vorbis), takže jakýkoli přehrávač, který čte metadata rodičovské kontroly, uvidí vaši aktualizaci.

{{< cards cols="1">}}
  {{< card title="" subtitle="Poradní hodnocení textů" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Úprava obalu alba

Pro změnu obalu alba:

1. Klepněte na **ikonu fotoaparátu** v karuselu obalů.  
2. Vyberte umístění obrázku: Místní soubory, Cloud, Stahování nebo Knihovna fotek.  
3. Vyberte obrázek pro použití jako obal.

{{< cards cols="1">}}
  {{< card title="" subtitle="Výběr obrázku" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Další akce v Editoru tagů

Další možnosti úprav jsou dostupné prostřednictvím panelu nástrojů pod zobrazením obalů.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nabídka Dalších akcí" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Automatické vyhledávání audio tagů

Tato akce aktivuje chytrý vyhledávač tagů, který vyhledá a vyplní úplná metadata pro váš audio soubor na základě existujících informací.  
Aplikace používá databázi MusicBrainz — jednu z nejkomplexnějších databází tagů — s více než **50 miliony** skladeb.

### Vyhledávání obalu alba

Použijte metadata pro vyhledávání správného obalu alba na webu.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Vyhledávání obalu alba" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Po nalezení uložte obrázek do **Fotek** pomocí systémové kontextové nabídky.

{{< cards cols="1">}}
  {{< card title="" subtitle="Přidat obrázek do Fotek" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Poté se vraťte do editoru tagů, klepněte na ikonu fotoaparátu, přejděte do **Knihovny fotek** a vyberte uložený obrázek. Aplikace jej nastaví jako obal vašeho audio souboru.

Způsob škálování obrázků obalů si můžete upravit v nastavení aplikace.

### Uložit obal alba

Tato akce uloží aktuální obal alba do složky **Dokumenty**, takže jej můžete později znovu použít.

### Normalizovat kódování

Tato akce normalizuje textové kódování všech tagů v metadatech audio souboru. Je zvláště užitečná, pokud přecházíte z počítače se systémem Windows, kde soubory mohou používat různá kódování, která se na Macu zobrazují jako nečitelné nebo poškozené znaky.

### Ruční vyhledávání tagů

Ručně vyhledejte metadata alba pomocí databáze MusicBrainz.  

- Vyberte album  

{{< cards cols="1">}}
  {{< card title="" subtitle="Výběr alba" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Vyberte správnou píseň  

{{< cards cols="1">}}
  {{< card title="" subtitle="Výběr písně" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Zvolte, které tagy použít  

{{< cards cols="1">}}
  {{< card title="" subtitle="Výběr audio tagů" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Klepnutím na **Hotovo** použijte vybraná metadata na skladbu.

### Smazat audio tagy

Vymazání všech polí metadat souboru. Užitečné při začínání od nuly. Klepnutím na **Uložit** potvrďte.

## Nastavení Editoru tagů

Přejděte do **Nastavení → Editor audio tagů** pro přizpůsobení chování.

### Škálování obalu alba

Vyberte způsob škálování obalů alb při ukládání do audio souborů. Škálování lze zakázat pro zachování původní velikosti obrázku, ale mějte na paměti, že některé přehrávače nemusí podporovat velké soubory obalů. Možnost "původní velikost" je součástí funkcí personalizace Premium.

### Možnosti ukládání tagů

- **ID3v2.4** — při povolení aplikace ukládá tagy ve formátu ID3v2.4, kdykoli je to možné. Deaktivujte pro návrat na více podporovaný ID3v2.3, pokud se audio tagy na starších přehrávačích nebo zařízeních nezobrazují správně.
- **Duplicitní tagy** — při povolení jsou běžná pole metadat duplikována do obou sekcí tagů souboru. To zlepšuje kompatibilitu se staršími audio přehrávači, ale ve většině případů to není nutné.

### Možnosti aktualizace metadat cloudových souborů

Můžete ovládat, jak aplikace aktualizuje metadata pro audio soubory uložené v cloudových službách:

- **Zobrazit potvrzovací zprávu**  
  Zeptejte se před aplikací změn metadat na cloudové soubory.

- **Automaticky aktualizovat metadata souboru**  
  Uložte změny metadat do cloudového souboru automaticky po úpravách.

- **Neaktualizovat metadata souboru**  
  Přeskočte aktualizaci cloudových souborů — změny se použijí pouze místně.

### Úprava online souborů

Zvolte, co se stane s místně staženými kopiemi cloudových souborů po úpravách:

- **Vždy smazat stažený soubor**  
  Odstraňte místní kopii po uložení změn.

- **Nesmazat stažený soubor**  
  Ponechte stažený soubor v zařízení po úpravách.

### Tlačítka hlavní obrazovky

Přizpůsobte, které akce se zobrazí na hlavní obrazovce editoru tagů (Automatické vyhledávání audio tagů, Ruční vyhledávání audio tagů, Vyhledávání obalu alba, Uložit obal alba, Normalizovat kódování, Smazat audio tagy). Můžete také přepínat **Zobrazit rozšířené tagy** a **Upravit soubory současně**, aby se editor vždy otevíral v preferovaném režimu.
