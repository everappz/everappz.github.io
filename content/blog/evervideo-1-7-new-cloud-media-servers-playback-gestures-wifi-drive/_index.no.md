---
title: "Evervideo 1.7: Ny Plex, Jellyfin, sky-strømming, avspillingsbevegelser"
date: 2026-05-18
description: "Evervideo 1.7 legger til 10+ nye tilkoblinger — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — pluss nye avspillingsbevegelser (dobbelttrykk for å spole, trykk og hold for 2x hastighet), en oppdatert Wi-Fi Drive med batch-opplasting og Liquid Glass UI-oppdateringer for iPhone, iPad og Mac."
keywords: ["Evervideo 1.7", "Evervideo-oppdatering", "HD-videospiller iPhone", "Plex videospiller iOS", "Jellyfin iPhone-video", "Emby videospiller iOS", "Subsonic video iOS", "Navidrome video iOS", "Internxt video-strømming", "Proton Drive videospiller", "QNAP videospiller iPhone", "Nextcloud videospiller iOS", "Amazon S3 video-strømming", "SFTP videospiller iPhone", "FTP videospiller iOS", "NFS video-strømming iPhone", "strøm video fra NAS iPhone", "MKV-spiller iPhone", "bevegelser i videospiller iOS", "dobbelttrykk for å spole video", "Wi-Fi Drive videooverføring iPhone", "Liquid Glass-design", "sky-videospiller iOS 2026", "strøm filmer fra sky iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Avspillingsbevegelser", "Liquid Glass", "Hva er nytt"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Kort fortalt:** [Evervideo 1.7](/products/evervideo) er en stor oppdatering for HD-videospilleren på iPhone, iPad og Mac. Utgivelsen legger til 10+ nye sky-, NAS- og medieserver-tilkoblinger — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, pluss de mest populære medieserverne **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** og **Emby**, og tre nettverksprotokoller: **FTP**, **SFTP** og **NFS**. Nye **avspillingsbevegelser** lar deg dobbelttrykke for å hoppe fremover eller bakover, trykke og holde for å kjøre på 2x, og enkelttrykke for å veksle kontrollene — alt uten å forlate fullskjerm. Wi-Fi Drive får et oppdatert grensesnitt med valgmodus og en smartere opplastingskø. Hele appen er innstilt for Apples nye **Liquid Glass**-design.

---

## Hei alle sammen!

En stor Evervideo-oppdatering er her. Dette er en av de største utgivelsene vi har sendt: **10+ nye sky-, server- og nettverkstilkoblinger**, helt nye **avspillingsbevegelser** for raskere kontroll i fullskjerm, en oppdatert **Wi-Fi Drive**-opplevelse, og et UI innstilt for **Liquid Glass** på tvers av iPhone, iPad og Mac.

[Last ned Evervideo 1.7 fra App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) eller oppdater fra din eksisterende versjon. Mac-brukere kan hente [skrivebordsversjonen her](https://apps.apple.com/app/evervideo/id6743504109).

## 10+ nye sky-, NAS- og medieserver-tilkoblinger

Evervideo 1.7 utvider hva som regnes som «videobiblioteket ditt». Hvis filmene, seriene eller opptakene dine bor i en sky du stoler på, på et NAS hjemme eller på en selvhostet medieserver, kan Evervideo nå strømme fra det direkte — uten nedlastinger, uten konverteringer, uten omkoding.

### Personvernfokusert skylagring: Internxt og Proton Drive

Hvis du bryr deg om ende-til-ende-kryptering og zero-knowledge-lagring, er to av de mest respekterte navnene innen personvern-først-skyer nå native i Evervideo:

- **Internxt** — open source-spansk sky med post-kvantum-kryptering og GDPR-samsvar. Gratis nivå tilgjengelig.
- **Proton Drive** — ende-til-ende-kryptert lagring fra skaperne av Proton Mail og Proton VPN, basert i Sveits. Gratis nivå tilgjengelig og betalte abonnementer for større biblioteker.

Koble til én gang, og videoene dine strømmer gjennom den krypterte tunnelen — Evervideo ser aldri dataene dine i klartekst, og det gjør heller ikke leverandørens server.

### Selvhostet lagring: QNAP, Nextcloud, Amazon S3

For brukere som driver sin egen infrastruktur:

- **QNAP** — native API-tilkobling til QNAP NAS-enheter for rask, pålitelig videoavspilling over lokalt Wi-Fi eller fjerntilgang. Strøm 4K MKV-filer direkte uten omkoding.
- **Nextcloud** — koble til en hvilken som helst selvhostet eller administrert Nextcloud-instans. Flott hvis du allerede har migrert vekk fra Google Drive eller Dropbox av personvernhensyn.
- **Amazon S3** — pek Evervideo mot en hvilken som helst S3-bøtte (eller S3-kompatibel lagring som Backblaze B2, Wasabi, MinIO, Cloudflare R2) og strøm samlingen din direkte.

### <a id="media-servers"></a>Medieservere: Plex, Subsonic, Navidrome, Jellyfin, Emby

Dette er den store for selvhostede videofans. Evervideo 1.7 gjør iPhone, iPad eller Mac om til en førsteklasses klient for de mest populære open source- og freemium-medieserverne:

- **Plex** — Plex Media Server er **gratis** å laste ned og kjøre, med valgfritt **Plex Pass**-abonnement for funksjoner som mobil synkronisering, maskinvare-transkoding og direkte-TV. Evervideo fungerer med både gratis og Plex Pass-biblioteker — strøm hele film- og TV-samlingen din.
- **Subsonic** — den opprinnelige selvhostede strømmeserveren. Den offisielle Subsonic-serveren er **betalt** ($1/måned etter 30-dagers prøveperiode), og Evervideo snakker også Subsonic-API til kompatible videoservere.
- **Navidrome** — moderne, lett, **helt gratis og open source** server. Implementerer Subsonic-API. Kjører på en Raspberry Pi, NAS eller hvilken som helst Linux-boks.
- **Jellyfin** — **helt gratis og open source** medieserver (en community-fork av Emby). Håndterer filmer, TV, musikk, bøker og hjemmevideo. Ingen kontoer, ingen telemetri, ingen abonnementer. Det foretrukne valget for brukere som vil ha selvhostet strømming uten kommersielle bånd.
- **Emby** — **freemium** medieserver. Kjerneserveren er gratis; **Emby Premiere** er et engangs- eller årlig kjøp som låser opp mobilapper, offline-synkronisering, Cinema Mode og mer. Evervideo kobler seg til både gratis- og Premiere-biblioteker.

Uansett hvilken server du kjører, strømmer Evervideo hele biblioteket ditt — filmer, serier, hjemmevideoer og innebygde undertekstspor — med video-equalizer, 360°-støtte, Picture-in-Picture, AirPlay og Chromecast.

### Nye nettverksprotokoller: FTP, SFTP, NFS

For brukere med egendefinerte servere, hjemmelaboratorier eller generiske NAS-bokser som ikke leveres med en polert mobilapp, legger Evervideo 1.7 til tre klassiske protokoller:

- **SFTP (SSH File Transfer Protocol)** — det riktige svaret for **sikker fjern-strømming av video fra din egen server**. SFTP kjører over SSH, så hele overføringen (autentisering og videodata) er kryptert. Hvis du har en VPS, dedikert server eller en Linux-boks hjemme med SSH-tilgang, kan du legge en mappe med videoer på den og strømme over det offentlige internett uten å eksponere noe annet. Støtter både passord- og nøkkelbasert autentisering.
- **FTP** — den langtidsetablerte standarden for filoverføring. Nyttig hvis ditt **hjemme-NAS** (eldre Synology, ASUS, D-Link, TerraMaster eller generiske bokser) eksponerer en FTP-server, men ikke har en native API-integrasjon. Best brukt inne i ditt lokale nettverk.
- **NFS (Network File System)** — de facto-delingsprotokollen på Linux og de fleste NAS-enheter. NFS-delinger er vanlige i hjemmelaboratorier og småbedriftsnettverk; Evervideo monterer dem nå og strømmer 4K- og HD-video med lav overhead.

> **Tips:** SFTP er protokollen du vil ha for strømming over det åpne internett. FTP og NFS er best inne i det lokale nettverket — hold dem unna det offentlige internett med mindre du pakker dem inn i en VPN.

## Nye avspillingsbevegelser

Å se på video i fullskjerm bør føles uanstrengt. Evervideo 1.7 introduserer et rent sett med trykkbevegelser som lar deg styre avspillingen uten å eksponere kontrollene på skjermen — perfekt for filmer, forelesninger eller hva som helst du vil se uavbrutt.

### Dobbelttrykk — hopp fremover eller bakover

Dobbelttrykk på **høyre side** av skjermen for å **hoppe fremover** med et konfigurerbart antall sekunder. Dobbelttrykk på **venstre side** for å **hoppe tilbake**. Du kan endre intervallet (standard: 10 sekunder) i **Innstillinger → Avspilling → Bevegelse-hoppintervall** — velg alt fra 5 sekunder (for fin spoling) til 60 sekunder (for å hoppe over introer).

Dette er bevegelsen YouTube- og Netflix-brukere vil kjenne igjen umiddelbart, og den er nå native i Evervideo for hvilken som helst video, fra hvilken som helst kilde.

### Trykk og hold — midlertidig 2x hastighet

Trykk og hold hvor som helst på skjermen for å **midlertidig øke avspillingen til 2x**. Slipp for å gå tilbake til normal hastighet. Perfekt for:

- Å hoppe gjennom langsomme scener uten å forplikte seg til en permanent hastighetsendring.
- Å raskt skanne gjennom forelesninger, opplæringer eller podkaster for å finne den relevante delen.
- Å smake på filmer før du forplikter deg til å se hele versjonen.

Hold-bevegelsen endrer ikke din lagrede avspillingshastighet — slipp og du er tilbake der du startet.

### Enkelttrykk — vis / skjul kontroller

Et enkelttrykk på skjermen veksler avspillingskontrollene (spill, pause, søkelinje, undertekster, equalizer). Trykk én gang for å bringe dem opp, trykk igjen for å skjule dem. Kombinert med dobbelttrykk og hold betyr dette at du kan tilbringe nesten en hel film i ren fullskjerm-modus og fortsatt spole, pause og hastighet-skanne når du trenger det.

## Wi-Fi Drive: nytt UI og raskere opplastinger

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) er Evertags innebygde funksjon for å **overføre videoer trådløst fra datamaskinen din til iPhone eller iPad — uten iTunes, uten kabler, uten skykonto påkrevd**. Begge enhetene må være på samme Wi-Fi-nettverk. Du starter serveren i iOS-appen og enten:

- Åpner URL-en i en hvilken som helst skrivebordsnettleser (Safari, Chrome, Firefox, Edge), drar videofilene dine inn på siden, og de lastes opp direkte til enheten, eller
- Monterer enheten som en nettverksdeling via **Mac Finder** («Koble til server…») eller **Windows Filutforsker** (Tilordne nettverksstasjon) med WebDAV.

Det er den raskeste måten å flytte en stor lokal videosamling til telefonen eller nettbrettet ditt uten noen tredjepartstjeneste. Se den [trinnvise veiledningen her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

I Evervideo 1.7 får Wi-Fi Drive:

- **Redesignet brukergrensesnitt** — ryddigere, lettere å lese ved et blikk, og oppdatert for Liquid Glass.
- **Ny valgmodus for batch-handlinger** — velg flere filer eller mapper og handle på dem i grupper (slett, flytt, kopier).
- **Forbedret filopplastingskø** — bedre fremskrittsfeedback og motstandsdyktighet mot nettverkshikker, slik at en ustabil Wi-Fi-tilkobling ikke lenger ødelegger en 30 GB-overføring.
- **Bedre overordnet overføringsytelse** — målbart raskere opplastinger for store biblioteker, særlig for 4K MKV-filer og filmsamlinger.

## Andre forbedringer

### Liquid Glass-designoppdateringer

Grensesnittet i Evervideo 1.7 er oppdatert for Apples nye **Liquid Glass**-materiale i hele appen — gjennomskinnelige overflater, jevnere animasjoner og raffinerte kontroller som passer naturlig inn i iOS 26, iPadOS 26 og macOS 26. Spilles nå av, filutforskeren og innstillingsskjermene er alle finjustert for å matche den nye systemestetikken.

### Oppdaterte tilkoblingsbiblioteker

Vi har oppdatert de underliggende bibliotekene Evervideo bruker for å snakke med **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** og andre tjenester. Resultatet: færre tilkoblingsfeil i kanttilfeller, bedre støtte for nyere serverversjoner og forbedret pålitelighet ved strømming av video på tregere eller geografisk fjerne tilkoblinger.

### Avspillings-feilrettinger

- Fikset avspillingsproblemer på visse selvhostede servere der strømmer ville stoppe etter spoling på store MKV-filer.
- Bedre gjenoppta-oppførsel når nettverket kort faller bort midt i avspillingen.
- Jevnere undertekst-synkronisering på lang-form-innhold.

### Lokaliseringsrettelser

Oversettelsesrettelser på tvers av flere språk basert på direkte tilbakemeldinger fra brukere. Bedre tekstplassering på mindre knapper og lengre europeiske språk (tysk, nederlandsk, fransk).

### Mindre forbedringer inspirert av tilbakemeldingen din

Mange mindre forbedringer basert på App Store-anmeldelser og e-poster til support@everappz.com. Vi leser hver melding.

## Hvorfor denne oppdateringen betyr noe

Evervideo 1.7 er bygget rundt tre ideer:

1. **Videoene dine, uansett hvor du oppbevarer dem.** Enten biblioteket ditt bor på iCloud Drive, en personvern-først-sky som Proton Drive eller Internxt, en medieserver som Plex eller Jellyfin, et NAS hjemme eller en Raspberry Pi som kjører Navidrome — Evervideo kobler seg nå til det nativt, med samme avspillingsopplevelse overalt.
2. **Fullskjerm-video som føles uanstrengt.** De nye trykkbevegelsene (dobbelttrykk, trykk og hold, enkelttrykk) bringer den slags flytende kontroll som strømmeapper som YouTube og Netflix har trent brukere til å forvente, anvendt på *din* videosamling.
3. **Raskere overføringer fra datamaskinen din.** En oppdatert Wi-Fi Drive med batch-valg og en smartere opplastingskø gjør det virkelig raskt å flytte store 4K-filmsamlinger til iPhone eller iPad — uten kabler, uten iTunes, uten komprimering.

## Skaff deg Evervideo 1.7

[**Last ned Evervideo i App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) eller oppdater fra App Store. [Mac-versjonen](https://apps.apple.com/app/evervideo/id6743504109) er tilgjengelig separat som en universell Mac-app. Evervideo er en gratis nedlasting med valgfrie oppgraderinger i appen for avanserte funksjoner. De nye sky-tilkoblingene, medieserver-støtten, avspillingsbevegelsene, Wi-Fi Drive-forbedringene og Liquid Glass-UI-en er en del av basisoppdateringen.

Hvis du liker appen, gi gjerne en vurdering i App Store — det hjelper virkelig. Har du tilbakemeldinger eller støtt på et problem? Send oss e-post på **support@everappz.com**. Vi leser hver melding.

## Vanlige spørsmål

{{% details title="Hva er nytt i Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 introduserer støtte for 10+ nye tilkoblinger (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), nye avspillingsbevegelser (dobbelttrykk for å spole, trykk og hold for 2x hastighet, enkelttrykk for å veksle kontroller), en redesignet Wi-Fi Drive med valgmodus og smartere opplastingskø, Liquid Glass-designoppdateringer, oppdaterte tilkoblingsbiblioteker og mange feilrettinger.
{{% /details %}}

{{% details title="Fungerer Evervideo med Plex?" closed="true" %}}
Ja. Fra Evervideo 1.7 kan du koble til en Plex Media Server og strømme hele videobiblioteket ditt — filmer, TV-serier og hjemmevideoer. Plex Media Server er gratis å kjøre; Plex Pass er valgfritt. Evervideo støtter både gratis og Plex Pass-oppsett, inkludert direkte avspilling av MKV, MP4, AVI, MOV og andre formater uten omkoding.
{{% /details %}}

{{% details title="Støttes Jellyfin eller Navidrome i Evervideo?" closed="true" %}}
Ja. Både Jellyfin og Navidrome støttes fullt ut i Evervideo 1.7. Jellyfin er en gratis, open source-medieserver som håndterer video og lyd. Navidrome er en gratis, open source-server som implementerer Subsonic-API. Evervideo kobler seg til begge nativt.
{{% /details %}}

{{% details title="Er Plex, Jellyfin, Emby, Navidrome og Subsonic gratis?" closed="true" %}}
- **Plex** — serveren er gratis; Plex Pass er en valgfri betalt oppgradering.
- **Jellyfin** — helt gratis og open source.
- **Emby** — serveren er gratis; Emby Premiere er betalt og låser opp mobil synkronisering og offline.
- **Navidrome** — helt gratis og open source.
- **Subsonic** — den offisielle serveren koster $1/måned etter 30-dagers prøveperiode, men API-en er åpen og mange gratis servere (inkludert Navidrome) implementerer den.
{{% /details %}}

{{% details title="Kan jeg strømme fra hjemme-NAS-et mitt over SFTP, FTP eller NFS?" closed="true" %}}
Ja. Evervideo 1.7 legger til SFTP, FTP og NFS som native tilkoblingstyper. SFTP er det anbefalte valget for å strømme fra din egen server over det offentlige internett fordi all trafikk krypteres via SSH. FTP og NFS er best brukt inne i det lokale nettverket eller bak en VPN.
{{% /details %}}

{{% details title="Hvordan kobler jeg Evervideo til en egendefinert server med SFTP?" closed="true" %}}
Åpne Evervideo, gå til Tilkoblinger-fanen, velg SFTP, og oppgi serverens vertsnavn eller IP, port (vanligvis 22), brukernavn og enten et passord eller en privat SSH-nøkkel. Evervideo vil bla gjennom dine eksterne mapper og strømme videofiler direkte med ende-til-ende-kryptering.
{{% /details %}}

{{% details title="Støtter Evervideo Internxt og Proton Drive?" closed="true" %}}
Ja. Begge personvernfokuserte skyer støttes fra og med Evervideo 1.7. De slutter seg til MEGA og andre personvern-først-tjenester som allerede er tilgjengelige i appen.
{{% /details %}}

{{% details title="Hvordan fungerer de nye avspillingsbevegelsene?" closed="true" %}}
I fullskjerm-videoavspilling, **dobbelttrykk på høyre side** for å hoppe fremover og **dobbelttrykk på venstre side** for å hoppe tilbake med et konfigurerbart intervall (standard 10 sekunder — endre det i Innstillinger). **Trykk og hold** hvor som helst på skjermen for å midlertidig øke til 2x; slipp for å gå tilbake til normalt. **Enkelttrykk** hvor som helst for å veksle avspillingskontrollene (vis eller skjul).
{{% /details %}}

{{% details title="Kan jeg endre dobbelttrykkets hoppintervall?" closed="true" %}}
Ja. Gå til **Innstillinger → Avspilling → Bevegelse-hoppintervall** og velg en verdi mellom 5 og 60 sekunder. De fleste brukere holder det på 10 eller 15 sekunder.
{{% /details %}}

{{% details title="Hva er Wi-Fi Drive i Evervideo?" closed="true" %}}
Wi-Fi Drive er Evervideos innebygde trådløse filoverføringsfunksjon. Den lar deg laste opp videoer fra datamaskinen din til iPhone eller iPad over ditt lokale Wi-Fi-nettverk — uten iTunes, uten kabler, uten skykonto. Du kan bruke hvilken som helst skrivebordsnettleser eller en WebDAV-klient som Mac Finder eller Windows Filutforsker. Se den [fullstendige Wi-Fi Drive-veiledningen](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Spiller Evervideo MKV, AVI og andre formater fra Plex eller Jellyfin?" closed="true" %}}
Ja. Evervideo spiller praktisk talt alle videoformater — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — og strømmer dem direkte fra Plex, Jellyfin, Emby og andre medieservere uten å kreve transkoding for de fleste kodeker. Dette betyr lavere CPU-belastning på serveren din og raskere oppstartstider.
{{% /details %}}

{{% details title="Er Evervideo 1.7 gratis å oppdatere?" closed="true" %}}
Ja. Evervideo er en gratis nedlasting fra App Store, og 1.7 er en gratis oppdatering for alle eksisterende brukere. De nye sky-integrasjonene, medieserver-støtten, avspillingsbevegelsene, Wi-Fi Drive-forbedringene og Liquid Glass-UI-en er en del av basisoppdateringen.
{{% /details %}}

{{% details title="Hvilke enheter er Evervideo 1.7 tilgjengelig på?" closed="true" %}}
Evervideo 1.7 kjører på iPhone, iPad og Mac. AirPlay og Chromecast lar deg caste avspillingen til en større skjerm. iCloud Drive-synkronisering holder biblioteket og innstillingene konsistente på tvers av enheter.
{{% /details %}}
