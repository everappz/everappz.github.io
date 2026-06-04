---
title: "Přehrávač zvuku"
date: 2020-02-01
description: "Naučte se používat přehrávač zvuku Flacbox na iPhonu, iPadu a Macu. Ovládejte přehrávání, spravujte fronty, konfigurujte zvukový engine FFmpeg / systému, měňte vzorkovací frekvenci, korekci výšky tónu, dobu trvání IO bufferu, ekvalizér, záložky zvuku, AirPlay 2, Google Cast, CarPlay, widgety a klávesové zkratky Macu."
keywords: [
  "průvodce přehrávačem Flacbox", "nastavení přehrávače zvuku", "ekvalizér Flacbox",
  "streamování hudby AirPlay", "hudba Google Cast", "záložky zvuku",
  "fronta přehrávání Flacbox", "opakování a náhodné přehrávání Flacbox", "ovládání hlasitosti Flacbox",
  "mini přehrávač macOS", "hudební aplikace VoiceOver",
  "FFmpeg Flacbox", "korekce výšky tónu Flacbox", "vzorkovací frekvence Flacbox",
  "externí DAC Flacbox", "prostorový zvuk Flacbox", "IO buffer Flacbox",
  "rychlost přehrávání Flacbox", "časovač spánku Flacbox"
]
tags: ["průvodce", "flacbox", "přehrávač"]
readingTime: 14
---


Přehrávač zvuku je hlavní obrazovkou aplikace, kde ovládáte hudbu a většinu funkcí přehrávání. Je to také místo, kde zvukový engine Flacbox s vysokým rozlišením — postavený na systémových kodecích plus přibalenou knihovnou **FFmpeg** — odvádí veškerou těžkou práci. Pojďme prozkoumat, jak ho používat.

## Přístup k přehrávači zvuku

Na přehrávač na celou obrazovku se dostanete z lišty mini přehrávače. Na iPhonu se mini přehrávač nachází v dolní části hlavní obrazovky. Na iPadu a Macu je na levé straně. Chcete-li skrýt mini přehrávač na iPhonu, klepněte na něj jednou a přejeďte dolů. Chcete-li přehrávač na celou obrazovku úplně zavřít, klepněte na tlačítko zavřít v pravém dolním rohu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Hlavní obrazovka přehrávače zvuku Flacbox" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Podporované zvukové formáty

Flacbox přehrává nejpopulárnější zvukové formáty — jak systémové kodeky Apple, tak mnoho dalších formátů zpracovávaných přibaleným enginem FFmpeg:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

To pokrývá prakticky každý moderní ztrátový i bezztrátový formát, který pravděpodobně máte v osobní hudební sbírce.

## Ovládací prvky přehrávání

V dolní části obrazovky přehrávače uvidíte tlačítka pro Přehrát, Pozastavit, Další skladba a Předchozí skladba. Jsou zde také volitelná tlačítka jako Dopředu 30 sekund a Zpět 30 sekund, která lze aktivovat v nastavení aplikace (šikovné pro audioknihy). Rychlé přetáčení dopředu nebo dozadu provedete podržením tlačítek Další / Předchozí. Chcete-li přejít na konkrétní část skladby, přetáhněte posuvník přehrávání.

## Opakování a náhodné přehrávání

Klepnutím na tlačítko opakování procházejte režimy opakování:

- **Opakovat vše** — opakuje všechny skladby ve frontě.
- **Opakovat jednu** — opakuje pouze aktuální skladbu.
- **Zastavit opakování** — pozastaví přehrávání po skončení aktuální skladby.
- **Bez opakování** — přehraje frontu jednou bez opakování.

Tlačítkem **Náhodně** randomizujte pořadí skladeb ve frontě.

## Ovládání hlasitosti

Otevřete obrazovku Nastavení zvuku klepnutím na ikonu zvuku pod ovládacími prvky přehrávání pro přístup k posuvníku hlasitosti. Zde také najdete tlačítka pro **Google Cast** a **AirPlay**, abyste mohli rychle přepnout přehrávání na jiné zařízení.

## Google Cast (Chromecast)

Pro uživatele Google Cast se ikona **Cast** zobrazuje v dolní části přehrávače. Klepněte na ni pro výběr zařízení a zahájení streamování. Ujistěte se, že vaše zařízení a přijímač Google Cast jsou ve stejné síti Wi-Fi. Poznámka: ne každý zvukový formát je kompatibilní s Google Cast — některé formáty s vysokým rozlišením mohou vyžadovat překódování.

## AirPlay

Pro AirPlay hledejte tlačítko **AirPlay** v dolní části přehrávače. Klepněte na něj a vyberte zařízení pro streamování. Flacbox podporuje **AirPlay 2**, takže můžete přehrávat na více HomePodech, Apple TV nebo reproduktorech kompatibilních s AirPlay 2 současně.

## Zvukový ekvalizér

Flacbox obsahuje **10-pásmový ekvalizér** s předvolbami ve stylu iPod. Klepněte na Ekvalizér v zobrazení hlasitosti a poté ho zapněte v pravém horním rohu. Můžete použít předvolby jako Acoustic a Bass Booster nebo upravit každé frekvenční pásmo posuvníky. Vytvořte si vlastní předvolby, uložte je pod libovolným názvem a zvyšte celkovou hlasitost předzesilovačem. Podrobnější návod k použití zvukového ekvalizéru máme [zde](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Ekvalizér přehrávače zvuku Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Panel nástrojů režimu přehrávače

Pro některé styly přehrávače je k dispozici vyhrazený panel nástrojů v horní části přehrávače na celou obrazovku. Tento panel nástrojů obsahuje tři užitečná tlačítka:

- **Hledat** — rychle najděte konkrétní skladbu ve frontě přehrávače.
- **Ovládání rychlosti přehrávání** — nastavte rychlost přehrávání v rozsahu od 0,02× do 3,00×. Ideální pro audioknihy, podcasty a přednášky. Klepnutím na Normální se vrátíte na výchozí rychlost.
- **Záložky zvuku** — vytvářejte více záložek pro každou skladbu. Kompletní návod k použití záložek máme [zde](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Fronta přehrávače

Chcete-li zobrazit frontu přehrávače, klepněte na tlačítko fronty na pravé straně aktuální písně. Každá píseň ve frontě má více akcí — klepněte na tři tečky pro jejich zobrazení. Chcete-li změnit pořadí písně ve frontě, použijte indikátor přeřazení u názvu a přetáhněte ho na novou pozici.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fronta přehrávání Flacbox" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Komentáře / Texty

Chcete-li zobrazit komentáře ke skladbě a vložené texty, a také soubory LRC, postupujte takto:

1. Otevřete **Nastavení**.
2. Přejděte na **Přehrávač zvuku**.
3. Vyberte **Personalizace**.
4. Klepněte na **Tlačítka na hlavní obrazovce**.
5. Povolte **Komentáře**.

Poté klepněte na tlačítko fronty přehrávače v dolní části obrazovky několikrát, abyste přepnuli z zobrazení obalu / fronty na zobrazení komentářů. Na obrazovce Komentáře přejeďte doprava pro přepínání mezi **Komentáři**, **Vloženými texty** a **Souborem LRC**. Kompletní pokyny jsou k dispozici [zde](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka textů a komentářů Flacbox" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Nabídka možností

Každá píseň ve frontě přehrávače zvuku má nabídku s dalšími akcemi, přístupnou klepnutím na tlačítko tří teček u názvu písně.

- **Přehrát jako další** — přidá píseň na začátek fronty přehrávače.
- **Přidat do seznamu skladeb** — zahrne píseň do seznamu skladeb s možností vytvoření nového.
- **Přidat do oblíbených** — označí píseň jako oblíbenou pro rychlý přístup.
- **Stáhnout** — uloží píseň do místních souborů, kde se zobrazí v záložce **Místní soubory** a v sekci **Offline hudba**.
- **Upravit audio tagy** — otevře vestavěný editor audio tagů pro opravu chybějících metadat, přičemž upraví píseň ve vašem úložišti.
- **Zobrazit ve složce** — odhalí složku, kde je zvukový soubor uložen.
- **Zobrazit ve Finderu** — pro soubory importované z Macu odhalí složku, kde se zvukový soubor nachází na vašem Macu.
- **Otevřít v** — exportuje zvukový soubor do jiné aplikace.
- **Smazat z fronty** — odstraní vybranou píseň z fronty přehrávače zvuku.
- **Smazat z cloudové služby** — smaže píseň z hudební knihovny i cloudového úložiště. **Tato akce je nevratná.**
- **Smazat z místních souborů** — smaže píseň z hudební knihovny i místního úložiště. **Tato akce je nevratná.**
- **Smazat z hudební knihovny** — smaže píseň z vaší hudební knihovny a ponechá soubor v úložišti.

Stejné možnosti jsou k dispozici pro aktuálně přehrávanou položku ve frontě přehrávače zvuku, ke které se dostanete klepnutím na ikonu **Další akce** u názvu skladby.

{{< cards cols="1">}}
  {{< card title="" subtitle="Možnosti Flacbox pro položku ve frontě přehrávání" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Další akce přehrávače

Klepnutím na tlačítko **Další akce** "..." na levé straně názvu aktuálně přehrávané písně zobrazíte další akce.

- **Pokračovat v přehrávání** — pokračujte od místa, kde jste skončili, včetně fronty a pozice médií. Zvláště užitečné pro audioknihy. Aktivuje se v nastavení aplikace.
- **Hledat** — rychle najděte konkrétní skladbu ve frontě přehrávače zvuku.
- **Záložky** — zobrazte si seznam vytvořených zvukových záložek.
- **Komentáře** — zobrazte komentáře ke skladbě a vložené texty, a také soubory LRC. Kompletní pokyny [zde](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Rychlost** — nastavte rychlost přehrávání podle svých preferencí.
- **Nedávné** — přistupte k seznamu nedávno přehrávaných písní.
- **Oblíbené** — prohlédněte si kolekci oblíbených písní.
- **Zvukový ekvalizér** — aktivujte zvukový ekvalizér.
- **Časovač spánku** — nastavte časovač pro zastavení přehrávání po zadaném intervalu. Skvělé pro chvíle, kdy chcete usnout při své hudbě.
- **Uložit frontu jako seznam skladeb** — uložte aktuální frontu přehrávače zvuku jako nový seznam skladeb.
- **Smazat frontu** — vyčistěte frontu přehrávače a zastavte přehrávání.
- **Nastavení** — přistupte k nastavení přehrávače zvuku.
- **Nápověda** — najděte pomoc a pokyny.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka dalších akcí přehrávače zvuku Flacbox" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Zvukové záložky

Tato funkce vám umožňuje vytvářet více záložek pro skladby ve vaší hudební knihovně — ideální pro audioknihy, přednášky, dlouhé DJ mixy nebo označení refrénu oblíbené skladby.

Vytvoření nové záložky:

- Začněte přehrávat požadovanou píseň.
- Otevřete obrazovku přehrávače.
- Klepněte na tlačítko **Záložky** na panelu nástrojů režimu přehrávače.
- Vyberte **Přidat záložku**.
- Zvolte čas záložky a klepněte na **Hotovo** v pravém horním rohu.

Úprava záložek pro aktuální skladbu je snadná: klepněte na Upravit v pravém horním rohu pro přechod do režimu úprav. V tomto režimu můžete záložky přeřadit, smazat, upravit čas záložky a změnit názvy záložek. Podrobnější pokyny ke zvukovým záložkám jsou k dispozici [zde](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka zvukových záložek Flacbox" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Nedávné a oblíbené

Na obrazovce přehrávače klepněte na tři tečky pro přístup k Nedávným a Oblíbeným. V obou sekcích můžete hledat písně, přehrávat vše, přehrávat vše náhodně, exportovat seznam a vymazat seznam. Podrobné pokyny k exportu seznamů písní máme [zde](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Připojte svůj iPhone k autu přes USB nebo bezdrátový Apple CarPlay a Flacbox se zobrazí na domovské obrazovce vašeho CarPlay, připraven bezpečně přehrávat hudbu při jízdě. Rozhraní CarPlay zahrnuje věnované záložky pro Knihovnu, Připojení, Místní soubory a Nastavení s ovládacími prvky přehrávání, náhodným přehráváním, opakováním, správou fronty a zvukovým ekvalizérem — vše dostupné bez sáhnutí po telefonu. Dále nakonfigurujte prostředí CarPlay v Nastavení → CarPlay — možnosti řazení, stránkování, barva přechodu ikon nabídky, zda jsou načteny obrázky, a možnost automaticky pozastavit přehrávání při připojení CarPlay.

[Přečtěte si úplného průvodce CarPlay](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox na Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widgety domovské obrazovky (iPhone a iPad)

Flacbox podporuje widgety domovské obrazovky a zamykací obrazovky iOS, takže vidíte a ovládáte přehrávání na první pohled. Ujistěte se, že jsou widgety povoleny v Nastavení → Widgety → Povolit widgety, poté dlouze stiskněte domovskou obrazovku nebo zamykací obrazovku, klepněte na **+**, vyhledejte **Flacbox** a přidejte widget. Widget se aktualizuje během přehrávání a zobrazuje obal aktuálně přehrávané skladby, název a umělce.

## Okno mini přehrávače (výhradně Mac)

Uživatelé Macu mohou používat kompaktní, vždy nahoře umístěný mini přehrávač. Přesuňte kurzor na pravý dolní okraj okna Flacbox, zmenšete ho na nejmenší velikost a klepněte na tlačítko sbalení. Udržte ho nad každým jiným oknem výběrem Okno → Vždy zobrazovat okno nahoře v liště nabídek — ideální pro udržení ovládacích prvků hudby viditelných, zatímco pracujete v jiné aplikaci.

## Klávesové zkratky (výhradně Mac)

Pro uživatele Macu je v liště stavu dostupná nabídka přehrávání systému s klávesovými zkratkami. Například stisknutím mezerníku přehrajete / pozastavíte. K dispozici jsou také zkratky pro Zastavit, Další skladba, Předchozí skladba, Přeskočit čas, Opakovat, Náhodně a Rychlost přehrávání.

## Nastavení přehrávače zvuku

Pro přístup k nastavení klepněte na tlačítko Více na obrazovce přehrávače a zvolte Nastavení. Zde najdete několik sekcí uvedených níže.

### Obecné

Tato nastavení pokrývají základní aspekty přehrávače zvuku, včetně fronty přehrávání, výstupu zvuku a ukládání stavu přehrávače.

- **Režim opakování** — zvolte, jak se přehrávač zvuku chová po skončení skladby:
  - **Opakovat vše** — znovu přehraje všechny skladby ve vaší frontě.
  - **Opakovat jednu** — opakuje pouze aktuální skladbu.
  - **Zastavit opakování** — pozastaví přehrávání po skončení aktuální skladby.
  - **Bez opakování** — umožňuje přehrát frontu bez opakování.
- **Režim náhodného přehrávání** — randomizuje pořadí skladeb ve frontě. Lze nastavit na **Náhodně vypnuto** nebo **Náhodně zapnuto**.
- **Zvukový kodek** — zvolte zvukový engine používaný pro přehrávání:
  - **Systémový kodek + FFmpeg** — tam, kde je to možné, dává přednost systémovému zvukovému kodeku, čímž zvyšuje kompatibilitu a stabilitu. Korekce výšky tónu a úpravy vzorkovací frekvence výstupu zvuku mohou být v tomto režimu omezeny.
  - **FFmpeg** — vynucuje kodek FFmpeg pro všechny zvukové soubory, což vám umožňuje upravit korekci výšky tónu a vzorkovací frekvenci výstupu zvuku.
- **Vzorkovací frekvence výstupu zvuku** — upravte vzorkovací frekvenci výstupu zvuku pro optimalizaci kvality zvuku, zvláště užitečné s externím DAC. Dostupné hodnoty: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** a **96 kHz**.
- **Počet kanálů výstupu zvuku** — pro vícekanálové zvukové systémy s externím DAC zadejte počet kanálů: **Mono, Stereo, Střed / Levý / Pravý, Střed / Levý / Pravý / Prostorový, ITU BS.775-1, 5.1 Prostorový** a **SDDS**.
- **Preferovaná doba trvání IO bufferu výstupu zvuku** — nakonfigurujte dobu trvání vstupního / výstupního bufferu pro přehrávání zvuku. Typická hodnota pro minimalizaci latence při přehrávání zvuku s vysokým rozlišením je přibližně **5 milisekund (0,005 sekundy)**. Přijatelná velikost bufferu závisí na vašem hardwarovém a softwarovém prostředí, proto otestujte různé doby na vašem cílovém zařízení a vyberte tu, která nejlépe vyvažuje nízkou latenci a přehrávání bez chyb.
- **Režim výstupu zvuku (pouze iOS)** — nakonfigurujte smíšený režim výstupu zvuku, aby se zvuk z Flacboxu prolínal s ostatními aplikacemi. Podrobné pokyny jsou [zde](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Uložit polohu přehrávání** — zajistí, že aplikace ukládá a obnovuje polohu přehrávání pro písně ve vaší hudební knihovně.
- **Uložit stav přehrávače zvuku** — zachová stav vašeho přehrávače zvuku před zavřením aplikace. Chcete-li pokračovat v přehrávání, klepněte na **Pokračovat v přehrávání** v horní části libovolné složky, alba, umělce nebo žánru při opětovném otevření aplikace. Přehrávání pro jednotlivé soubory můžete také obnovit klepnutím na konkrétní skladbu.

Jakmile povolíte **Uložit polohu přehrávání** i **Uložit stav přehrávače zvuku**, otevřete libovolnou složku, album, umělce nebo žánr a v horní části obrazovky uvidíte tlačítko **Pokračovat v přehrávání** spolu s poslední uloženou skladbou a polohou. Klepnutím na něj pokračujete přesně tam, kde jste skončili.

### Personalizace

Personalizace vám umožňuje přizpůsobit vzhled obrazovky přehrávače zvuku, změnit dostupné ovládací prvky na hlavní obrazovce, zamykací obrazovce a liště stavu a nakonfigurovat ovládací prvky přeskočení času.

- **Styl obrazovky přehrávače zvuku** — nakonfigurujte umístění prvků na obrazovce přehrávače zvuku.
- **Styl posouvání obalů alb** — nakonfigurujte preferovaný styl posouvání pro obaly alb.
- **Další prvky** — aktivujte další prvky na obrazovce přehrávače zvuku. **Informace o zvukovém formátu** zobrazuje zvukové informace o aktuálně přehrávané skladbě nad obalem; **Posuvník hlasitosti zvuku** zobrazuje posuvník výstupu zvuku pod ovládacími prvky přehrávání.
- **Akce hlavní obrazovky** — nakonfigurujte, která tlačítka by měla být ve výchozím nastavení viditelná na hlavní obrazovce přehrávače zvuku: **Režim opakování a náhodného přehrávání, Další a předchozí píseň, Přeskočit čas, Časovač spánku, Google Chromecast, AirPlay a Bluetooth, Zvukový ekvalizér, Hledat, Záložky, Rychlost, Přidat záložku, Přidat do oblíbených, Komentáře** a další.
- **Ovládací prvky přehrávání na zamykací obrazovce** — zvolte, které ovládací prvky se zobrazují na zamykací obrazovce. Možné hodnoty: **Přeskočit čas, Přidat záložku, Přidat do oblíbených**.
- **Tlačítka přeskočení času** — zvolte časový interval pro tlačítka **Přeskočit čas**.

### Načítání souborů

Během procesu načítání souborů můžete změnit typ sítě používaný pro načítání písní. Dostupné možnosti: **Wi-Fi**, **Wi-Fi a mobilní data**.

- **Čas předběžného načítání** — nastavte časový interval ukládání do vyrovnávací paměti. Zvyšte tuto hodnotu, pokud máte slabé síťové připojení.
- **Použít přímou URL** — pokud je povoleno, pro načtení písně se použije přímá URL, pokud to server podporuje. Může to zrychlit načítání písní, ale může ovlivnit stabilitu přehrávání.

### Zvukový ekvalizér

Přizpůsobte nastavení zvukového ekvalizéru. Více o konfiguraci zvukového ekvalizéru si můžete přečíst [zde](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Rychlost přehrávání

Nastavte rychlost přehrávání zvukového přehrávače od **0,02× do 3,00×**. Klepnutím na ikonu konfigurace v pravém horním rohu přepněte do **přesného režimu** pro jemnější úpravy.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka rychlosti přehrávání Flacbox" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Korekce výšky tónu

Změňte nastavení korekce výšky tónu pomocí předdefinovaných hodnot. Mezi předdefinovanými hodnotami a přesným režimem můžete také přepínat klepnutím na tlačítko v pravém horním rohu. Korekce výšky tónu je k dispozici v cestě kodeku FFmpeg s rozsahem od **-1000 do +1000**.

### Mezipaměť přehrávání

Písně ve frontě přehrávače zvuku jsou automaticky staženy, aby bylo zajištěno plynulé přehrávání. Pokud zvukové soubory stahujete ručně, můžete tuto možnost zakázat, abyste předešli duplicitám. Zde můžete také nakonfigurovat velikost mezipaměti přehrávače zvuku.

### Časovač spánku

Aktivujte časovač pro automatické zastavení přehrávání po zadané době — šikovné, když chcete usnout při hudbě. Klepnutím na ikonu konfigurace v pravém horním rohu aktivujte **přesný režim** s granularitou po minutách.

## Přístupnost

Flacbox je plně přístupný s **VoiceOver**. Každá komponenta má dobře navrženou popisku a popis. Když je VoiceOver aktivní, aplikace přepne do **Textového režimu**, takže se zobrazí pouze smysluplné prvky — čímž se zlepšuje rychlost navigace a přehlednost. Textový režim lze také aktivovat v **Nastavení → Přístupnost → Textový režim**.

### Úprava posuvníků pomocí VoiceOver

1. **Vyberte posuvník** — přejeďte doleva nebo doprava, dokud ho VoiceOver neoznámí.
2. **Upravte hodnotu** — dvojitě klepněte a podržte posuvník, poté přetáhněte nahoru nebo dolů pro rychlou změnu hodnoty. VoiceOver oznamuje novou hodnotu, jak postupujete.

### Úprava pozice skladby v seznamu pomocí VoiceOver

1. Klepněte na ikonu indikátoru přeřazení u názvu skladby, abyste mu dali fokus.
2. Rychle dvakrát klepněte na indikátor přeřazení. Při druhém klepnutí neuvolňujte prst — podržte ho, dokud neuslyšíte zvuk označující, že buňka je připravena k přesunutí.
3. Přesuňte buňku na novou pozici.

Ostatní komponenty fungují podle očekávání s použitím vzorů VoiceOver poskytovaných systémem.
