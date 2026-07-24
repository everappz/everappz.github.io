---
title: "Så använder du ljudeffekter och DSP i Flacbox: Kompressor, Freeverb, Crossfeed, Eko, Volymnormalisering och mer"
date: 2026-07-24
description: "Den kompletta guiden till Flacbox-ljud på iPhone, iPad och Mac. Lär dig hur BASS-motorn fungerar, vilka extra format den spelar (inklusive MOD- och trackermusik och DSD), och exakt vad varje effekt, varje reglage och varje förinställning gör med ditt ljud, plus 10-bands equalizern och den anpassade DSP-kedjan."
keywords: ["Flacbox ljudeffekter", "Flacbox förinställningar förklarade", "Flacbox BASS-motor", "BASS ljudbibliotek iOS", "MOD-musikspelare iPhone", "trackermusikspelare iOS", "spela MOD XM IT S3M iPhone", "DSD-spelare iOS", "FLAC-spelare iPhone", "förlustfri musikspelare iOS", "Flacbox equalizer förinställningar", "10-bands equalizer iPhone", "volymnormalisering iPhone", "EBU R128 iOS", "loudness-normalisering musikspelare", "crossfeed hörlurar iOS", "bs2b crossfeed", "kompressor förinställningar musikspelare", "freeverb reverb iOS", "eko delay musikspelare", "DSP-kedja musikspelare", "basförstärkning iPhone", "hur man lägger till effekter på musik Flacbox", "bästa equalizer-inställningar iPhone"]
tags: ["Flacbox", "Ljudeffekter", "Hur man gör", "BASS", "Equalizer", "Basförstärkning", "Kompressor", "Freeverb", "Crossfeed", "Eko", "Volymnormalisering", "EBU R128", "MOD-musik", "Trackermusik", "DSD", "FLAC", "DSP", "Hörlurar", "Förinställningar"]
readingTime: 30
---

{{< author-byline >}}

**Kort svar:** I Flacbox väljer du en **Uppspelningsmotor** i **Inställningar > Ljudspelare**: **Standard** (Apples systemmotor), **Universal** (FFmpeg-motorn) eller **Sound FX** (**BASS™-motorn**). Motorn du väljer avgör vilka filformat som spelas, så valet spelar roll. **Sound FX**-motorn spelar extra format som de flesta iPhone-appar hoppar över (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus och gammal **MOD- och trackermusik** som MOD, XM, IT och S3M), och den är den enda motorn som driver ljudverktygen: en **10-bands equalizer**, **Volymnormalisering**, **Kompressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Eko**, **Chorus**, **Distorsion**, **Rotate** och **Crossfeed**, samt en bygg-din-egen **DSP-kedja**. Så för att använda effekterna i den här guiden ska du först ställa in din uppspelningsmotor på **Sound FX**. Varje verktyg har färdiga **förinställningar**. Öppna dem i **Inställningar > Ljudspelare** (Ljudeffekter, Ljudequalizer, Signalbehandling), eller tryck på knappen **⋯ (Fler åtgärder)** på spelaren och välj **Ljudeffekter**. Ingenting du gör här ändrar någonsin dina filer.

> Förklaringarna av reglage och förinställningar nedan är samma korta beskrivningar som Flacbox visar dig inuti appen, blandade med lite extra bakgrund så att du får hela bilden innan du trycker.

## Så läser du den här guiden

Varje verktyg fungerar på samma sätt:

1. **Slå på det.** Varje effekt har sin egen på/av-knapp. De är alla avstängda från början. Du kan slå på så många du vill samtidigt.
2. **Välj en förinställning.** En förinställning är en färdig inställning. Tryck på en och ljudet ändras direkt. Den här guiden listar vad **varje** förinställning gör.
3. **Finjustera (valfritt).** Öppna reglagen för att justera för hand. I samma ögonblick som du flyttar ett reglage visar effekten **Manuell**, så att du vet att du har lämnat förinställningen. Varje reglage har en återställningsknapp.

Ingenting sparas i dina filer. Detta är liveeffekter. Slå av en effekt så kommer ditt ursprungliga ljud tillbaka på en gång.

## Välj din uppspelningsmotor (Sound FX har effekterna)

Flacbox blandar inte motorer med varandra. Du väljer **en** i **Inställningar > Ljudspelare > Uppspelningsmotor**, och motorn du väljer avgör vilka filformat du kan spela och om effekterna är tillgängliga. Det finns tre val, som visas i appen under dessa exakta namn:

1. **Standard.** Apples inbyggda systemmotor. Använder hårdvaruavkodning för lägre batteriförbrukning.
2. **Universal.** FFmpeg-motorn, som öppnar ett mycket brett urval av format.
3. **Sound FX.** **BASS™-motorn**. Den spelar förlustfria och högupplösta filer med full noggrannhet, lägger till modul- (tracker-) musik och driver varje effekt, 10-bands equalizern och DSP-kedjan i den här guiden.

Eftersom varje motor stöder sin egen uppsättning format ändras de filer du kan spela med motorn du väljer. Ännu viktigare är att effekterna, equalizern och DSP-kedjan fungerar **endast** med **Sound FX**-motorn, så välj den först om du vill använda dem.

Sound FX är byggd på **BASS™**, ett professionellt ljudbibliotek från Un4seen Developments. Du kan läsa mer om det på dess hemsida på [un4seen.com](https://www.un4seen.com/).

## Musikformat: Vad Sound FX- (BASS™-) motorn lägger till (inklusive MOD- och trackermusik)

Med **Sound FX (BASS™)**-motorn vald spelar Flacbox specialistformaten nedan, utöver de vardagliga. Det mest speciella är **modulmusik**, även kallad **trackermusik**. En modulfil är inte en vanlig inspelning. Den innehåller små instrumentljud plus ett «partitur» som säger hur man spelar dem, och Flacbox bygger om låten live utifrån det partituret, så som dessa filer var tänkta att spelas. Vanliga spelare kan inte göra detta.

| Typ av musik | Format | Bra att veta |
|---|---|---|
| **Modul- / trackermusik** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Byggs om live av BASS™-modulspelaren. Perfekt för chiptunes och gamla demoscene- eller Amiga-låtar. |
| **Modern förlustfri** | FLAC | Full kvalitet, mindre än WAV. |
| **Annan förlustfri** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Mindre vanliga förlustfria typer, alla stöds. |
| **Högupplöst DSD** | DSF, DFF | Spelas på vanlig hårdvara med DSD över PCM. |
| **Modern förlustbringande** | Opus, Ogg Vorbis, MP3 | De vanliga streaming- och nedladdningstyperna. |

Sound FX-motorn spelar också de vanliga Apple-formaten (AAC, ALAC, M4A, WAV, AIFF) och livestreams, så effekterna och equalizern fungerar på dem också.

**Varför detta hjälper dig:** om du har en blandning av FLAC-album, högupplösta DSD-filer och en mapp med gamla MOD- eller XM-trackerlåtar spelar Flacbox dem alla, och equalizern och effekterna fungerar på var och en av dem.

## De tre menyerna du kommer att använda

Flacbox håller sina ljudverktyg på tre platser, alla inuti ljudspelarens inställningar. Se först till att din **Uppspelningsmotor** är inställd på **Sound FX** (Inställningar > Ljudspelare > Uppspelningsmotor), eftersom effekterna, equalizern och DSP-kedjan endast är tillgängliga med den motorn.

- **Ljudeffekter** (effektracket): öppna spelaren, tryck på **⋯ (Fler åtgärder)**, tryck på **Ljudeffekter**. Eller gå till **Inställningar > Ljudspelare > Ljudeffekter**.
- **Ljudequalizer** (10 band och förinställningar): **Inställningar > Ljudspelare > Ljudequalizer**.
- **Signalbehandling** (din egen DSP-kedja): **Inställningar > Ljudspelare > Signalbehandling**.

Du kan också ställa in **utgångssamplingsfrekvens**, **kanaler** och **buffertstorlek** under **Inställningar > Ljudspelare**.

## 10-bands equalizern

**Vad den gör:** Ändrar musikens klangfärg, från djup bas till ljus diskant. Detta är det bästa verktyget för en ren **basförstärkning** eller en ljusare, tydligare topp. Se den som tio volymrattar, var och en för en annan del av ljudet. Höj ett band för att föra fram den delen, sänk det för att dra tillbaka det. Små ändringar på några dB låter oftast bäst, och den fungerar på allt du spelar.

**Hur den fungerar:** Tio reglage vid **32, 64, 125, 250, 500 Hz och 1, 2, 4, 8, 16 kHz**. Varje går från **-12 dB (sänkning)** till **+12 dB (höjning)**. Det finns också en **Förförstärkare** från **-24 till +24 dB** för övergripande nivå. Du kan spara dina egna förinställningar och **exportera eller importera** dem mellan enheter.

**Vad varje inbyggd förinställning gör (22 förinställningar):**

| Förinställning | Vad den gör med ditt ljud |
|---|---|
| **Flat** | Ingen ändring. Alla band på noll. En ren utgångspunkt. |
| **Acoustic** | Varm bas och skarp, närvarande diskant. Får akustiska gitarrer och röster att kännas naturliga och livfulla. |
| **Bass Booster** | Kraftig höjning i låga registret, mellanregister och diskant orörda. Mer punch och tyngd. |
| **Bass Reducer** | Sänker det låga registret. Praktiskt för dånande rum, billiga öronproppar eller tunga spår. |
| **Treble Booster** | Höjer endast diskanten. Ger glans och luft, mer detaljer. |
| **Treble Reducer** | Mjukar upp diskanten. Tämjer skarpa eller vassa inspelningar. |
| **Classical** | Fulla bastoner och mjuk diskant med en lätt sänkning i mellanregistret. Mjukt och rymligt för orkestermusik. |
| **Dance** | Stora bastoner och ljus diskant med urgröpta mellanregister. Punchigt och energiskt för klubbspår. |
| **Deep** | Varmt, tjockt lågregister med mjukare diskant. Ett mysigt, avslappnat ljud. |
| **Electronic** | Kraftig bas och ljus diskant för synthar och beats. Brett och modernt. |
| **Hip-Hop** | Tung bas och tydlig diskant med kontrollerat mellanregister. Tyngd och punch. |
| **Jazz** | Varmt och mjukt, med en liten sänkning i mellanregistret. Enkelt och naturligt för akustisk jazz. |
| **Latin** | Höjda bastoner och diskant med rena mellanregister. Ljust och livfullt. |
| **Loudness** | Höjer bas och diskant kraftigt (en «leende»-kurva). Låter fylligare vid låg volym. |
| **Lounge** | Framträdande mellanregister med mjuka kanter. Avslappnat och röstvänligt. |
| **Piano** | Tydliga mellanregister och diskant så att pianotoner klingar rent. |
| **Pop** | Höjda mellanregister för sång, med bastoner och diskant tillbakadragna. Röster ligger längst fram. |
| **R&B** | Mycket kraftig värme i låg-mellanregistret och tydlig diskant. Mjukt och rikt. |
| **Rock** | Höjda bastoner och diskant för gitarrer och trummor. Energiskt och fylligt. |
| **Small Speakers** | Höjer bastoner och sänker diskant för att hjälpa små högtalare att låta fylligare. |
| **Spoken Word** | Höjer röstregistret och sänker den djupa basen. Gör tal tydligt. |
| **Vocal Booster** | Skjuter fram mittregistret där röster ligger, sänker runt dem. Sång sticker ut. |

**Tips för bas:** Börja med **Bass Booster**, och om det låter grumligt, dra ner Förförstärkaren 1 till 2 dB så att inget distorderar.

## Volymnormalisering (jämn volym)

**Vad den gör:** Vissa låtar spelas högre än andra, så du ändrar hela tiden volymen. Detta gör att varje låt spelas på ungefär samma volym av sig själv, så att du inte behöver göra det. Den är perfekt för blandade spellistor som blandar gamla och nya inspelningar, olika album eller olika källor, där ett spår kan vara mycket högre än nästa.

**Hur den fungerar:** Den lyssnar på den verkliga volymen för varje spår med **EBU R128**-standarden (mätt i **LUFS**, samma idé som streamingtjänster använder), och justerar sedan varje spår mot ditt mål. Den behöver inga taggar i dina filer och ändrar aldrig ljudet. EBU R128 mäter den volym som dina öron faktiskt känner över hela låten, inte bara den högsta toppen, vilket är varför den matchar hur högt spår verkligen verkar för dig. Flacbox räknar ut detta live medan musiken spelas (och kontrollerar volymen i förväg när det går), och tillämpar sedan en enda, jämn volymändring på spåret. Gränsen för **Max boost** hindrar mycket tysta inspelningar från att skjutas upp så hårt att de distorderar. Eftersom den läser själva ljudet fungerar den på vilken källa som helst, inklusive molnfiler, livestreams och modulmusik, även när filerna inte har några volymtaggar alls.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Målvolym** | Ställer in den volym som varje spår nivelleras mot. Högre värden gör att allt spelas högre överlag. | -30 till -6 LUFS (-16) |
| **Max boost** | Begränsar hur mycket tysta spår kan förstärkas. Högre värden för mjuka inspelningar närmare målet. | 0 till 24 dB (12) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Light** | Mjuk nivellering för avslappnat lyssnande. Jämnar ut uppenbara volymhopp utan att skjuta tysta spår hårt. |
| **Standard** | Den allsidiga standarden. Ett streamingliknande volymmål som passar de flesta musik. Börja här. |
| **Strong** | Aggressiv matchning som skjuter upp tysta spår bestämt. Bäst för blandade bibliotek med stora nivåskillnader. |
| **Night** | Ett tystare övergripande mål som ändå lyfter mjuka partier, så att lyssnande sent på kvällen förblir konsekvent och lågt. |

## Kompressor (jämna ut höga och tysta partier)

**Vad den gör:** I en låt kan de tysta partierna vara för mjuka och de höga partierna för höga. Detta för dem närmare varandra, så att hela låten är lätt att höra, även i bilen eller på en bullrig plats. Den vrider försiktigt ner de högsta ögonblicken och lyfter de mjukare, så att du slutar sträcka dig efter volymen under ett enda spår. Detta är annorlunda än Volymnormalisering: Kompressorn jämnar ut saker **inuti** en låt, medan Volymnormalisering matchar volymen **mellan** låtar. De två fungerar bra tillsammans. Börja med en förinställning, och öppna bara reglagen om du vill ha mer kontroll.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Tröskel** | Nivån där komprimeringen börjar. Lägre värden pressar ihop mer av ljudet och håller tysta och höga partier närmare varandra. | -60 till 0 dB (-20) |
| **Ratio** | Hur kraftigt de höga partierna hålls tillbaka när de passerar tröskeln. Högre värden komprimerar hårdare och håller ljudet jämnare. | 1:1 till 30:1 (4:1) |
| **Attack** | Hur snabbt effekten reagerar på en plötslig hög topp. Korta värden fångar transienter; längre släpper igenom dem. | 0,1 till 1000 ms (10 ms) |
| **Release** | Hur snabbt effekten släpper efter att det höga partiet passerat. Korta värden kan pumpa; längre låter mjukare. | 10 ms till 5 s (100 ms) |
| **Master gain** | Slutlig utgångshöjning som tillämpas efter behandling. Höj denna för att lyfta den övergripande volymen när dynamiken har jämnats ut. | -30 till +30 dB (0) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Transparent** | Ett knappt märkbart skyddsnät. Bevarar dynamiken nästan helt och fångar bara de högsta topparna. |
| **Soft** | Lätt nivellering för hi-fi-lyssnande hemma. Subtil utjämning utan att pressa ihop musiken. |
| **Standard** | Förnuftig standard för vardaglig musikuppspelning. Den första förinställningen att prova. |
| **Heavy** | Aggressiv utjämning för bullriga miljöer. Bil, fullsatt rum, lyssnande på låg volym. |
| **Voice / Podcast** | Talanpassad. Långsammare attack släpper igenom väsljud, generös makeup-gain drar upp sång. |
| **Old Recordings** | Vintagealbum och restaurerat vinyl, där genomsnittsnivån är under moderna utgåvor. |
| **Late Night** | Tung komprimering plus stor höjning för tyst lyssnande när grannar eller sovande familj spelar roll. |
| **Movie Dialog** | För fram tal mot musik och ljudeffekter i ett varierat ljudspår. |
| **Streaming Match** | Siktar på ungefär volymnormaliseringen hos moderna streamingtjänster runt -14 LUFS. |
| **Maximum Loudness** | Allt in. Träffar limitern; förvänta dig en ihoppressad, mycket jämn signal. Den bokstavliga maxvolym-förinställningen. |

## Freeverb (reverb, en känsla av rymd)

**Vad den gör:** Lägger till en känsla av rymd till musiken, från ett litet rum upp till en stor sal. Välj en förinställning, eller finjustera den torra och våta blandningen, rumsstorlek, dämpning och bredd själv. Reverb är det naturliga eko du hör i vilken verklig rymd som helst, och Freeverb återskapar det i mjukvara. Lite får platta eller närmikade inspelningar att kännas mer öppna och levande. Mycket placerar musiken i en stor, avlägsen rymd. Det är en kreativ effekt, så håll den våta blandningen måttlig för naturliga resultat.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Torr blandning** | Hur mycket av det ursprungliga, orörda ljudet som behålls. Högre värden lämnar mer av den torra signalen i blandningen. | 0 till 1 (0,0) |
| **Våt blandning** | Hur mycket av det efterklingande ljudet som läggs till. Högre värden gör reverbet högre och tydligare. | 0 till 3 (1,0) |
| **Rumsstorlek** | Storleken på den föreställda rymden. Högre värden ger en längre, större reverb-svans, från ett litet rum upp till en katedral. | 0 till 1 (0,5) |
| **Dämpning** | Hur snabbt de höga frekvenserna klingar av i svansen. Högre värden gör reverbet mörkare och varmare. | 0 till 1 (0,5) |
| **Bredd** | Reverbets stereospridning. Högre värden får rymden att kännas bredare mellan vänster och höger kanal. | 0 till 1 (1,0) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Room** | En liten, tät rymd. Subtil ambiens som ger en känsla av plats utan att skölja bort ljudet. |
| **Studio** | Ett torrt, kontrollerat inspelningsrum. Precis tillräckligt med reflektion för att låta naturligt. |
| **Hall** | En stor konsertsal. En lång, frodig svans som passar orkester- och akustisk musik. |
| **Cathedral** | En enorm, ekande stenrymd. Den längsta, mest dramatiska reverb-svansen. |
| **Plate** | Ett ljust, tätt studioplåtreverb. Klassiskt för sång och trummor. |
| **Ambience** | En kort, luftig ambiens. Ger en lätt känsla av rymd samtidigt som det förblir mestadels torrt. |

## Auto Wah (funkigt filtersvep)

**Vad den gör:** Ett filter som sveper upp och ner på egen hand för ett funkigt, röstliknande wah-ljud. Välj en förinställning, eller ställ in våt blandning, feedback, hastighet, omfång och frekvens själv. Det är samma «wah»-svep som en gitarrwah-pedal gör, men här rör det sig av sig själv i takt med musiken. Det låter fantastiskt på funk-, disco- och elektroniska spår. Det är en djärv, tydlig effekt, så lite räcker långt vid vardagslyssnande.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Våt blandning** | Hur stark wah-effekten är i blandningen. Högre värden gör det svepande filtret tydligare. | -2 till +2 (1,5) |
| **Feedback** | Hur mycket av utgången som matas tillbaka in i effekten. Högre värden gör wah:et mer resonant och uttalat. | -1 till +1 (0,5) |
| **Hastighet** | Hur snabbt filtret sveper upp och ner. Högre värden ger ett snabbare, mer rytmiskt wah. | 0,1 till 9 Hz (2,0) |
| **Omfång** | Hur långt filtret sveper, i oktaver. Högre värden ger ett bredare, mer dramatiskt svep. | 0,1 till 9 oktaver (4,3) |
| **Frekvens** | Basfrekvensen som filtret sveper runt. Lägre värden låter djupare; högre värden låter ljusare. | 1 till 1000 Hz (50) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Classic** | Ett balanserat, klassiskt wah-svep. En bra utgångspunkt för funk och rock. |
| **Slow** | Ett långsamt, brett svep som driver försiktigt upp och ner. Perfekt för pads och långa toner. |
| **Funky** | Ett snabbt, punchigt svep med mycket rörelse. Ger rytmiskt bett till gitarrer och synthar. |
| **Deep** | Ett djupt, brett svep som börjar från en låg frekvens. Stort och dramatiskt. |
| **Subtle** | En försiktig, underskattad rörelse. Ger karaktär utan att dominera ljudet. |
| **Resonant** | Ett skarpt, resonant wah med hög feedback. Röstliknande och uttrycksfullt. |

## Phaser (virvlande vinande)

**Vad den gör:** Ett svepande filter som lägger till en virvlande, vinande rörelse till ljudet. Välj en förinställning, eller ställ in feedback, hastighet, omfång och frekvens själv. Det lägger till försiktig rörelse och skimmer utan att ändra tonerna. Det är subtilt på sång och pads, och dramatiskt på synthar och gitarrer. Prova Slow för en drömsk känsla eller Jet för en stark virvel.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Feedback** | Hur mycket av utgången som matas tillbaka in i effekten. Högre värden gör phasern mer resonant och uttalad. | -1 till +1 (0,0) |
| **Hastighet** | Hur snabbt filtret sveper upp och ner. Högre värden ger en snabbare, mer rytmisk phasing. | 0,1 till 9 Hz (1,0) |
| **Omfång** | Hur långt filtret sveper, i oktaver. Högre värden ger ett bredare, mer dramatiskt svep. | 0,1 till 9 oktaver (4,0) |
| **Frekvens** | Basfrekvensen som filtret sveper runt. Lägre värden låter djupare; högre värden låter ljusare. | 1 till 1000 Hz (100) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Classic** | Ett balanserat, klassiskt phaser-svep. En bra utgångspunkt för gitarrer och klaviatur. |
| **Slow** | Ett långsamt, brett svep som driver försiktigt upp och ner. Perfekt för pads och långa toner. |
| **Fast** | Ett snabbt, skimrande svep med mycket rörelse. Ger rörelse och energi. |
| **Deep** | Ett djupt, brett svep som börjar från en låg frekvens. Stort och dramatiskt. |
| **Subtle** | En försiktig, underskattad rörelse. Ger karaktär utan att dominera ljudet. |
| **Jet** | Ett intensivt, resonant svep med hög feedback, det klassiska jetplansvinandet. |

## Flanger (jetplanssvep)

**Vad den gör:** En kort, rörlig fördröjning som ger ljudet ett jetliknande, svepande vinande. Välj en förinställning, eller ställ in djup, feedback, hastighet och fördröjning själv. Det är en starkare, mer metallisk kusin till phasern, känd för det vinande svepet i klassisk rock och elektronisk musik. Subtila inställningar ger försiktig rörelse, medan djupa inställningar är dramatiska och tydliga. Bäst att använda sparsamt, för effekt.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Djup** | Hur stark den svepande effekten är. Högre värden gör flangern tydligare. | 0 till 100 % (25) |
| **Feedback** | Hur mycket av utgången som matas tillbaka in i effekten. Högre värden gör flangern mer resonant och metallisk. | -99 till +99 % (-50) |
| **Hastighet** | Hur snabbt svepet rör sig upp och ner. Högre värden ger en snabbare, mer skimrande rörelse. | 0 till 10 Hz (0,25) |
| **Fördröjning** | Den grundläggande fördröjningstiden som svepet bygger på. Högre värden ger en djupare, mer ihålig karaktär. | 0 till 4 ms (2,0) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Classic** | En balanserad, klassisk flanger. En bra utgångspunkt för gitarrer och klaviatur. |
| **Subtle** | Ett försiktigt, underskattat svep. Ger rörelse utan att dominera ljudet. |
| **Deep** | Ett djupt, tungt svep med stark feedback. Stort och dramatiskt. |
| **Jet** | Ett intensivt svep med positiv feedback, det klassiska jetplansvinandet. |
| **Fast** | Ett snabbt, skimrande svep med mycket rörelse och energi. |
| **Wide** | Ett långsamt, brett svep med lång fördröjning. Frodigt och rymligt. |

## Eko (upprepningar)

**Vad den gör:** Upprepar ljudet som avtonande ekon för en känsla av rymd och djup. Välj en förinställning, eller ställ in våt blandning, feedback och fördröjning själv. Det är som att ropa ut i en kanjon: ljudet kommer tillbaka en eller flera gånger efter ett kort mellanrum. En enda kort upprepning ger kropp och en retrokänsla, medan längre upprepningar med mer feedback skapar rymliga, avtonande svansar. Ping Pong-förinställningen studsar upprepningarna mellan dina vänstra och högra öron, vilket är kul i hörlurar. Håll den våta blandningen måttlig så att ekona stöttar musiken snarare än täcker den.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Våt blandning** | Hur höga ekona är jämfört med originalljudet. Högre värden gör att upprepningarna sticker ut mer. | -2 till +2 (0,6) |
| **Feedback** | Hur många gånger ekot upprepas. Högre värden ger fler upprepningar som tar längre tid att tona av. | -1 till +1 (0,5) |
| **Fördröjning** | Tiden mellan ekon. Kortare värden ger ett tight slap-back; längre värden ger utspridda upprepningar. | 0,01 till 2 s (0,4) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Slapback** | En enda, tight upprepning direkt bakom ljudet. Klassisk rockabilly-slap-back. |
| **Room** | Ett kort, naturligt eko, som ett litet rum. Ger rymd utan att smeta ut ljudet. |
| **Tape** | Varma, medellånga upprepningar som tonar av gradvis, som en gammal bandfördröjning. |
| **Dub** | Långa, tunga upprepningar med stark feedback. Stort, dubbigt och rymligt. |
| **Ping Pong** | Ekon studsar mellan vänster och höger högtalare för en bred stereoeffekt. |
| **Long** | Långsamma, brett utspridda upprepningar som tonar bort långt bakom ljudet. |

## Chorus (tjockare, bredare ljud)

**Vad den gör:** Förtjockar och breddar ljudet genom att lägga en skiftande kopia över originalet. Välj en förinställning, eller ställ in våt/torr-blandning, djup, hastighet och feedback själv. Det får ett instrument eller en röst att låta som flera som spelar tillsammans, genom att lägga till lätt distämda, rörliga kopior. Detta ger rikedom och ett försiktigt skimmer. Subtila inställningar värmer upp saker, medan starka inställningar låter frodiga och drömska. Det är populärt på gitarrer, klaviaturer och sång.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Våt/Torr** | Hur mycket av chorusen du hör jämfört med originalljudet. Högre värden gör effekten tydligare. | 0 till 100 % (50) |
| **Djup** | Hur långt tonhöjden vibrerar upp och ner. Högre värden ger ett tjockare, mer skimrande ljud. | 0 till 100 % (25) |
| **Hastighet** | Hur snabbt skimret rör sig. Långsammare hastigheter låter försiktiga och frodiga; snabbare hastigheter låter mer som vibrato. | 0 till 10 Hz (1,1) |
| **Feedback** | Hur mycket av effekten som matas tillbaka in i sig själv. Högre värden gör chorusen mer resonant och intensiv. | -99 till +99 % (25) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Subtle** | En försiktig förtjockning som ger värme utan att dra uppmärksamhet till sig. |
| **Lush** | En rik, klassisk chorus. En utmärkt allroundinställning för gitarrer och klaviatur. |
| **Ensemble** | Ett fullt, skiktat skimmer som får ett enda instrument att låta som flera. |
| **Vibrato** | Helt våt med en snabb hastighet, för ett vaggande vibrato istället för en subtil chorus. |
| **Wide** | Ett långsamt, brett skimmer som öppnar upp stereobilden. Rymligt och drömskt. |
| **Twelve-String** | Ett ljust, resonant skimmer som påminner om en tolvsträngad gitarr. |

## Distorsion (grus och kant)

**Vad den gör:** Lägger till grus och kant genom att överstyra ljudet. Välj en förinställning, eller ställ in drive, utgång och ton själv. Det gör ljudet medvetet skrovligt, från en varm, grusig kant till en trasig, luddig ton. Det är en kreativ effekt för skojs skull snarare än ett sätt att förbättra kvaliteten, så använd den i små mängder. Det är kul på elektroniska, rock- och experimentella spår. Sänk Utgången om en tung förinställning blir för hög.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Drive** | Hur hårt ljudet distorderas. Högre värden är grusigare och mer aggressiva. | 0 till 100 % (15) |
| **Utgång** | Utgångsnivån efter distorsion. Sänk den om en tung inställning blir för hög. | -60 till 0 dB (-18) |
| **Ton** | Rullar av diskanten före distorsion. Lägre värden låter mörkare och varmare. | 100 till 8000 Hz (8000) |
| **Center** | Vilken frekvens distorsionen är fokuserad kring. Skiftar karaktären ljusare eller mörkare. | 100 till 8000 Hz (2400) |
| **Bredd** | Hur bred det fokuset är. Smalt låter skarpt och nasalt; brett låter fullt och öppet. | 100 till 8000 Hz (2400) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Warm Drive** | Ett lätt, varmt grus som ger kant utan att ändra karaktären mycket. |
| **Crunch** | En klassisk crunchig overdrive, punchig och rytmisk. |
| **Overdrive** | En ljus, driven ton med mycket bett. Perfekt för leadljud. |
| **Fuzz** | En tjock, mättad fuzz. Tung och full av övertoner. |
| **Metal** | En tight, mellanregisterfokuserad högförstärkningston för aggressiva, tunga ljud. |
| **Screamer** | En mellanregisterhöjd overdrive som skär igenom, som en tube screamer. |
| **LoFi** | En krossad, smalbandig distorsion för en grusig lo-fi-karaktär. |

## Rotate (snurrande stereo)

**Vad den gör:** Snurrar ljudet runt stereofältet för en roterande, virvlande effekt. Välj en förinställning, eller ställ in hastigheten själv. Den flyttar långsamt ljudet runt dina vänstra och högra kanaler, lite som en snurrande högtalare, vilket ger en virvlande, hypnotisk känsla. Långsamma inställningar är försiktiga och breda, medan snabba inställningar är yra och tydliga. Det är en stereoeffekt, så den är mest märkbar på hörlurar eller välplacerade högtalare.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Hastighet** | Hur snabbt ljudet snurrar runt stereofältet. Negativa värden snurrar åt andra hållet; noll håller det stilla. | -5 till +5 Hz (1,0) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Slow Pan** | En långsam, försiktig drift från sida till sida. Subtil och bred. |
| **Sway** | En jämn vänster-höger-gungning. Ger försiktig rörelse till stereobilden. |
| **Rotary** | En medelsnabb snurr som påminner om en roterande högtalare. |
| **Fast Spin** | En snabb snurr runt stereofältet för en yr, virvlande effekt. |
| **Reverse** | En medelsnabb snurr i motsatt riktning. |
| **Whirl** | En mycket snabb virvel. Intensiv och förvirrande. |

## Crossfeed (naturligt ljud i hörlurar)

På högtalare hör vart och ett av dina öron både vänster och höger högtalare, bara vid något olika tidpunkter och volymer. På hörlurar är den naturliga blandningen borta: ditt vänstra öra hör bara den vänstra kanalen och ditt högra öra bara den högra. Denna «superstereo» kan få musik att kännas som om den är delad inuti ditt huvud, och hårt panorerade inspelningar, där ett instrument sitter helt på en sida, kan kännas onaturliga eller tröttsamma vid långa lyssningar.

Crossfeed löser detta genom att blanda en liten, filtrerad mängd av varje kanal in i den andra, med en liten fördröjning och en försiktig avrullning av de höga frekvenserna. Det är nära hur ljud från riktiga högtalare når båda dina öron, inklusive hur ditt huvud något skuggar det bortre örat. Resultatet är en mer naturlig, högtalarliknande bild som sitter lite framför dig istället för inuti ditt huvud, och det minskar lyssningströtthet vid långa sessioner. Flacbox använder den välkända **bs2b-metoden (Bauer stereophonic-to-binaural)**, en respekterad crossfeed med öppen källkod som används av många audiofila spelare. Du kan läsa om algoritmen på [bs2b-projektsidan](https://bs2b.sourceforge.net/).

**Cutoff** styr hur varm blandningen låter, och **Matningsnivå** styr hur stark den är. Förinställningarna täcker de klassiska bs2b-nivåerna, från en knappt märkbar antydan upp till en fast, högtalarliknande blandning. Crossfeed är en hörlurseffekt, så lämna den av när du lyssnar på högtalare.

**Reglage:**

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Cutoff** | Ställer in var blödningen mellan kanaler börjar rulla av. Lägre värden ger en varmare, mer uttalad effekt. | 300 till 2000 Hz (700) |
| **Matningsnivå** | Styr hur mycket av en kanal som blöder in i den andra. Högre värden ger ett mer högtalarliknande ljud. | 1 till 15 dB (4,5) |

**Förinställningar:**

| Förinställning | Vad den gör |
|---|---|
| **Subtle** | Knappt märkbar crossfeed för avslappnat lyssnande. Mjukar upp hårt panorerad stereo utan att ändra klangbalansen. |
| **Chu Moy** | Den klassiska allsidiga standarden. Balanserad och lätt varm, den fungerar på nästan vilket material som helst. Börja här. |
| **Strong** | Starkare blödning för hårdare panorerade mixar. Mer tydlig stereoförsmalning. |
| **Jan Meier** | Populär bland hörlursentusiaster. Bredare matning, mer högtalarliknande presentation, lätt bashöjning. |
| **Speaker-like** | Inställd för den mest naturliga högtalarliknande återgivningen över hörlurar. |
| **Vintage Stereo** | Aggressiv crossfeed inställd för 1960- och 1970-talsmixar med hårt panorerade trummor och sång. |

## Signalbehandling: Bygg din egen DSP-kedja

Utöver de färdiga effekterna låter Flacbox dig bygga din egen kedja i **Inställningar > Ljudspelare > Signalbehandling**. Som appen förklarar när kedjan är tom: *«Tryck på + för att lägga till en effekt. Slå på eller av var och en med dess brytare, dra för att ändra ordning, tryck för att redigera dess parametrar och håll länge nedtryckt för att duplicera eller ta bort.»*

**Ordningen spelar roll**: ett filter före en distorsion låter annorlunda än samma filter efter den. Du kan också rikta hela kedjan mot **Alla kanaler**, **Vänster kanal** eller **Höger kanal**.

Nedan är varje block, med appens egen text för varje reglage och varje förinställning.

### Gain (nivåtrimning)

Höjer eller sänker nivån vid en punkt i kedjan.

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Gain** | Höjer eller sänker nivån vid denna punkt i kedjan. Använd den för att kompensera nivå efter andra effekter, eller för att driva de som följer. | -24 till +24 dB (0) |

| Förinställning | Vad den gör |
|---|---|
| **Unity** | Ingen ändring i nivå. En neutral utgångspunkt. |
| **Cut** | En stor sänkning. Tämjer en hög källa, eller ger utrymme före effekterna som följer. |
| **Trim** | En försiktig sänkning för att dra tillbaka nivån lite. |
| **Lift** | En blygsam höjning för att lyfta upp en tyst källa. |
| **Boost** | En stark höjning för tyst material, eller för att driva de följande effekterna hårdare. |
| **Max** | Maximal höjning. Högt, se upp för klippning senare i kedjan. |

### Low Pass (tar bort diskant)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Cutoff** | Ställer in var filtret börjar rulla av diskanten. Sänk den för att göra ljudet mörkare och mjukare; höj den mot toppen för att öppna helt. | 20 Hz till 20 kHz (20 kHz) |
| **Resonans** | Framhäver frekvenserna precis vid cutoffen. Håll den låg för en ren avrullning; höj den för en toppig, visslande kant. | 0,1 till 10 (0,707) |

| Förinställning | Vad den gör |
|---|---|
| **Air** | Trimmar endast den allra översta toppen. Tar bort lite kant utan att dämpa ljudet. |
| **Warm** | En försiktig avrullning av diskanten för en varmare, rundare ton. |
| **Mellow** | Märkbart mjukat. Drar tillbaka ljusheten för en avslappnad känsla. |
| **Muffled** | Mörkt och dämpat, som om hört genom en vägg. |
| **Telephone** | En smal, resonant topp lågt i registret. En tunn, telefonliknande röst. |

### High Pass (tar bort bas)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Cutoff** | Ställer in var filtret börjar rulla av basen. Höj den för att tunna ut lågregistret och ta bort mullrande; sänk den mot botten för att öppna helt. | 20 Hz till 20 kHz (20 Hz) |
| **Resonans** | Framhäver frekvenserna precis vid cutoffen. Håll den låg för en ren avrullning; höj den för en toppig, visslande kant. | 0,1 till 10 (0,707) |

| Förinställning | Vad den gör |
|---|---|
| **Rumble Cut** | Tar bort subsoniskt mullrande och DC-offset utan att röra det hörbara lågregistret. |
| **Tighten** | Trimmar dånande låga frekvenser för en tightare, renare bas. |
| **Thin** | Sänker värmen och kroppen och lämnar ett lättare, tunnare ljud. |
| **Radio** | Endast mellanregistret och diskanten återstår, som en liten radiohögtalare. |
| **Telephone** | En smal, resonant topp högt i registret. En tunn, telefonliknande röst. |

### Band Pass (behåller ett mittband)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Center** | Ställer in frekvensen som filtret släpper igenom. Allt över och under den rullas av. Svep den för att välja ut bas, mellanregister eller diskant. | 20 Hz till 20 kHz (1 kHz) |
| **Resonans** | Styr hur brett bandet är. Låga värden släpper igenom ett brett register; höj den för att smalna in mot centret för en skarp, resonant ton. | 0,1 till 10 (0,707) |

| Förinställning | Vad den gör |
|---|---|
| **Voice** | Ett brett band runt mellanregistret där de flesta röster ligger. En neutral utgångspunkt. |
| **Bass** | Isolerar lågregistret och lämnar bara basen och bastrumman. |
| **Body** | Fokuserar på låg-mellanregistret för en varm, boxig kropp. |
| **Presence** | Höjer övre mellanregistret för klarhet och närvaro. |
| **Telephone** | Ett smalt mellanregisterband. Ett tunt, telefonliknande ljud. |
| **Wah** | En mycket smal, resonant topp. Svep centret för en wah-effekt. |

### Notch (tar bort ett smalt band)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Frekvens** | Ställer in frekvensen som filtret tar bort. Allt över och under den passerar igenom. Ställ in den på ett brum eller en resonans för att skära bort den. | 20 Hz till 20 kHz (60 Hz) |
| **Resonans** | Styr hur bred sänkningen är. Låga värden gröper ur ett brett register; höj den för att bara ta bort ett punktband och lämna resten orört. | 0,1 till 10 (8,0) |

| Förinställning | Vad den gör |
|---|---|
| **Mains Hum 60** | Tar bort 60 Hz elektriskt brum (nordamerikanskt elnät). En neutral utgångspunkt. |
| **Mains Hum 50** | Tar bort 50 Hz elektriskt brum (europeiskt och andra elnät). |
| **Rumble** | Skär bort ett lågfrekvent mullrande eller en resonans utan att tunna ut hela botten. |
| **Mud** | Gröper ur låg-mellanregistrets grumlighet för ett renare, tydligare ljud. |
| **Boxy** | Tar bort ett boxigt mellanregistertutande. |
| **Harsh** | Tämjer en skarp, genomträngande topp i övre mellanregistret. |

### Peaking (parametriskt EQ-band)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Frekvens** | Centret för bandet att höja eller sänka. Svep den för att hitta frekvensen du vill forma. | 20 Hz till 20 kHz (1 kHz) |
| **Gain** | Hur mycket att höja eller sänka vid centret. Positivt lyfter bandet; negativt gröper ur det. | -15 till +15 dB (0) |
| **Q-faktor** | Ställer in hur brett bandet är. Låga värden formar ett brett område; höga värden smalnar in för kirurgiska, punktvisa ändringar. | 0,1 till 10 (1,0) |

| Förinställning | Vad den gör |
|---|---|
| **Presence** | En bred höjning i övre mellanregistret för klarhet och närvaro. En neutral utgångspunkt. |
| **Warmth** | En bred höjning i låg-mellanregistret som ger kropp och värme. |
| **Vocal Boost** | Höjer det centrala röstregistret för att föra fram röster. |
| **Cut Mud** | Gröper ur boxig låg-mellanregistergrumlighet för ett renare ljud. |
| **Tame Harsh** | En smal sänkning för att tämja en skarp, genomträngande topp. |
| **Punch** | En låg höjning som ger punch och slagkraft till lågregistret. |
| **Sub Boost** | En djup höjning i den allra nedersta delen för extra sub-bas-tyngd. |
| **Air** | En bred höjning i toppen för en öppen, luftig glans. |
| **Clarity** | Höjer höga mellanregistret för att ge definition och kant. |
| **De-Ess** | En smal sänkning i väsregistret för att tämja skarpa S-ljud. |
| **De-Boom** | Skär bort en dånande lågfrekvent uppbyggnad för ett tightare lågregister. |
| **Scoop** | En bred sänkning i mellanregistret för en urgröpt, modern ton. |

### Low Shelf (baskontroll och basförstärkning)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Frekvens** | Ställer in hörnet under vilket shelfen träder i kraft. Allt under den höjs eller sänks tillsammans. | 20 till 2000 Hz (200) |
| **Gain** | Hur mycket att lyfta eller sänka lågregistret. Positivt ger tyngd och värme; negativt tunnar ut det. | -15 till +15 dB (0) |

| Förinställning | Vad den gör |
|---|---|
| **Warmth** | En försiktig lyftning av lågregistret för värme och kropp. En neutral utgångspunkt. |
| **Bass Boost** | En solid höjning av basen för tyngd och punch. |
| **Fullness** | Fyller ut låg-mellanregistret för ett fylligare, rundare ljud. |
| **Trim Bass** | En blygsam sänkning för att lätta en bastung mix. |
| **Cut Lows** | En stark sänkning för att tunna ut eller de-dåna lågregistret. |
| **Big Bottom** | En stor höjning av lågregistret för maximal tyngd och mullrande. |

### High Shelf (diskantkontroll)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Frekvens** | Ställer in hörnet över vilket shelfen träder i kraft. Allt över den höjs eller sänks tillsammans. | 1 till 20 kHz (8 kHz) |
| **Gain** | Hur mycket att lyfta eller sänka det höga registret. Positivt ger ljushet och luft; negativt jämnar ut och mörknar. | -15 till +15 dB (0) |

| Förinställning | Vad den gör |
|---|---|
| **Presence** | En försiktig höjning av det höga registret för klarhet och detaljer. En neutral utgångspunkt. |
| **Air** | Öppnar upp den allra översta toppen för ett luftigt, öppet ljud. |
| **Bright** | En stark höjning för en skarp, ljus, framträdande ton. |
| **Soften** | En blygsam sänkning för att ta bort kanten från skarp diskant. |
| **Tame Highs** | En stark sänkning för att mörkna och jämna ut ett alltför ljust ljud. |
| **Sparkle** | En stor höjning av det översta registret för maximalt skimmer och glans. |

### Soft Clip (varm mättnad)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Drive** | Pressar signalen hårdare in i vågformaren. Låga mängder ger försiktig värme; höga mängder rundar topparna till tjock mättnad och grus. | 0 till 40 dB (0) |

| Förinställning | Vad den gör |
|---|---|
| **Warm** | En gnutta drive för försiktig, analog-liknande värme. |
| **Drive** | Märkbar mättnad som förtjockar och färgar ljudet. |
| **Crunch** | Tung drive med en hörbar crunchig kant. |
| **Fuzz** | Tjock, luddig distorsion. Topparna är hårt ihoppressade. |
| **Destroy** | Maximal drive. Aggressivt, fullt mättat grus. |

### Bit Crusher (retro lo-fi)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Bitdjup** | Ställer in hur många bitar som beskriver varje sampel. Färre bitar betyder grövre steg och mer kvantiseringsbrus, för ett crunchigt, grusigt digitalt ljud. | 1 till 16 bitar (16) |
| **Samplingsfrekvens** | Nedsamplar ljudet. Vid hundra procent är frekvensen orörd; sänk den för att hålla varje sampel längre, dämpa diskanten och lägga till en skarp, aliaskant. | 1 % till 100 % (100 %) |

| Förinställning | Vad den gör |
|---|---|
| **Vintage** | En subtil sänkning i kvalitet, som en tidig digital sampler. |
| **LoFi** | Klassisk 8-bitars lo-fi med halv frekvens. Kornig och retro. |
| **Crunch** | Tyngre krossning med en hörbar crunchig kant. |
| **Gritty** | Grov och grusig. Stegen mellan nivåerna är tydliga. |
| **Destroy** | Extrem reduktion. Skarp, trasig, knappt igenkännlig. |

### Ring Modulator (metalliska och robotliknande toner)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Bärvåg** | Ställer in frekvensen på tonen som signalen multipliceras med. Några hertz ger en tremolo-vaggning; högre frekvenser ger metalliska, klockliknande och robotliknande övertoner. | 1 till 4000 Hz (440) |
| **Mix** | Blandar in det modulerade ljudet med originalet. Vid noll procent hör du bara den torra signalen; vid hundra procent bara den fullt modulerade tonen. | 0 % till 100 % (0 %) |

| Förinställning | Vad den gör |
|---|---|
| **Tremolo** | En mycket låg bärvåg gör det till en amplitudtremolo som vaggar volymen. |
| **Robot** | En bärvåg i mellanregistret ger klingande övertoner för en klassisk robotrösteffekt. |
| **Metallic** | Täta, disharmoniska övertoner för en skarp, metallisk ton. |
| **Bell** | En högre bärvåg ger ljusa, klockliknande klingningar. |
| **Alien** | Helt våt med en hög bärvåg. Extrem, utomjordisk, knappt igenkännlig. |

### Tremolo (volymvaggning)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Hastighet** | Ställer in hur snabbt volymen pulserar. Långsammare hastigheter ger en mjuk gungning; snabbare hastigheter ger ett snabbt stamningsljud. | 0,1 till 20 Hz (5) |
| **Djup** | Ställer in hur mycket volymen sjunker vid varje puls. Vid noll procent är nivån stadig; vid hundra procent sjunker den hela vägen till tystnad. | 0 % till 100 % (0 %) |

| Förinställning | Vad den gör |
|---|---|
| **Gentle** | En långsam, ytlig gungning. Subtil rörelse utan att dra uppmärksamhet. |
| **Classic** | Den klassiska förstärkartremolon: en medelhastighet och måttligt djup. |
| **Deep** | En stark, djup puls som nästan sjunker till tystnad varje cykel. |
| **Fast** | Ett snabbt fladdrande för en skimrande, nervös känsla. |
| **Chop** | Snabbt och fullt djup. En hård, stamnande huggning. |

### Delay (eko)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Tid** | Ställer in mellanrummet före varje eko. Korta tider ger ett tight slapback; längre tider sprider upprepningarna längre isär. | 0,01 till 2 s (0,25) |
| **Feedback** | Ställer in hur mycket av varje eko som matas tillbaka. Låga värden ger en enda upprepning; högre värden bygger en lång, avtonande serie ekon. | 0 till 0,95 (0,4) |
| **Mix** | Blandar in ekona med originalet. Vid noll procent hör du bara den torra signalen; vid hundra procent bara ekona. | 0 % till 100 % (0 %) |

| Förinställning | Vad den gör |
|---|---|
| **Slapback** | Ett enda kort eko, tight mot originalet. Rockabilly och sångdubblering. |
| **Echo** | Det klassiska ekot: en tydlig upprepning med några avtonande svansar. |
| **Ping** | En snabb, studsande upprepning som ger rytmisk rörelse. |
| **Ambient** | Längre, mjukare upprepningar som sköljer ut i en rymlig svans. |
| **Dub** | Hög feedback för långa, dubbiga kaskader av eko. |
| **Cavern** | Långa, djupa upprepningar, som ljud som ekar genom en enorm rymd. |

### Stereo Width (smalna eller bredda)

| Kontroll | Vad den gör | Intervall (standard) |
|---|---|---|
| **Bredd** | Smalnar eller breddar stereobilden. Noll procent kollapsar till mono, hundra procent lämnar den orörd, och högre värden trycker sidorna bredare. Påverkar endast stereospår på målet Alla kanaler. | 0 % till 200 % (100 %) |

| Förinställning | Vad den gör |
|---|---|
| **Wide** | En försiktig breddning som öppnar upp stereobilden. En neutral utgångspunkt. |
| **Wider** | En starkare spridning för ett stort, uppslukande stereofält. |
| **Max** | Maximal bredd. Mycket bred, men se upp för mono-kompatibilitetsproblem. |
| **Narrow** | Drar in sidorna för en tightare, mer centrerad bild. |
| **Focused** | Nästan centrerad, med bara en antydan av stereo. |
| **Mono** | Helt kollapsad till mono. Båda högtalarna spelar samma signal. |

## Hur allt fungerar under huven (enkel version)

- **Motorer:** du väljer en i Inställningar > Ljudspelare > Uppspelningsmotor: **Standard** (system), **Universal** (FFmpeg) eller **Sound FX** (**BASS™-motorn** från [Un4seen Developments](https://www.un4seen.com/)). Motorn du väljer avgör vilka format som spelas, och effekterna, equalizern och DSP-kedjan körs endast i Sound FX-motorn.
- **Format:** BASS™-motorn lägger till FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus och modul- (tracker-) musik utöver system- och FFmpeg-formaten.
- **Effekter:** equalizern, kompressorn och de flesta effekter använder BASS™-effekttilläggen. Freeverb är Freeverb-reverbet. Chorus, Flanger och Distorsion använder klassiska DirectX-liknande effekter med sina egna kontroller.
- **Volymnormalisering:** en live **EBU R128**-volymnivellerare (volymstandarden som används i broadcast och streaming).
- **Crossfeed:** **bs2b-crossfeeden (Bauer)**, som körs inuti BASS™-motorn.
- **DSP-kedja:** dina anpassade block, tillämpade i exakt den ordning du ställer in, på alla kanaler eller bara en sida.
- **Utgång:** du kan ställa in samplingsfrekvensen, kanalantalet och buffertstorleken för att matcha din utrustning.

Eftersom allt detta körs live medan musiken spelas är effekterna:

- Fungerar i **realtid** på allt, inklusive molnfiler, streams och modulmusik.
- **Ändrar eller sparar aldrig om** dina filer. Slå av en effekt så återkommer originalet.
- **Kommer ihåg dina inställningar** för varje effekt.
- Kan **blandas och matchas** fritt, eftersom var och en är separat.

## Enkla recept att prova

**Vardagslyssnande**

- **Mer bas, rent:** Equalizer > Bass Booster, sänk sedan Förförstärkaren 1 till 2 dB. Eller lägg till en DSP Low Shelf på Bass Boost.
- **Jämn volym över en blandad spellista:** Volymnormalisering > Standard, plus Kompressor > Soft.
- **Försiktig övergripande polering:** Kompressor > Transparent, plus Volymnormalisering > Light.
- **Tydligare sång:** Equalizer > Vocal Booster, eller ett DSP Peaking-block på Vocal Boost.
- **Fylligare ljud på små telefonhögtalare:** Equalizer > Small Speakers.

**Hörlurar**

- **Trevligare, mindre tröttsamt i hörlurar:** Crossfeed > Chu Moy eller Jan Meier.
- **Bredare ljud i hörlurar:** DSP Stereo Width > Wide, plus Crossfeed > Chu Moy.
- **Fixa hårt panorerade 1960- och 1970-talsskivor:** Crossfeed > Vintage Stereo.
- **Lite luft och rymd:** Freeverb > Ambience, hållen låg, plus Crossfeed > Subtle.

**Tysta stunder och talat ljud**

- **Tyst lyssnande sent på kvällen:** Volymnormalisering > Night, plus Kompressor > Late Night.
- **Poddar och ljudböcker:** Kompressor > Voice / Podcast, plus Equalizer > Spoken Word.
- **Högsta, jämnaste ljud i en bullrig bil:** Volymnormalisering > Strong, plus Kompressor > Heavy.

**Fixa problem**

- **Tämja en skarp, ljus inspelning:** Equalizer > Treble Reducer, eller ett DSP Peaking-block på Tame Harsh.
- **Ta bort elektriskt brum:** DSP-kedja > Notch > Mains Hum 60 (eller Mains Hum 50 i Europa).
- **Tightare, renare bas:** DSP High Pass > Tighten, för att skära bort det dånande lågregistret.
- **Mindre dån i en bastung mix:** DSP Low Shelf > Trim Bass, eller Peaking > De-Boom.

**Kreativt och kul**

- **Varm, rymlig känsla:** Freeverb > Hall, hållen låg.
- **Drömska, rymliga gitarrer:** Chorus > Wide, plus Eko > Long.
- **Retro lo-fi:** DSP-kedja > Bit Crusher (LoFi) in i Soft Clip (Warm).
- **Funkig rörelse på elektroniska spår:** Auto Wah > Funky, eller Phaser > Fast.
- **Klassiskt jetplansvep:** Flanger > Jet.

## FAQ

{{% details title="Vilken ljudmotor använder Flacbox?" closed="true" %}}
Du väljer en Uppspelningsmotor i Inställningar > Ljudspelare: Standard (Apples systemmotor), Universal (FFmpeg-motorn) eller Sound FX (BASS™-motorn från Un4seen Developments, un4seen.com). Motorn du väljer avgör vilka filformat som spelas. Sound FX är den som spelar extra format som FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus och MOD- eller trackermusik, och den är den enda motorn som ger liveeffekterna, 10-bands equalizern och DSP-kedjan. För att använda effekterna, ställ in Uppspelningsmotorn på Sound FX.
{{% /details %}}

{{% details title="Kan Flacbox spela MOD, XM, IT och annan tracker- eller modulmusik?" closed="true" %}}
Ja. BASS™-motorn har en inbyggd modulspelare som laddar MOD-, XM-, IT-, S3M-, MTM-, UMX- och MO3-filer och bygger om låten live från dess mönster och instrumentljud, så som trackermusik är tänkt att spelas. Vanliga iPhone-spelare kan inte göra detta. Effekter och equalizern fungerar på modulmusik också.
{{% /details %}}

{{% details title="Stöder Flacbox DSD och högupplösta filer?" closed="true" %}}
Ja. Flacbox spelar DSD-filer (DSF och DFF) genom BASS™-motorn med DSD över PCM så att de fungerar på vanlig utgångshårdvara, plus FLAC, WavPack, Monkey's Audio (APE), Musepack och TrueAudio för förlustfri uppspelning.
{{% /details %}}

{{% details title="Vilka ljudeffekter har Flacbox?" closed="true" %}}
En 10-bands equalizer, Volymnormalisering, Kompressor, Freeverb, Auto Wah, Phaser, Flanger, Eko, Chorus, Distorsion, Rotate och Crossfeed, plus en bygg-din-egen DSP-kedja med filter, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay och stereobredd. Var och en är separat och kan kombineras med de andra.
{{% /details %}}

{{% details title="Vad är en förinställning?" closed="true" %}}
En förinställning är en färdig inställning för en effekt. Istället för att flytta reglage själv trycker du på en förinställning och ljudet ändras för att matcha. Varje effekt i Flacbox har flera förinställningar, och den här guiden listar vad var och en gör. Om du flyttar ett reglage efter att ha valt en förinställning visar effekten «Manuell» för att tala om att den nu använder dina egna värden.
{{% /details %}}

{{% details title="Hur öppnar jag ljudeffekterna i Flacbox?" closed="true" %}}
Öppna spelaren Spelas nu, tryck på knappen ⋯ (Fler åtgärder) och välj Ljudeffekter. Eller gå till Inställningar > Ljudspelare > Ljudeffekter. Tryck på en effekt, slå på dess brytare och välj en förinställning, eller öppna reglagen för att finjustera.
{{% /details %}}

{{% details title="Var är equalizern, och vilka är de bästa inställningarna?" closed="true" %}}
Gå till Inställningar > Ljudspelare > Ljudequalizer. Den har 10 band från 32 Hz till 16 kHz, vart och ett från -12 till +12 dB, plus en Förförstärkare på -24 till +24 dB och 22 förinställningar. För mer bas, använd Bass Booster. För tydligare röster, använd Vocal Booster eller Pop. För ett ljusare ljud, använd Treble Booster. Justera sedan enskilda band efter smak.
{{% /details %}}

{{% details title="Hur förstärker jag basen i Flacbox?" closed="true" %}}
Två enkla sätt. I Ljudequalizern, välj Bass Booster (eller höj banden 32 Hz och 64 Hz några dB). Eller, i Signalbehandling, lägg till ett Low Shelf-block inställt på Bass Boost. I båda fallen, sänk Förförstärkaren eller lägg till ett Gain-block 1 till 2 dB så att basen förblir ren och inte distorderar.
{{% /details %}}

{{% details title="Vilken equalizer-förinställning är bäst för min musik?" closed="true" %}}
Rock och Electronic ger energi med kraftiga bastoner och diskant. Acoustic, Jazz och Classical förblir varma och naturliga. Pop och Vocal Booster för fram röster. Bass Booster och Hip-Hop ger tyngd. Deep och Loudness låter fylligare vid låg volym. Börja med den som matchar din genre, finjustera sedan.
{{% /details %}}

{{% details title="Vad är Volymnormalisering, och hur skiljer det sig från ReplayGain?" closed="true" %}}
Det gör att varje spår spelas på ungefär samma volym. Det mäter den verkliga volymen med EBU R128-standarden (i LUFS, som streamingtjänster) och justerar varje spår mot ditt mål, med en max-boost-gräns. Till skillnad från ReplayGain behöver det inga taggar i dina filer och fungerar på vilken källa som helst, live, utan att ändra ljudet. Förinställningar: Light, Standard, Strong och Night.
{{% /details %}}

{{% details title="Vad är Crossfeed, och bör jag använda det?" closed="true" %}}
Crossfeed blandar lite av vänster och höger kanaler tillsammans så att hörlurar känns mer som riktiga högtalare och mindre som att ljudet sitter fast i ditt huvud. Det är endast för hörlurar, så slå av det för högtalare. Flacbox använder bs2b-metoden (Bauer), med förinställningar som Chu Moy och Jan Meier.
{{% /details %}}

{{% details title="Vad är skillnaden mellan Kompressorn och Volymnormalisering?" closed="true" %}}
Volymnormalisering matchar volymen mellan olika låtar. Kompressorn jämnar ut de höga och tysta partierna inuti en enda låt. De löser olika problem och fungerar bra tillsammans, särskilt i en bil eller på en bullrig plats.
{{% /details %}}

{{% details title="Vad är Signalbehandlings- (DSP-) kedjan?" closed="true" %}}
Det är ett bygg-din-egen-rack i Inställningar > Ljudspelare > Signalbehandling. Lägg till block som filter, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay och stereobredd, sätt dem i vilken ordning som helst, slå på eller av var och en, och rikta kedjan mot alla kanaler, vänster eller höger. Eftersom ordningen spelar roll kan du designa exakt det ljud du vill ha.
{{% /details %}}

{{% details title="Vad är skillnaden mellan Equalizern, effekterna och DSP-kedjan?" closed="true" %}}
Equalizern är en enkel 10-bands tonkontroll. Ljudeffekterna är färdiga verktyg (kompressor, reverb, eko och så vidare) med förinställningar. DSP-kedjan är där du bygger din egen effektordning från enskilda block. Du kan köra alla tre samtidigt.
{{% /details %}}

{{% details title="Ändrar eller skadar effekterna mina musikfiler?" closed="true" %}}
Nej. Allt tillämpas live medan musiken spelas. Dina filer ändras eller sparas aldrig om. Slå av en effekt så återkommer originalljudet på en gång.
{{% /details %}}

{{% details title="Kan jag använda mer än en effekt samtidigt?" closed="true" %}}
Ja. Varje effekt har sin egen brytare och det finns ingen huvudbrytare, så vilken kombination som helst fungerar. Till exempel Volymnormalisering plus Kompressor för jämnt lyssnande, eller Freeverb plus Crossfeed i hörlurar, med equalizern ovanpå.
{{% /details %}}

{{% details title="Varför är effektkontrollerna nedtonade?" closed="true" %}}
Effekten är avstängd. Slå på dess brytare högst upp i redigeraren för att använda kontrollerna. Varje effekt är avstängd som standard.
{{% /details %}}

{{% details title="Vad betyder etiketten Manuell?" closed="true" %}}
Det betyder att du flyttade ett reglage bort från en förinställning, så effekten använder nu dina egna anpassade värden istället för en namngiven förinställning. Varje reglage har en återställningsknapp, och att välja en förinställning igen ersätter dina manuella värden.
{{% /details %}}

{{% details title="Kan jag spara och dela mina equalizer-förinställningar?" closed="true" %}}
Ja. Förutom de 22 inbyggda förinställningarna kan du göra dina egna, ändra ordning på dem och exportera eller importera dem för att flytta dina inställningar till en annan enhet.
{{% /details %}}

{{% details title="Fungerar effekterna med CarPlay, streaming och bakgrundsuppspelning?" closed="true" %}}
Ja. Effekterna körs inuti BASS™-motorn, så de tillämpas på lokala filer, molndiskar, mediaservrar, streams och modulmusik, och de fortsätter att fungera under CarPlay och bakgrundsuppspelning.
{{% /details %}}

{{% details title="Kan jag ändra ljudutgångens kvalitet?" closed="true" %}}
Ja. I Inställningar > Ljudspelare kan du ställa in utgångssamplingsfrekvensen, antalet kanaler och buffertstorleken för att matcha dina hörlurar, högtalare eller DAC.
{{% /details %}}

{{% details title="Vad är en bra startuppsättning för hörlurar?" closed="true" %}}
Slå på Volymnormalisering (Standard), lägg till en lätt Kompressor (Soft), välj en equalizer-förinställning du gillar och slå på Crossfeed (Chu Moy eller Jan Meier). Lämna reverb, eko och distorsion av om du inte vill ha ett kreativt ljud.
{{% /details %}}

---

*BASS är ett varumärke som tillhör Un4seen Developments Ltd. Se [un4seen.com](https://www.un4seen.com/). Crossfeed använder bs2b-algoritmen (Bauer stereophonic-to-binaural); se [bs2b-projektsidan](https://bs2b.sourceforge.net/).*
