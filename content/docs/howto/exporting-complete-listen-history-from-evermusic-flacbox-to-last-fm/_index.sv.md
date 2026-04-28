---
title: "Exportera din kompletta lyssningshistorik från Evermusic & Flacbox till Last.fm"
date: 2024-01-30
description: "Lär dig hur du exporterar din musikhistorik från Evermusic och Flacbox och laddar upp den till Last.fm med CSV-filer och Last.fm Scrubbler-verktyget för Windows."
keywords: ["evermusic", "flacbox", "lastfm", "musikhistorik", "scrobbling", "exportera låtar", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "senaste", "lastfm", "exportera", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Sammanfattning:** Exportera din lyssningshistorik från Evermusic eller Flacbox som en CSV-fil och ladda sedan upp den till Last.fm med det kostnadsfria verktyget Last.fm-Scrubbler-WPF på Windows. Automatisk scrobbling finns också tillgänglig inbyggt i båda apparna.

**Uppdatering:** Automatisk scrobbling är nu tillgänglig! Läs mer här: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling är ett enkelt sätt att automatiskt spara grundläggande detaljer som titel och artist för låten du lyssnar på till en onlinetjänst. Senare kan du granska din lyssningshistorik.

[Last.fm](https://www.last.fm/home), drivet av ett musikrekommendationssystem kallat Audioscrobbler, erbjuder denna tjänst gratis. Det skapar en detaljerad profil av din musiksmak genom att registrera spåren du lyssnar på, oavsett om det är från internetradiostationer, din dator eller olika bärbara musikenheter. Du kan besöka webbplatsen senare för att få rekommendationer om nya artister eller album som matchar din musiksmak.

Du kan ladda upp din lyssningshistorik till [Last.fm](http://Last.fm) från Evermusic- och Flacbox-apparna med ett gratis verktyg, och vi visar dig hur du gör det.

Öppna avsnittet 'Musikbibliotek' i applikationen och scrolla till avsnittet 'Snabbåtkomst'. Tryck på menyalternativet 'Senaste'.

![skärm för musikbibliotek](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

På skärmen 'Senaste' trycker du på knappen 'Mer' i det övre högra hörnet för att aktivera menyn 'Fler åtgärder'. Tryck på menyalternativet 'Exportera låtlista'.

![skärm för senaste](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

På skärmen 'Välj filformat' har du möjlighet att välja formatet för destinationsfilen. Tillgängliga alternativ - CSV, TXT, M3U.

![skärm för val av filformat](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Detta står för Comma-Separated Values, perfekt för att organisera dina data i ett snyggt tabellformat. I destinationsfilen hittar du parametrar som Artistnamn, Albumnamn, Spårnamn, Tidsstämpel (tiden du lyssnade på spåren), Albumartistnamn och Spårlängd.

TXT: Här pratar vi om en vanlig textfil. Den är enkel och okomplicerad, med parametrar inklusive Artistnamn, Albumnamn, Spårnamn och Längd.

M3U: Detta format är i grunden förstahandsvalet för att skapa spellistor. Det är bra för att du kan exportera din låtlista och njuta av dina spår på vilken enhet som helst, även om du inte har originalfilerna (förutsatt att du väljer alternativet för absolut URL för mediefiler). I utdatafilen hittar du parametrar som Längd, Artistnamn, Spårnamn och Mediafilsplats.

För vår uppgift är CSV det rätta valet. Vi kommer att använda denna fil med den kostnadsfria programvaran Last.fm-Scrubbler-WPF för att ladda upp vår lyssningshistorik till [Last.fm](http://Last.fm)-tjänsten. Välj helt enkelt CSV och tryck på knappen 'Exportera'.

![skärm för slutförd export](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

När exporten är klar trycker du helt enkelt på knappen 'Visa fil', och appen visar den skapade filen i din dokumentmapp. Tryck sedan på knappen 'Fler åtgärder' bredvid filnamnet och välj alternativet 'Öppna i' från menyn. Vårt nästa steg är att kopiera den exporterade filen till din stationära dator. Du kan enkelt göra detta genom att välja AirDrop-alternativet från menyn 'Öppna i'.

![fler åtgärder för exporterad fil](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Härnäst kommer vi att använda en gratis klient med öppen källkod för [Last.FM](http://Last.FM) som bara finns tillgänglig på Windows-plattformen. Denna klient låter dig effektivt uppdatera din lyssningshistorik på [Last.FM](http://Last.FM) med CSV-filen vi just exporterade.

Om du inte använder en Windows-dator för tillfället, oroa dig inte. Du kan fortfarande komma åt denna klient genom att installera VirtualBox på din Mac och använda den officiella avbildningen av Windows utvecklingsmiljö.

Här är vad du behöver göra:

- Installera VirtualBox från följande länk: [Ladda ner VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Ladda ner och installera Windows-utvecklingsmiljön från denna länk: [Windows-utvecklingsmiljö](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

På din Windows-dator (eller VirtualBox-appen med Windows Development-avbildningen) ladda ner och installera [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - gratis programvara med öppen källkod tillgänglig på GitHub. Vi testade på version 1.28 som du kan ladda ner här: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Nedladdningssida för Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Under avsnittet 'Assets' klickar du på [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) för att ladda ner installationsarkivet. Packa upp den nedladdade filen och öppna den uppackade mappen.

- VIKTIGT

Denna app är fortfarande i beta. Appskaparna har inte fått mycket testning. De rekommenderar att försöka scrobbla till ett testkonto först och se om det du vill scrobbla fungerar korrekt. Särskilt om du scrobblar många spår på en gång. Var försiktig med dina konton.

Kör Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

På applikationens huvudskärm trycker du helt enkelt på 'Inte inloggad' nere till vänster för att aktivera skärmen 'Lägg till konto'.

![Skärm för att lägga till konto](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Ange dina inloggningsuppgifter.

![skärm för inloggningsuppgifter](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Tryck på knappen 'Login' för att lägga till ditt konto.

![Tryck på knappen Login för att lägga till ditt konto.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Öppna fliken 'File Parse Scrobbler' för att börja importera CSV-filen från Evermusic-appen.

![Öppna fliken File Parse Scrobbler för att börja importera CSV-filen från Evermusic-appen.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Välj 'Parser: CSV' och tryck på knappen 'Settings'.

På nästa skärm kan du välja ordningen på parametrarna i din CSV-fil.

Enskilda fält kan omslutas av citattecken och MÅSTE omslutas av citattecken om fältet innehåller någon av de inställda avgränsarna. Till exempel:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Så lämna alla inställningar som standard; det enda du behöver ändra är att aktivera kryssrutan i fältet 'Has Fields Enclosed In Quotes'.

Tryck på 'Save & Close' för att tillämpa ändringarna.

![välj ordningen på parametrarna i din CSV-fil.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Filparse-scrobbling har två lägen. De kan ändras med ComboBox-en 'Scrobbling Mode'.

Normalt läge: I detta läge scrobblas spåren med tidsstämpeln från den parsade scrobblen. Endast scrobbles nyare än 14 dagar kan scrobblas.

Importläge: I detta läge scrobblas spåren med tidsstämpeln beräknad från 'Finish Time' och den valda längden mellan varje spår. Detta gör det möjligt att scrobbla spåren även om tidsstämpeln för den parsade scrobblen är äldre än 14 dagar. Därför kommer det första (översta) spåret i CSV-filen att scrobblas med 'Finish Time'.

Välj en tidigare genererad CSV-fil från Evermusic-appen i fältet 'File:' och tryck på 'Parse'. I vissa fall kan du se en felvarning som säger att vissa scrobbles inte kunde parsas. Det är okej om du har några spår utan fullständig metadata som Artistnamn.

![vissa scrobbles kunde inte parsas](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Tryck på knappen 'Check All' för att välja alla parsade spår.

![Tryck på knappen Check All för att välja alla parsade spår.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Tryck på knappen 'Preview' för att kontrollera alla ändringar som kommer att skickas till servern.

![Tryck på knappen Preview för att kontrollera alla ändringar som kommer att skickas till servern.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Tryck på knappen 'Scrobble' för att ladda upp alla ändringar till servern.

![Tryck på knappen Scrobble för att ladda upp alla ändringar till servern.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Tidigare hade Last.fm-Scrubbler-WPF ingen daglig scrobblegräns. Detta har nu ändrats eftersom vissa personer använde Scrubbler för att scrobbla så många spår att det orsakade problem för Last.fm-sidan. Scrobblegränsen är för närvarande 2800 scrobbles per dag. När du försöker scrobbla mer än det får du ett felmeddelande. Det finns planer på att lägga till en 'scrobblekö', så om du behöver scrobbla mer än 2800 spår läggs de till i en kö och scrobblas automatiskt efter en tid. Du kan kontrollera hur många scrobbles du har kvar i användarvalsvisningen.

När alla poster har laddats upp till servern ser du ett meddelande längst ner i appfönstret som bekräftar: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Nu kan du öppna din profil på [Last.fm](http://Last.fm)-sidan och kontrollera alla ändringar.

![din profil på Last.fm-sidan](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Vanliga frågor

{{% details title="Kan jag scrobbla automatiskt utan att exportera CSV-filer?" closed="true" %}}
Ja. Både Evermusic och Flacbox stöder nu automatisk Last.fm-scrobbling. Se guiden: [Hur man scrobblar till Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Vad händer om min CSV har spår som är äldre än 14 dagar?" closed="true" %}}
Använd Importläge i Last.fm-Scrubbler-WPF. Det beräknar om tidsstämplar från Finish Time, vilket gör att du kan scrobbla spår oavsett deras ursprungliga datum.
{{% /details %}}

{{% details title="Jag har ingen Windows-dator. Kan jag fortfarande använda Last.fm-Scrubbler?" closed="true" %}}
Ja. Installera VirtualBox på din Mac och ladda ner den kostnadsfria avbildningen av Windows-utvecklingsmiljö från Microsoft. Kör Last.fm-Scrubbler-WPF i den virtuella maskinen.
{{% /details %}}

{{% details title="Varför parsas inte vissa scrobbles?" closed="true" %}}
Spår som saknar väsentlig metadata (som artistnamn) kan inte parsas. Detta är förväntat och påverkar inte andra spår i filen.
{{% /details %}}

{{% details title="Finns det en daglig scrobblegräns?" closed="true" %}}
Ja. Last.fm-Scrubbler-WPF tillåter upp till 2 800 scrobbles per dag. Om du behöver scrobbla mer, fördela processen över flera dagar.
{{% /details %}}
