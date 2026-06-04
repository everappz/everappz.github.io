---
title: "Anslutningar"
date: 2020-01-01
description: "Lär dig hur du ansluter molntjänster, datorer, NAS-enheter och hanterar dina musikfiler med Evermusic. Steg-för-steg-guide för Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes-fildelning med mera."
keywords: [
  "Evermusic", "molnmusikspelare", "NAS-strömning", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes-fildelning",
  "ansluta molnlagring", "musiköverföring iPhone", "filhanterare iOS"
]
tags: ["evermusic", "guide", "anslutningar"]
readingTime: 11
---


På skärmen Anslutningar kan du ansluta alla källor som innehåller din musik — populära molntjänster, självhostade medieservrar, din Mac eller PC, en personlig NAS, Apple Time Capsule, WD My Cloud Home, till och med ett USB-minne — och använda dem alla från ett enhetligt gränssnitt. Anslutningar är också där du ställer in Snabbåtkomst till djupt kapslade molnmappar och autentiserar Last.fm för scrobbling.

Skärmen är uppdelad i tydligt märkta avsnitt så att den skalas från ett enda iCloud Drive-konto till ett bibliotek spritt över flera moln och NAS-enheter: Snabbåtkomst längst upp (dina favoritcloudmappar), Molnlagring (de konton du har lagt till), Lokalt nätverk (Bonjour-identifierade enheter), Dator (Wi-Fi Drive, iTunes-fildelning, SMB), Externa tillbehör (anslutna USB-minnen) och Andra tjänster (Last.fm och liknande).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Connections Screen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Anslut till molnlagring

- Öppna fliken Anslutningar.
- Välj Anslut till molnlagring från menyn.
- Välj en molnlagringstjänst från listan.
- Logga in på leverantörens officiella auktoriseringssida (Evermusic ser aldrig ditt lösenord).
- Tryck på Färdig.

{{< cards cols="1">}}
  {{< card title="" subtitle="Connect Cloud Storage Provider Picker" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Om du stöter på problem, dubbelkolla din internetanslutning och inloggningsuppgifter och se till att tvåfaktorsautentisering är korrekt konfigurerad för den tjänsten.  
I Premium-versionen av appen kan du lägga till ett obegränsat antal tjänster. Gratisanvändare kan ansluta ett enda molnkonto åt gången.

## Stödda molnlagringstjänster

Evermusic stöder hela utbudet av populära moln- och självhostade tjänster. Gratisanvändare får samma leverantörskatalog men med engångsgränsen; Premium låser upp obegränsade konton och tar bort de flesta andra begränsningar.

- **Personliga molnkonton:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Självhostade servrar och mediebibliotek:** Plex · Jellyfin · Emby · Subsonic (och alla Subsonic-kompatibla servrar — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (och Owncloud, via det delade API:et) · Synology Drive · QNAP.
- **NAS och fildelningsprotokoll:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (lösenord eller autentisering med offentlig nyckel), NFS och DLNA (skrivskyddat — uppspelning och nedladdning).
- **S3-kompatibel objektlagring:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage eller valfri S3-API-slutpunkt.
- **Lokal nätverksupptäckt:** avsnittet Tillgängliga enheter listar automatiskt alla enheter på ditt Wi-Fi som annonserar sig via Bonjour / mDNS — Plex, Jellyfin, Emby-servrar, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, AirPort-routrar med anslutna enheter och så vidare.

## Säkerhet och integritet

Vi använder bara officiellt SDK och säker anslutning för att interagera med anslutna molntjänster. Ditt användarnamn och lösenord är inte tillgängliga för programmet. Alla förfrågningar från applikationen till molntjänsten är krypterade.

När du anger ditt inloggningsnamn och lösenord visar programmet den officiella auktoriseringssidan som tillhandahålls av molntjänstleverantören och hela auktoriseringsprocessen sker utanför applikationen. Molntjänstleverantören skickar en auth-token till applikationen efter lyckad auktorisering och den token används för att göra API-anrop.

Auth-token är en digital nyckel som tillåter tredjepartsapplikationer att interagera med molnlagring. Auth-token lagras på din enhet i ett säkert systemlagringsutrymme kallat Keychain. Du kan ladda ner dina filer från den anslutna molntjänsten till enheten och dessa filer placeras i appens "Documents"-katalog. Du kan ta bort dessa filer när som helst med den inbyggda filhanteraren.

Applikationen delar ingen information från det anslutna molnkontot. Du kan återkalla åtkomst till ditt molnkonto när som helst genom att öppna kontoinställningssidan i din webbläsare.

## Återkalla auth-token

Logga in på ditt konto i webbläsaren och navigera till inställningssidan. Där hittar du alla tredjepartsappar som är anslutna till ditt molnkonto och kan ta bort dem om du inte vill använda den applikationen längre. Detaljerade instruktioner finns [här](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan också koppla bort de anslutna molnkontona i applikationen och auth-token tas även bort från din enhet. Om du tar bort applikationen från din enhet tas alla nedladdade data och åtkomsttokens också bort.

## Koppla bort molnlagring eller ändra konfiguration

- Öppna molnlagringsalternativ: Hitta först den molnlagring du vill hantera i appens gränssnitt.
- Tryck på '...'-knappen: Bredvid tjänsttiteln ser du en '...'-knapp. Tryck på den för att komma åt ytterligare alternativ.
  - **Byt namn**: Om du vill ändra namnet på molntjänsten som det visas i din lista, välj 'Byt namn.'
  - **Inställningar**: För att ändra konfiguration eller autentiseringsdata för molntjänsten, välj 'Inställningar.' Ibland kan du behöva omauktorisera den anslutna molntjänsten om auktoriseringstoken har gått ut.
  - **Koppla bort**: Om du vill helt avbryta anslutningen mellan appen och molntjänsten, välj 'Koppla bort.' Tänk på att detta alternativ tar bort alla låtar associerade med den här molntjänsten från appens musikbibliotek, men de finns kvar på servern.

{{< cards cols="1">}}
  {{< card title="" subtitle="Connected Cloud Storage More Actions Menu" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Anslut till dator eller NAS

Du kan också ansluta din dator, personliga NAS eller andra nätverksenheter med SMB, DLNA eller WebDAV-protokollet.

## Anslut till dator med SMB

- Tryck på "Anslut till molnlagring" → SMB.
- Ange datorns IP-adress och delade mappnamn i URL-fältet i formatet smb://computer-ip-address/shared-folder-name
- Välj protokollversion: Auto, SMB1, SMB2
- Ange användarnamn och lösenord (om det krävs)
- Tryck på "Färdig".

Om din anslutning lyckades ser du ansluten lagring i avsnittet "Molnlagring".  
En fullständig guide om hur du ansluter din MAC eller PC med SMB finns [här](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB Connection Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Anslut till NAS med WebDAV

Alla steg är desamma förutom URL-fältet.  
URL ska vara i formatet http://server-name, eller https://server-name om servern stöder SSL.
En fullständig guide om hur du ansluter NAS med WebDAV-protokollet finns [här](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV Connection Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Anslut till dator eller NAS med DLNA

Du kan också dela ett musikbibliotek på din Windows-PC eller personliga NAS med DLNA-protokollet och komma åt det biblioteket i appen som beskrivs [här](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA är ett populärt och brett använt protokoll, men det låter dig bara spela eller ladda ner musik. Du kan inte ladda upp filer eller skapa nya mappar på servern.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA Connection Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Tillgängliga enheter

Det här avsnittet visar alla enheter i ditt lokala nätverk som du kan ansluta till via applikationen.  
Följ dessa steg för att upprätta en anslutning med en enhet:

- Öppna appen och gå till avsnittet "Tillgängliga enheter".
- Tryck på den enhet du vill ansluta till från listan.
- Om det behövs anger du dina inloggningsuppgifter för att slutföra anslutningen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Available Devices on the Local Network" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive är en praktisk teknik som möjliggör trådlös filöverföring från din dator till din iOS-enhet via en webbläsare på skrivbordet.  
För att använda den här funktionen effektivt, se till att din enhet och dator är anslutna till samma Wi-Fi-nätverk.  
Här är en steg-för-steg-guide om hur du använder Wi-Fi Drive.

## Aktivera Wi-Fi Drive

- Öppna programmet och gå till fliken "Anslutningar".
- Välj "Anslut via Wi-Fi" för att komma åt Wi-Fi Drive-huvudskärmen.
- Tryck på "Starta Wi-Fi Drive" för att aktivera Wi-Fi Drive.

## Öppna Wi-Fi Drive på din dator

- På din dator (stationär eller bärbar), öppna en webbläsare (till exempel Chrome, Firefox eller Safari).
- I webbläsarens adressfält anger du URL:en som tillhandahålls av applikationen.

## Överför filer trådlöst

När webbsidan som motsvarar din iOS-enhet öppnas i webbläsaren kan du enkelt dra och släppa filer från din dator till webbsidan.  
Filerna du drar och släpper börjar överföras till din iOS-enhet och är tillgängliga i applikationen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive Server Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Detaljerade instruktioner om hur du överför filer trådlöst med WiFi-Drive finns [här](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes-fildelning

iTunes-fildelning är en annan teknik som låter dig överföra filer från datorn till enheten med hjälp av Finder-appen på din Mac och en lightning-kabel.  
- Anslut helt enkelt en enhet till datorn med en kabel och starta Finder-appen på din Mac.
- Öppna "Platser" → "Din anslutna enhet" → "Filer" → och hitta Evermusic-appen.
- Tryck på appikonen för att se alla delade mappar.
- Kopiera filer från datorn till den delade mappen på enheten med drag-och-släpp.

Detaljerade instruktioner om hur du använder iTunes-fildelning finns [här](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing on Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Anslut ett USB-minne

Om du har ett SD-kort kan du ansluta det med en lightning-kortläsare. Appen stöder för närvarande Apple Certified kortläsare och iXpand Flash Drives. Om du har iXpand Flash Drive — sätt in det i lightning-porten och öppna programmet. Du ser ett meddelande om 'Extern enhet ansluten' och enhetsinformation. Tryck bara på flash-enhetsikonen för att komma åt musikmappen och tryck på en ljudfil för att börja spela. Vi har detaljerade instruktioner om hur du ansluter ett USB-minne till iPhone och lyssnar på musik eller hanterar filer som finns på det, tillgängliga [här](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Filhanterare

När du har anslutit en molnlagringstjänst, tryck på dess ikon för att visa alla tillgängliga filer och mappar. Du kan använda den inbyggda filhanteraren för att arbeta med dessa filer — ladda ner, byta namn, flytta och mer. När du startar en nedladdning visas filen i överföringskön. För att visa överföringskön, gå till fliken "Lokala filer" och tryck på de snurrande pilarna i det övre vänstra hörnet. Alla nedladdade filer och mappar finns i avsnittet "Lokala filer".

## Övre verktygsfält

Det övre verktygsfältet, som bekvämt finns under navigeringsfältet, erbjuder flera användbara åtgärder för enkel åtkomst. Du kan visa eller dölja det här verktygsfältet med ett enkelt svepande nedåt-gest. Här är de tillgängliga åtgärderna:

- **Sök**: Med det här alternativet kan du göra en snabb sökning i den aktuella katalogen, vilket gör det enkelt att hitta specifika filer eller mappar.
- **Fortsätt uppspelning**: Om det är aktiverat i appinställningarna återställer den här funktionen ljudspelarens kö och den senaste mediepositionen för den aktuella mappen. Det är ett praktiskt sätt att fortsätta där du slutade i ditt musikbibliotek.
- **Spela alla**: Genom att välja den här åtgärden skannar appen den aktuella mappen och dess undermappar och lägger till alla hittade ljudfiler i en ny spelarkö. Det är användbart när du vill spela all musik i en viss katalog.
- **Blanda alla**: Liknar "Spela alla", men den här åtgärden skannar den aktuella mappen och dess undermappar men blandar filerna innan de läggs till i ljudspelarens kö. Det är ett bra sätt att njuta av din musik i slumpmässig ordning för lite variation.

{{< cards cols="1">}}
  {{< card title="" subtitle="Top Toolbar Inside a Cloud Folder" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Mappalternativ

När du öppnar en mapp i appen hittar du en praktisk uppsättning åtgärder tillgängliga genom att trycka på "..."-knappen i skärmens övre högra hörn.  
Här är en beskrivning av dessa åtgärder:

- **Välja**: Aktivera filvalläge. Det här läget gör att du kan välja en eller flera filer i mappen, vilket gör det enkelt att utföra åtgärder på valda objekt.
- **Ny mapp**: Skapa en ny mapp i den aktuella mappen. Den här funktionen låter dig organisera dina filer och hålla ditt bibliotek välstrukturerat.
- **Aktivera offline-läge**: Aktivera offline-läge för den aktuella mappen. Offline-läge går bortom enkel nedladdning; det övervakar aktivt mappen för ändringar. Om du lägger till nya filer i mappen online, laddar appen automatiskt ner dessa filer till din enhet. Det säkerställer att ditt lokala bibliotek hålls uppdaterat med ändringar på servern.
- **Ladda upp filer**: Ladda upp filer från din enhet till online-mappen. Den här åtgärden låter dig överföra filer till molnet eller servern, vilket gör dem tillgängliga varifrån som helst.
- **Sök**: Sök efter specifika filer i den aktuella mappen. Det är särskilt användbart för att snabbt hitta specifika objekt i en stor samling.
- **Sortera**: Sortera filer i mappen efter kriterier som namn, storlek eller redigeringsdatum. Standardsorteringsläget speglar vanligtvis sorteringsordningen på servern, men du kan ändra det enligt dina preferenser.
- **Rutnät/listvy**: Växla mellan två visningslägen: tabellvy och miniatyrvy. Tabellvyn presenterar filer i en lista, medan miniatyrvyn visar visuella representationer av filerna, vilket gör det lättare att identifiera innehåll på ett ögonkast.

{{< cards cols="1">}}
  {{< card title="" subtitle="Current Folder More Actions Menu" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Redigera onlinefiler

När du behöver hantera flera filer i din molnlagring på Evermusic kan du använda valläge för att effektivisera dina åtgärder. Följ dessa steg för effektiv filhantering:

- **Aktivera valläge**: Öppna appen på din enhet och navigera till avsnittet som innehåller din molnlagring. Leta efter det övre högra hörnet där du hittar "..."-knappen (ellips). Tryck på den och välj menyobjektet "Välja" för att aktivera valläge.
- **Välj filer**: Du märker att kryssrutor visas bredvid varje fil eller mapp i listan. Välj en eller flera filer eller mappar genom att trycka på kryssrutorna bredvid dem.
- **Utför olika åtgärder**: När du har valt de filer eller mappar du vill hantera har du tillgång till flera åtgärder anpassade till dina behov:

{{< cards cols="1">}}
  {{< card title="" subtitle="Selection Mode for Online Files" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Filåtgärder

Nära filens titel ser du ellipssymbolen "..." (tre punkter) — detta är åtgärdsmenyn.  
Tryck på den för att visa en lista med tillgängliga åtgärder:

- **Spela nästa**: Välj den här åtgärden för att infoga den valda filen längst upp i din spelarkö, vilket säkerställer att den spelas omedelbart efter det aktuella spåret.
- **Spela senare**: Att välja det här alternativet lägger till filen längst ned i din spelarkö, vilket säkerställer att den spelas efter den befintliga kön.
- **Lägg till i musikbibliotek**: Den här åtgärden låter dig inkludera filen i ditt musikbibliotek, vilket gör den lättillgänglig och snyggt organiserad efter artist, album, genre eller kompositör.
- **Lägg till i en spellista**: Använd den här åtgärden för att lägga till filen i en befintlig spellista eller skapa en ny.
- **Redigera ljudtaggar**: Genom att välja det här alternativet kan du öppna Evermusics inbyggda taggeditor, vilket låter dig ändra ljudtaggar för den valda filen. Filen laddas tillfälligt ner till en temporär katalog och laddas sedan upp till lagringen efter att du bekräftar ändringarna.
- **Lägg till i favoriter**: Den här åtgärden lägger till filen i din lista med favoritfiler för snabb och bekväm åtkomst.
- **Ladda ner**: Välj den här åtgärden för att ladda ner filen eller mappen till din enhet, vilket gör den tillgänglig för offline-användning.
- **Byt namn**: Det här alternativet låter dig byta namn på filen direkt på fjärrlagringen, vilket möjliggör anpassad filnamngivning.
- **Flytta**: Välj den här åtgärden för att flytta filen till en annan mapp i din molnlagring, vilket hjälper till att upprätthålla en organiserad filstruktur.
- **Öppna i**: Använd den här åtgärden för att exportera filen till en annan kompatibel app. Filen laddas ner till din enhet och sedan visas Dela-dialogrutan för ytterligare delning eller interaktion.
- **Ta bort**: Var försiktig med den här åtgärden, eftersom den permanent tar bort filen från din molnlagring. Denna borttagning kan inte ångras.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu for a Single File" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Om listan med åtgärder överskrider det tillgängliga skärmutrymmet, bläddra helt enkelt ner i åtgärdsmenyn för att komma åt ytterligare alternativ.

## Mappåtgärder

För varje mapp i din molnlagring har du olika åtgärder tillgängliga. För att komma åt dessa alternativ, tryck helt enkelt på ellipsikonen "..." bredvid mappens titel. Om du inte ser alla åtgärder, bläddra ner för att visa fler val. Här är de tillgängliga åtgärderna:

- **Spela alla**: Ersätt den aktuella spelarkön med alla objekt från den valda mappen.
- **Spela nästa**: Lägg till hela mappen längst upp i spelarkön, precis efter det aktuella spåret.
- **Spela senare**: Lägg till mappens innehåll längst ned i spelarkön.
- **Lägg till i musikbibliotek**: Den här åtgärden inkluderar mappens innehåll sömlöst i ditt musikbibliotek, vilket gör det lättillgängligt och snyggt organiserat efter artist, album, genre eller kompositör.
- **Lägg till i spellista**: Du kan inkludera hela mappen i en spellista. Du har också möjlighet att skapa en ny spellista, och mappens namn tilldelas automatiskt.
- **Lägg till i favoriter**: Använd den här åtgärden för att lägga till mappen i din lista med favoritfiler för snabb och bekväm åtkomst.
- **Aktivera offline-läge**: Genom att aktivera offline-läge för en vald mapp, går applikationen bortom enkel nedladdning. Den skannar kontinuerligt efter ändringar, och om nya filer läggs till i online-mappen laddas de automatiskt ner till appen.
- **Ladda ner**: Ladda ner allt mappens innehåll till din enhet för offline-åtkomst.
- **Byt namn**: Byt namn på mappen direkt på fjärrlagringen.
- **Flytta**: Flytta mappen till en annan plats i din molnlagring.
- **Ta bort**: Var försiktig med den här åtgärden eftersom den permanent tar bort mappen och dess innehåll från din molnlagring. Den här åtgärden kan inte ångras.


## Snabbåtkomst

Snabbåtkomstavsnittet finns längst upp på skärmen. Det ger dig snabb åtkomst till dina favorit- och nyligen öppnade filer från anslutna molntjänster.
Varje gång du öppnar en fil eller mapp från molnet läggs den till i listan "Senast öppnade". För att rensa den här listan, öppna "Senaste", tryck på knappen "Fler åtgärder" och välj "Ta bort lista." Du kan också markera djupt kapslade mappar som Favoriter för att komma åt dem snabbt utan att gräva igenom katalogstrukturen.

## Andra tjänster

Det här avsnittet visar extra funktioner som förbättrar din upplevelse. För närvarande stöder appen Last.fm-scrobbling. När den är ansluten skickas dina uppspelningsstatistik automatiskt till ditt Last.fm-konto. Du kan besöka din Last.fm-profil senare för att se lyssnaranalys och få personliga musikrekommendationer. Detaljerade installationsinstruktioner finns [här](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
