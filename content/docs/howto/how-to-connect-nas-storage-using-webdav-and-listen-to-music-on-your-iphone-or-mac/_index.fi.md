---
title: "Kuinka yhdistää NAS-tallennustila WebDAV:n avulla ja kuunnella musiikkia iPhonella tai Macilla"
date: 2024-07-28
description: "Opi konfiguroimaan WebDAV Synology NAS:iin ja suoratoistamaan musiikkia iPhonelle tai Macille Evermusicin tai Flacboxin avulla. Seuraa vaiheittaista opastamme."
keywords: ["yhdistä nas", "webdav synology", "suoratoista musiikkia nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["musiikki", "suoratoisto", "tallennustila", "nas", "yhdistä", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Tiivistelmä:** Asenna ja ota käyttöön WebDAV Synology NAS:iin, määritä jaetun kansion käyttöoikeudet ja yhdistä sitten Evermusicista tai Flacboxista käyttäen NAS:n IP-osoitetta ja WebDAV-porttia (oletus 5005/5006). Voit suoratoistaa ja hallita koko musiikkikirjastoasi kopioimatta tiedostoja laitteeseesi.

Tutustu siihen, miten yhdistät NAS-tallennustilasi WebDAV:n avulla ja suoratoistat vaivattomasti musiikkikirjastosi iPhonelle tai Macille. WebDAV (Web-based Distributed Authoring and Versioning) on protokolla, jonka avulla voit hallita ja jakaa tiedostoja Internetin kautta. Ottamalla WebDAV:n käyttöön NAS:issasi voit käyttää ja suoratoistaa musiikkikokoelmaasi, jolloin suosikkikappaleesi ovat aina ulottuvillasi.

Tässä oppaassa näytämme, kuinka WebDAV-yhteys asetetaan yhdellä suosituimmista NAS-palvelimista, Synology NAS:illa. Seuraa yksinkertaisia ohjeitamme WebDAV:n konfiguroimiseksi Synology NAS:iin, ja voit selata, suoratoistaa ja hallita musiikkikirjastoasi suoraan iPhoneltasi tai Maciltasi.

## Vaihe 1: Asenna WebDAV Synology NAS:iin

1. Kirjaudu Synology NAS:iin ja avaa **Pakettikeskus**.
2. Etsi "webdav" ja asenna WebDAV-paketti, jos sitä ei ole vielä asennettu. Avaa WebDAV-palvelin sen konfiguroimiseksi.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Asenna WebDAV Synologyyn" width="600" >}}

## Vaihe 2: Konfiguroi WebDAV-palvelin

1. WebDAV-asetussivulla valitse ruudut **Ota HTTP käyttöön**, **Ota HTTPS käyttöön**, **Ota anonyymi WebDAV käyttöön** ja **Ota DavDepthInfinity käyttöön**.
2. Napsauta **Käytä** tallentaaksesi muutokset. Merkitse muistiin HTTP- ja HTTPS-yhteyksien porttinumerot, jotka ovat oletuksena 5005 ja 5006.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfiguroi WebDAV-asetukset" width="600" >}}

## Vaihe 3: Konfiguroi jaetun kansion käyttöoikeudet

1. Avaa **Ohjauspaneeli** ja siirry **Jaettu kansio** -osioon.
2. Valitse **Musiikki**-kansio ja napsauta **Muokkaa**.
3. **Käyttöoikeudet**-välilehdessä määritä käyttöoikeudet. Ota vieraskäyttö käyttöön Vain luku -oikeudella, jos haluat vain kuunnella musiikkia, tai Luku/Kirjoitus -oikeudella, jos haluat muokata tiedostoja. Tallenna muutokset.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Jaetun kansion käyttöoikeudet" width="600" >}}

## Vaihe 4: Selvitä Synology NAS:n IP-osoite

1. Avaa **Ohjauspaneeli** ja siirry **Verkkoliitäntä**-välilehdelle, tai käytä selainta vieraillaksesi osoitteessa [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Selvitä NAS:n IP-osoite" width="600" >}}

2. Merkitse muistiin Synology NAS:n IP-osoite (esim. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS:n IP-osoite" width="600" >}}

## Vaihe 5: Yhdistä Synology NAS:iin Evermusicin/Flacboxin avulla

1. Avaa Evermusic- tai Flacbox-sovellus ja siirry **Yhteydet**-välilehdelle.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Yhteydet-välilehti Evermusicissa" width="600" >}}

2. Automaattista yhteyttä varten etsi Synology NAS **Saatavilla olevat laitteet** -osiosta ja napauta sitä yhdistääksesi.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Saatavilla olevien laitteiden lista" width="600" >}}

3. Manuaalista yhteyttä varten valitse **Yhdistä pilvipalvelu** ja valitse **WebDAV**. Syötä palvelimen osoite muodossa: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (esim. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Manuaalinen WebDAV-konfiguraatio" width="600" >}}

4. Jätä kirjautumis- ja salasanakentät tyhjiksi vieraskäyttöä varten, tai syötä Synology-tunnuksesi. Napauta **Kirjaudu sisään**.

## Vaihe 6: Selaa ja toista musiikkia

1. Kun yhteys on muodostettu, laite näkyy **Liitetyt lisävarusteet** -listassa.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Yhdistetyt laitteet Evermusicissa" width="600" >}}

2. Siirry **Musiikki**-kansioon ja napauta mitä tahansa äänitiedostoa aloittaaksesi toiston.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Musiikkikansion selaus" width="600" >}}

## Vaihe 7: Lisää yhdistetty pilvikansio musiikkikirjastoon

1. Avaa **Musiikkikirjasto**-osio sovelluksessa.
2. Valitse **Lisää musiikkia** ja valitse **Yhteydet**.
3. Valitse yhdistetty NAS-palvelin ja valitse **Musiikki**-kansio. Napauta **Valmis**.
4. Sovellus skannaa musiikkikansion ja lisää tuetut äänitiedostot musiikkikirjastoon. Metatiedot ladataan ja kappaleet ryhmitellään albumin, esittäjän ja genren mukaan.

## Yhteenveto

Näitä ohjeita noudattamalla voit helposti asettaa WebDAV-yhteyden Synology NAS:iin ja suoratoistaa musiikkikirjastosi iPhonelle tai Macille Evermusicin tai Flacboxin avulla. Nauti saumattomasta pääsystä suosikkikappaleisiisi milloin tahansa.

## UKK

{{% details title="Mitkä NAS-laitteet tukevat WebDAV:ia?" closed="true" %}}
Useimmat suositut NAS-merkit tukevat WebDAV:ia, mukaan lukien Synology, QNAP, TrueNAS ja Western Digital. Tarkista NAS-valmistajasi dokumentaatiosta WebDAV:n asennusohjeet.
{{% /details %}}

{{% details title="Mikä on WebDAV:n ja SMB:n ero NAS-musiikin suoratoistossa?" closed="true" %}}
WebDAV toimii HTTP/HTTPS-protokollan kautta ja soveltuu paremmin etäkäyttöön Internetin kautta. SMB on tyypillisesti nopeampi paikallisverkoissa. Evermusic ja Flacbox tukevat molempia protokollia, joten valitse sen mukaan, tarvitsetko paikallista vai etäkäyttöä.
{{% /details %}}

{{% details title="Tarvitsenko käyttäjätunnuksen ja salasanan WebDAV:lle Synologyssä?" closed="true" %}}
Et, jos otat käyttöön anonyymin WebDAV-käytön ja määrität vieraskäyttöoikeudet jaetulle kansiolle. Parempaa turvallisuutta varten voit käyttää Synology-tunnuksiasi.
{{% /details %}}

{{% details title="Voinko suoratoistaa FLAC:ia ja muita korkean resoluution formaatteja NAS:sta WebDAV:n kautta?" closed="true" %}}
Kyllä. Sekä Evermusic että Flacbox tukevat FLAC-, ALAC-, WAV-, DSD- ja muita korkean resoluution formaatteja suoratoistettaessa NAS-tallennustilasta WebDAV:n kautta.
{{% /details %}}

{{% details title="Miksi sovellus ei löydä NAS:iani Saatavilla olevista laitteista?" closed="true" %}}
Varmista, että iPhone/Mac ja NAS ovat samassa Wi-Fi-verkossa. Jos automaattinen löytäminen ei toimi, käytä manuaalista yhteysasetusta ja syötä NAS:n IP-osoite ja WebDAV-portti suoraan.
{{% /details %}}
