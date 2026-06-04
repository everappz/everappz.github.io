---
title: "Inställningar"
date: 2020-02-01
description: "Utforska varje inställning i Flacbox — från uppspelningsinställningar, FFmpeg / systemljudmotorn, Hi-Res-ljudutgång, equalizerjusteringar, tonhöjdskorrigering, IO-buffertduration, metadatasynkronisering, spellistekontroll, filöverföringar, hemskärmswidgetar, Apple CarPlay, UI-personalisering, språk, lösenkod, säkerhetskopiering och återställning samt premiumuppgradering."
keywords: [
  "Flacbox inställningar", "ljudspelarkonfiguration", "premiumuppgradering Flacbox",
  "WiFi Drive", "metadatasynkronisering", "equalizer", "uppspelningshastighet",
  "spellista dubbletter", "filhanterarinställningar", "offline musiksynkronisering",
  "ljudtaggsredigerare", "mörkt läge", "återställ köp", "säkerhetskopieringsinställningar",
  "Flacbox widgetinställningar", "Flacbox CarPlay-inställningar",
  "Flacbox FFmpeg-inställningar", "Flacbox samplingsfrekvens inställningar",
  "Flacbox tonhöjdskorrigering inställningar", "Flacbox IO-buffert",
  "Flacbox lösenkod", "Flacbox språk", "Flacbox personalisering",
  "Flacbox analys"
]
tags: ["guide", "flacbox", "inställningar"]
readingTime: 16
---


Inställningsskärmen är kontrollcentret för Flacbox. Härifrån kan du uppgradera till Premium, konfigurera ljudmotorn (systemkodekar eller FFmpeg), hantera ditt musikbibliotek, konfigurera filhanteraren, anpassa ljudtaggsredigeraren, aktivera hemskärmswidgetar och Apple CarPlay, säkerhetskopiera dina data och komma åt hjälp och juridisk information. Avsnitt är grupperade under rubriker: Köp och uppdateringar, Appinställningar, Hjälp samt Juridik och integritet.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox inställningarnas huvudskärm" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Uppgradera till Premium

Uppgradera applikationen till premiumversionen för att ta bort alla begränsningar. Gratisversionen av applikationen erbjuder ett engångsköp för livstid och två prenumerationsalternativ (1 månad och 1 år) för att ta bort alla begränsningar och uppgradera till Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox uppgradera till Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Family Sharing** är aktiverat för alla köp och planer, så du kan dela premiumversionen med upp till fem familjemedlemmar utan extra kostnad.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox välj en premiumplan" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Du kan läsa mer om köp och premiumversionen här: [Vad är skillnaden mellan Flacbox och Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Dela köp mellan iOS och Mac

Livstidsköp och prenumerationer delas mellan iOS och Mac med iCloud för att synkronisera den här informationen. Om du har premiumversionen på din iOS-enhet, se till att du har den senaste versionen installerad och att iCloud är aktiverat. Starta appen på iOS och vänta en minut tills din köpinformation har laddats upp till iCloud.

Du kan också trycka på knappen Återställ köp i appinställningarna. Installera sedan den senaste appversionen från App Store på din Mac och starta appen. Se till att du har en internetanslutning och använder samma iCloud- och App Store-konto på Mac som du använde på iOS. Vänta en minut tills appen har laddat ner köpinfo från iCloud — premiumversionen bör aktiveras på din Mac automatiskt.

## Återställ köp på en ny enhet

För att återställa ditt köp på en ny enhet, använd menyn Köp → Återställ köp. Du ser listan med dina köp. Om du inte ser alla, bekräfta att enheten är ansluten till samma Apple ID som användes för att göra köpen, och se till att iCloud är aktiverat.

## Prova Premium gratis

Du kan uppgradera till premiumversionen gratis, under en begränsad tid, med den här menyn. Titta bara på en annons eller berätta för dina vänner om appen för att få Premium gratis.

## Köp

Du kan återställa tidigare köp från den här menyn. Om du stöter på aktiveringsfel, prova att aktivera alternativet Återställ köp vid appstart.

## Programuppdatering

Tryck på Programuppdatering för att kontrollera om en nyare version av Flacbox är tillgänglig. Appen jämför din installerade version med den senaste versionen på App Store och meddelar dig om en uppdatering rekommenderas.

## Nyheter

Den här menyn är tillgänglig efter att en ny version har släppts. Den visar en sammanfattning av ändringarna och nya funktioner i den senaste uppdateringen.

## Ljudspelaren

Det här avsnittet konfigurerar ljudspelaren och den underliggande ljudmotorn, inklusive valet av FFmpeg / systemkodek och Hi-Res-ljudutgångsalternativ.

### Allmänt

Dessa inställningar täcker de grundläggande aspekterna av ljudspelaren — uppspelningskö, ljudutgång och sparandet av spelarens tillstånd.

- **Upprepningsläge** — välj hur ljudspelaren beter sig när ett spår är klart:
  - **Upprepa alla** — spelar om alla spår i din kö.
  - **Upprepa en** — upprepar bara det aktuella spåret.
  - **Upprepa stopp** — pausar uppspelning när det aktuella spåret är slut.
  - **Upprepa ingen** — låter kön spela igenom utan att upprepa.
- **Blandningsläge** — randomisera ordningen på spår i din kö. Du kan stänga av **Blandning** eller slå på **Blandning**.
- **Ljudkodek** — välj den ljudmotor som används för uppspelning:
  - **Systemkodek + FFmpeg** — prioriterar systemets ljudkodek där det är möjligt, vilket förbättrar kompatibilitet och stabilitet. Tonhöjdskorrigering och samplingsfrekvens för ljudutgång kan vara begränsade.
  - **FFmpeg** — tvingar FFmpeg-kodeken för alla ljudfiler och låser upp tonhöjdskorrigering och samplingsfrekvens för ljudutgång.
- **Samplingsfrekvens för ljudutgång** — justera samplingsfrekvensen för ljudutgången för att optimera ljudkvaliteten, särskilt användbart med en extern DAC. Tillgängliga värden: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** och **96 kHz**.
- **Antal kanaler för ljudutgång** — för flerkanals ljudsystem med en extern DAC, ange antal kanaler: Mono, Stereo, Center / Vänster / Höger, Center / Vänster / Höger / Surround, ITU BS.775-1, 5.1 Surround och SDDS.
- **Önskad IO-buffertduration för ljudutgång** — konfigurera in- / utbuffertdurationen. Ett typiskt värde för att minimera latens vid uppspelning av högupplöst ljud är runt **5 millisekunder (0,005 sekunder)**. Testa olika durationer på din målenhet för att hitta bästa balansen mellan låg latens och störningsfri uppspelning.
- **Ljudutgångsläge (endast iOS)** — konfigurera blandat ljudutgångsläge så att ljud från Flacbox blandas med andra applikationer. Detaljerade instruktioner finns [här](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Spara uppspelningsposition** — sparar och återställer uppspelningspositionen för låtar i ditt musikbibliotek.
- **Spara ljudspelartillstånd** — bevarar ljudspelarens tillstånd innan du stänger appen, vilket gör det enkelt att återuppta från där du slutade.

När du har aktiverat både **Spara uppspelningsposition** och **Spara ljudspelartillstånd**, öppna valfri mapp, album, artist eller genre och du ser en knapp **Fortsätt uppspelning** längst upp på skärmen.

### Personalisering

Personalisering låter dig anpassa utseendet på ljudspelarskärmen, ändra tillgängliga kontroller på huvudskärmen, låsskärmen och statusfältet, och konfigurera hoppa-tid-kontroller.

- **Stil för ljudspelarskärmen** — konfigurera placeringen av element på ljudspelarskärmen.
- **Rullningsstil för albumomslag** — konfigurera den föredragna rullningsstilen för albumomslag.
- **Ytterligare element** — aktivera extra element på ljudspelarskärmen. Ljudformatinfo visar det nu spelande spårets ljudinfo ovanför omslaget; Ljudvolymreglage visar reglaget för ljudutgång under uppspelningskontrollerna.
- **Åtgärder på huvudskärmen** — konfigurera vilka knappar som ska synas på den primära ljudspelarskärmen som standard: Upprepnings- och blandningsläge, Nästa och föregående låt, Hoppa tid, Sovtimer, Google Chromecast, AirPlay och Bluetooth, Audioequalizer, Sök, Bokmärken, Hastighet, Lägg till bokmärke, Lägg till i favoriter, Kommentarer och mer.
- **Uppspelningskontroller på låsskärmen** — välj vilka kontroller som visas på låsskärmen. Möjliga värden: Hoppa tid, Lägg till bokmärke, Lägg till i favoriter.
- **Hoppa-tid-knappar** — välj tidsintervallet för Hoppa tid-knapparna.

### Filladdning

Under filladdning kan du ändra den nätverkstyp som används för att ladda låtar. Tillgängliga alternativ: **Wi-Fi**, **Wi-Fi och mobildatanät**.

- **Förladdningstid** — ange bufferttidsintervallet. Öka detta om du har dålig nätverksanslutning.
- **Använd direktlänk** — när det är aktiverat används en direktlänk för att ladda låten om servern stöder det. Det kan påskynda låtladdning men kan påverka uppspelningsstabiliteten.

### Audioequalizer

Konfigurera den 10-bands audioequalizern, förinställningar och förförstärkaren. Du kan läsa mer om konfiguration av audioequalizern [här](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Uppspelningshastighet

Justera uppspelningshastigheten för ljudspelaren från **0,02× till 3,00×**. Tryck på konfigurationsikonen i det övre högra hörnet för att växla till **precist läge** för finare justeringar.

### Tonhöjdskorrigering

Ändra inställningar för tonhöjdskorrigering med de fördefinierade värdena, eller växla till **precist läge** genom att trycka på knappen i det övre högra hörnet. Tonhöjdskorrigering är tillgänglig i FFmpeg-kodekvärdet, med ett intervall från **-1000 till +1000**.

### Uppspelningscache

Låtar i ljudspelarens kö laddas automatiskt ner för att säkerställa smidig uppspelning. Om du manuellt laddar ner ljudfiler kan du inaktivera detta för att undvika dubbletter. Du kan också konfigurera storleken på ljudspelarens cache här.

### Sovtimer

Aktivera en timer för att automatiskt stoppa uppspelning efter en angiven period. Tryck på konfigurationsikonen i det övre högra hörnet för **precist läge** med minut-för-minut-granularitet.

## Bibliotek

Dina musikbiblioteksinställningar — automatisk synkronisering, metadataläsning, albumomslags laddning, spellistor, senaste och favoriter — finns här.

### Metadataläsning

När du lägger till spår i biblioteket sätter **metadataläsaren** igång. Den här bakgrundsprocessen läser all metadata från dina spår och organiserar dem efter Artist, Album, Genre och Kompositör. Du kan justera hastigheten för metadataläsning för att ladda data snabbare (till priset av mer batteri). Du kan också inaktivera metadataläsaren och visa filnamn i stället för tagginformation.

Metadataläsaren **uppdaterar bara metadata i ditt musikbibliotek** och ändrar inte filerna lagrade i ditt molnkonto eller lokal lagring. För att redigera metadata i själva ljudfilerna, använd den inbyggda **taggredigeraren** via motsvarande åtgärd i alternativmenyn.

När **Metadataläsning i bakgrunden** är på fortsätter läsaren att arbeta i bakgrundsläge. Om appen använder för mycket energi under ljuduppspelning kan iOS avbryta den.

Om du har en stor musiksamling, utför metadatasynkronisering på skrivbordsversionen av applikationen och överför det synkroniserade musikbiblioteket till iOS med **Säkerhetskopiering och återställning**.

När **Normalisera metadatakodning** är aktiverat normaliserar appen automatiskt kodningen av metadata för alla låtar. Det åtgärdar trasiga taggenkodar (till exempel efter redigering av filer på en Windows-PC) och förhindrar att felaktiga tecken visas i spårinformation.

**Ladda om metadata** flaggar varje fil i ditt musikbibliotek som att metadata saknas, vilket gör att metadataläsaren uppdaterar varje post.

**Starta metadataläsning** utlöser metadataläsaren manuellt. Förloppet visas under åtgärden.

### Onlinesynkronisering

Automatisk onlinemusiksync lägger till spår från anslutna molntjänster i musikbiblioteket automatiskt. För att aktivera det, öppna musikbiblioteksinställningarna och välj synkroniseringsmappar.

Med det här alternativet aktiverat skannar applikationen de valda mapparna, identifierar stödda ljudfiler och lägger till dem i ditt bibliotek. Starta eller stoppa synkronisering med motsvarande menyåtgärd.

Onlinesync körs bara när appen är i förgrunden, så synkronisering av ett stort bibliotek kan ta ett tag. För att påskynda processen, håll Flacbox öppen, anslut din enhet till ström och aktivera **Inställningar → Skärm → Alltid aktiv**.

Alternativt, utför onlinesync på skrivbordsversionen av appen och överför resultatet till iOS med **Säkerhetskopiering och återställning**.

Du kan också välja hur ofta onlinesync körs. Om du ställer in intervallet till **Omedelbart** utlöses en synkronisering varje gång du öppnar applikationen.

### Offlinesynkronisering

Konfigurera offlinemusiksync.

#### Synkroniserade offlinemappar

När du markerar en onlinemapp på din molnserver som tillgänglig offline (med menyn **Fler åtgärder**) visas den här. Mappinnehållet laddas ner till **Lokala filer → Offlinemappar**. När onlinemappen ändras (filer läggs till, tas bort eller uppdateras) kontrollerar appen efter ändringar och uppdaterar den lokala kopian på din enhet.

På den här skärmen kan du manuellt starta offlinemappssynkronisering, visa offlinemappen i dess överordnade mapp och inaktivera offline-läge för mappen. Inaktivering av offline-läge tar bort alla lokala kopior av filer från din enhet.

#### Tidsintervall

Välj hur ofta appen kontrollerar offlinemappar efter ändringar.

#### Starta skanning av lokala mappar

Skanna alla lokala mappar i applikationens **Documents**-katalog efter stödda ljudfiler. Hittade filer läggs automatiskt till i musikbiblioteket. Filer på din enhet men utanför applikationens Documents-katalog måste läggas till i musikbiblioteket manuellt, eftersom appen inte kan komma åt dem på grund av iOS / macOS säkerhetsbegränsningar.

**Viktigt:** Det är lämpligt att regelbundet initiera offlinemusiksync för att hålla ditt musikbibliotek uppdaterat med dina lokala filer.

### Personalisering

Konfigurera musikbiblioteksskärmstilen. Tre alternativ är tillgängliga: **Vanlig meny, Grupperad meny, Flikad meny**. Du kan också aktivera eller inaktivera albumomslag på albumdetaljskärmen.

### Albumomslag

Konfigurera hur applikationen laddar och lagrar albumkonstverk.

- **Nätverkstyp** — välj **Wi-Fi** eller **Wi-Fi och mobildatanät** för omslagnedladdningar.
- **Ladda albumomslag för onlinefiler** — när det är aktiverat laddas inbyggda albumomslag för filer lagrade i molnlagring. Det kan använda ytterligare nätverksdata.
- **Sök i mappen** — när det är aktiverat, om ett spår saknar inbyggt omslag, letar appen efter JPEG- eller PNG-bilder i samma mapp och använder dem som albumkonstverk.
- **Omslagskvalitet** — välj kvaliteten på albumomslag lagrade på din enhet.
- **Visa i mapp** — öppna mappen där albumomslag är cachade.
- **Ta bort alla** — ta bort cachade albumomslag för att frigöra lagring och tvinga appen att ladda om dem vid behov.

### Spellistor

Aktivera alternativet att lägga till samma låt i en spellista två gånger. Som standard är det här alternativet inaktiverat.

### Senaste

Hantera din lista med nyligen spelade låtar.

- **Ta bort lista** — ta bort hela listan med nyligen spelade låtar.
- **Ändra liststorlek** — ange antalet objekt som visas i listan.
- **Exportera låtlista** — exportera din lista med nyligen spelade låtar som M3U, CSV eller TXT. Detaljerade instruktioner finns [här](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoriter

Hantera listan med dina favoritlåtar.

- **Samtidig redigering** — när det är aktiverat lägger till en låt i favoriter både i musikbiblioteket och filsektionen samtidigt.
- **Ta bort lista** — ta bort hela listan med favoritlåtar.
- **Exportera låtlista** — liknar Senaste, exportera favoriter som M3U, CSV eller TXT.

### Ta bort musikbibliotek

Radera musikbiblioteksdatabasen. Dina musikfiler på lagringen lämnas orörda.

## Lösenkod

Aktivera lösenkodsskärmen för att skydda din applikationsdata med en 4-siffrig numerisk lösenkod. När den är aktiverad uppmanas du att ange lösenkoden varje gång appen startar. Kombinera den med iOS Face ID / Touch ID på enheten för extra skydd.

## Filhanteraren

Avsnittet Filhanteraren styr hur filer överförs, lagras och förhandsgranskas.

### Filöverföringar

Välj din nätverkspreferens för att ladda ner filer till din enhet.

### Maximalt antal parallella uppgifter

Ange antalet parallella nedladdningstrådar. Ett högre antal påskyndar nedladdningar men använder mer batteri.

### Filöverföringsuppgifter

Visar aktuella aktiva uppladdnings- och nedladdningsuppgifter.

### Bakgrundsöverföringar

Tillåt nedladdningar medan appen är i bakgrunden. Om bakgrundsöverföringar förbrukar mycket energi kan iOS avbryta appen.

### Spara nedladdade filer till

Välj standardnedladdningskatalogen, eller låt appen fråga dig varje gång.

### Synkroniserade offlinemappar

Hantera offlinesync för valda mappar. För att aktivera offlinesync, tryck på tre-punktsknappen bredvid en mapp och välj **Tillgängligt offline-läge**. Nya filer som läggs till i molnmappen laddas automatiskt ner till din enhet. Läs mer om offline-lägen [här](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Tidsintervall

Välj hur ofta offlinemappar synkroniseras. **Omedelbart** utlöser en synkronisering varje gång du öppnar appen.

### Visa fullständiga filnamn

Visa fullständiga filnamn, inklusive filändelser, i filhanteraren.

### Redigera onlinefiler

Inaktivera redigering av onlinefiler för att växla till skrivskyddat läge för anslutna molntjänster och förhindra oavsiktliga borttagningar. Den här åtgärden tar bort filredigeringsåtgärder från användargränssnittet.

### Kopiera filer vid öppning

Ange hur appen hanterar importerade filer från andra applikationer.

### Miniatyrer för filer

Hantera och ta bort genererade filminiatyrer för att frigöra lagringsutrymme.

### Ta bort temporära filer

Rensa applikationens cachemapp för att återta lagringsutrymme.

## Ljudtaggsredigeraren

Konfigurera den inbyggda ljudtaggsredigeraren — praktisk för batchrättning av artist / album / år / genre / omslagskonst-problem i moln- och lokala filer.

### Skalning av albumomslag

Välj skalningsmetoden som används när ett albumomslag sparas i ljudtaggar.

### Uppdatera onlinefiler

När det är aktiverat uppdaterar applikationen automatiskt en fils metadata på molnservern efter att du har redigerat den.

### Ta bort fil efter redigering online

Välj om applikationen ska ta bort den nedladdade kopian efter att redigeringen av en onlinefil på en molnserver är klar.

### Knappar på huvudskärmen

Välj vilka knappar som är synliga på huvudskärmen för ljudtaggsredigeraren.

För djupare batchredigering av många filer på en gång, installera vår följeapp **Evertag**.

## Widgetar

Aktivera widgetar så att appen uppdaterar widgetdata under uppspelning. Widgetuppdateringar kräver ytterligare energi, så reglaget är av som standard — aktivera det bara om du faktiskt använder widgetar på din hemskärm eller låsskärm.

Du kan lägga till Flacbox-widgetar genom att trycka länge på din hemskärm eller låsskärm, trycka på **+**, söka **Flacbox** och välja en widgetstorlek. Widgetar visar det aktuella omslaget, spårtiteln och artisten, och trycket går direkt till helskärmsspelaren. Widgetar fungerar också på macOS i meddelandecentret.

## CarPlay

Ändra CarPlay-inställningar här. Den här menyn är också tillgänglig inne i CarPlay-gränssnittet så att du kan justera upplevelsen under körning.

### Sortera

Konfigurera sorteringsalternativ för alla CarPlay-skärmar.

### Gräns för innehållsladdning

Välj om appen använder sidnumrering på CarPlay-skärmen. Sidnumrering håller menyer responsiva på stora bibliotek.

### Gradientfärg för menyikoner

Välj färgschemat för CarPlay-hemskärmen.

### Visa bilder

Inaktivera bilder på CarPlay-skärmen för att optimera laddningshastigheten och minska minnesanvändningen på stora bibliotek.

### Pausa uppspelning vid anslutning

Aktivera detta för att undvika plötsligt högt ljud när du ansluter din enhet till CarPlay.

## Wi-Fi Drive

Aktivera **Wi-Fi Drive** för att överföra filer från en dator till din enhet med en skrivbordswebbläsare, Finder eller Utforskaren. Detaljerade instruktioner om hur du använder Wi-Fi Drive finns [här](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalisering

Anpassa användargränssnittet efter dina önskemål.

### Applikationsikon

Välj en alternativ applikationsikon för din hemskärm (Premium).

### Färgschema

Välj användargränssnittets tema och aktivera mörkt läge. När **Standard** är valt följer applikationen enhetens övergripande utseendeinställningar.

### Bakgrundsstil

Ändra bakgrundsstilen för applikationen. För närvarande är det enda alternativet **Suddigt albumomslag**, som använder det nu spelande spårets konstverk som en suddad appbakgrund.

### Utseende för objekt i listan

Justera hur objekt visas i listor. Användbart på små skärmar — du kan låta appen justera radhöjden automatiskt baserat på innehåll, eller visa mindre ikoner i listceller för att ge text mer utrymme.

### Gräns för innehållsladdning

Som standard använder applikationen sidnumrering för att påskynda innehållsladdning. Du kan inaktivera sidnumrering för att ladda allt på en gång.

### Stil för skärmen Lokala filer

Ändra presentationsstilen för avsnittet **Lokala filer**.

### Stil för musikbiblioteksskärmen

Anpassa utseendet på skärmen **Musikbibliotek**.

### Stil för ljudspelarskärmen

Konfigurera utseendet på skärmen **Ljudspelaren**.

### Snabbmenystil

Välj stilen på snabbmenyn som visas när du trycker på knappen **Fler åtgärder**.

## Fönster

Tillgänglig på Mac och Catalyst. Konfigurera fönsterrelaterade inställningar som standardstorlek och beteende vid start.

## Skärm

Välj om skärmen ska förbli aktiv medan du använder applikationen. Användbart vid skanning av stora bibliotek eller utföring av långvarigt taggredigeringsarbete.

## Tillgänglighet

Aktivera **Textläge** för att dölja alla bilder i användargränssnittet. Textläge aktiveras automatiskt när VoiceOver är aktivt och är också användbart för mycket liten eller textbaserad uppsättning.

## Språk

Ändra applikationsspråket och åsidosätt systemstandarden. Ändringen träder i kraft efter att du helt har stängt och öppnat Flacbox igen. Stödda lokaliseringar inkluderar för närvarande: Afrikaans, Akan, Albanska, Amhariska, Arabiska, Armeniska, Assamesiska, Aymara, Azerbajdzjanska, Bambara, Bangla, Baskiska, Vitryska, Bosniska, Bulgariska, Burmesiska, Katalanska, Cebuano, Kinesiska (förenklad), Kinesiska (traditionell), Korsikanska, Kroatiska, Tjeckiska, Danska, Dhivehi, Dogri, Holländska, Engelska, Esperanto, Estniska, Ewe, Filippinska, Finska, Franska, Galiciska, Ganda, Georgiska, Tyska, Grekiska, Guarani, Gujarati, Haitisk kreol, Hausa, Hawaiiska, Hebreiska, Hindi, Hmong, Ungerska, Isländska, Igbo, Iloko, Indonesiska, Iriska, Italienska, Japanska, Javanesiska, Kannada, Kazakiska, Khmer, Kinyarwanda, Koreanska, Krio, Kurdiska, Kurdisk Sorani, Kirgiziska, Laotiska, Latin, Lettiska, Lingala, Litauiska, Luxemburgska, Makedonska, Maithili, Malagassiska, Malajiska, Malayalam, Maltesiska, Maori, Marathi, Mizo, Mongoliska, Nepalesiska, Norra Sotho, Norskt Bokmål, Nyanja, Odia, Oromo, Pashto, Persiska, Polska, Portugisiska, Punjabi, Rumänska, Ryska, Samoanska, Sanskrit, Skotsk gaeliska, Serbiska, Shona, Sindhi, Singalesiska, Slovakiska, Slovenska, Somaliska, Södra Sotho, Spanska, Sundanesiska, Swahili, Svenska, Tadzjikiska, Tamil, Tatariska, Telugu, Thailändska, Tsonga, Turkiska, Turkmeniska, Ukrainska, Urdu, Uiguriska, Uzbekiska, Vietnamesiska, Walesiska, Xhosa, Jiddisch, Yoruba, Zulu.

## Säkerhetskopiering och återställning

Använd den här funktionen för att säkerhetskopiera all din applikationsdata eller migrera den till en annan enhet. Du kan välja vad som ska inkluderas:

- **Databas** — alla dina spår i musikbiblioteket, inklusive spellistor. Offlinespår inkluderas inte för att hålla säkerhetskopieringsfilens storlek hanterbar.
- **Albumomslag** — alla dina cachade albumomslag.
- **Inställningar** — alla dina applikationsinställningar.

Tryck på **Säkerhetskopiera applikationsdata** för att starta säkerhetskopieringen. Applikationsdata skrivs till en enda fil som du kan använda senare för att återställa applikationstillståndet på en ny enhet eller efter att ha installerat om applikationen.

För att återställa applikationsdata på en ny enhet, flytta säkerhetskopieringsfilen till den nya enheten med en ansluten molntjänst eller iCloud och öppna den på den nya enheten.

Detaljerade steg-för-steg-instruktioner: [Hur man överför ditt musikbibliotek mellan enheter: Steg-för-steg-guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Hjälp

Öppna applikationsguiden för hjälp och vägledning om hur du använder appen effektivt.

## Vanliga frågor

Hitta svar på vanliga frågor i FAQ-avsnittet.

## Skicka feedback

Har du feedback eller behöver hjälp? Skicka din feedback till vårt supportteam direkt från appen.

## Dela den här appen

Dela applikationen med dina vänner för att sprida budskapet.

## Utforska fler appar

Utforska andra appar från Everappz.

## Villkor och bestämmelser

Beskriver villkoren och bestämmelserna för användning av applikationen. Läs dem innan du använder applikationen.

## Integritetspolicy

Besök sidan för integritetspolicy för att förstå vår datahantering. Läs den innan du använder applikationen.

## Analys och datainsamling

Kontrollera vilka tjänster som är aktiverade för analys och datainsamling och inaktivera de du inte vill ha.

## Juridiska meddelanden

Innehåller information om alla bibliotek som används i applikationen tillsammans med appens versionsnummer och buildinformation.
