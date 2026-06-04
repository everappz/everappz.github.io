---
title: "Ljudspelaren"
date: 2020-02-01
description: "Lär dig hur du använder Flacbox ljudspelaren på iPhone, iPad och Mac. Kontrollera uppspelning, hantera köer, konfigurera FFmpeg / systemljudmotorn, ändra samplingsfrekvens, tonhöjdskorrigering, IO-buffertduration, equalizer, ljudbokmärken, AirPlay 2, Google Cast, CarPlay, widgetar och Mac-tangentbordsgenvägar."
keywords: [
  "Flacbox spelargide", "ljudspelarinställningar", "Flacbox equalizer",
  "AirPlay musikströmning", "Google Cast musik", "ljudbokmärken",
  "Flacbox uppspelningskö", "Flacbox upprepa blanda", "Flacbox volymkontroll",
  "macOS minispelare", "voiceover musikapp",
  "Flacbox FFmpeg", "Flacbox tonhöjdskorrigering", "Flacbox samplingsfrekvens",
  "Flacbox extern DAC", "Flacbox surroundljud", "Flacbox IO-buffert",
  "Flacbox uppspelningshastighet", "Flacbox sovtimer"
]
tags: ["guide", "flacbox", "spelare"]
readingTime: 14
---


Ljudspelaren är appens huvudskärm där du kontrollerar musiken och de flesta uppspelningsfunktioner. Det är också där Flacbox hi-res-ljudmotor — byggd på systemkodekarna plus det medföljande **FFmpeg**-biblioteket — gör det tunga arbetet. Låt oss utforska hur man använder den.

## Öppna ljudspelaren

Du kan komma till helskärmsspelaren från minispelarfältet. På iPhone sitter minispelaren längst ned på huvudskärmen. På iPad och Mac är den på vänster sida. För att dölja minispelaren på iPhone, tryck på den en gång och svep nedåt. För att stänga helskärmsspelaren helt, tryck på stängknappen i det nedre högra hörnet.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox ljudspelares huvudskärm" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Stödda ljudformat

Flacbox spelar de mest populära ljudformaten — både Apples systemkodekar och många ytterligare format hanterade av det medföljande FFmpeg-motorn:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Det täcker praktiskt taget alla moderna förstörande och förlustfria format som du troligtvis har i en personlig musiksamling.

## Uppspelningskontroller

Längst ned på spelarskärmen hittar du knappar för Spela, Pausa, Nästa spår och Föregående spår. Det finns också valfria knappar som Nästa 30 sek och Föregående 30 sek som du kan aktivera i appinställningarna (praktiskt för ljudböcker). Du kan snabbspola framåt eller bakåt genom att hålla ned knapparna Nästa / Föregående. För att hoppa till en specifik del av ett spår, dra i uppspelningsreglaget.

## Upprepa och blanda

Tryck på upprepningsknappen för att cykla genom upprepningslägen:

- **Upprepa alla** — loopar alla spår i din kö.
- **Upprepa en** — upprepar bara det aktuella spåret.
- **Upprepa stopp** — pausar när det aktuella spåret är slut.
- **Upprepa ingen** — spelar kön en gång utan att upprepa.

Använd knappen **Blanda** för att randomisera ordningen på spår i kön.

## Volymkontroll

Öppna skärmen Ljudinställningar genom att trycka på ljudikonen under uppspelningskontrollerna för att komma åt volymreglaget. Du hittar också knappar här för **Google Cast** och **AirPlay** så att du snabbt kan växla uppspelning till en annan enhet.

## Google Cast (Chromecast)

För Google Cast-användare visas **Cast**-ikonen längst ned på spelaren. Tryck på den för att välja en enhet och börja strömma. Se till att din enhet och Google Cast-mottagaren är på samma Wi-Fi-nätverk. Obs: inte alla ljudformat är kompatibla med Google Cast — vissa hi-res-format kan behöva transkodas.

## AirPlay

För AirPlay, leta efter **AirPlay**-knappen längst ned på spelaren. Tryck på den och välj en enhet för strömning. Flacbox stöder **AirPlay 2**, så du kan spela upp till flera HomePods, Apple TVs eller AirPlay 2-kompatibla högtalare samtidigt.

## Audioequalizer

Flacbox inkluderar en **10-bands equalizer** med iPod-liknande förinställningar. Tryck på Equalizer i volymvyn och aktivera den sedan i det övre högra hörnet. Du kan använda förinställningar som Acoustic och Bass Booster, eller justera varje frekvensbands med reglage. Gör dina egna förinställningar, spara dem under valfritt namn och öka den totala volymen med förförstärkaren. Vi har mer detaljerade instruktioner om hur du använder equalizern [här](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox ljudspelarequalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Verktygsfält för spelarläge

För vissa spelarstiler finns det ett dedikerat verktygsfält längst upp i helskärmsspelaren. Det här verktygsfältet innehåller tre användbara knappar:

- **Sök** — hitta snabbt ett specifikt spår i din spelarkö.
- **Uppspelningshastighet** — justera uppspelningshastigheten från 0,02× till 3,00×. Perfekt för ljudböcker, poddar och föreläsningar. Tryck på Normal för att återgå till standardhastighet.
- **Ljudbokmärken** — skapa flera bokmärken per spår. Vi har fullständiga instruktioner om hur du använder bokmärken [här](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Spelarkö

För att se din spelarkö, tryck på köknappen till höger om den aktuella låten. Varje låt i kön har fler åtgärder — tryck på tre punkter för att visa dem. För att ändra ordning på en låt i kön, använd ordningsomkopplaren nära titeln och dra den till en ny position.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox uppspelningskö" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Kommentarer / Texter

För att visa spårkommentarer och inbyggda texter, samt LRC-filer, följ dessa steg:

1. Öppna **Inställningar**.
2. Gå till **Ljudspelaren**.
3. Välj **Personalisering**.
4. Tryck på **Knappar på huvudskärmen**.
5. Aktivera **Kommentarer**.

Tryck sedan på köknappen längst ned på skärmen flera gånger för att växla från omslags- / kövyn till kommentarsvyn. På skärmen Kommentarer, rulla åt höger för att växla mellan **Kommentarer**, **Inbyggda texter** och **LRC-filen**. Fullständiga instruktioner finns [här](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox texter och kommentarskärm" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Alternativmeny

Varje låt i ljudspelarens kö har en meny med fler åtgärder, nåbar genom att trycka på tre-punktsknappen nära låttiteln.

- **Spela härnäst** — lägger till låten överst i spelarkön.
- **Lägg till i spellista** — inkluderar låten i en spellista, med möjlighet att skapa en ny.
- **Lägg till i favoriter** — markerar låten som en favorit för snabb åtkomst.
- **Ladda ner** — sparar låten till lokala filer och visas på fliken **Lokala filer** och i avsnittet **Offlinemusik**.
- **Redigera ljudtaggar** — öppnar den inbyggda ljudtaggredigeraren för att fixa saknad metadata och ändrar låten på din lagring.
- **Visa i mapp** — avslöjar mappen där ljudfilen är lagrad.
- **Visa i Finder** — för filer importerade från din Mac avslöjar detta mappen där ljudfilen finns på din Mac.
- **Öppna i** — exporterar ljudfilen till en annan app.
- **Ta bort från kö** — tar bort den valda låten från ljudspelarens kö.
- **Ta bort från molntjänst** — tar bort låten från både musikbiblioteket och molnlagringen. **Den här åtgärden är oåterkallelig.**
- **Ta bort från lokala filer** — tar bort låten från både musikbiblioteket och lokal lagring. **Den här åtgärden är oåterkallelig.**
- **Ta bort från musikbibliotek** — tar bort låten från ditt musikbibliotek, medan filen bevaras på lagringen.

Samma alternativ är tillgängliga för det nu spelande objektet i ljudspelarens kö, som du kan komma åt genom att trycka på ikonen **Fler åtgärder** nära spårtiteln.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox alternativ för ett objekt i uppspelningskön" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Ytterligare spelaråtgärder

Tryck på knappen **Fler åtgärder** "..." på vänster sida av den nu spelande låttiteln för att se ytterligare åtgärder.

- **Fortsätt uppspelning** — återuppta från där du slutade, inklusive kö och medieposition. Särskilt användbart för ljudböcker. Aktiveras i appinställningarna.
- **Sök** — hitta snabbt ett specifikt spår i din ljudspelarkö.
- **Bokmärken** — visa din lista med skapade ljudbokmärken.
- **Kommentarer** — visa spårkommentarer och inbyggda texter, samt LRC-filer. Fullständiga instruktioner [här](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Hastighet** — justera uppspelningshastigheten efter dina önskemål.
- **Senaste** — öppna en lista med nyligen spelade låtar.
- **Favoriter** — se din samling med favoritmarkerade låtar.
- **Audioequalizer** — aktivera audioequalizern.
- **Sovtimer** — ange en timer för att stoppa uppspelningen efter ett angivet intervall. Bra för de stunder när du vill somna till din musik.
- **Spara kö som spellista** — spara den aktuella ljudspelarens kö som en ny spellista.
- **Ta bort kö** — rensa din spelarkö och stoppa uppspelningen.
- **Inställningar** — öppna ljudspelarinställningarna.
- **Hjälp** — hitta hjälp och vägledning.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox ljudspelares fler åtgärder-skärm" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Ljudbokmärken

Den här funktionen låter dig skapa flera bokmärken för spår i ditt musikbibliotek — perfekt för ljudböcker, föreläsningar, långa DJ-mixar eller att markera refrängen på ett favoritspår.

Så här skapar du ett nytt bokmärke:

- Börja spela den önskade låten.
- Öppna spelarskärmen.
- Tryck på knappen **Bokmärken** i verktygsfältet för spelarläge.
- Välj **Lägg till bokmärke**.
- Välj bokmärkestid och tryck på **Färdig** i det övre högra hörnet.

Redigering av bokmärken för det aktuella spåret är enkelt: tryck på Redigera i det övre högra hörnet för att gå in i redigeringsläge. I det här läget kan du ordna om bokmärken, ta bort dem, justera bokmärkestid och ändra bokmärkestitlar. Mer detaljerade instruktioner om ljudbokmärken finns [här](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox ljudbokmärkesskärm" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Senaste och favoriter

På spelarskärmen, tryck på tre punkter för att komma åt Senaste och Favoriter. I båda avsnitten kan du söka efter låtar, spela alla, blanda alla, exportera listan och rensa listan. Vi har detaljerade instruktioner om hur du exporterar låtlistor [här](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Anslut din iPhone till din bil via USB eller trådlös Apple CarPlay och Flacbox visas på din CarPlay-hemskärm, redo att spela musik säkert under körning. CarPlay-gränssnittet inkluderar dedikerade flikar för Bibliotek, Anslutningar, Lokala filer och Inställningar, med uppspelningskontroller, blanda, upprepa, köhantering och audioequalizern — allt tillgängligt utan att plocka upp telefonen. Konfigurera CarPlay-upplevelsen ytterligare i Inställningar → CarPlay — sorteringsalternativ, sidnumrering, menyikoners gradientfärg, om bilder laddas och ett alternativ för att pausa uppspelning automatiskt när CarPlay ansluts.

[Läs den fullständiga CarPlay-guiden](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox på Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Hemskärmswidgetar (iPhone och iPad)

Flacbox stöder iOS hemskärms- och låsskärmswidgetar så att du kan se och styra uppspelning på en blick. Se till att Widgetar är aktiverade i Inställningar → Widgetar → Aktivera widgetar, tryck sedan länge på din Hemskärm eller Låsskärm, tryck på **+**, sök **Flacbox** och lägg till en widget. Widgeten uppdateras under uppspelning för att visa det nu spelande spårets omslag, titel och artist.

## Minispelarfönstret (exklusivt för Mac)

Mac-användare kan använda en kompakt, alltid-ovanpå-minispelaren. Flytta markören till det nedre högra hörnet av Flacbox-fönstret, ändra storleken nedåt till minsta storlek och tryck på minimera-knappen. Håll det ovanpå alla andra fönster genom att välja Fönster → Visa fönster alltid överst i menyraden — perfekt för att hålla musikkontroller synliga medan du arbetar i en annan app.

## Tangentbordsgenvägar (exklusivt för Mac)

För Mac-användare finns en systemmeny för uppspelning tillgänglig i statusfältet med tangentbordsgenvägar. Till exempel, tryck på mellanslagstangenten för att Spela / Pausa. Genvägar för Stopp, Nästa låt, Föregående låt, Hoppa tid, Upprepa, Blanda och Uppspelningshastighet är också tillgängliga.

## Ljudspelarinställningar

För att komma åt inställningar, tryck på Fler-knappen på spelarskärmen och välj Inställningar. Här hittar du flera avsnitt, listade nedan.

### Allmänt

Dessa inställningar täcker de grundläggande aspekterna av ljudspelaren, inklusive uppspelningskön, ljudutgången och sparandet av spelarens tillstånd.

- **Upprepningsläge** — välj hur ljudspelaren beter sig när ett spår är klart:
  - **Upprepa alla** — spelar om alla spår i din kö.
  - **Upprepa en** — upprepar bara det aktuella spåret.
  - **Upprepa stopp** — pausar uppspelning när det aktuella spåret är slut.
  - **Upprepa ingen** — låter kön spela igenom utan att upprepa.
- **Blandningsläge** — randomisera ordningen på spår i din kö. Du kan stänga av **Blandning** eller slå på **Blandning**.
- **Ljudkodek** — välj den ljudmotor som används för uppspelning:
  - **Systemkodek + FFmpeg** — prioriterar systemets ljudkodek där det är möjligt, vilket förbättrar kompatibilitet och stabilitet. Tonhöjdskorrigering och justering av samplingsfrekvensen för ljudutgången kan vara begränsade i det här läget.
  - **FFmpeg** — tvingar FFmpeg-kodeken för alla ljudfiler, vilket låter dig justera tonhöjdskorrigering och samplingsfrekvensen för ljudutgången.
- **Samplingsfrekvens för ljudutgång** — justera samplingsfrekvensen för ljudutgången för att optimera ljudkvaliteten, särskilt användbart med en extern DAC. Tillgängliga värden: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** och **96 kHz**.
- **Antal kanaler för ljudutgång** — för flerkanals ljudsystem med en extern DAC, ange antal kanaler: **Mono, Stereo, Center / Vänster / Höger, Center / Vänster / Höger / Surround, ITU BS.775-1, 5.1 Surround** och **SDDS**.
- **Önskad IO-buffertduration för ljudutgång** — konfigurera in- / utbuffertdurationen för ljuduppspelning. Ett typiskt värde för att minimera latens vid uppspelning av högupplöst ljud är runt **5 millisekunder (0,005 sekunder)**. Den acceptabla buffertstorleken beror på din hårdvaru- och mjukvarumiljö, så testa olika durationer på din målenheten och välj den som bäst balanserar låg latens och störningsfri uppspelning.
- **Ljudutgångsläge (endast iOS)** — konfigurera blandat ljudutgångsläge så att ljud från Flacbox blandas med andra applikationer. Detaljerade instruktioner finns [här](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Spara uppspelningsposition** — säkerställer att applikationen sparar och återställer uppspelningspositionen för låtar i ditt musikbibliotek.
- **Spara ljudspelartillstånd** — bevarar ditt ljudspelartillstånd innan du stänger appen. För att fortsätta uppspelning, tryck på **Fortsätt uppspelning** längst upp i valfri mapp, album, artist eller genre när du öppnar appen igen. Du kan också återställa uppspelning för enskilda filer genom att trycka på det specifika spåret.

När du har aktiverat både **Spara uppspelningsposition** och **Spara ljudspelartillstånd**, öppna valfri mapp, album, artist eller genre och du ser en knapp **Fortsätt uppspelning** längst upp på skärmen tillsammans med det senast sparade spåret och positionen. Tryck på den för att återuppta precis där du slutade.

### Personalisering

Personalisering låter dig anpassa utseendet på ljudspelarskärmen, ändra tillgängliga kontroller på huvudskärmen, låsskärmen och statusfältet, och konfigurera hoppa-tid-kontroller.

- **Stil för ljudspelarskärmen** — konfigurera placeringen av element på ljudspelarskärmen.
- **Rullningsstil för albumomslag** — konfigurera den föredragna rullningsstilen för albumomslag.
- **Ytterligare element** — aktivera extra element på ljudspelarskärmen. **Ljudformatinfo** visar det nu spelande spårets ljudinfo ovanför omslaget; **Ljudvolymreglage** visar reglaget för ljudutgång under uppspelningskontrollerna.
- **Åtgärder på huvudskärmen** — konfigurera vilka knappar som ska synas på den primära ljudspelarskärmen som standard: **Upprepnings- och blandningsläge, Nästa och föregående låt, Hoppa tid, Sovtimer, Google Chromecast, AirPlay och Bluetooth, Audioequalizer, Sök, Bokmärken, Hastighet, Lägg till bokmärke, Lägg till i favoriter, Kommentarer** och mer.
- **Uppspelningskontroller på låsskärmen** — välj vilka kontroller som visas på låsskärmen. Möjliga värden: **Hoppa tid, Lägg till bokmärke, Lägg till i favoriter**.
- **Hoppa-tid-knappar** — välj tidsintervallet för knapparna **Hoppa tid**.

### Filladdning

Under filladdningsprocessen kan du ändra den nätverkstyp som används för att ladda låtar. Tillgängliga alternativ: **Wi-Fi**, **Wi-Fi och mobildatanät**.

- **Förladdningstid** — ange bufferttidsintervallet. Öka detta om du har dålig nätverksanslutning.
- **Använd direktlänk** — när det är aktiverat används en direktlänk för att ladda låten om servern stöder det. Det kan påskynda låtladdning men kan påverka uppspelningsstabiliteten.

### Audioequalizer

Anpassa inställningarna för audioequalizern. Du kan läsa mer om konfiguration av audioequalizern [här](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Uppspelningshastighet

Justera uppspelningshastigheten för ljudspelaren från **0,02× till 3,00×**. Tryck på konfigurationsikonen i det övre högra hörnet för att växla till **precist läge** för finare justeringar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox uppspelningshastighetsskärm" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Tonhöjdskorrigering

Ändra inställningar för tonhöjdskorrigering med de fördefinierade värdena. Du kan också växla mellan fördefinierade värden och precist läge genom att trycka på knappen i det övre högra hörnet. Tonhöjdskorrigering är tillgänglig i FFmpeg-kodekvärdet, med ett intervall från **-1000 till +1000**.

### Uppspelningscache

Låtar i ljudspelarens kö laddas automatiskt ner för att säkerställa smidig uppspelning. Om du manuellt laddar ner ljudfiler kan du inaktivera det här alternativet för att undvika dubbletter. Du kan också konfigurera storleken på ljudspelarens cache här.

### Sovtimer

Aktivera en timer för att automatiskt stoppa uppspelning efter en angiven period — praktiskt när du vill somna till musik. Tryck på konfigurationsikonen i det övre högra hörnet för **precist läge** med minut-för-minut-granularitet.

## Tillgänglighet

Flacbox är fullt tillgängligt med **VoiceOver**. Varje komponent har en väldesignad etikett och beskrivning. När VoiceOver är aktivt växlar appen till **Textläge** så att bara meningsfulla element visas — vilket förbättrar navigeringshastigheten och tydligheten. Du kan också aktivera Textläge i **Inställningar → Tillgänglighet → Textläge**.

### Justera reglage med VoiceOver

1. **Välj reglaget** — svep vänster eller höger tills VoiceOver meddelar det.
2. **Justera värdet** — dubbeltryck och håll reglaget, dra sedan uppåt eller nedåt för att snabbt ändra värdet. VoiceOver meddelar det nya värdet allteftersom du går.

### Justera spårposition i en lista med VoiceOver

1. Tryck på ikonen för ordningsomkoppling nära spårtiteln för att ge den fokus.
2. Dubbeltryck snabbt på ordningsomkopplaren. Vid det andra trycket, släpp inte fingret — håll det tills du hör ett ljud som indikerar att cellen är redo att flyttas.
3. Flytta cellen till sin nya position.

Andra komponenter fungerar som förväntat och använder systemets VoiceOver-mönster.
