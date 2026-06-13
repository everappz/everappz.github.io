---
title: "Ako zdarma získať metadáta, ikony a snímky obrazovky z App Store"
date: 2026-06-13
description: "Návod krok za krokom, ako získať metadáta, ikonu, snímky obrazovky a lokalizované údaje App Store pre akúkoľvek iOS aplikáciu pomocou AppLookup.pro, bezplatného nástroja v prehliadači využívajúceho oficiálne iTunes Search API."
keywords: [
  "metadáta app store", "získať dáta app store", "stiahnuť ikonu app store",
  "stiahnuť snímky obrazovky app store", "nástroj vyhľadávania app store", "itunes search api",
  "extraktor metadát aplikácie", "metadáta iOS aplikácie", "bezplatný nástroj api app store",
  "stiahnuť ikonu aplikácie vo vysokom rozlíšení", "analýza konkurencie app store",
  "lokalizované dáta app store", "vyhľadávanie krajiny app store", "bezplatný nástroj aso"
]
tags: [
  "Metadáta App Store", "Vyhľadávanie aplikácií", "iTunes Search API",
  "Stiahnutie ikony aplikácie", "Snímky obrazovky aplikácií", "ASO analýza"
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

## Získajte dáta App Store za pár sekúnd

**Krátka verzia:** [AppLookup.pro](https://applookup.pro) je bezplatný nástroj, ktorý získava verejné dáta pre akúkoľvek aplikáciu iOS, iPadOS, macOS alebo tvOS. Získate názov, popis, novinky, verziu, cenu, hodnotenia, ikonu aplikácie, snímky obrazovky, podporované zariadenia a surovú odpoveď iTunes API. Každé pole má tlačidlo kopírovania jedným klepnutím. Otvorte stránku, vložte odkaz App Store alebo napíšte názov aplikácie a máte dáta.

Použite to na:

- **ASO analýzu.** Pozrite sa, ako top aplikácie píšu svoje názvy, podtituly, popisy a kľúčové slová.
- **Sledovanie konkurencie.** Skontrolujte aktualizácie verzií, hodnotenia a ceny na rôznych trhoch.
- **Sťahovanie materiálov.** Uložte oficiálnu ikonu aplikácie a snímky obrazovky v plnej veľkosti v jednom ZIPe.
- **Kontroly lokalizácie.** Porovnajte popis, novinky a snímky obrazovky vo viac ako 40 krajinách App Store.
- **Testovanie API.** Skopírujte surový JSON iTunes Search API priamo do svojho kódu alebo Postmana.

## Čo je AppLookup.pro?

[AppLookup.pro](https://applookup.pro) je bezplatný nástroj na vyhľadávanie v App Store založený na prehliadači. Beží úplne na vašom zariadení. Každý výsledok pochádza priamo z oficiálneho [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) od Apple. Žiadny scraping. Žiadna registrácia. Žiadne sledovanie.

### Čo získate

- **Vyhľadávanie podľa názvu aplikácie alebo URL App Store.** Automatické dopĺňanie ukazuje výsledky v reálnom čase pri písaní.
- **Viac ako 40 krajinských obchodov.** Prepínajte medzi US, UK, JP, DE, FR, BR a ďalšími.
- **Kompletné metadáta.** Názov, podtitul, vývojár, bundle ID, verzia, cena, veľkosť súboru, hodnotenia, dátum vydania, vekové hodnotenie, jazyky a podporované zariadenia.
- **Materiály vo vysokom rozlíšení.** Ikony aplikácií a snímky obrazovky pre iPhone, iPad, macOS a Apple TV.
- **Hromadné stiahnutie ZIP.** Získajte všetky ikony alebo všetky snímky obrazovky v jednom archíve.
- **Surový JSON iTunes API.** Presná odpoveď od Apple, pripravená na skopírovanie.
- **Tlačidlá kopírovania pri každom poli.** Jedno klepnutie vloží hodnotu do schránky.

## Ako používať AppLookup.pro krok za krokom

### Krok 1. Zadajte názov aplikácie alebo vložte URL App Store

Otvorte [applookup.pro](https://applookup.pro) a začnite písať názov aplikácie. Automatické dopĺňanie ukazuje výsledky App Store v reálnom čase pri písaní.

Môžete tiež vložiť priamy odkaz App Store, ako je `https://apps.apple.com/us/app/instagram/id389801252`, alebo len ID aplikácie. Nástroj za vás extrahuje ID. Spracováva tiež presmerovacie URL Google.

![Zadajte názov aplikácie alebo URL App Store do AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Krok 2. Získajte informácie o aplikácii a stiahnite ikonu

Kliknite na **Lookup** alebo stlačte Enter. Nástroj volá oficiálne iTunes Search API a zobrazí ikonu aplikácie, meno vývojára, hodnotenie, verziu a cenu za menej ako sekundu.

Posuňte sa na sekciu **App Icon**. Každá veľkosť ikony, ktorú Apple vráti, sa zobrazí ako karta. Každá karta má:

- **Direct Link.** Otvorí obrázok v plnej veľkosti na novej karte.
- **Download.** Uloží súbor do počítača.

Použite **Download All Icons (ZIP)** na získanie všetkých veľkostí ikon v jednom archíve. To isté platí pre snímky obrazovky: každá sekcia platformy má vlastné tlačidlo **Download All (ZIP)**.

![Stiahnite ikony aplikácií a snímky obrazovky z AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Krok 3. Prečítajte si podrobnosti aplikácie a skopírujte akékoľvek pole

Posuňte sa na **App Details**. Uvidíte bundle ID, verziu, cenu, veľkosť súboru, minimálny OS, dátum vydania, dátum poslednej aktualizácie, vekové hodnotenie, žánre, ID žánrov, jazyky, predajcu, ID umelca a ID skladby.

Klepnite na tlačidlo **Copy** na akejkoľvek karte. Hodnota sa presunie do schránky a tlačidlo zobrazí zelený «Copied» háčik.

To isté funguje pre **Description**, **What's New** a **Supported Devices**. Tieto sekcie sú posuvné, takže si môžete prečítať celý text bez straty miesta, a tlačidlo Copy vloží celé pole do schránky.

![Zobrazte úplné podrobnosti App Store a skopírujte akékoľvek pole jedným klepnutím](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Krok 4. Zobrazte surovú odpoveď API App Store

Potrebujete presný JSON, ktorý Apple vracia? Posuňte sa na **Raw API Response**. Plné dátové zaťaženie iTunes Search API sa zobrazí v posuvnom prehliadači s tlačidlom **Copy** hore. Jedno klepnutie skopíruje celý JSON objekt.

**iTunes Lookup URL** je zobrazená priamo nad ňou. Vložte ju do Postmana, curl alebo vášho prehliadača a prehrajte rovnakú požiadavku.

![Zobrazte a skopírujte surovú JSON odpoveď iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Krok 5. Zmeňte krajinu a zobrazte lokalizovanú verziu

Metadáta App Store sa menia podľa krajiny. Rovnaká aplikácia má často iný názov, podtitul, popis, snímky obrazovky a cenu na každom trhu.

Vyberte krajinu z rozbaľovacieho menu hore. URL vo vstupnom poli sa automaticky aktualizuje. Kliknite znovu na **Lookup** a aplikácia sa znovu načíta na tomto trhu.

Toto je najrýchlejší spôsob, ako skontrolovať, ako konkurent prezentuje svoju aplikáciu v Japonsku, Nemecku, Brazílii alebo v ktorejkoľvek z viac ako 40 podporovaných krajín.

![Prepnite krajiny obchodov a zobrazte lokalizované metadáta App Store](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Krok 6. Skopírujte lokalizované metadáta

Akonáhle sa výsledok krajiny načíta, každé pole funguje rovnako. Klepnite na **Copy** v popise, novinkách, názve aplikácie, vývojárovi, bundle ID alebo na akejkoľvek karte podrobností pre získanie lokalizovaného textu.

To uľahčuje vytváranie porovnávacích tabuliek vedľa seba alebo odovzdávanie lokalizovaného textu na prekladovú kontrolu.

![Skopírujte lokalizovaný popis a metadáta App Store jedným klepnutím](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Kto používa AppLookup.pro

- **Nezávislí vývojári** vykonávajúci ASO analýzu pred spustením.
- **Tímy ASO a marketingu** sledujúce aktualizácie a ceny konkurencie.
- **Dizajnéri**, ktorí získavajú oficiálnu ikonu aplikácie vo vysokom rozlíšení a snímky obrazovky pre tlačové sady a prípadové štúdie.
- **Lokalizačné tímy** auditujúce, ktoré trhy sú pokryté a kde je stále dodávaný východiskový anglický text.
- **Backend a QA inžinieri** testujúci integrácie iTunes Search API bez písania scraperu.
- **Autori a blogeri**, ktorí potrebujú oficiálnu ikonu aplikácie a niekoľko snímok obrazovky pre príspevok.

## Súkromie a vyhlásenie

AppLookup.pro beží vo vašom prehliadači. Nie je tu žiadne prihlásenie. Nie je tu žiadne sledovanie. Nie je tu žiadne serverové logovanie aplikácií, ktoré vyhľadávate. Požiadavky idú priamo z vášho prehliadača do [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) od Apple.

Tento nástroj slúži iba na **vzdelávacie a výskumné účely**. Všetky dáta sú získavané z oficiálneho verejného API Apple a zostávajú vlastníctvom Apple Inc. a uvedených vydavateľov aplikácií. Použitie nástroja podlieha [Apple Media Services Terms and Conditions](https://www.apple.com/legal/internet-services/terms/site.html). Rešpektujte prosím limity rýchlosti Apple a nezdieľajte materiály chránené autorskými právami.

## Vyskúšajte teraz

Nepotrebujete kľúč API, vývojársky účet ani platený plán na preskúmanie dát App Store. Otvorte [applookup.pro](https://applookup.pro), vložte akúkoľvek URL App Store a budete mať metadáta, ikony a surový JSON za pár sekúnd.

## Open Source

AppLookup.pro je open source. Hlásenia chýb, pridávanie krajín a pull requesty sú vítané.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro na GitHube" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Často kladené otázky

{{% details title="Je AppLookup.pro naozaj zdarma?" closed="true" %}}
Áno. AppLookup.pro je 100 percent zdarma a open source. Beží vo vašom prehliadači. Nie je tu registrácia, platená úroveň ani limit používania nad rámec vlastných limitov iTunes Search API od Apple.
{{% /details %}}

{{% details title="Odkiaľ pochádzajú dáta?" closed="true" %}}
Každý výsledok je získavaný v reálnom čase z oficiálneho [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) od Apple. Nástroj nescrapuje stránky App Store a neukladá odpovede do vyrovnávacej pamäte na žiadnom serveri.
{{% /details %}}

{{% details title="Môžem stiahnuť ikonu aplikácie vo vysokom rozlíšení?" closed="true" %}}
Áno. Sekcia **App Icon** zobrazuje každú URL ikony, ktorú Apple vracia. Každá karta má Direct Link a tlačidlo Download a tlačidlo Download All Icons ZIP ich zabalí do jedného archívu.
{{% /details %}}

{{% details title="Môžem stiahnuť všetky snímky obrazovky App Store naraz?" closed="true" %}}
Áno. Každá sekcia snímok obrazovky (iPhone, iPad, macOS a Apple TV) má tlačidlo **Download All (ZIP)**, ktoré spojí každú snímku obrazovky v plnom rozlíšení.
{{% /details %}}

{{% details title="Ako vidím, ako aplikácia vyzerá v inej krajine?" closed="true" %}}
Vyberte krajinu v rozbaľovacom menu v hornej časti stránky. Je podporovaných viac ako 40 obchodov. Kliknite znovu na **Lookup** a nástroj znovu načíta aplikáciu pre túto krajinu, zobrazí lokalizovaný názov, popis, snímky obrazovky, novinky a cenu.
{{% /details %}}

{{% details title="Môžem kopírovať jednotlivé polia, ako je bundle ID alebo dátum vydania?" closed="true" %}}
Áno. Každé textové pole vo výsledku má vlastné tlačidlo Copy: názov aplikácie, vývojár, popis, novinky, bundle ID, verzia, cena, veľkosť súboru, minimálny OS, dátum vydania, vekové hodnotenie, jazyky, podporované zariadenia a surový JSON.
{{% /details %}}

{{% details title="Funguje AppLookup.pro pre akúkoľvek iOS aplikáciu?" closed="true" %}}
Funguje pre akúkoľvek aplikáciu, ktorá je verejne uvedená aspoň v jednej krajine App Store a vrátená iTunes Search API. Nezaradené, odstránené alebo podnikovo distribuované aplikácie sa nezobrazia.
{{% /details %}}

{{% details title="Podporuje aplikácie macOS a Apple TV?" closed="true" %}}
Áno. Ak má aplikácia snímky obrazovky macOS alebo Apple TV v odpovedi iTunes Search API, AppLookup.pro ich zobrazí vo vlastnom posuvnom paneli s tlačidlami na sťahovanie.
{{% /details %}}

{{% details title="Môžem použiť surový JSON vo vlastnom kóde?" closed="true" %}}
Áno. Sekcia Raw API Response zobrazuje presný JSON, ktorý Apple vracia. Skopírujte ho do Postmana, jednotkového testu alebo backend pipeline. Rešpektujte prosím podmienky API Apple a rozumné limity rýchlosti.
{{% /details %}}

{{% details title="Je bezpečné vkladať URL App Store do nástroja?" closed="true" %}}
Áno. URL je analyzovaná vo vašom prehliadači. Jediné odchádzajúce sieťové volanie je vyhľadávanie v iTunes Search API od Apple.
{{% /details %}}

{{% details title="Aký je rozdiel medzi AppLookup.pro a AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) slúži na čítanie metadát App Store z akejkoľvek zverejnenej aplikácie: analýza konkurencie, sťahovanie materiálov, kontroly lokalizácie. [AppKeywords.pro](https://appkeywords.pro) slúži na písanie metadát App Store pre vašu vlastnú aplikáciu: optimalizácia názvu, podtitulu a kľúčových slov s podporou Fastlane. Tieto dva nástroje spolu dobre fungujú.
{{% /details %}}
