---
title: "Anslutningar"
date: 2020-02-01
description: "Lär dig hur du ansluter molntjänster och NAS-enheter till Flacbox. Strömma högupplöst musik från iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk och mer. Använd SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder Fildelning och USB-flashenheter."
keywords: [
  "Flacbox molninställning", "anslut Google Drive till Flacbox", "SMB musikströmning",
  "WebDAV iOS-spelare", "DLNA musikapp", "NAS-ljudströmning", "Wi-Fi Drive iPhone",
  "överför filer till iPhone", "Flacbox iTunes Fildelning", "anslut NAS till iPhone",
  "Synology Drive musikapp", "QNAP musikapp", "Bluesound musikapp",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm scrobbling musikapp",
  "iXpand Flash Drive musik", "USB DAC iPhone"
]
tags: ["guide", "flacbox", "anslutningar", "moln", "NAS"]
readingTime: 12
---


På den här skärmen kan du ansluta alla källor som innehåller din musik. Du kan integrera populära molntjänster som Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive och många fler, samt din Mac, PC eller NAS via standardprotokoll. Oavsett om din samling finns på en strömningsvänlig tjänst som Dropbox eller på en personlig NAS som en Synology, QNAP, Buffalo, Apple Time Capsule eller WD My Cloud Home, ansluter Flacbox till dem alla från en enda skärm.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox anslutningsskärm" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Anslut till molnlagring

- Öppna fliken **Anslutningar**.
- Välj **Anslut till molnlagring** från menyn.
- Välj en molnlagringstjänst från listan.
- Ange dina uppgifter på den officiella auktoriseringssidan som tillhandahålls av molnleverantören och tryck sedan på **Färdig**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox lägg till en molnlagringstjänst" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Om du stöter på problem, kontrollera din internetanslutning och ditt inloggnings- / lösenord. I premiumversionen av appen kan du lägga till ett obegränsat antal tjänster; gratisversionen stöder upp till tre.

## Stödda molnlagringstjänster, medieservrar och protokoll

Flacbox stöder ett exceptionellt brett utbud av källor för din musik. Allt nedan fungerar från en enda skärm för **Anslut till molnlagring**.

**Personlig molnlagring:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Självhostade servrar:** Plex · Jellyfin · Emby · Subsonic (och alla Subsonic-kompatibla servrar — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (och ownCloud via det delade API:et) · Synology Drive · QNAP.

**NAS och fildelningsprotokoll:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH-filöverföringsprotokoll, lösenord eller autentisering med offentlig nyckel) · NFS · DLNA / UPnP (uppspelning och nedladdning).

**S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces och alla andra S3-API-slutpunkter.

**Lokalt nätverksupptäckt:** Avsnittet Tillgängliga enheter listar automatiskt alla Bonjour / mDNS-tjänster på ditt Wi-Fi-nätverk så att du kan trycka för att ansluta utan att skriva en IP-adress.

Varje anslutning använder **officiellt SDK eller öppet protokoll** från tjänsten, med OAuth-baserad auktorisering där det stöds. Du kan ansluta flera konton av samma tjänst (till exempel två Google Drive-konton, en personlig Dropbox bredvid en arbets-Dropbox, eller både en Plex- och en Jellyfin-server) och bläddra bland dem sida vid sida på anslutningsskärmen.

## Säkerhet och integritet

Vi använder endast officiella SDK:er och säkra anslutningar för att interagera med anslutna molntjänster. Ditt inloggningsnamn och lösenord är inte tillgängliga för applikationen — alla överföringar är TLS-krypterade.

När du anger ditt inloggningsnamn och lösenord visar applikationen den officiella auktoriseringssidan från molntjänstleverantören, och hela auktoriseringsprocessen sker utanför applikationen. Molntjänstleverantören skickar sedan en auth-token till applikationen efter lyckad auktorisering, och den token används för API-anrop.

En auth-token är en digital nyckel som gör det möjligt för tredjepartsapplikationer att interagera med molnlagring för din räkning. Token lagras på din enhet i Apples säkra systemlagring (Keychain), som är krypterad i vila och skyddad av din enhets lösenkod eller biometriskt lås. Du kan ladda ner filer från anslutna molntjänster till din enhet; dessa filer placeras i appens Documents-katalog och kan tas bort när som helst med den inbyggda filhanteraren.

Applikationen delar ingen information från dina anslutna molnkonton med Everappz, annonsörer eller tredje part. Du kan återkalla åtkomst till ditt molnkonto när som helst genom att öppna kontoinställningssidan i din webbläsare.

## Återkalla auth-token

För att återkalla en auth-token, logga in på ditt molnkonto i en webbläsare och navigera till sidan för säkerhet eller anslutna appar. Där kan du hitta alla tredjepartsappar som är anslutna till ditt molnkonto och ta bort vilken som helst om du inte längre vill använda den. Detaljerade instruktioner för Google-konton finns [här](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan också koppla bort molnkontot i applikationen själv — när du gör det raderas auth-token omedelbart från din enhet. Om du avinstallerar applikationen från din enhet tas alla nedladdade data och åtkomsttokens bort automatiskt med den.

## Koppla bort molnlagring eller ändra konfiguration

- **Öppna molnlagringsalternativ** — hitta den anslutna tjänsten på skärmen **Anslutningar**.
- **Tryck på knappen "..."** bredvid tjänstens titel för att öppna ytterligare alternativ:
  - **Byt namn** — ändra namnet på molntjänsten som den visas i din lista.
  - **Inställningar** — ändra konfigurationen eller autentiseringsdata. Ibland kan du behöva återauktorisera den anslutna molntjänsten om auktoriseringstoken har upphört att gälla.
  - **Koppla bort** — kapa helt anslutningen mellan appen och molntjänsten. Detta tar bort alla låtar som är kopplade till den tjänsten från appens musikbibliotek, men lämnar dem orörda på servern.

## Anslut till en dator eller NAS

Du kan också ansluta din dator, personliga NAS eller andra nätverksenheter med SMB-, DLNA- eller WebDAV-protokoll. Det här är det enklaste sättet att ta in ett befintligt hemmamusikbibliotek — oavsett om det finns på en Mac, en Windows-PC, en Synology-box eller en NAS — i Flacbox utan att kopiera något.

## Anslut till en dator med SMB

- Tryck på **Anslut till molnlagring → SMB**.
- Ange datorns IP-adress och delade mappnamn i URL-fältet med formatet `smb://dator-ip-adress/delade-mappnamnet`.
- Välj protokollversion: **Auto**, **SMB1** eller **SMB2**.
- Ange ditt inloggningsnamn och lösenord (om det krävs).
- Tryck på **Färdig**.

Om anslutningen lyckas ser du den anslutna lagringen i avsnittet **Molnlagring**. En fullständig handledning om hur du ansluter din Mac eller PC med SMB finns [här](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Anslut till en NAS med WebDAV

Alla steg är desamma som för SMB, förutom URL-fältet. URL:en ska vara i formatet `http://servernamn` eller `https://servernamn` om servern stöder SSL. WebDAV fungerar med **Synology, QNAP, Nextcloud, ownCloud** och många andra servrar — var ett WebDAV-slutpunkt är tillgänglig.

En fullständig handledning om hur du ansluter en NAS med WebDAV finns [här](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Anslut till en dator eller NAS med DLNA

Du kan också dela ett musikbibliotek som finns på din Windows-PC eller personliga NAS med DLNA / UPnP-protokollet och komma åt det biblioteket i appen som beskrivs [här](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA är ett populärt, allmänt stödt protokoll, men det låter dig bara spela eller ladda ner musik — du kan inte ladda upp filer eller skapa nya mappar på en DLNA-server.

## Anslut till en NAS eller server med FTP, FTPS eller SFTP

Flacbox stöder också de klassiska filöverföringsprotokollen. För att ansluta en server via FTP eller FTPS, tryck på **Anslut till molnlagring → FTP**, ange värd-URL:en i formatet `ftp://servernamn` (eller `ftps://servernamn` för en krypterad anslutning), ange ditt inloggningsnamn och lösenord och tryck sedan på **Färdig**. För **SFTP** (SSH-filöverföringsprotokoll), välj **SFTP** i stället och ange antingen ett lösenord eller ett SSH-nyckelpar. Båda fungerar med NAS-enheter, Linux-värdar och alla servrar som har en FTP / FTPS / SSH-daemon.

## Anslut till en NFS-resurs

Flacbox inkluderar stöd för **NFS** (Network File System) — praktiskt för Linux-värdar, BSD-servrar och NAS-enheter som föredrar att exponera musikbibliotek via NFS i stället för SMB. Välj **NFS** i menyn **Anslut till molnlagring**, ange serveradressen och den exporterade sökvägen och tryck på **Färdig**.

## Anslut en Plex Media Server

Flacbox kan ansluta direkt till en Plex Media Server och bläddra i ditt musikbibliotek efter Artister, Album, Genrer och Spellistor. Tryck på **Anslut till molnlagring → Plex**, logga in med ditt Plex-konto, välj en server, och biblioteket visas bredvid dina molntjänster. Plex-servrar på samma lokala nätverk identifieras också automatiskt i avsnittet **Tillgängliga enheter**.

## Anslut en Jellyfin- eller Emby-server

Både **Jellyfin** (öppen källkod) och **Emby** (kommersiell) medieservrar fungerar nativt i Flacbox. Tryck på **Anslut till molnlagring → Jellyfin** eller **Emby**, ange din server-URL (något som `http://server-ip:8096`) och dina uppgifter, och ditt musikbibliotek är klart att strömma. Precis som med Plex listas bibliotek på det lokala nätverket automatiskt under **Tillgängliga enheter**.

## Anslut en Subsonic- eller Navidrome-server

Flacbox stöder Subsonic API, vilket innebär att det fungerar med **Subsonic** själv, **Navidrome** och alla andra Subsonic-kompatibla servrar — inklusive Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Tryck på **Anslut till molnlagring → Subsonic**, ange server-URL och uppgifter, och biblioteket visas på anslutningsskärmen. Det här är det enklaste sättet att ge Flacbox tillgång till en självhostad musiksamling utan att exponera den underliggande filresursen.

## Anslut till S3-kompatibel objektlagring

För självhostare och audiofiler som använder molnobjektlagring inkluderar Flacbox en S3-kompatibel anslutning. Tryck på **Anslut till molnlagring → S3-lagring**, ange sedan slutpunkts-URL, region, åtkomstnyckel, hemlig nyckel och bucketnamn. Det fungerar med AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces och alla andra tjänster som exponerar en S3-API-slutpunkt.

## Tillgängliga enheter

Det här avsnittet visar alla enheter på ditt lokala nätverk som du kan ansluta till från Flacbox via Bonjour-upptäckt. Följ dessa steg för att upprätta en anslutning:

- Öppna appen och gå till avsnittet **Tillgängliga enheter** under Anslutningar.
- Tryck på den enhet du vill ansluta till.
- Om det behövs, ange dina inloggningsuppgifter för att slutföra anslutningen.

Det här är det snabbaste sättet att hitta en SMB-, WebDAV- eller DLNA-resurs på ditt hemnätverk utan att manuellt skriva IP-adresser.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox tillgängliga enheter på det lokala nätverket" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive är en bekväm teknik som möjliggör trådlösa filöverföringar från din dator till din iOS-enhet via valfri skrivbordswebbläsare. För att använda den här funktionen effektivt, se till att din enhet och dator är anslutna till samma Wi-Fi-nätverk. Här är en steg-för-steg-guide om hur du använder Wi-Fi Drive.

### Aktivera Wi-Fi Drive

- Öppna applikationen och gå till fliken **Anslutningar**.
- Välj **Anslut via Wi-Fi** för att komma åt Wi-Fi Drive-huvudskärmen.
- (Valfritt) Ange ett användarnamn och lösenord för den inbyggda webbservern för att skydda åtkomsten.
- Tryck på **Starta Wi-Fi Drive** för att aktivera Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Öppna Wi-Fi Drive på din dator

- På din dator (stationär eller bärbar), öppna en webbläsare (till exempel Chrome, Firefox eller Safari).
- Ange den URL som tillhandahålls av applikationen i webbläsarens adressfält.

### Överför filer trådlöst

När webbsidan som motsvarar din iOS-enhet öppnas i webbläsaren kan du enkelt dra och släppa filer från din dator på webbsidan. Filerna du släpper börjar överföras till din iOS-enhet och är tillgängliga i Flacbox.

Du kan också montera Wi-Fi Drive direkt i Finder på macOS (Gå → Anslut till server…) eller Utforskaren i Windows (Mappa nätverksenhet…) och behandla din iPhone eller iPad som en vanlig nätverksenhet.

Detaljerade instruktioner om hur du överför filer trådlöst med Wi-Fi Drive finns [här](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder Fildelning

iTunes Fildelning (nu Finder Fildelning på macOS Catalina och senare) är ett annat sätt att överföra filer från en dator till en enhet med en Lightning- eller USB-C-kabel.

- Anslut enheten till datorn med en kabel och kör **Finder** på Mac (eller **iTunes** på Windows).
- Öppna **Platser → Din anslutna enhet → Filer** och hitta Flacbox-appen.
- Tryck på appsymbolen för att se alla delade mappar.
- Kopiera filer från datorn till den delade mappen på enheten med dra-och-släpp.

Detaljerade instruktioner om hur du använder Finder Fildelning finns [här](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Anslut en USB-flashenhet

Om du har ett SD-kort eller en USB-enhet kan du ansluta den med en Lightning till USB / SD-kortläsare eller en USB-C-enhet (på iPad och iPhone 15 / 16 / 17 / Pro). Appen stöder Apple-certifierade kortläsare och iXpand Flash Drives. Med en iXpand Flash Drive, sätt in den i Lightning-porten och öppna applikationen — du ser ett meddelande om att en extern enhet är ansluten samt enhetsinformation. Tryck på flashenhetens ikon för att komma åt musikmappen och tryck på en ljudfil för att börja spela.

Vi har detaljerade instruktioner om hur du ansluter en USB-flashenhet till din iPhone och lyssnar på musik eller hanterar filer på den [här](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Filhanteraren

När du har anslutit en molnlagringstjänst trycker du på dess ikon för att visa alla tillgängliga filer och mappar. Du kan använda den inbyggda filhanteraren för att arbeta med dessa filer — ladda ner, byta namn, flytta, ladda upp, ta bort och mer. När du startar en nedladdning visas filen i överföringskön. För att öppna överföringskön, gå till fliken Lokala filer och tryck på ikonen med snurrande pilar i det övre vänstra hörnet. Alla nedladdade filer och mappar finns i avsnittet Lokala filer.

## Övre verktygsfält

Det övre verktygsfältet, som är bekvämt placerat under navigeringsfältet, erbjuder flera användbara åtgärder för enkel åtkomst. Du kan visa eller dölja det med en enkel svep-ned-gest.

- **Sök** — utför en snabbsökning i den aktuella katalogen, vilket gör det enkelt att hitta specifika filer eller mappar.
- **Fortsätt uppspelning** — om det är aktiverat i appinställningarna återställer detta ljudspelarens kö och den senaste mediepositionen för den aktuella mappen. Ett praktiskt sätt att fortsätta där du slutade.
- **Spela alla** — skannar den aktuella mappen och dess undermappar och lägger sedan till alla hittade ljudfiler i en ny spelarkö. Användbart när du vill spela varje spår i en katalog.
- **Blanda alla** — som Spela alla, men blandar filerna innan de läggs till i ljudspelarens kö. Bra för att återupptäcka en gammal musikmapp.

## Mappalternativ

När du öppnar en mapp hittar du en praktisk uppsättning åtgärder genom att trycka på knappen **"..."** i det övre högra hörnet.

- **Välja** — aktivera filvalläge. Det låter dig välja en eller flera filer i mappen och utföra åtgärder på hela urvalet.
- **Ny mapp** — skapa en ny mapp i den aktuella mappen. Bra för att hålla ditt bibliotek välstrukturerat.
- **Aktivera offline-läge** — aktivera offline-läge för den aktuella mappen. Offline-läge går bortom enkel nedladdning: det övervakar aktivt mappen efter ändringar. Om du lägger till nya filer online visas de automatiskt på din enhet.
- **Ladda upp filer** — ladda upp filer från din enhet till den onlinemappen. Det gör dem tillgängliga var som helst via samma molntjänst.
- **Sök** — sök efter specifika filer i den aktuella mappen.
- **Sortera** — sortera filer efter namn, storlek, ändringsdatum eller metadata. Standardsorteringsläget speglar sorteringsordningen på servern, men du kan ändra det efter dina önskemål.
- **Rutnät / Listvy** — växla mellan tabellvy och miniatyrvy. Tabellvy visar en kompakt lista; miniatyrvy visar stora omslagsbilder för snabb visuell identifiering.

## Redigera onlinefiler

När du behöver hantera flera filer i din molnlagring, använd **Markeringsläge** för att effektivisera dina åtgärder:

- **Aktivera markeringsläge** — tryck på knappen **"..."** i det övre högra hörnet och välj **Välja**.
- **Välj filer** — kryssrutor visas bredvid varje fil och mapp. Tryck för att välja ett eller flera objekt.
- **Utför åtgärder** — när du har valt filerna eller mapparna får du tillgång till Spela härnäst, Spela senare, Lägg till i musikbibliotek, Lägg till i en spellista, Kopiera, Ladda upp, Flytta, Byt namn och Ta bort.

Om du hellre vill behandla ansluten molnlagring som skrivskyddad (för att förhindra oavsiktliga borttagningar), aktivera Inställningar → Filhanteraren → Redigera onlinefiler → Av för att dölja alla destruktiva åtgärder från gränssnittet.

## Filåtgärder

Tryck på ikonen **"..."** nära en fils titel för att visa åtgärdsmenyn:

- **Spela härnäst** — lägg in filen överst i spelarkön, så den spelas direkt efter det aktuella spåret.
- **Spela senare** — lägg till filen längst ned i spelarkön.
- **Lägg till i musikbibliotek** — inkludera filen i ditt musikbibliotek, organiserat efter artist, album, genre eller kompositör.
- **Lägg till i en spellista** — lägg till filen i en befintlig spellista eller skapa en ny.
- **Redigera ljudtaggar** — öppna den inbyggda taggredigeraren för att ändra metadata. För onlinefiler laddas spåret temporärt ner, redigeras och laddas sedan upp igen när du bekräftar.
- **Lägg till i favoriter** — lägg till filen i din favoritlista för snabb åtkomst.
- **Ladda ner** — ladda ner filen eller mappen till din enhet för offline-användning.
- **Byt namn** — byt namn på filen direkt på fjärrlagringen.
- **Flytta** — flytta filen till en annan mapp i din molnlagring.
- **Öppna i** — exportera filen till en annan kompatibel app. Filen laddas ner till din enhet och sedan visas systemets delningsblad.
- **Ta bort** — ta bort filen permanent från din molnlagring. **Den här åtgärden kan inte ångras.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox fler åtgärder för en fil i ansluten molnlagring" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Om listan med åtgärder överskrider det tillgängliga skärmutrymmet, rulla bara ned i åtgärdsmenyn för att se fler alternativ.

## Mappåtgärder

För varje mapp i din molnlagring finns ett brett urval av åtgärder tillgängliga genom att trycka på ikonen **"..."** bredvid mapptiteln. Om du inte ser alla åtgärder, rulla ned för att visa fler.

- **Spela alla** — ersätt den aktuella spelarkön med allt innehåll i den valda mappen.
- **Spela härnäst** — lägg till hela mappen överst i spelarkön.
- **Spela senare** — lägg till mappinnehållet längst ned i spelarkön.
- **Lägg till i musikbibliotek** — inkludera mappens innehåll i ditt musikbibliotek.
- **Lägg till i spellista** — lägg till hela mappen i en spellista. Du har också möjlighet att skapa en ny spellista; dess namn fylls i automatiskt från mappnamnet.
- **Lägg till i favoriter** — lägg till mappen i dina favoriter för snabb åtkomst.
- **Aktivera offline-läge** — utöver en enkel nedladdning övervakar detta kontinuerligt mappen efter nya filer och laddar automatiskt ner dem när de visas online.
- **Ladda ner** — ladda ner allt innehåll i mappen till din enhet för offline-åtkomst.
- **Byt namn** — byt namn på mappen direkt på fjärrlagringen.
- **Flytta** — flytta mappen till en annan plats i din molnlagring.
- **Arkivera (ZIP)** — packa ihop mappinnehållet till en enda ZIP-fil (premiumfunktion).
- **Ta bort** — ta bort mappen och dess innehåll permanent från din molnlagring. **Den här åtgärden kan inte ångras.**

## Snabbåtkomst

Avsnittet Snabbåtkomst finns längst upp på skärmen. Det ger dig snabb åtkomst till dina favorit- och nyligen öppnade filer från anslutna molntjänster. Varje gång du öppnar en fil eller mapp från molnet läggs den till i listan Nyligen öppnade. För att rensa den här listan, öppna Senaste, tryck på knappen **Fler åtgärder** och välj Ta bort lista. Du kan också markera djupt nästlade mappar som Favoriter för att komma åt dem snabbt utan att gräva sig igenom katalogstrukturen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox onlinelänkar och snabbåtkomst" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Andra tjänster

Det här avsnittet visar extra funktioner som förbättrar din upplevelse. För närvarande stöder appen **Last.fm** scrobbling — när den är ansluten skickas din uppspelningsstatistik automatiskt till ditt Last.fm-konto. Du kan sedan besöka din Last.fm-profil för att se lyssningsanalys och få personliga musikrekommendationer. Detaljerade installationsinstruktioner finns [här](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm-anslutning" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
