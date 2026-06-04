---
date: 2020-01-01
title: 'Flacbox'
description: 'Lær hvordan du bruker Flacbox — hi-res FLAC, DSD, ALAC og FFmpeg-drevet skymusikkspiller for iPhone, iPad og Mac. Koble til iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB og DLNA. Strøm og last ned høyoppløsningslyd, rediger metadata, lytt til lydbøker, scroble til Last.fm, bruk Apple CarPlay og hjemskjerm-widgets, og tilpass 10-bands equalizeren.'
keywords: [
  "Flacbox brukerveiledning", "Flacbox hvordan", "hi-res musikk iPhone", "FLAC-spiller iPhone",
  "DSD-spiller iOS", "ALAC-spiller Mac", "tapsfri musikk-app", "skymusikkspiller iPhone",
  "offline FLAC-spiller Mac", "musikkbibliotekbehandler", "lydtaggredaktør",
  "CarPlay FLAC-spiller", "Chromecast lyd-app", "AirPlay 2 musikk",
  "Flacbox widgets", "Flacbox CarPlay", "FFmpeg musikk iOS",
  "lydbokspiller iPhone", "lydbokmerker iOS", "tonehøydekorreksjon musikk-app",
  "lydutsamplingshastighet", "ekstern DAC iPhone", "USB DAC Mac",
  "Synology musikk-app", "QNAP musikk-app", "NAS musikk iPhone",
  "WebDAV musikk", "SMB musikkstrøm", "DLNA musikk",
  "iCloud Drive musikk", "Google Drive FLAC", "Dropbox FLAC-spiller",
  "Wi-Fi Drive musikkoverføring", "M3U spilleliste import", "Last.fm scrobbling"
]
tags: ["flacbox", "guide", "hi-res", "FLAC", "FFmpeg", "sky", "CarPlay", "widgets"]
---


### Velkommen til Flacbox-guiden

Flacbox er en høyoppløsningsmusikkspiller for iPhone, iPad og Mac som lar deg gjøre din favoritt-skylagring, NAS og medieservere om til din egen personlige strømmingstjeneste.

Flacbox kobler til et bemerkelsesverdig bredt utvalg av kilder, alt i én app:

- **Personlig skylagring:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Selvhostede servere:** Plex · Jellyfin · Emby · Subsonic (og alle Subsonic-kompatible servere — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (og ownCloud via det delte API-et) · Synology Drive · QNAP.
- **NAS og fildeling-protokoller:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (passord eller offentlig-nøkkel-autentisering) · NFS · DLNA / UPnP (avspilling og nedlasting). Fungerer med Apple Time Capsule, Synology, QNAP, WD My Cloud, alle Linux Samba / NFS / SSH-verter, eller en delt mappe på din Mac eller Windows-PC.
- **S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og alle andre S3-API-endepunkter.
- **Lokalt nettverksoppdagelse:** Tilgjengelige enheter-seksjonen lister automatisk opp alle Bonjour / mDNS-tjenester på Wi-Fi-nettverket ditt — Plex, Jellyfin, Emby-servere, Synology, QNAP, AirPort-rutere med tilkoblede stasjoner, Time Capsule — slik at du kan trykke for å koble til uten å skrive inn en IP-adresse.

Der de fleste musikk-apper holder seg til Apples innebygde lydmotor, inkluderer Flacbox **FFmpeg** sammen med systemkodekene slik at du kan spille av formater som iOS ikke støtter ut av boksen — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, pluss den vanlige MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC-familien. Kombinert med en konfigurerbar lydutgang-samplingsrate (44,1 / 48 / 64 / 88,2 / 96 kHz), flerkanals utgang (Mono → 5.1 → SDDS → ITU BS.775-1), IO-buffer-justering og tonehøydekorreksjon gir Flacbox audiofil-kontroll som de fleste forbruker-musikk-apper rett og slett ikke tilbyr.

### Nyt Jevn Strømming og Frakoblet Avspilling

Flacbox har smart buffring for jevn strømming og en innebygd nedlastingsbehandler slik at du kan laste ned hele spillelister, artister, album, mapper eller individuelle spor til enheten din for offline bruk. Når du begynner å gå tom for lagringsplass, slett hurtigbufrede filer med ett trykk og fortsett å strømme fra skyen. Frakoblet modus for mapper, spillelister, album og artister synkroniserer også automatisk nye spor i det øyeblikket de vises i skyen, slik at samlingen din alltid er oppdatert.

### Automatisk Organisert Musikkbibliotek

Når du importerer lydspor, skanner Flacbox metadataene og organiserer dem i et oversiktlig musikkbibliotek — gruppert etter Sanger, Uspilte sanger, Album, Albumartister, Artister, Sjangre og Komponister. Bruk den innebygde søkefunksjonen til å finne hva som helst på sekunder, filtrer etter kilde (online sky / frakoblet / enhet) og velg mellom Enkel / Gruppert / Tabbed biblioteksoppsett. For biblioteker med blandede «various artists»-kompillasjoner gir Flacbox dedikerte visninger for Alle album / Eksklusive album / Soloalbum for å vise de riktige resultatene uten støy.

### Fiks Metadata og Tagg Musikken Din

Hvis du støter på ødelagte tagger eller rotete kodinger (et vanlig problem for rippede eller eldre filer), kan den innebygde ID3-taggredigeren rydde dem opp — manuelt eller med automatiske MusicBrainz-oppslag. Du kan også normalisere ødelagte tegnkodinger (flott for kyrilliske, japanske eller kinesiske tagger fra Windows-PC-er), søke etter manglende albumomslagsbilder og skrive endringer tilbake til den originale filen i skyen automatisk. For dypere batchredigering, installer følgeappen vår Evertag.

### Enkle Overføringer fra Mac, PC eller NAS

Flytt musikk mellom datamaskinen og din iPhone eller iPad med et av disse verktøyene: SMB, WebDAV, DLNA, Wi-Fi Drive (dra og slipp i en hvilken som helst skrivebordsnettleser), iTunes / Finder-fildeling over en Lightning- eller USB-C-kabel, USB-minnepinner eller iXpand-minnepinner. Har du en Apple Time Capsule, WD My Cloud, Synology, QNAP eller en annen NAS som støtter SMB / WebDAV / DLNA / FTP / SFTP? Koble til én gang og strøm hele biblioteket ditt uten å bruke enhetens lagringsplass.

### Tilpass Lyden din med Equalizeren

Flacbox inkluderer en 10-bands equalizer med iPod-stil forhåndsinnstillinger (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz og mange flere), en forforsterker og muligheten til å lagre egne forhåndsinnstillinger. Enten du tilpasser for et par audiofil-ørepropper, en HomePod mini eller et bilstereo, kan du forme lyden nøyaktig slik du liker det.

### Lydbokvennlig

Flacbox er en flott lydbokspiller — flere bokmerker per spor, finkornet avspillingshastighet (0,02× til 3,00×), fortsett avspilling for å gjenoppta nøyaktig der du stoppet, tilpassbare hopp-knapper og en soveavtimer som sakte fader ut ved sengetid. M4B-kapittelmerkere og lange filer støttes fullt ut.

### Strøm Overalt — Inkludert Bilen og Hjemskjermen

Strøm musikk til Apple TV / HomePod via AirPlay 2, send det til Google Chromecast-høyttalere og Cast-aktiverte TV-er, og ta alt med på veien med Apple CarPlay. Bruk hjemskjerm-widgets på iPhone og iPad for å se det aktuelle sporet med et blikk, og Last.fm-scrobbling for å holde lyttehistorikken din på tvers av apper.

### Personvern og Sikkerhet

Flacbox bruker kun offisielle SDK-er og OAuth-baserte pålogginger fra hver skyleverandør — passordet ditt når aldri appen. Tilgangstokener er kryptert lagret i iOS Keychain, alle overføringer er TLS-beskyttet, og tilbakekalling av tilgang i skykontoen din eller fjerning av Flacbox fra enheten sletter alt umiddelbart. Beskytt biblioteket ditt med en valgfri passordkode for et ekstra lag med personvern.

### Kom i Gang med Flacbox

Denne guiden tar deg gjennom hver del av Flacbox på iPhone, iPad og Mac — fra tilkobling av skytjenester, organisering av biblioteket, overføring av filer og administrasjon av spillelister, til finjustering av equalizeren og konfigurering av lydmotoren. Bruk kortene nedenfor for å hoppe direkte til den delen du trenger.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigasjon" subtitle="Fane-linje på iPhone, Venstre meny på iPad og Mac, minispiller, widgets, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Tilkoblinger" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Musikkbibliotek" subtitle="Sanger, Album, Artister, Sjangre, Komponister — synkroniser, søk, rediger metadata." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Spillelister" subtitle="Bygg, importer M3U / M3U8 / CUE, omorganiser og eksporter til M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Lokale filer" subtitle="Offline musikk, USB-stasjoner, Wi-Fi Drive, filbehandler, offline mapper." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Lydspiller" subtitle="Hi-res utgang, equalizer, tonehøyde, bokmerker, AirPlay, Chromecast, hastighet, soveavtimer." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Innstillinger" subtitle="Lydmotor, bibliotek, filbehandler, CarPlay, widgets, personalisering, språk, sikkerhetskopiering." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="Vanlige spørsmål" subtitle="Finn svar på de 50 vanligste spørsmålene om Flacbox." >}}

{{< /cards >}}
