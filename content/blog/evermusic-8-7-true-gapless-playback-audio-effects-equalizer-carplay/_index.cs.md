---
title: "Evermusic 8.7: skutečné přehrávání bez mezer, zvukové efekty, normalizace hlasitosti, přepracovaný ekvalizér"
date: 2026-07-05
description: "Evermusic 8.7 pro iPhone, iPad a Mac přidává skutečné přehrávání bez mezer, pět studiových zvukových efektů (dozvuk, echo, zkreslení, kompresor, crossfeed), normalizaci hlasitosti EBU R128, přepracovaný 10pásmový ekvalizér s importem/exportem předvoleb, přestavěný streamovací engine AVAudioEngine s podporou FLAC a Ogg Vorbis a rychlejší, přesnější CarPlay a Právě se přehrává."
keywords: ["Evermusic 8.7", "aktualizace Evermusic", "skutečné přehrávání bez mezer iPhone", "hudební přehrávač bez mezer iOS", "přehrávání bez mezer CarPlay", "zvukové efekty hudební přehrávač iPhone", "dozvuk echo zkreslení kompresor crossfeed iOS", "crossfeed sluchátka iOS", "normalizace hlasitosti iPhone", "normalizace hlasitosti hudební přehrávač", "normalizace EBU R128 iOS", "alternativa k replay gain iPhone", "10pásmový ekvalizér iPhone", "grafický ekvalizér aplikace iOS", "import export předvoleb ekvalizéru", "přehrávač FLAC iPhone", "přehrávač Ogg Vorbis iOS", "bezztrátový hudební přehrávač iPhone 2026", "hudební přehrávač AVAudioEngine", "hudební přehrávač CarPlay iPhone", "přesnost Právě se přehrává zamykací obrazovka", "cloudový hudební přehrávač iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Přehrávání bez mezer", "Zvukové efekty", "Dozvuk", "Echo", "Zkreslení", "Kompresor", "Crossfeed", "Normalizace hlasitosti", "EBU R128", "Ekvalizér", "FLAC", "Ogg Vorbis", "CarPlay", "Právě se přehrává", "Liquid Glass", "Novinky"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Ve zkratce:** [Evermusic 8.7](/products/evermusic) je vydání zaměřené na kvalitu zvuku pro iPhone, iPad a Mac. Přináší **skutečné přehrávání bez mezer** (žádné pauzy, lupnutí ani cvaknutí mezi skladbami), kompletní sadu **studiových zvukových efektů** – dozvuk, echo, zkreslení, kompresor a crossfeed – a **normalizaci hlasitosti EBU R128**, která udržuje hlasitost konzistentní od skladby ke skladbě bez značek ReplayGain. **10pásmový ekvalizér** byl přepracován s novými posuvníky, rychlejším přepínáním předvoleb, vlastními předvolbami, které lze importovat a exportovat, a lepším rozložením na šířku a na iPadu. Pod kapotou **přestavěný streamovací engine AVAudioEngine** zlepšuje spolehlivost a podporu formátů, včetně **FLAC** a **Ogg Vorbis**. **CarPlay** a **Právě se přehrává** jsou rychlejší a přesnější na zamykací obrazovce, v autě i z ovladačů na sluchátkách.

---

## Zdravím všechny!

Evermusic 8.7 je k dispozici ke stažení. Tato aktualizace je celá o tom, jak vaše hudba *zní*. Přestavěli jsme přehrávací engine pro skutečné přehrávání bez mezer, přidali sadu zvukových efektů studiové kvality, zavedli normalizaci hlasitosti a přepracovali ekvalizér od posuvníků nahoru. To vše je zabaleno do nového designu Applu **Liquid Glass**.

[Stáhněte si Evermusic 8.7 z App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) nebo aktualizujte ze své stávající verze. Evermusic je zdarma ke stažení s volitelnými vylepšeními v aplikaci.

## Skutečné přehrávání bez mezer

Přehrávání bez mezer znamená, že ticho mezi dvěma skladbami je pryč. Žádná pauza, žádné lupnutí, žádné cvaknutí – aktuální skladba plyne přímo do následující. Nejvíc záleží u hudby, která byla navržena k poslechu jako celek: **živé nahrávky, DJ mixy, klasická díla a koncepční alba**, kde jedna skladba přechází přímo do druhé.

Zde je, co se změnilo technicky. Zvukový engine Evermusic udržuje dvě skladby ve hře najednou: tu, kterou slyšíte, a následující ve frontě. Zatímco aktuální skladba hraje, následující se už na pozadí **načítá, dekóduje a předem vyrovnává do paměti**. Když aktuální skladba dosáhne konce, engine předá řízení následující skladbě **uvnitř přehrávače, nikoli uvnitř zvukového proudu**. Výstupní vykreslovací smyčka nepřetržitě odebírá zvukové vzorky ze souvislé kruhové vyrovnávací paměti a nikdy se nezastaví, takže posluchač nikdy neuslyší předěl. Přepnutí proběhne mezi vzorky, a přesně proto zde není žádná slyšitelná mezera.

Funguje to stejně, ať už je soubor v zařízení, v cloudu nebo na mediálním serveru – předběžné vyrovnávání do paměti u vzdálených zdrojů jen začne o něco dříve.

## Studiové zvukové efekty

Evermusic 8.7 přidává pět zvukových efektů v reálném čase, které můžete navrstvit na svou hudbu. Každý běží jako nativní zvukově zpracovací uzel v přehrávacím enginu, takže se použije na vše, co přehráváte – místní soubory, cloudové streamy i internetové rádio – bez opětovného kódování.

Každý efekt přichází s **pečlivě sestavenou knihovnou předvoleb**, abyste získali skvělý zvuk jedním klepnutím, a Evermusic si **pamatuje vaše přesné nastavení** mezi relacemi. Upravte jakýkoli ovládací prvek a efekt se přepne do stavu **Ručně**, takže vždy víte, kdy jste se odchýlili od předvolby.

### Dozvuk

Přidává pocit prostoru, od těsné místnosti po katedrálu. Postavený na `AVAudioUnitReverb` od Applu nabízí **13 předvoleb místností** (Malá místnost, Střední sál, Deska, Katedrála a další) plus ovládání **mokrého/suchého mixu** od 0 do 100 %, takže rozhodujete, kolik prostoru přidat.

### Echo

Klasická ozvěna s **10 předvolbami** – Slapback, Páskové echo, Dub, Ambientní a další. Můžete nastavit **dobu echa** (až 2 sekundy), **zpětnou vazbu** (kolik opakování), **dolní propust** pro zteplení opakování a **mokrý/suchý mix**.

### Zkreslení

Od jemné drsnosti po plnou lo-fi destrukci, řízené `AVAudioUnitDistortion` s **22 charakterovými předvolbami** (Bit Brush, Cellphone Concert, Radio Tower a další), ovládáním **předzesílení** a mokrým/suchým mixem, takže můžete efekt přimísit zpět k čistému signálu.

### Kompresor

Dynamický procesor (`AUDynamicsProcessor` od Applu), který vyrovnává hlasité a tiché pasáže. Zpřístupňuje kompletní profesionální sadu ovládání – **práh, poměr/rezerva, nástup, uvolnění, expanze a kompenzační zesílení** – s **10 předvolbami** vyladěnými na reálné situace: mimo jiné Hlas / Podcast, Pozdní noc, Filmový dialog, Sladění se streamem a Maximální hlasitost.

### Crossfeed

Crossfeed způsobí, že poslech na sluchátkách zní přirozeněji, tím, že přimíchá trochu levého kanálu do pravého a naopak, tak jak vaše uši slyší skutečné reproduktory. Je postaven na známém algoritmu **Bauer stereophonic-to-binaural (bs2b)**, s ovládáním **úrovně crossfeedu** a **mezní frekvence** a **6 předvolbami** včetně u audiofilů oblíbených nastavení *Chu Moy* a *Jan Meier*. Je zvlášť dobrý u starších stereo mixů ze 60. a 70. let s krajním panoramatem.

## Normalizace hlasitosti

Sestavili jste někdy playlist, kde jedna skladba burácí a další je šepot? Normalizace hlasitosti to vyřeší. Evermusic 8.7 používá **měření hlasitosti EBU R128** (stejný standard ITU-R BS.1770 používaný ve vysílání a streamovacími službami) k měření skutečné vnímané hlasitosti každé skladby a jejímu jemnému nasměrování ke konzistentnímu cíli.

Na rozdíl od ReplayGain **nevyžaduje** žádné značky ve vašich souborech a **neupravuje** váš zvuk. Funguje v reálném čase na čemkoli, co přehráváte, včetně cloudových streamů a živého rádia, a čistě se resetuje, když převíjíte nebo měníte skladby.

Čtyři předvolby pokrývají běžné případy:

- **Jemná** – mírné vyrovnání (cíl −20 LUFS).
- **Standardní** – výchozí, hlasitost ve stylu streamovacích služeb (cíl −16 LUFS, až +12 dB zvednutí u tichých skladeb).
- **Silná** – agresivní sladění pro velmi smíšené knihovny (cíl −14 LUFS).
- **Noční** – tišší a konzistentní pro tichý večerní poslech (cíl −23 LUFS).

Už nemusíte mezi skladbami sahat po hlasitosti.

## Přepracovaný ekvalizér

**10pásmový grafický ekvalizér** Evermusic dostal kompletní redesign. Pásma pokrývají **32 Hz až 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), každé nastavitelné od **−12 dB do +12 dB** v jemných krocích po 0,1 dB, s **předzesilovačem** od −24 dB do +24 dB, který zabraňuje ořezání při zvýraznění.

Co je nového v 8.7:

- **Nové posuvníky** – přesné, citlivé ovládací prvky, které přejímají vzhled nativního systémového posuvníku z iOS 26 a materiál **Liquid Glass**.
- **Rychlejší, plynulejší přepínání předvoleb** – přeskakujte mezi předvolbami okamžitě, s přepracovanou vodorovnou lištou předvoleb na výšku a svislým sloupcem předvoleb na šířku.
- **Lepší rozložení na šířku a na iPadu** – posuvníky a výběr předvoleb se přeuspořádají, aby využily šířku navíc místo natěsnání do sloupce velikosti telefonu.
- **Vlastní předvolby** – vytvářejte a ukládejte vlastní křivky, měňte jejich pořadí a **importujte a exportujte** předvolby jako soubory `.eqp`, abyste je přenášeli mezi zařízeními nebo sdíleli.

Ekvalizér běží nativně v enginu (`AVAudioUnitEQ`), takže se použije na každý zdroj, a funguje také přes AirPlay, Chromecast a CarPlay tam, kde je to podporováno.

## Přestavěný přehrávací engine

Pod kapotou běží Evermusic 8.7 na **přestavěném streamovacím enginu** postaveném na `AVAudioEngine` od Applu s vlastní vykreslovací pipeline. To je to, co umožňuje předání bez mezer, řetězec efektů a ekvalizér, a také to činí každodenní přehrávání spolehlivějším.

- **Lepší podpora formátů** – včetně **FLAC** (přes Core Audio) a **Ogg Vorbis** (přes `libvorbisfile`), vedle MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF a dalších.
- **Chytřejší vyrovnávání do paměti** – adaptivní předběžná vyrovnávací paměť se škáluje podle vašeho připojení a souvislá kruhová vyrovnávací paměť napájí výstup, takže se krátké výpadky sítě nepromění ve výpadky přehrávání.
- **Automatické zotavení** – stavový automat opětovného vyrovnávání a logika opakování s odstupem čistě obnoví přehrávání po chvíli slabého signálu místo zastavení skladby.
- **Méně přerušení** – stejný engine pohání místní soubory, cloudové streamy, mediální servery i internetové rádio, takže chování je všude konzistentní.

## Právě se přehrává a CarPlay

Obrazovky, na které se při poslechu skutečně díváte – **zamykací obrazovka**, **CarPlay** a tlačítka ovladačů v autě nebo na sluchátkách – jsou v 8.7 přesnější a rychlejší.

- **Přesnější informace v Právě se přehrává.** Evermusic zachytí stav přehrávače pod zámkem, než ho zveřejní, takže si název, uplynulý čas, délka a stav přehrávání/pauzy nemohou na zamykací obrazovce nebo v autě navzájem odporovat. Stavy vyrovnávání a načítání se nyní hlásí správně místo zobrazení „přehrává se“, zatímco se skladba ještě načítá.
- **Spolehlivé dálkové ovládání.** Přehrát, pauza, další, předchozí, převíjení, přeskočit, náhodné pořadí, opakovat a rychlost přehrávání – vše reaguje konzistentně z tlačítek sluchátek, ovladačů v autě a zamykací obrazovky, pod řízením `MPRemoteCommandCenter`.
- **Rychlejší obaly v CarPlay.** Obaly alb se nyní načítají několikanásobně rychleji v dlouhých seznamech (dávkování zrychleno z 1,0 s na 0,25 s, přičemž první viditelná obrazovka se načte okamžitě) a nyní se objevují v kompaktních řádcích seznamu CarPlay v iOS 26, které dříve žádný obal nezobrazovaly.
- **Opravy řazení a stability v CarPlay.** Rychlejší řazení u velkých knihoven a odolnost proti pádům v hraničních případech při procházení dlouhých seznamů.
- **Omezené aktualizace metadat.** Aktualizace Právě se přehrává a dálkových příkazů jsou omezeny, aby rychlé změny už nezahlcovaly systém, což udržuje ovládací prvky zamykací obrazovky a CarPlay pohotové.

## Další vylepšení

- **Vylepšení designu Liquid Glass** napříč aplikací – průsvitné plochy, plynulejší animace a zjemněné ovládací prvky na iOS, iPadOS a macOS.
- **Nové widgety plochy** s vylepšenou logikou aktualizace, která je udržuje synchronizované bez zbytečného vybíjení baterie.
- Opravy pro nedávná vydání iOS.
- Opravy lokalizace v několika jazycích.
- Mnoho menších vylepšení na základě vašich e-mailů a recenzí v App Store.

## Proč na této aktualizaci záleží

Evermusic 8.7 je postaven kolem jediné myšlenky: **vaše hudba by měla znít co nejlépe, z jakéhokoli zdroje.**

1. **Celá alba, tak jak byla zamýšlena.** Skutečné přehrávání bez mezer znamená, že živé sety, DJ mixy a koncepční alba konečně hrají tak, jak je umělec masteroval.
2. **Studio v kapse.** Dozvuk, echo, zkreslení, kompresor, crossfeed, přepracovaný ekvalizér a normalizace hlasitosti vám dávají skutečnou kontrolu nad vaším zvukem, ne jen přepínač zapnuto/vypnuto.
3. **Stejný zážitek všude.** Místní soubory, cloudové disky, mediální servery i internetové rádio procházejí stejným přestavěným enginem, s přesným Právě se přehrává a rychlejším CarPlay navrch.

## Získejte Evermusic 8.7

[**Stáhněte si Evermusic z App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) nebo aktualizujte přímo z App Store. Evermusic je zdarma ke stažení s volitelnými vylepšeními v aplikaci pro pokročilé funkce.

Pokud vás aplikace baví, zanechte prosím hodnocení v App Store – opravdu to pomáhá. Máte zpětnou vazbu nebo jste narazili na problém? Napište nám na **support@everappz.com**. Čteme každou zprávu.

## Časté dotazy

{{% details title="Co je nového v Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 přidává skutečné přehrávání bez mezer, pět studiových zvukových efektů (dozvuk, echo, zkreslení, kompresor a crossfeed), normalizaci hlasitosti EBU R128, přepracovaný 10pásmový ekvalizér s vlastními předvolbami a importem/exportem, přestavěný streamovací engine AVAudioEngine s lepší podporou formátů (včetně FLAC a Ogg Vorbis), rychlejší a přesnější CarPlay a Právě se přehrává, aktualizace designu Liquid Glass, přepracované widgety plochy a opravy chyb a lokalizace.
{{% /details %}}

{{% details title="Má Evermusic skutečné přehrávání bez mezer?" closed="true" %}}
Ano. Počínaje Evermusic 8.7 je přehrávání skutečně bez mezer: mezi skladbami není žádná pauza, lupnutí ani cvaknutí. Engine předem vyrovná do paměti a dekóduje následující skladbu, zatímco aktuální hraje, a předá řízení mezi zvukovými vzorky na souvislé kruhové vyrovnávací paměti, takže přechod je neslyšitelný. Funguje s místními soubory, cloudovými streamy a mediálními servery a je ideální pro živá alba, DJ mixy a koncepční alba.
{{% /details %}}

{{% details title="Jaké zvukové efekty Evermusic 8.7 obsahuje?" closed="true" %}}
Pět efektů v reálném čase: **dozvuk** (13 předvoleb místností, mokrý/suchý mix), **echo** (10 předvoleb s dobou echa, zpětnou vazbou, dolní propustí a mixem), **zkreslení** (22 charakterových předvoleb s předzesílením a mixem), **kompresor** (plnohodnotný dynamický procesor s prahem, poměrem, nástupem, uvolněním, expanzí a kompenzačním zesílením plus 10 předvoleb) a **crossfeed** (crossfeed pro sluchátka Bauer bs2b s ovládáním úrovně a mezní frekvence a 6 předvolbami). Každý efekt přichází s pečlivě sestavenými předvolbami a vaše vlastní nastavení se pamatuje mezi relacemi.
{{% /details %}}

{{% details title="Co je crossfeed a proč bych ho použil?" closed="true" %}}
Crossfeed přimíchá malé, filtrované množství každého stereo kanálu do druhého, tak jak vaše uši přirozeně slyší skutečné reproduktory v místnosti. Ve sluchátkách to zmírní přehnané, „v hlavě“ znějící oddělení u nahrávek s krajním panoramatem a učiní dlouhý poslech pohodlnějším. Evermusic používá známý algoritmus Bauer stereophonic-to-binaural (bs2b) a obsahuje předvolby jako Chu Moy a Jan Meier. Je zvlášť účinný u starších stereo mixů ze 60. a 70. let.
{{% /details %}}

{{% details title="Jak funguje normalizace hlasitosti v Evermusic?" closed="true" %}}
Evermusic 8.7 měří vnímanou hlasitost každé skladby pomocí standardu EBU R128 (ITU-R BS.1770) v reálném čase a jemně upravuje úroveň směrem ke konzistentnímu cíli, aby skladby neskákaly v hlasitosti. Nevyžaduje značky ReplayGain a neupravuje vaše soubory. K dispozici jsou čtyři předvolby – Jemná (−20 LUFS), Standardní (−16 LUFS), Silná (−14 LUFS) a Noční (−23 LUFS) – a normalizace se čistě resetuje, když převíjíte nebo měníte skladby.
{{% /details %}}

{{% details title="Je normalizace hlasitosti v Evermusic totéž co ReplayGain?" closed="true" %}}
Dosahuje stejného cíle – konzistentní hlasitosti mezi skladbami – ale funguje jinak. ReplayGain se spoléhá na hlasitostní značky uložené uvnitř vašich souborů. Normalizátor Evermusic měří hlasitost živě pomocí EBU R128, takže funguje na jakémkoli zdroji, včetně cloudových streamů a internetového rádia, i když soubory nemají vůbec žádné značky.
{{% /details %}}

{{% details title="Kolik pásem má ekvalizér Evermusic a můžu si vytvořit vlastní předvolby?" closed="true" %}}
Ekvalizér Evermusic je 10pásmový grafický ekvalizér pokrývající 32 Hz až 16 kHz, s každým pásmem nastavitelným od −12 dB do +12 dB v krocích po 0,1 dB a předzesilovačem od −24 dB do +24 dB. Obsahuje vestavěné předvolby, umožňuje vytvářet a ukládat vlastní předvolby a podporuje import a export předvoleb jako souborů .eqp, abyste je mohli přenášet nebo sdílet mezi zařízeními.
{{% /details %}}

{{% details title="Co se změnilo v ekvalizéru Evermusic 8.7?" closed="true" %}}
Ekvalizér byl přepracován s novými, přesnějšími posuvníky, které přejímají vzhled systémového posuvníku z iOS 26 a Liquid Glass, s rychlejším a plynulejším přepínáním předvoleb a lepším rozložením na šířku a na iPadu (vodorovná lišta předvoleb na výšku a svislý sloupec předvoleb na šířku). Podporovány jsou vlastní předvolby a import/export .eqp.
{{% /details %}}

{{% details title="Podporuje Evermusic 8.7 FLAC a Ogg Vorbis?" closed="true" %}}
Ano. Přestavěný engine přehrává FLAC (přes Core Audio) a Ogg Vorbis (přes libvorbisfile), spolu s MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF a dalšími, z místních souborů, cloudových disků a mediálních serverů.
{{% /details %}}

{{% details title="Co se zlepšilo v CarPlay a na zamykací obrazovce?" closed="true" %}}
Obaly alb v CarPlay se načítají několikanásobně rychleji v dlouhých seznamech a nyní se objevují v kompaktních řádcích seznamu iOS 26, které dříve žádný nezobrazovaly. Informace Právě se přehrává na zamykací obrazovce a v CarPlay jsou přesnější – název, uplynulý čas, délka a stav přehrávání/pauzy se zachytávají společně, takže si nemohou odporovat, a stavy vyrovnávání se hlásí správně. Dálkové ovládání (přehrát, pauza, další, předchozí, převíjení, náhodné pořadí, opakovat, rychlost) reaguje spolehlivě ze sluchátek a auta a řazení CarPlay u velkých knihoven je rychlejší.
{{% /details %}}

{{% details title="Fungují zvukové efekty a ekvalizér s cloudovým streamováním a CarPlay?" closed="true" %}}
Ano. Efekty, ekvalizér a normalizace hlasitosti běží nativně uvnitř přehrávacího enginu, takže se použijí na vše, co Evermusic přehrává – místní soubory, cloudové disky, mediální servery a internetové rádio – a fungují dál i během přehrávání přes CarPlay a tam, kde je to podporováno, přes AirPlay a Chromecast.
{{% /details %}}

{{% details title="Je Evermusic 8.7 aktualizace zdarma a jaká zařízení podporuje?" closed="true" %}}
Ano. Evermusic je zdarma ke stažení z App Store a 8.7 je bezplatná aktualizace pro stávající uživatele s volitelnými vylepšeními v aplikaci pro pokročilé funkce. Běží na iPhonu, iPadu a Macu. CarPlay vyžaduje vozidlo nebo autorádio kompatibilní s CarPlay.
{{% /details %}}
