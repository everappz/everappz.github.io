---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: 'Ofte stillede spørgsmål'
description: 'Find svar på almindelige spørgsmål om Evermusic, Flacbox, Evervideo og Evertag. Udforsk funktioner som cloud-streaming, filhåndtering, afspilningsmuligheder, metadataredigering og meget mere.'
keywords: [
  "Evermusic FAQ", "Flacbox support", "Evervideo hjælp", "Evertag spørgsmål",
  "hvordan bruger jeg Evermusic", "fejlfinding af cloud musikafspiller", "guide til offline afspilning",
  "support til lydtageditor", "problemer med videostreaming", "vejledning til filoverførsel"
]
tags: [
  "FAQ", "hjælp", "support", "evermusic", "flacbox", "evervideo", "evertag",
  "skyopsætning", "afspilningsproblemer", "filhåndtering", "metadataredigering",
  "fejlfinding", "offline-tilstand", "musikafspiller", "videoafspiller"
]
aliases:
  - /blog/categories/how-to/
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## Lær at bruge vores apps

Leder du efter svar eller hjælp til at bruge en af vores apps? Du er det rette sted.

Vores FAQ-sider hjælper dig med at forbinde skylager, administrere musik- og videofiler, opsætte offline afspilning, justere ekvalisatorindstillinger, rette metadata og meget mere.

Udforsk FAQ'en til din app nedenfor for at komme i gang, eller gennemse almindelige spørgsmål og svar, vi har modtaget fra bruger-e-mails.

## Vælg din app

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="Afspil 360°-videoer, stream fra iCloud, se med undertekster, anvend en videoekvalisator, organiser indhold med afspilningslister og download videoer til offline visning."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="Skymusikafspiller med offline-tilstand, lydekvalisator, crossfade, gapless afspilning, administration af afspilningslister, komplet musikbibliotek og indbygget filhåndtering."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="Højopløsnings lydafspiller til iPhone og Mac. Lyt til tabsfri formater som FLAC, ALAC, APE og DSD. Finjuster output med avancerede lydindstillinger."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="Smart musiktageditor med batchredigering. Ret manglende metadata, albumomslag og mere. Rediger ID3-, FLAC-, APE-tags — over 120 felter understøttet." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## Almindelige problemer og svar

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="Hvorfor kan jeg ikke logge ind på pCloud på en ældre iOS-version (15.8.4)?" closed="true" %}}
pClouds webloginside vises muligvis ikke korrekt på ældre iOS-versioner som 15.8.4, hvilket forhindrer indtastning af din e-mail og adgangskode på skærmen til cloud-forbindelsen.<br><br>

Som alternativ kan du bruge **WebDAV**-protokollen, som understøttes af pCloud og fungerer pålideligt på alle iOS-versioner.

**WebDAV-opsætning:**<br>
- **US-servere:** `https://webdav.pcloud.com`  
- **Europæiske servere:** `https://ewebdav.pcloud.com`  
- **Brugernavn:** Din pCloud-e-mailadresse  
- **Adgangskode:** Din pCloud-kontoadgangskode  

Åbn appen → Forbindelser → Opret forbindelse til skylager → Vælg **WebDAV** → Indtast dine legitimationsoplysninger og server-URL.

Denne metode giver dig mulighed for at oprette forbindelse til dit pCloud-lager og få adgang til dine filer uden problemer på ældre enheder.
{{% /details %}}

{{% details title="Hvordan afspiller jeg musik via AirPlay fra Mac (macOS)?" closed="true" %}}
macOS-versionen af appen inkluderer ikke indbyggede AirPlay-, Chromecast- eller Bluetooth-forbindelsesknapper som iOS.<br><br>

Følg disse trin for at bruge **AirPlay** på din MacBook Pro:

1. Gå til **øverste højre hjørne** af skærmen og åbn **Kontrolcenter** (nær uret).  
2. Klik på ikonet **Lyd/Lydstyrke**.  
3. På den næste skærm klikker du på **AirPlay** for at se en liste over alle tilgængelige AirPlay-enheder.  
4. Vælg den ønskede enhed for at begynde at streame din musik.  

Dette vil dirigere al systemlyd (inklusive fra Evermusic eller Flacbox) til din valgte AirPlay-enhed.
{{% /details %}}

{{% details title="Hvorfor er mit Premium-køb ikke aktiveret på Mac, hvis jeg købte det på iPhone?" closed="true" %}}
Livstidskøb og abonnementer synkroniseres mellem iOS og Mac via **iCloud**.<br><br>

Sådan aktiverer du Premium på din Mac:<br>
- Sørg for at have den nyeste app-version installeret på begge enheder<br>
- Aktivér **iCloud** på begge enheder<br>
- Start appen på din iOS-enhed og vent 1 minut på, at købsoplysningerne uploades<br>
- På din Mac skal du installere appen fra App Store med det **samme Apple ID**<br>
- Start appen og vent et par sekunder på, at oplysningerne synkroniseres<br>
- Alternativt kan du trykke på **Gendan køb** i appens indstillinger på begge enheder<br><br>

Dine Premium-funktioner bør derefter automatisk aktiveres på Mac.
{{% /details %}}

{{% details title="Hvordan synkroniserer jeg afspilningslister automatisk mellem enheder?" closed="true" %}}
Der er i øjeblikket **ingen automatisk synkronisering** af afspilningslister.<br><br>

Du kan bruge en af følgende muligheder:<br>
- **Sikkerhedskopiering og gendannelse** fra appindstillinger [Sådan overfører du dit musikbibliotek mellem enheder i Evermusic: trin-for-trin guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **Eksporter afspilningsliste til M3U** og importer på en anden enhed:<br>
  - [Sådan eksporterer du afspilningslister](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [Sådan importerer du afspilningslister](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **Arkiver afspilningsliste eller albums** og overfør via ZIP:<br>
  - [Guide til arkivering af afspilningslister](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="Er det sikkert at bruge jeres apps? Kan jeg deaktivere analyser?" closed="true" %}}
Ja, dit privatliv er vores højeste prioritet.<br><br>

- Alle data — musikfiler, indstillinger, cloud-logins — forbliver på din enhed<br>
- Loginoplysninger gemmes sikkert i **iOS Keychain**<br>
- Vi indsamler kun anonyme fejl- og brugsrapporter<br>
- Du kan fravælge det i **Appindstillinger → Analyser**<br><br>

Mere info:<br>
- [Privatlivspolitik](/legal/privacy-policy/)<br>
- [Apple Keychain-sikkerhed](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

Ved brug af personaliserede annoncer kræver Google Mobile Ads, at samtykkesindstillinger vises.<br>
Premium-brugere ser ingen annoncer, og annonce-SDK'et er fuldstændig deaktiveret.
{{% /details %}}

{{% details title="Understøtter jeres apps Familiedeling?" closed="true" %}}
Ja, Familiedeling understøttes.<br><br>

Sådan deler du køb i appen:<br>
- Sørg for, at købet er indstillet til at blive delt med din familiegruppe<br>
- På familiemedlemmets enhed skal du gå til **Indstillinger > Køb > Gendan køb**<br>
- Dette vil anmode om købsdata fra Apples servere og aktivere det på deres enhed
{{% /details %}}

{{% details title="Hvordan fremskynder jeg metadata og cloud-synkronisering?" closed="true" %}}
For at forbedre synkroniseringshastigheden skal du aktivere baggrundsopgaver:<br><br>

- **Indstillinger → Musikbibliotek → Metadatalæsning → Metadatalæsning i baggrunden**<br>
- **Indstillinger → Musikbibliotek → Online musiksynkronisering → Baggrundsynkronisering**<br><br>

På macOS kan du desuden øge metadatalæsningshastigheden via **Indstillinger → Musikbibliotek**.<br>
Hvis afspilleren er aktiv (lyd afspilles), vil iOS ikke suspendere appen, hvilket muliggør kontinuerlig synkronisering.
{{% /details %}}

{{% details title="Hvordan annullerer jeg mit abonnement?" closed="true" %}}
Du kan annullere dit abonnement via Apples officielle vejledning:<br>
👉 [Sådan annullerer du et abonnement](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="Hvordan forbinder og streamer jeg lyd fra WD MyCloud EX2 Ultra?" closed="true" %}}

Når du tilføjer en forbindelse i appen via **Forbindelser > Opret forbindelse til skylager > My Cloud Home**, er det officielt designet til at understøtte **WD MyCloud Home**-enheder.<br>
WD MyCloud EX2 Ultra bruger begrænset adgang for apps.<br><br>

Hvis du dog har forbundet dig til en **WD MyCloud EX2 Ultra**, **WD MyCloud Mirror** eller et andet **WD MyCloud**-lagermodel, kan du stadig bruge den med følgende løsning:<br><br>

1. Åbn **Forbindelser → Opret forbindelse til skylager → My Cloud Home**<br>
2. Opret en mappe med den indbyggede filhåndtering<br>
3. Upload musikfiler til denne mappe<br>
4. Disse gemmes i en "sandbox", der kun er tilgængelig for appen<br>
5. Du kan nu streame eller downloade dem direkte<br><br>

⚠️ Kun mapper oprettet via appen vil være tilgængelige fra NAS-enheden.
{{% /details %}}

{{% details title="Hvordan opretter jeg forbindelse til Koofr.eu?" closed="true" %}}
Du kan forbinde Koofr ved hjælp af **WebDAV**.<br><br>

- Koofr WebDAV-opsætningsguide: [koofr.eu blog](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Evermusic/Flacbox WebDAV-guide: [Sådan forbinder du NAS-lager med WebDAV og lytter til musik på din iPhone eller Mac](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="Hvad er appens URL-skemaer?" closed="true" %}}
Her er de understøttede skemaer:<br><br>

**Evermusic**<br>
- iOS (blåt ikon): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (rødt ikon): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="Musik stopper med at afspille, når appen er i baggrunden — hvordan løser jeg det?" closed="true" %}}
Hvis appen crasher eller sætter på pause i baggrunden:<br>
- Gå til **Indstillinger > Musikbibliotek > Online musiksynkronisering > Baggrundsynkronisering → Deaktiver**<br>
- **Indstillinger > Musikbibliotek > Metadatalæsning > Metadatalæsning i baggrunden → Deaktiver**<br>
- **Indstillinger > Filhåndtering > Baggrundsoverførsler → Deaktiver**
{{% /details %}}

{{% details title="Gapless afspilning virker ikke — hvordan løser jeg det?" closed="true" %}}
Gapless afspilning afhænger af iOS-versionen og lydmotoren.<br>
Prøv at skifte lydmotor:<br>
- Gå til **Indstillinger → Lydafspiller → Generelt → Lydprocessor**<br>
- Vælg **Core Audio** for bedre gapless-understøttelse
{{% /details %}}

{{% details title="Hvorfor viser appen kun 100 elementer på en liste?" closed="true" %}}
Appen bruger paginering for at forbedre ydeevnen.<br>
Sådan deaktiverer du det:<br>
- Gå til **Indstillinger → Tilpasning → Grænse for indlæsning af indhold → Deaktiveret**<br>
Nu indlæses alle elementer på én gang.
{{% /details %}}

{{% details title="Hvorfor er der mærkelige tegn i metadata?" closed="true" %}}
Prøv at aktivere metadatanormalisering:<br>
- **Indstillinger → Musikbibliotek → Metadatalæsning → Normaliser metadatakodning**
{{% /details %}}

{{% details title="Hvorfor kan appen ikke læse mappenavne med specialtegn?" closed="true" %}}
Dette er et kendt problem med **SMB2-protokollen**.<br><br>

Prøv følgende løsninger:<br>
- Aktivér **SMB1** på din server og i appindstillingerne<br>
- Brug **systemfilvælgeren**:<br>
  - Gå til **Lokale filer > Filer på denne enhed > Åbn filer...**<br>
  - Vælg mapper/filer ved hjælp af Apples native menu<br><br>

Alternativt kan du oprette forbindelse ved hjælp af **WebDAV** eller **DLNA**, hvis din NAS understøtter dem.
{{% /details %}}

{{% details title="Hvordan uploader og administrerer jeg musik i iCloud?" closed="true" %}}
– **Hvordan uploader jeg musik til iCloud?**  <br>
Gå til [https://www.icloud.com](https://www.icloud.com) i din browser, opret en mappe, og upload dine musikfiler direkte fra din Mac eller PC.<br>

– **Hvordan administrerer jeg iCloud-lager?**  <br>
Du har to muligheder:  <br>
1. Brug [https://www.icloud.com](https://www.icloud.com) i din browser til at organisere, uploade eller slette filer.<br>  
2. I appen, efter at have oprettet forbindelse til iCloud via **Forbindelser → Opret forbindelse til skylager → iCloud Drive**, kan du bruge den indbyggede filhåndtering til at uploade, downloade, omdøbe mapper eller slette filer direkte i dit iCloud-lager — uden at gemme dem på din enhed.<br>

⚠️ Vær forsigtig, når du sletter filer. Appen sletter dem permanent (de ryger ikke i papirkurven og kan ikke gendannes).<br>

Læs mere her: [Sådan streamer du musik fra iCloud Drive på din iPhone eller Mac](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="Hvordan kan jeg overføre mit 10 GB musikbibliotek fra Windows 11 til min iPhone til offline afspilning?" closed="true" %}}

Du har flere pålidelige muligheder for at flytte dit musikbibliotek fra din Windows 11-pc til din iPhone og bruge det offline i appen. Vælg den metode, der passer dig bedst:

1. **Med kabelforbindelse (anbefalet til store biblioteker)**  <br>
   Brug appen **Apple Devices** på Windows 11 til at overføre filer direkte til din iPhone via USB.  
   Følg Apples vejledning her:  
   https://support.apple.com/en-ph/120402 <br>

2. **Trådløst via Wi-Fi Drive**  <br>
   Aktivér funktionen **WiFi Drive** i appen og upload din musik via en browser på computeren.  
   Trin-for-trin vejledning her:  
   [Sådan overfører du musikfiler fra en computer til iPhone uden iTunes med WiFi-Drive](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **Trådløst med DLNA-server**  <br>
   Tænd DLNA-medieserveren på din Windows-computer, og stream eller overfør dit bibliotek direkte til appen.  
   Guide:  
   [Sådan aktiverer du DLNA-medieserver på Windows 10 og afspiller din musik på iPhone](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **Trådløst med SMB-fildeling**  <br>
   Aktivér **SMB-fildeling** på din pc, og opret forbindelse til den i appen for at gennemse, downloade eller overføre dine filer mappe for mappe.  
   Vejledning:  
   [Overfør filer fra computer til iPhone med SMB-protokollen](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ Ved overførsel af store biblioteker (10 GB+) er en kablet USB-overførsel normalt den hurtigste og mest stabile mulighed.

{{% /details %}}

</div>
