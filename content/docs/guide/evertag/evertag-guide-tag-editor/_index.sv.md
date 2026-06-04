---
title: "Taggeditor"
date: 2020-02-01
description: "Lär dig hur du använder Evertag Taggeditorn för att uppdatera musikmetadata, redigera albumomslag, batchredigera flera filer och hantera taggar från MusicBrainz. Idealisk för att organisera ditt musikbibliotek på iOS och Mac."
keywords: [
  "Evertag taggeditor", "ljudmetadataeditor", "musiktaggeditor",
  "redigera ljudtaggar iPhone", "albumomslagseditor", "batchredigera ljudtaggar",
  "MusicBrainz-metadata", "musikorganisationsapp", "Evertag-guide", "ID3-taggeditor"
]
tags: ["guide", "evertag", "taggeditor"]
readingTime: 5
---


**Taggeditorn** är Evertag-appens huvudskärm där du kan visa och redigera ljudfilsmetadata. Öppna den här skärmen genom att trycka på en fil från avsnittet **Lokala filer** eller från vilket som helst anslutet **molnlagringskonto**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Taggeditorskärm" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Redigeringslägen

Evertag erbjuder två redigeringslägen:

- **Enkelfil-läge**
  - Navigera mellan filer genom att svepa åt vänster eller höger på konstkarrusellen.

- **Batchläge**
  - Redigera flera filer på en gång och tillämpa delade metadata.
  - För att aktivera, scrolla till botten och tryck på **Redigera filer simultant**.

## Enkelfil-läge

Som standard öppnar appen taggeditorn i enkelfil-läge med endast de viktigaste redigeringsalternativen aktiverade. I det här läget kan du redigera de vanligaste metadatafälten, som:

**Spårtitel, Undertitel, Albumartist, Album, Artist, Kompositör, Utövare, Genre, Kommentar, Slag per minut, Podcast, Samling, Skivnummer, Spårnummer, Spårantal, Betyg, År**

För att komma åt alla tillgängliga taggar, scrolla till botten av skärmen och tryck på alternativet **Visa utökade taggar**. Detta växlar editorn till utökat läge, vilket låter dig redigera över **120 metadatafält**, inklusive **MusicBrainz-taggar**, **Texter**, **Rådgivande betyg**, replay-gain-värden, sorteringsordningar, podcast-metadata och mer. Använd **Inställningar → Ljudtaggeditor → Knappar på huvudskärmen** för att permanent aktivera Visa utökade taggar så att det alltid är på.

{{< cards cols="1">}}
{{< card title="" subtitle="Undre åtgärdspanel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Batchläge

Du kan aktivera batchredigering på två sätt:

1. **Från filhanteraren**
   - Tryck på **Fler åtgärder** (•••) i det övre högra hörnet.
   - Tryck på **Välja**, välj flera filer och tryck sedan på **Redigera ljudtaggar**.

2. **Från taggeditorn**
   - Öppna valfri fil, scrolla till botten och tryck på **Redigera filer simultant** för att ladda alla filer från samma mapp.

{{< cards cols="1">}}
{{< card title="" subtitle="Batchredigeringsläge" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Efter redigering trycker du på **Spara** för att tillämpa ändringar.

## Redigera texter

Den utökade editorn visar fältet **Texter**. Tryck på det för att öppna texterlistan — varje textinlägg har sitt eget språk och beskrivning, så ett enda spår kan lagra flera översättningar.

Du behöver inte skriva texter från grunden. Editorn innehåller enkeltryckssökgenvägar till de mest populära textdatabaserna på webben, förifyllda med det aktuella spårets artist och titel:

- **Lrclib** — den föredragna offentliga databasen för **tidsinställda (LRC-stil) texter**. Använd den när du vill ha synkroniserade texter som rullar rad för rad i spelare som stödjer dem.
- **Genius** — stor katalog med anteckningar och korrekta texter i ren text.
- **Lyricsify** — gemenskapsdriven databas med vanliga och tidsstämplade texter.
- **Google** — en allmän webbsökning som reserv när de dedikerade databaserna inte har en matchning.

Varje genväg visas bara när motsvarande tjänst är nåbar från din enhet. Tryck på en tjänst, kopiera texterna (eller LRC-tidsstämplarna) du vill ha, återvänd till Evertag och klistra in dem i textfältet — tryck sedan på **Spara** för att skriva tillbaka texterna i ljudfilens taggar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Textsidor" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Välj ett språk från väljaren:

{{< cards cols="1">}}
  {{< card title="" subtitle="Textersspråksväljare" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Klistra sedan in eller skriv texttexten. Evertag stödjer både ren text och tidsstämplade (synkroniserade) texter — platshållaren visar ett exempel på LRC-stilsformatet, vilket är exakt vad Lrclib och Lyricsify returnerar för synkroniserade resultat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Texttexteditor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Ange ett betyg och ett rådgivande betyg

Den utökade editorn erbjuder en stjärn- **Betyg**-kontroll vid sidan av en segmenterad **Rådgivande betyg**-kontroll.

### Stjärnbetyg

Använd fältet **Betyg** för att ge ett spår ett personligt betyg från ett till fem stjärnor. Värdet skrivs in i filens standardbetygstagg (POPM för ID3, `rate` för MP4, `RATING` för Vorbis/APE, etc.), så andra appar som läser den här taggen — inklusive Music-appen, Plex, Roon och de flesta skrivbordstaggeditorerna — omedelbart hämtar dina betyg.

{{< cards cols="1">}}
  {{< card title="" subtitle="Betyg" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Rådgivande betyg

**Rådgivande betyg** markerar ett spårs innehåll med ett av värdena från Föräldradeklarationsstandarden som iTunes Store och de flesta musikplattformar använder:

- **Icke-offensivt** — standardvärdet för spår utan information om föräldrarådgivning. Filen behandlas som lämplig för alla lyssnare och visar inte någon rådgivningsetikett i spelare som respekterar taggen.
- **Explicit** — spåret innehåller explicit språk eller innehåll. Spelare som respekterar föräldrakontroller (Music-appen, Apple TV-appen, Spotify-exporter, Plex, etc.) visar ett **E**-märke bredvid titeln och när begränsningar är aktiverade på enheten eller kontot kan de dölja spåret från barnprofiler eller vägra att spela det.
- **Ren** — en censurerad eller redigerad version av ett annars explicit spår. Spelare visar ett **C**-märke så att lyssnare kan skilja en ren redigering från den ursprungliga explicita mastern, vilket är användbart när båda versionerna lever i samma bibliotek.

Du vill ange eller fixa det här fältet när:

- En fil har fel etikett (till exempel en ren radiokopia som felaktigt märkts som Explicit, eller vice versa).
- Spår rippades eller laddades ner utan taggen och visas nu som Icke-offensivt trots att de innehåller explicit innehåll — nödvändigt för att föräldrakontroller och familjedelade bibliotek ska fungera korrekt.
- Du förbereder ett album för inlämning eller delning och behöver att varje spår bär konsekvent metadata.
- Du vill att CarPlay, låsskärmen, Apple Music-stilspelare eller DJ-programvara ska visa rätt **E** / **C**-märke bredvid spårtiteln.

Värdet lagras i standardrådgivande betyg-fältet för filformatet (`rtng` för MP4, `TXXX:ITUNESADVISORY` för ID3, `ITUNESADVISORY` för Vorbis), så att alla spelare som läser föräldrarådgivande metadata ser din uppdatering.

{{< cards cols="1">}}
  {{< card title="" subtitle="Texternas rådgivande betyg" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Redigera albumomslag

För att ändra ett albumomslag:

1. Tryck på ikonen **Kamera** i konstkarrusellen.
2. Välj bildplats: Lokala filer, Moln, Nedladdningar eller Fotobibliotek.
3. Välj en bild att tillämpa som omslagskonst.

{{< cards cols="1">}}
  {{< card title="" subtitle="Välj bild" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Fler åtgärder i taggeditorn

Extra redigeringsalternativ är tillgängliga via verktygsfältet under konstkarrusellen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menyn Fler åtgärder" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Autosök ljudtaggar

Den här åtgärden aktiverar den smarta taggsökmotorn, som hittar och fyller i komplett metadata för din ljudfil baserat på befintlig information.  
Appen använder MusicBrainz-databasen — en av de mest omfattande tagdatabaserna — med över **50 miljoner** spår.

### Sök albumomslag

Använd metadata för att söka webben efter rätt albumkonstverk.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sök albumomslag" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

När den hittats, spara bilden i dina **Foton** med hjälp av systemets kontextmeny.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lägg till bild i Foton" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Därefter återvänder du till taggeditorn, trycker på kameraikonen, går till **Fotobibliotek** och väljer den sparade bilden. Appen sätter den som omslag för din ljudfil.

Du kan justera hur omslagsbilder skalas i appens inställningar.

### Spara albumkonstverk

Den här åtgärden sparar det aktuella albumkonstarverket i mappen **Dokument** så att du kan återanvända det senare.

### Normalisera kodning

Den här åtgärden normaliserar textkodningen för alla taggar i ljudfilens metadata. Det är särskilt användbart om du byter från en Windows-PC, där filer kan använda olika kodningar som visas som oläsliga eller förvrängda tecken på en Mac.

### Manuell taggsökning

Sök manuellt efter albummetadata med hjälp av MusicBrainz-databasen.

- Välj albumet

{{< cards cols="1">}}
  {{< card title="" subtitle="Välj album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Välj rätt låt

{{< cards cols="1">}}
  {{< card title="" subtitle="Välj låt" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Välj vilka taggar som ska tillämpas

{{< cards cols="1">}}
  {{< card title="" subtitle="Välj ljudtaggar" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Tryck på **Färdig** för att tillämpa den valda metadatan på ditt spår.

### Ta bort ljudtaggar

Rensa alla metadatafält för en fil. Användbart när man börjar från grunden. Tryck på **Spara** för att bekräfta.

## Taggeditorsinställningar

Navigera till **Inställningar → Ljudtaggeditor** för att anpassa beteendet.

### Albumomslagsskalning

Välj hur albumomslag ska skalas när de sparas i ljudfiler. Du kan inaktivera skalning för att behålla den ursprungliga bildstorleken, men tänk på att vissa spelare kanske inte stödjer stora konstverk. Alternativet "originalstorlek" är en del av Premium-personaliseringsfunktionerna.

### Alternativ för tagglagring

- **ID3v2.4** — När aktiverat sparar appen taggar i ID3v2.4-format när möjligt. Inaktivera för att falla tillbaka till det mer brett stödda ID3v2.3 om dina ljudtaggar inte visas korrekt på äldre spelare eller enheter.
- **Duplicerade taggar** — När aktiverat dupliceras vanliga metadatafält i båda taggsektionerna i filen. Detta förbättrar kompatibiliteten med äldre ljudspelare, men i de flesta fall krävs det inte.

### Molnfilsmetadatauppdateringsalternativ

Du kan kontrollera hur appen uppdaterar metadata för ljudfiler lagrade i molntjänster:

- **Visa bekräftelsemeddelande**  
  Fråga innan metadataändringar tillämpas på molnfiler.

- **Uppdatera filens metadata automatiskt**  
  Spara metadataändringar i molnfilen automatiskt efter redigering.

- **Uppdatera inte filens metadata**  
  Hoppa över uppdatering av molnfiler — ändringar tillämpas bara lokalt.

### Redigera onlinefiler

Välj vad som händer med lokalt nedladdade kopior av molnfiler efter redigering:

- **Ta alltid bort den nedladdade filen**  
  Ta bort den lokala kopian efter att du sparat ändringar.

- **Ta inte bort den nedladdade filen**  
  Behåll den nedladdade filen på din enhet efter redigering.

### Knappar på huvudskärmen

Anpassa vilka åtgärder som visas på taggeditorns huvudskärm (Autosök ljudtaggar, Manuell sökning ljudtaggar, Sök albumomslag, Spara albumomslag, Normalisera kodning, Ta bort ljudtaggar). Du kan också aktivera **Visa utökade taggar** och **Redigera filer simultant** så att editorn alltid öppnas i ditt föredragna läge.
