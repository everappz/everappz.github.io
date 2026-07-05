---
title: "Evertag 4.2: nová cloudová připojení a vysvětlení nastavení editoru tagů"
date: 2026-05-09
description: "Evertag 4.2 přidává připojení k Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP a NFS, osvěžuje Wi-Fi Drive a aktualizuje rozhraní pro Liquid Glass. Tento příspěvek také vysvětluje každé nastavení editoru tagů — včetně ID3v2.4 vs ID3v2.3, škálování obalu alba, duplikování tagů, režimů nahrávání do cloudu a správných možností pro Spotify a další streamovací služby."
keywords: ["Evertag 4.2", "aktualizace Evertag", "ID3 editor tagů iPhone", "ID3v2.4 vs ID3v2.3", "úprava FLAC tagů iOS", "úprava MP3 tagů iPhone", "úprava obalu alba iOS", "editor tagů pro Spotify", "editor tagů Plex", "editor tagů Apple Music", "Evertag cloudový editor tagů", "editor tagů Internxt", "editor tagů Proton Drive", "editor tagů QNAP", "editor tagů Nextcloud", "editor tagů Amazon S3", "SFTP editor tagů iPhone", "FTP audio editor tagů", "NFS editor tagů iPhone", "Wi-Fi Drive editor tagů", "duplikování ID3 tagů", "škálování obalu", "design Liquid Glass", "editor audio metadat iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Editor tagů", "ID3", "ID3v2.4", "ID3v2.3", "FLAC tagy", "MP3 tagy", "Obal alba", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Co je nového"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Stručně:** [Evertag 4.2](/products/evertag) je velká aktualizace editoru zvukových tagů pro iPhone, iPad a Mac. Opravili jsme zásadní chyby při úpravě tagů a přidali přes 6 nových cloudových a serverových připojení — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** a protokoly **FTP**, **SFTP** a **NFS**. Wi-Fi Drive získal osvěžené rozhraní, režim vícenásobného výběru, chytřejší frontu nahrávání a rychlejší přenosy. Celá aplikace je naladěná na design **Liquid Glass**. Tento příspěvek se také ponoří do nastavení editoru tagů Evertag — vysvětluje **ID3v2.4 vs ID3v2.3**, **škálování obalu alba**, **duplikování tagů**, **režimy nahrávání do cloudu**, **mazání staženého souboru** a přesně to, jaké možnosti zvolit, pokud připravujete zvuk pro **Spotify**, **Apple Music**, **Plex**, **Jellyfin** nebo jakoukoli jinou streamovací službu.

---

## Ahoj všichni!

Velká aktualizace Evertag je tady. Opravili jsme zásadní chyby při úpravě tagů a přidali **přes 6 nových cloudových a serverových připojení**, abyste mohli spravovat zvuková metadata snáz než kdy dřív — ať už vaše knihovna žije v cloudu se zaměřením na soukromí, na vlastním NAS nebo na obecném serveru FTP/SFTP/NFS.

[Stáhněte si Evertag 4.2 z App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) nebo aktualizujte ze své stávající verze.

## Rozšířená podpora cloudu a serverů

Evertag se nyní nativně připojuje k širší škále cloudových a vlastních úložných řešení. Můžete upravovat tagy ID3, MP4, FLAC, OGG a APE u souborů kdekoli.

### Cloudy zaměřené na soukromí: Internxt a Proton Drive

Pokud vám záleží na end-to-end šifrování a úložišti bez znalosti, dvě nejuznávanější jména cloudů s důrazem na soukromí jsou nyní v Evertag nativně:

- **Internxt** — španělský cloud s otevřeným kódem, post-kvantovým šifrováním a souladem s GDPR. K dispozici je bezplatná úroveň.
- **Proton Drive** — end-to-end šifrované úložiště od tvůrců Proton Mail a Proton VPN se sídlem ve Švýcarsku. K dispozici je bezplatná úroveň, pro větší knihovny placené plány.

Nyní můžete upravovat metadata přímo u zvukových souborů uložených v některé z těchto služeb — soubor zůstává zašifrovaný při přenosu a do úložiště se zapíší pouze nové tagy.

### Vlastní řešení: QNAP, Nextcloud, Amazon S3

Pro uživatele provozující vlastní infrastrukturu:

- **QNAP** — nativní API připojení k zařízením QNAP NAS. Upravujte tagy u souborů na QNAPu přes místní Wi-Fi nebo vzdálený přístup.
- **Nextcloud** — připojte se k libovolné instanci Nextcloud, vlastní nebo spravované.
- **Amazon S3** — nasměrujte Evertag na libovolný S3 bucket (nebo úložiště kompatibilní s S3 jako Backblaze B2, Wasabi, MinIO, Cloudflare R2) a upravujte metadata přímo na místě.

### Nové síťové protokoly: FTP, SFTP, NFS

Evertag 4.2 přidává tři klasické protokoly pro uživatele s vlastními servery, homelaby nebo univerzálními NAS:

- **SFTP (SSH File Transfer Protocol)** — správná odpověď pro **bezpečné vzdálené úpravy tagů z vlastního serveru**. SFTP běží nad SSH, takže celý přenos (autentizace i zvuková data) je šifrován. Pokud máte VPS, dedikovaný server nebo Linux stroj doma se SSH přístupem, můžete upravovat tagy u vzdálených souborů, aniž byste odhalili cokoliv jiného. Podporuje autentizaci heslem i klíčem.
- **FTP** — dlouholetý standard pro přenos souborů. Užitečný pro starší domácí NAS, které nabízejí FTP, ale nemají nativní integraci přes API.
- **NFS (Network File System)** — de facto sdílecí protokol v Linuxu a na většině NAS. Menší režie než SMB na stejném hardwaru.

> **Tip:** SFTP je protokol, který chcete pro vzdálené úpravy přes otevřený internet. FTP a NFS se nejlépe používají v lokální síti — neotevírejte je do internetu, pokud je nezabalíte do VPN.

## Vylepšení Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) je integrovaná funkce Evertagu pro **bezdrátový přenos zvukových souborů mezi počítačem a iPhonem nebo iPadem — bez iTunes, kabelů a cloudového účtu**. Obě zařízení musí být ve stejné Wi-Fi síti.

V Evertag 4.2 Wi-Fi Drive získává:

- **Osvěžené, moderní rozhraní** — čistší, snadno čitelné na první pohled a aktualizované pro Liquid Glass.
- **Režim vícenásobného výběru** — vyberte více souborů nebo složek a zpracujte je hromadně.
- **Chytřejší fronta nahrávání** — lepší zpětná vazba o průběhu a odolnost vůči výkyvům sítě.
- **Lepší rychlost a celková spolehlivost** — rychlejší přenosy pro velké knihovny.

Je to nejrychlejší způsob, jak přesunout dávku zvukových souborů z počítače do telefonu, upravit jejich tagy a poslat je zpět — bez jakékoliv služby třetí strany.

## Nastavení editoru tagů: hluboký ponor

Toto je část, kterou většina uživatelů nikdy nečte — a část, která rozhoduje, zda vaše tagy fungují všude, nebo jen v některých aplikacích. Otevřete Evertag a přejděte do sekce **nastavení editoru zvukových tagů**. Zde je, co každá volba opravdu dělá a kterou zvolit podle vašeho cíle.

### Škálování obalu alba

Když ukládáte obal alba do zvukového souboru, Evertag může obraz před vložením zmenšit. Dostupné možnosti:

- **Malý** — nejmenší dopad na velikost souboru, nižší kvalita obrazu.
- **Střední** — vyvážená volba pro většinu uživatelů.
- **Velký** — vysoká kvalita, vhodné pro přehrávače s velkými obrazovkami a CarPlay.
- **Velmi velký** — velmi vysoká kvalita, znatelný nárůst velikosti souboru.
- **Originál (Vypnuto)** — vloží obal v původním rozlišení. **Žádné škálování.**

**Proč na tom záleží:**

- **Vyšší kvalita = větší soubor.** Obal 3 000 × 3 000 pixelů může přidat několik MB na každou skladbu. Vynásobeno celým albem se náklady na disk rychle nasčítají.
- **Některé přehrávače si s velmi velkými vloženými obrázky neporadí.** Starší zařízení, některé autorádia a starší stolní přehrávače mohou na obalech nad ~1 500 px zamrznout nebo je odmítnout zobrazit.
- **Pro většinu cloudových a streamovacích pracovních postupů** je **Střední** nebo **Velký** ideální. **Originál** používejte jen tehdy, když potřebujete archivní kvalitu nebo připravujete soubory pro důvěryhodný přehrávač.

> Volba velikosti **Originál** je součástí prémiového personalizačního upgradu Evertagu. Standardní velikosti (Malý/Střední/Velký/Velmi velký) jsou zdarma.

### Možnosti ukládání tagů: ID3v2.4 vs ID3v2.3

Toto je nejdůležitější jediné nastavení pro kompatibilitu. ID3v2 je formát metadat uvnitř MP3 souborů. Existují dvě široce používané verze, které se liší v jemných, ale důležitých detailech.

#### ID3v2.4

- Novější, podporuje **kódování textu UTF-8** — správné zpracování nelatinkových písem (čínština, ruština, japonština, arabština, hebrejština atd.).
- Více typů rámců (relativní hlasitost, presety ekvalizéru atd.).
- **Doporučeno pro moderní přehrávače**, které ji podporují.

#### ID3v2.3

- Starší, ale **nejuniverzálněji podporovaná verze ID3**.
- Nepodporuje UTF-8 přímo (pro Unicode používá UTF-16).
- **Doporučeno, když potřebujete maximální kompatibilitu** se staršími přehrávači, autorádii a některými stolními aplikacemi.

#### Kdy zapnout ID3v2.4 v Evertagu

- Používáte **moderní zvukové přehrávače** jako Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (aktuální verze) nebo moderní Android přehrávače. ✅ **Zapněte ID3v2.4.**
- Vaše knihovna obsahuje **nelatinkové znaky** (čínština, korejština, japonština, ruština, arabština, řečtina, hebrejština). ✅ **Zapněte ID3v2.4** — UTF-8 je zpracovává mnohem čistěji.

#### Kdy vypnout ID3v2.4 v Evertagu (použijte ID3v2.3)

- Připravujete soubory pro **starší autorádio nebo palubní jednotku**, která nečte tagy v2.4.
- Po úpravě vidíte v některých aplikacích **rozházený text nebo chybějící tagy** — to je silný signál, že tam není podporována v2.4. Přepněte zpět na v2.3.
- Cílíte na **starší stolní přehrávače** nebo starší přenosné přehrávače (rané iPody, některé MP3 přehrávače z let 2000–2010).

> **Praktické pravidlo:** pokud se vaše tagy zobrazují všude správně s v2.4, nechte ji zapnutou. Pokud i jediný důležitý přehrávač zobrazuje špatné znaky, prázdné nebo nečte tagy, vypněte v2.4 a uložte znovu.

#### Duplikování tagů

Když zapnete **Duplikování tagů**, Evertag zapíše společná pole metadat (název, interpret, album atd.) **do obou sekcí ID3v1 a ID3v2** souboru. To zlepšuje kompatibilitu s velmi starými přehrávači, které čtou pouze ID3v1 (původní 128bajtový tag na konci souboru).

- **Většina uživatelů to nepotřebuje.** Moderní přehrávače čtou ID3v2 jako první.
- **Zapněte to pouze tehdy**, pokud pracujete s vintage hardwarem nebo specifickým softwarem, který ID3v2 ignoruje.

### Aktualizace online souborů: jak Evertag řeší cloudové úpravy

Když upravujete tagy u souboru uloženého na připojeném cloudu (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP atd.), Evertag musí upravený soubor nahrát zpět. Vy řídíte, jak:

- **Zobrazit potvrzovací zprávu** *(výchozí, doporučeno)* — Evertag se před nahráním zeptá. Nejlepší pro opatrné uživatele a sdílené knihovny.
- **Automaticky aktualizovat metadata souboru** — po každé úpravě tiše nahraje. Nejlepší pro samostatné uživatele s rychlým, spolehlivým připojením, kteří hodně upravují.
- **Neaktualizovat metadata souboru** — Evertag upravuje pouze místní kopii. Užitečné pro náhled změn bez jejich nahrání do cloudu.

### Úprava online souborů: úklid místního souboru

Pro úpravu vzdáleného souboru ho Evertag nejprve stáhne do zařízení. Po úpravě si vyberete, co se s touto místní kopií stane:

- **Vždy smazat stažený soubor** — Evertag po úpravě dočasný soubor odstraní. **Doporučeno**, pokud máte málo úložiště nebo pracujete s cizími soubory.
- **Nemazat stažený soubor** — ponechá upravený soubor v zařízení. Užitečné, když chcete mít offline kopii i aktuální cloudovou kopii.

### Tlačítka na hlavní obrazovce

Hlavní obrazovka editoru tagů Evertag může zobrazit nebo skrýt tlačítka pro jednotlivé operace. Aktivujte pouze ta, která skutečně používáte, abyste rozhraní udrželi soustředěné:

- **Automaticky vyhledat zvukové tagy** — najde chybějící metadata online podle zvukového otisku souboru.
- **Ručně vyhledat zvukové tagy** — hledejte podle názvu/interpreta, když automatické hledání selže.
- **Hledat obal alba** — najde a vloží kvalitní obaly.
- **Uložit obal alba** — exportuje vložený obal do fotoknihovny nebo souborů.
- **Normalizovat kódování** — opravuje nelatinkový text rozházený starým kódováním (velmi užitečné pro cyrilské, čínské a japonské skladby ripnuté starším softwarem).
- **Smazat zvukové tagy** — odstraní všechny tagy ze souboru. Užitečné před čistým novým otagováním.

### Zobrazit rozšířené tagy

Zapněte to pro zobrazení celé sady polí metadat nad rámec základního název/interpret/album/rok — včetně BPM, dirigenta, původního interpreta, nálady, copyrightu, kodéru, komentářů, textů a dalších. Funkce pro pokročilé uživatele; většina běžných ji nepotřebuje.

### Upravovat soubory současně

Když je zapnuto, Evertag vám umožní upravit metadata u **více vybraných souborů najednou** — nastavte stejného album artist, rok nebo žánr pro celé album v jediné operaci. Nejrychlejší způsob, jak srovnat velkou neuspořádanou knihovnu.

## Úprava tagů pro Spotify, Apple Music a streamovací platformy

Častý dotaz: «upravil jsem si tagy v Evertagu, nahrál soubory a streamovací služba zobrazuje špatné metadata. Co se děje?»

Krátká odpověď: **streamovací služby ne vždy respektují vaše místní tagy.** Apple Music a Spotify mají vlastní interní databáze — když rozpoznají skladbu, přepíšou zobrazované metadata svými. Ale pro **nahrané soubory**, vaše místní soubory (funkce «Knihovna» Apple Music, Spotify Local Files) a **nahrávky distributorů na streamovací platformy** vaše tagy zcela jistě záleží. Tady je, jak nastavit Evertag pro každý scénář:

### Příprava souborů pro Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music správně zachází s UTF-8.
- **Obal alba: Velký** — aplikace Apple zobrazují velké obaly dobře; Originál je přehnaný.
- **Duplikování tagů: OFF** — není potřeba.
- Ujistěte se, že **Album Artist** je správně vyplněný — Apple Music ho používá ke seskupení.

### Příprava souborů pro Spotify Local Files

Spotify Local Files zobrazuje pouze dobře otagované soubory. Tagy, které Spotify čte, jsou omezené.

- **ID3v2.4: ON** ve většině případů. Pokud se skladba po úpravě v Spotify nezobrazí správně, **zkuste uložit s ID3v2.4: OFF** (tedy jako ID3v2.3) — parser Spotify byl historicky konzervativní vůči v2.4.
- **Obal alba: Střední nebo Velký** — Spotify obal stejně zmenšuje.
- Vyplňte minimálně **Název**, **Interpreta**, **Album** a **Číslo skladby**.

### Příprava souborů pro nahrávání distributorem (DistroKid, TuneCore, CD Baby atd.)

Pokud jste interpret nahrávající vlastní díla na streamovací platformy, distributor obvykle čte tagy, ale také požaduje metadata ve svém rozhraní. Tak jako tak:

- **ID3v2.3** je často bezpečnější výchozí volba — mnohé pipeliny distributorů byly postaveny před lety a preferují starší formát.
- Vložte **Velký** obal (většina distributorů vyžaduje obal ≥ 1 400 × 1 400 px — zkontrolujte jejich pokyny).
- Nespolehávejte se na rozšířené tagy — distributoři čtou pouze základní pole.

### Příprava souborů pro Plex, Jellyfin, Navidrome, Subsonic, Emby

Tyto vlastní mediální servery jsou velmi tolerantní. Čtou v2.3 i v2.4 čistě a UTF-8 zvládají dobře.

- **ID3v2.4: ON** je v pořádku.
- **Obal alba: Velký** nebo **Velmi velký** — tyto servery posílají obaly mobilním klientům a obrazovkám CarPlay, takže kvalita záleží.
- **Album Artist** je velmi doporučován — Plex/Jellyfin ho používají ke správnému seskupování alb podle interpreta.

### Příprava souborů pro autorádia a starší hardware

- **ID3v2.4: OFF** (použijte ID3v2.3) — starší jednotky často nepodporují v2.4.
- **Obal alba: Střední** — mnohé autodisplaye se na velkých vložených obalech zaseknou.
- **Duplikování tagů: ON** — starší autorádia někdy čtou pouze záložní ID3v1.

## Další vylepšení

### Design Liquid Glass

Rozhraní Evertag 4.2 je naladěno na nový materiál **Liquid Glass** od Apple v celé aplikaci — průsvitné povrchy, plynulejší animace a vytříbené ovládací prvky, které přirozeně zapadají do iOS, iPadOS a macOS.

### Aktualizované knihovny pro připojení

Osvěžili jsme interní knihovny, které Evertag používá pro komunikaci s **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** a dalšími službami. Výsledek: méně selhání připojení v okrajových případech, lepší podpora novějších verzí serverů a vyšší spolehlivost při úpravě tagů u vzdálených souborů.

### Opravy překladu a lokalizace

Vícero jazykových oprav v rozhraní na základě přímé zpětné vazby uživatelů. Lepší zarovnání textu na malých tlačítkách v několika jazycích.

### Drobnější vylepšení inspirovaná vaší zpětnou vazbou

Mnoho menších vylepšení založených na recenzích z App Store a e-mailech na support@everappz.com. Čteme každou zprávu.

## Stáhněte si Evertag 4.2

[**Stáhněte si Evertag z App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) nebo aktualizujte z App Store. Evertag je zdarma ke stažení s volitelnými upgrady v aplikaci pro pokročilé funkce. Nová cloudová připojení, síťové protokoly, vylepšení Wi-Fi Drive a UI Liquid Glass jsou součástí základní aktualizace.

Pokud se vám aplikace líbí, zanechte prosím v App Store hodnocení — hodně to pomáhá. Máte připomínky nebo problém? Napište nám na **support@everappz.com**. Čteme každou zprávu.

## Často kladené otázky

{{% details title="Co je nového v Evertag 4.2?" closed="true" %}}
Evertag 4.2 přidává přes 6 nových cloudových a serverových připojení (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), osvěžený Wi-Fi Drive s vícenásobným výběrem a chytřejší frontou nahrávání, aktualizace UI Liquid Glass, aktualizované knihovny pro připojení, klíčové opravy chyb v editaci tagů a vylepšení překladu.
{{% /details %}}

{{% details title="Mám v Evertagu používat ID3v2.4 nebo ID3v2.3?" closed="true" %}}
Použijte **ID3v2.4** pro moderní přehrávače (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, moderní Android aplikace) a pro knihovny s nelatinkovými znaky — podpora UTF-8 znamená čistší tagy v čínštině, korejštině, japonštině, ruštině, arabštině a hebrejštině. Použijte **ID3v2.3**, pokud se vaše tagy v některých aplikacích zobrazují špatně, pokud cílíte na starší autorádia, nebo pokud streamovací distributorský pipeline odmítá v2.4. Můžete kdykoliv přepnout a uložit znovu.
{{% /details %}}

{{% details title="Proč jsou moje tagy po úpravě v Spotify špatné?" closed="true" %}}
Spotify většinou zobrazuje metadata ze svého katalogu — vaše místní tagy se používají pouze pro «Local Files» nebo obsah, který jste nahráli jako interpret. Pokud taggujete soubory pro Spotify Local Files a nezobrazují se správně, zkuste v Evertagu vypnout ID3v2.4 a uložit jako ID3v2.3 — parser Spotify byl historicky konzervativní vůči v2.4.
{{% /details %}}

{{% details title="Jakou velikost obalu alba mám v Evertagu zvolit?" closed="true" %}}
Pro většinu uživatelů: **Velký**. Vypadá skvěle na telefonech, iPadech, Macích a moderních autodisplejích, aniž by soubory přiliš nafoukl. Použijte **Střední**, pokud máte obrovskou knihovnu a chcete šetřit disk. Použijte **Originál** (bez škálování) pouze pro archivní mastery nebo když opravdu potřebujete maximální kvalitu — ale berte v potaz, že některé starší přehrávače mají s velmi velkými vloženými obaly potíže. **Originál** je součástí prémiového personalizačního upgradu Evertagu.
{{% /details %}}

{{% details title="Zvětší větší obaly alba moje soubory?" closed="true" %}}
Ano. Vložení obalu 3 000 × 3 000 px může přidat několik megabajtů k jednomu zvukovému souboru. Na knihovně 1 000 skladeb se to rovná gigabajtům. Pokud je úložiště omezené, použijte Střední nebo Velký; pokud streamujete z NAS, kde na velikosti nezáleží, Velmi velký nebo Originál jsou v pořádku.
{{% /details %}}

{{% details title="Co je Duplikování tagů a mám ho zapnout?" closed="true" %}}
Duplikování tagů zapisuje základní metadata do obou sekcí ID3v1 (legacy 128 bajtů) a ID3v2 (moderní) v souboru. Zapněte ho jen tehdy, pokud cílíte na velmi staré přehrávače nebo hardware, který čte ID3v1. Pro vše moderní (smartphony, počítače, novější autorádia) ho nechte vypnuté.
{{% /details %}}

{{% details title="Upravuje Evertag tagy přímo v cloudových souborech?" closed="true" %}}
Ano. Připojte se ke svému cloudu (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 atd.) nebo přes FTP/SFTP/NFS, otevřete soubor a upravujte tagy, jako by byl místní. Evertag stáhne soubor, aplikuje vaše úpravy a aktualizovanou verzi nahraje zpět. V nastavení můžete zvolit režimy «Vždy se ptát», «Auto-upload» nebo «Nenahrávat».
{{% /details %}}

{{% details title="Můžu na iPhonu upravovat FLAC tagy v Evertagu?" closed="true" %}}
Ano. Evertag podporuje FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE a další významné formáty s plnou podporou čtení/zápisu tagů včetně vloženého obalu.
{{% /details %}}

{{% details title="Jak bezpečně upravím tagy na svém domácím serveru pomocí SFTP?" closed="true" %}}
Otevřete Evertag, přejděte do Připojení, vyberte SFTP a zadejte název hostitele nebo IP serveru, port (obvykle 22), uživatelské jméno a buď heslo, nebo soukromý SSH klíč. Evertag projde vaše vzdálené složky a tagy bude upravovat přímo s end-to-end šifrováním přes SSH.
{{% /details %}}

{{% details title="Můžu upravovat tagy u více souborů najednou?" closed="true" %}}
Ano. Aktivujte v nastavení **Upravovat soubory současně**. Vyberte více souborů, otevřete editor tagů a jakékoli pole, které změníte, se aplikuje na všechny vybrané soubory. Nejrychlejší způsob, jak nastavit stejného album artist, rok nebo žánr napříč celým albem.
{{% /details %}}

{{% details title="Je aktualizace na Evertag 4.2 zdarma?" closed="true" %}}
Ano. Evertag je zdarma ke stažení v App Store a 4.2 je bezplatná aktualizace pro všechny stávající uživatele. Nové cloudové integrace, vylepšení Wi-Fi Drive a UI Liquid Glass jsou součástí základní aktualizace.
{{% /details %}}

{{% details title="Na jakých zařízeních je Evertag 4.2 dostupný?" closed="true" %}}
Evertag 4.2 běží na iPhonu, iPadu a Macu. Synchronizace přes iCloud Drive udržuje vaše nastavení editoru tagů konzistentní napříč zařízeními.
{{% /details %}}
