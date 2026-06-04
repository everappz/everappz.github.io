---
date: 2020-01-01
title: 'Flacbox'
description: 'Naučte se používat Flacbox — hi-res cloudový hudební přehrávač s podporou FLAC, DSD, ALAC a FFmpeg pro iPhone, iPad a Mac. Připojte iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB a DLNA. Streamujte a stahujte zvuk ve vysokém rozlišení, upravujte metadata, poslouchejte audioknihy, scrobblujte na Last.fm, používejte Apple CarPlay a widgety plochy a přizpůsobte 10pásmový ekvalizér.'
keywords: [
  "uživatelská příručka Flacbox", "jak používat Flacbox", "hi-res přehrávač hudby iPhone", "přehrávač FLAC iPhone",
  "přehrávač DSD iOS", "přehrávač ALAC Mac", "aplikace pro bezztrátovou hudbu", "cloudový hudební přehrávač iPhone",
  "offline přehrávač FLAC Mac", "správce hudební knihovny", "editor zvukových tagů",
  "přehrávač FLAC CarPlay", "aplikace pro zvuk Chromecast", "hudba AirPlay 2",
  "widgety Flacbox", "Flacbox CarPlay", "hudební přehrávač FFmpeg iOS",
  "přehrávač audioknih iPhone", "záložky zvuku iOS", "aplikace pro korekci výšky tónu",
  "vzorkovací frekvence zvukového výstupu", "externí DAC iPhone", "USB DAC Mac",
  "hudební aplikace Synology", "hudební aplikace QNAP", "hudební přehrávač NAS iPhone",
  "hudební přehrávač WebDAV", "streamování hudby SMB", "hudební přehrávač DLNA",
  "hudba iCloud Drive", "Google Drive FLAC", "přehrávač FLAC Dropbox",
  "přenos hudby Wi-Fi Drive", "import seznamu M3U", "scrobbling Last.fm"
]
tags: ["flacbox", "příručka", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widgety"]
---


### Vítejte v průvodci Flacbox

Flacbox je hi-res hudební přehrávač pro iPhone, iPad a Mac, který vám umožňuje proměnit oblíbené cloudové úložiště, NAS a mediální servery ve vlastní osobní streamovací službu.

Flacbox se připojuje k pozoruhodně širokému seznamu zdrojů, vše v jedné aplikaci:

- **Osobní cloudové úložiště:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Vlastní servery:** Plex · Jellyfin · Emby · Subsonic (a každý server kompatibilní se Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (a ownCloud přes sdílené API) · Synology Drive · QNAP.
- **NAS a protokoly pro sdílení souborů:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (heslo nebo autentizace veřejným klíčem) · NFS · DLNA / UPnP (přehrávání a stahování). Funguje s Apple Time Capsule, Synology, QNAP, WD My Cloud, jakýmkoli hostitelem Linux Samba / NFS / SSH nebo sdílenou složkou na vašem Macu nebo Windows PC.
- **Objektové úložiště kompatibilní s S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a jakýkoli jiný endpoint S3-API.
- **Vyhledávání v lokální síti:** Sekce Dostupná zařízení automaticky zobrazuje každou službu Bonjour / mDNS ve vaší síti Wi-Fi — servery Plex, Jellyfin, Emby, Synology, QNAP, routery AirPort s připojenými disky, Time Capsule — takže se můžete připojit klepnutím bez zadávání IP adresy.

Zatímco většina hudebních aplikací se omezuje na vestavěný zvukový engine Apple, Flacbox obsahuje **FFmpeg** vedle systémových kodeků, takže můžete přehrávat formáty, které iOS standardně nepodporuje — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, plus běžná rodina MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. V kombinaci s konfigurovatelnou vzorkovací frekvencí zvukového výstupu (44,1 / 48 / 64 / 88,2 / 96 kHz), vícekánálový výstup (Mono → 5.1 → SDDS → ITU BS.775-1), ladění vyrovnávací paměti IO a korekcí výšky tónu dává Flacbox audiofili kontrolu, kterou většina spotřebitelských hudebních aplikací jednoduše nenabízí.

### Užijte si Plynulé Streamování a Offline Přehrávání

Flacbox disponuje chytrým bufferováním pro plynulé streamování a vestavěným správcem stahování, takže si můžete stáhnout celé seznamy skladeb, interprety, alba, složky nebo jednotlivé stopy do zařízení pro offline použití. Když dojde místo, vymažte soubory v mezipaměti jedním klepnutím a pokračujte ve streamování z cloudu. Offline režim pro složky, seznamy skladeb, alba a interprety také automaticky synchronizuje nové stopy ve chvíli, kdy se objeví v cloudu, takže vaše offline sbírka je vždy aktuální.

### Automaticky Organizovaná Hudební Knihovna

Když importujete zvukové stopy, Flacbox prohledá jejich metadata a zorganizuje je do přehledné hudební knihovny — seskupené podle Skladeb, Nepřehraných skladeb, Alb, Interpretů alba, Interpretů, Žánrů a Skladatelů. Pomocí vestavěného vyhledávání najdete cokoli během sekund, filtrujte podle zdroje (online cloud / offline / zařízení) a vybírejte mezi jednoduchým / seskupeným / záložkovým rozvržením knihovny. Pro knihovny se smíšenými kompilacemi 'různých interpretů' nabízí Flacbox speciální pohledy Všechna alba / Výhradní alba / Sólová alba pro zobrazení správných výsledků bez šumu.

### Opravte Metadata a Otagujte Svou Hudbu

Pokud narazíte na poškozené tagy nebo chaotické kódování (běžný problém u ripnutých nebo starších souborů), vestavěný editor tagů ID3 je může vyčistit — ručně nebo automatickým vyhledáváním v MusicBrainz. Můžete také normalizovat poškozená kódování znaků (skvělé pro cyrilická, japonská nebo čínská označení z počítačů Windows), vyhledávat chybějící obaly alb a automaticky zapsat změny zpět do původního souboru v cloudu. Pro hlubší dávkové úpravy nainstalujte naši doplňkovou aplikaci Evertag.

### Snadné Přenosy z Macu, PC nebo NAS

Přesouvejte hudbu mezi počítačem a iPhonem nebo iPadem pomocí libovolného z těchto nástrojů: SMB, WebDAV, DLNA, Wi-Fi Drive (přetažení v jakémkoli desktopovém prohlížeči), sdílení souborů iTunes / Finder přes kabel Lightning nebo USB-C, USB flash disky nebo iXpand Flash Drives. Máte Apple Time Capsule, WD My Cloud, Synology, QNAP nebo jiný NAS, který zpřístupňuje SMB / WebDAV / DLNA / FTP / SFTP? Připojte se jednou a streamujte celou knihovnu bez zabírání místa v zařízení.

### Přizpůsobte Zvuk Pomocí Ekvalizéru

Flacbox obsahuje 10pásmový ekvalizér s předvolbami ve stylu iPod (Akustika, Baskytara, Klasika, Dance, Rock, Pop, Jazz a mnoho dalšího), předzesilovač a možnost ukládat vlastní předvolby. Ať už ladíte pro audiofílní IEM, HomePod mini nebo autoradio, můžete zvuk tvarovat přesně podle svých představ.

### Vhodný pro Audioknihy

Flacbox je skvělý přehrávač audioknih — více záložek na stopu, přesná rychlost přehrávání (0,02× až 3,00×), pokračování přehrávání pro obnovení přesně tam, kde jste skončili, přizpůsobitelná tlačítka přeskočení a časovač spánku, který se na noc tiše ztlumí. Značky kapitol M4B a dlouhé soubory jsou plně podporovány.

### Streamujte Kdekoli — Včetně Vašeho Auta a Plochy

Streamujte hudbu do Apple TV / HomePod přes AirPlay 2, odesílejte ji do reproduktorů Google Chromecast a televizorů s podporou Cast a vše vezměte na cesty s Apple CarPlay. Používejte widgety plochy na iPhonu a iPadu pro zobrazení aktuálně přehrávané stopy na první pohled a scrobbling Last.fm pro uchovávání historii poslechu napříč aplikacemi.

### Soukromí a Bezpečnost

Flacbox používá pouze oficiální SDK a přihlašování přes OAuth od každého poskytovatele cloudu — vaše heslo se nikdy nedostane do aplikace. Přístupové tokeny jsou uloženy šifrovaně v iOS Keychain, všechny přenosy jsou chráněny TLS a odvolání přístupu v cloudovém účtu nebo odebrání Flacboxu ze zařízení vše okamžitě smaže. Chraňte svou knihovnu volitelným přístupovým kódem pro další vrstvu soukromí.

### Začínáme s Flacbox

Tato příručka vás provede každou částí Flacboxu na iPhonu, iPadu a Macu — od připojení cloudových služeb, organizování knihovny, přenosu souborů a správy seznamů skladeb až po doladění ekvalizéru a konfiguraci zvukového engine. Pomocí karet níže přejděte přímo do sekce, kterou potřebujete.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigace" subtitle="Lišta záložek na iPhonu, levé menu na iPadu a Macu, mini přehrávač, widgety, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Připojení" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Hudební knihovna" subtitle="Skladby, alba, interpreti, žánry, skladatelé — synchronizace, vyhledávání, úprava metadat." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Seznamy skladeb" subtitle="Vytvářejte, importujte M3U / M3U8 / CUE, řaďte a exportujte do M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Místní soubory" subtitle="Offline hudba, USB disky, Wi-Fi Drive, správce souborů, offline složky." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Přehrávač zvuku" subtitle="Hi-res výstup, ekvalizér, výška tónu, záložky, AirPlay, Chromecast, rychlost, časovač spánku." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Nastavení" subtitle="Zvukový engine, knihovna, správce souborů, CarPlay, widgety, personalizace, jazyk, záloha." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="Časté dotazy" subtitle="Najděte odpovědi na 50 nejčastějších otázek o Flacbox." >}}

{{< /cards >}}
