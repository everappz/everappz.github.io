---
title: "Hur du ansluter NAS-lagring via WebDAV och lyssnar på musik på din iPhone eller Mac"
date: 2024-07-28
description: "Lär dig hur du konfigurerar WebDAV på din Synology NAS och strömmar musik till din iPhone eller Mac med Evermusic eller Flacbox. Följ vår steg-för-steg-guide."
keywords: ["anslut nas", "webdav synology", "strömma musik nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["musik", "strömning", "lagring", "nas", "anslut", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Sammanfattning:** Installera och aktivera WebDAV på din Synology NAS, konfigurera behörigheter för delad mapp och anslut sedan från Evermusic eller Flacbox med NAS IP-adressen och WebDAV-porten (standard 5005/5006). Du kan strömma och hantera hela ditt musikbibliotek utan att kopiera filer till din enhet.

Upptäck hur du ansluter din NAS-lagring via WebDAV och enkelt strömmar ditt musikbibliotek till din iPhone eller Mac. WebDAV (Web-based Distributed Authoring and Versioning) är ett protokoll som låter dig hantera och dela filer över Internet. Genom att konfigurera WebDAV på din NAS kan du komma åt och strömma din musiksamling, så att dina favoritlåtar alltid finns till hands.

I den här guiden visar vi dig hur du konfigurerar en WebDAV-anslutning på en av de mest populära NAS-servrarna, Synology NAS. Följ våra enkla steg för att konfigurera WebDAV på din Synology NAS, och du kan bläddra, strömma och hantera ditt musikbibliotek direkt från din iPhone eller Mac.

## Steg 1: Installera WebDAV på Synology NAS

1. Logga in på din Synology NAS och öppna **Paketcenter**.
2. Sök efter "webdav" och installera WebDAV-paketet om det inte redan är installerat. Öppna WebDAV-servern för att konfigurera den.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Installera WebDAV på Synology" width="600" >}}

## Steg 2: Konfigurera WebDAV-servern

1. På WebDAV-inställningssidan, markera rutorna för **Aktivera HTTP**, **Aktivera HTTPS**, **Aktivera anonym WebDAV** och **Aktivera DavDepthInfinity**.
2. Klicka på **Tillämpa** för att spara ändringarna. Notera portnumren för HTTP- och HTTPS-anslutningar, som är 5005 och 5006 som standard.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfigurera WebDAV-inställningar" width="600" >}}

## Steg 3: Konfigurera behörigheter för delad mapp

1. Öppna **Kontrollpanelen** och gå till avsnittet **Delad mapp**.
2. Välj mappen **Musik** och klicka på **Redigera**.
3. I fliken **Behörigheter**, konfigurera behörigheterna. Aktivera gäståtkomst med Skrivskyddad om du bara behöver lyssna på musik, eller Läs/Skriv om du behöver ändra filer. Spara ändringarna.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Behörigheter för delad mapp" width="600" >}}

## Steg 4: Hitta IP-adressen för Synology NAS

1. Öppna **Kontrollpanelen** och gå till fliken **Nätverksgränssnitt**, eller använd din webbläsare för att besöka [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Hitta NAS IP-adress" width="600" >}}

2. Notera IP-adressen för din Synology NAS (t.ex. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP-adress" width="600" >}}

## Steg 5: Anslut till Synology NAS med Evermusic/Flacbox

1. Öppna Evermusic- eller Flacbox-appen och gå till fliken **Anslutningar**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Fliken Anslutningar i Evermusic" width="600" >}}

2. För automatisk anslutning, hitta din Synology NAS i avsnittet **Tillgängliga enheter** och tryck för att ansluta.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Lista över tillgängliga enheter" width="600" >}}

3. För manuell anslutning, välj **Anslut en molntjänst** och välj **WebDAV**. Ange serveradressen i formatet: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (t.ex. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Manuell WebDAV-konfiguration" width="600" >}}

4. Lämna inloggnings- och lösenordsfälten tomma för gäståtkomst, eller ange dina Synology-inloggningsuppgifter. Tryck på **Logga in**.

## Steg 6: Navigera och spela musik

1. När du är ansluten visas enheten i listan **Anslutna tillbehör**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Anslutna enheter i Evermusic" width="600" >}}

2. Navigera till mappen **Musik** och tryck på en ljudfil för att starta uppspelning.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Bläddra i musikmappen" width="600" >}}

## Steg 7: Lägg till ansluten molnmapp i musikbiblioteket

1. Öppna avsnittet **Musikbibliotek** i appen.
2. Välj **Lägg till musik** och välj **Anslutningar**.
3. Välj din anslutna NAS-server och välj mappen **Musik**. Tryck på **Färdig**.
4. Appen skannar musikmappen och lägger till stödda ljudfiler i musikbiblioteket. Metadata laddas och dina spår grupperas efter album, artist och genre.

## Slutsats

Genom att följa dessa steg kan du enkelt konfigurera en WebDAV-anslutning på din Synology NAS och strömma ditt musikbibliotek till din iPhone eller Mac med Evermusic eller Flacbox. Njut av sömlös åtkomst till dina favoritlåtar när som helst.

## Vanliga frågor

{{% details title="Vilka NAS-enheter stöder WebDAV?" closed="true" %}}
De flesta populära NAS-märken stöder WebDAV, inklusive Synology, QNAP, TrueNAS och Western Digital. Kontrollera din NAS-tillverkares dokumentation för instruktioner om WebDAV-konfiguration.
{{% /details %}}

{{% details title="Vad är skillnaden mellan WebDAV och SMB för musikströmning från NAS?" closed="true" %}}
WebDAV fungerar via HTTP/HTTPS och är bättre lämpad för fjärråtkomst via internet. SMB är vanligtvis snabbare på lokala nätverk. Evermusic och Flacbox stöder båda protokollen, så välj baserat på om du behöver lokal eller fjärråtkomst.
{{% /details %}}

{{% details title="Behöver jag användarnamn och lösenord för WebDAV på Synology?" closed="true" %}}
Nej, om du aktiverar anonym WebDAV-åtkomst och konfigurerar gästbehörigheter på din delade mapp. För bättre säkerhet kan du använda dina Synology-inloggningsuppgifter istället.
{{% /details %}}

{{% details title="Kan jag strömma FLAC och andra hi-res-format från NAS via WebDAV?" closed="true" %}}
Ja. Både Evermusic och Flacbox stöder FLAC, ALAC, WAV, DSD och andra högupplösta format vid strömning från NAS-lagring via WebDAV.
{{% /details %}}

{{% details title="Varför kan appen inte hitta min NAS i Tillgängliga enheter?" closed="true" %}}
Se till att din iPhone/Mac och NAS är på samma Wi-Fi-nätverk. Om automatisk upptäckt inte fungerar, använd det manuella anslutningsalternativet och ange NAS IP-adressen och WebDAV-porten direkt.
{{% /details %}}
