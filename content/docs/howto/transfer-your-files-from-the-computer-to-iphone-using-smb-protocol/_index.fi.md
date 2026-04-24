---
title: "Tiedostojen siirtäminen tietokoneelta iPhoneen SMB-protokollalla"
description: "Opi siirtämään ja käyttämään suuria tiedostoja Macilta tai Windows PC:ltä iPhoneen tai iPadiin Evermusicin ja SMB-protokollan avulla. Vaiheittainen opas saumattomaan suoratoistoon ja tiedostonhallintaan."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["tiedostojen siirto iPhoneen SMB", "PC-musiikin suoratoisto iPhonessa", "Macin yhdistäminen iPhoneen SMB", "Evermusic SMB-asetukset", "tietokoneen tiedostojen käyttö iPhonella", "Windows-musiikin jakaminen iOS", "SMB-tiedostosiirto Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Tiivistelmä:** Käytä Evermusicia iPhonessa tai iPadissa päästäksesi käsiksi Macille tai Windows PC:lle tallennettuihin tiedostoihin paikallisverkon kautta SMB:n avulla. Ei kaapeleita, ei iTunesia, ei pilvilatausta tarvita. Ota tiedostojen jakaminen käyttöön tietokoneellasi, yhdistä sovelluksessa ja selaa tai toista tiedostojasi langattomasti.

Onko sinulla laaja kokoelma suuria tiedostoja MAC- tai PC-tietokoneellasi ja haluatko käyttää niitä vaivattomasti iPhonesta tai iPadista? Sovelluksemme tarjoavat yksinkertaisen ratkaisun.

Seuraa näitä vaiheita mahdollistaaksesi saumattoman pääsyn tietokoneesi ja iOS-laitteesi välillä SMB-protokollan avulla:

## Vaihe 1: SMB-protokollan käyttöönotto tietokoneellasi

**MAC-tietokoneelle:**

1. Avaa "Järjestelmäasetukset" MAC-tietokoneellasi.
2. Napsauta "Jakaminen".
3. Ota käyttöön "Tiedostojen jakaminen" -palvelu.
4. Lisää musiikkikansiosi "Jaetut kansiot" -osioon. Lisää käyttäjä ja valitse käyttöoikeustaso (Luku ja kirjoitus tai Vain luku). Voit valita "Kaikki: Vain luku" lisätylle musiikkikansiolle.

   ![Macin asetusruutu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Muista tietokoneen URL (smb://192.168.xx.xx), sillä tarvitset sitä seuraavissa vaiheissa.
6. Napsauta "Asetukset" ja ota käyttöön "Jaa tiedostoja ja kansioita SMB:n kautta".

   ![Macin tiedostojen jakamisen ruutu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Ota käyttöön "Windows-tiedostojen jakaminen" käytettävissä oleville tileille.

   ![Macin SMB-jakamisruutu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Windows PC:lle:**

1. Napsauta hiiren oikealla painikkeella musiikkikansiotasi.
2. Valitse "Ominaisuudet".
3. Siirry "Jakaminen"-välilehdelle.
4. Napsauta "Jaa..."
5. Valitse henkilöt, joiden kanssa haluat jakaa kansion, ja määritä käyttöoikeustaso. Voit valita "Kaikki: Luku" valitulle musiikkikansiolle.

   ![Windowsin SMB-jakamisruutu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Napsauta "Valmis".
7. Napsauta "Valmis" "Tiedostojen jakaminen" -ikkunassa ja muista kansion polku.

   ![Windowsin SMB-jaettu kansio](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Vaihe 2: iOS-laitteen yhdistäminen

1. Avaa sovellus iPhonessa tai iPadissa.
2. Siirry "Yhteydet"-välilehdelle.

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusicin Yhteydet-ruutu"
  caption="Evermusicin Yhteydet-ruutu"
  width="400"
>}}

*Jos tietokoneesi näkyy "Saatavilla olevat laitteet" -osiossa:*

Jos tietokoneesi on näkyvissä "Saatavilla olevat laitteet" -osiossa ja valitsit "Kaikki: Vain luku" edellisessä vaiheessa, napauta yksinkertaisesti tietokonettasi ja se yhdistyy automaattisesti.

*Jos tietokoneesi ei näy automaattisesti:*

1. Napauta "Yhdistä pilvipalvelu".
2. Valitse "SMB" "Yhdistä pilvipalvelu" -ruudussa.

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusicin Yhdistä pilvipalvelu -ruutu"
  caption="Evermusicin Yhdistä pilvipalvelu -ruutu"
  width="400"
>}}

3. "SMB-yhteys" -ruudussa syötä palvelimen URL jaetun kansion polun kanssa. Voit käyttää palvelimen nimeä tai palvelimen IP-osoitetta:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Syötä käyttäjätunnuksesi ja salasanasi tai jätä nämä kentät tyhjiksi, jos valitsit "Kaikki: Vain luku" edellisessä vaiheessa.
5. "WORKGROUP"-kenttä on valinnainen ja sitä tulisi käyttää, jos sinulla on Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusicin SMB-yhteysruutu"
  caption="Evermusicin SMB-yhteysruutu"
  width="400"
>}}

6. Kun olet yhdistänyt tietokoneesi SMB-protokollalla, se näkyy "Pilvipalvelut"-osiossa "Yhteydet"-ruudussa.
7. Avaa yhdistetty palvelu ja siirry haluttuun kansioon.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Avattu SMB-kansio Evermusicissa"
  caption="Avattu SMB-kansio Evermusicissa"
  width="400"
>}}

8. Voit käyttää sisäänrakennettua tiedostonhallintaa tiedostojesi muokkaamiseen tarpeen mukaan.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusicin tiedostonhallinta"
  caption="Evermusicin tiedostonhallinta"
  width="400"
>}}

## Vaihe 3: SMB2-kansioiden erikoismerkkiongelma

Joskus saatat kohdata ongelmia kansioiden kanssa, jotka sisältävät erikoismerkkejä SMB2-protokollaa käytettäessä. Tässä muutamia vaiheita ongelman ratkaisemiseksi:

1. **SMB 1:n käyttöönotto:**  
   • Väliaikaisena ratkaisuna kokeile SMB 1:n käyttöönottoa palvelimellasi ja sovelluksen asetuksissa. Tämä voi auttaa ohittamaan erikoismerkkeihin liittyvät ongelmat kansioiden nimissä.

2. **Järjestelmän tiedostojen avausvalikon käyttö:**  
   • Siirry kohtaan "Paikalliset tiedostot".  
   • Vieritä alas "Tiedostot tällä laitteella" -osioon.  
   • Napauta "Avaa tiedostoja..." tai "Avaa kansioita...".  
   • Etsi palvelimesi ja valitse tarvitsemasi tiedostot tai kansiot.  
   • Napauta "Avaa" vahvistaaksesi valintasi.

3. **Vaihtoehtoiset protokollat:**  
   • Jos ongelma jatkuu, harkitse yhdistämistä NAS-laitteeseesi WebDAV- tai DLNA-protokollien avulla, jos NAS-laitteesi tukee näitä vaihtoehtoja. Nämä protokollat saattavat käsitellä erikoismerkkejä paremmin.

Näitä vaiheita seuraamalla voit lieventää erikoismerkkeihin liittyviä ongelmia kansioiden nimissä SMB2-protokollaa käytettäessä.

## Yhteenveto

Näillä vaiheilla voit vaivattomasti käyttää laajaa tiedostokokoelmaasi MAC- tai PC-tietokoneeltasi iPhonella tai iPadilla sovelluksiemme avulla.

## Usein kysytyt kysymykset

{{% details title="Voinko käyttää tietokoneeni tiedostoja iPhonesta ilman iTunesia?" closed="true" %}}
Kyllä. Evermusic yhdistää tietokoneeseen SMB:n kautta paikallisessa Wi-Fi-verkossa. iTunes- tai Finder-synkronointia ei tarvita. Ota tiedostojen jakaminen käyttöön PC:lläsi ja yhdistä suoraan sovelluksesta.
{{% /details %}}

{{% details title="Toimiiko SMB-tiedostojen käyttö internetin kautta?" closed="true" %}}
Ei. SMB on paikallisverkkoprotokolla. iPhonesi ja tietokoneesi on oltava samassa Wi-Fi-verkossa. Etäkäyttöä varten lataa tiedostot pilvipalveluun kuten Google Drive tai Dropbox ja yhdistä siihen Evermusicissa.
{{% /details %}}

{{% details title="Mitä tiedostotyyppejä voin käyttää SMB:n kautta?" closed="true" %}}
Evermusic tukee MP3-, FLAC-, AAC-, WAV-, AIFF-, OGG-, WMA-, ALAC- ja muita äänimuotoja. Voit myös selata ja hallita muita kuin äänitiedostoja sisäänrakennetun tiedostonhallinnan avulla.
{{% /details %}}

{{% details title="Voinko siirtää tiedostoja NAS-laitteesta iPhoneen SMB:n avulla?" closed="true" %}}
Kyllä. Useimmat NAS-laitteet (Synology, QNAP, WD My Cloud ja muut) tukevat SMB:tä. Yhdistä NAS-laitteeseesi samoja vaiheita käyttäen tässä oppaassa.
{{% /details %}}

{{% details title="Pitääkö minun kopioida tiedostot iPhoneen toistaakseni niitä?" closed="true" %}}
Ei. Evermusic suoratoistaa tiedostot suoraan tietokoneeltasi tai NAS-laitteestasi verkon kautta. Tiedostoja ei kopioida iPhoneen, ellet valitse ladata niitä offline-toistoa varten.
{{% /details %}}

{{% details title="Onko SMB-tiedostojen jakaminen turvallista?" closed="true" %}}
SMB-tiedostojen jakaminen toimii vain paikallisverkossasi. Muut laitteet eri verkoissa eivät pääse käsiksi jaettuihin kansioihisi. Lisäturvallisuutta varten käytä käyttäjätunnusta ja salasanaa anonyymin (Kaikki) käytön sijaan.
{{% /details %}}
