---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Naučte se používat Evervideo — kompletní cloudový přehrávač videí pro iPhone, iPad a Mac. Streamujte a stahujte videa z iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP/SFTP, DLNA a S3 — a také z Plex, Jellyfin, Emby, Subsonic a Navidrome. Picture-in-Picture, primární a sekundární titulky, ekvalizéry zvuku a videa, RTSP streamy IP kamer, Chromecast, AirPlay 2, hardwarové dekódování H.264/HEVC, integrace knihovny Fotek a Apple Music a kompaktní přehrávač vždy na obrazovce.'
keywords: [
  "průvodce Evervideo", "jak používat Evervideo", "cloudový přehrávač videí iPhone", "přehrávač videí Mac",
  "přehrávač MKV iOS", "přehrávač videí FFmpeg", "přehrávač HEVC iPhone",
  "Picture-in-Picture video iPhone", "přehrávač PiP video iPad",
  "přehrávač RTSP iPhone", "prohlížeč IP kamer", "přehrávač DLNA video",
  "klient Plex iPhone", "klient Jellyfin iOS", "klient Emby iPad",
  "přehrávač titulků iOS", "titulky SRT VTT ASS", "sekundární titulky iPhone",
  "ekvalizér videa iOS", "ekvalizér zvuku přehrávač videí", "externí DAC video",
  "streamovat video z Google Drive", "streamovat video z Dropbox",
  "streamovat video z OneDrive", "streamovat video z iCloud Drive",
  "streamovat video z MEGA", "streamovat video z NAS",
  "Chromecast video iPhone", "AirPlay 2 video", "cloudový přehrávač videí iCloud",
  "přehrávač videí knihovna Fotek", "přehrávač videí Apple Music",
  "přenos videí Wi-Fi Drive", "playlist videí M3U",
  "Evervideo Premium", "aplikace videí Family Sharing"
]
tags: ["evervideo", "průvodce", "přehrávač videí", "PiP", "titulky", "RTSP", "cloud", "FFmpeg"]
---


### Vítejte v průvodci Evervideo

Evervideo je plnohodnotný cloudový přehrávač médií pro iPhone, iPad a Mac, který přemění libovolný cloudový účet, NAS nebo mediální server na vaši osobní knihovnu médií — bez nutnosti cokoliv znovu nahrávat a při zachování plné kontroly nad soubory.

Postaven na vlastním přehrávacím stroji založeném na FFmpeg s hardwarovým dekódováním H.264 a HEVC, Evervideo přehrává prakticky jakýkoli moderní kontejner a kodek — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS a dlouhý seznam formátů FFmpeg — v plné kvalitě s inteligentním bufferováním pro plynulé streamování přes Wi-Fi nebo mobilní data. Picture-in-Picture udržuje video nad všemi ostatními aplikacemi, kompaktní přehrávač vždy na obrazovce vám umožňuje sledovat během procházení knihovny a Chromecast a AirPlay 2 přenášejí přehrávání na televizor, HomePod nebo reproduktory jediným klepnutím.

Evervideo se připojuje k pozoruhodně širokému seznamu zdrojů, vše z jedné aplikace:

- **Osobní cloudové úložiště:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Lokálně hostované mediální servery:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (a ownCloud přes sdílené API) · Synology Drive · QNAP.
- **Protokoly NAS a sdílení souborů:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP/HTTPS) · FTP · FTPS · SFTP (heslo nebo autentizace veřejným klíčem) · NFS · DLNA · UPnP.
- **Živé streamy a IP kamery:** RTSP — nasměrujte Evervideo na jakoukoliv RTSP URL (`rtsp://camera-ip/stream`) a prostě přehraje.
- **Objektové úložiště kompatibilní s S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a jakýkoli jiný endpoint S3 API.
- **Zdroje v zařízení:** knihovna Fotek (Všechna videa, Krátká/Střední/Dlouhá, Záznamy obrazovky a vaše Fotoalba), knihovna aplikace Hudba (Alba, Žánry, Seznamy skladeb), USB/SD disky a Místní soubory.

### Jeden přehrávač pro všechny formáty a kodeky

Kde většina iOS aplikací končí u H.264/H.265 uvnitř MP4/MOV, Evervideo zahrnuje FFmpeg vedle systémových kodeků Apple, takže můžete přehrávat formáty, které systém nerozpozná — kontejnery MKV, VP9, AV1, MPEG-2, OGG, Vorbis a mnoho dalších — a automaticky přepíná mezi hardwarovým H.264/HEVC dekódováním a softwarovým dekódováním na základě souboru a zařízení.

Můžete vybrat video stopu (multi-streamové Blu-ray ripy), zvukovou stopu (komentářové stopy, alternativní dabingy) a titulkovou stopu. Externí soubory titulků SRT, VTT a ASS/SSA se načtou jedním klepnutím; pokročilé stylování ASS/SSA je správně vykresleno díky přiložené knihovně libass.

### Chytré titulky

- **Výběr titulkové stopy** — ideální pro výuku jazyků.
- **Externí soubory titulků** (`.srt`, `.vtt`, `.ass`, `.ssa`) načtené z libovolného místa v zařízení nebo z cloudu.
- **libass** pro plně stylizované vykreslování ASS/SSA.
- **Výběr písma pro každou stopu a globálně** pro titulky.
- **Výběr zvukové stopy** — vyberte dabing, komentář nebo stopu režiséra.
- **Výběr video stopy** pro soubory s více úhly nebo verzemi.

### Doladění obrazu a zvuku

Dva ekvalizéry vedle sebe: zvukový ekvalizér pro ladění basů a výšek (s importem/exportem vlastních předvoleb) a video ekvalizér pro nastavení jasu, kontrastu, sytosti a odstínu (opět s importem/exportem). Oba stroje také nabízejí audiofil kontroly: výstupní vzorkovací frekvence zvuku, počet kanálů, trvání IO bufferu a smíšený režim — pro uživatele s externími DAC a domácími kiny.

### Cast, AirPlay a Picture-in-Picture

- **Picture-in-Picture (PiP):** sledujte dál, zatímco používáte jiné aplikace.
- **AirPlay 2:** odesílejte video na Apple TV, HomePod nebo jakýkoli reproduktor/televizor kompatibilní s AirPlay 2.
- **Google Chromecast:** přenášejte přímo na Chromecast nebo televizor s Cast.
- **Kompaktní přehrávač:** trvalý mini přehrávač v horní části každé obrazovky, takže můžete procházet knihovnu bez ztráty videa.

### Ochrana soukromí a zabezpečení

Evervideo používá pouze oficiální SDK a přihlašování pomocí OAuth od každého poskytovatele cloudu, takže vaše heslo se do aplikace nikdy nedostane. Přístupové tokeny jsou uloženy šifrovaně v iOS/MacOS Keychain, každý přenos je chráněn TLS a zrušení přístupu z vašeho cloudového účtu (nebo odebrání Evervideo ze zařízení) okamžitě vymaže vše. Chraňte svou knihovnu volitelným 4místným přístupovým kódem pro extra vrstvu soukromí.

### Začínáme s Evervideo

Tento průvodce vás provede každou částí Evervideo na iPhone, iPad a Mac — od připojení cloudových služeb, procházení knihovny, stahování a přenosu souborů, správy playlistů, až po doladění přehrávače médií, ekvalizérů, titulků a Picture-in-Picture. Pomocí karet níže přejděte přímo na sekci, kterou potřebujete.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navigace" subtitle="Lišta záložek na iPhone, levé menu na iPad a Mac, kompaktní přehrávač médií vždy na obrazovce." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Soubory" subtitle="Jedna sjednocená záložka pro cloud, NAS, RTSP streamy, místní soubory, USB disky a frontu přenosů." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Knihovna médií" subtitle="Procházejte podle alb, žánrů, nedávných, oblíbených — plus knihovna Fotek iOS a knihovna Apple Music." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Seznamy skladeb" subtitle="Vytvářejte playlisty z cloudu, místních souborů, Fotek nebo knihovny Hudby, importujte M3U/M3U8/CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Přehrávač médií" subtitle="Picture-in-Picture, zvukové a video stopy, titulky, ekvalizéry zvuku a videa, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Nastavení" subtitle="Zvukový stroj, video dekodér, titulky, knihovna, správce souborů, widgety, personalizace, jazyk, záloha." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="Nejčastější dotazy" subtitle="Najděte odpovědi na nejčastější otázky o Evervideo." >}}

{{< /cards >}}
