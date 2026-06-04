---
title: "Forbindelser"
date: 2020-02-01
description: "Lær, hvordan du forbinder cloud-tjenester og NAS-enheder til Flacbox. Stream højtopløsningsmusik fra iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk og mere. Brug SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder fildelingog USB-flashdrev."
keywords: [
  "Flacbox cloud-opsætning", "forbind Google Drive til Flacbox", "SMB musikstreaming",
  "WebDAV iOS afspiller", "DLNA musikapp", "NAS lydstreaming", "Wi-Fi Drive iPhone",
  "overfør filer til iPhone", "Flacbox iTunes File Sharing", "forbind NAS til iPhone",
  "Synology Drive musikapp", "QNAP musikapp", "Bluesound musikapp",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "musikapp med Last.fm scrobbling",
  "iXpand Flash Drive musik", "USB DAC iPhone"
]
tags: ["vejledning", "flacbox", "forbindelser", "cloud", "NAS"]
readingTime: 12
---


På denne skærm kan du forbinde alle de kilder, der indeholder din musik. Du kan integrere populære cloud-tjenester som Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive og mange flere, samt din Mac, PC eller NAS via standardprotokoller. Uanset om din samling lever på en streaming-venlig tjeneste som Dropbox eller på en personlig NAS som en Synology, QNAP, Buffalo, Apple Time Capsule eller WD My Cloud Home, forbinder Flacbox sig til dem alle fra én skærm.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Forbindelser-skærm" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Opret Forbindelse til Cloud-lager

- Åbn fanen **Forbindelser**.
- Vælg **Opret forbindelse til cloud-lager** fra menuen.
- Vælg en cloud-lagringstjeneste fra listen.
- Indtast dine legitimationsoplysninger på den officielle autorisationsside fra cloud-udbyderen, og tryk derefter på **Færdig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Tilføj en cloud-lagringstjeneste" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Hvis du støder på problemer, skal du kontrollere din internetforbindelse og dit login / adgangskode. I Premium-versionen af appen kan du tilføje et ubegrænset antal tjenester; den gratis version understøtter op til tre.

## Understøttede Cloud-lagringstjenester, Medieservere og Protokoller

Flacbox understøtter en usædvanlig bred vifte af kilder til din musik. Alt herunder fungerer fra én **Opret forbindelse til cloud-lager**-skærm.

**Personlig cloud-lagring:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Selvhostede servere:** Plex · Jellyfin · Emby · Subsonic (og alle Subsonic-kompatible servere — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (og ownCloud via den delte API) · Synology Drive · QNAP.

**NAS og fildelningsprotokoller:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, adgangskode eller offentlig nøgle-godkendelse) · NFS · DLNA / UPnP (afspilning og download).

**S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og enhver anden tjeneste, der eksponerer et S3-API-endpoint.

**Opdagelse på lokalt netværk:** Sektionen Tilgængelige enheder viser automatisk alle Bonjour / mDNS-tjenester på dit Wi-Fi-netværk, så du kan trykke for at forbinde uden at skrive en IP-adresse.

Hver forbindelse bruger den **officielle SDK eller åbne protokol** for tjenesten med OAuth-baseret godkendelse, hvor dette understøttes. Du kan forbinde flere konti til den samme tjeneste (f.eks. to Google Drive-konti, en personlig Dropbox ved siden af en arbejdsrelateret, eller både en Plex- og en Jellyfin-server) og gennemse dem side om side på Forbindelser-skærmen.

## Sikkerhed og Privatliv

Vi bruger kun officielle SDK'er og sikre forbindelser til at interagere med tilsluttede cloud-tjenester. Dit login og adgangskode er ikke tilgængeligt for applikationen — alle overførsler er TLS-krypterede.

Når du indtaster dit login og adgangskode, viser applikationen dig den officielle autorisationsside fra cloud-tjenesteudbyderen, og hele autorisationsprocessen foregår uden for applikationen. Cloud-tjenesteudbyderen sender derefter et auth-token til applikationen efter vellykket godkendelse, og dette token bruges til at foretage API-kald.

Et auth-token er en digital nøgle, der giver tredjepartsapplikationer mulighed for at interagere med cloud-lagring på dine vegne. Tokenet gemmes på din enhed i Apples sikre systemlager (Keychain), som er krypteret i hvile og beskyttet af din enheds adgangskode eller biometriske lås. Du kan downloade filer fra tilsluttede cloud-tjenester til din enhed; disse filer placeres i appens Documents-mappe og kan fjernes til enhver tid ved hjælp af den indbyggede filmanager.

Applikationen deler ingen oplysninger fra dine tilsluttede cloud-konti med Everappz, annoncører eller nogen tredjepart. Du kan til enhver tid tilbagekalde adgang til din cloud-konto ved at åbne kontoindstillingssiden i din webbrowser.

## Afvis Auth-Token

For at tilbagekalde et auth-token skal du logge ind på din cloud-konto i en webbrowser og navigere til sikkerheds- eller tilsluttede-apps-siden. Der kan du finde alle tredjepartsapps, der er tilsluttet din cloud-konto, og fjerne dem, hvis du ikke længere ønsker at bruge dem. Detaljerede instruktioner til Google-konti er tilgængelige [her](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan også frakoble cloud-kontoen inde i selve applikationen — når du gør det, slettes auth-tokenet straks fra din enhed. Hvis du afinstallerer applikationen fra din enhed, fjernes alle downloadede data og adgangstokens automatisk med den.

## Frakobl et Cloud-lager eller Skift Konfiguration

- **Åbn cloud-lagringsindstillingerne** — find den tilsluttede tjeneste på **Forbindelser**-skærmen.
- **Tryk på knappen "..."** ved siden af tjenestens titel for at åbne yderligere indstillinger:
  - **Omdøb** — skift navnet på cloud-tjenesten, som det vises på din liste.
  - **Indstillinger** — rediger konfigurationen eller godkendelsesdataene. Nogle gange skal du muligvis genautoriservicen, hvis autorisationstokenet er udløbet.
  - **Frakoble** — afbryd fuldstændigt forbindelsen mellem appen og cloud-tjenesten. Dette fjerner alle sange tilknyttet den pågældende tjeneste fra appens musikbibliotek, men efterlader dem urørte på serveren.

## Opret Forbindelse til en Computer eller NAS

Du kan også forbinde din computer, personlige NAS eller andre netværksenheder ved hjælp af SMB-, DLNA- eller WebDAV-protokollerne. Dette er den nemmeste måde at bringe et eksisterende hjemmemusiksbibliotek — hvad enten det lever på en Mac, en Windows-pc, en Synology-boks eller en NAS — ind i Flacbox uden at kopiere noget.

## Opret Forbindelse til en Computer via SMB

- Tryk på **Opret forbindelse til cloud-lager → SMB**.
- Indtast computerens IP-adresse og delt mappenavn i URL-feltet med formatet `smb://computer-ip-address/shared-folder-name`.
- Vælg protokolversion: **Auto**, **SMB1** eller **SMB2**.
- Indtast dit login og adgangskode (hvis påkrævet).
- Tryk på **Færdig**.

Hvis forbindelsen er vellykket, vil du se det tilsluttede lager i sektionen **Cloud-lager**. En komplet vejledning om, hvordan du forbinder din Mac eller PC via SMB, er tilgængelig [her](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Opret Forbindelse til en NAS via WebDAV

Alle trin er de samme som for SMB, undtagen URL-feltet. URL'en skal være i formatet `http://server-name` eller `https://server-name`, hvis serveren understøtter SSL. WebDAV fungerer med **Synology, QNAP, Nextcloud, ownCloud** og mange andre servere — overalt hvor et WebDAV-endpoint er tilgængeligt.

En komplet vejledning om, hvordan du forbinder en NAS via WebDAV, er tilgængelig [her](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Opret Forbindelse til en Computer eller NAS via DLNA

Du kan også dele et musikbibliotek på din Windows-pc eller personlige NAS ved hjælp af DLNA / UPnP-protokollen og få adgang til det bibliotek i appen som beskrevet [her](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA er en populær, bredt understøttet protokol, men den giver dig kun mulighed for at afspille eller downloade musik — du kan ikke uploade filer eller oprette nye mapper på en DLNA-server.

## Opret Forbindelse til en NAS eller Server via FTP, FTPS eller SFTP

Flacbox understøtter også de klassiske filoverførselsprotokoller. For at forbinde en server via FTP eller FTPS skal du trykke på **Opret forbindelse til cloud-lager → FTP**, indtaste host-URL'en i formatet `ftp://server-name` (eller `ftps://server-name` for en krypteret forbindelse), angive dit login og adgangskode og derefter trykke på **Færdig**. For **SFTP** (SSH File Transfer Protocol) skal du vælge **SFTP** i stedet og angive enten en adgangskode eller et SSH-nøglepar. Begge fungerer med NAS-enheder, Linux-hosts og enhver server, der har en FTP / FTPS / SSH-daemon.

## Opret Forbindelse til en NFS-deling

Flacbox inkluderer **NFS**-support (Network File System) — praktisk til Linux-hosts, BSD-servere og NAS-enheder, der foretrækker at eksponere musikbiblioteker via NFS frem for SMB. Vælg **NFS** i menuen **Opret forbindelse til cloud-lager**, indtast serveradressen og den eksporterede sti, og tryk på **Færdig**.

## Opret Forbindelse til en Plex Media Server

Flacbox kan forbinde direkte til en Plex Media Server og gennemse dit musikbibliotek efter Kunstnere, Album, Genrer og Afspilningslister. Tryk på **Opret forbindelse til cloud-lager → Plex**, log ind med din Plex-konto, vælg en server, og biblioteket vises ved siden af dine cloud-tjenester. Plex-servere på det samme lokale netværk opdages også automatisk i sektionen **Tilgængelige enheder**.

## Opret Forbindelse til en Jellyfin- eller Emby-server

Både **Jellyfin** (open-source) og **Emby** (kommercielt) medieservere fungerer naturligt i Flacbox. Tryk på **Opret forbindelse til cloud-lager → Jellyfin** eller **Emby**, indtast din server-URL (noget som `http://server-ip:8096`) og legitimationsoplysninger, og dit musikbibliotek er klar til at streame. Som med Plex vises biblioteker på det lokale netværk automatisk i **Tilgængelige enheder**.

## Opret Forbindelse til en Subsonic- eller Navidrome-server

Flacbox taler Subsonic API, hvilket betyder, at det fungerer med **Subsonic** selv, **Navidrome** og alle andre Subsonic-kompatible servere — herunder Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Tryk på **Opret forbindelse til cloud-lager → Subsonic**, indtast server-URL'en og legitimationsoplysningerne, og biblioteket vises på Forbindelser-skærmen. Dette er den nemmeste måde at give Flacbox adgang til en selvhostet musiksamling uden at eksponere den underliggende fildeling.

## Opret Forbindelse til S3-kompatibel Objektlagring

Til selvhostere og audiofiler, der bruger cloud-objektlagring, inkluderer Flacbox en S3-kompatibel connector. Tryk på **Opret forbindelse til cloud-lager → S3-lager**, og indtast endpoint-URL'en, regionen, adgangsnøglen, den hemmelige nøgle og bucket-navnet. Dette fungerer med AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og enhver anden tjeneste, der eksponerer et S3-API-endpoint.

## Tilgængelige Enheder

Denne sektion viser alle enheder på dit lokale netværk, som du kan forbinde til fra Flacbox via Bonjour-opdagelse. For at etablere en forbindelse skal du følge disse trin:

- Åbn appen og gå til sektionen **Tilgængelige enheder** under Forbindelser.
- Tryk på den enhed, du vil forbinde til.
- Hvis nødvendigt, indtast dine loginoplysninger for at fuldføre forbindelsen.

Dette er den hurtigste måde at opdage en SMB-, WebDAV- eller DLNA-deling på dit hjemmenetværk uden manuelt at skrive IP-adresser.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Tilgængelige enheder på det lokale netværk" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive er en praktisk teknologi, der muliggør trådløs filoverførsel fra din computer til din iOS-enhed via enhver desktopbrowser. For at bruge denne funktion effektivt skal du sikre, at din enhed og computer er forbundet til det samme Wi-Fi-netværk. Her er en trin-for-trin-vejledning om, hvordan du bruger Wi-Fi Drive.

### Aktivér Wi-Fi Drive

- Åbn applikationen og gå til fanen **Forbindelser**.
- Vælg **Opret forbindelse via Wi-Fi** for at få adgang til Wi-Fi Drive-hovedskærmen.
- (Valgfrit) Angiv et brugernavn og adgangskode til den integrerede webserver for at beskytte adgangen.
- Tryk på **Start Wi-Fi Drive** for at aktivere Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Få Adgang til Wi-Fi Drive på din Computer

- På din computer (stationær eller bærbar), åbn en webbrowser (såsom Chrome, Firefox eller Safari).
- I browserens adresselinje, indtast den URL, som applikationen angiver.

### Overfør Filer Trådløst

Når websiden, der svarer til din iOS-enhed, åbnes i browseren, kan du nemt trække og slippe filer fra din computer til websiden. De filer, du slipper, begynder at overføre til din iOS-enhed og vil være tilgængelige inde i Flacbox.

Du kan også montere Wi-Fi Drive direkte i Finder på macOS (Gå → Opret forbindelse til server…) eller Stifinder på Windows (Kortlæg netværksdrev…) og behandle din iPhone eller iPad som et almindeligt netværksdrev.

Detaljerede instruktioner om, hvordan du overfører filer trådløst ved hjælp af Wi-Fi Drive, er tilgængelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder Fildeling

iTunes-fildeling (nu Finder-fildeling på macOS Catalina og nyere) er en anden måde at overføre filer fra en computer til en enhed ved hjælp af et Lightning- eller USB-C-kabel.

- Forbind enheden til computeren med et kabel og kør **Finder** på Mac (eller **iTunes** på Windows).
- Åbn **Placeringer → Din tilsluttede enhed → Filer** og find Flacbox-appen.
- Tryk på appikonet for at se alle delte mapper.
- Kopiér filer fra computeren til den delte mappe på enheden ved hjælp af træk og slip.

Detaljerede instruktioner om, hvordan du bruger Finder-fildeling, er tilgængelige [her](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Opret Forbindelse til et USB-flashdrev

Hvis du har et SD-kort eller USB-drev, kan du forbinde det ved hjælp af en Lightning til USB / SD-kortlæser eller et USB-C-drev (på iPad og iPhone 15 / 16 / 17 / Pro). Appen understøtter Apple-certificerede kortlæsere og iXpand Flash Drives. Med et iXpand Flash Drive skal du sætte det i Lightning-porten og åbne applikationen — du vil se en meddelelse om, at en ekstern enhed er tilsluttet, og enhedsoplysningerne. Tryk på flashdrev-ikonet for at få adgang til musikmappen og tryk på en lydfil for at begynde at afspille.

Vi har detaljerede instruktioner om, hvordan du forbinder et USB-flashdrev til din iPhone og lytter til musik eller administrerer filer på det [her](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Filmanager

Når du har forbundet en cloud-lagringstjeneste, skal du trykke på dens ikon for at se alle tilgængelige filer og mapper. Du kan bruge den indbyggede filmanager til at arbejde med disse filer — downloade, omdøbe, flytte, uploade, slette og mere. Når du starter en download, vises filen i overførsels-køen. For at åbne overførsels-køen skal du gå til fanen Lokale filer og trykke på det roterende pil-ikon i øverste venstre hjørne. Alle downloadede filer og mapper er tilgængelige i sektionen Lokale filer.

## Øverste Værktøjslinje

Den øverste værktøjslinje, der er placeret under navigationslinjen, tilbyder flere nyttige handlinger for nem adgang. Du kan vise eller skjule den med et simpelt swipe-ned-gestus.

- **Søg** — udfør en hurtig søgning i den aktuelle mappe, hvilket gør det nemt at finde specifikke filer eller mapper.
- **Fortsæt afspilning** — hvis aktiveret i applikationsindstillingerne, gendanner dette afspillerens kø og den sidste medieposition for den aktuelle mappe. En praktisk måde at fortsætte, hvor du slap.
- **Afspil alt** — scanner den aktuelle mappe og dens undermapper og tilføjer derefter alle fundne lydfiler til en ny afspiller-kø. Nyttigt, når du vil afspille alle spor i et bibliotek.
- **Bland alt** — som Afspil alt, men blander filerne inden de tilføjes til afspiller-køen. Godt til at genopdage en gammel musikmappe.

## Mappemuligheder

Når du åbner en mappe, finder du et praktisk sæt handlinger tilgængeligt ved at trykke på knappen **"..."** i øverste højre hjørne.

- **Vælg** — aktivér filtilvalgstilstand. Dette lader dig vælge en eller flere filer i mappen og udføre handlinger på hele markeringen.
- **Ny mappe** — opret en ny mappe i den aktuelle mappe. Godt til at holde dit bibliotek velstruktureret.
- **Aktivere offline-tilstand** — slå offline-tilstand til for den aktuelle mappe. Offline-tilstand går ud over simpel download: det overvåger aktivt mappen for ændringer. Hvis du tilføjer nye filer online, vises de automatisk på din enhed.
- **Upload filer** — upload filer fra din enhed til onlinemappen. Dette gør dem tilgængelige overalt via den samme cloud-tjeneste.
- **Søg** — søg efter specifikke filer i den aktuelle mappe.
- **Sortér** — sortér filer efter navn, størrelse, ændringsdato eller efter metadata. Standard sorteringstilstand afspejler sorteringsrækkefølgen på serveren, men du kan ændre den efter dine præferencer.
- **Gitter / Listevisning** — skift mellem tabelvisning og miniaturevisning. Tabelvisning viser en kompakt liste; miniaturevisning viser store coverforhåndsvisninger til hurtig visuel identifikation.

## Rediger Online Filer

Når du har brug for at administrere flere filer i dit cloud-lager, skal du bruge **Markeringstilstand** til at strømlinjeforme dine handlinger:

- **Aktivér markeringstilstand** — tryk på knappen **"..."** i øverste højre hjørne og vælg **Vælg**.
- **Vælg filer** — afkrydsningsfelter vises ved siden af alle filer og mapper. Tryk for at vælge et eller flere elementer.
- **Udfør handlinger** — når du har valgt filerne eller mapperne, vil du have adgang til Afspil næste, Afspil senere, Føj til musikbibliotek, Føj til en afspilningsliste, Kopiér, Upload, Flyt, Omdøb og Slet.

Hvis du foretrækker at behandle tilsluttet cloud-lager som skrivebeskyttet (for at forhindre utilsigtede sletninger), skal du aktivere Indstillinger → Filmanager → Rediger online filer → Fra for at skjule alle destruktive handlinger fra brugergrænsefladen.

## Filhandlinger

Tryk på ikonet **"..."** nær en fils titel for at afsløre dens handlingsmenu:

- **Afspil næste** — indsætter filen øverst i afspillerkøen, så den afspilles lige efter det aktuelle spor.
- **Afspil senere** — tilføjer filen til bunden af afspillerkøen.
- **Føj til musikbibliotek** — inkorporerer filen i dit musikbibliotek, organiseret efter kunstner, album, genre eller komponist.
- **Føj til en afspilningsliste** — tilføjer filen til en eksisterende afspilningsliste eller opretter en ny.
- **Redigere lydtags** — åbner den indbyggede tags-editor til at ændre metadata. For online filer downloades sporet midlertidigt, redigeres og genuploadtes derefter, når du bekræfter.
- **Føj til favoritter** — tilføjer filen til din favoritliste for hurtig adgang.
- **Downloade** — downloader filen eller mappen til din enhed til offline brug.
- **Omdøb** — omdøber filen direkte på fjernlageret.
- **Flyt** — flytter filen til en anden mappe i dit cloud-lager.
- **Åbn med** — eksporterer filen til en anden kompatibel app. Filen downloades til din enhed, og derefter vises systemdelingsarket.
- **Slette** — fjerner filen permanent fra dit cloud-lager. **Denne handling kan ikke fortrydes.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Flere handlinger for en fil i tilsluttet cloud-lager" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Hvis listen over handlinger overskrider det tilgængelige skærmplads, skal du blot rulle ned i handlingsmenuen for at få adgang til yderligere muligheder.

## Mappehandlinger

For hver mappe i dit cloud-lager har du en bred vifte af handlinger tilgængeligt ved at trykke på ikonet **"..."** ved siden af mappetitlen. Hvis du ikke kan se alle handlinger, skal du rulle ned for at afsløre mere.

- **Afspil alt** — erstatter den aktuelle afspillerkø med hvert element i den valgte mappe.
- **Afspil næste** — tilføjer hele mappen øverst i afspillerkøen.
- **Afspil senere** — tilføjer mappeindholdet til bunden af afspillerkøen.
- **Føj til musikbibliotek** — inkorporerer mappens indhold i dit musikbibliotek.
- **Føj til afspilningsliste** — tilføjer hele mappen til en afspilningsliste. Du har også mulighed for at oprette en ny afspilningsliste; dens navn udfyldes automatisk fra mappenavnet.
- **Føj til favoritter** — tilføjer mappen til dine favoritter for hurtig adgang.
- **Aktivere offline-tilstand** — ud over en simpel download overvåger dette løbende mappen for nye filer og downloader dem automatisk, efterhånden som de vises online.
- **Downloade** — downloader alt indhold i mappen til din enhed for offline adgang.
- **Omdøb** — omdøber mappen direkte på fjernlageret.
- **Flyt** — flytter mappen til en anden placering i dit cloud-lager.
- **Arkiver (ZIP)** — pakker mappeindholdet ind i en enkelt ZIP-fil (Premium-funktion).
- **Slette** — fjerner mappen og dens indhold permanent fra dit cloud-lager. **Denne handling kan ikke fortrydes.**

## Hurtig Adgang

Sektionen Hurtig adgang er placeret øverst på skærmen. Den giver dig hurtig adgang til dine foretrukne og nyligt åbnede filer fra tilsluttede cloud-tjenester. Når du åbner en fil eller mappe fra skyen, tilføjes den til listen Nyligt åbnet. For at rydde denne liste skal du åbne Seneste, trykke på knappen Flere handlinger og vælge Slet liste. Du kan også markere dybt nestede mapper som Favoritter for at få hurtig adgang til dem uden at grave gennem mappestrukturen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Online-links og hurtig adgang" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Andre Tjenester

Denne sektion viser ekstra funktioner, der forbedrer din oplevelse. I øjeblikket understøtter appen **Last.fm**-scrobbling — når tilsluttet, sendes dine afspilningsstatistikker automatisk til din Last.fm-konto. Du kan derefter besøge din Last.fm-profil for at se lytteanalyse og få personlige musikanbefalinger. Detaljerede opsætningsinstruktioner er tilgængelige [her](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm-forbindelsen" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
