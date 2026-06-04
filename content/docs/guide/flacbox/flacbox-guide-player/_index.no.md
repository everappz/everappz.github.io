---
title: "Lydspiller"
date: 2020-02-01
description: "Lær hvordan du bruker Flacbox-lydspilleren på iPhone, iPad og Mac. Kontroller avspilling, administrer køer, konfigurer FFmpeg / system-lydmotoren, endre samplingsfrekvens, tonehøydekorrigering, IO-bufferlengde, equalizer, lydbokmerkef, AirPlay 2, Google Cast, CarPlay, widgets og Mac-tastatursnarveier."
keywords: [
  "Flacbox spillerveiledning", "lydspillerinnstillinger", "Flacbox equalizer",
  "AirPlay musikkstrømming", "Google Cast musikk", "lydbokmerker",
  "Flacbox avspillingskø", "Flacbox gjenta stokk", "Flacbox volumkontroll",
  "macOS minispiller", "voiceover musikk-app",
  "Flacbox FFmpeg", "Flacbox tonehøydekorrigering", "Flacbox samplingsfrekvens",
  "Flacbox ekstern DAC", "Flacbox surroundlyd", "Flacbox IO-buffer",
  "Flacbox avspillingshastighet", "Flacbox sovtimer"
]
tags: ["guide", "flacbox", "spiller"]
readingTime: 14
---


Lydspilleren er appens hovedskjerm der du styrer musikk og de fleste avspillingsfunksjoner. Det er også her Flacbox' hi-res lydmotor — bygget på systemkodekene pluss det medfølgende **FFmpeg**-biblioteket — gjør det tunge arbeidet. La oss utforske hvordan du bruker den.

## Tilgang til Lydspilleren

Du kan komme til fullskjermspilleren fra minispillerlinjen. På iPhone sitter minispilleren nederst på hovedskjermen. På iPad og Mac er den på venstre side. For å skjule minispilleren på iPhone, trykk på den én gang og sveip ned. For å lukke fullskjermspilleren fullstendig, trykk på lukkeknappen i nedre høyre hjørne.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lydspiller Hovedskjerm" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Støttede Lydformater

Flacbox spiller de mest populære lydformatene — både Apples systemkodeker og mange tilleggsformater håndtert av den medfølgende FFmpeg-motoren:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Dette dekker praktisk talt alle moderne lossy- og losslessformater du sannsynligvis har i en personlig musikksamling.

## Avspillingskontroller

Nederst på spillerskjermen vil du se knapper for Spill av, Pause, Neste spor og Forrige spor. Det finnes også valgfrie knapper som Neste 30 sek og Forrige 30 sek som du kan aktivere i appinnstillingene (nyttig for lydbøker). Du kan spole fremover eller bakover ved å holde nede Neste / Forrige-knappene. For å hoppe til en bestemt del av et spor, dra avspillingsglidebryter.

## Gjenta og Stokk

Trykk på gjentagelsesknappen for å bla gjennom gjentagelsesmodi:

- **Gjenta alle** — looper alle spor i køen din.
- **Gjenta én** — gjentar bare det gjeldende sporet.
- **Gjenta stopp** — setter på pause når det gjeldende sporet slutter.
- **Ingen gjentakelse** — spiller av køen én gang uten å gjenta.

Bruk knappen **Stokk** for å tilfeldiggjøre rekkefølgen på spor i køen.

## Volumkontroll

Åpne lydinnstillingsskjermen ved å trykke på lydikonet under avspillingskontrollene for å få tilgang til volumglidebryteren. Du vil også finne knapper her for **Google Cast** og **AirPlay** slik at du raskt kan bytte avspilling til en annen enhet.

## Google Cast (Chromecast)

For Google Cast-brukere vises **Cast**-ikonet nederst på spilleren. Trykk på det for å velge en enhet og begynne strømming. Sørg for at enheten din og Google Cast-mottakeren er på samme Wi-Fi-nettverk. Merk: ikke alle lydformater er kompatible med Google Cast — noen hi-res-formater kan trenge å transkodes.

## AirPlay

For AirPlay, se etter **AirPlay**-knappen nederst på spilleren. Trykk på den og velg en enhet for strømming. Flacbox støtter **AirPlay 2**, slik at du kan spille til flere HomePods, Apple TVer eller AirPlay-2-kompatible høyttalere samtidig.

## Lyd-Equalizer

Flacbox inkluderer en **10-bands equalizer** med iPod-stil-forhåndsinnstillinger. Trykk på Equalizer i volumvisningen, og slå den på i øvre høyre hjørne. Du kan bruke forhåndsinnstillinger som Akustisk og Bassforsterker, eller justere hvert frekvensbånd med glidebryterne. Lag dine egne forhåndsinnstillinger, lagre dem under et hvilket som helst navn, og øk det totale volumet med preamplifikatoren. Vi har mer detaljerte instruksjoner om hvordan du bruker equalizeren [her](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lydspiller Equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Spillermodus Verktøylinje

For noen spillerstiler er det en dedikert verktøylinje øverst på fullskjermspilleren. Denne verktøylinjen inneholder tre nyttige knapper:

- **Søk** — finn raskt et bestemt spor i spillerkøen din.
- **Avspillingshastighetskontroll** — juster avspillingshastigheten fra 0,02× til 3,00×. Perfekt for lydbøker, podcaster og forelesninger. Trykk på Normal for å gå tilbake til standardhastigheten.
- **Lydbokmerker** — opprett flere bokmerker per spor. Vi har fullstendige instruksjoner om hvordan du bruker bokmerker [her](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Spillerkø

For å se spillerkøen din, trykk på køknappen på høyre side av gjeldende sang. Hver sang i køen har flere handlinger — trykk på tre prikker for å se dem. For å omorganisere en sang i køen, bruk omorganiserings-indikatoren nær tittelen og dra den til en ny posisjon.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Avspillingskø" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Kommentarer / Sangtekster

For å vise sporkommentarer og innebygde sangtekster, samt LRC-filer, følg disse trinnene:

1. Åpne **Innstillinger**.
2. Gå til **Lydspiller**.
3. Velg **Personalisering**.
4. Trykk på **Knapper på hovedskjermen**.
5. Aktiver **Kommentarer**.

Trykk deretter på spillerkø-knappen nederst på skjermen flere ganger for å bytte fra artwork / kø-visning til kommentarvisning. Rull til høyre på Kommentarer-skjermen for å bytte mellom **Kommentarer**, **Innebygde sangtekster** og **LRC-filen**. Fullstendige instruksjoner er tilgjengelige [her](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Sangtekster og Kommentarer Skjerm" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Alternativer-Meny

Hver sang i lydspillerkøen har en meny med flere handlinger, tilgjengelig ved å trykke på tre-prikker-knappen nær sangtittelen.

- **Spill neste** — legger sangen til toppen av spillerkøen.
- **Legg til spilleliste** — inkluderer sangen i en spilleliste, med mulighet til å opprette en ny.
- **Legg til favoritter** — merker sangen som en favoritt for rask tilgang.
- **Last ned** — lagrer sangen til lokale filer, vises i fanen **Lokale filer** og seksjonen **Frakoblet musikk**.
- **Rediger lydtagger** — åpner den innebygde lydtagg-editoren for å fikse manglende metadata, og endrer sangen på lagringen din.
- **Vis i mappe** — avslører mappen der lydfilen er lagret.
- **Vis i Finder** — for filer importert fra Mac-en din, avslører dette mappen der lydfilen befinner seg på Mac-en din.
- **Åpne i** — eksporterer lydfilen til en annen app.
- **Slett fra kø** — fjerner den valgte sangen fra lydspillerkøen.
- **Slett fra skytjeneste** — sletter sangen fra både musikkbiblioteket og skylagringen. **Denne handlingen er ugjenkallelig.**
- **Slett fra lokale filer** — sletter sangen fra både musikkbiblioteket og lokal lagring. **Denne handlingen er ugjenkallelig.**
- **Slett fra musikkbibliotek** — sletter sangen fra musikkbiblioteket ditt, mens filen beholdes i lagringen.

De samme alternativene er tilgjengelige for det nå-spillende elementet i lydspillerkøen, som du kan åpne ved å trykke på ikonet **Flere handlinger** nær sporsporertittelen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Alternativer for et Element i Avspillingskøen" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Ytterligere Spillerhandlinger

Trykk på **Flere handlinger**-knappen "..." på venstre side av den nå-spillende sangtittelen for å se ytterligere handlinger.

- **Fortsett avspilling** — gjenoppta fra der du slapp, inkludert kø og mediaposisjon. Særlig nyttig for lydbøker. Aktivert i appinnstillingene.
- **Søk** — finn raskt et bestemt spor i lydspillerkøen din.
- **Bokmerker** — se listen over opprettede lydbokmerker.
- **Kommentarer** — se sporkommentarer og innebygde sangtekster, samt LRC-filer. Fullstendige instruksjoner [her](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Hastighet** — juster avspillingshastigheten etter smak.
- **Nylige** — åpne en liste over nylig avspilte sanger.
- **Favoritter** — se samlingen din av favorittsanger.
- **Lyd-Equalizer** — aktiver lyd-equalizeren.
- **Sovtimer** — sett en timer for å stoppe avspilling etter et bestemt intervall. Flott for de øyeblikkene når du vil sovne til musikken din.
- **Lagre kø som spilleliste** — lagre den gjeldende lydspillerkøen som en ny spilleliste.
- **Slett kø** — tøm spillerkøen og stopp avspilling.
- **Innstillinger** — åpne lydspillerinnstillinger.
- **Hjelp** — finn hjelp og veiledning.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lydspiller Flere Handlinger Skjerm" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Lydbokmerker

Denne funksjonen lar deg opprette flere bokmerker for spor i musikkbiblioteket ditt — perfekt for lydbøker, forelesninger, lange DJ-mikser eller markering av refrenget til en favorittlåt.

For å opprette et nytt bokmerke:

- Begynn å spille den ønskede sangen.
- Åpne spillerskjermen.
- Trykk på **Bokmerker**-knappen på verktøylinjen for spillermodus.
- Velg **Legg til bokmerke**.
- Velg bokmerketiden og trykk på **Ferdig** i øvre høyre hjørne.

Redigering av bokmerker for gjeldende spor er enkelt: trykk på Rediger i øvre høyre hjørne for å gå inn i redigeringsmodus. I denne modusen kan du omorganisere bokmerker, slette dem, justere bokmerketid og endre bokmerketitler. Mer detaljerte instruksjoner om lydbokmerker er tilgjengelige [her](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lydbokmerker Skjerm" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Nylige og Favoritter

På spillerskjermen, trykk på tre prikker for å åpne Nylige og Favoritter. I begge seksjoner kan du søke etter sanger, spille alle, stokke alle, eksportere listen og slette listen. Vi har detaljerte instruksjoner om hvordan du eksporterer sanglistelister [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Koble iPhone til bilen via USB eller trådløs Apple CarPlay, og Flacbox vises på CarPlay-hjemskjermen din, klar til å spille musikk trygt under kjøring. CarPlay-grensesnittet inkluderer dedikerte faner for Bibliotek, Tilkoblinger, Lokale filer og Innstillinger, med avspillingskontroller, stokking, gjentagelse, køhåndtering og lyd-equalizeren tilgjengelig uten å plukke opp telefonen. Konfigurer CarPlay-opplevelsen videre i Innstillinger → CarPlay — sorteringsalternativer, paginering, fargegradienten for menyikoner, om bilder lastes inn og et alternativ for automatisk å sette avspillingen på pause når CarPlay kobler til.

[Les den fullstendige CarPlay-veiledningen](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox på Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Hjemskjerm-Widgets (iPhone & iPad)

Flacbox støtter iOS hjemskjerm- og låsskjerm-widgets slik at du kan se og kontrollere avspillingen med et blikk. Sørg for at Widgets er aktivert i Innstillinger → Widgets → Aktiver widgets, trykk deretter lenge på hjemskjermen eller låsskjermen, trykk på **+**, søk etter **Flacbox** og legg til en widget. Widgeten oppdateres under avspilling for å vise albumomslaget, tittelen og artisten for gjeldende spor.

## Minispillervindu (Mac Eksklusivt)

Mac-brukere kan bruke en kompakt alltid-på-toppen minispiller. Flytt markøren til nedre høyre kant av Flacbox-vinduet, endre størrelse ned til minste størrelse, og trykk på sammenleggingsknappen. Hold det øverst over hvert annet vindu ved å velge Vindu → Vis vindu alltid på toppen i menylinjen — perfekt for å holde musikkontrollene synlige mens du jobber i en annen app.

## Tastatursnarveier (Mac Eksklusivt)

For Mac-brukere er det tilgjengelig en systemavspillingsmeny i statuslinjen med tastatursnarveier. Trykk for eksempel mellomrom for Spill av / Pause. Snarveier for Stopp, Neste sang, Forrige sang, Hopp over tid, Gjenta, Stokk og Avspillingshastighet er også tilgjengelige.

## Lydspillerinnstillinger

For å åpne innstillinger, trykk på Mer-knappen på spillerskjermen og velg Innstillinger. Her finner du flere seksjoner, listet nedenfor.

### Generelt

Disse innstillingene dekker de grunnleggende aspektene av lydspilleren, inkludert avspillingskøen, lydutgang og lagring av spillerens tilstand.

- **Gjentagelsesmodus** — velg hvordan lydspilleren oppfører seg når et spor er ferdig:
  - **Gjenta alle** — spiller alle sporene i køen på nytt.
  - **Gjenta én** — gjentar bare det gjeldende sporet.
  - **Gjenta stopp** — setter avspillingen på pause når det gjeldende sporet slutter.
  - **Ingen gjentakelse** — lar køen spilles gjennom uten å gjenta.
- **Stokkemodus** — tilfeldiggjør rekkefølgen på spor i køen. Du kan slå det **Stokk av** eller **Stokk på**.
- **Lydkodek** — velg lydmotoren som brukes for avspilling:
  - **Systemkodek + FFmpeg** — prioriterer systemets lydkodek der det er mulig, og forbedrer kompatibilitet og stabilitet. Tonehøydekorrigering og justering av lydutgangs-samplingsfrekvens kan være begrenset i denne modusen.
  - **FFmpeg** — tvinger FFmpeg-kodeken for alle lydfiler, slik at du kan justere tonehøydekorrigering og lydutgangs-samplingsfrekvensen.
- **Lydutgangs-samplingsfrekvens** — juster lydutgangs-samplingsfrekvensen for å optimalisere lydkvaliteten, særlig nyttig med en ekstern DAC. Tilgjengelige verdier: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** og **96 kHz**.
- **Antall kanaler for lydutgang** — for flerkanalslyd-systemer med ekstern DAC, angi antall kanaler: **Mono, Stereo, Senter / Venstre / Høyre, Senter / Venstre / Høyre / Surround, ITU BS.775-1, 5.1 Surround** og **SDDS**.
- **Foretrukket IO-bufferlengde for lydutgang** — konfigurer inn- / ut-bufferlengden for lydavspilling. En typisk verdi for å minimere latens ved avspilling av høyoppløsningslyd er omtrent **5 millisekunder (0,005 sekunder)**. Akseptabel bufferstørrelse avhenger av maskinvare- og programvaremiljøet ditt, så test ulike lengder på målenheten din og velg den som best balanserer lav latens og feilfri avspilling.
- **Lydutgangsmodus (bare iOS)** — konfigurer blandet lydutgangsmodus slik at lyd fra Flacbox blandes med andre applikasjoner. Detaljerte instruksjoner er [her](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Lagre avspillingsposisjon** — sikrer at applikasjonen lagrer og gjenoppretter avspillingsposisjonen for sanger i musikkbiblioteket ditt.
- **Lagre lydspillertilstand** — bevarer lydspillerens tilstand før du lukker appen. For å fortsette avspillingen, trykk på **Fortsett avspilling** øverst i en hvilken som helst mappe, album, artist eller sjanger når du åpner appen igjen. Du kan også gjenopprette avspilling for individuelle filer ved å trykke på det spesifikke sporet.

Når du har aktivert både **Lagre avspillingsposisjon** og **Lagre lydspillertilstand**, åpne en mappe, album, artist eller sjanger og du vil se en **Fortsett avspilling**-knapp øverst på skjermen sammen med det sist lagrede sporet og posisjonen. Trykk på det for å fortsette nøyaktig der du slapp.

### Personalisering

Personalisering lar deg tilpasse utseendet på lydspillerskjermen, endre tilgjengelige kontroller på hovedskjermen, låsskjermen og statuslinjen, og konfigurere hoppetidskontroller.

- **Lydspiller-skjermstil** — konfigurer plasseringen av elementer på lydspillerskjermen.
- **Rullelstil for albumomslag** — konfigurer den foretrukne rullingesstilen for albumomslag.
- **Tilleggselementer** — aktiver ekstra elementer på lydspillerskjermen. **Lydformat-info** viser lydinfo for det nå-spillende sporet over kunstverket; **Lydvolum-glidebryter** viser lydutgangs-glidebryteren under avspillingskontrollene.
- **Handlinger på hovedskjermen** — konfigurer hvilke knapper som skal være synlige på lydspillerens hovedskjerm som standard: **Gjenta- og Stokkemodus, Neste og Forrige sang, Hoppetid, Sovtimer, Google Chromecast, AirPlay og Bluetooth, Lyd-Equalizer, Søk, Bokmerker, Hastighet, Legg til bokmerke, Legg til favoritter, Kommentarer** og mer.
- **Avspillingskontroller på låsskjermen** — velg hvilke kontroller som vises på låsskjermen. Mulige verdier: **Hoppetid, Legg til bokmerke, Legg til favoritter**.
- **Hoppetidsknapper** — velg tidsintervallet for **Hoppetid**-knappene.

### Fillasting

Under fillastingsprosessen kan du endre nettverkstypen som brukes til å laste inn sanger. Tilgjengelige alternativer: **Wi-Fi**, **Wi-Fi og mobildata**.

- **Forhåndsinnlastingstid** — sett bufringtidsintervallet. Øk dette hvis du har en dårlig nettverkstilkobling.
- **Bruk direkte URL** — når aktivert, brukes en direkte URL for å laste inn sangen hvis serveren støtter det. Dette kan øke sanglastingshastigheten, men kan påvirke avspillingsstabiliteten.

### Lyd-Equalizer

Tilpass lyd-equalizer-innstillingene. Du kan lese mer om å konfigurere lyd-equalizeren [her](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Avspillingshastighet

Juster avspillingshastigheten til lydspilleren fra **0,02× til 3,00×**. Trykk på konfigurasjonikonet i øvre høyre hjørne for å bytte til **presisjonsmodusen** for finere justeringer.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Avspillingshastighet Skjerm" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Tonehøydekorrigering

Endre tonehøydekorrigeringsinnstillinger ved å bruke de forhåndsdefinerte verdiene. Du kan også bytte mellom forhåndsdefinerte verdier og presisjonsmodusen ved å trykke på knappen i øvre høyre hjørne. Tonehøydekorrigering er tilgjengelig i FFmpeg-kodekbanen, med et område fra **-1000 til +1000**.

### Avspillingsbuffer

Sanger i lydspillerkøen lastes automatisk ned for å sikre jevn avspilling. Hvis du manuelt laster ned lydfiler, kan du deaktivere dette alternativet for å unngå duplikater. Du kan også konfigurere lydspillerens bufferstørrelse her.

### Sovtimer

Aktiver en timer for automatisk å stoppe avspillingen etter en bestemt periode — hendig når du vil sovne til musikk. Trykk på konfigurasjonikonet i øvre høyre hjørne for **presisjonsmodusen** med minutt-for-minutt granularitet.

## Tilgjengelighet

Flacbox er fullt tilgjengelig med **VoiceOver**. Hver komponent har en godt utformet etikett og beskrivelse. Når VoiceOver er aktiv, bytter appen til **Tekstmodus** slik at bare meningsfulle elementer vises — noe som forbedrer navigasjonshastigheten og tydeligheten. Du kan også aktivere Tekstmodus i **Innstillinger → Tilgjengelighet → Tekstmodus**.

### Justere Glidebryterne med VoiceOver

1. **Velg glidebryteren** — sveip venstre eller høyre til VoiceOver annonserer den.
2. **Juster verdien** — dobbelttrykk og hold glidebryteren, og dra deretter opp eller ned for å endre verdien raskt. VoiceOver kunngjør den nye verdien mens du går.

### Justere Sporposisjon i en Liste med VoiceOver

1. Trykk på omorganiserings-indikator-ikonet nær spornavnet for å gi det fokus.
2. Dobbelttrykk raskt på omorganiserings-indikatoren. På det andre trykket, ikke slipp fingeren — hold den til du hører en lyd som indikerer at cellen er klar til å bli flyttet.
3. Flytt cellen til den nye posisjonen.

Andre komponenter fungerer som forventet ved å bruke system-leverte VoiceOver-mønstre.
