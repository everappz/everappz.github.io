---
title: "Připojení"
date: 2020-01-01
description: "Naučte se připojovat cloudové služby, počítače, NAS zařízení a spravovat hudební soubory pomocí Evermusic. Průvodce krok za krokem pro Wi-Fi Drive, SMB, DLNA, WebDAV, sdílení souborů iTunes a další."
keywords: [
  "Evermusic", "cloudový hudební přehrávač", "NAS streamování", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "sdílení souborů iTunes",
  "připojení cloudového úložiště", "přenos hudby iPhone", "správce souborů iOS"
]
tags: ["evermusic", "guide", "connections"]
readingTime: 11
---


Na obrazovce Připojení můžete připojit každý zdroj, který obsahuje vaši hudbu — oblíbené cloudové služby, samostatně hostované mediální servery, váš Mac nebo PC, osobní NAS, Apple Time Capsule, WD My Cloud Home, dokonce USB flash disk — a používat je všechny z jediného sjednoceného rozhraní. Připojení je také místo, kde nastavujete Rychlý přístup k hluboko vnořeným cloudovým složkám a kde ověřujete Last.fm pro scrobbling.

Obrazovka je rozdělena do přehledně označených sekcí, takže se přizpůsobí jak jednomu účtu iCloud Drive, tak knihovně rozložené přes více cloudů a NAS zařízení: Rychlý přístup nahoře (vaše oblíbené cloudové složky), Cloudové úložiště (přidané účty), Místní síť (zařízení objevená přes Bonjour), Počítač (Wi-Fi Drive, sdílení souborů iTunes, SMB), Externí příslušenství (připojené USB flash disky) a Další služby (Last.fm a podobné).

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka Připojení Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Připojení ke cloudovému úložišti

- Otevřete záložku Připojení.
- Vyberte Připojit cloudové úložiště z nabídky.
- Vyberte cloudovou úložnou službu ze seznamu.
- Přihlaste se na oficiální autorizační stránce poskytovatele (Evermusic nikdy nevidí vaše heslo).
- Klepněte na Hotovo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Výběr poskytovatele cloudového úložiště" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Pokud narazíte na problémy, zkontrolujte připojení k internetu a přihlašovací údaje a ujistěte se, že je pro danou službu správně nakonfigurováno dvoufaktorové ověřování.  
V prémiové verzi aplikace můžete přidat neomezený počet služeb. Bezplatnými uživatelé mohou připojit jeden cloudový účet najednou.

## Podporované cloudové úložné služby

Evermusic podporuje celou řadu populárních cloudových a samostatně hostovaných služeb. Bezplatní uživatelé získají stejný katalog poskytovatelů, ale s omezením na jeden účet; Prémiové odemkne neomezené účty a odstraní většinu ostatních omezení.

- **Osobní cloudové účty:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Samostatně hostované servery a mediální knihovny:** Plex · Jellyfin · Emby · Subsonic (a každý server kompatibilní se Subsonickem — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (a Owncloud, přes sdílené API) · Synology Drive · QNAP.
- **NAS a protokoly pro sdílení souborů:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (ověřování heslem nebo veřejným klíčem), NFS a DLNA (pouze pro čtení — přehrávání a stahování).
- **Objektové úložiště kompatibilní se S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage nebo jakýkoli endpoint S3 API.
- **Objevování v místní síti:** sekce Dostupná zařízení automaticky zobrazuje všechna zařízení ve vaší Wi-Fi, která se inzerují přes Bonjour / mDNS — Plex, Jellyfin, Emby servery, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, routery AirPort s připojenými disky a tak dále.

## Bezpečnost a soukromí

Ke komunikaci s připojenými cloudovými službami používáme pouze oficiální SDK a zabezpečené připojení. Vaše přihlašovací jméno a heslo nejsou dostupné pro aplikaci. Všechny požadavky z aplikace na cloudovou službu jsou šifrované.

Když zadáte přihlašovací jméno a heslo, aplikace vám zobrazí oficiální autorizační stránku poskytnutou poskytovatelem cloudové služby a celý autorizační proces probíhá mimo aplikaci. Poskytovatel cloudové služby odešle do aplikace autentizační token po úspěšné autorizaci a tento token se používá pro volání API.

Autentizační token je digitální klíč, který umožňuje aplikacím třetích stran komunikovat s cloudovým úložištěm. Token je uložen na vašem zařízení v bezpečném systémovém úložišti zvaném Keychain. Můžete stáhnout soubory z připojené cloudové služby do zařízení a tyto soubory budou umístěny v adresáři "Dokumenty" aplikace. Tyto soubory můžete kdykoli odstranit pomocí vestavěného správce souborů.

Aplikace nesdílí žádné informace z připojeného cloudového účtu. Přístup ke svému cloudovému účtu můžete kdykoli odvolat otevřením stránky nastavení účtu ve webovém prohlížeči.

## Odmítnutí autentizačního tokenu

Přihlaste se ke svému účtu ve webovém prohlížeči a přejděte na stránku nastavení. Tam najdete všechny aplikace třetích stran připojené k vašemu cloudovému účtu a můžete kteroukoli z nich odebrat, pokud ji již nechcete používat. Podrobné instrukce jsou dostupné [zde](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Připojené cloudové účty můžete také odpojit v aplikaci a autentizační token bude také odebrán z vašeho zařízení. Pokud odeberete aplikaci ze zařízení, všechna stažená data a přístupové tokeny budou také odebrány.

## Odpojení cloudového úložiště nebo změna konfigurace

- Přístup k možnostem cloudového úložiště: nejprve vyhledejte cloudové úložiště, které chcete spravovat, v rozhraní aplikace.
- Klepněte na tlačítko "...": vedle názvu služby uvidíte tlačítko "...". Klepnutím na něj získáte přístup k dalším možnostem.
  - **Přejmenovat**: pokud chcete změnit název cloudové služby tak, jak se zobrazuje ve vašem seznamu, vyberte "Přejmenovat".
  - **Nastavení**: pro úpravu konfigurace nebo autentizačních dat cloudové služby zvolte "Nastavení". Někdy může být potřeba znovu autorizovat připojenou cloudovou službu, pokud autorizační token vypršel.
  - **Odpojit**: pokud chcete zcela přerušit připojení mezi aplikací a cloudovou službou, vyberte "Odpojit". Pamatujte, že výběr této možnosti odebere všechny skladby spojené s touto cloudovou službou z hudební knihovny aplikace, ale zůstanou na serveru.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nabídka Další akce připojeného cloudového úložiště" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Připojení k počítači nebo NAS

Svůj počítač, osobní NAS nebo jiná síťová zařízení můžete také připojit pomocí protokolu SMB, DLNA nebo WebDAV.

## Připojení k počítači pomocí SMB

- Klepněte na "Připojit cloudové úložiště" → SMB.
- Zadejte IP adresu počítače a název sdílené složky do pole URL ve formátu smb://ip-adresa-pocitace/nazev-sdilene-slozky
- Zvolte verzi protokolu: Auto, SMB1, SMB2
- Zadejte přihlašovací jméno a heslo (pokud je požadováno)
- Klepněte na "Hotovo".

Pokud je připojení úspěšné, uvidíte připojené úložiště v sekci "Cloudové úložiště".  
Kompletní tutoriál o připojení Macu nebo PC pomocí SMB je dostupný [zde](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Nastavení připojení SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Připojení k NAS pomocí WebDAV

Všechny kroky jsou stejné, jen pole URL se liší.  
URL by měla být ve formátu http://nazev-serveru nebo https://nazev-serveru, pokud server podporuje SSL.
Kompletní tutoriál o připojení NAS pomocí protokolu WebDAV je dostupný [zde](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Nastavení připojení WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Připojení k počítači nebo NAS pomocí DLNA

Hudební knihovnu umístěnou na vašem Windows PC nebo osobním NAS můžete také sdílet pomocí protokolu DLNA a přistupovat k ní v aplikaci, jak je popsáno [zde](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA je populární a široce používaný protokol, ale umožňuje pouze přehrávání nebo stahování hudby. Nemůžete nahrávat soubory ani vytvářet nové složky na serveru.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nastavení připojení DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Dostupná zařízení

Tato sekce zobrazuje všechna zařízení ve vaší místní síti, ke kterým se můžete připojit prostřednictvím aplikace.  
Pro navázání připojení se zařízením postupujte takto:

- Otevřete aplikaci a přejděte do sekce "Dostupná zařízení".
- Klepněte na zařízení, ke kterému se chcete připojit, ze seznamu.
- V případě potřeby zadejte přihlašovací údaje pro dokončení připojení.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dostupná zařízení v místní síti" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive je pohodlná technologie, která umožňuje bezdrátový přenos souborů z počítače do iOS zařízení prostřednictvím desktopového prohlížeče.  
Pro efektivní použití této funkce se ujistěte, že vaše zařízení a počítač jsou připojeny ke stejné Wi-Fi síti.  
Zde je průvodce krok za krokem, jak používat Wi-Fi Drive.

## Aktivace Wi-Fi Drive

- Otevřete aplikaci a přejděte na záložku "Připojení".
- Vyberte "Připojit přes Wi-Fi" pro přístup na hlavní obrazovku Wi-Fi Drive.
- Klepněte na "Spustit Wi-Fi Drive" pro aktivaci Wi-Fi Drive.

## Přístup k Wi-Fi Drive na počítači

- Na počítači (desktop nebo notebook) otevřete webový prohlížeč (jako Chrome, Firefox nebo Safari).
- Do adresního řádku prohlížeče zadejte URL poskytnutou aplikací.

## Bezdrátový přenos souborů

Jakmile se v prohlížeči otevře webová stránka odpovídající vašemu iOS zařízení, můžete snadno přetahovat soubory z počítače na webovou stránku.  
Soubory, které přetáhnete, začnou přenášet do vašeho iOS zařízení a budou přístupné v aplikaci.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nastavení serveru Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Podrobné instrukce o bezdrátovém přenosu souborů pomocí WiFi-Drive jsou dostupné [zde](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Sdílení souborů iTunes

Sdílení souborů iTunes je další technologie, která umožňuje přenos souborů z počítače do zařízení pomocí aplikace Finder na Macu a kabelu lightning.  
- Stačí připojit zařízení k počítači kabelem a spustit aplikaci Finder na Macu.
- Otevřete "Umístění" → "Vaše připojené zařízení" → "Soubory" → a najděte aplikaci Evermusic.
- Klepněte na ikonu aplikace pro zobrazení všech sdílených složek.
- Přetáhněte soubory z počítače do sdílené složky na zařízení pomocí přetažení.

Podrobné instrukce o použití sdílení souborů iTunes jsou dostupné [zde](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Sdílení souborů iTunes / Finder na Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Připojení USB flash disku

Pokud máte SD kartu, můžete ji připojit pomocí čtečky karet lightning. Aplikace aktuálně podporuje čtečky karet Apple Certified a iXpand Flash Drives. Pokud máte iXpand Flash Drive — vložte jej do lightning portu a otevřete aplikaci. Uvidíte zprávu "Připojeno externí zařízení" a informace o zařízení. Jednoduše klepněte na ikonu flash disku pro přístup do hudební složky a klepněte na libovolný zvukový soubor pro zahájení přehrávání. Máme podrobné instrukce o připojení USB flash disku k iPhone a poslechu hudby nebo správě souborů na něm, které jsou dostupné [zde](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Správce souborů

Po připojení cloudové úložné služby klepněte na její ikonu pro zobrazení všech dostupných souborů a složek. Vestavěný správce souborů můžete použít pro práci s těmito soubory — stahování, přejmenování, přesun a další. Při zahájení stahování se soubor zobrazí ve frontě přenosů. Pro zobrazení fronty přenosů přejděte na záložku "Lokální soubory" a klepněte na točící se šipky v levém horním rohu. Všechny stažené soubory a složky jsou dostupné v sekci "Lokální soubory".

## Horní panel nástrojů

Horní panel nástrojů, pohodlně umístěný pod navigační lištou, nabízí několik užitečných akcí pro snadný přístup. Tento panel nástrojů můžete zobrazit nebo skrýt jednoduchým gestem přejetí dolů. Zde jsou dostupné akce:

- **Hledat**: Tato možnost umožňuje rychlé hledání v aktuálním adresáři, čímž usnadňuje vyhledání konkrétních souborů nebo složek.
- **Pokračovat v přehrávání**: Pokud je povoleno v nastavení aplikace, tato funkce obnoví frontu přehrávače zvuku a poslední pozici média pro aktuální složku. Je to praktický způsob, jak pokračovat tam, kde jste skončili ve své hudební knihovně.
- **Přehrát vše**: Výběrem této akce aplikace prohledá aktuální složku a její podsložky a přidá všechny nalezené zvukové soubory do nové fronty přehrávače. To je užitečné, když chcete přehrát veškerou hudbu v určitém adresáři.
- **Zamíchat vše**: Podobně jako "Přehrát vše", tato akce prohledá aktuální složku a její podsložky, ale soubory zamíchá před přidáním do fronty přehrávače zvuku. Je to skvělý způsob, jak si vychutnat hudbu v náhodném pořadí pro trochu rozmanitosti.

{{< cards cols="1">}}
  {{< card title="" subtitle="Horní panel nástrojů uvnitř cloudové složky" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Možnosti složky

Když v aplikaci otevřete složku, najdete praktickou sadu akcí dostupnou klepnutím na tlačítko "..." v pravém horním rohu obrazovky.  
Zde je přehled těchto akcí:

- **Vybrat**: Aktivujte režim výběru souborů. Tento režim vám umožňuje vybrat jeden nebo více souborů ve složce, což usnadňuje provádění akcí na vybraných položkách.
- **Nová složka**: Vytvořte novou složku v aktuální složce. Tato funkce umožňuje organizovat soubory a udržovat knihovnu dobře strukturovanou.
- **Aktivovat offline režim**: Zapněte offline režim pro aktuální složku. Offline režim přesahuje pouhé stahování; aktivně sleduje složku pro změny. Pokud přidáte nové soubory do složky online, aplikace je automaticky stáhne do vašeho zařízení. To zajistí, že vaše lokální knihovna zůstane aktuální se změnami na serveru.
- **Nahrát soubory**: Nahrajte soubory ze zařízení do online složky. Tato akce umožňuje přenášet soubory do cloudu nebo na server, čímž jsou dostupné odkudkoli.
- **Hledat**: Hledejte konkrétní soubory v aktuální složce. To je zvláště užitečné pro rychlé vyhledání konkrétních položek ve velké sbírce.
- **Seřadit**: Seřaďte soubory ve složce podle kritérií, jako je název, velikost nebo datum úpravy. Výchozí režim řazení obvykle odpovídá pořadí řazení na serveru, ale můžete ho změnit podle svých preferencí.
- **Mřížka/Seznam**: Přepínejte mezi dvěma režimy zobrazení: tabulkovým zobrazením a zobrazením náhledů. Tabulkové zobrazení zobrazuje soubory jako seznam, zatímco zobrazení náhledů ukazuje vizuální reprezentace souborů, což usnadňuje identifikaci obsahu na první pohled.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nabídka Další akce aktuální složky" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Úprava online souborů

Když potřebujete spravovat více souborů v cloudovém úložišti v Evermusic, můžete použít režim výběru pro zefektivnění akcí. Pro efektivní správu souborů postupujte takto:

- **Aktivujte režim výběru**: Otevřete aplikaci na zařízení a přejděte do sekce obsahující cloudové úložiště. Podívejte se do pravého horního rohu, kde najdete tlačítko "..." (tři tečky). Klepněte na něj a zvolte položku nabídky "Vybrat" pro aktivaci režimu výběru.
- **Vyberte soubory**: Uvidíte zaškrtávací políčka vedle každého souboru nebo složky v seznamu. Vyberte jeden nebo více souborů nebo složek jednoduše klepnutím na zaškrtávací políčka vedle nich.
- **Proveďte různé akce**: Po výběru souborů nebo složek, které chcete spravovat, budete mít přístup k několika akcím přizpůsobeným vašim potřebám:

{{< cards cols="1">}}
  {{< card title="" subtitle="Režim výběru pro online soubory" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Akce souborů

Vedle názvu souboru uvidíte symbol tří teček "..." — toto slouží jako nabídka akcí.  
Klepnutím na ni zobrazíte seznam dostupných akcí:

- **Přehrát jako další**: Zvolte tuto akci pro vložení vybraného souboru na začátek fronty přehrávače, čímž zajistíte, že se přehraje ihned po aktuálně přehrávané položce.
- **Přehrát později**: Výběrem této možnosti se soubor přidá na konec fronty přehrávače, čímž zajistíte, že se přehraje po existující frontě.
- **Přidat do hudební knihovny**: Tato akce umožňuje začlenit soubor do hudební knihovny, čímž je snadno dostupný a přehledně organizovaný podle interpreta, alba, žánru nebo skladatele.
- **Přidat do playlistu**: Touto akcí přidejte soubor do existujícího playlistu nebo vytvořte nový.
- **Upravit audio tagy**: Výběrem této možnosti získáte přístup k vestavěnému editoru tagů Evermusic, který umožňuje upravovat zvukové tagy pro vybraný soubor. Soubor bude dočasně stažen do dočasného adresáře a poté nahrán do úložiště po potvrzení změn.
- **Přidat do oblíbených**: Tato akce přidá soubor do seznamu oblíbených souborů pro rychlý a pohodlný přístup.
- **Stáhnout**: Zvolte tuto akci pro stažení souboru nebo složky do zařízení, čímž je zpřístupníte pro offline použití.
- **Přejmenovat**: Tato možnost umožňuje přejmenovat soubor přímo ve vzdáleném úložišti, což umožňuje přizpůsobené pojmenování souborů.
- **Přesunout**: Zvolte tuto akci pro přesunutí souboru do jiné složky v cloudovém úložišti, čímž pomáháte udržovat organizovanou strukturu souborů.
- **Otevřít v**: Touto akcí exportujte soubor do jiné kompatibilní aplikace. Soubor se stáhne do zařízení a poté se zobrazí dialogové okno Sdílet pro další sdílení nebo interakci.
- **Smazat**: S touto akcí buďte opatrní, protože trvale odebere soubor z cloudového úložiště. Toto smazání nelze vrátit zpět.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nabídka Další akce pro jeden soubor" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Pokud seznam akcí přesahuje dostupný prostor na obrazovce, jednoduše se posuňte dolů v nabídce akcí pro přístup k dalším možnostem.

## Akce složek

Pro každou složku v cloudovém úložišti máte k dispozici různé akce. Pro přístup k těmto možnostem jednoduše klepněte na ikonu tří teček "..." umístěnou vedle názvu složky. Pokud nevidíte všechny akce, posuňte se dolů pro zobrazení dalších možností. Zde jsou dostupné akce:

- **Přehrát vše**: Nahraďte aktuální frontu přehrávače všemi položkami z vybrané složky.
- **Přehrát jako další**: Přidejte celou složku na začátek fronty přehrávače, hned za aktuálně přehrávanou položku.
- **Přehrát později**: Přidejte obsah složky na konec fronty přehrávače.
- **Přidat do hudební knihovny**: Tato akce bezproblémově začlení obsah složky do hudební knihovny, čímž je snadno dostupný a přehledně organizovaný podle interpreta, alba, žánru nebo skladatele.
- **Přidat do playlistu**: Celou složku můžete zahrnout do playlistu. Máte také možnost vytvořit nový playlist a název složky bude automaticky přiřazen.
- **Přidat do oblíbených**: Touto akcí přidejte složku do seznamu oblíbených souborů pro rychlý a pohodlný přístup.
- **Aktivovat offline režim**: Aktivací offline režimu pro vybranou složku aplikace přesahuje pouhé stahování. Průběžně skenuje pro změny a pokud jsou do online složky přidány nové soubory, budou automaticky staženy do aplikace.
- **Stáhnout**: Stáhněte veškerý obsah složky do zařízení pro offline přístup.
- **Přejmenovat**: Přejmenujte složku přímo ve vzdáleném úložišti.
- **Přesunout**: Přesuňte složku na jiné místo v cloudovém úložišti.
- **Smazat**: S touto akcí buďte opatrní, protože trvale odebere složku a její obsah z cloudového úložiště. Tuto akci nelze vrátit zpět.

## Rychlý přístup

Sekce Rychlý přístup se nachází v horní části obrazovky. Poskytuje rychlý přístup k oblíbeným a nedávno otevřeným souborům z připojených cloudových služeb.
Kdykoli otevřete soubor nebo složku z cloudu, přidá se do seznamu "Naposledy otevřené". Pro vymazání tohoto seznamu otevřete "Nedávné", klepněte na tlačítko "Další akce" a zvolte "Smazat seznam". Můžete také označit hluboko vnořené složky jako Oblíbené pro rychlý přístup bez procházení adresářové struktury.

## Další služby

Tato sekce zobrazuje extra funkce, které vylepšují váš zážitek. Aplikace aktuálně podporuje scrobbling Last.fm. Po připojení jsou statistiky přehrávání automaticky odesílány na váš účet Last.fm. Svůj profil Last.fm můžete navštívit později pro zobrazení statistik poslechu a získání personalizovaných hudebních doporučení. Podrobné instrukce nastavení jsou dostupné [zde](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
