---
title: "Evertag 4.2: nové cloudové pripojenia, vysvetlenie nastavení editora značiek"
date: 2026-05-09
description: "Evertag 4.2 pridáva pripojenia k Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP a NFS, osvieži Wi-Fi Drive a aktualizuje rozhranie pre Liquid Glass. Tento príspevok tiež vysvetľuje každé nastavenie editora značiek — vrátane ID3v2.4 vs ID3v2.3, škálovania obalu albumu, duplikovania značiek, režimov nahrávania do cloudu a správnych možností pre Spotify a iné streamovacie služby."
keywords: ["Evertag 4.2", "aktualizácia Evertag", "ID3 editor značiek iPhone", "ID3v2.4 vs ID3v2.3", "úprava značiek FLAC iOS", "úprava značiek MP3 iPhone", "úprava obalu albumu iOS", "editor značiek pre Spotify", "editor značiek Plex", "editor značiek Apple Music", "Evertag cloudový editor značiek", "editor značiek Internxt", "editor značiek Proton Drive", "editor značiek QNAP", "editor značiek Nextcloud", "editor značiek Amazon S3", "SFTP editor značiek iPhone", "FTP audio editor značiek", "NFS editor značiek iPhone", "Wi-Fi Drive editor značiek", "duplikovanie značiek ID3", "škálovanie obalu", "dizajn Liquid Glass", "editor audio metadát iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Editor značiek", "ID3", "ID3v2.4", "ID3v2.3", "Značky FLAC", "Značky MP3", "Obal albumu", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Čo je nové"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**V skratke:** [Evertag 4.2](/products/evertag) je veľká aktualizácia editora audio značiek pre iPhone, iPad a Mac. Vyriešili sme kľúčové chyby pri úprave značiek a pridali viac ako 6 nových cloudových a serverových pripojení — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** plus protokoly **FTP**, **SFTP** a **NFS**. Wi-Fi Drive získal osvieženú rozhranie, režim viacnásobného výberu, inteligentnejšiu frontu nahrávania a rýchlejšie prenosy. Celá aplikácia je vyladená pre dizajn **Liquid Glass**. Tento príspevok tiež hlboko skúma nastavenia editora značiek Evertag — vysvetľuje **ID3v2.4 vs ID3v2.3**, **škálovanie obalu albumu**, **duplikovanie značiek**, **režimy nahrávania do cloudu**, **vymazanie stiahnutého súboru** a presne to, ktoré možnosti vybrať, ak pripravujete zvuk pre **Spotify**, **Apple Music**, **Plex**, **Jellyfin** alebo akúkoľvek inú streamovaciu službu.

---

## Ahojte všetci!

Veľká aktualizácia Evertag je tu. Vyriešili sme kľúčové chyby pri úprave značiek a pridali **viac ako 6 nových cloudových a serverových pripojení**, aby bola správa audio metadát jednoduchšia ako kedykoľvek predtým — či už vaša knižnica žije v cloude zameranom na súkromie, na vlastnom NAS alebo na všeobecnom serveri FTP/SFTP/NFS.

[Stiahnite si Evertag 4.2 z App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) alebo aktualizujte zo svojej súčasnej verzie.

## Rozšírená podpora cloudu a serverov

Evertag sa teraz natívne pripája k širšiemu rozsahu cloudových a vlastných úložných možností. Môžete upravovať značky ID3, MP4, FLAC, OGG a APE v súboroch kdekoľvek.

### Cloudové úložisko zamerané na súkromie: Internxt a Proton Drive

Ak vám záleží na koncovom šifrovaní a úložisku bez znalostí, dva najuznávanejšie názvy v cloudoch zameraných na súkromie sú teraz natívne v Evertagu:

- **Internxt** — španielsky cloud s otvoreným zdrojom, post-kvantovým šifrovaním a v súlade s GDPR. K dispozícii bezplatná úroveň.
- **Proton Drive** — koncové šifrované úložisko od tvorcov Proton Mail a Proton VPN, so sídlom vo Švajčiarsku. K dispozícii bezplatná úroveň, platené plány pre väčšie knižnice.

Teraz môžete upravovať metadáta priamo na audio súboroch uložených v ktorejkoľvek z týchto služieb — súbor zostáva šifrovaný počas prenosu a späť sa zapíšu len nové značky.

### Vlastné riešenia: QNAP, Nextcloud, Amazon S3

Pre používateľov, ktorí prevádzkujú vlastnú infraštruktúru:

- **QNAP** — natívne API pripojenie k zariadeniam QNAP NAS. Upravujte značky v súboroch na vašom QNAPe cez lokálnu Wi-Fi alebo vzdialený prístup.
- **Nextcloud** — pripojte sa k akejkoľvek inštancii Nextcloud, vlastnej alebo spravovanej.
- **Amazon S3** — nasmerujte Evertag na akýkoľvek S3 bucket (alebo S3-kompatibilné úložisko ako Backblaze B2, Wasabi, MinIO, Cloudflare R2) a upravujte metadáta priamo na mieste.

### Nové sieťové protokoly: FTP, SFTP, NFS

Evertag 4.2 pridáva tri klasické protokoly pre používateľov s vlastnými servermi, domácimi labormi alebo všeobecnými NAS zariadeniami:

- **SFTP (SSH File Transfer Protocol)** — správna odpoveď pre **bezpečnú vzdialenú úpravu značiek z vlastného servera**. SFTP beží nad SSH, takže celý prenos (autentifikácia a audio dáta) je šifrovaný. Ak máte VPS, dedikovaný server alebo Linux počítač doma s prístupom SSH, môžete upravovať značky v vzdialených súboroch bez vystavenia čohokoľvek iného. Podporuje autentifikáciu heslom aj kľúčom.
- **FTP** — dlhoročne zavedený štandard pre prenos súborov. Užitočný pre staršie domáce NAS, ktoré sprístupňujú FTP, ale nemajú natívnu API integráciu.
- **NFS (Network File System)** — de facto protokol zdieľania v Linuxe a na väčšine NAS zariadení. Nižší overhead ako SMB na rovnakom hardvéri.

> **Tip:** SFTP je protokol, ktorý chcete na vzdialenú úpravu cez otvorený internet. FTP a NFS sú najlepšie použiteľné v lokálnej sieti — nevystavujte ich do internetu, pokiaľ ich neuzavriete do VPN.

## Vylepšenia Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) je vstavaná funkcia Evertagu pre **bezdrôtový prenos audio súborov medzi vaším počítačom a iPhonom alebo iPadom — bez iTunes, káblov alebo cloudového účtu**. Obe zariadenia musia byť na rovnakej Wi-Fi sieti.

V Evertag 4.2 Wi-Fi Drive získava:

- **Osviežené, moderné rozhranie** — čistejšie, ľahšie čitateľné na prvý pohľad a aktualizované pre Liquid Glass.
- **Režim viacnásobného výberu** — vyberte viacero súborov alebo priečinkov a pracujte s nimi hromadne.
- **Inteligentnejšia fronta nahrávania** — lepšia spätná väzba o priebehu a odolnosť voči výpadkom siete.
- **Vylepšená rýchlosť a celková spoľahlivosť** — rýchlejšie prenosy pre veľké knižnice.

Toto je najrýchlejší spôsob, ako presunúť dávku audio súborov z počítača do telefónu, upraviť ich značky a poslať ich späť — bez akejkoľvek služby tretej strany.

## Nastavenia editora značiek: hlboký ponor

Toto je časť, ktorú väčšina používateľov nikdy neprečíta — a časť, ktorá rozhoduje o tom, či vaše značky fungujú všade alebo len v niektorých aplikáciách. Otvorte Evertag a prejdite do sekcie **nastavenia editora audio značiek**. Tu je, čo každá možnosť skutočne robí a ktorú vybrať podľa vášho cieľa.

### Škálovanie obalu albumu

Keď ukladáte obal albumu do audio súboru, Evertag môže obrázok pred vložením zmenšiť. Dostupné možnosti:

- **Malý** — najmenší vplyv na veľkosť súboru, nižšia kvalita obrázka.
- **Stredný** — vyvážená voľba pre väčšinu používateľov.
- **Veľký** — vysoká kvalita, vhodná pre prehrávače s veľkými obrazovkami a CarPlay.
- **Veľmi veľký** — veľmi vysoká kvalita, viditeľný nárast veľkosti súboru.
- **Originálny (Vypnuté)** — vloží obal v pôvodnom rozlíšení. **Žiadne škálovanie.**

**Prečo na tom záleží:**

- **Vyššia kvalita = väčší súbor.** Obal 3 000 × 3 000 pixelov môže pridať niekoľko MB na každú skladbu. Pri celom albume sa záťaž disku rýchlo nahromadí.
- **Niektoré prehrávače si nedokážu poradiť s veľmi veľkými vloženými obrázkami.** Staršie zariadenia, niektoré autorádiá a niektoré staršie desktop prehrávače sa môžu zaseknúť na obaloch nad ~1 500 px alebo ich odmietnuť zobraziť.
- **Pre väčšinu cloudových a streamovacích pracovných postupov** je **Stredný** alebo **Veľký** ideálnym bodom. Použite **Originálny** len vtedy, keď konkrétne potrebujete archívnu kvalitu alebo pripravujete súbory pre prehrávač, ktorému dôverujete.

> Možnosť veľkosti **Originálny** je súčasťou prémiovej personalizačnej aktualizácie Evertag. Štandardné veľkosti (Malý/Stredný/Veľký/Veľmi veľký) sú zadarmo.

### Možnosti ukladania značiek: ID3v2.4 vs ID3v2.3

Toto je najdôležitejšie jednotlivé nastavenie pre kompatibilitu. ID3v2 je formát metadát používaný vnútri MP3 súborov. Existujú dve široko používané verzie a líšia sa v jemných, ale dôležitých detailoch.

#### ID3v2.4

- Novšia, podporuje **kódovanie textu UTF-8** — správne spracovanie nelatinkových písiem (čínština, ruština, japončina, arabčina, hebrejčina atď.).
- Viac typov rámcov (relatívna hlasitosť, predvoľby ekvalizéra atď.).
- **Odporúča sa pre moderné prehrávače**, ktoré ju podporujú.

#### ID3v2.3

- Staršia, ale **najuniverzálnejšie podporovaná** verzia ID3.
- Nepodporuje UTF-8 priamo (používa UTF-16 pre Unicode text).
- **Odporúča sa, keď potrebujete maximálnu kompatibilitu** so staršími prehrávačmi, autorádiami a niektorými desktop aplikáciami.

#### Kedy zapnúť ID3v2.4 v Evertagu

- Používate **moderné audio prehrávače** ako Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (aktuálne verzie) alebo moderné Android prehrávače. ✅ **Zapnite ID3v2.4.**
- Vaša knižnica obsahuje **nelatinkové znaky** (čínština, kórejčina, japončina, ruština, arabčina, gréčtina, hebrejčina). ✅ **Zapnite ID3v2.4** — UTF-8 ich spracováva oveľa čistejšie.

#### Kedy vypnúť ID3v2.4 v Evertagu (použite ID3v2.3)

- Pripravujete súbory pre **staršie autorádio alebo palubnú jednotku**, ktorá nečíta značky v2.4.
- Po úprave vidíte **rozhádzaný text alebo chýbajúce značky** v niektorých aplikáciách — to je silný signál, že tam v2.4 nie je podporovaný. Vráťte sa k v2.3.
- Cielite na **staršie desktop prehrávače** alebo staršie prenosné prehrávače (rané iPody, niektoré MP3 prehrávače z 2000–2010).

> **Praktické pravidlo:** ak sa vaše značky zobrazujú správne všade s v2.4, nechajte ho zapnutý. Ak čo i len jeden dôležitý prehrávač zobrazuje nesprávne znaky, prázdne alebo nečíta značky, vypnite v2.4 a uložte znova.

#### Duplikovanie značiek

Keď zapnete **Duplikovanie značiek**, Evertag zapisuje spoločné polia metadát (názov, interpret, album atď.) do **oboch sekcií ID3v1 a ID3v2** súboru. To zlepšuje kompatibilitu s veľmi starými prehrávačmi, ktoré čítajú iba ID3v1 (pôvodná značka 128 bajtov na konci súboru).

- **Väčšina používateľov to nepotrebuje.** Moderné prehrávače čítajú najprv ID3v2.
- **Aktivujte to len ak** pracujete s vintage hardvérom alebo špecifickým softvérom, ktorý ignoruje ID3v2.

### Aktualizácia online súborov: ako Evertag spracováva cloudové úpravy

Keď upravujete značky v súbore uloženom v pripojenom cloude (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP atď.), Evertag musí upravený súbor nahrať späť. Vy kontrolujete ako:

- **Zobraziť potvrdzovaciu správu** *(predvolené, odporúčané)* — Evertag sa pýta pred nahrávaním. Najlepšie pre opatrných používateľov a zdieľané knižnice.
- **Automaticky aktualizovať metadáta súboru** — nahráva potichu po každej úprave. Najlepšie pre používateľov s rýchlymi, spoľahlivými pripojeniami, ktorí veľa editujú.
- **Neaktualizovať metadáta súboru** — Evertag upravuje len lokálnu kópiu. Užitočné pre náhľad zmien bez ich poslania do cloudu.

### Úprava online súborov: čistenie lokálneho súboru

Na úpravu vzdialeného súboru ho Evertag najprv stiahne do vášho zariadenia. Po úprave si vyberiete, čo sa stane s tou lokálnou kópiou:

- **Vždy odstrániť stiahnutý súbor** — Evertag po úprave odstráni dočasný súbor. **Odporúčané**, ak máte málo úložiska alebo pracujete na cudzích súboroch.
- **Neodstrániť stiahnutý súbor** — ponecháva upravený súbor na vašom zariadení. Užitočné, keď chcete mať aj offline kópiu, aj aktualizovanú cloudovú kópiu.

### Tlačidlá na hlavnej obrazovke

Hlavná obrazovka editora značiek Evertag môže zobraziť alebo skryť tlačidlá pre jednotlivé operácie. Aktivujte len tie, ktoré skutočne používate, aby rozhranie zostalo zamerané:

- **Automaticky vyhľadať audio značky** — nájde chýbajúce metadáta online na základe audio odtlačku súboru.
- **Manuálne vyhľadať audio značky** — vyhľadávajte podľa názvu/interpreta, keď automatické vyhľadávanie zlyhá.
- **Vyhľadať obal albumu** — nájde a vloží obaly vysokej kvality.
- **Uložiť obal albumu** — exportuje vložený obal do vašej knižnice fotografií alebo súborov.
- **Normalizovať kódovanie** — opravuje rozhádzaný nelatinkový text spôsobený starými kódovaniami (veľmi užitočné pre cyrilické, čínske a japonské skladby ripnuté so starším softvérom).
- **Vymazať audio značky** — odstráni všetky značky zo súboru. Užitočné pred čistým novým označovaním.

### Zobraziť rozšírené značky

Aktivujte to na zobrazenie celej sady polí metadát mimo základného názov/interpret/album/rok — vrátane BPM, dirigenta, pôvodného interpreta, nálady, copyrightu, kódera, komentárov, textov a ďalšie. Funkcia pre pokročilých používateľov; väčšina bežných používateľov ju nepotrebuje.

### Upravovať súbory súčasne

Keď je zapnuté, Evertag vám umožňuje upravovať metadáta na **viacerých vybraných súboroch naraz** — nastavte rovnakého album artist, rok alebo žáner pre celý album v jednej operácii. Toto je najrýchlejší spôsob, ako vyčistiť veľkú neorganizovanú knižnicu.

## Úprava značiek pre Spotify, Apple Music a streamovacie platformy

Bežná otázka: «upravil som značky v Evertagu, nahral súbory a streamovacia služba zobrazuje nesprávne metadáta. Čo sa deje?»

Krátka odpoveď: **streamovacie služby vždy nerešpektujú vaše lokálne značky.** Apple Music a Spotify majú svoje vlastné interné databázy — keď rozpoznajú skladbu, prepíšu zobrazované metadáta vlastnými. Ale pre **nahrané súbory**, vaše lokálne súbory (funkcia «Knižnica» Apple Music, Spotify Local Files) a **nahrávky distribútorov na streamovacie platformy** vaše značky absolútne záležia. Tu je, ako nastaviť Evertag pre každý scenár:

### Príprava súborov pre Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music spracováva UTF-8 správne.
- **Obal albumu: Veľký** — aplikácie Apple zobrazujú veľké obaly dobre; Originálny je prehnaný.
- **Duplikovanie značiek: OFF** — nepotrebné.
- Uistite sa, že **Album Artist** je správne vyplnený — Apple Music ho používa na zoskupovanie.

### Príprava súborov pre Spotify Local Files

Spotify Local Files zobrazuje len súbory, ktoré sú dobre označené. Značky, ktoré Spotify číta, sú obmedzené.

- **ID3v2.4: ON** vo väčšine prípadov. Ak sa skladba po úprave v Spotify nezobrazuje správne, **skúste uložiť s ID3v2.4: OFF** (t. j. ako ID3v2.3) — parser Spotify bol historicky konzervatívny voči v2.4.
- **Obal albumu: Stredný alebo Veľký** — Spotify ho aj tak zmenší.
- Vyplňte aspoň **Názov**, **Interpret**, **Album** a **Číslo skladby**.

### Príprava súborov pre nahrávanie distribútorom (DistroKid, TuneCore, CD Baby atď.)

Ak ste interpret, ktorý nahráva vlastné dielo na streamovacie platformy, váš distribútor obvykle číta značky, ale tiež žiada metadáta vo svojom rozhraní. Tak či onak:

- **ID3v2.3** je často bezpečnejšia predvolená voľba — mnohé pipeliny distribútorov boli vybudované pred rokmi a uprednostňujú starší formát.
- Vložte **Veľký** obal (väčšina distribútorov vyžaduje obaly ≥ 1 400 × 1 400 px — overte si ich pokyny).
- Nespoliehajte sa na rozšírené značky — distribútori čítajú len základné polia.

### Príprava súborov pre Plex, Jellyfin, Navidrome, Subsonic, Emby

Tieto vlastné mediálne servery sú veľmi tolerantné. Čítajú aj v2.3, aj v2.4 čisto a dobre spracovávajú UTF-8.

- **ID3v2.4: ON** je v poriadku.
- **Obal albumu: Veľký** alebo **Veľmi veľký** — tieto servery podávajú obaly mobilným klientom a obrazovkám CarPlay, takže kvalita je dôležitá.
- **Album Artist** veľmi odporúčame — to používajú Plex/Jellyfin na správne zoskupenie albumov podľa interpreta.

### Príprava súborov pre autorádiá a starší hardvér

- **ID3v2.4: OFF** (použite ID3v2.3) — staršie hlavné jednotky často nepodporujú v2.4.
- **Obal albumu: Stredný** — mnohé autodisplaye sa zaseknú na veľkých vložených obaloch.
- **Duplikovanie značiek: ON** — staršie autorádiá niekedy čítajú len záložné ID3v1.

## Ďalšie vylepšenia

### Dizajn Liquid Glass

Rozhranie Evertag 4.2 je vyladené pre nový materiál **Liquid Glass** od Apple v celej aplikácii — priesvitné povrchy, plynulejšie animácie a zjemnené ovládacie prvky, ktoré prirodzene zapadnú do iOS, iPadOS a macOS.

### Aktualizované knižnice pripojení

Osvieženie sme interné knižnice, ktoré Evertag používa na komunikáciu s **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** a inými službami. Výsledok: menej zlyhaní pripojenia v okrajových prípadoch, lepšia podpora novších verzií serverov a lepšia spoľahlivosť pri úprave značiek vo vzdialených súboroch.

### Opravy prekladov a lokalizácie

Viaceré jazykové opravy v UI na základe priameho feedbacku od používateľov. Lepšie umiestnenie textu na menších tlačidlách v niekoľkých jazykoch.

### Menšie vylepšenia inšpirované vašou spätnou väzbou

Mnoho menších vylepšení založených na recenziách App Store a e-mailoch na support@everappz.com. Čítame každú správu.

## Získajte Evertag 4.2

[**Stiahnite si Evertag z App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) alebo aktualizujte cez App Store. Evertag je bezplatné stiahnutie s voliteľnými upgradmi v aplikácii pre pokročilé funkcie. Nové cloudové pripojenia, sieťové protokoly, vylepšenia Wi-Fi Drive a UI Liquid Glass sú súčasťou základnej aktualizácie.

Ak sa vám aplikácia páči, zanechajte hodnotenie v App Store — naozaj to pomôže. Máte spätnú väzbu alebo ste narazili na problém? Napíšte nám na **support@everappz.com**. Čítame každú správu.

## Často kladené otázky

{{% details title="Čo je nové v Evertag 4.2?" closed="true" %}}
Evertag 4.2 pridáva viac ako 6 nových cloudových a serverových pripojení (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), osviežený Wi-Fi Drive s viacnásobným výberom a inteligentnejšou frontou nahrávania, aktualizácie UI Liquid Glass, aktualizované knižnice pripojení, kľúčové opravy chýb úpravy značiek a vylepšenia prekladu.
{{% /details %}}

{{% details title="Mám v Evertagu používať ID3v2.4 alebo ID3v2.3?" closed="true" %}}
Použite **ID3v2.4** pre moderné prehrávače (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, moderné Android aplikácie) a pre knižnice s nelatinkovými znakmi — podpora UTF-8 znamená čistejšie značky v čínštine, kórejčine, japončine, ruštine, arabčine a hebrejčine. Použite **ID3v2.3**, ak sa vaše značky v niektorých aplikáciách zobrazujú nesprávne, ak cielite na staršie autorádiá alebo ak streamovací distribútor pipeline odmieta v2.4. Vždy môžete prepnúť a uložiť znova.
{{% /details %}}

{{% details title="Prečo sú moje značky po úprave v Spotify nesprávne?" closed="true" %}}
Spotify zobrazuje prevažne metadáta zo svojho katalógu — vaše lokálne značky sa používajú len pre «Local Files» alebo obsah, ktorý ste nahrali ako interpret. Ak označujete súbory pre Spotify Local Files a nezobrazujú sa správne, skúste vypnúť ID3v2.4 v Evertagu a uložiť ako ID3v2.3 — parser Spotify bol historicky konzervatívny voči v2.4.
{{% /details %}}

{{% details title="Akú veľkosť obalu albumu mám vybrať v Evertagu?" closed="true" %}}
Pre väčšinu používateľov: **Veľký**. Vyzerá skvele na telefónoch, iPadoch, Macoch a moderných auto displejoch bez prílišného nafukovania súborov. Použite **Stredný**, ak máte obrovskú knižnicu a chcete ušetriť disk. Použite **Originálny** (bez škálovania) len pre archívne mastre alebo keď skutočne potrebujete maximálnu kvalitu — ale uvedomte si, že niektoré staršie prehrávače majú problémy s veľmi veľkými vloženými obalmi. **Originálny** je súčasťou prémiovej personalizačnej aktualizácie Evertag.
{{% /details %}}

{{% details title="Zväčšia väčšie obaly albumov moje súbory?" closed="true" %}}
Áno. Vloženie obalu 3 000 × 3 000 px môže pridať niekoľko megabajtov k jednému audio súboru. V knižnici 1 000 skladieb to dosahuje gigabajty. Ak je úložisko obmedzené, použite Stredný alebo Veľký; ak streamujete z NAS, kde veľkosť nezáleží, Veľmi veľký alebo Originálny sú v poriadku.
{{% /details %}}

{{% details title="Čo je Duplikovanie značiek a mám ho aktivovať?" closed="true" %}}
Duplikovanie značiek zapisuje základné metadáta do oboch sekcií ID3v1 (legacy 128 bajtov) a ID3v2 (moderná) súboru. Aktivujte ho len ak cielite na veľmi staré prehrávače alebo hardvér, ktorý číta ID3v1. Pre všetko moderné (smartfóny, počítače, novšie autorádiá) ho nechajte vypnuté.
{{% /details %}}

{{% details title="Upravuje Evertag značky priamo v cloudových súboroch?" closed="true" %}}
Áno. Pripojte sa k svojmu cloudu (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 atď.) alebo cez FTP/SFTP/NFS, otvorte súbor a upravujte značky, akoby bol lokálny. Evertag stiahne súbor, aplikuje vaše úpravy a nahrá aktualizovanú verziu späť. V nastaveniach môžete vybrať medzi režimami «Vždy sa pýtať», «Auto-nahrať» alebo «Nenahrávať».
{{% /details %}}

{{% details title="Môžem upravovať FLAC značky na iPhone s Evertagom?" closed="true" %}}
Áno. Evertag podporuje FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE a ďalšie dôležité formáty s plnou podporou čítania/zápisu značiek vrátane vloženého obalu.
{{% /details %}}

{{% details title="Ako bezpečne upravím značky na svojom domácom serveri pomocou SFTP?" closed="true" %}}
Otvorte Evertag, prejdite na Pripojenia, vyberte SFTP a zadajte hostname alebo IP servera, port (zvyčajne 22), používateľské meno a heslo alebo súkromný SSH kľúč. Evertag prejde vaše vzdialené priečinky a bude upravovať značky priamo s end-to-end šifrovaním cez SSH.
{{% /details %}}

{{% details title="Môžem upravovať značky vo viacerých súboroch naraz?" closed="true" %}}
Áno. V nastaveniach aktivujte **Upravovať súbory súčasne**. Vyberte viacero súborov, otvorte editor značiek, a akékoľvek pole, ktoré zmeníte, sa aplikuje na všetky vybrané súbory. Toto je najrýchlejší spôsob, ako nastaviť rovnakého album artist, rok alebo žáner v celom albume.
{{% /details %}}

{{% details title="Je aktualizácia na Evertag 4.2 zadarmo?" closed="true" %}}
Áno. Evertag je bezplatné stiahnutie z App Store a 4.2 je bezplatná aktualizácia pre všetkých existujúcich používateľov. Nové cloudové integrácie, vylepšenia Wi-Fi Drive a UI Liquid Glass sú súčasťou základnej aktualizácie.
{{% /details %}}

{{% details title="Na akých zariadeniach je Evertag 4.2 dostupný?" closed="true" %}}
Evertag 4.2 funguje na iPhone, iPade a Macu. Synchronizácia iCloud Drive udržuje vaše nastavenia editora značiek konzistentné medzi zariadeniami.
{{% /details %}}
