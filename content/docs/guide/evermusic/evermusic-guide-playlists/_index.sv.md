---
title: "Spellistor"
date: 2020-01-01
description: "Lär dig skapa, importera, anpassa och hantera spellistor i Evermusic. Innehåller detaljerade steg för redigering, sortering, offlineläge och tillgänglighet."
keywords: [
  "Evermusic", "spellistor", "spelliste-hantering", "importera M3U-spellista",
  "redigera spellista", "offline spellista", "ändra spelliste-ordning", "spellisteomslagsbilder",
  "spelliste-tillgänglighet", "ljudspelare"
]
tags: ["evermusic", "guide", "playlists"]
readingTime: 6
---


## Översikt

Sektionen Spellistor ger dig verktyg för att organisera dina spår i listor. Det inkluderar en innehållsvy som visar alla dina skapade spellistor, en "..."-knapp i navigeringsfältet som erbjuder olika spellistarelaterade åtgärder, och ett navigeringsverktygsfält med "Sök", "Spela alla" och "Blanda alla"-knappar. Dessutom har varje enskild spellista en "..."-knapp nära spellistetiteln, med ett antal åtgärder specifika för just den spellistan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Spellisteskärm" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-main.webp" >}}
{{< /cards >}}

## Skapa en Spellista

Skapa en ny spellista genom att antingen trycka på "+"-knappen eller "..."-knappen i det övre högra hörnet av navigeringsfältet, välj "Ny spellista" och ge din spellista ett namn. Tryck på "Spara" efter att du har namngett den.

{{< cards cols="1">}}
  {{< card title="" subtitle="Skapa en ny spellista" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-add-new.webp" >}}
{{< /cards >}}

Det öppnar dialogrutan "Lägg till låtar", där du kan välja vilka spår som ska läggas till i den nya spellistan. Spår kategoriseras efter källtyp och du har flera alternativ:

- **Bibliotek**: Spår från ditt musikbibliotek.
- **Filer i den här applikationen**: Ljudfiler lagrade i appens dokumentkatalog.
- **Filer på den här iPhone/iPad/Mac**: Ljudfiler på andra mappar på din enhet, utanför appen.
- **Anslutningar**: Online-filer lagrade i anslutna molnlagringstjänster.

Som standard kan du bara lägga till ett spår i en spellista en gång. För att tillåta duplicerade låtar i en spellista, aktivera den här funktionen i appinställningarna - Musikbibliotek - Spellistor - Dubbletter i en spellista - Aktivera.

## Importera Spellista

I Evermusic har vi lagt till M3U-filimportfunktionalitet, så att du inte behöver skapa spellistor manuellt.

{{< cards cols="1">}}
  {{< card title="" subtitle="Importera spellista från en filkälla" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-import-from-files.webp" >}}
{{< /cards >}}

Gå först till avsnittet 'Spellistor'. Tryck sedan på 'Mer'-knappen i det övre högra hörnet. Välj alternativet 'Importera spellista' från menyn som visas.

På nästa skärm väljer du filplatsen. Stödda alternativ inkluderar:

- Ansluten molnlagring
- Filer i applikationen
- Filer på din enhet

Låt oss välja ansluten molnlagring och öppna mappen som innehåller spellistefilen. Stödda spellistfilsändelser inkluderar M3U, M3U8 och CUE. Välj spellistefilen och tryck på 'Klar' för att bekräfta ditt val.

Appen tolkar spellistefilen, skapar en lista med spår och hittar de filerna på lagringen för att sammanställa en slutgiltig spellista, som importeras till musikbiblioteket. Det är avgörande att din M3U/CUE-fil innehåller korrekta sökvägar för mediefiler och att filerna finns på dessa sökvägar på din lagring. Du kan läsa mer om spelliste-import [här](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Spellistas Detaljskärm

När du öppnar en spellista visas "Spellistans detaljskärm". På den här skärmen hittar du en "..."-knapp i det övre högra hörnet med spelliste-alternativ och tre knappar under omslagsbilden: "Sök", "Fortsätt uppspelning", "Spela alla" och "Blanda alla". Dessutom finns en kryssruta för "Offlineläge".

{{< cards cols="1">}}
  {{< card title="" subtitle="Spellistans detaljskärm" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-detail-screen.webp" >}}
{{< /cards >}}

- **Fortsätt uppspelning**: Återställ uppspelningsposition för den här spellistan.
- **Sök**: Utför en sökning i den aktuella spellistan.
- **Spela alla**: Lägg till alla spår från den aktuella spellistan i spelarköen.
- **Blanda alla**: Liknar "Spela alla", men blandar spåren innan de läggs till i ljudspelarköen.
- **Offlineläge**: Ladda ned alla spår från den här spellistan till lokala filer. Alla nya objekt som läggs till i spellistan laddas ned automatiskt.

## Fler åtgärder för Spellista på Spellisteskärmen

Du kan komma åt åtgärder för en spellista genom att trycka på "..."-knappen nära spellistetiteln. Här är de tillgängliga åtgärderna:

- **Spela alla:** Lägger till spellistespår i den nya spelarköen.
- **Spela nästa:** Lägger till spellistespår överst i den befintliga spelarköen.
- **Spela senare:** Lägger till spellistespår längst ner i den befintliga spelarköen.
- **Redigera bild:** Redigera spellistans omslagsbild.
- **Aktivera offlineläge:** Aktiverar offlineläge för spellistan. I det här scenariot laddas både befintliga och nya spår ned automatiskt. Läs mer om offlineläge [här](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Exportera låtlista:** Du kan exportera den här spellistan till olika format som beskrivs [här](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Lägg till i arkiv:** Du kan arkivera den här spellistan inklusive m3u-fil, albumomslag och alla spår som beskrivs [här](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Lägg till låtar:** Lägg till fler låtar i den aktuella spellistan.
- **Byt namn:** Byt namn på spellistan.
- **Ta bort spellista:** Ta bort spellistan från Musikbiblioteket. Observera att den här åtgärden inte kan ångras.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menyn Fler åtgärder för en spellista" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-more-actions-for-separate-playlist.webp" >}}
{{< /cards >}}

## Fler åtgärder för Spellista på Spellistas Detaljskärm

Du kan komma åt åtgärder för en spellista genom att trycka på "..."-knappen i det övre högra hörnet. Här är de tillgängliga åtgärderna:

- **Välj:** Aktiverar spårvalsläge, användbart för att ta bort flera spår från spellistan eller ändra deras ordning.
- **Spela nästa:** Lägger till spellistespår överst i den befintliga spelarköen.
- **Spela senare:** Lägger till spellistespår längst ner i den befintliga spelarköen.
- **Lägg till låtar:** Lägg till nya låtar i spellistan.
- **Ordna om låtar:** Ändra manuellt ordningen på låtar i spellistan med dra-och-släpp.
- **Byt namn:** Byt namn på den aktuella spellistan.
- **Redigera bild:** Redigera albumomslagsbilden för den aktuella spellistan.
- **Exportera låtlista:** Exportera den här spellistan till olika format. Du kan läsa mer [här](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Lägg till i arkiv:** Zippa aktuell spellista inklusive alla spår och m3u-fil. Du kan läsa mer [här](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Sortera:** Ändra ordningen på spår i spellistan. Sorteringsalternativ inkluderar "Låttitel", "Låtnummer", "Album", "Artist", "Albumartist", "Genre", "Kompositör", "Betyg", "År", "Slag per minut", "Varaktighet", "Filnamn", "Filmodifieringsdatum", "Filskapandedatum" och "Manuell". Alternativet "Manuell" sortering gör det möjligt att manuellt ordna om låtar med dra-och-släpp.
- **Sök:** Sök efter ett specifikt spår i den aktuella spellistan.
- **Rutnät/Lista:** Ändra skärmens layoutpresentation.
- **Ta bort spellista:** Ta bort spellistan från Musikbiblioteket. Viktigt: den här åtgärden tar inte bort spår från din lagring och kan inte ångras.

## Ändra Låtordning i en Spellista

För att ändra ordningen på låtar i en spellista, tryck på "..."-knappen i det övre högra hörnet och välj "Välj" för att gå in i valläge. Använd ordningskontrollen och dra-och-släpp-gester nära varje spår för att flytta dem upp eller ned. Om du trycker på ordningskontrollen flyttas spåret högst upp i listan. Tryck på "Klar" för att avsluta valläget och tillämpa ändringarna.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ändra låtordning i en spellista" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-change-songs-order.webp" >}}
{{< /cards >}}

## Ändra Spellistans Omslagsbild

För att ändra omslagsbilden för en spellista, tryck på "..."-knappen i det övre högra hörnet och välj "Redigera bild". Välj en bild från de tillgängliga källorna och bekräfta ändringarna genom att trycka på "Klar".

## Lägga till Låtar i en Spellista

Öppna spellistan och tryck på "..."-knappen i det övre högra hörnet, välj sedan "Lägg till låtar" för att öppna en dialog. Välj de spår du vill lägga till och bekräfta ändringarna genom att trycka på "Klar".

## Ta bort Flera Låtar från en Spellista

Öppna spellistan, tryck på "..."-knappen i det övre högra hörnet och välj "Välj" för att gå in i valläge. Välj de spår du vill ta bort och tryck på knappen "Ta bort från spellista" längst ner på skärmen. Bekräfta ändringarna genom att trycka på "Klar".

{{< cards cols="1">}}
  {{< card title="" subtitle="Valläge inuti en spellista" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-selection-mode-in-playlist-details-screen.webp" >}}
{{< /cards >}}

## Spåralternativ

Varje spår i en spellista har en lista med åtgärder, åtkomlig genom att trycka på "..."-knappen. Om du inte kan se alla åtgärder rullar du ned för att se dem. Du kan ta bort spåret från spellistan, ladda ned det, redigera ljudtaggar och mer.

{{< cards cols="1">}}
  {{< card title="" subtitle="Spåralternativsmeny i en spellista" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-track-options.webp" >}}
{{< /cards >}}

- **Spela nästa:** Lägger till spåret överst i spelarköen.
- **Spela senare:** Lägger till spåret längst ner i spelarköen.
- **Lägg till i en spellista:** Lägger till spåret i en spellista.
- **Lägg till i favoriter:** Markerar spåret som en favorit för snabb åtkomst.
- **Ladda ner:** Gör spåret tillgängligt offline. Det visas i överföringskön och på fliken "Lokala filer" i avsnittet "Nedladdad musik" i Musikbiblioteket.
- **Redigera ljudtaggar:** Öppnar den inbyggda taggredigeraren för att ändra spårmetadata.
- **Öppna i:** Exporterar spåret och öppnar det i en annan app.
- **Visa i mapp:** Visar mappen där ljudfilen finns.
- **Visa i Finder:** För filer importerade från din Mac visar den här åtgärden mappen där ljudfilen finns på din Mac-dator.
- **Ta bort från spellista:** Tar bort spåret från spellistan.
- **Ta bort från molntjänst:** Tar bort spåret från spellistan och tillhörande molntjänst. Observera att den här åtgärden inte kan ångras.
- **Ta bort från musikbibliotek:** Tar bort spåret från musikbiblioteket och lämnar filen på lagring orörd.

## Tillgänglighet

Vår app är fullt tillgänglig med VoiceOver-teknologi, vilket säkerställer att varje komponent har en väldesignad etikett och beskrivning. När VoiceOver är aktivt översätter appen användargränssnittet till textläge och visar bara tillgängliga och användbara element för att förbättra navigeringshastighet och bekvämlighet. Du kan också aktivera textläge i Inställningar > Tillgänglighet > Textläge.

För att justera spårposition i en spellista med VoiceOver:

1. Öppna en spellista och tryck på knappen "Mer".
2. Välj "Ändra låtordning." Vyn byter till redigeringsläge.
3. Tryck på sorteringsindikatorikonen nära låttiteln för att ge den fokus.
4. Dubbeltryck snabbt på sorteringsindikatorikonen. Vid det andra trycket, släpp inte fingret — håll det tills du hör ett ljud som indikerar att cellen är redo att flyttas.
5. Nu kan du flytta cellen till en ny position.

Övriga komponenter fungerar som förväntat med hjälp av systemets VoiceOver-mönster.
