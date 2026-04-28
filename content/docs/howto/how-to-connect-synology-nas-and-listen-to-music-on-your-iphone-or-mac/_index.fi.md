---
title: "Kuinka yhdistää Synology NAS ja kuunnella musiikkia iPhonella tai Macilla"
date: 2024-09-19
description: "Opi yhdistämään Synology NAS käyttämällä natiivia API:a tai QuickConnectia ja suoratoistamaan korkealaatuista musiikkia iPhonelle tai Macille Evermusicin ja Flacboxin avulla."
keywords: ["synology nas", "suoratoista musiikkia", "quickconnect", "evermusic synology", "flacbox synology", "nas musiikkisoitin", "iphone nas musiikki"]
tags: ["musiikki", "suoratoisto", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Tiivistelmä:** Yhdistä Synology NAS Evermusiciin tai Flacboxiin käyttämällä Synologyn natiivia API:a -- joko manuaalisesti IP-osoitteen kautta tai automaattisesti QuickConnect ID:n avulla. QuickConnect mahdollistaa musiikin suoratoiston etänä ilman porttien uudelleenohjausta. Molemmat sovellukset tukevat FLAC-, MP3-, WAV- ja muita korkean resoluution formaatteja.

Jos etsit saumatonta tapaa yhdistää Synology NAS ja nauttia musiikkikirjastostasi iPhonella tai Macilla, Evermusic ja Flacbox ovat täydelliset ratkaisut. Nämä sovellukset tukevat laajaa valikoimaa äänimuotoja, mukaan lukien FLAC, MP3 ja WAV, mikä tekee korkealaatuisen musiikin suoratoistosta ja kuuntelusta helppoa suoraan Synology NAS:stasi.

Tässä oppaassa näytämme, kuinka yhdistät Synology NAS:si Evermusic- tai Flacbox-sovellukseen käyttämällä Synologyn natiivia API:a ja QuickConnect-ominaisuutta. Hyödyntämällä Synologyn suoraa API:a voit turvallisesti käyttää musiikkikirjastoasi kotiverkkosi ulkopuolelta ilman monimutkaisia määrityksiä kuten WebDAV, SMB, DLNA. QuickConnectin avulla voit suoratoistaa ja hallita musiikkiasi mistä tahansa iPhonella tai Macilla.

## Vaihe 1: Jaetun kansion käyttöoikeuksien määrittäminen (valinnainen)

1. Avaa **Ohjauspaneeli** ja siirry **Jaettu kansio** -osioon.

![Jaettu kansio](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Valitse **Musiikki**-kansio ja napsauta **Muokkaa**.

3. **Käyttöoikeudet**-välilehdellä määritä käyttöoikeudet. Ota vieraskäyttö käyttöön vain luku -oikeudella, jos tarvitset vain kuunnella musiikkia, tai luku/kirjoitus-oikeudella, jos tarvitset muokata tiedostoja. Tallenna muutokset.

![Käyttöoikeudet](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Vaihe 2: Synology NAS:n IP-osoitteen löytäminen

1. Avaa **Ohjauspaneeli** ja siirry **Verkkoliittymä**-välilehdelle.

![Verkkoliittymä](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Tai käytä verkkoselaintasi ja siirry osoitteeseen [find.synology.com](http://find.synology.com).

![Etsi Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Merkitse muistiin Synology NAS:si IP-osoite (esim. 192.168.18.137).

## Vaihe 3: Synology NAS:n verkkoporttien löytäminen

Löydät Synologyn virallisen dokumentaation DSM:n oletusverkkoporteista tästä [Synology Knowledge Center -artikkelista](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM käyttää seuraavia oletusportteja:
- **HTTP (Verkkokäyttö):** Portti **5000**
- **HTTPS (Suojattu verkkokäyttö):** Portti **5001**

Nämä ovat oletusportit DSM-käyttöliittymän käyttöön.

![Verkkoportit](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Vaihe 4: QuickConnect ID -ominaisuuden käyttöönotto

Synology QuickConnect ID on yksilöllinen tunniste, jonka avulla voit käyttää Synology NAS:iasi etänä internetin kautta ilman monimutkaisten verkkoasetusten, kuten porttien uudelleenohjauksen, määrittämistä. QuickConnect yksinkertaistaa etäkäytön käyttämällä Synologyn palvelimia yhteyden muodostamiseen NAS:si ja laitteesi, kuten älypuhelimen tai tietokoneen, välillä QuickConnect ID:n kautta.

**QuickConnect ID:n löytäminen tai määrittäminen:**

1. **Kirjaudu DSM:ään.**
2. Siirry kohtaan **Ohjauspaneeli > Ulkoinen käyttö > QuickConnect**.
3. **Ota QuickConnect käyttöön** ja luo tai tarkastele yksilöllistä QuickConnect ID:täsi.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Vaihe 5: Yhdistä Synology NAS:iin iPhonella/Macilla käyttäen Evermusicia tai Flacboxia

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) ja [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) ovat musiikkisoitinsovelluksia, jotka on suunniteltu iOS- ja macOS-laitteille, ja kumpikin tarjoaa ainutlaatuisia ominaisuuksia musiikkikirjastosi hallintaan ja nauttimiseen.

1. Avaa Evermusic tai Flacbox ja siirry **Yhteydet**-välilehdelle.

![Yhteydet](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Valitse **Yhdistä pilvipalvelu** ja valitse **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Sinulla on kaksi yhteysvaihtoehtoa: **manuaalinen** käyttäen palvelimen IP-osoitetta ja porttia, tai **automaattinen** QuickConnect ID:n kautta.

### Manuaalinen yhteys

Manuaalisessa menetelmässä tarvitset suoran IP-osoitteen ja porttinumeron, jotka sait edellisissä vaiheissa.

1. Syötä palvelimen URL, jonka sait vaiheessa 2, seuraavassa muodossa: PROTOKOLLA://IP_OSOITE:PORTTINUMERO
   - Käytä **porttia 5000** HTTP:lle ja **porttia 5001** HTTPS-yhteyksille.

   Esimerkiksi:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Todellinen porttinumero voidaan vahvistaa vaiheessa 3.
3. Syötä **käyttäjätunnuksesi** ja **salasanasi** Synology NAS:lle.
4. Napauta **Kirjaudu sisään** yhteyden muodostamiseksi.

![Manuaalinen yhteys](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automaattinen yhteys

Automaattisessa yhteydessä käytät **QuickConnect ID:tä** vaiheesta 4. IP-osoitteen ja porttinumeron manuaalisen syöttämisen sijaan syötä vain **QuickConnect ID**. Sovellus hakee automaattisesti tarvittavat yhteystiedot.

Tämä menetelmä mahdollistaa NAS:si käytön etänä, myös kotiverkkosi ulkopuolelta, joten voit hallita tiedostojasi internetistä ilman porttien uudelleenohjauksen tai staattisten IP-osoitteiden määrittämistä.

![Automaattinen yhteys](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Kaksivaiheinen todennus

DSM 4.2:sta alkaen Synology otti käyttöön **kaksivaiheisen vahvistuksen** turvallisuuden parantamiseksi. Tämä ominaisuus vaatii **kertakäyttösalasanan (OTP)** koodin, joka luodaan todennussovelluksella, tavallisten kirjautumistietojen lisäksi. Jos olet ottanut kaksivaiheisen vahvistuksen käyttöön, käyttäjätunnuksen ja salasanan syöttämisen jälkeen sinun on myös syötettävä OTP kirjautuaksesi DSM-istuntoon.

Huomaa, että istunnon vanhentuessa sovellus on valtuutettava uudelleen manuaalisesti. Uudelleenvaltuuttamiseksi:

1. Siirry sovelluksen **Yhteydet**-välilehdelle.
2. Napauta **Lisää toimintoja** -painiketta palvelimen nimen vieressä.
3. Valitse **Asetukset** valikosta syöttääksesi uuden todennuskoodin ja suorittaaksesi uudelleenvaltuutusprosessin loppuun.

Tämä varmistaa, että vaikka käyttäisit NAS:iasi epäluotettavasta verkosta, tietosi pysyvät turvassa.

## Vaihe 6: Selaa ja toista musiikkia

1. Yhdistämisen jälkeen laite näkyy **Yhdistetyt laitteet** -luettelossa.

![Yhdistetyt laitteet](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Siirry **Musiikki**-kansioon ja napauta mitä tahansa äänitiedostoa aloittaaksesi toiston.

![Toista musiikkia](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Vaihe 7: Yhdistetyn pilvikansion lisääminen musiikkikirjastoon

1. Avaa sovelluksen **Musiikkikirjasto**-osio.
2. Valitse **Lisää musiikkia** ja valitse **Yhteydet**.
3. Valitse yhdistetty NAS-palvelin ja valitse **Musiikki**-kansio. Napauta **Valmis**.
4. Sovellus skannaa musiikkikansion ja lisää tuetut äänitiedostot musiikkikirjastoon. Metatiedot ladataan ja kappaleet ryhmitellään albumin, esittäjän ja genren mukaan.

## Yhteenveto

Näitä vaiheita noudattamalla voit helposti luoda yhteyden Synology NAS:iin ja suoratoistaa koko musiikkikirjastosi iPhonelle tai Macille Evermusicin tai Flacboxin avulla. Olipa kotona tai liikkeellä, nauti saumattomasta, korkealaatuisesta pääsystä suosikkikappaleisiisi mistä tahansa QuickConnectin avulla. Hyödynnä joustavuutta ja mukavuutta, joita nämä sovellukset tarjoavat, ja aloita musiikkikokoelmasi hallinta helposti kaikilla laitteillasi.

Turvallisen etäkäytön QuickConnectin kautta ja laajan äänimuototuen ansiosta et ole koskaan kaukana musiikistasi. Nyt NAS:lle tallennetut tiedostosi ovat vain napauttamisen päässä!

## Usein kysytyt kysymykset

{{% details title="Mikä on ero manuaalisen yhteyden ja QuickConnectin välillä?" closed="true" %}}
Manuaalinen yhteys käyttää NAS:n IP-osoitetta ja porttia, joka toimii paikallisverkossasi. QuickConnect käyttää Synologyn välityspalvelua yhteyden muodostamiseen mistä tahansa internetin kautta, ilman porttien uudelleenohjausta.
{{% /details %}}

{{% details title="Voinko suoratoistaa musiikkia Synology NAS:sta kotiverkkoni ulkopuolella?" closed="true" %}}
Kyllä. Ota QuickConnect käyttöön Synology NAS:ssasi ja käytä QuickConnect ID:tä Evermusicissa tai Flacboxissa musiikin suoratoistoon mistä tahansa internetyhteydellä.
{{% /details %}}

{{% details title="Mitä äänimuotoja tuetaan suoratoistettaessa Synology NAS:sta?" closed="true" %}}
Evermusic ja Flacbox tukevat FLAC-, MP3-, AAC-, WAV-, ALAC-, OGG-, WMA-, DSD- ja monia muita formaatteja. Kaikki tuetut formaatit toimivat suoratoistettaessa Synology NAS:sta.
{{% /details %}}

{{% details title="Tarvitsenko kaksivaiheisen todennuksen yhdistämiseen?" closed="true" %}}
Ei, kaksivaiheinen todennus on valinnainen. Jos olet kuitenkin ottanut kaksivaiheisen vahvistuksen käyttöön Synology DSM:ssäsi, sovellus pyytää kertakäyttösalasanaa kirjautumisen yhteydessä. Sinun on valtuutettava uudelleen, kun istunto vanhenee.
{{% /details %}}

{{% details title="Pitäisikö minun käyttää Synologyn natiivia API:a, WebDAV:ia vai SMB:tä yhdistämiseen?" closed="true" %}}
Synologyn natiivi API QuickConnectin kanssa on paras valinta etäkäyttöön. Paikallisverkon käyttöön SMB on tyypillisesti nopein vaihtoehto. WebDAV toimii hyvin sekä paikalliseen että etäkäyttöön. Evermusic ja Flacbox tukevat kaikkia kolmea protokollaa.
{{% /details %}}
