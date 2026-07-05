---
title: "Evermusic 8.7: äkta sömlös uppspelning, ljudeffekter, volymnormalisering, omdesignad equalizer"
date: 2026-07-05
description: "Evermusic 8.7 för iPhone, iPad och Mac lägger till äkta sömlös uppspelning, fem studioljudeffekter (efterklang, delay, distorsion, kompressor, crossfeed), EBU R128-volymnormalisering, en omdesignad 10-bands equalizer med import/export av förval, en ombyggd AVAudioEngine-strömningsmotor med stöd för FLAC och Ogg Vorbis, och snabbare, mer exakt CarPlay och Spelas nu."
keywords: ["Evermusic 8.7", "Evermusic-uppdatering", "äkta sömlös uppspelning iPhone", "gapless musikspelare iOS", "sömlös uppspelning CarPlay", "ljudeffekter musikspelare iPhone", "efterklang delay distorsion kompressor crossfeed iOS", "crossfeed hörlurar iOS", "volymnormalisering iPhone", "ljudstyrkenormalisering musikspelare", "EBU R128-normalisering iOS", "replay gain-alternativ iPhone", "10-bands equalizer iPhone", "grafisk equalizer iOS-app", "equalizer-förval import export", "FLAC-spelare iPhone", "Ogg Vorbis-spelare iOS", "förlustfri musikspelare iPhone 2026", "AVAudioEngine musikspelare", "CarPlay musikspelare iPhone", "Spelas nu låsskärm noggrannhet", "molnmusikspelare iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Sömlös uppspelning", "Ljudeffekter", "Efterklang", "Delay", "Distorsion", "Kompressor", "Crossfeed", "Volymnormalisering", "EBU R128", "Equalizer", "FLAC", "Ogg Vorbis", "CarPlay", "Spelas nu", "Liquid Glass", "Nyheter"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Sammanfattning:** [Evermusic 8.7](/products/evermusic) är en ljudkvalitetsutgåva för iPhone, iPad och Mac. Den levererar **äkta sömlös uppspelning** (inga pauser, klick eller knäppar mellan spår), en full uppsättning **studioljudeffekter** — efterklang, delay, distorsion, kompressor och crossfeed — och **EBU R128-volymnormalisering** som håller ljudstyrkan jämn från låt till låt utan ReplayGain-taggar. **10-bands equalizern** är omdesignad med nya reglage, snabbare byte av förval, egna förval som du kan importera och exportera, samt en bättre layout i liggande läge och på iPad. Under huven förbättrar en **ombyggd AVAudioEngine-strömningsmotor** tillförlitligheten och formatstödet, inklusive **FLAC** och **Ogg Vorbis**. **CarPlay** och **Spelas nu** är snabbare och mer exakta på låsskärmen, i bilen och från hörlursfjärrkontroller.

---

## Hej allihopa!

Evermusic 8.7 finns att ladda ner. Den här uppdateringen handlar helt om hur din musik *låter*. Vi byggde om uppspelningsmotorn för äkta sömlös uppspelning, lade till en svit studiokvalitativa ljudeffekter, införde ljudstyrkenormalisering och designade om equalizern från reglagen och uppåt. Allt är insvept i Apples nya **Liquid Glass**-design.

[Ladda ner Evermusic 8.7 från App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) eller uppdatera från din befintliga version. Evermusic är en gratis nedladdning med valfria uppgraderingar i appen.

## Äkta sömlös uppspelning

Sömlös uppspelning innebär att tystnaden mellan två spår är borta. Ingen paus, inget klick, ingen knäpp — den aktuella låten flyter rakt in i nästa. Det spelar störst roll för musik som skapats för att höras som en helhet: **liveinspelningar, DJ-mixar, klassiska verk och konceptalbum** där ett spår tonar direkt in i ett annat.

Så här ändrades det tekniskt. Evermusics ljudmotor håller två spår i spel samtidigt: det du hör och det nästa i kön. Medan det aktuella spåret spelas **hämtas, avkodas och förbuffras** nästa spår redan i bakgrunden. När det aktuella spåret når sitt slut lämnar motorn över till nästa spår **inuti spelaren, inte inuti ljudströmmen**. Utsignalens renderingsloop fortsätter hämta ljudsampel från en sammanhängande ringbuffert utan att någonsin stanna, så lyssnaren hör aldrig en gräns. Bytet sker mellan sampel, vilket är precis därför det inte finns något hörbart glapp.

Detta fungerar likadant oavsett om filen finns på din enhet, i molnet eller på en mediaserver — förbuffringen börjar bara lite tidigare för fjärrkällor.

## Studioljudeffekter

Evermusic 8.7 lägger till fem ljudeffekter i realtid som du kan stapla ovanpå din musik. Var och en körs som en inbyggd ljudbearbetningsnod i uppspelningsmotorn, så den tillämpas på allt du spelar — lokala filer, molnströmmar och internetradio — utan omkodning.

Varje effekt levereras med ett **kurerat bibliotek av förval** för att ge dig ett bra ljud med ett tryck, och Evermusic **kommer ihåg dina exakta inställningar** mellan sessioner. Justera valfri kontroll så växlar effekten till läget **Manuell**, så du alltid vet när du har rört dig bort från ett förval.

### Efterklang

Tillför en känsla av rum, från ett tätt rum till en katedral. Byggd på Apples `AVAudioUnitReverb` erbjuder den **13 rumsförval** (Small Room, Medium Hall, Plate, Cathedral med flera) plus en **wet/dry-mix**-kontroll från 0 till 100 % så att du bestämmer hur mycket rum som ska läggas till.

### Delay (eko)

Ett klassiskt eko med **10 förval** — Slapback, Tape Echo, Dub, Ambient och andra. Du kan ställa in **delaytiden** (upp till 2 sekunder), **feedback** (hur många upprepningar), en **lågpass-cutoff** för att värma upp upprepningarna, och **wet/dry-mixen**.

### Distorsion

Från subtilt grus till full lo-fi-förstörelse, driven av `AVAudioUnitDistortion` med **22 karaktärsförval** (Bit Brush, Cellphone Concert, Radio Tower med flera), en **pre-gain**-drivkontroll och en wet/dry-mix så att du kan blanda tillbaka effekten i den rena signalen.

### Kompressor

En dynamikprocessor (Apples `AUDynamicsProcessor`) som jämnar ut höga och tysta partier. Den ger den fullständiga professionella kontrolluppsättningen — **threshold, ratio/headroom, attack, release, expansion och makeup gain** — med **10 förval** avstämda för verkliga situationer: Voice / Podcast, Late Night, Movie Dialog, Streaming Match och Maximum Loudness bland dem.

### Crossfeed

Crossfeed får hörlurslyssning att låta mer naturligt genom att blanda in lite av vänsterkanalen i höger och tvärtom, på det sätt dina öron hör riktiga högtalare. Den är byggd på den välkända algoritmen **Bauer stereophonic-to-binaural (bs2b)**, med kontroll över **crossfeed-nivån** och **cutoff-frekvensen**, och **6 förval** inklusive de audiofilfavoriterna *Chu Moy*- och *Jan Meier*-inställningarna. Den är särskilt bra på äldre, hårt panorerade stereomixar från 1960- och 1970-talet.

## Volymnormalisering

Har du någonsin byggt en spellista där ett spår dånar och nästa är en viskning? Volymnormalisering fixar det. Evermusic 8.7 använder **EBU R128-ljudstyrkemätning** (samma ITU-R BS.1770-standard som används i rundradio och av strömningstjänster) för att mäta varje spårs verkliga upplevda ljudstyrka och varsamt styra den mot ett jämnt mål.

Till skillnad från ReplayGain kräver den **inga** taggar i dina filer och den **ändrar inte** ditt ljud. Den fungerar i realtid på allt du spelar, inklusive molnströmmar och liveradio, och den återställs rent när du spolar eller byter spår.

Fyra förval täcker de vanliga fallen:

- **Light** — mild nivellering (mål −20 LUFS).
- **Standard** — standardvalet, strömningsliknande ljudstyrka (mål −16 LUFS, upp till +12 dB lyft för tysta spår).
- **Strong** — aggressiv matchning för mycket blandade bibliotek (mål −14 LUFS).
- **Night** — tystare och jämn för lågvolymlyssning på kvällen (mål −23 LUFS).

Du behöver inte längre sträcka dig efter volymen mellan låtar.

## Omdesignad equalizer

Evermusics **10-bands grafiska equalizer** fick en fullständig omdesign. Banden täcker **32 Hz till 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), var och en justerbar från **−12 dB till +12 dB** i fina steg om 0,1 dB, med en **förförstärkning** från −24 dB till +24 dB för att förhindra klippning när du höjer.

Vad som är nytt i 8.7:

- **Nya reglage** — precisa, responsiva kontroller som anammar det inbyggda iOS 26-systemreglageutseendet och **Liquid Glass**-materialet.
- **Snabbare, mjukare byte av förval** — hoppa mellan förval direkt, med en omdesignad horisontell förvalsrad i stående läge och en vertikal förvalskolumn i liggande läge.
- **Bättre layout i liggande läge och på iPad** — reglagen och förvalsväljaren omorganiseras för att använda den extra bredden istället för att trängas ihop i en telefonstor kolumn.
- **Egna förval** — skapa och spara egna kurvor, ändra ordning på dem och **importera och exportera** förval som `.eqp`-filer för att flytta dem mellan enheter eller dela dem.

Equalizern körs inbyggt i motorn (`AVAudioUnitEQ`), så den tillämpas på varje källa, och den fungerar även över AirPlay, Chromecast och CarPlay där det stöds.

## Ombyggd uppspelningsmotor

Under huven körs Evermusic 8.7 på en **ombyggd strömningsmotor** byggd på Apples `AVAudioEngine` med en anpassad renderingspipeline. Det är detta som gör den sömlösa överlämningen, effektkedjan och equalizern möjliga, och det gör också vardaglig uppspelning mer tillförlitlig.

- **Förbättrat formatstöd** — inklusive **FLAC** (via Core Audio) och **Ogg Vorbis** (via `libvorbisfile`), vid sidan av MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF med flera.
- **Smartare buffring** — en adaptiv förbuffert skalas med din anslutning, med en sammanhängande ringbuffert som matar utsignalen så att korta nätverkshack inte blir till avbrott.
- **Automatisk återhämtning** — en ombuffringsstatusmaskin och omförsökslogik med backoff återupptar uppspelningen rent efter ett svagt-signal-ögonblick istället för att stanna spåret.
- **Färre avbrott** — samma motor driver lokala filer, molnströmmar, mediaservrar och internetradio, så beteendet är konsekvent överallt.

## Spelas nu och CarPlay

Skärmarna du faktiskt tittar på medan du lyssnar — **låsskärmen**, **CarPlay** och din bils eller dina hörlurars fjärrknappar — är mer exakta och snabbare i 8.7.

- **Mer exakt Spelas nu-info.** Evermusic fångar spelarens tillstånd under ett lås innan det publiceras, så att titel, förfluten tid, längd och spela/pausa-tillstånd aldrig kan motsäga varandra på låsskärmen eller i bilen. Buffrings- och laddningstillstånd rapporteras nu korrekt istället för att visa "spelas" medan ett spår fortfarande hämtas.
- **Tillförlitliga fjärrkontroller.** Spela, pausa, nästa, föregående, spola, hoppa över, blanda, upprepa och uppspelningshastighet svarar alla konsekvent från hörlursknappar, bilkontroller och låsskärmen, drivet av `MPRemoteCommandCenter`.
- **Snabbare CarPlay-omslag.** Albumomslag laddas nu flera gånger snabbare i långa listor (batch-takt sänkt från 1,0 s till 0,25 s, med den första synliga skärmen laddad omedelbart), och det syns nu i de kompakta iOS 26 CarPlay-listraderna som tidigare inte visade något omslag.
- **CarPlay-sorterings- och stabilitetsfixar.** Snabbare sortering på stora bibliotek och härdning mot kantfallskrascher vid rullning i långa listor.
- **Begränsade metadatauppdateringar.** Spelas nu- och fjärrkommandouppdateringar begränsas så att snabba ändringar inte längre översvämmar systemet, vilket håller låsskärms- och CarPlay-kontroller responsiva.

## Övriga förbättringar

- **Liquid Glass-designförfiningar** i hela appen — genomskinliga ytor, mjukare animationer och förfinade kontroller på iOS, iPadOS och macOS.
- **Nya hemskärmswidgetar** med förbättrad uppdateringslogik som håller dem synkroniserade utan att dränera extra batteri.
- Fixar för senaste iOS-utgåvorna.
- Lokaliseringsfixar över flera språk.
- Många mindre förbättringar baserade på dina mejl och App Store-recensioner.

## Varför den här uppdateringen är viktig

Evermusic 8.7 är byggd kring en enda idé: **din musik ska låta så bra som möjligt, från vilken källa som helst.**

1. **Hela album, som avsett.** Äkta sömlös uppspelning innebär att live-set, DJ-mixar och konceptalbum äntligen spelas så som artisten mastrade dem.
2. **En studio i fickan.** Efterklang, delay, distorsion, kompressor, crossfeed, en omdesignad equalizer och ljudstyrkenormalisering ger dig verklig kontroll över ditt ljud, inte bara en på/av-knapp.
3. **Samma upplevelse överallt.** Lokala filer, molnenheter, mediaservrar och internetradio körs alla genom samma ombyggda motor, med exakt Spelas nu och en snabbare CarPlay ovanpå.

## Skaffa Evermusic 8.7

[**Ladda ner Evermusic från App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) eller uppdatera inifrån App Store. Evermusic är en gratis nedladdning med valfria uppgraderingar i appen för avancerade funktioner.

Om du gillar appen, lämna gärna ett betyg på App Store — det hjälper verkligen. Har du feedback eller stötte du på ett problem? Mejla oss på **support@everappz.com**. Vi läser varje meddelande.

## Vanliga frågor

{{% details title="Vad är nytt i Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 lägger till äkta sömlös uppspelning, fem studioljudeffekter (efterklang, delay, distorsion, kompressor och crossfeed), EBU R128-volymnormalisering, en omdesignad 10-bands equalizer med egna förval och import/export, en ombyggd AVAudioEngine-strömningsmotor med förbättrat formatstöd (inklusive FLAC och Ogg Vorbis), snabbare och mer exakt CarPlay och Spelas nu, Liquid Glass-designuppdateringar, uppfräschade hemskärmswidgetar samt fel- och lokaliseringsfixar.
{{% /details %}}

{{% details title="Har Evermusic äkta sömlös uppspelning?" closed="true" %}}
Ja. Från och med Evermusic 8.7 är uppspelningen verkligt sömlös: det finns ingen paus, inget klick eller knäpp mellan spår. Motorn förbuffrar och avkodar nästa spår medan det aktuella spelas och lämnar över mellan ljudsampel på en sammanhängande ringbuffert, så att övergången är ohörbar. Den fungerar för lokala filer, molnströmmar och mediaservrar, och den är idealisk för livealbum, DJ-mixar och konceptalbum.
{{% /details %}}

{{% details title="Vilka ljudeffekter innehåller Evermusic 8.7?" closed="true" %}}
Fem effekter i realtid: **efterklang** (13 rumsförval, wet/dry-mix), **delay/eko** (10 förval med delaytid, feedback, lågpass och mix), **distorsion** (22 karaktärsförval med pre-gain och mix), **kompressor** (en fullständig dynamikprocessor med threshold, ratio, attack, release, expansion och makeup gain, plus 10 förval) och **crossfeed** (Bauer bs2b-hörlurscrossfeed med nivå- och cutoff-kontroller och 6 förval). Varje effekt levereras med kurerade förval, och dina egna inställningar kommer ihåg mellan sessioner.
{{% /details %}}

{{% details title="Vad är crossfeed och varför skulle jag använda det?" closed="true" %}}
Crossfeed blandar in en liten, filtrerad mängd av varje stereokanal i den andra, på det sätt dina öron naturligt hör riktiga högtalare i ett rum. I hörlurar minskar detta den överdrivna, "inuti-huvudet"-separationen hos hårt panorerade inspelningar och gör långa lyssningar bekvämare. Evermusic använder den välkända algoritmen Bauer stereophonic-to-binaural (bs2b) och innehåller förval som Chu Moy och Jan Meier. Den är särskilt effektiv på äldre stereomixar från 1960- och 1970-talet.
{{% /details %}}

{{% details title="Hur fungerar volymnormalisering i Evermusic?" closed="true" %}}
Evermusic 8.7 mäter varje spårs upplevda ljudstyrka med EBU R128-standarden (ITU-R BS.1770) i realtid och justerar varsamt nivån mot ett jämnt mål så att spår inte hoppar i volym. Den kräver inga ReplayGain-taggar och ändrar inte dina filer. Fyra förval finns tillgängliga — Light (−20 LUFS), Standard (−16 LUFS), Strong (−14 LUFS) och Night (−23 LUFS) — och normaliseringen återställs rent när du spolar eller byter spår.
{{% /details %}}

{{% details title="Är Evermusics volymnormalisering samma sak som ReplayGain?" closed="true" %}}
Den uppnår samma mål — jämn ljudstyrka mellan spår — men fungerar annorlunda. ReplayGain förlitar sig på ljudstyrketaggar lagrade inuti dina filer. Evermusics normaliserare mäter ljudstyrka live med EBU R128, så den fungerar på vilken källa som helst, inklusive molnströmmar och internetradio, även när filerna inte har några taggar alls.
{{% /details %}}

{{% details title="Hur många band har Evermusics equalizer, och kan jag skapa egna förval?" closed="true" %}}
Evermusics equalizer är en 10-bands grafisk equalizer som täcker 32 Hz till 16 kHz, med varje band justerbart från −12 dB till +12 dB i steg om 0,1 dB och en förförstärkning från −24 dB till +24 dB. Den innehåller inbyggda förval, låter dig skapa och spara egna förval och stöder import och export av förval som .eqp-filer så att du kan flytta eller dela dem mellan enheter.
{{% /details %}}

{{% details title="Vad ändrades i Evermusic 8.7-equalizern?" closed="true" %}}
Equalizern designades om med nya, mer precisa reglage som anammar iOS 26-systemreglaget och Liquid Glass-utseendet, snabbare och mjukare byte av förval samt en bättre layout i liggande läge och på iPad (en horisontell förvalsrad i stående läge och en vertikal förvalskolumn i liggande läge). Egna förval och .eqp-import/export stöds.
{{% /details %}}

{{% details title="Stöder Evermusic 8.7 FLAC och Ogg Vorbis?" closed="true" %}}
Ja. Den ombyggda motorn spelar FLAC (via Core Audio) och Ogg Vorbis (via libvorbisfile), tillsammans med MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF med flera, från lokala filer, molnenheter och mediaservrar.
{{% /details %}}

{{% details title="Vad förbättrades i CarPlay och på låsskärmen?" closed="true" %}}
CarPlay-albumomslag laddas flera gånger snabbare i långa listor och syns nu i de kompakta iOS 26-listraderna som tidigare inte visade något. Spelas nu-information på låsskärmen och i CarPlay är mer exakt — titel, förfluten tid, längd och spela/pausa-tillstånd fångas tillsammans så att de inte kan motsäga varandra, och buffringstillstånd rapporteras korrekt. Fjärrkontroller (spela, pausa, nästa, föregående, spola, blanda, upprepa, hastighet) svarar tillförlitligt från hörlurar och bilen, och CarPlay-sortering på stora bibliotek är snabbare.
{{% /details %}}

{{% details title="Fungerar ljudeffekterna och equalizern med molnströmning och CarPlay?" closed="true" %}}
Ja. Effekterna, equalizern och volymnormaliseringen körs inbyggt inuti uppspelningsmotorn, så de tillämpas på allt Evermusic spelar — lokala filer, molnenheter, mediaservrar och internetradio — och de fortsätter att fungera under CarPlay-uppspelning och, där det stöds, över AirPlay och Chromecast.
{{% /details %}}

{{% details title="Är Evermusic 8.7 gratis att uppdatera, och vilka enheter stöds?" closed="true" %}}
Ja. Evermusic är en gratis nedladdning från App Store, och 8.7 är en gratis uppdatering för befintliga användare, med valfria uppgraderingar i appen för avancerade funktioner. Den körs på iPhone, iPad och Mac. CarPlay kräver ett CarPlay-kompatibelt fordon eller huvudenhet.
{{% /details %}}
