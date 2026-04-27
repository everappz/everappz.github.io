---
title: "Kuinka ottaa käyttöön DLNA Media Server Windows 10:ssä ja toistaa musiikkia iPhonessa"
date: 2019-11-26
description: "Ota DLNA-palvelin käyttöön Windows 10:ssä ja suoratoista musiikkiasi iPhoneen Evermusic-sovelluksella. Vaiheittainen asennusopas mukana."
keywords: ["evermusic", "dlna", "windows 10", "iphone musiikin suoratoisto", "mediapalvelin", "paikallinen verkko", "upnp"]
tags: ["evermusic", "musiikki", "pilvi", "iphone", "tallennus", "paikallinen", "nas", "windows", "wifi", "kuuntelu", "verkko", "etä", "koti", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Lyhyesti:** Windows 10:ssä on sisäänrakennettu DLNA-palvelin. Ota se käyttöön Verkko- ja jakamisasetuksissa ja käytä sitten ilmaista **Evermusic**-sovellusta iPhonessasi koko musiikkikirjastosi suoratoistoon Wi-Fi:n kautta. Kolmannen osapuolen palvelinohjelmistoa ei tarvita.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Kansikuva" caption="DLNA-musiikin suoratoisto iPhoneen Windows 10:n ja Evermusicin avulla" width="800" >}}

DLNA (Digital Living Network Alliance) on tehokas työkalu, jonka avulla voit vaivattomasti suoratoistaa erilaista mediasisältöä, mukaan lukien musiikkia, DLNA-yhteensopivien laitteiden välillä verkossasi. Hyvä uutinen on, että Windows 10 ja aiemmat versiot sisältävät sisäänrakennetun DLNA-ominaisuuden, mikä poistaa kolmannen osapuolen mediapalvelimien tarpeen. Näin otat DLNA Media Serverin käyttöön Windows 10:ssä ja nautit musiikin suoratoistosta iPhonessasi.

## Kuinka ottaa käyttöön DLNA Media Server Windows 10:ssä

1. Napsauta 'Käynnistä'-painiketta.  
2. Valitse 'Asetukset'-kuvake.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Palvelimen asennus" caption="Avaa Windows-asetukset" width="500" >}}

3. Valitse 'Windows-asetukset'-näytössä 'Verkko ja Internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows-asetukset" caption="Valitse Verkko ja Internet" width="500" >}}

4. Valitse kohdasta 'Verkko' vaihtoehto 'Verkko- ja jakamiskeskus'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Jakamiskeskus" caption="Avaa Verkko- ja jakamiskeskus" width="500" >}}

5. Napsauta 'Verkko- ja jakamiskeskus'-näytössä vasemman valikon 'Muuta jakamisen lisäasetuksia'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Jakamisen lisäasetukset" caption="Muuta jakamisen lisäasetuksia" width="500" >}}

6. Vieritä 'Jakamisen lisäasetukset'-näytössä alas kohtaan 'Kaikki verkot' ja laajenna se napsauttamalla nuolta.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Ota tunnistus käyttöön" caption="Laajenna kaikkien verkkojen asetukset" width="500" >}}

7. Napsauta 'Ota median suoratoisto käyttöön' aktivoidaksesi DLNA-palvelimen.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Ota palvelin käyttöön" caption="Ota median suoratoistopalvelin käyttöön" width="500" >}}

8. Anna mediakirjastollesi nimi ja valitse laitteet, joilla on pääsy siihen.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Mediakirjaston nimi" caption="Nimeä DLNA-mediakirjastosi" width="500" >}}

9. Napsauta 'OK' vahvistaaksesi. Nyt henkilökohtaiset kansiosi kuten Musiikki, Kuvat ja Videot ovat näkyvissä kaikille UPnP-yhteensopiville suoratoistolaitteille.

## Kuinka poistaa käytöstä DLNA Media Server Windows 10:ssä

1. Napsauta 'Käynnistä' ja kirjoita 'services' hakukenttään.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows-palvelut" caption="Avaa Windows-palvelut" width="500" >}}

2. Vieritä 'Palvelut'-näytössä alas löytääksesi 'Windows Media Player Network Sharing Service'.  
3. Kaksoisnapsauta sitä ja aseta 'Käynnistystyyppi' arvoon 'Manuaalinen'.  
4. Pysäytä palvelu napsauttamalla 'Pysäytä'-painiketta.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Pysäytä DLNA-palvelu" caption="Poista DLNA-verkon jakamispalvelu käytöstä" width="500" >}}

## Kuinka toistaa musiikkia DLNA-palvelimelta iPhonessa

1. Asenna ilmainen **Evermusic**-sovellus App Storesta:  
   [Evermusic-sovellus](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Avaa 'Yhteydet'-välilehti ja napauta 'Käytettävissä olevat laitteet' kohdassa 'Paikallinen verkko'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic-yhteydet" caption="Evermusic: Yhteydet-näyttö" width="500" >}}

3. Odota muutama sekunti laitelistan latautuessa ja napauta Windows Media Player DLNA -palvelinta (esim. 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Käytettävissä olevat laitteet" caption="Käytettävissä olevat DLNA-palvelimet Evermusicissa" width="500" >}}

4. Näet luettelon mediapalvelimella käytettävissä olevista kansioista.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic-kansiot" caption="Selaa DLNA-palvelimen jaettuja kansioita" width="500" >}}

5. Avaa mikä tahansa äänitiedostoja sisältävä kansio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Kansion sisältö" caption="Näytä jaettujen DLNA-kansioiden sisältö" width="500" >}}

6. Napauta mitä tahansa tiedostoa käynnistääksesi äänisoittimen.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Äänisoitin" caption="Toista äänitiedosto DLNA:sta Evermusicissa" width="500" >}}

7. Parantaaksesi äänikokemustasi, napauta 'Taajuuskorjain'-kuvaketta äänenvoimakkuusilmaisimen lähellä näytön alareunassa aktivoidaksesi iPod-tyylisen taajuuskorjaimen esivahvistimella.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Taajuuskorjain" caption="Käytä sisäänrakennettua taajuuskorjainta parempaan toistoon" width="500" >}}

## Yhteenveto

DLNA Media Serverin avulla Windows 10:ssä ja Evermusicin avulla iPhonessasi voit nauttia saumattomasta musiikin suoratoistosta tietokoneeltasi mobiililaitteellesi. Sano hyvästit tallennusrajoituksille ja tervetuloa musiikki pyynnöstä!

## Usein kysytyt kysymykset

{{% details title="Tarvitseeko minun asentaa palvelinohjelmistoa Windows 10:een?" closed="true" %}}
Ei. Windows 10 sisältää sisäänrakennetun DLNA-mediapalvelimen. Sinun tarvitsee vain ottaa käyttöön median suoratoisto Verkko- ja jakamiskeskuksen asetuksissa. Kolmannen osapuolen ohjelmistoa ei tarvita.
{{% /details %}}

{{% details title="Täytyykö iPhoneni olla samassa Wi-Fi-verkossa?" closed="true" %}}
Kyllä. DLNA-suoratoisto toimii paikallisverkossasi. Sekä Windows 10 -tietokoneesi että iPhonesi on oltava yhdistettynä samaan Wi-Fi-verkkoon, jotta Evermusic löytää DLNA-palvelimen.
{{% /details %}}

{{% details title="Mitä ääniformaatteja voin suoratoistaa DLNA:n kautta?" closed="true" %}}
Windows DLNA -palvelin jakaa tiedostoja Musiikki-kansiostasi riippumatta formaatista. Evermusic tukee MP3-, FLAC-, AAC-, WAV-, OGG-, AIFF- ja monia muita formaatteja, joten voit toistaa käytännössä minkä tahansa äänitiedoston palvelimelta.
{{% /details %}}

{{% details title="Voinko käyttää Flacboxia Evermusicin sijaan?" closed="true" %}}
Kyllä. Flacbox tukee myös DLNA/UPnP-selausta ja toistoa. Voit käyttää kumpaa tahansa sovellusta musiikin löytämiseen ja toistamiseen Windows DLNA -palvelimeltasi.
{{% /details %}}

{{% details title="Käyttääkö DLNA-suoratoisto mobiilidataa?" closed="true" %}}
Ei. DLNA toimii kokonaan paikallisessa Wi-Fi-verkossasi. Se ei käytä mobiilidataa. Molempien laitteiden on kuitenkin pysyttävä yhdistettynä samaan verkkoon toiston aikana.
{{% /details %}}
