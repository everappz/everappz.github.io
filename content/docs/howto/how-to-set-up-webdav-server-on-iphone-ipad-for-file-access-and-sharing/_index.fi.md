---
title: "Näin määrität WebDAV-palvelimen iPhonelle ja iPadille tiedostojen käyttöön ja jakamiseen"
description: "Muuta iPhone tai iPad WebDAV-palvelimeksi Everdiskillä ja liitä se verkkolevynä Macin Finderiin, Windowsin File Exploreriin, Linuxiin, Androidiin tai toiseen iPhoneen Wi-Fin kautta. Täysi käyttöönotto, WebDAV-osoite ja portti sekä vaiheittaiset yhdistämisohjeet jokaiselle laitteelle."
date: 2026-09-19
tags: ["everdisk", "webdav", "verkkolevy", "tiedostojen jakaminen", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV-palvelin iPhone", "WebDAV-palvelin iPad", "näin määrität WebDAVin iPhonella", "liitä iPhone verkkolevyksi", "yhdistä iPhonen WebDAV Mac Finder", "WebDAV Windows File Explorer iPhone", "iphone verkkolevy Windows", "WebDAV Linux iPhone", "käytä iPhonen tiedostoja tietokoneelta", "webdav iphonesta iphoneen", "jaa tiedostoja iPhone WebDAV", "liitä verkkoasema iphone", "siirrä tiedostoja iphone webdav", "webdav-osoite portti iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV muuttaa kansion verkkolevyksi, jonka tietokone voi avata tavallisessa tiedostonhallinnassaan. Se toimii saman verkkoprotokollan päällä, jota selaimesi käyttää, minkä vuoksi se kulkee hyvin Macin, Windowsin ja Linuxin välillä ilman erikoisajureita. [Everdiskin](/products/everdisk) avulla voit pyörittää WebDAV-palvelinta iPhonellasi tai iPadillasi, jolloin puhelin näkyy levynä, jota voit selata, josta voit kopioida ja johon voit kopioida lähes miltä tahansa tietokoneelta.

WebDAV on paras valinta, kun Windows on kuvassa mukana, koska Windowsin File Explorer yhdistää siihen siististi. Tämä opas kattaa käyttöönoton sekä sen, miten yhdistät Macilta, Windowsista, Linuxista, Androidista ja toiselta iPhonelta.

## Mitä tarvitset

- iPhonen tai iPadin, johon on asennettu [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Tietokoneen tai toisen laitteen **samassa Wi-Fi-verkossa**.
- Tiedostot, jotka haluat jakaa, Everdiskin Dokumentit-kansiossa tai lisäämissäsi kansioissa.

## Määritä WebDAV-palvelin Everdiskissä

### Vaihe 1: Valitse mitä jaat ja aseta käyttöoikeus

Avaa Everdisk, siirry **Jakaminen**-välilehdelle ja napauta **Mitä jaetaan**. Dokumentit-kansio jaetaan oletuksena. Lisää lisää toiminnoilla **Lisää kansio** ja **Lisää tiedosto**.

Avaa **Asetukset**, sitten **Jakaminen** ja sitten **Käyttöoikeus**. Aseta **Tiedostojen muokkaus** päälle, jos haluat yhdistettyjen tietokoneiden voivan kopioida tiedostoja puhelimeesi sekä nimetä uudelleen ja poistaa niitä, tai pois päältä vain luku -levyä varten. Aseta tähän **Käyttäjätunnus** ja **Salasana**, jos haluat kirjautumisen, tai jätä ne tyhjiksi vieraskäyttöä varten.

### Vaihe 2: Ota käyttöön WebDAV-palvelin

Siirry kohtaan **Asetukset**, sitten **Jakaminen** ja sitten **Yhteydet**, ja ota käyttöön **Tietokone**. Se on WebDAV-palvelin (se kantaa WebDAV-merkintää).

### Vaihe 3: Aloita jakaminen ja merkitse osoite muistiin

Palaa **Jakaminen**-välilehdelle ja napauta **Aloita**. **Miten yhdistät** -osio näyttää WebDAV-osoitteen. Se näyttää tältä:

```
http://192.168.1.20:8080
```

Kaksoispisteen jälkeinen numero on **portti**, joka on oletuksena **8080**. Ensimmäinen osa on iPhonesi osoite Wi-Fi-verkossa, joten omasi poikkeaa siitä. Pidä Everdisk avoinna näytöllä, kun laite on yhdistettynä.

## Yhdistä Macilta

1. Avaa **Finder**, valitse **Siirry**, sitten **Yhdistä palvelimeen** (tai paina **Command ja K**).
2. Kirjoita Everdiskissä näkyvä WebDAV-osoite, esimerkiksi `http://192.168.1.20:8080`.
3. Klikkaa **Yhdistä**, valitse sitten **Vieras** tai syötä **Käyttäjätunnus** ja **Salasana**.

iPhonesi avautuu Finder-ikkunaan ja käyttäytyy kuin tavallinen kansio. Kopioi tiedostoja kumpaan tahansa suuntaan, jos Tiedostojen muokkaus on päällä.

## Yhdistä Windowsista

Windowsissa on sisäänrakennettu WebDAV-asiakas, joten tämä toimii File Explorerista.

1. Avaa **File Explorer**, klikkaa hiiren oikealla sivupalkissa **Tämä tietokone** ja valitse **Lisää verkkosijainti** (voit myös käyttää **Yhdistä verkkoasema**).
2. Kun osoitetta kysytään, kirjoita sama WebDAV-osoite Everdiskistä, esimerkiksi `http://192.168.1.20:8080`, ja klikkaa sitten **Seuraava**.
3. Syötä **Käyttäjätunnus** ja **Salasana**, jos asetit sellaisen.

Laite näkyy sitten kohdassa Tämä tietokone verkkosijaintina, jonka voit avata ja josta voit kopioida tiedostoja. Jos Windows kieltäytyy yhdistämästä ensimmäisellä kerralla, varmista, että **WebClient**-palvelu on käynnissä (etsi Palvelut Käynnistä-valikosta, löydä WebClient ja aseta se käynnistymään), ja yritä sitten uudelleen.

## Yhdistä Linuxista

1. Avaa tiedostonhallintasi ja valitse **Connect to Server** tai **Other Locations**.
2. Syötä osoite WebDAV-etuliitteellä, esimerkiksi `dav://192.168.1.20:8080` (käytä `davs://` vain, jos määritit TLS:n).
3. Yhdistä vieraana tai syötä kirjautumistietosi.

## Yhdistä Androidista

Androidissa ei ole järjestelmän WebDAV-selainta, joten käytä sitä tukevaa tiedostonhallintaa:

1. Asenna sovellus, kuten **Solid Explorer** tai **CX File Explorer**.
2. Lisää uusi **WebDAV**-yhteys.
3. Syötä isäntä ja **portti 8080**, valitse `http`-malli ja lisää kirjautumistietosi, jos asetit sellaisen.

## Yhdistä toiselta iPhonelta tai iPadilta

iOS:n Tiedostot-sovelluksessa ei ole WebDAV-asiakasta, joten käytä jotain näistä:

- **Everdiskin oma Laitteet-välilehti.** Avaa toisella laitteella Everdisk, siirry kohtaan **Laitteet**, napauta **Uusi yhteys**, valitse **WebDAV** ja syötä osoite, esimerkiksi `http://192.168.1.20:8080`. Tämä on yksinkertaisin reitti eikä vaadi mitään ylimääräistä.
- **WebDAV-sovellus**, kuten Documents by Readdle, joka voi lisätä WebDAV-yhteyden samalla osoitteella ja kirjautumisella.

## Mieluummin nopea linkki kuin levy?

Jos sinun tarvitsee vain napata tiedosto nopeasti etkä halua liittää levyä lainkaan, ota käyttöön **Selain**-yhteys kohdassa Asetukset, Jakaminen, Yhteydet. Everdisk antaa sinulle tällöin verkko-osoitteen, jonka voit avata missä tahansa selaimessa millä tahansa laitteella tiedostojesi selaamiseen ja lataamiseen. Se on nopein tapa luovuttaa tiedosto Windows-tietokoneelle, Chromebookille tai ystävän puhelimeen.

## Vain luku vai luku ja kirjoitus

**Tiedostojen muokkaus** -kytkin kohdassa Asetukset, Jakaminen, Käyttöoikeus ratkaisee tämän. Päällä tarkoittaa, että yhdistetyt tietokoneet voivat lähettää, nimetä uudelleen ja poistaa. Pois päältä tarkoittaa, että levy on vain luku -tilassa, joten muut voivat katsella ja kopioida tiedostojasi mutta eivät voi muuttaa niitä.

## Tosielämän tapoja käyttää tätä

- **Kopioi tiedostoja iPhoneesi Windows-tietokoneelta** liittämällä se verkkosijainniksi ja vetämällä ne siirtymään.
- **Pura kuvat ja asiakirjat kannettavaan** käyttämällä jo tuntemaasi tiedostonhallintaa, ilman kaapelia ja ilman iTunesia.
- **Muokkaa asiakirjaa paikallaan** Maciltasi, avaamalla se suoraan puhelimesta ja tallentamalla takaisin.
- **Siirrä kansio iPhonen ja iPadin välillä** käyttämällä Everdiskin Laitteet-välilehteä vastaanottavalla laitteella.

## Muutama vinkki

- Pidä Everdisk avoinna, kun laite on yhdistettynä. Puhelimen lukitseminen pitkäksi aikaa voi pysäyttää sovelluksen.
- Windowsissa, jos yhteys epäonnistuu, käynnistä WebClient-palvelu ja kokeile osoitetta uudelleen.
- WebDAV ja SMB liittyvät molemmat verkkolevyinä. Käytä WebDAVia, kun Windows on mukana, ja [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/):tä, kun haluat Finderin nopeuden ja salauksen.
- Nopeimpia siirtoja varten pidä kuvien ja videoiden laatu asetuksella Alkuperäinen Asetuksissa.

## Usein kysytyt kysymykset

{{% details title="Mikä on iPhoneni WebDAV-osoite ja portti?" closed="true" %}}
Kun aloitat jakamisen, Everdisk näyttää osoitteen Jakaminen-näytöllä. Se näyttää tältä: http://192.168.1.20:8080. 8080 on portti, jota Everdisk käyttää WebDAViin, ja ensimmäinen osa on iPhonesi osoite Wi-Fi-verkossa, joten omasi on erilainen.
{{% /details %}}

{{% details title="Miten yhdistän iPhoneni WebDAViin Windowsista?" closed="true" %}}
Avaa File Explorer, klikkaa hiiren oikealla Tämä tietokone ja valitse Lisää verkkosijainti tai Yhdistä verkkoasema. Syötä Everdiskin WebDAV-osoite, esimerkiksi http://192.168.1.20:8080, ja syötä sitten kirjautumistietosi, jos asetit sellaisen. Jos Windows ei yhdistä, varmista, että WebClient-palvelu on käynnissä (etsi Palvelut, löydä WebClient, käynnistä se) ja yritä uudelleen.
{{% /details %}}

{{% details title="Voinko käyttää WebDAVia kahden iPhonen välillä?" closed="true" %}}
Kyllä, mutta iOS:n Tiedostot-sovelluksessa ei ole WebDAV-asiakasta, joten käytä Everdiskiä toisella laitteella. Avaa Laitteet-välilehti, napauta Uusi yhteys, valitse WebDAV ja syötä ensimmäisellä puhelimella näkyvä osoite. WebDAV-sovellus, kuten Documents by Readdle, toimii myös.
{{% /details %}}

{{% details title="Tarvitseeko WebDAV salasanan?" closed="true" %}}
Ei, kirjautuminen on valinnaista. Jätä Käyttäjätunnus ja Salasana tyhjiksi kohdassa Asetukset, Jakaminen, Käyttöoikeus vieraskäyttöä varten, tai aseta ne, jos haluat yhteyksien kirjautuvan sisään.
{{% /details %}}

{{% details title="Voivatko muut ihmiset muuttaa tiedostojani WebDAVin kautta?" closed="true" %}}
Vain jos sallit sen. Tiedostojen muokkaus -kytkin kohdassa Asetukset, Jakaminen, Käyttöoikeus hallitsee tätä. Päällä antaa yhdistettyjen laitteiden lähettää, nimetä uudelleen ja poistaa. Pois päältä tekee levystä vain luku -tilaisen, joten muut voivat katsella ja kopioida mutta eivät muuttaa mitään.
{{% /details %}}

{{% details title="WebDAV vai SMB, mikä ero on?" closed="true" %}}
Molemmat liittävät iPhonesi verkkolevynä. WebDAV toimii verkkoprotokollan päällä ja yhdistää siististi Windowsin File Explorerista, mikä on sen pääasiallinen vahvuus. SMB on natiivi tiedostojen jakaminen Macilla, Linuxissa ja NAS-laitteilla, on yleensä nopeampi Macilla ja on ainoa Everdisk-yhteys, joka voi salata siirrot. Everdisk voi pyörittää molempia yhtä aikaa.
{{% /details %}}

{{% details title="Miksi WebDAV-levyni katkeaa?" closed="true" %}}
iPhonesi on palvelin, ja iOS pysäyttää sovellukset, jotka pysyvät taustalla liian kauan. Pidä Everdisk avoinna näytöllä, kun laite on yhdistettynä, ja kytke virtalähteeseen pitkien siirtojen aikana. Varmista myös, että molemmat laitteet ovat edelleen samassa Wi-Fi-verkossa.
{{% /details %}}

{{% details title="Voinko yhdistää WebDAVin kautta ilman Wi-Fiä?" closed="true" %}}
Kyllä, jos kytket iPhonesi Maciin kaapelilla. Everdisk näyttää tällöin ylimääräisen kaapeliyhteysosoitteen, jonka yhdistetty Mac voi avata Finderissa, mikä toimii vaikka ilman Wi-Fiä lainkaan. Kaapelissa vain kyseinen Mac voi tavoittaa laitteen.
{{% /details %}}

{{% details title="Onko Everdisk ilmainen?" closed="true" %}}
Kyllä, Everdiskin voi ladata ilmaiseksi ja WebDAV-palvelin sisältyy siihen. Valinnainen kertaostoksena hankittava Premium lisää lisäominaisuuksia, kuten mukautetut portit sekä kuvien ja videoiden muunnoksen. Voit ottaa WebDAVin käyttöön ja jakaa tiedostoja maksamatta.
{{% /details %}}

Valmis kokeilemaan? [Lataa Everdisk App Storesta](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) ja liitä iPhonesi levynä parissa minuutissa. Kysymyksiä tai palautetta? Lähetä meille sähköpostia osoitteeseen **support@everappz.com**.
