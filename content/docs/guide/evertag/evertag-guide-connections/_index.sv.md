---
title: "Anslutningar"
date: 2020-02-01
description: "Lär dig hur du ansluter molnlagring, NAS och din dator till Evertag. Få åtkomst till och redigera ljudfiler direkt från molnlagring, personlig NAS eller Mac/PC."
keywords: [
  "Evertag molninställning", "anslut iCloud till Evertag", "SMB-filåtkomst iOS",
  "WebDAV ljudtaggeditor", "NAS metadataredigering", "Wi-Fi Drive Evertag",
  "överföra ljudfiler till iPhone", "Evertag iTunes File Sharing", "redigera FLAC-taggar från molnet"
]
tags: ["guide", "evertag", "anslutningar"]
readingTime: 11
---


På den här skärmen kan du ansluta olika källor som innehåller dina ljudfiler. Du kan integrera populära molntjänster som Google Drive, Dropbox, OneDrive, iCloud och andra, samt ansluta din Mac eller PC. Dessutom har du möjlighet att redigera ljudfiler som finns på Apple Time Capsule, WD Cloud Home eller valfri NAS som stödjer SMB eller WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Anslutningsskärm" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Snabbåtkomst

Längst upp på Anslutningsskärmen hittar du en lista för **Snabbåtkomst**. Varje molnmapp som du lägger till i favoriter — även en som är begravd flera nivåer djupt — visas här så att du kan hoppa till den utan att navigera genom överordnade mappar varje gång.

## Anslut till molnlagring

- Öppna fliken 'Anslutningar'
- Välj 'Anslut till molnlagring' från menyn
- Välj en molnlagringstjänst från listan
- Ange dina uppgifter och tryck på 'Färdig.'

Om du stöter på problem, kontrollera din internetanslutning och inloggning/lösenord.  
I Premium-versionen av appen kan du lägga till ett obegränsat antal tjänster.

## Molnlagringstjänster som stöds

För närvarande stödjer applikationen de mest populära molnlagringstjänsterna: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), samt alla SMB- eller WebDAV-servrar.

## Säkerhet och integritet

Vi använder endast officiella SDK:er och säkra anslutningar för att interagera med anslutna molntjänster. Ditt inloggningsnamn och lösenord är inte tillgängliga för applikationen. Alla förfrågningar från applikationen till molntjänsten krypteras.

När du anger ditt inloggningsnamn och lösenord visar applikationen den officiella auktoriseringssidan från molntjänstleverantören, och hela auktoriseringsprocessen sker utanför applikationen. Molntjänstleverantören skickar en auth-token till applikationen efter framgångsrik auktorisering, och denna token används för API-anrop.

En auth-token är en digital nyckel som tillåter tredjepartsapplikationer att interagera med molnlagring. Auth-token lagras på din enhet i ett säkert systemlagringsutrymme kallat Keychain. Du kan ladda ner dina filer från den anslutna molntjänsten till enheten, och dessa filer placeras i appens "Dokument"-katalog. Du kan ta bort dessa filer när som helst med den inbyggda filhanteraren.

Applikationen delar inte någon information från det anslutna molnkontot. Du kan återkalla åtkomst till ditt molnkonto när som helst genom att öppna kontoinställningssidan i din webbläsare.

## Avvisa auth-token

Logga in på ditt konto i en webbläsare och navigera till inställningssidan. Där kan du hitta alla tredjepartsappar som är anslutna till ditt molnkonto och ta bort dem om du inte längre vill använda den applikationen. Detaljerade instruktioner finns tillgängliga [här](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan också koppla från anslutna molnkonton i applikationen, och auth-token tas också bort från din enhet. Om du tar bort applikationen från din enhet, kommer all nedladdad data och åtkomsttoken också att tas bort.

## Koppla från molnlagring eller ändra konfiguration

- Öppna molnlagringsalternativ: Lokalisera först molnlagringen du vill hantera i appens gränssnitt.
- Tryck på '...'-knappen: Bredvid tjänstens titel hittar du en '...'-knapp. Tryck på den för att komma åt ytterligare alternativ.
  - **Byt namn**: Om du vill ändra namnet på molntjänsten som det visas i din lista, välj 'Byt namn.'
  - **Inställningar**: För att ändra konfiguration eller autentiseringsdata för molntjänsten, välj 'Inställningar.' Ibland kan du behöva omauktorisera den anslutna molntjänsten om auktoriseringstoken har gått ut.
  - **Koppla bort**: Om du vill helt avbryta anslutningen mellan appen och molntjänsten, välj 'Koppla bort.' Tänk på att om du väljer det här alternativet tas alla låtar kopplade till molntjänsten bort från appens musikbibliotek, men de finns kvar på servern.

## Anslut till dator eller NAS

Du kan också ansluta din dator, personliga NAS eller andra nätverksenheter med hjälp av SMB-, DLNA- eller WebDAV-protokollet.

## Anslut till dator med SMB

- Tryck på "Anslut till molnlagring" → SMB.
- Ange datorns IP-adress och namnet på den delade mappen i URL-fältet med formatet smb://dator-ip-adress/delad-mappnamn
- Välj protokollversion: Auto, SMB1, SMB2
- Ange inloggning och lösenord (om nödvändigt)
- Tryck på "Färdig."

Om din anslutning är framgångsrik ser du den anslutna lagringen i avsnittet "Molnlagring."  
En fullständig handledning om hur du ansluter din Mac eller PC med SMB finns tillgänglig [här](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Anslut till NAS med WebDAV

Alla steg är desamma utom URL-fältet.  
URL:en ska vara i formatet http://servernamn, eller https://servernamn om servern stödjer SSL.  
En fullständig handledning om hur du ansluter NAS med WebDAV-protokollet finns tillgänglig [här](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Tillgängliga enheter

Det här avsnittet visar alla enheter i ditt lokala nätverk som du kan ansluta till via applikationen.  
För att upprätta en anslutning med en enhet, följ dessa steg:

- Öppna appen och gå till avsnittet "Tillgängliga enheter."
- Tryck på den enhet du vill ansluta till från listan.
- Om nödvändigt, ange dina inloggningsuppgifter för att slutföra anslutningen.

## Wi-Fi Drive

Wi-Fi Drive är en praktisk teknik som möjliggör trådlösa filöverföringar från din dator till din iOS-enhet via en skrivbordswebbläsare.  
För att använda den här funktionen effektivt, se till att din enhet och dator är anslutna till samma Wi-Fi-nätverk.  
Här är en steg-för-steg-guide om hur du använder Wi-Fi Drive.

## Aktivera Wi-Fi Drive

- Öppna applikationen och gå till fliken "Anslutningar."
- Välj "Anslut via Wi-Fi" för att komma åt Wi-Fi Drive-huvudskärmen.
- Tryck på "Starta Wi-Fi Drive" för att aktivera Wi-Fi Drive.

## Kom åt Wi-Fi Drive på din dator

- På din dator (stationär eller bärbar), öppna en webbläsare (till exempel Chrome, Firefox eller Safari).
- I webbläsarens adressfält, ange URL:en som tillhandahålls av applikationen.

## Överför filer trådlöst

När webbsidan som motsvarar din iOS-enhet öppnas i webbläsaren, kan du enkelt dra och släppa filer från din dator till webbsidan.  
Filerna du drar och släpper börjar överföras till din iOS-enhet och är tillgängliga i applikationen.

Detaljerade instruktioner om hur du överför filer trådlöst med Wi-Fi Drive finns tillgängliga [här](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing är en annan teknik som låter dig överföra filer från en dator till en enhet med hjälp av Finder-appen på din Mac och en Lightning-kabel.  
- Anslut bara enheten till datorn med en kabel och kör Finder-appen på din Mac.
- Öppna "Platser" → "Din anslutna enhet" → "Filer" → och hitta den aktuella appen.
- Tryck på appens ikon för att se alla delade mappar.
- Kopiera filer från datorn till den delade mappen på enheten med dra-och-släpp.

Detaljerade instruktioner om hur du använder iTunes File Sharing finns tillgängliga [här](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Anslut ett USB-flashkort

Om du har ett SD-kort eller USB-minne kan du ansluta det med en Lightning- eller USB-C-kortläsare på iPhone/iPad, eller ansluta det direkt till en Mac. Appen stödjer för närvarande Apple-certifierade kortläsare. Vi har detaljerade instruktioner om hur du ansluter ett USB-flashkort till din iPhone eller iPad och hanterar filer på det, tillgängliga [här](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Anslutna enheter visas i avsnittet **Externa tillbehör** på Anslutningsskärmen.

## Filhanterare

När du har anslutit en molnlagringstjänst, tryck på dess ikon för att visa alla tillgängliga filer och mappar. Du kan använda den inbyggda filhanteraren för att arbeta med dessa filer — ladda ner, byta namn, flytta och mer. När du startar en nedladdning visas filen i överföringskön. För att visa överföringskön, gå till fliken "Lokala filer" och tryck på de roterande pilarna i det övre vänstra hörnet. Alla nedladdade filer och mappar finns tillgängliga i avsnittet "Lokala filer."

## Övre verktygsfält

Det övre verktygsfältet, bekvämt placerat under navigeringsfältet, erbjuder flera användbara åtgärder för enkel åtkomst. Du kan visa eller dölja det här verktygsfältet med en enkel svepning nedåt. Här är de tillgängliga åtgärderna:

- **Sök**: Det här alternativet låter dig utföra en snabb sökning i den aktuella katalogen, vilket gör det enkelt att hitta specifika filer eller mappar.

## Mappalternativ

När du öppnar en mapp i appen hittar du en praktisk uppsättning åtgärder tillgängliga genom att trycka på "..."-knappen i det övre högra hörnet av skärmen.  
Här är en genomgång av dessa åtgärder:

- **Välja**: Aktivera filurvalläge. Det här läget gör att du kan välja en eller flera filer i mappen, vilket gör det enkelt att utföra åtgärder på valda objekt.
- **Ny mapp**: Skapa en ny mapp i den aktuella mappen. Den här funktionen låter dig organisera dina filer och hålla ditt bibliotek välstrukturerat.
- **Ladda upp filer**: Ladda upp filer från din enhet till onlinemappen. Den här åtgärden låter dig överföra filer till molnet eller servern, vilket gör dem tillgängliga från var som helst.
- **Sök**: Sök efter specifika filer i den aktuella mappen. Det här är särskilt användbart för att snabbt hitta specifika objekt i en stor samling.
- **Sortera**: Sortera filer i mappen efter kriterier som namn, storlek eller redigeringsdatum. Standardsorteringsläget speglar vanligtvis sorteringsordningen på servern, men du kan ändra det efter dina önskemål.
- **Rutnät-/listvy**: Växla mellan två visningslägen: tabellvy och miniatyrvy. Tabellvyn presenterar filer i en lista, medan miniatyrvyn visar visuella representationer av filerna, vilket gör det lättare att identifiera innehåll på en blick.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Molnmappssortering" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Redigera onlinefiler

När du behöver hantera flera filer i din molnlagring i den här appen kan du använda urvalläget för att effektivisera dina åtgärder. Följ dessa steg för effektiv filhantering:

- **Aktivera urvalläge**: Öppna appen på din enhet och navigera till avsnittet som innehåller din molnlagring. Leta efter "..."-knappen (ellips) i det övre högra hörnet. Tryck på den och välj menyalternativet "Välja" för att aktivera urvalläge.
- **Välj filer**: Du märker att kryssrutor visas bredvid varje fil eller mapp i listan. Välj en eller flera filer eller mappar genom att trycka på kryssrutorna bredvid dem.
- **Utför olika åtgärder**: När du har valt de filer eller mappar du vill hantera, har du tillgång till flera åtgärder anpassade efter dina behov:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Filval" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Filåtgärder

Nära filens titel ser du ellipssymbolen "..." (tre punkter) – det här är åtgärdsmenyn.  
Tryck på den för att visa en lista med tillgängliga åtgärder:

- **Redigera ljudtaggar**: Genom att välja det här alternativet kan du komma åt den inbyggda taggeditorn, vilket låter dig ändra ljudtaggar för den valda filen. Filen laddas tillfälligt ner till en temporär katalog och laddas sedan upp till lagringen efter att du bekräftat ändringarna.
- **Lägg till i favoriter**: Den här åtgärden lägger till filen i din lista över favoritfiler för snabb och bekväm åtkomst.
- **Ladda ner**: Välj den här åtgärden för att ladda ner filen eller mappen till din enhet, vilket gör den tillgänglig för offlineanvändning.
- **Byt namn**: Det här alternativet låter dig byta namn på filen direkt på fjärrlagringen, vilket möjliggör anpassad filnamngivning.
- **Flytta**: Välj den här åtgärden för att flytta filen till en annan mapp i din molnlagring, vilket underlättar en organiserad filstruktur.
- **Öppna i**: Använd den här åtgärden för att exportera filen till en annan kompatibel app. Filen laddas ner till din enhet och sedan visas delningsdialogrutan för ytterligare delning eller interaktion.
- **Ta bort**: Var försiktig med den här åtgärden, eftersom den permanent tar bort filen från din molnlagring. **Borttagningen kan inte ångras**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Filalternativ" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Om listan med åtgärder överstiger det tillgängliga skärmutrymmet, rulla helt enkelt nedåt i åtgärdsmenyn för att komma åt ytterligare alternativ.

## Mappalternativ

För varje mapp i din molnlagring har du olika åtgärder tillgängliga. För att komma åt dessa alternativ, tryck helt enkelt på ellipsikonen "..." bredvid mappens titel. Om du inte ser alla åtgärder, rulla nedåt för att visa fler alternativ. Här är de tillgängliga åtgärderna:

- **Lägg till i favoriter**: Använd den här åtgärden för att lägga till mappen i din lista över favoritfiler för snabb och bekväm åtkomst.
- **Ladda ner**: Ladda ner allt innehåll i mappen till din enhet för offlineåtkomst.
- **Byt namn**: Byt namn på mappen direkt på fjärrlagringen.
- **Flytta**: Flytta mappen till en annan plats i din molnlagring.
- **Ta bort**: Var försiktig med den här åtgärden, eftersom den permanent tar bort mappen och dess innehåll från din molnlagring. **Åtgärden kan inte ångras**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Mappalternativ" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
