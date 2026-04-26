---
title: "Kuinka tuoda M3U-soittolista Evermusiciin ja Flacboxiin"
date: 2024-01-31
description: "Opi tuomaan M3U-, M3U8- ja CUE-soittolistatiedostoja pilvestä, paikallisesta tallennustilasta tai laitteesta Evermusiciin ja Flacboxiin."
keywords: ["evermusic", "flacbox", "soittolista", "m3u", "m3u8", "cue", "tuonti", "musiikkisovellus"]
tags: ["evermusic", "tuonti", "soittolistat", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Yhteenveto:** Evermusic ja Flacbox tukevat M3U-, M3U8- ja CUE-soittolistatiedostojen tuontia pilvitallennustilasta, sovelluksen paikallisista tiedostoista tai laitteestasi. Siirry kohtaan Soittolistat > Lisää > Tuo soittolista, valitse lähde, valitse tiedostosi, ja sovellus luo soittolistan automaattisesti.

M3U, joka tarkoittaa MP3 URL tai Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, on tietokonetiedostomuoto, jota käytetään multimediasoittolistoihin. Yksi sen pääkäyttötarkoituksista on luoda yhden merkinnän soittolistatiedostoja, jotka osoittavat internetin suoratoistoihin. Nämä tiedostot tarjoavat kätevän pääsyn suoratoistosisältöön, ja niitä käytetään yleisesti latauksiin, sähköpostiin ja internetradion kuunteluun.

Laajasta käytöstään huolimatta M3U-muodolle ei ole virallista määrittelyä; siitä on tullut de facto -standardi. M3U-tiedosto on olennaisesti tavallinen tekstitiedosto, joka määrittää yhden tai useamman mediatiedoston sijainnit. Koodauksesta riippuen se tallennetaan joko "m3u"- tai "m3u8"-tiedostopäätteellä. Jokainen tiedoston merkintä määrittää mediatiedoston sijainnin, joka voi olla absoluuttinen paikallinen polkunimi, M3U-tiedoston sijaintiin nähden suhteellinen paikallinen polkunimi tai URL. Merkinnät erotetaan rivinvaihdoilla, ja jotkut laitteet vaativat CR LF -muotoisia rivinvaihtoja.

Lisäksi M3U-tiedostot voivat sisältää "#"-merkillä alkavia kommentteja. Laajennetussa M3U:ssa "#" esittelee laajennettuja M3U-direktiivejä, jotka voivat tukea kaksoispisteellä ":" päättyviä parametreja.

Evermusic- ja Flacbox-sovelluksissamme olemme toteuttaneet M3U-tiedostojen tuontitoiminnon, mikä poistaa tarpeen luoda soittolistoja manuaalisesti. Tämä opas opastaa sinua soittolistojesi tuomisessa pilvitallennustilasta, paikallisista tiedostoista tai laitteesi tiedostoista suoraan sovellukseen.

Siirry ensin 'Soittolistat'-osioon. Napauta seuraavaksi oikeassa yläkulmassa olevaa 'Lisää'-painiketta. Valitse esiin tulevasta valikosta 'Tuo soittolista' -vaihtoehto.

![soittolistan tuontitoiminto](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Valitse seuraavalla näytöllä tiedoston sijainti. Tuetut vaihtoehdot ovat:

- Yhdistetty pilvitallennustila;
- Sovelluksen tiedostot;
- Laitteesi tiedostot;

![valitse tiedoston sijainti](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Valitaan yhdistetty pilvitallennustila ja avataan kansio, joka sisältää soittolistatiedoston. Tuetut soittolistatiedostopäätteet ovat M3U, M3U8 ja CUE. Valitse soittolistatiedosto ja napauta 'Valmis' vahvistaaksesi valintasi.

![valitse M3U-tiedosto](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Sovellus jäsentää soittolistatiedoston ja luo listan kappaleista. Sen jälkeen se paikantaa kyseiset tiedostot tallennustilasta ja kokoaa lopullisen soittolistan, joka tuodaan musiikkikirjastoon. On ratkaisevaa, että M3U/CUE-tiedostosi sisältää oikeat polut mediatiedostoille ja tiedostot sijaitsevat näissä poluissa tallennustilassasi.

![tuotu soittolista](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Sovellus tukee sekä suhteellisia polkuja että absoluuttisia tiedosto-URL-osoitteita.

Esimerkiksi:

Soittolista suhteellisilla poluilla:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Soittolista absoluuttisilla URL-osoitteilla:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Jos tuot soittolistatiedoston, joka sijaitsee sovelluksen sisällä (Paikalliset tiedostot -osio), lisävaiheita ei tarvita.

Jos kuitenkin haluat tuoda laitteellasi sijaitsevan soittolistan järjestelmän tiedostonvalitsimella, on tärkeä huomioitava seikka.

Tietoturvakäytäntöjen vuoksi sovellus voi käyttää vain järjestelmän tiedostonvalitsimella valitsemaasi tiedostoa. Soittolistatiedosto voi kuitenkin sisältää linkkejä muihin mediatiedostoihin laitteellasi. Tuodaksesi soittolistan laitteestasi sinun on valittava kansio, joka sisältää sekä soittolistatiedoston että kaikki siihen linkitetyt mediatiedostot. Tässä tapauksessa sovellus skannaa valitun kansion, löytää soittolistatiedoston, rakentaa kappaleluettelon ja tuo sen musiikkikirjastoon.

Lisäksi voit tuoda useita soittolistoja kerralla napauttamalla "Lisää toimintoja" -painiketta ja valitsemalla "Tuo soittolistat kansiosta". Sovellus skannaa sitten kansion sisällön, löytää tuetut soittolistatiedostot ja tuo ne kirjastoon.

## Usein kysytyt kysymykset

{{% details title="Mitä soittolistamuotoja Evermusic ja Flacbox tukevat?" closed="true" %}}
Molemmat sovellukset tukevat M3U-, M3U8- ja CUE-soittolistatiedostomuotoja. Nämä kattavat yleisimmät soittolistastandardit, joita musiikkisoittimet ja mediaohjelmistot käyttävät.
{{% /details %}}

{{% details title="Voinko tuoda soittolistoja pilvitallennustilasta?" closed="true" %}}
Kyllä. Voit tuoda soittolistatiedostoja mistä tahansa yhdistetystä pilvitallennuspalvelusta, mukaan lukien Google Drive, Dropbox, OneDrive ja WebDAV-palvelimet.
{{% /details %}}

{{% details title="Miksi jotkut kappaleet puuttuvat tuonnin jälkeen?" closed="true" %}}
Soittolistatiedoston on sisällettävä oikeat polut mediatiedostoihisi, ja näiden tiedostojen on oltava olemassa määritetyissä sijainneissa tallennustilassasi. Tarkista, että M3U- tai CUE-tiedostosi tiedostopolut vastaavat todellisia tiedostosijainteja.
{{% /details %}}

{{% details title="Voinko tuoda useita soittolistoja kerralla?" closed="true" %}}
Kyllä. Käytä Lisää toimintoja -painiketta ja valitse "Tuo soittolistat kansiosta". Sovellus skannaa kansion kaikki tuetut soittolistatiedostot ja tuo ne yhdellä kertaa.
{{% /details %}}

{{% details title="Pitääkö soittolistat luoda manuaalisesti?" closed="true" %}}
Ei. Tuontitoiminto poistaa manuaalisen soittolistojen luomisen tarpeen. Osoita sovellus vain olemassa olevaan M3U-, M3U8- tai CUE-tiedostoosi, ja se luo soittolistan automaattisesti.
{{% /details %}}
