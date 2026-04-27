---
title: "Hur du aktiverar DLNA Media Server på Windows 10 och spelar din musik på iPhone"
date: 2019-11-26
description: "Aktivera DLNA-server på Windows 10 och strömma din musik till iPhone med Evermusic-appen. Steg-för-steg installationsguide inkluderad."
keywords: ["evermusic", "dlna", "windows 10", "iphone musikströmning", "mediaserver", "lokalt nätverk", "upnp"]
tags: ["evermusic", "musik", "moln", "iphone", "lagring", "lokal", "nas", "windows", "wifi", "lyssna", "nätverk", "fjärr", "hem", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Sammanfattning:** Windows 10 har en inbyggd DLNA-server. Aktivera den i Nätverks- och delningsinställningar, använd sedan den gratis **Evermusic**-appen på din iPhone för att strömma hela ditt musikbibliotek via Wi-Fi. Ingen serverprogramvara från tredje part behövs.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Framsida" caption="DLNA-musikströmning till iPhone med Windows 10 och Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) är ett kraftfullt verktyg som låter dig enkelt strömma olika medieinnehåll, inklusive musik, mellan DLNA-stödda enheter på ditt nätverk. Den goda nyheten är att Windows 10, och tidigare versioner, levereras med en inbyggd DLNA-funktion, vilket eliminerar behovet av mediaservrar från tredje part. Här är hur du aktiverar DLNA Media Server på Windows 10 och njuter av musikströmning på din iPhone.

## Hur du aktiverar DLNA Media Server på Windows 10

1. Klicka på 'Start'-knappen.  
2. Välj ikonen 'Inställningar'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Serverinställning" caption="Öppna Windows-inställningar" width="500" >}}

3. På skärmen 'Windows-inställningar' väljer du 'Nätverk och Internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows-inställningar" caption="Välj Nätverk och Internet" width="500" >}}

4. Under 'Nätverk' väljer du 'Nätverks- och delningscenter'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Delningscenter" caption="Öppna Nätverks- och delningscenter" width="500" >}}

5. På skärmen 'Nätverks- och delningscenter' klickar du på 'Ändra avancerade delningsinställningar' i vänstermenyn.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Avancerade delningsinställningar" caption="Ändra avancerade delningsinställningar" width="500" >}}

6. På skärmen 'Avancerade delningsinställningar' scrollar du ner till sektionen 'Alla nätverk' och expanderar den genom att klicka på pilen.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Aktivera upptäckt" caption="Expandera alla nätverksinställningar" width="500" >}}

7. Klicka på 'Aktivera mediaströmning' för att aktivera DLNA-servern.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Aktivera server" caption="Aktivera mediaströmningsserver" width="500" >}}

8. Ge ditt mediabibliotek ett namn och välj de enheter som får åtkomst till det.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Mediabibliotekets namn" caption="Namnge ditt DLNA-mediabibliotek" width="500" >}}

9. Klicka 'OK' för att bekräfta. Nu kommer dina personliga mappar som Musik, Bilder och Videor att vara synliga för alla strömmningsenheter med UPnP-stöd.

## Hur du inaktiverar DLNA Media Server på Windows 10

1. Klicka 'Start' och skriv 'services' i sökfältet.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows-tjänster" caption="Öppna Windows-tjänster" width="500" >}}

2. På skärmen 'Tjänster' scrollar du ner för att hitta 'Windows Media Player Network Sharing Service'.  
3. Dubbelklicka på den och ställ in 'Starttyp' till 'Manuell'.  
4. Stoppa tjänsten genom att klicka på 'Stoppa'-knappen.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Stoppa DLNA-tjänst" caption="Inaktivera DLNA-nätverksdelningstiänst" width="500" >}}

## Hur du spelar musik från DLNA-server på iPhone

1. Installera den gratis **Evermusic**-appen från App Store:  
   [Evermusic App](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Öppna fliken 'Anslutningar' och tryck på 'Tillgängliga enheter' i sektionen 'Lokalt nätverk'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic-anslutningar" caption="Evermusic: Anslutningsskärm" width="500" >}}

3. Vänta några sekunder medan enhetslistan laddas och tryck på Windows Media Player DLNA-servern (t.ex. 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Tillgängliga enheter" caption="Tillgängliga DLNA-servrar i Evermusic" width="500" >}}

4. Du ser en lista med mappar tillgängliga på mediaservern.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic-mappar" caption="Bläddra i delade mappar från DLNA-server" width="500" >}}

5. Öppna valfri mapp som innehåller ljudfiler.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Mappinnehåll" caption="Visa innehållet i delade DLNA-mappar" width="500" >}}

6. Tryck på valfri fil för att starta ljudspelaren.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Ljudspelare" caption="Spela ljudfil från DLNA i Evermusic" width="500" >}}

7. För att förbättra din ljudupplevelse, tryck på 'Equalizer'-ikonen nära volymindikatorn längst ner på skärmen för att aktivera iPod-stil equalizern med förförstärkare.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Equalizer" caption="Använd den inbyggda equalizern för förbättrad uppspelning" width="500" >}}

## Slutsats

Med DLNA Media Server på Windows 10 och Evermusic på din iPhone kan du njuta av sömlös musikströmning från din dator till din mobila enhet. Säg adjö till lagringsbegränsningar och hej till musik on demand!

## Vanliga frågor

{{% details title="Behöver jag installera serverprogramvara på Windows 10?" closed="true" %}}
Nej. Windows 10 inkluderar en inbyggd DLNA-mediaserver. Du behöver bara aktivera mediaströmning i Nätverks- och delningscentrets inställningar. Ingen programvara från tredje part krävs.
{{% /details %}}

{{% details title="Måste min iPhone vara på samma Wi-Fi-nätverk?" closed="true" %}}
Ja. DLNA-strömning fungerar över ditt lokala nätverk. Både din Windows 10-dator och din iPhone måste vara anslutna till samma Wi-Fi-nätverk för att Evermusic ska kunna upptäcka DLNA-servern.
{{% /details %}}

{{% details title="Vilka ljudformat kan jag strömma via DLNA?" closed="true" %}}
Windows DLNA-servern delar filer från din Musik-mapp oavsett format. Evermusic stöder MP3, FLAC, AAC, WAV, OGG, AIFF och många andra format, så du kan spela upp praktiskt taget vilken ljudfil som helst från servern.
{{% /details %}}

{{% details title="Kan jag använda Flacbox istället för Evermusic?" closed="true" %}}
Ja. Flacbox stöder också DLNA/UPnP-bläddring och uppspelning. Du kan använda vilken som helst av de två apparna för att upptäcka och spela musik från din Windows DLNA-server.
{{% /details %}}

{{% details title="Använder DLNA-strömning mobildata?" closed="true" %}}
Nej. DLNA fungerar uteslutande på ditt lokala Wi-Fi-nätverk. Det använder ingen mobildata. Båda enheterna måste dock förbli anslutna till samma nätverk under uppspelning.
{{% /details %}}
