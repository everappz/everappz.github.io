---
title: "Spellistor"
date: 2020-02-01
description: "Lär dig hur du skapar, importerar, hanterar och anpassar spellistor i Flacbox på iPhone, iPad och Mac. Bygg spellistor från moln- och lokala filer, importera M3U / M3U8 / CUE, ändra ordning på låtar, redigera omslagskonst, arkivera till ZIP, exportera till M3U / CSV / TXT och använd offline-läge."
keywords: [
  "Flacbox spellistor", "importera M3U spellista", "spellistehanterare",
  "skapa spellista iPhone", "ljudspellistor Flacbox",
  "anpassad spellistebild", "ta bort låtar från spellista",
  "sortera spellista Flacbox", "VoiceOver spellista ändra ordning",
  "Flacbox M3U export", "Flacbox CSV export", "Flacbox spellistearkiv",
  "Flacbox spellista offline-läge", "Flacbox CUE import", "Flacbox dubbla låtar"
]
tags: ["guide", "flacbox", "spellistor"]
readingTime: 7
---


I avsnittet Spellistor hittar du användbara verktyg för att hantera dina musiksamlingar. Det här området visar alla dina spellistor på ett ställe. Längst upp finns en knapp **"..."** i navigeringsfältet som öppnar en meny med olika spellistealternativ, plus ett verktygsfält med snabbåtgärder som Sök, Spela alla och Blanda alla. Varje spellista har också sin egen knapp **"..."** bredvid titeln, vilket ger dig fler alternativ just för den spellistan.

Spellistor i Flacbox kan innehålla en blandning av onlinemolnspår, nedladdade offlinefiler och lokala filer från din enhet — allt i en spellista — och spelas sömlöst tillsammans.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox spellistors huvudskärm" image="/docs/guide/flacbox/img/playlists-main.webp" >}}
{{< /cards >}}

## Skapa en spellista

Att skapa en ny spellista är enkelt. Du har två alternativ: tryck på knappen **+**, eller tryck på knappen **"..."** i det övre högra hörnet av navigeringsfältet och välj Ny spellista. Ge din spellista ett meningsfullt namn och tryck sedan på Spara.

Det utlöser dialogrutan Lägg till låtar, där du kan handplocka de spår du vill inkludera i din nya spellista. Spår är bekvämt kategoriserade efter källtyp:

- **Bibliotek** — spår som redan finns i ditt musikbibliotek.
- **Filer i den här applikationen** — ljudfiler i appens Documents-mapp (nedladdade från molnlagring, importerade via Wi-Fi Drive eller tillagda via Finder Fildelning).
- **Filer på den här enheten** — ljudfiler på andra platser på din enhet, inte i den här applikationen.
- **Anslutningar** — onlinefiler som finns i dina anslutna molnlagringstjänster.

Som standard kan du lägga till ett enstaka spår i en spellista bara en gång. Om du vill tillåta dubbletter, aktivera den här funktionen i Inställningar → Musikbibliotek → Spellistor → Dubbletter i en spellista → Aktivera.

## Importera spellista

I Flacbox har vi lagt till import av M3U / M3U8 / CUE-filer så att du inte behöver återskapa spellistor manuellt efter att ha bytt från en annan spelare.

Gå först till avsnittet Spellistor. Tryck sedan på Fler-knappen i det övre högra hörnet. Välj Importera spellista från menyn.

På nästa skärm väljer du filplatsen. Stödda alternativ inkluderar:

- Ansluten molnlagring
- Filer i applikationen
- Filer på din enhet

Välj ansluten molnlagring och öppna mappen som innehåller spellistefilen. Stödda spellistfilsändelser inkluderar M3U, M3U8 och CUE. Välj spellistefilen och tryck på Färdig för att bekräfta ditt val.

Appen tolkar spellistefilen, skapar en lista med spår och lokaliserar dessa filer på lagringen för att sammanställa en slutlig spellista, som sedan importeras till musikbiblioteket. Viktigt: M3U / CUE-filen måste innehålla korrekta sökvägar till mediefilerna, och filerna måste faktiskt finnas på dessa sökvägar på din lagring. Läs mer om spellisteimport [här](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Spellistedetaljskärm

När du öppnar en spellista visas spellistedetaljskärmen. Du hittar en knapp **"..."** i det övre högra hörnet med spellistealternativ, och tre knappar under omslaget: Sök, Fortsätt uppspelning, Spela alla och Blanda alla. Det finns också en kryssruta för Offline-läge för att aktivera full spellistasynkronisering offline.

- **Fortsätt uppspelning** — återställ den senast sparade uppspelningspositionen för den här spellistan.
- **Sök** — utför en sökning i den aktuella spellistan.
- **Spela alla** — lägg till alla spår från den aktuella spellistan i spelarkön.
- **Blanda alla** — som **Spela alla**, men blandar spåren innan de läggs till i ljudspelarens kö.
- **Offline-läge** — ladda ner alla spår från den här spellistan till lokala filer. Alla nya objekt som läggs till i spellistan laddas också automatiskt ner.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox spellistedetaljskärm" image="/docs/guide/flacbox/img/playlist-details-screen.webp" >}}
{{< /cards >}}

## Fler åtgärder för en spellista på spellisteskärmen

Du kan komma åt åtgärder för en spellista genom att trycka på knappen **"..."** bredvid spellistetiteln. Tillgängliga åtgärder:

- **Spela alla** — lägger till spellistans spår i en ny spelarkö.
- **Spela härnäst** — lägger till spellistans spår överst i den befintliga spelarkön.
- **Spela senare** — lägger till spellistans spår längst ned i den befintliga spelarkön.
- **Redigera bild** — ändra spellistans omslagskonst.
- **Aktivera offline-läge** — aktivera offline-läge för spellistan. Både befintliga och nya spår laddas automatiskt ner. Läs mer om offline-läge [här](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Exportera låtlista** — exportera den här spellistan till **M3U / M3U8 / CSV / TXT** som beskrivs [här](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Lägg till i arkiv** — arkivera den här spellistan (inklusive m3u-fil, albumomslag och alla spår) i en enda ZIP som beskrivs [här](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to). Premiumfunktion.
- **Lägg till låtar** — lägg till fler låtar i den aktuella spellistan.
- **Byt namn** — byt namn på spellistan.
- **Ta bort spellista** — ta bort spellistan från musikbiblioteket. **Den här åtgärden kan inte ångras.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox fler åtgärder för en spellista på spellistornas huvudskärm" image="/docs/guide/flacbox/img/more-actions-for-playlist-in-playlists-main-screen.webp" >}}
{{< /cards >}}

## Fler åtgärder för en spellista på spellistedetaljskärmen

Du kan komma åt åtgärder för en spellista genom att trycka på knappen **"..."** i det övre högra hörnet. Tillgängliga åtgärder:

- **Välja** — aktivera spårmarkeringsläge, användbart för att ta bort flera spår från spellistan eller ändra deras ordning.
- **Spela härnäst** — lägg till spellistans spår överst i den befintliga spelarkön.
- **Spela senare** — lägg till spellistans spår längst ned i den befintliga spelarkön.
- **Lägg till låtar** — lägg till nya låtar i spellistan.
- **Ändra ordning på låtar** — ändra manuellt ordningen på låtar i spellistan med dra-och-släpp.
- **Byt namn** — byt namn på den aktuella spellistan.
- **Redigera bild** — ändra albumomslaget för den aktuella spellistan.
- **Exportera låtlista** — exportera den här spellistan till **M3U / M3U8 / CSV / TXT**. Läs mer [här](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Lägg till i arkiv** — ZIP den aktuella spellistan inklusive alla spår och m3u-fil. Läs mer [här](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Sortera** — ändra ordningen på spår i spellistan. Sorteringsalternativ inkluderar **Låttitel, Låtnummer, Album, Artist, Albumartist, Genre, Kompositör, Betyg, År, Slag per minut, Längd, Filnamn, Filmodifieringsdatum, Filskapelsedatum** och **Manuell**. Alternativet **Manuell** sortering möjliggör manuell omordning av låtar med dra-och-släpp.
- **Sök** — sök efter en specifik låt i den aktuella spellistan.
- **Rutnät / Lista** — ändra skärmlayoutpresentationen.
- **Ta bort spellista** — ta bort spellistan från musikbiblioteket. Den här åtgärden tar inte bort spår från din lagring, men **den kan inte ångras**.

## Ändra låtordning i en spellista

För att ändra ordningen på låtar i en spellista, tryck på knappen **"..."** i det övre högra hörnet och välj **Välja** för att gå in i markeringsläge. Använd ordningskontrollerna och dra-och-släpp-gester nära varje spår för att flytta dem uppåt eller nedåt. Att trycka på ordningskontrollen flyttar spåret till toppen av listan. För att avsluta markeringsläget och tillämpa ändringar, tryck på **Färdig**.

För ett ännu enklare arbetsflöde på långa spellistor, välj Fler åtgärder → Ändra ordning på låtar för att gå in i dedikerat dra-och-släpp-ordningsläge.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox ändra ordning på låtar i en spellista" image="/docs/guide/flacbox/img/playlist-details-rearange-songs.webp" >}}
{{< /cards >}}

## Ändra spellistans omslagsbild

För att ändra omslagsbilden för en spellista, tryck på knappen **"..."** i det övre högra hörnet och välj **Redigera bild**. Välj en bild från de tillgängliga källorna (Foton, Filer, molnlagring eller ett genererat konstverk från ett spår i spellistan), bekräfta sedan genom att trycka på **Färdig**.

## Lägga till låtar i en spellista

Öppna spellistan och tryck på knappen **"..."** i det övre högra hörnet, välj sedan **Lägg till låtar** för att öppna en dialog. Välj de spår du vill lägga till och bekräfta genom att trycka på **Färdig**.

## Ta bort flera låtar från en spellista

Öppna spellistan, tryck på knappen **"..."** i det övre högra hörnet och välj **Välja** för att gå in i markeringsläge. Välj de spår du vill ta bort och tryck på **Ta bort från spellista** längst ned på skärmen. Bekräfta genom att trycka på **Färdig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox markeringsläge i spellistedetaljskärmen" image="/docs/guide/flacbox/img/selection-mode-playlist-details-screen.webp" >}}
{{< /cards >}}

## Spåralternativ

Varje spår i en spellista har en lista med åtgärder, nåbara genom att trycka på knappen **"..."**. Om du inte kan se alla åtgärder, rulla ned för att visa dem. Du kan ta bort spåret från spellistan, ladda ner det, redigera ljudtaggar och mer.

- **Spela härnäst** — lägger till spåret överst i spelarkön.
- **Spela senare** — lägger till spåret längst ned i spelarkön.
- **Lägg till i en spellista** — lägger till spåret i en annan spellista.
- **Lägg till i favoriter** — markerar spåret som en favorit för snabb åtkomst.
- **Ladda ner** — gör spåret tillgängligt offline. Det visas i överföringskön och fliken **Lokala filer** i avsnittet **Nedladdad musik** i musikbiblioteket.
- **Redigera ljudtaggar** — öppnar den inbyggda taggredigeraren för att ändra spårmetadata.
- **Öppna i** — exporterar spåret och öppnar det i en annan app.
- **Visa i mapp** — avslöjar mappen där ljudfilen finns.
- **Visa i Finder** — för filer importerade från din Mac avslöjar detta mappen där ljudfilen finns på din Mac.
- **Ta bort från spellista** — tar bort spåret från spellistan.
- **Ta bort från molntjänst** — tar bort spåret från spellistan och den tillhörande molntjänsten. **Den här åtgärden kan inte ångras.**
- **Ta bort från musikbibliotek** — tar bort spåret från musikbiblioteket och lämnar filen på lagringen orörd.

## Tillgänglighet

Flacbox är fullt tillgängligt med **VoiceOver**-teknologi, vilket säkerställer att varje komponent har en väldesignad etikett och beskrivning. När VoiceOver är aktivt översätter appen användargränssnittet till **Textläge**, visar bara tillgängliga och användbara element för att förbättra navigeringshastigheten och bekvämligheten. Du kan också aktivera Textläge i Inställningar → Tillgänglighet → Textläge.

### Justera spårposition i en spellista med VoiceOver

1. Öppna en spellista och tryck på knappen **Fler**.
2. Välj **Ändra låtordning**. Vyn växlar till redigeringsläge.
3. Tryck på ikonen för ordningsomkoppling nära spårtiteln för att ge den fokus.
4. **Dubbeltryck** snabbt på ikonen för ordningsomkoppling. Vid det andra trycket, släpp inte fingret — håll det tills du hör ett ljud som indikerar att cellen är redo att flyttas.
5. Nu kan du flytta cellen till en ny position.

Andra komponenter fungerar som förväntat och använder systemets VoiceOver-mönster.
