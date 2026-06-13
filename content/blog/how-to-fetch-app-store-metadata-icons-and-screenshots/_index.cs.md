---
title: "Jak zdarma stáhnout metadata, ikony a snímky obrazovky z App Store"
date: 2026-06-13
description: "Návod krok za krokem, jak získat metadata, ikonu, snímky obrazovky a lokalizované údaje App Store pro jakoukoli iOS aplikaci pomocí AppLookup.pro, bezplatného nástroje v prohlížeči využívajícího oficiální iTunes Search API."
keywords: [
  "metadata app store", "získat data app store", "stáhnout ikonu app store",
  "stáhnout snímky obrazovky app store", "nástroj vyhledávání app store", "itunes search api",
  "extraktor metadat aplikace", "metadata iOS aplikace", "bezplatný nástroj api app store",
  "stáhnout ikonu aplikace ve vysokém rozlišení", "analýza konkurence app store",
  "lokalizovaná data app store", "vyhledávání země app store", "bezplatný nástroj aso"
]
tags: [
  "Metadata App Store", "Vyhledávání aplikací", "iTunes Search API",
  "Stažení ikony aplikace", "Snímky obrazovky aplikací", "ASO analýza"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Získejte data App Store za pár sekund

**Krátká verze:** [AppLookup.pro](https://applookup.pro) je bezplatný nástroj, který získává veřejná data pro jakoukoli aplikaci iOS, iPadOS, macOS nebo tvOS. Získáte název, popis, novinky, verzi, cenu, hodnocení, ikonu aplikace, snímky obrazovky, podporovaná zařízení a surovou odpověď iTunes API. Každé pole má tlačítko kopírování jedním klepnutím. Otevřete stránku, vložte odkaz App Store nebo napište název aplikace a máte data.

Použijte to pro:

- **ASO analýzu.** Podívejte se, jak top aplikace píší své názvy, podtituly, popisy a klíčová slova.
- **Sledování konkurence.** Zkontrolujte aktualizace verzí, hodnocení a ceny na různých trzích.
- **Stahování materiálů.** Uložte oficiální ikonu aplikace a snímky obrazovky v plné velikosti v jednom ZIPu.
- **Kontroly lokalizace.** Porovnejte popis, novinky a snímky obrazovky ve více než 40 zemích App Store.
- **Testování API.** Zkopírujte surový JSON iTunes Search API přímo do svého kódu nebo Postmana.

## Co je AppLookup.pro?

[AppLookup.pro](https://applookup.pro) je bezplatný nástroj pro vyhledávání v App Store založený na prohlížeči. Běží zcela na vašem zařízení. Každý výsledek pochází přímo z oficiálního [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) od Apple. Žádný scraping. Žádná registrace. Žádné sledování.

### Co získáte

- **Vyhledávání podle názvu aplikace nebo URL App Store.** Automatické dokončování ukazuje výsledky v reálném čase při psaní.
- **Více než 40 zemských obchodů.** Přepínejte mezi US, UK, JP, DE, FR, BR a dalšími.
- **Kompletní metadata.** Název, podtitul, vývojář, bundle ID, verze, cena, velikost souboru, hodnocení, datum vydání, věkové hodnocení, jazyky a podporovaná zařízení.
- **Materiály ve vysokém rozlišení.** Ikony aplikací a snímky obrazovky pro iPhone, iPad, macOS a Apple TV.
- **Hromadné stažení ZIP.** Získejte všechny ikony nebo všechny snímky obrazovky v jednom archivu.
- **Surový JSON iTunes API.** Přesná odpověď od Apple, připravená ke zkopírování.
- **Tlačítka kopírování u každého pole.** Jedno klepnutí vloží hodnotu do schránky.

## Jak používat AppLookup.pro krok za krokem

### Krok 1. Zadejte název aplikace nebo vložte URL App Store

Otevřete [applookup.pro](https://applookup.pro) a začněte psát název aplikace. Automatické dokončování ukazuje výsledky App Store v reálném čase při psaní.

Můžete také vložit přímý odkaz App Store, jako je `https://apps.apple.com/us/app/instagram/id389801252`, nebo jen ID aplikace. Nástroj za vás extrahuje ID. Zpracovává také přesměrovací URL Google.

![Zadejte název aplikace nebo URL App Store do AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Krok 2. Získejte informace o aplikaci a stáhněte ikonu

Klikněte na **Lookup** nebo stiskněte Enter. Nástroj volá oficiální iTunes Search API a zobrazí ikonu aplikace, jméno vývojáře, hodnocení, verzi a cenu za méně než sekundu.

Posuňte se na sekci **App Icon**. Každá velikost ikony, kterou Apple vrátí, se zobrazí jako karta. Každá karta má:

- **Direct Link.** Otevře obrázek v plné velikosti na nové kartě.
- **Download.** Uloží soubor do počítače.

Použijte **Download All Icons (ZIP)** k získání všech velikostí ikon v jednom archivu. Totéž platí pro snímky obrazovky: každá sekce platformy má vlastní tlačítko **Download All (ZIP)**.

![Stáhněte ikony aplikací a snímky obrazovky z AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Krok 3. Přečtěte si podrobnosti aplikace a zkopírujte jakékoli pole

Posuňte se na **App Details**. Uvidíte bundle ID, verzi, cenu, velikost souboru, minimální OS, datum vydání, datum poslední aktualizace, věkové hodnocení, žánry, ID žánrů, jazyky, prodejce, ID umělce a ID skladby.

Klepněte na tlačítko **Copy** na jakékoli kartě. Hodnota se přesune do schránky a tlačítko zobrazí zelený «Copied» háček.

Totéž funguje pro **Description**, **What's New** a **Supported Devices**. Tyto sekce jsou posuvné, takže si můžete přečíst celý text bez ztráty místa, a tlačítko Copy vloží celé pole do schránky.

![Zobrazte úplné podrobnosti App Store a zkopírujte jakékoli pole jedním klepnutím](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Krok 4. Zobrazte surovou odpověď API App Store

Potřebujete přesný JSON, který Apple vrací? Posuňte se na **Raw API Response**. Plná datová zátěž iTunes Search API se zobrazí v posuvném prohlížeči s tlačítkem **Copy** nahoře. Jedno klepnutí zkopíruje celý JSON objekt.

**iTunes Lookup URL** je zobrazena přímo nad ní. Vložte ji do Postmana, curl nebo vašeho prohlížeče a přehrajte stejný požadavek.

![Zobrazte a zkopírujte surovou JSON odpověď iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Krok 5. Změňte zemi a zobrazte lokalizovanou verzi

Metadata App Store se mění podle země. Stejná aplikace má často jiný název, podtitul, popis, snímky obrazovky a cenu na každém trhu.

Vyberte zemi z rozbalovacího menu nahoře. URL ve vstupním poli se automaticky aktualizuje. Klikněte znovu na **Lookup** a aplikace se znovu načte na tomto trhu.

Toto je nejrychlejší způsob, jak zkontrolovat, jak konkurent prezentuje svou aplikaci v Japonsku, Německu, Brazílii nebo v kterékoli z více než 40 podporovaných zemí.

![Přepněte země obchodů a zobrazte lokalizovaná metadata App Store](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Krok 6. Zkopírujte lokalizovaná metadata

Jakmile se výsledek země načte, každé pole funguje stejně. Klepněte na **Copy** v popisu, novinkách, názvu aplikace, vývojáři, bundle ID nebo na jakékoli kartě podrobností pro získání lokalizovaného textu.

To usnadňuje vytváření srovnávacích tabulek vedle sebe nebo předávání lokalizovaného textu k překladové kontrole.

![Zkopírujte lokalizovaný popis a metadata App Store jedním klepnutím](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Kdo používá AppLookup.pro

- **Nezávislí vývojáři** provádějící ASO analýzu před spuštěním.
- **Týmy ASO a marketingu** sledující aktualizace a ceny konkurence.
- **Designéři**, kteří získávají oficiální ikonu aplikace ve vysokém rozlišení a snímky obrazovky pro tiskové sady a případové studie.
- **Lokalizační týmy** auditující, které trhy jsou pokryty a kde je stále dodáván výchozí anglický text.
- **Backend a QA inženýři** testující integrace iTunes Search API bez psaní scraperu.
- **Autoři a blogeři**, kteří potřebují oficiální ikonu aplikace a několik snímků obrazovky pro příspěvek.

## Soukromí a prohlášení

AppLookup.pro běží ve vašem prohlížeči. Není zde žádné přihlášení. Není zde žádné sledování. Není zde žádné serverové logování aplikací, které vyhledáváte. Požadavky jdou přímo z vašeho prohlížeče do [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) od Apple.

Tento nástroj slouží pouze pro **vzdělávací a výzkumné účely**. Všechna data jsou získávána z oficiálního veřejného API Apple a zůstávají vlastnictvím Apple Inc. a uvedených vydavatelů aplikací. Použití nástroje podléhá [Apple Media Services Terms and Conditions](https://www.apple.com/legal/internet-services/terms/site.html). Respektujte prosím limity rychlosti Apple a nesdílejte materiály chráněné autorskými právy.

## Vyzkoušejte hned

Nepotřebujete klíč API, vývojářský účet ani placený plán k prozkoumání dat App Store. Otevřete [applookup.pro](https://applookup.pro), vložte jakoukoli URL App Store a budete mít metadata, ikony a surový JSON za pár sekund.

## Open Source

AppLookup.pro je open source. Hlášení chyb, přidávání zemí a pull requesty jsou vítány.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro na GitHubu" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Často kladené otázky

{{% details title="Je AppLookup.pro opravdu zdarma?" closed="true" %}}
Ano. AppLookup.pro je 100 procent zdarma a open source. Běží ve vašem prohlížeči. Není zde registrace, placená úroveň ani limit používání nad rámec vlastních limitů iTunes Search API od Apple.
{{% /details %}}

{{% details title="Odkud pocházejí data?" closed="true" %}}
Každý výsledek je získáván v reálném čase z oficiálního [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) od Apple. Nástroj nescrapuje stránky App Store a neukládá odpovědi do mezipaměti na žádném serveru.
{{% /details %}}

{{% details title="Mohu stáhnout ikonu aplikace ve vysokém rozlišení?" closed="true" %}}
Ano. Sekce **App Icon** zobrazuje každou URL ikony, kterou Apple vrací. Každá karta má Direct Link a tlačítko Download a tlačítko Download All Icons ZIP je zabalí do jednoho archivu.
{{% /details %}}

{{% details title="Mohu stáhnout všechny snímky obrazovky App Store najednou?" closed="true" %}}
Ano. Každá sekce snímků obrazovky (iPhone, iPad, macOS a Apple TV) má tlačítko **Download All (ZIP)**, které sbalí každý snímek obrazovky v plném rozlišení.
{{% /details %}}

{{% details title="Jak vidím, jak aplikace vypadá v jiné zemi?" closed="true" %}}
Vyberte zemi v rozbalovacím menu v horní části stránky. Je podporováno více než 40 obchodů. Klikněte znovu na **Lookup** a nástroj znovu načte aplikaci pro tuto zemi, zobrazí lokalizovaný název, popis, snímky obrazovky, novinky a cenu.
{{% /details %}}

{{% details title="Mohu kopírovat jednotlivá pole, jako je bundle ID nebo datum vydání?" closed="true" %}}
Ano. Každé textové pole ve výsledku má vlastní tlačítko Copy: název aplikace, vývojář, popis, novinky, bundle ID, verze, cena, velikost souboru, minimální OS, datum vydání, věkové hodnocení, jazyky, podporovaná zařízení a surový JSON.
{{% /details %}}

{{% details title="Funguje AppLookup.pro pro jakoukoli iOS aplikaci?" closed="true" %}}
Funguje pro jakoukoli aplikaci, která je veřejně uvedena alespoň v jedné zemi App Store a vrácena iTunes Search API. Nezařazené, odstraněné nebo podnikově distribuované aplikace se nezobrazí.
{{% /details %}}

{{% details title="Podporuje aplikace macOS a Apple TV?" closed="true" %}}
Ano. Pokud má aplikace snímky obrazovky macOS nebo Apple TV v odpovědi iTunes Search API, AppLookup.pro je zobrazí ve vlastním posuvném panelu s tlačítky pro stahování.
{{% /details %}}

{{% details title="Mohu použít surový JSON ve vlastním kódu?" closed="true" %}}
Ano. Sekce Raw API Response zobrazuje přesný JSON, který Apple vrací. Zkopírujte jej do Postmana, jednotkového testu nebo backend pipeline. Respektujte prosím podmínky API Apple a rozumné limity rychlosti.
{{% /details %}}

{{% details title="Je bezpečné vkládat URL App Store do nástroje?" closed="true" %}}
Ano. URL je analyzována ve vašem prohlížeči. Jediné odchozí síťové volání je vyhledávání v iTunes Search API od Apple.
{{% /details %}}

{{% details title="Jaký je rozdíl mezi AppLookup.pro a AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) slouží ke čtení metadat App Store z jakékoli zveřejněné aplikace: analýza konkurence, stahování materiálů, kontroly lokalizace. [AppKeywords.pro](https://appkeywords.pro) slouží k psaní metadat App Store pro vaši vlastní aplikaci: optimalizace názvu, podtitulu a klíčových slov s podporou Fastlane. Tyto dva nástroje spolu dobře fungují.
{{% /details %}}
