---
title: "Audio prehrávač"
date: 2020-02-01
description: "Naučte sa, ako používať audio prehrávač Flacbox na iPhone, iPad a Mac. Ovládajte prehrávanie, spravujte fronty, konfigurujte FFmpeg / systémový audio engine, meňte vzorkovaciu frekvenciu, korekciu výšky tónu, trvanie IO bufferu, ekvalizér, audio záložky, AirPlay 2, Google Cast, CarPlay, widgety a klávesové skratky Mac."
keywords: [
  "príručka prehrávača Flacbox", "nastavenia audio prehrávača", "ekvalizér Flacbox",
  "streamovanie hudby AirPlay", "hudba Google Cast", "audio záložky",
  "fronta prehrávania Flacbox", "opakovanie a zamiešanie Flacbox", "ovládanie hlasitosti Flacbox",
  "mini prehrávač macOS", "aplikácia hudby VoiceOver",
  "Flacbox FFmpeg", "korekcia výšky tónu Flacbox", "vzorkovacia frekvencia Flacbox",
  "externý DAC Flacbox", "priestorový zvuk Flacbox", "IO buffer Flacbox",
  "rýchlosť prehrávania Flacbox", "časovač spánku Flacbox"
]
tags: ["príručka", "flacbox", "prehrávač"]
readingTime: 14
---


Audio prehrávač je hlavná obrazovka aplikácie, kde ovládate hudbu a väčšinu funkcií prehrávania. Je to tiež miesto, kde hi-res audio engine Flacbox — postavený na systémových kodekoch a pribalenom **FFmpeg** — robí ťažkú prácu. Pozrime sa, ako ho používať.

## Prístup k audio prehrávači

Na prehrávač na celú obrazovku sa dostanete z lišty mini prehrávača. Na iPhone sedí mini prehrávač v dolnej časti hlavnej obrazovky. Na iPad a Mac je na ľavej strane. Ak chcete skryť mini prehrávač na iPhone, klepnite naň raz a potiahnite nadol. Ak chcete úplne zavrieť prehrávač na celú obrazovku, klepnite na tlačidlo zavrieť v pravom dolnom rohu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — hlavná obrazovka audio prehrávača" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Podporované zvukové formáty

Flacbox prehráva najpopulárnejšie zvukové formáty — systémové kodeky Apple aj mnohé ďalšie formáty spracované pribalených FFmpeg engine:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

To pokrýva prakticky každý moderný stratový a bezstratový formát, ktorý môžete mať v osobnej hudobnej zbierke.

## Ovládacie prvky prehrávania

V dolnej časti obrazovky prehrávača uvidíte tlačidlá Prehrať, Pozastaviť, Ďalšia skladba a Predchádzajúca skladba. Sú tu tiež voliteľné tlačidlá Ďalších 30 sek a Predchádzajúcich 30 sek, ktoré môžete povoliť v nastaveniach aplikácie (praktické pre audioknihy). Rýchle pretočenie dopredu alebo dozadu dosiahnete podržaním tlačidiel Ďalší / Predchádzajúci. Ak chcete preskočiť na konkrétnu časť skladby, potiahnite posúvač prehrávania.

## Opakovanie a zamiešanie

Klepnutím na tlačidlo opakovania cyklicky prechádzajte režimmi opakovania:

- **Opakovať všetko** — opakuje všetky skladby vo fronte.
- **Opakovať jednu** — opakuje iba aktuálnu skladbu.
- **Zastaviť opakovanie** — pozastaví sa, keď sa skončí aktuálna skladba.
- **Neopakovať** — prehrá frontu jedenkrát bez opakovania.

Pomocou tlačidla **Zamiešať** náhodne upravte poradie skladieb vo fronte.

## Ovládanie hlasitosti

Otvorte obrazovku Nastavenia zvuku klepnutím na ikonu zvuku pod ovládacími prvkami prehrávania, kde nájdete posúvač hlasitosti. Nájdete tu tiež tlačidlá **Google Cast** a **AirPlay**, aby ste mohli rýchlo prepnúť prehrávanie na iné zariadenie.

## Google Cast (Chromecast)

Pre používateľov Google Cast sa ikona **Cast** zobrazí v dolnej časti prehrávača. Klepnutím vyberte zariadenie a spustite streamovanie. Uistite sa, že vaše zariadenie a prijímač Google Cast sú v rovnakej sieti Wi-Fi. Poznámka: nie každý zvukový formát je kompatibilný s Google Cast — niektoré hi-res formáty môžu byť potrebné transkódovať.

## AirPlay

Pre AirPlay hľadajte tlačidlo **AirPlay** v dolnej časti prehrávača. Klepnite naň a vyberte zariadenie na streamovanie. Flacbox podporuje **AirPlay 2**, takže môžete prehrávať na viacerých HomePod, Apple TV alebo reproduktoroch kompatibilných s AirPlay 2 súčasne.

## Audio ekvalizér

Flacbox obsahuje **10-pásmový ekvalizér** s predvoľbami v štýle iPod. Klepnite na Ekvalizér v zobrazení hlasitosti, potom ho zapnite v pravom hornom rohu. Môžete použiť predvoľby ako Acoustic a Bass Booster alebo nastaviť každé frekvenčné pásmo pomocou posúvačov. Vytvárajte vlastné predvoľby, ukladajte ich pod ľubovoľným názvom a zvyšujte celkovú hlasitosť preamplifik átorom. Máme podrobnejšie pokyny na používanie ekvalizéra [tu](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — ekvalizér audio prehrávača" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Lišta nástrojov režimu prehrávača

Pre niektoré štýly prehrávača existuje vyhradená lišta nástrojov v hornej časti prehrávača na celú obrazovku. Táto lišta nástrojov obsahuje tri užitočné tlačidlá:

- **Hľadať** — rýchle vyhľadanie konkrétnej skladby vo fronte prehrávača.
- **Ovládanie rýchlosti prehrávania** — nastavte rýchlosť prehrávania od 0,02× do 3,00×. Ideálne pre audioknihy, podcasty a prednášky. Klepnutím na Normálne obnovíte predvolenú rýchlosť.
- **Audio záložky** — vytvárajte viacero záložiek na skladbu. Máme úplné pokyny na používanie záložiek [tu](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Fronta prehrávača

Ak chcete zobraziť frontu prehrávača, klepnite na tlačidlo fronty na pravej strane aktuálnej skladby. Každá skladba vo fronte má ďalšie akcie — klepnite na tri bodky a zobrazte ich. Ak chcete preusporiadať skladbu vo fronte, použite indikátor preusporiadania pri názve a presuňte ho na nové miesto.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — fronta prehrávania" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Komentáre / Texty

Ak chcete zobraziť komentáre k skladbe a vložené texty, ako aj súbory LRC, postupujte takto:

1. Otvorte **Nastavenia**.
2. Prejdite na **Audio prehrávač**.
3. Vyberte **Personalizácia**.
4. Klepnite na **Tlačidlá na hlavnej obrazovke**.
5. Povoľte **Komentáre**.

Potom klepnite niekoľkokrát na tlačidlo fronty prehrávača v dolnej časti obrazovky, aby ste prepínali z pohľadu na obal / frontu na pohľad komentárov. Na obrazovke Komentáre posuňte doprava, aby ste prepínali medzi **Komentármi**, **Vloženými textami** a **Súborom LRC**. Úplné pokyny sú dostupné [tu](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — obrazovka textov a komentárov" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Ponuka možností

Každá skladba vo fronte audio prehrávača má ponuku s ďalšími akciami, dostupnú klepnutím na tlačidlo s tromi bodkami pri názve skladby.

- **Prehrať ďalej** — pridá skladbu na začiatok fronty prehrávača.
- **Pridať do prehrávača** — zaradí skladbu do prehrávača, s možnosťou vytvorenia nového.
- **Pridať k obľúbeným** — označí skladbu ako obľúbenú pre rýchly prístup.
- **Stiahnuť** — uloží skladbu do lokálnych súborov, zobrazí sa na karte **Lokálne súbory** a v sekcii **Offline hudba**.
- **Upraviť audio tagy** — otvorí zabudovaný editor audio tagov na opravu chýbajúcich metadát, pričom modifikuje skladbu v úložisku.
- **Zobraziť v priečinku** — odhalí priečinok, kde je uložený zvukový súbor.
- **Zobraziť vo Finderi** — pre súbory importované z Mac odhalí priečinok, kde sa nachádza zvukový súbor na Mac.
- **Otvoriť v** — exportuje zvukový súbor do inej aplikácie.
- **Vymazať z fronty** — odstráni vybranú skladbu z fronty audio prehrávača.
- **Vymazať z cloudovej služby** — vymaže skladbu z hudobnej knižnice aj cloudového úložiska. **Táto akcia je nezvratná.**
- **Vymazať z lokálnych súborov** — vymaže skladbu z hudobnej knižnice aj lokálneho úložiska. **Táto akcia je nezvratná.**
- **Vymazať z hudobnej knižnice** — vymaže skladbu z hudobnej knižnice, pričom súbor zostáva v úložisku.

Rovnaké možnosti sú dostupné pre aktuálne prehrávanú položku vo fronte audio prehrávača, ku ktorej môžete pristupovať klepnutím na ikonu **Viac akcií** pri názve skladby.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — možnosti pre položku vo fronte prehrávania" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Ďalšie akcie prehrávača

Klepnutím na tlačidlo **Viac akcií** „..." na ľavej strane názvu aktuálne prehrávanej skladby zobrazíte ďalšie akcie.

- **Pokračovať v prehrávaní** — obnoví prehrávanie tam, kde ste skončili, vrátane fronty a pozície média. Obzvlášť užitočné pre audioknihy. Aktivuje sa v nastaveniach aplikácie.
- **Hľadať** — rýchle vyhľadanie konkrétnej skladby vo fronte audio prehrávača.
- **Záložky** — zobrazte zoznam vytvorených audio záložiek.
- **Komentáre** — zobrazte komentáre k skladbe a vložené texty, ako aj súbory LRC. Úplné pokyny [tu](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Rýchlosť** — nastavte rýchlosť prehrávania podľa svojich preferencií.
- **Nedávne** — prístup k zoznamu nedávno prehraných skladieb.
- **Obľúbené** — pozrite si zbierku obľúbených skladieb.
- **Audio ekvalizér** — aktivujte audio ekvalizér.
- **Časovač spánku** — nastavte časovač na automatické zastavenie prehrávania po uplynutí určeného intervalu. Skvelé pre chvíle, keď chcete zaspať pri hudbe.
- **Uložiť frontu do prehrávača** — uložte aktuálnu frontu audio prehrávača ako nový prehrávač.
- **Vymazať frontu** — vyčistí frontu prehrávača a zastaví prehrávanie.
- **Nastavenia** — prístup k nastaveniam audio prehrávača.
- **Pomocník** — nájdite pomoc a návod.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — obrazovka ďalšieho menu audio prehrávača" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Audio záložky

Táto funkcia vám umožňuje vytvárať viacero záložiek pre skladby v hudobnej knižnici — ideálne pre audioknihy, prednášky, dlhé DJ mixy alebo označenie refrénov obľúbených skladieb.

Ak chcete vytvoriť novú záložku:

- Začnite prehrávať požadovanú skladbu.
- Otvorte obrazovku prehrávača.
- Klepnite na tlačidlo **Záložky** na lište nástrojov režimu prehrávača.
- Vyberte **Pridať záložku**.
- Vyberte čas záložky a klepnite na **Hotovo** v pravom hornom rohu.

Úprava záložiek pre aktuálnu skladbu je jednoduchá: klepnite na Upraviť v pravom hornom rohu a vstúpite do režimu úprav. V tomto režime môžete preusporiadať záložky, odstrániť ich, upraviť čas záložky a zmeniť názvy záložiek. Podrobnejšie pokyny na audio záložky sú dostupné [tu](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — obrazovka audio záložiek" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Nedávne a obľúbené

Na obrazovke prehrávača klepnite na tri bodky pre prístup k Nedávnym a Obľúbeným. V oboch sekciách môžete vyhľadávať skladby, prehrávať všetko, zamiešať všetko, exportovať zoznam a vymazať zoznam. Máme podrobné pokyny na export zoznamov skladieb [tu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Pripojte iPhone k autu cez USB alebo bezdrôtový Apple CarPlay a Flacbox sa zobrazí na domovskej obrazovke CarPlay, pripravený na bezpečné prehrávanie hudby počas jazdy. Rozhranie CarPlay obsahuje vyhradené karty pre Knižnicu, Pripojenia, Lokálne súbory a Nastavenia, s ovládacími prvkami prehrávania, zamiešaním, opakovaním, správou fronty a audio ekvalizérom — všetko bez zdvíhania telefónu. Zážitok CarPlay ďalej konfigurujte v Nastavenia → CarPlay — možnosti zoradenia, stránkovanie, farba gradientu ikon ponuky, či sa načítavajú obrázky, a možnosť automatického pozastavenia prehrávania pri pripojení CarPlay.

[Prečítajte si úplného sprievodcu CarPlay](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox na Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widgety domovskej obrazovky (iPhone a iPad)

Flacbox podporuje widgety domovskej obrazovky a zamknutej obrazovky iOS, takže môžete na prvý pohľad vidieť a ovládať prehrávanie. Uistite sa, že Widgety sú povolené v Nastavenia → Widgety → Povoliť widgety, potom podržte Domovskú obrazovku alebo Zamknutú obrazovku, klepnite na **+**, vyhľadajte **Flacbox** a pridajte widget. Widget sa počas prehrávania aktualizuje a zobrazuje obal aktuálne prehrávanej skladby, názov a interpreta.

## Okno mini prehrávača (len Mac)

Používatelia Mac môžu používať kompaktný mini prehrávač, ktorý zostáva vždy navrchu. Presuňte kurzor na pravý dolný okraj okna Flacbox, zmenšite ho na minimálnu veľkosť a klepnite na tlačidlo zbaliť. Udržujte ho nad každým iným oknom výberom Okno → Zobraziť okno vždy navrchu v paneli ponúk — ideálne na udržanie ovládacích prvkov hudby viditeľných počas práce v inej aplikácii.

## Klávesové skratky (len Mac)

Pre používateľov Mac je v stavovom riadku k dispozícii systémová ponuka prehrávania s klávesovými skratkami. Napríklad stlačením medzerníka Prehrať / Pozastaviť. Skratky pre Zastaviť, Ďalšia skladba, Predchádzajúca skladba, Preskočiť čas, Opakovanie, Zamiešanie a Rýchlosť prehrávania sú tiež k dispozícii.

## Nastavenia audio prehrávača

Ak chcete získať prístup k nastaveniam, klepnite na tlačidlo Viac na obrazovke prehrávača a vyberte Nastavenia. Tu nájdete niekoľko sekcií, uvedených nižšie.

### Všeobecné

Tieto nastavenia pokrývajú základné aspekty audio prehrávača vrátane fronty prehrávania, audio výstupu a uloženia stavu prehrávača.

- **Režim opakovania** — vyberte, ako sa audio prehrávač správa, keď sa skončí skladba:
  - **Opakovať všetko** — znova prehrá všetky skladby vo fronte.
  - **Opakovať jednu** — opakuje iba aktuálnu skladbu.
  - **Zastaviť opakovanie** — pozastaví prehrávanie, keď sa skončí aktuálna skladba.
  - **Neopakovať** — umožňuje prehrávacej fronte prehrávať bez opakovania.
- **Režim zamiešania** — náhodne upraví poradie skladieb vo fronte. Môžete ho **Vypnúť** alebo **Zapnúť**.
- **Audio kodek** — vyberte audio engine použitý na prehrávanie:
  - **Systémový kodek + FFmpeg** — uprednostňuje systémový audio kodek tam, kde je to možné, čím zvyšuje kompatibilitu a stabilitu. Korekcia výšky tónu a nastavenia vzorkovacej frekvencie audio výstupu môžu byť v tomto režime obmedzené.
  - **FFmpeg** — vynúti kodek FFmpeg pre všetky zvukové súbory, čo vám umožní upravovať korekciu výšky tónu a vzorkovaciu frekvenciu audio výstupu.
- **Vzorkovacia frekvencia audio výstupu** — nastavte vzorkovaciu frekvenciu audio výstupu na optimalizáciu kvality zvuku, obzvlášť užitočné s externým DAC. Dostupné hodnoty: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** a **96 kHz**.
- **Počet kanálov audio výstupu** — pre viackanálové audio systémy s externým DAC zadajte počet kanálov: **Mono, Stereo, Stred / Ľavý / Pravý, Stred / Ľavý / Pravý / Surround, ITU BS.775-1, 5.1 Surround** a **SDDS**.
- **Preferované trvanie IO bufferu audio výstupu** — nakonfigurujte trvanie vstupného / výstupného bufferu pre prehrávanie zvuku. Typická hodnota na minimalizáciu latencie pri prehrávaní vysoko rozlišovacieho zvuku je okolo **5 milisekúnd (0,005 sekúnd)**. Prijateľná veľkosť bufferu závisí od hardvérového a softvérového prostredia, preto otestujte rôzne hodnoty trvania na cieľovom zariadení a vyberte tú, ktorá najlepšie vyvažuje nízku latenciu a prehrávanie bez výpadkov.
- **Režim audio výstupu (len iOS)** — nakonfigurujte režim zmiešaného audio výstupu, aby sa zvuk z Flacbox miešal s inými aplikáciami. Podrobné pokyny sú [tu](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Uložiť pozíciu prehrávania** — zabezpečí, že aplikácia ukladá a obnovuje pozíciu prehrávania pre skladby v hudobnej knižnici.
- **Uložiť stav audio prehrávača** — uchová stav audio prehrávača pred zatvorením aplikácie. Ak chcete pokračovať v prehrávaní, klepnite na **Pokračovať v prehrávaní** v hornej časti ľubovoľného priečinka, albumu, interpreta alebo žánru, keď znovu otvoríte aplikáciu. Prehrávanie môžete tiež obnoviť pre jednotlivé súbory klepnutím na konkrétnu skladbu.

Po povolení oboch nastavení **Uložiť pozíciu prehrávania** a **Uložiť stav audio prehrávača** otvorte ľubovoľný priečinok, album, interpreta alebo žáner a uvidíte tlačidlo **Pokračovať v prehrávaní** v hornej časti obrazovky spolu s naposledy uloženou skladbou a pozíciou. Klepnutím obnovíte prehrávanie presne tam, kde ste skončili.

### Personalizácia

Personalizácia vám umožňuje prispôsobiť vzhľad obrazovky audio prehrávača, zmeniť dostupné ovládacie prvky na hlavnej obrazovke, zamknutej obrazovke a stavovom riadku a konfigurovať ovládacie prvky preskočenia.

- **Štýl obrazovky audio prehrávača** — nakonfigurujte rozmiestnenie prvkov na obrazovke audio prehrávača.
- **Štýl posúvania obalov albumov** — nakonfigurujte preferovaný štýl posúvania pre obaly albumov.
- **Ďalšie prvky** — povoľte extra prvky na obrazovke audio prehrávača. **Informácie o audio formáte** zobrazujú audio informácie aktuálne prehrávanej skladby nad obalon; **Posúvač hlasitosti zvuku** zobrazuje posúvač audio výstupu pod ovládacími prvkami prehrávania.
- **Akcie hlavnej obrazovky** — nakonfigurujte, ktoré tlačidlá by mali byť predvolene viditeľné na hlavnej obrazovke audio prehrávača: **Opakovanie a zamiešanie, Ďalšia a predchádzajúca skladba, Preskočiť čas, Časovač spánku, Google Chromecast, AirPlay a Bluetooth, Audio ekvalizér, Hľadať, Záložky, Rýchlosť, Pridať záložku, Pridať k obľúbeným, Komentáre** a ďalšie.
- **Ovládacie prvky prehrávania na zamknutej obrazovke** — vyberte, ktoré ovládacie prvky sa zobrazujú na zamknutej obrazovke. Možné hodnoty: **Preskočiť čas, Pridať záložku, Pridať k obľúbeným**.
- **Tlačidlá preskočenia** — vyberte časový interval pre tlačidlá **Preskočiť čas**.

### Načítanie súborov

Počas procesu načítania súborov môžete zmeniť typ siete použitý na načítanie skladieb. Dostupné možnosti: **Wi-Fi**, **Wi-Fi a mobilné dáta**.

- **Čas prednahrávania** — nastavte časový interval bufferingu. Zvýšte ho, ak máte slabé sieťové pripojenie.
- **Použiť priamu URL** — ak je povolené, na načítanie skladby sa použije priama URL, ak to server podporuje. Môže to urýchliť načítanie skladby, ale môže to ovplyvniť stabilitu prehrávania.

### Audio ekvalizér

Prispôsobte nastavenia audio ekvalizéra. O konfigurácii audio ekvalizéra si môžete prečítať viac [tu](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Rýchlosť prehrávania

Nastavte rýchlosť prehrávania audio prehrávača od **0,02× do 3,00×**. Klepnutím na ikonu konfigurácie v pravom hornom rohu prepnete do **presného režimu** pre jemnejšie nastavenia.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — obrazovka rýchlosti prehrávania" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Korekcia výšky tónu

Zmeňte nastavenia korekcie výšky tónu pomocou preddefinovaných hodnôt. Medzi preddefinovanými hodnotami a presným režimom môžete tiež prepínať klepnutím na tlačidlo v pravom hornom rohu. Korekcia výšky tónu je k dispozícii v ceste kodeku FFmpeg s rozsahom od **-1000 do +1000**.

### Pamäť cache prehrávania

Skladby vo fronte audio prehrávača sa automaticky sťahujú na zabezpečenie plynulého prehrávania. Ak manuálne sťahujete zvukové súbory, môžete túto možnosť zakázať, aby ste sa vyhli duplicitám. Tu môžete tiež nastaviť veľkosť pamäte cache audio prehrávača.

### Časovač spánku

Aktivujte časovač na automatické zastavenie prehrávania po uplynutí určeného obdobia — praktické, keď chcete zaspať pri hudbe. Klepnutím na ikonu konfigurácie v pravom hornom rohu aktivujete **presný režim** s granularitou po minútach.

## Dostupnosť

Flacbox je plne prístupný s **VoiceOver**. Každá komponenta má dobre navrhnutý štítok a popis. Keď je aktívny VoiceOver, aplikácia prepne do **Textového režimu**, takže sa zobrazujú iba zmysluplné prvky — čím sa zlepšuje rýchlosť navigácie a prehľadnosť. Textový režim môžete tiež aktivovať v **Nastavenia → Dostupnosť → Textový režim**.

### Nastavenie posúvačov pomocou VoiceOver

1. **Vyberte posúvač** — potiahnite doľava alebo doprava, kým VoiceOver neoznámi posúvač.
2. **Upravte hodnotu** — dvakrát klepnite a podržte posúvač, potom ho rýchlo pretiahnite nahor alebo nadol, aby ste zmenili hodnotu. VoiceOver oznamuje novú hodnotu počas pohybu.

### Nastavenie pozície skladby v zozname pomocou VoiceOver

1. Klepnite na ikonu indikátora preusporiadania pri názve skladby, aby ste na ňu zamerali pozornosť.
2. Rýchlo dvakrát klepnite na indikátor preusporiadania. Pri druhom klepnutí neuvoľnite prst — podržte ho, kým nezačujete zvuk signalizujúci, že bunka je pripravená na presunutie.
3. Presuňte bunku na nové miesto.

Ostatné komponenty fungujú podľa očakávania, pričom používajú vzory VoiceOver poskytované systémom.
