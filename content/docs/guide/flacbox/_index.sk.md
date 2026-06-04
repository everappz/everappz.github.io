---
date: 2020-01-01
title: 'Flacbox'
description: 'Naučte sa používať Flacbox — hudobný prehrávač hi-res FLAC, DSD, ALAC a FFmpeg pre iPhone, iPad a Mac. Pripojte iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB a DLNA. Streamujte a sťahujte vysokorozlišovacie audio, upravujte metadáta, počúvajte audioknihy, scrobblujte na Last.fm, používajte Apple CarPlay a widgety plochy a prispôsobte 10-pásmový ekvalizér.'
keywords: [
  "používateľská príručka Flacbox", "ako na Flacbox", "hi-res hudobný prehrávač iPhone", "FLAC prehrávač iPhone",
  "DSD prehrávač iOS", "ALAC prehrávač Mac", "bezstratová hudobná aplikácia", "cloudový hudobný prehrávač iPhone",
  "offline FLAC prehrávač Mac", "správca hudobnej knižnice", "editor zvukových tagov",
  "CarPlay FLAC prehrávač", "Chromecast audio aplikácia", "AirPlay 2 hudba",
  "widgety Flacbox", "Flacbox CarPlay", "FFmpeg hudobný prehrávač iOS",
  "prehrávač audiokníh iPhone", "audio záložky iOS", "korekcia výšky tónu",
  "vzorkovacia frekvencia audio výstupu", "externý DAC iPhone", "USB DAC Mac",
  "Synology hudobná aplikácia", "QNAP hudobná aplikácia", "NAS hudobný prehrávač iPhone",
  "WebDAV hudobný prehrávač", "SMB hudobné streamovanie", "DLNA hudobný prehrávač",
  "iCloud Drive hudba", "Google Drive FLAC", "Dropbox FLAC prehrávač",
  "Wi-Fi Drive prenos hudby", "import M3U playlistu", "Last.fm scrobbling"
]
tags: ["flacbox", "príručka", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widgety"]
---


### Vitajte v príručke Flacbox

Flacbox je vysokorozlišovací hudobný prehrávač pre iPhone, iPad a Mac, ktorý vám umožňuje premeniť vaše obľúbené cloudové úložisko, NAS a mediálne servery na vlastnú osobnú streamovaciu službu.

Flacbox sa pripája k pozoruhodne širokému zoznamu zdrojov, všetky v jednej aplikácii:

- **Osobné cloudové úložisko:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Vlastnohostedné servery:** Plex · Jellyfin · Emby · Subsonic (a každý server kompatibilný so Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (a ownCloud cez zdieľané API) · Synology Drive · QNAP.
- **NAS a protokoly zdieľania súborov:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (heslo alebo autentifikácia verejným kľúčom) · NFS · DLNA / UPnP (prehrávanie a sťahovanie). Funguje s Apple Time Capsule, Synology, QNAP, WD My Cloud, akýmkoľvek Linux Samba / NFS / SSH hostiteľom alebo zdieľaným priečinkom na vašom Mac alebo Windows PC.
- **S3-kompatibilné objektové úložisko:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces a akýkoľvek iný S3-API endpoint.
- **Objavovanie lokálnej siete:** Sekcia Dostupné zariadenia automaticky vypíše každú Bonjour / mDNS službu vo vašej sieti Wi-Fi — servery Plex, Jellyfin, Emby, Synology, QNAP, AirPort routery s pripojenými diskami, Time Capsule — takže sa môžete pripojiť klepnutím bez zadávania IP adresy.

Kým väčšina hudobných aplikácií používa iba zabudovaný audio engine Apple, Flacbox pridáva **FFmpeg** popri systémových kodekoch, takže môžete prehrávať formáty, ktoré iOS nepodporuje — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, plus bežná rodina MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. V kombinácii s konfigurovateľnou vzorkovacou frekvenciou audio výstupu (44,1 / 48 / 64 / 88,2 / 96 kHz), viackanálovým výstupom (Mono → 5.1 → SDDS → ITU BS.775-1), ladením IO bufferu a korekciou výšky tónu, Flacbox dáva audiofinom kontrolu, ktorú väčšina spotrebiteľských hudobných aplikácií jednoducho neponúka.

### Užívajte si plynulé streamovanie a offline prehrávanie

Flacbox disponuje inteligentným bufferovaním pre plynulé streamovanie a zabudovaným správcom sťahovania, takže môžete stiahnuť celé playlisty, umelcov, albumy, priečinky alebo jednotlivé skladby na vaše zariadenie pre offline použitie. Keď vám dochádza úložisko, vymažete vyrovnávacie súbory jedným klepnutím a pokračujete v streamovaní z cloudu. Offline režim pre priečinky, playlisty, albumy a umelcov tiež automaticky synchronizuje nové skladby v momente, keď sa objavia v cloude, takže vaša offline kolekcia je vždy aktuálna.

### Automaticky organizovaná hudobná knižnica

Keď importujete audio skladby, Flacbox skenuje ich metadáta a organizuje ich do prehľadnej hudobnej knižnice — zoskupené podľa Skladieb, Neprehrané skladby, Albumov, Albumových umelcov, Umelcov, Žánrov a Skladateľov. Pomocou zabudovaného vyhľadávania nájdete čokoľvek v priebehu sekúnd, filtrujete podľa zdroja (online cloud / offline / zariadenie) a vyberáte medzi rozloženiami knižnice Plain / Grouped / Tabbed. Pre knižnice so zmiešanými kompilačnými albumami "rôznych umelcov" Flacbox poskytuje dedikované zobrazenia Všetky albumy / Exkluzívne albumy / Sólové albumy pre správne výsledky bez šumu.

### Opravte metadáta a tagujte svoju hudbu

Ak narazíte na poškodené tagy alebo neporiadne kódovanie (bežný problém pri ripovaných alebo starších súboroch), zabudovaný editor ID3 tagov ich môže vyčistiť — ručne alebo pomocou automatického vyhľadávania MusicBrainz. Môžete tiež normalizovať poškodené kódovanie znakov (skvelé pre kyrillické, japonské alebo čínske tagy, ktoré prišli z Windows PC), vyhľadávať chýbajúce albumové obaly a zapisovať zmeny späť do pôvodného súboru v cloude automaticky. Pre hlbšie hromadné úpravy nainštalujte našu sprievodnú aplikáciu Evertag.

### Jednoduché presuny z Mac, PC alebo NAS

Preneste hudbu medzi počítačom a vaším iPhone alebo iPad pomocou niektorého z týchto nástrojov: SMB, WebDAV, DLNA, Wi-Fi Drive (drag-and-drop v akomkoľvek desktopovom prehliadači), iTunes / Finder File Sharing cez Lightning alebo USB-C kábel, USB flash disky alebo iXpand Flash Drives. Máte Apple Time Capsule, WD My Cloud, Synology, QNAP alebo iný NAS, ktorý vystavuje SMB / WebDAV / DLNA / FTP / SFTP? Pripojte raz a streamujte celú knižnicu bez zaberania úložného priestoru zariadenia.

### Prispôsobte zvuk pomocou ekvalizéra

Flacbox obsahuje 10-pásmový ekvalizér s predvoľbami v štýle iPod (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz a mnoho ďalších), preamp a možnosť ukladať vlastné predvoľby. Či už ladíte pre pár audiofílnych IEM, HomePod mini alebo autorádiom, môžete tvarovať zvuk presne podľa svojich predstáv.

### Vhodné pre audioknihy

Flacbox je skvelý prehrávač audiokníh — viacero záložiek na skladbu, jemné riadenie rýchlosti prehrávania (0,02× až 3,00×), pokračovanie v prehrávaní presne tam, kde ste zastavili, prispôsobiteľné tlačidlá preskočenia a časovač spánku, ktorý jemne stíši pred spaním. Značky kapitol M4B a dlhé súbory sú plne podporované.

### Streamujte kdekoľvek — vrátane auta a plochy

Streamujte hudbu na Apple TV / HomePod cez AirPlay 2, odošlite ju na reproduktory Google Chromecast a televízory s Cast, a vezmite všetko na cestu s Apple CarPlay. Používajte widgety plochy na iPhone a iPad na zobrazenie aktuálne prehrávanej skladby na prvý pohľad a Last.fm scrobbling na uchovanie histórie počúvania naprieč aplikáciami.

### Súkromie a bezpečnosť

Flacbox používa iba oficiálne SDK a OAuth prihlásenia od každého poskytovateľa cloudu — vaše heslo sa nikdy nedostane do aplikácie. Prístupové tokeny sú šifrované v iOS Keychain, všetky prenosy sú chránené TLS a odvolanie prístupu v cloudovom účte alebo odstránenie Flacbox zo zariadenia okamžite vymaže všetko. Chráňte svoju knižnicu voliteľným prístupovým kódom pre extra vrstvu súkromia.

### Začíname s Flacbox

Táto príručka vás prevedie každou časťou Flacbox na iPhone, iPad a Mac — od pripájania cloudových služieb, organizovania knižnice, prenosu súborov a správy playlistov, až po jemné doladenie ekvalizéra a konfiguráciu audio enginu. Použite karty nižšie na rýchle skočenie priamo na požadovanú sekciu.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigácia" subtitle="Tab Bar na iPhone, ľavé menu na iPad a Mac, mini prehrávač, widgety, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Pripojenia" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Hudobná knižnica" subtitle="Skladby, albumy, umelci, žánre, skladatelia — synchronizácia, vyhľadávanie, úprava metadát." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Prehrávače" subtitle="Vytvorte, importujte M3U / M3U8 / CUE, zmeňte poradie a exportujte do M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Lokálne súbory" subtitle="Offline hudba, USB disky, Wi-Fi Drive, správca súborov, offline priečinky." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Audio prehrávač" subtitle="Hi-res výstup, ekvalizér, výška tónu, záložky, AirPlay, Chromecast, rýchlosť, časovač spánku." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Nastavenia" subtitle="Audio engine, knižnica, správca súborov, CarPlay, widgety, personalizácia, jazyk, záloha." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Nájdite odpovede na 50 najčastejších otázok o Flacbox." >}}

{{< /cards >}}
