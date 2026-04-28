---
title: "Eksporter din komplette lyttehistorikk fra Evermusic & Flacbox til Last.fm"
date: 2024-01-30
description: "Lær hvordan du eksporterer musikkhistorikken din fra Evermusic og Flacbox og laster den opp til Last.fm ved hjelp av CSV-filer og Last.fm Scrubbler-verktøyet for Windows."
keywords: ["evermusic", "flacbox", "lastfm", "musikkhistorikk", "scrobbling", "eksportere spor", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "nylige", "lastfm", "eksportere", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Sammendrag:** Eksporter lyttehistorikken din fra Evermusic eller Flacbox som en CSV-fil, og last den deretter opp til Last.fm ved hjelp av det gratis verktøyet Last.fm-Scrubbler-WPF på Windows. Automatisk scrobbling er også tilgjengelig innebygd i begge appene.

**Oppdatering:** Automatisk scrobbling er nå tilgjengelig! Les mer her: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling er en enkel måte å automatisk lagre grunnleggende detaljer som tittelen og artisten til sangen du spiller av til en nettbasert tjeneste. Senere kan du se gjennom lyttehistorikken din.

[Last.fm](https://www.last.fm/home), drevet av et musikkanbefalingssystem kalt Audioscrobbler, tilbyr denne tjenesten gratis. Den skaper en detaljert profil av din musikksmak ved å registrere sporene du lytter til, enten det er fra internettradiostasjoner, datamaskinen din eller forskjellige bærbare musikkenheter. Du kan besøke nettsiden senere for å motta anbefalinger om nye artister eller album som passer til din musikksmak.

Du kan laste opp lyttehistorikken din til [Last.fm](http://Last.fm) fra Evermusic- og Flacbox-appene ved hjelp av et gratis verktøy, og vi viser deg hvordan du gjør dette.

Åpne delen 'Musikkbibliotek' i applikasjonen og bla til delen 'Hurtigtilgang'. Trykk på menyelementet 'Nylige'.

![skjerm for musikkbibliotek](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

På skjermen 'Nylige' trykker du på 'Mer'-knappen i øvre høyre hjørne for å aktivere menyen 'Flere handlinger'. Trykk på menyelementet 'Eksporter sangliste'.

![skjerm for nylige](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

På skjermen 'Velg filformat' har du muligheten til å velge formatet på målfilen. Tilgjengelige alternativer - CSV, TXT, M3U.

![skjerm for valg av filformat](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Dette står for Comma-Separated Values, perfekt for å organisere dataene dine i et ryddig tabellformat. I målfilen finner du parametere som Artistnavn, Albumnavn, Spornavn, Tidsstempel (tiden du lyttet til sporene), Albumartistnavn og Sporvarighet.

TXT: Her snakker vi om en ren tekstfil. Den er enkel og grei, med parametere som inkluderer Artistnavn, Albumnavn, Spornavn og Varighet.

M3U: Dette formatet er i bunn og grunn førstevalget for å lage spillelister. Det er flott fordi du kan eksportere sanglisten din og nyte sporene dine på hvilken som helst enhet, selv om du ikke har originalfilene (forutsatt at du velger alternativet for absolutt URL for mediefiler). I utdatafilen finner du parametere som Varighet, Artistnavn, Spornavn og Mediefilplassering.

For vår oppgave er CSV det rette valget. Vi bruker denne filen med den gratis programvaren Last.fm-Scrubbler-WPF for å laste opp lyttehistorikken vår til [Last.fm](http://Last.fm)-tjenesten. Velg ganske enkelt CSV og trykk på 'Eksporter'-knappen.

![skjerm for fullført eksport](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Etter at eksporten er fullført, trykker du bare på 'Vis fil'-knappen, og appen vil vise den opprettede filen i dokumentmappen din. Trykk deretter på 'Flere handlinger'-knappen ved siden av filnavnet og velg 'Åpne i'-alternativet fra menyen. Neste steg er å kopiere den eksporterte filen til din stasjonære datamaskin. Du kan enkelt gjøre dette ved å velge AirDrop-alternativet fra 'Åpne i'-menyen.

![flere handlinger for eksportert fil](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Neste trinn er å bruke en gratis åpen kildekode [Last.FM](http://Last.FM)-klient som kun er tilgjengelig på Windows-plattformen. Denne klienten lar deg effektivt oppdatere lyttehistorikken din på [Last.FM](http://Last.FM) ved hjelp av CSV-filen vi nettopp eksporterte.

Hvis du ikke bruker en Windows-datamaskin for øyeblikket, ikke bekymre deg. Du kan fortsatt bruke denne klienten ved å installere VirtualBox på din Mac og bruke det offisielle Windows-utviklingsmiljøimaget.

Her er hva du må gjøre:

- Installer VirtualBox fra følgende lenke: [Last ned VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Last ned og installer Windows-utviklingsmiljøet fra denne lenken: [Windows-utviklingsmiljø](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

På din Windows-datamaskin (eller VirtualBox-app med Windows Development-image) last ned og installer [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - gratis åpen kildekode-programvare tilgjengelig på GitHub. Vi testet på versjon 1.28 som du kan laste ned her: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Nedlastingsside for Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Under 'Assets'-delen trykker du på [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) for å laste ned installasjonsarkivet. Pakk ut den nedlastede filen og åpne den utpakkede mappen.

- VIKTIG

Denne appen er fortsatt i beta. Appskaperne har ikke fått mye testing. De anbefaler å prøve å scrobble til en testkonto først og se om tingene du vil scrobble gjøres korrekt. Spesielt hvis du scrobbler mange spor på en gang. Vær forsiktig med kontoene dine.

Kjør Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

På hovedskjermen i applikasjonen trykker du bare på 'Ikke logget inn' nederst til venstre for å aktivere skjermen 'Legg til konto'.

![Skjerm for å legge til konto](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Skriv inn påloggingsinformasjonen din.

![skjerm for påloggingsinformasjon](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Trykk på 'Login'-knappen for å legge til kontoen din.

![Trykk på Login-knappen for å legge til kontoen din.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Åpne fanen 'File Parse Scrobbler' for å begynne å importere CSV-filen fra Evermusic-appen.

![Åpne fanen File Parse Scrobbler for å begynne å importere CSV-filen fra Evermusic-appen.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Velg 'Parser: CSV' og trykk på 'Settings'-knappen.

På neste skjerm kan du velge rekkefølgen på parameterne i CSV-filen din.

Individuelle felt kan omsluttes av anførselstegn og MÅ omsluttes av anførselstegn hvis feltet inneholder noen av de angitte skilletegnene. For eksempel:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Så la alle innstillinger stå som standard; det eneste du trenger å endre er å aktivere avkrysningsboksen i feltet 'Has Fields Enclosed In Quotes'.

Trykk 'Save & Close' for å bruke endringene.

![velg rekkefølgen på parameterne i CSV-filen din.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Filparse-scrobbling har to moduser. De kan endres med ComboBox-en 'Scrobbling Mode'.

Normal modus: I denne modusen vil sporene bli scrobblet med tidsstempelet fra den parsede scrobblen. Bare scrobbles nyere enn 14 dager kan scrobbles.

Importmodus: I denne modusen vil sporene bli scrobblet med tidsstempelet beregnet fra 'Finish Time' og den valgte varigheten mellom hvert spor. Dette gjør det mulig å scrobble sporene selv om tidsstempelet til den parsede scrobblen er eldre enn 14 dager. Derfor vil det første (øverste) sporet i CSV-filen bli scrobblet med 'Finish Time'.

Velg en tidligere generert CSV-fil fra Evermusic-appen i 'File:'-feltet og trykk 'Parse'. I noen tilfeller kan du se et feilvarsel som sier at noen scrobbles ikke kunne parses. Det er greit hvis du har noen spor uten fullstendig metadata som Artistnavn.

![noen scrobbles kunne ikke parses](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Trykk på 'Check All'-knappen for å velge alle parsede spor.

![Trykk på Check All-knappen for å velge alle parsede spor.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Trykk på 'Preview'-knappen for å sjekke alle endringer som vil bli sendt til serveren.

![Trykk på Preview-knappen for å sjekke alle endringer som vil bli sendt til serveren.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Trykk på 'Scrobble'-knappen for å laste opp alle endringer til serveren.

![Trykk på Scrobble-knappen for å laste opp alle endringer til serveren.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Tidligere hadde Last.fm-Scrubbler-WPF ingen daglig scrobblegrense. Dette har nå endret seg fordi noen brukte Scrubbler til å scrobble så mange spor at det forårsaket problemer for Last.fm-siden. Scrobblegrensen er for tiden 2800 scrobbles per dag. Når du prøver å scrobble mer enn det, vil du få en feilmelding. Det er planer om å legge til en 'scrobblekø', slik at hvis du trenger å scrobble mer enn 2800 spor, blir de lagt til i en kø og automatisk scrobblet etter en stund. Du kan sjekke hvor mange scrobbles du har igjen i brukervalgsvisningen.

Når alle poster er lastet opp til serveren, vil du se en melding nederst i appvinduet som bekrefter: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Nå kan du åpne profilen din på [Last.fm](http://Last.fm)-siden og sjekke alle endringene.

![profilen din på Last.fm-siden](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Ofte stilte spørsmål

{{% details title="Kan jeg scrobble automatisk uten å eksportere CSV-filer?" closed="true" %}}
Ja. Både Evermusic og Flacbox støtter nå automatisk Last.fm-scrobbling. Se veiledningen: [Hvordan scrobble til Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Hva om CSV-filen min har spor eldre enn 14 dager?" closed="true" %}}
Bruk Importmodus i Last.fm-Scrubbler-WPF. Den beregner tidsstempler på nytt fra Finish Time, slik at du kan scrobble spor uavhengig av den opprinnelige datoen.
{{% /details %}}

{{% details title="Jeg har ikke en Windows-datamaskin. Kan jeg fortsatt bruke Last.fm-Scrubbler?" closed="true" %}}
Ja. Installer VirtualBox på din Mac og last ned det gratis Windows-utviklingsmiljøimaget fra Microsoft. Kjør Last.fm-Scrubbler-WPF inne i den virtuelle maskinen.
{{% /details %}}

{{% details title="Hvorfor blir noen scrobbles ikke parset?" closed="true" %}}
Spor som mangler viktig metadata (som artistnavn) kan ikke parses. Dette er forventet og påvirker ikke andre spor i filen.
{{% /details %}}

{{% details title="Er det en daglig scrobblegrense?" closed="true" %}}
Ja. Last.fm-Scrubbler-WPF tillater opptil 2 800 scrobbles per dag. Hvis du trenger å scrobble mer, fordel prosessen over flere dager.
{{% /details %}}
