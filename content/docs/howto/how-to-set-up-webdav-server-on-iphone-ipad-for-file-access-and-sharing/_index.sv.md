---
title: "Så konfigurerar du en WebDAV-server på iPhone och iPad för filåtkomst och delning"
description: "Förvandla din iPhone eller iPad till en WebDAV-server med Everdisk och montera den som en nätverksdisk i Mac Finder, Windows File Explorer, Linux, Android eller en annan iPhone över Wi-Fi. Komplett konfiguration, WebDAV-adressen och porten samt steg-för-steg-anslutning för varje enhet."
date: 2026-09-19
tags: ["everdisk", "webdav", "nätverksdisk", "fildelning", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV-server iPhone", "WebDAV-server iPad", "hur man konfigurerar WebDAV på iPhone", "montera iPhone som nätverksdisk", "anslut iPhone WebDAV Mac Finder", "WebDAV Windows File Explorer iPhone", "iphone nätverksdisk Windows", "WebDAV Linux iPhone", "kom åt iPhone-filer från dator", "webdav iphone till iphone", "dela filer iPhone WebDAV", "mappa nätverksenhet iphone", "överför filer iphone webdav", "webdav-adress port iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV förvandlar en mapp till en nätverksdisk som en dator kan öppna i sin vanliga filhanterare. Det körs över samma webbprotokoll som din webbläsare använder, vilket är varför det reser väl mellan Mac, Windows och Linux utan särskilda drivrutiner. Med [Everdisk](/products/everdisk) kan du köra en WebDAV-server på din iPhone eller iPad, så att telefonen dyker upp som en disk du kan bläddra i, kopiera från och kopiera till från nästan vilken dator som helst.

WebDAV är det bästa valet när Windows är med i bilden, eftersom Windows File Explorer ansluter till det rent. Den här guiden täcker konfigurationen och hur du ansluter från en Mac, Windows, Linux, Android och en andra iPhone.

## Vad du behöver

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installerat.
- En dator eller en annan enhet på **samma Wi-Fi-nätverk**.
- Filerna du vill dela, i Everdisks Dokument-mapp eller i mappar du lägger till.

## Konfigurera WebDAV-servern i Everdisk

### Steg 1: Välj vad du vill dela och ställ in åtkomst

Öppna Everdisk, gå till fliken **Delning** och tryck på **Vad du vill dela**. Dokument-mappen delas som standard. Lägg till fler med **Lägg till mapp** och **Lägg till fil**.

Öppna **Inställningar**, sedan **Delning**, sedan **Åtkomst**. Slå på **Filredigering** om du vill att anslutna datorer ska kunna kopiera filer till din telefon och byta namn på eller ta bort dem, eller av för en skrivskyddad disk. Ange en **Inloggning** och ett **Lösenord** här om du vill ha en inloggning, eller lämna dem tomma för gäståtkomst.

### Steg 2: Slå på WebDAV-servern

Gå till **Inställningar**, sedan **Delning**, sedan **Anslutningar**, och slå på **Dator**. Det är WebDAV-servern (den bär WebDAV-taggen).

### Steg 3: Starta delningen och notera adressen

Gå tillbaka till fliken **Delning** och tryck på **Starta**. Avsnittet **Så ansluter du** visar WebDAV-adressen. Den ser ut så här:

```
http://192.168.1.20:8080
```

Numret efter kolonet är **porten**, som är **8080** som standard. Den första delen är din iPhones adress på Wi-Fi, så din blir annorlunda. Håll Everdisk öppet på skärmen medan en enhet är ansluten.

## Anslut från en Mac

1. Öppna **Finder**, välj **Gå**, sedan **Anslut till server** (eller tryck på **Kommando och K**).
2. Skriv WebDAV-adressen som visas i Everdisk, till exempel `http://192.168.1.20:8080`.
3. Klicka på **Anslut**, välj sedan **Gäst** eller ange din **Inloggning** och ditt **Lösenord**.

Din iPhone öppnas i ett Finder-fönster och beter sig som en vanlig mapp. Kopiera filer i vilken riktning som helst om Filredigering är på.

## Anslut från Windows

Windows har en inbyggd WebDAV-klient, så detta fungerar från File Explorer.

1. Öppna **File Explorer**, högerklicka på **Den här datorn** i sidofältet och välj **Lägg till en nätverksplats** (du kan också använda **Anslut nätverksenhet**).
2. När du blir tillfrågad om adressen skriver du samma WebDAV-adress från Everdisk, till exempel `http://192.168.1.20:8080`, och klickar sedan på **Nästa**.
3. Ange din **Inloggning** och ditt **Lösenord** om du angav ett.

Enheten visas sedan under Den här datorn som en nätverksplats du kan öppna och kopiera filer från. Om Windows vägrar ansluta första gången, se till att tjänsten **WebClient** körs (sök efter Tjänster i Start-menyn, hitta WebClient och ställ in den att starta), och försök sedan igen.

## Anslut från Linux

1. Öppna din filhanterare och välj **Connect to Server** eller **Other Locations**.
2. Ange adressen med ett WebDAV-prefix, till exempel `dav://192.168.1.20:8080` (använd `davs://` endast om du ställt in TLS).
3. Anslut som gäst eller ange din inloggning.

## Anslut från Android

Android har ingen inbyggd WebDAV-läsare i systemet, så använd en filhanterare som stöder det:

1. Installera en app som **Solid Explorer** eller **CX File Explorer**.
2. Lägg till en ny **WebDAV**-anslutning.
3. Ange värden och **porten 8080**, välj `http`-schemat och lägg till din inloggning om du angav en.

## Anslut från en annan iPhone eller iPad

iOS-appen Filer inkluderar inte en WebDAV-klient, så använd en av dessa:

- **Everdisks egen flik Enheter.** På den andra enheten öppnar du Everdisk, går till **Enheter**, trycker på **Ny anslutning**, väljer **WebDAV** och anger adressen, till exempel `http://192.168.1.20:8080`. Detta är den enklaste vägen och kräver inget extra.
- **En WebDAV-app** som Documents by Readdle, som kan lägga till en WebDAV-anslutning med samma adress och inloggning.

## Föredrar du en snabb länk framför en disk?

Om du bara behöver hämta en fil snabbt och inte vill montera en disk alls, slå på **Webbläsare**-anslutningen i Inställningar, Delning, Anslutningar. Everdisk ger dig då en webbadress du kan öppna i vilken webbläsare som helst på vilken enhet som helst för att bläddra bland och ladda ner dina filer. Det är det snabbaste sättet att lämna över en fil till en Windows-PC, en Chromebook eller en väns telefon.

## Skrivskyddat eller läsa och skriva

Reglaget **Filredigering** i Inställningar, Delning, Åtkomst avgör detta. På betyder att anslutna datorer kan ladda upp, byta namn och ta bort. Av betyder att disken är skrivskyddad, så andra kan visa och kopiera dina filer men inte ändra dem.

## Så här använder folk detta i verkligheten

- **Kopiera filer till din iPhone från en Windows-PC** genom att mappa den som en nätverksplats och dra dem över.
- **Flytta över foton och dokument till en bärbar dator** med filhanteraren du redan kan, utan kabel och utan iTunes.
- **Redigera ett dokument på plats** från din Mac, öppna det direkt från telefonen och spara tillbaka.
- **Flytta en mapp mellan en iPhone och en iPad** med Everdisks flik Enheter på den mottagande enheten.

## Några tips

- Håll Everdisk öppet medan en enhet är ansluten. Att låsa telefonen länge kan pausa appen.
- På Windows, om anslutningen misslyckas, starta tjänsten WebClient och prova adressen igen.
- WebDAV och SMB monteras båda som nätverksdiskar. Använd WebDAV när Windows är inblandat, och [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) när du vill ha Finder-hastighet och kryptering.
- För snabbast överföringar, håll foto- och videokvaliteten på Original i Inställningar.

## Vanliga frågor

{{% details title="Vad är WebDAV-adressen och porten för min iPhone?" closed="true" %}}
Efter att du startat delningen visar Everdisk adressen på Delning-skärmen. Den ser ut som http://192.168.1.20:8080. 8080 är porten Everdisk använder för WebDAV, och den första delen är din iPhones adress på Wi-Fi, så din blir annorlunda.
{{% /details %}}

{{% details title="Hur ansluter jag till min iPhones WebDAV från Windows?" closed="true" %}}
Öppna File Explorer, högerklicka på Den här datorn och välj Lägg till en nätverksplats eller Anslut nätverksenhet. Ange WebDAV-adressen från Everdisk, till exempel http://192.168.1.20:8080, och ange sedan din inloggning om du angav en. Om Windows inte vill ansluta, se till att tjänsten WebClient körs (sök efter Tjänster, hitta WebClient, starta den) och försök igen.
{{% /details %}}

{{% details title="Kan jag använda WebDAV mellan två iPhones?" closed="true" %}}
Ja, men iOS-appen Filer har ingen WebDAV-klient, så använd Everdisk på den andra enheten. Öppna fliken Enheter, tryck på Ny anslutning, välj WebDAV och ange adressen som visas på den första telefonen. En WebDAV-app som Documents by Readdle fungerar också.
{{% /details %}}

{{% details title="Behöver WebDAV ett lösenord?" closed="true" %}}
Nej, en inloggning är valfri. Lämna Inloggning och Lösenord tomma i Inställningar, Delning, Åtkomst för gäståtkomst, eller ange dem om du vill att anslutningar ska logga in.
{{% /details %}}

{{% details title="Kan andra personer ändra mina filer över WebDAV?" closed="true" %}}
Bara om du tillåter det. Reglaget Filredigering i Inställningar, Delning, Åtkomst styr detta. På låter anslutna enheter ladda upp, byta namn och ta bort. Av gör disken skrivskyddad, så andra kan visa och kopiera men inte ändra något.
{{% /details %}}

{{% details title="WebDAV eller SMB, vad är skillnaden?" closed="true" %}}
Båda monterar din iPhone som en nätverksdisk. WebDAV körs över webbprotokollet och ansluter rent från Windows File Explorer, vilket är dess huvudsakliga styrka. SMB är den inbyggda fildelningen på Mac, Linux och NAS-enheter, är vanligtvis snabbare på en Mac och är den enda Everdisk-anslutningen som kan kryptera överföringar. Everdisk kan köra båda samtidigt.
{{% /details %}}

{{% details title="Varför kopplar min WebDAV-disk från?" closed="true" %}}
Din iPhone är servern, och iOS pausar appar som ligger i bakgrunden för länge. Håll Everdisk öppet på skärmen medan en enhet är ansluten, och anslut till ström under långa överföringar. Bekräfta också att båda enheterna fortfarande är på samma Wi-Fi.
{{% /details %}}

{{% details title="Kan jag ansluta över WebDAV utan Wi-Fi?" closed="true" %}}
Ja, om du ansluter din iPhone till en Mac med en kabel. Everdisk visar då en extra kabelanslutningsadress som den anslutna Mac-datorn kan öppna i Finder, vilket fungerar även utan Wi-Fi alls. På kabeln kan bara den Mac-datorn nå enheten.
{{% /details %}}

{{% details title="Är Everdisk gratis?" closed="true" %}}
Ja, Everdisk är gratis att ladda ner och WebDAV-servern ingår. Ett valfritt engångsköp av Premium lägger till extrafunktioner som anpassade portar och konvertering av foton och video. Du kan konfigurera WebDAV och dela filer utan att betala.
{{% /details %}}

Redo att prova? [Ladda ner Everdisk från App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) och montera din iPhone som en disk på ett par minuter. Frågor eller synpunkter? Mejla oss på **support@everappz.com**.
