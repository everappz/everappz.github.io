---
title: "Evervideo 1.7: Nytt Plex, Jellyfin, molnströmning, uppspelningsgester"
date: 2026-05-18
description: "Evervideo 1.7 lägger till 10+ nya anslutningar — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — plus nya uppspelningsgester (dubbeltryck för att spola, tryck och håll för 2x hastighet), en uppdaterad Wi-Fi Drive med batchuppladdning samt Liquid Glass-UI-uppdateringar för iPhone, iPad och Mac."
keywords: ["Evervideo 1.7", "Evervideo-uppdatering", "HD-videospelare iPhone", "Plex-videospelare iOS", "Jellyfin iPhone-video", "Emby-videospelare iOS", "Subsonic video iOS", "Navidrome video iOS", "Internxt videoströmning", "Proton Drive-videospelare", "QNAP-videospelare iPhone", "Nextcloud-videospelare iOS", "Amazon S3 videoströmning", "SFTP-videospelare iPhone", "FTP-videospelare iOS", "NFS videoströmning iPhone", "strömma video från NAS iPhone", "MKV-spelare iPhone", "videospelare-gester iOS", "dubbeltryck för att spola video", "Wi-Fi Drive videoöverföring iPhone", "Liquid Glass-design", "molnvideospelare iOS 2026", "strömma filmer från molnet iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Uppspelningsgester", "Liquid Glass", "Vad är nytt"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Kort sagt:** [Evervideo 1.7](/products/evervideo) är en stor uppdatering för HD-videospelaren på iPhone, iPad och Mac. Versionen lägger till 10+ nya moln-, NAS- och mediaserveranslutningar — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, plus de mest populära mediaservrarna **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** och **Emby**, samt tre nätverksprotokoll: **FTP**, **SFTP** och **NFS**. Nya **uppspelningsgester** låter dig dubbeltrycka för att hoppa framåt eller bakåt, trycka och hålla för att köra i 2x och enkeltrycka för att växla kontrollerna — allt utan att lämna helskärm. Wi-Fi Drive får ett uppdaterat gränssnitt med urvalsläge och en smartare uppladdningskö. Hela appen är finjusterad för Apples nya **Liquid Glass**-design.

---

## Hej alla!

En stor Evervideo-uppdatering är här. Detta är en av de största versionerna vi har levererat: **10+ nya moln-, server- och nätverksanslutningar**, helt nya **uppspelningsgester** för snabbare kontroll i helskärm, en uppdaterad **Wi-Fi Drive**-upplevelse och ett UI finjusterat för **Liquid Glass** på iPhone, iPad och Mac.

[Ladda ner Evervideo 1.7 från App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) eller uppdatera från din befintliga version. Mac-användare kan hämta [skrivbordsversionen här](https://apps.apple.com/app/evervideo/id6743504109).

## 10+ nya moln-, NAS- och mediaserveranslutningar

Evervideo 1.7 utökar vad som räknas som ditt «videobibliotek». Om dina filmer, serier eller inspelningar finns i ett moln du litar på, en NAS hemma eller en självhostad mediaserver, kan Evervideo nu strömma från dem direkt — inga nedladdningar, inga konverteringar, ingen omkodning.

### Integritetsfokuserad molnlagring: Internxt och Proton Drive

Om du bryr dig om end-to-end-kryptering och nollkunskaps­lagring är två av de mest respekterade integritetsfokuserade molnen nu inbyggda i Evervideo:

- **Internxt** — open source, post-kvantkrypterat, GDPR-kompatibelt spanskt moln. Gratisnivå tillgänglig.
- **Proton Drive** — end-to-end-krypterad lagring från skaparna av Proton Mail och Proton VPN, baserat i Schweiz. Gratisnivå tillgänglig med betalda planer för större bibliotek.

Anslut en gång och dina videor strömmas genom den krypterade tunneln — Evervideo ser aldrig din data i klartext, och inte heller leverantörens server.

### Självhostad lagring: QNAP, Nextcloud, Amazon S3

För användare som driver sin egen infrastruktur:

- **QNAP** — inbyggd API-anslutning till QNAP NAS-enheter för snabb och pålitlig videouppspelning över lokalt Wi-Fi eller fjärråtkomst. Strömma 4K MKV-filer direkt utan omkodning.
- **Nextcloud** — anslut till valfri självhostad eller hanterad Nextcloud-instans. Bra om du redan har migrerat bort från Google Drive eller Dropbox av integritetsskäl.
- **Amazon S3** — peka Evervideo mot vilken S3-bucket som helst (eller S3-kompatibel lagring som Backblaze B2, Wasabi, MinIO, Cloudflare R2) och strömma din samling direkt.

### <a id="media-servers"></a>Mediaservrar: Plex, Subsonic, Navidrome, Jellyfin, Emby

Detta är den stora nyheten för fans av självhostad video. Evervideo 1.7 gör din iPhone, iPad eller Mac till en förstklassig klient för de mest populära open source- och freemium-mediaservrarna:

- **Plex** — Plex Media Server är **gratis** att ladda ner och köra, med en valfri **Plex Pass**-prenumeration för funktioner som mobilsynkronisering, hårdvarutranskodning och live-TV. Evervideo fungerar med både gratis- och Plex Pass-bibliotek — strömma hela din film- och TV-samling.
- **Subsonic** — den ursprungliga självhostade strömningsservern. Den officiella Subsonic-servern är **betald** (1 $/månad efter en 30-dagars provperiod), och Evervideo talar också Subsonic API till kompatibla videoservrar.
- **Navidrome** — modern, lättviktig, **helt gratis och open source** server. Implementerar Subsonic API. Körs på en Raspberry Pi, NAS eller vilken Linux-låda som helst.
- **Jellyfin** — **helt gratis och open source** mediaserver (en community-fork av Emby). Hanterar filmer, TV, musik, böcker och hemvideo. Inga konton, ingen telemetri, inga prenumerationer. Det självklara valet för användare som vill ha självhostad strömning utan kommersiella villkor.
- **Emby** — **freemium** mediaserver. Kärnservern är gratis; **Emby Premiere** är ett engångs- eller årligt köp som låser upp mobilappar, offlinesynkronisering, Cinema Mode och mer. Evervideo ansluter till både gratis- och Premiere-bibliotek.

Oavsett vilken server du kör, strömmar Evervideo hela ditt bibliotek — filmer, serier, hemvideor och inbäddade undertextspår — med videoekvalisern, 360°-stöd, Bild-i-bild, AirPlay och Chromecast.

### Nya nätverksprotokoll: FTP, SFTP, NFS

För användare med anpassade servrar, hemmalabb eller generiska NAS-lådor som inte levereras med en finslipad mobilapp, lägger Evervideo 1.7 till tre klassiska protokoll:

- **SFTP (SSH File Transfer Protocol)** — rätt svar för **säker fjärrströmning av video från din egen server**. SFTP körs ovanpå SSH, så hela överföringen (autentisering och videodata) är krypterad. Om du har en VPS, dedikerad server eller en Linux-låda hemma med SSH-åtkomst, kan du lägga en mapp med videor på den och strömma över det öppna internet utan att exponera något annat. Stöder lösenords- och nyckelbaserad autentisering.
- **FTP** — den långvariga standarden för filöverföring. Användbar om din **hem-NAS** (äldre Synology, ASUS, D-Link, TerraMaster eller generiska lådor) exponerar en FTP-server men inte har en inbyggd API-integration. Bäst att använda inom ditt lokala nätverk.
- **NFS (Network File System)** — det de facto delningsprotokollet på Linux och de flesta NAS-enheter. NFS-delningar är vanliga i hemmalabb och småföretagsnätverk; Evervideo monterar dem nu och strömmar 4K- och HD-video med låg overhead.

> **Tips:** SFTP är det protokoll du vill ha för strömning över det öppna internet. FTP och NFS används bäst inom ditt lokala nätverk — håll dem borta från det offentliga internet om du inte slår in dem i en VPN.

## Nya uppspelningsgester

Att titta på videor i helskärm ska kännas obesvärat. Evervideo 1.7 introducerar en ren uppsättning trycksrörelser som låter dig styra uppspelningen utan att visa kontrollerna på skärmen — perfekt för filmer, föreläsningar eller vad du än vill titta på utan avbrott.

### Dubbeltryck — hoppa framåt eller bakåt

Dubbeltryck på **höger sida** av skärmen för att **hoppa framåt** ett konfigurerbart antal sekunder. Dubbeltryck på **vänster sida** för att **hoppa tillbaka**. Du kan ändra intervallet (standard: 10 sekunder) i **Inställningar → Uppspelning → Gestintervall för hopp** — välj vad som helst från 5 sekunder (för fin sökning) till 60 sekunder (för att hoppa över intron).

Detta är gesten som YouTube- och Netflix-användare omedelbart känner igen, och den är nu inbyggd i Evervideo för vilken video som helst, från vilken källa som helst.

### Tryck och håll — tillfällig 2x hastighet

Tryck och håll var som helst på skärmen för att **tillfälligt öka uppspelningshastigheten till 2x**. Släpp för att återgå till normal hastighet. Perfekt för:

- Hoppa över långsamma scener utan att binda sig till en permanent hastighetsändring.
- Snabbt skanna igenom föreläsningar, handledningar eller poddar för att hitta den relevanta delen.
- Smakprov på filmer innan du bestämmer dig för att titta på hela versionen.

Hållgesten ändrar inte din sparade uppspelningshastighet — släpp och du är tillbaka där du började.

### Enkeltryck — visa/dölj kontroller

Ett enkeltryck på skärmen växlar uppspelningskontrollerna (spela, pausa, sökfält, undertexter, ekvaliser). Tryck en gång för att ta fram dem, tryck igen för att dölja dem. Kombinerat med dubbeltryck och håll betyder detta att du kan tillbringa nästan en hel film i rent helskärmsläge och fortfarande söka, pausa och snabbskanna när du behöver.

## Wi-Fi Drive: nytt UI och snabbare uppladdningar

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) är Evervideos inbyggda funktion för **trådlös överföring av videor från din dator till din iPhone eller iPad — inga iTunes, inga kablar, inget molnkonto krävs**. Båda enheterna måste vara på samma Wi-Fi-nätverk. Du startar servern i iOS-appen och antingen:

- Öppna URL:en i valfri skrivbordswebbläsare (Safari, Chrome, Firefox, Edge), dra dina videofiler till sidan, och de laddas upp direkt till enheten, eller
- Montera enheten som en nätverksdelning via **Mac Finder** («Anslut till server…») eller **Windows Utforskaren** (Anslut nätverksenhet) med WebDAV.

Det är det snabbaste sättet att flytta en stor lokal videosamling till din telefon eller surfplatta utan någon tredjepartstjänst. Se [steg-för-steg-guiden här](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

I Evervideo 1.7 får Wi-Fi Drive:

- **Omdesignat användargränssnitt** — renare, lättare att läsa vid en överblick och uppdaterat för Liquid Glass.
- **Nytt urvalsläge för batchåtgärder** — välj flera filer eller mappar och agera på dem i bulk (ta bort, flytta, kopiera).
- **Förbättrad filuppladdningskö** — bättre förloppsåterkoppling och motståndskraft mot nätverksavbrott så att en ostadig Wi-Fi-anslutning inte längre förstör en överföring på 30 GB.
- **Bättre övergripande överföringsprestanda** — mätbart snabbare uppladdningar för stora bibliotek, särskilt för 4K MKV-filer och filmsamlingar.

## Andra förbättringar

### Liquid Glass-designuppdateringar

Evervideo 1.7:s gränssnitt är uppdaterat för Apples nya **Liquid Glass**-material i hela appen — genomskinliga ytor, mjukare animationer och förfinade kontroller som passar naturligt in i iOS 26, iPadOS 26 och macOS 26. Spelas nu, filbläddraren och inställningsskärmarna har alla finjusterats för att matcha den nya systemestetiken.

### Uppdaterade anslutningsbibliotek

Vi har uppdaterat de underliggande biblioteken som Evervideo använder för att kommunicera med **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** och andra tjänster. Resultatet: färre anslutningsfel i kantfall, bättre stöd för nyare serverversioner och förbättrad tillförlitlighet vid videoströmning på långsammare eller geografiskt avlägsna anslutningar.

### Buggfixar för uppspelning

- Åtgärdat uppspelningsproblem på vissa självhostade servrar där strömmar stannade efter sökning på stora MKV-filer.
- Bättre återupptagningsbeteende när nätverket kort tappas mitt i uppspelningen.
- Jämnare undertextsynkronisering på långt innehåll.

### Lokaliseringsfixar

Översättningsfixar över flera språk baserat på direkt användarfeedback. Bättre textanpassning på mindre knappar och längre europeiska språk (tyska, holländska, franska).

### Mindre förbättringar inspirerade av din feedback

Många mindre förbättringar baserade på App Store-recensioner och e-postmeddelanden till support@everappz.com. Vi läser varje meddelande.

## Varför den här uppdateringen spelar roll

Evervideo 1.7 är byggd kring tre idéer:

1. **Dina videor, var du än har dem.** Oavsett om ditt bibliotek finns på iCloud Drive, ett integritetsfokuserat moln som Proton Drive eller Internxt, en mediaserver som Plex eller Jellyfin, en NAS hemma eller en Raspberry Pi som kör Navidrome — Evervideo ansluter nu inbyggt till det, med samma uppspelningsupplevelse överallt.
2. **Helskärmsvideo som känns obesvärad.** De nya tryckgesterna (dubbeltryck, tryck och håll, enkeltryck) ger den typ av flytande kontroll som strömningsappar som YouTube och Netflix har tränat användare att förvänta sig, tillämpat på *din* videosamling.
3. **Snabbare överföringar från din dator.** En uppdaterad Wi-Fi Drive med batchurval och en smartare uppladdningskö gör att flytta stora 4K-filmsamlingar till din iPhone eller iPad genuint snabbt — inga kablar, ingen iTunes, ingen komprimering.

## Skaffa Evervideo 1.7

[**Ladda ner Evervideo från App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) eller uppdatera inifrån App Store. [Mac-versionen](https://apps.apple.com/app/evervideo/id6743504109) är tillgänglig separat som en universell Mac-app. Evervideo är en gratis nedladdning med valfria uppgraderingar i appen för avancerade funktioner. De nya molnanslutningarna, mediaserverstödet, uppspelningsgesterna, Wi-Fi Drive-förbättringarna och Liquid Glass-UI är en del av basuppdateringen.

Om du gillar appen, lämna gärna ett betyg i App Store — det hjälper verkligen. Har du feedback eller stött på ett problem? Mejla oss på **support@everappz.com**. Vi läser varje meddelande.

## Vanliga frågor

{{% details title="Vad är nytt i Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 introducerar stöd för 10+ nya anslutningar (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), nya uppspelningsgester (dubbeltryck för att spola, tryck och håll för 2x hastighet, enkeltryck för att växla kontroller), en omdesignad Wi-Fi Drive med urvalsläge och en smartare uppladdningskö, Liquid Glass-designuppdateringar, uppdaterade anslutningsbibliotek och många buggfixar.
{{% /details %}}

{{% details title="Fungerar Evervideo med Plex?" closed="true" %}}
Ja. Från och med Evervideo 1.7 kan du ansluta till en Plex Media Server och strömma hela ditt videobibliotek — filmer, TV-program och hemvideor. Plex Media Server är gratis att köra; Plex Pass är valfritt. Evervideo stöder både gratis- och Plex Pass-inställningar, inklusive direkt uppspelning av MKV, MP4, AVI, MOV och andra format utan omkodning.
{{% /details %}}

{{% details title="Stöds Jellyfin eller Navidrome i Evervideo?" closed="true" %}}
Ja. Både Jellyfin och Navidrome stöds fullt ut i Evervideo 1.7. Jellyfin är en gratis, open source-mediaserver som hanterar video och ljud. Navidrome är en gratis, open source-server som implementerar Subsonic API. Evervideo ansluter till båda inbyggt.
{{% /details %}}

{{% details title="Är Plex, Jellyfin, Emby, Navidrome och Subsonic gratis?" closed="true" %}}
- **Plex** — servern är gratis; Plex Pass är en valfri betald uppgradering.
- **Jellyfin** — helt gratis och open source.
- **Emby** — servern är gratis; Emby Premiere är betald och låser upp mobilsynkronisering och offline.
- **Navidrome** — helt gratis och open source.
- **Subsonic** — den officiella servern kostar 1 $/månad efter en 30-dagars provperiod, men dess API är öppet och många gratisservrar (inklusive Navidrome) implementerar det.
{{% /details %}}

{{% details title="Kan jag strömma från min hem-NAS över SFTP, FTP eller NFS?" closed="true" %}}
Ja. Evervideo 1.7 lägger till SFTP, FTP och NFS som inbyggda anslutningstyper. SFTP är det rekommenderade valet för att strömma från din egen server över det offentliga internet eftersom all trafik är krypterad via SSH. FTP och NFS används bäst inom ditt lokala nätverk eller bakom en VPN.
{{% /details %}}

{{% details title="Hur ansluter jag Evervideo till en anpassad server med SFTP?" closed="true" %}}
Öppna Evervideo, gå till fliken Anslutningar, välj SFTP och ange din servers värdnamn eller IP, port (vanligtvis 22), användarnamn och antingen ett lösenord eller en privat SSH-nyckel. Evervideo bläddrar bland dina fjärrmappar och strömmar videofiler direkt med end-to-end-kryptering.
{{% /details %}}

{{% details title="Stöder Evervideo Internxt och Proton Drive?" closed="true" %}}
Ja. Båda integritetsfokuserade molnen stöds från och med Evervideo 1.7. De ansluter sig till MEGA och andra integritetsfokuserade tjänster som redan finns i appen.
{{% /details %}}

{{% details title="Hur fungerar de nya uppspelningsgesterna?" closed="true" %}}
Vid helskärmsuppspelning av video, **dubbeltryck på höger sida** för att hoppa framåt och **dubbeltryck på vänster sida** för att hoppa tillbaka med ett konfigurerbart intervall (standard 10 sekunder — ändra det i Inställningar). **Tryck och håll** var som helst på skärmen för att tillfälligt öka till 2x; släpp för att återgå till normalt. **Enkeltryck** var som helst för att växla uppspelningskontrollerna (visa eller dölj).
{{% /details %}}

{{% details title="Kan jag ändra intervallet för dubbeltrycks-hopp?" closed="true" %}}
Ja. Gå till **Inställningar → Uppspelning → Gestintervall för hopp** och välj ett värde mellan 5 och 60 sekunder. De flesta användare håller det på 10 eller 15 sekunder.
{{% /details %}}

{{% details title="Vad är Wi-Fi Drive i Evervideo?" closed="true" %}}
Wi-Fi Drive är Evervideos inbyggda funktion för trådlös filöverföring. Det låter dig ladda upp videor från din dator till din iPhone eller iPad över ditt lokala Wi-Fi-nätverk — inga iTunes, inga kablar, inget molnkonto. Du kan använda valfri skrivbordswebbläsare eller en WebDAV-klient som Mac Finder eller Windows Utforskaren. Se den [fullständiga Wi-Fi Drive-guiden](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Spelar Evervideo MKV, AVI och andra format från Plex eller Jellyfin?" closed="true" %}}
Ja. Evervideo spelar praktiskt taget alla videoformat — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — och strömmar dem direkt från Plex, Jellyfin, Emby och andra mediaservrar utan att kräva transkodning för de flesta codecs. Detta innebär lägre CPU-belastning på din server och snabbare starttider.
{{% /details %}}

{{% details title="Är Evervideo 1.7 gratis att uppdatera?" closed="true" %}}
Ja. Evervideo är en gratis nedladdning från App Store, och 1.7 är en gratis uppdatering för alla befintliga användare. De nya molnintegrationerna, mediaserverstödet, uppspelningsgesterna, Wi-Fi Drive-förbättringarna och Liquid Glass-UI är en del av basuppdateringen.
{{% /details %}}

{{% details title="Vilka enheter är Evervideo 1.7 tillgängligt på?" closed="true" %}}
Evervideo 1.7 körs på iPhone, iPad och Mac. AirPlay och Chromecast låter dig sända uppspelning till en större skärm. iCloud Drive-synkronisering håller ditt bibliotek och inställningar konsekventa mellan enheter.
{{% /details %}}
