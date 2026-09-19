---
title: "Yhdista laitteesi"
date: 2026-08-20
description: "Vaiheittaiset ohjeet Everdisk-langattomaan asemaan yhdistamiseen: katso alytelevisiosta DLNAn kautta, avaa tiedostosi missa tahansa verkkoselaimessa, liita laitteesi verkkoasemaksi Finderissa, Windowsissa tai Linuxissa WebDAVin tai SMB:n kautta (valinnaisella SMB3/AES-salauksella), yhdista tiedostosovelluksia FTP:n kautta ja siirra USB-kaapelilla Maciin ilman Wi-Fia."
keywords: ["yhdista Everdiskiin", "suoratoisto TV DLNA", "avaa tiedostot selaimessa", "liita verkkoasema Finder", "WebDAV Windows Linux", "FTP tiedostosovellus", "USB-kaapeli siirto Mac", "yhdista iPhone tietokoneeseen", "verkkoasema iPhone"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


Kun napautat **Aloita** [Jakaminen](/docs/guide/everdisk/everdisk-guide-sharing)-naytolla, muut laitteet voivat yhdistya tiedostoihisi viidella eri tavalla. Valitse tapa, joka sopii laitteelle, jota haluat kayttaa. Kaikissa tapauksissa tarvitsemasi tarkka **osoite** nakyy Jakaminen-nayton **Miten yhdistetaan** -osiossa.

> Molempien laitteiden on oltava **samassa Wi-Fi-verkossa** - tai Macin tapauksessa yhdistettyna **USB-kaapelilla** (katso viimeinen osio).

## Katso televisiosta (DLNA)

Kayta tata nayttaaksesi kuvia, videoita ja musiikkia alytelevisiossa tai mediasoittimessa.

1. Varmista kohdassa **Asetukset -> Jakaminen -> Yhteydet**, etta **TV ja mediakeskus** on paalla (se on oletuksena paalla).
2. Napauta Jakaminen-naytolla **Aloita**.
3. Avaa televisiossasi sen sisaanrakennettu mediasoitin tai mediapalvelinsovellus (se voi olla nimelta Media Player, SmartShare, AllShare tai vastaava).
4. Laitteesi ilmestyy mediapalvelinten listaan nimellaan (esimerkiksi "Speedy-Hare"). Valitse se.
5. Selaa jaettuja kuviasi, videoitasi ja musiikkiasi ja aloita toisto. Esikatselukuvat ilmestyvat automaattisesti.

Huomioita:

- DLNAa ei voi suojata salasanalla, joten tama yhteys on avoin kaikille samassa Wi-Fi-verkossa oleville sen ollessa paalla.
- Jos video ei toistu vanhemmassa televisiossa, laske videon laatua kohdassa **Asetukset -> Jakaminen -> Videot**, jotta Everdisk muuntaa sen yhteensopivampaan muotoon.

## Avaa verkkoselaimessa (HTTP)

Kayta tata jakaaksesi tiedostoja kenelle tahansa, jolla on verkkoselain - mitaan sovellusta ei tarvitse asentaa.

1. Varmista kohdassa **Asetukset -> Jakaminen -> Yhteydet**, etta **Selain** on paalla.
2. Napauta **Aloita**.
3. Kopioi Jakaminen-naytolta **Selain**-osoite (tai nayta sen QR-koodi).
4. Avaa toisessa puhelimessa, tabletissa tai tietokoneessa mika tahansa verkkoselain (Safari, Chrome, Edge, Firefox) ja syota kyseinen osoite.
5. Sivu avautuu jaettujen tiedostojesi kera.

Selaimessa toinen henkilo voi:

- Vaihdella **lista**- ja **ruudukko**-nakymien valilla ja lajitella nimen, paivamaaran tai koon mukaan.
- Nahda oikeat **esikatselukuvat** kuville, videoille, PDF-tiedostoille ja musiikin kansikuville.
- Avata kuvan koko naytolle **galleriaan**, jossa on pyyhkaisy, nipistyszoomaus ja diaesitys.
- Toistaa musiikkia sisaanrakennetussa **soittimessa**, jossa on jono, satunnaistoisto ja uusinta.
- **Ladata** minka tahansa tiedoston tai ladata koko kansion (tai useita valittuja kohteita) yhtena **Archive.zip**-tiedostona.
- **Ladata** tiedostoja takaisin laitteellesi - vain jos otit kayttoon **Tiedostojen muokkaus** (katso [Kaytto ja yksityisyys](/docs/guide/everdisk/everdisk-guide-access)).

## Kayta verkkoasemana (WebDAV)

Kayta tata saadaksesi laitteesi nakymaan tavallisena levyna Macilla, Windows-PC:lla tai Linux-koneella, jotta voit vetaa tiedostoja molempiin suuntiin.

**Macilla (Finder)**

1. Varmista kohdassa **Asetukset -> Jakaminen -> Yhteydet**, etta **Tietokone** on paalla.
2. Napauta **Aloita** ja merkitse muistiin **Tietokone (WebDAV)** -osoite.
3. Valitse Finderissa **Siirry -> Yhdista palvelimeen** (tai paina **⌘K**).
4. Syota WebDAV-osoite tarkalleen sellaisena kuin se nakyy ja napsauta **Yhdista**.
5. Syota kayttajatunnus ja salasana, jos asetit sellaisen, tai yhdista vieraana.
6. Laitteesi avautuu kuin mika tahansa muu verkkoasema. Veda tiedostoja sisaan tai ulos.

**Windowsissa**

1. Avaa **Resurssienhallinta**, napsauta hiiren oikealla painikkeella **Tama tietokone** ja valitse **Lisaa verkkosijainti** (tai maarita verkkoasema).
2. Syota Everdiskissa nakyva WebDAV-osoite.
3. Syota kayttajatunnus ja salasana, jos asetit sellaisen.

**Linuxissa**

1. Avaa tiedostonhallintasi ja valitse **Yhdista palvelimeen** (tai kayta `davs://` / `dav://`).
2. Syota Everdiskissa nakyva WebDAV-osoite.

Se, onko yhteys vain luku vai kaksisuuntainen, riippuu **Tiedostojen muokkaus** -asetuksesta. Kun se on paalla, voit kopioida tiedostoja laitteellesi seka nimetauudelleen tai poistaa niita; kun se on pois paalta, asema on vain luku.

## Yhdista SMB:n kautta (salattu verkkoasema)

SMB on verkkoasema Macille, Windowsille ja Linuxille, joka rakentuu naissa jarjestelmissa jo olevan tiedostojen jakamisen varaan, joten laitteesi nakyy tavallisena verkkoasemana - ja se on ainoa yhteys, jonka voit salata.

1. Varmista kohdassa **Asetukset -> Jakaminen -> Yhteydet**, etta **Tietokone (lisaasetukset)** (SMB-yhteys) on paalla.
2. Napauta **Aloita** ja merkitse muistiin **SMB**-osoite, joka nayttaa tallaiselta: `smb://192.168.1.20:4455/Share`.
3. Yhdista tietokoneeltasi:
   - **Mac:** laitteesi ilmestyy omana kohteenaan **Finderin sivupalkkiin** kohtaan **Sijainnit** (Verkko) - napsauta vain sita ja kirjaudu sisaan. Yhdistaaksesi kasin valitse **Siirry -> Yhdista palvelimeen** (**⌘K**) ja syota osoite.
   - **Windows:** avaa **Resurssienhallinta**, napsauta hiiren oikealla **Tama tietokone** ja valitse **Lisaa verkkoasema**, syota sitten `\\<address>\Share` kayttaen Jakaminen-naytolta saatavaa isantaa ja jaon nimea (tai kirjoita `smb://`-osoite osoitepalkkiin).
   - **Linux:** valitse tiedostonhallinnassasi **Yhdista palvelimeen** ja syota osoite.
4. Syota kayttajatunnus ja salasana, jos asetit sellaisen, tai yhdista vieraana.
5. Jaon nimi on **Share**. Kun **Tiedostojen muokkaus** on paalla, voit kopioida tiedostoja molempiin suuntiin; kun se on pois paalta, se on vain luku.

**Ota salaus kayttoon (suositeltavaa Wi-Fissa, johon et luota)**

SMB on ainoa Everdisk-yhteys, jonka voi salata. Suojataksesi jokaisen siirron **SMB3-salauksella (AES)**:

1. Aseta kohdassa **Asetukset -> Jakaminen -> Kaytto** **Kayttajatunnus** ja **Salasana** - salatut yhteydet eivat voi olla nimettomia.
2. Ota kohdassa **Asetukset -> Jakaminen** kayttoon **Vaadi SMB-salaus**.
3. **Lopeta ja aloita** jakaminen uudelleen, jotta muutos tulee voimaan.

Asiakkaasi on tuettava SMB3:a - Finderin nykyaikaisella Macilla tai **Windows 10:n tai uudemman**. SMB-salaus on Premium-ominaisuus.

## Yhdista tiedostosovellus (FTP)

Kayta tata tiedostonhallinta- ja siirtosovelluksille, jotka puhuvat FTP:ta (esimerkiksi FileZilla tai Cyberduck tietokoneella).

1. Varmista kohdassa **Asetukset -> Jakaminen -> Yhteydet**, etta **Muut sovellukset ja laitteet** on paalla.
2. Napauta **Aloita** ja merkitse muistiin **FTP**-osoite.
3. Lisaa FTP-sovelluksessasi uusi yhteys kayttamalla kyseista osoitetta.
4. Syota kayttajatunnus ja salasana, jos asetit sellaisen, tai jata ne tyhjiksi nimetonta paasya varten.

## Siirra USB-kaapelilla (Mac, ei Wi-Fia tarvita)

Kayta tata, kun Wi-Fia ei ole tai kun haluat nopeimman ja yksityisimman siirron. Se toimii vain **Macin** kanssa.

1. Kytke iPhone tai iPad Maciin tavallisella latauskaapelilla.
2. Jos laite kysyy, napauta **Luota tahan tietokoneeseen**.
3. Napauta Everdiskissa **Aloita**. Esiin tulee **Nopea yhteys saatavilla** -huomautus, ja Jakaminen-naytto nayttaa lisaosoitteen **Kaapeliyhteys**-merkinnalla, joka paattyy muotoon `.local`.
4. Avaa Macilla Finder -> **Siirry -> Yhdista palvelimeen** (**⌘K**) ja syota kyseinen `.local`-osoite (se toimii seka Selain- etta Tietokone-yhteyksissa).
5. Laitteesi avautuu kaapelin kautta - nopeammin kuin Wi-Fin kautta, eivatka tiedot koskaan kulje reitittimen tai internetin lapi.

Huomioita:

- Kayta **`.local`-nimea**, ei IP-osoitetta (IP-osoitteet toimivat vain Wi-Fin kautta), aloka koskaan `localhost`.
- Kaapelipolku on **vain Macille**. Windows-PC:iden ja Android-laitteiden on kaytettava Wi-Fia.
- Voit myos vetaa tiedostoja Everdisk-kansioon kayttamalla Finderia Macilla tai Apple Devices -sovellusta (tai iTunesia) Windowsissa iOS:n vakiotiedostonjaon kautta.

## Seuraavat vaiheet

- [Kaytto ja yksityisyys](/docs/guide/everdisk/everdisk-guide-access) - lisaa salasana, salli lataukset, esta laite.
- [Kuvat, musiikki ja video](/docs/guide/everdisk/everdisk-guide-media) - jaa koko kirjastosi ja aseta laatu.
- [Yhdista palvelimiin](/docs/guide/everdisk/everdisk-guide-devices) - paase muihin laitteisiin Everdiskista.
