---
title: "Evertag 4.2: Nye sky-forbindelser, indstillinger for tag-editor forklaret"
date: 2026-05-09
description: "Evertag 4.2 tilføjer forbindelser til Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP og NFS, opdaterer Wi-Fi Drive og tilpasser brugerfladen til Liquid Glass. Denne post forklarer også hver eneste indstilling i tag-editoren — herunder ID3v2.4 vs ID3v2.3, skalering af albumcover, duplikering af tags, sky-uploadtilstande og de rigtige valg for Spotify og andre streamingtjenester."
keywords: ["Evertag 4.2", "Evertag-opdatering", "ID3 tag-editor iPhone", "ID3v2.4 vs ID3v2.3", "rediger FLAC-tags iOS", "rediger MP3-tags iPhone", "rediger albumcover iOS", "tag-editor til Spotify", "tag-editor Plex", "tag-editor Apple Music", "Evertag sky tag-editor", "Internxt tag-editor", "Proton Drive tag-editor", "QNAP tag-editor", "Nextcloud tag-editor", "Amazon S3 tag-editor", "SFTP tag-editor iPhone", "FTP lyd tag-editor", "NFS tag-editor iPhone", "Wi-Fi Drive tag-editor", "duplikere ID3-tags", "albumcover-skalering", "Liquid Glass-design", "lyd-metadata-editor iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Tag-editor", "ID3", "ID3v2.4", "ID3v2.3", "FLAC-tags", "MP3-tags", "Albumcover", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Hvad er nyt"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**Kort fortalt:** [Evertag 4.2](/products/evertag) er en stor opdatering til lyd-tag-editoren på iPhone, iPad og Mac. Vi har udryddet vigtige fejl i tag-redigering og tilføjet 6+ nye sky- og serverforbindelser — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** plus protokollerne **FTP**, **SFTP** og **NFS**. Wi-Fi Drive har fået en opdateret brugerflade, multivalgstilstand, en smartere uploadkø og hurtigere overførsler. Hele appen er afstemt til **Liquid Glass**-designet. Denne post går også i dybden med Evertags tag-editor-indstillinger — forklarer **ID3v2.4 vs ID3v2.3**, **skalering af albumcover**, **duplikering af tags**, **sky-uploadtilstande**, **slet downloadet fil** og præcis hvilke valg du skal træffe, hvis du forbereder lyd til **Spotify**, **Apple Music**, **Plex**, **Jellyfin** eller en anden streamingtjeneste.

---

## Hej allesammen!

En stor Evertag-opdatering er her. Vi har udryddet vigtige fejl i tag-redigering og tilføjet **6+ nye sky- og serverforbindelser**, så du nemmere end nogensinde kan administrere dine lyd-metadata — uanset om dit bibliotek bor i en privatlivsfokuseret sky, på et selvhostet NAS eller på en generisk FTP/SFTP/NFS-server.

[Hent Evertag 4.2 i App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611), eller opdater fra din nuværende version.

## Udvidet sky- og serverunderstøttelse

Evertag forbinder sig nu nativt til en bredere vifte af sky- og selvhostede lagringsmuligheder. Du kan redigere ID3-, MP4-, FLAC-, OGG- og APE-tags på filer, hvor end de ligger.

### Privatlivsfokuseret sky-lager: Internxt og Proton Drive

Hvis du går op i ende-til-ende-kryptering og zero-knowledge-lagring, er to af de mest respekterede navne inden for privatlivsfokuserede skyer nu native i Evertag:

- **Internxt** — open source-spansk sky med post-kvantum-kryptering og GDPR-overensstemmelse. Gratis niveau tilgængeligt.
- **Proton Drive** — ende-til-ende-krypteret lager fra holdet bag Proton Mail og Proton VPN, baseret i Schweiz. Gratis niveau tilgængeligt og betalte abonnementer for større biblioteker.

Du kan nu redigere metadata direkte på lydfiler, der er gemt i en af de to tjenester — filen forbliver krypteret under transport, og kun de nye tags skrives tilbage.

### Selvhostede løsninger: QNAP, Nextcloud, Amazon S3

Til brugere, der driver deres egen infrastruktur:

- **QNAP** — native API-forbindelse til QNAP NAS-enheder. Rediger tags på filer på din QNAP via lokalt Wi-Fi eller fjernadgang.
- **Nextcloud** — forbind til en hvilken som helst Nextcloud-instans, selvhostet eller administreret.
- **Amazon S3** — peg Evertag mod en hvilken som helst S3-bucket (eller S3-kompatibel lagring som Backblaze B2, Wasabi, MinIO, Cloudflare R2), og rediger metadata på stedet.

### Nye netværksprotokoller: FTP, SFTP, NFS

Evertag 4.2 tilføjer tre klassiske protokoller for brugere med specialservere, hjemmelaboratorier eller generiske NAS-enheder:

- **SFTP (SSH File Transfer Protocol)** — det rigtige svar på **sikker fjern-redigering af tags fra din egen server**. SFTP kører ovenpå SSH, så hele overførslen (autentificering og lyddata) er krypteret. Hvis du har en VPS, dedikeret server eller Linux-maskine derhjemme med SSH-adgang, kan du redigere tags på fjernfiler uden at eksponere noget andet. Understøtter både adgangskode- og nøglebaseret autentificering.
- **FTP** — den langtidsetablerede standard for filoverførsel. Nyttig til ældre hjemme-NAS, der eksponerer FTP, men ikke har en native API-integration.
- **NFS (Network File System)** — det de facto delingsprotokol på Linux og de fleste NAS-enheder. Lavere overhead end SMB på samme hardware.

> **Tip:** SFTP er protokollen, du vil bruge til fjern-redigering over det åbne internet. FTP og NFS er bedst i det lokale netværk — eksponer dem ikke mod internettet, medmindre de pakkes ind i et VPN.

## Wi-Fi Drive-opgraderinger

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) er Evertags indbyggede funktion til **trådløs overførsel af lydfiler mellem din computer og iPhone eller iPad — uden iTunes, kabler eller skykonto**. Begge enheder skal være på det samme Wi-Fi-netværk.

I Evertag 4.2 får Wi-Fi Drive:

- **Opdateret, moderne brugerflade** — renere, lettere at læse hurtigt og opdateret til Liquid Glass.
- **Multivalgstilstand** — vælg flere filer eller mapper og handl på dem i grupper.
- **Smartere uploadkø** — bedre fremskridtsfeedback og bedre modstandsdygtighed over for netværksudfald.
- **Forbedret hastighed og overordnet pålidelighed** — hurtigere overførsler for store biblioteker.

Det er den hurtigste måde at flytte en bunke lydfiler fra computeren til telefonen, redigere deres tags og sende dem tilbage — uden tredjepartstjenester.

## Indstillinger for tag-editor: dybt dyk

Det er den del, de fleste brugere aldrig læser — og den del, der afgør, om dine tags fungerer overalt eller kun i nogle apps. Åbn Evertag, og gå til afsnittet **indstillinger for lyd-tag-editor**. Her er, hvad hver indstilling faktisk gør, og hvilken du skal vælge afhængigt af dit mål.

### Skalering af albumcover

Når du gemmer albumcoveret i en lydfil, kan Evertag skalere billedet ned, før det indlejres. De tilgængelige indstillinger er:

- **Lille** — mindst indvirkning på filstørrelse, lavere billedkvalitet.
- **Mellem** — afbalanceret valg for de fleste brugere.
- **Stor** — høj kvalitet, velegnet til afspillere med store skærme og CarPlay.
- **Ekstra stor** — meget høj kvalitet, mærkbar stigning i filstørrelse.
- **Original (Deaktiveret)** — indlejrer coveret i den oprindelige opløsning. **Ingen skalering.**

**Hvorfor det betyder noget:**

- **Højere kvalitet = større fil.** Et 3.000 × 3.000 pixel cover kan tilføje flere MB til hvert spor. Gang det med et helt album, og diskforbruget hober sig hurtigt op.
- **Nogle afspillere håndterer ikke meget store indlejrede billeder godt.** Ældre enheder, visse bil-headunits og nogle ældre desktop-afspillere kan gå i stå ved covers over ~1.500 px eller nægte at vise dem.
- **Til de fleste sky- og streaming-arbejdsgange** er **Mellem** eller **Stor** sweet spot. Brug kun **Original**, når du specifikt har brug for arkivkvalitet eller forbereder filer til en afspiller, du har tillid til.

> **Original**-indstillingen er en del af Evertags premium personalisering-opgradering. Standardstørrelser (Lille/Mellem/Stor/Ekstra stor) er gratis.

### Tag-gemmemuligheder: ID3v2.4 vs ID3v2.3

Det er den enkelteste vigtigste indstilling for kompatibilitet. ID3v2 er metadataformatet inde i MP3-filer. Der er to udbredte versioner, og de adskiller sig på subtile, men vigtige måder.

#### ID3v2.4

- Nyere, understøtter **UTF-8-tekstkodning** — korrekt håndtering af ikke-latinske skrifter (kinesisk, russisk, japansk, arabisk, hebraisk osv.).
- Flere frame-typer (relativ lydstyrke, equalizer-præsæter osv.).
- **Anbefales til moderne afspillere**, der understøtter den.

#### ID3v2.3

- Ældre, men **den mest universelt understøttede** ID3-version.
- Understøtter ikke UTF-8 direkte (bruger UTF-16 til Unicode-tekst).
- **Anbefales, når du har brug for maksimal kompatibilitet** med ældre afspillere, bilstereoanlæg og visse desktop-apps.

#### Hvornår skal du aktivere ID3v2.4 i Evertag

- Du bruger **moderne lydafspillere** som Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (nuværende versioner) eller moderne Android-afspillere. ✅ **Aktivér ID3v2.4.**
- Dit bibliotek indeholder **ikke-latinske tegn** (kinesisk, koreansk, japansk, russisk, arabisk, græsk, hebraisk). ✅ **Aktivér ID3v2.4** — UTF-8 håndterer dem meget renere.

#### Hvornår skal du deaktivere ID3v2.4 i Evertag (brug ID3v2.3 i stedet)

- Du forbereder filer til et **ældre bilstereo eller dashboard-enhed**, der ikke læser v2.4-tags.
- Du ser **forvansket tekst eller manglende tags** i nogle apps efter redigering — det er et stærkt signal om, at v2.4 ikke understøttes der. Skift tilbage til v2.3.
- Du sigter mod **ældre desktop-afspillere** eller ældre bærbare afspillere (tidlige iPods, visse MP3-afspillere fra 2000-2010'erne).

> **Tommelfingerregel:** hvis dine tags vises korrekt overalt med v2.4, så lad den være tændt. Hvis bare én vigtig afspiller viser forkerte tegn, blanke felter eller ikke kan læse dine tags, deaktivér v2.4 og gem igen.

#### Duplikere tags

Når du aktiverer **Duplikere tags**, skriver Evertag fælles metadatafelter (titel, kunstner, album osv.) i **både ID3v1- og ID3v2-sektionerne** af filen. Det forbedrer kompatibiliteten med meget gamle afspillere, der kun læser ID3v1 (det oprindelige 128-byte tag i slutningen af filen).

- **De fleste brugere har ikke brug for det.** Moderne afspillere læser ID3v2 først.
- **Aktivér det kun, hvis** du arbejder med vintage hardware eller specifik software, der ignorerer ID3v2.

### Opdater online-filer: hvordan Evertag håndterer sky-redigeringer

Når du redigerer tags på en fil gemt i en tilsluttet sky (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP osv.), skal Evertag uploade den ændrede fil tilbage. Du styrer hvordan:

- **Vis bekræftelsesbesked** *(standard, anbefalet)* — Evertag spørger før upload. Bedst for forsigtige brugere og delte biblioteker.
- **Opdater filens metadata automatisk** — uploader stille efter hver redigering. Bedst for solo-brugere med hurtige, pålidelige forbindelser, der redigerer meget.
- **Opdater ikke filens metadata** — Evertag redigerer kun den lokale kopi. Nyttigt til at se ændringer uden at skubbe dem til skyen.

### Rediger online-filer: oprydning af lokal fil

For at redigere en fjernfil downloader Evertag den først til din enhed. Efter redigering vælger du, hvad der skal ske med den lokale kopi:

- **Slet altid downloadet fil** — Evertag fjerner den midlertidige fil efter redigering. **Anbefalet**, hvis du har lidt lager eller arbejder med andres filer.
- **Slet ikke downloadet fil** — beholder den redigerede fil på din enhed. Nyttigt, hvis du både vil have en offline-kopi og en opdateret sky-kopi.

### Knapper på hovedskærmen

Hovedskærmen i Evertags tag-editor kan vise eller skjule knapper for individuelle handlinger. Aktivér kun dem, du faktisk bruger, for at holde brugerfladen fokuseret:

- **Søg lyd-tags automatisk** — finder manglende metadata online baseret på filens lydfingeraftryk.
- **Søg lyd-tags manuelt** — søg efter titel/kunstner, når den automatiske søgning fejler.
- **Søg albumcover** — finder og indlejrer covers af høj kvalitet.
- **Gem albumcover** — eksporterer det indlejrede cover til dit fotobibliotek eller dine filer.
- **Normaliser kodning** — retter forvansket ikke-latinsk tekst forårsaget af gamle kodninger (meget nyttigt for kyrilliske, kinesiske og japanske spor rippet med ældre software).
- **Slet lyd-tags** — fjerner alle tags fra en fil. Nyttigt før en frisk om-tagning.

### Vis udvidede tags

Slå dette til for at vise hele sættet af metadatafelter ud over titel/kunstner/album/år — herunder BPM, dirigent, oprindelig kunstner, stemning, copyright, encoder, kommentarer, tekster og mere. Power user-funktion; de fleste almindelige brugere har ikke brug for det.

### Rediger filer samtidig

Når aktiveret lader Evertag dig redigere metadata på **flere valgte filer på én gang** — sæt den samme album-kunstner, år eller genre for et helt album i én operation. Det er den hurtigste måde at rydde op i et stort, uorganiseret bibliotek på.

## Redigering af tags til Spotify, Apple Music og streamingplatforme

Et almindeligt spørgsmål: «jeg redigerede mine tags i Evertag, uploadede filerne, og streamingtjenesten viser forkerte metadata. Hvad sker der?»

Det korte svar: **streamingtjenester respekterer ikke altid dine lokale tags.** Apple Music og Spotify har deres egne interne databaser — når de genkender et nummer, overskriver de de viste metadata med deres egne. Men for **uploadede filer**, dine lokale filer (Apple Musics «Bibliotek»-funktion, Spotify Local Files) og **distributør-uploads til streamingplatforme** betyder dine tags absolut noget. Sådan indstiller du Evertag i hvert scenarie:

### Forberedelse af filer til Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music håndterer UTF-8 korrekt.
- **Albumcover: Stor** — Apples apps gengiver store covers godt; Original er overdrevet.
- **Duplikere tags: OFF** — ikke nødvendigt.
- Sørg for, at **Album Artist** er udfyldt korrekt — Apple Music bruger det til gruppering.

### Forberedelse af filer til Spotify Local Files

Spotify Local Files viser kun filer, der er godt taggede. De tags, Spotify læser, er begrænsede.

- **ID3v2.4: ON** i de fleste tilfælde. Hvis et nummer ikke vises korrekt i Spotify efter redigering, **prøv at gemme med ID3v2.4: OFF** (altså som ID3v2.3) — Spotifys parser har historisk været konservativ over for v2.4.
- **Albumcover: Mellem eller Stor** — Spotify skalerer det alligevel ned.
- Udfyld mindst **Titel**, **Kunstner**, **Album** og **Spornummer**.

### Forberedelse af filer til distributør-upload (DistroKid, TuneCore, CD Baby osv.)

Hvis du er kunstner og uploader dit eget arbejde til streamingplatforme, læser distributøren typisk tags, men beder også om metadata i deres brugerflade. Uanset hvad:

- **ID3v2.3** er ofte det sikrere standardvalg — mange distributørpipelines blev bygget for år siden og foretrækker det ældre format.
- Indlejr **Stort** cover (de fleste distributører kræver covers ≥ 1.400 × 1.400 px — tjek deres retningslinjer).
- Stol ikke på udvidede tags — distributører læser kun kernefelter.

### Forberedelse af filer til Plex, Jellyfin, Navidrome, Subsonic, Emby

Disse selvhostede medieservere er meget tolerante. De læser både v2.3 og v2.4 rent og håndterer UTF-8 godt.

- **ID3v2.4: ON** er fint.
- **Albumcover: Stor** eller **Ekstra stor** — disse servere serverer covers til mobile klienter og CarPlay-skærme, så kvaliteten betyder noget.
- **Album Artist** anbefales kraftigt — det er, hvad Plex/Jellyfin bruger til at gruppere albummer efter kunstner korrekt.

### Forberedelse af filer til bilstereoanlæg og ældre hardware

- **ID3v2.4: OFF** (brug ID3v2.3) — ældre headunits understøtter ofte ikke v2.4.
- **Albumcover: Mellem** — mange biludstillinger går i stå ved store indlejrede covers.
- **Duplikere tags: ON** — ældre bilstereoanlæg læser nogle gange kun ID3v1-fallback'en.

## Andre forbedringer

### Liquid Glass-design

Evertag 4.2's brugerflade er afstemt til Apples nye **Liquid Glass**-materiale i hele appen — gennemskinnelige overflader, jævnere animationer og forfinede betjeningselementer, der falder naturligt ind i iOS, iPadOS og macOS.

### Opdaterede forbindelsesbiblioteker

Vi har opdateret de interne biblioteker, som Evertag bruger til at tale med **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** og andre tjenester. Resultatet: færre forbindelsesfejl i kantsager, bedre understøttelse af nyere serverversioner og forbedret pålidelighed ved redigering af tags på fjernfiler.

### Oversættelses- og lokaliseringsrettelser

Flere sprogfixes i UI'en baseret på direkte feedback fra brugere. Bedre tekstplacering på små knapper i flere sprog.

### Mindre forbedringer inspireret af din feedback

Mange mindre forbedringer baseret på App Store-anmeldelser og e-mails til support@everappz.com. Vi læser hver besked.

## Hent Evertag 4.2

[**Hent Evertag i App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611), eller opdater fra App Store. Evertag er en gratis download med valgfrie in-app-opgraderinger til avancerede funktioner. De nye sky-forbindelser, netværksprotokoller, Wi-Fi Drive-forbedringer og Liquid Glass-UI er en del af basisopdateringen.

Hvis du kan lide appen, så efterlad gerne en bedømmelse i App Store — det hjælper virkelig. Har du feedback eller stødt på et problem? Skriv til os på **support@everappz.com**. Vi læser hver besked.

## Ofte stillede spørgsmål

{{% details title="Hvad er nyt i Evertag 4.2?" closed="true" %}}
Evertag 4.2 tilføjer 6+ nye sky- og serverforbindelser (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), et opdateret Wi-Fi Drive med multivalg og smartere uploadkø, Liquid Glass UI-opdateringer, opdaterede forbindelsesbiblioteker, vigtige tag-redigeringsfejlrettelser og oversættelsesforbedringer.
{{% /details %}}

{{% details title="Skal jeg bruge ID3v2.4 eller ID3v2.3 i Evertag?" closed="true" %}}
Brug **ID3v2.4** til moderne afspillere (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, moderne Android-apps) og til biblioteker med ikke-latinske tegn — UTF-8-understøttelse betyder renere tags på kinesisk, koreansk, japansk, russisk, arabisk og hebraisk. Brug **ID3v2.3**, hvis dine tags vises forkert i nogle apps, hvis du sigter mod ældre bilstereoanlæg, eller hvis en streaming-distributørpipeline afviser v2.4. Du kan altid skifte og gemme igen.
{{% /details %}}

{{% details title="Hvorfor er mine tags forkerte i Spotify efter redigering?" closed="true" %}}
Spotify viser for det meste metadata fra deres eget katalog — dine lokale tags bruges kun til «Local Files» eller indhold, du har uploadet som kunstner. Hvis du tagger filer til Spotify Local Files, og de ikke vises korrekt, så prøv at deaktivere ID3v2.4 i Evertag og gem som ID3v2.3 — Spotifys parser har historisk været konservativ over for v2.4.
{{% /details %}}

{{% details title="Hvilken albumcover-størrelse skal jeg vælge i Evertag?" closed="true" %}}
For de fleste brugere: **Stor**. Det ser fantastisk ud på telefoner, iPads, Macs og moderne biludstillinger uden at oppuste filerne for meget. Brug **Mellem**, hvis du har et stort bibliotek og vil spare diskplads. Brug kun **Original** (ingen skalering) til arkivmastere, eller når du virkelig har brug for maksimal kvalitet — men vær opmærksom på, at nogle ældre afspillere kæmper med meget store indlejrede covers. **Original** er en del af Evertags premium personalisering-opgradering.
{{% /details %}}

{{% details title="Vil større albumcovers gøre mine filer større?" closed="true" %}}
Ja. At indlejre et 3.000 × 3.000 px cover kan tilføje flere megabytes til en enkelt lydfil. På et bibliotek med 1.000 spor løber det op i gigabytes. Hvis lagerpladsen er knap, så brug Mellem eller Stor; hvis du streamer fra et NAS, hvor størrelsen ikke betyder noget, er Ekstra stor eller Original fint.
{{% /details %}}

{{% details title="Hvad er Duplikere tags, og skal jeg aktivere det?" closed="true" %}}
Duplikere tags skriver kerne-metadata til både ID3v1- (legacy 128-byte) og ID3v2-sektionerne (moderne) af filen. Aktivér det kun, hvis du sigter mod meget gamle afspillere eller hardware, der læser ID3v1. For alt moderne (smartphones, computere, nyere bilstereoanlæg) lad det være slukket.
{{% /details %}}

{{% details title="Redigerer Evertag tags direkte på sky-filer?" closed="true" %}}
Ja. Forbind til din sky (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 osv.) eller via FTP/SFTP/NFS, åbn en fil og rediger tags, som om den var lokal. Evertag downloader filen, anvender dine redigeringer og uploader den opdaterede version tilbage. Du kan vælge mellem tilstandene «Spørg altid», «Auto-upload» eller «Upload ikke» i indstillingerne.
{{% /details %}}

{{% details title="Kan jeg redigere FLAC-tags på iPhone med Evertag?" closed="true" %}}
Ja. Evertag understøtter FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE og andre vigtige formater med fuld læse-/skrivestøtte til tags inklusive indlejret cover.
{{% /details %}}

{{% details title="Hvordan redigerer jeg sikkert tags på min hjemmeserver med SFTP?" closed="true" %}}
Åbn Evertag, gå til Forbindelser, vælg SFTP, og indtast serverens hostnavn eller IP, port (normalt 22), brugernavn og enten en adgangskode eller en privat SSH-nøgle. Evertag gennemser dine fjernmapper og redigerer tags direkte med ende-til-ende-kryptering over SSH.
{{% /details %}}

{{% details title="Kan jeg redigere tags på flere filer på én gang?" closed="true" %}}
Ja. Aktivér **Rediger filer samtidig** i indstillingerne. Vælg flere filer, åbn tag-editoren, og ethvert felt, du ændrer, vil blive anvendt på alle valgte filer. Det er den hurtigste måde at sætte den samme album-kunstner, år eller genre på tværs af et helt album.
{{% /details %}}

{{% details title="Er opdateringen til Evertag 4.2 gratis?" closed="true" %}}
Ja. Evertag er en gratis download fra App Store, og 4.2 er en gratis opdatering for alle eksisterende brugere. De nye sky-integrationer, Wi-Fi Drive-forbedringer og Liquid Glass-UI er en del af basisopdateringen.
{{% /details %}}

{{% details title="Hvilke enheder er Evertag 4.2 tilgængelig på?" closed="true" %}}
Evertag 4.2 kører på iPhone, iPad og Mac. iCloud Drive-synkronisering holder dine tag-editor-indstillinger konsistente på tværs af enheder.
{{% /details %}}
