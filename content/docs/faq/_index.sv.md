---
date: '2025-06-12T17:00:00+00:00'
title: 'Vanliga frågor'
description: 'Hitta svar på vanliga frågor om Evermusic, Flacbox, Evervideo och Evertag. Utforska funktioner som molnstreaming, filhantering, uppspelningsalternativ, metadataredigering och mer.'
keywords: [
  "Evermusic FAQ", "Flacbox support", "Evervideo hjälp", "Evertag frågor",
  "hur man använder Evermusic", "felsökning av molnmusikspelarens", "guide för offlineuppspelning",
  "support för ljudtaggeditor", "videostreaminproblem", "handledning för filöverföring"
]
tags: [
  "FAQ", "hjälp", "support", "evermusic", "flacbox", "evervideo", "evertag",
  "molninställning", "uppspelningsproblem", "filhantering", "metadataredigering",
  "felsökning", "offlineläge", "musikspelare", "videospelare"
]
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## Lär dig använda våra appar

Letar du efter svar eller hjälp med att använda en av våra appar? Du är på rätt plats.

Våra FAQ-sidor hjälper dig att ansluta molnlagring, hantera musik- och videofiler, ställa in offlineuppspelning, justera equalizerinställningar, fixa metadata och mer.

Utforska FAQ:n för din app nedan för att komma igång, eller bläddra igenom vanliga frågor och svar vi fått från användarnas e-post.

## Välj din app

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="Spela upp 360°-videor, streama från iCloud, titta med undertexter, använd en videoequalizer, organisera innehåll med spellistor och ladda ner videor för offlinevisning."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="Molnmusikspelarе med offlineläge, ljudequalizer, crossfade, gapless uppspelning, spellisthantering, fullt musikbibliotek och inbyggd filhanterare."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="Hi-res-ljudspelare för iPhone och Mac. Lyssna på förlustfria format som FLAC, ALAC, APE och DSD. Finjustera utdata med avancerade ljudinställningar."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="Smart musiktaggeditor med batchredigering. Fixa saknad metadata, albumomslag och mer. Redigera ID3-, FLAC- och APE-taggar — över 120 fält stöds." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## Vanliga problem och svar

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="Varför kan jag inte logga in på pCloud på en äldre iOS-version (15.8.4)?" closed="true" %}}
pClouds webbinloggningssida kanske inte visas korrekt på äldre iOS-versioner som 15.8.4, vilket förhindrar att du anger din e-postadress och ditt lösenord på skärmen för molnanslutning.<br><br>

Som en lösning kan du använda **WebDAV**-protokollet, som stöds av pCloud och fungerar tillförlitligt på alla iOS-versioner.

**WebDAV-konfiguration:**<br>
- **Amerikanska servrar:** `https://webdav.pcloud.com`  
- **Europeiska servrar:** `https://ewebdav.pcloud.com`  
- **Användarnamn:** Din pCloud-e-postadress  
- **Lösenord:** Lösenordet till ditt pCloud-konto  

Öppna appen → Anslutningar → Anslut till molnlagring → Välj **WebDAV** → Ange dina uppgifter och server-URL.

Med den här metoden kan du ansluta till ditt pCloud-lagringsutrymme och komma åt dina filer utan problem på äldre enheter.
{{% /details %}}

{{% details title="Hur spelar man musik via AirPlay från Mac (macOS)?" closed="true" %}}
macOS-versionen av appen har inte inbyggda AirPlay-, Chromecast- eller Bluetooth-anslutningsknappar som på iOS.<br><br>

Följ dessa steg för att använda **AirPlay** på din MacBook Pro:

1. Gå till **övre högra hörnet** av skärmen och öppna **Kontrollcenter** (nära klockan).  
2. Klicka på ikonen **Ljud/Volym**.  
3. På nästa skärm klickar du på **AirPlay** för att se en lista över alla tillgängliga AirPlay-enheter.  
4. Välj önskad enhet för att börja strömma din musik.  

Det här dirigerar allt systemljud (inklusive från Evermusic eller Flacbox) till din valda AirPlay-enhet.
{{% /details %}}

{{% details title="Varför aktiveras inte mitt Premium-köp på Mac om jag köpte det på iPhone?" closed="true" %}}
Livstidsköp och prenumerationer synkroniseras mellan iOS och Mac via **iCloud**.<br><br>

Aktivera Premium på din Mac:<br>
- Se till att du har den senaste appversionen installerad på båda enheterna<br>
- Aktivera **iCloud** på båda enheterna<br>
- Starta appen på din iOS-enhet och vänta 1 minut tills köpinformationen laddas upp<br>
- Installera appen på din Mac från App Store med samma **Apple ID**<br>
- Starta appen och vänta några sekunder tills informationen synkroniseras<br>
- Alternativt trycker du på **Återställ köp** i appens inställningar på båda enheterna<br><br>

Dina Premium-funktioner ska sedan aktiveras på Mac automatiskt.
{{% /details %}}

{{% details title="Hur kan jag synkronisera spellistor automatiskt mellan enheter?" closed="true" %}}
Det finns för närvarande **ingen automatisk synkronisering** för spellistor.<br><br>

Du kan använda något av följande alternativ:<br>
- **Säkerhetskopiering och återställning** från appinställningarna [Hur du överför ditt musikbibliotek mellan enheter i Evermusic: steg-för-steg-guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **Exportera spellista till M3U**, importera sedan på en annan enhet:<br>
  - [Exportera spellistor](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [Importera spellistor](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **Arkivera spellista eller album** och överför via ZIP:<br>
  - [Guide för spellistearkiv](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="Är det säkert att använda era appar? Kan jag inaktivera analys?" closed="true" %}}
Ja, din integritet är vår högsta prioritet.<br><br>

- All data — musikfiler, inställningar, molninloggningar — stannar på din enhet<br>
- Inloggningsuppgifter lagras säkert i **iOS Keychain**<br>
- Vi samlar bara in anonyma krasch- och användningsrapporter<br>
- Du kan avanmäla dig i **Appinställningar → Analys**<br><br>

Mer info:<br>
- [Integritetspolicy](/legal/privacy-policy/)<br>
- [Apple Keychain-säkerhet](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

Om du använder personanpassade annonser kräver Google Mobile Ads att samtycksinställningar visas.<br>
Premium-användare ser inga annonser och annons-SDK:n är helt inaktiverad.
{{% /details %}}

{{% details title="Stöder era appar Familjedelning?" closed="true" %}}
Ja, Familjedelning stöds.<br><br>

Dela köp i appen:<br>
- Se till att köpet är inställt på att delas med din familjegrupp<br>
- På familjemedlemmens enhet, gå till **Inställningar > Köp > Återställ köp**<br>
- Det här begär köpdata från Apples servrar och aktiverar det på deras enhet
{{% /details %}}

{{% details title="Hur snabbar man upp metadata och molnsynkronisering?" closed="true" %}}
Aktivera bakgrundsuppgifter för att förbättra synkroniseringshastigheten:<br><br>

- **Inställningar → Musikbibliotek → Metadataavläsning → Metadataavläsning i bakgrunden**<br>
- **Inställningar → Musikbibliotek → Onlinemusiksync → Bakgrundssynk**<br><br>

Öka också metadataavläsningshastigheten på macOS via **Inställningar → Musikbibliotek**.<br>
Om spelaren är aktiv (ljud spelas upp) pausar iOS inte appen, vilket möjliggör kontinuerlig synkronisering.
{{% /details %}}

{{% details title="Hur kan jag avbryta min prenumeration?" closed="true" %}}
Du kan avbryta din prenumeration med hjälp av Apples officiella instruktioner:<br>
👉 [Avbryta en prenumeration](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="Hur ansluter och streamar man ljud från WD MyCloud EX2 Ultra?" closed="true" %}}

När du lägger till en anslutning i appen via **Anslutningar > Anslut till molnlagring > My Cloud Home** är den officiellt utformad för att stödja **WD MyCloud Home**-enheter.<br>
WD MyCloud EX2 Ultra använder begränsad åtkomst för appar.<br><br>

Men om du har anslutit till en **WD MyCloud EX2 Ultra**, **WD MyCloud Mirror** eller en annan **WD MyCloud**-lagringsmodell kan du fortfarande använda den med följande lösning:<br><br>

1. Öppna **Anslutningar → Anslut till molnlagring → My Cloud Home**<br>
2. Skapa en mapp med hjälp av den inbyggda filhanteraren<br>
3. Ladda upp musikfiler till den här mappen<br>
4. Dessa lagras i en "sandlåda" som bara är tillgänglig för appen<br>
5. Du kan nu strömma eller ladda ned dem direkt<br><br>

⚠️ Endast mappar skapade via appen kommer att vara åtkomliga från NAS:en.
{{% /details %}}

{{% details title="Hur ansluter man till Koofr.eu?" closed="true" %}}
Du kan ansluta Koofr med hjälp av **WebDAV**.<br><br>

- Guide för Koofr WebDAV-konfiguration: [koofr.eu blogg](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- WebDAV-guide för Evermusic/Flacbox: [Ansluta NAS-lagring med WebDAV och lyssna på musik på din iPhone eller Mac](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="Vilka är appens URL-scheman?" closed="true" %}}
Här är de scheman som stöds:<br><br>

**Evermusic**<br>
- iOS (blå ikon): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (röd ikon): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="Musiken slutar spela när appen är i bakgrunden — hur åtgärdar man det?" closed="true" %}}
Om appen kraschar eller pausar i bakgrunden:<br>
- Gå till **Inställningar > Musikbibliotek > Onlinemusiksync > Bakgrundssynk → Inaktivera**<br>
- **Inställningar > Musikbibliotek > Metadataavläsning > Metadataavläsning i bakgrunden → Inaktivera**<br>
- **Inställningar > Filhanterare > Bakgrundsöverföringar → Inaktivera**
{{% /details %}}

{{% details title="Gapless uppspelning fungerar inte — hur åtgärdar man det?" closed="true" %}}
Gapless uppspelning beror på iOS-version och ljudmotor.<br>
Försök att byta ljudmotor:<br>
- Gå till **Inställningar → Ljud spelare → Allmänt → Ljudprocessor**<br>
- Välj **Core Audio** för bättre gapless-stöd
{{% /details %}}

{{% details title="Varför visar appen bara 100 objekt i en lista?" closed="true" %}}
Appen använder sidnumrering för prestanda.<br>
Inaktivera det:<br>
- Gå till **Inställningar → Anpassning → Gräns för inläsning av innehåll → Inaktiverat**<br>
Nu laddas alla objekt på en gång.
{{% /details %}}

{{% details title="Varför finns det konstiga tecken i metadata?" closed="true" %}}
Prova att aktivera metadatanormalisering:<br>
- **Inställningar → Musikbibliotek → Metadataavläsning → Normalisera metadatakodning**
{{% /details %}}

{{% details title="Varför kan inte appen läsa mappnamn med specialtecken?" closed="true" %}}
Det här är ett känt problem med **SMB2-protokollet**.<br><br>

Prova följande lösningar:<br>
- Aktivera **SMB1** på din server och i appinställningarna<br>
- Använd **systemfilväljaren**:<br>
  - Gå till **Lokala filer > Filer på den här enheten > Öppna filer...**<br>
  - Välj mappar/filer med Apples inbyggda meny<br><br>

Alternativt kan du ansluta med **WebDAV** eller **DLNA** om din NAS stöder dem.
{{% /details %}}

{{% details title="Hur laddar man upp och hanterar musik i iCloud?" closed="true" %}}
– **Hur laddar jag upp musik till iCloud?**  <br>
Gå till [https://www.icloud.com](https://www.icloud.com) i din webbläsare, skapa en mapp och ladda upp dina musikfiler direkt från din Mac eller PC.<br>

– **Hur hanterar jag iCloud-lagring?**  <br>
Du har två alternativ:  <br>
1. Använd [https://www.icloud.com](https://www.icloud.com) i din webbläsare för att organisera, ladda upp eller ta bort filer.<br>  
2. I appen, efter att ha anslutit till iCloud via **Anslutningar → Anslut till molnlagring → iCloud Drive**, använd den inbyggda filhanteraren för att ladda upp, ladda ned, byta namn på mappar eller ta bort filer direkt i ditt iCloud-lagringsutrymme — utan att spara dem på din enhet.<br>

⚠️ Var försiktig när du tar bort filer. Appen tar bort dem permanent (de hamnar inte i papperskorgen och kan inte återställas).<br>

Lär dig mer här: [Strömma musik från iCloud Drive på min iPhone eller Mac](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="Hur överför man ett 10 GB musikbibliotek från Windows 11 till sin iPhone för offlineuppspelning?" closed="true" %}}

Du har flera tillförlitliga alternativ för att flytta ditt musikbibliotek från din Windows 11-dator till din iPhone och använda det offline i appen. Välj den metod som fungerar bäst för dig:

1. **Använda kabelanslutning (rekommenderas för stora bibliotek)**  <br>
   Använd appen **Apple Devices** på Windows 11 för att överföra filer direkt till din iPhone via USB.  
   Följ Apples guide här:  
   https://support.apple.com/en-ph/120402 <br>

2. **Trådlöst via Wi-Fi Drive**  <br>
   Aktivera funktionen **WiFi Drive** i appen och ladda upp din musik via en webbläsare på din dator.  
   Steg-för-steg-instruktioner här:  
   [Hur man överför musikfiler från en dator till iPhone utan iTunes med WiFi-Drive](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **Trådlöst med DLNA-server**  <br>
   Slå på DLNA-medieservern på din Windows-dator och strömma eller överför ditt bibliotek direkt till appen.  
   Guide:  
   [Hur man aktiverar DLNA-medieserver på Windows 10 och spelar musik på iPhone](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **Trådlöst med SMB-fildelning**  <br>
   Aktivera **SMB-fildelning** på din dator och anslut till den i appen för att bläddra, ladda ned eller överföra filer mapp för mapp.  
   Instruktioner:  
   [Överföra filer från dator till iPhone med SMB-protokoll](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ Vid överföring av stora bibliotek (10 GB+) är kabelansluten USB-överföring vanligtvis det snabbaste och mest stabila alternativet.

{{% /details %}}

</div>
