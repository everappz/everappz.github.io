---
title: "Soubory"
date: 2020-02-01
lastmod: 2026-06-01
description: "Naučte se používat záložku Soubory v Evervideo na iPhone, iPad a Mac. Připojte cloudové služby, NAS zařízení, mediální servery a RTSP streamy na jednom místě. Spravujte offline videa, frontu přenosů, stahování, Wi-Fi Drive, sdílení souborů iTunes/Finder a USB disky. Zahrnuje iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP/SFTP, DLNA a úložiště kompatibilní s S3."
keywords: [
  "soubory Evervideo", "připojení Evervideo", "místní soubory Evervideo",
  "nastavení cloudového videa iPhone", "připojit Google Drive video", "streamování videa SMB",
  "přehrávač videa WebDAV iOS", "DLNA video iPhone", "streamování videa NAS",
  "přenos videa Wi-Fi Drive", "sdílení souborů iTunes Evervideo", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "offline režim videa Evervideo", "fronta přenosů Evervideo",
  "správce souborů Evervideo", "složka Dokumenty Evervideo",
  "přehrávač videa Synology", "přehrávač videa QNAP",
  "přehrávač videa Apple Time Capsule", "USB DAC video",
  "přehrávač videa iXpand", "přehrávač videa S3"
]
tags: ["průvodce", "evervideo", "soubory", "připojení", "cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Záložka Soubory je komplexní správce souborů Evervideo. Na rozdíl od většiny video aplikací, které oddělují cloudové úložiště od místních souborů do různých záložek, Evervideo sloučí oboje do jediné rolovatelné obrazovky, takže se můžete přesunout ze serveru Plex do cloudové složky do složky Dokumenty na iPhone, aniž byste přepínali mezi záložkami.

Záložka Soubory je rozdělena do přehledných sekcí, které se zobrazují v tomto pořadí na obrazovce:

- **Rychlý přístup** — nedávné a oblíbené pro soubory a složky, které jste otevřeli naposledy.
- **Soubory v této aplikaci** — co je v sandboxované složce Dokumenty aplikace Evervideo.
- **Soubory v tomto iPhone/iPad/Mac** — videa jinde v zařízení, přístupná přes systémový výběr souborů.
- **Cloudové úložiště** — každý cloudový účet, NAS a mediální server, který máte připojen.
- **Dostupná zařízení** — servery a disky automaticky objevené přes Bonjour/mDNS ve vaší místní síti.

V pravém horním rohu obrazovky Soubory je tlačítko Přenosy (ikona točících se šipek). Klepněte na něj a otevřete frontu přenosů, kde sledujete každé stahování a nahrávání ze všech zdrojů.

{{< cards cols="1">}}
  {{< card title="" subtitle="Soubory Evervideo přes připojená úložiště" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Připojení k cloudovému úložišti

Sekce Cloudové úložiště záložky Soubory je místo, kde žije každý připojený účet, NAS, mediální server a stream — vedle sebe, v jednom rolovatelném seznamu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sekce Cloudové úložiště v záložce Soubory Evervideo" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Otevřete záložku **Soubory**.
- Přejděte na sekci **Cloudové úložiště**.
- Klepněte na **Připojit k cloudovému úložišti** z nabídky.
- Vyberte cloudovou službu ze seznamu.
- Zadejte přihlašovací údaje na oficiální autorizační stránce poskytovatele cloudu a klepněte na **Hotovo**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Připojení cloudové služby v Evervideo" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Pokud narazíte na problémy, zkontrolujte připojení k internetu a přihlašovací údaje. V prémiové verzi aplikace můžete přidat neomezený počet služeb; bezplatná verze podporuje až tři.

## Podporované cloudové služby, mediální servery a protokoly

Evervideo podporuje výjimečně širokou škálu zdrojů pro vaše videa. Vše níže funguje z jediného toku připojení k cloudovému úložišti.

**Osobní cloudové úložiště:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Lokálně hostované mediální servery:** Plex · Jellyfin · Emby · Subsonic (a každý server kompatibilní se Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (a ownCloud přes sdílené API) · Synology Drive · QNAP.

**Protokoly NAS a sdílení souborů:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP/HTTPS) · FTP · FTPS · SFTP (protokol přenosu souborů SSH, heslo nebo autentizace veřejným klíčem) · NFS · DLNA/UPnP (přehrávání a stahování).

**Živé streamy a IP kamery:** RTSP — nasměrujte Evervideo na jakoukoliv URL `rtsp://` a prostě přehraje. Ideální pro bezpečnostní kamery, kamerové zvonky, poskytovatele IPTV, monitory pro miminko a podobné živé zdroje.

**Objektové úložiště kompatibilní s S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a jakýkoli jiný endpoint S3 API.

**Místní knihovny:** knihovna Fotek (všechna videa, záznamy obrazovky, fotoalba) a knihovna aplikace Hudba (Alba, Žánry, Seznamy skladeb) — oboje se zobrazuje v knihovně médií, takže nemusíte nic kopírovat.

**Místní síťové objevování:** sekce Dostupná zařízení automaticky zobrazí každou Bonjour/mDNS službu na vaší Wi-Fi síti — servery Plex, Jellyfin, Emby, Synology, QNAP, routery AirPort s připojenými disky, Apple Time Capsule — takže stačí klepnout pro připojení bez zadávání IP adresy.

Každé připojení používá oficiální SDK nebo otevřený protokol služby s autorizací na základě OAuth tam, kde je podporována. Můžete připojit více účtů stejné služby (například dva účty Google Drive nebo server Plex i Jellyfin) a procházet je vedle sebe v sekci Cloudové úložiště.

## Zabezpečení a soukromí

Evervideo používá pouze oficiální SDK a zabezpečená připojení pro interakci s připojenými cloudovými službami. Vaše přihlašovací jméno a heslo nejsou přístupné aplikaci — všechny přenosy jsou šifrovány TLS.

Když zadáte přihlašovací jméno a heslo, aplikace vám zobrazí oficiální autorizační stránku poskytovatele cloudové služby a celý autorizační proces probíhá mimo aplikaci. Poskytovatel cloudové služby pak odešle auth-token do aplikace po úspěšné autorizaci a tento token se používá pro volání API.

Auth-token je digitální klíč, který umožňuje aplikacím třetích stran interagovat s cloudovým úložištěm vaším jménem. Token je uložen ve vašem zařízení v zabezpečeném systémovém úložišti Apple (Keychain), které je šifrováno v klidném stavu a chráněno přístupovým kódem zařízení nebo biometrickým zámkem. Soubory z připojených cloudových služeb můžete stahovat do zařízení; tyto soubory jsou umístěny v adresáři Dokumenty aplikace a lze je kdykoli odebrat pomocí vestavěného správce souborů.

Aplikace nesdílí žádné informace z připojených cloudových účtů s Everappz, inzerenty ani třetími stranami. Přístup ke cloudovému účtu můžete kdykoli odvolat otevřením stránky nastavení účtu ve webovém prohlížeči.

## Odmítnutí auth-tokenu

Pro odvolání auth-tokenu se přihlaste ke cloudovému účtu ve webovém prohlížeči a přejděte na stránku zabezpečení nebo připojených aplikací. Tam najdete každou aplikaci třetí strany připojenou k vašemu cloudovému účtu a libovolnou odeberete, pokud ji již nechcete používat. Podrobné pokyny pro účty Google jsou dostupné [zde](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Cloudový účet můžete také odpojit přímo v aplikaci — při tom se auth-token okamžitě odstraní ze zařízení. Pokud aplikaci odinstalujete ze zařízení, všechna stažená data a přístupové tokeny se automaticky odeberou.

## Odpojení cloudového úložiště nebo změna konfigurace

- **Přístup k možnostem cloudového úložiště** — najděte připojenou službu v sekci **Cloudové úložiště** záložky Soubory.
- **Klepněte na tlačítko "..."** vedle názvu služby pro otevření dalších možností:
  - **Přejmenovat** — změňte název cloudové služby tak, jak se zobrazuje v seznamu.
  - **Nastavení** — upravte konfiguraci nebo autentizační data. Někdy může být nutné znovu autorizovat připojenou cloudovou službu, pokud autorizační token vypršel.
  - **Odpojit** — zcela přerušte spojení mezi aplikací a cloudovou službou. Tím se odstraní všechna videa přidružená k této službě z knihovny médií, ale ponechají se nedotčená na serveru.

## Připojení k počítači nebo NAS

Počítač, osobní NAS nebo jiné síťové zařízení lze připojit pomocí protokolu SMB, WebDAV, FTP/FTPS, SFTP, NFS nebo DLNA. Toto je nejjednodušší způsob, jak přenést existující domácí mediální knihovnu — ať už žije na Macu, Windows PC, Synology, QNAP, Apple Time Capsule nebo WD My Cloud Home — do Evervideo bez kopírování čehokoli.

### Připojení k počítači pomocí SMB

- Klepněte na **Připojit k cloudovému úložišti → SMB**.
- Zadejte IP adresu počítače a název sdílené složky ve formátu `smb://computer-ip-address/shared-folder-name`.
- Vyberte verzi protokolu: **Auto**, **SMB1** nebo **SMB2**.
- Zadejte přihlašovací jméno a heslo (je-li požadováno).
- Klepněte na **Hotovo**.

Pokud je připojení úspěšné, sdílená složka se zobrazí v sekci Cloudové úložiště. Kompletní tutoriál o připojení Macu nebo PC pomocí SMB je dostupný [zde](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Připojení k NAS pomocí WebDAV

Všechny kroky jsou stejné jako pro SMB, kromě pole URL. Použijte `http://server-name` nebo `https://server-name`, pokud server podporuje SSL. WebDAV funguje se Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home a jakýmkoli jiným serverem s WebDAV endpointem.

Kompletní tutoriál o WebDAV je dostupný [zde](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Připojení přes DLNA/UPnP

Sdílejte mediální knihovnu umístěnou na Windows PC nebo NAS pomocí protokolu DLNA/UPnP a přistupujte k ní uvnitř Evervideo, jak je popsáno [zde](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA je široce podporováno, ale umožňuje pouze přehrávání nebo stahování videí — na DLNA server nelze nahrávat soubory ani vytvářet nové složky.

### Připojení pomocí FTP, FTPS nebo SFTP

Evervideo podporuje také klasické protokoly přenosu souborů. Pro připojení serveru přes FTP nebo FTPS klepněte na Připojit k cloudovému úložišti → FTP, zadejte URL hostitele ve formátu `ftp://server-name` (nebo `ftps://server-name` pro šifrované připojení), zadejte přihlašovací jméno a heslo a klepněte na Hotovo. Pro SFTP (SSH File Transfer Protocol) vyberte místo toho SFTP a zadejte heslo nebo pár klíčů SSH.

### Připojení k NFS sdílené složce

Evervideo zahrnuje podporu NFS (Network File System) — praktické pro Linux hostitele, BSD servery a NAS zařízení, která preferují zpřístupnění video knihoven přes NFS místo SMB. Vyberte NFS v nabídce Připojit k cloudovému úložišti, zadejte adresu serveru a exportovanou cestu a klepněte na Hotovo.

## Připojení Plex Media Serveru

Evervideo se může přímo připojit k Plex Media Serveru a procházet knihovny Filmů, TV pořadů a Domácích videí. Klepněte na Připojit k cloudovému úložišti → Plex, přihlaste se pomocí Plex účtu, vyberte server a knihovna se zobrazí vedle vašich cloudových služeb. Servery Plex ve stejné místní síti jsou také automaticky objeveny v sekci Dostupná zařízení.

## Připojení serveru Jellyfin nebo Emby

Jak Jellyfin (open-source) tak Emby (komerční) mediální servery fungují nativně v Evervideo. Klepněte na Připojit k cloudovému úložišti → Jellyfin nebo Emby, zadejte URL serveru (obvykle něco jako `http://server-ip:8096`) a přihlašovací údaje a vaše knihovna je připravena ke streamování.

## Připojení serveru Subsonic nebo Navidrome

Evervideo mluví Subsonic API, což znamená, že funguje se Subsonicem, Navidrome a každým jiným serverem kompatibilním se Subsonicem — včetně Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) a Ampache. Klepněte na Připojit k cloudovému úložišti → Subsonic, zadejte URL serveru a přihlašovací údaje a knihovna se zobrazí v sekci Cloudové úložiště.

## Připojení RTSP streamu (IP kamery, živé TV, IPTV)

Evervideo má nativní podporu RTSP, takže ho můžete nasměrovat na jakýkoli zdroj RTSP — bezpečnostní kamery, kamerové zvonky, poskytovatele IPTV, monitory pro miminko, vysílací kanály — a Evervideo bude stahovat a dekódovat stream živě. Klepněte na Online odkazy → Přidat odkaz, vložte celou URL (`rtsp://camera-ip:port/stream-path`), zadejte přihlašovací jméno a heslo, je-li požadováno, a klepněte na Hotovo.

## Připojení k objektovému úložišti kompatibilnímu s S3

Pro samohostitele a pokročilé uživatele používající cloudové objektové úložiště zahrnuje Evervideo konektor kompatibilní s S3. Klepněte na Připojit k cloudovému úložišti → Úložiště S3 a zadejte URL endpointu, region, přístupový klíč, tajný klíč a název bucketu. Funguje s AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a jakýmkoli jiným endpointem S3 API.

## Dostupná zařízení

Tato sekce zobrazuje každé zařízení ve vaší místní síti, ke kterému se můžete připojit z Evervideo přes Bonjour/mDNS objevování — servery Plex, Jellyfin, Emby, Synology, QNAP, routery AirPort s připojenými disky, Apple Time Capsule atd. Pro navázání připojení:

- Přejděte na sekci Dostupná zařízení v záložce Soubory.
- Klepněte na zařízení, ke kterému se chcete připojit.
- V případě potřeby zadejte přihlašovací údaje pro dokončení připojení.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dostupná zařízení v místní síti v Evervideo" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive umožňuje bezdrátový přenos souborů z počítače do iOS zařízení přes libovolný prohlížeč, Finder nebo Průzkumník souborů. Zařízení a počítač musí být ve stejné Wi-Fi síti.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive v Evervideo" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Aktivace Wi-Fi Drive

- V záložce Soubory přejděte na Cloudové úložiště → Připojit přes Wi-Fi pro otevření hlavní obrazovky Wi-Fi Drive.
- (Volitelně) Nastavte uživatelské jméno a heslo pro vestavěný webový server.
- Klepněte na Spustit Wi-Fi Drive.

### Přístup k Wi-Fi Drive z počítače

- Otevřete webový prohlížeč v počítači (Chrome, Firefox, Safari atd.).
- Zadejte URL zobrazené aplikací.
- Přetáhněte soubory z počítače na webovou stránku — začnou se přenášet do iOS zařízení.

Wi-Fi Drive lze také připojit přímo ve **Finderu** na macOS (Přejít → Připojit k serveru…) nebo Průzkumníku souborů ve Windows (Namapovat síťovou jednotku…) a zacházet s iPhone nebo iPad jako s běžnou síťovou jednotkou.

Podrobné pokyny jsou dostupné [zde](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Sdílení souborů iTunes/Finder

Sdílení souborů iTunes (nyní Sdílení souborů Finder na macOS Catalina a novějším) umožňuje přenášet soubory pomocí kabelu Lightning nebo USB-C. Připojte zařízení, otevřete Finder na Macu (nebo iTunes ve Windows), najděte Evervideo v seznamu aplikací a zkopírujte soubory do sdílené složky.

## Připojení USB flash disku nebo SD karty

Připojte USB disk nebo SD kartu k iPhone, iPad nebo Mac přes adaptér Lightning-to-USB/USB-C nebo čtečku karet. Otevřete Soubory → Soubory v tomto iPhone → Otevřít složku, přejděte na disk a vyberte video soubor nebo složku. Evervideo přehrává soubory přímo z disku bez kopírování do interního úložiště — praktické pro velmi velké 4K knihovny.

## Procházení složek v připojených úložištích

Klepněte na libovolnou připojenou cloudovou službu pro otevření prohlížeče souborů. Složky zobrazují náhledy videí, jsou-li dostupné, a klepnutím na video se okamžitě spustí přehrávání, zatímco zbytek souboru se nadále streamuje na pozadí.

{{< cards cols="1">}}
  {{< card title="" subtitle="Procházení složek v připojených úložištích v Evervideo" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Rychlý přístup

Sekce Rychlý přístup se nachází v horní části záložky Soubory. Poskytuje rychlý přístup k oblíbeným a naposledy otevřeným souborům a složkám — jak z cloudových služeb, tak z místního úložiště. Vždy když otevřete soubor nebo složku z cloudu, přidá se do seznamu Naposledy otevřených. Hluboce vnořené složky lze označit jako Oblíbené pro rychlý přístup bez procházení struktury adresářů.

{{< cards cols="1">}}
  {{< card title="" subtitle="Online odkazy a rychlý přístup v Evervideo" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Soubory v této aplikaci

Tato sekce zobrazuje soubory a složky uložené v sandboxovaném adresáři Dokumenty Evervideo — vše, co jste stáhli z cloudu, přenesli přes Wi-Fi Drive, zkopírovali přes Sdílení souborů Finder nebo importovali z jiné aplikace.

{{< cards cols="1">}}
  {{< card title="" subtitle="Soubory v této aplikaci v Evervideo" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Složka Dokumenty

Složka Dokumenty je kořenem všeho uvnitř sekce Soubory v této aplikaci. Můžete vytvářet podsložky, přejmenovávat soubory, přesouvat je a organizovat je jak chcete.

{{< cards cols="1">}}
  {{< card title="" subtitle="Místní soubory Evervideo — složka Dokumenty" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Soubory v tomto iPhone/iPad/Mac

Tato sekce zobrazuje videa umístěná ve vašem zařízení, ale v různých aplikacích. Můžete je importovat do Evervideo pomocí systémového výběru souborů:

- Klepněte na Otevřít soubory… pro výběr konkrétních souborů.
- Klepněte na Otevřít složku… pro výběr celé složky.

Můžete také použít Připojit složku pro vytvoření odkazu na složku ve vašem zařízení s přístupem pro čtení/zápis — ideální pro práci se složkou na iCloud Drive nebo připojeném USB disku bez kopírování čehokoli.

{{< cards cols="1">}}
  {{< card title="" subtitle="Soubory v tomto zařízení v Evervideo" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Speciální složky

V záložce Soubory uvidíte několik speciálních složek, které Evervideo automaticky vytváří a používá:

- **Stáhnout** — každý soubor stažený z cloudu se zobrazí zde ve výchozím nastavení. Přizpůsobte v Nastavení → Správce souborů → Uložit stažené soubory do.
- **Mezipaměť přehrávače** — mezipaměť přehrávače médií. Ve výchozím nastavení přehrávač stahuje nadcházející videa pro plynulé přehrávání. Mezipaměť lze vypnout v nastavení aplikace nebo tuto složku jednoduše smazat.
- **iCloud** — soubory v této složce se synchronizují napříč všemi zařízeními připojenými ke stejnému účtu iCloud.
- **Offline složky** — když označíte složku, playlist, album nebo žánr jako dostupné offline, soubory se stáhnou do této složky.

## Horní panel nástrojů

Horní panel nástrojů, umístěný pod navigační lištou, nabízí několik akcí, které lze zobrazit nebo skrýt gestem přejetí dolů:

- **Hledat** — provede vyhledávání v aktuální složce nebo sekci.
- **Pokračovat v přehrávání** — pokud je povoleno v nastavení, obnoví frontu přehrávače a poslední pozici videa pro aktuální složku.
- **Přehrát vše** — prohledá aktuální složku a podsložky a přidá soubory do fronty přehrávače.
- **Přehrát náhodně** — jako Přehrát vše, ale před přidáním zamíchá.

## Možnosti složky

Když otevřete složku, klepněte na tlačítko **"..."** v pravém horním rohu pro tyto akce:

- **Vybrat** — aktivuje režim výběru souborů.
- **Nová složka** — vytvoří novou složku v aktuální složce.
- **Povolit offline režim** — zapne offline synchronizaci pro aktuální složku. Nové soubory přidané online se automaticky stáhnou.
- **Nahrát soubory** — nahraje soubory ze zařízení do online složky.
- **Hledat** — vyhledá v složce.
- **Seřadit** — seřadí soubory podle názvu, velikosti, data změny nebo metadat.
- **Zobrazení mřížka/seznam** — přepíná mezi zobrazením tabulky a zobrazením miniatur. Zobrazení miniatur ukazuje velké náhledy posteru videa.

## Režim výběru

Klepněte na **"..."** v pravém horním rohu a zvolte **Vybrat** pro vstup do režimu výběru. Vedle každého souboru a složky se zobrazí zaškrtávací políčka. Klepnutím vyberte jednu nebo více položek a poté proveďte hromadné akce: Přehrát jako další, Přehrát později, Přidat do knihovny médií, Přidat do playlistu, Kopírovat, Nahrát, Přesunout, Přejmenovat nebo Smazat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Režim výběru ve správci souborů Evervideo" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Pokud chcete zacházet s připojeným cloudovým úložištěm jako s pouze pro čtení (abyste zabránili náhodnému mazání), povolte Nastavení → Správce souborů → Upravit online soubory → Vypnout, čímž skryjete všechny destruktivní operace z uživatelského rozhraní.

## Akce souboru

Klepněte na ikonu **"..."** u názvu souboru pro zobrazení nabídky akcí:

- **Přehrát jako další** — vloží soubor na začátek fronty přehrávače.
- **Přehrát později** — přidá soubor na konec fronty přehrávače.
- **Přidat do knihovny médií** — začlení soubor do knihovny médií, organizované podle alba a žánru.
- **Přidat do playlistu** — přidá soubor do existujícího playlistu nebo vytvoří nový.
- **Upravit tagy** — otevře vestavěný editor tagů pro úpravu metadat. U online souborů je soubor dočasně stažen, upraven a poté znovu nahrán po potvrzení.
- **Přidat do oblíbených** — přidá soubor do seznamu oblíbených pro rychlý přístup.
- **Stáhnout** — stáhne soubor nebo složku do zařízení pro offline použití.
- **Přejmenovat** — přejmenuje soubor přímo na vzdáleném úložišti.
- **Přesunout** — přesune soubor do jiné složky v cloudovém úložišti.
- **Přidat do archivu** — zabalí soubor do jednoho ZIP souboru (funkce Premium).
- **Otevřít v** — exportuje soubor do jiné kompatibilní aplikace přes systémový sdílecí list.
- **Smazat** — trvale odstraní soubor. **Tuto akci nelze vrátit zpět.**

## Akce složky

Pro každou složku v cloudovém úložišti máte k dispozici mnoho akcí klepnutím na ikonu **"..."** vedle názvu složky.

- **Přehrát vše** — nahradí aktuální frontu přehrávače všemi videi ve složce.
- **Přehrát jako další / Přehrát později** — přidá celou složku do fronty.
- **Přidat do knihovny médií** — začlení obsah složky do knihovny médií.
- **Přidat do playlistu** — přidá celou složku do playlistu.
- **Přidat do oblíbených** — přidá složku do oblíbených.
- **Povolit offline režim** — kromě jednoduchého stahování toto průběžně monitoruje složku pro nové soubory a automaticky je stahuje, jakmile se objeví online.
- **Stáhnout** — stáhne veškerý obsah složky do zařízení pro offline přístup.
- **Přejmenovat / Přesunout** — přejmenuje nebo přesune složku na vzdáleném úložišti.
- **Přidat do archivu** — zabalí obsah složky do ZIP souboru (funkce Premium).
- **Smazat** — trvale odstraní složku a její obsah. **Tuto akci nelze vrátit zpět.**

## Fronta přenosů

V pravém horním rohu záložky Soubory je tlačítko **Přenosy** (ikona točících se šipek). Klepněte na něj pro otevření fronty přenosů — seznam každého aktivního stahování a nahrávání ze všech zdrojů s průběhem v reálném čase, rychlostí a odhadovaným časem dokončení pro každý soubor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fronta přenosů souborů v Evervideo" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Přenosy můžete pozastavit, obnovit, opakovat neúspěšné přenosy, přeuspořádat položky pro upřednostnění konkrétních stahování nebo je individuálně zrušit. Rychlost fronty přenosů (maximální počet paralelních úloh), typ sítě (pouze Wi-Fi nebo Wi-Fi + Mobilní data) a přenosy na pozadí lze nastavit v Nastavení → Správce souborů.

{{< cards cols="1">}}
  {{< card title="" subtitle="Akce ve frontě přenosů souborů v Evervideo" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offline režim a synchronizované offline složky

Offline režim je praktická funkce, která vám umožňuje sledovat oblíbená videa i bez připojení k internetu. Když povolíte offline režim pro jakoukoli složku, playlist, album nebo žánr, všechny soubory v dané kolekci se automaticky stáhnou do zařízení pro offline přehrávání. Zobrazí se v sekci Offline složky.

Když na vzdálený server přidáte nové soubory, také se automaticky stáhnou — takže vaše offline kolekce zůstává aktuální bez jakéhokoli zásahu. Pro ruční opětovnou synchronizaci klepněte na tři tečky v pravém horním rohu offline složky a vyberte Synchronizovat.

Časový limit synchronizace lze upravit v Nastavení → Správce souborů → Synchronizované offline složky → Časový interval.

Podrobné pokyny jsou dostupné [zde](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalizace

V Nastavení → Personalizace lze nakonfigurovat, jak se záložka Soubory zobrazuje:

- **Styl obrazovky souborů** — Jednoduchá nabídka (zobrazuje seznam složek přímo) nebo Seskupená nabídka (seskupuje obsah podle kategorie — Rychlý přístup, Speciální složky, Cloudové úložiště atd.).
