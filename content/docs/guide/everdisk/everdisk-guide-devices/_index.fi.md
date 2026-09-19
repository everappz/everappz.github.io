---
title: "Yhdista palvelimiin"
date: 2026-08-20
description: "Kayta Everdiskin Laitteet-valilehtea yhdistaaksesi verkkosi muihin palvelimiin. Lisaa ja selaa DLNA-, WebDAV-, FTP-, SFTP- ja SMB-palvelimia ja NAS-asemia, suoratoista aanta ja videota, lataa tiedostoja ja luo, laheta, nimea uudelleen, siirra tai poista palvelimilla, jotka sen sallivat."
keywords: ["Everdisk Laitteet-valilehti", "yhdista NAS", "DLNA asiakas iPhone", "WebDAV asiakas iPhone", "FTP asiakas iPhone", "SFTP asiakas iPhone", "SMB asiakas iPhone", "yhdista SMB-jakoon", "selaa verkkopalvelinta", "suoratoisto NASsta", "lataa palvelimelta", "yhdista pilvi WebDAV"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk ei ole vain langaton asema - se on myos asiakas verkkosi muille laitteille. **Laitteet**-valilehdella voit yhdistya **DLNA**-, **WebDAV**-, **FTP**-, **SFTP**- ja **SMB**-palvelimiin, mukaan lukien Macit, Windows-tietokoneet, Linux-koneet, NAS-asemat ja mediapalvelimet, ja sitten selata, suoratoistaa ja ladata niiden tiedostoja.

## Laitteet-naytto

Laitteet-valilehdella on kaksi osaa:

- **Yhteydet** - jo tallentamasi palvelimet.
- **Saatavilla olevat laitteet** - palvelimet, jotka Everdisk loytaa automaattisesti paikallisverkostasi.

Yhdistyaksesi johonkin, jonka Everdisk on jo loytanyt, napauta sita vain kohdassa **Saatavilla olevat laitteet**. Lisataksesi palvelimen kasin napauta **plus (+)** -painiketta tai **Uusi yhteys**.

## Lisaa uusi yhteys

Napauta **Uusi yhteys** ja valitse palvelintyyppi, johon haluat paasta:

- **DLNA / UPnP** - paras mediapalvelimille. Suoratoista videota, musiikkia ja kuvia mediakirjastoista, verkkolevyilta seka DLNA-yhteensopivista televisioista ja tietokoneista. DLNA on vain luku: voit selata, suoratoistaa ja ladata, mutta et voi lahettaa tai muuttaa tiedostoja.
- **WebDAV** - yhdisty tiedostopalvelimiin, verkkolevyihin ja pilvilevyihin, jotka tukevat WebDAVia. Luku ja kirjoitus, kun palvelin sen sallii.
- **FTP** - yleinen reitittimissa, verkkolevyissa ja verkkohotelleissa. Oletusportti on 21 (990 suojatulle FTPS:lle); voit asettaa mukautetun portin osoitteeseen, esimerkiksi `ftp://host:2121`. Jata kayttajatunnus ja salasana tyhjiksi nimetonta paasya varten.
- **SFTP** - yhdisty turvallisesti SSH:n kautta. Oletusportti on 22; kayta tarvittaessa mukautettua porttia osoitteessa, esimerkiksi `sftp://host:2222`.
- **SMB** - yhdista Maceihin, Windows-tietokoneisiin, Linux-palvelimiin ja verkkolevyihin (NAS), jotka jakavat kansioita **SMB / CIFS** -protokollalla. Syota osoite kuten `smb://server-address/share-name/` (esimerkkeja: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB lisaa kaksi valinnaista kenttaa: **Tyoryhma**-nimen seka **Protokollaversion**, jonka voit jattaa asetukseen **Automaattinen** tai pakottaa tilaan **SMB1** tai **SMB2**. Jos tiedostot tai kansiot, joissa on erikoismerkkeja, eivat aukea, kokeile vaihtaa version tilaan **SMB1**.

> Everdisk yhdistyy vain naihin paikallisverkon ja suoraan osoitettaviin protokolliin. Se ei kirjaudu pilvitileihin kuten Google Drive tai Dropbox. Pilvilevy on tavoitettavissa vain, jos kyseinen palvelu tarjoaa **WebDAV**-osoitteen, jonka voit syottaa.

## Syota osoite ja kirjaudu sisaan

Tayta yhteyseditorissa:

- **Nimi** - ystavallinen nimi yhteydelle.
- **URL / osoite** - palvelimen osoite (esimerkit nakyvat jokaiselle tyypille).
- **Kayttajatunnus** ja **Salasana** - jata molemmat tyhjiksi, jos palvelin sallii nimettoman paasyn.

WebDAVin osalta voit sallia virheelliset varmenteet, jos palvelimesi kayttaa itse allekirjoitettua. Jos suojatun palvelimen identiteettia ei voida vahvistaa, Everdisk pyytaa sinua vahvistamaan ennen kuin siihen luotetaan.

Ilmaiskayttajat voivat tallentaa enintaan **10** yhteytta. Premium poistaa rajoituksen.

## Selaa, suoratoista ja lataa

Kun yhteys on muodostettu, napauta palvelinta avataksesi sen:

- **Selaa** kansioita listana tai ruudukkona, lajittele ne ja nae esikatselukuvat. DLNA-palvelimet nayttavat myos musiikin tiedot ja kansikuvat.
- **Suoratoista** aanta ja videota. Aani menee minisoittimen jonoon; video toistuu koko naytolla. Kelaus toimii tiedoston suoratoiston aikana.
- **Lataa** tiedostoja laitteellesi. Valitse useita kerralla erolatausta varten. Lataukset nakyvat kohdassa **Tiedostosiirrot** ja paatyvat **Asiakirjat**-kansioosi.
- **Tiedot** mista tahansa kohteesta nayttaa sen tyypin, koon, paivamaaran, polun ja mediatiedot.

## Muuta tiedostoja palvelimella

Palvelimilla, jotka sallivat kirjoituksen - **WebDAV, FTP, SFTP ja SMB** - voit myos hallita tiedostoja:

- **Uusi kansio**
- **Laheta tiedostoja** laitteeltasi
- **Nimea uudelleen**, **Siirra** ja **Poista** (yksi kohde tai useita kerralla)

**DLNA**-palvelimet ovat vain luku, joten nama toiminnot eivat ole siella kaytettavissa.

## Seuraa siirtojasi

Lataukset ja lahetykset kaynnistyvat taustalla ja nakyvat kohdassa **Tiedostosiirrot**, jonka avaat **Asiakirjat**-valilehden ylavasemmasta reunasta. Siella voit seurata edistymista seka keskeyttaa, jatkaa, yrittaa uudelleen, peruuttaa tai tyhjentaa tehtavia. Voit myos saataa siirtoja kohdassa [Asetukset -> Verkko](/docs/guide/everdisk/everdisk-guide-settings) (vain Wi-Fi vai Wi-Fi ja mobiilidata, kuinka moni ajetaan kerralla ja jatkuvatko ne taustalla).

## Seuraavat vaiheet

- [Tiedostot ja asiakirjat](/docs/guide/everdisk/everdisk-guide-files) - hallitse kaikkea, mita lataat.
- [Kuvat, musiikki ja video](/docs/guide/everdisk/everdisk-guide-media) - toista sita, mita suoratoistat.
- [Asetukset](/docs/guide/everdisk/everdisk-guide-settings) - yhteysrajoitukset ja siirtovaihtoehdot.
