---
title: "Tilkoblinger"
date: 2020-01-01
description: "Lær å koble til skytjenester, datamaskiner, NAS-enheter og administrere musikkfilene dine med Evermusic. Steg-for-steg-guide til Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes-fildeling og mer."
keywords: [
  "Evermusic", "skymusikkspiller", "NAS-streaming", "Wi-Fi Drive", 
  "SMB", "WebDAV", "DLNA", "iTunes-fildeling", 
  "koble til skylagring", "musikkoverdragelse iPhone", "filbehandler iOS"
]
tags: ["evermusic", "guide", "tilkoblinger"]
readingTime: 11
---


På Tilkoblinger-skjermen kan du koble til alle kilder som inneholder musikken din — populære skytjenester, selvhostede medieservere, Mac eller PC, en personlig NAS, Apple Time Capsule, WD My Cloud Home, til og med en USB-minnepinne — og bruke dem alle fra ett enhetlig grensesnitt. Tilkoblinger er også der du konfigurerer Hurtig tilgang til dypt nestede skymapper og der du autentiserer Last.fm for scrobbling.

Skjermen er delt inn i tydelig merkede seksjoner som skalerer fra en enkelt iCloud Drive-konto til et bibliotek spredt over flere skyer og NAS-enheter: Hurtig tilgang øverst (favorittskymappene dine), Skylagring (kontoene du har lagt til), Lokalt nettverk (Bonjour-oppdagede enheter), Datamaskin (Wi-Fi Drive, iTunes-fildeling, SMB), Eksterne tilbehør (tilkoblede USB-minnepinner) og Andre tjenester (Last.fm og lignende).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic tilkoblingsskjerm" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Koble til skylagring

- Åpne Tilkoblinger-fanen.
- Velg Koble til skylagring fra menyen.
- Velg en skylagringstjeneste fra listen.
- Logg inn på leverandørens offisielle autorisasjonsside (Evermusic ser aldri passordet ditt).
- Trykk Ferdig.

{{< cards cols="1">}}
  {{< card title="" subtitle="Velger for skyleverandør" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Hvis du støter på problemer, dobbeltsjekk internettforbindelsen og påloggingsinformasjonen, og sørg for at tofaktorautentisering er riktig konfigurert for den tjenesten.  
I Premium-versjonen av appen kan du legge til et ubegrenset antall tjenester. Gratisbrukere kan koble til én skykonto om gangen.

## Støttede skylagringstjenester

Evermusic støtter hele utvalget av populære sky- og selvhostede tjenester. Gratisbrukere får den samme leverandørkatalogen, men med én-konto-grensen; Premium låser opp ubegrensede kontoer og fjerner de fleste andre begrensninger.

- **Personlige skykontoer:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Selvhostede servere og mediebiblioteker:** Plex · Jellyfin · Emby · Subsonic (og alle Subsonic-kompatible servere — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (og Owncloud, via den delte API-en) · Synology Drive · QNAP.
- **NAS- og fildeling-protokoller:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (passord- eller offentlig nøkkelautentisering), NFS og DLNA (skrivebeskyttet — avspilling og nedlasting).
- **S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage eller et hvilket som helst S3-API-endepunkt.
- **Lokalt nettverk oppdagelse:** seksjonen Tilgjengelige enheter lister automatisk opp alle enheter på Wi-Fi-nettverket ditt som annonserer seg selv via Bonjour / mDNS — Plex, Jellyfin, Emby-servere, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, AirPort-rutere med tilkoblede stasjoner og så videre.

## Sikkerhet og personvern

Vi bruker bare offisiell SDK og sikker tilkobling for å samhandle med tilkoblede skytjenester. Brukernavnet og passordet ditt er ikke tilgjengelig for applikasjonen. Alle forespørsler fra applikasjonen til skytjenesten er kryptert.

Når du skriver inn brukernavn og passord, viser applikasjonen deg den offisielle autorisasjonssiden som tilbys av skyleverandøren, og hele autorisasjonsprosessen skjer utenfor applikasjonen. Skyleverandøren sender et auth-token til applikasjonen etter vellykket autorisasjon, og det tokenet brukes til å gjøre API-kall.

Auth-token er en digital nøkkel som lar tredjepartsapplikasjoner samhandle med skylagring. Auth-token lagres på enheten din i en sikker systemlagring kalt Keychain. Du kan laste ned filene dine fra den tilkoblede skytjenesten til enheten, og disse filene vil bli plassert i appens "Dokumenter"-katalog. Du kan fjerne disse filene når som helst ved hjelp av den innebygde filbehandleren.

Applikasjonen deler ingen informasjon fra den tilkoblede skykontoen. Du kan trekke tilbake tilgang til skykontoen din når som helst ved å åpne kontoinnstillingssiden i nettleseren din.

## Avvis auth-token

Logg inn på kontoen din i nettleseren og naviger til innstillingssiden. Der kan du finne alle tredjepartsapper som er koblet til skykontoen din og fjerne hvilke som helst du ikke vil bruke lenger. Detaljerte instruksjoner er tilgjengelige [her](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan også koble fra de tilkoblede skykontoene i applikasjonen, og auth-tokenet vil også bli fjernet fra enheten din. Hvis du fjerner applikasjonen fra enheten, vil alle nedlastede data og tilgangstokens også bli fjernet.

## Koble fra en skylagring eller endre konfigurasjon

- Tilgang til skylagringsalternativer: finn først skylagringen du ønsker å administrere i appens grensesnitt.
- Trykk på '...'-knappen: ved siden av tjenestetittelen ser du en '...'-knapp. Trykk på den for å få tilgang til ytterligere alternativer.
  - **Gi nytt navn**: hvis du vil endre navnet på skytjenesten slik det vises i listen din, velg 'Gi nytt navn.'
  - **Innstillinger**: for å endre konfigurasjon eller autentiseringsdata for skytjenesten, velg 'Innstillinger.' Noen ganger må du re-autorisere den tilkoblede skytjenesten hvis autorisasjonstokenet har utløpt.
  - **Koble fra**: hvis du ønsker å fullstendig avbryte forbindelsen mellom appen og skytjenesten, velg 'Koble fra.' Vær oppmerksom på at dette vil fjerne alle sanger tilknyttet denne skytjenesten fra appens musikkbibliotek, men de vil forbli på serveren.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flere handlinger-meny for tilkoblet skylagring" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Koble til datamaskin eller NAS

Du kan også koble til datamaskinen, personlig NAS eller andre nettverksenheter ved hjelp av SMB, DLNA eller WebDAV-protokoll.

## Koble til datamaskin via SMB

- Trykk på "Koble til skylagring" → SMB.
- Skriv inn datamaskinens IP-adresse og delt mappenavn i URL-feltet med formatet smb://datamaskin-ip-adresse/delt-mappenavn
- Velg protokollversjon: Auto, SMB1, SMB2
- Skriv inn brukernavn og passord (hvis nødvendig)
- Trykk "Ferdig".

Hvis tilkoblingen er vellykket, ser du tilkoblet lagring i seksjonen "Skylagring."  
En fullstendig opplæring om hvordan du kobler Mac eller PC via SMB er tilgjengelig [her](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB-tilkoblingsinnstillinger" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Koble til NAS via WebDAV

Alle trinnene er de samme bortsett fra URL-feltet.  
URL skal ha formatet http://servernavn, eller https://servernavn hvis serveren støtter SSL.
En fullstendig opplæring om hvordan du kobler NAS via WebDAV-protokoll er tilgjengelig [her](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV-tilkoblingsinnstillinger" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Koble til datamaskin eller NAS via DLNA

Du kan også dele et musikkbibliotek som befinner seg på Windows-PC-en eller den personlige NAS-en din ved hjelp av DLNA-protokollen og få tilgang til det biblioteket i appen som beskrevet [her](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA er en populær og mye brukt protokoll, men den lar deg bare spille av eller laste ned musikk. Du kan ikke laste opp filer eller opprette nye mapper på serveren.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA-tilkoblingsinnstillinger" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Tilgjengelige enheter

Denne seksjonen viser alle enheter i det lokale nettverket du kan koble til via applikasjonen.  
For å opprette en forbindelse med en enhet, følg disse trinnene:

- Åpne appen og gå til seksjonen "Tilgjengelige enheter".
- Trykk på enheten du vil koble til fra listen.
- Hvis nødvendig, skriv inn påloggingsinformasjonen din for å fullføre tilkoblingen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tilgjengelige enheter i det lokale nettverket" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive 

Wi-Fi Drive er en praktisk teknologi som muliggjør trådløse filoverføringer fra datamaskinen til iOS-enheten via en stasjonær nettleser.  
For å bruke denne funksjonen effektivt, sørg for at enheten og datamaskinen er koblet til det samme Wi-Fi-nettverket.   
Her er en steg-for-steg-guide om hvordan du bruker Wi-Fi Drive.

## Aktiver Wi-Fi Drive

- Åpne applikasjonen og gå til "Tilkoblinger"-fanen.
- Velg "Koble til via Wi-Fi" for å få tilgang til Wi-Fi Drive-hovedskjermen.
- Trykk "Start Wi-Fi Drive" for å aktivere Wi-Fi Drive.

## Få tilgang til Wi-Fi Drive på datamaskinen

- På datamaskinen (stasjonær eller bærbar), åpne en nettleser (som Chrome, Firefox eller Safari).
- I nettleserens adresselinje, skriv inn URL-en som applikasjonen oppgir.

## Overfør filer trådløst

Når nettsiden som tilsvarer iOS-enheten åpnes i nettleseren, kan du enkelt dra og slippe filer fra datamaskinen til nettsiden.  
Filene du drar og slipper begynner å overføres til iOS-enheten og vil være tilgjengelige i applikasjonen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive-serverinnstillinger" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Detaljerte instruksjoner om hvordan du overfører filer trådløst ved hjelp av Wi-Fi Drive er tilgjengelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes-fildeling

iTunes-fildeling er en annen teknologi som lar deg overføre filer fra datamaskin til enhet ved hjelp av Finder-appen på Mac og en lightning-kabel.   
- Bare koble en enhet til datamaskinen med en kabel og kjør Finder-appen på Mac-en. 
- Åpne "Steder" → "Din tilkoblede enhet" → "Filer" → og finn Evermusic-appen. 
- Trykk på app-ikonet for å se alle delte mapper. 
- Kopier filer fra datamaskinen til den delte mappen på enheten ved å dra og slippe.   

Detaljerte instruksjoner om hvordan du bruker iTunes-fildeling er tilgjengelige [her](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder-fildeling på Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Koble til et USB-minnekort

Hvis du har et SD-kort, kan du koble det til ved hjelp av en lightning-kortleser. Appen støtter for øyeblikket Apple Certified-kortlesere og iXpand-minnepinner. Hvis du har iXpand-minnepinne — sett den inn i lightning-porten og åpne applikasjonen. Du vil se en melding om 'Ekstern enhet tilkoblet' og enhetsinformasjon. Trykk ganske enkelt på minnepinneikonet for å få tilgang til musikkmappen og trykk på en lydfil for å begynne å spille. Vi har detaljerte instruksjoner om hvordan du kobler et USB-minnekort til iPhone og lytter til musikk eller administrerer filer på det som er tilgjengelige [her](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Filbehandler

Når du har koblet til en skylagringstjeneste, trykk på ikonet for å se alle tilgjengelige filer og mapper. Du kan bruke den innebygde filbehandleren til å jobbe med disse filene — laste ned, gi nytt navn, flytte og mer. Når du starter en nedlasting, vil filen vises i overføringskøen. For å se overføringskøen, gå til "Lokale filer"-fanen og trykk på de roterende pilene øverst til venstre. Alle nedlastede filer og mapper er tilgjengelige i seksjonen "Lokale filer".

## Øverste verktøylinje

Den øverste verktøylinjen, praktisk plassert under navigasjonsbjelken, tilbyr flere nyttige handlinger for enkel tilgang. Du kan vise eller skjule denne verktøylinjen ved å bruke en enkel sveipebevegelse nedover. Her er de tilgjengelige handlingene:

- **Søk**: Dette alternativet lar deg utføre et raskt søk i gjeldende katalog, noe som gjør det enkelt å finne bestemte filer eller mapper.
- **Fortsett avspilling**: Hvis aktivert i applikasjonsinnstillingene, gjenoppretter denne funksjonen lydspillerkøen og siste mediaposisjon for gjeldende mappe. Det er en praktisk måte å fortsette der du slapp i musikkbiblioteket ditt.
- **Spill alle**: Ved å velge denne handlingen vil appen skanne gjeldende mappe og undermapper, legge til alle lydfilene som er funnet i en ny spillerkø. Dette er nyttig når du vil spille all musikken i en bestemt katalog.
- **Bland alle**: Ligner på "Spill alle", denne handlingen skanner gjeldende mappe og undermapper, men blander filene før de legges til lydspillerkøen. Det er en flott måte å nyte musikken i tilfeldig rekkefølge for litt variasjon.

{{< cards cols="1">}}
  {{< card title="" subtitle="Øverste verktøylinje inne i en skymappe" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Mappealternativer

Når du åpner en mappe i appen, finner du et praktisk sett med handlinger tilgjengelig ved å trykke på "..."-knappen øverst til høyre på skjermen.   
Her er en oversikt over disse handlingene:

- **Velge**: Aktiver filvalg-modus. Denne modusen lar deg velge en eller flere filer i mappen, noe som gjør det enkelt å utføre handlinger på valgte elementer.
- **Ny mappe**: Opprett en ny mappe i gjeldende mappe. Denne funksjonen lar deg organisere filene dine og holde biblioteket ditt godt strukturert.
- **Aktiver offline-modus**: Slå på offline-modus for gjeldende mappe. Offline-modus går utover enkel nedlasting; den overvåker aktivt mappen for endringer. Hvis du legger til nye filer i mappen online, vil appen automatisk laste ned disse filene til enheten din. Dette sikrer at det lokale biblioteket ditt holder seg oppdatert med endringer på serveren.
- **Last opp filer**: Last opp filer fra enheten til den online-mappen. Denne handlingen lar deg overføre filer til skyen eller serveren, noe som gjør dem tilgjengelige fra hvor som helst.
- **Søk**: Søk etter bestemte filer i gjeldende mappe. Dette er spesielt nyttig for å raskt finne bestemte elementer i en stor samling.
- **Sorter**: Sorter filer i mappen etter kriterier som navn, størrelse eller redigeringsdato. Standard sorteringsmodus speiler vanligvis sorteringsrekkefølgen på serveren, men du kan endre den til å passe dine preferanser.
- **Rutenett/Listevisning**: Bytt mellom to visningsmoduser: tabellvisning og miniatyrvisning. Tabellvisningen presenterer filer i en liste, mens miniatyrvisningen viser visuelle representasjoner av filene, noe som gjør det lettere å identifisere innhold med et blikk.

{{< cards cols="1">}}
  {{< card title="" subtitle="Gjeldende mappe flere handlinger-meny" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Rediger online-filer

Når du trenger å administrere flere filer i skylagringen din på Evermusic, kan du bruke valgmodus for å effektivisere handlingene dine. Følg disse trinnene for effektiv filbehandling:

- **Aktiver valgmodus**: Åpne appen på enheten og naviger til seksjonen som inneholder skylagringen din. Se øverst til høyre der du finner "..."-knappen (ellipsis). Trykk på den og velg menyelementet "Velge" for å aktivere valgmodus.
- **Velg filer**: Du vil se avmerkingsbokser som vises ved siden av alle opplistede filer eller mapper. Velg en eller flere filer eller mapper ved enkelt å trykke på avmerkingsboksene ved siden av dem.
- **Utfør ulike handlinger**: Når du har valgt filene eller mappene du vil administrere, har du tilgang til flere handlinger tilpasset dine behov:

{{< cards cols="1">}}
  {{< card title="" subtitle="Valgmodus for online-filer" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Filhandlinger

Nær tittelen på filen vil du se et ellipsesymbol "..." (tre prikker) – dette er handlingsmenyen.  
Trykk på den for å avsløre en liste over tilgjengelige handlinger:

- **Spill neste**: Velg denne handlingen for å sette den valgte filen øverst i spillerkøen, og sikre at den spilles umiddelbart etter det som spilles nå.
- **Spill senere**: Å velge dette alternativet legger til filen nederst i spillerkøen, slik at den spilles etter den eksisterende køen.
- **Legg til musikkbibliotek**: Denne handlingen lar deg inkorporere filen i musikkbiblioteket ditt, noe som gjør det lett tilgjengelig og ryddig organisert etter artist, album, sjanger eller komponist.
- **Legg til en spilleliste**: Bruk denne handlingen for å legge til filen i en eksisterende spilleliste eller opprette en ny.
- **Rediger lydtagger**: Ved å velge dette alternativet får du tilgang til Evermusics innebygde tag-redigerer, som lar deg endre lydtagger for den valgte filen. Filen vil bli midlertidig lastet ned til en midlertidig katalog og deretter lastet opp til lagringen etter at du bekrefter endringene.
- **Legg til favoritter**: Denne handlingen legger til filen i listen over favoriettfiler for rask og praktisk tilgang.
- **Laste ned**: Velg denne handlingen for å laste ned filen eller mappen til enheten, noe som gjør den tilgjengelig for offline bruk.
- **Gi nytt navn**: Dette alternativet lar deg gi nytt navn til filen direkte på fjernlagringen, noe som tillater tilpasset filnavngivning.
- **Flytt**: Velg denne handlingen for å flytte filen til en annen mappe i skylagringen, noe som hjelper med å opprettholde en organisert filstruktur.
- **Åpne i**: Bruk denne handlingen for å eksportere filen til en annen kompatibel app. Filen vil bli lastet ned til enheten, og deretter vil Delingsdialoget vises for videre deling eller interaksjon.
- **Slette**: Vær forsiktig med denne handlingen, da den permanent fjerner filen fra skylagringen. Denne slettingen kan ikke angres.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flere handlinger-meny for én enkelt fil" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Hvis listen over handlinger overskrider tilgjengelig skjermlass, bla ganske enkelt ned i handlingsmenyen for å få tilgang til ytterligere alternativer.

## Mappehandlinger

For hver mappe i skylagringen har du ulike handlinger tilgjengelig. For å få tilgang til disse alternativene, trykk ganske enkelt på ellipseikonet "..." ved siden av maptittelen. Hvis du ikke ser alle handlingene, bla ned for å avsløre flere valg. Her er de tilgjengelige handlingene:

- **Spill alle**: Erstatt den gjeldende spillerkøen med alle elementer fra den valgte mappen.
- **Spill neste**: Legg til hele mappen øverst i spillerkøen, rett etter det som spilles nå.
- **Spill senere**: Legg til mappeinnholdet nederst i spillerkøen.
- **Legg til musikkbibliotek**: Denne handlingen inkorporerer mappeinnholdet sømløst i musikkbiblioteket ditt, noe som gjør det lett tilgjengelig og ryddig organisert etter artist, album, sjanger eller komponist.
- **Legg til spilleliste**: Du kan inkludere hele mappen i en spilleliste. Du har også muligheten til å opprette en ny spilleliste, og mappens navn vil bli automatisk tildelt.
- **Legg til favoritter**: Bruk denne handlingen for å legge til mappen i listen over favoriettfiler for rask og praktisk tilgang.
- **Aktiver offline-modus**: Ved å aktivere offline-modus for en valgt mappe, går applikasjonen utover enkel nedlasting. Den skanner kontinuerlig etter endringer, og hvis nye filer legges til i online-mappen, vil de automatisk bli lastet ned til appen.
- **Laste ned**: Last ned alt innholdet i mappen til enheten for offline-tilgang.
- **Gi nytt navn**: Gi nytt navn til mappen direkte på fjernlagringen.
- **Flytt**: Flytt mappen til et annet sted i skylagringen.
- **Slette**: Vær forsiktig med denne handlingen da den permanent fjerner mappen og innholdet fra skylagringen. Denne handlingen kan ikke angres.


## Hurtig tilgang

Seksjonen Hurtig tilgang er plassert øverst på skjermen. Den gir deg rask tilgang til favoriett- og nylig åpnede filer fra tilkoblede skytjenester.
Hver gang du åpner en fil eller mappe fra skyen, legges den til i listen "Nylig åpnet". For å slette denne listen, åpne "Nylige", trykk på "Flere handlinger"-knappen og velg "Slett liste." Du kan også merke dypt nestede mapper som Favoritter for å få rask tilgang til dem uten å grave gjennom katalogstrukturen.

## Andre tjenester

Denne seksjonen viser ekstra funksjoner som forbedrer opplevelsen din. For øyeblikket støtter appen Last.fm-scrobbling. Når tilkoblet, sendes avspillingsstatistikken din automatisk til Last.fm-kontoen din. Du kan besøke Last.fm-profilen din senere for å se lytteanalyse og få personaliserte musikkanbefalinger. Detaljerte oppsettinstruksjoner er tilgjengelige [her](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
