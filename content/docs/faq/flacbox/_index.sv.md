---
date: '2025-06-12T17:00:00+00:00'
title: 'Flacbox'
description: 'Flacbox FAQ: hi-res musikspelare för iPhone, iPad och Mac med stöd för FLAC, DSD, ALAC, WMA, OGG, OPUS, APE via FFmpeg. Anslut iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, DLNA. Svar om Hi-Res-ljud, samplingsfrekvens, tonhöjdskorrigering, flerkanalsutgång, equalizer, CarPlay, widgets, AirPlay 2, Chromecast, offlineläge, M3U-import/-export, ljudbokmärken, ljudböcker, Wi-Fi Drive, USB DAC, säkerhetskopiering och Premium-planer.'
keywords: [
  "Flacbox FAQ", "Flacbox-app", "hi-res musikspelare", "FLAC-spelare iPhone",
  "DSD-spelare iOS", "ALAC Mac-spelare", "FFmpeg musikspelare iOS", "förlustfri musikspelare",
  "offline musik", "molnmusikströmning", "NAS musikapp", "Synology musikapp",
  "QNAP musikapp", "DLNA musikspelare", "WebDAV musikapp", "SMB musikströmning",
  "Flacbox CarPlay", "Flacbox widgets", "AirPlay 2 musikapp", "Google Chromecast musik",
  "extern USB DAC iPhone", "Hi-Res ljud iPhone", "24-bit 96 kHz iOS", "ljudboksspelare iPhone",
  "ljudbokmärken iOS", "M3U-import iPhone", "M3U-export", "audiotaggeditor",
  "Last.fm-scrobbling", "Flacbox Premium", "Family Sharing musikapp",
  "tonhöjdskorrigering musikapp", "uppspelningshastighet", "audioequalizer",
  "Apple Music-alternativ", "iTunes fildelning"
]
tags: ["faq", "flacbox", "support", "FLAC", "DSD", "hi-res", "FFmpeg", "CarPlay"]
---


<div class="hx:mt-6"></div>

Flacbox är en **hi-res musikspelare** för **iPhone, iPad och Mac** som strömmar och laddar ner spår från iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology, QNAP, WD My Cloud Home och alla andra WebDAV-, SMB- eller DLNA-servrar. Byggd på systemkodekarna plus det medföljande **FFmpeg**-biblioteket lägger den till stöd för format som Apples standardspelare inte kan hantera — WMA, OGG, OPUS, APE, DSD — och ger audiofiler kontroll över utsamplingsfrekvens, flerkanalsrouting, tonhöjdskorrigering och IO-buffertduration. Dessa FAQ besvarar de frågor som användare skickar mest. För djupare genomgångar, se [Flacbox användarguide](/docs/guide/flacbox/) eller bläddra bland våra [Hur man-artiklar](/docs/howto/).

<div class="hx:w-full">

{{% details title="Hur fungerar Flacbox?" closed="true" %}}
**Flacbox är en hi-res musikspelare som låter dig hantera ljudspår som vanliga filer** och strömma dem från valfri molntjänst eller NAS — ingen iTunes-synkronisering behövs.<br><br>

Du kan ladda upp hela din musiksamling till molntjänster som **Dropbox, Google Drive, OneDrive, iCloud Drive, MEGA, Box, pCloud** eller ett personligt NAS och spela musik direkt från molnet med full kontroll. För att lyssna offline, använd den inbyggda nedladdningshanteraren för att spara musik på din enhet. Filer lagras på ditt lagringsutrymme precis som du lade dem där — Flacbox spelar dem helt enkelt.<br><br>

Utforska våra guider för mer information:<br>
- [Flacbox-guide](/docs/guide/flacbox/flacbox-guide)<br>
- [Hur man spelar musik från iCloud Drive på iPhone eller Mac](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac)<br>
- [Hur man aktiverar DLNA-mediaserver på Windows 10 och spelar musik på iPhone](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)<br>
- [Hur man laddar upp filer till molnlagring och ansluter dem till Evermusic, Flacbox, Evertag](/docs/howto/how-to-upload-my-files-to-the-cloud-storage-and-connect-them-to-evermusic-flacbox-evertag)<br>
- [Hur man trådlöst överför filer från en dator till iPhone med WiFi-Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)<br>
- [Hur man ansluter ett USB-flashminne till iPhone och lyssnar på musik](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it)<br>
- [Hur man spelar musik på iPhone från WD My Cloud Home](/docs/howto/how-to-play-music-on-iphone-from-wd-my-cloud-home)
{{% /details %}}

{{% details title="Är Flacbox gratis?" closed="true" %}}
**Ja — Flacbox är gratis att använda med vissa begränsningar**, som kan tas bort genom att uppgradera till Premium-versionen.<br><br>

Du kan välja mellan ett **engångspris för livstid** eller **två prenumerationsalternativ (månadsvis eller årsvis)**. Priserna kan variera beroende på din region. **Family Sharing** är aktiverat för alla planer, så du kan dela Premium med upp till fem familjemedlemmar. Premium-köp och prenumerationer delas mellan iOS och Mac via iCloud — för att synkronisera ditt köp, se till att iCloud är aktiverat på båda enheterna, öppna appen på iOS och vänta en minut för att synkroniseringen ska slutföras.<br><br>

[Läs mer om skillnaderna mellan Flacbox och Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/)
{{% /details %}}

{{% details title="Vad är skillnaden mellan Flacbox och Evermusic?" closed="true" %}}
**Flacbox är den audiofil-fokuserade spelaren med FFmpeg-drivet formatstöd, konfigurerbar samplingsfrekvens, flerkanalsutgång och tonhöjdskorrigering; Evermusic är mainstreamspelaren med crossfade, gapless, rumsljud och en bredare molnfunktionsuppsättning.**<br><br>

**Flacbox** är byggt för att stödja alla standard iOS-ljudformat tillsammans med många ytterligare format som inte stöds inbyggt på iPhone, såsom **WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV** och mer. Det använder en anpassad ljudmotor (systemkodekar + FFmpeg) för att hantera nästan varje format och erbjuder audiofil-grads funktioner som **justerbar ljudutgångssamplingsfrekvens (44,1 – 96 kHz), flerkanalsutgång (Mono → 5.1 → SDDS), IO-bufferttrimning och tonhöjdskorrigering (-1000 till +1000)**.<br><br>

**Evermusic** stödjer standard Apple-ljudformat och inkluderar konsumentvänliga funktioner som **crossfade-uppspelning, gapless-uppspelning, rumsljud, audioequalizer, uppspelningshastighetskontroll** och bredare verktyg för molnströmning. Om du huvudsakligen använder MP3, AAC, ALAC eller FLAC och vill ha crossfade, gapless eller rumsljud kan **Evermusic** vara det bättre alternativet. Om du behöver bred kompatibilitet med ett större utbud av ljudformat — särskilt DSD eller WMA — och vill ha fin kontroll över ljudutgångskedjan är **Flacbox** rätt val.<br><br>

[Läs mer om skillnaderna](/docs/faq/evermusic/what-is-the-difference-between-evermusic-and-flacbox/)
{{% /details %}}

{{% details title="Är Flacbox säkert?" closed="true" %}}
**Ja — Flacbox använder bara officiella SDK:er och säkra OAuth-anslutningar för att interagera med anslutna molntjänster, ser aldrig ditt lösenord och lagrar bara krypterade åtkomsttokens i iOS Keychain.**<br><br>

När du anger ditt inloggningsnamn och lösenord visar appen dig den officiella auktoriseringssidan som tillhandahålls av molntjänstleverantören, och hela auktoriseringsprocessen sker utanför Flacbox. Molnleverantören skickar sedan en **auth-token** till appen efter lyckad auktorisering, och den token används för API-anrop.<br><br>

En auth-token är en digital nyckel som låter tredjepartsappar interagera med molnlagring. Token lagras på din enhet i **Apples säkra systemlagring (Keychain)**, som är krypterad i vila och skyddad av din enhets lösenord eller biometriskt lås. Nedladdade filer lagras i appens **Documents**-katalog; du kan ta bort dem när som helst med den inbyggda filhanteraren.<br><br>

Appen **delar inte någon information** från anslutna molnkonton med Everappz, annonsörer eller någon tredje part. Du kan återkalla åtkomst till ditt molnkonto när som helst genom att öppna kontoinställningssidan i din webbläsare. För att återkalla en auth-token, logga in på ditt molnkonto på webben, navigera till säkerhets- eller anslutna appar-sidan och ta bort posten för Flacbox.<br><br>

Du kan också koppla bort molnkontot i själva appen — när du gör det raderas auth-token omedelbart från din enhet. Avinstallation av appen raderar alla nedladdade data och tokens automatiskt.<br><br>

[Läs mer](/docs/guide/flacbox/flacbox-guide-connections)
{{% /details %}}

{{% details title="Hur skapar jag en spellista i Flacbox?" closed="true" %}}
**För att skapa en spellista, öppna fliken Spellistor, tryck på "+" eller "..."-menyn, välj "Ny spellista", namnge den och välj sedan spår att lägga till från Bibliotek, Filer i denna app, Filer på denna enhet eller Anslutningar.**<br><br>

- Öppna avsnittet **Spellistor**.<br>
- Tryck på **+**-knappen eller **"..."**-knappen i det övre högra hörnet och välj **Ny spellista**.<br>
- Ange ett namn för spellistan och tryck på **Spara**. Dialogen **Lägg till låtar** visas.<br>
- Välj de spår du vill lägga till i spellistan och tryck sedan på **Färdig**.<br><br>

Som standard kan varje låt läggas till i en spellista bara en gång. För att tillåta duplicerade låtar, aktivera **Inställningar → Musikbibliotek → Spellistor → Dubbletter i en spellista → Aktivera**. Du kan senare ändra låtordning, byta namn på spellistan, redigera dess omslagsbild, arkivera den som ZIP och exportera den till M3U, CSV eller TXT.<br><br>

[Läs mer](/docs/guide/flacbox/flacbox-guide-playlists)
{{% /details %}}

{{% details title="Vilka molntjänster, mediaservrar och protokoll stöder Flacbox?" closed="true" %}}
**Flacbox stöder praktiskt taget alla populära molnlagringstjänster, självhostade mediaservrar, fildelningsprotokoll och S3-kompatibla objektlager — allt från en skärm för Anslut till molnlagring.**<br><br>

**Personlig molnlagring:** iCloud Drive · Google Drive · Dropbox · OneDrive (personlig och företag) · Box · MEGA · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).<br><br>

**Självhostade mediaservrar och musikserver-API:er:** **Plex** · **Jellyfin** · **Emby** · **Subsonic** (och varje Subsonic-kompatibel server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · **Navidrome** · Nextcloud (och ownCloud via det delade API:et) · **Synology Drive** · **QNAP**.<br><br>

**NAS och fildelningsprotokoll:** **SMB** (SMB1, SMB2, Auto) · **WebDAV** (HTTP / HTTPS) · **FTP / FTPS** · **SFTP** (lösenord eller autentisering med offentlig nyckel) · **NFS** · **DLNA / UPnP** (uppspelning och nedladdning). Fungerar med Apple Time Capsule, Synology, QNAP, WD My Cloud Home, Buffalo, vilken Linux Samba / NFS / SSH-värd som helst, eller en delad mapp på din Mac eller Windows-dator.<br><br>

**S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces och alla andra S3-API-slutpunkter.<br><br>

**Lokalnätverksupptäckt:** avsnittet **Tillgängliga enheter** listar automatiskt varje Bonjour / mDNS-tjänst på ditt Wi-Fi-nätverk — Plex, Jellyfin, Emby-servrar, Synology, QNAP, AirPort-routrar med anslutna enheter, Time Capsule — så att du kan trycka för att ansluta utan att skriva en IP-adress.<br><br>

Varje anslutning använder **officiellt SDK eller öppet protokoll** för tjänsten, med OAuth-baserad auktorisering där det stöds. Du kan ansluta flera konton för samma tjänst (till exempel två Google Drive-konton, ett personligt Dropbox vid sidan av ett arbets-Dropbox, eller både en Plex- och en Jellyfin-server). Premium-användare kan lägga till ett obegränsat antal tjänster; gratisversionen är begränsad till tre.<br><br>

[Läs mer](/docs/guide/flacbox/flacbox-guide-connections)
{{% /details %}}

{{% details title="Hur använder jag audioequalizer i Flacbox?" closed="true" %}}
**Öppna ljudspelarskärmen, tryck på Equalizer-ikonen, slå på equalizern och välj antingen en förinställning eller flytta skjutreglagen för att bygga din egen.**<br><br>

- Öppna skärmen **Ljudspelaren**.<br>
- Tryck på **Equalizer**-ikonen längst ner på skärmen.<br>
- Växla reglaget i det övre högra hörnet på equalizer-skärmen för att aktivera den.<br>
- Välj en av de tillgängliga förinställningarna (Rock, Pop, Dance, Disco, Classical, Jazz, Acoustic, Bass Booster med mera) eller dra bandskjutreglagen för att bygga din egen förinställning.<br>
- Använd **förförstärkaren** för att lägga till total förstärkning eller trimma tillbaka den. Tryck på **Spara** för att hålla din anpassade förinställning under valfritt namn.<br><br>

Flacbox använder en **10-bands equalizer** och EQ är även tillgänglig under AirPlay-, Chromecast- och CarPlay-uppspelning. Vi har en fullständig handledning här:<br>
[Hur man använder audioequalizer på din iPhone, iPad, Mac med Evermusic och Flacbox](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox)
{{% /details %}}

{{% details title="Hur aktiverar jag offlineläge i Flacbox?" closed="true" %}}
**Anslut en molntjänst, hitta en musikmapp, tryck på "Fler åtgärder → Aktivera offline-läge" — mappen och alla nya filer som läggs till i den laddas ned automatiskt till Lokala filer → Offline mappar.**<br><br>

- **Anslut en molntjänst:** öppna fliken **Anslutningar**. Välj **Anslut en molntjänst** och följ anvisningarna.<br>
- **Navigera till musikmapp:** öppna den anslutna molntjänsten och hitta din musikmapp.<br>
- **Aktivera offline-läge:** tryck på **"..."**-knappen bredvid mappnamnet och välj **Aktivera offline-läge**.<br>
- **Ladda ned innehåll:** den valda mappen och allt dess innehåll laddas ned till **Lokala filer → Offline mappar**.<br>
- **Automatiska uppdateringar:** appen söker kontinuerligt efter ändringar. Nya filer som läggs till i online-mappen laddas ned automatiskt.<br>
- **Konfigurera skanningtidsgräns:** gå till **Inställningar → Filhanteraren → Offline mappar → Tidsintervall** för att ange skanningsfrekvensen.<br>
- **Manuell synkronisering:** för att synka manuellt, gå till **Inställningar → Filhanteraren → Offline mappar → Synkroniserade offline-mappar**. Tryck på **"..."** och välj **Starta synkronisering**.<br><br>

[Läs mer](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/)
{{% /details %}}

{{% details title="Hur spelar jag lokalt nedladdad musik på iPhone?" closed="true" %}}
**Öppna Lokala filer, scrolla till "Filer på denna iPhone", tryck på "Öppna filer..." eller "Öppna mapp..." och välj de ljudfiler eller mapp du vill spela.**<br><br>

Appen skannar mappens innehåll, lägger till hittade ljudfiler i spelarens kö och spelar dem direkt från deras ursprungliga plats utan att kopiera något till appbunten.<br><br>

**Lägga till en mapp i Favoriter för snabb åtkomst**<br>
Öppna skärmen **Lokala filer**, scrolla till **Snabbåtkomst** och tryck på **Favoriter** för att komma åt skärmen **Favoritfiler**. Tryck på knappen för fler åtgärder **"..."** i det övre högra hörnet och välj **Lägg till mapp**. Navigera till önskad mapp och tryck på **Öppna** för att bekräfta. Din mapp läggs till i **Favoritfiler**, vilket ger dig snabb åtkomst till din musik utan att upprepa stegen.<br><br>

**Importera lokala filer till musikbiblioteket**<br>
Om du föredrar att organisera dina lokala filer i ditt musikbibliotek, öppna skärmen **Musikbibliotek**, tryck på trepunktsknappen i det övre högra hörnet och välj **+ Lägg till musik**. Välj menyalternativet **Lokala filer**, scrolla ned till avsnittet **Filer på denna iPhone** och tryck på **Öppna filer...**. Välj filerna du vill lägga till och tryck på **Öppna** för att bekräfta. Appen skannar de valda filerna och lägger till dem i ditt musikbibliotek, sorterat efter metadata som artist, album och genre.<br><br>

**Lägga till lokala filer i en spellista**<br>
För att lägga till lokala filer i en spellista, öppna skärmen **Spellistor** och tryck på mer-knappen i det övre högra hörnet. Välj **+ Ny spellista**, ange ett namn för din nya spellista och på nästa skärm väljer du alternativet **Lokala filer**. Scrolla ned till avsnittet **Filer på denna iPhone** och tryck på **Öppna filer...**. Välj ljudfilerna du vill lägga till och tryck på **Öppna** för att bekräfta. Filerna läggs till i din spellista, där du kan ändra låtordning och utföra andra åtgärder med mer-knappen.<br><br>

[Läs mer](/docs/howto/how-to-play-local-music-stored-on-your-iphone-or-mac)
{{% /details %}}

{{% details title="Hur kan jag återuppta en spellista från där jag slutade?" closed="true" %}}
**Aktivera Spara ljudspelartillstånd i Inställningar → Ljudspelaren → Allmänt, tryck sedan på Fortsätt uppspelning längst upp i valfri spellista, album, artist eller mapp för att återuppta från den exakta sista positionen.**<br><br>

När du byter till en annan spellista och kommer tillbaka ser du fyra åtgärder i det övre verktygsfältet under albumomslaget: **Sök, Fortsätt uppspelning, Spela alla** och **Blanda alla**. Tryck på **Fortsätt uppspelning** för att återuppta spellistan från det senast sparade tillståndet och mediapositionen. Du kan också aktivera **Spara uppspelningsposition** för att komma ihåg positionen i varje enskilt spår — praktiskt för ljudböcker och långa mixar.
{{% /details %}}

{{% details title="Hur ser jag låttexter i Flacbox?" closed="true" %}}
**Öppna helskärmsljudspelaren, tryck på "..." → Visa kommentarer och svep sedan för att växla mellan lägena Kommentarer, Inbäddade texter och LRC-fil.**<br><br>

1. Börja spela ett spår.<br>
2. Öppna helskärmsljudspelaren.<br>
3. Tryck på knappen **Fler åtgärder** i det övre högra hörnet.<br>
4. Välj **Visa kommentarer**.<br>
5. Svep åt höger för att växla mellan lägena **Kommentarer**, **Inbäddade texter** och **LRC-fil**.<br><br>

**Lägen:**<br>
- **Kommentarer** — innehåll från COMMENT-taggen.<br>
- **Inbäddade texter** — texter från LYRICS-taggen; stödjer tidsstyrd text i LRC-format. Redigera texter med en extern taggeditor som Evertag eller ladda ned LRC-filer från webbplatser som Lyricsify och klistra in dem i taggen.<br>
- **LRC-fil** — placera en `.lrc`-fil med samma basnamn i samma mapp som ljudfilen; appen plockar upp den automatiskt.<br><br>

[Läs mer](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox)
{{% /details %}}

{{% details title="Hur överför jag musik till Flacbox från min dator?" closed="true" %}}
**Du kan överföra musik till Flacbox via SMB, WebDAV, FTP / SFTP, DLNA, Wi-Fi Drive eller via iTunes / Finder Fildelning — alla metoder som exponerar filerna för din enhet fungerar.**<br><br>

För att ansluta en dator med **SMB**-protokollet, tryck på **Anslut en molntjänst → SMB**. Ange datorns IP-adress och delad mappnamn i URL-fältet med formatet `smb://dator-ip-adress/delad-mappnamn`, ange ditt inloggningsnamn och lösenord och tryck sedan på **Färdig**. Om anslutningen lyckas visas resursen i avsnittet **Molntjänster** på anslutningsskärmen.<br><br>

[Fullständig handledning: överför dina filer från datorn till iPhone med SMB-protokollet](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/)<br><br>

För **WebDAV** är alla steg desamma förutom URL-fältet — använd `http://servernamn` eller `https://servernamn` om servern stöder SSL. WebDAV fungerar utmärkt med Synology, QNAP, Nextcloud, ownCloud och alla andra servrar som exponerar en WebDAV-slutpunkt.<br><br>

[Fullständig handledning: hur man ansluter NAS-lagring med WebDAV och lyssnar på musik på iPhone eller Mac](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)<br><br>

**Wi-Fi Drive** är en populär teknik som låter dig överföra filer från din dator till en iOS-enhet trådlöst med valfri stationär webbläsare. För att använda den här funktionen bör din enhet och dator vara på samma Wi-Fi-nätverk. Öppna **Anslutningar → Dator → Ansluta med Wi-Fi** och aktivera servern. Öppna sedan en webbläsare på datorn och ange URL:en som appen visar. Du kan dra och släppa filer från din dator till den öppna webbsidan och de visas på din enhet nästan omedelbart.<br><br>

[Mer detaljerad handledning: hur man trådlöst överför filer från en dator till iPhone med WiFi-Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)<br><br>

**iTunes / Finder Fildelning** är ett annat alternativ, som överför filer från en dator till en enhet via en Lightning- eller USB-C-kabel. Anslut enheten till datorn, öppna iTunes (eller Finder på macOS Catalina och senare), välj enheten, hitta **Flacbox** i applistan och kopiera filer till dess delade mapp.<br><br>

[Detaljerade instruktioner: hur man spelar lokala filer på iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone)<br><br>

Med **DLNA** kan du också ställa in en DLNA-mediaserver och strömma din musik från en Windows-PC, NAS eller annan UPnP-enhet:<br>
[Hur man aktiverar DLNA-mediaserver på Windows 10 och spelar musik på iPhone](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)
{{% /details %}}

{{% details title="Hur laddar jag ned musik från molnlagring i Flacbox?" closed="true" %}}
**Öppna den anslutna molntjänsten, bläddra till en mapp, tryck på "..." → Välja, välj filerna och tryck sedan på Ladda ner — de sparas till Lokala filer för offlineuppspelning.**<br><br>

Innan du kan ladda ned musik och lyssna offline måste du ansluta minst ett molnkonto. Öppna skärmen **Anslutningar** och lägg till ditt konto.<br><br>

**Så här laddar du ned musik från molnet:**<br>
- Öppna den anslutna molntjänsten.<br>
- Navigera inuti mappen som innehåller musiken du vill ladda ned.<br>
- Tryck på **"..."**-knappen i det övre högra hörnet och välj **Välja**.<br>
- Välj filerna du vill ladda ned och tryck på knappen **Ladda ner** längst ned på skärmen.<br>
- Spåra förloppet i **Lokala filer → Överföringskö**.<br><br>

**Så här aktiverar du offlineläge för en artist, ett album, en spellista eller genre:**<br>
- Öppna skärmen **Artist / Album / Spellista / Genre**.<br>
- Tryck på kryssrutan **Offline-läge** under omslaget.<br>
- Den nedladdade samlingen visas i avsnittet **Offlinemusik** i ditt musikbibliotek.<br><br>

[Läs guiden för offlineläge](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/)
{{% /details %}}

{{% details title="Vilka ljudformat stöder Flacbox?" closed="true" %}}
**Flacbox spelar systemljudformat plus dussintals extra format via den medföljande FFmpeg-motorn — inklusive FLAC, ALAC, MP3, AAC, WAV, AIFF, M4A, OGG, OPUS, WMA, APE, DSD, DSF, DFF, TTA, MPC, WV och många fler.**<br><br>

Här är den fullständiga listan över filnamnstillägg som stöds:<br><br>

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, "dvr-ms", ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.
{{% /details %}}

{{% details title="Kan jag använda Flacbox för att spela ljudböcker?" closed="true" %}}
**Ja — Flacbox är en kraftfull ljudboksspelare med bokmärken per spår, variabel uppspelningshastighet (0,02× till 3,00×), fortsätt uppspelning, en sömntimeroch anpassningsbara hoppa-tid-knappar.**<br><br>

**Hur man lägger till ljudböcker**<br>
- För **lokala filer**, anslut din iPhone eller iPad till din dator, öppna iTunes (eller Finder på macOS Catalina eller senare) och dra dina ljudboksfiler till avsnittet **Flacbox**.<br>
- För **molnfiler**, anslut tjänster som iCloud Drive, Google Drive, Dropbox och andra inuti Flacbox-appen för att komma åt dina ljudböcker på distans.<br><br>

**Uppspelningsfunktioner**<br>
- Navigera till dina ljudböcker via **Musikbibliotek** eller **Lokala filer**.<br>
- Flacbox stöder **spela, pausa, hoppa** och **justerbar uppspelningshastighet**.<br>
- Aktivera **Hoppa tid**-knappar i inställningar för snabb navigering med 15, 30, 60 eller vilket annat intervall som helst.<br>
- Skapa **Ljudbokmärken** för att spara din plats — perfekt för kapitel eller favoritpassager.<br>
- Använd **Fortsätt uppspelning** för att återuppta där du slutade, även efter att du stängt appen.<br><br>

**Organisation och offlineåtkomst**<br>
- Organisera ljudböcker i spellistor efter genre, författare eller serie.<br>
- Ladda ned ljudböcker för offlinelyssning, perfekt för resor eller begränsad anslutning.<br><br>

Flacbox erbjuder en komplett lösning för ljudboksälskare på iPhone, iPad och Mac. **M4B-kapitelmarkörer** och långa filer stöds fullt ut.<br><br>

[Läs mer](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic)
{{% /details %}}

{{% details title="Fungerar Flacbox med NAS-enheter?" closed="true" %}}
**Ja — Flacbox stöder NAS-anslutningar med SMB, WebDAV, FTP / FTPS, SFTP, NFS och DLNA / UPnP-protokoll, vilket innebär att det fungerar med Synology, QNAP, WD My Cloud Home, Buffalo, Apple Time Capsule** och alla andra NAS som exponerar ett av dessa standardprotokoll.<br><br>

**För att ansluta ett NAS med SMB-protokollet:**<br>
- Tryck på **Anslut en molntjänst → SMB**.<br>
- Ange NAS-serverns IP-adress och delad mappnamn i formatet `smb://din-ip/delad-mapp`.<br>
- Välj protokollversion: **Auto**, **SMB1** eller **SMB2**.<br>
- Ange ditt inloggningsnamn och lösenord (om det behövs).<br>
- Tryck på **Färdig**.<br><br>

Om anslutningen lyckas ser du ditt NAS i avsnittet **Molntjänster**.<br>
[Läs fullständig handledning](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)<br><br>

**För att ansluta via WebDAV-protokollet:**<br>
- Stegen är desamma som SMB, men använd en WebDAV-URL som `http://ditt-servernamn` eller `https://ditt-servernamn` om SSL används.<br><br>

**För att strömma via DLNA:**<br>
- Du kan strömma från en Windows-PC genom att aktivera dess DLNA-mediaserver.<br>
[Läs DLNA-inställningsguiden](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)<br><br>

**Avsnittet Tillgängliga enheter:**<br>
- Visar alla upptäckbara NAS-enheter på ditt lokala nätverk.<br>
- Tryck på ett enhetsnamn för att ansluta och ange inloggningsuppgifter om det behövs.<br><br>

**Användbara länkar:**<br>
- [Hur man spelar musik på iPhone från WD My Cloud Home](/docs/howto/how-to-play-music-on-iphone-from-wd-my-cloud-home)<br>
- [Strömma musik från Mac eller PC till iPhone med SMB](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)<br>
- [Anslut Bluesound Vault-lagring](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag)<br>
- [Anslut NAS-lagring med WebDAV](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)
{{% /details %}}

{{% details title="Stöder Flacbox Plex, Jellyfin, Emby, Subsonic och Navidrome?" closed="true" %}}
**Ja — Flacbox ansluter inbyggt till Plex Media Server, Jellyfin, Emby, Subsonic och Navidrome**, så att du kan strömma ditt självhostade musikbibliotek utan att någonsin exponera den underliggande filresursen.<br><br>

- **Plex Media Server** — tryck på **Anslut till molnlagring → Plex**, logga in med ditt Plex-konto och välj en server. Plex-servrar på samma lokala nätverk upptäcks också automatiskt i **Tillgängliga enheter**.<br>
- **Jellyfin** (öppen källkod) — tryck på **Anslut till molnlagring → Jellyfin**, ange din server-URL (något som `http://server-ip:8096`) och inloggningsuppgifter.<br>
- **Emby** — tryck på **Anslut till molnlagring → Emby**, ange sedan serverns URL och inloggning.<br>
- **Subsonic och Subsonic-kompatibla servrar** — tryck på **Anslut till molnlagring → Subsonic**, ange server-URL och inloggningsuppgifter. Detta fungerar med den ursprungliga **Subsonic**-servern samt **Navidrome**, **Airsonic**, **Funkwhale**, **Gonic**, **Logitech Media Server (LMS)** och **Ampache** — allt som talar Subsonic API.<br><br>

När du väl är ansluten visas servern vid sidan av dina molnkonton på anslutningsskärmen. Du kan bläddra efter Artister, Album, Genrer, Spellistor och serverns egna mappstruktur, ladda ned spår för offlineuppspelning, köa dem i ljudspelaren och till och med hämta dem till Flacbox musikbibliotek så att de visas i dina globala vyer för Artister / Album / Genrer / Kompositörer.
{{% /details %}}

{{% details title="Stöder Flacbox FTP, FTPS, SFTP och NFS?" closed="true" %}}
**Ja — Flacbox stöder de klassiska Unix-filöverföringsprotokollen: FTP, FTPS, SFTP (SSH File Transfer Protocol) och NFS.**<br><br>

- **FTP / FTPS** — tryck på **Anslut till molnlagring → FTP**, ange värd-URL:en i formen `ftp://servernamn` (eller `ftps://servernamn` för en krypterad anslutning), ange ditt inloggningsnamn och lösenord och tryck sedan på **Färdig**.<br>
- **SFTP** — tryck på **Anslut till molnlagring → SFTP**, ange serveradressen och autentisera med antingen ett lösenord eller ett SSH-nyckelpar. SFTP fungerar med NAS-enheter, Linux-värdar och alla servrar som kör `sshd`.<br>
- **NFS (Network File System)** — tryck på **Anslut till molnlagring → NFS** och ange serveradressen och exporterad sökväg. Praktiskt för Linux-värdar, BSD-servrar och NAS-enheter som föredrar NFS framför SMB.<br><br>

Detta är utöver **SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS)** och **DLNA / UPnP** som Flacbox också stöder inbyggt.
{{% /details %}}

{{% details title="Stöder Flacbox S3-kompatibel objektlagring (AWS S3, Backblaze B2, Wasabi, MinIO, Cloudflare R2)?" closed="true" %}}
**Ja — Flacbox inkluderar en S3-kompatibel anslutning som fungerar med AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces och alla andra tjänster som exponerar en S3-API-slutpunkt.**<br><br>

Tryck på **Anslut till molnlagring → S3-lagring**, ange sedan slutpunktens URL, region, åtkomstnyckel, hemlig nyckel och bucketnamn. När du väl är ansluten visas bucketen vid sidan av dina andra molntjänster — du kan bläddra, strömma, ladda ned, synkronisera och lägga till spår i ditt musikbibliotek på exakt samma sätt.
{{% /details %}}

{{% details title="Stöder Flacbox Apple CarPlay?" closed="true" %}}
**Ja — Flacbox stöder fullt Apple CarPlay** med dedikerade flikar för **Bibliotek**, **Anslutningar**, **Lokala filer** och **Inställningar**, så att du kan bläddra och kontrollera uppspelning direkt från bilens infotainmentskärm.<br><br>

Du kan strömma från molnlagring, spela offlinespår, kontrollera blandning, upprepning, köhantering och till och med **audioequalizern** utan att plocka upp din telefon. För att använda CarPlay, se till att Siri är aktiverat på din iPhone och anslut den sedan till ditt fordon via **USB eller trådlöst CarPlay**.<br><br>

Finjustera CarPlay-upplevelsen i **Inställningar → CarPlay** — sorteringsalternativ, gräns för innehållsladdning (sidnumrering), menysikoners gradientfärg, om bilder visas för snabbare laddning på stora bibliotek och **Pausa uppspelning vid anslutning** för att undvika plötsligt högt ljud.<br><br>

[Läs den fullständiga guiden](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/)
{{% /details %}}

{{% details title="Hur använder jag Wi-Fi Drive-funktionen i Flacbox?" closed="true" %}}
**Wi-Fi Drive låter dig trådlöst överföra filer från valfri dator till din iOS-enhet via en webbläsare på skrivbordet, Finder eller File Explorer — båda enheterna behöver bara vara på samma Wi-Fi-nätverk.**<br><br>

**Trådlös överföring med en webbläsare på skrivbordet**<br>
1. Starta appen: öppna Flacbox.<br>
2. Anslut via Wi-Fi: gå till **Anslutningar → Dator → Ansluta med Wi-Fi**.<br>
3. (Valfritt) Lägg till säkerhet: ange ett användarnamn och lösenord om det behövs.<br>
4. Starta Wi-Fi Drive: tryck på **Starta Wi-Fi Drive** och kopiera den angivna URL:en.<br>
5. Öppna en webbläsare (Safari, Chrome, Opera, Firefox osv.) och ange URL:en.<br>
6. Använd den inbyggda filhanteraren för att ladda upp, ladda ned, byta namn på eller ta bort filer. Du kan dra och släppa filer direkt till din iPhone.<br>
7. När du är klar trycker du på **Stoppa Wi-Fi Drive** på din iPhone.<br><br>

Obs: Se till att JavaScript är aktiverat och att du använder den senaste webbläsarversionen för bästa prestanda.<br><br>

**Överföra filer med Mac Finder**<br>
1. I Finder klickar du på **Gå → Anslut till server...**.<br>
2. Ange server-URL:en som visas i Flacbox-appen.<br>
3. Klicka på **Ansluta** och hantera filer på din iPhone som vilken nätverksenhet som helst.<br><br>

**Överföra filer med Windows File Explorer**<br>
1. Högerklicka på **Den här datorn → Koppla nätverksenhet...**.<br>
2. Ange server-URL:en från Flacbox-appen i fältet **Mapp**.<br>
3. Välj en enhetsbeteckning, klicka på **Slutför** och bläddra i din iPhones filer direkt.<br><br>

[Läs mer](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)
{{% /details %}}

{{% details title="Spelar Flacbox FLAC på iPhone?" closed="true" %}}
**Ja — Flacbox spelar FLAC förlustfritt ljud inbyggt på iPhone, iPad och Mac**, inklusive mycket högupplösta filer, med fullt stöd för inbäddat albumomslag, texter och metadata.<br><br>

FLAC-filer strömmar direkt från ansluten molnlagring eller spelas lokalt utan konvertering eller transkodning. För bästa resultat med mycket högupplösta filer, lämna **Ljudkodek** inställd på **Systemkodek + FFmpeg** eller välj **FFmpeg** i **Inställningar → Ljudspelaren → Allmänt** så att du också kan justera samplingsfrekvens och tonhöjdskorrigering.
{{% /details %}}

{{% details title="Spelar Flacbox DSD-, DSF- och DFF-filer?" closed="true" %}}
**Ja — Flacbox spelar DSD-familjeformat (DSF, DFF) via sin medföljande FFmpeg-motor.** De flesta konsument-DAC:er accepterar inte inbyggt DSD via Lightning / USB-C, så DSD avkodas till PCM i realtid innan utmatning.<br><br>

För bästa resultat med DSD, byt **Ljudkodek** till **FFmpeg** i **Inställningar → Ljudspelaren → Allmänt** och välj en **Ljudutgångssamplingsfrekvens** på **88,2 kHz** eller **96 kHz** som matchar din DAC. Para Flacbox med en USB- eller Lightning-DAC för fullständigt transparent avkodning.
{{% /details %}}

{{% details title="Stöder Flacbox Hi-Res-ljud (24-bit / 96 kHz)?" closed="true" %}}
**Ja — Flacbox stöder Hi-Res-ljuduppspelning via FFmpeg-motorn med konfigurerbara utsamplingsfrekvenser på 44,1, 48, 64, 88,2 och 96 kHz.**<br><br>

I **Inställningar → Ljudspelaren → Allmänt**, byt **Ljudkodek** till **FFmpeg**, välj sedan din föredragna **Ljudutgångssamplingsfrekvens** och antal kanaler. Para detta med ett kompatibelt **externt DAC eller USB / Lightning-ljudgränssnitt** för bitperfekt utmatning från din iPhone, iPad eller Mac.
{{% /details %}}

{{% details title="Hur använder jag ett externt USB DAC med Flacbox?" closed="true" %}}
**Anslut din USB DAC till iPhone, iPad eller Mac (via Lightning-till-USB, USB-C eller direkt), och sedan i Inställningar → Ljudspelaren → Allmänt byt till FFmpeg-kodeken och välj samplingsfrekvensen och antalet kanaler som din DAC förväntar sig.**<br><br>

Många audiofil-DAC:er föredrar **88,2 kHz** eller **96 kHz** med **stereo**-utmatning. Sänk **Föredragen IO-buffertduration för ljudutgång** till runt **5 ms (0,005 s)** för låg latens och öka den sedan något om du hör störningar. Flacbox fungerar med de flesta class-compliant USB DAC:er och Lightning DAC:er, inklusive produkter från AudioQuest, iFi, Chord, FiiO, Topping med flera.
{{% /details %}}

{{% details title="Spelar Flacbox WMA-, OGG-, OPUS- och APE-filer?" closed="true" %}}
**Ja — Flacbox spelar WMA, OGG, OPUS, APE, TTA, MPC, WV och många andra mindre vanliga format via den medföljande FFmpeg-motorn**, även om iOS inte stöder dem inbyggt.<br><br>

Ingen konvertering krävs: lägg filerna i iCloud Drive, Dropbox, Google Drive eller ditt NAS, anslut den tjänsten i Flacbox och filerna spelas bara. Inbäddade taggar, albumomslag och texter läses där de finns.
{{% /details %}}

{{% details title="Stöder Flacbox flerkanals- eller 5.1-surroundutmatning?" closed="true" %}}
**Ja — Flacbox låter dig välja Mono, Stereo, Center/Vänster/Höger, Center/Vänster/Höger/Surround, ITU BS.775-1, 5.1 Surround och SDDS** i **Inställningar → Ljudspelaren → Allmänt → Antal ljudutgångskanaler** (FFmpeg-kodek krävs).<br><br>

Detta är användbart med externa flerkanalsdakar och AV-receivers. De flesta användare bör hålla sig till **Stereo** såvida de inte har specifik flerkanalshårdvara ansluten, eftersom iPhones inbyggda högtalare och de flesta hörlurar bara är stereo.
{{% /details %}}

{{% details title="Stöder Flacbox tonhöjdskorrigering?" closed="true" %}}
**Ja — Flacbox erbjuder tonhöjdskorrigering i ett brett intervall från -1000 till +1000 cent**, konfigurerbar i **Inställningar → Ljudspelaren → Tonhöjdskorrigering**.<br><br>

Använd **Precist läge** (tryck på konfigurationsikonen i det övre högra hörnet) för finare justeringar. Tonhöjdskorrigering är tillgänglig i **FFmpeg**-kodeksökvägen, så se till att du har valt **FFmpeg** under **Inställningar → Ljudspelaren → Allmänt → Ljudkodek** för att komma åt den.
{{% /details %}}

{{% details title="Hur importerar jag en M3U-, M3U8- eller CUE-spellista till Flacbox?" closed="true" %}}
**Öppna avsnittet Spellistor, tryck på "..."-menyn, välj "Importera spellista" och välj sedan .m3u-, .m3u8- eller .cue-filen från din molnlagring eller enhet.**<br><br>

Appen analyserar spellisfilen, lokaliserar varje refererat spår på ditt lagringsutrymme och skapar en verklig spellista i ditt musikbibliotek. Filnamnstillägg som stöds är **M3U**, **M3U8** och **CUE**. Se till att sökvägarna inne i spellisfilen matchar var ljudfilerna faktiskt finns på lagringsutrymmet.<br><br>

[Läs den fullständiga guiden](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox)
{{% /details %}}

{{% details title="Hur exporterar jag en spellista från Flacbox till M3U, CSV eller TXT?" closed="true" %}}
**Öppna spellistan, tryck på "..."-menyn och välj "Exportera låtlista" — du kan spara resultatet som M3U, M3U8, CSV eller TXT.**<br><br>

Samma åtgärd är också tillgänglig för album, artister, genrer, listan Senaste och listan Favoriter. Använd M3U för återimport till andra spelare, CSV för kalkylblad och TXT för en enkel, mänskligt läsbar kopia.<br><br>

[Läs den fullständiga guiden](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)
{{% /details %}}

{{% details title="Hur kastar jag musik från Flacbox till Google Chromecast eller AirPlay?" closed="true" %}}
**Öppna ljudspelaren, tryck på AirPlay- eller Chromecast-ikonen och välj din högtalare, TV eller AV-receiver från listan.**<br><br>

Både **AirPlay 2** och **Google Chromecast** stöds på iOS — knapparna kan läggas till på huvudspelarskärmen via **Inställningar → Ljudspelaren → Personalisering → Huvudskärmsåtgärder**. Vissa hi-res-format kan behöva transkodas för Chromecast-uppspelning. AirPlay 2 låter dig också spela till flera HomePods eller Apple TVs samtidigt.
{{% /details %}}

{{% details title="Hur aktiverar jag Flacbox-widgets på min iPhones hemskärm eller låsskärm?" closed="true" %}}
**Aktivera widgetuppdateringar i Inställningar → Widgets, tryck sedan länge på din hemskärm eller låsskärm, tryck på "+", sök "Flacbox" och välj en widgetstorlek.**<br><br>

Widgeten visar det aktuella spåret med omslag och grundläggande information. Eftersom widgetuppdateringar använder en liten mängd energi är **Aktivera widgets**-reglaget avstängt som standard — slå på det bara om du aktivt använder widgets. Widgets fungerar på iPhones och iPads hemskärm och låsskärm, och även i macOS Notifikationscenter.
{{% /details %}}

{{% details title="Hur redigerar jag MP3-taggar från Flacbox?" closed="true" %}}
**Tryck på "..." på ett spår och välj Redigera ljudtaggar för att öppna den inbyggda taggeditorn — du kan ändra titel, artist, album, år, genre, texter, albumomslag med mera.**<br><br>

För onlinefiler laddar Flacbox tillfälligt ned spåret, låter dig redigera och laddar sedan upp det igen till molntjänsten. Du kan konfigurera detta beteende i **Inställningar → Audiotaggeditor** — inklusive albumomslagsskalning, om ändringar skrivs tillbaka till molnfiler automatiskt och vilka knappar som visas på editorns huvudskärm. För djupare massredigering av många filer samtidigt, installera vår companion-app **Evertag**. [Läs mer om Evertag](/products/evertag/).
{{% /details %}}

{{% details title="Hur fixar jag saknade albumomslag i Flacbox?" closed="true" %}}
**Öppna Inställningar → Bibliotek → Albumomslag, aktivera "Ladda albumomslag för onlinefiler" och "Sök i mapp", öka sedan Omslagskvalitet om det behövs — appen hämtar inbäddat konstverk från dina molnfiler och använder JPEG / PNG-bilder som lagras bredvid dina ljudfiler när inget inbäddat omslag finns.**<br><br>

Du kan också trycka på **Ta bort alla** för att rensa omslagscachen och tvinga en uppdatering. För att manuellt ersätta ett specifikt omslag, tryck på **"..." → Redigera bild** på albumet, spellistan eller spåret och välj en ny bild från ditt fotobibliotek, Filer-appen eller en av dina anslutna molntjänster. För djupare kontroll över konstverk som lagras inuti själva ljudfilen, använd **Redigera ljudtaggar** eller vår companion-app **Evertag**.
{{% /details %}}

{{% details title="Hur tar jag bort en låt från Flacbox utan att ta bort den från min molnlagring?" closed="true" %}}
**På ett spår, tryck på "..." → Ta bort från musikbiblioteket — detta tar bort låten från din biblioteksdatabas men lämnar filen orörd i molnlagring och Lokala filer.**<br><br>

För att också ta bort filen från molnet eller den lokala enheten, välj istället **Ta bort från molntjänsten** eller **Ta bort från lokala filer**. Dessa destruktiva åtgärder kan inte ångras, så var försiktig när du har flera filer valda.
{{% /details %}}

{{% details title="Hur säkerhetskopierar och återställer jag mitt Flacbox-musikbibliotek?" closed="true" %}}
**Öppna Inställningar → Säkerhetskopiering och återställning, välj vad du vill inkludera (Databas, Albumomslag, Inställningar), tryck på "Säkerhetskopiera appdata" och spara säkerhetskopieringsfilen — öppna den på en annan enhet för att återställa.**<br><br>

Säkerhetskopian innehåller dina musikbiblioteksposter, spellistor, betyg, favoriter, inställningar och albumomslagscache. Den inkluderar inte offlineladdade ljudfiler för att hålla filstorleken hanterbar. Flytta säkerhetskopieringsfilen till den nya enheten via iCloud Drive, AirDrop eller vilken ansluten molntjänst som helst och öppna den sedan i Flacbox för att tillämpa.<br><br>

[Fullständig guide: hur man överför sitt musikbibliotek mellan enheter](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide)
{{% /details %}}

{{% details title="Hur delar jag Flacbox Premium med min familj?" closed="true" %}}
**Alla Flacbox Premium-planer — livstid, månadsvis och årsvis — fungerar med Apple Family Sharing, så vem som helst i din familjegrupp kan installera Flacbox och använda Premium utan extra kostnad.**<br><br>

Konfigurera Family Sharing i iOS / macOS **Inställningar → Familj** och låt sedan varje familjemedlem installera Flacbox från App Store och köra det en gång när de är inloggade på sitt eget Apple ID. Premium känns igen automatiskt inom en minut. Samma plan delas mellan iPhone, iPad och Mac för varje familjemedlem.
{{% /details %}}

{{% details title="Hur avbryter jag min Flacbox Premium-prenumeration?" closed="true" %}}
**Öppna iOS eller macOS Inställningar → [ditt namn] → Prenumerationer, hitta Flacbox och tryck på Avbryt prenumeration — dina Premium-funktioner förblir aktiva tills slutet av den aktuella faktureringsperioden.**<br><br>

Livstids köp i appen är inte prenumerationer och behöver inte avbrytas. För återbetalningar, använd Apples **Rapportera ett problem**-sida (`reportaproblem.apple.com`) — återbetalningar utfärdas av Apple, inte av Everappz.
{{% /details %}}

{{% details title="Hur skyddar jag Flacbox med ett lösenord?" closed="true" %}}
**Öppna Inställningar → Lösenord, tryck på Aktivera och välj en 4-siffrig kod — du uppmanas att ange den varje gång appen startar.**<br><br>

Flacbox använder ett fast 4-siffrigt numeriskt lösenord. Lösenordet förhindrar någon med tillgång till din enhet från att öppna Flacbox och bläddra bland dina anslutna molnkonton, nedladdade filer och bibliotek. Kombinera det med iOS Face ID / Touch ID på enheten för extra skydd.
{{% /details %}}

{{% details title="Hur aktiverar jag mörkt läge i Flacbox?" closed="true" %}}
**Öppna Inställningar → Personalisering → Färgschema och välj sedan Mörkt, Ljust eller Standard (som följer ditt systems utseende).**<br><br>

Du kan också välja alternativa appikoner i **Inställningar → Personalisering → Appikon** (Premium) och välja ett suddigt albumomslag som appbakgrund under **Bakgrundsstil**.
{{% /details %}}

{{% details title="Hur ändrar jag uppspelningshastigheten i Flacbox?" closed="true" %}}
**Öppna ljudspelaren, tryck på hastighetskontrollen och dra reglaget — hastigheten är justerbar från 0,02× till 3,00×.**<br><br>

Du kan också ändra standardhastigheten i **Inställningar → Ljudspelaren → Uppspelningshastighet**. Tryck på konfigurationsikonen i det övre högra hörnet för att byta till **precist läge** för mycket fina justeringar — praktiskt för ljudböcker, föreläsningar och språkinlärningsinnehåll.
{{% /details %}}

{{% details title="Hur ställer jag in en sömntimerare i Flacbox?" closed="true" %}}
**Öppna Inställningar → Ljudspelaren → Sömntimerare, slå på den och välj hur länge du vill att musik ska spela innan den stannar.**<br><br>

Du kan också aktivera knappen **Sömntimerare** direkt på ljudspelarskärmen genom att lägga till den via **Inställningar → Ljudspelaren → Personalisering → Huvudskärmsåtgärder**. Tryck på konfigurationsikonen i det övre högra hörnet på sömntimeraskärmen för att aktivera exakta minut-för-minut-justeringar.
{{% /details %}}

{{% details title="Kan jag använda Flacbox utan internetanslutning?" closed="true" %}}
**Ja — när du väl har laddat ned musik eller aktiverat offlineläge för en mapp spelar Flacbox allt helt offline.**<br><br>

Offlineinnehåll finns under **Lokala filer** och fortsätter att fungera i flygplansläge, på flygningar och var som helst utan Wi-Fi eller mobildata. Enbart molnspår (de du inte har laddat ned) är nedtonade tills du återfår en anslutning. För resor, aktivera **Offline-läge** för de relevanta mapparna eller ladda ned specifika album och spellistor innan du åker.
{{% /details %}}

{{% details title="Skrobbler Flacbox till Last.fm?" closed="true" %}}
**Ja — Flacbox stöder Last.fm-skrobbling, så varje spår du spelar loggas automatiskt till din Last.fm-profil.**<br><br>

Anslut ditt Last.fm-konto från avsnittet **Anslutningar → Andra tjänster**. När du väl är ansluten skickas all uppspelningsstatistik till Last.fm i bakgrunden. Du kan sedan besöka din Last.fm-profil för att se lyssningstrender, veckans toppkonstnärer och personliga rekommendationer.<br><br>

[Läs den fullständiga installationsguiden](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)
{{% /details %}}

{{% details title="Hur ändrar jag språket i Flacbox-gränssnittet?" closed="true" %}}
**Öppna Inställningar → Språk, välj bland över 120 språk som stöds och starta sedan om appen för att ändringen ska träda i kraft.**<br><br>

Appen stöder lokaliseringar inklusive engelska, franska, tyska, spanska, italienska, portugisiska, ryska, ukrainska, polska, nederländska, arabiska, hebreiska, hindi, japanska, koreanska, kinesiska (förenklad och traditionell), vietnamesiska, turkiska med mera. Välj **Standard** för att automatiskt följa enhetens språkinställning. Efter att ha valt ett nytt språk, avsluta Flacbox helt och öppna den igen så att varje skärm ritas om med de nya översättningarna.
{{% /details %}}

{{% details title="Hur söker jag efter en låt, ett album eller en artist i Flacbox?" closed="true" %}}
**Tryck på förstoringsglaset i valfri lista — Musikbibliotek, Spellistor, Album, Artister, Genrer eller inuti en mapp — och skriv ett namn för att filtrera resultaten omedelbart.**<br><br>

Sökning är lokal och fungerar helt offline mot din biblioteksdatabas, så resultat visas medan du skriver även på långsamma nätverk. Du kan också söka inuti en specifik spellista, ett album eller en mapp för att hitta ett enda spår bland hundratals. Spår, album, artister, genrer, kompositörer och mappar är alla sökbara.
{{% /details %}}

{{% details title="Fungerar Flacbox med Bluetooth-hörlurar, AirPods och externa DAC:er?" closed="true" %}}
**Ja — Flacbox spelar via valfri ljudutgång som din iPhone, iPad eller Mac kan använda: inbyggda högtalare, trådbundna hörlurar, Bluetooth-enheter (AirPods, Beats, Sony, Bose osv.) och USB / Lightning DAC:er.**<br><br>

För Hi-Res-utmatning till en extern DAC, byt audiokodek till **FFmpeg** i **Inställningar → Ljudspelaren → Allmänt** och välj lämplig **Ljudutgångssamplingsfrekvens** och antal kanaler. AirPods stjälkreglagen (spela / pausa, nästa / föregående) fungerar som förväntat och låsskärmskontrollerna kan anpassas i **Inställningar → Ljudspelaren → Personalisering → Uppspelningskontroller på låsskärmen**.
{{% /details %}}

{{% details title="Hur använder jag ett USB-flashminne eller SD-kort med Flacbox på iPhone eller iPad?" closed="true" %}}
**Anslut enheten till din iPhone eller iPad via Lightning-till-USB- eller USB-C-adaptern och öppna sedan i Flacbox Lokala filer → Filer på denna iPhone → Öppna mapp, navigera till enheten och välj musikmappen.**<br><br>

Flacbox spelar filer direkt från enheten utan att kopiera dem till intern lagring, vilket är användbart för mycket stora förlustfria bibliotek. Du kan också importera spår till musikbiblioteket eller lägga till dem i spellistor på samma sätt. Appen stöder **Apple-certifierade kortläsare** och **iXpand Flash Drives** — för iXpand, sätt in det i Lightning-porten och enheten visas automatiskt på anslutningsskärmen. Se de fullständiga steg-för-steg-instruktionerna i [Hur man ansluter ett USB-flashminne till iPhone och lyssnar på musik](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).
{{% /details %}}

{{% details title="Varför synkroniseras inte min molnmusik i Flacbox?" closed="true" %}}
**De flesta synkroniseringsproblem orsakas av en utgången auth-token, app-bakgrundning eller ingen aktiv internetanslutning — öppna Anslutningar, återauktorisera tjänsten och kör sedan synk manuellt från Inställningar → Bibliotek → Online-synkronisering.**<br><br>

Online-synk körs bara när appen är i förgrunden, så synkronisering av ett stort bibliotek kan ta en stund. För att påskynda det, håll Flacbox öppen, anslut din enhet till ström och aktivera **Inställningar → Skärm → Alltid aktiv**. För mycket stora bibliotek, kör synk på skrivbordsversionen av appen och överför resultatet till iOS med **Säkerhetskopiering och återställning**.
{{% /details %}}

{{% details title="Hur kontaktar jag Flacbox-support?" closed="true" %}}
**Öppna Inställningar → Skicka feedback för att e-posta vårt supportteam direkt från appen, med diagnostikinformation bifogad automatiskt.**<br><br>

Du kan också besöka [Hjälpcenter](/docs/), bläddra i [Hur man-guider](/docs/howto/) eller kolla in det bredare [FAQ](/docs/faq/) för självbetjäningssvar. Vi svarar vanligtvis inom en arbetsdag.
{{% /details %}}

</div>
