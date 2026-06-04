---
title: "Pripojenia"
date: 2020-02-01
description: "Naučte sa, ako pripojiť cloudové úložisko, NAS a počítač k Evertag. Pristupujte k audio súborom a upravujte ich priamo z cloudového úložiska, osobného NAS alebo Mac/PC."
keywords: [
  "nastavenie cloudu Evertag", "pripojenie iCloud k Evertag", "prístup k SMB súborom iOS",
  "WebDAV editor audio tagov", "úprava metadát NAS", "Wi-Fi Drive Evertag",
  "prenos audio súborov na iPhone", "Evertag iTunes File Sharing", "úprava FLAC tagov z cloudu"
]
tags: ["návod", "evertag", "pripojenia"]
readingTime: 11
---


Na tejto obrazovke môžete pripojiť rôzne zdroje obsahujúce vaše audio súbory. Môžete integrovať populárne cloudové služby ako Google Drive, Dropbox, OneDrive, iCloud a ďalšie, ako aj pripojiť váš Mac alebo PC. Okrem toho máte možnosť upravovať audio súbory umiestnené v Apple Time Capsule, WD Cloud Home alebo akomkoľvek NAS, ktorý podporuje SMB alebo WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka Pripojenia Evertag" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Rýchly prístup

V hornej časti obrazovky Pripojenia nájdete zoznam **Rýchleho prístupu**. Každý cloudový priečinok, ktorý pridáte do obľúbených – aj keď je zanorený niekoľko úrovní hlboko – sa tu zobrazí, aby ste k nemu mohli prejsť bez toho, aby ste zakaždým prechádzali nadriadenými priečinkami.

## Pripojenie k cloudovému úložisku

- Otvorte záložku 'Pripojenia'
- Vyberte 'Pripojiť k cloudovému úložisku' z ponuky
- Zo zoznamu vyberte službu cloudového úložiska
- Zadajte prihlasovacie údaje a klepnite na 'Hotovo.'

Ak narazíte na problémy, skontrolujte internetové pripojenie a prihlasovacie meno/heslo.  
V prémiowej verzii aplikácie môžete pridať neobmedzený počet služieb.

## Podporované cloudové úložiská

V súčasnosti aplikácia podporuje najpopulárnejšie cloudové úložiská: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), ako aj akýkoľvek SMB alebo WebDAV server.

## Bezpečnosť a súkromie

Na interakciu s prepojenými cloudovými službami používame iba oficiálne SDK a zabezpečené pripojenia. Vaše prihlasovacie meno a heslo nie sú dostupné aplikácii. Všetky požiadavky z aplikácie na cloudovú službu sú šifrované.

Keď zadáte prihlasovacie meno a heslo, aplikácia vám zobrazí oficiálnu autorizačnú stránku poskytnutú poskytovateľom cloudovej služby a celý autorizačný proces prebieha mimo aplikácie. Poskytovateľ cloudovej služby odošle do aplikácie autorizačný token po úspešnej autorizácii a tento token sa používa na volania API.

Autorizačný token je digitálny kľúč, ktorý umožňuje aplikáciám tretích strán interagovať s cloudovým úložiskom. Autorizačný token je uložený na vašom zariadení v bezpečnom systémovom úložisku nazývanom Keychain. Môžete stiahnuť súbory z prepojenej cloudovej služby do zariadenia a tieto súbory budú umiestnené v adresári 'Dokumenty' aplikácie. Tieto súbory môžete kedykoľvek odstrániť pomocou vstavaného správcu súborov.

Aplikácia nezdieľa žiadne informácie z prepojeného cloudového účtu. Prístup k vášmu cloudovému účtu môžete kedykoľvek odvolať otvorením stránky nastavení účtu vo webovom prehliadači.

## Odmietnutie autorizačného tokenu

Prihláste sa do svojho účtu vo webovom prehliadači a prejdite na stránku nastavení. Tam nájdete všetky aplikácie tretích strán, ktoré sú prepojené s vaším cloudovým účtom, a môžete ich odstrániť, ak ich už nechcete používať. Podrobné pokyny sú dostupné [tu](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Môžete tiež odpojiť prepojené cloudové účty v aplikácii a autorizačný token bude tiež odstránený z vášho zariadenia. Ak odstrániete aplikáciu zo zariadenia, všetky stiahnuté dáta a prístupové tokeny budú tiež odstránené.

## Odpojenie cloudového úložiska alebo zmena konfigurácie

- Prístup k možnostiam cloudového úložiska: Najprv vyhľadajte cloudové úložisko, ktoré chcete spravovať v rozhraní aplikácie.
- Klepnite na tlačidlo '...': Vedľa názvu služby uvidíte tlačidlo '...'. Klepnutím naň získate prístup k ďalším možnostiam.
  - **Premenovať**: Ak chcete zmeniť názov cloudovej služby tak, ako sa zobrazuje v zozname, vyberte 'Premenovať.'
  - **Nastavenia**: Ak chcete upraviť konfiguráciu alebo autentifikačné údaje cloudovej služby, zvoľte 'Nastavenia.' Niekedy môže byť potrebné znova autorizovať prepojenú cloudovú službu, ak platnosť autorizačného tokenu vypršala.
  - **Odpojiť**: Ak chcete úplne prerušiť spojenie medzi aplikáciou a cloudovou službou, vyberte 'Odpojiť.' Uvedomte si, že výberom tejto možnosti sa odstránia všetky piesne spojené s touto cloudovou službou z hudobnej knižnice aplikácie, ale zostanú na serveri.

## Pripojenie k počítaču alebo NAS

Môžete tiež pripojiť váš počítač, osobný NAS alebo iné sieťové zariadenia pomocou protokolu SMB, DLNA alebo WebDAV.

## Pripojenie k počítaču pomocou SMB

- Klepnite na "Pripojiť k cloudovému úložisku" → SMB.
- Do poľa URL zadajte IP adresu počítača a názov zdieľaného priečinka vo formáte smb://ip-adresa-počítača/názov-zdieľaného-priečinka
- Vyberte verziu protokolu: Automaticky, SMB1, SMB2
- Zadajte prihlasovacie meno a heslo (ak je potrebné)
- Klepnite na "Hotovo."

Ak je pripojenie úspešné, uvidíte prepojené úložisko v sekcii "Cloudové úložisko."  
Úplný návod na pripojenie Mac alebo PC pomocou SMB je dostupný [tu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Pripojenie k NAS pomocou WebDAV

Všetky kroky sú rovnaké okrem poľa URL.  
URL by mala byť vo formáte http://názov-servera alebo https://názov-servera, ak server podporuje SSL.  
Úplný návod na pripojenie NAS pomocou protokolu WebDAV je dostupný [tu](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Dostupné zariadenia

Táto sekcia zobrazuje všetky zariadenia v lokálnej sieti, ku ktorým sa môžete pripojiť cez aplikáciu.  
Na nadviazanie spojenia so zariadením postupujte podľa týchto krokov:

- Otvorte aplikáciu a prejdite do sekcie "Dostupné zariadenia."
- V zozname klepnite na zariadenie, ku ktorému sa chcete pripojiť.
- V prípade potreby zadajte prihlasovacie údaje na dokončenie pripojenia.

## Wi-Fi Drive

Wi-Fi Drive je pohodlná technológia, ktorá umožňuje bezdrôtový prenos súborov z počítača na zariadenie iOS prostredníctvom desktopového prehliadača.  
Aby ste túto funkciu efektívne využili, uistite sa, že zariadenie aj počítač sú pripojené k rovnakej sieti Wi-Fi.  
Tu je postup krok za krokom, ako používať Wi-Fi Drive.

## Aktivácia Wi-Fi Drive

- Otvorte aplikáciu a prejdite na záložku "Pripojenia."
- Vyberte "Pripojiť cez Wi-Fi" pre prístup na hlavnú obrazovku Wi-Fi Drive.
- Klepnite na "Spustiť Wi-Fi Drive" na aktiváciu Wi-Fi Drive.

## Prístup k Wi-Fi Drive na počítači

- Na počítači (stolnom alebo prenosnom) otvorte webový prehliadač (napríklad Chrome, Firefox alebo Safari).
- Do panela s adresou prehliadača zadajte URL poskytnutú aplikáciou.

## Bezdrôtový prenos súborov

Keď sa webová stránka zodpovedajúca vášmu zariadeniu iOS otvorí v prehliadači, môžete jednoducho pretiahnuť súbory z počítača na webovú stránku.  
Súbory, ktoré presuniete, sa začnú prenášať na zariadenie iOS a budú dostupné v aplikácii.

Podrobné pokyny na bezdrôtový prenos súborov pomocou Wi-Fi Drive sú dostupné [tu](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing je ďalšia technológia, ktorá umožňuje prenos súborov z počítača na zariadenie pomocou aplikácie Finder na vašom Mac a Lightning kábla.  
- Jednoducho pripojte zariadenie k počítaču káblom a spustite aplikáciu Finder na vašom Mac.
- Otvorte "Umiestnenia" → "Vaše pripojené zariadenie" → "Súbory" → a nájdite aktuálnu aplikáciu.
- Klepnite na ikonu aplikácie, aby ste videli všetky zdieľané priečinky.
- Skopírujte súbory z počítača do zdieľaného priečinka na zariadení pomocou funkcie drag-and-drop.

Podrobné pokyny na používanie iTunes File Sharing sú dostupné [tu](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Pripojenie USB flash karty

Ak máte SD kartu alebo USB kľúč, môžete ho pripojiť pomocou čítačky kariet Lightning alebo USB-C na iPhone/iPad, alebo ho pripojiť priamo do Mac. Aplikácia v súčasnosti podporuje certifikované čítačky kariet Apple. Máme podrobné pokyny na pripojenie USB flash karty k iPhone alebo iPad a správu súborov na nej, dostupné [tu](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Pripojené disky sa zobrazujú v sekcii **Externé príslušenstvo** na obrazovke Pripojenia.

## Správca súborov

Po pripojení cloudovej úložnej služby klepnite na jej ikonu, aby ste zobrazili všetky dostupné súbory a priečinky. Môžete použiť vstavaný správca súborov na prácu s týmito súbormi – sťahovanie, premenovanie, presúvanie a ďalšie. Keď spustíte sťahovanie, súbor sa zobrazí vo fronte prenosu. Na zobrazenie frontu prenosu prejdite na záložku "Lokálne súbory" a klepnite na rotujúce šípky v hornom ľavom rohu. Všetky stiahnuté súbory a priečinky sú dostupné v sekcii "Lokálne súbory."

## Horný panel nástrojov

Horný panel nástrojov, pohodlne umiestnený pod navigačnou lištou, ponúka niekoľko užitočných akcií pre jednoduchý prístup. Tento panel môžete zobraziť alebo skryť pomocou jednoduchého gesta potiahnutím nadol. Dostupné akcie sú:

- **Hľadať**: Táto možnosť umožňuje rýchle vyhľadávanie v aktuálnom adresári, čím ľahko nájdete konkrétne súbory alebo priečinky.

## Možnosti priečinka

Keď otvoríte priečinok v aplikácii, nájdete praktickú sadu akcií dostupných klepnutím na tlačidlo "..." v pravom hornom rohu obrazovky.  
Tu je prehľad týchto akcií:

- **Vybrať**: Aktivuje režim výberu súborov. Tento režim vám umožňuje vybrať jeden alebo viac súborov v priečinku, čím ľahko vykonáte akcie na vybraných položkách.
- **Nový priečinok**: Vytvorí nový priečinok v aktuálnom priečinku. Táto funkcia vám umožňuje organizovať súbory a udržiavať knižnicu dobre usporiadanú.
- **Nahrať súbory**: Nahrá súbory zo zariadenia do online priečinka. Táto akcia vám umožňuje preniesť súbory do cloudu alebo na server, čím ich sprístupní odkiaľkoľvek.
- **Hľadať**: Vyhľadáva konkrétne súbory v aktuálnom priečinku. Je to obzvlášť užitočné pri rýchlom vyhľadávaní konkrétnych položiek vo veľkej zbierke.
- **Zoradiť**: Zoradí súbory v priečinku podľa kritérií, ako je názov, veľkosť alebo dátum úpravy. Predvolený režim zoradenia zvyčajne zodpovedá poradiu zoradenia na serveri, ale môžete ho zmeniť podľa svojich preferencií.
- **Zobrazenie mriežky/zoznamu**: Prepínanie medzi dvoma režimami zobrazenia: tabuľkovým zobrazením a zobrazením miniatúr. Tabuľkové zobrazenie predstavuje súbory v zozname, zatiaľ čo zobrazenie miniatúr zobrazuje vizuálne reprezentácie súborov, čo uľahčuje identifikáciu obsahu na pohľad.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zoradenie cloudového priečinka Evertag" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Úprava online súborov

Keď potrebujete spravovať viacero súborov v cloudovom úložisku v tejto aplikácii, môžete použiť režim výberu na zefektívnenie akcií. Postupujte podľa týchto krokov pre efektívnu správu súborov:

- **Aktivácia režimu výberu**: Otvorte aplikáciu na zariadení a prejdite do sekcie obsahujúcej vaše cloudové úložisko. Vyhľadajte tlačidlo "..." (elipsa) v pravom hornom rohu. Klepnite naň a vyberte položku ponuky "Vybrať" na aktiváciu režimu výberu.
- **Výber súborov**: Vedľa každého súboru alebo priečinka sa zobrazia zaškrtávacie políčka. Vyberte jeden alebo viac súborov alebo priečinkov klepnutím na zaškrtávacie políčka vedľa nich.
- **Vykonanie rôznych akcií**: Po výbere súborov alebo priečinkov, ktoré chcete spravovať, budete mať prístup k niekoľkým akciám prispôsobeným vašim potrebám:

{{< cards cols="1">}}
  {{< card title="" subtitle="Výber súboru Evertag" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Akcie súboru

Vedľa názvu súboru uvidíte symbol elipsy "..." (tri bodky) – slúži ako ponuka akcií.  
Klepnutím naň zobrazíte zoznam dostupných akcií:

- **Upraviť audio tagy**: Výberom tejto možnosti môžete pristúpiť k vstavaného editora tagov, ktorý vám umožňuje upravovať audio tagy pre vybraný súbor. Súbor bude dočasne stiahnutý do dočasného adresára a po potvrdení zmien nahraný späť do úložiska.
- **Pridať do obľúbených**: Táto akcia pridá súbor do zoznamu obľúbených súborov pre rýchly a pohodlný prístup.
- **Stiahnuť**: Vyberte túto akciu na stiahnutie súboru alebo priečinka do zariadenia, čím ho sprístupníte na offline použitie.
- **Premenovať**: Táto možnosť vám umožňuje premenovať súbor priamo na vzdialenom úložisku, čo umožňuje prispôsobené pomenovanie súborov.
- **Presunúť**: Zvoľte túto akciu na premiestnenie súboru do iného priečinka v cloudovom úložisku, čo pomáha pri udržiavaní organizovanej štruktúry súborov.
- **Otvoriť v**: Použite túto akciu na export súboru do inej kompatibilnej aplikácie. Súbor bude stiahnutý do zariadenia a potom sa zobrazí dialóg Zdieľanie pre ďalšie zdieľanie alebo interakciu.
- **Vymazať**: S touto akciou buďte opatrní, pretože natrvalo odstráni súbor z cloudového úložiska. **Toto vymazanie nie je možné vrátiť**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Možnosti súboru Evertag" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Ak zoznam akcií presahuje dostupný priestor na obrazovke, jednoducho posuňte ponuku akcií nadol pre prístup k ďalším možnostiam.

## Akcie priečinka

Pre každý priečinok v cloudovom úložisku máte k dispozícii rôzne akcie. Na prístup k týmto možnostiam jednoducho klepnite na ikonu elipsy "..." umiestnenú vedľa názvu priečinka. Ak nevidíte všetky akcie, posuňte sa nadol, aby ste zobrazili ďalšie možnosti. Dostupné akcie sú:

- **Pridať do obľúbených**: Pomocou tejto akcie pridajte priečinok do zoznamu obľúbených súborov pre rýchly a pohodlný prístup.
- **Stiahnuť**: Stiahnite všetok obsah priečinka do zariadenia pre offline prístup.
- **Premenovať**: Premenujte priečinok priamo na vzdialenom úložisku.
- **Presunúť**: Premiestnite priečinok na iné miesto v cloudovom úložisku.
- **Vymazať**: S touto akciou buďte opatrní, pretože natrvalo odstráni priečinok a jeho obsah z cloudového úložiska. **Túto akciu nie je možné vrátiť**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Možnosti priečinka Evertag" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
