---
title: "Så konfigurerar du en SMB-server på iPhone och iPad för fildelning"
description: "Förvandla din iPhone eller iPad till en SMB-filserver med Everdisk och öppna den som en nätverksdisk från en Mac, en annan iPhone, Linux eller Android över Wi-Fi. Komplett konfiguration, smb-adressen och porten, valfri SMB3-kryptering och steg-för-steg-anslutning för varje enhet."
date: 2026-09-19
tags: ["everdisk", "smb", "fildelning", "nätverksdisk", "iphone", "ipad", "mac", "finder", "kryptering", "wifi"]
keywords: ["SMB-server iPhone", "SMB-server iPad", "hur man konfigurerar SMB på iPhone", "iPhone SMB-delning", "anslut iPhone SMB Mac Finder", "smb iphone till iphone", "iOS Filer-app anslut till server SMB", "dela filer iPhone SMB", "iphone nätverksdisk Finder", "SMB3-kryptering iOS", "smb-delning iPhone Android", "anslut till SMB från Linux", "iphone som nätverksdisk", "dela filer mellan iphones wifi", "mappa iphone som nätverksdisk"]
readingTime: 10
---

{{< author-byline >}}

SMB är fildelningen som är inbyggd i macOS, Windows och Linux, och i nästan varje nätverksdisk (NAS). När du ansluter till en delad mapp på en annan dator och den öppnas som en vanlig disk i Finder eller File Explorer, är det SMB som gör jobbet. Med [Everdisk](/products/everdisk) kan du lägga en SMB-delning på din iPhone eller iPad, så att telefonen själv dyker upp som en nätverksdisk som andra enheter bläddrar i, kopierar från och kopierar till.

Detta är alternativet att välja när du vill att din iPhone ska bete sig som en riktig disk, inte en webbsida. Det är snabbt, det drar och släpper åt båda hållen, och det är den enda anslutningstypen i Everdisk som kan kryptera varje överföring. Den här guiden täcker konfigurationen och hur du ansluter från en Mac, en annan iPhone eller iPad, Linux, Android och Windows.

## Vad du behöver

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installerat.
- En annan enhet på **samma Wi-Fi-nätverk**.
- Filerna du vill dela, i Everdisks Dokument-mapp eller i mappar du lägger till.

## Konfigurera SMB-servern i Everdisk

### Steg 1: Välj vad du vill dela och vem som kan skriva

Öppna Everdisk, gå till fliken **Delning** och tryck på **Vad du vill dela**. Dokument-mappen delas som standard. Lägg till fler med **Lägg till mapp** och **Lägg till fil**, och slå på ditt foto- eller musikbibliotek om du vill ha dem tillgängliga också.

Bestäm om andra enheter bara kan läsa dina filer, eller också ändra dem. Öppna **Inställningar**, sedan **Delning**, sedan **Åtkomst**, och ställ in **Filredigering**. Med den på kan anslutna enheter kopiera filer till din telefon och byta namn på eller ta bort dem. Med den av är delningen skrivskyddad.

Om du vill ha en inloggning, ange en **Inloggning** och ett **Lösenord** på samma Åtkomst-skärm. Lämna båda tomma för att tillåta gäståtkomst.

### Steg 2: Slå på SMB-servern

Gå till **Inställningar**, sedan **Delning**, sedan **Anslutningar**, och slå på **Dator (avancerat)**. Det är SMB-servern (den bär SMB-taggen).

### Steg 3: Starta delningen och notera adressen

Gå tillbaka till fliken **Delning** och tryck på **Starta**. Avsnittet **Så ansluter du** visar nu SMB-adressen. Den ser ut så här:

```
smb://192.168.1.20:4455/Share
```

Tre saker att veta om den adressen:

- Numret efter kolonet är **porten**. Everdisk använder **4455** som standard.
- Delningen heter **Share**.
- Den första delen är din iPhones adress på Wi-Fi, så den blir annorlunda på ditt nätverk.

Håll Everdisk öppet medan enheter är anslutna, eftersom iOS pausar appar som ligger i bakgrunden för länge.

## Anslut från en Mac

Detta är det smidigaste fallet, eftersom macOS talar SMB inbyggt.

Det snabbaste sättet: öppna **Finder** och titta i sidofältet under **Platser** eller **Nätverk**. Everdisk annonserar sig på Wi-Fi, så din iPhone dyker ofta upp där av sig själv. Klicka på den, klicka sedan på **Anslut som** och välj **Gäst**, eller ange din inloggning.

För att ansluta för hand:

1. I Finder väljer du **Gå**, sedan **Anslut till server** (eller trycker på **Kommando och K**).
2. Skriv SMB-adressen som visas i Everdisk, till exempel `smb://192.168.1.20:4455/Share`.
3. Klicka på **Anslut**, välj sedan **Gäst** eller ange din **Inloggning** och ditt **Lösenord**.

Din iPhone öppnas i ett Finder-fönster. Kopiera filer in eller ut genom att dra, precis som med vilken annan disk som helst (om Filredigering är på).

## Anslut från en annan iPhone eller iPad

iOS och iPadOS kan öppna SMB-delningar i den inbyggda appen **Filer**, vilket gör överföringar mellan telefoner rena och snabba.

På den andra enheten:

1. Öppna appen **Filer**.
2. Tryck på **fler**-knappen (de tre punkterna, uppe till höger på iPhone) och välj **Anslut till server**.
3. Ange SMB-adressen från Everdisk, till exempel `smb://192.168.1.20:4455/Share`.
4. Välj **Gäst**, eller **Registrerad användare** och ange din inloggning.
5. Delningen visas under Platser i Filer. Bläddra och kopiera i vilken riktning som helst.

Du kan också använda Everdisks egen flik **Enheter** på den andra enheten, som innehåller en SMB-klient. Öppna Everdisk, gå till **Enheter**, tryck på **Ny anslutning**, välj **SMB** och ange adressen.

## Anslut från Linux

1. Öppna din filhanterare (Files/Nautilus på GNOME, Dolphin på KDE).
2. Välj **Other Locations** eller **Connect to Server**.
3. Ange adressen, till exempel `smb://192.168.1.20:4455/Share`.
4. Anslut som gäst, eller ange din inloggning.

Från en terminal kan du också köra `smbclient //192.168.1.20/Share -p 4455` och ange din inloggning när du blir tillfrågad.

## Anslut från Android

Android har ingen inbyggd SMB-läsare i systemet, så använd en filhanterare som stöder SMB:

1. Installera en app som **CX File Explorer**, **Solid Explorer** eller **X-plore File Manager**.
2. Lägg till en ny **SMB**- eller **LAN**-anslutning.
3. Ange värden (din iPhones Wi-Fi-adress), ställ in **porten på 4455** och delningsnamnet **Share**.
4. Anslut som gäst eller med din inloggning, bläddra sedan och kopiera.

## Anslut från Windows

Windows kan läsa SMB-delningar, med en hake som är värd att känna till på förhand. Den inbyggda File Explorer talar bara med SMB på standardporten och låter dig inte skriva en anpassad port i sökvägen, och Everdisk använder porten 4455. Så den enkla vägen via **Anslut nätverksenhet** når det ofta inte.

Du har två bra alternativ på Windows:

- Använd en filhanterare eller SMB-klient som låter dig ställa in en anpassad port, och rikta den mot din iPhones adress med porten **4455** och delningsnamnet **Share**.
- Eller anslut från Windows med en av Everdisks andra servrar i stället. [WebDAV-konfigurationen](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) och [FTP-konfigurationen](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) fungerar båda bra från Windows File Explorer, och webbläsarlänken fungerar i vilken webbläsare som helst.

Om du ändå vill prova Anslut nätverksenhet: öppna **File Explorer**, högerklicka på **Den här datorn**, välj **Anslut nätverksenhet** och ange värden och delningsnamnet som visas i Everdisk. Om det inte kan ansluta är det portbegränsningen ovan, så byt till WebDAV eller FTP.

## Slå på kryptering för Wi-Fi du inte litar på

SMB är den enda Everdisk-anslutningen som kan kryptera varje överföring, vilket spelar roll på Wi-Fi du inte helt kontrollerar, som ett kafé eller ett kontorsnätverk.

1. I **Inställningar**, **Delning**, **Åtkomst**, ange en **Inloggning** och ett **Lösenord**. Krypterade anslutningar kan inte vara anonyma, så detta steg krävs.
2. I **Inställningar**, **Delning**, slå på **Kräv SMB-kryptering**.
3. Stoppa och starta delningen igen så att ändringen träder i kraft.

Varje SMB-överföring skyddas då med **SMB3-kryptering (AES)**. Den anslutande enheten behöver stödja SMB3, vilket Finder på en modern Mac och Windows 10 eller senare båda gör. SMB-kryptering ingår i engångsköpet av Premium.

## Skrivskyddat eller läsa och skriva

Reglaget **Filredigering** i Inställningar, Delning, Åtkomst styr detta för varje server, inklusive SMB. Slå på det och anslutna enheter kan ladda upp, byta namn och ta bort. Slå av det och de kan bara bläddra och kopiera filer från din telefon. Välj skrivskyddat när du lämnar över filer till någon du inte vill ska ändra något.

## Så här använder folk detta i verkligheten

- **Flytta en stor mapp till din iPhone från en Mac** genom att dra den till Finder-fönstret, snabbare än en webbuppladdning.
- **Hämta en dags foton och videor från din telefon** till en bärbar dator utan iTunes eller en kabel.
- **Skicka filer mellan två iPhones** via appen Filer, utan en tredje app på någon sida.
- **Arbeta med en fil på plats**, öppna ett dokument direkt från telefonen i en app på din Mac och spara tillbaka det.

## Några tips

- Håll Everdisk öppet medan en enhet är ansluten. Att låsa telefonen länge kan pausa appen och tappa anslutningen.
- Om en Mac inte kan se telefonen i Finders sidofält, anslut för hand med Anslut till server och den fullständiga smb-adressen.
- För bästa hastighet vid stora överföringar, håll foto- och videokvaliteten på Original i Inställningar.
- På ett nätverk du inte litar på, slå på Kräv SMB-kryptering och stäng av de andra servrarna medan du arbetar.

## Vanliga frågor

{{% details title="Vad är SMB-adressen och porten för min iPhone?" closed="true" %}}
Efter att du startat delningen visar Everdisk adressen på Delning-skärmen. Den ser ut som smb://192.168.1.20:4455/Share. 4455 är porten Everdisk använder för SMB, och Share är namnet på den delade mappen. Den första delen är din iPhones adress på Wi-Fi, så din blir annorlunda.
{{% /details %}}

{{% details title="Kan jag ansluta till min iPhones SMB-delning från Windows?" closed="true" %}}
Windows File Explorer ansluter bara till SMB på standardporten och accepterar inte en anpassad port i sökvägen, medan Everdisk använder porten 4455. Så den enkla vägen via Anslut nätverksenhet når det ofta inte. Använd en filhanterare som låter dig ställa in en anpassad port, eller anslut från Windows med WebDAV, FTP eller webbläsarlänken i stället. Alla dessa fungerar från Windows utan portproblem.
{{% /details %}}

{{% details title="Hur delar jag filer mellan två iPhones med SMB?" closed="true" %}}
Starta SMB-servern på den första iPhonen i Everdisk. På den andra iPhonen öppnar du appen Filer, trycker på fler-knappen, väljer Anslut till server och anger smb-adressen som visas i Everdisk (till exempel smb://192.168.1.20:4455/Share). Anslut som Gäst eller med din inloggning, och delningen visas i Filer. Du kan också använda Everdisks egen flik Enheter på den andra telefonen.
{{% /details %}}

{{% details title="Visas min iPhone automatiskt i Mac Finders sidofält?" closed="true" %}}
Vanligtvis ja. Everdisk annonserar SMB-delningen på ditt Wi-Fi, så din iPhone dyker ofta upp under Platser eller Nätverk i Finders sidofält. Klicka på den och välj Anslut som, sedan Gäst eller din inloggning. Om den inte visas, anslut för hand med Gå, Anslut till server och den fullständiga smb-adressen.
{{% /details %}}

{{% details title="Behöver jag ett lösenord för att använda SMB?" closed="true" %}}
Nej, en inloggning är valfri. Lämna Inloggning och Lösenord tomma i Inställningar, Delning, Åtkomst för att tillåta gäståtkomst. Ange dem om du vill att anslutningar ska logga in. En inloggning och ett lösenord krävs bara om du slår på Kräv SMB-kryptering, eftersom krypterade anslutningar inte kan vara anonyma.
{{% /details %}}

{{% details title="Är SMB-anslutningen krypterad?" closed="true" %}}
Den kan vara det. SMB är den enda Everdisk-anslutningen som stöder kryptering. Ange en inloggning och ett lösenord, slå sedan på Kräv SMB-kryptering i Inställningar, Delning. Varje överföring skyddas då med SMB3 (AES). Den andra enheten behöver stödja SMB3, vilket moderna Mac-datorer och Windows 10 eller senare gör. Kryptering är en Premium-funktion.
{{% /details %}}

{{% details title="Kan folk ändra eller ta bort mina filer över SMB?" closed="true" %}}
Bara om du tillåter det. Reglaget Filredigering i Inställningar, Delning, Åtkomst styr detta. Med det på kan anslutna enheter ladda upp, byta namn och ta bort. Med det av är delningen skrivskyddad och andra kan bläddra och kopiera filer från din telefon men inte ändra något.
{{% /details %}}

{{% details title="Varför tappade min SMB-anslutning?" closed="true" %}}
Din iPhone är servern, och iOS pausar appar som ligger i bakgrunden för länge. Håll Everdisk öppet på skärmen medan en enhet är ansluten, och anslut telefonen till ström under långa överföringar. Se också till att båda enheterna förblev på samma Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV eller FTP, vilken ska jag använda?" closed="true" %}}
Använd SMB när du vill att telefonen ska bete sig som en riktig nätverksdisk på en Mac, en annan iPhone, Linux eller en NAS, och när du vill ha kryptering. Använd WebDAV när du vill ha en nätverksdisk som också fungerar bra från Windows. Använd FTP för bredast kompatibilitet med äldre enheter och appar. Everdisk kan köra alla samtidigt, så du är inte låst till en.
{{% /details %}}

{{% details title="Är Everdisk gratis?" closed="true" %}}
Ja, Everdisk är gratis att ladda ner och SMB-servern ingår. Det valfria engångsköpet av Premium lägger till SMB-kryptering, anpassade portar och några andra extrafunktioner. Du kan konfigurera SMB och dela filer utan att betala.
{{% /details %}}

Redo att prova? [Ladda ner Everdisk från App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) och öppna din iPhone i Finder på ungefär en minut. Frågor eller synpunkter? Mejla oss på **support@everappz.com**.
