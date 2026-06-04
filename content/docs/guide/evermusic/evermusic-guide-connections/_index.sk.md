---
title: "Pripojenia"
date: 2020-01-01
description: "Naučte sa, ako pripojiť cloudové služby, počítače, NAS zariadenia a spravovať hudobné súbory pomocou Evermusic. Sprievodca krok za krokom pre Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing a ďalšie."
keywords: [
  "Evermusic", "cloudový hudobný prehrávač", "NAS streamovanie", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "pripojenie cloudového úložiska", "prenos hudby iPhone", "správca súborov iOS"
]
tags: ["evermusic", "sprievodca", "pripojenia"]
readingTime: 11
---


Na obrazovke Pripojenia môžete pripojiť každý zdroj, ktorý obsahuje vašu hudbu — obľúbené cloudové služby, vlastnohostitené mediálne servery, váš Mac alebo PC, osobný NAS, Apple Time Capsule, WD My Cloud Home, dokonca aj USB flash disk — a používať ich všetky z jedného jednotného rozhrania. Pripojenia je tiež miesto, kde nastavíte Rýchly prístup k hlboko vnoreným cloudovým priečinkom a kde overíte Last.fm pre scrobbling.

Obrazovka je rozdelená do zreteľne označených sekcií, takže sa škáluje od jedného účtu iCloud Drive až po knižnicu rozloženú naprieč viacerými cloudmi a NAS zariadeniami: Rýchly prístup v hornej časti (vaše obľúbené cloudové priečinky), Cloudové úložisko (účty, ktoré ste pridali), Lokálna sieť (zariadenia objavené cez Bonjour), Počítač (Wi-Fi Drive, iTunes File Sharing, SMB), Externé príslušenstvo (pripojené USB flash disky) a Ďalšie služby (Last.fm a podobné).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Connections Screen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Pripojiť sa ku cloudovému úložisku

- Otvorte kartu Pripojenia.
- Vyberte Pripojiť sa ku cloudovému úložisku z menu.
- Vyberte cloudovú úložnú službu zo zoznamu.
- Prihláste sa na oficiálnej autorizačnej stránke poskytovateľa (Evermusic nikdy nevidí vaše heslo).
- Klepnite na Hotovo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Connect Cloud Storage Provider Picker" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Ak narazíte na problémy, skontrolujte svoje internetové pripojenie a prihlasovacie údaje a uistite sa, že dvojfaktorová autentifikácia je správne nakonfigurovaná pre danú službu.  
V prémiовej verzii aplikácie môžete pridať neobmedzený počet služieb. Bezplatní používatelia môžu pripojiť jeden cloudový účet naraz.

## Podporované cloudové úložné služby

Evermusic podporuje celú škálu populárnych cloudových a vlastnohostitených služieb. Bezplatní používatelia získajú rovnaký katalóg poskytovateľov, ale s limitom jedného účtu; Premium odomyká neobmedzené účty a odstraňuje väčšinu ostatných limitov.

- **Osobné cloudové účty:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Vlastnohostitené servery a mediálne knižnice:** Plex · Jellyfin · Emby · Subsonic (a každý Subsonic-kompatibilný server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (a Owncloud, cez zdieľané API) · Synology Drive · QNAP.
- **NAS a protokoly zdieľania súborov:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (heslo alebo autentifikácia verejným kľúčom), NFS a DLNA (iba na čítanie — prehrávanie a sťahovanie).
- **S3-kompatibilné objektové úložisko:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage alebo akýkoľvek S3-API endpoint.
- **Objavovanie v lokálnej sieti:** sekcia Dostupné zariadenia automaticky zobrazuje každé zariadenie vo vašej Wi-Fi, ktoré sa inzeruje cez Bonjour / mDNS — servery Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, AirPort routery s pripojenými diskami atď.

## Bezpečnosť a súkromie

Používame iba oficiálne SDK a zabezpečené pripojenie na interakciu s pripojenými cloudovými službami. Vaše prihlasovacie meno a heslo nie sú dostupné pre aplikáciu. Všetky požiadavky z aplikácie na cloudovú službu sú šifrované.

Keď zadáte svoje prihlasovacie meno a heslo, aplikácia vám zobrazí oficiálnu autorizačnú stránku poskytnutú poskytovateľom cloudovej služby a celý autorizačný proces prebieha mimo aplikácie. Poskytovateľ cloudovej služby odošle autorizačný token do aplikácie po úspešnej autorizácii a tento token sa používa na volania API.

Auth-token je digitálny kľúč, ktorý umožňuje aplikáciám tretích strán komunikovať s cloudovým úložiskom. Auth-token je uložený na vašom zariadení v bezpečnom systémovom úložisku nazývanom Keychain. Môžete si stiahnuť súbory z pripojenej cloudovej služby do zariadenia a tieto súbory budú umiestnené v adresári „Documents" aplikácie. Tieto súbory môžete kedykoľvek odstrániť pomocou vstavaného správcu súborov.

Aplikácia nezdieľa žiadne informácie z pripojeného cloudového účtu. Prístup ku svojmu cloudovému účtu môžete kedykoľvek zrušiť otvorením stránky nastavení účtu vo webovom prehliadači.

## Zrušenie auth-tokenu

Prihláste sa do svojho účtu vo webovom prehliadači a prejdite na stránku nastavení. Tam nájdete všetky aplikácie tretích strán, ktoré sú pripojené k vášmu cloudovému účtu, a môžete ich odstrániť, ak ich viac nechcete používať. Podrobné pokyny sú dostupné [tu](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Môžete tiež odpojiť pripojené cloudové účty v aplikácii a auth token bude tiež odstrá­nený z vášho zariadenia. Ak odstránite aplikáciu zo svojho zariadenia, všetky stiahnuté dáta a prístupové tokeny budú tiež odstrá­nené.

## Odpojiť cloudové úložisko alebo zmeniť konfiguráciu

- Prístup k možnostiam cloudového úložiska: najprv nájdite cloudové úložisko, ktoré chcete spravovať, v rozhraní aplikácie.
- Klepnite na tlačidlo „...": vedľa názvu služby uvidíte tlačidlo „...". Klepnite naň pre prístup k ďalším možnostiam.
  - **Premenovať**: ak chcete zmeniť názov cloudovej služby tak, ako sa zobrazuje vo vašom zozname, vyberte „Premenovať".
  - **Nastavenia**: ak chcete upraviť konfiguráciu alebo autentifikačné údaje cloudovej služby, vyberte „Nastavenia". Niekedy môžete potrebovať znova autorizovať pripojenú cloudovú službu, ak platnosť autorizačného tokenu vypršala.
  - **Odpojiť**: ak chcete úplne prerušiť spojenie medzi aplikáciou a cloudovou službou, vyberte „Odpojiť". Majte na pamäti, že výberom tejto možnosti sa odstrá­nia všetky skladby priradené k tejto cloudovej službe z hudobnej knižnice aplikácie, ale zostanú na serveri.

{{< cards cols="1">}}
  {{< card title="" subtitle="Connected Cloud Storage More Actions Menu" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Pripojiť sa k počítaču alebo NAS

Môžete tiež pripojiť svoj počítač, osobný NAS alebo iné sieťové zariadenia pomocou protokolu SMB, DLNA alebo WebDAV.

## Pripojiť sa k počítaču pomocou SMB

- Klepnite na „Pripojiť sa ku cloudovému úložisku" → SMB.
- Zadajte IP adresu počítača a názov zdieľaného priečinka do poľa URL vo formáte smb://computer-ip-address/shared-folder-name
- Vyberte verziu protokolu: Auto, SMB1, SMB2
- Zadajte prihlasovacie meno a heslo (ak je požadované)
- Klepnite na „Hotovo".

Ak je vaše pripojenie úspešné, uvidíte pripojené úložisko v sekcii „Cloudové úložisko".  
Kompletný návod, ako pripojiť váš MAC alebo PC pomocou SMB, je dostupný [tu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB Connection Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Pripojiť sa k NAS pomocou WebDAV

Všetky kroky sú rovnaké, len pole URL je iné.  
URL by malo byť vo formáte http://server-name alebo https://server-name, ak server podporuje SSL.
Kompletný návod, ako pripojiť NAS pomocou protokolu WebDAV, je dostupný [tu](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV Connection Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Pripojiť sa k počítaču alebo NAS pomocou DLNA

Môžete tiež zdieľať hudobnú knižnicu umiestnenú na vašom Windows PC alebo osobnom NAS pomocou protokolu DLNA a pristupovať k tejto knižnici v aplikácii ako je opísané [tu](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA je populárny a široko používaný protokol, ale umožňuje len prehrávanie alebo sťahovanie hudby. Nemôžete nahrávať súbory ani vytvárať nové priečinky na serveri.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA Connection Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Dostupné zariadenia

Táto sekcia zobrazuje všetky zariadenia vo vašej lokálnej sieti, ku ktorým sa môžete pripojiť prostredníctvom aplikácie.  
Na nadviazanie spojenia so zariadením postupujte podľa nasledujúcich krokov:

- Otvorte aplikáciu a prejdite do sekcie „Dostupné zariadenia".
- Klepnite na zariadenie, ku ktorému sa chcete pripojiť, zo zoznamu.
- Ak je to potrebné, zadajte svoje prihlasovacie údaje na dokončenie pripojenia.

{{< cards cols="1">}}
  {{< card title="" subtitle="Available Devices on the Local Network" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive je pohodlná technológia, ktorá umožňuje bezdrôtový prenos súborov z počítača na vaše iOS zariadenie cez desktopový prehliadač.  
Aby ste túto funkciu mohli efektívne používať, uistite sa, že vaše zariadenie a počítač sú pripojené k rovnakej sieti Wi-Fi.  
Tu je sprievodca krok za krokom, ako používať Wi-Fi Drive.

## Aktivovať Wi-Fi Drive

- Otvorte aplikáciu a prejdite na kartu „Pripojenia".
- Vyberte „Pripojiť cez Wi-Fi" pre prístup k hlavnej obrazovke Wi-Fi Drive.
- Klepnite na „Spustiť Wi-Fi Drive" na aktiváciu Wi-Fi Drive.

## Prístup k Wi-Fi Drive na vašom počítači

- Na vašom počítači (desktope alebo notebooku) otvorte webový prehliadač (napríklad Chrome, Firefox alebo Safari).
- Do adresného riadku prehliadača zadajte URL poskytnutú aplikáciou.

## Bezdrôtový prenos súborov

Keď sa webová stránka zodpovedajúca vášmu iOS zariadeniu otvorí v prehliadači, môžete jednoducho presúvať súbory z počítača na webovú stránku.  
Súbory, ktoré presúvate, sa začnú prenášať na vaše iOS zariadenie a budú prístupné v aplikácii.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive Server Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Podrobné pokyny o tom, ako bezdrôtovo prenášať súbory pomocou WiFi-Drive, sú dostupné [tu](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing je ďalšia technológia, ktorá vám umožňuje prenášať súbory z počítača do zariadenia pomocou aplikácie Finder na vašom Mac a lightning kábla.  
- Jednoducho pripojte zariadenie k počítaču pomocou kábla a spustite aplikáciu Finder na vašom Mac.
- Otvorte „Umiestnenia" → „Vaše pripojené zariadenie" → „Súbory" → a nájdite aplikáciu Evermusic.
- Klepnite na ikonu aplikácie, aby ste videli všetky zdieľané priečinky.
- Kopírujte súbory z počítača do zdieľaného priečinka na zariadení pomocou presúvania.

Podrobné pokyny o tom, ako používať iTunes file sharing, sú dostupné [tu](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing on Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Pripojiť USB flash disk

Ak máte SD kartu, môžete ju pripojiť pomocou lightning čítačky kariet. Aplikácia momentálne podporuje Apple Certified čítačky kariet a iXpand Flash Drives. Ak máte iXpand Flash Drive — vložte ho do lightning portu a otvorte aplikáciu. Uvidíte správu „Pripojené externé zariadenie" a informácie o zariadení. Jednoducho klepnite na ikonu flash disku pre prístup k hudobnému priečinku a klepnite na ľubovoľný audio súbor a začnite prehrávanie. Máme podrobné pokyny, ako pripojiť USB flash disk k iPhone a počúvať hudbu alebo spravovať súbory na ňom umiestnené, dostupné [tu](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Správca súborov

Po pripojení cloudovej úložnej služby klepnite na jej ikonu pre zobrazenie všetkých dostupných súborov a priečinkov. Môžete použiť vstavaný správca súborov na prácu s týmito súbormi — sťahovanie, premenovanie, presúvanie a ďalšie. Keď začnete sťahovanie, súbor sa objaví vo fronte prenosov. Pre zobrazenie frontu prenosov prejdite na kartu „Lokálne súbory" a klepnite na točiace sa šípky v ľavom hornom rohu. Všetky stiahnuté súbory a priečinky sú dostupné v sekcii „Lokálne súbory".

## Horný panel nástrojov

Horný panel nástrojov, umiestnený pod navigačnou lištou, ponúka niekoľko užitočných akcií pre jednoduchý prístup. Tento panel nástrojov môžete zobraziť alebo skryť jednoduchým gestom potiahnutia nadol. Tu sú dostupné akcie:

- **Hľadať**: Táto možnosť vám umožňuje vykonať rýchle vyhľadávanie v aktuálnom adresári, čím uľahčuje nájdenie konkrétnych súborov alebo priečinkov.
- **Pokračovať v prehrávaní**: Ak je to povolené v nastaveniach aplikácie, táto funkcia obnoví front audio prehrávača a poslednú pozíciu médiá pre aktuálny priečinok. Je to praktický spôsob, ako pokračovať tam, kde ste skončili vo svojej hudobnej knižnici.
- **Prehrať všetko**: Výberom tejto akcie aplikácia prehľadá aktuálny priečinok a jeho podpriečinky, pričom pridá všetky nájdené audio súbory do nového frontu prehrávača. Toto je užitočné, keď chcete prehrať všetku hudbu v konkrétnom adresári.
- **Náhodne prehrať všetko**: Podobné ako „Prehrať všetko", táto akcia prehľadá aktuálny priečinok a jeho podpriečinky, ale zamieša súbory pred ich pridaním do frontu audio prehrávača. Je to skvelý spôsob, ako si vychutnať hudbu v náhodnom poradí pre trochu rozmanitosti.

{{< cards cols="1">}}
  {{< card title="" subtitle="Top Toolbar Inside a Cloud Folder" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Možnosti priečinka

Keď otvoríte priečinok v aplikácii, nájdete praktickú sadu akcií dostupnú klepnutím na tlačidlo „..." v pravom hornom rohu obrazovky.  
Tu je prehľad týchto akcií:

- **Vybrať**: Aktivujte režim výberu súborov. Tento režim vám umožňuje vybrať jeden alebo viac súborov v priečinku, čo uľahčuje vykonávanie akcií na vybraných položkách.
- **Nový priečinok**: Vytvorte nový priečinok v rámci aktuálneho priečinka. Táto funkcia vám umožňuje organizovať súbory a udržiavať knižnicu dobre štruktúrovanú.
- **Povoliť offline režim**: Zapnite offline režim pre aktuálny priečinok. Offline režim ide za jednoduché sťahovanie; aktívne monitoruje priečinok na zmeny. Ak do priečinka online pridáte nové súbory, aplikácia ich automaticky stiahne do vášho zariadenia. To zaisťuje, že vaša lokálna knižnica zostáva aktuálna so zmenami na serveri.
- **Nahrať súbory**: Nahrajte súbory zo svojho zariadenia do online priečinka. Táto akcia vám umožňuje prenášať súbory do cloudu alebo na server, čím sú prístupné odkiaľkoľvek.
- **Hľadať**: Vyhľadajte konkrétne súbory v aktuálnom priečinku. Toto je obzvlášť užitočné na rýchle nájdenie konkrétnych položiek vo veľkej zbierke.
- **Zoradiť**: Zoraďte súbory v priečinku podľa kritérií, ako je názov, veľkosť alebo dátum úpravy. Predvolený režim zoradenia zvyčajne zrkadlí poradie zoradenia na serveri, ale môžete ho zmeniť podľa svojich predstáv.
- **Zobrazenie mriežky/zoznamu**: Prepínajte medzi dvoma režimami zobrazenia: tabuľkové zobrazenie a zobrazenie miniatúr. Tabuľkové zobrazenie prezentuje súbory v zozname, zatiaľ čo zobrazenie miniatúr zobrazuje vizuálne reprezentácie súborov, čo uľahčuje identifikáciu obsahu na prvý pohľad.

{{< cards cols="1">}}
  {{< card title="" subtitle="Current Folder More Actions Menu" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Upraviť online súbory

Keď potrebujete spravovať viacero súborov v cloudovom úložisku v Evermusic, môžete použiť režim výberu na zefektívnenie vašich akcií. Pre efektívnu správu súborov postupujte podľa týchto krokov:

- **Aktivovať režim výberu**: Otvorte aplikáciu na svojom zariadení a prejdite do sekcie obsahujúcej vaše cloudové úložisko. Hľadajte v pravom hornom rohu tlačidlo „..." (elipsa). Klepnite naň a vyberte položku menu „Vybrať" na aktiváciu režimu výberu.
- **Vybrať súbory**: Vedľa každého súboru alebo priečinka v zozname sa zobrazia zaškrtávacie políčka. Vyberte jeden alebo viac súborov alebo priečinkov jednoduchým klepnutím na zaškrtávacie políčka vedľa nich.
- **Vykonať rôzne akcie**: Po výbere súborov alebo priečinkov, ktoré chcete spravovať, budete mať prístup k niekoľkým akciám prispôsobeným vašim potrebám:

{{< cards cols="1">}}
  {{< card title="" subtitle="Selection Mode for Online Files" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Akcie so súbormi

Vedľa názvu súboru uvidíte symbol elipsy „..." (tri bodky) — toto je menu akcií.  
Klepnite naň pre zobrazenie zoznamu dostupných akcií:

- **Prehrať ďalej**: Vyberte túto akciu na vloženie vybraného súboru na začiatok frontu prehrávača, čím sa zabezpečí, že sa prehrá ihneď po aktuálne prehrávanej položke.
- **Prehrať neskôr**: Výberom tejto možnosti sa súbor pridá na koniec frontu prehrávača, čím sa zabezpečí, že sa prehrá po existujúcom fronte.
- **Pridať do hudobnej knižnice**: Táto akcia vám umožňuje zaradiť súbor do hudobnej knižnice, čím bude ľahko prístupný a prehľadne usporiadaný podľa interpreta, albumu, žánru alebo skladateľa.
- **Pridať do playlistu**: Použite túto akciu na pridanie súboru do existujúceho playlistu alebo vytvorenie nového.
- **Upraviť audio tagy**: Výberom tejto možnosti môžete pristupovať k vstavanému editoru tagov Evermusic, čo vám umožní upravovať audio tagy pre vybraný súbor. Súbor bude dočasne stiahnutý do dočasného adresára a potom nahraný do úložiska po potvrdení zmien.
- **Pridať do obľúbených**: Táto akcia pridá súbor do vášho zoznamu obľúbených súborov pre rýchly a pohodlný prístup.
- **Stiahnuť**: Vyberte túto akciu na stiahnutie súboru alebo priečinka do vášho zariadenia, čím bude prístupný pre offline použitie.
- **Premenovať**: Táto možnosť vám umožňuje premenovať súbor priamo na vzdialenom úložisku, čo umožňuje vlastné pomenovanie súborov.
- **Presunúť**: Vyberte túto akciu na premiestnenie súboru do iného priečinka v rámci vášho cloudového úložiska, čím pomáhate udržiavať organizovanú štruktúru súborov.
- **Otvoriť v**: Použite túto akciu na export súboru do inej kompatibilnej aplikácie. Súbor bude stiahnutý do vášho zariadenia a potom sa zobrazí dialóg Zdieľať pre ďalšie zdieľanie alebo interakciu.
- **Vymazať**: Pri tejto akcii buďte opatrní, pretože trvalo odstraňuje súbor z vášho cloudového úložiska. Toto vymazanie nemožno vrátiť späť.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu for a Single File" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Ak zoznam akcií presahuje dostupný priestor na obrazovke, jednoducho sa posúvajte nadol v menu akcií pre prístup k ďalším možnostiam.

## Akcie s priečinkami

Pre každý priečinok v cloudovom úložisku máte k dispozícii rôzne akcie. Pre prístup k týmto možnostiam jednoducho klepnite na ikonu elipsy „..." umiestnenú vedľa názvu priečinka. Ak nevidíte všetky akcie, posuňte sa nadol pre zobrazenie ďalších možností. Tu sú dostupné akcie:

- **Prehrať všetko**: Nahraďte aktuálny front prehrávača všetkými položkami z vybraného priečinka.
- **Prehrať ďalej**: Pridajte celý priečinok na začiatok frontu prehrávača, hneď za aktuálne prehrávanú položku.
- **Prehrať neskôr**: Pridajte obsah priečinka na koniec frontu prehrávača.
- **Pridať do hudobnej knižnice**: Táto akcia bezproblémovo zaraďuje obsah priečinka do hudobnej knižnice, čím je ľahko prístupný a prehľadne usporiadaný podľa interpreta, albumu, žánru alebo skladateľa.
- **Pridať do playlistu**: Môžete zaradiť celý priečinok do playlistu. Máte tiež možnosť vytvoriť nový playlist a názov priečinka bude automaticky priradený.
- **Pridať do obľúbených**: Použite túto akciu na pridanie priečinka do zoznamu obľúbených súborov pre rýchly a pohodlný prístup.
- **Povoliť offline režim**: Povolením offline režimu pre vybraný priečinok aplikácia ide za jednoduché sťahovanie. Nepretržite skenuje zmeny a ak sú do online priečinka pridané nové súbory, budú automaticky stiahnuté do aplikácie.
- **Stiahnuť**: Stiahnite celý obsah priečinka do zariadenia pre offline prístup.
- **Premenovať**: Premenujte priečinok priamo na vzdialenom úložisku.
- **Presunúť**: Premiestnite priečinok na iné miesto v rámci cloudového úložiska.
- **Vymazať**: Buďte opatrní pri tejto akcii, pretože trvalo odstraňuje priečinok a jeho obsah z vášho cloudového úložiska. Túto akciu nemožno vrátiť späť.


## Rýchly prístup

Sekcia Rýchly prístup sa nachádza v hornej časti obrazovky. Poskytuje vám rýchly prístup k vašim obľúbeným a nedávno otvoreným súborom z pripojených cloudových služieb.
Vždy, keď otvoríte súbor alebo priečinok z cloudu, je pridaný do zoznamu „Nedávno otvorené". Na vymazanie tohto zoznamu otvorte „Nedávne", klepnite na tlačidlo „Viac akcií" a vyberte „Vymazať zoznam". Môžete tiež označiť hlboko vnorené priečinky ako Obľúbené, aby ste k nim mali rýchly prístup bez prehľadávania štruktúry adresárov.

## Ďalšie služby

Táto sekcia zobrazuje ďalšie funkcie, ktoré vylepšujú váš zážitok. Momentálne aplikácia podporuje scrobbling Last.fm. Po pripojení sú vaše štatistiky prehrávania automaticky odosielané na váš Last.fm účet. Neskôr môžete navštíviť svoj profil Last.fm, aby ste si prezreli analytiku počúvania a dostali personalizované odporúčania hudby. Podrobné pokyny na nastavenie sú dostupné [tu](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
