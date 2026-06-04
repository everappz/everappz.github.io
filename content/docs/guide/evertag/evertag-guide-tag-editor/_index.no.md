---
title: "Tag-editor"
date: 2020-02-01
description: "Lær hvordan du bruker Evertag Tag Editor for å oppdatere musikk-metadata, redigere albumomslag, batchredigere flere filer og administrere tagger fra MusicBrainz. Ideell for å organisere musikkbiblioteket ditt på iOS og Mac."
keywords: [
  "Evertag tag-editor", "lydmetadata-editor", "musikktag-editor",
  "rediger lyd-tagger iPhone", "albumomslag-editor", "batch rediger lyd-tagger",
  "MusicBrainz metadata", "musikk-organisator app", "Evertag veiledning", "ID3 tag-editor"
]
tags: ["veiledning", "evertag", "tag-editor"]
readingTime: 5
---


**Tag-editoren** er hovedskjermen i Evertag-appen der du kan se og redigere lydfilmetadata. Åpne dette skjermbildet ved å trykke på en fil fra **Lokale filer**-seksjonen eller fra en tilkoblet **skylagring**-konto.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag-editor-skjerm" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Redigeringsmodi

Evertag tilbyr to redigeringsmodi:

- **Enkeltfilmodus**  
  - Naviger mellom filer ved å sveipe til venstre eller høyre på kunstverkkarusellen.  

- **Batchmodus**  
  - Rediger flere filer på en gang og bruk felles metadata.  
  - For å aktivere, blar du ned og trykker **Rediger filer samtidig**.

## Enkeltfilmodus

Som standard åpner appen tag-editoren i enkeltfilmodus med kun de viktigste redigeringsalternativene aktivert. I denne modusen kan du redigere de vanligste metadatafeltene, som:

**Sporstittel, Undertittel, Albumartist, Album, Artist, Komponist, Utøver, Sjanger, Kommentar, Beats per minutt, Podcast, Samling, Skivnummer, Sporsnummer, Sporsum, Vurdering, År**

For å få tilgang til alle tilgjengelige tagger, blar du til bunnen av skjermen og trykker på alternativet **Vis utvidede tagger**. Dette bytter editoren til utvidet modus, slik at du kan redigere over **120 metadatafelt**, inkludert **MusicBrainz-tagger**, **sangtekster**, **rådgivende vurderinger**, replay-gain-verdier, sorteringsrekkefølger, podcast-metadata og mer. Bruk **Innstillinger → Lyd-tag-editor → Knapper på hovedskjermen** for å aktivere Vis utvidede tagger permanent slik at den alltid er på.

{{< cards cols="1">}}
{{< card title="" subtitle="Nedre handlingspanel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Batchmodus

Du kan starte batchredigering på to måter:

1. **Fra filbehandleren**  
   - Trykk på **Flere handlinger** (•••) øverst til høyre.  
   - Trykk på **Velge**, velg flere filer, og trykk deretter **Redigere lydtagger**.

2. **Fra tag-editoren**  
   - Åpne en fil, bla ned og trykk **Rediger filer samtidig** for å laste alle filer fra samme mappe.

{{< cards cols="1">}}
{{< card title="" subtitle="Batchredigeringsmodus" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Trykk på **Lagre** etter redigering for å bruke endringer.

## Rediger sangtekster

Den utvidede editoren eksponerer **Sangtekster**-feltet. Trykk på det for å åpne sangtekstlisten — hvert sangtekstoppføring har sitt eget språk og beskrivelse, slik at ett enkelt spor kan lagre flere oversettelser.

Du trenger ikke å skrive sangtekster fra bunnen av. Editoren inkluderer ett-klikk søkesnarveier til de mest populære sangtekstdatabasene på nettet, forhåndsutfylt med gjeldende spors artist og tittel:

- **Lrclib** — go-to offentlig database for **tidsstemplede (LRC-stil) sangtekster**. Bruk den når du vil ha synkroniserte sangtekster som ruller linje for linje i spillere som støtter dem.
- **Genius** — stor katalog med annoteringer og nøyaktige ren-tekst sangtekster.
- **Lyricsify** — fellesskapsbasert database med vanlige og tidsstemplede sangtekster.
- **Google** — en generell nettsøk som et alternativ når de dedikerte databasene ikke har en treff.

Hver snarvei vises bare når den tilsvarende tjenesten er tilgjengelig fra enheten din. Trykk på en tjeneste, kopier sangtekstene (eller LRC-tidsstempler) du vil ha, gå tilbake til Evertag og lim dem inn i tekstfeltet — trykk deretter **Lagre** for å skrive sangtekstene tilbake til lydfilens tagger.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sangtekstsider" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Velg et språk fra velgeren:

{{< cards cols="1">}}
  {{< card title="" subtitle="Sangtekstspråkvelger" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Lim inn eller skriv deretter sangtekstteksten. Evertag støtter både ren tekst og tidsstemplet (synkronisert) sangtekst — plassholderen viser et eksempel på LRC-stilformatet, som er nøyaktig hva Lrclib og Lyricsify returnerer for synkroniserte resultater.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sangtekstteksteditor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Angi en vurdering og rådgivende vurdering

Den utvidede editoren tilbyr en stjernevurderingskontroll **Vurdering** ved siden av en **Rådgivende vurdering**-segmentkontroll.

### Stjernevurdering

Bruk **Vurdering**-feltet for å gi et spor en personlig poengsum fra én til fem stjerner. Verdien skrives inn i filens standard vurderingstag (POPM for ID3, `rate` for MP4, `RATING` for Vorbis/APE osv.), slik at andre apper som leser denne taggen — inkludert Musikk-appen, Plex, Roon og de fleste stasjonære tag-editorer — vil plukke opp poengene dine umiddelbart.

{{< cards cols="1">}}
  {{< card title="" subtitle="Vurdering" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Rådgivende vurdering

Den **rådgivende vurderingen** markerer et spors innhold ved hjelp av en av verdiene fra Foreldreadvarselsstandarden som iTunes Store og de fleste musikkplattformer bruker:

- **Uskadelig** — standard for spor uten foreldreadvarsels-informasjon. Filen behandles som egnet for alle lyttere og vil ikke vise noen rådgivende etikett i spillere som respekterer taggen.
- **Eksplisitt** — sporet inneholder eksplisitt språk eller innhold. Spillere som respekterer foreldrekontroll (Musikk-appen, Apple TV-appen, Spotify-eksporter, Plex osv.) vil vise et **E**-merke ved siden av tittelen og, når begrensninger er aktivert på enheten eller kontoen, kan skjule sporet fra barneprofiler eller nekte å spille det.
- **Ren** — en sensurert eller redigert versjon av et ellers eksplisitt spor. Spillere viser et **C**-merke slik at lyttere kan skille en ren redigering fra den originale eksplisitte masteren, noe som er nyttig når begge versjonene finnes i samme bibliotek.

Du ønsker å angi eller rette dette feltet når:

- En fil har feil etikett (for eksempel en ren radioedit som feilaktig var tagget som Eksplisitt, eller omvendt).
- Spor ble rippet eller lastet ned uten taggen og vises nå som Uskadelig selv om de inneholder eksplisitt innhold — nødvendig for at foreldrekontroll og delte familiebiblioteker skal fungere korrekt.
- Du forbereder et album for innsending eller deling og trenger at hvert spor bærer konsistent metadata.
- Du vil at CarPlay, Låseskjermen, Apple Music-lignende spillere eller DJ-programvare skal vise riktig **E** / **C**-merke ved siden av sporstitelen.

Verdien er lagret i standardfeltet for rådgivende vurdering for filformatet (`rtng` for MP4, `TXXX:ITUNESADVISORY` for ID3, `ITUNESADVISORY` for Vorbis), slik at enhver spiller som leser metadata for foreldreadvarsler vil se oppdateringen din.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sangtekst rådgivende vurdering" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Rediger albumomslag

Slik endrer du et albumomslag:

1. Trykk på **kameraikonet** i kunstverkkarusellen.  
2. Velg bildeplasseringen: Lokale filer, Sky, Nedlastinger eller Fotobibliotek.  
3. Velg et bilde som skal brukes som omslagskunstverk.

{{< cards cols="1">}}
  {{< card title="" subtitle="Velg bilde" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Flere handlinger i tag-editoren

Ekstra redigeringsalternativer er tilgjengelige via verktøylinjen under kunstverkvisningen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Meny for flere handlinger" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Automatisk søk etter lyd-tagger

Denne handlingen aktiverer den smarte tagsøkmotoren, som finner og fyller inn fullstendige metadata for lydfilen din basert på den eksisterende informasjonen.  
Appen bruker MusicBrainz-databasen — en av de mest omfattende tagdatabasene — med over **50 millioner** spor.

### Søk albumomslag

Bruk metadata til å søke på nettet etter riktig albumkunstverk.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Søk albumomslag" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Lagre bildet til **Bilder** ved hjelp av systemkontekstmenyen når du finner det.

{{< cards cols="1">}}
  {{< card title="" subtitle="Legg til bilde i bilder" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Gå deretter tilbake til tag-editoren, trykk på kameraikonet, gå til **Fotobiblioteket** og velg det lagrede bildet. Appen setter det som omslag for lydfilen din.

Du kan justere hvordan omslags bilder skaleres i app-innstillingene.

### Lagre albumkunstverk

Denne handlingen lagrer det gjeldende albumkunstverket i **Dokumenter**-mappen, slik at du kan gjenbruke det senere.

### Normaliser koding

Denne handlingen normaliserer tekstkodingen til alle tagger i lydfilens metadata. Det er spesielt nyttig hvis du bytter fra en Windows-PC, der filer kan bruke forskjellige kodinger som vises som uleselige eller forvanskede tegn på en Mac.

### Manuelt tag-søk

Søk etter albummetadata manuelt ved hjelp av MusicBrainz-databasen.  

- Velg albumet  

{{< cards cols="1">}}
  {{< card title="" subtitle="Velg album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Velg riktig sang  

{{< cards cols="1">}}
  {{< card title="" subtitle="Velg sang" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Velg hvilke tagger som skal brukes  

{{< cards cols="1">}}
  {{< card title="" subtitle="Velg lyd-tagger" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Trykk **Ferdig** for å bruke de valgte metadataene på sporet ditt.

### Slett lyd-tagger

Fjern alle metadatafelt for en fil. Nyttig når du starter fra bunnen av. Trykk **Lagre** for å bekrefte.

## Tag-editor-innstillinger

Naviger til **Innstillinger → Lyd-tag-editor** for å tilpasse oppførselen.

### Skalering av albumomslag

Velg hvordan albumomslag skal skaleres når de lagres i lydfiler. Du kan deaktivere skalering for å beholde original bildestørrelse, men vær oppmerksom på at noen spillere kanskje ikke støtter store kunstverkfiler. "Original størrelse"-alternativet er en del av Premium-personaliseringsfunksjonene.

### Alternativer for tagging

- **ID3v2.4** — Når aktivert, lagrer appen tagger i ID3v2.4-format når mulig. Deaktiver for å falle tilbake til det mer bredt støttede ID3v2.3 hvis lyd-taggene dine ikke vises riktig på eldre spillere eller enheter.
- **Duplikate tagger** — Når aktivert, dupliseres vanlige metadatafelt i begge tag-seksjonene i filen. Dette forbedrer kompatibiliteten med eldre lydspillere, men er i de fleste tilfeller ikke nødvendig.

### Alternativer for oppdatering av skyfil-metadata

Du kan kontrollere hvordan appen oppdaterer metadata for lydfiler lagret i skytjenester:

- **Vis bekreftelsesmelding**  
  Spør før du bruker metadataendringer på skyfiler.

- **Oppdater filens metadata automatisk**  
  Lagre metadataendringer automatisk i skyfilen etter redigering.

- **Ikke oppdater filens metadata**  
  Hopp over oppdatering av skyfiler — endringer gjelder bare lokalt.

### Rediger nettfiler

Velg hva som skjer med lokalt nedlastede kopier av skyfiler etter redigering:

- **Slett alltid nedlastet fil**  
  Fjern den lokale kopien etter lagring av endringer.

- **Ikke slett nedlastet fil**  
  Behold den nedlastede filen på enheten din etter redigering.

### Knapper på hovedskjermen

Tilpass hvilke handlinger som vises på tag-editorens hovedskjerm (Automatisk søk etter lyd-tagger, Manuelt søk etter lyd-tagger, Søk albumkunstverk, Lagre albumkunstverk, Normaliser koding, Slett lyd-tagger). Du kan også veksle **Vis utvidede tagger** og **Rediger filer samtidig** slik at editoren alltid åpner i din foretrukne modus.
