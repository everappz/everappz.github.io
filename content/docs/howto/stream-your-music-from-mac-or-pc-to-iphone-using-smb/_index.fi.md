---
title: "Suoratoista musiikkia Macista tai PC:stä iPhoneen SMB:n avulla"
description: "Opi suoratoistamaan musiikkikokoelmasi Macista tai Windows PC:stä iPhoneen tai iPadiin Evermusicin ja SMB-protokollan avulla. Yksinkertainen vaiheittainen opas yhdistämiseen ja äänen nauttimiseen ilman synkronointia."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["suoratoista musiikkia Macista iPhoneen", "SMB äänen suoratoisto iOS", "Evermusic SMB asennus", "yhdistä PC musiikki iPhone", "Mac musiikin jakaminen iOS", "SMB Windows tiedostojen suoratoisto", "Evermusic PC kansioiden käyttö"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**Lyhyesti:** Käytä Evermusic-sovellusta iPhonelle tai iPadille suoratoistaaksesi musiikkia Macistasi tai Windows PC:stäsi paikallisverkon kautta SMB:n avulla. Ei synkronointia, ei kopiointia -- ota vain tiedostojen jakaminen käyttöön tietokoneellasi, yhdistä sovelluksessa ja toista. Asennus kestää alle 5 minuuttia.

Hukkuuko sinua musiikkimeri MAC:llasi tai PC:lläsi ja haluat nauttia siitä vaivattomasti iPhonellasi tai iPadillasi? Älä etsi kauempaa kuin Evermusic. Evermusicin avulla on uskomattoman helppoa yhdistää tietokoneesi SMB-protokollalla ja suoratoistaa lempikappaleitasi huolehtimatta ylimääräisestä tallennustilasta tai synkronointiongelmista. Tässä on vaiheittainen opas alkuun pääsemiseksi:

## Vaihe 1: Ota SMB-protokolla käyttöön tietokoneellasi

![Evermusic - SMB-tuki - Macin jakonäyttö](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Jos käytät MACia

- Avaa Järjestelmäasetukset -> Jakaminen.
- Ota Tiedostojen jakaminen käyttöön.
- "Jaetut kansiot" -osiossa lisää musiikkikansiosi, valitse käyttäjä ja aseta käyttöoikeustasot (Luku ja kirjoitus tai Vain luku).
- Lisämukavuuden vuoksi voit valita "Kaikki: Vain luku" musiikkikansiolle, mikä tekee siitä helposti saatavilla Evermusicissa.
- Muista merkitä muistiin tietokoneesi URL (smb://192.168.xx.xx) seuraavia vaiheita varten.

![Evermusic - SMB-tuki - Tiedostojen jakonäyttö](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Napauta "Asetukset" ja ota käyttöön "Jaa tiedostot ja kansiot SMB:n avulla."
- Ota "Windows-tiedostojen jakaminen" käyttöön saatavilla oleville tileille.

![Evermusic - SMB-tuki - Tiedostojen ja kansioiden jakonäyttö](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Jos käytät Windows PC:tä

![Evermusic - SMB-tuki - Tiedostojen jakaminen Windowsissa](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Napsauta hiiren oikealla painikkeella musiikkikansiotasi.
- Valitse "Ominaisuudet."
- Avaa "Jakaminen"-välilehti.
- Napsauta "Jaa..."
- Valitse ihmiset, joiden kanssa haluat jakaa, ja aseta heidän käyttöoikeustasonsa.
- Kuten MACissa, voit valita "Kaikki: Luku" valitulle musiikkikansiolle.
- Napsauta "Valmis" tallentaaksesi asetuksesi.

![Evermusic - SMB-tuki - Jaettu kansio Windowsissa](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Vaihe 2: Lisää tietokoneesi automaattisesti

- Avaa nyt Evermusic ja siirry "Yhteydet"-välilehteen ("Verkko" jos käytät sovelluksen vanhempaa versiota).
- Jos näet tietokoneesi "Saatavilla olevat laitteet" -osiossa ("Saatavilla olevat jaot" jos käytät sovelluksen vanhempaa versiota) ja valitsit "Kaikki: Vain luku" edellisessä vaiheessa, napauta vain tietokonettasi ja se yhdistyy automaattisesti.
- Jos tämä ei tapahdu, voit lisätä tietokoneesi manuaalisesti.

![Evermusic - SMB-tuki - Tilin yhdistämisnäyttö](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Vaihe 3: Lisää tietokoneesi manuaalisesti

- Napauta "Yhdistä pilvipalvelu" ("Lisää tili" jos käytät sovelluksen vanhempaa versiota)
- Valitse "SMB" saatavilla olevien palvelinten listasta seuraavalla näytöllä.
- "SMB"-asetusnäytöllä:
  - Syötä palvelimen URL jaetun kansion polun kanssa. Voit syöttää palvelimen nimen tai palvelimen IP:n. Esimerkiksi:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Syötä käyttäjätunnuksesi ja salasanasi tai jätä nämä kentät tyhjiksi, jos valitsit "Kaikki: Vain luku" edellisessä vaiheessa.
  - "WORKGROUP"-kenttä on valinnainen ja sitä tulisi käyttää, jos sinulla on Active Directory -toimialue.

![Evermusic - SMB-tuki - Tunnistetietojen syöttönäyttö](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Kun olet yhdistänyt SMB-tilisi, se näkyy "Pilvipalvelut"-osiossa ("Tilit"). Avaa yhdistetty tili napauttamalla sitä, siirry musiikkikansioon ja napauta mitä tahansa äänitiedostoa käynnistääksesi soittimen.

![Evermusic - SMB-tuki - Yhdistetyn kansion avausnäyttö](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Nauti musiikkikokoelmastasi saumattomasti iPhonellasi tai iPadillasi Evermusicin kanssa.

![Evermusic - SMB-tuki - Äänisoittimen näyttö](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Vaihe 4: SMB2-kiertotapa

Jos kohtaat ongelmia kansioiden selaamisessa tai tiedostojen toistamisessa, jotka sisältävät erikoismerkkejä (kuten ü, ö, é), tämä voi liittyä SMB2-protokollaan. Työskentelemme aktiivisesti tämän ongelman ratkaisemiseksi.

Väliaikaisena ratkaisuna kokeile ottaa SMB 1 käyttöön palvelimellasi ja sovelluksen asetuksissa. Vaihtoehtoisesti voit yhdistää SMB-palvelimeesi järjestelmän tiedostojen avausvalikon kautta. Näin:

1. Siirry "Paikalliset tiedostot" -kohtaan.
2. Vieritä alas "Tiedostot tällä laitteella" -osioon ja napauta "Avaa tiedostoja..." tai "Avaa kansioita..."
3. Etsi palvelimesi ja valitse tarvitsemasi tiedostot tai kansiot.
4. Napauta "Avaa" vahvistaaksesi valintasi.

## Vaihe 5: WebDAV-kiertotapa

Lisäksi voit kokeilla yhdistämistä NAS-laitteeseesi WebDAV- tai DLNA-protokollien avulla, jos ne ovat tuettuja.

Noudattamalla näitä vaiheita voit ohittaa erikoismerkkeihin liittyvät ongelmat tiedostonimissä ja jatkaa mediatiedostojesi nauttimista.

P.S. Voit myös siirtää äänitiedostoja MAC/PC:stäsi iPhonellesi iTunes-tiedostojen jakamisen avulla ja toistaa paikallisia äänitiedostoja. Lue lisää tästä ominaisuudesta oppaassamme: [Kuinka toistaa iTunes-tiedostoja iPhonessa](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Usein kysytyt kysymykset

{{% details title="Voinko suoratoistaa musiikkia PC:ltäni iPhonelleni ilman iTunesia?" closed="true" %}}
Kyllä. Evermusic yhdistää PC:hesi SMB:n kautta paikallisessa Wi-Fi-verkossasi. iTunesia ei tarvita. Ota vain tiedostojen jakaminen käyttöön PC:lläsi ja yhdistä sovelluksessa.
{{% /details %}}

{{% details title="Käyttääkö SMB-suoratoisto mobiilidataa?" closed="true" %}}
Ei. SMB toimii paikallisen Wi-Fi-verkkosi kautta. Internet-yhteyttä tai mobiilidataa ei tarvita.
{{% /details %}}

{{% details title="Mitä ääniformaatteja Evermusic tukee SMB:n kautta?" closed="true" %}}
Evermusic tukee MP3-, FLAC-, AAC-, WAV-, AIFF-, OGG-, WMA-, ALAC- ja muita yleisiä ääniformaatteja. Tiedostot toistetaan suoraan SMB-jaosta.
{{% /details %}}

{{% details title="Voinko suoratoistaa musiikkia NAS:sta iPhonelleni?" closed="true" %}}
Kyllä. Jos NAS:si tukee SMB:tä (useimmat tukevat, mukaan lukien Synology, QNAP ja WD My Cloud), voit yhdistää siihen käyttämällä samoja vaiheita tässä oppaassa.
{{% /details %}}

{{% details title="Pitääkö tietokoneeni olla päällä suoratoiston aikana?" closed="true" %}}
Kyllä. Koska Evermusic suoratoistaa tiedostoja suoraan tietokoneeltasi, sen on oltava päällä ja yhdistettynä samaan verkkoon kuin iPhonesi.
{{% /details %}}

{{% details title="Onko SMB-suoratoistossa tiedostokokorajoitusta?" closed="true" %}}
Ei. Evermusic suoratoistaa minkä tahansa kokoisia tiedostoja SMB:n kautta. Suuret häviöttömät tiedostot (FLAC, WAV) toimivat ongelmitta.
{{% /details %}}
