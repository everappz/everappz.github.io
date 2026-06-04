---
title: "Inställningar"
date: 2020-01-01
description: "Utforska alla inställningar i Evermusic inklusive ljudkonfiguration, synkronisering av musikbibliotek, offlinemappar, metadata, personalisering, tillgänglighet, widgets, CarPlay och säkerhetskopieringsalternativ."
keywords: [
  "Evermusic", "inställningar", "ljudinställningar", "synkronisering av musikbibliotek",
  "offlinemappar", "equalizer", "crossfade", "gapless uppspelning",
  "ljudprocessor", "spelliste-inställningar", "premiumuppgradering",
  "återställ köp", "filhanterare", "taggredigerare", "WiFi-enhet",
  "voiceover", "app-säkerhetskopiering", "tillgänglighet", "lokalisering",
  "widgets", "CarPlay", "rumsligt ljud", "ljudtonhöjd"
]
tags: ["evermusic", "guide", "settings"]
readingTime: 16
---


Inställningsskärmen är Evermusics kontrollcentral. Härifrån kan du uppgradera till Premium, konfigurera ljudspelaren, hantera ditt musikbibliotek, konfigurera filhanteraren, anpassa gränssnittet, aktivera widgets och CarPlay, säkerhetskopiera dina data och komma åt hjälp och juridisk information. Avsnitt är grupperade under rubrikerna: **Köp och uppdateringar**, appreferenser, **Hjälp** och **Juridiskt och sekretess**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Inställningsskärm" image="/docs/guide/evermusic/evermusic-guide-settings/img/settings-main-screen.webp" >}}
{{< /cards >}}

## Köp och Uppdateringar

### Uppgradera till Premium

Uppgradera applikationen till Premium-versionen för att ta bort alla begränsningar. Gratisversionen erbjuder ett livstids köp i appen och två prenumerationsalternativ som låser upp hela funktionsuppsättningen.

Family Sharing är aktiverat för alla köp och planer, så du kan dela Premium-versionen med familjemedlemmar.

Du kan läsa mer om köp och Premium-versionen här: [Vad är skillnaden mellan Evermusic och Evermusic Premium](/docs/faq/evermusic/what-is-the-difference-between-evermusic-and-evermusic-premium/).

#### Evermusic Free (blå ikon) vs Evermusic Pro (röd ikon)

Evermusic publiceras på App Store under två olika ikoner/färger:

- **Evermusic Free (blå ikon)** är uppdelat i **två separata App Store-appar med olika bundle-ID** — en för **iOS / iPadOS** och en dedikerad för **macOS** (Universell binärfil som körs på både **Apple Silicon och Intel Mac**). Premium-köp i appen **delas mellan iOS och Mac blå appar via iCloud** — köp Premium på iPhone och det aktiveras automatiskt på Mac (och vice versa), så länge båda enheterna använder samma Apple ID med iCloud aktiverat.
- **Evermusic Pro (röd ikon)** är en **enda App Store-app** med ett **enda bundle-ID** som körs på **iPhone, iPad och Apple Silicon Mac (M1 och senare)**. Den har **samma funktionalitet som Evermusic Free med en aktiverad Premium-plan**. Den röda appen **stödjer inte Intel Mac**, varför dess pris är något lägre än det motsvarande premiumköpet i den blå appen. Evermusic Pro **samlar inte in någon användardiagnostik eller analys alls** — analys är helt inaktiverat i bygget, utan opt-in-alternativ.

Eftersom bundle-ID skiljer sig mellan blå och röd låser ett Premium-köp i appen aktiverat i den blå appen inte upp den röda appen gratis, och vice versa. Om du redan använder den blå appen med Premium aktiverat finns det inget behov av att installera den röda appen — du har redan allt Pro erbjuder.

### Dela Köp Mellan iOS och Mac

Livstids köp och prenumerationer delas mellan iOS och Mac med iCloud. Om du redan äger Premium på iOS, se till att du har den senaste versionen installerad och att iCloud är aktiverat. Starta appen på iOS och vänta en minut för att din köpinformation ska laddas upp till iCloud.

Du kan också trycka på **Återställ köp** i appinställningarna. Installera sedan den senaste appversionen från App Store på din Mac och starta appen. Se till att du har en internetanslutning och är inloggad med samma iCloud och App Store-konto på båda enheterna. Vänta en minut för att appen ska ladda ned köpinformation från iCloud. Premium-versionen bör aktiveras automatiskt på din Mac.

### Återställa Köp på en Ny Enhet

För att återställa ditt köp på en ny enhet, använd **Köp → Återställ köp**. Du kommer att se listan över dina köp. Om något saknas, kontrollera att enheten är ansluten till samma iTunes-konto som användes för att göra köpen och att iCloud är aktiverat.

### Prova Premium Gratis

Du kan uppgradera till Premium-versionen gratis under en begränsad tid via den här menyn. Se en kort annons eller dela appen med vänner för att tillfälligt låsa upp Premium.

### Köp

Återställ tidigare köp från den här menyn. Om du stöter på aktiveringsfel, prova att aktivera alternativet **Återställ köp vid appstart**.

### Programuppdatering

Tryck på **Programuppdatering** för att kontrollera om en nyare version av Evermusic är tillgänglig. Appen jämför din installerade version med den senaste versionen på App Store och meddelar dig om en uppdatering rekommenderas.

### Nyheter

Den här menyn blir tillgänglig efter att en ny version släpps. Den visar en sammanfattning av ändringar och nya funktioner som ingår i den senaste uppdateringen.

## Inställningar för Ljudspelaren

Alla inställningar för ljudspelaren är grupperade här: equalizer, crossfade-uppspelning, ljudspelarcache, låtladdning och mer. Inställningar är organiserade i logiska underavsnitt.

### Allmänt

Det här underavsnittet innehåller allmänna uppspelningskö-, ljudutgångs- och statussparingsinställningar.

#### Upprepningsläge

Anger ljudspelarens beteende när ett spår avslutar uppspelning:

- **Upprepa alla** – loopar alla spår i din spelarkö.
- **Upprepa en** – upprepar bara det aktuella spåret.
- **Stopp upprepning** – pausar uppspelning när det aktuella spåret slutar.
- **Upprepa inte** – låter din kö spela igenom utan att upprepa.

#### Blandningsläge

Spelar spåren i en randomiserad ordning. Detta blandar faktiskt kön och spelar spår ett efter ett i den nya ordningen. Tillgängliga värden: **Blandning av** och **Blandning på**.

#### Ljudprocessor

Möjliga värden: **AVFoundation** och **CoreAudio**. Som standard används AVFoundation. På grund av ett känt problem med AVFoundation på iOS 17.0–17.6 kan crossfade-uppspelning och ljud-equalizern inte användas samtidigt. För att använda båda på dessa iOS-versioner, byt till CoreAudio-ljudprocessorn.

Om du upplever problem med gapless-uppspelning med AVFoundation, prova CoreAudio också. De enda begränsningarna med CoreAudio är internetströmning av vissa radiostationer och vissa ljudformat, eftersom det inte stödjer varje systemljudformat (som M4A och några andra).

#### Sampelfrekvens för Ljudutgång

Ställ in sampelfrekvensen för ljudutgången från 8 KHz till 384 KHz. Det här alternativet är bara tillgängligt när CoreAudio-processorn är vald.

#### Antal Kanaler för Ljudutgång

Ställ in antalet kanaler för ljudutgången — **MONO** eller **STEREO**. Det här alternativet är bara tillgängligt när CoreAudio-processorn är vald.

#### Ljudtonhöjdsalgoritm

Välj algoritmen som används för tonhöjdskorrigering. Tillgängliga värden är **Tidsdomänen**, **Spektral** och **Varispeed**. Användbart om du justerar uppspelningshastigheten och vill kontrollera den resulterande ljudkvaliteten.

#### Rumsligt Ljud

Rumsligt ljud använder psykoakustiska metoder för att skapa en mer uppslukande ljudupplevelse på stödda hörlurar och högtalaranordningar. Möjliga värden: **Inaktiverad**, **Mono och Stereo**, **Flerkanalig**, **Mono Stereo Flerkanalig**.

#### Ljudutgångsläge

Bara tillgängligt på iOS. Låter dig aktivera blandat läge så att ljud från den här applikationen blandas med andra applikationer. Du kan hitta instruktioner om hur du använder blandat läge [här](/docs/howto/how-to-record-video-while-playing-music-on-iphone).

#### Spara Uppspelningsposition

Säkerställer att applikationen sparar och återställer uppspelningspositionen för låtar i ditt musikbibliotek.

#### Spara Ljudspelartillstånd

Sparar ljudspelartillståndet innan applikationen stängs, vilket gör det enkelt att återuppta från där du slutade.

När båda dessa funktioner är aktiverade, öppna valfri mapp, album, artist eller genre. Du kommer att se en **Fortsätt uppspelning**-åtgärd längst upp på skärmen, tillsammans med den senast sparade låten och uppspelningspositionen. Tryck på **Fortsätt uppspelning** för att återuppta. Tryck bara på den filen för att återuppta uppspelning för en enskild fil.

### Personalisering

Anpassa utseendet på ljudspelarskärmen, välj vilka kontroller som är synliga på spelaren, låsskärmen och statusfältet, och konfigurera hoppa-tid-knapparna.

#### Stil för Ljudspelarskärm

Konfigurera placeringen av verktygsfält och huvudkontroller på ljudspelaren.

#### Albumomslagets Rullningsstil

Välj rullningsstilen för albumomslag på ljudspelarskärmen.

#### Ytterligare Element

Aktivera extra element på ljudspelarskärmen. **Ljudformatinfo** visar det nu spelande spårets tekniska info ovanför omslagsbilden; **Ljudvolymskjutreglage** visar ljudutgångsskjutreglaget under uppspelningskontrollerna.

#### Åtgärder på Huvudskärmen

Konfigurera vilka knappar som är synliga på ljudspelarens huvudskärm. Tillgängliga alternativ inkluderar Upprepa och Blanda-läge, Nästa och föregående låt, Hoppa tid, Sömnstimer, Google Chromecast, AirPlay och Bluetooth, Ljud-Equalizer, Sök, Bokmärken, Hastighet, Lägg till bokmärke, Lägg till i favoriter, Kommentarer och mer.

#### Uppspelningskontroller på Låsskärmen

Välj vilka extra kontroller som är aktiverade på låsskärmen. Möjliga värden: **Hoppa tid**, **Lägg till bokmärke** och **Lägg till i favoriter**.

#### Hoppa tid-intervall

Välj tidsintervallerna som används av knapparna Hoppa tid framåt och bakåt.

### Filladdning

Välj nätverkstypen som används för att strömma låtar. Tillgängliga alternativ: **Wi-Fi** och **Wi-Fi och Mobildata**.

#### Förinläsningstid

Ställ in bufferttidsintervallet. Öka det här värdet om du har en dålig nätverksanslutning.

#### Använd Direkt URL

När aktiverat används en direkt URL för att ladda låten om servern stödjer det. Detta kan snabba upp låtladdning men kan lätt påverka uppspelningsstabilitet.

#### Optimera Filladdning

När aktiverat optimerar systemet låtladdning för AVFoundation-ljudprocessorn, vilket kan förbättra uppspelningsstabilitet. Appen använder tekniken beskriven [här](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/).

### Ljud-Equalizer

Konfigurera ljud-equalizern. Du kan läsa mer om förinställningar och EQ-konfigurationer [här](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Enheter

Anslut till en AirPlay eller Google Chromecast-enhet (bara iOS).

### Uppspelningshastighet

Justera uppspelningshastigheten för ljudspelaren. För mer exakt kontroll, aktivera det exakta skjutreglaget genom att trycka på konfigurationsikonen i det övre högra hörnet.

### Crossfade-Uppspelning

Crossfade låter låtar flöda sömlöst i en kontinuerlig mix — nästa låt börjar spela några sekunder innan den nuvarande är klar. Crossfade är inte tillgängligt för AirPlay och Google Chromecast. På den här skärmen väljer du hur länge den nuvarande och nästa låt spelar samtidigt. Om du upplever problem med crossfade och ljud-equalizern samtidigt, byt ljudprocessorn som beskrivs ovan.

### Gapless-Uppspelning

Gapless-uppspelning säkerställer att låtar spelar utan avbrott eller tystnad däremellan. Det är perfekt för klassisk musik, liveinspelningar och konceptalbum. Om du har problem med gapless-uppspelning, byt ljudprocessorn som beskrivs ovan.

### Uppspelningscache

Låtar i ljudspelarköen laddas ned automatiskt för smidig uppspelning. Om du laddar ned ljudfiler manuellt kan du inaktivera det här alternativet för att undvika dubbletter. Du kan också konfigurera storleken på ljudspelarcachen här. Läs mer om offlineläge och uppspelningscache här: [Spela Offlinemusik i Evermusic & Flacbox: Ladda ned och Synkronisera från Molnet till Lokala Filer](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Sömnstimer

Aktivera en timer för att stoppa uppspelning efter en angiven timeout. För mer exakt kontroll, aktivera precist läge genom att trycka på konfigurationsikonen i det övre högra hörnet.

## Bibliotek

Musikbiblioteksinställningar — automatisk synkronisering, metadataläsning, albumomslags-laddning, spellistor, senaste och favoriter — finns här.

### Metadataläsning

När du lägger till spår i biblioteket bearbetar metadataläsaren dem i bakgrunden och organiserar dem efter Artist, Album, Genre och Kompositör. Du kan justera hur snabbt metadata läses för att ladda data snabbare (på bekostnad av mer batteri). Du kan också inaktivera metadataläsaren helt och visa filnamn istället för tagginformation.

Metadataläsaren uppdaterar bara musikbiblioteksdatabasen; den ändrar inte filer lagrade i ditt molnkonto eller lokal lagring. Om du behöver redigera metadata för ljudfiler, använd den inbyggda taggredigeraren via motsvarande åtgärd i alternativmenyn.

När **Metadataläsning i bakgrunden** är på fortsätter läsaren att arbeta i bakgrundsläge. Om appen använder för mycket energi under uppspelning kan iOS pausa den.

Om du har en stor musiksamling, rekommenderas det att utföra metadatasynkronisering på skrivbordsversionen av applikationen. Du kan sedan överföra det synkroniserade musikbiblioteket till iOS med funktionen **Säkerhetskopiering och Återställning**.

När **Normalisera Metadatakodning** är aktiverat normaliserar appen automatiskt kodningen av metadata för alla låtar. Detta åtgärdar problem där audio-tagkodning är trasig (t.ex. efter redigering av filer på en Windows-dator) och förhindrar att felaktiga tecken visas i spårinformation.

**Ladda om metadata** markerar varje fil i ditt musikbibliotek som saknad metadata, vilket gör att metadataläsaren uppdaterar varje post.

**Starta Metadataläsning** startar metadataläsaren manuellt. Förlopp visas nedan åtgärden.

### Online-Synkronisering

Automatisk online musiksynkronisering lägger till spår från anslutna molntjänster i musikbiblioteket automatiskt. För att aktivera det, öppna musikbiblioteksinställningarna och välj synkroniseringsmappar.

Med det här alternativet aktiverat genomsöker applikationen de valda mapparna, identifierar stödda ljudfiler och lägger till dem i ditt bibliotek. Starta eller stoppa synkronisering med motsvarande menyåtgärd.

Online-synkronisering körs bara när appen är i förgrunden, så synkronisering av ett stort bibliotek kan ta lite tid. För att påskynda saker, håll appen öppen, anslut till en strömkälla och aktivera **Skärm → Alltid aktiv** i inställningarna.

Alternativt, utför online-synkronisering på skrivbordsversionen av appen och överför musikbiblioteket till iOS med **Säkerhetskopiering och Återställning**.

Du kan också välja hur ofta online-synkronisering körs. Att ställa in intervallet till **Omedelbart** utlöser en synkronisering varje gång du öppnar applikationen.

### Offline-Synkronisering

Konfigurera offline musiksynkronisering.

#### Synkroniserade Offlinemappar

När du markerar en onlinemapp på din molnserver som tillgänglig offline (med menyn Fler åtgärder), visas den här. Mappinnehållet laddas ned till **Lokala filer → Offlinemappar**. När onlinemappen ändras (filer läggs till, tas bort eller uppdateras) kontrollerar appen för ändringar och uppdaterar den lokala kopian på din enhet.

På den här skärmen kan du manuellt starta offlinemappsynkronisering, avslöja offlinemappen i dess innehållsmapp och inaktivera offlineläge för mappen. Att inaktivera offlineläge tar bort alla lokala kopior av filer från din enhet.

#### Tidsintervall

Välj hur ofta appen kontrollerar offlinemappar för ändringar.

#### Starta Lokal Mappskanning

Skanna alla lokala mappar i applikationens dokumentkatalog för stödda ljudfiler. Hittade filer läggs automatiskt till i musikbiblioteket. Filer på din enhet men utanför applikationens dokumentkatalog måste läggas till i musikbiblioteket manuellt, eftersom appen inte kan komma åt dem på grund av iOS/macOS-säkerhetsbegränsningar.

**Viktigt:** Det rekommenderas att regelbundet starta offline musiksynkronisering för att hålla ditt musikbibliotek uppdaterat med dina lokala filer.

### Personalisering

Konfigurera musikbiblioteksskärmstiln. Tre alternativ finns tillgängliga: **Enkel meny**, **Grupperad meny** och **Flikmeny**. Du kan också aktivera eller inaktivera albumomslag på albumdetalj-skärmen.

### Albumomslag

Välj hur applikationen laddar och lagrar albumomslag.

- **Nätverkstyp** — välj **Wi-Fi** eller **Wi-Fi och Mobildata** för omslags-nedladdningar.
- **Ladda albumomslag för online-filer** — när aktiverat laddas inbäddade albumomslag för filer lagrade i molnlagring. Detta kan använda ytterligare nätverksdata.
- **Sök i mappen** — när aktiverat, om ett spår inte har ett inbäddat omslag, letar appen efter JPEG- eller PNG-bilder i samma mapp och använder dem som albumomslag.
- **Omslagskvalitet** — välj kvaliteten på albumomslag lagrade på din enhet.
- **Visa i mapp** — öppna mappen där albumomslag cachas så att du kan hantera eller säkerhetskopiera dem.
- **Ta bort alla** — ta bort cachade albumomslag för att frigöra lagring och tvinga appen att ladda om dem på begäran.

### Spellistor

Aktivera alternativet att lägga till samma låt i en spellista två gånger. Som standard är det här alternativet inaktiverat.

### Senaste

Hantera din lista med nyligen spelade låtar.

- **Ta bort lista** — ta bort hela listan med nyligen spelade låtar.
- **Ändra liststorlek** — ange antalet objekt som visas i listan.
- **Exportera låtlista** — exportera din lista med nyligen spelade låtar som M3U, CSV eller TXT. Detaljerade instruktioner finns tillgängliga [här](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoriter

Hantera listan över dina favoritlåtar.

- **Simultan Redigering** — när aktiverat lägger tillägg av en låt till favoriter till den i musikbiblioteket och filsektionen samtidigt.
- **Ta bort lista** — ta bort hela listan med favoritlåtar.
- **Exportera låtlista** — som Senaste, exportera favoriter som M3U, CSV eller TXT.

### Ta bort Musikbibliotek

Radera musikbiblioteksdatabasen. Dina musikfiler på lagring lämnas orörda.

## Lösenkod

Aktiverar lösenordsskyddsskärmen om du vill skydda din applikationsdata.

## Filhanterare

Filhanteraravsnittet styr hur filer överförs, lagras och förhandsgranskas.

### Filöverföringar

Välj dina nätverkspreferenser för att ladda ned filer till din enhet.

### Maximalt Antal Parallella Uppgifter

Ange antalet parallella nedladdningstrådar. Ett högre antal snabbar upp nedladdningar men kräver mer batteri.

### Filöverföringsuppgifter

Visar för närvarande aktiva uppladdnings- och nedladdningsuppgifter.

### Bakgrundsöverföringar

Tillåt nedladdningar medan appen är i bakgrunden. Om bakgrundsöverföringar förbrukar mycket energi kan iOS pausa appen.

### Spara Nedladdade Filer Till

Välj standardnedladdningskatalogen, eller låt appen fråga dig varje gång.

### Synkroniserade Offlinemappar

Hantera offline-synkronisering för valda mappar. För att aktivera offline-synkronisering, tryck på tre-punkter-knappen bredvid en mapp och välj **Tillgängligt Offlineläge**. Nya filer läggs till i molnmappen laddas ned till din enhet automatiskt. Läs mer om offlinelägen [här](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Tidsintervall

Välj hur ofta offlinemappar synkroniseras. **Omedelbart** utlöser en synkronisering varje gång du öppnar appen.

### Visa Fullständiga Filnamn

Visa fullständiga filnamn, inklusive tillägg, i filhanteraren.

### Redigera Online-Filer

Inaktivera online-filredigering för att byta till skrivskyddat läge för anslutna molntjänster och förhindra oavsiktliga borttagningar. Den här åtgärden tar bort filredigeringsoperationer från användargränssnittet.

### Kopiera Filer Vid Öppning

Ange hur appen hanterar importerade filer från andra applikationer.

### Miniatyrer för Filer

Hantera och ta bort genererade filminiatyrer för att frigöra lagringsutrymme.

### Ta bort Temporära Filer

Rensa applikationens cachemapp för att återvinna lagringsutrymme.

## Ljud-Taggredigerare

Konfigurera den inbyggda ljud-taggredigeraren.

### Albumomslags-Skalning

Välj skalningsmetoden som används när ett albumomslag sparas i ljudtaggar.

### Uppdatera Online-Filer

När aktiverat uppdaterar applikationen automatiskt en fils metadata på molnservern efter att du är klar med att redigera den.

### Ta bort Fil Efter Online-Redigering

Välj om applikationen ska ta bort den nedladdade kopian efter att ha avslutat redigeringen av en online-fil på en molnserver.

### Knappar på Huvudskärmen

Välj vilka knappar som är synliga på huvudskärmen för ljud-taggredigeraren.

## Widgets

Aktivera widgets så att appen uppdaterar widgetdata under uppspelning. Widgetuppdateringar kräver ytterligare energi, så aktivera detta bara om du faktiskt använder widgets på din hemskärm eller låsskärm.

Du kan läsa mer om Evermusic-widgets i [Navigeringsguiden](/docs/guide/evermusic/evermusic-guide-navigation/).

## CarPlay

Ändra CarPlay-inställningar här. Den här menyn är också tillgänglig inuti CarPlay-gränssnittet så att du kan justera upplevelsen under körning.

### Sortera

Konfigurera sorteringsalternativ för alla CarPlay-skärmar.

### Innehållsladdningsgräns

Välj om appen använder paginering på CarPlay-skärmen. Paginering håller menyer responsiva på enheter med begränsat minne och stora bibliotek.

### Gradient Färg för Menyikoner

Välj färgschemat för CarPlay-hemskärmen.

### Visa Bilder

Inaktivera bilder på CarPlay-skärmen för att optimera laddningshastighet och minska minnesanvändning på stora bibliotek.

### Pausa Uppspelning Vid Anslutning

Aktivera detta för att undvika plötsligt högt ljud när du ansluter din enhet till CarPlay.

## Wi-Fi-Enhet

Aktivera Wi-Fi-Enheten för att överföra filer från en dator till din enhet med en stationär webbläsare. Detaljerade instruktioner om hur du använder Wi-Fi-Enheten finns tillgängliga [här](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalisering

Anpassa användargränssnittet efter dina preferenser.

### Applikationsikon

Välj en alternativ applikationsikon för din hemskärm.

### Färgschema

Välj användargränssnittstema och aktivera mörkt läge. När **Standard** är valt följer applikationen enhetens övergripande utseendeinställningar.

### Bakgrundsstil

Ändra bakgrundsstilen för applikationen. För närvarande är det enda alternativet **Suddigt albumomslag**, som använder det nu spelande spårets omslag som ett suddigt appbakgrundsbild.

### Utseende på Objekt i Listan

Justera hur objekt visas i listor. Användbart på liten skärmar — du kan låta appen justera radhöjden automatiskt baserat på innehåll, eller visa mindre ikoner i listceller för att ge text mer utrymme.

### Innehållsladdningsgräns

Som standard använder applikationen paginering för att påskynda innehållsladdning. Du kan inaktivera paginering för att ladda allt på en gång.

### Stil för Lokala Filer-Skärm

Ändra presentationsstilen för avsnittet **Lokala filer**.

### Stil för Musikbiblioteksskärm

Anpassa utseendet på skärmen **Musikbibliotek**.

### Stil för Ljudspelarskärm

Konfigurera utseendet på skärmen **Ljudspelaren**.

### Snabbmenystil

Välj stilen på snabbmenyn som visas när du trycker på knappen Fler åtgärder.

## Fönster

Tillgängligt på Mac och Catalyst. Konfigurera fönsterrelaterade preferenser som standardstorlek och beteende vid start.

## Skärm

Välj om skärmen ska förbli aktiv medan du använder applikationen. Användbart vid skanning av stora bibliotek eller utförande av långvarigt taggredigeringsarbete.

## Tillgänglighet

Aktivera **Textläge** för att dölja alla bilder i användargränssnittet. Textläge aktiveras automatiskt när VoiceOver är aktiv och är också användbart för mycket liten eller textbaserade inställningar.

## Språk

Ändra applikationsspråket och åsidosätt systemstandarden. Appen stödjer för närvarande följande lokaliseringar: Afrikaans, Akan, Albanska, Amhariska, Arabiska, Armeniska, Assamesiska, Aymara, Azerbajdzjanska, Bambara, Bengali, Baskiska, Vitryska, Bosniska, Bulgariska, Burmesiska, Katalanska, Cebuano, Förenklad kinesiska, Traditionell kinesiska, Korsikanska, Kroatiska, Tjeckiska, Danska, Dhivehi, Dogri, Holländska, Engelska, Esperanto, Estniska, Ewe, Filippinska, Finska, Franska, Galiciska, Ganda, Georgiska, Tyska, Grekiska, Guaraní, Gujarati, Haitiansk kreolska, Hausa, Hawaiiska, Hebreiska, Hindi, Hmong, Ungerska, Isländska, Igbo, Iloko, Indonesiska, Irländska, Italienska, Japanska, Javanesiska, Kannada, Kazakiska, Khmer, Kinyarwanda, Koreanska, Krio, Kurdiska, Kurdisk Sorani, Kirgiziska, Lao, Latin, Lettiska, Lingala, Litauiska, Luxemburgska, Makedonska, Maithili, Malagassiska, Malajiska, Malayalam, Maltesiska, Māori, Marathi, Mizo, Mongoliska, Nepali, Norra Sotho, Norsk Bokmål, Nyanja, Odia, Oromo, Pashto, Persiska, Polska, Portugisiska, Punjabi, Rumänska, Ryska, Samoanska, Sanskrit, Skotsk gaeliska, Serbiska, Shona, Sindhi, Singalesiska, Slovakiska, Slovenska, Somaliska, Södra Sotho, Spanska, Sundanesiska, Swahili, Svenska, Tadzjikiska, Tamil, Tatariska, Telugu, Thailändska, Tsonga, Turkiska, Turkmenska, Ukrainska, Urdu, Uyghuriska, Uzbekiska, Vietnamesiska, Walesiska, Xhosa, Jiddisch, Yoruba, Zulu.

## Säkerhetskopiering och Återställning

Säkerhetskopiera all din applikationsdata eller migrera den till en annan enhet. Du kan välja vad som ska inkluderas:

- **Databas** — alla dina musikbiblioteksspår och spellistor. Offline-spår ingår inte för att hålla säkerhetskopieringsstorleken hanterbar.
- **Albumomslag** — alla dina cachade albumomslag.
- **Inställningar** — alla dina applikationsinställningar.

Tryck på **Säkerhetskopiera Applikationsdata** för att starta säkerhetskopieringsoperationen. Applikationsdata skrivs till en enda fil som du kan använda senare för att återställa applikationstillståndet på en ny enhet eller efter ominstallation av appen.

För att återställa applikationsdata på en ny enhet, flytta säkerhetskopieringsfilen till den nya enheten med en ansluten molntjänst eller iCloud och öppna den på den nya enheten.

Vi har en detaljerad steg-för-steg-guide här: [Hur du Överför ditt Musikbibliotek Mellan Enheter i Evermusic: Steg-för-Steg-Guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Hjälp

Öppna applikationsguiden för hjälp och vägledning om hur du använder appen effektivt.

## Vanliga Frågor

Hitta svar på vanliga frågor i FAQ-avsnittet.

## Skicka Feedback

Har du feedback eller behöver du hjälp? Skicka din feedback till vårt supportteam direkt från appen.

## Dela Den Här Appen

Dela applikationen med dina vänner för att hjälpa till att sprida ordet.

## Upptäck Fler Appar

Utforska andra appar från Everappz.

## Villkor och Bestämmelser

Beskriver villkoren för att använda applikationen. Läs det innan du använder applikationen.

## Integritetspolicy

Besök sidan för integritetspolicy för att förstå våra datahanteringspraxis. Läs det innan du använder applikationen.

## Analys och Datainsamling

Kontrollera vilka tjänster som är aktiverade för analys och datainsamling och inaktivera de du inte vill ha.

I **Evermusic Free (blå ikon)** är analys och diagnostik aktiverade som standard för att hjälpa oss förbättra appen — du kan stänga av dem här när som helst. **Evermusic Pro (röd ikon) inkluderar inte någon analys eller diagnostik alls** — avsnittet är tomt (eller dolt) eftersom ingenting samlas in, och det finns inget opt-in-alternativ.

## Juridiska Meddelanden

Innehåller information om varje bibliotek som används i applikationen tillsammans med appversionsnumret och bygginformationen.
