---
title: "Näin määrität SMB-palvelimen iPhonelle ja iPadille tiedostojen jakamiseen"
description: "Muuta iPhone tai iPad SMB-tiedostopalvelimeksi Everdiskillä ja avaa se verkkolevynä Macilta, toiselta iPhonelta, Linuxista tai Androidista Wi-Fin kautta. Täysi käyttöönotto, smb-osoite ja portti, valinnainen SMB3-salaus sekä vaiheittaiset yhdistämisohjeet jokaiselle laitteelle."
date: 2026-09-19
tags: ["everdisk", "smb", "tiedostojen jakaminen", "verkkolevy", "iphone", "ipad", "mac", "finder", "salaus", "wifi"]
keywords: ["SMB-palvelin iPhone", "SMB-palvelin iPad", "näin määrität SMB:n iPhonella", "iPhonen SMB-jako", "yhdistä iPhonen SMB Mac Finder", "smb iphonesta iphoneen", "iOS Files -sovellus yhdistä palvelimeen SMB", "jaa tiedostoja iPhone SMB", "iphone verkkolevy Finder", "SMB3-salaus iOS", "smb-jako iPhone Android", "yhdistä SMB:hen Linuxista", "iphone verkkolevynä", "jaa tiedostoja iphonejen välillä wifi", "liitä iphone verkkolevyksi"]
readingTime: 10
---

{{< author-byline >}}

SMB on macOS:ään, Windowsiin ja Linuxiin sekä lähes jokaiseen verkkolevyyn (NAS) sisäänrakennettu tiedostojen jakaminen. Kun yhdistät toisen tietokoneen jaettuun kansioon ja se avautuu tavallisena levynä Finderissa tai File Explorerissa, se on SMB:n työtä. [Everdiskin](/products/everdisk) avulla voit asettaa SMB-jaon iPhonellesi tai iPadillesi, jolloin puhelin itse näkyy verkkolevynä, jota muut laitteet selaavat, josta ne kopioivat ja johon ne kopioivat.

Tämä on vaihtoehto, johon kannattaa tarttua, kun haluat iPhonesi käyttäytyvän kunnon levynä eikä verkkosivuna. Se on nopea, se vetää ja pudottaa molempiin suuntiin, ja se on Everdiskin ainoa yhteystyyppi, joka voi salata jokaisen siirron. Tämä opas kattaa käyttöönoton sekä sen, miten yhdistät Macilta, toiselta iPhonelta tai iPadilta, Linuxista, Androidista ja Windowsista.

## Mitä tarvitset

- iPhonen tai iPadin, johon on asennettu [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Toisen laitteen **samassa Wi-Fi-verkossa**.
- Tiedostot, jotka haluat jakaa, Everdiskin Dokumentit-kansiossa tai lisäämissäsi kansioissa.

## Määritä SMB-palvelin Everdiskissä

### Vaihe 1: Valitse mitä jaat ja kuka voi kirjoittaa

Avaa Everdisk, siirry **Jakaminen**-välilehdelle ja napauta **Mitä jaetaan**. Dokumentit-kansio jaetaan oletuksena. Lisää lisää toiminnoilla **Lisää kansio** ja **Lisää tiedosto**, ja ota käyttöön kuva- tai musiikkikirjastosi, jos haluat myös ne saataville.

Päätä, voivatko muut laitteet vain lukea tiedostojasi vai myös muuttaa niitä. Avaa **Asetukset**, sitten **Jakaminen** ja sitten **Käyttöoikeus**, ja aseta **Tiedostojen muokkaus**. Kun se on päällä, yhdistetyt laitteet voivat kopioida tiedostoja puhelimeesi sekä nimetä uudelleen ja poistaa niitä. Kun se on pois päältä, jako on vain luku -tilassa.

Jos haluat kirjautumisen, aseta **Käyttäjätunnus** ja **Salasana** samalla Käyttöoikeus-näytöllä. Jätä molemmat tyhjiksi salliaksesi vieraskäytön.

### Vaihe 2: Ota käyttöön SMB-palvelin

Siirry kohtaan **Asetukset**, sitten **Jakaminen** ja sitten **Yhteydet**, ja ota käyttöön **Tietokone (lisäasetukset)**. Se on SMB-palvelin (se kantaa SMB-merkintää).

### Vaihe 3: Aloita jakaminen ja merkitse osoite muistiin

Palaa **Jakaminen**-välilehdelle ja napauta **Aloita**. **Miten yhdistät** -osio näyttää nyt SMB-osoitteen. Se näyttää tältä:

```
smb://192.168.1.20:4455/Share
```

Kolme asiaa, jotka on hyvä tietää tuosta osoitteesta:

- Kaksoispisteen jälkeinen numero on **portti**. Everdisk käyttää oletuksena **4455**.
- Jaon nimi on **Share**.
- Ensimmäinen osa on iPhonesi osoite Wi-Fi-verkossa, joten se on erilainen sinun verkossasi.

Pidä Everdisk avoinna, kun laitteet ovat yhdistettyinä, koska iOS pysäyttää sovellukset, jotka ovat taustalla liian kauan.

## Yhdistä Macilta

Tämä on sujuvin tapaus, koska macOS puhuu SMB:tä natiivisti.

Nopein tapa: avaa **Finder** ja katso sivupalkissa kohdista **Sijainnit** tai **Verkko**. Everdisk ilmoittautuu Wi-Fi-verkossa, joten iPhonesi ilmestyy sinne usein itsestään. Klikkaa sitä, klikkaa sitten **Yhdistä nimellä** ja valitse **Vieras**, tai syötä kirjautumistietosi.

Yhdistäminen käsin:

1. Valitse Finderissa **Siirry**, sitten **Yhdistä palvelimeen** (tai paina **Command ja K**).
2. Kirjoita Everdiskissä näkyvä SMB-osoite, esimerkiksi `smb://192.168.1.20:4455/Share`.
3. Klikkaa **Yhdistä**, valitse sitten **Vieras** tai syötä **Käyttäjätunnus** ja **Salasana**.

iPhonesi avautuu Finder-ikkunaan. Kopioi tiedostoja sisään tai ulos vetämällä, aivan kuten millä tahansa muulla levyllä (jos Tiedostojen muokkaus on päällä).

## Yhdistä toiselta iPhonelta tai iPadilta

iOS ja iPadOS voivat avata SMB-jaot sisäänrakennetussa **Tiedostot**-sovelluksessa, mikä tekee puhelimesta puhelimeen -siirroista siistejä ja nopeita.

Toisella laitteella:

1. Avaa **Tiedostot**-sovellus.
2. Napauta **lisää**-painiketta (kolme pistettä, iPhonessa oikeassa yläkulmassa) ja valitse **Yhdistä palvelimeen**.
3. Syötä Everdiskin SMB-osoite, esimerkiksi `smb://192.168.1.20:4455/Share`.
4. Valitse **Vieras**, tai **Rekisteröitynyt käyttäjä** ja syötä kirjautumistietosi.
5. Jako näkyy Tiedostoissa kohdassa Sijainnit. Selaa ja kopioi kumpaan tahansa suuntaan.

Voit myös käyttää Everdiskin omaa **Laitteet**-välilehteä toisella laitteella, joka sisältää SMB-asiakkaan. Avaa Everdisk, siirry kohtaan **Laitteet**, napauta **Uusi yhteys**, valitse **SMB** ja syötä osoite.

## Yhdistä Linuxista

1. Avaa tiedostonhallintasi (Files/Nautilus GNOMEssa, Dolphin KDE:ssä).
2. Valitse **Other Locations** tai **Connect to Server**.
3. Syötä osoite, esimerkiksi `smb://192.168.1.20:4455/Share`.
4. Yhdistä vieraana tai syötä kirjautumistietosi.

Päätteestä voit myös suorittaa komennon `smbclient //192.168.1.20/Share -p 4455` ja syöttää kirjautumistietosi pyydettäessä.

## Yhdistä Androidista

Androidissa ei ole järjestelmän SMB-selainta, joten käytä SMB:tä tukevaa tiedostonhallintaa:

1. Asenna sovellus, kuten **CX File Explorer**, **Solid Explorer** tai **X-plore File Manager**.
2. Lisää uusi **SMB**- tai **LAN**-yhteys.
3. Syötä isäntä (iPhonesi Wi-Fi-osoite), aseta **portiksi 4455** ja jaon nimeksi **Share**.
4. Yhdistä vieraana tai kirjautumistiedoillasi, selaa sitten ja kopioi.

## Yhdistä Windowsista

Windows osaa lukea SMB-jakoja, yhdellä varauksella, joka kannattaa tietää heti alkuun. Sisäänrakennettu File Explorer keskustelee SMB:n kanssa vain vakioportissa eikä anna kirjoittaa mukautettua porttia polkuun, ja Everdisk käyttää porttia 4455. Niinpä tavallinen **Yhdistä verkkoasema** -reitti ei useinkaan tavoita sitä.

Sinulla on kaksi hyvää vaihtoehtoa Windowsissa:

- Käytä tiedostonhallintaa tai SMB-asiakasta, joka antaa asettaa mukautetun portin, ja osoita se iPhonesi osoitteeseen portilla **4455** ja jaon nimellä **Share**.
- Tai yhdistä Windowsista sen sijaan jollain Everdiskin muista palvelimista. [WebDAV-käyttöönotto](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) ja [FTP-käyttöönotto](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) toimivat molemmat hyvin Windowsin File Explorerista, ja selainlinkki toimii missä tahansa selaimessa.

Jos haluat silti kokeilla Yhdistä verkkoasema -toimintoa: avaa **File Explorer**, klikkaa hiiren oikealla **Tämä tietokone** ja valitse **Yhdistä verkkoasema**, ja syötä Everdiskissä näkyvä isäntä ja jaon nimi. Jos se ei pysty yhdistämään, kyseessä on yllä mainittu porttirajoitus, joten vaihda WebDAViin tai FTP:hen.

## Ota salaus käyttöön epäluotettavaa Wi-Fiä varten

SMB on ainoa Everdisk-yhteys, joka voi salata jokaisen siirron, mikä on tärkeää Wi-Fi-verkossa, jota et täysin hallitse, kuten kahvilassa tai toimistoverkossa.

1. Aseta kohdassa **Asetukset**, **Jakaminen**, **Käyttöoikeus** **Käyttäjätunnus** ja **Salasana**. Salatut yhteydet eivät voi olla nimettömiä, joten tämä vaihe on pakollinen.
2. Ota kohdassa **Asetukset**, **Jakaminen** käyttöön **Vaadi SMB-salaus**.
3. Pysäytä ja aloita jakaminen uudelleen, jotta muutos tulee voimaan.

Jokainen SMB-siirto on tällöin suojattu **SMB3-salauksella (AES)**. Yhdistävän laitteen on tuettava SMB3:a, minkä nykyaikaisen Macin Finder ja Windows 10 tai uudempi molemmat tekevät. SMB-salaus on osa kertaostoksena hankittavaa Premiumia.

## Vain luku vai luku ja kirjoitus

**Tiedostojen muokkaus** -kytkin kohdassa Asetukset, Jakaminen, Käyttöoikeus hallitsee tätä jokaisen palvelimen osalta, mukaan lukien SMB. Ota se käyttöön, niin yhdistetyt laitteet voivat lähettää, nimetä uudelleen ja poistaa. Ota se pois päältä, niin ne voivat vain selata ja kopioida tiedostoja pois puhelimestasi. Valitse vain luku, kun luovutat tiedostoja jollekulle, jonka et halua muuttavan mitään.

## Tosielämän tapoja käyttää tätä

- **Siirrä iso kansio iPhoneesi Macilta** vetämällä se Finder-ikkunaan, nopeammin kuin verkkolähetys.
- **Vedä päivän kuvat ja videot pois puhelimestasi** kannettavaan ilman iTunesia tai kaapelia.
- **Lähetä tiedostoja kahden iPhonen välillä** Tiedostot-sovelluksen kautta, ilman kolmatta sovellusta kummallakaan puolella.
- **Työskentele tiedoston parissa paikallaan**, avaamalla asiakirjan suoraan puhelimesta Macin sovelluksessa ja tallentamalla sen takaisin.

## Muutama vinkki

- Pidä Everdisk avoinna, kun laite on yhdistettynä. Puhelimen lukitseminen pitkäksi aikaa voi pysäyttää sovelluksen ja katkaista yhteyden.
- Jos Mac ei näe puhelinta Finderin sivupalkissa, yhdistä käsin toiminnolla Yhdistä palvelimeen ja koko smb-osoitteella.
- Suurten siirtojen parasta nopeutta varten pidä kuvien ja videoiden laatu asetuksella Alkuperäinen Asetuksissa.
- Epäluotettavassa verkossa ota käyttöön Vaadi SMB-salaus ja sammuta muut palvelimet työskentelysi ajaksi.

## Usein kysytyt kysymykset

{{% details title="Mikä on iPhoneni SMB-osoite ja portti?" closed="true" %}}
Kun aloitat jakamisen, Everdisk näyttää osoitteen Jakaminen-näytöllä. Se näyttää tältä: smb://192.168.1.20:4455/Share. 4455 on portti, jota Everdisk käyttää SMB:hen, ja Share on jaetun kansion nimi. Ensimmäinen osa on iPhonesi osoite Wi-Fi-verkossa, joten omasi on erilainen.
{{% /details %}}

{{% details title="Voinko yhdistää iPhoneni SMB-jakoon Windowsista?" closed="true" %}}
Windowsin File Explorer yhdistää SMB:hen vain vakioportissa eikä hyväksy mukautettua porttia polussa, kun taas Everdisk käyttää porttia 4455. Niinpä tavallinen Yhdistä verkkoasema -reitti ei useinkaan tavoita sitä. Käytä tiedostonhallintaa, joka antaa asettaa mukautetun portin, tai yhdistä Windowsista sen sijaan WebDAVilla, FTP:llä tai selainlinkillä. Kaikki nämä toimivat Windowsista ilman porttiongelmia.
{{% /details %}}

{{% details title="Miten jaan tiedostoja kahden iPhonen välillä SMB:llä?" closed="true" %}}
Aloita SMB-palvelin ensimmäisellä iPhonella Everdiskissä. Avaa toisella iPhonella Tiedostot-sovellus, napauta lisää-painiketta, valitse Yhdistä palvelimeen ja syötä Everdiskissä näkyvä smb-osoite (esimerkiksi smb://192.168.1.20:4455/Share). Yhdistä vieraana tai kirjautumistiedoillasi, ja jako näkyy Tiedostoissa. Voit myös käyttää Everdiskin omaa Laitteet-välilehteä toisessa puhelimessa.
{{% /details %}}

{{% details title="Näkyykö iPhoneni Macin Finderin sivupalkissa automaattisesti?" closed="true" %}}
Yleensä kyllä. Everdisk ilmoittaa SMB-jaon Wi-Fi-verkossasi, joten iPhonesi ilmestyy usein Finderin sivupalkkiin kohtaan Sijainnit tai Verkko. Klikkaa sitä ja valitse Yhdistä nimellä, sitten Vieras tai kirjautumistietosi. Jos se ei ilmesty, yhdistä käsin toiminnolla Siirry, Yhdistä palvelimeen ja koko smb-osoitteella.
{{% /details %}}

{{% details title="Tarvitsenko salasanan SMB:n käyttöön?" closed="true" %}}
Ei, kirjautuminen on valinnaista. Jätä Käyttäjätunnus ja Salasana tyhjiksi kohdassa Asetukset, Jakaminen, Käyttöoikeus salliaksesi vieraskäytön. Aseta ne, jos haluat yhteyksien kirjautuvan sisään. Käyttäjätunnus ja salasana vaaditaan vain, jos otat käyttöön Vaadi SMB-salaus, koska salatut yhteydet eivät voi olla nimettömiä.
{{% /details %}}

{{% details title="Onko SMB-yhteys salattu?" closed="true" %}}
Se voi olla. SMB on ainoa Everdisk-yhteys, joka tukee salausta. Aseta käyttäjätunnus ja salasana, ota sitten käyttöön Vaadi SMB-salaus kohdassa Asetukset, Jakaminen. Jokainen siirto on tällöin suojattu SMB3:lla (AES). Toisen laitteen on tuettava SMB3:a, minkä nykyaikaiset Macit ja Windows 10 tai uudempi tekevät. Salaus on Premium-ominaisuus.
{{% /details %}}

{{% details title="Voivatko ihmiset muuttaa tai poistaa tiedostojani SMB:n kautta?" closed="true" %}}
Vain jos sallit sen. Tiedostojen muokkaus -kytkin kohdassa Asetukset, Jakaminen, Käyttöoikeus hallitsee tätä. Kun se on päällä, yhdistetyt laitteet voivat lähettää, nimetä uudelleen ja poistaa. Kun se on pois päältä, jako on vain luku -tilassa ja muut voivat selata ja kopioida tiedostoja pois puhelimestasi mutta eivät voi muuttaa mitään.
{{% /details %}}

{{% details title="Miksi SMB-yhteyteni katkesi?" closed="true" %}}
iPhonesi on palvelin, ja iOS pysäyttää sovellukset, jotka pysyvät taustalla liian kauan. Pidä Everdisk avoinna näytöllä, kun laite on yhdistettynä, ja kytke puhelin virtalähteeseen pitkien siirtojen aikana. Varmista myös, että molemmat laitteet pysyivät samassa Wi-Fi-verkossa.
{{% /details %}}

{{% details title="SMB, WebDAV vai FTP, mitä minun tulisi käyttää?" closed="true" %}}
Käytä SMB:tä, kun haluat puhelimen käyttäytyvän kunnon verkkolevynä Macilla, toisella iPhonella, Linuxissa tai NAS-levyllä, ja kun haluat salauksen. Käytä WebDAVia, kun haluat verkkolevyn, joka toimii hyvin myös Windowsista. Käytä FTP:tä laajimpaan yhteensopivuuteen vanhempien laitteiden ja sovellusten kanssa. Everdisk voi pyörittää niitä kaikkia yhtä aikaa, joten et ole sidottu yhteen.
{{% /details %}}

{{% details title="Onko Everdisk ilmainen?" closed="true" %}}
Kyllä, Everdiskin voi ladata ilmaiseksi ja SMB-palvelin sisältyy siihen. Valinnainen kertaostoksena hankittava Premium lisää SMB-salauksen, mukautetut portit ja muutaman muun lisäominaisuuden. Voit ottaa SMB:n käyttöön ja jakaa tiedostoja maksamatta.
{{% /details %}}

Valmis kokeilemaan? [Lataa Everdisk App Storesta](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) ja avaa iPhonesi Finderissa noin minuutissa. Kysymyksiä tai palautetta? Lähetä meille sähköpostia osoitteeseen **support@everappz.com**.
