---
title: "Tageditor"
date: 2020-02-01
description: "Lær hvordan du bruger Evertag Tagredaktøren til at opdatere musikmetadata, redigere albumomslag, batchredigere flere filer og administrere tags fra MusicBrainz. Ideel til at organisere dit musikbibliotek på iOS og Mac."
keywords: [
  "Evertag tageditor", "lydmetadataeditor", "musiktageditor",
  "rediger lydtags iPhone", "albumomslagseditor", "batchrediger lydtags",
  "MusicBrainz metadata", "musikorganisator-app", "Evertag vejledning", "ID3-tageditor"
]
tags: ["vejledning", "evertag", "tageditor"]
readingTime: 5
---


**Tagreditoren** er Evertag-appens hovedskærm, hvor du kan se og redigere lydfilmetadata. Åbn denne skærm ved at trykke på en fil fra sektionen **Lokale filer** eller fra en hvilken som helst tilsluttet **cloudlagrings**konto.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tagredaktørskærm" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Redigeringstilstande

Evertag tilbyder to redigeringstilstande:

- **Enkeltfilstilstand**  
  - Naviger mellem filer ved at swipe til venstre eller højre på kunstværkskarusellen.  

- **Batchtilstand**  
  - Rediger flere filer på én gang og anvend delte metadata.  
  - For at aktivere skal du scrolle til bunden og trykke på **Rediger flere filer samtidigt**.

## Enkeltfilstilstand

Som standard åbner appen tagreditoren i enkeltfilstilstand med kun de vigtigste redigeringsmuligheder aktiveret. I denne tilstand kan du redigere de mest almindelige metadatafelter, såsom:

**Sporets titel, Undertitel, Albuminterpret, Album, Interpret, Komponist, Performer, Genre, Kommentar, Slag pr. minut, Podcast, Kompilering, Disknummer, Spornummer, Spor i alt, Bedømmelse, År**

For at få adgang til alle tilgængelige tags skal du scrolle til bunden af skærmen og trykke på indstillingen **Vis udvidede tags**. Dette skifter editoren til udvidet tilstand, hvilket giver dig mulighed for at redigere over **120 metadatafelter**, herunder **MusicBrainz-tags**, **Lyrics**, **Rådgivende bedømmelser**, replay-gain-værdier, sorteringsrækkefølger, podcast-metadata og mere. Brug **Indstillinger → Lydtagseditor → Knapper på hovedskærmen** for permanent at slå Vis udvidede tags til, så det altid er aktiveret.

{{< cards cols="1">}}
{{< card title="" subtitle="Bundhandlingspanel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Batchtilstand

Du kan gå ind i batchredigering på to måder:

1. **Fra filhåndteringen**  
   - Tryk på **Flere handlinger** (•••) øverst til højre.  
   - Tryk på **Vælg**, vælg flere filer, og tryk derefter på **Rediger lydtags**.

2. **Fra Tagreditoren**  
   - Åbn en fil, scroll til bunden, og tryk på **Rediger filer samtidigt** for at indlæse alle filer fra den samme mappe.

{{< cards cols="1">}}
{{< card title="" subtitle="Batchredigeringstilstand" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Tryk på **Gem** for at anvende ændringer efter redigering.

## Rediger lyrics

Den udvidede editor viser feltet **Lyrics**. Tryk på det for at åbne lyrics-listen — hver lyrics-post har sit eget sprog og sin egen beskrivelse, så et enkelt spor kan gemme flere oversættelser.

Du behøver ikke at skrive lyrics fra bunden. Editoren inkluderer søgegenveje med ét tryk til de mest populære lyrics-databaser på nettet, forudfyldt med det aktuelle spors interpret og titel:

- **Lrclib** — den foretrukne offentlige database til **tidsstemplede (LRC-stil) lyrics**. Brug den, når du ønsker synkroniserede lyrics, der ruller linje for linje i afspillere, der understøtter dem.
- **Genius** — stort katalog med annotationer og nøjagtige tekstlyriks.
- **Lyricsify** — fællesskabsdrevet database med almindelige og tidsstemplede lyrics.
- **Google** — en generel websøgning som reserve, når de dedikerede databaser ikke har et match.

Hver genvej vises kun, når den tilsvarende tjeneste er tilgængelig fra din enhed. Tryk på en tjeneste, kopier de lyrics (eller LRC-tidsstempler), du ønsker, vend tilbage til Evertag, og indsæt dem i tekstfeltet — tryk derefter på **Gem** for at skrive lyrics tilbage i lydfilens tags.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics-sider" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Vælg et sprog fra vælgeren:

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics-sprogsvælger" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Indsæt eller skriv derefter lyrics-teksten. Evertag understøtter både ren tekst og tidsstemplede (synkroniserede) lyrics — pladsholderen viser et eksempel på LRC-stilformatet, som er præcis, hvad Lrclib og Lyricsify returnerer for synkroniserede resultater.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics-teksteditor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Indstil en bedømmelse og rådgivende bedømmelse

Den udvidede editor tilbyder en stjerne-**Bedømmelse**-kontrol ved siden af en **Rådgivende bedømmelse**-segmenteret kontrol.

### Stjernebedømmelse

Brug feltet **Bedømmelse** til at give et spor en personlig score fra én til fem stjerner. Værdien skrives ind i filens standardbedømmelsestag (POPM for ID3, `rate` for MP4, `RATING` for Vorbis/APE osv.), så andre apps, der læser dette tag — herunder Musik-appen, Plex, Roon og de fleste skrivebords-tareditorer — straks opfanger dine scores.

{{< cards cols="1">}}
  {{< card title="" subtitle="Bedømmelse" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Rådgivende bedømmelse

Den **Rådgivende bedømmelse** markerer et spors indhold ved hjælp af en af værdierne fra Forældrenes rådgivningsstandard, som iTunes Store og de fleste musikplatforme bruger:

- **Ufarligt** — standarden for spor uden forældrenes rådgivningsoplysninger. Filen behandles som egnet for alle lyttere og viser ikke nogen rådgivende etiket i afspillere, der respekterer tagget.
- **Eksplicit** — sporet indeholder eksplicit sprog eller indhold. Afspillere, der respekterer forældrenes kontrol (Musik-appen, Apple TV-appen, Spotify-eksporter, Plex osv.), vil vise et **E**-mærke ved siden af titlen og, når begrænsninger er aktiveret på enheden eller kontoen, kan skjule sporet fra børns profiler eller nægte at afspille det.
- **Ren** — en censureret eller redigeret version af et ellers eksplicit spor. Afspillere viser et **C**-mærke, så lyttere kan skelne en ren redigering fra det originale eksplicitte master, hvilket er nyttigt, når begge versioner er i det samme bibliotek.

Du vil ønske at indstille eller rette dette felt, når:

- En fil har den forkerte etiket (for eksempel en ren radioversion, der fejlagtigt er tagget som Eksplicit eller omvendt).
- Spor blev rippet eller downloadet uden tagget og vises nu som Ufarlige, selvom de indeholder eksplicit indhold — nødvendigt for at forældrenes kontrol og familiedelte biblioteker fungerer korrekt.
- Du forbereder et album til indsendelse eller deling og har brug for, at hvert spor bærer konsistente metadata.
- Du ønsker, at CarPlay, låseskærmen, Apple Music-lignende afspillere eller DJ-software viser det korrekte **E** / **C**-mærke ved siden af sporets titel.

Værdien gemmes i det standard rådgivende bedømmelsesfelt for filformatet (`rtng` for MP4, `TXXX:ITUNESADVISORY` for ID3, `ITUNESADVISORY` for Vorbis), så enhver afspiller, der læser forældrenes rådgivende metadata, vil se din opdatering.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics rådgivende bedømmelse" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Rediger albumomslag

For at ændre et albumomslag:

1. Tryk på **Kameraikon** i kunstværkskarusellen.  
2. Vælg billedplaceringen: Lokale filer, Cloud, Downloads eller Fotobibliotek.  
3. Vælg et billede til at anvende som covertkunstværk.

{{< cards cols="1">}}
  {{< card title="" subtitle="Vælg billede" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Flere handlinger i Tagreditoren

Ekstra redigeringsmuligheder er tilgængelige via værktøjslinjen under kunstværksvisningen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Flere handlinger" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Automatisk søgning efter lydtags

Denne handling aktiverer den smarte tagsøgemaskine, der finder og udfylder komplette metadata for din lydfil baseret på eksisterende oplysninger.  
Appen bruger MusicBrainz-databasen — en af de mest omfattende tagdatabaser — med over **50 millioner** spor.

### Søg albumomslag

Brug metadata til at søge på nettet efter det korrekte albumkunstværk.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Søg albumomslag" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Når det er fundet, skal du gemme billedet til dine **Fotos** ved hjælp af systemkontekstmenuen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tilføj billede til Fotos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Derefter skal du vende tilbage til tagreditoren, trykke på Kameraikon, gå til **Fotobibliotek** og vælge det gemte billede. Appen indstiller det som omslag til din lydfil.

Du kan justere, hvordan omslagsbilleder skaleres i appens indstillinger.

### Gem albumkunstværk

Denne handling gemmer det aktuelle albumkunstværk i **Dokumenter**-mappen, så du kan genbruge det senere.

### Normaliser kodning

Denne handling normaliserer tekstkodningen af alle tags i lydfilens metadata. Det er særligt nyttigt, hvis du skifter fra en Windows-pc, hvor filer kan bruge forskellige kodninger, der vises som ulæselige eller uforståelige tegn på en Mac.

### Manuel tagsøgning

Søg efter albummetadata manuelt ved hjælp af MusicBrainz-databasen.  

- Vælg album  

{{< cards cols="1">}}
  {{< card title="" subtitle="Vælg album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Vælg det korrekte sang  

{{< cards cols="1">}}
  {{< card title="" subtitle="Vælg sang" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Vælg hvilke tags der skal anvendes  

{{< cards cols="1">}}
  {{< card title="" subtitle="Vælg lydtags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Tryk på **Færdig** for at anvende de valgte metadata på dit spor.

### Slet lydtags

Ryd alle metadatafelter for en fil. Nyttigt, når du starter forfra. Tryk på **Gem** for at bekræfte.

## Tagredaktørindstillinger

Naviger til **Indstillinger → Lydtagseditor** for at tilpasse adfærd.

### Albumomslagsskalering

Vælg, hvordan albumomslag skal skaleres, når de gemmes i lydfiler. Du kan deaktivere skalering for at beholde den originale billedstørrelse, men vær opmærksom på, at nogle afspillere muligvis ikke understøtter store kunstværksfiler. Indstillingen "original størrelse" er en del af Premium-personaliseringsfunktionerne.

### Taggemuligheder

- **ID3v2.4** — Når aktiveret, gemmer appen tags i ID3v2.4-formatet, når det er muligt. Deaktiver for at falde tilbage til det mere bredt understøttede ID3v2.3, hvis dine lydtags ikke vises korrekt på ældre afspillere eller enheder.
- **Duplikerede tags** — Når aktiveret, duplikeres fælles metadatafelter til begge tagsektioner af filen. Dette forbedrer kompatibiliteten med ældre lydafspillere, men er i de fleste tilfælde ikke påkrævet.

### Cloudfilmetadataopdateringsindstillinger

Du kan kontrollere, hvordan appen opdaterer metadata for lydfiler gemt i cloudtjenester:

- **Vis bekræftelsesbesked**  
  Spørg inden du anvender metadataændringer på cloudfiler.

- **Opdater automatisk filens metadata**  
  Gem metadataændringer i cloudfilen automatisk efter redigering.

- **Opdater ikke filens metadata**  
  Spring over opdatering af cloudfiler — ændringer anvendes kun lokalt.

### Rediger onlinefiler

Vælg, hvad der sker med lokalt downloadede kopier af cloudfiler efter redigering:

- **Slet altid den downloadede fil**  
  Fjern den lokale kopi efter lagring af ændringer.

- **Slet ikke den downloadede fil**  
  Behold den downloadede fil på din enhed efter redigering.

### Hovedskærmsknapper

Tilpas hvilke handlinger der vises på tagredaktørens hovedskærm (Automatisk søgning efter lydtags, Manuel søgning efter lydtags, Søg albumomslag, Gem albumomslag, Normaliser kodning, Slet lydtags). Du kan også slå **Vis udvidede tags** og **Rediger filer samtidigt** til, så editoren altid åbner i din foretrukne tilstand.
