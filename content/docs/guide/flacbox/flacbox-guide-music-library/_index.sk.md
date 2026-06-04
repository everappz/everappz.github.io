---
title: "Hudobná knižnica"
date: 2020-02-01
description: "Naučte sa, ako budovať, organizovať a synchronizovať hudobnú knižnicu vo Flacbox na iPhone, iPad a Mac. Pridávajte skladby manuálne alebo synchronizujte z cloudových služieb, spravujte metadáta, obaly albumov, prehrávače, obľúbené, nedávne a záložky. Zahŕňa podporu Hi-Res audio, editor tagov MusicBrainz, online a offline synchronizáciu a možnosti personalizácie."
keywords: [
  "Flacbox hudobná knižnica", "synchronizácia hudby z cloudu", "organizácia hudobných metadát",
  "úprava audio tagov Flacbox", "offline synchronizácia hudby", "import lokálnej hudby",
  "správa prehrávačov Flacbox", "vyhľadávanie obalov albumov Flacbox",
  "metadáta hudby iPhone", "príručka aplikácie Flacbox",
  "Flacbox MusicBrainz", "Flacbox normalizácia tagov",
  "Flacbox hi-res hudobná knižnica", "Flacbox FFmpeg knižnica",
  "Flacbox sólové albumy", "Flacbox zobrazenie skladateľa"
]
tags: ["hudba", "príručka", "flacbox", "knižnica"]
readingTime: 11
---


Správa hudobnej knižnice je s Flacbox hračka — všetky vaše skladby v lokálnych formátoch FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE a desiatky ďalších formátov môžete bez námahy organizovať do jednej prehľadateľnej zbierky. Na budovanie hudobnej knižnice máte dve možnosti: manuálne pridávanie (sami si vyberáte, čo sa pridá) alebo automatická synchronizácia (Flacbox prehľadáva určené cloudové priečinky a automaticky pridáva nové súbory, keď sa objavia).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — zobrazenie albumov v hudobnej knižnici" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Manuálne pridávanie

Ak chcete manuálne pridávať skladby, klepnite na ikonu **Pridať hudbu** v ľavom hornom rohu a vyberte priečinky alebo súbory z pripojenej cloudovej úložnej služby alebo súbory nachádzajúce sa na zariadení. Keď pridáte skladby do knižnice, vytvárajú sa iba prepojenia na tieto skladby — skutočné súbory zostávajú na pôvodných miestach, aby sa ušetril cenný diskový priestor. Ak chcete mať skladby dostupné offline, môžete použiť akciu Stiahnuť z ponuky možností alebo povoliť Offline režim pre prehrávače a zbierky skladieb.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — pridanie skladieb do hudobnej knižnice" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Na verzii Mac môžete tiež pretiahnuť súbory do knižnice, alebo použiť **Otvoriť súbory…** / **Otvoriť priečinok…** zo systémového výberu súborov na iPhone a iPad.

## Pokračovať v prehrávaní

Obnoví frontu audio prehrávača z poslednej uloženej pozície, ak je táto funkcia povolená v nastaveniach aplikácie. Pre najlepší zážitok povolte **Uložiť stav audio prehrávača** aj **Uložiť pozíciu prehrávania** v Nastavenia → Audio prehrávač → Všeobecné. Po povolení sa tlačidlo **Pokračovať v prehrávaní** zobrazí v hornej časti každého priečinka, albumu, interpreta, žánru a obrazovky prehrávača — klepnutím sa okamžite vrátite na presnú skladbu a pozíciu, kde ste naposledy skončili.

## Umiestnenia

Všetky skladby v knižnici sú premyslene zoskupené podľa typu zdroja a hudobných tagov. Skladby môžete filtrovať podľa umiestnenia pomocou tlačidla **Viac akcií** v pravom hornom rohu a výberom **Filtrovať**.

### Online hudba

Táto sekcia zobrazuje hudbu z vašich pripojených cloudových úložných služieb. Skladby tu sú streamované na požiadanie; nič nezaberá lokálne úložisko, kým ich výslovne nestiahne alebo nepovolíte offline režim.

### Súbory v tejto aplikácii

Tu nájdete hudbu dostupnú na offline prehrávanie pochádzajúcu z lokálnych súborov. Zahŕňa súbory v priečinku Dokumenty aplikácie — všetko, čo ste stiahli, preniesli cez Wi-Fi Drive alebo importovali cez Finder File Sharing.

### Súbory na tomto iPhone / iPad / Mac

Táto kategória zahŕňa hudbu importovanú do aplikácie zo zariadenia, pridanú cez systémový dialóg **Otvoriť súbory…**. Pôvodné súbory zostávajú na pôvodnom mieste; Flacbox si uchováva iba prepojenie na ne.

## Kategórie

Keď pridáte skladby do hudobnej knižnice, aplikácia automaticky načíta ich audio tagy a organizuje ich do kategórií ako Skladby, Neprehrané skladby, Albumy, Albumoví interpreti, Interpreti, Žánre a Skladatelia.

## Zoskupovanie tagov

Tieto kategórie vám pomáhajú organizovať skladby podľa hudobných tagov. Keď pridáte skladby do hudobnej knižnice, aplikácia načíta ich metadáta a zoskupí ich podľa týchto kategórií. Ak nevidíte všetky albumy, uistite sa, že aplikácia prehľadala každú skladbu. Postup skenovania môžete skontrolovať v Nastavenia → Hudobná knižnica → Čítanie metadát → Počet spracovaných súborov v hudobnej knižnici. Pre lokálne súbory môžete tiež znovu skenovať offline priečinky v Nastavenia → Hudobná knižnica → Synchronizácia offline priečinkov → Spustiť skenovanie lokálnych priečinkov. Po dokončení všetkých operácií čítačkou metadát uvidíte v hudobnej knižnici nasledujúce kategórie:

- **Skladby** — všetky skladby zoskupené podľa tagu TRACK_TITLE. Poradie zoradenia môžete skontrolovať pomocou ponuky Viac akcií v pravom hornom rohu.
- **Neprehrané skladby** — všetky skladby, ktoré ešte neboli prehrané.
- **Albumy** — skladby zoskupené podľa tagu ALBUM_NAME, bez ohľadu na tagy interpreta, albumového interpreta a skladateľa. Ak máte viacero albumov s rovnakým názvom, ale rôznymi interpretmi, zvážte použitie zoradenia Exkluzívne albumy popísaného nižšie.
- **Albumoví interpreti** — skladby zoskupené iba podľa tagu ALBUM_ARTIST_TAG. Užitočné na čisté oddelenie kompilácií a spoluprác od sólových diel.
- **Interpreti** — skladby zoskupené iba podľa tagu ARTIST_TAG.
- **Žánre** — skladby zoskupené podľa tagu GENRE.
- **Skladatelia** — skladby zoskupené podľa tagu COMPOSER — neoceniteľné pre knižnice klasickej hudby, kde je „skladateľ" primárnou navigačnou osou.

## Obľúbené

Skladby môžete označiť ako obľúbené na obrazovke audio prehrávača alebo pomocou ponuky možností. Obľúbené sa zobrazujú vo vlastnej sekcii, takže ich nájdete jedným klepnutím.

## Nedávne

Táto sekcia zobrazuje všetky nedávno prehrané skladby. Môžete si prispôsobiť, koľko položiek zoznam Nedávne uchováva, v Nastavenia → Knižnica → Nedávne → Zmeniť veľkosť zoznamu, a exportovať zoznam do M3U / CSV / TXT na zálohovanie histórie počúvania.

## Záložky

Počas prehrávania skladby môžete vytvárať audio záložky a spravovať ich na tejto obrazovke — ideálne pre audioknihy, dlhé mixy, prednášky alebo jednoducho označenie refrénov obľúbených skladieb. Podrobné pokyny na prácu s audio záložkami sú dostupné [tu](/docs/guide/evermusic/evermusic-guide-music-library).

## Horná lišta nástrojov

Nachádza sa tesne pod navigačnou lištou a ponúka niekoľko pohodlných akcií: Hľadať, Prehrať všetko, Zamiešať všetko a Pokračovať v prehrávaní. Túto lištu môžete zobraziť alebo skryť jednoduchým potiahnutím nadol.

## Vyhľadávanie

Funkcia vyhľadávania vám umožňuje nájsť konkrétnu skladbu, interpreta, album alebo žáner v hudobnej knižnici. Na obrazovke Hľadať máte prístup k akciám Zoradiť, Filtrovať a zobrazeniu Mriežka / Zoznam. Vyhľadávanie prebieha lokálne v databáze hudobnej knižnice, takže funguje plne offline a vracia výsledky pri písaní.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — vyhľadávanie v hudobnej knižnici" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Ponuka možností

Každá skladba v hudobnej knižnici má ponuku s ďalšími akciami, dostupnú klepnutím na tlačidlo s tromi bodkami pri názve skladby. Tieto akcie sa líšia v závislosti od toho, či ide o jednotlivú skladbu alebo časť zbierky.

### Pre jednotlivé skladby

- **Prehrať ďalej** — pridá skladbu na začiatok fronty prehrávača.
- **Prehrať neskôr** — pridá skladbu na koniec fronty prehrávača.
- **Pridať do prehrávača** — pridá skladbu do prehrávača.
- **Pridať k obľúbeným** — označí skladbu ako obľúbenú pre rýchly prístup.
- **Stiahnuť** — uloží skladbu do lokálnych súborov. Zobrazí sa na karte **Lokálne súbory** a v sekcii **Offline hudba**.
- **Upraviť audio tagy** — otvorí zabudovaný editor audio tagov na opravu chýbajúcich metadát; upozorňujeme, že tým zmeníte skladbu v úložisku.
- **Zobraziť v priečinku** — odhalí priečinok, kde je uložený zvukový súbor.
- **Zobraziť vo Finderi** — pre súbory importované z Mac táto akcia odhalí priečinok, kde sa nachádza zvukový súbor na Mac.
- **Otvoriť v** — exportuje zvukový súbor do inej aplikácie.
- **Vymazať z cloudovej služby** — odstráni súbor z hudobnej knižnice aj cloudového úložiska. **Táto akcia je nezvratná.**
- **Vymazať z hudobnej knižnice** — vymaže skladbu z hudobnej knižnice, ale súbor zostáva v úložisku. Ak je povolená automatická synchronizácia a súbor existuje na vzdialenom úložisku, znovu sa objaví v knižnici po operácii synchronizácie.

### Pre zbierky skladieb

Pre zbierky skladieb ako Albumy, Interpreti, Žánre alebo Skladatelia ponuka možností obsahuje nasledujúce akcie.

- **Prehrať všetko** — nahradí frontu prehrávača skladbami z vybranej zbierky.
- **Prehrať ďalej** — pridá skladby z tejto zbierky na začiatok fronty prehrávača.
- **Prehrať neskôr** — pridá skladby z tejto zbierky na koniec fronty prehrávača.
- **Pridať do prehrávača** — zaradí skladby z tejto zbierky do prehrávača, s možnosťou vytvorenia nového.
- **Povoliť offline režim** — stiahne skladby z tejto zbierky do lokálnych súborov. Súbory sa zobrazia na karte **Lokálne súbory** a v sekcii **Offline hudba**. Ak sa na server pridajú nové položky zbierky, automaticky sa stiahnu.
- **Upraviť obrázok** — zmení obal albumu pre zbierku skladieb.
- **Pridať do archívu** — zabalí celú zbierku do jedného ZIP súboru pre jednoduchú zálohu alebo prenos (funkcia Premium).
- **Exportovať zoznam skladieb** — exportuje zbierku do M3U, CSV alebo TXT na použitie v iných prehrávačoch alebo na archiváciu.
- **Vymazať z hudobnej knižnice** — odstráni zbierku skladieb z hudobnej knižnice. Táto akcia neodstráni skutočné súbory z úložiska. Ak je povolená automatická synchronizácia a súbory existujú na vzdialenom úložisku, znovu sa objavia v knižnici po operácii synchronizácie.

## Režim výberu

Režim výberu môžete aktivovať pomocou tlačidla Viac akcií v pravom hornom rohu. V tomto režime môžete vybrať viacero skladieb naraz a vykonávať hromadné akcie — pridať do prehrávača, označiť ako obľúbené, vymazať z knižnice, stiahnuť a ďalšie.

## Detail albumu

Keď otvoríte sekcie Interpret, Albumový interpret alebo Skladateľ, zobrazí sa prepínač pre Skladby / Všetky albumy / Exkluzívne albumy / Sólové albumy.

- **Skladby** — zobrazuje všetky skladby, kde sa tento Interpret / Albumový interpret / Skladateľ objavuje v audio tagoch.
- **Všetky albumy** — zobrazuje kompilačné albumy a všetky albumy, kde je interpret vôbec prítomný.
- **Exkluzívne albumy** — zobrazuje albumy, kde je zadaný interpret jediným interpretom s týmto názvom albumu.
- **Sólové albumy** — zobrazuje albumy, kde sa objavujú iba skladby zadaného interpreta, aj keď iní interpreti majú albumy s rovnakým názvom.

Je to obzvlášť užitočné na čistenie zanedbaných kompilácií „Rôzni interpreti" vo veľkých knižniciach.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — obrazovka detailu albumu" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Nastavenia

Klepnite na Viac akcií → Nastavenia a nakonfigurujte predvoľby hudobnej knižnice.

### Čítanie metadát

Keď pridáte skladby do knižnice, čítačka metadát sa pustí do práce. Tento proces na pozadí načíta všetky metadáta zo skladieb a organizuje ich podľa Interpreta, Albumu, Žánru a Skladateľa. Rýchlosť čítania metadát môžete upraviť, aby sa údaje načítavali rýchlejšie — uvedomte si, že rýchlejšie čítanie spotrebúva viac energie. Čítačku metadát môžete tiež úplne vypnúť a namiesto informácií z tagov zobrazovať názvy súborov.

Dôležité je, že čítačka metadát iba aktualizuje metadáta v hudobnej knižnici a nemení súbory uložené v cloudovom účte alebo lokálnom úložisku. Ak chcete upravovať metadáta pre zvukové súbory, môžete to urobiť pomocou zabudovaného editora tagov, ktorý aktivujete z príslušnej akcie v ponuke možností.

### Dostupné režimy čítačky metadát

- **Deaktivovaná** — čítačka metadát je vypnutá a namiesto dát audio tagov sa zobrazujú názvy súborov.
- **Aktuálna skladba** — aplikácia číta metadáta iba pre aktuálne prehrávanú skladbu. Použite túto možnosť pri pomalej sieti, aby ste zabránili čítačke metadát posielať veľa požiadaviek na cloudový server, čo môže spôsobiť prerušenia prehrávania.
- **Fronta prehrávania** — aplikácia číta metadáta pre všetky skladby vo fronte audio prehrávača.
- **Knižnica** — aplikácia číta metadáta pre všetky skladby v hudobnej knižnici.

Keď je zapnutý prepínač **Čítanie metadát na pozadí**, čítačka metadát pokračuje v práci v režime na pozadí. Upozorňujeme, že ak aplikácia spotrebúva veľa energie počas prehrávania zvuku, operačný systém iOS ju môže pozastaviť.

Preto, ak máte veľkú hudobnú zbierku, odporúča sa používať desktopovú verziu aplikácie na synchronizáciu metadát. Potom môžete pomocou funkcie Zálohovanie a obnovenie dát v nastaveniach aplikácie preniesť synchronizovanú knižnicu z desktopovej verzie na mobilnú.

Keď je povolená možnosť **Normalizovať kódovanie metadát**, aplikácia automaticky normalizuje kódovanie metadát pre všetky skladby v hudobnej knižnici. Opravuje problémy s poškodeným kódovaním audio tagov (napríklad po úprave súborov na Windows PC) a zabraňuje zobrazovaniu nesprávnych znakov v informáciách o skladbe.

Akcia **Načítať metadata** označí každý súbor v hudobnej knižnici ako majúci chýbajúce metadáta, čím spustí čítačku metadát, aby obnovila každý záznam.

Klepnutím na **Spustiť čítanie metadát** spustíte čítačku manuálne. Postup operácie sa zobrazuje nižšie.

### Online synchronizácia

Automatická online synchronizácia hudby umožňuje automaticky pridávať skladby z pripojených cloudových služieb do hudobnej knižnice. Ak chcete túto funkciu aktivovať, prejdite do Nastavení hudobnej knižnice a vyberte priečinky synchronizácie.

Po povolení tejto možnosti aplikácia prehľadá všetky vybrané priečinky, identifikuje podporované zvukové súbory a bezproblémovo ich integruje do knižnice. Synchronizáciu môžete spustiť alebo zastaviť klepnutím na príslušnú akciu v ponuke.

Online synchronizácia hudby prebieha výlučne vtedy, keď je aplikácia v popredí, čo znamená, že synchronizácia veľkej knižnice môže chvíľu trvať. Aby ste urýchlili proces, nechajte aplikáciu otvorenú, pripojte ju k zdroju napájania a povoľte Obrazovka → Vždy aktívna v nastaveniach aplikácie.

Prípadne môžete vykonať online synchronizáciu hudby v desktopovej verzii aplikácie a preniesť hudobnú knižnicu do iOS verzie pomocou funkcie Zálohovanie a obnovenie.

Môžete tiež nastaviť, ako často chcete synchronizovať online hudobnú knižnicu. Ak nastavíte interval na Okamžite, online synchronizácia sa spustí vždy, keď otvoríte aplikáciu.

### Offline synchronizácia

Tu môžete konfigurovať offline synchronizáciu hudby.

#### Synchronizované offline priečinky

Keď sprístupníte cloudový priečinok offline (cez ponuku Viac akcií), zobrazí sa v sekcii Lokálne súbory → Offline priečinky. Aplikácia stiahne jeho obsah do zariadenia. Ak vykonáte zmeny v priečinku v cloude — napríklad pridaním, odstránením alebo aktualizáciou súborov — aplikácia tieto zmeny zistí a automaticky aktualizuje lokálnu kópiu.

Na tejto obrazovke môžete manuálne spustiť synchronizáciu offline priečinka, zobraziť offline priečinok v nadradenom priečinku a zakázať offline režim pre priečinok. Zakázanie offline režimu odstráni všetky lokálne kópie súborov zo zariadenia.

#### Časový interval

Môžete nastaviť časový interval, ako často má aplikácia kontrolovať zmeny offline priečinkov.

#### Spustiť skenovanie lokálnych priečinkov

Táto možnosť prehľadá všetky lokálne priečinky nachádzajúce sa v priečinku Dokumenty aplikácie na podporované zvukové súbory. Všetky tieto lokálne súbory sa bezproblémovo pridajú do hudobnej knižnice. Lokálne súbory nachádzajúce sa na zariadení, ale mimo tejto aplikácie, musia byť do hudobnej knižnice pridané manuálne, pretože aplikácia nemá prístup k súborom mimo priečinka Dokumenty aplikácie z dôvodu bezpečnostných obmedzení iOS / macOS.

#### Dôležité

Odporúča sa pravidelne spúšťať offline synchronizáciu hudby, aby bola hudobná knižnica aktualizovaná lokálnymi súbormi.

### Personalizácia

V tejto sekcii môžete konfigurovať štýl obrazovky hudobnej knižnice podľa svojich preferencií. Sú k dispozícii tri možnosti: Jednoduchá ponuka, Zoskupená ponuka, Záložková ponuka. Môžete tiež povoliť alebo zakázať zobrazenie obalov albumov na obrazovkách detailov albumu.

### Obaly albumov

Tu môžete konfigurovať, ako aplikácia načítava a ukladá obaly albumov.

- **Typ siete** — vyberte Wi-Fi alebo Wi-Fi a mobilné dáta na sťahovanie obalov.
- **Načítať obaly albumov pre online súbory** — ak je povolené, vložené obaly albumov sa načítajú pre súbory uložené v cloudovom úložisku. Môže to spotrebovať dodatočné sieťové dáta.
- **Hľadať v priečinku** — ak je povolené a skladba nemá vložený obal, aplikácia hľadá obrázky JPEG alebo PNG v rovnakom priečinku a používa ich ako obal albumu.
- **Kvalita obalu** — vyberte kvalitu obalov albumov uložených na zariadení.
- **Zobraziť v priečinku** — otvorí priečinok, kde sú uložené obaly albumov v pamäti cache, aby ste ich mohli spravovať alebo zálohovať.
- **Vymazať všetky** — vymaže obaly albumov uložené v pamäti cache, aby sa uvoľnil úložný priestor a vynútilo načítanie na požiadanie.

Predvolene aplikácia kontroluje vložené obaly albumov v skladbách a zobrazuje ich, ak sú k dispozícii. Ak neexistujú žiadne vložené obaly albumov a možnosť **Hľadať v priečinku** je povolená, aplikácia skontroluje nadradený priečinok na obrázky JPEG alebo PNG a použije ich ako obal albumu pre všetky skladby v danom priečinku.

### Prehrávače

Môžete povoliť možnosť pridania tej istej skladby do prehrávača dvakrát. Predvolene je táto možnosť zakázaná.

### Nedávne

Môžete spravovať zoznam nedávno prehraných skladieb.

- **Vymazať zoznam** — vymaže celý zoznam nedávno prehraných skladieb.
- **Zmeniť veľkosť zoznamu** — nastaví počet položiek, ktoré sa zobrazia v zozname.
- **Exportovať zoznam skladieb** — exportuje zoznam nedávno prehraných skladieb do M3U, CSV alebo TXT. Podrobné pokyny sú dostupné [tu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Obľúbené

Môžete spravovať zoznam obľúbených skladieb.

- **Simultánna úprava** — ak je povolená, pridanie skladby k obľúbeným ju pridá súčasne do hudobnej knižnice aj do sekcie súborov.
- **Vymazať zoznam** — vymaže celý zoznam obľúbených skladieb.
- **Exportovať zoznam skladieb** — podobne ako Nedávne, exportuje zoznam obľúbených do M3U, CSV alebo TXT.

### Vymazať knižnicu

Táto akcia vymaže databázu hudobnej knižnice, ale hudobné súbory v úložisku zostanú nedotknuté.

### Limit načítania obsahu

Predvolene aplikácia používa stránkovanie na skrátenie času načítania obsahu a udržanie veľkých knižníc responzívnych. Túto možnosť však môžete vypnúť a umožniť aplikácii načítať všetky dostupné dáta naraz. Ak to chcete urobiť, otvorte nastavenia aplikácie, posuňte nadol na Personalizácia → Limit načítania obsahu a vyberte Deaktivovaný.
