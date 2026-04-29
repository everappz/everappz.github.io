---
title: "Hur man exporterar spårsamling till M3U, CSV och TXT i Evermusic och Flacbox"
date: 2024-01-31
description: "Lär dig hur du exporterar senaste, favoriter, spellistor och album från Evermusic och Flacbox till M3U-, CSV- eller TXT-format. Perfekt för Last.fm-scrobbling och uppspelning på andra enheter."
keywords: ["evermusic export", "flacbox export", "exportera till m3u", "exportera spellista till csv", "m3u txt csv spellista", "musikexport"]
tags: ["evermusic", "senaste", "favoriter", "export", "m3u", "spellista", "csv", "txt", "album"]
---

{{< author-byline >}}


**Sammanfattning:** Evermusic och Flacbox låter dig exportera valfri spårsamling (senaste, favoriter, spellistor, album) till CSV-, TXT- eller M3U-filer. Använd dessa exporter för att scrobbla till Last.fm, säkerhetskopiera ditt bibliotek eller spela dina spellistor på andra enheter.

## Introduktion

Att exportera dina senaste, favoriter, album och spellistor från appen till en extern fil kan vara otroligt användbart. Du kan använda dessa filer för att uppdatera din lyssningshistorik på scrobblingstjänster som [Last.fm](http://Last.fm) eller lyssna på dina spellistor på externa enheter. Med Evermusic och Flacbox är denna process enkel. Här visar vi dig hur du exporterar senaste till CSV/TXT och dina spellistor till M3U. Denna funktion är dock tillgänglig för vilken spårsamling som helst i appen.

## Välj format

För att exportera senaste, öppna avsnittet «Musikbibliotek» och välj menyalternativet «Senaste».

![musikbibliotek](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

På nästa skärm trycker du på knappen «Mer» i det övre högra hörnet och väljer «Exportera låtlista».

![exportera senaste](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

På skärmen «Välj filformat» har du flera alternativ — CSV, TXT, M3U.

- CSV

Detta står för kommaseparerade värden, perfekt för att organisera dina data i ett snyggt tabellformat. I målfilen hittar du parametrar som artistnamn, albumnamn, spårnamn, tidsstämpel (tiden du lyssnade på spåren), albumartistnamn och spårlängd. Du kan använda den filen senare för att uppdatera din lyssningshistorik på scrobblingstjänster som [Last.fm](http://Last.fm) enligt beskrivningen [här](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Här talar vi om en vanlig textfil. Den är enkel och rakt på sak, med parametrar som artistnamn, albumnamn, spårnamn och längd. Användbar om du bara behöver en lista över spår i textformat.

- M3U

Detta format är i princip standardformatet för att skapa spellistor. Det är bra eftersom du kan exportera din låtlista och njuta av dina spår på vilken enhet som helst, även om du inte har originalfilerna (om du väljer alternativet med absolut URL för mediefilerna vid export). I utdatafilen hittar du parametrar som längd, artistnamn, spårnamn och medifilsplats.

## CSV-format

Nu väljer vi CSV och ser vad vi får. Välj helt enkelt CSV och tryck på knappen «Exportera».

![välj filformat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

När exporten är klar ser du en avisering med två alternativ. Genom att trycka på «Visa fil» visas den resulterande filen i din dokumentkatalog.

![export slutförd](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Nu kan du skicka den filen, öppna den i en extern textredigerare eller använda den för att uppdatera din lyssningshistorik på [Last.fm](http://Last.fm).

![exportmapp med resultatfiler](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Den resulterande CSV-filen kommer att innehålla fält i följande format:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Till exempel:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![exporterad csv-fil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT-format

Den resulterande TXT-filen kommer att innehålla fält i följande format:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Till exempel:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![exporterad txt-fil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U-format

Härnäst guidar vi dig genom export av din spellista till M3U-format, som är de facto-standarden för spellistfiler. Huvudförutsättningen för en lyckad spellistexport är att alla filer i spellistan måste finnas på samma lagring, oavsett om det är en molntjänst som Google Drive, lokala filer eller filer på din enhet. För att påbörja exportprocessen, öppna valfri spellista och tryck på knappen «Mer» i det övre högra hörnet, välj sedan menyalternativet «Exportera låtlista».

![spellistskärm](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

På nästa skärm väljer du filformatet «M3U», där du hittar två alternativ för «Typ av medifilsplats»:

![skärm för val av exportfilformat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Om du väljer «Relativ sökväg» skapas spellistan med medifilsplatser skrivna relativt till spellistfilen. Till exempel:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   I detta fall bör du undvika att ändra M3U-filens plats efter att exporten är klar, eftersom det bryter sökvägarna till medifilerna. För att börja spela din spellista trycker du helt enkelt på den exporterade spellistfilen, och appen hittar automatiskt medifilerna i din lagring och startar uppspelningen. Du kan till och med exportera dina spellistor till lagringen och sedan importera dem igen på din nya enhet.

2. Om du väljer «Absolut URL» genererar appen direkta URL-adresser för dina mediefiler. Detta gör att du kan spela spellistan på vilken enhet/applikation som helst utan att alla mediefiler behöver finnas på samma lagring som spellistfilen. Detta alternativ stöds bara för molnlagring som kan generera direkta fil-URL:er. Tänk dock på att de genererade URL-adresserna i vissa fall kan ha begränsad livstid och kan upphöra att gälla efter en tid. Här är listan över molntjänster som stöds: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (i gästläge)  

Den resulterande mediefil-URL:en kommer att se ut ungefär så här:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

När du har valt «Typ av medifilsplats» trycker du på «Exportera». Appen uppmanar dig att välja en målmapp för export av M3U-filen. Tryck på «Färdig» för att bekräfta ditt val.

![välj en mapp](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Appen genererar en M3U-fil och laddar upp/flyttar den till målmappen.

![laddar upp m3u-fil](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

När exporten är klar visas en systemavisering med alternativet «Visa fil».

![avisering om slutförd export](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Genom att trycka på detta visas den exporterade filen i appen.

![exporterad m3u-fil i fillistan](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Om du valde «Relativ sökväg» som «Typ av medifilsplats» i föregående steg kommer utdatafilen att vara i följande format:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![m3u-exempel med relativa sökvägar](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

För alternativet «Absolut URL» genererar appen en M3U-fil i formatet:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![m3u-exempel med absoluta fil-URL:er](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Du kan öppna den filen på vilken enhet/applikation som helst som stöder M3U-spellistor.

![m3u-spellista öppnad i extern app](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Avslutande tankar

Att exportera dina spår från Evermusic och Flacbox ger dig fullständig kontroll över dina musikdata. Oavsett om du säkerhetskopierar din lyssningshistorik, scrobblar till Last.fm eller njuter av spellistor på externa enheter, är dessa exportalternativ — M3U, CSV och TXT — kraftfulla verktyg anpassade för flexibilitet och kompatibilitet. Dra nytta av dessa funktioner för att förbättra hur du organiserar, delar och återbesöker din musiksamling över plattformar.

## Vanliga frågor

{{% details title="Vilket exportformat ska jag använda för Last.fm-scrobbling?" closed="true" %}}
Använd CSV. Det innehåller tidsstämplar och fullständig metadata som krävs av scrobblingsverktyg som Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Kan jag exportera vilken spårsamling som helst, inte bara spellistor?" closed="true" %}}
Ja. Du kan exportera senaste, favoriter, album, spellistor och alla andra spårsamlingar i appen med samma steg.
{{% /details %}}

{{% details title="Kommer min M3U-spellista att fungera på andra enheter?" closed="true" %}}
Om du väljer alternativet Absolut URL under exporten kan M3U-filen spelas på vilken enhet som helst som stöder M3U-spellistor. Observera att vissa moln-URL:er kan upphöra att gälla med tiden.
{{% /details %}}

{{% details title="Är exportfunktionen gratis?" closed="true" %}}
Ja. Export av spårsamlingar till M3U, CSV och TXT är tillgänglig i både gratis- och premiumversionerna av Evermusic och Flacbox.
{{% /details %}}

{{% details title="Vilka molntjänster stöder export med absolut URL?" closed="true" %}}
Export med absolut URL stöds för iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive och WebDAV (gästläge).
{{% /details %}}
