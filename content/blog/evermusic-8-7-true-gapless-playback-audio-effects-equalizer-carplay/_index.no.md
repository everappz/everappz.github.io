---
title: "Evermusic 8.7: ekte sømløs avspilling, lydeffekter, volumnormalisering, redesignet equalizer"
date: 2026-07-05
description: "Evermusic 8.7 for iPhone, iPad og Mac legger til ekte sømløs avspilling, fem studiolydeffekter (Reverb, Delay, Distortion, Compressor, Crossfeed), EBU R128 volumnormalisering, en redesignet 10-bånds equalizer med import/eksport av forhåndsinnstillinger, en gjenoppbygd AVAudioEngine-strømmemotor med støtte for FLAC og Ogg Vorbis, og raskere, mer nøyaktig CarPlay og Spilles nå."
keywords: ["Evermusic 8.7", "Evermusic-oppdatering", "ekte sømløs avspilling iPhone", "sømløs musikkspiller iOS", "sømløs avspilling CarPlay", "lydeffekter musikkspiller iPhone", "reverb delay distortion compressor crossfeed iOS", "crossfeed hodetelefoner iOS", "volumnormalisering iPhone", "lydstyrkenormalisering musikkspiller", "EBU R128 normalisering iOS", "replay gain-alternativ iPhone", "10-bånds equalizer iPhone", "grafisk equalizer iOS-app", "import eksport equalizer-forhåndsinnstillinger", "FLAC-spiller iPhone", "Ogg Vorbis-spiller iOS", "tapsfri musikkspiller iPhone 2026", "AVAudioEngine musikkspiller", "CarPlay musikkspiller iPhone", "Spilles nå låseskjerm nøyaktighet", "sky-musikkspiller iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Sømløs avspilling", "Lydeffekter", "Reverb", "Delay", "Distortion", "Compressor", "Crossfeed", "Volumnormalisering", "EBU R128", "Equalizer", "FLAC", "Ogg Vorbis", "CarPlay", "Spilles nå", "Liquid Glass", "Nyheter"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Kort oppsummert:** [Evermusic 8.7](/products/evermusic) er en lydkvalitetsutgivelse for iPhone, iPad og Mac. Den leverer **ekte sømløs avspilling** (ingen pauser, klikk eller tikk mellom spor), et fullstendig sett med **studiolydeffekter** — Reverb, Delay, Distortion, Compressor og Crossfeed — og **EBU R128 volumnormalisering** som holder lydstyrken konsistent fra sang til sang uten ReplayGain-tagger. **10-bånds equalizeren** er redesignet med nye glidebrytere, raskere bytte av forhåndsinnstillinger, egendefinerte forhåndsinnstillinger du kan importere og eksportere, og en bedre layout i liggende format og på iPad. Under panseret forbedrer en **gjenoppbygd AVAudioEngine-strømmemotor** påliteligheten og formatstøtten, inkludert **FLAC** og **Ogg Vorbis**. **CarPlay** og **Spilles nå** er raskere og mer nøyaktige på låseskjermen, i bilen og fra fjernkontroller på hodetelefoner.

---

## Hei alle sammen!

Evermusic 8.7 er tilgjengelig for nedlasting. Denne oppdateringen handler helt om hvordan musikken din *høres ut*. Vi bygde om avspillingsmotoren for ekte sømløs avspilling, la til en suite med studiokvalitets lydeffekter, introduserte lydstyrkenormalisering, og redesignet equalizeren fra glidebryterne og opp. Alt er pakket inn i Apples nye **Liquid Glass**-design.

[Last ned Evermusic 8.7 fra App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) eller oppdater fra din eksisterende versjon. Evermusic er en gratis nedlasting med valgfrie oppgraderinger i appen.

## Ekte sømløs avspilling

Sømløs avspilling betyr at stillheten mellom to spor er borte. Ingen pause, ingen klikk, ingen tikk — den nåværende sangen flyter rett over i den neste. Det betyr mest for musikken som ble designet for å høres som en helhet: **liveopptak, DJ-mikser, klassiske verk og konseptalbum** der ett spor fader direkte inn i et annet.

Her er hva som endret seg teknisk. Evermusics lydmotor holder to spor i spill samtidig: det du hører og det neste i køen. Mens det nåværende sporet spilles, blir det neste sporet allerede **hentet, dekodet og forhåndsbufret** i bakgrunnen. Når det nåværende sporet når slutten, overleverer motoren til det neste sporet **inne i spilleren, ikke inne i lydstrømmen**. Utgangsrenderløkken fortsetter å hente lydsampler fra en kontinuerlig ringbuffer uten noen gang å stoppe, så lytteren hører aldri en grense. Byttet skjer mellom sampler, og det er nettopp derfor det ikke er noe hørbart mellomrom.

Dette fungerer likt enten filen er på enheten din, i skyen eller på en medieserver — forhåndsbufringen begynner bare litt tidligere for eksterne kilder.

## Studiolydeffekter

Evermusic 8.7 legger til fem sanntids lydeffekter du kan stable oppå musikken din. Hver enkelt kjører som en native lydprosesseringsnode i avspillingsmotoren, så den brukes på alt du spiller — lokale filer, skystrømmer og internettradio likt — uten omkoding.

Hver effekt leveres med et **kuratert bibliotek av forhåndsinnstillinger** for å gi deg en flott lyd med ett trykk, og Evermusic **husker de eksakte innstillingene dine** mellom øktene. Juster en kontroll, og effekten bytter til en **Manuell** tilstand, så du alltid vet når du har beveget deg bort fra en forhåndsinnstilling.

### Reverb

Legger til en følelse av rom, fra et stramt rom til en katedral. Bygget på Apples `AVAudioUnitReverb` tilbyr den **13 rom-forhåndsinnstillinger** (Lite rom, Middels sal, Plate, Katedral og flere) pluss en **wet/dry-miks**-kontroll fra 0 til 100 % slik at du bestemmer hvor mye rom du vil legge til.

### Delay (Ekko)

Et klassisk ekko med **10 forhåndsinnstillinger** — Slapback, Tape-ekko, Dub, Ambient og andre. Du kan stille inn **delay-tiden** (opptil 2 sekunder), **feedback** (hvor mange gjentakelser), en **lavpass-cutoff** for å varme opp gjentakelsene, og **wet/dry-miksen**.

### Distortion

Fra subtil grus til full lo-fi-ødeleggelse, drevet av `AVAudioUnitDistortion` med **22 karakter-forhåndsinnstillinger** (Bit Brush, Cellphone Concert, Radio Tower og flere), en **pre-gain**-drivkontroll, og en wet/dry-miks slik at du kan blande effekten tilbake inn i det rene signalet.

### Compressor

En dynamikkprosessor (Apples `AUDynamicsProcessor`) som jevner ut høye og stille passasjer. Den eksponerer det fulle profesjonelle kontrollsettet — **terskel, forhold/headroom, attack, release, ekspansjon og makeup-gain** — med **10 forhåndsinnstillinger** tilpasset virkelige situasjoner: Tale / Podkast, Sen kveld, Filmdialog, Strømmematch og Maksimal lydstyrke blant dem.

### Crossfeed

Crossfeed får hodetelefonlytting til å høres mer naturlig ut ved å blande litt av venstre kanal inn i høyre og omvendt, slik ørene dine hører ekte høyttalere. Den er bygget på den velkjente **Bauer stereophonic-to-binaural (bs2b)**-algoritmen, med kontroll over **crossfeed-nivået** og **cutoff-frekvensen**, og **6 forhåndsinnstillinger** inkludert de audiofil-favoritte innstillingene *Chu Moy* og *Jan Meier*. Den er spesielt god på eldre, hardt panorerte stereomikser fra 1960- og 1970-tallet.

## Volumnormalisering

Har du noen gang laget en spilleliste der ett spor braker og det neste er en hvisken? Volumnormalisering fikser det. Evermusic 8.7 bruker **EBU R128-lydstyrkemåling** (den samme ITU-R BS.1770-standarden som brukes i kringkasting og av strømmetjenester) for å måle hvert spors faktiske opplevde lydstyrke og forsiktig styre den mot et konsistent mål.

I motsetning til ReplayGain krever den **ingen** tagger i filene dine, og den endrer **ikke** lyden din. Den fungerer i sanntid på alt du spiller, inkludert skystrømmer og direkteradio, og den nullstilles rent når du søker eller bytter spor.

Fire forhåndsinnstillinger dekker de vanlige tilfellene:

- **Lett** — mild jevning (mål −20 LUFS).
- **Standard** — standarden, strømmestil-lydstyrke (mål −16 LUFS, opptil +12 dB løft for stille spor).
- **Sterk** — aggressiv tilpasning for svært blandede biblioteker (mål −14 LUFS).
- **Natt** — stillere og konsistent for kveldslytting på lavt volum (mål −23 LUFS).

Du trenger ikke lenger å strekke deg etter volumet mellom sanger.

## Redesignet equalizer

Evermusics **10-bånds grafiske equalizer** fikk en full redesign. Båndene dekker **32 Hz til 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), hvert justerbart fra **−12 dB til +12 dB** i fine trinn på 0,1 dB, med en **forforsterker** fra −24 dB til +24 dB for å hindre klipping når du booster.

Hva er nytt i 8.7:

- **Nye glidebrytere** — presise, responsive kontroller som tar i bruk utseendet til den native iOS 26-systemglidebryteren og **Liquid Glass**-materialet.
- **Raskere, smidigere bytte av forhåndsinnstillinger** — hopp mellom forhåndsinnstillinger umiddelbart, med en redesignet horisontal forhåndsinnstillingslinje i stående format og en vertikal forhåndsinnstillingskolonne i liggende format.
- **Bedre layout i liggende format og på iPad** — glidebryterne og forhåndsinnstillingsvelgeren omorganiseres for å bruke den ekstra bredden i stedet for å presses sammen i en telefonstor kolonne.
- **Egendefinerte forhåndsinnstillinger** — lag og lagre dine egne kurver, endre rekkefølgen, og **importer og eksporter** forhåndsinnstillinger som `.eqp`-filer for å flytte dem mellom enheter eller dele dem.

Equalizeren kjører native i motoren (`AVAudioUnitEQ`), så den brukes på hver kilde, og den fungerer også over AirPlay, Chromecast og CarPlay der det støttes.

## Gjenoppbygd avspillingsmotor

Under panseret kjører Evermusic 8.7 på en **gjenoppbygd strømmemotor** bygget på Apples `AVAudioEngine` med en tilpasset render-pipeline. Dette er det som gjør den sømløse overleveringen, effektkjeden og equalizeren mulig, og det gjør også hverdagsavspilling mer pålitelig.

- **Forbedret formatstøtte** — inkludert **FLAC** (via Core Audio) og **Ogg Vorbis** (via `libvorbisfile`), sammen med MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF og mer.
- **Smartere bufring** — en adaptiv forhåndsbuffer skalerer med tilkoblingen din, med en kontinuerlig ringbuffer som mater utgangen slik at korte nettverksforstyrrelser ikke blir til avbrudd.
- **Automatisk gjenoppretting** — en rebufringstilstandsmaskin og gjentakelseslogikk med backoff gjenopptar avspilling rent etter et øyeblikk med svakt signal i stedet for å stoppe sporet.
- **Færre avbrudd** — den samme motoren driver lokale filer, skystrømmer, medieservere og internettradio, så oppførselen er konsistent overalt.

## Spilles nå og CarPlay

Skjermene du faktisk ser på mens du lytter — **låseskjermen**, **CarPlay** og fjernkontrollknappene på bilen eller hodetelefonene dine — er mer nøyaktige og raskere i 8.7.

- **Mer nøyaktig Spilles nå-info.** Evermusic fanger spillerens tilstand under en lås før den publiseres, slik at tittelen, forløpt tid, varighet og spill/pause-tilstand aldri kan være uenige med hverandre på låseskjermen eller i bilen. Bufring- og lastetilstander rapporteres nå korrekt i stedet for å vise «spiller» mens et spor fortsatt hentes.
- **Pålitelige fjernkontroller.** Spill, pause, neste, forrige, søk, hopp over, shuffle, gjenta og avspillingshastighet reagerer alle konsistent fra hodetelefonknapper, bilkontroller og låseskjermen, drevet av `MPRemoteCommandCenter`.
- **Raskere CarPlay-omslag.** Albumomslag lastes nå flere ganger raskere i lange lister (batch-tempo kuttet fra 1,0s til 0,25s, med den første synlige skjermen som lastes umiddelbart), og de vises nå i de kompakte iOS 26 CarPlay-listeradene som tidligere ikke viste omslag.
- **CarPlay-sortering og stabilitetsfikser.** Raskere sortering på store biblioteker og herding mot krasj i grensetilfeller ved rulling gjennom lange lister.
- **Struperegulerte metadataoppdateringer.** Spilles nå- og fjernkommandooppdateringer er struperegulert slik at raske endringer ikke lenger oversvømmer systemet, noe som holder låseskjerm- og CarPlay-kontrollene responsive.

## Andre forbedringer

- **Liquid Glass-designforbedringer** i hele appen — gjennomskinnelige overflater, smidigere animasjoner og forfinede kontroller på iOS, iPadOS og macOS.
- **Nye startskjermwidgeter** med forbedret oppdateringslogikk som holder dem synkronisert uten å tappe ekstra batteri.
- Fikser for nylige iOS-utgivelser.
- Lokaliseringsfikser på tvers av flere språk.
- Mange mindre forbedringer basert på e-postene og App Store-anmeldelsene dine.

## Hvorfor denne oppdateringen betyr noe

Evermusic 8.7 er bygget rundt én idé: **musikken din bør høres best mulig ut, på enhver kilde.**

1. **Hele album, slik det var ment.** Ekte sømløs avspilling betyr at livesett, DJ-mikser og konseptalbum endelig spilles slik artisten mastret dem.
2. **Et studio i lomma di.** Reverb, Delay, Distortion, Compressor, Crossfeed, en redesignet equalizer og lydstyrkenormalisering gir deg reell kontroll over lyden din, ikke bare en på/av-bryter.
3. **Den samme opplevelsen overalt.** Lokale filer, skystasjoner, medieservere og internettradio kjører alle gjennom den samme gjenoppbygde motoren, med nøyaktig Spilles nå og en raskere CarPlay på toppen.

## Skaff deg Evermusic 8.7

[**Last ned Evermusic fra App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) eller oppdater fra inne i App Store. Evermusic er en gratis nedlasting med valgfrie oppgraderinger i appen for avanserte funksjoner.

Hvis du liker appen, vennligst legg igjen en vurdering på App Store — det hjelper virkelig. Har du tilbakemeldinger eller støter på et problem? Send oss en e-post på **support@everappz.com**. Vi leser hver melding.

## Ofte stilte spørsmål

{{% details title="Hva er nytt i Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 legger til ekte sømløs avspilling, fem studiolydeffekter (Reverb, Delay, Distortion, Compressor og Crossfeed), EBU R128 volumnormalisering, en redesignet 10-bånds equalizer med egendefinerte forhåndsinnstillinger og import/eksport, en gjenoppbygd AVAudioEngine-strømmemotor med forbedret formatstøtte (inkludert FLAC og Ogg Vorbis), raskere og mer nøyaktig CarPlay og Spilles nå, Liquid Glass-designoppdateringer, oppfriskede startskjermwidgeter, og feil- og lokaliseringsfikser.
{{% /details %}}

{{% details title="Har Evermusic ekte sømløs avspilling?" closed="true" %}}
Ja. Fra og med Evermusic 8.7 er avspillingen ekte sømløs: det er ingen pause, klikk eller tikk mellom spor. Motoren forhåndsbufrer og dekoder neste spor mens det nåværende spilles og overleverer mellom lydsampler på en kontinuerlig ringbuffer, slik at overgangen er uhørbar. Den fungerer for lokale filer, skystrømmer og medieservere, og den er ideell for livealbum, DJ-mikser og konseptalbum.
{{% /details %}}

{{% details title="Hvilke lydeffekter inkluderer Evermusic 8.7?" closed="true" %}}
Fem sanntidseffekter: **Reverb** (13 rom-forhåndsinnstillinger, wet/dry-miks), **Delay/Ekko** (10 forhåndsinnstillinger med delay-tid, feedback, lavpass og miks), **Distortion** (22 karakter-forhåndsinnstillinger med pre-gain og miks), **Compressor** (en fullverdig dynamikkprosessor med terskel, forhold, attack, release, ekspansjon og makeup-gain, pluss 10 forhåndsinnstillinger), og **Crossfeed** (Bauer bs2b hodetelefon-crossfeed med nivå- og cutoff-kontroller og 6 forhåndsinnstillinger). Hver effekt leveres med kuraterte forhåndsinnstillinger, og de egendefinerte innstillingene dine huskes mellom øktene.
{{% /details %}}

{{% details title="Hva er Crossfeed og hvorfor skulle jeg bruke den?" closed="true" %}}
Crossfeed blander en liten, filtrert mengde av hver stereokanal inn i den andre, slik ørene dine naturlig hører ekte høyttalere i et rom. På hodetelefoner reduserer dette den overdrevne «inne-i-hodet»-separasjonen av hardt panorerte opptak og gjør lang lytting mer behagelig. Evermusic bruker den velkjente Bauer stereophonic-to-binaural (bs2b)-algoritmen og inkluderer forhåndsinnstillinger som Chu Moy og Jan Meier. Den er spesielt effektiv på eldre stereomikser fra 1960- og 1970-tallet.
{{% /details %}}

{{% details title="Hvordan fungerer volumnormalisering i Evermusic?" closed="true" %}}
Evermusic 8.7 måler hvert spors opplevde lydstyrke ved hjelp av EBU R128-standarden (ITU-R BS.1770) i sanntid og justerer forsiktig nivået mot et konsistent mål slik at spor ikke hopper i volum. Den krever ingen ReplayGain-tagger og endrer ikke filene dine. Fire forhåndsinnstillinger er tilgjengelige — Lett (−20 LUFS), Standard (−16 LUFS), Sterk (−14 LUFS) og Natt (−23 LUFS) — og normaliseringen nullstilles rent når du søker eller bytter spor.
{{% /details %}}

{{% details title="Er Evermusics volumnormalisering det samme som ReplayGain?" closed="true" %}}
Den oppnår det samme målet — konsistent lydstyrke mellom spor — men fungerer annerledes. ReplayGain er avhengig av lydstyrke-tagger lagret inne i filene dine. Evermusics normalisator måler lydstyrke direkte med EBU R128, så den fungerer på enhver kilde, inkludert skystrømmer og internettradio, selv når filene ikke har noen tagger i det hele tatt.
{{% /details %}}

{{% details title="Hvor mange bånd har Evermusic-equalizeren, og kan jeg lage mine egne forhåndsinnstillinger?" closed="true" %}}
Evermusic-equalizeren er en 10-bånds grafisk equalizer som dekker 32 Hz til 16 kHz, med hvert bånd justerbart fra −12 dB til +12 dB i trinn på 0,1 dB og en forforsterker fra −24 dB til +24 dB. Den inkluderer innebygde forhåndsinnstillinger, lar deg lage og lagre egendefinerte forhåndsinnstillinger, og støtter import og eksport av forhåndsinnstillinger som .eqp-filer slik at du kan flytte eller dele dem mellom enheter.
{{% /details %}}

{{% details title="Hva endret seg i Evermusic 8.7-equalizeren?" closed="true" %}}
Equalizeren ble redesignet med nye, mer presise glidebrytere som tar i bruk iOS 26-systemglidebryteren og Liquid Glass-utseendet, raskere og smidigere bytte av forhåndsinnstillinger, og en bedre layout i liggende format og på iPad (en horisontal forhåndsinnstillingslinje i stående format og en vertikal forhåndsinnstillingskolonne i liggende format). Egendefinerte forhåndsinnstillinger og .eqp import/eksport støttes.
{{% /details %}}

{{% details title="Støtter Evermusic 8.7 FLAC og Ogg Vorbis?" closed="true" %}}
Ja. Den gjenoppbygde motoren spiller FLAC (via Core Audio) og Ogg Vorbis (via libvorbisfile), sammen med MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF og mer, fra lokale filer, skystasjoner og medieservere.
{{% /details %}}

{{% details title="Hva ble forbedret i CarPlay og på låseskjermen?" closed="true" %}}
CarPlay-albumomslag lastes flere ganger raskere i lange lister og vises nå i de kompakte iOS 26-listeradene som tidligere ikke viste noen. Spilles nå-informasjon på låseskjermen og i CarPlay er mer nøyaktig — tittelen, forløpt tid, varighet og spill/pause-tilstand fanges sammen slik at de ikke kan være uenige, og bufringstilstander rapporteres korrekt. Fjernkontroller (spill, pause, neste, forrige, søk, shuffle, gjenta, hastighet) reagerer pålitelig fra hodetelefoner og bilen, og CarPlay-sortering på store biblioteker er raskere.
{{% /details %}}

{{% details title="Fungerer lydeffektene og equalizeren med skystrømming og CarPlay?" closed="true" %}}
Ja. Effektene, equalizeren og volumnormaliseringen kjører native inne i avspillingsmotoren, så de brukes på alt Evermusic spiller — lokale filer, skystasjoner, medieservere og internettradio — og de fortsetter å fungere under CarPlay-avspilling og, der det støttes, over AirPlay og Chromecast.
{{% /details %}}

{{% details title="Er Evermusic 8.7 gratis å oppdatere, og hvilke enheter støtter den?" closed="true" %}}
Ja. Evermusic er en gratis nedlasting fra App Store, og 8.7 er en gratis oppdatering for eksisterende brukere, med valgfrie oppgraderinger i appen for avanserte funksjoner. Den kjører på iPhone, iPad og Mac. CarPlay krever et CarPlay-kompatibelt kjøretøy eller hodeenhet.
{{% /details %}}
