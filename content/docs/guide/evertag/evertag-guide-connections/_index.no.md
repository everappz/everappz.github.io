---
title: "Tilkoblinger"
date: 2020-02-01
description: "Lær hvordan du kobler skylagring, NAS og datamaskinen din til Evertag. Få tilgang til og rediger lydfiler direkte fra skylagring, personlig NAS eller Mac/PC."
keywords: [
  "Evertag sky-oppsett", "koble iCloud til Evertag", "SMB filtilgang iOS",
  "WebDAV lyd-tag-editor", "NAS metadata-redigering", "Wi-Fi Drive Evertag",
  "overfør lydfiler til iPhone", "Evertag iTunes File Sharing", "rediger FLAC-tagger fra sky"
]
tags: ["veiledning", "evertag", "tilkoblinger"]
readingTime: 11
---


På dette skjermbildet kan du koble til ulike kilder som inneholder lydfilene dine. Du kan integrere populære skytjenester som Google Drive, Dropbox, OneDrive, iCloud og andre, samt koble til Mac eller PC. I tillegg har du muligheten til å redigere lydfiler i Apple Time Capsule, WD Cloud Home eller en NAS som støtter SMB eller WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tilkoblinger-skjerm" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Hurtigtilgang

Øverst på Tilkoblinger-skjermen finner du en liste for **Hurtigtilgang**. Enhver skymappe du legger til i favoritter — selv en som er mange nivåer dypt — vises her slik at du kan hoppe til den uten å navigere gjennom overordnede mapper hver gang.

## Koble til skylagring

- Åpne 'Tilkoblinger'-fanen  
- Velg 'Koble til skylagring' fra menyen  
- Velg en skylagringstjeneste fra listen  
- Skriv inn påloggingsinformasjonen din, og trykk 'Ferdig.'

Hvis du støter på problemer, må du sjekke internettforbindelsen og brukernavn/passord.  
I Premium-versjonen av appen kan du legge til et ubegrenset antall tjenester.

## Støttede skylagringstjenester

For øyeblikket støtter applikasjonen de mest populære skylagringstjenestene: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), samt enhver SMB- eller WebDAV-server.

## Sikkerhet og personvern

Vi bruker kun offisielle SDK-er og sikre forbindelser for å kommunisere med tilkoblede skytjenester. Brukernavnet og passordet ditt er ikke tilgjengelig for applikasjonen. Alle forespørsler fra applikasjonen til skytjenesten er kryptert.

Når du skriver inn brukernavn og passord, viser applikasjonen den offisielle autorisasjonssiden fra skyetjenesteleverandøren, og hele autorisasjonsprosessen foregår utenfor applikasjonen. Skytjenesteleverandøren sender et auth-token til applikasjonen etter vellykket autorisasjon, og det tokenet brukes til å foreta API-kall.

Et auth-token er en digital nøkkel som lar tredjepartsapplikasjoner kommunisere med skylagring. Auth-tokenet er lagret på enheten din i et sikkert systemlager kalt Keychain. Du kan laste ned filer fra den tilkoblede skytjenesten til enheten, og disse filene vil bli plassert i appens "Dokumenter"-katalog. Du kan fjerne disse filene når som helst ved hjelp av den innebygde filbehandleren.

Applikasjonen deler ingen informasjon fra den tilkoblede skykontoen. Du kan tilbakekalle tilgangen til skykontoen din når som helst ved å åpne kontoinnstillingssiden i nettleseren din.

## Avvise auth-token

Logg inn på kontoen din i en nettleser og naviger til innstillingssiden. Der kan du finne alle tredjepartsapper som er tilkoblet skykontoen din og fjerne dem du ikke lenger vil bruke. Detaljerte instruksjoner er tilgjengelige [her](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan også koble fra de tilkoblede skykontoene i applikasjonen, og auth-tokenet vil også bli fjernet fra enheten din. Hvis du fjerner applikasjonen fra enheten din, vil alle nedlastede data og tilgangstokener også fjernes.

## Koble fra skylagring eller endre konfigurasjon

- Tilgang til skylagringsalternativer: Finn først skylagringen du vil administrere i appens grensesnitt.  
- Trykk på '...'-knappen: Ved siden av tjenestetittelen ser du en '...'-knapp. Trykk på den for å få tilgang til flere alternativer.  
  - **Gi nytt navn**: Hvis du vil endre navnet på skytjenesten slik den vises i listen din, velger du 'Gi nytt navn.'  
  - **Innstillinger**: For å endre konfigurasjonen eller autentiseringsdata for skytjenesten, velger du 'Innstillinger.' Noen ganger må du autorisere den tilkoblede skytjenesten på nytt hvis autorisasjonstokenet har utløpt.  
  - **Koble fra**: Hvis du ønsker å fullstendig avbryte forbindelsen mellom appen og skytjenesten, velger du 'Koble fra.' Vær oppmerksom på at dette alternativet vil fjerne alle sanger tilknyttet denne skytjenesten fra appens musikkbibliotek, men de vil forbli på serveren.

## Koble til datamaskin eller NAS

Du kan også koble til datamaskinen din, personlig NAS eller andre nettverksenheter ved hjelp av SMB-, DLNA- eller WebDAV-protokollen.

## Koble til datamaskin med SMB

- Trykk på "Koble til skylagring" → SMB.  
- Skriv inn datamaskinens IP-adresse og navn på delt mappe i URL-feltet med formatet smb://datamaskin-ip-adresse/delt-mappe-navn  
- Velg protokollversjon: Auto, SMB1, SMB2  
- Skriv inn brukernavn og passord (hvis nødvendig)  
- Trykk på "Ferdig."

Hvis tilkoblingen er vellykket, vil du se den tilkoblede lagringen i "Skylagring"-seksjonen.  
En fullstendig veiledning om hvordan du kobler Mac eller PC ved hjelp av SMB er tilgjengelig [her](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Koble til NAS med WebDAV

Alle trinnene er de samme bortsett fra URL-feltet.  
URL-en skal være i formatet http://servernavn, eller https://servernavn hvis serveren støtter SSL.  
En fullstendig veiledning om hvordan du kobler NAS ved hjelp av WebDAV-protokollen er tilgjengelig [her](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Tilgjengelige enheter

Denne seksjonen viser alle enheter i det lokale nettverket ditt som du kan koble til via applikasjonen.  
Følg disse trinnene for å opprette en tilkobling med en enhet:

- Åpne appen og gå til "Tilgjengelige enheter"-seksjonen.  
- Trykk på enheten du vil koble til fra listen.  
- Skriv om nødvendig inn påloggingsinformasjonen din for å fullføre tilkoblingen.

## Wi-Fi Drive 

Wi-Fi Drive er en praktisk teknologi som muliggjør trådløs filoverføring fra datamaskinen din til iOS-enheten via en skrivebordsnettleser.  
For å bruke denne funksjonen effektivt, sørg for at enheten og datamaskinen er koblet til det samme Wi-Fi-nettverket.  
Her er en trinnvis veiledning for bruk av Wi-Fi Drive.

## Aktiver Wi-Fi Drive

- Åpne applikasjonen og gå til "Tilkoblinger"-fanen.  
- Velg "Koble til via Wi-Fi" for å gå til Wi-Fi Drive-hovedskjermen.  
- Trykk på "Start Wi-Fi Drive" for å aktivere Wi-Fi Drive.

## Tilgang til Wi-Fi Drive på datamaskinen din

- På datamaskinen din (stasjonær eller bærbar), åpne en nettleser (som Chrome, Firefox eller Safari).  
- Skriv inn URL-en gitt av applikasjonen i adressefeltet til nettleseren.

## Overfør filer trådløst

Når nettsiden som tilsvarer iOS-enheten din åpnes i nettleseren, kan du enkelt dra og slippe filer fra datamaskinen til nettsiden.  
Filene du drar og slipper vil begynne å overføres til iOS-enheten din og vil være tilgjengelige i applikasjonen.

Detaljerte instruksjoner om hvordan du overfører filer trådløst ved hjelp av Wi-Fi Drive er tilgjengelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing er en annen teknologi som lar deg overføre filer fra en datamaskin til en enhet ved hjelp av Finder-appen på Mac og en Lightning-kabel.  
- Bare koble enheten til datamaskinen med en kabel og kjør Finder-appen på Mac-en din.  
- Åpne "Steder" → "Den tilkoblede enheten" → "Filer" → og finn den gjeldende appen.  
- Trykk på appens ikon for å se alle delte mapper.  
- Kopier filer fra datamaskinen til den delte mappen på enheten ved å dra og slippe.

Detaljerte instruksjoner om hvordan du bruker iTunes File Sharing er tilgjengelige [her](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Koble til et USB-flashkort

Hvis du har et SD-kort eller en USB-pinne, kan du koble det til ved hjelp av en Lightning- eller USB-C-kortleser på iPhone/iPad, eller plugge det direkte inn i en Mac. Appen støtter for øyeblikket Apple-sertifiserte kortlesere. Vi har detaljerte instruksjoner om hvordan du kobler et USB-flashkort til iPhone eller iPad og administrerer filer på det, tilgjengelig [her](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Tilkoblede stasjoner vises i **Eksternt tilbehør**-seksjonen på Tilkoblinger-skjermen.

## Filbehandler

Når du har koblet til en skylagringstjeneste, trykker du på ikonet for å se alle tilgjengelige filer og mapper. Du kan bruke den innebygde filbehandleren til å arbeide med disse filene — laste ned, gi nytt navn, flytte og mer. Når du starter en nedlasting, vil filen vises i overføringskøen. For å se overføringskøen, gå til "Lokale filer"-fanen og trykk på de roterende pilene i øvre venstre hjørne. Alle nedlastede filer og mapper er tilgjengelige i "Lokale filer"-seksjonen.

## Øverste verktøylinje

Den øverste verktøylinjen, som er plassert under navigasjonslinjen, tilbyr flere nyttige handlinger for enkel tilgang. Du kan vise eller skjule denne verktøylinjen ved å bruke et enkelt sveipgestur nedover. Her er de tilgjengelige handlingene:

- **Søk**: Dette alternativet lar deg utføre et raskt søk i den gjeldende katalogen, noe som gjør det enkelt å finne spesifikke filer eller mapper.  

## Mappealternativer

Når du åpner en mappe i appen, finner du et praktisk sett med handlinger tilgjengelig ved å trykke på "..."-knappen øverst i høyre hjørne av skjermen.  
Her er en beskrivelse av disse handlingene:

- **Velge**: Aktiver filvalg-modus. Denne modusen lar deg velge én eller flere filer i mappen, noe som gjør det enkelt å utføre handlinger på valgte elementer.  
- **Ny mappe**: Opprett en ny mappe i den gjeldende mappen. Denne funksjonen lar deg organisere filene dine og holde biblioteket godt strukturert.   
- **Last opp filer**: Last opp filer fra enheten til den nettbaserte mappen. Denne handlingen lar deg overføre filer til skyen eller serveren, noe som gjør dem tilgjengelige fra hvor som helst.  
- **Søk**: Søk etter spesifikke filer i den gjeldende mappen. Dette er spesielt nyttig for raskt å finne spesifikke elementer i en stor samling.  
- **Sorter**: Sorter filer i mappen etter kriterier som navn, størrelse eller redigeringsdato. Standard sorteringsmodus speiler vanligvis sorteringsrekkefølgen på serveren, men du kan endre den etter dine preferanser.  
- **Rutenett/Listevisning**: Bytt mellom to visningsmoduser: tabellvisning og miniatyrbildevisning. Tabellvisningen presenterer filer i en liste, mens miniatyrbildevisningen viser visuelle representasjoner av filene, noe som gjør det enklere å identifisere innhold med et blikk.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Skymappe Sorter" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Rediger nettfiler

Når du trenger å administrere flere filer i skylagringen din i denne appen, kan du bruke valgmodus for å strømlinjeforme handlingene dine. Følg disse trinnene for effektiv filbehandling:

- **Aktiver valgmodus**: Åpne appen på enheten din og naviger til seksjonen som inneholder skylagringen din. Se etter øvre høyre hjørne der du finner "..." (ellipse)-knappen. Trykk på den og velg "Velge"-menyelementet for å aktivere valgmodus.  
- **Velg filer**: Du vil legge merke til at det vises avmerkingsbokser ved siden av alle filer eller mapper som er listet opp. Velg én eller flere filer eller mapper ved å trykke på avmerkingsboksene ved siden av dem.  
- **Utfør ulike handlinger**: Når du har valgt filene eller mappene du vil administrere, vil du ha tilgang til flere handlinger tilpasset dine behov:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Velg fil" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Filhandlinger

Nær tittelen til filen vil du legge merke til et ellipsetegn "..." (tre punkter) – dette fungerer som handlingsmenyen.  
Trykk på det for å vise en liste over tilgjengelige handlinger:

- **Redigere lydtagger**: Ved å velge dette alternativet kan du få tilgang til den innebygde tag-editoren, slik at du kan endre lyd-tagger for den valgte filen. Filen vil midlertidig lastes ned til en midlertidig katalog og deretter lastes opp til lagringen etter at du bekrefter endringene.  
- **Legg til i Favoritter**: Denne handlingen legger til filen i listen over favorittefiler for rask og praktisk tilgang.  
- **Laste ned**: Velg denne handlingen for å laste ned filen eller mappen til enheten din, noe som gjør den tilgjengelig for offline bruk.  
- **Gi nytt navn**: Dette alternativet tillater deg å gi nytt navn til filen direkte på den eksterne lagringen, noe som muliggjør tilpasset filnavngivning.  
- **Flytt**: Velg denne handlingen for å flytte filen til en annen mappe i skylagringen din, noe som hjelper med å opprettholde en organisert filstruktur.  
- **Åpne i**: Bruk denne handlingen for å eksportere filen til en annen kompatibel app. Filen vil bli lastet ned til enheten din, og deretter vil Dele-dialogen vises for videre deling eller interaksjon.  
- **Slette**: Vær forsiktig med denne handlingen, da den permanent fjerner filen fra skylagringen din. **Denne slettingen kan ikke angres**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Filalternativer" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Hvis handlingslisten overskrider den tilgjengelige skjermplassen, blar du bare ned i handlingsmenyen for å få tilgang til flere alternativer.

## Mappehandlinger

For hver mappe i skylagringen din er det ulike handlinger tilgjengelige. For å få tilgang til disse alternativene, trykker du bare på ellipseikonet "..." ved siden av maptittelen. Hvis du ikke ser alle handlingene, blar du ned for å vise flere alternativer. Her er de tilgjengelige handlingene:

- **Legg til i Favoritter**: Bruk denne handlingen for å legge til mappen i listen over favorittefiler for rask og praktisk tilgang.  
- **Laste ned**: Last ned alt innholdet i mappen til enheten din for offline tilgang.  
- **Gi nytt navn**: Gi nytt navn til mappen direkte på den eksterne lagringen.  
- **Flytt**: Flytt mappen til en annen plassering i skylagringen din.  
- **Slette**: Vær forsiktig med denne handlingen, da den permanent fjerner mappen og innholdet fra skylagringen din. **Denne handlingen kan ikke angres**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Mappealternativer" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
