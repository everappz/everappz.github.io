---
title: "Evertag 4.2: Nye sky-tilkoblinger, innstillinger for tag-redigerer forklart"
date: 2026-05-09
description: "Evertag 4.2 legger til tilkoblinger til Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP og NFS, fornyer Wi-Fi Drive og oppdaterer grensesnittet for Liquid Glass. Dette innlegget forklarer også alle innstillinger i tag-redigereren — inkludert ID3v2.4 vs ID3v2.3, skalering av albumcover, duplisering av tagger, sky-opplastingsmoduser og de riktige valgene for Spotify og andre strømmetjenester."
keywords: ["Evertag 4.2", "Evertag-oppdatering", "ID3 tag-redigerer iPhone", "ID3v2.4 vs ID3v2.3", "redigere FLAC-tagger iOS", "redigere MP3-tagger iPhone", "redigere albumcover iOS", "tag-redigerer for Spotify", "tag-redigerer Plex", "tag-redigerer Apple Music", "Evertag sky tag-redigerer", "Internxt tag-redigerer", "Proton Drive tag-redigerer", "QNAP tag-redigerer", "Nextcloud tag-redigerer", "Amazon S3 tag-redigerer", "SFTP tag-redigerer iPhone", "FTP lyd tag-redigerer", "NFS tag-redigerer iPhone", "Wi-Fi Drive tag-redigerer", "duplisere ID3-tagger", "skalering av albumcover", "Liquid Glass-design", "lyd-metadata-redigerer iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Tag-redigerer", "ID3", "ID3v2.4", "ID3v2.3", "FLAC-tagger", "MP3-tagger", "Albumcover", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Hva er nytt"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Kort fortalt:** [Evertag 4.2](/products/evertag) er en stor oppdatering for lyd-tag-redigereren på iPhone, iPad og Mac. Vi har knust viktige feil i tag-redigering og lagt til 6+ nye sky- og servertilkoblinger — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** pluss protokollene **FTP**, **SFTP** og **NFS**. Wi-Fi Drive har fått et oppdatert grensesnitt, multivalgsmodus, en smartere opplastingskø og raskere overføringer. Hele appen er innstilt for **Liquid Glass**-designet. Dette innlegget går også i dybden i Evertags tag-redigerer-innstillinger — forklarer **ID3v2.4 vs ID3v2.3**, **skalering av albumcover**, **duplisering av tagger**, **sky-opplastingsmoduser**, **slett nedlastet fil** og nøyaktig hvilke alternativer du skal velge hvis du forbereder lyd for **Spotify**, **Apple Music**, **Plex**, **Jellyfin** eller en annen strømmetjeneste.

---

## Hei alle sammen!

En stor Evertag-oppdatering er her. Vi har knust viktige feil i tag-redigering og lagt til **6+ nye sky- og servertilkoblinger** for å gjøre det enklere enn noensinne å håndtere lyd-metadata — enten biblioteket ditt bor i en personvernfokusert sky, på et selvhostet NAS eller på en generisk FTP/SFTP/NFS-server.

[Last ned Evertag 4.2 fra App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) eller oppdater fra din nåværende versjon.

## Utvidet sky- og serverstøtte

Evertag kobler seg nå nativt til et bredere utvalg av sky- og selvhostede lagringsalternativer. Du kan redigere ID3-, MP4-, FLAC-, OGG- og APE-tagger på filer hvor som helst.

### Personvernfokusert skylagring: Internxt og Proton Drive

Hvis du bryr deg om ende-til-ende-kryptering og zero-knowledge-lagring, er to av de mest respekterte navnene innen personvern-først-skyer nå native i Evertag:

- **Internxt** — open source-spansk sky med post-kvantum-kryptering og GDPR-samsvar. Gratis nivå tilgjengelig.
- **Proton Drive** — ende-til-ende-kryptert lagring fra skaperne av Proton Mail og Proton VPN, basert i Sveits. Gratis nivå tilgjengelig og betalte abonnementer for større biblioteker.

Du kan nå redigere metadata direkte på lydfiler lagret i begge tjenestene — filen forblir kryptert under transport, og bare de nye taggene skrives tilbake.

### Selvhostede løsninger: QNAP, Nextcloud, Amazon S3

For brukere som driver sin egen infrastruktur:

- **QNAP** — native API-tilkobling til QNAP NAS-enheter. Rediger tagger på filer på QNAP-en din via lokalt Wi-Fi eller fjerntilgang.
- **Nextcloud** — koble til en hvilken som helst Nextcloud-instans, selvhostet eller administrert.
- **Amazon S3** — pek Evertag mot en hvilken som helst S3-bøtte (eller S3-kompatibel lagring som Backblaze B2, Wasabi, MinIO, Cloudflare R2) og rediger metadata på stedet.

### Nye nettverksprotokoller: FTP, SFTP, NFS

Evertag 4.2 legger til tre klassiske protokoller for brukere med egendefinerte servere, hjemmelaboratorier eller generiske NAS-enheter:

- **SFTP (SSH File Transfer Protocol)** — det riktige svaret for **sikker fjern-redigering av tagger fra din egen server**. SFTP kjører over SSH, så hele overføringen (autentisering og lyddata) er kryptert. Hvis du har en VPS, dedikert server eller Linux-maskin hjemme med SSH-tilgang, kan du redigere tagger på fjernfiler uten å eksponere noe annet. Støtter både passord- og nøkkelbasert autentisering.
- **FTP** — den langtidsetablerte standarden for filoverføring. Nyttig for eldre hjemme-NAS som eksponerer FTP men ikke har en native API-integrasjon.
- **NFS (Network File System)** — de facto-delingsprotokollen på Linux og de fleste NAS-enheter. Lavere overhead enn SMB på samme maskinvare.

> **Tips:** SFTP er protokollen du vil bruke til fjern-redigering over åpent internett. FTP og NFS brukes best i det lokale nettverket — ikke eksponer dem på internett med mindre du pakker dem inn i en VPN.

## Wi-Fi Drive-oppgraderinger

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) er Evertags innebygde funksjon for å **overføre lydfiler trådløst mellom datamaskinen din og iPhone eller iPad — uten iTunes, kabler eller skykonto**. Begge enhetene må være på samme Wi-Fi-nettverk.

I Evertag 4.2 får Wi-Fi Drive:

- **Oppdatert, moderne grensesnitt** — ryddigere, lettere å lese på et øyeblikk og oppdatert for Liquid Glass.
- **Multivalgsmodus** — velg flere filer eller mapper og handle på dem i grupper.
- **Smartere opplastingskø** — bedre fremskrittsfeedback og bedre motstandsdyktighet over for nettverksforstyrrelser.
- **Forbedret hastighet og overordnet pålitelighet** — raskere overføringer for store biblioteker.

Det er den raskeste måten å flytte en bunke lydfiler fra datamaskinen til telefonen, redigere taggene deres og sende dem tilbake — uten noen tredjepartstjenester.

## Innstillinger for tag-redigerer: dypdykk

Dette er delen de fleste brukere aldri leser — og delen som avgjør om taggene dine fungerer overalt eller bare i noen apper. Åpne Evertag og gå til delen **innstillinger for lyd-tag-redigerer**. Her er hva hvert alternativ faktisk gjør, og hvilket du skal velge avhengig av målet ditt.

### Skalering av albumcover

Når du lagrer albumcoveret i en lydfil, kan Evertag skalere bildet før det innebygges. De tilgjengelige alternativene er:

- **Liten** — minst påvirkning på filstørrelsen, lavere bildekvalitet.
- **Middels** — balansert valg for de fleste brukere.
- **Stor** — høy kvalitet, egnet for spillere med store skjermer og CarPlay.
- **Ekstra stor** — svært høy kvalitet, merkbar økning i filstørrelse.
- **Original (Deaktivert)** — bygger inn coveret i den opprinnelige oppløsningen. **Ingen skalering.**

**Hvorfor dette betyr noe:**

- **Høyere kvalitet = større fil.** Et 3 000 × 3 000 piksler cover kan legge til flere MB til hver låt. Multipliser med et helt album, og diskbelastningen øker raskt.
- **Noen spillere håndterer ikke veldig store innebygde bilder bra.** Eldre enheter, noen bil-headunits og enkelte eldre desktop-spillere kan stoppe på cover over ~1 500 px eller nekte å vise dem.
- **For de fleste sky- og strømmingsarbeidsflyter** er **Middels** eller **Stor** det optimale punktet. Bruk **Original** kun når du spesifikt trenger arkivkvalitet eller forbereder filer for en spiller du har tillit til.

> **Original**-størrelsen er en del av Evertags premium-personaliseringsoppgradering. Standardstørrelser (Liten/Middels/Stor/Ekstra stor) er gratis.

### Tag-lagringsalternativer: ID3v2.4 vs ID3v2.3

Dette er den enkeltvis viktigste innstillingen for kompatibilitet. ID3v2 er metadataformatet som brukes inne i MP3-filer. Det finnes to mye brukte versjoner, og de skiller seg på subtile, men viktige måter.

#### ID3v2.4

- Nyere, støtter **UTF-8-tekstkoding** — riktig håndtering av ikke-latinske skrifter (kinesisk, russisk, japansk, arabisk, hebraisk osv.).
- Flere ramme-typer (relativ lydstyrke, equalizer-forhåndsinnstillinger osv.).
- **Anbefales for moderne spillere** som støtter den.

#### ID3v2.3

- Eldre, men **den mest universelt støttede** ID3-versjonen.
- Støtter ikke UTF-8 direkte (bruker UTF-16 for Unicode-tekst).
- **Anbefales når du trenger maksimal kompatibilitet** med eldre spillere, bilstereoanlegg og visse desktop-apper.

#### Når aktivere ID3v2.4 i Evertag

- Du bruker **moderne lydspillere** som Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (gjeldende versjoner) eller moderne Android-spillere. ✅ **Slå PÅ ID3v2.4.**
- Biblioteket ditt inneholder **ikke-latinske tegn** (kinesisk, koreansk, japansk, russisk, arabisk, gresk, hebraisk). ✅ **Slå PÅ ID3v2.4** — UTF-8 håndterer disse mye renere.

#### Når deaktivere ID3v2.4 i Evertag (bruk ID3v2.3 i stedet)

- Du forbereder filer for et **eldre bilstereo eller dashbord-enhet** som ikke leser v2.4-tagger.
- Du ser **forvansket tekst eller manglende tagger** i noen apper etter redigering — det er et sterkt signal om at v2.4 ikke støttes der. Bytt tilbake til v2.3.
- Du sikter mot **eldre desktop-spillere** eller eldre bærbare spillere (tidlige iPods, visse MP3-spillere fra 2000-2010-tallet).

> **Tommelfingerregel:** hvis taggene dine vises riktig overalt med v2.4, la den være på. Hvis bare én viktig spiller viser feil tegn, blanke felt eller ikke leser taggene dine, slå AV v2.4 og lagre på nytt.

#### Duplisering av tagger

Når du aktiverer **Duplisering av tagger**, skriver Evertag vanlige metadatafelter (tittel, artist, album osv.) i **både ID3v1- og ID3v2-seksjonene** av filen. Dette forbedrer kompatibilitet med svært gamle spillere som bare leser ID3v1 (det opprinnelige 128-byte tagget på slutten av filen).

- **De fleste brukere trenger ikke dette.** Moderne spillere leser ID3v2 først.
- **Aktiver det bare hvis** du arbeider med vintage-maskinvare eller spesifikk programvare som ignorerer ID3v2.

### Oppdatere online-filer: hvordan Evertag håndterer sky-redigeringer

Når du redigerer tagger på en fil lagret på en tilkoblet sky (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP osv.), må Evertag laste opp den endrede filen tilbake. Du kontrollerer hvordan:

- **Vis bekreftelsesmelding** *(standard, anbefalt)* — Evertag spør før opplasting. Best for forsiktige brukere og delte biblioteker.
- **Oppdater filens metadata automatisk** — laster opp stille etter hver redigering. Best for solo-brukere med raske, pålitelige tilkoblinger som redigerer mye.
- **Ikke oppdater filens metadata** — Evertag redigerer bare den lokale kopien. Nyttig for å forhåndsvise endringer uten å sende dem til skyen.

### Redigere online-filer: opprydding av lokal fil

For å redigere en fjernfil laster Evertag den først ned til enheten din. Etter redigering velger du hva som skjer med den lokale kopien:

- **Slett alltid nedlastet fil** — Evertag fjerner den midlertidige filen etter redigering. **Anbefalt** hvis du har lite lagringsplass eller jobber med andres filer.
- **Ikke slett nedlastet fil** — beholder den redigerte filen på enheten din. Nyttig hvis du ønsker både en offline-kopi og en oppdatert sky-kopi.

### Knapper på hovedskjermen

Hovedskjermen i Evertags tag-redigerer kan vise eller skjule knapper for individuelle operasjoner. Aktiver bare de du faktisk bruker for å holde grensesnittet fokusert:

- **Søk lyd-tagger automatisk** — finner manglende metadata online basert på filens lyd-fingeravtrykk.
- **Søk lyd-tagger manuelt** — søk etter tittel/artist når automatisk søk feiler.
- **Søk albumcover** — finner og bygger inn cover av høy kvalitet.
- **Lagre albumcover** — eksporterer det innebygde coveret til fotobiblioteket eller filene dine.
- **Normaliser koding** — fikser forvansket ikke-latinsk tekst forårsaket av gamle kodinger (svært nyttig for kyrilliske, kinesiske og japanske spor rippet med eldre programvare).
- **Slett lyd-tagger** — fjerner alle tagger fra en fil. Nyttig før en fersk om-tagging.

### Vis utvidede tagger

Slå dette på for å vise hele settet med metadatafelter utover grunnleggende tittel/artist/album/år — inkludert BPM, dirigent, opprinnelig artist, stemning, opphavsrett, encoder, kommentarer, sangtekster og mer. Power user-funksjon; de fleste vanlige brukere trenger ikke dette.

### Rediger filer samtidig

Når aktivert lar Evertag deg redigere metadata på **flere valgte filer på én gang** — sett samme album-artist, år eller sjanger for et helt album i én operasjon. Dette er den raskeste måten å rydde opp i et stort, uorganisert bibliotek.

## Redigere tagger for Spotify, Apple Music og strømmeplattformer

Et vanlig spørsmål: «jeg redigerte taggene mine i Evertag, lastet opp filene, og strømmetjenesten viser feil metadata. Hva skjer?»

Det korte svaret: **strømmetjenester respekterer ikke alltid dine lokale tagger.** Apple Music og Spotify har sine egne interne databaser — når de gjenkjenner et spor, overskriver de de viste metadataene med sine egne. Men for **opplastede filer**, dine lokale filer (Apple Music sin «Bibliotek»-funksjon, Spotify Local Files) og **distributør-opplastinger til strømmeplattformer**, betyr taggene dine absolutt noe. Slik stiller du inn Evertag for hvert scenario:

### Forberede filer for Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music håndterer UTF-8 riktig.
- **Albumcover: Stor** — Apples apper gjengir store cover godt; Original er overdrevet.
- **Duplisering av tagger: OFF** — ikke nødvendig.
- Sørg for at **Album Artist** er fylt ut riktig — Apple Music bruker den til gruppering.

### Forberede filer for Spotify Local Files

Spotify Local Files viser bare filer som er godt taggede. Taggene Spotify leser er begrensede.

- **ID3v2.4: ON** i de fleste tilfeller. Hvis et spor ikke vises riktig i Spotify etter redigering, **prøv å lagre med ID3v2.4: OFF** (altså som ID3v2.3) — Spotify sin parser har historisk vært konservativ overfor v2.4.
- **Albumcover: Middels eller Stor** — Spotify nedskaler det uansett.
- Fyll ut minst **Tittel**, **Artist**, **Album** og **Spornummer**.

### Forberede filer for distributør-opplasting (DistroKid, TuneCore, CD Baby osv.)

Hvis du er artist som laster opp ditt eget arbeid til strømmeplattformer, leser distributøren vanligvis tagger, men spør også om metadata i sitt grensesnitt. Uansett:

- **ID3v2.3** er ofte det tryggere standardvalget — mange distributør-pipelines ble bygget for år siden og foretrekker det eldre formatet.
- Bygg inn **Stort** cover (de fleste distributører krever cover ≥ 1 400 × 1 400 px — sjekk retningslinjene deres).
- Ikke stol på utvidede tagger — distributører leser bare kjernefelter.

### Forberede filer for Plex, Jellyfin, Navidrome, Subsonic, Emby

Disse selvhostede medieserverne er svært tolerante. De leser både v2.3 og v2.4 rent og håndterer UTF-8 godt.

- **ID3v2.4: ON** er greit.
- **Albumcover: Stor** eller **Ekstra stor** — disse serverne serverer cover til mobile klienter og CarPlay-skjermer, så kvalitet betyr noe.
- **Album Artist** sterkt anbefalt — det er det Plex/Jellyfin bruker for å gruppere album etter artist riktig.

### Forberede filer for bilstereoanlegg og eldre maskinvare

- **ID3v2.4: OFF** (bruk ID3v2.3) — eldre headunits støtter ofte ikke v2.4.
- **Albumcover: Middels** — mange bilskjermer stopper på store innebygde cover.
- **Duplisering av tagger: ON** — eldre bilstereoanlegg leser noen ganger bare ID3v1-fallback.

## Andre forbedringer

### Liquid Glass-design

Evertag 4.2 sitt grensesnitt er innstilt for Apples nye **Liquid Glass**-materiale i hele appen — gjennomskinnelige overflater, jevnere animasjoner og raffinerte kontroller som passer naturlig inn i iOS, iPadOS og macOS.

### Oppdaterte tilkoblingsbiblioteker

Vi har oppdatert de interne bibliotekene Evertag bruker for å snakke med **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** og andre tjenester. Resultatet: færre tilkoblingsfeil i kanttilfeller, bedre støtte for nyere serverversjoner og forbedret pålitelighet ved redigering av tagger på fjernfiler.

### Oversettelses- og lokaliseringsrettelser

Flere språkfikser i UI-en basert på direkte tilbakemeldinger fra brukere. Bedre tekstplassering på små knapper i flere språk.

### Mindre forbedringer inspirert av tilbakemeldingen din

Mange mindre forbedringer basert på App Store-anmeldelser og e-poster til support@everappz.com. Vi leser hver melding.

## Skaff deg Evertag 4.2

[**Last ned Evertag i App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) eller oppdater via App Store. Evertag er gratis å laste ned med valgfrie oppgraderinger i appen for avanserte funksjoner. De nye sky-tilkoblingene, nettverksprotokollene, Wi-Fi Drive-forbedringene og Liquid Glass-UI-en er en del av basisoppdateringen.

Hvis du liker appen, gi gjerne en vurdering i App Store — det hjelper virkelig. Har du tilbakemeldinger eller støtt på et problem? Send oss e-post på **support@everappz.com**. Vi leser hver melding.

## Vanlige spørsmål

{{% details title="Hva er nytt i Evertag 4.2?" closed="true" %}}
Evertag 4.2 legger til 6+ nye sky- og servertilkoblinger (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), oppdatert Wi-Fi Drive med multivalg og smartere opplastingskø, Liquid Glass UI-oppdateringer, oppdaterte tilkoblingsbiblioteker, viktige tag-redigeringsfeilrettelser og oversettelsesforbedringer.
{{% /details %}}

{{% details title="Skal jeg bruke ID3v2.4 eller ID3v2.3 i Evertag?" closed="true" %}}
Bruk **ID3v2.4** for moderne spillere (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, moderne Android-apper) og for biblioteker med ikke-latinske tegn — UTF-8-støtte betyr renere tagger på kinesisk, koreansk, japansk, russisk, arabisk og hebraisk. Bruk **ID3v2.3** hvis taggene dine vises feil i noen apper, hvis du sikter mot eldre bilstereoanlegg, eller hvis en strømme-distributør-pipeline avviser v2.4. Du kan alltid bytte og lagre på nytt.
{{% /details %}}

{{% details title="Hvorfor er taggene mine feil i Spotify etter redigering?" closed="true" %}}
Spotify viser for det meste metadata fra sin egen katalog — dine lokale tagger brukes bare for «Local Files» eller innhold du har lastet opp som artist. Hvis du tagger filer for Spotify Local Files og de ikke vises riktig, prøv å deaktivere ID3v2.4 i Evertag og lagre som ID3v2.3 — Spotify sin parser har historisk vært konservativ overfor v2.4.
{{% /details %}}

{{% details title="Hvilken albumcover-størrelse skal jeg velge i Evertag?" closed="true" %}}
For de fleste brukere: **Stor**. Det ser flott ut på telefoner, iPader, Maccer og moderne bilskjermer uten å blåse opp filene for mye. Bruk **Middels** hvis du har et stort bibliotek og vil spare diskplass. Bruk **Original** (ingen skalering) bare for arkivmastere eller når du virkelig trenger maksimal kvalitet — men vær oppmerksom på at noen eldre spillere sliter med svært store innebygde cover. **Original** er en del av Evertags premium-personaliseringsoppgradering.
{{% /details %}}

{{% details title="Vil større albumcover gjøre filene mine større?" closed="true" %}}
Ja. Å bygge inn et 3 000 × 3 000 px cover kan legge til flere megabyte til en enkelt lydfil. På et bibliotek med 1 000 spor blir det gigabyte. Hvis lagringsplassen er knapp, bruk Middels eller Stor; hvis du strømmer fra et NAS hvor størrelsen ikke betyr noe, er Ekstra stor eller Original greit.
{{% /details %}}

{{% details title="Hva er Duplisering av tagger og bør jeg aktivere det?" closed="true" %}}
Duplisering av tagger skriver kjerne-metadata til både ID3v1- (legacy 128-byte) og ID3v2-seksjonene (moderne) av filen. Aktiver det bare hvis du sikter mot svært gamle spillere eller maskinvare som leser ID3v1. For alt moderne (smarttelefoner, datamaskiner, nyere bilstereoanlegg), la det være av.
{{% /details %}}

{{% details title="Redigerer Evertag tagger direkte på sky-filer?" closed="true" %}}
Ja. Koble til skyen din (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 osv.) eller via FTP/SFTP/NFS, åpne en fil og rediger tagger som om den var lokal. Evertag laster ned filen, anvender redigeringene dine og laster opp den oppdaterte versjonen tilbake. Du kan velge mellom modusene «Spør alltid», «Auto-opplasting» eller «Ikke last opp» i innstillingene.
{{% /details %}}

{{% details title="Kan jeg redigere FLAC-tagger på iPhone med Evertag?" closed="true" %}}
Ja. Evertag støtter FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE og andre viktige formater med full lese-/skrivestøtte for tagger inkludert innebygd cover.
{{% /details %}}

{{% details title="Hvordan redigerer jeg tagger sikkert på hjemme-serveren min med SFTP?" closed="true" %}}
Åpne Evertag, gå til Tilkoblinger, velg SFTP, og oppgi serverens vertsnavn eller IP, port (vanligvis 22), brukernavn og enten et passord eller en privat SSH-nøkkel. Evertag blar gjennom de eksterne mappene dine og redigerer tagger direkte med ende-til-ende-kryptering over SSH.
{{% /details %}}

{{% details title="Kan jeg redigere tagger på flere filer på én gang?" closed="true" %}}
Ja. Aktiver **Rediger filer samtidig** i innstillingene. Velg flere filer, åpne tag-redigereren, og ethvert felt du endrer vil bli anvendt på alle valgte filer. Det er den raskeste måten å sette samme album-artist, år eller sjanger på tvers av et helt album.
{{% /details %}}

{{% details title="Er oppdateringen til Evertag 4.2 gratis?" closed="true" %}}
Ja. Evertag er en gratis nedlasting fra App Store, og 4.2 er en gratis oppdatering for alle eksisterende brukere. De nye sky-integrasjonene, Wi-Fi Drive-forbedringene og Liquid Glass-UI-en er en del av basisoppdateringen.
{{% /details %}}

{{% details title="Hvilke enheter er Evertag 4.2 tilgjengelig på?" closed="true" %}}
Evertag 4.2 kjører på iPhone, iPad og Mac. iCloud Drive-synkronisering holder tag-redigerer-innstillingene dine konsistente på tvers av enheter.
{{% /details %}}
