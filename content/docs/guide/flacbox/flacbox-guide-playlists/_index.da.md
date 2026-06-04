---
title: "Afspilningslister"
date: 2020-02-01
description: "Lær at oprette, importere, administrere og tilpasse afspilningslister i Flacbox på iPhone, iPad og Mac. Byg afspilningslister fra cloud- og lokale filer, importer M3U / M3U8 / CUE, omarranger sange, rediger coverbillede, arkiver til ZIP, eksporter til M3U / CSV / TXT og brug offline-tilstand."
keywords: [
  "Flacbox afspilningslister", "importer M3U-afspilningsliste", "afspilningslistehåndtering",
  "opret afspilningsliste iPhone", "lydafspilningslister Flacbox",
  "brugerdefineret afspilningslistebillede", "slet sange fra afspilningsliste",
  "sorter afspilningsliste Flacbox", "omarranger afspilningsliste VoiceOver",
  "Flacbox M3U-eksport", "Flacbox CSV-eksport", "Flacbox afspilningslistearkiv",
  "Flacbox offline afspilningsliste", "Flacbox CUE-import", "Flacbox dubletsange"
]
tags: ["guide", "flacbox", "afspilningslister"]
readingTime: 7
---


I sektionen Afspilningslister finder du nyttige værktøjer til at administrere dine musiksamlinger. Dette område viser alle dine afspilningslister på ét sted. Øverst er der en knap **"..."** i navigationslinjen, der åbner en menu med forskellige afspilningslistemuligheder, samt en værktøjslinje med hurtige handlinger som Søg, Afspil alle og Bland alle. Hver afspilningsliste har også sin egen **"..."**-knap ved siden af titlen, der giver dig flere muligheder for netop den afspilningsliste.

Afspilningslister i Flacbox kan indeholde en blanding af online cloud-numre, offline downloadede filer og lokale filer fra din enhed — alt i én afspilningsliste — og afspilles problemfrit sammen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox afspilningslisternes hovedskærm" image="/docs/guide/flacbox/img/playlists-main.webp" >}}
{{< /cards >}}

## Oprettelse af en afspilningsliste

At oprette en ny afspilningsliste er ligetil. Du har to muligheder: tryk på knappen **+**, eller tryk på knappen **"..."** i øverste højre hjørne af navigationslinjen og vælg Ny afspilningsliste. Giv din afspilningsliste et meningsfuldt navn og tryk på Gem.

Dette åbner dialogen Tilføj sange, hvor du kan håndplukke de numre, du vil inkludere i din nye afspilningsliste. Numre er bekvemt kategoriseret efter kildetype:

- **Bibliotek** — numre, der allerede er i dit musikbibliotek.
- **Filer i denne applikation** — lydfiler i appens Documents-mappe (downloadet fra cloudlagring, importeret via Wi-Fi Drive eller tilføjet via Finder File Sharing).
- **Filer på denne enhed** — lydfiler placeret andre steder på din enhed, ikke i denne applikation.
- **Forbindelser** — online filer placeret i dine tilsluttede cloudlagringstjenester.

Som standard kan du kun tilføje et enkelt nummer til en afspilningsliste én gang. Hvis du vil tillade dubletter, skal du aktivere denne funktion i Indstillinger → Musikbibliotek → Afspilningslister → Dubletter i en afspilningsliste → Aktiver.

## Importer afspilningsliste

I Flacbox har vi tilføjet M3U / M3U8 / CUE-filimport, så du ikke manuelt skal genskabe afspilningslister efter at have skiftet fra en anden afspiller.

Gå først til sektionen Afspilningslister. Tryk derefter på knappen Mere i øverste højre hjørne. Vælg Importer afspilningsliste i menuen.

Vælg filplaceringen på den næste skærm. Understøttede muligheder inkluderer:

- Tilsluttet cloudlagring
- Filer i applikationen
- Filer på din enhed

Vælg tilsluttet cloudlagring og åbn mappen med afspilningslistefilen. Understøttede filendelser er M3U, M3U8 og CUE. Vælg afspilningslistefilen og tryk på Færdig for at bekræfte dit valg.

Appen analyserer afspilningslistefilen, opretter en liste over numre og finder disse filer i lageret for at kompilere en endelig afspilningsliste, som derefter importeres til musikbiblioteket. Vigtigt: M3U / CUE-filen skal indeholde korrekte stier til mediefilerne, og filerne skal faktisk eksistere på disse stier i dit lager. Læs mere om import af afspilningslister [her](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Skærmen Afspilningslistedetaljer

Når du åbner en afspilningsliste, vises skærmen Afspilningslistedetaljer. Du finder en knap **"..."** i øverste højre hjørne med afspilningslistemuligheder og tre knapper under coverbilledet: Søg, Fortsæt afspilning, Afspil alle og Bland alle. Der er også et afkrydsningsfelt til Offline-tilstand til at slå fuld-afspilningsliste offline-synkronisering til og fra.

- **Fortsæt afspilning** — gendanner den sidst gemte afspilningsposition for denne afspilningsliste.
- **Søg** — udfør en søgning inden for den aktuelle afspilningsliste.
- **Afspil alle** — tilføjer alle numre fra den aktuelle afspilningsliste til afspillerkøen.
- **Bland alle** — som **Afspil alle**, men blander numrene, inden de tilføjes til lydafspillerens kø.
- **Offline-tilstand** — downloader alle numre fra denne afspilningsliste til lokale filer. Nye elementer tilføjet til afspilningslisten downloades også automatisk.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox afspilningslistedetaljerskærm" image="/docs/guide/flacbox/img/playlist-details-screen.webp" >}}
{{< /cards >}}

## Flere handlinger for en afspilningsliste på afspilningslisternes hovedskærm

Du kan tilgå handlinger for en afspilningsliste ved at trykke på knappen **"..."** nær afspilningslistetitlen. Tilgængelige handlinger:

- **Afspil alle** — tilføjer afspilningslistenumre til en ny afspillerkø.
- **Afspil næste** — tilføjer afspilningslistenumre til toppen af den eksisterende afspillerkø.
- **Afspil senere** — tilføjer afspilningslistenumre til bunden af den eksisterende afspillerkø.
- **Rediger billede** — ændrer afspilningslistens coverbillede.
- **Aktiver offline-tilstand** — slår offline-tilstand til for afspilningslisten. Både eksisterende og nye numre downloades automatisk. Læs mere om offline-tilstand [her](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Eksporter sangliste** — eksporterer denne afspilningsliste til **M3U / M3U8 / CSV / TXT** som beskrevet [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Føj til arkiv** — arkiverer denne afspilningsliste (inkl. m3u-fil, albumcover og alle numre) i en enkelt ZIP som beskrevet [her](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to). Premium-funktion.
- **Tilføj sange** — tilføjer flere sange til den aktuelle afspilningsliste.
- **Omdøb** — omdøber afspilningslisten.
- **Slet afspilningsliste** — sletter afspilningslisten fra musikbiblioteket. **Denne handling kan ikke fortrydes.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox – Flere handlinger for en afspilningsliste på hovedskærmen" image="/docs/guide/flacbox/img/more-actions-for-playlist-in-playlists-main-screen.webp" >}}
{{< /cards >}}

## Flere handlinger for en afspilningsliste på afspilningslistedetaljerskærmen

Du kan tilgå handlinger for en afspilningsliste ved at trykke på knappen **"..."** i øverste højre hjørne. Tilgængelige handlinger:

- **Vælg** — aktiverer nummervalgstilstand, nyttig til at slette flere numre fra afspilningslisten eller ændre deres rækkefølge.
- **Afspil næste** — tilføjer afspilningslistenumre til toppen af den eksisterende afspillerkø.
- **Afspil senere** — tilføjer afspilningslistenumre til bunden af den eksisterende afspillerkø.
- **Tilføj sange** — tilføjer nye sange til afspilningslisten.
- **Omarranger sange** — skifter manuelt rækkefølgen af sange i afspilningslisten ved hjælp af træk-og-slip.
- **Omdøb** — omdøber den aktuelle afspilningsliste.
- **Rediger billede** — ændrer albumcoverbilledet for den aktuelle afspilningsliste.
- **Eksporter sangliste** — eksporterer denne afspilningsliste til **M3U / M3U8 / CSV / TXT**. Læs mere [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Føj til arkiv** — ZIP-komprimerer den aktuelle afspilningsliste inkl. alle numre og m3u-fil. Læs mere [her](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Sorter** — ændrer rækkefølgen af numre i afspilningslisten. Sorteringsmuligheder inkluderer **Sangtitel, Sangnummer, Album, Kunstner, Albumkunstner, Genre, Komponist, Bedømmelse, År, Slag pr. minut, Varighed, Filnavn, Filændringsdato, Filoprettelsesdato** og **Manuel**. Sorteringsindstillingen **Manuel** giver mulighed for manuel omarrangering af sange ved hjælp af træk-og-slip.
- **Søg** — søger efter en bestemt sang inden for den aktuelle afspilningsliste.
- **Gitter / Liste** — ændrer skærmlayoutpræsentation.
- **Slet afspilningsliste** — sletter afspilningslisten fra musikbiblioteket. Denne handling sletter ikke numre fra dit lager, men **den kan ikke fortrydes**.

## Ændring af sangrækkefølge i en afspilningsliste

For at ændre rækkefølgen af sange i en afspilningsliste skal du trykke på knappen **"..."** i øverste højre hjørne og vælge **Vælg** for at gå i valgstilstand. Brug omarranger-kontrollen og træk-og-slip-gestikker nær hvert nummer for at flytte dem op eller ned. Tryk på omarranger-kontrollen for at flytte nummeret til toppen af listen. For at afslutte valgstilstand og anvende ændringer skal du trykke på **Færdig**.

For en endnu enklere arbejdsgang på lange afspilningslister skal du vælge Flere handlinger → Omarranger sange for at gå i dedikeret træk-og-slip-omarranger-tilstand.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox – Omarranger sange i en afspilningsliste" image="/docs/guide/flacbox/img/playlist-details-rearange-songs.webp" >}}
{{< /cards >}}

## Ændring af afspilningslistens coverbillede

For at ændre coverbilledet for en afspilningsliste skal du trykke på knappen **"..."** i øverste højre hjørne og vælge **Rediger billede**. Vælg et billede fra de tilgængelige kilder (Fotos, Filer, cloudlagring eller et genereret coverbillede fra et nummer i afspilningslisten) og bekræft ved at trykke på **Færdig**.

## Tilføjelse af sange til en afspilningsliste

Åbn afspilningslisten og tryk på knappen **"..."** i øverste højre hjørne, og vælg derefter **Tilføj sange** for at åbne en dialog. Vælg de numre, du vil tilføje, og bekræft ved at trykke på **Færdig**.

## Sletning af flere sange fra en afspilningsliste

Åbn afspilningslisten, tryk på knappen **"..."** i øverste højre hjørne, og vælg **Vælg** for at gå i valgstilstand. Vælg de numre, du vil slette, og tryk på **Slet fra afspilningsliste** nederst på skærmen. Bekræft ved at trykke på **Færdig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox – valgstilstand på afspilningslistedetaljerskærmen" image="/docs/guide/flacbox/img/selection-mode-playlist-details-screen.webp" >}}
{{< /cards >}}

## Nummerindstillinger

Hvert nummer i en afspilningsliste har en liste over handlinger, tilgængeligt ved at trykke på knappen **"..."**. Hvis du ikke kan se alle handlinger, skal du scrolle ned for at se dem. Du kan slette nummeret fra afspilningslisten, downloade det, redigere lydtags og meget mere.

- **Afspil næste** — tilføjer nummeret til toppen af afspillerkøen.
- **Afspil senere** — tilføjer nummeret til bunden af afspillerkøen.
- **Føj til en afspilningsliste** — tilføjer nummeret til en anden afspilningsliste.
- **Føj til favoritter** — markerer nummeret som en favorit for hurtig adgang.
- **Downloade** — gør nummeret tilgængeligt offline. Det vises i overførselskøen og i fanen **Lokale filer** i sektionen **Downloadet musik** i musikbiblioteket.
- **Redigere lydtags** — åbner den indbyggede tag-editor til ændring af nummers metadata.
- **Åbn i** — eksporterer nummeret og åbner det i en anden app.
- **Vis i mappe** — afslører mappen, hvor lydfilen er placeret.
- **Vis i Finder** — for filer importeret fra din Mac afslører dette mappen, hvor lydfilen er placeret på din Mac.
- **Slet fra afspilningsliste** — sletter nummeret fra afspilningslisten.
- **Slet fra cloudtjeneste** — sletter nummeret fra afspilningslisten og den tilknyttede cloudtjeneste. **Denne handling kan ikke fortrydes.**
- **Slet fra musikbibliotek** — sletter nummeret fra musikbiblioteket, mens filen i lagringen forbliver uberørt.

## Tilgængelighed

Flacbox er fuldt tilgængeligt med **VoiceOver**-teknologi, hvilket sikrer, at hver komponent har en veldesignet etiket og beskrivelse. Når VoiceOver er aktiv, oversætter appen brugergrænsefladen til **Teksttilstand** og viser kun tilgængelige og nyttige elementer for at forbedre navigationshastighed og bekvemmelighed. Du kan også aktivere Teksttilstand i Indstillinger → Tilgængelighed → Teksttilstand.

### Justering af nummers position på en afspilningsliste med VoiceOver

1. Åbn en afspilningsliste og tryk på knappen **Mere**.
2. Vælg **Skift sangrækkefølge**. Visningen skifter til redigeringstilstand.
3. Tryk på ikonet for omarranger-indikatoren nær nummertitlen for at give det fokus.
4. **Dobbeltryk** hurtigt på ikonet for omarranger-indikatoren. Ved andet tryk skal du ikke slippe fingeren — hold den, indtil du hører en lyd, der indikerer, at cellen er klar til at blive flyttet.
5. Nu kan du flytte cellen til en ny position.

Andre komponenter fungerer som forventet ved hjælp af systemleverede VoiceOver-mønstre.
