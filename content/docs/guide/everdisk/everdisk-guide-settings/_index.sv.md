---
title: "Inställningar"
date: 2026-08-20
description: "En komplett genomgång av Everdisk-inställningarna: enhetsprofil (namn och avatar), de fem anslutningsservrarna, åtkomstkontroller, SMB-kryptering (SMB3/AES), foto- och videokvalitet, anpassade portar, DLNA-miniatyrer, nätverks- och överföringsalternativ, filhanterarens alternativ och Premium."
keywords: ["Everdisk inställningar", "enhetsnamn avatar", "anslutningsservrar", "foto- videokvalitet", "anpassade portar HTTP WebDAV FTP", "DLNA-miniatyrer", "parallella överföringar", "ta bort filer permanent", "miniatyrcache", "Everdisk Premium"]
tags: ["everdisk", "guide", "settings"]
readingTime: 12
---


Fliken **Inställningar** grupperar allt i tre huvudområden - **Delning**, **Nätverk** och **Filhanterare** - plus Premium, feedback och juridiska länkar. Den här sidan förklarar varje inställning och dess standardvärde.

## Premium

Högst upp i Inställningar ser du din Premium-status, eller en knapp för att **Lås upp alla funktioner**. Everdisk är gratis att använda med några begränsningar; ett engångsköp av **Premium Lifetime** tar bort dem. Se [Premium Lifetime](#premium-lifetime) längst ner på den här sidan.

## Delningsinställningar

### Allmänt

- **Starta enhetsdelning automatiskt** - starta delning så snart du öppnar appen. *(Premium.)*
- **Dela Dokument-mappen** - dela appens egen Dokument-mapp. På som standard.
- **Meddela innan frånkoppling** - påminn dig om att öppna appen igen innan systemet pausar den i bakgrunden. Av som standard; ber om aviseringsbehörighet första gången.

### Enhetsprofil

- **Enhetsnamn** - namnet andra enheter ser för dig i nätverket. Tryck för att redigera. *(Premium.)*
- **Enhetsavatar** - ikonen och bakgrundsfärgen för din enhet. Du kan välja en ikon, en bakgrundsgradient eller **välja en avatar från Foton**. *(Premium.)*
- **Generera nytt namn och ny avatar** och **Generera ny avatar** - få ett nytt slumpmässigt namn och/eller en ny avatar. *(Gratis.)*

### Åtkomst

- **Inloggning** och **Lösenord** - kräv en inloggning för anslutningarna Webbläsare, Dator och Andra appar.
- **Filredigering** - låt anslutna enheter ladda upp, byta namn och ta bort. På som standard.
- **Blockerade enheter** - hantera de enheter du har blockerat.

Se [Åtkomst och integritet](/docs/guide/everdisk/everdisk-guide-access) för detaljer.

### Anslutningar

Slå på eller av varje server. Alla fem är på som standard, och var och en har en info-knapp (ⓘ) med anslutningsinstruktioner:

- **TV och mediacenter** (DLNA)
- **Webbläsare** (HTTP)
- **Dator** (WebDAV)
- **Dator (avancerat)** (SMB) - en nätverksdisk för Mac, Windows och Linux; på en Mac dyker den upp av sig själv i Finders sidofält. Den enda anslutningen som kan krypteras.
- **Andra appar och enheter** (FTP)

### Foton

- **Format** - Original eller Mest kompatibel (JPEG).
- **Kvalitet** - Original, Hög, Medel eller Låg.

Allt annat än Original konverterar foton när de delas, vilket är långsammare. Konvertering är en Premium-funktion.

### Videor

- **Format** - Original eller Mest kompatibel (H.264 MP4).
- **Kvalitet** - Original, Hög, Medel eller Låg.

Samma princip som Foton: Original är snabbast och konvertering är Premium. Sänk kvaliteten om en äldre TV inte kan spela upp en video.

### Avancerat

- **HTTP-port** (standard 80), **WebDAV-port** (standard 8080), **SMB-port** (standard 4455), **FTP-port** (standard 2121). DLNA väljer sin port automatiskt. *(Att ändra portar är Premium; gratisanvändare kan se värdena.)*

### SMB-kryptering

- **Kräv SMB-kryptering** - kryptera varje SMB-överföring med **SMB3-kryptering (AES)** så att ingen annan på nätverket kan läsa dina filer. Av som standard. Det kräver att ett **användarnamn och lösenord** anges ovan (krypterade anslutningar kan inte vara anonyma) och en klient som stöder SMB3, till exempel Finder på en modern Mac eller Windows 10 och senare. Ändringar träder i kraft nästa gång du startar delningen. *(Premium.)*

### DLNA-miniatyrer

- **Visa miniatyrer** - publicera förhandsvisningsbilder för TV-apparater. På som standard (gratis).
- Välj vilka storlekar som ska publiceras: **Liten (160px)**, **Medel (640px)**, **Stor (1024px)**, **Extra stor (4096px)**.

## Nätverksinställningar

- **Filöverföringar** - använd endast **Wi-Fi**, eller **Wi-Fi och mobildata**, för nedladdningar och uppladdningar. Standard Wi-Fi.
- **Gräns för parallella överföringar** - hur många överföringar som körs samtidigt. Standard 5.
- **Bakgrundsöverföringar** - håll överföringar igång medan du använder andra skärmar. På som standard.
- **Miniatyrer för filer** - om miniatyrer för filer på andra enheter ska hämtas endast över Wi-Fi eller även mobildata. Standard Wi-Fi.

## Filhanterarinställningar

- **Ta bort filer permanent** - ta bort omedelbart utan papperskorg. Av som standard. Se [Åtkomst och integritet](/docs/guide/everdisk/everdisk-guide-access).
- **Återställ alla notismeddelanden** - ta tillbaka tipsbannrarna du har stängt.
- **Miniatyrcache** - se hur mycket utrymme cachade miniatyrer använder, och **Rensa miniatyrcache**.

## Feedback och juridik

Längst ner kan du **Betygsätt den här appen**, **Skicka feedback**, **Skaffa fler appar** och öppna **Användarvillkor** och **Integritetspolicy**.

## Premium Lifetime

Everdisk är gratis att använda. Ett enda köp av **Premium Lifetime** - en engångsbetalning, inte en prenumeration - låser upp:

- **Obegränsat antal mappar** - dela fler än 5 mappar.
- **Obegränsat antal anslutningar** - spara fler än 10 servrar på fliken Enheter.
- **Foto- och videokonvertering** - dela i vilken kvalitet som helst utöver Original.
- **SMB-kryptering** - skydda SMB-överföringar med SMB3-kryptering (AES).
- **Anpassade portar** - ange dina egna portar för HTTP, WebDAV, SMB och FTP.
- **Automatisk start av delning** - starta delning automatiskt när du öppnar appen.
- **Enhetsanpassning** - ett eget enhetsnamn, en egen avatarikon, bakgrundsgradient eller fotoavatar.

Premium är knutet till ditt Apple ID. Använd **Återställ köp** för att låsa upp det på dina andra enheter som är inloggade med samma Apple ID.

## Nästa steg

- [Delning](/docs/guide/everdisk/everdisk-guide-sharing) - delningsskärmen i detalj.
- [Åtkomst och integritet](/docs/guide/everdisk/everdisk-guide-access) - lösenord, redigering och blockering.
- [Vanliga frågor](/docs/faq/everdisk) - snabba svar på vanliga frågor.
