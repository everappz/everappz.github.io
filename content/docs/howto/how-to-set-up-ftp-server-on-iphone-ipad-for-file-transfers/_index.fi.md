---
title: "Näin määrität FTP-palvelimen iPhonelle ja iPadille tiedostojen siirtoon"
description: "Muuta iPhone tai iPad FTP-palvelimeksi Everdiskillä ja siirrä tiedostoja Macilta, Windows-tietokoneelta, Linuxista, Androidista, FTP-sovelluksesta kuten FileZilla tai toiselta iPhonelta Wi-Fin kautta. Täysi käyttöönotto, ftp-osoite ja portti, vieraskäyttö sekä vaiheittaiset yhdistämisohjeet jokaiselle laitteelle."
date: 2026-09-19
tags: ["everdisk", "ftp", "tiedostonsiirto", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP-palvelin iPhone", "FTP-palvelin iPad", "näin määrität FTP:n iPhonella", "iphone ftp-palvelinsovellus", "yhdistä FileZilla iPhoneen", "Cyberduck iPhone FTP", "siirrä tiedostoja iPhone FTP", "ftp iphonesta tietokoneeseen", "ftp iphonesta iphoneen", "yhdistä iPhonen FTP:hen Windowsista", "ftp-osoite portti iphone", "nimetön ftp iphone", "jaa tiedostoja iphone ftp", "iphone ftp kameralle nas"]
readingTime: 9
---

{{< author-byline >}}

FTP on tiedostonsiirron vanha luotettava. Se on ollut olemassa vuosikymmeniä, mikä on juuri se syy, miksi se on niin hyödyllinen: lähes kaikki, mikä osaa keskustella palvelimen kanssa, ymmärtää sitä. Kamerat, älytelevisiot, reitittimet, verkkolevyt, automaatiotyökalut ja jokainen työpöydän FTP-sovellus puhuvat FTP:tä. [Everdiskin](/products/everdisk) avulla voit pyörittää FTP-palvelinta iPhonellasi tai iPadillasi, jolloin puhelimesta tulee paikka, johon nuo laitteet ja sovellukset voivat yhdistää ja siirtää tiedostoja.

Tartu FTP:hen, kun muut vaihtoehdot eivät sovi, esimerkiksi vanhemman laitteen tai sovelluksen kanssa, joka osaa yhdistää vain FTP:n kautta. Tämä opas kattaa käyttöönoton sekä sen, miten yhdistät Macilta, Windowsista, FTP-sovelluksesta, Linuxista, Androidista ja toiselta iPhonelta.

## Mitä tarvitset

- iPhonen tai iPadin, johon on asennettu [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Tietokoneen, sovelluksen tai laitteen **samassa Wi-Fi-verkossa**.
- Tiedostot, jotka haluat jakaa, Everdiskin Dokumentit-kansiossa tai lisäämissäsi kansioissa.

## Määritä FTP-palvelin Everdiskissä

### Vaihe 1: Valitse mitä jaat ja aseta käyttöoikeus

Avaa Everdisk, siirry **Jakaminen**-välilehdelle ja napauta **Mitä jaetaan**. Dokumentit-kansio jaetaan oletuksena. Lisää lisää toiminnoilla **Lisää kansio** ja **Lisää tiedosto**.

Avaa **Asetukset**, sitten **Jakaminen** ja sitten **Käyttöoikeus**. Ota **Tiedostojen muokkaus** käyttöön, jos haluat ihmisten voivan lähettää, nimetä uudelleen ja poistaa, tai pois päältä salliaksesi vain lataukset. Aseta **Käyttäjätunnus** ja **Salasana**, jos haluat kirjautumisen, tai jätä ne tyhjiksi, jotta kuka tahansa voi yhdistää vieraana.

### Vaihe 2: Ota käyttöön FTP-palvelin

Siirry kohtaan **Asetukset**, sitten **Jakaminen** ja sitten **Yhteydet**, ja ota käyttöön **Muut sovellukset ja laitteet**. Se on FTP-palvelin (se kantaa FTP-merkintää).

### Vaihe 3: Aloita jakaminen ja merkitse osoite muistiin

Palaa **Jakaminen**-välilehdelle ja napauta **Aloita**. **Miten yhdistät** -osio näyttää FTP-osoitteen. Se näyttää tältä:

```
ftp://192.168.1.20:2121
```

Kaksoispisteen jälkeinen numero on **portti**, joka on oletuksena **2121**. Ensimmäinen osa on iPhonesi osoite Wi-Fi-verkossa, joten omasi on erilainen. Pidä Everdisk avoinna näytöllä, kun laite on yhdistettynä.

## Yhdistä Macilta

1. Avaa **Finder**, valitse **Siirry**, sitten **Yhdistä palvelimeen** (tai paina **Command ja K**).
2. Kirjoita Everdiskissä näkyvä FTP-osoite, esimerkiksi `ftp://192.168.1.20:2121`.
3. Klikkaa **Yhdistä**, valitse sitten **Vieras** tai syötä **Käyttäjätunnus** ja **Salasana**.

Finder liittää FTP-jaon, jotta voit selata ja kopioida tiedostoja Macillesi. Huomaa, että Finder avaa FTP:n vain luku -tilassa. Kun haluat lähettää Macilta, käytä FTP-sovellusta kuten alla kuvataan.

## Yhdistä Windowsista

1. Avaa **File Explorer** ja klikkaa osoiteriviä yläreunassa.
2. Kirjoita Everdiskin FTP-osoite, esimerkiksi `ftp://192.168.1.20:2121`, ja paina **Enter**.
3. Syötä **Käyttäjätunnus** ja **Salasana**, jos asetit sellaisen, tai jatka vieraana.

Jaetut tiedostot näkyvät ikkunassa ja voit kopioida ne tietokoneellesi.

## Yhdistä FTP-sovelluksella (FileZilla, Cyberduck)

Lähetyksiä ja täyttä hallintaa varten FTP-sovellus on paras työkalu. **FileZilla** ja **Cyberduck** ovat ilmaisia ja toimivat Windowsissa, Macissa ja Linuxissa.

1. Avaa sovellus ja luo uusi yhteys.
2. Aseta **Host** iPhonesi Wi-Fi-osoitteeksi ja **Port** arvoon **2121**.
3. Syötä kirjautumista varten **Käyttäjätunnus** ja **Salasana**, tai valitse **Anonymous**, jos et asettanut sellaista.
4. Yhdistä ja vedä tiedostoja molempiin suuntiin (lähetykset vaativat, että Tiedostojen muokkaus on päällä).

## Yhdistä Linuxista

1. Avaa tiedostonhallintasi ja valitse **Connect to Server** tai **Other Locations**.
2. Syötä osoite, esimerkiksi `ftp://192.168.1.20:2121`.
3. Yhdistä vieraana tai kirjautumistiedoillasi.

Voit myös käyttää mitä tahansa Linuxin FTP-asiakasta päätteestä osoittamalla se samaan isäntään ja porttiin 2121.

## Yhdistä Androidista

Androidissa ei ole järjestelmän FTP-selainta, joten käytä sovellusta:

1. Asenna FTP-asiakas, kuten **AndFTP**, **FTPCafe**, tai FTP:tä tukeva tiedostonhallinta, kuten **Solid Explorer**.
2. Lisää yhteys isännällä, **portilla 2121** ja kirjautumistiedoillasi tai Anonymous.
3. Selaa ja siirrä.

## Yhdistä toiselta iPhonelta tai iPadilta

iOS:n Tiedostot-sovelluksessa ei ole FTP-asiakasta, joten käytä jotain näistä toisella laitteella:

- **Everdiskin oma Laitteet-välilehti.** Avaa Everdisk, siirry kohtaan **Laitteet**, napauta **Uusi yhteys**, valitse **FTP** ja syötä osoite, esimerkiksi `ftp://192.168.1.20:2121`. Tämä on yksinkertaisin reitti.
- **Erillinen FTP-sovellus** iOS:lle, käyttäen samaa isäntää, porttia 2121 ja kirjautumista.

## Yhdistä muut laitteet: kamerat, televisiot, reitittimet ja NAS

Tässä FTP loistaa. Monissa laitteissa on sisäänrakennettu FTP-asiakas, joka voi lähettää tai hakea tiedostoja:

- **Kamerat**, jotka lähettävät kuvia FTP:n kautta, voivat lähettää ne suoraan iPhoneesi.
- **Älytelevisiot, reitittimet, NAS-laatikot ja automaatiotyökalut**, jotka tukevat FTP:tä, voivat yhdistää samalla tavalla.

Osoita ne iPhonesi Wi-Fi-osoitteeseen, porttiin **2121** ja kirjautumistietoihisi (tai Anonymous) käyttäen Everdiskissä näkyvää osoitetta.

## Vain luku vai luku ja kirjoitus

**Tiedostojen muokkaus** -kytkin kohdassa Asetukset, Jakaminen, Käyttöoikeus hallitsee tätä. Päällä antaa ihmisten lähettää, nimetä uudelleen ja poistaa. Pois päältä tarkoittaa, että he voivat vain ladata. Valitse vain luku, kun luovutat tiedostoja etkä halua mitään muutettavan puhelimessasi.

## Tosielämän tapoja käyttää tätä

- **Yhdistä FileZilla iPhoneesi** ja työnnä nippu tiedostoja puhelimeen yhdellä kertaa.
- **Anna vanhan sovelluksen tai laitteen, joka puhuu vain FTP:tä**, tavoittaa tiedostosi, kun mikään muu ei yhdistä.
- **Vastaanota kuvia kamerasta**, joka lähettää FTP:n kautta.
- **Siirrä tiedostoja iPhonen ja iPadin välillä** käyttämällä Everdiskin Laitteet-välilehteä vastaanottavalla laitteella.

## Muutama vinkki

- Pidä Everdisk avoinna, kun laite on yhdistettynä, koska iOS pysäyttää taustasovellukset jonkin ajan kuluttua.
- Lähettääksesi Macilta, käytä FileZillaa tai Cyberduckia Finderin sijaan, koska Finder avaa FTP:n vain luku -tilassa.
- Jätä kirjautuminen tyhjäksi laajimman yhteensopivuuden takaamiseksi, yhdistä sitten Anonymous-tunnuksella, jota useimmat FTP-asiakkaat tarjoavat.
- FTP ei salaa liikennettään. Verkossa, johon et luota, käytä sen sijaan [SMB-palvelinta salauksella](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Usein kysytyt kysymykset

{{% details title="Mikä on iPhoneni FTP-osoite ja portti?" closed="true" %}}
Kun aloitat jakamisen, Everdisk näyttää osoitteen Jakaminen-näytöllä. Se näyttää tältä: ftp://192.168.1.20:2121. 2121 on portti, jota Everdisk käyttää FTP:hen, ja ensimmäinen osa on iPhonesi osoite Wi-Fi-verkossa, joten omasi on erilainen.
{{% /details %}}

{{% details title="Miten yhdistän FileZillan tai Cyberduckin iPhoneeni?" closed="true" %}}
Avaa sovellus ja luo uusi yhteys. Aseta Host iPhonesi Wi-Fi-osoitteeksi ja Port arvoon 2121. Syötä Käyttäjätunnus ja Salasana, tai valitse Anonymous, jos et asettanut sellaista Everdiskissä. Yhdistä, ja voit vetää tiedostoja molempiin suuntiin, kun Tiedostojen muokkaus on päällä.
{{% /details %}}

{{% details title="Voinko yhdistää iPhoneni FTP:hen Windowsista?" closed="true" %}}
Kyllä. Avaa File Explorer, klikkaa osoiteriviä, kirjoita Everdiskin FTP-osoite (esimerkiksi ftp://192.168.1.20:2121) ja paina Enter. Syötä kirjautumistietosi, jos asetit sellaisen, tai jatka vieraana. Lähetyksiä ja enemmän hallintaa varten käytä sen sijaan FTP-sovellusta, kuten FileZillaa.
{{% /details %}}

{{% details title="Tarvitsenko kirjautumisen FTP:tä varten?" closed="true" %}}
Ei, kirjautuminen on valinnaista. Jätä Käyttäjätunnus ja Salasana tyhjiksi kohdassa Asetukset, Jakaminen, Käyttöoikeus, ja yhdistä Anonymous-tunnuksella, jota useimmat FTP-asiakkaat tarjoavat. Aseta kirjautuminen, jos haluat yhteyksien kirjautuvan ensin sisään.
{{% /details %}}

{{% details title="Miksi voin vain ladata enkä lähettää FTP:n kautta?" closed="true" %}}
Kaksi syytä on yleisiä. Ensinnäkin Tiedostojen muokkaus -kytkimen kohdassa Asetukset, Jakaminen, Käyttöoikeus on oltava päällä salliakseen lähetykset, uudelleennimeämiset ja poistot. Toiseksi Macin Finder avaa FTP:n vain luku -tilassa, joten käytä FTP-sovellusta, kuten FileZillaa tai Cyberduckia, kun haluat lähettää.
{{% /details %}}

{{% details title="Voinko käyttää FTP:tä kahden iPhonen välillä?" closed="true" %}}
Kyllä. Aloita FTP-palvelin ensimmäisellä iPhonella. Avaa toisella Everdisk, siirry Laitteet-välilehdelle, napauta Uusi yhteys, valitse FTP ja syötä ensimmäisellä puhelimella näkyvä osoite. Erillinen FTP-sovellus iOS:lle toimii myös, koska iOS:n Tiedostot-sovelluksessa ei ole FTP-asiakasta.
{{% /details %}}

{{% details title="Onko FTP turvallinen?" closed="true" %}}
Tavallinen FTP ei salaa liikennettään, joten kohtele sitä työkaluna verkoille, joihin luotat, kuten kotisi Wi-Fi. Verkossa, jota et hallitse, käytä SMB-palvelinta Vaadi SMB-salaus käytössä, mikä suojaa jokaisen siirron.
{{% /details %}}

{{% details title="Mitkä laitteet voivat yhdistää FTP:n kautta?" closed="true" %}}
Lähes kaikki, joissa on FTP-asiakas. Tämä sisältää Mac-, Windows- ja Linux-tietokoneet, FTP-sovellukset kuten FileZilla ja Cyberduck, Androidin tiedostonhallinnat sekä laitteet, kuten kamerat, älytelevisiot, reitittimet, NAS-laatikot ja automaatiotyökalut. Tuo laaja tavoittavuus on tärkein syy valita FTP.
{{% /details %}}

{{% details title="Miksi FTP-yhteyteni katkesi?" closed="true" %}}
iPhonesi on palvelin, ja iOS pysäyttää sovellukset, jotka pysyvät taustalla liian kauan. Pidä Everdisk avoinna näytöllä, kun laite on yhdistettynä, ja kytke virtalähteeseen pitkien siirtojen aikana. Varmista myös, että molemmat laitteet ovat edelleen samassa Wi-Fi-verkossa.
{{% /details %}}

{{% details title="Onko Everdisk ilmainen?" closed="true" %}}
Kyllä, Everdiskin voi ladata ilmaiseksi ja FTP-palvelin sisältyy siihen. Valinnainen kertaostoksena hankittava Premium lisää lisäominaisuuksia, kuten mukautetut portit sekä kuvien ja videoiden muunnoksen. Voit ottaa FTP:n käyttöön ja siirtää tiedostoja maksamatta.
{{% /details %}}

Valmis kokeilemaan? [Lataa Everdisk App Storesta](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) ja yhdistä ensimmäinen FTP-asiakkaasi parissa minuutissa. Kysymyksiä tai palautetta? Lähetä meille sähköpostia osoitteeseen **support@everappz.com**.
