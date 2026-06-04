---
title: "Taggeditor"
date: 2020-02-01
description: "Leer hoe je de Evertag Tag Editor gebruikt om muziekmetadata bij te werken, albumhoezen te bewerken, meerdere bestanden in batch te bewerken en tags van MusicBrainz te beheren. Ideaal voor het organiseren van je muziekbibliotheek op iOS en Mac."
keywords: [
  "Evertag taggeditor", "audiometadata-editor", "muziektageditor",
  "audiotags bewerken iPhone", "albumhoes-editor", "audiotags batch bewerken",
  "MusicBrainz metadata", "muziekorganisatie-app", "Evertag handleiding", "ID3 taggeditor"
]
tags: ["handleiding", "evertag", "taggeditor"]
readingTime: 5
---


De **Taggeditor** is het hoofdscherm van de Evertag-app waar je audiobestandmetadata kunt bekijken en bewerken. Open dit scherm door op een bestand te tikken in het gedeelte **Lokale bestanden** of vanuit een verbonden **cloudopslag**-account.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Taggeditor Scherm" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Bewerkingsmodi

Evertag biedt twee bewerkingsmodi:

- **Enkelvoudige bestandsmodus**  
  - Navigeer tussen bestanden door naar links of rechts te vegen op de artworkcarrousel.  

- **Batchmodus**  
  - Bewerk meerdere bestanden tegelijk en pas gedeelde metadata toe.  
  - Om te activeren, scrol naar beneden en tik op **Bestanden tegelijkertijd bewerken**.

## Enkelvoudige bestandsmodus

Standaard opent de app de taggeditor in de enkelvoudige bestandsmodus met alleen de belangrijkste bewerkingsopties ingeschakeld. In deze modus kun je de meest voorkomende metadatavelden bewerken, zoals:

**Tracktitel, Ondertitel, Albumartiest, Album, Artiest, Componist, Uitvoerder, Genre, Commentaar, Beats per minuut, Podcast, Compilatie, Schijfnummer, Tracknummer, Tracktotaal, Beoordeling, Jaar**

Om toegang te krijgen tot alle beschikbare tags, scrol naar de onderkant van het scherm en tik op de optie **Uitgebreide tags weergeven**. Dit schakelt de editor over naar de uitgebreide modus, waarmee je meer dan **120 metadatavelden** kunt bewerken, inclusief **MusicBrainz-tags**, **songteksten**, **adviesbeoordelingen**, replay-gain-waarden, sorteerorders, podcast-metadata en meer. Gebruik **Instellingen → Audio-taggeditor → Knoppen op het hoofdscherm** om Uitgebreide tags weergeven permanent in te schakelen.

{{< cards cols="1">}}
{{< card title="" subtitle="Onderste actiepaneel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Batchmodus

Je kunt op twee manieren batchbewerking starten:

1. **Vanuit Bestandsbeheerder**  
   - Tik op **Meer acties** (•••) rechtsboven.  
   - Tik op **Selecteren**, kies meerdere bestanden en tik vervolgens op **Audio-tags bewerken**.

2. **Vanuit Taggeditor**  
   - Open een bestand, scrol naar beneden en tik op **Bestanden tegelijkertijd bewerken** om alle bestanden uit dezelfde map te laden.

{{< cards cols="1">}}
{{< card title="" subtitle="Batchbewerkingsmodus" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Tik na het bewerken op **Opslaan** om wijzigingen toe te passen.

## Songteksten bewerken

De uitgebreide editor onthult het veld **Songteksten**. Tik erop om de songtekstenlijst te openen — elk songtekstitem heeft zijn eigen taal en beschrijving, zodat een enkel nummer meerdere vertalingen kan opslaan.

Je hoeft songteksten niet from scratch te typen. De editor bevat zoekopdrachten met één tik naar de populairste songtekstendatabases op het web, vooraf ingevuld met de artiest en titel van het huidige nummer:

- **Lrclib** — de standaard publieke database voor **getimede (LRC-stijl) songteksten**. Gebruik het wanneer je gesynchroniseerde songteksten wilt die regel voor regel scrollen in spelers die ze ondersteunen.
- **Genius** — grote catalogus met annotaties en nauwkeurige platte tekst songteksten.
- **Lyricsify** — gemeenschapsgestuurde database met gewone en getimede songteksten.
- **Google** — een algemene webzoekopdracht als alternatief wanneer de speciale databases geen overeenkomst hebben.

Elke snelkoppeling verschijnt alleen wanneer de bijbehorende service bereikbaar is vanaf je apparaat. Tik op een service, kopieer de songteksten (of LRC-tijdstempels) die je wilt, ga terug naar Evertag en plak ze in het tekstveld — tik dan op **Opslaan** om de songteksten terug te schrijven naar de tags van het audiobestand.

{{< cards cols="1">}}
  {{< card title="" subtitle="Songtekstpagina's" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Kies een taal uit de kiezer:

{{< cards cols="1">}}
  {{< card title="" subtitle="Songteksttaalkiezer" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Plak of typ vervolgens de songtekst. Evertag ondersteunt zowel platte tekst als getimede (gesynchroniseerde) songteksten — de plaatsaanduiding toont een voorbeeld van het LRC-stijlformaat, wat precies is wat Lrclib en Lyricsify retourneren voor gesynchroniseerde resultaten.

{{< cards cols="1">}}
  {{< card title="" subtitle="Songteksteditor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Een beoordeling en adviesbeoordeling instellen

De uitgebreide editor biedt een ster **Beoordeling**-besturingselement naast een **Adviesbeoordeling**-segmentbediening.

### Sterbeoordeling

Gebruik het veld **Beoordeling** om een nummer een persoonlijke score van één tot vijf sterren te geven. De waarde wordt geschreven in de standaard beoordelingstag van het bestand (POPM voor ID3, `rate` voor MP4, `RATING` voor Vorbis/APE, enz.), zodat andere apps die deze tag lezen — inclusief de Muziek-app, Plex, Roon en de meeste desktop-taggeditors — je scores onmiddellijk opnemen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Beoordeling" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Adviesbeoordeling

De **Adviesbeoordeling** markeert de inhoud van een nummer met een van de waarden uit de Parental Advisory-standaard die de iTunes Store en de meeste muziekplatformen gebruiken:

- **Niet aanstootgevend** — de standaard voor nummers zonder ouderlijk advies-informatie. Het bestand wordt behandeld als geschikt voor alle luisteraars en toont geen adviesetiket in spelers die de tag respecteren.
- **Expliciet** — het nummer bevat expliciete taal of inhoud. Spelers die ouderlijke controles respecteren (de Muziek-app, de Apple TV-app, Spotify-exports, Plex, enz.) tonen een **E**-badge naast de titel en kunnen, wanneer restricties op het apparaat of account zijn ingeschakeld, het nummer verbergen voor kinderprofielen of weigeren het te spelen.
- **Schoon** — een gecensureerde of bewerkte versie van een anders expliciete track. Spelers tonen een **C**-badge zodat luisteraars een schone edit kunnen onderscheiden van de originele expliciete master, wat handig is wanneer beide versies in dezelfde bibliotheek staan.

Je wilt dit veld instellen of corrigeren wanneer:

- Een bestand het verkeerde label heeft (bijvoorbeeld een schone radio-edit die per ongeluk als Expliciet is getagd, of vice versa).
- Nummers zijn geript of gedownload zonder de tag en nu als Niet aanstootgevend worden weergegeven, ook al bevatten ze expliciete inhoud — noodzakelijk voor ouderlijke controles en gedeelde familiebibliotheken om correct te werken.
- Je een album voorbereidt voor indiening of delen en elk nummer consistente metadata nodig heeft.
- Je wilt dat CarPlay, het vergrendelingsscherm, Apple Music-stijl spelers of DJ-software de juiste **E** / **C**-badge naast de tracktitel weergeven.

De waarde is opgeslagen in het standaard adviesbeoordelingsveld voor het bestandsformaat (`rtng` voor MP4, `TXXX:ITUNESADVISORY` voor ID3, `ITUNESADVISORY` voor Vorbis), zodat elke speler die ouderlijk advies-metadata leest je update ziet.

{{< cards cols="1">}}
  {{< card title="" subtitle="Adviesbeoordeling songteksten" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Albumhoes bewerken

Een albumhoes wijzigen:

1. Tik op het **Camerapictogram** in de artworkcarrousel.  
2. Kies de afbeeldingslocatie: Lokale bestanden, Cloud, Downloads of Fotobibliotheek.  
3. Selecteer een afbeelding om als omslagart toe te passen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Afbeelding selecteren" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Meer acties in de taggeditor

Extra bewerkingsopties zijn beschikbaar via de werkbalk onder de artworkweergave.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Meer acties" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Audiotags automatisch zoeken

Deze actie activeert de slimme tagzoekmotor, die volledige metadata voor je audiobestand vindt en invult op basis van de bestaande informatie.  
De app gebruikt de MusicBrainz-database — een van de meest uitgebreide tagdatabases — met meer dan **50 miljoen** nummers.

### Albumhoes zoeken

Gebruik metadata om het juiste albumartwork te zoeken op het web.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Albumhoes zoeken" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Sla de afbeelding op in je **Foto's** via het systeemcontextmenu als je het hebt gevonden.

{{< cards cols="1">}}
  {{< card title="" subtitle="Afbeelding toevoegen aan Foto's" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Ga daarna terug naar de taggeditor, tik op het camerapictogram, ga naar **Fotobibliotheek** en selecteer de opgeslagen afbeelding. De app stelt deze in als de hoes voor je audiobestand.

Je kunt aanpassen hoe omslagafbeeldingen worden geschaald in de app-instellingen.

### Albumartwork opslaan

Deze actie slaat het huidige albumartwork op in de map **Documenten**, zodat je het later opnieuw kunt gebruiken.

### Codering normaliseren

Deze actie normaliseert de tekstcodering van alle tags in de metadata van het audiobestand. Dit is vooral handig als je overschakelt van een Windows-pc, waar bestanden mogelijk andere coderingen gebruiken die op een Mac als onleesbare of verminkte tekens verschijnen.

### Handmatig zoeken naar tags

Zoek handmatig naar albummetadata met behulp van de MusicBrainz-database.  

- Selecteer het album  

{{< cards cols="1">}}
  {{< card title="" subtitle="Album selecteren" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Kies het juiste nummer  

{{< cards cols="1">}}
  {{< card title="" subtitle="Nummer selecteren" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Kies welke tags toe te passen  

{{< cards cols="1">}}
  {{< card title="" subtitle="Audiotags selecteren" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Tik op **Voltooid** om de geselecteerde metadata op je nummer toe te passen.

### Audiotags verwijderen

Wis alle metadatavelden voor een bestand. Handig bij het opnieuw beginnen. Tik op **Opslaan** ter bevestiging.

## Taggeditor-instellingen

Navigeer naar **Instellingen → Audio-taggeditor** om het gedrag aan te passen.

### Albumhoes schalen

Selecteer hoe albumhoezen worden geschaald wanneer ze worden opgeslagen in audiobestanden. Je kunt schalen uitschakelen om de originele afbeeldingsgrootte te behouden, maar wees ervan bewust dat sommige spelers mogelijk geen grote artworkbestanden ondersteunen. De optie "originele grootte" maakt deel uit van de Premium-personalisatiefuncties.

### Opties voor het opslaan van tags

- **ID3v2.4** — Wanneer ingeschakeld, slaat de app tags op in het ID3v2.4-formaat indien mogelijk. Schakel uit om terug te vallen op het breder ondersteunde ID3v2.3 als je audiotags niet correct worden weergegeven op oudere spelers of apparaten.
- **Dubbele tags** — Wanneer ingeschakeld worden veelgebruikte metadatavelden gedupliceerd in beide tagsecties van het bestand. Dit verbetert de compatibiliteit met oudere audiospelers, maar is in de meeste gevallen niet vereist.

### Opties voor het bijwerken van cloudbestand-metadata

Je kunt bepalen hoe de app metadata bijwerkt voor audiobestanden die zijn opgeslagen in cloudservices:

- **Bevestigingsbericht tonen**  
  Vraag voordat je metadatawijzigingen toepast op cloudbestanden.

- **Bestandsmetadata automatisch bijwerken**  
  Sla metadatawijzigingen automatisch op in het cloudbestand na het bewerken.

- **Bestandsmetadata niet bijwerken**  
  Sla het bijwerken van cloudbestanden over — wijzigingen worden alleen lokaal toegepast.

### Online bestanden bewerken

Kies wat er gebeurt met lokaal gedownloade kopieën van cloudbestanden na het bewerken:

- **Gedownload bestand altijd verwijderen**  
  Verwijder de lokale kopie na het opslaan van wijzigingen.

- **Gedownload bestand niet verwijderen**  
  Bewaar het gedownloade bestand op je apparaat na het bewerken.

### Knoppen op het hoofdscherm

Pas aan welke acties verschijnen op het hoofdscherm van de taggeditor (Automatisch audiotags zoeken, Handmatig audiotags zoeken, Albumafbeelding zoeken, Albumafbeelding opslaan, Codering normaliseren, Audiotags verwijderen). Je kunt ook **Uitgebreide tags weergeven** en **Bestanden tegelijkertijd bewerken** instellen zodat de editor altijd opent in je gewenste modus.
