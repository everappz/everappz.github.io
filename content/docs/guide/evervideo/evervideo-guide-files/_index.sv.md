---
title: "Filer"
date: 2020-02-01
lastmod: 2026-06-01
description: "Lär dig använda fliken Filer i Evervideo på iPhone, iPad och Mac. Anslut molntjänster, NAS-enheter, mediaservrar och RTSP-strömmar på ett ställe. Hantera offlinevideor, överföringskön, nedladdningar, Wi-Fi Drive, iTunes / Finder File Sharing och USB-enheter. Inkluderar iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA och S3-kompatibel lagring."
keywords: [
  "Evervideo filer", "Evervideo anslutningar", "Evervideo lokala filer",
  "molnvideo-konfiguration iPhone", "anslut Google Drive video", "SMB videoströmning",
  "WebDAV videospelare iOS", "DLNA video iPhone", "NAS videoströmning",
  "Wi-Fi Drive videoöverföring", "Evervideo iTunes File Sharing", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo offline-läge video", "Evervideo överföringskö",
  "Evervideo filhanterare", "Evervideo Documents-mapp",
  "videospelare Synology", "videospelare QNAP",
  "videospelare Apple Time Capsule", "USB DAC video",
  "iXpand videospelare", "S3 videospelare"
]
tags: ["guide", "evervideo", "filer", "anslutningar", "moln", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Fliken Filer är Evervideo's allt-i-ett filhanterare. Till skillnad från de flesta videoappar som delar upp molnlagring från lokala filer i olika flikar, slår Evervideo samman båda i en enda rullningsbar skärm så att du kan gå från en Plex-server till en molnmapp till din iPhones Documents-mapp utan att byta flikar.

Fliken Filer är uppdelad i tydliga sektioner som visas i den här ordningen på skärmen:

- **Snabbåtkomst** — senaste och favoriter för filer och mappar du öppnade senast.
- **Filer i den här applikationen** — vad som finns i Evervideo's sandboxade Documents-mapp.
- **Filer på den här iPhone / iPad / Mac** — videor på andra ställen på din enhet, tillgängliga via systemets filväljare.
- **Molnlagring** — varje molnkonto, NAS och mediaserver du har anslutit.
- **Tillgängliga enheter** — servrar och enheter på ditt lokala nätverk som automatiskt hittats via Bonjour / mDNS.

I det övre högra hörnet av Filer-skärmen finns en Överföringsknapp (en ikon med roterande pilar). Tryck på den för att öppna Överföringskön där du övervakar varje nedladdning och uppladdning från alla dina källor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo filer över anslutna lagringar" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Anslut till molnlagring

Sektionen Molnlagring i fliken Filer är där varje anslutet konto, NAS, mediaserver och ström finns — sida vid sida, i en rullningsbar lista.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo molnlagringssektion i fliken Filer" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Öppna fliken **Filer**.
- Scrolla till sektionen **Molnlagring**.
- Tryck på **Anslut till molnlagring** från menyn.
- Välj en molnlagringstjänst från listan.
- Ange dina uppgifter på den officiella auktoriseringssidan som tillhandahålls av molnleverantören, tryck sedan på **Färdig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo anslut en molnlagringstjänst" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Om du stöter på problem, kontrollera din internetanslutning och ditt inloggning / lösenord. I Premium-versionen av appen kan du lägga till ett obegränsat antal tjänster; gratisversionen stöder upp till tre.

## Stödda molnlagringstjänster, mediaservrar och protokoll

Evervideo stöder ett exceptionellt brett utbud av källor för dina videor. Allt nedan fungerar från ett enda Anslut till molnlagring-flöde.

**Personlig molnlagring:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Självhostade mediaservrar:** Plex · Jellyfin · Emby · Subsonic (och varje Subsonic-kompatibel server — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (och ownCloud via det delade API:et) · Synology Drive · QNAP.

**NAS och fildelningsprotokoll:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, lösenord eller autentisering med offentlig nyckel) · NFS · DLNA / UPnP (uppspelning och nedladdning).

**Live och IP-kameraströmmar:** RTSP — peka Evervideo på valfri `rtsp://`-URL och den spelar bara. Utmärkt för säkerhetskameror, IPTV-strömmar, dörrklockskameror, babymonitorer och liknande livekällor.

**S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces och valfri annan S3-API-slutpunkt.

**Bibliotek på enheten:** Photos-biblioteket (alla videor, skärminspelningar, fotoalbum) och Music-appens bibliotek (Album, Genrer, Spellistor) — båda visas i Mediebiblioteket så att du inte behöver kopiera något.

**Lokal nätverksupptäckt:** sektionen Tillgängliga enheter listar automatiskt varje Bonjour / mDNS-tjänst på ditt Wi-Fi-nätverk — Plex, Jellyfin, Emby-servrar, Synology, QNAP, AirPort-routrar med anslutna enheter, Apple Time Capsule — så att du kan trycka för att ansluta utan att skriva en IP-adress.

Varje anslutning använder tjänstens officiella SDK eller öppna protokoll, med OAuth-baserad auktorisering där det stöds. Du kan ansluta flera konton av samma tjänst (till exempel två Google Drive-konton, eller både en Plex- och en Jellyfin-server) och bläddra dem sida vid sida i sektionen Molnlagring.

## Säkerhet och integritet

Evervideo använder bara officiella SDK:er och säkra anslutningar för att interagera med anslutna molntjänster. Din inloggning och ditt lösenord är inte tillgängliga för applikationen — alla överföringar är TLS-krypterade.

När du anger din inloggning och ditt lösenord visar applikationen den officiella auktoriseringssidan som tillhandahålls av molntjänstleverantören, och hela auktoriseringsprocessen sker utanför applikationen. Molntjänstleverantören skickar sedan ett auth-token till applikationen efter lyckad auktorisering, och det tokenet används för att göra API-anrop.

Ett auth-token är en digital nyckel som tillåter tredjepartsapplikationer att interagera med molnlagring på dina vägnar. Tokenet lagras på din enhet i Apples säkra systemlagring (Keychain), som är krypterad i vila och skyddad av din enhets lösenkod eller biometriskt lås. Du kan ladda ner filer från anslutna molntjänster till din enhet; dessa filer placeras i appens Documents-katalog och kan tas bort när som helst med den inbyggda filhanteraren.

Applikationen delar inte någon information från dina anslutna molnkonton med Everappz, annonsörer eller någon tredje part. Du kan återkalla åtkomst till ditt molnkonto när som helst genom att öppna kontoinställningssidan i din webbläsare.

## Återkalla Auth-Token

För att återkalla ett auth-token, logga in på ditt molnkonto i en webbläsare och navigera till säkerhets- eller anslutna appar-sidan. Där kan du hitta varje tredjepartsapp som är ansluten till ditt molnkonto och ta bort någon av dem om du inte längre vill använda den. Detaljerade instruktioner för Google-konton finns [här](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan också koppla bort molnkontot i applikationen själv — när du gör det tas auth-tokenet omedelbart bort från din enhet. Om du avinstallerar applikationen från din enhet tas alla nedladdade data och åtkomsttokens automatiskt bort med den.

## Koppla bort molnlagring eller ändra konfiguration

- **Åtkomst till molnlagringsalternativ** — leta upp den anslutna tjänsten i sektionen **Molnlagring** i fliken Filer.
- **Tryck på "..."-knappen** bredvid tjänstetiteln för att öppna ytterligare alternativ:
  - **Byt namn** — ändra namnet på molntjänsten som den visas i din lista.
  - **Inställningar** — ändra konfigurationen eller autentiseringsdata. Ibland kan du behöva omauktorisera den anslutna molntjänsten om auktoriseringstokenet har gått ut.
  - **Koppla bort** — bryt fullständigt anslutningen mellan appen och molntjänsten. Detta tar bort alla videor kopplade till den tjänsten från ditt mediebibliotek, men lämnar dem orörda på servern.

## Anslut till en dator eller NAS

Du kan ansluta din dator, personliga NAS eller annan nätverksenhet med SMB, WebDAV, FTP / FTPS, SFTP, NFS eller DLNA-protokollet. Detta är det enklaste sättet att ta in ett befintligt hemmemediebibliotek — oavsett om det bor på en Mac, Windows-PC, Synology, QNAP, Apple Time Capsule eller WD My Cloud Home — i Evervideo utan att kopiera något.

### Anslut till en dator med SMB

- Tryck på **Anslut till molnlagring → SMB**.
- Ange datorns IP-adress och namn på den delade mappen med formatet `smb://computer-ip-address/shared-folder-name`.
- Välj protokollversion: **Auto**, **SMB1** eller **SMB2**.
- Ange din inloggning och ditt lösenord (om det krävs).
- Tryck på **Färdig**.

Om anslutningen lyckas visas resursen i sektionen Molnlagring. En fullständig handledning om hur du ansluter din Mac eller PC med SMB finns [här](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Anslut till en NAS med WebDAV

Alla steg är desamma som SMB, förutom URL-fältet. Använd `http://server-name` eller `https://server-name` om servern stöder SSL. WebDAV fungerar med Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home och vilken annan server som helst med en WebDAV-slutpunkt.

En fullständig handledning om WebDAV finns [här](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Anslut via DLNA / UPnP

Dela ett mediebibliotek på din Windows-PC eller NAS med DLNA / UPnP-protokollet och kom åt det i Evervideo som beskrivs [här](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA stöds brett men tillåter dig bara att spela eller ladda ner videor — du kan inte ladda upp filer eller skapa nya mappar på en DLNA-server.

### Anslut med FTP, FTPS eller SFTP

Evervideo stöder också de klassiska filöverföringsprotokollen. För att ansluta en server via FTP eller FTPS, tryck på Anslut till molnlagring → FTP, ange värd-URL:en i formen `ftp://server-name` (eller `ftps://server-name` för en krypterad anslutning), ange din inloggning och ditt lösenord, tryck sedan på Färdig. För SFTP (SSH File Transfer Protocol), välj SFTP istället och ange antingen ett lösenord eller ett SSH-nyckelpar.

### Anslut till en NFS-resurs

Evervideo inkluderar NFS (Network File System)-stöd — praktiskt för Linux-värdar, BSD-servrar och NAS-enheter som föredrar att exponera videobibliotek via NFS istället för SMB. Välj NFS i menyn Anslut till molnlagring, ange serveradressen och den exporterade sökvägen, och tryck på Färdig.

## Anslut en Plex Media Server

Evervideo kan ansluta direkt till en Plex Media Server och bläddra i dina Film-, TV-serier- och Hemvideobi­bliotek. Tryck på Anslut till molnlagring → Plex, logga in med ditt Plex-konto, välj en server och biblioteket visas bredvid dina molntjänster. Plex-servrar i samma lokala nätverk upptäcks också automatiskt i sektionen Tillgängliga enheter.

## Anslut en Jellyfin- eller Emby-server

Båda Jellyfin (öppen källkod) och Emby (kommersiell) mediaservrar fungerar nativt i Evervideo. Tryck på Anslut till molnlagring → Jellyfin eller Emby, ange din server-URL (vanligtvis något som `http://server-ip:8096`) och uppgifter, och ditt bibliotek är redo att strömmas.

## Anslut en Subsonic- eller Navidrome-server

Evervideo talar Subsonic API, vilket innebär att det fungerar med Subsonic, Navidrome och varje annan Subsonic-kompatibel server — inklusive Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) och Ampache. Tryck på Anslut till molnlagring → Subsonic, ange server-URL och uppgifter, och biblioteket visas i sektionen Molnlagring.

## Anslut en RTSP-ström (IP-kameror, Live-TV, IPTV)

Evervideo har inbyggt RTSP-stöd, så du kan peka det på vilken RTSP-källa som helst — säkerhetskameror, dörrklockskameror, IPTV-leverantörer, babymonitorer, sändningsflöden — och Evervideo hämtar och avkodar strömmen live. Tryck på Online-länkar → Lägg till länk, klistra in hela URL:en (`rtsp://camera-ip:port/stream-path`), ange inloggning och lösenord om det krävs, och tryck på Färdig.

## Anslut till S3-kompatibel objektlagring

För självhostare och avancerade användare som använder molnobjektlagring inkluderar Evervideo en S3-kompatibel kontakt. Tryck på Anslut till molnlagring → S3-lagring, ange sedan slutpunkts-URL, region, åtkomstnyckel, hemlig nyckel och bucketnamn. Detta fungerar med AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces och valfri annan S3-API-slutpunkt.

## Tillgängliga enheter

Den här sektionen visar varje enhet i ditt lokala nätverk som du kan ansluta till från Evervideo via Bonjour / mDNS-identifiering — Plex, Jellyfin, Emby-servrar, Synology, QNAP, AirPort-routrar med anslutna enheter, Apple Time Capsule och så vidare. Så här upprättar du en anslutning:

- Scrolla till sektionen Tillgängliga enheter i fliken Filer.
- Tryck på enheten du vill ansluta till.
- Om det behövs, ange dina inloggningsuppgifter för att slutföra anslutningen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo tillgängliga enheter i det lokala nätverket" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive låter dig trådlöst överföra filer från din dator till din iOS-enhet via valfri skrivbordswebbläsare, Finder eller File Explorer. Din enhet och dator måste vara på samma Wi-Fi-nätverk.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Aktivera Wi-Fi Drive

- I fliken Filer, scrolla till Molnlagring → Anslut via Wi-Fi för att öppna Wi-Fi Drives huvudskärm.
- (Valfritt) Ange ett användarnamn och lösenord för den inbyggda webbservern.
- Tryck på Starta Wi-Fi Drive.

### Åtkomst till Wi-Fi Drive på din dator

- Öppna en webbläsare på din dator (Chrome, Firefox, Safari osv.).
- Ange URL:en som visas av applikationen.
- Dra och släpp filer från din dator på webbsidan — de börjar överföras till din iOS-enhet.

Du kan också montera Wi-Fi Drive direkt i **Finder** på macOS (Gå → Anslut till server…) eller File Explorer på Windows (Kartlägg nätverksenhet…) och behandla din iPhone eller iPad som en vanlig nätverksenhet.

Detaljerade instruktioner finns [här](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (nu Finder File Sharing på macOS Catalina och senare) låter dig överföra filer med en Lightning- eller USB-C-kabel. Anslut enheten, öppna Finder på Mac (eller iTunes på Windows), hitta Evervideo i applistan och kopiera filer till dess delade mapp.

## Anslut ett USB-minne eller SD-kort

Anslut ett USB-minne eller SD-kort till din iPhone, iPad eller Mac via Lightning-till-USB / USB-C-adaptern eller kortläsaren. Öppna Filer → Filer på den här iPhone → Öppna mapp, navigera till enheten och välj en videofil eller mapp. Evervideo spelar filer direkt från enheten utan att kopiera dem till intern lagring — praktiskt för mycket stora 4K-bibliotek.

## Mappbläddring i anslutna lagringar

Tryck på en ansluten molntjänst för att öppna dess filbläddrare. Mappar visar videominiatyrer när de är tillgängliga, och att trycka på en video startar uppspelning omedelbart medan resten av filen fortsätter att strömmas i bakgrunden.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo bläddrar i mappar i anslutna lagringar" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Snabbåtkomst

Sektionen Snabbåtkomst finns längst upp i fliken Filer. Den ger dig snabb åtkomst till dina favorit- och nyligen öppnade filer och mappar — både från molntjänster och från enhetslagring. Varje gång du öppnar en fil eller mapp från molnet läggs den till i listan Nyligen öppnade. Du kan markera djupt nästlade mappar som Favoriter för att komma åt dem snabbt utan att gräva igenom katalogstrukturen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo onlinelänkar och snabbåtkomst" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Filer i den här applikationen

Den här sektionen visar filer och mappar lagrade i Evervideo's sandboxade Documents-katalog — allt du har laddat ner från molnet, överfört via Wi-Fi Drive, kopierat via Finder File Sharing eller importerat från en annan app.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo filer i den här applikationen" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Documents-mappen

Documents-mappen är roten till allt inuti Filer i den här applikationen. Du kan skapa undermappar, byta namn på filer, flytta runt dem och gruppera dem hur du vill.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo lokala filer — Documents-mappen" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Filer på den här iPhone / iPad / Mac

Den här sektionen visar videor på din enhet men i olika applikationer. Du kan importera dem till Evervideo med systemets filväljare:

- Tryck på Öppna filer… för att välja specifika filer.
- Tryck på Öppna mapp… för att välja en hel mapp.

Du kan också använda Anslut en mapp för att skapa en länk till en mapp på din enhet med läs / skrivåtkomst — perfekt för att arbeta med en mapp på iCloud Drive eller en ansluten USB-enhet utan att kopiera något.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo filer på den här enheten" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Specialmappar

Inom fliken Filer ser du flera specialmappar som Evervideo skapar och använder automatiskt:

- **Nedladdningar** — varje fil som laddats ned från molnet visas här som standard. Anpassa i Inställningar → Filhanterare → Spara nedladdade filer till.
- **Spelarcache** — mediaspelarens cache. Som standard laddar spelaren ner kommande videor för smidig uppspelning. Du kan inaktivera cachen i appinställningarna eller helt enkelt ta bort den här mappen.
- **iCloud** — filer i den här mappen synkroniseras över alla dina enheter anslutna till samma iCloud-konto.
- **Offline mappar** — när du markerar en mapp, spellista, album eller genre som tillgänglig offline laddas filerna ner till den här mappen.

## Övre verktygsfält

Det övre verktygsfältet, placerat under navigeringsfältet, erbjuder flera åtgärder som du kan visa eller dölja med ett svepningsgestur nedåt:

- **Sök** — utför en sökning i den aktuella mappen eller sektionen.
- **Fortsätt uppspelning** — om det är aktiverat i inställningarna, återställ spelarkön och den senaste videopositionen för den aktuella mappen.
- **Spela alla** — skanna den aktuella mappen och dess undermappar och lägg till filer i spelarkön.
- **Blanda alla** — som Spela alla, men blandas innan de läggs till.

## Mappalternativ

När du öppnar en mapp, tryck på **"..."-knappen** i det övre högra hörnet för dessa åtgärder:

- **Välja** — aktivera filvalläge.
- **Ny mapp** — skapa en ny mapp inom den aktuella mappen.
- **Aktivera offline-läge** — slå på offlinesynkronisering för den aktuella mappen. Nya filer som läggs till online laddas ner automatiskt.
- **Ladda upp filer** — ladda upp filer från din enhet till onlinemappen.
- **Sök** — sök i mappen.
- **Sortera** — sortera filer efter namn, storlek, ändringsdatum eller metadata.
- **Rutnät / Listvy** — växla mellan tabellvy och miniatyrvy. Miniatyrvy visar stora videoförhandsvisningar.

## Urvalsläge

Tryck på **"..."** i det övre högra hörnet och välj **Välja** för att gå in i urvalsläge. Kryssrutor visas bredvid varje fil och mapp. Tryck för att välja ett eller flera objekt, utför sedan batchåtgärder: Spela nästa, Spela senare, Lägg till i mediebibliotek, Lägg till i en spellista, Kopiera, Ladda upp, Flytta, Byt namn eller Ta bort.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo urvalsläge i filhanteraren" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Om du hellre behandlar ansluten molnlagring som skrivskyddad (för att förhindra oavsiktliga raderingar), aktivera Inställningar → Filhanterare → Redigera onlinefiler → Av för att dölja alla destruktiva åtgärder från UI.

## Filåtgärder

Tryck på **"..."**-ikonen nära en fils titel för att visa dess åtgärdsmeny:

- **Spela nästa** — infoga filen längst upp i spelarkön.
- **Spela senare** — lägg till filen längst ner i spelarkön.
- **Lägg till i mediebibliotek** — integrera filen i ditt mediebibliotek, organiserat efter Album och Genre.
- **Lägg till i en spellista** — lägg till filen i en befintlig spellista eller skapa en ny.
- **Redigera taggar** — öppna den inbyggda taggredigeraren för att ändra metadata. För onlinefiler laddas filen tillfälligt ner, redigeras och laddas sedan upp igen efter att du bekräftar.
- **Lägg till i favoriter** — lägg till filen i din favoritlista för snabb åtkomst.
- **Ladda ner** — ladda ner filen eller mappen till din enhet för offlineanvändning.
- **Byt namn** — byt namn på filen direkt på fjärrlagringen.
- **Flytta** — flytta filen till en annan mapp i din molnlagring.
- **Lägg till i arkiv** — paketera filen i en enda ZIP-fil (Premium-funktion).
- **Öppna i** — exportera filen till en annan kompatibel app via systemets Dela-ark.
- **Ta bort** — ta bort filen permanent. **Den här åtgärden kan inte ångras.**

## Mappåtgärder

För varje mapp i din molnlagring finns det många åtgärder tillgängliga genom att trycka på **"..."**-ikonen bredvid mapptiteln.

- **Spela alla** — ersätt den aktuella spelarkön med varje video i mappen.
- **Spela nästa / Spela senare** — lägg till hela mappen i kön.
- **Lägg till i mediebibliotek** — integrera mappens innehåll i ditt mediebibliotek.
- **Lägg till i spellista** — lägg till hela mappen i en spellista.
- **Lägg till i favoriter** — lägg till mappen i dina favoriter.
- **Aktivera offline-läge** — utöver en enkel nedladdning övervakar detta kontinuerligt mappen för nya filer och laddar automatiskt ner dem när de visas online.
- **Ladda ner** — ladda ner allt innehåll i mappen till din enhet för offlineåtkomst.
- **Byt namn / Flytta** — byt namn på eller flytta mappen i fjärrlagringen.
- **Lägg till i arkiv** — paketera mappinnehållet i en ZIP-fil (Premium-funktion).
- **Ta bort** — ta bort mappen och dess innehåll permanent. **Den här åtgärden kan inte ångras.**

## Överföringskö

I det övre högra hörnet av fliken Filer finns en **Överförings**-knapp (en ikon med roterande pilar). Tryck på den för att öppna Överföringskön — en lista över varje aktiv nedladdning och uppladdning från alla dina källor, med realtidsprogress, hastighet och ETA per fil.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo filöverföringskö" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Du kan pausa, återuppta, försöka igen med misslyckade överföringar, ordna om objekt för att prioritera specifika nedladdningar eller avbryta dem individuellt. Du kan också justera överföringskö-hastigheten (maximalt parallella uppgifter), nätverkstyp (endast Wi-Fi eller Wi-Fi + Cellular) och bakgrundsöverföringar i Inställningar → Filhanterare.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo åtgärder för filöverföringskön" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offlineläge och synkroniserade offlinemappar

Offlineläge är en praktisk funktion som låter dig titta på dina favoritvideor även när du inte är ansluten till internet. När du aktiverar offlineläge för en mapp, spellista, album eller genre laddas automatiskt alla filer i den samlingen ner till din enhet för offline uppspelning. De visas i sektionen Offline mappar.

När du lägger till nya filer på fjärrservern laddas de också automatiskt ner — så din offlinesamling förblir aktuell utan att du behöver göra något. För att manuellt synkronisera om, tryck på tre punkter i det övre högra hörnet av en offlinemapp och välj Synkronisera.

Du kan justera synkroniseringstidsgränsen i Inställningar → Filhanterare → Synkroniserade offline-mappar → Tidsintervall.

Detaljerade instruktioner finns [här](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalisering

I Inställningar → Personalisering kan du konfigurera hur fliken Filer presenteras:

- **Filterskärmsformat** — Enkel meny (visar mapplistan direkt) eller Grupperad meny (grupperar innehåll efter kategori — Snabbåtkomst, Specialmappar, Molnlagring osv.).
