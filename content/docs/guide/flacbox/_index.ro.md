---
date: 2020-01-01
title: 'Flacbox'
description: 'Aflați cum să utilizați Flacbox — playerul de muzică hi-res cu FLAC, DSD, ALAC și FFmpeg pentru iPhone, iPad și Mac. Conectați iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB și DLNA. Transmiteți și descărcați audio de înaltă rezoluție, editați metadate, ascultați cărți audio, utilizați scrobbling pe Last.fm, Apple CarPlay și widget-uri pe ecranul principal și personalizați egalizatorul pe 10 benzi.'
keywords: [
  "ghid Flacbox", "cum se folosește Flacbox", "player muzică hi-res iPhone", "player FLAC iPhone",
  "player DSD iOS", "player ALAC Mac", "aplicație muzică fără pierderi", "player muzică cloud iPhone",
  "player FLAC offline Mac", "manager bibliotecă muzicală", "editor etichete audio",
  "player FLAC CarPlay", "aplicație audio Chromecast", "muzică AirPlay 2",
  "widget-uri Flacbox", "Flacbox CarPlay", "player muzică FFmpeg iOS",
  "player cărți audio iPhone", "marcaje audio iOS", "aplicație corecție ton",
  "rată eșantionare ieșire audio", "DAC extern iPhone", "USB DAC Mac",
  "aplicație muzică Synology", "aplicație muzică QNAP", "player muzică NAS iPhone",
  "player WebDAV", "streaming SMB", "player DLNA",
  "muzică iCloud Drive", "Google Drive FLAC", "player FLAC Dropbox",
  "transfer muzică Wi-Fi Drive", "import playlist M3U", "scrobbling Last.fm"
]
tags: ["flacbox", "ghid", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widget-uri"]
---


### Bun venit în Ghidul Flacbox

Flacbox este un player de muzică de înaltă rezoluție pentru iPhone, iPad și Mac care vă permite să transformați serviciul preferat de stocare în cloud, NAS și serverele media în propriul serviciu personal de streaming.

Flacbox se conectează la o listă remarcabil de largă de surse, toate într-o singură aplicație:

- **Stocare personală în cloud:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servere auto-găzduite:** Plex · Jellyfin · Emby · Subsonic (și orice server compatibil Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (și ownCloud prin API-ul partajat) · Synology Drive · QNAP.
- **Protocoale NAS și partajare fișiere:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (parolă sau autentificare cu cheie publică) · NFS · DLNA / UPnP (redare și descărcare). Funcționează cu Apple Time Capsule, Synology, QNAP, WD My Cloud, orice gazdă Linux Samba / NFS / SSH sau un folder partajat pe Mac sau PC Windows.
- **Stocare de obiecte compatibilă S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces și orice alt endpoint S3-API.
- **Descoperire în rețeaua locală:** Secțiunea Dispozitive disponibile listează automat fiecare serviciu Bonjour / mDNS din rețeaua Wi-Fi — servere Plex, Jellyfin, Emby, Synology, QNAP, routere AirPort cu unități atașate, Time Capsule — astfel încât puteți conecta fără a tasta o adresă IP.

În timp ce majoritatea aplicațiilor de muzică folosesc motorul audio integrat al Apple, Flacbox include **FFmpeg** alături de codecurile sistemului, astfel încât puteți reda formate pe care iOS nu le acceptă nativ — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, plus familia obișnuită MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. Combinat cu o rată de eșantionare configurabilă a ieșirii audio (44,1 / 48 / 64 / 88,2 / 96 kHz), ieșire multicanal (Mono → 5.1 → SDDS → ITU BS.775-1), reglaj buffer IO și corecție ton, Flacbox oferă audiofilor un control pe care majoritatea aplicațiilor de muzică pentru consumatori pur și simplu nu îl oferă.

### Bucurați-vă de Streaming Fluid și Redare Offline

Flacbox dispune de buffering inteligent pentru streaming fluid și un manager de descărcări integrat, astfel încât puteți descărca liste de redare, artiști, albume, foldere sau piese individuale pe dispozitivul dvs. pentru utilizare offline. Când spațiul de stocare este limitat, ștergeți fișierele din cache cu o singură atingere și continuați să transmiteți din cloud. Modul offline pentru foldere, liste de redare, albume și artiști sincronizează automat piesele noi imediat ce apar în cloud, astfel colecția dvs. offline rămâne mereu actualizată.

### Bibliotecă Muzicală Organizată Automat

Când importați piese audio, Flacbox scanează metadatele acestora și le organizează într-o Bibliotecă Muzicală ordonată — grupate pe Cântece, Cântece neredate, Albume, Artiști de album, Artiști, Genuri și Compozitori. Folosiți căutarea integrată pentru a găsi orice în câteva secunde, filtrați după sursă (cloud online / offline / dispozitiv) și alegeți între aspectele de bibliotecă Simplu / Grupat / Cu file. Pentru biblioteci cu compilații mixte de „artiști diverși", Flacbox oferă vizualizări dedicate Toate albumele / Albume exclusive / Albume solo pentru a afișa rezultatele corecte fără zgomot.

### Corectați Metadatele și Etichetați Muzica

Dacă întâlniți etichete corupte sau codificări dezordonate (o problemă frecventă pentru fișierele ripped sau mai vechi), editorul de etichete ID3 integrat le poate curăța — manual sau cu căutări automate MusicBrainz. Puteți, de asemenea, normaliza codificările de caractere deteriorate (excelent pentru etichete chirilice, japoneze sau chinezești provenite de pe PC-uri Windows), căuta coperți de album lipsă și scrie modificările înapoi în fișierul original din cloud automat. Pentru editare în lot mai aprofundată, instalați aplicația noastră complementară Evertag.

### Transferuri Ușoare de pe Mac, PC sau NAS

Mutați muzică între computer și iPhone sau iPad cu oricare dintre aceste instrumente: SMB, WebDAV, DLNA, Wi-Fi Drive (glisare și plasare în orice browser de desktop), Partajare fișiere iTunes / Finder printr-un cablu Lightning sau USB-C, unități USB flash sau iXpand Flash Drives. Aveți un Apple Time Capsule, WD My Cloud, Synology, QNAP sau orice alt NAS care expune SMB / WebDAV / DLNA / FTP / SFTP? Conectați o dată și transmiteți întreaga bibliotecă fără a ocupa spațiu pe dispozitiv.

### Personalizați Sunetul cu Egalizatorul

Flacbox include un egalizator pe 10 benzi cu presetări în stil iPod (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz și multe altele), un preamplificator și posibilitatea de a salva propriile presetări. Indiferent dacă reglați pentru niște IEM-uri audiofil, un HomePod mini sau un sistem audio auto, puteți modela sunetul exact cum doriți.

### Prietenos cu Cărțile Audio

Flacbox este un excelent player pentru cărți audio — mai multe marcaje per pistă, viteză de redare precisă (0,02× la 3,00×), continuarea redării exact de unde ați oprit, butoane de salt personalizabile și un temporizator de somn care reduce treptat volumul la culcare. Marcajele de capitole M4B și fișierele lungi sunt complet acceptate.

### Transmiteți Oriunde — Inclusiv în Mașina Dvs. și pe Ecranul Principal

Transmiteți muzică pe Apple TV / HomePod prin AirPlay 2, trimiteți-o pe difuzoarele Google Chromecast și televizoarele cu Cast, și luați totul la drum cu Apple CarPlay. Folosiți widget-uri pe ecranul principal pe iPhone și iPad pentru a vedea piesa curentă dintr-o privire, iar scrobbling-ul Last.fm vă menține istoricul ascultărilor în toate aplicațiile.

### Confidențialitate și Securitate

Flacbox folosește numai SDK-uri oficiale și autentificări bazate pe OAuth de la fiecare furnizor de cloud — parola dvs. nu ajunge niciodată la aplicație. Tokenurile de acces sunt stocate criptat în iOS Keychain, toate transferurile sunt protejate TLS, iar revocarea accesului în contul cloud sau eliminarea Flacbox de pe dispozitiv șterge totul instantaneu. Protejați-vă biblioteca cu un cod de acces opțional pentru un strat suplimentar de confidențialitate.

### Primii Pași cu Flacbox

Acest ghid vă îndrumă prin fiecare parte a Flacbox pe iPhone, iPad și Mac — de la conectarea serviciilor cloud, organizarea bibliotecii, transferul fișierelor și gestionarea listelor de redare, până la reglarea fină a egalizatorului și configurarea motorului audio. Folosiți cardurile de mai jos pentru a sări direct la secțiunea de care aveți nevoie.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigare" subtitle="Bara de file pe iPhone, meniu stânga pe iPad și Mac, mini player, widget-uri, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Conexiuni" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Bibliotecă Muzicală" subtitle="Cântece, albume, artiști, genuri, compozitori — sincronizare, căutare, editare metadate." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Liste de redare" subtitle="Creați, importați M3U / M3U8 / CUE, reordonați și exportați în M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Fișiere Locale" subtitle="Muzică offline, unități USB, Wi-Fi Drive, manager fișiere, foldere offline." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Player Audio" subtitle="Ieșire hi-res, egalizator, corecție ton, marcaje, AirPlay, Chromecast, viteză, temporizator somn." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Setări" subtitle="Motor audio, bibliotecă, manager fișiere, CarPlay, widget-uri, personalizare, limbă, copie de rezervă." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Găsiți răspunsuri la cele mai frecvente 50 de întrebări despre Flacbox." >}}

{{< /cards >}}
