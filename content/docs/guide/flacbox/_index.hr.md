---
date: 2020-01-01
title: 'Flacbox'
description: 'Naučite kako koristiti Flacbox — hi-res FLAC, DSD, ALAC i FFmpeg-pogonjen cloud glazbeni player za iPhone, iPad i Mac. Povežite iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB i DLNA. Streamajte i preuzimajte visokokvalitetni audio, uređujte metapodatke, slušajte audioknjige, scrobblajte na Last.fm, koristite Apple CarPlay i widgete početnog zaslona, te prilagodite 10-pojasni ekvilajzer.'
keywords: [
  "Flacbox korisnički vodič", "kako koristiti Flacbox", "hi-res glazbeni player iPhone", "FLAC player iPhone",
  "DSD player iOS", "ALAC player Mac", "aplikacija za glazbu bez gubitaka", "cloud glazbeni player iPhone",
  "offline FLAC player Mac", "upravitelj glazbene biblioteke", "uređivač audio oznaka",
  "CarPlay FLAC player", "Chromecast audio aplikacija", "AirPlay 2 glazba",
  "Flacbox widgeti", "Flacbox CarPlay", "FFmpeg glazbeni player iOS",
  "audioknjiga player iPhone", "audio oznake iOS", "aplikacija za korekciju visine tona",
  "audio izlazna frekvencija uzorkovanja", "vanjski DAC iPhone", "USB DAC Mac",
  "Synology glazbena aplikacija", "QNAP glazbena aplikacija", "NAS glazbeni player iPhone",
  "WebDAV glazbeni player", "SMB glazbeni streaming", "DLNA glazbeni player",
  "iCloud Drive glazba", "Google Drive FLAC", "Dropbox FLAC player",
  "Wi-Fi Drive glazbeni prijenos", "uvoz M3U popisa pjesama", "Last.fm scrobbling"
]
tags: ["flacbox", "vodič", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widgeti"]
---


### Dobrodošli u Flacbox vodič

Flacbox je visokokvalitetni glazbeni player za iPhone, iPad i Mac koji vam omogućuje da omiljeno cloud pohranjivanje, NAS uređaje i medijske poslužitelje pretvorite u vlastitu osobnu streaming uslugu.

Flacbox se povezuje s iznimno širokim popisom izvora, sve u jednoj aplikaciji:

- **Osobna pohrana u oblaku:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Samostalno hostirani poslužitelji:** Plex · Jellyfin · Emby · Subsonic (i svaki Subsonic-kompatibilni poslužitelj — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (i ownCloud putem zajedničkog API-ja) · Synology Drive · QNAP.
- **NAS i protokoli za dijeljenje datoteka:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (autentifikacija lozinkom ili javnim ključem) · NFS · DLNA / UPnP (reprodukcija i preuzimanje). Radi s Apple Time Capsule, Synology, QNAP, WD My Cloud, bilo kojim Linux Samba / NFS / SSH hostom ili dijeljenom mapom na vašem Mac ili Windows PC računalu.
- **S3-kompatibilna pohrana objekata:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i bilo koja druga S3-API krajnja točka.
- **Otkrivanje na lokalnoj mreži:** Odjeljak Dostupni uređaji automatski navodi svaku Bonjour / mDNS uslugu na vašem Wi-Fi-ju — Plex, Jellyfin, Emby poslužitelji, Synology, QNAP, AirPort usmjerivači s priključenim diskovima, Time Capsule — tako da možete tapnuti za povezivanje bez unošenja IP adrese.

Dok se većina glazbenih aplikacija oslanja na Appleov ugrađeni audio motor, Flacbox pakira **FFmpeg** uz sistemske kodeke kako biste mogli reproducirati formate koje iOS ne podržava izvorno — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, plus uobičajena obitelj MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. U kombinaciji s konfigurabilnom frekvencijom uzorkovanja audio izlaza (44,1 / 48 / 64 / 88,2 / 96 kHz), višekanalnim izlazom (Mono → 5.1 → SDDS → ITU BS.775-1), podešavanjem IO međuspremnika i korekcijom visine tona, Flacbox audiofilu nudi kontrolu koju većina potrošačkih glazbenih aplikacija jednostavno ne pruža.

### Uživajte u glatkom streamingu i offline reprodukciji

Flacbox ima pametno međuspremnivanje za glatko streamanje i ugrađeni upravitelj preuzimanja kako biste mogli preuzeti cijele Popise pjesama, izvođače, albume, mape ili pojedinačne pjesme na uređaj za offline korištenje. Kada ponestane prostora za pohranu, obrišite predmemoriranu datoteke jednim tapom i nastavite streamati iz oblaka. Offline način rada za mape, popise pjesama, albume i izvođače također automatski sinkronizira nove pjesme čim se pojave u oblaku, tako da vaša offline kolekcija uvijek ostaje aktualna.

### Automatski organizirana glazbena biblioteka

Kada uvozite audio pjesme, Flacbox skenira njihove metapodatke i organizira ih u čistu glazbenu biblioteku — grupirane po Pjesmama, Nepuštenim pjesmama, Albumima, Izvođačima albuma, Izvođačima, Žanrovima i Skladateljima. Koristite ugrađenu pretragu za pronalaženje bilo čega za nekoliko sekundi, filtrirajte prema izvoru (online cloud / offline / uređaj) i birajte između Plain / Grupirani / Tabbed izgleda biblioteke. Za biblioteke s mješovitim kompilacijama 'raznih izvođača', Flacbox pruža namjenske prikaze Svi albumi / Ekskluzivni albumi / Solo albumi.

### Popravite metapodatke i označite glazbu

Ako naiđete na oštećene oznake ili neuredna kodiranja (uobičajena neugodnost za ripane ili starije datoteke), ugrađeni uređivač ID3 oznaka može ih očistiti — ručno ili automatskim MusicBrainz pretragama. Možete i normalizirati pokvarena znakovana kodiranja (odlično za ćirilična, japanska ili kineska oznake s Windows PC-ja), tražiti nedostajuće omote albuma i automatski upisati promjene natrag u originalnu datoteku u oblaku. Za dublje grupno uređivanje, instalirajte našu pratnju aplikaciju Evertag.

### Lako prenošenje s Mac, PC ili NAS uređaja

Premještajte glazbu između računala i iPhonea ili iPada s bilo kojim od ovih alata: SMB, WebDAV, DLNA, Wi-Fi Drive (povuci i ispusti u bilo kojem desktop pregledniku), iTunes / Finder File Sharing putem Lightning ili USB-C kabela, USB Flash diskovi ili iXpand Flash diskovi. Imate li Apple Time Capsule, WD My Cloud, Synology, QNAP ili bilo koji drugi NAS koji izlaže SMB / WebDAV / DLNA / FTP / SFTP? Povežite ga jednom i streamajte cijelu biblioteku bez zauzimanja prostora na uređaju.

### Prilagodite zvuk s ekvilajzerom

Flacbox uključuje 10-pojasni ekvilajzer s iPod-style predefiniranim postavkama (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz i još mnogo toga), predpojačalo i mogućnost čuvanja vlastitih predefiniranih postavki. Bilo da podešavate za par audiofil IEM slušalica, HomePod mini ili auto stereo, možete oblikovati zvuk točno onako kako vam odgovara.

### Prilagođeno za audioknjige

Flacbox je odličan player za audioknjige — više oznaka po pjesmi, precizna brzina reprodukcije (0,02× do 3,00×), nastavak reprodukcije točno gdje ste stali, prilagodljivi gumbi za preskakanje i tajmer spavanja koji se nježno utišava pri odlasku na spavanje. M4B oznake poglavlja i duge datoteke u potpunosti su podržane.

### Streamajte bilo gdje — uključujući auto i početni zaslon

Streamajte glazbu na Apple TV / HomePod putem AirPlay 2, pošaljite je na Google Chromecast zvučnike i televizore s Castom, i ponesite sve na put s Apple CarPlayem. Koristite widgete početnog zaslona na iPhoneu i iPadu za jednogledi pogled na trenutnu pjesmu i Last.fm scrobbling za čuvanje povijesti slušanja kroz aplikacije.

### Privatnost i sigurnost

Flacbox koristi samo službene SDK-ove i OAuth prijave svakog davatelja cloud usluga — vaša lozinka nikada ne dospijeva do aplikacije. Pristupni tokeni žive šifrirani u iOS Keychainu, svi prijenosi su zaštićeni TLS-om, a opoziv pristupa u cloud računu ili uklanjanje Flacboxa s uređaja trenutačno briše sve. Zaštitite biblioteku opcijskim kodom pristupa za dodatni sloj privatnosti.

### Početak rada s Flacboxom

Ovaj vodič provodi vas kroz svaki dio Flacboxa na iPhoneu, iPadu i Macu — od povezivanja cloud usluga, organizacije biblioteke, prijenosa datoteka i upravljanja popisima pjesama, do finog podešavanja ekvilajzera i konfiguriranja audio motora. Koristite kartice ispod za skok izravno na odjeljak koji vam treba.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigacija" subtitle="Traka kartica na iPhoneu, lijevi izbornik na iPadu i Macu, mini player, widgeti, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Povezivanja" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Glazbena biblioteka" subtitle="Pjesme, albumi, izvođači, žanrovi, skladatelji — sinkronizacija, pretraga, uređivanje metapodataka." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Popisi pjesama" subtitle="Izgradite, uvezite M3U / M3U8 / CUE, promijenite redoslijed i izvezite u M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Lokalne datoteke" subtitle="Offline glazba, USB diskovi, Wi-Fi Drive, upravitelj datoteka, offline mape." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Audio player" subtitle="Hi-res izlaz, ekvilajzer, visina tona, oznake, AirPlay, Chromecast, brzina, tajmer spavanja." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Postavke" subtitle="Audio motor, biblioteka, upravitelj datoteka, CarPlay, widgeti, personalizacija, jezik, sigurnosna kopija." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="Česta pitanja" subtitle="Pronađite odgovore na 50 najčešćih pitanja o Flacboxu." >}}

{{< /cards >}}
