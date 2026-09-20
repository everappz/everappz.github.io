---
title: "Så konfigurerar du en FTP-server på iPhone och iPad för filöverföringar"
description: "Förvandla din iPhone eller iPad till en FTP-server med Everdisk och överför filer från en Mac, Windows-PC, Linux, Android, en FTP-app som FileZilla eller en annan iPhone över Wi-Fi. Komplett konfiguration, ftp-adressen och porten, gäståtkomst och steg-för-steg-anslutning för varje enhet."
date: 2026-09-19
tags: ["everdisk", "ftp", "filöverföring", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP-server iPhone", "FTP-server iPad", "hur man konfigurerar FTP på iPhone", "iphone ftp-server-app", "anslut FileZilla till iPhone", "Cyberduck iPhone FTP", "överför filer iPhone FTP", "ftp iphone till dator", "ftp iphone till iphone", "anslut till iPhone FTP från Windows", "ftp-adress port iphone", "anonym ftp iphone", "dela filer iphone ftp", "iphone ftp för kamera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP är den gamla pålitliga inom filöverföring. Det har funnits i decennier, vilket är precis varför det är så användbart: nästan allt som kan tala med en server förstår det. Kameror, smarta TV-apparater, routrar, nätverksdiskar, automatiseringsverktyg och varje FTP-app på skrivbordet talar FTP. Med [Everdisk](/products/everdisk) kan du köra en FTP-server på din iPhone eller iPad, så att telefonen blir en plats dit dessa enheter och appar kan ansluta och flytta filer.

Ta till FTP när de andra alternativen inte passar, till exempel en äldre enhet eller en app som bara kan ansluta över FTP. Den här guiden täcker konfigurationen och hur du ansluter från en Mac, Windows, en FTP-app, Linux, Android och en andra iPhone.

## Vad du behöver

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installerat.
- En dator, app eller enhet på **samma Wi-Fi-nätverk**.
- Filerna du vill dela, i Everdisks Dokument-mapp eller i mappar du lägger till.

## Konfigurera FTP-servern i Everdisk

### Steg 1: Välj vad du vill dela och ställ in åtkomst

Öppna Everdisk, gå till fliken **Delning** och tryck på **Vad du vill dela**. Dokument-mappen delas som standard. Lägg till fler med **Lägg till mapp** och **Lägg till fil**.

Öppna **Inställningar**, sedan **Delning**, sedan **Åtkomst**. Slå på **Filredigering** om du vill att folk ska kunna ladda upp, byta namn och ta bort, eller av för att bara tillåta nedladdningar. Ange en **Inloggning** och ett **Lösenord** om du vill ha en inloggning, eller lämna dem tomma så att vem som helst kan ansluta som gäst.

### Steg 2: Slå på FTP-servern

Gå till **Inställningar**, sedan **Delning**, sedan **Anslutningar**, och slå på **Andra appar och enheter**. Det är FTP-servern (den bär FTP-taggen).

### Steg 3: Starta delningen och notera adressen

Gå tillbaka till fliken **Delning** och tryck på **Starta**. Avsnittet **Så ansluter du** visar FTP-adressen. Den ser ut så här:

```
ftp://192.168.1.20:2121
```

Numret efter kolonet är **porten**, som är **2121** som standard. Den första delen är din iPhones adress på Wi-Fi, så din blir annorlunda. Håll Everdisk öppet på skärmen medan en enhet är ansluten.

## Anslut från en Mac

1. Öppna **Finder**, välj **Gå**, sedan **Anslut till server** (eller tryck på **Kommando och K**).
2. Skriv FTP-adressen som visas i Everdisk, till exempel `ftp://192.168.1.20:2121`.
3. Klicka på **Anslut**, välj sedan **Gäst** eller ange din **Inloggning** och ditt **Lösenord**.

Finder monterar FTP-delningen så att du kan bläddra och kopiera filer till din Mac. Observera att Finder öppnar FTP som skrivskyddat. När du vill ladda upp från en Mac, använd en FTP-app som beskrivs nedan.

## Anslut från Windows

1. Öppna **File Explorer** och klicka på adressfältet högst upp.
2. Skriv FTP-adressen från Everdisk, till exempel `ftp://192.168.1.20:2121`, och tryck på **Enter**.
3. Ange din **Inloggning** och ditt **Lösenord** om du angav ett, eller fortsätt som gäst.

De delade filerna visas i fönstret och du kan kopiera dem till din PC.

## Anslut med en FTP-app (FileZilla, Cyberduck)

För uppladdningar och full kontroll är en FTP-app det bästa verktyget. **FileZilla** och **Cyberduck** är gratis och körs på Windows, Mac och Linux.

1. Öppna appen och skapa en ny anslutning.
2. Ställ in **Host** till din iPhones Wi-Fi-adress, och **Port** till **2121**.
3. För inloggningen anger du din **Inloggning** och ditt **Lösenord**, eller väljer **Anonymous** om du inte angav någon.
4. Anslut, och dra filer i båda riktningarna (uppladdningar kräver att Filredigering är på).

## Anslut från Linux

1. Öppna din filhanterare och välj **Connect to Server** eller **Other Locations**.
2. Ange adressen, till exempel `ftp://192.168.1.20:2121`.
3. Anslut som gäst eller med din inloggning.

Du kan också använda vilken Linux-FTP-klient som helst från terminalen, riktad mot samma värd och port 2121.

## Anslut från Android

Android har ingen inbyggd FTP-läsare i systemet, så använd en app:

1. Installera en FTP-klient som **AndFTP**, **FTPCafe**, eller en filhanterare med FTP-stöd som **Solid Explorer**.
2. Lägg till en anslutning med värden, **porten 2121** och din inloggning eller Anonymous.
3. Bläddra och överför.

## Anslut från en annan iPhone eller iPad

iOS-appen Filer inkluderar inte en FTP-klient, så använd en av dessa på den andra enheten:

- **Everdisks egen flik Enheter.** Öppna Everdisk, gå till **Enheter**, tryck på **Ny anslutning**, välj **FTP** och ange adressen, till exempel `ftp://192.168.1.20:2121`. Detta är den enklaste vägen.
- **En dedikerad FTP-app** för iOS, med samma värd, port 2121 och inloggning.

## Anslut annan utrustning: kameror, TV-apparater, routrar och NAS

Det är här FTP glänser. Många enheter har en inbyggd FTP-klient som kan skicka eller hämta filer:

- **Kameror** som laddar upp foton över FTP kan skicka dem direkt till din iPhone.
- **Smarta TV-apparater, routrar, NAS-lådor och automatiseringsverktyg** som stöder FTP kan ansluta på samma sätt.

Rikta dem mot din iPhones Wi-Fi-adress, port **2121**, och din inloggning (eller Anonymous), med adressen som visas i Everdisk.

## Skrivskyddat eller läsa och skriva

Reglaget **Filredigering** i Inställningar, Delning, Åtkomst styr detta. På låter folk ladda upp, byta namn och ta bort. Av betyder att de bara kan ladda ner. Välj skrivskyddat när du lämnar ut filer och inte vill att något ändras på din telefon.

## Så här använder folk detta i verkligheten

- **Anslut FileZilla till din iPhone** och skjut en hög med filer till telefonen på en gång.
- **Låt en gammal app eller enhet som bara talar FTP** nå dina filer när inget annat vill ansluta.
- **Ta emot foton från en kamera** som laddar upp över FTP.
- **Flytta filer mellan en iPhone och en iPad** med Everdisks flik Enheter på den mottagande enheten.

## Några tips

- Håll Everdisk öppet medan en enhet är ansluten, eftersom iOS pausar bakgrundsappar efter ett tag.
- För att ladda upp från en Mac, använd FileZilla eller Cyberduck snarare än Finder, eftersom Finder öppnar FTP som skrivskyddat.
- Lämna inloggningen tom för bredast kompatibilitet, och anslut sedan som Anonymous, vilket de flesta FTP-klienter erbjuder.
- FTP krypterar inte sin trafik. På ett nätverk du inte litar på, använd [SMB-servern med kryptering](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) i stället.

## Vanliga frågor

{{% details title="Vad är FTP-adressen och porten för min iPhone?" closed="true" %}}
Efter att du startat delningen visar Everdisk adressen på Delning-skärmen. Den ser ut som ftp://192.168.1.20:2121. 2121 är porten Everdisk använder för FTP, och den första delen är din iPhones adress på Wi-Fi, så din blir annorlunda.
{{% /details %}}

{{% details title="Hur ansluter jag FileZilla eller Cyberduck till min iPhone?" closed="true" %}}
Öppna appen och skapa en ny anslutning. Ställ in Host till din iPhones Wi-Fi-adress och Port till 2121. Ange din Inloggning och ditt Lösenord, eller välj Anonymous om du inte angav någon i Everdisk. Anslut, och du kan dra filer i båda riktningarna när Filredigering är på.
{{% /details %}}

{{% details title="Kan jag ansluta till min iPhones FTP från Windows?" closed="true" %}}
Ja. Öppna File Explorer, klicka på adressfältet, skriv FTP-adressen från Everdisk (till exempel ftp://192.168.1.20:2121) och tryck på Enter. Ange din inloggning om du angav en, eller fortsätt som gäst. För uppladdningar och mer kontroll, använd en FTP-app som FileZilla i stället.
{{% /details %}}

{{% details title="Behöver jag en inloggning för FTP?" closed="true" %}}
Nej, en inloggning är valfri. Lämna Inloggning och Lösenord tomma i Inställningar, Delning, Åtkomst, och anslut som Anonymous, vilket de flesta FTP-klienter erbjuder. Ange en inloggning om du vill att anslutningar ska logga in först.
{{% /details %}}

{{% details title="Varför kan jag bara ladda ner och inte ladda upp över FTP?" closed="true" %}}
Två orsaker är vanliga. För det första måste reglaget Filredigering i Inställningar, Delning, Åtkomst vara på för att tillåta uppladdningar, namnbyten och borttagningar. För det andra öppnar Mac Finder FTP som skrivskyddat, så använd en FTP-app som FileZilla eller Cyberduck när du vill ladda upp.
{{% /details %}}

{{% details title="Kan jag använda FTP mellan två iPhones?" closed="true" %}}
Ja. Starta FTP-servern på den första iPhonen. På den andra öppnar du Everdisk, går till fliken Enheter, trycker på Ny anslutning, väljer FTP och anger adressen som visas på den första telefonen. En dedikerad FTP-app för iOS fungerar också, eftersom iOS-appen Filer inte inkluderar en FTP-klient.
{{% /details %}}

{{% details title="Är FTP säkert?" closed="true" %}}
Vanlig FTP krypterar inte sin trafik, så behandla det som ett verktyg för nätverk du litar på, som ditt hemma-Wi-Fi. På ett nätverk du inte kontrollerar, använd SMB-servern med Kräv SMB-kryptering påslaget, vilket skyddar varje överföring.
{{% /details %}}

{{% details title="Vilka enheter kan ansluta över FTP?" closed="true" %}}
Nästan allt med en FTP-klient. Det inkluderar Mac-, Windows- och Linux-datorer, FTP-appar som FileZilla och Cyberduck, Android-filhanterare och hårdvara som kameror, smarta TV-apparater, routrar, NAS-lådor och automatiseringsverktyg. Den breda räckvidden är den främsta anledningen att välja FTP.
{{% /details %}}

{{% details title="Varför tappade min FTP-anslutning?" closed="true" %}}
Din iPhone är servern, och iOS pausar appar som ligger i bakgrunden för länge. Håll Everdisk öppet på skärmen medan en enhet är ansluten, och anslut till ström under långa överföringar. Se också till att båda enheterna fortfarande är på samma Wi-Fi.
{{% /details %}}

{{% details title="Är Everdisk gratis?" closed="true" %}}
Ja, Everdisk är gratis att ladda ner och FTP-servern ingår. Ett valfritt engångsköp av Premium lägger till extrafunktioner som anpassade portar och konvertering av foton och video. Du kan konfigurera FTP och överföra filer utan att betala.
{{% /details %}}

Redo att prova? [Ladda ner Everdisk från App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) och anslut din första FTP-klient på ett par minuter. Frågor eller synpunkter? Mejla oss på **support@everappz.com**.
