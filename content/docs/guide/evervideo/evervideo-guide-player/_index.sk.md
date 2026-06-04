---
title: "Mediálny prehrávač"
date: 2020-02-01
lastmod: 2026-06-01
description: "Naučte sa používať mediálny prehrávač Evervideo na iPhone, iPad a Mac. Picture-in-Picture, hardvérovo akcelerované dekódovanie H.264 / HEVC, audio a video ekvalizéry, primárne a sekundárne titulky, výber audio a video stopy, škálovanie a rotácia videa, rýchlosť prehrávania, časovač spánku, AirPlay 2, Google Chromecast, RTSP streamy a kompaktný prehrávač vždy na obrazovke."
keywords: [
  "Evervideo sprievodca prehrávačom", "nastavenia prehrávača videa", "Evervideo ekvalizér",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "titulky videa iPhone", "externé SRT titulky",
  "prehrávač titulkov ASS SSA", "libass iOS",
  "duálne titulky učenie jazyka",
  "ekvalizér videa jas kontrast", "ekvalizér zvuku prehrávač videa",
  "zámok rotácie prehrávača videa", "režim škálovania videa iOS",
  "hardvérový dekodér H.264 iPhone", "hardvérový dekodér HEVC iPad",
  "rýchlosť prehrávania videa", "FFmpeg prehrávač videa iOS",
  "RTSP iPhone prehrávač", "kompaktný prehrávač videa",
  "VR 360 prehrávač videa iPhone"
]
tags: ["sprievodca", "evervideo", "prehrávač", "PiP", "titulky", "video ekvalizér"]
readingTime: 14
---


Mediálny prehrávač je hlavná obrazovka aplikácie, kde ovládate prehrávanie a väčšinu funkcií Evervideo. Prehráva video aj audio súbory a je postavený na vlastnom FFmpeg prehrávači s hardvérovo akcelerovaným dekódovaním H.264 a HEVC, ktoré zvláda náročnú prácu. Poďme preskúmať, ako ho používať.

## Prístup k mediálnemu prehrávači

Na prehrávač na celú obrazovku sa dostanete z kompaktného panela prehrávača. Na iPhone sedí kompaktný prehrávač v hornej časti hlavnej obrazovky. Na iPad a Mac je na ľavej strane (alebo v hornej časti hlavného panela). Ak chcete zbaliť prehrávač na celú obrazovku späť do kompaktného zobrazenia, klepnite na tlačidlo zatvoriť v pravom dolnom rohu alebo potiahnite nadol. Ak chcete kompaktný prehrávač úplne skryť, klepnite a potiahnite nadol ešte raz.

Kompaktný prehrávač zostáva viditeľný pri prehliadaní knižnice, správcu súborov alebo nastavení, takže nikdy nestratíte video pri hľadaní ďalšieho.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo mediálny prehrávač na celú obrazovku" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Podporované video a audio formáty

Evervideo prehráva prakticky každý moderný kontajner a kodek cez pribalený FFmpeg, s hardvérovo akcelerovaným dekódovaním H.264 a HEVC na podporovaných zariadeniach.

- **Video kontajnery:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — a mnohé ďalšie.
- **Video kodeky:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus prakticky každý iný kodek, ktorý FFmpeg podporuje.
- **Audio kodeky:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — a mnoho ďalších.
- **Formáty titulkov:** SRT, VTT (WebVTT), ASS / SSA a vložené textové alebo obrazové stopy titulkov.
- **Streamovacie protokoly:** HTTP / HTTPS, HLS (m3u8), RTSP (IP kamery a IPTV) a priame streamovanie súborov cez SMB / WebDAV / FTP / SFTP / NFS / DLNA.

To pokrýva prakticky každý video súbor, s ktorým sa pravdepodobne stretnete — vrátane MKV záznámov, RTSP streamov bezpečnostných kamier a AV1 webm stiahnutí z webu.

## Ovládacie prvky prehrávania

V dolnej časti obrazovky prehrávača uvidíte tlačidlá pre Prehrať, Pozastaviť, Ďalej a Predchádzajúci. Existujú aj voliteľné tlačidlá ako Preskočiť dopredu a Preskočiť dozadu (predvolene 10 sekúnd), ktoré môžete zapnúť v nastaveniach aplikácie. Podržte tlačidlá Ďalej / Predchádzajúci na rýchle preposielanie alebo pretáčanie. Potiahnite posúvač prehrávania na prechod na akúkoľvek pozíciu.

## Opakovanie a náhodné prehrávanie

Klepnutím na tlačidlo opakovania prechádzajte cez režimy opakovania:

- **Opakovať všetko** — opakuje každé video vo vašej fronte.
- **Opakovať jeden** — opakuje iba aktuálne video.
- **Opakovať stop** — pozastaví sa, keď aktuálne video skončí.
- **Bez opakovania** — prehráva frontu raz bez opakovania.

Použite tlačidlo **Náhodné prehrávanie** na náhodné usporiadanie videí vo fronte.

## Picture-in-Picture (PiP)

Na iPhone a iPad Evervideo plne podporuje Picture-in-Picture (PiP). Klepnite na ikonu PiP na obrazovke prehrávača alebo jednoducho presuňte Evervideo do pozadia — video pokračuje v prehrávaní v plávajúcom okne nad každou inou aplikáciou. Potiahnite plávajúce okno do ľubovoľného rohu; štipnite na zmenu veľkosti; klepnite raz na zobrazenie základných ovládacích prvkov prehrávanie / pauza / preskočiť; klepnite na malé tlačidlo rozbalenia na návrat do plného Evervideo.

PiP funguje s každým formátom videa, ktorý Evervideo prehráva, vrátane cloudových streamovaných súborov a RTSP streamov. PiP tiež pokračuje v behu, keď je váš telefón uzamknutý (závisí od nastavenia automatického uzamknutia).

## Kompaktný prehrávač

Kompaktný prehrávač je trvalý mini prehrávač, ktorý zostáva viditeľný v hornej časti každej obrazovky aplikácie pri prehliadaní knižnice, správcu súborov alebo nastavení. Klepnite naň na rozbalenie do prehrávača na celú obrazovku; potiahnite nadol na jeho opätovné zbalenie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nastavenia videa Evervideo z kompaktného prehrávača na hlavnej obrazovke" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Pre AirPlay klepnite na tlačidlo AirPlay na prehrávači. Evervideo podporuje AirPlay 2, takže môžete streamovať video na Apple TV, HomePod alebo akýkoľvek AirPlay 2-kompatibilný reproduktor alebo smart TV. V nastavení s viacerými AirPlay zariadeniami môžete smerovať zvuk na viacero prijímačov súčasne.

## Google Chromecast

Pre používateľov Google Cast sa na prehrávači zobrazí ikona Cast. Klepnutím na ňu si vyberte zariadenie a začnite castovanie. Uistite sa, že váš telefón a Cast prijímač sú v rovnakej Wi-Fi sieti. Nie každý kodek je podporovaný hardvérom Chromecast — niektoré súbory môžu potrebovať transkódovanie.

## RTSP live streamy

Evervideo môže priamo prehrávať zdroje RTSP — IP kamery, zvonkové kamery, IPTV streamy, broadcast zdroje a akákoľvek `rtsp://` URL. Pridajte stream ako RTSP pripojenie v Súbory → Online linky → Pridať link, potom klepnite naň na začatie sledovania. RTSP streamy fungujú v Picture-in-Picture, kompaktnom prehrávači a castujú cez AirPlay 2 a Chromecast rovnako ako bežné video.

## Výber audio stopy

Pre videá s viacerými audio stopami (komentár, alternatívne jazykové dabingy, réžijné stopy) klepnite na tlačidlo Viac akcií na prehrávači a vyberte Audio stopa — potom si vyberte stopu, ktorú chcete. Toto je nevyhnutné pre filmy v cudzom jazyku, BDMV / MKV súbory s viacerými dabingami a výukový obsah s komentárovými stopami.

## Výber video stopy

Niektoré video súbory obsahujú viaceré video streamy (viacuhlové Blu-ray, alternatívne strihy). Vyberte Video stopu z menu Viac akcií na prepínanie medzi nimi počas prehrávania.

## Titulky — interné a externé

Evervideo vám dáva jemnú kontrolu nad titulkami:

- **Stopa titulkov** — vyberte z stôp vložených do súboru.
- **Externé súbory titulkov** — načítajte súbory `.srt`, `.vtt`, `.ass` alebo `.ssa` z vášho zariadenia, iCloud Drive alebo akejkoľvek pripojenej cloudovej služby.
- **Renderovanie Libass** — pokročilé štýlovanie ASS / SSA (písma, farby, pozície, karaoke efekty) je správne renderované vďaka pribalenému libass.
- **Výber písma** — vyberte vlastné písmo pre primárne titulky a samostatné písmo pre sekundárne titulky. K dispozícii sú pribalené písma plus akékoľvek písmo nainštalované na vašom zariadení.

Všetko toto môžete nastaviť v Nastavenia → Titulky pred prehrávaním alebo použiť Viac akcií → Titulky z prehrávača na zmenu za behu.

## Audio ekvalizér

Evervideo obsahuje plnohodnotný audio ekvalizér na ladenie zvukovej stopy videa pre vaše slúchadlá, reproduktory alebo hi-fi zostavu. Klepnite na ikonu ekvalizéra na ovládači hlasitosti (alebo Akciu Audio ekvalizéra v menu Viac akcií prehrávača), zapnite ekvalizér prepínačom v pravom hornom rohu a buď vyberte preset alebo potiahnite posúvače pásiem na vytvorenie vlastného presetu. Vlastné presety môžu byť exportované a importované, takže ich môžete zdieľať naprieč zariadeniami alebo zálohovať.

## Video ekvalizér

Na ladenie obrazu Evervideo poskytuje dedikovaný video ekvalizér — upravte jas, kontrast, sýtosť a odtieň v reálnom čase počas prehrávania. Podobne ako audio ekvalizér, vlastné video presety môžu byť exportované a importované pre zdieľanie alebo zálohu. Použite ho na rozjasnenie tmavej scény za slnečného dňa, zvýšenie sýtosti na vyblednutom obsahu alebo zahriatie studeného farebného posunu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Video ekvalizér Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Režim škálovania videa

Vyberte, ako video vypĺňa obrazovku:

- **Prispôsobiť** — zachovajte pôvodný pomer strán; čierne pruhy tam, kde sú potrebné.
- **Vyplniť** — vyplňte celú obrazovku, ak je potrebné orezaním videa.
- **Roztiahnuť** — roztiahnite video na vyplnenie obrazovky, ak je potrebné skreslením.
- **Pôvodné** — zachovajte natívne rozlíšenie v 1:1.

## Rotácia videa

Pre videá nahrané s nesprávnou orientáciou vyberte **Viac akcií → Rotácia** a vyberte **0°**, **90°**, **180°** alebo **270°** na otočenie obrazu bez opustenia prehrávača.

## Hardvérové dekódovanie (H.264 a HEVC)

V Nastavenia → Prehrávač → Video môžete nezávisle zapnúť / vypnúť Hardvérové dekódovanie H.264 a Hardvérové dekódovanie H.265 (HEVC). Hardvérové dekódovanie je rýchlejšie, spotrebuje menej batérie a funguje chladnejšie — ale v zriedkavých prípadoch (poškodené súbory, exotické profily) možno budete musieť vypnúť hardvérové dekódovanie a zálohovať na softvérové FFmpeg dekódovanie. Evervideo vám to umožňuje urobiť súbor po súbore z menu Viac akcií prehrávača.

## VR 360° pohľad

Evervideo obsahuje VR / 360° pohľad pre sférické video súbory. Pri prehrávaní 360° videa môžete ťahať na pozeranie sa okolo, štipnúť na priblíženie a Evervideo bude skresľovať renderovanie v reálnom čase.

## Rýchlosť prehrávania

Klepnutím na ovládanie Rýchlosť na paneli nástrojov prehrávača zmeňte rýchlosť prehrávania — spomaľte ho na analýzu (0,25× alebo 0,5×) alebo zrýchlite ho pre tutoriály a prednášky (1,25×, 1,5×, 2× a až 3×). Klepnite na ikonu konfigurácie v pravom hornom rohu obrazovky Rýchlosť na prepnutie do presného režimu s jemnejšími úpravami. K dispozícii je aj korekcia výšky tónu pre každú stopu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Rýchlosť prehrávania Evervideo na hlavnom paneli nástrojov" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Fronta prehrávača

Ak chcete zobraziť frontu prehrávača, klepnite na tlačidlo fronty na prehrávači. Každé video vo fronte má viac akcií — klepnite na tri bodky na ich zobrazenie. Na zmenu poradia videa vo fronte použite indikátor poradenia pri názve a potiahnite ho na novú pozíciu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fronta prehrávania Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Časovač spánku

Otvorte Nastavenia → Prehrávač → Časovač spánku, zapnite ho a vyberte, ako dlho chcete pokračovať v prehrávaní pred automatickým zastavením. Tlačidlo Časovač spánku môžete tiež pridať priamo na hlavnú obrazovku prehrávača cez Nastavenia → Prehrávač → Personalizácia → Akcie hlavnej obrazovky.

## Záložky prehrávača

Uložte si miesto v dlhých videách — prednáškach, audio knihách na videu, tutoriáloch, hodinových YouTube stiahnutiach — klepnutím na Pridať záložku z menu Viac akcií. Záložky sa zobrazujú v zozname Viac akcií → Záložky videa a pretrvávajú medzi reláciami.

## Menu Viac akcií

Klepnite na tlačidlo **Viac akcií "..."** na prehrávači pre prístup k ďalším funkciám.

- **Pokračovať v prehrávaní** — obnoviť frontu od poslednej pozície.
- **Hľadať** — nájsť konkrétne video vo vašej fronte.
- **Záložky** — zobraziť a preskočiť na záložky.
- **Rýchlosť** — nastaviť rýchlosť prehrávania.
- **Nedávné** — nedávno prehrávané videá.
- **Obľúbené** — obľúbené videá.
- **Audio ekvalizér** — aktivovať audio ekvalizér.
- **Video ekvalizér** — aktivovať video ekvalizér.
- **Audio stopa** — vybrať audio stream.
- **Video stopa** — vybrať video stream.
- **Titulky** — primárna / sekundárna stopa, externý súbor, písmo.
- **Rotácia** — otočiť obraz 0° / 90° / 180° / 270°.
- **Režim škálovania** — Prispôsobiť / Vyplniť / Roztiahnuť / Pôvodné.
- **Picture-in-Picture** — vstúpiť do režimu PiP.
- **AirPlay** / **Chromecast** — odoslať na zariadenie.
- **Časovač spánku** — nastaviť časovač na zastavenie prehrávania.
- **Uložiť frontu ako playlist** — uložiť aktuálnu frontu ako nový playlist.
- **Odstrániť frontu** — vymazať frontu a zastaviť prehrávanie.
- **Nastavenia** — prejsť priamo na nastavenia prehrávača.
- **Pomoc** — otvoriť poradenstvo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo prehrávač obrazovka Viac akcií" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Nastavenia prehrávača

Úplný strom nastavení prehrávača je zdokumentovaný v [Sprievodcovi nastaveniami](/docs/guide/evervideo/evervideo-guide-settings/). Najpoužívanejšie sekcie:

- **Všeobecné** — Režim opakovania, Režim náhodného prehrávania, Uložiť stav prehrávača, Uložiť pozíciu prehrávania, Intervaly preskočenia.
- **Video** — Hardvérové dekódovanie H.264 / HEVC, video ekvalizér, režim škálovania, rotácia, režim zobrazenia, preferované FPS, preferovaný formát pixelov, VR pohľad.
- **Audio** — Audio ekvalizér, vzorkovacia frekvencia, kanály, trvanie IO bufferu, zmiešaný režim.
- **Titulky** — Primárna / sekundárna stopa, výber externého súboru, písmo, sekundárne písmo.
- **Zariadenia** (iOS) — AirPlay / Chromecast.
- **Personalizácia** — Štýl rozloženia prehrávača (Minimálny / Spodný / Antický / Klasický), akcie hlavnej obrazovky, ovládacie prvky uzamknutej obrazovky.
- **Vyrovnávacia pamäť prehrávania** — disková vyrovnávacia pamäť pre plynulejšie streamovanie.
- **Časovač spánku** — automatické zastavenie.

## Prístupnosť

Evervideo je plne prístupné s VoiceOver. Každá súčasť má dobre navrhnutý štítok a popis. Keď je VoiceOver aktívny, aplikácia sa prepne do textového režimu, takže sú zobrazené iba zmysluplné prvky — čo zlepšuje rýchlosť navigácie a prehľadnosť. Textový režim môžete tiež aktivovať v Nastavenia → Prístupnosť → Textový režim.

### Nastavenie posúvačov s VoiceOver

1. **Vyberte posúvač** — potiahnite vľavo alebo vpravo, kým VoiceOver neohlási posúvač.
2. **Nastavte hodnotu** — dvakrát klepnite a podržte posúvač, potom potiahnite nahor alebo nadol na rýchlu zmenu hodnoty. VoiceOver oznamuje novú hodnotu priebežne.

Ostatné súčasti fungujú podľa očakávaní, s použitím systémom poskytovaných vzorov VoiceOver.
