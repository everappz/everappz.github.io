---
title: "Spillelister"
date: 2020-01-01
description: "Lær å opprette, importere, tilpasse og administrere spillelister i Evermusic. Inkluderer detaljerte trinn for redigering, sortering, offline-modus og tilgjengelighet."
keywords: [
  "Evermusic", "spillelister", "spillelisteadministrasjon", "importer M3U-spilleliste",
  "rediger spilleliste", "offline spilleliste", "endre spillelisterekkefølge", "spillelisteomslag",
  "spillelistetilgjengelighet", "lydspiller"
]
tags: ["evermusic", "guide", "spillelister"]
readingTime: 6
---


## Oversikt

Spilleliste-seksjonen gir deg verktøyene til å organisere låtene dine i lister. Den inkluderer en innholdsvisning som viser alle opprettede spillelister, en "..."-knapp i navigasjonsbjelken som tilbyr ulike spillelisterelaterte handlinger, og en navigasjonsverktøylinje med knappene "Søk", "Spill alle" og "Bland alle". Dessuten har hver enkelt spilleliste selv en "..."-knapp nær spillelistetittelen, som tilbyr en rekke handlinger spesifikke for den spillelisten.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic spilleliste-skjerm" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-main.webp" >}}
{{< /cards >}}

## Opprette en spilleliste

For å opprette en ny spilleliste, trykk enten på "+"-knappen eller "..."-knappen øverst til høyre i navigasjonsbjelken, velg "Ny spilleliste" og tilordne et navn til spillelisten. Etter å ha navngitt den, trykk "Lagre."

{{< cards cols="1">}}
  {{< card title="" subtitle="Opprett en ny spilleliste" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-add-new.webp" >}}
{{< /cards >}}

Dette åpner dialogen "Legg til sanger", der du kan velge hvilke låter du vil legge til i den nye spillelisten. Låter er kategorisert etter kildetype, og du har flere alternativer:

- **Bibliotek**: Låter fra musikkbiblioteket ditt.
- **Filer i denne applikasjonen**: Lydfiler lagret i appens Dokumenter-katalog.
- **Filer på denne iPhone/iPad/Mac**: Lydfiler som er plassert i andre mapper på enheten, utenfor appen.
- **Tilkoblinger**: Online-filer lagret i tilkoblede skylagringstjenester.

Som standard kan du bare legge til en låt i en spilleliste én gang. For å tillate dupliserte sanger i en spilleliste, aktiver denne funksjonen i appinnstillingene - Musikkbibliotek - Spillelister - Duplikater i en spilleliste - Aktiver.

## Importer spilleliste

I Evermusic har vi lagt til M3U-filimportfunksjonalitet, slik at du ikke trenger å opprette spillelister manuelt.

{{< cards cols="1">}}
  {{< card title="" subtitle="Importer spilleliste fra en filkilde" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-import-from-files.webp" >}}
{{< /cards >}}

Gå først til 'Spillelister'-seksjonen. Trykk deretter på 'Mer'-knappen øverst til høyre. Fra menyen som vises, velg alternativet 'Importer spilleliste'.

På den neste skjermen, velg filstedet. Støttede alternativer inkluderer:

- Tilkoblet skylagring
- Filer i applikasjonen
- Filer på enheten din

La oss velge tilkoblet skylagring og åpne mappen som inneholder spillelistefilen. Støttede spillelistfilutvidelser inkluderer M3U, M3U8 og CUE. Velg spillelistefilen og trykk 'Ferdig' for å bekrefte valget.

Appen vil analysere spillelistefilen, opprette en liste over låter og finne disse filene på lagringen for å sette sammen en endelig spilleliste, som vil bli importert til musikkbiblioteket. Det er avgjørende at M3U/CUE-filen inneholder de riktige banene for mediafiler, og filene bør være plassert på disse banene på lagringen. Du kan lese mer om spillelisteimport [her](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Spillelistedetaljskjerm

Når du åpner en spilleliste, vises "Spillelistedetaljskjermen". På denne skjermen finner du en "..."-knapp øverst til høyre med spillelistealternativer og tre knapper under omslaget: "Søk", "Fortsett avspilling", "Spill alle" og "Bland alle". I tillegg er det en "Offline-modus"-avmerkingsboks.

{{< cards cols="1">}}
  {{< card title="" subtitle="Spillelistedetaljskjerm" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-detail-screen.webp" >}}
{{< /cards >}}

- **Fortsett avspilling**: Gjenopprett avspillingsposisjonen for denne spillelisten.
- **Søk**: Utfør et søk i gjeldende spilleliste.
- **Spill alle**: Legg til alle låter fra gjeldende spilleliste i spillerkøen.
- **Bland alle**: Ligner på "Spill alle", men blander låtene før de legges til i lydspillerkøen.
- **Offline-modus**: Last ned alle låter fra denne spillelisten til lokale filer. Nye elementer som legges til spillelisten vil automatisk lastes ned.

## Flere handlinger for spilleliste i spilleliste-skjermen

Du kan åpne handlinger for en spilleliste ved å trykke på "..."-knappen nær spillelistetittelen. Her er de tilgjengelige handlingene:

- **Spill alle:** Legger spillelistelåter til den nye spillerkøen.
- **Spill neste:** Legger spillelistelåter øverst i den eksisterende spillerkøen.
- **Spill senere:** Legger spillelistelåter nederst i den eksisterende spillerkøen.
- **Rediger bilde:** Rediger spillelistens omslags bilde.
- **Aktiver offline-modus:** Aktiverer offline-modus for spillelisten. I dette scenariet vil både eksisterende og nye låter lastes ned automatisk. Les mer om offline-modus [her](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Eksporter sangliste:** Du kan eksportere denne spillelisten til forskjellige formater som beskrevet [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Legg til arkiv:** Du kan arkivere denne spillelisten inkludert m3u-fil, albumomslag og alle låter som beskrevet [her](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Legg til sanger:** Legg til flere sanger i den gjeldende spillelisten.
- **Gi nytt navn:** Gi nytt navn til spillelisten.
- **Slett spilleliste:** Slett spillelisten fra musikkbiblioteket. Merk at denne handlingen ikke kan angres.

{{< cards cols="1">}}
  {{< card title="" subtitle="Meny med flere handlinger for en spilleliste" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-more-actions-for-separate-playlist.webp" >}}
{{< /cards >}}

## Flere handlinger for spilleliste i spillelistedetaljskjermen

Du kan åpne handlinger for en spilleliste ved å trykke på "..."-knappen øverst til høyre. Her er de tilgjengelige handlingene:

- **Velge:** Aktiverer sporvalg-modus, nyttig for å slette flere spor fra spillelisten eller endre rekkefølgen.
- **Spill neste:** Legger spillelistelåter øverst i den eksisterende spillerkøen.
- **Spill senere:** Legger spillelistelåter nederst i den eksisterende spillerkøen.
- **Legg til sanger:** Legg til nye sanger i spillelisten.
- **Omorganiser sanger:** Endre rekkefølgen på sanger i spillelisten manuelt ved hjelp av dra-og-slipp.
- **Gi nytt navn:** Gi nytt navn til den gjeldende spillelisten.
- **Rediger bilde:** Rediger albumomslagets bilde for den gjeldende spillelisten.
- **Eksporter sangliste:** Eksporter denne spillelisten til forskjellige formater. Du kan lese mer [her](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Legg til arkiv:** Zip gjeldende spilleliste inkludert alle låter og m3u-fil. Du kan lese mer [her](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Sorter:** Endre rekkefølgen på låter i spillelisten. Sorteringsalternativer inkluderer "Sangtittel", "Sangnummer", "Album", "Artist", "Albumartist", "Sjanger", "Komponist", "Vurdering", "År", "Slag per minutt", "Varighet", "Filnavn", "Filredigeringsdato", "Filopprinstingsdato" og "Manuell". Sorteringsalternativet "Manuell" tillater manuell omsortering av sanger ved hjelp av dra-og-slipp.
- **Søk:** Søk etter en bestemt sang i gjeldende spilleliste.
- **Rutenett/Liste:** Endre skjermoppsettspresentasjonen.
- **Slett spilleliste:** Slett spillelisten fra musikkbiblioteket. Viktig: denne handlingen sletter ikke låter fra lagringen din, og den kan ikke angres.

## Endre sangrekkefølge i en spilleliste

For å endre rekkefølgen på sanger i en spilleliste, trykk på "..."-knappen øverst til høyre og velg "Velge" for å gå inn i valg modus. Bruk omordningskontrollen og dra-og-slipp-gest nær hvert spor for å flytte dem opp eller ned. Å trykke på omordningskontrollen vil flytte sporet til toppen av listen. For å gå ut av valg modus og bruke endringer, trykk "Ferdig."

{{< cards cols="1">}}
  {{< card title="" subtitle="Endre sangrekkefølge i en spilleliste" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-change-songs-order.webp" >}}
{{< /cards >}}

## Endre spillelisteomslagets bilde

For å endre omslagsbildet til en spilleliste, trykk på "..."-knappen øverst til høyre og velg "Rediger bilde." Velg et bilde fra de tilgjengelige kildene og bekreft endringene ved å trykke "Ferdig."

## Legge til sanger i en spilleliste

Åpne spillelisten og trykk på "..."-knappen øverst til høyre, velg deretter "Legg til sanger" for å åpne en dialog. Velg låtene du vil legge til og bekreft endringene ved å trykke "Ferdig."

## Slette flere sanger fra en spilleliste

Åpne spillelisten, trykk på "..."-knappen øverst til høyre og velg "Velge" for å gå inn i valg modus. Velg låtene du vil slette og trykk på knappen "Slett fra spilleliste" nederst på skjermen. Bekreft endringene ved å trykke "Ferdig."

{{< cards cols="1">}}
  {{< card title="" subtitle="Valgmodus inne i en spilleliste" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-selection-mode-in-playlist-details-screen.webp" >}}
{{< /cards >}}

## Sporalternativer

Hvert spor i en spilleliste har en liste over handlinger, tilgjengelig ved å trykke på "..."-knappen. Hvis du ikke kan se alle handlingene, bla ned for å se dem. Du kan slette sporet fra spillelisten, laste det ned, redigere lydtagger og mer.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sporalternativmeny i en spilleliste" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-track-options.webp" >}}
{{< /cards >}}

- **Spill neste:** Legger til sporet øverst i spillerkøen.
- **Spill senere:** Legger til sporet nederst i spillerkøen.
- **Legg til en spilleliste:** Legger til sporet i en spilleliste.
- **Legg til favoritter:** Merker sporet som favoritt for rask tilgang.
- **Laste ned:** Gjør sporet tilgjengelig offline. Det vil vises i overføringskøen og fanen "Lokale filer" i seksjonen "Nedlastet musikk" i musikkbiblioteket.
- **Rediger lydtagger:** Åpner den innebygde tag-redigereren for å endre spormetadata.
- **Åpne i:** Eksporterer sporet og åpner det i en annen app.
- **Vis i mappe:** Avslører mappen der lydfilen er plassert.
- **Vis i Finder:** For filer importert fra Mac, avslører denne handlingen mappen der lydfilen er på Mac-datamaskinen.
- **Slett fra spilleliste:** Sletter sporet fra spillelisten.
- **Slett fra skytjeneste:** Sletter sporet fra spillelisten og den tilknyttede skytjenesten. Merk at denne handlingen ikke kan angres.
- **Slett fra musikkbibliotek:** Sletter sporet fra musikkbiblioteket, og lar filen på lagringen være urørt.

## Tilgjengelighet

Appen vår er fullt tilgjengelig med VoiceOver-teknologi, noe som sikrer at hvert komponent har en godt utformet etikett og beskrivelse. Når VoiceOver er aktiv, oversetter appen brukergrensesnittet til tekstmodus og viser bare tilgjengelige og nyttige elementer for å forbedre navigasjonshastighet og bekvemmelighet. Du kan også aktivere tekstmodus i Innstillinger > Tilgjengelighet > Tekstmodus.

For justering av sporposisjon i en spilleliste med VoiceOver:

1. Åpne en spilleliste og trykk på "Mer"-knappen.
2. Velg "Endre sangrekkefølge." Visningen bytter til redigeringsmodus.
3. Trykk på ikonet for omordningsindikator nær sporttittelen for å gi det fokus.
4. Dobbelttapp raskt på ikonet for omordningsindikator. På det andre trykket, ikke slipp fingeren — hold til du hører en lyd som indikerer at cellen er klar til å flyttes.
5. Nå kan du flytte cellen til en ny posisjon.

Andre komponenter fungerer som forventet, ved hjelp av systemleverte VoiceOver-mønstre.
