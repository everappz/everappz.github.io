---
title: "Súbory"
date: 2020-02-01
lastmod: 2026-06-01
description: "Naučte sa používať kartu Súbory v Evervideo na iPhone, iPad a Mac. Pripojte cloudové služby, NAS zariadenia, mediálne servery a RTSP streamy na jednom mieste. Spravujte offline videá, frontu prenosov, stiahnuté súbory, Wi-Fi Drive, zdieľanie súborov iTunes / Finder a USB disky. Zahŕňa iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA a S3-kompatibilné úložisko."
keywords: [
  "Evervideo súbory", "Evervideo pripojenia", "Evervideo miestne súbory",
  "nastavenie cloudového videa iPhone", "pripojenie Google Drive video", "SMB streamovanie videa",
  "WebDAV prehrávač videa iOS", "DLNA video iPhone", "NAS streamovanie videa",
  "prenos videa Wi-Fi Drive", "Evervideo zdieľanie súborov iTunes", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo offline režim videa", "Evervideo fronta prenosov",
  "Evervideo správca súborov", "Evervideo priečinok Documents",
  "prehrávač videa Synology", "prehrávač videa QNAP",
  "prehrávač videa Apple Time Capsule", "USB DAC video",
  "iXpand prehrávač videa", "S3 prehrávač videa"
]
tags: ["sprievodca", "evervideo", "súbory", "pripojenia", "cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Karta Súbory je univerzálny správca súborov Evervideo. Na rozdiel od väčšiny video aplikácií, ktoré rozdelia cloudové úložisko od miestnych súborov do rôznych kariet, Evervideo zlučuje oba do jednej obrazovky s posúvaním, takže môžete prejsť zo servera Plex na cloudový priečinok a potom do priečinka Documents vášho iPhone bez prepínania medzi kartami.

Karta Súbory je rozdelená do jasných sekcií, ktoré sa na vašej obrazovke zobrazujú v tomto poradí:

- **Rýchly prístup** — posledné a obľúbené súbory a priečinky, ktoré ste naposledy otvorili.
- **Súbory v tejto aplikácii** — čo sa nachádza v ohraničenom priečinku Documents Evervideo.
- **Súbory na tomto iPhone / iPad / Mac** — videá inde na vašom zariadení, zobrazené cez systémový výber súborov.
- **Cloudové úložisko** — každý cloudový účet, NAS a mediálny server, ktorý ste pripojili.
- **Dostupné zariadenia** — servery a disky na vašej miestnej sieti automaticky objavené cez Bonjour / mDNS.

V pravom hornom rohu obrazovky Súbory je tlačidlo Prenosy (ikona točiacich sa šípok). Klepnutím na ňu otvoríte frontu prenosov, kde monitorujete každé stiahnutie a nahrávanie naprieč všetkými vašimi zdrojmi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo súbory naprieč pripojenými úložiskami" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Pripojenie k cloudovému úložisku

Sekcia Cloudové úložisko karty Súbory je miestom, kde žije každý pripojený účet, NAS, mediálny server a stream — vedľa seba, v jednom posúvacom zozname.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sekcia cloudového úložiska Evervideo v karte Súbory" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Otvorte kartu **Súbory**.
- Prejdite na sekciu **Cloudové úložisko**.
- Klepnite na **Pripojiť k cloudovému úložisku** z menu.
- Vyberte cloudovú úložnú službu zo zoznamu.
- Zadajte svoje prihlasovacie údaje na oficiálnej autorizačnej stránke poskytovateľa cloudu, potom klepnite na **Hotovo**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo pripojenie cloudovej úložnej služby" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Ak narazíte na problémy, skontrolujte svoje internetové pripojenie a prihlasovacie meno / heslo. V Premium verzii aplikácie môžete pridať neobmedzený počet služieb; bezplatná verzia podporuje až tri.

## Podporované cloudové úložné služby, mediálne servery a protokoly

Evervideo podporuje výnimočne široký rozsah zdrojov pre vaše videá. Všetko nižšie funguje cez jediný tok pripojenia k cloudovému úložisku.

**Osobné cloudové úložisko:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Lokálne mediálne servery:** Plex · Jellyfin · Emby · Subsonic (a každý Subsonic-kompatibilný server — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (a ownCloud cez zdieľané API) · Synology Drive · QNAP.

**NAS a protokoly zdieľania súborov:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, heslo alebo autentifikácia verejným kľúčom) · NFS · DLNA / UPnP (prehrávanie a stiahnutie).

**Live a IP kamera streamy:** RTSP — namieriť Evervideo na akúkoľvek `rtsp://` URL a ono len prehráva. Skvelé pre bezpečnostné kamery, IPTV streamy, zvonkové kamery, detské monitory a podobné live zdroje.

**S3-kompatibilné objektové úložisko:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a akýkoľvek iný S3-API endpoint.

**Knižnice na zariadení:** knižnica Photos (všetky videá, nahrávky obrazovky, fotoalbumy) a knižnica aplikácie Music (Albumy, Žánre, Playlisty) — obe sa zobrazujú v Mediálnej knižnici, takže nemusíte nič kopírovať.

**Objavovanie lokálnej siete:** sekcia Dostupné zariadenia automaticky zobrazuje každú Bonjour / mDNS službu na vašej Wi-Fi sieti — Plex, Jellyfin, Emby servery, Synology, QNAP, AirPort routery s pripojenými diskami, Apple Time Capsule — takže môžete klepnutím pripojiť bez zadávania IP adresy.

Každé pripojenie používa oficiálne SDK alebo otvorený protokol služby, s autorizáciou na báze OAuth tam, kde je podporovaná. Môžete pripojiť viacero účtov rovnakej služby (napríklad dva účty Google Drive, alebo Plex aj Jellyfin server) a prehliadať ich vedľa seba v sekcii Cloudové úložisko.

## Bezpečnosť a súkromie

Evervideo používa iba oficiálne SDK a zabezpečené pripojenia na interakciu s pripojenými cloudovými službami. Vaše prihlasovacie meno a heslo nie sú prístupné aplikácii — všetky prenosy sú šifrované TLS.

Keď zadáte prihlasovacie meno a heslo, aplikácia vám zobrazí oficiálnu autorizačnú stránku poskytovateľa cloudovej služby a celý proces autorizácie prebieha mimo aplikácie. Poskytovateľ cloudovej služby potom po úspešnej autorizácii odošle auth-token aplikácii a ten sa používa na volania API.

Auth-token je digitálny kľúč, ktorý umožňuje aplikáciám tretích strán interagovať s cloudovým úložiskom vo vašom mene. Token je uložený na vašom zariadení v zabezpečenom systémovom úložisku Apple (Keychain), ktoré je šifrované v pokoji a chránené vašim prístupovým kódom zariadenia alebo biometrickým zámkom. Môžete sťahovať súbory z pripojených cloudových služieb na vaše zariadenie; tieto súbory sú umiestnené v adresári Documents aplikácie a môžu byť kedykoľvek odstránené pomocou vstavaného správcu súborov.

Aplikácia nezdieľa žiadne informácie z vašich pripojených cloudových účtov s Everappz, inzerentmi ani akoukoľvek treťou stranou. Prístup k vášmu cloudovému účtu môžete kedykoľvek odvolať otvorením stránky nastavení účtu vo vašom webovom prehliadači.

## Odmietnutie Auth-Token

Ak chcete odvolať auth-token, prihláste sa do svojho cloudového účtu vo webovom prehliadači a prejdite na stránku zabezpečenia alebo pripojených aplikácií. Tam nájdete každú aplikáciu tretej strany pripojenú k vášmu cloudovému účtu a môžete odstrániť akúkoľvek z nich, ak ju už nechcete používať. Podrobné pokyny pre účty Google sú k dispozícii [tu](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Cloudový účet môžete odpojiť aj priamo v aplikácii — keď to urobíte, auth-token je okamžite vymazaný z vášho zariadenia. Ak odinštalujete aplikáciu zo zariadenia, všetky stiahnuté dáta a prístupové tokeny sú automaticky s ňou odstránené.

## Odpojenie cloudového úložiska alebo zmena konfigurácie

- **Prístup k možnostiam cloudového úložiska** — nájdite pripojenú službu v sekcii **Cloudové úložisko** karty Súbory.
- **Klepnite na tlačidlo "..."** vedľa názvu služby na otvorenie ďalších možností:
  - **Premenovať** — zmeňte názov cloudovej služby tak, ako sa zobrazuje vo vašom zozname.
  - **Nastavenia** — upravte konfiguráciu alebo autentifikačné údaje. Niekedy môžete potrebovať znovu autorizovať pripojenú cloudovú službu, ak platnosť autorizačného tokenu vypršala.
  - **Odpojiť** — úplne prerušte prepojenie medzi aplikáciou a cloudovou službou. Toto odstráni všetky videá spojené s touto službou z vašej mediálnej knižnice, ale nechá ich nedotknuté na serveri.

## Pripojenie k počítaču alebo NAS

Počítač, osobný NAS alebo iné sieťové zariadenie môžete pripojiť pomocou protokolu SMB, WebDAV, FTP / FTPS, SFTP, NFS alebo DLNA. Toto je najjednoduchší spôsob, ako preniesť existujúcu domácu mediálnu knižnicu — či už sa nachádza na Macu, Windows PC, Synology, QNAP, Apple Time Capsule alebo WD My Cloud Home — do Evervideo bez kopírovania čohokoľvek.

### Pripojenie k počítaču pomocou SMB

- Klepnite na **Pripojiť k cloudovému úložisku → SMB**.
- Zadajte IP adresu počítača a názov zdieľaného priečinka pomocou formátu `smb://computer-ip-address/shared-folder-name`.
- Vyberte verziu protokolu: **Auto**, **SMB1** alebo **SMB2**.
- Zadajte prihlasovacie meno a heslo (ak je potrebné).
- Klepnite na **Hotovo**.

Ak je pripojenie úspešné, zdieľaná položka sa zobrazí v sekcii Cloudové úložisko. Kompletný návod na pripojenie Macu alebo PC pomocou SMB je k dispozícii [tu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Pripojenie k NAS pomocou WebDAV

Všetky kroky sú rovnaké ako pri SMB, okrem poľa URL. Použite `http://server-name` alebo `https://server-name`, ak server podporuje SSL. WebDAV funguje so Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home a akýmkoľvek iným serverom s WebDAV endpointom.

Kompletný návod na WebDAV je k dispozícii [tu](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Pripojenie cez DLNA / UPnP

Zdieľajte mediálnu knižnicu nachádzajúcu sa na vašom Windows PC alebo NAS pomocou protokolu DLNA / UPnP a pristupujte k nej v Evervideo ako je popísané [tu](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA je široko podporovaný, ale umožňuje iba prehrávanie alebo stiahnutie videí — nemôžete nahrávať súbory ani vytvárať nové priečinky na DLNA serveri.

### Pripojenie pomocou FTP, FTPS alebo SFTP

Evervideo tiež podporuje klasické protokoly prenosu súborov. Ak chcete pripojiť server cez FTP alebo FTPS, klepnite na Pripojiť k cloudovému úložisku → FTP, zadajte URL hostiteľa vo forme `ftp://server-name` (alebo `ftps://server-name` pre šifrované pripojenie), zadajte prihlasovacie meno a heslo, potom klepnite na Hotovo. Pre SFTP (SSH File Transfer Protocol) vyberte namiesto toho SFTP a zadajte buď heslo alebo pár SSH kľúčov.

### Pripojenie k NFS zdieľaniu

Evervideo obsahuje podporu NFS (Network File System) — užitočné pre Linux hostitelia, BSD servery a NAS zariadenia, ktoré uprednostňujú sprístupnenie video knižníc cez NFS namiesto SMB. Vyberte NFS v menu Pripojiť k cloudovému úložisku, zadajte adresu servera a exportovanú cestu, a klepnite na Hotovo.

## Pripojenie mediálneho servera Plex

Evervideo sa môže pripojiť priamo k Plex Media Server a prehliadať vaše knižnice Filmy, TV relácie a Domáce videá. Klepnite na Pripojiť k cloudovému úložisku → Plex, prihláste sa pomocou svojho účtu Plex, vyberte server a knižnica sa objaví vedľa vašich cloudových služieb. Servery Plex v rovnakej lokálnej sieti sú tiež automaticky objavené v sekcii Dostupné zariadenia.

## Pripojenie servera Jellyfin alebo Emby

Oba Jellyfin (open-source) a Emby (komerčné) mediálne servery fungujú natívne v Evervideo. Klepnite na Pripojiť k cloudovému úložisku → Jellyfin alebo Emby, zadajte URL vášho servera (zvyčajne niečo ako `http://server-ip:8096`) a prihlasovacie údaje, a vaša knižnica je pripravená na streamovanie.

## Pripojenie servera Subsonic alebo Navidrome

Evervideo hovorí Subsonic API, čo znamená, že funguje so Subsonic, Navidrome a každým iným Subsonic-kompatibilným serverom — vrátane Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) a Ampache. Klepnite na Pripojiť k cloudovému úložisku → Subsonic, zadajte URL servera a prihlasovacie údaje, a knižnica sa objaví v sekcii Cloudové úložisko.

## Pripojenie RTSP streamu (IP kamery, živá TV, IPTV)

Evervideo má natívnu podporu RTSP, takže ho môžete nasmerovať na akýkoľvek zdroj RTSP — bezpečnostné kamery, zvonkové kamery, poskytovatelia IPTV, detské monitory, broadcast zdroje — a Evervideo bude sťahovať a dekódovať stream naživo. Klepnite na Online Linky → Pridať link, vložte celú URL (`rtsp://camera-ip:port/stream-path`), zadajte prihlasovacie meno a heslo ak je potrebné, a klepnite na Hotovo.

## Pripojenie k S3-kompatibilnému objektovému úložisku

Pre samohostitelia a pokročilých používateľov využívajúcich cloudové objektové úložisko, Evervideo obsahuje S3-kompatibilný konektor. Klepnite na Pripojiť k cloudovému úložisku → S3 úložisko, potom zadajte URL endpointu, región, prístupový kľúč, tajný kľúč a názov bucketu. Funguje s AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a akýmkoľvek iným S3-API endpointom.

## Dostupné zariadenia

Táto sekcia zobrazuje každé zariadenie na vašej lokálnej sieti, ku ktorému sa môžete pripojiť z Evervideo cez Bonjour / mDNS objavovanie — Plex, Jellyfin, Emby servery, Synology, QNAP, AirPort routery s pripojenými diskami, Apple Time Capsule atď. Postup pri nadviazaní pripojenia:

- Prejdite na sekciu Dostupné zariadenia v karte Súbory.
- Klepnite na zariadenie, ku ktorému sa chcete pripojiť.
- Ak je potrebné, zadajte prihlasovacie údaje na dokončenie pripojenia.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo dostupné zariadenia na lokálnej sieti" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive vám umožňuje prenášať súbory bezdrôtovo z počítača na iOS zariadenie cez akýkoľvek desktopový prehliadač, Finder alebo File Explorer. Vaše zariadenie a počítač musia byť v rovnakej Wi-Fi sieti.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Povolenie Wi-Fi Drive

- V karte Súbory prejdite na Cloudové úložisko → Pripojiť cez Wi-Fi na otvorenie hlavnej obrazovky Wi-Fi Drive.
- (Voliteľné) Nastavte používateľské meno a heslo pre vstavaný webový server.
- Klepnite na Spustiť Wi-Fi Drive.

### Prístup k Wi-Fi Drive na počítači

- Otvorte webový prehliadač na počítači (Chrome, Firefox, Safari atď.).
- Zadajte URL zobrazenú aplikáciou.
- Pretiahnite súbory z počítača na webovú stránku — začnú sa prenášať na vaše iOS zariadenie.

Môžete tiež pripojiť Wi-Fi Drive priamo vo **Finderi** na macOS (Prejsť → Pripojiť k serveru…) alebo File Explorer na Windows (Mapovať sieťový disk…) a zaobchádzať s iPhone alebo iPad ako s bežným sieťovým diskom.

Podrobné pokyny sú k dispozícii [tu](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Zdieľanie súborov iTunes / Finder

Zdieľanie súborov iTunes (teraz Zdieľanie súborov Finder na macOS Catalina a novšom) vám umožňuje prenášať súbory pomocou kábla Lightning alebo USB-C. Pripojte zariadenie, otvorte Finder na Macu (alebo iTunes na Windows), nájdite Evervideo v zozname aplikácií a skopírujte súbory do jeho zdieľaného priečinka.

## Pripojenie USB flash disku alebo SD karty

Zapojte USB disk alebo SD kartu do iPhone, iPad alebo Mac cez adaptér Lightning-na-USB / USB-C alebo čítačku kariet. Otvorte Súbory → Súbory na tomto iPhone → Otvoriť priečinok, prejdite na disk a vyberte súbor videa alebo priečinok. Evervideo prehráva súbory priamo z disku bez kopírovania na internú pamäť — vhodné pre veľké 4K knižnice.

## Prehliadanie priečinkov v pripojených úložiskách

Klepnutím na akúkoľvek pripojenú cloudovú službu otvoríte jej prehliadač súborov. Priečinky zobrazujú miniatúry videa, keď sú dostupné, a klepnutím na video sa okamžite spustí prehrávanie, pričom sa na pozadí pokračuje v streamovaní zvyšku súboru.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo prehliadanie priečinkov v pripojených úložiskách" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Rýchly prístup

Sekcia Rýchly prístup sa nachádza v hornej časti karty Súbory. Poskytuje rýchly prístup k obľúbeným a naposledy otvoreným súborom a priečinkom — z cloudových služieb aj z úložiska na zariadení. Vždy keď otvoríte súbor alebo priečinok z cloudu, pridá sa do zoznamu Naposledy otvorené. Hlboko vnorené priečinky môžete označiť ako Obľúbené, aby ste k nim mali rýchly prístup bez prehliadania adresárovej štruktúry.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo online linky a rýchly prístup" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Súbory v tejto aplikácii

Táto sekcia zobrazuje súbory a priečinky uložené v ohraničenom adresári Documents Evervideo — všetko, čo ste stiahli z cloudu, preniesli cez Wi-Fi Drive, skopírovali cez Zdieľanie súborov Finder alebo importovali z inej aplikácie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo súbory v tejto aplikácii" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Priečinok Documents

Priečinok Documents je koreňom všetkého v Súboroch v tejto aplikácii. Môžete vytvárať podpriečinky, premenovávať súbory, presúvať ich a triediť ich podľa potreby.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo miestne súbory — priečinok Documents" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Súbory na tomto iPhone / iPad / Mac

Táto sekcia zobrazuje videá nachádzajúce sa na vašom zariadení, ale v rôznych aplikáciách. Môžete ich importovať do Evervideo pomocou systémového výberu súborov:

- Klepnite na Otvoriť súbory… na výber konkrétnych súborov.
- Klepnite na Otvoriť priečinok… na výber celého priečinka.

Môžete tiež použiť Pripojiť priečinok na vytvorenie odkazu na priečinok na vašom zariadení s prístupom na čítanie / zápis — ideálne pre prácu s priečinkom na iCloud Drive alebo pripojeným USB diskom bez kopírovania čohokoľvek.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo súbory na tomto zariadení" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Špeciálne priečinky

V karte Súbory uvidíte niekoľko špeciálnych priečinkov, ktoré Evervideo vytvára a automaticky používa:

- **Stiahnuté** — každý súbor stiahnutý z cloudu sa tu zobrazuje predvolene. Prispôsobte v Nastavenia → Správca súborov → Uložiť stiahnuté súbory do.
- **Vyrovnávacia pamäť prehrávača** — vyrovnávacia pamäť mediálneho prehrávača. Predvolene prehrávač sťahuje nadchádzajúce videá pre plynulé prehrávanie. Môžete vypnúť vyrovnávaciu pamäť v nastaveniach aplikácie alebo jednoducho odstrániť tento priečinok.
- **iCloud** — súbory v tomto priečinku sa synchronizujú naprieč všetkými vašimi zariadeniami pripojenými k rovnakému účtu iCloud.
- **Offline priečinky** — keď označíte priečinok, playlist, album alebo žáner ako dostupný offline, súbory sa stiahnu do tohto priečinka.

## Horný panel nástrojov

Horný panel nástrojov, nachádzajúci sa pod navigačnou lištou, ponúka niekoľko akcií, ktoré môžete zobraziť alebo skryť gestom potiahnutia nadol:

- **Hľadať** — vyhľadajte v aktuálnom priečinku alebo sekcii.
- **Pokračovať v prehrávaní** — ak je povolené v nastaveniach, obnoví frontu prehrávača a poslednú pozíciu videa pre aktuálny priečinok.
- **Prehrať všetko** — prehľadá aktuálny priečinok a jeho podpriečinky a pridá súbory do fronty prehrávača.
- **Prehrať náhodne** — ako Prehrať všetko, ale pred pridaním náhodne zmieša.

## Možnosti priečinka

Keď otvoríte priečinok, klepnite na tlačidlo **"..."** v pravom hornom rohu pre tieto akcie:

- **Vybrať** — aktivovať režim výberu súborov.
- **Nový priečinok** — vytvoriť nový priečinok v aktuálnom priečinku.
- **Povoliť offline režim** — zapnúť synchronizáciu offline pre aktuálny priečinok. Nové súbory pridané online sa automaticky stiahnu.
- **Nahrať súbory** — nahrať súbory z vášho zariadenia do online priečinka.
- **Hľadať** — vyhľadávať v priečinku.
- **Zoradiť** — zoradiť súbory podľa názvu, veľkosti, dátumu zmeny alebo metadát.
- **Zobrazenie mriežky / zoznamu** — prepínať medzi zobrazením tabuľky a miniatúr. Zobrazenie miniatúr zobrazuje veľké ukážky videí.

## Režim výberu

Klepnite na **"..."** v pravom hornom rohu a vyberte **Vybrať** na vstup do režimu výberu. Vedľa každého súboru a priečinka sa zobrazia zaškrtávacie políčka. Klepnutím vyberte jeden alebo viac položiek, potom vykonajte hromadné akcie: Prehrať ďalej, Prehrať neskôr, Pridať do mediálnej knižnice, Pridať do playlistu, Kopírovať, Nahrať, Presunúť, Premenovať alebo Odstrániť.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo režim výberu v správcovi súborov" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Ak radšej považujete pripojené cloudové úložisko za iba na čítanie (aby ste zabránili náhodným vymazaniam), povolte Nastavenia → Správca súborov → Upraviť online súbory → Vypnúť na skrytie všetkých deštruktívnych operácií z UI.

## Akcie so súbormi

Klepnite na ikonu **"..."** pri názve súboru na zobrazenie menu akcií:

- **Prehrať ďalej** — vložiť súbor na vrchol fronty prehrávača.
- **Prehrať neskôr** — pripojiť súbor na spodok fronty prehrávača.
- **Pridať do mediálnej knižnice** — zahrnúť súbor do mediálnej knižnice, organizovanej podľa albumu a žánru.
- **Pridať do playlistu** — pridať súbor do existujúceho playlistu alebo vytvoriť nový.
- **Upraviť tagy** — otvoriť vstavaný editor tagov na úpravu metadát. Pre online súbory sa súbor dočasne stiahne, upraví a potom znovu nahrá po potvrdení.
- **Pridať k obľúbeným** — pridať súbor do zoznamu obľúbených pre rýchly prístup.
- **Stiahnuť** — stiahnuť súbor alebo priečinok na zariadenie pre offline použitie.
- **Premenovať** — premenovať súbor priamo na vzdialenom úložisku.
- **Presunúť** — premiestniť súbor do iného priečinka v cloudovom úložisku.
- **Pridať do archívu** — zbaliť súbor do jediného ZIP súboru (funkcia Premium).
- **Otvoriť v** — exportovať súbor do inej kompatibilnej aplikácie cez systémový panel Zdieľať.
- **Odstrániť** — natrvalo odstrániť súbor. **Táto akcia sa nedá vrátiť späť.**

## Akcie s priečinkom

Pre každý priečinok v cloudovom úložisku máte k dispozícii mnohé akcie klepnutím na ikonu **"..."** vedľa názvu priečinka.

- **Prehrať všetko** — nahradiť aktuálnu frontu prehrávača každým videom v priečinku.
- **Prehrať ďalej / Prehrať neskôr** — pridať celý priečinok do fronty.
- **Pridať do mediálnej knižnice** — zahrnúť obsah priečinka do mediálnej knižnice.
- **Pridať do playlistu** — pridať celý priečinok do playlistu.
- **Pridať k obľúbeným** — pridať priečinok k obľúbeným.
- **Povoliť offline režim** — okrem jednoduchého stiahnutia, toto nepretržite monitoruje priečinok na nové súbory a automaticky ich stiahne po ich objavení online.
- **Stiahnuť** — stiahnuť celý obsah priečinka na zariadenie pre offline prístup.
- **Premenovať / Presunúť** — premenovať alebo premiestniť priečinok na vzdialenom úložisku.
- **Pridať do archívu** — zbaliť obsah priečinka do ZIP súboru (funkcia Premium).
- **Odstrániť** — natrvalo odstrániť priečinok a jeho obsah. **Táto akcia sa nedá vrátiť späť.**

## Fronta prenosov

V pravom hornom rohu karty Súbory je tlačidlo **Prenosy** (ikona točiacich sa šípok). Klepnutím na ňu otvoríte Frontu prenosov — zoznam každého aktívneho stiahnutia a nahrávania naprieč všetkými vašimi zdrojmi, s reálnym časom, rýchlosťou a odhadovaným časom dokončenia pre každý súbor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo fronta prenosov súborov" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Môžete pozastaviť, obnoviť, zopakovať neúspešné prenosy, preskupovať položky na uprednostnenie konkrétnych stiahnutí alebo ich jednotlivo zrušiť. Môžete tiež nastaviť rýchlosť fronty prenosov (maximálne paralelné úlohy), typ siete (iba Wi-Fi alebo Wi-Fi + Mobilné dáta) a prenosy na pozadí v Nastavenia → Správca súborov.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo akcie v fronte prenosov súborov" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offline režim a synchronizované offline priečinky

Offline režim je šikovná funkcia, ktorá vám umožňuje sledovať obľúbené videá aj bez pripojenia na internet. Keď povolíte offline režim pre akýkoľvek priečinok, playlist, album alebo žáner, všetky súbory v tejto kolekcii sa automaticky stiahnu na vaše zariadenie pre offline prehrávanie. Zobrazujú sa v sekcii Offline priečinky.

Keď na vzdialený server pridáte nové súbory, automaticky sa tiež stiahnu — takže vaša offline kolekcia zostáva aktuálna bez toho, aby ste museli čokoľvek robiť. Na manuálnu synchronizáciu klepnite na tri bodky v pravom hornom rohu offline priečinka a vyberte Synchronizovať.

Interval synchronizácie môžete nastaviť v Nastavenia → Správca súborov → Synchronizované offline priečinky → Časový interval.

Podrobné pokyny sú k dispozícii [tu](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalizácia

V Nastavenia → Personalizácia môžete nakonfigurovať spôsob zobrazenia karty Súbory:

- **Štýl obrazovky súborov** — Jednoduché menu (zobrazí zoznam priečinkov priamo) alebo Skupinové menu (zoskupí obsah podľa kategórie — Rýchly prístup, Špeciálne priečinky, Cloudové úložisko atď.).
