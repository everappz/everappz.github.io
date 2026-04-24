---
title: "Streama din musik från Mac eller PC till iPhone med SMB"
description: "Lär dig hur du streamar din musiksamling från Mac eller Windows PC till din iPhone eller iPad med Evermusic och SMB-protokollet. En enkel steg-för-steg-guide för att ansluta och njuta av ljud utan synkronisering."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["streama musik från Mac till iPhone", "SMB ljudstreaming iOS", "Evermusic SMB inställning", "anslut PC musik iPhone", "Mac musikdelning iOS", "SMB Windows filstreaming", "Evermusic PC mappåtkomst"]
---

{{< author-byline >}}


**Sammanfattning:** Använd Evermusic-appen för iPhone eller iPad för att streama musik från din Mac eller Windows PC via ditt lokala nätverk med SMB. Ingen synkronisering, ingen kopiering -- aktivera bara fildelning på din dator, anslut i appen och spela. Installationen tar under 5 minuter.

Drunknar du i ett hav av musik på din MAC eller PC och vill njuta av den problemfritt på din iPhone eller iPad? Leta inte längre än Evermusic. Med Evermusic är det otroligt enkelt att ansluta din dator med SMB-protokollet och streama dina favoritlåtar utan att oroa dig för att ta upp extra lagringsutrymme eller hantera synkroniseringsproblem. Här är en steg-för-steg-guide för att komma igång:

## Steg 1: Aktivera SMB-protokollet på din dator

![Evermusic - SMB-stöd - Mac delningsskärm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Om du använder MAC

- Öppna Systeminställningar -> Delning.
- Aktivera tjänsten Fildelning.
- I avsnittet "Delade mappar" lägger du till din musikmapp, väljer en användare och ställer in behörighetsnivåer (Läs och skriv eller Enbart läsning).
- För extra bekvämlighet kan du välja "Alla: Enbart läsning" för musikmappen, vilket gör den lättillgänglig i Evermusic.
- Glöm inte att komma ihåg din dators URL (smb://192.168.xx.xx) för nästa steg.

![Evermusic - SMB-stöd - Fildelningsskärm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Tryck på "Alternativ" och aktivera "Dela filer och mappar med SMB."
- Aktivera "Windows fildelning" för tillgängliga konton.

![Evermusic - SMB-stöd - Dela filer och mappar skärm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Om du använder en Windows PC

![Evermusic - SMB-stöd - Dela filer på Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Högerklicka på din musikmapp.
- Välj "Egenskaper."
- Öppna fliken "Delning."
- Klicka på "Dela..."
- Välj personerna att dela med och ställ in deras behörighetsnivåer.
- Precis som med MAC kan du välja "Alla: Läs" för den valda musikmappen.
- Klicka på "Färdig" för att spara dina inställningar.

![Evermusic - SMB-stöd - Delad mapp på Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Steg 2: Lägg till din dator automatiskt

- Öppna nu Evermusic och gå till fliken "Anslutningar" ("Nätverk" om du använder en äldre version av appen).
- Om du ser din dator i avsnittet "Tillgängliga enheter" ("Tillgängliga delningar" om du använder en äldre version av appen) och valde "Alla: Enbart läsning" i föregående steg, tryck bara på din dator och den ansluts automatiskt.
- Om detta inte händer kan du lägga till din dator manuellt.

![Evermusic - SMB-stöd - Anslut konto skärm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Steg 3: Lägg till din dator manuellt

- Tryck på "Anslut en molntjänst" ("Lägg till konto" om du använder en äldre version av appen)
- Välj "SMB" från listan över tillgängliga servrar på nästa skärm.
- På "SMB" inställningsskärmen:
  - Ange serverns URL med sökvägen till den delade mappen. Du kan ange servernamnet eller serverns IP. Till exempel:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Ange ditt användarnamn och lösenord eller lämna dessa fält tomma om du valde "Alla: Enbart läsning" i föregående steg.
  - Fältet "WORKGROUP" är valfritt och bör användas om du har en Active Directory-domän.

![Evermusic - SMB-stöd - Ange inloggningsuppgifter skärm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

När du har anslutit ditt SMB-konto visas det i avsnittet "Molntjänster" ("Konton"). Öppna det anslutna kontot genom att trycka på det, navigera till musikmappen och tryck på valfri ljudfil för att starta spelaren.

![Evermusic - SMB-stöd - Öppna ansluten mapp skärm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Njut av din musiksamling sömlöst på din iPhone eller iPad med Evermusic.

![Evermusic - SMB-stöd - Ljudspelare skärm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Steg 4: SMB2-lösning

Om du stöter på problem med att bläddra i mappar eller spela filer som innehåller specialtecken (som ü, ö, é), kan detta vara relaterat till SMB2-protokollet. Vi arbetar aktivt med att lösa detta problem.

Som en tillfällig lösning kan du prova att aktivera SMB 1 på din server och i appinställningarna. Alternativt kan du ansluta till din SMB-server via systemets filöppningsmeny. Så här gör du:

1. Navigera till "Lokala filer."
2. Scrolla ner till avsnittet "Filer på denna enhet" och tryck "Öppna filer..." eller "Öppna mappar..."
3. Hitta din server och välj de filer eller mappar du behöver.
4. Tryck "Öppna" för att bekräfta ditt val.

## Steg 5: WebDAV-lösning

Dessutom kan du prova att ansluta till din NAS med WebDAV- eller DLNA-protokoll om de stöds.

Genom att följa dessa steg kan du kringgå problemen relaterade till specialtecken i filnamn och fortsätta njuta av dina mediefiler.

P.S. Du kan också överföra ljudfiler från din MAC/PC till din iPhone med iTunes Fildelning och spela lokala ljudfiler. Lär dig mer om denna funktion i vår guide: [Hur man spelar iTunes-filer på iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Vanliga frågor

{{% details title="Kan jag streama musik från min PC till min iPhone utan iTunes?" closed="true" %}}
Ja. Evermusic ansluter till din PC via SMB på ditt lokala Wi-Fi-nätverk. iTunes behövs inte. Aktivera bara fildelning på din PC och anslut i appen.
{{% /details %}}

{{% details title="Använder SMB-streaming mobildata?" closed="true" %}}
Nej. SMB fungerar via ditt lokala Wi-Fi-nätverk. Ingen internetanslutning eller mobildata behövs.
{{% /details %}}

{{% details title="Vilka ljudformat stöder Evermusic via SMB?" closed="true" %}}
Evermusic stöder MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC och andra vanliga ljudformat. Filer spelas direkt från SMB-delningen.
{{% /details %}}

{{% details title="Kan jag streama musik från en NAS till min iPhone?" closed="true" %}}
Ja. Om din NAS stöder SMB (de flesta gör det, inklusive Synology, QNAP och WD My Cloud), kan du ansluta till den med samma steg i denna guide.
{{% /details %}}

{{% details title="Måste jag ha min dator påslagen under streaming?" closed="true" %}}
Ja. Eftersom Evermusic streamar filer direkt från din dator måste den vara påslagen och ansluten till samma nätverk som din iPhone.
{{% /details %}}

{{% details title="Finns det en filstorleksgräns för SMB-streaming?" closed="true" %}}
Nej. Evermusic streamar filer av alla storlekar via SMB. Stora förlustfria filer (FLAC, WAV) fungerar utan problem.
{{% /details %}}
