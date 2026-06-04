---
title: "Pripojenia"
date: 2020-02-01
description: "Naučte sa, ako pripojiť cloudové služby a NAS zariadenia k Flacbox. Streamujte vysokorozlišovaciu hudbu z iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk a ďalších. Používajte SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing a USB flash disky."
keywords: [
  "nastavenie cloudu Flacbox", "pripojenie Google Drive k Flacbox", "streamovanie hudby SMB",
  "WebDAV iOS prehrávač", "DLNA hudobná aplikácia", "NAS audio streaming", "Wi-Fi Drive iPhone",
  "prenos súborov na iPhone", "Flacbox iTunes File Sharing", "pripojenie NAS k iPhone",
  "Synology Drive hudobná aplikácia", "QNAP hudobná aplikácia", "Bluesound hudobná aplikácia",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm scrobbling hudobná aplikácia",
  "iXpand Flash Drive hudba", "USB DAC iPhone"
]
tags: ["príručka", "flacbox", "pripojenia", "cloud", "NAS"]
readingTime: 12
---


Na tejto obrazovke môžete pripojiť každý zdroj, kde sa nachádza vaša hudba. Môžete integrovať populárne cloudové služby ako Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive a mnohé ďalšie, ako aj váš Mac, PC alebo NAS cez štandardné protokoly. Bez ohľadu na to, či vaša zbierka žije na streamovacej službe ako Dropbox alebo na osobnom NAS ako Synology, QNAP, Buffalo, Apple Time Capsule alebo WD My Cloud Home, Flacbox sa k nim všetkým pripojí z jednej obrazovky.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — obrazovka Pripojenia" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Pripojenie ku cloudovému úložisku

- Otvorte kartu **Pripojenia**.
- Z ponuky vyberte **Pripojiť ku cloudovému úložisku**.
- Zo zoznamu vyberte cloudovú úložnú službu.
- Na oficiálnej autorizačnej stránke poskytovateľa cloudu zadajte svoje prihlasovacie údaje a klepnite na **Hotovo**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — pridanie cloudovej úložnej služby" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Ak narazíte na problémy, skontrolujte internetové pripojenie a prihlasovacie meno / heslo. V Premium verzii aplikácie môžete pridať neobmedzený počet služieb; bezplatná verzia podporuje až tri.

## Podporované cloudové úložné služby, mediálne servery a protokoly

Flacbox podporuje mimoriadne širokú škálu zdrojov pre vašu hudbu. Všetko nižšie funguje z jednej obrazovky **Pripojiť ku cloudovému úložisku**.

**Osobné cloudové úložisko:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Vlastnohostedné servery:** Plex · Jellyfin · Emby · Subsonic (a každý Subsonic-kompatibilný server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (a ownCloud cez zdieľané API) · Synology Drive · QNAP.

**NAS a protokoly zdieľania súborov:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, heslo alebo autentifikácia verejným kľúčom) · NFS · DLNA / UPnP (prehrávanie a sťahovanie).

**S3-kompatibilné objektové úložisko:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a akýkoľvek iný S3-API endpoint.

**Objavovanie lokálnej siete:** Sekcia Dostupné zariadenia automaticky vypíše každú Bonjour / mDNS službu vo vašej sieti Wi-Fi, takže sa môžete pripojiť klepnutím bez zadávania IP adresy.

Každé pripojenie používa **oficiálne SDK alebo otvorený protokol** danej služby, s autorizáciou cez OAuth tam, kde je podporovaná. Môžete pripojiť viacero účtov tej istej služby (napríklad dva účty Google Drive, osobný Dropbox vedľa pracovného, alebo server Plex aj Jellyfin súčasne) a prehliadať ich vedľa seba na obrazovke Pripojenia.

## Bezpečnosť a súkromie

Na interakciu s pripojenými cloudovými službami používame iba oficiálne SDK a zabezpečené pripojenia. Vaše prihlasovacie meno a heslo nie sú prístupné aplikácii — všetky prenosy sú šifrované pomocou TLS.

Keď zadáte prihlasovacie meno a heslo, aplikácia vám zobrazí oficiálnu autorizačnú stránku poskytovanú cloudovou službou a celý autorizačný proces prebieha mimo aplikácie. Poskytovateľ cloudovej služby potom po úspešnej autorizácii odošle autorizačný token do aplikácie a tento token sa používa na volania API.

Autorizačný token je digitálny kľúč, ktorý umožňuje aplikáciám tretích strán pracovať s cloudovým úložiskom vo vašom mene. Token je uložený na vašom zariadení v zabezpečenom systémovom úložisku Apple (Keychain), ktoré je šifrované a chránené prístupovým kódom zariadenia alebo biometrickým zámkom. Môžete sťahovať súbory z pripojených cloudových služieb na vaše zariadenie; tieto súbory sú umiestnené v priečinku Dokumenty aplikácie a môžu byť kedykoľvek odstránené pomocou zabudovaného správcu súborov.

Aplikácia nezdieľa žiadne informácie z vašich pripojených cloudových účtov so spoločnosťou Everappz, inzerentmi ani žiadnou treťou stranou. Prístup k cloudovému účtu môžete kedykoľvek odvolať otvorením stránky nastavení účtu vo webovom prehliadači.

## Odvolanie autorizačného tokenu

Ak chcete odvolať autorizačný token, prihláste sa do cloudového účtu vo webovom prehliadači a prejdite na stránku zabezpečenia alebo pripojených aplikácií. Tam nájdete každú aplikáciu tretej strany pripojenú k vášmu cloudovému účtu a môžete odstrániť akúkoľvek z nich, ak ju už nechcete používať. Podrobné pokyny pre účty Google sú dostupné [tu](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Cloudový účet môžete odpojiť aj priamo v aplikácii — keď to urobíte, autorizačný token je okamžite vymazaný z vášho zariadenia. Ak odinštalujete aplikáciu zo zariadenia, všetky stiahnuté údaje a prístupové tokeny sa spolu s ňou automaticky odstránia.

## Odpojenie cloudového úložiska alebo zmena konfigurácie

- **Prístup k možnostiam cloudového úložiska** — nájdite pripojenú službu na obrazovke **Pripojenia**.
- **Klepnite na tlačidlo „..."** vedľa názvu služby a otvorte ďalšie možnosti:
  - **Premenovať** — zmeňte názov cloudovej služby tak, ako sa zobrazuje v zozname.
  - **Nastavenia** — upravte konfiguráciu alebo autentifikačné údaje. Niekedy môže byť potrebné znovu autorizovať pripojenú cloudovú službu, ak platnosť autorizačného tokenu vypršala.
  - **Odpojiť** — úplne prerušte spojenie medzi aplikáciou a cloudovou službou. Tým sa z hudobnej knižnice aplikácie odstránia všetky skladby priradené k tejto službe, no na serveri zostanú nedotknuté.

## Pripojenie k počítaču alebo NAS

Môžete tiež pripojiť váš počítač, osobný NAS alebo iné sieťové zariadenia pomocou protokolov SMB, DLNA alebo WebDAV. Je to najjednoduchší spôsob, ako preniesť existujúcu domácu hudobnú knižnicu — či už sa nachádza na Mac, Windows PC, Synology alebo NAS — do Flacbox bez kopírovania čohokoľvek.

## Pripojenie k počítaču pomocou SMB

- Klepnite na **Pripojiť ku cloudovému úložisku → SMB**.
- Do poľa URL zadajte IP adresu počítača a názov zdieľaného priečinka vo formáte `smb://ip-adresa-počítača/názov-zdieľaného-priečinka`.
- Vyberte verziu protokolu: **Auto**, **SMB1** alebo **SMB2**.
- Zadajte prihlasovacie meno a heslo (ak sa vyžaduje).
- Klepnite na **Hotovo**.

Ak je pripojenie úspešné, uvidíte pripojené úložisko v sekcii **Cloudové úložisko**. Kompletný návod na pripojenie vášho Mac alebo PC pomocou SMB je dostupný [tu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Pripojenie k NAS pomocou WebDAV

Všetky kroky sú rovnaké ako pri SMB, s výnimkou poľa URL. URL by malo byť vo formáte `http://názov-servera` alebo `https://názov-servera`, ak server podporuje SSL. WebDAV funguje so **Synology, QNAP, Nextcloud, ownCloud** a mnohými ďalšími servermi — kdekoľvek je dostupný WebDAV endpoint.

Kompletný návod na pripojenie NAS pomocou WebDAV je dostupný [tu](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Pripojenie k počítaču alebo NAS pomocou DLNA

Môžete tiež zdieľať hudobnú knižnicu umiestnenú na vašom Windows PC alebo osobnom NAS pomocou protokolu DLNA / UPnP a pristupovať k nej v aplikácii podľa popisu [tu](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA je populárny, široko podporovaný protokol, ale umožňuje iba prehrávanie alebo sťahovanie hudby — nie je možné nahrávať súbory ani vytvárať nové priečinky na DLNA serveri.

## Pripojenie k NAS alebo serveru pomocou FTP, FTPS alebo SFTP

Flacbox podporuje aj klasické protokoly na prenos súborov. Ak chcete pripojiť server cez FTP alebo FTPS, klepnite na **Pripojiť ku cloudovému úložisku → FTP**, zadajte URL hostiteľa vo forme `ftp://názov-servera` (alebo `ftps://názov-servera` pre šifrované pripojenie), zadajte prihlasovacie meno a heslo a klepnite na **Hotovo**. Pre **SFTP** (SSH File Transfer Protocol) vyberte **SFTP** a zadajte buď heslo alebo pár kľúčov SSH. Oba fungujú so zariadeniami NAS, Linux hostiteľmi a akýmkoľvek serverom, ktorý má démona FTP / FTPS / SSH.

## Pripojenie k NFS zdieľaniu

Flacbox obsahuje podporu **NFS** (Network File System) — praktické pre Linux hostiteľov, BSD servery a NAS zariadenia, ktoré radšej sprístupňujú hudobné knižnice cez NFS namiesto SMB. Vyberte **NFS** v ponuke **Pripojiť ku cloudovému úložisku**, zadajte adresu servera a exportovanú cestu a klepnite na **Hotovo**.

## Pripojenie k Plex Media Server

Flacbox sa môže priamo pripojiť k Plex Media Server a prehliadať vašu hudobnú knižnicu podľa Umelcov, Albumov, Žánrov a Prehrávačov. Klepnite na **Pripojiť ku cloudovému úložisku → Plex**, prihláste sa účtom Plex, vyberte server a knižnica sa zobrazí vedľa vašich cloudových služieb. Plex servery v rovnakej lokálnej sieti sú tiež automaticky objavené v sekcii **Dostupné zariadenia**.

## Pripojenie k serveru Jellyfin alebo Emby

Oba mediálne servery **Jellyfin** (open-source) aj **Emby** (komerčný) fungujú natívne v Flacbox. Klepnite na **Pripojiť ku cloudovému úložisku → Jellyfin** alebo **Emby**, zadajte URL servera (napríklad `http://ip-servera:8096`) a prihlasovacie údaje a vaša hudobná knižnica je pripravená na streamovanie. Rovnako ako pri Plex, knižnice v lokálnej sieti sú automaticky vypísané v sekcii **Dostupné zariadenia**.

## Pripojenie k serveru Subsonic alebo Navidrome

Flacbox hovorí Subsonic API, čo znamená, že funguje so samotným **Subsonic**, **Navidrome** a každým iným Subsonic-kompatibilným serverom — vrátane Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Klepnite na **Pripojiť ku cloudovému úložisku → Subsonic**, zadajte URL servera a prihlasovacie údaje a knižnica sa zobrazí na obrazovke Pripojenia. Je to najjednoduchší spôsob, ako dať Flacbox prístup k vlastnohostednej hudobnej zbierke bez odhalenia podkladového zdieľaného súboru.

## Pripojenie k S3-kompatibilnému objektovému úložisku

Pre vlastných hostiteľov a audiofanov používajúcich cloudové objektové úložisko obsahuje Flacbox S3-kompatibilný konektor. Klepnite na **Pripojiť ku cloudovému úložisku → S3 úložisko**, zadajte URL endpointu, región, prístupový kľúč, tajný kľúč a názov bucketa. Funguje s AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a akoukoľvek inou službou, ktorá sprístupňuje S3-API endpoint.

## Dostupné zariadenia

Táto sekcia zobrazuje každé zariadenie vo vašej lokálnej sieti, ku ktorému sa môžete z Flacbox pripojiť prostredníctvom Bonjour discovery. Ak chcete nadviazať pripojenie, postupujte podľa nasledujúcich krokov:

- Otvorte aplikáciu a prejdite do sekcie **Dostupné zariadenia** v časti Pripojenia.
- Klepnite na zariadenie, ku ktorému sa chcete pripojiť.
- V prípade potreby zadajte prihlasovacie údaje na dokončenie pripojenia.

Je to najrýchlejší spôsob objavenia SMB, WebDAV alebo DLNA zdieľania vo vašej domácej sieti bez ručného zadávania IP adries.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — dostupné zariadenia v lokálnej sieti" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive je praktická technológia, ktorá umožňuje bezdrôtový prenos súborov z počítača na iOS zariadenie prostredníctvom ľubovoľného desktopového prehliadača. Na efektívne používanie tejto funkcie sa uistite, že vaše zariadenie a počítač sú pripojené k rovnakej sieti Wi-Fi. Tu je podrobný sprievodca používaním Wi-Fi Drive.

### Povolenie Wi-Fi Drive

- Otvorte aplikáciu a prejdite na kartu **Pripojenia**.
- Výberom **Pripojiť cez Wi-Fi** sa dostanete na hlavnú obrazovku Wi-Fi Drive.
- (Voliteľné) Nastavte používateľské meno a heslo pre vstavaný webový server na ochranu prístupu.
- Klepnutím na **Spustiť Wi-Fi Drive** aktivujete Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Prístup k Wi-Fi Drive na počítači

- Na počítači (stolnom alebo prenosnom) otvorte webový prehliadač (napríklad Chrome, Firefox alebo Safari).
- Do adresného riadka prehliadača zadajte URL poskytnutú aplikáciou.

### Bezdrôtový prenos súborov

Keď sa webová stránka zodpovedajúca vášmu iOS zariadeniu otvorí v prehliadači, môžete jednoducho pretiahnuť súbory z počítača na webovú stránku. Presunuté súbory sa začnú prenášať na vaše iOS zariadenie a budú dostupné v aplikácii Flacbox.

Wi-Fi Drive môžete tiež pripojiť priamo vo Finderi na macOS (Prejsť → Pripojiť k serveru…) alebo v Prieskumníkovi súborov na Windows (Namapovať sieťový disk…) a pracovať s iPhone alebo iPad ako s bežným sieťovým diskom.

Podrobné pokyny na bezdrôtový prenos súborov pomocou Wi-Fi Drive sú dostupné [tu](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (od macOS Catalina Finder File Sharing) je ďalší spôsob prenosu súborov z počítača do zariadenia pomocou kábla Lightning alebo USB-C.

- Pripojte zariadenie k počítaču pomocou kábla a spustite **Finder** na Mac (alebo **iTunes** na Windows).
- Otvorte **Polohy → Vaše pripojené zariadenie → Súbory** a nájdite aplikáciu Flacbox.
- Klepnite na ikonu aplikácie a zobrazia sa všetky zdieľané priečinky.
- Presuňte súbory z počítača do zdieľaného priečinka na zariadení pomocou drag-and-drop.

Podrobné pokyny na používanie Finder File Sharing sú dostupné [tu](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Pripojenie USB Flash Disku

Ak máte SD kartu alebo USB disk, môžete ho pripojiť pomocou adaptéra Lightning na USB / čítačky SD kariet alebo USB-C disku (na iPad a iPhone 15 / 16 / 17 / Pro). Aplikácia podporuje čítačky kariet s certifikátom Apple a iXpand Flash Drives. Pri iXpand Flash Drive ho zasuňte do portu Lightning a otvorte aplikáciu — zobrazí sa správa o pripojení externého zariadenia s informáciami o zariadení. Klepnutím na ikonu flash disku sa dostanete do hudobného priečinka a klepnutím na ľubovoľný zvukový súbor spustíte prehrávanie.

Podrobné pokyny na pripojenie USB flash disku k iPhone a počúvanie hudby alebo správu súborov na ňom sú dostupné [tu](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Správca súborov

Po pripojení cloudovej úložnej služby klepnite na jej ikonu a zobrazí sa zoznam všetkých dostupných súborov a priečinkov. Pomocou zabudovaného správcu súborov môžete s týmito súbormi pracovať — sťahovať, premenovávať, presúvať, nahrávať, mazať a ďalšie. Keď spustíte sťahovanie, súbor sa zobrazí vo fronte prenosov. Ak chcete otvoriť front prenosov, prejdite na kartu Lokálne súbory a klepnite na ikonu rotujúcich šípok v ľavom hornom rohu. Všetky stiahnuté súbory a priečinky sú dostupné v sekcii Lokálne súbory.

## Horná lišta nástrojov

Horná lišta nástrojov, ktorá sa nachádza pod navigačnou lištou, ponúka niekoľko užitočných akcií pre rýchly prístup. Môžete ju zobraziť alebo skryť jednoduchým potiahnutím nadol.

- **Hľadať** — rýchle vyhľadávanie v aktuálnom adresári, čo uľahčuje nájdenie konkrétnych súborov alebo priečinkov.
- **Pokračovať v prehrávaní** — ak je povolené v nastaveniach aplikácie, obnoví frontu audio prehrávača a posledné pozície médií pre aktuálny priečinok. Praktický spôsob, ako pokračovať tam, kde ste skončili.
- **Prehrať všetko** — prehľadá aktuálny priečinok a jeho podpriečinky a potom pridá všetky nájdené zvukové súbory do novej fronty prehrávača. Užitočné, keď chcete prehrať každú skladbu v adresári.
- **Zamiešať všetko** — podobne ako Prehrať všetko, ale súbory zamiešal pred pridaním do fronty audio prehrávača. Skvelé na znovuobjavovanie starého priečinka s hudbou.

## Možnosti priečinka

Keď otvoríte priečinok, nájdete praktickú sadu akcií dostupných klepnutím na tlačidlo **„..."** v pravom hornom rohu.

- **Vybrať** — aktivujte režim výberu súborov. Umožňuje vám vybrať jeden alebo viac súborov v priečinku a vykonať akcie na celom výbere.
- **Nový priečinok** — vytvorte nový priečinok v aktuálnom priečinku. Skvelé na udržiavanie dobre štruktúrovanej knižnice.
- **Povoliť offline režim** — zapnite offline režim pre aktuálny priečinok. Offline režim presahuje jednoduché sťahovanie: aktívne sleduje zmeny v priečinku. Ak online pridáte nové súbory, automaticky sa objavia na vašom zariadení.
- **Nahrať súbory** — nahrajte súbory zo zariadenia do online priečinka. Tým ich sprístupníte odkiaľkoľvek cez rovnakú cloudovú službu.
- **Hľadať** — vyhľadajte konkrétne súbory v aktuálnom priečinku.
- **Zoradiť** — zoraďte súbory podľa názvu, veľkosti, dátumu úpravy alebo metadát. Predvolený režim zoradenia odráža poradie zoradenia na serveri, ale môžete ho zmeniť podľa svojich preferencií.
- **Zobrazenie mriežka / zoznam** — prepínajte medzi zobrazením tabuľky a miniatúrami. Zobrazenie tabuľky zobrazuje kompaktný zoznam; zobrazenie miniatúr zobrazuje veľké ukážky obalov pre rýchlu vizuálnu identifikáciu.

## Úprava online súborov

Keď potrebujete spravovať viac súborov v cloudovom úložisku, použite **Režim výberu** na zefektívnenie akcií:

- **Aktivujte Režim výberu** — klepnite na tlačidlo **„..."** v pravom hornom rohu a vyberte **Vybrať**.
- **Vyberte súbory** — vedľa každého súboru a priečinka sa zobrazia zaškrtávacie políčka. Klepnutím vyberte jednu alebo viac položiek.
- **Vykonajte akcie** — po výbere súborov alebo priečinkov budete mať prístup k: Prehrať ďalej, Prehrať neskôr, Pridať do hudobnej knižnice, Pridať do prehrávača, Kopírovať, Nahrať, Presunúť, Premenovať a Vymazať.

Ak chcete pripojenú cloudovú službu tratovať ako len na čítanie (aby ste predišli náhodnému mazaniu), aktivujte Nastavenia → Správca súborov → Upraviť online súbory → Vypnuté, čo skryje všetky deštruktívne operácie z rozhrania.

## Akcie so súbormi

Klepnutím na ikonu **„..."** pri názve súboru zobrazíte ponuku akcií:

- **Prehrať ďalej** — vloží súbor na začiatok fronty prehrávača, takže sa prehrá ihneď po aktuálnej skladbe.
- **Prehrať neskôr** — pridá súbor na koniec fronty prehrávača.
- **Pridať do hudobnej knižnice** — zaradí súbor do hudobnej knižnice usporiadanej podľa interpreta, albumu, žánru alebo skladateľa.
- **Pridať do prehrávača** — pridá súbor do existujúceho prehrávača alebo vytvorí nový.
- **Upraviť audio tagy** — otvorí zabudovaný editor tagov na úpravu metadát. Pri online súboroch sa skladba dočasne stiahne, upraví a potom znovu nahráva po potvrdení.
- **Pridať k obľúbeným** — pridá súbor do zoznamu obľúbených pre rýchly prístup.
- **Stiahnuť** — stiahne súbor alebo priečinok do zariadenia na offline použitie.
- **Premenovať** — premenuje súbor priamo na vzdialenom úložisku.
- **Presunúť** — premiestni súbor do iného priečinka v cloudovom úložisku.
- **Otvoriť v** — exportuje súbor do inej kompatibilnej aplikácie. Súbor sa stiahne do zariadenia a potom sa zobrazí systémový panel Zdieľanie.
- **Vymazať** — natrvalo odstráni súbor z cloudového úložiska. **Túto akciu nie je možné vrátiť späť.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — ďalšie akcie pre súbor v pripojenom cloudovom úložisku" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Ak zoznam akcií presahuje dostupné miesto na obrazovke, jednoducho posuňte nadol v ponuke akcií, aby ste zobrazili ďalšie možnosti.

## Akcie s priečinkami

Pre každý priečinok v cloudovom úložisku máte k dispozícii širokú škálu akcií klepnutím na ikonu **„..."** vedľa názvu priečinka. Ak nevidíte všetky akcie, posuňte nadol, aby ste zobrazili viac.

- **Prehrať všetko** — nahradí aktuálnu frontu prehrávača všetkými položkami vo vybranom priečinku.
- **Prehrať ďalej** — pridá celý priečinok na začiatok fronty prehrávača.
- **Prehrať neskôr** — pridá obsah priečinka na koniec fronty prehrávača.
- **Pridať do hudobnej knižnice** — zaradí obsah priečinka do hudobnej knižnice.
- **Pridať do prehrávača** — pridá celý priečinok do prehrávača. Máte tiež možnosť vytvoriť nový prehrávač; jeho názov sa automaticky vyplní z názvu priečinka.
- **Pridať k obľúbeným** — pridá priečinok do obľúbených pre rýchly prístup.
- **Povoliť offline režim** — nad rámec jednoduchého sťahovania priebežne sleduje priečinok na nové súbory a automaticky ich sťahuje, keď sa objavia online.
- **Stiahnuť** — stiahne celý obsah priečinka do zariadenia pre offline prístup.
- **Premenovať** — premenuje priečinok priamo na vzdialenom úložisku.
- **Presunúť** — premiestni priečinok na iné miesto v cloudovom úložisku.
- **Archivovať (ZIP)** — zabalí obsah priečinka do jedného ZIP súboru (funkcia Premium).
- **Vymazať** — natrvalo odstráni priečinok a jeho obsah z cloudového úložiska. **Túto akciu nie je možné vrátiť späť.**

## Rýchly prístup

Sekcia Rýchly prístup sa nachádza v hornej časti obrazovky. Poskytuje rýchly prístup k obľúbeným a nedávno otváraným súborom z pripojených cloudových služieb. Vždy, keď otvoríte súbor alebo priečinok z cloudu, pridá sa do zoznamu Nedávno otvorené. Ak chcete zoznam vymazať, otvorte Nedávne, klepnite na tlačidlo Viac akcií a vyberte Vymazať zoznam. Môžete tiež označiť hlboko vnorené priečinky ako Obľúbené, aby ste k nim mali rýchly prístup bez prehľadávania adresárovej štruktúry.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — online prepojenia a rýchly prístup" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Ostatné služby

Táto sekcia zobrazuje doplnkové funkcie, ktoré vylepšujú váš zážitok. V súčasnosti aplikácia podporuje scrobbling **Last.fm** — keď je pripojený, štatistiky prehrávania sa automaticky posielajú na váš účet Last.fm. Neskôr môžete navštíviť profil Last.fm a zobraziť analýzy počúvania a získať personalizované odporúčania hudby. Podrobné pokyny na nastavenie sú dostupné [tu](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — pripojenie Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
