---
title: "Yhteydet"
date: 2020-02-01
description: "Opi yhdistämään pilvipalvelut, NAS ja tietokoneesi Evertagiin. Käytä ja muokkaa äänitiedostoja suoraan pilvipalvelusta, henkilökohtaisesta NAS-laitteesta tai Mac/PC:ltä."
keywords: [
  "Evertag cloud-asetukset", "iCloudin yhdistäminen Evertagiin", "SMB-tiedostokäyttö iOS",
  "WebDAV äänitunnistemuokkain", "NAS-metatietojen muokkaus", "Wi-Fi Drive Evertag",
  "äänitiedostojen siirto iPhoneen", "Evertag iTunes File Sharing", "FLAC-tunnisteiden muokkaus pilvestä"
]
tags: ["opas", "evertag", "yhteydet"]
readingTime: 11
---


Tässä näytössä voit yhdistää eri lähteitä, jotka sisältävät äänitiedostojasi. Voit integroida suosittuja pilvipalveluja kuten Google Drive, Dropbox, OneDrive, iCloud ja muita sekä yhdistää Mac- tai PC-tietokoneesi. Lisäksi sinulla on mahdollisuus muokata Apple Time Capsulessa, WD Cloud Homessa tai missä tahansa SMB- tai WebDAV-yhteensopivassa NAS-laitteessa sijaitsevia äänitiedostoja.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Connections Screen" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Pikakäyttö

Yhteydet-näytön yläosassa löydät **Pikakäyttö**-luettelon. Mikä tahansa pilvipalvelukansio, jonka lisäät suosikkeihin — vaikka se olisi useita tasoja syvällä — näkyy täällä, jotta voit siirtyä siihen ilman, että sinun täytyy joka kerta selata ylätasoja.

## Yhdistäminen pilvipalveluun

- Avaa «Yhteydet»-välilehti
- Valitse «Yhdistä pilvipalveluun» valikosta
- Valitse pilvipalvelu luettelosta
- Syötä kirjautumistietosi ja napauta «Valmis».

Jos kohtaat ongelmia, tarkista internet-yhteytesi ja käyttäjätunnus/salasana.
Sovelluksen Premium-versiossa voit lisätä rajattoman määrän palveluja.

## Tuetut pilvipalvelut

Tällä hetkellä sovellus tukee suosituimpia pilvipalveluja: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘) sekä mitä tahansa SMB- tai WebDAV-palvelinta.

## Turvallisuus ja yksityisyys

Käytämme vain virallisia SDK:ita ja suojattuja yhteyksiä vuorovaikutukseen yhdistettyjen pilvipalvelujen kanssa. Käyttäjätunnuksesi ja salasanasi eivät ole sovelluksen käytettävissä. Kaikki sovelluksen pyynnöt pilvipalvelulle ovat salattuja.

Kun syötät käyttäjätunnuksesi ja salasanasi, sovellus näyttää sinulle pilvipalvelun tarjoajan virallisen valtuutussivun, ja koko valtuutusprosessi tapahtuu sovelluksen ulkopuolella. Pilvipalvelun tarjoaja lähettää autentikointitokenin sovellukselle onnistuneen valtuutuksen jälkeen, ja tätä tokenia käytetään API-kutsuihin.

Autentikointitoken on digitaalinen avain, joka sallii kolmannen osapuolen sovellusten vuorovaikutuksen pilvipalvelun kanssa. Autentikointitoken tallennetaan laitteellesi turvalliseen järjestelmäsäilöön nimeltä Keychain. Voit ladata tiedostoja yhdistetystä pilvipalvelusta laitteellesi, ja ne sijoitetaan sovelluksen «Documents»-hakemistoon. Voit poistaa nämä tiedostot milloin tahansa sisäänrakennetun tiedostonhallinnan avulla.

Sovellus ei jaa yhdistetyn pilvipalvelutilisi tietoja. Voit peruuttaa pääsyn pilvipalvelutiliisi milloin tahansa avaamalla tilin asetussivun verkkoselaimessasi.

## Autentikointitokenin peruuttaminen

Kirjaudu tilillesi verkkoselaimessa ja siirry asetussivulle. Siellä voit löytää kaikki pilvipalvelutiliisi yhdistetyt kolmannen osapuolen sovellukset ja poistaa minkä tahansa niistä, jos et enää halua käyttää kyseistä sovellusta. Yksityiskohtaiset ohjeet ovat saatavilla [täällä](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Voit myös katkaista yhdistetyt pilvipalvelutilit sovelluksessa, jolloin autentikointitoken poistetaan myös laitteeltasi. Jos poistat sovelluksen laitteeltasi, kaikki ladatut tiedot ja pääsytokenit poistetaan myös.

## Pilvipalvelun katkaiseminen tai konfiguraation muuttaminen

- Pilvipalvelun asetusten käyttäminen: Etsi ensin pilvipalvelu, jota haluat hallita sovelluksen käyttöliittymässä.
- Napauta «...»-painiketta: Palvelun otsikon vieressä näet «...»-painikkeen. Napauta sitä lisävaihtoehtojen käyttämiseksi.
  - **Nimeä uudelleen**: Jos haluat muuttaa pilvipalvelun nimeä luettelossasi, valitse «Nimeä uudelleen».
  - **Asetukset**: Muokataksesi pilvipalvelun konfiguraatiota tai autentikointitietoja, valitse «Asetukset». Joskus saatat joutua valtuuttamaan yhdistetyn pilvipalvelun uudelleen, jos valtuutustoken on vanhentunut.
  - **Irrottaa**: Jos haluat katkaista yhteyden sovelluksen ja pilvipalvelun välillä kokonaan, valitse «Irrottaa». Tiedäthän, että tämän vaihtoehdon valitseminen poistaa kaikki tähän pilvipalveluun liittyvät kappaleet sovelluksesi musiikkikirjastosta, mutta ne pysyvät palvelimella.

## Yhdistäminen tietokoneeseen tai NAS-laitteeseen

Voit myös yhdistää tietokoneesi, henkilökohtaisen NAS-laitteen tai muita verkkolaitteita SMB-, DLNA- tai WebDAV-protokollan avulla.

## Yhdistäminen tietokoneeseen SMB:n kautta

- Napauta «Yhdistä pilvipalveluun» → SMB.
- Syötä tietokoneen IP-osoite ja jaetun kansion nimi URL-kenttään käyttämällä muotoa smb://tietokoneen-ip-osoite/jaetun-kansion-nimi
- Valitse protokollaversio: Auto, SMB1, SMB2
- Syötä käyttäjätunnus ja salasana (tarvittaessa)
- Napauta «Valmis».

Jos yhteys onnistuu, näet yhdistetyn tallennustilan «Pilvipalvelu»-osiossa.
Täydellinen opas Mac- tai PC-tietokoneesi yhdistämiseen SMB:n kautta on saatavilla [täällä](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Yhdistäminen NAS-laitteeseen WebDAV:n kautta

Kaikki vaiheet ovat samat paitsi URL-kenttä.
URL-osoitteen tulee olla muodossa http://palvelimen-nimi tai https://palvelimen-nimi, jos palvelin tukee SSL:ää.
Täydellinen opas NAS-laitteen yhdistämiseen WebDAV-protokollan avulla on saatavilla [täällä](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Saatavilla olevat laitteet

Tässä osiossa näytetään kaikki lähiverkossasi olevat laitteet, joihin voit muodostaa yhteyden sovelluksen kautta.
Luo yhteys laitteeseen seuraamalla näitä vaiheita:

- Avaa sovellus ja siirry «Saatavilla olevat laitteet» -osioon.
- Napauta laitetta, johon haluat muodostaa yhteyden, luettelosta.
- Syötä tarvittaessa kirjautumistietosi yhteyden muodostamiseksi.

## Wi-Fi Drive

Wi-Fi Drive on kätevä teknologia, joka mahdollistaa langattoman tiedostonsiirron tietokoneeltasi iOS-laitteellesi työpöytäselaimen kautta.
Käyttääksesi tätä ominaisuutta tehokkaasti, varmista, että laitteesi ja tietokoneesi ovat yhteydessä samaan Wi-Fi-verkkoon.
Tässä on vaiheittainen opas Wi-Fi Driven käyttöön.

## Wi-Fi Driven käyttöönotto

- Avaa sovellus ja siirry «Yhteydet»-välilehdelle.
- Valitse «Yhdistä Wi-Fi:n kautta» siirtyäksesi Wi-Fi Driven päänäyttöön.
- Napauta «Käynnistä Wi-Fi Drive» aktivoidaksesi Wi-Fi Driven.

## Wi-Fi Driven käyttäminen tietokoneelta

- Avaa tietokoneellasi (pöytäkone tai kannettava) verkkoselain (kuten Chrome, Firefox tai Safari).
- Syötä selaimen osoitekenttään sovelluksen tarjoama URL.

## Tiedostojen langaton siirtäminen

Kun iOS-laitettasi vastaava verkkosivu avautuu selaimessa, voit helposti vetää ja pudottaa tiedostoja tietokoneeltasi verkkosivulle.
Vetämäsi ja pudottamasi tiedostot alkavat siirtyä iOS-laitteellesi ja ovat käytettävissä sovelluksessa.

Yksityiskohtaiset ohjeet tiedostojen langattomaan siirtämiseen Wi-Fi Driven avulla ovat saatavilla [täällä](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing on toinen teknologia, jonka avulla voit siirtää tiedostoja tietokoneelta laitteelle Finder-sovelluksella Macilla ja Lightning-kaapelilla.
- Liitä laite tietokoneeseen kaapelilla ja käynnistä Finder-sovellus Macilla.
- Avaa «Sijainnit» → «Yhdistetty laitteesi» → «Tiedostot» → ja etsi nykyinen sovellus.
- Napauta sovelluksen kuvaketta nähdäksesi kaikki jaetut kansiot.
- Kopioi tiedostoja tietokoneelta laitteen jaettuun kansioon vetämällä ja pudottamalla.

Yksityiskohtaiset ohjeet iTunes File Sharing -ominaisuuden käyttöön ovat saatavilla [täällä](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## USB-muistikortin yhdistäminen

Jos sinulla on SD-kortti tai USB-tikku, voit yhdistää sen Lightning- tai USB-C-kortinlukijalla iPhonessa/iPadissa tai liittää sen suoraan Maciin. Sovellus tukee tällä hetkellä Applen sertifioimia kortinlukijoita. Meillä on yksityiskohtaiset ohjeet USB-muistikortin yhdistämisestä iPhoneen tai iPadiin ja siinä olevien tiedostojen hallinnoimisesta, saatavilla [täällä](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Yhdistetyt asemat näkyvät Yhteydet-näytön **Liitetyt lisävarusteet** -osiossa.

## Tiedostonhallinta

Kun olet yhdistänyt pilvipalvelun, napauta sen kuvaketta nähdäksesi kaikki saatavilla olevat tiedostot ja kansiot. Voit käyttää sisäänrakennettua tiedostonhallintaa näiden tiedostojen käsittelyyn — lataamiseen, uudelleennimeämiseen, siirtämiseen ja muuhun. Kun aloitat lataamisen, tiedosto näkyy siirtojonossa. Nähdäksesi siirtojonon, siirry «Paikalliset tiedostot» -välilehdelle ja napauta pyöriviä nuolia vasemmassa yläkulmassa. Kaikki ladatut tiedostot ja kansiot ovat saatavilla «Paikalliset tiedostot» -osiossa.

## Ylätyökalupalkki

Ylätyökalupalkki, joka sijaitsee kätevästi navigointipalkin alla, tarjoaa useita hyödyllisiä toimintoja helppoa käyttöä varten. Voit näyttää tai piilottaa tämän työkalupalkin yksinkertaisella pyyhkäisyllä alaspäin. Tässä ovat saatavilla olevat toiminnot:

- **Haku**: Tämä vaihtoehto mahdollistaa nopean haun nykyisessä hakemistossa, mikä tekee tiettyjen tiedostojen tai kansioiden löytämisestä helppoa.

## Kansiovaihtoehdot

Kun avaat kansion sovelluksessa, löydät käytännöllisen joukon toimintoja napauttamalla «...»-painiketta näytön oikeassa yläkulmassa.
Tässä on erittely näistä toiminnoista:

- **Valita**: Aktivoi tiedoston valinta -tila. Tämä tila mahdollistaa yhden tai useamman tiedoston valitsemisen kansiosta, mikä helpottaa toimintojen suorittamista valituille kohteille.
- **Uusi kansio**: Luo uusi kansio nykyiseen kansioon. Tämä ominaisuus mahdollistaa tiedostojen järjestämisen ja kirjastosi rakenteen ylläpitämisen.
- **Lataa tiedostoja**: Lähetä tiedostoja laitteeltasi online-kansioon. Tämä toiminto mahdollistaa tiedostojen siirtämisen pilveen tai palvelimelle, jolloin ne ovat käytettävissä mistä tahansa.
- **Haku**: Etsi tiettyjä tiedostoja nykyisestä kansiosta. Tämä on erityisen hyödyllistä tiettyjen kohteiden nopeaan löytämiseen suuresta kokoelmasta.
- **Lajittele**: Järjestä kansion tiedostot kriteerien mukaan, kuten nimi, koko tai muokkausajankohta. Oletusarvoinen lajittelutila heijastaa yleensä palvelimen lajittelujärjestystä, mutta voit muuttaa sen mieltymystesi mukaan.
- **Ruudukko/luettelonäkymä**: Vaihda kahden näkymätilan välillä: taulukonäkymä ja pikkukuvanäkymä. Taulukonäkymä esittää tiedostot luettelona, kun taas pikkukuvanäkymä näyttää tiedostojen visuaaliset esitykset, mikä helpottaa sisällön tunnistamista yhdellä silmäyksellä.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloud Folder Sort" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Online-tiedostojen muokkaaminen

Kun sinun täytyy hallita useita tiedostoja pilvipalvelussa tässä sovelluksessa, voit käyttää valinta-tilaa toimintojesi tehostamiseksi. Seuraa näitä vaiheita tehokkaaseen tiedostonhallintaan:

- **Valinta-tilan aktivointi**: Avaa sovellus laitteellasi ja siirry pilvipalvelusi sisältävään osioon. Etsi oikeasta yläkulmasta «...» (kolme pistettä) -painike. Napauta sitä ja valitse «Valita»-valikkovaihtoehto aktivoidaksesi valinta-tilan.
- **Tiedostojen valitseminen**: Huomaat valintaruutujen ilmestyvän jokaisen luetellun tiedoston tai kansion viereen. Valitse yksi tai useampi tiedosto tai kansio napauttamalla niiden vieressä olevia valintaruutuja.
- **Erilaisten toimintojen suorittaminen**: Kun olet valinnut tiedostot tai kansiot, joita haluat hallita, sinulla on pääsy useisiin tarpeisiisi räätälöityihin toimintoihin:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Select" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Tiedostotoiminnot

Tiedoston otsikon lähellä huomaat kolme pistettä «...» – tämä on toimintovalikko.
Napauta sitä nähdäksesi luettelon saatavilla olevista toiminnoista:

- **Muokata äänitunnisteita**: Valitsemalla tämän vaihtoehdon pääset sisäänrakennettuun tunnistemuokkaimeen, jonka avulla voit muokata valitun tiedoston äänitunnisteita. Tiedosto ladataan väliaikaisesti väliaikaiseen hakemistoon ja ladataan sitten takaisin tallennustilaan sen jälkeen, kun vahvistat muutokset.
- **Lisää suosikkeihin**: Tämä toiminto lisää tiedoston suosittujen tiedostojesi luetteloon nopeaa ja kätevää käyttöä varten.
- **Ladata**: Valitse tämä toiminto ladataksesi tiedoston tai kansion laitteellesi, jolloin se on käytettävissä offline-tilassa.
- **Nimeä uudelleen**: Tämä vaihtoehto mahdollistaa tiedoston uudelleennimeämisen suoraan etätallennustilassa, mikä mahdollistaa mukautetun tiedostonimeämisen.
- **Siirrä**: Valitse tämä toiminto siirtääksesi tiedoston eri kansioon pilvipalvelussasi, mikä auttaa järjestyneen tiedostorakenteen ylläpitämisessä.
- **Avaa sovelluksessa**: Käytä tätä toimintoa viedäksesi tiedoston toiseen yhteensopivaan sovellukseen. Tiedosto ladataan laitteellesi ja sitten näkyviin ilmestyy Jaa-valintaikkuna lisäjakamista tai vuorovaikutusta varten.
- **Poistaa**: Ole varovainen tämän toiminnon kanssa, sillä se poistaa tiedoston pysyvästi pilvipalvelustasi. **Tätä poistoa ei voi peruuttaa**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Options" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Jos toimintoluettelo ylittää käytettävissä olevan näyttötilan, selaa vain toimintovalikossa alaspäin päästäksesi lisävaihtoehtoihin.

## Kansiotoiminnot

Jokaiselle pilvipalvelusi kansiolle on saatavilla useita toimintoja. Päästäksesi näihin vaihtoehtoihin, napauta vain kansion otsikon vieressä olevaa «...»-kuvaketta. Jos et näe kaikkia toimintoja, selaa alaspäin paljastaaksesi lisää. Tässä ovat saatavilla olevat toiminnot:

- **Lisää suosikkeihin**: Käytä tätä toimintoa lisätäksesi kansion suosittujen tiedostojesi luetteloon nopeaa ja kätevää käyttöä varten.
- **Ladata**: Lataa kansion kaikki sisältö laitteellesi offline-käyttöä varten.
- **Nimeä uudelleen**: Nimeä kansio uudelleen suoraan etätallennustilassa.
- **Siirrä**: Siirrä kansio eri sijaintiin pilvipalvelussasi.
- **Poistaa**: Ole varovainen tämän toiminnon kanssa, sillä se poistaa kansion ja sen sisällön pysyvästi pilvipalvelustasi. **Tätä toimintoa ei voi peruuttaa**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Folder Options" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
