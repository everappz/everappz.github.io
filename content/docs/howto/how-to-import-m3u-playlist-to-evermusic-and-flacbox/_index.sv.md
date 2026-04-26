---
title: "Hur man importerar M3U-spellista till Evermusic och Flacbox"
date: 2024-01-31
description: "Lär dig hur du importerar M3U-, M3U8- och CUE-spellistefiler från moln, lokal lagring eller enhet till Evermusic och Flacbox."
keywords: ["evermusic", "flacbox", "spellista", "m3u", "m3u8", "cue", "importera", "musikapp"]
tags: ["evermusic", "importera", "spellistor", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Sammanfattning:** Evermusic och Flacbox stöder import av M3U-, M3U8- och CUE-spellistefiler från molnlagring, lokala appfiler eller din enhet. Gå till Spellistor > Mer > Importera spellista, välj en källa, välj din fil och appen bygger din spellista automatiskt.

M3U, som står för MP3 URL eller Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, är ett datorfilformat som används för multimediaspellistor. En av dess primära användningar är att skapa spellistefiler med en enda post som pekar på strömmar på internet. Dessa filer erbjuder bekväm åtkomst till strömmande innehåll och används ofta för nedladdningar, e-post och att lyssna på internetradio.

Trots sin utbredda användning finns det ingen formell specifikation för M3U-formatet; det har blivit en de facto-standard. En M3U-fil är i grunden en vanlig textfil som anger platserna för en eller flera mediefiler. Beroende på kodningen sparas den med filändelsen "m3u" eller "m3u8". Varje post i filen anger en mediefils plats, som kan vara ett absolut lokalt sökvägsnamn, ett lokalt sökvägsnamn relativt till M3U-filens plats eller en URL. Poster separeras av radbrytningar, där vissa enheter kräver radbrytningar representerade som CR LF.

Dessutom kan M3U-filer innehålla kommentarer som inleds med "#"-tecknet. I utökad M3U introducerar "#" utökade M3U-direktiv, som kan stödja parametrar som avslutas med kolon ":".

I våra appar Evermusic och Flacbox har vi implementerat M3U-filimportfunktionalitet, vilket eliminerar behovet av manuellt skapande av spellistor. Denna guide leder dig genom att importera dina spellistor från molnlagring, lokala filer eller filer på din enhet direkt in i appen.

Navigera först till avsnittet 'Spellistor'. Tryck sedan på knappen 'Mer' i det övre högra hörnet. Från menyn som visas, välj alternativet 'Importera spellista'.

![importera spellista-åtgärd](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

På nästa skärm väljer du filplats. Stödda alternativ inkluderar:

- Ansluten molnlagring;
- Filer i applikationen;
- Filer på din enhet;

![välj filplats](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Låt oss välja ansluten molnlagring och öppna mappen som innehåller spellistefilen. Stödda filtyper för spellistor inkluderar M3U, M3U8 och CUE. Välj spellistefilen och tryck på 'Färdig' för att bekräfta ditt val.

![välj M3U-fil](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Appen kommer att analysera spellistefilen och skapa en lista över spår. Den hittar sedan dessa filer i lagringen och sammanställer en slutgiltig spellista som importeras till musikbiblioteket. Det är avgörande att din M3U/CUE-fil innehåller korrekta sökvägar för mediefiler och att filerna finns på dessa sökvägar i din lagring.

![importerad spellista](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Appen stöder både relativa sökvägar och absoluta fil-URL:er.

Till exempel:

Spellista med relativa sökvägar:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Spellista med absoluta URL:er:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Om du importerar en spellistefil som finns i appen (avsnittet Lokala filer) krävs inga ytterligare steg.

Om du dock vill importera en spellista som finns på din enhet med systemfilväljaren finns det en viktig aspekt att tänka på.

På grund av säkerhetspolicyer kan applikationen bara komma åt den fil du väljer med systemfilväljaren. Spellistefilen kan dock innehålla länkar till andra mediefiler på din enhet. För att importera en spellista från din enhet måste du välja en mapp som innehåller både spellistefilen och alla mediefiler som är länkade till den. I detta fall skannar appen den valda mappen, hittar spellistefilen, bygger spårlistan och importerar den till musikbiblioteket.

Dessutom kan du importera flera spellistor samtidigt genom att trycka på knappen "Fler åtgärder" och välja "Importera spellistor från en mapp." Appen skannar sedan mappens innehåll, hittar stödda spellistefiler och importerar dem till biblioteket.

## Vanliga frågor

{{% details title="Vilka spellisteformat stöder Evermusic och Flacbox?" closed="true" %}}
Båda apparna stöder filformaten M3U, M3U8 och CUE för spellistor. Dessa täcker de vanligaste spellistestandarderna som används av musikspelare och mediaprogramvara.
{{% /details %}}

{{% details title="Kan jag importera spellistor från molnlagring?" closed="true" %}}
Ja. Du kan importera spellistefiler från alla anslutna molnlagringstjänster inklusive Google Drive, Dropbox, OneDrive och WebDAV-servrar.
{{% /details %}}

{{% details title="Varför saknas vissa spår efter import?" closed="true" %}}
Spellistefilen måste innehålla korrekta sökvägar till dina mediefiler och dessa filer måste finnas på de angivna platserna i din lagring. Dubbelkolla att filsökvägarna i din M3U- eller CUE-fil matchar de faktiska filplatserna.
{{% /details %}}

{{% details title="Kan jag importera flera spellistor samtidigt?" closed="true" %}}
Ja. Använd knappen Fler åtgärder och välj "Importera spellistor från en mapp." Appen skannar mappen efter alla stödda spellistefiler och importerar dem i ett steg.
{{% /details %}}

{{% details title="Måste jag skapa spellistor manuellt?" closed="true" %}}
Nej. Importfunktionen eliminerar manuellt skapande av spellistor. Peka bara appen mot din befintliga M3U-, M3U8- eller CUE-fil och den bygger spellistan automatiskt.
{{% /details %}}
