---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: 'Vanlige spørsmål'
description: 'Finn svar på vanlige spørsmål om Evermusic, Flacbox, Evervideo og Evertag. Utforsk funksjoner som skystreaming, filhåndtering, avspillingsalternativer, metadataredigering og mer.'
keywords: [
  "Evermusic FAQ", "Flacbox støtte", "Evervideo hjelp", "Evertag spørsmål",
  "slik bruker du Evermusic", "feilsøking av skymusikkspiller", "veiledning for frakoblet avspilling",
  "støtte for lydtaggeditor", "problemer med videostreaming", "opplæring i filoverføring"
]
tags: [
  "FAQ", "hjelp", "støtte", "evermusic", "flacbox", "evervideo", "evertag",
  "skyoppsett", "avspillingsproblemer", "filhåndtering", "metadataredigering",
  "feilsøking", "frakoblet modus", "musikkspiller", "videospiller"
]
aliases:
  - /blog/categories/how-to/
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## Lær å bruke appene våre

Leter du etter svar eller hjelp til å bruke en av appene våre? Du er på rett sted.

FAQ-sidene våre hjelper deg med å koble til skylagring, administrere musikk- og videofiler, sette opp frakoblet avspilling, justere equalizerinnstillinger, fikse metadata og mer.

Utforsk FAQ-en for appen din nedenfor for å komme i gang, eller bla gjennom vanlige spørsmål og svar vi har mottatt fra bruker-e-poster.

## Velg din app

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="Spill av 360°-videoer, stream fra iCloud, se med undertekster, bruk en videoequalizer, organiser innhold med spillelister og last ned videoer for frakoblet visning."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="Skymusikkspiller med frakoblet modus, lydequalizer, crossfade, gapless avspilling, spillelisteadministrasjon, fullt musikkbibliotek og innebygd filbehandler."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="Hi-res-lydspiller for iPhone og Mac. Lytt til lossless-formater som FLAC, ALAC, APE og DSD. Finjuster utdata med avanserte lydinnstillinger."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="Smart musikktaggeditor med batchredigering. Fiks manglende metadata, albumomslag og mer. Rediger ID3-, FLAC- og APE-tagger — over 120 felt støttes." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## Vanlige problemer og svar

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="Hvorfor kan jeg ikke logge inn på pCloud på en eldre iOS-versjon (15.8.4)?" closed="true" %}}
pClouds webinnloggingsside vises kanskje ikke riktig på eldre iOS-versjoner som 15.8.4, noe som hindrer deg i å angi e-post og passord i skjermbildet for skytilkobling.<br><br>

Som en løsning kan du bruke **WebDAV**-protokollen, som støttes av pCloud og fungerer pålitelig på alle iOS-versjoner.

**WebDAV-oppsett:**<br>
- **Amerikanske servere:** `https://webdav.pcloud.com`  
- **Europeiske servere:** `https://ewebdav.pcloud.com`  
- **Brukernavn:** Din pCloud-e-postadresse  
- **Passord:** Passordet til din pCloud-konto  

Åpne appen → Tilkoblinger → Koble til skylagring → Velg **WebDAV** → Skriv inn dine opplysninger og server-URL.

Denne metoden lar deg koble til pCloud-lagringen din og få tilgang til filene dine uten problemer på eldre enheter.
{{% /details %}}

{{% details title="Hvordan spille musikk på AirPlay fra Mac (macOS)?" closed="true" %}}
macOS-versjonen av appen inkluderer ikke innebygde AirPlay-, Chromecast- eller Bluetooth-tilkoblingsknapper slik som på iOS.<br><br>

Følg disse trinnene for å bruke **AirPlay** på MacBook Pro:

1. Gå til **øvre høyre hjørne** av skjermen og åpne **Kontrollsenter** (nær klokken).  
2. Klikk på **Lyd/Volum**-ikonet.  
3. Klikk på **AirPlay** på neste skjermbilde for å se en liste over alle tilgjengelige AirPlay-enheter.  
4. Velg ønsket enhet for å begynne å strømme musikken din.  

Dette vil rute all systemlyd (inkludert fra Evermusic eller Flacbox) til din valgte AirPlay-enhet.
{{% /details %}}

{{% details title="Hvorfor aktiveres ikke Premium-kjøpet mitt på Mac hvis jeg kjøpte det på iPhone?" closed="true" %}}
Livstidskjøp og abonnementer synkroniseres mellom iOS og Mac via **iCloud**.<br><br>

For å aktivere Premium på din Mac:<br>
- Sørg for at du har den nyeste appversjonen installert på begge enhetene<br>
- Aktiver **iCloud** på begge enhetene<br>
- Start appen på iOS-enheten din og vent 1 minutt til kjøpsinformasjon er lastet opp<br>
- Installer appen på din Mac fra App Store med samme **Apple ID**<br>
- Start appen og vent noen sekunder til informasjonen synkroniseres<br>
- Alternativt kan du trykke **Gjenopprett kjøp** i appens innstillinger på begge enhetene<br><br>

Premium-funksjonene dine skal da aktiveres på Mac automatisk.
{{% /details %}}

{{% details title="Hvordan kan jeg synkronisere spillelister automatisk mellom enheter?" closed="true" %}}
Det er for øyeblikket **ingen automatisk synkronisering** for spillelister.<br><br>

Du kan bruke ett av følgende alternativer:<br>
- **Sikkerhetskopier og gjenopprett** fra appinnstillinger [Slik overfører du musikkbiblioteket ditt mellom enheter i Evermusic: Trinn-for-trinn-guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **Eksporter spilleliste til M3U**, importer deretter på en annen enhet:<br>
  - [Eksporter spillelister](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [Importer spillelister](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **Arkiver spilleliste eller album** og overfør via ZIP:<br>
  - [Veiledning for spillelistearkiv](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="Er det trygt å bruke appene dine? Kan jeg deaktivere analyse?" closed="true" %}}
Ja, personvernet ditt er vår høyeste prioritet.<br><br>

- All data — musikfiler, innstillinger, skyinnlogginger — forblir på enheten din<br>
- Innloggingsopplysninger lagres sikkert i **iOS Keychain**<br>
- Vi samler bare inn anonyme krasj- og bruksrapporter<br>
- Du kan melde deg av i **Appinnstillinger → Analyse**<br><br>

Mer info:<br>
- [Personvernpolicy](/legal/privacy-policy/)<br>
- [Apple Keychain-sikkerhet](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

Hvis du bruker personaliserte annonser, krever Google Mobile Ads at samtykkeinnstillinger vises.<br>
Premium-brukere ser ingen annonser, og annonse-SDK-en er fullstendig deaktivert.
{{% /details %}}

{{% details title="Støtter appene dine Familiendeling?" closed="true" %}}
Ja, Familiendeling støttes.<br><br>

Slik deler du kjøp i app:<br>
- Sørg for at kjøpet er satt til å deles med familiegruppen din<br>
- Gå til **Innstillinger > Kjøp > Gjenopprett kjøp** på familiemedlemmets enhet<br>
- Dette vil be om kjøpsdata fra Apples servere og aktivere det på enheten deres
{{% /details %}}

{{% details title="Hvordan øke hastigheten på metadata og skysynkronisering?" closed="true" %}}
Aktiver bakgrunnsoppgaver for å forbedre synkroniseringshastigheten:<br><br>

- **Innstillinger → Musikkbibliotek → Metadataavlesning → Metadataavlesning i bakgrunnen**<br>
- **Innstillinger → Musikkbibliotek → Nettmusikksynk → Bakgrunnssynk**<br><br>

Øk også metadataavlesningshastigheten på macOS via **Innstillinger → Musikkbibliotek**.<br>
Hvis spilleren er aktiv (lyd spilles av), vil iOS ikke suspendere appen, noe som muliggjør kontinuerlig synkronisering.
{{% /details %}}

{{% details title="Hvordan kan jeg avbryte abonnementet mitt?" closed="true" %}}
Du kan avbryte abonnementet ditt fra Apples offisielle instruksjoner:<br>
👉 [Slik avbryter du et abonnement](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="Hvordan koble til og strømme lyd fra WD MyCloud EX2 Ultra?" closed="true" %}}

Når du legger til en tilkobling i appen via **Tilkoblinger > Koble til skylagring > My Cloud Home**, er den offisielt designet for å støtte **WD MyCloud Home**-enheter.<br>
WD MyCloud EX2 Ultra bruker begrenset tilgang for apper.<br><br>

Men hvis du har koblet deg til en **WD MyCloud EX2 Ultra**, **WD MyCloud Mirror** eller en annen **WD MyCloud**-lagringsmodell, kan du fremdeles bruke den med følgende løsning:<br><br>

1. Åpne **Tilkoblinger → Koble til skylagring → My Cloud Home**<br>
2. Opprett en mappe ved hjelp av innebygd filbehandler<br>
3. Last opp musikkfiler til denne mappen<br>
4. Disse lagres i en "sandkasse" som bare er tilgjengelig for appen<br>
5. Du kan nå strømme eller laste dem ned direkte<br><br>

⚠️ Bare mapper opprettet via appen vil være tilgjengelige fra NAS-en.
{{% /details %}}

{{% details title="Hvordan koble til Koofr.eu?" closed="true" %}}
Du kan koble til Koofr ved hjelp av **WebDAV**.<br><br>

- Koofr WebDAV-oppsettsveiledning: [koofr.eu blogg](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Evermusic/Flacbox WebDAV-veiledning: [Koble til NAS-lagring ved hjelp av WebDAV og lytte til musikk på iPhone eller Mac](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="Hva er app-URL-skjemaene?" closed="true" %}}
Her er de støttede skjemaene:<br><br>

**Evermusic**<br>
- iOS (blått ikon): `lsevermusic://`<br>
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

{{% details title="Musikk stopper å spille når appen er i bakgrunnen — hvordan fikse?" closed="true" %}}
Hvis appen krasjer eller pauser i bakgrunnen:<br>
- Gå til **Innstillinger > Musikkbibliotek > Nettmusikksynk > Bakgrunnssynk → Deaktiver**<br>
- **Innstillinger > Musikkbibliotek > Metadataavlesning > Metadataavlesning i bakgrunnen → Deaktiver**<br>
- **Innstillinger > Filbehandler > Bakgrunnsoverføringer → Deaktiver**
{{% /details %}}

{{% details title="Gapless avspilling fungerer ikke — hvordan fikse?" closed="true" %}}
Gapless avspilling avhenger av iOS-versjon og lyd-motor.<br>
Prøv å bytte lyd-motor:<br>
- Gå til **Innstillinger → Lydspleier → Generelt → Lydprosessor**<br>
- Velg **Core Audio** for bedre gapless-støtte
{{% /details %}}

{{% details title="Hvorfor viser appen bare 100 elementer i en liste?" closed="true" %}}
Appen bruker sidenummerering for ytelse.<br>
Slik deaktiverer du det:<br>
- Gå til **Innstillinger → Personalisering → Innholdslastegrense → Deaktivert**<br>
Nå lastes alle elementer inn på én gang.
{{% /details %}}

{{% details title="Hvorfor er det rare tegn i metadata?" closed="true" %}}
Prøv å aktivere metadatanormalisering:<br>
- **Innstillinger → Musikkbibliotek → Metadataavlesning → Normaliser metadatakoding**
{{% /details %}}

{{% details title="Hvorfor kan ikke appen lese mappenavn med spesialtegn?" closed="true" %}}
Dette er et kjent problem med **SMB2-protokollen**.<br><br>

Prøv følgende løsninger:<br>
- Aktiver **SMB1** på serveren din og i appinnstillinger<br>
- Bruk **systemfilvelgeren**:<br>
  - Gå til **Lokale filer > Filer på denne enheten > Åpne filer...**<br>
  - Velg mapper/filer ved hjelp av Apples opprinnelige meny<br><br>

Alternativt kan du koble til ved hjelp av **WebDAV** eller **DLNA** hvis NAS-en støtter dem.
{{% /details %}}

{{% details title="Hvordan laste opp og administrere musikk i iCloud?" closed="true" %}}
– **Hvordan laster jeg opp musikk til iCloud?**  <br>
Gå til [https://www.icloud.com](https://www.icloud.com) i nettleseren din, opprett en mappe og last opp musikfilene dine direkte fra Mac-en eller PC-en.<br>

– **Hvordan administrerer jeg iCloud-lagring?**  <br>
Du har to alternativer:  <br>
1. Bruk [https://www.icloud.com](https://www.icloud.com) i nettleseren din til å organisere, laste opp eller slette filer.<br>  
2. I appen, etter å ha koblet til iCloud via **Tilkoblinger → Koble til skylagring → iCloud Drive**, bruk den innebygde filbehandleren til å laste opp, laste ned, gi nytt navn til mapper eller slette filer direkte i iCloud-lagringen din — uten å lagre dem på enheten din.<br>

⚠️ Vær forsiktig når du sletter filer. Appen sletter dem permanent (de vil ikke gå til papirkurven og kan ikke gjenopprettes).<br>

Lær mer her: [Slik strømmer du musikk fra iCloud Drive på iPhone eller Mac](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="Hvordan overføre et 10 GB musikkbibliotek fra Windows 11 til iPhone for frakoblet avspilling?" closed="true" %}}

Du har flere pålitelige alternativer for å flytte musikkbiblioteket ditt fra Windows 11-PC-en til iPhone og bruke det frakoblet i appen. Velg metoden som passer best for deg:

1. **Bruke kabelforbindelse (anbefalt for store biblioteker)**  <br>
   Bruk **Apple Devices**-appen på Windows 11 til å overføre filer direkte til iPhone via USB.  
   Følg Apples veiledning her:  
   https://support.apple.com/en-ph/120402 <br>

2. **Trådløst via Wi-Fi Drive**  <br>
   Aktiver **WiFi Drive**-funksjonen i appen og last opp musikken din via en nettleser på datamaskinen.  
   Trinn-for-trinn-instruksjoner her:  
   [Slik overfører du musikkfiler fra en datamaskin til iPhone uten iTunes ved hjelp av WiFi-Drive](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **Trådløst ved hjelp av DLNA-server**  <br>
   Slå på DLNA-medieserveren på Windows-datamaskinen og strøm eller overfør biblioteket ditt direkte til appen.  
   Veiledning:  
   [Slik aktiverer du DLNA-medieserver på Windows 10 og spiller av musikk på iPhone](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **Trådløst ved hjelp av SMB-fildeling**  <br>
   Aktiver **SMB-fildeling** på PC-en og koble til den i appen for å bla, laste ned eller overføre filer mappe for mappe.  
   Instruksjoner:  
   [Overfør filer fra datamaskin til iPhone ved hjelp av SMB-protokollen](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ Når du overfører store biblioteker (10 GB+), er kablet USB-overføring vanligvis det raskeste og mest stabile alternativet.

{{% /details %}}

</div>
