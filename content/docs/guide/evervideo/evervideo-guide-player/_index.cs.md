---
title: "Přehrávač médií"
date: 2020-02-01
lastmod: 2026-06-01
description: "Naučte se používat přehrávač médií Evervideo na iPhone, iPad a Mac. Picture-in-Picture, hardwarové dekódování H.264/HEVC, ekvalizéry zvuku a videa, primární a sekundární titulky, výběr zvukových a video stop, škálování a rotace videa, rychlost přehrávání, časovač spánku, AirPlay 2, Google Chromecast, RTSP streamy a kompaktní přehrávač vždy na obrazovce."
keywords: [
  "průvodce přehrávačem Evervideo", "nastavení přehrávače videí", "ekvalizér Evervideo",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "titulky videa iPhone", "externí titulky SRT",
  "přehrávač titulků ASS SSA", "libass iOS",
  "dvojité titulky výuka jazyků",
  "ekvalizér videa jas kontrast", "ekvalizér zvuku přehrávač videí",
  "zámek rotace přehrávač videí", "režim škálování videa iOS",
  "hardwarový dekodér H.264 iPhone", "hardwarový dekodér HEVC iPad",
  "rychlost přehrávání videa", "přehrávač videí FFmpeg iOS",
  "přehrávač RTSP iPhone", "kompaktní přehrávač videí",
  "přehrávač VR 360 videí iPhone"
]
tags: ["průvodce", "evervideo", "přehrávač", "PiP", "titulky", "video ekvalizér"]
readingTime: 14
---


Přehrávač médií je hlavní obrazovka aplikace, kde ovládáte přehrávání a většinu funkcí Evervideo. Přehrává video i zvukové soubory a je postaven na vlastním přehrávači založeném na FFmpeg s hardwarovým dekódováním H.264 a HEVC. Pojďme se podívat, jak ho používat.

## Přístup k přehrávači médií

Do přehrávače na celou obrazovku se dostanete z kompaktní lišty přehrávače. Na iPhone je kompaktní přehrávač v horní části hlavní obrazovky. Na iPad a Mac je na levé straně (nebo v horní části hlavního panelu). Pro sbalení přehrávače na celou obrazovku zpět do kompaktního zobrazení klepněte na tlačítko zavřít v pravém dolním rohu nebo přejeďte dolů. Pro úplné skrytí kompaktního přehrávače klepněte a přejeďte dolů ještě jednou.

Kompaktní přehrávač zůstává viditelný, zatímco procházíte knihovnu, správce souborů nebo nastavení, takže video nikdy neztrácíte při hledání dalšího.

{{< cards cols="1">}}
  {{< card title="" subtitle="Přehrávač médií na celou obrazovku v Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Podporované video a zvukové formáty

Evervideo přehrává prakticky každý moderní kontejner a kodek prostřednictvím přibaleného FFmpeg stroje s hardwarovým dekódováním H.264 a HEVC na podporovaných zařízeních.

- **Video kontejnery:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — a mnoho dalšího.
- **Video kodeky:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus prakticky každý jiný kodek, který FFmpeg podporuje.
- **Zvukové kodeky:** AAC, MP3, FLAC, ALAC, OGG/Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — a mnoho dalšího.
- **Formáty titulků:** SRT, VTT (WebVTT), ASS/SSA a vložené textové nebo obrázkové titulkové stopy.
- **Streamovací protokoly:** HTTP/HTTPS, HLS (m3u8), RTSP (IP kamery a IPTV) a přímé streamování souborů přes SMB/WebDAV/FTP/SFTP/NFS/DLNA.

To pokrývá prakticky každý video soubor, na který pravděpodobně narazíte — včetně MKV ripů, RTSP streamů bezpečnostních kamer a AV1 webm webových stahování.

## Ovládání přehrávání

V dolní části obrazovky přehrávače uvidíte tlačítka Přehrát, Pauza, Další a Předchozí. Jsou zde také volitelná tlačítka jako Přeskočit vpřed a Přeskočit vzad (výchozí 10 sekund), která lze aktivovat v nastavení aplikace. Podržením tlačítek Další/Předchozí přetáčíte vpřed nebo vzad. Přetažením posuvníku přehrávání přejdete na libovolnou pozici.

## Opakování a náhodné přehrávání

Klepnutím na tlačítko opakování procházíte režimy opakování:

- **Opakovat vše** — opakuje každé video ve frontě.
- **Opakovat jedno** — opakuje pouze aktuální video.
- **Zastavit při konci** — pozastaví, když aktuální video skončí.
- **Bez opakování** — přehraje frontu jednou bez opakování.

Pomocí tlačítka **Náhodně** zamíchejte pořadí videí ve frontě.

## Picture-in-Picture (PiP)

Na iPhone a iPad Evervideo plně podporuje Picture-in-Picture (PiP). Klepněte na ikonu PiP na obrazovce přehrávače nebo jednoduše odešlete Evervideo do pozadí — video se nadále přehrává v plovoucím okně nad každou jinou aplikací. Plovoucí okno přetáhněte do libovolného rohu; přiblíženým gestem změňte velikost; jedním klepnutím zobrazte základní ovládání přehrávání/pauzy/přeskočení; klepnutím na malé tlačítko Rozbalit se vraťte do celého Evervideo.

PiP funguje s každým formátem videa, který Evervideo přehrává, včetně souborů streamovaných z cloudu a RTSP streamů. PiP také pokračuje v běhu, zatímco je telefon zamčen (v závislosti na nastavení automatického uzamčení).

## Kompaktní přehrávač

Kompaktní přehrávač je trvalý mini přehrávač, který zůstává viditelný v horní části každé obrazovky v aplikaci při procházení knihovny, správce souborů nebo nastavení. Klepněte pro rozbalení do přehrávače na celou obrazovku; přejeďte dolů pro opětovné sbalení.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nastavení videa z kompaktního přehrávače na hlavní obrazovce v Evervideo" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Pro AirPlay klepněte na tlačítko AirPlay v přehrávači. Evervideo podporuje AirPlay 2, takže video lze streamovat do Apple TV, HomePod nebo jakéhokoli reproduktoru či chytrého televizoru kompatibilního s AirPlay 2. V nastavení s více AirPlay zařízeními lze zvuk přesměrovat na více přijímačů současně.

## Google Chromecast

Pro uživatele Google Cast se na přehrávači zobrazí ikona Cast. Klepnutím vyberte zařízení a spusťte přenos. Ujistěte se, že telefon a Cast přijímač jsou ve stejné Wi-Fi síti. Ne každý kodek je podporován hardwarem Chromecast — některé soubory mohou vyžadovat překódování.

## Živé RTSP streamy

Evervideo může přehrávat RTSP zdroje přímo — IP kamery, kamerové zvonky, IPTV streamy, vysílací kanály a jakoukoli jinou URL `rtsp://`. Přidejte stream jako RTSP připojení v Soubory → Online odkazy → Přidat odkaz a klepnutím spusťte sledování. RTSP streamy fungují v Picture-in-Picture, kompaktním přehrávači a přenášejí se přes AirPlay 2 a Chromecast stejně jako běžné video.

## Výběr zvukové stopy

U videí s více zvukovými stopami (komentář, alternativní jazykové dabingy, stopy režiséra) klepněte na tlačítko Další akce v přehrávači a zvolte Zvuková stopa — poté vyberte požadovanou stopu. Nezbytné pro cizojazyčné filmy, soubory BDMV/MKV s více dabingy a výukový obsah s komentářovými stopami.

## Výběr video stopy

Některé video soubory obsahují více video streamů (Blu-ray s více úhly, alternativní střihy). Zvolte Video stopu z nabídky Další akce pro přepínání mezi nimi během přehrávání.

## Titulky — interní a externí

Evervideo poskytuje přesnou kontrolu nad titulky:

- **Titulková stopa** — vyberte z stop vložených do souboru.
- **Externí soubory titulků** — načtěte soubory `.srt`, `.vtt`, `.ass` nebo `.ssa` ze zařízení, iCloud Drive nebo jakékoli připojené cloudové služby.
- **Vykreslování Libass** — pokročilé stylování ASS/SSA (písma, barvy, pozice, karaoke efekty) je správně vykresleno díky přiložené knihovně libass.
- **Výběr písma** — vyberte vlastní písmo pro primární titulkovou stopu a samostatné písmo pro sekundární titulky. K dispozici jsou přiložená písma plus libovolné písmo nainstalované v zařízení.

Vše lze nakonfigurovat v Nastavení → Titulky před přehráváním nebo použít Další akce → Titulky z přehrávače pro přepínání za chodu.

## Zvukový ekvalizér

Evervideo obsahuje plný zvukový ekvalizér pro ladění zvukových stop videa pro sluchátka, reproduktory nebo hi-fi sestavu. Klepněte na ikonu ekvalizéru v zobrazení hlasitosti (nebo na akci Zvukový ekvalizér v nabídce Další akce přehrávače), zapněte ekvalizér přepínačem v pravém horním rohu a buď vyberte předvolbu nebo přetáhněte posuvníky pásma pro vytvoření vlastní předvolby. Vlastní předvolby lze exportovat a importovat pro sdílení napříč zařízeními nebo zálohování.

## Video ekvalizér

Pro ladění obrazu Evervideo poskytuje vyhrazený video ekvalizér — upravte jas, kontrast, sytost a odstín v reálném čase během přehrávání. Podobně jako zvukový ekvalizér lze vlastní video předvolby exportovat a importovat pro sdílení nebo zálohu. Použijte ho pro zesvětlení tmavé scény za slunečného dne, zvýšení sytosti vybledle vypadajícího obsahu nebo ohřátí studeného barevného nádechu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Video ekvalizér Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Režim škálování videa

Vyberte, jak video zaplní obrazovku:

- **Přizpůsobit** — zachovejte původní poměr stran; černé pruhy tam, kde je potřeba.
- **Vyplnit** — zaplňte celou obrazovku, v případě potřeby video ořízněte.
- **Roztáhnout** — roztáhněte video pro zaplnění obrazovky, v případě potřeby s deformací.
- **Původní** — zachovejte nativní rozlišení v poměru 1:1.

## Rotace videa

U videí zaznamenaných s nesprávnou orientací zvolte **Další akce → Rotace** a vyberte **0°**, **90°**, **180°** nebo **270°** pro otočení obrazu bez opuštění přehrávače.

## Hardwarové dekódování (H.264 a HEVC)

V Nastavení → Přehrávač → Video lze nezávisle aktivovat/deaktivovat Hardwarové dekódování H.264 a Hardwarové dekódování H.265 (HEVC). Hardwarové dekódování je rychlejší, spotřebovává méně baterie a běží chladněji — ale ve vzácných případech (poškozené soubory, exotické profily) může být nutné hardwarové dekódování zakázat a vrátit se k softwarovému dekódování FFmpeg. Evervideo to umožňuje soubor po souboru z nabídky Další akce přehrávače.

## Výřez VR 360°

Evervideo zahrnuje výřez VR/360° pro sférické video soubory. Při přehrávání 360° videa lze táhnout pro rozhlédnutí, přiblíženým gestem přiblížit a Evervideo bude deformovat vykreslování v reálném čase.

## Rychlost přehrávání

Klepnutím na ovládání Rychlost v panelu nástrojů přehrávače změňte rychlost přehrávání — zpomalte pro analýzu (0,25× nebo 0,5×) nebo zrychlte pro tutoriály a přednášky (1,25×, 1,5×, 2× a až 3×). Klepnutím na ikonu konfigurace v pravém horním rohu obrazovky Rychlost přepněte do přesného režimu s jemnějšími nastaveními. K dispozici je také korekce výšky tónu pro každou stopu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Rychlost přehrávání Evervideo v hlavním panelu nástrojů" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Fronta přehrávače

Pro zobrazení fronty přehrávače klepněte na tlačítko fronty v přehrávači. Každé video ve frontě má více akcí — klepněte na tři tečky pro jejich zobrazení. Pro přeuspořádání videa ve frontě použijte indikátor přeuspořádání u názvu a přetáhněte ho na novou pozici.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fronta přehrávání Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Časovač spánku

Otevřete Nastavení → Přehrávač → Časovač spánku, zapněte ho a vyberte, jak dlouho chcete, aby přehrávání pokračovalo před automatickým zastavením. Tlačítko Časovač spánku lze také přidat přímo na hlavní obrazovku přehrávače přes Nastavení → Přehrávač → Personalizace → Akce hlavní obrazovky.

## Záložky přehrávače

Uložte své místo v dlouhých videích — přednášky, audioknihy na videu, tutoriály, hodinová stahování z YouTube — klepnutím na Přidat záložku z nabídky Další akce. Záložky se zobrazí v seznamu Další akce → Záložky videa a přetrvávají mezi relacemi.

## Nabídka Další akce

Klepnutím na tlačítko **Další akce "..."** v přehrávači přistupte k dalším funkcím.

- **Pokračovat v přehrávání** — pokračujte ve frontě od poslední pozice.
- **Hledat** — najděte konkrétní video ve frontě.
- **Záložky** — zobrazit záložky a přejít na ně.
- **Rychlost** — nastavte rychlost přehrávání.
- **Nedávné** — nedávno přehrána videa.
- **Oblíbené** — oblíbená videa.
- **Zvukový ekvalizér** — aktivujte zvukový ekvalizér.
- **Video ekvalizér** — aktivujte video ekvalizér.
- **Zvuková stopa** — vyberte zvukový stream.
- **Video stopa** — vyberte video stream.
- **Titulky** — primární/sekundární stopa, externí soubor, písmo.
- **Rotace** — otočte obraz 0°/90°/180°/270°.
- **Režim škálování** — Přizpůsobit/Vyplnit/Roztáhnout/Původní.
- **Picture-in-Picture** — vstupte do režimu PiP.
- **AirPlay** / **Chromecast** — odeslat do zařízení.
- **Časovač spánku** — nastavte časovač pro zastavení přehrávání.
- **Uložit frontu jako playlist** — uložte aktuální frontu jako nový playlist.
- **Smazat frontu** — vyčistěte frontu a zastavte přehrávání.
- **Nastavení** — přejděte přímo do nastavení přehrávače.
- **Nápověda** — otevřete průvodce.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka Další akce přehrávače Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Nastavení přehrávače

Kompletní strom nastavení přehrávače je zdokumentován v [průvodci Nastavení](/docs/guide/evervideo/evervideo-guide-settings/). Nejpoužívanější sekce:

- **Obecné** — režim opakování, režim náhodného přehrávání, uložení stavu přehrávače, uložení pozice přehrávání, intervaly přeskočení.
- **Video** — hardwarové dekódování H.264/HEVC, video ekvalizér, režim škálování, rotace, režim zobrazení, preferované FPS, preferovaný formát pixelů, výřez VR.
- **Zvuk** — zvukový ekvalizér, vzorkovací frekvence, kanály, trvání IO bufferu, smíšený režim.
- **Titulky** — primární/sekundární stopa, výběr externího souboru, písmo, sekundární písmo.
- **Zařízení** (iOS) — AirPlay/Chromecast.
- **Personalizace** — styl rozvržení přehrávače (Minimální/Spodní/Starožitný/Klasický), akce hlavní obrazovky, ovládání zamčené obrazovky.
- **Mezipaměť přehrávání** — diskový mezipaměti pro plynulejší streamování.
- **Časovač spánku** — automatické zastavení.

## Přístupnost

Evervideo je plně přístupné s VoiceOver. Každá komponenta má dobře navrženou popisku a popis. Když je VoiceOver aktivní, aplikace přepne do Textového režimu, takže se zobrazují pouze smysluplné prvky — zlepšuje rychlost navigace a přehlednost. Textový režim lze také aktivovat v Nastavení → Přístupnost → Textový režim.

### Úprava posuvníků s VoiceOver

1. **Vyberte posuvník** — přejeďte doleva nebo doprava, dokud VoiceOver neoznámí posuvník.
2. **Upravte hodnotu** — dvojitě klepněte a podržte posuvník, poté táhněte nahoru nebo dolů pro rychlou změnu hodnoty. VoiceOver oznamuje novou hodnotu.

Ostatní komponenty fungují podle očekávání pomocí systémem poskytovaných vzorů VoiceOver.
