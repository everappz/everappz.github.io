---
date: 2020-01-01
title: 'Flacbox'
description: 'Lär dig använda Flacbox — hi-res FLAC-, DSD-, ALAC- och FFmpeg-driven molnmusikspelare för iPhone, iPad och Mac. Anslut iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB och DLNA. Strömma och ladda ner högupplöst ljud, redigera metadata, lyssna på ljudböcker, scrobble till Last.fm, använd Apple CarPlay och hemskärmswidgetar och anpassa 10-bands equalizern.'
keywords: [
  "Flacbox användarguide", "Flacbox hur man gör", "hi-res musikspelare iPhone", "FLAC-spelare iPhone",
  "DSD-spelare iOS", "ALAC-spelare Mac", "förlustfri musikapp", "molnmusikspelare iPhone",
  "offline FLAC-spelare Mac", "musikbibliotekshanterare", "ljudtaggsredigerare",
  "CarPlay FLAC-spelare", "Chromecast ljudapp", "AirPlay 2 musik",
  "Flacbox widgetar", "Flacbox CarPlay", "FFmpeg musikspelare iOS",
  "ljudboksspelare iPhone", "ljudbokmärken iOS", "tonhöjdskorrigering musikapp",
  "samplingsfrekvens för ljudutgång", "extern DAC iPhone", "USB DAC Mac",
  "Synology musikapp", "QNAP musikapp", "NAS musikspelare iPhone",
  "WebDAV musikspelare", "SMB musikströmning", "DLNA musikspelare",
  "iCloud Drive musik", "Google Drive FLAC", "Dropbox FLAC-spelare",
  "Wi-Fi Drive musiköverföring", "M3U spellisteimport", "Last.fm scrobbling"
]
tags: ["flacbox", "guide", "hi-res", "FLAC", "FFmpeg", "moln", "CarPlay", "widgetar"]
---


### Välkommen till Flacbox-guiden

Flacbox är en högupplöst musikspelare för iPhone, iPad och Mac som låter dig förvandla din favoritmolnlagring, NAS och medieservrar till din egen personliga streamingtjänst.

Flacbox ansluter till en remarkabelt bred lista med källor, allt i en app:

- **Personlig molnlagring:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Självhostade servrar:** Plex · Jellyfin · Emby · Subsonic (och alla Subsonic-kompatibla servrar — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (och ownCloud via det delade API:et) · Synology Drive · QNAP.
- **NAS och fildelningsprotokoll:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (lösenord eller autentisering med offentlig nyckel) · NFS · DLNA / UPnP (uppspelning och nedladdning). Fungerar med Apple Time Capsule, Synology, QNAP, WD My Cloud, alla Linux Samba / NFS / SSH-värdar eller en delad mapp på din Mac eller Windows PC.
- **S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces och alla andra S3-API-slutpunkter.
- **Lokalt nätverksupptäckt:** Avsnittet Tillgängliga enheter listar automatiskt varje Bonjour / mDNS-tjänst på ditt Wi-Fi — Plex, Jellyfin, Emby-servrar, Synology, QNAP, AirPort-routrar med anslutna enheter, Time Capsule — så att du kan trycka för att ansluta utan att skriva en IP-adress.

Medan de flesta musikappar håller sig till Apples inbyggda ljudmotor, paketerar Flacbox **FFmpeg** bredvid systemkodekarna så att du kan spela format som iOS inte stöder — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, plus den vanliga MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC-familjen. I kombination med en konfigurerbar samplingsfrekvens för ljudutgång (44,1 / 48 / 64 / 88,2 / 96 kHz), flerkanalsutgång (Mono → 5.1 → SDDS → ITU BS.775-1), IO-bufferjustering och tonhöjdskorrigering, ger Flacbox audiofiler kontroll som de flesta konsumentmusikapplikationer helt enkelt inte erbjuder.

### Njut av smidig strömning och offline-uppspelning

Flacbox har smart buffring för smidig strömning och en inbyggd nedladdningshanterare så att du kan hämta hela spellistor, artister, album, mappar eller enskilda spår till din enhet för offline-användning. När du har ont om lagringsutrymme rensar du cachade filer med ett tryck och fortsätter att strömma från molnet. Offline-läge för mappar, spellistor, album och artister synkroniserar också automatiskt nya spår i det ögonblick de visas i molnet, så din offline-samling håller sig alltid aktuell.

### Automatiskt organiserat musikbibliotek

När du importerar ljudspår skannar Flacbox deras metadata och organiserar dem i ett rent musikbibliotek — grupperade efter Låtar, Ospelade låtar, Album, Albumartister, Artister, Genrer och Kompositörer. Använd den inbyggda sökningen för att hitta vad som helst på sekunder, filtrera efter källa (online-moln / offline / enhet) och välj mellan Plain / Grouped / Tabbed bibliotekarslayouter. För bibliotek med blandade "various artists"-kompilationer tillhandahåller Flacbox dedikerade vyer för Alla album / Exklusiva album / Soloalbum för att visa rätt resultat utan brus.

### Fixa metadata och tagga din musik

Om du stöter på korrupta taggar eller röriga kodningar (ett vanligt problem med rippade eller äldre filer), kan den inbyggda ID3-taggsredigeraren städa upp dem — manuellt eller med automatiska MusicBrainz-sökningar. Du kan också normalisera trasig teckenkodning (bra för kyrilliska, japanska eller kinesiska taggar som kom från Windows-datorer), söka efter saknade albumomslag och skriva ändringar tillbaka till originalfilen i molnet automatiskt. För djupare batchredigering, installera vår följeapp Evertag.

### Enkla överföringar från Mac, PC eller NAS

Flytta musik mellan din dator och din iPhone eller iPad med något av dessa verktyg: SMB, WebDAV, DLNA, Wi-Fi Drive (dra och släpp i valfri skrivbordswebbläsare), iTunes / Finder File Sharing via Lightning- eller USB-C-kabel, USB-flashenheter eller iXpand Flash Drives. Har du en Apple Time Capsule, WD My Cloud, Synology, QNAP eller annan NAS som exponerar SMB / WebDAV / DLNA / FTP / SFTP? Anslut en gång och strömma hela ditt bibliotek utan att ta upp enhetens lagringsutrymme.

### Anpassa ditt ljud med equalizern

Flacbox inkluderar en 10-bands equalizer med iPod-liknande förinställningar (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz och många fler), en förförstärkare och möjligheten att spara egna förinställningar. Oavsett om du ställer in för ett par audiofila IEM, en HomePod mini eller ett bilstereo, kan du forma ljudet precis som du vill ha det.

### Vänlig för ljudböcker

Flacbox är en utmärkt ljudboksspelare — flera bokmärken per spår, finkornad uppspelningshastighet (0,02× till 3,00×), fortsätt uppspelning för att återuppta exakt där du slutade, anpassningsbara snabbhopp-knappar och en sovtimer som tonar ut mjukt vid sänggåendet. M4B-kapitelmarkörer och långa filer stöds fullt ut.

### Strömma var som helst — inklusive din bil och hemskärm

Strömma musik till Apple TV / HomePod via AirPlay 2, skicka den till Google Chromecast-högtalare och Cast-aktiverade TV-apparater och ta med allt på vägen med Apple CarPlay. Använd hemskärmswidgetar på iPhone och iPad för att se det aktuellt spelande spåret på en blick och Last.fm scrobbling för att hålla din lyssnhistorik med dig i alla appar.

### Integritet och säkerhet

Flacbox använder endast officiella SDK:er och OAuth-baserade inloggningar från varje molnleverantör — ditt lösenord når aldrig appen. Åtkomsttokens lagras krypterade i iOS Keychain, alla överföringar är TLS-skyddade och återkallelse av åtkomst i ditt molnkonto eller borttagning av Flacbox från enheten tar bort allt omedelbart. Skydda ditt bibliotek med en valfri lösenkod för ett extra lager av integritet.

### Komma igång med Flacbox

Denna guide går igenom varje del av Flacbox på iPhone, iPad och Mac — från att ansluta molntjänster, organisera ditt bibliotek, överföra filer och hantera spellistor, till att finjustera equalizern och konfigurera ljudmotorn. Använd korten nedan för att hoppa direkt till den sektion du behöver.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigering" subtitle="Flikfältet på iPhone, vänster meny på iPad och Mac, minispelare, widgetar, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Anslutningar" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Musikbibliotek" subtitle="Låtar, album, artister, genrer, kompositörer — synkronisering, sökning, redigering av metadata." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Spellistor" subtitle="Bygg, importera M3U / M3U8 / CUE, ordna om och exportera till M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Lokala filer" subtitle="Offline-musik, USB-enheter, Wi-Fi Drive, filhanterare, offline-mappar." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Ljudspelaren" subtitle="Hi-res-utgång, equalizer, tonhöjd, bokmärken, AirPlay, Chromecast, hastighet, sovtimer." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Inställningar" subtitle="Ljudmotor, bibliotek, filhanterare, CarPlay, widgetar, personalisering, språk, säkerhetskopiering." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Hitta svar på de 50 vanligaste frågorna om Flacbox." >}}

{{< /cards >}}
