---
title: "Överför filer från datorn till iPhone med SMB-protokollet"
description: "Lär dig hur du överför och får åtkomst till stora filer från din Mac eller Windows PC till din iPhone eller iPad med Evermusic och SMB-protokollet. En steg-för-steg-guide för sömlös streaming och filhantering."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["överföra filer till iPhone SMB", "streama PC-musik på iPhone", "ansluta Mac till iPhone SMB", "Evermusic SMB-inställning", "åtkomst till datorfiler iPhone", "Windows musikdelning iOS", "SMB filöverföring Evermusic"]
---

{{< author-byline >}}


**Sammanfattning:** Använd Evermusic på din iPhone eller iPad för att få åtkomst till filer lagrade på din Mac eller Windows PC över ditt lokala nätverk via SMB. Inga kablar, ingen iTunes, ingen molnuppladdning krävs. Aktivera fildelning på din dator, anslut i appen och bläddra eller spela upp dina filer trådlöst.

Har du en omfattande samling stora filer på din MAC eller PC och vill komma åt dem enkelt från din iPhone eller iPad? Våra appar ger en enkel lösning.

Följ dessa steg för att aktivera sömlös åtkomst mellan din dator och iOS-enhet med SMB-protokollet:

## Steg 1: Aktivera SMB-protokollet på din dator

**För MAC:**

1. Öppna "Systeminställningar" på din MAC.
2. Klicka på "Delning".
3. Aktivera tjänsten "Fildelning".
4. Lägg till din musikmapp i avsnittet "Delade mappar". Lägg till en användare och välj behörighetsnivå (Läs och skriv eller Skrivskyddad). Du kan välja "Alla: Skrivskyddad" för den tillagda musikmappen.

   ![Mac-inställningsskärm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Kom ihåg datorns URL (smb://192.168.xx.xx), eftersom du kommer att använda den i nästa steg.
6. Klicka på "Alternativ" och aktivera "Dela filer och mappar via SMB".

   ![Mac-fildelningsskärm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Aktivera "Windows-fildelning" för tillgängliga konton.

   ![Mac SMB-delningsskärm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**För Windows PC:**

1. Högerklicka på din musikmapp.
2. Välj "Egenskaper".
3. Gå till fliken "Delning".
4. Klicka på "Dela..."
5. Välj personerna du vill dela mappen med och ange behörighetsnivån. Du kan välja "Alla: Läs" för den valda musikmappen.

   ![Windows SMB-delningsskärm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Klicka på "Färdig".
7. Klicka på "Färdig" i fönstret "Fildelning" och kom ihåg mappsökvägen.

   ![Windows SMB delad mapp](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Steg 2: Anslut din iOS-enhet

1. Öppna appen på din iPhone eller iPad.
2. Gå till fliken "Anslutningar".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic Anslutningar-skärm"
  caption="Evermusic Anslutningar-skärm"
  width="400"
>}}

*Om din dator visas i avsnittet "Tillgängliga enheter":*

Om din dator är synlig i avsnittet "Tillgängliga enheter" och du valde "Alla: Skrivskyddad" i föregående steg, tryck helt enkelt på din dator så ansluts den automatiskt.

*Om din dator inte visas automatiskt:*

1. Tryck på "Anslut en molntjänst".
2. Välj "SMB" på skärmen "Anslut en molntjänst".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic Anslut en molntjänst-skärm"
  caption="Evermusic Anslut en molntjänst-skärm"
  width="400"
>}}

3. På skärmen "SMB-anslutning" anger du serverns URL med sökvägen till den delade mappen. Du kan använda servernamnet eller serverns IP:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Ange ditt användarnamn och lösenord eller lämna dessa fält tomma om du valde "Alla: Skrivskyddad" i föregående steg.
5. Fältet "WORKGROUP" är valfritt och bör användas om du har en Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMB-anslutningsskärm"
  caption="Evermusic SMB-anslutningsskärm"
  width="400"
>}}

6. När du har anslutit din dator med SMB-protokollet visas den i avsnittet "Molntjänster" på skärmen "Anslutningar".
7. Öppna den anslutna tjänsten och navigera till önskad mapp.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Öppnad SMB-mapp i Evermusic"
  caption="Öppnad SMB-mapp i Evermusic"
  width="400"
>}}

8. Du kan använda den inbyggda filhanteraren för att redigera dina filer efter behov.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic filhanterare"
  caption="Evermusic filhanterare"
  width="400"
>}}

## Steg 3: Lösning för SMB2-mappar med specialtecken

Ibland kan du stöta på problem med mappar som innehåller specialtecken när du använder SMB2-protokollet. Här är några steg för att lösa detta problem:

1. **Aktivera SMB 1:**  
   • Som en tillfällig lösning, försök aktivera SMB 1 på din server och i appinställningarna. Detta kan hjälpa till att kringgå problemen relaterade till specialtecken i mappnamn.

2. **Använd systemets filöppningsmeny:**  
   • Navigera till "Lokala filer".  
   • Scrolla ner till avsnittet "Filer på denna enhet".  
   • Tryck på "Öppna filer..." eller "Öppna mappar...".  
   • Hitta din server och välj de filer eller mappar du behöver.  
   • Tryck på "Öppna" för att bekräfta ditt val.

3. **Alternativa protokoll:**  
   • Om problemet kvarstår, överväg att ansluta till din NAS med WebDAV- eller DLNA-protokoll om din NAS stöder dessa alternativ. Dessa protokoll kan hantera specialtecken smidigare.

Genom att följa dessa steg kan du mildra problemen med specialtecken i mappnamn när du använder SMB2-protokollet.

## Slutsats

Med dessa steg kan du enkelt komma åt din stora samling filer från din MAC eller PC på din iPhone eller iPad med våra appar.

## Vanliga frågor

{{% details title="Kan jag komma åt filer på min PC från min iPhone utan iTunes?" closed="true" %}}
Ja. Evermusic ansluter till din dator via SMB på ditt lokala Wi-Fi-nätverk. Ingen iTunes- eller Finder-synkronisering behövs. Aktivera fildelning på din PC och anslut direkt från appen.
{{% /details %}}

{{% details title="Fungerar SMB-filåtkomst via internet?" closed="true" %}}
Nej. SMB är ett lokalt nätverksprotokoll. Din iPhone och dator måste vara på samma Wi-Fi-nätverk. För fjärråtkomst, ladda upp filer till en molntjänst som Google Drive eller Dropbox och anslut till den i Evermusic.
{{% /details %}}

{{% details title="Vilka filtyper kan jag komma åt via SMB?" closed="true" %}}
Evermusic stöder MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC och andra ljudformat. Du kan också bläddra och hantera icke-ljudfiler med den inbyggda filhanteraren.
{{% /details %}}

{{% details title="Kan jag överföra filer från en NAS till min iPhone med SMB?" closed="true" %}}
Ja. De flesta NAS-enheter (Synology, QNAP, WD My Cloud och andra) stöder SMB. Anslut till din NAS med samma steg i denna guide.
{{% /details %}}

{{% details title="Behöver jag kopiera filer till min iPhone för att spela dem?" closed="true" %}}
Nej. Evermusic streamar filer direkt från din dator eller NAS över nätverket. Filer kopieras inte till din iPhone om du inte väljer att ladda ner dem för offlineuppspelning.
{{% /details %}}

{{% details title="Är SMB-fildelning säkert?" closed="true" %}}
SMB-fildelning fungerar bara på ditt lokala nätverk. Andra enheter på andra nätverk kan inte komma åt dina delade mappar. För extra säkerhet, använd användarnamn och lösenord istället för anonym (Alla) åtkomst.
{{% /details %}}
