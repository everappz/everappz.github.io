---
title: "Eksportér din komplette lyttehistorik fra Evermusic og Flacbox til Last.fm"
date: 2024-01-30
description: "Lær hvordan du eksporterer din musikhistorik fra Evermusic og Flacbox og uploader den til Last.fm ved hjælp af CSV-filer og Last.fm Scrubbler-værktøjet til Windows."
keywords: ["evermusic", "flacbox", "lastfm", "musikhistorik", "scrobbling", "eksporter numre", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "seneste", "lastfm", "eksport", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Resumé:** Eksportér din lyttehistorik fra Evermusic eller Flacbox som en CSV-fil, og upload den derefter til Last.fm ved hjælp af det gratis Last.fm-Scrubbler-WPF-værktøj på Windows. Automatisk scrobbling er også tilgængelig direkte i begge apps.

**Opdatering:** Automatisk scrobbling er nu tilgængelig! Læs mere her: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling er en enkel måde at automatisk gemme grundlæggende detaljer som titel og kunstner for den sang, du lytter til, i en onlinetjeneste. Senere kan du gennemgå din lyttehistorik.

[Last.fm](https://www.last.fm/home), drevet af et musikanbefalingssystem kaldet Audioscrobbler, tilbyder denne tjeneste gratis. Det opretter en detaljeret profil af din musikalske smag ved at registrere de numre, du lytter til, uanset om det er fra internetradiostationer, din computer eller forskellige bærbare musikenheder. Du kan besøge hjemmesiden senere for at modtage anbefalinger til nye kunstnere eller albums, der matcher din musiksmag.

Du kan uploade din lyttehistorik til [Last.fm](http://Last.fm) fra Evermusic og Flacbox apps ved hjælp af et gratis værktøj, og vi guider dig igennem processen.

Åbn sektionen 'Musikbibliotek' i applikationen og rul ned til sektionen 'Hurtig adgang'. Tryk på menupunktet 'Seneste'.

![musikbiblioteksskærm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

På skærmen 'Seneste' tryk på knappen 'Mere' i øverste højre hjørne for at aktivere menuen 'Flere handlinger'. Tryk på menupunktet 'Eksportér sangliste'.

![seneste skærm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

På skærmen 'Vælg filformat' har du mulighed for at vælge formatet på destinationsfilen. Tilgængelige muligheder - CSV, TXT, M3U.

![vælg filformat skærm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Dette står for kommaseparerede værdier, perfekt til at organisere dine data i et pænt tabelformat. I destinationsfilen finder du parametre som Kunstnernavn, Albumnavn, Numernavn, Tidsstempel (tidspunktet du lyttede til numrene), Albumkunstnernavn og Numervarighed.

TXT: Her taler vi om en ren tekstfil. Den er enkel og ligetil, med parametre som Kunstnernavn, Albumnavn, Numernavn og Varighed.

M3U: Dette format er i bund og grund standarden for at oprette playlister. Det er fantastisk, fordi du kan eksportere din sangliste og nyde dine numre på enhver enhed, selv hvis du ikke har de originale filer (forudsat at du vælger den absolutte URL for mediefiler mulighed). I outputfilen finder du parametre som Varighed, Kunstnernavn, Numernavn og Mediefilplacering.

Til vores opgave er valget af CSV den rette vej. Vi bruger denne fil med det gratis software Last.fm-Scrubbler-WPF til at uploade vores lyttehistorik til [Last.fm](http://Last.fm)-tjenesten. Vælg blot CSV og tryk på knappen 'Eksportér'.

![eksport fuldført skærm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Når eksporten er fuldført, skal du blot trykke på knappen 'Vis fil', og appen viser den oprettede fil i din dokumentmappe. Tryk derefter på knappen 'Flere handlinger' ved siden af filnavnet og vælg muligheden 'Åbn i' fra menuen. Vores næste skridt er at kopiere den eksporterede fil til din stationære computer. Du kan nemt gøre dette ved at vælge AirDrop-muligheden fra menuen 'Åbn i'.

![flere handlinger for eksporteret fil](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Dernæst bruger vi en gratis open-source [Last.FM](http://Last.FM)-klient, som kun er tilgængelig på Windows-platformen. Denne klient giver dig mulighed for effektivt at opdatere din lyttehistorik på [Last.FM](http://Last.FM) ved hjælp af den CSV-fil, vi netop har eksporteret.

Hvis du ikke bruger en Windows-computer i øjeblikket, skal du ikke bekymre dig. Du kan stadig få adgang til denne klient ved at installere VirtualBox på din Mac og bruge den officielle Windows-udviklingsmiljø-billedfil.

Her er hvad du skal gøre:

- Installér VirtualBox fra følgende link: [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Download og installér Windows-udviklingsmiljøet fra dette link: [Windows-udviklingsmiljø](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

På din Windows-computer (eller VirtualBox-app med Windows Development-billede) download og installér [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - gratis open-source software tilgængelig på GitHub. Vi testede version 1.28, som du kan downloade her: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Last.fm-Scrubbler-WPF downloadside](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Under sektionen 'Assets' tryk på [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) for at downloade installationsarkivet. Pak den downloadede fil ud og åbn den udpakkede mappe.

- VIGTIGT

Denne app er stadig i beta. Appens skabere har ikke foretaget meget testning. De anbefaler at prøve at scrobble til en testkonto først og se, om de ting, du vil scrobble, gør det korrekt. Især hvis du scrobbler mange numre på én gang. Vær venligst forsigtig med dine konti.

Kør Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

På applikationens hovedskærm skal du blot trykke på 'Ikke logget ind', placeret i nederste venstre hjørne, for at aktivere skærmen 'Tilføj konto'.

![tilføj konto skærm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Indtast dine loginoplysninger.

![indtast loginoplysninger skærm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Tryk på knappen 'Log ind' for at tilføje din konto.

![Tryk på knappen Log ind for at tilføje din konto.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Åbn fanen 'File Parse Scrobbler' for at begynde at importere CSV-filen fra Evermusic-appen.

![Åbn fanen File Parse Scrobbler for at begynde at importere CSV-filen fra Evermusic-appen.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Vælg 'Parser: CSV' og tryk på knappen 'Indstillinger'.

På den næste skærm kan du vælge rækkefølgen af parametrene i din CSV-fil.

Individuelle felter kan være omsluttet af anførselstegn og SKAL være omsluttet af anførselstegn, hvis feltet indeholder nogen af de indstillede separatorer. For eksempel:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Så lad alle indstillinger stå som standard, det eneste du skal ændre er at aktivere afkrydsningsfeltet i feltet 'Has Fields Enclosed In Quotes'.

Tryk på 'Gem og luk' for at anvende ændringerne.

![vælg rækkefølgen af parametrene i din CSV-fil.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Filanalyse-scrobbling har to tilstande. De kan ændres med 'Scrobbling Mode' rullemenuen.

Normal tilstand: I denne tilstand scrobbles numrene med tidsstemplet fra den analyserede scrobble. Kun scrobbles nyere end 14 dage kan scrobbles.

Importtilstand: I denne tilstand scrobbles numrene med tidsstemplet beregnet fra 'Sluttidspunkt' og den valgte varighed mellem hvert nummer. Dette gør det muligt at scrobble numrene, selvom tidsstemplet for den analyserede scrobble er ældre end 14 dage. Derfor vil det første (øverste) nummer i CSV-filen blive scrobblet med 'Sluttidspunkt'.

Vælg en tidligere genereret CSV-fil fra Evermusic-appen i feltet 'File:' og tryk på 'Parse'. I nogle tilfælde kan du se en fejlbesked om, at nogle scrobbles ikke kunne analyseres. Det er okay, hvis du har nogle numre uden komplet metadata som Kunstnernavn.

![nogle scrobbles kunne ikke analyseres](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Tryk på knappen 'Markér alle' for at vælge alle analyserede numre.

![Tryk på knappen Markér alle for at vælge alle analyserede numre.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Tryk på knappen 'Forhåndsvisning' for at kontrollere alle ændringer, der vil blive sendt til serveren.

![Tryk på knappen Forhåndsvisning for at kontrollere alle ændringer, der vil blive sendt til serveren.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Tryk på knappen 'Scrobble' for at uploade alle ændringer til serveren.

![Tryk på knappen Scrobble for at uploade alle ændringer til serveren.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Tidligere havde Last.fm-Scrubbler-WPF ikke en daglig scrobblegrænse. Dette er nu ændret, da nogle mennesker brugte Scrubbler til at scrobble så mange numre, at det forårsagede problemer for Last.fm-siden. Scrobblegrænsen er i øjeblikket 2800 scrobbles pr. dag. Når du prøver at scrobble mere end det, får du en fejlmeddelelse. Der er planer om at tilføje en 'scrobblekø', så hvis du har brug for at scrobble mere end 2800 numre, tilføjes de til en kø og scrobbles automatisk efter nogen tid. Du kan tjekke, hvor mange scrobbles du har tilbage i brugerudvælgelsesvisningen.

Når alle poster er uploadet til serveren, vil du se en besked i bunden af appvinduet, der bekræfter: 'Valgte numre scrobblet med succes.'

![Valgte numre scrobblet med succes.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Nu kan du åbne din profil på [Last.fm](http://Last.fm)-siden og kontrollere alle ændringerne.

![din profil på Last.fm-siden](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Ofte stillede spørgsmål

{{% details title="Kan jeg scrobble automatisk uden at eksportere CSV-filer?" closed="true" %}}
Ja. Både Evermusic og Flacbox understøtter nu automatisk Last.fm-scrobbling. Se guiden: [Sådan scrobbler du til Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Hvad hvis min CSV har numre ældre end 14 dage?" closed="true" %}}
Brug Importtilstand i Last.fm-Scrubbler-WPF. Den genberegner tidsstempler fra Sluttidspunktet, så du kan scrobble numre uanset deres oprindelige dato.
{{% /details %}}

{{% details title="Jeg har ikke en Windows-computer. Kan jeg stadig bruge Last.fm-Scrubbler?" closed="true" %}}
Ja. Installér VirtualBox på din Mac og download det gratis Windows-udviklingsmiljø-billede fra Microsoft. Kør Last.fm-Scrubbler-WPF inde i den virtuelle maskine.
{{% /details %}}

{{% details title="Hvorfor analyseres nogle scrobbles ikke?" closed="true" %}}
Numre, der mangler vigtig metadata (som kunstnernavn), kan ikke analyseres. Dette er forventet og påvirker ikke andre numre i filen.
{{% /details %}}

{{% details title="Er der en daglig scrobblegrænse?" closed="true" %}}
Ja. Last.fm-Scrubbler-WPF tillader op til 2.800 scrobbles pr. dag. Hvis du har brug for at scrobble mere, fordel processen over flere dage.
{{% /details %}}
