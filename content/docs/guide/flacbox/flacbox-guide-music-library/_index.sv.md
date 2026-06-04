---
title: "Musikbibliotek"
date: 2020-02-01
description: "Lär dig hur du bygger, organiserar och synkroniserar ditt musikbibliotek i Flacbox på iPhone, iPad och Mac. Lägg till spår manuellt eller synkronisera från molntjänster, hantera metadata, albumomslag, spellistor, favoriter, senaste och bokmärken. Inkluderar stöd för hi-res-ljud, MusicBrainz-taggredigerare, online- och offlinesynkronisering samt personaliseringsalternativ."
keywords: [
  "Flacbox musikbibliotek", "synkronisera musik från molnet", "organisera musikmetadata",
  "redigera ljudtaggar Flacbox", "offline musiksynkronisering", "importera lokal musik",
  "Flacbox spellistehantering", "albumomslags sökning Flacbox",
  "iPhone musikmetadata", "Flacbox appguide",
  "Flacbox MusicBrainz", "Flacbox normalisera taggar",
  "Flacbox hi-res musikbibliotek", "Flacbox FFmpeg bibliotek",
  "Flacbox soloalbum", "Flacbox kompositörvy"
]
tags: ["musik", "guide", "flacbox", "bibliotek"]
readingTime: 11
---


Att hantera ditt musikbibliotek är enkelt med Flacbox, där du utan ansträngning kan organisera alla dina spår — lokala FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE och dussintals andra format — i en enda sökbar samling. Du har två alternativ för att bygga ditt musikbibliotek: manuellt tillägg (du väljer exakt vad som läggs till) eller automatisk synkronisering (Flacbox skannar utsedda molnmappar och lägger automatiskt till nya filer när de visas).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox musikbibliotek albumvy" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Manuellt tillägg

För att manuellt lägga till spår, tryck på ikonen **Lägg till musik** i det övre vänstra hörnet och välj mappar eller filer från en ansluten molnlagringstjänst eller filer på din enhet. När du lägger till spår i biblioteket skapas bara länkar till dessa spår — de faktiska filerna stannar kvar på sina ursprungliga platser för att spara värdefullt diskutrymme. Om du vill göra spår tillgängliga offline kan du använda åtgärden Ladda ner från alternativmenyn eller aktivera Offline-läge för spellistor och spårsamlingar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox lägg till låtar i musikbiblioteket" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Du kan också dra-och-släppa filer till biblioteket i Mac-versionen, eller använda **Öppna filer…** / **Öppna mapp…** från systemfilväljaren på iPhone och iPad.

## Fortsätt uppspelning

Återställ ljudspelarens kö från den senast sparade positionen om den här funktionen är aktiverad i appinställningarna. Aktivera både **Spara ljudspelartillstånd** och **Spara uppspelningsposition** i Inställningar → Ljudspelaren → Allmänt för bästa upplevelse. När det är aktiverat visas en knapp **Fortsätt uppspelning** längst upp i varje mapp, album, artist, genre och spellista — tryck på den för att hoppa direkt tillbaka till det exakta spåret och positionen du senast lämnade.

## Platser

Alla spår i ditt bibliotek är genomtänkt grupperade efter källtyp och musiktaggar. Du kan filtrera låtar efter plats med hjälp av knappen **Fler åtgärder** i det övre högra hörnet och välja **Filter**.

### Onlinemusik

Det här avsnittet visar musik från dina anslutna molnlagringstjänster. Spåren här strömmas vid behov; ingenting tar upp lokal lagring förrän du uttryckligen laddar ner eller aktiverar offline-läge.

### Filer i den här applikationen

Här kan du hitta musik tillgänglig för offline-uppspelning, hämtad från dina lokala filer. Det inkluderar filer i appens Documents-katalog — allt du laddat ner, överfört via Wi-Fi Drive eller importerat via Finder Fildelning.

### Filer på den här iPhone / iPad / Mac

Den här kategorin inkluderar musik importerad till applikationen från din enhet, tillagd via systemdialogen **Öppna filer…**. Originalfilerna stannar kvar på sin ursprungliga plats; Flacbox behåller bara en länk till dem.

## Kategorier

När du lägger till spår i ditt musikbibliotek läser appen automatiskt deras ljudtaggar och organiserar dem i kategorier som Låtar, Ospelat låtar, Album, Albumartister, Artister, Genrer och Kompositörer.

## Taggruppering

Dessa kategorier hjälper dig att organisera dina spår efter musiktaggar. När du lägger till spår i musikbiblioteket läser appen deras metadata och grupperar dem efter dessa kategorier. Om du inte ser alla dina album, se till att appen har skannat varje spår. Du kan kontrollera skanningsförloppet i Inställningar → Musikbibliotek → Metadataläsning → Antal bearbetade filer i musikbiblioteket. För lokala filer kan du också skanna om offlinemappar i Inställningar → Musikbibliotek → Synkronisering av offlinemappar → Starta skanning av lokala mappar. När metadataläsaren har slutfört alla åtgärder ser du följande kategorier i ditt musikbibliotek:

- **Låtar** — alla låtar grupperade efter taggen TRACK_TITLE. Du kan kontrollera sorteringsordningen med menyn Fler åtgärder i det övre högra hörnet.
- **Ospelade låtar** — alla låtar som aldrig har spelats upp.
- **Album** — låtar grupperade efter taggen ALBUM_NAME, ignorerar artist-, albumartist- och kompositörtaggar. Om du har flera album med samma namn men olika artister, överväg att använda sorteringen Exklusiva album som beskrivs nedan.
- **Albumartister** — låtar grupperade enbart efter ALBUM_ARTIST_TAG. Användbart för att hålla kompilationer och samarbeten tydligt separerade från soloarbete.
- **Artister** — låtar grupperade enbart efter ARTIST_TAG.
- **Genrer** — låtar grupperade efter taggen GENRE.
- **Kompositörer** — låtar grupperade efter taggen COMPOSER — ovärderligt för klassiska musikbibliotek där "kompositör" är den primära navigeringsaxeln.

## Favoriter

Du kan markera låtar som favoriter på ljudspelarskärmen eller via alternativmenyn. Favoriter visas i sin egen sektion så att du kan hitta dem med ett tryck.

## Senaste

Det här avsnittet visar alla nyligen spelade spår. Du kan anpassa hur många objekt listan Senaste håller i Inställningar → Bibliotek → Senaste → Ändra liststorlek, och exportera listan till M3U / CSV / TXT för att säkerhetskopiera din lyssningshistorik.

## Bokmärken

Du kan skapa ljudbokmärken medan en låt spelas upp och hantera dem på den här skärmen — perfekt för ljudböcker, långa mixar, föreläsningar eller bara markera refrängen på ett favoritspår. Detaljerade instruktioner om hur du arbetar med ljudbokmärken finns [här](/docs/guide/evermusic/evermusic-guide-music-library).

## Övre verktygsfält

Beläget precis under navigeringsfältet, erbjuder det övre verktygsfältet flera bekväma åtgärder: Sök, Spela alla, Blanda alla och Fortsätt uppspelning. Du kan visa eller dölja det här verktygsfältet med en enkel svep-ned-gest.

## Sök

Sökfunktionen ger dig möjlighet att hitta ett specifikt spår, artist, album eller genre i ditt musikbibliotek. På sökskärmen har du tillgång till åtgärderna Sortera, Filtrera och Rutnät / Listvy. Sökningen körs lokalt mot musikbiblioteksdatabasen, så den fungerar helt offline och returnerar resultat medan du skriver.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox musikbibliotekssökning" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Alternativmeny

Varje låt i ditt musikbibliotek har en meny med fler åtgärder, nåbar genom att trycka på tre-punktsknappen nära låttiteln. Dessa åtgärder varierar beroende på om det är en enstaka låt eller del av en samling.

### För enskilda låtar

- **Spela härnäst** — lägger till låten överst i spelarkön.
- **Spela senare** — lägger till låten längst ned i spelarkön.
- **Lägg till i spellista** — lägger till låten i en spellista.
- **Lägg till i favoriter** — markerar låten som en favorit för snabb åtkomst.
- **Ladda ner** — sparar låten till lokala filer. Den visas på fliken **Lokala filer** och i avsnittet **Offlinemusik**.
- **Redigera ljudtaggar** — öppnar den inbyggda ljudtaggredigeraren för att fixa saknad metadata; observera att detta ändrar låten på din lagring.
- **Visa i mapp** — avslöjar mappen där ljudfilen är lagrad.
- **Visa i Finder** — för filer importerade från din Mac avslöjar den här åtgärden mappen där ljudfilen finns på din Mac.
- **Öppna i** — exporterar ljudfilen till en annan app.
- **Ta bort från molntjänst** — tar bort filen från både musikbiblioteket och molnlagringen. **Den här åtgärden är oåterkallelig.**
- **Ta bort från musikbibliotek** — tar bort låten från ditt musikbibliotek, men filen finns kvar på lagringen. Om automatisk synkronisering är aktiverad och filen finns på fjärrlagring, visas den igen i ditt bibliotek efter en synkroniseringsåtgärd.

### För låtsamlingar

För låtsamlingar som Album, Artister, Genrer eller Kompositörer inkluderar alternativmenyn följande åtgärder.

- **Spela alla** — ersätter spelarkön med låtar från den valda samlingen.
- **Spela härnäst** — lägger till låtar från den här samlingen överst i spelarkön.
- **Spela senare** — lägger till låtar från den här samlingen längst ned i spelarkön.
- **Lägg till i spellista** — inkluderar låtar från den här samlingen i en spellista, med möjlighet att skapa en ny.
- **Aktivera offline-läge** — laddar ner låtar från den här samlingen till lokala filer. Filer visas på fliken **Lokala filer** och i avsnittet **Offlinemusik**. Om nya objekt läggs till i samlingen på servern laddas de automatiskt ner.
- **Redigera bild** — ändra albumomslaget för låtsamlingen.
- **Lägg till i arkiv** — packa hela samlingen i en enda ZIP-fil för enkel säkerhetskopiering eller överföring (premiumfunktion).
- **Exportera låtlista** — exportera samlingen till M3U, CSV eller TXT för användning i andra spelare eller för arkivering.
- **Ta bort från musikbibliotek** — tar bort låtsamlingen från ditt musikbibliotek. Den här åtgärden tar inte bort de faktiska filerna från lagringen. Om automatisk synkronisering är aktiverad och filerna finns på fjärrlagring, visas de igen i ditt bibliotek efter en synkroniseringsåtgärd.

## Markeringsläge

Du kan aktivera markeringsläge med hjälp av knappen Fler åtgärder i det övre högra hörnet. I det här läget kan du välja flera spår samtidigt och utföra batchåtgärder — lägg till i spellista, markera som favorit, ta bort från bibliotek, ladda ner och mer.

## Albumdetaljer

När du öppnar avsnitten Artist, Albumartist eller Kompositör kan du se en väljare för Låtar / Alla album / Exklusiva album / Soloalbum.

- **Låtar** — visar alla låtar där den här artisten / albumartisten / kompositören förekommer i ljudtaggarna.
- **Alla album** — visar kompilationsalbum och alla album där artisten förekommer överhuvudtaget.
- **Exklusiva album** — visar album där den angivna artisten är den enda artisten med det albumnamnet.
- **Soloalbum** — visar album där bara den angivna artistens spår förekommer, även om andra artister har album med samma namn.

Det här är särskilt användbart för att städa upp röriga "Various Artists"-kompilationer i stora bibliotek.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox albumdetaljskärm" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Inställningar

Tryck på Fler åtgärder → Inställningar för att konfigurera dina musikbiblioteksinställningar.

### Metadataläsning

När du lägger till spår i biblioteket sätter metadataläsaren igång. Den här bakgrundsprocessen läser all metadata från dina spår och organiserar dem efter Artist, Album, Genre och Kompositör. Du kan justera hastigheten för metadataläsning för att ladda data snabbare — observera att snabbare läsning använder mer energi. Du kan också inaktivera metadataläsaren helt och visa filnamn i stället för tagginformation.

Det är viktigt att notera att metadataläsaren bara uppdaterar metadata i ditt musikbibliotek och inte ändrar filerna lagrade i ditt molnkonto eller lokal lagring. Om du vill redigera metadata för ljudfiler kan du göra det med den inbyggda taggredigeraren, som du kan aktivera från motsvarande åtgärd i alternativmenyn.

### Tillgängliga lägen för metadataläsaren

- **Inaktiverad** — metadataläsaren är av och filnamn visas i stället för ljudtaggsdata.
- **Aktuell låt** — applikationen läser metadata enbart för den låt som spelas för tillfället. Använd det här alternativet om du har en långsam nätverksanslutning för att förhindra att metadataläsaren skickar många förfrågningar till molnservern, vilket kan orsaka uppspelningsavbrott.
- **Uppspelningskö** — appen läser metadata för alla låtar i ljudspelarens kö.
- **Bibliotek** — appen läser metadata för alla låtar i musikbiblioteket.

När reglaget **Metadataläsning i bakgrunden** är på fortsätter metadataläsaren att arbeta i bakgrundsläge. Observera att om appen förbrukar mycket energi under ljuduppspelning kan iOS-operativsystemet avbryta den.

Så om du har en stor musiksamling är det lämpligt att använda skrivbordsversionen av applikationen för metadatasynkronisering. Du kan sedan använda funktionen Säkerhetskopiering och återställning i appinställningarna för att överföra det synkroniserade biblioteket från skrivbordet till mobilen.

När alternativet **Normalisera metadatakodning** är aktiverat normaliserar appen automatiskt metadatakodningen för alla låtar i musikbiblioteket. Det åtgärdar problem där ljudtaggskodningen är trasig (till exempel efter redigering av filer på en Windows-PC) och förhindrar att felaktiga tecken visas i spårinformation.

Åtgärden **Ladda om metadata** flaggar varje fil i ditt musikbibliotek som att metadata saknas, vilket utlöser metadataläsaren att uppdatera varje post.

Tryck på **Starta metadataläsning** för att utlösa läsaren manuellt. Åtgärdsförloppet visas nedan.

### Onlinesynkronisering

Automatisk onlinemusiksync låter dig lägga till spår från anslutna molntjänster i musikbiblioteket automatiskt. För att aktivera den här funktionen, gå till inställningarna för musikbibliotek och välj synkroniseringsmappar.

Med det här alternativet aktiverat skannar applikationen alla valda mappar, identifierar stödda ljudfiler och integrerar dem sömlöst i ditt bibliotek. Du kan starta eller stoppa synkronisering genom att trycka på motsvarande menyåtgärd.

Onlinemusiksync körs exklusivt när appen är i förgrunden, vilket innebär att synkronisering av ett stort bibliotek kan ta lite tid. För att påskynda processen, lämna appen öppen, anslut den till en strömkälla och aktivera Skärm → Alltid aktiv i appinställningarna.

Alternativt kan du utföra onlinemusiksync på skrivbordsversionen av appen och överföra musikbiblioteket till iOS-versionen med funktionen Säkerhetskopiering och återställning.

Du kan också ange hur ofta du vill synkronisera ditt onlinemusiksbibliotek. Om du ställer in intervallet till Omedelbart startar onlinesync varje gång du öppnar applikationen.

### Offlinesynkronisering

Här kan du konfigurera offlinemusiksync.

#### Synkroniserade offlinemappar

När du gör en molnmapp tillgänglig offline (via menyn Fler åtgärder) visas den i avsnittet Lokala filer → Offlinemappar. Appen laddar ner dess innehåll till din enhet. Om du gör ändringar i mappen i molnet — som att lägga till, ta bort eller uppdatera filer — upptäcker appen dessa ändringar och uppdaterar den lokala kopian automatiskt.

På den här skärmen kan du manuellt starta offlinemappssynkronisering, visa offlinemappen i dess överordnade mapp och inaktivera offline-läge för mappen. Inaktivering av offline-läge tar bort alla lokala kopior av filer från din enhet.

#### Tidsintervall

Du kan ange tidsintervallet för hur ofta appen ska kontrollera offlinemappar efter ändringar.

#### Starta skanning av lokala mappar

Det här alternativet skannar alla lokala mappar som finns i applikationens Documents-katalog för att hitta stödda ljudfiler. Alla dessa lokala filer läggs sömlöst till i ditt musikbibliotek. Lokala filer på din enhet men utanför den här applikationen måste läggas till i musikbiblioteket manuellt, eftersom appen inte har åtkomst till filer utanför applikationens Documents-katalog på grund av iOS / macOS säkerhetsbegränsningar.

#### Viktigt

Det är lämpligt att regelbundet initiera offlinemusiksync för att hålla ditt musikbibliotek uppdaterat med dina lokala filer.

### Personalisering

I det här avsnittet kan du konfigurera musikbiblioteksskärmstilen efter dina preferenser. Tre alternativ är tillgängliga: Vanlig meny, Grupperad meny, Flikad meny. Du kan också aktivera eller inaktivera visning av albumomslag på albumdetaljskärmar.

### Albumomslag

Här kan du konfigurera hur applikationen laddar och lagrar albumkonstverk.

- **Nätverkstyp** — välj Wi-Fi eller Wi-Fi och mobildatanät för omslagnedladdningar.
- **Ladda albumomslag för onlinefiler** — när det är aktiverat laddas inbyggda albumomslag för filer lagrade i molnlagring. Det kan använda ytterligare nätverksdata.
- **Sök i mappen** — när det är aktiverat, om ett spår saknar inbyggt omslag, letar appen efter JPEG- eller PNG-bilder i samma mapp och använder dem som albumkonstverk.
- **Omslagskvalitet** — välj kvaliteten på albumomslag lagrade på din enhet.
- **Visa i mapp** — öppna mappen där albumomslag är cachade så att du kan hantera eller säkerhetskopiera dem.
- **Ta bort alla** — ta bort cachade albumomslag för att frigöra lagringsutrymme och tvinga appen att ladda om dem vid behov.

Som standard kontrollerar appen efter inbyggda albumomslag i dina spår och visar dem om tillgängliga. Om det inte finns några inbyggda albumomslag och alternativet **Sök i mappen** är aktiverat, kontrollerar appen den omslutande mappen efter JPEG- eller PNG-bilder och använder dem som albumkonstverk för alla spår i den mappen.

### Spellistor

Du kan aktivera alternativet att lägga till samma låt i en spellista två gånger. Som standard är det här alternativet inaktiverat.

### Senaste

Du kan hantera din lista med nyligen spelade låtar.

- **Ta bort lista** — ta bort hela listan med nyligen spelade låtar.
- **Ändra liststorlek** — ange antalet objekt som visas i listan.
- **Exportera låtlista** — exportera din lista med nyligen spelade låtar till M3U, CSV eller TXT. Detaljerade instruktioner finns [här](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoriter

Du kan hantera listan med dina favoritlåtar.

- **Samtidig redigering** — när det är aktiverat lägger till en låt till favoriter både i musikbiblioteket och filsektionen på en gång.
- **Ta bort lista** — ta bort hela listan med favoritlåtar.
- **Exportera låtlista** — liknar Senaste, exportera favoritlistan till M3U, CSV eller TXT.

### Ta bort bibliotek

Den här åtgärden raderar musikbiblioteksdatabasen, men lämnar dina musikfiler orörda på lagringen.

### Gräns för innehållsladdning

Som standard använder applikationen sidnumrering för att minska innehållsladdningstiden och hålla stora bibliotek responsiva. Du kan dock inaktivera det här alternativet och låta applikationen ladda all tillgänglig data på en gång. För att göra det, öppna appinställningarna, rulla ned till Personalisering → Gräns för innehållsladdning och välj Inaktiverad.
