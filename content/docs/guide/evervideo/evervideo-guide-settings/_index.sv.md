---
title: "Inställningar"
date: 2020-02-01
lastmod: 2026-06-01
description: "Utforska varje inställning i Evervideo — Mediaspelare (bild-i-bild, hårdvara H.264 / HEVC-avkodning, videoequalizer, skalning, rotation, VR-viewport), Ljud (equalizer, samplingshastighet, kanaler, IO-buffer, blandat läge), Undertexter (primär / sekundär, teckensnitt, extern fil, libass), Mediebibliotek, Filhanterare, Wi-Fi Drive, Widgets, Personalisering, Språk, Lösenord, Säkerhetskopia och återställning — för iPhone, iPad och Mac."
keywords: [
  "Evervideo inställningar", "videospelarkonfiguration", "Premium-uppgradering Evervideo",
  "bild-i-bild-inställningar", "videoequalizer-inställningar",
  "videoskalningsläge", "videorotation", "hårdvaruavkodare iPhone",
  "undertextsinställningar", "sekundär undertext iOS", "libass-inställningar",
  "extern undertextsfil", "undertextsteckensnitt",
  "audioequalizer-inställningar", "samplingshastighet för audioutgång",
  "audiokanaler", "IO-bufferttid", "blandat ljudläge",
  "WiFi Drive video", "Evervideo widgets",
  "Evervideo säkerhetskopia återställning", "Evervideo lösenord",
  "Evervideo språk", "Evervideo personalisering"
]
tags: ["guide", "evervideo", "settings"]
readingTime: 16
---


Inställningsskärmen är kontrollcentret för Evervideo. Härifrån kan du uppgradera till Premium, konfigurera video- och ljudmotorer (systemkodekar eller FFmpeg), hantera bild-i-bild, ställa in undertexter (primära, sekundära, libass, externa filer, teckensnitt), organisera mediebiblioteket, ställa in filhanteraren, aktivera widgets för hemskärmen, säkerhetskopiera dina data och komma åt hjälp och juridisk information. Avsnitt är grupperade under rubriker: Köp och uppdateringar, Appinställningar, Hjälp, Juridik och integritet.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Inställningar Huvudskärm" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Uppgradera till Premium

Uppgradera programmet till Premium-versionen för att ta bort alla begränsningar. Den kostnadsfria versionen av programmet erbjuder ett engångsinköp för livstid och två prenumerationsalternativ (1 månad och 1 år) för att ta bort alla begränsningar och uppgradera till Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Uppgradera till Premium" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

**Familjedelning** är aktiverat för alla köp och planer, så du kan dela Premium-versionen med upp till fem familjemedlemmar utan extra kostnad.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Välj en Premium-plan" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Dela köp mellan iOS och Mac

Livstidsinköp och prenumerationer delas mellan iOS och Mac med hjälp av **iCloud** för att synkronisera denna information. Om du har Premium på din iOS-enhet, se till att du har den senaste versionen installerad och att iCloud är aktiverat. Starta appen på iOS och vänta en minut på att köpinformation laddas upp till iCloud, starta sedan Mac-versionen — Premium bör aktiveras automatiskt.

Du kan också trycka på knappen **Återställ köp** i appinställningarna. Se till att du har en internetanslutning och är inloggad på samma iCloud- och App Store-konto på båda enheterna.

## Återställ köp på en ny enhet

För att återställa ditt köp på en ny enhet, använd menyn **Köp → Återställ köp**. Du kommer att se listan över dina köp. Om du inte ser alla, bekräfta att enheten är ansluten till samma Apple-ID som användes för att göra köpen och se till att iCloud är aktiverat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Köpmeny i Inställningar" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Prova Premium gratis

Du kan uppgradera till Premium-versionen gratis, under en begränsad tid, med den här menyn. Titta bara på en annons eller berätta för dina vänner om appen.

## Programuppdatering

Tryck på **Programuppdatering** för att kontrollera om en nyare version av Evervideo är tillgänglig i App Store.

## Nyheter

Den här menyn är tillgänglig efter att en ny version har släppts. Den visar en sammanfattning av ändringarna och nya funktioner i den senaste uppdateringen.

## Spelare

Allt relaterat till uppspelning finns här — ljud, video, undertexter, enheter, personalisering, cache och sömnstimer.

### Allmänt

Dessa inställningar täcker de grundläggande aspekterna av spelaren.

- **Upprepningsläge** — välj hur spelaren beter sig när ett video avslutas:
  - **Upprepa alla** — spelar om varje video i din kö.
  - **Upprepa en** — upprepar bara det aktuella videon.
  - **Stoppa vid upprepning** — pausar när det aktuella videon avslutas.
  - **Ingen upprepning** — spelar kön en gång utan upprepning.
- **Blandningsläge** — randomisera ordningen på videor i din kö (**På** eller **Av**).
- **Spara uppspelningsposition** — sparar och återställer uppspelningspositionen för videor i ditt bibliotek.
- **Spara spelartillstånd** — bevarar spelarens tillstånd innan du stänger appen, så att du kan återuppta från där du slutade.

### Video

Konfigurera hur Evervideo avkodar och renderar video.

- **Hårdvaruavkodning H.264** — slå på / av hårdvaruaccelererad AVC-avkodning. Använd när batteri och termisk prestanda spelar roll; stäng av för kompatibilitet med exotiska profiler.
- **Hårdvaruavkodning H.265 (HEVC)** — samma för HEVC. Moderna iPhones, iPads och Mac avkodar HEVC effektivt.
- **Föredragen pixelformat** — välj pixelformatet spelaren presenterar för renderaren (standardvärden är inställda för enheten).
- **Föredragen FPS** — ange ett mål-FPS för uppspelning. Användbart för att matcha en specifik bildskärmsuppdateringshastighet.
- **Videoskalningsläge** — Passa / Fyll / Sträck / Original. Avgör hur bilden fyller visningsområdet.
- **Videovisningsläge** (iOS / iPadOS) — hur videon presenteras i spelarns vy.
- **Videorotation** — rotera bilden manuellt 0° / 90° / 180° / 270° (hjälpsamt för videor inspelade med fel orientering).
- **Videoequalizer** — justera ljusstyrka, kontrast, mättnad och nyans med förhandsgranskning i realtid. Anpassade förinställningar kan **exporteras och importeras**.
- **VR-viewport** (iOS / iPadOS) — för 360° sfäriska videor. Dra för att titta runt, nyp för att zooma.
- **Bild-i-bild (PiP)** (iOS / iPadOS) — aktivera PiP-stöd; appen byter till ett flytande spelarfönster när du bakgrundslägger appen eller trycker på PiP-knappen.

### Ljud

Konfigurera ljuduppspelning och -utmatning.

- **Ljudspår** — välj ljudströmmen när ett video har flera (kommentar, synk, etc.).
- **Audioequalizer** — 10-bands EQ med förinställningar och en förförstärkare. Anpassade förinställningar kan exporteras / importeras.
- **Samplingshastighet för audioutgång** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Användbart med externa DAC:er.
- **Antal kanaler för audioutgång** — Mono, Stereo, 5.1, ITU BS.775-1, SDDS med mera.
- **Föredragen IO-bufferttid för audioutgång** — typiskt värde för låglatens hi-res uppspelning är cirka 5 ms (0,005 s). Justera för din hårdvara.
- **Audioutgångsläge** (endast iOS) — blandat läge låter Evervideo's ljud blandas med andra appar.

### Undertexter

Evervideo inkluderar omfattande undertextstöd.

- **Undertextspar** — välj från inbäddade undertextspår i filen.
- **Extern undertextsfil** — ladda en extern `.srt`-, `.vtt`-, `.ass`- eller `.ssa`-fil från din enhet eller någon ansluten molntjänst.
- **Teckensnitt** — välj ett teckensnitt för det primära undertextsspåret.

### Enheter (endast iOS/iPadOS)

Välj en **AirPlay**- eller **Google Chromecast**-enhet för videoutmatning.

### Personalisering

- **Spelarens layoutstil** — Minimal (standard för Evervideo), Botten, Antik, Klassisk med mera.
- **Huvudskärmsåtgärder** — välj vilka knappar som visas på spelarens huvudskärm.
- **Låsskärmskontroller** — Hoppa över tid, Lägg till bokmärke, Lägg till i favoriter.
- **Hoppintervall** — välj tidsintervall för hoppknappar (5 s, 10 s, 15 s, 30 s etc.).
- **Rullningsstil för albumomslag** — föredragen rullningsstil för omslagskonst.
- **Ytterligare element** — Audioformatinfo, Volymreglage.

### Filladdning

Konfigurera hur videodata strömmas från nätverket.

- **Nätverkstyp** — endast Wi-Fi, eller Wi-Fi + Mobilt.
- **Förladdningstid** — bufferttid för jämnare uppspelning på långsamma nätverk.
- **Använd direkt URL** — använd en direkt URL för snabbare laddning när det stöds.

### Uppspelningscache

Videor i spelarkön laddas automatiskt ned för att säkerställa jämn uppspelning. Du kan inaktivera det här alternativet eller konfigurera cachestorleken här.

### Sömnstimer

Aktivera en timer för att automatiskt stoppa uppspelning efter en angiven period. Tryck på konfigurationsikonen för **precist läge** med minutsminutupplösning.

## Mediebibliotek

Hantera automatisk synkronisering, metadata, albumomslag, spellistor, senaste och favoriter.

### Metadataläsning

När du lägger till videor i biblioteket skannar metadataläsaren dem i bakgrunden och organiserar dem efter album och genre. Du kan justera skanningshastigheten, inaktivera läsaren eller starta en fullständig omskanring med **Ladda om metadata**. **Normalisera metadatakodning** åtgärdar automatiskt trasiga teckenkodningar (vanligt med filer från Windows-datorer).

### Online-synkronisering

Lägg automatiskt till videor från anslutna molntjänster och medieservrar i ditt bibliotek. Välj vilka mappar som ska skannas, konfigurera hur ofta appen ska synkronisera och starta / stoppa synkronisering manuellt. Online-synk körs bara när appen är aktiv — för stora bibliotek, använd skrivbordsversionen och överför sedan det synkroniserade biblioteket med **Säkerhetskopia och återställning**.

### Offline-synkronisering

När du markerar en molnmapp som tillgänglig offline visas den i **Filer → Offline mappar** och laddas ned automatiskt. Nya filer som läggs till online laddas också ned. Konfigurera tidsintervallet och utlös manuella synkroniseringar från den här skärmen.

### Personalisering

- **Stil för mediebiblioteksskärm** — Enkel meny, Grupperad meny, Flikad meny.
- Växla om du vill visa stora albumomslag på detaljskärmar.

### Albumomslag

- **Nätverkstyp** — Wi-Fi eller Wi-Fi + Mobilt.
- **Ladda albumomslag för onlinefiler** — hämta inbäddad konstverk från molnfiler (använder extra data).
- **Sök i mappen** — använd JPEG / PNG-bilder i samma mapp när ett video inte har något inbäddat omslag.
- **Omslagskvalitet** — justera upplösningen som omslag cachas med.
- **Visa i mapp** / **Ta bort alla** — hantera konstverkcachen.

### Spellistor

Aktivera att lägga till samma video i en spellista två gånger (av som standard).

### Senaste

Hantera listan med senast spelade videor — ändra storlek, ta bort eller exportera som M3U / CSV / TXT.

### Favoriter

- **Simultanredigering** — spegla favoriter mellan mediebiblioteket och filsektionen.
- **Ta bort lista** — rensa favoritlistan.
- **Exportera låtlista** — exportera favoriter som M3U / CSV / TXT.

### Ta bort mediebibliotek

Radera mediebiblioteksdatabasen. Dina video- och ljudfiler i lagringsutrymmet lämnas orörda.

## Lösenord

Skydda Evervideo med en **4-siffrig numerisk lösenordskod**. När det är aktiverat uppmanas du att ange lösenordskoden varje gång appen startas. Kombinera det med iOS Face ID / Touch ID på enheten för extra skydd.

## Filhanterare

Kontrollerar hur filer överförs, lagras och förhandsgranskas.

- **Filöverföringar** — nätverkspreferens (endast Wi-Fi eller Wi-Fi + Mobilt).
- **Maximalt antal parallella uppgifter** — ange antalet parallella nedladdningstrådar.
- **Filöverföringsuppgifter** — se aktuellt aktiva uppladdningar och nedladdningar.
- **Bakgrundsöverföringar** — tillåt nedladdningar när appen är i bakgrunden.
- **Spara nedladdade filer till** — standardkatalog för nedladdningar.
- **Synkroniserade offline-mappar** — hantera offline-lägemappar.
- **Tidsintervall** — hur ofta offline-mappar kontrolleras för ändringar.
- **Visa fullständiga filnamn** — visa tillägg i filhanteraren.
- **Redigera onlinefiler** — inaktivera för att byta till skrivskyddat läge för anslutna molntjänster.
- **Kopiera filer vid öppning** — hur importerade filer från andra appar hanteras.
- **Miniatyrbilder för filer** — hantera genererade filminiatyrbilder.
- **Ta bort temporära filer** — rensa appens cachemapp.

## Wi-Fi Drive

Aktivera Wi-Fi Drive för att överföra filer från en dator till din enhet med en stationär webbläsare, Finder eller File Explorer. Detaljerade instruktioner finns [här](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Widgets

Aktivera widgets så att appen uppdaterar widgetdata under uppspelning. Widgetuppdateringar kräver extra energi, så reglaget är avstängt som standard — aktivera det bara om du faktiskt använder widgets på din hemskärm eller låsskärm.

Du kan lägga till Evervideo-widgets genom att långtrycka på din hemskärm eller låsskärm, trycka på **+**, söka **Evervideo** och välja en widgetstorlek. Widgets visar det video som spelas nu och trycker igenom direkt till helskärmsspelaren. Widgets fungerar också på macOS i aviseringscenter.

## Personalisering

Anpassa användargränssnittet efter dina preferenser.

- **Appikon** — alternativ hemskärmsikon (Premium).
- **Färgschema** — Mörk, Ljus eller Standard (följer ditt systemutseende).
- **Bakgrundsstil** — Suddigt albumomslag eller enfärg.
- **Utseende på objekt i listan** — justera radhöjd automatiskt; visa mindre miniatyrbilder.
- **Innehållsladdningsgräns** — slå på / av sidnumrering.
- **Filskärmsstil** — Enkel meny eller Grupperad meny.
- **Stil för mediebiblioteksskärm** — Enkel / Grupperad / Flikad meny.
- **Spelarskärmsstil** — Minimal / Botten / Antik / Klassisk.
- **Snabbmenysstil** — systemmeny eller stil med bottenark.

## Fönster

Tillgänglig på Mac och Catalyst. Konfigurera fönsterrelaterade inställningar som standardstorlek och beteende vid start.

## Skärm

Välj om skärmen ska förbli aktiv medan du använder programmet.

## Tillgänglighet

Aktivera **Textläge** för att dölja bilder i användargränssnittet. Textläge aktiveras automatiskt när VoiceOver är aktivt.

## Språk

Ändra programspråket och åsidosätt systemstandarden. Ändringen tillämpas efter att du helt avslutar och öppnar Evervideo igen. Över 120 språk stöds.

## Säkerhetskopia och återställning

Säkerhetskopiera alla dina programdata eller migrera dem till en annan enhet. Välj vad som ska inkluderas:

- **Databas** — dina mediebiblioteksposter, spellistor, betyg, favoriter, tittarhistorik. Offlinefiler är inte inkluderade för att hålla filstorleken hanterbar.
- **Albumomslag** — din cachade konstverk.
- **Inställningar** — dina programinställningar.

Tryck på **Säkerhetskopiera programdata** för att starta säkerhetskopieringen. För att återställa på en ny enhet, flytta säkerhetskopiefilen via iCloud Drive, AirDrop eller någon ansluten molntjänst och öppna den på den nya enheten.

## Hjälp

Åtkomst till programguiden för hjälp och vägledning om hur du använder appen effektivt.

## Vanliga frågor

Hitta svar på vanliga frågor i FAQ-avsnittet.

## Skicka feedback

Skicka din feedback till vårt supportteam direkt från appen, med diagnostikinformation bifogad automatiskt.

## Dela den här appen

Dela Evervideo med dina vänner för att sprida ordet.

## Utforska fler appar

Utforska andra appar från Everappz.

## Villkor och bestämmelser

Läs villkoren och bestämmelserna innan du använder programmet.

## Integritetspolicy

Läs integritetspolicyn för att förstå våra rutiner för datahantering.

## Analys och datainsamling

Kontrollera vilka tjänster som är aktiverade för analys och datainsamling och inaktivera de du inte vill ha.

## Juridiska meddelanden

Information om varje bibliotek som används i programmet tillsammans med appversionsnumret och bygginformation.
