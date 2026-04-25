---
title: "Musiikkikirjaston siirtäminen laitteiden välillä Evermusicissa: vaiheittainen opas"
description: "Siirrä helposti Evermusic-musiikkikirjastosi, soittolistat, albumin kansikuvat ja asetukset iPhonesta, iPadista tai Macista toiseen Wi-Fi Driven ja varmuuskopiointityökalujen avulla."
date: 2024-12-29
tags: ["musiikkikirjasto", "siirto", "wifi", "varmuuskopio", "webdav", "palautus"]
keywords: ["siirrä musiikkikirjasto Evermusic", "varmuuskopioi ja palauta soittolistat Evermusic", "Evermusic WiFi Drive", "synkronoi Evermusic laitteiden välillä", "siirrä Evermusic-tietokanta", "Evermusic tiedostojen siirto", "palauta äänisoittimen asetukset", "WebDAV musiikkisiirto iOS"]
readingTime: 3
---

{{< author-byline >}}


**Lyhyesti:** Siirtääksesi Evermusic-kirjastosi uuteen laitteeseen, luo varmuuskopio lähdelaitteella, käynnistä Wi-Fi Drive, yhdistä toinen laite samaan verkkoon, lataa varmuuskopio ja musiikkitiedostot ja palauta sitten varmuuskopiosta. Koko prosessi kestää noin 10 minuuttia kirjaston koosta riippuen.

Tässä oppaassa opastamme sinut koko musiikkikirjastosi siirtämisessä — mukaan lukien tietokanta, albumin kansikuvat ja asetukset — yhdestä laitteesta (iPhone tai Mac) toiseen. Vaikka automaattinen musiikkikirjaston ja soittolistojen synkronointi on tulevaisuuteen suunniteltu ominaisuus, tämä prosessi on tällä hetkellä tehtävä manuaalisesti.

## Vaihe 1: Luo varmuuskopio ensimmäisellä laitteella

1. **Avaa sovellus ensimmäisellä laitteellasi** (se, jossa on musiikkikirjastosi, soittolistat ja yhdistetyt pilvipalvelut).
2. **Siirry kohtaan Asetukset** ja valitse **Varmuuskopiointi ja palautus**.

![Varmuuskopiointi ja palautus](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. **Varmuuskopiointi ja palautus** -näytöllä valitse varmuuskopiotiedostoon sisällytettävät kohteet:
   - **Tietokanta** (sisältää musiikkikirjastosi ja soittolistat)
   - **Albumin kansikuvat**
   - **Asetukset**

Nämä vaihtoehdot ovat oletuksena käytössä.

![Varmuuskopiointivaihtoehdot](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Napauta **Varmuuskopioi sovelluksen tiedot** aloittaaksesi prosessin.

![Varmuuskopioi sovelluksen tiedot](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Kun varmuuskopiointi on valmis, näkyviin tulee tiedotusilmoitus.

![Varmuuskopiointi valmis](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Napauta **Näytä tiedosto** paljastaaksesi varmuuskopiotiedoston **Asiakirjat**-hakemistossa. Varmuuskopiotiedostot tallennetaan yleensä **Backup**-kansioon.

![Näytä varmuuskopiotiedosto](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Vaihe 2: Käynnistä Wi-Fi Drive -palvelin

1. Siirry sovelluksen **Yhteydet**-osioon.
2. Vieritä alas kohtaan **Yhdistä Wi-Fin kautta** ja napauta sitä.

![Yhdistä Wi-Fin kautta](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Seuraavalla näytöllä napauta **Käynnistä Wi-Fi Drive**.

- Vaihtoehtoisesti voit asettaa käyttäjätunnuksen ja salasanan turvallisuuden vuoksi, mutta tämä on tarpeetonta kotiverkoissa.

4. Käynnistyksen jälkeen näet käytettävissä olevat palvelinosoitteet. Tätä voidaan käyttää työpöytäselaimille tai WebDAV-sovelluksille, mutta tässä oppaassa jatkamme suoraan seuraaviin vaiheisiin.

![Wi-Fi Drive käynnistetty](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Vaihe 3: Yhdistä toinen laitteesi ensimmäiseen

1. Avaa sovellus toisella laitteellasi (johon haluat siirtää kirjaston).
2. Varmista, että molemmat laitteet ovat yhdistettynä samaan Wi-Fi-verkkoon.
3. Toisella laitteella avaa **Yhteydet**-välilehti ja valitse **Saatavilla olevat laitteet**.

![Saatavilla olevat laitteet](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Sinun pitäisi nähdä WebDAV-yhteys nimeltä **Evermusic** (palvelin, jonka käynnistimme ensimmäisellä laitteella). Napauta sitä yhdistääksesi.

5. Yhdistämisen jälkeen näet kaikki kansiot ensimmäiseltä laitteelta.

![Yhdistetty ensimmäiseen laitteeseen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Vaihe 4: Valmistaudu tiedostojen siirtoon

1. Toisella laitteella siirry kohtaan **Asetukset > Tiedostonhallinta** ja ota käyttöön **Tallenna ladatut tiedostot kohteeseen - Kysy joka kerta**.

- Tämä varmistaa, että voit valita kohdekansion jokaiselle lataukselle.

2. Palaa **Yhteydet**-välilehteen ja siirry yhdistettyyn WebDAV-palvelimeen.

![Valmistaudu tiedostojen siirtoon](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Vaihe 5: Siirrä varmuuskopio ja musiikkitiedostot

1. Avaa **Backup**-kansio yhdistetyllä WebDAV-palvelimella.

![Varmuuskopiokansio](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Napauta **Lisää toimintoja** -painiketta (kolme pistettä) varmuuskopiotiedoston vieressä ja valitse **Ladata**.

3. Luo **Backup**-kansio toiselle laitteelle ladattujen tiedostojen tallentamista varten. Vahvista valintasi napauttamalla **Valmis**.

![Lataa varmuuskopio](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Siirrä mahdolliset lisämusiikkitiedostot:
   - Tarkista **Lataukset**-kansio tai muut olennaiset kansiot WebDAV-palvelimella.

![Siirrä musiikkitiedostot](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Käytä **Valita**-vaihtoehtoa tiedostojen valitsemiseen ja napauta sitten **Lisää toimintoja > Ladata**. Tallenna ne vastaavaan kansioon toisella laitteella säilyttääksesi saman hakemistorakenteen.

Tavoitteena on siirtää kaikki tiedostot ensimmäiseltä laitteeltasi nykyiselle laitteellesi varmistaen, että kansiorakenne pysyy identtisenä. Tällä tavoin musiikkikirjastosi ja soittolistojesi linkit pysyvät ehjinä. Huomaa, että ensimmäisen laitteesi sovelluksen Asiakirjat-hakemiston ulkopuolelle tallennetut paikalliset tiedostot on siirrettävä erikseen. Koska sovellus ei voi käyttää näitä tiedostoja Wi-Fi Drive -tilassa, sinun on käytettävä järjestelmän Tiedostot-sovellusta niiden siirtämiseen.

![Siirto valmis](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Vaihe 6: Seuraa siirron edistymistä

1. Toisella laitteella siirry **Paikalliset tiedostot** -osioon (tai **Lataukset**-välilehteen iPadilla/Macilla).

2. Napauta **Siirtoaktiviteetti**-painiketta vasemmassa yläkulmassa seurataksesi siirtojonoa.

![Seuraa siirtoa](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Vaihe 7: Palauta tiedot varmuuskopiosta

1. Kun varmuuskopiotiedosto ja kaikki tarvittavat äänitiedostot on ladattu toiselle laitteelle, avaa **Backup**-kansio.

2. Napauta varmuuskopiotiedostoa, ja vahvistusviesti tulee näkyviin.

![Palauta varmuuskopio](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Huomautus:** Palautus korvaa kaikki nykyiset musiikkikirjaston tiedot, soittolistat, asetukset ja albumin kansikuvat varmuuskopion tiedoilla.

3. Napauta **Palauta** aloittaaksesi prosessin.

![Palautusprosessi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Palautuksen valmistuttua ilmoitus vahvistaa onnistumisen.

![Palautus valmis](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Tarkista **Soittolistat**- tai **Musiikkikirjasto**-osiot palautuksen vahvistamiseksi.

![Vahvista palautus](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Vaihe 8: Indeksoi musiikkikirjasto uudelleen

1. Parhaan tuloksen saamiseksi indeksoi kirjastosi uudelleen varmistaaksesi, että kaikki tiedostot havaitaan onnistuneesti.

2. Siirry kohtaan **Asetukset > Musiikkikirjasto > Offline-musiikin synkronointi** ja valitse **Aloita paikallisten kansioiden skannaus**.

Noudattamalla näitä vaiheita siirrät onnistuneesti musiikkikirjastosi, soittolistasi ja asetuksesi toiselle laitteelle. Jos kohtaat ongelmia, älä epäröi ottaa yhteyttä tukeen.

## Usein kysytyt kysymykset

{{% details title="Voinko siirtää Evermusic-kirjastoni ilman Wi-Fiä?" closed="true" %}}
Wi-Fi Drive vaatii molempien laitteiden olevan samassa Wi-Fi-verkossa. Bluetooth- tai mobiilisiirtovaihtoehtoa ei tällä hetkellä ole. Voit vaihtoehtoisesti käyttää AirDropia tai Tiedostot-sovellusta varmuuskopiotiedoston ja musiikkikansioiden manuaaliseen siirtämiseen laitteiden välillä.
{{% /details %}}

{{% details title="Siirtyvätkö pilvipalveluyhteydet varmuuskopion mukana?" closed="true" %}}
Varmuuskopio sisältää tietokantasi, soittolistat, albumin kansikuvat ja asetukset. Pilvipalveluiden kirjautumistietoja ei sisällytetä turvallisuussyistä. Sinun on yhdistettävä pilvitilit uudelleen uudella laitteella palautuksen jälkeen.
{{% /details %}}

{{% details title="Mitä tapahtuu olemassa olevalle kirjastolleni toisella laitteella?" closed="true" %}}
Varmuuskopion palauttaminen korvaa kaikki olemassa olevat musiikkikirjaston tiedot, soittolistat, asetukset ja albumin kansikuvat toisella laitteella. Tee erillinen varmuuskopio toisesta laitteesta ensin, jos haluat säilyttää sen tiedot.
{{% /details %}}

{{% details title="Toimiiko tämä prosessi iPhonen ja Macin välillä?" closed="true" %}}
Kyllä. Evermusic tukee Wi-Fi Drive -siirtoa minkä tahansa iPhonen, iPadin ja Macin yhdistelmän välillä. Molempien laitteiden tarvitsee vain olla samassa Wi-Fi-verkossa.
{{% /details %}}

{{% details title="Kuinka kauan siirto kestää?" closed="true" %}}
Siirtoaika riippuu musiikkikirjastosi koosta ja Wi-Fi-nopeudestasi. Tyypillinen muutaman gigatavun kirjasto siirtyy 5-15 minuutissa tavallisen kotiverkon kautta.
{{% /details %}}
