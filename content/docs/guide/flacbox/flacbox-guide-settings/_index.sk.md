---
title: "Nastavenia"
date: 2020-02-01
description: "Preskúmajte každé nastavenie vo Flacbox — od predvolieb prehrávania, FFmpeg / systémového audio engine, Hi-Res audio výstupu, doladenia ekvalizéra, korekcie výšky tónu, trvania IO bufferu, synchronizácie metadát, správy prehrávačov, prenosu súborov, widgetov domovskej obrazovky, Apple CarPlay, personalizácie používateľského rozhrania, jazyka, prístupového kódu, zálohovania a obnovy a upgradu na Premium."
keywords: [
  "nastavenia Flacbox", "konfigurácia audio prehrávača", "upgrade premium Flacbox",
  "WiFi Drive", "synchronizácia metadát", "ekvalizér", "rýchlosť prehrávania",
  "duplicity v prehrávači", "nastavenia správcu súborov", "synchronizácia offline hudby",
  "editor audio tagov", "tmavý režim", "obnovenie nákupov", "zálohovanie nastavení",
  "nastavenia widgetov Flacbox", "nastavenia CarPlay Flacbox",
  "nastavenia FFmpeg Flacbox", "nastavenia vzorkovacej frekvencie Flacbox",
  "nastavenia korekcie výšky tónu Flacbox", "IO buffer Flacbox",
  "prístupový kód Flacbox", "jazyk Flacbox", "personalizácia Flacbox",
  "analytika Flacbox"
]
tags: ["príručka", "flacbox", "nastavenia"]
readingTime: 16
---


Obrazovka Nastavenia je riadiace centrum Flacbox. Odtiaľto môžete upgradovať na Premium, konfigurovať audio engine (systémové kodeky alebo FFmpeg), spravovať hudobnú knižnicu, nastaviť správcu súborov, prispôsobiť editor audio tagov, povoliť widgety domovskej obrazovky a Apple CarPlay, zálohovať dáta a pristupovať k pomoci a právnym informáciám. Sekcie sú zoskupené pod hlavičkami: Nákupy a aktualizácie, Predvoľby aplikácie, Pomoc a Právne informácie a súkromie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — hlavná obrazovka Nastavenia" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Upgrade na Premium

Upgradujte aplikáciu na verziu Premium a odstráňte všetky obmedzenia. Bezplatná verzia aplikácie ponúka jednorazový doživotný nákup v aplikácii a dve možnosti predplatného (1 mesiac a 1 rok) na odstránenie všetkých obmedzení a upgrade na Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — upgrade na Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Family Sharing** je povolený pre všetky nákupy a plány, takže môžete zdieľať verziu Premium s až piatimi členmi rodiny bez ďalších nákladov.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — výber Premium plánu" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Viac o nákupoch a verzii Premium si môžete prečítať tu: [Aký je rozdiel medzi Flacbox a Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Zdieľanie nákupov medzi iOS a Mac

Doživotné nákupy a predplatné sú zdieľané medzi iOS a Mac pomocou iCloud na synchronizáciu týchto informácií. Ak máte verziu Premium na iOS zariadení, uistite sa, že máte nainštalovanú najnovšiu verziu a že iCloud je povolený. Spustite aplikáciu na iOS a počkajte minútu, kým sa informácie o nákupe nahrají na iCloud.

Môžete tiež skúsiť klepnúť na tlačidlo Obnoviť nákupy v nastaveniach aplikácie. Potom nainštalujte najnovšiu verziu aplikácie z App Store na Mac a spustite aplikáciu. Uistite sa, že máte internetové pripojenie a že na Mac používate rovnaký iCloud a App Store účet ako na iOS. Počkajte minútu, kým aplikácia stiahne informácie o nákupe z iCloud — verzia Premium by sa mala na Mac automaticky aktivovať.

## Obnovenie nákupov na novom zariadení

Ak chcete obnoviť nákup na novom zariadení, použite ponuku Nákupy → Obnoviť nákupy. Zobrazí sa zoznam vašich nákupov. Ak nevidíte všetky nákupy, potvrďte, že zariadenie je pripojené k rovnakému Apple ID, ktoré bolo použité na nákupy, a uistite sa, že iCloud je povolený.

## Vyskúšajte Premium zadarmo

Pomocou tejto ponuky môžete upgradovať na verziu Premium zadarmo na obmedzený čas. Stačí sledovať reklamu alebo povedať priateľom o aplikácii a získajte Premium zadarmo.

## Nákupy

Z tejto ponuky môžete obnoviť predchádzajúce nákupy. Ak narazíte na chyby aktivácie, skúste povoliť možnosť Obnoviť nákupy pri spustení aplikácie.

## Aktualizácia softvéru

Klepnutím na Aktualizácia softvéru skontrolujte, či je k dispozícii novšia verzia Flacbox. Aplikácia porovná vašu nainštalovanú verziu s najnovšou verziou v App Store a upozorní vás, ak sa odporúča aktualizácia.

## Čo je nové

Táto ponuka je k dispozícii po vydaní novej verzie. Zobrazuje súhrn zmien a nových funkcií v najnovšej aktualizácii.

## Audio prehrávač

Táto sekcia konfiguruje audio prehrávač a základný audio engine vrátane možnosti FFmpeg / systémový kodek a možností Hi-Res audio výstupu.

### Všeobecné

Tieto nastavenia pokrývajú základné aspekty audio prehrávača — frontu prehrávania, audio výstup a uloženie stavu prehrávača.

- **Režim opakovania** — vyberte, ako sa audio prehrávač správa, keď sa skončí skladba:
  - **Opakovať všetko** — znova prehrá všetky skladby vo fronte.
  - **Opakovať jednu** — opakuje iba aktuálnu skladbu.
  - **Zastaviť opakovanie** — pozastaví prehrávanie, keď sa skončí aktuálna skladba.
  - **Neopakovať** — umožňuje prehrávacej fronte prehrávať bez opakovania.
- **Režim zamiešania** — náhodne upraví poradie skladieb vo fronte. Môžete ho **Vypnúť** alebo **Zapnúť**.
- **Audio kodek** — vyberte audio engine použitý na prehrávanie:
  - **Systémový kodek + FFmpeg** — uprednostňuje systémový audio kodek tam, kde je to možné, čím zvyšuje kompatibilitu a stabilitu. Korekcia výšky tónu a vzorkovacia frekvencia audio výstupu môžu byť obmedzené.
  - **FFmpeg** — vynúti kodek FFmpeg pre všetky zvukové súbory, odomknutie korekcie výšky tónu a vzorkovacej frekvencie audio výstupu.
- **Vzorkovacia frekvencia audio výstupu** — nastavte vzorkovaciu frekvenciu audio výstupu na optimalizáciu kvality zvuku, obzvlášť užitočné s externým DAC. Dostupné hodnoty: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** a **96 kHz**.
- **Počet kanálov audio výstupu** — pre viackanálové audio systémy s externým DAC zadajte počet kanálov: Mono, Stereo, Stred / Ľavý / Pravý, Stred / Ľavý / Pravý / Surround, ITU BS.775-1, 5.1 Surround a SDDS.
- **Preferované trvanie IO bufferu audio výstupu** — nakonfigurujte trvanie vstupného / výstupného bufferu. Typická hodnota na minimalizáciu latencie pri prehrávaní vysoko rozlišovacieho zvuku je okolo **5 milisekúnd (0,005 sekúnd)**. Otestujte rôzne hodnoty trvania na cieľovom zariadení, aby ste našli najlepšiu rovnováhu medzi nízkou latenciou a prehrávaním bez výpadkov.
- **Režim audio výstupu (len iOS)** — nakonfigurujte zmiešaný audio výstup tak, aby sa zvuk z Flacbox miešal s inými aplikáciami. Podrobné pokyny sú [tu](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Uložiť pozíciu prehrávania** — ukladá a obnovuje pozíciu prehrávania pre skladby v hudobnej knižnici.
- **Uložiť stav audio prehrávača** — uchová stav audio prehrávača pred zatvorením aplikácie, čo uľahčuje pokračovanie tam, kde ste skončili.

Po povolení oboch nastavení **Uložiť pozíciu prehrávania** a **Uložiť stav audio prehrávača** otvorte ľubovoľný priečinok, album, interpreta alebo žáner a uvidíte tlačidlo **Pokračovať v prehrávaní** v hornej časti obrazovky.

### Personalizácia

Personalizácia vám umožňuje prispôsobiť vzhľad obrazovky audio prehrávača, zmeniť dostupné ovládacie prvky na hlavnej obrazovke, zamknutej obrazovke a stavovom riadku a konfigurovať ovládacie prvky preskočenia.

- **Štýl obrazovky audio prehrávača** — nakonfigurujte rozmiestnenie prvkov na obrazovke audio prehrávača.
- **Štýl posúvania obalov albumov** — nakonfigurujte preferovaný štýl posúvania pre obaly albumov.
- **Ďalšie prvky** — povoľte extra prvky na obrazovke audio prehrávača. Informácie o audio formáte zobrazujú audio informácie aktuálne prehrávanej skladby nad obalon; Posúvač hlasitosti zvuku zobrazuje posúvač audio výstupu pod ovládacími prvkami prehrávania.
- **Akcie hlavnej obrazovky** — nakonfigurujte, ktoré tlačidlá by mali byť predvolene viditeľné na hlavnej obrazovke audio prehrávača: Opakovanie a zamiešanie, Ďalšia a predchádzajúca skladba, Preskočiť čas, Časovač spánku, Google Chromecast, AirPlay a Bluetooth, Audio ekvalizér, Hľadať, Záložky, Rýchlosť, Pridať záložku, Pridať k obľúbeným, Komentáre a ďalšie.
- **Ovládacie prvky prehrávania na zamknutej obrazovke** — vyberte, ktoré ovládacie prvky sa zobrazujú na zamknutej obrazovke. Možné hodnoty: Preskočiť čas, Pridať záložku, Pridať k obľúbeným.
- **Tlačidlá preskočenia** — vyberte časový interval pre tlačidlá Preskočiť čas.

### Načítanie súborov

Počas načítania súborov môžete zmeniť typ siete použitý na načítanie skladieb. Dostupné možnosti: **Wi-Fi**, **Wi-Fi a mobilné dáta**.

- **Čas prednahrávania** — nastavte časový interval bufferingu. Zvýšte ho, ak máte slabé sieťové pripojenie.
- **Použiť priamu URL** — ak je povolené, na načítanie skladby sa použije priama URL, ak to server podporuje. Môže to urýchliť načítanie skladby, ale môže to ovplyvniť stabilitu prehrávania.

### Audio ekvalizér

Nakonfigurujte 10-pásmový audio ekvalizér, predvoľby a preamplifik átor. O konfigurácii audio ekvalizéra si môžete prečítať viac [tu](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Rýchlosť prehrávania

Nastavte rýchlosť prehrávania audio prehrávača od **0,02× do 3,00×**. Klepnutím na ikonu konfigurácie v pravom hornom rohu prepnete do **presného režimu** pre jemnejšie nastavenia.

### Korekcia výšky tónu

Zmeňte nastavenia korekcie výšky tónu pomocou preddefinovaných hodnôt, alebo prepnite do **presného režimu** klepnutím na tlačidlo v pravom hornom rohu. Korekcia výšky tónu je k dispozícii v ceste kodeku FFmpeg s rozsahom od **-1000 do +1000**.

### Pamäť cache prehrávania

Skladby vo fronte audio prehrávača sa automaticky sťahujú na zabezpečenie plynulého prehrávania. Ak manuálne sťahujete zvukové súbory, môžete to zakázať, aby ste sa vyhli duplicitám. Tu môžete tiež nastaviť veľkosť pamäte cache audio prehrávača.

### Časovač spánku

Aktivujte časovač na automatické zastavenie prehrávania po uplynutí určeného obdobia. Klepnutím na ikonu konfigurácie v pravom hornom rohu aktivujete **presný režim** s granularitou po minútach.

## Knižnica

Tu sa nachádzajú nastavenia hudobnej knižnice — automatická synchronizácia, čítanie metadát, načítanie obalov albumov, prehrávače, nedávne a obľúbené.

### Čítanie metadát

Keď pridáte skladby do knižnice, **čítačka metadát** sa pustí do práce. Tento proces na pozadí načíta všetky metadáta zo skladieb a organizuje ich podľa Interpreta, Albumu, Žánru a Skladateľa. Rýchlosť čítania metadát môžete upraviť, aby sa údaje načítavali rýchlejšie (za cenu väčšej spotreby batérie). Čítačku metadát môžete tiež vypnúť a namiesto informácií z tagov zobrazovať názvy súborov.

Čítačka metadát **iba aktualizuje metadáta v hudobnej knižnici** a nemení súbory uložené v cloudovom účte alebo lokálnom úložisku. Na úpravu metadát v samotných zvukových súboroch použite zabudovaný **editor tagov** cez príslušnú akciu v ponuke možností.

Keď je zapnutý prepínač **Čítanie metadát na pozadí**, čítačka pokračuje v práci v režime na pozadí. Ak aplikácia spotrebúva príliš veľa energie počas prehrávania zvuku, iOS ju môže pozastaviť.

Ak máte veľkú hudobnú zbierku, vykonajte synchronizáciu metadát v desktopovej verzii aplikácie a preneste synchronizovanú hudobnú knižnicu na iOS pomocou **Zálohovanie a obnovenie**.

Keď je povolená možnosť **Normalizovať kódovanie metadát**, aplikácia automaticky normalizuje kódovanie metadát pre všetky skladby. Opravuje poškodené kódovanie tagov (napríklad po úprave súborov na Windows PC) a zabraňuje zobrazovaniu nesprávnych znakov v informáciách o skladbe.

**Načítať metadata** označí každý súbor v hudobnej knižnici ako majúci chýbajúce metadáta, čo spôsobí, že čítačka metadát obnoví každý záznam.

**Spustiť čítanie metadát** spustí čítačku metadát manuálne. Postup sa zobrazuje pod akciou.

### Online synchronizácia

Automatická online synchronizácia hudby pridáva skladby z pripojených cloudových služieb do hudobnej knižnice automaticky. Ak ju chcete povoliť, otvorte nastavenia hudobnej knižnice a vyberte priečinky synchronizácie.

Po povolení tejto možnosti aplikácia prehľadá vybrané priečinky, identifikuje podporované zvukové súbory a pridá ich do knižnice. Synchronizáciu spustíte alebo zastavíte príslušnou akciou v ponuke.

Online synchronizácia prebieha iba vtedy, keď je aplikácia v popredí, takže synchronizácia veľkej knižnice môže chvíľu trvať. Na urýchlenie nechajte Flacbox otvorený, zapojte zariadenie do napájania a povoľte **Nastavenia → Obrazovka → Vždy aktívna**.

Prípadne vykonajte online synchronizáciu v desktopovej verzii aplikácie a preneste výsledok na iOS pomocou **Zálohovanie a obnovenie**.

Môžete tiež zvoliť, ako často sa online synchronizácia spúšťa. Nastavením intervalu na **Okamžite** sa synchronizácia spustí vždy, keď otvoríte aplikáciu.

### Offline synchronizácia

Nakonfigurujte offline synchronizáciu hudby.

#### Synchronizované offline priečinky

Keď označíte online priečinok na cloudovom serveri ako dostupný offline (pomocou ponuky **Viac akcií**), zobrazí sa tu. Obsah priečinka sa stiahne do **Lokálne súbory → Offline priečinky**. Keď sa online priečinok zmení (pridané, odstránené alebo aktualizované súbory), aplikácia skontroluje zmeny a aktualizuje lokálnu kópiu na zariadení.

Na tejto obrazovke môžete manuálne spustiť synchronizáciu offline priečinka, zobraziť offline priečinok v nadradenom priečinku a zakázať offline režim pre priečinok. Zakázanie offline režimu odstráni všetky lokálne kópie súborov zo zariadenia.

#### Časový interval

Vyberte, ako často aplikácia kontroluje zmeny offline priečinkov.

#### Spustiť skenovanie lokálnych priečinkov

Prehľadá všetky lokálne priečinky v priečinku **Dokumenty** aplikácie na podporované zvukové súbory. Nájdené súbory sa automaticky pridajú do hudobnej knižnice. Súbory nachádzajúce sa na zariadení, ale mimo priečinka Dokumenty aplikácie, musia byť do hudobnej knižnice pridané manuálne, pretože aplikácia k nim nemá prístup z dôvodu bezpečnostných obmedzení iOS / macOS.

**Dôležité:** Odporúča sa pravidelne spúšťať offline synchronizáciu hudby, aby bola hudobná knižnica aktualizovaná lokálnymi súbormi.

### Personalizácia

Nakonfigurujte štýl obrazovky hudobnej knižnice. Sú k dispozícii tri možnosti: **Jednoduchá ponuka, Zoskupená ponuka, Záložková ponuka**. Môžete tiež povoliť alebo zakázať obaly albumov na obrazovke detailov albumu.

### Obaly albumov

Nakonfigurujte, ako aplikácia načítava a ukladá obaly albumov.

- **Typ siete** — vyberte **Wi-Fi** alebo **Wi-Fi a mobilné dáta** na sťahovanie obalov.
- **Načítať obaly albumov pre online súbory** — ak je povolené, vložené obaly albumov sa načítajú pre súbory uložené v cloudovom úložisku. Môže to spotrebovať dodatočné sieťové dáta.
- **Hľadať v priečinku** — ak je povolené a skladba nemá vložený obal, aplikácia hľadá obrázky JPEG alebo PNG v rovnakom priečinku a používa ich ako obal albumu.
- **Kvalita obalu** — vyberte kvalitu obalov albumov uložených na zariadení.
- **Zobraziť v priečinku** — otvorí priečinok, kde sú uložené obaly albumov v pamäti cache.
- **Vymazať všetky** — vymaže obaly albumov uložené v pamäti cache, aby sa uvoľnil úložný priestor a vynútilo načítanie na požiadanie.

### Prehrávače

Povoľte možnosť pridania tej istej skladby do prehrávača dvakrát. Predvolene je táto možnosť zakázaná.

### Nedávne

Spravujte zoznam nedávno prehraných skladieb.

- **Vymazať zoznam** — vymaže celý zoznam nedávno prehraných skladieb.
- **Zmeniť veľkosť zoznamu** — nastaví počet položiek, ktoré sa zobrazia v zozname.
- **Exportovať zoznam skladieb** — exportuje zoznam nedávno prehraných skladieb ako M3U, CSV alebo TXT. Podrobné pokyny sú dostupné [tu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Obľúbené

Spravujte zoznam obľúbených skladieb.

- **Simultánna úprava** — ak je povolená, pridanie skladby k obľúbeným ju pridá súčasne do hudobnej knižnice aj do sekcie súborov.
- **Vymazať zoznam** — vymaže celý zoznam obľúbených skladieb.
- **Exportovať zoznam skladieb** — podobne ako Nedávne, exportuje obľúbené ako M3U, CSV alebo TXT.

### Vymazať hudobnú knižnicu

Vymaže databázu hudobnej knižnice. Hudobné súbory v úložisku zostanú nedotknuté.

## Prístupový kód

Aktivujte obrazovku prístupového kódu na ochranu dát aplikácie 4-miestnym číselným prístupovým kódom. Po povolení budete vyzvaní na zadanie prístupového kódu pri každom spustení aplikácie. Kombinujte ho s iOS Face ID / Touch ID na zariadení pre extra ochranu.

## Správca súborov

Sekcia Správca súborov riadi spôsob prenosu, ukladania a náhľadu súborov.

### Prenosy súborov

Vyberte sieťovú predvoľbu pre sťahovanie súborov do zariadenia.

### Maximálny počet paralelných úloh

Nastavte počet paralelných vlákien sťahovania. Vyšší počet urýchľuje sťahovania, ale spotrebúva viac batérie.

### Úlohy prenosu súborov

Zobrazuje aktuálne aktívne úlohy nahrávania a sťahovania.

### Prenosy na pozadí

Povolí sťahovania, keď je aplikácia na pozadí. Ak prenosy na pozadí spotrebúvajú veľa energie, iOS môže aplikáciu pozastaviť.

### Uložiť stiahnuté súbory do

Vyberte predvolený adresár sťahovania alebo nechajte aplikáciu, aby sa vás pýtala zakaždým.

### Synchronizované offline priečinky

Spravujte offline synchronizáciu pre vybrané priečinky. Ak chcete povoliť offline synchronizáciu, klepnite na tlačidlo s tromi bodkami vedľa priečinka a vyberte **Dostupný offline režim**. Nové súbory pridané do cloudového priečinka sa automaticky stiahnu do zariadenia. Prečítajte si viac o offline režimoch [tu](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Časový interval

Vyberte, ako často sa synchronizujú offline priečinky. **Okamžite** spustí synchronizáciu vždy, keď otvoríte aplikáciu.

### Zobraziť úplné názvy súborov

Zobrazuje úplné názvy súborov vrátane prípon v správcovi súborov.

### Upraviť online súbory

Zakázaním online úpravy súborov prepnete do režimu iba na čítanie pre pripojené cloudové služby a zabránite náhodným vymazaniam. Táto akcia odstráni operácie úpravy súborov z používateľského rozhrania.

### Kopírovať súbory pri otváraní

Zadajte, ako aplikácia spracúva importované súbory z iných aplikácií.

### Miniatúry súborov

Spravujte a odstraňujte vygenerované miniatúry súborov na uvoľnenie úložného priestoru.

### Vymazať dočasné súbory

Vyčistite priečinok cache aplikácie a získajte späť úložný priestor.

## Editor audio tagov

Nakonfigurujte zabudovaný editor audio tagov — praktický na hromadné opravenie problémov s interpretom / albumom / rokom / žánrom / obalon naprieč cloudovými a lokálnymi súbormi.

### Škálovanie obalu albumu

Vyberte metódu škálovania použitú pri ukladaní obalu albumu do audio tagov.

### Aktualizovať online súbory

Ak je povolené, aplikácia automaticky aktualizuje metadáta súboru na cloudovom serveri po dokončení úpravy.

### Vymazať súbor po úprave online

Vyberte, či má aplikácia vymazať stiahnutú kópiu po dokončení úpravy online súboru na cloudovom serveri.

### Tlačidlá hlavnej obrazovky

Vyberte, ktoré tlačidlá sú viditeľné na hlavnej obrazovke editora audio tagov.

Pre hlbšie hromadné úpravy naprieč mnohými súbormi naraz nainštalujte našu sprievodnú aplikáciu **Evertag**.

## Widgety

Povolte widgety, aby aplikácia aktualizovala dáta widgetov počas prehrávania. Aktualizácie widgetov vyžadujú dodatočnú energiu, takže prepínač je predvolene vypnutý — povoľte ho iba vtedy, ak skutočne používate widgety na domovskej obrazovke alebo zamknutej obrazovke.

Widgety Flacbox môžete pridať podržaním domovskej obrazovky alebo zamknutej obrazovky, klepnutím na **+**, vyhľadaním **Flacbox** a výberom veľkosti widgetu. Widgety zobrazujú aktuálny obal, názov skladby a interpreta a priamo odkazujú na prehrávač na celú obrazovku. Widgety fungujú aj na macOS v Centre oznámení.

## CarPlay

Zmeňte nastavenia CarPlay tu. Táto ponuka je tiež dostupná v rozhraní CarPlay, takže môžete upraviť zážitok počas jazdy.

### Zoradenie

Nakonfigurujte možnosti zoradenia pre všetky obrazovky CarPlay.

### Limit načítania obsahu

Vyberte, či aplikácia používa stránkovanie na obrazovke CarPlay. Stránkovanie udržuje ponuky responzívne pri veľkých knižniciach.

### Farba gradientu ikon ponuky

Vyberte farebnú schému pre domovskú obrazovku CarPlay.

### Zobraziť obrázky

Zakázaním obrázkov na obrazovke CarPlay optimalizujete rýchlosť načítania a znižujete využitie pamäte pri veľkých knižniciach.

### Pozastaviť prehrávanie pri pripojení

Povolením tejto možnosti sa vyhnete náhlemu hlasitému zvuku pri pripojení zariadenia k CarPlay.

## Wi-Fi Drive

Aktivujte **Wi-Fi Drive** na prenos súborov z počítača do zariadenia pomocou desktopového webového prehliadača, Finderu alebo Prieskumníka súborov. Podrobné pokyny na používanie Wi-Fi Drive sú dostupné [tu](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalizácia

Prispôsobte používateľské rozhranie podľa svojich preferencií.

### Ikona aplikácie

Vyberte alternatívnu ikonu aplikácie pre domovskú obrazovku (Premium).

### Farebná schéma

Vyberte tému používateľského rozhrania a povolte tmavý režim. Keď je vybraté **Predvolené**, aplikácia sleduje celozariadeniové nastavenia vzhľadu.

### Štýl pozadia

Upravte štýl pozadia aplikácie. V súčasnosti je jedinou možnosťou **Rozmazaný obal albumu**, ktorý používa obal aktuálne prehrávanej skladby ako rozmazané pozadie aplikácie.

### Vzhľad položiek v zozname

Doladte, ako sa položky zobrazujú v zoznamoch. Užitočné na malých obrazovkách — môžete nechať aplikáciu automaticky upravovať výšku riadkov na základe obsahu alebo zobrazovať menšie ikony v bunkách zoznamu, aby mal text viac miesta.

### Limit načítania obsahu

Predvolene aplikácia používa stránkovanie na urýchlenie načítania obsahu. Stránkovanie môžete zakázať, aby sa načítalo všetko naraz.

### Štýl obrazovky lokálnych súborov

Zmeňte štýl prezentácie sekcie **Lokálne súbory**.

### Štýl obrazovky hudobnej knižnice

Prispôsobte vzhľad obrazovky **Hudobná knižnica**.

### Štýl obrazovky audio prehrávača

Nakonfigurujte vzhľad obrazovky **Audio prehrávač**.

### Štýl kontextového menu

Vyberte štýl kontextového menu zobrazeného pri klepnutí na tlačidlo **Viac akcií**.

## Okno

Dostupné na Mac a Catalyst. Nakonfigurujte predvoľby týkajúce sa okna, ako je predvolená veľkosť a správanie pri spustení.

## Obrazovka

Vyberte, či má obrazovka zostať aktívna počas používania aplikácie. Užitočné pri skenovaní veľkých knižníc alebo pri dlhých prácach s úpravou tagov.

## Dostupnosť

Aktivujte **Textový režim** na skrytie všetkých obrázkov v používateľskom rozhraní. Textový režim sa automaticky povolí, keď je aktívny VoiceOver, a je tiež užitočný pre veľmi malé nastavenia alebo nastavenia iba s textom.

## Jazyk

Zmeňte jazyk aplikácie a prepíšte systémové predvolené nastavenie. Zmena sa uplatní po úplnom ukončení a opätovnom otvorení Flacbox. V súčasnosti podporované lokalizácie zahŕňajú: afrikánčinu, akan, albánčinu, amharčinu, arabčinu, arménčinu, ásámčinu, aymaru, azerbajdžančinu, bambaru, bengálčinu, baskičtinu, bieloruštinu, bosniačtinu, bulharčinu, barmčinu, katalánčinu, cebuánčinu, čínštinu (zjednodušenú), čínštinu (tradičnú), korzičtinu, chorvátčinu, češtinu, dánčinu, divehi, dogri, holandčinu, angličtinu, esperanto, estónčinu, ewe, filipínčinu, fínčinu, francúzštinu, galícijčinu, gandu, gruzínčinu, nemčinu, gréčtinu, guaraní, gudžarátčinu, haitskú kreolčinu, hauštinu, havajčinu, hebrejčinu, hindčinu, hmong, maďarčinu, islandčinu, igbo, iloko, indonézčinu, írčinu, taliančinu, japončinu, jávčinu, kannadčinu, kazaštinu, khmérčinu, kinyarwandu, kórejčinu, krio, kurdčinu, kurdčinu sorani, kirgizčinu, laošáinu, latinčinu, lotyštinu, lingalu, litovčinu, luxemburčinu, macedónčinu, maithili, malgaštinu, malajčinu, malayálam, maltčinu, maorčinu, maráthčinu, mizo, mongolčinu, nepálčinu, severné soto, nórsku bokmál, nyanja, odiu, oromo, paštčinu, perzštinu, poľštinu, portugalčinu, pandžábčinu, rumunčinu, ruštinu, samojčinu, sanskrit, škótsku gaelčinu, srbčinu, shona, sindhi, sinhalčinu, slovenčinu, slovinčinu, somálčinu, južné soto, španielčinu, sundánčinu, svahilčinu, švédčinu, tadžičtinu, tamilčinu, tatárčinu, telugčinu, thajčinu, tsonga, turečtinu, turkménčinu, ukrajinskú, urdčinu, ujgurčinu, uzbečtinu, vietnamčinu, waleščinu, xhosa, jidiš, jorubčinu, zuluštinu.

## Zálohovanie a obnovenie

Pomocou tejto funkcie zálohujte všetky dáta aplikácie alebo preneste ich na iné zariadenie. Môžete si vybrať, čo zahrnúť:

- **Databáza** — všetky skladby v hudobnej knižnici vrátane prehrávačov. Offline skladby nie sú zahrnuté, aby sa zachovala rozumná veľkosť záložného súboru.
- **Obaly albumov** — všetky uložené obaly albumov v pamäti cache.
- **Nastavenia** — všetky nastavenia aplikácie.

Klepnutím na **Zálohovať dáta aplikácie** spustíte zálohovanie. Dáta aplikácie sa zapíšu do jedného súboru, ktorý môžete neskôr použiť na obnovenie stavu aplikácie na novom zariadení alebo po preinštalovaní aplikácie.

Ak chcete obnoviť dáta aplikácie na novom zariadení, presuňte záložný súbor na nové zariadenie pomocou pripojenej cloudovej služby alebo iCloud a otvorte ho na novom zariadení.

Podrobné pokyny krok za krokom: [Ako preniesť hudobnú knižnicu medzi zariadeniami: sprievodca krok za krokom](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Pomocník

Prístup k príručke aplikácie pre pomoc a návod na efektívne používanie aplikácie.

## Často kladené otázky

Nájdite odpovede na bežné otázky v sekcii FAQ.

## Odoslať spätnú väzbu

Máte spätnú väzbu alebo potrebujete pomoc? Pošlite spätnú väzbu nášmu tímu podpory priamo z aplikácie.

## Zdieľať túto aplikáciu

Zdieľajte aplikáciu s priateľmi a šírte správu.

## Objavte ďalšie aplikácie

Preskúmajte ďalšie aplikácie od Everappz.

## Podmienky a ustanovenia

Načrtáva podmienky a ustanovenia používania aplikácie. Pred použitím aplikácie si ich prečítajte.

## Zásady ochrany súkromia

Navštívte stránku so zásadami ochrany súkromia, aby ste pochopili naše postupy spracovania dát. Pred použitím aplikácie si ich prečítajte.

## Analytika a zber dát

Skontrolujte, ktoré služby sú povolené na analytiku a zber dát, a deaktivujte tie, ktoré nechcete.

## Právne upozornenia

Obsahuje informácie o každej knižnici použitej v aplikácii spolu s číslom verzie aplikácie a informáciami o zostave.
