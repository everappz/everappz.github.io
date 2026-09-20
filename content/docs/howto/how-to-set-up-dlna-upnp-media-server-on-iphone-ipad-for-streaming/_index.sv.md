---
title: "Så konfigurerar du en DLNA/UPnP-mediaserver på iPhone och iPad för strömning"
description: "Förvandla din iPhone eller iPad till en DLNA/UPnP-mediaserver med Everdisk och strömma foton, videor och musik till en smart-TV, spelkonsol, VLC eller Kodi över Wi-Fi. Komplett konfiguration plus hur du ansluter från Samsung-, LG- och Sony-TV-apparater, Windows, Mac, Linux, Android och en annan iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "mediaserver", "strömning", "smart-tv", "iphone", "ipad", "wifi"]
keywords: ["DLNA-server iPhone", "UPnP-server iPad", "hur man konfigurerar DLNA på iPhone", "strömma till smart-TV från iPhone", "DLNA-mediaserver iOS", "strömma videor till TV utan kabel", "spela iPhone-foton på TV", "Samsung TV DLNA iPhone", "LG TV DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA-mediaserver", "UPnP AV-mediaserver iOS", "strömma musik till TV från iPhone", "mediaserver-app för iPhone"]
readingTime: 9
---

{{< author-byline >}}

DLNA (även kallat UPnP AV) är den tysta arbetshästen bakom de flesta smarta TV-apparater. Det är ett gemensamt språk som låter en TV eller mediaspelare hitta ett mediabibliotek på samma Wi-Fi och spela från det, utan att något behöver installeras på TV:n. Om din iPhone eller iPad kan fungera som det biblioteket dyker dina foton, videor och musik upp på storbilden av sig själva.

Den här guiden visar hur du förvandlar din iPhone eller iPad till en DLNA/UPnP-mediaserver med [Everdisk](/products/everdisk), och hur du öppnar det biblioteket från en smart-TV, en spelkonsol, VLC, Kodi, en dator, en Android-telefon och även en annan iPhone. Allt körs över ditt lokala Wi-Fi, så inget laddas upp någonstans.

## Vad du behöver

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installerat.
- En TV, spelare eller dator på **samma Wi-Fi-nätverk** som din enhet.
- De foton, videor eller den musik du vill spela, redan på din iPhone (i appen Bilder, i appen Musik eller i Everdisks Dokument-mapp).

## Konfigurera DLNA-servern i Everdisk

### Steg 1: Välj vad du vill dela

Öppna Everdisk och gå till fliken **Delning**. Tryck på **Vad du vill dela** och välj ditt innehåll:

- Slå på **Tillåt åtkomst till hela fotobiblioteket** för att dela varje album, eller tryck på **Lägg till foton** för att välja några.
- Slå på **Tillåt åtkomst till hela musikbiblioteket** för att dela dina låtar, eller tryck på **Lägg till låtar** för ett urval.
- Lägg till mappar eller filer med **Lägg till mapp** och **Lägg till fil**. Appens egen Dokument-mapp delas som standard.

Du måste ha minst ett objekt valt innan delningen kan börja.

### Steg 2: Slå på TV och mediacenter (DLNA)

Gå till **Inställningar**, sedan **Delning**, sedan **Anslutningar**. Se till att **TV och mediacenter** är på. Den är på som standard och bär DLNA-taggen. Detta är servern som TV-apparater och spelare letar efter.

### Steg 3: Starta delningen

Tillbaka på fliken **Delning**, tryck på den stora **Starta**-knappen. Din enhet är nu en mediaserver på ditt Wi-Fi. Den visas för andra enheter under sitt vänliga namn, det som visas som ditt enhetsnamn i appen (något i stil med ”Speedy-Hare” tills du ändrar det).

DLNA-strömning är alltid öppen, så det finns inget lösenord att ange på TV:n. Håll Everdisk öppet på skärmen medan du tittar, eftersom iOS pausar appar som skjuts helt i bakgrunden.

## Spela på en smart-TV

Detta är det vanligaste fallet, och det tar oftast omkring trettio sekunder.

1. Sätt TV:n på **samma Wi-Fi** som din iPhone.
2. Öppna TV:ns inbyggda mediaspelare. Namnet beror på märket: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** eller **SmartThings** (Samsung), **Content Share** eller **SimplyShare**.
3. Leta efter listan över mediaservrar eller källor. Din enhet visas där med sitt namn.
4. Välj den, bläddra in i dina foton, videor eller din musik och tryck på spela.

Förhandsvisningar dyker upp automatiskt, så att du kan hitta rätt semesteralbum eller film utan att gissa.

### Vilka TV-apparater fungerar

De flesta TV-apparater från **Samsung, LG, Sony BRAVIA, Panasonic (VIERA-firmware), Philips och Hisense** har DLNA inbyggt och fungerar direkt. Det gör även **PlayStation- och Xbox-konsoler och de flesta AV-receivrar**.

Några plattformar utelämnar det: **Roku-TV-apparater, Amazon Fire TV, Vizio SmartCast och vanlig Google TV** utan en tillverkares mediaapp. Om din TV är en av dessa och inte kan hitta din enhet är det oftast anledningen. På sådana TV-apparater installerar du en DLNA-spelarapp som VLC eller Kodi, eller når dina filer via en webbläsare i stället med [WebDAV-konfigurationsguiden](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Vissa märken behöll DLNA fungerande även efter att de tagit bort den officiella DLNA-logotypen, så om det ser ut att saknas kan du leta efter något av mediaspelarnamnen ovan.

## Spela i VLC eller Kodi på Windows, Mac och Linux

VLC och Kodi är gratis, körs på alla skrivbordssystem och talar DLNA väl. De är det pålitliga sättet att öppna ditt Everdisk-bibliotek på en dator.

**VLC (Windows, Mac, Linux):**

1. Öppna VLC.
2. Visa spellistan (på Windows och Linux trycker du på **Ctrl+L**, på Mac öppnar du **Playlist** från Visa-menyn).
3. Öppna **Universal Plug'n'Play** under Local Network i sidofältet.
4. Din enhet visas i listan. Klicka in i den och välj en fil.

**Kodi (Windows, Mac, Linux):**

1. Gå till **Videos**, **Music** eller **Pictures**, sedan **Files**, sedan **Add source** (eller **Browse**).
2. Välj **UPnP devices**.
3. Välj din enhet och bläddra i ditt bibliotek.

På Windows kan du också öppna **Windows Media Player**, expandera **Other Libraries** i sidofältet, och din enhet visas där.

## Spela på Android

Android-telefoner och -surfplattor har ingen inbyggd DLNA-läsare i systemet, så använd en app:

- **VLC för Android**: öppna sidomenyn, tryck på **Local Network**, och din enhet visas under UPnP-servrar.
- **BubbleUPnP** eller en liknande UPnP-app: din enhet dyker upp i serverlistan, och dessa appar kan också skicka uppspelning till en TV.

## Spela på en annan iPhone eller iPad

Två enheter, ett bibliotek. Säg att fotona finns på din iPhone och att du vill titta på dem på din iPad.

- Den enklaste vägen är Everdisks egen flik **Enheter** på den andra enheten. Den fungerar som en DLNA-klient såväl som en server. Öppna Everdisk på din iPad, gå till **Enheter**, och din iPhone visas under **Tillgängliga enheter**. Tryck på den för att bläddra och spela.
- Vilken DLNA-spelarapp för iOS som helst fungerar också, till exempel VLC eller en UPnP-läsare. Öppna dess lokala nätverksvy och välj din iPhone.

## Spela på en spelkonsol

- **PlayStation 5 och 4**: öppna appen **Media** (Media Gallery), och din enhet visas som en mediaserver du kan bläddra i.
- **Xbox**: använd en mediaspelarapp som stöder DLNA och välj sedan din enhet från serverlistan.

## Om din enhet inte visas i listan

Vissa spelare låter dig lägga till en mediaserver via adress i stället för att vänta på att den ska upptäckas. På Everdisks **Delning**-skärm visar DLNA-kortet en enhetsbeskrivningsadress som slutar på `/device-desc.xml`. Ange den adressen i spelarens fält för att lägga till server.

Om den ändå inte visas, kontrollera tre saker: att båda enheterna är på samma Wi-Fi (inte ett gästnätverk som blockerar trafik mellan enheter), att Everdisk är öppet och delningen startad, och att **TV och mediacenter** är på i Inställningar.

## Om en video inte vill spelas

DLNA lämnar filen som den är till TV:n, och TV:n måste kunna avkoda den. Om ett klipp vägrar spelas är dess format förmodligen inte stött av den TV:n. Två lösningar:

- Öppna **Inställningar**, sedan **Delning**, sedan **Videor**, och sänk **Kvalitet**. Everdisk konverterar då videon till ett mer kompatibelt format medan den strömmar. (Konvertering är en Premium-funktion.)
- Eller öppna samma fil i en webbläsare med Everdisks webbläsarlänk, som är mer förlåtande med format.

## Så här använder folk detta i verkligheten

- **Familjefilmkväll.** Videor filmade på din telefon spelas på vardagsrummets TV utan en kabel eller en Apple TV.
- **Semesterfoton på storbild.** Öppna ditt fotobibliotek på TV:n och svep genom resan med alla i rummet.
- **Bakgrundsmusik på en fest.** Rikta en DLNA-högtalare eller AV-receiver mot ditt musikbibliotek och låt det spela.
- **Titta på en hotell-TV** som har en mediaspelare, när båda enheterna är på rummets Wi-Fi.

## Några tips

- Håll Everdisk öppet medan du strömmar. Om du låser telefonen länge kan iOS pausa appen och uppspelningen stannar.
- Anslut telefonen till ström under långa filmpass.
- För snabbast strömning, håll **Format** och **Kvalitet** på **Original** i Inställningar, och sänk dem bara om en specifik TV har problem med en fil.
- DLNA är endast strömning. Ingen på TV-sidan kan ändra eller ta bort dina filer. För tvåvägs filöverföring, använd [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)-, [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/)- eller [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/)-servern i stället.

## Vanliga frågor

{{% details title="Vad är skillnaden mellan DLNA och UPnP?" closed="true" %}}
De är nära besläktade. UPnP är den underliggande nätverksstandarden, och DLNA är mediaprofilen byggd ovanpå den som TV-apparater och spelare använder för att dela och spela foton, videor och musik. I vardagligt bruk är orden utbytbara. När du slår på TV och mediacenter i Everdisk blir din enhet en DLNA/UPnP-mediaserver som vilken DLNA-klient som helst kan bläddra i.
{{% /details %}}

{{% details title="Behöver jag installera något på min TV?" closed="true" %}}
Nej. Om din TV stöder DLNA har den redan en mediaspelare som kan hitta din enhet på Wi-Fi. Du installerar bara Everdisk på den iPhone eller iPad som innehåller innehållet. Om din TV inte stöder DLNA, installera en spelare som VLC eller Kodi på en enhet som är ansluten till den.
{{% /details %}}

{{% details title="Varför visas inte min iPhone på TV:n?" closed="true" %}}
Kontrollera att båda enheterna är på samma Wi-Fi-nätverk. Gästnätverk och vissa kontors- eller hotellnätverk hindrar enheter från att se varandra, vilket stoppar DLNA. Bekräfta sedan att Everdisk är öppet med delningen startad, och att TV och mediacenter är på i Inställningar, Delning, Anslutningar. Om TV:n ändå inte kan hitta den, lägg till servern för hand med enhetsbeskrivningsadressen som slutar på /device-desc.xml.
{{% /details %}}

{{% details title="Behöver DLNA-strömning ett lösenord?" closed="true" %}}
Nej. DLNA är alltid öppen för alla på samma Wi-Fi medan det är på, vilket är varför det inte finns någon inloggning på TV-sidan. Det är bra på ett hemmanätverk du litar på. På ett nätverk du inte litar på, stäng av TV och mediacenter när du är klar, eller använd SMB-servern med kryptering i stället.
{{% /details %}}

{{% details title="Kan jag strömma till en Chromecast eller Roku?" closed="true" %}}
Chromecast och Roku fungerar inte som DLNA-spelare direkt, så de hittar inte din enhet direkt. Lösningen är att installera en DLNA-app som kan casta, som VLC eller BubbleUPnP på en telefon, och skicka uppspelning till Chromecast eller Roku därifrån. På de flesta andra smarta TV-apparater fungerar DLNA utan något av detta.
{{% /details %}}

{{% details title="En video spelas utan ljud eller vill inte öppnas. Vad kan jag göra?" closed="true" %}}
Det är ett format som TV:n inte kan avkoda. Öppna Inställningar, Delning, Videor i Everdisk och sänk Kvalitet så att appen konverterar videon till ett mer kompatibelt format medan den strömmar. Du kan också öppna samma fil via webbläsarlänken, som hanterar fler format.
{{% /details %}}

{{% details title="Kan jag strömma musik, inte bara video?" closed="true" %}}
Ja. Slå på Tillåt åtkomst till hela musikbiblioteket, eller lägg till specifika låtar, och starta sedan delningen. Dina låtar visas på vilken DLNA-högtalare, AV-receiver eller TV som helst, med omslag och spårdetaljer. Musik delas alltid i sin originalkvalitet.
{{% /details %}}

{{% details title="Måste appen förbli öppen medan jag tittar?" closed="true" %}}
Ja. Din iPhone fungerar som servern, och iOS pausar appar som skjuts helt i bakgrunden under lång tid. Håll Everdisk på skärmen medan du strömmar, och anslut till ström under långa pass.
{{% /details %}}

{{% details title="Hur strömmar jag från en iPhone till en annan iPad?" closed="true" %}}
Starta delningen på din iPhone, öppna sedan Everdisk på din iPad och gå till fliken Enheter. Din iPhone visas under Tillgängliga enheter som en mediaserver. Tryck på den för att bläddra och spela. Everdisk fungerar som en DLNA-klient och en server, så du behöver ingen annan app.
{{% /details %}}

{{% details title="Är Everdisk gratis?" closed="true" %}}
Ja, Everdisk är gratis att ladda ner och DLNA-mediaservern ingår. Ett valfritt engångsköp av Premium Lifetime lägger till extrafunktioner som konvertering av foton och video för äldre TV-apparater, anpassade portar med mera. Du kan konfigurera och använda DLNA-strömning utan att betala.
{{% /details %}}

Redo att prova? [Ladda ner Everdisk från App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) och strömma ditt första album till TV:n på ett par minuter. Frågor eller synpunkter? Mejla oss på **support@everappz.com**.
