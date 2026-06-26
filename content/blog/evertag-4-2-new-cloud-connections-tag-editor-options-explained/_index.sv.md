---
title: "Evertag 4.2: nya molnanslutningar, taggredigerarens inställningar förklarade"
date: 2026-05-09
description: "Evertag 4.2 lägger till anslutningar till Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP och NFS, fräschar upp Wi-Fi Drive och uppdaterar gränssnittet för Liquid Glass. Det här inlägget förklarar också varje inställning i taggredigeraren — inklusive ID3v2.4 vs ID3v2.3, skalning av albumomslag, dubblerade taggar, molnuppladdningslägen och rätt val för Spotify och andra strömningstjänster."
keywords: ["Evertag 4.2", "Evertag-uppdatering", "ID3 taggredigerare iPhone", "ID3v2.4 vs ID3v2.3", "redigera FLAC-taggar iOS", "redigera MP3-taggar iPhone", "redigera albumomslag iOS", "taggredigerare för Spotify", "taggredigerare Plex", "taggredigerare Apple Music", "Evertag molntaggredigerare", "Internxt taggredigerare", "Proton Drive taggredigerare", "QNAP taggredigerare", "Nextcloud taggredigerare", "Amazon S3 taggredigerare", "SFTP taggredigerare iPhone", "FTP ljudtaggredigerare", "NFS taggredigerare iPhone", "Wi-Fi Drive taggredigerare", "dubblera ID3-taggar", "albumomslagsskalning", "Liquid Glass-design", "ljudmetadataredigerare iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Taggredigerare", "ID3", "ID3v2.4", "ID3v2.3", "FLAC-taggar", "MP3-taggar", "Albumomslag", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Vad är nytt"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Kort sagt:** [Evertag 4.2](/products/evertag) är en stor uppdatering för ljudtaggredigeraren på iPhone, iPad och Mac. Vi krossade viktiga buggar i taggredigering och lade till över 6 nya moln- och serveranslutningar — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** plus protokollen **FTP**, **SFTP** och **NFS**. Wi-Fi Drive fick ett uppfräschat gränssnitt, flerval-läge, en smartare uppladdningskö och snabbare överföringar. Hela appen är inställd på **Liquid Glass**-designen. Det här inlägget gräver också djupt i Evertags taggredigerar-inställningar — förklarar **ID3v2.4 vs ID3v2.3**, **skalning av albumomslag**, **dubblerade taggar**, **molnuppladdningslägen**, **ta bort nedladdad fil** och precis vilka alternativ du ska välja om du förbereder ljud för **Spotify**, **Apple Music**, **Plex**, **Jellyfin** eller någon annan strömningstjänst.

---

## Hej allihop!

En stor Evertag-uppdatering är här. Vi krossade viktiga buggar i taggredigering och lade till **över 6 nya moln- och serveranslutningar** för att göra hanteringen av ljudmetadata enklare än någonsin — oavsett om ditt bibliotek bor i ett integritetsfokuserat moln, på en självhostad NAS eller på en generisk FTP/SFTP/NFS-server.

[Ladda ner Evertag 4.2 från App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) eller uppdatera från din nuvarande version.

## Utökat moln- och serverstöd

Evertag ansluter nu inbyggt till ett bredare urval av moln- och självhostade lagringsalternativ. Du kan redigera ID3-, MP4-, FLAC-, OGG- och APE-taggar på filer var de än finns.

### Integritetsfokuserad molnlagring: Internxt och Proton Drive

Om du bryr dig om end-to-end-kryptering och nollkunskapslagring är två av de mest respekterade namnen inom integritetsfokuserade moln nu inbyggt stödda i Evertag:

- **Internxt** — spanskt molntjänst med öppen källkod, postkvantkryptering och GDPR-kompatibilitet. Gratisnivå tillgänglig.
- **Proton Drive** — end-to-end-krypterad lagring från skaparna av Proton Mail och Proton VPN, baserat i Schweiz. Gratisnivå tillgänglig och betalplaner för större bibliotek.

Du kan nu redigera metadata direkt på ljudfiler lagrade i någon av tjänsterna — filen förblir krypterad under överföring och endast de nya taggarna skrivs tillbaka.

### Självhostade lösningar: QNAP, Nextcloud, Amazon S3

För användare som driver sin egen infrastruktur:

- **QNAP** — inbyggd API-anslutning till QNAP NAS-enheter. Redigera taggar på filer på din QNAP via lokalt Wi-Fi eller fjärråtkomst.
- **Nextcloud** — anslut till valfri Nextcloud-instans, självhostad eller hanterad.
- **Amazon S3** — peka Evertag mot vilken S3-bucket som helst (eller S3-kompatibel lagring som Backblaze B2, Wasabi, MinIO, Cloudflare R2) och redigera metadata på plats.

### Nya nätverksprotokoll: FTP, SFTP, NFS

Evertag 4.2 lägger till tre klassiska protokoll för användare med anpassade servrar, hemmalabb eller generiska NAS-enheter:

- **SFTP (SSH File Transfer Protocol)** — det rätta svaret för **säker fjärrtaggredigering från din egen server**. SFTP körs ovanpå SSH, så hela överföringen (autentisering och ljuddata) är krypterad. Om du har en VPS, dedikerad server eller Linuxmaskin hemma med SSH-åtkomst kan du redigera taggar på fjärrfiler utan att exponera något annat. Stödjer både lösenords- och nyckelbaserad autentisering.
- **FTP** — den sedan länge etablerade standarden för filöverföring. Användbar för äldre hemma-NAS som erbjuder FTP men saknar inbyggd API-integration.
- **NFS (Network File System)** — det de facto delningsprotokollet på Linux och de flesta NAS-enheter. Lägre overhead än SMB på samma hårdvara.

> **Tips:** SFTP är protokollet du vill använda för fjärrredigering över öppet internet. FTP och NFS fungerar bäst i det lokala nätverket — exponera dem inte mot internet om de inte ligger inuti ett VPN.

## Wi-Fi Drive-uppgraderingar

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) är Evertags inbyggda funktion för att **överföra ljudfiler trådlöst mellan din dator och iPhone eller iPad — utan iTunes, kablar eller molnkonto**. Båda enheterna måste vara på samma Wi-Fi-nätverk.

I Evertag 4.2 får Wi-Fi Drive:

- **Uppfräschat, modernt gränssnitt** — renare, lättare att läsa snabbt och uppdaterat för Liquid Glass.
- **Flerval-läge** — välj flera filer eller mappar och hantera dem i grupp.
- **Smartare uppladdningskö** — bättre återkoppling om förlopp och tåligare mot nätverksstörningar.
- **Förbättrad hastighet och övergripande tillförlitlighet** — snabbare överföringar för stora bibliotek.

Det är det snabbaste sättet att flytta en bunt ljudfiler från datorn till telefonen, redigera deras taggar och skicka dem tillbaka — utan tredjepartstjänster.

## Taggredigerar-inställningar: en djupdykning

Det här är delen som de flesta användare aldrig läser — och delen som avgör om dina taggar fungerar överallt eller bara i vissa appar. Öppna Evertag och gå till sektionen **inställningar för ljudtaggredigerare**. Här är vad varje alternativ faktiskt gör och vilket du ska välja beroende på ditt mål.

### Skalning av albumomslag

När du sparar albumomslaget i en ljudfil kan Evertag skala bilden innan den bäddas in. Tillgängliga alternativ:

- **Liten** — minst påverkan på filstorlek, lägre bildkvalitet.
- **Mellan** — balanserat val för de flesta användare.
- **Stor** — hög kvalitet, lämplig för spelare med stora skärmar och CarPlay.
- **Extra stor** — mycket hög kvalitet, märkbar ökning av filstorlek.
- **Original (Inaktiverad)** — bäddar in omslaget i originalupplösning. **Ingen skalning.**

**Varför det betyder något:**

- **Högre kvalitet = större fil.** Ett 3 000 × 3 000 pixel omslag kan lägga till flera MB till varje låt. Multiplicera med ett helt album så ackumuleras diskbelastningen snabbt.
- **Vissa spelare hanterar inte mycket stora inbäddade bilder bra.** Äldre enheter, vissa bil-headunits och en del äldre desktop-spelare kan fastna på omslag över ~1 500 px eller vägra visa dem.
- **För de flesta moln- och strömningsarbetsflöden** är **Mellan** eller **Stor** den optimala punkten. Använd **Original** endast när du specifikt behöver arkivkvalitet eller förbereder filer för en spelare du litar på.

> Storleksalternativet **Original** ingår i Evertags premium-personaliseringsuppgradering. Standardstorlekar (Liten/Mellan/Stor/Extra stor) är gratis.

### Taggsparalternativ: ID3v2.4 vs ID3v2.3

Detta är den enskilt viktigaste inställningen för kompatibilitet. ID3v2 är metadataformatet som används inuti MP3-filer. Det finns två allmänt använda versioner och de skiljer sig åt på subtila men viktiga sätt.

#### ID3v2.4

- Nyare, stödjer **UTF-8-textkodning** — korrekt hantering av icke-latinska skrifter (kinesiska, ryska, japanska, arabiska, hebreiska osv.).
- Fler ramtyper (relativ volym, equalizer-förinställningar osv.).
- **Rekommenderas för moderna spelare** som stödjer den.

#### ID3v2.3

- Äldre men **den mest universellt stödda** ID3-versionen.
- Stödjer inte UTF-8 direkt (använder UTF-16 för Unicode-text).
- **Rekommenderas när du behöver maximal kompatibilitet** med äldre spelare, bilstereo och vissa desktop-appar.

#### När du ska aktivera ID3v2.4 i Evertag

- Du använder **moderna ljudspelare** som Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (nuvarande versioner) eller moderna Android-spelare. ✅ **Slå PÅ ID3v2.4.**
- Ditt bibliotek innehåller **icke-latinska tecken** (kinesiska, koreanska, japanska, ryska, arabiska, grekiska, hebreiska). ✅ **Slå PÅ ID3v2.4** — UTF-8 hanterar dem mycket renare.

#### När du ska inaktivera ID3v2.4 i Evertag (använd ID3v2.3 istället)

- Du förbereder filer för en **äldre bilstereo eller instrumentbrädeenhet** som inte läser v2.4-taggar.
- Du ser **förvanskad text eller saknade taggar** i vissa appar efter redigering — det är en stark signal om att v2.4 inte stöds där. Byt tillbaka till v2.3.
- Du siktar på **äldre desktop-spelare** eller äldre bärbara spelare (tidiga iPods, vissa MP3-spelare från 2000–2010-talet).

> **Tumregel:** om dina taggar visas korrekt överallt med v2.4, lämna den på. Om även en viktig spelare visar fel tecken, blanka eller misslyckas att läsa taggar, slå AV v2.4 och spara om.

#### Dubblera taggar

När du aktiverar **Dubblera taggar** skriver Evertag gemensamma metadatafält (titel, artist, album osv.) i **både ID3v1- och ID3v2-sektionerna** av filen. Detta förbättrar kompatibilitet med mycket gamla spelare som endast läser ID3v1 (den ursprungliga 128-byte taggen i slutet av filen).

- **De flesta användare behöver inte detta.** Moderna spelare läser ID3v2 först.
- **Aktivera det endast om** du arbetar med vintage-hårdvara eller specifik mjukvara som ignorerar ID3v2.

### Uppdatera onlinefiler: hur Evertag hanterar molnredigeringar

När du redigerar taggar på en fil lagrad i ett anslutet moln (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP osv.) måste Evertag ladda upp den ändrade filen tillbaka. Du kontrollerar hur:

- **Visa bekräftelsemeddelande** *(standard, rekommenderas)* — Evertag frågar före uppladdning. Bäst för försiktiga användare och delade bibliotek.
- **Uppdatera filens metadata automatiskt** — laddar upp tyst efter varje redigering. Bäst för soloanvändare med snabba, pålitliga anslutningar som redigerar mycket.
- **Uppdatera inte filens metadata** — Evertag redigerar bara den lokala kopian. Användbart för att förhandsgranska ändringar utan att skicka dem till molnet.

### Redigera onlinefiler: rensning av lokal fil

För att redigera en fjärrfil laddar Evertag först ner den till din enhet. Efter redigering väljer du vad som händer med den lokala kopian:

- **Ta alltid bort nedladdad fil** — Evertag tar bort den temporära filen efter redigering. **Rekommenderas** om du har lite lagring eller arbetar med någon annans filer.
- **Ta inte bort nedladdad fil** — behåller den redigerade filen på din enhet. Användbart när du vill ha både en offlinekopia och en uppdaterad molnkopia.

### Knappar på huvudskärmen

Evertags taggredigerar-huvudskärm kan visa eller dölja knappar för enskilda åtgärder. Aktivera bara de du faktiskt använder för att hålla gränssnittet fokuserat:

- **Sök ljudtaggar automatiskt** — hittar saknad metadata online baserat på filens ljudfingeravtryck.
- **Sök ljudtaggar manuellt** — sök efter titel/artist när automatisk sökning misslyckas.
- **Sök albumomslag** — hittar och bäddar in högkvalitativa omslag.
- **Spara albumomslag** — exporterar det inbäddade omslaget till ditt fotobibliotek eller filer.
- **Normalisera kodning** — fixar förvanskad icke-latinsk text orsakad av gamla kodningar (mycket användbart för kyrilliska, kinesiska och japanska spår rippade med äldre programvara).
- **Ta bort ljudtaggar** — tar bort alla taggar från en fil. Användbart före en ren ny taggning.

### Visa utökade taggar

Slå på detta för att visa hela uppsättningen metadatafält bortom basen titel/artist/album/år — inklusive BPM, dirigent, ursprunglig artist, stämning, copyright, encoder, kommentarer, sångtexter och mer. Funktion för power users; de flesta vanliga användare behöver det inte.

### Redigera filer samtidigt

När aktiverad låter Evertag dig redigera metadata på **flera valda filer samtidigt** — sätt samma album-artist, år eller genre för ett helt album i en operation. Detta är det snabbaste sättet att städa upp ett stort oorganiserat bibliotek.

## Redigera taggar för Spotify, Apple Music och strömningsplattformar

En vanlig fråga: «jag redigerade mina taggar i Evertag, laddade upp filerna och strömningstjänsten visar fel metadata. Vad pågår?»

Det korta svaret: **strömningstjänster respekterar inte alltid dina lokala taggar.** Apple Music och Spotify har sina egna interna databaser — när de känner igen ett spår skriver de över de visade metadata med sina egna. Men för **uppladdade filer**, dina lokala filer (Apple Musics «Bibliotek»-funktion, Spotify Local Files) och **distributörsuppladdningar till strömningsplattformar** spelar dina taggar absolut roll. Så här ställer du in Evertag för varje scenario:

### Förbereda filer för Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music hanterar UTF-8 korrekt.
- **Albumomslag: Stor** — Apples appar renderar stora omslag bra; Original är överdrivet.
- **Dubblera taggar: OFF** — inte nödvändigt.
- Se till att **Album Artist** är korrekt ifylld — Apple Music använder den för gruppering.

### Förbereda filer för Spotify Local Files

Spotify Local Files visar bara väl-taggade filer. Taggarna Spotify läser är begränsade.

- **ID3v2.4: ON** i de flesta fall. Om ett spår inte visas korrekt i Spotify efter redigering, **prova att spara med ID3v2.4: OFF** (alltså som ID3v2.3) — Spotifys parser har historiskt varit konservativ gentemot v2.4.
- **Albumomslag: Mellan eller Stor** — Spotify skalar ner det ändå.
- Fyll minst i **Titel**, **Artist**, **Album** och **Spårnummer**.

### Förbereda filer för distributörsuppladdning (DistroKid, TuneCore, CD Baby osv.)

Om du är artist som laddar upp ditt eget verk till strömningsplattformar läser distributören vanligtvis taggar men begär också metadata i sitt gränssnitt. Hur som helst:

- **ID3v2.3** är ofta det säkrare standardvalet — många distributörspipelines byggdes för år sedan och föredrar det äldre formatet.
- Bädda in **Stor** omslag (de flesta distributörer kräver omslag ≥ 1 400 × 1 400 px — kontrollera deras riktlinjer).
- Förlita dig inte på utökade taggar — distributörer läser bara kärnfält.

### Förbereda filer för Plex, Jellyfin, Navidrome, Subsonic, Emby

Dessa självhostade mediaservrar är mycket toleranta. De läser både v2.3 och v2.4 rent och hanterar UTF-8 bra.

- **ID3v2.4: ON** är okej.
- **Albumomslag: Stor** eller **Extra stor** — dessa servrar levererar omslag till mobilklienter och CarPlay-skärmar, så kvaliteten är viktig.
- **Album Artist** rekommenderas starkt — det är det Plex/Jellyfin använder för att gruppera album per artist korrekt.

### Förbereda filer för bilstereo och äldre hårdvara

- **ID3v2.4: OFF** (använd ID3v2.3) — äldre headunits stödjer ofta inte v2.4.
- **Albumomslag: Mellan** — många bildisplayer fastnar på stora inbäddade omslag.
- **Dubblera taggar: ON** — äldre bilstereo läser ibland bara ID3v1-fallback.

## Andra förbättringar

### Liquid Glass-design

Evertag 4.2:s gränssnitt är inställt på Apples nya **Liquid Glass**-material i hela appen — genomskinliga ytor, mjukare animationer och förfinade kontroller som passar naturligt in i iOS, iPadOS och macOS.

### Uppdaterade anslutningsbibliotek

Vi fräschade upp de interna bibliotek som Evertag använder för att kommunicera med **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** och andra tjänster. Resultatet: färre anslutningsfel i kantfall, bättre stöd för nyare serverversioner och förbättrad tillförlitlighet vid taggredigering på fjärrfiler.

### Översättnings- och lokaliseringsfixar

Flera språkfixar i UI:t baserat på direkt återkoppling från användare. Bättre textplacering på små knappar i flera språk.

### Mindre förfiningar inspirerade av din feedback

Många mindre förbättringar baserade på App Store-recensioner och e-post till support@everappz.com. Vi läser varje meddelande.

## Skaffa Evertag 4.2

[**Ladda ner Evertag i App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) eller uppdatera via App Store. Evertag är en gratis nedladdning med valfria uppgraderingar i appen för avancerade funktioner. De nya molnanslutningarna, nätverksprotokollen, Wi-Fi Drive-förbättringarna och Liquid Glass-UI:t är en del av basuppdateringen.

Om du gillar appen, lämna gärna ett betyg i App Store — det hjälper verkligen. Har du feedback eller stötte på ett problem? Maila oss på **support@everappz.com**. Vi läser varje meddelande.

## Vanliga frågor

{{% details title="Vad är nytt i Evertag 4.2?" closed="true" %}}
Evertag 4.2 lägger till över 6 nya moln- och serveranslutningar (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), en uppfräschad Wi-Fi Drive med flerval och smartare uppladdningskö, Liquid Glass UI-uppdateringar, uppdaterade anslutningsbibliotek, viktiga taggredigeringsbuggfixar och översättningsförbättringar.
{{% /details %}}

{{% details title="Ska jag använda ID3v2.4 eller ID3v2.3 i Evertag?" closed="true" %}}
Använd **ID3v2.4** för moderna spelare (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, moderna Android-appar) och för bibliotek med icke-latinska tecken — UTF-8-stöd betyder renare taggar på kinesiska, koreanska, japanska, ryska, arabiska och hebreiska. Använd **ID3v2.3** om dina taggar visas felaktigt i vissa appar, om du siktar på äldre bilstereo eller om en strömnings-distributörspipeline avvisar v2.4. Du kan alltid byta och spara om.
{{% /details %}}

{{% details title="Varför är mina taggar fel i Spotify efter redigering?" closed="true" %}}
Spotify visar mestadels metadata från sin egen katalog — dina lokala taggar används bara för «Local Files» eller innehåll du har laddat upp som artist. Om du taggar filer för Spotify Local Files och de inte visas korrekt, prova att inaktivera ID3v2.4 i Evertag och spara som ID3v2.3 — Spotifys parser har historiskt varit konservativ gentemot v2.4.
{{% /details %}}

{{% details title="Vilken albumomslagsstorlek ska jag välja i Evertag?" closed="true" %}}
För de flesta användare: **Stor**. Det ser bra ut på telefoner, iPads, Macs och moderna bildisplayer utan att blåsa upp filerna för mycket. Använd **Mellan** om du har ett stort bibliotek och vill spara diskutrymme. Använd **Original** (ingen skalning) endast för arkivmastrar eller när du verkligen behöver maximal kvalitet — men var medveten om att vissa äldre spelare kämpar med mycket stora inbäddade omslag. **Original** är en del av Evertags premium-personaliseringsuppgradering.
{{% /details %}}

{{% details title="Kommer större albumomslag göra mina filer större?" closed="true" %}}
Ja. Att bädda in ett 3 000 × 3 000 px omslag kan lägga till flera megabyte till en enskild ljudfil. På ett bibliotek med 1 000 spår blir det gigabyte. Om lagringsutrymmet är knappt, använd Mellan eller Stor; om du strömmar från en NAS där storleken inte spelar roll är Extra stor eller Original okej.
{{% /details %}}

{{% details title="Vad är Dubblera taggar och bör jag aktivera det?" closed="true" %}}
Dubblera taggar skriver kärnmetadata till både ID3v1- (legacy 128-byte) och ID3v2-sektionerna (modern) av filen. Aktivera det bara om du siktar på mycket gamla spelare eller hårdvara som läser ID3v1. För allt modernt (smartphones, datorer, nyare bilstereo) lämna det av.
{{% /details %}}

{{% details title="Redigerar Evertag taggar direkt på molnfiler?" closed="true" %}}
Ja. Anslut till ditt moln (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 osv.) eller via FTP/SFTP/NFS, öppna en fil och redigera taggar som om den vore lokal. Evertag laddar ner filen, applicerar dina ändringar och laddar upp den uppdaterade versionen tillbaka. Du kan välja mellan lägena «Fråga alltid», «Auto-uppladdning» eller «Ladda inte upp» i inställningarna.
{{% /details %}}

{{% details title="Kan jag redigera FLAC-taggar på iPhone med Evertag?" closed="true" %}}
Ja. Evertag stödjer FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE och andra viktiga format med fullt läs-/skrivstöd för taggar inklusive inbäddat omslag.
{{% /details %}}

{{% details title="Hur redigerar jag taggar säkert på min hemmaserver med SFTP?" closed="true" %}}
Öppna Evertag, gå till Anslutningar, välj SFTP och ange serverns värdnamn eller IP, port (vanligtvis 22), användarnamn och antingen ett lösenord eller en privat SSH-nyckel. Evertag bläddrar i dina fjärrmappar och redigerar taggar direkt med end-to-end-kryptering över SSH.
{{% /details %}}

{{% details title="Kan jag redigera taggar på flera filer samtidigt?" closed="true" %}}
Ja. Aktivera **Redigera filer samtidigt** i inställningarna. Välj flera filer, öppna taggredigeraren, och alla fält du ändrar appliceras på alla valda filer. Det här är det snabbaste sättet att sätta samma album-artist, år eller genre på ett helt album.
{{% /details %}}

{{% details title="Är uppdateringen till Evertag 4.2 gratis?" closed="true" %}}
Ja. Evertag är en gratis nedladdning från App Store, och 4.2 är en gratis uppdatering för alla befintliga användare. De nya molnintegrationerna, Wi-Fi Drive-förbättringarna och Liquid Glass-UI:t är en del av basuppdateringen.
{{% /details %}}

{{% details title="På vilka enheter är Evertag 4.2 tillgängligt?" closed="true" %}}
Evertag 4.2 körs på iPhone, iPad och Mac. iCloud Drive-synkronisering håller dina taggredigerar-inställningar konsekventa över enheter.
{{% /details %}}
