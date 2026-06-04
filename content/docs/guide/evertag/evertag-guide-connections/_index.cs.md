---
title: "Připojení"
date: 2020-02-01
description: "Naučte se připojit cloudové úložiště, NAS a počítač k Evertag. Přistupujte a upravujte audio soubory přímo z cloudového úložiště, osobního NAS nebo Mac/PC."
keywords: [
  "nastavení cloudu Evertag", "připojit iCloud k Evertag", "přístup k souborům SMB iOS",
  "editor audio tagů WebDAV", "úprava metadat NAS", "Wi-Fi Drive Evertag",
  "přenos audio souborů do iPhone", "iTunes File Sharing Evertag", "úprava FLAC tagů z cloudu"
]
tags: ["průvodce", "evertag", "připojení"]
readingTime: 11
---


Na této obrazovce můžete připojit různé zdroje obsahující vaše audio soubory. Můžete integrovat oblíbené cloudové služby jako Google Drive, Dropbox, OneDrive, iCloud a další, stejně jako připojit váš Mac nebo PC. Navíc máte možnost upravovat audio soubory umístěné v Apple Time Capsule, WD Cloud Home nebo jakémkoli NAS, který podporuje SMB nebo WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka Připojení Evertag" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Rychlý přístup

V horní části obrazovky Připojení najdete seznam **Rychlý přístup**. Jakákoli cloudová složka, kterou přidáte do oblíbených — i ta zahrabaná několik úrovní hluboko — se zde zobrazí, takže k ní můžete přejít bez procházení nadřazených složek pokaždé.

## Připojení ke cloudovému úložišti

- Otevřete záložku 'Připojení'  
- Vyberte 'Připojit ke cloudovému úložišti' z nabídky  
- Zvolte službu cloudového úložiště ze seznamu  
- Zadejte přihlašovací údaje a klepněte na 'Hotovo'.

Pokud narazíte na jakékoli problémy, zkontrolujte své internetové připojení a přihlašovací jméno/heslo.  
V Premium verzi aplikace můžete přidat neomezený počet služeb.

## Podporované cloudové úložiště

Aplikace aktuálně podporuje nejoblíbenější cloudové úložiště: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), stejně jako jakýkoli server SMB nebo WebDAV.

## Bezpečnost a soukromí

Pro interakci s připojenými cloudovými službami používáme pouze oficiální SDK a zabezpečená připojení. Vaše přihlašovací jméno a heslo nejsou pro aplikaci přístupné. Všechny požadavky z aplikace na cloudovou službu jsou šifrované.

Když zadáte přihlašovací jméno a heslo, aplikace vám zobrazí oficiální autorizační stránku poskytnutou poskytovatelem cloudové služby a celý autorizační proces probíhá mimo aplikaci. Poskytovatel cloudové služby po úspěšné autorizaci pošle aplikaci autentizační token, který se používá k volání API.

Autentizační token je digitální klíč, který umožňuje aplikacím třetích stran interagovat s cloudovým úložištěm. Autentizační token je uložen na vašem zařízení v zabezpečeném systémovém úložišti zvaném Keychain. Soubory z připojené cloudové služby si můžete stáhnout do zařízení a tyto soubory budou umístěny do adresáře "Dokumenty" aplikace. Tyto soubory můžete kdykoli odstranit pomocí vestavěného správce souborů.

Aplikace nesdílí žádné informace z připojeného cloudového účtu. Přístup ke svému cloudovému účtu můžete kdykoli odvolat otevřením stránky nastavení účtu ve webovém prohlížeči.

## Odvolání autentizačního tokenu

Přihlaste se ke svému účtu ve webovém prohlížeči a přejděte na stránku nastavení. Tam najdete všechny aplikace třetích stran připojené k vašemu cloudovému účtu a odstraňte kteroukoli z nich, pokud ji již nechcete používat. Podrobné pokyny jsou k dispozici [zde](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Připojené cloudové účty můžete také odpojit v aplikaci a autentizační token bude ze zařízení také odstraněn. Pokud aplikaci ze zařízení odeberete, budou odstraněna i všechna stažená data a přístupové tokeny.

## Odpojení cloudového úložiště nebo změna konfigurace

- Přístup k možnostem cloudového úložiště: nejprve v rozhraní aplikace vyhledejte cloudové úložiště, které chcete spravovat.  
- Klepněte na tlačítko '...': vedle názvu služby uvidíte tlačítko '...'. Klepnutím na něj zobrazíte další možnosti.  
  - **Přejmenovat**: pokud chcete změnit název cloudové služby tak, jak se zobrazuje v seznamu, vyberte 'Přejmenovat'.  
  - **Nastavení**: pro úpravu konfigurace nebo autentizačních dat cloudové služby zvolte 'Nastavení'. Někdy může být nutné znovu autorizovat připojenou cloudovou službu, pokud platnost autorizačního tokenu vypršela.  
  - **Odpojit**: pokud chcete zcela přerušit spojení mezi aplikací a cloudovou službou, vyberte 'Odpojit'. Mějte na vědomí, že výběrem této možnosti odstraníte z hudební knihovny aplikace všechny písně spojené s touto cloudovou službou, ale na serveru zůstanou.

## Připojení k počítači nebo NAS

Svůj počítač, osobní NAS nebo jiná síťová zařízení můžete také připojit pomocí protokolu SMB, DLNA nebo WebDAV.

## Připojení k počítači pomocí SMB

- Klepněte na "Připojit ke cloudovému úložišti" → SMB.  
- Do pole URL zadejte IP adresu počítače a název sdílené složky ve formátu smb://computer-ip-address/shared-folder-name  
- Zvolte verzi protokolu: Auto, SMB1, SMB2  
- Zadejte přihlašovací jméno a heslo (pokud je vyžadováno)  
- Klepněte na "Hotovo".

Pokud je připojení úspěšné, zobrazí se připojené úložiště v sekci "Cloudové úložiště".  
Úplný tutoriál o připojení Mac nebo PC pomocí SMB je k dispozici [zde](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Připojení k NAS pomocí WebDAV

Všechny kroky jsou stejné s výjimkou pole URL.  
URL by mělo být ve formátu http://server-name nebo https://server-name, pokud server podporuje SSL.  
Úplný tutoriál o připojení NAS pomocí protokolu WebDAV je k dispozici [zde](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Dostupná zařízení

Tato sekce zobrazuje všechna zařízení ve vaší místní síti, ke kterým se můžete připojit prostřednictvím aplikace.  
Pro navázání spojení se zařízením postupujte takto:

- Otevřete aplikaci a přejděte do sekce "Dostupná zařízení".  
- Ze seznamu klepněte na zařízení, ke kterému se chcete připojit.  
- V případě potřeby zadejte přihlašovací údaje pro dokončení připojení.

## Wi-Fi Drive

Wi-Fi Drive je pohodlná technologie, která umožňuje bezdrátový přenos souborů z počítače do vašeho iOS zařízení prostřednictvím prohlížeče na ploše.  
Pro efektivní používání této funkce se ujistěte, že vaše zařízení a počítač jsou připojeny ke stejné Wi-Fi síti.  
Zde je podrobný průvodce, jak používat Wi-Fi Drive.

## Aktivace Wi-Fi Drive

- Otevřete aplikaci a přejděte na záložku "Připojení".  
- Vyberte "Připojit přes Wi-Fi" pro přístup na hlavní obrazovku Wi-Fi Drive.  
- Klepněte na "Spustit Wi-Fi Drive" pro aktivaci Wi-Fi Drive.

## Přístup k Wi-Fi Drive z počítače

- Na počítači (stolním nebo přenosném) otevřete webový prohlížeč (například Chrome, Firefox nebo Safari).  
- Do adresního řádku prohlížeče zadejte URL poskytnutou aplikací.

## Bezdrátový přenos souborů

Jakmile se webová stránka odpovídající vašemu iOS zařízení otevře v prohlížeči, můžete snadno přetahovat soubory z počítače na webovou stránku.  
Soubory, které přetáhnete, se začnou přenášet do vašeho iOS zařízení a budou přístupné v aplikaci.

Podrobné pokyny o bezdrátovém přenosu souborů pomocí Wi-Fi Drive jsou k dispozici [zde](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing je další technologie, která vám umožňuje přenášet soubory z počítače do zařízení pomocí aplikace Finder na Macu a kabelu Lightning.  
- Stačí připojit zařízení k počítači kabelem a spustit aplikaci Finder na Macu.  
- Otevřete "Umístění" → "Vaše připojené zařízení" → "Soubory" → a vyhledejte aktuální aplikaci.  
- Klepnutím na ikonu aplikace zobrazíte všechny sdílené složky.  
- Přetáhněte soubory z počítače do sdílené složky v zařízení.

Podrobné pokyny o používání iTunes File Sharing jsou k dispozici [zde](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Připojení USB karty

Pokud máte SD kartu nebo USB disk, můžete ji připojit pomocí čtečky Lightning nebo USB-C na iPhone/iPad nebo ji zapojit přímo do Macu. Aplikace aktuálně podporuje čtečky karet s certifikací Apple. Máme podrobné pokyny o připojení USB karty k iPhone nebo iPad a správě souborů na ní, k dispozici [zde](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Připojené disky se zobrazují v sekci **Připojené příslušenství** na obrazovce Připojení.

## Správce souborů

Jakmile připojíte cloudovou úložnou službu, klepnutím na její ikonu zobrazíte všechny dostupné soubory a složky. Pomocí vestavěného správce souborů můžete s těmito soubory pracovat — stahovat, přejmenovávat, přesouvat a další. Když zahájíte stahování, soubor se zobrazí ve frontě přenosu. Pro zobrazení fronty přenosu přejděte na záložku "Místní soubory" a klepněte na rotující šipky v levém horním rohu. Všechny stažené soubory a složky jsou dostupné v sekci "Místní soubory".

## Horní panel nástrojů

Horní panel nástrojů, pohodlně umístěný pod navigační lištou, nabízí několik užitečných akcí pro snadný přístup. Tento panel nástrojů můžete zobrazit nebo skrýt jednoduchým gestem přejetí dolů. Zde jsou dostupné akce:

- **Hledat**: tato možnost vám umožňuje provést rychlé vyhledávání v aktuálním adresáři, čímž usnadňuje vyhledání konkrétních souborů nebo složek.  

## Možnosti složky

Když v aplikaci otevřete složku, najdete praktickou sadu akcí dostupných klepnutím na tlačítko "..." v pravém horním rohu obrazovky.  
Zde je přehled těchto akcí:

- **Vybrat**: aktivuje režim výběru souborů. Tento režim umožňuje vybrat jeden nebo více souborů ve složce, čímž usnadňuje provádění akcí na vybraných položkách.  
- **Nová složka**: vytvoří novou složku v aktuální složce. Tato funkce vám umožňuje organizovat soubory a udržovat dobře strukturovanou knihovnu.   
- **Nahrát soubory**: nahrajte soubory ze zařízení do online složky. Tato akce vám umožňuje přenést soubory do cloudu nebo na server, čímž je zpřístupníte odkudkoli.  
- **Hledat**: hledejte konkrétní soubory v aktuální složce. Zvláště užitečné pro rychlé vyhledání konkrétních položek ve velké sbírce.  
- **Seřadit**: seřaďte soubory ve složce podle kritérií jako název, velikost nebo datum úpravy. Výchozí režim řazení obvykle odráží pořadí řazení na serveru, ale můžete jej změnit podle svých preferencí.  
- **Mřížka/Seznam**: přepínání mezi dvěma režimy zobrazení: tabulkovým zobrazením a zobrazením miniatur. Tabulkové zobrazení zobrazuje soubory v seznamu, zatímco zobrazení miniatur zobrazuje vizuální reprezentace souborů, čímž usnadňuje identifikaci obsahu na první pohled.

{{< cards cols="1">}}
  {{< card title="" subtitle="Řazení cloudové složky Evertag" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Úprava online souborů

Když potřebujete spravovat více souborů v cloudovém úložišti v této aplikaci, můžete použít režim výběru ke zjednodušení akcí. Postupujte takto pro efektivní správu souborů:

- **Aktivace režimu výběru**: otevřete aplikaci na zařízení a přejděte do sekce obsahující vaše cloudové úložiště. Vyhledejte pravý horní roh, kde najdete tlačítko "..." (tři tečky). Klepněte na něj a zvolte položku nabídky "Vybrat" pro aktivaci režimu výběru.  
- **Výběr souborů**: uvidíte zaškrtávací políčka vedle každého souboru nebo složky. Vyberte jeden nebo více souborů či složek jednoduchým klepnutím na zaškrtávací políčka vedle nich.  
- **Provádění různých akcí**: jakmile vyberete soubory nebo složky, které chcete spravovat, budete mít přístup k několika akcím přizpůsobeným vašim potřebám:

{{< cards cols="1">}}
  {{< card title="" subtitle="Výběr souboru Evertag" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Akce se souborem

U názvu souboru si všimnete symbolu tři tečky "..." – slouží jako nabídka akcí.  
Klepnutím na něj zobrazíte seznam dostupných akcí:

- **Upravit audio tagy**: výběrem této možnosti získáte přístup k vestavěnému editoru tagů, který vám umožňuje upravovat audio tagy vybraného souboru. Soubor bude dočasně stažen do dočasného adresáře a poté nahrán do úložiště po potvrzení změn.  
- **Přidat do oblíbených**: tato akce přidá soubor do vašeho seznamu oblíbených souborů pro rychlý a pohodlný přístup.  
- **Stáhnout**: tuto akci zvolte pro stažení souboru nebo složky do zařízení, aby byl dostupný pro offline použití.  
- **Přejmenovat**: tato možnost vám umožňuje přejmenovat soubor přímo na vzdáleném úložišti, což umožňuje vlastní pojmenování souborů.  
- **Přesunout**: zvolte tuto akci pro přesunutí souboru do jiné složky v cloudovém úložišti, čímž pomáháte udržovat organizovanou strukturu souborů.  
- **Otevřít v**: použijte tuto akci pro export souboru do jiné kompatibilní aplikace. Soubor bude stažen do vašeho zařízení a poté se zobrazí dialogové okno sdílení pro další sdílení nebo interakci.  
- **Smazat**: s touto akcí buďte opatrní, protože trvale odstraní soubor z cloudového úložiště. **Toto smazání nelze vrátit zpět**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Možnosti souboru Evertag" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Pokud seznam akcí přesáhne dostupný prostor na obrazovce, jednoduše se posuňte dolů v nabídce akcí pro přístup k dalším možnostem.

## Akce se složkou

Pro každou složku v cloudovém úložišti jsou k dispozici různé akce. Pro přístup k těmto možnostem jednoduše klepněte na ikonu tří teček "..." umístěnou vedle názvu složky. Pokud nevidíte všechny akce, posuňte se dolů pro zobrazení dalších možností. Zde jsou dostupné akce:

- **Přidat do oblíbených**: tuto akci použijte pro přidání složky do vašeho seznamu oblíbených souborů pro rychlý a pohodlný přístup.  
- **Stáhnout**: stáhněte veškerý obsah složky do zařízení pro offline přístup.  
- **Přejmenovat**: přejmenujte složku přímo na vzdáleném úložišti.  
- **Přesunout**: přesuňte složku na jiné místo v cloudovém úložišti.  
- **Smazat**: s touto akcí buďte opatrní, protože trvale odstraní složku a její obsah z cloudového úložiště. **Tuto akci nelze vrátit zpět**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Možnosti složky Evertag" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
