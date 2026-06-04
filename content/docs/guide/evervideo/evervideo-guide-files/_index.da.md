---
title: "Filer"
date: 2020-02-01
lastmod: 2026-06-01
description: "Lær at bruge Filer-fanen i Evervideo på iPhone, iPad og Mac. Tilslut cloudtjenester, NAS-enheder, medieservere og RTSP-streams ét sted. Administrer offline-videoer, overførselskøen, downloads, Wi-Fi Drive, iTunes / Finder-fildeling og USB-drev. Inkluderer iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA og S3-kompatibelt lager."
keywords: [
  "Evervideo filer", "Evervideo forbindelser", "Evervideo lokale filer",
  "cloud-videoopsætning iPhone", "tilslut Google Drive video", "SMB-videostreaming",
  "WebDAV-videoafspiller iOS", "DLNA video iPhone", "NAS-videostreaming",
  "Wi-Fi Drive videooverførsel", "Evervideo iTunes fildeling", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo offline-tilstand video", "Evervideo overførselskø",
  "Evervideo filhåndtering", "Evervideo Dokumenter-mappe",
  "videoafspiller Synology", "videoafspiller QNAP",
  "videoafspiller Apple Time Capsule", "USB DAC video",
  "iXpand videoafspiller", "S3-videoafspiller"
]
tags: ["guide", "evervideo", "filer", "forbindelser", "cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Filer-fanen er Evervideos alt-i-én filhåndtering. I modsætning til de fleste videoapps, der opdeler cloudlager fra lokale filer i forskellige faner, fusionerer Evervideo begge i én enkelt, rullbar skærm, så du kan bevæge dig fra en Plex-server til en cloudmappe til din iPhones Dokumenter-mappe uden at hoppe mellem faner.

Filer-fanen er opdelt i klare sektioner, der vises i denne rækkefølge på din skærm:

- **Hurtig adgang** — seneste og favoritter for filer og mapper, du åbnede senest.
- **Filer i denne applikation** — hvad der lever i Evervideos sandboxede Dokumenter-mappe.
- **Filer på denne iPhone / iPad / Mac** — videoer andre steder på din enhed, vist via systemets filudvælger.
- **Cloudlager** — alle cloudkonti, NAS og medieservere, du har tilsluttet.
- **Tilgængelige enheder** — Bonjour / mDNS-automatisk-opdagede servere og drev på dit lokale netværk.

I øverste højre hjørne af Filer-skærmen er en Overførsler-knap (et roterende-pile-ikon). Tryk på den for at åbne overførselskøen, hvor du overvåger alle downloads og uploads på tværs af alle dine kilder.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo filer på tværs af tilsluttede lagre" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Tilslut til cloudlager

Sektionen Cloudlager i Filer-fanen er, hvor alle tilsluttede konti, NAS, medieservere og streams befinder sig — side om side i én rullbar liste.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo cloudlagersektion i Filer-fanen" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Åbn **Filer**-fanen.
- Rul til **Cloudlager**-sektionen.
- Tryk på **Tilslut til cloudlager** fra menuen.
- Vælg en cloudlagertjeneste fra listen.
- Indtast dine legitimationsoplysninger på den officielle autorisationsside leveret af cloududbyderen, og tryk derefter på **Færdig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo tilslut en cloudlagertjeneste" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Hvis du støder på problemer, skal du tjekke din internetforbindelse og dit brugernavn / adgangskode. I Premium-versionen af appen kan du tilføje et ubegrænset antal tjenester; gratisversionen understøtter op til tre.

## Understøttede cloudlagertjenester, medieservere og protokoller

Evervideo understøtter en exceptionelt bred vifte af kilder til dine videoer. Alt nedenfor fungerer fra et enkelt Tilslut til cloudlager-flow.

**Personligt cloudlager:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Selvhostede medieservere:** Plex · Jellyfin · Emby · Subsonic (og alle Subsonic-kompatible servere — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (og ownCloud via den delte API) · Synology Drive · QNAP.

**NAS og fildeling-protokoller:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, adgangskode eller offentlig nøgle-godkendelse) · NFS · DLNA / UPnP (afspilning og download).

**Live og IP-kamerastreams:** RTSP — peg Evervideo mod en hvilken som helst `rtsp://` URL, og den afspilles bare. Godt til sikkerhedskameraer, dørklokke-kameraer, IPTV-streams, babymonitorer og lignende live-kilder.

**S3-kompatibelt objektlager:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og ethvert andet S3-API-endpoint.

**Lokale biblioteker:** Photos-biblioteket (alle videoer, skærmoptagelser, fotoalbummer) og Musik-app-biblioteket (Albums, Genrer, Afspilningslister) — begge vises inde i Mediebiblioteket, så du ikke behøver at kopiere noget.

**Lokalt netværksopdagelse:** sektionen Tilgængelige enheder viser automatisk alle Bonjour / mDNS-tjenester på dit Wi-Fi-netværk — Plex, Jellyfin, Emby-servere, Synology, QNAP, AirPort-routere med tilsluttede drev, Apple Time Capsule — så du kan trykke for at forbinde uden at indtaste en IP-adresse.

Hver forbindelse bruger den officielle SDK eller åben protokol for tjenesten med OAuth-baseret autorisation, hvor det understøttes. Du kan tilslutte flere konti af samme tjeneste (for eksempel to Google Drive-konti eller både en Plex og en Jellyfin-server) og gennemse dem side om side i Cloudlager-sektionen.

## Sikkerhed og privatliv

Evervideo bruger kun officielle SDK'er og sikre forbindelser til at interagere med tilsluttede cloudtjenester. Dit brugernavn og adgangskode er ikke tilgængeligt for applikationen — alle overførsler er TLS-krypterede.

Når du indtaster dit brugernavn og adgangskode, viser applikationen dig den officielle autorisationsside leveret af cloudtjenestens udbyder, og hele autorisationsprocessen finder sted uden for applikationen. Cloudtjenestens udbyder sender derefter et auth-token til applikationen efter vellykket autorisation, og det token bruges til at foretage API-kald.

Et auth-token er en digital nøgle, der giver tredjepartsapplikationer mulighed for at interagere med cloudlager på dine vegne. Token'en gemmes på din enhed i Apples sikre systemlager (Keychain), som er krypteret i hvile og beskyttet af din enheds adgangskode eller biometrisk lås. Du kan downloade filer fra tilsluttede cloudtjenester til din enhed; disse filer placeres i appens Dokumenter-mappe og kan fjernes til enhver tid ved hjælp af den indbyggede filhåndtering.

Applikationen deler ingen oplysninger fra dine tilsluttede cloudkonti med Everappz, annoncører eller nogen tredjepart. Du kan tilbagekalde adgangen til din cloudkonto til enhver tid ved at åbne kontoindstillingssiden i din webbrowser.

## Tilbagekald auth-token

For at tilbagekalde et auth-token skal du logge ind på din cloudkonto i en webbrowser og navigere til sikkerheds- eller tilsluttede-apps-siden. Der kan du finde alle tredjepartsapps, der er tilsluttet din cloudkonto, og fjerne dem, hvis du ikke længere ønsker at bruge dem. Detaljerede instruktioner til Google-konti er tilgængelige [her](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan også afbryde forbindelsen til cloudkontoen inden i selve applikationen — når du gør det, slettes auth-token'en øjeblikkeligt fra din enhed. Hvis du afinstallerer applikationen fra din enhed, fjernes alle downloadede data og adgangstokens automatisk med den.

## Afbryd et cloudlager eller skift konfiguration

- **Adgang til cloudlager-indstillinger** — find den tilsluttede tjeneste i sektionen **Cloudlager** i Filer-fanen.
- **Tryk på knappen "..."** ud for tjenestens titel for at åbne yderligere indstillinger:
  - **Omdøb** — skift navn på cloudtjenesten, som den vises på din liste.
  - **Indstillinger** — rediger konfiguration eller autentificeringsdata. Nogle gange kan det være nødvendigt at re-autorisere den tilsluttede cloudtjeneste, hvis autorisationstokenet er udløbet.
  - **Afbryd forbindelsen** — bryd fuldstændigt forbindelsen mellem appen og cloudtjenesten. Dette fjerner alle videoer tilknyttet den tjeneste fra dit mediebibliotek, men lader dem urørte på serveren.

## Tilslut til en computer eller NAS

Du kan tilslutte din computer, personlige NAS eller en anden netværksenhed ved hjælp af SMB, WebDAV, FTP / FTPS, SFTP, NFS eller DLNA-protokollen. Dette er den nemmeste måde at bringe et eksisterende hjemmemediebibliotek — hvad enten det befinder sig på en Mac, Windows PC, Synology, QNAP, Apple Time Capsule eller WD My Cloud Home — ind i Evervideo uden at kopiere noget.

### Tilslut til en computer via SMB

- Tryk på **Tilslut til cloudlager → SMB**.
- Indtast computerens IP-adresse og delt mappenavn i formatet `smb://computer-ip-adresse/delt-mappenavn`.
- Vælg protokolversion: **Auto**, **SMB1** eller **SMB2**.
- Indtast dit brugernavn og adgangskode (hvis påkrævet).
- Tryk på **Færdig**.

Hvis forbindelsen er vellykket, vises delingen i Cloudlager-sektionen. En komplet vejledning om, hvordan du tilslutter din Mac eller PC via SMB, er tilgængelig [her](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Tilslut til en NAS via WebDAV

Alle trin er de samme som SMB, bortset fra URL-feltet. Brug `http://server-name` eller `https://server-name`, hvis serveren understøtter SSL. WebDAV fungerer med Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home og enhver anden server med et WebDAV-endpoint.

En komplet vejledning om WebDAV er tilgængelig [her](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Tilslut via DLNA / UPnP

Del et mediebibliotek placeret på din Windows PC eller NAS ved hjælp af DLNA / UPnP-protokollen, og få adgang til det inde i Evervideo som beskrevet [her](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA er bredt understøttet, men det giver dig kun mulighed for at afspille eller downloade videoer — du kan ikke uploade filer eller oprette nye mapper på en DLNA-server.

### Tilslut via FTP, FTPS eller SFTP

Evervideo understøtter også de klassiske filoverførselsprotokaller. For at tilslutte en server via FTP eller FTPS skal du trykke på Tilslut til cloudlager → FTP, indtaste vært-URL'en i formen `ftp://server-name` (eller `ftps://server-name` for en krypteret forbindelse), angive dit brugernavn og adgangskode og derefter trykke på Færdig. For SFTP (SSH File Transfer Protocol) skal du vælge SFTP i stedet og angive enten en adgangskode eller et SSH-nøglepar.

### Tilslut til en NFS-deling

Evervideo inkluderer NFS-support (Network File System) — praktisk til Linux-hosts, BSD-servere og NAS-enheder, der foretrækker at eksponere videobiblioteker via NFS i stedet for SMB. Vælg NFS i menuen Tilslut til cloudlager, indtast serveradressen og den eksporterede sti, og tryk på Færdig.

## Tilslut en Plex Media Server

Evervideo kan oprette direkte forbindelse til en Plex Media Server og gennemse dine Film-, TV-shows- og Hjemmevideoer-biblioteker. Tryk på Tilslut til cloudlager → Plex, log ind med din Plex-konto, vælg en server, og biblioteket vises ved siden af dine cloudtjenester. Plex-servere på det samme lokale netværk opdages også automatisk i sektionen Tilgængelige enheder.

## Tilslut en Jellyfin eller Emby Server

Både Jellyfin (open-source) og Emby (kommerciel) medieservere fungerer native i Evervideo. Tryk på Tilslut til cloudlager → Jellyfin eller Emby, indtast din server-URL (typisk noget som `http://server-ip:8096`) og legitimationsoplysninger, og dit bibliotek er klar til streaming.

## Tilslut en Subsonic eller Navidrome Server

Evervideo taler Subsonic API, hvilket betyder, at det fungerer med Subsonic selv, Navidrome og alle andre Subsonic-kompatible servere — herunder Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) og Ampache. Tryk på Tilslut til cloudlager → Subsonic, indtast server-URL og legitimationsoplysninger, og biblioteket vises i Cloudlager-sektionen.

## Tilslut en RTSP-stream (IP-kameraer, live-TV, IPTV)

Evervideo har native RTSP-understøttelse, så du kan pege den mod enhver RTSP-kilde — sikkerhedskameraer, dørklokke-kameraer, IPTV-udbydere, babymonitorer, udsendelsesfeeds — og Evervideo vil trække og dekode streamen live. Tryk på Online links → Tilføj link, indsæt den fulde URL (`rtsp://camera-ip:port/stream-sti`), angiv brugernavn og adgangskode, hvis det kræves, og tryk på Færdig.

## Tilslut til S3-kompatibelt objektlager

Til selvhostere og superbrugere, der bruger cloud-objektlager, inkluderer Evervideo en S3-kompatibel connector. Tryk på Tilslut til cloudlager → S3-lager, og indtast derefter endpoint-URL, region, adgangsnøgle, hemmelig nøgle og bucket-navn. Dette fungerer med AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces og ethvert andet S3-API-endpoint.

## Tilgængelige enheder

Denne sektion viser alle enheder på dit lokale netværk, som du kan oprette forbindelse til fra Evervideo via Bonjour / mDNS-opdagelse — Plex, Jellyfin, Emby-servere, Synology, QNAP, AirPort-routere med tilsluttede drev, Apple Time Capsule og så videre. For at etablere en forbindelse:

- Rul til sektionen Tilgængelige enheder i Filer-fanen.
- Tryk på den enhed, du vil oprette forbindelse til.
- Hvis det er nødvendigt, skal du indtaste dine loginoplysninger for at fuldføre forbindelsen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo tilgængelige enheder på det lokale netværk" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive lader dig overføre filer trådløst fra din computer til din iOS-enhed via en hvilken som helst skrivebordsbrowser, Finder eller File Explorer. Din enhed og computer skal være på det samme Wi-Fi-netværk.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Aktivér Wi-Fi Drive

- I Filer-fanen, rul til Cloudlager → Tilslut via Wi-Fi for at åbne Wi-Fi Drive-startskærmen.
- (Valgfrit) Angiv et brugernavn og adgangskode til den indlejrede webserver.
- Tryk på Start Wi-Fi Drive.

### Få adgang til Wi-Fi Drive på din computer

- Åbn en webbrowser på din computer (Chrome, Firefox, Safari osv.).
- Indtast den URL, der vises af applikationen.
- Træk og slip filer fra din computer til websiden — de begynder at overføre til din iOS-enhed.

Du kan også montere Wi-Fi Drive direkte i **Finder** på macOS (Gå → Opret forbindelse til server…) eller File Explorer på Windows (Kortlæg netværksdrev…) og behandle din iPhone eller iPad som et almindeligt netværksdrev.

Detaljerede instruktioner er tilgængelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder fildeling

iTunes Fildeling (nu Finder Fildeling på macOS Catalina og nyere) lader dig overføre filer ved hjælp af et Lightning- eller USB-C-kabel. Tilslut enheden, åbn Finder på Mac (eller iTunes på Windows), find Evervideo på applisten, og kopier filer til dens delte mappe.

## Tilslut et USB-flashdrev eller SD-kort

Sæt et USB-drev eller SD-kort i din iPhone, iPad eller Mac via Lightning-til-USB / USB-C-adapteren eller kortlæseren. Åbn Filer → Filer på denne iPhone → Åbn mappe, naviger til drevet, og vælg en videofil eller mappe. Evervideo afspiller filer direkte fra drevet uden at kopiere dem til intern lager — praktisk til meget store 4K-biblioteker.

## Mappegennemsyn i tilsluttede lagre

Tryk på en tilsluttet cloudtjeneste for at åbne dens filbrowser. Mapper viser videominiaturebilleder, når de er tilgængelige, og tryk på en video starter afspilning med det samme, mens resten af filen fortsætter med at streame i baggrunden.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo gennemsyn af mapper i tilsluttede lagre" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Hurtig adgang

Hurtig adgang-sektionen sidder øverst i Filer-fanen. Den giver dig hurtig adgang til dine foretrukne og senest åbnede filer og mapper — både fra cloudtjenester og fra lager på enheden. Når du åbner en fil eller mappe fra clouden, tilføjes den til listen Senest åbnede. Du kan markere dybt indlejrede mapper som Favoritter for hurtigt at få adgang til dem uden at grave igennem mappestrukturen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo online links og hurtig adgang" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Filer i denne applikation

Denne sektion viser filer og mapper gemt i Evervideos sandboxede Dokumenter-mappe — alt, hvad du har downloaded fra clouden, overført via Wi-Fi Drive, kopieret via Finder fildeling eller importeret fra en anden app.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo filer i denne applikation" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Dokumenter-mappe

Dokumenter-mappen er roden af alt inde i Filer i denne applikation. Du kan oprette undermapper, omdøbe filer, flytte dem rundt og gruppere dem, som du ønsker.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo lokale filer — Dokumenter-mappe" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Filer på denne iPhone / iPad / Mac

Denne sektion viser videoer placeret på din enhed, men i andre applikationer. Du kan importere dem til Evervideo ved hjælp af systemets filudvælger:

- Tryk på Åbn filer… for at vælge bestemte filer.
- Tryk på Åbn mappe… for at vælge en hel mappe.

Du kan også bruge Tilslut en mappe til at oprette et link til en mappe på din enhed med læse / skrive-adgang — perfekt til at arbejde med en mappe på iCloud Drive eller et tilsluttet USB-drev uden at kopiere noget.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo filer på denne enhed" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Specielle mapper

I Filer-fanen vil du se adskillige specielle mapper, som Evervideo opretter og bruger automatisk:

- **Hente** — alle filer downloaded fra clouden vises her som standard. Tilpas i Indstillinger → Filhåndtering → Gem downloadede filer til.
- **Afspiller-cache** — medieafspillerens cache. Som standard downloader afspilleren kommende videoer for problemfri afspilning. Du kan deaktivere cachen i appindstillinger eller blot slette denne mappe.
- **iCloud** — filer i denne mappe synkroniseres på tværs af alle dine enheder forbundet til den samme iCloud-konto.
- **Offline mapper** — når du markerer en mappe, afspilningsliste, album eller genre som tilgængeligt offline, downloades filerne til denne mappe.

## Øverste værktøjslinje

Den øverste værktøjslinje, placeret under navigationsbaren, tilbyder adskillige handlinger, du kan vise eller skjule med en swipe-ned gestus:

- **Søg** — udfør en søgning inden for den aktuelle mappe eller sektion.
- **Fortsæt afspilning** — hvis det er aktiveret i indstillinger, gendanner afspillerkøen og den sidste videoposition for den aktuelle mappe.
- **Afspil alle** — scan den aktuelle mappe og dens undermapper og tilføj filer til afspillerkøen.
- **Bland alle** — ligesom Afspil alle, men blander inden tilføjelse.

## Mappeindstillinger

Når du åbner en mappe, skal du trykke på knappen **"..."** i øverste højre hjørne for disse handlinger:

- **Vælg** — aktiver filvalg-tilstand.
- **Ny mappe** — opret en ny mappe inden for den aktuelle mappe.
- **Aktivér offline-tilstand** — slå offline-synkronisering til for den aktuelle mappe. Nye filer tilføjet online downloades automatisk.
- **Upload filer** — upload filer fra din enhed til den online mappe.
- **Søg** — søg inden for mappen.
- **Sorter** — sorter filer efter navn, størrelse, ændringsdato eller metadata.
- **Gitter / Listevisning** — skift mellem tabelvisning og miniaturebilledevisning. Miniaturebilledevisning viser store videoposter-forhåndsvisninger.

## Valg-tilstand

Tryk på **"..."** i øverste højre hjørne og vælg **Vælg** for at gå ind i valg-tilstand. Afkrydsningsfelter vises ved siden af alle filer og mapper. Tryk for at vælge et eller flere elementer, og udfør derefter batch-handlinger: Afspil næste, Afspil senere, Tilføj til mediebibliotek, Tilføj til en afspilningsliste, Kopier, Upload, Flyt, Omdøb eller Slet.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo valg-tilstand i filhåndteringen" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Hvis du foretrækker at behandle tilsluttet cloudlager som skrivebeskyttet (for at forhindre utilsigtede sletninger), skal du aktivere Indstillinger → Filhåndtering → Rediger online filer → Fra for at skjule alle destruktive handlinger fra brugerfladen.

## Filhandlinger

Tryk på ikonet **"..."** nær en fils titel for at afsløre dens handlingsmenu:

- **Afspil næste** — indsæt filen øverst i afspillerkøen.
- **Afspil senere** — tilføj filen nederst i afspillerkøen.
- **Tilføj til mediebibliotek** — inkorporer filen i dit mediebibliotek, organiseret efter Album og Genre.
- **Tilføj til en afspilningsliste** — tilføj filen til en eksisterende afspilningsliste eller opret en ny.
- **Rediger tags** — åbn den indbyggede tag-editor til at ændre metadata. For online filer downloades filen midlertidigt, redigeres og uploades derefter igen, efter du bekræfter.
- **Tilføj til favoritter** — tilføj filen til din favoritliste for hurtig adgang.
- **Downloade** — download filen eller mappen til din enhed til offline brug.
- **Omdøb** — omdøb filen direkte på fjernlageret.
- **Flyt** — flyt filen til en anden mappe inden for dit cloudlager.
- **Tilføj til arkiv** — bundter filen i en enkelt ZIP-fil (Premium-funktion).
- **Åbn i** — eksporter filen til en anden kompatibel app via systemets Del-ark.
- **Slette** — fjern filen permanent. **Denne handling kan ikke fortrydes.**

## Mappehandlinger

For hver mappe i dit cloudlager har du mange handlinger tilgængelige ved at trykke på ikonet **"..."** ved siden af mappens titel.

- **Afspil alle** — erstat den aktuelle afspillerkø med alle videoer i mappen.
- **Afspil næste / Afspil senere** — tilføj hele mappen til køen.
- **Tilføj til mediebibliotek** — inkorporer mappens indhold i dit mediebibliotek.
- **Tilføj til afspilningsliste** — tilføj hele mappen til en afspilningsliste.
- **Tilføj til favoritter** — tilføj mappen til dine favoritter.
- **Aktivér offline-tilstand** — ud over en simpel download overvåger dette løbende mappen for nye filer og auto-downloader dem, efterhånden som de vises online.
- **Downloade** — download alt indhold i mappen til din enhed til offline adgang.
- **Omdøb / Flyt** — omdøb eller flyt mappen på fjernlageret.
- **Tilføj til arkiv** — bundter mappeindholdet i en ZIP-fil (Premium-funktion).
- **Slette** — fjern mappen og dens indhold permanent. **Denne handling kan ikke fortrydes.**

## Overførselskø

I øverste højre hjørne af Filer-fanen er en **Overførsler**-knap (et roterende-pile-ikon). Tryk på den for at åbne overførselskøen — en liste over alle aktive downloads og uploads på tværs af alle dine kilder med realtids-fremskridt, hastighed og ETA per fil.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo filoverførsels-kø" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Du kan sætte på pause, genoptage, genforsøge mislykkede overførsler, omarrangere elementer for at prioritere specifikke downloads eller annullere dem individuelt. Du kan også justere overførselskoens hastighed (maksimale parallelle opgaver), netværkstype (kun Wi-Fi eller Wi-Fi + Mobil) og baggrundsoverførsler i Indstillinger → Filhåndtering.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo handlinger på filoverførsels-køen" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offline-tilstand og synkroniserede offline mapper

Offline-tilstand er en praktisk funktion, der lader dig se dine yndlingsvideoer, selv når du ikke er tilsluttet internettet. Når du aktiverer offline-tilstand for en mappe, afspilningsliste, album eller genre, downloades alle filer i den samling automatisk til din enhed til offline afspilning. De vises i sektionen Offline mapper.

Når du tilføjer nye filer til fjernserveren, downloades de også automatisk — så din offline samling holdes opdateret uden at du gør noget. For manuelt at synkronisere igen skal du trykke på de tre prikker i øverste højre hjørne af en offline mappe og vælge Synkronisere.

Du kan justere synkroniseringstimeout i Indstillinger → Filhåndtering → Synkroniserede offline mapper → Tidsinterval.

Detaljerede instruktioner er tilgængelige [her](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalisering

I Indstillinger → Personalisering kan du konfigurere, hvordan Filer-fanen præsenteres:

- **Filer-skærmstil** — Simpel menu (viser mappalisten direkte) eller Grupperet menu (grupperer indhold efter kategori — Hurtig adgang, Specielle mapper, Cloudlager osv.).
