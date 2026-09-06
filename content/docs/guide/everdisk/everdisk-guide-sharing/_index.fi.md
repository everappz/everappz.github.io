---
title: "Jakaminen"
date: 2026-08-20
description: "Opi, miten jakaminen toimii Everdiskissa: napauta Aloita ja muuta iPhone tai iPad langattomaksi asemaksi, valitse mita jaat (tiedostot, kansiot, kuvat ja musiikki), pyorita neljaa palvelinta (DLNA, HTTP, WebDAV, FTP), lue yhteysosoitteet, nae kuka on yhdistettyna ja pida jakaminen kaynnissa Wi-Fin tai USB-kaapelin kautta."
keywords: ["Everdisk jakaminen", "langaton asema iPhone", "aloita jakaminen", "jaa tiedostoja iPhone", "jaa kuvia verkossa", "DLNA HTTP WebDAV FTP", "mita jaetaan", "miten yhdistetaan", "pida sovellus auki", "Wi-Fi tai USB-kaapeli jakaminen"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


**Jakaminen**-valilehti on Everdiskin sydan. Sielta muutat iPhonen tai iPadin langattomaksi asemaksi, valitset tarkalleen mita haluat jakaa ja saat osoitteet, joilla muut laitteet yhdistyvat. Tama on ensimmainen valilehti, jonka naet sovelluksen avatessasi.

## Aloita ja lopeta jakaminen

Jakaminen-nayton keskella on suuri pyorea painike.

- Napauta **Aloita**, niin kaikki kaytossa olevat palvelimesi tulevat verkkoon yhta aikaa. Painikkeessa lukee **Kaynnistetaan...** ja sen jalkeen **Lopeta**, kun jakaminen on kaynnissa.
- Napauta **Lopeta**, niin kaikki poistuu jalleen verkosta. Yhdistetyt laitteet katkaistaan.

Jakamisen ollessa kaynnissa valitsemasi tiedostot, kuvat ja musiikki ovat kaikkien samassa verkossa olevien laitteiden kaytettavissa, kun ne yhdistyvat jollakin alla olevista neljasta tavasta.

> Jakaminen toimii vain sovelluksen ollessa auki. Katso **Pida sovellus auki** taman sivun lopusta selitys sille, miksi nain on ja miten pidat suuret siirrot kaynnissa.

## Valitse mita jaat

Ennen aloittamista napauta **Mita jaetaan** -otsikkoa avataksesi kolme ryhmaa. Voit jakaa niita missa tahansa yhdistelmassa, ja sinun on valittava vahintaan yksi asia ennen kuin jakaminen voi alkaa.

**Tiedostot ja kansiot**

- Sovelluksesi oma **Asiakirjat**-kansio jaetaan oletuksena. Voit halutessasi lopettaa sen jakamisen.
- Napauta **Lisaa kansio** jakaaksesi kansion mista tahansa laitteeltasi, tai **Lisaa tiedosto** jakaaksesi yksittaisia tiedostoja.
- Jokaisella jaetulla kohteella on **Tiedot**-painike ja **Lopeta jakaminen** -painike.

**Kuvat ja videot**

- Ota kayttoon **Salli paasy koko kuvakirjastoon** jakaaksesi koko kuva- ja videokirjastosi, tai
- Napauta **Lisaa kuvia** ja poimi kasin vain ne kuvat ja videot, jotka haluat jakaa.

**Musiikki**

- Ota kayttoon **Salli paasy koko musiikkikirjastoon** jakaaksesi koko musiikkikirjastosi, tai
- Napauta **Lisaa kappaleita** jakaaksesi vain valitut kappaleet.
- Suojattuja (DRM) tai vain pilveen tallennettuja kappaleita ei voi jakaa.

Jos yritat aloittaa ilman mitaan valittua, Everdisk nayttaa **Ei mitaan jaettavaa** -huomautuksen. Jos muutat jaettavaa jakamisen ollessa kaynnissa, **lopeta ja aloita uudelleen** ottaaksesi muutoksen kayttoon.

## Neljä palvelinta

Everdisk jakaa saman sisallon neljalla tavalla yhta aikaa. Jokainen niista on suunniteltu erilaiselle laitteelle, ja jokaisen voi kytkea paalle tai pois kohdassa **Asetukset -> Jakaminen -> Yhteydet**. Oletuksena kaikki nelja ovat paalla.

- **TV ja mediakeskus (DLNA)** - alytelevisioille ja mediasoittimille. Ne loytavat laitteesi itse ja nayttavat kuvasi, videosi ja musiikkisi esikatselukuvien kera.
- **Selain (HTTP)** - mille tahansa puhelimelle, tabletille tai tietokoneelle. Toinen henkilo avaa linkin verkkoselaimessa selatakseen ja ladatakseen tiedostojasi. Mitaan ei tarvitse asentaa.
- **Tietokone (WebDAV)** - Macille, Windows-PC:lle tai Linux-koneelle. Laitteesi nakyy tavallisena verkkoasemana, joten voit vetaa tiedostoja molempiin suuntiin.
- **Muut sovellukset ja laitteet (FTP)** - tiedostosovelluksille ja tehokayttajille, jotka puhuvat FTP:ta.

Vaiheittaiset yhteysohjeet jokaiselle tyypille loydat sivulta [Yhdista laitteesi](/docs/guide/everdisk/everdisk-guide-connect).

## Miten yhdistetaan ja yhteysosoitteet

Kun napautat Aloita, **Miten yhdistetaan** -osio nayttaa kortin jokaiselle aktiiviselle palvelimelle ja tarkan **osoitteen**, joka syotetaan toiseen laitteeseen. Jokainen osoite on helppo kopioida - napauta sita kopioidaksesi, kayta **Jaa**-painiketta lahettaaksesi sen tai napauta **tiedot (ⓘ)** -painiketta saadaksesi yksityiskohtaiset, protokollakohtaiset ohjeet.

- DLNA-kortti nayttaa laitteen kuvausosoitteen, joka paattyy muotoon `/device-desc.xml` niita soittimia varten, jotka sita pyytavat.
- Kun laitteesi on kytketty Maciin kaapelilla, esiin tulee lisaosoite **Kaapeliyhteys**-merkinnalla, joka kayttaa laitteesi `.local`-nimea.

Voit myos avata osoitteen **QR-koodina**, jotta toisen laitteen kamera paasee suoraan siihen.

## Kuka on yhdistettyna

**Kuka on yhdistettyna** -osio listaa reaaliajassa laitteet, jotka ovat parhaillaan yhdistettyna sinuun. Napauta lisaa toimintoja -painiketta minka tahansa laitteen vieressa ja valitse **Esta tama laite**, jos et tunnista sita. Estettyja laitteita hallitaan kohdassa [Kaytto ja yksityisyys](/docs/guide/everdisk/everdisk-guide-access).

## Laitteesi nimi ja avatar

Jokaisella laitteella on ystavallinen nimi (kuten "Speedy-Hare") ja varillinen avatar. Tama on nimi, jonka TV, tietokone tai muu sovellus nayttaa laitteellesi verkossa, joten se on helppo erottaa. Voit luoda nimen ja avatarin uudelleen ilmaiseksi tai asettaa mukautetun nimen, kuvakkeen tai valokuva-avatarin Premiumilla. Katso [Asetukset](/docs/guide/everdisk/everdisk-guide-settings).

## Jakaminen Wi-Fin tai USB-kaapelin kautta

Jakaminen voi toimia kahdessa tilanteessa:

- **Wi-Fin kautta** - laitteesi ja muut laitteet ovat samassa Wi-Fi-verkossa.
- **USB-kaapelin kautta** - laitteesi on kytketty **Maciin** kaapelilla, vaikka Wi-Fia ei olisi lainkaan. Tama on nopeampaa kuin Wi-Fi ja toimii edelleen lentokoneessa, hotellissa tai lukitussa verkossa.

Jos kaytettavissa ei ole Wi-Fia eika kaapelia, **Aloita**-painike on pois kaytosta ja esiin tulee **Ei Wi-Fi-yhteytta** -huomautus. Jos yhteys katkeaa jakamisen aikana, Everdisk lopettaa jakamisen automaattisesti ja ilmoittaa siita. Napauta minka tahansa naista huomautuksista tiedot-painiketta saadaksesi taydellisen selityksen.

## Pida sovellus auki

Koska iPhone tai iPad toimii palvelimena, **jakaminen toimii vain, kun Everdisk on auki naytolla**. Jos suljet sovelluksen tai lukitset laitteen pitkaksi aikaa, jarjestelma voi keskeyttaa sovelluksen ja jakaminen loppuu.

Suuria siirtoja varten:

- Pida Everdisk auki ja etualalla.
- Kytke laitteesi virtalahteeseen.
- Aseta **Automaattilukitus** arvoon **Ei koskaan** iOS-asetuksissa siirron ajaksi.

Voit ottaa kayttoon **Ilmoita ennen yhteyden katkaisua** (kohdassa Asetukset -> Jakaminen), jotta Everdisk muistuttaa avaamaan sovelluksen uudelleen ennen kuin jarjestelma keskeyttaa sen. Napauta tiedot-painiketta **Pida sovellus auki** -bannerissa saadaksesi lisatietoja.

## Seuraavat vaiheet

- [Yhdista laitteesi](/docs/guide/everdisk/everdisk-guide-connect) - yhdista TV, tietokone, selain, puhelin tai USB-kaapeli.
- [Kaytto ja yksityisyys](/docs/guide/everdisk/everdisk-guide-access) - lisaa salasana ja hallitse muokkausta.
- [Asetukset](/docs/guide/everdisk/everdisk-guide-settings) - kytke palvelimet paalle tai pois ja saada laatua.
