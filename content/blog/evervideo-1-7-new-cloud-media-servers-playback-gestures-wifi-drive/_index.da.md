---
title: "Evervideo 1.7: nye Plex, Jellyfin, sky-streaming og afspilningsgester"
date: 2026-05-18
description: "Evervideo 1.7 tilføjer 10+ nye forbindelser — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — plus nye afspilningsgester (dobbelt-tap for at spole, tryk og hold for 2x-hastighed), en opfrisket Wi-Fi Drive med batch-upload og Liquid Glass-opdateringer for iPhone, iPad og Mac."
keywords: ["Evervideo 1.7", "Evervideo-opdatering", "HD-videoafspiller iPhone", "Plex videoafspiller iOS", "Jellyfin iPhone video", "Emby videoafspiller iOS", "Subsonic video iOS", "Navidrome video iOS", "Internxt video-streaming", "Proton Drive videoafspiller", "QNAP videoafspiller iPhone", "Nextcloud videoafspiller iOS", "Amazon S3 video-streaming", "SFTP videoafspiller iPhone", "FTP videoafspiller iOS", "NFS video-streaming iPhone", "stream video fra NAS iPhone", "MKV-afspiller iPhone", "videoafspiller-gester iOS", "dobbelt-tap for at spole video", "Wi-Fi Drive videooverførsel iPhone", "Liquid Glass-design", "sky-videoafspiller iOS 2026", "stream film fra sky iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Afspilningsgester", "Liquid Glass", "Hvad er nyt"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Kort fortalt:** [Evervideo 1.7](/products/evervideo) er en stor opdatering til HD-videoafspilleren på iPhone, iPad og Mac. Udgivelsen tilføjer 10+ nye forbindelser til sky, NAS og medieservere — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** plus de mest populære medieservere **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** og **Emby**, samt tre netværksprotokoller: **FTP**, **SFTP** og **NFS**. Nye **afspilningsgester** lader dig dobbelt-tappe for at hoppe frem eller tilbage, trykke og holde for at køre med 2x hastighed og tappe én gang for at skifte mellem kontrolelementer — alt sammen uden at forlade fuldskærm. Wi-Fi Drive får en opdateret brugerflade med valgtilstand og en smartere uploadkø. Hele appen er afstemt til Apples nye **Liquid Glass**-design.

---

## Hej allesammen!

En stor Evervideo-opdatering er her. Det er en af de største udgivelser, vi har sendt afsted: **10+ nye sky-, server- og netværksforbindelser**, helt nye **afspilningsgester** for hurtigere styring i fuldskærm, en opfrisket **Wi-Fi Drive**-oplevelse og en brugerflade afstemt til **Liquid Glass** på iPhone, iPad og Mac.

[Hent Evervideo 1.7 i App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336), eller opdater fra din nuværende version. Mac-brugere kan hente [skrivebordsversionen her](https://apps.apple.com/app/evervideo/id6743504109).

## 10+ nye forbindelser til sky, NAS og medieservere

Evervideo 1.7 udvider, hvad der tæller som dit «videobibliotek». Hvis dine film, serier eller optagelser bor i en sky, du stoler på, på et NAS derhjemme eller på en selvhostet medieserver, kan Evervideo nu streame direkte fra det — ingen download, ingen konverteringer, ingen genkodning.

### Privatlivsfokuseret skylagring: Internxt og Proton Drive

Hvis du går op i end-to-end-kryptering og nul-vidende lagring, er to af de mest respekterede privatlivsfokuserede skyer nu native i Evervideo:

- **Internxt** — open source, post-kvante-krypteret, GDPR-kompatibel spansk sky. Gratis niveau tilgængeligt.
- **Proton Drive** — end-to-end-krypteret lagring fra skaberne af Proton Mail og Proton VPN, baseret i Schweiz. Gratis niveau tilgængeligt med betalte abonnementer til større biblioteker.

Forbind én gang, og dine videoer streames gennem den krypterede tunnel — Evervideo ser aldrig dine data i klartekst, og det gør udbyderens server heller ikke.

### Selvhostet lagring: QNAP, Nextcloud, Amazon S3

For brugere, der kører deres egen infrastruktur:

- **QNAP** — native API-forbindelse til QNAP NAS-enheder for hurtig og pålidelig videoafspilning over lokal Wi-Fi eller fjernadgang. Stream 4K MKV-filer direkte uden genkodning.
- **Nextcloud** — forbind til enhver selvhostet eller administreret Nextcloud-instans. Godt, hvis du allerede er flyttet væk fra Google Drive eller Dropbox af privatlivsgrunde.
- **Amazon S3** — pege Evervideo mod en hvilken som helst S3-bucket (eller S3-kompatibel lagring som Backblaze B2, Wasabi, MinIO, Cloudflare R2) og stream din samling direkte.

### <a id="media-servers"></a>Medieservere: Plex, Subsonic, Navidrome, Jellyfin, Emby

Dette er det store nyt for fans af selvhostet video. Evervideo 1.7 forvandler din iPhone, iPad eller Mac til en førsteklasses klient til de mest populære open source- og freemium-medieservere:

- **Plex** — Plex Media Server er **gratis** at hente og køre, med et valgfrit **Plex Pass**-abonnement til funktioner som mobil synkronisering, hardware-transkodning og live-TV. Evervideo virker med både gratis og Plex Pass-biblioteker — stream hele din film- og TV-samling.
- **Subsonic** — den oprindelige selvhostede streamingserver. Den officielle Subsonic-server er **betalt** (1$/måned efter en 30-dages prøveperiode), og Evervideo taler også Subsonic-API'et til kompatible videoservere.
- **Navidrome** — moderne, letvægts, **fuldstændig gratis og open source** server. Implementerer Subsonic-API'et. Kører på en Raspberry Pi, et NAS eller en hvilken som helst Linux-boks.
- **Jellyfin** — **fuldstændig gratis og open source** medieserver (en community-fork af Emby). Håndterer film, TV, musik, bøger og hjemmevideo. Ingen konti, ingen telemetri, ingen abonnementer. Det foretrukne valg for brugere, der vil have selvhostet streaming uden kommercielle bindinger.
- **Emby** — **freemium** medieserver. Kerneserveren er gratis; **Emby Premiere** er et engangs- eller årligt køb, der låser op for mobilapps, offline-synkronisering, Cinema Mode og mere. Evervideo forbinder til både gratis og Premiere-biblioteker.

Uanset hvilken server du kører, streamer Evervideo hele dit bibliotek — film, serier, hjemmevideoer og indlejrede undertekstspor — med video-equalizeren, 360°-understøttelse, Picture-in-Picture, AirPlay og Chromecast.

### Nye netværksprotokoller: FTP, SFTP, NFS

For brugere med tilpassede servere, hjemmelaboratorier eller generiske NAS-bokse, der ikke leveres med en poleret mobilapp, tilføjer Evervideo 1.7 tre klassiske protokoller:

- **SFTP (SSH File Transfer Protocol)** — det rigtige svar til **sikker fjern-videostreaming fra din egen server**. SFTP kører oven på SSH, så hele overførslen (autentificering og videodata) er krypteret. Hvis du har en VPS, dedikeret server eller en Linux-boks derhjemme med SSH-adgang, kan du smide en mappe med videoer på den og streame over det offentlige internet uden at eksponere andet. Understøtter adgangskode- og nøglebaseret autentificering.
- **FTP** — den langvarige standard for filoverførsel. Nyttig, hvis dit **hjemme-NAS** (ældre Synology, ASUS, D-Link, TerraMaster eller generiske bokse) eksponerer en FTP-server, men ikke har en native API-integration. Bedst brugt inden for dit lokale netværk.
- **NFS (Network File System)** — de facto delingsprotokol på Linux og de fleste NAS-enheder. NFS-shares er almindelige på hjemmelaboratorier og små virksomhedsnetværk; Evervideo monterer dem nu og streamer 4K- og HD-video med lav overhead.

> **Tip:** SFTP er protokollen, du vil have til streaming over det åbne internet. FTP og NFS er bedst inden for dit lokale netværk — hold dem væk fra det offentlige internet, medmindre du pakker dem ind i en VPN.

## Nye afspilningsgester

At se videoer i fuldskærm bør føles ubesværet. Evervideo 1.7 introducerer et rent sæt tap-gester, der lader dig styre afspilning uden at vise kontrolelementerne på skærmen — perfekt til film, forelæsninger eller alt, du vil se uden afbrydelser.

### Dobbelt-tap — Spring frem eller tilbage

Dobbelt-tap på **højre side** af skærmen for at **spole frem** med et konfigurerbart antal sekunder. Dobbelt-tap på **venstre side** for at **hoppe tilbage**. Du kan ændre intervallet (standard: 10 sekunder) i **Indstillinger → Afspilning → Gesturspring-interval** — vælg alt fra 5 sekunder (til finere søgning) op til 60 sekunder (til at springe intros over).

Dette er gesten, som YouTube- og Netflix-brugere genkender med det samme, og nu er den native i Evervideo for enhver video fra enhver kilde.

### Tryk og hold — Midlertidig 2x hastighed

Tryk og hold hvor som helst på skærmen for **midlertidigt at sætte afspilningen op til 2x**. Slip for at vende tilbage til normal hastighed. Perfekt til:

- At springe langsomme scener over uden at binde sig til en permanent hastighedsændring.
- Hurtigt at scanne forelæsninger, tutorials eller podcasts for at finde det relevante afsnit.
- At smage på film, før du forpligter dig til at se hele versionen.

Tryk-og-hold-gesten ændrer ikke din gemte afspilningshastighed — slip, og du er tilbage, hvor du startede.

### Enkelt-tap — Vis / skjul kontrolelementer

Et enkelt tap på skærmen skifter afspilningskontrolelementerne (afspil, pause, søgelinje, undertekster, equalizer). Tap én gang for at vise dem, tap igen for at skjule dem. Kombineret med dobbelt-tap og tryk-og-hold betyder det, at du kan tilbringe næsten en hel film i ren fuldskærmstilstand og stadig søge, pause og hurtigt scanne, når du har brug for det.

## Wi-Fi Drive: ny brugerflade og hurtigere uploads

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) er Evervideos indbyggede funktion til **trådløs overførsel af videoer fra din computer til din iPhone eller iPad — uden iTunes, uden kabler, uden sky-konto**. Begge enheder skal være på samme Wi-Fi-netværk. Du starter serveren i iOS-appen og enten:

- Åbner URL'en i en hvilken som helst desktop-browser (Safari, Chrome, Firefox, Edge), trækker dine videofiler ind på siden, og de uploades direkte til enheden, eller
- Monterer enheden som en netværksshare via **Mac Finder** ('Opret forbindelse til server…') eller **Windows File Explorer** (Tilknyt netværksdrev) ved hjælp af WebDAV.

Det er den hurtigste måde at flytte en stor lokal videosamling til din telefon eller tablet på, uden nogen tredjepartstjeneste. Se [trin-for-trin-vejledningen her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

I Evervideo 1.7 får Wi-Fi Drive:

- **Redesignet brugerflade** — renere, lettere at læse med et blik og opdateret til Liquid Glass.
- **Ny valgtilstand for batch-handlinger** — vælg flere filer eller mapper og udfør handlinger i bulk (slet, flyt, kopier).
- **Forbedret filuploadkø** — bedre fremskridtsfeedback og modstandsdygtighed over for netværkshikke, så en ustabil Wi-Fi-forbindelse ikke længere ødelægger en 30 GB-overførsel.
- **Bedre samlet overførselsydeevne** — målbart hurtigere uploads til store biblioteker, især til 4K MKV-filer og filmsamlinger.

## Andre forbedringer

### Liquid Glass-designopdateringer

Evervideo 1.7's brugerflade er opdateret til Apples nye **Liquid Glass**-materiale i hele appen — translucente overflader, smidigere animationer og forfinede kontrolelementer, der passer naturligt ind i iOS 26, iPadOS 26 og macOS 26. Now Playing, filbrowseren og indstillingsskærmene er alle finjusteret for at matche systemets nye æstetik.

### Opdaterede forbindelsesbiblioteker

Vi har opfrisket de underliggende biblioteker, Evervideo bruger til at tale med **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** og andre tjenester. Resultat: færre kant-tilfælde af forbindelsesfejl, bedre understøttelse af nyere serverversioner og forbedret pålidelighed ved streaming af video over langsommere eller geografisk fjerne forbindelser.

### Afspilnings-fejlrettelser

- Rettede afspilningsproblemer på visse selvhostede servere, hvor streams gik i stå efter søgning i store MKV-filer.
- Bedre genoptagelsesadfærd, når netværket kortvarigt falder ud midt i afspilningen.
- Smidigere undertekstsynkronisering på langt indhold.

### Lokaliseringsrettelser

Oversættelsesrettelser på flere sprog baseret på direkte brugerfeedback. Bedre tekstpasning på mindre knapper og længere europæiske sprog (tysk, hollandsk, fransk).

### Mindre justeringer inspireret af jeres feedback

Mange mindre forbedringer baseret på App Store-anmeldelser og e-mails til support@everappz.com. Vi læser hver besked.

## Hvorfor denne opdatering betyder noget

Evervideo 1.7 er bygget omkring tre idéer:

1. **Dine videoer, hvor end du gemmer dem.** Uanset om dit bibliotek bor på iCloud Drive, i en privatlivsfokuseret sky som Proton Drive eller Internxt, på en medieserver som Plex eller Jellyfin, på et NAS derhjemme eller på en Raspberry Pi, der kører Navidrome — Evervideo forbinder sig nu nativt til det, med den samme afspilningsoplevelse overalt.
2. **Fuldskærmsvideo, der føles ubesværet.** De nye tap-gester (dobbelt-tap, tryk og hold, enkelt-tap) bringer den slags flydende kontrol, som streamingapps som YouTube og Netflix har lært brugerne at forvente, anvendt på *din* videosamling.
3. **Hurtigere overførsler fra din computer.** En opfrisket Wi-Fi Drive med batch-valg og en smartere uploadkø gør det reelt hurtigt at flytte store 4K-filmsamlinger til din iPhone eller iPad — ingen kabler, ingen iTunes, ingen komprimering.

## Få Evervideo 1.7

[**Hent Evervideo i App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336), eller opdater inde fra App Store. [Mac-versionen](https://apps.apple.com/app/evervideo/id6743504109) er tilgængelig separat som en universel Mac-app. Evervideo er gratis at hente med valgfrie opgraderinger i appen til avancerede funktioner. De nye sky-forbindelser, medieserver-understøttelse, afspilningsgester, Wi-Fi Drive-forbedringer og Liquid Glass-brugerflade er en del af basisopdateringen.

Hvis du kan lide appen, så efterlad gerne en vurdering i App Store — det hjælper virkelig. Har du feedback eller løber ind i et problem? Skriv til os på **support@everappz.com**. Vi læser hver besked.

## Ofte stillede spørgsmål

{{% details title="Hvad er nyt i Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 introducerer understøttelse af 10+ nye forbindelser (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), nye afspilningsgester (dobbelt-tap for at spole, tryk og hold for 2x-hastighed, enkelt-tap for at skifte kontroller), en redesignet Wi-Fi Drive med valgtilstand og en smartere uploadkø, Liquid Glass-designopdateringer, opdaterede forbindelsesbiblioteker og mange fejlrettelser.
{{% /details %}}

{{% details title="Virker Evervideo med Plex?" closed="true" %}}
Ja. Fra og med Evervideo 1.7 kan du forbinde til en Plex Media Server og streame hele dit videobibliotek — film, TV-serier og hjemmevideoer. Plex Media Server er gratis at køre; Plex Pass er valgfrit. Evervideo understøtter både gratis og Plex Pass-opsætninger, herunder direkte afspilning af MKV, MP4, AVI, MOV og andre formater uden genkodning.
{{% /details %}}

{{% details title="Understøttes Jellyfin eller Navidrome i Evervideo?" closed="true" %}}
Ja. Både Jellyfin og Navidrome er fuldt ud understøttet i Evervideo 1.7. Jellyfin er en gratis open source-medieserver, der håndterer video og lyd. Navidrome er en gratis open source-server, der implementerer Subsonic-API'et. Evervideo forbinder til begge nativt.
{{% /details %}}

{{% details title="Er Plex, Jellyfin, Emby, Navidrome og Subsonic gratis?" closed="true" %}}
- **Plex** — serveren er gratis; Plex Pass er en valgfri betalt opgradering.
- **Jellyfin** — fuldstændig gratis og open source.
- **Emby** — serveren er gratis; Emby Premiere er betalt og låser op for mobil synkronisering og offline.
- **Navidrome** — fuldstændig gratis og open source.
- **Subsonic** — den officielle server koster 1$/måned efter en 30-dages prøveperiode, men dens API er åbent, og mange gratis servere (inklusive Navidrome) implementerer det.
{{% /details %}}

{{% details title="Kan jeg streame fra mit hjemme-NAS over SFTP, FTP eller NFS?" closed="true" %}}
Ja. Evervideo 1.7 tilføjer SFTP, FTP og NFS som native forbindelsestyper. SFTP er det anbefalede valg til streaming fra din egen server over det offentlige internet, fordi al trafik er krypteret via SSH. FTP og NFS er bedst brugt inden for dit lokale netværk eller bag en VPN.
{{% /details %}}

{{% details title="Hvordan forbinder jeg Evervideo til en tilpasset server med SFTP?" closed="true" %}}
Åbn Evervideo, gå til fanen Forbindelser, vælg SFTP, og indtast serverens værtsnavn eller IP, port (normalt 22), brugernavn og enten en adgangskode eller en privat SSH-nøgle. Evervideo gennemser dine fjernmapper og streamer videofiler direkte med end-to-end-kryptering.
{{% /details %}}

{{% details title="Understøtter Evervideo Internxt og Proton Drive?" closed="true" %}}
Ja. Begge privatlivsfokuserede skyer er understøttet fra Evervideo 1.7. De slutter sig til MEGA og andre privatlivsfokuserede tjenester, der allerede er tilgængelige i appen.
{{% /details %}}

{{% details title="Hvordan fungerer de nye afspilningsgester?" closed="true" %}}
Under videoafspilning i fuldskærm **dobbelt-tap på højre side** for at hoppe frem og **dobbelt-tap på venstre side** for at hoppe tilbage med et konfigurerbart interval (standard 10 sekunder — skift det i Indstillinger). **Tryk og hold** hvor som helst på skærmen for midlertidigt at sætte hastigheden op til 2x; slip for at vende tilbage til normalt. **Enkelt-tap** hvor som helst for at skifte afspilningskontrolelementerne (vis eller skjul).
{{% /details %}}

{{% details title="Kan jeg ændre intervallet for dobbelt-tap-spring?" closed="true" %}}
Ja. Gå til **Indstillinger → Afspilning → Gesturspring-interval** og vælg en værdi mellem 5 og 60 sekunder. De fleste brugere holder det på 10 eller 15 sekunder.
{{% /details %}}

{{% details title="Hvad er Wi-Fi Drive i Evervideo?" closed="true" %}}
Wi-Fi Drive er Evervideos indbyggede trådløse filoverførselsfunktion. Den lader dig uploade videoer fra din computer til din iPhone eller iPad over dit lokale Wi-Fi-netværk — uden iTunes, uden kabler, uden sky-konto. Du kan bruge en hvilken som helst desktop-browser eller en WebDAV-klient som Mac Finder eller Windows File Explorer. Se [den fulde Wi-Fi Drive-vejledning](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Afspiller Evervideo MKV, AVI og andre formater fra Plex eller Jellyfin?" closed="true" %}}
Ja. Evervideo afspiller stort set alle videoformater — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — og streamer dem direkte fra Plex, Jellyfin, Emby og andre medieservere uden at kræve transkodning for de fleste codecs. Det betyder lavere CPU-belastning på din server og hurtigere starttider.
{{% /details %}}

{{% details title="Er det gratis at opdatere til Evervideo 1.7?" closed="true" %}}
Ja. Evervideo er gratis at hente fra App Store, og 1.7 er en gratis opdatering for alle eksisterende brugere. De nye sky-integrationer, medieserver-understøttelsen, afspilningsgesterne, Wi-Fi Drive-forbedringerne og Liquid Glass-brugerfladen er en del af basisopdateringen.
{{% /details %}}

{{% details title="Hvilke enheder er Evervideo 1.7 tilgængelig på?" closed="true" %}}
Evervideo 1.7 kører på iPhone, iPad og Mac. AirPlay og Chromecast lader dig caste afspilning til en større skærm. iCloud Drive-synkronisering holder dit bibliotek og dine indstillinger ensartede på tværs af enheder.
{{% /details %}}
