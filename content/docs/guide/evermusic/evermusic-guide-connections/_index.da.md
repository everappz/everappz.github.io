---
title: "Forbindelser"
date: 2020-01-01
description: "Lær at tilslutte cloud-tjenester, computere, NAS-enheder og administrere dine musikfiler med Evermusic. Trin-for-trin guide til Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes-fildeling med mere."
keywords: [
  "Evermusic", "cloud-musikafspiller", "NAS-streaming", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes-fildeling",
  "tilslut cloud-lagring", "musikoverførsel iPhone", "filmanager iOS"
]
tags: ["evermusic", "guide", "connections"]
readingTime: 11
---


På skærmen Forbindelser kan du tilslutte alle kilder, der indeholder din musik — populære cloud-tjenester, selvhostede medieservere, din Mac eller pc, en personlig NAS, Apple Time Capsule, WD My Cloud Home, endda et USB-flashdrev — og bruge dem alle fra én samlet brugerflade. Forbindelser er også, hvor du opsætter Hurtig adgang til dybt indlejrede cloud-mapper, og hvor du godkender Last.fm til scrobbling.

Skærmen er opdelt i tydeligt mærkede sektioner, så den skalerer fra en enkelt iCloud Drive-konto til et bibliotek spredt over flere skyer og NAS-enheder: Hurtig adgang øverst (dine foretrukne cloud-mapper), Cloud-lagring (de konti, du har tilføjet), Lokalt netværk (Bonjour-opdagede enheder), Computer (Wi-Fi Drive, iTunes-fildeling, SMB), Eksternt tilbehør (tilsluttede USB-flashdrev) og Andre tjenester (Last.fm og lignende).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Forbindelser-skærm" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Tilslut til cloud-lagring

- Åbn fanen Forbindelser.
- Vælg Tilslut til cloud-lagring fra menuen.
- Vælg en cloud-lagringstjeneste fra listen.
- Log ind på udbyderens officielle autorisationsside (Evermusic ser aldrig din adgangskode).
- Tryk på Færdig.

{{< cards cols="1">}}
  {{< card title="" subtitle="Vælger til tilslutning af cloud-lagringudbyder" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Hvis du støder på problemer, skal du dobbelttjekke din internetforbindelse og loginoplysninger og sørge for, at tofaktorautentificering er korrekt konfigureret for den pågældende tjeneste.  
I Premium-versionen af appen kan du tilføje et ubegrænset antal tjenester. Gratis brugere kan tilslutte én cloud-konto ad gangen.

## Understøttede cloud-lagringstjenester

Evermusic understøtter hele udvalget af populære cloud- og selvhostede tjenester. Gratis brugere får det samme udbyderkatalog, men med grænsen på én konto; Premium låser op for ubegrænsede konti og fjerner de fleste andre begrænsninger.

- **Personlige cloud-konti:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Selvhostede servere og mediebiblioteker:** Plex · Jellyfin · Emby · Subsonic (og alle Subsonic-kompatible servere — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (og Owncloud, via den delte API) · Synology Drive · QNAP.
- **NAS og fildelingsprotokoller:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (adgangskode- eller offentlig nøglegodkendelse), NFS og DLNA (skrivebeskyttet — afspilning og download).
- **S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage eller ethvert S3 API-slutpunkt.
- **Lokalt netværksopdagelse:** sektionen Tilgængelige enheder viser automatisk alle enheder på din Wi-Fi, der annoncerer sig selv via Bonjour/mDNS — Plex, Jellyfin, Emby-servere, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, AirPort-routere med tilsluttede drev og så videre.

## Sikkerhed og privatliv

Vi bruger kun officielt SDK og sikker forbindelse til at interagere med tilsluttede cloud-tjenester. Dit brugernavn og din adgangskode er ikke tilgængelige for applikationen. Alle forespørgsler fra applikationen til cloud-tjenesten er krypteret.

Når du indtaster dit brugernavn og din adgangskode, viser applikationen den officielle autorisationsside fra cloud-tjenesteudbyderen, og al autorisationsprocessen foregår uden for applikationen. Cloud-tjenesteudbyderen sender en auth-token til applikationen efter vellykket autorisering, og denne token bruges til API-kald.

Auth-token er en digital nøgle, der giver tredjepartsapplikationer mulighed for at interagere med cloud-lagring. Auth-token gemmes på din enhed i et sikkert systemlager kaldet Keychain. Du kan downloade dine filer fra den tilsluttede cloud-tjeneste til enheden, og disse filer vil blive placeret i appens "Dokumenter"-mappe. Du kan fjerne disse filer til enhver tid ved hjælp af den indbyggede filmanager.

Applikationen deler ingen oplysninger fra den tilsluttede cloud-konto. Du kan tilbagekalde adgang til din cloud-konto til enhver tid ved at åbne kontoindstillingssiden i din webbrowser.

## Afvis auth-token

Log ind på din konto i webbrowseren og naviger til indstillingssiden. Der kan du finde alle tredjepartsapps, der er tilsluttet din cloud-konto, og fjerne dem, hvis du ikke vil bruge den pågældende applikation længere. Detaljerede instruktioner er tilgængelige [her](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan også frakoble de tilsluttede cloud-konti i applikationen, og auth-token vil også blive fjernet fra din enhed. Hvis du fjerner applikationen fra din enhed, fjernes alle downloadede data og adgangstokens også.

## Frakobl en cloud-lagring eller skift konfiguration

- Adgang til indstillinger for cloud-lagring: find først den cloud-lagring, du vil administrere, i appens brugerflade.
- Tryk på "..."-knappen: ved siden af tjenestenavnet vil du se en "..."-knap. Tryk på den for at få adgang til yderligere indstillinger.
  - **Omdøb**: hvis du vil ændre navnet på cloud-tjenesten, som det vises på din liste, skal du vælge "Omdøb".
  - **Indstillinger**: for at ændre konfiguration eller godkendelsesdata for cloud-tjenesten skal du vælge "Indstillinger". Til tider kan du have behov for at genautentificere den tilsluttede cloud-tjeneste, hvis autorisationstokenet er udløbet.
  - **Frakoble**: hvis du vil fuldstændig afbryde forbindelsen mellem appen og cloud-tjenesten, skal du vælge "Frakoble". Vær opmærksom på, at valg af denne mulighed vil fjerne alle sange, der er knyttet til denne cloud-tjeneste, fra appens musikbibliotek, men de forbliver på serveren.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu med Flere handlinger for tilsluttet cloud-lagring" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Tilslut til Computer eller NAS

Du kan også tilslutte din computer, personlige NAS eller andre netværksenheder ved hjælp af SMB, DLNA eller WebDAV-protokol.

## Tilslut til computer med SMB

- Tryk på "Tilslut til cloud-lagring" → SMB.
- Indtast computerens IP-adresse og delt mappenavn i URL-feltet i formatet smb://computer-ip-adresse/delt-mappenavn
- Vælg protokolversion: Auto, SMB1, SMB2
- Indtast brugernavn og adgangskode (hvis påkrævet)
- Tryk på "Færdig".

Hvis din forbindelse er vellykket, vil du se tilsluttet lagring i sektionen "Cloud-lagring".  
En komplet vejledning om, hvordan du tilslutter din Mac eller pc med SMB, er tilgængelig [her](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB-forbindelsesindstillinger" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Tilslut til NAS med WebDAV

Alle trin er de samme, bortset fra URL-feltet.  
URL skal være i formatet http://servernavn eller https://servernavn, hvis serveren understøtter SSL.
En komplet vejledning om, hvordan du tilslutter NAS med WebDAV-protokol, er tilgængelig [her](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV-forbindelsesindstillinger" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Tilslut til Computer eller NAS med DLNA

Du kan også dele et musikbibliotek på din Windows-pc eller personlige NAS ved hjælp af DLNA-protokollen og få adgang til det bibliotek i appen som beskrevet [her](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA er en populær og meget brugt protokol, men den giver dig kun mulighed for at afspille eller downloade musik. Du kan ikke uploade filer eller oprette nye mapper på serveren.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA-forbindelsesindstillinger" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Tilgængelige enheder

Denne sektion viser alle enheder på dit lokale netværk, som du kan oprette forbindelse til via applikationen.  
Følg disse trin for at etablere en forbindelse med en enhed:

- Åbn appen og gå til sektionen "Tilgængelige enheder".
- Tryk på den enhed, du vil oprette forbindelse til, fra listen.
- Indtast om nødvendigt dine loginoplysninger for at fuldføre forbindelsen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tilgængelige enheder på det lokale netværk" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive er en praktisk teknologi, der muliggør trådløse filoverførsler fra din computer til din iOS-enhed via en desktopbrowser.  
For at bruge denne funktion effektivt skal du sørge for, at din enhed og computer er tilsluttet det samme Wi-Fi-netværk.  
Her er en trin-for-trin guide til, hvordan du bruger Wi-Fi Drive.

## Aktiver Wi-Fi Drive

- Åbn applikationen og gå til fanen "Forbindelser".
- Vælg "Tilslut via Wi-Fi" for at få adgang til Wi-Fi Drive-startskærmen.
- Tryk på "Start Wi-Fi Drive" for at aktivere Wi-Fi Drive.

## Adgang til Wi-Fi Drive på din computer

- Åbn en webbrowser (som Chrome, Firefox eller Safari) på din computer (desktop eller laptop).
- Indtast den URL, som applikationen giver, i browserens adresselinje.

## Overfør filer trådløst

Når den webside, der svarer til din iOS-enhed, åbner i browseren, kan du nemt trække og slippe filer fra din computer til websiden.  
De filer, du trækker og slipper, begynder at overføre til din iOS-enhed og vil være tilgængelige i applikationen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive serverindstillinger" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Detaljerede instruktioner om, hvordan du overfører filer trådløst ved hjælp af WiFi-Drive, er tilgængelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes-fildeling

iTunes-fildeling er en anden teknologi, der giver dig mulighed for at overføre filer fra computer til enhed ved hjælp af Finder-appen på din Mac og et lightning-kabel.  
- Tilslut blot en enhed til computeren med et kabel og kør Finder-appen på din Mac.
- Åbn "Placeringer" → "Din tilsluttede enhed" → "Filer" → og find Evermusic-appen.
- Tryk på app-ikonet for at se alle delte mapper.
- Kopiér filer fra computeren til den delte mappe på enheden ved hjælp af træk og slip.

Detaljerede instruktioner om, hvordan du bruger iTunes-fildeling, er tilgængelige [her](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder fildeling på Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Tilslut et USB-flashkort

Hvis du har et SD-kort, kan du tilslutte det ved hjælp af en lightning-kortlæser. Appen understøtter i øjeblikket Apple Certified kortlæsere og iXpand Flash Drives. Hvis du har iXpand Flash Drive — indsæt det i lightning-porten og åbn applikationen. Du vil se en besked om "Ekstern enhed tilsluttet" og enhedsoplysninger. Tryk blot på flashdrev-ikonet for at få adgang til musikmappen og tryk på en lydfil for at starte afspilning. Vi har detaljerede instruktioner om, hvordan du tilslutter et USB-flashkort til iPhone og lytter til musik eller administrerer filer på det, som er tilgængelige [her](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Filmanager

Når du har tilsluttet en cloud-lagringstjeneste, skal du trykke på dens ikon for at se alle tilgængelige filer og mapper. Du kan bruge den indbyggede filmanager til at arbejde med disse filer — downloade, omdøbe, flytte med mere. Når du starter en download, vises filen i overførselskøen. For at se overførselskøen skal du gå til fanen "Lokale filer" og trykke på de snurrende pile øverst til venstre. Alle downloadede filer og mapper er tilgængelige i sektionen "Lokale filer".

## Øverste værktøjslinje

Den øverste værktøjslinje, der er bekvemt placeret under navigationslinjen, tilbyder flere nyttige handlinger for nem adgang. Du kan vise eller skjule denne værktøjslinje ved hjælp af en simpel stryg-nedad-gestus. Her er de tilgængelige handlinger:

- **Søg**: Denne mulighed giver dig mulighed for at udføre en hurtig søgning i den aktuelle mappe, så det er nemt at finde specifikke filer eller mapper.
- **Fortsæt afspilning**: Hvis aktiveret i applikationsindstillingerne, gendanner denne funktion lydafspillerkøen og den seneste medieposition for den aktuelle mappe. Det er en praktisk måde at fortsætte, hvor du slap i dit musikbibliotek.
- **Afspil alle**: Ved at vælge denne handling vil appen scanne den aktuelle mappe og dens undermapper og tilføje alle fundne lydfiler til en ny afspillerkø. Dette er nyttigt, når du vil afspille al musik i en bestemt mappe.
- **Bland alle**: I lighed med "Afspil alle" scanner denne handling den aktuelle mappe og dens undermapper, men blander filerne, inden de tilføjes til lydafspillerkøen. Det er en god måde at nyde din musik i tilfældig rækkefølge for lidt variation.

{{< cards cols="1">}}
  {{< card title="" subtitle="Øverste værktøjslinje inde i en cloud-mappe" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Mappeindstillinger

Når du åbner en mappe i appen, finder du et praktisk sæt handlinger tilgængeligt ved at trykke på "..."-knappen øverst til højre på skærmen.  
Her er en oversigt over disse handlinger:

- **Vælg**: Aktiver filvalgtilstand. Denne tilstand giver dig mulighed for at vælge en eller flere filer i mappen, hvilket gør det nemt at udføre handlinger på valgte elementer.
- **Ny mappe**: Opret en ny mappe i den aktuelle mappe. Denne funktion giver dig mulighed for at organisere dine filer og holde dit bibliotek velstruktureret.
- **Aktivere offline-tilstand**: Slå offline-tilstand til for den aktuelle mappe. Offline-tilstand går ud over blot at downloade; den overvåger aktivt mappen for ændringer. Hvis du tilføjer nye filer til mappen online, downloader appen automatisk disse filer til din enhed. Dette sikrer, at dit lokale bibliotek holdes opdateret med ændringer på serveren.
- **Upload filer**: Upload filer fra din enhed til den online mappe. Denne handling lader dig overføre filer til skyen eller serveren og gøre dem tilgængelige overalt.
- **Søg**: Søg efter specifikke filer i den aktuelle mappe. Dette er især nyttigt til hurtigt at finde specifikke elementer i en stor samling.
- **Sorter**: Sorter filer i mappen efter kriterier som navn, størrelse eller redigeringsdato. Standardsorteringstilstanden afspejler typisk sorteringsrækkefølgen på serveren, men du kan ændre den efter dine præferencer.
- **Gitter/Liste**: Skift mellem to visningstilstande: tabelvisning og miniaturevisning. Tabelvisningen præsenterer filer som en liste, mens miniaturevisningen viser visuelle repræsentationer af filerne og gør det lettere at identificere indhold med et blik.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu med Flere handlinger for aktuel mappe" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Rediger online filer

Når du har brug for at administrere flere filer i din cloud-lagring på Evermusic, kan du bruge valgstilstand til at strømline dine handlinger. Følg disse trin for effektiv filhåndtering:

- **Aktiver valgstilstand**: Åbn appen på din enhed og naviger til sektionen med din cloud-lagring. Kig i øverste højre hjørne, hvor du finder "..."-knappen (ellipsis). Tryk på den og vælg menupunktet "Vælg" for at aktivere valgstilstand.
- **Vælg filer**: Du vil bemærke afkrydsningsfelter, der vises ved siden af hver fil eller mappe på listen. Vælg en eller flere filer eller mapper ved blot at trykke på afkrydsningsfelterne ved siden af dem.
- **Udfør forskellige handlinger**: Når du har valgt de filer eller mapper, du vil administrere, har du adgang til flere handlinger, der er tilpasset dine behov:

{{< cards cols="1">}}
  {{< card title="" subtitle="Valgstilstand for online filer" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Filhandlinger

Nær filnavnet vil du se et ellipsis-symbol "..." (tre prikker) — dette fungerer som handlingsmenuen.  
Tryk på det for at afsløre en liste over tilgængelige handlinger:

- **Afspil næste**: Vælg denne handling for at indsætte den valgte fil øverst i din afspillerkø og sikre, at den afspilles umiddelbart efter det aktuelt afspillede element.
- **Afspil senere**: Valg af denne mulighed tilføjer filen til bunden af din afspillerkø og sikrer, at den afspilles efter den eksisterende kø.
- **Tilføj til musikbibliotek**: Denne handling lader dig inkorporere filen i dit musikbibliotek og gøre den let tilgængelig og pænt organiseret efter kunstner, album, genre eller komponist.
- **Tilføj til en afspilningsliste**: Brug denne handling til at tilføje filen til en eksisterende afspilningsliste eller oprette en ny.
- **Redigere lydtags**: Ved at vælge denne mulighed kan du få adgang til Evermusics indbyggede tageditor, der giver dig mulighed for at ændre lydtags for den valgte fil. Filen vil midlertidigt blive downloadet til en midlertidig mappe og derefter uploadet til lagringen, efter du bekræfter ændringerne.
- **Tilføj til favoritter**: Denne handling tilføjer filen til din liste over favoritfiler for hurtig og bekvem adgang.
- **Downloade**: Vælg denne handling for at downloade filen eller mappen til din enhed og gøre den tilgængelig til offline brug.
- **Omdøb**: Denne mulighed giver dig mulighed for at omdøbe filen direkte på fjernlagringen og give tilpasset filnavngivning.
- **Flyt**: Vælg denne handling for at flytte filen til en anden mappe i din cloud-lagring og bidrage til at opretholde en organiseret filstruktur.
- **Åbn i**: Brug denne handling til at eksportere filen til en anden kompatibel app. Filen downloades til din enhed, og derefter vises delingsdialogen for yderligere deling eller interaktion.
- **Slette**: Vær forsigtig med denne handling, da den permanent fjerner filen fra din cloud-lagring. Denne sletning kan ikke fortrydes.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu med Flere handlinger for en enkelt fil" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Hvis listen over handlinger overskrider den tilgængelige skærmplads, skal du blot rulle ned i handlingsmenuen for at få adgang til yderligere muligheder.

## Mappehandlinger

For hver mappe i din cloud-lagring har du forskellige tilgængelige handlinger. For at få adgang til disse muligheder skal du blot trykke på ellipsis-ikonet "..." ved siden af mappenavnet. Hvis du ikke kan se alle handlinger, skal du rulle ned for at afsløre flere valg. Her er de tilgængelige handlinger:

- **Afspil alle**: Erstat den aktuelle afspillerkø med alle elementer fra den valgte mappe.
- **Afspil næste**: Tilføj hele mappen øverst i afspillerkøen, lige efter det aktuelt afspillede element.
- **Afspil senere**: Tilføj mappeindholdet til bunden af afspillerkøen.
- **Tilføj til musikbibliotek**: Denne handling inkorporerer problemfrit mappens indhold i dit musikbibliotek og gør det let tilgængeligt og pænt organiseret efter kunstner, album, genre eller komponist.
- **Tilføj til afspilningsliste**: Du kan inkludere hele mappen i en afspilningsliste. Du har også mulighed for at oprette en ny afspilningsliste, og mappens navn tildeles automatisk.
- **Tilføj til favoritter**: Brug denne handling til at tilføje mappen til din liste over favoritfiler for hurtig og bekvem adgang.
- **Aktivere offline-tilstand**: Ved at aktivere offline-tilstand for en valgt mappe går applikationen ud over blot at downloade. Den scanner løbende for ændringer, og hvis nye filer tilføjes til den online mappe, downloades de automatisk til appen.
- **Downloade**: Download alt indhold i mappen til din enhed til offline adgang.
- **Omdøb**: Omdøb mappen direkte på fjernlagringen.
- **Flyt**: Flyt mappen til et andet sted i din cloud-lagring.
- **Slette**: Vær forsigtig med denne handling, da den permanent fjerner mappen og dens indhold fra din cloud-lagring. Denne handling kan ikke fortrydes.

## Hurtig adgang

Sektionen Hurtig adgang er placeret øverst på skærmen. Den giver dig hurtig adgang til favorit- og senest åbnede filer fra tilsluttede cloud-tjenester.
Når du åbner en fil eller mappe fra skyen, tilføjes den til listen "Senest åbnet". For at rydde denne liste skal du åbne "Seneste", trykke på knappen "Flere handlinger" og vælge "Slet liste". Du kan også markere dybt indlejrede mapper som Favoritter for at få hurtig adgang til dem uden at grave igennem mappestrukturen.

## Andre tjenester

Denne sektion viser ekstra funktioner, der forbedrer din oplevelse. Appen understøtter i øjeblikket Last.fm-scrobbling. Når det er tilsluttet, sendes dine afspilningsstatistikker automatisk til din Last.fm-konto. Du kan besøge din Last.fm-profil senere for at se lytteanalyse og få personaliserede musikanbefalinger. Detaljerede opsætningsinstruktioner er tilgængelige [her](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
