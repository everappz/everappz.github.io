---
title: "Filer"
date: 2020-02-01
lastmod: 2026-06-01
description: "Lær hvordan du bruker Filer-fanen i Evervideo på iPhone, iPad og Mac. Koble til skytjenester, NAS-enheter, medieservere og RTSP-strømmer på ett sted. Administrer offline videoer, overføringskøen, nedlastinger, Wi-Fi Drive, iTunes / Finder fildeling og USB-stasjoner. Inkluderer iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA og S3-kompatibel lagring."
keywords: [
  "Evervideo filer", "Evervideo tilkoblinger", "Evervideo lokale filer",
  "sky video oppsett iPhone", "koble til Google Drive video", "SMB videostrømming",
  "WebDAV videospiller iOS", "DLNA video iPhone", "NAS videostrømming",
  "Wi-Fi Drive videooverføring", "Evervideo iTunes fildeling", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo offline modus video", "Evervideo overføringskø",
  "Evervideo filbehandling", "Evervideo Dokumenter mappe",
  "videospiller Synology", "videospiller QNAP",
  "videospiller Apple Time Capsule", "USB DAC video",
  "iXpand videospiller", "S3 videospiller"
]
tags: ["guide", "evervideo", "filer", "tilkoblinger", "sky", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Filer-fanen er Evervideo sin alt-i-ett filbehandler. I motsetning til de fleste video-apper som deler skylagring og lokale filer i separate faner, slår Evervideo begge sammen til én rullbar skjerm slik at du kan gå fra en Plex-server til en skymappe til iPhone-ens Dokumenter-mappe uten å hoppe mellom faner.

Filer-fanen er delt inn i tydelige seksjoner som vises i denne rekkefølgen på skjermen din:

- **Hurtigtilgang** — nylige og favoritter for filer og mapper du åpnet sist.
- **Filer i denne applikasjonen** — det som befinner seg i Evervideo sin sandkasse-Dokumenter-mappe.
- **Filer på denne iPhone / iPad / Mac** — videoer andre steder på enheten din, gjort tilgjengelig gjennom systemfilvelgeren.
- **Skylagring** — alle skykontoer, NAS og medieservere du har koblet til.
- **Tilgjengelige enheter** — servere og stasjoner auto-oppdaget via Bonjour / mDNS på det lokale nettverket ditt.

I øvre høyre hjørne av Filer-skjermen er en Overføringer-knapp (et snurrende piler-ikon). Trykk på den for å åpne Overføringskøen der du overvåker alle nedlastinger og opplastinger på tvers av alle kildene dine.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Filer Across Tilkoblede Lagringsenheter" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Koble til skylagring

Skylagring-seksjonen i Filer-fanen er der alle tilkoblede kontoer, NAS, medieservere og strømmer befinner seg — side om side, i én rullbar liste.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Skylagring Seksjon i Filer-fanen" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Åpne **Filer**-fanen.
- Rull til **Skylagring**-seksjonen.
- Trykk på **Koble til skylagring** fra menyen.
- Velg en skylagringstjeneste fra listen.
- Skriv inn legitimasjonen din på den offisielle autorisasjonssiden levert av skyleverandøren, og trykk deretter på **Ferdig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Koble til en skylagringstjeneste" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Hvis du støter på problemer, sjekk internettforbindelsen og brukernavn / passord. I Premium-versjonen av appen kan du legge til et ubegrenset antall tjenester; gratisversjonen støtter opptil tre.

## Støttede skylagringstjenester, medieservere og protokoller

Evervideo støtter et eksepsjonelt bredt utvalg av kilder for videoene dine. Alt nedenfor fungerer fra én Koble til skylagring-flyt.

**Personlig skylagring:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Selvhostede medieservere:** Plex · Jellyfin · Emby · Subsonic (og alle Subsonic-kompatible servere — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (og ownCloud via den delte API-en) · Synology Drive · QNAP.

**NAS- og fildeleprotokoller:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH-filoverføringsprotokoll, passord eller offentlig nøkkel-godkjenning) · NFS · DLNA / UPnP (avspilling og nedlasting).

**Direktestrøm og IP-kamerastrømmer:** RTSP — pek Evervideo mot en hvilken som helst `rtsp://`-URL og den spilles av umiddelbart. Flott for overvåkningskameraer, IPTV-strømmer, dørklokke-kameraer, babymonitorer og lignende direktekilder.

**S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og alle andre S3-API-endepunkter.

**Enhetsbiblioteker:** Bilder-biblioteket (alle videoer, skjermopptak, fotoalbum) og Musikk-appbiblioteket (Album, Sjangre, Spillelister) — begge vises inne i Mediebiblioteket slik at du ikke trenger å kopiere noe.

**Lokalt nettverksoppdagelse:** seksjonen Tilgjengelige enheter lister automatisk opp alle Bonjour / mDNS-tjenester på Wi-Fi-nettverket ditt — Plex, Jellyfin, Emby, Synology, QNAP, AirPort-rutere med tilkoblede stasjoner, Apple Time Capsule — slik at du kan trykke for å koble til uten å skrive inn en IP-adresse.

Hver tilkobling bruker den offisielle SDK-en eller den åpne protokollen til tjenesten, med OAuth-basert autorisasjon der det støttes. Du kan koble til flere kontoer av samme tjeneste (for eksempel to Google Drive-kontoer, eller både en Plex- og en Jellyfin-server) og bla gjennom dem side om side i Skylagring-seksjonen.

## Sikkerhet og personvern

Evervideo bruker bare offisielle SDK-er og sikre tilkoblinger for å kommunisere med tilkoblede skytjenester. Brukernavnet og passordet ditt er ikke tilgjengelig for applikasjonen — alle overføringer er TLS-kryptert.

Når du skriver inn brukernavnet og passordet ditt, viser applikasjonen den offisielle autorisasjonssiden levert av skyleverandøren, og hele autorisasjonsprosessen foregår utenfor applikasjonen. Skyleverandøren sender deretter et auth-token til applikasjonen etter vellykket autorisasjon, og det tokenet brukes til API-kall.

Et auth-token er en digital nøkkel som lar tredjepartsapplikasjoner samhandle med skylagring på vegne av deg. Tokenet lagres på enheten din i Apples sikre systemlagring (Keychain), som er kryptert i hvile og beskyttet av enhetens kode eller biometrisk lås. Du kan laste ned filer fra tilkoblede skytjenester til enheten din; disse filene plasseres i appens Dokumenter-katalog og kan fjernes når som helst ved hjelp av den innebygde filbehandleren.

Applikasjonen deler ingen informasjon fra de tilkoblede skykontoene dine med Everappz, annonsører eller noen tredjepart. Du kan tilbakekalle tilgang til skykontoen din når som helst ved å åpne kontoinnstillingssiden i nettleseren din.

## Avvis auth-token

For å tilbakekalle et auth-token, logg inn på skykontoen din i en nettleser og naviger til sikkerhet eller tilkoblede-apper-siden. Der kan du finne alle tredjepartsapper som er koblet til skykontoen din og fjerne hvilken som helst av dem hvis du ikke lenger ønsker å bruke den. Detaljerte instruksjoner for Google-kontoer er tilgjengelige [her](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan også koble fra skykontoen inne i selve applikasjonen — når du gjør det, slettes auth-tokenet umiddelbart fra enheten din. Hvis du avinstallerer applikasjonen fra enheten din, fjernes alle nedlastede data og tilgangstokener automatisk med den.

## Koble fra en skylagring eller endre konfigurasjon

- **Tilgang til skylagringsalternativer** — finn den tilkoblede tjenesten i **Skylagring**-seksjonen i Filer-fanen.
- **Trykk på "..."-knappen** ved siden av tjenestenavnet for å åpne ytterligere alternativer:
  - **Gi nytt navn** — endre navnet på skytjenesten slik det vises i listen din.
  - **Innstillinger** — endre konfigurasjonen eller autentiseringsdataene. Noen ganger må du autorisere den tilkoblede skytjenesten på nytt hvis autorisasjonstokenet har utløpt.
  - **Koble fra** — bryt fullstendig forbindelsen mellom appen og skytjenesten. Dette fjerner alle videoer tilknyttet den tjenesten fra mediebiblioteket ditt, men etterlater dem urørt på serveren.

## Koble til en datamaskin eller NAS

Du kan koble til datamaskinen din, personlig NAS eller annen nettverksenhet ved hjelp av SMB-, WebDAV-, FTP / FTPS-, SFTP-, NFS- eller DLNA-protokollen. Dette er den enkleste måten å bringe et eksisterende hjemme-mediebibliotek — enten det befinner seg på en Mac, Windows-PC, Synology, QNAP, Apple Time Capsule eller WD My Cloud Home — inn i Evervideo uten å kopiere noe.

### Koble til en datamaskin ved hjelp av SMB

- Trykk på **Koble til skylagring → SMB**.
- Skriv inn datamaskinens IP-adresse og delt mappenavn ved hjelp av formatet `smb://computer-ip-address/shared-folder-name`.
- Velg protokollversjon: **Auto**, **SMB1** eller **SMB2**.
- Skriv inn brukernavnet og passordet ditt (hvis påkrevd).
- Trykk på **Ferdig**.

Hvis tilkoblingen er vellykket, vises delingen i Skylagring-seksjonen. En fullstendig veiledning om hvordan du kobler til Mac eller PC via SMB er tilgjengelig [her](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Koble til en NAS ved hjelp av WebDAV

Alle trinn er de samme som for SMB, bortsett fra URL-feltet. Bruk `http://server-name` eller `https://server-name` hvis serveren støtter SSL. WebDAV fungerer med Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home og alle andre servere med et WebDAV-endepunkt.

En fullstendig veiledning om WebDAV er tilgjengelig [her](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Koble til via DLNA / UPnP

Del et mediebibliotek som befinner seg på Windows-PCen eller NAS-en din ved hjelp av DLNA / UPnP-protokollen og få tilgang til den i Evervideo som beskrevet [her](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA er bredt støttet, men det tillater deg kun å spille av eller laste ned videoer — du kan ikke laste opp filer eller opprette nye mapper på en DLNA-server.

### Koble til ved hjelp av FTP, FTPS eller SFTP

Evervideo støtter også de klassiske filoverføringsprotokollene. For å koble til en server via FTP eller FTPS, trykk på Koble til skylagring → FTP, skriv inn verts-URL-en i formatet `ftp://server-name` (eller `ftps://server-name` for en kryptert tilkobling), oppgi brukernavnet og passordet ditt, og trykk deretter Ferdig. For SFTP (SSH-filoverføringsprotokoll), velg SFTP og oppgi enten et passord eller et SSH-nøkkelpar.

### Koble til en NFS-del

Evervideo inkluderer NFS-støtte (Network File System) — nyttig for Linux-verter, BSD-servere og NAS-enheter som foretrekker å eksponere videobiblioteker over NFS i stedet for SMB. Velg NFS i menyen Koble til skylagring, skriv inn serveradressen og den eksporterte stien, og trykk Ferdig.

## Koble til Plex Media Server

Evervideo kan koble direkte til en Plex Media Server og bla gjennom Movies-, TV Shows- og Home Videos-bibliotekene dine. Trykk på Koble til skylagring → Plex, logg inn med Plex-kontoen din, velg en server, og biblioteket vises ved siden av skytjenestene dine. Plex-servere på det samme lokale nettverket oppdages også automatisk i seksjonen Tilgjengelige enheter.

## Koble til en Jellyfin- eller Emby-server

Både Jellyfin (åpen kildekode) og Emby (kommersiell) medieservere fungerer nativt i Evervideo. Trykk på Koble til skylagring → Jellyfin eller Emby, skriv inn server-URL-en din (vanligvis noe som `http://server-ip:8096`) og legitimasjonen, og biblioteket ditt er klart til å streame.

## Koble til en Subsonic- eller Navidrome-server

Evervideo snakker Subsonic-API, noe som betyr at det fungerer med Subsonic selv, Navidrome og alle andre Subsonic-kompatible servere — inkludert Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) og Ampache. Trykk på Koble til skylagring → Subsonic, skriv inn server-URL og legitimasjon, og biblioteket vises i Skylagring-seksjonen.

## Koble til en RTSP-strøm (IP-kameraer, direktesending, IPTV)

Evervideo har native RTSP-støtte, slik at du kan peke den mot hvilken som helst RTSP-kilde — overvåkningskameraer, dørklokke-kameraer, IPTV-leverandører, babymonitorer, kringkastingsfôr — og Evervideo vil hente og dekode strømmen direkte. Trykk på Nettlenker → Legg til lenke, lim inn den fullstendige URL-en (`rtsp://camera-ip:port/stream-path`), oppgi brukernavn og passord hvis påkrevd, og trykk Ferdig.

## Koble til S3-kompatibel objektlagring

For selvhostere og avanserte brukere som bruker skyobjektlagring, inkluderer Evervideo en S3-kompatibel kobling. Trykk på Koble til skylagring → S3-lagring, og skriv inn endepunkt-URL, region, tilgangsnøkkel, hemmelig nøkkel og bucketnavn. Dette fungerer med AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og alle andre S3-API-endepunkter.

## Tilgjengelige enheter

Denne seksjonen viser alle enheter på det lokale nettverket ditt som du kan koble til fra Evervideo via Bonjour / mDNS-oppdagelse — Plex, Jellyfin, Emby, Synology, QNAP, AirPort-rutere med tilkoblede stasjoner, Apple Time Capsule og så videre. For å opprette en tilkobling:

- Rull til seksjonen Tilgjengelige enheter i Filer-fanen.
- Trykk på enheten du vil koble til.
- Hvis nødvendig, skriv inn påloggingsdetaljene for å fullføre tilkoblingen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Tilgjengelige enheter på det lokale nettverket" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive lar deg overføre filer trådløst fra datamaskinen til iOS-enheten din via hvilken som helst stasjonær nettleser, Finder eller File Explorer. Enheten og datamaskinen din må være på samme Wi-Fi-nettverk.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Aktiver Wi-Fi Drive

- I Filer-fanen, rull til Skylagring → Koble til via Wi-Fi for å åpne Wi-Fi Drive-hovedskjermen.
- (Valgfritt) Sett et brukernavn og passord for den innebygde webserveren.
- Trykk på Start Wi-Fi Drive.

### Få tilgang til Wi-Fi Drive på datamaskinen din

- Åpne en nettleser på datamaskinen din (Chrome, Firefox, Safari, osv.).
- Skriv inn URL-en vist av applikasjonen.
- Dra og slipp filer fra datamaskinen til nettsiden — de vil begynne å overføres til iOS-enheten din.

Du kan også montere Wi-Fi Drive direkte i **Finder** på macOS (Gå → Koble til server…) eller File Explorer på Windows (Kartlegg nettverksstasjon…) og behandle iPhone eller iPad som en vanlig nettverksstasjon.

Detaljerte instruksjoner er tilgjengelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder fildeling

iTunes-fildeling (nå Finder-fildeling på macOS Catalina og nyere) lar deg overføre filer ved hjelp av en Lightning- eller USB-C-kabel. Koble til enheten, åpne Finder på Mac (eller iTunes på Windows), finn Evervideo i applisten, og kopier filer til den delte mappen.

## Koble til en USB-flashstasjon eller SD-kort

Koble en USB-stasjon eller SD-kort til iPhone, iPad eller Mac via Lightning-til-USB / USB-C-adapteren eller kortleseren. Åpne Filer → Filer på denne iPhone → Åpne mappe, naviger til stasjonen og velg en videofil eller mappe. Evervideo spiller av filer direkte fra stasjonen uten å kopiere dem til intern lagring — nyttig for svært store 4K-biblioteker.

## Mappenavigasjon i tilkoblede lagringsenheter

Trykk på en tilkoblet skytjeneste for å åpne filleseren. Mapper viser videominiatyrbilder når tilgjengelig, og å trykke på en video starter avspilling umiddelbart mens resten av filen streames i bakgrunnen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Blar gjennom mapper i tilkoblede lagringsenheter" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Hurtigtilgang

Hurtigtilgang-seksjonen sitter øverst i Filer-fanen. Den gir deg rask tilgang til favorittfilene og -mappene dine og nylig åpnede filer og mapper — både fra skytjenester og fra enhetens lagring. Når du åpner en fil eller mappe fra skyen, legges den til i listen Nylig åpnet. Du kan merke dypt nestede mapper som Favoritter for å få tilgang til dem raskt uten å grave gjennom katalogstrukturen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Nettlenker og hurtigtilgang" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Filer i denne applikasjonen

Denne seksjonen viser filer og mapper lagret i Evervideo sin sandkasse-Dokumenter-katalog — alt du har lastet ned fra skyen, overført via Wi-Fi Drive, kopiert gjennom Finder-fildeling eller importert fra en annen app.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Filer i denne applikasjonen" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Dokumenter-mappen

Dokumenter-mappen er roten til alt inne i Filer i denne applikasjonen. Du kan opprette undermapper, gi filer nytt navn, flytte dem rundt og gruppere dem slik du ønsker.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Lokale filer — Dokumenter-mappen" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Filer på denne iPhone / iPad / Mac

Denne seksjonen viser videoer som befinner seg på enheten din, men i andre applikasjoner. Du kan importere dem til Evervideo ved hjelp av systemfilvelgeren:

- Trykk på Åpne filer… for å velge spesifikke filer.
- Trykk på Åpne mappe… for å velge en hel mappe.

Du kan også bruke Koble til en mappe for å opprette en kobling til en mappe på enheten din med lese- / skrivetilgang — perfekt for å arbeide med en mappe på iCloud Drive eller en tilkoblet USB-stasjon uten å kopiere noe.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Filer på denne enheten" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Spesielle mapper

I Filer-fanen vil du se flere spesielle mapper som Evervideo oppretter og bruker automatisk:

- **Nedlastinger** — alle filer lastet ned fra skyen vises her som standard. Tilpass i Innstillinger → Filbehandling → Lagre nedlastede filer i.
- **Spillerbuffer** — mediespillerens buffer. Som standard laster spilleren ned kommende videoer for jevn avspilling. Du kan deaktivere bufferen i appinnstillinger eller ganske enkelt slette denne mappen.
- **iCloud** — filer i denne mappen synkroniseres på alle enhetene dine koblet til den samme iCloud-kontoen.
- **Offline-mapper** — når du merker en mappe, spilleliste, album eller sjanger som tilgjengelig offline, lastes filene ned til denne mappen.

## Verktøylinje øverst

Verktøylinjen øverst, under navigasjonslinjen, tilbyr flere handlinger du kan vise eller skjule med et nedover-sveipgebaar:

- **Søk** — utfør et søk innen den gjeldende mappen eller seksjonen.
- **Fortsett avspilling** — hvis aktivert i innstillinger, gjenopprett avspillingskøen og siste videoposisjon for den gjeldende mappen.
- **Spill alle** — skann den gjeldende mappen og dens undermapper og legg til filer i avspillingskøen.
- **Bland alle** — som Spill alle, men bland først.

## Mappealternativer

Når du åpner en mappe, trykk på **"..."**-knappen i øvre høyre hjørne for disse handlingene:

- **Velge** — aktiver filtvelgingsmodus.
- **Ny mappe** — opprett en ny mappe i den gjeldende mappen.
- **Aktivere offline-modus** — slå på offline-synkronisering for den gjeldende mappen. Nye filer lagt til online lastes ned automatisk.
- **Last opp filer** — last opp filer fra enheten til den online mappen.
- **Søk** — søk innen mappen.
- **Sorter** — sorter filer etter navn, størrelse, endringsdato eller metadata.
- **Rutenett / Listevisning** — bytt mellom tabellvisning og miniatyrbildevisning. Miniatyrbildevisning viser store videoposter-forhåndsvisninger.

## Utvelgelsesmodus

Trykk på **"..."** i øvre høyre hjørne og velg **Velge** for å gå inn i utvelgelsesmodus. Det vises avmerkingsbokser ved siden av alle filer og mapper. Trykk for å velge ett eller flere elementer, og utfør deretter batchhandlinger: Spill neste, Spill senere, Legg til i mediebibliotek, Legg til i spilleliste, Kopier, Last opp, Flytt, Gi nytt navn eller Slett.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Utvelgelsesmodus i filbehandleren" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Hvis du heller vil behandle tilkoblet skylagring som skrivebeskyttet (for å forhindre utilsiktet sletting), aktiver Innstillinger → Filbehandling → Rediger netttfiler → Av for å skjule alle destruktive operasjoner fra UI-en.

## Filhandlinger

Trykk på **"..."**-ikonet nær filens tittel for å vise handlingsmenyen:

- **Spill neste** — sett inn filen øverst i avspillingskøen.
- **Spill senere** — legg til filen nederst i avspillingskøen.
- **Legg til i mediebibliotek** — inkluder filen i mediebiblioteket ditt, organisert etter Album og Sjanger.
- **Legg til i spilleliste** — legg til filen i en eksisterende spilleliste eller opprett en ny.
- **Rediger tagger** — åpne den innebygde taggeditoren for å endre metadata. For nettfiler lastes filen ned midlertidig, redigeres og lastes deretter opp på nytt etter at du bekrefter.
- **Legg til i favoritter** — legg til filen i favorittlisten din for rask tilgang.
- **Laste ned** — last ned filen eller mappen til enheten for offline bruk.
- **Gi nytt navn** — gi filen nytt navn direkte på fjernlagringen.
- **Flytt** — flytt filen til en annen mappe i skylagringen din.
- **Legg til i arkiv** — pakk filen inn i en enkelt ZIP-fil (Premium-funksjon).
- **Åpne i** — eksporter filen til en annen kompatibel app via system-Delings-arket.
- **Slette** — fjern filen permanent. **Denne handlingen kan ikke angres.**

## Mappehandlinger

For hver mappe i skylagringen din har du mange handlinger tilgjengelig ved å trykke på **"..."**-ikonet ved siden av mappenavnet.

- **Spill alle** — erstatt gjeldende avspillingskø med alle videoer i mappen.
- **Spill neste / Spill senere** — legg til hele mappen i køen.
- **Legg til i mediebibliotek** — inkluder mappens innhold i mediebiblioteket ditt.
- **Legg til i spilleliste** — legg til hele mappen i en spilleliste.
- **Legg til i favoritter** — legg til mappen i favorittene dine.
- **Aktivere offline-modus** — utover en enkel nedlasting, overvåker dette kontinuerlig mappen for nye filer og laster dem automatisk ned ettersom de dukker opp online.
- **Laste ned** — last ned alt innhold i mappen til enheten for offline tilgang.
- **Gi nytt navn / Flytt** — gi mappen nytt navn eller flytt den på fjernlagring.
- **Legg til i arkiv** — pakk mappeinnholdet inn i en ZIP-fil (Premium-funksjon).
- **Slette** — fjern mappen og dens innhold permanent. **Denne handlingen kan ikke angres.**

## Overføringskø

I øvre høyre hjørne av Filer-fanen er en **Overføringer**-knapp (et snurrende piler-ikon). Trykk på den for å åpne Overføringskøen — en liste over alle aktive nedlastinger og opplastinger på tvers av alle kildene dine, med sanntidsfremdrift, hastighet og ETA per fil.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Filoverføringskø" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Du kan sette på pause, gjenoppta, prøve mislykkede overføringer på nytt, omorganisere elementer for å prioritere spesifikke nedlastinger, eller avbryte dem individuelt. Du kan også justere overføringskøhastigheten (maksimale parallelle oppgaver), nettverkstype (kun Wi-Fi eller Wi-Fi + mobil) og bakgrunnsoverføringer i Innstillinger → Filbehandling.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Handlinger på filoverføringskøen" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offline modus og synkroniserte offline-mapper

Offline modus er en praktisk funksjon som lar deg se favorittvideoene dine selv når du ikke er koblet til internett. Når du aktiverer offline modus for en mappe, spilleliste, album eller sjanger, lastes alle filer i den samlingen automatisk ned til enheten for offline avspilling. De vises i seksjonen Offline-mapper.

Når du legger til nye filer på den eksterne serveren, lastes de også automatisk ned — slik at offline-samlingen din holder seg oppdatert uten at du trenger å gjøre noe. For å synkronisere manuelt, trykk på de tre prikkene i øvre høyre hjørne av en offline-mappe og velg Synkronisere.

Du kan justere synkroniseringstidsavbruddet i Innstillinger → Filbehandling → Synkroniserte offline-mapper → Tidsintervall.

Detaljerte instruksjoner er tilgjengelige [her](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalisering

I Innstillinger → Personalisering kan du konfigurere hvordan Filer-fanen presenteres:

- **Filskjermstil** — Enkel meny (viser mappelisten direkte) eller Gruppert meny (grupperer innhold etter kategori — Hurtigtilgang, Spesielle mapper, Skylagring, osv.).
