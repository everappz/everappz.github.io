---
title: "Sådan aktiverer du DLNA Media Server på Windows 10 og afspiller din musik på iPhone"
date: 2019-11-26
description: "Aktiver DLNA-server på Windows 10 og stream din musik til iPhone med Evermusic-appen. Trin-for-trin opsætningsguide inkluderet."
keywords: ["evermusic", "dlna", "windows 10", "iphone musikstreaming", "medieserver", "lokalt netværk", "upnp"]
tags: ["evermusic", "musik", "cloud", "iphone", "lagring", "lokal", "nas", "windows", "wifi", "lyt", "netværk", "fjern", "hjem", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Kort sagt:** Windows 10 har en indbygget DLNA-server. Aktiver den i Netværks- og delingsindstillinger, og brug derefter den gratis **Evermusic**-app på din iPhone til at streame hele dit musikbibliotek over Wi-Fi. Ingen tredjeparts serversoftware nødvendig.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Forside" caption="DLNA-musikstreaming til iPhone med Windows 10 og Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) er et kraftfuldt værktøj, der gør det muligt at streame forskellige medieindhold, herunder musik, mellem DLNA-understøttede enheder på dit netværk. Den gode nyhed er, at Windows 10 og tidligere versioner leveres med en indbygget DLNA-funktion, hvilket eliminerer behovet for tredjeparts medieservere. Her er, hvordan du aktiverer DLNA Media Server på Windows 10 og nyder musikstreaming på din iPhone.

## Sådan aktiverer du DLNA Media Server på Windows 10

1. Klik på 'Start'-knappen.  
2. Vælg 'Indstillinger'-ikonet.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Opsæt server" caption="Åbn Windows-indstillinger" width="500" >}}

3. På skærmen 'Windows-indstillinger' skal du vælge 'Netværk og internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows-indstillinger" caption="Vælg Netværk og internet" width="500" >}}

4. Under 'Netværk' skal du vælge 'Netværks- og delingscenter'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Delingscenter" caption="Åbn Netværks- og delingscenter" width="500" >}}

5. På skærmen 'Netværks- og delingscenter' skal du klikke på 'Skift avancerede delingsindstillinger' i venstremenuen.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Avancerede delingsindstillinger" caption="Skift avancerede delingsindstillinger" width="500" >}}

6. På skærmen 'Avancerede delingsindstillinger' skal du scrolle ned til sektionen 'Alle netværk' og udvide den ved at klikke på pilen.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Slå registrering til" caption="Udvid alle netværksindstillinger" width="500" >}}

7. Klik på 'Slå mediestreaming til' for at aktivere DLNA-serveren.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Slå server til" caption="Aktiver mediestreaming-server" width="500" >}}

8. Giv dit mediebibliotek et navn og vælg de enheder, der skal have adgang til det.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Mediebiblioteksnavn" caption="Navngiv dit DLNA-mediebibliotek" width="500" >}}

9. Klik 'OK' for at bekræfte. Nu vil dine personlige mapper som Musik, Billeder og Videoer være synlige for alle streamingenheder med UPnP-understøttelse.

## Sådan deaktiverer du DLNA Media Server på Windows 10

1. Klik 'Start' og skriv 'services' i søgefeltet.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows-tjenester" caption="Åbn Windows-tjenester" width="500" >}}

2. På skærmen 'Tjenester' skal du scrolle ned for at finde 'Windows Media Player Network Sharing Service'.  
3. Dobbeltklik på den og sæt 'Starttype' til 'Manuel'.  
4. Stop tjenesten ved at klikke på 'Stop'-knappen.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Stop DLNA-tjeneste" caption="Deaktiver DLNA-netværksdelingstjeneste" width="500" >}}

## Sådan afspiller du musik fra DLNA-server på iPhone

1. Installer den gratis **Evermusic**-app fra App Store:  
   [Evermusic App](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Åbn fanen 'Forbindelser' og tryk på 'Tilgængelige enheder' i sektionen 'Lokalt netværk'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic-forbindelser" caption="Evermusic: Forbindelsesskærm" width="500" >}}

3. Vent et par sekunder mens enhedslisten indlæses, og tryk på Windows Media Player DLNA-serveren (f.eks. 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Tilgængelige enheder" caption="Tilgængelige DLNA-servere i Evermusic" width="500" >}}

4. Du vil se en liste over mapper tilgængelige på medieserveren.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic-mapper" caption="Gennemse delte mapper fra DLNA-server" width="500" >}}

5. Åbn en hvilken som helst mappe med lydfiler.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Mappeindhold" caption="Se indholdet af delte DLNA-mapper" width="500" >}}

6. Tryk på en hvilken som helst fil for at starte lydafspilleren.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Lydafspiller" caption="Afspil lydfil fra DLNA i Evermusic" width="500" >}}

7. For at forbedre din lydoplevelse skal du trykke på 'Equalizer'-ikonet nær lydstyrkeindikatoren nederst på skærmen for at aktivere iPod-stil equalizeren med en forstærker.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Equalizer" caption="Brug den indbyggede equalizer til forbedret afspilning" width="500" >}}

## Konklusion

Med DLNA Media Server på Windows 10 og Evermusic på din iPhone kan du nyde problemfri musikstreaming fra din computer til din mobilenhed. Sig farvel til lagringsbegrænsninger og hej til musik on demand!

## Ofte stillede spørgsmål

{{% details title="Skal jeg installere serversoftware på Windows 10?" closed="true" %}}
Nej. Windows 10 inkluderer en indbygget DLNA-medieserver. Du skal kun aktivere mediestreaming i indstillingerne for Netværks- og delingscenter. Ingen tredjeparts software nødvendig.
{{% /details %}}

{{% details title="Skal min iPhone være på det samme Wi-Fi-netværk?" closed="true" %}}
Ja. DLNA-streaming fungerer over dit lokale netværk. Både din Windows 10-pc og din iPhone skal være forbundet til det samme Wi-Fi-netværk, for at Evermusic kan finde DLNA-serveren.
{{% /details %}}

{{% details title="Hvilke lydformater kan jeg streame via DLNA?" closed="true" %}}
Windows DLNA-serveren deler filer fra din Musik-mappe uanset format. Evermusic understøtter MP3, FLAC, AAC, WAV, OGG, AIFF og mange andre formater, så du kan afspille stort set enhver lydfil fra serveren.
{{% /details %}}

{{% details title="Kan jeg bruge Flacbox i stedet for Evermusic?" closed="true" %}}
Ja. Flacbox understøtter også DLNA/UPnP-browsing og afspilning. Du kan bruge begge apps til at finde og afspille musik fra din Windows DLNA-server.
{{% /details %}}

{{% details title="Bruger DLNA-streaming mobildata?" closed="true" %}}
Nej. DLNA fungerer udelukkende på dit lokale Wi-Fi-netværk. Det bruger ingen mobildata. Begge enheder skal dog forblive forbundet til det samme netværk under afspilning.
{{% /details %}}
