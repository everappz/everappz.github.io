---
title: "Hur du ansluter Synology NAS och lyssnar på musik på din iPhone eller Mac"
date: 2024-09-19
description: "Lär dig hur du ansluter din Synology NAS med native API eller QuickConnect och strömmar högkvalitativ musik till din iPhone eller Mac med Evermusic och Flacbox."
keywords: ["synology nas", "strömma musik", "quickconnect", "evermusic synology", "flacbox synology", "nas musikspelare", "iphone nas musik"]
tags: ["musik", "strömning", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Sammanfattning:** Anslut din Synology NAS till Evermusic eller Flacbox med Synologys native API -- antingen manuellt via IP-adress eller automatiskt via QuickConnect ID. QuickConnect låter dig strömma musik på distans utan portvidarebefordran. Båda apparna stöder FLAC, MP3, WAV och andra hi-res-format.

Om du letar efter ett smidigt sätt att ansluta din Synology NAS och njuta av ditt musikbibliotek på din iPhone eller Mac, är Evermusic och Flacbox-apparna de perfekta lösningarna. Dessa appar stöder ett brett utbud av ljudformat, inklusive FLAC, MP3 och WAV, vilket gör det enkelt att strömma och lyssna på högkvalitativ musik direkt från din Synology NAS.

I den här guiden visar vi dig hur du ansluter din Synology NAS till Evermusic eller Flacbox-appen med Synologys native API och QuickConnect-funktion. Genom att utnyttja Synologys direkta API kan du säkert komma åt ditt musikbibliotek utanför ditt hemnätverk utan att behöva komplicerade konfigurationer som WebDAV, SMB, DLNA. Med QuickConnect kan du strömma och hantera din musik var som helst med din iPhone eller Mac.

## Steg 1: Konfigurera behörigheter för delad mapp (valfritt)

1. Öppna **Kontrollpanelen** och gå till avsnittet **Delad mapp**.

![Delad mapp](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Välj mappen **Music** och klicka på **Redigera**.

3. I fliken **Behörigheter** konfigurerar du behörigheterna. Aktivera gäståtkomst med Skrivskyddad om du bara behöver lyssna på musik, eller Läs/Skriv om du behöver ändra filer. Spara ändringarna.

![Behörigheter](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Steg 2: Hitta Synology NAS IP-adress

1. Öppna **Kontrollpanelen** och gå till fliken **Nätverksgränssnitt**.

![Nätverksgränssnitt](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Eller använd din webbläsare för att besöka [find.synology.com](http://find.synology.com).

![Hitta Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Notera IP-adressen för din Synology NAS (t.ex. 192.168.18.137).

## Steg 3: Hitta Synology NAS nätverksportar

Du hittar den officiella Synology-dokumentationen för standard DSM-nätverksportar i denna [Synology Knowledge Center-artikel](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM använder följande standardportar:
- **HTTP (Webbåtkomst):** Port **5000**
- **HTTPS (Säker webbåtkomst):** Port **5001**

Dessa är standardportarna för åtkomst till DSM-gränssnittet.

![Nätverksportar](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Steg 4: Aktivera QuickConnect ID-funktionen

Ett Synology QuickConnect ID är en unik identifierare som låter dig komma åt din Synology NAS på distans via internet utan att behöva konfigurera komplicerade nätverksinställningar som portvidarebefordran. QuickConnect förenklar fjärråtkomst genom att använda Synologys servrar för att upprätta en anslutning mellan din NAS och din enhet, som din smartphone eller dator, via QuickConnect ID.

**Så hittar eller konfigurerar du ditt QuickConnect ID:**

1. **Logga in på DSM.**
2. Gå till **Kontrollpanelen > Extern åtkomst > QuickConnect**.
3. **Aktivera QuickConnect** och skapa eller visa ditt unika QuickConnect ID.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Steg 5: Anslut till Synology NAS på din iPhone/Mac med Evermusic eller Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) och [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) är båda musikspelarappar designade för iOS- och macOS-enheter, var och en med unika funktioner och möjligheter för att hantera och njuta av ditt musikbibliotek.

1. Öppna Evermusic eller Flacbox-appen och gå till fliken **Anslutningar**.

![Anslutningar](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Välj **Anslut en molntjänst** och välj **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Du har två anslutningsalternativ: **manuellt** med serverns IP-adress och port, eller **automatiskt** via QuickConnect ID.

### Manuell anslutning

För den manuella metoden behöver du den direkta IP-adressen och portnumret som du hämtade i tidigare steg.

1. Ange server-URL:en du fick i steg 2, med följande format: PROTOKOLL://IP_ADRESS:PORTNUMMER
   - Använd **port 5000** för HTTP och **port 5001** för HTTPS-anslutningar.

   Till exempel:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Det faktiska portnumret kan bekräftas i steg 3 i din konfiguration.
3. Ange ditt **användarnamn** och **lösenord** för Synology NAS.
4. Tryck på **Logga in** för att upprätta anslutningen.

![Manuell anslutning](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automatisk anslutning

För den automatiska anslutningen använder du **QuickConnect ID** från steg 4. Istället för att manuellt ange IP-adressen och portnumret för din Synology NAS, ange helt enkelt **QuickConnect ID**. Appen hämtar automatiskt nödvändig anslutningsinformation.

Denna metod låter dig komma åt din NAS på distans, även utanför ditt hemnätverk, så att du kan hantera dina filer från internet utan att behöva konfigurera portvidarebefordran eller statiska IP-adresser.

![Automatisk anslutning](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Tvåfaktorsautentisering

Från och med DSM 4.2 introducerade Synology **tvåstegsverifiering** för att förbättra säkerheten. Denna funktion kräver en **engångslösenordskod (OTP)**, genererad av en autentiseringsapp, utöver dina vanliga inloggningsuppgifter. Om du har aktiverat tvåstegsverifiering måste du efter att ha angett användarnamn och lösenord också ange OTP för att logga in på din DSM-session.

Observera att när din session löper ut måste appen omauktoriseras manuellt. För att omauktorisera:

1. Gå till fliken **Anslutningar** i appen.
2. Tryck på knappen **Fler åtgärder** bredvid servernamnet.
3. Välj **Inställningar** från menyn för att ange den nya autentiseringskoden och slutföra omauktoriseringsprocessen.

Detta säkerställer att även om du kommer åt din NAS från ett opålitligt nätverk förblir dina data säkra.

## Steg 6: Navigera och spela musik

1. När du är ansluten visas enheten i listan **Anslutna enheter**.

![Anslutna enheter](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navigera till mappen **Music** och tryck på valfri ljudfil för att starta uppspelning.

![Spela musik](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Steg 7: Lägg till ansluten molnmapp i musikbiblioteket

1. Öppna avsnittet **Musikbibliotek** i appen.
2. Välj **Lägg till musik** och välj **Anslutningar**.
3. Välj din anslutna NAS-server och välj mappen **Music**. Tryck på **Färdig**.
4. Appen skannar musikmappen och lägger till ljudfiler som stöds i musikbiblioteket. Metadata laddas och dina spår grupperas efter album, artist och genre.

## Slutsats

Genom att följa dessa steg kan du enkelt konfigurera en anslutning på din Synology NAS och strömma hela ditt musikbibliotek till din iPhone eller Mac med Evermusic eller Flacbox. Oavsett om du är hemma eller på språng, njut av sömlös högkvalitativ åtkomst till dina favoritlåtar var som helst med QuickConnect. Dra nytta av den flexibilitet och bekvämlighet som dessa appar erbjuder och börja hantera din musiksamling enkelt på alla dina enheter.

Med säker fjärråtkomst genom QuickConnect och stöd för ett brett utbud av ljudformat kommer du aldrig att vara långt från din musik. Nu är dina NAS-lagrade filer bara ett tryck bort!

## FAQ

{{% details title="Vad är skillnaden mellan manuell anslutning och QuickConnect?" closed="true" %}}
Manuell anslutning använder NAS IP-adress och port, som fungerar på ditt lokala nätverk. QuickConnect använder Synologys relätjänst för att upprätta en anslutning var som helst via internet, utan portvidarebefordran.
{{% /details %}}

{{% details title="Kan jag strömma musik från Synology NAS utanför mitt hemnätverk?" closed="true" %}}
Ja. Aktivera QuickConnect på din Synology NAS och använd QuickConnect ID i Evermusic eller Flacbox för att strömma musik var som helst med internetanslutning.
{{% /details %}}

{{% details title="Vilka ljudformat stöds vid strömning från Synology NAS?" closed="true" %}}
Evermusic och Flacbox stöder FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD och många andra format. Alla format som stöds fungerar vid strömning från Synology NAS.
{{% /details %}}

{{% details title="Behöver jag tvåfaktorsautentisering för att ansluta?" closed="true" %}}
Nej, 2FA är valfritt. Om du har aktiverat tvåstegsverifiering på din Synology DSM kommer appen dock att be om ett engångslösenord vid inloggning. Du behöver omauktorisera när sessionen löper ut.
{{% /details %}}

{{% details title="Ska jag använda Synology native API, WebDAV eller SMB för att ansluta?" closed="true" %}}
Synology native API med QuickConnect är det bästa valet för fjärråtkomst. För användning på lokalt nätverk är SMB vanligtvis det snabbaste alternativet. WebDAV fungerar bra för både lokal och fjärråtkomst. Evermusic och Flacbox stöder alla tre protokollen.
{{% /details %}}
