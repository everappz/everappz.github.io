---
title: "Připojení"
date: 2020-02-01
description: "Naučte se, jak připojit cloudové služby a zařízení NAS k Flacboxu. Streamujte hudbu ve vysokém rozlišení z iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk a dalších. Použijte SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, sdílení souborů iTunes / Finder a USB flash disky."
keywords: [
  "nastavení cloudu Flacbox", "připojit Google Drive k Flacbox", "streamování hudby SMB",
  "přehrávač WebDAV iOS", "hudební aplikace DLNA", "streamování zvuku NAS", "Wi-Fi Drive iPhone",
  "přenos souborů do iPhone", "Flacbox iTunes File Sharing", "připojit NAS k iPhone",
  "hudební aplikace Synology Drive", "hudební aplikace QNAP", "hudební aplikace Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "hudební aplikace se scrobblingem Last.fm",
  "hudba iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["příručka", "flacbox", "připojení", "cloud", "NAS"]
readingTime: 12
---


Na této obrazovce můžete připojit každý zdroj, kde se nachází vaše hudba. Můžete integrovat oblíbené cloudové služby jako Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive a mnoho dalších, stejně jako váš Mac, PC nebo NAS přes standardní protokoly. Ať už vaše sbírka žije ve streamovací službě jako Dropbox nebo na osobním NAS jako Synology, QNAP, Buffalo, Apple Time Capsule nebo WD My Cloud Home, Flacbox se připojí ke všem z jedné obrazovky.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka Připojení Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Připojit ke Cloudovému Úložišti

- Otevřete kartu **Připojení**.
- Vyberte **Připojit ke cloudovému úložišti** z nabídky.
- Zvolte cloudovou úložnou službu ze seznamu.
- Zadejte přihlašovací údaje na oficiální autorizační stránce poskytnuté poskytovatelem cloudu a klepněte na **Hotovo**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Přidat cloudovou úložnou službu ve Flacboxu" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Pokud narazíte na problémy, zkontrolujte připojení k internetu a přihlašovací jméno / heslo. V Premium verzi aplikace můžete přidat neomezený počet služeb; bezplatná verze podporuje až tři.

## Podporované Cloudové Úložné Služby, Mediální Servery a Protokoly

Flacbox podporuje výjimečně širokou škálu zdrojů vaší hudby. Vše níže funguje z jedné obrazovky **Připojit ke cloudovému úložišti**.

**Osobní cloudové úložiště:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Vlastní servery:** Plex · Jellyfin · Emby · Subsonic (a každý server kompatibilní se Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (a ownCloud přes sdílené API) · Synology Drive · QNAP.

**NAS a protokoly pro sdílení souborů:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, heslo nebo autentizace veřejným klíčem) · NFS · DLNA / UPnP (přehrávání a stahování).

**Objektové úložiště kompatibilní s S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a jakákoli jiná služba, která vystavuje endpoint S3-API.

**Vyhledávání v lokální síti:** Sekce Dostupná zařízení automaticky zobrazuje každou službu Bonjour / mDNS ve vaší síti Wi-Fi, takže se můžete připojit klepnutím bez zadávání IP adresy.

Každé připojení používá **oficiální SDK nebo otevřený protokol** dané služby s autorizací OAuth tam, kde je podporována. Můžete připojit více účtů stejné služby (například dva účty Google Drive, osobní Dropbox vedle pracovního nebo server Plex i Jellyfin) a procházet je vedle sebe na obrazovce Připojení.

## Bezpečnost a Soukromí

Pro interakci s připojenými cloudovými službami používáme pouze oficiální SDK a zabezpečená připojení. Vaše přihlašovací jméno a heslo nejsou pro aplikaci přístupné — všechny přenosy jsou šifrovány TLS.

Když zadáte přihlašovací jméno a heslo, aplikace vám zobrazí oficiální autorizační stránku poskytnutou poskytovatelem cloudové služby a celý proces autorizace probíhá mimo aplikaci. Poskytovatel cloudové služby pak po úspěšné autorizaci odešle do aplikace autorizační token, který se používá k volání API.

Autorizační token je digitální klíč, který umožňuje aplikacím třetích stran interagovat s cloudovým úložištěm vaším jménem. Token je uložen ve vašem zařízení v zabezpečeném systémovém úložišti Apple (Keychain), které je šifrováno v klidu a chráněno heslem vašeho zařízení nebo biometrickým zámkem. Z připojených cloudových služeb si můžete stahovat soubory do zařízení; tyto soubory jsou umístěny v adresáři Documents aplikace a lze je kdykoli odebrat pomocí vestavěného správce souborů.

Aplikace nesdílí žádné informace z vašich připojených cloudových účtů s Everappzem, inzerenty ani žádnou třetí stranou. Přístup ke svému cloudovému účtu můžete kdykoli odvolat otevřením stránky nastavení účtu ve webovém prohlížeči.

## Odmítnutí Autorizačního Tokenu

Chcete-li odvolat autorizační token, přihlaste se ke svému cloudovému účtu ve webovém prohlížeči a přejděte na stránku zabezpečení nebo připojených aplikací. Tam najdete každou aplikaci třetí strany připojenou k vašemu cloudovému účtu a můžete kteroukoli odebrat, pokud ji nechcete dál používat. Podrobné pokyny pro účty Google jsou k dispozici [zde](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Cloudový účet můžete odpojit také přímo v aplikaci — když to uděláte, autorizační token se okamžitě odstraní z vašeho zařízení. Pokud aplikaci z zařízení odinstalujete, veškerá stažená data a přístupové tokeny se s ní automaticky odeberou.

## Odpojit Cloudové Úložiště nebo Změnit Konfiguraci

- **Přístup k možnostem cloudového úložiště** — najděte připojenou službu na obrazovce **Připojení**.
- **Klepněte na tlačítko "..."** vedle názvu služby pro otevření dalších možností:
  - **Přejmenovat** — změňte název cloudové služby, jak se zobrazuje ve vašem seznamu.
  - **Nastavení** — upravte konfiguraci nebo autentizační data. Někdy může být nutné znovu autorizovat připojenou cloudovou službu, pokud vypršela platnost autorizačního tokenu.
  - **Odpojit** — zcela přeruší spojení mezi aplikací a cloudovou službou. Tím se ze záhlaví hudební knihovny aplikace odeberou všechny skladby přidružené k této službě, ale na serveru zůstanou nedotčeny.

## Připojit Počítač nebo NAS

Svůj počítač, osobní NAS nebo jiná síťová zařízení můžete připojit také pomocí protokolů SMB, DLNA nebo WebDAV. Je to nejjednodušší způsob, jak přenést stávající domácí hudební knihovnu — ať už se nachází na Macu, Windows PC, Synology nebo NAS — do Flacboxu bez kopírování čehokoli.

## Připojit Počítač Pomocí SMB

- Klepněte na **Připojit ke cloudovému úložišti → SMB**.
- Zadejte IP adresu počítače a název sdílené složky do pole URL ve formátu `smb://computer-ip-address/shared-folder-name`.
- Zvolte verzi protokolu: **Auto**, **SMB1** nebo **SMB2**.
- Zadejte přihlašovací jméno a heslo (je-li vyžadováno).
- Klepněte na **Hotovo**.

Pokud je připojení úspěšné, připojené úložiště se zobrazí v sekci **Cloudové úložiště**. Kompletní návod na připojení vašeho Macu nebo PC pomocí SMB je k dispozici [zde](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Připojit NAS Pomocí WebDAV

Všechny kroky jsou stejné jako pro SMB, kromě pole URL. URL by měla být ve formátu `http://server-name` nebo `https://server-name`, pokud server podporuje SSL. WebDAV funguje se **Synology, QNAP, Nextcloud, ownCloud** a mnoha dalšími servery — všude, kde je k dispozici endpoint WebDAV.

Kompletní návod na připojení NAS pomocí WebDAV je k dispozici [zde](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Připojit Počítač nebo NAS Pomocí DLNA

Hudební knihovnu umístěnou na vašem Windows PC nebo osobním NAS můžete také sdílet pomocí protokolu DLNA / UPnP a přistupovat k ní v aplikaci, jak je popsáno [zde](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA je oblíbený, široce podporovaný protokol, ale umožňuje pouze přehrávání nebo stahování hudby — na serveru DLNA nemůžete nahrávat soubory ani vytvářet nové složky.

## Připojit NAS nebo Server Pomocí FTP, FTPS nebo SFTP

Flacbox podporuje také klasické protokoly pro přenos souborů. Chcete-li připojit server přes FTP nebo FTPS, klepněte na **Připojit ke cloudovému úložišti → FTP**, zadejte URL hostitele ve formátu `ftp://server-name` (nebo `ftps://server-name` pro šifrované připojení), zadejte přihlašovací jméno a heslo a klepněte na **Hotovo**. Pro **SFTP** (SSH File Transfer Protocol) zvolte **SFTP** a zadejte heslo nebo pár klíčů SSH. Oboje funguje se zařízeními NAS, hostiteli Linux a jakýmkoli serverem, který má démona FTP / FTPS / SSH.

## Připojit Sdílenou Složku NFS

Flacbox obsahuje podporu **NFS** (Network File System) — vhodné pro hostitele Linux, servery BSD a zařízení NAS, která preferují vystavování hudebních knihoven přes NFS místo SMB. Vyberte **NFS** v nabídce **Připojit ke cloudovému úložišti**, zadejte adresu serveru a exportovanou cestu a klepněte na **Hotovo**.

## Připojit Plex Media Server

Flacbox se může přímo připojit k serveru Plex Media Server a procházet vaši hudební knihovnu podle Interpretů, Alb, Žánrů a Seznamů skladeb. Klepněte na **Připojit ke cloudovému úložišti → Plex**, přihlaste se svým účtem Plex, vyberte server a knihovna se zobrazí vedle vašich cloudových služeb. Servery Plex ve stejné lokální síti jsou také automaticky objeveny v sekci **Dostupná zařízení**.

## Připojit Server Jellyfin nebo Emby

Oba servery **Jellyfin** (open-source) i **Emby** (komerční) fungují ve Flacboxu nativně. Klepněte na **Připojit ke cloudovému úložišti → Jellyfin** nebo **Emby**, zadejte URL svého serveru (něco jako `http://server-ip:8096`) a přihlašovací údaje, a vaše hudební knihovna je připravena ke streamování. Stejně jako u Plexu jsou knihovny v lokální síti automaticky uvedeny v části **Dostupná zařízení**.

## Připojit Server Subsonic nebo Navidrome

Flacbox hovoří API Subsonicu, což znamená, že funguje s **Subsonicем** samotným, **Navidrome** a každým dalším serverem kompatibilním se Subsonicem — včetně Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Klepněte na **Připojit ke cloudovému úložišti → Subsonic**, zadejte URL serveru a přihlašovací údaje, a knihovna se zobrazí na obrazovce Připojení. To je nejjednodušší způsob, jak dát Flacboxu přístup k vlastnoručně hostované hudební sbírce bez vystavení sdílené složky souborů.

## Připojit k Objektovému Úložišti Kompatibilnímu s S3

Pro vlastní hostitele a audiofily používající cloudové objektové úložiště obsahuje Flacbox konektor kompatibilní s S3. Klepněte na **Připojit ke cloudovému úložišti → Úložiště S3**, zadejte URL endpointu, oblast, přístupový klíč, tajný klíč a název bucketu. Funguje s AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a jakoukoliv jinou službou, která vystavuje endpoint S3-API.

## Dostupná Zařízení

Tato sekce zobrazuje každé zařízení ve vaší lokální síti, ke kterému se můžete z Flacboxu připojit přes Bonjour discovery. Pro navázání připojení postupujte takto:

- Otevřete aplikaci a přejděte do sekce **Dostupná zařízení** pod Připojení.
- Klepněte na zařízení, ke kterému se chcete připojit.
- V případě potřeby zadejte přihlašovací údaje pro dokončení připojení.

To je nejrychlejší způsob, jak najít sdílení SMB, WebDAV nebo DLNA ve vaší domácí síti bez ručního zadávání IP adres.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dostupná zařízení v lokální síti ve Flacboxu" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive je pohodlná technologie, která umožňuje bezdrátový přenos souborů z počítače na iOS zařízení prostřednictvím jakéhokoli desktopového prohlížeče. Pro efektivní použití této funkce se ujistěte, že vaše zařízení a počítač jsou připojeny ke stejné síti Wi-Fi. Zde je podrobný průvodce, jak používat Wi-Fi Drive.

### Povolit Wi-Fi Drive

- Otevřete aplikaci a přejděte na kartu **Připojení**.
- Vyberte **Připojit přes Wi-Fi** pro přístup na hlavní obrazovku Wi-Fi Drive.
- (Volitelně) Nastavte uživatelské jméno a heslo pro vestavěný webový server, abyste chránili přístup.
- Klepněte na **Spustit Wi-Fi Drive** pro aktivaci Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive ve Flacboxu" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Přistupovat k Wi-Fi Drive na Počítači

- Na svém počítači (stolním nebo přenosném) otevřete webový prohlížeč (jako Chrome, Firefox nebo Safari).
- Do adresního řádku prohlížeče zadejte URL poskytnuté aplikací.

### Bezdrátový Přenos Souborů

Jakmile se webová stránka odpovídající vašemu iOS zařízení otevře v prohlížeči, můžete snadno přetahovat soubory z počítače na webovou stránku. Soubory, které přetáhnete, se začnou přenášet na vaše iOS zařízení a budou přístupné ve Flacboxu.

Také můžete Wi-Fi Drive přímo připojit ve Finderu na macOS (Přejít → Připojit k serveru…) nebo v Průzkumníku souborů ve Windows (Mapovat síťový disk…) a zacházet s iPhone nebo iPad jako s běžnou síťovou jednotkou.

Podrobné pokyny k bezdrátovému přenosu souborů pomocí Wi-Fi Drive jsou k dispozici [zde](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Sdílení Souborů iTunes / Finder

Sdílení souborů iTunes (nyní Sdílení souborů Finder na macOS Catalina a novějších) je další způsob přenosu souborů z počítače na zařízení pomocí kabelu Lightning nebo USB-C.

- Připojte zařízení k počítači kabelem a spusťte **Finder** na Macu (nebo **iTunes** na Windows).
- Otevřete **Umístění → Vaše připojené zařízení → Soubory** a najděte aplikaci Flacbox.
- Klepněte na ikonu aplikace, abyste viděli všechny sdílené složky.
- Přetáhněte soubory z počítače do sdílené složky na zařízení.

Podrobné pokyny k používání Sdílení souborů Finder jsou k dispozici [zde](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Připojit USB Flash Disk

Máte-li SD kartu nebo USB disk, můžete ho připojit pomocí adaptéru Lightning na USB / čtečku SD karet nebo USB-C disku (na iPadu a iPhonu 15 / 16 / 17 / Pro). Aplikace podporuje Apple certifikované čtečky karet a iXpand Flash Drives. S iXpand Flash Drive ho zasuňte do portu Lightning a otevřete aplikaci — uvidíte zprávu o připojení externího zařízení a informace o zařízení. Klepněte na ikonu flash disku pro přístup ke složce s hudbou a klepněte na libovolný zvukový soubor pro zahájení přehrávání.

Máme podrobné pokyny k připojení USB flash disku k iPhonu a poslechu hudby nebo správě souborů na něm umístěných [zde](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Správce Souborů

Jakmile jste připojili cloudovou úložnou službu, klepnutím na její ikonu zobrazíte všechny dostupné soubory a složky. Pomocí vestavěného správce souborů můžete s těmito soubory pracovat — stahovat, přejmenovávat, přesouvat, nahrávat, mazat a další. Když zahájíte stahování, soubor se zobrazí ve frontě přenosů. Frontu přenosů otevřete přechodem na kartu Místní soubory a klepnutím na ikonu rotujících šipek v levém horním rohu. Všechny stažené soubory a složky jsou dostupné v sekci Místní soubory.

## Horní Panel Nástrojů

Horní panel nástrojů, pohodlně umístěný pod navigační lištou, nabízí několik užitečných akcí pro snadný přístup. Zobrazit nebo skrýt jej můžete jednoduše přejetím dolů.

- **Hledat** — proveďte rychlé vyhledávání v aktuálním adresáři, čímž snadno najdete konkrétní soubory nebo složky.
- **Pokračovat v přehrávání** — pokud je povoleno v nastavení aplikace, obnoví frontu přehrávače a poslední pozici médií pro aktuální složku. Praktický způsob, jak pokračovat tam, kde jste skončili.
- **Přehrát vše** — prohledá aktuální složku a její podsložky a přidá všechny nalezené zvukové soubory do nové fronty přehrávače. Užitečné, když chcete přehrát každou stopu v adresáři.
- **Přehrát vše náhodně** — jako Přehrát vše, ale před přidáním do fronty přehrávače soubory zamíchá. Skvělé pro znovuobjevování staré složky s hudbou.

## Možnosti Složky

Když otevřete složku, najdete sadu dostupných akcí klepnutím na tlačítko **"..."** v pravém horním rohu.

- **Vybrat** — aktivuje režim výběru souborů. To vám umožní vybrat jeden nebo více souborů ve složce a provádět akce nad celým výběrem.
- **Nová složka** — vytvoří novou složku v aktuální složce. Skvělé pro udržení dobré struktury vaší knihovny.
- **Povolit offline režim** — zapne offline režim pro aktuální složku. Offline režim jde nad rámec jednoduchého stahování: aktivně monitoruje složku na změny. Pokud online přidáte nové soubory, automaticky se zobrazí na vašem zařízení.
- **Nahrát soubory** — nahraje soubory z vašeho zařízení do online složky. Tím budou přístupné odkudkoli prostřednictvím stejné cloudové služby.
- **Hledat** — hledá konkrétní soubory v aktuální složce.
- **Seřadit** — seřadí soubory podle názvu, velikosti, data změny nebo metadat. Výchozí režim řazení odráží pořadí řazení na serveru, ale můžete jej změnit podle svých preferencí.
- **Mřížka / Seznam** — přepínání mezi zobrazením tabulky a zobrazením miniatur. Tabulkové zobrazení ukazuje kompaktní seznam; zobrazení miniatur ukazuje velké náhledy obalů pro rychlou vizuální identifikaci.

## Úprava Online Souborů

Pokud potřebujete spravovat více souborů ve svém cloudovém úložišti, použijte **Režim výběru** ke zjednodušení akcí:

- **Aktivovat režim výběru** — klepněte na tlačítko **"..."** v pravém horním rohu a zvolte **Vybrat**.
- **Zvolit soubory** — vedle každého souboru a složky se zobrazí zaškrtávací políčka. Klepnutím vyberte jednu nebo více položek.
- **Provádět akce** — jakmile vyberete soubory nebo složky, budete mít přístup k Přehrát jako další, Přehrát později, Přidat do hudební knihovny, Přidat do seznamu skladeb, Kopírovat, Nahrát, Přesunout, Přejmenovat a Smazat.

Pokud dáváte přednost nakládání s připojeným cloudovým úložištěm pouze pro čtení (aby se předešlo náhodným mazáním), aktivujte Nastavení → Správce souborů → Upravit online soubory → Vypnout, abyste ze UI skryli všechny destruktivní operace.

## Akce pro Soubory

Klepnutím na ikonu **"..."** poblíž názvu souboru odhalíte jeho nabídku akcí:

- **Přehrát jako další** — vloží soubor na vrchol fronty přehrávače, takže se přehraje hned po aktuální stopě.
- **Přehrát později** — přidá soubor na konec fronty přehrávače.
- **Přidat do hudební knihovny** — zahrne soubor do vaší hudební knihovny, organizované podle interpreta, alba, žánru nebo skladatele.
- **Přidat do seznamu skladeb** — přidá soubor do existujícího seznamu nebo vytvoří nový.
- **Upravit audio tagy** — otevře vestavěný editor tagů pro úpravu metadat. U online souborů se stopa dočasně stáhne, upraví a poté po potvrzení znovu nahraje.
- **Přidat do oblíbených** — přidá soubor do vašeho seznamu oblíbených pro rychlý přístup.
- **Stáhnout** — stáhne soubor nebo složku do zařízení pro offline použití.
- **Přejmenovat** — přejmenuje soubor přímo na vzdáleném úložišti.
- **Přesunout** — přemístí soubor do jiné složky ve vašem cloudovém úložišti.
- **Otevřít v** — exportuje soubor do jiné kompatibilní aplikace. Soubor se stáhne do vašeho zařízení, poté se zobrazí systémový list sdílení.
- **Smazat** — trvale odstraní soubor z vašeho cloudového úložiště. **Tato akce je nevratná.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Další akce pro soubor v připojeném cloudovém úložišti ve Flacboxu" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Pokud seznam akcí překračuje dostupný prostor na obrazovce, jednoduše posuňte v nabídce akcí dolů pro přístup k dalším možnostem.

## Akce pro Složky

Pro každou složku ve vašem cloudovém úložišti máte k dispozici celou řadu akcí klepnutím na ikonu **"..."** vedle názvu složky. Pokud nevidíte všechny akce, posuňte dolů pro zobrazení dalších.

- **Přehrát vše** — nahradí aktuální frontu přehrávače všemi položkami ve vybrané složce.
- **Přehrát jako další** — přidá celou složku na vrchol fronty přehrávače.
- **Přehrát později** — připojí obsah složky na konec fronty přehrávače.
- **Přidat do hudební knihovny** — zahrne obsah složky do vaší hudební knihovny.
- **Přidat do seznamu skladeb** — přidá celou složku do seznamu. Máte také možnost vytvořit nový seznam; jeho název je automaticky vyplněn z názvu složky.
- **Přidat do oblíbených** — přidá složku do oblíbených pro rychlý přístup.
- **Povolit offline režim** — jde nad rámec jednoduchého stahování, nepřetržitě monitoruje složku pro nové soubory a automaticky je stahuje v okamžiku, kdy se online zobrazí.
- **Stáhnout** — stáhne veškerý obsah složky do zařízení pro offline přístup.
- **Přejmenovat** — přejmenuje složku přímo na vzdáleném úložišti.
- **Přesunout** — přemístí složku na jiné místo ve vašem cloudovém úložišti.
- **Archivovat (ZIP)** — zabalí obsah složky do jednoho souboru ZIP (funkce Premium).
- **Smazat** — trvale odstraní složku a její obsah z cloudového úložiště. **Tato akce je nevratná.**

## Rychlý Přístup

Sekce Rychlý přístup se nachází v horní části obrazovky. Poskytuje rychlý přístup k vašim oblíbeným a naposledy otevřeným souborům z připojených cloudových služeb. Kdykoli otevřete soubor nebo složku z cloudu, přidá se do seznamu Naposledy otevřené. Chcete-li tento seznam vymazat, otevřete Nedávné, klepněte na tlačítko Další akce a zvolte Smazat seznam. Hluboce vnořené složky můžete také označit jako Oblíbené pro rychlý přístup bez procházení struktury adresáře.

{{< cards cols="1">}}
  {{< card title="" subtitle="Online odkazy a rychlý přístup ve Flacboxu" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Ostatní Služby

Tato sekce zobrazuje extra funkce, které vylepšují váš zážitek. Aplikace v současnosti podporuje scrobbling **Last.fm** — po připojení jsou vaše statistiky přehrávání automaticky odesílány na váš účet Last.fm. Poté můžete navštívit svůj profil Last.fm a prohlédnout si analytiku poslechu a získat personalizovaná hudební doporučení. Podrobné pokyny k nastavení jsou k dispozici [zde](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Připojení Last.fm ve Flacboxu" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
