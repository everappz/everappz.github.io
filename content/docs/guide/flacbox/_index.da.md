---
date: 2020-01-01
title: 'Flacbox'
description: 'Lær at bruge Flacbox — den hi-res cloud-musikafspiller med understøttelse af FLAC, DSD, ALAC og FFmpeg til iPhone, iPad og Mac. Tilslut iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB og DLNA. Stream og download højtopløsningslyd, rediger metadata, lyt til lydbøger, scrobble til Last.fm, brug Apple CarPlay og startskærmswidgets, og tilpas den 10-bånds equalizer.'
keywords: [
  "Flacbox brugervejledning", "Flacbox hvordan", "hi-res musikafspiller iPhone", "FLAC afspiller iPhone",
  "DSD afspiller iOS", "ALAC afspiller Mac", "app til lossless musik", "cloud musikafspiller iPhone",
  "offline FLAC afspiller Mac", "musikbiblioteksmanager", "lydtags-editor",
  "FLAC afspiller CarPlay", "Chromecast lydapp", "AirPlay 2 musik",
  "Flacbox widgets", "Flacbox CarPlay", "FFmpeg musikafspiller iOS",
  "lydbogafspiller iPhone", "lyd-bogmærker iOS", "app til tonehøjdekorrektion",
  "lydoutput samplingshastighed", "ekstern DAC iPhone", "USB DAC Mac",
  "Synology musikapp", "QNAP musikapp", "NAS musikafspiller iPhone",
  "WebDAV musikafspiller", "SMB musikstreaming", "DLNA musikafspiller",
  "iCloud Drive musik", "Google Drive FLAC", "Dropbox FLAC afspiller",
  "Wi-Fi Drive musikoverførsel", "M3U spilleliste import", "Last.fm scrobbling"
]
tags: ["flacbox", "vejledning", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widgets"]
---


### Velkommen til Flacbox-vejledningen

Flacbox er en hi-res musikafspiller til iPhone, iPad og Mac, der lader dig omdanne din foretrukne cloud-lagring, NAS og medieservere til din egen personlige streamingtjeneste.

Flacbox forbinder til en bemærkelsesværdig bred liste af kilder, alt i én app:

- **Personlig cloud-lagring:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Selvhostede servere:** Plex · Jellyfin · Emby · Subsonic (og alle Subsonic-kompatible servere — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (og ownCloud via den delte API) · Synology Drive · QNAP.
- **NAS og fildelningsprotokoller:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (adgangskode eller offentlig nøgle-godkendelse) · NFS · DLNA / UPnP (afspilning og download). Fungerer med Apple Time Capsule, Synology, QNAP, WD My Cloud, enhver Linux Samba / NFS / SSH-vært, eller en delt mappe på din Mac eller Windows PC.
- **S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og ethvert andet S3-API-endpoint.
- **Opdagelse på lokalt netværk:** Sektionen Tilgængelige enheder viser automatisk alle Bonjour / mDNS-tjenester på dit Wi-Fi — Plex, Jellyfin, Emby-servere, Synology, QNAP, AirPort-routere med tilsluttede drev, Time Capsule — så du kan trykke for at forbinde uden at skrive en IP-adresse.

Mens de fleste musikapps holder sig til Apples indbyggede lydmotor, inkluderer Flacbox **FFmpeg** ved siden af systemkodecs, så du kan afspille formater som iOS ikke understøtter som standard — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, samt den almindelige MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC-familie. Kombineret med en konfigurerbar lydoutput-samplingshastighed (44,1 / 48 / 64 / 88,2 / 96 kHz), flerkanalsoutput (Mono → 5.1 → SDDS → ITU BS.775-1), IO-bufferjustering og tonehøjdekorrektion giver Flacbox audiofiler den kontrol, som de fleste forbrugermusikapper simpelthen ikke tilbyder.

### Nyd Jævn Streaming og Offline Afspilning

Flacbox har smart buffering til jævn streaming og en indbygget downloadmanager, så du kan hente hele spillelister, artister, album, mapper eller individuelle numre til dit enhed til offline brug. Når lagerpladsen er lav, ryd cachelagrede filer med ét tryk og fortsæt med at streame fra skyen. Offline-tilstand for mapper, spillelister, album og artister synkroniserer også automatisk nye numre i det øjeblik, de vises i skyen, så din offline-samling altid er opdateret.

### Automatisk Organiseret Musikbibliotek

Når du importerer lydspor, scanner Flacbox deres metadata og organiserer dem i et overskueligt musikbibliotek — grupperet efter Sange, Ikke-afspillede sange, Album, Albumkunstnere, Kunstnere, Genrer og Komponister. Brug den indbyggede søgning til at finde noget på få sekunder, filtrer efter kilde (online sky / offline / enhed), og vælg mellem Simple / Grupperet / Fanebladet bibliotekslayout. For biblioteker med blandede 'diverse artister'-kompilationer tilbyder Flacbox dedikerede visninger Alle album / Eksklusive album / Solo-album for at vise de rigtige resultater uden støj.

### Ret Metadata og Taggé Din Musik

Hvis du støder på beskadigede tags eller rodet kodning (en almindelig hovedpine for rippede eller ældre filer), kan den indbyggede ID3-tags-editor rydde op — manuelt eller med automatiske MusicBrainz-opslag. Du kan også normalisere ødelagte tegnkodninger (fantastisk til kyrilliske, japanske eller kinesiske tags fra Windows-pc'er), søge efter manglende albumcovers og automatisk skrive ændringer tilbage til den originale fil i skyen. Til dybere batchredigering, installer vores ledsagende app Evertag.

### Nemme Overførsler fra Mac, PC eller NAS

Flyt musik mellem din computer og din iPhone eller iPad med et af disse værktøjer: SMB, WebDAV, DLNA, Wi-Fi Drive (træk og slip i enhver desktopbrowser), iTunes / Finder fildelingvia et Lightning eller USB-C-kabel, USB-flashdrev eller iXpand Flash Drives. Har du en Apple Time Capsule, WD My Cloud, Synology, QNAP eller en anden NAS, der eksponerer SMB / WebDAV / DLNA / FTP / SFTP? Tilslut én gang og stream hele dit bibliotek uden at optage nogen enhedslagring.

### Tilpas Din Lyd med Equalizeren

Flacbox inkluderer en 10-bånds equalizer med iPod-stil forudindstillinger (Akustisk, Basbooster, Klassisk, Dance, Rock, Pop, Jazz og mange flere), en forforstærker og muligheden for at gemme dine egne forudindstillinger. Hvad enten du tuner til et par audiofil-IEMs, en HomePod mini eller et bilanlæg, kan du forme lyden præcis, som du kan lide det.

### Venlig over for Lydbøger

Flacbox er en fremragende lydbogafspiller — flere bogmærker per spor, finkornet afspilningshastighed (0,02× til 3,00×), fortsæt afspilning for at genoptage præcis der, hvor du stoppede, tilpassede spring-tid-knapper og en sove-timer, der dæmper lydene blidt ved sengetid. M4B-kapitelmarkører og lange filer understøttes fuldt ud.

### Stream Overalt — Inklusive Din Bil og Startskærm

Stream musik til Apple TV / HomePod via AirPlay 2, send det til Google Chromecast-højttalere og Cast-aktiverede TV'er, og tag alt på vejen med Apple CarPlay. Brug startskærmswidgets på iPhone og iPad for at se det aktuelle nummer på et øjeblik, og Last.fm scrobbling for at holde din lyttehistorik med dig på tværs af apps.

### Privatliv og Sikkerhed

Flacbox bruger kun officielle SDK'er og OAuth-baserede logins fra hver cloud-udbyder — din adgangskode når aldrig frem til appen. Adgangstokens gemmes krypteret i iOS Keychain, alle overførsler er TLS-beskyttede, og tilbagekaldelse af adgang i din cloudkonto eller fjernelse af Flacbox fra enheden sletter alt øjeblikkeligt. Beskyt dit bibliotek med en valgfri adgangskode for et ekstra lag af privatliv.

### Kom i Gang med Flacbox

Denne vejledning guider dig gennem hver del af Flacbox på iPhone, iPad og Mac — fra at forbinde cloud-tjenester, organisere dit bibliotek, overføre filer og administrere spillelister, til at finjustere equalizeren og konfigurere lydmotoren. Brug kortene nedenfor til at hoppe direkte til den sektion, du har brug for.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigation" subtitle="Fanebladslinje på iPhone, Venstremenu på iPad og Mac, mini-afspiller, widgets, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Forbindelser" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Musikbibliotek" subtitle="Sange, Album, Kunstnere, Genrer, Komponister — synkroniser, søg, rediger metadata." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Afspilningslister" subtitle="Byg, importer M3U / M3U8 / CUE, omarranger og eksporter til M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Lokale filer" subtitle="Offline musik, USB-drev, Wi-Fi Drive, filmanager, offline mapper." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Lydafspiller" subtitle="Hi-res output, equalizer, tonehøjde, bogmærker, AirPlay, Chromecast, hastighed, sove-timer." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Indstillinger" subtitle="Lydmotor, bibliotek, filmanager, CarPlay, widgets, personalisering, sprog, sikkerhedskopiering." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="Ofte stillede spørgsmål" subtitle="Find svar på de 50 mest almindelige spørgsmål om Flacbox." >}}

{{< /cards >}}
