---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: 'Usein kysytyt kysymykset'
description: 'Löydä vastauksia yleisiin kysymyksiin Evermusic-, Flacbox-, Evervideo- ja Evertag-sovelluksista. Tutustu ominaisuuksiin kuten pilvisuoratoisto, tiedostonhallinta, toistoasetukset, metatietojen muokkaus ja paljon muuta.'
keywords: [
  "Evermusic UKK", "Flacbox tuki", "Evervideo ohje", "Evertag kysymykset",
  "kuinka käyttää Evermusicaa", "pilvimusiikin soittimen vianmääritys", "offline-toiston opas",
  "äänitunnisteiden editorin tuki", "videosuoratoiston ongelmat", "tiedostonsiirron opas"
]
tags: [
  "UKK", "ohje", "tuki", "evermusic", "flacbox", "evervideo", "evertag",
  "pilviasennus", "toistongelmat", "tiedostonhallinta", "metatietojen muokkaus",
  "vianmääritys", "offline-tila", "musiikkisoitin", "videosoitin"
]
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## Opi käyttämään sovelluksiamme

Etsitkö vastauksia tai apua jonkin sovelluksemme käyttöön? Olet oikeassa paikassa.

UKK-sivumme auttavat sinua yhdistämään pilvivarastoon, hallitsemaan musiikki- ja videotiedostoja, määrittämään offline-toiston, säätämään ekvalisaattoriasetuksia, korjaamaan metatietoja ja paljon muuta.

Tutustu sovelluksesi UKK:hon alla aloittaaksesi, tai selaa yleisiä kysymyksiä ja vastauksia, joita olemme saaneet käyttäjien sähköposteista.

## Valitse sovelluksesi

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="Toista 360°-videoita, suoratoista iCloudista, katso tekstityksen kanssa, käytä videoekvalisaattoria, järjestä sisältö soittolistoilla ja lataa videoita offline-katselua varten."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="Pilvimusiikin soitin offline-tilalla, ääniekvalisaattorilla, crossfadella, taukottomalla toistolla, soittolistojen hallinnalla, täydellisellä musiikkikirjastolla ja sisäänrakennetulla tiedostonhallinnalla."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="Korkearesoluutioinen äänisoitin iPhonelle ja Macille. Kuuntele häviöttömiä muotoja kuten FLAC, ALAC, APE ja DSD. Hienosäädä lähtöä edistyneillä ääniasetuksilla."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="Älykäs musiikkitunnisteiden muokkain erätoiminnolla. Korjaa puuttuvat metatiedot, albumin kansikuvat ja muuta. Muokkaa ID3-, FLAC-, APE-tunnisteita — yli 120 kenttää tuettu." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## Yleiset ongelmat ja vastaukset

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="Miksi en pysty kirjautumaan pCloudiin vanhemmalla iOS-versiolla (15.8.4)?" closed="true" %}}
pCloudin verkkokirjautumissivu ei välttämättä näy oikein vanhemmilla iOS-versioilla, kuten 15.8.4, mikä estää sähköpostin ja salasanan syöttämisen pilviyhteysruudulla.<br><br>

Vaihtoehtoisena ratkaisuna voit käyttää **WebDAV**-protokollaa, jota pCloud tukee ja joka toimii luotettavasti kaikilla iOS-versioilla.

**WebDAV-asetukset:**<br>
- **Yhdysvaltain palvelimet:** `https://webdav.pcloud.com`  
- **Euroopan palvelimet:** `https://ewebdav.pcloud.com`  
- **Käyttäjänimi:** pCloud-sähköpostiosoitteesi  
- **Salasana:** pCloud-tilisi salasana  

Avaa sovellus → Yhteydet → Yhdistä pilvitallennustilaan → Valitse **WebDAV** → Syötä tunnistetietosi ja palvelimen URL.

Tällä tavalla voit yhdistää pCloud-tallennustilaan ja käyttää tiedostojasi ongelmitta vanhemmilla laitteilla.
{{% /details %}}

{{% details title="Kuinka soitan musiikkia AirPlayn kautta Macilta (macOS)?" closed="true" %}}
Sovelluksen macOS-versio ei sisällä sisäänrakennettuja AirPlay-, Chromecast- tai Bluetooth-yhteyspainikeita kuten iOS.<br><br>

Käytä **AirPlayta** MacBook Prossa seuraavilla vaiheilla:

1. Siirry näytön **oikeaan yläkulmaan** ja avaa **Ohjauskeskus** (kellon lähellä).  
2. Napsauta **Ääni/Äänenvoimakkuus**-kuvaketta.  
3. Seuraavassa näkymässä napsauta **AirPlay** nähdäksesi luettelon kaikista käytettävissä olevista AirPlay-laitteista.  
4. Valitse haluamasi laite aloittaaksesi musiikin suoratoiston.  

Tämä ohjaa kaiken järjestelmääänen (mukaan lukien Evermusicista tai Flacboxista) valitsemaasi AirPlay-laitteeseen.
{{% /details %}}

{{% details title="Miksi Premium-ostokseni ei aktivoitunut Macilla, vaikka ostin sen iPhonella?" closed="true" %}}
Elinikäiset ostokset ja tilaukset synkronoidaan iOS:n ja Macin välillä **iCloudin** kautta.<br><br>

Premiumin aktivoiminen Macilla:<br>
- Varmista, että sovelluksen uusin versio on asennettu molemmille laitteille<br>
- Ota **iCloud** käyttöön molemmilla laitteilla<br>
- Käynnistä sovellus iOS-laitteellasi ja odota 1 minuutti, jotta ostotiedot latautuvat<br>
- Asenna sovellus Macille App Storesta käyttäen **samaa Apple ID:tä**<br>
- Käynnistä sovellus ja odota muutama sekunti tietojen synkronointia varten<br>
- Vaihtoehtoisesti napauta **Palauta ostokset** sovelluksen asetuksissa molemmilla laitteilla<br><br>

Premium-ominaisuuksien pitäisi aktivoitua automaattisesti Macilla.
{{% /details %}}

{{% details title="Kuinka voin synkronoida soittolistat automaattisesti laitteiden välillä?" closed="true" %}}
Tällä hetkellä **automaattista synkronointia** ei ole soittolistoille.<br><br>

Voit käyttää yhtä seuraavista vaihtoehdoista:<br>
- **Varmuuskopiointi ja palautus** sovelluksen asetuksista [Musiikin siirtäminen laitteiden välillä Evermusicissa: vaiheittainen opas](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **Vie soittolista M3U-muotoon** ja tuo se toisella laitteella:<br>
  - [Soittolistojen vieminen](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [Soittolistojen tuominen](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **Arkistoi soittolista tai albumit** ja siirrä ZIP-tiedostona:<br>
  - [Soittolistojen arkistointiopas](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="Onko sovellusten käyttö turvallista? Voinko poistaa analytiikan käytöstä?" closed="true" %}}
Kyllä, yksityisyytesi on korkein prioriteettimme.<br><br>

- Kaikki tiedot — musiikkitiedostot, asetukset, pilvikirjautumiset — pysyvät laitteellasi<br>
- Kirjautumistiedot tallennetaan turvallisesti **iOS Keychainiin**<br>
- Keräämme vain anonyymejä kaatumis- ja käyttöraportteja<br>
- Voit kieltäytyä kohdassa **Sovelluksen asetukset → Analytiikka**<br><br>

Lisätietoja:<br>
- [Tietosuojakäytäntö](/legal/privacy-policy/)<br>
- [Apple Keychain -suojaus](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

Käytettäessä personoituja mainoksia Google Mobile Ads edellyttää suostumusasetusten näyttämistä.<br>
Premium-käyttäjät eivät näe mainoksia ja mainos-SDK on täysin poistettu käytöstä.
{{% /details %}}

{{% details title="Tukevatko sovelluksenne perhejakamista?" closed="true" %}}
Kyllä, perhejakaminen on tuettu.<br><br>

Sovelluksen sisäisten ostojen jakaminen:<br>
- Varmista, että ostos on asetettu jaettavaksi perheryhmäsi kanssa<br>
- Perheenjäsenen laitteella siirry kohtaan **Asetukset > Ostokset > Palauta ostokset**<br>
- Tämä pyytää ostotiedot Applen palvelimilta ja aktivoi ne laitteella
{{% /details %}}

{{% details title="Kuinka nopeuttaa metatietojen ja pilven synkronointia?" closed="true" %}}
Synkronointinopeuden parantamiseksi ota käyttöön taustatyöt:<br><br>

- **Asetukset → Musiikkikirjasto → Metatietojen luku → Metatietojen luku taustalla**<br>
- **Asetukset → Musiikkikirjasto → Online-musiikkisynkronointi → Taustasynkronointi**<br><br>

Lisäksi macOS:llä lisää metatietojen lukunopeutta kohdassa **Asetukset → Musiikkikirjasto**.<br>
Jos soitin on aktiivinen (ääni toistuu), iOS ei keskeytä sovellusta, mikä mahdollistaa jatkuvan synkronoinnin.
{{% /details %}}

{{% details title="Kuinka voin peruuttaa tilaukseni?" closed="true" %}}
Voit peruuttaa tilauksesi Applen virallisten ohjeiden mukaisesti:<br>
👉 [Tilauksen peruuttaminen](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="Kuinka yhdistän ja suoratoistan ääntä WD MyCloud EX2 Ultrasta?" closed="true" %}}

Kun lisäät yhteyden sovellukseen kohdassa **Yhteydet > Yhdistä pilvitallennustilaan > My Cloud Home**, se on virallisesti suunniteltu tukemaan **WD MyCloud Home** -laitteita.<br>
WD MyCloud EX2 Ultra käyttää sovelluksille rajoitettua käyttöoikeutta.<br><br>

Jos olet kuitenkin onnistuneesti yhdistänyt **WD MyCloud EX2 Ultraan**, **WD MyCloud Mirroriin** tai muuhun **WD MyCloud** -tallennusmalliin, voit silti käyttää sitä seuraavalla ratkaisulla:<br><br>

1. Avaa **Yhteydet → Yhdistä pilvitallennustilaan → My Cloud Home**<br>
2. Luo kansio sisäänrakennetun tiedostonhallinnan avulla<br>
3. Lataa musiikkitiedostoja tähän kansioon<br>
4. Ne tallennetaan "hiekkalaatikkoon", johon vain sovellus pääsee käsiksi<br>
5. Voit nyt suoratoistaa tai ladata ne suoraan<br><br>

⚠️ Vain sovelluksen kautta luodut kansiot ovat käytettävissä NAS-laitteelta.
{{% /details %}}

{{% details title="Kuinka yhdistän Koofr.eu:hun?" closed="true" %}}
Voit yhdistää Koofrin käyttämällä **WebDAViä**.<br><br>

- Koofrin WebDAV-asennusopas: [koofr.eu-blogi](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Evermusic/Flacbox WebDAV-opas: [NAS-tallennustilan yhdistäminen WebDAVin avulla ja musiikin kuuntelu iPhonella tai Macilla](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="Mitkä ovat sovelluksen URL-kaavat?" closed="true" %}}
Tuetut kaavat:<br><br>

**Evermusic**<br>
- iOS (sininen kuvake): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (punainen kuvake): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="Musiikki lakkaa soimasta, kun sovellus on taustalla — miten korjaan sen?" closed="true" %}}
Jos sovellus kaatuu tai pysähtyy taustalla:<br>
- Siirry kohtaan **Asetukset > Musiikkikirjasto > Online-musiikkisynkronointi > Taustasynkronointi → Poista käytöstä**<br>
- **Asetukset > Musiikkikirjasto > Metatietojen luku > Metatietojen luku taustalla → Poista käytöstä**<br>
- **Asetukset > Tiedostonhallinta > Taustasiirrot → Poista käytöstä**
{{% /details %}}

{{% details title="Taukoton toisto ei toimi — miten korjaan sen?" closed="true" %}}
Taukoton toisto riippuu iOS-versiosta ja äänimoottorista.<br>
Kokeile vaihtaa äänimoottoria:<br>
- Siirry kohtaan **Asetukset → Äänisoistin → Yleiset → Ääniprosessori**<br>
- Valitse **Core Audio** paremman taukottoman toiston tuen saamiseksi
{{% /details %}}

{{% details title="Miksi sovellus näyttää vain 100 kohdetta luettelossa?" closed="true" %}}
Sovellus käyttää sivutusta suorituskyvyn parantamiseksi.<br>
Sen poistaminen käytöstä:<br>
- Siirry kohtaan **Asetukset → Personointi → Sisällön latausraja → Poistettu käytöstä**<br>
Nyt kaikki kohteet ladataan kerralla.
{{% /details %}}

{{% details title="Miksi metatiedoissa on outoja merkkejä?" closed="true" %}}
Kokeile ottaa metatietojen normalisointi käyttöön:<br>
- **Asetukset → Musiikkikirjasto → Metatietojen luku → Normalisoi metatietojen koodaus**
{{% /details %}}

{{% details title="Miksi sovellus ei pysty lukemaan erikoismerkkejä sisältäviä kansioiden nimiä?" closed="true" %}}
Tämä on tunnettu ongelma **SMB2-protokollan** kanssa.<br><br>

Kokeile seuraavia ratkaisuja:<br>
- Ota **SMB1** käyttöön palvelimellasi ja sovelluksen asetuksissa<br>
- Käytä **järjestelmän tiedostonvalitsinta**:<br>
  - Siirry kohtaan **Paikalliset tiedostot > Tiedostot tässä laitteessa > Avaa tiedostoja...**<br>
  - Valitse kansiot/tiedostot Applen natiivivalikon avulla<br><br>

Vaihtoehtoisesti yhdistä käyttäen **WebDAViä** tai **DLNAa**, jos NAS-laitteesi tukee niitä.
{{% /details %}}

{{% details title="Kuinka lataan ja hallinnoin musiikkia iCloudissa?" closed="true" %}}
– **Kuinka lataan musiikkia iCloudiin?**  <br>
Siirry selaimessa osoitteeseen [https://www.icloud.com](https://www.icloud.com), luo kansio ja lataa musiikkitiedostosi suoraan Macilta tai PC:ltä.<br>

– **Kuinka hallinnoin iCloud-tallennustilaa?**  <br>
Sinulla on kaksi vaihtoehtoa:  <br>
1. Käytä [https://www.icloud.com](https://www.icloud.com) selaimessa tiedostojen järjestämiseen, lataamiseen tai poistamiseen.<br>  
2. Sovelluksessa, kun olet yhdistänyt iCloudiin kohdassa **Yhteydet → Yhdistä pilvitallennustilaan → iCloud Drive**, käytä sisäänrakennettua tiedostonhallintaa tiedostojen lataamiseen, lataamiseen, kansioiden nimeämiseen tai tiedostojen poistamiseen suoraan iCloud-tallennustilastasi — tallentamatta niitä laitteeseesi.<br>

⚠️ Ole varovainen poistaessasi tiedostoja. Sovellus poistaa ne pysyvästi (ne eivät siirry roskakoriin eikä niitä voi palauttaa).<br>

Lue lisää täältä: [Musiikin suoratoistaminen iCloud Drivesta iPhonella tai Macilla](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="Kuinka voin siirtää 10 Gt:n musiikkikirjastoni Windows 11:stä iPhonelleni offline-toistoa varten?" closed="true" %}}

Sinulla on useita luotettavia vaihtoehtoja musiikkikirjastosi siirtämiseksi Windows 11 -tietokoneeltasi iPhonellesi ja sen käyttämiseksi offline-tilassa sovelluksessa. Valitse sinulle parhaiten sopiva menetelmä:

1. **Kaapeliyhteyden avulla (suositellaan suurille kirjastoille)**  <br>
   Käytä **Apple Devices** -sovellusta Windows 11:ssä tiedostojen siirtämiseen suoraan iPhonelle USB:n kautta.  
   Seuraa Applen ohjetta täältä:  
   https://support.apple.com/en-ph/120402 <br>

2. **Langattomasti Wi-Fi Driven kautta**  <br>
   Ota sovelluksessa käyttöön **WiFi Drive** -ominaisuus ja lataa musiikkisi tietokoneen selaimen kautta.  
   Vaiheittaiset ohjeet täältä:  
   [Musiikkitiedostojen siirtäminen tietokoneelta iPhonelle ilman iTunesia WiFi-Drivella](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **Langattomasti DLNA-palvelimen avulla**  <br>
   Käynnistä DLNA-mediapalvelin Windows-tietokoneellasi ja suoratoista tai siirrä kirjastosi suoraan sovellukseen.  
   Opas:  
   [DLNA-mediapalvelimen ottaminen käyttöön Windows 10:ssä ja musiikin toistaminen iPhonella](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **Langattomasti SMB-tiedostonjakamisen avulla**  <br>
   Ota **SMB-tiedostonjako** käyttöön tietokoneellasi ja yhdistä siihen sovelluksessa selataksesi, ladataksesi tai siirtääksesi tiedostoja kansio kerrallaan.  
   Ohjeet:  
   [Tiedostojen siirtäminen tietokoneelta iPhonelle SMB-protokollan avulla](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ Siirrettäessä suuria kirjastoja (10 Gt+), langallinen USB-siirto on yleensä nopein ja vakain vaihtoehto.

{{% /details %}}

</div>
