---
title: "Evermusic"
date: 2020-01-01
description: "Evermusic — den kraftfulla molnmusikspelaren och bibliotekshanteraren för iPhone, iPad och Mac. Strömma från Google Drive, Dropbox, iCloud, OneDrive, MEGA, Synology, pCloud, Plex, Jellyfin, Subsonic, Navidrome eller valfri NAS via SMB / WebDAV / FTP / SFTP. Redigera ID3- och FLAC-taggar, organisera efter artist / album / genre, spela offline, använd 10-bands equalizer, crossfade, gapless, spatial audio, sömntimer, CarPlay, AirPlay 2, Google Cast, ljudbokmärken, Last.fm-scrobbling och låsskärmswidgetar."
keywords: [
  "Evermusic", "Evermusic Pro", "Evermusic iPhone", "Evermusic iPad", "Evermusic Mac",
  "molnmusikspelare", "FLAC-spelare iOS", "DSD-spelare", "hi-res audio iPhone",
  "strömma musik Google Drive", "strömma musik Dropbox", "strömma musik iCloud Drive",
  "strömma musik OneDrive", "strömma musik MEGA", "Synology musikspelare", "pCloud musikspelare",
  "Plex musikklient", "Jellyfin musikspelare", "Emby musikklient",
  "Subsonic klient iPhone", "Navidrome klient iPhone", "Nextcloud musikspelare",
  "NAS musikströmning", "SMB musikspelare iPhone", "WebDAV ljudspelare",
  "FTP musikspelare iPhone", "SFTP musikspelare", "S3 musikspelare",
  "10-bands equalizer", "crossfade uppspelning", "gapless uppspelning", "spatial audio",
  "ljudbokmärken för ljudböcker", "offline musikapp", "musikbibliotek iPhone", "ID3-taggeditor",
  "M3U-spellistaimport", "CSV TXT-spellistaexport", "Apple CarPlay musikspelare",
  "AirPlay 2", "Google Cast Chromecast musik", "Last.fm scrobbling", "låsskärmswidgetar"
]
tags: ["evermusic", "guide"]
readingTime: 4
---


Evermusic är en kraftfull molnmusikspelare och bibliotekshanterare som förvandlar din iPhone, iPad eller Mac till ett komplett strömmande och offline musiksystem. Den fungerar med de molnkonton och NAS du redan äger, spelar praktiskt taget alla ljudformat som din enhet kan avkoda, och ger dig en avancerad ljudmotor (10-bands equalizer, crossfade, gapless, spatial audio, tonhöjdskorrigering) ovanpå det.

Tillgänglig i två utgåvor: Evermusic (gratis, med annonser) och Evermusic Pro (betald, inga annonser, fullständig funktionsuppsättning). Livstids-, månads- och årsbaserade premiumplaner i gratisutgåvan låser upp samma funktionsuppsättning; båda utgåvorna delar köp mellan iOS och Mac via iCloud och Family Sharing.

### Din musik överallt

Evermusic låter dig bygga ditt eget molnbaserade musikströmningssystem — precis som Spotify, men utan några begränsningar. Anslut valfri kombination av källor och strömma eller ladda ner låtar på begäran:

- **Personliga molnkonton:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Självhostade servrar och mediebibliotek:** Plex · Jellyfin · Emby · Subsonic (och alla Subsonic-kompatibla servrar — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (och Owncloud, via det delade API:et) · Synology Drive · QNAP.
- **NAS och fildelningsprotokoll:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (SSH File Transfer Protocol, lösenord eller autentisering med offentlig nyckel) · NFS · DLNA / UPnP (uppspelning och nedladdning). Fungerar med Apple Time Capsule, Synology, QNAP, WD My Cloud Home, Buffalo, vilken Linux Samba / NFS / SSH-värd som helst, eller en delad mapp på din Mac eller Windows-PC.
- **S3-kompatibel objektlagring:** AWS S3 · Backblaze B2 · Wasabi · Cloudflare R2 · MinIO · DigitalOcean Spaces · Linode Object Storage · IBM Cloud Object Storage · valfri S3-API-slutpunkt.
- **Lokal nätverksupptäckt:** avsnittet Tillgängliga enheter listar automatiskt alla Bonjour / mDNS-enheter på ditt Wi-Fi — Plex, Jellyfin, Emby-servrar, Synology, QNAP, AirPort-routrar med anslutna enheter, Time Capsule — så att du kan ansluta med ett tryck utan att skriva en IP-adress.
- **Enhet och externa källor:** iPod / Apple Music-biblioteket (spår utan DRM), filer i systemappen Filer (andra appar, externa SSD:er, monterade mappar), USB-flashenheter via Apple Certified kortläsare och iXpand Flash Drives, Wi-Fi Drive (dra och släpp i en skrivbordswebbläsare) och iTunes / Finder-fildelning via USB-kabel.

Det är 30+ källtyper i en app. När din musik finns i molnet kan du spela den var som helst, när som helst, med samma bibliotek på alla enheter. Säkerhetskopiering och återställning låter dig ta en ögonblicksbild av hela biblioteket till en enda fil och importera den på en annan iPhone, iPad eller Mac på några sekunder.

### Smidig uppspelning

Evermusic använder smart förinläsning och en konfigurerbar uppspelningscache för att låtar ska spela smidigt även över långsamma anslutningar. Smart strömning använder AVAssetResourceLoader så att uppspelningen startar omedelbart medan resten av filen laddas ner i bakgrunden. Du kan också ladda ner album, artister, spellistor eller enskilda låtar för att lyssna offline — och om lagringen tar slut, ta helt enkelt bort cachade filer och fortsätt strömma från molnet.

### Enkel musiksortering

När du lägger till låtar i Evermusic läser bakgrundsmetadataläsaren varje fil och bygger ett rent musikbibliotek sorterat efter Låtar, Ospelade låtar, Album, Albumartister, Artister, Genrer och Kompositörer. Album har tre undervyer: Alla album, Exklusiva album och Soloalbum så att kompilationer och lika namngivna album av olika artister inte kolliderar.

### Fixa låtinformation enkelt

Om låttitlar eller albuminfo är fel eller saknas, oroa dig inte. Evermusic innehåller en inbyggd taggeditor som låter dig fixa metadata på några sekunder. Du kan uppdatera titel, artist, album, albumartist, år, genre och albumomslag, plus normalisera trasiga kodningar (kyrillisk eller asiatisk text som visas förvrängd) med ett tryck. Editorn använder MusicBrainz för att automatiskt hitta saknade taggar och albumomslag.

### Enkla filöverföringar

Att skicka musik från din dator till din iPhone eller iPad är enkelt. Evermusic stöder SMB, WebDAV, FTP / FTPS, SFTP, NFS, DLNA, Wi-Fi Drive (dra och släpp i en webbläsare), iTunes / Finder-fildelning (USB-kabel) och direktnedladdningar från valfritt anslutet molnkonto. Du kan också ansluta Apple Time Capsule, WD My Cloud Home, Synology, QNAP, Buffalo eller annan NAS som exponerar ett av dessa standardprotokoll, utan att använda enhetens lagringsutrymme.

### Kraftfulla ljudkontroller

Evermusic inkluderar en fullständig 10-bands ljudequalizer med iPod-liknande förinställningar (Acoustic, Bass Booster, Classical, Dance, Electronic, Flat, Hip-Hop, Jazz, Latin, Loudness, Lounge, Piano, Pop, R&B, Rock, Small Speakers, Spoken Word, Treble Booster, Vocal Booster), en förförstärkare för tysta låtar, exporterbara och importerbara anpassade förinställningar och RMS-baserad volymberäkning. Lägg till crossfade-uppspelning (1–15 sek), gapless-uppspelning, spatial audio, tonhöjdskorrigering och CoreAudio-utmatning upp till 384 kHz mono eller stereo, och du kan finjustera ljudet precis som du vill ha det.

### Utmärkt för ljudböcker

Om du lyssnar på ljudböcker, poddar eller inspelade föreläsningar är Evermusic perfekt. Du kan lägga till flera bokmärken per spår, automatiskt återuppta från den senaste positionen, ändra uppspelningshastigheten från 0,02× till 3× (med ett precisionsskjutreglage), ställa in en sömntimer med anpassade intervall och visa kommentarer, inbäddade texter och LRC-filer på samma skärm.

### Fungerar överallt

Du är inte begränsad till din telefon eller surfplatta. Evermusic fungerar även med Apple CarPlay (endast iOS, optimerad för bilgränssnittet), AirPlay 2 (strömma till flera högtalare samtidigt), Google Cast / Chromecast, låsskärmswidgetar, Now Playing-kontroller, Last.fm-scrobbling (skicka automatiskt uppspelning till ditt Last.fm-konto för statistik och rekommendationer) och Mac-tangentbordsgenvägar. Oavsett om du är hemma, i bilen eller reser är din musik alltid med dig.

### Kom igång med Evermusic

Den här guiden hjälper dig att få ut det mesta av Evermusic på din iPhone, iPad eller Mac. Lär dig att strömma musik från molnet, organisera ett bibliotek som lever på din egen lagring, hantera spellistor och offlinemappar, finjustera ljudmotorn och lyssna på ljudböcker. Evermusic ger dig full kontroll över din musiksamling i en enkel app.<br><br>


{{< cards >}}
  {{< card icon="location-marker" title="Navigering" subtitle="Lär dig navigera i Evermusic med hjälp av flikfältet på iPhone eller vänstermenyn på iPad och Mac." link="/docs/guide/evermusic/evermusic-guide-navigation" >}}

  {{< card icon="cloud" title="Anslutningar" subtitle="Anslut dina molnkonton och hantera onlinefiler med den inbyggda filhanteraren." link="/docs/guide/evermusic/evermusic-guide-connections" >}}

  {{< card icon="collection" title="Musikbibliotek" subtitle="Organisera och utforska dina spår, album och artister i musikbiblioteket." link="/docs/guide/evermusic/evermusic-guide-music-library" >}}

  {{< card icon="music-note" title="Spellistor" subtitle="Skapa och arrangera spellistor som passar ditt humör eller tillfälle." link="/docs/guide/evermusic/evermusic-guide-playlists" >}}

  {{< card icon="folder" title="Lokala filer" subtitle="Öppna och hantera offlinemusik via avsnittet Lokala filer." link="/docs/guide/evermusic/evermusic-guide-local-files" >}}

  {{< card icon="play" title="Musikspelare" subtitle="Styr uppspelning, kö och ljudinställningar som equalizer och sömntimer." link="/docs/guide/evermusic/evermusic-guide-player" >}}

  {{< card icon="adjustments" title="Inställningar" subtitle="Anpassa Evermusics utseende, funktioner och prestandainställningar." link="/docs/guide/evermusic/evermusic-guide-settings" >}}

  {{< card icon="question-mark-circle" title="FAQ" subtitle="Hitta snabba svar på vanliga frågor i vår FAQ-sektion." link="/docs/faq/evermusic" >}}
{{< /cards >}}
