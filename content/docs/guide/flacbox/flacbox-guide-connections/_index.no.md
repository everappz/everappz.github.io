---
title: "Tilkoblinger"
date: 2020-02-01
description: "Lær hvordan du kobler til skytjenester og NAS-enheter i Flacbox. Stream høyoppløsningsmusikk fra iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk og mer. Bruk SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder-fildeling og USB-minnepinner."
keywords: [
  "Flacbox sky-oppsett", "koble Google Drive til Flacbox", "SMB musikkstrøm",
  "WebDAV iOS spiller", "DLNA musikk-app", "NAS lydstrøm", "Wi-Fi Drive iPhone",
  "overføre filer til iPhone", "Flacbox iTunes fildeling", "koble NAS til iPhone",
  "Synology Drive musikk-app", "QNAP musikk-app", "Bluesound musikk-app",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm scrobbling musikk-app",
  "iXpand Flash Drive musikk", "USB DAC iPhone"
]
tags: ["guide", "flacbox", "tilkoblinger", "sky", "NAS"]
readingTime: 12
---


På dette skjermbildet kan du koble til alle kilder som inneholder musikken din. Du kan integrere populære skytjenester som Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive og mange flere, samt din Mac, PC eller NAS via standard protokoller. Enten samlingen din ligger på en strømmevennlig tjeneste som Dropbox eller på en personlig NAS som Synology, QNAP, Buffalo, Apple Time Capsule eller WD My Cloud Home, kobler Flacbox til dem alle fra ett enkelt skjermbilde.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Tilkoblinger-skjerm" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Koble til Skylagring

- Åpne **Tilkoblinger**-fanen.
- Velg **Koble til skylagring** fra menyen.
- Velg en skylagringstjeneste fra listen.
- Skriv inn påloggingsinformasjonen din på den offisielle autorisasjonssiden som skyleverandøren gir, og trykk deretter på **Ferdig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Legg til en Skylagringstjeneste" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Hvis du opplever problemer, sjekk internettforbindelsen og brukernavnet / passordet ditt. I Premium-versjonen av appen kan du legge til et ubegrenset antall tjenester; gratisversjonen støtter opptil tre.

## Støttede Skylagringstjenester, Medieservere og Protokoller

Flacbox støtter et eksepsjonelt bredt spekter av musikkilder. Alt nedenfor fungerer fra ett enkelt **Koble til skylagring**-skjermbilde.

**Personlig skylagring:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Selvhostede servere:** Plex · Jellyfin · Emby · Subsonic (og alle Subsonic-kompatible servere — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (og ownCloud via det delte API-et) · Synology Drive · QNAP.

**NAS og fildeling-protokoller:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH-filoverføringsprotokoll, passord eller offentlig-nøkkel-autentisering) · NFS · DLNA / UPnP (avspilling og nedlasting).

**S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og alle andre S3-API-endepunkter.

**Lokalt nettverksoppdagelse:** Tilgjengelige enheter-seksjonen lister automatisk opp alle Bonjour / mDNS-tjenester på Wi-Fi-nettverket ditt slik at du kan trykke for å koble til uten å skrive inn en IP-adresse.

Hver tilkobling bruker **den offisielle SDK-en eller det åpne protokollen** til tjenesten, med OAuth-autorisasjon der det støttes. Du kan koble til flere kontoer av samme tjeneste og bla gjennom dem side om side i Tilkoblinger-skjermbildet.

## Sikkerhet og Personvern

Vi bruker kun offisielle SDK-er og sikre tilkoblinger for å samhandle med tilkoblede skytjenester. Brukernavnet og passordet ditt er ikke tilgjengelig for applikasjonen — alle overføringer er TLS-kryptert.

Når du skriver inn brukernavnet og passordet ditt, viser applikasjonen den offisielle autorisasjonssiden som skyleverandøren gir, og hele autorisasjonsprosessen foregår utenfor applikasjonen. Skyleverandøren sender deretter et auth-token til applikasjonen etter vellykket autorisasjon, og det tokenet brukes til å gjøre API-kall.

Et auth-token er en digital nøkkel som lar tredjepartsapplikasjoner samhandle med skylagring på dine vegne. Tokenet lagres på enheten din i Apples sikre systemlagring (Keychain), som er kryptert i hvile og beskyttet av enhetskoden eller biometrisk lås. Du kan laste ned filer fra tilkoblede skytjenester til enheten din; disse filene plasseres i appens Documents-katalog og kan fjernes når som helst ved hjelp av den innebygde filbehandleren.

Applikasjonen deler ingen informasjon fra dine tilkoblede skykontoer med Everappz, annonsører eller noen tredjepart. Du kan tilbakekalle tilgangen til skykontoen din når som helst ved å åpne kontoinnstillingssiden i nettleseren din.

## Avvis Auth-Token

For å tilbakekalle et auth-token, logg inn på skykontoen din i en nettleser og naviger til sikkerhets- eller tilkoblede apper-siden. Der kan du finne alle tredjepartsapper som er koblet til skykontoen din og fjerne dem hvis du ikke lenger vil bruke dem. Detaljerte instruksjoner for Google-kontoer er tilgjengelige [her](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan også koble fra skykontoen inne i selve applikasjonen — når du gjør det, slettes auth-tokenet umiddelbart fra enheten din. Hvis du avinstallerer applikasjonen fra enheten din, fjernes alle nedlastede data og tilgangstokener automatisk sammen med den.

## Koble fra en Skylagring eller Endre Konfigurasjon

- **Tilgang til skylagringsalternativer** — finn den tilkoblede tjenesten i **Tilkoblinger**-skjermbildet.
- **Trykk på "..."-knappen** ved siden av tjenestens tittel for å åpne ekstra alternativer:
  - **Gi nytt navn** — endre navnet på skytjenesten slik det vises i listen din.
  - **Innstillinger** — endre konfigurasjonen eller autentiseringsdataene. Noen ganger må du kanskje re-autorisere den tilkoblede skytjenesten hvis autorisasjonstokenet har utløpt.
  - **Koble fra** — bryt forbindelsen mellom appen og skytjenesten fullstendig. Dette fjerner alle sanger tilknyttet den tjenesten fra appens musikkbibliotek, men lar dem være urørte på serveren.

## Koble til en Datamaskin eller NAS

Du kan også koble til datamaskinen din, personlig NAS eller andre nettverksenheter ved hjelp av SMB-, DLNA- eller WebDAV-protokollene. Dette er den enkleste måten å bringe et eksisterende hjemmemusikkbibliotek — enten det befinner seg på en Mac, Windows-PC, Synology-boks eller NAS — inn i Flacbox uten å kopiere noe.

## Koble til en Datamaskin med SMB

- Trykk på **Koble til skylagring → SMB**.
- Skriv inn datamaskinens IP-adresse og navnet på den delte mappen i URL-feltet med formatet `smb://computer-ip-address/shared-folder-name`.
- Velg protokollversjon: **Auto**, **SMB1** eller **SMB2**.
- Skriv inn brukernavnet og passordet ditt (om nødvendig).
- Trykk på **Ferdig**.

Hvis tilkoblingen er vellykket, ser du den tilkoblede lagringen i **Skylagring**-seksjonen. En fullstendig veiledning om hvordan du kobler til Mac eller PC med SMB er tilgjengelig [her](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Koble til en NAS med WebDAV

Alle trinnene er de samme som SMB, bortsett fra URL-feltet. URL-en skal ha formatet `http://server-name` eller `https://server-name` hvis serveren støtter SSL. WebDAV fungerer med **Synology, QNAP, Nextcloud, ownCloud** og mange andre servere.

En fullstendig veiledning om hvordan du kobler til en NAS med WebDAV er tilgjengelig [her](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Koble til en Datamaskin eller NAS med DLNA

Du kan også dele et musikkbibliotek på Windows-PC-en eller den personlige NAS-en din ved hjelp av DLNA / UPnP-protokollen og få tilgang til det biblioteket i appen som beskrevet [her](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA er en populær, mye støttet protokoll, men den lar deg bare spille av eller laste ned musikk — du kan ikke laste opp filer eller opprette nye mapper på en DLNA-server.

## Koble til en NAS eller Server med FTP, FTPS eller SFTP

Flacbox støtter også de klassiske filoverføringsprotokollene. For å koble til en server via FTP eller FTPS, trykk på **Koble til skylagring → FTP**, skriv inn vert-URL-en i formen `ftp://server-name` (eller `ftps://server-name` for en kryptert forbindelse), oppgi brukernavnet og passordet ditt, og trykk deretter på **Ferdig**. For **SFTP** (SSH-filoverføringsprotokoll), velg **SFTP** i stedet og oppgi enten et passord eller et SSH-nøkkelpar.

## Koble til en NFS-deling

Flacbox inkluderer **NFS**-støtte (Network File System) — praktisk for Linux-verter, BSD-servere og NAS-enheter. Velg **NFS** i menyen **Koble til skylagring**, skriv inn serveradressen og den eksporterte stien, og trykk på **Ferdig**.

## Koble til en Plex Media Server

Flacbox kan koble direkte til en Plex Media Server og bla gjennom musikkbiblioteket ditt etter artister, album, sjangre og spillelister. Trykk på **Koble til skylagring → Plex**, logg inn med Plex-kontoen din, velg en server, og biblioteket vises ved siden av skytjenestene dine. Plex-servere på det samme lokale nettverket oppdages også automatisk i **Tilgjengelige enheter**-seksjonen.

## Koble til en Jellyfin- eller Emby-server

Både **Jellyfin** (åpen kildekode) og **Emby** (kommersiell) fungerer nativt i Flacbox. Trykk på **Koble til skylagring → Jellyfin** eller **Emby**, skriv inn server-URL-en din (noe som `http://server-ip:8096`) og påloggingsinformasjon, og musikkbiblioteket ditt er klart til å strømme.

## Koble til en Subsonic- eller Navidrome-server

Flacbox støtter Subsonic API, noe som betyr at det fungerer med **Subsonic** selv, **Navidrome** og alle andre Subsonic-kompatible servere — inkludert Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Trykk på **Koble til skylagring → Subsonic**, skriv inn server-URL og påloggingsinformasjon, og biblioteket vises i Tilkoblinger-skjermbildet.

## Koble til S3-kompatibel Objektlagring

For selvhostere og audiofiler som bruker skyobjektlagring, inkluderer Flacbox en S3-kompatibel tilkobling. Trykk på **Koble til skylagring → S3-lagring**, og skriv deretter inn endepunkt-URL, region, tilgangsnøkkel, hemmelig nøkkel og bøttenavn.

## Tilgjengelige Enheter

Denne seksjonen viser alle enheter på det lokale nettverket ditt som du kan koble til fra Flacbox via Bonjour-oppdagelse. Følg disse trinnene for å opprette en tilkobling:

- Åpne appen og gå til **Tilgjengelige enheter**-seksjonen under Tilkoblinger.
- Trykk på enheten du vil koble til.
- Skriv om nødvendig inn påloggingsinformasjonen din for å fullføre tilkoblingen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Tilgjengelige Enheter på Lokalt Nettverk" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive er en praktisk teknologi som muliggjør trådløs filoverføring fra datamaskinen til iOS-enheten din via en hvilken som helst skrivebordsnettleser. For å bruke denne funksjonen effektivt, sørg for at enheten og datamaskinen er koblet til det samme Wi-Fi-nettverket.

### Aktiver Wi-Fi Drive

- Åpne applikasjonen og gå til **Tilkoblinger**-fanen.
- Velg **Koble til via Wi-Fi** for å få tilgang til Wi-Fi Drive-hovedskjermen.
- (Valgfritt) Angi brukernavn og passord for den innebygde webserveren for å beskytte tilgangen.
- Trykk på **Start Wi-Fi Drive** for å aktivere Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Tilgang til Wi-Fi Drive på Datamaskinen din

- Åpne en nettleser på datamaskinen din (Chrome, Firefox eller Safari).
- I adressefeltet i nettleseren, skriv inn URL-en som applikasjonen oppgir.

### Overfør Filer Trådløst

Når nettsiden for iOS-enheten din åpnes i nettleseren, kan du enkelt dra og slippe filer fra datamaskinen til nettsiden. Filene du slipper begynner å bli overført til iOS-enheten din og er tilgjengelige inne i Flacbox.

Du kan også montere Wi-Fi Drive direkte i Finder på macOS (Gå → Koble til server…) eller Filutforsker på Windows (Koble til nettverksstasjon…) og behandle iPhone eller iPad som en vanlig nettverksstasjon.

Detaljerte instruksjoner om trådløs filoverføring via Wi-Fi Drive er tilgjengelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder-fildeling

iTunes-fildeling (nå Finder-fildeling på macOS Catalina og nyere) er en annen måte å overføre filer fra en datamaskin til en enhet ved hjelp av en Lightning- eller USB-C-kabel.

- Koble enheten til datamaskinen med en kabel og kjør **Finder** på Mac (eller **iTunes** på Windows).
- Åpne **Steder → Tilkoblet enhet → Filer** og finn Flacbox-appen.
- Trykk på app-ikonet for å se alle delte mapper.
- Kopier filer fra datamaskinen til den delte mappen på enheten ved hjelp av dra-og-slipp.

Detaljerte instruksjoner om Finder-fildeling er tilgjengelige [her](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Koble til en USB-minnepenn

Hvis du har et SD-kort eller USB-stasjon, kan du koble det til med en Lightning-til-USB / SD-kortleser eller en USB-C-stasjon (på iPad og iPhone 15 / 16 / 17 / Pro). Appen støtter Apple-sertifiserte kortlesere og iXpand-minnepinner. Med en iXpand-minnepenn, sett den inn i Lightning-porten og åpne applikasjonen — du ser meldingen Ekstern enhet tilkoblet og enhetsinformasjon. Trykk på minnepenn-ikonet for å få tilgang til musikkmappen og trykk på en lydfil for å begynne å spille.

Detaljerte instruksjoner om tilkobling av en USB-minnepenn til iPhone er tilgjengelige [her](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Filbehandler

Etter at du har koblet til en skylagringstjeneste, trykk på ikonet for å se alle tilgjengelige filer og mapper. Du kan bruke den innebygde filbehandleren til å jobbe med disse filene — laste ned, gi nytt navn, flytte, laste opp, slette og mer. Når du starter en nedlasting, vises filen i overføringskøen. For å åpne overføringskøen, gå til fanen Lokale filer og trykk på det roterende pil-ikonet øverst til venstre. Alle nedlastede filer og mapper er tilgjengelige i Lokale filer-seksjonen.

## Øverste Verktøylinje

Den øverste verktøylinjen, som er plassert under navigasjonslinjen, tilbyr flere nyttige handlinger for enkel tilgang. Du kan vise eller skjule den med en enkel sveip ned-bevegelse.

- **Søk** — utfør et raskt søk i gjeldende katalog.
- **Fortsett avspilling** — hvis aktivert i applikasjonsinnstillingene, gjenoppretter dette lydspillerkøen og den siste medieposisjonen for gjeldende mappe.
- **Spill alle** — skanner gjeldende mappe og undermapper, legger deretter til alle lydfilene i en ny spillerkø.
- **Shuffle alle** — som Spill alle, men stokker filene før de legges til lydspillerkøen.

## Mappealternativer

Når du åpner en mappe, finner du et praktisk sett med handlinger ved å trykke på **"..."**-knappen øverst til høyre.

- **Velge** — aktiver filvalg-modus.
- **Ny mappe** — opprett en ny mappe i gjeldende mappe.
- **Aktivere offline-modus** — slå på offline-modus for gjeldende mappe.
- **Last opp filer** — last opp filer fra enheten til online-mappen.
- **Søk** — søk etter spesifikke filer i gjeldende mappe.
- **Sorter** — sorter filer etter navn, størrelse, endringsdato eller etter metadata.
- **Rutenett / Listevisning** — bytt mellom tabellvisning og miniatyrvisning.

## Rediger Online Filer

Når du trenger å administrere flere filer i skylagringen din, bruk **Valgmodus** for å effektivisere handlingene dine:

- **Aktiver Valgmodus** — trykk på **"..."**-knappen øverst til høyre og velg **Velge**.
- **Velg Filer** — avmerkingsbokser vises ved siden av alle filer og mapper.
- **Utfør Handlinger** — etter at du har valgt filene eller mappene, har du tilgang til Spill neste, Spill senere, Legg til i musikkbiblioteket, Legg til i en spilleliste, Kopier, Last opp, Flytt, Gi nytt navn og Slette.

## Filhandlinger

Trykk på **"..."**-ikonet nær filens tittel for å åpne handlingsmenyen:

- **Spill neste** — sett inn filen øverst i spillerkøen, slik at den spilles etter gjeldende spor.
- **Spill senere** — legg til filen nederst i spillerkøen.
- **Legg til i musikkbiblioteket** — inkluder filen i musikkbiblioteket ditt.
- **Legg til i en spilleliste** — legg til filen i en eksisterende spilleliste eller opprett en ny.
- **Redigere lydtagger** — åpne den innebygde taggredigeren for å endre metadata.
- **Legg til i favoritter** — legg til filen i favorittlisten din for rask tilgang.
- **Laste ned** — last ned filen eller mappen til enheten din for offline bruk.
- **Gi nytt navn** — gi filen nytt navn direkte på fjernlagringen.
- **Flytt** — flytt filen til en annen mappe i skylagringen din.
- **Åpne i** — eksporter filen til en annen kompatibel app.
- **Slette** — fjern filen permanent fra skylagringen din. **Denne handlingen kan ikke angres.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Flere handlinger for en fil i tilkoblet skylagring" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

## Mappehandlinger

For hver mappe i skylagringen din er et bredt utvalg av handlinger tilgjengelig ved å trykke på **"..."**-ikonet ved siden av mappenavnet.

- **Spill alle** — erstatt gjeldende spillerkø med alle elementer i den valgte mappen.
- **Spill neste** — legg til hele mappen øverst i spillerkøen.
- **Spill senere** — legg til mappeinnholdet nederst i spillerkøen.
- **Legg til i musikkbiblioteket** — inkluder mappens innhold i musikkbiblioteket ditt.
- **Legg til i spilleliste** — legg til hele mappen i en spilleliste. Du har også muligheten til å opprette en ny spilleliste; navn fylles automatisk fra mappenavnet.
- **Legg til i favoritter** — legg til mappen i favorittene dine for rask tilgang.
- **Aktivere offline-modus** — utover en enkel nedlasting, overvåker dette mappen kontinuerlig for nye filer og laster dem ned automatisk når de vises online.
- **Laste ned** — last ned alt innholdet i mappen til enheten din for offline tilgang.
- **Gi nytt navn** — gi mappen nytt navn direkte på fjernlagringen.
- **Flytt** — flytt mappen til en annen plassering i skylagringen din.
- **Arkiv (ZIP)** — samle mappeinnholdet i én ZIP-fil (Premium-funksjon).
- **Slette** — fjern mappen og innholdet permanent fra skylagringen din. **Denne handlingen kan ikke angres.**

## Hurtigtilgang

Hurtigtilgang-seksjonen er plassert øverst på skjermen. Den gir deg rask tilgang til favoritt- og nylig åpnede filer fra tilkoblede skytjenester.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Online lenker og Hurtigtilgang" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Andre Tjenester

Denne seksjonen viser ekstra funksjoner som forbedrer opplevelsen din. For øyeblikket støtter appen **Last.fm**-scrobbling — når tilkoblet sendes avspillingsstatistikken din automatisk til Last.fm-kontoen din. Detaljerte oppsettinstruksjoner er tilgjengelige [her](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm Tilkobling" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
