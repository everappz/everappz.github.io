---
title: "Evermusic 8.7: skutočné prehrávanie bez medzier, zvukové efekty, normalizácia hlasitosti, prepracovaný ekvalizér"
date: 2026-07-05
description: "Evermusic 8.7 pre iPhone, iPad a Mac pridáva skutočné prehrávanie bez medzier, päť štúdiových zvukových efektov (reverb, delay, skreslenie, kompresor, crossfeed), normalizáciu hlasitosti EBU R128, prepracovaný 10-pásmový ekvalizér s importom/exportom predvolieb, prestavaný streamovací engine AVAudioEngine s podporou FLAC a Ogg Vorbis a rýchlejšie, presnejšie CarPlay a Práve hrá."
keywords: ["Evermusic 8.7", "aktualizácia Evermusic", "skutočné prehrávanie bez medzier iPhone", "gapless prehrávač hudby iOS", "prehrávanie bez medzier CarPlay", "zvukové efekty prehrávača hudby iPhone", "reverb delay skreslenie kompresor crossfeed iOS", "crossfeed slúchadlá iOS", "normalizácia hlasitosti iPhone", "normalizácia hlasitosti prehrávač hudby", "normalizácia EBU R128 iOS", "alternatíva k replay gain iPhone", "10-pásmový ekvalizér iPhone", "grafický ekvalizér iOS aplikácia", "import export predvolieb ekvalizéra", "FLAC prehrávač iPhone", "Ogg Vorbis prehrávač iOS", "bezstratový prehrávač hudby iPhone 2026", "AVAudioEngine prehrávač hudby", "CarPlay prehrávač hudby iPhone", "presnosť Práve hrá na uzamknutej obrazovke", "cloudový prehrávač hudby iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Prehrávanie bez medzier", "Zvukové efekty", "Reverb", "Delay", "Skreslenie", "Kompresor", "Crossfeed", "Normalizácia hlasitosti", "EBU R128", "Ekvalizér", "FLAC", "Ogg Vorbis", "CarPlay", "Práve hrá", "Liquid Glass", "Novinky"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Zhrnutie:** [Evermusic 8.7](/products/evermusic) je vydanie zamerané na kvalitu zvuku pre iPhone, iPad a Mac. Prináša **skutočné prehrávanie bez medzier** (žiadne pauzy, cvaknutia či kliknutia medzi skladbami), kompletnú sadu **štúdiových zvukových efektov** — reverb, delay, skreslenie, kompresor a crossfeed — a **normalizáciu hlasitosti EBU R128**, ktorá udržiava konzistentnú hlasitosť od skladby ku skladbe bez značiek ReplayGain. **10-pásmový ekvalizér** je prepracovaný s novými posuvníkmi, rýchlejším prepínaním predvolieb, vlastnými predvoľbami, ktoré môžete importovať a exportovať, a lepším rozložením na šírku a na iPade. Pod kapotou **prestavaný streamovací engine AVAudioEngine** zlepšuje spoľahlivosť a podporu formátov, vrátane **FLAC** a **Ogg Vorbis**. **CarPlay** a **Práve hrá** sú rýchlejšie a presnejšie na uzamknutej obrazovke, v aute aj z diaľkových ovládačov slúchadiel.

---

## Zdravím všetkých!

Evermusic 8.7 je k dispozícii na stiahnutie. Táto aktualizácia je celá o tom, ako vaša hudba *znie*. Prestavali sme prehrávací engine pre skutočné prehrávanie bez medzier, pridali sadu štúdiových zvukových efektov, zaviedli normalizáciu hlasitosti a prepracovali ekvalizér od posuvníkov nahor. Všetko je zabalené do nového dizajnu Apple **Liquid Glass**.

[Stiahnite si Evermusic 8.7 z App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) alebo aktualizujte z existujúcej verzie. Evermusic je bezplatné stiahnutie s voliteľnými upgradmi v aplikácii.

## Skutočné prehrávanie bez medzier

Prehrávanie bez medzier znamená, že ticho medzi dvoma skladbami je preč. Žiadna pauza, žiadne cvaknutie, žiadne kliknutie — aktuálna skladba plynie priamo do nasledujúcej. Najviac záleží na hudbe, ktorá bola navrhnutá tak, aby sa počúvala ako celok: **živé nahrávky, DJ mixy, klasické diela a koncepčné albumy**, kde jedna skladba prechádza priamo do druhej.

Tu je, čo sa zmenilo technicky. Zvukový engine Evermusic udržiava dve skladby v hre naraz: tú, ktorú počujete, a nasledujúcu vo fronte. Kým aktuálna skladba hrá, nasledujúca skladba sa už na pozadí **načítava, dekóduje a vopred bufferuje**. Keď aktuálna skladba dosiahne svoj koniec, engine odovzdá riadenie nasledujúcej skladbe **vnútri prehrávača, nie vnútri zvukového streamu**. Vykresľovacia slučka výstupu neustále odoberá zvukové vzorky zo súvislého kruhového bufferu bez toho, aby sa kedy zastavila, takže poslucháč nikdy nepočuje prechod. Prepnutie nastane medzi vzorkami, čo je presne dôvod, prečo nie je počuteľná žiadna medzera.

Funguje to rovnako, či už je súbor vo vašom zariadení, v cloude alebo na mediálnom serveri — pri vzdialených zdrojoch sa predbufferovanie len začne o niečo skôr.

## Štúdiové zvukové efekty

Evermusic 8.7 pridáva päť zvukových efektov v reálnom čase, ktoré môžete navrstviť na svoju hudbu. Každý z nich beží ako natívny uzol na spracovanie zvuku v prehrávacom engine, takže sa uplatňuje na všetko, čo prehrávate — lokálne súbory, cloudové streamy aj internetové rádio — bez prekódovania.

Každý efekt sa dodáva s **kurátorovanou knižnicou predvolieb**, aby ste získali skvelý zvuk jedným ťuknutím, a Evermusic si **pamätá vaše presné nastavenia** medzi reláciami. Upravte ktorýkoľvek ovládací prvok a efekt sa prepne do stavu **Manuálne**, takže vždy viete, kedy ste sa odklonili od predvoľby.

### Reverb

Pridáva pocit priestoru, od tesnej miestnosti po katedrálu. Postavený na Apple `AVAudioUnitReverb` ponúka **13 predvolieb miestností** (Small Room, Medium Hall, Plate, Cathedral a ďalšie) plus ovládanie **mixu wet/dry** od 0 do 100 %, takže rozhodujete, koľko priestoru pridať.

### Delay (echo)

Klasické echo s **10 predvoľbami** — Slapback, Tape Echo, Dub, Ambient a ďalšie. Môžete nastaviť **čas oneskorenia** (až 2 sekundy), **feedback** (počet opakovaní), **low-pass cutoff** na zohriatie opakovaní a **mix wet/dry**.

### Skreslenie

Od jemnej zrnitosti po plnú lo-fi deštrukciu, poháňané `AVAudioUnitDistortion` s **22 charakterovými predvoľbami** (Bit Brush, Cellphone Concert, Radio Tower a ďalšie), ovládaním jazdy **pre-gain** a mixom wet/dry, takže môžete efekt zmiešať späť do čistého signálu.

### Kompresor

Dynamický procesor (Apple `AUDynamicsProcessor`), ktorý vyrovnáva hlasné a tiché pasáže. Sprístupňuje kompletnú profesionálnu sadu ovládacích prvkov — **threshold, ratio/headroom, attack, release, expansion a makeup gain** — s **10 predvoľbami** naladenými na reálne situácie: okrem iného Voice / Podcast, Late Night, Movie Dialog, Streaming Match a Maximum Loudness.

### Crossfeed

Crossfeed spôsobuje, že počúvanie cez slúchadlá znie prirodzenejšie tým, že mieša trochu ľavého kanálu do pravého a naopak, tak ako vaše uši počujú skutočné reproduktory. Je postavený na známom algoritme **Bauer stereophonic-to-binaural (bs2b)**, s ovládaním **úrovne crossfeedu** a **medznej frekvencie**, a **6 predvoľbami** vrátane audiofilsky obľúbených nastavení *Chu Moy* a *Jan Meier*. Je obzvlášť dobrý pri starších, tvrdo panorámovaných stereo mixoch zo 60. a 70. rokov.

## Normalizácia hlasitosti

Zostavili ste niekedy playlist, kde jedna skladba hučí a nasledujúca je šepot? Normalizácia hlasitosti to napraví. Evermusic 8.7 používa **meranie hlasitosti EBU R128** (ten istý štandard ITU-R BS.1770 používaný vo vysielaní a streamovacími službami) na meranie skutočnej vnímanej hlasitosti každej skladby a jej jemné nasmerovanie ku konzistentnému cieľu.

Na rozdiel od ReplayGain **nevyžaduje** žiadne značky vo vašich súboroch a **nemení** váš zvuk. Funguje v reálnom čase na čomkoľvek, čo prehrávate, vrátane cloudových streamov a živého rádia, a čisto sa resetuje, keď pretáčate alebo meníte skladby.

Štyri predvoľby pokrývajú bežné prípady:

- **Light** — jemné vyrovnávanie (cieľ −20 LUFS).
- **Standard** — predvolená, hlasitosť v štýle streamovania (cieľ −16 LUFS, až +12 dB nadvihnutia pre tiché skladby).
- **Strong** — agresívne prispôsobenie pre veľmi zmiešané knižnice (cieľ −14 LUFS).
- **Night** — tichšie a konzistentné pre počúvanie s nízkou hlasitosťou večer (cieľ −23 LUFS).

Už nemusíte siahať po hlasitosti medzi skladbami.

## Prepracovaný ekvalizér

**10-pásmový grafický ekvalizér** Evermusic dostal kompletný redizajn. Pásma pokrývajú **32 Hz až 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), každé nastaviteľné od **−12 dB do +12 dB** v jemných krokoch po 0,1 dB, s **predzosilnením** od −24 dB do +24 dB na zabránenie orezaniu pri zosilnení.

Čo je nové v 8.7:

- **Nové posuvníky** — presné, responzívne ovládacie prvky, ktoré preberajú natívny vzhľad systémového posuvníka iOS 26 a materiál **Liquid Glass**.
- **Rýchlejšie, plynulejšie prepínanie predvolieb** — skáčte medzi predvoľbami okamžite, s prepracovanou horizontálnou lištou predvolieb na výšku a vertikálnym stĺpcom predvolieb na šírku.
- **Lepšie rozloženie na šírku a na iPade** — posuvníky a výber predvolieb sa preusporiadajú tak, aby využili šírku navyše, namiesto natláčania do stĺpca veľkosti telefónu.
- **Vlastné predvoľby** — vytvárajte a ukladajte si vlastné krivky, meňte ich poradie a **importujte a exportujte** predvoľby ako súbory `.eqp`, aby ste ich preniesli medzi zariadeniami alebo zdieľali.

Ekvalizér beží natívne v engine (`AVAudioUnitEQ`), takže sa uplatňuje na každý zdroj, a funguje aj cez AirPlay, Chromecast a CarPlay, kde je to podporované.

## Prestavaný prehrávací engine

Pod kapotou beží Evermusic 8.7 na **prestavanom streamovacom engine** postavenom na Apple `AVAudioEngine` s vlastnou vykresľovacou pipeline. Práve to umožňuje odovzdanie bez medzier, reťazec efektov a ekvalizér, a robí to aj bežné prehrávanie spoľahlivejším.

- **Zlepšená podpora formátov** — vrátane **FLAC** (cez Core Audio) a **Ogg Vorbis** (cez `libvorbisfile`), popri MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF a ďalších.
- **Inteligentnejšie bufferovanie** — adaptívny predbuffer sa škáluje podľa vášho pripojenia, so súvislým kruhovým bufferom napájajúcim výstup, takže krátke sieťové výpadky sa nezmenia na výpadky zvuku.
- **Automatické zotavenie** — stavový automat opätovného bufferovania a logika opakovania s odloženým resetom čisto obnovia prehrávanie po chvíli slabého signálu namiesto zastavenia skladby.
- **Menej prerušení** — ten istý engine poháňa lokálne súbory, cloudové streamy, mediálne servery a internetové rádio, takže správanie je všade konzistentné.

## Práve hrá a CarPlay

Obrazovky, na ktoré sa počas počúvania skutočne pozeráte — **uzamknutá obrazovka**, **CarPlay** a tlačidlá diaľkového ovládania vášho auta či slúchadiel — sú v 8.7 presnejšie a rýchlejšie.

- **Presnejšie informácie Práve hrá.** Evermusic zachytáva stav prehrávača pod zámkom pred jeho zverejnením, takže názov, uplynutý čas, dĺžka a stav prehrávanie/pauza si nikdy nemôžu navzájom protirečiť na uzamknutej obrazovke ani v aute. Stavy bufferovania a načítavania sa teraz hlásia správne namiesto zobrazovania „prehráva sa“, kým sa skladba ešte načítava.
- **Spoľahlivé diaľkové ovládanie.** Prehrávanie, pauza, ďalej, späť, pretáčanie, preskočenie, náhodné poradie, opakovanie a rýchlosť prehrávania reagujú konzistentne z tlačidiel slúchadiel, ovládačov auta a uzamknutej obrazovky, poháňané `MPRemoteCommandCenter`.
- **Rýchlejší obal albumu v CarPlay.** Obal albumu sa teraz načítava niekoľkonásobne rýchlejšie v dlhých zoznamoch (dávkové tempo znížené z 1,0 s na 0,25 s, pričom prvá viditeľná obrazovka sa načíta okamžite) a teraz sa objavuje aj v kompaktných riadkoch zoznamu CarPlay v iOS 26, ktoré predtým nezobrazovali žiadny obal.
- **Opravy triedenia a stability CarPlay.** Rýchlejšie triedenie vo veľkých knižniciach a spevnenie proti okrajovým pádom pri posúvaní dlhých zoznamov.
- **Obmedzené aktualizácie metadát.** Aktualizácie Práve hrá a diaľkových príkazov sú obmedzené, takže rýchle zmeny už nezahlcujú systém, čím sa udržiava responzívnosť ovládania na uzamknutej obrazovke a v CarPlay.

## Ďalšie vylepšenia

- **Vylepšenia dizajnu Liquid Glass** naprieč aplikáciou — priesvitné povrchy, plynulejšie animácie a vylepšené ovládacie prvky na iOS, iPadOS a macOS.
- **Nové widgety na plochu** s vylepšenou logikou aktualizácie, ktorá ich udržiava synchronizované bez zbytočného vybíjania batérie.
- Opravy pre nedávne vydania iOS.
- Opravy lokalizácie naprieč viacerými jazykmi.
- Množstvo menších vylepšení na základe vašich e-mailov a recenzií na App Store.

## Prečo je táto aktualizácia dôležitá

Evermusic 8.7 je postavený okolo jednej myšlienky: **vaša hudba by mala znieť čo najlepšie na akomkoľvek zdroji.**

1. **Celé albumy, tak ako boli zamýšľané.** Skutočné prehrávanie bez medzier znamená, že živé sety, DJ mixy a koncepčné albumy konečne hrajú tak, ako ich umelec masteroval.
2. **Štúdio vo vrecku.** Reverb, delay, skreslenie, kompresor, crossfeed, prepracovaný ekvalizér a normalizácia hlasitosti vám dávajú skutočnú kontrolu nad vaším zvukom, nie len prepínač zap/vyp.
3. **Rovnaký zážitok všade.** Lokálne súbory, cloudové disky, mediálne servery a internetové rádio bežia cez ten istý prestavaný engine, s presným Práve hrá a rýchlejším CarPlay navrch.

## Získajte Evermusic 8.7

[**Stiahnite si Evermusic z App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) alebo aktualizujte priamo v App Store. Evermusic je bezplatné stiahnutie s voliteľnými upgradmi v aplikácii pre pokročilé funkcie.

Ak sa vám aplikácia páči, zanechajte prosím hodnotenie na App Store — naozaj to pomáha. Máte spätnú väzbu alebo ste narazili na problém? Napíšte nám na **support@everappz.com**. Čítame každú správu.

## Často kladené otázky

{{% details title="Čo je nové v Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 pridáva skutočné prehrávanie bez medzier, päť štúdiových zvukových efektov (reverb, delay, skreslenie, kompresor a crossfeed), normalizáciu hlasitosti EBU R128, prepracovaný 10-pásmový ekvalizér s vlastnými predvoľbami a importom/exportom, prestavaný streamovací engine AVAudioEngine so zlepšenou podporou formátov (vrátane FLAC a Ogg Vorbis), rýchlejšie a presnejšie CarPlay a Práve hrá, aktualizácie dizajnu Liquid Glass, obnovené widgety na plochu a opravy chýb a lokalizácie.
{{% /details %}}

{{% details title="Má Evermusic skutočné prehrávanie bez medzier?" closed="true" %}}
Áno. Počnúc Evermusic 8.7 je prehrávanie skutočne bez medzier: medzi skladbami nie je žiadna pauza, cvaknutie ani kliknutie. Engine vopred bufferuje a dekóduje nasledujúcu skladbu, kým aktuálna hrá, a odovzdá riadenie medzi zvukovými vzorkami na súvislom kruhovom bufferi, takže je prechod nepočuteľný. Funguje pre lokálne súbory, cloudové streamy a mediálne servery a je ideálny pre živé albumy, DJ mixy a koncepčné albumy.
{{% /details %}}

{{% details title="Aké zvukové efekty obsahuje Evermusic 8.7?" closed="true" %}}
Päť efektov v reálnom čase: **reverb** (13 predvolieb miestností, mix wet/dry), **delay/echo** (10 predvolieb s časom oneskorenia, feedbackom, low-pass a mixom), **skreslenie** (22 charakterových predvolieb s pre-gain a mixom), **kompresor** (plnohodnotný dynamický procesor s thresholdom, ratiom, attackom, releasom, expansiou a makeup gainom, plus 10 predvolieb) a **crossfeed** (crossfeed pre slúchadlá Bauer bs2b s ovládaním úrovne a cutoffu a 6 predvoľbami). Každý efekt sa dodáva s kurátorovanými predvoľbami a vaše vlastné nastavenia sa pamätajú medzi reláciami.
{{% /details %}}

{{% details title="Čo je crossfeed a prečo by som ho použil?" closed="true" %}}
Crossfeed mieša malé, filtrované množstvo každého stereo kanálu do toho druhého, tak ako vaše uši prirodzene počujú skutočné reproduktory v miestnosti. Na slúchadlách to znižuje prehnané, „vo vašej hlave“ oddelenie tvrdo panorámovaných nahrávok a robí dlhé počúvanie pohodlnejším. Evermusic používa známy algoritmus Bauer stereophonic-to-binaural (bs2b) a obsahuje predvoľby ako Chu Moy a Jan Meier. Je obzvlášť účinný pri starších stereo mixoch zo 60. a 70. rokov.
{{% /details %}}

{{% details title="Ako funguje normalizácia hlasitosti v Evermusic?" closed="true" %}}
Evermusic 8.7 meria vnímanú hlasitosť každej skladby pomocou štandardu EBU R128 (ITU-R BS.1770) v reálnom čase a jemne prispôsobuje úroveň smerom ku konzistentnému cieľu, takže skladby neskáču v hlasitosti. Nevyžaduje značky ReplayGain a nemení vaše súbory. K dispozícii sú štyri predvoľby — Light (−20 LUFS), Standard (−16 LUFS), Strong (−14 LUFS) a Night (−23 LUFS) — a normalizácia sa čisto resetuje, keď pretáčate alebo meníte skladby.
{{% /details %}}

{{% details title="Je normalizácia hlasitosti Evermusic to isté ako ReplayGain?" closed="true" %}}
Dosahuje rovnaký cieľ — konzistentnú hlasitosť medzi skladbami — ale funguje inak. ReplayGain sa spolieha na značky hlasitosti uložené vnútri vašich súborov. Normalizátor Evermusic meria hlasitosť živo pomocou EBU R128, takže funguje na akomkoľvek zdroji, vrátane cloudových streamov a internetového rádia, aj keď súbory nemajú žiadne značky.
{{% /details %}}

{{% details title="Koľko pásiem má ekvalizér Evermusic a môžem si vytvoriť vlastné predvoľby?" closed="true" %}}
Ekvalizér Evermusic je 10-pásmový grafický ekvalizér pokrývajúci 32 Hz až 16 kHz, s každým pásmom nastaviteľným od −12 dB do +12 dB v krokoch po 0,1 dB a predzosilnením od −24 dB do +24 dB. Obsahuje vstavané predvoľby, umožňuje vytvárať a ukladať vlastné predvoľby a podporuje import a export predvolieb ako súbory .eqp, takže ich môžete presúvať alebo zdieľať medzi zariadeniami.
{{% /details %}}

{{% details title="Čo sa zmenilo v ekvalizéri Evermusic 8.7?" closed="true" %}}
Ekvalizér bol prepracovaný s novými, presnejšími posuvníkmi, ktoré preberajú vzhľad systémového posuvníka iOS 26 a Liquid Glass, rýchlejším a plynulejším prepínaním predvolieb a lepším rozložením na šírku a na iPade (horizontálna lišta predvolieb na výšku a vertikálny stĺpec predvolieb na šírku). Podporované sú vlastné predvoľby a import/export .eqp.
{{% /details %}}

{{% details title="Podporuje Evermusic 8.7 FLAC a Ogg Vorbis?" closed="true" %}}
Áno. Prestavaný engine prehráva FLAC (cez Core Audio) a Ogg Vorbis (cez libvorbisfile), spolu s MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF a ďalšími, z lokálnych súborov, cloudových diskov a mediálnych serverov.
{{% /details %}}

{{% details title="Čo sa zlepšilo v CarPlay a na uzamknutej obrazovke?" closed="true" %}}
Obal albumu v CarPlay sa načítava niekoľkonásobne rýchlejšie v dlhých zoznamoch a teraz sa objavuje aj v kompaktných riadkoch zoznamu iOS 26, ktoré predtým žiadny nezobrazovali. Informácie Práve hrá na uzamknutej obrazovke a v CarPlay sú presnejšie — názov, uplynutý čas, dĺžka a stav prehrávanie/pauza sú zachytené spolu, takže si nemôžu protirečiť, a stavy bufferovania sa hlásia správne. Diaľkové ovládanie (prehrávanie, pauza, ďalej, späť, pretáčanie, náhodné poradie, opakovanie, rýchlosť) reaguje spoľahlivo zo slúchadiel a auta a triedenie CarPlay vo veľkých knižniciach je rýchlejšie.
{{% /details %}}

{{% details title="Fungujú zvukové efekty a ekvalizér s cloudovým streamovaním a CarPlay?" closed="true" %}}
Áno. Efekty, ekvalizér a normalizácia hlasitosti bežia natívne vnútri prehrávacieho enginu, takže sa uplatňujú na všetko, čo Evermusic prehráva — lokálne súbory, cloudové disky, mediálne servery a internetové rádio — a naďalej fungujú počas prehrávania cez CarPlay a, kde je to podporované, cez AirPlay a Chromecast.
{{% /details %}}

{{% details title="Je Evermusic 8.7 aktualizácia zadarmo a ktoré zariadenia podporuje?" closed="true" %}}
Áno. Evermusic je bezplatné stiahnutie z App Store a 8.7 je bezplatná aktualizácia pre existujúcich používateľov, s voliteľnými upgradmi v aplikácii pre pokročilé funkcie. Beží na iPhone, iPad a Mac. CarPlay vyžaduje vozidlo alebo hlavnú jednotku kompatibilnú s CarPlay.
{{% /details %}}
